<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/common/readme
title: fixtures/contracts/v1/common/ — Common Contract Fixture Family Index
type: readme; directory-readme; contract-fixture-index; valid-invalid-schema-cases; non-authoritative
version: v0.2.0
status: draft; repository-grounded; partial-coverage; fixture-only
owners: OWNER_TBD — Schema steward · Common-contract steward · Fixture steward · Validator steward · Test/QA steward · Docs steward
created: NEEDS VERIFICATION — file predates the 2026-06-30 v0.1.0 expansion
updated: 2026-07-19
supersedes: v0.1.0
policy_label: public-review; fixtures; common-contracts; synthetic-only; non-authoritative
owning_root: fixtures/
current_path: fixtures/contracts/v1/common/README.md
truth_posture: >
  CONFIRMED existing parent README, four directly verified common schemas and paired semantic
  contracts, one verified fixture family (`spec_hash`), generic pytest discovery behavior,
  and current validator file posture / PROPOSED future fixture families and coverage repairs /
  UNKNOWN production consumers, branch-protection coupling, and complete recursive inventory /
  NEEDS VERIFICATION owners, CODEOWNERS, policy integration, full-repository test result,
  and fixture coverage for identity_token, temporal_window, and spatial_geometry
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 860ccaececd0562dad22694a046215807495f1dc
  prior_blob: 15fa7d8282c72c6f54984ea853e1e06e6cd525c1
  spec_hash_schema_blob: 80b496b01b8de8c0e8ba67bf020977e6b1f3c652
  identity_token_schema_blob: f3eace84a75c2dd97cfabfa7661a098e4353e825
  temporal_window_schema_blob: 70b96839615551164d3964596dea238c33709616
  spatial_geometry_schema_blob: 97921f5f98cb34a84caaf4df7a594f5af6d57fba
  generic_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
related:
  - ../README.md
  - ../../../README.md
  - spec_hash/README.md
  - ../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../../../schemas/contracts/v1/common/temporal_window.schema.json
  - ../../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../../contracts/common/spec_hash.md
  - ../../../../contracts/common/identity_token.md
  - ../../../../contracts/common/temporal_window.md
  - ../../../../contracts/common/spatial_geometry.md
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, common, json-schema, valid, invalid, expected-error, no-network, fail-closed, partial-coverage, non-authoritative]
notes:
  - "v0.2.0 replaces the one-family parent inventory with a repository-grounded coverage matrix for four directly verified common schemas."
  - "Only `spec_hash/` is confirmed as a populated, README-covered fixture family in this inspection."
  - "The generic pytest harness skips schemas whose derived fixture directory does not exist and does not require non-empty valid and invalid lanes."
  - "This documentation change does not create fixtures, implement validators, change schemas or contracts, alter policy, or authorize release or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Common Contract Fixture Family Index

`fixtures/contracts/v1/common/`

> **Purpose.** Index deterministic positive and negative fixtures for shared KFM contract schemas while keeping fixture examples subordinate to semantic contracts, machine schemas, policy, evidence, review, release, and publication authority.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-orange">
  <img alt="Version: v0.2.0" src="https://img.shields.io/badge/version-v0.2.0-informational">
  <img alt="Schemas directly verified: four" src="https://img.shields.io/badge/schemas%20verified-four-1f6feb">
  <img alt="Fixture families verified: one" src="https://img.shields.io/badge/fixture%20families%20verified-one-yellow">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-success">
  <img alt="Coverage: partial" src="https://img.shields.io/badge/coverage-partial-critical">
</p>

> [!IMPORTANT]
> A passing fixture proves only that the paired schema accepts or rejects the tested JSON shape. It does not establish semantic truth, deterministic identity, temporal correctness, geometry validity, geoprivacy safety, evidence closure, policy approval, review approval, release readiness, or publication authority.

> [!WARNING]
> The current generic harness adds a schema case only when the derived fixture directory exists. Missing fixture families are therefore skipped rather than failed. It also does not require at least one valid and one invalid file inside every discovered family. A green test result is not complete common-schema fixture coverage.

**Quick links:** [Status](#status-and-evidence-boundary) · [Scope](#scope-and-audience) · [Placement](#placement-and-authority) · [Coverage](#current-coverage-matrix) · [Harness](#executable-harness-and-coverage-boundary) · [Layout](#fixture-family-layout) · [Outcomes](#fixture-outcome-language) · [Safety](#no-network-rights-and-sensitivity-posture) · [Validation](#validation) · [Maintenance](#maintenance-and-change-discipline) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

---

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| This README | **CONFIRMED prior v0.1.0 file** | Revised in place; prior blob is pinned in the meta block. |
| Directly verified common schemas | **CONFIRMED: four files** | `spec_hash`, `identity_token`, `temporal_window`, and `spatial_geometry` schemas exist at the pinned base. |
| Paired semantic contracts | **CONFIRMED: four draft files** | Each verified schema has a corresponding `contracts/common/*.md` file. |
| Verified populated fixture family | **CONFIRMED: `spec_hash/`** | One valid fixture, one invalid fixture, and one expected-error sidecar are documented by the child family. |
| Other declared fixture roots | **NEEDS VERIFICATION / coverage not established** | Direct fetches found no family README for `identity_token/`, `temporal_window/`, or `spatial_geometry/`. |
| Generic pytest harness | **CONFIRMED executable code** | It validates discovered valid and invalid JSON files and optional expected-error sidecars. |
| One-to-one schema coverage | **NOT ESTABLISHED** | Missing fixture directories and empty fixture lanes do not fail this harness. |
| Dedicated common validators | **PARTIAL** | `spec_hash`, `temporal_window`, and `spatial_geometry` validators are placeholders; the schema-declared identity validator path was not found. |
| Current full-repository test result | **NEEDS VERIFICATION** | No local checkout test run is claimed by this README revision. |
| Production adoption | **UNKNOWN** | Fixture and schema presence do not prove producers or consumers. |

This inventory is bounded to the files directly inspected at `main@860ccaececd0562dad22694a046215807495f1dc`. It is not a recursive tree attestation.

[Back to top](#top)

---

## Scope and audience

This parent directory coordinates fixture coverage for reusable schemas under `schemas/contracts/v1/common/`.

It is intended for:

- schema and contract stewards;
- fixture and validation maintainers;
- reviewers checking positive and negative coverage;
- CI maintainers evaluating whether a test is non-vacuous;
- downstream object-family owners reusing common shapes;
- documentation maintainers tracking drift between declared and implemented fixture surfaces.

This directory owns fixture-family navigation, coverage posture, polarity conventions, and links to authority surfaces. It does **not** own schema shape, contract meaning, validator implementation, policy decisions, source admission, lifecycle state, evidence, proof, release, runtime behavior, or public output.

[Back to top](#top)

---

## Placement and authority

### Directory Rules basis

`fixtures/` is the existing responsibility root for synthetic, reviewable validation inputs. The version, family, object, and polarity segments keep common contract fixtures separate from schemas, contracts, policy, tools, tests, lifecycle data, receipts, proofs, and release records.

```text
fixtures/
└── contracts/
    └── v1/
        └── common/
            ├── README.md                 # this index
            └── <schema_name>/
                ├── README.md
                ├── valid/
                │   ├── README.md
                │   └── valid_<n>.json
                └── invalid/
                    ├── README.md
                    ├── invalid_<n>.json
                    └── invalid_<n>.expected_error.txt
```

| Responsibility | Owning surface |
|---|---|
| Shared semantic meaning | [`contracts/common/`](../../../../contracts/common/README.md) |
| Common machine shape | [`schemas/contracts/v1/common/`](../../../../schemas/contracts/v1/common/README.md) |
| Fixture examples and expected-error sidecars | This directory and its child families |
| Generic schema-fixture execution | [`tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) |
| Dedicated validator implementation | `tools/validators/` |
| Admissibility and exposure decisions | `policy/` |
| Evidence, lifecycle, receipts, proofs, catalog, release, and publication | Their separate governed roots |

### Known placement tension

The root [`fixtures/README.md`](../../../README.md) currently distinguishes `fixtures/` as runtime/synthetic corpora and `tests/fixtures/` as test-only data. The live common-schema harness, existing `fixtures/contracts/v1/` tree, and Directory Rules fixture responsibility support this contract-fixture lane.

This README records that documentation drift. It does not relocate the lane, redefine the root, or settle the conflict without a broader root-level review.

[Back to top](#top)

---

## Current coverage matrix

Four common schema and semantic-contract pairs were directly verified. Fixture coverage is asymmetric.

| Common object | Semantic contract | Schema-declared fixture root | Verified fixture coverage | Dedicated validator posture |
|---|---|---|---|---|
| `spec_hash` | [`contracts/common/spec_hash.md`](../../../../contracts/common/spec_hash.md) | `fixtures/contracts/v1/common/spec_hash/` | **CONFIRMED:** [`spec_hash/README.md`](spec_hash/README.md), one valid case, one invalid case, one expected-error sidecar | [`validate_spec_hash.py`](../../../../tools/validators/validate_spec_hash.py) exists but raises `NotImplementedError` |
| `identity_token` | [`contracts/common/identity_token.md`](../../../../contracts/common/identity_token.md) | `fixtures/contracts/v1/common/identity_token/` | **NEEDS VERIFICATION:** family README not found; valid/invalid coverage not established | Schema-declared `tools/validators/validate_identity_token.py` was not found |
| `temporal_window` | [`contracts/common/temporal_window.md`](../../../../contracts/common/temporal_window.md) | `fixtures/contracts/v1/common/temporal_window/` | **NEEDS VERIFICATION:** family README not found; valid/invalid coverage not established | [`validate_temporal_window.py`](../../../../tools/validators/validate_temporal_window.py) exists but raises `NotImplementedError` |
| `spatial_geometry` | [`contracts/common/spatial_geometry.md`](../../../../contracts/common/spatial_geometry.md) | `fixtures/contracts/v1/common/spatial_geometry/` | **NEEDS VERIFICATION:** family README not found; valid/invalid coverage not established | [`validate_spatial_geometry.py`](../../../../tools/validators/validate_spatial_geometry.py) exists but raises `NotImplementedError` |

### Verified `spec_hash` cases

| Case | File | Expected behavior |
|---|---|---|
| Minimal valid object | [`spec_hash/valid/valid_1.json`](spec_hash/valid/valid_1.json) | Produces zero schema errors. |
| Missing required value | [`spec_hash/invalid/invalid_1.json`](spec_hash/invalid/invalid_1.json) | Produces at least one schema error because `value` is absent. |
| Expected error | [`spec_hash/invalid/invalid_1.expected_error.txt`](spec_hash/invalid/invalid_1.expected_error.txt) | Matches the reviewed missing-required-property message. |

No additional common fixture family is claimed as populated by this parent index.

[Back to top](#top)

---

## Executable harness and coverage boundary

[`tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) includes `common` in its configured family list and derives each candidate fixture path as:

```text
schemas/contracts/v1/common/<name>.schema.json
                      ↓
fixtures/contracts/v1/common/<name>/
```

For every **discovered** family:

1. `valid/valid_*.json` files must produce zero JSON Schema errors;
2. `invalid/invalid_*.json` files must produce at least one JSON Schema error;
3. a sibling `invalid_<n>.expected_error.txt`, when present, must match the combined error messages.

### What the harness currently proves

- collected valid cases match the paired schema;
- collected invalid cases are rejected;
- reviewed expected-error text or patterns match when a sidecar exists;
- schema loading and fixture JSON parsing succeed for the exercised cases.

### What the harness does not currently prove

- every common schema has a fixture directory;
- every discovered fixture directory contains at least one valid and one invalid case;
- every invalid case has an expected-error sidecar;
- schema metadata `x-kfm.fixtures_root` matches the path derived by the test;
- dedicated validators exist or are implemented;
- semantic invariants beyond JSON Schema are enforced;
- policy, evidence, rights, sensitivity, release, or public-safety gates pass.

The `schema-validation` workflow adds explicit non-vacuous checks for five aggregate validator families, but those configured checks do not include these common schemas. It later runs the generic schema and contract tests, which retain the common-family skip behavior described above.

### Coverage implication

```text
green generic test
≠ every common schema has fixtures
≠ every fixture family is non-empty
≠ dedicated validator enforcement
≠ semantic or policy correctness
```

Until presence and non-vacuity checks cover the common family, missing lanes must remain visible as coverage gaps rather than inferred passes.

[Back to top](#top)

---

## Fixture family layout

A common fixture family should use this reviewable pattern:

```text
<schema_name>/
├── README.md
├── valid/
│   ├── README.md
│   └── valid_<n>.json
└── invalid/
    ├── README.md
    ├── invalid_<n>.json
    └── invalid_<n>.expected_error.txt
```

### Accepted material

| Item | Purpose |
|---|---|
| `<schema_name>/README.md` | Defines the local fixture boundary, exact inventory, schema and contract basis, coverage limits, and validation command. |
| `valid/valid_<n>.json` | Minimal synthetic object expected to pass the paired schema. |
| `valid/README.md` | Documents positive-case intent and limits. |
| `invalid/invalid_<n>.json` | Minimal synthetic object expected to fail for one primary reason. |
| `invalid/invalid_<n>.expected_error.txt` | Stable expected message or reviewed pattern for the paired negative case. |
| `invalid/README.md` | Documents rejection intent, expected cause, and failure interpretation. |

### Exclusions

Do not place these under this fixture index:

- JSON Schema definitions or duplicate schema copies;
- semantic contract prose other than local links and fixture notes;
- validator or policy implementation;
- source payloads, live API responses, or production data;
- credentials, secrets, tokens, private identifiers, or exact sensitive coordinates;
- actual SourceDescriptors, EvidenceBundles, receipts, proofs, catalog objects, release records, or published artifacts;
- generated CI output or logs;
- examples whose rights, origin, or public-safety posture is unclear.

[Back to top](#top)

---

## Fixture outcome language

The following labels describe test expectations; they are not policy decisions or runtime authority.

| Outcome | Meaning |
|---|---|
| `EXPECTED_ACCEPTANCE` | A collected valid fixture produces zero schema errors. |
| `EXPECTED_REJECTION` | A collected invalid fixture fails for the intended reviewed reason. |
| `UNEXPECTED_ACCEPTANCE` | An invalid fixture produces no errors. |
| `UNEXPECTED_REJECTION` | A valid fixture produces one or more errors. |
| `WRONG_REJECTION` | An invalid fixture fails, but not for the intended reason. |
| `FIXTURE_ERROR` | Fixture JSON or its expected-error sidecar is malformed, missing, or ambiguous. |
| `HARNESS_ERROR` | Schema loading, imports, dependencies, resolver behavior, or test execution fails. |
| `UNCOLLECTED` | A schema or fixture exists but is skipped by discovery or filename conventions. |

`ABSTAIN`, `DENY`, `QUARANTINE`, and runtime `ERROR` cases belong in the owning policy, source-admission, runtime, or domain fixture family when those outcomes are part of that object's contract. They must not be invented as common JSON Schema outcomes merely to make this index look comprehensive.

A missing file, missing dependency, placeholder validator, parser crash, or unrelated nonzero exit is not `EXPECTED_REJECTION`.

[Back to top](#top)

---

## No-network, rights, and sensitivity posture

Fixture evaluation should be deterministic and network-free after declared dependencies are installed.

Rules:

- use synthetic, compact, reviewable JSON;
- do not fetch upstream services during fixture execution;
- do not copy restricted or uncertain-rights source payloads into this lane;
- do not use real living-person, DNA, private-land, archaeology, rare-species, rare-plant, or critical-infrastructure records;
- geometry cases must be synthetic and must not imply that schema acceptance authorizes exposure;
- `spatial_geometry` fixtures must keep precision-bucket testing separate from geometry validity, CRS transformation, geoprivacy, and policy approval;
- temporal cases must keep format validation separate from chronology, freshness, supersession, and correction semantics;
- identity cases must not use credentials or present a token as proof of identity or authorization;
- hash cases must not use private production hashes or imply canonicalization equivalence.

The GitHub workflows may use network access to install declared dependencies. The fixture logic itself should remain offline and reproducible.

[Back to top](#top)

---

## Validation

### Repository-native command

```bash
python -m pytest -q tests/schemas/test_common_contracts.py
```

A broader repository-owned lane is:

```bash
make test
```

### Documentation and fixture checks

Before claiming this index is current:

1. verify the target file and every linked authoritative path at a pinned ref;
2. compare direct common schema filenames with documented fixture families;
3. confirm each populated family has a README, non-empty valid lane, non-empty invalid lane, and reviewed sidecars where required;
4. run the bounded pytest command;
5. distinguish collected-case success from schema-tree coverage;
6. check that no fixture redefines contract meaning, policy, evidence, release, or publication authority;
7. scan changed files for secrets, real source data, and sensitive material;
8. validate Markdown hierarchy, links, code fences, whitespace, and final newline.

### Acceptance criteria for a populated common family

- at least one valid fixture is collected and accepted;
- at least one invalid fixture is collected and rejected;
- each negative case has one primary concern;
- expected-error evidence identifies the intended failure;
- the family README states what remains untested;
- the paired contract and schema are linked;
- dedicated validator posture is accurate;
- all examples are synthetic, deterministic, public-safe, and rights-safe.

Passing the generic suite establishes only the behavior of collected cases. It does not establish complete common-family coverage or release-grade proof.

[Back to top](#top)

---

## Maintenance and change discipline

When adding or changing a common schema:

- update its semantic contract and machine schema together when meaning or shape changes;
- create or revise the matching fixture family;
- add both positive and negative cases for every material boundary;
- update the local family README and this parent coverage matrix;
- preserve deterministic names and one-concern negative fixtures;
- verify schema metadata paths rather than copying them blindly;
- implement or accurately label dedicated validators;
- update the generic harness or add a separate presence/non-vacuity test when coverage requirements change;
- keep root-level fixture documentation drift visible until resolved;
- record migration and rollback when a common concept moves to a more specific owner.

Do not silently treat a missing fixture directory as “not applicable.” Record the gap as `NEEDS VERIFICATION`, create a reviewed family, or move the schema through a governed deprecation/migration decision.

### Definition of done for this index

- [ ] Owners and CODEOWNERS coverage are confirmed.
- [x] Four directly verified common schemas and contracts are indexed.
- [x] Verified `spec_hash` coverage is linked without overstating it.
- [x] Missing or unverified common fixture families are visible.
- [x] Generic harness skip and non-vacuity limits are documented.
- [ ] `identity_token`, `temporal_window`, and `spatial_geometry` fixture coverage is implemented or explicitly dispositioned.
- [ ] Dedicated validator gaps are resolved or formally accepted as scoped placeholders.
- [ ] Parent `fixtures/contracts/v1/README.md`, `fixtures/README.md`, schema-family README, and contract-family README are reconciled with current inventory.
- [ ] Bounded and repository-wide test results are recorded from the final revision.
- [ ] Human review is complete.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Complete recursive common schema and fixture inventory | **NEEDS VERIFICATION** | Tree listing or mounted checkout at the final head. |
| `identity_token` fixture family | **NEEDS VERIFICATION** | Family files plus positive/negative test evidence. |
| `temporal_window` fixture family | **NEEDS VERIFICATION** | Family files plus format, enum, and interval-semantics coverage decision. |
| `spatial_geometry` fixture family | **NEEDS VERIFICATION** | Family files plus shape, precision, geometry-validity, CRS, and geoprivacy coverage decision. |
| `validate_identity_token.py` | **NEEDS VERIFICATION / declared path absent in this inspection** | Implemented validator or corrected schema metadata with review. |
| Placeholder dedicated validators | **NEEDS VERIFICATION** | Implementations, tests, and explicit finite exit behavior. |
| Common-family presence/non-vacuity enforcement | **PROPOSED improvement** | Test or workflow assertion that every in-scope schema has non-empty positive and negative lanes. |
| Root fixture placement wording | **DRIFT / NEEDS VERIFICATION** | Root README update, ADR, or accepted migration decision. |
| Parent indexes | **DRIFT / refresh needed** | Reconcile current schemas/contracts/fixtures without broadening this PR. |
| Branch-protection required checks | **UNKNOWN** | Repository ruleset/branch-protection evidence. |
| Production consumers | **UNKNOWN** | Import, runtime, API, pipeline, manifest, or release evidence. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `fixtures/contracts/v1/common/README.md` blob `15fa7d8282c72c6f54984ea853e1e06e6cd525c1` | **CONFIRMED** | Existing parent purpose, `spec_hash` inventory, authority boundary, and earlier drift note. | Inventory predates the current grounded child family and omits three verified schemas. |
| [`spec_hash/README.md`](spec_hash/README.md) | **CONFIRMED repository-grounded child README** | One valid fixture, one invalid fixture, expected-error sidecar, harness behavior, and placeholder validator. | Does not prove other common fixture families. |
| Four `schemas/contracts/v1/common/*.schema.json` files linked above | **CONFIRMED direct reads** | Machine shapes and declared contract, fixture, validator, policy metadata. | Each schema carries `x-kfm.status: PROPOSED`; metadata does not prove target existence. |
| Four `contracts/common/*.md` files linked above | **CONFIRMED draft semantic contracts** | Meaning and explicit non-goals for the common objects. | Draft prose does not prove implementation or adoption. |
| [`tests/schemas/test_common_contracts.py`](../../../../tests/schemas/test_common_contracts.py) | **CONFIRMED executable source** | Discovery, valid/invalid polarity, and expected-error matching. | Skips absent fixture directories and does not assert non-empty lanes. |
| [`schema-validation.yml`](../../../../.github/workflows/schema-validation.yml) | **CONFIRMED command-bearing workflow** | Runs schema inventory checks, aggregate non-vacuity checks, and repository schema/contract tests with read-only permissions. | Aggregate non-vacuity list does not include common schemas; current run outcome not established here. |
| [`contracts-validate.yml`](../../../../.github/workflows/contracts-validate.yml) | **CONFIRMED command-bearing workflow** | Runs `make test` on pull requests with read-only permissions. | A passing job is not complete fixture coverage or release authority. |
| [`docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | **CONFIRMED doctrine** | Responsibility-root separation and `tests/` + `fixtures/` validation posture. | Does not prove every specific fixture path is populated. |
| [`fixtures/README.md`](../../../README.md) | **CONFIRMED root README** | Fixture non-authority, public-safe, deterministic, synthetic posture. | Current test-only placement wording conflicts with this live contract-fixture lane. |

[Back to top](#top)

---

## Correction and rollback

Correct this README when:

- a common schema, contract, fixture family, or validator is added, removed, renamed, or migrated;
- the generic harness begins enforcing presence or non-vacuity;
- parent fixture/schema/contract indexes are reconciled;
- workflow coverage or required-check status changes;
- a factual inventory statement no longer matches the pinned repository state.

Rollback target for this documentation revision:

```text
prior blob: 15fa7d8282c72c6f54984ea853e1e06e6cd525c1
```

Before merge, close the draft pull request. After merge, revert the documentation commit and its generated-receipt commit. Rollback changes documentation and process memory only; it does not alter schema behavior, fixture payloads, tests, policy, lifecycle state, release state, deployment, or publication.

[Back to top](#top)
