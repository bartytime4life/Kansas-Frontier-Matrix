#!/usr/bin/env python3
"""Validate fixture-only SourceArtifact-to-ClaimFieldBinding chain closure.

PASS proves bounded synthetic shape, executable ParseResult conformance, exact
reference closure, and all-false authority effects only. The validator does not
fetch sources, expose values, resolve EvidenceBundles, evaluate policy, write
lifecycle state, release, or publish.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
CONNECTORS_SRC = ROOT / "packages/connectors-core/src"
for source_root in (str(ROOT), str(HASH_SRC), str(CONNECTORS_SRC)):
    if source_root not in sys.path:
        sys.path.insert(0, source_root)

from connectors_core.source_adapter import (  # noqa: E402
    AdapterBoundaryError,
    ParseFinding,
    ParseOutcome,
    ParseResult,
)
from hashing import compute_spec_hash  # noqa: E402
from tools.validators import validate_claim_field_binding as field_binding_validator  # noqa: E402
from tools.validators._common.local_resolver import build_registry  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/evidence/evidence_binding_chain_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/evidence_binding_chain_assessment"
BASELINE = FIXTURES / "valid_assessment.json"
CASES = FIXTURES / "cases.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "synthetic-evidence-binding-reference-closure-only"
ZERO_DIGEST = "sha256:" + "0" * 64
FALSE_EFFECTS = {
    "source_activated": False,
    "evidence_created": False,
    "evidence_resolved": False,
    "evidence_bundle_created": False,
    "policy_evaluated": False,
    "review_approved": False,
    "released": False,
    "published": False,
}
PARSE_AUTHORITY_FIELDS = (
    "authority_created",
    "evidence_created",
    "lifecycle_write_allowed",
    "receipt_created",
    "release_authorized",
    "publication_authorized",
    "public_use_allowed",
    "repository_mutation_allowed",
)
ERROR_CODES = {
    "ASSESSMENT_ID_MISMATCH",
    "ASSESSMENT_SPEC_HASH_MISMATCH",
    "CLAIM_FIELD_BINDING_ID_MISMATCH",
    "FIXTURE_MANIFEST_INVALID",
    "HASHING_UNAVAILABLE",
    "INPUT_NOT_FILE",
    "INPUT_READ_ERROR",
    "INPUT_SYMLINK_DENIED",
    "INPUT_TOO_LARGE",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "OBSERVATION_DIGEST_PLACEHOLDER",
    "PARSE_RESULT_ID_MISMATCH",
    "PARSE_RESULT_MODEL_INVALID",
    "PARSE_RESULT_SPEC_HASH_MISMATCH",
    "ROOT_NOT_OBJECT",
    "SCHEMA_FINDINGS_TRUNCATED",
    "SCHEMA_INVALID",
    "SCHEMA_UNAVAILABLE",
    "SOURCE_ARTIFACT_IDENTITY_INVALID",
    "SOURCE_CONTENT_DIGEST_PLACEHOLDER",
    "SPEC_HASH_MISMATCH",
}
ABSTAIN_CODES = {
    "PARSED_RECORD_UNRESOLVED",
    "PARSE_RESULT_NOT_PARSED",
    "SOURCE_ARTIFACT_NOT_FETCHED",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except FileNotFoundError:
        return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            registry=build_registry(ROOT),
            format_checker=FormatChecker(),
        )
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical_strings(value: Any, *, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def parse_identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("parse_result_ref", None)
    subject.pop("spec_hash", None)
    return subject


def expected_parse_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash(parse_identity_subject(candidate))


def expected_parse_ref(candidate: Mapping[str, Any]) -> str:
    return "parse-result:" + expected_parse_hash(candidate)


def assign_parse_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = expected_parse_hash(result)
    result["parse_result_ref"] = expected_parse_ref(result)
    return result


def assessment_identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_assessment_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash(assessment_identity_subject(candidate))


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    return "evidence-binding-chain:" + expected_assessment_hash(candidate).removeprefix("sha256:")[:24]


def assign_assessment_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = expected_assessment_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _parse_result_model(candidate: Mapping[str, Any]) -> ParseResult:
    records = candidate.get("records") if isinstance(candidate.get("records"), list) else []
    findings = candidate.get("findings") if isinstance(candidate.get("findings"), list) else []
    flags = candidate.get("unsupported_flags") if isinstance(candidate.get("unsupported_flags"), list) else []
    return ParseResult(
        source_artifact_ref=candidate["source_artifact_ref"],
        parser_id=candidate["parser_id"],
        parser_version=candidate["parser_version"],
        parser_spec_digest=candidate["parser_spec_digest"],
        outcome=ParseOutcome(candidate["outcome"]),
        records=tuple(copy.deepcopy(records)),
        findings=tuple(ParseFinding(item["code"], item["path"]) for item in findings),
        unsupported_flags=tuple(flags),
        source_conflict_ref=candidate.get("source_conflict_ref"),
        **{field: candidate[field] for field in PARSE_AUTHORITY_FIELDS},
    )


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if candidate.get("spec_hash") != expected_assessment_hash(candidate):
            findings.append(Finding("ASSESSMENT_SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("assessment_id") != expected_assessment_id(candidate):
            findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    except (TypeError, ValueError, RuntimeError):
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))

    if not _canonical_strings(candidate.get("limitations")):
        findings.append(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))

    artifact = candidate.get("source_artifact") if isinstance(candidate.get("source_artifact"), Mapping) else {}
    content_digest = artifact.get("content_digest")
    if content_digest == ZERO_DIGEST:
        findings.append(Finding("SOURCE_CONTENT_DIGEST_PLACEHOLDER", "/source_artifact/content_digest"))
    if isinstance(content_digest, str):
        expected_artifact = "source-artifact:" + content_digest
        expected_storage = "cas:" + content_digest
        if artifact.get("artifact_id") != expected_artifact or artifact.get("immutable_storage_ref") != expected_storage:
            findings.append(Finding("SOURCE_ARTIFACT_IDENTITY_INVALID", "/source_artifact/artifact_id"))
    if artifact.get("retrieval_outcome") != "FETCHED":
        findings.append(Finding("SOURCE_ARTIFACT_NOT_FETCHED", "/source_artifact/retrieval_outcome"))

    parse_result = candidate.get("parse_result") if isinstance(candidate.get("parse_result"), Mapping) else {}
    try:
        if parse_result.get("spec_hash") != expected_parse_hash(parse_result):
            findings.append(Finding("PARSE_RESULT_SPEC_HASH_MISMATCH", "/parse_result/spec_hash"))
        if parse_result.get("parse_result_ref") != expected_parse_ref(parse_result):
            findings.append(Finding("PARSE_RESULT_ID_MISMATCH", "/parse_result/parse_result_ref"))
        model = _parse_result_model(parse_result)
    except (AdapterBoundaryError, KeyError, TypeError, ValueError, RuntimeError):
        model = None
        findings.append(Finding("PARSE_RESULT_MODEL_INVALID", "/parse_result"))

    if parse_result.get("source_artifact_ref") != artifact.get("artifact_id"):
        findings.append(Finding("PARSE_ARTIFACT_REF_MISMATCH", "/parse_result/source_artifact_ref"))
    artifact_parser = artifact.get("parser") if isinstance(artifact.get("parser"), Mapping) else {}
    parser_tuple = (
        parse_result.get("parser_id"),
        parse_result.get("parser_version"),
        parse_result.get("parser_spec_digest"),
    )
    artifact_parser_tuple = (
        artifact_parser.get("parser_id"),
        artifact_parser.get("version"),
        artifact_parser.get("spec_digest"),
    )
    if parser_tuple != artifact_parser_tuple:
        findings.append(Finding("SOURCE_PARSER_IDENTITY_MISMATCH", "/parse_result/parser_id"))
    if parse_result.get("outcome") != "PARSED":
        findings.append(Finding("PARSE_RESULT_NOT_PARSED", "/parse_result/outcome"))

    records = parse_result.get("records") if isinstance(parse_result.get("records"), list) else []
    record_refs = [record.get("record_ref") for record in records if isinstance(record, Mapping)]
    if record_refs != sorted(record_refs) or len(record_refs) != len(set(record_refs)):
        findings.append(Finding("PARSED_RECORDS_NOT_CANONICAL", "/parse_result/records"))
    for index, record in enumerate(records):
        if isinstance(record, Mapping) and record.get("record_digest") == ZERO_DIGEST:
            findings.append(Finding("PARSED_RECORD_DIGEST_PLACEHOLDER", f"/parse_result/records/{index}/record_digest"))

    evidence_ref = candidate.get("evidence_ref") if isinstance(candidate.get("evidence_ref"), Mapping) else {}
    resolution = candidate.get("evidence_resolution") if isinstance(candidate.get("evidence_resolution"), Mapping) else {}
    if resolution.get("evidence_ref") != evidence_ref.get("ref"):
        findings.append(Finding("EVIDENCE_REF_MISMATCH", "/evidence_resolution/evidence_ref"))
    if resolution.get("source_artifact_ref") != artifact.get("artifact_id"):
        findings.append(Finding("RESOLUTION_SOURCE_ARTIFACT_MISMATCH", "/evidence_resolution/source_artifact_ref"))
    if resolution.get("parse_result_ref") != parse_result.get("parse_result_ref"):
        findings.append(Finding("RESOLUTION_PARSE_RESULT_MISMATCH", "/evidence_resolution/parse_result_ref"))
    if not _canonical_strings(resolution.get("limitations")):
        findings.append(Finding("RESOLUTION_LIMITATIONS_NOT_CANONICAL", "/evidence_resolution/limitations"))
    if resolution.get("supported_observation_digest") == ZERO_DIGEST:
        findings.append(Finding("OBSERVATION_DIGEST_PLACEHOLDER", "/evidence_resolution/supported_observation_digest"))

    record_by_ref = {
        record.get("record_ref"): record
        for record in records
        if isinstance(record, Mapping) and isinstance(record.get("record_ref"), str)
    }
    resolved_record = record_by_ref.get(resolution.get("parsed_record_ref"))
    if not isinstance(resolved_record, Mapping):
        findings.append(Finding("PARSED_RECORD_UNRESOLVED", "/evidence_resolution/parsed_record_ref"))
    else:
        if resolution.get("parsed_record_digest") != resolved_record.get("record_digest"):
            findings.append(Finding("PARSED_RECORD_DIGEST_MISMATCH", "/evidence_resolution/parsed_record_digest"))
        if resolution.get("cited_native_locator") != resolved_record.get("native_locator"):
            findings.append(Finding("PARSED_RECORD_LOCATOR_MISMATCH", "/evidence_resolution/cited_native_locator"))

    binding = candidate.get("claim_field_binding") if isinstance(candidate.get("claim_field_binding"), Mapping) else {}
    nested_result = field_binding_validator.validate_payload(binding)
    findings.extend(
        Finding(item.code, "/claim_field_binding" + (item.path if item.path != "/" else ""))
        for item in nested_result.findings
    )
    if binding.get("source_artifact_ref") != artifact.get("artifact_id"):
        findings.append(Finding("CLAIM_SOURCE_ARTIFACT_MISMATCH", "/claim_field_binding/source_artifact_ref"))
    if isinstance(content_digest, str):
        expected_snapshot = "kfm:source-snapshot:" + content_digest.removeprefix("sha256:")
        if binding.get("source_snapshot_ref") != expected_snapshot:
            findings.append(Finding("CLAIM_SOURCE_SNAPSHOT_MISMATCH", "/claim_field_binding/source_snapshot_ref"))
    if binding.get("evidence_ref") != evidence_ref.get("ref"):
        findings.append(Finding("CLAIM_EVIDENCE_REF_MISMATCH", "/claim_field_binding/evidence_ref"))
    if binding.get("native_locator") != resolution.get("cited_native_locator"):
        findings.append(Finding("CLAIM_NATIVE_LOCATOR_MISMATCH", "/claim_field_binding/native_locator"))
    if binding.get("native_value_digest") != resolution.get("supported_observation_digest"):
        findings.append(Finding("CLAIM_NATIVE_VALUE_DIGEST_MISMATCH", "/claim_field_binding/native_value_digest"))
    transform = binding.get("transform") if isinstance(binding.get("transform"), Mapping) else {}
    if transform.get("kind") == "NONE" and binding.get("native_value_digest") != binding.get("normalized_value_digest"):
        findings.append(Finding("NO_TRANSFORM_VALUE_DIGEST_MISMATCH", "/claim_field_binding/normalized_value_digest"))

    if candidate.get("public_use_allowed") is not False:
        findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("evidence_bundle_ref") is not None:
        findings.append(Finding("EVIDENCE_BUNDLE_OVERCLAIM", "/evidence_bundle_ref"))
    if candidate.get("release_ref") is not None:
        findings.append(Finding("RELEASE_OVERCLAIM", "/release_ref"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("AUTHORITY_EFFECT_ENABLED", "/effects"))

    if model is not None and model.record_count != len(records):
        findings.append(Finding("PARSE_RESULT_MODEL_COUNT_MISMATCH", "/parse_result/records"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    ordered = tuple(sorted(set(findings)))
    codes = {finding.code for finding in ordered}
    if not ordered:
        outcome = "PASS"
    elif codes & ERROR_CODES:
        outcome = "ERROR"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, ordered)


def validate(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _mutation(candidate: Any, operation: Mapping[str, Any]) -> None:
    pointer = operation.get("path")
    op = operation.get("op")
    if not isinstance(pointer, str) or not pointer.startswith("/") or pointer == "/":
        raise ValueError("invalid mutation pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    current = candidate
    for raw in parts[:-1]:
        current = current[int(raw)] if isinstance(current, list) else current[raw]
    key = parts[-1]
    if op == "remove":
        if isinstance(current, list):
            current.pop(int(key))
        else:
            del current[key]
        return
    if op not in {"add", "replace"} or "value" not in operation:
        raise ValueError("unsupported mutation")
    value = copy.deepcopy(operation["value"])
    if isinstance(current, list):
        index = int(key)
        if op == "add":
            current.insert(index, value)
        else:
            current[index] = value
    else:
        current[key] = value


def materialize_case(baseline: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(baseline))
    for operation in case.get("mutations", []):
        _mutation(candidate, operation)

    nested_mode = case.get("nested_identity_mode", "RECOMPUTE")
    if nested_mode not in {"RECOMPUTE", "STALE_PARSE", "STALE_BINDING"}:
        raise ValueError("unknown nested identity mode")
    if nested_mode != "STALE_PARSE":
        candidate["parse_result"] = assign_parse_identity(candidate["parse_result"])
    if case.get("relink_parse_result") is True:
        candidate["evidence_resolution"]["parse_result_ref"] = candidate["parse_result"]["parse_result_ref"]
    if nested_mode != "STALE_BINDING":
        candidate["claim_field_binding"] = field_binding_validator.assign_identity(candidate["claim_field_binding"])

    identity_mode = case.get("assessment_identity_mode", "RECOMPUTE")
    candidate = assign_assessment_identity(candidate)
    if identity_mode == "STALE_SPEC_HASH":
        candidate["spec_hash"] = ZERO_DIGEST
    elif identity_mode == "STALE_ID":
        candidate["assessment_id"] = "evidence-binding-chain:" + "0" * 24
    elif identity_mode != "RECOMPUTE":
        raise ValueError("unknown assessment identity mode")
    return candidate


def run_fixtures() -> int:
    try:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        suite = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    passed = True
    for case in suite.get("cases", []):
        try:
            candidate = materialize_case(baseline, case)
            result = validate_payload(candidate)
            codes = sorted({finding.code for finding in result.findings})
        except (KeyError, TypeError, ValueError, RecursionError):
            result = ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),))
            codes = ["FIXTURE_MANIFEST_INVALID"]
        match = result.outcome == case.get("expected_outcome") and codes == case.get("expected_findings")
        print(
            json.dumps(
                {
                    "case_id": case.get("case_id"),
                    "outcome": result.outcome,
                    "findings": codes,
                    "suite_match": match,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and match
    return 0 if passed and bool(suite.get("cases")) else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    failed = False
    for path in sorted(args.files or [BASELINE], key=lambda item: item.as_posix()):
        result = validate(path)
        print(
            json.dumps(
                {
                    "file": path.as_posix(),
                    "outcome": result.outcome,
                    "findings": [
                        {"code": finding.code, "field": finding.field}
                        for finding in result.findings
                    ],
                    "scope": SCOPE,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
