"""Deterministic candidate builder for the current RuntimeResponseEnvelope profile.

The helper performs only local, schema-confirmed checks. It does not resolve
EvidenceRef objects, evaluate policy, calculate source freshness, mutate
correction state, authorize a release, or create a public response. Callers must
supply every authority-bearing value explicitly and must still run the
repository's authoritative JSON Schema validation at the trust boundary.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from copy import deepcopy
from datetime import datetime
import re
from typing import Final


OUTCOMES: Final[frozenset[str]] = frozenset(
    {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
)
EVIDENCE_KINDS: Final[frozenset[str]] = frozenset(
    {"measurement", "record", "dataset", "artifact"}
)
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_SPEC_HASH_RE: Final[re.Pattern[str]] = re.compile(r"^sha256:[a-f0-9]{64}$")
_RECEIPT_REF_RE: Final[re.Pattern[str]] = re.compile(
    r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$"
)
_ALLOWED_EVIDENCE_FIELDS: Final[frozenset[str]] = frozenset(
    {"ref", "kind", "bundle_ref"}
)
_PRECISION_FIELDS: Final[frozenset[str]] = frozenset(
    {
        "spatial",
        "temporal",
        "attribute",
        "evidence_refs",
        "transform_receipt_refs",
    }
)
_PRECISION_OPTIONAL_FIELDS: Final[frozenset[str]] = frozenset(
    {"requested_precision"}
)


class EnvelopeBuildError(ValueError):
    """Safe, deterministic rejection of a locally invalid envelope candidate."""

    def __init__(self, code: str, field: str) -> None:
        self.code = code
        self.field = field
        super().__init__(f"{code}:{field}")


def _require_nonempty_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EnvelopeBuildError("FIELD_INVALID", field)
    return value


def _require_pattern(
    value: object,
    field: str,
    pattern: re.Pattern[str],
) -> str:
    candidate = _require_nonempty_string(value, field)
    if pattern.fullmatch(candidate) is None:
        raise EnvelopeBuildError("FIELD_PATTERN_INVALID", field)
    return candidate


def _require_aware_datetime(value: object, field: str) -> str:
    candidate = _require_nonempty_string(value, field)
    try:
        parsed = datetime.fromisoformat(candidate.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EnvelopeBuildError("DATETIME_INVALID", field) from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise EnvelopeBuildError("DATETIME_NOT_OFFSET_AWARE", field)
    return candidate


def _normalize_evidence_refs(
    evidence_refs: object,
    *,
    field: str = "evidence_refs",
) -> list[dict[str, str]]:
    if isinstance(evidence_refs, (str, bytes, bytearray)) or not isinstance(
        evidence_refs, Sequence
    ):
        raise EnvelopeBuildError("EVIDENCE_REFS_NOT_ARRAY", field)
    if len(evidence_refs) > 128:
        raise EnvelopeBuildError("EVIDENCE_REFS_TOO_MANY", field)

    normalized: list[dict[str, str]] = []
    seen: set[tuple[str, str, str | None]] = set()
    for index, item in enumerate(evidence_refs):
        item_field = f"{field}[{index}]"
        if not isinstance(item, Mapping):
            raise EnvelopeBuildError("EVIDENCE_REF_NOT_OBJECT", item_field)

        keys = set(item)
        if not {"ref", "kind"}.issubset(keys):
            raise EnvelopeBuildError(
                "EVIDENCE_REF_REQUIRED_FIELD_MISSING", item_field
            )
        if extras := keys - _ALLOWED_EVIDENCE_FIELDS:
            # Do not include attacker-controlled key names in the outward error.
            raise EnvelopeBuildError(
                "EVIDENCE_REF_ADDITIONAL_FIELD", f"{item_field}[{len(extras)}]"
            )

        ref = _require_nonempty_string(item.get("ref"), f"{item_field}.ref")
        kind = _require_nonempty_string(item.get("kind"), f"{item_field}.kind")
        if kind not in EVIDENCE_KINDS:
            raise EnvelopeBuildError(
                "EVIDENCE_REF_KIND_INVALID", f"{item_field}.kind"
            )

        bundle_ref: str | None = None
        normalized_item = {"ref": ref, "kind": kind}
        if "bundle_ref" in item:
            bundle_ref = _require_nonempty_string(
                item.get("bundle_ref"), f"{item_field}.bundle_ref"
            )
            normalized_item["bundle_ref"] = bundle_ref

        identity = (ref, kind, bundle_ref)
        if identity in seen:
            raise EnvelopeBuildError("EVIDENCE_REF_DUPLICATE", item_field)
        seen.add(identity)
        normalized.append(normalized_item)

    return normalized


def _evidence_identity(value: Mapping[str, str]) -> tuple[str, str, str | None]:
    return (value["ref"], value["kind"], value.get("bundle_ref"))


def _normalize_precision(
    value: object,
    *,
    top_level_evidence_refs: Sequence[Mapping[str, str]],
) -> dict[str, object]:
    field = "precision_actually_used"
    if not isinstance(value, Mapping):
        raise EnvelopeBuildError("PRECISION_NOT_OBJECT", field)
    keys = set(value)
    if not _PRECISION_FIELDS.issubset(keys):
        raise EnvelopeBuildError("PRECISION_REQUIRED_FIELD_MISSING", field)
    if extras := keys - _PRECISION_FIELDS - _PRECISION_OPTIONAL_FIELDS:
        raise EnvelopeBuildError(
            "PRECISION_ADDITIONAL_FIELD", f"{field}[{len(extras)}]"
        )

    precision_evidence = _normalize_evidence_refs(
        value["evidence_refs"], field=f"{field}.evidence_refs"
    )
    if not precision_evidence:
        raise EnvelopeBuildError(
            "PRECISION_EVIDENCE_REFS_REQUIRED", f"{field}.evidence_refs"
        )
    top_level_identities = {
        _evidence_identity(item) for item in top_level_evidence_refs
    }
    if any(
        _evidence_identity(item) not in top_level_identities
        for item in precision_evidence
    ):
        raise EnvelopeBuildError(
            "PRECISION_EVIDENCE_NOT_TOP_LEVEL", f"{field}.evidence_refs"
        )

    receipt_refs = value["transform_receipt_refs"]
    if isinstance(receipt_refs, (str, bytes, bytearray)) or not isinstance(
        receipt_refs, Sequence
    ):
        raise EnvelopeBuildError(
            "PRECISION_RECEIPT_REFS_NOT_ARRAY", f"{field}.transform_receipt_refs"
        )
    if len(receipt_refs) > 128:
        raise EnvelopeBuildError(
            "PRECISION_RECEIPT_REFS_TOO_MANY", f"{field}.transform_receipt_refs"
        )
    normalized_receipts: list[str] = []
    seen_receipts: set[str] = set()
    for index, item in enumerate(receipt_refs):
        item_field = f"{field}.transform_receipt_refs[{index}]"
        ref = _require_pattern(item, item_field, _RECEIPT_REF_RE)
        if len(ref) > 640:
            raise EnvelopeBuildError("FIELD_TOO_LONG", item_field)
        if ref in seen_receipts:
            raise EnvelopeBuildError("PRECISION_RECEIPT_REF_DUPLICATE", item_field)
        seen_receipts.add(ref)
        normalized_receipts.append(ref)

    spatial = value["spatial"]
    if not isinstance(spatial, Mapping):
        raise EnvelopeBuildError("PRECISION_SPATIAL_NOT_OBJECT", f"{field}.spatial")
    if spatial.get("generalization_applied") is True and not normalized_receipts:
        raise EnvelopeBuildError(
            "PRECISION_GENERALIZATION_RECEIPT_REQUIRED",
            f"{field}.transform_receipt_refs",
        )

    temporal = value["temporal"]
    if not isinstance(temporal, Mapping):
        raise EnvelopeBuildError("PRECISION_TEMPORAL_NOT_OBJECT", f"{field}.temporal")
    interval = temporal.get("observation_interval")
    if isinstance(interval, Mapping) and {"start", "end"}.issubset(interval):
        start = _require_aware_datetime(
            interval["start"], f"{field}.temporal.observation_interval.start"
        )
        end = _require_aware_datetime(
            interval["end"], f"{field}.temporal.observation_interval.end"
        )
        start_instant = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_instant = datetime.fromisoformat(end.replace("Z", "+00:00"))
        if start_instant > end_instant:
            raise EnvelopeBuildError(
                "PRECISION_INTERVAL_INVERTED",
                f"{field}.temporal.observation_interval",
            )

    normalized = deepcopy(dict(value))
    normalized["evidence_refs"] = precision_evidence
    normalized["transform_receipt_refs"] = normalized_receipts
    return normalized


def build_runtime_response_candidate(
    *,
    response_id: str,
    spec_hash: str,
    version: str,
    issued_at: str,
    outcome: str,
    reason_code: str,
    evidence_refs: Sequence[Mapping[str, object]],
    policy_state: str,
    freshness: str,
    correction_state: str,
    precision_actually_used: Mapping[str, object] | None = None,
) -> dict[str, object]:
    """Build one closed RuntimeResponseEnvelope candidate from explicit inputs.

    The return value contains exactly the fields in the current paired schema.
    Successful construction means only that the local checks in this module
    passed; it does not establish evidence sufficiency, policy allow, release
    state, publication safety, or complete schema validity.
    """

    checked_outcome = _require_nonempty_string(outcome, "outcome")
    if checked_outcome not in OUTCOMES:
        raise EnvelopeBuildError("OUTCOME_INVALID", "outcome")

    normalized_evidence_refs = _normalize_evidence_refs(evidence_refs)
    if checked_outcome == "ANSWER" and not normalized_evidence_refs:
        raise EnvelopeBuildError(
            "ANSWER_EVIDENCE_REFS_REQUIRED", "evidence_refs"
        )
    if checked_outcome == "ANSWER" and precision_actually_used is None:
        raise EnvelopeBuildError(
            "ANSWER_PRECISION_REQUIRED", "precision_actually_used"
        )
    if checked_outcome != "ANSWER" and precision_actually_used is not None:
        raise EnvelopeBuildError(
            "NEGATIVE_OUTCOME_PRECISION_FORBIDDEN", "precision_actually_used"
        )

    candidate: dict[str, object] = {
        "id": _require_pattern(response_id, "id", _ID_RE),
        "spec_hash": _require_pattern(spec_hash, "spec_hash", _SPEC_HASH_RE),
        "version": _require_nonempty_string(version, "version"),
        "issued_at": _require_aware_datetime(issued_at, "issued_at"),
        "outcome": checked_outcome,
        "reason_code": _require_nonempty_string(reason_code, "reason_code"),
        "evidence_refs": normalized_evidence_refs,
        "policy_state": _require_nonempty_string(policy_state, "policy_state"),
        "freshness": _require_nonempty_string(freshness, "freshness"),
        "correction_state": _require_nonempty_string(
            correction_state, "correction_state"
        ),
    }
    if checked_outcome == "ANSWER":
        candidate["precision_actually_used"] = _normalize_precision(
            precision_actually_used,
            top_level_evidence_refs=normalized_evidence_refs,
        )
    return candidate


__all__ = [
    "EVIDENCE_KINDS",
    "OUTCOMES",
    "EnvelopeBuildError",
    "build_runtime_response_candidate",
]
