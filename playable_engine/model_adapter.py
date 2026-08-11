"""Local model proposal boundary. Accepted calls are validated, hashed, and replayable."""
import json
from typing import Callable
from .canonical import content_hash
from .contracts import ContractError, validate_envelope

class FunctionGemmaBoundary:
    """Wrap an embedded runner callable without granting execution capabilities."""
    def __init__(self, runner: Callable[[str, str], str], model_receipt: dict):
        missing = {"checkpoint_hash", "tokenizer_hash", "runtime", "decoding"} - model_receipt.keys()
        if missing:
            raise ContractError(f"model receipt missing: {', '.join(sorted(missing))}")
        self._runner = runner
        self.model_receipt = dict(model_receipt)

    def propose(self, prompt: str, mode: str) -> dict:
        raw = self._runner(prompt, mode)
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ContractError("model output is not JSON") from exc
        validate_envelope(value)
        if value["mode"] != mode:
            raise ContractError(f"model returned mode {value['mode']!r} for requested mode {mode!r}")
        expected_prompt_hash = content_hash(" ".join(prompt.split()))
        if value["provenance"]["prompt_hash"] != expected_prompt_hash:
            raise ContractError("model prompt hash does not match the request")
        value["provenance"]["model"] = self.model_receipt
        value["provenance"]["accepted_envelope_hash"] = content_hash(value)
        return value
