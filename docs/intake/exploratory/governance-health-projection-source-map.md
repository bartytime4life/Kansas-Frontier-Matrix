# Governance health projection source adaptation

Status: PROPOSED implementation candidate.

The KFM Indicator Catalog mirrors 23 governance-health indicators from the Atlas and explicitly states that indicators are reported rather than enforced. Current repository evidence confirms extensive dashboard specifications but no executable `governance_health` projection compiler.

This slice implements a deterministic, fixture-only first projection over eight high-value indicators spanning evidence resolution, cite-or-abstain, release rollback support, correction derivative invalidation, sensitive fail-closed behavior, AIReceipt presence, ADR completeness, and open drift. It accepts normalized references to existing record families rather than reading canonical stores directly.

The projection emits counts and ratios only. It does not apply dashboard target thresholds or declare the system healthy, safe, compliant, release-ready, or publishable. No policy, lifecycle, release, deployment, publication, or enforcement effect is created.

Directory Rules basis: semantic meaning under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic replay under `fixtures/contracts/v1/governance/`; deterministic generation under `tools/generators/governance_health/`; tests under `tests/generators/governance_health/`; orchestration under `.github/workflows/`.
