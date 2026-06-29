<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/roads-rail-trade/sources/readme
name: Roads Rail Trade Source Registry README
path: data/registry/roads-rail-trade/sources/README.md
type: data-registry-roads-rail-trade-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <roads-rail-trade-domain-steward>
  - <transport-network-steward>
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
registry_scope: roads-rail-trade-source-descriptor-records
domain: roads-rail-trade
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-domain; domain-specific-source-registry-doc-not-found-in-this-edit; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; not-navigation-authority; not-current-operational-status; source-role-preserving; rights-aware; access-and-restriction-context-fail-closed; infrastructure-and-sensitive-route-context-reviewed; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/roads-rail-trade/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/roads-rail-trade/
  - ../../../work/roads-rail-trade/
  - ../../../quarantine/roads-rail-trade/
  - ../../../processed/roads-rail-trade/
  - ../../../catalog/domain/roads-rail-trade/
  - ../../../published/layers/roads-rail-trade/
  - ../../../receipts/roads-rail-trade/
  - ../../../proofs/roads-rail-trade/
  - ../../../../packages/domains/roads-rail-trade/network/README.md
  - ../../../../packages/domains/roads-rail-trade/identity/README.md
  - ../../../../packages/domains/roads-rail-trade/graph_projection/README.md
  - ../../../../packages/domains/roads-rail-trade/frontier_routes/README.md
  - ../../../../packages/domains/roads-rail-trade/generalization/README.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../docs/domains/roads-rail-trade/ARCHITECTURE.md
  - ../../../../docs/domains/roads-rail-trade/PROMOTION.md
  - ../../../../contracts/domains/roads-rail-trade/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - roads-rail-trade
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
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/roads-rail-trade/sources/README.md`."
  - "Roads/Rail/Trade source registry records are admission and authority-control records. They do not store source payloads, prove route/current-status/access/navigation claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "No domain-specific Roads/Rail/Trade source-registry doctrine was found during this edit; package READMEs confirm adjacent implementation boundaries and keep source registry, policy, proofs, receipts, release, and public interfaces separate."
  - "KFM transport records are evidence context and governed publication material, not emergency alerts, navigation instructions, legal access advice, current road-condition authority, or railroad-operating instructions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads / Rail / Trade Source Registry

Domain-first registry lane for Roads / Rail / Trade source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-2f6f4e">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not navigation" src="https://img.shields.io/badge/boundary-not%20navigation-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Roads/Rail/Trade source boundary](#roadsrailtrade-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/roads-rail-trade/sources/` is a source-registry lane for Roads / Rail / Trade admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, current navigation guidance, legal access advice, operational transport instruction, or generated-answer authority.

---

## Scope

This directory documents and may hold Roads / Rail / Trade source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Roads / Rail / Trade lane.

Roads / Rail / Trade source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, terms, endpoint, and access posture;
- sensitivity posture for transportation, infrastructure, private access, historic-route, facility, crossing, and restriction context;
- cadence, source head, retrieval window, source vintage, source scale, publication date, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required quarantine, validation, topology checks, generalization, proof, catalog, release, correction, stale-state, withdrawal, and rollback requirements.

They do **not** prove that a road, rail line, crossing, bridge, route, corridor, restriction, access condition, or facility is true, current, complete, safe, legally accessible, operational, or public-safe. A source descriptor can authorize or deny admission conditions, but every consequential claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/roads-rail-trade/sources/
```

This is a domain-first registry path. The cross-domain source registry parent also supports a subtype-first source registry pattern:

```text
data/registry/sources/<domain>/
```

During this edit, no domain-specific Roads / Rail / Trade `SOURCE_REGISTRY.md` or `DATA_LIFECYCLE.md` equivalent was found through repository search. Package READMEs for network, identity, and graph projection do reference `data/registry/roads-rail-trade/` or source-registry homes as governance data, but they mark implementation depth as `NEEDS VERIFICATION`.

Therefore, this requested path is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. If `data/registry/sources/roads-rail-trade/` is later accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Roads / Rail / Trade source descriptor/admission records | `data/registry/roads-rail-trade/sources/` and/or reconciled `data/registry/sources/roads-rail-trade/` | Source identity, role, rights, terms, cadence, activation, authority limits, and caveats. |
| Domain-first registry parent | `data/registry/roads-rail-trade/` | Parent currently exists as a stub; topology remains NEEDS VERIFICATION. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Roads / Rail / Trade source payloads | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, `data/quarantine/roads-rail-trade/`, `data/processed/roads-rail-trade/` | Actual data belongs in lifecycle lanes, not registry records. |
| Network helper code | `packages/domains/roads-rail-trade/network/` | Implementation helpers only; not source registry, data, policy, proof, release, or public authority. |
| Identity helper code | `packages/domains/roads-rail-trade/identity/` | Deterministic IDs and digests only; not proof, source authority, release, or public route truth. |
| Graph projection helper code | `packages/domains/roads-rail-trade/graph_projection/` | Derived graph candidate support only; not source truth, release decision, proof, or public routing authority. |
| Semantic meaning | `contracts/domains/roads-rail-trade/` or accepted equivalent | Object meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/roads-rail-trade/`, or ADR-selected schema lane | Schema enforcement; exact domain schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/roads-rail-trade/`, `policy/rights/`, and accepted sensitivity/access policy lanes | Access, rights, stale-state, restrictions, sensitivity, and release rules. |
| Validation/topology/generalization receipts | `data/receipts/roads-rail-trade/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/roads-rail-trade/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/roads-rail-trade/`, `data/triplets/`, and accepted graph/catalog lanes | Catalog/discovery carriers and derived relationship projections after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Roads/Rail/Trade source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Transport source is not operational authority | A source record does not make KFM a navigation, dispatch, road-condition, railroad-operating, legal-access, or emergency-routing authority. |
| Source role is fixed at admission | Observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, or restricted roles must not be upgraded by processing, topology, graph projection, cataloging, rendering, or generated explanation. |
| Current status requires current-source support | Closures, restrictions, access status, ownership/operator state, route status, and active infrastructure conditions must carry source time, valid/effective time, retrieval time, stale-state handling, and official authority limits. |
| Historic routes carry uncertainty | Trails, frontier roads, military roads, postal routes, stage routes, trade corridors, and reconstructed paths must preserve source vintage, method, confidence, and geometry uncertainty. |
| Geometry is not legal access | Road, rail, parcel, PLSS, bridge, ferry, crossing, route, and corridor geometry does not prove legal access, safety, current passability, ownership, or operating status by itself. |
| Graph edges are derived | Graph projection outputs are analytic candidates under stated evidence and policy conditions; they are not source truth or public routing authority. |
| Rights and restrictions travel | License, attribution, redistribution, source terms, access restrictions, private-road restrictions, and sensitive infrastructure caveats must remain attached downstream. |
| Infrastructure-sensitive context fails closed | Sensitive facilities, restricted access, critical infrastructure, private access notes, and safety-relevant details require policy review before exposure. |
| Registry is not validation | Validation receipts, topology receipts, run receipts, and generalization receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Roads / Rail / Trade source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, license, attribution, redistribution, cadence, access, endpoint, terms, steward, authority-scope, and caveat metadata;
- source vintage, route-status basis, jurisdiction, operator/owner assertion scope, infrastructure context, scale/accuracy notes, retrieval refs, and stale-state notes;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation/topology receipts, generalization receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed source payloads, full network extracts, graph databases, proof packs, policy decisions, catalog records, release manifests, operational instructions, or Roads / Rail / Trade claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw transportation payloads, road centerlines, rail datasets, route inventories, closure feeds, WZDx-like feeds, GTFS-like feeds, TIGER/transport extracts, HPMS-like records, rail crossing files, historic map scans, survey plats, geocoded route tables, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, `data/quarantine/roads-rail-trade/`, or `data/processed/roads-rail-trade/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| Network helper code, identity helper code, or graph-projection helper code | `packages/domains/roads-rail-trade/` |
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

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/roads-rail-trade/sources/
├── README.md
├── road_network/
│   ├── README.md
│   └── index.local.json
├── rail_network/
│   ├── README.md
│   └── index.local.json
├── crossings_bridges_ferries/
│   ├── README.md
│   └── index.local.json
├── route_membership/
│   ├── README.md
│   └── index.local.json
├── historic_frontier_routes/
│   ├── README.md
│   └── index.local.json
├── trade_corridors/
│   ├── README.md
│   └── index.local.json
├── restrictions_access_context/
│   ├── README.md
│   └── index.local.json
├── operators_ownership_context/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/roads-rail-trade/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Roads / Rail / Trade source registry record should be structured enough for audit, admission, validation, stale-state handling, correction, and rollback.

```json
{
  "id": "kfm-source:roads-rail-trade:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "roads-rail-trade",
  "source_family": "road_network | rail_network | crossings_bridges_ferries | route_membership | historic_frontier_routes | trade_corridors | restrictions_access_context | operators_ownership_context | other",
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
  "topology_receipt_refs": [],
  "generalization_receipt_refs": [],
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

- [ ] Confirm whether `data/registry/roads-rail-trade/sources/` or `data/registry/sources/roads-rail-trade/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, rights record, layer record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, jurisdiction, retrieval time, valid/effective time, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, topology validation, graph projection, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm road, rail, crossing, bridge, ferry, route, corridor, restriction, access, ownership/operator, and current-status contexts are not collapsed.
- [ ] Confirm historic-route uncertainty, method lineage, source vintage, and geometry uncertainty remain explicit.
- [ ] Confirm current-status, closure, restriction, access, or operational claims carry official source scope, valid/effective time, stale-state handling, and release posture.
- [ ] Confirm sensitive infrastructure, private access, restricted facility, or safety-relevant details are not exposed in registry files, local indexes, public summaries, vector indexes, map labels, or generated responses.
- [ ] Confirm validation/topology receipts exist before catalog, graph projection, or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable, time-bound, rights-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/roads-rail-trade/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/roads-rail-trade/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Cross-domain `data/registry/sources/README.md` says source registry records are admission and authority-control records, not raw data, schemas, policy decisions, receipts, proofs, releases, or bibliographic prose. | CONFIRMED by GitHub contents API during this edit |
| Roads/Rail/Trade network package README states network helpers do not publish data, activate sources, decide policy, approve routing claims, replace EvidenceBundle support, or turn derived graph edges into source truth. | CONFIRMED by GitHub contents API during this edit |
| Roads/Rail/Trade identity package README states deterministic IDs are not proof that a route, road, rail line, crossing, restriction, or corridor is true, current, legally accessible, public-safe, complete, or reviewed. | CONFIRMED by GitHub contents API during this edit |
| Roads/Rail/Trade graph projection README states graph projection is derived analytic carrier, not source truth, release decision, proof, or public-routing authority. | CONFIRMED by GitHub contents API during this edit |
| Concrete Roads / Rail / Trade source descriptor payloads exist under this requested lane. | UNKNOWN |
| A domain-specific Roads / Rail / Trade source-registry doctrine file was found during this edit. | UNKNOWN / NOT FOUND |
| The final accepted topology between domain-first and subtype-first source registry lanes is resolved. | NEEDS VERIFICATION |
| A canonical Roads / Rail / Trade source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Roads / Rail / Trade source registry records. | UNKNOWN |
| This README grants public access to Roads / Rail / Trade source registry internals. | DENY |

---

## Maintainer note

Roads / Rail / Trade source registry records are useful because they make source identity, source role, rights, cadence, authority limits, stale-state, transport context, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, current operational truth, or public navigation authority. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> rights/sensitivity/stale-state gate -> RAW admission -> lifecycle processing -> validation/topology/generalization receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Roads / Rail / Trade truth
```
