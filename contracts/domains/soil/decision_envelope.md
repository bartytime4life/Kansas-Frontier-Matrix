# Soil DecisionEnvelope projection

Status: PROPOSED  
Authority: domain projection of the shared runtime `DecisionEnvelope`; not independent runtime, policy, evidence, promotion, release, or publication authority.

The Soil lane uses the shared runtime `DecisionEnvelope` semantics from `contracts/runtime/decision_envelope.md`. The Soil-specific schema at `schemas/contracts/v1/domains/soil/decision_envelope.schema.json` therefore projects the shared runtime shape instead of defining a competing envelope.

## Meaning

A Soil DecisionEnvelope records a finite runtime-facing result associated with a Soil request or render decision. Its finite outcomes remain `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, with the same required fields and closed shape as the shared runtime contract.

Soil-specific evidence, sensitivity, rights, source-role, support-type, release, and correction requirements remain owned by their existing evidence, policy, registry, release, and domain-contract surfaces. This projection may reference those decisions through the shared envelope fields, but it cannot make them.

## Compatibility

`schemas/contracts/v1/domains/soil/soil_decision_envelope.schema.json` is retained as a deprecated compatibility alias that resolves to `decision_envelope.schema.json`. It must not acquire independent fields, enums, or semantic rules. Retirement of the alias requires a verified consumer inventory and a bounded migration decision.

## Trust boundary

A valid Soil DecisionEnvelope is not proof that evidence resolves, not a PolicyDecision, not a PromotionDecision, not a ReleaseManifest, and not permission to render unpublished or sensitive content. Public clients remain downstream of governed runtime/API interfaces and released artifacts.
