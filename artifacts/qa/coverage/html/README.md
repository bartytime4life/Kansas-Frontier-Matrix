<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-coverage-html-readme
title: artifacts/qa/coverage/html/ — HTML Coverage Browser Output, Inspection, and Non-Authority Boundary
type: readme; directory-readme; qa-output; html-coverage-browser; compatibility-boundary; inspection-contract
version: v0.1
status: draft; repository-grounded; compatibility-root; transitional; readme-and-gitkeep-tracked; html-report-not-present; coverage-producer-not-established; pytest-cov-not-declared; coverage-config-not-established; threshold-not-established; workflow-not-established; retention-not-established; non-authoritative
owners: OWNER_TBD — QA steward · Test steward · Coverage steward · Security/privacy steward · CI steward · Build steward · Release steward · Docs steward
created: 2026-07-16
updated: 2026-07-16
policy_label: public-doc; artifacts; qa; coverage; html; generated-output; inspection-only; no-secrets; no-trust-authority; no-release-authority; correction-aware; rollback-aware
current_path: artifacts/qa/coverage/html/README.md
truth_posture: CONFIRMED target README existed as an empty tracked file, sibling .gitkeep exists and states that it retains the proposed human-readable coverage-browser directory, parent artifacts/qa and artifacts/qa/coverage boundaries, root artifacts compatibility classification, root pyproject test extra declaring pytest but not pytest-cov, Makefile test targets running pytest without coverage options, contracts-validate workflow invoking make test, policy-boundary-guards workflow uploading JUnit XML rather than coverage HTML, root .gitignore ignoring only direct artifacts/qa/*.xml and not this nested HTML lane, bounded search surfacing no HTML coverage payload or producer, and checked absence of index.html, .coveragerc, and .github/workflows/coverage-html.yml / PROPOSED explicit coverage scope, branch coverage, threshold policy, omission policy, normalized source mapping, stable report metadata, producer command, coverage manifest, validator, CI artifact upload, access and expiry controls, source-excerpt redaction, receipt binding, correction, and retirement procedure / CONFLICTED parent coverage README presenting htmlcov as a typical accepted output while no generator or dependency is established; tracked placeholder versus generated-output lifecycle; HTML source excerpts versus source/privacy exposure; coverage percentage convenience versus correctness and release significance; and local browser output versus canonical QA/run records / UNKNOWN uncommitted local reports, CI-only reports, external coverage services, package-local coverage tooling, actual measured modules, current line or branch coverage, active consumers, branch-protection significance, report freshness, retention, hosting, and production use / NEEDS VERIFICATION accepted owners, CODEOWNERS, complete recursive inventory, generated-output commit policy, coverage tool and version, source scope, test selection, branch coverage, concurrency/subprocess behavior, omit/include patterns, threshold ownership, path normalization, source-code rendering policy, secret and private-path scanning, workflow ownership, artifact retention, receipt/proof linkage, release significance, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ca991f25b42bf4fe7ee801db681581ba234d886d
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  confirmed_lane_files:
    - artifacts/qa/coverage/html/README.md
    - artifacts/qa/coverage/html/.gitkeep
  checked_absent_paths:
    - artifacts/qa/coverage/html/index.html
    - .coveragerc
    - .github/workflows/coverage-html.yml
  execution_surfaces:
    - pyproject.toml
    - Makefile
    - .github/workflows/contracts-validate.yml
    - .github/workflows/policy-boundary-guards.yml
    - .gitignore
  bounded_inventory_note: tracked repository evidence cannot establish uncommitted local coverage trees, CI workspaces, package-local ignored outputs, external coverage services, historical artifacts, or uninspected subprojects
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../tests/README.md
  - ../../../../../pyproject.toml
  - ../../../../../Makefile
  - ../../../../../.github/workflows/contracts-validate.yml
  - ../../../../../.github/workflows/policy-boundary-guards.yml
  - ../../../../../.gitignore
  - ../../../../../data/receipts/README.md
  - ../../../../../data/proofs/README.md
  - ../../../../../release/README.md
tags: [kfm, artifacts, qa, coverage, htmlcov, pytest, pytest-cov, line-coverage, branch-coverage, source-mapping, security, privacy, retention, ci-artifact, non-authoritative]
notes:
  - "This is the first substantive contract for an otherwise empty README."
  - "The lane contains only README.md and .gitkeep in bounded tracked evidence."
  - "No HTML coverage producer, coverage dependency, threshold, configuration, workflow, payload, or consumer was established."
  - "The root ignore rules do not protect this nested lane from accidental generated-report commits."
  - "Coverage percentage is inspection evidence about execution, not proof of correctness, policy compliance, evidence support, or release readiness."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `artifacts/qa/coverage/html/` — HTML Coverage Browser Output, Inspection, and Non-Authority Boundary

> **Purpose.** Define the staging boundary for generated, human-browsable coverage output without allowing an HTML report, percentage, green badge, workflow artifact, or opened browser page to become test authority, proof of correctness, policy compliance, evidence closure, release approval, publication, or production truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: artifacts compatibility" src="https://img.shields.io/badge/root-artifacts__compatibility-orange">
  <img alt="Direct inventory: README and gitkeep" src="https://img.shields.io/badge/direct__inventory-README%20%2B%20gitkeep-informational">
  <img alt="Producer: not established" src="https://img.shields.io/badge/producer-not__established-red">
  <img alt="Coverage: not measured" src="https://img.shields.io/badge/coverage-NOT__MEASURED-critical">
  <img alt="Authority: none" src="https://img.shields.io/badge/trust__authority-none-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-audience) · [Authority](#authority-and-directory-rules-basis) · [Inventory](#confirmed-current-inventory) · [Meaning](#what-html-coverage-can-and-cannot-mean) · [Inputs](#measurement-input-contract) · [Output](#html-output-contract) · [Security](#security-privacy-and-source-exposure) · [Producer](#producer-contract) · [CI](#ci-artifact-access-and-retention) · [Validation](#validation-and-finite-outcomes) · [Trust](#receipt-proof-release-and-publication-boundary) · [Correction](#correction-invalidation-and-rollback) · [Done](#definition-of-done) · [Plan](#smallest-sound-implementation-sequence) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Snapshot:** `main@ca991f25b42bf4fe7ee801db681581ba234d886d`<br>
> **Prior README blob:** `8b137891791fe96927ad78e64b0aad7bded08bdc` — empty file<br>
> **Confirmed direct files:** `README.md`, `.gitkeep`<br>
> **HTML report payload:** not established<br>
> **Coverage tool, configuration, threshold, workflow, and consumer:** not established<br>
> **Generated-output ignore protection:** not established

`artifacts/qa/coverage/html/` is a repository-confirmed compatibility placeholder. It is **not an operational coverage-reporting system**.

### Safe conclusion

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Boundary README | `CONFIRMED` | The path existed, but its README was empty before this revision. |
| Directory retention marker | `CONFIRMED` | `.gitkeep` identifies the lane as a proposed human-readable coverage-browser directory. |
| Generated `index.html` | `NOT ESTABLISHED` | The checked canonical entry page is absent. |
| Coverage producer | `NOT ESTABLISHED` | No accepted command or writer surfaced. |
| Coverage dependency | `NOT ESTABLISHED` | Root test extras declare `pytest`, not `pytest-cov`. |
| Root test command | `NO COVERAGE` | `make test` runs selected tests without coverage options. |
| Contract validation workflow | `NO COVERAGE` | It invokes `make test`. |
| Boundary workflow | `JUNIT ONLY` | It uploads a JUnit XML report, not HTML coverage. |
| Coverage configuration | `NOT ESTABLISHED` | Checked root `.coveragerc` is absent. |
| Coverage threshold | `NOT ESTABLISHED` | No line or branch threshold was verified. |
| Branch coverage | `NOT ESTABLISHED` | No branch-measurement policy was verified. |
| Source scope | `NOT ESTABLISHED` | No canonical include/omit package set was verified. |
| Report freshness | `UNKNOWN` | No payload exists in tracked evidence. |
| CI artifact retention | `NOT ESTABLISHED` | No coverage-specific upload or expiry policy surfaced. |
| Receipt/proof/release binding | `NOT ESTABLISHED` | No canonical record was linked to this lane. |
| Correctness or release proof | `DENY` | Coverage cannot prove behavior is correct or releasable. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, exact paths, or bounded search. |
| `PROPOSED` | A recommended command, structure, policy, threshold, or gate not established as current implementation. |
| `CONFLICTED` | Current files or documentation create incompatible expectations. |
| `UNKNOWN` | Not observable or not established from inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently proven for operational reliance. |
| `DENY` | A prohibited trust, correctness, security, release, or publication interpretation. |

[Back to top](#top)

---

## Purpose and audience

This README governs generated HTML coverage-browser output for maintainers who need to inspect which executable lines or branches were observed during a bounded test run.

It is intended for:

- test, QA, and coverage stewards;
- application, package, connector, pipeline, runtime, and tooling maintainers;
- CI and artifact-retention maintainers;
- security and privacy reviewers inspecting rendered source excerpts and paths;
- reviewers evaluating test gaps without confusing execution with correctness;
- receipt, proof, release, correction, and rollback stewards;
- documentation maintainers correcting coverage claims or stale report references.

The durable question is:

> Can a reviewer inspect a precisely scoped coverage run without mistaking the report for test authority, complete behavioral verification, policy enforcement, or a release decision?

A correct answer is bounded. A report can show 100% measured line coverage and still miss:

- incorrect assertions;
- missing negative cases;
- vacuous or tautological tests;
- incorrect requirements;
- untested combinations;
- race conditions;
- real external integrations;
- policy-significant denial paths;
- sensitivity and rights failures;
- deployment-specific behavior;
- semantic, accessibility, security, or data-quality defects.

[Back to top](#top)

---

## Authority and Directory Rules basis

`artifacts/` is a transitional compatibility root for derived, regenerable, non-authoritative material. This HTML lane inherits that classification through `artifacts/qa/coverage/`.

```text
source code and tests                     authority and executable inputs
pyproject / package configs              test and tool declarations
CI workflows and Make targets            orchestration
artifacts/qa/coverage/html/               generated browser output only
data/receipts/ and data/proofs/           canonical run memory and evidence support
release/                                  governed release decisions
```

This directory may contain rendered coverage pages and their static assets. It must not become:

- a source-test or source-code home;
- a coverage-policy authority;
- a CI configuration home;
- a canonical test-run receipt;
- a proof or EvidenceBundle home;
- a release gate or promotion record;
- a public documentation or deployment surface;
- a permanent archive of source excerpts;
- a shortcut around governed review.

### Placement decision

The target path is appropriate for **HTML rendering of coverage inspection output** because:

1. the owning responsibility root is `artifacts/`;
2. the parent role is QA output;
3. the grandparent role is coverage export;
4. the child role is the human-browsable HTML representation;
5. canonical meaning, policy, orchestration, and release decisions remain outside this lane.

No new root, parallel coverage authority, schema home, release home, or proof home is created.

[Back to top](#top)

---

## Confirmed current inventory

Bounded tracked evidence supports:

```text
artifacts/qa/coverage/html/
├── README.md
└── .gitkeep
```

The `.gitkeep` states that it retains a proposed human-readable coverage-browser directory.

Checked absent:

```text
artifacts/qa/coverage/html/index.html
.coveragerc
.github/workflows/coverage-html.yml
```

Also confirmed:

- root `pyproject.toml` declares `pytest` in the `test` extra but does not declare `pytest-cov`;
- `make test` runs `tests/schemas` and `tests/contracts` without coverage options;
- `contracts-validate.yml` installs the test extra and invokes `make test`;
- `policy-boundary-guards.yml` emits and uploads JUnit XML only;
- root `.gitignore` ignores `artifacts/qa/*.xml`, but that direct-child XML pattern does not protect this nested HTML tree;
- no tracked `index.html` or static coverage asset tree was surfaced.

> [!WARNING]
> Because this lane is tracked and lacks an established generated-output ignore rule, a local HTML report can be accidentally committed. Generated pages often include source excerpts, file paths, tool metadata, and large static asset trees. Commit retention must be an explicit reviewed decision, never the incidental result of running a tool.

[Back to top](#top)

---

## Relationship to parent and sibling lanes

| Lane | Role | Boundary |
|---|---|---|
| `artifacts/qa/` | Parent QA compatibility lane | Generated inspection copies only. |
| `artifacts/qa/coverage/` | Coverage output parent | Routes HTML, XML, JSON, LCOV, summaries, and run metadata. |
| **`artifacts/qa/coverage/html/`** | Human-browsable coverage rendering | Generated pages and assets only. |
| `artifacts/qa/reports/` | Structured QA summaries | Do not duplicate coverage page trees here. |
| `artifacts/qa/validation/` | Validator inspection copies | Not a coverage browser. |
| `tests/` and package-local tests | Source tests and fixtures | Canonical test definitions remain outside artifacts. |
| `.github/workflows/` | CI orchestration | Coverage policy and execution do not live here. |
| `data/receipts/` | Canonical run/process memory | May cite a report digest; never replaced by HTML. |
| `data/proofs/` | Evidence support | Coverage pages are not proofs. |
| `release/` | Promotion and release decisions | Release significance is decided elsewhere. |

### Representation rule

HTML coverage is a **representation** of measured execution data. If a machine-readable coverage export is retained, the HTML tree should identify which export and run generated it. The HTML copy must not silently diverge from the corresponding machine-readable result.

[Back to top](#top)

---

## What HTML coverage can and cannot mean

### It can help answer

- Which measured files were included?
- Which executable lines were observed by the selected test run?
- Which measured branches were observed, when branch coverage is enabled?
- Which lines or branches were missed?
- Which files have unusually low measured coverage?
- Did the report include expected packages and modules?
- Are generated files, migrations, or adapters being measured unintentionally?
- Are test gaps concentrated in policy-significant or error-handling paths?

### It cannot establish

| Unsupported inference | Why it fails |
|---|---|
| “Covered code is correct.” | Execution does not prove assertions were meaningful. |
| “100% means complete testing.” | Coverage does not enumerate inputs, states, properties, or requirements. |
| “The full repository was measured.” | Scope may include only selected tests or packages. |
| “Policy behavior is enforced.” | Coverage does not prove deny/abstain semantics or policy correctness. |
| “External integrations work.” | Mocks and local substitutes may dominate the run. |
| “No security defects exist.” | Coverage is not static analysis, threat modeling, or penetration testing. |
| “Sensitive data is safe.” | Coverage does not prove redaction, rights, consent, or geoprivacy. |
| “The PR is releasable.” | Release requires governed validation, evidence, review, and release state. |
| “A stale report describes current code.” | Source and report revisions may differ. |
| “A green page is canonical.” | The canonical objects are source, tests, configs, receipts, proofs, and release records elsewhere. |

### Coverage-quality anti-patterns

Reviewers should reject:

- threshold-only gaming through broad omissions;
- measuring only trivial modules;
- excluding failing tests while publishing a report;
- treating import execution as behavioral validation;
- ignoring branch coverage for decision-heavy code without explanation;
- generating a report after tests failed and presenting it as a pass;
- merging reports from incompatible commits or configurations;
- publishing percentages without denominator and scope;
- comparing percentages across different include/omit policies;
- using HTML color alone as the status signal;
- retaining a report without source `git_sha` and run identity.

[Back to top](#top)

---

## Measurement input contract

A future producer should close these inputs before generating HTML.

### Required run identity

| Field | Requirement |
|---|---|
| `run_id` | Stable identifier for the coverage run. |
| `source_git_sha` | Exact commit measured. |
| `dirty_tree` | Explicit boolean; dirty runs must be labeled local/non-comparable. |
| `test_command` | Exact command and arguments. |
| `test_targets` | Explicit files, directories, markers, or packages selected. |
| `coverage_tool` | Tool name and version. |
| `test_runner` | Runner name and version. |
| `python_or_runtime` | Runtime version and implementation. |
| `platform` | Normalized OS/container identity where material. |
| `started_at` / `completed_at` | Run timing; not a substitute for immutable identity. |
| `result` | Test and coverage outcome with finite vocabulary. |

### Required scope identity

A useful report must state:

- measured source roots;
- package/module include patterns;
- omit patterns and reasons;
- whether test files are measured;
- whether generated code is excluded;
- whether branch coverage is enabled;
- whether subprocess and concurrency collection are enabled;
- whether plugins or dynamic imports affect collection;
- whether xfailed, skipped, deselected, or quarantined tests were present;
- whether failed tests contributed data;
- whether multiple data files were combined;
- whether the run is repository-wide, suite-specific, package-specific, or PR-specific.

### Test-result closure

HTML generation must not conceal the test outcome. A report built from a failed or interrupted test run may be retained for debugging, but it must be labeled `FAILED_RUN` or `INCOMPLETE`, never `PASS`.

### Non-vacuity requirements

A coverage run must fail or abstain when:

- no test was collected unexpectedly;
- no source file was measured unexpectedly;
- the measured denominator is zero;
- expected packages are absent;
- report generation succeeds after the measurement file is missing;
- thresholds are evaluated against a different scope than the displayed report;
- a stale data file is reused without explicit opt-in;
- the source commit differs from the recorded run commit.

[Back to top](#top)

---

## HTML output contract

### Accepted generated contents

| Content | Example | Posture |
|---|---|---|
| Entry page | `index.html` | Generated browser landing page. |
| Per-file pages | hashed or path-derived `.html` pages | Generated source/coverage views. |
| Static styles and scripts | CSS, JavaScript, icons | Local report assets only. |
| Status metadata | tool-generated status JSON or equivalent | Non-authoritative; source run remains external. |
| Key or function indexes | tool-generated index pages | Inspection aids. |
| Optional manifest | `coverage-html-manifest.json` | `PROPOSED`; binds run, source, and tree digest. |
| README and `.gitkeep` | repository-maintained boundary files | Human contract and directory marker. |

### Forbidden contents

| Do not place here | Correct home |
|---|---|
| Source tests or fixtures | `tests/` or package-local test roots |
| Source code of record | application, package, connector, pipeline, runtime, or tool roots |
| Coverage policy or thresholds | accepted config/contract location outside artifacts |
| CI workflows | `.github/workflows/` |
| Run receipts or validation records | `data/receipts/` |
| EvidenceBundle, proof, or attestation | `data/proofs/` |
| ReleaseManifest, approval, rollback, or correction record | `release/` |
| Published QA documentation | governed publication lane after release, if ever required |
| Secrets, credentials, tokens, or private endpoints | never serialize; use protected secret channels |
| Restricted source excerpts or sensitive file paths | protected review channels only |
| Hand-edited replacements for generated pages | fix the producer or source and regenerate |

### Tree integrity

A retained HTML tree should be treated as one unit. Review or upload must not include an `index.html` while omitting required styles, scripts, per-file pages, or metadata.

A future manifest should include:

```json
{
  "schema_version": "PROPOSED",
  "run_id": "<stable-run-id>",
  "source_git_sha": "<40-hex-sha>",
  "test_command": "<exact-command>",
  "coverage_tool": {"name": "<tool>", "version": "<version>"},
  "scope": {
    "source_roots": ["<path>"],
    "test_targets": ["<path>"],
    "branch": true,
    "include": [],
    "omit": []
  },
  "test_result": "<PASS|FAIL|INCOMPLETE>",
  "coverage_result": "<PASS|FAIL|HOLD|ABSTAIN|ERROR>",
  "summary": {
    "lines_total": 0,
    "lines_covered": 0,
    "branches_total": 0,
    "branches_covered": 0
  },
  "html_entrypoint": "index.html",
  "tree_digest": "sha256:<digest>",
  "canonical_refs": []
}
```

This manifest is `PROPOSED`; no current schema or producer is established.

[Back to top](#top)

---

## Determinism, comparability, and freshness

HTML coverage trees are often not byte-reproducible by default. They may include timestamps, tool-version-specific layouts, hashed asset names, absolute paths, or generated identifiers.

### Required comparison posture

Separate:

1. **measurement equivalence** — same measured files, statements, branches, and counts;
2. **semantic report equivalence** — same source/run mapping and outcomes;
3. **byte identity** — identical HTML and asset bytes.

Byte identity may be desirable but is not required to establish equivalent coverage measurement. The chosen comparison level must be declared.

### Freshness controls

A report is stale when any material input changes without regeneration, including:

- source commit;
- test commit;
- test selection;
- include/omit policy;
- branch-coverage setting;
- coverage or test-runner version;
- runtime version;
- environment or dependency lock;
- subprocess/concurrency collection;
- generated-code policy;
- threshold.

A stale report must be labeled, removed, or regenerated. It must not remain linked as current.

[Back to top](#top)

---

## Security, privacy, and source exposure

HTML coverage can expose more than percentages.

### Common exposure classes

- absolute user-home and workspace paths;
- usernames, hostnames, runner labels, and container paths;
- internal module names and repository layout;
- source excerpts containing embedded credentials or test secrets;
- private endpoints or infrastructure names in code;
- names of restricted datasets, fixtures, or connectors;
- exception text and generated comments;
- browser-executable JavaScript in report assets;
- source maps or links to internal files;
- dependency/tool version fingerprints;
- file names that reveal sensitive workstreams.

### Required controls

A future producer or uploader should:

- use an explicit allowlist of measured source roots;
- normalize repository-relative paths;
- deny user-home and runner-specific path leakage;
- scan rendered text and source excerpts for credential patterns;
- verify that test fixtures contain no protected or production data;
- avoid network-loaded assets;
- avoid embedding external analytics or trackers;
- inspect JavaScript and active content;
- set artifact access according to repository sensitivity;
- expire debugging reports automatically;
- prohibit public hosting unless separately reviewed and released;
- record whether source excerpts are included;
- support a source-excerpt-disabled profile when needed.

> [!CAUTION]
> `.gitignore` is not a confidentiality control. A generated report can be manually added, uploaded as a CI artifact, copied to a web server, or attached to an issue. Safety must be enforced before persistence or sharing.

[Back to top](#top)

---

## Producer contract

No producer is currently established. A future producer belongs in an implementation root such as `tools/`, a package, or a workflow—not in this output directory.

### Producer obligations

The producer should:

1. resolve the exact source commit and dirty-tree state;
2. resolve test targets and measured source roots;
3. install or verify pinned runner and coverage tool versions;
4. remove or isolate stale coverage data;
5. execute tests and preserve the test outcome;
6. collect line and, where required, branch data;
7. validate nonempty collection and expected scope;
8. apply accepted include/omit policy;
9. generate machine-readable output before or alongside HTML;
10. render the complete HTML tree;
11. scrub paths, source excerpts, and sensitive metadata;
12. create a run/manifest record;
13. calculate a tree or archive digest where material;
14. upload or retain the tree under an explicit retention class;
15. emit canonical receipts elsewhere when governance significance requires it.

### Proposed command profile

The following is an example only and is **not a current repository command**:

```bash
python -m pytest \
  <explicit-test-targets> \
  --cov=<explicit-source-package> \
  --cov-branch \
  --cov-report=term-missing \
  --cov-report=xml:artifacts/qa/coverage/coverage.xml \
  --cov-report=html:artifacts/qa/coverage/html
```

This requires a coverage plugin that is not currently declared by the root test extra. Do not copy this command into CI until dependency, scope, thresholds, exclusions, and retention are governed.

### Producer failure posture

| Condition | Outcome |
|---|---|
| Tests fail | `FAIL`; HTML may be debug-only and labeled. |
| No tests collected unexpectedly | `ERROR` or `ABSTAIN`; never pass. |
| No source measured | `ERROR`; no valid report. |
| Expected package missing | `HOLD`; investigate scope. |
| Threshold missed | `FAIL` when threshold is authoritative. |
| Report rendering fails after valid measurement | `ERROR`; machine export may remain. |
| Secret/path scan fails | `DENY`; do not persist or upload. |
| Source commit mismatch | `DENY`; regenerate. |
| Coverage tool unavailable | `ERROR`; do not synthesize results. |

[Back to top](#top)

---

## CI artifact, access, and retention

No coverage-specific workflow is established.

### Current workflow evidence

- `contracts-validate.yml` installs root test dependencies and invokes `make test`;
- `make test` runs selected schema and contract tests without coverage;
- `policy-boundary-guards.yml` emits a JUnit XML report to `artifacts/qa/`;
- no checked `.github/workflows/coverage-html.yml` exists.

### Proposed CI separation

A future workflow should separate:

1. **test execution**;
2. **coverage measurement**;
3. **threshold evaluation**;
4. **HTML rendering**;
5. **security/path scanning**;
6. **artifact upload**;
7. **receipt or status emission**.

A failed upload must not change a valid coverage measurement into a pass or fail. Conversely, a successful upload must not override failed tests or missed thresholds.

### Retention classes

| Class | Use | Default posture |
|---|---|---|
| PR debugging | Reviewer inspection for one PR | Short-lived, access-controlled. |
| Main-branch trend | Approved comparison snapshot | Retain only with stable scope and explicit owner. |
| Release support | Coverage evidence referenced by release review | Canonical receipt must bind source/run/digest elsewhere. |
| Local developer report | Browser inspection | Untracked and disposable by default. |
| Incident/debug report | Temporary forensic support | Restricted, time-limited, source-excerpt reviewed. |

### Hosting boundary

An uploaded CI artifact is not a public website. A preview URL is not a released artifact. Public hosting would require:

- source and run identity;
- security and privacy review;
- accessibility review of the hosting surface where material;
- rights review for displayed source;
- release decision;
- correction and removal path;
- expiry or supersession policy.

[Back to top](#top)

---

## Threshold and trend policy

No threshold is currently established.

### Threshold requirements

Before a threshold becomes a gate, define:

- owning steward;
- measured source scope;
- line and branch metrics;
- global versus per-package thresholds;
- treatment of new/changed lines;
- excluded files and reasons;
- rounding behavior;
- fail-under semantics;
- handling of unreachable or platform-specific code;
- handling of generated code;
- baseline migration;
- exception process;
- expiry of exceptions;
- required-check or advisory status.

### Trend integrity

Do not compare percentages across runs unless scope and configuration are compatible. A percentage increase can result from deleting difficult files, adding omissions, or measuring a smaller package.

Trend records should compare:

- numerator and denominator;
- included files;
- omitted files;
- branch setting;
- tool version;
- test selection;
- source commit;
- exception set.

[Back to top](#top)

---

## Validation and finite outcomes

A validator for this lane is `PROPOSED`; none is established.

### Required validation layers

| Layer | Example checks |
|---|---|
| Inventory | Entry page and referenced assets exist. |
| Run identity | Source SHA, test command, tool version, and scope are present. |
| Non-vacuity | Tests and measured source are nonempty. |
| Consistency | HTML summary agrees with machine-readable export. |
| Path safety | Paths are repository-relative and scrubbed. |
| Secret safety | No credential or protected-value patterns. |
| Scope | Expected packages are present; prohibited roots absent. |
| Threshold | Declared metric and rounding semantics applied. |
| Freshness | Report inputs match current referenced run. |
| Tree integrity | No missing pages, styles, scripts, or indexes. |
| Authority | No receipt, proof, release decision, or authored source stored here. |
| Retention | Access and expiry class are declared. |

### Finite outcome vocabulary

| Outcome | Meaning |
|---|---|
| `PASS` | Tests, measurement, report, safety, and declared threshold checks passed. |
| `FAIL` | Tests or authoritative coverage threshold failed. |
| `HOLD` | Report exists, but scope, freshness, review, or retention closure is incomplete. |
| `ABSTAIN` | Coverage interpretation cannot be made from available evidence. |
| `DENY` | Security, privacy, source exposure, or authority boundary is violated. |
| `ERROR` | Tooling, rendering, collection, or validation malfunctioned. |

Avoid ambiguous statuses such as `OK`, `green`, `mostly covered`, or `good enough`.

### Anti-tautology requirements

A valid check must not merely confirm:

- that the generator wrote files;
- that `index.html` contains the word “coverage”;
- that the total percentage parses as a number;
- that the current output matches a fixture generated by the same unchecked path;
- that every file in the report is present in the report’s own index;
- that a threshold passes because the report omitted the intended source roots.

[Back to top](#top)

---

## Receipt, proof, release, and publication boundary

The HTML report is not a canonical governance object.

```text
tests + code + config
        |
        v
coverage measurement
        |
        +--> machine export
        |
        +--> HTML browser output  [this lane]
        |
        v
validation / review
        |
        +--> data/receipts/       canonical run memory when material
        +--> data/proofs/         evidence support when material
        +--> release/             governed decision if release depends on coverage
```

### Digest semantics

A digest proves byte identity for the digested tree or archive. It does not prove:

- correct scope;
- complete tests;
- meaningful assertions;
- correct policy;
- safe source exposure;
- valid release state;
- current freshness.

### Release significance

Coverage may support a release decision, but release significance must be explicit. A ReleaseManifest or review record should identify:

- the exact source commit;
- exact coverage run;
- measured scope;
- test outcome;
- threshold result;
- report or archive digest;
- known exclusions;
- exception approvals;
- rollback target.

The presence of HTML under `artifacts/` never promotes anything.

[Back to top](#top)

---

## Correction, invalidation, and rollback

Coverage reports can become wrong or misleading after generation.

### Invalidation triggers

Invalidate or supersede a report when:

- source or tests change;
- scope or omit rules change;
- tool versions change materially;
- stale data was reused;
- paths or source excerpts expose protected information;
- test failures were omitted from the displayed status;
- branch coverage was misreported;
- package mapping was incorrect;
- thresholds were evaluated against a different denominator;
- machine-readable and HTML summaries disagree;
- a report was attached to the wrong commit or PR.

### Correction procedure

1. Stop linking or uploading the affected report.
2. Record the source/run identity and nature of the error.
3. Remove or restrict exposed copies where needed.
4. Correct producer configuration or source tests.
5. Regenerate from a clean, pinned run.
6. validate scope, safety, and summary consistency.
7. update any canonical receipt, review, or release reference transparently.
8. preserve the prior digest in correction history when governance significance requires it.

### Rollback target

The rollback target is normally:

- deletion of the generated HTML tree;
- restoration of the prior documentation contract;
- removal of stale CI artifacts or links;
- reversion of any incorrect threshold/configuration change.

Source code or test rollback is a separate decision and must not be inferred from a coverage-report rollback.

[Back to top](#top)

---

## Review burden and change control

### Low-risk documentation change

A wording correction that does not change path, authority, measurement meaning, security posture, retention, or validation semantics may use normal documentation review.

### Elevated review

Require relevant stewards when changing:

- measured source scope;
- include/omit policy;
- branch coverage;
- thresholds;
- exception rules;
- generated source-excerpt policy;
- access or retention;
- report upload or hosting;
- release significance;
- canonical receipt/proof references;
- the lane’s retain/migrate/retire posture.

### Deny-on-review findings

Reject a change that:

- treats percentage as correctness;
- hides failed tests;
- widens omissions without rationale;
- publishes source excerpts without review;
- commits a generated tree accidentally;
- stores receipts, proofs, or release decisions here;
- creates a public endpoint from this directory without governed release;
- claims full-repository coverage from a partial suite;
- marks an advisory report as a required gate without an accepted policy.

[Back to top](#top)

---

## Safe operator checklist

Before generating:

- [ ] Pin source commit and dirty-tree state.
- [ ] Declare test targets and measured source roots.
- [ ] Verify coverage/test tool versions.
- [ ] Clear stale measurement data.
- [ ] Confirm include/omit and branch settings.
- [ ] Confirm source excerpts are permitted.
- [ ] Confirm no protected fixtures or production data are in scope.

Before retaining or uploading:

- [ ] Confirm tests completed and result is visible.
- [ ] Confirm nonempty test and source measurement.
- [ ] Confirm expected packages appear.
- [ ] Compare HTML summary with machine-readable output.
- [ ] Scan paths, source text, scripts, and metadata.
- [ ] Assign access and retention class.
- [ ] Record run/source identity.
- [ ] Calculate digest where material.

Before using in review or release:

- [ ] Confirm report freshness.
- [ ] Confirm scope and exclusions.
- [ ] Confirm threshold authority.
- [ ] Confirm known limitations.
- [ ] Resolve canonical receipt/proof/release references where required.
- [ ] Confirm correction and rollback paths.

[Back to top](#top)

---

## Definition of done

This lane is operational only when all applicable items are closed:

- [ ] Owners and CODEOWNERS are accepted.
- [ ] Generated-output commit and ignore policy is explicit.
- [ ] Coverage tool and version are pinned.
- [ ] Coverage dependency is declared in the correct package/root.
- [ ] Producer command or implementation is accepted.
- [ ] Test targets and measured source roots are explicit.
- [ ] Include/omit and generated-code policies are accepted.
- [ ] Branch, concurrency, and subprocess behavior are defined.
- [ ] Nonempty collection is enforced.
- [ ] Machine-readable export is generated.
- [ ] HTML summary is checked against the machine export.
- [ ] Run identity and source commit are embedded or linked.
- [ ] Path and source-excerpt scrubbing are executable.
- [ ] Secret and sensitive-name scanning is executable.
- [ ] Threshold policy and exception process are accepted.
- [ ] CI workflow and required/advisory status are accepted.
- [ ] Artifact upload access and expiry are accepted.
- [ ] Retention and cleanup are implemented.
- [ ] Canonical receipt/proof/release linkage is defined where material.
- [ ] Correction, invalidation, and rollback are tested.
- [ ] The README and parent coverage/QA docs agree.
- [ ] A real report has been generated and independently inspected.
- [ ] No claim exceeds the verified implementation.

[Back to top](#top)

---

## Smallest sound implementation sequence

### Phase 1 — Decide retention and scope

- assign owners;
- decide local-only versus CI artifact versus tracked output;
- define repository-wide or package-specific scope;
- decide line and branch metrics;
- define initial include/omit policy.

### Phase 2 — Add tool declaration

- add the coverage plugin to the correct dependency surface;
- pin compatible versions;
- add accepted coverage configuration;
- document source and test targets.

### Phase 3 — Implement producer

- clear stale data;
- run explicit tests;
- enforce nonempty collection;
- emit terminal and machine-readable summaries;
- render HTML to this lane or a temporary equivalent.

### Phase 4 — Add safety and integrity checks

- normalize paths;
- scan source excerpts and assets;
- compare HTML with machine export;
- validate complete tree references;
- assign run identity and digest.

### Phase 5 — Add CI and retention

- add path-aware workflow triggers;
- separate tests, measurement, threshold, render, and upload;
- set access and expiry;
- prevent accidental Git commits.

### Phase 6 — Add governance binding

- define when a receipt is required;
- define whether coverage is advisory or release-significant;
- link immutable digests from canonical records;
- document exceptions and expiry.

### Phase 7 — Exercise correction and rollback

- generate a known stale/mismatched report;
- prove validators reject it;
- remove uploaded copies;
- regenerate;
- verify correction and rollback records.

Each phase is independently reversible and should not promote the lane to authority.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status | Why it matters |
|---|---|---:|---|
| COVHTML-01 | Confirm accepted owners and CODEOWNERS | `NEEDS VERIFICATION` | Establishes review responsibility. |
| COVHTML-02 | Confirm complete recursive tracked inventory | `NEEDS VERIFICATION` | Prevents hidden payload assumptions. |
| COVHTML-03 | Decide generated-output commit policy | `NEEDS VERIFICATION` | Prevents repository bloat and accidental source exposure. |
| COVHTML-04 | Decide ignore rule for generated pages/assets | `NEEDS VERIFICATION` | Current root rule does not protect this lane. |
| COVHTML-05 | Select coverage tool and version | `NEEDS VERIFICATION` | No root plugin is declared. |
| COVHTML-06 | Select configuration home | `NEEDS VERIFICATION` | Root `.coveragerc` is absent. |
| COVHTML-07 | Define measured source roots | `NEEDS VERIFICATION` | Percentage is meaningless without denominator scope. |
| COVHTML-08 | Define test targets | `NEEDS VERIFICATION` | Current `make test` is partial. |
| COVHTML-09 | Define line versus branch metrics | `NEEDS VERIFICATION` | Decision-heavy code needs explicit branch posture. |
| COVHTML-10 | Define include/omit policy | `NEEDS VERIFICATION` | Omissions can game results. |
| COVHTML-11 | Define generated-code policy | `NEEDS VERIFICATION` | Generated files can distort totals. |
| COVHTML-12 | Define subprocess/concurrency collection | `NEEDS VERIFICATION` | Missing child processes undercounts execution. |
| COVHTML-13 | Define skipped/xfail/deselected treatment | `NEEDS VERIFICATION` | Test outcome context affects interpretation. |
| COVHTML-14 | Define failed-run report policy | `NEEDS VERIFICATION` | Debug reports must not look like passes. |
| COVHTML-15 | Define threshold ownership and semantics | `NEEDS VERIFICATION` | No gate is established. |
| COVHTML-16 | Define changed-lines or diff coverage posture | `NEEDS VERIFICATION` | Global coverage may hide new gaps. |
| COVHTML-17 | Implement nonempty collection checks | `PROPOSED` | Prevents vacuous passes. |
| COVHTML-18 | Implement HTML/machine-summary consistency check | `PROPOSED` | Prevents representation drift. |
| COVHTML-19 | Define source-excerpt rendering policy | `NEEDS VERIFICATION` | HTML may expose source text. |
| COVHTML-20 | Implement path normalization | `PROPOSED` | Prevents private runner-path leakage. |
| COVHTML-21 | Implement secret and sensitive-name scanning | `PROPOSED` | Prevents unsafe persistence. |
| COVHTML-22 | Define browser-script and external-asset policy | `NEEDS VERIFICATION` | Reports include executable assets. |
| COVHTML-23 | Define CI workflow and triggers | `NEEDS VERIFICATION` | No coverage workflow is established. |
| COVHTML-24 | Decide advisory versus required-check status | `NEEDS VERIFICATION` | Workflow presence is not gate significance. |
| COVHTML-25 | Define artifact access controls | `NEEDS VERIFICATION` | Source excerpts may be sensitive. |
| COVHTML-26 | Define retention and expiry | `NEEDS VERIFICATION` | Stale reports create drift and exposure. |
| COVHTML-27 | Define local cleanup command | `PROPOSED` | Regenerable outputs should be easy to delete. |
| COVHTML-28 | Define run manifest/schema home | `NEEDS VERIFICATION` | Meaning and shape belong outside artifacts. |
| COVHTML-29 | Define canonical receipt linkage | `NEEDS VERIFICATION` | HTML must not substitute for process memory. |
| COVHTML-30 | Define release significance | `NEEDS VERIFICATION` | Coverage is not automatically a release gate. |
| COVHTML-31 | Define trend-baseline compatibility rules | `NEEDS VERIFICATION` | Percentages need stable scope. |
| COVHTML-32 | Define correction and invalidation consumers | `NEEDS VERIFICATION` | Stale links and artifacts must be removable. |
| COVHTML-33 | Test rollback and report deletion | `PROPOSED` | Proves reversibility. |
| COVHTML-34 | Resolve retain/migrate/externalize/retire posture | `NEEDS VERIFICATION` | Compatibility roots should not drift indefinitely. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation | Status |
|---|---|---:|
| `artifacts/qa/coverage/html/README.md` | File existed and was empty. | `CONFIRMED` |
| `artifacts/qa/coverage/html/.gitkeep` | Retains a proposed human-readable coverage-browser directory. | `CONFIRMED` |
| `artifacts/qa/coverage/README.md` | Parent permits generated HTML coverage output but marks implementation unknown. | `CONFIRMED` |
| `artifacts/qa/README.md` | Parent QA lane is compatibility, non-authoritative, and regenerable. | `CONFIRMED` |
| `pyproject.toml` | Root test extra declares `pytest`, not `pytest-cov`. | `CONFIRMED` |
| `Makefile` | `make test` runs selected tests without coverage flags. | `CONFIRMED` |
| `contracts-validate.yml` | Installs root test extra and invokes `make test`. | `CONFIRMED` |
| `policy-boundary-guards.yml` | Uploads JUnit XML, not coverage HTML. | `CONFIRMED` |
| `.gitignore` | Ignores direct `artifacts/qa/*.xml`, not this nested HTML tree. | `CONFIRMED` |
| `artifacts/qa/coverage/html/index.html` | Checked path absent. | `CONFIRMED ABSENT` |
| `.coveragerc` | Checked root path absent. | `CONFIRMED ABSENT` |
| `.github/workflows/coverage-html.yml` | Checked workflow path absent. | `CONFIRMED ABSENT` |
| Local/CI ignored reports | Not observable through tracked repository evidence. | `UNKNOWN` |
| Coverage percentage and threshold | No operational measurement or gate established. | `UNKNOWN / NOT ESTABLISHED` |

### Evidence limits

This ledger does not prove that no developer, package, external service, or historical workflow has ever generated coverage output. It supports only the bounded repository conclusions stated above.

[Back to top](#top)

---

## No-loss assessment

The prior target README contained no text. This revision therefore removes no substantive local contract.

It inherits and narrows the parent coverage and QA rules:

- coverage output is generated and non-authoritative;
- source tests and source code remain in their owning roots;
- receipts, proofs, and release decisions remain canonical elsewhere;
- reports should be regenerable and scrubbed;
- report presence does not prove correctness or release readiness.

The added material makes HTML-specific risks visible: source excerpts, paths, executable assets, stale trees, accidental commits, percentage misuse, scope gaming, and ambiguous retention.

[Back to top](#top)

---

## Documentation correction and rollback

This change is documentation-only.

Before merge:

- close the draft PR; or
- restore the prior empty blob in a transparent follow-up commit.

After merge:

- revert the documentation commit; or
- publish an evidence-grounded corrective revision.

No test run, source code, coverage measurement, CI artifact, release, deployment, or production rollback is required because this README does not implement those behaviors.

Any later implementation change must update this README and the parent QA/coverage contracts in the same governed change or explain the temporary divergence.

[Back to top](#top)

---

## Status summary

`artifacts/qa/coverage/html/` is a tracked compatibility placeholder for future human-browsable coverage output.

It currently establishes **no coverage percentage, no threshold, no producer, no workflow, no retained HTML tree, no correctness claim, and no release significance**.

When implementation exists, the lane should remain an inspection surface only: generated, scoped, scrubbed, expiring, reversible, and bound to canonical run and release records elsewhere when material.

<p align="right"><a href="#top">Back to top</a></p>
