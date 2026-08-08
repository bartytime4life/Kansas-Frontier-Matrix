<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/output-lane-split-manifest
title: OutputLaneSplitManifest Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Data steward · Evidence steward · Policy steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; fixture-only; no-network; non-authoritative
owning_root: contracts/
responsibility: Define a review-before-authority routing manifest for generated proof-of-concept outputs.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/data/output_lane_split_manifest.schema.json
  - ../../fixtures/contracts/v1/data/output_lane_split_manifest/cases.json
  - ../../tools/generators/build_output_lane_split.py
  - ../../tests/generators/test_build_output_lane_split.py
  - ../../docs/intake/exploratory/pass-32-output-lane-splitter-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [data, output-routing, generator, review, fixture-only, pass-32]
notes:
  - "This contract defines routing meaning only. It is not a lifecycle store, policy decision, receipt, proof, release, or publication record."
  - "The generator indexes opaque references and never moves or copies payload bytes."
[/KFM_META_BLOCK_V2] -->

# OutputLaneSplitManifest Contract

## Status

**PROPOSED, inactive, fixture-only.** This contract adapts Pass 32 card
`KFM-P32-PROG-0020` into a bounded review-routing object. It does not activate
a source, ingest data, change lifecycle state, create policy, promote, release,
deploy, publish, or authorize public use.

## Purpose

Generated proof-of-concept outputs often have different accountability and review
needs. `OutputLaneSplitManifest` prevents them from being reviewed as one
undifferentiated bundle by assigning each opaque artifact reference to exactly one
logical lane before review:

| Lane | Semantic role | Authority boundary |
|---|---|---|
| `FEATURE_VECTOR` | `ANALYSIS_DERIVATIVE` | Derived analysis input; never evidence or a public claim by itself. |
| `SCORECARD` | `REVIEW_SCORECARD` | Review aid; never approval or proof. |
| `POLICY_REPORT` | `POLICY_REVIEW_CANDIDATE` | Candidate report; never a `PolicyDecision`. |
| `RECEIPT` | `PROCESS_MEMORY_RECEIPT` | Process memory reference; never proof, release, or truth. |
| `PREFILTER` | `PREFILTER_DECISION_CANDIDATE` | Candidate triage output; never source admission or promotion. |

The manifest is a **routing plan**, not a file move. The companion generator
emits deterministic lane indexes from opaque references. It does not read, copy,
transform, redact, or publish referenced payload bytes.

## Required closure

A valid manifest:

1. declares all five lanes in canonical order;
2. contains at least one output for every lane;
3. assigns each artifact reference to exactly one output and one lane;
4. binds each output to a SHA-256 digest and media type;
5. maps each lane to its required logical role;
6. orders outputs by canonical lane order and then `output_id`;
7. records `PENDING` review and `DRY_RUN` / `DENY` execution and network modes;
8. fixes source activation, network, RAW admission, promotion, release, and
   publication authority to `false`; and
9. binds the complete manifest through a canonical `spec_hash`.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed synthetic shape and routing semantics pass. |
| `DENY` | Schema or bounded semantic rules reject the manifest. |
| `ERROR` | The validator cannot safely read or evaluate the input. |

A `PASS` does not make any referenced output valid, evidentiary, policy-approved,
reviewed, released, public-safe, or published.

## Generator behavior

`tools/generators/build_output_lane_split.py` is no-network and deterministic.

- Default invocation prints one `OutputLaneSplitResult` and writes nothing.
- `--write --output-dir <empty-dir>` writes five lane indexes and one summary.
- The output directory must be explicit, real, and empty.
- Existing files are never overwritten.
- Payload bytes are never moved or copied.
- Every emitted index says review is required and write authority is false.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Semantic meaning belongs in
`contracts/data/`; machine shape belongs in `schemas/contracts/v1/data/`;
deterministic generation belongs in `tools/generators/`; fixtures and tests remain
under their responsibility roots; exploratory source adaptation belongs in
`docs/intake/exploratory/`; authoring receipts remain under
`data/receipts/generated/`. No new root or parallel authority is created.

## Rollback

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the additive commit. The slice creates no live data,
policy decision, release, API, cache, or public artifact.
