<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/settlements-infrastructure/readme
name: Settlements Infrastructure Receipts README
path: data/receipts/settlements-infrastructure/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <settlements-infrastructure-domain-steward>
  - <settlement-sublane-steward>
  - <infrastructure-sublane-steward>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: settlements-infrastructure-receipts
receipt_scope: settlements-infrastructure-process-memory
domain: settlements-infrastructure
path_posture: domain-receipt-parent-lane; condition-redaction-child-lane-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; condition-and-dependency-detail-restricted; critical-infrastructure-review-required; release-blocked
related:
  - condition_redaction/README.md
  - ../README.md
  - ../../README.md
  - ../../receipts/settlement/README.md
  - ../../raw/settlements-infrastructure/README.md
  - ../../work/settlements-infrastructure/README.md
  - ../../quarantine/settlements-infrastructure/README.md
  - ../../processed/settlements-infrastructure/README.md
  - ../../proofs/settlements-infrastructure/README.md
  - ../../proofs/settlement/README.md
  - ../../catalog/domain/settlements-infrastructure/README.md
  - ../../published/layers/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../packages/domains/settlements-infrastructure/README.md
  - ../../../packages/domains/settlement/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - settlements-infrastructure
  - settlements
  - infrastructure
  - process-memory
  - source-role
  - condition-observation
  - dependency
  - redaction-receipt
  - aggregation-receipt
  - validation-report
  - review-record
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/receipts/settlements-infrastructure/README.md`."
  - "Confirmed child receipt README lane during this edit: `condition_redaction/`."
  - "Settlements/Infrastructure doctrine owns settlement, municipality, census place, townsite, ghost town, fort, mission, reservation-community, infrastructure asset, network, facility, service-area, operator, condition-observation, and dependency evidence."
  - "The domain uses proposed settlements and infrastructure sublanes, but both share canonical responsibility roots keyed to `settlements-infrastructure`."
  - "README presence confirms documentation only; it does not prove emitted receipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements/Infrastructure Receipts

Domain parent receipt lane for Settlements/Infrastructure process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-1f6feb">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/settlements-infrastructure/` is for Settlements/Infrastructure receipt process memory only. It is not place truth, infrastructure truth, condition truth, dependency truth, source registry authority, sensitivity policy, proof, catalog authority, release authority, published artifact authority, public API/UI material, planning guidance, operations guidance, emergency guidance, or generated-answer authority.

---

## Scope

This directory is the Settlements/Infrastructure domain parent lane for receipts that document governed process memory: source-intake support, validation support, redaction/generalization support, aggregation support, review support, pipeline-run support, correction support, rollback support, and release-candidate support.

The broader domain covers settled-place evidence and infrastructure evidence: settlements, municipalities, census places, historic townsites, ghost towns, forts, missions, reservation communities, infrastructure assets, networks, facilities, service areas, operators, condition observations, dependencies, and public-safe derivatives.

Receipts record what a process did, what references it inspected, what finite outcome or decision class it produced, and what evidence, policy, review, validation, source-role, correction, rollback, or release-candidate references should travel downstream.

Receipts do **not** prove place identity, municipal status, census status, historic settlement status, infrastructure identity, asset condition, dependency state, operator status, release state, or public-safe publication. They also do not replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Settlements/Infrastructure domain parent lane is:

```text
data/receipts/settlements-infrastructure/
```

The child lane `condition_redaction/` is confirmed as a substantive README file in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

The singular `data/receipts/settlement/` path is documented separately as a settlement-sublane or compatibility lane. This README does not resolve naming governance between `settlement` and `settlements-infrastructure`.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/settlements-infrastructure/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | settlements-infrastructure |
| Scope | Settlements/Infrastructure process memory across intake, validation, redaction, aggregation, review, correction, rollback, and release-support steps |
| Confirmed child receipt lanes | `condition_redaction/` |
| Related settlement sublane | `data/receipts/settlement/` |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Lifecycle payload authority | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, `data/processed/settlements-infrastructure/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/`, not this lane |
| Schema authority | `schemas/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, identity basis, time facets, rights, sensitivity, review state, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`condition_redaction/`](condition_redaction/README.md) | **CONFIRMED README** | Condition-redaction process memory for infrastructure condition/dependency material, review handoff, redaction/generalization support, aggregation support, validation support, correction, rollback, and release-candidate support. | Not condition truth, dependency truth, infrastructure authority, sensitivity policy, proof, release approval, planning guidance, operations guidance, or public artifact authority. |

Other Settlements/Infrastructure receipt child lanes are **UNKNOWN** until verified by repository evidence.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed processes did; it is not the truth source. |
| Source roles stay explicit | Observed, regulatory, aggregate, administrative, candidate, synthetic, and context roles must not collapse. |
| Identity remains evidence-bound | Place labels, facility labels, operators, service areas, dependencies, condition records, and status events must remain distinct where evidence requires it. |
| Time facets stay distinct | Source, observed, valid, retrieval, release, and correction times stay separate where material. |
| Cross-lane ownership stays intact | Roads/Rail, Hydrology, Hazards, People/Land, Archaeology/Cultural Heritage, and other lanes retain their own truth boundaries. |
| Sensitive joins fail closed | Living-person, parcel/ownership, cultural, archaeology, reservation-community, operator, facility, service-area, condition, and dependency joins require policy and review support before use. |
| Condition/dependency detail stays protected | Condition observations and dependencies cannot become public merely because a receipt exists. |
| Policy remains separate | Binding sensitivity, rights, source-role, publication, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt parent. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Settlements/Infrastructure receipt instances and receipt-local sidecars:

- RunReceipt, TransformReceipt, RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, aggregation refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, place truth, infrastructure truth, condition truth, dependency truth, planning authority, operations authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Settlements/Infrastructure source payloads | `data/raw/settlements-infrastructure/` or accepted restricted source storage |
| Work/candidate outputs | `data/work/settlements-infrastructure/` |
| Quarantined material | `data/quarantine/settlements-infrastructure/` |
| Processed Settlements/Infrastructure payloads | `data/processed/settlements-infrastructure/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Package helpers or executable code | `packages/`, `pipelines/`, and approved tool roots |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, generated answer text, legal-status certification, condition reporting, planning instructions, operations instructions, or emergency instructions | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/settlements-infrastructure/
├── README.md
├── condition_redaction/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, release authority, place authority, condition authority, operations source, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Settlements/Infrastructure domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, source refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, object identity basis, time facets, public geometry posture, review state, caveats, and limitations are preserved where material.
- [ ] Confirm sensitive joins and restricted infrastructure, condition, dependency, operator, service-area, or facility detail are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where a public-safe derivative, cultural/steward review, infrastructure-adjacent context, or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Settlements/Infrastructure claim path.
- [ ] Confirm receipt presence is not treated as place truth, legal-status authority, census truth, infrastructure truth, condition truth, dependency truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, released layer, legal-status certification, condition report, planning instruction, operations instruction, or emergency instruction uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/settlements-infrastructure/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `condition_redaction/`. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine owns settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, infrastructure asset, network, facility, service-area, operator, condition-observation, and dependency evidence. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine says source role, temporal scope, evidence, sensitivity, release state, and cross-lane ownership must remain explicit. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine says condition observations, dependencies, operator-sensitive details, and exact facility geometry are restricted or review-gated by default. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| Exact receipt subtype layout under `data/receipts/settlements-infrastructure/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Settlements/Infrastructure receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is place truth, infrastructure truth, condition truth, dependency truth, planning authority, operations authority, emergency authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`condition_redaction/README.md`](condition_redaction/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../receipts/settlement/README.md`](../../receipts/settlement/README.md)
- [`../../raw/settlements-infrastructure/README.md`](../../raw/settlements-infrastructure/README.md)
- [`../../work/settlements-infrastructure/README.md`](../../work/settlements-infrastructure/README.md)
- [`../../quarantine/settlements-infrastructure/README.md`](../../quarantine/settlements-infrastructure/README.md)
- [`../../processed/settlements-infrastructure/README.md`](../../processed/settlements-infrastructure/README.md)
- [`../../proofs/settlements-infrastructure/README.md`](../../proofs/settlements-infrastructure/README.md)
- [`../../proofs/settlement/README.md`](../../proofs/settlement/README.md)
- [`../../catalog/domain/settlements-infrastructure/README.md`](../../catalog/domain/settlements-infrastructure/README.md)
- [`../../published/layers/settlements-infrastructure/README.md`](../../published/layers/settlements-infrastructure/README.md)
- [`../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md`](../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md)
- [`../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md)
- [`../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md`](../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md)
- [`../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md`](../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/settlements.md`](../../../docs/domains/settlements-infrastructure/sublanes/settlements.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
- [`../../../packages/domains/settlements-infrastructure/README.md`](../../../packages/domains/settlements-infrastructure/README.md)
- [`../../../packages/domains/settlement/README.md`](../../../packages/domains/settlement/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/settlements-infrastructure/` is a Settlements/Infrastructure receipt parent lane for process memory only. It is not place truth, infrastructure truth, condition truth, dependency truth, planning authority, operations authority, emergency authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
