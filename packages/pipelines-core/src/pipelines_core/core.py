"""Bounded in-memory execution of explicitly supplied, trusted pipeline stages.

Callbacks are application code, not a sandbox. No declaration is activated and
no data is fetched, persisted, promoted or published by this module.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import re
from typing import Any, Callable, Sequence

MAX_STAGES = 64
MAX_ARTIFACT_BYTES = 4 * 1024 * 1024
MAX_TOTAL_ARTIFACT_BYTES = 16 * 1024 * 1024
MAX_JSON_NODES = 100_000
MAX_JSON_DEPTH = 48
_NAME = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
_DIGEST = re.compile(r"sha256:[0-9a-f]{64}\Z")


class PipelineError(ValueError):
    """A finite setup or artifact error, without embedding input contents."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class Stage:
    """A trusted transform and optional raising validator, with explicit inputs.

    The transform receives independent JSON copies of ``input`` and its named
    ``dependencies``. A validator must return None or raise to reject an output.
    """

    name: str
    transform: Callable[[dict[str, Any]], Any]
    requires: tuple[str, ...] = ()
    validate: Callable[[Any], None] | None = None


def canonical_bytes(value: Any) -> bytes:
    """Reject non-JSON values, cycles, non-finite numbers and oversized trees."""
    nodes = 0

    def visit(item: Any, depth: int) -> None:
        nonlocal nodes
        nodes += 1
        if nodes > MAX_JSON_NODES or depth > MAX_JSON_DEPTH:
            raise PipelineError("ARTIFACT_STRUCTURE_LIMIT")
        kind = type(item)
        if kind is dict:
            if any(type(key) is not str for key in item):
                raise PipelineError("ARTIFACT_KEYS_INVALID")
            for child in item.values():
                visit(child, depth + 1)
        elif kind is list:
            for child in item:
                visit(child, depth + 1)
        elif kind is float:
            if not math.isfinite(item):
                raise PipelineError("ARTIFACT_NONFINITE")
        elif kind not in (str, bool, int, type(None)):
            raise PipelineError("ARTIFACT_NOT_JSON")

    visit(value, 0)
    try:
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError, UnicodeError, RecursionError) as exc:
        raise PipelineError("ARTIFACT_NOT_JSON") from exc
    if len(raw) > MAX_ARTIFACT_BYTES:
        raise PipelineError("ARTIFACT_BYTE_LIMIT")
    return raw


def _digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _references(values: Sequence[str]) -> list[str]:
    if not isinstance(values, (tuple, list)) or len(values) > MAX_STAGES:
        raise PipelineError("REFERENCES_INVALID")
    if any(type(value) is not str or not 0 < len(value) <= 512
           or any(ord(char) < 32 for char in value) for value in values):
        raise PipelineError("REFERENCES_INVALID")
    if len(set(values)) != len(values):
        raise PipelineError("REFERENCES_INVALID")
    return sorted(values)


def _ordered(stages: Sequence[Stage]) -> list[Stage]:
    if not isinstance(stages, (tuple, list)) or not 1 <= len(stages) <= MAX_STAGES:
        raise PipelineError("STAGE_COUNT_INVALID")
    by_name: dict[str, Stage] = {}
    for stage in stages:
        if (not isinstance(stage, Stage) or type(stage.name) is not str
                or not _NAME.fullmatch(stage.name) or stage.name in by_name
                or not callable(stage.transform)
                or (stage.validate is not None and not callable(stage.validate))):
            raise PipelineError("STAGE_INVALID")
        if (type(stage.requires) is not tuple
                or any(type(name) is not str for name in stage.requires)
                or len(set(stage.requires)) != len(stage.requires)):
            raise PipelineError("DEPENDENCIES_INVALID")
        by_name[stage.name] = stage
    if any(name not in by_name for stage in stages for name in stage.requires):
        raise PipelineError("DEPENDENCY_MISSING")
    ordered: list[Stage] = []
    complete: set[str] = set()
    while len(complete) < len(stages):
        ready = sorted(name for name, stage in by_name.items()
                       if name not in complete and set(stage.requires) <= complete)
        if not ready:
            raise PipelineError("DEPENDENCY_CYCLE")
        for name in ready:
            ordered.append(by_name[name])
            complete.add(name)
    return ordered


def run_pipeline(stages: Sequence[Stage], value: Any, *, spec_hash: str,
                 code_ref: str, source_descriptor_refs: Sequence[str] = (),
                 validation_refs: Sequence[str] = ()) -> dict[str, Any]:
    """Execute a deterministic DAG once and emit schema-shaped RunReceipts.

    Invalid topology fails before any callback. Failed stages block descendants;
    independent branches still run. Receipts describe computed in-memory bytes,
    not durable artifacts, policy decisions, evidence closure or released data.
    Caller-supplied references are declarations, not authenticated approvals.
    """
    ordered = _ordered(stages)
    if type(spec_hash) is not str or not _DIGEST.fullmatch(spec_hash):
        raise PipelineError("SPEC_HASH_INVALID")
    code_refs = _references([code_ref])
    sources, validations = _references(source_descriptor_refs), _references(validation_refs)
    input_raw = canonical_bytes(value)
    input_digest = _digest(input_raw)
    manifest = {
        "engine_version": 1, "spec_hash": spec_hash, "code_ref": code_refs[0],
        "input": input_digest, "source_descriptor_refs": sources,
        "validation_refs": validations,
        "stages": [{"name": stage.name, "requires": sorted(stage.requires)} for stage in ordered],
    }
    run_id = "run:" + hashlib.sha256(canonical_bytes(manifest)).hexdigest()
    total_bytes = len(input_raw)
    artifacts: dict[str, bytes] = {}
    failed: set[str] = set()
    steps: list[dict[str, Any]] = []
    for stage in ordered:
        inputs = [input_digest] + [_digest(artifacts[name])
                                  for name in sorted(stage.requires) if name in artifacts]
        reason = "COMPLETED"
        if any(name in failed for name in stage.requires):
            reason = "DEPENDENCY_FAILED"
        else:
            context = {"input": json.loads(input_raw), "dependencies": {
                name: json.loads(artifacts[name]) for name in sorted(stage.requires)}}
            try:
                raw = canonical_bytes(stage.transform(context))
                if total_bytes + len(raw) > MAX_TOTAL_ARTIFACT_BYTES:
                    raise PipelineError("ARTIFACT_TOTAL_BYTE_LIMIT")
                if stage.validate is not None:
                    if stage.validate(json.loads(raw)) is not None:
                        raise PipelineError("VALIDATOR_CONTRACT_INVALID")
            except PipelineError as exc:
                # Only this module's finite errors are exposed, never callback text.
                reason = exc.code if exc.code in {
                    "ARTIFACT_STRUCTURE_LIMIT", "ARTIFACT_KEYS_INVALID",
                    "ARTIFACT_NONFINITE", "ARTIFACT_NOT_JSON", "ARTIFACT_BYTE_LIMIT",
                    "VALIDATOR_CONTRACT_INVALID", "ARTIFACT_TOTAL_BYTE_LIMIT"} else "STAGE_REJECTED"
            except Exception:
                reason = "STAGE_EXECUTION_FAILED"
            else:
                artifacts[stage.name] = raw
                total_bytes += len(raw)
        succeeded = stage.name in artifacts
        if not succeeded:
            failed.add(stage.name)
        receipt = {"run_id": run_id + ":" + stage.name, "stage": stage.name,
                   "inputs": inputs,
                   "outputs": [_digest(artifacts[stage.name])] if succeeded else [],
                   "code_ref": code_ref, "spec_hash": spec_hash,
                   "source_descriptor_refs": sources.copy(),
                   "validation_refs": validations.copy(),
                   "outcome": "SUCCESS" if succeeded else "FAIL"}
        steps.append({"name": stage.name, "reason_code": reason, "receipt": receipt})
    outcome = "SUCCESS" if not failed else ("PARTIAL" if artifacts else "FAIL")
    return {"run_id": run_id, "outcome": outcome, "steps": steps,
            "artifacts": {name: json.loads(raw) for name, raw in artifacts.items()},
            "execution_scope": "IN_MEMORY", "review_required": True,
            "source_admitted": False, "release_authorized": False,
            "publication_authorized": False}
