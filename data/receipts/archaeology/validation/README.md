<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/archaeology/validation/readme
name: Archaeology Validation Receipts README
path: data/receipts/archaeology/validation/README.md
type: data-receipts-domain-validation-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <archaeology-domain-steward>
  - <validation-steward>
  - <ci-owner>
  - <sensitivity-reviewer>
  - <data-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: archaeology-validation-receipts
receipt_scope: archaeology-validation-process-memory
path_posture: proposed-by-archaeology-validator-doctrine; parent-archaeology-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; fail-closed-validation; exact-location-deny-default; release-blocked
related:
  - ../README.md
  - ../raw/README.md
  - ../review/README.md
  - ../sensitivity/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../raw/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/archaeology/README.md
  - ../../../published/layers/archaeology/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../../docs/domains/archaeology/PIPELINE.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - archaeology
  - validation
  - validation-report
  - validator
  - fail-closed
  - finite-outcome
  - evidencebundle
  - candidate-not-site
  - public-no-leak
  - catalog-closure
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/archaeology/validation/README.md`."
  - "Parent `data/receipts/archaeology/README.md` is currently a greenfield stub."
  - "Archaeology validator doctrine says every validator invocation emits a ValidationReport and missing receipts mean the validator did not run in the governed sense."
  - "Archaeology validator doctrine lists `data/receipts/archaeology/validation/` as the proposed persistence path for ValidationReport receipts."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted ValidationReport payloads, schemas, validators, fixtures, CI checks, signing, policy parity, replay harnesses, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Validation Receipts

Receipt lane for Archaeology validation process-memory records and `ValidationReport` artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Lane: validation" src="https://img.shields.io/badge/lane-validation-7048e8">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail--closed-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Validation receipt boundary](#validation-receipt-boundary) · [Validator families](#validator-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/archaeology/validation/` is for Archaeology validation receipt process memory only. It is not site truth, artifact truth, candidate confirmation, proof, EvidenceBundle authority, catalog authority, source registry authority, validator implementation authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipts and receipt-local sidecars that document Archaeology validation activity: validator invocation, input and output digests, finite outcomes, reason codes, policy-bundle digest, spec hash, fixture context, CI/runtime parity context, replay context, signatures, and gate decisions that downstream proof or release governance may inspect.

Validation receipts record that a validation process ran and what outcome it produced. They do **not** prove an archaeology claim by themselves, do not make a candidate a confirmed site, do not authorize release, and do not replace EvidenceBundle, ProofPack, CatalogMatrix, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target.

---

## Path posture

The Archaeology validator doctrine names this path as the proposed persistence lane for `ValidationReport` receipts:

```text
data/receipts/archaeology/validation/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/archaeology/README.md` is still a greenfield stub, and exact domain/validation receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/archaeology/validation/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | archaeology |
| Validation scope | validator invocation, finite outcomes, reason codes, spec hash, policy parity, replay, and gate support |
| Path posture | proposed by archaeology validator doctrine; exact subtype layout needs verification |
| Parent root | `data/receipts/archaeology/` |
| Sibling lanes | `data/receipts/archaeology/raw/`, `data/receipts/archaeology/review/`, `data/receipts/archaeology/sensitivity/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Validator implementation authority | `tools/validators/`, not this lane |
| Fixture/test authority | `fixtures/` and `tests/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when validator identity, input digest, output digest, policy bundle, spec hash, finite outcome, reason code, fixture context, review state, proof ref, correction path, rollback target, or release state is insufficient |

---

## Validation receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records validator behavior, not source truth, site truth, artifact truth, or release approval. |
| Missing receipt fails closed | If a required `ValidationReport` is absent, the validator did not run in the governed sense. |
| Outcomes are finite | Receipts should preserve the validator outcome and reason code rather than free-text-only conclusions. |
| Policy parity is recorded | CI and runtime decisions should reference the same policy bundle digest where applicable. |
| Replay context travels | Spec hash, input digests, output digests, and replay/golden-hash context must remain inspectable. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, correction notices, rollback cards, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |
| Restricted detail stays out of README/index text | Do not expose restricted location, cultural, collection-security, private-owner, consent-token, revocation-token, or exact pre-redaction detail in public-readable summaries. |

---

## Validator families

The exact validator implementation state is not proven by this README. The Archaeology validator doctrine names the following validation families for the lane:

| Validator family | Purpose | Boundary |
|---|---|---|
| EvidenceBundle-required | Checks that a claim, layer, drawer payload, API answer, or AI answer resolves to citable current evidence. | Passing does not replace proof-side EvidenceBundle closure. |
| Candidate-not-site | Prevents candidate features, remote-sensing anomalies, LiDAR candidates, or geophysics observations from being treated as confirmed sites. | Passing does not confirm a site. |
| Public no-leak | Checks public carriers for exact-location or side-channel leakage across map, label, export, 3D, URL, or AI surfaces. | Passing one carrier is not enough if another carrier leaks. |
| Rights and cultural-review | Checks rights, cultural review, sovereignty, and review-state requirements. | Validation does not replace reviewer authority or policy. |
| Exact sensitive geometry denial | Checks that protected/sensitive exact geometry is denied or transformed as required. | Validation does not make exact detail public. |
| Catalog closure | Checks catalog/provenance closure before publication support. | Catalog entries remain carriers and must dereference evidence. |
| AI exact-location denial | Checks that AI surfaces do not disclose denied precision or upcast restricted/candidate material. | AI receipts remain process memory, not truth. |

---

## Accepted material

Accepted content is limited to Archaeology validation receipt instances and receipt-local sidecars:

- `ValidationReport` JSON or JSONL records;
- validator invocation receipts for evidence, candidate-not-site, public-no-leak, rights/cultural review, exact sensitive geometry denial, catalog closure, AI exact-location denial, and cross-domain validation support;
- run IDs, validator IDs, validator versions, validator-class names, source refs, input refs, input hashes, output hashes, spec hashes, policy-bundle digests, finite outcomes, reason codes, details, started/finished timestamps, actor/runner identity, and status fields;
- companion citation-validation refs, review refs, sensitivity refs, policy-decision refs, correction refs, rollback refs, and release-candidate refs;
- receipt manifests, checksums, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect validation receipt state without becoming proof, catalog, policy, release, public output, site-truth, validator implementation, or generated-answer authority.

Do not put restricted location details, cultural-knowledge substance, private-owner details, collection-security details, consent tokens, revocation tokens, exact pre-transform geometry, or culturally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Archaeology source payloads, packets, exact coordinates, or restricted source detail | `data/raw/archaeology/` or governed restricted storage as applicable |
| Validator implementation code | `tools/validators/` |
| Validation fixtures, expected-output pairs, and replay fixtures | `fixtures/` and `tests/` |
| Validator semantic contracts or schemas | `contracts/` and `schemas/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Sensitivity, redaction, sovereignty, consent, revocation, embargo, or release policy | `policy/` and governed policy roots |
| Review authority and review decision records | Review receipt lanes and governed review records, not this lane alone |
| Site truth, artifact truth, cultural authority, public interpretation, or generated answer text | governed downstream/proof/release lanes only after evidence and policy checks |

---

## Directory map

```text
data/receipts/archaeology/validation/
├── README.md
├── <run_id>/
│   ├── validation_report.json
│   ├── policy_bundle_digest.txt
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
├── evidence/
│   └── <run_id>/
│       └── README.md
├── public-no-leak/
│   └── <run_id>/
│       └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, validator implementations, schemas, fixtures, CI checks, signing, policy parity, replay harnesses, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, site-truth index, validator registry, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Validation receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Validator ID, version, input digest, output digest, spec hash, policy bundle digest, finite outcome, reason code, or signature support is incomplete. |
| Quarantine/correct | Receipt contradicts inputs, omits required details, violates policy parity, lacks replay support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as validation support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/archaeology/validation/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. A validation receipt can support proof and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Archaeology domain and validation receipt lane.
- [ ] Confirm canonical domain/validation receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final authority.
- [ ] Confirm validator ID, validator version, run ID, input hashes, output hashes, spec hash, policy-bundle digest, finite outcome, reason code, timestamps, actor/runner identity, and status fields are present where applicable.
- [ ] Confirm every required validator invocation emitted a `ValidationReport`; missing receipts hold or fail closed.
- [ ] Confirm policy parity: CI and runtime use the same policy bundle digest where applicable.
- [ ] Confirm replay/golden-hash context is present before using the receipt in a promotion path.
- [ ] Confirm receipt text does not expose restricted location, cultural, collection-security, private-owner, consent, revocation, or exact pre-transform detail.
- [ ] Confirm EvidenceBundle/proof references resolve before using this receipt in any public claim path.
- [ ] Confirm receipt presence is not treated as validator implementation, policy authority, cultural authority, site truth, artifact truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/error/needs-review states are recorded when evidence, rights, sensitivity, cultural review, sovereignty, citation, precision, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/archaeology/validation/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/archaeology/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology validator doctrine says every invocation emits a `ValidationReport`; missing receipt means the validator did not run in the governed sense. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology validator doctrine lists `data/receipts/archaeology/validation/` as the proposed persistence path for `ValidationReport` receipts. | **CONFIRMED by GitHub contents API during this edit / PROPOSED path status** |
| Archaeology validator doctrine lists seven canonical validator families and finite outcomes. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology RAW-stage, review, and sensitivity receipt sibling lanes have substantive README documentation. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard places receipts under `data/receipts/` and defines fail-closed verification before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/archaeology/validation/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Archaeology validation receipt payloads exist under this subtree. | **UNKNOWN** |
| Validator implementations, schemas, fixtures, CI checks, signing, policy parity, replay harnesses, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is site truth, artifact truth, validator implementation authority, cultural authority, policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../raw/README.md`](../raw/README.md)
- [`../review/README.md`](../review/README.md)
- [`../sensitivity/README.md`](../sensitivity/README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/archaeology/README.md`](../../../raw/archaeology/README.md)
- [`../../../quarantine/archaeology/README.md`](../../../quarantine/archaeology/README.md)
- [`../../../processed/archaeology/README.md`](../../../processed/archaeology/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/archaeology/README.md`](../../../catalog/domain/archaeology/README.md)
- [`../../../published/layers/archaeology/README.md`](../../../published/layers/archaeology/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/archaeology/VALIDATORS.md`](../../../../docs/domains/archaeology/VALIDATORS.md)
- [`../../../../docs/domains/archaeology/PIPELINE.md`](../../../../docs/domains/archaeology/PIPELINE.md)
- [`../../../../docs/domains/archaeology/SENSITIVITY.md`](../../../../docs/domains/archaeology/SENSITIVITY.md)
- [`../../../../docs/domains/archaeology/CULTURAL_REVIEW.md`](../../../../docs/domains/archaeology/CULTURAL_REVIEW.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/archaeology/validation/` is an Archaeology validation receipt lane for process memory only. It is not site truth, artifact truth, validator implementation authority, cultural authority, policy authority, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
