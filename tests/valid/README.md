<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-valid-readme
title: tests/valid/ — Governed Cross-Cutting Positive-Path Compatibility Lane
type: readme; directory-readme; positive-test-compatibility-boundary; routing-index
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; compatibility-utility-lane; positive-tests-confirmed-elsewhere; dedicated-valid-suite-not-established; no-network-by-default; non-authoritative
owners: OWNER_TBD — QA steward · Test steward · Contract steward · Schema steward · Validator steward · Policy steward · Evidence steward · Runtime/API/UI stewards · Release steward · Domain stewards · Security reviewer · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; valid; positive-path; compatibility-lane; synthetic-only; no-network; paired-negative; no-parallel-authority; no-publication
current_path: tests/valid/README.md
truth_posture: CONFIRMED target README and prior blob, canonical tests root, current compatibility-lane classification, tests/invalid companion, fixture-home split, schemas/tests/valid compatibility index, executable schema fixture tests, Hydrology alias tests, control-plane metadata tests, governed-API boundary tests, Makefile commands, contracts-validate workflow, checked absence of tests/valid/conftest.py, tests/valid/test_valid.py, and tests/valid/pytest.ini, and bounded search that did not establish a direct executable suite or valid-specific workflow / PROPOSED lane-retention rule, routing matrix, minimum positive-case contract, required negative companion, anti-tautology controls, deterministic no-network harness, zero-collection failure, coverage artifact, sensitive-fixture review, CI graduation, correction and rollback cases, and deprecation path / CONFLICTED tests/valid and schemas/tests/valid compatibility labels versus owner-specific positive assertions already living in tests/schemas, tests/policy, app tests, domain tests, and other responsibility lanes / UNKNOWN exhaustive recursive inventory, dynamic collection, complete fixture inventory, current pass rates, coverage, flake rate, required-check status, promotion dependency, and production parity / NEEDS VERIFICATION accepted owners, CODEOWNERS, retain-route-retire decision, canonical fixture split, outcome normalization, network enforcement, artifact retention, CI ownership, and migration of future cases
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0d0f8109486763c7b4099a7a7b8b4c9fbed7219d
  target_prior_blob: fb405f82578d70538d3f54d05662b258b39f3303
  direct_lane_files_confirmed:
    - tests/valid/README.md
  checked_absent_paths:
    - tests/valid/conftest.py
    - tests/valid/test_valid.py
    - tests/valid/pytest.ini
  bounded_inventory_note: checked paths and bounded search did not establish a direct executable suite; ignored, generated, historical, branch-local, dynamically collected, package-local, domain-local, and external files remain UNKNOWN
related:
  - ../README.md
  - ../invalid/README.md
  - ../fixtures/README.md
  - ../schemas/README.md
  - ../contracts/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../runtime_proof/README.md
  - ../domains/
  - ../schemas/test_common_contracts.py
  - ../schemas/test_hydrology_alias_contracts.py
  - ../policy/test_control_plane_register_meta_contract.py
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../schemas/tests/valid/README.md
  - ../../fixtures/contracts/v1/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../Makefile
  - ../../.github/workflows/contracts-validate.yml
tags: [kfm, tests, valid, positive-path, compatibility, fixtures, pytest, no-network, evidence, policy, release, correction, rollback]
notes:
  - "v0.2 replaces a planning-oriented positive-path guide with a commit-pinned compatibility and routing boundary."
  - "The direct lane is README-only at the bounded snapshot."
  - "Executable positive assertions exist in specific owner lanes and must not be relabeled as tests/valid coverage."
  - "make test does not collect tests/valid, and no valid-specific workflow was established."
  - "This revision changes documentation only and creates no test, fixture, schema, contract, policy, workflow behavior, data, receipt, proof, release object, runtime behavior, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/valid/` — Governed Cross-Cutting Positive-Path Compatibility Lane

> Use this path only for genuinely cross-cutting positive tests that prove a supported path succeeds at its **named gate**. “Valid,” a passing fixture, schema conformance, a green workflow, or a returned `ANSWER` must never be upgraded into truth, authority, release approval, or publication.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Placement: compatibility utility" src="https://img.shields.io/badge/placement-compatibility__utility-orange">
  <img alt="Positive coverage: elsewhere" src="https://img.shields.io/badge/positive__coverage-owner__lanes-success">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Publication authority: none" src="https://img.shields.io/badge/publication-none-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Routing](#placement-and-routing-law) · [Case contract](#minimum-positive-case-contract) · [Controls](#paired-negative-and-anti-tautology-controls) · [Fixtures](#fixtures-security-and-sensitive-material) · [Outcomes](#outcome-vocabularies) · [Trust spine](#trust-spine-boundaries) · [CI](#runner-ci-and-promotion-boundary) · [Migration](#migration-deprecation-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Snapshot:** `main@0d0f8109486763c7b4099a7a7b8b4c9fbed7219d`  
> **Prior blob:** `fb405f82578d70538d3f54d05662b258b39f3303`  
> **Direct lane:** README only  
> **Checked absent:** `conftest.py`, `test_valid.py`, `pytest.ini`  
> **Current `make test`:** `python -m pytest tests/schemas tests/contracts -q`  
> **Valid-specific workflow:** not established

`tests/valid/` is a **compatibility and utility lane**, not an established executable suite.

The parent `tests/README.md` now explicitly lists it as a compatibility lane. That corrects the stale v0.1 statement that it was absent from the parent tree.

| Capability | Status | Safe conclusion |
|---|---:|---|
| README | `CONFIRMED` | This boundary exists. |
| Direct executable module | `NOT ESTABLISHED` | Checked paths and bounded search found none. |
| Lane-local runner/config | `NOT ESTABLISHED` | No collection contract was verified. |
| Positive assertions elsewhere | `CONFIRMED` | Specific owner lanes contain executable positive checks. |
| Fixture homes | `CONFIRMED` | Root reusable and test-local fixture homes are documented. |
| `schemas/tests/valid/` | `CONFIRMED compatibility index` | It routes executable schema proof to `tests/schemas/`. |
| Makefile collection | `NOT ESTABLISHED` | `tests/valid/` is omitted. |
| Valid-specific CI | `NOT ESTABLISHED` | No dedicated workflow surfaced. |
| Pass rate / coverage | `UNKNOWN` | No suite report was verified. |
| Promotion dependency | `UNKNOWN` | Workflow presence does not prove required-check status. |

Truth labels: `CONFIRMED`, `PROPOSED`, `CONFLICTED`, `UNKNOWN`, `NEEDS VERIFICATION`, and `DENY`.

[Back to top](#top)

---

## Purpose

A positive test proves only that explicit preconditions satisfied the gate actually exercised.

Use this lane only when:

1. the assertion spans multiple responsibility owners;
2. no specific owner lane fits without duplication;
3. the system under test and named gates are explicit;
4. a meaningful negative or boundary companion exists;
5. the case is deterministic and no-network by default;
6. success cannot be vacuous;
7. the result preserves evidence, policy, rights, sensitivity, lifecycle, review, release, correction, and rollback boundaries where material.

A passing case must not claim that:

- a source is authoritative because its descriptor validates;
- a claim is true because a fixture is accepted;
- a contract is complete because JSON shape passes;
- evidence is adequate because an `EvidenceRef` string exists;
- policy approved a use because required fields are populated;
- release exists because a manifest-shaped object validates;
- publication occurred because CI is green;
- rollback happened because a rollback target string exists;
- production matches local or CI behavior.

`valid` is a **test expectation**, not an authority class.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Test assertions | `tests/` | May own a truly cross-cutting assertion after routing review. |
| Machine shape | `schemas/` | Exercised, never defined here. |
| Semantic meaning | `contracts/` | Exercised, never rewritten here. |
| Policy and obligations | `policy/` | Evaluated, never invented here. |
| Reusable validators | `tools/validators/` or package owner | Called, never hidden here. |
| Shared fixtures | `fixtures/` | Referenced, never duplicated as authority. |
| Test-local fixtures | `tests/fixtures/` | Referenced under the documented split. |
| Source admission/registry | accepted source, policy, registry, connector roots | Tested through governed interfaces only. |
| Evidence/proof | governed evidence and proof roots | Synthetic refs only. |
| Lifecycle data | governed `data/` phases | Never stored or mutated here. |
| Release/correction/rollback | `release/` | Tested, never approved here. |
| API/UI/runtime | accepted implementation roots | Exercised through bounded interfaces. |
| Domain interpretation | `tests/domains/<domain>/` | Domain owner retains meaning. |

> [!WARNING]
> Do not turn this lane into a second schema, contract, policy, fixture, source, registry, evidence, receipt, proof, lifecycle, release, runtime, domain, or public-output home.

### Directory Rules basis

The existing file remains under the `tests/` enforceability root. No path is created, moved, renamed, or promoted. Specific positive assertions stay with the responsibility that owns the gate.

[Back to top](#top)

---

## Confirmed current state

### Direct lane

```text
tests/valid/
└── README.md
```

This bounded inventory does not prove permanent absence from history, ignored files, generated workspaces, dynamic collection, other branches, packages, domains, or external systems.

### Positive coverage confirmed elsewhere

| Evidence | Positive assertion | Limit |
|---|---|---|
| `tests/schemas/test_common_contracts.py` | Discovered `valid/valid_*.json` fixtures produce no JSON Schema errors. | Seven hard-coded top-level families; fixture-gated shape coverage only. |
| `tests/schemas/test_hydrology_alias_contracts.py` | One valid fixture for each Hydrology `decision_envelope`, `run_receipt`, and `evidence_bundle` alias validates. | Three aliases and one fixture each. |
| `tests/policy/test_control_plane_register_meta_contract.py` | Nine required registers have required metadata, valid dates, owners, doctrine refs, allowed status, and entries. | Static register structure, not policy-engine evaluation. |
| `apps/governed-api/tests/test_boundary_guards.py` | API route manifest is exactly `/bootstrap`, `/layers`, and `/evidence`. | Scaffolded route surface, not production parity. |
| `Makefile` `boundary-guards` | Runs selected policy and governed-API guard modules. | Mixed structural/static suite, not a universal success suite. |
| `Makefile` `test` | Runs schema and contract test paths. | Does not collect this lane. |
| `contracts-validate.yml` | Installs test dependencies and runs `make test` on push/PR. | No direct valid-lane coverage or required-check proof. |

Do not copy these tests here merely because their expected result is positive.

### Compatibility-name conflict

| Path | Current posture |
|---|---|
| `tests/valid/` | README-only cross-cutting compatibility lane. |
| `schemas/tests/valid/` | README-only valid-schema placement index; executable schema tests route to `tests/schemas/`. |

Resolve naming or migration through reviewed change, not silent consolidation.

[Back to top](#top)

---

## Placement and routing law

Prefer the most specific owner.

| Primary assertion | Preferred lane |
|---|---|
| JSON Schema acceptance | `tests/schemas/` |
| Contract semantic conformance | `tests/contracts/` |
| Policy allow/restrict behavior | `tests/policy/` |
| Validator acceptance | `tests/validators/` or validator package tests |
| Source admission success | `tests/source/` or owning connector/domain lane |
| Pipeline transition success | `tests/pipelines/` or owning pipeline tests |
| Governed API success | `tests/api/` or application tests |
| UI trust-state success | `tests/ui/` |
| Release/correction/rollback success | `tests/release/` |
| Runtime bounded `ANSWER` | `tests/runtime_proof/` |
| Domain-owned success | `tests/domains/<domain>/` |
| End-to-end composed success | `tests/e2e/<owner>/` |
| Truly cross-cutting success with no specific owner | `tests/valid/`, if retained |

Do not route a case here because its file begins with `valid_`, returns HTTP 200, expects `ALLOW` or `ANSWER`, is schema-valid, or is convenient for a workflow glob.

[Back to top](#top)

---

## Minimum positive-case contract

```yaml
case_id: valid.cross_cutting.example.v1
owner: OWNER_TBD
system_under_test:
  kind: validator|policy|resolver|pipeline|runtime|api|ui|release|rollback
  path: path/to/implementation
named_gates: [gate_id]
input:
  fixture_ref: fixtures/.../valid/valid_1.json
  synthetic: true
expected:
  test_result: PASS
  governed_outcome: ANSWER|ALLOW|RESTRICT|VALID|READY|OTHER
  forbidden_side_effects: []
negative_companion:
  case_ref: owner_specific.negative.case
network:
  allowed: false
determinism:
  clock: fixed
  ordering: stable
support:
  contract_refs: []
  schema_refs: []
  policy_refs: []
  evidence_refs: []
correction_case_ref: null
rollback_case_ref: null
```

Minimum requirements:

- stable case identity;
- named owner;
- exact system under test;
- named gates;
- resolvable deterministic fixture;
- separate test result and governed outcome;
- meaningful negative companion;
- explicit forbidden side effects;
- resolvable support refs appropriate to the gate;
- no-network default;
- fixed time/order/randomness where relevant;
- correction and rollback cases for consequential state.

[Back to top](#top)

---

## Paired-negative and anti-tautology controls

A material positive case should pair with at least one malformed, missing-support, stale, unresolved-rights, unresolved-sensitivity, denied-policy, missing-review, skipped-lifecycle, absent-release, superseded, withdrawn, correction-mismatch, rollback-failure, network, filesystem, or public-leakage case.

The companion stays with the owner of the failure, which may be `tests/invalid/`, an owner-specific test lane, or a fixture `invalid/` directory.

A positive test must not pass because:

- it repeats a fixture field;
- expected output is generated by the same unverified implementation;
- no fixture matched a glob;
- no schema or source file was discovered;
- the runner skipped the case;
- `all([])` or an empty scan succeeds;
- it checks only that a path or README exists;
- a TODO workflow exits zero;
- `|| true` or `continue-on-error` masks failure.

A mature harness must fail on zero collected tests and zero discovered cases.

Proposed future checks:

```bash
python -m pytest tests/valid --collect-only -q
python scripts/assert_nonzero_test_collection.py tests/valid
```

These commands are **PROPOSED**, not current repository proof.

[Back to top](#top)

---

## Fixtures, security, and sensitive material

### Fixture homes

| Home | Use |
|---|---|
| `fixtures/` | Reusable cross-cutting valid, invalid, golden, and synthetic examples. |
| `tests/fixtures/` | Small fixtures owned by a particular test area. |
| Tiny inline values | Only when clearer than a file and fully synthetic. |

A `valid/` directory stores expected-to-pass **inputs**. It does not store approved records, source truth, released objects, or publication state.

The confirmed generic schema convention is:

```text
fixtures/contracts/v1/<family>/<schema_name>/
├── valid/valid_*.json
└── invalid/
    ├── invalid_*.json
    └── invalid_*.expected_error.txt
```

### Default security posture

Positive tests must:

- make no live network, model, vendor, tile, database, or package-registry calls;
- use synthetic or pinned public-safe fixtures;
- freeze clocks and stabilize ordering;
- seed randomness if needed;
- use temporary directories;
- avoid credentials and secret discovery;
- avoid writes to canonical, lifecycle, registry, proof, receipt, and release roots;
- produce no public artifact.

### Sensitive domains

Living-person, DNA/genomic, private-land, archaeology, rare-species, infrastructure, health, security, and culturally restricted cases must be synthetic or irreversibly transformed. A “valid public” result may be generalized, delayed, redacted, restricted, or denied-precision—not detailed exposure.

Required controls:

- omit direct identifiers and protected exact coordinates;
- preserve consent, sovereignty, rights, and community authority;
- model redaction/generalization/withholding;
- pair public-safe success with a case that blocks more precise output;
- require specialist review.

### Live tier

Any future live-source tier requires explicit opt-in, approved test credentials, rights review, endpoint allowlist, cost/rate limits, timeouts, source-head recording, temporary outputs, sanitization, and a deterministic fixture equivalent. It has no publication authority.

[Back to top](#top)

---

## Outcome vocabularies

Keep vocabularies separate.

| Layer | Example values |
|---|---|
| Test framework | `PASS`, `FAIL`, `ERROR`, `SKIP`, `XFAIL`, `XPASS`, `NOT_COLLECTED` |
| Runtime envelope | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Policy engine | `ALLOW`, `RESTRICT`, `HOLD`, `DENY` or contract-specific vocabulary |
| Validator/gate | `VALID`, `INVALID`, `HELD`, `READY`, `NOT_READY`, `APPROVED`, `REJECTED` |
| Release lifecycle | contract-specific candidate, released, corrected, superseded, withdrawn states |

A test can pass while expecting `ABSTAIN`, `DENY`, `RESTRICT`, or `HOLD` when that is correct governed behavior.

```text
test PASS ≠ source truth
test PASS ≠ evidence closure
test PASS ≠ policy approval
test PASS ≠ release approval
test PASS ≠ publication
test PASS ≠ production parity
```

[Back to top](#top)

---

## Trust-spine boundaries

A cross-cutting case should name the stages it exercises:

```text
source admission
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> validation
  -> EvidenceRef -> EvidenceBundle
  -> policy and obligations
  -> CATALOG / TRIPLET
  -> review and promotion
  -> ReleaseManifest
  -> governed API/UI/runtime
  -> correction / withdrawal / supersession / rollback
```

Rules:

- evidence support must resolve for the tested claim, time, geometry, and source role;
- policy success includes obligation enforcement, not only an allow-like decision;
- lifecycle success cannot skip phases;
- promotion is a governed transition, not a file move;
- release success requires accepted support, review, correction, and rollback posture;
- public clients use governed interfaces, not canonical stores;
- citations, caveats, denials, abstentions, stale states, and corrections remain visible.

A passing test proves only the named gates and scoped assertions.

[Back to top](#top)

---

## Failure interpretation

| Failure | Required interpretation |
|---|---|
| Valid fixture rejected | Inspect schema, contract, fixture, and version drift; do not weaken the fixture blindly. |
| Negative companion accepted | Fail-closed regression; block promotion. |
| Zero cases collected | Vacuous success; fail the suite. |
| Fixture missing | Coverage gap, not implicit skip. |
| Support ref unresolved | Fail, hold, deny, or abstain according to contract. |
| Network used in default tier | Isolation violation. |
| Canonical store mutated | Authority and side-effect breach; restore and audit. |
| Nondeterministic time/order diff | Fix the harness, not the expectation. |
| Public precision denied | May be correct policy behavior; inspect decision and obligations. |
| TODO workflow green | No substantive proof. |
| Early gate passes, later gate fails | Earlier success remains bounded; do not label the object globally valid. |

[Back to top](#top)

---

## What passing does not prove

Passing does not by itself prove source authority, current source availability, current rights, resolved sensitivity for every use, claim truth, semantic completeness, full schema coverage, policy-engine correctness, obligation enforcement elsewhere, broader evidence adequacy, later lifecycle integrity, human review, release, publication, correction propagation, rollback execution, deployment, observability, required-check significance, production parity, or absence of untested leakage.

Positive evidence should narrow uncertainty, not erase it.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

### Confirmed commands

```bash
make test
# python -m pytest tests/schemas tests/contracts -q

make schemas
# python tools/validators/_common/run_all.py

make boundary-guards
# selected policy and governed-API boundary tests

make validate
# make schemas test
```

`python -m pytest tests/valid -q` is a future candidate only. Do not present it as current proof until cases, collection safeguards, dependencies, and CI wiring exist.

### Workflow posture

| Surface | Confirmed behavior | Limit |
|---|---|---|
| `contracts-validate.yml` | Runs on push/PR, installs `.[test]`, invokes `make test`. | No direct valid-lane collection. |
| Schema workflows | Invoke `make schemas`. | Validator aggregate is not a general positive suite. |
| Boundary workflow | Runs selected static/structural tests. | Not a universal allow/success suite. |
| Valid-specific workflow | Not established. | No owner, artifact, or pass history. |

### CI graduation criteria

Before this lane can be promotion-significant:

- direct cases and accepted lane ownership exist;
- zero collection fails;
- fixture manifests and negative companions are enforced;
- network and canonical-store mutation are denied;
- sensitive review is enforced;
- counts and coverage gaps are emitted;
- artifact retention is accepted;
- retries do not hide first-attempt failures;
- path filters include affected code, contracts, schemas, policies, fixtures, and tests;
- branch-protection or promotion dependency is intentionally approved;
- correction and rollback cases exist;
- workflow steps are substantive, not TODO-only.

A future QA report remains non-authoritative and must not become a release receipt or proof of truth.

[Back to top](#top)

---

## Migration, deprecation, and rollback

Maintainers should choose one explicit posture:

1. **Retain narrowly** — only truly cross-cutting positive assertions.
2. **Routing-only** — README points contributors to specific owners.
3. **Retire** — move cases, update backlinks/workflows, leave a temporary compatibility pointer, then remove through reviewed migration.

Migration must preserve case identity or aliases, fixture manifests, negative companions, history, owners, workflow filters, coverage reporting, deprecation window, and rollback target.

Do not merge `tests/valid/` with `schemas/tests/valid/` by convenience. Keep executable schema proof under `tests/schemas/`, schemas under versioned schema roots, and fixtures under accepted fixture homes.

Documentation rollback is ordinary Git rollback: before merge, close the draft PR or restore `fb405f82578d70538d3f54d05662b258b39f3303` in a transparent follow-up; after merge, revert the documentation commit. No runtime, data, policy, source, or release rollback is required.

[Back to top](#top)

---

## Definition of done

Documentation work completed here:

- [x] current path, base, and prior blob pinned;
- [x] stale parent-tree claim corrected;
- [x] direct README-only inventory bounded;
- [x] representative absent runner/config paths recorded;
- [x] owner-specific positive coverage distinguished;
- [x] compatibility-name conflict surfaced;
- [x] authority and routing rules defined;
- [x] minimum case contract defined;
- [x] paired-negative and anti-tautology controls defined;
- [x] fixture, sensitive-data, network, and side-effect rules defined;
- [x] outcome vocabularies separated;
- [x] current commands and CI limits grounded;
- [x] passing limits, migration, and rollback stated.

Still unresolved:

- [ ] lane retention decision;
- [ ] owners and CODEOWNERS;
- [ ] direct cases and runner;
- [ ] zero-collection enforcement;
- [ ] coverage/report contract;
- [ ] CI and promotion significance;
- [ ] current execution logs and pass rates.

Unchecked items are implementation or governance work, not repository facts.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| VALID-01 | Retain, route-only, or retire this lane? | `NEEDS VERIFICATION` |
| VALID-02 | Are there ignored, generated, historical, or branch-local direct cases? | `UNKNOWN` |
| VALID-03 | Who owns the lane and CODEOWNERS entry? | `NEEDS VERIFICATION` |
| VALID-04 | Is there an accepted case-manifest schema? | `UNKNOWN` |
| VALID-05 | Which positive cases are currently collected repository-wide? | `UNKNOWN` |
| VALID-06 | What are pass, skip, error, coverage, and flake rates? | `UNKNOWN` |
| VALID-07 | Does any required check depend on a positive suite? | `UNKNOWN` |
| VALID-08 | Is zero collection rejected? | `NEEDS VERIFICATION` |
| VALID-09 | How is no-network behavior enforced? | `NEEDS VERIFICATION` |
| VALID-10 | Are valid fixtures required to have invalid companions and nonempty polarity? | `NEEDS VERIFICATION` |
| VALID-11 | How are sensitive positive fixtures reviewed? | `NEEDS VERIFICATION` |
| VALID-12 | Which policy outcome vocabulary is accepted? | `CONFLICTED / NEEDS VERIFICATION` |
| VALID-13 | Are policy obligations tested at consumers? | `UNKNOWN` |
| VALID-14 | Is EvidenceRef adequacy tested beyond resolvability? | `UNKNOWN` |
| VALID-15 | Is release-gate success tested independently from schema validity? | `UNKNOWN` |
| VALID-16 | Are correction, withdrawal, supersession, and rollback cases complete? | `UNKNOWN` |
| VALID-17 | What is the retirement plan for `schemas/tests/valid/`? | `NEEDS VERIFICATION` |
| VALID-18 | Where are QA artifacts retained? | `NEEDS VERIFICATION` |
| VALID-19 | Which workflows are substantive versus TODO-only? | `NEEDS VERIFICATION` |
| VALID-20 | Does production enforcement match tested behavior? | `UNKNOWN` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---:|---|---|
| Prior target README | `CONFIRMED` | v0.1 rules and prior planning posture. | Did not establish executable maturity. |
| `tests/README.md` | `CONFIRMED` | Canonical root and compatibility classification. | Broad executable depth remains mixed. |
| `tests/invalid/README.md` | `CONFIRMED` | Companion routing and negative controls. | Does not create positive coverage. |
| `tests/fixtures/README.md` | `CONFIRMED` | Fixture split and synthetic/no-network posture. | Payload inventory is partial. |
| `schemas/tests/valid/README.md` | `CONFIRMED` | Separate schema-valid compatibility index. | README-only and migration-sensitive. |
| `tests/schemas/README.md` | `CONFIRMED` | Two executable modules, commands, and blind spots. | Full schema coverage/pass state unknown. |
| Common contract fixture test | `CONFIRMED executable` | Valid fixtures accept; invalid fixtures reject. | Hard-coded families and fixture-gated discovery. |
| Hydrology alias test | `CONFIRMED executable` | Three narrow positive alias cases. | Not broad semantic proof. |
| Control-plane metadata test | `CONFIRMED executable` | Positive structure for nine registers. | Static, not policy evaluation. |
| Governed-API boundary test | `CONFIRMED executable` | Route manifest and boundary behavior. | Scaffold, not deployment proof. |
| Makefile | `CONFIRMED` | Current commands. | This lane omitted. |
| Contracts workflow | `CONFIRMED` | Push/PR invokes `make test`. | No direct valid-lane collection. |
| Directory Rules | `CONFIRMED doctrine` | Responsibility-root separation. | Lane retention remains a governance choice. |
| Bounded search / checked paths | `CONFIRMED for snapshot` | No direct suite established. | Not exhaustive permanent absence. |

[Back to top](#top)

---

## No-loss assessment

Preserved and strengthened from v0.1:

- gate-limited positive claims;
- synthetic, public-safe, no-network inputs;
- fixture separation;
- meaningful negative companions;
- authority separation;
- no inference from test success to truth, policy, release, or publication;
- preference for specific owner lanes;
- honest maturity labels.

Corrected:

- the current parent README now lists `tests/valid/`;
- specific executable positive coverage exists elsewhere;
- the confirmed root command is documented rather than treating `pytest tests/valid` as current;
- direct-lane absence is bounded without denying repository-wide positive tests.

[Back to top](#top)

---

## Maintainer rule

> Put a positive test with the responsibility that owns the gate. Retain it here only when it is truly cross-cutting, independently testable, paired with a meaningful negative case, deterministic, no-network by default, and incapable of turning green into truth, policy, release, or publication authority.

Until maintainers accept direct cases and a substantive runner, keep this directory README-only.

[Back to top](#top)
