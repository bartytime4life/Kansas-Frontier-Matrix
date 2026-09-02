<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-smoke-readme
title: tools/validators/smoke README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-validator-steward-plus-ci-steward-plus-schema-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; smoke-validator-index; fast-health-checks; wiring-checks; fail-closed; non-authoritative; not-domain-smoke; release-gated
owning_root: tools/
responsibility: parent smoke-test validator routing README under tools/validators; documents fast health-check expectations for validator imports, CLI entrypoints, registry discovery, minimal schema availability, fixture discoverability, policy bundle references, evidence/release validator reachability, deterministic exit codes, no-network/no-secret/no-write posture, CI smoke execution, and routing to full validators while deferring schema validation, policy decisions, evidence records, receipts, lifecycle data, release records, domain meaning, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../lifecycle/README.md
  - ../evidence/README.md
  - ../sensitivity/README.md
  - ../rights/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../domains/atmosphere/smoke/README.md
  - ../../../tests/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty placeholder at tools/validators/smoke/README.md. It does not confirm executable smoke validators, registry wiring, CI jobs, policy bundles, fixtures, or runtime behavior."
  - "This path is for smoke tests / health checks. It is not the Atmosphere smoke domain lane; Atmosphere smoke validation lives under tools/validators/domains/atmosphere/smoke/."
  - "Smoke checks are shallow gates that prove basic wiring and fail-closed posture. They must not be treated as full schema, contract, evidence, policy, lifecycle, release, sensitivity, rights, geometry, PMTiles, MapLibre, or domain validation."
  - "A passing smoke validator means only that the checked entrypoint is reachable and minimally coherent. It is not proof of correctness, evidence closure, policy approval, release approval, publication readiness, or public safety."
  - "Smoke validators must avoid network calls, secrets, source downloads, lifecycle data writes, release writes, receipt/proof writes, public artifact emission, and hidden mutation unless an accepted test harness explicitly authorizes a temporary sandbox."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/smoke

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-smoke--validator--index-informational)
![depth](https://img.shields.io/badge/depth-shallow--health--checks-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/smoke/` is the smoke-test validator routing index for fast validator health checks, import checks, CLI/registry reachability, fixture discovery, deterministic exit codes, and CI wiring probes without replacing full KFM validators or release gates.

---

## Purpose

`tools/validators/smoke/` exists to organize shallow validator health checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Can the validator surface start, discover its registry, load minimal schemas and fixtures, locate policy/evidence/release validator dependencies, return deterministic finite outcomes, avoid unsafe side effects, and fail closed when basic wiring is missing?

The answer should be a fast, deterministic result suitable for early CI, local sanity checks, and maintainer triage. This folder should not validate domain truth, approve release, decide policy, prove evidence closure, write receipts, write proofs, store lifecycle data, publish artifacts, authorize public surfaces, or replace full negative-path tests.

[Back to top](#top)

---

## Naming note: smoke tests, not smoke domain

`tools/validators/smoke/` is for **smoke tests**.

It must not be confused with Atmosphere smoke validation, which concerns smoke plumes, AOD rasters, model fields, Hazards seams, source roles, freshness, and alert-authority denial. Atmosphere smoke validation remains domain-specific and belongs in `tools/validators/domains/atmosphere/smoke/` or another accepted Atmosphere/Hazards lane.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/smoke/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/README.md` | **CONFIRMED short README** | Defines validators as fail-closed checkers, cross-cutting plus per-domain. |
| `tools/validators/domains/atmosphere/smoke/README.md` | **CONFIRMED domain smoke README / executable behavior NEEDS VERIFICATION** | Domain-specific Atmosphere smoke lane; distinct from this smoke-test lane. |
| Smoke validator executables | **NEEDS VERIFICATION** | No script, package entrypoint, registry entry, Make target, pytest mark, fixture set, CI job, or runtime behavior is claimed here. |
| Schema, fixture, policy, evidence, release, report, receipt, and CI integration | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Smoke-test scope

Smoke validators should answer shallow health questions only:

| Check family | Smoke question | Must not be treated as |
|---|---|---|
| Import health | Can validator modules import without syntax errors or missing mandatory dependencies? | Functional validation proof. |
| CLI entrypoints | Do declared validator CLI entrypoints start and return finite status codes? | Runtime correctness or release readiness. |
| Registry discovery | Can the validator registry or manifest load without duplicate ids, missing paths, or invalid refs? | Registry authority by itself. |
| Minimal schema reachability | Are expected schema homes discoverable where required? | Schema conformance. |
| Fixture discovery | Are valid/invalid fixture directories or indexes reachable where expected? | Fixture correctness. |
| Policy bundle reference check | Are policy bundle refs shaped and discoverable where required? | Policy decision or policy approval. |
| Evidence/release validator reachability | Can smoke checks find evidence, lifecycle, policy, promotion, and release validators when required? | Evidence closure or release approval. |
| Deterministic output | Does the smoke check return stable finite outcomes and machine-readable reports? | Full validation report authority. |
| Safe side-effect posture | Does the smoke check avoid network calls, source downloads, secrets, lifecycle writes, release writes, proof/receipt writes, and public artifact emission? | Permission to mutate repo or runtime state. |

[Back to top](#top)

---

## Smoke-test invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Shallow by design | Smoke tests prove reachability and basic wiring only. | Smoke pass is treated as domain validation, policy approval, or release approval. |
| Fail closed | Missing imports, missing registry entries, missing fixtures, missing schemas, missing policy refs, or unsafe side effects return finite failure outcomes. | Silent skip, best-effort pass, or swallowed error. |
| No public authority | Smoke checks never publish artifacts, approve release, authorize APIs, render public UI, or generate AI answers. | Smoke check emits public-facing output or release state. |
| No hidden mutation | Smoke checks should not write lifecycle data, release records, proofs, receipts, or source registries. | Check mutates governed state without explicit sandbox. |
| No network or secrets | Smoke checks should run offline and must not require source credentials, connector access, production signing keys, or private tokens. | Check fetches external/source content or reads secrets. |
| Deterministic output | Same inputs and environment produce stable outcomes and reason codes. | Random, clock-sensitive, environment-leaky, or non-finite results. |
| Full validators remain authoritative | Full schema, contract, evidence, policy, lifecycle, receipt, release, domain, and public-surface validators decide real readiness. | Smoke checks replace deeper validators. |

[Back to top](#top)

---

## Suggested smoke checks

The following checks are **PROPOSED** until executable files and CI wiring are verified:

| Proposed check | Expected result | Notes |
|---|---|---|
| `validator-imports` | `SMOKE_VALIDATOR_PASS` or `SMOKE_IMPORT_FAIL` | Import validator modules without running external effects. |
| `validator-registry-load` | `SMOKE_REGISTRY_PASS` or `SMOKE_REGISTRY_FAIL` | Load registry/manifest if one exists; detect duplicate ids and missing paths. |
| `validator-cli-help` | `SMOKE_CLI_PASS` or `SMOKE_CLI_FAIL` | `--help` or equivalent should exit cleanly without source access. |
| `schema-home-reachable` | `SMOKE_SCHEMA_HOME_PASS` or `SMOKE_SCHEMA_HOME_MISSING` | Check only reachability, not full validation. |
| `fixtures-index-reachable` | `SMOKE_FIXTURE_INDEX_PASS` or `SMOKE_FIXTURE_INDEX_MISSING` | Check only expected fixture index presence, not fixture correctness. |
| `policy-ref-reachable` | `SMOKE_POLICY_REF_PASS` or `SMOKE_POLICY_REF_MISSING` | Check reference shape/reachability only. |
| `evidence-release-validator-reachable` | `SMOKE_TRUST_GATE_PASS` or `SMOKE_TRUST_GATE_MISSING` | Confirm gate validators can be found, not that candidates are release-ready. |
| `no-side-effects` | `SMOKE_SIDE_EFFECT_PASS` or `SMOKE_SIDE_EFFECT_DENIED` | Confirm smoke check did not mutate governed roots or call networks. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Smoke-test validator routing | `tools/validators/smoke/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Full cross-cutting validators | `tools/validators/policy/`, `evidence/`, `lifecycle/`, `release/`, `promotion_gate/`, `sensitivity/`, `rights/`, and accepted siblings |
| Full domain validators | `tools/validators/domains/` and accepted domain validator lanes |
| Atmosphere smoke domain validation | `tools/validators/domains/atmosphere/smoke/` |
| Schemas | `schemas/contracts/v1/` or accepted schema homes |
| Policy rules and bundles | `policy/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | `data/` lifecycle roots |
| Release records | `release/` |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** smoke validator code may live here when it checks shallow reachability and safe side-effect posture while delegating real validation to full validator lanes.
- **NEEDS VERIFICATION:** exact executable files, registry entries, pytest markers, fixture indexes, policy refs, schema refs, report destinations, CI jobs, and runtime behavior.
- **DENY:** using this folder as full validator authority, policy authority, schema authority, domain meaning authority, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/smoke/` include:

- this README;
- tiny import/entrypoint/registry health-check adapters;
- checks that return finite, deterministic health outcomes;
- local-only sanity tests for validator discovery and no-side-effect posture;
- documentation that tells maintainers which full validator to run after a smoke failure or smoke pass;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Full schema/contract/policy/evidence/lifecycle/release/domain validators | dedicated validator lanes under `tools/validators/` |
| Policy rules, allowlists, denylists, steward decisions, release gates | `policy/`, `release/`, accepted governance homes |
| Canonical schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/...` or accepted schema homes |
| Semantic contracts | `contracts/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures that assert full behavior | `tests/` and `fixtures/` conventions |
| Source credentials, private source content, production signing keys, secrets, network-only checks | denied for smoke checks unless explicitly sandboxed by accepted test harness |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SMOKE_VALIDATOR_PASS` | Smoke check passed its shallow health condition. |
| `SMOKE_VALIDATOR_FAIL` | Smoke check failed one or more shallow health conditions. |
| `SMOKE_IMPORT_FAIL` | Required module or dependency could not import. |
| `SMOKE_CLI_FAIL` | Declared CLI entrypoint failed to start or did not return finite status. |
| `SMOKE_REGISTRY_FAIL` | Validator registry or manifest could not load, had duplicate ids, or referenced missing paths. |
| `SMOKE_SCHEMA_HOME_MISSING` | Required schema home or schema reference was not reachable. |
| `SMOKE_FIXTURE_INDEX_MISSING` | Required fixture directory or fixture index was not reachable. |
| `SMOKE_POLICY_REF_MISSING` | Required policy reference was absent or malformed. |
| `SMOKE_TRUST_GATE_MISSING` | Expected evidence, policy, lifecycle, promotion, or release validator dependency was not reachable. |
| `SMOKE_SIDE_EFFECT_DENIED` | Smoke check attempted network access, secret access, source download, governed-state mutation, release write, receipt/proof write, or public artifact emission. |
| `SMOKE_TIMEOUT` | Smoke check exceeded configured runtime budget. |
| `SMOKE_OVERCLAIM_DENIED` | Smoke check result was treated as full validation, policy approval, evidence closure, release approval, or public-safety proof. |
| `VALIDATOR_SYSTEM_ERROR` | Smoke check could not complete because of malformed input, missing dependency, missing registry entry, unexpected runtime error, or test harness misconfiguration. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/smoke/
├── README.md
├── smoke_imports.py                     # PROPOSED; not confirmed
├── smoke_registry.py                    # PROPOSED; not confirmed
├── smoke_cli.py                         # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add smoke checks that contact networks, depend on secrets, mutate governed roots, emit release artifacts, or claim full validation. A smoke check should make the system safer by failing early, not by weakening deeper gates.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/smoke/README.md`.
- [x] It distinguishes smoke-test validation from Atmosphere smoke domain validation.
- [x] It marks this path as shallow health-check routing, not schema, policy, evidence, lifecycle, release, domain, public runtime, or AI authority.
- [x] It preserves fail-closed posture and requires deterministic finite outcomes.
- [x] It forbids network calls, secrets, source downloads, governed-state writes, release writes, proof/receipt writes, and public artifact emission for normal smoke checks.
- [x] It marks executable scripts, registry wiring, pytest markers, fixtures, policy refs, schema refs, report destinations, CI jobs, and runtime behavior as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to smoke validators are searched and classified.
- [ ] Smoke scripts and/or pytest markers are verified.
- [ ] Fixture indexes and schema/policy refs used by smoke checks are verified.
- [ ] Tests prove smoke pass, smoke fail, import fail, registry fail, side-effect denied, timeout, and overclaim-denied cases.
- [ ] CI invokes smoke validators in deterministic order before deeper validators.
- [ ] Any generated smoke reports write only to accepted report or CI artifact homes and never to proof, receipt, release, or lifecycle authority roots unless explicitly approved.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with smoke-test validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
