"""Build deterministic, fixture-only remote-sensing lineage activities.

The generated companion binds bounded scene metrics and a PROV-shaped activity
to an already governed OpenLineage terminal projection. It performs no source
access, event export, repository mutation, signing, release, or publication.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import compute_spec_hash  # noqa: E402


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_OPENLINEAGE_BUILDER = _load_module(
    "kfm_remote_sensing_source_openlineage_builder",
    REPO_ROOT
    / "tools/generators/telemetry/build_openlineage_run_event_projection.py",
)

PROFILE = "kfm.telemetry.remote-sensing-lineage-activity.v1"
NON_EFFECTS = [
    "does_not_contact_remote_sensing_sources",
    "does_not_post_or_export_lineage_events",
    "does_not_create_or_modify_canonical_evidence",
    "does_not_admit_sources_or_mutate_lifecycle_state",
    "does_not_grant_policy_review_or_release_authority",
    "does_not_promote_release_deploy_or_publish",
    "does_not_authorize_public_use",
]


def _normalize_utc(value: str) -> str:
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(candidate)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    normalized = parsed.astimezone(timezone.utc).replace(microsecond=0)
    return normalized.isoformat().replace("+00:00", "Z")


def _elapsed_ms(started_at: str, ended_at: str) -> int:
    def parse(value: str) -> datetime:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))

    return int((parse(ended_at) - parse(started_at)).total_seconds() * 1000)


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    """Return identity-bearing content without self-derived identifiers."""

    material = copy.deepcopy(dict(document))
    material.pop("activity_id", None)
    material.pop("spec_hash", None)
    facet = material.get("remote_sensing_facet")
    if isinstance(facet, dict):
        facet.pop("activityId", None)
    activity = material.get("prov_activity")
    if isinstance(activity, dict):
        activity.pop("id", None)
    return material


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    activity_id = "kfm:remote-sensing-activity:" + spec_hash.removeprefix(
        "sha256:"
    )
    return spec_hash, activity_id


def expected_decision(document: Mapping[str, Any]) -> tuple[str, list[str]]:
    source_outcome = document["source_openlineage_projection"]["decision"][
        "outcome"
    ]
    if source_outcome == "ABSTAIN":
        return "ABSTAIN", ["SOURCE_PROJECTION_ABSTAIN"]
    if source_outcome == "DENY":
        return "DENY", ["SOURCE_PROJECTION_DENIED"]
    if source_outcome == "ERROR":
        return "ERROR", ["SOURCE_PROJECTION_ERROR"]

    metrics = document["metrics"]
    reasons: list[str] = []
    if metrics["scene_count"] != (
        metrics["processed_scene_count"] + metrics["failed_scene_count"]
    ):
        reasons.append("SCENE_COUNT_MISMATCH")
    if _elapsed_ms(metrics["started_at"], metrics["ended_at"]) != metrics[
        "runtime_ms"
    ]:
        reasons.append("RUNTIME_MISMATCH")

    receipt_outcome = document["source_openlineage_projection"][
        "source_run_receipt"
    ]["outcome"]
    failure_recorded = metrics["failed_scene_count"] > 0
    if failure_recorded != (receipt_outcome == "FAIL"):
        reasons.append("RUN_OUTCOME_MISMATCH")

    source_descriptors = set(
        document["source_openlineage_projection"]["source_run_receipt"][
            "source_descriptor_refs"
        ]
    )
    if not source_descriptors.issubset(set(document["source_links"])):
        reasons.append("SOURCE_LINK_CLOSURE_MISMATCH")
    if reasons:
        return "DENY", sorted(set(reasons))

    pass_reasons = [
        "METRICS_COHERENT",
        "SOURCE_LINKS_BOUND",
        "SOURCE_PROJECTION_VALID",
    ]
    pass_reasons.append(
        "REMOTE_SENSING_FAILURE_RECORDED"
        if failure_recorded
        else "REMOTE_SENSING_SUCCESS_RECORDED"
    )
    return "PASS", sorted(pass_reasons)


def expected_facet(document: Mapping[str, Any]) -> dict[str, Any]:
    metrics = document["metrics"]
    return {
        "activityId": document["activity_id"],
        "sceneCount": metrics["scene_count"],
        "processedSceneCount": metrics["processed_scene_count"],
        "failedSceneCount": metrics["failed_scene_count"],
        "retryCount": metrics["retry_count"],
        "runtimeMs": metrics["runtime_ms"],
        "sourceLinks": list(document["source_links"]),
    }


def expected_prov_activity(document: Mapping[str, Any]) -> dict[str, Any]:
    receipt = document["source_openlineage_projection"]["source_run_receipt"]
    metrics = document["metrics"]
    return {
        "id": document["activity_id"],
        "type": "kfm:RemoteSensingProcessingActivity",
        "startedAt": metrics["started_at"],
        "endedAt": metrics["ended_at"],
        "used": sorted(receipt["inputs"]),
        "generated": sorted(receipt["outputs"]),
        "wasAssociatedWith": (
            "kfm:agent:fixture-only-remote-sensing-lineage-v1"
        ),
        "sourceLinks": list(document["source_links"]),
    }


def _reidentify(document: dict[str, Any]) -> dict[str, Any]:
    document["spec_hash"], document["activity_id"] = expected_identity(document)
    document["remote_sensing_facet"]["activityId"] = document["activity_id"]
    document["prov_activity"]["id"] = document["activity_id"]
    return document


def finalize(document: dict[str, Any]) -> dict[str, Any]:
    metrics = document["metrics"]
    metrics["started_at"] = _normalize_utc(str(metrics["started_at"]))
    metrics["ended_at"] = _normalize_utc(str(metrics["ended_at"]))
    document["source_links"] = sorted(document["source_links"])
    outcome, reasons = expected_decision(document)
    document["decision"] = {"outcome": outcome, "reason_codes": reasons}
    document["remote_sensing_facet"] = expected_facet(document)
    document["prov_activity"] = expected_prov_activity(document)
    return _reidentify(document)


def build_document(
    *,
    scene_count: int = 8,
    processed_scene_count: int = 8,
    failed_scene_count: int = 0,
    retry_count: int = 1,
    runtime_ms: int = 1_200_000,
    started_at: str = "2026-08-10T18:00:00Z",
    ended_at: str = "2026-08-10T18:20:00Z",
    run_outcome: str = "SUCCESS",
    telemetry_allowed: bool = True,
) -> dict[str, Any]:
    source_projection = _OPENLINEAGE_BUILDER.build_document(
        run_outcome=run_outcome,
        sensitivity_level="internal",
        telemetry_allowed=telemetry_allowed,
        event_time=ended_at,
    )
    receipt = source_projection["source_run_receipt"]
    source_links = sorted(
        set(receipt["source_descriptor_refs"])
        | set(receipt["inputs"])
        | set(receipt["outputs"])
    )
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": PROFILE,
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
        "authority": "NONE",
        "activity_id": "kfm:remote-sensing-activity:" + "0" * 64,
        "source_openlineage_projection": source_projection,
        "metrics": {
            "scene_count": scene_count,
            "processed_scene_count": processed_scene_count,
            "failed_scene_count": failed_scene_count,
            "retry_count": retry_count,
            "runtime_ms": runtime_ms,
            "started_at": started_at,
            "ended_at": ended_at,
        },
        "source_links": source_links,
        "remote_sensing_facet": {},
        "prov_activity": {},
        "decision": {"outcome": "PASS", "reason_codes": ["METRICS_COHERENT"]},
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    document = build_document(
        scene_count=int(case.get("scene_count", 8)),
        processed_scene_count=int(case.get("processed_scene_count", 8)),
        failed_scene_count=int(case.get("failed_scene_count", 0)),
        retry_count=int(case.get("retry_count", 1)),
        runtime_ms=int(case.get("runtime_ms", 1_200_000)),
        started_at=str(case.get("started_at", "2026-08-10T18:00:00Z")),
        ended_at=str(case.get("ended_at", "2026-08-10T18:20:00Z")),
        run_outcome=str(case.get("run_outcome", "SUCCESS")),
        telemetry_allowed=bool(case.get("telemetry_allowed", True)),
    )
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "COUNT_MISMATCH":
        document["metrics"]["processed_scene_count"] -= 1
        return finalize(document)
    if mutation == "RUNTIME_MISMATCH":
        document["metrics"]["runtime_ms"] += 1
        return finalize(document)
    if mutation == "SOURCE_LINK_MISSING":
        source_descriptor = document["source_openlineage_projection"][
            "source_run_receipt"
        ]["source_descriptor_refs"][0]
        document["source_links"] = [
            link for link in document["source_links"] if link != source_descriptor
        ]
        return finalize(document)
    if mutation == "FACET_DRIFT":
        document["remote_sensing_facet"]["retryCount"] += 1
        return _reidentify(document)
    if mutation == "PROV_DRIFT":
        document["prov_activity"]["generated"] = document["prov_activity"][
            "used"
        ]
        return _reidentify(document)
    if mutation == "SPEC_HASH_DRIFT":
        document["spec_hash"] = "sha256:" + "f" * 64
        return document
    if mutation == "EXTRA_COORDINATES":
        document["metrics"]["coordinates"] = [-98.0, 38.5]
        return _reidentify(document)
    raise ValueError("unsupported fixture mutation")


def render_case(case_id: str, manifest: Mapping[str, Any]) -> dict[str, Any]:
    for case in manifest.get("cases", []):
        if isinstance(case, dict) and case.get("case_id") == case_id:
            return build_case(case)
    raise KeyError(case_id)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Render one fixture-only remote-sensing lineage activity."
    )
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=(
            REPO_ROOT
            / "fixtures/contracts/v1/telemetry/"
            "remote_sensing_lineage_activity/cases.json"
        ),
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    print(
        json.dumps(
            render_case(args.case, manifest),
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
