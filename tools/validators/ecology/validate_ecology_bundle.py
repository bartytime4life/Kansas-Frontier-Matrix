#!/usr/bin/env python3
"""Validate ecology bundle descriptors against registry references and policy prerequisites."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any




def _parse_min_yaml(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_list: str | None = None
    current_item: dict[str, Any] | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue
        if line.startswith('  - '):
            if current_list is None:
                continue
            item: dict[str, Any] = {}
            data.setdefault(current_list, []).append(item)
            current_item = item
            rem = line[4:]
            if ':' in rem:
                k, v = rem.split(':', 1)
                current_item[k.strip()] = v.strip().strip('"')
            continue
        if line.startswith('    ') and current_item is not None and ':' in line.strip():
            k, v = line.strip().split(':', 1)
            val = v.strip().strip('"')
            if val.startswith('[') and val.endswith(']'):
                val = [x.strip().strip('"') for x in val[1:-1].split(',') if x.strip()]
            current_item[k.strip()] = val
            continue
        if not line.startswith(' ') and ':' in line:
            k, v = line.split(':', 1)
            key = k.strip()
            val = v.strip().strip('"')
            if val == '':
                current_list = key
                data[current_list] = []
                current_item = None
            else:
                data[key] = val
                current_list = None
                current_item = None
    return data

def _load_yaml_like(path: Path) -> dict[str, Any]:
    """Load YAML using PyYAML if available, else JSON fallback for YAML-compatible JSON."""
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


def validate_bundle(
    bundle: dict[str, Any],
    sources_registry: dict[str, Any],
    datasets_registry: dict[str, Any],
    policies_registry: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    required = [
        "bundle_id",
        "source_refs",
        "dataset_refs",
        "policy_id",
        "sensitivity",
        "rights_status",
        "evidence_refs",
    ]
    for field in required:
        if field not in bundle:
            errors.append(f"missing_required_field:{field}")

    source_ids = {s.get("source_id") for s in sources_registry.get("sources", []) if isinstance(s, dict)}
    dataset_ids = {d.get("dataset_id") for d in datasets_registry.get("datasets", []) if isinstance(d, dict)}
    policy_ids = {p.get("policy_id") for p in policies_registry.get("policies", []) if isinstance(p, dict)}

    for ref in bundle.get("source_refs", []):
        if ref not in source_ids:
            errors.append(f"unknown_source_ref:{ref}")

    for ref in bundle.get("dataset_refs", []):
        if ref not in dataset_ids:
            errors.append(f"unknown_dataset_ref:{ref}")

    pid = bundle.get("policy_id")
    if pid and pid not in policy_ids:
        errors.append(f"unknown_policy_id:{pid}")

    evidence_refs = bundle.get("evidence_refs", [])
    if not isinstance(evidence_refs, list) or len(evidence_refs) == 0:
        errors.append("evidence_refs_required")

    sensitivity = bundle.get("sensitivity")
    if sensitivity == "restricted" and bundle.get("exact_geometry_present", False):
        errors.append("restricted_exact_geometry_not_allowed")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ecology bundle descriptor")
    parser.add_argument("--bundle", required=True, help="Path to bundle JSON file")
    parser.add_argument("--sources", default="data/registry/ecology/sources.yaml")
    parser.add_argument("--datasets", default="data/registry/ecology/datasets.yaml")
    parser.add_argument("--policies", default="data/registry/ecology/sensitivity_policies.yaml")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args()

    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    sources_registry = _load_yaml_like(Path(args.sources))
    datasets_registry = _load_yaml_like(Path(args.datasets))
    policies_registry = _load_yaml_like(Path(args.policies))

    errors = validate_bundle(bundle, sources_registry, datasets_registry, policies_registry)

    result = {
        "validator": "tools/validators/ecology/validate_ecology_bundle.py",
        "bundle_id": bundle.get("bundle_id"),
        "decision": "pass" if not errors else "fail",
        "errors": errors,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"decision={result['decision']}")
        for error in errors:
            print(f"error={error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
