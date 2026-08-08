"""Deterministic candidate builder for the current RuntimeResponseEnvelope profile.

The helper performs only local, schema-confirmed checks. It does not resolve
EvidenceRef objects, evaluate policy, calculate source freshness or precision,
mutate correction state, authorize a release, or create a public response.
Callers must supply every authority-bearing value explicitly and must still run
the repository's authoritative JSON Schema and semantic validation at the trust
boundary.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime
import re
from typing import Final


OUTCOMES: Final[frozenset[str]] = frozenset(
    {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
)
EVIDENCE_KINDS: Final[frozenset[str]] = frozenset(
    {"measurement", "record", "dataset", "artifact"}
)
SPATIAL_REPRESENTATIONS: Final[frozenset[str]] = frozenset(
    {"point", "line", "polygon", "grid", "raster", "aggregate", "none"}
)
FRESHNESS_CLASSES: Final[frozenset[str]] = frozenset(
    {"current", "stale-accepted", "historical", "unknown"}
)
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_SPEC_HASH_RE: Final[re.Pattern[str]] = re.compile(r"^sha256:[a-f0-9]{64}$")
_RECEIPT_REF_RE: Final[re.Pattern[str]] = re.compile(
    r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$"
)
_ALLOWED_EVIDENCE_FIELDS: Final[frozenset[str]] = frozenset(
    {"ref", "kind", "bundle_ref"}
)
_PRECISION_REQUIRED_FIELDS: Final[frozenset[str]] = frozenset(
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


def _require_exact_fields(
    value: object,
    *,
    field: str,
    required: frozenset[str],
    optional: frozenset[str] = frozenset(),
) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise EnvelopeBuildError("FIELD_NOT_OBJECT", field)
    keys = set(value)
    if not required.issubset(keys):
        raise EnvelopeBuildError("FIELD_REQUIRED_MISSING", field)
    if keys - required - optional:
        raise EnvelopeBuildError("FIELD_ADDITIONAL", field)
    return value


def _normalize_evidence_refs(
    evidence_refs: object,
    *,
    field_name: str = "evidence_refs",
) -> list[dict[str, str]]:
    if isinstance(evidence_refs, (str, bytes, bytearray)) or not isinstance(
        evidence_refs, Sequence
    ):
        raise EnvelopeBuildError("EVIDENCE_REFS_NOT_ARRAY", field_name)

    normalized: list[dict[str, str]] = []
    seen: set[tuple[str, str, str | None]] = set()
    for index, item in enumerate(evidence_refs):
        field = f"{field_name}[{index}]"
        if not isinstance(item, Mapping):
            raise EnvelopeBuildError("EVIDENCE_REF_NOT_OBJECT", field)

        keys = set(item)
        if not {"ref", "kind"}.issubset(keys):
            raise EnvelopeBuildError("EVIDENCE_REF_REQUIRED_FIELD_MISSING", field)
        if extras := keys - _ALLOWED_EVIDENCE_FIELDS:
            raise EnvelopeBuildError(
                "EVIDENCE_REF_ADDITIONAL_FIELD", f"{field}[{len(extras)}]"
            )

        ref = _require_nonempty_string(item.get("ref"), f"{field}.ref")
        kind = _require_nonempty_string(item.get("kind"), f"{field}.kind")
        if kind not in EVIDENCE_KINDS:
            raise EnvelopeBuildError("EVIDENCE_REF_KIND_INVALID", f"{field}.kind")

        bundle_ref: str | None = None
        normalized_item = {"ref": ref, "kind": kind}
        if "bundle_ref" in item:
            bundle_ref = _require_nonempty_string(
                item.get("bundle_ref"), f"{field}.bundle_ref"
            )
            normalized_item["bundle_ref"] = bundle_ref

        identity = (ref, kind, bundle_ref)
        if identity in seen:
            raise EnvelopeBuildError("EVIDENCE_REF_DUPLICATE", field)
        seen.add(identity)
        normalized.append(normalized_item)

    return normalized


def _evidence_identity(value: Mapping[str, object]) -> tuple[str, str, str | None]:
    bundle_ref = value.get("bundle_ref")
    return (
        str(value["ref"]),
        str(value["kind"]),
        str(bundle_ref) if bundle_ref is not None else None,
    )


def _normalize_string_array(value: object, field: str) -> list[str]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        raise EnvelopeBuildError("FIELD_NOT_ARRAY", field)
    normalized: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(value):
        candidate = _require_nonempty_string(item, f"{field}[{index}]")
        if candidate in seen:
            raise EnvelopeBuildError("FIELD_DUPLICATE", f"{field}[{index}]")
        seen.add(candidate)
        normalized.append(candidate)
    return normalized


def _normalize_precision(
    value: object,
    *,
    top_level_evidence_refs: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    precision = _require_exact_fields(
        value,
        field="precision_actually_used",
        required=_PRECISION_REQUIRED_FIELDS,
        optional=_PRECISION_OPTIONAL_FIELDS,
    )

    spatial = _require_exact_fields(
        precision.get("spatial"),
        field="precision_actually_used.spatial",
        required=frozenset(
            {"representation", "resolution", "accuracy", "generalization_applied"}
        ),
    )
    representation = _require_nonempty_string(
        spatial.get("representation"),
        "precision_actually_used.spatial.representation",
    )
    if representation not in SPATIAL_REPRESENTATIONS:
        raise EnvelopeBuildError(
            "PRECISION_SPATIAL_REPRESENTATION_INVALID",
            "precision_actually_used.spatial.representation",
        )
    generalization_applied = spatial.get("generalization_applied")
    if not isinstance(generalization_applied, bool):
        raise EnvelopeBuildError(
            "PRECISION_GENERALIZATION_FLAG_INVALID",
            "precision_actually_used.spatial.generalization_applied",
        )
    normalized_spatial: dict[str, object] = {
        "representation": representation,
        "resolution": _require_nonempty_string(
            spatial.get("resolution"),
            "precision_actually_used.spatial.resolution",
        ),
        "accuracy": _require_nonempty_string(
            spatial.get("accuracy"),
            "precision_actually_used.spatial.accuracy",
        ),
        "generalization_applied": generalization_applied,
    }

    temporal = _require_exact_fields(
        precision.get("temporal"),
        field="precision_actually_used.temporal",
        required=frozenset(
            {"granularity", "observation_interval", "freshness_class"}
        ),
    )
    interval = _require_exact_fields(
        temporal.get("observation_interval"),
        field="precision_actually_used.temporal.observation_interval",
        required=frozenset({"start", "end"}),
    )
    start = _require_aware_datetime(
        interval.get("start"),
        "precision_actually_used.temporal.observation_interval.start",
    )
    end = _require_aware_datetime(
        interval.get("end"),
        "precision_actually_used.temporal.observation_interval.end",
    )
    if datetime.fromisoformat(start.replace("Z", "+00:00")) > datetime.fromisoformat(
        end.replace("Z", "+00:00")
    ):
        raise EnvelopeBuildError(
            "PRECISION_INTERVAL_INVERTED",
            "precision_actually_used.temporal.observation_interval",
        )
    freshness_class = _require_nonempty_string(
        temporal.get("freshness_class"),
        "precision_actually_used.temporal.freshness_class",
    )
    if freshness_class not in FRESHNESS_CLASSES:
        raise EnvelopeBuildError(
            "PRECISION_FRESHNESS_CLASS_INVALID",
            "precision_actually_used.temporal.freshness_class",
        )
    normalized_temporal: dict[str, object] = {
        "granularity": _require_nonempty_string(
            temporal.get("granularity"),
            "precision_actually_used.temporal.granularity",
        ),
        "observation_interval": {"start": start, "end": end},
        "freshness_class": freshness_class,
    }

    attribute = _require_exact_fields(
        precision.get("attribute"),
        field="precision_actually_used.attribute",
        required=frozenset(
            {
                "measure",
                "unit",
                "significant_precision",
                "classification_granularity",
            }
        ),
    )
    significant_precision = attribute.get("significant_precision")
    if type(significant_precision) is not int or not 0 <= significant_precision <= 12:
        raise EnvelopeBuildError(
            "PRECISION_SIGNIFICANT_PRECISION_INVALID",
            "precision_actually_used.attribute.significant_precision",
        )
    classification_granularity = attribute.get("classification_granularity")
    if classification_granularity is not None:
        classification_granularity = _require_nonempty_string(
            classification_granularity,
            "precision_actually_used.attribute.classification_granularity",
        )
    normalized_attribute: dict[str, object] = {
        "measure": _require_nonempty_string(
            attribute.get("measure"),
            "precision_actually_used.attribute.measure",
        ),
        "unit": _require_nonempty_string(
            attribute.get("unit"),
            "precision_actually_used.attribute.unit",
        ),
        "significant_precision": significant_precision,
        "classification_granularity": classification_granularity,
    }

    precision_refs = _normalize_evidence_refs(
        precision.get("evidence_refs"),
        field_name="precision_actually_used.evidence_refs",
    )
    if not precision_refs:
        raise EnvelopeBuildError(
            "PRECISION_EVIDENCE_REQUIRED",
            "precision_actually_used.evidence_refs",
        )
    top_identities = {_evidence_identity(item) for item in top_level_evidence_refs}
    if any(_evidence_identity(item) not in top_identities for item in precision_refs):
        raise EnvelopeBuildError(
            "PRECISION_EVIDENCE_NOT_TOP_LEVEL",
            "precision_actually_used.evidence_refs",
        )

    transform_refs = _normalize_string_array(
        precision.get("transform_receipt_refs"),
        "precision_actually_used.transform_receipt_refs",
    )
    if any(_RECEIPT_REF_RE.fullmatch(item) is None for item in transform_refs):
        raise EnvelopeBuildError(
            "PRECISION_TRANSFORM_REF_INVALID",
            "precision_actually_used.transform_receipt_refs",
        )
    if generalization_applied and not transform_refs:
        raise EnvelopeBuildError(
            "PRECISION_GENERALIZATION_RECEIPT_REQUIRED",
            "precision_actually_used.transform_receipt_refs",
        )

    normalized: dict[str, object] = {
        "spatial": normalized_spatial,
        "temporal": normalized_temporal,
        "attribute": normalized_attribute,
        "evidence_refs": precision_refs,
        "transform_receipt_refs": transform_refs,
    }
    if "requested_precision" in precision:
        requested = _require_exact_fields(
            precision.get("requested_precision"),
            field="precision_actually_used.requested_precision",
            required=frozenset(),
            optional=frozenset({"spatial", "temporal", "attribute"}),
        )
        if not requested:
            raise EnvelopeBuildError(
                "PRECISION_REQUESTED_EMPTY",
                "precision_actually_used.requested_precision",
            )
        normalized["requested_precision"] = {
            key: _require_nonempty_string(
                requested.get(key),
                f"precision_actually_used.requested_precision.{key}",
            )
            for key in ("spatial", "temporal", "attribute")
            if key in requested
        }
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

    `ANSWER` requires an evidence-bound multidimensional precision disclosure.
    Other finite outcomes reject that field. Successful construction means only
    that the local checks in this module passed; it does not establish evidence
    sufficiency, policy allow, release state, publication safety, or complete
    schema validity.
    """

    checked_outcome = _require_nonempty_string(outcome, "outcome")
    if checked_outcome not in OUTCOMES:
        raise EnvelopeBuildError("OUTCOME_INVALID", "outcome")

    normalized_evidence_refs = _normalize_evidence_refs(evidence_refs)
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
        if not normalized_evidence_refs:
            raise EnvelopeBuildError("ANSWER_EVIDENCE_REQUIRED", "evidence_refs")
        if precision_actually_used is None:
            raise EnvelopeBuildError(
                "PRECISION_REQUIRED",
                "precision_actually_used",
            )
        candidate["precision_actually_used"] = _normalize_precision(
            precision_actually_used,
            top_level_evidence_refs=normalized_evidence_refs,
        )
    elif precision_actually_used is not None:
        raise EnvelopeBuildError(
            "PRECISION_FORBIDDEN",
            "precision_actually_used",
        )

    return candidate


__all__ = [
    "EVIDENCE_KINDS",
    "FRESHNESS_CLASSES",
    "OUTCOMES",
    "SPATIAL_REPRESENTATIONS",
    "EnvelopeBuildError",
    "build_runtime_response_candidate",
]
