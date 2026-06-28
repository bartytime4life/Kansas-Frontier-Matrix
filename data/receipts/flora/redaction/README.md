<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/flora/redaction/readme
name: Flora Redaction Receipts README
path: data/receipts/flora/redaction/README.md
type: data-receipts-domain-redaction-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <flora-domain-steward>
  - <sensitivity-reviewer>
  - <rights-holder-representative>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: flora-redaction-receipts
receipt_scope: flora-redaction-process-memory
domain: flora
path_posture: requested-domain-redaction-receipt-lane; parent-flora-receipt-root-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; deny-by-default; exact-location-deny-default; redaction-receipt-required; steward-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/flora/README.md
  - ../../../published/layers/flora/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/MAP_UI_CONTRACTS.md
  - ../../../../contracts/domains/flora/rare_plant_record.md
  - ../../../../contracts/domains/flora/flora_occurrence.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - flora
  - redaction
  - redaction-receipt
  - geoprivacy
  - rare-plant
  - sensitive-taxa
  - exact-location-deny
  - steward-review
  - policy-decision
  - review-record
  - correction-notice
  - rollback-card
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/flora/redaction/README.md`."
  - "Parent `data/receipts/flora/README.md` is currently a greenfield stub."
  - "Flora sensitivity doctrine says rare, protected, or culturally sensitive plant locations default to T4 and require generalized/withheld geometry plus RedactionReceipt and steward review before public-safe movement."
  - "Concrete redaction parameters, grid sizes, radii, fuzzing values, transform seeds, exact sensitive geometry, and private stewardship detail are deliberately excluded from this README."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted RedactionReceipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Redaction Receipts

Receipt lane for Flora geoprivacy and redaction process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: redaction" src="https://img.shields.io/badge/lane-redaction-critical">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Redaction receipt boundary](#redaction-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/flora/redaction/` is for Flora redaction receipt process memory only. It is not rare-plant truth, exact-location authority, sensitivity policy, rights authority, proof, EvidenceBundle authority, catalog authority, source registry authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document Flora redaction and geoprivacy activity: suppression, generalization, steward-only handling, delayed publication support, aggregation support, join-induced sensitivity handling, tier-transition support, review-state recording, correction support, rollback support, and release-candidate support.

Redaction receipts record what transform happened, which policy and review references governed it, what input/output hashes apply, which fields were kept or removed, and which downstream proof or release artifacts may inspect the receipt.

Redaction receipts do **not** define sensitivity policy, prove a rare plant occurrence, approve public release, make exact geometry public, or replace ReviewRecord, PolicyDecision, EvidenceBundle, ProofPack, ReleaseManifest, CorrectionNotice, or RollbackCard.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested Flora redaction lane is:

```text
data/receipts/flora/redaction/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/flora/README.md` is still a greenfield stub, and exact domain/redaction receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/flora/redaction/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | flora |
| Redaction scope | Geoprivacy, suppression, generalization, steward-only handling, delayed publication support, tier transition, correction, rollback, and release-support process memory |
| Path posture | requested domain/redaction receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/flora/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/sensitivity/flora/` and `policy/geoprivacy/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when tier, policy ref, reviewer, rights state, stewardship state, geometry precision, input/output hash, evidence refs, review state, correction path, rollback target, or release state is insufficient |

---

## Redaction receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records redaction behavior, not rare-plant truth, location truth, or release approval. |
| Deny by default | Rare, protected, culturally sensitive, steward-controlled, or join-sensitive plant records fail closed when sensitivity, rights, or review state is unresolved. |
| Exact geometry stays protected | Receipt README/index text must not expose exact rare-plant coordinates, identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, consent tokens, or revocation tokens. |
| Redaction is policy-driven | Redaction must cite a policy/profile reference and reviewer state; it must not be improvised at the UI/API edge. |
| Transform receipt is required | A public-safe transform without a resolvable RedactionReceipt did not happen in the governed sense. |
| Review remains separate | ReviewRecord, steward review, rights-holder review, sensitivity review, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This lane may hold or reference Flora redaction records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RedactionReceipt | Records policy ref, redaction method, kept/removed fields, geometry transform class, reviewer refs, input hash, output hash, and replay/correction support. | Does not prove source truth or authorize release by itself. |
| ReviewRecord reference | Records steward, sensitivity, rights, or release-readiness review state. | Review support is not ReleaseManifest authority. |
| PolicyDecision reference | Records finite policy decision state for tier, denial, withholding, or transformation. | Policy authority remains in policy roots. |
| AggregationReceipt reference | Records aggregation support where redaction is by count, density, range surface, or suppressed cell. | Aggregation does not replace redaction or proof closure. |
| CorrectionNotice / RollbackCard reference | Records correction or rollback support when a redacted public product must be demoted, withdrawn, invalidated, or regenerated. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to Flora redaction receipt instances and receipt-local sidecars:

- RedactionReceipt JSON or JSONL records;
- review, policy-decision, aggregation-support, suppression, withholding, delayed-publication, steward-only, correction-support, rollback-support, and release-support receipt references tied to redaction work;
- run IDs, subject refs, source refs, occurrence refs, rare-plant refs, input hashes, output hashes, policy refs, profile refs, transform-family refs, kept-field summaries, removed-field summaries, reviewer refs, evidence refs, validation refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect redaction receipt state without becoming proof, catalog, policy, release, public output, exact-location authority, rare-plant truth, or generated-answer authority.

Do not put exact rare-plant coordinates, protected or culturally sensitive plant locations, private landowner details, restricted identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, reviewer private notes, consent tokens, revocation tokens, tribal/CARE-restricted details, or culturally/legally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora occurrence/source payloads, exact sensitive coordinates, restricted identifiers, or source-native files | `data/raw/flora/` or governed restricted storage as applicable |
| Work/scratch redaction candidates and transform experiments | `data/work/flora/` |
| Quarantined or unresolved sensitive material | `data/quarantine/flora/` |
| Processed public-safe Flora objects or generalized layers | `data/processed/flora/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, redaction, rights, sovereignty, CARE, consent, revocation, or release policy | `policy/sensitivity/flora/`, `policy/geoprivacy/`, and governed policy roots |
| Redaction schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, species pages, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/flora/redaction/
├── README.md
├── <receipt_id>/
│   ├── redaction_receipt.json
│   ├── review_record_ref.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── suppression/
│   └── <receipt_id>/
│       └── README.md
├── generalization/
│   └── <receipt_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, exact-location authority, sensitivity-policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Redaction receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Profile/policy refs, reviewer refs, input/output hash, evidence refs, validation refs, or decision scope are incomplete. |
| Deny/abstain | Sensitivity, rights, review state, stewardship state, source role, geometry precision, or re-identification risk remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as redaction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/flora/redaction/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / species page / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Flora redaction receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and redaction receipt lane.
- [ ] Confirm canonical domain/redaction receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, subject refs, rare-plant refs, input/output hashes, policy refs, profile refs, reviewer refs, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm exact sensitive coordinates, identifiers, generalization radii, grid sizes, fuzzing parameters, transform seeds, consent tokens, revocation tokens, and restricted stewardship details are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where tier movement, rare/protected/culturally sensitive plant handling, steward-controlled records, rights restrictions, or public-safe derivatives are involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public Flora claim path.
- [ ] Confirm receipt presence is not treated as sensitivity policy, exact-location authority, rare-plant truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/quarantine states are recorded when sensitivity, rights, review, source role, re-identification risk, evidence, policy, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or map surface uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/flora/redaction/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/flora/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized or withheld geometry, and RedactionReceipt for public release. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says RedactionReceipt is required for every public-safe transform of sensitive Flora content. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says the transform vocabulary is proposed and exact thresholds/parameters live in `policy/sensitivity/flora/`, not this README. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/flora/redaction/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Flora redaction receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is rare-plant truth, exact-location authority, sensitivity policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/flora/README.md`](../../../raw/flora/README.md)
- [`../../../processed/flora/README.md`](../../../processed/flora/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/flora/README.md`](../../../catalog/domain/flora/README.md)
- [`../../../published/layers/flora/README.md`](../../../published/layers/flora/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/flora/SENSITIVITY.md`](../../../../docs/domains/flora/SENSITIVITY.md)
- [`../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md)
- [`../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../../docs/domains/flora/SOURCE_REGISTRY.md`](../../../../docs/domains/flora/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/flora/MAP_UI_CONTRACTS.md`](../../../../docs/domains/flora/MAP_UI_CONTRACTS.md)
- [`../../../../contracts/domains/flora/rare_plant_record.md`](../../../../contracts/domains/flora/rare_plant_record.md)
- [`../../../../contracts/domains/flora/flora_occurrence.md`](../../../../contracts/domains/flora/flora_occurrence.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/flora/redaction/` is a Flora redaction receipt lane for process memory only. It is not rare-plant truth, exact-location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
