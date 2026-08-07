<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/decision-envelope/validation-notes
title: DecisionEnvelope Validation Notes
type: validation-notes; compatibility-support; no-authority
version: v0.1.0
status: proposed; implemented-validator; fixture-first; no-network
owners: OWNER_TBD — Runtime steward · Validation steward · Contracts steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; runtime; validation; no-authority
related:
  - ../decision_envelope.md
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../fixtures/contracts/v1/runtime/decision_envelope/
  - ../../../tools/validators/validate_decision_envelope.py
  - ../../../tests/validators/test_validate_decision_envelope.py
[/KFM_META_BLOCK_V2] -->

# DecisionEnvelope validation notes

The canonical semantic contract remains [`../decision_envelope.md`](../decision_envelope.md).
This note documents the implemented validation boundary; it does not define a second
`DecisionEnvelope` meaning.

## Enforced boundary

The validator preserves the current schema and existing valid fixtures while adding deterministic
semantic checks for:

- `decision` / `outcome` alias agreement;
- bounded, unique reason and obligation text;
- credential-like text denial without value echo;
- canonical, public-safe evidence-reference lists;
- DENY and ERROR support non-disclosure;
- `evaluated_at` / `issued_at` ordering;
- lowercase SHA-256 `spec_hash` syntax;
- semantic-version syntax;
- upper-snake `reason_code` syntax;
- safe compatibility IDs;
- duplicate-key, non-finite-number, symlink, oversized, malformed, and unreadable inputs.

The exact fixture matrix is
`fixtures/contracts/v1/runtime/decision_envelope/expected_findings_manifest.json`.

## Finite validator outcomes

| Exit | Meaning |
|---:|---|
| `0` | Schema and semantic validation passed. |
| `1` | Candidate is readable but violates schema or semantic rules. |
| `2` | Input, manifest, or validator dependency failed safely. |

A pass proves only local contract conformance. It does not resolve an `EvidenceRef`, evaluate
policy, authenticate a reviewer, establish release state, authorize an action, publish, or permit
public use.

## Rollback

Revert the bounded validator packet. Existing serialized envelopes and the current machine
schema are unchanged, so no migration, reprocessing, release withdrawal, or public correction
is required.
