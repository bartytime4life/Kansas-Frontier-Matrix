#!/usr/bin/env python3
"""Validate KFM release-support ProofPack manifests without network access.

A pass proves only the declared fixture-first schema, component-family closure,
cross-reference bindings, path safety, and local SHA-256 integrity. It does not
create evidence, policy, review, release, signature, deployment, publication, or
public-use authority.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.proof_pack._common import (
    MAX_TOTAL_COMPONENT_BYTES,
    canonical_relative_path,
    load_json_object,
    resolve_regular_file,
    sha256_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/proof_pack.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/evidence/proof_pack"
MAX_SCHEMA_FINDINGS = 50
REQUIRED_KINDS = frozenset(
    {
        "EVIDENCE_BUNDLE",
        "VALIDATION_REPORT",
        "INTEGRITY_MANIFEST",
        "PROV_EXPORT",
        "LINEAGE_INDEX",
        "PROMOTION_DECISION",
        "RUNTIME_PROOF",
        "CITATION_SAMPLE",
        "CI_RUN",
        "RELEASE_ANCHOR",
        "ROLLBACK_REFERENCE",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(payload: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1))
    errors = sorted(errors, key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path), f"schema constraint failed: {error.validator}")
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings truncated"))
    return findings


def _components(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    raw = payload.get("components")
    return [item for item in raw if isinstance(item, dict)] if isinstance(raw, list) else []


def _semantic_findings(payload: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    release_id = payload.get("release_id")
    subject = payload.get("subject")
    subject_map = subject if isinstance(subject, dict) else {}
    subject_id = subject_map.get("subject_id")
    subject_spec_hash = subject_map.get("spec_hash")
    correction_state = subject_map.get("correction_state")
    components = _components(payload)

    kinds = {item.get("kind") for item in components if isinstance(item.get("kind"), str)}
    for kind in sorted(REQUIRED_KINDS - kinds):
        findings.append(Finding("REQUIRED_COMPONENT_MISSING", "/components", f"required component family is absent: {kind}"))

    if correction_state != "NONE" and "CORRECTION_HISTORY" not in kinds:
        findings.append(Finding("CORRECTION_HISTORY_REQUIRED", "/components", "non-current correction state requires correction history"))

    ids: set[str] = set()
    paths: set[str] = set()
    for index, item in enumerate(components):
        artifact_id = item.get("artifact_id")
        path = item.get("path")
        if isinstance(artifact_id, str):
            if artifact_id in ids:
                findings.append(Finding("COMPONENT_ID_DUPLICATE", f"/components/{index}/artifact_id", "component artifact IDs must be unique"))
            ids.add(artifact_id)
        if isinstance(path, str):
            if path in paths:
                findings.append(Finding("COMPONENT_PATH_DUPLICATE", f"/components/{index}/path", "component paths must be unique"))
            paths.add(path)
            if canonical_relative_path(path) is None:
                findings.append(Finding("COMPONENT_PATH_INVALID", f"/components/{index}/path", "component path must be canonical and repository-relative"))
        if item.get("release_id") != release_id:
            findings.append(Finding("COMPONENT_RELEASE_MISMATCH", f"/components/{index}/release_id", "component release binding differs from the pack"))
        if item.get("subject_id") != subject_id:
            findings.append(Finding("COMPONENT_SUBJECT_MISMATCH", f"/components/{index}/subject_id", "component subject binding differs from the pack"))
        if item.get("subject_spec_hash") != subject_spec_hash:
            findings.append(Finding("COMPONENT_SPEC_HASH_MISMATCH", f"/components/{index}/subject_spec_hash", "component spec-hash binding differs from the pack"))

    return findings


def _reference_findings(
    payload: Mapping[str, object],
    *,
    manifest_path: Path | None,
    repo_root: Path,
) -> list[Finding]:
    findings: list[Finding] = []
    total_bytes = 0
    try:
        resolved_manifest = manifest_path.resolve(strict=True) if manifest_path else None
    except OSError:
        resolved_manifest = None

    for index, item in enumerate(_components(payload)):
        raw_path = item.get("path")
        if canonical_relative_path(raw_path) is None:
            continue
        try:
            candidate = resolve_regular_file(repo_root, raw_path)
        except FileNotFoundError:
            findings.append(Finding("COMPONENT_NOT_FILE", f"/components/{index}/path", "referenced component is missing"))
            continue
        except (OSError, ValueError):
            findings.append(Finding("COMPONENT_NOT_FILE", f"/components/{index}/path", "referenced component is not a safe regular file"))
            continue
        if resolved_manifest is not None and candidate == resolved_manifest:
            findings.append(Finding("MANIFEST_SELF_REFERENCE_DENIED", f"/components/{index}/path", "a proof pack cannot bind its own bytes"))
            continue
        total_bytes += candidate.stat().st_size
        if total_bytes > MAX_TOTAL_COMPONENT_BYTES:
            findings.append(Finding("COMPONENT_TOTAL_TOO_LARGE", "/components", "component set exceeds the 128 MiB limit"))
            break
        expected = item.get("sha256")
        if isinstance(expected, str) and sha256_file(candidate) != expected:
            findings.append(Finding("COMPONENT_DIGEST_MISMATCH", f"/components/{index}/sha256", "referenced bytes do not match the declared SHA-256 digest"))
    return findings


def validate_payload(
    payload: Mapping[str, object],
    *,
    manifest_path: Path | None = None,
    repo_root: Path = REPO_ROOT,
    verify_references: bool = True,
) -> tuple[Finding, ...]:
    schema = _schema_findings(payload)
    if schema:
        return tuple(sorted(set(schema)))
    findings = _semantic_findings(payload)
    if verify_references:
        findings.extend(_reference_findings(payload, manifest_path=manifest_path, repo_root=repo_root))
    return tuple(sorted(set(findings)))


def validate_manifest(
    path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    verify_references: bool = True,
) -> tuple[Finding, ...]:
    try:
        payload = load_json_object(path)
    except ValueError:
        return (Finding("JSON_INVALID", "/", "manifest could not be read as a safe JSON object"),)
    return validate_payload(
        payload,
        manifest_path=path,
        repo_root=repo_root,
        verify_references=verify_references,
    )


def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_code.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 128:
            return None
        code = sidecar.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return None
    return code or None


def run_fixtures() -> int:
    valid = sorted((FIXTURES_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    if not valid or not invalid:
        print("PROOF_PACK_FIXTURES_ERROR nonempty valid and invalid lanes are required")
        return 2
    failures: list[str] = []
    for path in valid:
        if validate_manifest(path):
            failures.append(f"valid/{path.name}")
    for path in invalid:
        findings = validate_manifest(path)
        expected = _expected_code(path)
        if expected is None or expected not in {item.code for item in findings}:
            failures.append(f"invalid/{path.name}")
    if failures:
        for name in failures:
            print(f"PROOF_PACK_FIXTURE_POLARITY_FAIL file={name}")
        return 1
    print(
        "PROOF_PACK_FIXTURES_VALID "
        f"valid={len(valid)} invalid={len(invalid)} required_kinds={len(REQUIRED_KINDS)} "
        "no_network=true release_authority=false"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--no-reference-check", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.manifest is not None or args.no_reference_check or args.repo_root != REPO_ROOT:
            raise SystemExit("--fixtures cannot be combined with manifest-specific options")
        return run_fixtures()
    if args.manifest is None:
        raise SystemExit("manifest is required unless --fixtures is used")
    findings = validate_manifest(
        args.manifest,
        repo_root=args.repo_root,
        verify_references=not args.no_reference_check,
    )
    if not findings:
        print(f"PROOF_PACK_CHECK_PASS file={args.manifest.name} release_authority=false")
        return 0
    for finding in findings:
        print(f"PROOF_PACK_CHECK_FAIL code={finding.code} field={finding.field} detail={finding.detail}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
