<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-ai-readme
title: tools/validators/ai README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-governed-ai-steward-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; ai-validator-parent; governed-ai
owning_root: tools/
responsibility: parent boundary and index for AI validators that enforce evidence-first, policy-aware, finite-outcome, receipt-backed model use
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ./evidence_before_model/README.md
  - ../../../docs/architecture/governed-ai.md
  - ../../../docs/architecture/governed-ai/AI_RECEIPTS.md
  - ../../../docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - ../../../docs/architecture/governed-ai/BOUNDARIES.md
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../contracts/ai/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../schemas/contracts/v1/ai/
  - ../../../policy/ai/
  - ../../../runtime/model_adapters/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/ai/
notes:
  - "This README documents the parent AI validator lane. It does not confirm executable files."
  - "AI validators check governed-AI envelopes and evidence/policy/citation/receipt ordering. They do not call models, generate answers, create EvidenceBundles, define policy, approve release, or publish public output."
  - "AI is interpretive in KFM. EvidenceBundle, policy decisions, citation validation, finite outcomes, and receipts outrank generated language."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/ai

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-AI--validators-informational)
![ai](https://img.shields.io/badge/AI-interpretive--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/ai/` is the parent validator lane for governed-AI checks: evidence-before-model ordering, policy pre/post checks, bounded context, structured runtime envelopes, citation validation, finite outcomes, and AIReceipt/RunReceipt presence.

---

## Purpose

`tools/validators/ai/` exists to hold AI-specific validator lanes under `tools/validators/`.

The durable KFM question for this parent lane is:

> Did an AI-facing request, response, receipt, or runtime envelope preserve KFM's evidence-first and policy-aware trust membrane?

The answer should be a deterministic validation result. It should never be model output, evidence truth, policy approval, release approval, or a public answer.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/ai/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| AI validator parent lane | **PROPOSED / draft** | Parent boundary and child index are documented here. |
| `evidence_before_model/` child lane | **CONFIRMED README / executable PROPOSED** | First documented child validator lane. |
| AI validator executables | **PROPOSED / NEEDS VERIFICATION** | No executable is claimed here. |
| Governed-AI doctrine | **CONFIRMED in repo evidence / draft** | AI may interpret released, policy-safe evidence and must return finite outcomes. |
| Runtime contracts and schemas | **PROPOSED / NEEDS VERIFICATION** | Contract and schema paths must be checked before implementation claims. |
| Policy and citation wiring | **PROPOSED / NEEDS VERIFICATION** | This parent README does not prove policy or citation validators are wired in CI. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| AI validator parent/index | `tools/validators/ai/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Evidence-before-model validator | `tools/validators/ai/evidence_before_model/` |
| Governed-AI architecture | `docs/architecture/governed-ai.md` and related docs |
| Runtime and AI contracts | `contracts/runtime/`, `contracts/ai/`, `contracts/evidence/` |
| Runtime and AI schemas | `schemas/contracts/v1/runtime/`, `schemas/contracts/v1/ai/`, or accepted schema homes |
| AI policy rules | `policy/ai/` |
| EvidenceBundle instances | `data/proofs/evidence_bundle/` or accepted proof lane |
| AIReceipt instances | `data/receipts/ai/` |
| Model adapters | `runtime/model_adapters/` |
| Public API exposure | `apps/governed-api/` |
| Tests and fixtures | `tests/validators/ai/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED:** the `evidence_before_model/` child README exists.
- **PROPOSED:** additional AI validator lanes may live here when they validate declared contracts, schemas, policy, and governed-AI doctrine.
- **NEEDS VERIFICATION:** exact executable names, schema paths, fixture locations, CI wiring, and runtime envelope maturity.
- **DENY:** using this folder as model runtime, model adapter, evidence store, policy root, receipt store, answer generator, release authority, or public API.

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `evidence_before_model/` | Did policy precheck, EvidenceRef resolution, policy-safe context assembly, citation validation, policy postcheck, finite outcome, and receipt capture occur in the required order? | README confirmed; executable proposed. |

Future child lanes should be named for the invariant they validate, not for a model provider or UI feature. Provider-specific adapter behavior belongs under runtime adapter tests unless the invariant is cross-provider and governed by contracts/policy.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/ai/` include validators that check:

- evidence-before-model ordering;
- AIReceipt presence and required references;
- RuntimeResponseEnvelope finite outcome shape;
- citation validation presence for answer claims;
- policy precheck and postcheck references;
- bounded context source restrictions;
- no direct RAW, WORK, QUARANTINE, or canonical-store exposure to public AI context;
- no provider-specific bypass of governed API;
- no private chain-of-thought persisted as evidence or proof;
- prompt contract hash and output envelope hash references where required.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/ai/` | Correct home |
|---|---|
| Model adapter implementations | `runtime/model_adapters/` |
| AI policy rules | `policy/ai/` |
| AI/runtime/evidence contracts | `contracts/ai/`, `contracts/runtime/`, `contracts/evidence/` |
| AI/runtime schemas | `schemas/contracts/v1/ai/`, `schemas/contracts/v1/runtime/` |
| EvidenceBundle instances | `data/proofs/evidence_bundle/` |
| AIReceipt instances | `data/receipts/ai/` |
| Public AI routes | `apps/governed-api/` |
| Generated AI answers | governed runtime output surfaces, not validator code |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `AI_VALIDATION_PASS` | Configured AI validator checks passed. |
| `AI_VALIDATION_FAIL` | Configured AI validator checks failed. |
| `EVIDENCE_REF_MISSING` | Required evidence reference is absent. |
| `EVIDENCE_BUNDLE_UNRESOLVED` | Required evidence bundle is unresolved. |
| `POLICY_CHECK_MISSING` | Required policy precheck or postcheck reference is absent. |
| `CITATION_VALIDATION_MISSING` | Required citation validation reference is absent. |
| `INVALID_RUNTIME_ENVELOPE` | Runtime response envelope does not match accepted contract/schema. |
| `INVALID_AI_OUTCOME` | Outcome is not accepted by the runtime envelope. |
| `AI_RECEIPT_MISSING` | Required AIReceipt pointer is absent. |
| `UNAUTHORIZED_CONTEXT` | Context appears outside released or authorized bounds. |
| `PRIVATE_COT_PERSISTED` | Payload appears to persist hidden reasoning as evidence or proof. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/ai/
├── README.md
├── test_ai_validator_index.py
├── evidence_before_model/
│   ├── README.md
│   ├── test_evidence_before_model.py
│   └── fixtures/
└── fixtures/
    ├── valid_runtime_envelope/
    ├── missing_ai_receipt/
    ├── invalid_outcome/
    └── unauthorized_context/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/ai
```

> [!NOTE]
> This is a proposed validation surface, not proof that `tests/validators/ai/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared AI/runtime/evidence contracts rather than defining them locally.
- [ ] Validator reads declared schemas rather than inlining shape rules.
- [ ] Validator reads policy posture rather than defining policy locally.
- [ ] Validator checks finite outcomes.
- [ ] Validator checks evidence and citation support before `ANSWER`.
- [ ] Validator checks AIReceipt / RunReceipt pointers where required.
- [ ] Validator rejects hidden reasoning persisted as evidence/proof material.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft parent README replacement for empty file. |
| Next smallest safe change | Add `tests/validators/ai/README.md`, then verify runtime envelope schemas, AIReceipt fixtures, citation validation fixtures, and CI wiring. |
