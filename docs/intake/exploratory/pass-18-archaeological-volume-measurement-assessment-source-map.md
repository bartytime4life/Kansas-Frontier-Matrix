<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-archaeological-volume-measurement-assessment-source-map
title: Pass 18 Archaeological Volume Measurement Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Archaeology steward · 3D documentation steward · Evidence steward · Validation steward
created: 2026-08-12
updated: 2026-08-12
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; archaeology; three-d; measurement; uncertainty
responsibility: Reconcile Pass 18 card KFM-P18-INV-435 and its connected 3D GIS source with current Archaeology-domain ownership, implementing only an inactive synthetic declaration profile for a volume measurement object distinct from visual carriers.
truth_posture: "CONFIRMED source-card statement, connected-source support, current-repository collision check, Directory Rules placement, deterministic local fixture replay, and coordinate-free authority boundary; PROPOSED inactive implementation; UNKNOWN real measurement, asset, method, uncertainty, and reference validity; NEEDS VERIFICATION archaeology, cultural, technical, evidence, policy, release, human-review, and hosted-CI acceptance"
related:
  - ../../../contracts/domains/archaeology/archaeological_volume_measurement_assessment.md
  - ../../../schemas/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment.schema.json
  - ../../../contracts/domains/archaeology/three_d_documentation.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Archaeological Volume Measurement Assessment Source Map

## Evidence and selected gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, card `KFM-P18-INV-435`, physical PDF page 155 (printed page 152) | KFM should model archaeological volume measurements, CT-derived volumes, and deposit-volume estimates as evidence objects distinct from visual meshes. The card names a 3D asset manifest, measurement receipt, uncertainty profile, and review state as dependencies. | `CONFIRMED` source-card statement; page rendered and visually inspected |
| Connected Google Drive `Archaeological 3D GIS.pdf` (`1gDC9HlpspL5hlQUjOTlYnZe4XJBqzgDb`), especially its volume chapter and CT/volume discussion | The source distinguishes volumetric carriers and representations from the analytical workflows that derive and relate new information, and describes CT, voxel, boundary-model, and deposit-oriented cases. | `CONFIRMED` conceptual support; not KFM implementation proof |
| `contracts/domains/archaeology/three_d_documentation.md` and its paired fixture profile | Current ownership already covers 3D acquisition, processing, scale, interpretation, and carrier lineage. | `CONFIRMED` adjacent semantic owner; composed by opaque reference rather than duplicated |
| Repository tree, code, issue, and pull-request collision checks on `main@1a3af1b2762b26cfc2973a6df28d732127930ec2` | No `KFM-P18-INV-435`, archaeological volume-measurement assessment path, matching contract object, or matching pull request was found. The three open pull requests at inspection touched other paths. | `CONFIRMED` bounded gap at inspected revision |
| Accepted Directory Rules through ADR-0029 | Domain meaning belongs under `contracts/`; shape under `schemas/`; examples, validator, focused tests, workflow, source map, and generated receipt retain their established roots. | `CONFIRMED` placement basis |

The atlas is treated as a candidate source, not implementation proof. The
connected book supports the problem space, not this contract's authority or
scientific fitness. The repository collision check establishes only that the
named bounded slice was not already present at the inspected revision.

## Connected-dots adaptation

The source idea is implemented as a separate
`ArchaeologicalVolumeMeasurementAssessmentCandidate` that references existing
3D documentation and assets without owning or opening them. This preserves the
card's distinction between an analytical measurement and a visual carrier while
respecting current Archaeology ownership.

The slice records:

- subject kind and measurement scope through opaque synthetic references;
- the governing `ThreeDDocumentation` reference;
- declared input, visual-mesh, and volumetric-input roles;
- method, algorithm, scale-basis, processing, and measurement receipts;
- value, unit, precision, and quantified, qualitative, or unresolved uncertainty;
- evidence, rights, technical/cultural review, policy, sensitivity, and reversible lifecycle references; and
- explicit false authority claims and coordinate-free limitations.

It does not model a mesh, CT volume, excavation geometry, or map location. It
does not calculate a volume or determine whether any method is scientifically
appropriate.

## Implemented ownership map

| Meaning or artifact | Canonical path | Truth label |
|---|---|---|
| Proposed domain semantics and non-effects | `contracts/domains/archaeology/archaeological_volume_measurement_assessment.md` | `PROPOSED` |
| Proposed machine-readable shape | `schemas/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment.schema.json` | `PROPOSED` |
| Synthetic exact outcome matrix | `fixtures/contracts/v1/domains/archaeology/archaeological_volume_measurement_assessment/cases.json` | `CONFIRMED` fixture behavior only |
| Local deterministic declaration validator | `tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py` | `CONFIRMED` implementation |
| Focused safety and replay tests | `tests/validators/domains/archaeology/test_validate_archaeological_volume_measurement_assessment.py` | `CONFIRMED` local validation |
| Path-scoped no-network CI check | `.github/workflows/archaeological-volume-measurement-assessment.yml` | `PROPOSED` until hosted exact-head run |
| Source reconciliation | this file | `CONFIRMED` evidence map; non-authoritative |
| Authoring provenance and hashes | `data/receipts/generated/genrec-pass18-archaeological-volume-measurement-assessment-20260812.json` | `CONFIRMED` after hash replay |

## Deterministic outcomes

The fixture matrix covers all four finite outcomes:

- `PASS` for complete synthetic CT-derived and mesh-derived candidates;
- `ABSTAIN` for unresolved measurement, uncertainty, governance, or specialist review;
- `DENY` for invalid identity, undeclared or method-incompatible source roles,
  incomplete measurement closure, contradictory uncertainty, unsafe publication
  posture, noncanonical references, or forbidden authority; and
- `ERROR` for an explicitly failed measurement or governance state.

Findings are sorted, identity binds all declaration content, and the tests block
network creation during replay. Schema constants prevent a conforming candidate
from claiming measurement truth or any evidence, policy, review, release,
publication, or public-use authority.

## Directory Rules and lifecycle boundary

This packet adds no new root and no parallel semantic owner. It is additive,
inactive, fixture-only, and path-scoped. No live source, data route, map layer,
renderer, API, deployment, or publication behavior is activated.

Activation would require a later decision naming the canonical runtime owner,
real-data classification, scientific method and unit-conversion rules,
uncertainty governance, cultural and technical reviewers, evidence handling,
release controls, correction process, and rollback authority. Human review and
hosted exact-head CI remain required before even this inactive proposal can be
accepted.

Rollback is deletion of the eight-file packet. Because it has no runtime
consumer or live data, no data migration is implied.

## Source inventory

| Source | Identifier | Use |
|---|---|---|
| Pass 18 Idea Index, Category Atlas, and Expansion Dossier | attached PDF SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`; card `KFM-P18-INV-435` | Candidate statement and dependency framing |
| Archaeological 3D GIS | Google Drive file `1gDC9HlpspL5hlQUjOTlYnZe4XJBqzgDb` | Connected conceptual source for 3D volume representations and analytical workflows |
| Current KFM repository | `bartytime4life/Kansas-Frontier-Matrix`, inspected `main@1a3af1b2762b26cfc2973a6df28d732127930ec2` | Ownership, collision, and placement evidence |

All real asset contents, measurements, sensitive locations, external reference
validity, reviewer decisions, and downstream consumer behavior remain `UNKNOWN`.
