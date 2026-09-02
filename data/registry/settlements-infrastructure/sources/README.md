<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/settlements-infrastructure/sources/readme
name: Settlements Infrastructure Source Registry README
path: data/registry/settlements-infrastructure/sources/README.md
type: data-registry-settlements-infrastructure-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <settlements-infrastructure-domain-steward>
  - <settlements-steward>
  - <infrastructure-steward>
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
registry_scope: settlements-infrastructure-source-descriptor-records
domain: settlements-infrastructure
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-path-doc-names-data-registry-sources-or-data-registry-settlements-infrastructure-as-proposed; pipeline-doc-points-to-data-registry-sources-settlements-infrastructure; final-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; critical-asset-detail-deny-default; exact-facility-geometry-reviewed; operator-condition-dependency-context-fail-closed; private-property-living-person-cultural-context-reviewed; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/settlements-infrastructure/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../rights/README.md
  - ../../sensitivity/README.md
  - ../../layers/README.md
  - ../../../raw/settlements-infrastructure/
  - ../../../work/settlements-infrastructure/
  - ../../../quarantine/settlements-infrastructure/
  - ../../../processed/settlements-infrastructure/
  - ../../../catalog/domain/settlements-infrastructure/
  - ../../../triplets/settlements-infrastructure/
  - ../../../published/layers/settlements-infrastructure/
  - ../../../receipts/settlements-infrastructure/
  - ../../../proofs/settlements-infrastructure/
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../../contracts/domains/settlements-infrastructure/README.md
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../../policy/domains/settlements-infrastructure/
  - ../../../../policy/sensitivity/infrastructure/
  - ../../../../policy/rights/
  - ../../../../pipelines/domains/settlements-infrastructure/README.md
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - settlements-infrastructure
  - settlements
  - infrastructure
  - sources
  - source-descriptor
  - source-role
  - municipalities
  - census-places
  - townsites
  - ghost-towns
  - forts
  - missions
  - reservation-communities
  - infrastructure-assets
  - facilities
  - service-areas
  - operators
  - condition-observations
  - dependencies
  - critical-assets
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/settlements-infrastructure/sources/README.md`."
  - "Settlements/Infrastructure source registry records are admission and authority-control records. They do not store source payloads, prove settlement/facility/legal/operational claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Domain docs identify the hyphenated `settlements-infrastructure` slug while noting path-shape conflicts with singular `settlement` and infrastructure policy lanes; this source-registry README preserves the requested path and marks final topology NEEDS VERIFICATION."
  - "Critical infrastructure, exact facility geometry, operator-sensitive, condition, dependency, private-property, living-person, cultural, emergency-adjacent, and public-safety-relevant details fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Source Registry

Domain-first registry lane for Settlements / Infrastructure source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-7048e8">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not operational truth" src="https://img.shields.io/badge/boundary-not%20operational%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Settlements/Infrastructure source boundary](#settlementsinfrastructure-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/settlements-infrastructure/sources/` is a source-registry lane for Settlements / Infrastructure admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, legal-status authority, operational-status authority, emergency guidance, infrastructure-security guidance, or generated-answer authority.

---

## Scope

This directory documents and may hold Settlements / Infrastructure source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Settlements / Infrastructure lane.

Settlements / Infrastructure source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, endpoint terms, steward obligations, and access posture;
- sensitivity posture for settlements, historic places, critical assets, facilities, networks, service areas, operators, condition observations, dependencies, private-property context, living-person context, cultural context, and public-safety-relevant material;
- cadence, source head, retrieval window, source vintage, effective time, valid time, release time, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required quarantine, validation, normalization, geocoding, redaction, generalization, proof, catalog, release, correction, stale-state, withdrawal, and rollback requirements.

They do **not** prove that a settlement, municipality, census place, townsite, fort, mission, reservation community, facility, network asset, service area, operator, condition, dependency, address, boundary, access condition, legal status, ownership, service availability, emergency readiness, or operational state is true, current, complete, public-safe, or release-approved. A source descriptor can authorize or deny admission conditions, but every consequential claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/settlements-infrastructure/sources/
```

This is a domain-first registry path. Other KFM registry lanes also use subtype-first patterns such as:

```text
data/registry/sources/<domain>/
data/registry/datasets/<domain>/
data/registry/domains/<domain>/
data/registry/crosswalks/<domain-or-scope>/
data/registry/rights/<domain-or-scope>/
data/registry/sensitivity/<domain-or-scope>/
```

Settlements / Infrastructure path doctrine confirms the hyphenated `settlements-infrastructure` domain slug, but it also records slug/path variance with singular `settlement` and infrastructure policy projections. Domain documentation lists source-descriptor registry entries under `data/registry/sources/` or `data/registry/settlements-infrastructure/` as proposed homes, while the pipeline README points to `data/registry/sources/settlements-infrastructure/` as a related source-registry lane.

Therefore, this requested path is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. If `data/registry/sources/settlements-infrastructure/` is later accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Settlements / Infrastructure source descriptor/admission records | `data/registry/settlements-infrastructure/sources/` and/or reconciled `data/registry/sources/settlements-infrastructure/` | Source identity, role, rights, terms, cadence, activation, authority limits, and caveats. |
| Domain-first registry parent | `data/registry/settlements-infrastructure/` | Parent currently exists as a stub; topology remains NEEDS VERIFICATION. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Settlements / Infrastructure source payloads | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, `data/processed/settlements-infrastructure/` | Actual data belongs in lifecycle lanes, not registry records. |
| Human-facing domain doctrine | `docs/domains/settlements-infrastructure/README.md` | Explains domain scope and source families; not registry storage. |
| Canonical path guidance | `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` | Path registry and slug-variance control surface; not source descriptors. |
| Semantic meaning | `contracts/domains/settlements-infrastructure/` | Object-family meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/settlements-infrastructure/`, or ADR-selected schema lane | Schema enforcement; exact source descriptor schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/settlements-infrastructure/`, `policy/sensitivity/infrastructure/`, `policy/rights/`, and accepted sensitivity/access policy lanes | Access, rights, sensitivity, stale-state, dependency, infrastructure, privacy, and release rules. |
| Pipeline logic | `pipelines/domains/settlements-infrastructure/` | Executable transformation support only; not source descriptors, data, policy, proof, release, or public authority. |
| Validation/redaction/pipeline receipts | `data/receipts/settlements-infrastructure/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/settlements-infrastructure/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/settlements-infrastructure/`, `data/triplets/settlements-infrastructure/`, and accepted graph/catalog lanes | Catalog/discovery carriers and derived relationship projections after catalog closure. |
| Release decisions | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/`, and release roots | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Settlements/Infrastructure source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source is not legal or operational authority | A source descriptor does not make KFM the authority for municipal status, address validity, land access, service availability, facility condition, utility dependency, emergency readiness, or operational instructions. |
| Source role is fixed at admission | Observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, or restricted roles must not be upgraded by processing, normalization, geocoding, cataloging, rendering, or generated explanation. |
| Current status requires current-source support | Municipal status, facility operation, condition observations, dependencies, service areas, ownership/operator state, and infrastructure condition claims must carry source time, valid/effective time, retrieval time, stale-state handling, and authority limits. |
| Historic and cultural places carry uncertainty | Townsites, ghost towns, forts, missions, reservation communities, boundary changes, name changes, and historical settlement references must preserve source vintage, method, confidence, and geometry uncertainty. |
| Geometry is not legal status | Points, polygons, addresses, footprints, service areas, networks, and boundaries do not prove legal existence, jurisdiction, ownership, access, service entitlement, safety, or current operational state by themselves. |
| Infrastructure-sensitive context fails closed | Critical assets, exact facility geometry, dependency chains, utility/security-sensitive detail, private-property context, and public-safety-relevant fields require policy review before exposure. |
| Living-person and private-property joins fail closed | Address, operator, parcel, owner, tenant, resident, employee, facility, and service-dependency joins must not expose living-person or private-property detail without explicit policy support. |
| Rights and restrictions travel | License, attribution, redistribution, endpoint terms, source restrictions, private-source restrictions, and steward caveats must remain attached downstream. |
| Registry is not validation | Validation receipts, geocoding receipts, normalization receipts, redaction receipts, policy receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Settlements / Infrastructure source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, license, attribution, redistribution, cadence, access, endpoint, terms, steward, authority-scope, and caveat metadata;
- source vintage, jurisdiction, geography, spatial precision, temporal precision, operator/owner assertion scope, infrastructure context, retrieval refs, and stale-state notes;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation/geocoding/redaction receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed source payloads, full facility inventories, condition feeds, dependency graphs, proof packs, policy decisions, catalog records, release manifests, emergency instructions, infrastructure-security detail, or Settlements / Infrastructure claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw settlement, municipal, census, facility, address, building, utility, service-area, operator, condition, dependency, parcel, infrastructure, or historic-place payloads | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, or `data/processed/settlements-infrastructure/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| Pipeline logic | `pipelines/domains/settlements-infrastructure/` |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Rights registry records | `data/registry/rights/` after accepted rights-registry topology |
| Sensitivity registry records | `data/registry/sensitivity/` after accepted sensitivity-registry topology |
| Layer registry records | `data/registry/layers/` after accepted layer-registry topology |
| Semantic object contracts | `contracts/domains/settlements-infrastructure/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/settlements-infrastructure/` |
| Policy rules, sensitivity rules, rights rules, access-control logic, stale-state rules, public-safety rules, or release rules | `policy/` |
| Validation receipts, geocoding receipts, redaction receipts, pipeline receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Emergency guidance, legal access advice, utility operations instructions, infrastructure-security instructions, or safety instructions | out of scope for KFM public interpretive surfaces; use official operational systems |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/settlements-infrastructure/sources/
├── README.md
├── settlements/
│   ├── README.md
│   └── index.local.json
├── municipalities_census_places/
│   ├── README.md
│   └── index.local.json
├── historic_places/
│   ├── README.md
│   └── index.local.json
├── reservation_communities/
│   ├── README.md
│   └── index.local.json
├── infrastructure_assets/
│   ├── README.md
│   └── index.local.json
├── facilities_service_areas/
│   ├── README.md
│   └── index.local.json
├── operators_condition_observations/
│   ├── README.md
│   └── index.local.json
├── dependencies_networks/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/settlements-infrastructure/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Settlements / Infrastructure source registry record should be structured enough for audit, admission, validation, stale-state handling, correction, and rollback.

```json
{
  "id": "kfm-source:settlements-infrastructure:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "settlements-infrastructure",
  "source_family": "settlements | municipalities_census_places | historic_places | reservation_communities | infrastructure_assets | facilities_service_areas | operators_condition_observations | dependencies_networks | other",
  "source_name": "Human-readable source name",
  "source_role": "observed | regulatory | administrative | modeled | aggregate | candidate | context | synthetic | restricted",
  "authority_scope": "What this source may and may not support",
  "rights_posture": "open | attribution-required | restricted | unknown | denied | needs-review",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | user-supplied | unknown",
  "source_time_kind_refs": [],
  "stale_state_refs": [],
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "geocoding_receipt_refs": [],
  "redaction_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | restricted | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/settlements-infrastructure/sources/` or `data/registry/sources/settlements-infrastructure/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, rights record, sensitivity record, layer record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, jurisdiction, retrieval time, valid/effective time, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, geocoding, conflation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm settlement identity, legal status, jurisdiction, facility identity, service availability, operator state, condition observation, dependency, and public-safety context are not collapsed.
- [ ] Confirm historic-place uncertainty, naming changes, boundary changes, source vintage, method lineage, and geometry uncertainty remain explicit.
- [ ] Confirm current-status, condition, service, operator, dependency, emergency-adjacent, or operational claims carry official source scope, valid/effective time, stale-state handling, and release posture.
- [ ] Confirm critical assets, exact facility geometry, private property, living-person, cultural, security-sensitive, utility-sensitive, or dependency-chain details are not exposed in registry files, local indexes, public summaries, vector indexes, map labels, or generated responses.
- [ ] Confirm validation, geocoding, normalization, redaction, and policy receipts exist before catalog, graph projection, or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, rights-change, sensitivity-change, and rollback paths exist for mutable, time-bound, rights-bound, sensitivity-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/settlements-infrastructure/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/settlements-infrastructure/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Settlements / Infrastructure canonical-path docs confirm the hyphenated `settlements-infrastructure` slug and record path-shape variance with singular `settlement` and infrastructure policy projections. | CONFIRMED by GitHub contents API during this edit |
| Settlements / Infrastructure domain README says source-descriptor registry entries belong under `data/registry/sources/` or `data/registry/settlements-infrastructure/` as proposed homes and that lifecycle data, contracts, schemas, policy, catalog, and release have separate roots. | CONFIRMED by GitHub contents API during this edit |
| Contract-lane README says contracts do not host schemas, policy, fixtures, tests, packages, pipelines, registries, source data, lifecycle data, release decisions, or public artifacts. | CONFIRMED by GitHub contents API during this edit |
| Pipeline README says pipeline logic does not own object meaning, schemas, policy, source descriptors, legal status, operational status, lifecycle storage, catalog truth, or release approval. | CONFIRMED by GitHub contents API during this edit |
| Concrete Settlements / Infrastructure source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first source registry lanes is resolved. | NEEDS VERIFICATION |
| A canonical Settlements / Infrastructure source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Settlements / Infrastructure source registry records. | UNKNOWN |
| This README grants public access to Settlements / Infrastructure source registry internals. | DENY |

---

## Maintainer note

Settlements / Infrastructure source registry records are useful because they make source identity, source role, rights, cadence, authority limits, stale-state, critical-asset context, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, legal status truth, infrastructure truth, operational truth, or public guidance. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> rights/sensitivity/stale-state gate -> RAW admission -> lifecycle processing -> validation/geocoding/redaction receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Settlements / Infrastructure truth
```
