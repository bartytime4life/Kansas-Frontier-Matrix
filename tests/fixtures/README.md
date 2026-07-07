<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-readme
title: Tests Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; parent-fixture-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; unit-test-scoped; synthetic-only; no-network; public-safe; evidence-aware; policy-aware; release-gated; rollback-aware
tags: [kfm, tests, fixtures, unit-test-scoped, synthetic, no-network, public-safe, valid, invalid, denied, abstention, rollback, correction, EvidenceBundle, PolicyDecision, ReleaseManifest, RuntimeResponseEnvelope]
related:
  - ../README.md
  - ../../fixtures/README.md
  - ./focus/README.md
  - ./layers/README.md
  - ./maplibre/README.md
  - ./people-dna-land/README.md
  - ./settlements/README.md
  - ./settlements-infrastructure/README.md
  - ./ui/README.md
  - ./domains/
  - ../../docs/doctrine/directory-rules.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../release/
notes:
  - "This README replaces placeholder content at tests/fixtures/README.md."
  - "This parent lane documents unit-test-scoped fixtures only. Root fixtures/ remains the cross-cutting reusable fixture home unless repository doctrine resolves a single fixture home."
  - "Fixtures here are synthetic test carriers; they do not create source truth, evidence closure, policy approval, release approval, schema authority, implementation authority, or public artifacts."
  - "Fixture payload inventory, executable tests, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Test fixtures

> Parent README for unit-test-scoped fixture lanes under `tests/fixtures/`. This directory is for small synthetic fixtures owned by particular tests. It is not the cross-cutting reusable fixture authority, not lifecycle data, not source truth, not policy, not schema, not evidence closure, and not a release or publication surface.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: fixtures" src="https://img.shields.io/badge/lane-fixtures-purple">
  <img alt="Scope: unit test scoped" src="https://img.shields.io/badge/scope-unit__test__scoped-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/README.md`  
**Status:** draft / placeholder replaced / parent fixture lane / PROPOSED until executable tests and inventory are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures`  
**Default posture:** deterministic, synthetic, no-network, public-safe fixture material only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/README.md` defines `tests/fixtures/` as unit-test-scoped and root `fixtures/` as cross-cutting; CONFIRMED several child fixture READMEs exist; NEEDS VERIFICATION for full payload inventory, executable tests, schemas, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/` for fixtures local to test needs. A file in this tree should help a test prove an expected behavior, rejection, abstention, denial, correction, rollback, no-leak condition, or finite-outcome boundary.

In scope:

- small synthetic JSON/YAML/Markdown fixtures;
- valid, invalid, denied, abstention, correction, and rollback examples;
- no-network loader inputs;
- public-safe transformed sensitive-lane examples;
- toy refs for evidence, policy, release, review, correction, rollback, layer, runtime, UI, map, and domain objects;
- README files that route test-local fixture material to the correct lane.

Out of scope:

- real source exports or lifecycle data;
- production EvidenceBundles, receipts, proofs, releases, or policy decisions;
- schema, contract, or policy authority;
- implementation code, app routing, renderer code, or model output;
- public tiles, screenshots, exports, or map artifacts;
- sensitive raw detail, secrets, production logs, or private endpoints.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Unit-test-scoped fixtures | `tests/fixtures/` | This parent lane. |
| Executable tests | `tests/` subtrees | Consumers; not owned by this README. |
| Cross-cutting reusable fixtures | `fixtures/` root | Shared fixture home; keep separate unless doctrine resolves one home. |
| Object semantics | `contracts/` | Defines meaning; fixtures may reference toy refs only. |
| Machine schemas | `schemas/` | Defines shape; fixtures are examples, not schemas. |
| Policy/admissibility | `policy/` | Defines allow/deny/restrict/hold/abstain behavior. |
| Release/correction/rollback | `release/` and release contracts | Publication authority; fixtures do not approve release. |
| Lifecycle data | `data/` roots | RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED stays outside tests. |

> [!IMPORTANT]
> `tests/fixtures/` must not become a second canonical fixture registry, data store, release store, evidence store, policy home, schema home, contract home, or public artifact root. It is a test-local proof surface.

---

## Fixture-home rule

KFM currently allows two fixture homes with a strict split:

| Home | Purpose | Guardrail |
|---|---|---|
| `tests/fixtures/` | Unit-test-scoped fixtures local to a particular test area. | Do not promote to cross-cutting fixture authority. |
| `fixtures/` | Cross-cutting golden, valid, invalid, and synthetic fixtures shared by multiple test areas and pipelines. | Do not duplicate with `tests/fixtures/` without documenting the split. |

Every major object family should have coverage for valid, invalid, denied, abstention, and rollback/correction cases. Sensitive lanes must use public-safe transformed fixtures only.

---

## Observed child lanes

This parent README indexes lanes verified or recently documented in this repository. The list is an orientation surface, not a complete fixture payload inventory.

| Lane | Use for | Notes |
|---|---|---|
| [`focus/`](./focus/README.md) | Governed Focus request/response examples. | Finite outcomes and bounded evidence context. |
| [`layers/`](./layers/README.md) | Layer, layer-catalog, layer-manifest, and map-release examples. | Release-backed layer behavior; not tile/style authority. |
| [`maplibre/`](./maplibre/README.md) | MapLibre tiny, baseline, invalid, and bad-baseline examples. | Renderer fixtures; not rendered truth. |
| [`people-dna-land/`](./people-dna-land/README.md) | Consent, revocation, DNA/genomic, relationship, and land-link canaries. | Deny-by-default sensitive lane. |
| [`settlements/`](./settlements/README.md) | Short-name settlements compatibility fixtures. | Compatibility lane, not canonical domain authority. |
| [`settlements-infrastructure/`](./settlements-infrastructure/README.md) | Canonical Settlements/Infrastructure test-local fixtures. | Critical-asset and release-aware lane. |
| [`ui/`](./ui/README.md) | UI trust-state, accessibility, and finite-outcome fixtures. | UI fixtures; not component implementation. |
| [`domains/`](./domains/) | Domain-scoped test fixture grouping. | Inventory and child README coverage NEEDS VERIFICATION. |

---

## Fixture rule

Fixtures are downstream test carriers. They should prove behavior without becoming authority.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic only | Use toy IDs, toy refs, toy timestamps, toy geometry, and review-safe values. |
| No-network default | No live source, API, tile, style, glyph, sprite, model, vendor, or public-service calls. |
| Finite outcomes | Expected outcomes are explicit where useful: `PASS`, `ANSWER`, `ABSTAIN`, `DENY`, `HOLD`, `ERROR`, or validation failure. |
| Public-safe sensitive fixtures | Sensitive examples are transformed, generalized, redacted, withheld, denied, or synthetic-only. |
| Trust boundary | Fixtures do not bypass governed APIs, release gates, policy checks, evidence resolution, or review state. |
| Reversibility | Correction and rollback cases remain testable where public or consequential state is modeled. |

---

## Accepted material

Accepted material is limited to compact, synthetic, reviewable examples, such as:

- `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, and `*.md` fixture files;
- toy EvidenceRef, EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackCard, LayerManifest, RuntimeResponseEnvelope, FocusResponseEnvelope, and EvidenceDrawerPayload refs;
- public-safe expected-output examples;
- negative canaries for forbidden boundaries, missing evidence, denied policy, stale release, missing rollback, unsupported citations, direct-store access, and no-network violations;
- child README files that explain lane scope and route material to the correct responsibility root.

---

## Exclusions

Do not place these materials in this parent lane:

| Excluded material | Correct destination |
|---|---|
| cross-cutting reusable fixture sets | `fixtures/` root, if shared across tests/pipelines |
| executable test code | appropriate `tests/` subtree |
| object contracts | `contracts/` |
| machine schemas | `schemas/` |
| policy rules | `policy/` |
| source data or lifecycle material | `data/` lifecycle roots |
| release decisions, real correction notices, rollback cards | `release/` roots |
| UI/app/renderer/model implementation | `apps/`, `packages/`, `runtime/`, or accepted code roots |
| real sensitive data, secrets, production logs, public artifacts | not allowed in this fixture lane |

---

## Suggested layout

```text
tests/fixtures/
|-- README.md
|-- focus/
|-- layers/
|-- maplibre/
|-- people-dna-land/
|-- settlements/
|-- settlements-infrastructure/
|-- ui/
`-- domains/
```

The visible README coverage for these lanes was inspected during authoring, but complete fixture payload inventory remains NEEDS VERIFICATION.

---

## Run posture

No single executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures
```

Default fixture use should be deterministic, local, no-network, public-safe, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep this parent README navigational and boundary-focused.
- [ ] Keep fixture payloads synthetic, compact, public-safe, and reviewable.
- [ ] Preserve the split between `tests/fixtures/` and root `fixtures/` unless doctrine is updated.
- [ ] Do not store real source data, releases, evidence/proof records, schemas, contracts, policy rules, app code, renderer code, model output, secrets, production logs, or public artifacts here.
- [ ] Add or update child README files when a fixture lane is introduced.
- [ ] Link child fixture lanes to consumer tests only after verification.
- [ ] Mark payload inventory, test wiring, schema bindings, policy/runtime wiring, CI coverage, and pass rates as NEEDS VERIFICATION until checked.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| `tests/fixtures/` fixture-home rule | CONFIRMED in `tests/README.md`. |
| Root `fixtures/` split | CONFIRMED in `tests/README.md`; resolved single-home status remains NEEDS VERIFICATION. |
| Child README examples | PARTIALLY CONFIRMED during authoring. |
| Complete child-lane inventory | NEEDS VERIFICATION. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
