<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-three-d-documentation-paradata-source-map
title: Pass 18 ThreeDDocumentation Paradata Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Archaeology steward · 3D documentation steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; archaeology; three-d; paradata
responsibility: Reconcile Pass 18 card KFM-P18-INV-410 and its 3D GIS source with the existing ThreeDDocumentation family, closing only a fixture-validation gap without creating asset, evidence, interpretation, policy, review, release, or publication authority.
truth_posture: "CONFIRMED source-card support, connected source inspection, current scaffold gap, closed fixture profile, and deterministic local replay; PROPOSED inactive implementation; UNKNOWN real asset and reference validity; NEEDS VERIFICATION archaeology, cultural, evidence, policy, review, release, and hosted-CI acceptance"
related:
  - ../../../contracts/domains/archaeology/three_d_documentation.md
  - ../../../schemas/contracts/v1/domains/archaeology/three_d_documentation.schema.json
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 ThreeDDocumentation Paradata Source Map

## Evidence and bounded gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, card `KFM-P18-INV-410`, physical PDF pages 340–341 (printed pages 337–338) | 3D GIS artifacts should retain acquisition methods, processing choices, scaling, georeferencing, and interpretive steps so mixed scan, photogrammetry, CT, and interpretation choices remain reviewable. | `CONFIRMED` source statement; rendered page visually inspected |
| Connected Google Drive file `Archaeological 3D GIS.pdf` (`1gDC9HlpspL5hlQUjOTlYnZe4XJBqzgDb`) | The cited source distinguishes image-based modeling, laser scanning, scale/georeference handling, reality-based and interpretive models, and the procedural choices behind 3D results. | `CONFIRMED` source support; not KFM implementation evidence |
| Connected Google Drive `KFM_Full_Atlas_seed_cards` | The wider proposal corpus keeps source, evidence, policy/review, release, correction, and rollback dependencies explicit. | `CONFIRMED` corroborating doctrine; not asserted byte-identical to Pass 18 |
| `contracts/domains/archaeology/three_d_documentation.md` | Existing semantics already require capture, processing, scale/accuracy, uncertainty, sensitivity, review, and lifecycle state to remain inspectable. | `CONFIRMED` authority owner retained |
| Prior paired schema on `main@01b3f70bb0514c0557e777294b36992317e992c8` | The existing schema had empty properties and `additionalProperties: true`; no matching validator, fixture family, focused test, or workflow was found. | `CONFIRMED` bounded implementation gap |

The selected change closes the existing family rather than creating a second
paradata contract. The card's suggested `3d_asset_paradata` concept is adapted
inside `ThreeDDocumentation`, which already owns Archaeology-domain 3D
documentation meaning.

## Implemented slice

The inactive profile records synthetic references for:

- capture state, methods, devices, receipt, and method statement;
- ordered processing steps with explicit input/output assets and receipts;
- scale, georeference, coordinate-reference, orientation, and receipts;
- reality-based, interpretive, or mixed knowledge character;
- true-3D versus 2.5D representation and vertical-surface-loss disclosure;
- source, derived, and public-safe asset roles; and
- evidence, rights, technical/cultural review, policy, transform, release,
  correction, and rollback references.

The deterministic validator returns `PASS`, `ABSTAIN`, `DENY`, or `ERROR` for
declaration coherence. It does not open an asset, resolve a reference, execute a
transform, decide an interpretation, expose coordinates, or authorize any
governance or public action.

## Directory Rules basis

Accepted ADR-0029 keeps semantic ownership in the existing
`contracts/domains/archaeology/` lane. Machine shape stays in
`schemas/contracts/v1/domains/archaeology/`; synthetic inputs in
`fixtures/contracts/v1/domains/archaeology/`; reusable checks in
`tools/validators/domains/archaeology/`; conformance proof in
`tests/validators/domains/archaeology/`; read-only orchestration in
`.github/workflows/`; source reconciliation here; and authoring accountability
in `data/receipts/generated/`.

No new root, parallel semantic owner, asset store, source registry entry,
policy module, review record, release artifact, API route, viewer, or public
surface is introduced.

## Non-effects and rollback

A local `PASS` proves only that a synthetic declaration is coherent under this
proposed profile. It is not evidence proof, archaeological interpretation,
rights clearance, cultural/steward approval, policy permission, release state,
publication, or permission to expose a location or model.

Rollback is one feature-commit revert. No external asset or operational state
requires cleanup.
