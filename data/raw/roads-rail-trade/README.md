<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/roads-rail-trade/readme
name: Roads Rail Trade Raw README
path: data/raw/roads-rail-trade/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <roads-rail-trade-domain-steward>
  - <roads-rail-trade-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: roads-rail-trade
artifact_family: immutable-roads-rail-trade-source-capture-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; route-status-not-assumed; legal-status-not-inferred; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../quarantine/roads-rail-trade/README.md
  - ../../processed/roads-rail-trade/README.md
  - ../../catalog/domain/roads-rail-trade/README.md
  - ../../published/layers/roads-rail-trade/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../../docs/domains/roads-rail-trade/SOURCE_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/UBIQUITOUS_LANGUAGE.md
  - ../../../docs/domains/roads-rail-trade/API_CONTRACTS.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - roads-rail-trade
  - roads
  - rail
  - trade-routes
  - transport-network
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/roads-rail-trade/README.md`."
  - "No child RAW README lanes under `data/raw/roads-rail-trade/` were confirmed during this edit."
  - "The Roads/Rail/Trade source registry lists source families such as TIGER/Line roads, FHWA HPMS, FHWA NHFN, WZDx, KDOT/KanPlan/KanDrive/Kansas GIS, county/state bridge and restriction data, GNIS, and OSM, but admission, source role, rights, sensitivity, and freshness must be resolved per source."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads / Rail / Trade RAW

Parent RAW lifecycle index for immutable Roads/Rail/Trade source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Source-family posture](#source-family-posture) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/roads-rail-trade/` is a no-public-path RAW lifecycle lane. It is not processed Roads/Rail/Trade truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, graph authority, route-status authority, legal-designation authority, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and RAW-local sidecars for the Roads/Rail/Trade domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, vintages, source times, retrieval times, rights notes, citations, geometry/support metadata, source-head metadata, hashes, review notes, and caveats must travel downstream.

RAW does not decide whether a road, rail segment, bridge, route, corridor, operator assignment, closure, restriction, or trade-route interpretation is true, current, legal, public-safe, or release-ready. It also does not authorize routing, public maps, graph edges, generated summaries, or legal-status claims.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/roads-rail-trade/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `roads-rail-trade` |
| Artifact role | Parent RAW domain index for source captures and RAW-local sidecars |
| Confirmed child README lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted connector/source-admission output only |
| Downstream | `data/work/roads-rail-trade/` or `data/quarantine/roads-rail-trade/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, citation, geometry/support, freshness, sensitivity, validation, correction, rollback, or release support is insufficient |

---

## Source-family posture

The Roads/Rail/Trade source registry lists families that may feed the lane after governed admission. This parent README does not prove that any payloads or child source-family folders exist.

| Source family | Typical RAW posture | Boundary |
|---|---|---|
| Census TIGER/Line roads | Administrative / geometry-context capture by vintage. | Geometry context is not route condition or legal designation by itself. |
| FHWA HPMS | Administrative network extent and regulatory/functional-class context where applicable. | HPMS rows must not be treated as observed event timelines. |
| FHWA National Highway Freight Network | Regulatory designation / administrative roster capture. | Designation context is not observed use or freight volume. |
| WZDx feeds | Observed work-zone event capture when admitted. | Feed freshness, producer terms, and stale-state handling must travel downstream. |
| KDOT / KanPlan / KanDrive / Kansas GIS | Mixed authority, observed-status, and administrative source capture by product. | State-route designation, asset rosters, and status feeds must not collapse into one role. |
| County / state bridge and restriction data | Regulatory restriction and administrative inventory capture. | Posted restriction context is not bridge-condition truth unless supported by the owning source role. |
| GNIS names | Administrative named-feature context. | GNIS is not legal-status authority for route designations. |
| OpenStreetMap | Candidate / context capture only. | OSM must not be cited as legal-status authority without governed corroboration and release gates. |
| Historic and trade-corridor sources | Candidate, observed, administrative, or synthetic by source and review state. | Historic alignments, Indigenous corridors, and interpretive routes require rights, sensitivity, provenance, and generalization review. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Administrative is not observed | TIGER/Line geometry, HPMS rows, facility rosters, and inventories must not become observed event timelines. |
| Regulatory is not observed | Route designations, freight corridors, posted restrictions, and operating-right records remain regulatory/admin context until downstream proof closes. |
| Candidate remains candidate | OSM ways, unresolved historic alignments, and unreviewed connector output cannot become public authority without promotion. |
| Modeled graph is not canonical truth | Routing, traversal, reconstructed alignment, and freight-flow models require model/run support and cannot replace source records. |
| Aggregate is not per-place truth | Corridor totals, county totals, annual summaries, and other rollups need aggregation scope before join or claim use. |
| Public use requires governed release | Public layers, PMTiles, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, product vintage, endpoint identity, geometry/support metadata, citation, attribution, rights posture, freshness posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, event counts, topology counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, graph authority, route-status authority, legal-status authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Roads/Rail/Trade domain doctrine | `docs/domains/roads-rail-trade/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/roads-rail-trade/` |
| Connector code or connector decisions | `connectors/` |
| Pipeline code or pipeline decisions | `pipelines/domains/roads-rail-trade/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, route-status, historic-corridor, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/roads-rail-trade/` |
| Normalized working material | `data/work/roads-rail-trade/` |
| Validated Roads/Rail/Trade objects | `data/processed/roads-rail-trade/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Legal route status, observed facility condition, live operational status, routing authority, public artifact authority, or generated-answer authority | Owning governed downstream/proof/policy/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/roads-rail-trade/
├── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

Potential future source-family folders must be created only after admission/path review. Examples may include `tiger-line-roads/`, `fhwa-hpms/`, `fhwa-nhfn/`, `wzdx/`, `kdot/`, `bridge-restrictions/`, `gnis/`, `osm/`, and `historic-routes/`, but none are confirmed by this README.

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, endpoint, product/vintage identity, citation, geometry/support, schema, freshness, sensitivity, or activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization/model/freshness receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/roads-rail-trade/
→ data/processed/roads-rail-trade/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Roads/Rail/Trade lane and a documented source-family subfolder.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, citation, endpoint identity, freshness posture, and hash posture.
- [ ] Confirm administrative, regulatory, observed, modeled, aggregate, candidate, and synthetic source roles are not collapsed.
- [ ] Confirm TIGER/Line, HPMS, rosters, and inventories are not cited as observed event timelines by themselves.
- [ ] Confirm OSM and GNIS are not cited as legal route-status authority without governed corroboration and release gates.
- [ ] Confirm historic-route, Indigenous-corridor, oral-history, and critical-facility material receives sensitivity and public-generalization review where required.
- [ ] Confirm modeled graph, routing, freight-flow, and reconstructed alignment outputs preserve model/run lineage before claim use.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW Roads/Rail/Trade material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/roads-rail-trade/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child RAW README lanes under `data/raw/roads-rail-trade/` were confirmed during this edit. | **UNKNOWN / not confirmed** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Roads/Rail/Trade source-registry doctrine lists source families including TIGER/Line roads, FHWA HPMS, FHWA NHFN, WZDx, KDOT/KanPlan/KanDrive/Kansas GIS, bridge/restriction data, GNIS, OSM, and historic/trade-corridor evidence. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade source-role doctrine says source role is first-class and fails closed when roles are conflated. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Roads/Rail/Trade RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, graph authority, route-status authority, legal-designation authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/roads-rail-trade/README.md`](../../quarantine/roads-rail-trade/README.md)
- [`../../processed/roads-rail-trade/README.md`](../../processed/roads-rail-trade/README.md)
- [`../../catalog/domain/roads-rail-trade/README.md`](../../catalog/domain/roads-rail-trade/README.md)
- [`../../published/layers/roads-rail-trade/README.md`](../../published/layers/roads-rail-trade/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md)
- [`../../../docs/domains/roads-rail-trade/SOURCE_FAMILIES.md`](../../../docs/domains/roads-rail-trade/SOURCE_FAMILIES.md)
- [`../../../docs/domains/roads-rail-trade/SOURCES.md`](../../../docs/domains/roads-rail-trade/SOURCES.md)
- [`../../../docs/domains/roads-rail-trade/UBIQUITOUS_LANGUAGE.md`](../../../docs/domains/roads-rail-trade/UBIQUITOUS_LANGUAGE.md)
- [`../../../docs/domains/roads-rail-trade/API_CONTRACTS.md`](../../../docs/domains/roads-rail-trade/API_CONTRACTS.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Roads/Rail/Trade RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, legal-status authority, route-status authority, graph authority, public artifact authority, UI authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
