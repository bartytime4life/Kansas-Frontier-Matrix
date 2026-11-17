#!/usr/bin/env python3
"""Rehearse synthetic drought observation/forecast boundaries for #3390.

Uses existing WesternKansasObservationAssessment and ForecastProduct semantics.
This fixture runner accepts no live input or store and grants no source,
evidence, policy, review, release or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.local_data.file_io import read_regular
from tools.validators import validate_forecast_product as forecast
from tools.validators.evidence import validate_western_kansas_observation_assessment as observation

FIXTURES = ROOT / "fixtures/domains/hydrology/western_kansas_observation_assessment/multiclock"
PROFILE = "kfm.synthetic-drought-multiclock/v1"
FILES = ("bindings.json", "observations.json", "forecast.json", "correction.json")
CLAIMS = {
    "USDM": "DROUGHT_CLASSIFICATION", "USGS_STREAMFLOW": "STREAMFLOW_CONDITION",
    "KGS_GROUNDWATER": "GROUNDWATER_CONDITION", "PRECIP_EDDI": "EVAPORATIVE_DEMAND",
    "SOIL_MOISTURE": "SOIL_MOISTURE_CONDITION", "AGRICULTURE_CONTEXT": "AGRICULTURE_CONTEXT",
    "WATER_MANAGEMENT_BOUNDARY": "MANAGEMENT_BOUNDARY_CONTEXT",
}
GOVERNANCE = dict.fromkeys(("source_admitted", "lifecycle_mutated", "policy_approved",
                            "release_authorized", "publication_authorized"), False)


class RehearsalError(ValueError):
    """A static code, without source values, paths or exception details."""


def require(condition, code):
    if not condition:
        raise RehearsalError(code)


def canonical(value):
    """Fixture comparison bytes, not a new object-family identity algorithm."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(data):
    return "sha256:" + hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def reject_constant(_value):
    raise RehearsalError("NONFINITE_JSON")


def finite_float(value):
    number = float(value)
    require(math.isfinite(number), "NONFINITE_JSON")
    return number


def instant(value):
    require(isinstance(value, str) and re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value),
        "EXPLICIT_TIME_REQUIRED")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise RehearsalError("EXPLICIT_TIME_REQUIRED") from None
    return parsed


def load_inputs(root):
    raw, objects = {}, {}
    for name in FILES:
        raw[name] = read_regular(root / name, 256 * 1024)
        objects[name] = json.loads(raw[name], object_pairs_hook=unique_object,
                                   parse_constant=reject_constant, parse_float=finite_float)
        require(isinstance(objects[name], dict), "FIXTURE_OBJECT_REQUIRED")
    return raw, objects


def candidate(sources, analysis_time, *, kind=None, outcome="OBSERVED", prior=None, **claim_changes):
    sources = copy.deepcopy(sources)
    source = sources[0]
    claim = {"kind": kind or CLAIMS[source["source_family"]],
             "support_kind": source["support_kind"], "support_id": source["support_id"],
             "transformation_ref": None, "source_conflict": False, "county_intersection_only": False,
             "resampled": False, "source_support_preserved": True,
             "tuple_evidence_refs": sorted(item["evidence_ref"] for item in sources)}
    claim.update(claim_changes)
    current = digest(canonical({"sources": sources, "claim": claim}))
    return {"profile": observation.PROFILE, "analysis_time": analysis_time, "max_age_days": 30,
            "sources": sources, "claim": claim, "outcome": outcome,
            "material_change": {"prior_claim_digest": prior, "current_claim_digest": current,
                                "declared_material": prior is not None and prior != current},
            "governance": dict(GOVERNANCE)}


def observation_case(results, name, value, outcome, reasons=()):
    require(value["material_change"]["current_claim_digest"] == digest(canonical(
        {"sources": value["sources"], "claim": value["claim"]})), "CLAIM_DIGEST_BINDING_MISMATCH")
    actual = observation.assess(value)
    require((actual.outcome, actual.reason_codes) == (outcome, tuple(reasons)), "OBSERVATION_POLARITY_MISMATCH")
    results[name] = {"outcome": actual.outcome, "reason_codes": list(actual.reason_codes),
                     "tuple_evidence_refs": value["claim"]["tuple_evidence_refs"],
                     "claim_digest": value["material_change"]["current_claim_digest"]}


def forecast_case(results, name, value, outcome, reasons=()):
    actual = forecast.validate_payload(value)
    codes = tuple(item.code for item in actual.findings)
    require((actual.outcome, codes) == (outcome, tuple(reasons)), "FORECAST_POLARITY_MISMATCH")
    results[name] = {"outcome": actual.outcome, "reason_codes": list(codes)}


def rehearse(root=FIXTURES):
    raw, objects = load_inputs(root)
    original = canonical(objects)
    bindings, old, predicted, corrected = (objects[name] for name in FILES)
    require(set(bindings) == {"profile", "synthetic", "predecessor_evaluated_at", "successor_evaluated_at",
                              "input_sha256", "successor_relation", "source_corrected_at", "uncertainty_by_source"},
            "BINDINGS_INVALID")
    require(bindings["profile"] == PROFILE and bindings["synthetic"] is True, "SYNTHETIC_FIXTURE_REQUIRED")
    require(bindings["input_sha256"] == {name: digest(raw[name]) for name in FILES[1:]}, "INPUT_BINDING_MISMATCH")
    require(bindings["successor_relation"] == "SUCCESSOR_FORECAST_CONTEXT_ONLY", "FORECAST_IS_NOT_OBSERVATION_CORRECTION")
    before_time, after_time = bindings["predecessor_evaluated_at"], bindings["successor_evaluated_at"]
    require(instant(before_time) < instant(after_time), "CHECKPOINT_ORDER_INVALID")
    require(set(old) == {"synthetic", "sources"} and old["synthetic"] is True, "SYNTHETIC_FIXTURE_REQUIRED")
    sources = old["sources"]
    require(isinstance(sources, list) and len(sources) == len(CLAIMS), "SEVEN_FAMILIES_REQUIRED")
    by_family = {item["source_family"]: item for item in sources}
    require(set(by_family) == set(CLAIMS), "SEVEN_FAMILIES_REQUIRED")
    for field in ("source_id", "source_version_ref", "evidence_ref"):
        require(len({item[field] for item in sources}) == len(sources)
                and all("synthetic" in item[field] for item in sources), "SOURCE_IDENTITY_COLLAPSE")
    uncertainty = {item["evidence_ref"]: {"status": "NOT_PROVIDED", "value": None} for item in sources}
    require(canonical(bindings["uncertainty_by_source"]) == canonical(uncertainty), "UNCERTAINTY_OVERCLAIM")

    results = {}
    for family, source in sorted(by_family.items()):
        observation_case(results, "observed_" + family.lower(), candidate([source], before_time), "OBSERVED")
        require(len({instant(source[key]) for key in ("observation_start", "observation_end", "valid_start",
                                                     "valid_end", "publication_time", "retrieval_time")}) == 6,
                "OBSERVATION_CLOCKS_COLLAPSED")
        require(instant(source["observation_end"]) < instant(source["publication_time"])
                < instant(source["retrieval_time"]) <= instant(before_time), "OBSERVATION_CLOCKS_COLLAPSED")

    forecast_case(results, "successor_forecast", predicted, "PASS")
    require("synthetic" in predicted["source_native_id"], "SYNTHETIC_FORECAST_REQUIRED")
    times = predicted["times"]
    require(len({instant(times[key]) for key in ("source_data_cutoff_at", "issued_at", "valid_from",
                                                "valid_to", "retrieved_at")}) == 5, "FORECAST_CLOCKS_COLLAPSED")
    require(instant(before_time) < instant(times["issued_at"]) < instant(times["retrieved_at"]) <= instant(after_time)
            and instant(times["valid_to"]) > instant(after_time), "SUCCESSOR_CLOCKS_INVALID")
    require(predicted["uncertainty"] == {"kind": "NOT_PROVIDED", "value_ref": None, "confidence": "UNKNOWN"}
            and predicted["lineage"] == {"state": "CURRENT", "corrects": [], "superseded_by": [], "conflict_refs": []},
            "FORECAST_CONTEXT_OVERCLAIM")

    flow, soil, eddi = (by_family[key] for key in ("USGS_STREAMFLOW", "SOIL_MOISTURE", "PRECIP_EDDI"))
    joined = candidate([soil, eddi], before_time, kind="CROSS_SOURCE_STRESS", outcome="DERIVED",
                       support_kind="BASIN", support_id="synthetic-review-envelope",
                       transformation_ref="transform:synthetic:support-preserving-context-v1")
    observation_case(results, "derived_context", joined, "DERIVED")
    conflict = candidate([soil, eddi], before_time, outcome="CONFLICT",
                         **{**joined["claim"], "source_conflict": True, "kind": "CROSS_SOURCE_STRESS"})
    observation_case(results, "conflict_no_winner", conflict, "CONFLICT", ("SOURCE_CONFLICT",))
    recent = copy.deepcopy(flow)
    recent.update(publication_time=times["issued_at"], retrieval_time=times["retrieved_at"])
    stale = candidate([recent], after_time, outcome="STALE")
    stale["max_age_days"] = 7
    observation_case(results, "recent_publication_old_observation", stale, "STALE", ("OBSERVATION_STALE",))
    missing = copy.deepcopy(flow)
    missing["observation_status"] = "MISSING"
    observation_case(results, "missing_not_zero", candidate([missing], before_time, outcome="ABSTAIN"),
                     "ABSTAIN", ("MISSING_OBSERVATION",))

    preserved = ("source_family", "source_id", "observation_start", "observation_end", "valid_start", "valid_end",
                 "support_kind", "support_id", "crs", "resolution_m", "method", "unit")
    require(all(corrected[key] == flow[key] for key in preserved), "CORRECTION_SUPPORT_OR_CLOCK_CHANGED")
    require(corrected["revision_status"] == "CORRECTED" and corrected["supersedes_ref"] == flow["source_version_ref"]
            and corrected["correction_ref"] == "correction:synthetic:flow-v2"
            and corrected["source_version_ref"] != flow["source_version_ref"]
            and corrected["payload_digest"] != flow["payload_digest"]
            and corrected["evidence_ref"] != flow["evidence_ref"], "CORRECTION_BINDING_INVALID")
    require(instant(flow["retrieval_time"]) < instant(bindings["source_corrected_at"])
            < instant(corrected["publication_time"]) < instant(corrected["retrieval_time"]) <= instant(after_time),
            "CORRECTION_CLOCKS_INVALID")
    prior = candidate([flow], before_time)["material_change"]["current_claim_digest"]
    observation_case(results, "corrected_observation", candidate([corrected], after_time, prior=prior), "OBSERVED")
    superseded = copy.deepcopy(corrected)
    superseded["revision_status"] = "SUPERSEDED"
    observation_case(results, "superseded_not_current", candidate([superseded], after_time, outcome="ABSTAIN"),
                     "ABSTAIN", ("SOURCE_SUPERSEDED",))

    for name, source, kind, code in (
        ("usdm_groundwater", by_family["USDM"], "GROUNDWATER_CONDITION", "USDM_CANNOT_PROVE_GROUNDWATER"),
        ("flow_groundwater", flow, "GROUNDWATER_CONDITION", "STREAMFLOW_CANNOT_PROVE_GROUNDWATER"),
        ("soil_crop_loss", soil, "AGRICULTURAL_LOSS", "CONTEXT_CANNOT_PROVE_AGRICULTURAL_LOSS"),
        ("eddi_crop_loss", eddi, "AGRICULTURAL_LOSS", "CONTEXT_CANNOT_PROVE_AGRICULTURAL_LOSS"),
        ("boundary_condition", by_family["WATER_MANAGEMENT_BOUNDARY"], "GROUNDWATER_CONDITION", "BOUNDARY_CANNOT_PROVE_CONDITION"),
    ):
        observation_case(results, name, candidate([source], before_time, kind=kind, outcome="ABSTAIN"), "ABSTAIN", (code,))
    observation_case(results, "county_not_uniform", candidate([by_family["USDM"]], before_time, outcome="ABSTAIN",
                     support_kind="COUNTY", county_intersection_only=True), "ABSTAIN", ("COUNTY_INTERSECTION_NOT_UNIFORM",))
    erased = candidate([soil, eddi], before_time, outcome="ERROR",
                       **{**joined["claim"], "resampled": True, "source_support_preserved": False})
    observation_case(results, "support_erasure", erased, "ERROR", ("SOURCE_SUPPORT_ERASURE_DENIED",))
    omitted = candidate([soil, eddi], before_time, outcome="ERROR",
                        **{**joined["claim"], "tuple_evidence_refs": [soil["evidence_ref"]]})
    observation_case(results, "missing_tuple_evidence", omitted, "ERROR", ("TUPLE_EVIDENCE_INCOMPLETE",))
    causal = candidate([soil, eddi], before_time, outcome="ERROR",
                       **{**joined["claim"], "causal_attribution": True})
    observation_case(results, "causal_attribution", causal, "ERROR", ("SCHEMA_INVALID",))
    for name, section, field, value, code in (
        ("forecast_as_observation", None, "source_role", "OBSERVATION", "SOURCE_ROLE_COLLAPSE"),
        ("prediction_as_measurement", None, "support_type", "DIRECT_MEASUREMENT", "SUPPORT_TYPE_COLLAPSE"),
        ("unknown_confidence_not_high", "uncertainty", "confidence", "HIGH", "UNCERTAINTY_CONFIDENCE_OVERCLAIM"),
        ("cutoff_not_issuance", "times", "source_data_cutoff_at", times["retrieved_at"], "DATA_CUTOFF_AFTER_ISSUANCE"),
    ):
        changed = copy.deepcopy(predicted)
        (changed if section is None else changed[section])[field] = value
        forecast_case(results, name, forecast.assign_identity(changed), "DENY", (code,))

    require(canonical(objects) == original, "REPLAY_MUTATED_INPUT")
    require(all(read_regular(root / name, 256 * 1024) == data for name, data in raw.items()), "FIXTURE_BYTES_CHANGED")
    report = {"profile": PROFILE, "outcome": "PASS", "scope": "SYNTHETIC_FIXTURE_REHEARSAL_ONLY",
              "input_sha256": {name: digest(data) for name, data in sorted(raw.items())},
              "schema_sha256": {path.relative_to(ROOT).as_posix(): digest(read_regular(path, 1024 * 1024))
                                for path in (observation.SCHEMA_PATH, forecast.SCHEMA)},
              "consumer_sha256": {path: digest(read_regular(ROOT / path, 1024 * 1024)) for path in (
                  "tools/validators/evidence/rehearse_drought_multiclock.py",
                  "tools/validators/evidence/validate_western_kansas_observation_assessment.py",
                  "tools/validators/validate_forecast_product.py")},
              "predecessor_evaluated_at": before_time, "successor_evaluated_at": after_time,
              "predecessor_bytes_unchanged": True, "successor_relation": bindings["successor_relation"],
              "forecast": {"id": predicted["forecast_product_id"], "source_role": predicted["source_role"],
                           "support_type": predicted["support_type"], "times": times, "uncertainty": predicted["uncertainty"]},
              "family_matrix": [{"source_family": family, "source": by_family[family],
                                  "uncertainty": uncertainty[by_family[family]["evidence_ref"]],
                                  "live_authority": "NOT_ASSESSED", "live_cadence": "NOT_ASSESSED", "rights": "UNKNOWN"}
                                 for family in sorted(by_family)],
              "correction": {"source_corrected_at": bindings["source_corrected_at"], "source": corrected,
                             "prior_claim_digest": prior, "uncertainty": {"status": "NOT_PROVIDED", "value": None}},
              "cases": dict(sorted(results.items())),
              "remaining": ["LIVE_SEVEN_FAMILY_AUTHORITY_CADENCE_RIGHTS", "QUANTITATIVE_UNCERTAINTY_PROPAGATION",
                            "REAL_EVIDENCE_CLOSURE", "AUTHENTICATED_API_UI_AI_REPLAY", "INDEPENDENT_ACCEPTANCE"],
              "authority": {**GOVERNANCE, "review": False, "production_write": False, "public_use": False}}
    report["report_sha256"] = digest(canonical(report))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", action="store_true", required=True)
    parser.parse_args(argv)
    try:
        report = rehearse()
    except RehearsalError as exc:
        report = {"profile": PROFILE, "outcome": "FAIL", "reason_code": str(exc)}
    except (OSError, ValueError, TypeError, KeyError, IndexError, RecursionError, RuntimeError):
        report = {"profile": PROFILE, "outcome": "ERROR", "reason_code": "FIXTURE_REHEARSAL_UNAVAILABLE"}
    print(json.dumps(report, sort_keys=True))
    return {"PASS": 0, "FAIL": 1, "ERROR": 2}[report["outcome"]]


if __name__ == "__main__":
    raise SystemExit(main())
