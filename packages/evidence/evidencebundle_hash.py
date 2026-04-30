from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def build_hash_input(bundle: dict[str, Any]) -> dict[str, Any]:
    spec = bundle.get("spec")
    if isinstance(spec, dict):
        return spec

    return {
        "schema_version": bundle.get("schema_version"),
        "object_type": bundle.get("object_type"),
        "domain": bundle.get("domain"),
        "source": bundle.get("source"),
        "source_uri": bundle.get("source_uri"),
        "query_predicate": bundle.get("query_predicate"),
        "aggregate": bundle.get("aggregate"),
        "suppression_min_n": bundle.get("suppression_min_n"),
        "mapping": bundle.get("mapping"),
    }


def compute_spec_hash(bundle: dict[str, Any]) -> str:
    digest = hashlib.sha256(canonical_json(build_hash_input(bundle)).encode("utf-8")).hexdigest()
    return f"sha256:{digest}"
