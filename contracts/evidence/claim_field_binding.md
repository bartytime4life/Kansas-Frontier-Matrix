<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/claim-field-binding/v1
title: ClaimFieldBinding Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define field-level evidence binding without treating source text, normalization, a receipt, or generated language as resolved evidence or release authority.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION steward review and operational adoption"
related:
  - ../../schemas/contracts/v1/evidence/claim_field_binding.schema.json
  - ../../fixtures/contracts/v1/evidence/claim_field_binding/
  - ../../tools/validators/validate_claim_field_binding.py
  - ../../tests/validators/test_validate_claim_field_binding.py
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ../common/spec_hash.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, field-binding, provenance, transform, confidence, deterministic, fixture-only, no-network]
notes:
  - "Implements the field-level ClaimFieldBinding named by the briefing-to-system evidence-binding table."
  - "A PASS proves local shape and invariants only; no EvidenceRef is dereferenced and no EvidenceBundle is created."
[/KFM_META_BLOCK_V2] -->

# ClaimFieldBinding

## Purpose

`ClaimFieldBinding` records how one normalized object field is supported by one
source-native location and a declared transformation. It binds:

```text
object field
  -> source artifact and immutable source snapshot
  -> native locator
  -> source statement/value digests
  -> normalized value digest
  -> transform and TransformReceipt reference
  -> EvidenceRef
  -> support scope, quality, confidence, and limitations
```

The binding is intentionally value-minimizing. It carries digests and references,
not raw source statements or normalized values. It does not resolve an
`EvidenceRef`, create an `EvidenceBundle`, establish rights, authorize a claim,
or make a field public.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.evidence.claim-field-binding.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Schema | `schemas/contracts/v1/evidence/claim_field_binding.schema.json` |
| Validator | `tools/validators/validate_claim_field_binding.py` |
| Evidence resolution | Not performed |
| Release state | Semantically fixed to `UNRELEASED` |
| Public use | Semantically fixed to `false` |
| Lifecycle writes | None |

A `PASS` means only that the candidate is internally coherent for this profile.

## Published language

| Concept | Meaning |
|---|---|
| `field_pointer` | Canonical JSON Pointer into the normalized object |
| `native_locator` | Source-native field, range, column, pointer, or path |
| `native_statement_digest` | Digest of the source statement used for support |
| `native_value_digest` | Digest of the source-native value |
| `normalized_value_digest` | Digest of the normalized field value |
| `transform` | Declared normalization/redaction/generalization step |
| `evidence_ref` | Reference to support that remains unresolved here |
| `support_scope` | `EXACT_FIELD`, `DERIVED_FIELD`, or `CONTEXT_ONLY` |
| `quality` | Bounded state, confidence, and stable reason codes |
| `lineage` | Source-binding correction, supersession, or conflict state |

## Transform rules

`NONE` requires no transform or receipt reference and must remain deterministic.
Every non-`NONE` transform requires:

- `transform_ref`;
- `transform_receipt_ref`;
- `deterministic: true`.

A transform receipt is process memory, not evidence or proof. A field that lacks
the required receipt is denied rather than silently treated as normalized.

## Confidence and conflict rules

`CONTEXT_ONLY` support cannot claim `CONFIRMED` or `HIGH` confidence. A
`CONFLICTED` binding requires:

- at least two conflict references;
- `quality.state = CONFLICTED`;
- `quality.confidence = UNRESOLVED`.

Conflicting source values remain represented. The validator never selects one
because it is newer or more fluent.

## Identity

`spec_hash` uses the repository RFC 8785 JCS plus SHA-256 package.
`claim_field_binding_id` is derived from the first 24 hexadecimal characters of
that hash. The identity subject excludes only those two identity fields.

## Finite outcomes

- `PASS` — bounded candidate accepted;
- `DENY` — semantic or authority boundary violated;
- `ERROR` — unsafe input, unavailable dependency, or identity corruption.

Diagnostics expose stable code/path pairs and do not echo source values.

## Authority non-effects

Every fixture carries all-false source, evidence, policy, promotion, release, and
publication effects. Any released state, release reference, public-use claim, or
true effect is denied.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. The packet uses established
responsibility roots: `contracts/evidence/` for meaning,
`schemas/contracts/v1/evidence/` for machine shape,
`fixtures/contracts/v1/evidence/` for synthetic proof input,
`tools/validators/` for execution, `tests/validators/` for behavior,
`.github/workflows/` for read-only CI, `docs/intake/exploratory/` for the
adaptation record, and `data/receipts/generated/` for authoring accountability.

No new root, EvidenceBundle authority, policy home, source registry, release
home, proof home, or publication path is created.

## Non-effects

This profile does not fetch a source, expose source values, resolve evidence,
evaluate rights or policy, write a lifecycle stage, promote, release, publish,
serve an API, draw a map, or answer with AI.

## Rollback

Before merge, close the draft pull request or abandon the branch. After an
authorized merge, revert the additive packet. No live or public state requires
restoration.
