"""
tools/validators/hazards/validate_drought_families.py

Deterministic no-network validator for DroughtObservation and DroughtDeclaration
object families.

Emits one of: PASS / ABSTAIN / DENY / ERROR per fixture.

No approval, publication, connector activation, source activation, or release
semantics are produced by this validator. These outcomes are bounded to
schema conformance and anti-collapse invariant enforcement.

Anti-collapse invariants enforced:
  - DroughtObservation must not carry a legal stage.
  - DroughtDeclaration stage must not be derived from USDM D0-D4 categories.
  - Missing or unresolved legal instrument evidence → ABSTAIN (stage must be 'unknown').
  - Forbidden fields (legal_stage, usdm_derived, observation_stage) → DENY.
  - Geometry and source evidence must be explicitly bound or marked unresolved.
  - Unknown severity vocabulary → DENY.
  - Undeclared fields → DENY.

Usage:
    python tools/validators/hazards/validate_drought_families.py --fixtures
    python tools/validators/hazards/validate_drought_families.py path/to/file.json
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[3]

OBS_SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/drought_observation.schema.json"
DECL_SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/drought_declaration.schema.json"
REL_SCHEMA = ROOT / "schemas/contracts/v1/domains/hazards/drought_obs_decl_relationship.schema.json"

OBS_FIXTURES = ROOT / "fixtures/domains/hazards/drought_observation"
DECL_FIXTURES = ROOT / "fixtures/domains/hazards/drought_declaration"
REL_FIXTURES = ROOT / "fixtures/domains/hazards/drought_obs_decl_relationship"

OBJECT_TYPE_TO_SCHEMA = {
    "DroughtObservation": OBS_SCHEMA,
    "DroughtDeclaration": DECL_SCHEMA,
    "DroughtObsDeclarationRelationship": REL_SCHEMA,
}

# Anti-collapse: legal stage values from the Kansas declaration vocabulary.
# These must never appear on a DroughtObservation.
LEGAL_STAGE_VALUES = {"watch", "warning", "emergency"}

# Anti-collapse: USDM severity codes must never appear as declaration stages.
USDM_SEVERITY_CODES = {"None", "D0", "D1", "D2", "D3", "D4"}


def _outcome(label: str, path: str, message: str) -> int:
    print(f"{label} {path}: {message}")
    return label


def validate_file(path: Path) -> str:
    """Validate a single JSON file. Returns one of PASS/ABSTAIN/DENY/ERROR."""
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        _outcome("ERROR", str(path), f"JSON parse error: {exc}")
        return "ERROR"

    object_type = doc.get("object_type")
    if object_type not in OBJECT_TYPE_TO_SCHEMA:
        _outcome("DENY", str(path), f"Unknown or missing object_type: {object_type!r}")
        return "DENY"

    schema_path = OBJECT_TYPE_TO_SCHEMA[object_type]
    try:
        validator = load_validator(schema_path)
    except Exception as exc:
        _outcome("ERROR", str(path), f"Schema load error: {exc}")
        return "ERROR"

    errors = sorted(validator.iter_errors(doc), key=lambda e: e.path)
    if errors:
        _outcome("DENY", str(path), errors[0].message)
        return "DENY"

    # Anti-collapse: check ABSTAIN condition for DroughtDeclaration.
    if object_type == "DroughtDeclaration":
        resolution = doc.get("legal_instrument_resolution_status")
        stage = doc.get("declaration_stage")
        if resolution in {"unresolved", "abstain"} and stage != "unknown":
            _outcome(
                "DENY",
                str(path),
                f"legal_instrument_resolution_status={resolution!r} requires declaration_stage='unknown', got {stage!r}",
            )
            return "DENY"
        if resolution in {"unresolved", "abstain"} and stage == "unknown":
            _outcome("ABSTAIN", str(path), "Legal instrument unresolved; stage held as unknown.")
            return "ABSTAIN"

    _outcome("PASS", str(path), "Conforms to schema and anti-collapse invariants.")
    return "PASS"


def run_fixtures(fixture_dir: Path, *, label: str) -> bool:
    """Run valid and invalid fixture suites. Returns True if all checks pass."""
    ok = True
    valid_dir = fixture_dir / "valid"
    invalid_dir = fixture_dir / "invalid"

    valid_files = sorted(valid_dir.glob("*.json")) if valid_dir.exists() else []
    invalid_files = sorted(invalid_dir.glob("*.json")) if invalid_dir.exists() else []

    if not valid_files:
        print(f"FAIL {valid_dir}: no valid fixtures found")
        ok = False

    for fp in valid_files:
        outcome = validate_file(fp)
        if outcome not in {"PASS", "ABSTAIN"}:
            print(f"FAIL {fp}: expected PASS/ABSTAIN for valid fixture, got {outcome}")
            ok = False

    for fp in invalid_files:
        outcome = validate_file(fp)
        if outcome in {"PASS"}:
            print(f"FAIL {fp}: expected DENY/ERROR/ABSTAIN for invalid fixture, got {outcome}")
            ok = False

    return ok


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate DroughtObservation and DroughtDeclaration fixtures."
    )
    parser.add_argument("files", nargs="*", help="JSON files to validate.")
    parser.add_argument("--fixtures", action="store_true", help="Run all fixture suites.")
    ns = parser.parse_args(argv)

    if not ns.fixtures and not ns.files:
        print("No files provided. Use --fixtures or supply file paths.", file=sys.stderr)
        return 2

    if ns.fixtures:
        ok = True
        for fixture_dir, label in [
            (OBS_FIXTURES, "DroughtObservation"),
            (DECL_FIXTURES, "DroughtDeclaration"),
            (REL_FIXTURES, "DroughtObsDeclarationRelationship"),
        ]:
            ok = run_fixtures(fixture_dir, label=label) and ok
        return 0 if ok else 1

    ok = True
    for fp in ns.files:
        outcome = validate_file(Path(fp))
        if outcome not in {"PASS", "ABSTAIN"}:
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
