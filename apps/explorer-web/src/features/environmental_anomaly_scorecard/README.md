# Environmental anomaly scorecard

This inactive Explorer feature adapts Pass 32 card `KFM-P32-FEAT-0006` into a strict, table-first county scorecard for vegetation, hydrology, air, soils, and biodiversity.

An available projection shows exactly five synthetic domain lanes with freshness and anomaly-candidate states. `COMPLETE` or `HOLD` describes fixture coherence only. `PROPOSED` is a candidate state, not an environmental finding, and requires a separate interpretation gate.

The adapter requires an exact pre-governed projection fixed to fixture-only, inactive, no-interpretation, no-publication, and no-public-use posture. Missing or malformed input renders nothing. Finite abstain, deny, and error projections expose no county, time, lane, evidence, health-assessment, or candidate detail.

This module is not mounted on a route. It performs no transport, source probing, freshness authoring, anomaly computation, model invocation, policy evaluation, lifecycle write, promotion, release, deployment, publication, or public-use action.

Validation lives in `apps/explorer-web/tests/environmental-anomaly-scorecard.test.ts` and the isolated browser fixture. Rollback is a focused revert of this additive feature packet.
