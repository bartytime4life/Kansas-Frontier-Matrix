<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-18-historic-map-scan-lineage-source-map
title: Pass 18 Historic Map Scan Lineage Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Evidence steward · Source steward · Map steward · Rights steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: Trace Pass 18 card KFM-P18-INV-252 into a bounded fixture-only historic-map scan-lineage candidate without activating a source, deciding rights, executing georeferencing, or admitting evidence.
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION source rights, operational need, and hosted exact-head execution
related:
  - ../../../contracts/evidence/historic_map_scan_lineage_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../sources/catalog/loc/loc-historic-maps.md
  - ../../../contracts/map/georeference_control_point_set.md
  - ../../../contracts/map/georeference_transform_quality.md
  - ../../../contracts/source/source_rights_currentness_assessment.md
tags: [kfm, pass-18, historic-map, scan-lineage, rights, georeference, source-map]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Historic Map Scan Lineage Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, local supplied artifact SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, card `KFM-P18-INV-252`, PDF pages 141–142 (printed pages 138–139) | Historic/scanned-map workflows should distinguish original-map rights, scan provenance, georeferencing, and derivative GIS use. The card proposes original-rights, scan-source, georeference-method, GCP-count, and derivative-use-limit fields. | Proposal register; it does not establish schema ownership, legal status, accepted accuracy, or operational source use. |
| Google Drive file `KFM Pass 18 Idea Index Category Atlas and Expansion Dossier`, file `1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5` | Drive metadata confirms the matching dossier title used for corpus discovery. | The locally supplied PDF was the inspected evidence. Its byte size differs from the Drive object metadata, so byte identity is not asserted. |
| `docs/sources/catalog/loc/loc-historic-maps.md` | The repository already treats historic-map overlays as interpretive representations and calls for rights, GCP provenance, RMS uncertainty, representation receipts, and reality-boundary disclosure. | Proposed source documentation; it does not activate Library of Congress data or prove any specific item. |
| Existing georeference and rights contracts | `GeoreferenceControlPointSet`, `GeoreferenceTransformQuality`, and `SourceRightsCurrentnessAssessment` already own adjacent machine-checkable meanings. | This candidate records opaque references only and does not replay or supersede those validators. |
| Adopted Directory Rules v2 | Placement follows responsibility and must not create parallel authority. | Placement law only; it does not adopt the candidate. |

## Card transcription

`KFM-P18-INV-252` is titled **“Digital map libraries preserve original-map
rights and scan lineage.”** Its proposed behavior is to keep four layers
separate: original paper-map rights, scan provenance, georeferencing, and
derived GIS use. The card identifies these dependencies:

- original-map citation;
- scan receipt;
- georeference annotation; and
- rights review.

It also asks how the system should handle a map whose copyright is clear but
whose georeferencing quality is weak. The bounded answer in this candidate is
not to infer permission: weak geometry can retain catalog lineage, but cannot
pass a context-overlay request and can never become positional evidence.

The cited source attribution inside the dossier is `SRC-P18-002`, source pages
242. This packet does not independently verify or reproduce that source book;
the dossier card is the proposal evidence being adapted.

## Repository reconciliation

GitHub `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` already contained
the historic-map source page and the three adjacent contract families named
above. Exact and semantic searches found no
`historic_map_scan_lineage_assessment`,
`HistoricMapScanLineageAssessmentCandidate`, or equivalent fixture/validator
packet that jointly preserves original, scan, georeference, and derivative-use
boundaries.

The existing source page contains proposed implementation paths. Those paths
are not treated as adopted owners. The candidate is placed by current
responsibility and links to existing map/source contracts instead of creating a
new source connector, map store, receipt family, or policy owner.

## Bounded adaptation

| Source pressure | Retained behavior | Deferred authority |
|---|---|---|
| Original-map identity and rights | Original reference, format, citation, declared rights state, and rights-review reference remain explicit. | Legal determination, rights currentness execution, and release permission. |
| Scan provenance | A distinct scan reference, provider/source, capture declaration, digest, and receipt reference are required. | Retrieval, byte verification, scanning, and receipt issuance. |
| Georeference quality | Method, GCP count, control-point reference, quality reference, RMS declaration, reality-boundary note, and distinct derivative are preserved. | CRS verification, transform execution, quality acceptance, and positional truth. |
| Derivative GIS use | Catalog and context uses are finite; context requires cleared declared rights and assessable geometry. | Evidence admission, public use, and any positional-evidence claim. |

## Path decision

~~~yaml
path_decision:
  artifact: HistoricMapScanLineageAssessmentCandidate
  proposed_path: contracts/evidence/historic_map_scan_lineage_assessment.md
  artifact_kind: semantic contract
  authority_owner: bounded historic-map evidence-lineage candidate meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: historic-map-scan-lineage-assessment
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/sources/catalog/loc/loc-historic-maps.md
    - contracts/map/georeference_control_point_set.md
    - contracts/map/georeference_transform_quality.md
    - contracts/source/source_rights_currentness_assessment.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The evidence contract lane owns the combined lineage-assessment meaning. The
map contract lane continues to own georeference control points and transform
quality; the source contract lane continues to own rights-currentness meaning.

## Non-effects

This packet does not activate a digital-map source, retrieve or transform map
bytes, determine rights, verify citations or receipts, validate geospatial
accuracy, admit evidence, execute policy, approve review, promote, release,
deploy, publish, or authorize public use.
