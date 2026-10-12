#!/usr/bin/env python3
"""Validate deterministic synthetic affine georeference transform quality."""
from __future__ import annotations

import argparse
import copy
import json
import math
from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/georeference_transform_quality.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/georeference_transform_quality/cases.json"
MAX_FILE_BYTES = 1_048_576
Q = Decimal("0.000001")
EPS = Decimal("1e-30")

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
class DegenerateGeometry(ValueError): pass

@dataclass(frozen=True)
class Quality:
    coefficients: tuple[Decimal, ...]
    rms: Decimal
    max_residual: Decimal
    loo_rms: Decimal | None
    loo_max_residual: Decimal | None

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

def _finite_float(v):
    x = float(v)
    if not math.isfinite(x): raise NonFiniteNumberError
    return x

def _read(path: Path):
    try:
        if path.is_symlink(): return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file(): return None, "FILE_NOT_FOUND"
        if path.stat().st_size > MAX_FILE_BYTES: return None, "FILE_TOO_LARGE"
        with path.open("r", encoding="utf-8") as f:
            return json.load(f, object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float), None
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

def _D(v: Any) -> Decimal: return Decimal(str(v))

def _solve3(a: list[list[Decimal]], b: list[Decimal]) -> tuple[Decimal, Decimal, Decimal]:
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    with localcontext() as ctx:
        ctx.prec = 50
        for c in range(3):
            pivot = max(range(c, 3), key=lambda r: abs(m[r][c]))
            if abs(m[pivot][c]) <= EPS: raise DegenerateGeometry
            m[c], m[pivot] = m[pivot], m[c]
            p = m[c][c]
            m[c] = [x / p for x in m[c]]
            for r in range(3):
                if r == c: continue
                f = m[r][c]
                m[r] = [m[r][j] - f * m[c][j] for j in range(4)]
        return m[0][3], m[1][3], m[2][3]

def _fit(gcps: Sequence[Mapping[str, Any]]) -> tuple[Decimal, ...]:
    rows = [(_D(g["resource"][0]), _D(g["resource"][1]), _D(g["target"][0]), _D(g["target"][1])) for g in gcps]
    n = Decimal(len(rows)); sx = sum((r[0] for r in rows), Decimal(0)); sy = sum((r[1] for r in rows), Decimal(0))
    sxx = sum((r[0]*r[0] for r in rows), Decimal(0)); syy = sum((r[1]*r[1] for r in rows), Decimal(0)); sxy = sum((r[0]*r[1] for r in rows), Decimal(0))
    A = [[n, sx, sy], [sx, sxx, sxy], [sy, sxy, syy]]
    bx = [sum((r[2] for r in rows), Decimal(0)), sum((r[0]*r[2] for r in rows), Decimal(0)), sum((r[1]*r[2] for r in rows), Decimal(0))]
    by = [sum((r[3] for r in rows), Decimal(0)), sum((r[0]*r[3] for r in rows), Decimal(0)), sum((r[1]*r[3] for r in rows), Decimal(0))]
    return _solve3(A, bx) + _solve3(A, by)

def _residual(g: Mapping[str, Any], c: tuple[Decimal, ...]) -> Decimal:
    x, y = _D(g["resource"][0]), _D(g["resource"][1]); X, Y = _D(g["target"][0]), _D(g["target"][1])
    px = c[0] + c[1]*x + c[2]*y; py = c[3] + c[4]*x + c[5]*y
    with localcontext() as ctx:
        ctx.prec = 50
        return ((px-X)*(px-X) + (py-Y)*(py-Y)).sqrt()

def _rms(values: Sequence[Decimal]) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 50
        return (sum((v*v for v in values), Decimal(0)) / Decimal(len(values))).sqrt()

def _round(v: Decimal | None) -> float | None:
    return None if v is None else float(v.quantize(Q, rounding=ROUND_HALF_EVEN))

def compute_quality(gcps: Sequence[Mapping[str, Any]]) -> Quality:
    resources = [tuple(map(_D, g["resource"])) for g in gcps]
    if len(set(resources)) != len(resources): raise ValueError("DUPLICATE_RESOURCE_GCP")
    coeff = _fit(gcps)
    residuals = [_residual(g, coeff) for g in gcps]
    loo: list[Decimal] = []
    if len(gcps) >= 4:
        for i, held in enumerate(gcps):
            subset = [g for j, g in enumerate(gcps) if j != i]
            try: loo.append(_residual(held, _fit(subset)))
            except DegenerateGeometry: raise ValueError("LOO_GEOMETRY_DEGENERATE")
    return Quality(coeff, _rms(residuals), max(residuals), _rms(loo) if loo else None, max(loo) if loo else None)

def _declared(q: Quality) -> dict[str, Any]:
    return {
        "affine_coefficients": [_round(v) for v in q.coefficients],
        "rms": _round(q.rms), "max_residual": _round(q.max_residual),
        "loo_rms": _round(q.loo_rms), "loo_max_residual": _round(q.loo_max_residual),
    }

def derive(candidate: Mapping[str, Any]) -> Result:
    gcps = candidate["gcps"]
    if candidate["gcp_count"] != len(gcps): return Result("ERROR", ("GCP_COUNT_MISMATCH",))
    try: q = compute_quality(gcps)
    except DegenerateGeometry: return Result("ERROR", ("DEGENERATE_GCP_GEOMETRY",))
    except ValueError as exc: return Result("ERROR", (str(exc),))
    if candidate["computed"] != _declared(q): return Result("ERROR", ("METRIC_MISMATCH",))
    t = candidate["thresholds"]; hold: list[str] = []
    if len(gcps) < t["minimum_gcps"]: hold.append("INSUFFICIENT_REDUNDANCY")
    if q.rms > _D(t["max_rms"]): hold.append("RMS_THRESHOLD_EXCEEDED")
    if q.max_residual > _D(t["max_residual"]): hold.append("MAX_RESIDUAL_THRESHOLD_EXCEEDED")
    if q.loo_rms is not None and q.loo_rms > _D(t["max_loo_rms"]): hold.append("LOO_RMS_THRESHOLD_EXCEEDED")
    if q.loo_max_residual is not None and q.loo_max_residual > _D(t["max_loo_residual"]): hold.append("LOO_MAX_RESIDUAL_THRESHOLD_EXCEEDED")
    return Result("HOLD", tuple(sorted(hold))) if hold else Result("READY", ("GEOREFERENCE_TRANSFORM_QUALITY_READY",))

def validate_candidate(candidate: Any) -> Result:
    if not isinstance(candidate, Mapping): return Result("ERROR", ("ROOT_NOT_OBJECT",))
    errors = _schema_errors(candidate)
    if errors: return Result("ERROR", ("SCHEMA_INVALID",))
    result = derive(candidate)
    decision = candidate["decision"]
    if decision["outcome"] != result.outcome or decision["reasons"] != list(result.reasons): return Result("ERROR", ("DECISION_MISMATCH",))
    return result

def _parts(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"): raise ValueError
    return [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")] if pointer != "/" else []

def _set(obj: dict[str, Any], pointer: str, value: Any) -> None:
    parts = _parts(pointer); target: Any = obj
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    leaf = parts[-1]
    if isinstance(target, list): target[int(leaf)] = copy.deepcopy(value)
    else: target[leaf] = copy.deepcopy(value)

def _truncate(obj: dict[str, Any], pointer: str, length: int) -> None:
    parts = _parts(pointer); target: Any = obj
    for part in parts:
        target = target[int(part)] if isinstance(target, list) else target[part]
    if not isinstance(target, list) or not isinstance(length, int) or length < 0: raise ValueError("invalid truncate mutation")
    del target[length:]

def materialize_case(manifest: Mapping[str, Any], entry: Mapping[str, Any]) -> dict[str, Any]:
    c = copy.deepcopy(manifest["base_candidate"])
    for mutation in entry.get("mutations", []):
        op = mutation.get("op", "set")
        if op == "set": _set(c, mutation["path"], mutation["value"])
        elif op == "truncate": _truncate(c, mutation["path"], mutation["length"])
        else: raise ValueError("unsupported mutation")
    if entry.get("recompute", False):
        try: c["computed"] = _declared(compute_quality(c["gcps"]))
        except (DegenerateGeometry, ValueError): pass
    if "decision" in entry: c["decision"] = copy.deepcopy(entry["decision"])
    return c

def validate_fixtures() -> int:
    value, error = _read(FIXTURE_PATH)
    if error or not isinstance(value, dict) or not isinstance(value.get("cases"), list): print("ERROR: fixture manifest invalid"); return 1
    failed = False; outcomes: set[str] = set()
    for entry in value["cases"]:
        c = materialize_case(value, entry); r = validate_candidate(c); actual = {"outcome": r.outcome, "reasons": list(r.reasons)}
        print(json.dumps({"case_id": entry["case_id"], **actual}, sort_keys=True, separators=(",", ":")))
        failed = failed or actual != entry["expected"]; outcomes.add(r.outcome)
    if outcomes != {"READY", "HOLD", "ERROR"}: failed = True
    if failed: return 1
    print(f"CONFIRMED: {len(value['cases'])} georeference transform-quality cases passed exact polarity."); return 0

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true"); args = parser.parse_args(argv)
    if args.fixtures: return validate_fixtures()
    if not args.files: parser.error("provide files or --fixtures")
    failed = False
    for path in args.files:
        value, error = _read(path); r = Result("ERROR", (error,)) if error else validate_candidate(value)
        print(json.dumps({"file": path.name, "outcome": r.outcome, "reasons": list(r.reasons)}, sort_keys=True, separators=(",", ":"))); failed |= r.outcome != "READY"
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
