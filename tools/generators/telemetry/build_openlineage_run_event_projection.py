"""Build deterministic, fixture-only KFM OpenLineage terminal RunEvent projections.

The generated document is a bounded telemetry projection. It never posts an
OpenLineage event, reads a network endpoint, admits a source, mutates lifecycle
state, or grants evidence, policy, review, release, deployment, publication, or
public-use authority.
"""

from __future__ import annotations

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import compute_spec_hash  # noqa: E402

PROFILE = "kfm.telemetry.openlineage-run-event-projection.v1"
PROFILE_STATUS = "PROPOSED_INACTIVE"
EXECUTION_MODE = "FIXTURE_ONLY_NO_NETWORK"
AUTHORITY = "NONE"
PROFILE_SCHEMA = (
    "https://schemas.kfm.local/contracts/v1/telemetry/"
    "openlineage_run_event_projection.schema.json"
)
RUN_FACET_SCHEMA = PROFILE_SCHEMA + "#/$defs/runReceiptFacet"
PROJECTION_FACET_SCHEMA = PROFILE_SCHEMA + "#/$defs/projectionFacet"
DATASET_FACET_SCHEMA = PROFILE_SCHEMA + "#/$defs/datasetFacet"
NON_EFFECTS = [
    "does_not_post_or_export_openlineage_events",
    "does_not_create_or_modify_canonical_evidence",
    "does_not_admit_sources_or_mutate_lifecycle_state",
    "does_not_grant_policy_review_or_release_authority",
    "does_not_promote_release_deploy_or_publish",
    "does_not_authorize_public_use",
]
DATASET_STAGES = (
    "RAW",
    "WORK",
    "QUARANTINE",
    "PROCESSED",
    "CATALOG",
    "TRIPLET",
    "PUBLISHED",
)
EVIDENCE_RELEASE_STATES = (
    "WORK",
    "QUARANTINE",
    "PROCESSED",
    "CATALOG",
    "PUBLISHED",
)
SENSITIVITY_LEVELS = (
    "public",
    "generalized",
    "internal",
    "restricted",
    "unknown",
    "quarantine",
)
PUBLIC_SENSITIVITY_LEVELS = frozenset({"public", "generalized"})
DENIED_SENSITIVITY_LEVELS = frozenset({"restricted", "unknown", "quarantine"})


def _normalize_utc(value: str) -> str:
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(candidate)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("event_time must include a timezone")
    normalized = parsed.astimezone(timezone.utc).replace(microsecond=0)
    return normalized.isoformat().replace("+00:00", "Z")


def _dataset_key(dataset: Mapping[str, object]) -> tuple[str, str]:
    return str(dataset.get("role", "")), str(dataset.get("ref", ""))


def _resolution_key(resolution: Mapping[str, object]) -> str:
    return str(resolution.get("evidence_ref", ""))


def _run_uuid(receipt: Mapping[str, object]) -> str:
    material = f"{receipt['run_id']}|{receipt['spec_hash']}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, material))


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    """Return the identity-bearing projection without self-identifiers."""

    return {
        key: value
        for key, value in document.items()
        if key not in {"projection_id", "spec_hash"}
    }


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    projection_id = "kfm:openlineage-projection:" + spec_hash.removeprefix(
        "sha256:"
    )
    return spec_hash, projection_id


def _dataset_ref_sets(
    document: Mapping[str, Any],
) -> tuple[set[str], set[str]]:
    inputs = {
        str(item["ref"])
        for item in document["datasets"]
        if item["role"] == "INPUT"
    }
    outputs = {
        str(item["ref"])
        for item in document["datasets"]
        if item["role"] == "OUTPUT"
    }
    return inputs, outputs


def _evidence_ref_sets(document: Mapping[str, Any]) -> tuple[set[str], set[str]]:
    used = {
        str(evidence_ref)
        for dataset in document["datasets"]
        for evidence_ref in dataset["evidence_refs"]
    }
    resolved = {
        str(item["evidence_ref"])
        for item in document["evidence_resolutions"]
    }
    return used, resolved


def expected_decision(document: Mapping[str, Any]) -> tuple[str, list[str]]:
    """Derive the finite projection disposition and stable reason codes."""

    receipt = document["source_run_receipt"]
    datasets = document["datasets"]
    resolutions = document["evidence_resolutions"]
    visibility = document["request"]["visibility"]

    if receipt["outcome"] == "PARTIAL":
        return "ABSTAIN", ["RUN_RECEIPT_PARTIAL"]

    reasons: list[str] = []
    declared_inputs, declared_outputs = _dataset_ref_sets(document)
    if declared_inputs != set(receipt["inputs"]):
        reasons.append("INPUT_DATASET_BINDING_MISMATCH")
    if declared_outputs != set(receipt["outputs"]):
        reasons.append("OUTPUT_DATASET_BINDING_MISMATCH")

    used_evidence, resolved_evidence = _evidence_ref_sets(document)
    if used_evidence != resolved_evidence:
        reasons.append("EVIDENCE_RESOLUTION_SET_MISMATCH")

    if any(item["lifecycle_stage"] == "QUARANTINE" for item in datasets):
        reasons.append("DATASET_QUARANTINED")
    if any(item["release_state"] == "QUARANTINE" for item in resolutions):
        reasons.append("EVIDENCE_QUARANTINED")
    if any(
        item["sensitivity_level"] in DENIED_SENSITIVITY_LEVELS
        for item in resolutions
    ):
        reasons.append("EVIDENCE_SENSITIVITY_DENIED")
    if any(not item["telemetry_allowed"] for item in resolutions):
        reasons.append("TELEMETRY_NOT_ALLOWED")

    if visibility == "PUBLIC":
        if any(item["lifecycle_stage"] != "PUBLISHED" for item in datasets):
            reasons.append("PUBLIC_DATASET_NOT_PUBLISHED")
        if any(not item["public_safe"] for item in datasets):
            reasons.append("PUBLIC_DATASET_NOT_SAFE")
        if any(item["release_state"] != "PUBLISHED" for item in resolutions):
            reasons.append("PUBLIC_EVIDENCE_NOT_PUBLISHED")
        if any(
            item["sensitivity_level"] not in PUBLIC_SENSITIVITY_LEVELS
            for item in resolutions
        ):
            reasons.append("PUBLIC_EVIDENCE_SENSITIVITY_DENIED")
        if any(not item["public_use_allowed"] for item in resolutions):
            reasons.append("PUBLIC_USE_NOT_ALLOWED")

    if reasons:
        return "DENY", sorted(set(reasons))

    pass_reasons = ["EVIDENCE_RESOLVED", "TELEMETRY_POLICY_SATISFIED"]
    if receipt["outcome"] == "SUCCESS":
        pass_reasons.append("RUN_SUCCESS")
    else:
        pass_reasons.append("RUN_FAILURE_RECORDED")
    if visibility == "PUBLIC":
        pass_reasons.append("PUBLIC_RELEASE_GATES_SATISFIED")
    return "PASS", sorted(pass_reasons)


def _resolution_index(document: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {
        str(item["evidence_ref"]): item
        for item in document["evidence_resolutions"]
    }


def expected_event(document: Mapping[str, Any]) -> dict[str, Any]:
    """Build the exact derived terminal RunEvent for a PASS projection."""

    request = document["request"]
    receipt = document["source_run_receipt"]
    producer = request["producer"]
    resolutions = _resolution_index(document)

    def dataset_payload(dataset: Mapping[str, Any]) -> dict[str, Any]:
        evidence_bundles = []
        for evidence_ref in dataset["evidence_refs"]:
            resolution = resolutions[evidence_ref]
            evidence_bundles.append(
                {
                    "evidenceRef": evidence_ref,
                    "bundleId": resolution["bundle_id"],
                    "bundleSpecHash": resolution["bundle_spec_hash"],
                    "releaseState": resolution["release_state"],
                    "sensitivityLevel": resolution["sensitivity_level"],
                }
            )
        return {
            "namespace": dataset["namespace"],
            "name": dataset["name"],
            "facets": {
                "kfm_dataset_state": {
                    "_producer": producer,
                    "_schemaURL": DATASET_FACET_SCHEMA,
                    "datasetRef": dataset["ref"],
                    "evidenceBundles": evidence_bundles,
                    "evidenceRefs": list(dataset["evidence_refs"]),
                    "lifecycleStage": dataset["lifecycle_stage"],
                    "publicSafe": dataset["public_safe"],
                }
            },
        }

    inputs = [
        dataset_payload(item)
        for item in document["datasets"]
        if item["role"] == "INPUT"
    ]
    outputs = [
        dataset_payload(item)
        for item in document["datasets"]
        if item["role"] == "OUTPUT"
    ]
    return {
        "eventType": "COMPLETE" if receipt["outcome"] == "SUCCESS" else "FAIL",
        "eventTime": request["event_time"],
        "run": {
            "runId": _run_uuid(receipt),
            "facets": {
                "kfm_run_receipt": {
                    "_producer": producer,
                    "_schemaURL": RUN_FACET_SCHEMA,
                    "codeRef": receipt["code_ref"],
                    "outcome": receipt["outcome"],
                    "runReceiptRef": request["run_receipt_ref"],
                    "sourceDescriptorRefs": list(
                        receipt["source_descriptor_refs"]
                    ),
                    "sourceRunId": receipt["run_id"],
                    "sourceRunSpecHash": receipt["spec_hash"],
                    "validationRefs": list(receipt["validation_refs"]),
                }
            },
        },
        "job": {
            "namespace": request["namespace"],
            "name": request["job_name"],
            "facets": {
                "kfm_projection": {
                    "_producer": producer,
                    "_schemaURL": PROJECTION_FACET_SCHEMA,
                    "authority": AUTHORITY,
                    "executionMode": EXECUTION_MODE,
                    "profile": PROFILE,
                    "visibility": request["visibility"],
                }
            },
        },
        "inputs": inputs,
        "outputs": outputs,
        "producer": producer,
        "schemaURL": request["schema_url"],
    }


def _reidentify(document: dict[str, Any]) -> dict[str, Any]:
    document["spec_hash"], document["projection_id"] = expected_identity(document)
    return document


def finalize(
    document: dict[str, Any],
    *,
    derive_decision: bool = True,
    derive_event: bool = True,
) -> dict[str, Any]:
    """Normalize order/time, derive decision/event, and bind deterministic identity."""

    document["request"]["event_time"] = _normalize_utc(
        str(document["request"]["event_time"])
    )
    receipt = document["source_run_receipt"]
    for field in (
        "inputs",
        "outputs",
        "source_descriptor_refs",
        "validation_refs",
    ):
        receipt[field] = sorted(receipt[field])
    for dataset in document["datasets"]:
        dataset["evidence_refs"] = sorted(dataset["evidence_refs"])
    document["datasets"] = sorted(document["datasets"], key=_dataset_key)
    document["evidence_resolutions"] = sorted(
        document["evidence_resolutions"], key=_resolution_key
    )

    if derive_decision:
        outcome, reasons = expected_decision(document)
        document["decision"] = {"outcome": outcome, "reason_codes": reasons}
    if derive_event:
        document["event"] = (
            expected_event(document)
            if document["decision"]["outcome"] == "PASS"
            else None
        )
    return _reidentify(document)


def _receipt(outcome: str) -> dict[str, Any]:
    return {
        "run_id": "kfm:run:synthetic-openlineage-v1",
        "stage": "PROCESSED",
        "inputs": ["kfm:dataset:synthetic-input-v1"],
        "outputs": ["kfm:dataset:synthetic-output-v1"],
        "code_ref": "repo:tools/generators/telemetry/openlineage-projection@v1",
        "spec_hash": compute_spec_hash(
            {"run": "synthetic-openlineage-v1", "outcome": outcome}
        ),
        "source_descriptor_refs": ["kfm:source:synthetic-lineage-fixture-v1"],
        "validation_refs": [
            "kfm:validation:fixture-policy-v1",
            "kfm:validation:fixture-schema-v1",
        ],
        "outcome": outcome,
    }


def _datasets(*, stage: str, public_safe: bool) -> list[dict[str, Any]]:
    if stage not in DATASET_STAGES:
        raise ValueError("unsupported lifecycle stage")
    return [
        {
            "ref": "kfm:dataset:synthetic-input-v1",
            "role": "INPUT",
            "namespace": "kfm.synthetic",
            "name": "input-v1",
            "lifecycle_stage": stage,
            "public_safe": public_safe,
            "evidence_refs": ["kfm:evidence:synthetic-input-v1"],
        },
        {
            "ref": "kfm:dataset:synthetic-output-v1",
            "role": "OUTPUT",
            "namespace": "kfm.synthetic",
            "name": "output-v1",
            "lifecycle_stage": stage,
            "public_safe": public_safe,
            "evidence_refs": ["kfm:evidence:synthetic-output-v1"],
        },
    ]


def _resolutions(
    *,
    release_state: str,
    sensitivity_level: str,
    telemetry_allowed: bool,
    public_use_allowed: bool,
) -> list[dict[str, Any]]:
    if release_state not in EVIDENCE_RELEASE_STATES:
        raise ValueError("unsupported evidence release state")
    if sensitivity_level not in SENSITIVITY_LEVELS:
        raise ValueError("unsupported sensitivity level")
    return [
        {
            "evidence_ref": "kfm:evidence:synthetic-input-v1",
            "bundle_id": "kfm:evidence-bundle:synthetic-input-v1",
            "bundle_spec_hash": compute_spec_hash(
                {"bundle": "synthetic-input-v1"}
            ),
            "release_state": release_state,
            "sensitivity_level": sensitivity_level,
            "telemetry_allowed": telemetry_allowed,
            "public_use_allowed": public_use_allowed,
        },
        {
            "evidence_ref": "kfm:evidence:synthetic-output-v1",
            "bundle_id": "kfm:evidence-bundle:synthetic-output-v1",
            "bundle_spec_hash": compute_spec_hash(
                {"bundle": "synthetic-output-v1"}
            ),
            "release_state": release_state,
            "sensitivity_level": sensitivity_level,
            "telemetry_allowed": telemetry_allowed,
            "public_use_allowed": public_use_allowed,
        },
    ]


def build_document(
    *,
    visibility: str = "INTERNAL",
    run_outcome: str = "SUCCESS",
    dataset_stage: str = "PROCESSED",
    public_safe: bool = False,
    evidence_release_state: str = "PROCESSED",
    sensitivity_level: str = "public",
    telemetry_allowed: bool = True,
    public_use_allowed: bool = False,
    event_time: str = "2026-08-07T02:00:00Z",
) -> dict[str, Any]:
    if visibility not in {"INTERNAL", "PUBLIC"}:
        raise ValueError("unsupported visibility")
    if run_outcome not in {"SUCCESS", "PARTIAL", "FAIL"}:
        raise ValueError("unsupported run outcome")
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": PROFILE,
        "profile_status": PROFILE_STATUS,
        "execution_mode": EXECUTION_MODE,
        "authority": AUTHORITY,
        "projection_id": "kfm:openlineage-projection:" + "0" * 64,
        "request": {
            "visibility": visibility,
            "event_time": event_time,
            "namespace": "kfm.fixture",
            "job_name": "kfm-fixture/openlineage-projection",
            "producer": "https://kansasfrontiermatrix.org/telemetry/projection/v1",
            "schema_url": (
                "https://openlineage.io/spec/2-0-2/"
                "OpenLineage.json#/$defs/RunEvent"
            ),
            "run_receipt_ref": "kfm:run-receipt:synthetic-openlineage-v1",
        },
        "source_run_receipt": _receipt(run_outcome),
        "datasets": _datasets(stage=dataset_stage, public_safe=public_safe),
        "evidence_resolutions": _resolutions(
            release_state=evidence_release_state,
            sensitivity_level=sensitivity_level,
            telemetry_allowed=telemetry_allowed,
            public_use_allowed=public_use_allowed,
        ),
        "decision": {"outcome": "PASS", "reason_codes": ["RUN_SUCCESS"]},
        "event": None,
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    document = build_document(
        visibility=str(case.get("visibility", "INTERNAL")),
        run_outcome=str(case.get("run_outcome", "SUCCESS")),
        dataset_stage=str(case.get("dataset_stage", "PROCESSED")),
        public_safe=bool(case.get("public_safe", False)),
        evidence_release_state=str(
            case.get("evidence_release_state", "PROCESSED")
        ),
        sensitivity_level=str(case.get("sensitivity_level", "public")),
        telemetry_allowed=bool(case.get("telemetry_allowed", True)),
        public_use_allowed=bool(case.get("public_use_allowed", False)),
        event_time=str(case.get("event_time", "2026-08-07T02:00:00Z")),
    )
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "UNRESOLVED_EVIDENCE_REF":
        document["evidence_resolutions"] = document["evidence_resolutions"][1:]
        return _reidentify(document)
    if mutation == "DATASET_RECEIPT_DRIFT":
        document["datasets"][0]["ref"] = "kfm:dataset:unexpected-input-v1"
        document["event"] = expected_event(document)
        return _reidentify(document)
    if mutation == "PROJECTION_ID_DRIFT":
        document["projection_id"] = "kfm:openlineage-projection:" + "f" * 64
        return document
    if mutation == "SPEC_HASH_DRIFT":
        document["spec_hash"] = "sha256:" + "f" * 64
        return document
    if mutation == "DECISION_REASON_DRIFT":
        document["decision"]["reason_codes"] = ["RUN_SUCCESS"]
        return _reidentify(document)
    if mutation == "EVENT_ON_DENY":
        document["event"] = expected_event(document)
        return _reidentify(document)
    if mutation == "EVENT_RUN_ID_DRIFT":
        if document["event"] is None:
            raise ValueError("event mutation requires a PASS decision")
        document["event"]["run"]["runId"] = str(uuid.UUID(int=0))
        return _reidentify(document)
    if mutation == "EVENT_TIME_DRIFT":
        if document["event"] is None:
            raise ValueError("event mutation requires a PASS decision")
        document["event"]["eventTime"] = "2026-08-07T03:00:00Z"
        return _reidentify(document)
    if mutation == "UNSORTED_DATASETS":
        document["datasets"] = list(reversed(document["datasets"]))
        return _reidentify(document)
    if mutation == "EXTRA_GEOMETRY":
        document["datasets"][0]["geometry"] = {
            "type": "Point",
            "coordinates": [-98.0, 38.5],
        }
        return _reidentify(document)
    if mutation == "NON_EFFECTS_DRIFT":
        document["non_effects"] = document["non_effects"][:-1]
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
        description=(
            "Render one deterministic fixture-only OpenLineage terminal "
            "RunEvent projection."
        )
    )
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=(
            REPO_ROOT
            / "fixtures/contracts/v1/telemetry/"
            "openlineage_run_event_projection/cases.json"
        ),
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    document = render_case(args.case, manifest)
    print(json.dumps(document, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
