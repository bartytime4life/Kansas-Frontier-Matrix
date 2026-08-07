"""Replay the effective web-delta fixture set with append-only corrections.

The three original fixture manifests remain immutable lineage. A small correction
manifest updates only the two stale HTTP 304 identity fields exposed by hosted
RFC 8785 validation. This module applies those corrections in memory, verifies
the prior values before replacement, and then replays exact outcomes/findings.
It performs no network, source, lifecycle, policy, release, or publication work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path

from tools.validators.validate_source_event_envelope import _load_json_object
from tools.validators.validate_web_delta_profile import (
    FIXTURE_FILES,
    NON_EFFECTS,
    SCOPE,
    validate_document,
)

CORRECTION_PATH = (
    Path(__file__).resolve().parents[2]
    / "fixtures"
    / "contracts"
    / "v1"
    / "source"
    / "web_delta_profile"
    / "identity-corrections.json"
)


def _load_mapping(path: Path) -> Mapping[str, object]:
    value, findings = _load_json_object(path)
    if not isinstance(value, Mapping):
        codes = ",".join(sorted(finding.code for finding in findings)) or "INVALID_ROOT"
        raise ValueError(f"{path.name}:{codes}")
    return value


def load_effective_cases() -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    index_by_id: dict[str, int] = {}

    for path in FIXTURE_FILES:
        manifest = _load_mapping(path)
        raw_cases = manifest.get("cases")
        if not isinstance(raw_cases, list):
            raise ValueError(f"{path.name}:CASES_INVALID")
        for raw_case in raw_cases:
            if not isinstance(raw_case, Mapping):
                raise ValueError(f"{path.name}:CASE_INVALID")
            case = copy.deepcopy(dict(raw_case))
            case_id = case.get("case_id")
            if not isinstance(case_id, str) or case_id in index_by_id:
                raise ValueError(f"{path.name}:CASE_ID_INVALID")
            index_by_id[case_id] = len(cases)
            cases.append(case)

    correction_manifest = _load_mapping(CORRECTION_PATH)
    corrections = correction_manifest.get("corrections")
    if not isinstance(corrections, list):
        raise ValueError("identity-corrections.json:CORRECTIONS_INVALID")

    corrected_ids: set[str] = set()
    for raw_correction in corrections:
        if not isinstance(raw_correction, Mapping):
            raise ValueError("identity-corrections.json:CORRECTION_INVALID")
        correction = dict(raw_correction)
        case_id = correction.get("case_id")
        if not isinstance(case_id, str) or case_id not in index_by_id:
            raise ValueError("identity-corrections.json:CASE_ID_UNKNOWN")
        if case_id in corrected_ids:
            raise ValueError("identity-corrections.json:CASE_ID_DUPLICATE")
        corrected_ids.add(case_id)

        case = cases[index_by_id[case_id]]
        document = case.get("document")
        if not isinstance(document, dict):
            raise ValueError(f"{case_id}:DOCUMENT_INVALID")
        payload = document.get("payload")
        if not isinstance(payload, dict):
            raise ValueError(f"{case_id}:PAYLOAD_INVALID")

        if payload.get("payload_spec_hash") != correction.get("prior_payload_spec_hash"):
            raise ValueError(f"{case_id}:PRIOR_PAYLOAD_HASH_MISMATCH")
        if document.get("event_id") != correction.get("prior_event_id"):
            raise ValueError(f"{case_id}:PRIOR_EVENT_ID_MISMATCH")

        new_payload_hash = correction.get("payload_spec_hash")
        new_event_id = correction.get("event_id")
        if not isinstance(new_payload_hash, str) or not isinstance(new_event_id, str):
            raise ValueError(f"{case_id}:CORRECTED_IDENTITY_INVALID")
        payload["payload_spec_hash"] = new_payload_hash
        document["event_id"] = new_event_id
        case["identity_correction_reason"] = correction.get("reason_code")

    if corrected_ids != {
        "valid_http_304_heartbeat",
        "invalid_heartbeat_carries_new_content",
    }:
        raise ValueError("identity-corrections.json:CORRECTION_SET_INVALID")
    return cases


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    suite_findings: list[dict[str, object]] = []
    try:
        cases = load_effective_cases()
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        return False, {
            "authority": "NONE",
            "cases": 0,
            "execution_mode": "FIXTURE_ONLY",
            "findings": [{"code": "FIXTURE_CORRECTION_ERROR", "detail": str(exc)}],
            "non_effects": NON_EFFECTS,
            "outcome": "ERROR",
            "scope": SCOPE,
        }

    for index, case in enumerate(cases):
        result = validate_document(case.get("document"))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if result.outcome != case.get("expected_outcome"):
            suite_findings.append(
                {
                    "actual": result.outcome,
                    "case": case.get("case_id", index),
                    "code": "FIXTURE_OUTCOME_MISMATCH",
                    "expected": case.get("expected_outcome"),
                    "event_id": result.event_id,
                    "payload_spec_hash": result.payload_spec_hash,
                }
            )
        if actual != case.get("expected_findings"):
            suite_findings.append(
                {
                    "actual": actual,
                    "case": case.get("case_id", index),
                    "code": "FIXTURE_FINDINGS_MISMATCH",
                    "expected": case.get("expected_findings"),
                    "event_id": result.event_id,
                    "payload_spec_hash": result.payload_spec_hash,
                }
            )

    return not suite_findings, {
        "authority": "NONE",
        "cases": len(cases),
        "corrections_applied": 2,
        "execution_mode": "FIXTURE_ONLY",
        "findings": suite_findings,
        "non_effects": NON_EFFECTS,
        "outcome": "DENY" if suite_findings else "PASS",
        "scope": SCOPE,
    }


def main(argv: Sequence[str] | None = None) -> int:
    if argv:
        raise SystemExit("this replay command accepts no arguments")
    ok, payload = run_fixture_suite()
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
