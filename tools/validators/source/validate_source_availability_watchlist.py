#!/usr/bin/env python3
"""Validate a fixture-only SourceAvailabilityWatchlist aggregate projection."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import CanonicalizationFailure, compute_spec_hash
except ImportError as exc:
    raise RuntimeError("repository hashing package is required") from exc

SCHEMA = ROOT / "schemas/contracts/v1/source/source_availability_watchlist.schema.json"
MAX_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source.availability_watchlist.fixture.v1"
IDENTITY_PREFIX = "kfm:source-availability-watchlist:"
NON_EFFECTS = (
    "no_network_request",
    "no_source_activation",
    "no_candidate_work_creation_or_execution",
    "no_raw_or_lifecycle_write",
    "no_evidence_policy_or_review_creation",
    "no_promotion_release_deployment_or_publication",
)

class DuplicateKeyError(ValueError):
    pass

class NonFiniteNumberError(ValueError):
    pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"

def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out

def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError

def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed

def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _compact(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))

def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None

def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("WATCHLIST_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("WATCHLIST_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("WATCHLIST_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("WATCHLIST_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("WATCHLIST_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("WATCHLIST_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("WATCHLIST_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("WATCHLIST_ROOT_NOT_OBJECT", "/"),)
    return value, ()

def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"watchlist_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]

def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("WATCHLIST_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("WATCHLIST_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("WATCHLIST_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))

def _health_reason(value: str) -> str:
    return {
        "HEALTHY": "SOURCE_HEALTHY",
        "DEGRADED": "SOURCE_DEGRADED",
        "STALE": "SOURCE_STALE",
        "UNAVAILABLE": "SOURCE_UNAVAILABLE",
        "UNKNOWN": "SOURCE_UNKNOWN",
    }[value]

def _change_reasons(entry: Mapping[str, Any]) -> set[str]:
    change = entry.get("change_class")
    if change == "UNCHANGED":
        return {"NO_MATERIAL_CHANGE"}
    if change == "BYTE_ONLY":
        return {"BYTE_ONLY_CHANGE"}
    if change == "SEMANTIC_NON_MATERIAL":
        return {"SEMANTIC_NON_MATERIAL_CHANGE"}
    if change == "MATERIAL":
        code = {
            "SCHEMA": "MATERIAL_SCHEMA_CHANGE",
            "CONTENT": "MATERIAL_CONTENT_CHANGE",
            "BOTH": "MATERIAL_SCHEMA_AND_CONTENT_CHANGE",
        }.get(entry.get("material_change_kind"))
        return {code, "CANDIDATE_REVIEW_REQUIRED"} if code else set()
    if change == "UNDETERMINED":
        return {"MATERIALITY_UNDETERMINED"}
    if change == "ERROR":
        return {"ASSESSMENT_ERROR"}
    return set()

def _changed(pair: object) -> bool:
    if not isinstance(pair, Mapping):
        return False
    prior, current = pair.get("prior"), pair.get("current")
    return prior is not None and current is not None and prior != current

def _entry_findings(entry: Mapping[str, Any], index: int) -> set[Finding]:
    out: set[Finding] = set()
    prefix = f"/entries/{index}"
    source_id = entry.get("source_id")
    if entry.get("source_descriptor_ref") != f"kfm://source/{source_id}":
        out.add(Finding("WATCHLIST_SOURCE_REF_MISMATCH", prefix + "/source_descriptor_ref"))
    health_ref = entry.get("source_health_assessment_ref")
    if not isinstance(health_ref, str) or not health_ref.startswith(f"kfm:source-health:{source_id}:"):
        out.add(Finding("WATCHLIST_HEALTH_REF_MISMATCH", prefix + "/source_health_assessment_ref"))

    change = entry.get("change_class")
    kind = entry.get("material_change_kind")
    expected = {
        "UNCHANGED": ("NONE", "NON_EVENT", "NO_ACTION", False, False),
        "BYTE_ONLY": ("NONE", "NON_EVENT", "NO_ACTION", False, False),
        "SEMANTIC_NON_MATERIAL": ("NONE", "NON_EVENT", "NO_ACTION", False, False),
        "MATERIAL": (None, "PROMOTION_CANDIDATE", "REVIEW_CANDIDATE", True, True),
        "UNDETERMINED": ("UNDETERMINED", "HOLD", "HOLD", True, False),
        "ERROR": ("ERROR", "ERROR", "ERROR", True, False),
    }.get(change)
    if expected is None:
        return out
    expected_kind, outcome, routing, review, needs_candidate = expected
    if expected_kind is not None and kind != expected_kind:
        out.add(Finding("WATCHLIST_CHANGE_KIND_MISMATCH", prefix + "/material_change_kind"))
    if change == "MATERIAL" and kind not in {"SCHEMA", "CONTENT", "BOTH"}:
        out.add(Finding("WATCHLIST_CHANGE_KIND_MISMATCH", prefix + "/material_change_kind"))
    if entry.get("material_change_outcome") != outcome or entry.get("routing") != routing or entry.get("review_required") is not review:
        out.add(Finding("WATCHLIST_ROUTING_MISMATCH", prefix + "/routing"))
    candidate = entry.get("candidate_work_ref")
    if needs_candidate and not isinstance(candidate, str):
        out.add(Finding("WATCHLIST_CANDIDATE_WORK_REQUIRED", prefix + "/candidate_work_ref"))
    if not needs_candidate and candidate is not None:
        out.add(Finding("WATCHLIST_CANDIDATE_WORK_FORBIDDEN", prefix + "/candidate_work_ref"))

    availability = entry.get("availability")
    if availability in {"UNAVAILABLE", "UNKNOWN"} and change not in {"UNDETERMINED", "ERROR"}:
        out.add(Finding("WATCHLIST_AVAILABILITY_CHANGE_CONFLICT", prefix + "/change_class"))
    if change == "MATERIAL":
        if kind in {"SCHEMA", "BOTH"} and not _changed(entry.get("schema_digests")):
            out.add(Finding("WATCHLIST_SCHEMA_CHANGE_UNPROVEN", prefix + "/schema_digests"))
        if kind in {"CONTENT", "BOTH"} and not _changed(entry.get("content_digests")):
            out.add(Finding("WATCHLIST_CONTENT_CHANGE_UNPROVEN", prefix + "/content_digests"))
    expected_reasons = sorted({_health_reason(str(availability)), *_change_reasons(entry)})
    if entry.get("reason_codes") != expected_reasons:
        out.add(Finding("WATCHLIST_REASON_CODES_MISMATCH", prefix + "/reason_codes"))
    return out

def recompute_summary(entries: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    counts = {"stable_count": 0, "review_candidate_count": 0, "hold_count": 0, "error_count": 0}
    for entry in entries:
        route = entry.get("routing")
        if route == "NO_ACTION":
            counts["stable_count"] += 1
        elif route == "REVIEW_CANDIDATE":
            counts["review_candidate_count"] += 1
        elif route == "HOLD":
            counts["hold_count"] += 1
        elif route == "ERROR":
            counts["error_count"] += 1
    overall = "ERROR" if counts["error_count"] else "HOLD" if counts["hold_count"] else "REVIEW_REQUIRED" if counts["review_candidate_count"] else "STABLE"
    return {"entry_count": len(entries), **counts, "overall_outcome": overall}

def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("WATCHLIST_CANONICALIZATION_ERROR", "/"))
    else:
        if value.get("spec_hash") != expected_hash:
            out.add(Finding("WATCHLIST_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value.get("watchlist_id") != expected_id:
            out.add(Finding("WATCHLIST_ID_MISMATCH", "/watchlist_id"))
    entries = value.get("entries")
    if not isinstance(entries, list):
        return tuple(sorted(out))
    source_ids = [entry.get("source_id") for entry in entries if isinstance(entry, Mapping)]
    if source_ids != sorted(source_ids):
        out.add(Finding("WATCHLIST_ENTRY_ORDER_INVALID", "/entries"))
    if len(source_ids) != len(set(source_ids)):
        out.add(Finding("WATCHLIST_SOURCE_ID_DUPLICATE", "/entries"))
    health_refs = [entry.get("source_health_assessment_ref") for entry in entries if isinstance(entry, Mapping)]
    if len(health_refs) != len(set(health_refs)):
        out.add(Finding("WATCHLIST_HEALTH_REF_DUPLICATE", "/entries"))
    observed = _parse_time(value.get("observed_at"))
    for index, entry in enumerate(entries):
        if not isinstance(entry, Mapping):
            continue
        out.update(_entry_findings(entry, index))
        checked = _parse_time(entry.get("checked_at"))
        if observed is None or checked is None or checked > observed:
            out.add(Finding("WATCHLIST_CHECK_TIME_INVALID", f"/entries/{index}/checked_at"))
    expected_summary = recompute_summary([entry for entry in entries if isinstance(entry, Mapping)])
    if value.get("summary") != expected_summary:
        out.add(Finding("WATCHLIST_SUMMARY_MISMATCH", "/summary"))
    return tuple(sorted(out))

def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    overall = value["summary"]["overall_outcome"]
    if overall == "HOLD":
        return Result("ABSTAIN", (Finding("WATCHLIST_UNRESOLVED_ENTRY", "/summary/overall_outcome"),))
    if overall == "ERROR":
        return Result("ERROR", (Finding("WATCHLIST_ASSESSMENT_ERROR_PRESENT", "/summary/overall_outcome"),))
    return Result("PASS", ())

def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)

def _serialize(path: Path | None, result: Result) -> str:
    return _compact({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "file": path.as_posix() if path else None,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "non_effects": NON_EFFECTS,
        "outcome": result.outcome,
        "scope": SCOPE,
    })

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]

if __name__ == "__main__":
    raise SystemExit(main())
