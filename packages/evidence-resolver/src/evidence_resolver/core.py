"""Pure, bounded EvidenceRef-to-EvidenceBundle candidate evaluation.

This module deliberately evaluates only an explicit internal alpha profile.  It
does not read a registry, evidence store, policy engine, release store, clock,
environment, or network.  ``RESOLVED`` means that the supplied candidate passed
the checks named in the result; it is never a public ANSWER, evidence truth,
policy clearance, review, release approval, or publication authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
import math
import re
from typing import Mapping


PROFILE = "kfm/evidence-ref-bundle-candidate/v1alpha1"
MAX_INPUT_BYTES = 131_072
MAX_DEPTH = 20
MAX_COLLECTION_ITEMS = 128
MAX_STRING_LENGTH = 4_096
MAX_NUMBER_TOKEN_LENGTH = 128
_MAX_ABS_INTEGER = 10**MAX_NUMBER_TOKEN_LENGTH

_DIGEST = re.compile(r"^sha256:[a-f0-9]{64}$")
_BUNDLE_ID = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_RFC3339 = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})$"
)
_REF_KINDS = frozenset({"measurement", "record", "dataset", "artifact"})
_POLICY_OUTCOMES = frozenset({"ANSWER", "ABSTAIN", "DENY", "ERROR"})
_CORRECTION_STATES = frozenset(
    {"ACTIVE", "SUPERSEDED", "WITHDRAWN", "UNKNOWN"}
)
_LIMITATIONS = (
    "claim_scope_not_machine_checked",
    "citations_rights_and_sensitivity_not_decided",
    "policy_is_caller_supplied_not_evaluated",
    "no_review_release_runtime_or_publication_authority",
)


class BoundedJSONError(ValueError):
    """Raised when serialized input violates deterministic parser bounds."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


class CandidateInputError(ValueError):
    """Raised for a safe, profile-local input failure."""

    def __init__(self, code: str, field: str | None = None) -> None:
        super().__init__(code)
        self.code = code
        self.field = field


@dataclass(frozen=True, order=True)
class ResolutionIssue:
    """Safe issue carrier containing only governed codes and field labels."""

    code: str
    field: str | None = None

    def as_dict(self) -> dict[str, str]:
        payload = {"code": self.code}
        if self.field is not None:
            payload["field"] = self.field
        return payload


@dataclass(frozen=True)
class ResolutionCandidate:
    """Non-authoritative result for the internal candidate profile."""

    profile: str
    status: str
    bundle_id: str | None
    checks_performed: tuple[str, ...]
    issues: tuple[ResolutionIssue, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "profile": self.profile,
            "status": self.status,
            "authoritative": False,
            "bundle_id": self.bundle_id if self.status == "RESOLVED" else None,
            "checks_performed": list(self.checks_performed),
            "issues": [issue.as_dict() for issue in self.issues],
            "limitations": list(_LIMITATIONS),
        }


def _reject_constant(_: str) -> None:
    raise BoundedJSONError("input/non-finite-number")


def _parse_bounded_int(value: str) -> int:
    if len(value.lstrip("-")) > MAX_NUMBER_TOKEN_LENGTH:
        raise BoundedJSONError("input/number-too-large")
    return int(value)


def _parse_finite_float(value: str) -> float:
    if len(value.lstrip("-")) > MAX_NUMBER_TOKEN_LENGTH:
        raise BoundedJSONError("input/number-too-large")
    parsed = float(value)
    if not math.isfinite(parsed):
        raise BoundedJSONError("input/non-finite-number")
    return parsed


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise BoundedJSONError("input/duplicate-key")
        result[key] = value
    return result


def _walk_bounds(value: object, *, depth: int = 0) -> None:
    if depth > MAX_DEPTH:
        raise BoundedJSONError("input/max-depth")
    if isinstance(value, str):
        if len(value) > MAX_STRING_LENGTH:
            raise BoundedJSONError("input/string-too-long")
        return
    if isinstance(value, bool) or value is None:
        return
    if isinstance(value, int):
        # Compare numerically to avoid converting an attacker-controlled huge
        # integer back to a string.
        if abs(value) >= _MAX_ABS_INTEGER:
            raise BoundedJSONError("input/number-too-large")
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise BoundedJSONError("input/non-finite-number")
        return
    if isinstance(value, Mapping):
        if len(value) > MAX_COLLECTION_ITEMS:
            raise BoundedJSONError("input/collection-too-large")
        for key, item in value.items():
            if not isinstance(key, str):
                raise BoundedJSONError("input/non-string-key")
            _walk_bounds(key, depth=depth + 1)
            _walk_bounds(item, depth=depth + 1)
        return
    if isinstance(value, list):
        if len(value) > MAX_COLLECTION_ITEMS:
            raise BoundedJSONError("input/collection-too-large")
        for item in value:
            _walk_bounds(item, depth=depth + 1)


def loads_bounded(data: bytes | str) -> object:
    """Parse JSON with byte, duplicate-key, depth, and collection bounds."""

    try:
        raw = data if isinstance(data, bytes) else data.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise BoundedJSONError("input/not-utf8") from exc
    if len(raw) > MAX_INPUT_BYTES:
        raise BoundedJSONError("input/too-large")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BoundedJSONError("input/not-utf8") from exc
    try:
        parsed = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_constant,
            parse_int=_parse_bounded_int,
            parse_float=_parse_finite_float,
        )
    except BoundedJSONError:
        raise
    except (json.JSONDecodeError, OverflowError, RecursionError, ValueError) as exc:
        raise BoundedJSONError("input/malformed-json") from exc
    _walk_bounds(parsed)
    return parsed


def _mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise CandidateInputError("input/not-object", field)
    return value


def _closed(
    value: object,
    *,
    allowed: frozenset[str],
    required: frozenset[str],
    field: str,
) -> Mapping[str, object]:
    item = _mapping(value, field=field)
    keys = set(item)
    if not required.issubset(keys):
        raise CandidateInputError("input/missing-field", field)
    if not keys.issubset(allowed):
        # Never echo attacker-controlled field names into diagnostics.
        raise CandidateInputError("profile/mixed-fields", field)
    return item


def _string(value: object, *, field: str, nullable: bool = False) -> str | None:
    if value is None and nullable:
        return None
    if not isinstance(value, str) or not value or len(value) > MAX_STRING_LENGTH:
        raise CandidateInputError("input/invalid-string", field)
    return value


def _string_list(
    value: object, *, field: str, allow_empty: bool = False
) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise CandidateInputError("input/invalid-array", field)
    if (not allow_empty and not value) or len(value) > MAX_COLLECTION_ITEMS:
        raise CandidateInputError("input/invalid-array", field)
    return tuple(_string(item, field=field) or "" for item in value)


def _validate_evidence_ref(value: object) -> dict[str, str]:
    ref = _closed(
        value,
        allowed=frozenset({"ref", "kind", "bundle_ref"}),
        required=frozenset({"ref", "kind"}),
        field="evidence_ref",
    )
    ref_value = _string(ref["ref"], field="evidence_ref")
    kind = _string(ref["kind"], field="evidence_ref")
    if kind not in _REF_KINDS:
        raise CandidateInputError("schema/evidence-ref-invalid", "evidence_ref")
    result = {"ref": ref_value or "", "kind": kind or ""}
    if "bundle_ref" in ref:
        result["bundle_ref"] = _string(
            ref["bundle_ref"], field="evidence_ref"
        ) or ""
    return result


def _validate_timestamp(value: object) -> None:
    text = _string(value, field="bundle_candidate")
    if not _RFC3339.fullmatch(text or ""):
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )
    try:
        parsed = datetime.fromisoformat(
            (text or "").replace("Z", "+00:00").replace("z", "+00:00")
        )
    except ValueError as exc:
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        ) from exc
    if parsed.tzinfo is None:
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )


def _validate_evidence_bundle(value: object) -> dict[str, object]:
    required = frozenset(
        {
            "bundle_id",
            "claim_scope",
            "evidence_refs",
            "source_records",
            "citations",
            "rights",
            "sensitivity",
            "transforms",
            "checksums",
            "spec_hash",
        }
    )
    bundle = _closed(
        value,
        allowed=required,
        required=required,
        field="bundle_candidate",
    )

    bundle_id = _string(bundle["bundle_id"], field="bundle_candidate") or ""
    if not _BUNDLE_ID.fullmatch(bundle_id):
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )
    _string(bundle["claim_scope"], field="bundle_candidate")

    raw_refs = bundle["evidence_refs"]
    if (
        not isinstance(raw_refs, list)
        or not raw_refs
        or len(raw_refs) > MAX_COLLECTION_ITEMS
    ):
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )
    evidence_refs = tuple(_validate_evidence_ref(item) for item in raw_refs)
    _string_list(bundle["source_records"], field="bundle_candidate")
    _string_list(bundle["citations"], field="bundle_candidate")
    _string_list(bundle["transforms"], field="bundle_candidate", allow_empty=True)

    rights = _closed(
        bundle["rights"],
        allowed=frozenset({"license"}),
        required=frozenset({"license"}),
        field="bundle_candidate",
    )
    _string(rights["license"], field="bundle_candidate")

    sensitivity = _closed(
        bundle["sensitivity"],
        allowed=frozenset({"level", "reason", "applied_at"}),
        required=frozenset({"level", "reason", "applied_at"}),
        field="bundle_candidate",
    )
    level = _string(sensitivity["level"], field="bundle_candidate")
    if level not in {"public", "generalized", "restricted", "quarantine"}:
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )
    _string(sensitivity["reason"], field="bundle_candidate")
    _validate_timestamp(sensitivity["applied_at"])

    checksums = _mapping(bundle["checksums"], field="bundle_candidate")
    if not checksums or len(checksums) > MAX_COLLECTION_ITEMS:
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )
    for key, digest in checksums.items():
        _string(key, field="bundle_candidate")
        digest_text = _string(digest, field="bundle_candidate") or ""
        if not _DIGEST.fullmatch(digest_text):
            raise CandidateInputError(
                "schema/evidence-bundle-invalid", "bundle_candidate"
            )

    spec_hash = _closed(
        bundle["spec_hash"],
        allowed=frozenset({"value"}),
        required=frozenset({"value"}),
        field="bundle_candidate",
    )
    spec_digest = _string(spec_hash["value"], field="bundle_candidate") or ""
    if not _DIGEST.fullmatch(spec_digest):
        raise CandidateInputError(
            "schema/evidence-bundle-invalid", "bundle_candidate"
        )

    return {"bundle_id": bundle_id, "evidence_refs": evidence_refs}


def _validate_lookup_context(value: object) -> dict[str, object]:
    required = frozenset(
        {
            "bundle_id",
            "current_head",
            "policy_outcome",
            "policy_decision_ref",
            "correction_state",
            "correction_ref",
        }
    )
    context = _closed(
        value,
        allowed=required,
        required=required,
        field="lookup_context",
    )
    bundle_id = _string(
        context["bundle_id"], field="lookup_context", nullable=True
    )
    current_head = context["current_head"]
    if current_head is not None and not isinstance(current_head, bool):
        raise CandidateInputError("input/invalid-boolean", "lookup_context")
    policy_outcome = _string(context["policy_outcome"], field="lookup_context")
    if policy_outcome not in _POLICY_OUTCOMES:
        raise CandidateInputError("input/invalid-enum", "lookup_context")
    correction_state = _string(context["correction_state"], field="lookup_context")
    if correction_state not in _CORRECTION_STATES:
        raise CandidateInputError("input/invalid-enum", "lookup_context")
    return {
        "bundle_id": bundle_id,
        "current_head": current_head,
        "policy_outcome": policy_outcome,
        "policy_decision_ref": _string(
            context["policy_decision_ref"],
            field="lookup_context",
            nullable=True,
        ),
        "correction_state": correction_state,
        "correction_ref": _string(
            context["correction_ref"], field="lookup_context", nullable=True
        ),
    }


def _error_result(issue: CandidateInputError) -> ResolutionCandidate:
    return ResolutionCandidate(
        profile=PROFILE,
        status="ERROR",
        bundle_id=None,
        checks_performed=("input_structure_bounds", "profile_shape"),
        issues=(ResolutionIssue(issue.code, issue.field),),
    )


def _bounded_error_result(issue: BoundedJSONError) -> ResolutionCandidate:
    return ResolutionCandidate(
        profile=PROFILE,
        status="ERROR",
        bundle_id=None,
        checks_performed=("input_structure_bounds",),
        issues=(ResolutionIssue(issue.code, "request"),),
    )


def evaluate_resolution_candidate(value: object) -> ResolutionCandidate:
    """Evaluate the explicit alpha profile without hidden I/O or authority.

    Status precedence is ``ERROR`` > ``DENIED`` > ``UNRESOLVED`` >
    ``RESOLVED``.  This keeps caller-supplied deny context fail-closed even when
    other closure inputs are incomplete.
    """

    try:
        _walk_bounds(value)
        request = _closed(
            value,
            allowed=frozenset(
                {"profile", "evidence_ref", "bundle_candidate", "lookup_context"}
            ),
            required=frozenset(
                {"profile", "evidence_ref", "bundle_candidate", "lookup_context"}
            ),
            field="request",
        )
        profile = _string(request["profile"], field="profile")
        if profile != PROFILE:
            raise CandidateInputError("profile/unsupported", "profile")
        evidence_ref = _validate_evidence_ref(request["evidence_ref"])
        lookup = _validate_lookup_context(request["lookup_context"])
        bundle = (
            None
            if request["bundle_candidate"] is None
            else _validate_evidence_bundle(request["bundle_candidate"])
        )
    except BoundedJSONError as exc:
        return _bounded_error_result(exc)
    except CandidateInputError as exc:
        return _error_result(exc)

    checks = [
        "input_structure_bounds",
        "profile_shape",
        "evidence_ref_shape",
        "lookup_context_shape",
    ]
    if bundle is not None:
        checks.append("evidence_bundle_shape")
    issues: list[ResolutionIssue] = []

    claimed_bundle_id = evidence_ref.get("bundle_ref")
    lookup_bundle_id = lookup["bundle_id"]
    candidate_bundle_id = bundle["bundle_id"] if bundle is not None else None

    if claimed_bundle_id is None:
        issues.append(ResolutionIssue("closure/bundle-ref-missing", "evidence_ref"))
    if bundle is None:
        issues.append(ResolutionIssue("lookup/not-found", "bundle_candidate"))
    if lookup_bundle_id is None:
        issues.append(ResolutionIssue("lookup/not-found", "lookup_context"))

    if claimed_bundle_id is not None and lookup_bundle_id is not None:
        checks.append("bundle_identity")
        if claimed_bundle_id != lookup_bundle_id:
            issues.append(ResolutionIssue("lookup/inconsistent-id", "lookup_context"))
    if candidate_bundle_id is not None and claimed_bundle_id is not None:
        if candidate_bundle_id != claimed_bundle_id:
            issues.append(
                ResolutionIssue("lookup/inconsistent-id", "bundle_candidate")
            )
    if candidate_bundle_id is not None and lookup_bundle_id is not None:
        if candidate_bundle_id != lookup_bundle_id:
            issues.append(
                ResolutionIssue("lookup/inconsistent-id", "bundle_candidate")
            )

    if bundle is not None:
        checks.append("bundle_membership")
        if any(
            member.get("bundle_ref") not in {None, candidate_bundle_id}
            for member in bundle["evidence_refs"]
        ):
            issues.append(
                ResolutionIssue(
                    "closure/member-bundle-ref-mismatch", "bundle_candidate"
                )
            )
        membership = any(
            member["ref"] == evidence_ref["ref"]
            and member["kind"] == evidence_ref["kind"]
            for member in bundle["evidence_refs"]
        )
        if not membership:
            issues.append(
                ResolutionIssue(
                    "closure/evidence-ref-not-member", "bundle_candidate"
                )
            )

    checks.append("lookup_current_head")
    if lookup["current_head"] is not True:
        issues.append(ResolutionIssue("lookup/not-current-head", "lookup_context"))

    checks.append("policy_passthrough")
    policy = lookup["policy_outcome"]
    if lookup["policy_decision_ref"] is None:
        issues.append(ResolutionIssue("policy/context-unbound", "lookup_context"))
    if policy == "DENY":
        issues.append(ResolutionIssue("policy/blocked-context", "lookup_context"))
    elif policy == "ABSTAIN":
        issues.append(ResolutionIssue("policy/context-abstained", "lookup_context"))
    elif policy == "ERROR":
        issues.append(ResolutionIssue("policy/context-error", "lookup_context"))

    checks.append("correction_context")
    correction_state = lookup["correction_state"]
    if correction_state == "SUPERSEDED":
        issues.append(ResolutionIssue("correction/superseded", "lookup_context"))
    elif correction_state == "WITHDRAWN":
        issues.append(ResolutionIssue("correction/withdrawn", "lookup_context"))
    elif correction_state == "UNKNOWN":
        issues.append(ResolutionIssue("correction/unknown", "lookup_context"))
    if (
        correction_state in {"SUPERSEDED", "WITHDRAWN"}
        and lookup["correction_ref"] is None
    ):
        issues.append(
            ResolutionIssue("correction/reference-missing", "lookup_context")
        )

    deduplicated = tuple(sorted(set(issues)))
    codes = {issue.code for issue in deduplicated}
    if "policy/context-error" in codes:
        status = "ERROR"
    elif "policy/blocked-context" in codes:
        status = "DENIED"
    elif codes:
        status = "UNRESOLVED"
    else:
        status = "RESOLVED"

    return ResolutionCandidate(
        profile=PROFILE,
        status=status,
        bundle_id=(
            candidate_bundle_id
            if status == "RESOLVED" and isinstance(candidate_bundle_id, str)
            else None
        ),
        checks_performed=tuple(dict.fromkeys(checks)),
        issues=deduplicated,
    )


def result_json(result: ResolutionCandidate) -> str:
    """Serialize a result deterministically without reflecting raw input."""

    return json.dumps(
        result.as_dict(),
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )
