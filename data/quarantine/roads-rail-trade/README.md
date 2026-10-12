<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/quarantine/roads-rail-trade/readme
name: Roads Rail Trade Quarantine README
path: data/quarantine/roads-rail-trade/README.md
type: data-quarantine-index-readme
version: v0.1.0
status: draft
owners:
  - <roads-rail-trade-domain-steward>
  - <network-topology-steward>
  - <data-steward>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: quarantine
responsibility_root: data/
domain: roads-rail-trade
artifact_family: held-roads-rail-trade-material
sensitivity_posture: fail-closed; no-public-path; source-role-preservation-required; critical-transport-review-required; cultural-corridor-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../processed/roads-rail-trade/README.md
  - ../../catalog/domain/roads-rail-trade/README.md
  - ../../published/layers/roads-rail-trade/README.md
  - ../../proofs/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/PIPELINE.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../docs/domains/roads-rail-trade/ARCHITECTURE.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - quarantine
  - roads-rail-trade
  - roads
  - rail
  - trade-routes
  - source-role
  - route-identity
  - network-topology
  - cultural-corridors
  - critical-transport
  - evidence-first
notes:
  - "This README replaces the greenfield stub and documents the parent Roads/Rail/Trade quarantine lane."
  - "No child quarantine README lanes were confirmed during this edit; proposed classes are routing guidance only."
  - "Roads/Rail/Trade quarantine is a hold area, not a staging shortcut to processed, catalog, triplet, published, reports, layers, PMTiles, stories, graph/vector indexes, generated answers, or public UI."
  - "Source-role anti-collapse is mandatory: observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles are not interchangeable."
  - "Actual held payload presence, policy automation, validator wiring, CI enforcement, and review completion remain UNKNOWN unless verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads/Rail/Trade Quarantine

Parent hold lane for Roads/Rail/Trade material that is not safe or sufficiently governed for normal processing, cataloging, publication, reporting, map rendering, story playback, graph/vector indexing, or generated-answer use.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: quarantine" src="https://img.shields.io/badge/lifecycle-quarantine-critical">
  <img alt="Domain: roads rail trade" src="https://img.shields.io/badge/domain-roads--rail--trade-555">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail--closed-d1242f">
  <img alt="Access: no public path" src="https://img.shields.io/badge/access-no%20public%20path-b83232">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Proposed quarantine classes](#proposed-quarantine-classes) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/quarantine/roads-rail-trade/` is a no-public-path hold lane. Material here is not public, not processed truth, not catalog truth, not proof, not release authority, not policy authority, not source registry authority, not road-status authority, not rail-status authority, not route truth, not facility-condition truth, not emergency-routing guidance, and not generated-answer authority. Nothing in this subtree may be consumed by public clients or normal UI surfaces until a governed exit transition leaves inspectable evidence.

---

## Scope

This directory holds Roads/Rail/Trade material when source role, rights, route identity, segment identity, network topology, temporal state, geometry precision, critical-transport sensitivity, cultural-corridor sensitivity, cross-lane evidence, validation, review record, policy decision, receipt closure, correction path, or rollback target is unresolved.

Roads/Rail/Trade owns road and rail evidence, corridor and route membership, network topology, crossings, bridges, ferries, transport facilities, restriction/status events, operator assignments, historic route claims, and trade-route corridors. It cites but does not own Settlements/Infrastructure facility truth, Hydrology water evidence, Hazards event truth, Archaeology/Cultural Heritage sensitive-route truth, or People/Land truth.

This parent lane does not make held content authoritative. It routes quarantine material so stewards can review, deny, restrict, return to work, or promote only through governed lifecycle transitions.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/quarantine/roads-rail-trade/` |
| Responsibility root | `data/` |
| Lifecycle phase | `quarantine/` |
| Domain lane | `roads-rail-trade` |
| Artifact role | Parent hold lane for Roads/Rail/Trade quarantine material and quarantine-local review sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Exit posture | Only by explicit policy decision, source-role/evidence/rights/sensitivity/identity/topology closure, required receipt closure, corrected lifecycle placement, and release-state closure |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Catalog authority | `data/catalog/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `DENY`, `RESTRICT`, or `ABSTAIN` when source role, rights, evidence, sensitivity, identity, topology, geometry, temporal role, review, correction, or rollback support is insufficient |

---

## Confirmed child lanes

No `data/quarantine/roads-rail-trade/` child-lane README paths were confirmed during this edit. This parent index is confirmed as authored, but child routing remains proposed until a child README path is created and verified.

| Child lane | Status | Notes |
|---|---|---|
| `<none confirmed>` | **UNKNOWN** | Do not infer payloads, validators, source descriptors, release gates, or CI coverage from this parent README. |

---

## Proposed quarantine classes

The Roads/Rail/Trade pipeline and object-family doctrine name or imply the hold classes below. They are routing guidance, not proof that child README paths or payloads exist.

| Class | Status | Typical handling |
|---|---|---|
| Source role collapse | **PROPOSED / NEEDS VERIFICATION** | Hold administrative-as-observed, candidate-as-verified, aggregate-as-place-truth, or synthetic-as-observed claims. |
| Route identity unresolved | **PROPOSED / NEEDS VERIFICATION** | Hold CorridorRoute, RouteMembership, Historic RouteClaim, and TradeRouteCorridor candidates until source role, temporal scope, and evidence are explicit. |
| Segment/topology defect | **PROPOSED / NEEDS VERIFICATION** | Hold road/rail segment, node, crossing, bridge, ferry, route-membership, or graph-topology defects until corrected. |
| Facility condition sensitive | **PROPOSED / NEEDS VERIFICATION** | Hold critical-transport-facility detail, condition observations, restriction events, and operator-sensitive fields until policy/review closes. |
| Cultural corridor sensitive | **PROPOSED / NEEDS VERIFICATION** | Hold Indigenous corridors, oral-history-derived paths, historic-route precision, archaeology-adjacent routes, and treaty/cultural evidence pending steward review and generalization. |
| Rights unknown | **PROPOSED / NEEDS VERIFICATION** | Hold until source terms, redistribution posture, attribution, and permitted claims are recorded. |
| Cross-lane citation unresolved | **PROPOSED / NEEDS VERIFICATION** | Re-bind or hold when Settlement, Hydrology, Hazards, Archaeology, People/Land, or other cited evidence is stale, restricted, quarantined, or missing. |
| Temporal role defect | **PROPOSED / NEEDS VERIFICATION** | Separate source, observed, valid, retrieval, release, and correction times before exit. |
| Evidence open | **PROPOSED / NEEDS VERIFICATION** | Build EvidenceBundle support or deny/abstain. |
| Slug split unresolved | **PROPOSED / NEEDS VERIFICATION** | Keep `roads-rail-trade` vs `roads-rail` segment divergence visible until ADR/migration resolution. |

> [!NOTE]
> Add child lanes only after confirming the risk class, responsibility-root fit, reviewer roles, receipt requirements, correction path, rollback target, and Directory Rules placement basis.

---

## Inputs

Accepted content is limited to held review material and quarantine-local sidecars such as source references, source-role notes, rights notes, identity notes, topology notes, geometry notes, temporal notes, sensitivity notes, policy-decision drafts, validation notes, receipt-closure checklists, digest sidecars, correction notes, rollback notes, and local README/index files.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Clean RAW source mirrors that have not triggered quarantine | `data/raw/roads-rail-trade/` or source-specific intake |
| Ordinary WORK material that is safe to process | `data/work/roads-rail-trade/` |
| Validated processed Roads/Rail/Trade objects | `data/processed/roads-rail-trade/` only after quarantine resolution |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Final validation, redaction, aggregation, source-role-review, AI, or release receipts | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, or signatures | `release/` |
| Source descriptors, activation records, source registries, or registry truth | `data/registry/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Settlements/Infrastructure, Hydrology, Hazards, Archaeology/Cultural Heritage, People/Land, Agriculture, Geology, Habitat, Fauna, Flora, or Soil canonical truth | Owning domain lane, not Roads/Rail/Trade quarantine |
| Contracts, schemas, validators, policy rules, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `policy/`, `apps/`, or UI roots |

---

## Directory map

```text
data/quarantine/roads-rail-trade/
├── README.md
├── <future-risk-sublane>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain quarantine-local. It is not a public index, catalog record, release manifest, registry, graph edge source, layer/story/report pointer, search index, vector index, map source, route authority, road/rail-status authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay held | Any unresolved source-role, rights, sensitivity, identity, topology, geometry, temporal, cross-lane evidence, validation, review, policy, correction, rollback, or release question remains. |
| Deny | PolicyDecision says `DENY`; public/UI/generated-answer surfaces abstain or deny. |
| Restrict | PolicyDecision and ReviewRecord identify allowed audience, purpose, terms, redaction/generalization state, correction path, and rollback target. |
| Return to work | Hold reason is resolved, but normal transformation, validation, attribution, temporal handling, source-role review, cross-lane evidence rebind, or EvidenceBundle work still remains. |
| Promote downstream | Only after required receipts, source descriptors, source-role closure, validation closure, evidence closure, policy/review closure, correction path, rollback target, and release support exist. |

---

## Forbidden shortcuts

```text
data/quarantine/roads-rail-trade/
→ data/processed/roads-rail-trade/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless the appropriate governed transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the material is Roads/Rail/Trade-domain material and belongs under `data/quarantine/roads-rail-trade/`.
- [ ] Confirm the hold reason is recorded using a governed reason code.
- [ ] Confirm source descriptors, source roles, authority roles, upstream citation chain, rights posture, cadence, and current terms.
- [ ] Confirm object class: road segment, rail segment, corridor route, route membership, network node, crossing, bridge, ferry, transport facility, restriction event, status event, operator assignment, historic route claim, or trade-route corridor.
- [ ] Confirm source role is preserved and not upgraded by promotion.
- [ ] Confirm identity is not collapsed by geometry similarity alone.
- [ ] Confirm time axes are separated where material: source, observed, valid, retrieval, release, and correction time.
- [ ] Confirm critical-transport, cultural-corridor, historic-route, archaeology-adjacent, operator, condition, restriction, and emergency-adjacent joins follow policy.
- [ ] Confirm required receipts are present or explicitly marked missing.
- [ ] Confirm PolicyDecision, ValidationReport, ReviewRecord where required, correction path, rollback target, and release-state handling before any exit.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses quarantined material.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/quarantine/roads-rail-trade/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No `data/quarantine/roads-rail-trade/` child-lane README path was confirmed during this edit. | **CONFIRMED by GitHub search/fetch during this edit** |
| Roads/Rail/Trade pipeline doctrine says there is no published edge from WORK or QUARANTINE. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade doctrine says source role is fixed at admission, preserved through promotion, and never upgraded by promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade object-family doctrine says geometry similarity must never collapse identity. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade doctrine says sensitive joins fail closed and critical/cultural corridors require review/generalization where needed. | **CONFIRMED by GitHub contents API during this edit** |
| `data/processed/roads-rail-trade/README.md` exists as the downstream processed-stage parent lane. | **CONFIRMED by GitHub contents API during this edit** |
| `data/published/layers/roads-rail-trade/README.md` exists as the released public-safe layer parent lane. | **CONFIRMED by GitHub contents API during this edit** |
| Actual quarantined payloads exist under this subtree. | **UNKNOWN** |
| Policy automation, validators, and CI checks enforce every listed Roads/Rail/Trade quarantine class. | **NEEDS VERIFICATION** |
| This README is proof, release, catalog, registry, policy, road-status authority, rail-status authority, route truth, facility-condition truth, emergency-routing guidance, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../processed/roads-rail-trade/README.md`](../../processed/roads-rail-trade/README.md)
- [`../../catalog/domain/roads-rail-trade/README.md`](../../catalog/domain/roads-rail-trade/README.md)
- [`../../published/layers/roads-rail-trade/README.md`](../../published/layers/roads-rail-trade/README.md)
- [`../../proofs/roads-rail-trade/README.md`](../../proofs/roads-rail-trade/README.md)
- [`../../../docs/domains/roads-rail-trade/PIPELINE.md`](../../../docs/domains/roads-rail-trade/PIPELINE.md)
- [`../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md`](../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md)
- [`../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md`](../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md)
- [`../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md`](../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md)
- [`../../../docs/domains/roads-rail-trade/ARCHITECTURE.md`](../../../docs/domains/roads-rail-trade/ARCHITECTURE.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Roads/Rail/Trade quarantine hold index only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, registry authority, policy authority, road-status authority, rail-status authority, route truth, facility-condition truth, emergency-routing guidance, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
