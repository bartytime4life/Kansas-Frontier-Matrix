<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/archaeology/raw/readme
name: Archaeology RAW Receipts README
path: data/receipts/archaeology/raw/README.md
type: data-receipts-domain-stage-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <data-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: archaeology-raw-receipts
receipt_scope: archaeology-raw-stage-process-memory
path_posture: requested-domain-stage-receipt-lane; parent-archaeology-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; exact-location-deny-default; cultural-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/archaeology/README.md
  - ../../../published/layers/archaeology/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - archaeology
  - raw
  - raw-stage
  - ingest-receipt
  - validation-receipt
  - redaction-receipt
  - cultural-review
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/archaeology/raw/README.md`."
  - "Parent `data/receipts/archaeology/README.md` is currently a greenfield stub."
  - "Archaeology RAW doctrine says RAW is immutable source capture and is not truth, proof, receipt authority, release authority, public output, or generated-answer authority."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology RAW Receipts

Receipt lane for Archaeology RAW-stage process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Stage: RAW" src="https://img.shields.io/badge/stage-RAW-orange">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Receipt boundary](#receipt-boundary) · [Archaeology RAW boundaries](#archaeology-raw-boundaries) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/archaeology/raw/` is for Archaeology RAW-stage receipt process memory only. It is not Archaeology truth, site truth, artifact truth, cultural-review authority, sovereignty authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts that document Archaeology RAW-stage activity: source admission, source-head capture, intake checks, hash/digest recording, preliminary validation, sensitivity triage, cultural-review routing, redaction/generalization decisions tied to RAW intake, quarantine routing, correction support, and rollback-support context.

Receipts document what a governed process did. They can record run identity, source references, input digests, review state, policy outcome, sensitivity posture, affected outputs, correction references, and rollback targets. They do **not** prove the underlying source is true, do not approve public use, and do not replace EvidenceBundle, ProofPack, catalog closure, cultural review, or release governance.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested lane is scoped by domain and lifecycle stage:

```text
data/receipts/archaeology/raw/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/archaeology/README.md` is still a greenfield stub, and exact domain/stage receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/archaeology/raw/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | archaeology |
| Stage scope | RAW-stage process memory |
| Path posture | requested domain/stage receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/archaeology/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lane | `data/raw/archaeology/` |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, sensitivity, cultural review, sovereignty label, consent, geometry precision, citation, digest, validation, correction path, rollback target, or release state is insufficient |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records RAW-stage process behavior, not site truth or source truth. |
| RAW payloads stay elsewhere | Source material and source references belong in `data/raw/archaeology/`, not in receipt files. |
| Sensitive context fails closed | Receipts may point to restricted review state, but they must not expose restricted location or cultural details in README/index text. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Archaeology RAW boundaries

| RAW-stage condition | Receipt handling | Boundary |
|---|---|---|
| Source admission | Record source ID/ref, admission result, rights/sensitivity posture, and run ID. | Admission receipt is not SourceDescriptor authority by itself. |
| Source capture | Record payload refs, hashes, source-head state, retrieval/admission time, and caveats. | Receipt does not store or publish the source payload. |
| Preliminary validation | Record validator outcome and reason codes. | Passing validation is not proof or release approval. |
| Sensitivity triage | Record policy decision refs, review state, and redaction/generalization routing. | Exact protected or culturally restricted detail remains denied unless governance says otherwise. |
| Quarantine routing | Record quarantine reason and required remediation. | Quarantine is not rejection or publication. |
| Correction / rollback support | Record supersession, correction, or rollback references where applicable. | Authority remains in proof/release governance. |

---

## Accepted material

Accepted content is limited to Archaeology RAW-stage receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records for Archaeology RAW intake/capture processes;
- ingest, source-admission, validation, redaction, quarantine-routing, review-routing, correction-support, and rollback-support receipt records;
- run IDs, source refs, input refs, input digests, output refs, policy-decision refs, review-state refs, quarantine refs, correction refs, rollback refs, timestamps, actor/runner identity, and status fields;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, site-truth, cultural-review, or generated-answer authority.

Do not put restricted location details, cultural-knowledge text, private-owner details, collection-security details, consent tokens, or revocation tokens into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Archaeology source payloads, source packets, coordinates, or restricted source detail | `data/raw/archaeology/` or governed restricted storage as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Rights, sensitivity, cultural review, sovereignty, consent, redaction, or release policy | `policy/` and governed review lanes |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Site truth, artifact truth, cultural authority, public interpretation, or generated answer text | governed downstream/proof/release lanes only after evidence and policy checks |

---

## Directory map

```text
data/receipts/archaeology/raw/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── validation_receipt.json
│   ├── redaction_receipt.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, cultural-review workflows, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, site-truth index, cultural-review index, sovereignty authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream review. |
| Hold | Source role, rights, sensitivity, review state, input digest, method identity, or citation support is incomplete. |
| Quarantine/correct | Receipt contradicts source refs, omits required limits, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as process support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/archaeology/raw/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A RAW-stage receipt can support review, proof, and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Archaeology domain and RAW-stage receipt lane.
- [ ] Confirm canonical domain/stage receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, source refs, input refs, input digests, policy refs, review refs, timestamps, actor/runner identity, and status fields are present where applicable.
- [ ] Confirm receipt text does not expose restricted location, cultural, collection-security, private-owner, consent, or revocation detail.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public claim path.
- [ ] Confirm receipt presence is not treated as site truth, artifact truth, cultural-review approval, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm hold/quarantine/deny/abstain states are recorded when rights, sensitivity, cultural review, sovereignty, consent, citation, precision, or release state blocks use.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/archaeology/raw/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/archaeology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology RAW README says RAW is immutable source capture and not truth, proof, receipt authority, release authority, public output, or generated-answer authority. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology RAW README says exact site coordinates and culturally sensitive/looting-risk material fail closed until appropriate review and policy records exist. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard places receipts under `data/receipts/` and defines fail-closed verification before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/archaeology/raw/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Archaeology RAW-stage receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, cultural-review workflows, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is site truth, artifact truth, cultural-review authority, sovereignty authority, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/archaeology/README.md`](../../../raw/archaeology/README.md)
- [`../../../quarantine/archaeology/README.md`](../../../quarantine/archaeology/README.md)
- [`../../../processed/archaeology/README.md`](../../../processed/archaeology/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/archaeology/README.md`](../../../catalog/domain/archaeology/README.md)
- [`../../../published/layers/archaeology/README.md`](../../../published/layers/archaeology/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/archaeology/raw/` is an Archaeology RAW-stage receipt lane for process memory only. It is not site truth, artifact truth, cultural-review authority, sovereignty authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
