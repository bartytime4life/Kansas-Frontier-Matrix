# Planning scenario review

This Explorer Web feature renders a strict, fixture-only planning-scenario projection as a text-first review surface. It adapts the existing synthetic `PlanningScenarioManifest` pilot and the Atlas `Participatory Planning Support` triad into visible horizon, input uncertainty, assumptions, equity questions, participation references, evidence references, limitations, and non-authority labels.

The feature lives under the existing `apps/explorer-web/src/features/` responsibility boundary because it is app-local presentation. Its parser lives under the adjacent app-local adapter boundary. Reusable synthetic inputs remain under `fixtures/ui/`, and executable proof remains under `apps/explorer-web/tests/`. No schema, policy, source, evidence, release, or lifecycle authority is duplicated.

An available projection remains `ABSTAIN`, `HELD`, `PROPOSED_INACTIVE`, synthetic, and fixture-only. It exposes review context without becoming a prediction, recommendation, emergency alert, regulatory determination, evidence resolution, policy approval, human review, release, deployment, or publication. Missing or malformed input renders nothing. Missing, denied, and error projections show fixed copy and no scenario, evidence, participation, or limitation detail.

The feature performs no transport, persistence, source retrieval, model invocation, scenario computation, preference aggregation, policy evaluation, lifecycle write, release action, or publication action. It is not mounted on a production route.

Validation is provided by `apps/explorer-web/tests/planning-scenario-review.test.ts` and the isolated Playwright fixture. The unit suite also checks that the available UI fixture remains aligned with the existing validated water-planning manifest for title, purpose, horizon, input identities, assumptions, equity dimensions, participation references, evidence references, and limitations.

Rollback is a focused revert of this additive adapter, feature, fixture, test, and parent-index packet.
