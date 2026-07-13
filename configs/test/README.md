<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-test-readme
title: configs/test/ — Commit-Safe Test Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Test steward · QA steward · Security steward · Consumer owner(s) · Validation steward · CI steward · Docs steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public; config-sublane; test-configuration; commit-safe; non-secret; no-network-default; no-side-effect-default; non-authoritative; no-test-proof; no-ci-authority; no-release-authority
current_path: configs/test/README.md
truth_posture: CONFIRMED repository-present README-only lane at the inspected path search and named conventional probes, parent configs root contract, canonical tests root, tests/fixtures versus root fixtures split, no-secrets doctrine, and v0.1 introduction lineage / PROPOSED test-configuration contract, runner-binding metadata, marker and selection guardrails, environment isolation defaults, validation matrix, review workflow, and minimum safe test-config slice / UNKNOWN exhaustive recursive inventory, differently named config files, consumers, runner/framework bindings, precedence, auto-discovery, schema bindings, secret scanning, CI enforcement, pass rates, deployment integration, owner assignments, and runtime behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8
  prior_blob: 02023ee483fa245c0c761630dcd0f1c28fc790eb
  introduction_commit: c41b0c45d43220a8964effca50658d7966cb8f44
related:
  - ../README.md
  - ../examples/README.md
  - ../templates/README.md
  - ../local/README.md
  - ../dev/README.md
  - ../domains/README.md
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../fixtures/README.md
  - ../../tools/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/security/SECRETS.md
  - ../../docs/runbooks/SECRET_LEAK_RUNBOOK.md
  - ../../schemas/contracts/v1/
  - ../../contracts/
  - ../../policy/
  - ../../apps/
  - ../../packages/
  - ../../pipelines/
  - ../../pipeline_specs/
  - ../../runtime/
  - ../../infra/
  - ../../artifacts/
  - ../../release/
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, configs, test, testing, runner-config, markers, selection, sharding, deterministic, no-network, no-side-effects, fixtures, placeholders, non-secret, commit-safe, config-validation, consumer-binding, non-authoritative, governance]
notes:
  - "At the pinned base, a path-scoped repository search returned this README but no additional configs/test files. Exact probes for pytest.example.toml, test.template.yaml, validation.md, and ci.example.yaml returned Not Found. These are bounded findings, not an exhaustive recursive tree receipt."
  - "configs/test/ contains configuration-facing documentation and future safe templates only. tests/ remains the canonical enforceability root; fixtures live under tests/fixtures/ or root fixtures/ according to the documented ownership split."
  - "A test config may select, parameterize, or isolate a verified test consumer. It cannot prove collection, execution, coverage, pass state, policy enforcement, release readiness, correction, rollback, or trust-spine closure."
  - "No real secret, live endpoint, production identifier, sensitive geometry, source payload, lifecycle record, proof, receipt, release object, or generated report may be stored here."
  - "Main advanced from b2db8a4f84754c111b28d756cbaac145fa0fcd84 to b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8 before branching. The compare touched configs/examples/README.md and connectors/manual_curation/README.md; this target retained prior blob 02023ee483fa245c0c761630dcd0f1c28fc790eb."
  - "Only this Markdown file changes. No test config, test, fixture, schema, contract, policy, validator, workflow, secret-scanning rule, runner, lifecycle artifact, release object, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Commit-Safe Test Configuration

> `configs/test/` is the test-configuration sublane under `configs/`. It may document or template safe settings for a named test consumer, but it does not create tests, fixtures, validation proof, CI authority, policy enforcement, release readiness, or operational truth.

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Observed lane maturity:** README-only at the inspected repository search and named conventional probes  
> **Owning responsibility root:** `configs/` — safe, non-secret defaults and templates  
> **Authority:** test-configuration documentation only; no test, fixture, schema, policy, CI, lifecycle, proof, release, or publication authority  
> **Default posture:** deterministic · no-network · no-side-effect · fail closed · not proof of execution

> [!CAUTION]
> A test configuration can change which tests run, which tests are skipped, what environment they see, and where they write. Treat it as trust-bearing configuration. Never use it to hide negative tests, weaken fail-closed behavior, inherit real credentials, enable live network access by default, write to governed lifecycle or release roots, or represent a green run that did not occur.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs](#what-belongs-here) · [What does not](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Evidence](#evidence-basis) · [Lane distinctions](#test-configuration-lane-distinctions) · [Config contract](#proposed-test-config-contract) · [Runner binding](#runner-and-consumer-binding) · [Selection](#selection-markers-skips-and-sharding) · [Isolation](#environment-and-isolation-contract) · [Secrets](#secret-sensitive-and-production-value-handling) · [Fixtures](#fixture-and-test-data-boundary) · [Determinism](#time-randomness-and-determinism) · [Network](#network-and-side-effect-posture) · [CI parity](#local-ci-and-matrix-parity) · [Failures](#failure-semantics) · [Naming](#file-format-and-naming-posture) · [Change pattern](#safe-change-pattern) · [Rollback](#rollback-and-correction-posture) · [Backlog](#verification-backlog) · [Done](#definition-of-done)

---

## Purpose

`configs/test/` exists for small, commit-safe configuration templates and configuration-facing notes that support a **named, verified test consumer**.

A useful test config explains:

- which test runner, harness, package, domain lane, validator, or CI job it is intended to support;
- whether the file is illustrative, a safe default, or an explicitly loaded operational test config;
- which runner and consumer versions the settings target;
- how tests are discovered, selected, marked, sharded, timed, retried, isolated, and reported;
- which environment variables are allowed and which are forbidden;
- which fixture roots and temporary storage locations may be read or written;
- whether network access, subprocesses, clocks, randomness, GPUs, browsers, containers, or external services are permitted;
- how a maintainer validates syntax, known keys, selection completeness, and consumer compatibility;
- which settings are `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.

This lane should make test execution safer and more reproducible. It must not make an unverified test run look authoritative.

[Back to top](#top)

---

## Authority level

**Configuration sublane / non-authoritative test settings.**

| Concern | Authority status | Determination |
|---|---:|---|
| Folder placement | **CONFIRMED** | The path exists under `configs/`, whose parent README identifies that root as the home for safe non-secret defaults and templates. |
| Test authority | **NONE** | Executable tests and enforceability proof belong under `tests/`. |
| Fixture authority | **NONE** | Unit-test-scoped fixtures belong under `tests/fixtures/`; cross-cutting fixtures belong under root `fixtures/` according to the documented split. |
| Current inventory | **BOUNDED README-ONLY FINDING** | Search returned this README only; common candidate filenames were absent at named probes. Differently named or unindexed files remain `UNKNOWN`. |
| Runner behavior | **UNKNOWN** | No runner, config loader, auto-discovery rule, import path, precedence order, or supported command is established by this README. |
| Validation | **PROPOSED / NEEDS VERIFICATION** | This README defines expected checks; executable bindings were not established in the inspected evidence. |
| CI enforcement | **UNKNOWN** | Workflow success, collection, coverage, pass rate, and matrix completeness require workflow and log evidence. |
| Secret safety | **CONFIRMED DOCTRINE / ENFORCEMENT UNKNOWN** | Real secrets are forbidden in the repository; automated secret-scanning coverage remains `NEEDS VERIFICATION`. |
| Production/release use | **NOT AUTHORIZED** | Test configuration cannot activate a source, mutate governed data, approve release, or establish public readiness. |

A test config can point to an authority surface. It cannot become that authority surface.

[Back to top](#top)

---

## Status

### Bounded repository snapshot

At base commit `b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8`, the directly verified lane is:

```text
configs/test/
└── README.md
```

A path-scoped repository search returned no additional file in this lane. Exact probes returned `Not Found` for:

```text
configs/test/pytest.example.toml
configs/test/test.template.yaml
configs/test/validation.md
configs/test/ci.example.yaml
```

These are bounded absence statements for named paths and indexed search results—not a recursive filesystem receipt. Differently named files, ignored files, generated files, branch-only work, or unindexed content remain `UNKNOWN`.

### Current maturity

| Capability | Status | Safe conclusion |
|---|---:|---|
| README boundary | **CONFIRMED** | The lane has documentation. |
| Test configuration files | **NOT ESTABLISHED** | No actual test-config payload was verified in the inspected lane. |
| Named consumers | **NOT ESTABLISHED** | No runner, harness, package, domain suite, validator, or workflow was bound here. |
| Auto-discovery and precedence | **NOT ESTABLISHED** | Do not infer that any runner reads this directory automatically. |
| Test collection | **NOT ESTABLISHED** | No collected-test count or zero-test guard is proven here. |
| Marker/selection behavior | **NOT ESTABLISHED** | No marker registry, skip policy, shard plan, or selection completeness proof was verified. |
| Fixture binding | **NOT ESTABLISHED** | Fixture homes are documented elsewhere; no config-to-fixture binding was proven. |
| Environment isolation | **NOT ESTABLISHED** | No environment allowlist, temp-root policy, clock, locale, timezone, or seed binding was verified. |
| Network/side-effect blocking | **NOT ESTABLISHED** | No executable guard was verified from this lane. |
| Secret scanning | **NEEDS VERIFICATION** | Doctrine forbids secrets; automation coverage was not established by the inspected evidence. |
| Test/CI enforcement | **NEEDS VERIFICATION** | No lane-specific executable check or passing proof was verified. |
| Ownership | **OWNER_TBD** | `CODEOWNERS` has no verified `configs/test/`-specific mapping. |

### What this README does not establish

This document does not prove:

- that a test framework is installed;
- that a supported command exists;
- that tests collect;
- that any suite passes;
- that negative or trust-spine tests run;
- that configured markers are registered;
- that skips or expected failures are reviewed;
- that shards cover the complete suite;
- that fixtures exist;
- that network or writes are blocked;
- that test environments exclude real secrets;
- that local and CI behavior match;
- that coverage thresholds are meaningful;
- that release or promotion gates consume the result.

[Back to top](#top)

---

## What belongs here

This lane may contain only test-configuration templates, safe defaults, and tightly coupled explanatory notes that remain subordinate to the actual tests and their consumers.

| Accepted material | Purpose | Required posture |
|---|---|---|
| `*.example.toml` | Illustrate TOML settings for a named runner or tool. | Parseable; runner/version named; not auto-loaded unless explicitly verified. |
| `*.example.yaml` / `*.example.yml` | Illustrate test profile, matrix, environment, or validation settings. | Parseable; consumer identified; no workflow or policy authority. |
| `*.example.json` | Strict machine-readable test settings. | Valid JSON; schema reference or `NEEDS VERIFICATION`. |
| `.env.test.example` or equivalent | Document allowed test variable names and obvious mock/reference values. | No real values; explicit allowlist; never inherited production secrets. |
| Marker/selection template | Document intended marker names and inclusion/exclusion behavior. | Must not suppress trust-spine or negative tests silently. |
| Matrix/shard example | Show proposed dimensions or shard ownership. | Completeness and merge semantics documented; no CI authority. |
| `README.md` | Lane contract, inventory, review guidance, and evidence boundary. | Truth-labeled and current. |
| `validation.md` | Human validation instructions. | Commands verified or labeled `PROPOSED`; no false pass claims. |
| `MIGRATION.md` | Temporary key/path compatibility guidance. | Review-linked, reversible, and sunset-dated. |
| Small public-safe config snippets | Explain one test-setting concern. | Synthetic, non-secret, no sensitive identifiers or source data. |

Each non-trivial file should make its consumer, scope, replacement requirements, isolation posture, and expected failure behavior inspectable without guessing.

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Executable test code | Configuration is not enforceability proof. | `tests/` in the owning lane. |
| `conftest.py`, helper modules, plugins, or test utilities | These are executable test implementation. | `tests/`, package test helpers, or accepted implementation home. |
| Unit-test-scoped fixture payloads | Config cannot become fixture authority. | `tests/fixtures/`. |
| Cross-cutting reusable fixture corpora | Shared fixtures need explicit ownership. | Root `fixtures/`. |
| Real source exports, production snapshots, logs, dumps, traces | These may contain rights-, privacy-, security-, or sensitivity-bearing material. | Governed data/quarantine or synthetic fixture generation. |
| Real secrets, credentials, cookies, signed URLs, private endpoints | Repository is not a secret store. | External secret manager; rotate and invoke leak response if committed. |
| Production or staging configuration copied for tests | Creates accidental live binding and data leakage. | Build clean synthetic test settings from the accepted field surface. |
| Schemas | Config cannot own machine shape. | `schemas/`. |
| Contracts | Config cannot own semantic meaning. | `contracts/`. |
| Policy rules or policy decisions | Config cannot authorize allow/deny/restrict/abstain behavior. | `policy/`. |
| Validators and repo-wide checks | These are executable tooling. | `tools/` or accepted validator home. |
| Test workflow definitions | GitHub Actions and other CI definitions are operational automation. | `.github/workflows/` or accepted CI root. |
| App/package/pipeline/runtime code | Test settings cannot become implementation. | `apps/`, `packages/`, `pipelines/`, or `runtime/`. |
| Deployment/network/access-control definitions | Test config cannot own infrastructure exposure. | `infra/`. |
| Lifecycle records or governed data | Tests must not write into canonical lifecycle stores. | `data/` through governed workflows; use temp/synthetic data for tests. |
| EvidenceBundles, receipts, proofs, registry rows, catalog/triplet records | Test carriers are not operational trust objects. | Their owning `data/` or `control_plane/` homes. |
| Release manifests, promotion decisions, corrections, rollback cards | Tests may exercise synthetic shapes but cannot create release state. | `release/` for real objects; fixtures for synthetic examples. |
| Generated reports, coverage output, screenshots, logs, junit XML | These are run artifacts. | `artifacts/` or ephemeral CI storage. |
| Worked testing walkthroughs | Narrative assemblies are not config defaults. | Root `examples/` when useful. |
| Sensitive exact locations, living-person data, genomic data, private parcel joins, infrastructure-sensitive detail | Unnecessary and potentially harmful in test config. | Use synthetic/generalized fixtures, quarantine, restrict, or deny. |

A test configuration lane must not become a quiet parallel home for test code, fixtures, policy, secrets, lifecycle data, evidence, or release state.

[Back to top](#top)

---

## Inputs

### Current input

The current lane consumes documentation and repository evidence only. No test-config payload or supported loading interface is established by the inspected repository evidence.

### Future admissible inputs

A proposed test configuration may be authored from:

- a verified test runner or harness interface;
- a verified package, app, pipeline, validator, or domain-suite test entrypoint;
- accepted test markers, labels, suites, or selection rules;
- a machine schema for the configuration surface;
- a semantic contract or runner documentation describing setting meaning;
- a reviewed fixture-home decision;
- a reviewed CI matrix or shard contract;
- safe local defaults derived from existing tests;
- a migration from an older setting, command, marker, or file path;
- a minimal synthetic use case needed to reproduce a test environment.

Do not derive a test config by copying a production configuration and replacing a few values. Build it from the accepted test-facing field surface with synthetic values and explicit denials.

### Required preconditions for a future file

Before adding a test config, identify:

```text
consumer
consumer version or commit
load mechanism
auto-discovery status
precedence/merge behavior
test scope
fixture roots
network posture
side-effect posture
environment-variable allowlist
time/randomness controls
validation command
owner
review date
sunset/migration posture
```

Unknown items must remain explicit. A filename must not be used to imply a binding that has not been verified.

[Back to top](#top)

---

## Outputs

### Current output

This README emits documentation only.

It does not emit:

- a loaded test configuration;
- collected tests;
- a test plan;
- a test result;
- coverage;
- a validation report;
- a fixture;
- a CI check;
- an EvidenceBundle;
- a receipt or proof;
- a release decision;
- a lifecycle transition;
- a public artifact.

### Future bounded outputs

A future config file may be consumed to produce an in-memory runner configuration or a test invocation plan, provided the verified consumer owns that behavior.

Acceptable downstream results may include:

- parsed configuration;
- resolved safe defaults;
- selected test identifiers;
- marker expressions;
- shard assignments;
- deterministic environment settings;
- temp-directory settings;
- fixture-root references;
- timeout/resource settings;
- reporting format choices;
- syntax or compatibility validation results.

Those results remain runner/test inputs. They are not pass evidence until tests actually execute and logs/results are inspected.

### Forbidden outputs

A test config must not directly:

- modify repository files;
- write to `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/receipts/`, or `data/published/`;
- create or alter source authority;
- approve or promote a release;
- publish a map, API response, story, report, or layer;
- upload artifacts;
- mutate cloud, database, queue, registry, or external service state;
- expose credentials or private endpoints;
- claim test success.

[Back to top](#top)

---

## Validation

Validation should be layered. A parseable file can still select the wrong tests, enable unsafe effects, or point at an unsupported consumer.

### Validation matrix

| Layer | Check | Failure posture |
|---|---|---|
| Text/encoding | UTF-8, no hidden control characters, final newline. | Reject. |
| Format syntax | Parse TOML/YAML/JSON/INI/env syntax with the actual parser where possible. | Reject. |
| Schema | Validate against the accepted configuration schema when one exists. | Reject; do not silently accept unknown shape. |
| Known keys | Reject unknown, misspelled, removed, or deprecated keys unless the consumer explicitly supports them. | Reject or emit reviewed migration warning. |
| Consumer binding | Consumer and version/commit exist and recognize the config surface. | Hold / `NEEDS VERIFICATION`. |
| Load path | Explicitly prove whether the file is auto-discovered or passed by command/argument. | Abstain from behavior claim. |
| Precedence | Document merge/override order and duplicate-key behavior. | Reject ambiguity for trust-bearing settings. |
| Collection | Verify selected tests collect and non-empty collection is enforced. | Fail if zero tests are unexpectedly collected. |
| Selection | Confirm markers, path filters, ignores, and expressions include required negative/trust-spine tests. | Reject silent exclusions. |
| Skip/xfail | Review reason, owner, issue, expiry, and strictness. | Reject unowned or indefinite suppression. |
| Sharding | Prove shard union covers intended set and duplicates/omissions are visible. | Fail incomplete matrix. |
| Fixtures | Fixture roots resolve and follow the `tests/fixtures/` versus `fixtures/` split. | Reject ambiguous or missing fixture ownership. |
| Secrets | Detect real credentials, private keys, tokens, cookies, signed URLs, private endpoints, and copied production values. | Block and invoke leak response when real. |
| Sensitive material | Detect real personal, genomic, exact-location, infrastructure-sensitive, proprietary, or source-restricted identifiers. | Quarantine/reject. |
| Environment | Allowlist inherited variables; isolate HOME, cache, temp, locale, timezone, and paths. | Reject uncontrolled inheritance. |
| Network | No-network by default; explicitly separated integration lanes only. | Deny unexpected network. |
| Side effects | Writes limited to disposable temp/output paths; no canonical stores or external mutation. | Deny and clean up. |
| Determinism | Fix/record seed, time, locale, timezone, ordering, and concurrency where material. | Mark nondeterministic / fail reproducibility gate. |
| Resource bounds | Timeouts, memory, process, file-size, archive, GPU, browser, and retry limits where relevant. | Fail boundedly. |
| CI parity | Local and CI load the same reviewed profile or document intentional differences. | Hold until divergence is understood. |
| Documentation | Consumer, owner, validation, review, and rollback links resolve. | Reject incomplete trust-bearing config. |

### Required negative checks

A mature lane should prove rejection of:

- malformed syntax;
- unknown or removed keys;
- missing consumer/version metadata;
- unsupported auto-discovery assumptions;
- zero-test collection;
- unregistered markers;
- blanket ignores or skips;
- non-strict expected failures for trust-bearing tests;
- incomplete shards;
- fixture paths outside accepted homes;
- inherited real credentials;
- live production endpoints;
- unrestricted network;
- writes to repository, lifecycle, proof, receipt, release, or publication roots;
- uncontrolled clock/randomness;
- invalid timeout/resource values;
- sensitive or proprietary content;
- config that disables fail-closed tests.

### Documentation-only validation performed for this revision

This README revision can validate Markdown structure and repository evidence. It cannot validate absent test-config payloads or runner behavior.

Performed:

- one H1;
- required folder-README sections present and ordered;
- internal quick-link targets resolved;
- balanced fenced blocks;
- no stale rollback placeholder;
- no secret-like value;
- current target and prior blob verified;
- bounded named-path absence checks;
- one-file branch comparison and remote read-back.

Not performed:

- runner installation or import;
- config parsing;
- test collection;
- test execution;
- coverage;
- marker validation;
- shard completeness;
- fixture loading;
- network/side-effect guards;
- secret-scanner execution;
- CI parity;
- release or promotion-gate integration.

[Back to top](#top)

---

## Review burden

### Required reviewers by change type

| Change | Required review posture |
|---|---|
| Documentation-only clarification | Config/QA/docs review. |
| New runner or framework binding | Test steward + owning consumer + dependency/security review. |
| Marker, ignore, selection, or skip change | Test steward + affected domain/component owner; trust-spine impact review. |
| Shard or matrix change | CI steward + test steward; completeness proof. |
| Environment variable or secret-reference change | Security + consumer owner; no-secret and least-privilege review. |
| Network enablement | Security + test steward + owner of the integration lane; explicit isolation. |
| Filesystem/database/cloud side-effect change | Security/ops + test steward; cleanup and deny-by-default review. |
| Fixture-root change | Test + fixture steward; preserve fixture-home split. |
| Time/randomness/concurrency change | Test steward; determinism and flake analysis. |
| Timeout/retry/resource-limit change | Test/CI owner; avoid masking hangs or unsafe load. |
| Coverage threshold change | Test steward + component/domain owner; no metric gaming. |
| Config precedence or auto-discovery change | Architecture/config/test owners; compatibility and migration review. |
| Test config used by promotion/release gate | Separation-of-duties review; executable proof and rollback required. |

### Review questions

Reviewers should ask:

1. Which verified consumer reads this file?
2. How is the file loaded?
3. Could the file silently change collection, selection, skips, xfails, shards, or coverage?
4. Are trust-spine and negative tests still included?
5. Are all values synthetic, non-secret, and public-safe?
6. Is network disabled by default?
7. Are writes confined to disposable locations?
8. Are time, randomness, locale, timezone, concurrency, and ordering controlled?
9. Do fixture references use the accepted home?
10. Does local execution match CI, or is divergence explicit?
11. Are errors fail-closed and visible?
12. Can the change be rolled back without rewriting history?

### CODEOWNERS posture

The current `CODEOWNERS` file provides a general maintainer fallback but no verified `configs/test/`-specific owner. Ownership remains `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Related folders

| Path | Relationship | Boundary |
|---|---|---|
| [`../README.md`](../README.md) | Parent configuration-root contract. | Safe defaults/templates only; no secrets or authority collapse. |
| [`../examples/`](../examples/README.md) | Generic configuration examples. | Not test-specific enforceability. |
| [`../templates/`](../templates/README.md) | Reusable configuration templates. | Templates are not tests or test results. |
| [`../local/`](../local/README.md) | Local configuration notes/templates. | Personal overrides remain uncommitted. |
| [`../dev/`](../dev/README.md) | Development configuration. | Development settings are not necessarily test settings. |
| [`../domains/`](../domains/README.md) | Domain-scoped safe config defaults. | Domain config cannot bypass policy or sensitivity. |
| [`../../tests/`](../../tests/README.md) | Canonical enforceability root. | Tests and results live here/CI, not under configs. |
| [`../../tests/fixtures/`](../../tests/fixtures/README.md) | Unit-test-scoped fixtures. | Test-local inputs; not config authority. |
| [`../../fixtures/`](../../fixtures/README.md) | Cross-cutting reusable fixtures. | Shared synthetic corpora; not test config. |
| `../../tools/` | Validators and repo-wide checks. | Executable tooling, not configuration examples. |
| `../../schemas/` | Machine shape. | Config may reference; never duplicate. |
| `../../contracts/` | Semantic meaning. | Config may reference; never replace. |
| `../../policy/` | Allow/deny/restrict/abstain rules. | Test config cannot weaken policy. |
| `../../artifacts/` | Generated reports and test outputs. | Never store generated results in configs. |
| `../../release/` | Promotion, release, correction, rollback. | Test config cannot approve release. |
| `../../.github/workflows/` | CI orchestration. | Workflow definitions and permissions do not belong here. |

### Root boundary summary

```text
configs/test/       test settings and templates
tests/              executable enforceability proof
tests/fixtures/     test-local synthetic inputs
fixtures/           cross-cutting reusable synthetic inputs
tools/              validators and test tooling
.github/workflows/  CI orchestration
artifacts/          generated reports/results
release/            real promotion/release/correction/rollback authority
```

[Back to top](#top)

---

## ADRs

No ADR is enacted by this README.

An ADR or explicit per-root decision may be required before:

- making `configs/test/` an auto-discovered operational config root;
- introducing a universal test-config envelope across runners;
- changing canonical test or fixture homes;
- making configuration decide promotion or release gates;
- centralizing marker, skip, xfail, shard, or coverage policy across unrelated suites;
- permitting live network, credentials, or external mutation in a default test profile;
- creating a parallel schema, policy, test, fixture, report, or CI authority;
- changing lifecycle boundaries or allowing tests to write governed stores.

### Decision threshold

A lane-local naming or documentation convention may be resolved by test/config stewards. A cross-cutting behavior that changes multiple runners, CI, promotion gates, authority homes, or core invariants requires wider architecture review and potentially an ADR.

[Back to top](#top)

---

## Last reviewed

**Last reviewed:** 2026-07-13  
**Evidence base:** `main@b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8`  
**Prior target blob:** `02023ee483fa245c0c761630dcd0f1c28fc790eb`  
**Review scope:** target README, parent configs root, canonical tests root, fixture-home docs, secrets doctrine, path search, named candidate probes, CODEOWNERS, and recent base movement  
**Not reviewed as implementation proof:** recursive tree, runner manifests, imports, config loaders, test files, fixture payloads, workflow logic, logs, pass rates, coverage, release integration, deployment, or ownership acceptance

Refresh this section whenever an actual test config, consumer, marker registry, fixture binding, validation tool, CI check, or owner is added.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `configs/test/README.md` | **CONFIRMED** | Existing target and v0.1 boundary. | Any test config payload or runtime behavior. |
| Introduction commit `c41b0c45...` | **CONFIRMED** | Lineage from three-line stub to v0.1. | Current maturity or accepted behavior. |
| `configs/README.md` | **CONFIRMED** | `configs/` owns safe non-secret defaults/templates. | Current child inventory, consumers, or validation. |
| `tests/README.md` | **CONFIRMED** | `tests/` is the canonical enforceability root and documents trust-spine expectations. | That any particular runner or suite currently passes. |
| `tests/fixtures/README.md` | **CONFIRMED DOC** | Test-local fixture posture and no-network/synthetic expectations. | Fixture payload completeness or consumer tests. |
| `fixtures/README.md` | **CONFIRMED DOC** | Cross-cutting fixture root and split from test-local fixtures. | Complete payload inventory or executable bindings. |
| `docs/security/SECRETS.md` | **CONFIRMED DOC** | No real secrets in repository, including test/local material. | Automated secret scanning or operational rotation. |
| Path-scoped search | **CONFIRMED SEARCH** | Returned this README and no additional indexed lane files. | Exhaustive recursive absence. |
| Named file probes | **CONFIRMED ABSENCE AT PATHS** | Four common candidate files returned `Not Found`. | Absence of differently named files. |
| `.github/CODEOWNERS` | **CONFIRMED** | General fallback ownership exists. | Accepted lane-specific owners. |
| Current branch comparison | **CONFIRMED** | This revision can remain one-file scoped. | Runtime correctness. |

### Evidence conflicts and limits

- README doctrine is richer than verified implementation.
- The tests root describes required test classes but explicitly bounds runner/CI/pass-rate claims.
- Fixture READMEs describe ownership and safety but do not prove payloads or test consumption.
- Repository search is not a recursive tree receipt.
- A green generic workflow may be a placeholder and does not prove test-config enforcement.
- No config payload exists in the inspected lane to parse or execute.

[Back to top](#top)

---

## Test-configuration lane distinctions

| Lane or artifact | Intended role | Why it is different |
|---|---|---|
| `configs/test/` | Safe settings/templates for named test consumers. | Configures tests; does not implement or prove them. |
| `configs/examples/` | Generic configuration examples. | May target any consumer, not specifically tests. |
| `configs/templates/` | Reusable template shapes. | May remain abstract rather than test-executable. |
| `configs/dev/` | Development defaults. | Developer convenience may differ from test isolation. |
| `configs/local/` | Local setup notes/templates. | Personal overrides should remain uncommitted. |
| `tests/` | Executable enforceability proof. | Owns test code and trust-spine assertions. |
| `tests/fixtures/` | Test-local fixtures. | Inputs owned by particular tests. |
| `fixtures/` | Cross-cutting reusable fixtures. | Shared corpora across tests/pipelines/runtime checks. |
| `.github/workflows/` | CI orchestration. | Owns runner jobs, permissions, matrices, and workflow triggers. |
| `tools/` | Validators/helpers. | Executable checks, not config documentation. |
| `artifacts/` | Generated results. | JUnit, coverage, logs, reports, screenshots, and build output. |
| root `examples/` | Walkthroughs and teaching assemblies. | Narrative/non-authoritative demonstrations. |
| `pipeline_specs/` | Durable declarative pipeline intent. | Not a test runner profile. |
| `infra/` | Deployment/network/access controls. | Real exposure and host binding. |
| external secret store | Real credential values. | Repository contains only names/placeholders. |

### Operational-config warning

Some test frameworks auto-discover files such as root-level project configuration, package-local config, or plugin modules. An auto-discovered operational file may belong beside the verified consumer rather than in `configs/test/`.

Before placing an operational file here, prove that:

- the runner can load it from this path;
- the invocation explicitly points to it or accepted auto-discovery reaches it;
- precedence is documented;
- local and CI commands agree;
- no parallel operational config already owns the same settings.

Otherwise retain a clearly named `.example` or `.template` file and document the intended migration.

[Back to top](#top)

---

## Proposed test-config contract

The following metadata is **PROPOSED** for future test-config files. It is guidance, not a schema.

```yaml
kfm_test_config:
  example: true
  authority: non_authoritative_test_configuration
  do_not_publish: true

  config_id: "example:test-config:<consumer>:<profile>"
  config_version: "0.1.0"

  consumer:
    name: "<runner-or-harness>"
    repository_path: "<verified-path>"
    version_or_commit: "<version-or-sha>"
    load_method: "<explicit-argument|environment|auto-discovery|unknown>"
    precedence: "<documented-order-or-needs-verification>"

  scope:
    suite_paths: ["<test-path>"]
    markers: ["<marker>"]
    exclusions: []
    expected_collection_minimum: 1
    trust_spine_required: true
    negative_tests_required: true

  isolation:
    network: disabled
    side_effects: temp_only
    inherited_environment: allowlist
    timezone: UTC
    locale: C.UTF-8
    random_seed: 0
    clock: controlled_or_recorded

  fixtures:
    roots: ["tests/fixtures/<lane>"]
    cross_cutting_roots: []
    real_source_data: forbidden

  resources:
    timeout_seconds: 60
    retries: 0
    max_workers: 1

  validation:
    syntax: "<verified-command-or-needs-verification>"
    known_keys: "<verified-command-or-needs-verification>"
    collection: "<verified-command-or-needs-verification>"
    secret_scan: "<verified-command-or-needs-verification>"

  governance:
    owner: "OWNER_TBD"
    reviewed_at: "NEEDS_VERIFICATION"
    migration_ref: null
    sunset_at: null
```

### Contract rules

1. `example: true` must remain visible for non-operational examples.
2. The consumer must be concrete and verified.
3. `load_method` and precedence must not be guessed.
4. Expected collection must make accidental zero-test runs visible.
5. Trust-spine and negative tests must not be silently excluded.
6. Network and side effects default to denied.
7. Fixtures must use accepted homes.
8. Values must be synthetic and non-secret.
9. Validation commands must be executable evidence or labeled `NEEDS VERIFICATION`.
10. Governance metadata must name an owner before operational adoption.

[Back to top](#top)

---

## Runner and consumer binding

### Required binding evidence

A future test config should link to:

- runner/framework dependency declaration;
- consumer package/app/pipeline/domain test path;
- supported version or commit;
- invocation command;
- config load path;
- plugin/extension dependencies;
- marker registration;
- fixture roots;
- CI workflow/job when applicable;
- expected collected-test range;
- relevant schema or key registry;
- owner and review cadence.

### Auto-discovery posture

Do not assume a runner searches `configs/test/`.

Use one of these explicit postures:

| Posture | Meaning |
|---|---|
| `example_only` | Documentation; never loaded automatically. |
| `explicit_argument` | Runner command passes the path. |
| `environment_selected` | A safe environment variable selects the path. |
| `generated_copy` | A reviewed tool renders/copies the example into a consumer-owned location. |
| `auto_discovered` | Verified runner behavior finds the file without an explicit path. |
| `unknown` | No behavior claim allowed. |

### Precedence posture

When multiple config sources exist, document:

```text
built-in defaults
-> project/package operational config
-> configs/test profile (if explicitly loaded)
-> environment allowlist
-> command-line overrides
```

This sequence is illustrative. The actual consumer order must be verified. Ambiguous precedence can hide tests or weaken isolation and should fail closed for trust-bearing settings.

[Back to top](#top)

---

## Selection, markers, skips, and sharding

Test selection is consequential. A config can turn a broad suite into an empty or misleading green run.

### Selection guardrails

- Register marker names in the verified consumer.
- Fail on unknown markers where the runner supports strict marker validation.
- Keep inclusion and exclusion expressions reviewable.
- Do not use broad ignore paths to hide failing trust-spine tests.
- Require non-empty collection unless the profile explicitly documents a no-tests-expected state.
- Record expected collection ranges when stable.
- Keep negative, denial, abstention, correction, and rollback cases in required profiles.
- Make platform- or dependency-specific exclusions explicit and bounded.
- Do not let a “fast” profile become the only promotion evidence.

### Skip and expected-failure discipline

Every consequential skip or expected failure should carry:

```text
reason
owner
issue or backlog reference
introduced date
expiry/review date
strictness
affected trust-spine stage
```

Disallowed patterns include:

- blanket directory skips;
- unowned permanent skips;
- expected failures that pass unexpectedly without failing the run;
- configuration-only suppression of security, policy, evidence, release, or rollback tests;
- skip reasons that reveal secrets or sensitive details.

### Shard/matrix completeness

For sharded or matrix runs:

- assign stable shard identity;
- prove union coverage of the intended suite;
- detect duplicate and omitted tests;
- merge results before claiming pass;
- preserve failed/cancelled/skipped shard state;
- keep platform and feature dimensions explicit;
- do not drop a shard because no tests were collected without review;
- retain a deterministic reproduction command per failed shard.

[Back to top](#top)

---

## Environment and isolation contract

Test configuration should make environment inheritance explicit and minimal.

### Environment allowlist

Prefer an allowlist such as:

```text
PATH
HOME=<disposable-test-home>
TMPDIR=<disposable-test-temp>
TZ=UTC
LC_ALL=C.UTF-8
LANG=C.UTF-8
KFM_TEST_PROFILE=<non-secret-profile-name>
```

This is illustrative. Actual variables must be consumer-verified.

Deny or sanitize by default:

- cloud credentials;
- source API keys;
- signing keys;
- database URLs;
- production service URLs;
- proxy credentials;
- deployment tokens;
- personal home paths;
- user-specific config directories;
- editor/session variables that affect behavior;
- credentials inherited from the operator shell.

### Filesystem isolation

Tests should:

- use disposable temp roots;
- avoid the operator home directory;
- avoid shared mutable caches unless isolated by run ID;
- avoid repository writes unless the test explicitly uses a disposable checkout;
- never write canonical `data/`, `release/`, proof, receipt, registry, or published roots;
- clean up bounded resources;
- preserve failing temp artifacts only through an intentional artifact-copy step.

### Process isolation

Document whether tests may:

- start subprocesses;
- spawn browsers;
- start containers;
- access GPUs;
- bind ports;
- use local databases;
- run model runtimes;
- invoke shell commands.

Anything not required should be denied. Allowed processes need timeout, cleanup, port, and resource limits.

[Back to top](#top)

---

## Secret, sensitive, and production-value handling

### No-secret rule

The repository is not a secret store. This applies to material labeled `test`, `mock`, `example`, or `local`.

Allowed:

```yaml
api_key_ref: "${TEST_SOURCE_API_KEY}"
token: "MOCK_TOKEN_NOT_VALID"
private_key_path: "<external-test-secret-reference>"
endpoint: "https://example.invalid"
```

Forbidden:

```yaml
api_key: "<real-value>"
cookie: "<captured-session>"
signed_url: "<live-url>"
database_url: "<production-connection>"
private_endpoint: "<internal-host>"
```

### Test credential posture

When a test genuinely requires credentials:

- place it in a separately gated integration lane;
- use least-privilege ephemeral credentials;
- keep values outside the repository;
- bind credentials only to the job requiring them;
- redact commands, logs, errors, snapshots, and reports;
- verify revocation and rotation paths;
- never expose them to fork/untrusted contexts;
- do not make credentialed tests the default local profile.

### Sensitive data posture

Test config must not embed:

- names or identifiers of living people;
- DNA/genomic identifiers;
- private parcel/operator links;
- rare-species or archaeological exact locations;
- infrastructure-sensitive endpoints or topology;
- proprietary source identifiers or terms;
- restricted source paths;
- reconstructive redaction clues.

Use synthetic IDs, generalized geometry, public-safe fixtures, denied states, or quarantine-oriented negative tests.

### Leak response

If a real secret or protected value is committed:

1. stop using it;
2. revoke/rotate it;
3. assess logs, caches, artifacts, and forks;
4. remove it through transparent correction;
5. invoke the accepted secret-leak/incident process;
6. add regression coverage;
7. do not rely on history rewriting as the only response.

[Back to top](#top)

---

## Fixture and test-data boundary

Test config may reference fixture roots; it must not duplicate fixture payloads.

### Fixture-home split

| Home | Use |
|---|---|
| `tests/fixtures/` | Unit-test-scoped fixtures owned by a particular test area. |
| `fixtures/` | Cross-cutting reusable fixtures shared across tests, pipelines, runtime checks, or documentation. |

A config should identify:

```text
fixture root
fixture owner
fixture version/hash when stable
expected outcome
public-safety posture
network posture
generation recipe or source note
```

### Test-data guardrails

- Prefer synthetic, compact, deterministic, public-safe fixtures.
- Never point default tests at live lifecycle stores.
- Never use production snapshots merely because they are convenient.
- Do not treat a fixture as source truth, policy approval, evidence closure, or release state.
- Keep valid, invalid, denied, abstention, correction, and rollback cases distinguishable.
- Pair stable input fixtures with expected outputs where practical.
- Verify fixture paths do not escape through traversal, symlinks, or environment substitution.
- Bound archive extraction, file count, file size, and expansion ratio where relevant.

[Back to top](#top)

---

## Time, randomness, and determinism

A test configuration should control or record nondeterminism.

### Time controls

Where material:

- fix or inject the current time;
- use UTC;
- test daylight-saving and timezone boundaries explicitly;
- separate source, observed, valid, retrieval, release, and correction times;
- avoid wall-clock sleeps as synchronization;
- bound retries and backoff;
- record clock mode in results.

### Randomness controls

- set a stable seed for reproducible profiles;
- record randomized/property-test seeds on failure;
- avoid global shared random state;
- keep fuzz/property-test budgets explicit;
- make failure reproduction commands visible;
- do not hide flaky behavior with retries alone.

### Ordering and concurrency

- define stable ordering where assertions depend on it;
- distinguish deterministic single-worker profiles from concurrency tests;
- record worker count and shard ID;
- detect race-dependent state leakage;
- isolate shared caches and temp paths;
- repeat concurrency-sensitive tests only as an explicit diagnostic profile.

A deterministic test config does not prove the code is deterministic; it makes the claimed test conditions inspectable.

[Back to top](#top)

---

## Network and side-effect posture

### Default profile

```text
network: denied
external services: denied
cloud mutation: denied
database mutation: disposable/local only
filesystem writes: disposable temp only
repository mutation: denied
lifecycle/release writes: denied
subprocesses: denied unless required
```

### Integration profiles

A separately reviewed integration profile may permit bounded access when it defines:

- allowed hosts;
- protocol and TLS posture;
- credential source;
- rate limits;
- timeouts;
- retries;
- expected data volume;
- write prohibition or disposable target;
- cleanup;
- failure and cancellation handling;
- redaction;
- fork/untrusted-context behavior;
- owner and review date.

### No bypass by configuration

A test config must not:

- point tests at production services;
- disable certificate verification;
- allow arbitrary hosts;
- use broad proxy inheritance;
- bypass governed APIs to read internal stores;
- write to source systems;
- publish artifacts;
- promote lifecycle state;
- invoke model runtimes with real data;
- turn failures into warnings for convenience.

[Back to top](#top)

---

## Local, CI, and matrix parity

### Parity requirement

A local profile and its CI counterpart should either:

1. load the same reviewed config; or
2. document every intentional difference.

Differences to make visible:

- test paths;
- markers;
- ignored directories;
- environment variables;
- plugins;
- worker count;
- shard/matrix dimensions;
- timeouts;
- retries;
- network policy;
- fixture roots;
- coverage settings;
- report formats;
- platform-specific skips;
- secret availability.

### Green-run interpretation

A green CI status is not sufficient evidence when:

- the workflow only echoes placeholder text;
- no tests were collected;
- a required shard was skipped;
- negative/trust-spine tests were excluded;
- errors were converted to warnings;
- coverage omitted changed code;
- artifacts/results were not merged;
- the job ran against a different ref/config than claimed.

### Coverage posture

Coverage is a diagnostic, not truth.

- Do not lower thresholds through an example config without review.
- Do not exclude trust-bearing code to improve a metric.
- Keep branch/condition coverage where it matters.
- Separate unit coverage from trust-spine/e2e proof.
- Record untested risk rather than smoothing it into a percentage.
- A high percentage does not replace negative, policy, evidence, release, or rollback tests.

[Back to top](#top)

---

## Failure semantics

A future validator/consumer should fail deterministically and without leaking sensitive details.

### Proposed configuration outcomes

| Outcome | Meaning | Safe response |
|---|---|---|
| `CONFIG_VALID` | Syntax and accepted binding checks pass. | Permit test invocation; do not claim test pass. |
| `CONFIG_INVALID` | Syntax/schema/key/value failure. | Reject. |
| `CONSUMER_UNKNOWN` | Consumer or version cannot be resolved. | Hold / `NEEDS VERIFICATION`. |
| `LOAD_PATH_UNKNOWN` | Auto-discovery or explicit load behavior is unverified. | Abstain from runtime claim. |
| `UNKNOWN_KEY` | Consumer does not recognize a setting. | Reject unless reviewed compatibility mode applies. |
| `ZERO_TESTS_UNEXPECTED` | Selection collects no tests unexpectedly. | Fail. |
| `SELECTION_INCOMPLETE` | Required trust-spine/negative tests are excluded. | Fail. |
| `MARKER_UNREGISTERED` | Selection uses an unregistered marker. | Fail. |
| `SHARD_INCOMPLETE` | Matrix union does not cover intended tests. | Fail. |
| `FIXTURE_MISSING` | Required fixture or expected output does not resolve. | Fail. |
| `SECRET_DETECTED` | Real or likely credential value appears. | Block; initiate leak review. |
| `SENSITIVE_VALUE_DETECTED` | Protected real-world detail appears. | Quarantine/reject. |
| `NETWORK_FORBIDDEN` | Default profile attempts external network. | Deny. |
| `SIDE_EFFECT_FORBIDDEN` | Test attempts prohibited write/mutation. | Deny and clean up. |
| `VERSION_MISMATCH` | Config targets unsupported consumer version. | Reject/hold for migration. |
| `NONDETERMINISTIC` | Conditions cannot reproduce or seed/time is missing where required. | Mark failure/flake; preserve reproduction evidence. |
| `CANCELLED` | Operator/CI cancellation. | Clean up; do not convert to pass. |
| `RATE_LIMITED` | Bounded integration target throttles. | Stop/retry within policy; do not hide. |
| `ERROR` | Unexpected internal failure. | Fail safely with redacted diagnostics. |

These names are **PROPOSED**, not an accepted KFM-wide enum.

### Diagnostic safety

Errors may include:

- config path;
- field name;
- reason code;
- consumer/version;
- test profile;
- shard ID;
- redacted host class;
- remediation link.

Errors must not include:

- secret values;
- authorization headers;
- cookies;
- full private URLs;
- sensitive fixture content;
- production connection strings;
- unredacted environment dumps.

[Back to top](#top)

---

## File-format and naming posture

No naming convention is accepted by this README. Prefer names that make status and consumer visible.

### Proposed patterns

```text
<consumer>.<profile>.example.toml
<consumer>.<profile>.example.yaml
<consumer>.<profile>.template.json
<consumer>.<profile>.validation.md
.env.test.example
```

Examples:

```text
pytest.unit.example.toml
validator-suite.no-network.example.yaml
governed-api.integration.template.json
```

These are illustrative only.

### Naming rules

- Include `.example` or `.template` for non-operational files.
- Do not name a file as though it is automatically loaded unless verified.
- Avoid `prod`, `production`, or real environment names.
- Do not embed secrets or identifiers in filenames.
- Keep consumer/profile names stable and lowercase where practical.
- Use migration notes when renaming a consumed file.
- Record deprecation and sunset dates for old names.
- Do not create a new child directory until ownership and consumer justify it.

### Format rules

- JSON remains strict JSON.
- YAML should avoid unsafe/custom object constructors.
- TOML should parse with the consumer-supported implementation.
- Environment examples use names plus obvious mock/reference values only.
- Comments explain intent, not secrets or sensitive source details.
- Duplicate keys should be rejected where the parser permits ambiguity.
- Encoding is UTF-8.

[Back to top](#top)

---

## Safe change pattern

### Add or revise a test config

1. Confirm `configs/test/` is the correct lane.
2. Pin the current base and target blob.
3. Search for existing operational configs and competing PRs.
4. Identify the exact consumer, version, load path, and precedence.
5. Decide whether the file is example-only or operationally loaded.
6. Confirm tests remain under `tests/`.
7. Confirm fixtures remain in accepted fixture homes.
8. Build settings from the test-facing field surface—not production config.
9. Use only synthetic values, placeholders, and references-by-name.
10. Default network and side effects to denied.
11. Make collection, markers, skips, xfails, shards, and expected minimums explicit.
12. Control/record time, randomness, locale, timezone, concurrency, and resources.
13. Parse and validate against the actual consumer.
14. Run collection and negative safety checks.
15. Compare local and CI behavior.
16. Update owner, review, migration, and rollback notes.
17. Keep the diff scoped and reversible.
18. Do not claim pass until tests and logs prove it.

### Move an operational config

A path move requires:

- consumer and workflow updates;
- precedence and auto-discovery analysis;
- compatibility/redirect plan if applicable;
- tests proving old/new behavior;
- rollback target;
- migration documentation;
- owner review;
- ADR consideration if authority or cross-cutting architecture changes.

[Back to top](#top)

---

## Anti-patterns

Reject these patterns:

- “The config exists, so the test is enforced.”
- Auto-discovery assumed from filename.
- An example file named like a live operational config.
- Test config copied from production.
- Real credentials in “test” values.
- Default live network access.
- Writes to repository, lifecycle, proof, receipt, release, or published roots.
- A fast profile that omits negative/trust-spine tests but is used for promotion.
- Zero tests collected with exit success.
- Unknown markers treated as warnings.
- Blanket ignore/skip patterns.
- Permanent unowned `xfail`.
- Retries used to hide nondeterminism.
- Coverage exclusions used to improve percentages.
- Shards whose union is not checked.
- Local and CI profiles silently diverging.
- Fixture payloads embedded in config.
- Sensitive identifiers or exact locations in parameters.
- Test config that weakens policy, redaction, geoprivacy, evidence, or release gates.
- A green TODO-only workflow presented as proof.
- Generated reports committed into `configs/`.
- Silent history rewriting after a leaked secret.

[Back to top](#top)

---

## Rollback and correction posture

### Documentation rollback

Restore prior blob:

```text
02023ee483fa245c0c761630dcd0f1c28fc790eb
```

or revert the documentation commit through reviewed history.

### Future config rollback

For an operationally consumed test config:

1. disable the new profile at the consumer/workflow boundary if it causes unsafe selection or effects;
2. preserve failing logs and redacted diagnostics;
3. restore the last reviewed config and invocation;
4. rerun collection and required safety tests;
5. verify negative/trust-spine coverage;
6. verify no real credentials, external mutations, or governed-store writes occurred;
7. publish a correction/migration note when maintainers could have relied on misleading results;
8. do not force-push shared history.

### Rollback triggers

Rollback or disable a test config when it:

- collects zero tests unexpectedly;
- excludes required negative or trust-spine tests;
- introduces unknown markers or unowned skips;
- leaves a shard uncovered;
- enables live network or external mutation without approval;
- inherits real credentials;
- points at production/staging services;
- writes governed stores or repository state;
- leaks sensitive values in logs/artifacts;
- changes precedence unexpectedly;
- makes local and CI results materially diverge;
- converts failures to warnings;
- claims validation/test success without execution evidence.

### Correction discipline

Documentation errors should be fixed by transparent commits. A misleading green run should be corrected in the PR/release record that relied on it. A leaked credential requires revocation and incident response, not only a text edit.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Evidence needed |
|---|---:|---|
| Produce recursive `configs/test/` inventory | **NEEDS VERIFICATION** | Tree receipt pinned to commit. |
| Confirm whether lane should remain README-only | **OPEN** | Config/test steward decision. |
| Assign owners and CODEOWNERS coverage | **NEEDS VERIFICATION** | Accepted ownership mapping. |
| Identify supported runners/frameworks | **UNKNOWN** | Dependency/manifests and test entrypoints. |
| Identify actual consumers | **UNKNOWN** | Code, commands, workflows, and tests. |
| Document load path and auto-discovery | **UNKNOWN** | Runner behavior and invocation proof. |
| Document precedence and overrides | **UNKNOWN** | Consumer code/docs and compatibility tests. |
| Freeze example/template/operational naming | **PROPOSED** | Per-root convention and migration plan. |
| Bind config to schema/key registry | **NEEDS VERIFICATION** | Accepted schema and validator. |
| Add syntax validation | **PROPOSED** | Parser-based tests/tooling. |
| Add known-key/deprecation validation | **PROPOSED** | Consumer-aware validator. |
| Add zero-test collection guard | **PROPOSED** | Runner config/test and CI log. |
| Register markers strictly | **NEEDS VERIFICATION** | Marker registry and negative tests. |
| Audit skips and xfails | **NEEDS VERIFICATION** | Inventory, owners, issues, expiries. |
| Prove shard/matrix completeness | **NEEDS VERIFICATION** | Collected test manifest and union check. |
| Verify fixture-root bindings | **NEEDS VERIFICATION** | Config refs and consumer tests. |
| Verify environment allowlist | **NEEDS VERIFICATION** | Harness code and negative tests. |
| Verify time/randomness controls | **NEEDS VERIFICATION** | Config, tests, reproduction logs. |
| Verify no-network enforcement | **NEEDS VERIFICATION** | Blocking harness and failing fixture. |
| Verify side-effect isolation | **NEEDS VERIFICATION** | Temp-root and denied-write tests. |
| Verify secret scanning | **NEEDS VERIFICATION** | Tool/workflow config and safe positive/negative fixtures. |
| Verify sensitive-value scanning/review | **NEEDS VERIFICATION** | Policy/review checks. |
| Verify local/CI parity | **NEEDS VERIFICATION** | Commands, config digests, and logs. |
| Verify substantive docs/link checks | **NEEDS VERIFICATION** | Real workflow rather than placeholder echo. |
| Define generated report/artifact routing | **NEEDS VERIFICATION** | Workflow and `artifacts/` contract. |
| Define migration/sunset rules | **PROPOSED** | Maintainer policy and tests. |
| Confirm secret-leak runbook operational readiness | **NEEDS VERIFICATION** | Runbook inspection and drill evidence. |
| Prove promotion/release gate use, if any | **UNKNOWN** | Gate configs, tests, logs, review records. |

[Back to top](#top)

---

## Definition of done

This lane may advance beyond README-only draft when:

- [ ] a commit-pinned recursive inventory exists;
- [ ] owners and CODEOWNERS coverage are assigned;
- [ ] supported runners/frameworks and versions are documented;
- [ ] every config names a verified consumer and test scope;
- [ ] every config documents load method and precedence;
- [ ] example-only files are visibly distinct from operational files;
- [ ] test code remains under `tests/`;
- [ ] fixture references obey the `tests/fixtures/` versus `fixtures/` split;
- [ ] syntax parsing is automated for every supported format;
- [ ] schema/known-key/deprecation validation is wired where applicable;
- [ ] zero-test collection fails unexpectedly empty profiles;
- [ ] markers are registered and unknown markers fail;
- [ ] skips/xfails have owners, reasons, issues, and review/expiry dates;
- [ ] required negative, denial, abstention, correction, rollback, and trust-spine tests cannot be silently excluded;
- [ ] shard/matrix union completeness is proven;
- [ ] all values are synthetic, non-secret, and public-safe;
- [ ] inherited environment is allowlisted;
- [ ] default test profiles are no-network and no-side-effect;
- [ ] writes are confined to disposable paths;
- [ ] no canonical lifecycle, proof, receipt, release, registry, or published root is mutated;
- [ ] time, randomness, locale, timezone, concurrency, ordering, and resource bounds are controlled or recorded;
- [ ] credentialed integration tests are separately gated and redacted;
- [ ] local and CI profiles match or intentional differences are documented;
- [ ] CI jobs prove actual collection/execution rather than placeholder success;
- [ ] generated reports route to ephemeral storage or `artifacts/`, not `configs/`;
- [ ] rollback and secret-leak response are documented and tested;
- [ ] stale configs have migration and sunset paths;
- [ ] this README is refreshed from resulting evidence.

A safe test config makes execution conditions inspectable. It is not the test, the test result, the policy decision, the proof, or the release gate.

[Back to top](#top)
