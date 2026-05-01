# ADR-0241: Policy Obligation Engine + Release Gate v1

## KFM Meta Block v2
- doc_id: ADR-0241
- title: Policy Obligation Engine + Release Gate v1
- status: draft
- owners: governance
- updated: 2026-05-01
- policy_label: PROPOSED

## Context
This ADR proposes an offline, fixture-backed governance gate that fail-closes before artifacts can move to public, controlled, or export channels.

## Decision
Introduce a deterministic local policy gate that emits:
- `DecisionEnvelope.v1`
- `PolicyEvaluationResult.v1`

No artifact may be publicly released/exported unless decision is `allow`.

## Fail-closed doctrine
Quarantine/deny/suppress/recompute is required on:
- missing schema
- missing policy profile
- missing consent reference where required
- expired retention
- unknown release channel
- revoked consent
- hash mismatches

## Inputs
- Artifact metadata
- EvidenceBundle
- run_receipt
- obligations profile (`policy/consent/*.md` currently hashed as profile input)
- gate config (`policy/gates/release_gate.v1.yaml`)
- optional revoke_delta

## Outputs
- DecisionEnvelope (signed local stub)
- PolicyEvaluationResult

## Evaluation order
1. Structural input validation.
2. Canonical-hash verification.
3. Consent resolution.
4. Revocation check.
5. Retention check.
6. Aggregation/coordinate check.
7. Export format check.
8. rights_status/policy_label compatibility.
9. Emit deterministic IDs + local stub signature.

## Revocation handling
- Revoked + direct artifact => `suppress`
- Revoked + derived artifact => `recompute_required`
- Revocation token is never persisted in outputs.

## Privacy
Coordinates are blocked for exact public release. Only policy-safe metadata is emitted.

## Rollback
Rollback is code/config/schema revert. No source EvidenceBundle mutation is allowed.

## No-network posture
v1 runs completely offline and does not call Sigstore, VC registries, or remote policy servers.

## NEEDS_VERIFICATION
- Canonical schema-home authority between `contracts/` and `schemas/contracts/v1/`.
- Whether policy profile should be machine-readable in v2 (current v1 hashes file bytes).