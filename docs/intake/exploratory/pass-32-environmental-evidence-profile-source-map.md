<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-32-environmental-evidence-profile-source-map
title: Pass 32 Environmental Evidence Profile Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; EXPLORATORY; implementation-companion
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; intake-only; no-authority
owning_root: docs/
responsibility: trace Pass 32 environmental-evidence ideas into a bounded fixture-only companion profile without replacing EvidenceBundle authority
truth_posture: cite-or-abstain; source cards are proposal evidence, not implementation or publication authority
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../contracts/evidence/environmental_evidence_bundle_profile.md
  - ../../../schemas/contracts/v1/evidence/environmental_evidence_bundle_profile.schema.json
  - ../../../fixtures/contracts/v1/evidence/environmental_evidence_bundle_profile/README.md
  - ../../../tools/validators/evidence/validate_environmental_evidence_bundle_profile.py
  - ../../../tests/validators/evidence/test_environmental_evidence_bundle_profile.py
tags: [kfm, pass-32, evidence, environment, fixture-only, intake]
notes:
  - "Adapts KFM-P32-PROG-0007 and KFM-P32-IDEA-0013."
  - "The profile is a digest-bound companion to the generic EvidenceBundle, not a new EvidenceBundle authority."
[/KFM_META_BLOCK_V2] -->

# Pass 32 Environmental Evidence Profile Source Map

## Status

- **Source ideas:** `KFM-P32-PROG-0007` and `KFM-P32-IDEA-0013`.
- **Disposition:** `PROPOSED` dependency-closed implementation companion.
- **Authority:** none. The Pass 32 atlas remains exploratory input.
- **Execution:** fixture-only, deterministic, and no-network.

## Adapted requirements

The bounded profile records:

- the referenced generic EvidenceBundle identity and `spec_hash`;
- environmental source assets and source roles;
- observation and processing windows;
- HTTP validator or immutable-digest posture;
- declared indicator and threshold semantics;
- cluster or change summaries without raw observations;
- limitations and uncertainty;
- evidence-resolution, rights, sensitivity, policy, and review posture;
- explicit denial of promotion, release, publication, and public-use authority.

## Narrowing decisions

The source cards are narrowed as follows:

1. The generic EvidenceBundle remains the evidence authority. The new object is only a companion profile bound to an existing bundle ID and digest.
2. The profile contains no live source payload, precise sensitive coordinate, raster, station observation, or derived public layer.
3. Source validators, thresholds, and summaries are declarations checked for internal consistency; they are not authenticated scientific truth.
4. Unknown rights, sensitivity, evidence resolution, or review state produces a finite hold or denial rather than optimistic release.
5. A passing fixture validates only the inactive profile and never changes lifecycle state.

## Deferred work

Separate authorization is required for live source resolution, EvidenceRef resolution, source-rights verification, policy execution, scientific threshold review, geospatial computation, catalog emission, MapLibre consumption, promotion, release, or publication.

## Directory Rules basis

Placement follows accepted ADR-0029 and the responsibility split in the Directory Governance Standard:

- source adaptation and human explanation under `docs/`;
- semantic profile meaning under `contracts/evidence/`;
- machine shape under `schemas/contracts/v1/evidence/`;
- synthetic examples under `fixtures/contracts/v1/evidence/`;
- executable validation under `tools/validators/evidence/`;
- behavior proof under `tests/validators/evidence/`;
- read-only orchestration under `.github/workflows/`;
- AI authoring provenance under `data/receipts/generated/`.

No parallel evidence store, schema root, policy home, release lane, or publication path is created.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the additive implementation commit or merge commit. No live source, evidence record, lifecycle object, release, deployment, or public artifact requires restoration.
