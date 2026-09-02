"""Validate fixture-only COG byte-range integrity manifest candidates.

This module proves bounded local byte identity, exact range coverage, explicit
range digest replay, canonical declarations, and authority boundaries. It does
not parse TIFF, validate COG layout, perform HTTP range requests, implement
BAO/BLAKE3, interpret pixels, resolve evidence, verify signatures, decide
policy or review, promote, release, deploy, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/evidence/cog_byte_range_integrity_manifest.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/evidence/cog_byte_range_integrity_manifest/cases.json"
)
FIXTURE_ROOT = REPO_ROOT / "fixtures"
MAX_JSON_BYTES = 1_048_576
MAX_PAYLOAD_BYTES = 67_108_864
REQUIRED_RANGE_ROLES = {
    "HEADER",
    "IMAGE_FILE_DIRECTORY",
    "TILE_DATA",
    "OVERVIEW_DATA",
}
ABSTAIN_CODES = {
    "IMMUTABILITY_UNKNOWN",
    "PAYLOAD_MISSING",
    "PAYLOAD_UNAVAILABLE",
    "PAYLOAD_UNKNOWN",
    "SIDECAR_FRESHNESS_UNKNOWN",
}
ERROR_CODES = {
    "PAYLOAD_TOO_LARGE",
    "PAYLOAD_UNREADABLE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_manifest_spec_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("manifest_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _fixture_payload_path(artifact_ref: object) -> tuple[Path | None, Finding | None]:
    if not isinstance(artifact_ref, str) or not artifact_ref.startswith("fixture://"):
        return None, Finding("ARTIFACT_REF_SCHEME_DENIED", "/artifact/artifact_ref")
    relative_text = artifact_ref.removeprefix("fixture://")
    relative = PurePosixPath(relative_text)
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or "." in relative.parts
        or str(relative) != relative_text
        or not relative.parts
        or relative.parts[0] != "fixtures"
    ):
        return None, Finding("ARTIFACT_REF_PATH_DENIED", "/artifact/artifact_ref")
    candidate = REPO_ROOT.joinpath(*relative.parts)
    try:
        candidate.resolve().relative_to(FIXTURE_ROOT.resolve())
    except (OSError, ValueError):
        return None, Finding("ARTIFACT_REF_PATH_DENIED", "/artifact/artifact_ref")
    return candidate, None


def _load_payload(artifact: Mapping[str, object]) -> tuple[bytes | None, list[Finding]]:
    availability = artifact.get("payload_availability")
    if availability == "MISSING":
        return None, [Finding("PAYLOAD_MISSING", "/artifact/payload_availability")]
    if availability == "UNKNOWN":
        return None, [Finding("PAYLOAD_UNKNOWN", "/artifact/payload_availability")]

    path, path_finding = _fixture_payload_path(artifact.get("artifact_ref"))
    if path_finding is not None:
        return None, [path_finding]
    assert path is not None
    try:
        if path.is_symlink():
            return None, [Finding("PAYLOAD_SYMLINK_DENIED", "/artifact/artifact_ref")]
        if not path.is_file():
            return None, [Finding("PAYLOAD_UNAVAILABLE", "/artifact/artifact_ref")]
        if path.stat().st_size > MAX_PAYLOAD_BYTES:
            return None, [Finding("PAYLOAD_TOO_LARGE", "/artifact/artifact_ref")]
        return path.read_bytes(), []
    except OSError:
        return None, [Finding("PAYLOAD_UNREADABLE", "/artifact/artifact_ref")]


def _artifact_state_findings(artifact: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    immutability = artifact.get("immutability_state")
    if immutability == "MUTABLE":
        findings.append(Finding("ARTIFACT_MUTABLE", "/artifact/immutability_state"))
    elif immutability == "UNKNOWN":
        findings.append(Finding("IMMUTABILITY_UNKNOWN", "/artifact/immutability_state"))

    freshness = artifact.get("sidecar_freshness_state")
    if freshness == "STALE":
        findings.append(Finding("SIDECAR_STALE", "/artifact/sidecar_freshness_state"))
    elif freshness == "UNKNOWN":
        findings.append(
            Finding("SIDECAR_FRESHNESS_UNKNOWN", "/artifact/sidecar_freshness_state")
        )
    return findings


def _range_findings(
    entries: list[object],
    payload: bytes,
) -> list[Finding]:
    findings: set[Finding] = set()
    typed_entries = [entry for entry in entries if isinstance(entry, Mapping)]
    ids = [entry.get("range_id") for entry in typed_entries]
    if len(ids) != len(set(ids)):
        findings.add(Finding("DUPLICATE_RANGE_ID", "/range_profile/entries"))

    roles = {entry.get("role") for entry in typed_entries}
    if not REQUIRED_RANGE_ROLES <= roles:
        findings.add(Finding("REQUIRED_RANGE_ROLE_MISSING", "/range_profile/entries"))

    sort_keys = [
        (entry.get("offset"), entry.get("range_id")) for entry in typed_entries
    ]
    if sort_keys != sorted(sort_keys):
        findings.add(Finding("RANGES_NOT_CANONICAL", "/range_profile/entries"))
        return sorted(findings)

    topology_invalid = False
    cursor = 0
    for index, entry in enumerate(typed_entries):
        offset = int(entry["offset"])
        length = int(entry["length"])
        if offset > cursor:
            findings.add(Finding("RANGE_GAP", f"/range_profile/entries/{index}"))
            topology_invalid = True
        elif offset < cursor:
            findings.add(Finding("RANGE_OVERLAP", f"/range_profile/entries/{index}"))
            topology_invalid = True
        end = offset + length
        if end > len(payload):
            findings.add(
                Finding("RANGE_OUT_OF_BOUNDS", f"/range_profile/entries/{index}")
            )
            topology_invalid = True
        cursor = end

    if not topology_invalid and cursor != len(payload):
        findings.add(
            Finding("RANGE_COVERAGE_INCOMPLETE", "/range_profile/entries")
        )
        topology_invalid = True

    if not topology_invalid:
        for index, entry in enumerate(typed_entries):
            offset = int(entry["offset"])
            length = int(entry["length"])
            observed = "sha256:" + hashlib.sha256(
                payload[offset : offset + length]
            ).hexdigest()
            if observed != entry.get("digest"):
                findings.add(
                    Finding(
                        "RANGE_DIGEST_MISMATCH",
                        f"/range_profile/entries/{index}/digest",
                    )
                )
    return sorted(findings)


def _format_findings(format_validation: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    states = [
        format_validation.get("tiff_structure_state"),
        format_validation.get("cog_layout_state"),
        format_validation.get("overview_layout_state"),
    ]
    report_ref = format_validation.get("validator_report_ref")
    if "INVALID" in states:
        findings.append(Finding("FORMAT_VALIDATION_FAILED", "/format_validation"))
    if "VALID" in states and report_ref is None:
        findings.append(
            Finding(
                "FORMAT_VALIDATION_REFERENCE_REQUIRED",
                "/format_validation/validator_report_ref",
            )
        )
    if all(state in {"NOT_EVALUATED", "UNKNOWN"} for state in states) and report_ref is not None:
        findings.append(
            Finding(
                "FORMAT_VALIDATION_REFERENCE_INCOHERENT",
                "/format_validation/validator_report_ref",
            )
        )
    return findings


def _governance_findings(governance: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    if not _canonical_strings(governance.get("evidence_refs")):
        findings.append(
            Finding("EVIDENCE_REFS_NOT_CANONICAL", "/governance/evidence_refs")
        )
    if governance.get("policy_state") != "NOT_EVALUATED":
        findings.append(Finding("POLICY_STATE_OVERCLAIM", "/governance/policy_state"))
    if governance.get("review_state") != "PENDING":
        findings.append(Finding("REVIEW_STATE_OVERCLAIM", "/governance/review_state"))
    if governance.get("release_state") != "NOT_RELEASED":
        findings.append(
            Finding("RELEASE_STATE_OVERCLAIM", "/governance/release_state")
        )
    if governance.get("release_manifest_ref") is not None:
        findings.append(
            Finding(
                "RELEASE_MANIFEST_REFERENCE_UNEXPECTED",
                "/governance/release_manifest_ref",
            )
        )
    if governance.get("rollback_ref") is not None:
        findings.append(
            Finding("ROLLBACK_REFERENCE_UNEXPECTED", "/governance/rollback_ref")
        )

    authority_codes = {
        "interpretation_authority": "INTERPRETATION_AUTHORITY_OVERCLAIM",
        "format_conformance_authority": "FORMAT_CONFORMANCE_AUTHORITY_OVERCLAIM",
        "policy_authority": "POLICY_AUTHORITY_OVERCLAIM",
        "review_authority": "REVIEW_AUTHORITY_OVERCLAIM",
        "promotion_authority": "PROMOTION_AUTHORITY_OVERCLAIM",
        "release_authority": "RELEASE_AUTHORITY_OVERCLAIM",
        "publication_authority": "PUBLICATION_AUTHORITY_OVERCLAIM",
    }
    for field, code in authority_codes.items():
        if governance.get(field) is not False:
            findings.append(Finding(code, f"/governance/{field}"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("manifest_spec_hash") != compute_manifest_spec_hash(candidate):
        findings.add(
            Finding("MANIFEST_SPEC_HASH_MISMATCH", "/manifest_spec_hash")
        )
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    artifact = candidate["artifact"]
    range_profile = candidate["range_profile"]
    format_validation = candidate["format_validation"]
    governance = candidate["governance"]
    assert isinstance(artifact, Mapping)
    assert isinstance(range_profile, Mapping)
    assert isinstance(format_validation, Mapping)
    assert isinstance(governance, Mapping)

    findings.update(_artifact_state_findings(artifact))
    payload, payload_findings = _load_payload(artifact)
    findings.update(payload_findings)
    if payload is not None:
        if artifact.get("byte_length") != len(payload):
            findings.add(Finding("BYTE_LENGTH_MISMATCH", "/artifact/byte_length"))
        observed_whole = "sha256:" + hashlib.sha256(payload).hexdigest()
        if artifact.get("whole_digest") != observed_whole:
            findings.add(
                Finding("WHOLE_DIGEST_MISMATCH", "/artifact/whole_digest")
            )
        entries = range_profile["entries"]
        assert isinstance(entries, list)
        findings.update(_range_findings(entries, payload))

    findings.update(_format_findings(format_validation))
    findings.update(_governance_findings(governance))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes & ERROR_CODES:
        outcome = "ERROR"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _resolve_pointer(root: object, path: str) -> tuple[object, str]:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in path.split("/")[1:]]
    if not parts:
        raise ValueError("root replacement is not supported")
    target = root
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    return target, parts[-1]


def _apply_mutations(candidate: dict[str, object], mutations: object) -> None:
    assert isinstance(mutations, list)
    for mutation in mutations:
        assert isinstance(mutation, Mapping)
        target, key = _resolve_pointer(candidate, str(mutation["path"]))
        operation = mutation.get("op")
        if operation == "reverse":
            value = target[int(key)] if isinstance(target, list) else target[key]
            assert isinstance(value, list)
            value.reverse()
        elif operation == "remove":
            if isinstance(target, list):
                target.pop(int(key))
            else:
                del target[key]
        else:
            value = copy.deepcopy(mutation.get("value"))
            if isinstance(target, list):
                target[int(key)] = value
            else:
                target[key] = value


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    assert isinstance(candidate, dict)
    _apply_mutations(candidate, entry.get("mutations", []))
    candidate["manifest_spec_hash"] = compute_manifest_spec_hash(candidate)
    if entry.get("tamper") == "manifest_spec_hash":
        candidate["manifest_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only COG byte-range integrity manifest candidates."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
