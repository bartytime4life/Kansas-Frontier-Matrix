<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/composed-claim-dependency-closure
title: Composed Claim Dependency Closure Candidate Contract
type: semantic-contract; fixture-first; no-network
version: v0.1.0
status: proposed; fixture-only; no-live-resolution
owners: OWNER_TBD — Evidence steward · Contracts steward · Validation steward · Runtime steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; evidence; composed-claim; dependency-closure; no-publish
related:
  - ./README.md
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ./runtime_evidence_resolution.md
  - ../../schemas/contracts/v1/evidence/composed_claim_dependency_closure.schema.json
  - ../../fixtures/contracts/v1/evidence/composed_claim_dependency_closure/
  - ../../tools/validators/validate_composed_claim_dependency_closure.py
  - ../../tests/validators/test_validate_composed_claim_dependency_closure.py
  - ../../docs/intake/exploratory/new-ideas-4-23-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, composed-claim, dependency-graph, closure, qualified, abstain, deny, error, fixture-only]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Composed Claim Dependency Closure Candidate Contract

> A fixture-first evidence contract for declaring the dependency roles of one composed claim and deriving one finite closure outcome without performing live evidence resolution, policy evaluation, review, release, deployment, or publication.

## Source-derived gap

The governed source map for *New Ideas 4-23-26* identifies multi-bundle composed claims as a remaining connective gap. Existing KFM surfaces describe `EvidenceRef`, `EvidenceBundle`, runtime evidence resolution, and finite response envelopes, but the inspected source map did not confirm one common contract for **required**, **optional**, **alternative**, and **mutually exclusive** evidence dependencies across a single claim.

The packet's all-required examples remain useful pressure, but direct transfer would be too narrow and would recreate stale packet paths. This contract adopts the source map's smaller continuation: a contract-only dependency graph, synthetic closure fixtures, deterministic validation, and five finite outcomes.

## Bounded context

A `ComposedClaimDependencyClosureCandidate` may describe:

- one synthetic claim statement and bounded spatial/temporal scope;
- evidence roles and expected `EvidenceRef`/spec-hash identities;
- synthetic resolution observations for each dependency;
- alternative groups with minimum and maximum resolved cardinality;
- exclusion groups that prevent mutually incompatible evidence roles from simultaneously resolving;
- deterministic graph, closure, revision, and record identities; and
- one derived closure outcome.

It must not:

- dereference a live `EvidenceRef`;
- assert that an `EvidenceBundle` exists or is admissible;
- make a `PolicyDecision`, `ReviewRecord`, `PromotionReceipt`, or `ReleaseManifest`;
- turn a fixture result into a public claim;
- expose source payload bytes, exact geometry, credentials, internal lifecycle paths, or sensitive facts; or
- authorize lifecycle mutation, promotion, release, deployment, publication, or public use.

## Dependency roles

| Requirement | Meaning | Closure effect |
|---|---|---|
| `REQUIRED` | The claim cannot stand without this role. | `UNRESOLVED` produces `ABSTAIN`; `DENIED` produces `DENY`; `ERROR` produces `ERROR`. |
| `OPTIONAL` | The role can strengthen or qualify the claim but is not mandatory. | `UNRESOLVED` or `DENIED` produces `QUALIFIED` after every required and alternative condition closes. |
| `ALTERNATIVE` | The role participates in exactly one declared alternative group. | The group must meet its minimum resolved count without exceeding its maximum. |

Alternative roles are not silently treated as optional. Every `ALTERNATIVE` dependency must appear in exactly one alternative group, and every alternative-group member must be declared `ALTERNATIVE`.

## Alternative and exclusion groups

An alternative group declares:

```text
minimum_resolved <= number of RESOLVED members <= maximum_resolved
```

If the minimum is not met:

- all candidates denied → `DENY`;
- otherwise → `ABSTAIN`.

If the maximum is exceeded, the graph returns `ERROR`; it does not select a preferred source silently.

An exclusion group declares that at most one member may resolve. A violation returns `ERROR` with a visible mutual-exclusion reason. Exclusion groups are closure constraints, not policy decisions.

## Finite outcomes

| Outcome | Render allowed | Meaning in this profile |
|---|---:|---|
| `SUPPORTED` | yes | Required dependencies resolve, alternative groups close, exclusion rules hold, and optional dependencies are available. |
| `QUALIFIED` | yes | Required and alternative closure succeeds, but one or more optional dependencies are unavailable. |
| `ABSTAIN` | no | A required dependency or viable alternative remains unresolved. |
| `DENY` | no | A required dependency is denied or every member of an unmet alternative group is denied. |
| `ERROR` | no | A resolver error, alternative-cardinality violation, or mutual-exclusion violation prevents safe evaluation. |

`QUALIFIED` is not partial truth by default. It is a bounded result whose unavailable optional roles remain visible. A later runtime or policy consumer must still decide whether a qualified claim is usable in its own context.

## Deterministic identity

```text
dependency_graph_hash =
  SHA-256(canonical {
    claim,
    dependencies projected to role/requirement/ref/expected_spec_hash,
    alternative_groups,
    exclusion_groups
  })

closure_id =
  kfm://candidate/evidence/composed-claim/<dependency_graph_hash-hex>

previous_closure_ref =
  null at revision 1, otherwise <closure_id>/revision/<revision-1>

spec_hash =
  SHA-256(canonical top-level record excluding spec_hash)
```

The validator uses recursively sorted, whitespace-free JSON with finite JSON numbers. This profile is a deterministic repository fixture profile, not a claim that the project has adopted a universal canonicalization standard for every object family.

## Synthetic resolution observations

Each dependency carries one synthetic state:

```text
RESOLVED | UNRESOLVED | DENIED | ERROR
```

A `RESOLVED` dependency must bind:

- a synthetic `bundle_id`;
- an `actual_spec_hash` equal to the declared expected spec hash;
- a synthetic promotion-receipt reference; and
- no reason code.

Every non-resolved state carries no bundle, digest, or promotion reference and must carry a reason code. The validator checks internal consistency only; it does not authenticate the referenced object or assert that promotion occurred.

## Public-safety and authority boundary

Every v1 fixture fixes:

```text
mode = FIXTURE_ONLY
fail_closed = true
live_evidence_resolution_performed = false
policy_decision_authority = false
review_authority = false
release_authority = false
deployment_authority = false
publication_authority = false
public_use_allowed = false
```

The validator rejects exact-geometry keys, secret-bearing keys, and references into RAW, WORK, QUARANTINE, or PUBLISHED lifecycle paths. Fixtures use synthetic, non-joinable identifiers only.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. This slice follows existing responsibility roots:

- semantic meaning: `contracts/evidence/`;
- machine shape: `schemas/contracts/v1/evidence/`;
- synthetic examples: `fixtures/contracts/v1/evidence/`;
- executable validation: `tools/validators/`;
- enforceability: `tests/validators/`;
- hosted orchestration: `.github/workflows/`; and
- AI authoring provenance: `data/receipts/generated/`.

No new root or parallel contract, schema, policy, source registry, evidence store, proof store, receipt authority, release authority, or publication path is created.

## Validation

```bash
python -m pytest -q -p no:cacheprovider \
  tests/validators/test_validate_composed_claim_dependency_closure.py

python tools/validators/validate_composed_claim_dependency_closure.py \
  --fixtures
```

A green result proves only closed schema shape, deterministic synthetic identity, declared role/group consistency, exact fixture polarity, and derived finite closure outcomes.

## Non-goals and later work

This v1 candidate deliberately does not add:

- `packages/evidence/` runtime code;
- Evidence Drawer or Focus Mode rendering;
- policy composition;
- real EvidenceRef/EvidenceBundle lookup;
- catalog/proof/release integration;
- claim generation; or
- public API behavior.

A later implementation may consume this meaning only after current runtime ownership, policy integration, compatibility with existing envelopes, and reviewer authority are verified.

## Rollback

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/receipt slice through a reviewed pull request. No source, evidence bundle, lifecycle store, public API, deployment, release, cache, or published object requires cleanup.

[Back to top](#top)
