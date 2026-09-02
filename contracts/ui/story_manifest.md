<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-story-manifest
title: contracts/ui/story_manifest.md — UI StoryManifest Composite Trust Contract
type: semantic-contract
version: v1.0.0
status: proposed; fixture-only; public-safe-projection; evidence-dependent; release-gated
owners: OWNER_TBD — UI steward · Story steward · Evidence steward · Policy steward · Release steward · Accessibility steward
created: NEEDS VERIFICATION — scaffold predates this closure
updated: 2026-08-10
policy_label: public; contracts; ui; story-manifest; composite-inheritance; no-sovereign-truth
tags: [kfm, contracts, ui, StoryManifest, StoryNode, composite, trust-inheritance, fail-closed]
related:
  - ./story_node.md
  - ../story/README.md
  - ../../schemas/contracts/v1/ui/story_manifest.schema.json
  - ../../fixtures/ui/story_manifest/cases.json
  - ../../tools/validators/ui/validate_story_manifest.py
  - ../../docs/intake/exploratory/pass-20-story-manifest-inheritance-source-map.md
notes:
  - "This revision replaces the confirmed permissive schema stub with a closed fixture-only profile."
  - "The bounded rule is deterministic: every composite dimension inherits the least permissive constituent posture and the effective manifest state cannot be more permissive than any constituent."
  - "This contract does not resolve refs, execute policy, approve review or release, render a UI, publish, or create story truth."
[/KFM_META_BLOCK_V2] -->

# UI StoryManifest composite trust contract

> `StoryManifest` is a public-safe, fixture-only projection for assembling ordered `StoryNode` references. It preserves the least permissive constituent trust posture. It is not story truth, policy, review, release, or publication authority.

**Status:** PROPOSED  
**Profile:** `kfm.ui.story-manifest.public-safe.v1`  
**Machine shape:** `schemas/contracts/v1/ui/story_manifest.schema.json`  
**Execution:** deterministic, offline, synthetic fixtures only

## Decision

The repository now closes one bounded Pass 20 gap: composite story inheritance is executable instead of prose-only.

For each manifest:

1. constituent nodes are ordered by unique `order_index` values;
2. each node contributes a declared finite state, outcome, reason code, and trust snapshot;
3. each trust dimension is reduced with an explicit least-permissive precedence table;
4. the manifest state/outcome is the worst effective constituent state;
5. `limiting_node_refs` and `reason_codes` expose the constituents and reasons that set that result;
6. correction and replacement links are mandatory when the composite is corrected, withdrawn, or superseded.

The fixture profile never dereferences a node. It validates a bounded snapshot only.

## Finite posture

Manifest state precedence, from most to least permissive:

| Rank | State | Outcome |
|---:|---|---|
| 0 | `READY` | `ANSWER` |
| 1 | `PARTIAL` | `ABSTAIN` |
| 2 | `ABSTAINED` | `ABSTAIN` |
| 3 | `SUPERSEDED` | `ABSTAIN` |
| 4 | `BLOCKED` | `DENY` |
| 5 | `ERROR` | `ERROR` |

An effective node can be made less permissive by its trust snapshot:

- `policy=ERROR` forces `ERROR`;
- `policy=DENY`, unresolved/withheld rights, restricted/unknown sensitivity, or a withdrawn release without a supersession posture forces `BLOCKED`;
- `correction=SUPERSEDED` with `release=WITHDRAWN` forces `SUPERSEDED`;
- generalized rights/sensitivity, `policy=ABSTAIN`, pending review, unreleased support, or stale/unknown freshness forces at least `PARTIAL`.

The validator rejects a constituent whose declared state/outcome is more permissive than its own snapshot.

## Composite trust reduction

Each dimension has a fixed order. The manifest must declare the maximum observed rank.

| Dimension | Most permissive → least permissive |
|---|---|
| rights | `CLEARED`, `GENERALIZED`, `WITHHELD`, `UNRESOLVED` |
| sensitivity | `PUBLIC`, `GENERALIZED`, `RESTRICTED`, `UNKNOWN` |
| policy | `ALLOW`, `ABSTAIN`, `DENY`, `ERROR` |
| review | `REVIEWED`, `NOT_APPLICABLE`, `PENDING` |
| release | `RELEASED`, `UNRELEASED`, `WITHDRAWN` |
| freshness | `CURRENT`, `STALE`, `UNKNOWN` |
| correction | `NONE`, `CURRENT`, `CORRECTED`, `SUPERSEDED` |

This ordering is a validation profile, not a repository-wide policy decision.

## Required public-safe shape

| Field | Meaning |
|---|---|
| `profile`, `id`, `version`, `spec_hash` | Closed profile and content-addressed identity. |
| `story_ref`, `title`, `accessibility_summary` | Public-safe display identity and assistive summary. |
| `state`, `outcome` | Derived composite posture. |
| `constituents` | Ordered bounded StoryNode snapshots; no body or source payload. |
| `trust_state` | Least-permissive per-dimension composite. |
| `reason_codes`, `limiting_node_refs` | Visible explanation of the effective result. |
| `support` | Governed evidence, citation, policy, release, review, and correction references. |
| `caveats` | Public-safe limitations that must remain visible. |
| `supersession` | Replacement manifest and public note when superseded. |
| `authoritative`, `projection_only` | Fixed boundary flags: `false`, `true`. |

## Invariants

- The schema is closed; raw prose bodies, claims, source payloads, coordinates, and geometry are out of profile.
- Constituents and governed ref arrays are sorted and unique.
- `READY/ANSWER` requires evidence, citation, policy, release, and review refs, and every constituent must be effectively ready.
- `limiting_node_refs` is empty only for `READY`; otherwise it is exactly the sorted set of nodes at the worst effective rank.
- `reason_codes` is `SUPPORTED` for `READY`; otherwise it is the sorted unique set of limiting-node reason codes.
- `CORRECTED` requires correction refs.
- `SUPERSEDED` or `WITHDRAWN` requires correction refs and a non-self replacement manifest.
- Identity is the repository JCS SHA-256 over the document without `id` and `spec_hash`.
- Validation is bounded, deterministic, and performs no network or ref resolution.

## Non-effects

A passing fixture does not:

- prove a narrative claim or evidence item;
- validate a citation;
- execute or approve policy;
- approve review, promotion, release, deployment, public use, or publication;
- fetch, resolve, or expose a StoryNode body;
- authorize a story player or any external write.

## Evidence and truth labels

| Evidence | Label | Use |
|---|---|---|
| Pass 20 Part 2 composite-manifest recommendation | `CONFIRMED` | Names the missing schema and visible worst-state inheritance behavior. |
| Existing `StoryManifest` contract and permissive schema stub | `CONFIRMED` | Establishes the accepted UI responsibility root and closure target. |
| Existing executable `StoryNode` trust profile | `CONFIRMED` | Supplies the adjacent finite state/trust vocabulary. |
| This composite reduction profile | `PROPOSED` | Bounded fixture behavior pending human review. |

The exact source mapping and exclusions are recorded in `docs/intake/exploratory/pass-20-story-manifest-inheritance-source-map.md`.

## Rollback

Rollback is file-scoped: revert this contract, schema, fixtures, validator, tests, workflow, source map, and generated receipt together. No data migration, connector state, release state, deployment, or publication is created by this proposal.
