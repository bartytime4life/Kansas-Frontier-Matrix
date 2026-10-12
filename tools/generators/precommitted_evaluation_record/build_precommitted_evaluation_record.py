"""Build deterministic fixture-only precommitted evaluation records."""

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
    "observation_write_allowed": False,
    "scoreboard_write_allowed": False,
    "lifecycle_write_allowed": False,
    "release_allowed": False,
    "publication_allowed": False,
    "public_use_allowed": False,
}
NON_EFFECTS = [
    "does_not_publish_a_commitment_or_reveal",
    "does_not_collect_or_authenticate_observations",
    "does_not_run_an_experiment_or_update_a_scoreboard",
    "does_not_release_deploy_publish_or_authorize_public_use",
]


def expected_score(document: Mapping[str, Any]) -> dict[str, Any]:
    outcomes = {item["prediction_id"]: item["occurred"] for item in document["observed_outcomes"]}
    per_prediction = []
    numerator = 0
    for prediction in document["sealed_payload"]["predictions"]:
        prediction_id = prediction["prediction_id"]
        observed = 10000 if outcomes[prediction_id] else 0
        squared_error = (prediction["confidence_basis_points"] - observed) ** 2
        numerator += squared_error
        per_prediction.append({"prediction_id": prediction_id, "squared_error_basis_points_2": squared_error})
    return {
        "rule": "BRIER_SCORE",
        "per_prediction": per_prediction,
        "mean_brier_fraction": {
            "numerator": numerator,
            "denominator": len(per_prediction) * 100000000,
        },
    }


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in document.items() if key not in {"evaluation_id", "spec_hash"}}


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    return spec_hash, "kfm:precommitted-evaluation:" + spec_hash.removeprefix("sha256:")


def finalize(document: dict[str, Any], *, derive_score: bool = True) -> dict[str, Any]:
    document["seal"]["commitment"] = compute_spec_hash(document["sealed_payload"])
    if derive_score:
        document["score"] = expected_score(document)
    document["spec_hash"], document["evaluation_id"] = expected_identity(document)
    return document


def build_document() -> dict[str, Any]:
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": "kfm.validation.precommitted-evaluation-record.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
        "authority": "NONE",
        "evaluation_id": "kfm:precommitted-evaluation:" + "0" * 64,
        "seal": {
            "commitment_method": "RFC8785-JCS+SHA-256",
            "commitment": "sha256:" + "0" * 64,
            "published_at": "2026-08-25T10:00:00Z",
            "revealed_at": "2026-08-25T18:30:00Z",
        },
        "sealed_payload": {
            "protocol_ref": "kfm://fixture/evaluation-protocol/cairnwake-adaptation-v1",
            "window": {
                "opens_at": "2026-08-25T12:00:00Z",
                "closes_at": "2026-08-25T18:00:00Z",
            },
            "scoring_rule": "BRIER_SCORE",
            "predictions": [
                {
                    "prediction_id": "P01",
                    "event_definition": "At least one synthetic qualifying return occurs in the window.",
                    "falsifier": "No synthetic qualifying return occurs before the window closes.",
                    "confidence_basis_points": 5500,
                },
                {
                    "prediction_id": "P02",
                    "event_definition": "At least one synthetic reviewed completion occurs in the window.",
                    "falsifier": "No synthetic reviewed completion occurs before the window closes.",
                    "confidence_basis_points": 2000,
                },
            ],
        },
        "interventions": [
            {
                "at": "2026-08-25T13:00:00Z",
                "kind": "DISCLOSURE_ONLY",
                "evidence_ref": "kfm://fixture/intervention/disclosure-v1",
            },
            {
                "at": "2026-08-25T14:00:00Z",
                "kind": "MECHANISM_CHANGE",
                "evidence_ref": "kfm://fixture/intervention/mechanism-v1",
            },
        ],
        "observed_outcomes": [
            {"prediction_id": "P01", "occurred": True, "evidence_ref": "kfm://fixture/outcome/P01"},
            {"prediction_id": "P02", "occurred": False, "evidence_ref": "kfm://fixture/outcome/P02"},
        ],
        "score": {
            "rule": "BRIER_SCORE",
            "per_prediction": [],
            "mean_brier_fraction": {"numerator": 0, "denominator": 100000000},
        },
        "permissions": dict(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def _refresh_identity(document: dict[str, Any]) -> dict[str, Any]:
    document["spec_hash"], document["evaluation_id"] = expected_identity(document)
    return document


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    document = build_document()
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "SEAL_DRIFT":
        document["seal"]["commitment"] = "sha256:" + "f" * 64
        return _refresh_identity(document)
    if mutation == "LATE_REGISTRATION":
        document["seal"]["published_at"] = "2026-08-25T12:00:01Z"
        return _refresh_identity(document)
    if mutation == "EARLY_REVEAL":
        document["seal"]["revealed_at"] = "2026-08-25T17:59:59Z"
        return _refresh_identity(document)
    if mutation == "OUTCOME_MISSING":
        document["observed_outcomes"] = document["observed_outcomes"][:1]
        return _refresh_identity(document)
    if mutation == "SCORE_DRIFT":
        document["score"]["mean_brier_fraction"]["numerator"] += 1
        return _refresh_identity(document)
    if mutation == "UNSORTED_INTERVENTIONS":
        document["interventions"] = list(reversed(document["interventions"]))
        return _refresh_identity(document)
    if mutation == "IDENTITY_DRIFT":
        document["spec_hash"] = "sha256:" + "f" * 64
        document["evaluation_id"] = "kfm:precommitted-evaluation:" + "f" * 64
        return document
    raise ValueError("unsupported mutation")


def render_case(case_id: str, manifest: Mapping[str, Any]) -> dict[str, Any]:
    for case in manifest.get("cases", []):
        if isinstance(case, dict) and case.get("case_id") == case_id:
            return build_case(case)
    raise KeyError(case_id)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Render one PrecommittedEvaluationRecord fixture.")
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "fixtures/contracts/v1/validation/precommitted_evaluation_record/cases.json",
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    print(json.dumps(render_case(args.case, manifest), sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
