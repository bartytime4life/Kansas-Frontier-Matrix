<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-intake-exploratory-specimen-record-conformance-source-map
title: Flora SpecimenRecord conformance - governed source map
type: exploratory-intake; implementation-source-map
version: v1.0
status: draft; triaged; noncanonical
owners: OWNER_TBD — Flora steward · specimen steward · source steward · rights steward · sensitivity steward · validation steward
created: 2026-08-12
updated: 2026-08-12
policy_label: public; flora; specimen; fixture-only; no-network
owning_root: docs/
responsibility: reconcile supplied specimen-readiness ideas with the existing Flora SpecimenRecord scaffold and bound the smallest inactive conformance slice
truth_posture: CONFIRMED supplied-source excerpts and inspected repository gap / PROPOSED fixture-only implementation / NEEDS VERIFICATION real source, specimen, taxonomy, rights, sensitivity, evidence, policy, review, release, and publication state
related: [../../../contracts/domains/flora/specimen_record.md, ../../../schemas/contracts/v1/domains/flora/specimen_record.schema.json, ../../../fixtures/domains/flora/specimen_record/README.md, ../../../tools/validators/domains/flora/validate_specimen_record.py]
tags: [kfm, intake, flora, specimen-record, herbarium, idigbio, historical-evidence, conformance]
notes: [The complete New Ideas 5-19-26 Drive document was reviewed through the connected Google Drive representation; the locally supplied consolidated atlas was text-extracted and relevant pages inspected; this source map grants no source activation, ingest, taxonomy, evidence, rights, sensitivity, release, deployment, or publication authority.]
[/KFM_META_BLOCK_V2] -->

# Flora SpecimenRecord conformance — governed source map

> [!IMPORTANT]
> **Authority:** `EXPLORATORY / IMPLEMENTATION LINEAGE ONLY`
> **Implementation:** closed synthetic conformance profile
> **Public effect:** none

## Evidence reconciled

| Evidence | Confirmed signal | Adaptation boundary |
|---|---|---|
| Google Drive document *New Ideas 5-19-26*, document ID `1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ`, complete connector representation reviewed | Biodiversity readiness should retain GBIF/iDigBio occurrence and specimen provenance, taxonomic backbone links, georeference quality, rights, and sensitive-location posture. | The packet is exploratory and cannot activate a source or turn historical evidence from a specimen into current presence. |
| Supplied `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`, PDF pages 936–939 | The flora watcher cards preserve institution/catalog identity, event date, coordinates/uncertainty, license/rights holder, specimen-backed source role, dedupe lineage, restricted-taxa handling, deterministic hashes, and thin-slice-first validation. | Proposed paths and live watcher behavior are not adopted. Raw coordinates are specifically excluded from this public-safe fixture profile. |
| Current repository `main@753dfe4c4d17482c51bdf90ae8f8bb93e8644d3c` | `contracts/domains/flora/specimen_record.md` already owned the semantics, but its paired schema was empty/permissive and it listed fixtures and validators as open work. | Extend the existing owner; do not create another specimen contract or source-specific runtime. |
| GitHub overlap check on 2026-08-12 | No open pull requests and no active branch matched the SpecimenRecord conformance slice. Historical iDigBio/herbarium documentation PRs do not fill the object-level schema/validator gap. | Absence is bounded to searched names and inspected current main; differently named future work remains possible. |

## Chosen bounded slice

The implementation closes only the existing contract's first dependency-complete
conformance gap:

- one closed Draft 2020-12 candidate schema;
- one shared synthetic base record and exact mutation matrix;
- deterministic source/catalog-bound candidate identity and `spec_hash`;
- historical-evidence-not-current-occurrence enforcement;
- label-text, determination, locality, rights, sensitivity, correction, and
  public-candidate checks;
- fixed-false source/evidence/policy/review/release/publication effects;
- focused no-network tests and read-only CI.

## Explicit non-effects

This slice does not contact KANU, KSC, iDigBio, GBIF, USDA PLANTS,
NatureServe, or any other source. It does not:

- establish a real specimen, collection event, institution, catalog number, or
  current occurrence;
- accept taxonomy, resolve a crosswalk, or treat label text as authority;
- resolve evidence, source terms, rights, sensitivity, review, or policy;
- ingest RAW data, produce a catalog record, create a released public payload,
  deploy, or publish; or
- supersede the existing occurrence, taxon, redaction, evidence, promotion,
  release, correction, or rollback families.

## Directory Rules basis

Existing responsibility roots remain unchanged: semantic meaning under
`contracts/domains/flora/`; machine shape under
`schemas/contracts/v1/domains/flora/`; synthetic replay under
`fixtures/domains/flora/`; reusable validation under
`tools/validators/domains/flora/`; focused proof under
`tests/domains/flora/`; read-only orchestration under
`.github/workflows/`; source reconciliation here; and AI authoring
provenance under `data/receipts/generated/`.

## Remaining holds

Real integration still requires primary source and terms verification, stable
source descriptors, identifier collision rules, taxonomic re-determination and
crosswalk policy, media rights, rare-taxon and joined-location review,
EvidenceBundle closure, policy and human approval, correction/withdrawal
behavior, released consumer contracts, and rollback proof.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, transparently revert this dependency-closed change and rerun
the focused profile and generated-receipt validation. No live source, database,
cache, release, deployment, or publication cleanup is required.
