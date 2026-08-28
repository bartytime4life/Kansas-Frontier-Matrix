<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-source-readme
title: tests/source/ — Source Admission, Authority, and Anti-Collapse Enforceability Boundary
type: readme; directory-readme; source-test-compatibility-lane; source-admission; source-role; rights-and-sensitivity
version: v0.2
status: draft; repository-grounded; compatibility-lane; direct-lane-readme-only; source-descriptor-schema-validator-executable; schema-fixture-coverage-confirmed; connector-non-publisher-static-guard-confirmed; dedicated-source-behavior-suite-not-established; source-policy-stub; source-workflow-todo-only; path-drift-visible; no-network-by-default; fail-closed; non-authoritative
owners: OWNER_TBD — QA steward · Source steward · Source-registry steward · Contract steward · Schema steward · Fixture steward · Validator steward · Rights steward · Sensitivity steward · Citation steward · Connector steward · Pipeline steward · Evidence steward · Policy steward · Release steward · CI steward · Security reviewer · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 planning-oriented source-test README
policy_label: public-doc; tests; source; source-admission; SourceDescriptor; source-role; authority-rank; rights; sensitivity; cadence; freshness; access; citation; source-head; registry; connectors; non-publisher; synthetic-only; no-network; fail-closed; evidence-aware; policy-aware; release-gated; correction-aware; no-source-authority
current_path: tests/source/README.md
truth_posture: CONFIRMED target README and prior blob, canonical tests root, tests/source compatibility-lane posture, source semantic contract family, detailed SourceDescriptor schema and naming/path drift, one valid and one invalid SourceDescriptor schema fixture, executable top-level SourceDescriptor validator, five-validator aggregate including SourceDescriptor, root pytest configuration, Makefile schema/test/boundary targets, common schema fixture harness, connector/pipeline non-publisher static test, source-descriptor workflow TODO scaffold, schema-validation and validator-suite execution through make schemas, source registry README and its stale proposed paths, proposed ADR-0017, source policy stub, and bounded search that did not establish a direct executable under tests/source / PROPOSED dedicated source-behavior tests, source case manifest, rights/sensitivity/role/cadence/citation/registry/activation matrices, live-source tier, coverage artifact, path-migration tests, policy integration, required promotion dependency, and maturity ladder / CONFLICTED singular source versus plural sources schema and validator paths, hyphen versus underscore names, tests/source versus proposed tests/sources path, schema-declared tests/fixtures root versus observed fixtures/contracts root, README-only compatibility validator lanes versus confirmed top-level executable, and proposed ADR vocabulary versus current implementation evidence / UNKNOWN exhaustive recursive direct-lane inventory, dynamic test generation, ignored files, additional source tests in other refs, complete registry instance inventory, active source policy evaluator, production connector behavior, current pass rates, branch-protection requirements, emitted admission receipts, and production source activation behavior / NEEDS VERIFICATION accepted owners, CODEOWNERS, lane retention or migration, canonical schema/fixture/validator paths, complete fixture polarity, source-role validator implementation, rights/sensitivity policy implementation, source authority register behavior, downstream consumer enforcement, CI path filters, required checks, correction consumers, and rollback drill execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ba141d8ee7092427936161ad7b954fc449036601
  target_prior_blob: e40cdff2c1dbcb042c5c7e26d9c54c5cd8ff46a2
  direct_lane_files_confirmed:
    - tests/source/README.md
  adjacent_executable_surfaces:
    - tools/validators/validate_source_descriptor.py
    - tools/validators/_common/run_all.py
    - tests/schemas/test_common_contracts.py
    - tests/policy/test_pipeline_connector_non_publisher.py
  bounded_inventory_note: connector code search established the README as the only direct tests/source result for the searched source-test names; this does not prove permanent absence from history, other refs, ignored files, generated workspaces, dynamic test generation, package-local tests, domain-local tests, or uninspected paths
related:
  - ../README.md
  - ../schemas/README.md
  - ../contracts/README.md
  - ../policy/README.md
  - ../pipelines/README.md
  - ../release/README.md
  - ../fixtures/README.md
  - ../schemas/test_common_contracts.py
  - ../policy/test_pipeline_connector_non_publisher.py
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../contracts/source/README.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/README.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../tools/validators/validate_source_descriptor.py
  - ../../tools/validators/_common/run_all.py
  - ../../tools/validators/sources/README.md
  - ../../tools/validators/source_role/README.md
  - ../../data/registry/sources/README.md
  - ../../policy/source/README.md
  - ../../Makefile
  - ../../pyproject.toml
  - ../../.github/workflows/source-descriptor-validate.yml
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../.github/workflows/contracts-validate.yml
  - ../../.github/workflows/policy-boundary-guards.yml
tags: [kfm, tests, source, SourceDescriptor, admission, source-role, rights, sensitivity, cadence, freshness, citation, registry, connector, watcher, non-publisher, pytest, json-schema, fixtures, no-network, fail-closed, drift, correction, rollback]
notes:
  - "v0.2 replaces a planning-oriented README with a repository-grounded source-test compatibility boundary and current maturity assessment."
  - "The direct tests/source lane is README-only in the bounded snapshot; no dedicated executable source-behavior test module was established."
  - "SourceDescriptor machine-shape validation is executable through tools/validators/validate_source_descriptor.py and make schemas."
  - "The common schema harness also covers the source family when matching fixture roots exist; the observed SourceDescriptor family has one valid and one invalid fixture."
  - "The connector/pipeline non-publisher test is executable but static and lexical; it does not prove complete source admission, rights, sensitivity, role, cadence, citation, or registry behavior."
  - "Source path metadata is conflicted across singular/plural, hyphen/underscore, tests/source versus proposed tests/sources, and observed versus schema-declared fixture/validator homes."
  - "policy/source is a greenfield stub, source-descriptor-validate is TODO-only, and no active source-role or source-activation policy engine was established."
  - "This revision changes documentation only and creates no test, fixture, schema, contract, validator, policy, workflow behavior, source record, registry entry, lifecycle artifact, receipt, proof, release record, connector behavior, or public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/source/` — Source Admission, Authority, and Anti-Collapse Enforceability Boundary

> **Purpose.** Define the cross-cutting proof boundary for source admission and source-authority discipline. KFM must not treat a discovered URL, successful fetch, valid schema, registry entry, connector output, map layer, catalog record, model summary, or AI statement as source authority. A mature suite must prove that identity, role, authority, rights, sensitivity, cadence, access, citation, source-head, activation, record-level admission, correction, and downstream restrictions remain explicit and fail closed.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Compatibility lane: confirmed" src="https://img.shields.io/badge/lane-compatibility-informational">
  <img alt="SourceDescriptor validator: executable" src="https://img.shields.io/badge/descriptor__validator-executable-success">
  <img alt="Behavior suite: not established" src="https://img.shields.io/badge/behavior__suite-not__established-orange">
  <img alt="Path drift: unresolved" src="https://img.shields.io/badge/path__drift-UNRESOLVED-red">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: tests only" src="https://img.shields.io/badge/authority-tests__only-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-audience) · [Authority](#authority-and-repository-fit) · [Current state](#confirmed-current-state) · [Scope](#test-scope-and-non-scope) · [Admission](#source-admission-model) · [Roles](#source-role-and-authority-anti-collapse) · [Case contract](#minimum-source-test-case-contract) · [Outcomes](#finite-outcomes-and-state-vocabularies) · [Fixtures](#fixture-and-test-data-contract) · [Layers](#required-validation-layers) · [Coverage](#current-coverage-and-material-gaps) · [Execution](#deterministic-execution-and-no-network-posture) · [CI](#ci-workflow-and-promotion-boundary) · [Failures](#failure-interpretation) · [Passing](#what-a-passing-check-does-not-prove) · [Review](#review-burden-and-change-control) · [Done](#definition-of-done) · [Plan](#incremental-implementation-sequence) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **CONFIRMED direct lane:** the bounded repository snapshot establishes `tests/source/README.md` but did not establish a direct `test_*.py` or equivalent executable under `tests/source/`.
>
> **CONFIRMED adjacent execution:** SourceDescriptor shape validation is executable through a top-level validator, the shared validator aggregate, and the common schema-fixture harness. A static policy test also checks that connector and pipeline write contexts do not target catalog, published, or release paths.
>
> **NOT established:** a dedicated source-behavior suite; a complete source-role, rights, sensitivity, cadence, citation, registry, activation, or record-admission evaluator; a substantive source-policy bundle; or a source-specific CI job that executes those behaviors.

### Safe conclusion

`tests/source/` is a repo-confirmed compatibility lane for cross-cutting source-admission and source-role tests. It is not yet a direct executable suite. The repository has a meaningful but partial foundation:

- `tools/validators/validate_source_descriptor.py` invokes the shared Draft 2020-12 JSON Schema runner against the singular source schema and observed contract-fixture root.
- `tools/validators/_common/run_all.py` runs the SourceDescriptor validator first, followed by four other trust-object validators, and fails fast.
- `make schemas` runs that aggregate.
- `schema-validation.yml` and `validator-suite.yml` run `make schemas`.
- `tests/schemas/test_common_contracts.py` includes the `source` family and discovers a schema only when a matching fixture directory exists.
- `fixtures/contracts/v1/source/source_descriptor/` documents one valid fixture and one invalid fixture missing `source_id`.
- `tests/policy/test_pipeline_connector_non_publisher.py` statically scans selected connector and pipeline files for likely write operations near `data/catalog`, `data/published`, and `release/`.
- `make boundary-guards` and `policy-boundary-guards.yml` execute that static non-publisher check with other boundary tests.
- `source-descriptor-validate.yml` is a TODO-only scaffold, not a substantive source-admission workflow.
- `policy/source/README.md` is a greenfield stub.
- ADR-0017 remains `proposed`, so its activation-state and gate vocabulary is design guidance, not accepted implementation evidence.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from repository files or bounded connector search at the pinned snapshot. |
| `PROPOSED` | Recommended test behavior, fixture family, command, artifact, or integration not established as current implementation. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Repository evidence disagrees or points to competing paths, names, or vocabularies; no silent winner is selected. |
| `DENY` | A prohibited authority, admission, release, or public-surface interpretation. |

[Back to top](#top)

---

## Purpose and audience

`tests/source/` should prove that source material is governed before and after intake.

This README is for:

- QA and test stewards;
- source and registry stewards;
- contract, schema, fixture, and validator maintainers;
- rights, sensitivity, sovereignty, citation, and policy reviewers;
- connector, watcher, loader, pipeline, catalog, API, UI, map, and AI maintainers;
- domain stewards who need shared source-admission behavior;
- CI and release stewards deciding which source checks may support promotion.

The durable test question is:

> Can the repository demonstrate, with deterministic public-safe evidence, that a source has a stable admitted identity and bounded role, that unresolved rights or sensitivity fail closed, that freshness and citation obligations propagate, and that no connector, pipeline, registry, map, API, or AI surface silently upgrades the source's authority?

This lane must cover more than schema shape. A source can be schema-valid and still be inadmissible, stale, rights-unknown, sensitivity-unresolved, context-only, candidate-only, restricted, superseded, retired, or unsuitable for a requested claim.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place enforceability proof under `tests/`. Source registry records remain under `data/registry/sources/`; source meaning remains under `contracts/source/`; source shape remains under `schemas/`; admissibility remains under `policy/`; implementations remain under connectors, pipelines, packages, apps, and tools.

The parent `tests/README.md` now lists `tests/source/` as a compatibility lane for source-admission and source-role checks. That is stronger evidence than the v0.1 statement that the path was absent from the parent tree. Retention as a permanent lane still needs an accepted migration or maintainer decision.

| Responsibility | Authority home | Role of `tests/source/` |
|---|---|---|
| Cross-cutting source behavior tests | `tests/source/` if retained | Compatibility lane; direct suite not established. |
| Source schema tests | `tests/schemas/` | Confirmed adjacent machine-shape coverage. |
| Source policy and boundary tests | `tests/policy/` | Confirmed static connector/pipeline non-publisher coverage; broader source policy unestablished. |
| Source semantic-contract tests | `tests/contracts/` or accepted source sublane | Contract enforceability; direct source-specific suite not established. |
| Domain-owned source tests | `tests/domains/<domain>/...` | Preferred when semantics or policy are domain-specific. |
| Source object meaning | `contracts/source/` | Canonical semantic responsibility. |
| Source machine shape | `schemas/contracts/v1/source/` or accepted successor | Current detailed schema exists; path/name drift remains. |
| Source fixtures | `fixtures/contracts/v1/source/` and accepted behavior-fixture homes | Synthetic test inputs only. |
| Source registry records | `data/registry/sources/` | Source identity and admission-control records; never stored here. |
| Source authority register | `control_plane/` accepted register | Governance record; tests may resolve synthetic examples. |
| Source policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | Allow, deny, restrict, hold, abstain, and obligations. |
| Source validators | `tools/validators/` | Confirmed top-level SourceDescriptor validator; other paths are compatibility or proposed. |
| Connector and pipeline behavior | `connectors/`, `pipelines/`, shared packages | Implementation under test; not owned here. |
| Evidence, receipts, proofs | accepted evidence, receipt, and proof roots | Tests verify refs and outcomes; never store trust records here. |
| Release, correction, rollback | `release/` and governed release roots | Tests may block transitions; they do not approve them. |

> [!CAUTION]
> `tests/source/` must not become a source registry, descriptor-instance store, source-authority register, policy bundle, schema home, contract home, fixture archive, connector implementation, lifecycle data path, evidence store, receipt/proof store, release record, or public source endpoint.

### Compatibility and path-drift boundary

Current repository documents and files expose several competing path shapes:

```text
tests/source/                                  # confirmed README compatibility lane
tests/sources/                                 # proposed in older registry docs; README not found at snapshot

schemas/contracts/v1/source/                   # confirmed detailed schema family
schemas/contracts/v1/sources/                  # declared canonical by metadata/older docs; needs migration decision

source_descriptor.schema.json                  # detailed underscore schema
source-descriptor.schema.json                  # separate permissive scaffold

fixtures/contracts/v1/source/source_descriptor/ # confirmed schema-fixture family
tests/fixtures/sources/source_descriptor/       # declared by schema metadata; not the validator's current fixture root

tools/validators/validate_source_descriptor.py # confirmed executable
tools/validators/source_descriptor/            # README route
tools/validators/source-descriptor/            # README route
tools/validators/sources/                      # plural compatibility/index route
tools/validators/source_role/                  # role-validator README route
```

Until an accepted migration settles these paths:

1. Do not create parallel executable implementations.
2. Treat the confirmed top-level validator as the executable fact for current behavior.
3. Treat singular/plural and hyphen/underscore alternatives as compatibility or migration surfaces.
4. Make tests assert alias consistency before any compatibility path is promoted.
5. Update schemas, metadata, fixtures, validator registry, docs, workflows, and tests together when paths change.
6. Preserve rollback links and old-path diagnostics during migration.

[Back to top](#top)

---

## Confirmed current state

### Direct lane inventory

| Path or surface | Status | Evidence-bounded conclusion |
|---|---:|---|
| `tests/source/README.md` | `CONFIRMED` | This compatibility boundary exists. |
| Direct `tests/source/test_*.py` module | `NOT ESTABLISHED` | Bounded search for the v0.1 proposed test names returned only this README. |
| Direct lane fixtures | `NOT ESTABLISHED` | No test-local payload family was verified under this lane. |
| Lane-specific runner/config | `NOT ESTABLISHED` | No direct command or marker was verified beyond the repository-wide pytest configuration. |
| `tests/sources/README.md` | `NOT FOUND` | Older source-registry docs propose the plural test path, but the exact README was not present at the pinned snapshot. |

### Adjacent executable inventory

| Surface | Status | What it currently proves |
|---|---:|---|
| `tools/validators/validate_source_descriptor.py` | `CONFIRMED EXECUTABLE` | Runs the detailed SourceDescriptor schema against the observed contract-fixture family. |
| `tools/validators/_common/run_all.py` | `CONFIRMED EXECUTABLE` | Includes SourceDescriptor in the five-validator aggregate and fails fast. |
| `tests/schemas/test_common_contracts.py` | `CONFIRMED EXECUTABLE` | Valid/invalid schema fixture behavior for source schemas with matching fixture directories. |
| `fixtures/contracts/v1/source/source_descriptor/valid/valid_1.json` | `CONFIRMED BY FIXTURE README` | One complete positive descriptor example. |
| `fixtures/contracts/v1/source/source_descriptor/invalid/invalid_1.json` | `CONFIRMED BY FIXTURE README` | One negative example missing required `source_id`. |
| `tests/policy/test_pipeline_connector_non_publisher.py` | `CONFIRMED EXECUTABLE` | Static lexical guard against likely connector/pipeline writes to catalog, published, or release paths. |
| `make schemas` | `CONFIRMED COMMAND` | Runs the five-validator aggregate including SourceDescriptor. |
| `make boundary-guards` | `CONFIRMED COMMAND` | Runs connector/pipeline non-publisher guard with other boundary tests. |

### Current documentation and governance posture

| Surface | Status | Material limit |
|---|---:|---|
| ADR-0017 | `PROPOSED` | Admission and activation flow is not yet an accepted repository decision. |
| `contracts/source/README.md` | `DRAFT / PROPOSED` | Semantic boundary exists; implementation references are partly stale. |
| `schemas/contracts/v1/source/README.md` | `MIXED MATURITY` | Detailed descriptor schema coexists with empty scaffolds and path/name drift. |
| `data/registry/sources/README.md` | `PROPOSED BUNDLE` | Contains older proposed test, fixture, schema, and validator paths that differ from current executable evidence. |
| `tools/validators/sources/README.md` | `COMPATIBILITY INDEX` | Does not reflect the confirmed top-level executable as its primary current implementation. |
| `policy/source/README.md` | `GREENFIELD STUB` | No substantive source policy bundle established. |
| `source-descriptor-validate.yml` | `TODO-ONLY` | Checks out code and echoes TODO messages. |

### Maturity statement

Current SourceDescriptor shape validation is real. Current cross-cutting source-admission behavior enforcement is not complete.

The repository can currently demonstrate:

- rich SourceDescriptor shape and required-field enforcement;
- one positive and one negative descriptor fixture path;
- aggregate local/CI execution through `make schemas`;
- a bounded static check that connectors and pipelines do not visibly write to publication targets.

It cannot yet demonstrate, from the inspected evidence alone:

- complete source-role anti-collapse;
- rights and license expiry evaluation;
- sensitivity and sovereignty obligations;
- cadence and stale-state enforcement;
- citation propagation;
- source-authority-register resolution;
- descriptor-level activation state transitions;
- record-level admission and quarantine reason codes;
- source-head drift, retirement, supersession, and correction behavior;
- downstream API/UI/map/AI preservation of admitted source posture;
- source-policy bundle selection and execution;
- production source activation or release blocking.

[Back to top](#top)

---

## Test scope and non-scope

### In scope

A mature `tests/source/` suite may own cross-cutting tests for:

1. SourceDescriptor identity and required governance fields.
2. Descriptor-level source admission and activation state.
3. Record-level minimum admission bars and quarantine routing.
4. Source role and authority-rank anti-collapse.
5. Rights, terms, attribution, redistribution, commercial-use, AI-use, and expiry posture.
6. Sensitivity, geoprivacy, sovereignty, cultural/community authority, and review obligations.
7. Update cadence, freshness expectation, stale-state, retirement, and supersession.
8. Access posture, authentication metadata, endpoint classes, and secret non-disclosure.
9. Citation template, attribution, disclaimer, role qualifier, and link-back obligations.
10. Source-head identity, change detection, drift classification, and re-review.
11. Registry identity, version, correction, supersession, and resolver behavior.
12. Connector/watcher/loader non-publisher guarantees.
13. Pipeline preservation of source role and admissibility limits.
14. Evidence and citation payloads preserving source identity without treating metadata as truth.
15. API/UI/map/export/graph/embedding/Focus Mode/AI surfaces preserving restrictions.
16. Correction, withdrawal, retirement, and rollback propagation.
17. Compatibility-path consistency and migration behavior.
18. No-network defaults and separately governed live probes.

### Route elsewhere when primary responsibility differs

| Primary assertion | Preferred lane |
|---|---|
| JSON Schema acceptance/rejection | `tests/schemas/` |
| Semantic contract completeness | `tests/contracts/` |
| Policy evaluator outcome or obligation | `tests/policy/` |
| Connector parser/fetch behavior | connector-local tests or accepted connector test lane |
| Pipeline transform behavior | `tests/pipelines/` or pipeline-local tests |
| Domain source semantics | `tests/domains/<domain>/...` |
| Runtime response envelope | runtime/API test lane |
| Release readiness | `tests/release/` |
| UI source badges and caveats | `tests/ui/` or e2e lane |
| Source registry package implementation | package-local tests or accepted package test lane |

### Out of scope

Do not place these materials in `tests/source/`:

- real SourceDescriptor registry instances;
- real source payloads, downloads, snapshots, or credentials;
- semantic contract prose;
- JSON Schema definitions;
- policy rules or policy bundles;
- connector, watcher, loader, package, pipeline, API, UI, map, graph, or AI implementation;
- actual source activation decisions;
- actual rights or sensitivity decisions;
- production EvidenceBundles, receipts, proofs, catalog records, release records, corrections, or rollback cards;
- generated CI reports of record;
- private keys, tokens, passwords, account identifiers, or live protected endpoints;
- exact protected locations, living-person identifiers, DNA/genomic data, culturally sensitive material, or infrastructure-sensitive detail;
- generated language treated as source truth.

[Back to top](#top)

---

## Source admission model

Source admission has two distinct test subjects. Tests must not collapse them.

| Admission sense | Subject | Question | Typical test evidence |
|---|---|---|---|
| Descriptor-level admission | Source family or source service | Is this source allowed in KFM, under which role, rights, sensitivity, access, and activation state? | SourceDescriptor, authority-register entry, activation decision, rights/sensitivity review, fixture, dry-run receipt. |
| Record-level admission | Individual source record | Does this record meet the source's minimum bar, and is a fail-closed trigger active? | Source-specific admission rules, normalized candidate, quarantine reason, validation report, record receipt. |

### Governed flow

```text
source discovered
  -> draft SourceDescriptor
  -> rights review
  -> sensitivity / sovereignty review
  -> source authority registration
  -> activation decision
  -> synthetic no-network fixture
  -> connector dry-run to RAW or QUARANTINE
  -> validation and policy
  -> steward review
  -> active internal / public candidate / denied / retired
  -> downstream evidence, catalog, release, and public surfaces remain separately gated
```

ADR-0017 proposes the detailed activation flow and state vocabulary. Because the ADR is still `proposed`, tests should encode its current rules only as proposed or ADR-pinned cases. They must fail visibly if implementation and ADR vocabulary diverge.

### Minimum descriptor-level assertions

A descriptor-level test should check, where required:

- stable `source_id` and descriptor version;
- source type and source role;
- secondary roles and authority rank;
- publisher and owner/steward;
- rights status, terms/license, attribution, redistribution, commercial/AI use, verification date, verifier, and obligations;
- sensitivity default, notes, review requirements, and transform posture;
- cadence, freshness expectation, staleness policy, and known update window;
- access method, access posture, endpoints, authentication metadata, and rate-limit notes;
- citation requirement, template, guidance, link, and disclaimer;
- source-head observation method and at least one content identity signal;
- allowed and prohibited claim roles;
- public-release posture;
- review state, release state, lifecycle state, correction, supersession, and retirement.

### Minimum record-level assertions

A record-level test should check, where source rules require:

- source descriptor resolves and is current;
- record identity is deterministic or explicitly provisional;
- source role and authority are inherited without upgrade;
- temporal fields are present and coherent;
- geometry or spatial support matches the source's stated precision;
- rights and sensitivity obligations are applied;
- required fields and quality qualifiers are present;
- invalid, ambiguous, duplicate, unsupported, stale, restricted, or sensitive records route to `QUARANTINE`, `HOLD`, `DENY`, or `ABSTAIN` with reason codes;
- connector and pipeline receipts point to source identity and version;
- no record crosses directly from fetch to public release.

[Back to top](#top)

---

## Source role and authority anti-collapse

A source role is an admission-time constraint, not a display label.

### Core anti-collapse rules

- `candidate` must not become verified merely because a pipeline succeeds.
- `modeled` must not become `observed`.
- `aggregate` must not become per-place or per-person truth.
- `regulatory` context must not become observed physical condition.
- `administrative` records must not become physical, biological, historical, or legal truth outside their scope.
- `context` or corroborative material must not become primary authority.
- `synthetic` or reconstructed material must not become observation.
- `restricted` source posture must not become public through derivation or summarization.
- an AI model must not infer, mint, upgrade, or erase source authority.
- promotion, publication, mapping, graph projection, export, or citation formatting must not alter source role.

### Required role test matrix

| Scenario | Expected behavior |
|---|---|
| Supported source role and claim role | `PASS` for the tested relation only. |
| Unsupported claim role | `FAIL` or policy `DENY`. |
| Ambiguous role | `ABSTAIN` or `HOLD_FOR_REVIEW`. |
| Downstream upgrade attempt | `FAIL` with anti-collapse reason code. |
| Multiple source roles | Preserve primary and secondary roles explicitly; no implicit precedence. |
| Role correction | New descriptor/version or correction record; no silent in-place upgrade. |
| Source supersession | New descriptor points backward; old descriptor remains auditable. |
| AI-proposed role | Candidate suggestion only; steward review required. |

### Authority rank is not truth

Authority rank helps resolve source posture and conflicts. It does not:

- prove a record is accurate;
- remove uncertainty;
- satisfy EvidenceBundle closure;
- authorize publication;
- waive rights or sensitivity obligations;
- replace review;
- permit exact-location disclosure;
- justify AI certainty.

[Back to top](#top)

---

## Minimum source-test case contract

Every future direct source test should declare enough metadata to make its scope inspectable.

```yaml
case_id: source-test-<stable-id>
title: <human-readable purpose>
status: proposed | active | deprecated | superseded
test_owner: <role or code owner>
subject:
  source_id: <toy or fixture id>
  descriptor_ref: <fixture path>
  descriptor_version: <version>
  admission_level: descriptor | record | downstream
source_posture:
  source_type: <value>
  source_role: <value>
  authority_rank: <value>
  rights_status: <value>
  sensitivity: <value>
  cadence_state: current | stale | expired | unknown
  access_posture: <value>
  citation_required: true
inputs:
  fixture_refs: []
  schema_refs: []
  contract_refs: []
  policy_refs: []
  registry_refs: []
  validator_refs: []
assertions:
  - <one bounded assertion>
expected:
  test_outcome: PASS | FAIL | ABSTAIN | SKIP_EXPLICIT | ERROR
  governance_outcome: ALLOW | DENY | RESTRICT | HOLD | ABSTAIN | NOT_APPLICABLE
  reason_codes: []
network: denied
sensitive_data: synthetic_public_safe
cleanup: <temporary-output rule>
```

This case shape is `PROPOSED`. It is not a new schema, contract, registry record, policy object, or runtime envelope.

### Case design rules

1. One case should prove one primary invariant.
2. Expected negative outcomes are successful tests when the system rejects correctly.
3. Fixture path, schema version, descriptor version, policy version, and validator version should be explicit.
4. Network behavior must be explicit.
5. Sensitive-data posture must be explicit.
6. Assertions must distinguish schema validity, semantic validity, policy admissibility, evidence support, activation state, and release state.
7. A test that scans files must assert that its scan set is nonempty.
8. A parametrized test must fail or report explicitly when it collects zero cases.
9. A skipped test must record why it is inapplicable.
10. A changed source descriptor, enum, fixture, validator, policy, registry, or consumer must update affected cases.

[Back to top](#top)

---

## Finite outcomes and state vocabularies

Do not collapse test outcomes, policy outcomes, activation states, lifecycle states, and runtime outcomes.

### Test-run outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The bounded assertion was supported. |
| `FAIL` | The tested invariant was violated. |
| `ABSTAIN` | Required repository or fixture evidence was unavailable or ambiguous. |
| `SKIP_EXPLICIT` | Intentionally inapplicable with a recorded reason. |
| `ERROR` | Test infrastructure failed; no governance conclusion is valid. |

### Source-governance outcomes

A policy or admission layer may use an accepted vocabulary such as:

| Outcome | Meaning |
|---|---|
| `ALLOW` | Tested use is allowed under stated scope and obligations. |
| `RESTRICT` | Use is allowed only under explicit restrictions or transforms. |
| `HOLD` | Human review or missing support blocks progress. |
| `DENY` | Tested use is prohibited. |
| `ABSTAIN` | Evidence or authority is insufficient for a decision. |

The exact canonical policy vocabulary remains `NEEDS VERIFICATION`.

### ADR-0017 activation states

ADR-0017 currently proposes:

- `denied`
- `draft`
- `active_internal`
- `active_public_candidate`
- `retired`

These are not synonymous with:

- lifecycle states such as RAW, QUARANTINE, PROCESSED, or PUBLISHED;
- runtime outcomes such as ANSWER, ABSTAIN, DENY, or ERROR;
- release states;
- test-run PASS or FAIL.

### Required reason-code families

A mature suite should expect stable reason-code families for:

```text
SOURCE_ID_*
SOURCE_ROLE_*
AUTHORITY_*
RIGHTS_*
SENSITIVITY_*
SOVEREIGNTY_*
CADENCE_*
FRESHNESS_*
ACCESS_*
CITATION_*
SOURCE_HEAD_*
REGISTRY_*
ACTIVATION_*
RECORD_ADMISSION_*
CONNECTOR_BOUNDARY_*
PIPELINE_BOUNDARY_*
DOWNSTREAM_PROPAGATION_*
CORRECTION_*
SUPERSESSION_*
RETIREMENT_*
PUBLIC_RELEASE_*
INTERNAL_ERROR_*
```

Reason codes are `PROPOSED` until accepted by contract or policy. Free-form prose alone is not a stable test interface.

[Back to top](#top)

---

## Fixture and test-data contract

### Confirmed schema-fixture family

The observed SourceDescriptor fixture family is:

```text
fixtures/contracts/v1/source/source_descriptor/
  README.md
  valid/
    README.md
    valid_1.json
  invalid/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
```

Confirmed current coverage:

- one complete positive SourceDescriptor;
- one negative SourceDescriptor missing required `source_id`;
- one expected-error file containing `required`.

That is real shape coverage, but it is narrow.

### Required future fixture classes

| Fixture class | Purpose | Expected posture |
|---|---|---|
| Valid public source | Complete public-safe descriptor. | Shape pass; no automatic activation or release. |
| Valid internal-only source | Complete descriptor with internal restriction. | Shape pass; public use denied. |
| Valid restricted source | Rights/sensitivity restrictions and obligations present. | Shape pass; downstream restrictions preserved. |
| Invalid missing identity | Missing or malformed source id/version. | Validation failure. |
| Invalid role | Unknown, unsupported, or contradictory role. | Validation failure or hold. |
| Role upgrade attempt | Candidate/modeled/aggregate/context upgraded downstream. | Anti-collapse failure. |
| Rights unknown | License or terms unresolved. | Hold, deny public use, or abstain. |
| Rights expired | Verification window expired. | Stale/hold/deny according to policy. |
| Sensitivity unknown | Missing classification or review. | Hold or deny. |
| Sovereignty/cultural review required | Community authority or cultural obligation unresolved. | Hold; no public use. |
| Stale cadence | Source missed expected refresh window. | Mark stale, abstain, hold, or deny publication. |
| Source-head drift | ETag/hash/version changed. | Re-review or quarantine; no silent update. |
| Citation missing | Required template or attribution absent. | Failure or abstention for public use. |
| Closed access | Credentials or permission needed. | No secret in fixture; access denied without test stub. |
| Connector disabled | Descriptor does not allow connector activation. | Connector must not run. |
| Record quarantined | Record violates source-specific minimum bar. | Explicit quarantine reason. |
| Superseded descriptor | New version replaces old without erasure. | Lineage pass; old state remains queryable. |
| Retired source | New fetch prohibited; historical records retained. | Deny new intake. |
| Correction | Rights, role, sensitivity, or citation posture corrected. | New record/notice; no silent mutation. |
| Public-boundary bypass | Unreleased/restricted source reaches UI/API/map/AI. | Failure or deny. |
| AI authority invention | Model assigns unsupported role or confidence. | Failure or abstention. |

### Sensitive-data safeguards

All default fixtures must be synthetic and public-safe.

Never use:

- real API keys, session cookies, access tokens, account identifiers, passwords, or private endpoints;
- real exact archaeology, rare species, rare plants, cultural/sacred, infrastructure, private parcel, living-person, or DNA/genomic details;
- unpublished source payloads;
- full restricted license text when a toy excerpt or metadata field is sufficient;
- production reviewer identities;
- real source-system secrets;
- data that would be unsafe if copied into a public CI artifact.

Sensitive-case fixtures should model the decision boundary using toy identifiers, generalized geometry, placeholder obligations, and expected denial/hold outcomes.

### Fixture-home conflict

The confirmed validator and schema harness use:

```text
fixtures/contracts/v1/source/source_descriptor/
```

The detailed schema metadata names:

```text
tests/fixtures/sources/source_descriptor/
```

The source registry README also proposes the latter path.

This is `CONFLICTED`. Do not duplicate fixtures to make both paths pass silently. Resolve by migration decision, compatibility redirect, or explicit loader support with tests proving one source of fixture truth.

[Back to top](#top)

---

## Required validation layers

A mature source suite should separate these layers.

### 1. Schema and syntax

- JSON/YAML parses.
- SourceDescriptor validates under the pinned schema.
- `$id`, version, and refs are resolvable.
- Required fields and nested conditionals are enforced.
- Unknown properties fail where the schema is closed.
- Zero fixtures is a failure or explicit no-case report.

### 2. Semantic contract

- SourceDescriptor means source-governance posture, not source truth.
- Contract exclusions are present.
- Role and authority meaning matches accepted vocabulary.
- Contract/schema/fixture/validator references resolve.
- Maturity labels match repo evidence.

### 3. Identity and versioning

- source id is stable and correctly namespaced;
- descriptor version changes when governed posture changes;
- source-head identity is separate from descriptor version;
- upstream version, ETag, checksum, or revision is captured where available;
- duplicate source ids and conflicting active versions fail;
- corrections and supersessions preserve lineage.

### 4. Source role and authority

- role is allowed;
- authority rank is allowed;
- allowed and prohibited claim roles are coherent;
- secondary roles do not override primary role silently;
- downstream representations preserve role;
- no AI or UI component invents role;
- role correction creates a new governed state.

### 5. Rights and terms

- rights status and terms/license are present;
- attribution, redistribution, commercial use, and AI-use obligations are modeled;
- verification time and verifier are present;
- expired, unknown, contested, incompatible, or unverified rights fail closed;
- terms changes trigger re-review and downstream correction.

### 6. Sensitivity and sovereignty

- sensitivity default is present;
- exact-location and protected-data policies are applied;
- review, redaction, generalization, delay, or staged-access obligations are explicit;
- the most restrictive applicable posture propagates;
- unknown or conflicting sensitivity fails closed;
- community, tribal, cultural, institutional, or data-sovereignty obligations are not reduced to a generic public flag.

### 7. Cadence and freshness

- update cadence and freshness expectation exist;
- retrieval time and source/valid/observed times remain distinct where material;
- stale-state policy is deterministic;
- missed updates, drift, retirement, and supersession are visible;
- stale source support cannot silently back current claims.

### 8. Access and security

- endpoint classes and access posture are explicit;
- secrets are referenced, never embedded;
- no default test makes live network calls;
- closed or account-gated sources use stubs;
- rate-limit and retry posture is testable where implemented;
- file and network writes remain bounded to temporary test space.

### 9. Citation and attribution

- required citation template and guidance are present;
- publisher attribution, preferred link, disclaimer, and role qualifier propagate;
- public outputs preserve citation and source role;
- citation presence does not substitute for evidence or rights clearance;
- missing citation support causes failure or abstention.

### 10. Registry and activation

- descriptor resolves from the accepted registry home;
- source authority register entry resolves where required;
- activation decision is explicit;
- active internal and public-candidate states remain distinct;
- retired or denied sources cannot activate connectors;
- descriptor-level admission does not equal publication.

### 11. Record-level admission

- source-specific minimum bar is enforced;
- invalid or ambiguous records are quarantined with reason codes;
- candidate records remain candidates;
- source identity and role follow the record;
- no record skips RAW/QUARANTINE, processing, evidence, policy, catalog, and release gates.

### 12. Connector and watcher boundary

- connectors read admitted source posture;
- connectors do not rewrite source authority;
- connectors do not publish;
- watchers may propose changes but do not activate or release them;
- default tests are no-network;
- static scans assert nonempty file sets and document blind spots.

### 13. Pipeline and derived-artifact boundary

- transforms preserve source refs, role, rights, sensitivity, cadence, and citation;
- derived layers are labeled as derived;
- aggregation does not create false precision;
- model output does not become observation;
- catalog, graph, tiles, maps, indexes, and summaries remain downstream carriers.

### 14. Evidence and public-consumer boundary

- EvidenceRef/EvidenceBundle resolution remains separate from source admission;
- governed APIs expose source posture appropriate to access role;
- UI/MapLibre source badges and caveats reflect admitted posture;
- Focus Mode and AI cite released evidence and abstain when support is insufficient;
- internal/restricted source detail is not leaked in public errors or citations.

### 15. Correction, supersession, retirement, and rollback

- source posture changes create auditable new state;
- prior descriptors remain retrievable;
- affected evidence, catalogs, releases, maps, exports, indexes, and AI caches are identified;
- stale or withdrawn public outputs are corrected or disabled;
- rollback target is explicit where operational state changes.

### 16. Compatibility and migration

- singular/plural, hyphen/underscore, and fixture-root aliases resolve consistently;
- one executable validator authority is identified;
- compatibility paths do not fork behavior;
- old paths fail with actionable migration messages when retired;
- registry, docs, schemas, fixtures, tests, workflows, and consumers migrate together.

[Back to top](#top)

---

## Current coverage and material gaps

| Concern | Current evidence | Coverage status |
|---|---|---:|
| SourceDescriptor JSON Schema | Detailed Draft 2020-12 schema exists. | `CONFIRMED / PROPOSED schema status` |
| SourceDescriptor valid fixture | One documented valid fixture. | `CONFIRMED NARROW` |
| SourceDescriptor invalid fixture | One missing-source-id fixture. | `CONFIRMED NARROW` |
| Dedicated SourceDescriptor validator | Top-level executable exists. | `CONFIRMED` |
| Aggregate validator execution | `make schemas` includes SourceDescriptor. | `CONFIRMED` |
| Generic schema pytest | Source family is fixture-gated in common harness. | `CONFIRMED PARTIAL` |
| Direct source-behavior tests | No direct module established. | `GAP` |
| Connector/pipeline non-publisher guard | Static lexical test exists. | `CONFIRMED BOUNDED` |
| Source-role evaluator | README lanes exist; executable behavior not established. | `GAP / NEEDS VERIFICATION` |
| Rights policy | Source policy root is a stub; broader policy coverage unresolved. | `GAP` |
| Sensitivity/sovereignty policy | No source-specific executable matrix established. | `GAP` |
| Cadence/freshness behavior | Schema fields exist; behavioral tests unestablished. | `GAP` |
| Citation propagation | Schema fields exist; consumer tests unestablished. | `GAP` |
| Registry resolution | Registry README exists; current instance/resolver behavior unresolved. | `GAP / UNKNOWN` |
| Activation states | Proposed ADR only. | `PROPOSED` |
| Record-level admission | No shared executable suite established. | `GAP` |
| Source-head drift | Schema surface exists; behavior unestablished. | `GAP` |
| Correction/supersession | Doctrine exists; cross-consumer tests unestablished. | `GAP` |
| Public API/UI/map/AI propagation | Not established by source suite. | `GAP` |
| Path migration | Multiple conflicts documented; no accepted migration. | `CONFLICTED` |
| Source-specific CI | TODO-only workflow; aggregate schema CI is substantive. | `PARTIAL` |
| Coverage report | No source coverage artifact established. | `GAP` |
| Branch protection dependency | Not inspected. | `UNKNOWN` |

### Non-vacuity requirements

Future source checks must fail or report explicitly when:

- `tests/source/` collects zero tests;
- fixture directories contain zero matching valid or invalid cases;
- static scans inspect zero files;
- registry scans find zero descriptors unexpectedly;
- no policy bundle was loaded;
- no consumer paths were exercised;
- an alias path was skipped silently;
- a live tier was requested but no source or credential stub was configured;
- expected reason codes are absent.

A green result from zero work is a failed governance signal.

[Back to top](#top)

---

## Deterministic execution and no-network posture

### Confirmed current commands

```bash
# Dedicated SourceDescriptor schema-fixture validation.
python tools/validators/validate_source_descriptor.py --fixtures

# Five-validator aggregate; SourceDescriptor runs first.
python tools/validators/_common/run_all.py

# Repository convenience target for the validator aggregate.
make schemas

# Generic schema-fixture pytest path, including source when fixture roots match.
python -m pytest -q tests/schemas/test_common_contracts.py

# Static connector/pipeline non-publisher boundary.
make boundary-guards

# CI-shaped boundary run with JUnit output.
make boundary-guards-ci
```

### Diagnostic direct-lane command

```bash
# Diagnostic only until a direct module exists.
python -m pytest --collect-only -q tests/source
```

Do not describe `pytest tests/source` as a substantive passing source suite until collection is nonzero and the collected case inventory is reviewed.

### Proposed future direct command

```bash
python -m pytest -q tests/source
```

This remains `PROPOSED`.

### Default tier

The default source-test tier must be:

- deterministic;
- no-network;
- synthetic;
- public-safe;
- credential-free;
- locale/timezone explicit;
- temporary-output only;
- stable under repeated execution;
- independent of vendor availability;
- explicit about fixture and schema versions.

### Live-source tier

Live checks, when admitted, must be separate and opt-in.

A live tier should require:

- explicit marker or command;
- source descriptor and activation posture;
- rights and terms confirmation;
- credential reference through approved secret handling;
- rate-limit and retry controls;
- read-only behavior;
- bounded endpoint and time window;
- redacted logs;
- no publication;
- receipt/report destination;
- timeout and cleanup;
- degraded or skipped behavior that does not mask default-suite failures.

Live source success is an operational probe, not source truth, evidence closure, release approval, or permission to publish.

### Determinism and replay

Tests should pin:

- schema and descriptor versions;
- fixture hashes;
- source-role vocabulary version;
- policy bundle version/digest when implemented;
- registry snapshot version;
- validator version or commit;
- clock/now value;
- timezone and locale;
- canonical JSON rules where identity depends on serialization;
- expected reason codes and outcomes.

[Back to top](#top)

---

## CI workflow and promotion boundary

### Confirmed workflow posture

| Workflow | Current action | Source-test significance |
|---|---|---|
| `source-descriptor-validate.yml` | Checkout plus TODO echo steps. | No substantive source validation. |
| `schema-validation.yml` | Runs `make schemas`. | Substantively executes SourceDescriptor validator through the aggregate. |
| `validator-suite.yml` | Runs `make schemas` and a separate evidence fail-closed check. | Substantively executes SourceDescriptor validator, but no source-specific report. |
| `contracts-validate.yml` | Runs `make test`. | Runs schema and contract lanes; source schema cases are fixture-gated. |
| `policy-boundary-guards.yml` | Runs static boundary suite for selected path filters. | Includes connector/pipeline non-publisher guard; target README is not a substantive source-behavior trigger. |

### Required future source CI

A mature source workflow should:

1. trigger on changes to source contracts, schemas, fixtures, policy, registry vocabularies, validators, connectors, source tests, relevant pipelines, and consumer adapters;
2. install pinned dependencies;
3. run SourceDescriptor validation and direct source behavior tests;
4. fail when collection or fixture polarity is unexpectedly zero;
5. emit a source-test coverage manifest;
6. emit machine-readable findings with reason codes;
7. upload only public-safe reports;
8. identify source/descriptor/schema/policy/fixture versions;
9. distinguish schema, semantic, policy, registry, connector, and consumer results;
10. never activate a source, fetch live data, mutate registry records, publish, or release by itself;
11. support local parity;
12. preserve correction and rollback references when source posture changes.

### Proposed coverage artifact

```json
{
  "suite": "tests/source",
  "commit": "<sha>",
  "schema_path": "schemas/contracts/v1/source/source_descriptor.schema.json",
  "schema_digest": "sha256:<digest>",
  "fixture_root": "fixtures/contracts/v1/source/source_descriptor",
  "collected": 0,
  "passed": 0,
  "failed": 0,
  "abstained": 0,
  "skipped_explicit": 0,
  "layers": {
    "schema": "covered",
    "source_role": "not_established",
    "rights": "not_established",
    "sensitivity": "not_established",
    "cadence": "not_established",
    "citation": "not_established",
    "registry": "not_established",
    "connector_boundary": "bounded_static",
    "public_consumer": "not_established"
  },
  "release_authority_created": false,
  "source_activation_created": false
}
```

This artifact is `PROPOSED`. Its home and schema require review before implementation.

### Promotion significance

A source test may support a future admission or promotion gate only when:

- test identity and scope are known;
- collection is nonzero;
- fixture versions and hashes are recorded;
- schema, contract, policy, and registry versions are pinned;
- negative cases fail closed;
- reason codes are stable;
- rights and sensitivity obligations are exercised where material;
- report integrity is verifiable;
- required human review remains separate;
- the release process consumes the result through an accepted contract.

A passing source test is never, by itself:

- source activation;
- rights approval;
- sensitivity clearance;
- evidence closure;
- policy approval;
- release approval;
- publication;
- a watcher permission;
- an AI authority grant.

[Back to top](#top)

---

## Failure interpretation

| Failure class | Meaning | Required response |
|---|---|---|
| Schema failure | Descriptor shape is invalid. | Reject fixture or candidate; do not infer semantics. |
| Contract failure | Meaning, exclusions, or cross-root declarations are incomplete. | Hold and correct contract/metadata. |
| Identity failure | Source id/version/head is missing, duplicate, or inconsistent. | Quarantine or hold; preserve evidence. |
| Role failure | Role is unsupported, contradictory, or upgraded downstream. | Deny use; emit anti-collapse reason. |
| Rights failure | Terms/license/attribution/use posture is unknown, expired, or incompatible. | Hold or deny public use. |
| Sensitivity failure | Classification, review, or transform is unresolved. | Deny or restrict; no precise public output. |
| Cadence failure | Source is stale or update expectation is unmet. | Mark stale, abstain, hold, or deny according to policy. |
| Citation failure | Required attribution or role qualifier is missing. | Block public claim or abstain. |
| Registry failure | Descriptor/register entry cannot resolve or conflicts. | Hold; do not activate connector. |
| Activation failure | No valid activation decision for requested use. | Deny connector or downstream use. |
| Record-admission failure | Record misses source-specific minimum bar. | Route to quarantine with reason. |
| Connector boundary failure | Connector writes toward catalog, release, or published targets. | Block and remediate; connector is non-publisher. |
| Consumer propagation failure | API/UI/map/AI drops source restrictions. | Block public surface and correct affected outputs. |
| Path-drift failure | Compatibility paths resolve to different schemas, validators, or fixtures. | Stop migration; choose or restore one authority. |
| Infrastructure error | Runner, resolver, or filesystem failed. | Return `ERROR`; do not classify source posture. |
| Zero-case result | Suite or scan did no meaningful work. | Fail or report noncoverage explicitly. |

### Fail-closed principle

When a test cannot distinguish safe from unsafe source use, it should not guess. It should produce an explicit failure, abstention, hold, or error with enough context for steward review.

### Quarantine is not deletion

A failed source or record should remain traceable when rights and policy allow retention. Quarantine should preserve:

- source and descriptor identity;
- reason codes;
- input digest or governed reference;
- run/attempt identity;
- time of decision;
- validator and policy versions;
- reviewer obligation;
- correction or retry path.

[Back to top](#top)

---

## What a passing check does not prove

Even complete success does not prove that:

- the source's claims are true;
- the source is complete or error-free;
- the source is the highest authority for every claim;
- the source is currently reachable;
- rights or terms will remain unchanged;
- sensitive content may be public;
- every record was admitted;
- EvidenceBundle closure exists;
- catalog, graph, map, or AI outputs are correct;
- a connector may publish;
- a watcher may merge or activate;
- a release is approved;
- a public UI may expose exact source detail;
- an AI answer is authoritative;
- all domains interpret the source identically;
- production enforcement matches test behavior;
- branch protection requires the check.

Tests provide bounded enforceability evidence. They do not create truth or authority.

[Back to top](#top)

---

## Review burden and change control

| Change | Minimum review posture |
|---|---|
| README-only source-test clarification | QA/source/docs reviewer. |
| New direct source test | QA + source steward + affected implementation owner. |
| Source role or authority vocabulary | Source + governance + affected domain stewards; ADR-class review where required. |
| Rights/terms test | Rights/legal steward + source steward. |
| Sensitivity or sovereignty test | Sensitivity/security + relevant domain/community authority. |
| Source fixture | Fixture + source + schema/contract owner; sensitive review when material. |
| Schema or contract pairing | Schema + contract + source steward. |
| Registry-resolution test | Registry + source + control-plane steward. |
| Connector boundary test | Connector + pipeline + policy + QA reviewers. |
| Public API/UI/map/AI test | Consumer owner + evidence + policy + release reviewer. |
| Live-source tier | Source + security + rights + infra + CI steward. |
| Path migration | Directory steward + affected root owners; ADR/migration note where authority homes change. |
| Test removal or weakening | QA + source + affected gate owner; explicit coverage impact. |

### Separation of duties

Where source activation or public release is policy-significant:

- connector implementer should not be the sole activation approver;
- source steward should not be the sole rights reviewer;
- model/AI author should not assign source authority;
- fixture author should not be the sole validator reviewer;
- validator pass should not replace human review;
- release approval remains outside the test lane.

### Change budget

A README-only PR should not silently:

- add or alter tests;
- change schema or contract meaning;
- change source-role enums;
- activate a source;
- mutate registry records;
- change policy;
- change workflow behavior;
- create receipts or proofs;
- move authority paths;
- publish or release data.

Those changes require their own scoped review.

[Back to top](#top)

---

## Definition of done

This README update is complete when:

- [x] repository, base, target, and prior blob are pinned;
- [x] Directory Rules and parent test-lane posture are checked;
- [x] direct and adjacent executable surfaces are distinguished;
- [x] current SourceDescriptor schema, fixture, validator, aggregate, Makefile, and workflow paths are documented;
- [x] source path/name/fixture-root conflicts are explicit;
- [x] v0.1 scope and anti-collapse rules are preserved;
- [x] no executable maturity is invented;
- [x] no source authority, activation, policy, release, or publication action is taken;
- [ ] human review approves the documentation;
- [ ] CI completes for the pull request.

A future **mature direct source suite** is done only when:

- [ ] direct tests collect nonzero cases;
- [ ] fixture inventory covers valid, invalid, restricted, stale, denied/held, correction, and migration cases;
- [ ] SourceDescriptor shape and semantic contract pairing are enforced;
- [ ] source role and authority anti-collapse are tested;
- [ ] rights and sensitivity policy behavior is tested;
- [ ] cadence, freshness, citation, and source-head drift are tested;
- [ ] registry and activation behavior is tested;
- [ ] record-level admission and quarantine reason codes are tested;
- [ ] connector/watcher non-publisher behavior is tested dynamically where practical;
- [ ] downstream API/UI/map/AI restrictions are tested;
- [ ] correction, supersession, retirement, and rollback propagation are tested;
- [ ] compatibility-path drift is resolved or deliberately guarded;
- [ ] no-network default and governed live tier are separate;
- [ ] source-specific CI emits a public-safe coverage artifact;
- [ ] zero collection and zero scans fail;
- [ ] local and CI commands match;
- [ ] required-check and promotion significance are documented;
- [ ] owners and CODEOWNERS are confirmed.

[Back to top](#top)

---

## Incremental implementation sequence

Prefer the smallest reversible progression.

### Phase 1 — Inventory and non-vacuity

- add a direct inventory test or manifest;
- assert nonzero collected cases;
- assert the SourceDescriptor fixture family has at least one valid and invalid case;
- emit exact schema/fixture/validator paths.

### Phase 2 — Path reconciliation guard

- test singular/plural and hyphen/underscore relationships;
- identify the one executable validator entrypoint;
- fail if compatibility metadata points to missing or divergent implementations;
- preserve migration diagnostics.

### Phase 3 — SourceDescriptor shape expansion

- add invalid cases for every required nested group;
- add enum, pattern, conditional, additional-property, and source-head cases;
- add internal-only, restricted, stale, retired, and superseded valid cases.

### Phase 4 — Semantic and role tests

- test SourceDescriptor exclusions;
- test allowed/prohibited claim roles;
- add candidate/modeled/aggregate/context/synthetic anti-collapse cases;
- add AI role-invention denial.

### Phase 5 — Rights, sensitivity, cadence, and citation

- bind accepted policy evaluator;
- add rights unknown/expired/incompatible cases;
- add sensitivity/sovereignty review and transform obligations;
- add stale cadence and missing citation cases.

### Phase 6 — Registry and activation

- test registry resolution and version conflict;
- test activation states after ADR acceptance or explicit profile pinning;
- test retired and denied source behavior;
- test correction and supersession lineage.

### Phase 7 — Record-level admission

- define source-specific admission-case interface;
- add quarantine and reason-code assertions;
- prove records cannot skip lifecycle gates;
- integrate selected domain source lanes.

### Phase 8 — Connector and downstream propagation

- supplement static non-publisher scan with behavioral tests;
- test connector dry-run destinations and receipts;
- test pipeline preservation of source posture;
- test API/UI/map/AI restriction and citation propagation.

### Phase 9 — CI and release integration

- replace TODO source workflow with substantive local-parity commands;
- emit coverage manifest and JUnit/JSON artifacts;
- define required checks and promotion dependencies;
- preserve human review and release separation.

Each phase should be independently reviewable and revertible.

[Back to top](#top)

---

## Maintenance and fixture update rules

Update this README whenever any of these change:

- direct `tests/source/` inventory;
- lane retention, migration, or compatibility posture;
- SourceDescriptor contract or schema;
- source role, authority, rights, sensitivity, cadence, access, or citation vocabulary;
- fixture root, fixture count, or fixture naming;
- validator entrypoint, registry id, or aggregate runner;
- source policy implementation;
- source registry layout or resolver;
- activation-state contract or ADR status;
- connector/watcher boundary;
- Makefile command;
- workflow trigger, command, artifact, or required-check status;
- downstream API/UI/map/AI consumer behavior;
- correction, supersession, retirement, or rollback process.

### Fixture update discipline

When a source fixture changes:

1. identify the contract/schema/policy field that changed;
2. update valid and invalid polarity together where material;
3. update expected reason/error text;
4. update fixture hashes or coverage manifest;
5. run direct validator and generic schema harness;
6. run source behavior tests if present;
7. update affected source/domain/docs indexes;
8. record migration for breaking vocabulary or path changes.

### Deprecation and supersession

Do not delete old source test cases silently.

A deprecated case should retain:

- old case id;
- reason for deprecation;
- successor case;
- affected source/schema/policy versions;
- last applicable commit or release;
- rollback path.

[Back to top](#top)

---

## Open verification register

| ID | Question | Evidence needed | Current status |
|---|---|---|---|
| SRCTEST-001 | Is `tests/source/` retained as the permanent cross-cutting lane? | Accepted test-layout decision, Directory Rules refinement, or migration note. | `NEEDS VERIFICATION` |
| SRCTEST-002 | Why do older docs propose `tests/sources/` while singular README exists? | Path authority and migration review. | `CONFLICTED` |
| SRCTEST-003 | Which schema path is canonical: singular `source/` or plural `sources/`? | Accepted ADR/migration and updated `$id`/metadata. | `CONFLICTED` |
| SRCTEST-004 | Which filename is canonical: `source_descriptor` or `source-descriptor`? | Slug/filename decision and compatibility tests. | `CONFLICTED` |
| SRCTEST-005 | Which fixture root is canonical? | Schema metadata, validator implementation, fixture index, and migration decision. | `CONFLICTED` |
| SRCTEST-006 | Which validator path is canonical? | Validator registry, one executable entrypoint, compatibility redirects, and CI references. | `CONFLICTED` |
| SRCTEST-007 | Are source-role validators executable? | Source files, entrypoints, tests, and run evidence. | `NOT ESTABLISHED` |
| SRCTEST-008 | Which SourceDescriptor cases are currently collected and passing? | Pytest collection and validator run at pinned commit. | `UNKNOWN` |
| SRCTEST-009 | Does `make schemas` fail on all relevant SourceDescriptor invalid fixtures? | Run logs and complete fixture manifest. | `NEEDS VERIFICATION` |
| SRCTEST-010 | Is policy/source substantive? | Policy files, evaluator binding, fixtures, tests, and run evidence. | `NO — STUB AT SNAPSHOT` |
| SRCTEST-011 | Which rights and sensitivity policies govern source use? | Accepted policy bundles and obligation tests. | `UNKNOWN` |
| SRCTEST-012 | Is ADR-0017 accepted, superseded, or still proposed at implementation time? | Current ADR status and decision log. | `PROPOSED AT SNAPSHOT` |
| SRCTEST-013 | Where are active SourceDescriptor instances and authority records stored? | Registry inventory and control-plane register evidence. | `NEEDS VERIFICATION` |
| SRCTEST-014 | Does source-head drift trigger re-review and downstream correction? | Validator/policy/registry/consumer tests and logs. | `UNKNOWN` |
| SRCTEST-015 | Are connectors dynamically prevented from publishing? | Runtime/behavior tests in addition to static lexical scan. | `PARTIAL / NEEDS VERIFICATION` |
| SRCTEST-016 | Do APIs, UI, maps, exports, graph, and AI preserve source restrictions? | Consumer tests and governed runtime evidence. | `UNKNOWN` |
| SRCTEST-017 | Which source checks are required by branch protection or promotion? | Rulesets, workflow checks, and release gate config. | `UNKNOWN` |
| SRCTEST-018 | What are current pass rates and coverage? | CI/local run artifacts and coverage manifest. | `UNKNOWN` |
| SRCTEST-019 | Who owns this lane and its reviews? | CODEOWNERS and steward registry. | `NEEDS VERIFICATION` |
| SRCTEST-020 | How are source corrections, retirement, and supersession propagated? | Accepted contracts, registry logic, release records, and consumer tests. | `UNKNOWN` |
| SRCTEST-021 | Which domain source lanes are executable rather than README scaffolds? | Domain test inventory and collection report. | `NEEDS VERIFICATION` |
| SRCTEST-022 | Should a direct source suite consume schema fixtures or separate behavior fixtures? | Fixture authority decision and test design review. | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior `tests/source/README.md` blob | `CONFIRMED` | v0.1 scope, exclusions, expected families, and anti-collapse intent. | Planning-oriented and stale on parent-lane placement. |
| `tests/README.md` | `CONFIRMED` | Canonical tests root and `tests/source/` compatibility-lane posture. | Does not prove executable depth. |
| `contracts/source/README.md` | `CONFIRMED` | Source semantic boundary and anti-collapse rules. | Draft/proposed; implementation references partly stale. |
| `schemas/contracts/v1/source/README.md` | `CONFIRMED` | Mixed schema maturity and singular/plural, hyphen/underscore drift. | Family index does not prove acceptance or current run status. |
| `source_descriptor.schema.json` | `CONFIRMED FILE / PROPOSED STATUS` | Rich required field groups, closed shape, conditionals, source-head and governance metadata. | Metadata names conflicting canonical, fixture, and validator paths. |
| SourceDescriptor fixture README | `CONFIRMED` | One valid and one invalid fixture plus observed fixture layout. | Narrow coverage; prior run not evidence of current pass. |
| `tools/validators/validate_source_descriptor.py` | `CONFIRMED EXECUTABLE` | Current top-level schema/fixture validation entrypoint. | Shape only; no source policy or runtime behavior. |
| `tools/validators/_common/run_all.py` | `CONFIRMED EXECUTABLE` | SourceDescriptor is in five-validator aggregate. | Fail-fast aggregate is not a source coverage report. |
| `tests/schemas/test_common_contracts.py` | `CONFIRMED EXECUTABLE` | Generic source family valid/invalid fixture behavior. | Fixture-gated discovery can omit unpopulated schemas. |
| `tests/policy/test_pipeline_connector_non_publisher.py` | `CONFIRMED EXECUTABLE` | Static connector/pipeline publication-target guard. | Lexical and file-extension bounded; not dynamic enforcement. |
| `tests/policy/README.md` | `CONFIRMED` | Exact boundary-suite commands and limits. | Policy engine/source policy behavior remains unestablished. |
| `tools/validators/sources/README.md` | `CONFIRMED COMPATIBILITY DOC` | Validator path fragmentation and one-entrypoint rule. | Predates/does not center the confirmed top-level executable. |
| `data/registry/sources/README.md` | `CONFIRMED DOCUMENT / PROPOSED BUNDLE` | Registry purpose, admission boundary, older proposed paths. | Generated outside mounted repo; several paths conflict with current evidence. |
| `policy/source/README.md` | `CONFIRMED STUB` | Source policy path exists. | No substantive rules or evaluator. |
| ADR-0017 | `CONFIRMED DOCUMENT / PROPOSED DECISION` | Two admission senses, activation flow, states, fixtures-first, connector non-publisher doctrine. | Not accepted implementation evidence. |
| `source-descriptor-validate.yml` | `CONFIRMED TODO SCAFFOLD` | Workflow name and trigger exist. | Echoes TODO; no validation. |
| `schema-validation.yml` and `validator-suite.yml` | `CONFIRMED EXECUTION` | `make schemas` runs in CI and includes SourceDescriptor. | No source-specific behavior artifact or coverage matrix. |
| `contracts-validate.yml` | `CONFIRMED EXECUTION` | `make test` runs schema and contract lanes. | Direct source lane excluded. |
| `policy-boundary-guards.yml` | `CONFIRMED EXECUTION` | Runs non-publisher guard for selected changes. | Does not establish complete source admission or policy. |
| Bounded GitHub code search | `CONFIRMED SEARCH RESULT` | Proposed v0.1 direct test names surfaced only the README. | Not exhaustive history, ignored-file, or dynamic-generation proof. |
| Exact `tests/sources/README.md` fetch | `NOT FOUND` | Confirms proposed plural README is absent at snapshot. | Does not prove absence of every plural test file or historical path. |

### No-loss assessment

The v0.1 README’s strongest material is retained and expanded:

- source admission remains the first trust-spine gate;
- SourceDescriptor governs how a source may be treated, not whether its claims are true;
- source roles cannot be silently upgraded;
- unknown rights and sensitivity fail closed;
- cadence, access, citation, source-head, and registry posture remain explicit;
- connectors, watchers, loaders, pipelines, API/UI, and AI remain subordinate to admitted source posture;
- candidates, modeled outputs, aggregates, regulatory/administrative records, and synthetic material remain distinct;
- default tests remain synthetic and no-network;
- source records, contracts, schemas, policy, fixtures, implementation, evidence, receipts, proofs, lifecycle data, and release records remain in their owning roots.

The schematic `.test.PROPOSED` filenames and blanket “no executable runner verified” statement were replaced with the confirmed current validator, fixtures, schema harness, aggregate runner, static boundary test, workflows, and explicit coverage gaps.

[Back to top](#top)

---

## Documentation correction and rollback

This README is documentation, not a source registry record, source activation decision, policy decision, evidence object, receipt, release record, or public artifact.

### Correction triggers

Correct this README when:

- a direct source test is added or removed;
- lane retention or migration is decided;
- singular/plural or hyphen/underscore paths are resolved;
- fixture roots or validator paths change;
- SourceDescriptor schema or contract changes;
- source role, rights, sensitivity, cadence, access, citation, or activation vocabulary changes;
- policy/source becomes substantive;
- registry or authority-register implementation is verified;
- source-specific workflow becomes substantive;
- consumer enforcement is added;
- ADR-0017 changes status;
- CI or branch-protection significance changes;
- any statement becomes stale, contradicted, or overbroad.

### Rollback path

Before merge:

- leave the draft pull request unmerged; or
- restore the prior blob in a transparent follow-up commit on the same branch.

After merge:

- revert the documentation commit or pull request;
- do not reset or rewrite shared history;
- preserve the superseded v0.2 record in Git history;
- file a drift/correction note when rollback reflects a substantive governance conflict rather than a simple editorial error.

Rolling back this README does not roll back a source activation, registry state, connector run, schema, fixture, validator, policy bundle, workflow, receipt, proof, release, or public artifact because this change modifies documentation only.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Review state | Draft, repository-grounded documentation update |
| Direct lane maturity | README-only compatibility lane at bounded snapshot |
| Adjacent executable maturity | SourceDescriptor shape validator and fixtures confirmed; static connector/pipeline non-publisher guard confirmed |
| Dedicated source behavior suite | Not established |
| Next smallest safe change | Add a non-vacuous direct inventory/path-consistency test before adding broader source-policy behavior tests. |

---

*Last updated: 2026-07-16 · Version: v0.2 · Authority: enforceability documentation only · [Back to top](#top)*
