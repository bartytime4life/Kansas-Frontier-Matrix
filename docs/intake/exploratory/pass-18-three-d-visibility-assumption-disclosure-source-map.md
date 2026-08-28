<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-three-d-visibility-assumption-disclosure-source-map
title: Pass 18 Three-D Visibility Assumption Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Archaeology steward · 3D analysis steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; archaeology; three-d; visibility
responsibility: Reconcile supplied and connected-drive 3D visibility ideas with current repository evidence while preserving archaeology, sensitivity, evidence, policy, review, release, and publication boundaries.
truth_posture: CONFIRMED supplied card, connected Drive corroboration, current repository gap, and local fixture replay / PROPOSED inactive implementation / UNKNOWN real analysis validity / NEEDS VERIFICATION steward and hosted-CI acceptance
related:
  - ../../../contracts/domains/archaeology/three_d_visibility_assumption_disclosure.md
  - ../../../contracts/domains/archaeology/three_d_documentation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Three-D Visibility Assumption Disclosure Source Map

## Evidence and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, `KFM-P18-INV-458`, physical PDF pages 342–343 (printed pages 339–340) | 3D visibility analyses should disclose observer points, target points, obstacles, model resolution, line-of-sight rules, and interpretation scope because results depend on assumptions. | `CONFIRMED` source statement; source PDF inspected locally |
| Connected Google Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The broader field/3D seed keeps acquisition, processing, interpretation, sensitivity, evidence, policy/review, release, correction, and rollback dependencies explicit. | `CONFIRMED` corroborating proposal; not implementation evidence |
| Current `ThreeDDocumentation` family | Owns capture, processing, scale, georeference, representation, asset, and governance paradata. | `CONFIRMED` adjacent authority retained |
| Current repository and open-PR search | No contract, schema, fixture validator, or workflow was found for observer/target heights, viewshed or line-of-sight assumptions, obstacle completeness, or visibility interpretation scope. | `CONFIRMED` bounded gap at authoring base |

The implementation adds a domain-specific disclosure profile. It does not
change `ThreeDDocumentation`, run an analysis, or claim that visibility is an
archaeological fact.

## Selected slice

The closed candidate records only opaque references and aggregate parameters:

- scene-model identity, resolution, and vertical datum;
- observer and target geometry posture, counts, height values, and basis refs;
- obstacle mode, completeness, transparency rule, and model refs;
- algorithm, line-of-sight rule, curvature, refraction, distance limit, and
  scenario IDs;
- interpretation and uncertainty statements; and
- evidence, technical/cultural review, policy, public transform, release,
  correction, and rollback references.

Unknown or incomplete assumptions return `ABSTAIN`. Contradictory declarations,
identity drift, exact-location public candidates, or incomplete public closure
return `DENY`. A declared analysis error returns `ERROR`.

## Directory Rules basis

Accepted ADR-0029 assigns the semantic owner to the existing archaeology domain
root. Shape, fixtures, reusable validation, tests, read-only workflow,
exploratory source map, and generated receipt use their established paired
roots. No source registry, evidence store, policy authority, review queue,
release lane, map surface, API, or public artifact is created.

## Non-effects

A fixture `PASS` proves only local disclosure coherence. It does not validate a
model, geometry, observer, target, obstacle, line of sight, interpretation,
rights posture, cultural decision, release, publication, or public use.
