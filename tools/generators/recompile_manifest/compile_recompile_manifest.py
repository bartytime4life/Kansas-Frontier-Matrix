"""Compile one fixture-only JSON work candidate and RecompileManifest in memory.

The compiler reads explicit local QueryRunRecord, AIChangeProposal, and JSON
subject inputs. It emits canonical candidate bytes and a manifest to memory/stdout
only. It has no file-write, network, repository-mutation, lifecycle, release, or
publication capability.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    canonicalize_json,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/recompile_manifest.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/recompile_manifest"
CASES_PATH = FIXTURE_ROOT / "cases.json"
MAX_OUTPUT_BYTES = 1_000_000
SCOPE = "governance.recompile_manifest"
COMPILER_PROJECTION = {
    "compiler_id": "kfm.tools.recompile-fixture.v1",
    "compiler_version": "1.0.0",
    "canonicalization": "RFC8785-JCS",
    "hash_algorithm": "SHA-256",
    "network_access": "FORBIDDEN",
    "write_mode": "NO_WRITE",
}
PERMISSIONS = {
    "repository_write_allowed": False,
    "lifecycle_write_allowed": False,
    "canonical_write_allowed": False,
    "promotion_allowed": False,
    "release_allowed": False,
    "deployment_allowed": False,
    "publication_allowed": False,
    "public_use_allowed": False,
}
NON_EFFECTS = [
    "does_not_apply_to_repository",
    "does_not_create_evidence_policy_review_or_release_authority",
    "does_not_promote_release_deploy_or_publish",
    "does_not_write_canonical_or_lifecycle_state",
    "does_not_write_files_or_use_network",
    "output_is_fixture_only_work_candidate",
]
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class CompilationResult:
    outcome: str
    findings: tuple[Finding, ...]
    candidate: Mapping[str, Any] | None = None
    candidate_bytes: bytes | None = None
    manifest: Mapping[str, Any] | None = None


def _load_validator_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_QUERY_VALIDATOR = _load_validator_module(
    "kfm_query_run_record_validator",
    REPO_ROOT / "tools/validators/governance/validate_query_run_record.py",
)
_PROPOSAL_VALIDATOR = _load_validator_module(
    "kfm_ai_change_proposal_validator",
    REPO_ROOT / "tools/validators/governance/validate_ai_change_proposal.py",
)


def _parse_aware_datetime(value: object) -> bool:
    if not isinstance(value, str):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() is not None


def _decode_pointer(pointer: str) -> tuple[str, ...]:
    return tuple(
        token.replace("~1", "/").replace("~0", "~")
        for token in pointer[1:].split("/")
    )


def _state_matches(
    *,
    present: bool,
    value: object,
    expected: Mapping[str, Any],
) -> bool:
    return present == expected["present"] and (
        not present or value == expected.get("value")
    )


def _apply_verified_patch(
    subject: Mapping[str, Any],
    operations: list[Mapping[str, Any]],
) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    output: object = copy.deepcopy(subject)
    findings: set[Finding] = set()
    for index, operation in enumerate(operations):
        tokens = _decode_pointer(operation["path"])
        parent = output
        for token in tokens[:-1]:
            if not isinstance(parent, dict) or token not in parent:
                findings.add(
                    Finding(
                        "PATCH_PARENT_UNAVAILABLE",
                        f"$.patch.operations[{index}].path",
                    )
                )
                return None, tuple(sorted(findings))
            parent = parent[token]
        if not isinstance(parent, dict):
            findings.add(
                Finding(
                    "PATCH_CONTAINER_NOT_OBJECT",
                    f"$.patch.operations[{index}].path",
                )
            )
            return None, tuple(sorted(findings))
        key = tokens[-1]
        present = key in parent
        current = parent.get(key)
        if not _state_matches(
            present=present,
            value=current,
            expected=operation["before"],
        ):
            findings.add(
                Finding(
                    "PATCH_PREIMAGE_MISMATCH",
                    f"$.patch.operations[{index}].before",
                )
            )
            return None, tuple(sorted(findings))
        after = operation["after"]
        if after["present"]:
            parent[key] = copy.deepcopy(after["value"])
        else:
            del parent[key]
    if not isinstance(output, dict):
        findings.add(Finding("OUTPUT_ROOT_NOT_OBJECT", "$candidate"))
        return None, tuple(sorted(findings))
    return output, ()


def _manifest_projection(manifest: Mapping[str, Any]) -> dict[str, object]:
    return {
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_id", "manifest_spec_hash"}
    }


def _build_manifest(
    *,
    query_run: Mapping[str, Any],
    proposal: Mapping[str, Any],
    candidate_bytes: bytes,
    compiled_at: str,
) -> dict[str, Any]:
    output_hash = compute_spec_hash(json.loads(candidate_bytes.decode("utf-8")))
    compiler = dict(COMPILER_PROJECTION)
    compiler["compiler_spec_hash"] = compute_spec_hash(COMPILER_PROJECTION)
    manifest: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": "kfm.governance.recompile-manifest.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_WRITE",
        "authority": "NONE",
        "compiled_at": compiled_at,
        "artifact_kind": "JSON_DERIVED_CANDIDATE",
        "target_stage": "WORK",
        "inputs": {
            "query_run_id": query_run["query_run_id"],
            "query_run_hash": query_run["hashes"]["run_hash"],
            "query_run_spec_hash": query_run["hashes"]["spec_hash"],
            "proposal_id": proposal["proposal_id"],
            "patch_spec_hash": proposal["patch"]["patch_spec_hash"],
            "subject_ref": proposal["subject"]["subject_ref"],
            "input_spec_hash": proposal["subject"]["input_spec_hash"],
        },
        "compiler": compiler,
        "output": {
            "candidate_ref": "kfm:recompile-candidate:"
            + output_hash.removeprefix("sha256:"),
            "content_spec_hash": output_hash,
            "byte_length": len(candidate_bytes),
            "media_type": "application/json",
            "canonical_bytes": True,
        },
        "rollback": {
            "target_ref": proposal["subject"]["subject_ref"],
            "content_spec_hash": proposal["subject"]["input_spec_hash"],
            "exact_restore": True,
        },
        "verification": {
            "query_record": "PASS",
            "query_outcome": "ANSWER",
            "evidence_resolution": "COMPLETE",
            "proposal_record": "PASS",
            "proposal_readiness": "READY_FOR_STEWARD_APPLY",
            "policy_projection": "ALLOW",
            "human_attestation": "APPROVED",
            "proposal_bound_to_query": True,
            "preimage_bound": True,
            "output_hash_bound": True,
            "destination_allowed": True,
            "no_write": True,
        },
        "permissions": dict(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
    }
    manifest_hash = compute_spec_hash(_manifest_projection(manifest))
    manifest["manifest_spec_hash"] = manifest_hash
    manifest["manifest_id"] = "kfm:recompile-manifest:" + manifest_hash.removeprefix(
        "sha256:"
    )
    return manifest


def compile_documents(
    query_run: object,
    proposal: object,
    subject: object,
    *,
    compiled_at: object,
    target_stage: object = "WORK",
) -> CompilationResult:
    if not _parse_aware_datetime(compiled_at):
        return CompilationResult(
            "ERROR",
            (Finding("COMPILED_AT_INVALID", "$.compiled_at"),),
        )
    if target_stage != "WORK":
        return CompilationResult(
            "DENY",
            (Finding("TARGET_STAGE_NOT_ALLOWED", "$.target_stage"),),
        )

    query_result = _QUERY_VALIDATOR.validate_document(query_run)
    if query_result.outcome != "PASS" or not isinstance(query_run, dict):
        return CompilationResult(
            "DENY",
            (Finding("QUERY_RECORD_INVALID", "$.query_run"),),
        )
    if (
        query_run["outcome"] != "ANSWER"
        or query_run["evidence_resolution"]["summary"] != "COMPLETE"
    ):
        return CompilationResult(
            "HOLD",
            (Finding("QUERY_NOT_READY", "$.query_run.outcome"),),
        )

    proposal_result = _PROPOSAL_VALIDATOR.validate_document(proposal, subject)
    if proposal_result.outcome != "PASS" or not isinstance(proposal, dict):
        return CompilationResult(
            "DENY",
            (Finding("PROPOSAL_RECORD_INVALID", "$.proposal"),),
        )
    if not isinstance(subject, dict):
        return CompilationResult(
            "DENY",
            (Finding("SUBJECT_ROOT_NOT_OBJECT", "$.subject"),),
        )

    if proposal["proposal_id"] not in query_run["candidate_proposal_refs"]:
        return CompilationResult(
            "DENY",
            (
                Finding(
                    "PROPOSAL_NOT_BOUND_TO_QUERY",
                    "$.query_run.candidate_proposal_refs",
                ),
            ),
        )

    policy_outcome = proposal["policy_projection"]["outcome"]
    review_state = proposal["human_attestation"]["state"]
    readiness = proposal["readiness"]["disposition"]
    if policy_outcome == "DENY" or review_state == "REJECTED" or readiness == "DENY":
        return CompilationResult(
            "DENY",
            (Finding("PROPOSAL_DENIED", "$.proposal.readiness"),),
        )
    if (
        policy_outcome != "ALLOW"
        or review_state != "APPROVED"
        or readiness != "READY_FOR_STEWARD_APPLY"
    ):
        return CompilationResult(
            "HOLD",
            (Finding("PROPOSAL_NOT_READY", "$.proposal.readiness"),),
        )
    candidate, patch_findings = _apply_verified_patch(
        subject,
        proposal["patch"]["operations"],
    )
    if candidate is None:
        return CompilationResult("DENY", patch_findings)
    try:
        candidate_bytes = canonicalize_json(candidate)
        output_hash = compute_spec_hash(candidate)
    except CanonicalizationFailure:
        return CompilationResult(
            "DENY",
            (Finding("CANONICALIZATION_ERROR", "$candidate"),),
        )
    if len(candidate_bytes) > MAX_OUTPUT_BYTES:
        return CompilationResult(
            "DENY",
            (Finding("OUTPUT_TOO_LARGE", "$candidate"),),
        )
    if output_hash != proposal["subject"]["expected_output_spec_hash"]:
        return CompilationResult(
            "DENY",
            (Finding("OUTPUT_HASH_MISMATCH", "$candidate"),),
        )

    manifest = _build_manifest(
        query_run=query_run,
        proposal=proposal,
        candidate_bytes=candidate_bytes,
        compiled_at=compiled_at,
    )
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(manifest),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if schema_errors:
        return CompilationResult(
            "ERROR",
            (Finding("MANIFEST_SCHEMA_INVALID", "$manifest"),),
        )
    return CompilationResult(
        "COMPILED_CANDIDATE",
        (),
        candidate=candidate,
        candidate_bytes=candidate_bytes,
        manifest=manifest,
    )


def compile_files(
    query_path: Path,
    proposal_path: Path,
    subject_path: Path,
    *,
    compiled_at: object,
    target_stage: object = "WORK",
) -> CompilationResult:
    try:
        query_run = load_json_file(query_path)
    except JsonInputError:
        return CompilationResult(
            "ERROR",
            (Finding("QUERY_JSON_INVALID", "$.query_run"),),
        )
    try:
        proposal = load_json_file(proposal_path)
    except JsonInputError:
        return CompilationResult(
            "ERROR",
            (Finding("PROPOSAL_JSON_INVALID", "$.proposal"),),
        )
    try:
        subject = load_json_file(subject_path)
    except JsonInputError:
        return CompilationResult(
            "ERROR",
            (Finding("SUBJECT_JSON_INVALID", "$.subject"),),
        )
    return compile_documents(
        query_run,
        proposal,
        subject,
        compiled_at=compiled_at,
        target_stage=target_stage,
    )


def _serialize_result(result: CompilationResult) -> str:
    payload: dict[str, object] = {
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY_NO_WRITE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "non_effects": NON_EFFECTS,
        "outcome": result.outcome,
        "scope": SCOPE,
    }
    if result.outcome == "COMPILED_CANDIDATE":
        payload["candidate"] = result.candidate
        payload["manifest"] = result.manifest
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _resolve_repo_path(value: object) -> Path | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    candidate = REPO_ROOT / value
    try:
        resolved = candidate.resolve(strict=False)
        resolved.relative_to(REPO_ROOT.resolve())
    except (OSError, ValueError):
        return None
    return candidate


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(CASES_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    cases = suite.get("cases", []) if isinstance(suite, dict) else []
    results: list[dict[str, object]] = []
    ok = True
    for case in cases:
        if not isinstance(case, dict):
            ok = False
            continue
        paths = {
            name: _resolve_repo_path(case.get(name))
            for name in ("query_run", "proposal", "subject")
        }
        if paths["query_run"] is None or paths["proposal"] is None or paths["subject"] is None:
            result = CompilationResult(
                "ERROR",
                (Finding("FIXTURE_PATH_INVALID", "$fixture"),),
            )
        else:
            result = compile_files(
                paths["query_run"],
                paths["proposal"],
                paths["subject"],
                compiled_at=case.get("compiled_at"),
                target_stage=case.get("target_stage", "WORK"),
            )
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("outcome")
            and actual_codes == expected.get("finding_codes")
        )
        if case_ok and result.outcome == "COMPILED_CANDIDATE":
            expected_candidate_path = _resolve_repo_path(expected.get("candidate"))
            expected_manifest_path = _resolve_repo_path(expected.get("manifest"))
            if expected_candidate_path is None or expected_manifest_path is None:
                case_ok = False
            else:
                try:
                    expected_candidate = load_json_file(expected_candidate_path)
                    expected_manifest = load_json_file(expected_manifest_path)
                except JsonInputError:
                    case_ok = False
                else:
                    case_ok = (
                        result.candidate == expected_candidate
                        and result.manifest == expected_manifest
                    )
        ok = ok and case_ok
        results.append(
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
    return ok, {"cases": results, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compile a fixture-only JSON candidate and RecompileManifest in memory."
    )
    parser.add_argument("--query-run", type=Path)
    parser.add_argument("--proposal", type=Path)
    parser.add_argument("--subject", type=Path)
    parser.add_argument("--compiled-at")
    parser.add_argument("--target-stage", default="WORK")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if any((args.query_run, args.proposal, args.subject, args.compiled_at)):
            parser.error("--fixtures cannot be combined with explicit compilation inputs")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not all((args.query_run, args.proposal, args.subject, args.compiled_at)):
        parser.error(
            "--query-run, --proposal, --subject, and --compiled-at are required"
        )
    result = compile_files(
        args.query_run,
        args.proposal,
        args.subject,
        compiled_at=args.compiled_at,
        target_stage=args.target_stage,
    )
    print(_serialize_result(result))
    return 0 if result.outcome == "COMPILED_CANDIDATE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
