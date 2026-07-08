<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-lifecycle-readme
title: tools/validators/lifecycle README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-lifecycle-steward-plus-data-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward-plus-tooling-qa-owner
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; lifecycle-validator-index; state-transition-aware; quarantine-aware; catalog-aware; evidence-bound; release-gated; rollback-aware; non-authoritative
owning_root: tools/
responsibility: broad lifecycle validator routing index for checking governed lifecycle state transitions, RAW-to-WORK-or-QUARANTINE admission, WORK-to-PROCESSED transformation, PROCESSED-to-CATALOG-or-TRIPLET registration, CATALOG-or-TRIPLET-to-PUBLISHED promotion, quarantine exits, correction and withdrawal propagation, evidence/proof linkage, policy/review/release linkage, rollback support, and public-surface denial while deferring lifecycle data, schemas, policy decisions, proof records, receipts, catalog records, triplets, release decisions, and published artifacts to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog/README.md
  - ../evidence/README.md
  - ../joins/README.md
  - ../cross-domain-joins/README.md
  - ../identity/README.md
  - ../../../data/raw/
  - ../../../data/work/
  - ../../../data/quarantine/
  - ../../../data/processed/
  - ../../../data/catalog/
  - ../../../data/triplets/
  - ../../../data/published/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/registry/
  - ../../../release/
  - ../../../contracts/data/catalog_matrix.md
  - ../../../contracts/data/validation_report.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../tests/
  - ../../../fixtures/
notes:
  - "This README replaces an empty file at tools/validators/lifecycle/README.md. It does not confirm executable validator code."
  - "Lifecycle validation enforces state-transition posture. It does not move files, create lifecycle data, create EvidenceBundles, write receipts, decide policy, approve release, publish artifacts, or authorize public UI/API/AI use."
  - "Promotion is a governed state transition, not a storage operation or file move. A copied file, merged PR, deployed tile, or generated AI response is not promotion without the required decision, evidence, policy, review, rollback, and release artifacts."
  - "Catalog records are discovery/interchange carriers, not truth, proof, receipts, release decisions, or publication by themselves."
  - "Evidence validators check readiness and closure, but EvidenceBundle support is still not a PolicyDecision or ReleaseManifest."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/lifecycle

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-lifecycle--validator--index-informational)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-blueviolet)
![release](https://img.shields.io/badge/release-governed--transition-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/lifecycle/` is the validator routing index for checking KFM lifecycle state transitions without becoming lifecycle data storage, catalog truth, proof storage, receipt storage, policy authority, release authority, or publication machinery.

---

## Purpose

`tools/validators/lifecycle/` exists to organize lifecycle-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a candidate preserve the governed lifecycle path, required evidence support, source-role posture, policy/review state, validation reports, catalog/triplet registration, release decision, correction path, rollback target, and public-surface limits before it moves from RAW to WORK or QUARANTINE, from WORK to PROCESSED, from PROCESSED to CATALOG/TRIPLET, or from CATALOG/TRIPLET to PUBLISHED?

The answer should be a deterministic validation result or routing decision. This folder should not create lifecycle data, approve movement, write catalog records, generate triplets, create EvidenceBundles, write receipts, decide policy, approve release, publish artifacts, authorize public API/UI/map/AI access, or convert generated text into truth.

[Back to top](#top)

---

## Lifecycle invariant

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This path is a trust membrane, not a set of convenience folders. A lifecycle validator should detect bypasses, missing transition artifacts, stale or contradicted support, unresolved quarantine exits, missing correction cascades, absent rollback targets, and public exposure before release.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/lifecycle/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Catalog validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/catalog/README.md` treats catalog records as discovery/interchange carriers, not proof, receipts, release decisions, or publication by themselves. |
| Evidence validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/evidence/README.md` checks EvidenceRef resolution and EvidenceBundle closure while denying proof storage, receipt storage, policy decisions, and release approval in validator code. |
| Promotion decision contract | **CONFIRMED contract / validator wiring NEEDS VERIFICATION** | `PromotionDecision` is an auditable decision record for governed transitions and is not a storage operation. |
| Executables, registry wiring, schema bindings, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, release integration, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable lifecycle validator, test suite, receipt path, runtime route, release gate, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby validator lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Lifecycle state-transition validation | `tools/validators/lifecycle/` | This parent README and possible future validator adapters. |
| Catalog readiness and catalog boundary checks | `tools/validators/catalog/` | Catalog is discovery/interchange, not truth, proof, receipt, release, or publication. |
| EvidenceRef and EvidenceBundle closure checks | `tools/validators/evidence/` | Evidence validators check readiness; they do not create proof or release authority. |
| Join lifecycle checks | `tools/validators/joins/`, `tools/validators/cross-domain-joins/` | Joined derivatives must preserve lifecycle and most-restrictive posture. |
| Identity and spec-hash checks | `tools/validators/identity/` | Lifecycle records may need deterministic identity, hash, and public-safe ID checks. |
| Shared validator plumbing | `tools/validators/_common/` | Common runner/helper code if accepted. |
| Source descriptors | `data/registry/`, `data/registry/sources/`, and accepted source registry homes | Source-role and source-rights authority stay outside validators. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` | Validators check posture; data roots store lifecycle artifacts. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Proof and receipt authority stays outside validators. |
| Release decisions and rollback | `release/` | Release authority stays in release records and promotion decisions. |
| Contracts and schemas | `contracts/`, `schemas/contracts/v1/` | Validators check declared meaning and shape; they do not define them. |
| Policy | `policy/` | Validators report policy gaps; they do not decide policy. |

[Back to top](#top)

---

## Transition gates

| Transition | Validator question | Fail / abstain condition |
|---|---|---|
| `RAW -> WORK` | Was source material admitted with source descriptor, rights, source role, digest, retrieval/import record, and quarantine screen? | Source identity, rights, role, digest, provenance, or import receipt is missing. |
| `RAW -> QUARANTINE` | Was risky, sensitive, rights-unclear, malformed, conflicting, or unsupported material held rather than normalized into truth? | Candidate bypasses quarantine despite sensitivity, rights, quality, evidence, or policy uncertainty. |
| `QUARANTINE -> WORK` | Did a governed exit record resolve the reason for hold? | Quarantine exit lacks review, evidence, rights, policy, transform, receipt, correction, or rollback support. |
| `WORK -> PROCESSED` | Are transforms, normalization, enrichment, derivation, model output, and quality results recorded with reproducible inputs and outputs? | Processed candidate lacks transform lineage, validation report, version, digest, or source-role preservation. |
| `PROCESSED -> CATALOG` | Does the catalog candidate describe governed data without becoming proof, release, publication, or truth? | Catalog entry lacks source/evidence/policy/release posture or overclaims authority. |
| `PROCESSED -> TRIPLET` | Does graph/triplet projection preserve EvidenceRef, source role, sensitivity, object identity, and correction lineage? | Graph edge becomes truth without evidence/policy/release support or weakens restrictions. |
| `CATALOG/TRIPLET -> PUBLISHED` | Does the release candidate have EvidenceBundle closure, validation reports, PolicyDecision, review state, ReleaseManifest, rollback target, and public-safe derivative boundaries? | Public exposure is attempted without governed release support. |
| `PUBLISHED -> CORRECTED/WITHDRAWN/ROLLED BACK` | Do correction, withdrawal, revocation, stale-state, source-rights changes, and rollback propagate to derivatives and public surfaces? | Downstream artifact remains active or citable after a blocking change. |

[Back to top](#top)

---

## Lifecycle validation invariants

| Invariant | Validator expectation | Must not become |
|---|---|---|
| State is explicit | Candidate declares current lifecycle state and intended next state. | Implied state from folder path only. |
| Transition is governed | Candidate has required decision, review, validation, evidence, policy, receipt, and rollback support for the transition. | File move or PR merge as promotion. |
| Quarantine is sticky until resolved | Quarantine reason must close before downstream use. | Informal staging shortcut. |
| Source role survives | Observed, modeled, administrative, regulatory, aggregate, candidate, synthetic, and public-safe roles remain visible. | Generic processed truth. |
| Evidence closes consequential claims | EvidenceRef resolves to sufficient EvidenceBundle/proof support where claims depend on evidence. | Generated summary or catalog entry as proof. |
| Policy gates remain separate | PolicyDecision and policy bundle identity are recorded where required. | Validator pass as policy approval. |
| Release gates remain separate | ReleaseManifest, PromotionDecision, correction path, and rollback target are present before public use. | Catalog/triplet/public folder presence as release approval. |
| Public surfaces use released derivatives | Map, tile, graph, export, search, Focus Mode, screenshot, embedding, or AI output reads only governed public-safe release surfaces. | Direct RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/internal-store access. |
| Corrections propagate | Correction, withdrawal, revocation, stale state, source-rights change, and rollback invalidate downstream carriers. | One-time validation treated as permanent truth. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Lifecycle validator routing index | `tools/validators/lifecycle/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Catalog validator lane | `tools/validators/catalog/` |
| Evidence validator lane | `tools/validators/evidence/` |
| Identity validator lane | `tools/validators/identity/` |
| Join and cross-domain lifecycle checks | `tools/validators/joins/`, `tools/validators/cross-domain-joins/` |
| Source descriptors and registries | `data/registry/`, `data/registry/sources/` |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, correction, rollback, withdrawal | `release/` |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/contracts/v1/` |
| Policy rules and release gates | `policy/` |
| Tests and fixtures | `tests/validators/lifecycle/`, `tests/lifecycle/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared lifecycle invariants and delegates meaning, schemas, policy, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, runtime behavior, release integration, and CI wiring.
- **DENY:** using this folder as source registry, lifecycle data store, catalog store, triplet store, proof store, receipt store, release record store, policy home, schema home, public runtime surface, AI answer authority, file-move promotion shortcut, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/lifecycle/` include checks that:

- verify source admission has source descriptor, rights, role, digest, provenance, and import/retrieval receipt support;
- detect material that must enter or remain in quarantine;
- verify quarantine exits are evidence-backed, reviewed, policy-supported, receipt-backed, and rollback-aware;
- verify processed candidates carry transform lineage, validation reports, versions, digests, and source-role preservation;
- verify catalog and triplet projections do not become proof, release, or public truth;
- verify public-bound candidates have EvidenceBundle closure, policy decisions, review records, promotion decisions, release manifests, correction paths, rollback targets, and public-safe derivative boundaries;
- verify corrections, withdrawals, revocations, stale-state transitions, source-rights changes, and rollbacks propagate to downstream carriers;
- emit deterministic validation findings for steward review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/lifecycle/` | Correct home |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| Catalog records or indexes | `data/catalog/` |
| Graph/triplet projections | `data/triplets/` |
| Published public-safe artifacts | `data/published/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Schemas, DTOs, enums, or lifecycle machine shape | `schemas/contracts/v1/...` |
| Semantic contracts | `contracts/` |
| Policy rules, release gates, steward decisions, sensitivity thresholds | `policy/`, `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, screenshot, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `LIFECYCLE_VALIDATOR_PASS` | Candidate passed configured lifecycle checks. |
| `LIFECYCLE_VALIDATOR_FAIL` | One or more configured lifecycle checks failed. |
| `LIFECYCLE_VALIDATOR_DENY` | Candidate is denied because evidence, rights, policy, review, release, correction, rollback, or public-surface support cannot be resolved. |
| `LIFECYCLE_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `LIFECYCLE_VALIDATOR_ABSTAIN` | Candidate lacks enough evidence or policy support for the transition. |
| `STATE_MISSING` | Candidate does not declare current lifecycle state. |
| `TARGET_STATE_MISSING` | Candidate does not declare intended next lifecycle state. |
| `INVALID_STATE_TRANSITION` | Candidate attempts a transition outside accepted lifecycle order or without gate support. |
| `QUARANTINE_REQUIRED` | Candidate must enter quarantine because rights, sensitivity, evidence, quality, policy, or source-role risk is unresolved. |
| `QUARANTINE_EXIT_UNSUPPORTED` | Candidate attempts to leave quarantine without closing the hold reason. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor or source role support is absent. |
| `TRANSFORM_LINEAGE_MISSING` | Transform/version/digest/spec-hash lineage is absent or unresolved. |
| `VALIDATION_REPORT_MISSING` | Required validation report is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `POLICY_OR_REVIEW_GAP` | Required PolicyDecision, review state, rights posture, or release policy support is absent. |
| `CATALOG_AUTHORITY_OVERCLAIM` | Catalog entry is treated as truth, proof, release, or publication. |
| `TRIPLET_AUTHORITY_OVERCLAIM` | Graph/triplet projection is treated as truth without required evidence/policy/release support. |
| `PROMOTION_DECISION_MISSING` | Required governed transition decision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Public surface exposes unsafe or unreleased lifecycle state. |
| `CORRECTION_CASCADE_MISSING` | Correction, revocation, withdrawal, stale state, rights change, or rollback did not propagate. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/lifecycle/
├── README.md
├── validate_lifecycle_transition.py     # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_lifecycle_transition.py` is added, it should act as an adapter or dispatcher that routes to accepted source, evidence, catalog, identity, policy, release, receipt, and domain validators. It should not move files, write lifecycle data, create EvidenceBundles, write receipts, decide policy, approve release, publish public outputs, or generate AI truth.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/lifecycle/README.md`.
- [x] It marks this path as lifecycle validator routing, not lifecycle data, catalog, proof, receipt, policy, release, public runtime, or AI authority.
- [x] It preserves RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED lifecycle posture.
- [x] It distinguishes catalog records, evidence support, receipts, promotion decisions, release manifests, corrections, and rollback targets as separate authority families.
- [x] It routes machine shape, policy, fixtures, evidence, receipts, release, lifecycle data, tests, and semantic meaning to their owning roots.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixture files, receipt emission, runtime behavior, release integration, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `lifecycle/` are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid lifecycle transitions, quarantine exits, catalog/triplet projections, release gaps, correction cascades, and public-surface leakage cases.
- [ ] CI invokes the relevant lifecycle validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with lifecycle validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
