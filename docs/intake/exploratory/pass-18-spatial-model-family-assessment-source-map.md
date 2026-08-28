<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-spatial-model-family-assessment-source-map
title: Pass 18 Spatial Model Family Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Domain steward · Evidence steward · Map steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; spatial-model; uncertainty
responsibility: Reconcile one supplied spatial-model-family idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied card, accepted Directory Rules, adjacent repository contracts, and bounded gap; PROPOSED inactive implementation profile; UNKNOWN domain adoption and scientific validation rules; NEEDS VERIFICATION steward review and hosted exact-head CI"
related:
  - ../../../contracts/common/spatial_model_family_assessment.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../contracts/common/modeled_surface.md
  - ../../../contracts/evidence/representation_fitness_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Spatial Model Family Assessment Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-054` | Positions, networks, continuous fields, and spatial transformations are different model families and should not share one generic validation rubric. | `CONFIRMED` source statement |
| `contracts/common/spatial_geometry.md` | Defines geometry representation rules but not model-family dispatch or composite-family uncertainty. | `CONFIRMED` adjacent contract |
| `contracts/common/modeled_surface.md` | Defines modeled-surface semantics for a field-like product without classifying other spatial families. | `CONFIRMED` adjacent contract |
| `contracts/evidence/representation_fitness_assessment.md` | Assesses representation fitness for an intended use but does not declare the subject's spatial model family. | `CONFIRMED` adjacent contract |
| Current `main@ded9a9755316fee97827d5d65b8fc26e31c2ae4b` search | No exact spatial-model-family assessment contract, schema, fixture family, validator, workflow, branch, or PR was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used for candidate discovery and corroboration only. Private filenames, IDs, URLs, hashes, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The packet creates one closed synthetic assessment profile. It declares a
subject and digest, one base family or a decomposed composite, family-specific
characteristics and evidence references, uncertainty references, review state,
content identity, limitations, and fixed-false authority claims.

It deliberately does not create the card's proposed production
`spatial_model_type` registry or validator dispatcher. Those require domain
ownership, compatibility analysis, migration policy, and steward decisions that
the supplied material and current repository do not resolve.

## Directory Rules basis

The implementation uses existing responsibility roots for contract meaning,
schema shape, synthetic fixtures, validation, tests, read-only orchestration,
source reconciliation, and generated authoring provenance. It introduces no
parallel domain, source, evidence, registry, policy, release, or publication
authority.

## Truth and non-effects

The source idea and repository gap are `CONFIRMED`. The assessment is
`PROPOSED_INACTIVE`. Domain adoption and scientific validation profiles remain
`UNKNOWN`; steward review and hosted exact-head CI `NEED VERIFICATION`.

A local `PASS` authenticates no geometry, topology, field support,
transformation, component, uncertainty statement, review record, evidence,
policy, release, or public-use state. Rollback is a single additive commit
revert with no external cleanup.
