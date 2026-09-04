<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-test-readme
title: configs/test/ — Commit-Safe Test Configuration Boundary
type: readme
version: v0.4.0
prior_version: v0.3
status: repository-grounded; draft; boundary-compact; readme-only; non-authoritative
owner: "@bartytime4life — CODEOWNERS review route only; accountable test/config stewardship and independent review NEEDS VERIFICATION"
created: 2026-06-16
updated: 2026-09-04
policy_label: public-review; non-secret; no-network-default; no-side-effect-default; non-publisher
current_path: configs/test/README.md
owning_root: configs/
responsibility: explain shared test-configuration placement, verified lane inventory, consumer binding, isolation, validation limits, and correction without owning tests, fixtures, policy, CI, or release
truth_posture: CONFIRMED tracked README-only lane and inspected repository declarations; PROPOSED future consumer-bound profiles; UNKNOWN operational consumption and enforcement; NEEDS VERIFICATION fixture-placement resolution and independent stewardship
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
evidence_prior_blob: 087b4241ba3020f084d4d19dccde7cdbd22880dc
evidence_directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
evidence_adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
evidence_pyproject_blob: cbfc1af273f125caca0c2eea055af1ad39baf2b8
evidence_test_local_fixture_readme_blob: 157baec3725bcc23376c7b6135242d05bb1a18d0
related:
  - ../README.md
  - ../../pyproject.toml
  - ../../tests/README.md
  - ../../tests/fixtures/README.md
  - ../../fixtures/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/link-check.yml
  - ../../.github/workflows/docs-meta-block.yml
  - ../../.github/workflows/docs-stale-scan.yml
  - ../../CONTRIBUTING.md
  - ../../data/receipts/generated/README.md
tags: [kfm, configs, test, consumer-binding, deterministic, synthetic, no-network, non-secret, documentation]
notes:
  - "Current GitHub direct-child inspection closes the tracked lane inventory: README.md only, no child directories or configuration payloads."
  - "The root Python manifest declares pytest and Hypothesis; declaration is not installation, execution, or configs/test consumption."
  - "The previous unconditional tests/fixtures placement split is corrected to the current documented local-support exception and unresolved placement conflict."
  - "Existing headings remain navigation surfaces; future profile fields and outcomes remain proposals, not a new runner schema or policy."
  - "No configuration payload, test, fixture, workflow, dependency, authority decision, or runtime behavior changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Commit-Safe Test Configuration

**Shared test settings belong here only when a named consumer needs them. Tests,
fixtures, and test results do not.** Start with the [configuration parent](../README.md),
the [test-root guide](../../tests/README.md), or the
[existing Python project configuration](../../pyproject.toml), depending on the task.

> [!IMPORTANT]
> **Current lane: README only.** At the evidence commit below, `configs/test/`
> contains no tracked configuration payload or child directory. This README does
> not install a runner, select tests, load a profile, block network access, or prove
> a passing run. No operational profile is activated by this update.

> [!WARNING]
> **Fixture placement is not an unconditional two-home rule.** Root `fixtures/`
> owns reusable fixtures. The existing `tests/fixtures/` guide describes bounded
> local support with an unresolved placement conflict. Preserve existing consumer
> bindings; do not use this README to authorize another reusable fixture home.

**Navigate:** [Snapshot](#status) · [Placement](#authority-level) ·
[Consumer binding](#runner-and-consumer-binding) · [Selection](#selection-markers-skips-and-sharding) ·
[Isolation](#environment-and-isolation-contract) · [Validation](#validation) ·
[Fixture boundary](#fixture-and-test-data-boundary) · [Rollback](#rollback-and-correction-posture) ·
[Open verification](#verification-backlog)

## Purpose

Make test execution conditions inspectable without confusing configuration with
execution evidence. A useful shared profile identifies its consumer and version,
load method, precedence, test scope, selection rules, fixtures, environment,
resources, validation, owner, and rollback. A one-consumer configuration normally
stays with that consumer; central placement is not a goal by itself.

## Authority level

This is a compact boundary under canonical `configs/`, not a separate authority
root. [Accepted ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../docs/doctrine/directory-rules.md).
Section 10.4 makes configuration follow its consumer unless genuinely shared;
section 16 governs README inheritance and verified direct-child maps.

Configuration may select already-defined behavior. It cannot redefine semantic
contracts, machine schemas, policy, source authority, evidence, review, release,
public access, or the lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Public clients use governed APIs and released artifacts, never this directory as
a data or evidence interface. EvidenceRef-to-EvidenceBundle resolution remains
upstream of interpretive maps, indexes, reports, and AI. Promotion is a governed
transition, not a configuration toggle, passing test, file move, or merge.

## Status

### Bounded repository snapshot

Evidence base: `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`.
Prior README blob: `087b4241ba3020f084d4d19dccde7cdbd22880dc`.
The complete direct-child listing contains one file and no subdirectories:

```text
configs/test/
└── README.md  # authored boundary guidance; not a loaded test profile
```

This also closes the tracked recursive inventory for this lane. It does not
inspect ignored, untracked, externally stored, or other-branch material.

### Current maturity

| Surface | Evidence-bounded result |
|---|---|
| Shared test-config payload in this lane | **CONFIRMED / ABSENT** at the pinned tree |
| README | **CONFIRMED / DRAFT**; authored documentation, not a generated mirror |
| Python runner declarations | **CONFIRMED**: root `pyproject.toml` declares Python `>=3.11`, test extras `pytest>=9.1.1,<10` and `hypothesis>=6.138.0,<7` |
| Root pytest configuration | **CONFIRMED**: `[tool.pytest.ini_options]` contains `pythonpath = ["."]`; no lane selection is declared in that table |
| Installed/resolved runner versions | **UNKNOWN**; dependency ranges are not installation evidence |
| Consumer, loader, precedence, or semantic validator for this lane | **NEEDS VERIFICATION**; no operational binding established by this review |
| Default no-network and temporary-write posture | Required design boundary; executable enforcement **NOT INSPECTED** |
| Review route | `/configs/` routes to `@bartytime4life`; approval and independent stewardship remain separate |

### What this README does not establish

No collected-test count, complete suite, marker/skip audit, shard coverage,
fixture consumption, sandbox enforcement, coverage percentage, secret-scanning
coverage, required-check coupling, runtime parity, or release readiness is proved
here. The declarations above do not imply that a runner discovers `configs/test/`.

## What belongs here

Only small, non-secret, genuinely shared test defaults/templates and directly
related guidance for a verified consumer. Clearly mark examples and templates
as non-operational. A future file needs a concrete use, not directory symmetry.

Possible formats include TOML, YAML, JSON, and environment examples, subject to
the consumer's parser and supported keys. Marker/selection and matrix/shard
examples remain configuration inputs, not global testing policy or workflow
implementation. Local validation or migration notes need an actual owned change;
none are added by this revision.

## What does NOT belong here

| Material | Owning responsibility or handling |
|---|---|
| Executable tests, `conftest.py`, plugins, helpers | `tests/` or an already verified consumer-owned implementation lane |
| Reusable fixture payloads | Root `fixtures/`; existing test-local support follows the unresolved boundary below |
| Schemas / semantic contracts / admissibility rules | `schemas/` / `contracts/` / `policy/`; no copied authority here |
| PolicyDecision instances | The governed process or release-object lane they record, not automatically beside policy source |
| Validators / CI jobs / deployment controls | `tools/` / `.github/workflows/` / `infra/` |
| App, package, pipeline, runtime code or pipeline specifications | Their corresponding responsibility roots; not disguised as configuration |
| Domain data, registry rows, EvidenceBundles, receipts, proofs, catalog/triplet records | Governed object-family homes; synthetic test shapes remain fixtures |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard | `release/` for real decision objects; never test-profile authority |
| Coverage, JUnit XML, logs, screenshots, generated reports | Disposable test or CI storage; `artifacts/` only under its existing scoped compatibility rules |
| Real credentials, production/staging snapshots, sensitive identifiers or source exports | Do not commit; use synthetic/minimized inputs and approved restricted handling |

A test configuration is not a shortcut into any lifecycle, release, proof,
fixture, schema, registry, policy, or public-delivery home.

## Inputs

### Current input

Pinned repository files and directory listings inform this documentation. The
lane has no operational configuration input at the evidence base.

### Future admissible inputs

Use the verified runner/harness interface, dependency declaration, test entrypoint,
accepted field semantics, consumer schema where present, reviewed selection rules,
and fixture references. Build synthetic settings from that interface; do not
copy a production config and replace a few values.

### Required preconditions for a future file

Record consumer/version, explicit load path or proven discovery, precedence and
duplicate-key handling, selected suite, fixture ownership, environment allowlist,
network/write limits, deterministic conditions, resource budget, validation,
accountable owner, review trigger, and migration/rollback reference. Missing
safety-critical bindings block operational use, not truthful example authoring.

## Outputs

### Current output

Human-readable guidance only. The separately required generated-work receipt
records authorship provenance, not test execution or approval.

### Future bounded outputs

A verified consumer may turn a profile into parsed settings, selected test IDs,
marker expressions, shard assignments, fixture references, resource limits, or
an invocation plan. Those are test inputs until actual execution and results
establish an outcome.

### Forbidden outputs

Do not let a profile authorize writes to real repository/lifecycle stores,
source systems, cloud services, registries, or release/publication objects. Use
disposable substitutes for tests. Artifact upload and durable receipt emission
are separate, reviewed producer responsibilities, not effects granted by a flag.

## Validation

### Validation matrix

| Layer | Required evidence before claiming the behavior |
|---|---|
| Syntax and shape | Actual parser, accepted schema when present, valid types, duplicate/unknown-key handling |
| Binding and precedence | Exact consumer/version, loader/invocation, override order, unsupported-version rejection |
| Collection and selection | Intended test IDs, nonempty expected collection, preserved negative/trust-boundary cases |
| Markers, skips, expected failures | Registered names, reasons, owner, issue, review/expiry and strict unexpected-pass behavior where supported |
| Shards and local/CI parity | Intended union, visible duplicates/omissions, all required shard outcomes and documented environment differences |
| Fixtures and isolation | Approved fixture ownership, path containment, disposable writes, environment allowlist and denied unintended effects |
| Secrets and sensitivity | Synthetic/minimized values, redacted diagnostics, separately gated credentialed integration |
| Determinism and resources | Controlled/recorded clock, seed, locale, ordering, concurrency, timeout, retry, memory/process/browser/GPU budgets |
| Documentation and provenance | Resolving navigation, exact revision, artifact hashes, honest performed/not-run results and rollback |

### Required negative checks

Before a future profile is used as assurance evidence, demonstrate rejection of
malformed/duplicate/unknown keys, unsupported consumers, unexpected empty
collection, unknown markers, hidden critical exclusions, unowned suppression,
incomplete shards, missing/escaping fixtures, real credential inheritance,
production endpoints, unexpected network, prohibited writes, unsafe resource
limits, and lost determinism. A parse-only pass does not close these checks.

### Documentation-only validation performed for this revision

Current reads verified the lane inventory, parent boundary, accepted placement
rule, runner declarations, fixture-placement disclosure, review route, and the
three documentation workflow definitions. Changed-area checks and their exact
outcomes belong in the branch/PR handoff and generated-work receipt, not an
unqualified evergreen claim that this README passes all repository checks.

The workflow coverage distinction remains important:

| Workflow | Definition inspected at this revision | Limit |
|---|---|---|
| `link-check` | Checks local Markdown targets in changed Markdown files | Definition covers this README; hosted result is a separate observation; external URLs are not requested |
| `docs-meta-block` | Markdown trigger; validation roots are `README.md docs tools/validators/docs` | `configs/` remains outside those explicit roots |
| `docs-stale-scan` | Markdown trigger; same explicit validation roots | Same coverage gap; advisory freshness is not correctness |

No workflow is edited here. No local runner installation, test collection,
semantic test-config validation, full suite, browser, network-isolation probe,
release drill, or hosted check is claimed merely from this documentation update.
The v0.3 validation record and its warning counts remain historical, not rerun results.

## Review burden

### Required reviewers by change type

Documentation needs config/test/docs review. Consumer or dependency binding adds
its implementation owner. Selection, skips, expected failures, shards, and
coverage changes need affected test owners and completeness review. Environment,
network, credentials, processes, or writes need security/operations review.
Fixture placement needs fixture/test owners; cross-cutting authority or
release-gate changes require the corresponding separate decision and review.

### Review questions

Can the reviewer identify the consumer, loader and override order, actual selected
tests, negative cases, fixture owner, safe environment, allowed effects,
reproduction command, CI differences, and rollback? Are missing evidence and
unexpected outcomes visible rather than converted into a green status?

### CODEOWNERS posture

[CODEOWNERS](../../.github/CODEOWNERS) confirms review routing only. Do not infer
accepted stewardship, independent approval, required-review enforcement, or
separation of duties from the named account.

## Related folders

| Start here | Purpose |
|---|---|
| [Parent configuration guide](../README.md) | Shared defaults, consumer-first placement, secret boundary |
| [Python project configuration](../../pyproject.toml) | Existing Python dependency and pytest declarations |
| [Test root](../../tests/README.md) | Executable conformance and bounded suite guidance |
| [Reusable fixtures](../../fixtures/README.md) | Canonical reusable synthetic inputs and expected outputs |
| [Existing test-local support](../../tests/fixtures/README.md) | Placement conflict and current support-lane guidance |
| [Contributor contract](../../CONTRIBUTING.md) | Branch delivery, evidence, review, and generated-work provenance |
| [Generated-work receipts](../../data/receipts/generated/README.md) | Authorship process memory, not approval |

### Root boundary summary

Configuration selects; tests assert; fixtures supply synthetic cases; tools
validate; workflows orchestrate; receipts record; proofs support; release records
authorize governed transitions. No carrier replaces the authority it references.

## ADRs

ADR-0029 supplies placement authority; this same-path update does not change an
accepted decision, root class, fixture home, schema, policy, or runtime contract.

### Decision threshold

A justified shared example does not require inventing a new architecture. A new
universal config envelope, automatic discovery root, canonical fixture migration,
cross-runner selection policy, release-gate authority, or relaxation of network,
credential, or lifecycle boundaries does require the applicable explicit decision
and migration/rollback evidence. This README accepts none of those changes.

## Last reviewed

Reviewed 2026-09-04 against `bb3eb695e6068b38453ca3ded8f1394a8fdebc20`.
Scope: complete target, direct-child inventory, parent and fixture guidance,
Python manifest, adopted placement authority, contributor requirements,
CODEOWNERS, and documentation workflow definitions.

Re-review when a profile, loader, dependency, fixture binding, selection rule,
owner, validation boundary, or exposure changes. No operational consumer,
installed dependency, complete test suite, or deployment was validated here.

## Evidence basis

| Evidence at the base commit | What it supports |
|---|---|
| `configs/test/` complete listing and prior blob `087b4241ba3020f084d4d19dccde7cdbd22880dc` | One tracked README; no payload or deeper tree |
| `configs/README.md`, blob `a800983eac7582a84e9dd82bc7d4baf04f552ad8` | Inherited canonical configuration boundary |
| Directory Rules, blob `fd49a0b83e55cef52c1124281f093e263526898d`; ADR-0029, blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Adopted consumer-first placement and README profile |
| `pyproject.toml`, blob `cbfc1af273f125caca0c2eea055af1ad39baf2b8` | Declared Python/pytest/Hypothesis surface, not installed versions |
| `tests/fixtures/README.md`, blob `157baec3725bcc23376c7b6135242d05bb1a18d0` | Explicit unresolved local-support placement conflict |
| `fixtures/README.md`, blob `fce9ef8422077e10e82325d5b50333df2628d6bc` | Reusable fixture root guidance |
| CODEOWNERS, blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | Review route |
| `link-check.yml`, blob `7b6c675d879a36d685b19b18fde401fca1bdd00e` | Bounded changed-Markdown link-check definition |
| `docs-meta-block.yml`, blob `732879cd8a5aca71ef3c570a0c34c4c389f20e8a` | Explicit validation roots and metadata coverage gap |
| `docs-stale-scan.yml`, blob `5a94d7c353c4c18c0bcb9a0df45c81a3916f747a` | Explicit validation roots and freshness coverage gap |

### Evidence conflicts and limits

The earlier README's unconditional `tests/fixtures/` versus `fixtures/` split is
not adequate current placement guidance. The current child guide explicitly
records a conflict; this update discloses it without moving files or deciding
its resolution. The earlier unknown runner list is narrowed to inspected Python
declarations, not promoted to installed or passing capability. A bounded code
search is discovery evidence, not proof of zero dynamic or external consumers.

Drive's *Directory Rules* is lineage; adopted repository bytes and ADR-0029
control current placement. Coordination notes, old receipts, historical SHAs,
workflow titles, and prior passes cannot replace fresh exact-revision evidence.

## Test-configuration lane distinctions

`configs/test/` is shared test configuration; generic examples/templates,
development defaults, local override guidance, and domain knobs remain in their
existing `configs/` lanes. Test code, reusable fixtures, pipeline specifications,
infrastructure, generated results, and secrets retain their separate homes.

### Operational-config warning

Do not relocate an existing project/package config merely to populate this lane.
Prove consumer load support, precedence, local/CI parity, and no competing writer
before centralizing. Documentation-only examples must remain visibly inert.

## Proposed test-config contract

The v0.3 `kfm_test_config` envelope remains **PROPOSED**, not a supported runner
format, accepted schema, or new policy. Its useful review fields are retained:

| Field group | Review information, not executable keys |
|---|---|
| Identity/status | `config_id`, `config_version`, `example`, `authority`, `do_not_publish` |
| Consumer | Name, repository path, version/commit, load method, precedence |
| Scope | Suite paths, registered markers, exclusions, expected collection, required negative/trust-boundary cases |
| Isolation | Network/writes, environment allowlist, timezone/locale, seed, clock |
| Fixtures | Approved roots, owner, content identity, expected outcome, real-source-data prohibition |
| Resources | Timeout, retry budget, workers and other justified limits |
| Validation/governance | Parser, known-key and collection checks, secret-safety checks, owner, review, migration, sunset |

No sample timeout, seed, worker count, or minimum test count is made a universal
KFM setting. Do not paste this field map into pytest or another runner as config.

### Contract rules

A real implementation must bind these concerns to the actual consumer's supported
format. Keep examples labeled, reject unsupported safety-relevant values, preserve
negative cases, and block operational use when consumer, ownership, fixture
placement, or effect boundaries cannot be established.

## Runner and consumer binding

### Required binding evidence

The root manifest is an inspected declaration surface, not a universal runner
contract. Before adding a file here, identify its consumer entrypoint, dependency
version, plugins, accepted keys, invocation, expected selected tests, fixtures,
workflow/job where applicable, and owner. Record resolved versions when executed.

### Auto-discovery posture

Use an explicit description: `example_only`, `explicit_argument`,
`environment_selected`, `generated_copy`, `auto_discovered`, or `unknown`.
These are retained descriptive proposals, not machine enums. Only the consumer's
verified loader can establish discovery; a directory name cannot.

### Precedence posture

Record actual built-in, project/package, shared-profile, environment, and CLI
ordering. The prior schematic ordering was illustrative, not a pytest guarantee.
Include duplicate-key and override rejection tests for consequential settings.

## Selection, markers, skips, and sharding

### Selection guardrails

Keep selection inspectable and expected collection nonempty unless a reviewed
profile explicitly expects no tests. Preserve denial, abstention, correction,
rollback, security, policy, and evidence-boundary cases. Register markers and
reject unknown markers where supported. A fast subset is not full assurance.
The inspected root pytest table alone does not establish these controls.

### Skip and expected-failure discipline

Consequential skips/xfails need a reason, owner, issue, introduction/review date,
expiry where applicable, strictness, and affected boundary. Do not hide tests with
blanket ignores, permanent unowned skips, or unexpected-pass suppression. Keep
sensitive details out of reasons.

### Shard/matrix completeness

Retain stable shard IDs and the intended collected-test set. Prove the union,
report duplicates/omissions, preserve failed/cancelled/skipped shards, merge
results before claiming completeness, and provide a reproduction command per
failure. An empty shard is a reviewed outcome, not an automatic success.

## Environment and isolation contract

### Environment allowlist

Allow only variables required by the verified consumer. Use disposable HOME,
cache, and temporary locations; control locale/timezone when material. Do not
inherit cloud credentials, signing keys, database URLs, proxies, deployment
tokens, personal config, or production endpoints from an operator's shell.
`KFM_NO_NETWORK` or a similar flag is a declaration, not a network sandbox.

### Filesystem isolation

Use disposable paths or a disposable checkout for tests that modify files. Do not
write real governed stores. Check traversal, symlinks and substituted paths;
isolate caches by run, clean up bounded resources, and retain failures only through
an intentional redacted artifact step. This does not prohibit the separate,
reviewed authorship receipt accompanying a repository change.

### Process isolation

Subprocesses, shells, browsers, containers, GPUs, ports, local databases and model
runtimes require explicit necessity, resource limits and cancellation cleanup.
An allowed local process is not permission to contact external services or use
real sensitive inputs.

## Secret, sensitive, and production-value handling

### No-secret rule

`test`, `mock`, `local`, and `.example` never make real values safe to commit.
Use obvious mock values and names of approved external references. Even an
`example.invalid` endpoint is only an illustrative string; attempting to resolve
it would still be network activity. Avoid executable network examples by default.

### Test credential posture

Credentialed integration is separately gated: least-privilege short-lived values,
job-specific injection, redacted commands/results, revocation/rotation, and no
exposure to untrusted/fork execution. It is not the default local profile.

### Sensitive data posture

Use synthetic identifiers and generalized geometry. Exclude living-person/DNA
information, private-land joins, protected archaeology/rare-species locations,
restricted source identifiers, infrastructure-sensitive topology and clues that
reconstruct redacted data. Unclear rights or sensitivity means quarantine,
restriction, generalization, or denial, not a convenient real-world fixture.

### Leak response

Stop use, invoke the repository's incident process, arrange authorized revocation
and rotation, assess logs/artifacts/caches and other copies, correct transparently,
and add safe regressions. Deleting a string or rewriting history alone does not
revoke a credential. This README authorizes no credential administration.

## Fixture and test-data boundary

### Fixture-home split

| Home | Current documented interpretation |
|---|---|
| Root `fixtures/` | Canonical reusable synthetic, valid, invalid and golden inputs/expected outputs |
| Existing `tests/fixtures/` | Bounded test-local support with **unresolved placement conformance**, not an independently accepted reusable-fixture authority |

The [test-local fixture guide](../../tests/fixtures/README.md) records the conflict
between current support material and the tests-root prohibition on `test_fixture`
artifacts. Keep it explicit. Preserve existing bindings pending reviewed
resolution; do not create new competing fixture collections or bulk-move by name.

### Test-data guardrails

Reference fixture owner, version/hash where stable, expected outcome, synthetic
and rights posture, and generation/source note. Keep positive, invalid, denied,
abstained, corrected and rollback cases distinct. Never point default tests at
live lifecycle stores or copy production snapshots. Bound archive expansion,
file count/size, traversal, symlinks and environment substitution.

## Time, randomness, and determinism

### Time controls

Control or record clocks; use explicit timezones and test timezone/daylight-saving
edges where relevant. Keep source, observed, valid, retrieval, release and
correction times distinct. Avoid sleeps as synchronization; bound retries/backoff.

### Randomness controls

Record stable or failing randomized/property-test seeds, isolate random state,
and set explicit fuzz budgets. Preserve reproduction instructions. Retries do not
turn a flaky result into deterministic evidence.

### Ordering and concurrency

Control ordering and record workers/shards. Separate deterministic profiles from
concurrency diagnostics, isolate mutable state and caches, and test race/leakage
conditions deliberately. A seed alone does not prove reproducibility.

## Network and side-effect posture

### Default profile

The intended default is no external network or service mutation, no real
repository/lifecycle/release writes, and temporary-only local effects. This is
not verified enforcement. Tests must not gain source admission, publication,
or direct internal-store/model access from their configuration.

### Integration profiles

A reviewed integration profile specifies allowed hosts/protocols, credentials,
TLS, rates, timeout/retry/volume budgets, disposable targets or write denial,
cleanup, cancellation, redaction, untrusted-context behavior, and ownership.
Network-dependent setup is distinct from a no-network test-execution claim.

### No bypass by configuration

Never disable certificate checks, permit arbitrary hosts/proxies, point at live
production services, write source systems, invoke models on real restricted data,
or coerce failures to warnings merely to make a run green.

## Local, CI, and matrix parity

### Parity requirement

Use the same reviewed profile or enumerate differences in dependencies, paths,
markers, exclusions, plugins, environment, fixtures, workers/shards, timeouts,
retries, network, coverage, reports, platform skips and available credentials.
Record the config digest and exact tested revision when asserting parity.

### Green-run interpretation

A TODO-only job, empty collection, skipped required shard, hidden negative tests,
unmerged results, suppressed error, or different tested ref is not the claimed
assurance. Report pass, failure, pending, skipped, cancelled and not-run separately.

### Coverage posture

Coverage is diagnostic. Do not silently lower thresholds or exclude consequential
code to improve a number. Branch/condition coverage, negative cases, end-to-end
proof and untested risks remain distinct; percentages do not grant release.

## Failure semantics

### Proposed configuration outcomes

The following retained names describe candidate diagnostics only; no accepted
KFM-wide enum or runtime implementation is introduced:

| Candidate outcomes | Intended treatment |
|---|---|
| `CONFIG_VALID` | Configuration checks passed; test execution is still separate |
| `CONFIG_INVALID`, `UNKNOWN_KEY`, `VERSION_MISMATCH` | Reject unsupported syntax/keys/values or hold for reviewed migration |
| `CONSUMER_UNKNOWN`, `LOAD_PATH_UNKNOWN` | Hold operational use; do not claim loading behavior |
| `ZERO_TESTS_UNEXPECTED`, `SELECTION_INCOMPLETE`, `MARKER_UNREGISTERED`, `SHARD_INCOMPLETE` | Fail the incomplete or unsupported selection |
| `FIXTURE_MISSING` | Fail missing or invalid fixture binding |
| `SECRET_DETECTED`, `SENSITIVE_VALUE_DETECTED` | Block and route to restricted incident/review handling |
| `NETWORK_FORBIDDEN`, `SIDE_EFFECT_FORBIDDEN` | Deny unintended effects; clean up safely |
| `NONDETERMINISTIC` | Preserve flake/reproduction evidence; do not claim determinism |
| `CANCELLED`, `RATE_LIMITED`, `ERROR` | Keep the finite outcome visible; never convert it to pass |

### Diagnostic safety

Report only safe path/field identifiers, reason, consumer/version, profile/shard,
redacted host class and remediation guidance. Exclude values, credentials,
headers, cookies, private URLs, connection strings, fixture contents and raw
environment dumps. Configuration status is not test, policy, or release status.

## File-format and naming posture

### Proposed patterns

A future example may use `<consumer>.<profile>.example.toml`, an equivalent YAML
example, or a JSON template. An environment example must be unmistakably inert.
These are naming proposals, not existing files or reserved output paths.

### Naming rules

Make consumer, scope and example/operational status visible. Avoid sensitive or
real-environment names. Preserve consumed names or provide migration and sunset
notes. Create children only for an actual owned consumer need.

### Format rules

Use strict JSON, safe YAML parsing without custom constructors, and the
consumer-supported TOML/INI/env parser. Handle duplicate keys explicitly; validate
known keys and value semantics. Use UTF-8 and a final newline. Comments must not
contain sensitive values or substitute for a machine-enforced rule.

## Safe change pattern

### Add or revise a test config

Pin the base and check overlap; identify shared versus consumer-local ownership;
bind the actual parser/loader and precedence; author synthetic defaults; verify
selection, fixtures, environment, effects and resource bounds; run relevant
positive and negative checks; compare local/CI behavior; and record review,
limitations, provenance and rollback. Do not add inert files solely to populate
this lane, and do not claim execution from configuration presence.

### Move an operational config

A move requires consumer/workflow changes, discovery and precedence analysis,
old/new compatibility tests, migration and rollback, and the applicable authority
review. This update moves nothing and does not settle fixture placement.

## Anti-patterns

Reject presence-as-proof, guessed discovery, examples disguised as live profiles,
production-derived settings, real credentials, unrestricted effects, hidden
negative tests, zero-test success, unknown markers, indefinite suppression,
retry-hidden flakes, coverage gaming, incomplete shards, silent local/CI drift,
embedded fixture payloads, protected detail, authority overrides and TODO-only
green claims. Do not copy generated reports into `configs/` or treat Git history
rewriting as leak remediation.

## Rollback and correction posture

### Documentation rollback

The pre-v0.4.0 target is blob `087b4241ba3020f084d4d19dccde7cdbd22880dc` at the
pinned base. Restore only this file through a reviewed non-force revert or forward
correction. Preserve the generated-work receipt as history, not a binding for new
bytes. Restoring the old file also restores its now-outdated fixture-placement
wording, so review that consequence explicitly.

### Future config rollback

Disable an unsafe profile at its consumer; preserve redacted diagnostics; restore
the last reviewed config/invocation; rerun collection and negative cases; verify
no real credentials, external mutations or governed-store writes occurred; and
correct records that relied on misleading results. Do not rewrite shared history.

### Rollback triggers

Unexpected empty collection, missing critical cases/shards, unsupported markers,
unowned skips, credential inheritance, live targets/effects, leaked values,
precedence surprises, local/CI divergence, suppressed failure or false assurance
requires a bounded disable/correction decision.

### Correction discipline

A README correction is not runtime rollback. A misleading green run needs a
correction in the record that relied on it. A real leak needs incident handling.
None of these actions follows automatically from a documentation commit.

## Verification backlog

| Item | Current boundary and next evidence |
|---|---|
| Tracked inventory | **CONFIRMED**; refresh on any lane-content change |
| Need for a shared profile | **NEEDS VERIFICATION**; identify one real consumer need before adding files |
| Python declarations | **CONFIRMED**; installed/resolved versions and execution remain **UNKNOWN** |
| Consumer/loader/precedence | **NEEDS VERIFICATION**; exact entrypoint and focused binding tests |
| Fixture placement | **NEEDS VERIFICATION**; resolve documented local-support conflict separately; no migration here |
| Collection/selection/skips/shards | **NEEDS VERIFICATION**; actual selected-ID manifest and positive/negative cases |
| Isolation, deterministic conditions and resource limits | **NEEDS VERIFICATION**; harness and denied-effect/reproduction tests |
| Secret/sensitive-value controls | **NEEDS VERIFICATION**; safe scanner fixtures, configuration and review evidence |
| Local/CI and report routing | **NEEDS VERIFICATION**; exact commands, digests, result retention and completeness |
| Documentation workflows | **CONFIRMED** definition-level link coverage; explicit metadata/freshness root gap remains |
| Stewardship and review | Route **CONFIRMED**; accountable assignments and independent review **NEEDS VERIFICATION** |
| Runtime, release-gate use, external consumers and drills | **UNKNOWN / NOT INSPECTED**; separate operational evidence required |

## Definition of done

For this documentation update: keep the stable document identity and navigation,
show the actual README-only tree, distinguish declared runners from lane
consumption, disclose the fixture-placement conflict, verify changed Markdown and
receipt integrity, and report the exact delivery and validation limits.

A future operational profile additionally needs an owned consumer, proven
loading/precedence, approved fixture bindings, parser/key checks, nonempty and
complete selection, reviewed skips/xfails, shard closure, synthetic inputs,
environment/effect isolation, deterministic resource-bounded execution,
credentialed-integration separation, local/CI parity, retained results and
reviewed correction/rollback. No such profile is added or graduated here.

The v0.3 checkpoint, detailed examples, and historical validation remain available
in Git at the prior blob. This revision consolidates repetition, retains the
existing heading navigation and candidate-outcome vocabulary, and corrects the
specific currentness and placement claims rather than accepting a new test policy.

[Back to top](#top)
