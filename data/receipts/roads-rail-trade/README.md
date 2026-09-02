<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/roads-rail-trade/readme
name: Roads Rail Trade Receipts README
path: data/receipts/roads-rail-trade/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <roads-rail-trade-domain-steward>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: roads-rail-trade-receipts
receipt_scope: roads-rail-trade-process-memory
domain: roads-rail-trade
path_posture: domain-receipt-parent-lane; redaction-child-lane-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; derived-graph-not-truth; review-required-for-sensitive-corridors-and-critical-facilities; release-blocked
related:
  - redaction/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/roads-rail-trade/README.md
  - ../../work/roads-rail-trade/README.md
  - ../../quarantine/roads-rail-trade/README.md
  - ../../processed/roads-rail-trade/README.md
  - ../../proofs/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/ARCHITECTURE.md
  - ../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../../docs/domains/roads-rail-trade/RELEASE_INDEX.md
  - ../../../contracts/domains/roads-rail-trade/trade_route_corridor.md
  - ../../../contracts/domains/roads-rail-trade/network_edge.md
  - ../../../contracts/domains/roads-rail-trade/route_uncertainty_profile.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - roads-rail-trade
  - roads
  - rail
  - trade-routes
  - process-memory
  - redaction-receipt
  - aggregation-receipt
  - review-record
  - validation-report
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/roads-rail-trade/README.md`."
  - "Confirmed child receipt README lane during this edit: `redaction/`."
  - "Roads/Rail/Trade architecture says source-role collapse is forbidden, derived graph projections are not canonical truth, and historic/Indigenous corridors require generalized public geometry and review where applicable."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted receipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads/Rail/Trade Receipts

Domain parent receipt lane for Roads/Rail/Trade process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: roads-rail-trade" src="https://img.shields.io/badge/domain-roads--rail--trade-6f42c1">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/roads-rail-trade/` is for Roads/Rail/Trade receipt process memory only. It is not route truth, transport-network truth, source registry authority, sensitivity policy, proof, catalog authority, release authority, published artifact authority, public API/UI material, routing guidance, dispatch guidance, or generated-answer authority.

---

## Scope

This directory is the Roads/Rail/Trade domain parent lane for receipts that document governed process memory: source-intake support, validation support, redaction/generalization support, aggregation support, review support, pipeline-run support, correction support, rollback support, and release-candidate support.

Receipts record what a process did, what references it inspected, what finite outcome or decision class it produced, and what evidence, policy, review, validation, source-role, correction, rollback, or release-candidate references should travel downstream.

Receipts do **not** prove road alignment, rail alignment, historic route claims, trade corridor geometry, facility identity, closure authority, transport status, derived graph truth, release state, or public-safe publication. They also do not replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Roads/Rail/Trade domain parent lane is:

```text
data/receipts/roads-rail-trade/
```

The child lane `redaction/` is confirmed as a substantive README file in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/roads-rail-trade/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | roads-rail-trade |
| Scope | Roads/Rail/Trade process memory across intake, validation, redaction, aggregation, review, correction, rollback, and release-support steps |
| Confirmed child receipt lanes | `redaction/` |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Lifecycle payload authority | `data/raw/roads-rail-trade/`, `data/work/roads-rail-trade/`, `data/quarantine/roads-rail-trade/`, `data/processed/roads-rail-trade/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/domains/roads-rail-trade/`, not this lane |
| Schema authority | `schemas/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, route uncertainty, rights, sensitivity, review state, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`redaction/`](redaction/README.md) | **CONFIRMED README** | Roads/Rail/Trade redaction process memory for public generalization support, sensitive-route review handoff, public-safe corridor shaping, derived-graph safety checks, validation support, correction, rollback, and release-candidate support. | Not route truth, network truth, location authority, sensitivity policy, proof, release approval, routing guidance, dispatch guidance, or public artifact authority. |

Other Roads/Rail/Trade receipt child lanes are **UNKNOWN** until verified by repository evidence.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed processes did; it is not the truth source. |
| Source roles stay explicit | Modern graph, historic route claim, operational status, restriction event, source observation, and derived network projection roles must not collapse. |
| Derived graphs stay derived | Network edges and connectivity projections remain downstream carriers, not canonical truth. |
| Historic route uncertainty stays visible | Receipts must not erase uncertainty or overstate precision. |
| Cross-lane ownership stays intact | Settlements, Hydrology, Hazards, Archaeology, Cultural Heritage, and People/Land retain their own truth boundaries. |
| Policy remains separate | Binding sensitivity, rights, source-role, publication, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt parent. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Roads/Rail/Trade receipt instances and receipt-local sidecars:

- RunReceipt, RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, aggregation refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, route truth, network truth, routing source, dispatch source, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Roads/Rail/Trade source payloads | `data/raw/roads-rail-trade/` |
| Work/candidate outputs | `data/work/roads-rail-trade/` |
| Quarantined Roads/Rail/Trade material | `data/quarantine/roads-rail-trade/` |
| Processed Roads/Rail/Trade payloads | `data/processed/roads-rail-trade/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Pipeline code, tests, fixtures, package code, or CI workflows | `pipelines/`, `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, routing instructions, dispatch instructions, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/roads-rail-trade/
├── README.md
├── redaction/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, routing source, policy authority, release authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Roads/Rail/Trade domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, source refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, route uncertainty, public generalization posture, review state, caveats, and limitations are preserved where material.
- [ ] Confirm sensitive route detail, restricted facility detail, and re-identifying cross-lane detail are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Roads/Rail/Trade claim path.
- [ ] Confirm receipt presence is not treated as route truth, network truth, routing authority, dispatch authority, location authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, released layer, routing instruction, or dispatch instruction uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/roads-rail-trade/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `redaction/`. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade architecture says derived graph and connectivity projections are downstream carriers and never canonical truth. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade architecture says source-role collapse is forbidden and source role is fixed at admission. | **CONFIRMED by GitHub contents API during this edit** |
| Roads/Rail/Trade architecture says sensitive historic/cultural corridors default to generalized public geometry and review where applicable. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| Exact receipt subtype layout under `data/receipts/roads-rail-trade/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Roads/Rail/Trade receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is route truth, network truth, routing authority, dispatch authority, location authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`redaction/README.md`](redaction/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/roads-rail-trade/README.md`](../../raw/roads-rail-trade/README.md)
- [`../../work/roads-rail-trade/README.md`](../../work/roads-rail-trade/README.md)
- [`../../quarantine/roads-rail-trade/README.md`](../../quarantine/roads-rail-trade/README.md)
- [`../../processed/roads-rail-trade/README.md`](../../processed/roads-rail-trade/README.md)
- [`../../proofs/roads-rail-trade/README.md`](../../proofs/roads-rail-trade/README.md)
- [`../../../docs/domains/roads-rail-trade/ARCHITECTURE.md`](../../../docs/domains/roads-rail-trade/ARCHITECTURE.md)
- [`../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md`](../../../docs/domains/roads-rail-trade/DATA_LIFECYCLE.md)
- [`../../../docs/domains/roads-rail-trade/RELEASE_INDEX.md`](../../../docs/domains/roads-rail-trade/RELEASE_INDEX.md)
- [`../../../contracts/domains/roads-rail-trade/trade_route_corridor.md`](../../../contracts/domains/roads-rail-trade/trade_route_corridor.md)
- [`../../../contracts/domains/roads-rail-trade/network_edge.md`](../../../contracts/domains/roads-rail-trade/network_edge.md)
- [`../../../contracts/domains/roads-rail-trade/route_uncertainty_profile.md`](../../../contracts/domains/roads-rail-trade/route_uncertainty_profile.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/roads-rail-trade/` is a Roads/Rail/Trade receipt parent lane for process memory only. It is not route truth, network truth, routing authority, dispatch authority, location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
