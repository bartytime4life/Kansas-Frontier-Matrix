<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-citation-readme
title: tools/validators/citation README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-citation-steward-plus-evidence-steward-plus-proof-steward-plus-policy-steward-plus-release-steward-plus-ui-evidence-drawer-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; citation-validator; CitationValidationReport; EvidenceRef; EvidenceBundle; cite-or-abstain; source-role-aware; sensitivity-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Citation validator lane for checking citation presence, citation scope, source record linkage, EvidenceRef resolution, EvidenceBundle linkage, CitationValidationReport readiness, source-role preservation, rights/sensitivity/freshness/caveat posture, release/correction/rollback linkage, governed-answer readiness, finite negative outcomes, and public-surface denial checks while deferring citation semantics, schemas, proof storage, receipts, policy decisions, release authority, package helpers, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../evidence/README.md
  - ../evidence_bundle/README.md
  - ../../contracts/evidence/README.md
  - ../../contracts/evidence/citation_validation_report.md
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../fixtures/contracts/v1/evidence/citation_validation_report/
  - ../../data/proofs/citation_validation/README.md
  - ../../data/proofs/evidence_bundle/README.md
  - ../../data/registry/sources/
  - ../../data/receipts/
  - ../../release/
  - ../../policy/evidence/
  - ../../packages/citation/README.md
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "CitationValidationReport is a validation/report object. It is not EvidenceBundle closure, not policy permission, not release approval, and not materialized proof storage."
  - "The paired citation-validation-report schema is confirmed as a permissive scaffold; field-level shape, executable validator behavior, fixtures, CI wiring, policy enforcement, release behavior, public API behavior, Evidence Drawer behavior, and runtime/AI behavior remain NEEDS VERIFICATION."
  - "packages/citation/ may provide reusable citation helpers, but it cannot create EvidenceBundles, decide truth, approve source admission, decide policy, or approve release."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/citation

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-citation--validator-informational)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-success)
![boundary](https://img.shields.io/badge/boundary-not--proof--storage-critical)
![release](https://img.shields.io/badge/release-gated-critical)

> **One-line purpose.** `tools/validators/citation/` is the proposed validator lane for checking citation readiness, EvidenceRef resolution, source/citation scope, citation-validation report posture, release linkage, and public-surface safety before any governed claim, map popup, Evidence Drawer payload, export, Focus Mode output, or AI answer can cite it.

---

## Purpose

`tools/validators/citation/` exists for citation validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Are the citations supporting a governed claim present, resolvable, complete, scoped, rights-aware, sensitivity-aware, source-role-aware, release-linked, correction-aware, rollback-aware, and safe for the requested surface — or must the system return a finite negative outcome instead of citing or answering?

The answer should be a deterministic validation result. This folder should not create citations as truth, store proof artifacts, store receipts, create EvidenceBundles, decide policy, approve release, publish public map/API/UI/AI outputs, or convert generated text into evidence.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/citation/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| CitationValidationReport contract | **CONFIRMED in repo evidence / draft** | `contracts/evidence/citation_validation_report.md` defines report semantics and states the report is not EvidenceBundle closure, policy permission, release approval, or proof storage. |
| Paired CitationValidationReport schema | **CONFIRMED permissive scaffold / NEEDS VERIFICATION** | The contract says the paired schema exists but is permissive with no declared properties and `additionalProperties: true`; field realization remains proposed. |
| Citation-validation proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/citation_validation/README.md` supports EvidenceRef resolution checks, citation closure, finite negative outcomes, and governed-answer readiness without publishing claims. |
| Citation package | **CONFIRMED README / implementation NEEDS VERIFICATION** | `packages/citation/README.md` describes reusable citation and EvidenceRef helpers but says concrete implementation, exports, tests, and CI remain unverified. |
| Executable, fixtures, resolver behavior, policy enforcement, release behavior, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator implementation, report schema enforcement, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Citation validator lane | `tools/validators/citation/` |
| Parent evidence validator index | `tools/validators/evidence/` |
| EvidenceBundle validator lane | `tools/validators/evidence_bundle/` |
| Shared validator plumbing | `tools/validators/_common/` |
| CitationValidationReport meaning | `contracts/evidence/citation_validation_report.md` |
| Citation/Evidence machine shape | `schemas/contracts/v1/evidence/` |
| Citation-validation proof support | `data/proofs/citation_validation/` |
| EvidenceBundle proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Reusable citation helpers | `packages/citation/` |
| Source descriptors | `data/registry/sources/` |
| Policy and admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Receipts | `data/receipts/` |
| Release, corrections, rollback, withdrawal | `release/` |

This README does not move, replace, or override those roots. It only defines where citation validation orchestration and citation-readiness checks may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and schema fields are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Citation presence | Are required citations present for the claim or surface? | Proof by itself. |
| Citation scope | Does each citation support the exact claim scope, time, place, object family, and caveat? | Broad authority for uncited claims. |
| EvidenceRef resolution | Do citations connect to resolvable EvidenceRefs and EvidenceBundles where required? | Closure if references are unresolved. |
| Source record linkage | Are SourceDescriptors, source roles, source families, rights, freshness, and limits visible? | Source admission or source authority. |
| Rights and sensitivity | Are rights, restrictions, geoprivacy, redaction, aggregation, and review posture visible? | Policy approval. |
| CitationValidationReport | Does the report record PASS/FAIL/HOLD/DENY/ABSTAIN/ERROR findings and remediation? | EvidenceBundle closure or release approval. |
| Release linkage | Are release/correction/rollback/supersession/withdrawal references present when public-bound? | Publication by validation alone. |
| Finite negative outcomes | Does the candidate abstain, deny, hold, or error instead of answering when citation closure fails? | Model-generated workaround. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Citation validator lane | `tools/validators/citation/` |
| Parent evidence validator index | `tools/validators/evidence/` |
| EvidenceBundle validator lane | `tools/validators/evidence_bundle/` |
| Shared validator plumbing | `tools/validators/_common/` |
| CitationValidationReport semantics | `contracts/evidence/citation_validation_report.md` |
| EvidenceRef and EvidenceBundle semantics | `contracts/evidence/evidence_ref.md`, `contracts/evidence/evidence_bundle.md` |
| Evidence/citation schemas | `schemas/contracts/v1/evidence/` |
| Citation-validation proof support | `data/proofs/citation_validation/` |
| EvidenceBundle/proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Citation helper library | `packages/citation/` |
| Source descriptors | `data/registry/sources/` |
| Policy/admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/citation/`, `tests/evidence/`, `fixtures/contracts/v1/evidence/citation_validation_report/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED AS TEXT:** citation-validation contract/proof/package documentation exists and defines boundaries.
- **PROPOSED:** validator code may live here when it checks declared citation readiness, evidence linkage, policy, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, report fields, schema enforcement, fixture coverage, resolver behavior, package integration, policy enforcement, receipt emission, release integration, governed route behavior, runtime/AI behavior, and CI wiring.
- **DENY:** using this folder as citation semantics, schema home, proof storage, receipt storage, source registry, policy home, release record store, public runtime surface, Evidence Drawer payload store, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/citation/` include checks that:

- verify every public-bound claim, Evidence Drawer payload, map popup, export, Focus Mode answer, API answer, report card, or AI answer candidate has required citations;
- verify citations resolve to allowed EvidenceRefs, EvidenceBundles, SourceDescriptors, proof support, release references, correction references, and rollback references where required;
- verify citations are scoped to the claim and do not overstate source authority;
- verify citation source roles, caveats, freshness, sensitivity, rights, redaction, aggregation, and review posture are visible;
- verify stale, withdrawn, superseded, embargoed, rights-blocked, sensitivity-blocked, malformed, or out-of-scope citations fail closed;
- verify candidates return finite negative outcomes when citation closure fails;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/citation/` | Correct home |
|---|---|
| CitationValidationReport meaning/contracts | `contracts/evidence/citation_validation_report.md` |
| EvidenceRef / EvidenceBundle meaning | `contracts/evidence/` |
| Evidence and citation schemas/enums | `schemas/contracts/v1/evidence/` |
| Materialized citation-validation proof artifacts | `data/proofs/citation_validation/` |
| EvidenceBundles, ProofPacks, proof records | `data/proofs/` |
| Receipts, ValidationReports, AIReceipts, RunReceipts | `data/receipts/` |
| Source descriptors or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| Citation helper package implementation | `packages/citation/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Evidence Drawer payloads, map popups, Focus Mode text, AI answer text, public API responses | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Citation validator posture

Citation validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks required citations;
- contains missing, malformed, unresolved, stale, withdrawn, superseded, embargoed, rights-blocked, sensitivity-blocked, redaction-incomplete, aggregation-incomplete, or out-of-scope citations;
- cites an EvidenceRef without resolving required EvidenceBundle support;
- treats a CitationValidationReport as EvidenceBundle closure, PolicyDecision approval, ReleaseManifest approval, proof storage, or receipt by itself;
- treats generated text, summaries, vector retrieval, graph projection, map tile, scene, UI payload, or model output as source evidence;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct canonical/internal stores, direct model output, or incomplete proof closure;
- emits reports, receipts, or findings outside accepted roots;
- treats validator output as citation truth, EvidenceBundle creation, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CITATION_VALIDATOR_PASS` | Configured citation checks passed. |
| `CITATION_VALIDATOR_FAIL` | One or more configured citation checks failed. |
| `CITATION_MISSING` | Required citation is absent. |
| `CITATION_MALFORMED` | Citation shape is invalid or incomplete. |
| `CITATION_SCOPE_MISMATCH` | Citation does not support the exact claim scope. |
| `CITATION_UNRESOLVED` | Citation cannot resolve through accepted resolver/path. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef is absent. |
| `EVIDENCE_REF_UNRESOLVED` | EvidenceRef cannot resolve to required support. |
| `EVIDENCE_BUNDLE_MISSING` | Required EvidenceBundle support is absent. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor pointer is absent. |
| `SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `RIGHTS_OR_SENSITIVITY_GAP` | Rights, sensitivity, redaction, aggregation, or access posture is incomplete. |
| `CITATION_STALE_OR_SUPERSEDED` | Citation is stale, corrected, withdrawn, superseded, or embargoed for the requested use. |
| `CITATION_VALIDATION_REPORT_MISSING` | Required CitationValidationReport is absent. |
| `POLICY_OR_RELEASE_GAP` | Required PolicyDecision, ReviewRecord, ReleaseManifest, correction path, or rollback target is absent. |
| `CITATION_REPORT_AS_RELEASE_DENIED` | Candidate treats citation validation as release approval. |
| `GENERATED_TEXT_AS_CITATION_DENIED` | Candidate treats generated text or model output as source citation. |
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
tests/validators/citation/
├── README.md
├── test_citation_validator.py
└── fixtures/
    ├── valid_citation_closure/
    ├── missing_citation/
    ├── malformed_citation/
    ├── citation_scope_mismatch/
    ├── unresolved_citation/
    ├── missing_evidence_ref/
    ├── missing_evidence_bundle/
    ├── rights_or_sensitivity_gap/
    ├── stale_or_superseded_citation/
    └── generated_text_as_citation_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/citation
```

```bash
python tools/validators/citation/validate_citation.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_citation.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared citation/evidence contracts, schemas, source descriptors, policy, proof, receipt, and release records rather than defining meaning locally.
- [ ] Citation, EvidenceRef, EvidenceBundle, CitationValidationReport, PolicyDecision, and ReleaseManifest are not collapsed.
- [ ] Citation validation remains readiness/gating support, not public claim text or proof storage.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, or incomplete proof closure.
- [ ] AI/governed answer surfaces return finite negative outcomes when citation closure is incomplete.
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
| Review state | Draft README replacement for stray one-character Citation validator file. |
| Next smallest safe change | Verify actual citation validator script path, report schema binding, fixture coverage, resolver behavior, package integration, report destination, receipt emission, policy enforcement, release linkage, governed route behavior, and CI/runtime wiring before promoting this lane beyond draft. |
