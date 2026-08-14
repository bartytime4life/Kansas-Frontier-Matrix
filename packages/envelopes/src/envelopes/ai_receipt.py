"""Deterministic candidate builder for the current ``AIReceipt`` profile.

The helper performs only bounded, local checks that are already explicit in the
paired AIReceipt schema and validator.  It does not call a model, resolve
EvidenceRef objects, evaluate policy, validate citations, calculate the input or
output digests, persist a receipt, authorize an answer, promote lifecycle state,
or create release/publication authority.

Callers must supply every authority-bearing reference and digest explicitly and
must still run the repository's authoritative JSON Schema and semantic validator
at the trust boundary.
"""

from __future__ import annotations

import re
from typing import Final

from .runtime_response import EnvelopeBuildError


AI_RECEIPT_OUTCOMES: Final[frozenset[str]] = frozenset(
    {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
)
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_SHA256_RE: Final[re.Pattern[str]] = re.compile(r"^sha256:[a-f0-9]{64}$")
_ZERO_SHA256: Final[str] = "sha256:" + ("0" * 64)


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


def _require_digest(value: object, field: str) -> str:
    digest = _require_pattern(value, field, _SHA256_RE)
    if digest == _ZERO_SHA256:
        raise EnvelopeBuildError("DIGEST_PLACEHOLDER", field)
    return digest


def build_ai_receipt_candidate(
    *,
    receipt_id: str,
    run_id: str,
    adapter: str,
    model_ref: str,
    inputs_digest: str,
    outputs_digest: str,
    policy_decision_ref: str,
    citation_validation_ref: str,
    outcome: str,
) -> dict[str, str]:
    """Build one closed ``AIReceipt`` candidate from explicit caller inputs.

    Successful construction means only that this module's bounded checks passed.
    It does not establish evidence sufficiency, policy authorization, citation
    validity, model approval, public-answer eligibility, review, release, or
    publication.  The returned mapping contains exactly the fields required by
    ``schemas/contracts/v1/runtime/ai_receipt.schema.json``.
    """

    checked_outcome = _require_nonempty_string(outcome, "outcome")
    if checked_outcome not in AI_RECEIPT_OUTCOMES:
        raise EnvelopeBuildError("OUTCOME_INVALID", "outcome")

    return {
        "id": _require_pattern(receipt_id, "id", _ID_RE),
        "run_id": _require_nonempty_string(run_id, "run_id"),
        "adapter": _require_nonempty_string(adapter, "adapter"),
        "model_ref": _require_nonempty_string(model_ref, "model_ref"),
        "inputs_digest": _require_digest(inputs_digest, "inputs_digest"),
        "outputs_digest": _require_digest(outputs_digest, "outputs_digest"),
        "policy_decision_ref": _require_nonempty_string(
            policy_decision_ref, "policy_decision_ref"
        ),
        "citation_validation_ref": _require_nonempty_string(
            citation_validation_ref, "citation_validation_ref"
        ),
        "outcome": checked_outcome,
    }
