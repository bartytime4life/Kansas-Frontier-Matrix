<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-validators-readme
title: tests/validators/ — Validator Test Lane
type: README
version: v0.14
status: draft; repository-grounded; executable-test-index; mixed-workflow-coverage; non-authoritative
owners: ["OWNER_TBD — validator and QA stewardship remains unverified"]
created: 2026-07-07
updated: 2026-08-31
supersedes: v0.13 documentation at the same path; no test, validator, registry, workflow, fixture, or authority state is superseded
policy_label: public-doc; tests; validators; deterministic; no-network-default; fail-closed; non-authoritative
owning_root: tests/
responsibility: index executable validator tests, current registry and compatibility execution surfaces, failure interpretation, maintenance obligations, and authority limits
truth_posture: CONFIRMED 433 tracked files, 402 test modules, 17 direct child directories, 26 registered validators, four named registry profiles, and a nine-validator historical compatibility aggregate at the pinned main snapshot / UNKNOWN complete collected case count, coverage, mutation score, flake rate, required-check status, production parity, accountable ownership, correction propagation, and operational rollback
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_target_prior_blob: beda059555042c7b256b6ee93b288f40a9a8d37f
evidence_tests_tree: 2852d7576bc72c1aa5b35efb90a9a7a52351ee98
tracked_file_count: 433
test_module_count: 402
direct_child_directory_count: 17
registered_validator_count: 26
legacy_compatibility_validator_count: 9
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/runbooks/VALIDATOR_ORCHESTRATOR.md
  - ../../tools/validators/README.md
  - ../../tools/validators/validator_registry.json
  - ../../tools/validators/validate_all.py
  - ../../tools/validators/_common/run_all.py
  - ../../Makefile
  - ../../pyproject.toml
  - ../../.github/workflows/validator-suite.yml
  - ../../.github/workflows/schema-validation.yml
notes:
  - "v0.14 replaces the stale seven-entry, focused-lane snapshot with a bounded current inventory and registry-driven execution map."
  - "Counts describe tracked source paths at the pinned tree; they are not collected-test, coverage, required-check, or production-parity claims."
  - "The canonical registry and its reports coordinate checks but do not become evidence, policy, review, release, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/validators/` — Validator Test Lane

This directory contains executable conformance tests for shared validator
mechanics, validator entrypoints, governance checks, domain-facing validator
bindings, documentation tooling, receipts, release-support checks, and other
bounded validation surfaces.

A passing test supports only its named assertion against the checked revision.
It does not establish source authority, semantic truth, rights or sensitivity
clearance, policy approval, evidence closure, review completion, lifecycle
promotion, release, deployment, publication, or production parity.

## Quick start

Validate the canonical registry without running child validators:

```bash
make validator-registry-check
```

List registered validator IDs and profiles:

```bash
make validator-list
```

Run the canonical profiles:

```bash
make validator-focused
make validator-release-profile
make validator-full
```

Run the historical schema-fixture compatibility surface:

```bash
make schemas
```

Run this test subtree directly for diagnostic collection:

```bash
python -m pytest tests/validators -q
```

> [!IMPORTANT]
> The direct pytest command is not a declared root Make target or a claim of
> complete repository validation. Use focused commands and workflow bindings
> below when reviewing a particular implementation slice.

## Snapshot and scope

This README is grounded in
`main@5d835798e09a4dd14735779cb44206a8a3e8b2d3` and the
`tests/validators/` tree
`2852d7576bc72c1aa5b35efb90a9a7a52351ee98`.

| Inventory fact | Confirmed value | Boundary |
|---|---:|---|
| Tracked files | 433 | File count is not a collected test count. |
| `test_*.py` modules | 402 | Module presence does not prove execution or coverage. |
| Direct child directories | 17 | Nested homes group primary assertions; they are not new authority roots. |
| Markdown files | 17 | Documentation does not substitute for executable checks. |
| Canonical registry entries | 26 | Registry membership is bounded coordination metadata. |
| Historical compatibility entries | 9 | `make schemas` intentionally selects only this reviewed subset. |

The previous README described a seven-entry aggregate and a much smaller direct
lane. Both claims are stale. The compatibility aggregate now selects nine
validator IDs, while the canonical registry-driven orchestrator owns 26 entries.

## Directory inventory

Counts below are exact for tracked files in the pinned tree.

| Lane | Files | Test modules | Purpose boundary |
|---|---:|---:|---|
| Root | 214 | 212 | Shared entrypoints, registries, cross-cutting validators, and compatibility tests. |
| `catalog_closure/` | 2 | 2 | Catalog closure validation. |
| `common/` | 1 | 1 | Shared object-family validation. |
| `correction/` | 1 | 1 | Correction-impact validation. |
| `data/` | 3 | 3 | Data and analytical-view validation. |
| `directory_governance/` | 14 | 10 | Root registry, topology, aliases, and placement checks. |
| `docs/` | 32 | 8 | Metadata, links, document graph, stale scan, and truth-label tooling. |
| `domains/` | 54 | 54 | Domain-owned validator bindings and convergence tests. |
| `evidence/` | 37 | 37 | Evidence, provenance, measurement, and claim-boundary validation. |
| `governance/` | 48 | 48 | Repository, workflow, review, lifecycle, and governance checks. |
| `map/` | 7 | 7 | Map, renderer, 3D, and manifest validation. |
| `receipts/` | 1 | 1 | Typed receipt aggregation. |
| `release/` | 6 | 6 | Release-adjacent API and conditional-write checks. |
| `review/` | 1 | 1 | Review-sharing validation. |
| `stac/` | 2 | 2 | STAC behavior and metadata profiles. |
| `telemetry/` | 4 | 3 | Lineage and sustainability telemetry checks. |
| `ui/` | 5 | 5 | UI registry, camera, playback, and hydration validation. |
| `watchers/` | 1 | 1 | Watcher gate-packet validation. |

The tree also contains 17 Markdown files and 14 non-test support or fixture
files. Consult the Git tree for exact filenames; do not maintain a 400-line
manual filename mirror in this README.

## Authority and placement

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) assign
executable conformance evidence to `tests/` and repository-wide validator
implementation to `tools/`.

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| Validator implementation | [`tools/validators/`](../../tools/validators/README.md) | Exercise behavior; do not duplicate implementation. |
| Validator selection metadata | [`validator_registry.json`](../../tools/validators/validator_registry.json) | Test registry shape and selection; do not infer policy or release authority. |
| Machine shape | `schemas/` | Validate against schemas; do not redefine them. |
| Semantic meaning | `contracts/` | Test declared meaning; do not become contract authority. |
| Policy | `policy/` | Exercise accepted decisions or synthetic inputs; never approve use. |
| Reusable fixtures | `fixtures/` | Consume public-safe fixtures; do not create a parallel fixture registry. |
| Test-local support | `tests/fixtures/` or bounded lane-local fixtures | Keep synthetic, public-safe, and non-authoritative. |
| Workflow orchestration | `.github/workflows/` | Workflows invoke checks and report bounded outcomes. |
| Release and publication | `release/` and governed publication surfaces | Test prerequisites and denials; never promote or publish. |

A test should live here when validator mechanics, validator entrypoint behavior,
or a cross-cutting validator contract is the primary assertion. Domain,
schema, contract, policy, release, application, and package-local assertions
should remain with their owning responsibility lane unless current precedent
shows a shared validator boundary.

## Canonical orchestrator

[`tools/validate_all.py`](../../tools/validate_all.py) is the thin canonical
entrypoint. Its implementation lives in
[`tools/validators/validate_all.py`](../../tools/validators/validate_all.py),
and executable selection metadata lives in
[`validator_registry.json`](../../tools/validators/validator_registry.json).

The pinned registry contains 26 validators and four named profiles:

| Profile | Registered IDs | Selection behavior |
|---|---:|---|
| `focused` | 4 | Small trust-spine subset declared by the registry. |
| `changed-area` | 0 fixed IDs | Selects entries whose registered globs match supplied changed paths. |
| `release-dry-run` | 13 | Release-adjacent evidence, receipt, catalog, and release-support checks. |
| `full` | 26 | Every registered validator exactly once in registry order. |

The orchestrator emits deterministic JSON by default and distinguishes:

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | 0 | Every selected child exited successfully. |
| `ABSTAIN` | 0 | Changed-area selection matched no validator; no pass claim is made. |
| `FAIL` | 1 | At least one selected validator rejected its input. |
| `ERROR` | 2 | Registry, path, I/O, timeout, or child-system failure occurred. |

Raw child output is excluded from the default report. Timing is also excluded
unless explicitly requested, which keeps equivalent reports deterministic.

For complete operating details, use the
[Validator Orchestrator Runbook](../../docs/runbooks/VALIDATOR_ORCHESTRATOR.md).

## Historical compatibility surface

[`tools/validators/_common/run_all.py`](../../tools/validators/_common/run_all.py)
remains the implementation behind `make schemas`. It delegates to the
canonical orchestrator engine but explicitly requests these nine reviewed
fixture-capable validator IDs:

1. `source-descriptor`
2. `evidence-ref`
3. `evidence-bundle`
4. `layer-manifest`
5. `dataset-version`
6. `runtime-response-envelope`
7. `decision-envelope`
8. `run-receipt`
9. `ingest-receipt`

This compatibility command does not equal the `full` profile. In particular,
it does not silently add catalog-closure, release-support, dependency,
workflow-security, or topology validators.

New operator-facing use should select a canonical profile or explicit
registered IDs. Existing workflow-compatible use of `make schemas` remains a
bounded historical surface.

## Make targets

| Command | Current scope |
|---|---|
| `make validator-registry-check` | Parse and validate the canonical registry. |
| `make validator-list` | List profiles and validator IDs. |
| `make validator-focused` | Run the four-entry focused profile. |
| `make validator-release-profile` | Run the 13-entry release-dry-run profile. |
| `make validator-full` or `make validators` | Run all 26 registered validators. |
| `make validator-changed-area CHANGED_PATH_FILE=<file>` | Select validators from a newline-delimited path list. |
| `make schemas` | Run the nine-entry compatibility schema-fixture aggregate. |
| `make test` | Run `tests/schemas` and `tests/contracts`; it does not collect this lane. |
| `make validate` | Run `make schemas` and `make test`; it still does not collect all 402 validator test modules. |

Do not use a green `make schemas`, `make test`, or `make validate` result as
evidence that the entire validator test tree ran.

## Hosted workflow coverage

### `validator-suite`

[`validator-suite.yml`](../../.github/workflows/validator-suite.yml) runs on
pull requests, pushes to `main`, and manual dispatch. Its current bounded work
includes:

- canonical registry validation;
- workflow-security and repository-topology ratchets;
- a nonempty, unique, resolvable compatibility inventory check;
- focused shared JSON Schema runner tests;
- focused generated-receipt tests and fixture polarity;
- focused MaterialChangeAssessment tests and fixture polarity;
- `make schemas`;
- one reviewed invalid EvidenceBundle canary.

The workflow does not collect all 402 modules and emits no canonical validation
report, receipt, proof, policy decision, lifecycle record, release record, or
published artifact.

### `schema-validation`

[`schema-validation.yml`](../../.github/workflows/schema-validation.yml)
checks schema JSON structure, canonical schema identity, the nine configured
compatibility fixture families, and the schema/contract test lane. It is not the
canonical full validator profile and does not prove complete direct coverage.

Other focused workflows collect particular modules or directories. Workflow
presence and a green result do not establish required-check status or release
dependency.

## Focused execution examples

Shared JSON Schema runner:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_jsonschema_runner.py' \
  --verbose
```

Canonical orchestrator:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validator_orchestrator.py' \
  --verbose
python tools/validate_all.py --validate-registry
python tools/validate_all.py --profile focused
```

Historical compatibility boundary:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_legacy_schema_runner_scope.py' \
  --verbose
python tools/validators/_common/run_all.py
```

Documentation metadata and links:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  --warnings-as-errors \
  tests/validators/README.md

python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose
```

A focused command proves only its named implementation slice. It should be
paired with the implementation, fixture, workflow, or contract checks affected
by the change under review.

## Test and fixture contract

Substantive validator tests should make these facts inspectable:

- implementation and validator identity;
- schema, contract, policy, registry, and fixture bindings;
- valid, invalid, error, deny, hold, abstain, correction, or rollback posture;
- exact expected exit and bounded diagnostics;
- deterministic filesystem, time, locale, randomness, and environment controls;
- network and side-effect posture;
- public-safety and sensitivity assumptions;
- a negative companion that prevents vacuous success;
- what a pass does not prove.

Fixtures must be synthetic or legally reusable, public-safe for repository
visibility, free of credentials and production payloads, and appropriately
generalized for exact-location, archaeology, rare-species, infrastructure,
living-person, DNA/genomic, private-parcel, or culturally sensitive cases.

Default tests should not call live APIs, registries, databases, tile services,
models, or secret managers. Network-dependent point-in-time checks belong in
explicitly bounded workflows and must remain distinguishable from deterministic
fixture tests.

## Failure interpretation

| Failure | Interpret as | Do not interpret as |
|---|---|---|
| Unit test failure | The named behavior changed or regressed for the tested case. | Proof that a real-world claim is false. |
| Registry validation error | Selection metadata is malformed, unsafe, or internally inconsistent. | A reviewed business denial. |
| Validator `FAIL` | A selected validator rejected its declared input. | Policy, review, release, or publication authority. |
| Orchestrator `ERROR` | Execution or configuration failed. | Expected invalidity or fail-closed proof. |
| Empty changed-area selection | `ABSTAIN`; no matching validator ran. | An all-pass result. |
| Fixture polarity failure | Valid/invalid expectations or harness behavior diverged. | Permission to weaken the fixture. |
| Workflow failure | The checked revision did not satisfy that workflow. | Automatic rollback or release withdrawal. |

Preserve `FAIL` and `ERROR` as distinct outcomes. An arbitrary nonzero exit is
not evidence that the reviewed negative condition was detected.

## Non-vacuity and safety requirements

A trust-bearing test or workflow should fail when its declared subject is
missing or empty. As applicable, require:

- at least one collected test for a declared module;
- nonempty valid and invalid fixture lanes;
- existing, unique, repository-contained registry paths;
- a deliberately valid canary and a deliberately invalid canary;
- visible skips, exclusions, holds, and abstentions;
- deterministic ordering and bounded diagnostics;
- symlink and path-escape refusal;
- no unauthorized writes;
- no secret or sensitive-payload echo;
- explicit timeout and resource limits for risky parsers or subprocesses.

A test count, module count, registry count, workflow count, or green check is not
a coverage report.

## Maintenance

When tests, validators, registry entries, profiles, fixtures, commands, or
workflows change:

1. identify the primary responsibility owner;
2. update focused positive and negative tests;
3. preserve or intentionally version exit codes and diagnostics;
4. update registry membership, path globs, profile membership, or documented
   compatibility exclusions;
5. verify nonempty fixture polarity and safe paths;
6. run the narrowest affected tests;
7. run registry validation and the affected profile;
8. run `make schemas` when the nine-entry compatibility surface changes;
9. inspect the exact-head workflow outcome and any skipped work;
10. update this README when inventory, commands, or workflow bindings change;
11. preserve correction and rollback visibility;
12. do not infer promotion or publication from passing validation.

Shared helper or orchestrator changes require broader review because many
entrypoints and tests consume them.

## Known gaps

The following remain unverified or incomplete:

- complete collected test-case count across 402 modules;
- coverage, mutation score, runtime budget, and flake rate;
- a single hosted workflow that collects the complete subtree;
- complete mapping from every executable validator to registry membership,
  focused tests, fixtures, workflows, and exclusions;
- required-check and branch-protection significance;
- production invocation and parity;
- accountable validator and QA stewardship;
- machine artifact retention for all focused workflows;
- correction propagation and operational rollback drills;
- complete resource-budget and sensitive-fixture review.

Keep these as explicit gaps. Do not turn the current inventory into a maturity
or release claim.

## Open verification register

| ID | Question | Status |
|---|---|---|
| `VAL-TST-001` | Who is accountable for this lane and its review route? | NEEDS VERIFICATION |
| `VAL-TST-002` | Which tests should remain shared versus owner-local? | NEEDS VERIFICATION |
| `VAL-TST-003` | Does the registry cover every executable validator intended for orchestration? | UNKNOWN |
| `VAL-TST-004` | Which validators must remain in the nine-entry compatibility surface? | NEEDS VERIFICATION |
| `VAL-TST-005` | Which executable validators are intentionally excluded, and why? | UNKNOWN |
| `VAL-TST-006` | Which shared helper APIs and output contracts are compatibility-sensitive? | UNKNOWN |
| `VAL-TST-007` | Which exit-code contracts are accepted and versioned? | NEEDS VERIFICATION |
| `VAL-TST-008` | Which diagnostics and reason codes are stable interfaces? | NEEDS VERIFICATION |
| `VAL-TST-009` | Which focused checks must emit retained machine-readable reports? | NEEDS VERIFICATION |
| `VAL-TST-010` | Which fixture families require both positive and negative lanes? | NEEDS VERIFICATION |
| `VAL-TST-011` | Which empty selections must error versus abstain? | NEEDS VERIFICATION |
| `VAL-TST-012` | Are all authority and object-family bindings current? | UNKNOWN |
| `VAL-TST-013` | What parser, path, memory, and runtime budgets are required? | NEEDS VERIFICATION |
| `VAL-TST-014` | Which sensitive fixture classes require additional review? | NEEDS VERIFICATION |
| `VAL-TST-015` | What artifact retention policy applies to validator reports? | NEEDS VERIFICATION |
| `VAL-TST-016` | Which validator checks, if any, are required by current rulesets? | NEEDS VERIFICATION |
| `VAL-TST-017` | Which release gates consume validator outcomes? | UNKNOWN |
| `VAL-TST-018` | Is every compatibility surface documented with an exit condition? | NEEDS VERIFICATION |
| `VAL-TST-019` | What migration window protects current imports and commands? | NEEDS VERIFICATION |
| `VAL-TST-020` | Have correction and rollback drills been executed? | UNKNOWN |

## What passing does not prove

Passing any command or workflow named here does not prove:

- complete validator discovery or complete test collection;
- semantic correctness of schemas or contracts;
- source identity, authority, admissibility, or activation;
- rights, sovereignty, privacy, or sensitivity clearance;
- evidence adequacy or EvidenceBundle closure;
- policy approval or obligation completion;
- human review, separation of duties, or merge legitimacy;
- lifecycle promotion;
- release, deployment, publication, or public-use permission;
- production parity;
- correction or rollback execution.

Evidence outranks generated language, and validation remains one bounded gate in
the trust spine.

## Lineage and rollback

Version v0.13 accumulated valuable test-family guidance and historical
implementation notes, but its manually maintained inventory no longer described
the current tree or orchestrator. Git history preserves that material at prior
blob `beda059555042c7b256b6ee93b288f40a9a8d37f`.

To roll back this documentation change before merge, close the draft pull
request. After merge, revert the documentation commit through a reviewed pull
request. Do not reset shared history or revert tests, validators, fixtures,
registry entries, workflows, or Make targets merely to restore old prose.

[Back to top](#top)

