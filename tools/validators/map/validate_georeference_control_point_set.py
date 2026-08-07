#!/usr/bin/env python3
"""Validate fixture-only canonical georeference control-point-set identity."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/georeference_control_point_set.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/georeference_control_point_set/cases.json"
MAX_FILE_BYTES = 1_048_576

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True)
class Result:
    outcome: str
    reasons: tuple[str, ...]


def _pairs(pairs):
    out = {}
    for k, v in pairs:
        if k in out: raise DuplicateKeyError(k)
        out[k] = v
    return out

def _nonfinite(_): raise NonFiniteNumberError

def _finite_decimal(value: str) -> Decimal:
    parsed = Decimal(value)
    if not parsed.is_finite(): raise NonFiniteNumberError
    return parsed

def _read(path: Path):
    try:
        if path.is_symlink(): return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file(): return None, "FILE_NOT_FOUND"
        if path.stat().st_size > MAX_FILE_BYTES: return None, "FILE_TOO_LARGE"
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream, object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_decimal), None
    except UnicodeDecodeError: return None, "JSON_NOT_UTF8"
    except DuplicateKeyError: return None, "JSON_DUPLICATE_KEY"
    except NonFiniteNumberError: return None, "JSON_NONFINITE_NUMBER"
    except json.JSONDecodeError: return None, "JSON_INVALID"
    except OSError: return None, "FILE_READ_ERROR"
    except (RecursionError, ValueError): return None, "JSON_COMPLEXITY_LIMIT"

def _schema_errors(candidate: Mapping[str, Any]) -> list[str]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [str(e.validator) for e in list(validator.iter_errors(candidate))[:100]]
    except Exception:
        return ["SCHEMA_UNAVAILABLE"]

def _decimal_text(value: Any) -> str:
    d = value if isinstance(value, Decimal) else Decimal(str(value))
    if not d.is_finite(): raise ValueError("non-finite coordinate")
    if d == 0: return "0"
    normalized = d.normalize()
    text = format(normalized, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text

def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def _hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(value)).hexdigest()

def _point_strings(point: Sequence[Any]) -> list[str]:
    return [_decimal_text(point[0]), _decimal_text(point[1])]

def identity(candidate: Mapping[str, Any]) -> tuple[str, str, str]:
    resource = candidate["resource_space"]
    target = candidate["target_space"]
    points = candidate["control_points"]
    resource_projection = {
        "resource_space": {
            "kind": resource["kind"], "axis_order": resource["axis_order"],
            "width_px": resource["width_px"], "height_px": resource["height_px"]
        },
        "points": [{"id": p["id"], "resource": _point_strings(p["resource"])} for p in points],
    }
    target_projection = {
        "target_space": {"kind": target["kind"], "axis_order": target["axis_order"], "unit": target["unit"]},
        "points": [{"id": p["id"], "target": _point_strings(p["target"])} for p in points],
    }
    full_projection = {
        "resource_space": resource_projection["resource_space"],
        "target_space": target_projection["target_space"],
        "points": [
            {"id": p["id"], "resource": _point_strings(p["resource"]), "target": _point_strings(p["target"])}
            for p in points
        ],
    }
    resource_hash = _hash(resource_projection)
    target_hash = _hash(target_projection)
    set_id = "kfm:georeference-gcp-set:sha256:" + hashlib.sha256(_canonical_json(full_projection)).hexdigest()
    return set_id, resource_hash, target_hash

def derive(candidate: Mapping[str, Any]) -> Result:
    points = candidate["control_points"]
    if candidate["control_point_count"] != len(points):
        return Result("ERROR", ("CONTROL_POINT_COUNT_MISMATCH",))
    ids = [p["id"] for p in points]
    if ids != sorted(ids) or len(ids) != len(set(ids)):
        return Result("ERROR", ("POINT_IDS_NOT_CANONICAL",))
    resources = [tuple(_decimal_text(v) for v in p["resource"]) for p in points]
    targets = [tuple(_decimal_text(v) for v in p["target"]) for p in points]
    if len(resources) != len(set(resources)):
        return Result("ERROR", ("DUPLICATE_RESOURCE_POINT",))
    if len(targets) != len(set(targets)):
        return Result("ERROR", ("DUPLICATE_TARGET_POINT",))
    width = Decimal(candidate["resource_space"]["width_px"])
    height = Decimal(candidate["resource_space"]["height_px"])
    for p in points:
        x = p["resource"][0] if isinstance(p["resource"][0], Decimal) else Decimal(str(p["resource"][0]))
        y = p["resource"][1] if isinstance(p["resource"][1], Decimal) else Decimal(str(p["resource"][1]))
        if x < 0 or y < 0 or x > width or y > height:
            return Result("ERROR", ("RESOURCE_POINT_OUT_OF_BOUNDS",))
    expected_id, resource_hash, target_hash = identity(candidate)
    reasons = []
    if candidate["resource_set_hash"] != resource_hash: reasons.append("RESOURCE_SET_HASH_MISMATCH")
    if candidate["target_set_hash"] != target_hash: reasons.append("TARGET_SET_HASH_MISMATCH")
    if candidate["set_id"] != expected_id: reasons.append("SET_ID_MISMATCH")
    if reasons: return Result("ERROR", tuple(sorted(reasons)))
    return Result("VALID", ("GEOREFERENCE_CONTROL_POINT_SET_VALID",))

def validate_candidate(candidate: Any) -> Result:
    if not isinstance(candidate, Mapping): return Result("ERROR", ("ROOT_NOT_OBJECT",))
    if _schema_errors(candidate): return Result("ERROR", ("SCHEMA_INVALID",))
    result = derive(candidate)
    decision = candidate["decision"]
    if decision["outcome"] != result.outcome or decision["reasons"] != list(result.reasons):
        return Result("ERROR", ("DECISION_MISMATCH",))
    return result

def _parts(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"): raise ValueError
    return [] if pointer == "/" else [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")]

def _set(obj: dict[str, Any], pointer: str, value: Any) -> None:
    target: Any = obj
    parts = _parts(pointer)
    for part in parts[:-1]: target = target[int(part)] if isinstance(target, list) else target[part]
    leaf = parts[-1]
    if isinstance(target, list): target[int(leaf)] = copy.deepcopy(value)
    else: target[leaf] = copy.deepcopy(value)

def materialize_case(manifest: Mapping[str, Any], entry: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    for mutation in entry.get("mutations", []): _set(candidate, mutation["path"], mutation["value"])
    if entry.get("recompute", False):
        candidate["control_point_count"] = len(candidate["control_points"])
        set_id, resource_hash, target_hash = identity(candidate)
        candidate["set_id"] = set_id; candidate["resource_set_hash"] = resource_hash; candidate["target_set_hash"] = target_hash
    if "decision" in entry: candidate["decision"] = copy.deepcopy(entry["decision"])
    return candidate

def validate_fixtures() -> int:
    manifest, error = _read(FIXTURE_PATH)
    if error or not isinstance(manifest, Mapping) or not isinstance(manifest.get("cases"), list):
        print("ERROR: fixture manifest invalid"); return 1
    failed = False; outcomes = set()
    for entry in manifest["cases"]:
        candidate = materialize_case(manifest, entry); result = validate_candidate(candidate)
        actual = {"outcome": result.outcome, "reasons": list(result.reasons)}
        print(json.dumps({"case_id": entry["case_id"], **actual}, sort_keys=True, separators=(",", ":")))
        failed |= actual != entry["expected"]; outcomes.add(result.outcome)
    if outcomes != {"VALID", "ERROR"}: failed = True
    if failed: return 1
    print(f"CONFIRMED: {len(manifest['cases'])} georeference control-point-set cases passed exact polarity."); return 0

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true"); args = parser.parse_args(argv)
    if args.fixtures: return validate_fixtures()
    if not args.files: parser.error("provide files or --fixtures")
    failed = False
    for path in args.files:
        value, error = _read(path); result = Result("ERROR", (error,)) if error else validate_candidate(value)
        print(json.dumps({"file": path.name, "outcome": result.outcome, "reasons": list(result.reasons)}, sort_keys=True, separators=(",", ":")))
        failed |= result.outcome != "VALID"
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
