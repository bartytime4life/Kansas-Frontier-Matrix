<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/settlement/readme
name: Settlement Receipts README
path: data/receipts/settlement/README.md
type: data-receipts-sublane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <settlements-infrastructure-domain-steward>
  - <settlement-sublane-steward>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: settlement-receipts
receipt_scope: settlement-sublane-process-memory
domain: settlement
canonical_domain_posture: singular-settlement-sublane-under-broader-settlements-infrastructure; naming-needs-verification
path_posture: requested-settlement-receipt-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; identity-and-time-anti-collapse-required; critical-infrastructure-and-sensitive-joins-fail-closed; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../proofs/settlement/README.md
  - ../../raw/settlements-infrastructure/README.md
  - ../../quarantine/settlements-infrastructure/README.md
  - ../../processed/settlements-infrastructure/README.md
  - ../../catalog/domain/settlements-infrastructure/README.md
  - ../../published/layers/settlements-infrastructure/README.md
  - ../../../packages/domains/settlement/README.md
  - ../../../packages/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - settlement
  - settlements-infrastructure
  - settlements-sublane
  - place-identity
  - municipality
  - census-place
  - townsite
  - ghost-town
  - fort
  - mission
  - reservation-community
  - source-role
  - validation-report
  - redaction-receipt
  - aggregation-receipt
  - review-record
  - policy-decision
  - correction
  - rollback
  - no-public-path
notes:
  - "This README replaces a blank placeholder at `data/receipts/settlement/README.md`."
  - "Search evidence shows singular `settlement` is used by `data/proofs/settlement/` and `packages/domains/settlement/`, while broader doctrine uses `settlements-infrastructure`."
  - "This README treats `data/receipts/settlement/` as a settlement-sublane receipt lane inside the broader Settlements/Infrastructure domain, not as a new standalone authority."
  - "No child receipt README lanes under `data/receipts/settlement/` were confirmed during this edit."
  - "README presence confirms documentation only; it does not prove emitted receipts, validators, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlement Receipts

Settlement-sublane receipt lane for process-memory records inside the broader Settlements/Infrastructure domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Sublane: settlement" src="https://img.shields.io/badge/sublane-settlement-2da44e">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-1f6feb">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Naming posture](#naming-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Boundary](#boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/settlement/` is for settlement-sublane receipt process memory only. It is not place truth, municipal-status certification, census truth, historic-townsite truth, infrastructure authority, property/ownership authority, proof, catalog authority, source registry authority, policy authority, release authority, public artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document governed settlement-sublane process memory: source-intake support, validation support, identity-normalization support, temporal-status support, redaction/generalization support, aggregation support, review support, correction support, rollback support, and release-candidate support.

Receipts record what a process did, what references it inspected, what finite outcome or decision class it produced, and what evidence, policy, review, validation, source-role, correction, rollback, or release-candidate references should travel downstream.

Receipts do **not** prove settlement identity, municipal status, census-place status, townsite status, ghost-town status, fort/mission status, reservation-community status, facility identity, infrastructure condition, dependency, ownership, release state, or public-safe publication. They also do not replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Naming posture

The requested receipt lane is:

```text
data/receipts/settlement/
```

Current repository evidence shows the singular `settlement` segment already appears in `data/proofs/settlement/` and `packages/domains/settlement/`. Broader domain doctrine and many lifecycle lanes use `settlements-infrastructure` for the combined settlements and infrastructure domain.

This README therefore treats `data/receipts/settlement/` as a settlement-sublane receipt lane under the broader Settlements/Infrastructure domain. It does not decide the final canonical naming relationship between `settlement` and `settlements-infrastructure`. That relationship remains **NEEDS VERIFICATION** until accepted directory governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/settlement/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Requested lane | settlement |
| Broader domain | settlements-infrastructure |
| Scope | Settlement-sublane process memory across intake, validation, redaction, aggregation, review, correction, rollback, and release-support steps |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No direct public path; no normal UI; no governed-public API exposure |
| Related proof lane | `data/proofs/settlement/` |
| Related package lane | `packages/domains/settlement/` |
| Broader lifecycle payload authority | `data/raw/settlements-infrastructure/`, `data/work/settlements-infrastructure/`, `data/quarantine/settlements-infrastructure/`, `data/processed/settlements-infrastructure/`, not this lane |
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

No child receipt README lanes were confirmed under `data/receipts/settlement/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `redaction/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `aggregation/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `review/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `release/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |

This confirms only current README/path evidence. It does **not** prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

---

## Boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed processes did; it is not the truth source. |
| Singular settlement is not a new authority by itself | This path is treated as a sublane/compatibility lane until naming governance confirms otherwise. |
| Source roles stay explicit | Legal/administrative, aggregate, historical/context, observed, candidate, and synthetic roles must not collapse. |
| Identity remains evidence-bound | Place labels, aliases, boundaries, legal status, census status, and historic interpretation must remain distinct where evidence requires it. |
| Time facets stay distinct | Source, observed, valid, retrieval, release, and correction times stay separate where material. |
| Cross-lane ownership stays intact | Roads/Rail, Hydrology, Hazards, People/Land, Archaeology/Cultural Heritage, and Infrastructure boundaries remain separate. |
| Sensitive joins fail closed | Living-person, parcel/ownership, cultural, archaeology, reservation-community, and infrastructure-adjacent joins require policy and review support before use. |
| Policy remains separate | Binding sensitivity, rights, source-role, publication, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | ReviewRecord and release authority roles must remain visible and must not collapse into this receipt parent. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to settlement-sublane receipt instances and receipt-local sidecars:

- RunReceipt, TransformReceipt, RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision reference, ReviewRecord reference, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, transform refs, aggregation refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, signing sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, place truth, municipal-status authority, census truth, ownership truth, infrastructure authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw settlement or Settlements/Infrastructure source payloads | `data/raw/settlements-infrastructure/` or accepted restricted source storage |
| Work/candidate outputs | `data/work/settlements-infrastructure/` |
| Quarantined material | `data/quarantine/settlements-infrastructure/` |
| Processed settlement or infrastructure payloads | `data/processed/settlements-infrastructure/` |
| EvidenceBundle, ProofPack, CatalogMatrix, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, signature, or release changelog | `release/` |
| Sensitivity, rights, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Package helpers or executable code | `packages/`, `pipelines/`, and approved tool roots |
| Tests, fixtures, package code, or CI workflows | `tests/`, `fixtures/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, generated answer text, legal-status certification, or planning/emergency instructions | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/settlement/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, release authority, place authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the settlement sublane and a documented receipt subtype.
- [ ] Confirm canonical settlement / settlements-infrastructure naming against accepted directory governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, policy refs, reviewer refs, source refs, object refs, input/output hashes, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, place identity basis, time facets, public geometry posture, review state, caveats, and limitations are preserved where material.
- [ ] Confirm sensitive joins and restricted details are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where public-safe derivative, cultural/steward review, infrastructure-adjacent context, or release-candidate handoff is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public settlement claim path.
- [ ] Confirm receipt presence is not treated as place truth, legal-status authority, census truth, historic-townsite truth, infrastructure authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when policy, review, rights, sensitivity, evidence, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, generated answer, released layer, legal-status certification, or emergency/planning instruction uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/settlement/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Singular `settlement` appears as an existing proof lane at `data/proofs/settlement/`. | **CONFIRMED by GitHub contents API during this edit** |
| Singular `settlement` appears as an existing package lane at `packages/domains/settlement/`. | **CONFIRMED by GitHub contents API during this edit** |
| Broader domain doctrine uses `settlements-infrastructure` for the combined settlements and infrastructure lane. | **CONFIRMED by GitHub contents API during this edit** |
| The final canonical relationship between `settlement` and `settlements-infrastructure` receipt paths is settled. | **NEEDS VERIFICATION** |
| No child receipt README lanes under `data/receipts/settlement/` were confirmed during this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Settlements/Infrastructure doctrine says source role, evidence, time, sensitivity, release state, and cross-lane ownership must remain explicit. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| Actual Settlement receipt payloads exist under this subtree. | **UNKNOWN** |
| Emitted receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is place truth, legal-status authority, census truth, historic-townsite truth, infrastructure authority, property/ownership authority, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../proofs/settlement/README.md`](../../proofs/settlement/README.md)
- [`../../raw/settlements-infrastructure/README.md`](../../raw/settlements-infrastructure/README.md)
- [`../../quarantine/settlements-infrastructure/README.md`](../../quarantine/settlements-infrastructure/README.md)
- [`../../processed/settlements-infrastructure/README.md`](../../processed/settlements-infrastructure/README.md)
- [`../../catalog/domain/settlements-infrastructure/README.md`](../../catalog/domain/settlements-infrastructure/README.md)
- [`../../published/layers/settlements-infrastructure/README.md`](../../published/layers/settlements-infrastructure/README.md)
- [`../../../packages/domains/settlement/README.md`](../../../packages/domains/settlement/README.md)
- [`../../../packages/domains/settlements-infrastructure/README.md`](../../../packages/domains/settlements-infrastructure/README.md)
- [`../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md`](../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md)
- [`../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md`](../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md)
- [`../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md)
- [`../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md`](../../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/settlements.md`](../../../docs/domains/settlements-infrastructure/sublanes/settlements.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/settlement/` is a settlement-sublane receipt parent lane for process memory only. It is not place truth, legal-status authority, census truth, historic-townsite truth, infrastructure authority, property/ownership authority, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
