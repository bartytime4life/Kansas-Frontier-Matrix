<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/hazards/readme
name: Hazards Receipts README
path: data/receipts/hazards/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <hazards-domain-steward>
  - <validation-steward>
  - <freshness-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: hazards-receipts
receipt_scope: hazards-domain-process-memory
domain: hazards
path_posture: domain-receipt-parent-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; not-emergency-alert-system; not-life-safety-authority; source-role-preserving; freshness-bound; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/hazards/README.md
  - ../../work/hazards/README.md
  - ../../quarantine/hazards/README.md
  - ../../processed/hazards/README.md
  - ../../proofs/hazards/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/hazards/README.md
  - ../../published/layers/hazards/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/EXPANSION_PLAN.md
  - ../../../docs/domains/hazards/EXPANSION_BACKLOG.md
  - ../../../pipelines/domains/hazards/README.md
  - ../../../pipeline_specs/hazards/README.md
  - ../../../contracts/domains/hazards/domain_feature_identity.md
  - ../../../docs/sources/catalog/noaa/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - hazards
  - process-memory
  - not-emergency-alert-system
  - not-life-safety-authority
  - source-role
  - freshness
  - warning-context
  - advisory-context
  - regulatory-context
  - remote-sensing-detection
  - model-run-receipt
  - validation-report
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/hazards/README.md`."
  - "No substantive child receipt README lanes under `data/receipts/hazards/` were confirmed during this edit."
  - "Hazards domain doctrine says KFM is not an emergency alert system and operational warning/advisory/watch material is context only, not life-safety authority."
  - "Hazards lifecycle doctrine requires source-role, freshness, evidence, policy, release, correction, and rollback closure before public-safe use."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, freshness enforcement, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Receipts

Domain parent receipt lane for Hazards process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-8b0000">
  <img alt="Boundary: not alert system" src="https://img.shields.io/badge/boundary-not%20alert%20system-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/hazards/` is for Hazards receipt process memory only. It is not emergency alert authority, life-safety authority, hazard truth, regulatory determination authority, observed-event proof, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is the Hazards-domain parent lane for receipts that document governed process memory: source intake support, transform support, source-role validation, freshness checks, warning/advisory/watch context handling, regulatory-context handling, remote-sensing candidate handling, model/materialization support, correction support, rollback support, and release-candidate support.

Hazards receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, source-role, freshness, validation, transform, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove hazard claims, approve public release, issue warnings, provide life-safety guidance, establish regulatory determinations, confirm remote-sensing candidates as events, or replace SourceDescriptors, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, or official source links.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Hazards domain parent lane is:

```text
data/receipts/hazards/
```

No substantive child receipt README lanes under this parent were confirmed during this edit. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/hazards/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | hazards |
| Scope | Hazards process memory across source intake support, transform, validation, freshness, operational-context, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, `data/processed/hazards/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/domains/hazards/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/hazards/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, freshness, expiry, official source link, rights, sensitivity, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

No child receipt README lanes were confirmed under `data/receipts/hazards/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `warning_context/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `freshness/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `model_run/` | **UNKNOWN** | Not confirmed by current-session repo search. |

This confirms only current README/path evidence. It does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, freshness enforcement, correction hooks, rollback hooks, or release integration.

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Hazards processes did; it is not the truth source. |
| KFM is not an alert system | Receipts may document operational context, but they cannot issue warnings or life-safety instructions. |
| Official sources remain authoritative | Urgent hazard action must redirect to official sources, not KFM receipt lanes or generated summaries. |
| Source roles stay explicit | Historical, regulatory, administrative, observed, modeled, aggregate, candidate, synthetic, and operational-context material must not collapse. |
| Freshness is material | Warning/advisory/watch context must carry issue, expiry, retrieval, freshness, and source state where applicable. |
| Candidate material stays candidate | Remote-sensing detections and unreviewed anomalies require review before being treated as confirmed events. |
| Regulatory context is not observed reality | Regulatory flood or hazard areas are not observed inundation, forecasts, or model outputs unless independently supported. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Hazards receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, freshness, model/materialization, aggregation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `ModelRunReceipt`, `AggregationReceipt`, `PolicyDecision`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, source-role refs, freshness refs, issue/expiry/retrieval time refs, official-source refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, emergency alert authority, life-safety authority, hazard truth, regulatory determination authority, or generated-answer authority.

Do not put emergency instructions, live alert substitutes, official-source impersonation, unsupported current-state claims, unresolved operational context, expired context presented as current, private-party details, infrastructure-sensitive details, or unsupported source-as-authority claims into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw hazard feeds, agency payloads, event packets, alert payloads, or source-native files | `data/raw/hazards/` or source-specific raw lanes |
| Work/scratch candidates, normalization drafts, model experiments, or transform drafts | `data/work/hazards/` |
| Quarantined Hazards material | `data/quarantine/hazards/` and child quarantine lanes where applicable |
| Normalized Hazards payloads | `data/processed/hazards/` and accepted sublanes |
| Released layers, PMTiles, reports, or public downloads | `data/published/` only after release gates close |
| Pipeline executable logic | `pipelines/domains/hazards/` |
| Pipeline declarative specs | `pipeline_specs/hazards/` |
| Semantic contracts | `contracts/domains/hazards/` |
| Machine schemas | `schemas/contracts/v1/domains/hazards/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Source-role, rights, sensitivity, freshness, advisory, alert-boundary, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Emergency instructions, live alert delivery, regulatory determinations, or life-safety guidance | Official external authorities and governed redirects, never this receipt lane |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/hazards/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, freshness enforcement, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, alert authority, hazard truth index, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, freshness refs, official-source refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Life-safety use, alert substitution, expired context, unresolved source role, unresolved sensitivity, missing evidence, missing official-source reference, or release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required source-role or freshness limits, collapses source meaning, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation/freshness support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/hazards/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / alert / warning / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Hazards receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Hazards domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, knowledge character, official-source link, issue time, expiry time, retrieval time, freshness state, and correction state remain explicit where material.
- [ ] Confirm operational context is marked not-for-life-safety and cannot substitute for official emergency instructions.
- [ ] Confirm candidate, modeled, regulatory, administrative, aggregate, observed, and synthetic material remain distinct.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Hazards claim path.
- [ ] Confirm receipt presence is not treated as hazard truth, emergency alert authority, life-safety authority, regulatory determination, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/quarantine states are recorded when life-safety boundary, rights, sensitivity, source role, freshness, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, report, generated answer, alert, warning, or life-safety statement uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/hazards/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No substantive child receipt README lanes under `data/receipts/hazards/` were confirmed during this edit. | **CONFIRMED by GitHub search during this edit / limited to current search evidence** |
| Hazards doctrine says KFM is not an emergency alert system and operational warning/advisory/watch context is not life-safety authority. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards doctrine says source roles and knowledge-character labels are not interchangeable and must not collapse. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards lifecycle doctrine says promotion follows RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and is governed, not a file move. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards receipt README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, freshness enforcement, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/hazards/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Hazards receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is emergency alert authority, life-safety authority, hazard truth, regulatory determination authority, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/hazards/README.md`](../../raw/hazards/README.md)
- [`../../work/hazards/README.md`](../../work/hazards/README.md)
- [`../../quarantine/hazards/README.md`](../../quarantine/hazards/README.md)
- [`../../processed/hazards/README.md`](../../processed/hazards/README.md)
- [`../../proofs/hazards/README.md`](../../proofs/hazards/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/hazards/README.md`](../../catalog/domain/hazards/README.md)
- [`../../published/layers/hazards/README.md`](../../published/layers/hazards/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/hazards/ARCHITECTURE.md`](../../../docs/domains/hazards/ARCHITECTURE.md)
- [`../../../docs/domains/hazards/DATA_LIFECYCLE.md`](../../../docs/domains/hazards/DATA_LIFECYCLE.md)
- [`../../../docs/domains/hazards/EXPANSION_PLAN.md`](../../../docs/domains/hazards/EXPANSION_PLAN.md)
- [`../../../docs/domains/hazards/EXPANSION_BACKLOG.md`](../../../docs/domains/hazards/EXPANSION_BACKLOG.md)
- [`../../../pipelines/domains/hazards/README.md`](../../../pipelines/domains/hazards/README.md)
- [`../../../pipeline_specs/hazards/README.md`](../../../pipeline_specs/hazards/README.md)
- [`../../../contracts/domains/hazards/domain_feature_identity.md`](../../../contracts/domains/hazards/domain_feature_identity.md)
- [`../../../docs/sources/catalog/noaa/README.md`](../../../docs/sources/catalog/noaa/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/hazards/` is a Hazards receipt parent lane for process memory only. It is not emergency alert authority, life-safety authority, hazard truth, regulatory determination authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
