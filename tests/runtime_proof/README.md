<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-runtime-proof-readme
title: Runtime Proof README
type: test-readme
version: v0.1
status: draft; greenfield-stub-replaced; runtime-proof-parent-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Runtime proof steward
  - OWNER_TBD - Governed API steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; runtime-proof; finite-outcomes; abstain-proof; no-network; synthetic-only; evidence-aware; policy-aware; release-gated; trust-membrane
tags: [kfm, tests, runtime-proof, finite-outcomes, abstain-proof, governed-api, RuntimeResponseEnvelope, EvidenceBundle, PolicyDecision, ReleaseManifest, RollbackCard, CorrectionNotice, AIReceipt, RunReceipt, ANSWER, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../fixtures/README.md
  - ./domains/README.md
  - ./domains/roads-rail-trade/README.md
  - ../../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - ../../docs/architecture/governed-api.md
  - ../../schemas/contracts/v1/runtime/
  - ../../policy/runtime/
  - ../../apps/governed-api/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
notes:
  - "This README replaces the greenfield stub at tests/runtime_proof/README.md."
  - "This parent lane documents runtime proof expectations for finite governed outcomes. It is not a runtime implementation home, fixture archive, governed API route, schema home, policy home, receipt/proof store, release store, or public UI surface."
  - "Runtime proof must show finite ANSWER / ABSTAIN / DENY / ERROR behavior through evidence, policy, release, citation, correction, rollback, and receipt gates."
  - "Complete child-lane inventory, executable test inventory, fixture payloads, actual runner/framework, schema bindings, runtime/API wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Runtime proof

> Parent README for runtime-proof tests under `tests/runtime_proof/`. This lane proves that governed runtime surfaces return finite, auditable outcomes — `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` — without bypassing evidence, policy, release, correction, rollback, citation, receipt, or trust-membrane gates.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: runtime proof" src="https://img.shields.io/badge/lane-runtime__proof-purple">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/runtime_proof/README.md`  
**Status:** draft / greenfield stub replaced / runtime-proof parent lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `runtime_proof`  
**Default posture:** deterministic, synthetic, no-network, public-safe runtime proof only  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tests/README.md` names `tests/runtime_proof/` as finite `ANSWER / ABSTAIN / DENY / ERROR` and abstain proof; CONFIRMED ADR-0020 defines `ABSTAIN` as a first-class finite outcome; CONFIRMED `domains/` child index exists; NEEDS VERIFICATION for executable tests, fixture payloads, route bindings, schema bindings, runtime/API wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/runtime_proof/` for tests that prove governed runtime behavior and outcome discipline.

In scope:

- `RuntimeResponseEnvelope` finite-outcome proof;
- abstain proof for missing, stale, conflicted, inaccessible, insufficient, or unresolved evidence;
- deny proof for policy, rights, sensitivity, consent, access, release, review, or public-surface refusal;
- error proof for malformed request, schema mismatch, contract drift, unavailable runtime machinery, or infrastructure failure;
- AI/focus proof that generated language remains evidence-subordinate and receipt-backed;
- governed API proof that public clients receive bounded envelopes and never read internal lifecycle or canonical stores;
- domain-specific runtime-proof child lanes under `domains/`.

Out of scope:

- runtime or governed API implementation;
- domain implementation;
- fixture payload collections;
- schemas, contracts, policies, release records, source registries, lifecycle data, proof stores, receipts, public map artifacts, screenshots, dashboards, or generated AI truth.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Runtime proof parent lane | `tests/runtime_proof/` | This lane. |
| Domain-specific runtime proof | `tests/runtime_proof/domains/<domain>/` | Child lanes indexed by `domains/`. |
| Domain behavior tests | `tests/domains/<domain>/` | Domain test lanes; not runtime-proof parent. |
| Governed API tests | `tests/api/` or app-owned test lanes | API route/envelope tests; not this parent. |
| Unit-test fixtures | `tests/fixtures/` | Test-local input payloads. |
| Shared fixtures | `fixtures/` and `fixtures/domains/<domain>/` | Reusable synthetic examples; not owned here. |
| Runtime schemas | `schemas/contracts/v1/runtime/` and related schema roots | Shape authority. |
| Runtime policy | `policy/runtime/`, `policy/domains/`, and related policy roots | Allow/deny/restrict/abstain authority. |
| Runtime implementation | `apps/governed-api/`, runtime packages, or accepted app roots | Surfaces under test; not owned here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Audit artifacts; tests reference or assert, not store. |
| Release records | `release/` | Publication, correction, withdrawal, and rollback authority. |

> [!IMPORTANT]
> This lane proves runtime outcomes. It must not become implementation, fixture storage, route authority, schema authority, policy authority, receipt/proof storage, release approval, public artifact storage, or a direct model-output surface.

---

## Runtime-proof rule

Every runtime-proof test should show that the runtime emits exactly one finite governed outcome and preserves an auditable reason for that outcome.

Core expectations:

| Expectation | Required posture |
|---|---|
| Finite outcome | Runtime surfaces return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` only. |
| Answer proof | `ANSWER` requires evidence support, policy pass, release state, citation posture, and trust-visible caveats where material. |
| Abstain proof | Missing, stale, conflicted, inaccessible, unresolved, or insufficient evidence produces `ABSTAIN`, not invented text. |
| Deny proof | Policy, rights, sensitivity, consent, access, review, release, or public-surface refusal produces `DENY`. |
| Error proof | Runtime machinery, schema, contract, malformed request, adapter, or infrastructure failure produces `ERROR` without claim leakage. |
| Receipt posture | AI and non-AI gates carry receipt-ready reason codes and unresolved handles where material. |
| Trust membrane | Runtime proof must not read RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, source APIs, graph internals, or direct model output. |
| Release and rollback | Public-facing runtime state requires release, correction, and rollback posture where material. |

---

## Outcome discipline

| Outcome | Runtime-proof meaning | Must not collapse into |
|---|---|---|
| `ANSWER` | Cited, policy-passed, release-aware answer or payload. | Generated fluency, rendered feature labels, source convenience fields, or unreleased candidates. |
| `ABSTAIN` | The runtime cannot or will not produce a cited, policy-passed answer because evidence/scope/source support is insufficient. | `ERROR`, silent fallback, empty response, low-confidence `ANSWER`, or hidden warning. |
| `DENY` | Policy, rights, sensitivity, consent, access, review, release, or public-surface rule blocks the response. | `ABSTAIN`, `ANSWER`, style-only hiding, or admin bypass. |
| `ERROR` | Governance machinery cannot evaluate safely because request, schema, contract, adapter, policy runtime, or infrastructure failed. | Unbounded exception, leaked internal detail, or uncited fallback. |

---

## Observed child lanes

This list is an orientation surface, not a complete inventory.

| Lane | Use for | Status |
|---|---|---|
| [`domains/`](./domains/README.md) | Parent index for domain-specific runtime-proof lanes. | README confirmed; full child inventory NEEDS VERIFICATION. |
| [`domains/roads-rail-trade/`](./domains/roads-rail-trade/README.md) | Roads/Rail/Trade feature, layer, Evidence Drawer, Focus Mode, abstain/deny/error, correction, and rollback runtime proof. | README confirmed; executable tests NEEDS VERIFICATION. |

Add future child lanes only with a README that states scope, evidence basis, accepted inputs, exclusions, run posture, and verification status.

---

## Expected proof families

| Family | What it proves | Expected outcome |
|---|---|---|
| `answer_requires_evidence` | A substantive runtime answer has EvidenceBundle/citation and release support. | `ANSWER` / validation failure. |
| `missing_evidence_abstains` | Missing or unresolved EvidenceRef does not produce invented text. | `ABSTAIN`. |
| `stale_or_conflicted_abstains` | Stale or conflicted evidence does not become current truth. | `ABSTAIN`. |
| `policy_denied` | Rights, sensitivity, consent, review, release, or access policy blocks response. | `DENY`. |
| `malformed_request_errors` | Bad request or schema failure returns bounded error. | `ERROR`. |
| `direct_model_forbidden` | Model output alone cannot become runtime answer. | validation failure / `ABSTAIN`. |
| `direct_store_forbidden` | Runtime/public path cannot read internal lifecycle or canonical stores directly. | validation failure / `DENY`. |
| `receipt_required` | Runtime outcome has receipt-ready reason codes, refs, and unresolved handles where material. | `PASS` / validation failure. |
| `rollback_required` | Public-facing runtime state has correction and rollback posture where material. | `ANSWER` / `DENY` / `ERROR`. |
| `outcome_enum_closed` | Runtime cannot emit unregistered outcomes such as `PARTIAL`, `PENDING`, or `UNKNOWN`. | validation failure / `ERROR`. |

---

## Accepted inputs

Accepted material is limited to parent README guidance, child README files, executable runtime-proof tests, lane-local notes, and tiny synthetic inline values when they are too small to justify fixture files.

Preferred input sources:

- `tests/fixtures/` for unit-test-scoped runtime fixtures;
- `fixtures/` and `fixtures/domains/<domain>/` for reusable synthetic examples when accepted;
- `docs/adr/ADR-0020-abstain-is-a-first-class-decision.md` for abstain outcome rules;
- `contracts/`, `schemas/`, `policy/`, `release/`, `data/receipts/`, and `data/proofs/` for authoritative object, shape, policy, release, and audit references.

---

## Exclusions

Do not place these materials in this parent lane:

| Excluded material | Correct destination |
|---|---|
| governed API or runtime implementation | `apps/governed-api/`, runtime packages, or accepted implementation roots |
| domain implementation helpers | `packages/domains/<domain>/` or accepted package roots |
| fixture payload collections | `tests/fixtures/` or `fixtures/` |
| contracts, schemas, policy rules | `contracts/`, `schemas/`, `policy/` |
| source registry entries | `data/registry/` or accepted source registry home |
| lifecycle data | governed `data/` lifecycle roots |
| receipts, proofs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| release manifests, correction notices, rollback cards | `release/` |
| public map artifacts, screenshots, production logs, secrets, direct model output, generated AI truth | not allowed in this runtime-proof lane |

---

## Suggested layout

```text
tests/runtime_proof/
|-- README.md
`-- domains/
    |-- README.md
    `-- roads-rail-trade/
        `-- README.md
```

Additional runtime-proof children are PROPOSED until created, documented, and linked to verified tests and fixtures.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/runtime_proof
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only. Replace the command once the repo's actual test runner and naming convention are verified.

---

## Maintenance checklist

- [ ] Keep this parent README as a runtime-proof boundary and index page.
- [ ] Keep runtime proof focused on finite `ANSWER / ABSTAIN / DENY / ERROR` outcomes.
- [ ] Treat `ABSTAIN` as first-class, visible, auditable, and receipt-backed where material.
- [ ] Keep implementation, API routes, fixtures, contracts, schemas, policies, data, proofs, receipts, and release records in their owning roots.
- [ ] Assert evidence, policy, release, correction, rollback, citation, receipt, source-role, temporal, and public-safe posture where material.
- [ ] Assert no runtime path reads RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, source APIs, graph internals, or direct model output.
- [ ] Use public-safe transformed fixtures for sensitive examples.
- [ ] Link tests to fixtures, contracts, schemas, policy gates, release records, receipts, proofs, and API surfaces only after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| Runtime-proof purpose | CONFIRMED in `tests/README.md` as finite-outcome and abstain proof. |
| Abstain doctrine | CONFIRMED in ADR-0020 as first-class finite outcome; ADR status remains proposed. |
| Domain runtime-proof child index | CONFIRMED; README exists. |
| Roads/Rail/Trade child lane | CONFIRMED; README exists. |
| Complete child-lane inventory | NEEDS VERIFICATION. |
| Executable test inventory | NEEDS VERIFICATION. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Schema and policy bindings | NEEDS VERIFICATION. |
| Runtime/API wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
