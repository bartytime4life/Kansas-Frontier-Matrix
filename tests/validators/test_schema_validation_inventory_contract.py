from __future__ import annotations

from tools.validators._common.run_all import RUNNER_VALIDATORS


HISTORICAL_SCHEMA_VALIDATION_CORE = [
    "validate_source_descriptor.py",
    "validate_evidence_ref.py",
    "validate_evidence_bundle.py",
    "validate_layer_manifest.py",
    "validate_dataset_version.py",
    "validate_runtime_response_envelope.py",
    "validate_decision_envelope.py",
    "validate_run_receipt.py",
    "validate_ingest_receipt.py",
]


def test_historical_schema_validation_core_is_stable_prefix_of_full_fixture_inventory() -> None:
    """Registry growth must not invalidate the bounded historical fixture preflight."""

    assert RUNNER_VALIDATORS[: len(HISTORICAL_SCHEMA_VALIDATION_CORE)] == (
        HISTORICAL_SCHEMA_VALIDATION_CORE
    )
    assert len(RUNNER_VALIDATORS) == len(set(RUNNER_VALIDATORS))
    assert len(RUNNER_VALIDATORS) >= len(HISTORICAL_SCHEMA_VALIDATION_CORE)
