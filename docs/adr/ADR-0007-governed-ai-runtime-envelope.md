# ADR-0007: Governed AI Runtime Response Envelope

- **Status:** proposed
- **Date:** 2026-04-27
- **Decision area:** AI runtime / API contract / trust boundary

## Context

AI outputs require enforceable structure to preserve citations, abstention behavior, and policy annotations.

## Decision

Governed AI responses must use a versioned response envelope including claim payload, evidence references, policy annotations, and abstention/error semantics.

## Alternatives considered

- **Free-form text responses only:** rejected because policy and evidence linkage cannot be reliably enforced.
- **Provider-native envelopes:** rejected because portability and governance consistency degrade.

## Consequences

### Positive

- Stronger traceability for generated claims.
- Contract-level enforcement of abstain/fail-safe behavior.

### Negative / tradeoffs

- Envelope evolution requires version management.
- May add integration friction for client consumers.

## Verification

- Contract tests for envelope shape and required fields.
- Policy tests for abstain behavior when evidence is insufficient.

## Migration / rollback

Provide envelope adapters for legacy clients and deprecate old formats on a scheduled timeline.
