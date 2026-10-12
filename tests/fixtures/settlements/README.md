<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-settlements-readme
title: Settlements Compatibility Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; compatibility-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Settlements/Infrastructure domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; settlements; settlements-infrastructure; compatibility-path; synthetic-only; no-network; public-safe; deny-by-default-aware; release-gated
tags: [kfm, tests, fixtures, settlements, settlements-infrastructure, compatibility, synthetic, no-network, public-safe, deny-by-default, ABSTAIN, DENY, ERROR, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/DENY_BY_DEFAULT.md
  - ../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../contracts/domains/settlements-infrastructure/
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../policy/sensitivity/infrastructure/
  - ../../../fixtures/domains/settlements-infrastructure/
  - ../../../release/candidates/settlements-infrastructure/
notes:
  - "This README replaces placeholder content at tests/fixtures/settlements/README.md."
  - "The requested path uses the short segment settlements/. Current domain path doctrine favors settlements-infrastructure/ and records slug variance as CONFLICTED / ADR-class."
  - "This lane is therefore documented as a compatibility/test-local fixture lane, not as the canonical reusable Settlements/Infrastructure fixture root."
  - "Executable tests, payload inventory, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements compatibility test fixtures

> Unit-test-scoped compatibility lane for synthetic settlement-related fixtures under `tests/fixtures/settlements/`. This README keeps short-name settlement fixtures useful for tests while preserving the canonical Settlements/Infrastructure responsibility boundaries.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: settlements compatibility" src="https://img.shields.io/badge/lane-settlements__compatibility-purple">
  <img alt="Canonical domain: settlements-infrastructure" src="https://img.shields.io/badge/canonical-settlements--infrastructure-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/settlements/README.md`  
**Status:** draft / placeholder replaced / compatibility fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/settlements`  
**Canonical domain segment:** `settlements-infrastructure`  
**Default posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/fixtures/` is unit-test-scoped by repo doctrine; CONFIRMED canonical path doctrine names the domain segment `settlements-infrastructure` and records slug variance as CONFLICTED; NEEDS VERIFICATION for fixture payload inventory, executable tests, schemas, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/settlements/` only for test-local compatibility fixtures that intentionally use the short `settlements` segment.

In scope:

- tiny synthetic settlement identity fixtures;
- legal/census/status distinction canaries;
- ghost-town or historic-place state examples using toy refs;
- public-safe generalized footprint examples;
- abstention, denial, correction, and rollback examples;
- manifest notes that route canonical material toward `settlements-infrastructure` homes.

Out of scope:

- canonical reusable domain fixtures;
- real source exports;
- critical-asset detail;
- exact sensitive facility geometry;
- release decisions;
- schema, contract, or policy definitions;
- public map payloads.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Short-name compatibility fixtures | `tests/fixtures/settlements/` | This lane. |
| Canonical domain tests | `tests/domains/settlements-infrastructure/` | Expected consumers; not proven here. |
| Canonical reusable fixtures | `fixtures/domains/settlements-infrastructure/` | Preferred reusable fixture root; presence NEEDS VERIFICATION. |
| Object meaning | `contracts/domains/settlements-infrastructure/` | Defines semantics; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` | Defines shape; not owned here. |
| Policy gates | `policy/domains/settlements-infrastructure/` and `policy/sensitivity/infrastructure/` | Admissibility authority; not owned here. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

> [!IMPORTANT]
> This path must not become a parallel `settlements` domain root. Use it only as a bounded test-local compatibility surface until slug placement is settled and consumers are verified.

---

## Fixture rule

Settlements fixtures are downstream test carriers. They do not create settlement truth, legal truth, census truth, infrastructure truth, evidence closure, release approval, policy approval, or public-map authority.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic only | Use toy IDs, toy names, toy dates, toy geometries, and toy refs. |
| No-network default | No live source, tile, style, API, model, or public-service calls. |
| Canonical routing | Reusable or domain-authoritative cases route to `settlements-infrastructure` homes. |
| Role clarity | Legal municipality, census place, townsite, historic site, and infrastructure context must not collapse. |
| Sensitivity aware | Restricted or exact-detail cases must expect `DENY`, `ABSTAIN`, `HOLD`, or validation failure. |
| Release aware | Public-facing examples require synthetic release, review, correction, and rollback posture where material. |

---

## Accepted inputs

Accepted material is limited to compact, synthetic, reviewable examples, such as:

- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy settlement refs, toy status refs, toy geometry refs, and toy release refs;
- public-safe generalized examples;
- expected outcome notes for `PASS`, `ABSTAIN`, `DENY`, `HOLD`, `ERROR`, or validation failure;
- links to consumer tests once those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| canonical reusable Settlements/Infrastructure fixtures | `fixtures/domains/settlements-infrastructure/` if accepted |
| domain tests | `tests/domains/settlements-infrastructure/` |
| object contracts | `contracts/domains/settlements-infrastructure/` |
| schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted schema home |
| policy rules | `policy/` roots |
| real source exports or lifecycle data | governed `data/` lifecycle roots |
| release records | `release/` roots |
| public tiles, layers, screenshots, or map exports | governed publication/artifact roots only after release |
| secrets, production logs, private endpoints, or unsafe exact-detail material | not allowed in repository fixtures |

---

## Suggested layout

```text
tests/fixtures/settlements/
|-- README.md
|-- legal_status.valid.json
|-- census_place_not_municipality.invalid.json
|-- ghost_town_status.valid.json
|-- missing_evidence.abstain.json
|-- restricted_detail.deny.json
|-- correction_visible.valid.json
`-- rollback_required.valid.json
```

The layout is PROPOSED until payload files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/settlements-infrastructure tests/fixtures/settlements
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples synthetic, public-safe, compact, and reviewable.
- [ ] Do not let `settlements/` become a parallel canonical domain segment.
- [ ] Route reusable domain fixtures toward `fixtures/domains/settlements-infrastructure/` once accepted.
- [ ] Keep legal/census/historic/infrastructure roles distinct.
- [ ] Use fail-closed outcomes for unresolved evidence, sensitivity, rights, review, release, or exact-detail exposure.
- [ ] Do not store real source data, public artifacts, release records, policy rules, schemas, implementation code, secrets, or production logs here.
- [ ] Link to consumer tests only after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Canonical domain segment | CONFIRMED as `settlements-infrastructure` in current doctrine. |
| Slug variance | CONFIRMED as CONFLICTED / ADR-class in canonical path docs. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
