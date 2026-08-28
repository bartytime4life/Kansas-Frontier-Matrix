# Governance health projection source adaptation

Status: IMPLEMENTED as a bounded `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile.

Reconciled against `main@2d0c9a8e4072ce14cb71404585e85fbc86339e12` on 2026-08-25. Proposal lineage remains the 23-indicator Atlas mirror described by [`docs/dashboards/INDICATOR_CATALOG.md`](../../dashboards/INDICATOR_CATALOG.md), v0.2, §§1 and 4. The catalog explicitly keeps indicators observational rather than enforcing policy or publication decisions.

The earlier absence statement is superseded by current executable repository evidence. The bounded profile now exists as:

- semantic contract: [`contracts/governance/governance_health_projection.md`](../../../contracts/governance/governance_health_projection.md);
- machine shape: [`schemas/contracts/v1/governance/governance_health_projection.schema.json`](../../../schemas/contracts/v1/governance/governance_health_projection.schema.json);
- synthetic cases: [`fixtures/contracts/v1/governance/governance_health_projection/cases.json`](../../../fixtures/contracts/v1/governance/governance_health_projection/cases.json);
- deterministic compiler: [`tools/generators/governance_health/compile_governance_health_projection.py`](../../../tools/generators/governance_health/compile_governance_health_projection.py);
- focused proof: [`tests/generators/governance_health/test_compile_governance_health_projection.py`](../../../tests/generators/governance_health/test_compile_governance_health_projection.py); and
- read-only workflow: [`.github/workflows/governance-health-projection.yml`](../../../.github/workflows/governance-health-projection.yml).

The compiler emits counts and ratios for eight bounded indicators from normalized fixture inputs and validates the complete output shape before returning it. It does not read canonical stores, apply dashboard thresholds, or declare the system healthy, safe, compliant, release-ready, or publishable. No policy, lifecycle, release, deployment, publication, or enforcement effect is created.

Accepted ADR-0029 and the adopted Directory Rules support the existing placement: meaning under `contracts/governance/`, shape under `schemas/contracts/v1/governance/`, synthetic replay under `fixtures/`, deterministic generation under `tools/generators/governance_health/`, proof under `tests/generators/governance_health/`, and orchestration under `.github/workflows/`. This reconciliation changes only the source map; no packet file, registry, manifest, compatibility surface, or authority home changes.
