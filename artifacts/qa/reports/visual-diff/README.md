<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-reports-visual-diff-readme
title: artifacts/qa/reports/visual-diff/ — Visual-Difference QA Report, Baseline, and Non-Authority Boundary
type: readme; directory-readme; qa-report-output; visual-difference-report; compatibility-boundary; comparison-inspection-contract
version: v0.1
status: draft; repository-grounded; compatibility-root; transitional; readme-empty-before-revision; gitkeep-tracked; report-payload-not-present; general-comparator-not-established; dedicated-workflow-not-established; report-schema-not-established; retention-not-established; release-binding-unestablished; maplibre-render-diff-confirmed-separate; maplibre-schema-permissive; referenced-baseline-pngs-absent-at-checked-paths; non-authoritative
owners: OWNER_TBD — QA/report steward · Visual-regression steward · UI steward · MapLibre steward · Browser-test steward · Accessibility steward · Security/privacy steward · Rights/sensitivity reviewer · CI/artifact-retention steward · Receipt/proof steward · Release/publication steward · Docs steward
created: 2026-07-16
updated: 2026-07-16
policy_label: public-doc; artifacts; qa; visual-diff; screenshots; baselines; image-comparison; generated-output; inspection-only; no-secrets; no-renderer-authority; no-truth-authority; no-proof-authority; no-policy-authority; no-release-authority; correction-aware; rollback-aware
current_path: artifacts/qa/reports/visual-diff/README.md
truth_posture: CONFIRMED target README existed as an empty tracked file; sibling .gitkeep retains a proposed visual-diff inspection directory; parent artifacts/qa/reports and sibling render-smoke boundaries; Directory Rules and root artifacts README classify artifacts as a transitional compatibility root for derived, regenerable, non-authoritative material; root package declares pixelmatch, Playwright, and pngjs and exposes a MapLibre render-diff command; scripts/build-maplibre-render-diff.mjs compares actual PNG screenshots from artifacts/perf/screenshots with baselines under tests/fixtures/maplibre/baselines, writes diff PNGs and a RenderDiffReport under artifacts/perf/render-diff, distinguishes dimension_mismatch and missing_baseline, uses pixelmatch threshold 0.1, and applies an envelope-owned overall pixel-delta ratio; configs/maplibre/perf-envelope.v1.json sets render_pixel_delta_ratio to 0.01; maplibre-perf-governance workflow executes and validates the separate pipeline and uploads artifacts/perf for 30 days; schemas/maplibre/render-diff-report.schema.json is permissive; the two exact baseline PNG filenames derived from the scripted scenarios were absent at checked paths; tests/fixtures/maplibre/baselines README treats baselines as synthetic review fixtures and not truth, evidence, release, or screenshot archive; root gitignore covers direct artifacts/qa/*.xml only and not this nested report lane; checked visual-diff report/run/summary/workflow/schema paths were absent / PROPOSED immutable comparison identity; explicit actual, expected, diff, algorithm, threshold, mask, viewport, browser, renderer, fixture, source, policy, locale, theme, motion, font, network, and timing scope; normalized findings and finite outcomes; deterministic comparison and anti-aliasing controls; baseline approval separation; screenshot security and rights controls; CI artifact access and expiry; canonical receipt/proof/release linkage; correction, invalidation, supersession, withdrawal, rollback, and lane retirement / CONFLICTED general visual-diff lane versus only a specialized MapLibre comparator; target report lane versus artifacts/perf/render-diff output; root artifacts strict build/docs/qa/temporary scope versus artifacts/perf; permissive schema versus governance language; baseline README no-run posture versus executable comparator; expected baseline naming versus absent scenario PNGs; per-pixel threshold 0.1 versus aggregate ratio threshold 0.01; pixel similarity versus semantic, accessibility, evidence, policy, or release meaning; and generated comparison convenience versus canonical validation memory / UNKNOWN uncommitted local reports, ignored screenshots, CI-only artifacts, historical runs, external visual-regression services, actual current workflow pass status, complete baseline inventory, current screenshots and diffs, active consumers, branch-protection significance, hosting, deployment, production use, and operational rollback / NEEDS VERIFICATION accepted owners, CODEOWNERS, complete recursive inventory, retain/migrate/retire decision, artifacts/perf exception or migration ADR, canonical report and receipt homes, accepted comparison profiles, algorithm and threshold ownership, browser and renderer pins, baseline approval and review duties, mask policy, anti-aliasing and font policy, sensitive-content redaction, artifact retention, release significance, correction consumers, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 524ec92059a367a1f1107a6d0eb781aeadecf948
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  confirmed_lane_files:
    - artifacts/qa/reports/visual-diff/README.md
    - artifacts/qa/reports/visual-diff/.gitkeep
  confirmed_lane_blobs:
    README.md: 8b137891791fe96927ad78e64b0aad7bded08bdc
    .gitkeep: aac94f80c38eb76d6d9c2d3b65a8187d2db88d17
  checked_absent_paths:
    - artifacts/qa/reports/visual-diff/visual-diff-report.json
    - artifacts/qa/reports/visual-diff/visual-diff-run.json
    - artifacts/qa/reports/visual-diff/visual-diff-summary.md
    - .github/workflows/visual-diff.yml
    - schemas/artifacts/visual-diff-report.schema.json
    - tests/fixtures/maplibre/baselines/cache-heavy-layout-slim.png
    - tests/fixtures/maplibre/baselines/cache-light-heavy-paint-heavy.png
  confirmed_specialized_maplibre_surfaces:
    - scripts/build-maplibre-render-diff.mjs
    - scripts/maplibre-smoke-perf.mjs
    - configs/maplibre/perf-envelope.v1.json
    - schemas/maplibre/render-diff-report.schema.json
    - tools/validators/maplibre/validate_render_diff_report.py
    - .github/workflows/maplibre-perf-governance.yml
    - tests/fixtures/maplibre/baselines/README.md
  bounded_inventory_note: tracked repository evidence cannot establish uncommitted local reports, ignored or generated screenshots, CI workspaces, historical workflow artifacts, external visual-regression services, object stores, branch-local outputs, production routes, branch-protection settings, or uninspected subprojects
related:
  - ../README.md
  - ../render-smoke/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../artifacts/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../package.json
  - ../../../../scripts/build-maplibre-render-diff.mjs
  - ../../../../scripts/maplibre-smoke-perf.mjs
  - ../../../../configs/maplibre/perf-envelope.v1.json
  - ../../../../schemas/maplibre/render-diff-report.schema.json
  - ../../../../tools/validators/maplibre/validate_render_diff_report.py
  - ../../../../tests/fixtures/maplibre/baselines/README.md
  - ../../../../.github/workflows/maplibre-perf-governance.yml
  - ../../../../data/receipts/README.md
  - ../../../../data/proofs/README.md
  - ../../../../release/README.md
  - ../../../../.gitignore
tags: [kfm, artifacts, qa, reports, visual-diff, visual-regression, screenshots, baselines, pixelmatch, maplibre, deterministic-rendering, accessibility, sensitive-content, retention, correction, rollback]
notes:
  - "This is the first substantive contract for an otherwise empty README."
  - "The direct lane contains only README.md and .gitkeep in bounded tracked evidence."
  - "No general visual-diff report, producer, schema, dedicated test suite, workflow, retained run manifest, consumer, or release binding was established."
  - "A substantive MapLibre render-diff pipeline exists separately under artifacts/perf/render-diff; this README does not adopt, duplicate, or relocate it."
  - "The checked MapLibre render-diff schema is permissive and the two exact scripted scenario baseline PNGs were absent at checked paths."
  - "A visual difference is an observation about representations, not truth, evidence, accessibility conformance, policy permission, release approval, or publication."
  - "This revision changes documentation only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `artifacts/qa/reports/visual-diff/` — Visual-Difference QA Report, Baseline, and Non-Authority Boundary

> **Purpose.** Define the staging boundary for generated visual-comparison reports without allowing a baseline, screenshot, heatmap, changed-pixel count, similarity score, green workflow, accepted threshold, or human “looks good” judgment to become source truth, semantic correctness, accessibility conformance, evidence closure, policy permission, release approval, publication, or production truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: artifacts compatibility" src="https://img.shields.io/badge/root-artifacts__compatibility-orange">
  <img alt="Direct inventory: README and gitkeep" src="https://img.shields.io/badge/direct__inventory-README%20%2B%20gitkeep-informational">
  <img alt="General comparator: not established" src="https://img.shields.io/badge/general__comparator-NOT__ESTABLISHED-critical">
  <img alt="MapLibre comparator: separate" src="https://img.shields.io/badge/MapLibre__comparator-SEPARATE-blue">
  <img alt="Authority: none" src="https://img.shields.io/badge/trust__authority-none-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Authority](#authority-and-directory-rules-basis) · [Inventory](#confirmed-current-inventory) · [Meaning](#what-visual-diff-can-and-cannot-mean) · [Topology](#comparison-and-report-topology) · [Scope](#comparison-scope-contract) · [Inputs](#actual-expected-and-diff-input-contract) · [Algorithm](#algorithm-threshold-mask-and-region-contract) · [Baselines](#baseline-identity-approval-and-lifecycle) · [Outputs](#output-format-and-routing-contract) · [MapLibre](#confirmed-maplibre-specialized-comparator) · [Determinism](#determinism-fonts-animation-and-network) · [Accessibility](#accessibility-and-trust-visible-state-boundary) · [Security](#security-privacy-rights-and-sensitive-content) · [CI](#producer-ci-artifact-and-retention-contract) · [Outcomes](#validation-non-vacuity-and-finite-outcomes) · [Trust](#receipt-proof-release-and-publication-boundary) · [Correction](#correction-invalidation-and-rollback) · [Done](#definition-of-done) · [Plan](#smallest-sound-implementation-sequence) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

> [!IMPORTANT]
> **Snapshot:** `main@524ec92059a367a1f1107a6d0eb781aeadecf948`<br>
> **Prior README blob:** `8b137891791fe96927ad78e64b0aad7bded08bdc` — empty file<br>
> **Confirmed direct files:** `README.md`, `.gitkeep`<br>
> **General comparator, report, workflow, schema, tests, retention, consumer:** not established<br>
> **Specialized MapLibre comparator:** confirmed elsewhere under `artifacts/perf/render-diff/`<br>
> **Current target authority:** none; reviewer-inspection staging only

`artifacts/qa/reports/visual-diff/` is a repository-confirmed compatibility placeholder. It is **not an operational general visual-regression system**.

### Safe conclusion

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Boundary README | `CONFIRMED` | The path existed, but the README was empty before this revision. |
| Directory retention marker | `CONFIRMED` | `.gitkeep` identifies a proposed visual-diff inspection directory. |
| General visual-diff report | `NOT ESTABLISHED` | No checked report payload exists. |
| General run manifest or summary | `NOT ESTABLISHED` | Checked candidate paths are absent. |
| Dedicated general workflow | `NOT ESTABLISHED` | Checked `.github/workflows/visual-diff.yml` is absent. |
| Dedicated general report schema | `NOT ESTABLISHED` | Checked schema path is absent. |
| General comparator implementation | `NOT ESTABLISHED` | Repository search surfaced only the specialized MapLibre comparator. |
| Root comparison dependencies | `CONFIRMED` | `pixelmatch`, `pngjs`, and Playwright are declared. |
| Specialized MapLibre comparator | `CONFIRMED EXECUTABLE` | It compares PNG screenshots and writes diff images plus a report. |
| Specialized workflow | `CONFIRMED SUBSTANTIVE` | It executes and validates the separate MapLibre pipeline. |
| Specialized report schema | `PERMISSIVE` | The current schema accepts any object shape. |
| Specialized overall pixel ratio | `0.01` | Envelope-owned MapLibre threshold; not a general default. |
| Pixelmatch per-pixel threshold | `0.1` | Script-local comparison sensitivity; distinct from overall ratio. |
| Scenario baseline PNGs | `ABSENT AT CHECKED PATHS` | The two exact filenames derived from scripted scenarios returned not found. |
| Target-lane ignore protection | `NOT ESTABLISHED` | Root ignore rules do not cover nested screenshots, diffs, or reports. |
| Receipt/proof/release binding | `NOT ESTABLISHED FOR THIS LANE` | No canonical trust record points to this target. |
| Current pass rate | `UNKNOWN` | Workflow and implementation presence do not prove the latest run passed. |
| Public or production use | `UNKNOWN` | A comparison artifact or workflow name cannot prove deployment. |
| Truth or release proof | `DENY` | Pixel similarity cannot establish those authorities. |

### Truth labels

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from current repository files, exact paths, executable code, workflow bodies, or bounded search. |
| `PROPOSED` | A recommended object, profile, path, check, or gate not established as current implementation. |
| `CONFLICTED` | Current files, paths, contracts, thresholds, or duties create incompatible expectations. |
| `UNKNOWN` | Not observable or not established from inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently proven for operational reliance or release significance. |
| `DENY` | A prohibited authority, security, evidence, policy, release, or publication interpretation. |

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules state that placement expresses responsibility and that compatibility roots are transitional. The root `artifacts/README.md` permits derived, regenerable, non-authoritative QA material but forbids trust-bearing content.

```text
source UI, documents, maps, styles          apps/ packages/ docs/ configs/
comparison implementation                  scripts/ tools/ packages/
approved baseline fixtures                  tests/fixtures/ or accepted fixture root
generated actual/diff/report output          artifacts/qa/reports/visual-diff/
canonical process memory                    data/receipts/
proof and EvidenceBundle support             data/proofs/
policy decisions                             policy/ and governed decision objects
release and publication decisions            release/
published public-safe products               data/published/ or governed deployment
```

This lane may stage generated comparison outputs. It must not become:

- a baseline fixture authority;
- a renderer implementation root;
- an authored screenshot archive;
- an EvidenceBundle or proof store;
- a canonical receipt store;
- a policy-decision root;
- a release manifest or rollback-card home;
- a public image host;
- a second MapLibre comparator;
- a substitute for accessibility or semantic testing.

### Compatibility conflict

The confirmed MapLibre comparator writes to:

```text
artifacts/perf/render-diff/
```

The root artifacts contract lists ordinary compatibility scope as:

```text
artifacts/build/
artifacts/docs/
artifacts/qa/
artifacts/temporary/
```

This is a governance conflict requiring an accepted exception, migration note, or ADR. This README does not resolve it and does not use the conflict as justification for another parallel output root.

[Back to top](#top)

---

<a id="confirmed-current-inventory"></a>

## Confirmed current inventory

```text
artifacts/qa/reports/visual-diff/
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
artifacts/qa/reports/visual-diff/visual-diff-report.json
artifacts/qa/reports/visual-diff/visual-diff-run.json
artifacts/qa/reports/visual-diff/visual-diff-summary.md
.github/workflows/visual-diff.yml
schemas/artifacts/visual-diff-report.schema.json
```

### Bounded absence

These exact-path checks do not establish that uncommitted, historical, ignored, external-service, branch-local, or dynamically generated equivalents never existed.

[Back to top](#top)

---

<a id="what-visual-diff-can-and-cannot-mean"></a>

## What visual diff can and cannot mean

### Visual diff can observe

- changed pixels between declared images;
- missing or unreadable actual/baseline images;
- dimension or format mismatch;
- declared region changes;
- gross blank-screen or layout shifts;
- visible trust-state changes;
- color, icon, text, or geometry drift;
- screenshot-rendering instability;
- unexpected change outside approved masks;
- threshold exceedance for a declared profile.

### Visual diff cannot prove

- the underlying data is correct;
- the rendered claim is true;
- the screenshot is evidence;
- the citation resolves;
- the EvidenceBundle is complete;
- rights permit public reuse;
- sensitive content is safe beyond configured checks;
- keyboard and screen-reader behavior is correct;
- the page is semantically equivalent;
- the UI works across untested browsers or devices;
- no hidden, intermittent, or off-screen defect exists;
- policy permits exposure;
- release is approved;
- production is healthy.

### Similarity is not equivalence

Two screenshots may be pixel-identical while:

- accessible names are missing;
- focus order is broken;
- evidence links point to the wrong object;
- stale state is hidden in DOM semantics;
- the wrong data is rendered with the same style;
- a private endpoint is called;
- policy state is incorrect;
- interactive behavior is broken.

Two screenshots may differ while the change is acceptable because:

- fonts rasterized differently;
- anti-aliasing changed;
- an approved correction notice appeared;
- a timestamp was intentionally fixed;
- a browser patch changed glyph placement;
- a responsive breakpoint changed;
- a reviewed visual design change was accepted.

[Back to top](#top)

---

<a id="comparison-and-report-topology"></a>

## Comparison and report topology

```text
EXPECTED / BASELINE                   ACTUAL
reviewed fixture image                captured candidate image
        |                                  |
        +---------------+------------------+
                        |
                        v
              COMPARISON PROFILE
algorithm · thresholds · masks · regions · dimensions
                        |
                        v
           OBSERVATIONS + DIFF IMAGE + REPORT
                        |
                        v
      REVIEW / RECEIPT / PROOF / RELEASE HANDOFF
```

### Responsibility matrix

| Responsibility | Owning surface | This lane's relationship |
|---|---|---|
| Application or renderer source | `apps/`, `packages/`, `scripts/` | Input only |
| Visual baseline fixture | accepted `tests/fixtures/` lane | Input only |
| Comparison profile/config | accepted config or tool profile home | Input only |
| Comparator implementation | `scripts/`, `tools/`, package tooling | Producer, not stored here |
| Generated actual/diff/report | this lane, if implemented | Non-authoritative inspection output |
| Specialized MapLibre diff | currently `artifacts/perf/render-diff/` | Separate confirmed implementation |
| Canonical validation memory | accepted report/receipt homes | Referenced, not stored here |
| Evidence/proof | `data/proofs/` | Separate authority |
| Policy decision | governed policy surface | Separate authority |
| Release decision | `release/` | Separate authority |
| Public image or product | governed publication route | Never inferred from this lane |

### Family separation

```text
baseline fixture        ≠ source truth
actual screenshot       ≠ observation of the real world
diff image              ≠ explanation
comparison report       ≠ ValidationReport authority
threshold pass          ≠ policy permission
review approval         ≠ release approval
release approval        ≠ production verification
```

[Back to top](#top)

---

<a id="comparison-scope-contract"></a>

## Comparison scope contract

Every comparison must bind the complete scope that can influence pixels.

### Required identity

| Field | Requirement |
|---|---|
| `comparison_id` | Unique comparison identity |
| `run_id` | Producer-run identity |
| `source_git_sha` | Exact candidate revision |
| `baseline_source_sha` | Revision or immutable source for baseline |
| `actual_ref` | Actual image path plus digest |
| `baseline_ref` | Baseline image path plus digest |
| `diff_ref` | Generated diff path plus digest |
| `profile_ref` | Algorithm/threshold/mask profile plus digest |
| `case_id` | Stable test case identity |
| `surface_ref` | Route, component, map scene, report page, or document |
| `browser` | Engine and version |
| `renderer` | Renderer and version where material |
| `platform` | OS, architecture, runtime |
| `viewport` | Width, height, scale, orientation |
| `locale_timezone` | Language, locale, timezone |
| `theme_motion` | Theme, contrast, reduced-motion posture |
| `fixture_refs` | Input fixture/data digests |
| `network_mode` | denied, local-only, allowlisted, or external |
| `font_asset_refs` | Fonts, glyphs, sprites, images, tiles |
| `dirty_tree` | Whether source or fixture inputs were modified |
| `created_utc` | Comparison time |

### Scope wording

Do not report:

> Visual regression passed.

Report:

> Case `trust-header-deny-chromium-1280x720` was within the accepted profile threshold for the declared actual, baseline, environment, and input digests.

[Back to top](#top)

---

<a id="actual-expected-and-diff-input-contract"></a>

## Actual, expected, and diff input contract

### Actual image

The actual image must identify:

- capture producer;
- source revision;
- surface and case;
- browser, renderer, viewport, and scale;
- theme, locale, timezone, and motion;
- fixture/data refs;
- ready signal or capture timing rule;
- content safety and redaction state;
- digest and media type.

### Baseline image

The baseline must identify:

- baseline id and digest;
- approval status;
- approver or review record;
- source revision and environment;
- intended case and surface;
- creation reason;
- superseded baseline, if any;
- rights and sensitivity posture;
- rollback target.

### Diff image

The diff is derived output. It should identify:

- actual and baseline digests;
- comparison profile;
- algorithm/version;
- changed-region representation;
- mask behavior;
- whether unchanged pixels are retained;
- output digest;
- safe-retention posture.

### No implicit matching

Never match actual and baseline solely by filename when immutable identity can be used. Filenames are convenience labels; digests and case/profile identity govern comparison.

[Back to top](#top)

---

<a id="algorithm-threshold-mask-and-region-contract"></a>

## Algorithm, threshold, mask, and region contract

### Algorithm identity

Record:

- library and version;
- comparison mode;
- color-space treatment;
- alpha handling;
- anti-aliasing handling;
- per-pixel sensitivity;
- aggregate threshold;
- resize or crop behavior;
- dimension mismatch behavior;
- mask and ignore regions;
- output visualization method.

### Two threshold levels

A profile may have both:

1. **Per-pixel sensitivity** — whether a pixel pair counts as changed.
2. **Aggregate acceptance threshold** — how much changed area is allowed.

These must not be conflated.

The confirmed MapLibre implementation currently uses:

```text
pixelmatch threshold:                 0.1
accepted changed-pixel ratio:         0.01
```

Those values belong to the MapLibre profile and are not general defaults.

### Dimension mismatch

Dimension mismatch must not be resized away silently. It should produce a finite finding with:

- actual and expected dimensions;
- viewport and scale;
- browser and renderer versions;
- capture mode;
- safe diagnostic;
- blocking posture.

### Masks

Masks are high-risk because they can hide defects. Every mask needs:

- stable id;
- owner;
- reason;
- exact region or selector;
- case scope;
- creation date;
- expiry or review date;
- evidence that the masked area is truly nondeterministic;
- review of whether important trust state is hidden.

Wildcard masks are prohibited for release-significant surfaces.

### Region analysis

Reports may distinguish:

- changed bounding boxes;
- changed component regions;
- text-only regions;
- map/canvas regions;
- intentionally masked regions;
- unexpectedly unchanged regions when change was expected.

A region label is explanatory metadata, not proof of cause.

[Back to top](#top)

---

<a id="baseline-identity-approval-and-lifecycle"></a>

## Baseline identity, approval, and lifecycle

### Baselines are reviewed expectations

A baseline is not automatically correct because it exists in `tests/fixtures/`. It can preserve an old bug, inaccessible design, stale policy state, sensitive content, or incorrect data.

### Approval separation

When visual diffs affect release:

- the producer may generate a candidate baseline;
- a reviewer evaluates the intended change;
- an authorized steward approves or rejects the baseline;
- the release authority remains separate.

One actor or unreviewed automation should not create a new baseline and declare it acceptable in the same opaque step.

### Baseline states

| State | Meaning |
|---|---|
| `candidate` | Generated for review |
| `approved` | Accepted for a named profile and scope |
| `rejected` | Not suitable |
| `stale` | Inputs or environment changed |
| `superseded` | Replaced by a newer approved baseline |
| `withdrawn` | Unsafe or invalid |
| `rolled_back` | Prior baseline restored |

### Missing baseline

A missing baseline must produce:

```text
BASELINE_MISSING
```

It must not:

- silently bless the actual image;
- produce a zero-delta pass;
- auto-approve a new baseline;
- overwrite a prior reference;
- convert the case to skipped without explanation.

### Baseline storage

Baseline fixtures belong in the accepted test-fixture lane. Generated actuals, diffs, and reports do not belong in the baseline fixture directory.

The current MapLibre baseline README explicitly prohibits using that lane as a screenshot archive or retained CI-output store.

[Back to top](#top)

---

<a id="output-format-and-routing-contract"></a>

## Output format and routing contract

### Proposed target shape

```text
artifacts/qa/reports/visual-diff/
├── README.md
├── visual-diff-run.json
├── visual-diff-report.json
├── visual-diff-summary.md
├── actual/
├── expected/
├── diffs/
└── logs/
```

This shape is **PROPOSED**, not current repository fact. Retaining copies of approved baselines under `expected/` may be unnecessary and should be avoided if immutable references suffice.

### Routing table

| Output | Proposed route | Authority |
|---|---|---|
| Run metadata | `visual-diff-run.json` | Non-authoritative |
| Structured comparisons | `visual-diff-report.json` | Inspection copy |
| Human summary | `visual-diff-summary.md` | Generated summary |
| Actual screenshots | `actual/` | Short-lived, sanitized |
| Baseline references | report fields | Point to fixture authority |
| Diff images | `diffs/` | Derived output |
| Tool logs | `logs/` | Sanitized diagnostics |
| Canonical validation memory | accepted `ValidationReport`/receipt home | Separate |
| Proof or attestation | `data/proofs/` | Separate |
| Release decision | `release/` | Separate |
| Public images | governed publication route | Separate |

### Proposed report skeleton

```yaml
object_type: VisualDiffReport
schema_version: v1
report_id: kfm:visual-diff-report:<id>
run_ref: kfm:visual-diff-run:<id>
source_git_sha: <sha>
profile_ref: <ref>
profile_digest: sha256:<digest>
overall_outcome: PASS
comparisons:
  - case_id: trust-header-deny-chromium
    actual: {ref: actual/trust-header.png, digest: sha256:<digest>}
    baseline: {ref: tests/fixtures/ui/baselines/trust-header.png, digest: sha256:<digest>}
    diff: {ref: diffs/trust-header.diff.png, digest: sha256:<digest>}
    dimensions: {width: 1280, height: 720}
    changed_pixels: 42
    changed_pixel_ratio: 0.000046
    aggregate_threshold: 0.001
    outcome: PASS
summary:
  selected: 1
  compared: 1
  passed: 1
  failed: 0
  missing_baseline: 0
limitations: []
created_utc: <timestamp>
```

[Back to top](#top)

---

<a id="confirmed-maplibre-specialized-comparator"></a>

## Confirmed MapLibre specialized comparator

The repository contains one confirmed executable pixel-comparison implementation.

### Current paths

```text
actual screenshots: artifacts/perf/screenshots/
baseline images:    tests/fixtures/maplibre/baselines/
diff images:        artifacts/perf/render-diff/*.diff.png
report:             artifacts/perf/render-diff/render-diff-report.json
```

### Comparator behavior

`scripts/build-maplibre-render-diff.mjs`:

- reads all `.png` files in the actual screenshot directory;
- selects a baseline with the same filename;
- rejects dimension mismatch;
- compares pixels with `pixelmatch`;
- writes a diff PNG;
- calculates changed-pixel ratio;
- compares that ratio with the envelope threshold;
- records scenario, actual, baseline, diff, status, ratio, threshold, pass flag, and notes;
- writes a `RenderDiffReport`;
- exits nonzero when any scenario fails.

### Current report statuses

The implementation emits:

```text
compared
dimension_mismatch
missing_baseline
```

The top-level report uses:

```text
passed
failed
```

A future general contract should not silently reuse these vocabularies without an accepted mapping.

### Current weaknesses and conflicts

1. The report schema is permissive and does not enforce the script's fields.
2. The baseline README says payload inventory and runner wiring need verification, even though the comparator references the lane.
3. The two exact scenario baseline PNGs were absent at checked paths.
4. The workflow can exist without a verified current passing run.
5. The output lives under `artifacts/perf/`, outside the strict listed compatibility structure.
6. A render-diff report is bundled into a broader proof/release-oriented workflow, but visual similarity remains subordinate to canonical review and release objects.
7. The script matches actual and expected by filename.
8. No general visual-diff producer writes to this target.

### Relationship to this lane

This README does not:

- move the MapLibre comparator;
- change its threshold;
- create its baselines;
- change its schema;
- declare its report canonical here;
- duplicate its report;
- weaken or replace its workflow;
- resolve the `artifacts/perf/` placement conflict.

[Back to top](#top)

---

<a id="determinism-fonts-animation-and-network"></a>

## Determinism, fonts, animation, and network

### Deterministic inputs

A reproducible comparison should pin:

- browser and renderer versions;
- OS/container and graphics stack;
- viewport, scale, zoom, and orientation;
- fonts, glyphs, sprites, icons, and images;
- styles, tiles, shaders, and plugins;
- fixture data and API responses;
- locale, timezone, and language;
- clock, random seeds, and UUIDs;
- animation, transition, and reduced-motion state;
- cache, service-worker, and storage posture;
- network allowlist or denial;
- comparison algorithm and thresholds;
- baseline digest.

### Font and anti-aliasing variance

Text rendering can differ by OS, font installation, browser patch, GPU path, and anti-aliasing. Profiles should either:

- run in a pinned environment;
- package the exact fonts;
- define reviewed text-region tolerances;
- use semantic assertions in addition to pixels;
- mark noncomparable runs honestly.

### Animation

Capture only after an explicit stable-ready signal. Avoid arbitrary sleep when a deterministic condition can be asserted.

### Network classes

| Class | Meaning |
|---|---|
| `deny` | No network |
| `local-only` | Loopback fixture services |
| `allowlisted` | Explicit immutable or controlled hosts |
| `external` | Mutable third-party services |

External assets must be disclosed because they can alter pixels without source changes.

### Comparison classes

| Result | Meaning |
|---|---|
| `PIXEL_IDENTICAL` | No changed pixels |
| `WITHIN_THRESHOLD` | Difference remains within accepted profile |
| `EXPECTED_CHANGE` | Reviewed change matches declared expectation |
| `NONCOMPARABLE` | Environment or inputs differ materially |
| `UNEXPECTED_DIFFERENCE` | Review required |
| `ERROR` | Comparison did not complete |
| `NOT_RUN` | No comparison attempted |

[Back to top](#top)

---

<a id="accessibility-and-trust-visible-state-boundary"></a>

## Accessibility and trust-visible-state boundary

### Pixels do not prove accessibility

A visual diff cannot determine:

- accessible names;
- focus order;
- keyboard reachability;
- live-region announcements;
- semantic heading structure;
- form labels;
- screen-reader reading order;
- reduced-motion behavior beyond visible frames;
- whether color-only meaning is announced.

Accessibility requires separate semantic and interaction checks.

### Useful bounded visual checks

A visual profile may inspect:

- visible focus indicator;
- color contrast snapshots as a cue;
- text-plus-icon trust labels;
- zoom and narrow-viewport reflow;
- high-contrast theme layout;
- reduced-motion final state;
- visible error/deny/abstain labels;
- map/list alternative presence;
- correction and stale-state visibility.

A pass means only the configured visual cue was present in the compared image.

### Trust-visible comparisons

Release-significant visual cases should cover, where applicable:

- `ANSWER`;
- `ABSTAIN`;
- `DENY`;
- `ERROR`;
- loading and cancelled;
- stale and restricted;
- corrected, superseded, withdrawn, and rolled back;
- source role and evidence count;
- rights and sensitivity;
- review and release state;
- map geometry/reality boundary;
- non-map fallback.

The comparison must not expose restricted values merely to prove a redaction state.

[Back to top](#top)

---

<a id="security-privacy-rights-and-sensitive-content"></a>

## Security, privacy, rights, and sensitive content

Screenshots and diffs can leak protected material even when logs are clean.

### Prohibited retained content

- tokens, cookies, authorization headers, or credentials;
- private URLs, hostnames, signed queries, or filesystem paths;
- RAW, WORK, or QUARANTINE content;
- precise rare-species, archaeology, cultural, or private-well locations;
- living-person, DNA, land-ownership, or protected community data;
- restricted infrastructure detail;
- unreleased internal identifiers;
- confidential browser storage;
- copyrighted or licensed imagery without accepted reuse rights;
- hidden data exposed by diff amplification.

### Required controls

1. Use synthetic or public-safe fixtures by default.
2. Clear cookies, storage, and cache between cases.
3. Deny production credentials.
4. Redact URLs, console output, DOM excerpts, filenames, and metadata.
5. Generalize protected spatial detail.
6. Scan actual, expected, and diff images.
7. Review screenshot and baseline rights.
8. Prevent public artifact access unless separately approved.
9. Record redaction transforms and reasons where material.
10. Withdraw unsafe artifacts immediately.

### Diff amplification risk

A diff image can reveal content intentionally hidden in either the actual or baseline through contrast enhancement. Security review must include the derived diff, not only source screenshots.

### Active report content

HTML summaries must not embed untrusted scripts or uncontrolled remote assets. Prefer static, sanitized output.

[Back to top](#top)

---

<a id="producer-ci-artifact-and-retention-contract"></a>

## Producer, CI artifact, and retention contract

### Producer obligations

A future general comparator should:

- fail on zero selected cases;
- reject unreadable images;
- reject missing required baselines;
- treat dimension mismatch explicitly;
- bind image and profile digests;
- distinguish per-pixel and aggregate thresholds;
- validate masks and regions;
- emit deterministic ordering;
- write atomically;
- sanitize diagnostics;
- avoid automatic baseline approval;
- return stable exit codes;
- preserve correction and supersession refs.

### CI stages

```text
prepare deterministic inputs
        |
capture actual images
        |
validate actual-image safety
        |
compare with approved baselines
        |
validate report shape and non-vacuity
        |
upload bounded artifacts
        |
write canonical memory when required
        |
separate policy/release decision
```

### Artifact names

```text
visual-diff-<profile>-<run-id>
visual-diff-failure-<profile>-<run-id>
```

### Retention classes

| Class | Typical purpose | Requirement |
|---|---|---|
| `ephemeral` | local debugging | delete after run |
| `ci-short` | pull-request review | bounded retention |
| `investigation` | active defect | owner and expiry |
| `release-candidate` | release review support | canonical references |
| `public-disclosure` | approved public explanation | separate publication approval |

The specialized MapLibre workflow uses 30-day retention. That does not establish this target's retention policy.

### Access

Artifacts containing screenshots should default to the narrowest practical audience. Public access requires separate rights, sensitivity, and release review.

[Back to top](#top)

---

<a id="validation-non-vacuity-and-finite-outcomes"></a>

## Validation, non-vacuity, and finite outcomes

### A report must not pass when

- zero comparisons were selected;
- zero actual images were captured;
- every comparison was skipped;
- all baselines were missing;
- images could not be decoded;
- dimensions differed and were silently resized;
- the comparison profile was absent;
- the report parser failed;
- all differences were hidden by wildcard masks;
- only placeholder files were compared;
- output paths escaped the artifact root;
- actual and baseline were accidentally the same file;
- baseline digest did not match the approved reference;
- the actual image was stale relative to source revision;
- unsafe content was found;
- external assets failed and the page silently degraded.

### Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Required configured comparisons passed for the declared scope |
| `WARN` | Non-blocking difference requires visibility |
| `FAIL` | Blocking unexpected difference |
| `HOLD` | Unsafe, stale, incomplete, or noncomparable |
| `ABSTAIN` | Insufficient context or missing dependency |
| `DENY` | Security, rights, sensitivity, policy, or exposure prohibition |
| `ERROR` | Tool, decode, storage, or environment failure |
| `REVIEW_REQUIRED` | Human determination required |
| `EMPTY_SCOPE` | No meaningful comparison selected |
| `PROFILE_NOT_ESTABLISHED` | No accepted profile bound |
| `BASELINE_MISSING` | Required baseline absent |
| `BASELINE_CONFLICT` | Multiple or incompatible approved baselines |
| `DIMENSION_MISMATCH` | Actual and expected sizes differ |
| `NONCOMPARABLE` | Material environment or input drift |
| `MASK_INVALID` | Mask missing, expired, or overbroad |
| `PLACEHOLDER_ONLY` | Only scaffolding was exercised |
| `NOT_RUN` | Comparison intentionally not executed |

### Composition rule

The top-level outcome should preserve the most restrictive material child outcome. A sensitive-content denial must not be averaged away by many visually identical cases.

[Back to top](#top)

---

<a id="receipt-proof-release-and-publication-boundary"></a>

## Receipt, proof, release, and publication boundary

```text
visual-diff report
       |
       +--> validation receipt / ValidationReport when material
       |
       +--> proof or attestation when material
       |
       +--> policy and steward review
       |
       +--> release decision
       |
       +--> governed publication/deployment
```

### Non-collapse rules

- Actual screenshot is not evidence of the underlying claim.
- Baseline screenshot is not an approved product.
- Diff image is not an explanation of cause.
- Pixel threshold is not a policy rule.
- Comparison report is not a receipt merely because it records a run.
- A passing workflow is not a ReleaseManifest.
- Artifact upload is not publication.
- Human “looks good” is not a governed approval without a recorded review state.
- Visual similarity does not override a semantic, accessibility, security, evidence, policy, or release failure.

### Canonical memory

This lane is replaceable and expirable. Long-lived decisions must point to immutable digests and canonical records outside the compatibility output tree.

[Back to top](#top)

---

<a id="correction-invalidation-and-rollback"></a>

## Correction, invalidation, and rollback

### Invalidate comparisons when

- source revision changes;
- baseline changes;
- fixture/data inputs change;
- browser, renderer, OS, font, or graphics stack changes materially;
- algorithm or threshold changes;
- mask or region policy changes;
- rights or sensitivity posture changes;
- a screenshot leaks protected content;
- baseline approval is withdrawn;
- comparison logic is found defective;
- correction or withdrawal affects the rendered surface;
- the report is stale for its decision.

### Correction procedure

1. mark the report invalid, stale, superseded, or withdrawn;
2. identify affected comparison ids and digests;
3. preserve the reason and lineage;
4. remove unsafe actual, baseline copies, and diffs from accessible storage;
5. invalidate cached summaries and links;
6. restore or select the correct approved baseline;
7. rerun with corrected inputs when permitted;
8. update canonical receipts, proofs, reviews, and release records where material;
9. preserve the rollback target.

### Rollback table

| Change | Rollback |
|---|---|
| README-only change | revert documentation commit |
| Comparator change | revert producer/profile and rerun |
| Baseline change | restore prior approved baseline |
| Threshold change | restore prior profile |
| Mask change | restore prior reviewed mask or remove it |
| Unsafe artifact | delete/withdraw and update references |
| Release-significant defect | execute governed correction/rollback |

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This lane is operational only when all applicable conditions are satisfied:

- [ ] Owners and CODEOWNERS are accepted.
- [ ] Retain, migrate, or retire decision is recorded.
- [ ] `artifacts/perf/` placement is resolved or explicitly excepted.
- [ ] One general comparator and registry id are accepted.
- [ ] Report and run-manifest contracts have meaningful schemas.
- [ ] Actual, baseline, diff, and profile identities are digest-bound.
- [ ] Browser, renderer, platform, viewport, scale, locale, theme, motion, and font profiles are pinned.
- [ ] Baseline creation, review, approval, supersession, and rollback duties are defined.
- [ ] Algorithm, per-pixel sensitivity, aggregate threshold, masks, and region semantics are owned.
- [ ] Missing-baseline and dimension-mismatch cases fail safely.
- [ ] Zero-scope and same-file canaries exist.
- [ ] External-resource policy is explicit.
- [ ] Sensitive-content and secret scanning cover actual, baseline, and diff images.
- [ ] Accessibility and semantic checks remain separate.
- [ ] Reports are deterministic and non-vacuous.
- [ ] CI uploads bounded artifacts with an access and expiry policy.
- [ ] Canonical receipt/proof/release handoffs are documented and tested.
- [ ] Correction, withdrawal, supersession, and rollback are tested.
- [ ] No report in this lane is served directly as public truth.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Phase 1 — Decide placement and ownership

- decide whether this lane is retained;
- resolve or record the `artifacts/perf/` exception;
- assign owners;
- prohibit parallel comparator authority.

### Phase 2 — Define contracts

- accept comparison profile;
- accept report and run-manifest semantics;
- create meaningful schemas;
- define finite outcomes and reason codes.

### Phase 3 — Implement a minimal comparator

- one synthetic local-only case;
- one actual and approved baseline;
- explicit dimensions;
- digest binding;
- missing-baseline and same-file canaries;
- structured report and diff image.

### Phase 4 — Stabilize determinism

- pin browser, platform, viewport, fonts, locale, time, motion, and assets;
- define network mode;
- add anti-aliasing and nondeterminism policy;
- test independent reruns.

### Phase 5 — Add governance controls

- baseline approval separation;
- mask owner/reason/expiry;
- sensitive-content and rights scanning;
- accessibility and semantic companion checks.

### Phase 6 — Wire CI and canonical memory

- dedicated workflow;
- report validation;
- bounded artifact retention;
- receipt/proof linkage where required;
- required-check decision by owners.

### Phase 7 — Exercise correction and rollback

- stale baseline;
- missing baseline;
- dimension mismatch;
- unsafe screenshot;
- changed threshold;
- expired mask;
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
4. Canonical general visual comparator.
5. Comparator registry id and CLI/exit-code contract.
6. Canonical run-manifest contract.
7. Canonical report contract.
8. Meaningful report schema.
9. Actual-image identity contract.
10. Baseline identity contract.
11. Diff-image identity contract.
12. Browser and renderer matrix.
13. OS/container and graphics-stack matrix.
14. Viewport, scale, zoom, and orientation profiles.
15. Theme, locale, timezone, and motion profiles.
16. Font, glyph, icon, sprite, tile, and style pins.
17. Fixture/data ownership and digests.
18. Complete baseline inventory.
19. Missing scenario baseline PNG disposition.
20. Baseline approval roles.
21. Baseline candidate-generation policy.
22. Baseline supersession and rollback.
23. Per-pixel algorithm and version.
24. Per-pixel sensitivity ownership.
25. Aggregate changed-ratio ownership.
26. Color-space and alpha semantics.
27. Anti-aliasing policy.
28. Dimension mismatch policy.
29. Resize/crop prohibition or rules.
30. Region and bounding-box semantics.
31. Mask creation, ownership, and expiry.
32. Wildcard-mask prohibition.
33. Same-file actual/baseline canary.
34. Blank-image and unchanged-when-change-expected canaries.
35. Network deny/local/allowlist policy.
36. External-resource disclosure.
37. Cache and service-worker posture.
38. Sensitive-location redaction.
39. Screenshot and baseline rights review.
40. Diff-amplification review.
41. Credential, cookie, storage, and private-path isolation.
42. Accessibility companion checks.
43. Semantic companion checks.
44. Artifact access and retention.
45. Canonical receipt linkage.
46. Proof/attestation linkage.
47. Release and branch-protection significance.
48. Correction and cache invalidation.
49. Operational rollback drill.
50. Production consumers, metrics, deployment, and current pass state.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports |
|---|---|---|
| Target prior blob `8b137891...` | `CONFIRMED` | README was empty |
| `.gitkeep` blob `aac94f80...` | `CONFIRMED` | Proposed visual-diff lane |
| Directory Rules | `CONFIRMED doctrine` | Placement by responsibility; compatibility roots transitional |
| Root `artifacts/README.md` | `CONFIRMED draft boundary` | Derived, regenerable, non-authoritative QA only |
| `artifacts/qa/reports/README.md` | `CONFIRMED draft` | Visual-diff report family is proposed |
| Render-smoke sibling | `CONFIRMED grounded boundary` | Render smoke and visual diff remain separate concepts |
| Root `package.json` | `CONFIRMED` | Pixelmatch/PNG/Playwright dependencies and MapLibre command |
| MapLibre comparator script | `CONFIRMED executable` | Actual/baseline/diff/report behavior |
| MapLibre performance envelope | `CONFIRMED` | Aggregate ratio 0.01 |
| MapLibre workflow | `CONFIRMED substantive` | Executes, validates, uploads 30-day artifacts |
| MapLibre report schema | `CONFIRMED permissive` | Weak shape enforcement |
| MapLibre baseline README | `CONFIRMED draft` | Fixtures are not truth or retained CI output |
| Exact scenario baseline checks | `CONFIRMED absent at checked paths` | Baseline completeness not established |
| Root `.gitignore` | `CONFIRMED` | Nested visual artifacts not protected |
| Checked target report/workflow/schema paths | `CONFIRMED absent` | No general lane implementation established |

This evidence supports the documentation boundary only. It does not establish a current passing comparison, approved baseline set, release decision, deployment, or production use.

[Back to top](#top)

---

<a id="documentation-correction-and-rollback"></a>

## Documentation correction and rollback

This revision changes only:

```text
artifacts/qa/reports/visual-diff/README.md
```

It does not change:

- application or renderer source;
- comparator scripts;
- algorithms or thresholds;
- schemas or validators;
- fixtures or baselines;
- screenshots or diff images;
- workflows or artifact retention;
- ignore rules;
- receipts, proofs, policy, or release records;
- deployment or public serving.

### Rollback target

Before merge, close the draft pull request or restore the prior empty blob:

```text
8b137891791fe96927ad78e64b0aad7bded08bdc
```

After merge, revert the documentation commit or publish a corrective evidence-grounded revision. No application, renderer, test, release, deployment, data, or production rollback is required for this README-only change.

[Back to top](#top)
