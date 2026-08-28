<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/flora/readme
name: Flora Receipts README
path: data/receipts/flora/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <flora-domain-steward>
  - <sensitivity-reviewer>
  - <rights-holder-representative>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: flora-receipts
receipt_scope: flora-domain-process-memory
domain: flora
path_posture: domain-receipt-parent-lane; redaction-child-lane-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; deny-by-default; exact-location-deny-default; redaction-receipt-required; steward-review-required; release-blocked
related:
  - redaction/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/flora/README.md
  - ../../work/flora/README.md
  - ../../quarantine/flora/README.md
  - ../../processed/flora/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/flora/README.md
  - ../../published/layers/flora/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/MAP_UI_CONTRACTS.md
  - ../../../contracts/domains/flora/rare_plant_record.md
  - ../../../contracts/domains/flora/flora_occurrence.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - flora
  - process-memory
  - redaction
  - redaction-receipt
  - geoprivacy
  - rare-plant
  - sensitive-taxa
  - exact-location-deny
  - steward-review
  - policy-decision
  - review-record
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/flora/README.md`."
  - "Confirmed child receipt README lane during this edit: `redaction/`."
  - "Flora sensitivity doctrine says exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized or withheld geometry, and RedactionReceipt for public release."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Receipts

Domain parent receipt lane for Flora process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/flora/` is for Flora receipt process memory only. It is not rare-plant truth, exact-location authority, sensitivity policy, rights authority, proof, EvidenceBundle authority, catalog authority, source registry authority, release authority, public artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the Flora-domain parent lane for receipts that document governed process memory: source intake support, redaction/geoprivacy, steward review support, sensitivity review support, validation support, aggregation support, correction support, rollback support, and release-candidate support.

Flora receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, review, source-role, redaction, validation, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove rare plant occurrence, approve public release, expose exact geometry, define sensitivity policy, decide rights authority, or replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Flora domain parent lane is:

```text
data/receipts/flora/
```

The child lane `redaction/` is confirmed as a substantive README file in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | flora |
| Scope | Flora process memory across source intake support, redaction/geoprivacy, review, validation, aggregation, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/sensitivity/flora/` and `policy/geoprivacy/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when tier, policy ref, reviewer, rights state, stewardship state, source role, geometry precision, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`redaction/`](redaction/README.md) | **CONFIRMED README** | Flora geoprivacy and redaction process memory for suppression, generalization, steward-only handling, delayed publication support, aggregation support, join-induced sensitivity handling, tier-transition support, review-state recording, correction support, rollback support, and release-candidate support. | Not rare-plant truth, exact-location authority, sensitivity policy, proof, release approval, or public artifact authority. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Flora processes did; it is not the truth source. |
| Deny by default | Rare, protected, culturally sensitive, steward-controlled, or join-sensitive plant records fail closed when sensitivity, rights, review state, or stewardship state is unresolved. |
| Exact geometry stays protected | README/index text must not expose exact rare-plant coordinates, identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, consent tokens, revocation tokens, or restricted stewardship detail. |
| Policy remains separate | Binding sensitivity/geoprivacy rules live in `policy/sensitivity/flora/` and `policy/geoprivacy/`. |
| Review remains separate | ReviewRecord, steward review, rights-holder review, sensitivity review, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Flora receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, redaction/geoprivacy, steward review, sensitivity review, validation, aggregation-support, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `AggregationReceipt`, `ValidationReport`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, occurrence refs, rare-plant refs, input/output hashes, evidence refs, policy refs, profile refs, transform-family refs, reviewer refs, validation refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, exact-location authority, rare-plant truth, or generated-answer authority.

Do not put exact rare-plant coordinates, protected or culturally sensitive plant locations, private landowner details, restricted identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, reviewer private notes, consent tokens, revocation tokens, tribal/CARE-restricted details, or culturally/legally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora occurrence/source payloads, exact sensitive coordinates, restricted identifiers, or source-native files | `data/raw/flora/` or governed restricted storage as applicable |
| Work/scratch candidates and transform experiments | `data/work/flora/` |
| Quarantined or unresolved sensitive material | `data/quarantine/flora/` |
| Processed public-safe Flora objects or generalized layers | `data/processed/flora/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, redaction, rights, sovereignty, CARE, consent, revocation, or release policy | `policy/sensitivity/flora/`, `policy/geoprivacy/`, and governed policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, species pages, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/flora/
├── README.md
├── redaction/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, exact-location authority, sensitivity-policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, reviewer refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Sensitivity, rights, review state, stewardship state, source role, geometry precision, or re-identification risk remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/redaction/validation support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/flora/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / species page / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Flora receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and a documented child receipt lane.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, subject refs, rare-plant refs, input/output hashes, policy refs, profile refs, reviewer refs, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm exact sensitive coordinates, identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, consent tokens, revocation tokens, and restricted stewardship details are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where tier movement, rare/protected/culturally sensitive plant handling, steward-controlled records, rights restrictions, or public-safe derivatives are involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Flora claim path.
- [ ] Confirm receipt presence is not treated as sensitivity policy, exact-location authority, rare-plant truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/quarantine states are recorded when sensitivity, rights, review, source role, re-identification risk, evidence, policy, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or map surface uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/flora/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `redaction/`. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized or withheld geometry, and RedactionReceipt for public release. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says RedactionReceipt is required for every public-safe transform of sensitive Flora content. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says the transform vocabulary is proposed and exact thresholds/parameters live in `policy/sensitivity/flora/`, not this README. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Flora receipt child README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/flora/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Flora receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is rare-plant truth, exact-location authority, sensitivity policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`redaction/README.md`](redaction/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/flora/README.md`](../../raw/flora/README.md)
- [`../../work/flora/README.md`](../../work/flora/README.md)
- [`../../quarantine/flora/README.md`](../../quarantine/flora/README.md)
- [`../../processed/flora/README.md`](../../processed/flora/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/flora/README.md`](../../catalog/domain/flora/README.md)
- [`../../published/layers/flora/README.md`](../../published/layers/flora/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/flora/SENSITIVITY.md`](../../../docs/domains/flora/SENSITIVITY.md)
- [`../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md)
- [`../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../docs/domains/flora/SOURCE_REGISTRY.md`](../../../docs/domains/flora/SOURCE_REGISTRY.md)
- [`../../../docs/domains/flora/MAP_UI_CONTRACTS.md`](../../../docs/domains/flora/MAP_UI_CONTRACTS.md)
- [`../../../contracts/domains/flora/rare_plant_record.md`](../../../contracts/domains/flora/rare_plant_record.md)
- [`../../../contracts/domains/flora/flora_occurrence.md`](../../../contracts/domains/flora/flora_occurrence.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/flora/` is a Flora receipt parent lane for process memory only. It is not rare-plant truth, exact-location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
