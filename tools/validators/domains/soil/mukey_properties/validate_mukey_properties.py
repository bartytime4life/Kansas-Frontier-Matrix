#!/usr/bin/env python3
"""No-network validator for the inactive, fixture-only MukeyProperties profile."""
from __future__ import annotations

import argparse, hashlib, json, math
from collections import namedtuple
from pathlib import Path
from typing import Any, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[5]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/soil/mukey_properties.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/domains/soil/mukey_properties"
SCOPE = "soil-mukey-properties-fixture-only"
Finding = namedtuple("Finding", "code field")
ERROR = {"INPUT_NOT_FILE", "INPUT_SYMLINK_DENIED", "INPUT_TOO_LARGE", "INPUT_UNREADABLE", "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "JSON_ROOT_INVALID", "SCHEMA_UNAVAILABLE"}
ABSTAIN = {"ROOT_ZONE_INCOMPLETE", "SURFACE_WINDOW_INCOMPLETE", "CRITICAL_PROPERTY_MISSING"}


class Result:
    def __init__(self, findings=()): self.findings = tuple(sorted(set(findings)))
    @property
    def ok(self): return not self.findings
    @property
    def outcome(self):
        codes = {x.code for x in self.findings}
        if not codes: return "PASS"
        if codes & ERROR: return "ERROR"
        return "ABSTAIN" if codes <= ABSTAIN else "DENY"
    def __eq__(self, other): return isinstance(other, Result) and self.findings == other.findings


class DuplicateKey(ValueError): pass
class NonFinite(ValueError): pass


def _pairs(items):
    out = {}
    for key, value in items:
        if key in out: raise DuplicateKey(key)
        out[key] = value
    return out


def _constant(_): raise NonFinite
def _float(value):
    out = float(value)
    if not math.isfinite(out): raise NonFinite
    return out


def _read(path):
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file(): return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > 1_048_576: return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_constant, parse_float=_float)
    except DuplicateKey: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFinite: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError, RecursionError, ValueError): return None, [Finding("INPUT_UNREADABLE", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("JSON_ROOT_INVALID", "/")])


def _ptr(path):
    parts = [str(x).replace("~", "~0").replace("/", "~1") for x in path]
    return "/" + "/".join(parts) if parts else "/"


def _schema(candidate):
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate), key=lambda e: _ptr(e.absolute_path))
        return [Finding("CANDIDATE_SCHEMA_INVALID", _ptr(e.absolute_path)) for e in errors[:50]]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def canonical_payload(candidate):
    body = {k: v for k, v in candidate.items() if k != "content_spec_hash"}
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def compute_content_spec_hash(candidate): return "sha256:" + hashlib.sha256(canonical_payload(candidate)).hexdigest()


def _num(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)): return None
    value = float(value)
    return value if math.isfinite(value) else None


def _close(a, b, tolerance):
    a, b = _num(a), _num(b)
    return a is not None and b is not None and abs(a - b) <= tolerance


def _avg(rows, field, start, end, tolerance):
    total = covered = 0.0
    for row in rows:
        top, bottom, value = _num(row.get("top_cm")), _num(row.get("bottom_cm")), _num(row.get(field))
        if None in (top, bottom, value): return None
        overlap = max(0.0, min(bottom, end) - max(top, start))
        total, covered = total + value * overlap, covered + overlap
    return total / covered if covered and abs(covered - (end - start)) <= tolerance else None


def validate_candidate(candidate):
    findings = _schema(candidate)
    add = lambda code, field: findings.append(Finding(code, field))
    aggregation = candidate.get("aggregation") if isinstance(candidate.get("aggregation"), dict) else {}
    tolerance = _num(aggregation.get("comparison_tolerance")) or 1e-6

    digest = candidate.get("content_spec_hash")
    if digest == "sha256:" + "0" * 64: add("DIGEST_PLACEHOLDER", "/content_spec_hash")
    try:
        if digest != compute_content_spec_hash(candidate): add("CONTENT_HASH_MISMATCH", "/content_spec_hash")
    except (TypeError, ValueError, OverflowError): add("CONTENT_HASH_MISMATCH", "/content_spec_hash")

    mukey = candidate.get("mukey")
    if isinstance(mukey, str) and candidate.get("record_id") != f"soil-mukey-properties:{mukey}": add("RECORD_ID_MISMATCH", "/record_id")
    source = candidate.get("source") if isinstance(candidate.get("source"), dict) else {}
    roles = {"nrcs_sda": "official_query", "nrcs_ssurgo": "official_static_survey"}
    if roles.get(source.get("source_family")) != source.get("source_role"): add("SOURCE_ROLE_MISMATCH", "/source/source_role")
    refs = candidate.get("evidence_refs")
    if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs) or refs != sorted(set(refs)): add("EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs")

    components = candidate.get("components") if isinstance(candidate.get("components"), list) else []
    cokeys, chkeys, component_total, weighted = set(), set(), 0.0, []
    for ci, component in enumerate(x for x in components if isinstance(x, dict)):
        cp, cokey = f"/components/{ci}", component.get("cokey")
        if isinstance(cokey, str):
            if cokey in cokeys: add("DUPLICATE_COKEY", cp + "/cokey")
            cokeys.add(cokey)
        pct = _num(component.get("component_pct"))
        if pct is not None: component_total += pct
        rows = [x for x in component.get("horizons", []) if isinstance(x, dict)]
        ordered = sorted(rows, key=lambda x: (_num(x.get("top_cm")) or 0, _num(x.get("bottom_cm")) or 0, str(x.get("chkey", ""))))
        if rows != ordered: add("HORIZONS_NOT_CANONICAL", cp + "/horizons")
        previous = None
        for hi, row in enumerate(ordered):
            hp, chkey = f"{cp}/horizons/{hi}", row.get("chkey")
            if isinstance(chkey, str):
                if chkey in chkeys: add("DUPLICATE_CHKEY", hp + "/chkey")
                chkeys.add(chkey)
            top, bottom = _num(row.get("top_cm")), _num(row.get("bottom_cm"))
            if top is None or bottom is None or top >= bottom: add("HORIZON_DEPTH_INVALID", hp)
            elif previous is not None:
                if top < previous - tolerance: add("HORIZON_OVERLAP", hp + "/top_cm")
                elif top > previous + tolerance: add("HORIZON_GAP", hp + "/top_cm")
            if bottom is not None: previous = bottom
            sand, clay = _num(row.get("sand_total_pct")), _num(row.get("clay_total_pct"))
            organic, ksat, awc = _num(row.get("organic_matter_pct")), _num(row.get("ksat_um_s")), _num(row.get("available_water_capacity_fraction"))
            if None in (sand, clay, organic, ksat, awc) or not (0 <= sand <= 100 and 0 <= clay <= 100 and sand + clay <= 100 + tolerance and 0 <= organic <= 20 and ksat > 0 and 0 <= awc <= 1): add("PHYSICAL_RANGE_INVALID", hp)
        if ordered:
            first, last = _num(ordered[0].get("top_cm")), _num(ordered[-1].get("bottom_cm"))
            if first is None or last is None or first > tolerance or last < 100 - tolerance: add("ROOT_ZONE_INCOMPLETE", cp + "/horizons")
            if first is None or last is None or first > tolerance or last < 5 - tolerance: add("SURFACE_WINDOW_INCOMPLETE", cp + "/horizons")
        metrics = {
            "root_zone_clay_pct": _avg(ordered, "clay_total_pct", 0, 100, tolerance),
            "root_zone_ksat_um_s": _avg(ordered, "ksat_um_s", 0, 100, tolerance),
            "root_zone_available_water_capacity_fraction": _avg(ordered, "available_water_capacity_fraction", 0, 100, tolerance),
            "surface_organic_matter_pct": _avg(ordered, "organic_matter_pct", 0, 5, tolerance),
        }
        if pct is not None and all(x is not None for x in metrics.values()): weighted.append((pct, metrics))
        elif ordered: add("CRITICAL_PROPERTY_MISSING", cp + "/horizons")

    minimum, maximum = _num(aggregation.get("component_percent_min_total")) or 99.0, _num(aggregation.get("component_percent_max_total")) or 101.0
    if not minimum - tolerance <= component_total <= maximum + tolerance: add("COMPONENT_PERCENT_CLOSURE", "/components")
    derived = candidate.get("derived") if isinstance(candidate.get("derived"), dict) else {}
    if not _close(derived.get("component_pct_total"), component_total, tolerance): add("COMPONENT_PERCENT_TOTAL_MISMATCH", "/derived/component_pct_total")
    if weighted and component_total > 0:
        for field in ("root_zone_clay_pct", "root_zone_ksat_um_s", "root_zone_available_water_capacity_fraction", "surface_organic_matter_pct"):
            expected = sum(weight * metrics[field] for weight, metrics in weighted) / component_total
            if not _close(derived.get(field), expected, tolerance): add("DERIVED_METRIC_MISMATCH", "/derived/" + field)

    hydric = candidate.get("hydric") if isinstance(candidate.get("hydric"), dict) else {}
    if hydric.get("status") == "CURRENT" and hydric.get("criteria_ref") is None: add("HYDRIC_CRITERIA_REQUIRED", "/hydric/criteria_ref")
    governance = candidate.get("governance") if isinstance(candidate.get("governance"), dict) else {}
    flags = ("source_activated", "evidence_resolution_claimed", "policy_evaluated", "promotion_authorized", "release_authorized", "publication_authorized")
    if candidate.get("public_use_requested") is not False: add("PUBLIC_USE_DENIED", "/public_use_requested")
    if governance.get("authority") != "NONE" or any(governance.get(x) is not False for x in flags) or governance.get("release_ref") is not None: add("CANDIDATE_GOVERNANCE_VIOLATION", "/governance")
    return Result(findings)


def validate_file(path):
    candidate, findings = _read(path)
    return Result(findings) if candidate is None else validate_candidate(candidate)


def _expected(path):
    sidecar = path.with_suffix(".expected_code.txt")
    try:
        return sidecar.read_text(encoding="utf-8").strip() if sidecar.is_file() and not sidecar.is_symlink() and sidecar.stat().st_size <= 128 else None
    except (OSError, UnicodeError): return None


def validate_fixture_tree(root=FIXTURE_ROOT):
    findings, valid, invalid = [], sorted((root / "valid").glob("*.json")), sorted((root / "invalid").glob("*.json"))
    if not valid: findings.append(Finding("VALID_FIXTURES_MISSING", "/valid"))
    if not invalid: findings.append(Finding("INVALID_FIXTURES_MISSING", "/invalid"))
    for path in valid:
        if not validate_file(path).ok: findings.append(Finding("VALID_FIXTURE_REJECTED", "/valid/" + path.name))
    for path in invalid:
        result, expected = validate_file(path), _expected(path)
        codes = {x.code for x in result.findings}
        if expected is None: findings.append(Finding("INVALID_EXPECTATION_MISSING", "/invalid/" + path.name))
        elif expected not in codes: findings.append(Finding("INVALID_EXPECTATION_NOT_MET", "/invalid/" + path.name))
        if result.ok: findings.append(Finding("INVALID_FIXTURE_ACCEPTED", "/invalid/" + path.name))
    return tuple(sorted(set(findings)))


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--fixture-root", type=Path, default=FIXTURE_ROOT)
    args = parser.parse_args(argv)
    if args.fixtures: result = Result(validate_fixture_tree(args.fixture_root))
    elif args.candidate is not None: result = validate_file(args.candidate)
    else: parser.error("provide --candidate or --fixtures")
    print(json.dumps({
        "scope": SCOPE, "outcome": result.outcome,
        "findings": [{"code": x.code, "field": x.field} for x in result.findings],
        "authority": "NONE", "non_effects": ["no_source_activation", "no_evidence_resolution", "no_policy_evaluation", "no_promotion_release_or_publication", "no_public_use"],
    }, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__": raise SystemExit(main())
