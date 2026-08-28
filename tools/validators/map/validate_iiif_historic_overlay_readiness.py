#!/usr/bin/env python3
"""Deterministic, fixture-only IIIF historic-overlay readiness preflight."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/iiif_historic_overlay_readiness.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/iiif_historic_overlay_readiness/cases.json"
MAX_FILE_BYTES = 1_048_576
SCOPE = "iiif-historic-overlay-fixture-readiness-only"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    reasons: tuple[str, ...]
    findings: tuple[Finding, ...] = ()


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise DuplicateKeyError(key)
        out[key] = value
    return out


def _nonfinite(_: str) -> None: raise NonFiniteNumberError

def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[Any | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink(): return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file(): return None, (Finding("FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_FILE_BYTES: return None, (Finding("FILE_TOO_LARGE", "/"),)
        with path.open("r", encoding="utf-8") as stream:
            return json.load(stream, object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_float), ()
    except UnicodeDecodeError: return None, (Finding("JSON_NOT_UTF8", "/"),)
    except DuplicateKeyError: return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError: return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except json.JSONDecodeError: return None, (Finding("JSON_INVALID", "/"),)
    except OSError: return None, (Finding("FILE_READ_ERROR", "/"),)
    except (RecursionError, ValueError): return None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),)


def _pointer(parts: Sequence[object]) -> str:
    values = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(values) if values else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(candidate), key=lambda e: (_pointer(tuple(e.absolute_path)), str(e.validator)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("SCHEMA_UNAVAILABLE", "/"),)
    return tuple(Finding("SCHEMA_INVALID", _pointer(tuple(error.absolute_path))) for error in errors[:100])


def _map(value: Any) -> Mapping[str, Any]: return value if isinstance(value, Mapping) else {}
def _list(value: Any) -> list[Any]: return value if isinstance(value, list) else []
def _annotation_digest(payload: str) -> str: return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _mask_closed(mask: Any) -> bool:
    points = _list(mask)
    if len(points) < 4 or points[0] != points[-1]: return False
    seen: set[tuple[float, float]] = set()
    for point in points[:-1]:
        if not isinstance(point, list) or len(point) != 2: return False
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(float(v)) for v in point): return False
        seen.add((float(point[0]), float(point[1])))
    return len(seen) >= 3


def derive_decision(candidate: Mapping[str, Any]) -> tuple[str, tuple[str, ...], tuple[Finding, ...]]:
    source = _map(candidate.get("source")); raw = _map(candidate.get("raw_capture")); overlay = _map(candidate.get("overlay"))
    rights = _map(candidate.get("rights")); care = _map(candidate.get("care")); renderer = _map(candidate.get("renderer")); public = _map(candidate.get("public_boundary"))

    errors: list[str] = []; findings: list[Finding] = []
    payload, declared = raw.get("annotation_payload_utf8"), raw.get("annotation_digest")
    if isinstance(payload, str) and isinstance(declared, str) and _annotation_digest(payload) != declared:
        errors.append("ANNOTATION_DIGEST_MISMATCH"); findings.append(Finding("ANNOTATION_DIGEST_MISMATCH", "/raw_capture/annotation_digest"))
    gcps = _list(overlay.get("gcps"))
    count = overlay.get("gcp_count")
    if isinstance(count, int) and not isinstance(count, bool) and count != len(gcps):
        errors.append("GCP_COUNT_MISMATCH"); findings.append(Finding("GCP_COUNT_MISMATCH", "/overlay/gcp_count"))
    if overlay.get("georeference_present") is True and not _mask_closed(overlay.get("resource_mask")):
        errors.append("RESOURCE_MASK_INVALID"); findings.append(Finding("RESOURCE_MASK_INVALID", "/overlay/resource_mask"))
    if errors: return "ERROR", tuple(sorted(set(errors))), tuple(sorted(set(findings)))

    deny: list[str] = []
    if public.get("raw_route_exposed") is True: deny.append("RAW_ROUTE_EXPOSED")
    if public.get("unreleased_fetch_allowed") is True: deny.append("UNRELEASED_FETCH_ALLOWED")
    if rights.get("kfm_rights_state") == "DENIED": deny.append("RIGHTS_DENIED")
    if care.get("state") == "DENIED": deny.append("CARE_DENIED")
    if _list(care.get("authority_to_control")) and not care.get("consent_grant_ref"): deny.append("CARE_CONSENT_MISSING")
    if renderer.get("plugin_required") is True and renderer.get("allowlisted") is not True: deny.append("PLUGIN_NOT_ALLOWLISTED")
    if deny: return "DENY", tuple(sorted(set(deny))), ()

    hold: list[str] = []
    if source.get("presentation_api_version") == "4.0-preview": hold.append("PREVIEW_API_NOT_ADOPTED")
    if (source.get("presentation_api_version") == "2.1.1" or source.get("image_api_version") == "2.1.1") and not source.get("legacy_normalization_ref"):
        hold.append("LEGACY_NORMALIZATION_REQUIRED")
    if source.get("freshness") == "STALE": hold.append("SOURCE_STALE")
    elif source.get("freshness") == "UNKNOWN": hold.append("SOURCE_FRESHNESS_UNKNOWN")
    if raw.get("bytes_preserved") is not True or raw.get("capture_metadata_present") is not True: hold.append("RAW_CAPTURE_INCOMPLETE")
    if overlay.get("georeference_present") is not True: hold.append("GEOREFERENCE_REQUIRED")
    else:
        if overlay.get("gcp_count") == 0: hold.append("GCP_REQUIRED")
        if not overlay.get("transform_method"): hold.append("TRANSFORM_METHOD_REQUIRED")
        if not overlay.get("overlay_uncertainty"): hold.append("OVERLAY_UNCERTAINTY_REQUIRED")
    if rights.get("kfm_rights_state") == "UNKNOWN" or rights.get("rights_uri") is None: hold.append("RIGHTS_UNKNOWN")
    if rights.get("rights_propagated") is not True: hold.append("RIGHTS_PROPAGATION_REQUIRED")
    if care.get("state") in {"UNKNOWN", "REVIEW_REQUIRED"}: hold.append("CARE_REVIEW_REQUIRED")
    if renderer.get("plugin_required") is True and not renderer.get("plugin_version"): hold.append("PLUGIN_VERSION_REQUIRED")
    if not public.get("evidence_bundle_ref"): hold.append("EVIDENCE_BUNDLE_REQUIRED")
    if not public.get("rollback_target_ref"): hold.append("ROLLBACK_TARGET_REQUIRED")
    if hold: return "HOLD", tuple(sorted(set(hold))), ()
    return "READY", ("IIIF_HISTORIC_OVERLAY_READY",), ()


def validate_candidate(candidate: Any) -> ValidationResult:
    if not isinstance(candidate, Mapping): return ValidationResult("ERROR", ("ROOT_NOT_OBJECT",), (Finding("ROOT_NOT_OBJECT", "/"),))
    findings = _schema_findings(candidate)
    if findings: return ValidationResult("ERROR", ("SCHEMA_INVALID",), findings)
    outcome, reasons, semantic = derive_decision(candidate)
    decision = _map(candidate.get("decision"))
    if decision.get("outcome") != outcome or decision.get("reasons") != list(reasons):
        mismatch = Finding("DECISION_MISMATCH", "/decision")
        return ValidationResult("ERROR", ("DECISION_MISMATCH",), tuple(sorted(set(semantic + (mismatch,)))))
    return ValidationResult(outcome, reasons, semantic)


def _parts(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"): raise ValueError("invalid JSON pointer")
    return [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")] if pointer != "/" else []


def _mutate(candidate: dict[str, Any], mutation: Mapping[str, Any]) -> None:
    parts = _parts(mutation.get("path")); target: Any = candidate
    if not parts: raise ValueError("root mutation denied")
    for part in parts[:-1]:
        if not isinstance(target, dict) or part not in target: raise ValueError("missing mutation path")
        target = target[part]
    leaf = parts[-1]
    if not isinstance(target, dict): raise ValueError("mutation target not object")
    if mutation.get("op") == "set": target[leaf] = copy.deepcopy(mutation.get("value"))
    elif mutation.get("op") == "delete" and leaf in target: del target[leaf]
    else: raise ValueError("unsupported mutation")


def materialize_fixture_case(manifest: Mapping[str, Any], entry: Mapping[str, Any]) -> dict[str, Any]:
    base, mutations = manifest.get("base_candidate"), entry.get("mutations")
    if not isinstance(base, dict) or not isinstance(mutations, list): raise ValueError("invalid fixture case")
    candidate = copy.deepcopy(base)
    for mutation in mutations:
        if not isinstance(mutation, Mapping): raise ValueError("invalid mutation")
        _mutate(candidate, mutation)
    return candidate


def validate_fixtures() -> int:
    value, findings = _read(FIXTURE_PATH)
    if findings or not isinstance(value, dict) or not isinstance(value.get("base_candidate"), dict) or not isinstance(value.get("cases"), list) or not value["cases"]:
        print("ERROR: IIIF readiness fixture manifest is unavailable or invalid."); return 1
    failed = False; seen: set[str] = set(); outcomes: set[str] = set()
    for entry in value["cases"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("case_id"), str) or entry["case_id"] in seen or not isinstance(entry.get("expected"), dict): failed = True; continue
        seen.add(entry["case_id"])
        try: candidate = materialize_fixture_case(value, entry)
        except (TypeError, ValueError, RecursionError): failed = True; continue
        result = validate_candidate(candidate); actual = {"outcome": result.outcome, "reasons": list(result.reasons)}
        print(json.dumps({"case_id": entry["case_id"], **actual}, sort_keys=True, separators=(",", ":")))
        failed = failed or actual != entry["expected"]; outcomes.add(result.outcome)
    if outcomes != {"READY", "HOLD", "DENY", "ERROR"}: failed = True
    if failed: return 1
    print(f"CONFIRMED: {len(value['cases'])} IIIF historic-overlay readiness cases passed exact polarity."); return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only IIIF historic-overlay readiness.")
    parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files: parser.error("provide candidate files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda p: p.as_posix()):
        value, findings = _read(path)
        result = ValidationResult("ERROR", tuple(sorted({f.code for f in findings})), findings) if findings else validate_candidate(value)
        print(json.dumps({"file": path.name, "outcome": result.outcome, "reasons": list(result.reasons), "scope": SCOPE}, sort_keys=True, separators=(",", ":")))
        failed = failed or result.outcome != "READY"
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
