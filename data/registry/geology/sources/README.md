<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/geology/sources/readme
name: Geology Source Registry README
path: data/registry/geology/sources/README.md
type: data-registry-geology-sources-readme
version: v0.3.1
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
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: geology-source-registry-compatibility-view
domain: geology
path_posture: compatibility-generated-view; canonical-writes-under-data-registry-sources; no-independent-writes; adr-0029-accepted
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
  - "Canonical Geology source registry records under `data/registry/sources/` are admission and authority-control records. This domain-first compatibility path documents and routes to that authority; it does not store those records."
  - "Adopted Directory Rules v2 (`DIR-SOURCE-003/004`) makes `data/registry/sources/` the canonical machine source-descriptor topology. This domain-first path is a compatibility/navigation surface and must not independently write descriptors."
  - "Restricted subsurface and resource-adjacent details fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Source Registry

Domain-first compatibility and navigation surface for Geology and Natural Resources source registry governance.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-795548">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Authority](#authority-and-path-posture) · [Repo fit](#repo-fit) · [Write contract](#write-contract) · [Geology source boundary](#geology-source-boundary) · [Exclusions](#exclusions) · [Validation](#required-checks-before-use) · [Status](#status-notes)

> [!CAUTION]
> `data/registry/geology/sources/` is a source-registry lane for Geology admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is a compatibility and navigation surface. It may contain only this README, links to canonical records, separately authorized migration or tombstone metadata, and a verified one-way generated view that satisfies the write contract below. It must not contain independently authored source descriptors, activation or intake sidecars, source-family indexes, source-authority records, or manually copied registry state.

Canonical Geology source registry records under `data/registry/sources/` describe how a source may be treated before source material reaches RAW. Those canonical records may record:

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

## Authority and path posture

`data/registry/geology/sources/` is an existing domain-first compatibility and navigation surface. Adopted Directory Rules v2 and ADR-0029 resolve its authority:

- `DIR-SOURCE-003` places machine source identities and descriptors under `data/registry/sources/`;
- `DIR-SOURCE-004` permits `data/registry/<domain>/sources/` only as a generated view, never as an independent writer when the canonical source registry is authoritative;
- this README may explain and link, but it does not admit, activate, mutate, or duplicate source descriptors.

**Placement result:** `DENY` independent descriptor writes here. A generated Geology view is `MIRROR`-eligible only after its canonical inputs, generator, owner, digests, parity check, consumers, correction path, rollback target, and exit criteria are verified. Until then, retain this README-only compatibility surface and route machine records through the accepted subtype-first registry topology.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Canonical Geology source descriptor/admission records | `data/registry/sources/` using the accepted source-identity topology | Source identity, role, rights, terms, cadence, sensitivity, activation, supersession, and authority limits. This compatibility path is not a writer. |
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

## Write contract

### Allowed here

- this compatibility README;
- links to canonical source records and governing contracts, schemas, policy, receipts, proofs, catalogs, corrections, rollback targets, and release decisions;
- a verified one-way generated index whose entries resolve to canonical records without minting local identities or weakening role, rights, sensitivity, time, provenance, or correction state;
- migration or tombstone metadata required by an accepted migration.

### Not allowed here

- independently authored `SourceDescriptor`, intake, activation, or source-authority records;
- manually copied descriptor indexes;
- source payloads, secrets, restricted details, proofs, catalogs, policy, contracts, schemas, or release objects;
- any public-serving, activation, promotion, proof, release, or publication path.

A future generated view must fail closed on missing or ambiguous canonical identity, digest mismatch, unresolved rights or sensitivity, stale input, role mismatch, parity failure, or absent rollback evidence.

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

<a id="suggested-directory-shape"></a>
## Retired directory sketch

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

This earlier sketch is retired. Do not materialize it at this compatibility path. Any generated view must be derived one-way from canonical source records with parity, correction, and rollback evidence.

---

<a id="suggested-descriptor-shape"></a>
## Retired descriptor sketch

The illustrative descriptor below is retained only as historical documentation context and is not an accepted schema or authorization to write records here. Canonical contracts and schemas govern actual descriptor shape; their current pairing remains **NEEDS VERIFICATION**.

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

- [ ] Confirm every machine descriptor write resolves to the accepted canonical topology under `data/registry/sources/`; do not add descriptors here.
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
| The authority relationship is resolved: canonical machine descriptors use `data/registry/sources/`; this path is compatibility/generated-view only. | CONFIRMED by adopted ADR-0029 and `DIR-SOURCE-003/004` |
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

---

## Change history

### v0.3.1 — 2026-07-28

- removed conflicting Scope language that could be read as authorizing independent descriptor, activation, intake, or index writes at this compatibility path;
- qualified source-registry semantics as belonging to canonical records under `data/registry/sources/`;
- repaired the quick-link targets for validation and status without changing any registry, source, lifecycle, proof, release, or publication state.

### v0.3.0 — 2026-07-28

- aligned this path with adopted ADR-0029 and `DIR-SOURCE-003/004`;
- classified it as a compatibility/generated view with no independent descriptor writes;
- retired the local directory and descriptor sketches as implementation guidance;
- preserved Geology source-role, rights, sensitivity, evidence, correction, rollback, and public-boundary controls.

### v0.2.0 — 2026-06-28

- replaced the original placeholder with a detailed Geology source-registry boundary;
- recorded the then-unresolved domain-first versus subtype-first path conflict.

[Back to top](#top)
