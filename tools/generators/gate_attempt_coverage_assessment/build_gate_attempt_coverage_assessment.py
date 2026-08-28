"""Build deterministic fixture-only gate attempt coverage assessments."""

from __future__ import annotations

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

PERMISSIONS = {
    "guarded_action_allowed": False,
    "gate_configuration_write_allowed": False,
    "feedback_write_allowed": False,
    "source_admission_allowed": False,
    "lifecycle_write_allowed": False,
    "release_allowed": False,
    "deployment_allowed": False,
    "publication_allowed": False,
    "public_use_allowed": False,
}
NON_EFFECTS = [
    "does_not_execute_or_authenticate_a_guarded_action",
    "does_not_store_submitted_or_rejected_payloads_or_sensitive_values",
    "does_not_activate_reconfigure_or_feed_a_gate",
    "does_not_bind_the_unresolved_run_receipt_family",
    "does_not_admit_sources_mutate_lifecycle_release_deploy_publish_or_authorize_public_use",
]


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in document.items() if key not in {"assessment_id", "spec_hash"}}


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    return spec_hash, "kfm:gate-attempt-coverage:" + spec_hash.removeprefix("sha256:")


def finalize(document: dict[str, Any]) -> dict[str, Any]:
    document["spec_hash"], document["assessment_id"] = expected_identity(document)
    return document


def build_document() -> dict[str, Any]:
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": "kfm.validation.gate-attempt-coverage-assessment.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
        "authority": "NONE",
        "assessment_id": "kfm:gate-attempt-coverage:" + "0" * 64,
        "gate_id": "kfm://fixture/gate/synthetic-mail-v1",
        "window": {
            "opens_at": "2026-08-28T12:00:00Z",
            "closes_at": "2026-08-28T13:00:00Z",
        },
        "counts": {
            "attempted": 5,
            "admitted": 2,
            "refused": 1,
            "error": 1,
            "unobserved": 1,
        },
        "attempt_classes": {
            "admitted": [
                {
                    "attempt_ref": "kfm://fixture/gate-attempt/A001",
                    "record_ref": "kfm://fixture/gate-attempt-record/admitted/A001",
                    "signature_domain": "kfm.gate.attempt.admitted.v1",
                },
                {
                    "attempt_ref": "kfm://fixture/gate-attempt/A002",
                    "record_ref": "kfm://fixture/gate-attempt-record/admitted/A002",
                    "signature_domain": "kfm.gate.attempt.admitted.v1",
                },
            ],
            "refused": [
                {
                    "attempt_ref": "kfm://fixture/gate-attempt/R001",
                    "record_ref": "kfm://fixture/gate-attempt-record/refused/R001",
                    "signature_domain": "kfm.gate.attempt.refused.v1",
                }
            ],
            "error": [
                {
                    "attempt_ref": "kfm://fixture/gate-attempt/E001",
                    "record_ref": "kfm://fixture/gate-attempt-record/error/E001",
                    "signature_domain": "kfm.gate.attempt.error.v1",
                }
            ],
            "unobserved": [
                {
                    "attempt_ref": "kfm://fixture/gate-attempt/U001",
                    "signature_domain": "kfm.gate.attempt.unobserved.v1",
                }
            ],
        },
        "denominator_policies": [
            {
                "metric_id": "admission-rate-among-attempts",
                "included_classes": ["ADMITTED", "ERROR", "REFUSED", "UNOBSERVED"],
                "excluded_classes": [],
                "denominator_count": 5,
            },
            {
                "metric_id": "terminal-outcome-distribution",
                "included_classes": ["ADMITTED", "ERROR", "REFUSED"],
                "excluded_classes": ["UNOBSERVED"],
                "denominator_count": 4,
            },
        ],
        "class_semantics": {
            "ADMITTED": {
                "guarded_action_occurrence": "CONFIRMED",
                "same_gate_feedback_allowed": True,
            },
            "REFUSED": {
                "guarded_action_occurrence": "DID_NOT_OCCUR",
                "same_gate_feedback_allowed": False,
            },
            "ERROR": {
                "guarded_action_occurrence": "NOT_CONFIRMED",
                "same_gate_feedback_allowed": False,
            },
            "UNOBSERVED": {
                "guarded_action_occurrence": "UNKNOWN",
                "same_gate_feedback_allowed": False,
            },
        },
        "terminal_coverage_state": "INCOMPLETE",
        "permissions": dict(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def _refresh_identity(document: dict[str, Any]) -> dict[str, Any]:
    document["spec_hash"], document["assessment_id"] = expected_identity(document)
    return document


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    document = build_document()
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "ATTEMPT_COUNT_DRIFT":
        document["counts"]["attempted"] += 1
        return _refresh_identity(document)
    if mutation == "CLASS_COUNT_DRIFT":
        document["counts"]["refused"] += 1
        document["counts"]["attempted"] += 1
        for policy in document["denominator_policies"]:
            if "REFUSED" in policy["included_classes"]:
                policy["denominator_count"] += 1
        return _refresh_identity(document)
    if mutation == "DUPLICATE_ATTEMPT_REF":
        document["attempt_classes"]["refused"][0]["attempt_ref"] = document["attempt_classes"]["admitted"][0]["attempt_ref"]
        return _refresh_identity(document)
    if mutation == "DUPLICATE_RECORD_REF":
        document["attempt_classes"]["error"][0]["record_ref"] = document["attempt_classes"]["refused"][0]["record_ref"]
        return _refresh_identity(document)
    if mutation == "DENOMINATOR_COUNT_DRIFT":
        document["denominator_policies"][0]["denominator_count"] += 1
        return _refresh_identity(document)
    if mutation == "DENOMINATOR_PARTITION_DRIFT":
        document["denominator_policies"][0]["included_classes"].remove("REFUSED")
        document["denominator_policies"][0]["denominator_count"] -= document["counts"]["refused"]
        return _refresh_identity(document)
    if mutation == "REFUSAL_FEEDBACK_ENABLED":
        document["class_semantics"]["REFUSED"]["same_gate_feedback_allowed"] = True
        return _refresh_identity(document)
    if mutation == "REFUSAL_OCCURRENCE_DRIFT":
        document["class_semantics"]["REFUSED"]["guarded_action_occurrence"] = "CONFIRMED"
        return _refresh_identity(document)
    if mutation == "SIGNATURE_DOMAIN_DRIFT":
        document["attempt_classes"]["refused"][0]["signature_domain"] = "kfm.gate.attempt.admitted.v1"
        return _refresh_identity(document)
    if mutation == "TERMINAL_COVERAGE_DRIFT":
        document["terminal_coverage_state"] = "COMPLETE"
        return _refresh_identity(document)
    if mutation == "WINDOW_ORDER_DRIFT":
        document["window"]["closes_at"] = "2026-08-28T11:59:59Z"
        return _refresh_identity(document)
    if mutation == "IDENTITY_DRIFT":
        document["spec_hash"] = "sha256:" + "f" * 64
        document["assessment_id"] = "kfm:gate-attempt-coverage:" + "f" * 64
        return document
    raise ValueError("unsupported mutation")


def render_case(case_id: str, manifest: Mapping[str, Any]) -> dict[str, Any]:
    for case in manifest.get("cases", []):
        if isinstance(case, dict) and case.get("case_id") == case_id:
            return build_case(case)
    raise KeyError(case_id)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Render one GateAttemptCoverageAssessment fixture.")
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "fixtures/contracts/v1/validation/gate_attempt_coverage_assessment/cases.json",
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    print(json.dumps(render_case(args.case, manifest), sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
