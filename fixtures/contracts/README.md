<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/readme
title: Contract fixtures README
type: fixture-readme
version: v0.3.0
status: draft; repository-grounded
owners:
  - "@bartytime4life"
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
  - ../../tools/validators/_common/jsonschema_runner.py
  - ../../tools/validators/_common/local_resolver.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../.github/CODEOWNERS
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
  - "The current review snapshot at main@4f46eaaa444bb66f1f37d5c83b8311375ce8e572 confirms v1/README.md and does not resolve v2/README.md."
  - "The generic harness covers immediate v1 schema files in seven hard-coded families only when a matching fixture directory exists."
  - "The schema-validation workflow separately enforces non-empty positive and negative lanes for six configured aggregate validators."
  - "The generic schema harness resolves schema references from a repository-local registry; the workflow dependency-install step is separate network use."
  - "The Makefile fixtures target is a non-enforcing readiness marker and does not regenerate fixtures."
  - "Schema polarity, policy or admission outcome, evidence state, and release state are separate axes; a schema-valid DENY or ABSTAIN envelope remains a valid schema fixture."
  - "Repository evidence currently reports unresolved Directory Rules identity, home, and status collisions; this README relies only on the common responsibility-root rule and does not claim authority closure."
  - "CODEOWNERS routes fixtures/ to @bartytime4life; fixture, schema, contract, validator, policy, and documentation stewardship assignments remain NEEDS VERIFICATION."
  - "Passing fixture checks prove only the tested machine-shape behavior; they do not establish meaning, evidence closure, policy permission, release readiness, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract fixtures

Reusable, versioned examples for exercising KFM contract schemas without turning sample data into contract, schema, policy, evidence, release, or publication authority.

**Path:** `fixtures/contracts/README.md`  
**Status:** draft; repository-grounded at `main@4f46eaaa444bb66f1f37d5c83b8311375ce8e572`  
**Owning root:** `fixtures/`  
**Current version index:** [`v1/`](v1/README.md)  
**Default posture:** deterministic, no-network, public-safe, non-authoritative

**Quick navigation:** [Purpose](#purpose) · [Scope and audience](#scope-and-audience) · [Authority level](#authority-level) · [Status](#status) · [Placement](#placement-and-fixture-home-rule) · [Directory map](#directory-map-and-family-routes) · [Validation](#current-executable-behavior) · [Review burden](#review-burden) · [Fixture contract](#fixture-case-contract) · [Outcome matrix](#outcome-and-polarity-matrix) · [Safety](#sensitive-data-rights-and-safety) · [Drift](#known-drift-and-open-verification) · [Evidence](#evidence-ledger)

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

## Scope and audience

This README governs orientation and contribution rules for `fixtures/contracts/` only. It is written for fixture authors, schema and contract maintainers, validator and test contributors, reviewers, and release or policy reviewers who need to understand what a fixture result can and cannot establish.

In scope:

- reusable examples for versioned KFM contract schemas;
- routing to version and family indexes;
- schema-polarity conventions and family-specific snapshot exceptions;
- deterministic, no-network, rights-aware, and sensitivity-aware fixture design;
- current harness, validator, Makefile, and workflow behavior that was directly inspected;
- coverage gaps, authority conflicts, review burden, compatibility, correction, and rollback.

Out of scope:

- recursively documenting every JSON payload;
- defining contract semantics, schema shape, policy, source authority, evidence closure, runtime behavior, or release state;
- claiming that a documented family is complete merely because its directory or README exists;
- resolving repository-wide Directory Rules, ADR-number, fixture-home, or stewardship conflicts.

## Authority level

**Verification-supporting directory contract; non-authoritative for KFM truth, policy, evidence, and release.**

`fixtures/` is an established responsibility root for reusable test inputs. This nested directory is implementation-supporting: it holds instances consumed by schemas, validators, tests, and workflows, but it cannot make a normative or operational decision.

| Surface | Authority relationship to this README |
|---|---|
| KFM invariants and accepted governance | Higher authority; this README must remain subordinate. |
| Semantic contracts | `contracts/` defines meaning; this README may link but must not restate a competing definition. |
| Machine schemas | `schemas/contracts/` defines shape; fixtures exercise selected versions and constraints. |
| Policy and admission | `policy/` and accepted decision surfaces define admissibility; fixture directory names do not. |
| Executable tests and validators | Current code determines what is actually checked; prose does not manufacture enforcement. |
| Version and family READMEs | Child indexes refine their bounded inventory; this parent routes and does not flatten or supersede them. |
| This README | Documents placement, contribution rules, current consumers, limitations, and open drift. |

### Authority and supersession boundary

- v0.3.0 supersedes v0.2.0 of this file for parent-directory guidance only.
- It does not supersede `v1/README.md`, family READMEs, contracts, schemas, policy, tests, validators, workflows, receipts, proofs, or release records.
- The repository doctrine file is marked `draft` while also asserting canonical placement authority, and repository scan evidence reports divergent Directory Rules identities, homes, and statuses. This README therefore uses only the non-conflicting responsibility-root intersection: reusable cross-cutting fixtures remain under `fixtures/`, competing fixture homes require an explicit distinction, and new authority roots require governance review.
- No merge, receipt, fixture pass, README status, or document version converts this lane into published KFM authority.

## Status

| Item | Current evidence | Truth status |
|---|---|---:|
| Target path | `fixtures/contracts/README.md` exists on current `main`. | **CONFIRMED** |
| Document lifecycle | Draft, repository-grounded directory guidance. | **CONFIRMED** |
| Direct version index | `v1/README.md` resolves. | **CONFIRMED** |
| Later version index | `v2/README.md` did not resolve by exact-path probe. | **BOUNDED ABSENCE** |
| v1 family inventory | Six README-covered family roots; the harness also names `release`, whose v1 fixture-family README is absent. | **PARTIAL / NEEDS VERIFICATION** |
| Generic schema harness | Present and executable for discovered matching directories. | **CONFIRMED behavior; coverage is non-exhaustive** |
| Aggregate validation | Six configured validator families receive stricter non-empty CI checks. | **CONFIRMED bounded coverage** |
| Fixture regeneration | `make fixtures` prints a TODO readiness marker and performs no regeneration. | **CONFIRMED non-enforcing marker** |
| Review routing | `.github/CODEOWNERS` routes `/fixtures/` to `@bartytime4life`. | **CONFIRMED route; not proof of review or stewardship assignment** |
| Steward identities and permanent fixture-home decision | No accepted fixture-specific decision was verified. | **NEEDS VERIFICATION** |

## What belongs here

- small, deterministic JSON instances that exercise one canonical schema version and family;
- positive and negative schema-polarity cases named for the generic harness;
- stable expected-error fragments paired with negative JSON fixtures;
- family-specific input or expected-output snapshots only when the family README identifies the consumer, outcome, update rule, and exception to the generic layout;
- README files that explain purpose, tested constraint, consumer, sensitivity posture, coverage limit, and maintenance rule;
- synthetic identifiers, fixed timestamps, generalized geometry, redacted values, and bounded examples safe for a public repository.

## What does NOT belong here

- semantic contract definitions, JSON Schemas, policy modules, validator implementations, or executable test modules;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data;
- actual SourceDescriptors, EvidenceBundles, receipts, proofs, review records, release manifests, rollback cards, or correction notices presented as real governed objects;
- copied production payloads, source-system exports, live-service captures, unrestricted logs, credentials, or private endpoints;
- exact sensitive locations, living-person or realistic DNA data, title claims, emergency guidance, or rights-restricted source content;
- duplicated reusable cases under both `fixtures/` and `tests/fixtures/` without a documented consumer and migration reason;
- generated outputs whose canonical home is an artifact, receipt, proof, report, or release lane.

## Inputs

Fixture work may derive from:

- a confirmed semantic contract and its compatibility notes;
- the exact canonical schema version and `$id` being exercised;
- an executable validator or test that names the fixture path and expected polarity;
- a policy, evidence-closure, admission, runtime, or release outcome defined by its owning surface;
- a minimized synthetic reproduction of a confirmed defect;
- fixed, public-safe values authored specifically for deterministic testing.

Do not derive fixtures by copying a real governed record and merely changing its name. Unknown rights, sensitivity, source role, or provenance is a reason to synthesize a smaller case or stop, not a reason to commit the payload.

## Outputs

This directory supports deterministic test inputs and expected-output snapshots for repository validators, schema tests, and CI. Its durable outputs are reviewable fixture bytes and documentation.

It does not emit or authorize lifecycle records, validation reports, policy decisions, receipts, proofs, releases, deployments, published data, public API responses, map layers, or AI answers. A consuming tool may emit a report elsewhere, but that output must use its accepted responsibility root and authority contract.

## Placement and fixture-home rule

The inspected Directory Rules editions and current root READMEs share the placement rule that golden, valid, invalid, and synthetic test inputs belong under the `fixtures/` responsibility root. Because Directory Rules authority identity and adoption remain conflicted, this is recorded as the common placement intersection rather than a claim that one edition has final authority. KFM currently documents two fixture homes with a strict split:

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

## Directory map and family routes

The bounded README-covered structure at the review snapshot is:

```text
fixtures/contracts/
├── README.md
└── v1/
    ├── README.md
    ├── common/
    ├── evidence/
    ├── governance/
    ├── policy/
    ├── runtime/
    └── source/
```

This map is a routing view, not a complete recursive tree or a claim that every family is fully populated.

| v1 family route | README-reported coverage | Parent posture |
|---|---|---:|
| [`common/`](v1/common/README.md) | `spec_hash/` is the grounded child family. | **PARTIAL** |
| [`evidence/`](v1/evidence/README.md) | `evidence_ref/` and `evidence_bundle/` are README-covered. | **PARTIAL** |
| [`governance/`](v1/governance/README.md) | `review_record/` is populated; other reported schema relationships remain incomplete. | **PARTIAL** |
| [`policy/`](v1/policy/README.md) | `policy_decision/`; parent/child drift exists around `sensitivity_label/`. | **PARTIAL / DRIFT** |
| [`runtime/`](v1/runtime/README.md) | `ai_receipt/`, `decision_envelope/`, `run_receipt/`, and `runtime_response_envelope/` are README-covered. | **PARTIAL** |
| [`source/`](v1/source/README.md) | Mixed schema fixtures plus a documented snapshot-style provenance-check family. | **PARTIAL / MIXED STYLE** |
| `release/` | Named by the generic harness, but `fixtures/contracts/v1/release/README.md` did not resolve. | **BOUNDED ABSENCE** |

Do not confuse the separate reusable lane [`fixtures/release/`](../release/README.md) with the absent versioned path `fixtures/contracts/v1/release/`. The former contains synthetic release-governance examples; it does not fill versioned contract-schema coverage for the latter.

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

The harness calls `load_validator()` in [`jsonschema_runner.py`](../../tools/validators/_common/jsonschema_runner.py). That helper builds a registry from repository-local `schemas/contracts/v1/**/*.schema.json` files through [`local_resolver.py`](../../tools/validators/_common/local_resolver.py). Fixture execution therefore has a no-network resolution path once declared dependencies are installed. The CI dependency-install step may use the network; that is a workflow bootstrap concern, not fixture data access.

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

The aggregate runner currently prints `FAIL` lines when it feeds expected-invalid instances through its generic file validator. The subsequent polarity checks and process exit status determine whether those expected failures are correct. Review the final command result and pytest assertions; do not classify the run from an isolated log label.

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

The Makefile also exposes a `fixtures` target, but it is not an implemented generator:

```bash
make fixtures
# Current result: prints "TODO: regenerate deterministic fixtures" and exits successfully.
```

That zero exit status is a readiness marker, not proof that fixtures were generated, refreshed, normalized, or validated.

Interpret the commands narrowly:

| Command | What a pass supports | What it does not prove |
|---|---|---|
| focused pytest | Discovered contract fixtures have the expected JSON Schema polarity. | Complete schema coverage, non-empty lanes for every schema, semantic validity, or runtime behavior. |
| `make schemas` | Configured aggregate validators accept/reject their wired fixtures as implemented. | Every validator or contract family is in the aggregate. |
| `make test` | Current `tests/schemas` and `tests/contracts` assertions pass. | Policy-engine, API, UI, map, release, or end-to-end behavior. |
| `make validate` | The current aggregate schema-validator and schema/contract test baseline passes. | Evidence closure, rights or sensitivity clearance, review approval, release readiness, or publication. |
| `make fixtures` | Nothing beyond confirming the readiness marker can be invoked. | Fixture generation, determinism, freshness, completeness, or validation. |

The repository's documentation link-check workflow remains an explicit readiness hold at the evidence snapshot. A green or skipped documentation workflow must not be represented as full relative-link or external-link validation.

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life`. That mapping requests review; it is not a StewardshipAssignment, ReviewRecord, proof that review occurred, or authority to approve policy, evidence, release, or publication.

Review the smallest applicable set:

| Change | Minimum review concerns |
|---|---|
| README-only clarification | Placement, links, current executable claims, authority boundaries, and no-loss check. |
| New or changed JSON fixture | Schema version, intended polarity, tested constraint, deterministic values, rights, sensitivity, and consumer coverage. |
| Changed expected-error text | Validator-version stability, durable message fragment, and risk of accepting the wrong failure. |
| New snapshot-style family | Exception rationale, exact consumer, input/output role, update rule, authority boundary, and rollback. |
| Sensitive-domain example | Public-safe transformation, most-restrictive handling, domain or cultural review, and absence of reconstruction risk. Reviewer identities beyond the verified CODEOWNERS route remain **NEEDS VERIFICATION**. |
| Version, home, or identity change | Compatibility map, old-fixture parity, migration plan, Directory Rules review, and accepted ADR when required. |

Human review must remain distinct from generated receipt state. A pending or schema-valid receipt records provenance only.

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent reusable-fixture boundary and top-level lane index. |
| [`v1/README.md`](v1/README.md) | Current version router and bounded family inventory. |
| [`../../contracts/README.md`](../../contracts/README.md) | Semantic meaning and invariants. |
| [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md) | Versioned machine-shape authority. |
| [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md) | Current v1 schema-family index. |
| [`../../policy/README.md`](../../policy/README.md) | Admissibility, allow/deny/restrict/abstain, rights, and sensitivity behavior. |
| [`../../tests/README.md`](../../tests/README.md) | Executable proof boundary and reusable-versus-local fixture rule. |
| [`../../tests/fixtures/README.md`](../../tests/fixtures/README.md) | Test-local fixture boundary. |
| [`../../tools/validators/README.md`](../../tools/validators/README.md) | Reusable validator boundary. |
| [`../../data/receipts/generated/README.md`](../../data/receipts/generated/README.md) | AI-authorship process memory; not fixture or proof authority. |
| [`../../release/README.md`](../../release/README.md) | Release decisions, correction, and rollback authority. |

## ADRs

[`ADR-0002`](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) describes the proposed division of labor among contracts, schemas, policy, fixtures, tests, and validators. Its document status is `draft`, its decision status is `proposed`, and its number assignment is conflict-bearing. It is useful context but not accepted authority.

No accepted fixture-home ADR was verified at the review snapshot. Creating a new fixture root, making both fixture homes compete, changing object identity, or moving a versioned family across authority roots therefore remains an ADR-class or governance-blocked action. Routine cases that preserve the existing responsibility split do not gain ADR authority merely by linking this section.

## Last reviewed

- **Date:** 2026-07-20
- **Repository snapshot:** `bartytime4life/Kansas-Frontier-Matrix@4f46eaaa444bb66f1f37d5c83b8311375ce8e572`
- **Target blob at snapshot:** `8ee089cf5f35388ad1cde89f09cb211470702f28`
- **Reviewed surfaces:** target and v1 indexes, family routes, root and test-local fixture READMEs, generic harness, local schema resolver, aggregate runner boundary, Makefile targets, schema/contract workflows, CODEOWNERS, Directory Rules, proposed ADR-0002, and generated-receipt contract.
- **Not established:** complete recursive fixture inventory, permanent Directory Rules authority, accepted ADR inventory, complete fixture coverage, every family consumer, steward assignments, or public-release readiness.

Re-review after a schema-version addition, fixture-home decision, harness family change, validator inventory change, `make fixtures` implementation, workflow change, sensitivity/rights rule change, or accepted ADR affecting this boundary.

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

## Outcome and polarity matrix

Do not collapse machine shape, governed outcome, evidence state, lifecycle state, and release state into one `valid` or `invalid` label.

| Axis | Example values | What `valid/` and `invalid/` mean |
|---|---|---|
| Schema polarity | conforms / does not conform | This is the axis used by the generic harness. |
| Runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Any outcome may be schema-valid when the envelope conforms. |
| Policy or admission outcome | allow, restrict, abstain, deny, review required | The outcome must come from the owning policy or decision contract, not the fixture directory name. |
| Lifecycle routing | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED | A schema-valid record may still be quarantined or blocked from promotion. |
| Evidence state | resolved, missing, stale, conflicted, unsupported | Evidence posture controls claim use; it is not inferred from JSON Schema success. |
| Release state | candidate, approved, denied, withdrawn, corrected, rolled back | Release state requires governed records; a fixture can only model an example. |

Operational rules:

- Put a schema-conforming `DENY`, `ABSTAIN`, `ERROR`, quarantine, or release-blocked envelope under `valid/` when the case is testing its machine shape.
- Put an object under `invalid/` for the generic harness only when it is deliberately schema-invalid.
- Test policy denial, evidence abstention, quarantine routing, finite runtime outcomes, and release blocking with the owning policy/runtime/admission/release tests in addition to schema polarity.
- Record both expected axes in family documentation, for example: `schema: valid; runtime: ABSTAIN; reason: missing EvidenceBundle`.
- Do not rename a negative business outcome to schema-invalid merely to reuse the generic harness.

### Minimum case declaration

The family README or an adjacent case index should identify, where applicable:

- canonical contract path and object name;
- schema path, version, and `$id`;
- consuming test, validator, or workflow;
- schema polarity and primary constraint exercised;
- expected policy, runtime, admission, evidence, or release outcome;
- stable reason code or durable expected-error fragment;
- source role, rights, sensitivity, and public-safe transformation posture;
- fixed identity/time assumptions and whether hashes are shape-only or recomputed;
- known untested semantics and rollback or replacement rule.

## Deterministic identity, time, and provenance

- Use stable synthetic identifiers; do not generate a new random UUID or ULID on every test run.
- Use fixed, timezone-qualified timestamps. Do not use the current clock unless the owning test explicitly freezes and tests it.
- Preserve distinct time meanings required by the contract. Do not copy one timestamp into source, retrieval, valid, release, and correction fields merely to satisfy a format.
- Keep digests, `spec_hash` values, canonicalization inputs, and referenced fixture paths coherent when a semantic validator checks them. When only shape is tested, say so rather than implying digest verification.
- Preserve source-role vocabulary and anti-collapse rules from the owning contract or schema. A syntactically valid role value does not make a source authoritative for every claim.
- Prefer numbered stable filenames only while their identity remains unambiguous. Use a descriptive family README or case table to explain the tested behavior.
- Record whether a snapshot was manually authored, minimized from a public-safe defect, or generated by a deterministic tool. Generated fixture bytes still require review and do not self-approve.
- Never store prompts, hidden reasoning, or tool transcripts as fixture provenance. AI-authored repository changes use the accepted generated-receipt lane; real governed objects use their own receipt and proof contracts.

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

## Object-family readiness relation

The proposed contract/schema split ADR describes a broader object-family packet. This fixture root supplies only the example portion of that packet.

| Readiness surface | Expected relationship | Can this README claim it complete? |
|---|---|---:|
| Semantic contract | Names meaning, invariants, compatibility, and lifecycle semantics. | No |
| Machine schema | Defines versioned shape and `$id`. | No |
| Positive and negative fixtures | Exercise selected supported and rejected shapes. | Only for individually inventoried cases |
| Validator | Reusable executable checker consumes the canonical schema and fixtures. | No; must inspect implementation |
| Policy or evidence-closure test | Proves admissibility, deny/abstain behavior, or EvidenceRef-to-EvidenceBundle closure. | No |
| Cross-references | Contract, schema, fixture, policy, validator, and test links agree. | Only for links explicitly checked |
| Compatibility and rollback | Preserves old-fixture parity, migration, deprecation, and reversal. | No; family-specific evidence required |
| Release and correction | Governed promotion, rollback, withdrawal, and correction records exist. | Never from fixture presence |

Do not promote a family from “fixtures exist” to “validated,” “release-ready,” or “published” without the other accepted surfaces and their executable evidence. Because ADR-0002 remains proposed, this table is a review aid, not ratification of that ADR.

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
| FIX-CONTRACT-10 | Fixture, schema, contract, validator, policy, and documentation stewardship assignments remain unresolved beyond the verified CODEOWNERS route. | **NEEDS VERIFICATION** | Record approved role assignments through repository governance; do not infer them from review routing. |
| FIX-CONTRACT-11 | `make fixtures` is a successful-exit TODO marker, not deterministic regeneration. | **CONFIRMED** | Implement and review a generator before citing this target as freshness or reproducibility evidence. |
| FIX-CONTRACT-12 | Repository scan evidence reports three divergent Directory Rules artifacts and no reliably accepted ADR index. | **CONFLICTED / BLOCKED OUTSIDE THIS FILE** | Reconcile authority identity, canonical home, status, mirrors, and supersession before claiming final doctrine closure. |
| FIX-CONTRACT-13 | CODEOWNERS supplies a verified GitHub review route, while fixture/schema/contract/policy steward assignments remain unresolved. | **CONFIRMED route / NEEDS VERIFICATION stewardship** | Keep GitHub routing and governance roles distinct; record approved assignments through the accepted governance surface. |
| FIX-CONTRACT-14 | Generic `valid`/`invalid` placement proves schema polarity only and can be confused with policy, runtime, admission, or release outcomes. | **CONFIRMED semantic risk** | Record the independent expected outcome axes and test them in their owning executable lanes. |

This README records these signals without resolving them or creating parallel authority.

## Maintenance checklist

- [ ] Keep this file a parent boundary and version router, not a recursive payload inventory.
- [ ] Preserve the reusable `fixtures/` versus test-local `tests/fixtures/` split.
- [ ] Keep contract meaning, schema shape, policy, tests, validators, lifecycle data, receipts, proofs, release, and publication in their owning roots.
- [ ] Match fixture version, family, and schema name to the canonical schema path.
- [ ] Require distinct positive and negative cases for any fixture family claimed as covered.
- [ ] Keep schema polarity separate from policy, runtime, admission, evidence, lifecycle, and release outcomes.
- [ ] Keep expected-error evidence beside its negative JSON fixture.
- [ ] Keep fixtures deterministic, no-network, minimal, reviewable, and public-safe.
- [ ] Keep synthetic identity, time fields, hashes, source roles, and provenance assumptions stable and explicit.
- [ ] Document snapshot or non-schema exceptions explicitly.
- [ ] Update version and family indexes when a lane is added, retired, renamed, or migrated.
- [ ] Run the focused harness and applicable aggregate validation before claiming success.
- [ ] Do not cite `make fixtures` as regeneration until its TODO marker is replaced by reviewed executable behavior.
- [ ] Report skipped or vacuous coverage as incomplete.
- [ ] Obtain the applicable CODEOWNERS and governance review without treating routing as approval.
- [ ] Preserve correction and transparent rollback paths.
- [ ] Never treat a fixture or green validation check as truth, policy approval, release approval, or publication authority.

## Common questions

### Why can a `DENY` example live under `valid/`?

Because `valid/` means the JSON conforms to the tested schema. `DENY` is a governed outcome carried by a conforming decision or runtime envelope. A separate policy or runtime test must verify that the outcome is correct.

### Should a reusable contract fixture go under `tests/fixtures/`?

Not by default. Current repository documentation assigns reusable cross-cutting cases to `fixtures/` and small test-local cases to `tests/fixtures/`. Do not duplicate the same family. If ownership changes, document the migration, consumers, compatibility, and accepted governance decision.

### Does `make fixtures` regenerate this tree?

No. At the review snapshot it only prints a TODO message and exits successfully. Use explicit authored changes or an accepted deterministic generator, then run schema and contract validation separately.

### Does a green schema workflow prove complete contract coverage?

No. The generic harness skips schemas without matching fixture directories and can be vacuous when case globs are empty. The stricter workflow preflight covers six configured aggregate families only. Meaning, policy, evidence, rights, sensitivity, runtime, release, and publication remain separate burdens.

### Can a production record be anonymized and committed as a fixture?

Only when an accepted rights and sensitivity review establishes that the transformed content is irreversibly public-safe and necessary. The safer default is a minimal synthetic case that cannot reconstruct a person, location, source payload, or restricted fact.

## Evidence ledger

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix@4f46eaaa444bb66f1f37d5c83b8311375ce8e572` on 2026-07-20.

| Source and precise location | Status | Supports | Does not prove |
|---|---|---|---|
| Prior target blob `8ee089cf5f35388ad1cde89f09cb211470702f28` at `fixtures/contracts/README.md` | **CONFIRMED** | v0.2 identity, routing, harness detail, case rules, drift, and rollback preserved as the editing baseline. | That v0.2 contained every required directory-contract or fixture-profile concern. |
| [`v1/README.md` — “Observed family roots” and “Known exceptions and drift”](v1/README.md#observed-family-roots) | **CONFIRMED** | Six README-covered family routes, mixed maturity, snapshot exception, and absent release-family README. | Complete recursive inventory or consumer coverage. |
| [`fixtures/README.md` — “Placement basis” and “Current top-level lane inventory”](../README.md#placement-basis) | **CONFIRMED** | Reusable root posture and distinction from test-local fixtures. | Its lane index omits the existing `contracts/` lane. |
| [`tests/README.md` — “Fixture and test-data contract” through “Outcome vocabularies”](../../tests/README.md#fixture-and-test-data-contract) | **CONFIRMED** | Two-home rule, required fixture classes, non-vacuity, finite outcomes, determinism, network, and passing-check limits. | Permanent fixture-home governance or complete test coverage. |
| [`tests/fixtures/README.md` — “Fixture-home rule” and “Run posture”](../../tests/fixtures/README.md#fixture-home-rule) | **CONFIRMED** | Test-local purpose, duplication guardrail, and deterministic/no-network posture. | Every child or consumer is wired. |
| [`test_common_contracts.py` — `FAMILIES`, `_schema_cases()`, and `test_contract_fixtures()`](../../tests/schemas/test_common_contracts.py) | **CONFIRMED definition** | Seven hard-coded families, immediate-schema discovery, skip behavior, filename globs, polarity, and expected-error matching. | Complete or non-vacuous coverage for every schema. |
| [`jsonschema_runner.py` — `load_validator()`, `validate_files()`, and `run()`](../../tools/validators/_common/jsonschema_runner.py) plus [`local_resolver.py` — `build_registry()`](../../tools/validators/_common/local_resolver.py) | **CONFIRMED definition** | Repository-local schema registry, aggregate fixture execution, and final polarity rechecks. | That every semantic reference, policy result, or digest is validated. |
| [`schema-validation.yml` — job `validate-fixtures-against-schemas`](../../.github/workflows/schema-validation.yml) | **CONFIRMED definition** | Six configured aggregates, non-empty polarity lanes, expectation files, schema parsing, Draft 2020-12 checks, unique `$id` checks, `make schemas`, and pytest. | A workflow definition is not a run result, proof, or publication authority. |
| [`contracts-validate.yml` — job `validate`](../../.github/workflows/contracts-validate.yml) | **CONFIRMED definition** | Pull-request/main/manual triggers and `make test`. | Complete semantic equivalence across contracts, schemas, APIs, fixtures, or policy. |
| [`Makefile` — targets `schemas`, `test`, `validate`, and `fixtures`](../../Makefile) | **CONFIRMED** | Exact command scope and the non-enforcing `fixtures` TODO marker. | Fixture regeneration or repository-wide readiness. |
| [`.github/CODEOWNERS` — `/fixtures/`](../../.github/CODEOWNERS) | **CONFIRMED route** | GitHub review routing to `@bartytime4life`. | Stewardship assignment, completed review, separation of duties, or merge approval. |
| [Directory Rules — §§3, 6.6, 13.5, and 15](../../docs/doctrine/directory-rules.md#15-required-readme-contract) | **CONFLICTED authority / common rules corroborated** | Responsibility-root placement, competing-home guardrail, fixture-sprawl warning, and root README contract appear in the inspected edition. | Final authority identity, canonical home, adoption, or supersession while divergent artifacts remain unresolved. |
| Repository scan commit `cd477b176888710eb2506a203b62f62b57c844dc` — `state_changes` and `required_human_decision` in the commit message | **CONFIRMED engineering scan; non-authoritative** | Reports three divergent Directory Rules artifacts, no reliable accepted-ADR index, and required human reconciliation. | The repair commit is not an ADR, doctrine adoption, or drift-register resolution. |
| [Contract schema v1 index](../../schemas/contracts/v1/README.md) | **CONFIRMED mixed maturity** | v1 schema-family routing and schema authority boundary. | Fixture completeness or semantic readiness. |
| [ADR-0002 — status block, decision, readiness packet, compatibility, and rollback](../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT / PROPOSED / CONFLICTED** | Review rationale for separating contracts, schemas, policy, fixtures, tests, validators, and broader object-family readiness. | Accepted authority or resolved fixture-home and ADR-number decisions. |

## Change history

- **v0.3.0 - 2026-07-20:** Added the missing scope/audience, authority level, status, accepted/excluded material, inputs/outputs, direct family map, CODEOWNERS review burden, related-folder and ADR routing, last-reviewed record, local resolver behavior, `make fixtures` readiness-marker warning, schema-polarity versus governed-outcome matrix, deterministic identity/time/provenance rules, broader object-family readiness relation, common questions, precise evidence locations, and Directory Rules authority-conflict disclosure. No fixture payload, schema, contract, policy, test, validator, workflow, release, or publication behavior changed.
- **v0.2.0 - 2026-07-20:** Reconciled the parent README with the current repository. Added the two-home fixture rule, exact harness and CI boundaries, local commands, non-vacuous coverage warning, case contract, sensitive-data rules, drift register, evidence snapshot, and rollback guidance. Preserved the prior document identity, v1 routing, authority boundary, valid/invalid layout, and non-authoritative posture.
- **v0.1.0 - 2026-07-01:** Expanded the previously blank parent file into a v1 contract-fixture index.

[Back to top](#top)
