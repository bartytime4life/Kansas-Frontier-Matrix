<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/habitat/sources/readme
name: Habitat Source Registry README
path: data/registry/habitat/sources/README.md
type: data-registry-habitat-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <habitat-domain-steward>
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
registry_scope: habitat-source-descriptor-records
domain: habitat
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-habitat; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; sensitive-joins-fail-closed; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/habitat/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/habitat/
  - ../../../work/habitat/
  - ../../../quarantine/habitat/
  - ../../../processed/habitat/
  - ../../../catalog/domain/habitat/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../../contracts/domains/habitat/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - habitat
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - land-cover
  - wetlands
  - stewardship
  - ecological-systems
  - critical-habitat
  - occurrence-context
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/habitat/sources/README.md`."
  - "Habitat source registry records are admission and authority-control records. They do not store source payloads, prove habitat claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Habitat source-registry doctrine names `data/registry/sources/habitat/` as the machine-readable registry lane and explicitly notes a path-form question between `sources/habitat` and `habitat`. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Sensitive joins, occurrence-context inputs, controlled ecological records, rights-unclear feeds, and source-role conflicts fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Source Registry

Domain-first registry lane for Habitat source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Habitat source boundary](#habitat-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/habitat/sources/` is a source-registry lane for Habitat admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Habitat source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Habitat lane.

Habitat source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity and geoprivacy posture, especially for sensitive joins;
- cadence, source head, retrieval window, source vintage, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, and rollback requirements.

They do **not** record habitat truth. A source descriptor can authorize or deny admission conditions, but every habitat claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/habitat/sources/
```

This is a domain-first registry path. Current Habitat source-registry doctrine and source-ledger docs name the subtype-first pattern as the machine-readable source registry home:

```text
data/registry/sources/habitat/
```

Habitat source-registry doctrine also identifies the `sources/habitat` versus `habitat` path form as an open question. Because both patterns are visible in repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory or ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/habitat/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Habitat source descriptor/admission records | `data/registry/habitat/sources/` and/or `data/registry/sources/habitat/` after topology reconciliation | Source identity, role, rights, terms, cadence, sensitivity, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Habitat source orientation | `docs/domains/habitat/SOURCE_REGISTRY.md`, `HABITAT_SOURCE_LEDGER.md`, `SOURCES.md`, `SOURCE_FAMILIES.md` | Explains source families, admission posture, source-role discipline, and ledger state; not machine descriptor storage. |
| Habitat source payloads | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` | Actual data belongs in lifecycle lanes, not registry records. |
| Habitat domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Habitat semantic meaning | `contracts/domains/habitat/` | Object-family meaning and invariants. |
| Habitat machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/habitat/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Habitat policy and sensitivity | `policy/domains/habitat/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, source-role, join sensitivity, and admissibility rules. |
| Habitat validation receipts | `data/receipts/validation/habitat/` if/when accepted | Process memory for validation checks. |
| Habitat proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Habitat catalog projections | `data/catalog/domain/habitat/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Habitat release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Habitat source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, or public presentation. |
| Descriptor is not habitat truth | NLCD, NWI, GAP, LANDFIRE, ECOS, NatureServe, KDWP, PAD-US, occurrence aggregators, remote-sensing vegetation indices, field surveys, and steward-reviewed models still require evidence and review before claims. |
| Habitat does not own occurrence truth | Occurrence aggregators and Flora/Fauna occurrence records are join context unless the owning lane releases a public-safe derivative. |
| Sensitive joins fail closed | Public-safe habitat context can become restricted when joined to sensitive Flora/Fauna, heritage, stewardship, or other protected context. The most restrictive joined tier governs. |
| Regulatory and modeled products remain scoped | Critical-habitat designations, wetland inventories, modeled suitability layers, and stewardship overlays must retain their source role and authority limits. |
| Models are not observations | Modeled habitat, suitability, ecological-system, or restoration-priority layers require model identity, run receipts, uncertainty, and source-role preservation. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Habitat source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, and authority-scope metadata;
- source vintage, class-system version, map/service version, model lineage, and source-head metadata summaries;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, sensitive joined details, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or habitat claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Habitat source payloads, land-cover packages, wetland inventories, stewardship layers, ecological-system tables, remote-sensing products, field-survey files, model outputs, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, or `data/processed/habitat/` depending on lifecycle state |
| Sensitive joined context, protected occurrence-derived locations, steward-only notes, private identifiers, access secrets, or restricted review material | restricted lifecycle lane, quarantine, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/habitat/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/habitat/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/habitat/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Habitat layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/habitat/sources/
├── README.md
├── land_cover/
│   ├── README.md
│   └── index.local.json
├── wetlands/
│   ├── README.md
│   └── index.local.json
├── ecological_systems/
│   ├── README.md
│   └── index.local.json
├── critical_habitat/
│   ├── README.md
│   └── index.local.json
├── stewardship/
│   ├── README.md
│   └── index.local.json
├── occurrence_context/
│   ├── README.md
│   └── index.local.json
├── remote_sensing/
│   ├── README.md
│   └── index.local.json
├── field_surveys/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/habitat/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Habitat source registry record should be structured enough for audit, admission, validation, correction, and rollback.

```json
{
  "id": "kfm-source:habitat:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "habitat",
  "source_family": "land_cover | wetlands | ecological_systems | critical_habitat | stewardship | occurrence_context | remote_sensing | field_surveys | model | context_layer | restricted_steward | other",
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

- [ ] Confirm whether `data/registry/habitat/sources/` or `data/registry/sources/habitat/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, source vintage, class-system version, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm occurrence context, habitat context, regulatory designations, observed land-cover, modeled suitability, stewardship overlays, and aggregate products are not collapsed.
- [ ] Confirm sensitive joined details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm joined products inherit the most restrictive applicable sensitivity posture and fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Habitat-owned truth beyond their admitted scope.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Habitat source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/habitat/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/habitat/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Habitat source-registry doctrine names `data/registry/sources/habitat/` as the machine-readable registry lane and notes the path-form question. | CONFIRMED by GitHub contents API during this edit |
| Habitat source ledger states authoritative SourceDescriptor records live under `data/registry/sources/habitat/` and that admission is deny-by-default until descriptor and activation decision exist. | CONFIRMED by GitHub contents API during this edit |
| Habitat source ledger describes occurrence aggregators as join context and warns joined products inherit the most restrictive applicable tier. | CONFIRMED by GitHub contents API during this edit |
| Concrete Habitat source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/habitat/sources/` and `data/registry/sources/habitat/` is resolved. | NEEDS VERIFICATION |
| A canonical Habitat source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Habitat source registry records. | UNKNOWN |
| This README grants public access to Habitat source registry internals. | DENY |

---

## Maintainer note

Habitat source registry records are useful because they make source identity, source role, rights, sensitivity, cadence, activation, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Habitat truth
```
