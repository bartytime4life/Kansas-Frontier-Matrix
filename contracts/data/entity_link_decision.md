<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/entity-link-decision
title: EntityLinkDecisionCandidate Contract
type: semantic-contract; entity-resolution; cross-domain; fixture-first
version: v0.1.0
status: proposed; no-canonical-mutation
owners: OWNER_TBD — Data steward · Domain stewards · Evidence steward · Contracts steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; data; entity-resolution; candidate-only
related:
  - ./README.md
  - ../../schemas/contracts/v1/data/entity_link_decision.schema.json
  - ../../fixtures/contracts/v1/data/entity_link_decision/
  - ../../tools/validators/validate_entity_link_decision.py
  - ../../tests/validators/test_validate_entity_link_decision.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, entity-resolution, link-score, explainability, evidence, review, no-auto-merge]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EntityLinkDecisionCandidate

> An `EntityLinkDecisionCandidate` records one candidate pair, reproducible matching features, deterministic checks, evidence references, thresholds, conflicts, and a proposed routing action. It never merges canonical entities and never creates truth, evidence, policy, review, release, or publication authority.

## Source-derived need

Pages 4–8 of *New Ideas 3-19-26* describe an entity-resolution pipeline that:

1. generates candidate pairs and link scores;
2. preserves explain features;
3. applies deterministic tie-break checks;
4. routes high-confidence pairs, ambiguous pairs, and rejected pairs differently;
5. attaches evidence and delta/run receipts; and
6. keeps policy, review, observability, secrets, and rollback visible.

This slice implements the smallest common artifact: the candidate link decision. It deliberately does not add Splink, Dedupe, a canonicalizer, an entity merge writer, OPA, telemetry, Vault, signing, or a reviewer UI.

## Directory Rules basis

The object is data-family process memory shared across domains, so semantic meaning belongs under `contracts/data/`. Machine shape, fixtures, executable validation, tests, read-only workflow orchestration, and authoring provenance remain in their existing responsibility roots. No new root or parallel authority is introduced.

## Pair and evidence semantics

- Endpoints use stable synthetic `kfm://record/...` references and content hashes.
- A pair is unordered for identity; fixtures enforce lexicographic endpoint order.
- A record cannot link to itself.
- Both endpoints must use the same entity type.
- Features and deterministic checks are sorted, unique, and explainable.
- A `PROPOSE_MERGE` candidate requires at least two canonical EvidenceRefs.
- EvidenceRefs are pointers only; this candidate does not resolve them into an EvidenceBundle.

## Routing actions

| Action | Meaning |
|---|---|
| `PROPOSE_MERGE` | Score meets the merge-candidate threshold, every required deterministic check passes, evidence is sufficient, and no conflict flag is set. This still does **not** merge anything. |
| `REVIEW` | Score is in the review band or a required check remains unresolved without a rights/sensitivity/identity conflict. |
| `REJECT` | Score is below the review threshold or a required deterministic check fails. |
| `HOLD` | Licensing, sensitivity, identity, evidence, profile, or other governance conflict prevents safe routing. |

The source packet's “auto-merge” suggestion is narrowed here to `PROPOSE_MERGE`. KFM canonical mutation remains a separate policy- and review-bearing transition.

## Deterministic identity

For the fixture profile:

1. remove `decision_id` and `spec_hash`;
2. serialize canonical JSON with sorted keys, compact separators, finite numbers, and array order preserved;
3. compute SHA-256;
4. set `spec_hash = "sha256:<hex>"`;
5. set `decision_id = "kfm://candidate/entity-link/<hex>"`.

Any change to pair identity, features, score, thresholds, checks, evidence, flags, action, or governance changes the candidate identity.

## Governance boundary

Every v1 candidate fixes:

- `auto_merge_performed = false`;
- `canonical_mutation_performed = false`;
- `authority_created = false`;
- `policy_evaluated = false`;
- `human_review_completed = false`;
- `promotion_authorized = false`;
- `release_state = HOLD`;
- `public_use_allowed = false`.

A green result proves only local candidate shape and consistency. It does not prove two records refer to the same real-world entity.

## Rollback

Before merge, close the pull request and abandon the branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/receipt commit. No canonical entity, graph, source, policy decision, release, deployment, or published artifact requires restoration.

[Back to top](#top)
