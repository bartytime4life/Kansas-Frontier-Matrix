"""Deterministic candidate builder for the current RuntimeResponseEnvelope profile.

The helper performs only local, schema-confirmed checks. It does not resolve
EvidenceRef objects, evaluate policy, calculate source freshness, mutate
correction state, authorize a release, or create a public response. Callers must
supply every authority-bearing value explicitly and must still run the
repository's authoritative JSON Schema validation at the trust boundary.
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
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_SPEC_HASH_RE: Final[re.Pattern[str]] = re.compile(r"^sha256:[a-f0-9]{64}$")
_ALLOWED_EVIDENCE_FIELDS: Final[frozenset[str]] = frozenset(
    {"ref", "kind", "bundle_ref"}
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
) -> list[dict[str, str]]:
    if isinstance(evidence_refs, (str, bytes, bytearray)) or not isinstance(
        evidence_refs, Sequence
    ):
        raise EnvelopeBuildError("EVIDENCE_REFS_NOT_ARRAY", "evidence_refs")

    normalized: list[dict[str, str]] = []
    seen: set[tuple[str, str, str | None]] = set()
    for index, item in enumerate(evidence_refs):
        field = f"evidence_refs[{index}]"
        if not isinstance(item, Mapping):
            raise EnvelopeBuildError("EVIDENCE_REF_NOT_OBJECT", field)

        keys = set(item)
        if not {"ref", "kind"}.issubset(keys):
            raise EnvelopeBuildError("EVIDENCE_REF_REQUIRED_FIELD_MISSING", field)
        if extras := keys - _ALLOWED_EVIDENCE_FIELDS:
            # Do not include attacker-controlled key names in the outward error.
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

    return {
        "id": _require_pattern(response_id, "id", _ID_RE),
        "spec_hash": _require_pattern(spec_hash, "spec_hash", _SPEC_HASH_RE),
        "version": _require_nonempty_string(version, "version"),
        "issued_at": _require_aware_datetime(issued_at, "issued_at"),
        "outcome": checked_outcome,
        "reason_code": _require_nonempty_string(reason_code, "reason_code"),
        "evidence_refs": _normalize_evidence_refs(evidence_refs),
        "policy_state": _require_nonempty_string(policy_state, "policy_state"),
        "freshness": _require_nonempty_string(freshness, "freshness"),
        "correction_state": _require_nonempty_string(
            correction_state, "correction_state"
        ),
    }


__all__ = [
    "EVIDENCE_KINDS",
    "OUTCOMES",
    "EnvelopeBuildError",
    "build_runtime_response_candidate",
]
