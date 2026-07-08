<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-release-readme
title: tools/validators/release README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-release-steward-plus-promotion-steward-plus-policy-steward-plus-evidence-steward-plus-correction-steward-plus-rollback-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; release-validator-index; release-manifest-aware; promotion-decision-aware; rollback-aware; correction-aware; withdrawal-aware; signed-release-aware; evidence-bound; policy-bound; fail-closed; non-authoritative
owning_root: tools/
responsibility: parent release validator routing README under tools/validators; documents release validation expectations for ReleaseManifest readiness, PromotionDecision linkage, rollback-card support, correction and withdrawal posture, release artifact reference integrity, evidence/proof/receipt linkage, policy/review posture, lifecycle boundary preservation, post-release supersession and rollback propagation, public-surface denial, schema/fixture/test routing, and finite outcomes while deferring release object meaning, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, release tooling helpers, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../promotion_gate/README.md
  - ../lifecycle/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../../release/README.md
  - ../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../contracts/release/README.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/rollback_card.md
  - ../../../contracts/release/withdrawal_notice.md
  - ../../../contracts/correction/correction_notice.md
  - ../../../schemas/contracts/v1/release/
  - ../../../schemas/contracts/v1/correction/
  - ../../../policy/release/
  - ../../../policy/promotion/
  - ../../../release/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/catalog/
  - ../../../data/triplets/
  - ../../../data/published/
  - ../../../fixtures/release/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/release/README.md. It does not confirm executable release validators, registry wiring, release storage, policy bundles, receipt emission, or CI behavior."
  - "Release validators check release-governance readiness. They do not store release records, approve release, publish artifacts, write ReleaseManifests, write PromotionDecisions, execute rollback, or authorize public surfaces."
  - "ReleaseManifest is the release-facing trust spine for published KFM artifacts, but it is not sovereign truth, not policy approval, not proof closure by itself, and not an artifact store."
  - "PromotionDecision is a governed transition decision, not a file move, release manifest, or public-surface permission by itself."
  - "tools/release/ is release-support tooling; tools/validators/release/ is validation routing. Both remain subordinate to release/ for release governance records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/release

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-release--validator--index-informational)
![authority](https://img.shields.io/badge/authority-validator--not--release--root-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/release/` is the release validator routing index for checking ReleaseManifest readiness, PromotionDecision linkage, rollback/correction/withdrawal posture, evidence/proof/receipt support, policy/review posture, artifact-reference integrity, public-surface denial, and post-release reversibility without becoming the `release/` governance root.

---

## Purpose

`tools/validators/release/` exists to organize release-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a release candidate or released artifact family have the ReleaseManifest, PromotionDecision, evidence, proof, receipt, policy, review, rights, sensitivity, attestation, rollback, correction, withdrawal, supersession, lifecycle, and public-surface support required before it can be treated as a governed KFM release or remain active as one?

The answer should be a deterministic validation result or routing decision. This folder should not create release records, write ReleaseManifests, write PromotionDecisions, issue rollback cards, issue correction or withdrawal notices, create EvidenceBundles, write receipts, decide policy, approve release, publish artifacts, move files, authorize public API/UI/map/AI access, or convert generated language into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/release/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `contracts/release/release_manifest.md` | **CONFIRMED contract / schema maturity mixed** | Defines ReleaseManifest as governed release binding; current schema is described as thin/permissive and detailed fields remain proposed until hardened. |
| `contracts/release/README.md` | **CONFIRMED contract-family README / mixed maturity** | Release contracts define semantic meaning only; release artifact/process authority belongs to `release/`. |
| `tools/release/README.md` | **CONFIRMED tooling README / executable behavior NEEDS VERIFICATION** | Release-support helpers may prepare dry-run reports and review scaffolds; they do not approve release. |
| `docs/architecture/publication/RELEASE_GATES.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Defines release gates at `CATALOG / TRIPLET -> PUBLISHED` and public-trust membrane constraints. |
| `tools/validators/promotion_gate/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Specialized promotion-gate validator route; release validation is broader and includes manifest, correction, rollback, withdrawal, and post-release posture. |
| Executable release validator scripts, registry wiring, schema bindings, policy bundles, release storage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/release/` is a **validator routing lane**, not the release authority root.

| Responsibility | Preferred home | Validator relationship |
|---|---|---|
| Release validation adapters | `tools/validators/release/` | Check release-readiness and active-release posture; emit deterministic findings. |
| Promotion-gate validation | `tools/validators/promotion_gate/` | Specialized pre-publication gate for transition packets. |
| Release-support tooling | `tools/release/` | Dry-run helpers, manifest inspectors, rollback/correction scaffold helpers, and review summaries. |
| Release semantic contracts | `contracts/release/` and correction contract homes | Contracts explain object meaning; validators check conformance. |
| Release/correction machine schemas | `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/` | Schemas define object shape; validators check schema bindings. |
| Release and promotion policy | `policy/release/`, `policy/promotion/`, accepted policy homes | Validators reference accepted policy bundle ids/digests; they do not decide policy. |
| Release records and process outputs | `release/` | Release authority, manifests, promotion decisions, correction, withdrawal, rollback, signatures, and changelogs live here. |
| Evidence and proof support | `data/proofs/` and accepted evidence/proof homes | Validators check EvidenceRef/EvidenceBundle/proof closure; they do not create evidence authority. |
| Receipts | `data/receipts/` | Validators may emit receipt-ready metadata only to accepted destinations. |
| Lifecycle data and public artifacts | `data/catalog/`, `data/triplets/`, `data/published/`, accepted lifecycle roots | Validators do not move or publish files. |
| Fixtures and tests | `fixtures/release/`, `tests/`, accepted fixture/test homes | Synthetic examples and tests prove behavior; they are not release authority. |

Validators may fail closed when required release support is absent, stale, contradictory, unsupported, unresolved, or withdrawn. They must not silently substitute file location, generated text, UI state, tile presence, catalog presence, schema validity, signature validity, fixture success, or a merged PR for release approval.

[Back to top](#top)

---

## Release validation packet

A release candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Release identity | Release id, domain/lane, artifact family, version/spec lineage, digests, and stable release refs. | Public truth by naming convention. |
| ReleaseManifest | Manifest reference or candidate shape with artifact set, digest/spec lineage, rights, sensitivity, evidence, policy, review, attestation, rollback, correction, and supersession context. | Proof closure, policy approval, or artifact store by itself. |
| PromotionDecision | Reviewed `APPROVE`, `DENY`, or `ABSTAIN` transition decision where required. | ReleaseManifest or public-surface permission by itself. |
| Artifact references | PMTiles, COG, GeoParquet, layer manifests, map manifests, exports, screenshots, API bundles, or other release payload references with digests. | Artifact existence as release approval. |
| Evidence/proof support | EvidenceRefs, EvidenceBundle refs, proof packs, validation reports, and citation-validation refs required for release-visible claims. | Generated text or catalog metadata as proof. |
| Policy/review support | Policy bundle id/version/digest, finite policy decision, obligations, rights/sensitivity posture, reviewer/ticket binding, and separation-of-duties posture. | Validator pass as policy approval. |
| Receipts/attestations | RunReceipt, validation receipt, publication receipt, signature, attestation, or equivalent support where required. | Receipt presence as truth or release approval. |
| Rollback support | RollbackCard, rollback target, prior release, previous alias, and reversal path. | Rollback execution. |
| Correction/withdrawal posture | CorrectionNotice, WithdrawalNotice, supersession, stale-state, retirement, and reevaluation posture. | One-time permanent publication. |
| Public-surface controls | Public API/UI/map/tile/export/screenshot/graph/Focus Mode/AI surfaces are denied until release-supported and public-safe. | Direct public access to internal stores. |

[Back to top](#top)

---

## Release invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Release is governed | Release has explicit manifest, promotion/policy/review support, evidence/proof support, receipt/attestation support, and rollback/correction support. | File move, deployed artifact, generated map tile, or generated AI answer is treated as release. |
| Manifest is not sovereign truth | ReleaseManifest binds artifacts and refs; it does not replace EvidenceBundle, policy, proofs, receipts, or release records. | Manifest validity is treated as proof closure or policy approval. |
| Promotion remains separate | PromotionDecision records transition decision; ReleaseManifest records release binding. | PromotionDecision and ReleaseManifest are collapsed. |
| Rollback is ready | Rollback target and previous release state are explicit and resolvable. | Release cannot be reversed, superseded, or corrected. |
| Correction and withdrawal are first-class | Correction, withdrawal, supersession, stale-state, and reevaluation paths remain visible. | Released artifact remains active after a blocking change. |
| Policy is explicit | Release policy bundle, rights, sensitivity, obligations, and review state are visible. | Policy is missing, stale, unsupported, or inferred from file placement. |
| Evidence closes release-visible claims | EvidenceRef and EvidenceBundle/proof refs resolve for claims and artifacts. | Evidence is missing, unresolved, stale, contradicted, withdrawn, or insufficient. |
| Public surfaces use released derivatives | Public clients consume only released/public-safe artifacts through governed interfaces. | Public surface reaches RAW, WORK, QUARANTINE, unpublished candidates, internal stores, or direct model output. |
| Downstream carriers stay subordinate | Maps, tiles, exports, graphs, screenshots, Focus Mode, and AI outputs cite released artifacts and evidence posture. | Downstream carrier becomes sovereign truth. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Release validator routing | `tools/validators/release/` |
| Promotion-gate validation | `tools/validators/promotion_gate/` |
| Lifecycle validation | `tools/validators/lifecycle/` |
| Evidence validation | `tools/validators/evidence/` and accepted evidence validator lanes |
| Policy validation | `tools/validators/policy/` |
| Map/tile/public-surface validation | `tools/validators/maplibre/`, `tools/validators/pmtiles/`, accepted public-surface validator lanes |
| Release-support tooling | `tools/release/` |
| Release semantic contracts | `contracts/release/` and correction contract homes |
| Release/correction schemas | `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/` |
| Release/promotion policy | `policy/release/`, `policy/promotion/`, accepted policy roots |
| Release records and process outputs | `release/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data and artifacts | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Fixtures | `fixtures/release/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared release-readiness and active-release invariants and delegates policy, evidence, schemas, contracts, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, ReleaseManifest schemas, PromotionDecision schemas, RollbackCard schemas, CorrectionNotice and WithdrawalNotice schemas, policy bundle homes, policy bundle digests, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as release authority, release record store, ReleaseManifest store, PromotionDecision store, rollback-card store, correction/withdrawal record store, policy home, evidence store, proof store, receipt store, lifecycle data store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/release/` include:

- this README;
- small validation adapters that check release manifests, release packets, correction posture, withdrawal posture, rollback readiness, and active-release consistency;
- checks for ReleaseManifest readiness, PromotionDecision linkage, EvidenceBundle closure, policy bundle identity, review binding, artifact digest integrity, receipts/attestations, rollback readiness, correction/withdrawal posture, lifecycle boundary, and public-surface denial;
- routing notes for promotion-gate validators, lifecycle validators, policy validators, evidence validators, PMTiles/MapLibre validators, and domain-specific release validators;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of release/proof/receipt authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Actual ReleaseManifest records, PromotionDecision records, RollbackCards, correction notices, withdrawal notices, signatures, release changelogs | `release/` or accepted release record homes |
| Release object semantic contracts | `contracts/release/`, correction contract homes |
| Release/correction schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/release/`, `schemas/contracts/v1/correction/`, or accepted schema homes |
| Policy rules, promotion policy, release policy, steward approval rules, thresholds | `policy/promotion/`, `policy/release/`, accepted policy homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| Release-support helper scripts unrelated to validation | `tools/release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `RELEASE_VALIDATOR_PASS` | Candidate passed configured release checks. |
| `RELEASE_VALIDATOR_FAIL` | Candidate failed one or more configured release checks. |
| `RELEASE_VALIDATOR_DENY` | Candidate must not be released or remain active because evidence, policy, review, release, rollback, correction, rights, sensitivity, integrity, or public-surface support cannot be resolved. |
| `RELEASE_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `RELEASE_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a release assertion. |
| `RELEASE_MANIFEST_MISSING` | Required ReleaseManifest or release-manifest-ready packet is absent. |
| `RELEASE_MANIFEST_INVALID` | ReleaseManifest-like record fails accepted schema/contract checks. |
| `RELEASE_MANIFEST_OVERCLAIM` | ReleaseManifest is treated as proof closure, policy approval, artifact store, or public permission by itself. |
| `PROMOTION_DECISION_MISSING` | Required PromotionDecision or transition-decision reference is absent. |
| `PROMOTION_DECISION_INVALID` | PromotionDecision-like record fails accepted schema/contract checks. |
| `ARTIFACT_DIGEST_MISSING` | Required artifact digest, spec hash, signature, or attestation reference is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `VALIDATION_REPORT_MISSING` | Required validation report or validator outcome is absent. |
| `POLICY_BUNDLE_REF_MISSING` | Required policy bundle id, version, digest, or decision support is absent. |
| `REVIEW_BINDING_MISSING` | Required reviewer/ticket/steward binding is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Required rollback card, prior release, or rollback target is absent. |
| `CORRECTION_CASCADE_MISSING` | Correction, withdrawal, supersession, stale state, rights change, or rollback did not propagate. |
| `WITHDRAWAL_NOTICE_MISSING` | Required withdrawal notice or retirement posture is absent. |
| `STALE_OR_SUPERSEDED_RELEASE_DENIED` | Release candidate or published artifact is stale, superseded, withdrawn, revoked, rollback-mismatched, or correction-pending. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/release/
├── README.md
├── validate_release_manifest.py         # PROPOSED; path named by contract, not confirmed
├── validate_release_packet.py           # PROPOSED; not confirmed
├── validate_rollback_readiness.py       # PROPOSED; not confirmed
├── validate_correction_withdrawal.py    # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, local schema files, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/release/README.md`.
- [x] It marks this path as release validator routing, not release authority, release storage, policy authority, evidence authority, proof/receipt storage, lifecycle data, public runtime, or AI authority.
- [x] It distinguishes `tools/validators/release/` from `tools/release/` and `release/`.
- [x] It distinguishes ReleaseManifest from PromotionDecision, PolicyDecision, proof closure, artifact storage, file movement, deployment, tile generation, generated AI text, and public-surface permission.
- [x] It routes release objects to `contracts/`, schemas to `schemas/`, policy to `policy/`, release records to `release/`, evidence/proofs/receipts to `data/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, schema files, fixtures, policy bundles, receipts, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to release validators are searched and classified.
- [ ] ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, and WithdrawalNotice schema homes are verified.
- [ ] Release/promotion policy bundle homes, accepted bundle ids, versions, and digest rules are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, abstain, stale, superseded, rollback-missing, correction-missing, withdrawal-missing, evidence-missing, and public-surface-blocked cases.
- [ ] CI invokes release validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with release validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
