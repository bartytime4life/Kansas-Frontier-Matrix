<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-evidence-bundle-readme
title: tools/validators/evidence_bundle README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-evidence-bundle-steward-plus-evidence-steward-plus-proof-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; evidence-bundle-validator; EvidenceBundle; claim-scope-closure; schema-aware; cite-or-abstain; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed EvidenceBundle validator lane for checking claim-scope closure, required schema fields, EvidenceRef closure, source records, citations, rights posture, sensitivity posture, transforms, checksums, spec-hash/schema linkage, policy/review/release references, correction and rollback linkage, resolver readiness, governed-answer readiness, finite negative outcomes, and public-surface denial checks while deferring evidence semantics, schemas, proof storage, receipts, policy decisions, release authority, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../evidence/README.md
  - ../../contracts/evidence/README.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../contracts/evidence/evidence_ref.md
  - ../../contracts/evidence/evidence_bundle/README.md
  - ../../contracts/evidence/citation_validation_report.md
  - ../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../schemas/contracts/v1/evidence/README.md
  - ../../fixtures/contracts/v1/evidence/evidence_bundle/
  - ../../data/proofs/README.md
  - ../../data/proofs/evidence_bundle/README.md
  - ../../data/proofs/citation_validation/README.md
  - ../../data/registry/sources/
  - ../../data/receipts/
  - ../../release/
  - ../../policy/evidence/
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "The EvidenceBundle contract confirms a paired schema and references validator metadata, but actual validator behavior, CI status, fixture coverage, resolver behavior, policy enforcement, release behavior, public API behavior, Evidence Drawer behavior, and runtime/AI behavior remain NEEDS VERIFICATION unless separately tested."
  - "EvidenceBundle is the claim-scope closure artifact. It is not an EvidenceRef, not a PolicyDecision, not a ReleaseManifest, not proof storage by itself, not a receipt, not source registry authority, and not AI answer authority."
  - "Materialized EvidenceBundle proof records belong under data/proofs/ unless an ADR changes proof authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/evidence_bundle

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-EvidenceBundle--validator-informational)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-success)
![boundary](https://img.shields.io/badge/boundary-not--proof--storage-critical)
![release](https://img.shields.io/badge/release-gated-critical)

> **One-line purpose.** `tools/validators/evidence_bundle/` is the proposed validator lane for checking whether `EvidenceBundle` candidates satisfy claim-scope closure, schema posture, source/citation/rights/sensitivity/transform/checksum support, and policy/release linkage before any governed use.

---

## Purpose

`tools/validators/evidence_bundle/` exists for EvidenceBundle-specific validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does an EvidenceBundle candidate close the evidence side of a governed claim scope with resolvable EvidenceRefs, reconstructable source records, publication-ready citations, rights posture, sensitivity posture, transform lineage, checksums/spec hashes, schema linkage, policy/review/release references, correction lineage, rollback targets, and finite negative outcomes when closure is incomplete?

The answer should be a deterministic validation result. This folder should not create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish public map/API/UI/AI outputs, or convert generated text into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/evidence_bundle/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| EvidenceBundle contract | **CONFIRMED in repo evidence / draft** | `contracts/evidence/evidence_bundle.md` defines EvidenceBundle as the claim-scope closure artifact and warns it is not release approval, proof storage, receipt, source registry, or AI answer authority. |
| Paired EvidenceBundle schema | **CONFIRMED in repo evidence / draft** | The contract confirms `schemas/contracts/v1/evidence/evidence_bundle.schema.json` as a fielded schema. |
| Materialized EvidenceBundle proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/evidence_bundle/README.md` supports EvidenceRef → EvidenceBundle closure, claim support, digest closure, finite negative outcomes, and governed-answer readiness. |
| Parent evidence validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/evidence/README.md` defines the parent evidence validator index and nearby-lane routing. |
| Executable, fixtures, resolver behavior, policy enforcement, release behavior, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | The contract references validator metadata, but this README does not claim tested runtime behavior or CI enforcement. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| EvidenceBundle meaning | `contracts/evidence/evidence_bundle.md` |
| EvidenceBundle machine shape | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` |
| Materialized EvidenceBundle proof support | `data/proofs/evidence_bundle/` and domain proof lanes |
| Parent evidence validator routing | `tools/validators/evidence/` |
| EvidenceRef resolution checks | `tools/validators/evidence/` or future `tools/validators/evidence/evidence_ref_resolution/` |
| Citation validation proof support | `data/proofs/citation_validation/` |
| Validation receipts | `data/receipts/validation/` or accepted receipts roots |
| Source descriptors | `data/registry/sources/` |
| Policy and admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Release, corrections, rollback, withdrawal | `release/` |

This README does not move, replace, or override those roots. It only defines where EvidenceBundle validation orchestration and closure checks may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior is verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Claim scope | Is the claim scope explicit, bounded, and stable enough to validate? | Public truth by itself. |
| EvidenceRef closure | Do all required EvidenceRefs resolve to accepted bundle members or negative outcomes? | Closure if references are unresolved. |
| Source records | Are source descriptors, source roles, source times, and source rights present where required? | Source admission or source authority. |
| Citations | Are citations publication-ready and tied to the claim scope? | Citation truth without evidence closure. |
| Rights and sensitivity | Are rights, restrictions, redaction, aggregation, sensitivity, and review posture visible? | Policy approval. |
| Transform and digest closure | Are transforms, checksums, spec hashes, and schema linkage reconstructable? | Receipt storage or proof storage. |
| Release linkage | Are release/correction/rollback references present when public-bound? | Release approval. |
| Finite negative outcomes | Does the candidate return `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` when closure is incomplete? | Model-generated workaround. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| EvidenceBundle validator lane | `tools/validators/evidence_bundle/` |
| Parent evidence validator index | `tools/validators/evidence/` |
| Shared validator plumbing | `tools/validators/_common/` |
| EvidenceBundle semantics | `contracts/evidence/evidence_bundle.md` |
| EvidenceRef semantics | `contracts/evidence/evidence_ref.md` |
| Evidence schemas | `schemas/contracts/v1/evidence/` |
| Evidence policy/admissibility | `policy/evidence/`, `policy/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/` |
| EvidenceBundle/proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Citation-validation proof support | `data/proofs/citation_validation/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/evidence_bundle/`, `tests/validators/evidence/`, `fixtures/contracts/v1/evidence/evidence_bundle/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED AS TEXT:** the EvidenceBundle contract points to a schema and validator metadata.
- **PROPOSED:** validator code may live here when it checks declared EvidenceBundle closure rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable behavior, report shape, fixture coverage, resolver behavior, policy enforcement, receipt emission, release integration, governed route behavior, runtime/AI behavior, and CI wiring.
- **DENY:** using this folder as evidence semantics, schema home, proof storage, receipt storage, source registry, policy home, release record store, public runtime surface, Evidence Drawer payload store, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/evidence_bundle/` include checks that:

- verify EvidenceBundle candidates conform to the accepted schema when schema validation is configured;
- verify required claim scope, EvidenceRefs, source records, citations, rights, sensitivity, transforms, checksums, and spec/schema linkage are present;
- verify EvidenceRef pointers resolve through accepted resolver behavior or produce finite negative outcomes;
- verify rights/sensitivity posture matches the requested surface and does not bypass redaction, aggregation, review, or policy requirements;
- verify policy, review, release, correction, rollback, supersession, and withdrawal references are present when public-bound;
- verify stale, withdrawn, embargoed, superseded, restricted, or policy-denied evidence is not used as public answer support;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/evidence_bundle/` | Correct home |
|---|---|
| EvidenceBundle meaning/contracts | `contracts/evidence/evidence_bundle.md` |
| Evidence schemas/enums | `schemas/contracts/v1/evidence/` |
| Materialized EvidenceBundles, ProofPacks, proof records | `data/proofs/` |
| Citation-validation proof artifacts | `data/proofs/citation_validation/` |
| Receipts, ValidationReports, AIReceipts, RunReceipts | `data/receipts/` |
| Source descriptors or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Evidence Drawer payloads, map popups, Focus Mode text, AI answer text, public API responses | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## EvidenceBundle validator posture

EvidenceBundle validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks explicit claim scope;
- contains unresolved, stale, withdrawn, superseded, embargoed, restricted, or policy-denied EvidenceRefs;
- lacks required source records, citations, rights, sensitivity posture, transforms, checksums, spec hashes, schema linkage, policy refs, review refs, release refs, correction refs, or rollback refs;
- treats EvidenceRef as equivalent to EvidenceBundle closure;
- treats EvidenceBundle closure as PolicyDecision or ReleaseManifest approval;
- treats generated text, summaries, vector retrieval, graph projection, map tile, scene, or UI payload as sovereign evidence;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct canonical/internal stores, direct model output, or incomplete proof closure;
- emits reports, receipts, or findings outside accepted roots;
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
| `EVIDENCE_BUNDLE_VALIDATOR_PASS` | Configured EvidenceBundle checks passed. |
| `EVIDENCE_BUNDLE_VALIDATOR_FAIL` | One or more configured EvidenceBundle checks failed. |
| `CLAIM_SCOPE_MISSING` | Required claim scope is absent or unbounded. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef is absent. |
| `EVIDENCE_REF_UNRESOLVED` | EvidenceRef cannot resolve through accepted resolver/path. |
| `EVIDENCE_BUNDLE_SCHEMA_INVALID` | Candidate does not satisfy accepted EvidenceBundle schema. |
| `SOURCE_RECORDS_MISSING` | Required source records or source descriptors are absent. |
| `CITATION_CLOSURE_MISSING` | Required citations or citation-validation support are absent. |
| `RIGHTS_OR_SENSITIVITY_GAP` | Rights, sensitivity, redaction, aggregation, or access posture is incomplete. |
| `TRANSFORM_OR_DIGEST_GAP` | Transform, checksum, spec-hash, or schema linkage is incomplete. |
| `POLICY_OR_RELEASE_GAP` | Required PolicyDecision, ReviewRecord, ReleaseManifest, correction path, or rollback target is absent. |
| `EVIDENCE_STALE_OR_SUPERSEDED` | Evidence is stale, corrected, withdrawn, superseded, or embargoed for the requested use. |
| `EVIDENCE_BUNDLE_AS_RELEASE_DENIED` | Candidate treats bundle closure as release approval. |
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
tests/validators/evidence_bundle/
├── README.md
├── test_evidence_bundle_validator.py
└── fixtures/
    ├── valid_evidence_bundle_closure/
    ├── missing_claim_scope/
    ├── missing_evidence_ref/
    ├── unresolved_evidence_ref/
    ├── schema_invalid/
    ├── missing_source_records/
    ├── missing_citation_closure/
    ├── rights_or_sensitivity_gap/
    ├── policy_or_release_gap/
    └── generated_text_as_evidence_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/evidence_bundle
```

```bash
python tools/validators/evidence_bundle/validate_evidence_bundle.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_evidence_bundle.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared EvidenceBundle contracts, schemas, source descriptors, policy, proof, receipt, and release records rather than defining meaning locally.
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
| Review state | Draft README replacement for stray one-character EvidenceBundle validator file. |
| Next smallest safe change | Verify actual EvidenceBundle validator script path, schema binding, fixtures, resolver behavior, report destination, receipt emission, policy enforcement, release linkage, governed route behavior, and CI/runtime wiring before promoting this lane beyond draft. |
