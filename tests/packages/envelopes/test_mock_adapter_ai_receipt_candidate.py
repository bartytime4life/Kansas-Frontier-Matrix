"""Focused proof for MockAdapter-to-AIReceipt candidate projection."""

from __future__ import annotations

import unittest

from envelopes.mock_adapter_receipt import (
    MOCK_ADAPTER_ID,
    MOCK_MODEL_REF,
    build_mock_adapter_ai_receipt_candidate,
)
from envelopes.runtime_response import EnvelopeBuildError
from runtime.model_adapters.MockAdapter import MockAdapter


INPUT_DIGEST = "sha256:" + ("a" * 64)
OUTPUT_DIGEST = "sha256:" + ("b" * 64)


def _scenarios() -> dict[str, dict[str, object]]:
    return {
        f"fixture-{outcome.lower()}": {"outcome": outcome}
        for outcome in ("ANSWER", "ABSTAIN", "DENY", "ERROR")
    }


def _kwargs(response: object) -> dict[str, object]:
    return {
        "response_envelope": response,
        "receipt_id": "ai_receipt:focus:mock-001",
        "run_id": "mock-run-001",
        "inputs_digest": INPUT_DIGEST,
        "outputs_digest": OUTPUT_DIGEST,
        "policy_decision_ref": "policy-decision:fixture-001",
        "citation_validation_ref": "citation-validation:fixture-001",
    }


class MockAdapterAIReceiptCandidateTests(unittest.TestCase):
    def test_projects_all_mock_outcomes_with_fixed_mock_identity(self) -> None:
        adapter = MockAdapter(_scenarios())

        for scenario_id in adapter.scenario_ids:
            response = adapter.respond(scenario_id)
            receipt = build_mock_adapter_ai_receipt_candidate(**_kwargs(response))

            self.assertEqual(receipt["outcome"], response["outcome"])
            self.assertEqual(receipt["adapter"], MOCK_ADAPTER_ID)
            self.assertEqual(receipt["model_ref"], MOCK_MODEL_REF)

    def test_does_not_mutate_response(self) -> None:
        response = {"outcome": "ABSTAIN", "reason_code": "synthetic"}
        original = dict(response)

        build_mock_adapter_ai_receipt_candidate(**_kwargs(response))

        self.assertEqual(response, original)

    def test_rejects_non_mapping_or_missing_outcome_without_echoing_payload(self) -> None:
        with self.assertRaises(EnvelopeBuildError) as caught:
            build_mock_adapter_ai_receipt_candidate(**_kwargs([]))

        self.assertEqual(
            (caught.exception.code, caught.exception.field),
            ("FIELD_NOT_OBJECT", "response_envelope"),
        )

        secret = {"answer": "secret-like-value"}
        with self.assertRaises(EnvelopeBuildError) as caught:
            build_mock_adapter_ai_receipt_candidate(**_kwargs(secret))

        self.assertEqual(
            (caught.exception.code, caught.exception.field),
            ("FIELD_INVALID", "response_envelope.outcome"),
        )
        self.assertNotIn("secret-like-value", str(caught.exception))

    def test_rejects_outcome_outside_closed_ai_receipt_vocabulary(self) -> None:
        with self.assertRaises(EnvelopeBuildError) as caught:
            build_mock_adapter_ai_receipt_candidate(
                **_kwargs({"outcome": "WAITING"})
            )

        self.assertEqual(
            (caught.exception.code, caught.exception.field),
            ("OUTCOME_INVALID", "outcome"),
        )

    def test_preserves_explicit_digest_and_authority_refs(self) -> None:
        receipt = build_mock_adapter_ai_receipt_candidate(
            **_kwargs({"outcome": "DENY"})
        )

        self.assertEqual(receipt["inputs_digest"], INPUT_DIGEST)
        self.assertEqual(receipt["outputs_digest"], OUTPUT_DIGEST)
        self.assertEqual(
            receipt["policy_decision_ref"], "policy-decision:fixture-001"
        )
        self.assertEqual(
            receipt["citation_validation_ref"],
            "citation-validation:fixture-001",
        )


if __name__ == "__main__":
    unittest.main()
