<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/geology/sources/readme
name: Geology Source Registry README
path: data/registry/geology/sources/README.md
type: data-registry-geology-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <geology-domain-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: geology-source-descriptor-records
domain: geology
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-geology; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; restricted-subsurface-details-fail-closed; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/geology/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/geology/
  - ../../../work/geology/
  - ../../../quarantine/geology/
  - ../../../processed/geology/README.md
  - ../../../catalog/domain/geology/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/geology/SOURCES.md
  - ../../../../docs/domains/geology/SOURCE_LEDGER.md
  - ../../../../docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/geology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/geology/SENSITIVITY.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/sources/catalog/usgs/usgs-ngmdb.md
  - ../../../../docs/sources/catalog/usgs/usgs-mrds.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../policy/domains/geology/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - geology
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - subsurface
  - boreholes
  - well-logs
  - mineral-resources
  - kgs
  - kcc
  - usgs
  - ngmdb
  - gems
  - mrds
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/geology/sources/README.md`."
  - "Geology source registry records are admission and authority-control records. They do not store source payloads, prove geologic claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Geology source-registry doctrine names `data/registry/sources/geology/` as the machine-readable registry lane. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Restricted subsurface and resource-adjacent details fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Source Registry

Domain-first registry lane for Geology and Natural Resources source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-795548">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Geology source boundary](#geology-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/geology/sources/` is a source-registry lane for Geology admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Geology source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Geology and Natural Resources lane.

Geology source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity posture for subsurface, resource, well-log, sample, and map-derived material;
- cadence, source head, retrieval window, source vintage, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, and rollback requirements.

They do **not** record geologic truth. A source descriptor can authorize or deny admission conditions, but every geologic claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/geology/sources/
```

This is a domain-first registry path. Current Geology source-registry doctrine and source-family docs name the subtype-first pattern as the machine-readable source registry home:

```text
data/registry/sources/geology/
```

Because both patterns are visible in repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory or ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/geology/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Geology source descriptor/admission records | `data/registry/geology/sources/` and/or `data/registry/sources/geology/` after topology reconciliation | Source identity, role, rights, terms, cadence, sensitivity, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Geology source orientation | `docs/domains/geology/SOURCE_REGISTRY.md`, `SOURCES.md`, `SOURCE_LEDGER.md`, `SOURCE_ROLE_MATRIX.md` | Explains source families, source-role discipline, admission posture, and anti-collapse rules; not machine descriptor storage. |
| Geology source payloads | `data/raw/geology/`, `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/` | Actual data belongs in lifecycle lanes, not registry records. |
| Geology domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Geology semantic meaning | `contracts/domains/geology/` | Object-family meaning and invariants. |
| Geology machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Geology policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/`, `policy/rights/` | Exposure, rights, source-role, subsurface sensitivity, and admissibility rules. |
| Geology validation receipts | `data/receipts/validation/geology/` if/when accepted | Process memory for validation checks. |
| Geology proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Geology catalog projections | `data/catalog/domain/geology/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Geology release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Geology source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, or public presentation. |
| Descriptor is not geologic truth | KGS, KCC, USGS, WWC5, LAS, NGMDB, GeMS, MRDS, geophysics, geochemistry, and natural-resource sources still require evidence and review before claims. |
| Anti-collapse is mandatory | Occurrence, deposit, estimate, permit, production, reserve, borehole, well-log, sample, map unit, model, and aggregate are not interchangeable claim types. |
| Restricted details fail closed | Sensitive subsurface, resource-adjacent, sample, well-log, and precise local details are denied, restricted, or generalized unless policy/review/redaction gates explicitly permit a public-safe derivative. |
| Regulatory and administrative context remain scoped | KCC regulatory data and permit/operator records are regulatory or administrative context unless separately supported as observed geology evidence. |
| Aggregates are not per-place records | County, basin, field, or formation rollups cannot be cited as individual observations. |
| Models are not observations | Resource estimate surfaces, inversions, interpolations, and synthetic subsurface surfaces require model identity, run receipts, uncertainty, and reality-boundary notes where applicable. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Geology source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, and authority-scope metadata;
- source vintage, map series, well-log vintage, sample or lab lineage, model lineage, and source-head metadata summaries;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, sensitive location details, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or geologic claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Geology source payloads, geologic map packages, borehole tables, well logs, LAS files, well tops, WWC5 records, KCC extracts, production tables, MRDS records, NGMDB/GeMS packages, geophysics/geochemistry files, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/geology/`, `data/work/geology/`, `data/quarantine/geology/`, or `data/processed/geology/` depending on lifecycle state |
| Restricted subsurface details, restricted well-log detail, private identifiers, access secrets, or sensitive resource-adjacent details | restricted lifecycle lane, quarantine, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/geology/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/geology/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/geology/` |
| Policy rules, sensitivity rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Geology layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/geology/sources/
├── README.md
├── kgs_maps/
│   ├── README.md
│   └── index.local.json
├── usgs_ngmdb_gems/
│   ├── README.md
│   └── index.local.json
├── oil_gas_wells/
│   ├── README.md
│   └── index.local.json
├── kcc_regulatory/
│   ├── README.md
│   └── index.local.json
├── wwc5_water_wells/
│   ├── README.md
│   └── index.local.json
├── las_well_logs/
│   ├── README.md
│   └── index.local.json
├── usgs_mrds/
│   ├── README.md
│   └── index.local.json
├── geophysics_geochemistry/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/geology/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Geology source registry record should be structured enough for audit, admission, validation, correction, and rollback.

```json
{
  "id": "kfm-source:geology:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "geology",
  "source_family": "kgs_maps | usgs_ngmdb_gems | oil_gas_wells | kcc_regulatory | wwc5_water_wells | las_well_logs | usgs_mrds | geophysics_geochemistry | context_layer | restricted_steward | other",
  "source_name": "Human-readable source name",
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "authority_scope": "What this source may and may not support",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | unknown",
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/geology/sources/` or `data/registry/sources/geology/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, source vintage, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm occurrence, deposit, estimate, permit, production, reserve, borehole, well-log, sample, model, and aggregate claim types are not collapsed.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm restricted subsurface, resource-adjacent, sample, well-log, and precise local details fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Geology truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Geology source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/geology/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/geology/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Geology source-registry doctrine names `data/registry/sources/geology/` as the machine-readable registry lane. | CONFIRMED by GitHub contents API during this edit |
| Geology source-family docs name canonical SourceDescriptor records under `data/registry/sources/geology/` and list source-role discipline. | CONFIRMED by GitHub contents API during this edit |
| Geology canonical-path docs include `data/registry/sources/geology/` in the data lifecycle lane and keep Geology as a segment inside responsibility roots. | CONFIRMED by GitHub contents API during this edit |
| Concrete Geology source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/geology/sources/` and `data/registry/sources/geology/` is resolved. | NEEDS VERIFICATION |
| A canonical Geology source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Geology source registry records. | UNKNOWN |
| This README grants public access to Geology source registry internals. | DENY |

---

## Maintainer note

Geology source registry records are useful because they make source identity, source role, rights, sensitivity, cadence, activation, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Geology truth
```
