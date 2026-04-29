#!/usr/bin/env python3
"""Validate ecology descriptors, bundles, and governed output objects."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]

DEFAULT_SOURCES = REPO_ROOT / "data/registry/ecology/sources.yaml"
DEFAULT_DATASETS = REPO_ROOT / "data/registry/ecology/datasets.yaml"
DEFAULT_POLICIES = REPO_ROOT / "data/registry/ecology/sensitivity_policies.yaml"

SCHEMA_MAP = {
    "TaxonRecord": REPO_ROOT / "schemas/contracts/v1/ecology/taxon_record.schema.json",
    "DerivedVegetationLayer": REPO_ROOT / "schemas/contracts/v1/ecology/derived_vegetation_layer.schema.json",
    "ObservationPlot": REPO_ROOT / "schemas/contracts/v1/ecology/observation_plot.schema.json",
    "SensitiveOccurrenceRecord": REPO_ROOT / "schemas/contracts/v1/ecology/sensitive_occurrence_record.schema.json",
    "HabitatAssignment": REPO_ROOT / "schemas/contracts/v1/ecology/habitat_assignment.schema.json",
    "EcologyObservationBundle": REPO_ROOT / "schemas/contracts/v1/ecology/ecology_observation_bundle.schema.json",
    "EvidenceBundle": REPO_ROOT / "schemas/contracts/v1/ecology/evidence_bundle.schema.json",
    "DecisionEnvelope": REPO_ROOT / "schemas/contracts/v1/ecology/decision_envelope.schema.json",
    "EcologicalClaim": REPO_ROOT / "schemas/contracts/v1/ecology/ecological_claim.schema.json",
    "ReleaseManifest": REPO_ROOT / "schemas/contracts/v1/ecology/release_manifest.schema.json",
    "FocusModeRequest": REPO_ROOT / "schemas/contracts/v1/ecology/focus_mode_request.schema.json",
    "FocusModeResponse": REPO_ROOT / "schemas/contracts/v1/ecology/focus_mode_response.schema.json",
    "EcologyEvidenceDrawerPayload": REPO_ROOT / "schemas/contracts/v1/ecology/ecology_evidence_drawer_payload.schema.json",
}

BUNDLE_OBJECT_TYPES = {
    "EcologyObservationBundle",
    "EvidenceBundle",
}

OUTPUT_OBJECT_TYPES = {
    "DecisionEnvelope",
    "EcologicalClaim",
    "ReleaseManifest",
}

UI_OBJECT_TYPES = {"EcologyEvidenceDrawerPayload"}

SPEC_HASH_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")
EVIDENCE_REF_RE = re.compile(r"^kfm://evidence/.+")
KFM_REF_RE = re.compile(r"^kfm://.+")


def _parse_scalar(value: str) -> Any:
    value = value.strip().strip('"').strip("'")

    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "None", "~"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        return [
            item.strip().strip('"').strip("'")
            for item in value[1:-1].split(",")
            if item.strip()
        ]

    return value


def _parse_min_yaml(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_list: str | None = None
    current_item: dict[str, Any] | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()

        if not line or line.lstrip().startswith("#"):
            continue

        if line.startswith("  - "):
            if current_list is None:
                continue

            item: dict[str, Any] = {}
            data.setdefault(current_list, []).append(item)
            current_item = item

            remainder = line[4:]
            if ":" in remainder:
                key, value = remainder.split(":", 1)
                current_item[key.strip()] = _parse_scalar(value.strip())
            continue

        if line.startswith("    ") and current_item is not None and ":" in line.strip():
            key, value = line.strip().split(":", 1)
            current_item[key.strip()] = _parse_scalar(value.strip())
            continue

        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value == "":
                current_list = key
                data[current_list] = []
                current_item = None
            else:
                data[key] = _parse_scalar(value)
                current_list = None
                current_item = None

    return data


def _load_yaml_like(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except Exception:
        try:
            data = json.loads(text)
        except Exception:
            data = _parse_min_yaml(text)

    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping at top-level in {path}")

    return data


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object at top-level in {path}")

    return data


def _registry_ids(registry: dict[str, Any], list_key: str, id_key: str) -> set[str]:
    return {
        item.get(id_key)
        for item in registry.get(list_key, [])
        if isinstance(item, dict) and isinstance(item.get(id_key), str)
    }


def _is_bundle_object(obj: dict[str, Any]) -> bool:
    return obj.get("object_type") in BUNDLE_OBJECT_TYPES or "bundle_id" in obj


def _is_output_object(obj: dict[str, Any]) -> bool:
    return obj.get("object_type") in OUTPUT_OBJECT_TYPES


def _object_identifier(obj: dict[str, Any]) -> str | None:
    for key in (
        "bundle_id",
        "decision_id",
        "claim_id",
        "release_id",
        "assignment_id",
        "layer_id",
        "plot_id",
        "occurrence_id",
        "taxon_id",
        "payload_id",
    ):
        value = obj.get(key)
        if isinstance(value, str):
            return value
    return None


def _required_governance_fields(obj: dict[str, Any]) -> list[str]:
    object_type = obj.get("object_type")

    if object_type == "EvidenceBundle":
        return [
            "object_type",
            "bundle_id",
            "source_refs",
            "dataset_refs",
            "evidence_refs",
            "object_refs",
            "resolved",
            "policy_label",
            "rights_status",
            "sensitivity",
            "spec_hash",
        ]

    if object_type == "DecisionEnvelope":
        return [
            "object_type",
            "decision_id",
            "bundle_ref",
            "policy_id",
            "surface",
            "decision",
            "allow",
            "evaluated_at",
            "spec_hash",
        ]

    if object_type == "EcologicalClaim":
        return [
            "object_type",
            "claim_id",
            "statement",
            "claim_status",
            "knowledge_character",
            "evidence_bundle_ref",
            "decision_ref",
            "policy_label",
            "spec_hash",
        ]

    if object_type == "ReleaseManifest":
        return [
            "object_type",
            "release_id",
            "surface",
            "release_state",
            "policy_pass",
            "published_at",
            "objects",
            "spec_hash",
        ]

    if _is_bundle_object(obj):
        return [
            "object_type",
            "bundle_id",
            "source_refs",
            "dataset_refs",
            "policy_id",
            "policy_label",
            "sensitivity",
            "rights_status",
            "spec_hash",
            "evidence_refs",
            "evidence_bundle_resolved",
        ]

    return [
        "object_type",
        "source_id",
        "source_role",
        "policy_id",
        "policy_label",
        "sensitivity",
        "rights_status",
        "spec_hash",
        "evidence_refs",
        "evidence_bundle_resolved",
    ]


def _validate_schema(obj: dict[str, Any]) -> list[str]:
    object_type = obj.get("object_type")
    if not object_type:
        return ["missing_required_field:object_type"]

    schema_path = SCHEMA_MAP.get(str(object_type))
    if schema_path is None:
        return [f"unknown_object_type:{object_type}"]

    if not schema_path.exists():
        return [f"missing_schema:{schema_path}"]

    try:
        from jsonschema import Draft202012Validator  # type: ignore
    except Exception:
        return ["missing_dependency:jsonschema"]

    schema = _load_json(schema_path)
    validator = Draft202012Validator(schema)

    errors: list[str] = []
    for err in sorted(validator.iter_errors(obj), key=lambda e: list(e.path)):
        location = ".".join(str(part) for part in err.path) or "<root>"
        errors.append(f"schema_error:{location}:{err.message}")

    return errors


def _validate_registry_refs(
    obj: dict[str, Any],
    sources_registry: dict[str, Any],
    datasets_registry: dict[str, Any],
    policies_registry: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    source_ids = _registry_ids(sources_registry, "sources", "source_id")
    dataset_ids = _registry_ids(datasets_registry, "datasets", "dataset_id")
    policy_ids = _registry_ids(policies_registry, "policies", "policy_id")

    source_refs = obj.get("source_refs", [])
    if source_refs:
        if not isinstance(source_refs, list):
            errors.append("source_refs_must_be_array")
        else:
            for ref in source_refs:
                if source_ids and ref not in source_ids:
                    errors.append(f"unknown_source_ref:{ref}")

    source_id = obj.get("source_id")
    if source_id and source_ids and source_id not in source_ids:
        errors.append(f"unknown_source_id:{source_id}")

    dataset_refs = obj.get("dataset_refs", [])
    if dataset_refs:
        if not isinstance(dataset_refs, list):
            errors.append("dataset_refs_must_be_array")
        else:
            for ref in dataset_refs:
                if dataset_ids and ref not in dataset_ids:
                    errors.append(f"unknown_dataset_ref:{ref}")

    policy_id = obj.get("policy_id")
    if policy_id and policy_ids and policy_id not in policy_ids:
        errors.append(f"unknown_policy_id:{policy_id}")

    return errors


def _validate_catalog_refs(obj: dict[str, Any]) -> list[str]:
    catalog_refs = obj.get("catalog_refs")
    errors: list[str] = []

    if catalog_refs is None:
        return errors

    if isinstance(catalog_refs, dict):
        for key, value in catalog_refs.items():
            if key not in {"stac", "dcat", "prov"}:
                errors.append(f"unknown_catalog_ref_kind:{key}")
            if not isinstance(value, str) or not KFM_REF_RE.match(value):
                errors.append(f"invalid_catalog_ref:{key}")
        return errors

    if isinstance(catalog_refs, list):
        for ref in catalog_refs:
            if not isinstance(ref, str) or not KFM_REF_RE.match(ref):
                errors.append(f"invalid_catalog_ref:{ref}")
        return errors

    return ["catalog_refs_must_be_object_or_array"]


def _validate_governance(obj: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in _required_governance_fields(obj):
        if field not in obj:
            errors.append(f"missing_required_field:{field}")

    spec_hash = obj.get("spec_hash")
    if not isinstance(spec_hash, str) or not SPEC_HASH_RE.match(spec_hash):
        errors.append("invalid_spec_hash")

    evidence_refs = obj.get("evidence_refs")
    if evidence_refs is not None:
        if not isinstance(evidence_refs, list) or not evidence_refs:
            errors.append("evidence_refs_required")
        else:
            for ref in evidence_refs:
                if not isinstance(ref, str) or not EVIDENCE_REF_RE.match(ref):
                    errors.append(f"invalid_evidence_ref:{ref}")

    if obj.get("object_type") not in OUTPUT_OBJECT_TYPES and obj.get("object_type") != "EvidenceBundle":
        if obj.get("evidence_bundle_resolved") is not True:
            errors.append("unresolved_evidence_bundle")

    if obj.get("resolved") is False:
        errors.append("unresolved_evidence_bundle")

    if obj.get("rights_status") == "unknown":
        errors.append("unknown_rights")

    if obj.get("policy_label") == "internal":
        errors.append("internal_policy_label_not_publishable")

    if obj.get("surface", "public") == "public" and obj.get("publication_state") in {
        "candidate",
        "held",
        "quarantined",
    }:
        errors.append(f"{obj.get('publication_state')}_not_publishable")

    if obj.get("source_role") == "DERIVED_MODEL_LAYER":
        if obj.get("claim_status") == "CONFIRMED":
            errors.append("derived_layer_as_confirmed_truth")
        if obj.get("catalog_closure") is not True and not obj.get("catalog_refs"):
            errors.append("derived_layer_missing_catalog_closure")

    if obj.get("source_role") == "SENSITIVE_OCCURRENCE":
        if obj.get("exact_geometry_present") is True:
            errors.append("sensitive_exact_geometry_not_publishable")

    if obj.get("public_visibility") == "generalized" and not obj.get("redaction_receipt_ref"):
        errors.append("missing_redaction_receipt")

    if obj.get("sensitivity") == "restricted" and obj.get("exact_geometry_present", False):
        errors.append("restricted_exact_geometry_not_allowed")

    if obj.get("sensitivity") == "review_required":
        errors.append("requires_steward_review")

    if obj.get("object_type") == "DecisionEnvelope":
        if obj.get("decision") == "allow" and obj.get("allow") is not True:
            errors.append("decision_allow_mismatch")
        if obj.get("decision") in {"deny", "hold", "generalize"} and obj.get("allow") is True:
            errors.append("decision_allow_mismatch")

    if obj.get("object_type") == "EcologicalClaim":
        if obj.get("claim_status") == "CONFIRMED" and obj.get("knowledge_character") in {
            "derived",
            "modeled",
        }:
            errors.append("derived_claim_marked_confirmed")

    if obj.get("object_type") == "ReleaseManifest":
        if obj.get("release_state") == "published" and obj.get("policy_pass") is not True:
            errors.append("published_release_without_policy_pass")

    errors.extend(_validate_catalog_refs(obj))

    return errors


def validate_object(
    obj: dict[str, Any],
    sources_registry: dict[str, Any],
    datasets_registry: dict[str, Any],
    policies_registry: dict[str, Any],
    *,
    validate_schema: bool = True,
) -> list[str]:
    errors: list[str] = []

    if validate_schema:
        errors.extend(_validate_schema(obj))

    if obj.get("object_type") not in UI_OBJECT_TYPES:
        errors.extend(_validate_governance(obj))
        errors.extend(_validate_registry_refs(obj, sources_registry, datasets_registry, policies_registry))

    return sorted(set(errors))


def validate_file(
    path: Path,
    sources_registry: dict[str, Any],
    datasets_registry: dict[str, Any],
    policies_registry: dict[str, Any],
    *,
    validate_schema: bool = True,
) -> dict[str, Any]:
    obj = _load_json(path)
    errors = validate_object(
        obj,
        sources_registry,
        datasets_registry,
        policies_registry,
        validate_schema=validate_schema,
    )

    return {
        "path": str(path),
        "object_id": _object_identifier(obj),
        "object_type": obj.get("object_type"),
        "decision": "pass" if not errors else "fail",
        "errors": errors,
    }


def _expand_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []

    for pattern in patterns:
        matched = sorted(Path().glob(pattern)) if any(ch in pattern for ch in "*?[]") else [Path(pattern)]
        paths.extend(matched)

    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ecology descriptor, bundle, or governed output fixtures")
    parser.add_argument("--bundle", action="append", default=[], help="Path or glob to descriptor/bundle JSON file")
    parser.add_argument("--sources", default=str(DEFAULT_SOURCES))
    parser.add_argument("--datasets", default=str(DEFAULT_DATASETS))
    parser.add_argument("--policies", default=str(DEFAULT_POLICIES))
    parser.add_argument("--skip-schema", action="store_true", help="Skip JSON Schema validation")
    parser.add_argument("--expect", choices=["pass", "fail"], help="Expected decision for all input files")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args()

    if not args.bundle:
        parser.error("at least one --bundle path or glob is required")

    bundle_paths = _expand_paths(args.bundle)
    if not bundle_paths:
        parser.error("no bundle files matched")

    sources_registry = _load_yaml_like(Path(args.sources))
    datasets_registry = _load_yaml_like(Path(args.datasets))
    policies_registry = _load_yaml_like(Path(args.policies))

    results = [
        validate_file(
            path,
            sources_registry,
            datasets_registry,
            policies_registry,
            validate_schema=not args.skip_schema,
        )
        for path in bundle_paths
    ]

    if args.expect:
        for result in results:
            if result["decision"] != args.expect:
                result["errors"] = [
                    *result["errors"],
                    f"unexpected_decision:expected_{args.expect}:got_{result['decision']}",
                ]
                result["decision"] = "fail"

    output = {
        "validator": "tools/validators/ecology/validate_ecology_bundle.py",
        "decision": "pass" if all(r["decision"] == "pass" for r in results) else "fail",
        "count": len(results),
        "results": results,
    }

    if args.json:
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        print(f"decision={output['decision']}")
        print(f"count={output['count']}")
        for result in results:
            print(f"{result['decision'].upper()} {result['path']}")
            print(f"  object_id={result['object_id']}")
            print(f"  object_type={result['object_type']}")
            for error in result["errors"]:
                print(f"  error={error}")

    return 0 if output["decision"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
