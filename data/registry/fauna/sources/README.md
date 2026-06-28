<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/fauna/sources/readme
name: Fauna Source Registry README
path: data/registry/fauna/sources/README.md
type: data-registry-fauna-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <fauna-domain-steward>
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
registry_scope: fauna-source-descriptor-records
domain: fauna
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-fauna; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; deny-by-default-sensitive-sites; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/fauna/
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../../raw/fauna/
  - ../../../work/fauna/
  - ../../../quarantine/fauna/
  - ../../../processed/fauna/
  - ../../../catalog/domain/fauna/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../docs/sources/catalog/gbif/occurrence-api.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../policy/domains/fauna/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - fauna
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - nests
  - dens
  - roosts
  - hibernacula
  - spawning-sites
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/fauna/sources/README.md`."
  - "Fauna source registry records are admission and authority-control records. They do not store source payloads, prove observations, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Fauna source-registry doctrine names `data/registry/sources/fauna/` as the canonical machine-readable registry lane. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Fauna exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, and steward-controlled records carry deny-by-default sensitivity until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Source Registry

Domain-first registry lane for Fauna source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Fauna source boundary](#fauna-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/fauna/sources/` is a source-registry lane for Fauna admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Fauna source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Fauna lane.

Fauna source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity and geoprivacy posture;
- cadence, source head, retrieval window, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, and rollback requirements.

They do **not** record animal truth. A source descriptor can authorize or deny admission conditions, but every animal claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/fauna/sources/
```

This is a domain-first registry path. Current Fauna source-registry doctrine and the cross-domain source registry README name the subtype-first pattern as the machine-readable source registry home:

```text
data/registry/sources/fauna/
```

Because both patterns are visible in the repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory/ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/fauna/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Fauna source descriptor/admission records | `data/registry/fauna/sources/` and/or `data/registry/sources/fauna/` after topology reconciliation | Source identity, role, rights, terms, cadence, sensitivity, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Fauna source orientation | `docs/domains/fauna/SOURCE_REGISTRY.md`, `SOURCES.md`, `SOURCE_FAMILIES.md`, `SOURCE_ROLES.md` | Explains source families and role discipline; not machine descriptor storage. |
| Fauna source payloads | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` | Actual data belongs in lifecycle lanes, not registry records. |
| Fauna domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Fauna semantic meaning | `contracts/domains/fauna/` | Object-family meaning and invariants. |
| Fauna machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Fauna policy and sensitivity | `policy/domains/fauna/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, geoprivacy, source-role, and admissibility rules. |
| Fauna validation receipts | `data/receipts/validation/fauna/` if/when accepted | Process memory for validation checks. |
| Fauna proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Fauna catalog projections | `data/catalog/domain/fauna/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Fauna release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Fauna source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, or public presentation. |
| Aggregator is not a role | GBIF, iNaturalist, eBird, iDigBio, BISON-like systems, and similar aggregators require underlying role and evidence discipline. |
| Sensitive sites fail closed | Exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, breeding sites, and steward-controlled records are denied or restricted unless policy/review/redaction gates explicitly permit a public-safe derivative. |
| Context is not Fauna truth | Habitat, soil, hydrology, land cover, PAD-US, NWI, roads, settlements, and similar context sources support governed joins only. They do not become animal occurrence truth. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Fauna source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, and authority-scope metadata;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, sensitive coordinates, proof packs, policy decisions, catalog records, release manifests, or source-native dumps in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Fauna source payloads, occurrence downloads, telemetry feeds, disease surveillance data, mortality reports, acoustic files, eDNA results, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, or `data/processed/fauna/` depending on lifecycle state |
| Exact sensitive coordinates, nests, dens, roosts, hibernacula, spawning sites, breeding sites, private identifiers, steward-only notes, tokens, credentials, or API keys | restricted lifecycle lane, quarantine, secret manager, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/fauna/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/fauna/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/fauna/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Fauna layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/fauna/sources/
├── README.md
├── authority/
│   ├── README.md
│   └── index.local.json
├── observations/
│   ├── README.md
│   └── index.local.json
├── aggregators/
│   ├── README.md
│   └── index.local.json
├── heritage_status/
│   ├── README.md
│   └── index.local.json
├── invasive_species/
│   ├── README.md
│   └── index.local.json
├── context_layers/
│   ├── README.md
│   └── index.local.json
├── restricted_steward/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/fauna/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Fauna source registry record should be structured enough for audit, admission, validation, correction, and rollback.

```json
{
  "id": "kfm-source:fauna:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "fauna",
  "source_family": "authority | observation | aggregator | heritage_status | invasive_species | context_layer | restricted_steward | other",
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

- [ ] Confirm whether `data/registry/fauna/sources/` or `data/registry/sources/fauna/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm nests, dens, roosts, hibernacula, spawning sites, exact sensitive occurrence geometry, and steward-controlled records fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Fauna truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Fauna source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/fauna/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/fauna/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and defines the source registry as an admission and authority-control surface, not a bibliography. | CONFIRMED by GitHub contents API during this edit |
| Fauna source-registry doctrine names `data/registry/sources/fauna/` as the machine-readable registry lane and treats the docs file as human-facing orientation. | CONFIRMED by GitHub contents API during this edit |
| Fauna source-role docs state SourceDescriptor source_role uses the canonical seven-class enum and wins over docs on conflict. | CONFIRMED by GitHub contents API during this edit |
| Fauna lifecycle docs require SourceDescriptor at RAW admission and deny-by-default handling for sensitive sites. | CONFIRMED by GitHub contents API during this edit |
| Concrete Fauna source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/fauna/sources/` and `data/registry/sources/fauna/` is resolved. | NEEDS VERIFICATION |
| A canonical Fauna source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Fauna source registry records. | UNKNOWN |
| This README grants public access to Fauna source registry internals. | DENY |

---

## Maintainer note

Fauna source registry records are useful because they make source identity, source role, rights, sensitivity, cadence, activation, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Fauna truth
```
