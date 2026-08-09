"""Validate fixture-only LiDAR derived-product lineage receipts."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/spatial-foundation/lidar_derived_product_lineage_receipt/cases.json"
SCOPE = "spatial-foundation.lidar-derived-product-lineage-receipt"

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())

_ROLE_MAP = {
    "LAZ": ("OBSERVED", "SOURCE_CAPTURE"),
    "COPC": ("OBSERVED", "ANALYTIC_ACCESS_CARRIER"),
    "EPT": ("OBSERVED", "ANALYTIC_ACCESS_CARRIER"),
    "DEM": ("MODELED", "ELEVATION_MODEL"),
    "TERRAIN": ("MODELED", "TERRAIN_DERIVATIVE"),
}
_ZERO_DIGEST = "sha256:" + ("0" * 64)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    lineage_outcome: str | None
    findings: tuple[Finding, ...]
    lineage_id: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _sorted_unique(values: list[object]) -> bool:
    encoded = [json.dumps(value, sort_keys=True, separators=(",", ":")) for value in values]
    return encoded == sorted(encoded) and len(encoded) == len(set(encoded))


def _set_path(document: object, path: str, value: object) -> None:
    parts = path.split(".")
    target: object = document
    for part in parts[:-1]:
        if isinstance(target, dict):
            target = target[part]
        elif isinstance(target, list):
            target = target[int(part)]
        else:
            raise ValueError("mutation path cannot be traversed")
    final = parts[-1]
    if isinstance(target, dict):
        target[final] = value
    elif isinstance(target, list):
        target[int(final)] = value
    else:
        raise ValueError("mutation target is not a container")


def _identity(document: Mapping[str, Any]) -> tuple[str, str]:
    projection = {
        key: value
        for key, value in document.items()
        if key not in {"lineage_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(projection)
    return (
        "kfm:lidar-derived-product-lineage:"
        + spec_hash.removeprefix("sha256:"),
        spec_hash,
    )


def _product_map(document: Mapping[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    products = [item for item in document.get("products", []) if isinstance(item, dict)]
    return products, {
        item["node_id"]: item
        for item in products
        if isinstance(item.get("node_id"), str)
    }


def _has_laz_ancestor(
    node_id: str,
    root_id: str,
    products: Mapping[str, Mapping[str, Any]],
    visiting: frozenset[str] = frozenset(),
) -> bool:
    if node_id == root_id:
        return True
    if node_id in visiting:
        return False
    node = products.get(node_id)
    if not isinstance(node, Mapping):
        return False
    parents = node.get("parent_node_ids")
    if not isinstance(parents, list) or not parents:
        return False
    next_visiting = visiting | {node_id}
    return any(
        isinstance(parent, str)
        and _has_laz_ancestor(parent, root_id, products, next_visiting)
        for parent in parents
    )


def _derive_summary(document: Mapping[str, Any]) -> dict[str, object]:
    products, by_id = _product_map(document)
    laz_nodes = [item for item in products if item.get("product_kind") == "LAZ"]
    root = laz_nodes[0] if laz_nodes else (products[0] if products else {})
    root_id = root.get("node_id", "lidar-node:00:invalid")

    referenced = {
        parent
        for item in products
        for parent in item.get("parent_node_ids", [])
        if isinstance(parent, str) and parent in by_id
    }
    leaf_ids = sorted(
        item["node_id"]
        for item in products
        if isinstance(item.get("node_id"), str) and item["node_id"] not in referenced
    )
    edge_count = sum(
        len(item.get("parent_node_ids", []))
        for item in products
        if isinstance(item.get("parent_node_ids"), list)
    )
    role_mapping = all(
        _ROLE_MAP.get(item.get("product_kind"))
        == (item.get("source_role"), item.get("product_role"))
        for item in products
    )

    acquisition = root.get("acquisition_window")
    acquisition_preserved = bool(products) and all(
        item.get("acquisition_window") == acquisition for item in products
    )
    spatial_projection = (
        root.get("quality_level"),
        root.get("horizontal_crs_ref"),
        root.get("vertical_reference"),
    )
    spatial_preserved = bool(products) and all(
        (
            item.get("quality_level"),
            item.get("horizontal_crs_ref"),
            item.get("vertical_reference"),
        )
        == spatial_projection
        for item in products
    )
    ancestry_closed = (
        len(laz_nodes) == 1
        and isinstance(root_id, str)
        and all(
            isinstance(item.get("node_id"), str)
            and _has_laz_ancestor(item["node_id"], root_id, by_id)
            for item in products
        )
    )
    return {
        "root_node_id": root_id,
        "leaf_node_ids": leaf_ids,
        "edge_count": edge_count,
        "all_nodes_have_laz_ancestor": ancestry_closed,
        "role_mapping_preserved": role_mapping,
        "acquisition_window_preserved": acquisition_preserved,
        "spatial_reference_preserved": spatial_preserved,
    }


def _finalize_document(document: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(document))
    candidate["lineage_summary"] = _derive_summary(candidate)
    candidate["outcome"] = "LINEAGE_RECORDED"
    lineage_id, spec_hash = _identity(candidate)
    candidate["lineage_id"] = lineage_id
    candidate["spec_hash"] = spec_hash
    return candidate


def materialize_case(base_document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate: dict[str, Any] = copy.deepcopy(dict(base_document))
    mutations = case.get("mutations", [])
    if not isinstance(mutations, list):
        raise ValueError("mutations must be a list")
    for mutation in mutations:
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise ValueError("invalid mutation")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
    candidate = _finalize_document(candidate)
    tamper = case.get("tamper", [])
    if not isinstance(tamper, list):
        raise ValueError("tamper must be a list")
    for mutation in tamper:
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise ValueError("invalid tamper")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
    return candidate


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def validate_document(document: object) -> ValidationResult:
    findings: set[Finding] = set()
    try:
        schema_errors = sorted(
            _VALIDATOR.iter_errors(document),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult("ERROR", None, (Finding("SCHEMA_UNAVAILABLE", "$"),))
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(document, dict):
        return ValidationResult("DENY", None, tuple(sorted(findings)))

    products, by_id = _product_map(document)
    node_ids = [item.get("node_id") for item in products]
    if not _sorted_unique(node_ids):
        findings.add(Finding("PRODUCT_ORDER_OR_ID_INVALID", "$.products"))

    for path, values in (
        ("$.evidence_refs", document["evidence_refs"]),
        ("$.lineage_summary.leaf_node_ids", document["lineage_summary"]["leaf_node_ids"]),
    ):
        if not _sorted_unique(values):
            findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", path))

    laz_indexes = [
        index for index, item in enumerate(products) if item.get("product_kind") == "LAZ"
    ]
    if laz_indexes != [0]:
        findings.add(Finding("LAZ_ROOT_INVALID", "$.products"))
    root_id = products[0]["node_id"] if laz_indexes == [0] else None

    for index, product in enumerate(products):
        path = f"$.products[{index}]"
        parents = product["parent_node_ids"]
        transforms = product["transform_receipt_refs"]
        if not _sorted_unique(parents):
            findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", path + ".parent_node_ids"))
        if not _sorted_unique(transforms):
            findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", path + ".transform_receipt_refs"))

        expected_role = _ROLE_MAP.get(product["product_kind"])
        if expected_role != (product["source_role"], product["product_role"]):
            findings.add(Finding("SOURCE_ROLE_MISMATCH", path))

        if product["artifact_spec_hash"] == _ZERO_DIGEST:
            findings.add(Finding("DIGEST_PLACEHOLDER", path + ".artifact_spec_hash"))

        if product["product_kind"] == "LAZ":
            if parents:
                findings.add(Finding("LAZ_PARENT_FORBIDDEN", path + ".parent_node_ids"))
            if transforms:
                findings.add(Finding("LAZ_TRANSFORM_FORBIDDEN", path + ".transform_receipt_refs"))
        else:
            if not parents:
                findings.add(Finding("DERIVED_PARENT_REQUIRED", path + ".parent_node_ids"))
            if not transforms:
                findings.add(Finding("DERIVED_TRANSFORM_REQUIRED", path + ".transform_receipt_refs"))

        for parent in parents:
            if parent not in by_id:
                findings.add(Finding("LINEAGE_PARENT_UNKNOWN", path + ".parent_node_ids"))
            elif node_ids.index(parent) >= index:
                findings.add(Finding("LINEAGE_NOT_TOPOLOGICAL", path + ".parent_node_ids"))

        window = product["acquisition_window"]
        start = _parse_time(window["start"])
        end = _parse_time(window["end"])
        if start is not None and end is not None and start > end:
            findings.add(Finding("ACQUISITION_WINDOW_INVALID", path + ".acquisition_window"))

    if root_id is not None:
        root = by_id[root_id]
        for index, product in enumerate(products[1:], start=1):
            path = f"$.products[{index}]"
            if not _has_laz_ancestor(product["node_id"], root_id, by_id):
                findings.add(Finding("LAZ_ANCESTRY_MISSING", path + ".parent_node_ids"))
            if product["acquisition_window"] != root["acquisition_window"]:
                findings.add(Finding("ACQUISITION_WINDOW_MISMATCH", path + ".acquisition_window"))
            if (
                product["quality_level"],
                product["horizontal_crs_ref"],
                product["vertical_reference"],
            ) != (
                root["quality_level"],
                root["horizontal_crs_ref"],
                root["vertical_reference"],
            ):
                findings.add(Finding("SPATIAL_REFERENCE_MISMATCH", path))

    expected_summary = _derive_summary(document)
    if document["lineage_summary"] != expected_summary:
        findings.add(Finding("LINEAGE_SUMMARY_MISMATCH", "$.lineage_summary"))
    if not document["lineage_summary"]["all_nodes_have_laz_ancestor"]:
        findings.add(Finding("LAZ_ANCESTRY_MISSING", "$.lineage_summary"))
    if not document["lineage_summary"]["role_mapping_preserved"]:
        findings.add(Finding("SOURCE_ROLE_MISMATCH", "$.lineage_summary"))
    if not document["lineage_summary"]["acquisition_window_preserved"]:
        findings.add(Finding("ACQUISITION_WINDOW_MISMATCH", "$.lineage_summary"))
    if not document["lineage_summary"]["spatial_reference_preserved"]:
        findings.add(Finding("SPATIAL_REFERENCE_MISMATCH", "$.lineage_summary"))

    if document["source_descriptor_spec_hash"] == _ZERO_DIGEST:
        findings.add(Finding("DIGEST_PLACEHOLDER", "$.source_descriptor_spec_hash"))

    try:
        expected_id, expected_hash = _identity(document)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", document["outcome"], tuple(sorted(findings)))
    if document["lineage_id"] != expected_id:
        findings.add(Finding("LINEAGE_ID_MISMATCH", "$.lineage_id"))
    if document["spec_hash"] != expected_hash:
        findings.add(Finding("LINEAGE_SPEC_HASH_MISMATCH", "$.spec_hash"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        document["outcome"],
        tuple(sorted(findings)),
        expected_id,
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult("ERROR", None, (Finding("LINEAGE_JSON_INVALID", "$"),))
    return validate_document(document)


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "lineage_id": result.lineage_id,
            "lineage_outcome": result.lineage_outcome,
            "scope": SCOPE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    if not isinstance(suite, dict) or not isinstance(suite.get("base_document"), dict):
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    reports: list[dict[str, object]] = []
    ok = True
    for case in suite.get("cases", []):
        if not isinstance(case, dict):
            ok = False
            continue
        try:
            document = materialize_case(suite["base_document"], case)
            result = validate_document(document)
        except (KeyError, IndexError, TypeError, ValueError, CanonicalizationFailure):
            ok = False
            continue
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.status == expected.get("status")
            and result.lineage_outcome == expected.get("lineage_outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        reports.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.lineage_outcome,
                "actual_status": result.status,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes") if isinstance(expected, dict) else None,
                "expected_outcome": expected.get("lineage_outcome") if isinstance(expected, dict) else None,
                "expected_status": expected.get("status") if isinstance(expected, dict) else None,
                "ok": case_ok,
            }
        )
    return bool(reports) and ok, {
        "cases": reports,
        "ok": bool(reports) and ok,
        "scope": SCOPE,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("--fixtures cannot be combined with a path")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(_serialize(result))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
