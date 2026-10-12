"""Build deterministic, fixture-only Watcher/Planner/Executor envelopes in memory."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import compute_spec_hash  # noqa: E402

GATE_ORDER = ("SCHEMA", "POLICY", "QA", "REPRODUCIBILITY")
NON_EFFECTS = [
    "does_not_execute_network_or_repository_operations",
    "does_not_authenticate_evidence_policy_review_or_attestation",
    "does_not_grant_branch_or_pull_request_permissions",
    "does_not_merge_or_write_protected_branches",
    "does_not_promote_release_deploy_or_publish",
    "does_not_authorize_public_use",
]
PERMISSIONS = {
    "repository_write_allowed": False,
    "lifecycle_write_allowed": False,
    "canonical_write_allowed": False,
    "merge_allowed": False,
    "promotion_allowed": False,
    "release_allowed": False,
    "deployment_allowed": False,
    "publication_allowed": False,
    "public_use_allowed": False,
}
CAPABILITIES = {
    "WATCHER": {
        "repository_read": True,
        "consume_facts": False,
        "consume_plan": False,
        "emit_facts": True,
        "emit_alerts": True,
        "emit_plan": False,
        "emit_diff_candidate": False,
        "feature_branch_write": False,
        "draft_pr_write": False,
        "protected_branch_write": False,
        "merge": False,
        "release": False,
        "deploy": False,
        "publish": False,
    },
    "PLANNER": {
        "repository_read": True,
        "consume_facts": True,
        "consume_plan": False,
        "emit_facts": False,
        "emit_alerts": False,
        "emit_plan": True,
        "emit_diff_candidate": True,
        "feature_branch_write": False,
        "draft_pr_write": False,
        "protected_branch_write": False,
        "merge": False,
        "release": False,
        "deploy": False,
        "publish": False,
    },
    "EXECUTOR": {
        "repository_read": True,
        "consume_facts": False,
        "consume_plan": True,
        "emit_facts": False,
        "emit_alerts": False,
        "emit_plan": False,
        "emit_diff_candidate": False,
        "feature_branch_write": True,
        "draft_pr_write": True,
        "protected_branch_write": False,
        "merge": False,
        "release": False,
        "deploy": False,
        "publish": False,
    },
}


def _binding(kind: str, ref: str, payload: Mapping[str, object]) -> dict[str, str]:
    return {"kind": kind, "ref": ref, "spec_hash": compute_spec_hash(payload)}


ROLE_BINDINGS = {
    "WATCHER": (
        [
            _binding(
                "SOURCE_SNAPSHOT",
                "kfm:source-snapshot:synthetic-hydrology-v1",
                {"source": "synthetic-hydrology-v1"},
            )
        ],
        [
            _binding(
                "ALERTS",
                "kfm:agent-output:watcher-alerts-v1",
                {"output": "watcher-alerts-v1"},
            ),
            _binding(
                "FACTS",
                "kfm:agent-output:watcher-facts-v1",
                {"output": "watcher-facts-v1"},
            ),
        ],
    ),
    "PLANNER": (
        [
            _binding(
                "POLICY_BASELINE",
                "kfm:policy-baseline:agent-fixture-v1",
                {"policy": "agent-fixture-v1"},
            ),
            _binding(
                "WATCHER_FACTS",
                "kfm:agent-output:watcher-facts-v1",
                {"output": "watcher-facts-v1"},
            ),
        ],
        [
            _binding(
                "DIFF_CANDIDATE",
                "kfm:agent-output:planner-diff-v1",
                {"output": "planner-diff-v1"},
            ),
            _binding(
                "PLAN",
                "kfm:agent-output:planner-plan-v1",
                {"output": "planner-plan-v1"},
            ),
            _binding(
                "VALIDATION_EVIDENCE",
                "kfm:agent-output:planner-validation-v1",
                {"output": "planner-validation-v1"},
            ),
        ],
    ),
    "EXECUTOR": (
        [
            _binding(
                "ATTESTATION",
                "kfm:attestation:synthetic-agent-plan-v1",
                {"attestation": "synthetic-agent-plan-v1"},
            ),
            _binding(
                "PLAN",
                "kfm:agent-output:planner-plan-v1",
                {"output": "planner-plan-v1"},
            ),
            _binding(
                "VALIDATION_EVIDENCE",
                "kfm:agent-output:planner-validation-v1",
                {"output": "planner-validation-v1"},
            ),
        ],
        [
            _binding(
                "DRAFT_PR_METADATA",
                "kfm:agent-output:draft-pr-metadata-v1",
                {"output": "draft-pr-metadata-v1"},
            ),
            _binding(
                "EXECUTION_RECEIPT",
                "kfm:agent-output:execution-receipt-v1",
                {"output": "execution-receipt-v1"},
            ),
        ],
    ),
}


def _binding_key(binding: Mapping[str, object]) -> tuple[str, str]:
    return str(binding.get("kind", "")), str(binding.get("ref", ""))


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in document.items()
        if key not in {"operation_id", "spec_hash"}
    }


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    return spec_hash, "kfm:agent-operation:" + spec_hash.removeprefix("sha256:")


def expected_idempotency_key(document: Mapping[str, Any]) -> str:
    actor = document["actor"]
    operation = document["operation"]
    return compute_spec_hash(
        {
            "role": actor["role"],
            "subject_ref": operation["subject_ref"],
            "window": operation["window"],
            "commit_seed": operation["commit_seed"],
            "input_bundle_hash": operation["input_bundle_hash"],
        }
    )


def expected_disposition(document: Mapping[str, Any]) -> tuple[str, list[str]]:
    role = str(document["actor"]["role"])
    kill_state = str(document["kill_switch"]["state"])
    if kill_state == "ENGAGED" and role in {"PLANNER", "EXECUTOR"}:
        return "HOLD", ["KILL_SWITCH_ENGAGED"]

    for gate_outcome, disposition, prefix in (
        ("ERROR", "ERROR", "GATE_ERROR_"),
        ("DENY", "DENY", "GATE_DENIED_"),
        ("HOLD", "HOLD", "GATE_HOLD_"),
    ):
        reasons = [
            prefix + str(gate["gate"])
            for gate in document["gates"]
            if gate["outcome"] == gate_outcome
        ]
        if reasons:
            return disposition, reasons

    reasons = ["GATES_PASS", "ROLE_BOUNDARY_SATISFIED"]
    if kill_state == "ENGAGED" and role == "WATCHER":
        reasons.append("WATCHER_READ_ONLY_DURING_KILL_SWITCH")
    return "READY", reasons


def _gates(overrides: Mapping[str, str] | None = None) -> list[dict[str, str]]:
    overrides = overrides or {}
    return [
        {
            "gate": name,
            "outcome": overrides.get(name, "PASS"),
            "evidence_ref": f"kfm:validation:{name.lower()}-fixture-v1",
        }
        for name in GATE_ORDER
    ]


def finalize(document: dict[str, Any], *, derive_disposition: bool = True) -> dict[str, Any]:
    document["inputs"] = sorted(document["inputs"], key=_binding_key)
    document["outputs"] = sorted(document["outputs"], key=_binding_key)
    document["operation"]["input_bundle_hash"] = compute_spec_hash(document["inputs"])
    document["operation"]["idempotency_key"] = expected_idempotency_key(document)
    if derive_disposition:
        outcome, reasons = expected_disposition(document)
        document["disposition"] = {"outcome": outcome, "reason_codes": reasons}
    document["spec_hash"], document["operation_id"] = expected_identity(document)
    return document


def build_document(
    role: str,
    *,
    kill_switch_state: str = "DISENGAGED",
    gate_overrides: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    if role not in ROLE_BINDINGS:
        raise ValueError("unsupported role")
    inputs, outputs = copy.deepcopy(ROLE_BINDINGS[role])
    kind = {
        "WATCHER": "OBSERVE",
        "PLANNER": "PLAN",
        "EXECUTOR": "OPEN_OR_UPDATE_DRAFT_PR",
    }[role]
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": "kfm.governance.agent-operation-envelope.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
        "authority": "NONE",
        "operation_id": "kfm:agent-operation:" + "0" * 64,
        "actor": {
            "role": role,
            "component_id": f"kfm:agent:{role.lower()}-fixture",
            "component_version": "1.0.0",
        },
        "operation": {
            "kind": kind,
            "subject_ref": "kfm:subject:synthetic-agent-operation-v1",
            "window": "2026-08-06T00:00:00Z/2026-08-06T23:59:59Z",
            "commit_seed": "new-ideas-4-wpe-v1",
            "input_bundle_hash": "sha256:" + "0" * 64,
            "idempotency_key": "sha256:" + "0" * 64,
        },
        "determinism": {
            "canonicalization": "RFC8785-JCS",
            "hash_algorithm": "SHA-256",
            "clock_mode": "PINNED",
            "network_access": "FORBIDDEN",
            "replay_safe": True,
        },
        "kill_switch": {
            "checked": True,
            "state": kill_switch_state,
            "source_ref": "kfm:config:agent-kill-switch-fixture-v1",
        },
        "inputs": inputs,
        "outputs": outputs,
        "gates": _gates(gate_overrides),
        "capability_ceiling": copy.deepcopy(CAPABILITIES[role]),
        "credential_ceiling": (
            "FEATURE_BRANCH_AND_DRAFT_PR_ONLY" if role == "EXECUTOR" else "READ_ONLY"
        ),
        "target": (
            {
                "base_branch": "main",
                "head_branch": "agent/wpe-fixture-20260806",
                "base_is_protected": True,
                "head_is_protected": False,
                "draft": True,
            }
            if role == "EXECUTOR"
            else None
        ),
        "evidence_refs": [
            "kfm:evidence:new-ideas-4-wpe",
            "kfm:evidence:repo-directory-rules-v2",
        ],
        "disposition": {"outcome": "READY", "reason_codes": ["GATES_PASS"]},
        "permissions": copy.deepcopy(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    role = str(case["role"])
    document = build_document(
        role,
        kill_switch_state=str(case.get("kill_switch", "DISENGAGED")),
        gate_overrides=case.get("gate_overrides") or {},
    )
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "WATCHER_PR_WRITE_OVERREACH":
        document["capability_ceiling"]["draft_pr_write"] = True
        return document
    if mutation == "EXECUTOR_PROTECTED_HEAD":
        document["target"]["head_is_protected"] = True
        return document
    if mutation == "PLANNER_PR_OUTPUT":
        document["outputs"].append(
            _binding(
                "DRAFT_PR_METADATA",
                "kfm:agent-output:forbidden-draft-pr-v1",
                {"output": "forbidden-draft-pr-v1"},
            )
        )
        return finalize(document)
    if mutation == "EXECUTOR_MISSING_ATTESTATION":
        document["inputs"] = [
            item for item in document["inputs"] if item["kind"] != "ATTESTATION"
        ]
        return finalize(document)
    if mutation == "IDEMPOTENCY_DRIFT":
        document["operation"]["idempotency_key"] = "sha256:" + "f" * 64
        document["spec_hash"], document["operation_id"] = expected_identity(document)
        return document
    if mutation == "DISPOSITION_DRIFT":
        document["disposition"] = {
            "outcome": "HOLD",
            "reason_codes": ["KILL_SWITCH_ENGAGED"],
        }
        document["spec_hash"], document["operation_id"] = expected_identity(document)
        return document
    if mutation == "UNSORTED_EVIDENCE":
        document["evidence_refs"] = list(reversed(document["evidence_refs"]))
        document["spec_hash"], document["operation_id"] = expected_identity(document)
        return document
    raise ValueError("unsupported fixture mutation")


def render_case(case_id: str, manifest: Mapping[str, Any]) -> dict[str, Any]:
    for case in manifest.get("cases", []):
        if isinstance(case, dict) and case.get("case_id") == case_id:
            return build_case(case)
    raise KeyError(case_id)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Render one deterministic AgentOperationEnvelope fixture to stdout."
    )
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=(
            REPO_ROOT
            / "fixtures/contracts/v1/governance/agent_operation_envelope/cases.json"
        ),
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    document = render_case(args.case, manifest)
    print(json.dumps(document, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
