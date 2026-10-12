<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/soil/readme
name: Soil Receipts README
path: data/receipts/soil/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <soil-domain-steward>
  - <soil-source-steward>
  - <soil-policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: soil-receipts
receipt_scope: soil-process-memory
domain: soil
path_posture: domain-receipt-parent-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; support-type-separation-required; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/soil/README.md
  - ../../work/soil/README.md
  - ../../quarantine/soil/README.md
  - ../../processed/soil/README.md
  - ../../proofs/soil/README.md
  - ../../catalog/domain/soil/README.md
  - ../../published/layers/soil/README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/API_CONTRACTS.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../connectors/nrcs/gssurgo/README.md
  - ../../../connectors/nrcs/ssurgo/README.md
  - ../../../pipelines/domains/soil/README.md
  - ../../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../../pipeline_specs/soil/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - soil
  - ssurgo
  - gssurgo
  - gnatsgo
  - soil-data-access
  - soil-moisture
  - support-type
  - source-role
  - run-receipt
  - transform-receipt
  - redaction-receipt
  - aggregation-receipt
  - validation-report
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/soil/README.md`."
  - "No child receipt README lanes under `data/receipts/soil/` were confirmed during this edit."
  - "Soil architecture says support-type separation is mandatory: static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface."
  - "Soil architecture says unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion."
  - "README presence confirms documentation only; it does not prove emitted receipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Receipts

Domain parent receipt lane for Soil process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/soil/` is for Soil receipt process memory only. It is not soil truth, survey truth, gridded-derivative truth, sensor-observation truth, interpretation authority, source registry authority, policy authority, proof, catalog authority, release authority, published artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the Soil domain parent lane for receipts that document governed process memory: source-intake support, SSURGO/SDA/gSSURGO/gNATSGO support, soil-moisture observation support, validation support, transform support, redaction/generalization support, aggregation support, review support, pipeline-run support, correction support, rollback support, and release-candidate support.

The Soil lane covers static soil survey evidence, gridded soil derivatives, components, horizons, pedons, soil-moisture observations, soil interpretations, suitability, erosion context, soil time caveats, and public-safe soil map/API products after release.

Receipts record what a process did, what references it inspected, what finite outcome or decision class it produced, and what evidence, policy, review, validation, source-role, support-type, correction, rollback, or release-candidate references should travel downstream.

Receipts do **not** prove soil map-unit truth, component truth, horizon truth, soil-moisture truth, survey authority, gridded-derivative authority, suitability truth, erosion-context truth, release state, or public-safe publication. They also do not replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Soil domain parent lane is:

```text
data/receipts/soil/
```

The live repository target existed as a greenfield stub before this edit. No child receipt README lanes under `data/receipts/soil/` were confirmed during this edit. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/soil/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | soil |
| Scope | Soil process memory across intake, validation, transform, redaction, aggregation, review, correction, rollback, and release-support steps |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Lifecycle payload authority | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, `data/processed/soil/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/`, not this lane |
| Schema authority | `schemas/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, support type, identity basis, time facets, rights, sensitivity, review state, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

No child receipt README lanes were confirmed under `data/receipts/soil/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `ingest/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `transform/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `redaction/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `aggregation/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `pipeline/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `release/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |

This confirms only current README/path evidence. It does **not** prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed processes did; it is not the truth source. |
| Support types stay separate | Static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface. |
| Source roles stay explicit | Authority, observation, context, model, gridded derivative, station observation, and interpretive uses must not collapse. |
| Identity remains evidence-bound | MUKEY, COKEY, CHKEY, horizon joins, pedon/profile identity, source IDs, and digests must remain traceable. |
| Time facets stay distinct | Source, observed, valid, retrieval, release, and correction times stay separate where material. |
| Cross-lane ownership stays intact | Agriculture, Hydrology, Hazards, Geology, Habitat, Flora, and Fauna retain their own truth boundaries. |
| Review-gated detail stays protected | Non-public, proprietary, operational, or cross-lane-sensitive details require rights, policy, review, proof, and release support before use. |
| Interpretations carry caveats | Suitability and erosion-context products must preserve source role, support type, time, scale, and limitation caveats. |
| Policy remains separate | Binding sensitivity, rights, source-role, publication, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt parent. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Soil receipt instances and receipt-local sidecars:

- RunReceipt, TransformReceipt, RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, support-type refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, aggregation refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, soil truth, survey truth, sensor truth, interpretation authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Soil source payloads | `data/raw/soil/` or accepted restricted source storage |
| Work/candidate outputs | `data/work/soil/` |
| Quarantined material | `data/quarantine/soil/` |
| Processed Soil payloads | `data/processed/soil/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Connectors, fetchers, package helpers, executable pipeline code, or pipeline specs | `connectors/`, `packages/`, `pipelines/`, and `pipeline_specs/` |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, generated answer text, recommendation text, or planning instructions | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/soil/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, release authority, soil authority, recommendation source, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Soil domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, source refs, object refs, support-type refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, support-type separation, object identity basis, time facets, public geometry posture, caveats, and limitations are preserved where material.
- [ ] Confirm restricted or cross-lane-sensitive detail is not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative, aggregation, interpretation, redaction, or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Soil claim path.
- [ ] Confirm receipt presence is not treated as soil truth, survey truth, sensor-observation truth, interpretation authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when support type, policy, review, rights, sensitivity, evidence, validation, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, released layer, recommendation text, or planning instruction uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/soil/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No child receipt README lanes under `data/receipts/soil/` were confirmed during this edit. | **CONFIRMED by GitHub search during this edit** |
| Soil architecture says Soil owns static soil-survey evidence, gridded soil derivatives, components, horizons, pedons, soil-moisture observations, interpretations, suitability, erosion context, and public-safe soil map/API products. | **CONFIRMED by GitHub contents API during this edit** |
| Soil architecture says support-type separation is mandatory and untagged support-type mixing is denied, abstained, or quarantined. | **CONFIRMED by GitHub contents API during this edit** |
| Soil architecture says unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| Exact receipt subtype layout under `data/receipts/soil/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Soil receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is soil truth, survey truth, gridded-derivative truth, sensor-observation truth, interpretation authority, policy authority, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/soil/README.md`](../../raw/soil/README.md)
- [`../../work/soil/README.md`](../../work/soil/README.md)
- [`../../quarantine/soil/README.md`](../../quarantine/soil/README.md)
- [`../../processed/soil/README.md`](../../processed/soil/README.md)
- [`../../proofs/soil/README.md`](../../proofs/soil/README.md)
- [`../../catalog/domain/soil/README.md`](../../catalog/domain/soil/README.md)
- [`../../published/layers/soil/README.md`](../../published/layers/soil/README.md)
- [`../../../docs/domains/soil/ARCHITECTURE.md`](../../../docs/domains/soil/ARCHITECTURE.md)
- [`../../../docs/domains/soil/DATA_LIFECYCLE.md`](../../../docs/domains/soil/DATA_LIFECYCLE.md)
- [`../../../docs/domains/soil/CANONICAL_PATHS.md`](../../../docs/domains/soil/CANONICAL_PATHS.md)
- [`../../../docs/domains/soil/API_CONTRACTS.md`](../../../docs/domains/soil/API_CONTRACTS.md)
- [`../../../docs/sources/catalog/nrcs/ssurgo.md`](../../../docs/sources/catalog/nrcs/ssurgo.md)
- [`../../../docs/sources/catalog/nrcs/gssurgo.md`](../../../docs/sources/catalog/nrcs/gssurgo.md)
- [`../../../connectors/nrcs/gssurgo/README.md`](../../../connectors/nrcs/gssurgo/README.md)
- [`../../../connectors/nrcs/ssurgo/README.md`](../../../connectors/nrcs/ssurgo/README.md)
- [`../../../pipelines/domains/soil/README.md`](../../../pipelines/domains/soil/README.md)
- [`../../../pipelines/domains/soil/ssurgo_ingest/README.md`](../../../pipelines/domains/soil/ssurgo_ingest/README.md)
- [`../../../pipeline_specs/soil/README.md`](../../../pipeline_specs/soil/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/soil/` is a Soil receipt parent lane for process memory only. It is not soil truth, survey truth, gridded-derivative truth, sensor-observation truth, interpretation authority, policy authority, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
