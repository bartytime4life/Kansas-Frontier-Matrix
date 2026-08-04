"""Validate the proposed fixture-first KFMGeoManifest profile.

A passing result proves bounded metadata shape, profile-local deterministic
hashing, transform-chain consistency, fail-closed release-candidate posture,
and optional exact local-byte binding. It does not accept ADR-0023, verify a
signature, resolve evidence, evaluate policy or review, release, deploy, or
publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from collections.abc import Mapping, Sequence
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.evidence._kfm_geo_manifest import (
    DuplicateKeyError,
    Finding,
    MAX_MANIFEST_BYTES,
    MAX_PAYLOAD_BYTES,
    NonFiniteNumberError,
    ValidationResult,
    finite_float,
    mapping,
    object_no_duplicates,
    read_json_object,
    read_regular_bytes,
    reject_nonfinite,
    schema_findings,
    strings,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/evidence/kfm_geo_manifest"
_ZERO_DIGEST = "sha256:" + ("0" * 64)
_MEDIA_BY_TYPE = {
    "pmtiles": "application/vnd.pmtiles",
    "cog": "image/tiff; application=geotiff; profile=cloud-optimized",
    "geoparquet": "application/vnd.apache.parquet",
    "geojson": "application/geo+json",
}
_PUBLIC_CANDIDATE_ROLES = {"release_candidate", "generalized_derivative", "rollback_target"}


def _sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def canonical_spec_hash(candidate: Mapping[str, object]) -> str:
    """Hash the fixture profile's declared projection.

    This is deliberately profile-local. It uses the repository's currently
    implemented bare ``sha256:`` grammar and does not claim RFC 8785/JCS or
    cross-runtime hash-policy authority.
    """

    projection = {key: value for key, value in candidate.items() if key != "spec_hash"}
    canonical = json.dumps(
        projection,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return _sha256(canonical)


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _canonical_reference_arrays(candidate: Mapping[str, object]) -> list[tuple[str, list[str]]]:
    artifact = mapping(candidate.get("artifact"))
    evidence = mapping(candidate.get("evidence"))
    derivation = mapping(candidate.get("derivation"))
    lineage = mapping(candidate.get("lineage"))
    return [
        ("/artifact/source_artifact_refs", strings(artifact.get("source_artifact_refs"))),
        ("/evidence/evidence_bundle_refs", strings(evidence.get("evidence_bundle_refs"))),
        ("/evidence/evidence_refs", strings(evidence.get("evidence_refs"))),
        ("/evidence/source_descriptor_refs", strings(evidence.get("source_descriptor_refs"))),
        ("/derivation/receipt_refs", strings(derivation.get("receipt_refs"))),
        ("/lineage/correction_refs", strings(lineage.get("correction_refs"))),
    ]


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    artifact = mapping(candidate.get("artifact"))
    spatial = mapping(candidate.get("spatial"))
    derivation = mapping(candidate.get("derivation"))
    governance = mapping(candidate.get("governance"))
    lineage = mapping(candidate.get("lineage"))
    transforms = [item for item in derivation.get("transforms", []) if isinstance(item, Mapping)] if isinstance(derivation.get("transforms"), list) else []

    digest_fields: list[tuple[str, object]] = [
        ("/spec_hash", candidate.get("spec_hash")),
        ("/artifact/content_digest", artifact.get("content_digest")),
        ("/derivation/parameters_digest", derivation.get("parameters_digest")),
    ]
    for index, transform in enumerate(transforms):
        digest_fields.extend(
            (
                (f"/derivation/transforms/{index}/input_digest", transform.get("input_digest")),
                (f"/derivation/transforms/{index}/output_digest", transform.get("output_digest")),
            )
        )
    for field, value in digest_fields:
        if value == _ZERO_DIGEST:
            findings.append(Finding("PLACEHOLDER_DIGEST", field, "all-zero digest is not accepted"))

    try:
        expected_hash = canonical_spec_hash(candidate)
    except (TypeError, ValueError, RecursionError):
        findings.append(Finding("SPEC_HASH_EVALUATION_ERROR", "/spec_hash", "profile hash could not be evaluated"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash", "spec_hash is not bound to the declared profile"))

    artifact_type = artifact.get("artifact_type")
    media_type = artifact.get("media_type")
    if isinstance(artifact_type, str) and artifact_type in _MEDIA_BY_TYPE:
        if media_type != _MEDIA_BY_TYPE[artifact_type]:
            findings.append(Finding("MEDIA_TYPE_MISMATCH", "/artifact/media_type", "media type is incompatible with artifact type"))

    bbox = spatial.get("bbox")
    if isinstance(bbox, list) and len(bbox) == 4 and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in bbox):
        if bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
            findings.append(Finding("BBOX_ORDER_INVALID", "/spatial/bbox", "bbox minimums must precede maximums"))
        if spatial.get("crs") == "EPSG:4326" and (
            bbox[0] < -180 or bbox[2] > 180 or bbox[1] < -90 or bbox[3] > 90
        ):
            findings.append(Finding("BBOX_CRS_RANGE_INVALID", "/spatial/bbox", "EPSG:4326 bbox is out of range"))

    scale = mapping(spatial.get("scale_or_resolution"))
    tiling = spatial.get("tiling_profile")
    if artifact_type == "pmtiles":
        if not isinstance(tiling, Mapping):
            findings.append(Finding("TILING_PROFILE_REQUIRED", "/spatial/tiling_profile", "PMTiles requires a tiling profile"))
        if scale.get("kind") != "zoom_range":
            findings.append(Finding("TILE_SCALE_PROFILE_REQUIRED", "/spatial/scale_or_resolution", "PMTiles requires a zoom range"))
        if isinstance(tiling, Mapping) and scale.get("kind") == "zoom_range":
            if tiling.get("min_zoom") != scale.get("min_zoom") or tiling.get("max_zoom") != scale.get("max_zoom"):
                findings.append(Finding("TILING_PROFILE_SCALE_MISMATCH", "/spatial/tiling_profile", "tile and scale zoom ranges differ"))
    elif tiling is not None:
        findings.append(Finding("TILING_PROFILE_UNEXPECTED", "/spatial/tiling_profile", "non-tile artifact cannot claim a tile profile"))
    if scale.get("kind") == "zoom_range":
        minimum, maximum = scale.get("min_zoom"), scale.get("max_zoom")
        if isinstance(minimum, int) and isinstance(maximum, int) and minimum > maximum:
            findings.append(Finding("ZOOM_RANGE_INVALID", "/spatial/scale_or_resolution", "minimum zoom exceeds maximum zoom"))
    if isinstance(tiling, Mapping):
        minimum, maximum = tiling.get("min_zoom"), tiling.get("max_zoom")
        if isinstance(minimum, int) and isinstance(maximum, int) and minimum > maximum:
            findings.append(Finding("ZOOM_RANGE_INVALID", "/spatial/tiling_profile", "minimum zoom exceeds maximum zoom"))

    transform_ids: list[str] = []
    for transform in transforms:
        transform_id = transform.get("transform_id")
        if isinstance(transform_id, str):
            transform_ids.append(transform_id)
    if len(transform_ids) != len(set(transform_ids)):
        findings.append(Finding("TRANSFORM_ID_DUPLICATE", "/derivation/transforms", "transform IDs must be unique"))
    for index in range(1, len(transforms)):
        if transforms[index - 1].get("output_digest") != transforms[index].get("input_digest"):
            findings.append(Finding("TRANSFORM_CHAIN_BROKEN", f"/derivation/transforms/{index}/input_digest", "transform chain is discontinuous"))
    if transforms and transforms[-1].get("output_digest") != artifact.get("content_digest"):
        findings.append(Finding("ARTIFACT_TRANSFORM_OUTPUT_MISMATCH", "/artifact/content_digest", "artifact digest is not the final transform output"))

    if governance.get("sensitivity_state") == "generalized":
        matching = [transform for transform in transforms if transform.get("operation") == "generalize"]
        if not matching or any(transform.get("receipt_ref") is None for transform in matching):
            findings.append(Finding("SENSITIVITY_TRANSFORM_RECEIPT_REQUIRED", "/derivation/transforms", "generalized sensitivity requires a receipted generalization"))
    if governance.get("sensitivity_state") == "redacted":
        matching = [transform for transform in transforms if transform.get("operation") == "redact"]
        if not matching or any(transform.get("receipt_ref") is None for transform in matching):
            findings.append(Finding("SENSITIVITY_TRANSFORM_RECEIPT_REQUIRED", "/derivation/transforms", "redacted sensitivity requires a receipted redaction"))
    if artifact.get("artifact_role") == "generalized_derivative" and governance.get("sensitivity_state") not in {"generalized", "redacted"}:
        findings.append(Finding("GENERALIZED_ROLE_POSTURE_MISMATCH", "/governance/sensitivity_state", "generalized derivative requires transformed sensitivity posture"))

    role = artifact.get("artifact_role")
    if role in _PUBLIC_CANDIDATE_ROLES:
        if governance.get("rights_state") != "verified_open":
            findings.append(Finding("PUBLIC_CANDIDATE_RIGHTS_BLOCKED", "/governance/rights_state", "public-bound candidate requires verified open rights"))
        if governance.get("sensitivity_state") not in {"public", "generalized", "redacted"}:
            findings.append(Finding("PUBLIC_CANDIDATE_SENSITIVITY_BLOCKED", "/governance/sensitivity_state", "public-bound candidate has unresolved sensitivity"))
        for field, value, code in (
            ("/governance/policy_decision_ref", governance.get("policy_decision_ref"), "POLICY_REFERENCE_REQUIRED"),
            ("/governance/review_ref", governance.get("review_ref"), "REVIEW_REFERENCE_REQUIRED"),
            ("/governance/rollback_ref", governance.get("rollback_ref"), "ROLLBACK_REFERENCE_REQUIRED"),
        ):
            if value is None:
                findings.append(Finding(code, field, "governance reference is required for a public-bound candidate"))

    identifier = candidate.get("id")
    supersedes = lineage.get("supersedes")
    rollback_of = lineage.get("rollback_of")
    if identifier in {supersedes, rollback_of}:
        findings.append(Finding("SELF_LINEAGE_REFERENCE", "/lineage", "manifest cannot reference itself in lineage"))
    corrections = strings(lineage.get("correction_refs"))
    if supersedes is not None and not corrections:
        findings.append(Finding("SUPERSESSION_CORRECTION_REQUIRED", "/lineage/correction_refs", "supersession requires a correction reference"))
    if role == "rollback_target" and rollback_of is None:
        findings.append(Finding("ROLLBACK_LINEAGE_REQUIRED", "/lineage/rollback_of", "rollback target requires rollback_of"))
    if role != "rollback_target" and rollback_of is not None:
        findings.append(Finding("ROLLBACK_LINEAGE_UNEXPECTED", "/lineage/rollback_of", "non-rollback artifact cannot claim rollback_of"))

    temporal = mapping(mapping(candidate.get("claim_scope")).get("temporal_scope"))
    start, end = _parse_time(temporal.get("valid_from")), _parse_time(temporal.get("valid_to"))
    if start and end and start > end:
        findings.append(Finding("TEMPORAL_SCOPE_INVALID", "/claim_scope/temporal_scope", "valid_from follows valid_to"))

    for field, values in _canonical_reference_arrays(candidate):
        if values != sorted(set(values)):
            findings.append(Finding("REFERENCE_ARRAY_NOT_CANONICAL", field, "reference arrays must be sorted and unique"))
    return findings


def validate_manifest(manifest_path: Path, payload_path: Path | None = None) -> ValidationResult:
    candidate, findings = read_json_object(manifest_path)
    if candidate is None:
        return ValidationResult(tuple(sorted(findings)))
    schema_errors = schema_findings(SCHEMA_PATH, candidate)
    findings.extend(schema_errors)
    if not schema_errors:
        findings.extend(_semantic_findings(candidate))
        if payload_path is not None:
            payload, payload_findings = read_regular_bytes(payload_path, MAX_PAYLOAD_BYTES)
            if payload is None:
                findings.extend(Finding(item.code, "/payload", item.detail) for item in payload_findings)
            else:
                artifact = mapping(candidate.get("artifact"))
                if artifact.get("byte_length") != len(payload):
                    findings.append(Finding("PAYLOAD_LENGTH_MISMATCH", "/artifact/byte_length", "declared length differs from local payload"))
                if artifact.get("content_digest") != _sha256(payload):
                    findings.append(Finding("PAYLOAD_DIGEST_MISMATCH", "/artifact/content_digest", "declared digest differs from local payload"))
    return ValidationResult(tuple(sorted(set(findings))))


def _read_fixture_array(path: Path) -> list[Mapping[str, object]]:
    data, findings = read_regular_bytes(path, MAX_MANIFEST_BYTES)
    if data is None or findings:
        raise ValueError(f"fixture could not be read: {path.name}")
    try:
        value = json.loads(
            data.decode("utf-8"),
            object_pairs_hook=object_no_duplicates,
            parse_constant=reject_nonfinite,
            parse_float=finite_float,
        )
    except (UnicodeError, DuplicateKeyError, NonFiniteNumberError, json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise ValueError(f"fixture is invalid: {path.name}") from exc
    if not isinstance(value, list) or not all(isinstance(item, Mapping) for item in value):
        raise ValueError(f"fixture must contain object array: {path.name}")
    return list(value)


def load_fixture_cases() -> dict[str, list[Mapping[str, object]]]:
    return {
        "valid": _read_fixture_array(FIXTURE_ROOT / "valid_cases.json"),
        "invalid": _read_fixture_array(FIXTURE_ROOT / "invalid_cases.json"),
        "semantic_invalid": [
            *_read_fixture_array(FIXTURE_ROOT / "semantic_invalid_cases_a.json"),
            *_read_fixture_array(FIXTURE_ROOT / "semantic_invalid_cases_b.json"),
        ],
    }


def materialize_case(case: Mapping[str, object], root: Path) -> tuple[Path, Path | None]:
    name, manifest = case.get("name"), case.get("manifest")
    if not isinstance(name, str) or not isinstance(manifest, Mapping):
        raise ValueError("fixture case is malformed")
    manifest_path = root / f"{name}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    payload_path = None
    if isinstance(case.get("payload_text"), str):
        payload_path = root / f"{name}.payload"
        payload_path.write_bytes(case["payload_text"].encode("utf-8"))
    return manifest_path, payload_path


def run_fixture_profile() -> int:
    try:
        corpus = load_fixture_cases()
    except ValueError as exc:
        print(json.dumps({"outcome": "FAIL", "reason": str(exc)}, sort_keys=True, separators=(",", ":")))
        return 1
    ok = True
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for lane in ("valid", "invalid", "semantic_invalid"):
            cases = corpus[lane]
            if not cases:
                return 1
            for case in cases:
                manifest, payload = materialize_case(case, root)
                supplied_payload = payload if lane == "valid" or case.get("use_payload") is True else None
                result = validate_manifest(manifest, supplied_payload)
                actual = sorted({finding.code for finding in result.findings})
                expected = [] if lane == "valid" else sorted(case.get("expected_codes", []))
                case_ok = result.ok if lane == "valid" else (not result.ok and actual == expected)
                ok = ok and case_ok
                print(
                    json.dumps(
                        {
                            "case": case.get("name"),
                            "findings": [{"code": finding.code, "field": finding.field} for finding in result.findings],
                            "outcome": "PASS" if case_ok else "FIXTURE_POLARITY_ERROR",
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    )
                )
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a proposed KFMGeoManifest candidate.")
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--payload", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.manifest or args.payload:
            parser.error("--fixtures cannot be combined with manifest or --payload")
        return run_fixture_profile()
    if args.manifest is None:
        parser.error("provide a manifest or use --fixtures")
    result = validate_manifest(args.manifest, args.payload)
    print(
        json.dumps(
            {
                "file": args.manifest.as_posix(),
                "findings": [{"code": finding.code, "field": finding.field} for finding in result.findings],
                "outcome": "PASS" if result.ok else "FAIL",
                "scope": "kfm-geo-manifest-fixture-shape-integrity-and-local-byte-binding-only",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
