<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-promotion-gate-readme
title: tools/validators/promotion_gate README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-promotion-steward-plus-release-steward-plus-policy-steward-plus-evidence-steward-plus-review-steward-plus-rollback-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; promotion-gate-validator-index; governed-state-transition; catalog-triplet-to-published; promotion-decision-aware; release-manifest-aware; evidence-bound; policy-bound; review-required; rollback-required; fail-closed; non-authoritative
owning_root: tools/
responsibility: parent promotion-gate validator routing README under tools/validators; documents promotion gate validation expectations for CATALOG/TRIPLET-to-PUBLISHED candidates, PromotionDecision readiness, ReleaseManifest relationship, EvidenceRef and EvidenceBundle closure, policy bundle linkage, review binding, rollback/correction/withdrawal readiness, lifecycle boundary preservation, public-surface denial, fixture/schema/test routing, and finite outcomes while deferring release object meaning, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../lifecycle/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../contracts/release/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/rollback_card.md
  - ../../../contracts/release/withdrawal_notice.md
  - ../../../schemas/contracts/v1/release/
  - ../../../policy/promotion/
  - ../../../policy/release/
  - ../../../release/
  - ../../../fixtures/release/promotion_decision/README.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/catalog/
  - ../../../data/triplets/
  - ../../../data/published/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/promotion_gate/README.md. It does not confirm executable promotion-gate validators, registry wiring, release storage, policy bundles, receipt emission, or CI behavior."
  - "Promotion is a governed state transition, not a file move, merged PR, deployed tile, copied artifact, generated AI answer, or public UI permission."
  - "PromotionDecision records a reviewed, evidence-bound, policy-bound decision about a candidate crossing a lifecycle boundary; it is not a ReleaseManifest, runtime PolicyDecision, file move, deployment shortcut, or public-surface permission by itself."
  - "Release gates sit at the CATALOG/TRIPLET to PUBLISHED boundary and are followed by correction and rollback discipline."
  - "Validators may check required promotion artifacts and references; they do not approve release, publish artifacts, write release records, create EvidenceBundles, decide policy, or authorize public surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/promotion_gate

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-promotion--gate--validator-informational)
![boundary](https://img.shields.io/badge/boundary-CATALOG%2FTRIPLET%E2%86%92PUBLISHED-blueviolet)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/promotion_gate/` is the promotion-gate validator routing lane for checking whether a release candidate has the evidence, policy, review, rollback, correction, withdrawal, lifecycle, and public-surface support required before any governed transition toward `PUBLISHED`.

---

## Purpose

`tools/validators/promotion_gate/` exists to organize promotion-gate validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a CATALOG/TRIPLET-to-PUBLISHED candidate have an auditable PromotionDecision-ready packet with EvidenceRef, EvidenceBundle closure, validation reports, policy bundle identity, review binding, release-manifest relationship, rollback target, correction/withdrawal posture, lifecycle boundary context, and public-surface limits before it may cross the trust membrane?

The answer should be a deterministic validation result or routing decision. This folder should not create lifecycle data, approve promotion, write PromotionDecision records, write ReleaseManifests, create EvidenceBundles, write receipts, decide policy, approve release, publish artifacts, move files, authorize public API/UI/map/AI access, or convert generated language into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/promotion_gate/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `contracts/release/promotion_decision.md` | **CONFIRMED contract / validator wiring NEEDS VERIFICATION** | Defines PromotionDecision as a reviewed, evidence-bound, policy-bound governed transition decision; not a file move, ReleaseManifest, or public-surface permission. |
| `docs/architecture/publication/RELEASE_GATES.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Defines release gates at `CATALOG / TRIPLET -> PUBLISHED` and states public surfaces must not reach RAW/WORK/QUARANTINE/internal stores. |
| `tools/validators/lifecycle/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Lifecycle validator index preserves state-transition posture and says promotion is not a storage operation or file move. |
| `contracts/release/README.md` | **CONFIRMED contract-family README / mixed maturity** | Release contracts define semantic meaning only; release artifact/process authority belongs to `release/`. |
| `fixtures/release/promotion_decision/README.md` | **CONFIRMED fixture README / payload behavior NEEDS VERIFICATION** | Synthetic fixtures are examples only and not actual promotion decisions, release manifests, evidence, policy, proof, receipt, or publication authority. |
| Executable promotion-gate scripts, registry wiring, schema bindings, policy bundles, release storage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/promotion_gate/` is a **validator routing lane**, not the promotion or release authority root.

| Responsibility | Preferred home | Validator relationship |
|---|---|---|
| Promotion-gate validation adapter | `tools/validators/promotion_gate/` | Checks gate readiness and emits deterministic findings. |
| Lifecycle-state validation | `tools/validators/lifecycle/` | Promotion gate is a specialized boundary check at `CATALOG/TRIPLET -> PUBLISHED`. |
| Release object semantic meaning | `contracts/release/` | Contracts explain object meaning; validators check conformance. |
| Release object machine shape | `schemas/contracts/v1/release/` | Schemas define object shape; validators check schema bindings. |
| Promotion/release policy | `policy/promotion/`, `policy/release/`, accepted policy homes | Validators reference accepted policy bundle ids/digests; they do not decide policy. |
| Evidence and proof support | `data/proofs/` and accepted evidence/proof homes | Validators check EvidenceRef/EvidenceBundle closure; they do not create evidence authority. |
| Receipts | `data/receipts/` | Validators may emit receipt-ready metadata only to accepted destinations. |
| Release records and publication state | `release/` | Release authority, manifests, correction, withdrawal, and rollback records live here. |
| Lifecycle data and public artifacts | `data/catalog/`, `data/triplets/`, `data/published/`, accepted lifecycle roots | Validators do not move or publish files. |
| Fixtures and tests | `fixtures/release/promotion_decision/`, `tests/`, accepted fixture/test homes | Synthetic examples and tests prove behavior; they are not release authority. |

Validators may fail closed when required promotion support is absent, stale, contradictory, unsupported, or unresolved. They must not silently substitute file location, generated text, UI state, tile presence, catalog presence, schema validity, or a merged PR for promotion approval.

[Back to top](#top)

---

## Promotion-gate packet

A promotion-gate candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, domain/lane, run id, artifact refs, content digests, spec hashes, version, and lifecycle boundary. | Promotion approval by naming convention. |
| Lifecycle state | Current state is `CATALOG` or `TRIPLET`; requested state is `PUBLISHED`; upstream states are closed. | File path as state proof. |
| Evidence support | EvidenceRef resolves to EvidenceBundle/proof support required for claims and artifacts. | Evidence truth without review/policy/release. |
| Validation support | ValidationReport or equivalent finite findings are present for schemas, contracts, sources, joins, policy, artifacts, and public surfaces where required. | Universal correctness proof. |
| Policy support | Policy bundle id/version/digest, PolicyDecision-like result, reasons, obligations, sensitivity posture, and review flags are present where required. | Policy authority inside validator code. |
| Review binding | Reviewer, ticket, steward role, separation-of-duties posture, and review timestamp are present where required. | Rubber-stamp or hidden approval. |
| PromotionDecision readiness | PromotionDecision shape can be produced or validated with finite `APPROVE`, `DENY`, or `ABSTAIN` transition vocabulary. | ReleaseManifest or runtime answer. |
| Release relationship | ReleaseManifest or release-reference relationship is explicit for the intended publication surface. | Public-surface permission by itself. |
| Rollback support | RollbackCard/rollback target is present and matches the candidate lineage. | Rollback execution. |
| Correction/withdrawal posture | Correction, supersession, withdrawal, stale-state, and reevaluation paths are explicit. | One-time permanent truth. |
| Public-surface controls | Public API/UI/map/tile/export/screenshot/graph/Focus Mode/AI surfaces are denied until release-supported and public-safe. | Direct renderer or AI permission. |

[Back to top](#top)

---

## Promotion-gate invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Promotion is governed | Candidate has explicit transition evidence, policy, review, release, correction, and rollback support. | File move, deployment, merge, tile generation, or generated text is treated as promotion. |
| Lifecycle boundary is correct | Gate applies to `CATALOG/TRIPLET -> PUBLISHED`, or a documented specialized promotion boundary. | Candidate bypasses RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET gates. |
| Evidence closes claims | EvidenceRef and EvidenceBundle refs resolve for release-significant claims and artifacts. | Evidence is missing, unresolved, stale, contradicted, withdrawn, or insufficient. |
| Policy is explicit | Policy bundle, version, digest, outcome, reasons, obligations, sensitivity, and review flags are present. | Policy is missing, stale, unsupported, unreviewed, or invented from context. |
| Review is accountable | Reviewer/ticket binding and separation-of-duties posture are visible where required. | Reviewer is missing, hidden, self-approving where prohibited, or not bound to a ticket. |
| Decision is finite | PromotionDecision vocabulary remains `APPROVE`, `DENY`, or `ABSTAIN` unless an accepted schema changes it. | Candidate emits ambiguous, non-finite, or runtime-answer vocabulary. |
| Rollback is ready | Rollback target, prior state, rollback card, and correction path are present. | Candidate cannot be reversed or corrected. |
| Public surface is denied until release | Public clients consume only released/public-safe artifacts through governed interfaces. | Public surface reaches internal stores or unpublished candidates. |
| Downstream carriers stay subordinate | Maps, tiles, exports, graphs, screenshots, Focus Mode, and AI outputs cite released artifacts and evidence posture. | Downstream carrier becomes sovereign truth. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Promotion-gate validator routing | `tools/validators/promotion_gate/` |
| Lifecycle transition validation | `tools/validators/lifecycle/` |
| Evidence validation | `tools/validators/evidence/` and accepted evidence validator lanes |
| Policy validation | `tools/validators/policy/` |
| Map/tile/public-surface validation | `tools/validators/maplibre/`, `tools/validators/pmtiles/`, accepted public-surface validator lanes |
| Release semantic contracts | `contracts/release/` |
| Release schemas | `schemas/contracts/v1/release/` |
| Promotion/release policy | `policy/promotion/`, `policy/release/`, accepted policy roots |
| Release records and process outputs | `release/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data and artifacts | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Fixtures | `fixtures/release/promotion_decision/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared promotion-gate readiness and delegates policy, evidence, schemas, contracts, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, PromotionDecision schemas, ReleaseManifest schemas, policy bundle homes, policy bundle digests, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as release authority, release record store, PromotionDecision store, ReleaseManifest store, rollback-card store, policy home, evidence store, proof store, receipt store, lifecycle data store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/promotion_gate/` include:

- this README;
- small validation adapters that check promotion-gate packets;
- checks for PromotionDecision readiness, EvidenceBundle closure, policy bundle identity, review binding, rollback readiness, correction/withdrawal posture, lifecycle boundary, and public-surface denial;
- routing notes for release-gate validators, lifecycle validators, policy validators, evidence validators, PMTiles/MapLibre validators, and domain-specific release validators;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of release/proof/receipt authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Actual PromotionDecision records, ReleaseManifests, RollbackCards, correction notices, withdrawal notices | `release/` or accepted release record homes |
| Release object semantic contracts | `contracts/release/` |
| Release schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/release/` or accepted schema homes |
| Policy rules, promotion policy, release policy, steward approval rules, thresholds | `policy/promotion/`, `policy/release/`, accepted policy homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PROMOTION_GATE_PASS` | Candidate passed configured promotion-gate checks. |
| `PROMOTION_GATE_FAIL` | Candidate failed one or more configured checks. |
| `PROMOTION_GATE_APPROVE_READY` | Candidate appears ready for an `APPROVE` PromotionDecision, pending actual release authority. |
| `PROMOTION_GATE_DENY` | Candidate must not promote because evidence, policy, review, release, rollback, correction, rights, sensitivity, or public-surface support cannot be resolved. |
| `PROMOTION_GATE_ABSTAIN` | Candidate lacks enough support for promotion decision. |
| `PROMOTION_DECISION_MISSING` | Required PromotionDecision or decision-ready packet is absent. |
| `PROMOTION_DECISION_INVALID` | PromotionDecision-like record fails accepted schema/contract checks. |
| `PROMOTION_DECISION_OVERCLAIM` | PromotionDecision is treated as file move, ReleaseManifest, or public permission by itself. |
| `LIFECYCLE_BOUNDARY_INVALID` | Candidate is not at an accepted promotion boundary or bypasses lifecycle gates. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `VALIDATION_REPORT_MISSING` | Required validation report or validator outcome is absent. |
| `POLICY_BUNDLE_REF_MISSING` | Required policy bundle id, version, digest, or decision support is absent. |
| `REVIEW_BINDING_MISSING` | Required reviewer/ticket/steward binding is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, release reference, correction path, withdrawal path, or rollback target is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Required rollback card or rollback target is absent. |
| `CORRECTION_CASCADE_MISSING` | Correction, withdrawal, supersession, stale state, rights change, or rollback did not propagate. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/promotion_gate/
├── README.md
├── validate_promotion_gate.py           # PROPOSED; not confirmed
├── validate_promotion_packet.py         # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, local schema files, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting promotion or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/promotion_gate/README.md`.
- [x] It marks this path as promotion-gate validator routing, not release authority, release storage, policy authority, evidence authority, proof/receipt storage, lifecycle data, public runtime, or AI authority.
- [x] It preserves the `CATALOG/TRIPLET -> PUBLISHED` release-gate boundary and the broader RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED lifecycle invariant.
- [x] It distinguishes PromotionDecision from ReleaseManifest, PolicyDecision, file movement, deployment, tile generation, generated AI text, and public-surface permission.
- [x] It routes release objects to `contracts/`, schemas to `schemas/`, policy to `policy/`, records to `release/`, evidence/proofs/receipts to `data/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, schema files, fixtures, policy bundles, receipts, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to promotion-gate validators are searched and classified.
- [ ] PromotionDecision, ReleaseManifest, RollbackCard, CorrectionNotice, and WithdrawalNotice schema homes are verified.
- [ ] Promotion/release policy bundle homes, accepted bundle ids, versions, and digest rules are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, abstain, rollback-missing, review-missing, evidence-missing, and public-surface-blocked cases.
- [ ] CI invokes promotion-gate validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with promotion-gate validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
