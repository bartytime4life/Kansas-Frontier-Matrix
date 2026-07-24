<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-slim-readme
title: fixtures/slim/README.md — Slim Runtime Fixture Boundary
type: README
version: v0.2
status: draft; repository-grounded; reusable-fixture-lane; activation-held; payload-inventory-unverified; no-network-default; synthetic; non-authoritative
owners:
  - "@bartytime4life — CONFIRMED GitHub CODEOWNERS review route for /fixtures/"
  - "OWNER_TBD — semantic slim-fixture stewardship and runtime activation approval"
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, script, workflow, package command, schema, policy, runtime, artifact, release object, or publication state is superseded
policy_label: repository-facing; fixtures; slim; runtime-smoke; synthetic; public-safe; deterministic; no-network-default; activation-held; correction-aware; rollback-aware; non-publisher
owning_root: fixtures/
responsibility: define the admission and activation boundary for small reusable runtime fixtures that are too cross-cutting for test-local or domain-owned fixture lanes
truth_posture: cite-or-abstain; README presence, a fixture name, script syntax, workflow success, or a future smoke result proves only the specifically executed check and never truth, evidence closure, policy approval, production capacity, release readiness, or publication
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d4c7683c1b7b85cb731a0bfd397ca90d719eed16
  prior_blob: f175ac21e849f405c47efd7f40f1f29968992930
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  heavy_readme_blob: 2d53424b89fb0ac3c49c2251007836210aad4ecc
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  smoke_script_blob: 699dd4cf42d355dd2ed7620852b7fd1f3000bbe2
  workflow_blob: bfb36a84ba72bec68d964976dc7964cde7f5d603
  package_json_blob: 62f45306aef7376a2d68042b0c9e7f556edf0e78
  makefile_blob: 51537af34ee065c2de571134688415042b83b22a
  maplibre_perf_governance_doc_blob: 67f57a9a0878801f83a13f3b1c6d80be3174036e
  expected_style_path: fixtures/slim/style.json
  expected_style_path_state: CONFIRMED ABSENT at the pinned base
related:
  - ../README.md
  - ../heavy/README.md
  - ../golden/README.md
  - ../domains/README.md
  - ../../tests/fixtures/README.md
  - ../../scripts/maplibre-smoke-perf.mjs
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../configs/maplibre/perf-envelope.v1.json
  - ../../docs/quality/maplibre-perf-governance.md
  - ../../package.json
  - ../../Makefile
  - ../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, fixture payload, generator, schema, validator, policy, runtime output, proof, receipt, release object, or publication state."
  - "The MapLibre smoke script is command-bearing and references fixtures/slim/style.json, but that referenced style fixture is absent at the pinned base."
  - "The MapLibre performance-governance workflow path-scopes fixtures/slim/**, syntax-checks the smoke script, and deliberately holds browser/performance execution while runtime fixtures, lockfile-backed dependencies, local assets, meaningful schemas, and governed output placement remain unresolved."
  - "The workflow currently asserts that fixtures/slim/style.json and fixtures/heavy/style.json do not exist; adding either requires a coordinated implementation and workflow update rather than an isolated payload commit."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/slim/` — Slim Runtime Fixture Boundary

[![Status: activation held](https://img.shields.io/badge/status-activation%20held-f59e0b?style=flat-square)](#status)
[![Lane: slim runtime fixture](https://img.shields.io/badge/lane-slim%20runtime%20fixture-1f6feb?style=flat-square)](#purpose)
[![Network: denied by default](https://img.shields.io/badge/network-denied%20by%20default-15803d?style=flat-square)](#validation-and-activation)
[![Authority: fixture only](https://img.shields.io/badge/authority-fixture%20only-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `fixtures/slim/` is the preferred boundary for small, reusable, synthetic runtime-smoke inputs when the case is cross-cutting, reviewable, no-network by default, and not better owned by a domain lane or `tests/fixtures/`.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Current MapLibre boundary](#current-maplibre-boundary) · [Routing](#fixture-home-routing) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Admission](#fixture-admission-contract) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation-and-activation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Verification](#verification-status) · [Rollback](#rollback) · [Last reviewed](#last-reviewed)

> [!IMPORTANT]
> This lane is **not currently an operational MapLibre runtime corpus**. The command-bearing smoke script references `fixtures/slim/style.json`, but that path is absent. The current performance-governance workflow intentionally records a hold rather than running the browser, server, renderer, screenshot, receipt, proof, release, correction, or rollback stages.

> [!CAUTION]
> “Slim” describes reviewable fixture scale, not weak governance. A small fixture still needs a named consumer, deterministic identity, safe content, expected outcome, and explicit proof limits. A filename such as `public-safe`, `release-ready`, or `approved` never establishes those properties.

> [!WARNING]
> Do not add `style.json` or another runtime payload in isolation. The present workflow deliberately fails when the slim or heavy runtime style fixture surfaces so maintainers must review local tile serving, glyphs, sprites, dependency locking, browser installation, network denial, expected metrics, artifacts, correction, and rollback together.

---

## Purpose

`fixtures/slim/` provides the **smallest reusable runtime-fixture tier** under the canonical [`fixtures/`](../README.md) root.

It exists to answer:

> What compact, deterministic, synthetic or demonstrably public-safe input can exercise a named runtime, renderer, adapter, API-envelope, or documentation-smoke boundary without using lifecycle data or requiring a heavy stress corpus?

The lane should help maintainers:

- start with a small fixture before considering [`fixtures/heavy/`](../heavy/README.md);
- keep cross-cutting runtime examples separate from test-local examples;
- preserve domain ownership when domain meaning or sensitivity is material;
- make fixture identity, generation, consumer, expected outcome, and limits inspectable;
- run locally without live sources, remote tiles, remote fonts, remote scripts, models, or vendor services by default;
- separate immutable inputs from environment-bound measurements and generated QA output;
- avoid turning demonstration data into source, evidence, policy, release, or publication authority.

This directory is not a miscellaneous sample folder and is not the default home for every small file.

[Back to top](#top)

---

## Authority level

| Field | Authority |
|---|---|
| **Directory class** | Nested reusable-fixture lane under canonical `fixtures/` |
| **Primary responsibility** | Small cross-cutting runtime and renderer-smoke inputs |
| **May own** | Compact synthetic/public-safe inputs, deterministic generation notes, lane manifests, expected-output pointers, and consumer-binding documentation |
| **Must not own** | Contracts, schemas, policy, lifecycle data, source records, EvidenceBundles, canonical receipts/proofs, review approvals, release objects, application code, generated QA results, or published artifacts |
| **Network posture** | Denied by default; live external dependencies require a separately governed integration or watcher workflow |
| **Public-path posture** | DENY direct public use; public clients consume governed APIs and released artifacts, not fixture paths |
| **Truth posture** | A result supports only its declared consumer, input identity, environment, and expected condition |
| **Review route** | `/fixtures/` routes to `@bartytime4life` through CODEOWNERS; required review and semantic stewardship remain unverified |

### Responsibility boundary

| Responsibility | Authority home | Role of `fixtures/slim/` |
|---|---|---|
| Semantic meaning | `contracts/` | Supply examples; never redefine object or runtime meaning |
| Machine shape | `schemas/` | Supply inputs when a schema exists; never become schema authority |
| Policy, sensitivity, rights, and access | `policy/` | Supply reviewed test inputs or mocks; never approve exposure |
| Runtime and adapter implementation | `apps/`, `packages/`, `runtime/`, or another repo-confirmed implementation root | Exercise named behavior; never contain implementation code |
| Executable validators and harnesses | `tools/`, `scripts/`, `tests/`, or package-owned test lanes | Provide inputs; never replace assertions or harness logic |
| Test-local fixtures | [`tests/fixtures/`](../../tests/fixtures/README.md) | Do not duplicate one-test-only material here |
| Domain-owned fixtures | `fixtures/domains/<domain>/` or another verified domain fixture lane | Defer when domain semantics, rights, or sensitivity are material |
| Large stress inputs | [`fixtures/heavy/`](../heavy/README.md) | Escalate only when scale is necessary and documented |
| Expected outputs | [`fixtures/golden/`](../golden/README.md) when accepted | Pair stable outputs without treating them as truth authority |
| Lifecycle and source data | `data/` | Use synthetic/public-safe representations only |
| Generated QA measurements | `artifacts/` or another accepted temporary QA home | Keep outputs separate from immutable fixture inputs |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Never store canonical trust-bearing objects here |
| Release and rollback decisions | `release/` | Fixture or benchmark success never approves release |

Directory Rules place this lane under `fixtures/` because its primary responsibility is reusable checking input. This same-path README update creates no new root, migration, lifecycle phase, or parallel authority.

[Back to top](#top)

---

## Status

Snapshot: `main@d4c7683c1b7b85cb731a0bfd397ca90d719eed16`, inspected on 2026-07-24.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `f175ac21e849f405c47efd7f40f1f29968992930` | Existing documentation is modernized in place |
| Root fixture contract | **CONFIRMED** at [`../README.md`](../README.md) | Reusable fixtures are non-authoritative, no-network by default, and distinct from test-local fixtures |
| Heavy sibling boundary | **CONFIRMED** at [`../heavy/README.md`](../heavy/README.md) | Slim is the preferred starting tier; heavy is an exception for scale-dependent cases |
| CODEOWNERS routing | **CONFIRMED** for `/fixtures/` | GitHub review requests route to `@bartytime4life`; required-review enforcement is not established |
| MapLibre smoke script | **CONFIRMED** at [`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) | Script contains a slim scenario and references `fixtures/slim/style.json` through localhost |
| Root command surfaces | **CONFIRMED** in [`package.json`](../../package.json) and [`Makefile`](../../Makefile) | `npm run maplibre:perf` and `make maplibre-perf` invoke the smoke script, but command presence is not runtime proof |
| Expected slim style fixture | **CONFIRMED ABSENT** | `fixtures/slim/style.json` does not exist at the pinned base |
| MapLibre governance workflow | **CONFIRMED** at [`.github/workflows/maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | Changes under `fixtures/slim/**` trigger readiness checks, not the browser performance run |
| Current workflow outcome contract | **CONFIRMED** | Static syntax and narrow negative-path checks may run; browser/perf/render/trust stages remain explicit `WORKFLOW_HOLD` |
| Direct payload inventory | **UNKNOWN / not exhaustive** | No byte-complete recursive directory listing is claimed; the specifically referenced `style.json` is absent |
| Deterministic generator | **NOT ESTABLISHED** | No generator for a slim runtime corpus was verified |
| Dedicated slim fixture schema or manifest | **NOT ESTABLISHED** | Admission fields below are documentation guidance, not a current machine contract |
| Executable no-network runtime test | **NOT ESTABLISHED** | Current script contains live CDN and remote glyph references |
| Active Evidence Drawer, Focus Mode, Cesium, or governed-API consumer | **NOT ESTABLISHED** | Prior broad examples are not treated as implemented lane consumers |
| Production performance or release readiness | **DENIED as inference** | Script, fixture, workflow, or benchmark presence cannot prove production capacity or publication safety |

### Material corrections in this revision

- Replaces broad consumer claims with the one verified direct runtime reference: the MapLibre smoke script.
- Records that `fixtures/slim/style.json` is absent.
- Distinguishes command-bearing Make/npm surfaces from a runnable, governed performance lane.
- Records that current CI intentionally holds browser/performance execution and asserts that runtime style fixtures have not surfaced.
- Removes Cesium, Evidence Drawer, Focus Mode, governed-API, and generic renderer claims from the **current implemented** posture; they remain possible only after a named consumer is verified.
- Makes the slim/heavy split subordinate to domain ownership and test-local ownership.
- Separates fixture inputs from environment-bound measurements, screenshots, candidate receipts, proofs, and release-shaped outputs.
- Adds activation criteria, failure interpretation, no-network requirements, and rollback guidance.

[Back to top](#top)

---

## Current MapLibre boundary

### Confirmed command path

```text
package.json: npm run maplibre:perf
Makefile:      make maplibre-perf
                    │
                    ▼
scripts/maplibre-smoke-perf.mjs
                    │
                    ├── slim scenario
                    │     └── http://localhost:8080/fixtures/slim/style.json
                    └── heavy scenario
                          └── http://localhost:8080/fixtures/heavy/style.json
```

The smoke script also loads MapLibre GL JS and glyphs from external HTTPS endpoints. It writes environment-bound performance results, frame-time CSV files, screenshots, and a run-receipt-shaped JSON object under `artifacts/perf/` when executed.

### Confirmed readiness hold

The current MapLibre performance-governance workflow:

- watches `fixtures/slim/**` and `fixtures/heavy/**`;
- checks JavaScript and Python syntax;
- runs three deterministic negative-path functions;
- verifies that no dependency lockfile or executable MapLibre runtime fixture payload has surfaced;
- verifies that `fixtures/slim/style.json` and `fixtures/heavy/style.json` remain absent;
- verifies that the smoke script still carries its live-CDN, remote-glyph, and localhost-fixture markers;
- does not install browsers or packages;
- does not start a server or run the smoke script;
- does not emit screenshots, receipts, attestations, proofs, release manifests, corrections, rollbacks, failure bundles, or uploaded artifacts;
- records `WORKFLOW_SKIPPED_EXPLICIT` and `WORKFLOW_HOLD` for the runtime and trust-shaped stages.

This is a deliberate fail-safe boundary. The correct next state is not to bypass it; it is to land the fixture, local serving model, dependency lock, no-network design, meaningful schemas, validators, artifact placement, and tests as one reviewed activation slice.

### Current blockers to activation

| Blocker | Current evidence | Required resolution before runtime claims |
|---|---|---|
| Slim style input absent | `fixtures/slim/style.json` is missing | Add a deterministic, reviewed fixture with identity and expected consumer |
| Heavy style input absent | `fixtures/heavy/style.json` is missing | Keep heavy optional; add only for a justified scale case |
| Live MapLibre CDN | Script loads MapLibre from `unpkg.com` | Pin and install dependencies through an accepted lockfile and cache strategy |
| Remote glyph endpoint | Script loads glyphs from `demotiles.maplibre.org` | Provide local/pinned assets or a separately governed network test tier |
| Local fixture server unspecified | Script expects `localhost:8080` | Define deterministic server command, lifecycle, port, shutdown, and failure behavior |
| Browser installation unbound | Playwright is declared but no accepted lockfile/install path is active in CI | Pin package manager, lockfile, browser version, and cache policy |
| Expected metrics unbound | Perf envelope exists, but runtime evidence is not generated in CI | Wire actual frame/idle/load measurements and deterministic verification |
| Output placement conflicted | Script emits trust-shaped candidates under `artifacts/perf/` | Keep QA output temporary and move canonical receipts/proofs/releases to accepted authority roots after review |
| Placeholder governance surfaces | Workflow confirms permissive schemas and placeholder validators | Replace through contract/schema/fixture/validator/test slices |
| Release-grade gate absent | Workflow explicitly holds promotion and publication claims | Preserve HOLD until governance closure is implemented and reviewed |

[Back to top](#top)

---

## Fixture-home routing

Use the narrowest correct owner.

| Scenario | Preferred home | Reason |
|---|---|---|
| Small cross-cutting runtime smoke input shared by multiple consumers | `fixtures/slim/` | This lane |
| One test module's private helper data | `tests/fixtures/` or owning test subtree | Test-local ownership |
| Domain-specific object, geometry, policy, or sensitivity case | Verified domain fixture lane | Domain responsibility and review context |
| Schema-positive or schema-negative object fixture | Object-family valid/invalid lane | Consumer and expected outcome are explicit |
| Large cross-cutting stress corpus | `fixtures/heavy/` | Only after slim is inadequate and scale need is documented |
| Stable deterministic expected output | `fixtures/golden/` | Keeps expected results separate from inputs |
| Temporary screenshots, timing CSV files, diff reports, or logs | `artifacts/` or accepted QA output home | Generated and environment-bound |
| Real source or lifecycle material | `data/<phase>/` | Governed lifecycle, never fixture storage |
| Canonical receipt or proof | `data/receipts/` or `data/proofs/` | Trust-bearing authority |
| Release decision, manifest, correction, or rollback record | `release/` | Release authority |

A fixture does not move to `heavy/` merely because it is inconvenient to review. First reduce, sample, generate deterministically, or narrow the consumer. Use heavy only when the behavior under test depends on scale.

[Back to top](#top)

---

## What belongs here

Material may be admitted only when it is compact, reusable, deterministic or reproducibly generated, synthetic or demonstrably public-safe, and tied to a named consumer.

Examples may include:

- small local MapLibre style/source fixtures after the activation contract is implemented;
- compact GeoJSON, vector-tile, JSON, JSONL, SVG, YAML, sprite, glyph, or style examples that remain practical for normal review;
- toy layer, source, camera, style-switch, attribution, interaction, and adapter-envelope inputs;
- bounded generalized geometries created specifically for runtime smoke checks;
- deterministic generators, seeds, canonicalization rules, hashes, and generation notes;
- lane manifests or README tables naming fixture identity, purpose, consumer, rights, sensitivity, expected outcome, and retirement posture;
- pointers to compact golden outputs when stable comparison is justified;
- documentation-only examples clearly labeled as non-executable.

A payload is not admitted merely because it is small. It must have a real reason to be reusable and cross-cutting.

[Back to top](#top)

---

## What does not belong here

Do not place the following in `fixtures/slim/`:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle material;
- live source exports, production snapshots, vendor responses, remote tiles, or copied public-service payloads;
- real EvidenceBundles, SourceDescriptors, PolicyDecisions, ReviewRecords, RunReceipts, proofs, attestations, release manifests, corrections, withdrawals, or rollback records;
- credentials, tokens, signed URLs, secrets, private tickets, or personally identifying reviewer data;
- living-person records, DNA/genomic data, exact archaeology sites, rare-species localities, critical-infrastructure detail, culturally restricted information, or reverse-engineerable protected geometry;
- implementation code, validators, tests, schemas, contracts, or policy rules;
- generated screenshots, timing logs, CSV measurements, diff images, reports, or CI artifacts;
- a domain-owned or test-local fixture copied here for convenience;
- large binaries or corpora that require an unreviewed storage exception;
- direct public API, map, tile, scene, or AI-serving material.

When uncertain, quarantine the candidate outside this lane until ownership, rights, sensitivity, and consumer are resolved. Do not sanitize by assumption.

[Back to top](#top)

---

## Fixture admission contract

Before adding a substantive payload, record at least the following in the fixture, a sidecar, or a reviewed lane index.

| Field | Required meaning |
|---|---|
| Stable identity | Deterministic name or id for the fixture revision |
| Scenario | Exact behavior or boundary under exercise |
| Consumer | Script, test, validator, package, application, or documentation surface that reads it |
| Expected outcome | Finite result or bounded observation expected from the consumer |
| Generation method | Hand-authored rule or deterministic generator with pinned seed/config |
| Content hash | Digest over the reviewed payload or generation specification |
| Size and scale | Bytes, feature count, layer count, tile count, or another relevant bounded measure |
| Rights posture | Synthetic, generated, or verified public-safe basis |
| Sensitivity posture | Why no protected exact location or restricted subject is exposed |
| Network posture | No-network by default; any exception must be separately governed |
| Runtime prerequisites | Local server, assets, package lock, browser, environment, and commands |
| Output destinations | Temporary QA versus canonical trust-bearing homes |
| Correction path | How a wrong or unsafe fixture is replaced and references repaired |
| Retirement trigger | When the fixture should be removed, migrated, or promoted to heavy/domain/test-local ownership |

### Activation change budget

The first executable slim MapLibre payload should not be added as a one-file shortcut. A sound activation slice is expected to review, at minimum:

1. fixture payload and deterministic identity;
2. local tiles/style/glyphs/sprites or explicit absence of each;
3. dependency lockfile and package-manager decision;
4. browser installation and cache behavior;
5. local server start/health/shutdown behavior;
6. no-network enforcement or a separately governed network tier;
7. expected metrics and deterministic assertions;
8. generated QA output paths;
9. canonical receipt/proof/release placement, if those objects are produced;
10. valid, invalid, error, and timeout paths;
11. workflow transition from HOLD to an explicit finite outcome;
12. synchronized docs, tests, rollback, and correction guidance.

These are **PROPOSED activation requirements** derived from the currently held workflow boundary. They are not claims that the implementation already exists.

[Back to top](#top)

---

## Inputs

### Current verified input surface

| Input | State | Notes |
|---|---:|---|
| `fixtures/slim/README.md` | **CONFIRMED** | Documentation boundary only |
| `fixtures/slim/style.json` | **CONFIRMED ABSENT** | Referenced by the smoke script; not available at the pinned base |
| `configs/maplibre/perf-envelope.v1.json` | **CONFIRMED PRESENT** | Declares threshold-shaped configuration; runtime use is not exercised by current CI |
| MapLibre and glyph CDN assets | **REFERENCED** | Live external dependencies in the smoke script; incompatible with the ordinary no-network fixture posture |
| localhost fixture server | **ASSUMED BY SCRIPT / NOT ESTABLISHED** | Script expects port 8080; no accepted start/stop command was verified |

### Future admitted inputs

Future payloads may be accepted only after the admission contract and activation review are satisfied. README prose alone must not be treated as payload coverage.

[Back to top](#top)

---

## Outputs

`fixtures/slim/` should own immutable or reproducibly generated **inputs**, not environment-bound outputs.

The current smoke script is written to emit:

```text
artifacts/perf/
├── perf-results.json
├── run-receipt.json
├── frame-times/*.csv
├── screenshots/*.png
└── render-diff/render-diff-report.json
```

Current safe interpretation:

- these paths are candidate or QA outputs described by script text;
- the current workflow does not execute the script or produce them;
- timing data and screenshots are environment-bound observations;
- a JSON object named `RunReceipt`, `ProofPack`, or `ReleaseManifest` under `artifacts/` does not become canonical because of its filename or shape;
- canonical trust-bearing outputs require accepted contracts, schemas, validators, authority homes, review, and release discipline;
- generated output must never be copied into `fixtures/slim/` as though it were an immutable input without a reviewed conversion and identity decision.

[Back to top](#top)

---

## Validation and activation

### Safe checks available now

From a repository checkout, maintainers can inspect documentation and script syntax without claiming runtime activation:

```bash
node --check scripts/maplibre-smoke-perf.mjs
git ls-files fixtures/slim
```

The path-scoped workflow also performs static readiness checks when `fixtures/slim/**` changes.

### Commands that exist but are not release-grade proof

```bash
npm run maplibre:perf
make maplibre-perf
```

These commands are present, but the current repository evidence does not establish a reproducible governed execution because:

- the referenced slim and heavy style fixtures are absent;
- the script relies on live external MapLibre and glyph assets;
- the local fixture server contract is unspecified;
- package and browser installation are not locked for CI execution;
- current CI deliberately skips the browser/performance stages;
- trust-shaped output placement and validators remain unresolved.

Do not use command presence, a local ad hoc run, or generated artifacts as proof that the lane is activated, deterministic, no-network, release-ready, or production-representative.

### What future activation must prove

A future executable check should prove only bounded statements such as:

- the pinned fixture can be loaded by the named local runtime;
- declared layers and sources resolve without live network access;
- expected finite success and failure paths occur;
- measured values are reproducible within an accepted environment/tolerance contract;
- generated outputs are complete, hashable, and stored in accepted QA or trust-bearing homes;
- the workflow reports an explicit finite result and fails closed on missing inputs.

It still must not claim source truth, evidence closure, policy approval, public safety, production capacity, release eligibility, or publication by itself.

[Back to top](#top)

---

## Failure interpretation

| Observation | Safe interpretation | Required response |
|---|---|---|
| `style.json` missing | Runtime fixture is not activated | Preserve HOLD; do not invent fallback data |
| Script syntax fails | Command surface is malformed | Fix script or revert change before runtime work |
| External CDN unavailable | Live-network dependency prevented evaluation | Return ERROR/HOLD; do not treat as renderer regression |
| Local server unavailable | Runtime precondition missing | Fail explicitly; do not silently switch to remote data |
| Fixture parse/load failure | Input, serving, or runtime contract mismatch | Identify exact layer/source/asset error and correct fixture or consumer |
| Metrics exceed envelope | Environment-bound performance observation failed | Preserve artifacts as QA evidence; do not infer source or policy failure |
| Screenshot differs | Visual regression signal | Review rendering, baseline identity, environment, and sensitivity before conclusions |
| Workflow remains HOLD | Governance prerequisites are incomplete | Do not bypass with a manual browser run |
| Workflow passes static checks | Readiness assumptions remain unchanged | Does not prove browser execution or performance |
| Fixture unexpectedly contains real/sensitive data | Admission and safety failure | Remove from normal use, quarantine appropriately, assess exposure, repair history/references, and document correction |

Failures must remain finite and inspectable. Avoid fallback behavior that converts missing fixtures or blocked network calls into apparently successful smoke results.

[Back to top](#top)

---

## Rights, sensitivity, and test data

Slim fixtures should normally be fully synthetic.

When a public-safe generalized representation is proposed:

- verify the source and rights basis before inclusion;
- record every transform, generalization, redaction, and aggregation step;
- ensure the output cannot reconstruct protected locations or identities;
- avoid living-person data, DNA/genomics, exact archaeology, rare-species locations, critical infrastructure, and culturally restricted material;
- use the minimum geometry and attributes needed for the declared runtime behavior;
- preserve a correction and withdrawal path;
- deny admission when rights, sovereignty, sensitivity, or derivation is unresolved.

A renderer needs visual structure, not realistic protected content. Synthetic geometry is preferred over copied real-world detail.

[Back to top](#top)

---

## Review burden

A slim fixture change should be reviewed for more than file size.

| Review concern | Minimum question |
|---|---|
| Placement | Is this reusable and cross-cutting, rather than domain-owned or test-local? |
| Consumer | Which exact executable or documentation surface reads it? |
| Determinism | Can the same bytes be regenerated or reviewed reliably? |
| Network | Does normal validation remain no-network? |
| Rights and sensitivity | Is the material synthetic or demonstrably public-safe? |
| Runtime prerequisites | Are local assets, server, browser, package versions, and commands pinned? |
| Expected outcome | Is success/failure finite and testable? |
| Outputs | Are generated QA files separated from fixture inputs and trust-bearing artifacts? |
| Scale | Is slim still sufficient, or is a justified heavy/domain-specific lane needed? |
| Correction and rollback | Can a wrong fixture or activation change be reversed without hidden state? |
| Documentation | Are README, scripts, workflows, tests, and manifests synchronized? |

CODEOWNERS routing does not prove that semantic, policy, sensitivity, security, or release review occurred.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Canonical reusable-fixture root contract |
| [`../heavy/README.md`](../heavy/README.md) | Scale-dependent exception lane; slim is preferred first |
| [`../golden/README.md`](../golden/README.md) | Stable expected-output lane when an accepted comparison exists |
| `../domains/` | Preferred family for domain-owned fixture meaning and sensitivity context |
| [`../../tests/fixtures/README.md`](../../tests/fixtures/README.md) | Test-local fixture responsibility |
| [`../../scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) | Command-bearing script that references the absent slim style fixture |
| [`../../.github/workflows/maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | Path-scoped readiness workflow and explicit runtime HOLD |
| [`../../configs/maplibre/perf-envelope.v1.json`](../../configs/maplibre/perf-envelope.v1.json) | Threshold-shaped configuration consumed by script text |
| [`../../docs/quality/maplibre-perf-governance.md`](../../docs/quality/maplibre-perf-governance.md) | Doctrine-grounded but implementation-bounded design document |
| [`../../package.json`](../../package.json) | npm command surface and unlocked development dependencies |
| [`../../Makefile`](../../Makefile) | Make command surface; `fixtures` regeneration remains TODO-only |
| [`../../artifacts/`](../../artifacts/) | Generated QA/temporary outputs, not fixture or trust authority |
| `../../data/receipts/` | Canonical receipt authority when a governed implementation exists |
| `../../data/proofs/` | Canonical proof authority when a governed implementation exists |
| `../../release/` | Release, correction, withdrawal, and rollback authority |
| [`../../docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Live placement preflight referenced by current repository documentation |

[Back to top](#top)

---

## ADRs

No ADR is required for this same-path documentation modernization. It creates no root, fixture payload, runtime activation, schema, policy, output authority, or migration.

An ADR or explicit migration/activation note may be required when a future change:

- activates browser-based performance CI or introduces a live-network fixture tier;
- establishes a repository-wide slim/heavy size threshold;
- creates a new fixture manifest schema or identity contract;
- chooses a package manager, lockfile, browser pin, or cache strategy with repository-wide effects;
- moves MapLibre scripts from `scripts/` to a canonical tools/package home;
- changes the accepted home for generated QA, receipts, proofs, attestations, or release objects;
- introduces external or large-object fixture storage;
- changes the canonical split among `fixtures/slim/`, `fixtures/heavy/`, domain fixtures, and `tests/fixtures/`;
- exposes fixtures through a public runtime or documentation host;
- retires this lane or redirects downstream consumers.

A new payload does not automatically require an ADR, but it does require the admission and activation evidence described above.

[Back to top](#top)

---

## Verification status

| Check | Result |
|---|---|
| Target path and prior bytes | **CONFIRMED** at `main@d4c7683c1b7b85cb731a0bfd397ca90d719eed16`, blob `f175ac21e849f405c47efd7f40f1f29968992930` |
| Same-path documentation update | **PASS** — no sibling README or path move |
| Root fixture contract | **CONFIRMED** at blob `911c20c86d9322f38b1f59db66b922a94fd027eb` |
| Heavy sibling boundary | **CONFIRMED** at blob `2d53424b89fb0ac3c49c2251007836210aad4ecc` |
| Review route | **CONFIRMED** at CODEOWNERS blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` |
| Smoke script reference | **CONFIRMED** at blob `699dd4cf42d355dd2ed7620852b7fd1f3000bbe2` |
| `fixtures/slim/style.json` | **CONFIRMED ABSENT** at the pinned base |
| Package and Make command surfaces | **CONFIRMED** at blobs `62f45306aef7376a2d68042b0c9e7f556edf0e78` and `51537af34ee065c2de571134688415042b83b22a` |
| Path-scoped governance workflow | **CONFIRMED** at blob `bfb36a84ba72bec68d964976dc7964cde7f5d603` |
| Runtime workflow execution | **CONFIRMED HELD** — browser/perf/render/trust stages are explicitly skipped/held |
| Exhaustive payload inventory | **UNKNOWN / not performed** |
| Deterministic generator and manifest | **NOT ESTABLISHED** |
| No-network runtime execution | **NOT ESTABLISHED** |
| Browser, server, and asset reproducibility | **NOT ESTABLISHED** |
| Evidence Drawer, Focus Mode, Cesium, or governed-API slim consumers | **NOT ESTABLISHED** |
| Python/Node runtime execution for this update | **NOT RUN locally** — no executable repository checkout was mounted |
| Markdown lint, docs build, and link checker | **NOT RUN locally** |
| Required-check and branch-protection enforcement | **NEEDS VERIFICATION** |
| Production performance, release, or publication | **NOT CLAIMED** |

Remote repository reads establish bytes, references, and explicit workflow posture. They do not substitute for a local server, browser run, deterministic fixture generation, performance measurement, policy test, proof validation, release dry-run, or public-runtime verification.

[Back to top](#top)

---

## Rollback

This is a documentation-only, same-path update.

Rollback options:

1. revert the update commit created for this README; or
2. restore prior blob `f175ac21e849f405c47efd7f40f1f29968992930` at `fixtures/slim/README.md`.

Rollback changes documentation only. It does not remove or restore a runtime fixture, server, browser, package lock, script, workflow, schema, validator, metric, screenshot, receipt, proof, release object, correction, rollback execution, or publication state because none of those are changed by this update.

[Back to top](#top)

---

## Last reviewed

**2026-07-24** — repository-grounded documentation review against `main@d4c7683c1b7b85cb731a0bfd397ca90d719eed16`.

Review again when:

- `fixtures/slim/style.json` or another substantive payload is added;
- the MapLibre smoke script changes its fixture, network, server, browser, metric, or output contract;
- a lockfile or accepted package-manager/browser installation path lands;
- the workflow moves from `WORKFLOW_HOLD` to executing browser or performance stages;
- a deterministic generator, manifest, schema, validator, golden output, or dedicated slim-fixture test is introduced;
- Evidence Drawer, Focus Mode, governed API, or another runtime becomes a verified consumer;
- output authority or storage locations change;
- ownership, required review, or branch-protection rules change;
- six months pass without review.

[Back to top](#top)
