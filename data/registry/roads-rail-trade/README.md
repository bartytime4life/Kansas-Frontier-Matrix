<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/roads-rail-trade/readme
name: Roads Rail Trade Registry README
path: data/registry/roads-rail-trade/README.md
type: data-registry-roads-rail-trade-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <roads-rail-trade-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
  - <transport-network-steward>
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
registry_scope: roads-rail-trade-domain-first-registry-parent
domain: roads-rail-trade
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-source-registry-topology-needs-verification; domain-specific-source-registry-doc-not-found-in-this-sequence
sensitivity_posture: registry-internal; no-public-path; not-navigation-authority; not-current-operational-status; not-legal-access-advice; not-railroad-operating-instructions; source-role-preserving; rights-aware; access-and-restriction-context-fail-closed; infrastructure-and-sensitive-route-context-reviewed; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/roads-rail-trade/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - ../rights/README.md
  - ../layers/README.md
  - sources/README.md
  - ../../raw/roads-rail-trade/
  - ../../work/roads-rail-trade/
  - ../../quarantine/roads-rail-trade/
  - ../../processed/roads-rail-trade/
  - ../../catalog/domain/roads-rail-trade/
  - ../../published/layers/roads-rail-trade/
  - ../../receipts/roads-rail-trade/
  - ../../proofs/roads-rail-trade/
  - ../../../packages/domains/roads-rail-trade/network/README.md
  - ../../../packages/domains/roads-rail-trade/identity/README.md
  - ../../../packages/domains/roads-rail-trade/graph_projection/README.md
  - ../../../packages/domains/roads-rail-trade/frontier_routes/README.md
  - ../../../packages/domains/roads-rail-trade/generalization/README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/ARCHITECTURE.md
  - ../../../docs/domains/roads-rail-trade/PROMOTION.md
  - ../../../contracts/domains/roads-rail-trade/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../policy/rights/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - roads-rail-trade
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - roads
  - rail
  - trade-routes
  - historic-routes
  - frontier-routes
  - transport-network
  - crossings
  - restrictions
  - access-context
  - graph-projection
  - topology
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/roads-rail-trade/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The cross-domain source registry parent uses the subtype-first source-registry pattern. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Roads/Rail/Trade registry state must not become source payload storage, navigation authority, legal access advice, operational transport instruction, proof, policy, release, or public truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads / Rail / Trade Registry

Domain-first registry parent for Roads / Rail / Trade registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-2f6f4e">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not navigation" src="https://img.shields.io/badge/boundary-not%20navigation-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Roads/Rail/Trade registry boundary](#roadsrailtrade-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/roads-rail-trade/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, current navigation guidance, legal access advice, operational transport instruction, or generated-answer authority.

---

## Scope

`data/registry/roads-rail-trade/` is a domain-first routing lane for Roads / Rail / Trade registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for Roads / Rail / Trade sources.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Roads / Rail / Trade registry lane may point to or summarize governance state for:

- source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, terms, sensitivity, cadence, source-head, activation, intake, correction, supersession, stale-state, withdrawal, and freshness state;
- road, rail, trail, ferry, bridge, crossing, route, corridor, restriction, access, operator, ownership, facility, and graph-projection contexts;
- topology checks, identity refs, graph projection refs, generalization refs, and public-safe geometry refs;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, transport network datasets, graph databases, route-release manifests, proof packs, catalog records, published artifacts, operational instructions, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/roads-rail-trade/
```

This is a **domain-first** registry path. Current source-registry evidence also supports the subtype-first source registry pattern:

```text
data/registry/sources/<domain>/
```

During this sequence, no domain-specific Roads / Rail / Trade `SOURCE_REGISTRY.md` or `DATA_LIFECYCLE.md` equivalent was found through repository search. Package READMEs for Roads / Rail / Trade network, identity, and graph projection reference this registry lane as governance data, but they mark implementation depth as `NEEDS VERIFICATION` and explicitly keep source registry, lifecycle data, proof, receipts, policy, release, API, and UI separate.

Therefore, `data/registry/roads-rail-trade/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Roads / Rail / Trade domain-first registry parent | `data/registry/roads-rail-trade/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed child registry lane | `data/registry/roads-rail-trade/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical source lane | `data/registry/sources/roads-rail-trade/` | Needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, routes, segments, operators, crossings, vocabularies, measures, classes, and domain lanes. |
| Rights registry records | `data/registry/rights/` | Rights review state and rights-readiness pointers. |
| Layer registry records | `data/registry/layers/` | Layer identity and release-readiness pointers. |
| Roads / Rail / Trade source payloads | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, `data/quarantine/roads-rail-trade/`, `data/processed/roads-rail-trade/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Network helper code | `packages/domains/roads-rail-trade/network/` | Implementation helpers only; not registry, data, proof, policy, release, or public authority. |
| Identity helper code | `packages/domains/roads-rail-trade/identity/` | Deterministic IDs and digests only; not proof, source authority, release, or public route truth. |
| Graph projection helper code | `packages/domains/roads-rail-trade/graph_projection/` | Derived graph candidate support only; not source truth, release decision, proof, or public routing authority. |
| Semantic meaning | `contracts/domains/roads-rail-trade/` or accepted equivalent | Object-family meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/roads-rail-trade/`, or ADR-selected schema lane | Schema enforcement; exact domain schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/roads-rail-trade/`, `policy/rights/`, and accepted sensitivity/access policy lanes | Access, rights, stale-state, restrictions, sensitivity, and release rules. |
| Validation/topology/generalization receipts | `data/receipts/roads-rail-trade/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/roads-rail-trade/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/roads-rail-trade/`, `data/triplets/`, and accepted graph/catalog lanes | Catalog/discovery carriers and derived relationship projections after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Roads / Rail / Trade source descriptor and source-admission registry lane. | Not source payload storage, route/current-status/access/navigation truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, or public output. |

---

## Roads/Rail/Trade registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/roads-rail-trade/...` and `data/registry/sources/roads-rail-trade/`. |
| Registry is not operational authority | Registry state does not make KFM a navigation, dispatch, road-condition, railroad-operating, legal-access, or emergency-routing authority. |
| Source role is preserved | Registry state must not upgrade observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, or restricted source roles. |
| Current status requires current-source support | Closures, restrictions, access status, ownership/operator state, route status, and active infrastructure conditions must carry source time, valid/effective time, retrieval time, stale-state handling, and official authority limits. |
| Historic routes carry uncertainty | Trails, frontier roads, military roads, postal routes, stage routes, trade corridors, and reconstructed paths must preserve source vintage, method, confidence, and geometry uncertainty. |
| Geometry is not legal access | Road, rail, parcel, PLSS, bridge, ferry, crossing, route, and corridor geometry does not prove legal access, safety, current passability, ownership, or operating status by itself. |
| Graph edges are derived | Graph projection outputs are analytic candidates under stated evidence and policy conditions; they are not source truth or public routing authority. |
| Sensitive infrastructure and access context fail closed | Sensitive facilities, restricted access, private roads, safety-relevant details, and infrastructure-sensitive context require policy review before exposure. |
| Registry is not validation | Validation receipts, topology receipts, run receipts, and generalization receipts remain separate process-memory objects. |
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
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, rights registry records, layer registry records, contracts, schemas, policy refs, lifecycle payloads, validation/topology/generalization receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw transportation payloads, road centerlines, rail datasets, route inventories, closure feeds, GTFS-like feeds, WZDx-like feeds, TIGER/transport extracts, HPMS-like records, rail crossing files, historic map scans, survey plats, geocoded route tables, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, `data/quarantine/roads-rail-trade/`, or `data/processed/roads-rail-trade/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| Network helper code, identity helper code, or graph-projection helper code | `packages/domains/roads-rail-trade/` |
| Canonical source descriptor records if a subtype-first lane is accepted as canonical | `data/registry/sources/roads-rail-trade/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Rights registry records | `data/registry/rights/` after accepted rights-registry topology |
| Layer registry records | `data/registry/layers/` after accepted layer-registry topology |
| Semantic object contracts | `contracts/domains/roads-rail-trade/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/roads-rail-trade/` |
| Policy rules, stale-state rules, sensitivity rules, rights rules, access-control logic, graph-publication rules, or release rules | `policy/` |
| Validation receipts, topology receipts, projection receipts, generalization receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Current navigation, dispatch, emergency routing, legal access advice, railroad operating instructions, or safety instructions | out of scope for KFM public surfaces; use official operational systems |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/roads-rail-trade/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/roads-rail-trade/       # possible canonical source descriptors
data/registry/roads-rail-trade/README.md      # compatibility pointer / migration note only
```

Do not maintain divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/roads-rail-trade/...` or `data/registry/sources/roads-rail-trade/` is canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, jurisdiction, retrieval time, valid/effective time, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, current operational status, or public-safe posture.
- [ ] Confirm road, rail, crossing, bridge, ferry, route, corridor, restriction, access, ownership/operator, and current-status contexts are not collapsed.
- [ ] Confirm historic-route uncertainty, method lineage, source vintage, and geometry uncertainty remain explicit.
- [ ] Confirm current-status, closure, restriction, access, or operational claims carry official source scope, valid/effective time, stale-state handling, and release posture.
- [ ] Confirm sensitive infrastructure, private access, restricted facility, or safety-relevant details are not exposed in registry files, local indexes, public summaries, vector indexes, map labels, or generated responses.
- [ ] Confirm validation/topology receipts exist before catalog, graph projection, or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable, time-bound, rights-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/roads-rail-trade/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/roads-rail-trade/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against the subtype-first source-registry pattern. | CONFIRMED by GitHub contents API during this edit |
| Cross-domain `data/registry/sources/README.md` says source registry records are admission and authority-control records, not raw data, schemas, policy decisions, receipts, proofs, releases, or bibliographic prose. | CONFIRMED by GitHub contents API in this sequence |
| Roads/Rail/Trade network package README states network helpers do not publish data, activate sources, decide policy, approve routing claims, replace EvidenceBundle support, or turn derived graph edges into source truth. | CONFIRMED by GitHub contents API in this sequence |
| Roads/Rail/Trade identity package README states deterministic IDs are not proof that a route, road, rail line, crossing, restriction, or corridor is true, current, legally accessible, public-safe, complete, or reviewed. | CONFIRMED by GitHub contents API in this sequence |
| Roads/Rail/Trade graph projection README states graph projection is a derived analytic carrier, not source truth, release decision, proof, or public-routing authority. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Roads / Rail / Trade registry payloads exist under this parent lane. | UNKNOWN |
| A domain-specific Roads / Rail / Trade source-registry doctrine file was found during this sequence. | UNKNOWN / NOT FOUND |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Roads / Rail / Trade registry records. | UNKNOWN |
| This README grants public access to Roads / Rail / Trade registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Roads / Rail / Trade registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> rights/sensitivity/stale-state gate -> lifecycle payload -> validation/topology/generalization receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Roads / Rail / Trade truth
```
