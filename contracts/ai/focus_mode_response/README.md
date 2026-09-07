<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ai-focus-mode-response-readme
title: contracts/ai/focus_mode_response/ — Focus Mode Response Contract
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Governed AI steward · Contract steward · Schema steward · Policy steward · Evidence steward · API steward · UI steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; ai; focus-mode; response-contract; semantic-contract; finite-outcome; cite-or-abstain
related:
  - ../focus_mode_request/README.md
  - ../../focus_mode/focus_mode_payload.md
  - ../../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../../docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../schemas/contracts/v1/ai/
  - ../../../schemas/contracts/v1/focus/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../schemas/contracts/v1/evidence/
  - ../../../policy/focus/
  - ../../../apps/workers/src/ai_focus_worker/
  - ../../../tools/validators/
  - ../../../.github/workflows/
tags: [kfm, contracts, ai, governed-ai, focus-mode, focus-mode-response, runtime-response-envelope, evidence-bundle, policy-decision, citation-validation, ai-receipt, finite-outcome, cite-or-abstain, semantic-contract, governance]
notes:
  - "This README records semantic intent and current repository evidence; it is not a machine schema or a live Focus implementation."
  - "Focus-specific response schemas remain permissive PROPOSED scaffolds. The runtime, citation-report, and AIReceipt validators are bounded local proof surfaces, not authorization or publication systems."
  - "The Focus worker is a comment-only placeholder and no live Governed API Focus route or provider-backed transaction is registered."
  - "Google Drive doctrine corroborates evidence-first and trust-membrane principles; GitHub repository evidence controls paths, status, and implementation claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Focus Mode Response Contract

> Semantic contract for the meaning and trust boundary of a Focus Mode response. It describes a finite governed response envelope; it is not raw model output, a prompt result, a machine schema, an API route, a worker implementation, a released payload, or UI behavior.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Root: contracts/ai/focus_mode_response" src="https://img.shields.io/badge/root-contracts%2Fai%2Ffocus__mode__response-blue">
  <img alt="Subsystem: governed AI" src="https://img.shields.io/badge/subsystem-governed__AI-purple">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-orange">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-green">
</p>

\`contracts/ai/focus_mode_response/\`

## Quick jumps

[Status](#status) · [Scope and authority](#scope-and-authority) · [Current implementation snapshot](#current-implementation-snapshot) · [Response semantics](#response-semantics) · [Proposed gates](#proposed-gates) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Open verification](#open-verification) · [Rollback](#rollback)

---

## Status

> [!IMPORTANT]
> **Status:** \`draft\` / \`repository-grounded\` / \`implementation-bounded\`  
> **Path:** \`contracts/ai/focus_mode_response/\`  
> **Path posture:** the README path and file are confirmed; the canonical semantic/schema home is unresolved.  
> **Execution posture:** bounded fixture-first validators and client-local Focus proof exist; no live Governed API Focus route, provider adapter, or worker transaction is established.  
> **Authority posture:** local validation can prove declared shape and consistency only. It does not resolve evidence, execute policy, authenticate review, persist receipts, authorize a public answer, release, publish, or mutate lifecycle state.

This document is intentionally conservative. It keeps the intended Focus response semantics visible while separating them from repository facts that are still proposed, placeholder-only, or unimplemented.

---

## Scope and authority

The target directory owns the semantic meaning of a Focus Mode response:

- one finite outcome: \`ANSWER\`, \`ABSTAIN\`, \`DENY\`, or \`ERROR\`;
- evidence and citation boundaries for an \`ANSWER\`;
- safe reason handling for non-answer outcomes;
- separation between generated language, policy state, evidence state, receipts, release, and publication.

It does not own:

- JSON Schema or another machine-readable shape;
- prompt text or provider configuration;
- model adapter code;
- evidence resolution or EvidenceBundle storage;
- policy evaluation;
- API route or worker execution;
- AIReceipt persistence;
- UI rendering;
- release, rollback, or publication authority.

The authority split is deliberate:

| Surface | What it may establish | What it may not establish |
|---|---|---|
| This README | Semantic intent and trust boundaries. | Runtime readiness or schema enforcement. |
| JSON Schema | Machine shape, required fields, and closed-field behavior where the schema is closed. | Evidence truth, policy approval, release, or publication. |
| Local validator and fixtures | Deterministic local shape/fixture checks. | Evidence resolution, authenticated review, policy execution, or public-answer authority. |
| Policy bundle/evaluator | Policy decisions when an active evaluator exists. | Evidence truth or release by itself. |
| Runtime/API/worker | Executable composition when wired and independently tested. | Publication authority without release controls. |
| Receipt and review records | Traceability and review evidence. | Proof closure or permission to publish on their own. |

Do not select a canonical contract family by filename similarity. The repository currently contains parallel Focus, AI, runtime, evidence, and UI paths with different status and authority.

---

## Current implementation snapshot

The following is the repository-grounded state at the time of this update.

| Surface | Current state | Boundary |
|---|---|---|
| \`contracts/ai/focus_mode_response/README.md\` | This draft semantic contract. | Does not enforce a machine shape. |
| \`schemas/contracts/v1/ai/focus_mode_response.schema.json\` | \`PROPOSED\` permissive scaffold; empty \`properties\`, \`additionalProperties: true\`. | Not a closed Focus response schema. |
| \`schemas/contracts/v1/focus/focus_response.schema.json\` | \`PROPOSED\` permissive scaffold; empty \`properties\`, \`additionalProperties: true\`. | Not a closed Focus response schema. |
| \`schemas/contracts/v1/focus/runtime_response_envelope.schema.json\` | \`PROPOSED\` compatibility alias to the runtime envelope schema. | Not a second canonical machine shape. |
| \`schemas/contracts/v1/runtime/runtime_response_envelope.schema.json\` | \`PROPOSED\` but closed, with a validator and valid/invalid fixtures. | Bounded runtime-envelope proof; no live Focus route. |
| \`schemas/contracts/v1/evidence/citation_validation_report.schema.json\` | \`PROPOSED_FIXTURE_FIRST\`; closed report shape with a 27-case fixture suite. | Does not resolve citations or grant public-answer authority. |
| \`schemas/contracts/v1/runtime/ai_receipt.schema.json\` | \`PROPOSED\`; closed receipt shape with nine required fields. | No Focus receipt emitter or store is wired. |
| \`policy/focus/focus_response.rego\` | Package-only scaffold. | No active Focus response evaluator rules are established. |
| \`apps/workers/src/ai_focus_worker/main.py\` | Comment-only greenfield placeholder. | No executable worker, queue, schedule, health check, or emitted artifact. |
| \`docs/architecture/governed-ai/FOCUS_FLOW.md\` | Repository-grounded architecture hold. | Records no live Focus route, no provider integration, and no release/publication. |

The existence of a validator, fixture, or workflow is evidence of a bounded local check—not evidence that the full Focus transaction is live.

---

## Response semantics

A Focus Mode response is intended to be a governed envelope, never whatever a model provider returns. The target semantic rules are:

- exactly one finite outcome is present;
- \`ANSWER\` contains only claims supported by the evidence actually used;
- citations identify evidence that a CitationValidationReport can validate;
- \`ABSTAIN\` does not substitute unsupported claims for missing, stale, conflicting, or unresolved evidence;
- \`DENY\` is safe to display and does not leak restricted geometry, identities, source internals, or sensitive detail;
- \`ERROR\` is bounded and does not silently downgrade to \`ANSWER\`;
- policy postcheck occurs after candidate generation and before any user-facing display;
- an adapter invocation is traceable to a receipt when receipt infrastructure is actually wired;
- public clients consume governed envelopes, never raw provider output.

### Semantic outcome carriers

These fields describe the intended Focus response meaning. They are not currently enforced by either permissive Focus-specific schema.

| Outcome | Semantic content | Intended carrier fields |
|---|---|---|
| \`ANSWER\` | Cited answer supported by the evidence actually used. | \`answer_text\`, \`citations[]\`, \`evidence_used[]\`, policy decisions, citation report reference, and receipt linkage when an adapter was invoked. |
| \`ABSTAIN\` | Safe explanation of an evidence, freshness, conflict, or citation gap. | \`abstain_reason\`, optional evidence-gap detail, optional citation report reference, and receipt linkage when applicable. |
| \`DENY\` | Safe policy denial or restricted-scope response. | \`deny_reason\`, policy decision detail that is safe to disclose, and receipt linkage if an adapter ran before denial. |
| \`ERROR\` | Bounded operational or validation failure. | \`error_code\`, correlation/request identity, and no claim leakage. |

### Machine-carrier mismatch that must be resolved

The currently proposed machine contracts are separate families:

- RuntimeResponseEnvelope requires \`id\`, \`spec_hash\`, \`version\`, \`issued_at\`, \`outcome\`, \`reason_code\`, \`evidence_refs\`, \`policy_state\`, \`freshness\`, and \`correction_state\`; it optionally carries \`precision_actually_used\`.
- It does not currently carry \`answer_text\`, \`citations[]\`, \`ai_receipt_id\`, or an \`ai_receipt_ref\`.
- AIReceipt separately requires \`id\`, \`run_id\`, \`adapter\`, \`model_ref\`, \`inputs_digest\`, \`outputs_digest\`, \`policy_decision_ref\`, \`citation_validation_ref\`, and \`outcome\`.
- CitationValidationReport is a separate declaration/report family.

An implementation must choose and document an adapter or migration between these families. Do not silently merge the Focus semantic fields into RuntimeResponseEnvelope or treat one family as the authority of the others.

---

## Proposed gates

The intended orchestration is:

1. validate request scope and permitted operation;
2. run policy precheck;
3. resolve admissible EvidenceRef values to the EvidenceBundle actually used;
4. pass only bounded context to an approved adapter;
5. build a candidate with claim-to-evidence references;
6. produce and validate a CitationValidationReport;
7. run policy postcheck over the candidate;
8. record receipt linkage when the adapter/receipt path is wired;
9. validate the selected response carrier before user-facing use.

A failed gate maps to a finite outcome:

| Failure class | Safe outcome |
|---|---|
| Missing, stale, conflicting, or unresolved evidence | \`ABSTAIN\` |
| Scope or policy restriction | \`DENY\` |
| Tooling, validation, or composition failure | \`ERROR\` |

This is proposed orchestration, not a claim that the repository currently executes the sequence. The current citation validator explicitly does not perform evidence resolution, policy evaluation, review authentication, release verification, lifecycle mutation, publication, or public-answer authorization.

---

## Lifecycle

The following is the intended trust boundary, not a live route diagram:

~~~mermaid
flowchart TD
  A["Request and scope"] --> B["Policy precheck and evidence"]
  B --> C["Bounded adapter candidate"]
  C --> D["Citation validation"]
  D --> E["Policy postcheck"]
  E --> F["Finite response envelope"]
  F --> G["Receipt, review, release, and publication gates"]
~~~

No node in this diagram is established as a live Focus transaction by this README.

---

## Validation

Run the focused local checks from the repository root when changing the corresponding implementation surfaces:

~~~bash
KFM_NO_NETWORK=1 python -m pytest -q tests/validators/test_validate_citation_validation_report.py
KFM_NO_NETWORK=1 python tools/validators/citation/validate_citation_validation_report.py --fixtures

KFM_NO_NETWORK=1 python -m unittest tests.validators.test_validate_runtime_response_envelope -v
KFM_NO_NETWORK=1 python tools/validators/validate_runtime_response_envelope.py --fixtures

KFM_NO_NETWORK=1 python -m unittest tests.validators.test_validate_ai_receipt -v
KFM_NO_NETWORK=1 python tools/validators/validate_ai_receipt.py --fixtures
~~~

The repository also has focused citation-validation and runtime-response HTTP-binding workflows. Those workflows are fixture/declaration lanes with explicit no-network and no-publication boundaries; there is no dedicated end-to-end Focus response workflow.

A green local check proves only the bounded assertion covered by that validator or fixture suite. It does not prove evidence closure, model approval, policy execution, route health, receipt persistence, independent review, release, or publication.

---

## Evidence basis

| Repository evidence | What it supports | Important limit |
|---|---|---|
| \`docs/architecture/governed-ai/FOCUS_FLOW.md\` | Focus architecture status, finite outcomes, fixture-first client proof, and the no-live-route/no-release hold. | Architecture is not runtime wiring. |
| \`schemas/contracts/v1/runtime/runtime_response_envelope.schema.json\` and \`tools/validators/validate_runtime_response_envelope.py\` | A proposed, closed runtime envelope and bounded local validator/fixture lane. | No Focus-specific field convergence or live route. |
| \`schemas/contracts/v1/evidence/citation_validation_report.schema.json\`, \`contracts/evidence/citation_validation_report.md\`, and \`tools/validators/citation/validate_citation_validation_report.py\` | Proposed fixture-first citation declaration/report surface and explicit validator limits. | No evidence resolution, policy/review/release/publication authority. |
| \`schemas/contracts/v1/runtime/ai_receipt.schema.json\`, \`contracts/runtime/ai_receipt.md\`, and \`tools/validators/validate_ai_receipt.py\` | Proposed receipt shape and bounded local consistency checks. | No emitter, store, or authorization effect. |
| \`schemas/contracts/v1/ai/focus_mode_response.schema.json\` and \`schemas/contracts/v1/focus/focus_response.schema.json\` | Focus-specific schema paths exist. | Both remain permissive \`PROPOSED\` scaffolds, not enforceable response contracts. |
| \`policy/focus/focus_response.rego\` | Focus policy path exists. | Current file is package-only; no active evaluator rules are established. |
| \`apps/workers/src/ai_focus_worker/README.md\` and \`main.py\` | Focus worker lane is documented as placeholder-only. | No executable worker or live route. |
| \`contracts/focus_mode/focus_mode_payload.md\` | Older semantic Focus payload family exists. | It is not automatically the authority for this response envelope. |
| Google Drive: *Kansas Frontier Matrix — AI Build Operating Contract* | Corroborating evidence-first, finite-outcome, trust-membrane, and publication-separation doctrine. | Drive doctrine does not establish GitHub paths, schema status, runtime wiring, or release readiness. |

---

## Open verification

The contract is not complete until the following are independently resolved and evidenced:

- [ ] Owners replace \`OWNER_TBD\` for semantic contract, schema, policy, evidence, API, UI, and release responsibilities.
- [ ] An ADR or migration note resolves the canonical semantic and machine-contract homes.
- [ ] Focus response semantics are reconciled with RuntimeResponseEnvelope, CitationValidationReport, and AIReceipt without silently merging object families.
- [ ] A strict, accepted Focus response schema or an explicit adapter to an accepted runtime envelope exists.
- [ ] EvidenceBundle resolution, citation validation, and policy pre/postcheck are executable and tested together.
- [ ] A live Governed API Focus route and worker/provider integration exist with health, error, and rollback behavior.
- [ ] AIReceipt emission, persistence, and linkage are implemented; receipt presence is not mistaken for proof closure.
- [ ] API and UI surfaces consume only governed envelopes and never raw provider output.
- [ ] Independent review, release, publication, and rollback evidence exists for any public surface.
- [ ] CI covers the accepted Focus contract path and fails closed on schema, citation, policy, and outcome regressions.

---

## Rollback

This update is documentation-only. Revert the single README commit to roll it back; no schema, policy, worker, runtime, receipt, release, or source-of-truth file was changed, and no target-specific receipt was found or updated.

---

## Status summary

\`contracts/ai/focus_mode_response/\` is a draft, repository-grounded semantic contract directory. It records the intended finite outcome and evidence/policy trust boundaries while keeping current implementation limits explicit: Focus-specific schemas are permissive proposed scaffolds, runtime/citation/receipt validators are bounded local proof surfaces, the Focus worker is a placeholder, and no live Focus route or provider-backed transaction is established.

<p align="right"><a href="#top">Back to top</a></p>
