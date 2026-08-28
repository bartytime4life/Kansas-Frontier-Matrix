# `tests/contracts/` — Governed Semantic Contract Enforceability Lane

> Test boundary for proving that KFM semantic contracts remain explicit, non-duplicative, machine-linked where claimed, policy-aware, evidence-aware, and safe to consume. This lane proves contract behavior; it does not author contract meaning, schema shape, policy, fixtures, validators, release state, or public behavior.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-contracts-readme
title: tests/contracts/README.md — Governed Semantic Contract Enforceability Lane
type: readme; directory-readme; semantic-contract-test-boundary; enforceability-index
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; related-schema-contract-tests-confirmed; dedicated-semantic-suite-not-established
owners: OWNER_TBD — QA steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Runtime steward · Release steward · Security steward · Domain stewards · Docs steward
created: NEEDS VERIFICATION — README existed before v0.1 expansion
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; contracts; semantic-enforceability; fail-closed; no-contract-authority; no-schema-authority; no-policy-authority; no-release-authority
current_path: tests/contracts/README.md
truth_posture: CONFIRMED target README, canonical tests root, canonical contracts root, schema-contract fixture test under tests/schemas/test_common_contracts.py, contracts-validate workflow invoking make test, Directory Rules authority boundaries, and bounded repository search that did not establish a direct executable under tests/contracts / PROPOSED dedicated semantic metadata, boundary, crosswalk, maturity, drift, evidence, policy, release, correction, rollback, and compatibility tests / UNKNOWN exhaustive recursive inventory, dynamic pytest collection, make test expansion, workflow pass rates, semantic coverage breadth, contract-to-schema completeness, fixture coverage, validator coverage, and release-gate dependency / NEEDS VERIFICATION owners, accepted direct-lane test runner, canonical contract inventory, object-map coverage rule, contract metadata schema, cross-root linkage rules, negative fixtures, CI gate ownership, and promotion-blocking policy
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 15d88fceced7050abac4493b9cf66f5bc288c1e6
  target_prior_blob: 394366bd731c30223ec4519542cd3898f47dad2e
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    contracts_root_readme: 6e05ba40fcc255e392210e56ef9519203aec6006
    schema_contract_test: b04342cc034d7f1cc554e155fdd02d6e972976e6
    contracts_validate_workflow: fba63efbae13c665a04d699f0651937dfbf633b3
  direct_lane_files_confirmed:
    - tests/contracts/README.md
  bounded_inventory_note: repository code search did not establish a direct executable test under tests/contracts; related contract-shape tests exist under tests/schemas
related:
  - ../README.md
  - ../schemas/README.md
  - ../schemas/test_common_contracts.py
  - ../../contracts/README.md
  - ../../contracts/OBJECT_MAP.md
  - ../../schemas/contracts/v1/
  - ../../fixtures/contracts/
  - ../../policy/
  - ../../tools/validators/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
  - ../../runtime/
  - ../../apps/
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../.github/workflows/contracts-validate.yml
notes:
  - "v0.2 replaces a generic contract-test plan with a repository-grounded maturity boundary."
  - "The direct lane is README-only at the bounded snapshot."
  - "Executable schema/fixture validation for several contract families exists in tests/schemas/test_common_contracts.py; that is machine-shape coverage, not proof of complete semantic-contract enforcement."
  - "The contracts-validate workflow invokes make test and therefore does not by itself establish a dedicated tests/contracts command or semantic coverage."
  - "This revision changes documentation only and creates no tests, fixtures, schemas, contracts, validators, policies, receipts, proofs, workflow behavior, or release objects."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Related schema tests: confirmed" src="https://img.shields.io/badge/related__schema__tests-confirmed-success">
  <img alt="Semantic suite: not established" src="https://img.shields.io/badge/semantic__suite-not__established-orange">
  <img alt="Authority: enforceability only" src="https://img.shields.io/badge/authority-enforceability__only-blue">
  <img alt="Failure posture: fail closed" src="https://img.shields.io/badge/failure-fail__closed-critical">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Test model](#semantic-contract-test-model) · [Required families](#required-test-families) · [Cross-root links](#cross-root-linkage-contract) · [Fixtures](#fixture-and-data-boundary) · [Negative states](#negative-and-fail-closed-coverage) · [Maturity](#maturity-and-claim-discipline) · [Execution](#execution-and-runner-boundary) · [CI](#ci-and-promotion-boundary) · [Review](#review-burden) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Direct lane:** `tests/contracts/README.md` only at the bounded repository snapshot.
> **Related executable evidence:** `tests/schemas/test_common_contracts.py` validates schema fixtures for selected contract families.
> **Workflow evidence:** `.github/workflows/contracts-validate.yml` installs test dependencies and runs `make test`.
> **Not established:** a dedicated semantic-contract runner, direct `tests/contracts/test_*.py` modules, complete contract inventory coverage, or promotion-blocking semantic coverage.

### Safe conclusion

`tests/contracts/` is the intended semantic-contract enforceability lane, but direct executable coverage was not established in the inspected path. Existing related tests validate JSON Schema fixtures for the families `evidence`, `runtime`, `common`, `policy`, `source`, `governance`, and `release`. Those tests prove selected machine-shape and fixture behavior; they do not prove every contract Markdown document is semantically complete, correctly classified, cross-linked, policy-aware, or release-safe.

- **CONFIRMED:** `tests/contracts/README.md` exists.
- **CONFIRMED:** `tests/` is the canonical enforceability root.
- **CONFIRMED:** `contracts/` is the canonical semantic-meaning root.
- **CONFIRMED:** `tests/schemas/test_common_contracts.py` parametrically validates valid and invalid fixtures against selected schemas.
- **CONFIRMED:** `contracts-validate` runs `make test`.
- **PROPOSED:** direct semantic tests should live here when their primary assertion concerns contract meaning or boundary discipline.
- **UNKNOWN:** full contract inventory, full schema pairing, direct semantic coverage, runner selection, pass rates, and release-gate dependency.
- **NEEDS VERIFICATION:** accepted ownership and whether some tests should remain paired under `tests/schemas/`, `tests/policy/`, `tests/release/`, or domain lanes.

### Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository files or bounded search. |
| `PROPOSED` | Recommended test behavior not established as current implementation. |
| `UNKNOWN` | Not proven by inspected repository or workflow evidence. |
| `NEEDS VERIFICATION` | Checkable, but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed because it would collapse responsibility or overstate maturity. |

---

## Purpose

`tests/contracts/` proves that human-readable semantic contracts are enforceable as part of the KFM trust spine.

A semantic contract test should answer one or more of these questions:

1. Does the contract clearly define the object or message meaning?
2. Does it state what the object may and may not support?
3. Does it preserve the split between semantic meaning, machine shape, policy, evidence, lifecycle state, and release authority?
4. Does it point to companion schemas, fixtures, validators, policy, evidence, runtime, API/UI, and release surfaces only when those surfaces actually exist?
5. Does its maturity label match repository evidence?
6. Do invalid, unsupported, denied, stale, withdrawn, superseded, and correction states fail closed?
7. Does a compatibility path remain a guard rather than becoming parallel authority?

A passing semantic test does not make the contract true. It proves that the contract document and its declared relationships meet accepted enforceability rules.

---

## Authority boundary

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| Semantic meaning | `contracts/` | Test meaning and exclusions; never redefine them here. |
| Machine shape | `schemas/contracts/v1/` | Check declared alignment where applicable. |
| Policy and admissibility | `policy/` | Test required references and fail-closed states; never author policy. |
| Fixtures | `fixtures/` or accepted test-local fixture home | Consume deterministic examples; never create a second fixture authority. |
| Validator implementation | `tools/validators/` or accepted package | Exercise behavior; never hide validator logic inside tests. |
| Evidence and provenance | `data/proofs/`, `data/receipts/`, accepted evidence roots | Use synthetic references and verify required posture. |
| Lifecycle data | governed `data/` lifecycle roots | Test transition meaning; do not store real lifecycle records here. |
| Release, correction, rollback | `release/` | Test required contract posture; never decide release state. |
| Runtime/API/UI behavior | accepted runtime and app roots | Pair with consumer tests where behavior is implemented. |
| Contract enforceability | `tests/contracts/` | This lane. |

> [!CAUTION]
> Tests may contain assertions about contract text and declared links. They must not duplicate canonical contract prose, embed shadow schemas, implement policy, or become a registry of release decisions.

---

## Confirmed current state

### Direct lane inventory

| Path | Status | Evidence-bounded conclusion |
|---|---:|---|
| `tests/contracts/README.md` | `CONFIRMED` | This boundary document exists. |
| direct executable test module | `NOT ESTABLISHED` | Bounded search did not establish a direct test file in this lane. |
| direct fixtures | `NOT ESTABLISHED` | No direct fixture lane was verified here. |
| dedicated runner/config | `NOT ESTABLISHED` | No lane-specific runner was verified. |

### Related executable coverage

`tests/schemas/test_common_contracts.py`:

- discovers JSON Schemas in selected families;
- discovers matching fixture directories under `fixtures/contracts/v1/<family>/<name>/`;
- requires valid fixtures to produce no validation errors;
- requires invalid fixtures to produce errors;
- optionally checks expected error text or patterns.

This is valuable confirmed coverage, but its primary authority is schema/fixture conformance. It should not be described as complete semantic-contract validation.

### Current workflow posture

`.github/workflows/contracts-validate.yml`:

1. checks out the repository;
2. sets up Python 3.11;
3. installs `.[test]`;
4. runs `make test`.

This confirms a workflow named `contracts-validate`, but not:

- the expansion of `make test`;
- whether all contract documents are discovered;
- whether direct semantic tests run;
- whether failures block every promotion path;
- current pass rates;
- coverage thresholds;
- artifact retention.

---

## Semantic contract test model

A semantic test should evaluate a contract as a governed declaration with resolvable support.

```text
contract Markdown
  -> stable identity and metadata
  -> semantic definition and exclusions
  -> responsibility-root discipline
  -> companion schema posture
  -> policy / rights / sensitivity posture
  -> evidence and provenance posture
  -> lifecycle and source-role posture
  -> consumer / runtime posture
  -> release / correction / rollback posture
  -> positive and negative enforceability evidence
```

### Test unit

The smallest useful unit is one contract document plus its declared support set:

```text
ContractUnderTest {
  contract_path
  contract_id
  status
  semantic_family
  schema_posture
  schema_refs[]
  policy_refs[]
  fixture_refs[]
  validator_refs[]
  evidence_refs[]
  consumer_refs[]
  release_refs[]
  compatibility_class
}
```

This shape is **PROPOSED**. It is not a repository schema or contract.

### Required outcomes

A test should produce a finite result:

| Outcome | Meaning |
|---|---|
| `PASS` | The asserted semantic boundary is supported. |
| `FAIL` | A required invariant is violated. |
| `ABSTAIN` | Required repository evidence is unavailable or ambiguous. |
| `SKIP_EXPLICIT` | Test is intentionally inapplicable with a recorded reason. |
| `ERROR` | Test infrastructure failed; no semantic conclusion is valid. |

Silent omission is not a success state.

---

## Required test families

### 1. Identity and metadata tests

Verify, where required by accepted authoring rules:

- stable document identity;
- title and path consistency;
- status and maturity labels;
- owner posture;
- supersession and rollback references;
- related path syntax;
- truth labels;
- compatibility classification.

Do not enforce fields that lack an accepted contract or authoring rule. Mark them `PROPOSED` or `NEEDS VERIFICATION`.

### 2. Semantic definition tests

Verify that the contract:

- defines the object or message meaning;
- distinguishes canonical objects from views, projections, receipts, or generated summaries;
- names unsupported interpretations;
- does not treat generated language as evidence;
- preserves source-role and evidence boundaries where claims are involved.

### 3. Responsibility-boundary tests

Reject semantic documents that silently become:

- JSON Schema definitions;
- executable policy;
- source registry records;
- fixture stores;
- validator implementation;
- runtime code;
- API route definitions;
- UI implementation;
- lifecycle records;
- proof or receipt instances;
- release decisions.

### 4. Schema-posture tests

For each contract, require one explicit posture when schema linkage is material:

- `schema-confirmed`;
- `schema-stub-confirmed`;
- `schema-missing`;
- `schema-conflicted`;
- `schema-not-applicable`.

A schema reference must resolve to a repository-present path at the tested commit, or the contract must abstain from claiming alignment.

### 5. Crosswalk tests

Verify declared relationships among:

- contract ID and path;
- schema ID and path;
- fixture family;
- validator;
- policy bundle;
- evidence object;
- runtime/API/UI consumer;
- release object.

Crosswalk tests must not invent missing companions merely to make the matrix complete.

### 6. Maturity-claim tests

Labels such as `validated`, `active`, `released`, `production`, `public`, or `canonical` require support appropriate to their meaning.

Examples:

| Claim | Minimum evidence |
|---|---|
| `schema-aligned` | Contract/schema mapping plus passing shape tests. |
| `validated` | Positive and negative fixtures plus passing tests/validator evidence. |
| `active` | Verified consumer or registry binding. |
| `released` | Release state, review, correction, and rollback evidence. |
| `public` | Governed release and public-surface evidence. |

A README, path, schema, or passing local test alone does not establish release.

### 7. Compatibility and drift tests

Detect:

- compatibility guards containing canonical object definitions;
- duplicate object authority across paths;
- alias names minting new identities;
- mirrored schemas under `contracts/`;
- contract families split without ADR or migration note;
- stale references after moves or supersession;
- undocumented version forks.

### 8. Evidence and provenance tests

Where a contract represents a claim-bearing object, verify that it:

- requires resolvable evidence references;
- distinguishes EvidenceRef from EvidenceBundle;
- supports abstention when evidence is absent;
- carries provenance and source-role expectations;
- does not allow fluent text to substitute for evidence.

### 9. Policy, rights, and sensitivity tests

Where material, verify the contract:

- names the policy decision boundary;
- preserves `ALLOW`, `DENY`, `RESTRICT`, or `ABSTAIN` semantics;
- does not imply consent from mere data possession;
- does not weaken rights or sensitivity at rendering time;
- defaults sensitive and unresolved cases safely.

### 10. Release, correction, and rollback tests

Public-facing contract semantics should require:

- review state;
- release state;
- correction path;
- withdrawal or supersession behavior;
- rollback target;
- downstream invalidation where material.

A semantic contract may describe these requirements but cannot issue the decision.

---

## Cross-root linkage contract

### Link rules

A declared path should be:

1. repository-relative;
2. owned by the correct responsibility root;
3. resolvable at the tested commit, unless explicitly marked proposed;
4. semantically appropriate;
5. non-circular where authority matters.

### Missing companion behavior

| Missing item | Required result |
|---|---|
| Required schema missing | `FAIL` or explicit `schema-missing`; never claim alignment. |
| Required policy missing | `FAIL_CLOSED` / `ABSTAIN`; never assume allow. |
| Required evidence contract missing | `ABSTAIN`; never synthesize evidence sufficiency. |
| Required fixture missing | `NEEDS_FIXTURE`; never claim validation. |
| Required validator missing | `NEEDS_VALIDATOR`; never claim executable enforcement. |
| Required release support missing | not released/public. |
| Optional companion absent | explicit not-applicable or proposed posture. |

### Source of truth order

1. accepted doctrine and ADRs;
2. canonical contract document;
3. companion schema and policy;
4. fixtures, validators, and tests;
5. runtime and release evidence;
6. generated indexes and summaries.

Generated indexes may assist discovery but do not outrank canonical files.

---

## Fixture and data boundary

Contract tests should use deterministic, synthetic, redacted, generalized, or public-safe fixtures.

### Allowed

- minimal valid object examples;
- invalid missing-field examples;
- invalid enum, pattern, timestamp, or identifier examples;
- unsupported-state examples;
- denied and abstain examples;
- correction, withdrawal, and supersession examples;
- compatibility drift examples.

### Denied by default

- living-person private data;
- raw DNA/genomic data;
- exact protected archaeology or rare-species locations;
- credentials, tokens, keys, or private endpoints;
- production receipts or release records copied as fixtures;
- mutable live-network dependencies;
- undocumented snapshots of governed data.

### Fixture authority

Fixtures prove examples. They do not define contract meaning. When fixture and contract disagree, the discrepancy must fail review; maintainers must not silently treat fixture behavior as the new contract.

---

## Negative and fail-closed coverage

Every material contract family should include negative cases for applicable failures:

- missing identity;
- unknown version;
- unresolved reference;
- schema mismatch;
- missing evidence;
- invalid source role;
- missing or denied policy decision;
- unresolved rights;
- unresolved sensitivity;
- missing consent or revoked consent;
- stale or superseded object;
- unsupported public projection;
- absent release state;
- missing rollback target;
- duplicate authority;
- incompatible alias;
- unknown field that could affect trust;
- malformed correction or withdrawal state.

Positive-only coverage is insufficient for trust-bearing contract families.

### No-network rule

The default contract test suite should not require live network access. External systems should be represented by deterministic fixtures or explicitly governed integration tests outside the default semantic suite.

---

## Maturity and claim discipline

### Contract maturity state

A test should not infer maturity from path existence.

```text
SCAFFOLD
  -> DRAFT
  -> SCHEMA_LINKED
  -> FIXTURED
  -> VALIDATED
  -> CONSUMER_BOUND
  -> RELEASE_GOVERNED
```

This sequence is **PROPOSED** and may be refined by accepted contract governance.

Each transition requires evidence; later states do not erase earlier obligations.

### Forbidden shortcuts

Do not infer:

- schema alignment from similar field names;
- validation from a schema file alone;
- consumer use from imports mentioned in docs;
- release from a public-sounding contract;
- canonical status from age or path depth;
- authority from generated indexes;
- successful semantics from workflow naming.

---

## Execution and runner boundary

### Current confirmed command

The repository workflow runs:

```bash
make test
```

The exact command expansion and direct semantic coverage are **NEEDS VERIFICATION**.

### Proposed local discovery

Until an accepted direct suite exists, maintainers may inspect with:

```bash
find tests/contracts -maxdepth 5 -type f | sort
find contracts -type f -name '*.md' | sort
find schemas/contracts/v1 -type f -name '*.schema.json' | sort
find fixtures/contracts -type f | sort
pytest -q tests/schemas/test_common_contracts.py
```

Do not append `|| true` to a command used as enforceability evidence.

### Future dedicated command

A dedicated command should be added only when actual direct tests exist, for example:

```bash
pytest -q tests/contracts
```

That command is **PROPOSED**, not confirmed current behavior.

### Exit behavior

| Condition | Exit posture |
|---|---|
| semantic violation | non-zero |
| unresolved required companion | non-zero or explicit abstain gate |
| no tests collected unexpectedly | non-zero |
| test infrastructure error | non-zero |
| only explicitly optional checks skipped | zero with visible skip reasons |

---

## CI and promotion boundary

The workflow name `contracts-validate` does not itself prove contract semantics.

A CI gate is substantive only when:

- its command is known;
- its collected tests are visible;
- no-tests-collected behavior is fail-closed;
- failures are not masked;
- expected fixtures are present;
- results are retained or inspectable;
- promotion depends on the result where contract significance requires it.

### Required separation

| Check class | Suggested owner |
|---|---|
| Markdown metadata and links | contract test or docs validator |
| JSON Schema fixture conformance | `tests/schemas/` |
| executable policy behavior | `tests/policy/` |
| release/correction/rollback behavior | `tests/release/` |
| domain meaning | `tests/contracts/` plus domain companions |
| runtime/API/UI consumption | runtime/API/UI test lanes |
| end-to-end trust spine | e2e or runtime-proof lanes |

Tests may be cross-referenced, but one lane must not claim another lane's coverage.

---

## Security and sensitive-domain posture

Contract tests must be safe to run in forks and ordinary CI.

- no embedded secrets;
- no live production credentials;
- no write access to governed data roots;
- no mutation of registries, policy, or release state;
- no execution of untrusted fixture content;
- bounded file traversal;
- symlink-safe discovery;
- explicit encoding;
- deterministic ordering;
- size and recursion limits where generated or adversarial inputs are possible.

Security-significant contract families require negative tests for confusion, path traversal, identity collision, unsupported versions, and policy bypass where applicable.

---

## Review burden

### Maintainer review

Required for ordinary test additions and documentation changes.

### Steward review

Required when a test changes the accepted interpretation of:

- contract authority;
- schema linkage;
- evidence requirements;
- policy, rights, sensitivity, or consent;
- identity or versioning;
- lifecycle states;
- public API/UI semantics;
- release, correction, withdrawal, supersession, or rollback;
- compatibility-path behavior.

### Review questions

1. Is the test asserting accepted meaning or inventing new meaning?
2. Is the primary assertion in the correct test lane?
3. Are positive and negative fixtures deterministic?
4. Does the test fail closed?
5. Does it avoid real sensitive data?
6. Does it distinguish direct coverage from companion coverage?
7. Does it preserve correction and rollback?
8. Does its failure block the right gate?

---

## Definition of done

### This README revision

- [x] Records the direct lane as README-only at the bounded snapshot.
- [x] Records related executable schema/fixture coverage without calling it complete semantic coverage.
- [x] Records the current workflow command without inferring its full expansion.
- [x] Preserves contract/schema/policy/test responsibility boundaries.
- [x] Defines positive, negative, drift, maturity, evidence, policy, and release test families.
- [x] Requires synthetic or public-safe fixtures.
- [x] Adds no executable test, schema, contract, fixture, validator, workflow, policy, data, proof, receipt, or release object.

### Future active lane

The lane is operationally established only when:

- direct test modules exist;
- ownership is assigned;
- the contract inventory rule is accepted;
- collection behavior is deterministic;
- no-tests-collected fails;
- metadata and semantic rules are accepted;
- valid and invalid fixtures exist;
- companion schema/policy/release tests are linked without double-counting;
- CI command and promotion dependency are explicit;
- corrections and rollback are tested;
- current results are inspectable.

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `TCON-001` | What is the exhaustive direct inventory under `tests/contracts/`? | `NEEDS VERIFICATION` | Commit-pinned recursive listing. |
| `TCON-002` | What does `make test` execute today? | `NEEDS VERIFICATION` | Makefile and runner inspection. |
| `TCON-003` | Is a dedicated semantic-contract runner accepted? | `UNKNOWN` | Test configuration and steward decision. |
| `TCON-004` | What is the canonical generated or maintained contract inventory? | `NEEDS VERIFICATION` | Accepted inventory contract/tool. |
| `TCON-005` | Which contract metadata fields are mandatory? | `NEEDS VERIFICATION` | Contract authoring standard or schema. |
| `TCON-006` | Which contract documents have companion schemas? | `UNKNOWN` | Generated crosswalk plus review. |
| `TCON-007` | Which schema links are validated by `test_common_contracts.py`? | `NEEDS VERIFICATION` | Collected parametrization report. |
| `TCON-008` | Where should semantic fixtures live? | `NEEDS VERIFICATION` | Fixture ADR/root contract. |
| `TCON-009` | Which maturity labels are machine-enforced? | `UNKNOWN` | Validator and tests. |
| `TCON-010` | Which compatibility paths must be tested for drift? | `NEEDS VERIFICATION` | ADRs and inventory. |
| `TCON-011` | Which policy and sensitivity references are mandatory by family? | `NEEDS VERIFICATION` | Policy/contract crosswalk. |
| `TCON-012` | Which public-facing contracts require release companion tests? | `NEEDS VERIFICATION` | Release and consumer inventory. |
| `TCON-013` | Does CI fail when zero direct semantic tests are collected? | `UNKNOWN` | Runner configuration and CI log. |
| `TCON-014` | Does contract validation block promotion? | `UNKNOWN` | Branch protection and promotion workflow evidence. |
| `TCON-015` | What correction and rollback cases are required per family? | `NEEDS VERIFICATION` | Release/correction contract and fixtures. |
| `TCON-016` | Are real sensitive values excluded automatically? | `UNKNOWN` | Secret/sensitivity scanners and negative tests. |
| `TCON-017` | What are current pass rates and flaky tests? | `UNKNOWN` | Recent workflow logs and history. |

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `394366bd…` | `CONFIRMED` | Existing intended lane and prior planning posture. | Current executable depth. |
| Directory Rules blob `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility roots and anti-collapse rules. | Test implementation. |
| tests root README blob `5614de99…` | `CONFIRMED ROOT CONTRACT` | Tests as canonical enforceability root. | Pass rates or direct lane coverage. |
| contracts root README blob `6e05ba40…` | `CONFIRMED CONTRACT ROOT` | Contracts define semantic meaning; schemas define shape. | Complete contract inventory. |
| schema contract test blob `b04342cc…` | `CONFIRMED EXECUTABLE TEST` | Parametric schema/fixture validation for selected families. | Complete semantic-contract enforcement. |
| workflow blob `fba63ef…` | `CONFIRMED WORKFLOW` | Workflow installs tests and runs `make test`. | Exact collected tests or success. |
| bounded repository search | `CONFIRMED BOUNDED RESULT` | No direct executable was established in this lane. | Exhaustive absence across history, branches, ignored files, or generated files. |

### Evidence hierarchy

Current contract files, schemas, policy, fixtures, validators, test code, workflow logs, runtime evidence, and release records outrank planning prose. This README may define guardrails and proposed acceptance criteria, but it cannot upgrade missing implementation to `CONFIRMED`.

---

## Maintainer note

Keep the distinction visible:

- `contracts/` says what an object means;
- `schemas/` says what shape it has;
- `policy/` decides whether use is allowed;
- `tests/contracts/` proves semantic boundaries;
- companion test lanes prove schema, policy, release, runtime, API, and UI behavior;
- evidence and release state determine whether a claim may be trusted or published.

Do not call schema fixture coverage complete semantic validation. Do not create tests merely to fill a tree. Add the smallest test that proves a real contract invariant, fails closed, and has a clear owner.

<p align="right"><a href="#top">Back to top</a></p>
