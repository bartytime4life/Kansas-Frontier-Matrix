"""Validate KFM IngestReceipt records and optional local integrity bindings.

The validator is deliberately no-network.  It validates the proposed receipt
and SourceDescriptor schemas, enforces bounded semantic invariants, and can
bind named receipt digests to explicit local artifacts and a SourceDescriptor
source-head checksum.  Validation output never includes receipt values or
artifact contents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry


RECEIPT_SCHEMA = REPO_ROOT / "schemas/contracts/v1/source/ingest_receipt.schema.json"
SOURCE_DESCRIPTOR_SCHEMA = (
    REPO_ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
)
FIXTURES_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/ingest_receipt"
MAX_JSON_BYTES = 5 * 1024 * 1024
ZERO_SHA256 = "sha256:" + ("0" * 64)


@dataclass(frozen=True, order=True)
class Finding:
    """One bounded validation failure that contains no input values."""

    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ArtifactBinding:
    """Bind one receipt digest key to one explicit local artifact."""

    digest_key: str
    path: Path


@dataclass(frozen=True)
class ValidationResult:
    """Deterministic validation result for one receipt."""

    findings: tuple[Finding, ...]
    outcome: str | None
    artifact_count: int
    source_head_bound: bool

    @property
    def ok(self) -> bool:
        return not self.findings


def _load_schema_validator(path: Path) -> Draft202012Validator:
    schema = json.loads(path.read_text(encoding="utf-8"))
    registry = build_registry(REPO_ROOT)
    return Draft202012Validator(
        schema,
        registry=registry,
        format_checker=FormatChecker(),
    )


def _load_json_object(path: Path, field: str) -> tuple[dict[str, object] | None, list[Finding]]:
    findings: list[Finding] = []
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", field, "symbolic links are denied")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", field, "input is not a regular file")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", field, "JSON input exceeds 5 MiB")]
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError):
        return None, [Finding("INPUT_UNREADABLE", field, "input could not be read safely")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", field, "input is not valid JSON")]
    if not isinstance(value, dict):
        findings.append(Finding("JSON_ROOT_INVALID", field, "JSON root must be an object"))
        return None, findings
    return value, findings


def _json_pointer(error_path: Iterable[object]) -> str:
    parts = [str(part).replace("~", "~0").replace("/", "~1") for part in error_path]
    return "/" + "/".join(parts) if parts else "/"


def _schema_findings(
    validator: Draft202012Validator,
    value: Mapping[str, object],
    prefix: str,
) -> list[Finding]:
    findings: list[Finding] = []
    errors = sorted(
        validator.iter_errors(value),
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )
    for error in errors:
        findings.append(
            Finding(
                "SCHEMA_INVALID",
                f"{prefix}{_json_pointer(error.absolute_path)}",
                f"schema constraint failed: {error.validator}",
            )
        )
    return findings


def _parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def _sha256_and_size(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
            size += len(block)
    return f"sha256:{digest.hexdigest()}", size


def _semantic_findings(receipt: Mapping[str, object], require_success: bool) -> list[Finding]:
    findings: list[Finding] = []
    started = _parse_datetime(receipt.get("started_at"))
    finished = _parse_datetime(receipt.get("finished_at"))
    if started is not None and finished is not None and finished < started:
        findings.append(
            Finding(
                "TIME_ORDER_INVALID",
                "/finished_at",
                "finished_at precedes started_at",
            )
        )

    digests = receipt.get("digests")
    if isinstance(digests, dict):
        for key, value in sorted(digests.items()):
            if value == ZERO_SHA256:
                findings.append(
                    Finding(
                        "DIGEST_PLACEHOLDER_DENIED",
                        f"/digests/{key}",
                        "all-zero SHA-256 placeholders are denied",
                    )
                )

    if require_success and receipt.get("outcome") != "SUCCESS":
        findings.append(
            Finding(
                "OUTCOME_NOT_SUCCESS",
                "/outcome",
                "operational gate requires SUCCESS",
            )
        )
    return findings


def _source_binding_findings(
    receipt: Mapping[str, object],
    descriptor: Mapping[str, object],
    source_head_key: str,
) -> list[Finding]:
    findings: list[Finding] = []
    if receipt.get("source_id") != descriptor.get("source_id"):
        findings.append(
            Finding(
                "SOURCE_ID_MISMATCH",
                "/source_id",
                "receipt and SourceDescriptor source identities differ",
            )
        )

    source_head = descriptor.get("source_head")
    content_identity = source_head.get("content_identity") if isinstance(source_head, dict) else None
    content_sha256 = (
        content_identity.get("content_sha256")
        if isinstance(content_identity, dict)
        else None
    )
    if not isinstance(content_sha256, str):
        findings.append(
            Finding(
                "SOURCE_HEAD_DIGEST_MISSING",
                "/source_descriptor/source_head/content_identity/content_sha256",
                "SourceDescriptor does not expose a SHA-256 source-head identity",
            )
        )
        return findings

    digests = receipt.get("digests")
    expected = f"sha256:{content_sha256.lower()}"
    actual = digests.get(source_head_key) if isinstance(digests, dict) else None
    if actual != expected:
        findings.append(
            Finding(
                "SOURCE_HEAD_DIGEST_MISMATCH",
                f"/digests/{source_head_key}",
                "receipt digest does not bind the SourceDescriptor source head",
            )
        )
    return findings


def _artifact_findings(
    receipt: Mapping[str, object],
    bindings: Sequence[ArtifactBinding],
) -> list[Finding]:
    findings: list[Finding] = []
    digests = receipt.get("digests")
    seen_keys: set[str] = set()
    seen_paths: set[Path] = set()
    total_bytes = 0

    for binding in sorted(bindings, key=lambda item: (item.digest_key, str(item.path))):
        if not binding.digest_key:
            findings.append(
                Finding("ARTIFACT_KEY_INVALID", "/artifacts", "digest key must not be empty")
            )
            continue
        if binding.digest_key in seen_keys:
            findings.append(
                Finding(
                    "ARTIFACT_KEY_DUPLICATE",
                    f"/digests/{binding.digest_key}",
                    "artifact digest key is bound more than once",
                )
            )
            continue
        seen_keys.add(binding.digest_key)

        path = binding.path
        try:
            if path.is_symlink():
                findings.append(
                    Finding(
                        "ARTIFACT_SYMLINK_DENIED",
                        f"/digests/{binding.digest_key}",
                        "symbolic-link artifacts are denied",
                    )
                )
                continue
            if not path.is_file():
                findings.append(
                    Finding(
                        "ARTIFACT_NOT_FILE",
                        f"/digests/{binding.digest_key}",
                        "bound artifact is not a regular file",
                    )
                )
                continue
            resolved = path.resolve(strict=True)
            if resolved in seen_paths:
                findings.append(
                    Finding(
                        "ARTIFACT_PATH_DUPLICATE",
                        f"/digests/{binding.digest_key}",
                        "one artifact path is bound more than once",
                    )
                )
                continue
            seen_paths.add(resolved)
            actual_digest, size = _sha256_and_size(path)
        except OSError:
            findings.append(
                Finding(
                    "ARTIFACT_UNREADABLE",
                    f"/digests/{binding.digest_key}",
                    "bound artifact could not be read safely",
                )
            )
            continue

        total_bytes += size
        expected_digest = digests.get(binding.digest_key) if isinstance(digests, dict) else None
        if expected_digest is None:
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_MISSING",
                    f"/digests/{binding.digest_key}",
                    "receipt has no digest for the bound artifact",
                )
            )
        elif expected_digest != actual_digest:
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_MISMATCH",
                    f"/digests/{binding.digest_key}",
                    "bound artifact bytes do not match the receipt digest",
                )
            )

    if bindings and receipt.get("bytes_in") != total_bytes:
        findings.append(
            Finding(
                "BYTE_COUNT_MISMATCH",
                "/bytes_in",
                "bytes_in does not equal the unique bound artifact byte total",
            )
        )
    return findings


def validate_receipt(
    receipt_path: Path,
    *,
    source_descriptor_path: Path | None = None,
    source_head_key: str = "source_head",
    artifacts: Sequence[ArtifactBinding] = (),
    require_success: bool = False,
) -> ValidationResult:
    """Validate one receipt and any requested source/artifact bindings."""

    receipt, findings = _load_json_object(receipt_path, "/receipt")
    if receipt is None:
        return ValidationResult(tuple(sorted(findings)), None, len(artifacts), False)

    receipt_validator = _load_schema_validator(RECEIPT_SCHEMA)
    findings.extend(_schema_findings(receipt_validator, receipt, ""))
    findings.extend(_semantic_findings(receipt, require_success))

    source_head_bound = False
    if source_descriptor_path is not None:
        descriptor, descriptor_findings = _load_json_object(
            source_descriptor_path,
            "/source_descriptor",
        )
        findings.extend(descriptor_findings)
        if descriptor is not None:
            descriptor_validator = _load_schema_validator(SOURCE_DESCRIPTOR_SCHEMA)
            schema_findings = _schema_findings(
                descriptor_validator,
                descriptor,
                "/source_descriptor",
            )
            findings.extend(schema_findings)
            if not schema_findings:
                binding_findings = _source_binding_findings(
                    receipt,
                    descriptor,
                    source_head_key,
                )
                findings.extend(binding_findings)
                source_head_bound = not binding_findings

    findings.extend(_artifact_findings(receipt, artifacts))
    outcome = receipt.get("outcome") if isinstance(receipt.get("outcome"), str) else None
    return ValidationResult(
        tuple(sorted(set(findings))),
        outcome,
        len(artifacts),
        source_head_bound,
    )


def _artifact_argument(value: str) -> ArtifactBinding:
    key, separator, raw_path = value.partition("=")
    if not separator or not key or not raw_path:
        raise argparse.ArgumentTypeError("artifact binding must be DIGEST_KEY=PATH")
    return ArtifactBinding(key, Path(raw_path))


def _render_result(path: Path, result: ValidationResult) -> tuple[str, ...]:
    if result.ok:
        return (
            "INGEST_RECEIPT_VALID "
            f"file={path.name} outcome={result.outcome} "
            f"artifacts={result.artifact_count} "
            f"source_head={'bound' if result.source_head_bound else 'not-requested'}",
        )
    return tuple(
        "INGEST_RECEIPT_INVALID "
        f"code={finding.code} field={finding.field} detail={finding.detail}"
        for finding in result.findings
    )


def _run_fixtures() -> int:
    valid_paths = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    if not valid_paths or not invalid_paths:
        print("INGEST_RECEIPT_FIXTURES_ERROR nonempty valid and invalid lanes are required")
        return 2

    failures: list[str] = []
    for path in valid_paths:
        if not validate_receipt(path).ok:
            failures.append(f"valid/{path.name}")
    for path in invalid_paths:
        if validate_receipt(path).ok:
            failures.append(f"invalid/{path.name}")

    if failures:
        for name in sorted(failures):
            print(f"INGEST_RECEIPT_FIXTURE_POLARITY_FAIL file={name}")
        return 1
    print(
        "INGEST_RECEIPT_FIXTURES_VALID "
        f"valid={len(valid_paths)} invalid={len(invalid_paths)}"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one IngestReceipt without network access.",
    )
    parser.add_argument("receipt", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--source-descriptor", type=Path)
    parser.add_argument("--source-head-key", default="source_head")
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        type=_artifact_argument,
        metavar="DIGEST_KEY=PATH",
    )
    parser.add_argument("--require-success", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.fixtures:
        if (
            args.receipt is not None
            or args.source_descriptor is not None
            or args.artifact
            or args.require_success
            or args.source_head_key != "source_head"
        ):
            parser.error("--fixtures cannot be combined with receipt binding options")
        return _run_fixtures()
    if args.receipt is None:
        parser.error("receipt is required unless --fixtures is used")

    result = validate_receipt(
        args.receipt,
        source_descriptor_path=args.source_descriptor,
        source_head_key=args.source_head_key,
        artifacts=tuple(args.artifact),
        require_success=args.require_success,
    )
    for line in _render_result(args.receipt, result):
        print(line)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
