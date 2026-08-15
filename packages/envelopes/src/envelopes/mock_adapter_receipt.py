"""Bounded projection from a prevalidated MockAdapter response to AIReceipt.

This helper closes only one deterministic compatibility gap: it copies the finite
outcome selected by the existing no-I/O ``MockAdapter`` proof into the existing
``AIReceipt`` candidate builder while fixing the adapter/model identity to the
synthetic mock lane.

It does not call a model, invoke ``MockAdapter``, validate a RuntimeResponseEnvelope,
canonicalize or calculate digests, resolve evidence or references, evaluate policy,
validate citations, persist a receipt, authorize an answer, promote lifecycle state,
or create release/publication authority. Callers must supply already-computed input
and output digests plus authority-bearing references and must run the repository's
own schema/semantic validators at the trust boundary.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from .ai_receipt import build_ai_receipt_candidate
from .runtime_response import EnvelopeBuildError


MOCK_ADAPTER_ID: Final[str] = "mock"
MOCK_MODEL_REF: Final[str] = "fixture-only"


def build_mock_adapter_ai_receipt_candidate(
    *,
    response_envelope: Mapping[str, object],
    receipt_id: str,
    run_id: str,
    inputs_digest: str,
    outputs_digest: str,
    policy_decision_ref: str,
    citation_validation_ref: str,
) -> dict[str, str]:
    """Project one prevalidated mock response into a closed AIReceipt candidate.

    The response envelope remains owned by its existing contract/schema/validator.
    This helper reads only ``outcome``. Successful construction does not prove that
    either supplied digest binds the response bytes; canonicalization remains an
    upstream responsibility until KFM adopts a reproducible digest profile.
    """

    if not isinstance(response_envelope, Mapping):
        raise EnvelopeBuildError("FIELD_NOT_OBJECT", "response_envelope")

    outcome = response_envelope.get("outcome")
    if not isinstance(outcome, str) or not outcome.strip():
        raise EnvelopeBuildError("FIELD_INVALID", "response_envelope.outcome")

    return build_ai_receipt_candidate(
        receipt_id=receipt_id,
        run_id=run_id,
        adapter=MOCK_ADAPTER_ID,
        model_ref=MOCK_MODEL_REF,
        inputs_digest=inputs_digest,
        outputs_digest=outputs_digest,
        policy_decision_ref=policy_decision_ref,
        citation_validation_ref=citation_validation_ref,
        outcome=outcome,
    )
