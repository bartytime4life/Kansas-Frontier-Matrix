#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = ROOT / "schemas" / "air_quality" / "airnow"

POLLUTANTS = {
    "OZONE", "O3", "PM2.5", "PM25", "PM10", "NO2", "SO2", "CO"
}
CATEGORY_BANDS = {
    1: ("Good", 0, 50),
    2: ("Moderate", 51, 100),
    3: ("Unhealthy for Sensitive Groups", 101, 150),
    4: ("Unhealthy", 151, 200),
    5: ("Very Unhealthy", 201, 300),
    6: ("Hazardous", 301, 500),
}


def _schema_for(obj_type: str) -> Path:
    return {
        "AirNowObservation": SCHEMA_DIR / "observation.airnow.v1.schema.json",
        "AirNowForecast": SCHEMA_DIR / "forecast.airnow.v1.schema.json",
        "AirNowIntakeManifest": SCHEMA_DIR / "intake_manifest.airnow.v1.schema.json",
        "AirNowSourceDescriptor": SCHEMA_DIR / "source_descriptor.airnow.v1.schema.json",
        "AirNowIntakeReceipt": SCHEMA_DIR / "intake_receipt.airnow.v1.schema.json",
    }[obj_type]


def validate_doc(doc: dict, input_path: str) -> dict:
    errors, warnings = [], []
    obj_type = doc.get("object_type")
    if obj_type not in {"AirNowObservation", "AirNowForecast", "AirNowIntakeManifest", "AirNowSourceDescriptor", "AirNowIntakeReceipt"}:
        errors.append("object_type.unsupported")
    else:
        schema = json.loads(_schema_for(obj_type).read_text())
        schema_errors = sorted(Draft202012Validator(schema).iter_errors(doc), key=lambda e: list(e.path))
        for e in schema_errors:
            errors.append(f"schema.{'/'.join(str(p) for p in e.path) or '<root>'}:{e.message}")

    if doc.get("fixture_only") is not True:
        errors.append("fixture_only.must_be_true")
    if doc.get("no_live_airnow_data") is not True:
        errors.append("no_live_airnow_data.must_be_true")
    if doc.get("not_for_publication") is not True:
        errors.append("not_for_publication.must_be_true")

    if obj_type in {"AirNowObservation", "AirNowForecast"}:
        if doc.get("preliminary_data") is not True:
            errors.append("preliminary_data.must_be_true")
        pollutant = str(doc.get("parameter_name", "")).upper()
        if pollutant not in POLLUTANTS:
            errors.append("parameter_name.unknown_pollutant")
        aqi = doc.get("aqi")
        if not isinstance(aqi, int) or not (0 <= aqi <= 500):
            errors.append("aqi.out_of_range")
        category = doc.get("category") or {}
        number, name = category.get("number"), category.get("name")
        band = CATEGORY_BANDS.get(number)
        if band is None:
            errors.append("category.number.invalid")
        else:
            expected_name, low, high = band
            if name != expected_name:
                errors.append("category.name.mismatch")
            if isinstance(aqi, int) and not (low <= aqi <= high):
                errors.append("category.aqi_band_mismatch")

    if obj_type == "AirNowIntakeManifest":
        if doc.get("no_network") is not True:
            errors.append("manifest.no_network.must_be_true")
        if doc.get("bulk_loop_prohibited") is not True:
            errors.append("manifest.bulk_loop_prohibited.must_be_true")
        if "bulk" in str(doc.get("intake_mode", "")).lower() or "zip" in str(doc.get("intake_mode", "")).lower():
            errors.append("manifest.intake_mode.bulk_zip_loop_prohibited")

    return {
        "object_type": "ValidationReport",
        "schema_version": "v1",
        "validator": "validate_airnow_layer1.py",
        "input_path": input_path,
        "validation_outcome": "PASS" if not errors else "FAIL",
        "finite_outcome": "ANSWER" if not errors else "DENY",
        "warnings": sorted(warnings),
        "errors": sorted(errors),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_airnow_layer1.py <json-file>", file=sys.stderr)
        return 2
    p = Path(sys.argv[1])
    doc = json.loads(p.read_text())
    report = validate_doc(doc, str(p))
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["validation_outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
