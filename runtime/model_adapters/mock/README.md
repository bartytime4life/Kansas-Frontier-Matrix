# `runtime/model_adapters/mock/` — Mock Model Adapter Lane

Mock-only model adapter lane for deterministic KFM runtime tests, fixture-backed adapter behavior, and mock-to-live migration notes. This path is not a live model provider, not evidence authority, not policy authority, and not release authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-model-adapters-mock-readme
title: runtime/model_adapters/mock/README.md — Mock Model Adapter Lane
type: readme; directory-readme; runtime-adapter-guardrail; mock-adapter-index
version: v0.1
status: draft; empty-path-expanded; mock-only; no-direct-implementation-confirmed; NEEDS VERIFICATION
owners: OWNER_TBD — Runtime steward · Governed-AI steward · Test steward · Policy steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-05
policy_label: public; runtime; model-adapter; mock; deterministic-tests; no-provider-authority
tags: [kfm, runtime, model-adapters, mock, governed-ai, finite-outcomes, ai-receipt, runtime-envelope, deterministic-tests]
related:
  - ../README.md
  - ../../mock/README.md
  - ../../AI/README.md
  - ../../envelopes/README.md
  - ../../../fixtures/
  - ../../../tests/
  - ../../../tools/validators/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../policy/
  - ../../../data/
  - ../../../release/
notes:
  - "Expanded from an empty runtime/model_adapters/mock/README.md."
  - "Current-session search found no direct files under runtime/model_adapters/mock/ beyond this README."
  - "runtime/model_adapters/ is the inspected provider-neutral model adapter lane."
  - "runtime/mock/ is the inspected deterministic mock runtime lane."
  - "This README does not prove adapter implementation, test coverage, fixture coverage, AIReceipt emission, RuntimeResponseEnvelope behavior, CI wiring, provider integration, or release readiness."
[/KFM_META_BLOCK_V2] -->

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: runtime" src="https://img.shields.io/badge/root-runtime%2F-blue">
  <img alt="Lane: mock adapter" src="https://img.shields.io/badge/lane-mock__adapter-purple">
  <img alt="Maturity: no implementation confirmed" src="https://img.shields.io/badge/maturity-no__implementation__confirmed-orange">
  <img alt="Boundary: not provider authority" src="https://img.shields.io/badge/boundary-not__provider__authority-critical">
</p>

**Status:** draft / mock-only adapter guardrail
**Path:** `runtime/model_adapters/mock/`
**Current role:** README-only compatibility/index lane for mock model adapters
**Truth posture:** CONFIRMED empty README path before this update; CONFIRMED nearby runtime/model-adapter and mock-runtime README boundaries; NEEDS VERIFICATION for actual adapter code, fixtures, tests, envelopes, receipts, CI, and owner assignments.

## Quick jumps

[Purpose](#purpose) · [Boundary](#boundary) · [Current inventory](#current-inventory) · [Repo fit](#repo-fit) · [Mock adapter responsibilities](#mock-adapter-responsibilities) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Minimal mock adapter card](#minimal-mock-adapter-card) · [Validation](#validation) · [Open questions](#open-questions)

---

## Purpose

`runtime/model_adapters/mock/` is the mock-only child lane under the provider-neutral model adapter runtime lane.

Use it for deterministic mock adapter notes, mock adapter cards, fixture-to-adapter mappings, finite-outcome coverage notes, and mock-to-live migration notes. The lane exists to prove adapter behavior can be exercised safely before local or provider-backed model adapters are admitted.

This lane should bridge the broader deterministic mock runtime lane at `runtime/mock/` and the provider-neutral adapter lane at `runtime/model_adapters/` without replacing either one.

## Boundary

This path is not a live provider home, not a model runtime, not an evidence store, not a source registry, not a lifecycle data root, not a policy engine, not a validator implementation, not a contract/schema home, not a receipt/proof root, not a public API, and not release authority.

Mock adapter output is test material only. It must not be treated as evidence, citation support, policy approval, steward review, release decision, public truth, or implementation proof unless paired tests, fixtures, validators, receipts, and review records say so.

> [!IMPORTANT]
> Mock-first does not mean trust-free. Mock adapters must still preserve finite outcomes, evidence pointers when relevant, policy posture, citation posture, RuntimeResponseEnvelope posture, AIReceipt posture, and deterministic replay notes.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `runtime/model_adapters/mock/README.md` | present | Empty file expanded by this README. |
| `runtime/model_adapters/mock/*` | no files found in current search | No mock adapter cards, fixtures, tests, or implementation files confirmed under this path. |
| `runtime/model_adapters/README.md` | present | Inspected provider-neutral model adapter lane. |
| `runtime/mock/README.md` | present | Inspected deterministic mock runtime lane. |
| `runtime/AI/README.md` | present | Inspected governed AI runtime compatibility/index lane. |

## Repo fit

```text
runtime/
├── README.md
├── model_adapters/
│   ├── README.md                     # provider-neutral adapter lane
│   └── mock/
│       └── README.md                 # this file; mock adapter guardrail
├── mock/                             # broader deterministic mock runtime lane
├── AI/                               # governed AI compatibility/index lane
├── envelopes/                        # runtime response envelope lane
├── ollama/                           # local model runtime lane
├── local/                            # local runtime wiring
└── service_configs/                  # service configuration templates

fixtures/                             # deterministic examples and expected cases
tests/                                # executable proof of behavior
tools/validators/                     # validator implementation
contracts/                            # semantic meaning
schemas/                              # machine-checkable shape
policy/                               # admissibility, rights, sensitivity, runtime policy
data/                                 # lifecycle records, receipts, proofs, catalogs, emitted data
release/                              # release, correction, rollback authority
```

## Mock adapter responsibilities

| Responsibility | Requirement |
|---|---|
| Mock identity | Name the adapter, adapter card, fixture route, and owner. |
| Runtime mode | Mark `mock` explicitly; do not imply local or provider-backed execution. |
| Determinism | State the fixed inputs, expected outputs, finite outcomes, and replay assumptions. |
| Evidence posture | Use evidence pointers only when test fixtures intentionally exercise evidence handling. |
| Policy posture | Link policy references when the mock exercises `DENY`, `ABSTAIN`, restriction, or fail-closed behavior. |
| Citation posture | Link citation-validation support when generated mock text includes citation-like output. |
| Envelope posture | Link RuntimeResponseEnvelope expectations when mock output is envelope-shaped. |
| Receipt posture | Link AIReceipt or RunReceipt expectations when the mock participates in receipted runtime tests. |
| Test posture | Link fixtures, tests, validators, or expected-output files before behavior is claimed. |
| Migration posture | Record whether the mock may graduate to `runtime/model_adapters/`, `runtime/ollama/`, or a provider-specific lane. |

## What belongs here

- This README.
- Mock adapter cards and mock adapter index notes.
- Deterministic fixture-to-adapter mapping notes.
- Mock finite-outcome coverage notes for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.
- Mock-to-live migration notes that preserve provider neutrality.
- Pointers to contracts, schemas, policy, fixtures, tests, validators, runtime envelopes, AIReceipt records, and RunReceipt records.
- Review notes explaining why a mock adapter remains test material rather than evidence, release material, or public truth.

## What does not belong here

| Do not put this in `runtime/model_adapters/mock/` | Correct home |
|---|---|
| Live provider implementation code | accepted provider/local adapter lane after review |
| Provider credentials, tokens, private config, or local `.env` values | never in repo |
| General model-adapter index notes | `runtime/model_adapters/` |
| Broad mock runtime notes not adapter-specific | `runtime/mock/` |
| Runtime response envelope definitions | `runtime/envelopes/`, `contracts/`, and `schemas/` as appropriate |
| Canonical contracts or semantic meaning | `contracts/` |
| Schema definitions | `schemas/` |
| Policy rules or policy decisions | `policy/` and governed review/release roots |
| Fixture payloads or golden outputs | `fixtures/` |
| Executable tests | `tests/` or accepted package/app test root |
| Validator source code | `tools/validators/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | `data/` lifecycle roots |
| EvidenceBundles, SourceDescriptors, receipts, proofs, catalogs, release manifests, correction records, or rollback records | accepted `data/`, source-registry, proof, receipt, catalog, or `release/` roots |
| Generated text treated as evidence, citation support, review, policy, publication, or public truth | nowhere; generated text remains downstream and bounded |

## Minimal mock adapter card

```markdown
# <mock-adapter-card-id>

## Status
DRAFT / READY_FOR_REVIEW / MOCK_ONLY / ACTIVE_ADAPTER / VALIDATION_REQUIRED / HELD / MIGRATE / SUPERSEDED / RETIRED

## Adapter name
<mock adapter name>

## Runtime mode
mock

## Canonical home
runtime/model_adapters/mock/

## Allowed use
<deterministic test, fixture replay, finite-outcome coverage, envelope test, receipt test, or N/A>

## Expected finite outcome
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Governed support pointers
- Contract: <path or N/A>
- Schema: <path or N/A>
- Policy: <path or N/A>
- Evidence fixture: <path or N/A>
- Citation validation: <path or N/A>
- RuntimeResponseEnvelope: <path or N/A>
- AIReceipt: <path or N/A>
- Test: <path or N/A>
- Validator: <path or N/A>

## Determinism note
<fixed input, fixed output, seeded behavior, or NEEDS VERIFICATION>

## Boundary notes
<what this mock may prove and what it must not become>

## Reviewer
<steward or maintainer>

## Review date
<YYYY-MM-DD>

## Follow-up
<open items or none>
```

## Validation

```bash
find runtime/model_adapters/mock -maxdepth 4 -type f | sort
find runtime/model_adapters runtime/mock runtime/envelopes -maxdepth 4 -type f 2>/dev/null | sort
find fixtures tests -maxdepth 5 -type f 2>/dev/null | sort
pytest tests/runtime tests/api tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once the accepted runtime/model-adapter test commands are confirmed.

## Review checklist

- [ ] Mock adapter identity is explicit.
- [ ] Runtime mode is marked `mock`.
- [ ] Expected finite outcome is explicit or marked `N/A`.
- [ ] Contract/schema pointers are linked when output is contract- or schema-shaped.
- [ ] Policy pointer is linked when the mock exercises deny, restrict, abstain, or fail-closed behavior.
- [ ] Fixture/test/validator evidence is linked before behavior is claimed.
- [ ] RuntimeResponseEnvelope or AIReceipt pointers are linked when applicable.
- [ ] No provider credentials, private runtime values, lifecycle data, contracts, schemas, policy files, validator code, receipts, proofs, or release records are stored here.
- [ ] The entry does not claim implementation maturity without tests, fixtures, runtime evidence, or code references.

## Open questions

| Question | Status |
|---|---|
| Should `runtime/model_adapters/mock/` remain as a child lane, or should mock adapter cards live only under `runtime/mock/`? | NEEDS VERIFICATION |
| Which fixture family owns deterministic mock adapter inputs and expected outputs? | NEEDS VERIFICATION |
| Which tests or CI workflows consume mock adapter cards today? | NEEDS VERIFICATION |
| Should mock adapter behavior emit AIReceipt and RuntimeResponseEnvelope fixtures by default? | NEEDS VERIFICATION |
| What owner approves mock-to-live migration from this lane into local or provider-backed adapters? | NEEDS VERIFICATION |
