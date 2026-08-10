<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-5-atlas-card-delta-source-map
title: New Ideas 5-19-26 - Atlas Card Delta Assessment Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: proposed; fixture-only; repository-grounded
owners: OWNER_TBD - Intake steward; Atlas steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; intake; exploratory; cite-or-abstain
truth_posture: CONFIRMED source and repository evidence; PROPOSED fixture-only profile; cite-or-abstain
owning_root: docs/
responsibility: Preserve the evidence and repository routing for a fixture-only Atlas-card delta assessment derived from the Drive-proposed Atlas diff visualizer.
source_evidence:
  title: New Ideas 5-19-26
  drive_id: 1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ
  source_date: 2026-05-19
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 169ac1946812b6452a28c38ee57bc78ee41901b8
related:
  - ./new-ideas-5-source-map.md
  - ../../doctrine/directory-rules.md
  - ../../../contracts/governance/atlas_card_delta_assessment.md
  - ../../../schemas/contracts/v1/governance/atlas_card_delta_assessment.schema.json
tags: [kfm, intake, new-ideas, atlas, delta, diff, governance, fixture-only]
notes:
  - "The source proposes an Atlas diff visualizer; this slice implements only a deterministic comparison profile that a future governed visualizer may consume."
  - "No Google Drive document, Atlas card, registry, policy decision, release, deployment, or publication state is modified."
[/KFM_META_BLOCK_V2] -->

# New Ideas 5-19-26 - Atlas card delta assessment source map

## Source pressure

The Drive document *New Ideas 5-19-26* lists an **Atlas diff visualizer** among its future expansion paths. The useful design pressure is visibility: reviewers should be able to see changes to normalized statements, truth labels, evidence references, dependencies, and candidate authority families without comparing large card bodies by eye.

The source does not establish a canonical card-history store, UI framework, review authority, or safe mutation path. Copying the visualizer idea directly into an application would therefore risk making display logic the de facto comparison authority.

## Repository comparison

At `main@169ac1946812b6452a28c38ee57bc78ee41901b8`:

- Atlas documents and stable candidate IDs are present under `docs/atlases/` and related corpus files.
- Existing validators cover many object families, but repository search found no Atlas-card delta contract or validator.
- The existing `docs/intake/exploratory/new-ideas-5-source-map.md` preserves the larger New Ideas packet as exploratory lineage and rejects packet-shaped parallel roots.
- Accepted Directory Rules require the comparison meaning, shape, executable, fixtures, tests, hosted orchestration, and generated receipt to remain in their existing responsibility roots.
- Open draft PRs #2400 and #2401 concern rendering-resource and offline-release assessments, not Atlas-card comparison.

## Smallest safe implementation

This change adds a fixture-only `AtlasCardDeltaAssessmentCandidate` that:

- compares synthetic before/after snapshots;
- derives transition, changed fields, and set additions/removals;
- preserves stable identity;
- fails closed on stale hashes, false declarations, and authority overreach;
- abstains on unresolved or unsupported truth claims; and
- emits `PASS`, `ABSTAIN`, `DENY`, or `ERROR` with stable reason codes.

The profile is a prerequisite for, not an implementation of, a visualizer. A future UI may render its output through a governed adapter, but it must not recompute, hide, or promote outcomes.

## Directory Rules basis

| Artifact responsibility | Home |
|---|---|
| Semantic comparison meaning | `contracts/governance/` |
| Machine shape | `schemas/contracts/v1/governance/` |
| Synthetic cases | `fixtures/contracts/v1/governance/` |
| Deterministic executable | `tools/validators/governance/` |
| Focused proof | `tests/validators/governance/` |
| Source lineage and limits | `docs/intake/exploratory/` |
| Hosted read-only orchestration | `.github/workflows/` |
| AI-authoring process memory | `data/receipts/generated/` |

This additive slice creates no new root and no parallel Atlas, registry, policy, proof, release, or publication home.

## Validation and limits

Validation is local and no-network. Synthetic fixtures cover modified, unchanged, added, unresolved, unsupported-confirmed, identity-change, declaration-mismatch, stale-hash, authority-overreach, and upstream-error cases.

A green result proves only that a candidate matches the bounded comparison profile. It does not resolve evidence, decide truth, edit a card, approve review, authorize release, deploy a visualizer, publish, or permit public use.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, use a focused revert of the additive contract, schema, fixtures, validator, tests, source map, workflow, and generated receipt. No external or published state requires rollback.
