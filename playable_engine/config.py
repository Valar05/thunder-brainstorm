"""Deterministic configuration packs with explicit extension."""
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable
from .canonical import content_hash
from .contracts import ContractError

def _read(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("version") != 1 or not isinstance(value.get("actions"), dict):
        raise ContractError(f"invalid config pack: {path}")
    return value

def load_config(base: str | Path, extensions: Iterable[str | Path] = ()) -> dict[str, Any]:
    result = deepcopy(_read(Path(base)))
    sources = [str(Path(base))]
    for raw_path in sorted((Path(p) for p in extensions), key=lambda p: p.as_posix()):
        extension = _read(raw_path)
        for namespace in ("actions", "plugins", "profiles"):
            incoming = extension.get(namespace, {})
            target = result.setdefault(namespace, {})
            overlap = set(target) & set(incoming)
            if overlap:
                raise ContractError(f"{raw_path} attempts to replace {namespace}: {', '.join(sorted(overlap))}")
            target.update(deepcopy(incoming))
        sources.append(str(raw_path))
    result["sources"] = sources
    result["config_hash"] = content_hash({k: v for k, v in result.items() if k != "config_hash"})
    return result
