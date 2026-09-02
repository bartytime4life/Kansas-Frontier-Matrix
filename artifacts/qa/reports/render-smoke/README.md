<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-reports-render-smoke-readme
title: artifacts/qa/reports/render-smoke/ — Render Smoke QA Report, Inspection, and Non-Authority Boundary
type: readme; directory-readme; qa-report-output; render-smoke-report; compatibility-boundary; browser-and-render-inspection-contract
version: v0.1
status: draft; repository-grounded; compatibility-root; transitional; readme-empty-before-revision; gitkeep-tracked; report-payload-not-present; general-render-producer-not-established; ui-build-workflow-todo-only; explorer-build-test-todo-only; maplibre-perf-pipeline-confirmed-separate; maplibre-render-diff-schema-permissive; referenced-baseline-pngs-absent-at-checked-paths; dedicated-render-smoke-workflow-not-established; report-schema-not-established; retention-not-established; release-binding-unestablished; non-authoritative
owners: OWNER_TBD — QA/report steward · UI steward · MapLibre steward · Browser-test steward · Visual-regression steward · Accessibility steward · Security/privacy steward · Rights/sensitivity reviewer · CI/artifact-retention steward · Receipt/proof steward · Release/publication steward · Docs steward
created: 2026-07-16
updated: 2026-07-16
policy_label: public-doc; artifacts; qa; render-smoke; browser-smoke; visual-regression; generated-output; inspection-only; no-secrets; no-renderer-authority; no-truth-authority; no-proof-authority; no-release-authority; correction-aware; rollback-aware
current_path: artifacts/qa/reports/render-smoke/README.md
truth_posture: CONFIRMED target README existed as an empty tracked file; sibling .gitkeep retains a proposed render-smoke summary directory; parent artifacts/qa/reports and artifacts/qa boundaries; Directory Rules and root artifacts README classify artifacts as a transitional compatibility root limited to derived, regenerable, non-authoritative material under build/docs/qa/temporary; root package exposes executable MapLibre perf and render-diff scripts but TODO-only generic lint/test/build commands; scripts/maplibre-smoke-perf.mjs launches Playwright Chromium with two fixed scenarios and writes performance, screenshot, frame-time, and run-receipt-shaped files under artifacts/perf; scripts/build-maplibre-render-diff.mjs compares those screenshots against tests/fixtures/maplibre/baselines and writes a RenderDiffReport under artifacts/perf; maplibre-perf-governance workflow substantively executes and validates that separate pipeline and uploads artifacts/perf for 30 days; render-diff schema is currently a permissive object schema; exact expected baseline PNGs for the two scripted scenarios were absent at checked paths; ui-build workflow and Explorer Web package scripts remain TODO-only; root gitignore covers direct artifacts/qa/*.xml only and not this nested report lane; checked render-smoke report/run/summary/workflow/schema paths were absent / PROPOSED immutable render-run identity; explicit surface, route, viewport, browser, renderer, fixture, network, data, policy, locale, time, motion, theme, and input scope; normalized observations and findings; screenshot and console/network evidence routing; non-vacuity checks; accessibility and trust-state smoke; deterministic visual comparison; CI artifact upload, access, expiry, and retention; canonical receipt/proof/release linkage; correction, invalidation, supersession, withdrawal, rollback, and lane retirement / CONFLICTED general render-smoke report naming versus no general producer; substantive MapLibre artifacts/perf pipeline versus Directory Rules strict build/docs/qa/temporary scope; target report lane versus specialized artifacts/perf output; RenderDiffReport object and run-receipt-shaped file under artifacts compatibility versus canonical receipt/proof/release homes; permissive render-diff schema versus strong governance language; baseline README no-run posture versus executable script references; workflow existence versus checked absent scenario baseline PNGs; external MapLibre/CDN/glyph dependencies versus deterministic or no-network aspirations; and render success versus correctness, accessibility, evidence support, policy permission, release approval, or publication / UNKNOWN uncommitted local reports, CI-only artifacts, historical runs, external browser services, dynamically loaded routes, actual current workflow pass status, complete baseline inventory, current screenshots/diffs, active consumers, branch-protection significance, hosting, deployment, production use, and operational rollback / NEEDS VERIFICATION accepted owners, CODEOWNERS, complete recursive inventory, retain/migrate/retire decision, artifacts/perf exception or migration ADR, canonical report and receipt homes, accepted render-smoke profiles, browser and renderer version pins, route/surface inventory, deterministic fixture strategy, external-resource policy, baseline approval, threshold ownership, accessibility coverage, sensitive-content redaction, workflow ownership, artifact retention, release significance, correction consumers, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b2ce3b33a53304cc6cc080f268f7321fa6ed56c3
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  confirmed_lane_files:
    - artifacts/qa/reports/render-smoke/README.md
    - artifacts/qa/reports/render-smoke/.gitkeep
  confirmed_lane_blobs:
    README.md: 8b137891791fe96927ad78e64b0aad7bded08bdc
    .gitkeep: 81eedf2b891c7f1ae7e9e6b493b30893f425f589
  checked_absent_paths:
    - artifacts/qa/reports/render-smoke/render-smoke-report.json
    - artifacts/qa/reports/render-smoke/render-smoke-run.json
    - artifacts/qa/reports/render-smoke/render-smoke-summary.md
    - .github/workflows/render-smoke.yml
    - schemas/artifacts/render-smoke-report.schema.json
    - tests/fixtures/maplibre/baselines/cache-heavy-layout-slim.png
    - tests/fixtures/maplibre/baselines/cache-light-heavy-paint-heavy.png
  confirmed_separate_maplibre_surfaces:
    - scripts/maplibre-smoke-perf.mjs
    - scripts/build-maplibre-render-diff.mjs
    - configs/maplibre/perf-envelope.v1.json
    - schemas/maplibre/render-diff-report.schema.json
    - tools/validators/maplibre/validate_render_diff_report.py
    - .github/workflows/maplibre-perf-governance.yml
    - tests/fixtures/maplibre/baselines/README.md
  bounded_inventory_note: tracked repository evidence cannot establish uncommitted local reports, ignored or generated screenshots, CI workspaces, historical workflow artifacts, external browser services, object stores, branch-local outputs, production routes, branch-protection settings, or uninspected subprojects
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../artifacts/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../package.json
  - ../../../../apps/explorer-web/package.json
  - ../../../../scripts/maplibre-smoke-perf.mjs
  - ../../../../scripts/build-maplibre-render-diff.mjs
  - ../../../../configs/maplibre/perf-envelope.v1.json
  - ../../../../schemas/maplibre/render-diff-report.schema.json
  - ../../../../tools/validators/maplibre/validate_render_diff_report.py
  - ../../../../tests/fixtures/maplibre/baselines/README.md
  - ../../../../.github/workflows/maplibre-perf-governance.yml
  - ../../../../.github/workflows/ui-build.yml
  - ../../../../data/receipts/README.md
  - ../../../../data/proofs/README.md
  - ../../../../release/README.md
  - ../../../../.gitignore
tags: [kfm, artifacts, qa, reports, render-smoke, browser-smoke, maplibre, playwright, screenshots, visual-diff, baselines, deterministic-rendering, accessibility, sensitive-content, retention, correction, rollback]
notes:
  - "This is the first substantive contract for an otherwise empty README."
  - "The direct lane contains only README.md and .gitkeep in bounded tracked evidence."
  - "No general render-smoke report, producer, schema, dedicated test suite, workflow, retained run manifest, consumer, or release binding was established."
  - "A substantive MapLibre performance/render-diff pipeline exists separately under artifacts/perf; this README does not adopt, duplicate, or relocate it."
  - "The checked MapLibre render-diff schema is permissive and the two exact scenario baseline PNGs referenced by the scripts were absent at checked paths."
  - "A report in this lane is an inspection copy, not renderer truth, source truth, evidence, a receipt, proof, PolicyDecision, ReleaseManifest, publication approval, or public artifact."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `artifacts/qa/reports/render-smoke/` — Render Smoke QA Report, Inspection, and Non-Authority Boundary

> **Purpose.** Define the staging boundary for generated browser and renderer smoke-test reports without allowing a screenshot, successful page load, pixel-diff result, green workflow, performance threshold, map render, or human visual inspection to become source truth, evidence closure, accessibility conformance, policy permission, release approval, publication, or production truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: artifacts compatibility" src="https://img.shields.io/badge/root-artifacts__compatibility-orange">
  <img alt="Direct inventory: README and gitkeep" src="https://img.shields.io/badge/direct__inventory-README%20%2B%20gitkeep-informational">
  <img alt="General report payload: absent" src="https://img.shields.io/badge/general__payload-NOT__ESTABLISHED-critical">
  <img alt="MapLibre pipeline: separate" src="https://img.shields.io/badge/MapLibre__pipeline-SEPARATE-blue">
  <img alt="Authority: none" src="https://img.shields.io/badge/trust__authority-none-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Authority](#authority-and-directory-rules-basis) · [Inventory](#confirmed-current-inventory) · [Topology](#render-and-report-topology) · [Meaning](#what-render-smoke-can-and-cannot-mean) · [Scope](#render-smoke-scope-contract) · [Cases](#smoke-case-contract) · [Outputs](#output-format-and-routing-contract) · [MapLibre](#confirmed-maplibre-specialized-pipeline) · [Baselines](#baseline-and-visual-comparison-contract) · [Accessibility](#accessibility-and-trust-visible-state-contract) · [Security](#security-privacy-rights-and-sensitive-content) · [Determinism](#determinism-network-and-reproducibility) · [CI](#producer-ci-artifact-and-retention-contract) · [Outcomes](#validation-non-vacuity-and-finite-outcomes) · [Trust](#receipt-proof-release-and-publication-boundary) · [Correction](#correction-invalidation-and-rollback) · [Done](#definition-of-done) · [Plan](#smallest-sound-implementation-sequence) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

> [!IMPORTANT]
> **Snapshot:** `main@b2ce3b33a53304cc6cc080f268f7321fa6ed56c3`
> **Prior README blob:** `8b137891791fe96927ad78e64b0aad7bded08bdc` — empty file
> **Confirmed direct files:** `README.md`, `.gitkeep`
> **General render-smoke payload, producer, workflow, schema, tests, retention, consumer:** not established
> **Specialized MapLibre perf/render-diff pipeline:** confirmed elsewhere under `artifacts/perf/`
> **Current target authority:** none; inspection staging only

`artifacts/qa/reports/render-smoke/` is a repository-confirmed compatibility placeholder. It is **not an operational general render-smoke reporting system**.

### Safe conclusion

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Boundary README | `CONFIRMED` | The path existed, but the README was empty before this revision. |
| Directory retention marker | `CONFIRMED` | `.gitkeep` identifies a proposed render-smoke summary directory. |
| General render-smoke report | `NOT ESTABLISHED` | No checked report payload exists. |
| General run manifest or summary | `NOT ESTABLISHED` | Checked candidate paths are absent. |
| Dedicated general workflow | `NOT ESTABLISHED` | Checked `.github/workflows/render-smoke.yml` is absent. |
| Dedicated general report schema | `NOT ESTABLISHED` | Checked schema path is absent. |
| Generic UI build/test | `TODO ONLY` | Root and Explorer Web scripts do not establish a rendered application. |
| UI-build workflow | `TODO ONLY` | Current jobs only echo build/test TODO messages. |
| Specialized MapLibre smoke script | `CONFIRMED EXECUTABLE` | Playwright launches Chromium and emits screenshots, frame times, and perf results. |
| Specialized MapLibre render diff | `CONFIRMED EXECUTABLE` | Pixel comparison writes a `RenderDiffReport` and fails on threshold or missing baseline. |
| Specialized MapLibre workflow | `CONFIRMED SUBSTANTIVE` | It runs, validates, attests, packages, and uploads `artifacts/perf/` with 30-day retention. |
| Specialized render-diff schema | `PERMISSIVE` | The current schema accepts any object shape. |
| Scenario baseline PNGs | `ABSENT AT CHECKED PATHS` | The two exact filenames derived from scripted scenarios returned not found. |
| Target-lane ignore protection | `NOT ESTABLISHED` | Root ignore rules do not cover nested render reports or screenshots. |
| Receipt/proof/release binding | `NOT ESTABLISHED FOR THIS LANE` | No canonical trust record points to this target. |
| Current pass rate | `UNKNOWN` | Workflow and scripts do not prove the latest run passed. |
| Public or production use | `UNKNOWN` | A workflow, screenshot, or directory name cannot prove deployment. |
| Renderer truth or release proof | `DENY` | Render smoke cannot establish those authorities. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, exact paths, executable code, workflow bodies, or bounded search. |
| `PROPOSED` | A recommended object, profile, path, check, or gate not established as current implementation. |
| `CONFLICTED` | Current files, paths, contracts, or duties create incompatible expectations. |
| `UNKNOWN` | Not observable or not established from inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently proven for operational reliance or release significance. |
| `DENY` | A prohibited authority, security, evidence, policy, release, or publication interpretation. |

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules and the root `artifacts/README.md` place generated QA reports under `artifacts/qa/` because they are derived, regenerable, and non-authoritative.

```text
source UI, styles, routes, fixtures       apps/ packages/ configs/ tests/
render and comparison implementations     scripts/ tools/ packages/
generated screenshots and QA reports      artifacts/qa/ or an accepted compatibility lane
canonical run/process memory               data/receipts/
proof and EvidenceBundle support           data/proofs/
release and publication decisions          release/
published public-safe products             data/published/
```

This lane may stage generated reviewer-inspection reports. It must not become:

- a renderer implementation root;
- a screenshot archive of record;
- a baseline-fixture authority;
- an accessibility-conformance authority;
- an EvidenceBundle or proof store;
- a canonical receipt store;
- a release decision root;
- a published map or documentation surface;
- a public hosting origin;
- a second home for the specialized MapLibre pipeline.

### Compatibility-root constraint

The root `artifacts/` contract limits ordinary compatibility scope to:

```text
artifacts/build/
artifacts/docs/
artifacts/qa/
artifacts/temporary/
```

The confirmed MapLibre pipeline writes to `artifacts/perf/`. That is a **repository fact and a governance conflict**, not permission to expand this target into another parallel output root.

Until an ADR, migration note, or accepted compatibility decision resolves `artifacts/perf/`:

1. do not silently relocate its outputs;
2. do not copy its trust-shaped objects into this lane;
3. do not call this lane its canonical report home;
4. do not create a second MapLibre report producer here;
5. surface the conflict in review and migration planning.

[Back to top](#top)

---

<a id="confirmed-current-inventory"></a>

## Confirmed current inventory

```text
artifacts/qa/reports/render-smoke/
├── README.md
└── .gitkeep
```

### Direct-file semantics

| File | Current meaning | Authority |
|---|---|---:|
| `README.md` | Human boundary contract; empty before this revision | Documentation only |
| `.gitkeep` | Retains the proposed directory | None |

### Checked absent candidates

```text
artifacts/qa/reports/render-smoke/render-smoke-report.json
artifacts/qa/reports/render-smoke/render-smoke-run.json
artifacts/qa/reports/render-smoke/render-smoke-summary.md
.github/workflows/render-smoke.yml
schemas/artifacts/render-smoke-report.schema.json
```

Absence at these checked paths does not prove that uncommitted, historical, external, dynamically generated, or branch-local equivalents never existed.

[Back to top](#top)

---

<a id="render-and-report-topology"></a>

## Render and report topology

A governed render-smoke system separates implementation, inputs, outputs, and authority.

```text
SOURCE / FIXTURE INPUTS
  apps/ packages/ configs/ tests/fixtures/
                  |
                  v
RENDER PRODUCER
  browser runner / renderer / capture script
                  |
                  v
NON-AUTHORITATIVE OUTPUTS
  screenshots / logs / observations / diff summaries
                  |
                  v
REVIEW AND CANONICAL MEMORY
  QA review -> receipt/proof/release homes when required
```

### Responsibility matrix

| Responsibility | Owning surface | Target-lane relationship |
|---|---|---|
| UI source and routes | `apps/`, `packages/` | Inputs only |
| Renderer and browser code | implementation roots | Inputs only |
| Fixture and baseline inputs | `tests/fixtures/` | Inputs only |
| Render-smoke producer | `scripts/`, `tools/`, package or app tooling | Writes reports if accepted |
| General render-smoke report | this lane, if implemented | Non-authoritative inspection copy |
| Specialized MapLibre perf/render output | currently `artifacts/perf/` | Separate confirmed system; migration unresolved |
| Canonical validation memory | accepted `ValidationReport` / receipt homes | Referenced, not stored here |
| Proof and attestations | `data/proofs/` | Referenced, not stored here |
| Release decision | `release/` | Separate authority |
| Published UI/map product | governed deployment or `data/published/` | Never inferred from this lane |

### Do not collapse these concepts

```text
page loaded        ≠ route behaved correctly
pixels appeared    ≠ content was semantically correct
pixel match        ≠ accessibility conformance
screenshot exists  ≠ evidence exists
render passed      ≠ policy allowed exposure
performance passed ≠ release was approved
report exists      ≠ canonical validation memory exists
```

[Back to top](#top)

---

<a id="what-render-smoke-can-and-cannot-mean"></a>

## What render smoke can and cannot mean

### A render-smoke report may support

- confirmation that a declared browser opened;
- confirmation that a declared route or document produced a frame;
- observation of console, network, page, or renderer errors;
- observation of a blank, crashed, incomplete, or visibly degraded surface;
- comparison against an accepted synthetic baseline;
- confirmation that declared trust-state labels were visible;
- confirmation that a keyboard or accessibility smoke step completed;
- bounded performance and timing observations;
- reviewer triage and defect reproduction.

### It cannot prove

- source data correctness;
- evidence sufficiency;
- citation validity;
- policy permission;
- rights clearance;
- sensitive-data safety beyond configured checks;
- accessibility conformance beyond the tested cases;
- semantic equivalence from pixel similarity;
- full browser/device coverage;
- release approval;
- publication status;
- production health;
- absence of hidden or intermittent defects.

### Negative-result value

A failing render smoke is often more trustworthy than an over-broad pass. It may establish that:

- a route failed to load;
- a baseline is missing;
- dimensions changed;
- pixel delta exceeded a declared threshold;
- required trust state was absent;
- a browser or fixture dependency failed;
- a network or resource assumption was violated;
- a screenshot or report is unsafe to retain.

It still must identify the exact scope and must not generalize beyond that scope.

[Back to top](#top)

---

<a id="render-smoke-scope-contract"></a>

## Render-smoke scope contract

Every run must declare immutable or digest-bound scope.

### Required identity fields

| Field | Requirement |
|---|---|
| `run_id` | Unique, stable run identity |
| `source_git_sha` | Exact source revision |
| `producer_ref` | Script/tool/package identity and version |
| `profile_ref` | Accepted smoke profile and digest |
| `surface_ref` | Route, page, component, map scene, document preview, or artifact |
| `case_ids` | Exact selected smoke cases |
| `browser` | Engine, version, channel, headless/headed posture |
| `viewport` | Width, height, device scale factor, orientation |
| `platform` | OS, architecture, runtime versions |
| `renderer_ref` | Renderer and version where material |
| `fixture_refs` | Exact fixture/baseline references and digests |
| `network_mode` | denied, local-only, allowlisted, or external |
| `locale_timezone` | Locale, language, timezone, date/time controls |
| `theme_motion` | Theme, contrast mode, reduced-motion posture |
| `policy_context` | Audience, rights, sensitivity, release posture |
| `started_utc` / `completed_utc` | Run time |
| `dirty_tree` | Whether source or fixture inputs were modified |

### Scope must be explicit

A report must not say “the UI passed” when it tested:

- one route;
- one viewport;
- one browser;
- one theme;
- one locale;
- one fixture;
- one policy outcome;
- one map scene;
- one screenshot timing point.

Use language such as:

> Case `shell-answer-desktop-chromium` passed for the declared revision, viewport, fixture set, browser version, network posture, and threshold profile.

[Back to top](#top)

---

<a id="smoke-case-contract"></a>

## Smoke-case contract

Each case should identify:

```yaml
case_id: render-smoke.example.v1
surface:
  kind: route
  ref: /example
environment:
  browser: chromium
  viewport: {width: 1280, height: 720, device_scale_factor: 1}
  locale: en-US
  timezone: America/Chicago
  theme: light
  reduced_motion: reduce
inputs:
  fixture_refs: []
  baseline_ref: null
  network_mode: local-only
actions:
  - navigate
  - wait_for_declared_ready_signal
  - assert_required_text
  - capture_screenshot
checks:
  console_errors: deny
  page_errors: deny
  network_failures: report
  blank_frame: deny
  pixel_diff: not_run
expected_outcome: PASS
```

### Required case families

A mature profile should distinguish:

1. route and shell load;
2. finite outcomes — `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`;
3. loading, cancelled, stale, restricted, corrected, superseded, and withdrawn states;
4. Evidence Drawer open/close and focus behavior;
5. map/list/table parity;
6. keyboard navigation;
7. reduced motion;
8. narrow viewport and zoom;
9. theme and contrast variants;
10. offline or constrained-network behavior;
11. renderer and baseline comparison;
12. safe error and missing-resource behavior.

### Case isolation

Cases should not depend on undocumented ordering, prior browser state, shared credentials, external mutable data, or a prior case's cache unless the profile explicitly declares that dependency.

[Back to top](#top)

---

<a id="output-format-and-routing-contract"></a>

## Output format and routing contract

### Proposed direct outputs

```text
artifacts/qa/reports/render-smoke/
├── README.md
├── render-smoke-run.json
├── render-smoke-report.json
├── render-smoke-summary.md
├── screenshots/
├── diffs/
└── logs/
```

This tree is **PROPOSED**, not current repository fact.

### Routing rules

| Output | Proposed route | Notes |
|---|---|---|
| Run metadata | `render-smoke-run.json` | Non-authoritative scope identity |
| Structured findings | `render-smoke-report.json` | Machine-readable inspection copy |
| Human summary | `render-smoke-summary.md` | Generated; must not become authored doctrine |
| Screenshots | `screenshots/` | Redacted, bounded, short-lived |
| Pixel diffs | `diffs/` | Include baseline and threshold refs |
| Console/network logs | `logs/` | Sanitize secrets and private URLs |
| Canonical run receipt | `data/receipts/` | Separate object and authority |
| Proof or attestation | `data/proofs/` | Separate object and authority |
| Release decision | `release/` | Separate decision |
| Public artifact | governed publication route | Never served directly from this lane |

### Proposed report skeleton

```yaml
object_type: RenderSmokeReport
schema_version: v1
report_id: kfm:render-smoke-report:<id>
run_ref: kfm:render-smoke-run:<id>
source_git_sha: <sha>
profile_ref: <ref>
profile_digest: sha256:<digest>
overall_outcome: PASS
cases:
  - case_id: shell-answer-desktop-chromium
    outcome: PASS
    observations: []
    findings: []
    screenshot_ref: screenshots/shell-answer.png
summary:
  selected_cases: 1
  executed_cases: 1
  passed_cases: 1
  failed_cases: 0
  skipped_cases: 0
limitations: []
created_utc: <timestamp>
```

[Back to top](#top)

---

<a id="confirmed-maplibre-specialized-pipeline"></a>

## Confirmed MapLibre specialized pipeline

A substantive MapLibre smoke/performance and visual-diff system exists, but it is **not this lane**.

### Confirmed producer behavior

`scripts/maplibre-smoke-perf.mjs`:

- launches Playwright Chromium headlessly;
- uses a 1280 × 720 viewport;
- runs two fixed scenarios;
- records load, idle, average-frame, and p95-frame timing;
- writes frame-time CSV files;
- captures PNG screenshots;
- writes `artifacts/perf/perf-results.json`;
- writes a run-receipt-shaped JSON file;
- references `artifacts/perf/render-diff/render-diff-report.json`.

`scripts/build-maplibre-render-diff.mjs`:

- reads screenshots from `artifacts/perf/screenshots`;
- reads expected baselines from `tests/fixtures/maplibre/baselines`;
- compares PNG pixels with `pixelmatch`;
- writes diff PNGs;
- writes a `RenderDiffReport`;
- exits nonzero for missing baselines, dimension mismatch, or excess pixel delta.

### Confirmed threshold envelope

The current envelope declares:

| Threshold | Value |
|---|---:|
| Average frame time | 22 ms |
| p95 frame time | 40 ms |
| Idle time | 3000 ms |
| Load time | 4000 ms |
| Pixel delta ratio | 0.01 |

These are MapLibre profile values. They do not become general render-smoke thresholds.

### Confirmed CI behavior

The MapLibre workflow:

- installs Node, Python, npm dependencies, and Playwright Chromium;
- validates the performance envelope;
- starts a local fixture server;
- runs smoke performance and render-diff producers;
- validates the render-diff report;
- builds attestations, manifests, proof packs, and failure/correction artifacts;
- uploads `artifacts/perf/` for 30 days.

### Bounded maturity concerns

1. The checked render-diff JSON Schema requires only an object and allows arbitrary fields.
2. The two exact scenario baseline PNGs derived from the script were absent at checked paths.
3. The smoke page imports MapLibre CSS and JavaScript from `unpkg.com`.
4. The style uses a remote demo glyph URL.
5. Workflow existence does not establish a current passing run.
6. `artifacts/perf/` is outside the root `artifacts/` README's strict listed scope.
7. A run-receipt-shaped file under a compatibility root must not be confused with canonical process memory.

### Relationship to this lane

This README does not:

- rename `artifacts/perf/`;
- redirect the MapLibre workflow;
- adopt its report format as the general format;
- claim its output belongs here;
- duplicate its scripts;
- weaken its specialized governance;
- resolve its compatibility-root placement conflict.

Those are separate implementation and ADR decisions.

[Back to top](#top)

---

<a id="baseline-and-visual-comparison-contract"></a>

## Baseline and visual-comparison contract

### Baseline identity

Every comparison must bind:

- baseline file digest;
- baseline set version;
- reviewer and approval state;
- source revision used to produce the baseline;
- renderer/browser/platform/viewport profile;
- fixture and data digest;
- theme, locale, timezone, motion, and scale;
- expected sensitivity and rights posture;
- supersession and rollback target.

### Baselines are fixtures, not truth

A baseline can be wrong, stale, inaccessible, unsafe, or generated from unreleased data. Matching it only proves similarity to that baseline under the declared comparison.

### Missing baseline

A missing baseline must produce a finite outcome such as:

```text
BASELINE_MISSING
```

It must not:

- silently create and approve a new baseline;
- treat the current screenshot as accepted;
- report 0% delta;
- pass the case;
- overwrite a prior baseline without review.

### Dimension mismatch

A dimension mismatch should preserve:

- actual dimensions;
- expected dimensions;
- device scale factor;
- viewport;
- browser/version;
- screenshot mode;
- safe diagnostic.

### Pixel threshold

Thresholds must be profile-owned. A threshold change requires:

- owner;
- reason;
- before/after impact;
- representative fixtures;
- false-positive/false-negative review;
- rollback;
- release-significance review where applicable.

### Baseline update discipline

Baseline creation and approval should be separate duties when the baseline affects release. At minimum, the producer must not both create a changed baseline and declare the change acceptable without review.

[Back to top](#top)

---

<a id="accessibility-and-trust-visible-state-contract"></a>

## Accessibility and trust-visible state contract

A screenshot cannot establish accessibility. A render-smoke profile may include bounded accessibility checks, but it must distinguish them from visual inspection.

### Minimum accessibility smoke candidates

- keyboard-only navigation reaches the declared controls;
- focus order is stable;
- dialogs and drawers trap and return focus;
- required status messages are announced;
- `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` are textually distinguishable;
- trust badges do not rely on color alone;
- map interactions have a non-map alternative;
- reduced-motion behavior is respected;
- narrow-viewport and zoom behavior preserve critical trust state;
- images and exported captures carry appropriate alt-text metadata.

### Trust-visible state

Render cases should verify that consequential state is visible as text:

- outcome;
- source role;
- rights;
- sensitivity;
- review state;
- freshness;
- release state;
- correction or supersession;
- geometry/reality boundary where relevant;
- reason codes for abstention or denial.

### Accessibility outcome boundary

A case may report:

```text
ACCESSIBILITY_SMOKE_PASS
```

It must not claim:

```text
WCAG_CONFORMANT
ACCESSIBLE_FOR_ALL_USERS
ACCESSIBILITY_APPROVED
```

unless a separate accepted conformance process supports that claim.

[Back to top](#top)

---

<a id="security-privacy-rights-and-sensitive-content"></a>

## Security, privacy, rights, and sensitive content

Screenshots and logs can expose more than the source code.

### Prohibited leakage

Do not retain or upload:

- credentials, tokens, cookies, authorization headers, or session ids;
- private hostnames, signed URLs, query secrets, or internal filesystem paths;
- precise sensitive-species or archaeology locations;
- living-person, DNA, private-well, land-ownership, or protected cultural details;
- restricted infrastructure locations;
- unreleased internal identifiers;
- RAW, WORK, or QUARANTINE content;
- confidential browser storage;
- sensitive console payloads;
- third-party copyrighted content without accepted rights posture.

### Required controls

1. Use synthetic or public-safe fixtures by default.
2. Deny production credentials.
3. Clear storage between cases.
4. Block or allowlist network requests.
5. Sanitize URLs, headers, console messages, DOM excerpts, and filenames.
6. Redact or generalize protected spatial detail.
7. Review screenshot rights before retention or distribution.
8. Keep failure diagnostics safe enough for the artifact audience.
9. Record redaction transforms where material.
10. Treat unsafe output as `DENY` or `HOLD`, not as a normal report.

### Active content

HTML reports must not execute untrusted scripts, load uncontrolled remote assets, or embed active content from tested pages.

[Back to top](#top)

---

<a id="determinism-network-and-reproducibility"></a>

## Determinism, network, and reproducibility

### Determinism inputs

A reproducible run should pin:

- browser engine and version;
- OS/container;
- runtime and dependency lockfiles;
- renderer and plugin versions;
- fonts, glyphs, sprites, styles, and tiles;
- viewport and scale;
- locale and timezone;
- clock and random seeds;
- animation and transition state;
- network fixtures and cache posture;
- baseline digests;
- threshold profile;
- source revision.

### Network classes

| Mode | Meaning |
|---|---|
| `deny` | No network permitted |
| `local-only` | Loopback fixture services only |
| `allowlisted` | Explicit hosts and resources |
| `external` | Mutable external services are used |

External resources make byte-for-byte screenshot reproduction weaker. A report must disclose them.

### Rebuild classes

| Outcome | Meaning |
|---|---|
| `PIXEL_IDENTICAL` | Same pixels under the accepted profile |
| `WITHIN_THRESHOLD` | Delta is within accepted threshold |
| `EXPECTED_VARIANCE` | Difference is explained and accepted |
| `NONCOMPARABLE` | Inputs or environment differ materially |
| `DIFFERENT_UNEXPECTED` | Difference requires review |
| `ERROR` | Comparison could not complete |
| `NOT_RUN` | No comparison attempted |

### Clock and animation

Do not capture while the surface is in an undocumented transient state. Use an explicit ready signal, deterministic wait contract, or stable animation-disabled profile.

[Back to top](#top)

---

<a id="producer-ci-artifact-and-retention-contract"></a>

## Producer, CI artifact, and retention contract

### Producer obligations

A future general producer should:

- fail on zero selected cases;
- fail or abstain on missing required profile;
- identify every tested surface;
- preserve safe logs and findings;
- distinguish page, console, network, assertion, screenshot, and comparison failures;
- write atomically;
- avoid silently approving baselines;
- emit deterministic ordering;
- sanitize output;
- return meaningful exit codes;
- preserve correction and supersession links.

### CI separation

CI should separate:

1. build or fixture preparation;
2. render execution;
3. report validation;
4. security/redaction scan;
5. artifact upload;
6. canonical receipt creation where required;
7. release decision.

A single green job must not collapse those duties.

### Proposed artifact names

```text
render-smoke-report-<run-id>
render-smoke-failure-<run-id>
```

### Retention classes

| Class | Typical use | Posture |
|---|---|---|
| `ephemeral` | local debugging | delete after run |
| `ci-short` | pull-request review | short bounded retention |
| `investigation` | active defect review | owner and expiry required |
| `release-candidate` | release review support | canonical references required |
| `externally-published` | public disclosure | separate publication approval required |

The specialized MapLibre workflow currently uses 30-day artifact retention. That does not automatically set this lane's retention policy.

[Back to top](#top)

---

<a id="validation-non-vacuity-and-finite-outcomes"></a>

## Validation, non-vacuity, and finite outcomes

### Non-vacuity requirements

A report must not pass when:

- zero cases were selected;
- zero routes or surfaces were rendered;
- the expected application never built;
- every case was skipped;
- the required baseline was missing;
- the profile was absent;
- the browser failed to launch;
- the report parser failed;
- screenshot capture failed;
- all findings were suppressed by a wildcard;
- only a placeholder or README was inspected;
- the test page was blank but did not throw;
- external dependencies failed and the case silently degraded.

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Required configured checks passed for the declared scope |
| `WARN` | Non-blocking finding requires visibility |
| `FAIL` | Blocking smoke or comparison defect |
| `HOLD` | Unsafe, incomplete, stale, or noncomparable output |
| `ABSTAIN` | Insufficient context or missing dependency |
| `DENY` | Security, rights, sensitivity, policy, or exposure prohibition |
| `ERROR` | Tool or environment failure |
| `REVIEW_REQUIRED` | Human determination required |
| `EMPTY_SCOPE` | No meaningful case or surface selected |
| `PROFILE_NOT_ESTABLISHED` | No accepted profile bound |
| `BASELINE_MISSING` | Required baseline absent |
| `BASELINE_CONFLICT` | Multiple or incompatible baselines |
| `NONCOMPARABLE` | Material environment/input drift |
| `PLACEHOLDER_ONLY` | Only scaffolding was exercised |
| `NOT_RUN` | Check intentionally not executed |

### Result composition

The top-level outcome should preserve the most restrictive material child outcome. Do not average a security denial with successful screenshots.

[Back to top](#top)

---

<a id="receipt-proof-release-and-publication-boundary"></a>

## Receipt, proof, release, and publication boundary

### This lane is not canonical memory

A report staged here can be deleted, regenerated, or expired. A trust-bearing decision must resolve through canonical objects elsewhere.

```text
render-smoke report
        |
        +--> validation receipt / ValidationReport when required
        |
        +--> proof or attestation when required
        |
        +--> policy/review decision
        |
        +--> release decision
        |
        +--> governed publication or deployment
```

### Required separation

- A screenshot is not an EvidenceBundle.
- A run summary is not a receipt unless it conforms to the accepted receipt contract and lives in its canonical home.
- A render-diff report is not proof closure.
- A threshold envelope is not a PolicyDecision.
- A passing workflow is not a ReleaseManifest.
- An uploaded artifact is not publication.
- A hosted preview is not production truth.

### MapLibre-specific caution

The specialized script writes `artifacts/perf/run-receipt.json`. Its filename and shape must not be used to infer canonical receipt authority. Canonical placement and validation remain separate governance questions.

[Back to top](#top)

---

<a id="correction-invalidation-and-rollback"></a>

## Correction, invalidation, and rollback

### Invalidate a report when

- source revision changes;
- fixture or baseline changes;
- browser, renderer, dependency, font, or platform changes materially;
- threshold profile changes;
- rights or sensitivity posture changes;
- tested route or data contract changes;
- a screenshot is found to expose protected content;
- a baseline was wrongly approved;
- report parsing or counting was defective;
- correction or withdrawal affects the rendered subject;
- the report is stale for its intended decision.

### Correction flow

1. mark the report invalid, stale, superseded, or withdrawn;
2. preserve the affected report id and digest;
3. identify the reason and affected cases;
4. remove unsafe artifacts from accessible storage;
5. invalidate caches and links;
6. rerun with corrected inputs when permitted;
7. update canonical receipts, proofs, reviews, and release records where material;
8. preserve the rollback target and lineage.

### Rollback classes

| Change | Rollback |
|---|---|
| README-only correction | revert documentation commit |
| Report generator change | revert producer/profile and rerun |
| Baseline change | restore prior reviewed baseline set |
| Threshold change | restore prior profile |
| Unsafe screenshot | delete/withdraw artifact and update canonical references |
| Release-significant defect | execute release rollback/correction procedure |

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is operational only when all applicable items are complete:

- [ ] Owners and CODEOWNERS are accepted.
- [ ] Retain, migrate, or retire decision is recorded.
- [ ] `artifacts/perf/` placement conflict is resolved or explicitly excepted.
- [ ] General producer and registry id are accepted.
- [ ] Report and run-manifest schemas are meaningful.
- [ ] Exact surface/route inventory is defined.
- [ ] Browser, platform, renderer, locale, theme, motion, and viewport profiles are pinned.
- [ ] Fixture and baseline identities are digest-bound.
- [ ] Baseline creation and approval duties are defined.
- [ ] Network policy is explicit.
- [ ] External-resource behavior is controlled.
- [ ] Zero-case and blank-frame guards exist.
- [ ] Console, page, and network failures are captured.
- [ ] Accessibility smoke scope is explicit.
- [ ] Trust-visible state cases exist.
- [ ] Sensitive-content and secret scanning are enforced.
- [ ] Report ordering and rerun semantics are deterministic.
- [ ] Suppressions have owner, reason, scope, and expiry.
- [ ] CI executes nonempty positive and negative cases.
- [ ] Artifacts have access and retention policy.
- [ ] Canonical receipt/proof/release handoffs are documented and tested.
- [ ] Correction, withdrawal, supersession, and rollback are tested.
- [ ] No output in this lane is served directly as public truth.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Phase 1 — Decide placement

- decide whether this lane is retained;
- resolve or document the `artifacts/perf/` exception;
- assign owners;
- prohibit parallel producers.

### Phase 2 — Define contracts

- accept case profile;
- accept report and run-manifest meaning;
- create meaningful schemas;
- define reason codes and finite outcomes.

### Phase 3 — Build a minimal producer

- one synthetic local-only page;
- one Chromium viewport;
- explicit ready signal;
- console/page/network capture;
- screenshot and structured report;
- zero-scope and blank-frame failure.

### Phase 4 — Add deterministic comparison

- approved synthetic baseline;
- digest binding;
- dimension and pixel-delta checks;
- explicit missing-baseline outcome;
- separate baseline approval.

### Phase 5 — Add governance checks

- trust-visible finite outcomes;
- keyboard/reduced-motion smoke;
- secret and sensitive-content canaries;
- safe diagnostic validation.

### Phase 6 — Wire CI and canonical memory

- dedicated workflow;
- validated report;
- bounded artifact retention;
- receipt/proof linkage where required;
- required-check decision by owners.

### Phase 7 — Exercise correction and rollback

- stale baseline;
- unsafe screenshot;
- changed threshold;
- withdrawn route;
- invalid report;
- artifact deletion and reference invalidation.

Each phase should be independently reviewable and reversible.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

1. Accepted owners and CODEOWNERS.
2. Retain, migrate, or retire decision for this lane.
3. Accepted disposition of `artifacts/perf/`.
4. Canonical general render-smoke producer.
5. Registry id and CLI/exit-code contract.
6. Canonical report and run-manifest contracts.
7. Meaningful JSON Schemas.
8. Route and surface inventory.
9. Browser engine/version matrix.
10. OS/container matrix.
11. Viewport and device-scale profiles.
12. Renderer/plugin version pins.
13. Theme, contrast, locale, timezone, and reduced-motion profiles.
14. Fixture ownership and digests.
15. Baseline file inventory.
16. Baseline approval duties.
17. Scenario baseline PNG disposition.
18. Missing-baseline policy.
19. Pixel threshold ownership.
20. Performance threshold ownership.
21. Ready-signal and wait policy.
22. Blank-frame detection.
23. Console/page/network error policy.
24. Network deny/local/allowlist policy.
25. External CDN and glyph dependency policy.
26. Font, sprite, tile, and style pinning.
27. Cache and service-worker posture.
28. Screenshot rights review.
29. Sensitive-location redaction.
30. Private endpoint and path sanitization.
31. Credential/cookie/storage isolation.
32. Accessibility smoke profile.
33. Trust-visible state profile.
34. Map/non-map alternative cases.
35. Negative and finite-outcome cases.
36. Screenshot/diff retention.
37. Reviewer access.
38. Suppression and waiver registry.
39. Deterministic ordering.
40. Independent rerun comparability.
41. Report validation semantics.
42. MapLibre render-diff schema strengthening.
43. Canonical receipt linkage.
44. Proof/attestation linkage.
45. Release significance.
46. Branch-protection significance.
47. Correction and cache invalidation.
48. Unsafe-artifact deletion procedure.
49. Operational rollback drill.
50. Production consumers, metrics, deployment, and current pass state.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports |
|---|---|---|
| Target prior blob `8b137891...` | `CONFIRMED` | README was empty |
| `.gitkeep` blob `81eedf2b...` | `CONFIRMED` | Proposed directory retention |
| Root `artifacts/README.md` | `CONFIRMED draft boundary` | Compatibility-only, derived, non-authoritative scope |
| `artifacts/qa/README.md` | `CONFIRMED scaffold` | QA reports are inspection copies |
| `artifacts/qa/reports/README.md` | `CONFIRMED draft` | Render-smoke report family is proposed |
| Root `package.json` | `CONFIRMED` | Generic build/test TODO; MapLibre commands executable |
| `scripts/maplibre-smoke-perf.mjs` | `CONFIRMED executable` | Specialized Playwright smoke/perf output |
| `scripts/build-maplibre-render-diff.mjs` | `CONFIRMED executable` | Specialized baseline pixel comparison |
| MapLibre performance envelope | `CONFIRMED` | Specialized thresholds |
| MapLibre render-diff validator | `CONFIRMED executable wrapper` | Schema validation path exists |
| MapLibre render-diff schema | `CONFIRMED permissive` | Current shape enforcement is weak |
| MapLibre workflow | `CONFIRMED substantive` | Executes and uploads specialized artifacts |
| Scenario baseline PNG exact checks | `CONFIRMED absent at checked paths` | Current baseline completeness not established |
| UI-build workflow | `CONFIRMED TODO-only` | No general rendered app producer |
| Root `.gitignore` | `CONFIRMED` | Nested target outputs not protected |
| Checked target report/workflow/schema paths | `CONFIRMED absent at exact paths` | No general lane implementation established |

This evidence supports the documentation boundary only. It does not establish a current passing render run, release approval, deployment, or production use.

[Back to top](#top)

---

<a id="documentation-correction-and-rollback"></a>

## Documentation correction and rollback

This revision changes only `artifacts/qa/reports/render-smoke/README.md`.

It does not change:

- renderer or application source;
- MapLibre scripts or workflow;
- thresholds or baselines;
- schemas or validators;
- fixtures or screenshots;
- report payloads;
- ignore rules;
- receipts, proofs, policy, or release records;
- deployment or public serving.

### Rollback target

Before merge, close the draft pull request or restore prior empty blob:

```text
8b137891791fe96927ad78e64b0aad7bded08bdc
```

After merge, revert the documentation commit or publish a corrective evidence-grounded revision. No renderer, test, release, deployment, data, or production rollback is required for this README-only change.

[Back to top](#top)
