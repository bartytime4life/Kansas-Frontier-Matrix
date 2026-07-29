"""Validate non-authoritative KFM BriefingSignal records.

A passing BriefingSignal is discovery and routing metadata only. It cannot admit a
source, mutate the repository, construct proof, release, deploy, publish, or serve
public truth. Validation is deterministic and no-network.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker


SCHEMA_PATH = Path("schemas/contracts/v1/governance/briefing_signal.schema.json")
MAX_RECORD_BYTES = 1_000_000

INLINE_GEOMETRY_KEYS = frozenset(
    {
        "geometry",
        "coordinates",
        "latitude",
        "longitude",
        "lat",
        "lon",
        "lng",
        "bbox",
        "centroid",
        "easting",
        "northing",
        "x",
        "y",
    }
)

TRUST_BEARING_TRUE_KEYS = frozenset(
    {
        "approved",
        "admitted",
        "released",
        "published",
        "public",
        "promotion_eligible",
        "source_active",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code=code, path=path)
    if finding not in findings:
        findings.append(finding)


def _json_path(parts: Sequence[object]) -> str:
    if not parts:
        return "$"
    return "$." + ".".join(str(part) for part in parts)


def _walk(value: object, path: tuple[object, ...] = ()):
    if isinstance(value, Mapping):
        for key in sorted(value, key=str):
            child_path = (*path, key)
            yield child_path, key, value[key]
            yield from _walk(value[key], child_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            child_path = (*path, index)
            yield child_path, index, item
            yield from _walk(item, child_path)


def _load_schema() -> Mapping[str, object]:
    payload = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(payload)
    return payload


def validate_candidate(candidate: object) -> tuple[Finding, ...]:
    findings: list[Finding] = []

    if not isinstance(candidate, Mapping):
        return (Finding("DOCUMENT_NOT_OBJECT", "$"),)

    try:
        schema = _load_schema()
    except (OSError, UnicodeError, ValueError):
        return (Finding("BRIEFING_SIGNAL_SCHEMA_UNAVAILABLE", "$"),)

    schema_validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(schema_validator.iter_errors(candidate), key=lambda item: list(item.path)):
        _add(findings, "BRIEFING_SIGNAL_SCHEMA_INVALID", _json_path(tuple(error.path)))

    claims = candidate.get("claims")
    if isinstance(claims, list):
        for index, claim in enumerate(claims):
            if not isinstance(claim, Mapping):
                continue
            if claim.get("truth_label") == "CONFIRMED" and not claim.get("evidence_refs"):
                _add(
                    findings,
                    "CONFIRMED_CLAIM_WITHOUT_EVIDENCE",
                    f"$.claims.{index}.evidence_refs",
                )

    candidate_payload = candidate.get("candidate_payload")
    if isinstance(candidate_payload, Mapping):
        attributes = candidate_payload.get("attributes")
        if isinstance(attributes, Mapping):
            for path, key, value in _walk(attributes):
                dotted = "$.candidate_payload.attributes." + ".".join(str(part) for part in path)
                if isinstance(key, str) and key.lower() in INLINE_GEOMETRY_KEYS:
                    _add(findings, "INLINE_GEOMETRY_FORBIDDEN", dotted)
                if (
                    isinstance(key, str)
                    and key.lower() in TRUST_BEARING_TRUE_KEYS
                    and value is True
                ):
                    _add(findings, "TRUST_BEARING_STATE_FORBIDDEN", dotted)

    if candidate.get("public_use_allowed") is not False:
        _add(findings, "PUBLIC_USE_MUST_REMAIN_FALSE", "$.public_use_allowed")

    permissions = candidate.get("permissions")
    if isinstance(permissions, Mapping):
        for field in (
            "source_activation",
            "proof_construction",
            "release",
            "deployment",
            "publication",
        ):
            if permissions.get(field) is not False:
                _add(findings, "CONSEQUENTIAL_PERMISSION_FORBIDDEN", f"$.permissions.{field}")

    next_action = candidate.get("next_action")
    if isinstance(next_action, Mapping) and next_action.get("repository_mutation_allowed") is not False:
        _add(
            findings,
            "REPOSITORY_MUTATION_PERMISSION_FORBIDDEN",
            "$.next_action.repository_mutation_allowed",
        )

    return tuple(sorted(findings))


def validate_file(path: Path) -> tuple[Finding, ...]:
    try:
        if path.stat().st_size > MAX_RECORD_BYTES:
            return (Finding("BRIEFING_SIGNAL_TOO_LARGE", "$"),)
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return (Finding("BRIEFING_SIGNAL_JSON_INVALID", "$"),)
    return validate_candidate(payload)


def _serialize(path: Path, findings: Sequence[Finding]) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in findings
            ],
            "outcome": "PASS" if not findings else "FAIL",
            "scope": "briefing-signal-discovery-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate non-authoritative KFM BriefingSignal records."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        findings = validate_file(path)
        print(_serialize(path, findings))
        failed = failed or bool(findings)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
