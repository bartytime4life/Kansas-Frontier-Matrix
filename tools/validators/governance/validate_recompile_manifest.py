"""Validate fixture-only KFM RecompileManifest records by deterministic replay."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, canonicalize_json, compute_spec_hash, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/recompile_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/recompile_manifest"
EXPECTED_MANIFEST_PATH = FIXTURE_ROOT / "expected_manifest.json"
EXPECTED_CANDIDATE_PATH = FIXTURE_ROOT / "expected_candidate.json"
QUERY_PATH = FIXTURE_ROOT / "query_ready.json"
PROPOSAL_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/ai_change_proposal/valid/valid_ready.json"
)
SUBJECT_PATH = (
    REPO_ROOT / "fixtures/contracts/v1/governance/ai_change_proposal/subjects/base.json"
)
INVALID_CASES_PATH = FIXTURE_ROOT / "invalid_manifest_cases.json"
SCOPE = "governance.recompile_manifest"
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    manifest_id: str | None = None


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_COMPILER = _load_module(
    "kfm_recompile_manifest_compiler",
    REPO_ROOT
    / "tools/generators/recompile_manifest/compile_recompile_manifest.py",
)


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def validate_documents(
    manifest: object,
    candidate: object,
    query_run: object,
    proposal: object,
    subject: object,
) -> ValidationResult:
    findings: set[Finding] = set()
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(manifest),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(manifest, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))
    if not isinstance(candidate, dict):
        findings.add(Finding("CANDIDATE_ROOT_NOT_OBJECT", "$candidate"))
        return ValidationResult("DENY", tuple(sorted(findings)))

    replay = _COMPILER.compile_documents(
        query_run,
        proposal,
        subject,
        compiled_at=manifest["compiled_at"],
        target_stage=manifest["target_stage"],
    )
    if replay.outcome != "COMPILED_CANDIDATE":
        findings.add(Finding("REPLAY_COMPILATION_FAILED", "$"))
        return ValidationResult("DENY", tuple(sorted(findings)))

    if replay.candidate != candidate:
        findings.add(Finding("CANDIDATE_REPLAY_MISMATCH", "$candidate"))

    manifest_projection = {
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_id", "manifest_spec_hash"}
    }
    current_manifest_hash = compute_spec_hash(manifest_projection)
    current_manifest_id = (
        "kfm:recompile-manifest:"
        + current_manifest_hash.removeprefix("sha256:")
    )
    if manifest["manifest_spec_hash"] != current_manifest_hash:
        findings.add(
            Finding("MANIFEST_SPEC_HASH_MISMATCH", "$.manifest_spec_hash")
        )
    if manifest["manifest_id"] != current_manifest_id:
        findings.add(Finding("MANIFEST_ID_MISMATCH", "$.manifest_id"))

    if replay.manifest != manifest:
        expected = replay.manifest if isinstance(replay.manifest, Mapping) else {}
        if manifest.get("output") != expected.get("output"):
            findings.add(Finding("OUTPUT_BINDING_MISMATCH", "$.output"))
        if manifest.get("rollback") != expected.get("rollback"):
            findings.add(Finding("ROLLBACK_BINDING_MISMATCH", "$.rollback"))
        if manifest.get("compiler") != expected.get("compiler"):
            findings.add(Finding("COMPILER_BINDING_MISMATCH", "$.compiler"))
        if manifest.get("inputs") != expected.get("inputs"):
            findings.add(Finding("INPUT_BINDING_MISMATCH", "$.inputs"))
        if manifest.get("verification") != expected.get("verification"):
            findings.add(Finding("VERIFICATION_BINDING_MISMATCH", "$.verification"))
        if manifest.get("permissions") != expected.get("permissions"):
            findings.add(Finding("AUTHORITY_BOUNDARY_MISMATCH", "$.permissions"))
        if manifest.get("non_effects") != expected.get("non_effects"):
            findings.add(Finding("NON_EFFECTS_MISMATCH", "$.non_effects"))

    candidate_bytes = canonicalize_json(candidate)
    candidate_hash = compute_spec_hash(candidate)
    if manifest["output"]["content_spec_hash"] != candidate_hash:
        findings.add(Finding("OUTPUT_CONTENT_HASH_MISMATCH", "$.output.content_spec_hash"))
    if manifest["output"]["byte_length"] != len(candidate_bytes):
        findings.add(Finding("OUTPUT_BYTE_LENGTH_MISMATCH", "$.output.byte_length"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        manifest_id=manifest.get("manifest_id"),
    )


def validate_files(
    manifest_path: Path,
    candidate_path: Path,
    query_path: Path,
    proposal_path: Path,
    subject_path: Path,
) -> ValidationResult:
    loaded: list[object] = []
    for code, path in (
        ("MANIFEST_JSON_INVALID", manifest_path),
        ("CANDIDATE_JSON_INVALID", candidate_path),
        ("QUERY_JSON_INVALID", query_path),
        ("PROPOSAL_JSON_INVALID", proposal_path),
        ("SUBJECT_JSON_INVALID", subject_path),
    ):
        try:
            loaded.append(load_json_file(path))
        except JsonInputError:
            return ValidationResult("ERROR", (Finding(code, "$"),))
    return validate_documents(*loaded)


def _serialize_result(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY_NO_WRITE",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "manifest_id": result.manifest_id,
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        manifest = load_json_file(EXPECTED_MANIFEST_PATH)
        candidate = load_json_file(EXPECTED_CANDIDATE_PATH)
        query_run = load_json_file(QUERY_PATH)
        proposal = load_json_file(PROPOSAL_PATH)
        subject = load_json_file(SUBJECT_PATH)
        invalid_suite = load_json_file(INVALID_CASES_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    cases: list[dict[str, object]] = []
    valid_result = validate_documents(manifest, candidate, query_run, proposal, subject)
    valid_ok = valid_result.outcome == "PASS" and not valid_result.findings
    cases.append(
        {
            "actual_findings": [],
            "actual_outcome": valid_result.outcome,
            "case_id": "valid-replay",
            "expected_findings": [],
            "expected_outcome": "PASS",
            "ok": valid_ok,
        }
    )
    ok = valid_ok

    entries = invalid_suite.get("cases", []) if isinstance(invalid_suite, dict) else []
    for case in entries:
        if not isinstance(case, dict) or not isinstance(case.get("manifest"), dict):
            ok = False
            continue
        result = validate_documents(
            case["manifest"],
            candidate,
            query_run,
            proposal,
            subject,
        )
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        cases.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes")
                if isinstance(expected, dict)
                else None,
                "expected_outcome": expected.get("outcome")
                if isinstance(expected, dict)
                else None,
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only RecompileManifest records by replay."
    )
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--query-run", type=Path)
    parser.add_argument("--proposal", type=Path)
    parser.add_argument("--subject", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    explicit = (
        args.manifest,
        args.candidate,
        args.query_run,
        args.proposal,
        args.subject,
    )
    if args.fixtures:
        if any(explicit):
            parser.error("--fixtures cannot be combined with explicit files")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not all(explicit):
        parser.error(
            "--manifest, --candidate, --query-run, --proposal, and --subject are required"
        )
    result = validate_files(*explicit)
    print(_serialize_result(result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
