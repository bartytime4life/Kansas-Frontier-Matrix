#!/usr/bin/env python3
"""Validate fixture-only OpenAdrBacklogDisciplineAssessment candidates.

The validator checks caller-supplied synthetic declarations only. It never
reads or mutates a canonical backlog or ADR and never resolves opaque refs.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/governance/open_adr_backlog_discipline_assessment.schema.json"
FIXTURE_DIR = ROOT / "fixtures/contracts/v1/governance/open_adr_backlog_discipline_assessment"
VALID_FIXTURE = FIXTURE_DIR / "valid.json"
CASES = FIXTURE_DIR / "cases.json"
IDENTITY_PREFIX = "kfm:open-adr-backlog:"
MAX_BYTES = 1_048_576
MAX_FINDINGS = 100
ACTIVE_STATES = {"OPEN", "IN_REVIEW", "BLOCKED"}
TERMINAL_STATES = {"RESOLVED", "WITHDRAWN", "SUPERSEDED"}
NON_EFFECTS = (
    "no_adr_creation",
    "no_backlog_mutation",
    "no_owner_assignment",
    "no_decision_approval",
    "no_promotion",
    "no_release",
    "no_publication",
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


def read_json_object(path: Path) -> tuple[dict[str, object] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    if _contains_surrogate(value):
        return None, (Finding("JSON_UNPAIRED_SURROGATE", "/"),)
    return value, ()


def canonical_bytes(value: object) -> bytes:
    if _contains_surrogate(value):
        raise UnicodeError("unpaired surrogate")
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def expected_id(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    return IDENTITY_PREFIX + hashlib.sha256(canonical_bytes(subject)).hexdigest()


def _pointer(parts: Iterable[object]) -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped) if escaped else "/"


def _schema_findings(candidate: object) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema).iter_errors(candidate), MAX_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError):
        return (Finding("SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_FINDINGS]]
    if len(errors) > MAX_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _semantic_findings(candidate: Mapping[str, object]) -> tuple[set[Finding], set[Finding]]:
    deny: set[Finding] = set()
    abstain: set[Finding] = set()
    entries = candidate["entries"]
    review = candidate["review"]
    effects = candidate["effects"]
    assert isinstance(entries, list) and isinstance(review, Mapping) and isinstance(effects, Mapping)

    typed_entries = [entry for entry in entries if isinstance(entry, Mapping)]
    ids = [str(entry["backlog_id"]) for entry in typed_entries]
    if ids != sorted(set(ids)):
        deny.add(Finding("BACKLOG_ENTRIES_NOT_CANONICAL", "/entries"))
    declared_ids = set(ids)

    for index, entry in enumerate(typed_entries):
        state = str(entry["state"])
        backlog_id = str(entry["backlog_id"])
        owner_roles = entry["owner_roles"]
        blocker_refs = entry["blocker_refs"]
        evidence_refs = entry["evidence_refs"]
        for field, value in (
            ("owner_roles", owner_roles),
            ("blocker_refs", blocker_refs),
            ("evidence_refs", evidence_refs),
        ):
            if not _canonical_strings(value):
                deny.add(Finding("BACKLOG_ARRAY_NOT_CANONICAL", f"/entries/{index}/{field}"))

        if state in ACTIVE_STATES:
            if entry["decision_required"] is not True:
                deny.add(Finding("ACTIVE_DECISION_FLAG_INVALID", f"/entries/{index}/decision_required"))
            if not owner_roles:
                abstain.add(Finding("BACKLOG_OWNER_UNKNOWN", f"/entries/{index}/owner_roles"))
            if not evidence_refs:
                abstain.add(Finding("BACKLOG_EVIDENCE_MISSING", f"/entries/{index}/evidence_refs"))
            if state == "BLOCKED" and not blocker_refs:
                deny.add(Finding("BACKLOG_BLOCKER_REQUIRED", f"/entries/{index}/blocker_refs"))
            if state != "BLOCKED" and blocker_refs:
                deny.add(Finding("BACKLOG_BLOCKER_STATE_MISMATCH", f"/entries/{index}/blocker_refs"))
            if entry["superseded_by"] is not None:
                deny.add(Finding("ACTIVE_SUCCESSOR_FORBIDDEN", f"/entries/{index}/superseded_by"))

        if state in TERMINAL_STATES:
            if entry["decision_required"] is not False:
                deny.add(Finding("TERMINAL_DECISION_FLAG_INVALID", f"/entries/{index}/decision_required"))
            if blocker_refs:
                deny.add(Finding("TERMINAL_BLOCKER_FORBIDDEN", f"/entries/{index}/blocker_refs"))
            if not evidence_refs:
                deny.add(Finding("TERMINAL_EVIDENCE_REQUIRED", f"/entries/{index}/evidence_refs"))

        if state == "RESOLVED":
            if entry["candidate_adr_ref"] is None:
                deny.add(Finding("RESOLUTION_ADR_REQUIRED", f"/entries/{index}/candidate_adr_ref"))
            if entry["superseded_by"] is not None:
                deny.add(Finding("RESOLUTION_SUCCESSOR_FORBIDDEN", f"/entries/{index}/superseded_by"))
        elif state == "WITHDRAWN":
            if entry["superseded_by"] is not None:
                deny.add(Finding("WITHDRAWN_SUCCESSOR_FORBIDDEN", f"/entries/{index}/superseded_by"))
        elif state == "SUPERSEDED":
            successor = entry["superseded_by"]
            if successor is None:
                deny.add(Finding("SUPERSEDED_TARGET_REQUIRED", f"/entries/{index}/superseded_by"))
            elif successor == backlog_id:
                deny.add(Finding("SUPERSEDED_SELF_REFERENCE", f"/entries/{index}/superseded_by"))
            elif successor not in declared_ids:
                deny.add(Finding("SUPERSEDED_TARGET_NOT_DECLARED", f"/entries/{index}/superseded_by"))

    index_by_id = {str(entry["backlog_id"]): index for index, entry in enumerate(typed_entries)}
    successors = {
        str(entry["backlog_id"]): str(entry["superseded_by"])
        for entry in typed_entries
        if entry["state"] == "SUPERSEDED"
        and isinstance(entry["superseded_by"], str)
        and entry["superseded_by"] != entry["backlog_id"]
        and entry["superseded_by"] in declared_ids
    }
    visited: set[str] = set()
    for backlog_id in successors:
        chain: list[str] = []
        positions: dict[str, int] = {}
        current = backlog_id
        while current in successors and current not in visited:
            if current in positions:
                for cycle_id in chain[positions[current] :]:
                    deny.add(
                        Finding(
                            "SUPERSESSION_CYCLE",
                            f"/entries/{index_by_id[cycle_id]}/superseded_by",
                        )
                    )
                break
            positions[current] = len(chain)
            chain.append(current)
            current = successors[current]
        visited.update(chain)

    review_refs = review["record_refs"]
    if not _canonical_strings(review_refs):
        deny.add(Finding("REVIEW_RECORDS_NOT_CANONICAL", "/review/record_refs"))
    if review["state"] == "COMPLETE" and not review_refs:
        deny.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))
    elif review["state"] == "PENDING":
        abstain.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review["state"] == "UNKNOWN":
        abstain.add(Finding("REVIEW_UNKNOWN", "/review/state"))

    if any(value is not False for value in effects.values()):
        deny.add(Finding("AUTHORITY_OVERREACH", "/effects"))
    return deny, abstain


def validate_candidate(candidate: object) -> Result:
    if not isinstance(candidate, Mapping):
        return Result("ERROR", (Finding("ROOT_NOT_OBJECT", "/"),))
    if _contains_surrogate(candidate):
        return Result("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("ERROR", schema_findings)
    try:
        identity = expected_id(candidate)
    except (TypeError, ValueError, UnicodeError, RecursionError):
        return Result("ERROR", (Finding("CANONICALIZATION_ERROR", "/"),))
    if candidate["assessment_id"] != identity:
        return Result("ERROR", (Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"),))
    deny, abstain = _semantic_findings(candidate)
    if deny:
        return Result("DENY", tuple(sorted(deny)))
    if abstain:
        return Result("ABSTAIN", tuple(sorted(abstain)))
    return Result("PASS", ())


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]  # type: ignore[index]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(value)
    else:
        target[key] = copy.deepcopy(value)  # type: ignore[index]


def materialize_case(base: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = copy.deepcopy(dict(base))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    if not case.get("preserve_identity", False):
        candidate["assessment_id"] = expected_id(candidate)
    return candidate


def _finding_records(result: Result) -> list[dict[str, str]]:
    return [{"code": finding.code, "path": finding.path} for finding in result.findings]


def validate_fixture_matrix() -> list[dict[str, object]]:
    base = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in cases:
        result = validate_candidate(materialize_case(base, case))
        findings = _finding_records(result)
        results.append(
            {
                "name": case["name"],
                "outcome": result.outcome,
                "findings": findings,
                "suite_match": result.outcome == case["expected_outcome"]
                and findings == case["expected_findings"],
            }
        )
    return results


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": _finding_records(result),
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixtures() -> int:
    results = validate_fixture_matrix()
    for result in results:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if all(result["suite_match"] for result in results) else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = read_json_object(args.input)
    result = Result("ERROR", findings) if candidate is None else validate_candidate(candidate)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
