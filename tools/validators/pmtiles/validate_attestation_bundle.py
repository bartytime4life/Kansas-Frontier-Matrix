#!/usr/bin/env python3
"""Reconcile the existing KFM PMTiles compatibility attestation bundle.

This offline validator binds one archive to its PMIDX, PMSIG, and RunReceipt
companions.  Success is structural only.  Signature verification, policy
evaluation, and release authorization are deliberately reported as holds.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from validate_header import HeaderValidationError, inspect_archive
from verify_merkle import MerkleValidationError, inspect_index

MAX_JSON_BYTES = 1024 * 1024
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
PROFILE = "kfm.pmtiles.attestation.compat.v1"
HOLDS = (
    "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
    "POLICY_EVALUATION_NOT_RUN",
    "RANGE_METADATA_NOT_AUTHENTICATED",
    "RELEASE_AUTHORIZATION_NOT_EVALUATED",
)
CHECKS = (
    "PMTILES_V3_HEADER_METADATA",
    "PMIDX_ARCHIVE_CHUNKS_MERKLE_RANGES",
    "PMSIG_SUBJECT_SHAPE",
    "RUNRECEIPT_SUBJECT_SHAPE",
    "CROSS_ARTIFACT_DIGEST_SPEC_HASH_ROOT",
)


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str


@dataclass(frozen=True)
class SignatureSubject:
    pmtiles_sha256: str
    pmidx_merkle_root: str
    spec_hash: str


@dataclass(frozen=True)
class ReceiptSubject:
    name: str
    pmtiles_sha256: str
    spec_hash: str


@dataclass(frozen=True)
class BundleResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def status(self) -> str:
        return "STRUCTURAL_PASS" if self.ok else "DENY"


def companion_paths(archive: Path) -> tuple[Path, Path, Path]:
    """Return the compatibility names already used by the repository workflow."""

    raw = str(archive)
    return (
        Path(raw + ".pmidx"),
        Path(raw + ".pmsig"),
        Path(raw + ".runreceipt.json"),
    )


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_json(path: Path, prefix: str) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding(f"{prefix}_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding(f"{prefix}_NOT_FILE")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding(f"{prefix}_JSON_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError:
        return None, [Finding(f"{prefix}_JSON_DUPLICATE_KEY")]
    except _NonFiniteNumberError:
        return None, [Finding(f"{prefix}_JSON_NONFINITE_NUMBER")]
    except (UnicodeError, json.JSONDecodeError):
        return None, [Finding(f"{prefix}_JSON_INVALID")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding(f"{prefix}_JSON_UNREADABLE")]
    if not isinstance(value, dict):
        return None, [Finding(f"{prefix}_ROOT_INVALID")]
    return value, []


def _hash(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = value.lower()
    return normalized if SHA256_RE.fullmatch(normalized) else None


def _signature_subject(
    value: dict[str, object],
) -> tuple[SignatureSubject | None, list[Finding]]:
    findings: list[Finding] = []
    if value.get("schema_version") != "kfm.pmsig.v1":
        findings.append(Finding("PMSIG_SCHEMA_VERSION_INVALID"))
    subject = value.get("subject")
    if not isinstance(subject, dict):
        return None, findings + [Finding("PMSIG_SUBJECT_INVALID")]
    archive_digest = _hash(subject.get("pmtiles_sha256"))
    root = _hash(subject.get("pmidx_merkle_root"))
    spec_hash = _hash(subject.get("spec_hash"))
    if archive_digest is None:
        findings.append(Finding("PMSIG_ARCHIVE_DIGEST_INVALID"))
    if root is None:
        findings.append(Finding("PMSIG_MERKLE_ROOT_INVALID"))
    if spec_hash is None:
        findings.append(Finding("PMSIG_SPEC_HASH_INVALID"))
    if not isinstance(value.get("key_id"), str) or not value.get("key_id"):
        findings.append(Finding("PMSIG_KEY_ID_INVALID"))
    if not isinstance(value.get("signature"), str) or not value.get("signature"):
        findings.append(Finding("PMSIG_SIGNATURE_SHAPE_INVALID"))
    if archive_digest is None or root is None or spec_hash is None:
        return None, findings
    return SignatureSubject(archive_digest, root, spec_hash), findings


def _receipt_subject(
    value: dict[str, object],
) -> tuple[ReceiptSubject | None, list[Finding]]:
    findings: list[Finding] = []
    if value.get("schema_version") != "kfm.runreceipt.pmtiles.v1":
        findings.append(Finding("RUNRECEIPT_SCHEMA_VERSION_INVALID"))
    if value.get("type") != "https://slsa.dev/provenance/v1":
        findings.append(Finding("RUNRECEIPT_TYPE_INVALID"))
    subjects = value.get("subject")
    if not isinstance(subjects, list) or len(subjects) != 1:
        return None, findings + [Finding("RUNRECEIPT_SUBJECT_INVALID")]
    subject = subjects[0]
    if not isinstance(subject, dict):
        return None, findings + [Finding("RUNRECEIPT_SUBJECT_INVALID")]
    name = subject.get("name")
    digest = subject.get("digest")
    raw_digest = digest.get("sha256") if isinstance(digest, dict) else None
    if isinstance(raw_digest, str) and not raw_digest.startswith("sha256:"):
        raw_digest = "sha256:" + raw_digest
    archive_digest = _hash(raw_digest)

    predicate = value.get("predicate")
    definition = predicate.get("buildDefinition") if isinstance(predicate, dict) else None
    build_type = definition.get("buildType") if isinstance(definition, dict) else None
    parameters = (
        definition.get("externalParameters") if isinstance(definition, dict) else None
    )
    spec_hash = _hash(
        parameters.get("spec_hash") if isinstance(parameters, dict) else None
    )
    run_details = predicate.get("runDetails") if isinstance(predicate, dict) else None
    builder = run_details.get("builder") if isinstance(run_details, dict) else None

    if not isinstance(name, str) or not name or "\\" in name:
        findings.append(Finding("RUNRECEIPT_SUBJECT_NAME_INVALID"))
    if archive_digest is None:
        findings.append(Finding("RUNRECEIPT_ARCHIVE_DIGEST_INVALID"))
    if build_type != "kfm/pmtiles/build@v1":
        findings.append(Finding("RUNRECEIPT_BUILD_TYPE_INVALID"))
    if spec_hash is None:
        findings.append(Finding("RUNRECEIPT_SPEC_HASH_INVALID"))
    if (
        not isinstance(builder, dict)
        or not isinstance(builder.get("id"), str)
        or not builder.get("id")
    ):
        findings.append(Finding("RUNRECEIPT_BUILDER_INVALID"))
    if not isinstance(name, str) or archive_digest is None or spec_hash is None:
        return None, findings
    return ReceiptSubject(name, archive_digest, spec_hash), findings


def _name_matches_archive(name: str, archive: Path) -> bool:
    path = PurePosixPath(name)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return False
    return path.name == archive.name


def validate_bundle(archive: Path) -> BundleResult:
    """Reconcile one split bundle without granting cryptographic or release trust."""

    findings: list[Finding] = []
    archive_info = None
    index_info = None
    try:
        archive_info = inspect_archive(archive)
    except HeaderValidationError as exc:
        findings.append(Finding(exc.code))

    pmidx_path, pmsig_path, receipt_path = companion_paths(archive)
    try:
        index_info = inspect_index(pmidx_path, archive)
    except MerkleValidationError as exc:
        findings.append(Finding(exc.code))

    pmsig, pmsig_load_findings = _load_json(pmsig_path, "PMSIG")
    findings.extend(pmsig_load_findings)
    signature = None
    if pmsig is not None:
        signature, signature_findings = _signature_subject(pmsig)
        findings.extend(signature_findings)

    receipt, receipt_load_findings = _load_json(receipt_path, "RUNRECEIPT")
    findings.extend(receipt_load_findings)
    receipt_subject = None
    if receipt is not None:
        receipt_subject, receipt_findings = _receipt_subject(receipt)
        findings.extend(receipt_findings)

    if archive_info is not None and index_info is not None:
        if archive_info.spec_hash != index_info.spec_hash:
            findings.append(Finding("PMTILES_PMIDX_SPEC_HASH_MISMATCH"))
    if signature is not None and index_info is not None:
        if signature.pmtiles_sha256 != index_info.pmtiles_sha256:
            findings.append(Finding("PMSIG_ARCHIVE_DIGEST_MISMATCH"))
        if signature.pmidx_merkle_root != index_info.merkle_root:
            findings.append(Finding("PMSIG_MERKLE_ROOT_MISMATCH"))
        if signature.spec_hash != index_info.spec_hash:
            findings.append(Finding("PMSIG_SPEC_HASH_MISMATCH"))
    if receipt_subject is not None and index_info is not None:
        if receipt_subject.pmtiles_sha256 != index_info.pmtiles_sha256:
            findings.append(Finding("RUNRECEIPT_ARCHIVE_DIGEST_MISMATCH"))
        if receipt_subject.spec_hash != index_info.spec_hash:
            findings.append(Finding("RUNRECEIPT_SPEC_HASH_MISMATCH"))
        if not _name_matches_archive(receipt_subject.name, archive):
            findings.append(Finding("RUNRECEIPT_SUBJECT_NAME_MISMATCH"))

    return BundleResult(tuple(sorted(set(findings), key=lambda item: item.code)))


def render_result(result: BundleResult) -> str:
    """Render bounded machine output containing codes, never candidate values."""

    return json.dumps(
        {
            "authority": "NONE",
            "checks": list(CHECKS),
            "holds": list(HOLDS),
            "issues": [{"code": finding.code} for finding in result.findings],
            "profile": PROFILE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmtiles", type=Path)
    args = parser.parse_args()
    try:
        result = validate_bundle(args.pmtiles)
    except Exception:  # fail closed without echoing attacker-controlled values
        print(
            json.dumps(
                {
                    "authority": "NONE",
                    "holds": list(HOLDS),
                    "issues": [{"code": "INTERNAL_VALIDATOR_ERROR"}],
                    "profile": PROFILE,
                    "status": "ERROR",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    print(render_result(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
