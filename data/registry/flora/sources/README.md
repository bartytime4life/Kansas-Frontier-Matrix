<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/flora/sources/readme
name: Flora Source Registry README
path: data/registry/flora/sources/README.md
type: data-registry-flora-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <flora-domain-steward>
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
registry_scope: flora-source-descriptor-records
domain: flora
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-flora; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; rare-plant-deny-default; culturally-sensitive-plant-knowledge-protected; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/flora/
  - ../../datasets/README.md
  - ../../datasets/flora/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/flora/
  - ../../../work/flora/
  - ../../../quarantine/flora/
  - ../../../processed/flora/
  - ../../../catalog/domain/flora/
  - ../../../catalog/stac/flora/README.md
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../../docs/domains/flora/SOURCES.md
  - ../../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/sources/catalog/gbif/async-download.md
  - ../../../../docs/sources/catalog/natureserve/sensitive-taxa-list.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../policy/domains/flora/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - flora
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - rare-plants
  - culturally-sensitive-plants
  - taxonomy
  - specimens
  - occurrences
  - vegetation
  - invasive-plants
  - phenology
  - restoration
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/flora/sources/README.md`."
  - "Flora source registry records are admission and authority-control records. They do not store source payloads, prove plant occurrences, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Flora source-registry doctrine names `data/registry/sources/flora/` as the machine-readable registry lane. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Rare-plant exact geometry, culturally sensitive plant knowledge, steward-controlled records, rights-unclear feeds, taxonomy collisions, and join-induced sensitivity fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Source Registry

Domain-first registry lane for Flora source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Flora source boundary](#flora-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/flora/sources/` is a source-registry lane for Flora admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Flora source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Flora lane.

Flora source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity and geoprivacy posture;
- cadence, source head, retrieval window, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, and rollback requirements.

They do **not** record botanical truth. A source descriptor can authorize or deny admission conditions, but every plant claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/flora/sources/
```

This is a domain-first registry path. Current Flora source-registry doctrine names the subtype-first pattern as the machine-readable source registry home:

```text
data/registry/sources/flora/
```

Because both patterns are visible in repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory/ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/flora/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora source descriptor/admission records | `data/registry/flora/sources/` and/or `data/registry/sources/flora/` after topology reconciliation | Source identity, role, rights, terms, cadence, sensitivity, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Flora source orientation | `docs/domains/flora/SOURCE_REGISTRY.md`, `SOURCE_FAMILIES.md`, `SOURCES.md`, `SOURCE_INTAKE.md` | Explains source families, descriptor expectations, and intake mechanics; not machine descriptor storage. |
| Flora source payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not registry records. |
| Flora domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Flora semantic meaning | `contracts/domains/flora/` | Object-family meaning and invariants. |
| Flora machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/flora/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Flora policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, geoprivacy, source-role, and admissibility rules. |
| Flora validation receipts | `data/receipts/validation/flora/` | Process memory for validation checks. |
| Flora proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Flora catalog projections | `data/catalog/domain/flora/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Flora release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Flora source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, or public presentation. |
| Descriptor is not botanical truth | PLANTS, GBIF, iNaturalist, NatureServe, herbarium, vegetation, invasive, phenology, restoration, and remote-sensing sources still require evidence and review before claims. |
| Rare and sensitive plant data fail closed | Exact rare/protected/culturally sensitive plant locations, steward-controlled records, and culturally sensitive plant knowledge are denied or restricted unless policy/review/redaction gates explicitly permit a public-safe derivative. |
| Context is not Flora truth | Soil, hydrology, habitat, land cover, roads, settlements, archaeology, and similar context sources support governed joins only. They do not become botanical occurrence truth. |
| Watchers are non-publishers | Source-health, source-head, and drift watchers may create candidate intake records; they must not write directly to processed, catalog, published, or public surfaces. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Flora source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, and authority-scope metadata;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, sensitive coordinates, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or botanical claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads, herbarium archives, occurrence exports, taxonomy tables, rare-plant feeds, vegetation datasets, invasive records, phenology feeds, restoration records, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Exact rare/protected/culturally sensitive plant coordinates, steward-only notes, private identifiers, tokens, credentials, API keys, or culturally sensitive plant knowledge | restricted lifecycle lane, quarantine, secret manager, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/flora/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` or `data/registry/datasets/flora/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/flora/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/flora/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Flora layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/flora/sources/
├── README.md
├── taxonomy/
│   ├── README.md
│   └── index.local.json
├── specimens/
│   ├── README.md
│   └── index.local.json
├── occurrences/
│   ├── README.md
│   └── index.local.json
├── rare_plants/
│   ├── README.md
│   └── index.local.json
├── vegetation/
│   ├── README.md
│   └── index.local.json
├── invasive_plants/
│   ├── README.md
│   └── index.local.json
├── phenology/
│   ├── README.md
│   └── index.local.json
├── restoration/
│   ├── README.md
│   └── index.local.json
├── remote_sensing/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/flora/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Flora source registry record should be structured enough for audit, admission, validation, correction, and rollback.

```json
{
  "id": "kfm-source:flora:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "flora",
  "source_family": "taxonomy | specimen | occurrence | rare_plant | vegetation | invasive_plant | phenology | restoration | remote_sensing | context_layer | restricted_steward | other",
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

- [ ] Confirm whether `data/registry/flora/sources/` or `data/registry/sources/flora/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations, steward-controlled records, culturally sensitive plant knowledge, and join-induced sensitivity fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Flora truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Flora source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/flora/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/flora/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Flora source-registry doctrine names `data/registry/sources/flora/` as the machine-readable registry lane and treats this docs file as human-readable doctrine. | CONFIRMED by GitHub contents API during this edit |
| Flora data lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and place watchers/source-head checks at the pre-RAW edge. | CONFIRMED by GitHub contents API during this edit |
| Flora lifecycle docs identify rare-plant exact geometry, rights-unclear feeds, taxonomy collisions, and join-induced sensitivity as quarantine concerns. | CONFIRMED by GitHub contents API during this edit |
| Concrete Flora source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/flora/sources/` and `data/registry/sources/flora/` is resolved. | NEEDS VERIFICATION |
| A canonical Flora source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Flora source registry records. | UNKNOWN |
| This README grants public access to Flora source registry internals. | DENY |

---

## Maintainer note

Flora source registry records are useful because they make source identity, source role, rights, sensitivity, cadence, activation, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Flora truth
```
