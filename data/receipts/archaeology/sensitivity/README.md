<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/archaeology/sensitivity/readme
name: Archaeology Sensitivity Receipts README
path: data/receipts/archaeology/sensitivity/README.md
type: data-receipts-domain-sensitivity-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <archaeology-domain-steward>
  - <sensitivity-reviewer>
  - <cultural-review-liaison>
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
artifact_family: archaeology-sensitivity-receipts
receipt_scope: archaeology-sensitivity-process-memory
path_posture: requested-domain-sensitivity-receipt-lane; parent-archaeology-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; exact-location-deny-default; redaction-receipt-required; consent-revocation-fail-closed; release-blocked
related:
  - ../README.md
  - ../raw/README.md
  - ../review/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/archaeology/README.md
  - ../../../published/layers/archaeology/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../contracts/domains/archaeology/sensitivity_transform.md
  - ../../../../contracts/domains/archaeology/publication_transform_receipt.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - archaeology
  - sensitivity
  - redaction-receipt
  - sensitivity-transform
  - generalization
  - suppression
  - consent
  - revocation
  - sovereignty-label
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/archaeology/sensitivity/README.md`."
  - "Parent `data/receipts/archaeology/README.md` is currently a greenfield stub."
  - "Archaeology sensitivity doctrine says the lane is deny-by-default at every gate and every public-safe transformation must emit a RedactionReceipt against a named, versioned redaction profile."
  - "Archaeology review receipts and RAW-stage receipts are siblings; this lane records sensitivity/redaction/generalization process memory only."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted sensitivity receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, consent/revocation enforcement, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Sensitivity Receipts

Receipt lane for Archaeology sensitivity, redaction, generalization, suppression, consent, revocation, and public-safe-transform process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Lane: sensitivity" src="https://img.shields.io/badge/lane-sensitivity-critical">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not policy" src="https://img.shields.io/badge/boundary-not%20policy-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Sensitivity receipt boundary](#sensitivity-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/archaeology/sensitivity/` is for Archaeology sensitivity receipt process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, proof, EvidenceBundle authority, catalog authority, source registry authority, sensitivity policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document sensitivity process memory for the Archaeology domain: sensitivity-tier evaluation, redaction profile application, geometry generalization, suppression/withholding, consent and revocation checks, embargo checks, sovereignty-label inheritance, public-safe transform checks, and cache-invalidation support for revocation or correction.

Sensitivity receipts record what sensitivity decision or transformation happened, what named profile or policy reference was used, which input/output hashes apply, which fields were kept or removed, which review or consent references were required, and which downstream proof/release artifacts may inspect the receipt.

Sensitivity receipts do **not** define sensitivity policy, prove site or artifact truth, grant publication, approve release, or replace ReviewRecord, PolicyDecision, EvidenceBundle, ProofPack, ReleaseManifest, correction path, or rollback target.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested lane is scoped by domain and sensitivity function:

```text
data/receipts/archaeology/sensitivity/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/archaeology/README.md` is still a greenfield stub, and exact domain/sensitivity receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/archaeology/sensitivity/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | archaeology |
| Sensitivity scope | redaction, generalization, suppression, consent, revocation, embargo, sovereignty-label, and public-safe-transform process memory |
| Path posture | requested domain/sensitivity receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/archaeology/` |
| Sibling lanes | `data/receipts/archaeology/raw/`, `data/receipts/archaeology/review/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `DENY`, `HOLD`, `ABSTAIN`, or `QUARANTINE` when sensitivity tier, rank, redaction profile, review state, consent state, revocation endpoint, embargo state, sovereignty label, input/output hash, proof refs, correction path, rollback target, or release state is insufficient |

---

## Sensitivity receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records sensitivity transform behavior, not site truth, artifact truth, or policy authority. |
| Policy remains separate | Sensitivity rules, named profiles, consent rules, sovereignty rules, and release rules belong in `policy/` and governed policy roots. |
| Exact detail fails closed | Receipt text and public-readable indexes must not expose restricted location, cultural, collection-security, private-owner, consent-token, or revocation-token detail. |
| Redaction receipts are required support | A public-safe transform without a resolvable receipt did not happen in the governed sense. |
| Review remains separate | ReviewRecord, cultural review, rights review, and sensitivity review support belongs in review lanes and review records. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

| Receipt family | Purpose | Boundary |
|---|---|---|
| `RedactionReceipt` | Records named profile, method, input hash, output hash, kept/removed fields, geometry transform, reviewer refs, consent refs, care/sovereignty labels, and replay data. | It supports a transform; it does not prove source truth or authorize release by itself. |
| Sensitivity transform receipt | Records tier/rank evaluation, sensitivity decision, and transform selection. | It does not replace policy bundles or reviewer decisions. |
| Suppression / withholding receipt | Records that no public carrier was produced or that fields were removed. | Suppression is not deletion; correction/revocation rules still apply where needed. |
| Generalization receipt | Records grid, aggregate, or coarsening transform and deterministic replay context. | Generalization does not guarantee public safety without review and release gates. |
| Consent / revocation receipt refs | Records consent-state and revocation-state checks used by the transform. | Consent remains revocable and must fail closed where required. |
| Embargo / cache-invalidation receipt refs | Records embargo state and derivative/cache invalidation actions. | Cache invalidation support is not release authority. |
| Sovereignty-label receipt refs | Records inherited labels or signed waivers where applicable. | Labeling does not transfer cultural authority to KFM. |

---

## Accepted material

Accepted content is limited to Archaeology sensitivity receipt instances and receipt-local sidecars:

- sensitivity receipt JSON or JSONL records;
- `RedactionReceipt`, sensitivity transform, suppression, withholding, generalization, consent-check, revocation-check, embargo-check, cache-invalidation-support, sovereignty-label, correction-support, rollback-support, and release-support receipt records;
- run IDs, subject refs, source refs, evidence refs, policy refs, profile IDs, input hashes, output hashes, kept/removed field summaries, reviewer refs, consent refs, revocation refs, embargo refs, correction refs, rollback refs, timestamps, actor/runner identity, and status fields;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect sensitivity receipt state without becoming proof, catalog, policy, release, public output, site-truth, cultural authority, or generated-answer authority.

Do not put restricted location details, cultural-knowledge substance, private-owner details, collection-security details, consent tokens, revocation tokens, exact pre-transform geometry, or culturally restricted text into this README or public-facing local indexes.

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
| Sensitivity, redaction, sovereignty, consent, revocation, embargo, or release policy | `policy/` and governed policy roots |
| Review authority and review decision records | Review receipt lanes and governed review records, not this lane alone |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Site truth, artifact truth, cultural authority, public interpretation, or generated answer text | governed downstream/proof/release lanes only after evidence and policy checks |

---

## Directory map

```text
data/receipts/archaeology/sensitivity/
├── README.md
├── <receipt_id>/
│   ├── redaction_receipt.json
│   ├── policy_decision_ref.json
│   ├── review_record_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── redaction/
│   └── <receipt_id>/
│       └── README.md
├── suppression/
│   └── <receipt_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, consent/revocation enforcement, cache-invalidation hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, site-truth index, sensitivity-policy authority, sovereignty authority, consent authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Sensitivity receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Profile ID, policy ref, input/output hash, reviewer refs, consent/revocation state, embargo state, or decision scope is incomplete. |
| Quarantine/correct | Receipt contradicts evidence, lacks a named versioned profile, omits required limits, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as sensitivity-transform support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/archaeology/sensitivity/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A sensitivity receipt can support proof and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Archaeology domain and sensitivity receipt lane.
- [ ] Confirm canonical domain/sensitivity receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final authority.
- [ ] Confirm receipt ID, subject refs, evidence refs, policy refs, named profile ID/version, input hash, output hash, kept/removed field summary, reviewer refs, timestamps, actor/runner identity, and status fields are present where applicable.
- [ ] Confirm every public-safe transform has a named, versioned redaction profile and a replayable RedactionReceipt.
- [ ] Confirm receipt text does not expose restricted location, cultural, collection-security, private-owner, consent, revocation, or exact pre-transform detail.
- [ ] Confirm consent, revocation, embargo, sovereignty, rights, and review refs are present where required and fail closed when unresolved.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public claim path.
- [ ] Confirm receipt presence is not treated as policy authority, cultural authority, site truth, artifact truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/deny/abstain/quarantine states are recorded when rights, sensitivity, cultural review, sovereignty, consent, citation, precision, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/archaeology/sensitivity/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/archaeology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology sensitivity doctrine says the lane is deny-by-default at every gate and every public-safe transformation must emit a RedactionReceipt against a named, versioned redaction profile. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology sensitivity doctrine says consent is enforceable, machine-readable, and revocable, and revocation/cache invalidation fail closed. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology RAW-stage and review receipt sibling lanes have substantive README documentation. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard places receipts under `data/receipts/` and defines fail-closed verification before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/archaeology/sensitivity/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Archaeology sensitivity receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, policy enforcement, consent/revocation enforcement, cache-invalidation hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is site truth, artifact truth, cultural authority, sovereignty authority, consent authority, sensitivity policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../raw/README.md`](../raw/README.md)
- [`../review/README.md`](../review/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/archaeology/README.md`](../../../raw/archaeology/README.md)
- [`../../../quarantine/archaeology/README.md`](../../../quarantine/archaeology/README.md)
- [`../../../processed/archaeology/README.md`](../../../processed/archaeology/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/archaeology/README.md`](../../../catalog/domain/archaeology/README.md)
- [`../../../published/layers/archaeology/README.md`](../../../published/layers/archaeology/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/archaeology/SENSITIVITY.md`](../../../../docs/domains/archaeology/SENSITIVITY.md)
- [`../../../../docs/domains/archaeology/CULTURAL_REVIEW.md`](../../../../docs/domains/archaeology/CULTURAL_REVIEW.md)
- [`../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md`](../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md)
- [`../../../../contracts/domains/archaeology/sensitivity_transform.md`](../../../../contracts/domains/archaeology/sensitivity_transform.md)
- [`../../../../contracts/domains/archaeology/publication_transform_receipt.md`](../../../../contracts/domains/archaeology/publication_transform_receipt.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/archaeology/sensitivity/` is an Archaeology sensitivity receipt lane for process memory only. It is not site truth, artifact truth, cultural authority, sovereignty authority, consent authority, sensitivity policy authority, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
