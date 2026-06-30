<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/trade-routes/readme
name: Trade Routes Data Compatibility README
path: data/trade-routes/README.md
type: data-compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <directory-rules-steward>
  - <roads-rail-trade-domain-steward>
  - <historic-routes-steward>
  - <trade-routes-steward>
  - <sensitivity-reviewer>
  - <rights-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
domain: roads-rail-trade
subtopic: trade-routes
artifact_family: compatibility-marker-and-migration-guide
compatibility_class: transitional
authority_posture: compatibility-lane; not-canonical-lifecycle-lane; not-source-data; not-processed-data; not-catalog; not-proof; not-receipt; not-published; not-release-authority; not-policy-authority; not-schema-authority; not-public-api-ui-source
path_posture: existing-empty-file-replaced; data-trade-routes-path-present; directory-rules-data-lifecycle-lists-domain-segment-lanes-not-topic-lanes; roads-rail-trade-domain-docs-confirm-data-segment-roads-rail-trade; trade-routes-sublane-doc-says-documentation-only-and-does-not-create-data-trade-routes; canonical-targets-are-roads-rail-trade-data-lifecycle-lanes; migration-needed-before-new-payloads
sensitivity_posture: deny-new-payloads-by-default; historic-route-claim-not-route-truth; trade-route-corridor-not-exact-alignment; geometry-not-authority; cultural-and-indigenous-corridor-review-required; archaeology-joins-fail-closed; private-land-and-living-person-joins-fail-closed; infrastructure-and-restricted-route-detail-reviewed; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-aware
related:
  - ../README.md
  - ../raw/roads-rail-trade/
  - ../work/roads-rail-trade/
  - ../quarantine/roads-rail-trade/
  - ../processed/roads-rail-trade/README.md
  - ../catalog/domain/roads-rail-trade/README.md
  - ../registry/sources/roads-rail-trade/README.md
  - ../receipts/roads-rail-trade/README.md
  - ../proofs/roads-rail-trade/README.md
  - ../published/roads-rail-trade/README.md
  - ../published/layers/roads-rail-trade/README.md
  - ../rollback/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md
  - ../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../docs/domains/roads-rail-trade/sublanes/trade_routes.md
  - ../../docs/domains/roads-rail-trade/HISTORIC_ROUTES.md
  - ../../docs/domains/roads-rail-trade/GRAPH_PROJECTIONS.md
  - ../../docs/domains/roads-rail-trade/SENSITIVITY.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../release/README.md
  - ../../contracts/transport/
  - ../../schemas/contracts/v1/transport/
  - ../../policy/domains/roads-rail-trade/
  - ../../policy/sensitivity/transport/
tags:
  - kfm
  - data
  - compatibility
  - transitional
  - trade-routes
  - historic-routes
  - roads-rail-trade
  - transport
  - historic-route-claim
  - trade-route-corridor
  - corridor-route
  - route-membership
  - movement-story-node
  - source-role
  - public-safe-geometry
  - cultural-corridors
  - indigenous-corridors
  - archaeology-sensitive
  - rights-review
  - evidence-bundle
  - release-gated
  - no-public-path
  - not-canonical
  - not-data-payload-lane
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/trade-routes/README.md`."
  - "Directory Rules lists `data/<lifecycle-phase>/<domain>/` lanes and `data/rollback/<domain>/<release_id>/`; it does not list `data/trade-routes/` as a canonical lifecycle lane."
  - "Roads/Rail/Trade doctrine confirms `roads-rail-trade` as the data/docs/policy/test-style domain segment, with a separate unresolved `transport/` schema/contract segment split."
  - "The trade-routes sublane document says the sublane is documentation-only and does not create `data/trade-routes/` or separate schema/policy/data homes."
  - "This file therefore acts as a compatibility marker and migration guide, not a new authority root or data lake."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Trade Routes Data Compatibility Lane

Compatibility marker for the existing `data/trade-routes/` path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Compatibility: transitional" src="https://img.shields.io/badge/compatibility-transitional-orange">
  <img alt="Canonical domain: roads rail trade" src="https://img.shields.io/badge/canonical%20domain-roads--rail--trade-2b6cb0">
  <img alt="Boundary: not canonical data" src="https://img.shields.io/badge/boundary-not%20canonical%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Canonical homes](#canonical-homes) · [Allowed contents](#allowed-contents) · [Exclusions](#exclusions) · [Trade-route guardrails](#trade-route-guardrails) · [Migration plan](#migration-plan) · [Suggested marker shape](#suggested-marker-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/trade-routes/` is **not** a canonical KFM lifecycle lane. Do not use this directory as RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, release, schema, policy, source-registry, route-truth, graph-truth, map-truth, or public UI/API authority. The canonical data domain segment for trade-route and historic-corridor material is `roads-rail-trade`, placed under the proper lifecycle phase.

---

## Scope

This README exists because `data/trade-routes/README.md` is present in the repository as an empty file. The purpose of this document is to make that path inspectable and prevent it from becoming an accidental parallel authority.

`data/trade-routes/` may contain only narrow compatibility material such as:

- this README;
- migration notes that point from legacy/topic-shaped paths to canonical Roads/Rail/Trade lifecycle lanes;
- inventory indexes that identify material needing relocation, if such material is later discovered;
- redirect notes or deprecation markers;
- temporary audit outputs clearly marked as non-authoritative and not public.

This directory should **not** receive new trade-route payloads. New trade-route source, processed, catalog, proof, receipt, published, or rollback material should land under the owning responsibility root and the canonical `roads-rail-trade` domain lane.

---

## Path posture

Observed path:

```text
data/trade-routes/
```

Canonical domain lane pattern:

```text
data/<phase>/roads-rail-trade/
```

Why this path is non-canonical:

- Directory Rules define `data/` as a lifecycle root with phase-first lanes such as `raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `triplets/`, `receipts/`, `proofs/`, `published/`, `rollback/`, and `registry/`.
- Directory Rules list `data/rollback/<domain>/<release_id>/` and otherwise show lifecycle phases holding `<domain>` segments.
- The Roads/Rail/Trade domain README confirms `roads-rail-trade` as the data/docs/policy/test-style domain segment, while schema/contracts may use `transport/` pending ADR resolution.
- The Roads/Rail/Trade file-system plan says the domain should be a lane across responsibility roots, not a topic root.
- The trade-routes sublane document says the sublane is documentation-only and explicitly says it does not create a `data/trade-routes/` tree.

Therefore this README treats `data/trade-routes/` as **CONFIRMED path presence / TRANSITIONAL compatibility lane / DENY new payloads until migration or ADR**.

---

## Canonical homes

| Material type | Canonical home | Notes |
|---|---|---|
| RAW trade-route source captures | `data/raw/roads-rail-trade/` | Source-edge captures only, with retrieval metadata and checksums. |
| WORK candidates and scratch | `data/work/roads-rail-trade/` | Normalization, route matching, alignment reconstruction, and review scratch. |
| QUARANTINE material | `data/quarantine/roads-rail-trade/` | Rights, sensitivity, overprecision, source-role, or evidence problems. |
| PROCESSED trade-route candidates | `data/processed/roads-rail-trade/` | Normalized HistoricRouteClaim, TradeRouteCorridor, CorridorRoute, RouteMembership, and related candidates. |
| Catalog records | `data/catalog/domain/roads-rail-trade/` | Discovery, catalog closure, evidence/source/release references. |
| Proof support | `data/proofs/roads-rail-trade/` | EvidenceBundle/ProofPack support, source-role proof, corridor generalization proof, rollback proof. |
| Receipts | `data/receipts/roads-rail-trade/` | Run, transform, redaction, validation, review, AI, release-support, and correction receipts. |
| Source registry | `data/registry/sources/roads-rail-trade/` | SourceDescriptor and source-admission records. |
| Published non-layer artifacts | `data/published/roads-rail-trade/` | Released public-safe export bundles and sidecars. |
| Published map layers | `data/published/layers/roads-rail-trade/` | Released public-safe generalized route/corridor layers. |
| Rollback support | `data/rollback/roads-rail-trade/` | Data-plane rollback support tied to release-plane decisions. |
| Doctrine and sublane explanation | `docs/domains/roads-rail-trade/` | Human-facing domain and sublane documentation. |
| Release decisions | `release/` | ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures. |
| Contracts and schemas | `contracts/transport/`, `schemas/contracts/v1/transport/`, or ADR-resolved homes | Segment split remains unresolved; this README does not resolve it. |

---

## Allowed contents

Allowed material is intentionally narrow:

- `README.md` files that document compatibility status and migration posture;
- migration inventories, if they are clearly marked as indexes and not payloads;
- pointer files that direct maintainers to canonical `roads-rail-trade` lifecycle lanes;
- temporary audit notes that do not embed restricted source data or public claims.

Any allowed file here must say that it is not source data, not processed data, not catalog, not proof, not receipt, not release, not published artifact, not policy, not schema, and not public API/UI material.

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Historic maps, scans, source exports, source tables, source logs, partner data, or source-native geometry | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, or `data/quarantine/roads-rail-trade/` |
| Normalized HistoricRouteClaim, TradeRouteCorridor, CorridorRoute, RouteMembership, MovementStoryNode, segment membership, or graph candidates | `data/processed/roads-rail-trade/` or accepted graph/triplet lanes |
| Catalog records, STAC/DCAT/PROV, domain catalog indexes, or story-node catalog records | `data/catalog/domain/roads-rail-trade/` |
| EvidenceBundle, ProofPack, validation proof, sensitivity proof, corridor-generalization proof, or release proof | `data/proofs/roads-rail-trade/` |
| Run, transform, redaction, review, policy, AI, release-support, correction, or rollback receipts | `data/receipts/roads-rail-trade/` or `data/rollback/roads-rail-trade/` as applicable |
| SourceDescriptor, source registry records, source-family records, rights/sensitivity source posture | `data/registry/sources/roads-rail-trade/` or ADR-resolved registry home |
| Published public-safe artifacts or layers | `data/published/roads-rail-trade/` or `data/published/layers/roads-rail-trade/` |
| ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `release/` |
| Semantic contracts, schemas, policy, validators, tests, code, or pipeline specs | `contracts/`, `schemas/`, `policy/`, `tools/`, `tests/`, `packages/`, `pipelines/`, or `pipeline_specs/` |
| Exact sensitive route geometry, restricted Indigenous/cultural corridor detail, archaeology-linked route detail, private-land joins, critical-facility context, or restricted source detail | Restricted governed lanes only; public-safe derivative after policy/review/release |

---

## Trade-route guardrails

| Risk | Guardrail |
|---|---|
| Topic lane becomes authority | Keep this directory as a marker only; canonical material belongs in `roads-rail-trade` lifecycle lanes. |
| Historic route claim becomes route truth | Treat historic route geometry as evidence-bearing `Historic RouteClaim`, not a confirmed route by placement. |
| Corridor becomes exact alignment | Treat `TradeRouteCorridor` as generalized corridor context unless evidence, sensitivity review, and release support narrower geometry. |
| Geometry becomes authority | A line, polygon, tile, or graph edge is not route truth without EvidenceBundle, source-role, catalog, proof, policy, and release support. |
| Cultural corridor overexposure | Indigenous, cultural, treaty, oral-history, archaeology-adjacent, or sensitive corridor material requires steward review and public-safe generalization or denial. |
| Source-role collapse | Historic maps, oral history, administrative records, modern road data, graph projections, model outputs, and AI summaries must not collapse into one role. |
| Cross-domain truth drift | Hydrology owns water evidence; Archaeology owns site identity and exact coordinates; Settlements/Infrastructure owns facility/settlement truth; People/Land owns living-person and land claims; Hazards owns hazard-event context. |
| Public shortcut | Public clients must use governed APIs, release-resolved artifacts, catalog/proof-backed responses, and policy-safe map layers, not this directory. |
| AI surface drift | Generated summaries must not cite this compatibility lane as evidence or release authority. |
| Migration drift | Do not maintain live payloads in both `data/trade-routes/` and `data/<phase>/roads-rail-trade/`. |

---

## Migration plan

1. Inventory any non-README files under `data/trade-routes/`.
2. Classify each file by lifecycle phase: RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, RECEIPT, PROOF, PUBLISHED, ROLLBACK, REGISTRY, or RELEASE.
3. Move by responsibility root and domain lane, not by topic name.
4. Preserve checksums, source metadata, source role, rights posture, sensitivity posture, evidence refs, review refs, catalog refs, and release refs during migration.
5. Create receipts for any migration that changes location, identity, redaction, generalization, aggregation, or release surface.
6. Keep this README as a compatibility marker until a Directory Rules update, ADR, or migration note explicitly retires the path.

Rollback for this README is simple: revert this README to the previous empty blob if maintainers reject the compatibility posture. Do not delete data payloads through this file; deletion and erasure require separate governed processes.

---

## Suggested marker shape

Do not pre-create these files unless an audit finds material to track.

```text
data/trade-routes/
├── README.md
├── MIGRATION-NOTE.md                 # PROPOSED only if migration starts
├── inventory.index.json              # PROPOSED only if non-README files are found
└── redirects.json                     # PROPOSED only if canonical paths need explicit pointers
```

If any payload-like file appears here, classify it immediately and move it to the correct lifecycle lane after review.

---

## Required checks before use

- [ ] Confirm whether `data/trade-routes/` contains anything beyond this README.
- [ ] Confirm whether any ADR, migration note, or Directory Rules update explicitly authorizes this path.
- [ ] Confirm all new trade-route payloads use `data/<phase>/roads-rail-trade/` rather than `data/trade-routes/`.
- [ ] Confirm historic-route and trade-corridor claims preserve source role, uncertainty, time scope, evidence refs, sensitivity posture, and release state.
- [ ] Confirm cultural, Indigenous, archaeology-linked, private-land, critical-facility, or restricted-source material is generalized, restricted, quarantined, or denied before public exposure.
- [ ] Confirm generated AI answers, maps, graph projections, and story surfaces never cite this compatibility lane as proof or release authority.
- [ ] Confirm public clients resolve any released route/corridor material through governed API or released artifact aliases, not by reading this directory.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/trade-routes/README.md` existed as an empty file before this update. |
| Data root authority | CONFIRMED README | `data/README.md` says `data/` owns lifecycle data and excludes release decisions. |
| Directory Rules lifecycle path | CONFIRMED doctrine | Directory Rules list lifecycle phase lanes under `data/`, with domain segments under the phase. |
| Canonical domain segment | CONFIRMED docs | Roads/Rail/Trade docs use `roads-rail-trade` for data/docs/policy/test-style lanes. |
| Trade-routes sublane | CONFIRMED docs / PROPOSED convention | `docs/domains/roads-rail-trade/sublanes/trade_routes.md` defines the trade-route/historic-corridor subset but says sublane placement and terminology need verification. |
| `data/trade-routes/` as canonical data lane | DENY | Current evidence does not support this as a canonical lifecycle lane. |
| Compatibility posture | PROPOSED | This README proposes transitional compatibility marking until migration or ADR. |
| Actual payload inventory under this path | UNKNOWN | This edit only verified the README target, not a full subtree inventory. |
| Runtime validators, CI, and migration tooling | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY until proven | A compatibility README cannot publish, prove, or expose trade-route claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/trade-routes/README.md` existed as an empty file. | Did not define boundaries. |
| [`../README.md`](../README.md) | CONFIRMED README | `data/` owns lifecycle data and excludes release decisions. | Data root README is short and status `PROPOSED`. |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | Data lifecycle phase lanes; rollback domain path; promotion is governed state transition; compatibility roots are not parallel authority. | Does not specifically enumerate `data/trade-routes/`. |
| [`../../docs/domains/roads-rail-trade/README.md`](../../docs/domains/roads-rail-trade/README.md) | CONFIRMED docs | Roads/Rail/Trade owns historic routes, trade corridors, route membership, graph projections, publication/correction/rollback doctrine; `roads-rail-trade` is the data/docs/policy/test-style segment. | Implementation maturity remains PROPOSED/NEEDS VERIFICATION in parts. |
| [`../../docs/domains/roads-rail-trade/sublanes/trade_routes.md`](../../docs/domains/roads-rail-trade/sublanes/trade_routes.md) | CONFIRMED docs | Defines trade-route/historic-corridor scope and says the sublane is documentation-only and does not create `data/trade-routes/`. | It also records filename/terminology conflicts that remain unresolved. |
| [`../../docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md`](../../docs/domains/roads-rail-trade/FILE_SYSTEM_PLAN.md) | CONFIRMED draft plan | Applies responsibility-root placement and domain-lane pattern to Roads/Rail/Trade. | Marks many repo-state claims as NEEDS VERIFICATION. |
| [`../processed/roads-rail-trade/README.md`](../processed/roads-rail-trade/README.md) | CONFIRMED README | Canonical processed lane for roads, rail, historic route claims, trade-route corridors, route membership, and graph candidates. | Does not prove payload inventory. |
| [`../catalog/domain/roads-rail-trade/README.md`](../catalog/domain/roads-rail-trade/README.md) | CONFIRMED README | Canonical domain catalog lane for Roads/Rail/Trade catalog records and indexes. | Catalog records are not proof or release decisions. |
| [`../registry/sources/roads-rail-trade/README.md`](../registry/sources/roads-rail-trade/README.md) | CONFIRMED README | Source registry/admission lane for Roads/Rail/Trade sources, roles, rights, sensitivity, and no-public-path posture. | Registry records do not authorize publication. |
| [`../proofs/roads-rail-trade/README.md`](../proofs/roads-rail-trade/README.md) | CONFIRMED README | Proof support lane for evidence closure, source-role separation, corridor proof, sensitivity, release, correction, and rollback. | Proof lane does not publish by itself. |
| [`../published/roads-rail-trade/README.md`](../published/roads-rail-trade/README.md) | CONFIRMED README | Released public-safe non-layer Roads/Rail/Trade artifact lane. | Does not prove released payloads exist. |
| [`../published/layers/roads-rail-trade/README.md`](../published/layers/roads-rail-trade/README.md) | CONFIRMED README | Released public-safe Roads/Rail/Trade layer lane and child layer index. | Does not prove layer payloads exist. |

[Back to top](#top)
