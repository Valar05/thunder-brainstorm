"""In-process allowlisted plugin registry. Plugins return data and never receive a shell."""
from dataclasses import dataclass
from typing import Any, Callable
from .canonical import content_hash
from .contracts import ContractError

PluginHandler = Callable[[dict[str, Any]], dict[str, Any]]

@dataclass(frozen=True)
class Plugin:
    manifest: dict[str, Any]
    handler: PluginHandler

class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(self, manifest: dict[str, Any], handler: PluginHandler) -> None:
        missing = {"id", "version", "actions", "capabilities"} - manifest.keys()
        if missing:
            raise ContractError(f"plugin manifest missing: {', '.join(sorted(missing))}")
        if manifest["id"] in self._plugins:
            raise ContractError(f"plugin already registered: {manifest['id']}")
        if not isinstance(manifest["actions"], list) or not manifest["actions"]:
            raise ContractError("plugin must declare at least one action")
        forbidden = {"shell", "subprocess", "network", "raw_filesystem"}
        requested = set(manifest["capabilities"])
        if forbidden & requested:
            raise ContractError(f"forbidden plugin capabilities: {', '.join(sorted(forbidden & requested))}")
        self._plugins[manifest["id"]] = Plugin(dict(manifest), handler)

    def execute(self, plugin_id: str, action: str, arguments: dict[str, Any]) -> dict[str, Any]:
        plugin = self._plugins.get(plugin_id)
        if plugin is None:
            raise ContractError(f"unknown plugin: {plugin_id}")
        if action not in plugin.manifest["actions"]:
            raise ContractError(f"plugin action not allowed: {plugin_id}.{action}")
        output = plugin.handler({"action": action, "arguments": dict(arguments)})
        if not isinstance(output, dict):
            raise ContractError("plugin output must be an object")
        return {"plugin": plugin_id, "version": plugin.manifest["version"], "action": action, "output": output, "receipt": content_hash(output)}

    def manifests(self) -> list[dict[str, Any]]:
        return [dict(self._plugins[key].manifest) for key in sorted(self._plugins)]
