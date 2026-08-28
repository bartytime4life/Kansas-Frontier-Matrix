<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/archaeology/review/readme
name: Archaeology Review Receipts README
path: data/receipts/archaeology/review/README.md
type: data-receipts-domain-review-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <archaeology-domain-steward>
  - <cultural-review-liaison>
  - <sensitivity-reviewer>
  - <rights-reviewer>
  - <data-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: archaeology-review-receipts
receipt_scope: archaeology-review-process-memory
path_posture: requested-domain-review-receipt-lane; parent-archaeology-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; community-authority-defers-to-named-authority; exact-location-deny-default; release-blocked
related:
  - ../README.md
  - ../raw/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/archaeology/README.md
  - ../../../published/layers/archaeology/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../contracts/domains/archaeology/cultural_review.md
  - ../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - archaeology
  - review
  - cultural-review
  - steward-review
  - review-record
  - consent-receipt
  - revocation-manifest
  - sovereignty-label
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/archaeology/review/README.md`."
  - "Parent `data/receipts/archaeology/README.md` is currently a greenfield stub."
  - "Archaeology cultural-review doctrine says KFM records who reviews, when, how recorded, and how revoked, but does not define the substance of cultural knowledge."
  - "Cultural review authority is community-conferred where applicable; KFM records and defers rather than substitutes its own interpretation."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted review receipt payloads, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, reviewer rosters, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Review Receipts

Receipt lane for Archaeology cultural, steward, rights, sensitivity, and release-review process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Lane: review" src="https://img.shields.io/badge/lane-review-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not authority" src="https://img.shields.io/badge/boundary-not%20authority-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Review boundary](#review-boundary) · [Review families](#review-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/archaeology/review/` is for Archaeology review receipt process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document review process memory for the Archaeology domain: cultural review, steward review, rights review, sensitivity review, release-readiness review, consent/revocation checks, sovereignty-label checks, and review-gated lifecycle transitions.

Review receipts record what review happened, who or what authority was recorded, what decision class was produced, what evidence or policy references were considered, what obligations were attached, what expiry or revocation path applies, and which downstream proof/release artifacts may reference the review state.

Review receipts do **not** decide the substance of cultural knowledge, do not prove site or artifact truth, do not grant publication by themselves, and do not replace the named authority, EvidenceBundle, ProofPack, policy decision, ReleaseManifest, correction path, or rollback target.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested lane is scoped by domain and review function:

```text
data/receipts/archaeology/review/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/archaeology/README.md` is still a greenfield stub, and exact domain/review receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/archaeology/review/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | archaeology |
| Review scope | cultural, steward, rights, sensitivity, consent, sovereignty, and release-review process memory |
| Path posture | requested domain/review receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/archaeology/` |
| Sibling stage lane | `data/receipts/archaeology/raw/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, or `QUARANTINE` when reviewer authority, role separation, rights, sensitivity, consent, sovereignty label, evidence refs, policy refs, expiry, revocation path, correction path, rollback target, or release state is insufficient |

---

## Review boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records review process behavior, not site truth, artifact truth, or cultural substance. |
| Named authority is not replaced | Where cultural or community authority applies, KFM records the named authority and defers; it does not substitute its own interpretation. |
| Review records are not release decisions | Review receipts can support a release decision, but release authority remains in `release/`. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Policy remains separate | Sensitivity, consent, sovereignty, redaction, and release rules belong in `policy/` and governed review lanes. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |
| Restricted substance stays out of README/index text | Do not expose restricted location, cultural knowledge, consent token, revocation token, or private-party detail in public-readable summaries. |

---

## Review families

| Review family | Purpose | Boundary |
|---|---|---|
| `ReviewRecord` | Cross-cutting review-decision record with reviewer, scope, decision, basis, expiry, revocation path, evidence refs, and policy refs. | It records a decision state; it does not become proof or release approval by itself. |
| `CulturalReview` | Community/cultural-authority review record where cultural, Indigenous, sacred, burial, oral-history, or community-controlled material is involved. | Cultural authority is community-conferred, not KFM-conferred. |
| `StewardReview` | Archaeology domain-steward review of interpretation, source-role posture, evidence sufficiency, and candidate/confirmed status. | Steward review does not replace cultural review, rights review, sensitivity review, proof, or release. |
| Rights-holder review | Review of source rights, use terms, redistribution, attribution, and restricted joins. | Rights approval does not approve cultural sensitivity or release by itself. |
| Sensitivity review | Review of access tier, public-safe transform, generalization, redaction, and exact-location denial. | Sensitivity review does not prove site truth or grant release by itself. |
| Consent / revocation receipt | Records consent grant, waiver, restriction, revocation, or live fail-closed state. | Consent state must remain checkable and revocable where applicable. |
| Sovereignty label decision | Records sovereignty label inheritance or waiver state where applicable. | Labeling does not transfer cultural authority to KFM. |
| Release-readiness review | Records review support for release candidacy. | Release decision remains in `release/` and must cite proof and rollback support. |

---

## Accepted material

Accepted content is limited to Archaeology review receipt instances and receipt-local sidecars:

- review receipt JSON or JSONL records;
- `ReviewRecord`, `CulturalReview`, `StewardReview`, rights-review, sensitivity-review, consent, revocation, sovereignty-label, waiver, correction-support, rollback-support, and release-readiness receipt records;
- run IDs, subject refs, evidence refs, policy refs, reviewer refs, authority-basis refs, decision states, obligations, expiry state, revocation refs, correction refs, rollback refs, timestamps, actor/runner identity, and status fields;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect review receipt state without becoming proof, catalog, policy, release, public output, site-truth, cultural authority, or generated-answer authority.

Do not put restricted location details, cultural-knowledge substance, private-owner details, collection-security details, consent tokens, revocation tokens, or culturally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Archaeology source payloads, packets, exact coordinates, or restricted source detail | `data/raw/archaeology/` or governed restricted storage as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Sensitivity, cultural review, sovereignty, consent, redaction, or release policy | `policy/` and governed policy roots |
| Review schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Cultural-knowledge substance, site truth, artifact truth, public interpretation, or generated answer text | Named authority and governed downstream/proof/release lanes only after evidence and policy checks |

---

## Directory map

```text
data/receipts/archaeology/review/
├── README.md
├── <review_id>/
│   ├── review_record.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── cultural/
│   └── <review_id>/
│       └── README.md
├── steward/
│   └── <review_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, reviewer rosters, cultural-review workflows, consent/revocation enforcement, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, site-truth index, cultural-review authority, sovereignty authority, consent authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Review receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Reviewer authority, separation of duties, evidence refs, policy refs, consent state, expiry, revocation path, or decision scope is incomplete. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, violates role separation, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as process/review support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/archaeology/review/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A review receipt can support proof and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Archaeology domain and review receipt lane.
- [ ] Confirm canonical domain/review receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final authority.
- [ ] Confirm receipt ID, subject refs, evidence refs, policy refs, reviewer refs, authority-basis refs, decision state, obligations, expiry, revocation path, timestamps, actor/runner identity, and status fields are present where applicable.
- [ ] Confirm role separation: author, domain steward, cultural reviewer, rights reviewer, sensitivity reviewer, and release authority are not collapsed where doctrine forbids it.
- [ ] Confirm cultural authority is recorded as named/community-conferred where applicable and is not replaced by KFM interpretation.
- [ ] Confirm receipt text does not expose restricted location, cultural, collection-security, private-owner, consent, or revocation detail.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public claim path.
- [ ] Confirm receipt presence is not treated as cultural authority, site truth, artifact truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/quarantine states are recorded when rights, sensitivity, cultural review, sovereignty, consent, citation, precision, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/archaeology/review/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/archaeology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology cultural-review doctrine says KFM records review governance but does not define the substance of cultural knowledge. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology cultural-review doctrine identifies reviewer roles, ReviewRecord-family objects, and separation-of-duties constraints. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard places receipts under `data/receipts/` and defines fail-closed verification before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/archaeology/review/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Archaeology review receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, reviewer rosters, consent/revocation enforcement, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is site truth, artifact truth, cultural authority, sovereignty authority, consent authority, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../raw/README.md`](../raw/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/archaeology/README.md`](../../../raw/archaeology/README.md)
- [`../../../quarantine/archaeology/README.md`](../../../quarantine/archaeology/README.md)
- [`../../../processed/archaeology/README.md`](../../../processed/archaeology/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/archaeology/README.md`](../../../catalog/domain/archaeology/README.md)
- [`../../../published/layers/archaeology/README.md`](../../../published/layers/archaeology/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/archaeology/CULTURAL_REVIEW.md`](../../../../docs/domains/archaeology/CULTURAL_REVIEW.md)
- [`../../../../docs/domains/archaeology/SENSITIVITY.md`](../../../../docs/domains/archaeology/SENSITIVITY.md)
- [`../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md`](../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md)
- [`../../../../contracts/domains/archaeology/cultural_review.md`](../../../../contracts/domains/archaeology/cultural_review.md)
- [`../../../../contracts/domains/archaeology/steward_review.md`](../../../../contracts/domains/archaeology/steward_review.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/archaeology/review/` is an Archaeology review receipt lane for process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
