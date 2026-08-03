"""No-network CorridorRoute validator with PASS/ABSTAIN/DENY/ERROR outcomes."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from tools.validators._common.jsonschema_runner import load_validator

SCHEMA = ROOT / "schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json"
FIXTURES = ROOT / "fixtures/domains/roads-rail-trade/corridor_route"
OUTCOMES = {"PASS", "ABSTAIN", "DENY", "ERROR"}


def emit(outcome: str, path: Path, message: str) -> str:
    print(f"{outcome} {path}: {message}")
    return outcome


def canonical_payload(document: dict[str, Any]) -> bytes:
    payload = {k: v for k, v in document.items() if k not in {"_fixture_meta", "spec_hash"}}
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def compute_spec_hash(document: dict[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(canonical_payload(document)).hexdigest()


def load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def schema_message(error: Any, document: dict[str, Any]) -> str:
    if (
        error.validator == "not"
        and document.get("geometry_accuracy") == "derived-geocode"
        and document.get("representation_layer") == "authoritative"
    ):
        return "derived-geocode geometry cannot be authoritative"
    pointer = "/" + "/".join(str(part) for part in error.path) if error.path else "/"
    detail = " ".join(error.message.split())
    if len(detail) > 240:
        detail = detail[:237] + "..."
    return f"schema {error.validator} failure at {pointer}: {detail}"


def validate_file(path: Path) -> str:
    try:
        document = load_object(path)
        validator = load_validator(SCHEMA)
    except Exception as exc:
        return emit("ERROR", path, f"load error: {exc}")

    errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
    if errors:
        return emit("DENY", path, schema_message(errors[0], document))
    if document["spec_hash"] != compute_spec_hash(document):
        return emit("DENY", path, "spec_hash does not match canonical content")

    try:
        start = date.fromisoformat(document["valid_time"]["start"])
        end = date.fromisoformat(document["valid_time"]["end"])
    except (KeyError, TypeError, ValueError) as exc:
        return emit("DENY", path, f"invalid valid_time: {exc}")
    if start > end:
        return emit("DENY", path, "valid_time.start must not be later than valid_time.end")

    public_geometry = document["public_geometry_posture"] == "generalized"
    if public_geometry and document["sensitivity"] in {"restricted", "sensitive"}:
        return emit("DENY", path, "sensitive route geometry cannot be generalized for public use")
    if public_geometry and document["rights_status"] in {"restricted", "proprietary"}:
        return emit("DENY", path, "rights block public route geometry")

    unresolved = []
    if document["source_resolution_status"] != "bound":
        unresolved.append("source")
    if document["evidence_resolution_status"] != "bound":
        unresolved.append("evidence")
    if document["geometry_resolution_status"] == "unresolved":
        unresolved.append("geometry")
    if document["rights_status"] == "unknown":
        unresolved.append("rights")
    if unresolved:
        if document["release_posture"] == "released" or document["claim_status"] == "released":
            return emit("DENY", path, "released posture cannot contain unresolved support")
        return emit("ABSTAIN", path, "unresolved support: " + ", ".join(sorted(set(unresolved))))

    if document["rights_status"] in {"restricted", "proprietary"}:
        return emit("ABSTAIN", path, "rights keep the candidate non-public")
    if document["sensitivity"] in {"restricted", "sensitive"}:
        return emit("ABSTAIN", path, "sensitivity requires steward review or withholding")
    return emit("PASS", path, "schema, hash, time, source-role, and public-safety checks passed")


def run_fixtures() -> bool:
    ok = True
    for lane in ("valid", "invalid"):
        paths = sorted((FIXTURES / lane).glob("*.json"))
        if not paths:
            print(f"FAIL {FIXTURES / lane}: no fixtures")
            ok = False
        for path in paths:
            try:
                expected = load_object(path)["_fixture_meta"]["expected_outcome"]
            except Exception as exc:
                print(f"FAIL {path}: expected outcome unavailable: {exc}")
                ok = False
                continue
            actual = validate_file(path)
            if expected not in OUTCOMES or actual != expected:
                print(f"FAIL {path}: expected {expected}, got {actual}")
                ok = False
    return ok


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return 0 if run_fixtures() else 1
    if not args.files:
        return 2
    return 0 if all(validate_file(Path(item)) in {"PASS", "ABSTAIN"} for item in args.files) else 1


if __name__ == "__main__":
    raise SystemExit(main())
