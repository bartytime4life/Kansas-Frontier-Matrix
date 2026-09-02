<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/habitat/land-cover/readme
name: Habitat Land Cover Receipts README
path: data/receipts/habitat/land_cover/README.md
type: data-receipts-domain-sublane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <habitat-domain-steward>
  - <land-cover-steward>
  - <source-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: habitat-land-cover-receipts
receipt_scope: habitat-land-cover-process-memory
domain: habitat
object_family: LandCoverObservation
path_posture: requested-domain-sublane-receipt-lane; parent-habitat-receipt-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; native-classification-preserved; advisory-crosswalk-not-authority; restricted-joins-fail-closed; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/habitat/README.md
  - ../../../work/habitat/README.md
  - ../../../quarantine/habitat/README.md
  - ../../../quarantine/habitat/land_cover/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/land_cover/README.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover/README.md
  - ../../../../pipelines/domains/habitat/land_cover/README.md
  - ../../../../pipeline_specs/habitat/land_cover/README.md
  - ../../../../contracts/domains/habitat/land_cover_observation.md
  - ../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - habitat
  - land-cover
  - land-cover-observation
  - native-classification
  - advisory-crosswalk
  - transform-receipt
  - validation-report
  - model-run-receipt
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/habitat/land_cover/README.md`."
  - "Parent `data/receipts/habitat/README.md` is currently a greenfield stub."
  - "Habitat land-cover docs confirm LandCoverObservation, native classification preservation, advisory/lossy crosswalks, source vintage requirements, and restricted-join fail-closed posture."
  - "Pipeline docs confirm land-cover pipeline logic is not public release and that receipt emission remains implementation-sensitive."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted land-cover receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Land Cover Receipts

Receipt lane for Habitat land-cover process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: LandCoverObservation" src="https://img.shields.io/badge/object-LandCoverObservation-7048e8">
  <img alt="Crosswalk: advisory only" src="https://img.shields.io/badge/crosswalk-advisory%20only-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/habitat/land_cover/` is for Habitat land-cover receipt process memory only. It is not land-cover truth, habitat truth, native-classification authority, crosswalk authority, proof, EvidenceBundle authority, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipt records and receipt-local sidecars that document Habitat land-cover processing: source intake support, native classification preservation, class-map version checks, advisory crosswalk attachment, raster/vector metadata validation, source-vintage handling, restricted-join checks, model/materialization support, correction support, rollback support, and release-candidate support.

Receipts document what a process did. They may cite run IDs, source refs, object refs, source roles, class-map refs, input/output hashes, validation outcomes, policy refs, evidence refs, correction refs, rollback refs, and release-candidate refs.

Receipts do **not** prove land-cover values, define `LandCoverObservation`, make a crosswalk authoritative, approve public release, resolve source rights, or replace contracts, schemas, EvidenceBundles, ProofPacks, catalog records, PolicyDecisions, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested Habitat land-cover receipt lane is:

```text
data/receipts/habitat/land_cover/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/habitat/README.md` is still a greenfield stub, and exact domain/sublane receipt naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/habitat/land_cover/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | habitat |
| Object family | `LandCoverObservation` |
| Sublane scope | Land-cover process memory: native classification, advisory crosswalk, validation, model/materialization, restricted-join, correction, rollback, and release-support records |
| Path posture | requested domain/sublane receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/habitat/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Pipeline logic authority | `pipelines/domains/habitat/land_cover/`, not this lane |
| Pipeline spec authority | `pipeline_specs/habitat/land_cover/`, not this lane |
| Contract authority | `contracts/domains/habitat/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/habitat/`, not this lane |
| Lifecycle payload lanes | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, rights, source vintage, native class map, advisory-crosswalk provenance, restricted joins, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed land-cover processes did; it is not land-cover truth or release approval. |
| Native classification is preserved | Source class codes, labels, epochs, and class-map versions must remain auditable. |
| Crosswalks are advisory | Cross-scheme mappings are lossy context and must not overwrite native source classification or become authority. |
| Source roles stay explicit | Authority, observation, context, model, derived, aggregate, candidate, and synthetic roles must not collapse. |
| Source vintage matters | Stale land cover must not be presented as current; relevant time facets stay distinct. |
| Restricted joins fail closed | Joins with restricted ecology, land, or cultural context are denied or generalized unless governed evidence, policy, review, and transform support exists. |
| Downstream lanes retain truth ownership | Land cover can inform other domains; it does not replace those domains' truth. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Habitat land-cover receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, crosswalk, model/materialization, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `ModelRunReceipt`, `PolicyDecision`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, source-role refs, source epoch refs, class-map version refs, native class summaries, advisory crosswalk refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, land-cover truth, habitat truth, crosswalk authority, or generated-answer authority.

Do not put raw raster payloads, raw source packages, normalized data payloads, full class maps that belong to contracts/sources, restricted joins, private-party details, unsafe transform parameters, or unsupported source-as-authority claims into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw land-cover source payloads | `data/raw/habitat/` or source-specific raw lanes |
| Work/scratch candidates, crosswalk experiments, or transform drafts | `data/work/habitat/` |
| Quarantined land-cover material | `data/quarantine/habitat/` and `data/quarantine/habitat/land_cover/` where applicable |
| Normalized `LandCoverObservation` payloads | `data/processed/habitat/` and accepted sublanes |
| Released land-cover layers, PMTiles, reports, or public downloads | `data/published/layers/habitat/land_cover/` only after release gates close |
| Pipeline executable logic | `pipelines/domains/habitat/land_cover/` |
| Pipeline declarative specs | `pipeline_specs/habitat/land_cover/` |
| Semantic contracts or crosswalk authority | `contracts/domains/habitat/` |
| Machine schemas | `schemas/contracts/v1/domains/habitat/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Source-role, rights, sensitivity, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/habitat/land_cover/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── transform_receipt.json
│   ├── validation_report.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── crosswalk/
│   └── <run_id>/
│       └── README.md
├── validation/
│   └── <run_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, land-cover truth index, crosswalk authority, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, source-vintage refs, class-map refs, crosswalk refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Rights, sensitivity, source role, restricted joins, evidence, policy, stale-source posture, or release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits native classification, overwrites native class with a crosswalk class, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation/crosswalk support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/habitat/land_cover/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Habitat land-cover receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Habitat domain and `land_cover` receipt lane.
- [ ] Confirm canonical domain/sublane receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm native source classification, class-map version, source epoch/vintage, source role, relevant time facets, CRS/resolution/nodata posture, and advisory crosswalk provenance remain explicit.
- [ ] Confirm crosswalk classes are not treated as authoritative native classes and do not overwrite native classification.
- [ ] Confirm restricted joins fail closed unless proof, policy, review, and transform support resolve the exposure.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public Habitat land-cover claim path.
- [ ] Confirm receipt presence is not treated as land-cover truth, habitat truth, crosswalk authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/quarantine states are recorded when rights, sensitivity, source role, crosswalk provenance, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, report, generated answer, or domain claim uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/habitat/land_cover/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat land-cover docs identify `LandCoverObservation`, source families including NLCD/CDL/LANDFIRE/GAP/NWI, native-classification preservation, and advisory-only crosswalks. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat land-cover docs say restricted joins fail closed and publication requires ReleaseManifest, EvidenceBundle, validation/policy support, correction path, and rollback target. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat land-cover pipeline docs say pipeline output is not public release and native classifications, source roles, evidence, rights, time, sensitivity, and public-safe release boundaries must be preserved. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/habitat/land_cover/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Habitat land-cover receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is land-cover truth, habitat truth, native-classification authority, crosswalk authority, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/habitat/README.md`](../../../raw/habitat/README.md)
- [`../../../work/habitat/README.md`](../../../work/habitat/README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../quarantine/habitat/land_cover/README.md`](../../../quarantine/habitat/land_cover/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/land_cover/README.md`](../../../published/layers/habitat/land_cover/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/habitat/sublanes/land_cover/README.md`](../../../../docs/domains/habitat/sublanes/land_cover/README.md)
- [`../../../../pipelines/domains/habitat/land_cover/README.md`](../../../../pipelines/domains/habitat/land_cover/README.md)
- [`../../../../pipeline_specs/habitat/land_cover/README.md`](../../../../pipeline_specs/habitat/land_cover/README.md)
- [`../../../../contracts/domains/habitat/land_cover_observation.md`](../../../../contracts/domains/habitat/land_cover_observation.md)
- [`../../../../contracts/domains/habitat/land_cover/crosswalk.md`](../../../../contracts/domains/habitat/land_cover/crosswalk.md)
- [`../../../../contracts/domains/habitat/land_cover/model_run_receipt.md`](../../../../contracts/domains/habitat/land_cover/model_run_receipt.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/habitat/land_cover/` is a Habitat land-cover receipt lane for process memory only. It is not land-cover truth, habitat truth, native-classification authority, crosswalk authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
