<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-ai-evidence-before-model-readme
title: tools/validators/ai/evidence_before_model README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-governed-ai-steward-plus-evidence-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; ai-validator-lane; evidence-before-model
owning_root: tools/
responsibility: proposed AI validator lane for enforcing evidence resolution, policy precheck, released-context assembly, citation validation, and finite outcome requirements before or around model use
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../../../docs/architecture/governed-ai.md
  - ../../../../docs/architecture/governed-ai/AI_RECEIPTS.md
  - ../../../../docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - ../../../../docs/architecture/governed-ai/BOUNDARIES.md
  - ../../../../contracts/runtime/ai_receipt.md
  - ../../../../contracts/runtime/runtime_response_envelope.md
  - ../../../../contracts/evidence/evidence_ref.md
  - ../../../../contracts/evidence/citation_validation_report.md
  - ../../../../data/proofs/evidence_bundle/
  - ../../../../data/receipts/ai/
  - ../../../../policy/ai/
  - ../../../../runtime/model_adapters/
notes:
  - "This README documents a proposed AI validator lane. It does not confirm executable files."
  - "The validator checks that evidence and policy gates precede model interpretation. It does not call the model, create EvidenceBundles, approve policy, publish answers, or store private chain-of-thought."
  - "A valid AI answer is downstream of resolved evidence, policy-safe context, structured output validation, citation validation, post-policy check, and AIReceipt/RunReceipt capture."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/ai/evidence_before_model

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-evidence--before--model-informational)
![ai](https://img.shields.io/badge/AI-interpretive--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/ai/evidence_before_model/` is the proposed validator lane for checking that AI-facing requests and responses preserve KFM's evidence-first sequence: policy precheck, EvidenceRef resolution, policy-safe context assembly, model interpretation, citation validation, post-policy check, finite outcome, and receipt capture.

---

## Purpose

KFM allows AI to interpret governed evidence. It does not allow AI to become root truth.

This validator lane exists to check whether an AI request, runtime envelope, or Focus Mode flow proves that required evidence and policy gates happened before model output was treated as answerable.

The durable KFM question for this lane is:

> Did the AI flow resolve required evidence and policy context before model interpretation, and did the output remain bounded by citations, policy checks, finite outcomes, and receipts?

The answer should be a deterministic validation result. It should not call the model, generate an answer, create evidence, approve release, or publish anything.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/ai/evidence_before_model/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executable | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Governed-AI rule | **CONFIRMED in repo evidence / draft** | AI is interpretive and must use released, policy-safe EvidenceBundle context. |
| Required AI flow | **CONFIRMED in repo evidence / draft** | Policy precheck, EvidenceRef resolution, released context assembly, adapter call, citation validation, postcheck, receipt capture, and finite outcome are documented. |
| AIReceipt contract use | **PROPOSED / NEEDS VERIFICATION** | Contract paths and schema wiring require implementation verification. |
| Citation validation wiring | **PROPOSED / NEEDS VERIFICATION** | Validator should check references, not invent citation truth. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Evidence-before-model validator entrypoint | `tools/validators/ai/evidence_before_model/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Governed-AI architecture | `docs/architecture/governed-ai.md` and related docs |
| Runtime/AI contracts | `contracts/runtime/`, `contracts/ai/`, `contracts/evidence/` |
| Runtime/AI schemas | `schemas/contracts/v1/runtime/`, `schemas/contracts/v1/ai/`, or accepted schema homes |
| AI policy rules | `policy/ai/` |
| EvidenceBundle instances | `data/proofs/evidence_bundle/` or accepted proof lane |
| AIReceipt instances | `data/receipts/ai/` |
| Model adapters | `runtime/model_adapters/` |
| Tests and fixtures | `tests/validators/ai/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared contracts/schemas/policy and is fixture-tested.
- **NEEDS VERIFICATION:** exact executable names, current fixtures, schema paths, CI wiring, and runtime envelope shape.
- **DENY:** using this folder as a model adapter, evidence store, policy root, receipt store, answer generator, release surface, or public API.

[Back to top](#top)

---

## What belongs here

Good fits for this validator lane include checks for:

- required `EvidenceRef` inputs before model use;
- resolved `EvidenceBundle` references before answerable output;
- policy precheck recorded before context assembly;
- released or otherwise authorized context assembly only;
- no RAW, WORK, QUARANTINE, or internal canonical-store bytes in public AI context;
- provider-neutral adapter call only after bounded context exists;
- structured runtime response envelope;
- citation validation result for claims;
- policy postcheck after model output;
- finite outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- AIReceipt and RunReceipt references where required;
- no private chain-of-thought persisted as evidence.

[Back to top](#top)

---

## What does not belong here

| Do not put in this lane | Correct home |
|---|---|
| Model adapter implementation | `runtime/model_adapters/` |
| AI policy rules | `policy/ai/` |
| Runtime or evidence contracts | `contracts/runtime/`, `contracts/evidence/`, `contracts/ai/` |
| Runtime schemas | `schemas/contracts/v1/runtime/`, `schemas/contracts/v1/ai/` |
| EvidenceBundle instances | `data/proofs/evidence_bundle/` |
| AIReceipt instances | `data/receipts/ai/` |
| Public API routes | `apps/governed-api/` |
| Generated answers | governed runtime outputs, not validator code |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `EVIDENCE_BEFORE_MODEL_PASS` | Required evidence and policy gates appear in the correct order. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef is absent. |
| `EVIDENCE_BUNDLE_UNRESOLVED` | Required EvidenceBundle is missing or unresolved. |
| `POLICY_PRECHECK_MISSING` | Model path begins without a recorded policy precheck. |
| `UNAUTHORIZED_CONTEXT` | Context includes material outside released or authorized bounds. |
| `CITATION_VALIDATION_MISSING` | Output claims lack citation validation. |
| `POLICY_POSTCHECK_MISSING` | Output lacks policy postcheck. |
| `INVALID_AI_OUTCOME` | Runtime envelope outcome is not an accepted finite outcome. |
| `AI_RECEIPT_MISSING` | Required AIReceipt pointer is absent. |
| `PRIVATE_COT_PERSISTED` | Payload appears to persist hidden reasoning as evidence or proof. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/ai/evidence_before_model/
├── README.md
├── test_evidence_before_model.py
└── fixtures/
    ├── valid_answer_flow/
    ├── missing_evidence_ref/
    ├── unresolved_bundle/
    ├── missing_policy_precheck/
    ├── unauthorized_context/
    ├── missing_citation_validation/
    └── private_cot_persisted/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/ai/evidence_before_model
```

```bash
python tools/validators/ai/evidence_before_model/validate_evidence_before_model.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_evidence_before_model.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator checks evidence resolution before model use.
- [ ] Validator checks policy precheck before context assembly.
- [ ] Validator checks context is released or authorized.
- [ ] Validator checks citation validation before `ANSWER`.
- [ ] Validator checks policy postcheck after model output.
- [ ] Validator checks finite outcome envelope.
- [ ] Validator checks AIReceipt / RunReceipt pointers where required.
- [ ] Validator rejects private chain-of-thought as evidence/proof material.
- [ ] Validator reads contracts, schemas, and policy rather than defining them locally.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify runtime envelope contracts, AIReceipt schema, policy fixtures, and citation-validation report fixtures before wiring CI. |
