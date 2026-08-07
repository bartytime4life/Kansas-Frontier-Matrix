"""Composition engine for bounded promotion verification execution."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from .common import (
    Finding,
    ProcessResult,
    STATUS_RANK,
    canonical_hash,
    read_json,
    resolve,
    run_tool,
    run_validator,
    schema_findings,
    sha_bytes,
    sha_file,
    tool_digest,
)

REQUIRED_KINDS = {"EVIDENCE_BUNDLE", "STAC", "DCAT", "PROV", "ROLLBACK"}


def _packet_ids(packet: Mapping[str, Any], kind: str) -> set[str]:
    if kind == "EVIDENCE_BUNDLE":
        return {item for item in packet.get("evidence_refs", []) if isinstance(item, str)}
    if kind in {"STAC", "DCAT", "PROV"}:
        value = packet.get("catalog_refs", {})
        items = value.get(kind.lower(), []) if isinstance(value, dict) else []
        return {item for item in items if isinstance(item, str)}
    key = "card_ref" if kind == "ROLLBACK" else "notice_ref"
    value = packet.get("rollback" if kind == "ROLLBACK" else "correction", {})
    item = value.get(key) if isinstance(value, dict) else None
    return {item} if isinstance(item, str) else set()


def _check_references(root: Path, plan: Mapping[str, Any], packet: Mapping[str, Any]) -> tuple[list[dict[str, str]], list[Finding]]:
    results: list[dict[str, str]] = []
    findings: list[Finding] = []
    seen: set[str] = set()
    manifest = packet.get("release_manifest", {})
    artifacts = set(manifest.get("artifact_digests", [])) if isinstance(manifest, dict) else set()
    for index, declaration in enumerate(plan.get("references", [])):
        pointer = f"/references/{index}"
        kind = declaration["kind"]
        seen.add(kind)
        resolved, problem = resolve(root, declaration["path"])
        if problem:
            findings.append(Finding(problem.code, pointer, problem.status))
            results.append({"kind": kind, "status": problem.status})
            continue
        assert resolved is not None
        if sha_file(resolved) != declaration["sha256"]:
            findings.append(Finding("REFERENCE_DIGEST_MISMATCH", pointer, "DENY"))
            results.append({"kind": kind, "status": "DENY"})
            continue
        value, parse_findings = read_json(resolved)
        if parse_findings or not isinstance(value, dict):
            findings.append(Finding("REFERENCE_JSON_INVALID", pointer, "DENY"))
            results.append({"kind": kind, "status": "DENY"})
            continue
        checks = (
            (declaration["ref_id"] in _packet_ids(packet, kind), "REFERENCE_ID_MISMATCH"),
            (value.get("ref_id") == declaration["ref_id"], "REFERENCE_ID_MISMATCH"),
            (value.get("kind") == kind, "REFERENCE_KIND_MISMATCH"),
            (value.get("subject_spec_hash") == packet.get("spec_hash"), "REFERENCE_SUBJECT_MISMATCH"),
            (value.get("artifact_digest") in artifacts, "REFERENCE_ARTIFACT_MISMATCH"),
        )
        for passed, code in checks:
            if not passed:
                findings.append(Finding(code, pointer, "DENY"))
        results.append({"kind": kind, "status": "DENY" if any(item.path == pointer for item in findings) else "PASS"})
    required = set(REQUIRED_KINDS)
    correction = packet.get("correction", {})
    if isinstance(correction, dict) and correction.get("supersedes_prior") is True:
        required.add("CORRECTION")
    for kind in sorted(required - seen):
        status = "ABSTAIN" if kind == "EVIDENCE_BUNDLE" else "DENY"
        findings.append(Finding("REFERENCE_KIND_MISSING", "/references", status))
        results.append({"kind": kind, "status": status})
    return sorted(results, key=lambda item: item["kind"]), sorted(set(findings))


def _stage(result: ProcessResult) -> dict[str, Any]:
    payload = json.dumps(result.payload or {}, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {"status": result.status, "result_sha256": sha_bytes(payload)}


def _tool(result: ProcessResult) -> dict[str, Any]:
    return {
        "status": result.status,
        "exit_code": result.exit_code,
        "stdout_sha256": result.stdout_sha256,
        "stderr_sha256": result.stderr_sha256,
    }


def _overall(findings: Iterable[Finding]) -> str:
    return max((item.status for item in findings), key=STATUS_RANK.get, default="PASS")


def result_payload(
    plan: Mapping[str, Any],
    findings: Sequence[Finding],
    *,
    promotion: ProcessResult | None = None,
    cosign_plan: ProcessResult | None = None,
    tools: Mapping[str, Any] | None = None,
    references: Sequence[Mapping[str, str]] | None = None,
) -> dict[str, Any]:
    status = _overall(findings)
    return {
        "object_type": "PromotionVerificationExecutionResult",
        "schema_version": "1.0.0",
        "execution_id": plan.get("execution_id"),
        "evaluated_at": plan.get("evaluated_at"),
        "status": status,
        "readiness": "APPROVE_READY" if status == "PASS" else "BLOCKED",
        "promotion_gate": _stage(promotion) if promotion else {"status": "NOT_EVALUATED"},
        "cosign_plan_validation": _stage(cosign_plan) if cosign_plan else {"status": "NOT_EVALUATED"},
        "tools": dict(tools or {}),
        "references": list(references or []),
        "findings": [
            {"code": item.code, "path": item.path, "status": item.status}
            for item in sorted(set(findings))
        ],
        "authority": {
            "lifecycle_write": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "deployment_authorized": False,
            "publication_authorized": False,
        },
    }


def execute(
    plan: Mapping[str, Any],
    *,
    repo_root: Path,
    schema_path: Path,
    cosign_bin: Path,
    conftest_bin: Path,
    promotion_validator: Path,
    cosign_plan_validator: Path,
) -> dict[str, Any]:
    findings = schema_findings(plan, schema_path)
    if plan.get("spec_hash") != canonical_hash(plan):
        findings.append(Finding("EXECUTION_SPEC_HASH_MISMATCH", "/spec_hash", "DENY"))
    if findings:
        return result_payload(plan, findings)

    files: dict[str, Path] = {}
    for key in ("promotion_packet", "cosign_plan", "subject", "bundle"):
        resolved, problem = resolve(repo_root, plan[key]["path"])
        if problem:
            findings.append(Finding(problem.code, f"/{key}", problem.status))
            continue
        assert resolved is not None
        files[key] = resolved
        if sha_file(resolved) != plan[key]["sha256"]:
            findings.append(Finding("INPUT_DIGEST_MISMATCH", f"/{key}/sha256", "DENY"))
    if findings:
        return result_payload(plan, findings)

    packet, packet_findings = read_json(files["promotion_packet"])
    cosign, cosign_findings = read_json(files["cosign_plan"])
    if packet_findings or not isinstance(packet, dict):
        findings.append(Finding("PROMOTION_PACKET_INVALID", "/promotion_packet", "ERROR"))
    if cosign_findings or not isinstance(cosign, dict):
        findings.append(Finding("COSIGN_PLAN_INVALID", "/cosign_plan", "ERROR"))
    if findings:
        return result_payload(plan, findings)
    assert isinstance(packet, dict) and isinstance(cosign, dict)

    promotion = run_validator(repo_root, promotion_validator, files["promotion_packet"], deny_code="PROMOTION_GATE_BLOCKED", error_code="PROMOTION_GATE_RESULT_INVALID")
    plan_check = run_validator(repo_root, cosign_plan_validator, files["cosign_plan"], deny_code="COSIGN_PLAN_BLOCKED", error_code="COSIGN_PLAN_RESULT_INVALID")
    for process in (promotion, plan_check):
        if process.finding:
            findings.append(process.finding)

    references, reference_findings = _check_references(repo_root, plan, packet)
    findings.extend(reference_findings)
    tools: dict[str, Any] = {}

    cosign_digest, problem = tool_digest(cosign_bin, "/cosign_plan/tool/binary_digest")
    if problem:
        findings.append(problem)
        tools["cosign"] = {"status": problem.status}
    elif cosign_digest != cosign.get("tool", {}).get("binary_digest"):
        findings.append(Finding("COSIGN_BINARY_DIGEST_MISMATCH", "/cosign_plan/tool/binary_digest", "DENY"))
        tools["cosign"] = {"status": "DENY"}
    else:
        trust = cosign["trust"]
        crypto = run_tool(
            repo_root,
            cosign_bin,
            [
                "verify-blob-attestation",
                "--bundle", str(files["bundle"]),
                "--type", cosign["predicate"]["predicate_type"],
                "--certificate-identity", trust["certificate_identity"],
                "--certificate-oidc-issuer", trust["certificate_oidc_issuer"],
                "--offline", str(files["subject"]),
            ],
            deny_code="COSIGN_VERIFICATION_DENIED",
            error_path="/crypto",
        )
        tools["cosign"] = _tool(crypto)
        if crypto.finding:
            findings.append(crypto.finding)

    policy_dir, problem = resolve(repo_root, plan["policy"]["directory"], directory=True)
    if problem:
        findings.append(Finding(problem.code, "/policy/directory", problem.status))
        tools["conftest"] = {"status": problem.status}
    else:
        conftest_digest, tool_problem = tool_digest(conftest_bin, "/policy/conftest_binary_sha256")
        if tool_problem:
            findings.append(tool_problem)
            tools["conftest"] = {"status": tool_problem.status}
        elif conftest_digest != plan["policy"]["conftest_binary_sha256"]:
            findings.append(Finding("CONFTEST_BINARY_DIGEST_MISMATCH", "/policy/conftest_binary_sha256", "DENY"))
            tools["conftest"] = {"status": "DENY"}
        else:
            policy_ok = True
            for index, declaration in enumerate(plan["policy"]["files"]):
                policy_file, file_problem = resolve(repo_root, declaration["path"])
                pointer = f"/policy/files/{index}"
                if file_problem or policy_file is None:
                    item = file_problem or Finding("REFERENCE_NOT_FOUND", "/", "ABSTAIN")
                    findings.append(Finding(item.code, pointer, item.status))
                    policy_ok = False
                elif policy_file.parent != policy_dir:
                    findings.append(Finding("POLICY_FILE_OUTSIDE_DIRECTORY", pointer, "DENY"))
                    policy_ok = False
                elif sha_file(policy_file) != declaration["sha256"]:
                    findings.append(Finding("POLICY_FILE_DIGEST_MISMATCH", pointer, "DENY"))
                    policy_ok = False
            if policy_ok:
                policy_result = run_tool(
                    repo_root,
                    conftest_bin,
                    ["test", str(files["promotion_packet"]), "--policy", str(policy_dir), "--output", "json", "--no-color"],
                    deny_code="POLICY_EVALUATION_DENIED",
                    error_path="/policy",
                )
                tools["conftest"] = _tool(policy_result)
                if policy_result.finding:
                    findings.append(policy_result.finding)

    return result_payload(plan, findings, promotion=promotion, cosign_plan=plan_check, tools=tools, references=references)
