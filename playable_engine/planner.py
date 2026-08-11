"""Atom-preserving campaign planner and deterministic DAG validator."""
import re
from typing import Any
from .canonical import content_hash
from .contracts import ContractError

def atomize(prompt: str) -> list[dict[str, str]]:
    normalized = re.sub(r"\s+", " ", prompt).strip()
    if not normalized:
        raise ContractError("prompt is empty")
    chunks = [chunk.strip(" ,.") for chunk in re.split(r"(?:[.;!?]+|\bthen\b|\band also\b|\bplus\b)", normalized, flags=re.I) if chunk.strip(" ,.")]
    return [{"id": f"A{index:03d}", "text": text} for index, text in enumerate(chunks, 1)]

def build_plan(prompt: str) -> dict[str, Any]:
    atoms = atomize(prompt)
    tasks = []
    for index, atom in enumerate(atoms, 1):
        task_id = f"T{index:03d}"
        tasks.append({
            "id": task_id,
            "owner": "campaign-worker",
            "action": "materialize_atom",
            "atom_ids": [atom["id"]],
            "inputs": {"prompt_atom": atom["text"], "input_hash": content_hash(atom)},
            "reads": [],
            "writes": [f"artifacts/{task_id}.json"],
            "output": f"artifacts/{task_id}.json",
            "verifier": {"kind": "canonical_hash", "required": True},
            "dependencies": [],
            "parallel_group": "atom-materialization",
            "idempotency_key": content_hash({"task": task_id, "atom": atom}),
            "failure": {"stop": "park_branch", "retry": 1, "rollback": "discard_isolated_output"},
            "merge_handoff": "G001",
        })
    plan = {
        "version": 1,
        "prompt_hash": content_hash(prompt),
        "atoms": atoms,
        "tasks": tasks,
        "merge_gates": [{"id": "G001", "depends_on": [task["id"] for task in tasks], "checks": ["all_atoms_covered", "all_receipts_valid", "no_shared_writes"], "output": "campaign/final.json"}],
    }
    validate_plan(plan)
    plan["plan_hash"] = content_hash(plan)
    return plan

def validate_plan(plan: dict[str, Any]) -> dict[str, Any]:
    atoms = {atom["id"] for atom in plan.get("atoms", [])}
    tasks = plan.get("tasks", [])
    task_ids = {task["id"] for task in tasks}
    if len(task_ids) != len(tasks):
        raise ContractError("duplicate task id")
    covered: set[str] = set()
    writers: dict[str, str] = {}
    graph: dict[str, list[str]] = {}
    required = {"owner", "action", "atom_ids", "inputs", "reads", "writes", "output", "verifier", "dependencies", "parallel_group", "idempotency_key", "failure", "merge_handoff"}
    for task in tasks:
        missing = required - task.keys()
        if missing:
            raise ContractError(f"task {task.get('id')} missing: {', '.join(sorted(missing))}")
        covered.update(task["atom_ids"])
        graph[task["id"]] = list(task["dependencies"])
        for dependency in task["dependencies"]:
            if dependency not in task_ids:
                raise ContractError(f"unknown dependency: {dependency}")
        for target in task["writes"]:
            if target in writers:
                raise ContractError(f"shared writable target: {target}")
            writers[target] = task["id"]
    if covered != atoms:
        raise ContractError(f"atom coverage mismatch; missing={sorted(atoms-covered)} extra={sorted(covered-atoms)}")
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        if node in visiting:
            raise ContractError(f"dependency cycle at {node}")
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency)
        visiting.remove(node)
        visited.add(node)
    for node in sorted(graph):
        visit(node)
    return plan
