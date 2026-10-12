#!/usr/bin/env python3
"""Validate synthetic RunReceipt -> EvidenceBundle -> TraceReceiptLink -> TemporalSlice closure.

The validator is deterministic and no-network. It checks only local reference
and digest agreement, including the final materialized artifact bytes. A green
result does not authenticate a trace, receipt, EvidenceBundle, signature,
policy decision, release, or publication event.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/data/trace_temporal_closure"
CASES_PATH = FIXTURE_ROOT / "cases.json"
MAX_FILE_BYTES = 1_048_576
SHA256 = re.compile(r"^(?:jcs:)?sha256:[0-9a-f]{64}$")
CLOSURE_ID = re.compile(r"^urn:kfm:trace-temporal-closure:sha256:[0-9a-f]{64}$")
SCOPE = "synthetic-cross-contract-reference-and-byte-closure-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(item.code.startswith(("FILE_", "JSON_", "INPUT_", "ROOT_")) for item in self.findings)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _hex_digest(value: Any) -> str | None:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        return None
    return value.rsplit("sha256:", 1)[1]


def _nonplaceholder_digest(value: Any) -> bool:
    digest = _hex_digest(value)
    return digest is not None and set(digest) != {"0"}


def _canonical_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return "sha256:" + digest.hexdigest()


def canonical_closure_id(candidate: Mapping[str, Any]) -> str:
    run = _mapping(candidate.get("run_receipt"))
    evidence = _mapping(candidate.get("evidence_bundle"))
    temporal = _mapping(candidate.get("temporal_slice"))
    materialization = _mapping(temporal.get("materialization"))
    digests = sorted(
        str(_mapping(item).get("digest"))
        for item in _array(materialization.get("artifacts"))
    )
    anchors = [
        run.get("digest"),
        evidence.get("digest"),
        temporal.get("slice_id"),
        *digests,
    ]
    if not all(isinstance(item, str) for item in anchors):
        raise ValueError("closure anchors are incomplete")
    encoded = "\n".join(anchors).encode("utf-8")
    return "urn:kfm:trace-temporal-closure:sha256:" + hashlib.sha256(encoded).hexdigest()


def _governance_violation(value: Any) -> bool:
    governance = _mapping(value)
    return any(
        governance.get(name) is not False
        for name in (
            "authority_created",
            "evidence_closure_claimed",
            "policy_evaluated",
            "promotion_authorized",
            "release_authorized",
            "publication_authorized",
            "public_use_allowed",
        )
    )


def _semantic_findings(candidate: Mapping[str, Any], *, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    if candidate.get("record_type") != "TraceTemporalClosure":
        findings.append(Finding("RECORD_TYPE_INVALID", "/record_type"))
    if candidate.get("schema_version") != "1.0.0":
        findings.append(Finding("SCHEMA_VERSION_INVALID", "/schema_version"))
    if candidate.get("fixture_only") is not True:
        findings.append(Finding("FIXTURE_ONLY_REQUIRED", "/fixture_only"))
    if candidate.get("network_access") != "forbidden":
        findings.append(Finding("NETWORK_ACCESS_NOT_FORBIDDEN", "/network_access"))

    run = _mapping(candidate.get("run_receipt"))
    evidence = _mapping(candidate.get("evidence_bundle"))
    link = _mapping(candidate.get("trace_receipt_link"))
    link_run = _mapping(link.get("run_receipt"))
    link_evidence = _mapping(link.get("evidence_bundle"))
    link_anchor = _mapping(link.get("run_anchor"))
    temporal = _mapping(candidate.get("temporal_slice"))
    provenance = _mapping(temporal.get("provenance"))
    materialization = _mapping(temporal.get("materialization"))

    supplied_id = candidate.get("closure_id")
    if not isinstance(supplied_id, str) or not CLOSURE_ID.fullmatch(supplied_id):
        findings.append(Finding("CLOSURE_ID_FORMAT_INVALID", "/closure_id"))
    else:
        try:
            if supplied_id != canonical_closure_id(candidate):
                findings.append(Finding("CLOSURE_ID_MISMATCH", "/closure_id"))
        except ValueError:
            findings.append(Finding("CLOSURE_ID_UNVERIFIABLE", "/closure_id"))

    digest_fields = {
        "/run_receipt/digest": run.get("digest"),
        "/evidence_bundle/digest": evidence.get("digest"),
        "/evidence_bundle/run_receipt_digest": evidence.get("run_receipt_digest"),
        "/trace_receipt_link/run_receipt/digest": link_run.get("digest"),
        "/trace_receipt_link/evidence_bundle/digest": link_evidence.get("digest"),
    }
    for field, value in digest_fields.items():
        if not _nonplaceholder_digest(value):
            findings.append(Finding("DIGEST_INVALID_OR_PLACEHOLDER", field))

    if not (run.get("digest") == evidence.get("run_receipt_digest") == link_run.get("digest")):
        findings.append(Finding("RUN_RECEIPT_DIGEST_MISMATCH", "/run_receipt/digest"))
    if evidence.get("digest") != link_evidence.get("digest"):
        findings.append(Finding("EVIDENCE_DIGEST_MISMATCH", "/evidence_bundle/digest"))
    if run.get("receipt_ref") != link_run.get("receipt_ref"):
        findings.append(Finding("RUN_RECEIPT_REF_MISMATCH", "/trace_receipt_link/run_receipt/receipt_ref"))
    if evidence.get("bundle_ref") != link_evidence.get("bundle_ref"):
        findings.append(Finding("EVIDENCE_REF_MISMATCH", "/trace_receipt_link/evidence_bundle/bundle_ref"))

    run_ids = (run.get("run_id"), evidence.get("run_id"), link_run.get("run_id"), link_evidence.get("run_id"), link_anchor.get("run_id"))
    if len(set(run_ids)) != 1:
        findings.append(Finding("RUN_ID_MISMATCH", "/run_receipt/run_id"))
    spec_hex = tuple(_hex_digest(value) for value in (run.get("spec_hash"), evidence.get("spec_hash"), link_run.get("spec_hash"), link_evidence.get("spec_hash"), link_anchor.get("spec_hash"), provenance.get("spec_hash")))
    if any(value is None for value in spec_hex) or len(set(spec_hex)) != 1:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/temporal_slice/provenance/spec_hash"))

    if provenance.get("run_receipt_ref") != run.get("receipt_ref"):
        findings.append(Finding("TEMPORAL_RUN_RECEIPT_REF_MISMATCH", "/temporal_slice/provenance/run_receipt_ref"))
    evidence_refs = _array(provenance.get("evidence_bundle_refs"))
    if evidence.get("bundle_ref") not in evidence_refs:
        findings.append(Finding("TEMPORAL_EVIDENCE_REF_MISMATCH", "/temporal_slice/provenance/evidence_bundle_refs"))
    if evidence_refs != sorted(set(item for item in evidence_refs if isinstance(item, str))):
        findings.append(Finding("TEMPORAL_EVIDENCE_REFS_NOT_CANONICAL", "/temporal_slice/provenance/evidence_bundle_refs"))

    artifact_refs: set[str] = set()
    for index, raw in enumerate(_array(materialization.get("artifacts"))):
        artifact = _mapping(raw)
        path_value = artifact.get("artifact_path")
        relative = _canonical_path(path_value)
        field = f"/temporal_slice/materialization/artifacts/{index}"
        if relative is None:
            findings.append(Finding("ARTIFACT_PATH_INVALID", field + "/artifact_path"))
            continue
        ref = artifact.get("artifact_ref")
        if not isinstance(ref, str) or ref in artifact_refs:
            findings.append(Finding("ARTIFACT_REF_DUPLICATE_OR_INVALID", field + "/artifact_ref"))
        else:
            artifact_refs.add(ref)
        candidate_path = repo_root.joinpath(*relative.parts)
        try:
            resolved_root = repo_root.resolve(strict=True)
            if any((resolved_root.joinpath(*relative.parts[:offset])).is_symlink() for offset in range(1, len(relative.parts) + 1)):
                findings.append(Finding("ARTIFACT_SYMLINK_DENIED", field + "/artifact_path"))
                continue
            resolved = candidate_path.resolve(strict=True)
            resolved.relative_to(resolved_root)
            if not resolved.is_file():
                raise OSError
            actual = _sha256(resolved)
        except ValueError:
            findings.append(Finding("ARTIFACT_PATH_ESCAPE", field + "/artifact_path"))
            continue
        except OSError:
            findings.append(Finding("ARTIFACT_NOT_READABLE", field + "/artifact_path"))
            continue
        if artifact.get("digest") != actual:
            findings.append(Finding("ARTIFACT_DIGEST_MISMATCH", field + "/digest"))

    if _governance_violation(candidate.get("governance")) or _governance_violation(temporal.get("governance")):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_candidate(candidate: Mapping[str, Any], *, repo_root: Path = REPO_ROOT) -> ValidationResult:
    findings = _semantic_findings(candidate, repo_root=repo_root)
    return ValidationResult(tuple(sorted(set(findings))))


def validate_closure(path: Path, *, repo_root: Path = REPO_ROOT) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_candidate(candidate, repo_root=repo_root).findings)
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _apply_case_patch(base: Mapping[str, Any], changes: Mapping[str, Any]) -> dict[str, Any]:
    import copy

    candidate = copy.deepcopy(dict(base))
    for pointer, value in sorted(changes.items()):
        if not isinstance(pointer, str) or not pointer.startswith("/"):
            raise ValueError
        parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
        target: Any = candidate
        for part in parts[:-1]:
            target = target[int(part)] if isinstance(target, list) else target[part]
        final = parts[-1]
        if isinstance(value, Mapping) and value.get("$delete") is True:
            if isinstance(target, list):
                del target[int(final)]
            else:
                del target[final]
        elif isinstance(target, list):
            target[int(final)] = value
        else:
            target[final] = value
    return candidate


def fixture_cases() -> tuple[Mapping[str, Any], list[tuple[str, Mapping[str, Any], list[str]]]]:
    value = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("base"), dict) or not isinstance(value.get("invalid"), list):
        raise ValueError
    base = value["base"]
    invalid: list[tuple[str, Mapping[str, Any], list[str]]] = []
    for entry in value["invalid"]:
        if not isinstance(entry, Mapping) or not isinstance(entry.get("set"), Mapping) or not isinstance(entry.get("expected"), list):
            raise ValueError
        invalid.append((str(entry.get("name", "invalid")), _apply_case_patch(base, entry["set"]), [str(code) for code in entry["expected"]]))
    return base, invalid


def validate_fixtures() -> int:
    try:
        base, invalid_cases = fixture_cases()
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError):
        print("ERROR: closure case manifest is unavailable or invalid.")
        return 1
    if not invalid_cases:
        print("ERROR: closure invalid case lane must be non-empty.")
        return 1
    failed = False
    valid_result = validate_candidate(base)
    print(_serialize(Path("valid_closure.json"), valid_result))
    failed = failed or not valid_result.ok
    for name, candidate, expected in invalid_cases:
        result = validate_candidate(candidate)
        print(_serialize(Path(name + ".json"), result))
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(expected)
        failed = failed or result.ok or actual != expected
        if actual != expected:
            print(json.dumps({"actual": actual, "expected": expected, "file": name, "outcome": "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    if failed:
        return 1
    print(f"CONFIRMED: 1 valid and {len(invalid_cases)} invalid trace-temporal closure cases passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files or args.repo_root != REPO_ROOT:
            parser.error("--fixtures cannot be combined with explicit files or --repo-root")
        return validate_fixtures()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_closure(path, repo_root=args.repo_root)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
