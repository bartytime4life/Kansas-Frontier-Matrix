<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-map-master-performance-budgets
title: Map Master — Performance Budgets
type: architecture-reference
version: v1.0-draft
status: draft; repository-grounded; mixed-maturity; fixture-first; operational-performance-hold; non-authoritative
owner: "@bartytime4life via CODEOWNERS; independent UI, map-runtime, reliability, accessibility, privacy, policy, and operations stewardship NEEDS VERIFICATION"
created: 2026-05-24
updated: 2026-08-19
policy_label: public; architecture; map-master; performance; reliability; mobile; no-release; no-publication
owning_root: docs/
responsibility: "Explain KFM map-performance budget boundaries, current fixture-first evidence, finite failure posture, and graduation requirements without becoming contract, schema, policy, runtime, telemetry, review, release, deployment, or publication authority."
truth_posture: "CONFIRMED repository evidence / PROPOSED production profiles / UNKNOWN deployed performance; cite-or-abstain"
current_path: docs/architecture/map-master/PERFORMANCE_BUDGETS.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 34ad2c64c5f15da148e3b63dd27bc14ca46e54da
  target_prior_blob: 560c936fb08cd7fba3d780461b8ea173f9474880
  parent_readme_blob: e26f81e3452b812b70ef25b4b7f791be72e88154
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  mobile_pmtiles_module_blob: c554298345117a19835da92de8a6e187cae63f4d
  mobile_pmtiles_fixture_readme_blob: bcf13b01e2daa83cb42b7509e9f4b4ef10bf87be
  mobile_pmtiles_cases_blob: 068ebdcf04b6cad5496b850fbb1ae21bf123ce2b
  rendering_resource_contract_blob: 63f1b197afa9d28f8998bc532bfe37e459af0789
  rendering_resource_schema_blob: 25210e4a1d79e078a69710b213b3f22b08250b0f
  public_map_slo_contract_blob: b3e1f8cf9d62cf3ebdc266c94d04ba149336a4ea
  public_map_slo_schema_blob: 9bf95e421b871dbe5d21ab076e1569fe6cd24a51
  telemetry_architecture_blob: 4d8038d933a5398313a362589ec1d7bc6a4c9586
  two_d_three_d_parity_blob: 0c56d7a27a1d26d34779b4a40f576e06d79a6c6a
inspection_boundary: "Current-session GitHub reads covered this complete prior page, its parent boundary, accepted placement authority, CODEOWNERS, the mobile PMTiles fixture implementation and profile, the VerifiedRenderingResourceEnvelope contract/schema/validator family, the PublicMapServiceSLOAssessment contract/schema family, Explorer current-state documentation, UI telemetry architecture, and the newly grounded 2D/3D parity page merged immediately before this branch. No mounted checkout, local repository-native test run, live MapLibre boot, real-device benchmark, production service probe, telemetry sink, dashboard, deployment, release, or public endpoint was exercised."
related:
  - README.md
  - ../map-shell.md
  - TILE_ARTIFACTS.md
  - VIEWER_VERIFICATION.md
  - 2D_3D_PARITY.md
  - ../ui/MAP_RUNTIME_BOUNDARY.md
  - ../ui/TELEMETRY.md
  - ../../../apps/explorer-web/README.md
  - ../../../apps/explorer-web/src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md
  - ../../../contracts/runtime/verified_rendering_resource_envelope.md
  - ../../../contracts/validation/public_map_service_slo_assessment.md
  - ../../../schemas/contracts/v1/runtime/verified_rendering_resource_envelope.schema.json
  - ../../../schemas/contracts/v1/validation/public_map_service_slo_assessment.schema.json
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
tags: [kfm, architecture, map-master, performance, budgets, resource-envelope, service-slo, mobile, pmtiles, telemetry, accessibility, fail-closed]
notes:
  - "v1.0-draft replaces proposal-only and unmounted-repository language with a current evidence matrix."
  - "Current executable evidence is fixture-first and mixed: one tiny mobile browser decode/render proof, one synthetic worker-trace/resource-envelope assessment, and one synthetic service-SLO/error-budget assessment."
  - "No production threshold, device classifier, live renderer probe, general UI telemetry event, telemetry route, sink, dashboard, release gate, or automatic rollback effect is established."
  - "Legacy section anchors 1 through 12 are preserved for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Map Master — Performance Budgets

> **Operating rule.** KFM map performance must fail visibly and safely. A fast but unverified, unsupported, misleading, inaccessible, or unreleased map is not a successful map.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-authority)
[![Implementation: fixture first](https://img.shields.io/badge/implementation-fixture%20first-8250df?style=flat-square)](#current-evidence-matrix)
[![Renderer: hold](https://img.shields.io/badge/renderer-HOLD-b42318?style=flat-square)](#current-evidence-matrix)
[![Operational telemetry: hold](https://img.shields.io/badge/operational%20telemetry-HOLD-b42318?style=flat-square)](#8-telemetry)
[![Production budgets: unresolved](https://img.shields.io/badge/production%20budgets-unresolved-6e7781?style=flat-square)](#budget-authority)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#status-and-authority)

> [!IMPORTANT]
> **Current repository evidence does not establish production map-performance budgets.** KFM has bounded synthetic profiles that exercise selected byte, verification, decode/render, worker-resource, availability, latency, and error-budget declarations. Those profiles are useful implementation evidence, but they do not monitor a live service, boot MapLibre, certify a device class, set policy, approve release, trigger rollback, deploy, or publish.

> [!CAUTION]
> **Budget compliance never substitutes for the trust chain.** Performance measurements are process and delivery evidence. They do not resolve an `EvidenceRef`, authenticate an `EvidenceBundle`, establish source truth, reduce sensitivity, clear rights, approve review, or create release authority.

> [!WARNING]
> **Silent success is a trust failure.** A blank tile, dropped layer, stale fallback, hidden decode failure, or simplified geometry must not be presented as “no data” or as equivalent evidence. When KFM cannot render the supported released representation within an admitted profile, the user-facing surface must expose a finite held, degraded, denied, or error state with an accessible non-map explanation.

**Quick navigation:** [Status](#status-and-authority) · [Current evidence](#current-evidence-matrix) · [Scope](#1-scope) · [Categories](#2-budget-categories) · [Profiles](#3-device-class-profiles) · [Probes](#4-runtime-probes) · [Handling](#5-over-budget-handling) · [Mobile](#6-mobile-first-tile-playbook) · [3D](#7-3d-additional-budgets) · [Telemetry](#8-telemetry) · [Anti-patterns](#9-anti-patterns) · [Decisions](#10-open-questions-and-adr-triggers) · [Related](#11-related-docs) · [Appendix](#12-appendix)

---

<a id="status-and-authority"></a>

## Status and authority

| Field | Current evidence-backed result |
|---|---|
| **Path** | `docs/architecture/map-master/PERFORMANCE_BUDGETS.md` — CONFIRMED at `main@34ad2c64c5f15da148e3b63dd27bc14ca46e54da` |
| **Owning root** | `docs/` — human-readable architecture under accepted ADR-0029 and Directory Rules v2 |
| **Document authority** | Explanatory architecture only; not a semantic contract, machine schema, budget policy, runtime profile, telemetry event, receipt, review, release, or publication record |
| **Review route** | `@bartytime4life` through current CODEOWNERS; independent performance, accessibility, reliability, privacy, policy, and operations review remains NEEDS VERIFICATION |
| **Current executable proof** | Three bounded families: mobile PMTiles verification, verified-rendering resource-envelope assessment, and public-map-service SLO assessment |
| **Current live renderer** | HOLD / not established by the inspected evidence |
| **Current production thresholds** | UNKNOWN / no accepted production profile identified |
| **Current operational telemetry** | HOLD / no general UI telemetry event, producer, route, sink, or receipt instance established |
| **Deployment and public service** | UNKNOWN / not inspected |
| **Release or publication effect of this page** | None |

This page explains how performance evidence should fit into the map trust boundary. Contracts define meaning, schemas define shape, policy decides admissibility, runtime code measures or acts, receipts preserve process memory, review records carry accountability, and release objects govern public state. This document owns none of those effects.

### Directory Rules basis

This is a same-path update inside an existing `docs/architecture/` lane. Accepted ADR-0029 adopts Directory Rules v2 and supports `docs/` as the human explanation root. No root, package, schema family, contract family, policy home, telemetry lane, runtime implementation, receipt store, release lane, or published-data path is created or moved.

[Back to top](#top)

---

<a id="current-evidence-matrix"></a>

## Current evidence matrix

The current repository contains more than proposal prose, but less than an operational performance system. The safest description is **mixed, fixture-first maturity**.

| Surface | CONFIRMED repository evidence | What it does **not** prove |
|---|---|---|
| **Mobile PMTiles verification** | An app-local TypeScript verifier accepts a bounded synthetic PMTiles packet, validates archive/index/range/tile bindings, measures verification and injected PNG decode/render time, and has a mobile-emulated browser proof. | No network fetch, real PMTiles service, MapLibre import or boot, real-device benchmark, cryptographic trust, source admission, policy, release, deployment, or publication. |
| **Mobile fixture profile** | The fixture declares a 390 × 844 viewport, device-scale factor 3, touch/mobile flags, archive and tile byte limits, and verification/decode-render time limits. | Those values are test-fixture limits, not production defaults, browser-support claims, or device-class policy. |
| **Verified rendering resource envelope** | A closed candidate contract/schema/validator family checks a synthetic worker-message trace, verify-before-decode ordering, chunk accounting, and declared fetch/hash/decode/heap/CPU/queue/concurrency budgets. | It does not fetch, hash, parse a proof, verify a signature, decode, render, select a renderer, or authorize execution. |
| **Public map service SLO assessment** | A closed candidate family validates synthetic measurement-window declarations, availability arithmetic, latency objectives/observations, support references, and error-budget arithmetic. | It does not query a service, authenticate telemetry, select a production SLO, apply promotion, execute rollback, release, deploy, or publish. |
| **Explorer Web** | The app has a real toolchain and bounded fixture-first projections, including the mobile PMTiles proof. Its default shell remains fail-closed. | No integrated live map, admitted renderer, production route tree, released layer, or operational performance monitor is established. |
| **UI telemetry architecture** | Current documentation inventories four bounded telemetry profiles and explicit operational holds. | No general `TelemetryEvent` contract/schema, operative general validator/policy, UI emitter, governed ingestion route, sink, retention regime, dashboard, or emitted telemetry receipt instance. |
| **Map Master architecture** | The parent page identifies performance budgets as a tracked draft and records the renderer/runtime HOLD. | It does not accept threshold numbers or make this page executable authority. |

### Maturity ladder

```text
CONFIRMED
  bounded synthetic byte and timing checks
  deterministic resource-envelope arithmetic
  deterministic service-SLO arithmetic
  explicit finite negative cases
  no-network fixture workflows

PROPOSED
  production device/workload profiles
  real renderer measurements
  governed performance event envelope
  service objectives and alerting policy
  visible degradation mapping

HOLD
  MapLibre runtime admission
  operational UI telemetry
  automated performance-based release or rollback effects

UNKNOWN
  deployed service behavior
  real-device distribution
  production CDN/Range/CORS behavior
  dashboards, alerts, retention, incident response
  public availability and release state
```

[Back to top](#top)

---

<a id="1-scope"></a>

## 1. Scope

This page defines the architecture boundary for map-performance budgets across:

- immutable or server-mediated map carriers;
- verification-before-decode work;
- browser decode/render work;
- renderer resource consumption;
- interaction responsiveness;
- public-map-service availability and latency;
- error-budget arithmetic;
- visible degradation;
- accessibility-preserving fallback;
- privacy-safe observability;
- correction and rollback.

It also reconciles current repository evidence with the prior v0.1 proposal.

### In scope

- Performance measurement dimensions and their authority owners.
- The three current fixture-first implementation families.
- Finite over-budget and incomplete-measurement outcomes.
- Requirements for production profile admission.
- Mobile-first, low-resource, and accessibility constraints.
- Separation between client resource budgets and service SLOs.
- Performance evidence needed before a released public map can claim fitness for use.
- Re-review, correction, supersession, and rollback triggers.

### Out of scope

- Selecting production threshold numbers.
- Accepting a device-class vocabulary.
- Installing or admitting MapLibre, PMTiles, COG, telemetry, monitoring, or profiling dependencies.
- Creating a generic budget contract, schema, policy bundle, configuration file, route, emitter, sink, dashboard, alert, or retention schedule.
- Benchmarking a live endpoint or real device.
- Changing map, API, release, deployment, publication, or repository settings.
- Treating a performance pass as evidence truth or public-use authority.

### When this page should be consulted

Use this page when:

- adding or changing a map carrier or renderer path;
- defining a service SLO candidate;
- building a worker or browser measurement profile;
- reviewing a mobile or low-resource fallback;
- deciding whether a performance regression should hold a candidate;
- designing performance telemetry or an operational runbook;
- documenting correction or rollback after a released map becomes unusable.

[Back to top](#top)

---

<a id="2-budget-categories"></a>

## 2. Budget categories

Performance is not one number. KFM needs separate, composable budget families because each answers a different question and carries a different proof burden.

### 2.1 Carrier and transfer budgets

| Dimension | Meaning | Current evidence | Production status |
|---|---|---|---|
| Artifact bytes | Total immutable carrier size or bounded server response size. | Declared in current fixture profiles. | Thresholds unresolved. |
| Requested/fetched bytes | Bytes transferred for the requested scope. | Synthetic declaration in the rendering envelope; mobile proof uses caller-supplied bytes and no fetch. | Live network measurement not established. |
| Tile/range bytes | Bytes for one tile, range, or chunk. | Mobile PMTiles fixture verifies one digest-bound range and tile. | Real workload distribution unknown. |
| Hash-chunk bytes | Maximum verification chunk size. | Closed field in the rendering resource envelope. | Production profile unresolved. |
| Request count/concurrency | Simultaneous transfer pressure. | Synthetic resource-envelope declaration. | No live transport probe established. |
| Range/CORS capability | Whether the released host supports required delivery behavior. | Separate artifact/release concern; not proved by this page. | NEEDS VERIFICATION per release. |

Carrier limits protect resource use. They do not prove that a file is semantically correct, evidence-backed, public-safe, or released.

### 2.2 Verification and decode budgets

| Dimension | Meaning | Current evidence | Production status |
|---|---|---|---|
| Verification time | Time spent checking declared archive/index/tile bindings. | `verifyMs` measured by the mobile fixture. | Tiny synthetic input only. |
| Hashed bytes | Bytes covered by the declared verification process. | Synthetic worker-envelope accounting. | No live hasher integration. |
| Decode time | Time to decode the selected carrier payload. | `decodeRenderMs` measured through an injected PNG adapter in mobile emulation. | No MapLibre or production tile decoder proof. |
| Decoded bytes | Expanded data volume after decode. | Synthetic worker-envelope declaration. | No live decoder accounting. |
| Verify-before-decode ordering | Unverified bytes must not reach decode/render. | Deterministically assessed in the resource-envelope fixture family. | Runtime enforcement remains separate. |

> [!IMPORTANT]
> A timing result is admissible only when the measurement scope is explicit. “Decode took 40 ms” is incomplete without the carrier identity, digest, workload, device/environment profile, decoder version, measurement boundaries, warm/cold state, sample count, and whether verification happened first.

### 2.3 Renderer and interaction budgets

| Dimension | Meaning | Current repository status |
|---|---|---|
| Peak heap | Maximum observed or declared memory pressure for the scoped operation. | Synthetic resource-envelope field; no admitted live renderer measurement. |
| CPU time | CPU consumed by the bounded worker/rendering operation. | Synthetic resource-envelope field; no live renderer proof. |
| GPU memory | Estimated or measured texture/buffer residency. | PROPOSED; no current machine profile established. |
| Queue depth | Pending rendering or worker tasks. | Synthetic resource-envelope field. |
| Concurrency | Simultaneous work units. | Synthetic resource-envelope field. |
| Frame time / frame stability | Responsiveness during pan, zoom, animation, and layer updates. | PROPOSED; no current general frame probe established. |
| Long tasks / main-thread blocking | User-visible responsiveness risk. | PROPOSED; no current general browser profile established. |
| Time to usable map | Time until the required released base state and accessible status are usable. | PROPOSED; prior “cold-start” language was not backed by a current executable profile. |
| Interaction latency | Delay from user action to bounded visible response. | PROPOSED; no integrated map runtime. |

### 2.4 Service SLO and error-budget dimensions

The current `PublicMapServiceSLOAssessmentCandidate` uses a separate vocabulary:

- measurement-window start, end, and completeness;
- service kind;
- availability target in basis points;
- eligible events and good events;
- latency percentile;
- latency target, observation, sample count, and state;
- allowed, observed, and remaining bad events;
- support references;
- finite report outcome.

This is intentionally separate from client heap, decode, or frame budgets. A service can meet its availability objective while a browser is unusable, and a browser can render a local fixture quickly while the public service is unavailable.

### 2.5 Accessibility and trust budgets

Accessibility and truth cannot be “traded away” to meet latency:

| Obligation | Performance relationship |
|---|---|
| Accessible status | Loading, held, degraded, denied, stale, and error states need text and programmatic semantics, not color alone. |
| Keyboard and focus behavior | Optimization must not remove reachable controls or reliable focus return. |
| Reduced motion | Animation may be reduced or disabled without hiding the same evidence and outcome. |
| Non-map alternative | A map failure must retain an accessible explanation or tabular/text alternative when the released product contract requires one. |
| Evidence parity | Lower-detail or fallback views must preserve the same evidence, policy, release, and correction context. |
| Sensitive geometry | Performance pressure never authorizes weaker redaction, generalization, delay, or access controls. |

<a id="budget-authority"></a>

### 2.6 Budget authority

The prior page said “budgets are doctrine.” The corrected boundary is narrower:

- **CONFIRMED doctrine:** performance failures must be visible; public clients remain downstream of trust; unknown or unsafe state fails closed.
- **CONFIRMED implementation:** selected fixture profiles declare bounded values and validate arithmetic or ordering.
- **PROPOSED policy/profile:** production thresholds, workload classes, device/environment classes, and release significance.
- **UNKNOWN operation:** deployed measurements, alerts, dashboards, and enforcement.

A production threshold needs an accountable owner, semantic meaning, machine shape, scope, version, review state, evidence basis, change procedure, and rollback behavior. Whether that threshold belongs in a semantic profile, configuration, policy, release criteria, or a composed set remains NEEDS VERIFICATION. This page does not create a new `BUDGETS.yaml` or parallel authority.

[Back to top](#top)

---

<a id="3-device-class-profiles"></a>

## 3. Device class profiles

### 3.1 Current verified profile

The only current device-shaped evidence inspected for this page is the synthetic mobile PMTiles fixture:

| Field | Fixture declaration |
|---|---:|
| Viewport | 390 × 844 |
| Device scale factor | 3 |
| Touch | true |
| Mobile | true |
| Network access | none in the browser proof |
| Renderer | injected PNG decode/canvas adapter; MapLibre boot remains HOLD |

This proves the bounded fixture can execute under one mobile-emulated browser configuration. It does not prove real-device performance, market coverage, battery behavior, thermal behavior, memory pressure, browser parity, accessibility conformance, or production fitness.

### 3.2 Legacy profile tokens

The v0.1 page named `MOBILE-LOW`, `MOBILE-MID`, `TABLET`, `DESKTOP-STD`, and `DESKTOP-HI`. No accepted machine profile or production thresholds for those names were established by the inspected evidence.

| Legacy token | Current status | Safe treatment |
|---|---|---|
| `MOBILE-LOW` | PROPOSAL LINEAGE | Do not branch runtime or release behavior on this token without an admitted profile. |
| `MOBILE-MID` | PROPOSAL LINEAGE | Same. |
| `TABLET` | PROPOSAL LINEAGE | Same. |
| `DESKTOP-STD` | PROPOSAL LINEAGE | Same. |
| `DESKTOP-HI` | PROPOSAL LINEAGE | Same. |

The old claim that the shell detects a class from `navigator` and connection hints, then lets the user override it, is not current implementation evidence. Device detection can also create fingerprinting, instability, accessibility, and support risks. It remains a design decision.

### 3.3 Minimum production profile contract

Before KFM admits any device/environment profile, it should define:

| Field family | Required content |
|---|---|
| Identity | Stable profile ID, semantic version, deterministic digest, supersession relation. |
| Scope | Browser/runtime family, viewport range, input modes, memory/CPU assumptions, network condition, accessibility modes, workload class. |
| Carrier set | Which released artifact types and size classes are covered. |
| Measurement method | Warm/cold state, sample count, percentile, clock, start/end boundaries, outlier rule, timeout. |
| Resource limits | Transfer, verification, decode, heap, CPU, queue, concurrency, frame, and interaction limits as applicable. |
| Fallbacks | Predeclared released fallback references; no client-invented semantic substitution. |
| Policy | Audience, rights, sensitivity, telemetry, and public-use obligations. |
| Review | Accountable review record and independent accessibility/performance review where required. |
| Release binding | Release/artifact refs, correction path, rollback target, expiry or revalidation trigger. |
| Limitations | Unsupported devices, browsers, datasets, operations, and known confidence limits. |

### 3.4 Profile selection rules

A future selector should:

1. use only admitted, privacy-reviewed signals;
2. expose the selected profile and why it was selected;
3. allow a safer/lower-resource choice without weakening evidence or policy;
4. preserve user accessibility preferences;
5. avoid claiming precise hardware capability from weak browser hints;
6. return a finite hold or conservative profile when selection is uncertain;
7. record profile version with any performance receipt;
8. never treat a profile as release authority.

[Back to top](#top)

---

<a id="4-runtime-probes"></a>

## 4. Runtime probes

The old page described per-tile, per-frame, per-request, and per-session probes as if operational. Current evidence supports a narrower statement: selected fixture code measures or validates bounded values; a general map-runtime probe system is not established.

### 4.1 Current measurement and declaration surfaces

| Surface | Values | Execution depth |
|---|---|---|
| Mobile PMTiles verifier | archive bytes, tile bytes, verification milliseconds, decode/render milliseconds | Actual timing over tiny caller-supplied synthetic bytes and an injected PNG adapter; no network or MapLibre |
| Verified rendering resource envelope | artifact/fetched/hashed/decoded bytes, peak heap, CPU ms, max queue depth, max concurrency, chunk accounting, worker-stage ordering | Synthetic declarations validated locally; no actual fetch/hash/decode/render |
| Public map service SLO assessment | availability counts/target, latency percentile/target/observation/sample count, error-budget arithmetic | Synthetic declarations validated locally; no live service or authenticated telemetry |
| General UI telemetry | None admitted for operational use | HOLD |

### 4.2 Measurement evidence levels

| Level | Minimum evidence | Permitted claim |
|---|---|---|
| `DECLARED_FIXTURE` | Closed synthetic input plus deterministic validator. | “The declaration and arithmetic conform to the fixture profile.” |
| `EXECUTED_SYNTHETIC` | Bounded code executes over synthetic bytes/environment. | “This exact synthetic case completed within the declared fixture limit.” |
| `EXECUTED_REPRESENTATIVE` | Versioned representative artifacts and admitted environment matrix. | “These representative workloads met the profile under stated conditions.” |
| `OPERATIONAL_OBSERVATION` | Governed producer, transport, policy, sink, retention, and authenticated support. | “The deployed service/runtime observed these measurements for this window.” |
| `RELEASE_GATING_EVIDENCE` | Accepted policy, accountable review, release binding, correction and rollback. | “The evidence was considered by the governed release process.” |

Current KFM map-performance evidence inspected here reaches the first two levels only.

### 4.3 Required probe metadata

Any future probe or receipt should bind at least:

- probe/profile ID and version;
- code/build identity;
- artifact and release identity;
- carrier digest;
- environment and workload profile;
- measurement start/end;
- monotonic clock or equivalent method;
- warm/cold/cache state;
- sample count and percentile rule;
- value and unit;
- timeout and cancellation state;
- finite outcome and stable finding codes;
- policy and review references where material;
- limitations and redaction posture;
- correction/supersession lineage.

### 4.4 Probe safety

A probe must not:

- fetch unreleased or internal material from a public client;
- send raw evidence, prompts, credentials, exact restricted coordinates, full upstream URLs, or unbounded feature properties;
- use user identifiers when aggregate or session-local measurement is sufficient;
- expose policy internals or sensitive denial reasons;
- turn an absent telemetry sink into permissive behavior;
- retry indefinitely;
- keep measuring after cancellation or page teardown;
- write `PUBLISHED` state;
- claim that timing proves semantic correctness.

### 4.5 Determinism and variance

Performance observations are inherently variable. Deterministic identity should bind the **profile and inputs**, not pretend that timing values are deterministic. Production evidence should report distributions, sample counts, environment conditions, and uncertainty rather than a single persuasive number.

[Back to top](#top)

---

<a id="5-over-budget-handling"></a>

## 5. Over-budget handling

Over-budget behavior must be finite, visible, accessible, and non-authoritative.

### 5.1 Keep existing vocabularies separate

Current candidate families use different finite vocabularies for different responsibilities:

| Family | Finite vocabulary | Meaning |
|---|---|---|
| Public map service SLO assessment | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | Assessment/report outcome for a declared service window. |
| Verified rendering resource envelope | `READY_FOR_SEPARATE_EXECUTION`, `DEGRADED`, `BLOCKED`, `CANCELLED`, `ERROR` | Synthetic trace/resource assessment; no rendering is authorized. |
| Mobile PMTiles verifier | `PASS`, `DENY`, `ERROR` | Exact fixture verification/decode-render result; authority remains `NONE`. |
| User-facing Explorer state | Existing finite governed-response and feature-specific states | Presentation contract; must not be silently inferred from another family. |

This page does not collapse them into one enum. Any cross-family mapping needs a reviewed adapter contract.

### 5.2 Decision matrix

| Condition | Safe architecture result | User-facing obligation | Authority effect |
|---|---|---|---|
| Measurement/profile support missing | `ABSTAIN`, `INCOMPLETE`, or `HOLD` as the owning contract defines | Explain that fitness is unassessed; do not imply “no data.” | None |
| Declared resource limit exceeded before execution | `BLOCKED` or `DENY` | Show a bounded resource-limit state and available safe alternative. | None |
| Verification fails | `DENY` or `BLOCKED` | Never decode or show unverified content. | None |
| Timeout | `BLOCKED` or `ERROR` | Show timeout and retry/cancel options if admitted. | None |
| User cancellation | `CANCELLED` | Stop work, clear transient output, preserve prior safe view. | None |
| Worker/runtime failure | `ERROR` | Show safe fixed copy; do not leak internal values. | None |
| Predeclared lower-detail fallback is valid and released | `DEGRADED` candidate | Identify the fallback, lost detail, evidence/release identity, and correction state. | No automatic release effect |
| Service error budget exhausted | `DENY` or review hold according to accepted policy | Surface service degradation; do not auto-promote or silently reroute to an ungoverned source. | Review only unless separate policy decides otherwise |
| Required map carrier unavailable | Held/degraded/error state | Preserve accessible evidence summary where allowed; never render a blank as “no observations.” | None |

### 5.3 Rules for visible degradation

A degradation is admissible only when:

1. the fallback is predeclared and versioned;
2. its artifact is separately verified and released;
3. evidence, policy, rights, sensitivity, time, and correction context remain visible;
4. the loss of detail is explicit;
5. it cannot reveal more precise or restricted information;
6. it preserves an accessible equivalent or clearly states the limitation;
7. the user can distinguish fallback content from the preferred representation;
8. the event is reviewable without leaking sensitive payloads;
9. returning to the preferred representation is deterministic;
10. no performance result is misrepresented as a policy or release decision.

### 5.4 Unsafe runtime “optimizations”

The following require rejection or a separate governed transform:

- dropping features without a disclosed sampling/generalization method;
- changing geometry precision client-side to escape a budget;
- removing evidence or trust indicators;
- substituting a stale archive without release/correction context;
- disabling accessibility behavior to reduce work;
- bypassing verify-before-decode;
- loading an upstream provider directly when the governed path is slow;
- lowering redaction or sensitivity controls;
- changing the claim scope to make a number look compliant;
- recording “success” after required layers failed.

### 5.5 Correction and rollback

If a released map later violates its admitted performance or accessibility profile:

1. preserve the original observations and release lineage;
2. classify whether the issue is artifact, hosting, client, profile, telemetry, policy, or environment related;
3. issue correction, hold, withdrawal, supersession, or rollback through the owning release process;
4. invalidate affected caches and aliases when required;
5. keep the prior safe rollback target available;
6. update public status and accessible alternatives;
7. re-measure against the same profile or a transparently superseding profile;
8. never edit historical receipts or measurements in place.

[Back to top](#top)

---

<a id="6-mobile-first-tile-playbook"></a>

## 6. Mobile-first tile playbook

“Mobile-first” means the base public experience must remain useful, inspectable, and safe under constrained resources. It does not make one artifact format universally canonical, and it does not turn one emulated fixture into a production device policy.

### 6.1 What the current mobile fixture proves

The current bounded proof:

1. receives a synthetic PMTiles archive and JSON sidecars from its caller;
2. validates closed packet shape and fixed authority holds;
3. verifies archive and sidecar digests;
4. checks PMTiles v3 header/metadata constraints for the fixture;
5. checks PMIDX Merkle/range/tile bindings;
6. checks structural PMSIG and RunReceipt subject bindings;
7. extracts one PNG tile from a declared byte range;
8. invokes an injected PNG decode/canvas render adapter;
9. records verification and decode/render durations;
10. runs under a 390 × 844 mobile-emulated Playwright profile;
11. denies tamper and authority-overclaim cases;
12. makes no external request.

MapLibre boot, cryptographic verification, release authorization, real-device performance, hosting behavior, and public use remain explicit holds.

### 6.2 Fixture values are not production defaults

| Fixture limit | Value | Correct interpretation |
|---|---:|---|
| Maximum archive bytes | 4,096 | Bounds one tiny synthetic archive only. |
| Maximum tile bytes | 1,024 | Bounds one tiny synthetic PNG only. |
| Maximum verification time | 2,500 ms | Prevents an unbounded fixture run; not a public SLO. |
| Maximum decode/render time | 2,500 ms | Prevents an unbounded fixture run; not an interaction target. |

Do not copy these numbers into production configuration, policy, documentation badges, or release criteria without representative evidence and review.

### 6.3 Production mobile graduation

Before claiming mobile readiness, KFM needs:

- admitted renderer and protocol dependencies;
- representative released PMTiles/COG/server-mediated artifacts;
- real archive/range/tile size distributions;
- verification and decode measurements over representative payloads;
- real browser and device coverage;
- constrained network profiles;
- memory, CPU, long-task, frame, interaction, battery, and thermal observations where material;
- keyboard, touch, screen-reader, contrast, reduced-motion, zoom, and non-map alternatives;
- no-external-internal-store and no-sensitive-egress tests;
- CDN/host Range, CORS, cache, correction, and invalidation evidence;
- profile versioning and deterministic workload identity;
- governed telemetry or signed benchmark receipts;
- release review, correction path, and rollback rehearsal.

### 6.4 Artifact-selection posture

Performance may inform artifact selection, but it cannot decide authority.

| Candidate | Performance question | Separate trust questions |
|---|---|---|
| PMTiles | Can immutable range delivery and verification meet the admitted workload profile? | Is the exact archive released, digest-bound, policy-safe, and correctly hosted? |
| COG | Can required windows/overviews be retrieved and decoded within the profile? | Is the raster semantically valid, public-safe, released, and Range/CORS-capable? |
| Server-mediated layer | Can the governed service meet availability, latency, load, and cost objectives? | Does the service enforce policy and return only released public-safe data? |
| Composite map surface | Can required components become usable together? | Are all components mutually compatible in evidence, time, policy, release, and correction state? |

A faster ungoverned path is not a fallback.

[Back to top](#top)

---

<a id="7-3d-additional-budgets"></a>

## 7. 3D additional budgets

### 7.1 Current state

The sibling [`2D_3D_PARITY.md`](2D_3D_PARITY.md) is now a repository-grounded v1.0 architecture page. It replaces the old dual-renderer assumption with a renderer-neutral trust-parity boundary and records bounded `ThreeDAdmissionDecision`, `RealityBoundaryNote`, and `RepresentationReceipt` evidence. That update still keeps renderer boot, scene release, GPU profiling, deployment, and publication on HOLD. No current live 3D renderer, admitted scene package, GPU profile, or enforceable performance gate was established for this update.

Therefore:

- 3D performance thresholds are **PROPOSED**;
- live 3D performance is **UNKNOWN**;
- renderer and scene admission remain **HOLD**;
- no 3D result may be inferred from 2D or mobile PMTiles fixture success.

### 7.2 Future 3D dimensions

A separately admitted 3D profile may need:

| Dimension | Why separate evidence is required |
|---|---|
| Scene manifest and asset bytes | A scene can compose terrain, textures, models, point clouds, and overlays. |
| GPU memory | Browser heap does not capture texture/buffer residency. |
| Shader compile and pipeline setup | Cold/warm behavior can differ materially. |
| Terrain/mesh decode | Format and level-of-detail behavior differ from 2D tiles. |
| Point-cloud decode/draw | Density and culling have distinct cost and privacy implications. |
| Frame stability | Camera motion, transparency, terrain, and custom layers can create sustained regressions. |
| Camera-path motion | Reduced-motion and motion-independent outcomes are mandatory. |
| 2D parity fallback | The fallback must preserve evidence and policy, not merely show a screenshot. |
| Context loss | Generalization, occlusion, vertical exaggeration, and synthetic reconstruction must remain disclosed. |

### 7.3 3D admission requirements

A 3D performance candidate should remain held until:

1. renderer and plugin/dependency admission are accepted;
2. scene and representation contracts are accepted;
3. artifact integrity and release binding close;
4. representative browser/device/GPU evidence exists;
5. 2D evidence parity and non-map alternatives are proved;
6. sensitive geometry and reconstruction risk are reviewed;
7. cancellation, timeout, context loss, and recovery paths are tested;
8. correction/cache invalidation and rollback are rehearsed.

[Back to top](#top)

---

<a id="8-telemetry"></a>

## 8. Telemetry

### 8.1 Current boundary

The prior page named `/api/v1/telemetry` as the sink and described probe sampling behavior as operational. Current repository evidence does not support those claims.

The current UI telemetry architecture records:

- four bounded fixture-first telemetry profiles;
- no admitted general UI telemetry event contract or schema;
- a placeholder general telemetry safety validator;
- non-enforcing general Rego stubs;
- no established Explorer emitter;
- no governed ingestion route;
- no collector, exporter, sink, dashboard, or retention regime;
- no confirmed telemetry receipt instances.

Accordingly, operational performance telemetry remains on **HOLD**.

### 8.2 Telemetry is not truth

Performance telemetry may support operations and review. It must not become:

- evidence for a domain claim;
- a source of protected geometry;
- a substitute for an artifact digest;
- proof of policy enforcement;
- authenticated review;
- a release decision;
- a public status claim without a separate governed projection.

### 8.3 Minimum future performance-event posture

Before operational emission, KFM needs a reviewed event family covering:

| Concern | Requirement |
|---|---|
| Event identity | Stable profile/version and bounded event name. |
| Measurement | Value, unit, method, scope, sample count/window, environment/workload refs. |
| Context | Safe artifact/release/profile refs, not raw evidence payloads. |
| Minimization | Allowlisted fields; no unnecessary identifiers or URLs. |
| Sensitivity | Source-side classification and suppression before egress. |
| Reconstruction risk | Prevent joins that reveal protected people, places, or activity. |
| Policy | Finite allow/deny/hold/error outcome before transport. |
| Transport | Authenticated, bounded, retry-limited, and fail-closed. |
| Retention | Purpose-bound duration, access, deletion/correction, and incident handling. |
| Receipt | Auditable process memory where significance requires it. |
| Operations | Sink health, backpressure, drop policy, and no-publish boundary. |
| Public projection | Separate release-reviewed summary; clients never read the operational sink directly. |

### 8.4 Allowed and forbidden classes

| Potentially admissible after contract and policy | Forbidden by default |
|---|---|
| Bounded duration, byte count, queue depth, finite outcome code, profile/version ref | Raw evidence or source payloads |
| Coarse admitted environment/workload class | Precise device fingerprint |
| Released artifact and release references | Credentials, tokens, signed URLs |
| Stable non-sensitive layer or feature-family identifier | Exact restricted coordinates |
| Aggregated error category | Prompts, model input/output, hidden reasoning |
| Correction/supersession reference | Full upstream provider URLs or query strings |
| Accessibility mode category when necessary and privacy-reviewed | Living-person identity or behavior trail |
| Sampling/drop metadata | Policy internals or sensitive denial details |

### 8.5 Opt-out and essential local measurement

A future design must distinguish:

- local ephemeral measurement needed to keep the current session safe;
- governed operational emission;
- public operational summaries.

A user opt-out may stop emission while local safeguards still operate, but that behavior needs an accepted contract and privacy review. The old page's opt-out claim is proposal lineage, not current runtime evidence.

[Back to top](#top)

---

<a id="9-anti-patterns"></a>

## 9. Anti-patterns

| Anti-pattern | Why it is unsafe | Required correction |
|---|---|---|
| Treating fixture limits as production budgets | Synthetic values lack representative evidence. | Label fixture scope and create a reviewed production profile. |
| Calling a validator `PASS` a live benchmark | Declaration conformance is not operational measurement. | State the executed evidence level. |
| Blank map after failure | Users may infer “no observations.” | Expose a finite accessible failure/degraded state. |
| Verify after decode | Unverified bytes reach a higher-risk stage. | Enforce verify-before-decode ordering. |
| Using performance to bypass governed API | A faster path becomes a second trust authority. | Use only released public-safe artifacts or governed interfaces. |
| Silent feature dropping | Changes the apparent claim. | Use a governed transform/fallback with explicit loss disclosure. |
| Client-side sensitivity reduction | Browser code cannot grant safer authority. | Apply reviewed transforms upstream and bind receipts. |
| Universal “mobile” threshold | Devices, browsers, workloads, and accessibility settings vary. | Version scope-specific profiles and report limitations. |
| Fingerprinting as device classification | Creates privacy and stability risk. | Use minimal reviewed signals and conservative fallback. |
| One average hides tail latency | User harm occurs in the tail. | Define percentiles, sample count, window, and outlier rule. |
| Availability SLO used as browser-performance proof | Service and client budgets are different. | Keep assessment families separate. |
| Auto-release on green performance | Performance is one input, not release authority. | Require separate policy, review, release, and rollback controls. |
| Auto-rollback from unauthenticated telemetry | Weak signals can cause unsafe transitions. | Keep current SLO rollback effect review-only. |
| Per-frame telemetry with unbounded cardinality | Cost, privacy, and reconstruction risk. | Sample, aggregate, allowlist, and bound. |
| Telemetry route asserted before implementation | Documentation invents runtime behavior. | Mark route/sink HOLD until code, policy, tests, and operations exist. |
| 3D gate treated as implemented because prose names it | Architecture vocabulary is not enforcement. | Require contract/schema/validator/runtime evidence. |
| Disabling accessibility to meet a budget | Produces an unusable public surface. | Treat accessibility as a non-negotiable constraint. |
| Stale fallback without correction state | Users see superseded content as current. | Bind fallback to release, freshness, and correction lineage. |
| Performance badge without evidence | Polish is mistaken for proof. | Link to bounded evidence or omit the badge. |
| Editing historical measurements | Erases audit and regression context. | Append correction/supersession records. |

[Back to top](#top)

---

<a id="10-open-questions-and-adr-triggers"></a>

## 10. Open questions and ADR triggers

### 10.1 Prioritized verification register

| ID | Priority | Question | Closure evidence |
|---|---:|---|---|
| PB-01 | P0 | Who owns production map-performance profile semantics, policy, review, and operations? | Verified stewardship assignments and review route. |
| PB-02 | P0 | Which renderer/runtime is admitted, and what is the exact measurement boundary? | Accepted decision, pinned dependency, adapter implementation, tests. |
| PB-03 | P0 | Which performance failures block execution, hold release, or require human review? | Accepted policy/decision contract with finite outcomes. |
| PB-04 | P0 | How are lower-detail fallbacks predeclared, verified, released, and corrected? | Contract/schema, fixtures, policy, release refs, rollback drill. |
| PB-05 | P0 | What event fields may leave the browser or worker? | General telemetry contract/schema, operative policy, validator, privacy review. |
| PB-06 | P1 | What representative artifact/workload matrix covers PMTiles, COG, server-mediated, and composite surfaces? | Versioned workload corpus with digests and limitations. |
| PB-07 | P1 | What real browser/device/network matrix is supported? | Reproducible benchmark records and accessibility review. |
| PB-08 | P1 | What production service objectives and error-budget windows apply by service kind? | Reviewed SLO policy refs and operational measurement support. |
| PB-09 | P1 | How are frame, long-task, interaction, and time-to-usable-map metrics defined? | Accepted measurement profile and cross-browser tests. |
| PB-10 | P1 | Which check results are release-significant, and how are inherited/external failures classified? | Release-gate mapping and reviewer checklist. |
| PB-11 | P2 | What Range/CORS/cache behavior is required at deployed hosts? | Live preflight, receipts, correction/invalidation rehearsal. |
| PB-12 | P2 | What operational telemetry backend, retention, and incident path are admitted? | Security/privacy review, runbooks, sink and deletion tests. |
| PB-13 | P2 | What 3D/GPU/scene profiles are needed? | Renderer/scene decisions and representative measured proof. |
| PB-14 | P2 | What sustained, soak, battery, and thermal evidence is required? | Long-run benchmark profile and operations acceptance criteria. |
| PB-15 | P3 | Can adaptive scheduling improve performance without changing evidence meaning? | Controlled experiment and reviewed deterministic fallback rules. |

### 10.2 ADR triggers

A new ADR or amendment is likely when work would:

- select a canonical production budget/profile authority;
- make a new contract, policy, registry, configuration, or release-significant home;
- change renderer or package ownership;
- adopt device classification inputs with privacy implications;
- make performance results automatic promotion or rollback inputs;
- approve a direct public delivery path;
- change the telemetry trust boundary;
- change 2D/3D admission or parity doctrine;
- weaken accessibility, sensitivity, evidence, or release obligations.

Routine measured-profile additions under an already accepted authority may not need a new ADR, but they still need contract/schema/policy/review evidence appropriate to consequence.

### 10.3 Stop conditions

Stop or narrow implementation when:

- threshold authority is unresolved;
- representative workload or environment identity is missing;
- telemetry fields can leak sensitive or identifying information;
- fallback changes claim meaning without a governed transform;
- renderer or protocol dependencies are unadmitted;
- release/correction/rollback bindings are absent;
- a proposed optimization bypasses verify-before-decode;
- a public client would read an internal or candidate store;
- accessibility parity is unproved;
- a green fixture result is being used to claim operational readiness.

[Back to top](#top)

---

<a id="11-related-docs"></a>

## 11. Related docs

| Reference | Role | Current posture |
|---|---|---|
| [`README.md`](README.md) | Map Master lane boundary and current repository maturity | Repository-grounded; renderer/runtime HOLD |
| [`../map-shell.md`](../map-shell.md) | Broader map-shell architecture | Human architecture; implementation depth must be checked independently |
| [`TILE_ARTIFACTS.md`](TILE_ARTIFACTS.md) | Carrier and integrity architecture | Draft; format-specific proof remains mixed |
| [`VIEWER_VERIFICATION.md`](VIEWER_VERIFICATION.md) | Verify-before-render architecture | Draft; do not infer live viewer enforcement |
| [`2D_3D_PARITY.md`](2D_3D_PARITY.md) | 2D/3D trust-parity boundary and bounded candidate evidence | Repository-grounded v1.0; renderer, scene release, deployment, and publication remain HOLD |
| [`../ui/MAP_RUNTIME_BOUNDARY.md`](../ui/MAP_RUNTIME_BOUNDARY.md) | UI-to-map-runtime authority boundary | Human architecture; preserves renderer and trust holds |
| [`../ui/TELEMETRY.md`](../ui/TELEMETRY.md) | Current telemetry inventory and graduation map | Repository-grounded fixture evidence; operational telemetry HOLD |
| [`../../../apps/explorer-web/README.md`](../../../apps/explorer-web/README.md) | Current browser-shell implementation boundary | Real toolchain and bounded slices; no live integrated map |
| [`../../../apps/explorer-web/src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md`](../../../apps/explorer-web/src/features/map_runtime/MOBILE_PMTILES_VERIFICATION_FIXTURE.md) | Mobile synthetic archive/range/decode-render proof | Executed synthetic fixture; MapLibre/release HOLD |
| [`../../../contracts/runtime/verified_rendering_resource_envelope.md`](../../../contracts/runtime/verified_rendering_resource_envelope.md) | Worker-trace and resource-budget candidate meaning | Proposed-inactive, fixture-only |
| [`../../../contracts/validation/public_map_service_slo_assessment.md`](../../../contracts/validation/public_map_service_slo_assessment.md) | Service SLO/error-budget candidate meaning | Proposed-inactive, fixture-only |
| [`../../adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Placement authority | Accepted |
| [`../../doctrine/directory-rules.md`](../../doctrine/directory-rules.md) | Responsibility-root and lifecycle placement law | Adopted exact bytes through ADR-0029 |

[Back to top](#top)

---

<a id="12-appendix"></a>

## 12. Appendix

### 12.1 Current field crosswalk

| Architecture concept | Current repository field/example | Boundary |
|---|---|---|
| Archive bytes | `archiveBytes`, `max_archive_bytes` | Mobile synthetic fixture only |
| Tile bytes | `tileBytes`, `max_tile_bytes` | One synthetic PNG tile |
| Verification duration | `verifyMs`, `max_verify_ms` | Measured locally in fixture execution |
| Decode/render duration | `decodeRenderMs`, `max_decode_render_ms` | Injected PNG/canvas adapter, not MapLibre |
| Fetch bytes | `fetch_bytes`, `fetched_bytes` | Synthetic resource-envelope declaration |
| Hash chunk bytes | `hash_chunk_bytes`, chunk declarations | Synthetic accounting |
| Decode bytes | `decode_bytes`, `decoded_bytes` | Synthetic accounting |
| Heap | `heap_bytes`, `peak_heap_bytes` | Synthetic accounting |
| CPU | `cpu_ms` budget and observation | Synthetic accounting |
| Queue depth | `queue_depth`, `max_queue_depth` | Synthetic accounting |
| Concurrency | `concurrency`, `max_concurrency` | Synthetic accounting |
| Availability | target basis points, eligible/good events | Synthetic SLO declaration |
| Latency | percentile, target/observed ms, sample count | Synthetic SLO declaration |
| Error budget | allowed/observed/remaining bad events | Deterministic arithmetic |
| Frame time | No admitted general field identified | PROPOSED |
| Long tasks | No admitted general field identified | PROPOSED |
| Time to usable map | No admitted general field identified | PROPOSED |
| Operational telemetry route | None established | HOLD |

### 12.2 Repository-native validation entry points

These commands describe existing bounded checks. They were not rerun in this connector-only documentation update and do not prove production readiness.

Public map service SLO fixture profile:

```bash
python -m unittest -v \
  tests.validators.test_validate_public_map_service_slo_assessment

python tools/validators/validate_public_map_service_slo_assessment.py \
  --fixtures
```

Verified rendering resource-envelope fixture profile:

```bash
python -m unittest -v \
  tests.validators.test_validate_verified_rendering_resource_envelope

python tools/validators/runtime/validate_verified_rendering_resource_envelope.py \
  --fixtures
```

Mobile PMTiles profile and Explorer browser proof:

```bash
python tools/validators/pmtiles/validate_mobile_verification_fixture.py \
  --fixtures

pnpm --filter explorer-web test
pnpm --filter explorer-web test:browser
```

Workflow evidence is path-scoped under:

- `.github/workflows/public-map-service-slo-assessment.yml`;
- `.github/workflows/verified-rendering-resource-envelope.yml`;
- `.github/workflows/pmtiles-mobile-verification.yml`;
- `.github/workflows/ui-build.yml`.

A green workflow proves only the stages it actually executes at the exact head.

### 12.3 Contributor checklist

Before changing a production-significant map budget:

- [ ] Identify the owning semantic, schema, configuration, policy, runtime, receipt, review, and release surfaces.
- [ ] Pin the exact base and profile version.
- [ ] State workload, artifact, environment, and measurement boundaries.
- [ ] Distinguish declared fixture, synthetic execution, representative execution, and operational evidence.
- [ ] Include positive, incomplete, denied, exhausted, timeout, cancellation, and error cases.
- [ ] Preserve verify-before-decode.
- [ ] Prove no direct internal-store or unreleased-source access.
- [ ] Prove no telemetry leakage or harmful reconstruction.
- [ ] Preserve accessibility, evidence, policy, and release context in fallback states.
- [ ] Use percentiles and sample counts where variance matters.
- [ ] Record limitations and unsupported cases.
- [ ] Keep review, release, correction, and rollback separate.
- [ ] Update this page when the current maturity boundary materially changes.

### 12.4 No-loss modernization ledger

| v0.1 material | v1.0-draft disposition |
|---|---|
| Decode, heap, network, concurrency, frame, and cold-start categories | Preserved, separated into implemented and proposed dimensions. |
| Device-class profiles | Preserved as proposal lineage; unsupported detection/threshold claims removed. |
| Runtime probes | Reconciled to actual fixture evidence and operational HOLD. |
| Visible degradation rule | Preserved and strengthened with finite outcomes, accessibility, and evidence-parity requirements. |
| Mobile-first playbook | Preserved, grounded in the current mobile PMTiles fixture, and stripped of universal format/threshold claims. |
| 3D budgets | Preserved as a held future profile; stale `G3D-6` enforcement claim removed. |
| Telemetry safety | Preserved; invented route/sink and operational sampling claims removed. |
| Open questions | Replaced with a prioritized verification and decision register. |
| Legacy anchors | Preserved for sections 1 through 12. |
| Historical generated receipt | Left immutable as prior authoring lineage; this revision uses a new receipt. |

### 12.5 Truth-label legend

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from current-session GitHub repository evidence or exact checked artifacts. |
| `PROPOSED` | Design or future state not established as current implementation. |
| `UNKNOWN` | Evidence is insufficient to act as fact. |
| `NEEDS VERIFICATION` | A concrete check remains before reliance. |
| `HOLD` | A required decision, implementation, evidence, or review gate remains open. |

### 12.6 Glossary

| Term | Meaning |
|---|---|
| **Budget** | A versioned limit for a defined resource, workload, environment, and measurement method. |
| **Objective / SLO** | A target for service behavior over a defined measurement window. |
| **Error budget** | Allowed bad events derived from an objective and eligible-event population. |
| **Probe** | Code or instrumentation that observes a defined measurement. |
| **Fixture profile** | Synthetic, deterministic test boundary; not operational proof. |
| **Representative benchmark** | Execution over versioned workloads/environments intended to approximate supported use. |
| **Operational observation** | Authenticated measurement from an admitted deployed producer and governed path. |
| **Fallback** | A predeclared alternative representation; never a silent semantic substitution. |
| **Degraded** | A finite state where reduced capability is explicit and trust context remains intact. |
| **Blocked** | Execution must not continue under the owning contract. |
| **Fitness for use** | Evidence that a released product is usable for a stated audience, task, environment, and limitation set. |

---

> **Last reviewed:** 2026-08-19 · **Version:** v1.0-draft · **Path:** confirmed · **Operational map performance:** HOLD / UNKNOWN · **Publication effect:** none

[Back to top](#top)
