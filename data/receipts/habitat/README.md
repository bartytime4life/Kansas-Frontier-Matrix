<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/habitat/readme
name: Habitat Receipts README
path: data/receipts/habitat/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <habitat-domain-steward>
  - <land-cover-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: habitat-receipts
receipt_scope: habitat-domain-process-memory
domain: habitat
path_posture: domain-receipt-parent-lane; land-cover-child-lane-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; native-classification-preserved; advisory-crosswalk-not-authority; restricted-joins-fail-closed; release-blocked
related:
  - land_cover/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/habitat/README.md
  - ../../work/habitat/README.md
  - ../../quarantine/habitat/README.md
  - ../../processed/habitat/README.md
  - ../../catalog/domain/habitat/README.md
  - ../../published/layers/habitat/README.md
  - ../../published/layers/habitat/land_cover/README.md
  - ../../proofs/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/habitat/sublanes/land_cover/README.md
  - ../../../pipelines/domains/habitat/land_cover/README.md
  - ../../../pipeline_specs/habitat/land_cover/README.md
  - ../../../contracts/domains/habitat/README.md
  - ../../../contracts/domains/habitat/land_cover_observation.md
  - ../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../contracts/domains/habitat/land_cover/model_run_receipt.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - habitat
  - process-memory
  - land-cover
  - land-cover-observation
  - native-classification
  - advisory-crosswalk
  - transform-receipt
  - validation-report
  - model-run-receipt
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/habitat/README.md`."
  - "Confirmed child receipt README lane during this edit: `land_cover/`."
  - "Habitat land-cover docs confirm LandCoverObservation, native classification preservation, advisory/lossy crosswalks, source vintage requirements, and restricted-join fail-closed posture."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Receipts

Domain parent receipt lane for Habitat process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/habitat/` is for Habitat receipt process memory only. It is not habitat truth, land-cover truth, restoration truth, occurrence truth, native-classification authority, crosswalk authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is the Habitat-domain parent lane for receipts that document governed process memory: source intake support, transform support, land-cover processing, validation support, advisory crosswalk support, restricted-join checks, correction support, rollback support, and release-candidate support.

Habitat receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, source-role, validation, transform, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove Habitat claims, approve public release, define object meaning, resolve source rights, authorize crosswalks, or replace SourceDescriptors, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Habitat domain parent lane is:

```text
data/receipts/habitat/
```

The child lane `land_cover/` is confirmed as a substantive README file in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/habitat/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | habitat |
| Scope | Habitat process memory across source intake support, transform, validation, land-cover, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Confirmed child receipt lanes | `land_cover/` |
| Lifecycle payload lanes | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/domains/habitat/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/habitat/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, rights, source vintage, native class map, advisory-crosswalk provenance, restricted joins, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`land_cover/`](land_cover/README.md) | **CONFIRMED README** | Habitat land-cover process memory for native classification preservation, advisory crosswalks, validation, model/materialization support, restricted-join checks, correction, rollback, and release-candidate support. | Not land-cover truth, Habitat truth, native-classification authority, crosswalk authority, proof, release approval, or public artifact authority. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Habitat processes did; it is not the truth source. |
| Source roles stay explicit | Authority, observation, context, model, derived, aggregate, candidate, and synthetic roles must not collapse. |
| Native classifications stay auditable | Where land-cover or similar classified surfaces are involved, source classes and class-map versions must remain inspectable. |
| Advisory crosswalks remain non-authoritative | Crosswalks can support interpretation, but they must not overwrite native source meaning or become root authority. |
| Restricted joins fail closed | Joins with restricted ecology, land, or cultural context require governed evidence, policy, review, and transform support before public use. |
| Downstream lanes retain truth ownership | Habitat context cannot overwrite Fauna, Flora, Agriculture, Hydrology, Soil, Hazards, or other domain truth. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Habitat receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, crosswalk, model/materialization, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `ModelRunReceipt`, `PolicyDecision`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, source-role refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, habitat truth, land-cover truth, crosswalk authority, or generated-answer authority.

Do not put raw source payloads, normalized data payloads, full class maps that belong to contracts/sources, restricted joins, private-party details, unsafe transform parameters, or unsupported source-as-authority claims into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Habitat source payloads | `data/raw/habitat/` or source-specific raw lanes |
| Work/scratch candidates, crosswalk experiments, or transform drafts | `data/work/habitat/` |
| Quarantined Habitat material | `data/quarantine/habitat/` and child quarantine lanes where applicable |
| Normalized Habitat payloads | `data/processed/habitat/` and accepted sublanes |
| Released layers, PMTiles, reports, or public downloads | `data/published/` only after release gates close |
| Pipeline executable logic | `pipelines/domains/habitat/` |
| Pipeline declarative specs | `pipeline_specs/habitat/` |
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
data/receipts/habitat/
├── README.md
├── land_cover/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, habitat truth index, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Rights, sensitivity, source role, restricted joins, evidence, policy, stale-source posture, or release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required source-role limits, collapses source meaning, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/habitat/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Habitat receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Habitat domain and a documented child receipt lane.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, source vintage, relevant time facets, and transformation provenance remain explicit where material.
- [ ] Confirm restricted joins fail closed unless proof, policy, review, and transform support resolve the exposure.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Habitat claim path.
- [ ] Confirm receipt presence is not treated as habitat truth, land-cover truth, crosswalk authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/quarantine states are recorded when rights, sensitivity, source role, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, report, generated answer, or domain claim uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/habitat/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `land_cover/`. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat land-cover docs identify `LandCoverObservation`, native-classification preservation, advisory-only crosswalks, source-vintage handling, and restricted-join fail-closed posture. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat receipt child README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/habitat/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Habitat receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is habitat truth, land-cover truth, native-classification authority, crosswalk authority, proof, catalog authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`land_cover/README.md`](land_cover/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/habitat/README.md`](../../raw/habitat/README.md)
- [`../../work/habitat/README.md`](../../work/habitat/README.md)
- [`../../quarantine/habitat/README.md`](../../quarantine/habitat/README.md)
- [`../../processed/habitat/README.md`](../../processed/habitat/README.md)
- [`../../catalog/domain/habitat/README.md`](../../catalog/domain/habitat/README.md)
- [`../../published/layers/habitat/README.md`](../../published/layers/habitat/README.md)
- [`../../published/layers/habitat/land_cover/README.md`](../../published/layers/habitat/land_cover/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/habitat/sublanes/land_cover/README.md`](../../../docs/domains/habitat/sublanes/land_cover/README.md)
- [`../../../pipelines/domains/habitat/land_cover/README.md`](../../../pipelines/domains/habitat/land_cover/README.md)
- [`../../../pipeline_specs/habitat/land_cover/README.md`](../../../pipeline_specs/habitat/land_cover/README.md)
- [`../../../contracts/domains/habitat/README.md`](../../../contracts/domains/habitat/README.md)
- [`../../../contracts/domains/habitat/land_cover_observation.md`](../../../contracts/domains/habitat/land_cover_observation.md)
- [`../../../contracts/domains/habitat/land_cover/crosswalk.md`](../../../contracts/domains/habitat/land_cover/crosswalk.md)
- [`../../../contracts/domains/habitat/land_cover/model_run_receipt.md`](../../../contracts/domains/habitat/land_cover/model_run_receipt.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/habitat/` is a Habitat receipt parent lane for process memory only. It is not habitat truth, land-cover truth, native-classification authority, crosswalk authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
