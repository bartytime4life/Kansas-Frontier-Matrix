<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/settlements-infrastructure/readme
name: Settlements Infrastructure Registry README
path: data/registry/settlements-infrastructure/README.md
type: data-registry-settlements-infrastructure-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <settlements-infrastructure-domain-steward>
  - <settlements-steward>
  - <infrastructure-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: settlements-infrastructure-domain-first-registry-parent
domain: settlements-infrastructure
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-path-doc-confirms-hyphenated-slug-but-records-settlement-and-infrastructure-policy-variance; subtype-first-source-registry-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; precise-facility-context-reviewed; operator-condition-dependency-context-fail-closed; private-property-living-person-cultural-context-reviewed; legal-and-operational-status-not-authoritative; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/settlements-infrastructure/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../layers/README.md
  - sources/README.md
  - ../../raw/settlements-infrastructure/
  - ../../work/settlements-infrastructure/
  - ../../quarantine/settlements-infrastructure/
  - ../../processed/settlements-infrastructure/
  - ../../catalog/domain/settlements-infrastructure/
  - ../../triplets/settlements-infrastructure/
  - ../../published/layers/settlements-infrastructure/
  - ../../receipts/settlements-infrastructure/
  - ../../proofs/settlements-infrastructure/
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../contracts/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../policy/sensitivity/infrastructure/
  - ../../../policy/rights/
  - ../../../pipelines/domains/settlements-infrastructure/README.md
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - settlements-infrastructure
  - domain-first-registry
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
  - legal-status
  - operational-status
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/settlements-infrastructure/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The domain canonical-path document confirms the hyphenated `settlements-infrastructure` slug while recording path-shape variance with singular `settlement` and infrastructure policy projections."
  - "This parent is a compatibility/routing lane until registry topology is reconciled. It must not become source payload storage, contract/schema/policy authority, legal or operational status authority, proof, catalog, release, or public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure Registry

Domain-first registry parent for Settlements / Infrastructure registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-7048e8">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not operational truth" src="https://img.shields.io/badge/boundary-not%20operational%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Registry boundary](#registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/settlements-infrastructure/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, legal-status authority, operational-status authority, or generated-answer authority.

---

## Scope

`data/registry/settlements-infrastructure/` is a domain-first routing lane for Settlements / Infrastructure registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for Settlements / Infrastructure sources.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Settlements / Infrastructure registry lane may point to or summarize governance state for:

- source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, cadence, source-head, activation, intake, correction, supersession, stale-state, withdrawal, and freshness state;
- settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, infrastructure asset, network node, network segment, facility, service-area, operator, condition-observation, and dependency context;
- precise facility context, operator-sensitive context, condition context, dependency context, private-property context, living-person context, cultural context, legal-status context, operational-status context, and other policy-sensitive blockers;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, full inventories, precise restricted details, private-property details, living-person details, proof packs, catalog records, release manifests, public map artifacts, operational instructions, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/settlements-infrastructure/
```

This is a **domain-first** registry path. Current Settlements / Infrastructure source-registry evidence also supports subtype-first source registry patterns such as:

```text
data/registry/sources/settlements-infrastructure/
```

Settlements / Infrastructure canonical-path documentation confirms the hyphenated `settlements-infrastructure` domain slug, but it also records path-shape variance with singular `settlement` and infrastructure policy projections. The child source README preserves the requested domain-first path while marking final topology **NEEDS VERIFICATION**.

Therefore, `data/registry/settlements-infrastructure/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Settlements / Infrastructure domain-first registry parent | `data/registry/settlements-infrastructure/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed child registry lane | `data/registry/settlements-infrastructure/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical source lane | `data/registry/sources/settlements-infrastructure/` | Needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, names, boundaries, addresses, facilities, operators, service areas, dependencies, vocabularies, measures, classes, and domain lanes. |
| Rights registry records | `data/registry/rights/` | Rights review state and rights-readiness pointers. |
| Sensitivity registry records | `data/registry/sensitivity/` | Sensitivity, geoprivacy, redaction, review, and exposure-control state. |
| Layer registry records | `data/registry/layers/` | Layer identity and release-readiness pointers. |
| Settlements / Infrastructure source payloads | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, `data/processed/settlements-infrastructure/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Human-facing domain doctrine | `docs/domains/settlements-infrastructure/README.md` | Explains domain scope and source families; not registry storage. |
| Canonical path guidance | `docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` | Path registry and slug-variance control surface; not source descriptors. |
| Semantic meaning | `contracts/domains/settlements-infrastructure/` | Object-family meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/settlements-infrastructure/`, or ADR-selected schema lane | Schema enforcement; exact source/registry schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/settlements-infrastructure/`, `policy/sensitivity/infrastructure/`, `policy/rights/`, and accepted sensitivity/access policy lanes | Access, rights, sensitivity, stale-state, dependency, infrastructure, privacy, and release rules. |
| Pipeline logic | `pipelines/domains/settlements-infrastructure/` | Executable transformation support only; not registry data, policy, proof, release, or public authority. |
| Validation/redaction/pipeline receipts | `data/receipts/settlements-infrastructure/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/settlements-infrastructure/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/settlements-infrastructure/`, `data/triplets/settlements-infrastructure/`, and accepted graph/catalog lanes | Catalog/discovery carriers and derived relationship projections after catalog closure. |
| Release decisions | `release/candidates/settlements-infrastructure/`, `release/manifests/settlements-infrastructure/`, and release roots | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, public-safe summaries, or public UI behavior.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Settlements / Infrastructure source descriptor and source-admission registry lane. | Not source payload storage, settlement/facility/legal/operational truth, proof, receipt storage, catalog closure, semantic contract authority, schema authority, policy, release authority, or public output. |

---

## Registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/settlements-infrastructure/...` and `data/registry/sources/settlements-infrastructure/`. |
| Registry is not legal or operational authority | Registry state does not make KFM the authority for municipal status, address validity, access, service availability, facility condition, dependency state, or operational instructions. |
| Source role is preserved | Registry state must not upgrade observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, or restricted source roles. |
| Current status requires current-source support | Municipal status, facility operation, condition observations, dependencies, service areas, ownership/operator state, and infrastructure condition claims must carry source time, valid/effective time, retrieval time, stale-state handling, and authority limits. |
| Historic and cultural places carry uncertainty | Townsites, ghost towns, forts, missions, reservation communities, boundary changes, name changes, and historical settlement references must preserve source vintage, method, confidence, and geometry uncertainty. |
| Geometry is not legal status | Points, polygons, addresses, footprints, service areas, networks, and boundaries do not prove legal existence, jurisdiction, ownership, access, service entitlement, safety, or current operational state by themselves. |
| Sensitive context fails closed | Precise facility context, restricted detail, dependency context, private-property context, living-person context, and culturally sensitive context require policy review before exposure. |
| Rights and restrictions travel | License, attribution, redistribution, endpoint terms, source restrictions, private-source restrictions, and steward caveats must remain attached downstream. |
| Registry is not validation | Validation receipts, geocoding receipts, normalization receipts, redaction receipts, policy receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining domain-first versus subtype-first topology;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, rights registry records, sensitivity registry records, layer registry records, contracts, schemas, policy refs, lifecycle payloads, validation/geocoding/redaction receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw settlement, municipal, census, facility, address, building, service-area, operator, condition, dependency, parcel, infrastructure, or historic-place payloads | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, or `data/processed/settlements-infrastructure/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| Pipeline logic | `pipelines/domains/settlements-infrastructure/` |
| Canonical source descriptor records if a subtype-first lane is accepted as canonical | `data/registry/sources/settlements-infrastructure/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Rights registry records | `data/registry/rights/` after accepted rights-registry topology |
| Sensitivity registry records | `data/registry/sensitivity/` after accepted sensitivity-registry topology |
| Layer registry records | `data/registry/layers/` after accepted layer-registry topology |
| Semantic object contracts | `contracts/domains/settlements-infrastructure/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/settlements-infrastructure/` |
| Policy rules, sensitivity rules, rights rules, access-control logic, stale-state rules, or release rules | `policy/` |
| Validation receipts, geocoding receipts, redaction receipts, pipeline receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Legal advice, access advice, operational instructions, or safety instructions | out of scope for KFM public interpretive surfaces; use official systems of record |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/settlements-infrastructure/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/settlements-infrastructure/       # possible canonical source descriptors
data/registry/settlements-infrastructure/README.md      # compatibility pointer / migration note only
```

Do not maintain divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/settlements-infrastructure/...` or `data/registry/sources/settlements-infrastructure/` is canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, test, pipeline, or public artifact.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, jurisdiction, retrieval time, valid/effective time, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, current operational status, legal status, or public-safe posture.
- [ ] Confirm settlement identity, legal status, jurisdiction, facility identity, service availability, operator state, condition observation, dependency, and sensitivity context are not collapsed.
- [ ] Confirm historic-place uncertainty, naming changes, boundary changes, source vintage, method lineage, and geometry uncertainty remain explicit.
- [ ] Confirm current-status, condition, service, operator, dependency, or operational claims carry official source scope, valid/effective time, stale-state handling, and release posture.
- [ ] Confirm precise facility context, private property, living-person, cultural, restricted, or dependency details are not exposed in registry files, local indexes, public summaries, vector indexes, map labels, or generated responses.
- [ ] Confirm validation, geocoding, normalization, redaction, and policy receipts exist before catalog, graph projection, or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, rights-change, sensitivity-change, and rollback paths exist for mutable, time-bound, rights-bound, sensitivity-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/settlements-infrastructure/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/settlements-infrastructure/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The child `sources/` README marks the domain-first path as confirmed but final topology NEEDS VERIFICATION against subtype-first source-registry patterns. | CONFIRMED by GitHub contents API during this edit |
| Settlements / Infrastructure canonical-path docs confirm the hyphenated `settlements-infrastructure` slug and record path-shape variance with singular `settlement` and infrastructure policy projections. | CONFIRMED by GitHub contents API in this sequence |
| Settlements / Infrastructure domain README says source-descriptor registry entries belong under `data/registry/sources/` or `data/registry/settlements-infrastructure/` as proposed homes and that lifecycle data, contracts, schemas, policy, catalog, and release have separate roots. | CONFIRMED by GitHub contents API in this sequence |
| Contract-lane README says contracts do not host schemas, policy, fixtures, tests, packages, pipelines, registries, source data, lifecycle data, release decisions, or public artifacts. | CONFIRMED by GitHub contents API in this sequence |
| Pipeline README says pipeline logic does not own object meaning, schemas, policy, source descriptors, legal status, operational status, lifecycle storage, catalog truth, or release approval. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Settlements / Infrastructure registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Settlements / Infrastructure registry records. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this registry lane. | UNKNOWN |
| This README grants public access to Settlements / Infrastructure registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Settlements / Infrastructure registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> rights/sensitivity/stale-state gate -> lifecycle payload -> validation/geocoding/redaction receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Settlements / Infrastructure truth
```
