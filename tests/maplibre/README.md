<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-maplibre-readme
title: tests/maplibre/ — MapLibre Renderer, Performance, Visual-Diff, and Governance Test Lane
type: readme; directory-readme; renderer-test-index; performance-proof-guardrail; visual-regression-boundary
version: v0.2
status: draft; repository-present-executable-tests; performance-workflow-present; mixed-maturity; network-posture-conflicted; proof-chain-broken; placement-needs-verification; NEEDS VERIFICATION
policy_label: public-doc; restricted-review-when-sensitive-map-output-is-in-scope
owners: OWNER_TBD — QA steward · MapLibre steward · Map-runtime steward · UI steward · Performance steward · Visual-regression steward · Policy steward · Security/sensitivity reviewer · Release steward · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
current_path: tests/maplibre/README.md
truth_posture: CONFIRMED target README and prior blob, tests responsibility root, two direct executable Python files, three negative scalar-budget tests, synthetic MapLibre fixture lanes, root npm and Make targets, MapLibre smoke/render-diff scripts, MapLibre performance workflow, permissive MapLibre schemas, validator wrappers, placeholder governance validator, external network dependencies, proposed MapLibre ADRs, explorer-web adapter-boundary test, and artifacts/perf output behavior at the pinned snapshot / CONFLICTED tests/maplibre versus tests/packages/maplibre placement, no-network doctrine versus external CDN/runtime calls, tests versus workflow coverage, repository-root scripts versus package ownership, apps/web workflow filters versus apps/explorer-web, artifacts/perf outputs versus governed receipt/proof/release roots, and proposed sole-renderer/package-importer decisions versus current implementation / UNKNOWN current pass state, browser reproducibility, package consumer graph, accepted MapLibre version and plugin set, production renderer behavior, sensitive-surface coverage, release integration, and operational health / NEEDS VERIFICATION owners, placement decision, package/API implementation, lockfile and dependency policy, hermetic fixture strategy, schema hardening, governance validator implementation, CI trigger repair, test expansion, artifact migration, correction propagation, and rollback proof
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: c42adda522241315e03176947c437d14ce15fb46
  prior_blob: 4c5d24be322fcbff1a98aa255adc1be26b168ba6
related:
  - ../README.md
  - ../fixtures/maplibre/README.md
  - ./perf_fixture_builder.py
  - ./test_perf_governance_negative_paths.py
  - ../../packages/maplibre/README.md
  - ../../packages/maplibre/src/README.md
  - ../../tests/policy/test_explorer_web_adapter_boundary.py
  - ../../configs/maplibre/perf-envelope.v1.json
  - ../../schemas/maplibre/perf-envelope.schema.json
  - ../../schemas/maplibre/render-diff-report.schema.json
  - ../../schemas/maplibre/perf-proof-pack.schema.json
  - ../../tools/validators/maplibre/README.md
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../tools/validators/maplibre/validate_render_diff_report.py
  - ../../tools/validators/maplibre/validate_perf_governance.py
  - ../../tools/validators/maplibre/validate_perf_proof_pack.py
  - ../../scripts/maplibre-smoke-perf.mjs
  - ../../scripts/build-maplibre-render-diff.mjs
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../docs/quality/maplibre-perf-governance.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, tests, maplibre, renderer-boundary, performance, visual-regression, playwright, pixelmatch, fixtures, negative-tests, network-hermeticity, schema-validation, receipts, proof-pack, release-manifest, correction, rollback, no-parallel-authority]
notes:
  - "v0.2 replaces a mostly aspirational README with a repository-grounded test, workflow, proof-boundary, and remediation contract."
  - "The lane contains executable Python tests, but those tests validate only three scalar fixture constraints and do not exercise the browser renderer or the current performance workflow."
  - "The MapLibre performance workflow is substantive but currently cannot be treated as closed proof because of trigger gaps, lockfile absence, external network dependencies, permissive schemas, and a placeholder governance validator invoked without required arguments."
  - "This revision changes documentation only and creates, moves, deletes, or activates no test, fixture, schema, validator, workflow, script, package, artifact, policy, or release record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/maplibre/` — MapLibre Renderer, Performance, Visual-Diff, and Governance Test Lane

> **Purpose.** Prove that MapLibre-facing code and artifacts remain downstream of KFM evidence, policy, lifecycle, release, correction, and rollback controls while renderer performance and visual behavior are tested reproducibly and without turning screenshots, tiles, styles, metrics, or generated proof-shaped files into sovereign truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Implementation: partial" src="https://img.shields.io/badge/implementation-partial-orange">
  <img alt="Workflow: conflicted" src="https://img.shields.io/badge/workflow-CONFLICTED-red">
  <img alt="Renderer: downstream only" src="https://img.shields.io/badge/renderer-downstream__only-critical">
</p>

> [!IMPORTANT]
> `tests/maplibre/` is an enforceability-proof lane. It is not renderer implementation, fixture authority, source or layer authority, schema or contract authority, policy authority, receipt or proof storage, release authority, or publication authority.

> [!WARNING]
> Current repository evidence does **not** support calling the MapLibre performance chain closed or release-ready. The workflow is substantive, but the checked root has no `package-lock.json` for its `npm ci` step, the smoke harness uses external CDN resources, the MapLibre schemas accept any object, and `validate_perf_governance.py` is a placeholder that exits with code `2` when the workflow invokes it without file arguments.

## Quick navigation

[Status](#status-and-evidence-boundary) · [Placement](#placement-and-authority) · [Inventory](#confirmed-implementation-inventory) · [Current tests](#current-python-test-coverage) · [Workflow](#performance-and-visual-governance-workflow) · [Conflicts](#confirmed-proof-and-wiring-conflicts) · [Invariants](#renderer-and-trust-membrane-invariants) · [Coverage](#required-test-families) · [Visual diff](#visual-regression-and-baseline-rules) · [Network](#network-hermeticity-and-dependency-control) · [Artifacts](#artifact-receipt-proof-and-release-boundary) · [Fixtures](#fixture-contract) · [CI](#ci-and-gate-acceptance) · [Authoring](#test-authoring-contract) · [Validation](#validation) · [Done](#definition-of-done) · [Migration](#placement-and-implementation-migration) · [Rollback](#correction-and-rollback) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis)

---

## Status and evidence boundary

| Surface | Status at the pinned snapshot | Safe conclusion |
|---|---|---|
| `tests/maplibre/README.md` | **CONFIRMED** | Target exists; prior blob is pinned in metadata. |
| `perf_fixture_builder.py` | **CONFIRMED executable helper** | Builds a frozen three-field Python fixture and performs local scalar checks. |
| `test_perf_governance_negative_paths.py` | **CONFIRMED pytest module** | Contains three negative tests for zero frame budget, negative memory budget, and out-of-range tile error rate. |
| Other direct test modules under `tests/maplibre/` | **NOT SURFACED in bounded search** | Do not invent broader executable coverage. |
| `tests/fixtures/maplibre/` | **CONFIRMED parent and child README lanes** | `tiny/`, `baselines/`, `invalid/`, and `bad-baselines/` are documented; payload completeness remains unverified. |
| Root npm commands | **CONFIRMED** | MapLibre perf, diff, attestation, manifest, proof, governance, failure, correction, and cleanup commands are declared. |
| Make targets | **CONFIRMED** | `maplibre-perf`, `maplibre-govern`, `maplibre-proof`, and `maplibre-clean` exist. |
| MapLibre performance workflow | **CONFIRMED substantive workflow** | Runs browser smoke, render diff, validators, attestation, manifest/proof builders, and artifact upload. |
| Current workflow success | **NOT ESTABLISHED** | Source inspection is not a successful run. Several checked conditions predict failure or incomplete proof. |
| Package implementation | **CONFIRMED scaffold / not functional adapter** | `packages/maplibre/` is a private `0.0.0` workspace scaffold with a placeholder source export and no established consumer. |
| ADR-0006 single-importer boundary | **CONFIRMED document / PROPOSED** | Tests may track it, but this README cannot treat it as accepted architecture. |
| ADR-0007 sole-renderer decision | **CONFIRMED document / PROPOSED** | Additional-renderer denial tests are acceptance work, not current authoritative behavior. |
| Production renderer behavior | **UNKNOWN** | Test, workflow, and README presence do not prove deployed public behavior. |

**Authority of this README:** lane routing, current evidence disclosure, test expectations, negative-state coverage, fixture discipline, CI acceptance criteria, and correction/rollback guidance.

Executable tests, package code, accepted ADRs, contracts, schemas, policy, workflow definitions, CI logs, emitted receipts and proofs, release records, and steward decisions outrank this README.

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified in current repository evidence or commit metadata. |
| **PROPOSED** | A design or implementation expectation not yet accepted or proven. |
| **CONFLICTED** | Repository surfaces disagree or implement incompatible postures. |
| **NEEDS VERIFICATION** | Checkable, but not sufficiently proven for reliance. |
| **UNKNOWN** | Not established by inspected evidence. |

---

## Placement and authority

Directory Rules place files by primary responsibility:

```text
tests/                            enforceability proof
tests/fixtures/                   unit-test-scoped synthetic examples
packages/maplibre/                reusable MapLibre adapter/package implementation
apps/explorer-web/                deployable browser shell
tools/validators/maplibre/        reusable validation implementation
configs/maplibre/                 non-secret threshold/config declarations
schemas/                          machine-checkable shape
contracts/                        semantic meaning
policy/                           allow / deny / restrict / abstain
artifacts/                        temporary build/QA outputs only
data/receipts/ and data/proofs/   governed emitted audit/proof records
release/                          promotion, correction, withdrawal, rollback authority
```

`tests/maplibre/` is correctly inside the `tests/` responsibility root. Its narrower placement remains **NEEDS VERIFICATION** because repository documentation also discusses `tests/packages/maplibre/` as a possible package-scoped home.

### Current path class

| Field | Value |
|---|---|
| Primary responsibility | MapLibre and renderer-boundary enforceability proof |
| Repository status | Present with executable Python helper/tests |
| Placement status | `CURRENT / NEEDS VERIFICATION` |
| Alternate discussed path | `tests/packages/maplibre/` |
| Duplicate posture | Do not create a second executable suite without an explicit migration plan |
| Fixture companion | `tests/fixtures/maplibre/` |
| Required reviewers | QA, MapLibre/runtime, UI, performance, policy/security, release, CI, docs |

The safe interim rule is:

1. keep current executable tests in `tests/maplibre/`;
2. do not duplicate them under `tests/packages/maplibre/`;
3. record any eventual move as a reviewed migration;
4. update workflow path filters and fixture references atomically;
5. preserve history and rollback through normal commits.

### Authority routing

| Concern | Owning home | This lane's role |
|---|---|---|
| Renderer adapter implementation | `packages/maplibre/` | Test; never implement here |
| Browser shell and map UI | `apps/explorer-web/` | Test public behavior and boundaries |
| Performance thresholds | `configs/maplibre/` plus accepted policy/review | Assert; do not silently redefine |
| Schema shape | `schemas/` | Exercise validators and negative fixtures |
| Semantic meaning | `contracts/` | Assert declared behavior |
| Renderer admission policy | `policy/` | Test finite outcomes |
| Synthetic MapLibre inputs | `tests/fixtures/maplibre/` or accepted shared fixtures | Consume; do not duplicate |
| Validator code | `tools/validators/maplibre/` | Unit/integration test |
| Temporary screenshots/diffs | `artifacts/qa/` or tightly scoped temporary artifact lane | Inspect as ephemeral test outputs |
| Trust-bearing receipts/proofs | `data/receipts/`, `data/proofs/` | Assert creation and linkage |
| Release/correction/rollback | `release/` | Assert gate behavior; never decide |

---

## Confirmed implementation inventory

### Direct test-lane files

```text
tests/maplibre/
├── README.md
├── perf_fixture_builder.py
└── test_perf_governance_negative_paths.py
```

Bounded search did not surface another direct executable test module.

### Fixture documentation lanes

```text
tests/fixtures/maplibre/
├── README.md
├── tiny/
├── baselines/
├── invalid/
└── bad-baselines/
```

README presence does not prove that all expected fixture payloads exist, are current, or are consumed.

### Operational and validation surfaces

```text
configs/maplibre/perf-envelope.v1.json

scripts/
├── maplibre-smoke-perf.mjs
├── build-maplibre-render-diff.mjs
├── attest-maplibre-perf.mjs
├── build-maplibre-perf-release-manifest.mjs
├── build-maplibre-perf-proof-pack.mjs
├── build-maplibre-perf-correction-and-rollback.mjs
└── build-maplibre-perf-failure-bundle.mjs

tools/validators/maplibre/
├── validate_perf_envelope.py
├── validate_render_diff_report.py
├── validate_perf_governance.py
├── validate_perf_proof_pack.py
└── related validator entry points

.github/workflows/
└── maplibre-perf-governance.yml
```

The existence of this chain establishes operational intent and partial implementation—not proof closure.

---

## Current Python test coverage

`perf_fixture_builder.py` defines:

```text
PerfGovernanceFixture
├── frame_budget_ms
├── memory_budget_mb
└── tile_error_rate
```

Its validator reports an error when:

- `frame_budget_ms <= 0`;
- `memory_budget_mb <= 0`;
- `tile_error_rate` is outside `[0, 1]`.

`test_perf_governance_negative_paths.py` contains exactly three confirmed tests for those cases.

### What these tests prove

They prove that a small local Python helper rejects three invalid scalar values.

### What these tests do not prove

They do not currently prove:

- `configs/maplibre/perf-envelope.v1.json` matches its schema;
- the configured thresholds are the same as the Python helper fields;
- Playwright can launch;
- MapLibre loads;
- source/style/glyph requests succeed;
- frame and load measurements are valid;
- screenshots match baselines;
- the render-diff report is complete;
- the proof pack, run receipt, manifest, attestation, correction, or rollback objects are valid;
- the workflow runs;
- the package boundary is enforced;
- released/public-safe artifacts are the only rendered inputs;
- sensitive data cannot leak;
- a failed renderer or missing source cannot be misclassified as a successful performance run.

The helper's fields also differ from the checked JSON envelope, which uses:

```text
avg_frame_ms
p95_frame_ms
idle_ms
load_ms
render_pixel_delta_ratio
```

A migration or pairing decision is required before the helper tests can be described as direct `PerfEnvelope` schema tests.

---

## Performance and visual governance workflow

The MapLibre workflow currently performs a substantial chain:

```text
checkout
  -> Node and Python setup
  -> npm ci
  -> Playwright Chromium install
  -> Python validator dependency install
  -> PerfEnvelope schema wrapper
  -> local fixture HTTP server
  -> browser smoke/performance run
  -> render-diff builder
  -> render-diff schema wrapper
  -> attestation builder
  -> release-manifest-shaped builder
  -> governance validator
  -> proof-pack-shaped builder
  -> proof-pack schema wrapper
  -> final governance validator
  -> success/failure artifact upload
```

The root package and Makefile expose related commands.

### Confirmed browser-smoke behavior

The smoke script:

- launches Chromium through Playwright;
- runs two hard-coded scenarios;
- serves local style references from `localhost:8080`;
- imports MapLibre GL JS `5.5.0` and CSS from `unpkg.com`;
- loads glyphs from `demotiles.maplibre.org`;
- measures load, idle, average frame, and p95 frame timing;
- saves frame-time CSV files and screenshots;
- emits `perf-results.json` and a `RunReceipt`-shaped JSON file under `artifacts/perf/`.

The render-diff builder:

- compares generated screenshots with PNG baselines under `tests/fixtures/maplibre/baselines/`;
- uses the configured pixel-delta threshold;
- emits diff PNGs and `render-diff-report.json`;
- exits non-zero when baselines are missing, dimensions mismatch, or pixel deltas exceed threshold.

### Current safe interpretation

These scripts are useful performance and visual-regression harnesses. Their outputs are candidate QA artifacts until schema, identity, integrity, receipt/proof, policy, review, and release requirements close in accepted authority roots.

---

## Confirmed proof and wiring conflicts

### 1. Governance validator invocation is broken

`validate_perf_governance.py` is a placeholder file-existence checker.

Its behavior is:

```text
no file arguments -> exit 2
missing file       -> exit 1
existing files     -> print OK
```

The workflow, Makefile, and npm `maplibre:govern` command invoke it with **no arguments**.

Therefore the checked invocation does not perform the documented governance checks and exits with code `2`.

### 2. Schema wrappers are structurally permissive

The checked schemas for:

- `PerfEnvelope`;
- `RenderDiffReport`;
- `PerfProofPack`;

contain only an object type with `additionalProperties: true`.

A passing JSON Schema wrapper currently proves only that the instance is an object. It does not validate required fields, finite outcomes, thresholds, digests, identities, subjects, evidence refs, release refs, correction refs, or rollback targets.

### 3. Workflow install requires an absent root lockfile

The workflow runs:

```bash
npm ci
```

No root `package-lock.json` was found at the checked path. The workflow cannot be considered reproducible or runnable until the package-manager and lockfile strategy are resolved.

### 4. No-network posture conflicts with the smoke harness

The workflow starts a local fixture server, but the browser page still requests:

- MapLibre JavaScript and CSS from `unpkg.com`;
- glyph assets from `demotiles.maplibre.org`.

This is not a hermetic no-network test. It is vulnerable to network availability, CDN changes, upstream retention, and supply-chain drift.

### 5. Workflow filters omit important implementation and test paths

The checked workflow watches:

- `apps/web/**`;
- MapLibre scripts;
- `schemas/maplibre/**`;
- `tools/validators/maplibre/**`;
- `configs/maplibre/**`;
- `tests/fixtures/maplibre/**`.

It does not watch:

- `tests/maplibre/**`;
- `packages/maplibre/**`;
- `apps/explorer-web/**`.

Thus changes to the confirmed Python tests, the MapLibre package scaffold, or the named explorer application may not trigger this workflow.

### 6. The workflow does not execute the Python tests in this lane

No `pytest tests/maplibre` step appears in the checked MapLibre workflow.

The direct Python tests and the browser/performance workflow are separate proof surfaces today.

### 7. Browser error handling needs explicit correctness assertions

The smoke harness resolves its load timer on either a MapLibre `load` event or an `error` event. A source/runtime error therefore does not itself fail that step.

Visual diff or later checks may detect a bad result, but tests must explicitly distinguish:

```text
renderer loaded intended fixture
renderer emitted an error
renderer timed out
renderer rendered an empty/default/error surface
```

### 8. Temporary artifact path carries trust-shaped objects

Current scripts write receipt-, proof-, manifest-, correction-, rollback-, and failure-bundle-shaped objects under:

```text
artifacts/perf/
```

Directory Rules classify `artifacts/` as a compatibility root for temporary build/docs/QA outputs, not canonical trust-bearing storage.

Until migration:

- call them candidate or shaped outputs;
- do not register them as authoritative receipts/proofs/releases;
- do not let downstream clients consume them as canonical;
- retain CI artifacts only as bounded review evidence;
- require promotion into accepted roots through a governed transition.

### 9. Failure-artifact validation is non-blocking

Failure-path builders and validation commands use `|| true`.

That may be appropriate to maximize diagnostic collection after a failure, but a completed failure-handling step does not prove the failure bundle, correction, or rollback output is valid.

### 10. Proposed architecture decisions are not current test authority

ADR-0006 and ADR-0007 remain proposed.

The current explorer-web boundary test permits MapLibre or Cesium imports inside `apps/explorer-web/src/adapters/`. That is not equivalent to the proposed ADR-0006 rule that only a dedicated MapLibre package imports the renderer, and it does not prove ADR-0007 sole-renderer acceptance.

Tests must label these distinctions rather than silently merging them.

---

## Renderer and trust-membrane invariants

### Renderer is downstream

The renderer may consume:

- governed descriptors;
- released and public-safe artifact refs;
- catalog records and released snapshots;
- finite policy/runtime outcomes;
- correction and rollback posture;
- safe evidence references for downstream inspection.

It must not own or create:

- source truth;
- claim truth;
- evidence closure;
- rights or sensitivity decisions;
- release decisions;
- geoprivacy authority;
- canonical lifecycle state;
- correction or rollback authority.

### Forbidden public-path behavior

Tests should fail when browser or renderer code attempts to:

- read RAW, WORK, QUARANTINE, unpublished-candidate, canonical, or internal stores directly;
- call source credentials or private endpoints;
- import or call a model runtime directly;
- load unreviewed arbitrary URLs;
- render exact sensitive geometry without upstream policy and transformation;
- display withdrawn, superseded, correction-pending, or rollback-mismatched layers as current;
- use style filtering or opacity as a substitute for upstream redaction;
- treat feature properties, popups, screenshots, visual diffs, graph edges, or AI summaries as evidence authority.

### Adapter and import boundary

Current enforceability work should distinguish:

| Boundary | Current status |
|---|---|
| Imports remain in `apps/explorer-web/src/adapters/` | Partially enforced by a confirmed policy test |
| Only `packages/maplibre/` imports MapLibre | Proposed ADR requirement; not equivalent to current test |
| No alternate renderer on default path | Proposed ADR requirement |
| Plugin/protocol set is admitted and pinned | NEEDS VERIFICATION |
| Package API hides raw renderer types | NEEDS VERIFICATION |
| Consumers import `@kfm/maplibre` | No consumer surfaced in bounded package evidence |

---

## Required test families

### 1. Placement and dependency boundary

- direct renderer imports outside the accepted adapter seam;
- MapLibre package dependency/version absence or mismatch;
- unapproved renderer/plugin/protocol dependency;
- missing or drifted lockfile;
- wrong application path filter;
- package changes that fail to trigger governance.

### 2. PerfEnvelope and configuration

- missing object identity and schema version;
- missing thresholds;
- zero, negative, non-numeric, or implausible thresholds;
- unknown fields after the schema becomes closed;
- stale envelope;
- envelope hash mismatch;
- helper fields that drift from config fields.

### 3. Browser smoke correctness

- expected fixture source loads;
- source error is not treated as successful load;
- timeout is a finite failure;
- rendered layer count/source state is asserted;
- browser, MapLibre, and dependency versions are recorded;
- no unintended remote requests occur in hermetic mode.

### 4. Performance metrics

- average and p95 frame times recompute from frame CSV data;
- scenario count and identifiers match the envelope;
- load and idle metrics remain within thresholds;
- missing or truncated frame data fails;
- non-finite values fail;
- threshold violation blocks candidate posture.

### 5. Visual regression

- baseline exists;
- screenshot dimensions match;
- pixel delta is recomputed;
- baseline and actual identities are pinned;
- bad-baseline canary fails;
- transparent/blank/error-page screenshots fail;
- review-required versus automatic pass is explicit;
- updating a baseline requires review and provenance.

### 6. Schema and validator behavior

- every validator has valid and invalid fixtures;
- schemas require identity, version, status, references, and relevant fields;
- additional properties are intentionally controlled;
- validator errors are stable enough for review;
- a placeholder validator cannot satisfy a gate;
- command arguments match validator contracts.

### 7. Receipt, proof, and attestation

- run receipt records inputs, versions, timestamps, hashes, outcomes, and scenario results;
- attestation subject and payload digests resolve;
- proof pack references the same artifacts and manifest;
- signatures or unsigned posture are explicit;
- shaped files under `artifacts/` are not mistaken for canonical records;
- missing proof support blocks promotion.

### 8. Release, correction, withdrawal, and rollback

- candidate manifest is not publication;
- missing rollback target blocks promotion;
- failed run produces a reviewable blocker;
- correction references the affected run/artifacts;
- withdrawal and supersession reach browser-visible state;
- rollback restores a known prior renderer/package/artifact state.

### 9. Policy, rights, and sensitivity

- exact rare-species, archaeology, infrastructure, living-person, DNA/genomic, and private-parcel detail fails closed;
- style/filter changes cannot reveal withheld attributes or geometry;
- screenshot and diff artifacts do not leak protected detail;
- public-safe derivatives carry reviewed transform/receipt posture;
- missing policy or review yields finite non-answer/blocker state.

### 10. Public surfaces and side channels

- map popups and feature-state fields expose only governed fields;
- tiles, sprites, glyphs, style JSON, screenshots, exports, caches, search, and URLs do not bypass release state;
- stale/withdrawn/corrected layers are not cached as current;
- error pages and console logs do not leak private endpoints or filesystem paths;
- generated summaries and Evidence Drawer views resolve governed evidence rather than raw map attributes.

### 11. Negative outcomes

Every material family should include:

```text
positive
invalid
DENY
ABSTAIN
ERROR
review-required
stale
withdrawn
correction-pending
rollback
```

A passing success-only renderer suite is insufficient.

---

## Finite system outcomes and test results

Do not collapse runtime/policy outcomes into test-run states.

### System outcomes

| Outcome | Meaning |
|---|---|
| `ANSWER` | Governed surface may provide supported output. |
| `ABSTAIN` | Evidence, freshness, scope, or support is insufficient. |
| `DENY` | Policy, rights, sensitivity, access, or release posture forbids output. |
| `ERROR` | Validation, dependency, adapter, configuration, or infrastructure failure prevents safe completion. |

### Test results

| Result | Meaning |
|---|---|
| pass | Observed behavior matches the expected system outcome and leakage posture. |
| fail | Observed behavior violates the test contract. |
| skip | Explicitly unavailable condition; not proof of success. |
| expected failure | Known defect with a tracked reason and expiry. |
| infrastructure error | Suite could not evaluate behavior; must not be reported as product pass. |
| zero tests collected | Configuration failure for a required suite. |

A test expecting `DENY` passes only when the system safely denies and does not leak. A `DENY` outcome is not a failed test.

---

## Visual regression and baseline rules

A baseline is an expected test artifact, not truth.

### Baseline identity

Every promoted baseline should identify:

- scenario id;
- fixture id and digest;
- viewport and device scale;
- browser/version;
- MapLibre/version;
- renderer/package build or commit;
- style/source/layer descriptor refs;
- font/glyph/sprite inputs;
- expected release/policy posture;
- creation and review metadata.

### Baseline update control

A baseline change should not be accepted merely because a developer regenerated files.

Require:

1. stated reason;
2. before/after diff;
3. affected scenario list;
4. deterministic reproduction;
5. sensitive-data review;
6. renderer and dependency versions;
7. review by an appropriate steward;
8. rollback target.

### Blank and error-surface detection

Pixel thresholds alone can accept the wrong thing.

Tests should separately detect:

- blank map;
- browser error page;
- missing glyphs or sprites;
- missing source layer;
- unexpected console errors;
- transparent or all-background render;
- wrong camera or viewport;
- stale or withdrawn layer rendered as current.

### Bad-baseline canary

At least one intentionally wrong baseline should fail in CI. If the canary passes, the visual-diff gate is not trustworthy.

---

## Network hermeticity and dependency control

### Current conflict

Repository documentation calls for no-network default tests, but the smoke harness uses public CDNs.

### Required profiles

Use two explicitly distinct profiles:

| Profile | Purpose | Network posture |
|---|---|---|
| `hermetic` | Required pull-request and local regression proof | No external network; vendored or locally served pinned assets |
| `external-smoke` | Optional ecosystem/integration observation | Explicit network allowlist, retries, provenance, and non-authoritative result |

Do not let an external-smoke pass substitute for hermetic proof.

### Hermetic requirements

- lockfile present and reviewed;
- exact MapLibre dependency pinned through package metadata;
- local JS/CSS assets;
- local glyph and sprite fixtures;
- local tile/style fixtures;
- network interception that fails on unexpected requests;
- deterministic browser/version;
- recorded platform and rendering environment;
- no live credentials or private endpoints.

### Supply-chain checks

Before renderer dependencies or plugins are accepted:

- license reviewed;
- version pinned;
- integrity/lockfile recorded;
- vulnerability and provenance posture reviewed;
- plugin/protocol admission recorded where required;
- rollback version known;
- browser/runtime compatibility tested.

---

## Artifact, receipt, proof, and release boundary

The current performance scripts produce several object shapes under `artifacts/perf/`.

Keep the following distinctions:

```text
raw metric file
  != RunReceipt

screenshot
  != RenderDiffReport

RenderDiffReport
  != EvidenceBundle

attestation-shaped envelope
  != verified signature

proof-pack-shaped JSON
  != accepted proof

release-manifest-shaped JSON
  != release decision

correction/rollback draft
  != executed correction or rollback
```

### Interim posture for `artifacts/perf/`

Until accepted migration:

- use it for ephemeral CI/build/QA material only;
- retain bounded workflow artifact retention;
- label trust-shaped objects as candidates;
- prohibit public-client consumption;
- do not register them as canonical receipts, proofs, or release records;
- include run identity and digests so later promotion is possible;
- delete or supersede through transparent cleanup and correction procedures.

### Governed promotion

A candidate output may move into a governed receipt/proof/release lane only after:

- identity and schema validation;
- digest verification;
- policy and sensitivity checks;
- reviewer approval;
- accepted destination;
- correction and rollback linkage;
- provenance and source-code/run linkage;
- no unresolved failure or stale state.

Promotion is a governed state transition, not a file copy.

---

## Fixture contract

### Accepted fixture classes

| Lane | Role |
|---|---|
| `tests/fixtures/maplibre/tiny/` | Minimal smoke inputs |
| `tests/fixtures/maplibre/baselines/` | Expected render baselines |
| `tests/fixtures/maplibre/invalid/` | Malformed and fail-closed cases |
| `tests/fixtures/maplibre/bad-baselines/` | Intentionally failing canaries |

### Fixture requirements

Fixtures must be:

- synthetic or explicitly public-safe;
- deterministic;
- compact and reviewable;
- offline for the hermetic profile;
- free of credentials and private endpoints;
- free of exact sensitive geometry;
- explicit about expected outcome;
- linked to the consuming test;
- versioned when shape changes;
- paired with invalid cases where material.

### Fixture anti-authority rule

A fixture can show expected shape and behavior. It does not establish:

- source authority;
- evidence closure;
- current release state;
- real-world correctness;
- production safety;
- policy approval;
- public publication.

---

## CI and gate acceptance

### Current MapLibre workflow status

The workflow is **implemented but not closed**.

It must not be treated as an accepted promotion gate until the following are resolved:

- package-manager lockfile and `npm ci`;
- external network dependency;
- missing `tests/maplibre/**` trigger;
- missing `packages/maplibre/**` trigger;
- `apps/web/**` versus `apps/explorer-web/**` drift;
- no pytest step for direct MapLibre tests;
- permissive schemas;
- placeholder governance validator;
- no-argument validator mismatch;
- non-blocking failure-artifact validation;
- trust-shaped outputs under `artifacts/perf/`;
- accepted correction and rollback destinations.

### Required CI behavior

A trusted MapLibre test workflow should:

1. trigger on every implementation, test, fixture, config, schema, validator, script, and workflow path that can change behavior;
2. install from an accepted lockfile;
3. run direct Python tests;
4. run hermetic browser smoke;
5. run visual-diff canary;
6. validate schemas with positive and negative fixtures;
7. fail when zero tests or zero scenarios run;
8. fail on unexpected network requests;
9. record browser, renderer, package, and operating-system versions;
10. upload bounded QA artifacts;
11. emit finite status and stable reason codes;
12. keep diagnostic collection from masking the primary failure;
13. produce no release approval;
14. expose an explicit rollback target.

### CI evidence hierarchy

```text
workflow file present
  < workflow started
  < workflow completed
  < expected tests actually collected
  < negative canaries failed correctly
  < artifacts and digests verified
  < repeated stable runs
  < accepted promotion-gate integration
```

Never report a higher maturity level from a lower one.

---

## Test authoring contract

Every executable MapLibre test should identify:

| Field | Requirement |
|---|---|
| Test id | Stable and descriptive |
| Surface | Package, adapter, browser, source, style, layer, tile, visual, perf, receipt, proof, release, public surface |
| Inputs | Fixture/config/artifact refs and digests where material |
| Authority refs | Contract, schema, policy, ADR, release rule |
| Expected system outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or non-runtime validation result |
| Expected test result | pass/fail/skip/expected failure |
| Leakage checks | Fields, URLs, paths, geometry, logs, caches, screenshots |
| Network profile | `hermetic` or explicitly bounded `external-smoke` |
| Determinism controls | Browser, viewport, versions, fonts, timing, seed |
| Correction behavior | What changes when an old baseline/result is invalid |
| Rollback target | Prior known-good package/config/baseline/artifact state |
| Review burden | Required owners/stewards |

### Minimal test card

```markdown
# <maplibre-test-id>

## Status
DRAFT / ACTIVE / HELD / SUPERSEDED / RETIRED

## Test family
import-boundary / schema / browser-smoke / performance / visual-diff / artifact-integrity / policy / release / rollback / leakage

## Network profile
hermetic / external-smoke

## Inputs
- Fixture:
- Config:
- Schema:
- Contract:
- Policy:
- Release/correction/rollback refs:

## Expected system outcome
ANSWER / ABSTAIN / DENY / ERROR / N/A

## Assertions
- Behavior:
- Negative state:
- Leakage:
- Artifact/proof boundary:

## Determinism
- Browser/version:
- MapLibre/version:
- Viewport:
- Fonts/glyphs/sprites:
- Seed/time controls:

## Reviewer
<required steward roles>
```

---

## Validation

### Documentation and inventory checks

```bash
find tests/maplibre -maxdepth 4 -type f | sort
find tests/fixtures/maplibre -maxdepth 5 -type f | sort
find tools/validators/maplibre scripts configs/maplibre schemas/maplibre -maxdepth 5 -type f | sort
```

### Direct Python tests

```bash
python -m pytest -q tests/maplibre
```

### Static script checks

```bash
python -m py_compile tests/maplibre/*.py tools/validators/maplibre/*.py
node --check scripts/maplibre-smoke-perf.mjs
node --check scripts/build-maplibre-render-diff.mjs
node --check scripts/attest-maplibre-perf.mjs
node --check scripts/build-maplibre-perf-release-manifest.mjs
node --check scripts/build-maplibre-perf-proof-pack.mjs
node --check scripts/build-maplibre-perf-correction-and-rollback.mjs
node --check scripts/build-maplibre-perf-failure-bundle.mjs
```

### Current operational commands

```bash
npm run maplibre:perf
npm run maplibre:render-diff
npm run maplibre:attest
npm run maplibre:manifest
npm run maplibre:proof
```

Treat these as operational entry points, not proof of success.

Do not use the current no-argument `maplibre:govern` invocation as an accepted gate until the validator contract is implemented and the caller is corrected.

### Current-session execution status

Repository tests, Node scripts, validators, browser runs, and workflows were **not run** during this Markdown-only API update.

---

## Definition of done

This lane is implementation-complete only when all applicable conditions are met.

### Placement

- [ ] `tests/maplibre/` or a successor path is accepted.
- [ ] No duplicate suite exists under `tests/packages/maplibre/`.
- [ ] Parent indexes and CODEOWNERS are current.
- [ ] Workflow path filters include the accepted implementation and test paths.

### Package and browser

- [ ] MapLibre package API exists and is consumed.
- [ ] Renderer dependency and version are pinned.
- [ ] Lockfile and package-manager strategy are accepted.
- [ ] Hermetic JS/CSS/glyph/sprite/tile assets exist.
- [ ] Browser/version matrix is recorded.

### Tests

- [ ] Current helper tests are paired with actual config/schema fields or clearly scoped as separate unit tests.
- [ ] Browser smoke distinguishes load, error, timeout, blank render, and expected render.
- [ ] Performance metrics are recomputed from raw frame data.
- [ ] Visual baseline and bad-canary coverage are executable.
- [ ] Import, source, policy, sensitivity, release, correction, rollback, and leakage tests exist.
- [ ] Zero-test and zero-scenario runs fail.

### Schemas and validators

- [ ] MapLibre schemas define required fields and close unintended properties.
- [ ] Positive and negative fixtures exist.
- [ ] `validate_perf_governance.py` implements the documented checks.
- [ ] Workflow arguments match validator contracts.
- [ ] Failure-path validation is inspectable and not misreported as success.

### Governance

- [ ] Temporary and trust-bearing outputs are separated.
- [ ] Receipt/proof/release destination decisions are accepted.
- [ ] Evidence, policy, review, release, correction, withdrawal, and rollback references are validated.
- [ ] Sensitive surfaces fail closed.
- [ ] Test pass is never treated as release approval.

### CI

- [ ] Workflow runs on all relevant changes.
- [ ] Hermetic profile is required.
- [ ] Optional external-smoke profile is clearly non-authoritative.
- [ ] Current logs show expected tests and scenarios executed.
- [ ] Repeated stable runs exist.
- [ ] Promotion integration is accepted and reversible.

---

## Placement and implementation migration

Do not bulk-move tests or trust-shaped outputs.

### Phase 1 — Inventory

Inventory:

- direct test files;
- package-local tests;
- UI, E2E, policy, and API tests that exercise MapLibre;
- fixtures and baselines;
- workflows and callers;
- scripts and validators;
- schemas/configs;
- output and artifact consumers.

### Phase 2 — Decide test home

Resolve:

```text
tests/maplibre/
tests/packages/maplibre/
another accepted topic path
```

Record the decision before creating a duplicate.

### Phase 3 — Repair proof chain in place

Before moving paths:

- implement governance validation;
- harden schemas;
- add direct pytest execution;
- correct path filters;
- establish lockfile;
- add hermetic assets;
- separate candidate artifacts from canonical records.

### Phase 4 — Normalize fixtures

Choose accepted fixture homes and eliminate undocumented mirrors while preserving history and consumers.

### Phase 5 — Migrate trust-shaped outputs

Move only through governed destination, identity, schema, review, correction, and rollback decisions.

### Phase 6 — Update consumers atomically

Update:

- imports;
- scripts;
- package commands;
- Make targets;
- workflow filters;
- validators;
- docs;
- artifact upload paths;
- release/correction/rollback refs.

### Phase 7 — Prove migration

Run:

- old/new path detection;
- full direct tests;
- hermetic browser tests;
- visual canary;
- negative schemas/validators;
- CI trigger checks;
- rollback drill.

### Phase 8 — Deprecate old path

Only after consumers and rollback are proven:

- mark old path deprecated;
- retain a bounded pointer if needed;
- remove duplicate executables in a transparent commit;
- preserve migration and correction history.

### Stop conditions

Stop migration when:

- ownership is unclear;
- test collection changes unexpectedly;
- a workflow no longer triggers;
- fixtures or baselines are lost;
- a consumer depends on old paths;
- sensitive-output review is incomplete;
- trust-shaped artifacts would be silently reclassified;
- rollback cannot restore the prior behavior.

---

## Correction and rollback

### Documentation correction

If this README overstates implementation:

1. narrow the claim;
2. identify the evidence that invalidated it;
3. update truth labels;
4. link the correction to affected tests/workflows/docs;
5. preserve prior history.

### Baseline correction

When a baseline is invalid:

1. hold affected visual claims;
2. identify scenarios and releases affected;
3. regenerate only from accepted fixtures and pinned environment;
4. review before replacement;
5. invalidate stale diffs and caches;
6. retain old baseline identity for audit;
7. keep a rollback target.

### Workflow correction

When workflow behavior is unsafe or misleading:

1. do not mark its green status as proof;
2. isolate the failing or non-hermetic stage;
3. preserve logs and diagnostics;
4. correct trigger, dependency, schema, validator, or artifact wiring;
5. add regression tests;
6. rerun the required proof profile;
7. record remaining limitations.

### Safety rollback

Rollback is required if a change:

- exposes sensitive detail;
- weakens no-network or dependency controls;
- makes missing tests appear green;
- bypasses the adapter or governed API;
- promotes temporary artifacts as receipts/proofs/releases;
- removes correction or rollback linkage;
- causes stale/withdrawn layers to appear current;
- weakens visual-diff canaries;
- hides renderer errors.

Before merge, rollback is leaving the review unmerged or restoring the prior blob in a transparent commit.

After merge, rollback is a normal revert commit or revert PR. Do not reset or rewrite shared history.

---

## Open verification backlog

### Placement and ownership

- [ ] Decide `tests/maplibre/` versus `tests/packages/maplibre/`.
- [ ] Confirm CODEOWNERS and required review roles.
- [ ] Inventory all MapLibre-related tests outside this lane.
- [ ] Decide whether performance scripts graduate from `scripts/` to `tools/` or a pipeline lane.

### Package and dependency

- [ ] Confirm package manager and create/restore accepted lockfile.
- [ ] Confirm MapLibre version and dependency ownership.
- [ ] Confirm package exports, build, browser, and consumer graph.
- [ ] Resolve proposed ADR-0006 and ADR-0007 status before enforcing them as accepted rules.
- [ ] Define plugin/protocol admission and supply-chain checks.

### Tests and fixtures

- [ ] Verify direct pytest collection and pass state.
- [ ] Align Python fixture fields with config/schema or document the separate purpose.
- [ ] Inventory PNG baselines and bad-baseline canaries.
- [ ] Add source-error, timeout, blank-render, and missing-glyph tests.
- [ ] Add sensitive-output and side-channel fixtures.
- [ ] Add correction, withdrawal, and rollback scenarios.

### Schema and validator backlog

- [ ] Replace open-object MapLibre schemas with reviewed shapes.
- [ ] Add required fields, enums, identities, refs, and digest rules.
- [ ] Implement governance validator behavior.
- [ ] Add positive and negative validator fixtures.
- [ ] Correct validator command arguments.
- [ ] Verify proof/manifest/attestation subject linkage.

### Workflow and CI

- [ ] Add `tests/maplibre/**` to workflow paths.
- [ ] Add `packages/maplibre/**` to workflow paths.
- [ ] Resolve `apps/web/**` versus `apps/explorer-web/**`.
- [ ] Run direct Python tests in the MapLibre workflow.
- [ ] Create a required hermetic profile.
- [ ] Separate external-smoke results.
- [ ] Fail on zero tests and zero scenarios.
- [ ] Verify current pass/fail state from logs.
- [ ] Prove failure artifacts do not mask the primary failure.

### Artifacts and release

- [ ] Decide accepted homes for metrics, receipts, proofs, manifests, corrections, and rollback.
- [ ] Record identity, retention, correction, and deletion rules.
- [ ] Prevent public/client consumption of `artifacts/perf/`.
- [ ] Verify release and rollback integration.
- [ ] Define cache invalidation for corrected or withdrawn map outputs.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior target README | CONFIRMED | Prior scope, placement uncertainty, and intended renderer boundary | Outdated executable/workflow claims |
| `tests/README.md` | CONFIRMED | `tests/` is canonical enforceability proof | Does not settle MapLibre sublane placement |
| `perf_fixture_builder.py` | CONFIRMED executable helper | Current three-field scalar fixture behavior | Not renderer/config/schema integration |
| `test_perf_governance_negative_paths.py` | CONFIRMED pytest module | Three current negative tests | No browser or workflow coverage |
| `tests/fixtures/maplibre/README.md` | CONFIRMED | Fixture parent and four documented child lanes | Payload inventory and consumption incomplete |
| `packages/maplibre/README.md` | CONFIRMED current package evidence | Package scaffold, placement conflicts, runtime and CI gaps | Package remains non-functional scaffold |
| Root `package.json` | CONFIRMED | MapLibre operational commands and dev dependencies | Generic lint/test/build remain placeholders |
| Root `Makefile` | CONFIRMED | MapLibre targets and current no-argument governance call | Command success not proven |
| `maplibre-smoke-perf.mjs` | CONFIRMED executable script | Browser scenarios, metrics, screenshots, candidate receipt output, external URLs | Correctness and current run state unproven |
| `build-maplibre-render-diff.mjs` | CONFIRMED executable script | Pixel diff, missing/dimension failure, threshold exit | Baseline provenance and current pass state unproven |
| `maplibre-perf-governance.yml` | CONFIRMED substantive workflow | Current chain, triggers, commands, uploads, retention | Contains wiring and proof conflicts |
| MapLibre schemas | CONFIRMED permissive | JSON object acceptance | Do not enforce documented object contracts |
| Validator wrappers | CONFIRMED | Schema-runner entry points exist | Validation strength bounded by schemas |
| `validate_perf_governance.py` | CONFIRMED placeholder | Current finite file-existence behavior | Not documented governance implementation |
| ADR-0006 | CONFIRMED document / PROPOSED | Intended single-importer seam | Not accepted implementation authority |
| ADR-0007 | CONFIRMED document / PROPOSED | Intended sole-renderer/plugin posture | Not accepted implementation authority |
| Explorer-web adapter-boundary test | CONFIRMED | Some direct import and internal-store path checks exist | Not equivalent to package-only adapter rule |
| Directory Rules | CONFIRMED doctrine | Responsibility roots and artifact authority | Does not prove implementation maturity |
| Current-session execution | NOT RUN | Documentation-only API change | No test, validator, browser, or CI pass claim |

[Back to top](#top)
