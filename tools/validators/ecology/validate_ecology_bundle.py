#!/usr/bin/env python3
"""Validate ecology bundle descriptors against schemas, registry references, and policy prerequisites."""

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
}

SPEC_HASH_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")
EVIDENCE_REF_RE = re.compile(r"^kfm://evidence/.+")


def _parse_min_yaml(text: str) -> dict[str, Any]:
    """Small YAML fallback for simple registry files.

    Prefer PyYAML when installed. This fallback intentionally supports only
    shallow mappings and list-of-mapping registries used by KFM fixtures.
    """
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


def _load_yaml_like(path: Path) -> dict[str, Any]:
    """Load YAML using PyYAML if available, then JSON, then minimal YAML fallback."""
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


def _validate_schema(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    object_type = bundle.get("object_type")
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

    for err in sorted(validator.iter_errors(bundle), key=lambda e: list(e.path)):
        location = ".".join(str(part) for part in err.path) or "<root>"
        errors.append(f"schema_error:{location}:{err.message}")

    return errors


def validate_bundle(
    bundle: dict[str, Any],
    sources_registry: dict[str, Any],
    datasets_registry: dict[str, Any],
    policies_registry: dict[str, Any],
    *,
    validate_schema: bool = True,
) -> list[str]:
    errors: list[str] = []

    required = [
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

    for field in required:
        if field not in bundle:
            errors.append(f"missing_required_field:{field}")

    if validate_schema:
        errors.extend(_validate_schema(bundle))

    source_ids = _registry_ids(sources_registry, "sources", "source_id")
    dataset_ids = _registry_ids(datasets_registry, "datasets", "dataset_id")
    policy_ids = _registry_ids(policies_registry, "policies", "policy_id")

    for ref in bundle.get("source_refs", []):
        if ref not in source_ids:
            errors.append(f"unknown_source_ref:{ref}")

    for ref in bundle.get("dataset_refs", []):
        if ref not in dataset_ids:
            errors.append(f"unknown_dataset_ref:{ref}")

    policy_id = bundle.get("policy_id")
    if policy_id and policy_ids and policy_id not in policy_ids:
        errors.append(f"unknown_policy_id:{policy_id}")

    spec_hash = bundle.get("spec_hash")
    if not isinstance(spec_hash, str) or not SPEC_HASH_RE.match(spec_hash):
        errors.append("invalid_spec_hash")

    evidence_refs = bundle.get("evidence_refs", [])
    if not isinstance(evidence_refs, list) or len(evidence_refs) == 0:
        errors.append("evidence_refs_required")
    else:
        for ref in evidence_refs:
            if not isinstance(ref, str) or not EVIDENCE_REF_RE.match(ref):
                errors.append(f"invalid_evidence_ref:{ref}")

    if bundle.get("evidence_bundle_resolved") is not True:
        errors.append("unresolved_evidence_bundle")

    if bundle.get("rights_status") == "unknown":
        errors.append("unknown_rights")

    if bundle.get("policy_label") == "internal":
        errors.append("internal_policy_label_not_publishable")

    publication_state = bundle.get("publication_state")
    if bundle.get("surface", "public") == "public" and publication_state in {
        "candidate",
        "held",
        "quarantined",
    }:
        errors.append(f"{publication_state}_not_publishable")

    source_role = bundle.get("source_role")

    if source_role == "DERIVED_MODEL_LAYER":
        if bundle.get("claim_status") == "CONFIRMED":
            errors.append("derived_layer_as_confirmed_truth")

        if bundle.get("catalog_closure") is not True and not bundle.get("catalog_refs"):
            errors.append("derived_layer_missing_catalog_closure")

    if source_role == "SENSITIVE_OCCURRENCE":
        if bundle.get("exact_geometry_present") is True:
            errors.append("sensitive_exact_geometry_not_publishable")

        if bundle.get("public_visibility") == "generalized" and not bundle.get("redaction_receipt_ref"):
            errors.append("missing_redaction_receipt")

    if bundle.get("sensitivity") == "restricted" and bundle.get("exact_geometry_present", False):
        errors.append("restricted_exact_geometry_not_allowed")

    if bundle.get("sensitivity") == "review_required":
        errors.append("requires_steward_review")

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ecology bundle descriptor")
    parser.add_argument("--bundle", required=True, help="Path to bundle JSON file")
    parser.add_argument("--sources", default=str(DEFAULT_SOURCES))
    parser.add_argument("--datasets", default=str(DEFAULT_DATASETS))
    parser.add_argument("--policies", default=str(DEFAULT_POLICIES))
    parser.add_argument("--skip-schema", action="store_true", help="Skip JSON Schema validation")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args()

    bundle_path = Path(args.bundle)
    bundle = _load_json(bundle_path)

    sources_registry = _load_yaml_like(Path(args.sources))
    datasets_registry = _load_yaml_like(Path(args.datasets))
    policies_registry = _load_yaml_like(Path(args.policies))

    errors = validate_bundle(
        bundle,
        sources_registry,
        datasets_registry,
        policies_registry,
        validate_schema=not args.skip_schema,
    )

    result = {
        "validator": "tools/validators/ecology/validate_ecology_bundle.py",
        "bundle_path": str(bundle_path),
        "bundle_id": bundle.get("bundle_id"),
        "object_type": bundle.get("object_type"),
        "decision": "pass" if not errors else "fail",
        "errors": errors,
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"decision={result['decision']}")
        print(f"bundle_id={result['bundle_id']}")
        print(f"object_type={result['object_type']}")
        for error in errors:
            print(f"error={error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
