<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/archaeology/readme
name: Archaeology Receipts README
path: data/receipts/archaeology/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <archaeology-domain-steward>
  - <data-steward>
  - <validation-steward>
  - <sensitivity-reviewer>
  - <cultural-review-liaison>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: archaeology-receipts
receipt_scope: archaeology-domain-process-memory
path_posture: domain-receipt-parent-lane; child-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; exact-location-deny-default; cultural-review-required; fail-closed-validation; release-blocked
related:
  - raw/README.md
  - review/README.md
  - sensitivity/README.md
  - validation/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/archaeology/README.md
  - ../../quarantine/archaeology/README.md
  - ../../processed/archaeology/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/archaeology/README.md
  - ../../published/layers/archaeology/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../docs/domains/archaeology/PIPELINE.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - archaeology
  - process-memory
  - raw-stage
  - review-record
  - redaction-receipt
  - validation-report
  - cultural-review
  - sensitivity
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/archaeology/README.md`."
  - "Confirmed child receipt README lanes during this edit: `raw/`, `review/`, `sensitivity/`, and `validation/`."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, policy enforcement, consent/revocation enforcement, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Receipts

Domain parent receipt lane for Archaeology process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/archaeology/` is for Archaeology receipt process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is the Archaeology-domain parent lane for receipts that document governed process memory: RAW-stage intake/capture, review, sensitivity/redaction, validation, correction support, rollback support, and release-support context.

Archaeology receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, review, sensitivity, consent, revocation, hash, signature, correction, or rollback references should travel downstream, and what conditions block use.

Receipts do **not** decide cultural substance, prove site or artifact truth, authorize publication, replace a named authority, or replace EvidenceBundle, ProofPack, CatalogMatrix, PolicyDecision, ReleaseManifest, correction path, rollback target, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This domain parent lane is:

```text
data/receipts/archaeology/
```

The child lanes `raw/`, `review/`, `sensitivity/`, and `validation/` are confirmed as substantive README files in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/archaeology/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | archaeology |
| Scope | Archaeology process memory across RAW, review, sensitivity, validation, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/archaeology/`, `data/work/archaeology/`, `data/processed/archaeology/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Validator implementation authority | `tools/validators/`, not this lane |
| Default failure posture | `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when source role, rights, sensitivity, cultural review, sovereignty label, consent, revocation, validation, evidence refs, policy refs, digest, signature, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, policy enforcement, consent/revocation enforcement, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`raw/`](raw/README.md) | **CONFIRMED README** | RAW-stage process memory for source admission, source capture, preliminary validation, sensitivity triage, quarantine routing, correction support, and rollback support. | Not site truth, source truth, proof, catalog, policy, release, or public artifact authority. |
| [`review/`](review/README.md) | **CONFIRMED README** | Review process memory for cultural, steward, rights, sensitivity, consent/revocation, sovereignty-label, and release-readiness review. | Not cultural authority, site truth, proof, policy, release approval, or public artifact authority. |
| [`sensitivity/`](sensitivity/README.md) | **CONFIRMED README** | Sensitivity process memory for redaction, generalization, suppression, consent, revocation, embargo, sovereignty-label, and public-safe-transform support. | Not sensitivity policy, proof, release approval, site truth, or public artifact authority. |
| [`validation/`](validation/README.md) | **CONFIRMED README** | Validation process memory and `ValidationReport` receipts for finite outcomes, reason codes, spec hashes, policy parity, replay, and gate support. | Not validator implementation authority, site truth, proof, catalog closure, or release approval. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Archaeology processes did; it is not the truth source. |
| Sensitive context fails closed | Receipts and indexes must not expose restricted location, cultural, collection-security, private-owner, consent-token, revocation-token, or exact pre-redaction detail. |
| Named authority is not replaced | Where cultural/community authority applies, KFM records and defers; it does not substitute its own interpretation. |
| Validation receipts are not validators | Validator implementations, fixtures, and CI workflows live outside this receipt lane. |
| Sensitivity receipts are not policy | Sensitivity and redaction rules live in policy/contracts; receipts record process outputs. |
| Review receipts are not release decisions | Review receipts can support release decisions; release authority remains in `release/`. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Archaeology receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- RAW-stage, review, sensitivity/redaction, validation, correction-support, rollback-support, and release-support receipt records;
- `ReviewRecord`, `CulturalReview`, `StewardReview`, `RedactionReceipt`, `ValidationReport`, consent/revocation, sovereignty-label, suppression, generalization, cache-invalidation-support, and related process-memory records where applicable;
- run IDs, subject refs, source refs, input refs, input/output hashes, evidence refs, policy refs, review refs, profile IDs, validator IDs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, site-truth, cultural authority, validator implementation authority, or generated-answer authority.

Do not put restricted location details, cultural-knowledge substance, private-owner details, collection-security details, consent tokens, revocation tokens, exact pre-transform geometry, or culturally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Archaeology source payloads, packets, exact coordinates, or restricted source detail | `data/raw/archaeology/` or governed restricted storage as applicable |
| Normalized work or processed objects | `data/work/archaeology/` and `data/processed/archaeology/` |
| Validator implementation code | `tools/validators/` |
| Validation fixtures, expected-output pairs, and replay fixtures | `fixtures/` and `tests/` |
| Receipt schemas, validator schemas, or semantic contracts | `schemas/` and `contracts/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Sensitivity, redaction, sovereignty, consent, revocation, embargo, validation, or release policy | `policy/` and governed policy roots |
| Site truth, artifact truth, cultural authority, public interpretation, or generated answer text | governed downstream/proof/release lanes only after evidence and policy checks |

---

## Directory map

```text
data/receipts/archaeology/
├── README.md
├── raw/
│   └── README.md
├── review/
│   └── README.md
├── sensitivity/
│   └── README.md
├── validation/
│   └── README.md
└── index.local.json
```

This map confirms the README child lanes currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, policy enforcement, consent/revocation enforcement, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, site-truth index, cultural-review authority, sensitivity-policy authority, validator registry, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, signatures, review state, policy state, validation state, consent/revocation state, or decision scope are incomplete. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, violates role separation or policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/review/validation/sensitivity support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/archaeology/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Archaeology receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Archaeology domain and a documented child receipt lane.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, subject/source refs, input/output hashes, evidence refs, policy refs, review refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm receipt text does not expose restricted location, cultural, collection-security, private-owner, consent, revocation, or exact pre-transform detail.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public claim path.
- [ ] Confirm receipt presence is not treated as site truth, artifact truth, cultural authority, sovereignty authority, validator implementation, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/error/needs-review/quarantine states are recorded when rights, sensitivity, cultural review, sovereignty, consent, citation, precision, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/archaeology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lanes during this edit: `raw/`, `review/`, `sensitivity/`, and `validation/`. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology receipt child README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, policy enforcement, consent/revocation enforcement, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/archaeology/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Archaeology receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is site truth, artifact truth, cultural authority, sovereignty authority, consent authority, validator implementation authority, sensitivity policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`raw/README.md`](raw/README.md)
- [`review/README.md`](review/README.md)
- [`sensitivity/README.md`](sensitivity/README.md)
- [`validation/README.md`](validation/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/archaeology/README.md`](../../raw/archaeology/README.md)
- [`../../quarantine/archaeology/README.md`](../../quarantine/archaeology/README.md)
- [`../../processed/archaeology/README.md`](../../processed/archaeology/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/archaeology/README.md`](../../catalog/domain/archaeology/README.md)
- [`../../published/layers/archaeology/README.md`](../../published/layers/archaeology/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/archaeology/CULTURAL_REVIEW.md`](../../../docs/domains/archaeology/CULTURAL_REVIEW.md)
- [`../../../docs/domains/archaeology/SENSITIVITY.md`](../../../docs/domains/archaeology/SENSITIVITY.md)
- [`../../../docs/domains/archaeology/VALIDATORS.md`](../../../docs/domains/archaeology/VALIDATORS.md)
- [`../../../docs/domains/archaeology/PIPELINE.md`](../../../docs/domains/archaeology/PIPELINE.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/archaeology/` is an Archaeology receipt parent lane for process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, validator implementation authority, sensitivity policy authority, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
