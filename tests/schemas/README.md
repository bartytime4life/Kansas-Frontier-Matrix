<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-schemas-readme
title: Schema Tests README
type: test-readme
version: v0.1
status: draft; greenfield-stub-replaced; schema-test-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Test steward
  - OWNER_TBD - Schema steward
  - OWNER_TBD - Contract steward
  - OWNER_TBD - Validation steward
  - OWNER_TBD - QA steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tests; schemas; machine-shape-tests; no-network; synthetic-only; fixture-backed; schema-boundary; trust-spine
tags: [kfm, tests, schemas, schema-tests, json-schema, machine-shape, valid, invalid, fixtures, validators, contracts, policy-boundary, release-boundary]
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../schemas/README.md
  - ../../schemas/tests/README.md
  - ../../schemas/contracts/v1/README.md
  - ../../contracts/README.md
  - ../../fixtures/
  - ../../tools/validators/
  - ../../policy/
  - ../../release/
notes:
  - "This README replaces the greenfield stub at tests/schemas/README.md."
  - "This lane documents executable schema tests. It is not schema authority; canonical schema definitions belong under schemas/."
  - "Schema tests verify machine-checkable shape and schema boundary behavior. They do not prove semantic truth, evidence support, policy approval, rights clearance, sensitivity clearance, release readiness, implementation maturity, or public safety by themselves."
  - "Executable test inventory, actual runner/framework, fixture consumption, validator wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Schema tests

> Test-lane README for schema and machine-shape tests under `tests/schemas/`. This directory should contain executable checks that prove KFM governed objects conform to accepted schema shape without turning tests into schema authority, fixtures, policy, contracts, data, release approval, or public truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: schema tests" src="https://img.shields.io/badge/lane-schema__tests-purple">
  <img alt="Authority: executable checks" src="https://img.shields.io/badge/authority-executable__checks-0a7ea4">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/schemas/README.md`  
**Status:** draft / greenfield stub replaced / schema test lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `schemas`  
**Schema authority root:** `schemas/`  
**Compatibility sibling:** `schemas/tests/`  
**Default posture:** deterministic, synthetic, no-network, fixture-backed schema checks only  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tests/README.md` lists `tests/schemas/` as machine-shape tests; CONFIRMED `schemas/README.md` defines `schemas/` as machine-checkable shape authority and separates it from contracts, policy, fixtures, validators, data, and release; CONFIRMED `schemas/tests/` exists as a compatibility index; NEEDS VERIFICATION for executable test inventory, runner/framework, fixture consumption, validator wiring, CI coverage, and pass rates.

---

## Scope

Use `tests/schemas/` for executable tests that verify schema behavior.

In scope:

- required-field, enum, type, reference, version, and `$id` checks;
- JSON Schema draft/posture compatibility checks;
- valid and invalid fixture validation checks;
- schema/contract pairing checks;
- domain schema shape checks;
- runtime envelope, policy decision, evidence, receipt, release, correction, rollback, layer, source, and UI payload shape checks;
- negative tests proving shape validation fails closed and does not imply public admissibility.

Out of scope:

- canonical schema definitions;
- semantic contract prose;
- fixture payload collections;
- validator implementation;
- policy rules, release decisions, evidence/proof records, lifecycle data, public artifacts, dashboards, screenshots, or generated model output.

[Back to top](#top)

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Executable schema tests | `tests/schemas/` | This lane. |
| Canonical schema definitions | `schemas/` and accepted versioned child lanes | Machine-shape authority; tests reference. |
| Schema-test compatibility index | `schemas/tests/` | Compatibility/index lane; executable ownership remains NEEDS VERIFICATION. |
| Semantic contracts | `contracts/` | Meaning authority; schemas and tests reference. |
| Fixtures | `tests/fixtures/` or root `fixtures/` | Valid/invalid/golden examples; not owned here. |
| Validator implementation | `tools/validators/` or accepted tool roots | Executable validation code; not schema-test documentation. |
| Policy rules | `policy/` | Admissibility authority; schema tests do not approve policy. |
| Release/correction/rollback | `release/` | Publication authority; schema tests do not approve release. |
| Lifecycle data and proofs | `data/` roots | Evidence-bearing and process records; not stored here. |

> [!IMPORTANT]
> `tests/schemas/` must not become a second `schemas/` root, fixture archive, contract home, policy home, validator package, data store, release store, proof store, public artifact root, or generated-output surface.

---

## Schema-test rule

Schema tests prove machine-checkable shape only. A passing schema test means a payload matches the tested schema; it does not mean the payload is true, cited, rights-cleared, policy-allowed, reviewed, released, public-safe, or implementation-proven.

Core expectations:

| Expectation | Required posture |
|---|---|
| Shape only | Validate required fields, types, enums, refs, versions, and structural constraints. |
| Pair with meaning | Schema tests should point to the paired contract when semantic meaning is material. |
| Fixture-backed | Use synthetic valid/invalid fixtures from accepted fixture lanes where possible. |
| No-network default | Do not call live sources, APIs, validators-as-services, models, tiles, vendors, or public services. |
| Fail closed | Missing required schema support, unresolved `$ref`, invalid enum, extra forbidden field, or schema drift fails visibly. |
| Boundary-safe | Passing schema validation does not skip evidence, policy, release, correction, rollback, or runtime gates. |
| Sensitive-safe | Sensitive examples remain synthetic, public-safe transformed, redacted, generalized, or denied. |

---

## Expected test families

| Family | What it proves | Expected outcome |
|---|---|---|
| `schema_loads` | Schema files parse and declare expected JSON Schema posture. | `PASS` / validation failure. |
| `schema_id_unique` | `$id` or schema identifier collisions are detected. | `PASS` / validation failure. |
| `required_fields` | Required fields are enforced for governed object families. | `PASS` / validation failure. |
| `enum_closed` | Finite enums reject unregistered values. | `PASS` / validation failure. |
| `ref_resolution` | `$ref` targets resolve inside accepted schema roots. | `PASS` / validation failure. |
| `valid_fixtures_pass` | Valid fixtures pass shape validation. | `PASS`. |
| `invalid_fixtures_fail` | Invalid fixtures fail shape validation with bounded diagnostics. | validation failure. |
| `contract_pairing` | Consequential schemas point to semantic contracts or mark missing contracts. | `PASS` / NEEDS VERIFICATION. |
| `domain_schema_shape` | Domain-specific schemas keep domain segment placement and do not create root drift. | `PASS` / validation failure. |
| `schema_not_policy` | Schema pass does not imply policy allow, rights clearance, release, or publication. | `PASS` / guardrail failure. |

---

## Compatibility note: `schemas/tests/`

`schemas/tests/` exists as a compatibility index for schema-test placement under the schema root. Current schema-root documentation treats executable test ownership as belonging to `tests/` or an accepted project test root, while `schemas/tests/` remains a compatibility/index lane until maintainers formally adopt it.

Use this rule until an ADR or migration note says otherwise:

```text
tests/schemas/   = executable schema tests
schemas/tests/   = compatibility index / placement guardrail, not executable authority by default
schemas/         = canonical schema definitions
```

If executable test files are discovered under `schemas/tests/`, either migrate them to `tests/schemas/` or update both READMEs with the accepted split and CI ownership.

---

## Accepted inputs

Accepted material is limited to executable schema tests, lane-local notes, and minimal synthetic inline values when they are too small to justify a fixture file.

Preferred input sources:

- `schemas/contracts/v1/` and accepted schema lanes for schema definitions under test;
- `contracts/` for semantic contract references;
- `tests/fixtures/` for unit-test-scoped fixture inputs;
- `fixtures/` and object-family fixture lanes for shared valid/invalid/golden examples;
- `tools/validators/` for validator implementations after ownership is verified.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Correct destination |
|---|---|
| canonical `.schema.json` definitions | `schemas/` and accepted versioned schema lanes |
| semantic contract prose | `contracts/` |
| fixture payload collections | `tests/fixtures/` or `fixtures/` |
| validator implementation code | `tools/validators/` or accepted tool/package root |
| policy rules, rights decisions, sensitivity decisions, public-access decisions | `policy/` |
| release manifests, correction notices, rollback cards, promotion decisions | `release/` |
| lifecycle data, EvidenceBundles, SourceDescriptors, proof packs, receipts | governed `data/` roots |
| runtime/API/UI implementation | `apps/`, `packages/`, or accepted implementation roots |
| public map payloads, tiles, screenshots, dashboards, production logs, secrets, direct model output | not allowed in schema tests |

---

## Suggested layout

```text
tests/schemas/
|-- README.md
|-- schema_loads.test.PROPOSED
|-- schema_id_unique.test.PROPOSED
|-- required_fields.test.PROPOSED
|-- enum_closed.test.PROPOSED
|-- ref_resolution.test.PROPOSED
|-- valid_fixtures_pass.test.PROPOSED
|-- invalid_fixtures_fail.test.PROPOSED
|-- contract_pairing.test.PROPOSED
|-- domain_schema_shape.test.PROPOSED
`-- schema_not_policy.test.PROPOSED
```

The layout is schematic. Actual test filenames, extensions, package manager, runner, and framework remain NEEDS VERIFICATION.

---

## Run posture

No executable runner was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/schemas
```

Schema-root documentation also includes a provisional command:

```bash
pytest tests/schemas tests/contract || true
```

Replace provisional `|| true` behavior with fail-closed CI once the accepted schema-test command, fixture inventory, and CI owner are confirmed.

---

## Maintenance checklist

- [ ] Keep executable schema tests in `tests/schemas/` unless an ADR or migration note chooses a different test root.
- [ ] Keep schema definitions in `schemas/`, not this test lane.
- [ ] Keep fixtures in `tests/fixtures/` or `fixtures/` and reference them from tests.
- [ ] Keep validator implementation in `tools/validators/` or accepted tool/package roots.
- [ ] Assert schema validation remains necessary but not sufficient for truth, policy, release, or publication.
- [ ] Link tests to schemas, contracts, fixtures, validators, policy gates, and release gates after verification.
- [ ] Do not store real source data, sensitive detail, production logs, public artifacts, schemas, contracts, policy rules, release records, secrets, or direct model output here.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| `tests/schemas/` placement | CONFIRMED in `tests/README.md` as machine-shape tests. |
| `schemas/` authority | CONFIRMED as machine-checkable shape root in `schemas/README.md`. |
| `schemas/tests/` compatibility index | CONFIRMED; long-term ownership NEEDS VERIFICATION. |
| Executable test inventory | NEEDS VERIFICATION. |
| Actual runner/framework | NEEDS VERIFICATION. |
| Fixture consumption | NEEDS VERIFICATION. |
| Validator wiring | NEEDS VERIFICATION. |
| CI wiring and pass rates | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
