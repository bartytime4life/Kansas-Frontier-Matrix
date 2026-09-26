"""Check the bounded identity envelope for Settlements/Infrastructure candidates.

This is a candidate validator, not a policy, evidence-resolution, or release gate.
The paired JSON Schema is still a proposed, permissive stub.
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import sys
from pathlib import Path


MAX_BYTES = 1024 * 1024
FAMILIES = frozenset({
    "Settlement", "Municipality", "CensusPlace", "Townsite", "GhostTown",
    "Fort", "Mission", "ReservationCommunity", "InfrastructureAsset",
    "NetworkNode", "NetworkSegment", "Facility", "ServiceArea", "Operator",
    "ConditionObservation", "Dependency",
})
REQUIRED_TEXT = (
    "id", "object_family", "feature_role", "source_id", "source_role",
    "source_record_digest", "normalized_digest", "evidence_ref",
)


def _unique_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number: {value}")


def load_candidate(path: Path) -> object:
    absolute = path.absolute()
    if any(part.is_symlink() for part in (absolute, *absolute.parents)):
        raise ValueError("candidate path must be a regular non-symlink file")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(absolute, flags)
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError("candidate path must be a regular file")
        if metadata.st_size > MAX_BYTES:
            raise ValueError("candidate exceeds 1048576 bytes")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            payload = stream.read(MAX_BYTES + 1)
    finally:
        if descriptor != -1:
            os.close(descriptor)
    if len(payload) > MAX_BYTES:
        raise ValueError("candidate exceeds 1048576 bytes")
    return json.loads(payload.decode("utf-8"), object_pairs_hook=_unique_pairs,
                      parse_constant=_reject_constant)


def validate(candidate: object) -> list[str]:
    if not isinstance(candidate, dict):
        return ["IDENTITY_OBJECT_REQUIRED"]
    if not isinstance(candidate.get("object_family"), str) or not candidate["object_family"].strip() or not isinstance(candidate.get("feature_role"), str) or not candidate["feature_role"].strip():
        # Preserve the diagnostic recorded by the existing negative fixture.
        return ["OBJECT_FAMILY_NOT_DISTINGUISHABLE"]
    findings = [f"REQUIRED_TEXT_INVALID:{key}" for key in REQUIRED_TEXT
                if not isinstance(candidate.get(key), str) or not candidate[key].strip()]
    if isinstance(candidate.get("object_family"), str) and candidate["object_family"] not in FAMILIES:
        findings.append("OBJECT_FAMILY_UNKNOWN")
    if not any(isinstance(candidate.get(key), str) and candidate[key].strip()
               for key in ("source_native_id", "normalized_name_key")):
        findings.append("SOURCE_KEY_MISSING")
    scope = candidate.get("temporal_scope")
    if not isinstance(scope, dict) or not scope:
        findings.append("TEMPORAL_SCOPE_MISSING")
    for key in ("source_record_digest", "normalized_digest"):
        value = candidate.get(key)
        if isinstance(value, str) and (len(value) != 71 or not value.startswith("sha256:")
                                       or any(ch not in "0123456789abcdef" for ch in value[7:])):
            findings.append(f"DIGEST_INVALID:{key}")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check candidate identity envelopes only; no release decision.")
    parser.add_argument("candidates", nargs="+", type=Path)
    args = parser.parse_args(argv)
    failed = False
    for path in args.candidates:
        try:
            findings = validate(load_candidate(path))
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
            # Avoid printing input content, which could contain sensitive details.
            findings = [f"INPUT_ERROR:{type(exc).__name__}"]
        if findings:
            failed = True
            print(f"FAIL {path}: {', '.join(findings)}")
        else:
            print(f"OK {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
