<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-focus-readme
title: Focus Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; focus-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Governed AI steward
  - OWNER_TBD - Focus Mode steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; focus; governed-ai; synthetic-only; no-network; public-safe; evidence-bound; citation-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, focus, FocusModeRequest, FocusModeResponse, RuntimeResponseEnvelope, ANSWER, ABSTAIN, DENY, ERROR, EvidenceRef, EvidenceBundle, CitationValidationReport, PolicyDecision, AIReceipt, governed-ai, no-network]
related:
  - ../README.md
  - ../../README.md
  - ../../runtime_proof/README.md
  - ../../ui/README.md
  - ../../api/README.md
  - ../../../docs/architecture/governed-ai/README.md
  - ../../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../../docs/architecture/governed-ai/BOUNDARIES.md
  - ../../../docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - ../../../docs/architecture/governed-ai/MOCK_FIRST.md
  - ../../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../schemas/contracts/v1/focus/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../schemas/contracts/v1/evidence/
  - ../../../policy/focus/
  - ../../../policy/domains/
  - ../../../contracts/runtime/
  - ../../../contracts/evidence/
  - ../../../data/receipts/ai/
  - ../../../data/proofs/evidence_bundle/
  - ../../../release/candidates/
notes:
  - "This README replaces placeholder content at tests/fixtures/focus/README.md."
  - "This lane documents unit-test-scoped Focus Mode fixtures. It does not become a canonical truth, evidence, policy, release, or public artifact root."
  - "Focus fixtures must exercise the governed request → policy → evidence → adapter → citation → policy → envelope path; no browser-to-model shortcut is allowed."
  - "Executable tests, fixture payload inventory, schema bindings, runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Focus test fixtures

> Test-local fixture documentation for Focus Mode examples under `tests/fixtures/focus/`. This lane supports deterministic, no-network fixtures for governed Focus request/response behavior without turning examples into evidence truth, policy approval, release approval, public map material, or AI authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: focus fixtures" src="https://img.shields.io/badge/lane-focus__fixtures-purple">
  <img alt="Subsystem: governed AI" src="https://img.shields.io/badge/subsystem-governed__AI-blueviolet">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/focus/README.md`  
**Status:** draft / placeholder replaced / Focus test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/focus`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/README.md` names `tests/fixtures/focus/answer.valid.json`, `abstain_uncited.invalid.json`, and `deny_restricted.valid.json` as proposed Focus fixture examples; CONFIRMED Focus Flow identifies `tests/fixtures/focus/` as the proposed Focus fixture home; NEEDS VERIFICATION for executable tests, fixture payload inventory, schema bindings, runtime wiring, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/focus/` is the unit-test-scoped fixture lane for Focus Mode request/response examples.

Use this lane for synthetic fixtures that exercise the governed Focus path:

1. request scope is defined;
2. policy precheck runs;
3. `EvidenceRef` values resolve to admissible `EvidenceBundle`s;
4. the model adapter receives only bounded, admissible context;
5. citations are validated;
6. policy postcheck runs;
7. a finite `RuntimeResponseEnvelope` is returned;
8. `AIReceipt` and related refs are recorded as process memory, not proof of release.

A Focus fixture should not mean that a claim is true, a source is authoritative, a release is approved, a policy decision is binding, an AI answer is sovereign, or a public artifact exists. It should mean only that a bounded synthetic input is expected to produce a bounded Focus outcome.

[Back to top](#top)

---

## Placement basis

`tests/README.md` identifies `tests/fixtures/` as an optional home for unit-test-scoped fixtures and gives Focus examples under `tests/fixtures/focus/`. The governed-AI Focus Flow also lists `tests/fixtures/focus/` as the proposed fixture surface for Focus. This path is therefore a test-local fixture lane, not a cross-cutting reusable fixture root and not a publication surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Focus unit-test fixtures | `tests/fixtures/focus/` | This directory. |
| Runtime-proof tests | `tests/runtime_proof/` or focused consumer tests | Expected executable consumers; not fixture authority. |
| Governed API tests | `tests/api/` | Expected consumer lane for API envelope behavior. |
| UI trust-state tests | `tests/ui/` | Expected consumer lane for Focus/Evidence Drawer rendering. |
| Focus schemas | `schemas/contracts/v1/focus/` | Defines machine shape; not owned here. |
| Runtime envelope schemas | `schemas/contracts/v1/runtime/` | Defines finite envelope shape; not owned here. |
| Evidence schemas/contracts | `schemas/contracts/v1/evidence/` and `contracts/evidence/` | Defines evidence support shape and meaning; not owned here. |
| Policy authority | `policy/focus/` and domain policy roots | Referenced by expected outcomes; not defined here. |
| AI receipts | `data/receipts/ai/` | Process memory; referenced by synthetic refs only. |
| Evidence proof | `data/proofs/evidence_bundle/` and accepted proof roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a second schema, policy, evidence, receipt, release, model-output, or public API home. Fixtures here are test carriers only.

---

## Invariant under test

> **Focus Mode answers are governed outputs, not model outputs.** A Focus fixture must prove that generated language never outranks evidence, policy, citation validation, review state, or release state.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Finite-outcome boundary | Every fixture expects exactly one of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. | validation failure. |
| No-browser-to-model boundary | Fixtures never model a direct browser-to-model shortcut. | `DENY` / validation failure. |
| No-network boundary | Default fixtures do not call live sources, public APIs, model providers, map services, or release services. | `ERROR`. |
| Evidence boundary | Claim-like `ANSWER` fixtures require resolvable synthetic EvidenceRefs or explicitly abstain. | `ABSTAIN`. |
| Citation boundary | Every claim span in an `ANSWER` fixture has citation-validation expectations. | `ABSTAIN` / validation failure. |
| Policy precheck boundary | Rights, sensitivity, release state, role, scope, and user context can terminate before evidence retrieval. | `DENY` / `ABSTAIN` / `ERROR`. |
| Policy postcheck boundary | Proposed answer text is checked for leakage, obligations, attribution, and release/correction consistency. | `DENY`. |
| Sensitive-data boundary | Exact restricted geometry, living-person data, DNA/genomic material, archaeology, rare-species locations, or critical-infrastructure details fail closed. | `DENY`. |
| Receipt boundary | `AIReceipt` references process memory and does not become release proof. | validation failure. |
| Release boundary | Fixture success does not authorize publication, correction, withdrawal, or rollback. | promotion block. |

---

## Expected fixture families

| Family | Purpose | Expected outcome |
|---|---|---|
| `answer.valid` | Public-safe request with resolved evidence, passing policy, passing citations, and release-allowed state. | `ANSWER`. |
| `abstain_uncited.invalid` | Claim request where evidence or citations do not close. | `ABSTAIN`. |
| `abstain_missing_evidence` | EvidenceRef does not resolve to a usable EvidenceBundle. | `ABSTAIN`. |
| `deny_restricted.valid` | Policy denies because rights, sensitivity, release state, or role blocks exposure. | `DENY`. |
| `deny_sensitive_geometry` | Request would expose exact restricted geometry or sensitive location. | `DENY`. |
| `deny_direct_model_path` | Fixture attempts browser/model shortcut or direct model runtime use. | `DENY` / validation failure. |
| `error_malformed_request` | Request envelope is malformed or violates schema. | `ERROR`. |
| `error_adapter_contract` | Adapter result lacks required structure or citation anchors. | `ERROR` / `ABSTAIN` depending on consumer. |
| `correction_visible` | Released answer should display correction or withdrawal context. | `ANSWER` / `ABSTAIN` / `DENY` as policy dictates. |
| `rollback_visible` | Runtime response shows rollback-safe state after release reversal. | finite outcome only. |

---

## Accepted material

Only bounded, synthetic, reviewable material belongs in this lane:

- small Focus request and response fixture examples
- synthetic `FocusModeRequest`, `FocusModeResponse`, `RuntimeResponseEnvelope`, `MapContextEnvelope`, `EvidenceRef`, `EvidenceBundle`, `CitationValidationReport`, `PolicyDecision`, `AIReceipt`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- expected-output examples for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`
- negative canaries for uncited claims, missing evidence, sensitive leak attempts, policy denial, schema failure, adapter contract failure, direct model path, and public-read bypass
- toy map-context scopes, toy evidence refs, toy layer refs, toy feature refs, toy timestamps, toy hashes, and toy policy refs
- local manifests that point to reusable fixtures elsewhere when needed

Safe outputs may include fixture ID, route or surface name, expected outcome, expected reason code, evidence refs, citation report refs, policy decision refs, AI receipt refs, release refs, correction refs, rollback refs, and expected UI limits.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Live model outputs, private chain-of-thought, prompts with secrets, provider credentials, telemetry, or access tokens | Security and governance risk. |
| Exact sensitive geometry, living-person identifiers, DNA/genomic data, rare-species coordinates, archaeology site geometry, or critical-infrastructure detail | Sensitive material must fail closed and be represented only by synthetic denial canaries. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, public APIs, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/focus/
|-- README.md
|-- answer.valid.json
|-- abstain_uncited.invalid.json
|-- abstain_missing_evidence.valid.json
|-- deny_restricted.valid.json
|-- deny_sensitive_geometry.valid.json
|-- deny_direct_model_path.invalid.json
|-- error_malformed_request.invalid.json
|-- error_adapter_contract.invalid.json
|-- correction_visible.valid.json
|-- rollback_visible.valid.json
`-- expected_reason_codes.json
```

This layout is PROPOSED until executable files and consumers exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/runtime_proof tests/api tests/ui tests/fixtures/focus
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no direct model runtime calls, no real secrets, no production logs, no production trust artifacts, no exact sensitive locations, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

---

## Minimal Focus fixture manifest

Synthetic manifests should describe fixture expectations without carrying real evidence or model output.

```json
{
  "fixture_manifest_id": "focus-answer-public-safe-example",
  "fixture_family": "answer_valid",
  "runtime_surface": "focus_mode",
  "expected_outcome": "ANSWER",
  "focus_request_ref": "focus:synthetic:request:public-safe-example",
  "evidence_refs": [
    "evidence:synthetic:bundle:public-safe-example"
  ],
  "citation_validation_ref": "citation:synthetic:focus:public-safe-example",
  "policy_decision_ref": "policy:synthetic:focus:allow-public-safe-example",
  "ai_receipt_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "uses_live_model": false,
  "authorizes_publication": false
}
```

For denial cases, make the denial explicit without carrying the restricted value:

```json
{
  "fixture_manifest_id": "focus-deny-sensitive-geometry-example",
  "fixture_family": "deny_sensitive_geometry",
  "runtime_surface": "focus_mode",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SENSITIVE_GEOMETRY_BLOCKED",
    "POLICY_DENY"
  ],
  "policy_decision_ref": "policy:synthetic:focus:deny-sensitive-geometry",
  "ai_receipt_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "uses_live_model": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `ANSWER` | Evidence resolves, policy allows, release/review state permits, citations validate, and postcheck allows. | Public-safe summary with citation refs and AIReceipt ref. |
| `ABSTAIN` | Evidence is missing, stale, conflicted, uncited, or insufficient to support a claim. | Uncited claim fixture. |
| `DENY` | Rights, sensitivity, release state, user role, or policy forbids the response. | Restricted geometry request. |
| `ERROR` | Request, schema, resolver, adapter, fixture, or infrastructure contract is malformed or unavailable. | Malformed FocusModeRequest. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, public-safe, and no-network
- [ ] every fixture declares exactly one expected outcome
- [ ] `ANSWER` fixtures include evidence, citation, policy, release/review, and AIReceipt expectations
- [ ] `ABSTAIN` fixtures state the missing or insufficient support
- [ ] `DENY` fixtures do not expose blocked restricted values
- [ ] `ERROR` fixtures distinguish malformed/infrastructure failure from policy denial
- [ ] no fixture models a browser-to-model shortcut or direct public read of internal stores
- [ ] no real source records, live model outputs, secrets, logs, exact sensitive geometry, or production artifacts are present
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, policies, and runtime consumers are updated when Focus behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add an `ANSWER` fixture | Include EvidenceRef, CitationValidationReport, PolicyDecision, release/review posture, and AIReceipt expectations. |
| Add an `ABSTAIN` fixture | State the missing evidence, stale evidence, citation failure, conflict, or unsupported scope. |
| Add a `DENY` fixture | State the policy/sensitivity/release/user-role reason without exposing the restricted value. |
| Add an `ERROR` fixture | Make the malformed request, schema failure, resolver failure, or adapter contract failure explicit. |
| Add cross-domain context | Keep the owning domain's authority external and cited by synthetic refs. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Focus fixture path: verified as proposed in `docs/architecture/governed-ai/FOCUS_FLOW.md` and example fixture names in `tests/README.md`.
- Fixture payload inventory: not exhaustively verified in this update.
- Focus Flow alignment: verified against `docs/architecture/governed-ai/FOCUS_FLOW.md` for request → policy → evidence → adapter → citation → policy → envelope flow, finite outcomes, no browser-to-model shortcut, citation validation, policy postcheck, and AIReceipt posture.
- Test-root alignment: verified against `tests/README.md` for tests as enforceability proof, optional `tests/fixtures/` split, five-fixture rule, forbidden boundaries, and deterministic no-network default.
- Contract/schema alignment: NEEDS VERIFICATION against Focus, runtime, evidence, and policy schemas.
- Consumer alignment: NEEDS VERIFICATION against runtime-proof tests, governed-API tests, UI trust-state tests, Evidence Drawer checks, Focus Mode checks, citation-validation checks, policy checks, release-state checks, rollback drills, and CI coverage.
- Tests and validators: NOT RUN.
