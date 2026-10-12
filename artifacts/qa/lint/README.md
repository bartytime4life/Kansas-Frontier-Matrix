<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-lint-readme
title: artifacts/qa/lint/ — Lint, Formatting, Type-Checking, and Static-Inspection Output Boundary
type: readme; directory-readme; qa-output-parent; lint-inspection-index; compatibility-boundary; ci-artifact-contract
version: v0.2
status: draft; repository-grounded; compatibility-root; transitional; mixed-scaffold; readme-tracked; ruff-placeholder-tracked; eslint-placeholder-tracked; markdownlint-placeholder-tracked; mypy-placeholder-tracked; no-substantive-lint-results; root-lint-command-todo-only; precommit-placeholder-present; lint-workflow-not-established; tool-configs-not-established; retention-not-established; release-binding-unestablished; non-authoritative
owners: OWNER_TBD — QA steward · Lint/tooling steward · Python steward · JavaScript/TypeScript steward · Documentation steward · Type-system steward · Security/privacy steward · CI and artifact-retention steward · Receipt/proof steward · Release steward
created: 2026-06-16
updated: 2026-07-16
supersedes: v0.1 bounded lint-output contract
policy_label: public-doc; artifacts; qa; lint; formatting; typecheck; static-inspection; generated-output; inspection-only; no-secrets; no-trust-authority; no-release-authority; correction-aware; rollback-aware
current_path: artifacts/qa/lint/README.md
truth_posture: CONFIRMED target README and prior blob, Directory Rules classification of artifacts as a transitional compatibility root, artifacts/qa QA-output boundary, direct tracked README.md plus PROPOSED empty-result ruff.json plus PROPOSED empty-result eslint.json plus PROPOSED empty-result markdownlint.json plus mypy.txt explicitly stating no type-check run has been recorded, root package lint command remaining TODO-only, root pyproject declaring no Ruff/Mypy lint dependency or root tool profile, pre-commit file explicitly marked a greenfield placeholder with only trailing-whitespace/end-of-file/YAML/JSON/merge-conflict hooks, bounded repository search surfacing no operational Ruff/ESLint/Markdownlint/Mypy producer, checked absence of lane .gitkeep, lint-run.json, lint-summary.json, static-analysis.sarif, root ruff.toml, root mypy.ini, root eslint.config.js, root .markdownlint.json, .github/workflows/lint.yml, and schemas/artifacts/lint-run.schema.json, root gitignore covering direct artifacts/qa/*.xml only and not this nested JSON/TXT lane, and tools/validators/docs remaining a proposed documentation-validator parent rather than proof of executable linting / PROPOSED accepted lint profile registry, explicit source and rule scope, deterministic command envelopes, immutable run manifest, normalized findings vocabulary, cross-tool severity mapping, suppression and baseline governance, changed-file versus full-scope semantics, path and secret scrubbing, machine-format validators, CI artifact upload, access and expiry controls, canonical receipt linkage, correction, invalidation, supersession, and retirement procedure / CONFLICTED tracked empty-result placeholders versus no producer; v0.1 examples versus current scaffold inventory; root lint script name versus TODO-only behavior; pre-commit configuration present versus activation explicitly pending; lint/type/static-analysis grouping versus distinct semantics and authorities; direct tracked generated-output paths versus no ignore or retention rule; passing lint convenience versus correctness, security, evidence, and release significance; and local QA output versus canonical run memory / UNKNOWN uncommitted local reports, CI-only reports, external lint services, exhaustive package-local dependencies and configs, actual inspected targets, current finding counts, active consumers, branch-protection significance, report freshness, retention, hosting, deployment, and production use / NEEDS VERIFICATION accepted owners, CODEOWNERS, complete recursive inventory, generated-output commit policy, canonical tool set and versions, source scope, rule profiles, formatter policy, type-check strictness, security-scanner routing, suppressions and baseline ownership, severity normalization, path normalization, secret and private-path scanning, workflow ownership, artifact retention, receipt/proof linkage, release significance, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 44c4e5e1432f36efa2cbf9958458ba0c3c6c0e85
  target_prior_blob: b28c8c9d0f602340566ab6983522c635a45c181c
  confirmed_lane_files:
    - artifacts/qa/lint/README.md
    - artifacts/qa/lint/ruff.json
    - artifacts/qa/lint/eslint.json
    - artifacts/qa/lint/markdownlint.json
    - artifacts/qa/lint/mypy.txt
  confirmed_lane_blobs:
    README.md: b28c8c9d0f602340566ab6983522c635a45c181c
    ruff.json: b163d5a5f1bb6e8cc75711b32726ed1dc2c2d37b
    eslint.json: 99126ae6106555e879a979fb4518c33e43d175a3
    markdownlint.json: 089338bab727b626c06feca15ee58e352da5a56b
    mypy.txt: f5f917f540bc371efe79e5cb6cd18a0b34d3757d
  checked_absent_paths:
    - artifacts/qa/lint/.gitkeep
    - artifacts/qa/lint/lint-run.json
    - artifacts/qa/lint/lint-summary.json
    - artifacts/qa/lint/static-analysis.sarif
    - ruff.toml
    - mypy.ini
    - eslint.config.js
    - .markdownlint.json
    - .github/workflows/lint.yml
    - schemas/artifacts/lint-run.schema.json
  execution_surfaces:
    - package.json
    - pyproject.toml
    - .pre-commit-config.yaml
    - Makefile
    - .gitignore
    - tools/validators/docs/README.md
  bounded_inventory_note: tracked repository evidence cannot establish uncommitted local reports, package-local ignored outputs, CI workspaces, editor integrations, external lint services, historical artifacts, dynamically generated configuration, branch-protection settings, or uninspected subprojects
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../tools/validators/docs/README.md
  - ../../../tests/README.md
  - ../../../package.json
  - ../../../pyproject.toml
  - ../../../.pre-commit-config.yaml
  - ../../../Makefile
  - ../../../.gitignore
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../release/README.md
tags: [kfm, artifacts, qa, lint, ruff, eslint, markdownlint, mypy, pre-commit, formatting, typecheck, static-analysis, sarif, suppressions, baselines, path-redaction, retention, ci-artifact, correction, rollback]
notes:
  - "v0.2 replaces blanket uncertainty and a proposed tree with a commit-pinned mixed-scaffold inventory."
  - "Ruff, ESLint, and Markdownlint JSON files are illustrative PROPOSED placeholders with empty result lists."
  - "mypy.txt explicitly states that no type-check run has been recorded."
  - "The root lint command is TODO-only; no operational tool configuration, producer, workflow, threshold, or consumer was established."
  - "The pre-commit file is a greenfield placeholder and does not establish installation, activation, CI enforcement, or lint-output generation."
  - "The root ignore rules do not protect this nested lane from accidental generated-report commits."
  - "Lint and static-analysis findings are inspection signals; they do not prove correctness, security, evidence support, policy compliance, or release readiness."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `artifacts/qa/lint/` — Lint, Formatting, Type-Checking, and Static-Inspection Output Boundary

> **Purpose.** Define the staging boundary for generated lint, formatting, type-checking, and bounded static-inspection outputs without allowing an empty result list, zero finding count, green check, SARIF upload, formatter success, type-check pass, editor badge, or workflow name to become source authority, proof of correctness, security assurance, policy compliance, evidence closure, release approval, publication, or production truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: artifacts compatibility" src="https://img.shields.io/badge/root-artifacts__compatibility-orange">
  <img alt="Maturity: mixed scaffolds" src="https://img.shields.io/badge/maturity-MIXED__SCAFFOLDS-red">
  <img alt="Substantive findings: not established" src="https://img.shields.io/badge/findings-NOT__ESTABLISHED-critical">
  <img alt="Producer: not established" src="https://img.shields.io/badge/producer-not__established-lightgrey">
  <img alt="Authority: none" src="https://img.shields.io/badge/trust__authority-none-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-audience) · [Authority](#authority-and-directory-rules-basis) · [Inventory](#confirmed-current-inventory) · [Scaffolds](#current-scaffold-semantics) · [Meaning](#what-lint-can-and-cannot-mean) · [Families](#inspection-family-and-routing-matrix) · [Scope](#inspection-scope-contract) · [Rules](#tool-rule-and-profile-identity) · [Findings](#finding-and-severity-contract) · [Formats](#output-format-and-routing-contract) · [Manifest](#proposed-lint-run-manifest) · [Suppressions](#suppressions-baselines-and-waivers) · [Consistency](#cross-tool-consistency-and-reproducibility) · [Security](#security-privacy-and-path-exposure) · [Producer](#producer-contract) · [CI](#ci-artifact-access-and-retention) · [Validation](#validation-non-vacuity-and-finite-outcomes) · [Trust](#receipt-proof-release-and-publication-boundary) · [Correction](#correction-invalidation-and-rollback) · [Review](#review-burden-and-change-control) · [Done](#definition-of-done) · [Plan](#smallest-sound-implementation-sequence) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Snapshot:** `main@44c4e5e1432f36efa2cbf9958458ba0c3c6c0e85`<br>
> **Prior README blob:** `b28c8c9d0f602340566ab6983522c635a45c181c`<br>
> **Confirmed tracked files:** parent README, three empty-result JSON placeholders, and one no-run Mypy text placeholder<br>
> **Substantive lint or type-check run:** not established<br>
> **Operational tool profiles, producer, workflow, threshold, and consumer:** not established<br>
> **Generated-output ignore protection:** not established

`artifacts/qa/lint/` is a repository-confirmed compatibility lane with **mixed scaffolding**, not an operational lint system.

### Safe conclusion

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Parent boundary README | `CONFIRMED` | A human lint-output contract exists. |
| Ruff output | `SCAFFOLD ONLY` | `status` is `PROPOSED`; `results` is empty; notes call it illustrative. |
| ESLint output | `SCAFFOLD ONLY` | `status` is `PROPOSED`; `results` is empty; notes call it illustrative. |
| Markdownlint output | `SCAFFOLD ONLY` | `status` is `PROPOSED`; `results` is empty; notes call it illustrative. |
| Mypy output | `SCAFFOLD ONLY` | The file states no type-check run has been recorded. |
| Root JavaScript lint command | `TODO-ONLY` | `npm run lint` only echoes `TODO: pnpm -r lint`. |
| Root Python lint dependency | `NOT ESTABLISHED` | Root optional dependencies declare pytest, not Ruff or Mypy. |
| Root Ruff profile | `NOT ESTABLISHED` | Checked `ruff.toml` is absent and no root Ruff block surfaced. |
| Root Mypy profile | `NOT ESTABLISHED` | Checked `mypy.ini` is absent and no root Mypy block surfaced. |
| Root ESLint profile | `NOT ESTABLISHED` | Checked `eslint.config.js` is absent. |
| Root Markdownlint profile | `NOT ESTABLISHED` | Checked `.markdownlint.json` is absent. |
| Pre-commit profile | `PLACEHOLDER` | Basic hooks are listed, but the file says activation is pending. |
| Dedicated lint workflow | `NOT ESTABLISHED` | Checked `.github/workflows/lint.yml` is absent. |
| Run manifest or summary | `NOT ESTABLISHED` | Checked `lint-run.json` and `lint-summary.json` are absent. |
| SARIF staging | `NOT ESTABLISHED` | Checked lane-local `static-analysis.sarif` is absent. |
| Generated-output ignore policy | `NOT ESTABLISHED` | Root ignore rules do not cover this nested JSON/TXT lane. |
| Finding thresholds | `NOT ESTABLISHED` | No accepted maximum, changed-file gate, or severity floor was verified. |
| Suppression governance | `NOT ESTABLISHED` | No accepted baseline or waiver registry was verified. |
| Report freshness | `UNKNOWN` | Tracked files are placeholders, not run-bound output. |
| Canonical run binding | `NOT ESTABLISHED` | No receipt, proof, or release record is linked. |
| Correctness or release proof | `DENY` | Lint cannot establish semantic correctness or releasability. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, exact paths, or bounded search. |
| `PROPOSED` | A recommended command, object, policy, profile, or workflow not established as current implementation. |
| `CONFLICTED` | Current files or documentation create incompatible expectations. |
| `UNKNOWN` | Not observable or not established from inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently proven for operational reliance. |
| `DENY` | A prohibited trust, correctness, security, release, or publication interpretation. |

[Back to top](#top)

---

## Purpose and audience

This README is the parent operating contract for maintainers who run, export, inspect, upload, compare, retain, suppress, baseline, or cite lint and related static-inspection results.

It is intended for:

- QA, test-architecture, and lint/tooling stewards;
- Python, JavaScript/TypeScript, Markdown, schema, contract, and documentation maintainers;
- formatter and type-system owners;
- CI and artifact-retention maintainers;
- security and privacy reviewers inspecting paths, source excerpts, and machine output;
- reviewers deciding whether findings are actionable or safely suppressed;
- receipt, proof, release, correction, and rollback stewards;
- documentation maintainers correcting stale lint or quality claims.

The durable question is:

> Can KFM describe exactly what a configured inspection run checked, preserve useful machine output, and review suppressions without treating the absence of configured findings as proof that the inspected material is correct, safe, evidence-backed, policy-compliant, or releasable?

A valid lint result is always scoped. Even a clean run can coexist with:

- incorrect behavior;
- incorrect requirements;
- missing tests;
- type-unsound runtime paths outside the checked scope;
- dynamically loaded code the tool cannot see;
- ignored files or generated code;
- incorrect data semantics;
- evidence-resolution failures;
- policy or sensitivity violations;
- security flaws outside the selected rule set;
- inaccessible or misleading user interfaces;
- race conditions and integration defects;
- rights or licensing problems;
- release and rollback gaps.

### What this parent governs

This parent governs:

1. inspected source and document scope;
2. tool, version, plugin, and rule-profile identity;
3. formatter-check versus mutating-format separation;
4. finding representation and severity normalization;
5. machine-readable output routing;
6. suppressions, baselines, and waivers;
7. cross-tool consistency and reproducibility;
8. source/path/security exposure;
9. CI artifact access and retention;
10. the boundary between QA output and canonical receipts, proofs, and release decisions.

It does not define language semantics, source authority, policy rules, schemas, contracts, or release approval.

[Back to top](#top)

---

## Authority and Directory Rules basis

`artifacts/` is a transitional compatibility root for derived, regenerable, non-authoritative material. `artifacts/qa/lint/` inherits that classification through `artifacts/qa/`.

```text
source, docs, schemas, contracts, policy     authority and inspected inputs
tool and package configuration               configured rule/profile authority
CI workflows and executable tooling          orchestration
artifacts/qa/lint/                            generated inspection output only
data/receipts/ and data/proofs/               canonical run memory and support
release/                                      governed release decisions
```

This lane may contain generated findings and summaries. It must not become:

- a source-code, source-document, schema, contract, or policy home;
- a lint or type-check configuration authority;
- a CI workflow home;
- a suppression-decision authority;
- a canonical run receipt;
- a proof or EvidenceBundle home;
- a release gate or promotion record;
- a public documentation or deployment surface;
- a permanent archive of source excerpts or private paths;
- a shortcut around governed review.

### Placement decision

The existing path is appropriate because it is already governed as a QA-output sublane under the `artifacts/` compatibility root.

The responsibilities remain separated:

| Responsibility | Owning location |
|---|---|
| Source code and authored documents | Their canonical responsibility roots |
| Tool dependencies and profiles | Root/package configuration or accepted tooling roots |
| Lint and formatter execution | Executable tooling and CI |
| Generated lint reports | `artifacts/qa/lint/` |
| Documentation-specific semantic validators | `tools/validators/docs/` when implemented |
| QA receipts | `data/receipts/` when material |
| Proof or attestation | `data/proofs/` when material |
| Release decision | `release/` |
| Public delivery | Governed published surfaces, never this lane directly |

A new schema for a future lint-run manifest would belong under the canonical `schemas/` responsibility root, not under `artifacts/`. The checked candidate `schemas/artifacts/lint-run.schema.json` is absent; that exact path remains `PROPOSED / NEEDS VERIFICATION`, not repo fact.

[Back to top](#top)

---

## Confirmed current inventory

Bounded tracked evidence supports:

```text
artifacts/qa/lint/
├── README.md
├── eslint.json
├── markdownlint.json
├── mypy.txt
└── ruff.json
```

Checked absent:

```text
artifacts/qa/lint/.gitkeep
artifacts/qa/lint/lint-run.json
artifacts/qa/lint/lint-summary.json
artifacts/qa/lint/static-analysis.sarif
ruff.toml
mypy.ini
eslint.config.js
.markdownlint.json
.github/workflows/lint.yml
schemas/artifacts/lint-run.schema.json
```

### Inventory interpretation

| Path | Current role | Current limitation |
|---|---|---|
| `README.md` | Human boundary | v0.1 did not enumerate the actual scaffolds. |
| `ruff.json` | Illustrative Ruff placeholder | Empty `results`; no run identity or tool version. |
| `eslint.json` | Illustrative ESLint placeholder | Empty `results`; no run identity or tool version. |
| `markdownlint.json` | Illustrative Markdownlint placeholder | Empty `results`; no run identity or tool version. |
| `mypy.txt` | Proposed Mypy placeholder | Explicitly says no type-check run is recorded. |

Tracked repository evidence cannot enumerate:

- uncommitted local outputs;
- ignored package-local reports;
- editor diagnostics;
- CI workspaces;
- GitHub-native annotations;
- external lint or security services;
- historical workflow artifacts;
- package-local configuration not surfaced by bounded search;
- dynamically generated profiles;
- branch-protection settings.

[Back to top](#top)

---

## Current scaffold semantics

### Ruff placeholder

The tracked JSON declares:

- `status: PROPOSED`;
- `tool: ruff`;
- its own path;
- an empty `results` list;
- a note saying it is an illustrative placeholder.

Therefore it does **not** prove:

- Ruff is installed;
- a Ruff version is selected;
- a rule set exists;
- any Python file was inspected;
- zero findings were produced by a real run;
- formatting was checked;
- CI passed.

### ESLint placeholder

The tracked JSON follows the same placeholder pattern. It does not establish:

- ESLint installation;
- parser, plugin, or resolver configuration;
- a JavaScript or TypeScript project graph;
- inspected files;
- warnings or errors;
- autofix behavior;
- CI enforcement.

### Markdownlint placeholder

The tracked JSON also has an empty `results` list and illustrative note. It does not establish:

- a Markdownlint implementation or version;
- a rule profile;
- glob scope;
- generated-document exclusions;
- inline disable policy;
- link, citation, terminology, or truth-label validation;
- a clean documentation run.

Markdown style lint and KFM documentation-semantic validators are different concerns. Style checks do not replace link, metadata, truth-label, evidence-posture, or terminology validators.

### Mypy placeholder

`mypy.txt` states that no type-check run has been recorded and should be replaced only if a QA pipeline writes generated output there.

It therefore does not establish:

- Mypy installation or version;
- Python targets;
- import discovery;
- namespace-package behavior;
- strictness;
- ignored missing imports;
- plugin configuration;
- cache state;
- a clean or failing type-check result.

### Scaffold outcome

The only safe current result is:

```text
LINT_MEASUREMENT_NOT_ESTABLISHED
```

Do not convert the placeholders to any of these claims:

```text
0 findings
all lint checks passed
type checking passed
formatting is clean
static analysis passed
release quality gate passed
```

A placeholder with no denominator, tool identity, scope, or command is not a measurement.

[Back to top](#top)

---

## What lint can and cannot mean

### What a lint result may support

A properly bound result may support statements such as:

- a named tool version inspected a declared target set;
- a declared rule profile was loaded;
- configured findings were emitted;
- a formatter check found or did not find changes;
- type analysis completed under a named strictness profile;
- a SARIF-compatible scanner emitted normalized findings;
- a threshold or changed-file policy was evaluated;
- an artifact was retained for reviewer inspection.

### What it cannot establish by itself

Lint output cannot prove:

- semantic correctness;
- runtime correctness;
- test completeness;
- source authority;
- evidence sufficiency;
- policy compliance beyond explicitly implemented static checks;
- absence of security vulnerabilities;
- data quality;
- rights or licensing clearance;
- accessibility;
- release readiness;
- publication approval;
- production behavior.

### Clean is not complete

A zero-finding result may mean:

1. the inspected files satisfy the configured rules;
2. the selected rules do not cover the defect;
3. files were omitted or ignored;
4. a parser failed open;
5. the command inspected an empty target set;
6. the output was stale;
7. suppressions hid findings;
8. baseline mode ignored existing debt;
9. the tool exited before emitting findings;
10. the representation lost data.

Every clean result must therefore carry enough identity and non-vacuity evidence to distinguish these cases.

[Back to top](#top)

---

## Inspection family and routing matrix

The word “lint” is often used too broadly. KFM should preserve distinct result classes.

| Family | Example purpose | Output role | Important boundary |
|---|---|---|---|
| Syntax/style lint | Python, JS/TS, Markdown style findings | Findings | Not semantic correctness. |
| Formatter check | Detect whether canonical formatting would change files | Pass/fail plus changed paths | Check mode must not mutate source. |
| Type checking | Static type constraints and import graph | Type findings | Not runtime proof. |
| Documentation semantic validation | Metadata, links, truth labels, terminology | Validator findings | Belongs to docs-validator tooling; not generic style lint. |
| Schema/contract validation | Shape and contract enforceability | Validation findings | Canonical validators, not lint-output authority. |
| Security static analysis | Security-focused findings | SARIF or tool-native results | Security review remains separate. |
| Dependency analysis | Package vulnerability/license findings | Scanner output | Not source lint. |
| Secret scanning | Credential-pattern and entropy findings | Restricted scanner output | Sensitive output handling required. |
| Compiler diagnostics | Language compiler errors/warnings | Compiler output | Toolchain-specific, not interchangeable with lint. |
| Generated-code checks | Generated file drift or regeneration requirement | Drift result | Generator authority remains elsewhere. |

### Routing rules

- Keep each tool’s native output or a lossless normalized form.
- Do not merge type errors, style warnings, and security findings into an unexplained count.
- Route documentation-semantic validators to their accepted tooling lanes; stage their non-authoritative outputs under QA only when useful.
- Route security-sensitive findings under access controls appropriate to their content.
- Route canonical decisions, waivers, receipts, proofs, and release gates outside this directory.

[Back to top](#top)

---

## Inspection scope contract

A lint result is interpretable only when its inspected scope is explicit.

### Required source identity

A material run should record:

| Field | Requirement |
|---|---|
| Repository | Stable repository identity |
| Source commit | Full Git SHA |
| Dirty state | Clean, dirty, or unknown |
| Diff basis | Base/head refs for changed-file mode |
| Working directory | Normalized repository-relative path |
| Submodule state | When applicable |
| Generated inputs | Generator and source refs when inspected |
| Configuration digest | Digest of effective profile and ignore rules |

### Required target identity

The run must distinguish:

- repository-wide scope;
- workspace/package scope;
- explicit path scope;
- changed-file scope;
- staged-file scope;
- generated-output scope;
- documentation-only scope;
- language-specific scope.

Record include and exclude patterns after expansion where practical.

### Empty-scope posture

If no files are selected:

```text
EMPTY_SCOPE
```

The result must not be reported as a successful clean run unless the profile explicitly defines empty scope as expected and records why.

### Changed-file mode

Changed-file lint can be useful for incremental enforcement, but it must not be presented as repository-wide quality.

Record:

- comparison base;
- rename handling;
- deleted-file handling;
- generated-file treatment;
- path filters;
- whether dependent files were also inspected;
- whether full-scope checks run elsewhere.

### Generated and vendored code

Every profile should explicitly classify:

- generated code;
- vendored dependencies;
- migrations;
- fixtures;
- snapshots;
- minified assets;
- compiled output;
- archived material;
- compatibility roots.

Silent exclusion is not acceptable for material scope decisions.

[Back to top](#top)

---

## Tool, rule, and profile identity

### Tool identity

Record for every producer:

- tool name;
- semantic version;
- executable or package digest when material;
- runtime version;
- plugin names and versions;
- parser or language-service versions;
- invocation command or immutable command reference;
- configuration paths and digests.

A filename such as `ruff.json` is not tool identity.

### Effective rule identity

The effective profile includes:

- enabled rules;
- disabled rules;
- severity overrides;
- formatter settings;
- target language/runtime version;
- plugin configuration;
- resolver and import settings;
- per-file ignores;
- excluded paths;
- inline suppression policy;
- baseline files;
- generated-code policy.

Record the effective configuration, not only the nominal config filename.

### Root and package-local profiles

KFM is a multi-language, multi-package repository. A future implementation may need:

- root defaults;
- package-local extensions;
- domain-specific constraints;
- generated-code exceptions;
- documentation profiles;
- security overlays.

Profile precedence must be deterministic and reviewable.

### Configuration absence

When an expected profile is missing, use:

```text
PROFILE_NOT_ESTABLISHED
```

Do not silently run a tool’s changing defaults and call the result canonical.

[Back to top](#top)

---

## Finding and severity contract

### Minimum normalized finding

A normalized finding should preserve:

| Field | Purpose |
|---|---|
| `finding_id` | Stable identity for review and correction |
| `tool` | Producer name and version |
| `rule_id` | Native rule identity |
| `category` | Style, correctness, type, documentation, security, other |
| `severity_native` | Original tool severity |
| `severity_normalized` | Accepted cross-tool severity |
| `message` | Human-readable diagnostic |
| `path` | Repository-relative normalized path |
| `start` / `end` | Location when available |
| `fingerprint` | Stable suppression/baseline identity |
| `autofix_available` | Whether a tool proposes a fix |
| `suppression_state` | Active, suppressed, baseline, expired, disputed |
| `source_ref` | Commit or run binding |

### Native data preservation

Normalization must not discard:

- rule help URLs;
- code frames;
- secondary locations;
- traces;
- fixes;
- tags;
- confidence;
- precision;
- security taxonomy;
- parser errors.

Retain native output or a digest-addressed native attachment when a normalized summary is emitted.

### Severity mapping

A cross-tool severity map is `PROPOSED` until accepted.

Suggested normalized levels:

```text
INFO
WARNING
ERROR
BLOCKER
UNKNOWN
```

Do not map a tool warning to a release blocker without a governed profile and owner.

### Stable finding identity

A finding fingerprint should avoid host-specific absolute paths and unstable line-only identity where practical. It may combine:

- tool and rule;
- normalized path;
- syntax or symbol identity;
- message class;
- nearby semantic context;
- profile version.

Fingerprint collisions and changes must be reviewable.

[Back to top](#top)

---

## Output format and routing contract

### Current tracked formats

| Current file | Intended family | Current posture |
|---|---|---|
| `ruff.json` | Python lint | Placeholder only |
| `eslint.json` | JS/TS lint | Placeholder only |
| `markdownlint.json` | Markdown style lint | Placeholder only |
| `mypy.txt` | Python type check | Placeholder only |

### Future accepted staging formats

Potential outputs, all `PROPOSED`, include:

| Format | Appropriate use | Constraints |
|---|---|---|
| Tool-native JSON | Lossless findings | Validate structure and scrub paths |
| SARIF | Multi-tool code-scanning exchange | Preserve tool/rule identity |
| Plain text | Human inspection | Must have companion run identity |
| JUnit XML | Test-like CI display | Do not erase finding semantics |
| Summary JSON | Dashboard or PR summary | Must point to native output |
| HTML | Human browser inspection | Separate sublane if needed |
| Formatter diff | Proposed formatting changes | Never apply silently in check mode |

### Parent versus sublane routing

Keep the parent flat unless a durable tool-specific or representation-specific child has a distinct contract.

A future child should have:

- clear responsibility;
- producer;
- profile;
- output shape;
- retention;
- reviewer;
- correction path.

Do not create one child directory per tool merely for visual tidiness.

### Staging names

Run-bound filenames should prevent accidental overwrite. A possible pattern is:

```text
<run-id>.<tool>.<format>
```

This naming pattern is `PROPOSED`; exact identity and retention policy remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Proposed lint-run manifest

A future non-authoritative manifest may describe one coordinated inspection run.

```json
{
  "schema_version": "PROPOSED",
  "status": "PROPOSED",
  "run_id": "immutable-run-id",
  "source": {
    "repository": "owner/repository",
    "git_sha": "full-sha",
    "dirty": false,
    "base_sha": null
  },
  "scope": {
    "mode": "full|package|paths|changed|staged",
    "include": [],
    "exclude": [],
    "selected_file_count": 1
  },
  "tools": [
    {
      "name": "tool-name",
      "version": "tool-version",
      "profile_ref": "profile-ref",
      "profile_digest": "sha256:...",
      "command_ref": "command-ref",
      "exit_code": 0,
      "findings": {
        "info": 0,
        "warning": 0,
        "error": 0,
        "blocker": 0
      },
      "output_ref": "relative-path",
      "output_digest": "sha256:..."
    }
  ],
  "suppressions": {
    "active": 0,
    "expired": 0,
    "unowned": 0
  },
  "outcome": "PASS|FAIL|HOLD|ABSTAIN|DENY|ERROR|NOT_EVALUATED",
  "canonical_refs": {
    "receipt_ref": null,
    "proof_ref": null,
    "release_ref": null
  }
}
```

### Manifest invariants

A validator should reject or hold a manifest when:

- source SHA is missing;
- dirty state is unknown where clean state is required;
- selected file count is zero without an accepted empty-scope reason;
- tool version is absent;
- profile identity is absent;
- native output is missing;
- output digest does not match;
- counts disagree with native output;
- suppressions are unowned or expired;
- a placeholder is presented as a run;
- outcome is inconsistent with findings or thresholds;
- canonical references are implied but unresolved.

### Authority boundary

This manifest would be a staging index only. A trust-bearing run receipt belongs in `data/receipts/`; a proof or attestation belongs in `data/proofs/`; a release decision belongs in `release/`.

[Back to top](#top)

---

## Suppressions, baselines, and waivers

Suppressions are governance-significant because they change which findings are visible.

### Suppression types

Distinguish:

- inline source suppression;
- per-file ignore;
- profile-level disabled rule;
- path exclusion;
- generated-code exception;
- accepted baseline debt;
- temporary waiver;
- false-positive disposition;
- tool limitation;
- duplicate finding.

### Minimum suppression record

A material suppression should identify:

- finding or rule;
- affected path/scope;
- owner;
- reason;
- created date;
- review or expiry date;
- risk acceptance;
- replacement or remediation plan;
- linked issue/ADR where material.

### Default posture

- New unowned suppressions: `HOLD`.
- Expired suppressions: `FAIL` or `HOLD` according to profile.
- Broad wildcard suppressions: elevated review.
- Security-related suppressions: security steward review.
- Sensitive-lane suppressions: policy and domain review where material.
- Suppressions that hide parser/configuration failures: `DENY`.

### Baseline mode

A baseline can support gradual adoption, but reports must separate:

- pre-existing baseline findings;
- newly introduced findings;
- resolved findings;
- changed fingerprints;
- unclassified findings.

“Only new findings fail” must never be summarized as “repository lint passes” without qualification.

### Autofix boundary

Autofix changes source. Therefore:

- check and fix modes must be distinct;
- CI should not silently mutate source and then pass;
- generated fix patches should be reviewable;
- tool version and profile must be pinned;
- post-fix checks must rerun;
- semantic or large transformations require normal code review.

[Back to top](#top)

---

## Cross-tool consistency and reproducibility

### Same-run consistency

Outputs from coordinated tools should agree on:

- source commit;
- dirty state;
- path normalization;
- selected target set;
- generated-code policy;
- run identity;
- profile set.

A “clean” summary assembled from outputs against different commits is invalid.

### Representation consistency

When native JSON, SARIF, text, and summary outputs describe the same tool run:

- total finding counts must reconcile;
- severities must map deterministically;
- paths must normalize consistently;
- suppressions must be represented consistently;
- digests must bind exact retained bytes.

### Reproducibility classes

Use precise claims:

| Claim | Requirement |
|---|---|
| `COMMAND_REPRODUCIBLE` | Same command/profile can be reconstructed |
| `FINDING_EQUIVALENT` | Normalized finding set matches |
| `BYTE_REPRODUCIBLE` | Retained output bytes match |
| `NOT_COMPARABLE` | Scope/profile/tool differs materially |
| `UNKNOWN` | Evidence is insufficient |

Lint output may contain timestamps, ordering differences, tool paths, or environment details. Byte reproducibility is not always required, but normalized-finding equivalence must be defined before claiming stable results.

### Ordering

For deterministic machine output, sort findings by stable keys where the tool does not guarantee order:

1. normalized path;
2. start position;
3. rule ID;
4. stable fingerprint.

Do not reorder native data in a way that invalidates signatures or digests.

### Network posture

Lint and formatting should generally run without network access after dependencies are resolved. A network-dependent plugin or remote service must be explicit, bounded, and reviewed.

[Back to top](#top)

---

## Thresholds, trends, and comparability

### Threshold classes

Possible policies include:

- zero errors;
- maximum warnings;
- zero new findings relative to a baseline;
- changed-file cleanliness;
- no expired suppressions;
- no parser/configuration failures;
- security severity floor;
- type-check strictness floor;
- formatter-clean requirement.

Every threshold must identify an owner and profile.

### Finding counts are not quality scores

Counts are affected by:

- target size;
- rule-set changes;
- tool upgrades;
- parser changes;
- generated-code policy;
- baseline changes;
- severity remapping;
- code movement;
- deduplication.

Do not compare counts across materially different profiles.

### Comparable trend identity

A trend point should match on:

- tool and version policy;
- profile digest;
- target scope;
- path normalization;
- baseline policy;
- suppression policy;
- severity map;
- generated-code classification.

Otherwise report `NOT_COMPARABLE`.

### Changed-file gates

Changed-file gates can prevent new debt but do not prove repository-wide cleanliness. Summaries must label them explicitly.

### Rule upgrades

When upgrading a tool or ruleset:

1. run old and new profiles where practical;
2. classify added and removed findings;
3. review severity changes;
4. update baselines transparently;
5. record migration effects;
6. avoid presenting the new count as a code regression without analysis.

[Back to top](#top)

---

## Security, privacy, and path exposure

Lint output can expose more than finding counts.

### Potential exposure

Reports may contain:

- absolute developer or runner paths;
- usernames and home directories;
- private repository names;
- internal endpoints;
- source excerpts;
- secrets embedded in source;
- generated configuration;
- dependency locations;
- stack traces;
- command arguments;
- environment variables;
- suppressed security findings.

### Required controls

Before retention or upload:

- normalize paths to repository-relative form;
- scan names and values for credentials and tokens;
- redact private endpoints and hostnames;
- avoid embedding full environment dumps;
- limit source excerpts;
- remove editor- or workstation-specific metadata;
- validate MIME type and encoding;
- reject active HTML/JavaScript unless explicitly required;
- prevent external assets from loading in retained reports;
- classify security-sensitive findings separately.

### Public-repository posture

Because the repository is public, tracked lint artifacts must be assumed public. Never commit a report merely because it was generated by a trusted tool.

### SARIF posture

SARIF can carry code flows, locations, help URIs, and partial fingerprints. Validate and scrub it before staging. GitHub-native code-scanning storage does not automatically make a lane-local SARIF copy safe or authoritative.

### Secret-scanner output

Secret-scanning findings may themselves reveal sensitive substrings. Route them through restricted handling; do not place raw secrets in this public compatibility lane.

[Back to top](#top)

---

## Producer contract

A future producer must be executable, versioned, and outside this output directory.

### Required producer inputs

- source commit and working-tree state;
- selected scope;
- tool profile registry;
- dependency lock or resolved tool versions;
- suppression/baseline registry;
- output destination;
- retention class;
- no-network and redaction settings.

### Required producer behavior

1. Remove or quarantine stale outputs before execution.
2. Resolve tools and profiles fail-closed.
3. Expand scope and record selected file count.
4. Reject unexpected empty scope.
5. Run tools in check-only mode unless mutation is explicitly requested.
6. Preserve native exit codes.
7. Capture native outputs.
8. Normalize findings without losing native data.
9. Validate output structures.
10. Scan retained artifacts for sensitive values.
11. Compute digests.
12. Emit a run manifest.
13. Evaluate thresholds.
14. Write canonical receipts elsewhere when required.
15. Return a finite outcome.

### Required producer outputs

- run manifest;
- native tool outputs;
- normalized summary;
- validation result;
- suppression state;
- digests;
- explicit outcome;
- cleanup status.

### Failure cleanup

On failure:

- do not leave stale files appearing current;
- mark partial outputs;
- preserve diagnostic logs only when safe;
- distinguish tool failure from findings;
- distinguish parser failure from clean output;
- emit `ERROR`, `HOLD`, or `ABSTAIN` as appropriate.

### No writer in this lane

Executable producer code, configuration, or schemas must not be placed under `artifacts/qa/lint/`.

[Back to top](#top)

---

## CI artifact access and retention

### CI separation

Separate these steps:

1. install/resolve tools;
2. calculate scope;
3. execute inspection;
4. validate outputs;
5. evaluate thresholds;
6. upload artifacts;
7. emit annotations;
8. write canonical receipts if required;
9. allow release systems to consume the governed result.

Uploading an artifact is not a gate decision.

### Artifact naming

A CI artifact name should identify:

- workflow;
- run attempt;
- source SHA;
- scope/profile;
- tool family.

Avoid mutable names such as only `lint-report`.

### Access posture

Reports that contain source excerpts, security findings, internal paths, or proprietary plugin data may require restricted access even when the repository is public.

### Retention classes

Proposed classes:

| Class | Use | Posture |
|---|---|---|
| `EPHEMERAL_PR` | Reviewer inspection | Short expiry |
| `DEBUG_FAILURE` | Failure investigation | Restricted, short-lived |
| `BASELINE_CANDIDATE` | Suppression/baseline review | Steward review required |
| `RELEASE_SUPPORT` | Release-significant QA support | Canonical receipt reference required |
| `LOCAL_ONLY` | Developer inspection | Never uploaded by default |

Exact durations remain `NEEDS VERIFICATION`.

### Repository retention

Generated outputs should not be committed by default merely to preserve history. Prefer CI artifact storage or regenerable local output unless an accepted policy requires a tracked fixture or scaffold.

### Current ignore conflict

The root `.gitignore` ignores only direct XML files under `artifacts/qa/`. It does not protect the tracked JSON/TXT lint lane. Until a policy is accepted, reviewers must detect accidental generated-output commits manually.

[Back to top](#top)

---

## Validation, non-vacuity, and finite outcomes

### Structural validation

Validate:

- file parseability;
- expected tool identity;
- manifest shape;
- output digests;
- path normalization;
- finding counts;
- severity vocabulary;
- source/run identity.

### Semantic validation

Validate:

- selected file count is nonzero unless explicitly allowed;
- profile loaded successfully;
- parser/config errors are not presented as clean;
- all expected tool outputs exist;
- native and normalized counts reconcile;
- suppressions are owned and current;
- thresholds use the intended scope;
- stale outputs are not mixed into the run.

### Security validation

Validate:

- no credentials;
- no private keys;
- no private endpoints;
- no unapproved absolute paths;
- no unsafe active content;
- no unreviewed security-sensitive finding details;
- no unrestricted full source copies.

### Non-vacuity checks

A clean result is invalid when:

- zero files were selected unexpectedly;
- a tool executable was missing;
- a config was not loaded;
- parsing failed open;
- every finding was suppressed by a broad rule;
- outputs are still placeholders;
- output timestamps/source refs do not match the run;
- only generated or empty files were inspected unintentionally.

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Configured inspections completed and accepted thresholds passed. |
| `FAIL` | Findings or threshold violations require failure. |
| `HOLD` | Review, suppression, baseline, security, or ownership issue blocks reliance. |
| `ABSTAIN` | Available evidence cannot support a safe conclusion. |
| `DENY` | Output or requested interpretation violates authority, security, or governance rules. |
| `ERROR` | Tooling or orchestration could not complete safely. |
| `NOT_EVALUATED` | A threshold or gate was intentionally not applied. |
| `EMPTY_SCOPE` | No targets were selected; clean interpretation denied unless expected. |
| `PROFILE_NOT_ESTABLISHED` | Required configuration is absent or unresolved. |
| `PLACEHOLDER_ONLY` | Files are scaffolds rather than run-bound results. |
| `NOT_COMPARABLE` | Trend or cross-run comparison is invalid. |

### Outcome precedence

A suggested conservative precedence is:

```text
DENY > ERROR > HOLD > FAIL > ABSTAIN > NOT_EVALUATED > PASS
```

`EMPTY_SCOPE`, `PROFILE_NOT_ESTABLISHED`, and `PLACEHOLDER_ONLY` should normally map to `HOLD`, `ABSTAIN`, or `ERROR` according to context.

[Back to top](#top)

---

## Receipt, proof, release, and publication boundary

A lint report in this directory is not a canonical governance artifact.

```text
source + profiles + tools
          |
          v
lint execution and output validation
          |
          v
artifacts/qa/lint/              non-authoritative inspection copy
          |
          +--> data/receipts/   canonical run memory when material
          +--> data/proofs/     attestation or evidence support when material
          +--> release/         governed decision, never automatic
```

### Required distinctions

- Digest proves byte identity, not finding correctness.
- Signature authenticates a signer and bytes, not semantic sufficiency.
- SARIF interchange does not create security approval.
- A receipt records the run, not source correctness.
- A proof supports a claim within scope, not all quality.
- A release record decides promotion; the QA directory does not.

### Release-significant lint

When a release depends on lint:

- the accepted profile must be pinned;
- scope must be release-relevant;
- run identity must bind the release commit;
- suppressions must be reviewed;
- results must be validated;
- a canonical receipt must record the outcome;
- the release manifest should reference the canonical record or digest;
- rollback and correction targets must exist.

### Public clients

Public clients and normal UI surfaces must never consume this directory directly.

[Back to top](#top)

---

## Correction, invalidation, and rollback

### Correction triggers

Correct or invalidate a result when:

- source SHA was wrong;
- wrong scope was selected;
- config failed to load;
- tool version was misreported;
- parser errors were hidden;
- output was stale;
- counts did not reconcile;
- suppression ownership was invalid;
- a secret or private path was exposed;
- severity mapping changed;
- a baseline was corrupted;
- a finding fingerprint collision occurred;
- a release cited the wrong result.

### Correction procedure

1. Stop relying on the affected report.
2. Mark or remove the stale staging copy.
3. Identify affected commits, PRs, receipts, proofs, and releases.
4. Preserve the original digest when audit value requires it.
5. Fix the producer, profile, scope, or redaction.
6. Rerun against an immutable source.
7. Emit a new run identity and digests.
8. Write canonical correction records where required.
9. Invalidate caches, annotations, or external uploads.
10. Review whether release correction or rollback is necessary.

### Withdrawal

Withdraw artifacts that contain secrets, protected information, or misleading clean results. Deletion from this directory does not retract copies already uploaded to CI, code-scanning systems, comments, dashboards, or release records.

### Rollback

Documentation-only rollback:

- restore the prior README blob;
- revert the documentation commit;
- or publish a corrective evidence-grounded revision.

Operational rollback, once implementation exists, must target:

- producer version;
- tool profile;
- baseline/suppression set;
- workflow configuration;
- artifact retention;
- canonical receipts;
- release consumers.

[Back to top](#top)

---

## Review burden and change control

### Routine review

README-only corrections require:

- evidence check;
- authority-boundary check;
- link and Markdown validation;
- no new implementation claims without proof.

### Elevated review

Require additional review for:

- new lint tools or plugins;
- new severity mappings;
- new suppressions or baseline policy;
- security scanners;
- source-excerpt retention;
- external services;
- release-blocking thresholds;
- changed-file-only enforcement;
- generated-code exclusions;
- public artifact retention;
- tool outputs containing sensitive data.

### Material behavior changes

A material implementation change should update:

- tool dependencies;
- configuration;
- producer code;
- workflow;
- tests;
- schemas/contracts where applicable;
- this README;
- parent QA documentation;
- retention policy;
- security documentation;
- receipt/release documentation when relied upon.

### No silent promotion

Do not promote a placeholder, editor integration, pre-commit hook, or optional local command into a required release gate without explicit governance and CI evidence.

[Back to top](#top)

---

## Definition of done

This lane is operationally complete only when all applicable items are satisfied.

### Ownership and placement

- [ ] Owners are accepted.
- [ ] `CODEOWNERS` coverage is verified.
- [ ] Compatibility-root retention or retirement is decided.
- [ ] Generated-output commit policy is accepted.
- [ ] No parallel authority home is created.

### Tools and profiles

- [ ] Canonical tool families are selected.
- [ ] Tool and plugin versions are pinned.
- [ ] Root/package profile precedence is documented.
- [ ] Language/runtime targets are explicit.
- [ ] Formatter check and fix modes are separated.
- [ ] Type-check strictness is explicit.
- [ ] Documentation style and semantic validation are separated.
- [ ] Security-scanner routing is explicit.

### Scope and execution

- [ ] Source and test/document scope is explicit.
- [ ] Include/omit rules are accepted.
- [ ] Generated and vendored code policy is accepted.
- [ ] Empty-scope checks fail safely.
- [ ] Network posture is explicit.
- [ ] Dirty-tree behavior is explicit.
- [ ] Changed-file and full-scope modes are distinguished.

### Outputs

- [ ] Native output formats are documented.
- [ ] Normalized finding schema is accepted.
- [ ] Run manifest shape is accepted.
- [ ] Digests are computed after final serialization.
- [ ] Cross-format counts reconcile.
- [ ] Placeholder detection is enforced.
- [ ] Stale-output cleanup is enforced.

### Suppressions and thresholds

- [ ] Suppression ownership and expiry are enforced.
- [ ] Baseline policy is documented.
- [ ] Severity map is accepted.
- [ ] Threshold owners are accepted.
- [ ] Trend comparability rules are implemented.
- [ ] Rule-upgrade migrations are reviewable.

### Security and retention

- [ ] Path normalization is enforced.
- [ ] Secret/private-endpoint scanning is enforced.
- [ ] Source-excerpt policy is accepted.
- [ ] Active-content policy is enforced.
- [ ] CI access and expiry are configured.
- [ ] Cleanup and withdrawal are tested.

### Governance

- [ ] Finite outcomes are emitted.
- [ ] Canonical receipts are written when material.
- [ ] Proof/release consumers resolve canonical references.
- [ ] Correction and rollback paths are tested.
- [ ] Public clients cannot consume this lane directly.

Until then, the safe status remains:

```text
MIXED_SCAFFOLD / LINT_MEASUREMENT_NOT_ESTABLISHED
```

[Back to top](#top)

---

## Smallest sound implementation sequence

### Phase 1 — Inventory and ownership

- Confirm all root and package-local lint/type/formatter configs.
- Confirm actual tool dependencies.
- Confirm owners and `CODEOWNERS`.
- Decide whether tracked placeholders remain, migrate to fixtures, or are removed.
- Decide generated-output commit policy.

**Exit:** accepted inventory and ownership map.

### Phase 2 — Profiles and scope

- Define canonical tool/profile registry.
- Define source scopes and package precedence.
- Define generated/vendored exclusions.
- Define changed-file versus full-scope behavior.
- Define no-network and dirty-tree posture.

**Exit:** deterministic profile and scope contract.

### Phase 3 — Producer and native outputs

- Implement a versioned producer outside this lane.
- Emit native outputs and a run manifest.
- Remove stale outputs before each run.
- Reject empty scope and placeholder output.
- Compute digests after final serialization.

**Exit:** reproducible local run.

### Phase 4 — Suppressions and normalization

- Define normalized finding schema.
- Preserve native data.
- Establish severity mapping.
- Implement owned, expiring suppressions.
- Implement baseline migration and fingerprint handling.

**Exit:** reviewable findings and waivers.

### Phase 5 — CI and retention

- Add substantive workflow execution.
- Separate check, threshold, upload, and canonical receipt steps.
- Configure artifact access and expiry.
- Verify no source mutation occurs in check mode.
- Test failure cleanup.

**Exit:** CI produces governed inspection artifacts.

### Phase 6 — Security and governance binding

- Enforce path and secret scrubbing.
- Restrict sensitive findings.
- Write canonical receipts when material.
- Bind release consumers to canonical records.
- Test correction, invalidation, and withdrawal.

**Exit:** safe governed handoff.

### Phase 7 — Retirement or stabilization

- Decide whether this compatibility lane remains useful.
- Migrate durable records to canonical homes.
- Remove redundant tracked scaffolds.
- Document deprecation if retiring.
- Preserve rollback and audit references.

**Exit:** accepted steady-state or retirement plan.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status | Why it matters |
|---|---|---:|---|
| LINT-001 | Confirm accepted owners | `NEEDS VERIFICATION` | Accountability |
| LINT-002 | Confirm `CODEOWNERS` coverage | `NEEDS VERIFICATION` | Review routing |
| LINT-003 | Decide retain/migrate/retire posture | `NEEDS VERIFICATION` | Compatibility debt |
| LINT-004 | Confirm complete tracked inventory | `NEEDS VERIFICATION` | Avoid omissions |
| LINT-005 | Confirm untracked/ignored local output policy | `UNKNOWN` | Workspace hygiene |
| LINT-006 | Decide disposition of four placeholders | `NEEDS VERIFICATION` | Prevent false measurement |
| LINT-007 | Confirm canonical Python lint tool | `NEEDS VERIFICATION` | Tool identity |
| LINT-008 | Confirm canonical Python formatter | `NEEDS VERIFICATION` | Formatting policy |
| LINT-009 | Confirm canonical Python type checker | `NEEDS VERIFICATION` | Type policy |
| LINT-010 | Confirm canonical JS/TS lint tool | `NEEDS VERIFICATION` | Tool identity |
| LINT-011 | Confirm JS/TS parser/plugins | `NEEDS VERIFICATION` | Correct scope |
| LINT-012 | Confirm Markdown style tool | `NEEDS VERIFICATION` | Docs style |
| LINT-013 | Separate docs semantic validators from style lint | `NEEDS VERIFICATION` | Authority clarity |
| LINT-014 | Confirm package-local tool configs | `UNKNOWN` | Profile completeness |
| LINT-015 | Confirm root/package precedence | `NEEDS VERIFICATION` | Determinism |
| LINT-016 | Confirm tool and plugin versions | `NEEDS VERIFICATION` | Reproducibility |
| LINT-017 | Confirm inspected source scopes | `NEEDS VERIFICATION` | Interpretation |
| LINT-018 | Confirm changed-file behavior | `NEEDS VERIFICATION` | Gate meaning |
| LINT-019 | Confirm generated/vendored exclusions | `NEEDS VERIFICATION` | Denominator integrity |
| LINT-020 | Confirm no-network posture | `NEEDS VERIFICATION` | Hermeticity |
| LINT-021 | Confirm dirty-tree behavior | `NEEDS VERIFICATION` | Source identity |
| LINT-022 | Confirm formatter mutation policy | `NEEDS VERIFICATION` | Source safety |
| LINT-023 | Confirm type strictness | `NEEDS VERIFICATION` | Result meaning |
| LINT-024 | Confirm severity normalization | `NEEDS VERIFICATION` | Cross-tool review |
| LINT-025 | Confirm stable finding fingerprint | `NEEDS VERIFICATION` | Suppression tracking |
| LINT-026 | Confirm suppression owner and expiry | `NEEDS VERIFICATION` | Governance |
| LINT-027 | Confirm baseline adoption policy | `NEEDS VERIFICATION` | Debt transparency |
| LINT-028 | Confirm threshold owners | `NEEDS VERIFICATION` | Gate authority |
| LINT-029 | Confirm zero/new-finding policy | `NEEDS VERIFICATION` | CI behavior |
| LINT-030 | Confirm native output formats | `NEEDS VERIFICATION` | Data fidelity |
| LINT-031 | Confirm normalized finding schema | `NEEDS VERIFICATION` | Machine interoperability |
| LINT-032 | Confirm run-manifest schema home | `NEEDS VERIFICATION` | Directory Rules |
| LINT-033 | Confirm cross-format validator | `NEEDS VERIFICATION` | Consistency |
| LINT-034 | Confirm placeholder/stale-output detection | `NEEDS VERIFICATION` | Non-vacuity |
| LINT-035 | Confirm path normalization | `NEEDS VERIFICATION` | Privacy/reproducibility |
| LINT-036 | Confirm secret/private-endpoint scanning | `NEEDS VERIFICATION` | Security |
| LINT-037 | Confirm source-excerpt policy | `NEEDS VERIFICATION` | Exposure |
| LINT-038 | Confirm SARIF routing and access | `NEEDS VERIFICATION` | Security findings |
| LINT-039 | Confirm external lint-service posture | `UNKNOWN` | Data egress |
| LINT-040 | Confirm pre-commit installation/activation | `UNKNOWN` | Local enforcement |
| LINT-041 | Confirm substantive CI workflow | `NEEDS VERIFICATION` | Automation |
| LINT-042 | Confirm branch-protection significance | `UNKNOWN` | Gate authority |
| LINT-043 | Confirm CI artifact naming | `NEEDS VERIFICATION` | Traceability |
| LINT-044 | Confirm retention and expiry | `NEEDS VERIFICATION` | Storage/privacy |
| LINT-045 | Confirm canonical receipt binding | `NEEDS VERIFICATION` | Auditability |
| LINT-046 | Confirm release consumer behavior | `UNKNOWN` | Promotion safety |
| LINT-047 | Confirm correction consumers | `UNKNOWN` | Propagation |
| LINT-048 | Test invalidation and withdrawal | `NEEDS VERIFICATION` | Incident response |
| LINT-049 | Test documentation rollback | `PROPOSED` | Reversibility |
| LINT-050 | Confirm production/public use is absent | `UNKNOWN` | Boundary verification |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation | Effect on this README |
|---|---|---|
| `artifacts/qa/lint/README.md` prior blob | v0.1 broad proposed contract | Preserved boundary; grounded inventory |
| `ruff.json` | `PROPOSED`, empty `results`, illustrative note | Classified scaffold only |
| `eslint.json` | `PROPOSED`, empty `results`, illustrative note | Classified scaffold only |
| `markdownlint.json` | `PROPOSED`, empty `results`, illustrative note | Classified scaffold only |
| `mypy.txt` | Says no type-check run recorded | Classified scaffold only |
| `artifacts/qa/README.md` | QA output is non-authoritative and regenerable | Confirms parent placement |
| `package.json` | Root `lint` script echoes TODO | No operational JS lint command |
| `pyproject.toml` | No root Ruff/Mypy dependency or tool block | Python lint/type profile not established |
| `.pre-commit-config.yaml` | Greenfield placeholder with basic hooks | Presence does not prove activation |
| `.gitignore` | Only direct `artifacts/qa/*.xml` ignored | Nested JSON/TXT outputs unprotected |
| `tools/validators/docs/README.md` | Proposed docs-validator parent, executables unverified | Separates docs semantic validation from generic lint |
| Bounded search | No operational Ruff/ESLint/Mypy producer surfaced | Producer remains unestablished |
| Exact path checks | Config/workflow/manifest/schema candidates absent | Proposed implementation remains unverified |

### Evidence limitations

This ledger does not prove:

- an exhaustive recursive repository search;
- package-local tool installation;
- editor or local pre-commit behavior;
- external service behavior;
- current CI status;
- branch protection;
- active consumers;
- historical outputs;
- production use.

[Back to top](#top)

---

## No-loss assessment

The prior README correctly established that:

- this is a compatibility QA-output lane;
- lint output is generated and non-authoritative;
- source, configs, workflows, receipts, proofs, release records, and published artifacts belong elsewhere;
- reports should identify source refs, tools, and rule configurations;
- sensitive paths and deployment values must not be exposed;
- release significance requires canonical records.

This revision preserves those constraints and adds current-session evidence:

- the actual four tracked placeholders;
- their explicit scaffold semantics;
- the TODO-only root lint command;
- the placeholder pre-commit posture;
- missing root tool profiles and dedicated workflow;
- generated-output ignore conflict;
- non-vacuity, suppression, baseline, cross-format, security, retention, correction, and rollback contracts.

No implementation is claimed beyond inspected evidence.

[Back to top](#top)

---

## Documentation correction and rollback

This revision changes only `artifacts/qa/lint/README.md`.

Before merge:

- close the draft pull request; or
- restore prior blob `b28c8c9d0f602340566ab6983522c635a45c181c` in a transparent follow-up commit.

After merge:

- revert the documentation commit; or
- publish a corrective evidence-grounded revision.

No source, test, lint tool, profile, placeholder, workflow, receipt, proof, release, deployment, or production rollback is required for this documentation-only change.

---

`artifacts/qa/lint/` is currently a mixed-scaffold compatibility lane. Its tracked files document intended output families, but they do not establish that any Ruff, ESLint, Markdownlint, Mypy, formatter, static-analysis, or CI lint run has occurred. Treat every result as `PLACEHOLDER_ONLY` until a versioned producer, declared scope, accepted profiles, validated outputs, and canonical run identity exist.

<p align="right"><a href="#top">Back to top</a></p>
