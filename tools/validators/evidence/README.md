<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-evidence-readme
title: tools/validators/evidence README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-evidence-steward-plus-proof-steward-plus-policy-steward-plus-release-steward-plus-ui-evidence-drawer-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; evidence-validator-index; EvidenceRef; EvidenceBundle; citation-validation; cite-or-abstain; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed evidence validator index for EvidenceRef resolution, EvidenceBundle closure, citation validation, source-role preservation, rights/sensitivity posture, transform/digest/spec-hash posture, policy/review/release linkage, correction and rollback linkage, governed-answer readiness, finite negative outcomes, and public-surface denial checks while deferring evidence semantics, schemas, proof storage, receipts, policy decisions, release authority, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../validators/README.md
  - ../validators/_common/README.md
  - ../validators/ai/evidence_before_model/README.md
  - ../../contracts/evidence/README.md
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../contracts/evidence/citation_validation_report.md
  - ../../schemas/contracts/v1/evidence/README.md
  - ../../data/proofs/README.md
  - ../../data/proofs/evidence_bundle/README.md
  - ../../data/proofs/citation_validation/README.md
  - ../../data/registry/sources/
  - ../../data/receipts/
  - ../../release/
  - ../../policy/evidence/
  - ../../packages/evidence-resolver/src/README.md
  - ../../packages/citation/README.md
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "Evidence validators check readiness and closure. They do not define evidence semantics, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish public outputs, or authorize generated answers."
  - "Contracts define evidence semantics; schemas define machine shape; data/proofs stores materialized proof support; data/receipts stores receipts; policy decides admissibility; release decides publication."
  - "EvidenceBundle outranks generated language, but a valid EvidenceBundle is still not a PolicyDecision or ReleaseManifest."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/evidence

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-evidence--validators-informational)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-success)
![boundary](https://img.shields.io/badge/boundary-validator--only-lightgrey)
![release](https://img.shields.io/badge/release-gated-critical)

> **One-line purpose.** `tools/validators/evidence/` is the proposed parent index for evidence validators that check EvidenceRef resolution, EvidenceBundle closure, citation validation, source-role preservation, policy/release linkage, correction/rollback linkage, and governed-answer readiness without becoming proof storage or evidence authority.

---

## Purpose

`tools/validators/evidence/` exists to organize evidence-facing validators under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Do evidence-bearing candidates resolve EvidenceRefs into complete EvidenceBundle support, preserve source-role, rights, sensitivity, transform, digest, checksum, citation, policy, release, correction, and rollback posture, and return finite negative outcomes when closure is incomplete?

The answer should be a deterministic validation result. This folder should not create EvidenceRefs, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish public map/API/UI/AI outputs, or convert generated text into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/evidence/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| Evidence contracts | **CONFIRMED in repo evidence / draft** | `contracts/evidence/README.md` defines evidence semantics and says EvidenceBundle is the closure artifact while EvidenceRef is a governed pointer that does not by itself guarantee closure. |
| EvidenceBundle proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/evidence_bundle/README.md` supports EvidenceRef → EvidenceBundle closure, claim support, digest closure, finite negative outcomes, and governed-answer readiness. |
| Citation validation proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/citation_validation/README.md` supports EvidenceRef resolution checks, citation closure, finite negative outcomes, and governed answer readiness. |
| AI evidence-before-model lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/ai/evidence_before_model/README.md` checks that evidence and policy gates happen before model interpretation. |
| Executables, schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This index does not claim a validator implementation, report schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Evidence meaning | `contracts/evidence/` |
| Evidence machine shape | `schemas/contracts/v1/evidence/` |
| EvidenceBundle proof support | `data/proofs/evidence_bundle/` and domain proof lanes |
| Citation-validation proof support | `data/proofs/citation_validation/` |
| Validation receipts | `data/receipts/validation/` or accepted receipts roots |
| AI evidence-before-model checks | `tools/validators/ai/evidence_before_model/` |
| Generic evidence validator index / parent runner | `tools/validators/evidence/` |
| Source descriptors | `data/registry/sources/` |
| Policy and admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Release, corrections, rollback, withdrawal | `release/` |

This README does not move, replace, or override those roots. It only defines where evidence validation orchestration and evidence-readiness checks may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed child lanes

No child README lanes under `tools/validators/evidence/` were confirmed during this edit.

Possible future children remain **PROPOSED** until created and verified:

- `evidence_ref_resolution/` for checking that EvidenceRefs resolve to allowed, current, accessible EvidenceBundle support;
- `evidence_bundle_closure/` for checking source/citation/rights/sensitivity/transform/digest/spec-hash/release closure;
- `citation_validation/` for checking claim-to-citation readiness while storing proof artifacts in `data/proofs/citation_validation/`;
- `rights_sensitivity/` for checking rights, sensitivity, restriction, redaction, aggregation, and public-use posture;
- `release_linkage/` for checking ReleaseManifest, correction, rollback, supersession, and withdrawal references;
- `governed_answer_readiness/` for checking finite outcomes before Evidence Drawer, Focus Mode, API, map popup, report, or AI answer surfaces.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Evidence validator index and optional parent runner | `tools/validators/evidence/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Evidence-before-model AI validator | `tools/validators/ai/evidence_before_model/` |
| Evidence semantics | `contracts/evidence/` |
| Evidence schemas | `schemas/contracts/v1/evidence/` |
| Evidence policy/admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/` |
| EvidenceBundle/proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Citation-validation proof support | `data/proofs/citation_validation/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Evidence resolver / citation packages | `packages/evidence-resolver/`, `packages/citation/`, or accepted package roots |
| Tests and fixtures | `tests/validators/evidence/`, `tests/evidence/`, `fixtures/contracts/v1/evidence/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared evidence closure, citation, policy, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, child lane names, schemas, fixtures, report destinations, receipt emission, resolver behavior, package integration, governed route behavior, and CI wiring.
- **DENY:** using this folder as evidence semantics, schema home, proof storage, receipt storage, source registry, policy home, release record store, public runtime surface, Evidence Drawer payload store, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/evidence/` include checks that:

- verify an EvidenceRef resolves to an expected EvidenceBundle or fails with a finite negative outcome;
- verify an EvidenceBundle contains required source records, citations, rights, sensitivity, transforms, checksums, spec-hash/digest posture, time scope, geography/generalization posture, review refs, policy refs, release refs, correction refs, and rollback refs for the claim scope;
- verify citation validation reports are present and consistent for public-bound claims;
- verify claims do not cite unresolved, stale, withdrawn, embargoed, superseded, restricted, or policy-denied evidence;
- verify public/AI/governed answer candidates return `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` instead of an answer when evidence closure is incomplete;
- verify validator reports are deterministic and point receipts to accepted roots;
- emit findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/evidence/` | Correct home |
|---|---|
| Evidence meaning/contracts | `contracts/evidence/` |
| Evidence schemas/enums | `schemas/contracts/v1/evidence/` |
| Materialized EvidenceBundles, ProofPacks, proof records | `data/proofs/` |
| Citation-validation proof artifacts | `data/proofs/citation_validation/` |
| Receipts, ValidationReports, AIReceipts, RunReceipts | `data/receipts/` |
| Source descriptors or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Evidence resolver or citation runtime libraries | `packages/evidence-resolver/`, `packages/citation/`, or accepted package roots |
| Public API, UI, Evidence Drawer payloads, map popups, report text, Focus Mode output, AI runtime output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Evidence validator posture

Evidence validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- has an unresolved EvidenceRef;
- has an EvidenceBundle that lacks required source, citation, rights, sensitivity, transform, digest, checksum, policy, review, release, correction, or rollback support;
- treats EvidenceRef as equivalent to EvidenceBundle closure;
- treats EvidenceBundle closure as policy approval or release approval;
- cites evidence that is stale, withdrawn, superseded, embargoed, rights-restricted, sensitivity-restricted, redaction-incomplete, aggregation-incomplete, or release-denied for the requested surface;
- presents generated text, summaries, vector retrieval, graph projection, map tile, scene, or UI payload as sovereign evidence;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct canonical/internal stores, direct model output, or incomplete proof closure;
- emits validator reports, receipts, or findings outside accepted roots;
- treats validator output as EvidenceBundle creation, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `EVIDENCE_VALIDATORS_PASS` | Configured evidence validators passed. |
| `EVIDENCE_VALIDATORS_FAIL` | One or more configured evidence validators failed. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef is absent. |
| `EVIDENCE_REF_UNRESOLVED` | EvidenceRef cannot resolve through accepted resolver/path. |
| `EVIDENCE_BUNDLE_MISSING` | Required EvidenceBundle is absent. |
| `EVIDENCE_BUNDLE_INCOMPLETE` | EvidenceBundle lacks required source/citation/rights/sensitivity/transform/digest/policy/release/correction/rollback support. |
| `CITATION_VALIDATION_MISSING` | Required citation-validation report or proof support is absent. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor pointer is absent. |
| `RIGHTS_OR_SENSITIVITY_GAP` | Rights, sensitivity, redaction, aggregation, or access posture is incomplete. |
| `POLICY_OR_RELEASE_GAP` | Required PolicyDecision, ReviewRecord, ReleaseManifest, correction path, or rollback target is absent. |
| `EVIDENCE_STALE_OR_SUPERSEDED` | Evidence is stale, corrected, withdrawn, superseded, or embargoed for the requested use. |
| `EVIDENCE_AS_RELEASE_DENIED` | Candidate treats evidence closure as release approval. |
| `GENERATED_TEXT_AS_EVIDENCE_DENIED` | Candidate treats generated text or model output as source evidence. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, closure, or quarantine before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/evidence/
├── README.md
├── test_evidence_validator_parent.py
└── fixtures/
    ├── valid_evidence_bundle_closure/
    ├── missing_evidence_ref/
    ├── unresolved_evidence_ref/
    ├── missing_evidence_bundle/
    ├── incomplete_evidence_bundle/
    ├── missing_citation_validation/
    ├── rights_or_sensitivity_gap/
    ├── policy_or_release_gap/
    ├── stale_or_superseded_evidence/
    └── generated_text_as_evidence_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/evidence
```

```bash
python tools/validators/evidence/run_evidence_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_evidence_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared evidence contracts, schemas, source descriptors, policy, proof, receipt, and release records rather than defining meaning locally.
- [ ] EvidenceRef and EvidenceBundle are not collapsed.
- [ ] EvidenceBundle closure is not treated as PolicyDecision or ReleaseManifest approval.
- [ ] Citation validation remains evidence-readiness proof support, not public claim text.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, or incomplete proof closure.
- [ ] AI/governed answer surfaces return finite negative outcomes when closure is incomplete.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for stray one-character evidence validator file. |
| Next smallest safe change | Verify actual evidence validator scripts, child lanes, schema bindings, fixtures, resolver behavior, report destinations, receipt emission, release linkage, governed route behavior, and CI/runtime wiring before promoting this lane beyond draft. |
