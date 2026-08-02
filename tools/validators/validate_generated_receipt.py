"""Validate GENERATED_RECEIPT provenance records without network access.

This validator binds the repository-authoring receipt schema to final local
artifact bytes.  A successful default validation proves bounded shape,
cross-field, and SHA-256 integrity checks only.  An optional gate can require a
receipt to contain an approval or override claim, but the validator does not
authenticate that claim.  No result grants truth, policy, review, mutation,
merge, release, or publication authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry


RECEIPT_SCHEMA = (
    REPO_ROOT / "schemas/contracts/v1/receipts/generated_receipt.schema.json"
)
FIXTURES_ROOT = REPO_ROOT / "fixtures/generated_receipt"
CONTRACT_VERSION = "3.0.0"
MAX_JSON_BYTES = 5 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_ARTIFACTS = 1_000
MAX_ARTIFACT_BYTES = 64 * 1024 * 1024
MAX_TOTAL_ARTIFACT_BYTES = 256 * 1024 * 1024
POLICY_DECISION_ROOTS = (
    "policy/",
    "schemas/contracts/v1/",
    "data/registry/",
    "release/",
)
DOCUMENT_SUFFIXES = frozenset({".md", ".markdown", ".mdx", ".rst"})


@dataclass(frozen=True, order=True)
class Finding:
    """One deterministic failure that does not contain receipt values."""

    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class ValidationResult:
    """Bounded result for one GENERATED_RECEIPT candidate."""

    findings: tuple[Finding, ...]
    artifact_count: int
    review_state: str | None
    integrity_checked: bool
    review_claim_present: bool

    @property
    def ok(self) -> bool:
        return not self.findings


class DuplicateKeyError(ValueError):
    """Raised when any parsed JSON object repeats a member name."""


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number token."""


def _reject_nonfinite_number(_value: str) -> object:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _load_schema_validator() -> Draft202012Validator:
    schema = json.loads(RECEIPT_SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(
        schema,
        registry=build_registry(REPO_ROOT),
        format_checker=FormatChecker(),
    )


def _load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [
                Finding("INPUT_SYMLINK_DENIED", "/receipt", "symbolic links are denied")
            ]
        if not path.is_file():
            return None, [
                Finding("INPUT_NOT_FILE", "/receipt", "input is not a regular file")
            ]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [
                Finding("INPUT_TOO_LARGE", "/receipt", "JSON input exceeds 5 MiB")
            ]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_number,
            parse_float=_parse_finite_float,
        )
    except (OSError, UnicodeError):
        return None, [
            Finding("INPUT_UNREADABLE", "/receipt", "input could not be read safely")
        ]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/receipt", "input is not valid JSON")]
    except DuplicateKeyError:
        return None, [
            Finding(
                "JSON_DUPLICATE_KEY",
                "/receipt",
                "JSON objects must not contain duplicate member names",
            )
        ]
    except NonFiniteNumberError:
        return None, [
            Finding(
                "JSON_NONFINITE_NUMBER",
                "/receipt",
                "JSON numbers must be finite and standards-conforming",
            )
        ]
    except (RecursionError, ValueError):
        return None, [
            Finding(
                "JSON_COMPLEXITY_LIMIT",
                "/receipt",
                "JSON input exceeds parser complexity limits",
            )
        ]

    if not isinstance(value, dict):
        return None, [
            Finding("JSON_ROOT_INVALID", "/receipt", "JSON root must be an object")
        ]
    return value, []


def _json_pointer(error_path: Iterable[object]) -> str:
    parts = [str(part).replace("~", "~0").replace("/", "~1") for part in error_path]
    return "/" + "/".join(parts) if parts else "/"


def _schema_findings(
    validator: Draft202012Validator,
    receipt: Mapping[str, object],
) -> list[Finding]:
    try:
        errors = list(
            islice(validator.iter_errors(receipt), MAX_SCHEMA_FINDINGS + 1)
        )
    except (RecursionError, ValueError):
        return [
            Finding(
                "SCHEMA_EVALUATION_LIMIT",
                "/receipt",
                "schema evaluation exceeded bounded complexity limits",
            )
        ]

    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    errors = sorted(
        errors,
        key=lambda error: (_json_pointer(error.absolute_path), str(error.validator)),
    )[:MAX_SCHEMA_FINDINGS]
    findings = [
        Finding(
            "SCHEMA_INVALID",
            _json_pointer(error.absolute_path),
            f"schema constraint failed: {error.validator}",
        )
        for error in errors
    ]
    if truncated:
        findings.append(
            Finding(
                "SCHEMA_FINDINGS_TRUNCATED",
                "/receipt",
                "schema findings were truncated at the 100-finding output limit",
            )
        )
    return findings


def _artifact_paths(receipt: Mapping[str, object]) -> list[str]:
    value = receipt.get("artifact_paths")
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _review_claim_present(receipt: Mapping[str, object]) -> bool:
    review = receipt.get("human_review")
    approved = isinstance(review, dict) and review.get("state") == "approved"
    return approved or isinstance(receipt.get("override_record"), dict)


def _semantic_findings(
    receipt: Mapping[str, object],
    *,
    require_review_claim: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    paths = _artifact_paths(receipt)
    hashes = receipt.get("artifact_hashes")
    labels = receipt.get("truth_labels")
    path_keys = set(paths)

    if receipt.get("contract_version") != CONTRACT_VERSION:
        findings.append(
            Finding(
                "CONTRACT_VERSION_UNSUPPORTED",
                "/contract_version",
                "receipt must use the current AI-build contract version",
            )
        )
    if isinstance(hashes, dict) and set(hashes) != path_keys:
        findings.append(
            Finding(
                "ARTIFACT_HASH_KEYS_MISMATCH",
                "/artifact_hashes",
                "artifact hash keys must exactly match artifact_paths",
            )
        )
    if isinstance(labels, dict) and set(labels) != path_keys:
        findings.append(
            Finding(
                "TRUTH_LABEL_KEYS_MISMATCH",
                "/truth_labels",
                "truth label keys must exactly match artifact_paths",
            )
        )
    if len(paths) > MAX_ARTIFACTS:
        findings.append(
            Finding(
                "ARTIFACT_COUNT_EXCEEDED",
                "/artifact_paths",
                "receipt exceeds the 1000-artifact validation budget",
            )
        )

    decisions = receipt.get("policy_decisions")
    if any(path.startswith(POLICY_DECISION_ROOTS) for path in paths) and not decisions:
        findings.append(
            Finding(
                "POLICY_DECISION_REQUIRED",
                "/policy_decisions",
                "governed responsibility roots require a policy decision reference",
            )
        )

    citations = receipt.get("citations")
    if (
        any(PurePosixPath(path).suffix.lower() in DOCUMENT_SUFFIXES for path in paths)
        and not citations
    ):
        findings.append(
            Finding(
                "DOCUMENT_CITATIONS_REQUIRED",
                "/citations",
                "documentation artifacts require citation records",
            )
        )

    if require_review_claim and not _review_claim_present(receipt):
        findings.append(
            Finding(
                "REVIEW_CLAIM_MISSING",
                "/human_review/state",
                "receipt must declare approved review or a non-null override; "
                "external authority is not verified",
            )
        )
    return findings


def _canonical_artifact_path(value: str) -> PurePosixPath | None:
    if not value or "\\" in value or value.startswith("/"):
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {".", ".."} for part in path.parts):
        return None
    return path


def _has_symlink_component(root: Path, path: PurePosixPath) -> bool:
    candidate = root
    for part in path.parts:
        candidate = candidate / part
        if candidate.is_symlink():
            return True
    return False


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"


def _integrity_findings(
    receipt: Mapping[str, object],
    receipt_path: Path,
    repo_root: Path,
) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if repo_root.is_symlink():
            return [
                Finding(
                    "REPO_ROOT_SYMLINK_DENIED",
                    "/repo_root",
                    "symbolic-link repository roots are denied",
                )
            ]
        if not repo_root.is_dir():
            return [
                Finding(
                    "REPO_ROOT_INVALID",
                    "/repo_root",
                    "repository root is not a directory",
                )
            ]
        resolved_root = repo_root.resolve(strict=True)
        resolved_receipt = receipt_path.resolve(strict=True)
    except OSError:
        return [
            Finding(
                "REPO_ROOT_UNREADABLE",
                "/repo_root",
                "repository root could not be resolved safely",
            )
        ]

    hashes = receipt.get("artifact_hashes")
    if not isinstance(hashes, dict):
        return findings
    paths = _artifact_paths(receipt)
    if len(paths) > MAX_ARTIFACTS:
        return findings

    candidates: list[tuple[int, Path, str]] = []
    total_bytes = 0
    for index, raw_path in enumerate(paths):
        field = f"/artifact_paths/{index}"
        relative = _canonical_artifact_path(raw_path)
        if relative is None:
            findings.append(
                Finding(
                    "ARTIFACT_PATH_INVALID",
                    field,
                    "artifact path must be canonical, POSIX, and repository-relative",
                )
            )
            continue

        candidate = resolved_root.joinpath(*relative.parts)
        try:
            if _has_symlink_component(resolved_root, relative):
                findings.append(
                    Finding(
                        "ARTIFACT_SYMLINK_DENIED",
                        field,
                        "symbolic-link artifact paths are denied",
                    )
                )
                continue
            if not candidate.is_file():
                findings.append(
                    Finding(
                        "ARTIFACT_NOT_FILE",
                        field,
                        "artifact is not a regular file",
                    )
                )
                continue
            resolved_candidate = candidate.resolve(strict=True)
            resolved_candidate.relative_to(resolved_root)
            if resolved_candidate == resolved_receipt:
                findings.append(
                    Finding(
                        "RECEIPT_SELF_REFERENCE_DENIED",
                        field,
                        "receipt must not bind its own bytes",
                    )
                )
                continue
            size = resolved_candidate.stat().st_size
        except ValueError:
            findings.append(
                Finding(
                    "ARTIFACT_PATH_ESCAPE",
                    field,
                    "artifact resolves outside the repository root",
                )
            )
            continue
        except OSError:
            findings.append(
                Finding(
                    "ARTIFACT_UNREADABLE",
                    field,
                    "artifact could not be inspected safely",
                )
            )
            continue

        if size > MAX_ARTIFACT_BYTES:
            findings.append(
                Finding(
                    "ARTIFACT_TOO_LARGE",
                    field,
                    "artifact exceeds the 64 MiB validation budget",
                )
            )
            continue
        total_bytes += size
        expected = hashes.get(raw_path)
        if isinstance(expected, str):
            candidates.append((index, resolved_candidate, expected))

    if total_bytes > MAX_TOTAL_ARTIFACT_BYTES:
        findings.append(
            Finding(
                "ARTIFACT_TOTAL_TOO_LARGE",
                "/artifact_paths",
                "artifact set exceeds the 256 MiB validation budget",
            )
        )
        return findings

    for index, candidate, expected in candidates:
        field = f"/artifact_paths/{index}"
        algorithm, separator, encoded = expected.partition(":")
        if algorithm == "blake3" and separator:
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_UNSUPPORTED",
                    field,
                    "BLAKE3 verification requires an explicitly admitted dependency",
                )
            )
            continue
        if algorithm != "sha256" or not separator or not 32 <= len(encoded) <= 64:
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_INVALID",
                    field,
                    "SHA-256 artifact digests must contain 32 to 64 hex characters",
                )
            )
            continue
        if set(encoded) == {"0"}:
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_PLACEHOLDER_DENIED",
                    field,
                    "all-zero artifact digest placeholders are denied",
                )
            )
            continue
        try:
            actual = _sha256(candidate)
        except OSError:
            findings.append(
                Finding(
                    "ARTIFACT_UNREADABLE",
                    field,
                    "artifact could not be hashed safely",
                )
            )
            continue
        if not actual.removeprefix("sha256:").startswith(encoded):
            findings.append(
                Finding(
                    "ARTIFACT_DIGEST_MISMATCH",
                    field,
                    "artifact bytes do not match the receipt digest",
                )
            )
    return findings


def validate_receipt(
    receipt_path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    verify_integrity: bool = True,
    require_review_claim: bool = False,
) -> ValidationResult:
    """Validate one generated receipt against bounded local evidence."""

    receipt, findings = _load_json_object(receipt_path)
    if receipt is None:
        return ValidationResult(tuple(sorted(findings)), 0, None, False, False)

    paths = _artifact_paths(receipt)
    review = receipt.get("human_review")
    review_state = review.get("state") if isinstance(review, dict) else None
    review_claim_present = _review_claim_present(receipt)

    schema_findings = _schema_findings(_load_schema_validator(), receipt)
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(
            _semantic_findings(receipt, require_review_claim=require_review_claim)
        )
        if verify_integrity:
            findings.extend(_integrity_findings(receipt, receipt_path, repo_root))

    return ValidationResult(
        tuple(sorted(set(findings))),
        len(paths),
        review_state if isinstance(review_state, str) else None,
        verify_integrity and not schema_findings,
        review_claim_present,
    )


def _render_result(path: Path, result: ValidationResult) -> tuple[str, ...]:
    if result.ok:
        return (
            "GENERATED_RECEIPT_VALID "
            f"file={path.name} artifacts={result.artifact_count} "
            f"integrity={'bound' if result.integrity_checked else 'not-requested'} "
            f"review={result.review_state} "
            f"review_claim={'present' if result.review_claim_present else 'absent'}",
        )
    return tuple(
        "GENERATED_RECEIPT_INVALID "
        f"code={finding.code} field={finding.field} detail={finding.detail}"
        for finding in result.findings
    )


def _expected_finding(path: Path) -> Finding | None:
    sidecar = path.with_suffix(".expected_error.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 1024:
            return None
        lines = [line for line in sidecar.read_text(encoding="utf-8").splitlines() if line]
    except (OSError, UnicodeError):
        return None
    if len(lines) != 1:
        return None
    parts = lines[0].split("|", 2)
    if len(parts) != 3 or not all(parts):
        return None
    return Finding(parts[0], parts[1], parts[2])


def _run_fixtures() -> int:
    valid_paths = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
    invalid_paths = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    if not valid_paths or not invalid_paths:
        print(
            "GENERATED_RECEIPT_FIXTURES_ERROR "
            "nonempty valid and invalid lanes are required"
        )
        return 2

    failures: list[str] = []
    for path in valid_paths:
        if not validate_receipt(path).ok:
            failures.append(f"valid/{path.name}")
    for path in invalid_paths:
        result = validate_receipt(path)
        expected = _expected_finding(path)
        if expected is None or result.findings != (expected,):
            failures.append(f"invalid/{path.name}")

    if failures:
        for name in sorted(failures):
            print(f"GENERATED_RECEIPT_FIXTURE_POLARITY_FAIL file={name}")
        return 1
    print(
        "GENERATED_RECEIPT_FIXTURES_VALID "
        f"valid={len(valid_paths)} invalid={len(invalid_paths)} integrity=bound"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate one GENERATED_RECEIPT and its local artifact bindings "
            "without network access."
        )
    )
    parser.add_argument("receipt", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument(
        "--require-review-claim",
        action="store_true",
        help=(
            "require an approved-review or override claim in the receipt; "
            "does not authenticate or authorize the claim"
        ),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.fixtures:
        if (
            args.receipt is not None
            or args.require_review_claim
            or args.repo_root != REPO_ROOT
        ):
            parser.error("--fixtures cannot be combined with receipt options")
        return _run_fixtures()
    if args.receipt is None:
        parser.error("receipt is required unless --fixtures is used")

    result = validate_receipt(
        args.receipt,
        repo_root=args.repo_root,
        require_review_claim=args.require_review_claim,
    )
    for line in _render_result(args.receipt, result):
        print(line)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
