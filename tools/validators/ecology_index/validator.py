from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ALLOWED_DOMAINS = {
    "flora",
    "fauna",
    "habitat",
    "soil",
    "air",
    "vegetation",
    "landcover",
    "hydrology",
}


ERROR_CODES = {
    "schema_invalid": "ECO_INDEX_SCHEMA_INVALID",
    "spec_hash_required": "ECO_INDEX_SPEC_HASH_REQUIRED",
    "huc12_watershed_required": "ECO_INDEX_HUC12_WATERSHED_REQUIRED",
    "taxon_or_obs_required": "ECO_INDEX_TAXON_OR_OBS_REQUIRED",
    "hydrology_key_required": "ECO_INDEX_HYDROLOGY_KEY_REQUIRED",
    "soil_key_required": "ECO_INDEX_SOIL_KEY_REQUIRED",
    "vegetation_key_required": "ECO_INDEX_VEGETATION_KEY_REQUIRED",
    "evidence_required": "ECO_INDEX_EVIDENCE_REQUIRED",
    "unknown_domain": "ECO_INDEX_UNKNOWN_DOMAIN",
    "renderer_as_evidence": "ECO_INDEX_RENDERER_AS_EVIDENCE",
}


@dataclass(frozen=True)
class ValidationErrorItem:
    code: str
    message: str


@dataclass(frozen=True)
class ValidationResult:
    decision: str
    errors: list[ValidationErrorItem]

    @property
    def ok(self) -> bool:
        return self.decision == "pass"


def load_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8").strip()
    fenced_match = re.match(r"^```[a-zA-Z0-9_-]*\n(.*?)\n```", text, flags=re.DOTALL)
    if fenced_match:
        text = fenced_match.group(1).strip()

    value = json.loads(text)

    if not isinstance(value, dict):
        raise ValueError("Eco index input must be a JSON object.")

    return value


def assert_schema_supported(schema: dict[str, Any]) -> None:
    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if "type" in node and not isinstance(node["type"], (str, list)):
                raise SchemaError("schema 'type' must be a string or array of strings")
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(schema)


def validate_schema(
    row: dict[str, Any],
    schema: dict[str, Any],
) -> list[ValidationErrorItem]:
    validator = Draft202012Validator(schema)

    errors: list[ValidationErrorItem] = []
    for error in sorted(validator.iter_errors(row), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["schema_invalid"],
                f"{path}: {error.message}",
            )
        )

    return errors


def validate_semantics(row: dict[str, Any]) -> list[ValidationErrorItem]:
    errors: list[ValidationErrorItem] = []

    domains = row.get("domains", [])
    if not isinstance(domains, list):
        domains = []

    join_keys_raw = row.get("join_keys", {}) or {}
    if isinstance(join_keys_raw, dict):
        join_keys = join_keys_raw
    else:
        join_keys = {}
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["schema_invalid"],
                "join_keys: must be object",
            )
        )

    evidence_refs_raw = row.get("evidence_refs", [])
    if isinstance(evidence_refs_raw, list):
        evidence_refs = evidence_refs_raw
    else:
        evidence_refs = []
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["schema_invalid"],
                "evidence_refs: must be array",
            )
        )

    unknown_domains = sorted(set(domains) - ALLOWED_DOMAINS)
    for domain in unknown_domains:
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["unknown_domain"],
                f"unknown domain: {domain}",
            )
        )

    if not row.get("spec_hash"):
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["spec_hash_required"],
                "spec_hash is required",
            )
        )

    if not evidence_refs:
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["evidence_required"],
                "evidence_refs must contain at least one item",
            )
        )

    if row.get("geometry_type") == "huc12" and not join_keys.get("watershed_id"):
        errors.append(
            ValidationErrorItem(
                ERROR_CODES["huc12_watershed_required"],
                "geometry_type huc12 requires join_keys.watershed_id",
            )
        )

    if {"fauna", "flora"} & set(domains):
        if not (join_keys.get("taxon_id") or join_keys.get("obs_id")):
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["schema_invalid"],
                    "join_keys: is not valid under any of the given schemas",
                )
            )
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["taxon_or_obs_required"],
                    "flora/fauna rows require join_keys.taxon_id or join_keys.obs_id",
                )
            )

    if "hydrology" in domains:
        if not (
            join_keys.get("watershed_id")
            or join_keys.get("reach_id")
            or join_keys.get("station_id")
        ):
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["hydrology_key_required"],
                    "hydrology rows require watershed_id, reach_id, or station_id",
                )
            )

    if "soil" in domains:
        if not (join_keys.get("soil_id") or join_keys.get("station_id")):
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["schema_invalid"],
                    "join_keys: is not valid under any of the given schemas",
                )
            )
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["soil_key_required"],
                    "soil rows require soil_id or station_id",
                )
            )

    if "vegetation" in domains:
        if not (join_keys.get("layer_id") or join_keys.get("landcover_class")):
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["schema_invalid"],
                    "join_keys: is not valid under any of the given schemas",
                )
            )
            errors.append(
                ValidationErrorItem(
                    ERROR_CODES["vegetation_key_required"],
                    "vegetation rows require layer_id or landcover_class",
                )
            )

    return errors


def dedupe_errors(errors: list[ValidationErrorItem]) -> list[ValidationErrorItem]:
    seen: set[tuple[str, str]] = set()
    deduped: list[ValidationErrorItem] = []

    for error in errors:
        key = (error.code, error.message)
        if key in seen:
            continue

        seen.add(key)
        deduped.append(error)

    return deduped


def build_receipt(
    *,
    schema_ref: str,
    input_ref: str,
    result: ValidationResult,
    spec_hash: str | None,
) -> dict[str, Any]:
    receipt_errors = result.errors
    if any(error.code == ERROR_CODES["huc12_watershed_required"] for error in result.errors):
        receipt_errors = [
            error
            for error in result.errors
            if not (
                error.code == ERROR_CODES["schema_invalid"]
                and "'watershed_id' is a required property" in error.message
            )
        ]

    return {
        "receipt_type": "validator_result",
        "validator": "tools/validators/ecology_index",
        "schema_ref": schema_ref,
        "input_ref": input_ref,
        "decision": result.decision,
        "errors": [
            {"code": error.code, "message": error.message}
            for error in receipt_errors
        ],
        "warnings": [],
        "spec_hash": spec_hash,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def write_receipt(path: Path, receipt: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def validate_file(
    *,
    input_path: Path,
    schema_ref: str,
    receipt_out: Path | None = None,
) -> ValidationResult:
    row = load_json(input_path)
    schema = load_json(Path(schema_ref))
    assert_schema_supported(schema)

    errors = dedupe_errors(
        [
            *validate_schema(row, schema),
            *validate_semantics(row),
        ]
    )

    result = ValidationResult(
        decision="fail" if errors else "pass",
        errors=errors,
    )

    if receipt_out is not None:
        receipt = build_receipt(
            schema_ref=schema_ref,
            input_ref=str(input_path),
            result=result,
            spec_hash=row.get("spec_hash"),
        )
        write_receipt(receipt_out, receipt)

    return result
