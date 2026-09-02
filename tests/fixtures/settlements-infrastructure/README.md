<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-settlements-infrastructure-readme
title: Settlements-Infrastructure Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; canonical-test-fixture-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Settlements/Infrastructure domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; settlements-infrastructure; synthetic-only; no-network; public-safe; deny-by-default-aware; release-gated; rollback-aware
tags: [kfm, tests, fixtures, settlements-infrastructure, settlements, infrastructure, synthetic, no-network, public-safe, deny-by-default, EvidenceBundle, ReleaseManifest, ReviewRecord, RedactionReceipt, AggregationReceipt, CorrectionNotice, RollbackCard, PASS, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../settlements/README.md
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
  - "This README replaces placeholder content at tests/fixtures/settlements-infrastructure/README.md."
  - "This lane documents unit-test-scoped Settlements/Infrastructure fixtures. It does not become the canonical reusable fixture root unless repo doctrine later resolves tests/fixtures/ as the sole fixture home."
  - "The short tests/fixtures/settlements/ lane is compatibility-only; this lane uses the canonical domain segment settlements-infrastructure."
  - "Executable tests, payload inventory, schema bindings, policy/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements-Infrastructure test fixtures

> Unit-test-scoped fixture lane for synthetic Settlements/Infrastructure examples under `tests/fixtures/settlements-infrastructure/`. This README keeps settlement identity, infrastructure, legal/census distinction, sensitivity, release, correction, and rollback test cases reviewable without turning fixtures into source data, evidence closure, release approval, policy authority, or public-map artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: settlements-infrastructure" src="https://img.shields.io/badge/lane-settlements--infrastructure-purple">
  <img alt="Posture: deny by default aware" src="https://img.shields.io/badge/posture-deny__by__default__aware-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/settlements-infrastructure/README.md`  
**Status:** draft / placeholder replaced / canonical test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/settlements-infrastructure`  
**Canonical domain segment:** `settlements-infrastructure`  
**Compatibility sibling:** `../settlements/`  
**Default posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED current doctrine names `settlements-infrastructure` as the canonical domain segment; CONFIRMED proof-root doctrine names `tests/domains/settlements-infrastructure/` and `fixtures/domains/settlements-infrastructure/`; NEEDS VERIFICATION for fixture payload inventory, executable tests, schemas, policy/runtime wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/fixtures/settlements-infrastructure/` for test-local synthetic fixtures that exercise Settlements/Infrastructure expectations.

In scope:

- settlement, municipality, census place, townsite, fort, mission, and ghost-town identity examples;
- legal-status vs census/statistical distinction canaries;
- public-safe generalized footprint examples;
- critical-asset denial and review-gated examples using toy refs only;
- condition-temporal examples such as toy `observed_at` posture;
- evidence, review, release, correction, rollback, abstention, denial, and error examples;
- test-local manifests that explain expected outcomes without carrying real operational or restricted material.

Out of scope:

- real source exports;
- production settlement or infrastructure data;
- exact restricted facility geometry;
- dependency-graph detail;
- policy rules, schemas, contracts, release records, receipts, proofs, or public map artifacts;
- emergency alert, instruction, or life-safety authority.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Unit-test-scoped Settlements/Infrastructure fixtures | `tests/fixtures/settlements-infrastructure/` | This lane. |
| Short-name compatibility fixtures | `tests/fixtures/settlements/` | Compatibility sibling; not canonical authority. |
| Domain tests | `tests/domains/settlements-infrastructure/` | Expected consumers; not fixture authority. |
| Reusable cross-test fixtures | `fixtures/domains/settlements-infrastructure/` | Preferred reusable fixture root per current doctrine. |
| Object meaning | `contracts/domains/settlements-infrastructure/` | Defines semantics; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` | Defines shape; not owned here. |
| Policy gates | `policy/domains/settlements-infrastructure/` and `policy/sensitivity/infrastructure/` | Admissibility authority; not owned here. |
| Release decisions | `release/` | Publication, correction, withdrawal, and rollback authority. |

> [!IMPORTANT]
> This lane is a test fixture surface. It must not become a lifecycle data store, source registry, object-contract home, schema home, policy home, release store, artifact store, public-map root, or emergency/life-safety system.

---

## Fixture rule

Settlements/Infrastructure fixtures are downstream test carriers. They do not create settlement truth, infrastructure truth, legal truth, census truth, evidence closure, release approval, policy approval, or public-map authority.

Core expectations:

| Expectation | Required posture |
|---|---|
| Synthetic only | Use toy IDs, toy names, toy dates, toy geometries, and toy refs. |
| No-network default | No live source, tile, style, API, model, emergency, or public-service calls. |
| Role clarity | Legal municipality, census place, historic townsite, and infrastructure context must not collapse. |
| Evidence aware | Claim-like fixtures require synthetic EvidenceRef/EvidenceBundle posture or expect `ABSTAIN`. |
| Sensitivity aware | Restricted or exact-detail cases must expect `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or validation failure. |
| Release aware | Public-facing examples require synthetic review, release, correction, and rollback posture where material. |
| Lifecycle aware | Fixtures must not imply direct `RAW` or `WORK` to `PUBLISHED` promotion. |

---

## Expected fixture families

| Family | Purpose | Expected posture |
|---|---|---|
| `legal_municipality_valid` | Public-safe legal-status settlement identity. | `PASS` with evidence/release refs. |
| `census_place_not_municipality` | Prevents census/statistical place from becoming legal municipality truth. | validation failure / `ABSTAIN`. |
| `ghost_town_status_valid` | Historical place status with bounded evidence refs. | `PASS`. |
| `missing_evidence` | Claim-like fixture lacks support. | `ABSTAIN`. |
| `restricted_asset_detail` | Critical-asset detail must not publish. | `DENY`. |
| `generalized_footprint_valid` | Public-safe generalized geometry with transform posture. | `PASS`. |
| `condition_observation_temporal` | `observed_at` and release/freshness posture are explicit. | `PASS` / validation failure. |
| `dependency_graph_restricted` | Sensitive dependency topology remains blocked or generalized. | `DENY` / `ABSTAIN`. |
| `correction_visible` | Correction lineage is preserved. | `PASS`. |
| `rollback_required` | Rollback target is present for public-facing fixture state. | `PASS` / validation failure. |

---

## Accepted inputs

Accepted material is limited to compact, synthetic, reviewable examples, such as:

- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, or `*.md` fixture notes;
- toy settlement refs, toy infrastructure refs, toy geometry refs, toy source refs, and toy release refs;
- public-safe generalized examples;
- expected outcomes and reason-code notes for `PASS`, `ABSTAIN`, `DENY`, `HOLD`, `ERROR`, or validation failure;
- links to consumer tests once those tests are verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| reusable cross-test fixture payloads | `fixtures/domains/settlements-infrastructure/` unless repo resolves otherwise |
| executable domain tests | `tests/domains/settlements-infrastructure/` |
| object contracts | `contracts/domains/settlements-infrastructure/` |
| schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or accepted schema home |
| policy rules | `policy/` roots |
| real source exports or lifecycle data | governed `data/` lifecycle roots |
| release records | `release/` roots |
| public tiles, layers, screenshots, or map exports | governed publication/artifact roots only after release |
| secrets, production logs, private endpoints, exact restricted detail, or emergency instructions | not allowed in repository fixtures |

---

## Suggested layout

```text
tests/fixtures/settlements-infrastructure/
|-- README.md
|-- legal_municipality.valid.json
|-- census_place_not_municipality.invalid.json
|-- ghost_town_status.valid.json
|-- missing_evidence.abstain.json
|-- restricted_asset_detail.deny.json
|-- generalized_footprint.valid.json
|-- condition_observation_temporal.valid.json
|-- dependency_graph_restricted.deny.json
|-- correction_visible.valid.json
`-- rollback_required.valid.json
```

The layout is PROPOSED until payload files and consumers exist.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/settlements-infrastructure tests/fixtures/settlements-infrastructure
```

Default runs should be deterministic, local, no-network, public-safe, and finite-outcome only.

---

## Maintenance checklist

- [ ] Keep examples synthetic, public-safe, compact, and reviewable.
- [ ] Keep canonical domain examples under the `settlements-infrastructure` segment.
- [ ] Keep short-name compatibility cases in `../settlements/` only when needed.
- [ ] Keep legal/census/historic/infrastructure roles distinct.
- [ ] Use fail-closed outcomes for unresolved evidence, source role, sensitivity, rights, review, release, exact detail, or dependency topology.
- [ ] Do not store real source data, public artifacts, release records, policy rules, schemas, implementation code, secrets, production logs, or emergency instructions here.
- [ ] Link to consumer tests only after verification.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; placeholder replaced. |
| Canonical domain segment | CONFIRMED as `settlements-infrastructure`. |
| Compatibility sibling `settlements/` | CONFIRMED and documented as compatibility-only. |
| Fixture payload inventory | NEEDS VERIFICATION. |
| Consumer tests | NEEDS VERIFICATION. |
| Schema bindings | NEEDS VERIFICATION. |
| Policy/runtime wiring | NEEDS VERIFICATION. |
| Runner and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
