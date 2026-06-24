<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-readme
title: contracts/runtime — Runtime Contract Semantics README
type: readme
version: v0.2
status: draft; semantic-contract-lane; runtime-boundary; governed-interface-aware
owners: OWNER_TBD — Runtime steward · API steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Release steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; runtime; semantic-contracts; governed-runtime; finite-outcomes; trust-membrane; no-executable-authority; no-public-bypass
tags: [kfm, contracts, runtime, README, semantic-contracts, decision-envelope, runtime-response-envelope, policy-decision, finite-outcomes, evidence-refs, policy-runtime, governed-api, trust-membrane, no-parallel-authority]
related:
  - ../README.md
  - ./decision_envelope.md
  - ./decision_envelope/README.md
  - ./DecisionEnvelope.md
  - ./runtime_response_envelope.md
  - ./policy_decision.md
  - ./layer_manifest.md
  - ../policy/policy_decision.md
  - ../release/promotion_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/runtime/
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../policy/runtime/
  - ../../fixtures/contracts/v1/runtime/
  - ../../tools/validators/
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai.md
  - ../../docs/atlas/master-api-surface.md
notes:
  - "Expanded from existing `contracts/runtime/README.md` stub."
  - "This README defines the runtime semantic-contract lane only; executable runtime/API behavior belongs in implementation roots and policy behavior belongs in `policy/runtime/`."
  - "Verified runtime objects include `decision_envelope.md` and `runtime_response_envelope.md`; some adjacent files remain scaffold/compatibility paths and are labeled accordingly."
  - "Contracts own meaning; schemas own shape; policy owns admissibility; runtime/API code owns execution; tests/fixtures prove enforceability."
  - "Rollback target for this expansion is previous blob SHA `d8c94bc1428e7ba07311631e3fc0f42eb85c1603`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/runtime

> Semantic contract lane for KFM runtime-facing envelopes and governed interface objects. Runtime contracts define what runtime objects mean; they do **not** implement API behavior, policy evaluation, UI rendering, map serving, AI generation, logging, or release publication.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Runtime: not executable" src="https://img.shields.io/badge/runtime-not__executable-critical">
  <img alt="Trust: governed interfaces" src="https://img.shields.io/badge/trust-governed__interfaces-green">
</p>

**Status:** draft / semantic-contract lane  
**Path:** `contracts/runtime/README.md`  
**Owning root:** `contracts/` — semantic object meaning only  
**Schema root:** `schemas/contracts/v1/runtime/`  
**Policy root:** `policy/runtime/`  
**Runtime/API authority:** implementation and API roots, not this folder  
**Truth posture:** CONFIRMED target stub replaced · CONFIRMED runtime schema paths exist for decision and response envelopes · CONFIRMED some runtime-adjacent files are scaffolds/compatibility aliases · NEEDS VERIFICATION for full runtime object roster, validator wiring, fixtures, policy behavior, API implementation, public-client tests, and CI enforcement

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Observed contract index](#observed-contract-index) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Runtime trust rules](#runtime-trust-rules) · [Finite outcomes](#finite-outcomes) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Scope

`contracts/runtime/` owns semantic Markdown contracts for runtime-facing object meaning.

Runtime contracts may describe:

- decision envelopes;
- runtime response envelopes;
- finite runtime outcomes;
- evidence refs carried to runtime clients;
- policy-family state reflected in runtime envelopes;
- runtime obligations and safe-display constraints;
- freshness, correction, withdrawal, and error posture visible to clients;
- trust-membrane objects that protect public surfaces from canonical/internal stores.

Runtime contracts do not execute runtime behavior.

> [!IMPORTANT]
> Public clients and normal UI surfaces must rely on governed runtime/API envelopes and released/cited artifacts. They must not read RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, direct source-system side effects, graph/vector internals, credentials, or direct model runtime output.

---

## Repo fit

| Responsibility | Correct home | Relationship to this README |
|---|---|---|
| Runtime object meaning | `contracts/runtime/` | This lane; semantic Markdown only. |
| DecisionEnvelope meaning | `contracts/runtime/decision_envelope.md` | Canonical inspected snake_case contract. |
| DecisionEnvelope folder pointer | `contracts/runtime/decision_envelope/README.md` | Compatibility/object-folder pointer. |
| DecisionEnvelope CamelCase alias | `contracts/runtime/DecisionEnvelope.md` | Compatibility pointer; not canonical. |
| RuntimeResponseEnvelope meaning | `contracts/runtime/runtime_response_envelope.md` | API-facing runtime response envelope contract. |
| Runtime PolicyDecision scaffold | `contracts/runtime/policy_decision.md` | Scaffold/compatibility; canonical inspected PolicyDecision is under `contracts/policy/`. |
| Runtime LayerManifest scaffold | `contracts/runtime/layer_manifest.md` | Scaffold/compatibility; layer meaning is governed elsewhere. |
| Machine shape | `schemas/contracts/v1/runtime/` | Runtime schema authority. |
| Runtime policy rules | `policy/runtime/` | Admissibility/rule authority. |
| Fixtures | `fixtures/contracts/v1/runtime/` | Runtime example/proof data. |
| Validators | `tools/validators/` | Validation implementation; verify per file. |
| Runtime/API implementation | apps/packages/API roots | Execution/transport behavior. |
| Receipts/proofs/logs | accepted receipt/proof/log homes | Auditable evidence, not contract prose. |

---

## Observed contract index

| File | Status in this session | Role |
|---|---|---|
| `README.md` | expanded from stub | Runtime contract-lane boundary. |
| `decision_envelope.md` | CONFIRMED existing canonical flat contract | DecisionEnvelope semantic contract. |
| `decision_envelope/README.md` | CONFIRMED object-folder compatibility pointer | Prevents folder from becoming duplicate authority. |
| `DecisionEnvelope.md` | CONFIRMED compatibility pointer after rewrite | Legacy/CamelCase alias to snake_case contract. |
| `runtime_response_envelope.md` | CONFIRMED existing proposed contract | Governed API-facing response envelope. |
| `policy_decision.md` | CONFIRMED scaffold | Needs review; avoid conflict with `contracts/policy/policy_decision.md`. |
| `layer_manifest.md` | CONFIRMED scaffold | Needs review; avoid conflict with data/release layer manifests. |

---

## Accepted contents

| Accepted content | Purpose | Required posture |
|---|---|---|
| Runtime object semantic contracts | Define runtime object meaning and anti-collapse rules. | Pair with schemas where implemented. |
| Compatibility pointers | Preserve legacy paths without duplicate authority. | Clearly point to canonical home. |
| Field semantics tables | Explain schema-paired fields. | Must not replace JSON Schema. |
| Runtime boundary notes | Explain what public clients can/cannot infer. | Must preserve trust membrane. |
| Validation notes | Identify schema/validator/fixture/policy gaps. | Mark unverified behavior NEEDS VERIFICATION. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| JSON Schema | `schemas/contracts/v1/runtime/` | Schemas own shape. |
| Runtime/API code | apps/packages/API roots | Runtime behavior is executable implementation, not contract prose. |
| Runtime policy rules | `policy/runtime/` | Policy owns admissibility and obligations. |
| Runtime payload instances | fixtures, logs, receipts, or accepted artifact homes | Contracts do not store operational records. |
| Receipts/proofs/logs | accepted receipt/proof/log homes | Audit artifacts remain separately inspectable. |
| Release manifests or promotion decisions | `contracts/release/` and `release/` | Release state is not runtime envelope state. |
| Public UI/map/AI implementation | UI/web/map/AI/runtime roots | Downstream rendering/execution. |
| Direct model output as truth | Governed AI envelopes with evidence/policy/release checks | AI is interpretive, not authority. |

---

## Runtime trust rules

1. **Contracts define meaning only.** They do not execute policy, runtime code, or API transport.
2. **Schemas define shape.** Field requirements and enums must be enforced in `schemas/contracts/v1/runtime/` and validators/tests.
3. **Policy decides admissibility.** Runtime envelopes may carry policy state, reasons, obligations, or policy-family context, but policy rules live under `policy/runtime/`.
4. **Finite outcomes are mandatory.** Runtime-facing decisions must avoid ambiguous success/failure language.
5. **Evidence refs are not evidence closure.** Evidence-bearing answers require resolvable evidence support and cite-or-abstain posture.
6. **Public clients are downstream.** UI/API/map/AI surfaces consume governed envelopes; they do not reach back into RAW/WORK/QUARANTINE/canonical stores.
7. **Correction and withdrawal state must flow forward.** Runtime envelopes must carry or reflect correction/withdrawal/staleness posture where public reliance could be unsafe.
8. **Compatibility paths must not become authority.** CamelCase aliases and object-folder READMEs remain pointers unless ADR/migration accepts a new canonical path.

---

## Finite outcomes

Runtime envelope outcome vocabularies observed in schema include:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

Recommended meaning boundary:

| Outcome | Runtime meaning | Client posture |
|---|---|---|
| `ANSWER` | The system may provide the requested answer/payload under current evidence/policy/release constraints. | Render with citations/obligations. |
| `ABSTAIN` | The system refuses to answer because evidence, policy, rights, sensitivity, freshness, or context is insufficient or unsafe. | Show abstention reason safely. |
| `DENY` | The system denies access/render/action under policy or governance rules. | Do not render restricted payload. |
| `ERROR` | Runtime could not complete safely or deterministically. | Show safe error; do not infer truth. |

Runtime outcome vocabulary is related to, but distinct from, release `PromotionDecision` vocabulary and policy-object semantics.

---

## Validation checklist

- [ ] Verify all runtime contract files have canonical/compatibility status clearly marked.
- [ ] Verify schema paths and `x-kfm.contract_doc` values point to canonical contract files.
- [ ] Verify validators named by schemas exist and are wired into test/CI flow.
- [ ] Verify fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes.
- [ ] Verify runtime policies produce safe obligations/reasons without leaking sensitive facts.
- [ ] Verify public API/UI/map/AI tests prove no direct RAW/WORK/QUARANTINE/internal-store access.
- [ ] Verify correction, withdrawal, stale, and rollback posture can propagate through runtime envelopes.
- [ ] Resolve scaffold files that may duplicate policy or layer contract authority.

---

## Open questions

- Should `contracts/runtime/policy_decision.md` become a compatibility pointer to `contracts/policy/policy_decision.md`?
- Should `contracts/runtime/layer_manifest.md` become a compatibility pointer to the data/release layer manifest contracts?
- Should runtime outcomes and policy decision outcomes share a vocabulary register?
- Which runtime contracts are public API contracts versus internal runtime envelopes?
- Which CI checks prove trust-membrane enforcement?

---

## Rollback

Rollback is required if this README is used to claim runtime implementation, API behavior, policy execution, public access permission, release state, proof/receipt authority, or AI truth without supporting schemas, policy, validators, tests, implementation evidence, and release governance.

Rollback target for this expansion: previous stub blob SHA `d8c94bc1428e7ba07311631e3fc0f42eb85c1603`.

<p align="right"><a href="#top">Back to top</a></p>
