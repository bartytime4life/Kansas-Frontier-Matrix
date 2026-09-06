<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/examples/story-decks/readme
title: `examples/story_decks/` — Evidence-Gated Story Deck Examples
type: readme; nested-example-lane; non-authoritative-demonstration-boundary
version: v0.3.0
status: repository-grounded currentness refresh; STATIC_WALKTHROUGH; non-authoritative; validation-bounded; do-not-publish
owners: NEEDS VERIFICATION — examples steward and listed specialist reviewers
updated: 2026-09-06
supersedes: v0.2.0 content at the same path; no operational object, runtime behavior, release, or publication state
prepared_under_prompt: user-requested story-deck README currentness update
policy_label: public-review; synthetic-first; fail-closed; cite-or-abstain; correction-aware
current_path: examples/story_decks/README.md
review_packet_id: kfm-md-story-decks-currentness-20260906
truth_posture: >
  CONFIRMED exact path, current parent examples contract, accepted Directory Rules decision through
  ADR-0029, current direct directory inventory, and bounded linked story-source evidence / PROPOSED
  normalized lane contract and future example-validator profile / UNKNOWN executable child payloads,
  runtime parity, deployed consumers, and production effects / NEEDS VERIFICATION owners, child
  schema conformance, validator wiring, fixtures, CI, host rendering, correction propagation,
  and retirement drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c
  current_target_blob_before_patch: b7735f58aa1605abaf94165f352cee4f55a69b67
  prior_v0.2.0_blob: 5235af859ea076c19dad4750f0e92947690bf337
  parent_examples_blob: 749dfd2f387589f8ef1edd639a13f066eb2d2958
  child_deck_blob: a65b225e8498e518f0bb955004e39e4e2a466245
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  story_architecture_blob: 893ccbd0cc9a10edd892462c74119e4d5d9284ef
  published_stories_readme_blob: eba161a2740417be017a7e4514d6a09d3b6ce24c
  inventory_method: exact target read plus pinned direct-directory listing and bounded linked-file reads; no example execution or runtime inspection
notes:
  - "Directory Rules v2 bytes are adopted by accepted ADR-0029 even though the pinned doctrine file retains PROPOSED_FOR_ADOPTION in its internal control block."
  - "The current direct listing contains README.md and kansas_drought_2012.md; recursive/non-Markdown completeness remains unverified."
  - "This is a Markdown-only documentation refresh; it creates no fixture, test, schema, policy, proof, receipt, route, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `examples/story_decks/` — Evidence-Gated Story Deck Examples

> **One-line purpose.** Teach story node sequencing, camera/time/layer state, evidence callouts, finite outcomes, Reality Boundary Notes, accessibility, and release gates while keeping illustrative plans separate from StoryManifest/StoryNode contracts, runtime, and published payloads.

[![Status: static walkthrough](https://img.shields.io/badge/status-STATIC__WALKTHROUGH-f59e0b?style=flat-square)](#status)
[![Authority: example only](https://img.shields.io/badge/authority-example%20only-b42318?style=flat-square)](#authority-level)
[![Publication: denied](https://img.shields.io/badge/publication-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> `examples/` is canonical for demonstrations, not for the objects or behavior demonstrated. A polished file, merged pull request, parser pass, or screenshot does not prove source authority, runtime parity, evidence closure, policy permission, release approval, or KFM publication.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Contract](#example-contract) · [Guardrails](#guardrails) · [Inventory](#current-bounded-inventory) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

Teach story node sequencing, camera/time/layer state, evidence callouts, finite outcomes, Reality Boundary Notes, accessibility, and release gates.

This lane exists to make review and learning faster. It must not become a parallel contract, schema, policy, fixture, test, proof, receipt, source registry, runtime, release, or publication authority.

## Authority level

**Non-authoritative story example lane; story contracts, runtime, published payloads, and release decisions remain outside examples.**

Operational meaning remains owned by the relevant `docs/`, `contracts/`, `schemas/`, `policy/`, implementation, `tests/`, `fixtures/`, `data/`, and `release/` surfaces.

The current story architecture describes public-safe StoryManifest/StoryNode projections and an app-local projection consumer, while live transport, rendered playback, evidence dereference, policy execution, release, deployment, and publication remain outside this lane's verified boundary. This README may illustrate those handoffs but cannot establish them.

## Status

| Field | Bounded result |
|---|---|
| Path | `examples/story_decks/README.md` |
| Version | `v0.3.0` |
| Evidence base | `main@4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c` |
| Base target blob before this patch | `b7735f58aa1605abaf94165f352cee4f55a69b67` |
| Prior v0.2.0 blob | `5235af859ea076c19dad4750f0e92947690bf337` |
| Direct inventory | `CONFIRMED BOUNDED` — README plus `kansas_drought_2012.md` |
| Recursive/non-Markdown inventory | `UNKNOWN` beyond the pinned direct listing |
| Story implementation relation | `BOUNDED` — story architecture is implementation-partial/projection-only; no publisher is verified here |
| Executable entrypoint / observed run | `NOT ESTABLISHED` |
| Public/release readiness | `DENY BY PLACEMENT` |

## What belongs here

- synthetic deck outlines and node walkthroughs
- evidence-callout and Evidence Drawer handoff examples
- negative states for missing evidence, policy denial, stale layers, plugin denial, or runtime error
- Reality Boundary Note and 2D/3D parity examples
- release-readiness and accessibility review checklists

Every new file must be visibly synthetic or safely transformed, name its learning objective, identify the operational home it does not replace, and declare its expected finite outcome.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| StoryManifest/StoryNode contracts and schemas | `contracts/ui/` and `schemas/contracts/v1/ui/` |
| released story payloads, packages, or latest indexes | `data/published/stories/` after release |
| unreleased authoring drafts or generated narration candidates | governed WORK/QUARANTINE story lanes |
| evidence/proof, receipts, policy, release, UI/API runtime, plugins, or schemas | their canonical roots |
| sensitive detail hidden only by camera, style, zoom, or narration | transform before publication or deny |
| generated narration presented as evidence | cite resolvable evidence or abstain |

## Inputs

Story architecture, synthetic map/time/layer states, example evidence and policy refs, and public-safe narrative slots.

Input provenance, real-versus-synthetic status, rights, sensitivity, and the operational object being illustrated must be explicit.

## Outputs

Static story-plan examples marked `not_released`; never published story payloads.

Outputs may be reviewed, corrected, or proposed for separate fixture/test graduation. They do not become operational merely by being copied.

## Validation

- Confirm consequential story claims resolve to example evidence refs or default to `ABSTAIN`.
- Confirm camera/style/3D cannot substitute for sensitivity transforms or evidence.
- Confirm malformed nodes, missing dependencies, route/plugin/runtime failures yield `ERROR`.
- Confirm sensitive or unreleased nodes yield `DENY`, `HOLD`, or `ABSTAIN`.
- Validate links, JSON sketches, Mermaid, reality-boundary notes, and accessibility states.

No examples-specific runner or complete validator was verified. A Markdown/source check proves only the declared static scope.

## Review burden

Examples/docs plus story, UI/map, evidence, policy/sensitivity, release, accessibility, and affected domain reviewers.

CODEOWNERS routing is not stewardship, approval evidence, policy permission, or release authorization.

## Related folders

- [Parent examples contract](../README.md)
- [Kansas Drought 2012 deck](kansas_drought_2012.md)
- [Story architecture](../../docs/architecture/story/README.md)
- [StoryManifest contract](../../contracts/ui/story_manifest.md)
- [StoryNode contract](../../contracts/ui/story_node.md)
- [StoryManifest schema](../../schemas/contracts/v1/ui/story_manifest.schema.json)
- [StoryNode schema](../../schemas/contracts/v1/ui/story_node.schema.json)
- [Published story lane](../../data/published/stories/README.md)
- [Published root](../../data/published/README.md)

## ADRs

Placement follows accepted ADR-0029 and the `DIR-ROOT-EXAMPLES` root registration without granting this lane authority. Renderer, story contract, public-client, and release decisions remain governed outside examples; this lane accepts none.

## Last reviewed

- **Date:** 2026-09-06
- **Evidence boundary:** `main@4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c`
- **Method:** exact target read, pinned direct-directory listing, and bounded reads of the parent contract, Directory Rules, ADR-0029, root registry, child deck, story architecture, and published-story README
- **Execution/runtime inspection:** not performed
- **Human review:** pending

Re-review when an example is added, made runnable, mirrored into fixtures/tests, invalidated by an operational contract, or affected by rights/sensitivity/release changes.

## Example contract

Every consequential example must declare:

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: explicit
expected_outcome: ANSWER | ABSTAIN | DENY | ERROR | HOLD | QUARANTINE | NOT_APPLICABLE
operational_home: "<verified owning root or NEEDS VERIFICATION>"
validation_boundary: "<exact checks performed>"
correction_trigger: "<contract, policy, source, runtime, or release change>"
```

`ANSWER` requires support appropriate to the scenario. Missing, stale, conflicting, or citation-invalid evidence yields `ABSTAIN`; prohibited rights/sensitivity/role exposure yields `DENY` or `HOLD`; tool/schema/runtime failure yields `ERROR`.

## Guardrails

| Risk | Guardrail |
|---|---|
| Narration becomes evidence | Every consequential claim cites support or abstains. |
| Camera hides sensitivity | Camera, blur, opacity, and filters are not redaction. |
| 3D becomes truth | Require Reality Boundary Notes and evidence parity. |
| Deck becomes release | Only release records and published lanes can create public story state. |

## Current bounded inventory

The current direct listing contains exactly two Markdown files:

- `README.md` (this file)
- `kansas_drought_2012.md` (the only verified child deck)

This direct listing is bounded evidence. It does not prove recursive absence, retirement, or permission to create speculative children.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Direct directory listing | `CONFIRMED BOUNDED` | `main@4a2ddb9abe7ae64aad7c2d650478a7a14af1b73c` lists README.md and kansas_drought_2012.md |
| Recursive subtree and non-Markdown inventory | `UNKNOWN` | Pinned recursive tree and file classification |
| Runnable entrypoints and dependency closure | `UNKNOWN` | Manifests, locks, commands, no-network inputs, observed runs |
| Schema/contract conformance | `NEEDS VERIFICATION` | Accepted versions and validation results |
| Examples-specific validation and CI | `NEEDS VERIFICATION` | Repository-owned validator, tests, fixtures, workflow |
| Host rendering and accessibility | `NEEDS VERIFICATION` | Render/browser inspection and accepted checks |
| Correction and retirement consumers | `NEEDS VERIFICATION` | Inbound references, owner, replacement, rollback |

## No-loss ledger

| Prior material | Disposition |
|---|---|
| Stable path and `doc_id` | Preserved |
| Current-main evidence re-pin and direct two-file inventory | Added as bounded current evidence; not a recursive absence claim |
| Non-authority and trust-membrane warnings | Preserved and strengthened |
| Accepted material and exclusions | Preserved and normalized |
| Finite outcomes and fail-closed behavior | Preserved |
| Domain/source-role/sensitivity guardrails | Preserved |
| Lifecycle and operational-home separation | Preserved |
| Prior evidence ledger and limitations | Consolidated into current evidence/verification sections |
| Speculative child trees | Removed as proposals; no child is retired by omission |
| Operational payload, code, fixture, test, or release change | None |

### Change history

#### v0.3.0 — 2026-09-06

- re-pinned the README to current `main` and recorded the exact direct directory inventory;
- reconciled placement with accepted ADR-0029 while preserving the non-authoritative example boundary;
- clarified StoryManifest/StoryNode contract and schema homes versus released story payloads;
- refreshed the linked story-source evidence and review method;
- changed Markdown only; no operational, runtime, release, or publication state changed.

#### v0.2.0 — 2026-07-24

- normalized the first twelve H2 sections to the current folder contract;
- classified the lane as `STATIC_WALKTHROUGH`;
- preserved substantive boundaries, negative states, safety controls, and prior rollback identity;
- removed speculative tree pressure without treating unlisted files as absent;
- changed Markdown only.

<p align="right"><a href="#top">Back to top</a></p>
