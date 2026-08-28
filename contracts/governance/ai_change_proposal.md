<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/ai-change-proposal
title: AIChangeProposal Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Governance steward · AI surface steward · Contract steward · Schema steward · Policy steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/ai_change_proposal.schema.json
  - ../../fixtures/contracts/v1/governance/ai_change_proposal/
  - ../../tools/validators/governance/validate_ai_change_proposal.py
  - ../../tests/validators/governance/test_ai_change_proposal.py
  - ../../packages/hashing/src/hashing/core.py
  - ../../policy/ai_builder/operating_contract.rego
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, ai, proposal, deterministic-patch, compare-and-set, idempotency, policy, human-review]
notes:
  - "This contract implements a fixture-only proposal record. It does not call a model, evaluate OPA, sign an artifact, apply a patch, mutate the repository, or authorize promotion."
  - "The current executable spec_hash grammar remains sha256:<hex>; this contract reuses the merged RFC 8785 implementation without changing hash identity policy."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AIChangeProposal Contract

> **Purpose.** Define a deterministic, reviewable, non-authoritative record for a JSON change proposed by an AI proposal engine. The proposal may be inspected and validated, but it cannot apply itself.

## Status

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Authority created | `NONE` |
| Machine shape | `schemas/contracts/v1/governance/ai_change_proposal.schema.json` |
| Validator | `tools/validators/governance/validate_ai_change_proposal.py` |
| Current live integration | None |
| Public-use posture | Denied |

A conforming proposal proves only that a bounded JSON subject, a deterministic compare-and-set patch, a policy-decision projection, a human-review projection, and a readiness projection agree with this profile.

It does **not** prove that:

- the proposed content is true, useful, rights-cleared, policy-approved, or safe;
- an `EvidenceRef` was resolved to an `EvidenceBundle`;
- a policy engine actually evaluated the proposal;
- a human actually approved the proposal;
- a signature or transparency-log entry exists;
- the patch may be applied to a repository, canonical store, lifecycle store, release, or public product.

## Source-derived design

The supplied *New Ideas 3-7-2026* packet describes AI as a proposal engine rather than an autopilot. Its recurring sequence is:

```text
canonical subject
  -> deterministic identity
  -> proposal
  -> policy gate
  -> idempotency check
  -> receipt / human attestation
  -> separately authorized apply
```

This contract implements only the smallest dependency-closed part of that pattern: deterministic proposal identity, compare-and-set patch mechanics, policy/review projections, finite readiness, and fail-closed validation. Live AI, OPA/Conftest, Cosign, Rekor, Temporal, repository mutation, and promotion remain outside this slice.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2 and makes paths authority claims. This object is a governance record, so meaning belongs under `contracts/governance/`; machine shape belongs under `schemas/contracts/v1/governance/`; synthetic examples belong under `fixtures/contracts/v1/governance/`; enforceability belongs under `tools/validators/` and `tests/`; CI belongs under `.github/workflows/`; the generated authoring receipt belongs under `data/receipts/generated/`.

No new root or parallel contract, schema, policy, receipt, proof, release, source-registry, or publication authority is created.

## Object meaning

An `AIChangeProposal` binds six distinct concerns without collapsing their authority:

1. **Producer identity** — which proposal engine profile produced the candidate, plus hashes of its prompt and admitted input bundle.
2. **Subject identity** — an opaque subject reference and exact RFC 8785 + SHA-256 pre-image and expected post-image hashes.
3. **Patch mechanics** — a deterministic ordered set of object-only JSON Pointer compare-and-set operations.
4. **Policy projection** — a cited policy decision and the obligations it requires and records as satisfied.
5. **Human-attestation projection** — pending, approved, or rejected state linked to a separate review record when resolved.
6. **Readiness projection** — a deterministic `HOLD`, `DENY`, or `READY_FOR_STEWARD_APPLY` label.

`READY_FOR_STEWARD_APPLY` means only that this proposal's internal projections are mutually consistent. It is not permission to mutate anything. A separate actor and governed operation must still re-read the current subject, verify the pre-image, re-evaluate policy, verify review authority, and emit its own receipt.

## Required top-level invariants

- `profile_status` is `PROPOSED_INACTIVE`.
- `execution_mode` is `FIXTURE_ONLY`.
- `authority` is `NONE`.
- `subject.target_zone` is `WORK`.
- every permission flag is `false`;
- `non_effects` is the exact closed list required by the schema;
- `evidence_refs` is sorted, unique, and non-empty;
- no prompt body, model response body, credential, secret, signature key, or sensitive source payload is embedded.

## Deterministic identity

### Subject identity

```text
input_spec_hash  = SHA-256(RFC8785-JCS(input_subject))
output_spec_hash = SHA-256(RFC8785-JCS(output_subject))
```

The serialized identifier remains the repository's current executable form:

```text
sha256:<64 lowercase hexadecimal characters>
```

### Patch identity

The patch hash covers only the meaning-bearing patch mechanics:

```json
{
  "algorithm": "kfm-json-compare-and-set-v1",
  "operations": [
    {
      "op": "replace",
      "path": "/settings/enabled",
      "before": {"present": true, "value": false},
      "after": {"present": true, "value": true}
    }
  ]
}
```

```text
patch_spec_hash = SHA-256(RFC8785-JCS(patch_projection))
```

### Proposal identity

The proposal ID covers:

- profile and schema version;
- producer identity and input hashes;
- sorted evidence references;
- subject identity;
- patch algorithm, operations, patch hash, and deterministic claims.

It intentionally excludes timestamps, policy outcome, review state, and readiness so a review transition does not create a second proposal identity.

```text
proposal_id = "kfm:ai-change-proposal:" + SHA-256(RFC8785-JCS(identity_projection))
```

## Compare-and-set patch profile

Only object-member paths are admitted. Array traversal and root replacement are not part of v1.

### Operation rules

| Operation | Before | After | First application |
|---|---|---|---|
| `add` | absent | present | create the object member |
| `replace` | present | present with a different value | replace exact pre-image value |
| `remove` | present | absent | delete the object member |

Additional invariants:

- operation paths are strictly lexicographically sorted;
- each path is unique;
- no path may be an ancestor or descendant of another operation path;
- each parent container must be a JSON object;
- a no-op operation is denied;
- an unexpected current value is denied as a compare-and-set conflict;
- reapplying the patch to the verified post-image must make no change;
- the input object must remain unmodified by validation.

These rules make the fixture patch deterministic, minimal, and idempotent without pretending to solve arbitrary JSON Patch semantics.

## Policy projection

`policy_projection` does not evaluate policy. It records a decision reference, a finite outcome, required obligations, and obligations asserted as satisfied.

- `ALLOW` does not make the proposal applicable.
- `HOLD` requires readiness `HOLD`.
- `DENY` requires readiness `DENY`.
- satisfied obligations must be an exact subset of required obligations;
- each obligation is compared by canonical JSON value, not only by code;
- an allowed proposal with unresolved obligations remains on `HOLD`.

## Human attestation projection

Human attestation is always required in this profile.

| State | `review_record_ref` | Consequence |
|---|---|---|
| `PENDING` | `null` | readiness cannot exceed `HOLD` |
| `APPROVED` | non-empty separate review reference | may participate in readiness calculation |
| `REJECTED` | non-empty separate review reference | readiness is `DENY` |

The validator checks shape and internal consistency only. It does not authenticate the reviewer or dereference the review record.

## Readiness derivation

Readiness is derived from policy, obligation, and review projections.

| Policy | Obligations | Review | Expected disposition |
|---|---|---|---|
| `ALLOW` | satisfied | `APPROVED` | `READY_FOR_STEWARD_APPLY` |
| `ALLOW` | unresolved | any | `HOLD` |
| `ALLOW` | satisfied | `PENDING` | `HOLD` |
| `ALLOW` | satisfied | `REJECTED` | `DENY` |
| `HOLD` | any | any | `HOLD` |
| `DENY` | any | any | `DENY` |

The matching reason-code set is deterministic and sorted. Readiness never overrides the all-false permission block.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Schema, identities, patch mechanics, policy/review projections, readiness, and no-effect boundaries agree. |
| `DENY` | The proposal is contradictory, non-deterministic, non-idempotent, hash-invalid, over-authoritative, or otherwise nonconforming. |
| `ERROR` | The proposal or subject could not be read or parsed safely. |

A `PASS` creates no approval or effect.

## Fixture profile

The fixture family contains:

- a synthetic subject;
- valid ready, pending-review, and policy-denied proposals;
- negative hash, path, obligation, readiness, and authority cases;
- an expected-findings manifest.

Fixtures are synthetic and must not be treated as Kansas facts, model outputs, policy decisions, human approvals, or release records.

## Validation

Focused validation:

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_ai_change_proposal.py' \
  --verbose

python tools/validators/governance/validate_ai_change_proposal.py --fixtures
```

Single proposal validation:

```bash
python tools/validators/governance/validate_ai_change_proposal.py \
  --proposal fixtures/contracts/v1/governance/ai_change_proposal/valid/valid_ready.json \
  --subject fixtures/contracts/v1/governance/ai_change_proposal/subjects/sbase.json
```

## Trust boundary

This profile does not:

- call an AI model or preserve model chain-of-thought;
- evaluate OPA, Conftest, or another policy engine;
- generate or validate a cryptographic signature;
- resolve evidence;
- write to Git, GitHub, a database, object storage, or a lifecycle directory;
- apply a patch;
- grant merge, promotion, release, deployment, publication, or public-use authority;
- make a decision about a real person, place, dataset, map layer, or Kansas condition.

## Rollback

The implementation is additive. Before merge, close the pull request and delete the feature branch. After an authorized merge, revert the implementation commit or merge commit. No source deactivation, data migration, lifecycle reprocessing, release withdrawal, cache purge, or public correction is required because the profile creates no live state or published product.
