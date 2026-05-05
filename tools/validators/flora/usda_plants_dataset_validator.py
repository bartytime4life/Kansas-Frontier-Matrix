from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path("schemas/flora/usda_plants_dataset.schema.json")
SYMBOL_RE = re.compile(r"^[A-Z0-9]+$")
AUTHOR_RE = re.compile(r"^[A-Z][a-z-]+\s+[a-z-]+\s+.+$")
FIPS_RE = re.compile(r"^\d{5}$")


def _schema_validate(payload: dict[str, Any], schema_path: Path, reasons: list[str]) -> None:
    if not schema_path.exists():
        reasons.append("schema.missing")
        return
    try:
        from jsonschema import Draft202012Validator  # type: ignore
    except ImportError:
        reasons.append("dependency.jsonschema_missing")
        return

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for error in validator.iter_errors(payload):
        path_parts = getattr(error, "absolute_path", getattr(error, "path", ()))
        field_path = ".".join(str(part) for part in path_parts) or "root"
        reasons.append(f"schema.invalid:{field_path}")


def validate_dataset(payload: dict[str, Any], schema_path: Path = SCHEMA_PATH) -> dict[str, Any]:
    reasons: list[str] = []
    _schema_validate(payload, schema_path, reasons)

    props = payload.get("properties") if isinstance(payload.get("properties"), dict) else {}
    symbol = props.get("plants:symbol")
    if not isinstance(symbol, str) or not SYMBOL_RE.fullmatch(symbol):
        reasons.append("field.symbol.invalid")

    scientific_name = props.get("scientificName")
    if not isinstance(scientific_name, str) or not AUTHOR_RE.match(scientific_name.strip()):
        reasons.append("field.scientific_name.missing_author")

    family = props.get("family")
    if not isinstance(family, str) or not family.strip():
        reasons.append("field.family.empty")

    if props.get("license") != "USDA / U.S. Public Domain":
        reasons.append("field.license.invalid")

    if props.get("rightsHolder") != "United States Department of Agriculture":
        reasons.append("field.rights_holder.invalid")

    counties = payload.get("distributions", {}).get("county", []) if isinstance(payload.get("distributions"), dict) else []
    if isinstance(counties, list):
        for idx, county in enumerate(counties):
            fips = county.get("fips") if isinstance(county, dict) else None
            if not isinstance(fips, str) or not FIPS_RE.fullmatch(fips):
                reasons.append(f"field.county_fips.invalid:{idx}")
    else:
        reasons.append("field.county_fips.invalid_type")

    top_spec_hash = payload.get("spec_hash")
    prop_spec_hash = props.get("kfm:spec_hash")
    if top_spec_hash != prop_spec_hash:
        reasons.append("field.spec_hash.mismatch")

    reasons = sorted(set(reasons))
    return {"result": "pass" if not reasons else "fail", "reason_codes": reasons}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate USDA PLANTS dataset fixture/object")
    parser.add_argument("dataset", type=Path, help="Path to one USDA PLANTS dataset JSON object")
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH, help="Path to JSON schema")
    args = parser.parse_args()

    payload = json.loads(args.dataset.read_text(encoding="utf-8"))
    result = validate_dataset(payload, args.schema)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
