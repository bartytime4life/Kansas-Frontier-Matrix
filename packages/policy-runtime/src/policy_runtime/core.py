"""Fail-closed serving preconditions for owner-controlled water release records.

The caller must obtain a decision from trusted storage, never from a package,
URL or request body. This is a narrow serving gate, not a general policy engine.
"""
import re
from connectors_core.captured_json import utc_time

REQUIRED_REFS = ("source_admission_ref", "rights_ref", "sensitivity_ref", "policy_ref", "review_ref", "release_ref")
DECISION_KEYS = {"profile", "package_id", "decision", "reviewed_at", "released_at", "expires_at", "correction_state", "correction_ref", "reviewer", "releaser", *REQUIRED_REFS}
REF = re.compile(r"^kfm://[A-Za-z0-9._~:/-]{1,240}$")
# ADR-0044: licenses of admitted public sources whose owner may review and
# release the same package. Must match apps/site/source/app/governed-water.ts.
SELF_RELEASE_LICENSES = frozenset({
    "U.S. Public Domain (USGS-authored data, 17 U.S.C. 105); provisional data subject to revision",
})


def _self_release_eligible(evidence: dict) -> bool:
    entries = evidence["entries"]
    return bool(entries) and all(entry["bundle"]["sensitivity"]["level"] == "public"
                                 and entry["bundle"]["rights"]["license"] in SELF_RELEASE_LICENSES
                                 for entry in entries)


def serving_gate(manifest: dict, evidence: dict, decision: dict | None, *, now: str) -> str:
    if decision is None:
        return "REVIEW_REQUIRED"
    if not isinstance(decision, dict) or set(decision) != DECISION_KEYS:
        return "RELEASE_METADATA_INVALID"
    if decision["profile"] != "kfm.water-release-decision/v1" or decision["package_id"] != manifest["package_id"]:
        return "RELEASE_BINDING_MISMATCH"
    if decision["correction_state"] != "ACTIVE":
        return "CORRECTION_HOLD"
    if decision["correction_ref"] is not None or decision["decision"] != "APPROVED":
        return "RELEASE_NOT_APPROVED"
    if any(not isinstance(decision[k], str) or not REF.fullmatch(decision[k]) for k in REQUIRED_REFS):
        return "REVIEW_REFERENCE_MISSING"
    if any(not isinstance(decision[k], str) or not 1 <= len(decision[k]) <= 128 for k in ("reviewer", "releaser")):
        return "INDEPENDENT_REVIEW_REQUIRED"
    if decision["reviewer"] == decision["releaser"] and not _self_release_eligible(evidence):
        return "INDEPENDENT_REVIEW_REQUIRED"
    try:
        if not utc_time(manifest["created_at"]) <= utc_time(decision["reviewed_at"]) <= utc_time(decision["released_at"]) <= utc_time(now) < utc_time(decision["expires_at"]):
            return "RELEASE_TIME_INVALID"
    except (ValueError, TypeError):
        return "RELEASE_TIME_INVALID"
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        if bundle["sensitivity"]["level"] != "public" or "review required" in bundle["rights"]["license"].lower():
            return "RIGHTS_OR_SENSITIVITY_HOLD"
    return "ELIGIBLE"
