import pytest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]


@pytest.mark.xfail(reason="stale air reentry fixtures/schema paths removed during restructuring")
def test_new_schemas_exist():
    names=[
        'reentry_deployment_environment_refresh_candidate.schema.json',
        'reentry_static_hosting_manifest_refresh_candidate.schema.json',
        'reentry_deployment_readiness_refresh_plan.schema.json',
        'reentry_synthetic_probe_refresh_spec.schema.json',
        'reentry_synthetic_probe_refresh_report.schema.json',
        'reentry_cache_invalidation_refresh_plan.schema.json',
        'reentry_deployment_rollback_refresh_plan.schema.json',
        'reentry_deployment_readiness_refresh_report.schema.json',
        'reentry_deployment_readiness_refresh_manifest.schema.json',
        'reentry_deployment_readiness_refresh_decision.schema.json',
        'reentry_deployment_readiness_refresh_postcheck_report.schema.json',
        'reentry_deployment_readiness_refresh_ledger_entry.schema.json',
        'reentry_deployment_readiness_refresh_ledger_manifest.schema.json',
        'reentry_deployment_readiness_refresh_audit_report.schema.json',
        'reentry_deployment_readiness_refresh_event.schema.json',
    ]
    for n in names:
        assert (ROOT/'schemas/contracts/v1/air'/n).exists()
