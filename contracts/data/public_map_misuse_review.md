<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/public-map-misuse-review-candidate
title: PublicMapMisuseReviewCandidate Semantic Contract
type: semantic-contract; fixture-profile; cartographic-review
version: 1.0.0
status: proposed; inactive; fixture-only; NEEDS STEWARD REVIEW
owners: OWNER_TBD — Data steward · Cartography steward · Evidence steward · Review steward · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: public; data; maps; misuse-review; evidence-first; non-authoritative
tags: [kfm, contract, data, map, cartography, review, omission, symbology, scale, framing, abstain]
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/data/public_map_misuse_review.schema.json
  - ./cartographic_omission_disclosure.md
  - ./layer_legend_disclosure.md
  - ../evidence/representation_fitness_assessment.md
notes:
  - "Implements a bounded candidate from Pass 18 card KFM-P18-INV-352."
  - "The profile records review declarations only; it does not inspect, mutate, render, approve, release, or publish a map."
[/KFM_META_BLOCK_V2] -->

# PublicMapMisuseReviewCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile records whether a public-facing map candidate has been reviewed for ways that selection, framing, scale, symbology, or omission could overstate evidence strength. It creates no cartographic, evidence, policy, review, release, publication, or public-use authority.

## Purpose

Evidence-first publication can still mislead when visual encoding implies more precision, completeness, or authority than the evidence supports. `PublicMapMisuseReviewCandidate` makes five communication-risk dimensions explicit before a map can be considered by a separate review or release plane:

1. `SELECTIVITY` — feature, geography, or record selection;
2. `FRAMING` — viewport, comparison, annotation, or narrative context;
3. `SCALE_PRECISION` — display scale or apparent positional/measurement precision;
4. `SYMBOLOGY` — color, size, class, icon, or emphasis choices;
5. `OMISSION` — absent layers, categories, caveats, or known gaps.

The declaration composes existing governed references instead of duplicating their meaning: representation fitness, cartographic omission disclosure, and layer legend disclosure remain separate objects.

## Object meaning

The candidate binds one immutable map candidate digest to a resolved purpose and evidence scope, a declared audience and consequence tier, three prerequisite references, exactly one review check per required dimension, a conclusion, correction/rollback pointers, and an all-false authority block.

`profile_spec_hash` is the lowercase SHA-256 digest of this contract's exact bytes. The validator checks that binding but does not authenticate authorship.

## Deterministic outcomes

| Outcome | Bounded meaning |
|---|---|
| `PASS` | Shape and hash bindings are valid; all prerequisites resolve; all five dimensions are canonical, complete, and clear; the declaration is `COMPLETE` and `READY_FOR_REVIEW`. |
| `ABSTAIN` | A prerequisite, check state, materiality, or conclusion is unresolved or incomplete. |
| `DENY` | The declaration has a concern, incomplete dimension coverage, incoherent conclusion, noncanonical ordering, missing high-consequence review evidence, or misleading material-concern disclosure. |
| `ERROR` | JSON, schema, timestamp, source-card, profile-hash, or authority constraints fail. |

These outcomes classify the fixture declaration only. `PASS` means “eligible for separate human review,” not “safe,” “approved,” “released,” or “published.”

## Fail-closed rules

- All five dimensions must appear exactly once and be sorted by `check_id`.
- Evidence and review references must be sorted and unique.
- Any unresolved purpose, evidence scope, or prerequisite produces `ABSTAIN`.
- Any `UNKNOWN` check state or materiality, or an `INCOMPLETE` conclusion, produces `ABSTAIN`.
- Any `CONCERN` produces `DENY`. A material concern must also name a disclosure surface, remediation reference, and review reference; missing those is separately reported.
- Every high-consequence check must carry a review reference, including checks declared clear.
- A complete, all-clear candidate must declare `READY_FOR_REVIEW`; an unresolved candidate must declare `HOLD`; a concern-bearing candidate must declare `DENY`.
- Every authority claim is literally `false` in the schema.

## Non-authority boundary

The validator does not resolve any reference, decide evidence strength, assess the actual map, determine materiality, edit a style or layer, conduct accessibility testing, create a `ReviewRecord`, make a `PolicyDecision`, promote data, issue a `ReleaseManifest`, deploy, publish, or authorize public use. Human review and release gates remain external and mandatory.

## Rollback

Rollback is additive: remove the inactive packet and its path-scoped workflow. No runtime or data migration is required because no consumer is wired by this proposal.
