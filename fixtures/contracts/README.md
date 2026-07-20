<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/readme
title: Contract fixtures README
type: fixture-readme
version: v0.2.0
status: draft; repository-grounded
owners:
  - TODO(owner): fixture steward
  - TODO(owner): schema steward
  - TODO(owner): contract steward
  - TODO(owner): validator steward
  - TODO(owner): policy steward
  - TODO(owner): docs steward
created: NEEDS VERIFICATION - file predates the 2026-07-01 documentation expansion
updated: 2026-07-20
policy_label: public-review
truth_posture: cite-or-abstain
responsibility_root: fixtures/
fixture_scope: reusable versioned contract-schema examples
related:
  - ../README.md
  - v1/README.md
  - ../../contracts/README.md
  - ../../schemas/contracts/README.md
  - ../../schemas/contracts/v1/README.md
  - ../../policy/README.md
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../tests/schemas/test_common_contracts.py
  - ../../tools/validators/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/contracts-validate.yml
  - ../../Makefile
tags:
  - kfm
  - fixtures
  - contracts
  - schemas
  - json-schema
  - valid
  - invalid
  - deterministic
  - no-network
  - public-safe
  - non-authoritative
notes:
  - "This README documents the reusable contract-fixture parent at fixtures/contracts/."
  - "The exact-path inventory at main@0b9307b94c67920e3451e1d40b80d287e7364ee7 confirmed v1/README.md and did not resolve v2/README.md."
  - "The generic harness covers immediate v1 schema files in seven hard-coded families only when a matching fixture directory exists."
  - "The schema-validation workflow separately enforces non-empty positive and negative lanes for six configured aggregate validators."
  - "Passing fixture checks prove only the tested machine-shape behavior; they do not establish meaning, evidence closure, policy permission, release readiness, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract fixtures

Reusable, versioned examples for exercising KFM contract schemas without turning sample data into contract, schema, policy, evidence, release, or publication authority.

**Path:** `fixtures/contracts/README.md`  
**Status:** draft; repository-grounded at `main@0b9307b94c67920e3451e1d40b80d287e7364ee7`  
**Owning root:** `fixtures/`  
**Current version index:** [`v1/`](v1/README.md)  
**Default posture:** deterministic, no-network, public-safe, non-authoritative

> [!IMPORTANT]
> A fixture can demonstrate that a tested validator accepts or rejects a JSON instance. It cannot define semantic meaning, change a schema, execute policy, resolve an `EvidenceRef`, establish an `EvidenceBundle`, approve a release, or authorize publication.

## Purpose

`fixtures/contracts/` is the reusable fixture home for versioned contract-schema examples shared by schema tests, validator wrappers, and repository validation workflows.

This parent README exists to:

- route contributors to the correct version and family;
- document the contract/schema/policy/test responsibility split;
- define the accepted valid/invalid fixture layout;
- state exactly what the current generic harness and CI do;
- keep fixture data deterministic, reviewable, no-network, and public-safe;
- surface coverage gaps instead of allowing directory presence or a green check to imply completeness.

It does not recursively inventory every fixture payload. Family and case details belong in the version and family READMEs.

## Placement and fixture-home rule

Directory Rules assign golden, valid, invalid, and synthetic test inputs to the canonical `fixtures/` responsibility root. KFM currently documents two fixture homes with a strict split:

| Home | Responsibility | Guardrail |
|---|---|---|
| `fixtures/` | Reusable, cross-cutting fixtures shared by tests, validators, or pipelines. | Do not store real lifecycle data or duplicate test-local cases without a documented reason. |
| `tests/fixtures/` | Small fixtures local to one test area. | Must not become a second reusable fixture authority. |

Contract fixtures belong here because `tests/schemas/test_common_contracts.py` and the configured validator wrappers consume the reusable path `fixtures/contracts/v1/.../`. See the [root fixture boundary](../README.md) and the [test-local fixture boundary](../../tests/fixtures/README.md).

The long-term permanence of the two-home split remains **NEEDS VERIFICATION** in the test-root open-verification register. Until an accepted ADR or migration changes it, do not copy the same fixture family into both homes.

## Responsibility boundary

| Responsibility | Owning surface | Role of this directory |
|---|---|---|
| Semantic meaning and invariants | [`contracts/`](../../contracts/README.md) | Fixtures illustrate selected cases; they do not define meaning. |
| Machine-checkable shape | [`schemas/contracts/`](../../schemas/contracts/README.md) | Fixtures are instances evaluated against schemas; they do not define shape. |
| Executable policy and admissibility | [`policy/`](../../policy/README.md) | Fixtures may exercise a decision shape; they do not make a policy decision. |
| Reusable validator implementation | [`tools/validators/`](../../tools/validators/README.md) | Validators consume fixtures; validator logic does not belong here. |
| Enforceability assertions | [`tests/`](../../tests/README.md) | Tests decide the expected result for their declared scope. |
| Source and lifecycle records | `data/` lifecycle and registry lanes | Real records never belong here. |
| Receipts and proofs | governed receipt and proof lanes | Fixture-shaped receipts or proofs are examples only. |
| Release, correction, and rollback decisions | `release/` and its contracts/policies | No fixture promotes, publishes, corrects, withdraws, or rolls back a real release. |
| Runtime, API, UI, map, and AI behavior | accepted app, package, and runtime surfaces | A fixture does not prove that a consumer exists or behaves correctly. |

The separation follows the KFM contract/schema/policy split. [ADR-0002](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) discusses that split but remains a proposed, conflict-bearing record; it is supporting context, not accepted authority.

## Version routing

### Confirmed version index

| Version | Role | Evidence status |
|---|---|---:|
| [`v1/`](v1/README.md) | Index for current v1 contract fixture families and their known exceptions. | **CONFIRMED** at the evidence snapshot |

An exact-path probe for `fixtures/contracts/v2/README.md` returned not found at the evidence snapshot. That is a **bounded absence**, not proof that no unindexed directory or future version exists.

### Version rules

- Keep versions explicit: `fixtures/contracts/<version>/`.
- Match the schema version that owns the tested machine shape.
- Do not mix fixtures for incompatible schema versions in one family.
- Preserve old-version fixtures while compatibility or migration tests depend on them.
- Treat a semantic identity change as a contract/schema migration, not a fixture rename.
- Add a version README before treating a new version root as navigable or governed.
- Do not create a parallel contract, schema, policy, registry, receipt, proof, or release authority under this tree.

## Accepted layout

The generic schema harness currently derives fixture directories with this shape:

```text
fixtures/contracts/<version>/<family>/<schema_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
└── invalid/
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

The executable harness requires the `valid/` and `invalid/` names and the `valid_*.json` / `invalid_*.json` filename patterns to discover cases. The README files are documentation requirements, not harness-discovery inputs.

Snapshot or policy-oriented fixture families that intentionally differ from this layout must document:

- why the generic schema pattern does not apply;
- the consumer and expected outcome;
- whether the content is an input, expected output, or snapshot;
- the update and review rule;
- the authority boundary and known validation limits.

The v1 child index currently identifies one such snapshot-style source fixture family. Refer to [`v1/README.md`](v1/README.md) for the bounded family-level inventory and drift notes.

## Current executable behavior

### Generic schema harness

[`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) currently hard-codes these v1 families:

```text
evidence, runtime, common, policy, source, governance, release
```

For each immediate `*.schema.json` file under `schemas/contracts/v1/<family>/`, the harness:

1. derives `<schema_name>` from the filename;
2. looks for `fixtures/contracts/v1/<family>/<schema_name>/`;
3. creates a test case only when that fixture directory exists;
4. expects every discovered `valid/valid_*.json` instance to produce no JSON Schema errors;
5. expects every discovered `invalid/invalid_*.json` instance to produce at least one JSON Schema error;
6. checks a sibling `invalid_<n>.expected_error.txt` when present.

Expected-error files are lower-cased before comparison. The harness supports:

- `enum` as a specific enum-error expectation;
- `enum|pattern|date-time` as a special alternative expectation;
- other pipe-delimited text as a regular expression;
- other non-empty lines as required substrings in the combined validator errors.

> [!WARNING]
> The generic harness does not assert that every schema has a fixture directory, and it does not independently require each discovered directory to contain at least one valid and one invalid JSON file. Missing directories are skipped; empty glob results can make an individual generated case vacuous. Do not interpret generic-harness success as complete schema coverage.

### Aggregate validator and CI coverage

The [schema-validation workflow](../../.github/workflows/schema-validation.yml) adds a stricter, bounded check for six configured aggregate validators:

| Configured validator target | Fixture family |
|---|---|
| `source_descriptor` | `v1/source/source_descriptor/` |
| `evidence_ref` | `v1/evidence/evidence_ref/` |
| `evidence_bundle` | `v1/evidence/evidence_bundle/` |
| `runtime_response_envelope` | `v1/runtime/runtime_response_envelope/` |
| `decision_envelope` | `v1/runtime/decision_envelope/` |
| `run_receipt` | `v1/runtime/run_receipt/` |

For those six targets, the workflow requires:

- the configured validator and schema files;
- at least one JSON file in each `valid/` and `invalid/` lane;
- an expected-error file for every configured invalid JSON fixture;
- all schema JSON to parse;
- every `*.schema.json` to satisfy the Draft 2020-12 meta-schema;
- canonical v1 schemas to declare unique `$id` values;
- `make schemas` and the repository-owned schema/contract pytest suites to pass.

This stricter preflight does not extend non-vacuous coverage to every schema in the seven generic families.

The [contracts-validate workflow](../../.github/workflows/contracts-validate.yml) runs `make test` on pull requests, pushes to `main`, and manual dispatch. Both workflows have read-only repository permission and emit job output only; neither creates fixture authority, proof, release state, or publication.

## Local validation

Use the repository-owned commands from [`Makefile`](../../Makefile):

```bash
# Focused generic contract-fixture harness.
python -m pytest -q tests/schemas/test_common_contracts.py

# Configured aggregate validators and their fixture polarity.
make schemas

# Repository schema and contract tests.
make test

# Aggregate validator plus schema/contract test baseline.
make validate
```

Interpret the commands narrowly:

| Command | What a pass supports | What it does not prove |
|---|---|---|
| focused pytest | Discovered contract fixtures have the expected JSON Schema polarity. | Complete schema coverage, non-empty lanes for every schema, semantic validity, or runtime behavior. |
| `make schemas` | Configured aggregate validators accept/reject their wired fixtures as implemented. | Every validator or contract family is in the aggregate. |
| `make test` | Current `tests/schemas` and `tests/contracts` assertions pass. | Policy-engine, API, UI, map, release, or end-to-end behavior. |
| `make validate` | The current aggregate schema-validator and schema/contract test baseline passes. | Evidence closure, rights or sensitivity clearance, review approval, release readiness, or publication. |

The repository's documentation link-check workflow remains an explicit readiness hold at the evidence snapshot. A green or skipped documentation workflow must not be represented as full relative-link or external-link validation.

## Fixture case contract

Each fixture case should make its intent inspectable.

### Required case qualities

- **Deterministic:** stable input bytes and stable expected polarity.
- **Minimal:** one primary behavior per case unless the case explicitly tests interaction.
- **Reviewable:** small enough for a reviewer to understand without a live service.
- **No-network:** validation must not depend on source availability or external APIs.
- **Public-safe:** no secrets, restricted payloads, or harmful exact location detail.
- **Version-bound:** linked to the schema version and family it exercises.
- **Polarity-explicit:** clearly valid or invalid for a named reason.
- **Non-authoritative:** never presented as a real decision, evidence record, receipt, proof, release, or published object.

### Positive cases

A `valid/valid_<n>.json` case should:

- satisfy all required schema fields and constraints intended by the case;
- use synthetic identifiers and values;
- cover a supported path without implying factual truth;
- avoid redundant copies that add no distinct constraint coverage.

### Negative cases

An `invalid/invalid_<n>.json` case should:

- violate a deliberate, documented constraint;
- fail for the intended primary reason where practical;
- include a sibling expected-error file for stable review and configured CI coverage;
- avoid depending on a validator's entire prose message when a durable fragment or bounded alternative is sufficient.

A schema-invalid object is not automatically policy-denied, semantically false, or unsafe; those are separate evaluations. Likewise, a schema-valid object is not automatically meaningful, admissible, evidence-resolved, release-ready, or public-safe.

## Sensitive data, rights, and safety

Contract fixtures must use synthetic or irreversibly public-safe values.

Do not add:

- credentials, tokens, private keys, connection strings, or private endpoints;
- source-system exports, production logs, or copied restricted payloads;
- living-person private data or realistic DNA/genomic records;
- exact rare-species, archaeological, sacred/cultural, or critical-infrastructure coordinates;
- title, ownership, emergency, or life-safety examples that could be mistaken for authoritative advice;
- copyrighted or terms-restricted source material beyond an explicitly permitted minimal test excerpt;
- prompts, hidden reasoning, or private review notes.

When a sensitive behavior must be tested, use a toy identifier, generalized geometry, redacted field, deny-path example, or quarantined-state example. Record the transform and expected outcome in the family README or case documentation.

## Adding or changing a fixture family

1. Confirm the semantic contract under `contracts/`.
2. Confirm the canonical schema and version under `schemas/contracts/`.
3. Confirm the owning version and family in the corresponding fixture README.
4. Add the smallest distinct positive and negative cases.
5. Add stable expected-error evidence for each negative case.
6. Update the family and version indexes when coverage or layout changes.
7. Run the focused harness and applicable repository-owned validation commands.
8. Record failures, skips, and uncovered schemas honestly.
9. Inspect the diff for secrets, sensitive data, rights issues, and unintended authority claims.
10. Submit through review with rollback and generated-work provenance when applicable.

If the change requires a new fixture home, changes the meaning of an object, creates a new authority root, or duplicates an existing family, stop and resolve placement through Directory Rules and an ADR-backed migration before adding files.

## Change interpretation and rollback

Fixture changes are test-input changes. They may expose a schema or validator defect, but they do not themselves change KFM truth or release state.

When validation fails:

- determine whether the fixture, schema, validator, or test expectation is wrong;
- do not weaken a negative case merely to make CI green;
- do not update snapshots without reviewing the semantic and policy impact;
- quarantine or remove sensitive content from the proposed change immediately;
- preserve the failing evidence in the review discussion when safe.

Before merge, rollback is abandoning or closing the scoped pull request through normal repository controls. After merge, use a transparent revert commit or pull request for the exact fixture/documentation change and rerun the same validation. Never rewrite shared history. No data-release rollback is implied unless a separate governed release artifact was actually affected.

## Known drift and open verification

| ID | Item | Status | Required follow-up |
|---|---|---:|---|
| FIX-CONTRACT-01 | Root `fixtures/README.md` does not list `contracts/` in its current top-level lane inventory. | **CONFIRMED drift signal** | Refresh the root index in a separately scoped change. |
| FIX-CONTRACT-02 | `v1/README.md` records no release-family README although the generic harness names `release`. | **CONFIRMED bounded absence** | Inventory release schemas and decide whether fixtures are required before creating a lane. |
| FIX-CONTRACT-03 | The v1 policy index reports a stale relationship with its `sensitivity_label/` child. | **CONFIRMED in child documentation** | Reconcile the policy family index against current files and tests. |
| FIX-CONTRACT-04 | SourceDescriptor schema metadata and observed fixture-home documentation have reported different homes. | **CONFLICTED / NEEDS VERIFICATION** | Reconcile schema metadata, reusable fixture placement, tests, and migration notes. |
| FIX-CONTRACT-05 | The generic harness skips schemas without fixture directories and can be vacuous for empty case lanes. | **CONFIRMED behavior** | Decide whether coverage and non-empty polarity should be enforced for every in-scope schema. |
| FIX-CONTRACT-06 | Only six configured aggregate validators receive the stricter non-empty CI preflight. | **CONFIRMED bounded coverage** | Establish the accepted aggregate inventory and expansion rule. |
| FIX-CONTRACT-07 | The root `fixtures/` versus `tests/fixtures/` split lacks a verified permanent ADR. | **NEEDS VERIFICATION** | Keep the documented split until governance accepts a migration or permanent rule. |
| FIX-CONTRACT-08 | No `v2/README.md` resolved at the evidence snapshot. | **BOUNDED ABSENCE** | Add a version index only with an accepted schema-version and migration need. |
| FIX-CONTRACT-09 | Documentation link checking is not implemented; the current workflow is a readiness hold. | **CONFIRMED** | Validate links manually or wire an accepted deterministic checker in a separate change. |
| FIX-CONTRACT-10 | Steward identities remain placeholders. | **NEEDS VERIFICATION** | Assign owners through repository governance; do not invent names. |

This README records these signals without resolving them or creating parallel authority.

## Maintenance checklist

- [ ] Keep this file a parent boundary and version router, not a recursive payload inventory.
- [ ] Preserve the reusable `fixtures/` versus test-local `tests/fixtures/` split.
- [ ] Keep contract meaning, schema shape, policy, tests, validators, lifecycle data, receipts, proofs, release, and publication in their owning roots.
- [ ] Match fixture version, family, and schema name to the canonical schema path.
- [ ] Require distinct positive and negative cases for any fixture family claimed as covered.
- [ ] Keep expected-error evidence beside its negative JSON fixture.
- [ ] Keep fixtures deterministic, no-network, minimal, reviewable, and public-safe.
- [ ] Document snapshot or non-schema exceptions explicitly.
- [ ] Update version and family indexes when a lane is added, retired, renamed, or migrated.
- [ ] Run the focused harness and applicable aggregate validation before claiming success.
- [ ] Report skipped or vacuous coverage as incomplete.
- [ ] Preserve correction and transparent rollback paths.
- [ ] Never treat a fixture or green validation check as truth, policy approval, release approval, or publication authority.

## Evidence ledger

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix@0b9307b94c67920e3451e1d40b80d287e7364ee7` on 2026-07-20.

| Source | Status | Supports | Limit |
|---|---|---|---|
| Prior `fixtures/contracts/README.md` | **CONFIRMED** | Existing identity, purpose, v1 routing, harness summary, authority boundary, and maintenance posture. | Dated 2026-07-01; contained stale blank-file and not-run wording. |
| [`v1/README.md`](v1/README.md) | **CONFIRMED** | Bounded v1 family index and child-level drift notes. | It is partial and contains known stale relationships. |
| [`fixtures/README.md`](../README.md) | **CONFIRMED** | Reusable fixture-root boundary and distinction from test-local fixtures. | Current lane inventory omits `contracts/`. |
| [`tests/README.md`](../../tests/README.md) | **CONFIRMED** | Two-home fixture rule, generic harness convention, and current test-lane maturity. | Repository-wide case counts and permanent split remain open. |
| [`tests/fixtures/README.md`](../../tests/fixtures/README.md) | **CONFIRMED** | Test-local fixture purpose and duplication guardrail. | Child inventory and consumer wiring are partial. |
| [`test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) | **CONFIRMED, NOT RUN LOCALLY** | Seven hard-coded families, path derivation, valid/invalid polarity, and expected-error logic. | Does not require complete or non-vacuous coverage for every schema. |
| [`schema-validation.yml`](../../.github/workflows/schema-validation.yml) | **CONFIRMED definition** | Six configured aggregate validators, non-empty preflight, meta-schema checks, and invoked commands. | Workflow definition is not a current run result or release proof. |
| [`contracts-validate.yml`](../../.github/workflows/contracts-validate.yml) | **CONFIRMED definition** | Broad PR trigger and `make test` invocation. | Workflow definition is not a current run result. |
| [`Makefile`](../../Makefile) | **CONFIRMED** | `make schemas`, `make test`, and `make validate` command behavior. | Does not cover all repository test or governance surfaces. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) | **CONFIRMED doctrine** | Canonical fixture root, responsibility split, README contract, and fixture-sprawl prohibition. | Does not prove current fixture completeness or CI success. |
| [Contract schema v1 index](../../schemas/contracts/v1/README.md) | **CONFIRMED** | Canonical v1 schema-family routing and schema authority boundary. | Mixed family maturity; indexes do not prove fixture coverage. |
| [ADR-0002](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **PROPOSED / CONFLICTED** | Supporting rationale for separating contracts, schemas, policy, fixtures, tests, and validators. | Not accepted authority; fixture-home and ADR-number questions remain open. |

## Change history

- **v0.2.0 - 2026-07-20:** Reconciled the parent README with the current repository. Added the two-home fixture rule, exact harness and CI boundaries, local commands, non-vacuous coverage warning, case contract, sensitive-data rules, drift register, evidence snapshot, and rollback guidance. Preserved the prior document identity, v1 routing, authority boundary, valid/invalid layout, and non-authoritative posture.
- **v0.1.0 - 2026-07-01:** Expanded the previously blank parent file into a v1 contract-fixture index.

[Back to top](#top)

