"""Shared model and deterministic fixture construction for ProgramOutcomeChain.

This module creates no source, evidence, policy, review, causation, release,
publication, or public-use authority.
"""
from __future__ import annotations

import copy
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/governance/program_outcome_chain.schema.json"
CASES = ROOT / "fixtures/contracts/v1/governance/program_outcome_chain/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "program-outcome-chain-fixture-only-v1"

STAGE_ORDER = {
    "PROGRAM_VERSION": 0,
    "ELIGIBILITY_AREA": 1,
    "APPLICATION_WINDOW": 2,
    "APPLICATION": 3,
    "ADMINISTRATIVE_REVIEW": 4,
    "TECHNICAL_REVIEW": 5,
    "RECOMMENDATION": 6,
    "AWARD": 7,
    "AGREEMENT": 8,
    "PROJECT": 9,
    "PROJECT_FOOTPRINT": 10,
    "PAYMENT": 11,
    "MILESTONE": 12,
    "COMPLETION": 13,
    "OUTCOME_OBSERVATION": 14,
    "EVALUATION": 15,
}
REPEATABLE_STAGE_TYPES = {"PAYMENT", "MILESTONE", "OUTCOME_OBSERVATION"}
EXPECTED_CLAIM_CODES = {
    "PROGRAM_VERSION": "PROGRAM_VERSION_EXISTS",
    "ELIGIBILITY_AREA": "AREA_ELIGIBLE_NOT_FUNDED",
    "APPLICATION_WINDOW": "APPLICATION_WINDOW_ONLY",
    "APPLICATION": "APPLICATION_EXISTS_NOT_APPROVED",
    "ADMINISTRATIVE_REVIEW": "ADMIN_REVIEW_NOT_AWARD",
    "TECHNICAL_REVIEW": "TECHNICAL_REVIEW_NOT_AWARD",
    "RECOMMENDATION": "RECOMMENDATION_NOT_DECISION",
    "AWARD": "AWARD_NOT_IMPLEMENTATION_OR_PAYMENT",
    "AGREEMENT": "AGREEMENT_NOT_COMPLETION",
    "PROJECT": "PROJECT_STATE_ONLY",
    "PROJECT_FOOTPRINT": "FOOTPRINT_SCOPE_ONLY",
    "PAYMENT": "PAYMENT_NOT_COMPLETION",
    "MILESTONE": "MILESTONE_NOT_PROJECT_COMPLETION",
    "COMPLETION": "COMPLETION_FOR_AGREED_SCOPE",
    "OUTCOME_OBSERVATION": "OUTCOME_OBSERVED_NOT_CAUSAL",
    "EVALUATION": "EVALUATION_BOUNDED_NOT_UNIVERSAL_CAUSATION",
}
ALLOWED_STAGE_STATUSES = {
    "PROGRAM_VERSION": {"ASSERTED"},
    "ELIGIBILITY_AREA": {"ASSERTED"},
    "APPLICATION_WINDOW": {"OPEN", "CLOSED", "CANCELLED"},
    "APPLICATION": {"RECEIVED", "WITHDRAWN"},
    "ADMINISTRATIVE_REVIEW": {"UNDER_REVIEW", "COMPLETED"},
    "TECHNICAL_REVIEW": {"UNDER_REVIEW", "COMPLETED"},
    "RECOMMENDATION": {"RECOMMENDED", "WITHDRAWN"},
    "AWARD": {"AWARDED", "CANCELLED"},
    "AGREEMENT": {"EXECUTED", "CANCELLED"},
    "PROJECT": {"PLANNED", "ACTIVE", "COMPLETED", "CANCELLED"},
    "PROJECT_FOOTPRINT": {"ASSERTED"},
    "PAYMENT": {"DISBURSED"},
    "MILESTONE": {"COMPLETED"},
    "COMPLETION": {"ACCEPTED"},
    "OUTCOME_OBSERVATION": {"OBSERVED"},
    "EVALUATION": {"EVALUATED"},
}
DEFAULT_STAGE_STATUS = {
    "PROGRAM_VERSION": "ASSERTED",
    "ELIGIBILITY_AREA": "ASSERTED",
    "APPLICATION_WINDOW": "OPEN",
    "APPLICATION": "RECEIVED",
    "ADMINISTRATIVE_REVIEW": "COMPLETED",
    "TECHNICAL_REVIEW": "COMPLETED",
    "RECOMMENDATION": "RECOMMENDED",
    "AWARD": "AWARDED",
    "AGREEMENT": "EXECUTED",
    "PROJECT": "ACTIVE",
    "PROJECT_FOOTPRINT": "ASSERTED",
    "PAYMENT": "DISBURSED",
    "MILESTONE": "COMPLETED",
    "COMPLETION": "ACCEPTED",
    "OUTCOME_OBSERVATION": "OBSERVED",
    "EVALUATION": "EVALUATED",
}
REQUIRED_PREDECESSOR_TYPES = {
    "PROGRAM_VERSION": (),
    "ELIGIBILITY_AREA": ("PROGRAM_VERSION",),
    "APPLICATION_WINDOW": ("PROGRAM_VERSION",),
    "APPLICATION": ("ELIGIBILITY_AREA", "APPLICATION_WINDOW"),
    "ADMINISTRATIVE_REVIEW": ("APPLICATION",),
    "TECHNICAL_REVIEW": ("ADMINISTRATIVE_REVIEW",),
    "RECOMMENDATION": ("TECHNICAL_REVIEW",),
    "AWARD": ("RECOMMENDATION",),
    "AGREEMENT": ("AWARD",),
    "PROJECT": ("AGREEMENT",),
    "PROJECT_FOOTPRINT": ("PROJECT",),
    "PAYMENT": ("PROJECT",),
    "MILESTONE": ("PROJECT",),
    "COMPLETION": ("PROJECT",),
    "OUTCOME_OBSERVATION": ("COMPLETION",),
    "EVALUATION": ("OUTCOME_OBSERVATION",),
}
FALSE_EFFECTS = {
    "source_activated": False,
    "evidence_resolved": False,
    "policy_evaluated": False,
    "review_approved": False,
    "causation_established": False,
    "promoted": False,
    "released": False,
    "published": False,
}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
    "PROGRAM_OUTCOME_CHAIN_ID_MISMATCH",
    "FIXTURE_MANIFEST_INVALID",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("program_outcome_chain_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_chain_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "program-outcome-chain:" + digest[:24]


def assign_identity(candidate: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(candidate)
    result["spec_hash"] = canonical_spec_hash(result)
    result["program_outcome_chain_id"] = expected_chain_id(result)
    return result


def aware_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def canonical_string_array(values: Any) -> bool:
    return (
        isinstance(values, list)
        and all(isinstance(value, str) for value in values)
        and values == sorted(set(values))
    )


def _fixture_hex(seed: str) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash({"fixture_seed": seed}).removeprefix("sha256:")


def build_fixture_base(recipe: Mapping[str, Any]) -> dict[str, Any]:
    stage_types = recipe.get("stage_types")
    if (
        not isinstance(stage_types, list)
        or len(stage_types) < 2
        or not all(
            isinstance(item, str) and item in STAGE_ORDER
            for item in stage_types
        )
    ):
        raise ValueError("invalid fixture stage recipe")

    stages: list[dict[str, Any]] = []
    seen_types: dict[str, list[str]] = {}
    for index, stage_type in enumerate(stage_types):
        stage_id = (
            "program-stage:"
            + _fixture_hex(f"stage:{stage_type}:{index}")[:24]
        )
        dependencies: list[str] = []
        for required_type in REQUIRED_PREDECESSOR_TYPES[stage_type]:
            prior = seen_types.get(required_type, [])
            if prior:
                dependencies.append(prior[-1])

        amount: dict[str, Any] | None = None
        if stage_type == "AWARD":
            amount = {"value": 1000000, "currency": "USD"}
        elif stage_type == "PAYMENT":
            amount = {"value": 250000, "currency": "USD"}

        geometry_ref = None
        if stage_type == "ELIGIBILITY_AREA":
            geometry_ref = "kfm:geometry:synthetic-eligibility"
        elif stage_type == "PROJECT_FOOTPRINT":
            geometry_ref = "kfm:geometry:synthetic-project-footprint"

        method_ref = (
            "kfm:method:synthetic-monitoring"
            if stage_type in {"OUTCOME_OBSERVATION", "EVALUATION"}
            else None
        )
        uncertainty_ref = (
            "kfm:uncertainty:synthetic-evaluation"
            if stage_type == "EVALUATION"
            else None
        )
        stage = {
            "stage_id": stage_id,
            "stage_type": stage_type,
            "stage_status": DEFAULT_STAGE_STATUS[stage_type],
            "native_ref": (
                f"kfm:program-native:{stage_type.lower()}:{index}"
            ),
            "recorded_at": f"2026-01-{index + 1:02d}T00:00:00Z",
            "depends_on": sorted(dependencies),
            "evidence_refs": sorted(
                [
                    "kfm:evidence-ref:"
                    + _fixture_hex(
                        f"stage-evidence:{stage_type}:{index}:a"
                    ),
                    "kfm:evidence-ref:"
                    + _fixture_hex(
                        f"stage-evidence:{stage_type}:{index}:b"
                    ),
                ]
            ),
            "public_claim_code": EXPECTED_CLAIM_CODES[stage_type],
            "amount": amount,
            "geometry_ref": geometry_ref,
            "method_ref": method_ref,
            "uncertainty_ref": uncertainty_ref,
        }
        stages.append(stage)
        seen_types.setdefault(stage_type, []).append(stage_id)

    candidate = {
        "profile": "kfm.governance.program-outcome-chain.v1",
        "status": "PROPOSED_INACTIVE",
        "program_outcome_chain_id": "program-outcome-chain:" + "0" * 24,
        "version": "1.0.0",
        "spec_hash": "sha256:" + "0" * 64,
        "source_ref": "kfm:source:synthetic-program-authority",
        "source_native_program_id": "synthetic-program-v1",
        "issuing_authority_ref": "kfm:authority:synthetic",
        "temporal_authority_ref": (
            "kfm:temporal-authority:synthetic-program-v1"
        ),
        "source_snapshot_refs": [
            "kfm:source-snapshot:" + _fixture_hex("program-snapshot")
        ],
        "evidence_refs": sorted(
            [
                "kfm:evidence-ref:"
                + _fixture_hex("program-evidence:a"),
                "kfm:evidence-ref:"
                + _fixture_hex("program-evidence:b"),
            ]
        ),
        "stages": stages,
        "lineage": {
            "state": "CURRENT",
            "corrects": [],
            "superseded_by": [],
            "conflict_refs": [],
        },
        "release_state": "UNRELEASED",
        "release_ref": None,
        "limitations": sorted(
            [
                "Fixture-only candidate; no real program or funding claim.",
                (
                    "Observation and evaluation references are synthetic "
                    "and non-causal."
                ),
            ]
        ),
        "public_use_allowed": False,
        "effects": copy.deepcopy(FALSE_EFFECTS),
    }
    return assign_identity(candidate)
