<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-maplibre-readme
title: configs/maplibre/ — MapLibre README-Only Configuration, Drift, and Consumer-Binding Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Map steward · MapLibre adapter steward · Explorer Web steward · Governed API steward · Security steward · Policy steward · Release steward · Validation steward · Test steward · Docs steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public; configs; maplibre; readme-only; commit-safe; non-secret; non-authoritative; consumer-bound; renderer-downstream; released-artifacts-only; no-direct-publication; drift-visible
current_path: configs/maplibre/README.md
truth_posture: CONFIRMED repository-present README-only configs/maplibre lane at the inspected path search and named conventional probes, canonical configs root contract, MapLibre architecture and renderer-boundary documents, packages/maplibre README, Explorer Web map-runtime README, proposed sole-renderer ADR, existing MapLibre performance workflow and scripts, absent packages/maplibre-runtime README, absent named policy/maplibre and schemas/contracts/v1/maplibre READMEs, missing config/maplibre/perf-envelope.v1.json, permissive legacy schemas/maplibre/perf-envelope.schema.json, and singular config/maplibre references in workflow/scripts / CONFLICTED configs/ versus config/ path authority, MapLibre performance-envelope home, schema home, workflow trigger coverage, current app path, trust-artifact output homes, and hermetic-network posture / PROPOSED commit-safe MapLibre configuration contract, consumer-binding metadata, precedence rules, validation matrix, migration sequence, and minimum safe implementation slice / UNKNOWN exhaustive recursive inventory, differently named config files, config loader behavior, actual consumers, accepted config DTOs, schema enforcement, policy wiring, runtime binding, deployment binding, complete CI coverage, release use, and owner assignments
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8
  prior_blob: bdf6bc8deb4a1c6cefdb2631b9db3234624f9b7d
related:
  - ../README.md
  - ../examples/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/architecture/maplibre.md
  - ../../docs/architecture/map-master.md
  - ../../docs/architecture/maplibre-master.md
  - ../../docs/architecture/maplibre-3d.md
  - ../../docs/architecture/map-shell.md
  - ../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../docs/architecture/ui/LAYERING.md
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../docs/quality/maplibre-perf-governance.md
  - ../../docs/security/SECRETS.md
  - ../../apps/explorer-web/src/features/map_runtime/README.md
  - ../../packages/maplibre/README.md
  - ../../packages/maplibre-runtime/README.md
  - ../../schemas/maplibre/perf-envelope.schema.json
  - ../../schemas/contracts/v1/maplibre/
  - ../../schemas/contracts/v1/3d/
  - ../../policy/maplibre/
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../scripts/maplibre-smoke-perf.mjs
  - ../../release/
  - ../../data/published/
tags: [kfm, configs, maplibre, renderer, defaults, templates, consumer-binding, map-runtime, styles, layers, tiles, performance, security, secrets, validation, release, rollback, governance]
notes:
  - "At the pinned base, a path-scoped repository search returned configs/maplibre/README.md but no additional file in that lane. Exact probes for viewer.example.yaml, style.example.json, layers.example.yaml, and validation.md returned Not Found."
  - "The existing MapLibre performance workflow and scripts reference singular config/maplibre/perf-envelope.v1.json. That payload was not found, and the workflow path filters do not include configs/maplibre/**."
  - "The performance validator reads schemas/maplibre/perf-envelope.schema.json, which is an open permissive object scaffold, while MapLibre doctrine proposes schemas/contracts/v1/maplibre/ as the governed schema family. Final schema authority remains conflicted."
  - "The performance workflow watches apps/web/**, schemas/maplibre/**, and config/maplibre/**, while current app documentation uses apps/explorer-web/ and Directory Rules identify configs/ as the canonical safe-config root. This README records the drift and does not silently choose a migration."
  - "The smoke script loads MapLibre and glyph assets from public external URLs. Therefore current performance tooling is not proven hermetic or no-network, and endpoint/admission posture remains NEEDS VERIFICATION."
  - "packages/maplibre/README.md exists as a bounded helper-package document. packages/maplibre-runtime/README.md, policy/maplibre/README.md, and schemas/contracts/v1/maplibre/README.md returned Not Found at named probes."
  - "Only this Markdown file changes. No config payload, schema, contract, policy, package code, app code, workflow, script, validator, fixture, test, artifact, lifecycle object, release record, endpoint, secret, path move, or public behavior is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre README-Only Configuration, Drift, and Consumer-Binding Boundary

> `configs/maplibre/` is the canonical-root sublane intended for commit-safe MapLibre defaults and templates. At the inspected repository state, the lane contains this README but no verified configuration payload. It is documentation, not a live viewer configuration, style manifest, layer registry, endpoint allowlist, performance envelope, policy decision, release manifest, or runtime binding.

**Document lifecycle:** `draft v0.2`  
**Observed lane maturity:** `CONFIRMED` README-only at the inspected search and named probes  
**Owning responsibility root:** `configs/` — safe, non-secret configuration defaults and templates  
**Authority:** configuration-boundary documentation only; no truth, schema, contract, policy, source, evidence, lifecycle, release, deployment, renderer, or publication authority  
**Default posture:** commit-safe · non-secret · consumer-bound · versioned · explicit precedence · fail closed · renderer downstream · no public binding by presence alone

> [!IMPORTANT]
> A configuration file can influence renderer behavior, performance, network access, visual emphasis, and public exposure. That influence does **not** make configuration an authority surface. MapLibre may render only governed and released artifacts through accepted consumers; configuration cannot activate a source, admit a plugin, approve a style, release a layer, resolve evidence, override sensitivity, or publish a map.

> [!CAUTION]
> The repository currently contains a path conflict. The canonical root is `configs/`, but MapLibre performance workflow and script bodies refer to `config/maplibre/` in the singular. The expected `config/maplibre/perf-envelope.v1.json` payload was not found, and the workflow does not watch `configs/maplibre/**`. Do not copy files between the paths or treat either spelling as runtime authority without a reviewed migration.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-repository-state) · [Repository fit](#repository-fit) · [Path conflict](#config-versus-configs-path-conflict) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Config classes](#configuration-classes) · [Consumer binding](#consumer-binding-contract) · [Precedence](#precedence-overrides-and-environments) · [Security](#secrets-endpoints-and-network-posture) · [Map trust](#map-trust-release-and-sensitive-geometry-boundaries) · [Styles](#styles-layers-tiles-sprites-and-glyphs) · [Plugins](#plugins-protocols-and-renderer-capabilities) · [Performance](#maplibre-performance-configuration-drift) · [Formats](#formats-naming-and-versioning) · [Validation](#validation) · [Negative cases](#required-negative-cases) · [Tests and CI](#tests-workflows-and-ci) · [Review](#review-burden) · [Change pattern](#safe-change-pattern) · [Implementation sequence](#smallest-safe-implementation-sequence) · [Definition of done](#definition-of-done) · [Evidence](#evidence-basis) · [Open decisions](#open-decisions-and-adr-triggers) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`configs/maplibre/` is intended to hold small, reviewable, non-secret configuration defaults and templates for a **named MapLibre consumer**.

A mature file in this lane should help a maintainer answer:

- which app, package, tool, validator, smoke harness, or review workflow consumes it;
- whether it is a default, template, example, threshold declaration, or compatibility alias;
- which semantic contract owns the meaning of its fields;
- which machine schema validates its shape;
- which policy decisions or release records constrain its use;
- which values are safe defaults and which are placeholders;
- how overrides are resolved;
- whether network access is allowed, denied, or allowlisted;
- how the file is versioned, deprecated, corrected, and rolled back;
- which negative states must fail closed;
- what evidence proves that the consumer actually reads it.

The lane may eventually support safe configuration for:

- local, development, test, or review-only viewport defaults;
- accessibility-safe map interaction defaults;
- bounded cache or performance thresholds;
- debug and diagnostics toggles that are disabled by default;
- named style, layer, legend, sprite, glyph, tile, PMTiles, COG, terrain, globe, or plugin **references**;
- protocol and renderer-capability preferences that remain subordinate to plugin admission and release state;
- synthetic fixture-server references for test-only consumers;
- configuration migration aliases with explicit expiry and rollback;
- deterministic performance-envelope declarations after path and schema authority are accepted.

The lane must not become an alternate map application, renderer package, style registry, source registry, layer catalog, policy bundle, endpoint registry, secret store, release directory, artifact directory, or runtime database.

A config file documents or supplies bounded inputs to a consumer. It does not prove that the consumer exists, imports the file, validates it, applies it, or exposes it safely.

[Back to top](#top)

---

## Authority level

**Canonical configuration sublane / no independent map or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Parent root | **CONFIRMED** | `configs/README.md` identifies `configs/` as the canonical root for safe, non-secret defaults and templates. |
| Current path | **CONFIRMED** | `configs/maplibre/README.md` exists at the pinned base. |
| Current payload inventory | **BOUNDED README-ONLY FINDING** | Path search returned this README; four conventional candidate files were absent at exact probes. Differently named or unindexed files remain `UNKNOWN`. |
| Config consumer | **NOT ESTABLISHED** | No loader, import, route, package binding, merge order, or runtime use is proven by this lane. |
| MapLibre renderer doctrine | **CONFIRMED DOCUMENTED / IMPLEMENTATION MIXED** | Architecture documents establish the renderer-downstream posture; current runtime implementation remains only partly evidenced. |
| Shared helper package | **README PRESENT / IMPLEMENTATION UNKNOWN** | `packages/maplibre/README.md` exists as a proposed bounded helper-package contract. |
| Runtime package | **NOT FOUND AT NAMED PATH** | `packages/maplibre-runtime/README.md` was absent at the current probe. |
| Explorer Web map runtime | **DOCUMENTED / RUNTIME NEEDS VERIFICATION** | The app-local map-runtime README exists and keeps the renderer behind a trust-preserving seam. |
| Sole-renderer decision | **PROPOSED ADR** | ADR-0007 is present with status `PROPOSED`; this README does not promote it. |
| Single-importer boundary | **PROPOSED ADR** | ADR-0006 documents a `MapLibreAdapter` seam; enforcement remains to be verified. |
| MapLibre policy home | **NOT FOUND AT NAMED README** | `policy/maplibre/README.md` was absent at the named probe. |
| Governed MapLibre schema family | **NOT FOUND AT NAMED README** | `schemas/contracts/v1/maplibre/README.md` was absent at the named probe. |
| Legacy performance schema | **CONFIRMED PERMISSIVE SCAFFOLD** | `schemas/maplibre/perf-envelope.schema.json` accepts any object because `additionalProperties` is true and no fields are required. |
| Performance workflow | **CONFIRMED PRESENT / PATH-CONFLICTED** | The workflow exists but watches singular `config/maplibre/**`, not this plural lane, and expects a missing payload. |
| Release or publication authority | **NONE** | A config file cannot approve a style, layer, tile, plugin, release, or public exposure. |

A canonical config location grants placement responsibility. It does not establish field semantics, consumer behavior, policy, release, or renderer authority.

[Back to top](#top)

---

## Current repository state

### Bounded snapshot

Direct repository inspection at base commit `b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8` supports this lane snapshot:

```text
configs/
├── README.md                              # canonical safe-config root contract
├── examples/
│   └── README.md                          # commit-safe examples boundary v0.2
└── maplibre/
    └── README.md                          # this file; v0.1 before revision
```

A path-scoped repository search returned `configs/maplibre/README.md` and no additional file in the lane.

Exact probes returned `Not Found` for:

```text
configs/maplibre/viewer.example.yaml
configs/maplibre/style.example.json
configs/maplibre/layers.example.yaml
configs/maplibre/validation.md
```

These are bounded findings. They do not prove the absolute absence of every differently named, ignored, generated, branch-only, or unindexed file.

### Adjacent MapLibre surfaces

The following repository surfaces were directly inspected:

```text
docs/architecture/maplibre.md
docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
docs/quality/maplibre-perf-governance.md
apps/explorer-web/src/features/map_runtime/README.md
packages/maplibre/README.md
.github/workflows/maplibre-perf-governance.yml
tools/validators/maplibre/validate_perf_envelope.py
schemas/maplibre/perf-envelope.schema.json
scripts/maplibre-smoke-perf.mjs
```

Named probes returned `Not Found` for:

```text
packages/maplibre-runtime/README.md
policy/maplibre/README.md
schemas/contracts/v1/maplibre/README.md
config/maplibre/perf-envelope.v1.json
```

### Current maturity table

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| `configs/maplibre/README.md` | Existing v0.1 boundary before this revision | Documentation existed; no payload or consumer proof followed. |
| MapLibre config payloads | Not established in plural lane | No supported defaults, templates, style config, layer config, or performance envelope can be claimed here. |
| `configs/README.md` | v0.2 canonical config-root contract | Placement and non-secret posture are established; lane behavior is not. |
| `packages/maplibre/README.md` | Bounded helper-package README | A helper boundary is documented; package code and APIs remain unverified. |
| Explorer Web map-runtime README | Governed app-feature boundary | The intended consumer seam is documented; runtime loading remains unverified. |
| Performance workflow | Executable YAML present | Its path contract conflicts with this lane and its required config payload is absent. |
| Performance validator | Python entry point present | It validates against a legacy permissive schema and requires a caller-supplied path. |
| Legacy perf schema | Open object | It does not provide meaningful field enforcement. |
| Perf smoke script | Node/Playwright script present | It expects the missing singular-path envelope and performs external network loads. |
| MapLibre policy bundle | Not found at named README path | No MapLibre-specific policy authority is established through that path. |
| Governed MapLibre schema README | Not found at named path | Final schema family and contents remain unresolved. |
| CI coverage for this README lane | Not established | The MapLibre perf workflow does not watch `configs/maplibre/**`. |
| Deployment use | Unknown | No production, staging, local, test, or review binding is proven. |

There is no supported quickstart for this lane because there is no verified config payload, loader, accepted schema, precedence contract, or consumer invocation.

[Back to top](#top)

---

## Repository fit

Directory Rules assign one primary responsibility to each root. `configs/maplibre/` must remain subordinate to the map, app, schema, policy, data, release, test, runtime, and infrastructure roots that own behavior and authority.

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Safe defaults and templates | `configs/maplibre/` | This lane after a consumer and validator are verified. |
| Deployable Explorer Web behavior | `apps/explorer-web/` | Consumer implementation; config cannot replace app code. |
| App-local map-runtime composition | `apps/explorer-web/src/features/map_runtime/` | Proposed consumer seam; config must not bypass it. |
| Shared MapLibre adapter/helpers | `packages/maplibre/` | Reusable implementation; config supplies bounded inputs only. |
| Runtime adapters or harnesses | Accepted `runtime/` or package/app surface | Runtime behavior does not belong under config. |
| Map architecture and renderer doctrine | `docs/architecture/`, accepted ADRs | Defines boundaries; config references rather than restates authority. |
| Semantic configuration contracts | `contracts/` | Owns field meaning where a stable object family exists. |
| Machine configuration schemas | `schemas/contracts/v1/` after accepted placement | Owns shape and version rules. |
| Renderer, layer, access, sensitivity, rights, plugin, and release policy | `policy/` | Config carries refs or safe defaults; it does not decide. |
| Layer/style/tile/source registries | Governed registry and catalog roots | Config must not become a registry. |
| Lifecycle artifacts | `data/` through governed transitions | Config is not RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Generated trust evidence is not config. |
| Release, correction, supersession, withdrawal, rollback | `release/` | Config cannot authorize release or record rollback state. |
| Test-local fixtures | `tests/fixtures/` under accepted lanes | Deterministic test carriers; not config defaults. |
| Cross-cutting reusable fixtures | `fixtures/` | Shared synthetic corpora; not config. |
| Generated QA/build output | `artifacts/` | Reports and temporary outputs; not trusted config or release state. |
| Deployment secrets and exposure controls | External secret manager and `infra/` | Never commit real secret material here. |

### Configuration is not a release artifact

A MapLibre style JSON, source list, layer definition, tile endpoint, sprite URL, glyph URL, camera preset, or plugin list can materially affect what users see. When such a file is itself a released public artifact, its authoritative copy and release state belong in the governed artifact/release lifecycle, not in `configs/` merely because the file is parseable configuration.

`configs/maplibre/` may contain safe defaults, templates, or references. It must not become the authoritative public style, manifest, tile index, plugin admission record, or release declaration.

[Back to top](#top)

---

## `config/` versus `configs/` path conflict

### Confirmed conflict

The canonical root documented by Directory Rules and `configs/README.md` is:

```text
configs/
```

The existing MapLibre performance workflow and scripts instead refer to:

```text
config/maplibre/perf-envelope.v1.json
```

The inspected workflow also uses these path filters:

```text
apps/web/**
schemas/maplibre/**
config/maplibre/**
tests/fixtures/maplibre/**
```

Current repository documentation instead identifies or proposes:

```text
apps/explorer-web/
schemas/contracts/v1/maplibre/
configs/maplibre/
```

### Why this matters

The mismatch creates several failure modes:

- a valid change under `configs/maplibre/**` may not trigger the MapLibre performance workflow;
- a maintainer may create a second, singular config root to satisfy a script;
- scripts and validators may read a path that does not exist;
- two copies of the same performance envelope may drift;
- schema validation may target a compatibility schema rather than the accepted schema family;
- documentation may claim canonical placement while executable tooling uses another path;
- rollback may restore one copy while a consumer reads the other;
- branch protection may report a green unrelated workflow while the changed config was never evaluated.

### Current safe posture

Until a migration is reviewed:

- do not create a duplicate payload under both `config/maplibre/` and `configs/maplibre/`;
- do not add symlink, copy, fallback search, or silent alias behavior merely to make the workflow pass;
- do not state that `configs/maplibre/` is consumed;
- do not state that `config/maplibre/` is accepted or canonical;
- keep the path conflict visible in documentation and review;
- require a migration plan that updates consumers, validators, workflows, tests, docs, and rollback together.

### Migration decision requirements

A path decision should identify:

- canonical target;
- all readers and writers;
- schema path;
- workflow path filters;
- package/app consumers;
- precedence and fallback behavior during migration;
- deprecation period, if any;
- compatibility tests;
- rollback commit and file targets;
- drift-register or ADR need;
- owner and reviewer assignments.

This README does not make that decision.

[Back to top](#top)

---

## What belongs here

This lane may contain only commit-safe MapLibre configuration defaults, templates, and tightly coupled documentation for a verified consumer.

| Accepted material | Purpose | Required posture |
|---|---|---|
| `README.md` | Lane contract, inventory, drift, validation, and review guidance | Truth-labeled and current. |
| Safe default YAML/TOML/JSON | Non-sensitive defaults for a named consumer | Consumer, version, precedence, schema, and rollback identified. |
| Template files | Illustrate required fields with placeholders | No live binding, no secrets, no private endpoints. |
| Local/dev/test config | Bound to an explicitly non-production consumer | Environment and override rules explicit; safe to commit. |
| Performance threshold declaration | Defines reviewable limits for a named smoke/perf harness | Path and schema authority accepted; values bounded; release authority separate. |
| Camera or accessibility defaults | Initial view, reduced motion, keyboard, or non-map fallback preferences | Must not hide denial, evidence, or sensitive state. |
| Cache/resource defaults | Bounded cache, concurrency, memory, or timeout values | Resource ceilings and failure behavior documented. |
| Diagnostics defaults | Logging level, debug overlays, safe health probes | Disabled or conservative by default; no sensitive payload logging. |
| Style/layer reference templates | References IDs, manifests, or released artifact handles | No inline authority; release and policy refs required where material. |
| Endpoint placeholders | Demonstrate endpoint slots for a named consumer | Public-safe placeholders; runtime authorization remains external. |
| Migration notes | Explain field/path compatibility during a bounded transition | Time-bounded, test-backed, reversible, owner assigned. |
| Validation notes | Explain verified commands and expected outcomes | Commands observed or labeled `PROPOSED`. |

Every non-trivial payload should be understandable without relying on tribal knowledge or hidden loader behavior.

[Back to top](#top)

---

## What does not belong here

| Prohibited material | Why prohibited | Correct home or action |
|---|---|---|
| Real tokens, keys, passwords, cookies, signed URLs, credentials, private endpoints | Repository is not a secret store. | External secret manager / deployment system; rotate and follow incident response if committed. |
| Production- or operator-specific live values | Creates accidental deployment binding. | Governed deployment controls outside this lane. |
| Authoritative public style JSON | A released style is a governed artifact with integrity and rollback state. | Published artifact and `release/` surfaces. |
| Layer or source registry | Configuration cannot activate or register layers/sources. | Governed registry/catalog roots. |
| Tile, PMTiles, COG, MVT, MLT, raster, terrain, sprite, glyph, or 3D asset payloads | These are artifacts/data, not config defaults. | Governed data/artifact/release homes. |
| `LayerManifest`, `StyleManifest`, `MapReleaseManifest`, plugin admission decision | Trust-bearing objects cannot live as convenient config. | Contracts/schemas for shape; lifecycle/release/policy homes for instances. |
| SourceDescriptor or source authority record | Map config cannot establish source identity or admissibility. | Source registry/control-plane surfaces. |
| Policy rules or allow/deny decisions | Config cannot authorize exposure or plugins. | `policy/`. |
| Machine schemas | Config cannot define its own shape authority. | Accepted `schemas/contracts/v1/` home. |
| Semantic contracts | Config cannot define stable object meaning. | `contracts/`. |
| App or renderer code | Config lane is not implementation. | `apps/` or `packages/`. |
| Runtime adapters, protocols, loaders, service definitions | Config lane cannot become runtime authority. | Accepted package/runtime/app homes. |
| Deployment/network/access-control definitions | Config defaults cannot own operational exposure. | `infra/` and external deployment systems. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | Lifecycle data must remain phase-visible. | `data/` lifecycle roots. |
| Receipts, proofs, validation reports, attestations | Trust evidence must remain separately auditable. | `data/receipts/`, `data/proofs/`, or governed QA lanes. |
| Promotion decisions, correction notices, rollback cards | Config cannot approve or record release. | `release/`. |
| Render screenshots, diff images, performance results | Generated QA output is not config. | `artifacts/` or governed evidence/proof homes. |
| Test fixture corpora | Config defaults are not valid/invalid test authorities. | `fixtures/` or `tests/fixtures/`. |
| Sensitive geometry or protected-location examples | Style/config redaction is not sufficient protection. | Transform upstream; use synthetic/public-safe fixtures. |
| AI-generated guessed defaults | Fluency is not evidence of a safe or supported value. | Verify against consumer, contracts, policy, tests, and release posture. |

[Back to top](#top)

---

## Configuration classes

A file should declare which class it belongs to. Do not infer class from extension alone.

| Class | Meaning | May be auto-loaded? | Production authority |
|---|---|---:|---:|
| `default` | Conservative values used when the consumer receives no explicit override | Only after loader and precedence are verified | No |
| `template` | Placeholder-bearing starting point copied or rendered outside the repository | No | No |
| `example` | Teaching artifact for a named consumer | No | No |
| `local` | Safe local-development values | Only by explicit local profile | No |
| `test` | Deterministic config for a test harness | Only by explicit test invocation | No |
| `review` | Bounded values for PR preview or review app | Only by explicit review environment | No |
| `threshold` | Declared validation or performance limits | Only by named validator/harness | No; validation does not publish |
| `compatibility-alias` | Temporary old-to-new path or field mapping | Only during reviewed migration | No |
| `released-reference` | References released artifact IDs/hashes without containing the artifact | Only through governed consumer | No; refs do not grant release |
| `deployment-template` | Safe shape with placeholders for deployment binding | No direct deployment | No |

A file that cannot be classified should fail review until its responsibility is clear.

### No hidden promotion

Changing a class from `example` or `test` to `default`, or from `default` to a live deployment input, is a behavior change. It requires consumer, test, security, policy, release, and rollback review appropriate to the consequences.

[Back to top](#top)

---

## Consumer-binding contract

No config should be accepted into this lane merely because it looks reasonable. It must bind to a verified or explicitly proposed consumer surface.

### Proposed metadata fields

A future config or adjacent metadata record should make these values inspectable:

```yaml
config_id: "kfm://config/maplibre/<name>"
config_version: "0.1.0"
config_class: "default | template | example | local | test | review | threshold"
status: "proposed | active | deprecated | retired"
consumer:
  path: "apps/explorer-web/... or packages/maplibre/..."
  interface: "accepted loader or option object"
  version: "consumer version or commit"
schema_ref: "kfm://schema/..."
contract_ref: "kfm://contract/..."
policy_refs: []
release_refs: []
environment: "local | dev | test | review | production-template"
network_posture: "deny | allowlist | governed-runtime"
precedence_rank: 0
override_sources: []
owner: "OWNER_TBD"
reviewers: []
last_reviewed: "YYYY-MM-DD"
deprecated_after: null
replacement_ref: null
rollback_ref: null
```

This shape is `PROPOSED`. It is not a current schema and must not be copied into production until contract and schema review accepts it.

### Minimum binding evidence

A config should not be called “used,” “active,” or “supported” without:

- a consumer file or package manifest that names the config path or accepted config ID;
- a loader or invocation that deterministically reads it;
- a documented precedence order;
- a parser and schema validator;
- tests for missing, malformed, denied, stale, and override cases;
- CI or release evidence that exercises the consumer path;
- a rollback target;
- owner and review assignment.

### Binding by convention is forbidden

These do not prove a binding:

- directory proximity;
- matching filenames;
- a README link;
- a workflow path filter;
- an environment variable with a similar name;
- a script constant pointing to a missing path;
- a passing unrelated workflow;
- an AI-generated explanation;
- a developer's memory.

[Back to top](#top)

---

## Precedence, overrides, and environments

Configuration ambiguity is operational risk. A consumer must define one deterministic precedence model.

A proposed precedence may look like:

```text
compiled safe fallback
  < repository default
  < explicit environment profile
  < deployment binding
  < command/request override allowed by policy
```

This ordering is illustrative, not repository fact.

### Required rules

A mature consumer should document:

- all allowed config sources;
- exact merge order;
- whether merges are shallow, deep, field-specific, or forbidden;
- which fields are immutable;
- which fields may be overridden only in local/test environments;
- whether unknown fields fail or are ignored;
- whether null deletes, resets, or is invalid;
- environment-variable substitution behavior;
- path resolution rules;
- duplicate-key behavior;
- version compatibility;
- deprecation warnings;
- rollback behavior.

### Fail-closed defaults

For trust-significant fields, missing or conflicting values should not silently choose the most permissive option.

Examples include:

- public layer visibility;
- endpoint authorization;
- plugin enablement;
- external network access;
- source/layer release state;
- sensitive-geometry behavior;
- evidence or citation controls;
- telemetry payload detail;
- debug panels exposing internal values;
- unsigned or hash-mismatched artifacts.

### Environment separation

Local, test, review, staging, and production-template values must not be collapsed into one ambiguous file. Environment differences should be explicit, minimal, and reviewable.

[Back to top](#top)

---

## Secrets, endpoints, and network posture

### Secret prohibition

Never commit:

- API keys;
- OAuth tokens;
- passwords;
- cookies;
- private keys;
- client secrets;
- signed URLs;
- presigned object-store URLs;
- private tile-service credentials;
- internal-only hostnames;
- VPN-only endpoints;
- operator usernames or home paths;
- production database or object-store handles;
- restricted source identifiers;
- sensitive query parameters.

Use references-by-name or obvious placeholders when a template must demonstrate a binding.

### Endpoint rules

A committed endpoint or endpoint template must state:

- whether it is mock, local, public, review-only, or governed-runtime;
- who owns it;
- whether credentials are required;
- whether it may receive location, identity, or evidence context;
- expected transport and certificate posture;
- timeout, retry, and circuit-breaker behavior;
- allowed response content;
- attribution and rights obligations;
- whether the endpoint can redirect;
- which policy or allowlist controls runtime access.

Config presence does not allow a runtime to fetch an endpoint.

### Current performance-script network finding

The inspected performance smoke script embeds public external URLs for:

- MapLibre CSS and JavaScript from `unpkg.com`;
- glyphs from `demotiles.maplibre.org`.

The script also uses a local HTTP fixture server.

Therefore:

- current performance execution is not proven hermetic or no-network;
- supply-chain pinning, content integrity, redirect handling, offline fallback, and endpoint admission remain unresolved;
- the script's URLs must not be adopted as general MapLibre defaults by copying them into this lane;
- a future test config must state whether external access is forbidden, mocked, vendored, or explicitly admitted.

### Logging and telemetry

Config parsers and consumers must not log:

- secrets or substituted secret values;
- signed URLs;
- full private endpoints;
- raw feature properties;
- exact sensitive coordinates;
- EvidenceBundle payloads;
- living-person or genomic data;
- protected infrastructure details;
- private filesystem paths.

Log stable IDs, reason codes, config versions, hashes, and redacted diagnostics instead.

[Back to top](#top)

---

## Map trust, release, and sensitive-geometry boundaries

MapLibre is downstream of KFM's trust membrane.

A config file must not let a consumer:

- read RAW, WORK, QUARANTINE, unpublished candidate, canonical/internal, graph, vector-index, or object-store paths directly;
- add an unverified source because a URL is present;
- render an unreleased layer because a toggle is true;
- replace policy with a visibility flag;
- hide a policy denial through opacity or style filtering;
- infer source authority from layer order, color, prominence, or label;
- claim evidence closure from popup properties;
- bypass governed API envelopes;
- substitute a map click for a verified claim;
- publish a style, layer, tile, plugin, or scene by configuration merge;
- override correction, supersession, withdrawal, stale, degraded, or rollback state.

### Released-artifact references only

Normal public consumers should receive released, integrity-bound references such as:

- layer manifest reference;
- style manifest reference;
- tile artifact manifest reference;
- map release manifest reference;
- artifact digest or spec hash;
- correction/supersession/rollback reference;
- EvidenceRef or governed resolution handle;
- policy decision reference.

A config may point to those handles. It may not fabricate or approve them.

### Sensitive geometry

Generalization, aggregation, jitter, omission, temporal delay, or denial must occur in governed upstream transformation and release flows. A MapLibre config or style filter is not an acceptable geoprivacy control because the underlying geometry may remain downloadable, queryable, inspectable, cached, or inferable.

### Negative states must remain visible

Consumers must preserve explicit states such as:

```text
UNAVAILABLE
UNRELEASED
STALE
DEGRADED
DENIED
RESTRICTED
ABSTAINED
CONFLICT
INVALID_CONFIG
INVALID_MANIFEST
UNVERIFIED_ARTIFACT
ROLLBACK_MISMATCH
ERROR
```

Exact accepted vocabularies remain subject to contract review. The invariant is that unsafe or unresolved state is not silently rendered as success.

[Back to top](#top)

---

## Styles, layers, tiles, sprites, and glyphs

### Style configuration

A safe style config may define or reference:

- initial basemap preference;
- approved style ID or manifest ref;
- safe color-scheme preference;
- reduced-motion preference;
- label-density preference within accepted bounds;
- debug style only in explicit non-production profiles;
- legend reference;
- attribution requirement;
- style version and compatibility range.

It must not:

- become the authoritative released style artifact;
- omit required attribution;
- inline restricted endpoints or credentials;
- suppress policy, evidence, stale, correction, or rollback indicators;
- implement sensitivity through client-side filtering alone;
- change semantic truth by color or order without documented meaning;
- load unsigned or hash-mismatched style assets.

### Layer configuration

A layer toggle or default visibility file may express preference only after the layer is admitted and released.

It must preserve:

- layer ID;
- manifest/release refs;
- source role;
- time scope;
- scale/zoom scope;
- evidence and citation handles;
- sensitivity transform state;
- correction and rollback state;
- unavailable/denied behavior.

A `visible: true` default is not a publication decision.

### Tile and raster references

Config may carry a template or released reference for:

- vector tiles;
- raster tiles;
- PMTiles;
- COGs;
- DEM/terrain;
- MLT;
- OGC API Tiles;
- test fixture tiles.

The consumer must verify the relevant manifest, digest, tiling scheme, bounds, zoom limits, format, attribution, release state, and policy before binding the source.

### Sprites and glyphs

Sprite and glyph URLs can create supply-chain, availability, attribution, privacy, and cross-origin risks. A mature config should pin or reference approved assets rather than relying on mutable public URLs.

### Camera and viewport defaults

Viewport defaults should be bounded and public-safe:

- center;
- zoom;
- pitch;
- bearing;
- min/max zoom;
- min/max pitch;
- bounds;
- projection;
- animation duration;
- reduced-motion behavior.

They must not expose precise protected locations, override a denied layer's extent, or create a misleading geographic emphasis without review.

[Back to top](#top)

---

## Plugins, protocols, and renderer capabilities

Config may express a **preference** or reference for an accepted capability. It cannot admit a plugin or protocol.

Examples include:

- PMTiles protocol;
- COG protocol;
- vector-text protocols;
- 3D Tiles;
- glTF;
- LiDAR/point-cloud support;
- deck.gl interop;
- terrain;
- globe;
- custom WebGL layers.

Before enablement, a governed path should verify:

- accepted renderer decision;
- plugin/protocol identity;
- exact version and integrity;
- license and rights;
- supply-chain attestation;
- maintenance status;
- browser compatibility;
- resource limits;
- data formats;
- schema/manifest representation;
- sensitivity and release implications;
- fallback/negative state;
- rollback and disable path.

A boolean such as `enable_3d_tiles: true` cannot replace plugin admission.

### Renderer-boundary compatibility

ADR-0006 proposes that only the MapLibre adapter imports MapLibre runtime packages. Config should bind to a KFM-shaped adapter interface, not leak raw `maplibre-gl` objects or events to arbitrary consumers.

ADR-0007 proposes MapLibre GL JS as the sole browser-side renderer. Because its status is `PROPOSED`, this README records the dependency but does not claim acceptance.

[Back to top](#top)

---

## MapLibre performance configuration drift

### Current observed workflow

`.github/workflows/maplibre-perf-governance.yml` is an executable workflow file with Node, Python, Playwright, validators, report builders, attestations, release-manifest builders, proof-pack builders, artifact uploads, and failure handling.

Its current MapLibre config contract is:

```text
config/maplibre/perf-envelope.v1.json
```

The workflow and smoke script both reference that path.

### Missing payload

The expected file returned `Not Found` at the pinned base.

Consequences:

- the workflow cannot validate or read the declared envelope unless another step creates it;
- no active threshold values are established by the inspected repository;
- no performance baseline or release eligibility can be inferred;
- workflow presence is not proof of successful execution;
- copying a proposed example from documentation would not create authority.

### Trigger mismatch

The workflow watches:

```text
config/maplibre/**
```

It does not watch:

```text
configs/maplibre/**
```

Therefore a change to the canonical-root lane may not trigger the specific MapLibre performance workflow.

### App-path mismatch

The workflow watches:

```text
apps/web/**
```

The inspected application documentation uses:

```text
apps/explorer-web/**
```

Whether `apps/web/` is a compatibility root, stale path, active app, or parallel shell remains `NEEDS VERIFICATION`.

### Schema mismatch

The validator reads:

```text
schemas/maplibre/perf-envelope.schema.json
```

The inspected schema is:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true
}
```

This validates only that the input is an object. It does not require:

- object type;
- schema version;
- envelope ID/version;
- scenarios;
- metrics;
- thresholds;
- units;
- browser/runtime version;
- viewport;
- device profile;
- network posture;
- evidence refs;
- owner;
- review state;
- release state;
- lifecycle;
- rollback.

MapLibre architecture documents instead propose a governed schema family under `schemas/contracts/v1/maplibre/`, whose named README was not found. Final schema placement and content remain conflicted.

### Trust-artifact output mismatch

The workflow writes and uploads material under:

```text
artifacts/perf/
```

The performance-governance document warns that trust-bearing receipts, proofs, and release manifests belong under their canonical `data/receipts/`, `data/proofs/`, and `release/` homes rather than being treated as authoritative merely because they were built in `artifacts/`.

A workflow artifact upload may be a convenient transport or QA output. It is not automatically canonical evidence or release state.

### Current safe conclusion

The MapLibre performance lane contains substantive-looking workflow and script scaffolding, but the inspected path, payload, schema, trigger, network, and trust-artifact relationships are not coherent enough to claim an active governed performance configuration.

This README does not fix those executable surfaces. It records the required reconciliation.

[Back to top](#top)

---

## Formats, naming, and versioning

### Supported format posture

No payload format is currently established for this lane. Future files may use YAML, JSON, TOML, or another consumer-required format only when the parser and validation path are known.

| Format | Appropriate use | Guardrails |
|---|---|---|
| JSON | Strict machine-consumed config and threshold declarations | Valid JSON; no comments; schema version required. |
| YAML | Human-reviewed defaults/templates | Duplicate keys rejected; anchors/merges constrained; parser behavior pinned. |
| TOML | Tool/package defaults where consumer uses TOML | Consumer and version named; no implicit environment secrets. |
| `.env.example` | Variable names and obvious placeholders only | Prefer `configs/examples/`; never real values. |
| Markdown | Lane docs and verified validation instructions | Not machine configuration. |

### Proposed naming pattern

Names should communicate class and version, for example:

```text
<consumer>.<purpose>.defaults.v1.yaml
<consumer>.<purpose>.template.v1.yaml
<consumer>.<purpose>.example.v1.json
<consumer>.<purpose>.thresholds.v1.json
```

This is guidance, not accepted repository convention.

### Versioning

A mature config should distinguish:

- file format/schema version;
- semantic config version;
- consumer compatibility range;
- artifact/release version refs;
- upstream MapLibre/plugin version;
- environment profile;
- deprecation state.

A filename such as `v1` is insufficient unless the file also declares or resolves its version semantics.

### Deterministic identity

Where config affects reproducible tests, generated artifacts, or release candidates, the consumer should record a canonical digest or spec hash over the resolved config and its relevant refs. Hashing does not authorize the config; it enables drift detection and replay.

[Back to top](#top)

---

## Validation

Validation must be layered. Parsing alone is not enough.

### Validation matrix

| Layer | Required check | Failure posture |
|---|---|---|
| Path | File lives in the accepted config lane | Reject or migrate through review. |
| Classification | Config class is explicit | Reject ambiguous payload. |
| Syntax | Strict parser succeeds | `INVALID_CONFIG`. |
| Duplicate keys | Duplicate/ambiguous fields rejected | Fail closed. |
| Schema | Accepted versioned schema validates | Reject; permissive scaffold is insufficient. |
| Contract | Field meaning matches accepted contract | Reject semantic drift. |
| Consumer | Named consumer and interface exist | `UNBOUND_CONFIG`. |
| Version | Consumer/config/schema versions are compatible | `INCOMPATIBLE_CONFIG`. |
| Precedence | Merge and override behavior is deterministic | Reject ambiguous result. |
| Secrets | No real secret or private endpoint is present | Block and invoke incident process if leaked. |
| Network | Endpoint and external access posture is explicit | Deny unknown network access. |
| Policy | Config cannot override deny/restrict/abstain obligations | Preserve governed outcome. |
| Release | Referenced artifacts are released, current, and integrity-bound | Do not load unresolved artifact. |
| Evidence | Evidence/citation refs are preserved where required | Abstain or show unsupported state. |
| Sensitivity | No style-only geoprivacy or hidden precision | Deny or require upstream transform. |
| Resources | Cache, concurrency, size, timeout, and plugin limits bounded | Reject unsafe values. |
| Accessibility | Reduced motion, keyboard, focus, and non-map alternatives preserved | Block public-ready claim. |
| Observability | Logs are redacted and reason-coded | Reject unsafe diagnostics. |
| Determinism | Same resolved inputs produce same effective config | Fail replay proof. |
| Rollback | Prior version and replacement path are explicit | Block activation. |
| Trigger coverage | Relevant workflows watch the canonical path | Mark CI enforcement absent. |

### Validation result

A validator should return a finite, structured outcome such as:

```text
PASS
FAIL
ABSTAIN
DENY
ERROR
```

Exact contract names remain proposed. A `PASS` means the validator's checks passed. It does not authorize release, plugin admission, source activation, or publication.

### Effective-config receipt

A mature consumer may emit a non-authoritative audit record containing:

- config ID/version;
- config digest;
- source files and precedence;
- consumer version;
- schema version;
- allowed override sources;
- network posture;
- release/artifact refs;
- redacted warnings;
- finite result;
- timestamp;
- rollback ref.

Placement and trust class for such a record require contract, data, and release review. It must not be invented as a local config sidecar.

[Back to top](#top)

---

## Required negative cases

Before a MapLibre config is treated as supported, tests should cover at least:

| Case | Expected safe outcome |
|---|---|
| Missing config | Conservative fallback or explicit error; never permissive public load. |
| Malformed JSON/YAML/TOML | `INVALID_CONFIG`. |
| Duplicate YAML keys | Reject. |
| Unknown field | Reject unless schema explicitly permits extension. |
| Unsupported schema version | `INCOMPATIBLE_CONFIG`. |
| Config/consumer version mismatch | Reject or explicit migration path. |
| Two conflicting config sources | Deterministic conflict/error. |
| Real secret detected | Block, redact, rotate, incident response. |
| Private/signed endpoint committed | Block review. |
| Redirect to unapproved host | Deny. |
| External network unavailable | Deterministic offline/negative state. |
| Unreleased style/layer/tile ref | Do not bind. |
| Missing digest/spec hash | Do not treat artifact as verified. |
| Hash mismatch | Deny load; surface integrity error. |
| Withdrawn or rolled-back release | Remove/deny and surface state. |
| Stale config | Warn, abstain, or block according to contract. |
| Plugin enabled without admission | Deny. |
| Plugin version mismatch | Deny or degrade explicitly. |
| Style attempts sensitivity filtering | Reject; require upstream transform. |
| Config points to RAW/WORK/QUARANTINE | Deny. |
| Config points to canonical/internal store | Deny public consumer. |
| Debug mode in production profile | Deny or force disabled. |
| Excessive cache/concurrency/resource values | Reject bounded validation. |
| Missing attribution | Reject public-ready state. |
| Accessibility options disable required alternative | Block public-ready state. |
| Telemetry includes sensitive properties | Redact and fail test. |
| Workflow watches wrong config path | CI coverage marked failed/absent. |
| Validator uses permissive empty schema | Governance validation fails. |
| Required config payload absent | Workflow fails finitely; no release claim. |

[Back to top](#top)

---

## Tests, workflows, and CI

### Current state

The repository contains a MapLibre performance workflow and several scripts/validators, but no lane payload was verified under `configs/maplibre/`.

The workflow currently:

- does not watch `configs/maplibre/**`;
- watches singular `config/maplibre/**`;
- expects a missing `perf-envelope.v1.json`;
- uses `schemas/maplibre/` rather than an accepted `schemas/contracts/v1/maplibre/` family;
- watches `apps/web/**` rather than the documented `apps/explorer-web/**` path;
- uses external network resources in the smoke script;
- writes QA/trust-shaped output under `artifacts/perf/`.

This is implementation evidence of drift, not evidence that the requested lane is validated.

### Required test layers

A mature configuration surface should have:

1. **Parser tests** — valid and invalid syntax, duplicate keys, numeric bounds.
2. **Schema tests** — required fields, versions, enums, closed objects, extension rules.
3. **Consumer tests** — loader reads the expected path or config ID.
4. **Precedence tests** — defaults, profiles, deployment bindings, and overrides resolve deterministically.
5. **Security tests** — secret, private endpoint, redirect, and log-redaction cases.
6. **Network tests** — deny-by-default/offline behavior and allowlist enforcement.
7. **Map-boundary tests** — no RAW/canonical/internal URLs; no direct unverified `addSource`.
8. **Release tests** — unreleased, stale, corrected, withdrawn, superseded, and rolled-back refs.
9. **Sensitivity tests** — no style-filter geoprivacy; transformed artifacts only.
10. **Plugin tests** — unknown/unadmitted/version-mismatched plugins fail closed.
11. **Performance tests** — thresholds, units, scenarios, browser/runtime pins, deterministic metrics.
12. **Accessibility tests** — reduced motion, keyboard, focus, non-map alternative.
13. **Migration tests** — old path/field compatibility and deprecation.
14. **Workflow-trigger tests** — canonical path changes run the required checks.
15. **Root trust-spine tests** — public clients remain on governed released interfaces.

### CI claims

Do not claim that a config is “CI validated” unless:

- the relevant workflow watches its canonical path;
- the job actually runs the parser/schema/consumer/security checks;
- the required payload exists;
- the workflow result is inspected;
- generated evidence is distinguished from release authority;
- branch protection or promotion gates actually require the check where material.

A green workflow that did not trigger on the changed path is not validation.

[Back to top](#top)

---

## Review burden

Review depends on consequence, not file size.

| Change | Minimum review |
|---|---|
| README wording only | Config steward or Docs steward. |
| New example/template with no consumer | Config + security review; must remain non-active. |
| Default used by local/test consumer | Consumer owner + config + test review. |
| Endpoint or network posture | Security + consumer + policy review. |
| Public layer/style default | Map + UI + policy + release review. |
| Plugin/protocol configuration | MapLibre adapter + security/supply-chain + policy review. |
| Sensitive-geometry-related config | Sensitivity/domain steward; likely upstream transformation review. |
| Performance threshold change | Map/performance + validation + release-gate review. |
| Config path migration | Config + all consumer owners + CI + docs; ADR/migration review if compatibility/authority changes. |
| Schema/contract change | Schema + contract owners; config README update is insufficient. |
| Production binding | Ops/infra/security and consumer owner; real values remain outside this lane. |

### Separation of duties

For high-impact public behavior:

- the config author should not unilaterally approve release;
- performance threshold authors should not be the sole release authority;
- plugin admission should remain separate from config enablement;
- sensitive-data transformation review should remain separate from style authorship;
- correction and rollback approval should remain independently reviewable.

[Back to top](#top)

---

## Safe change pattern

For any future file under `configs/maplibre/`:

1. **Identify the consumer.**
   - Confirm current app/package/tool path.
   - Confirm the loader/interface and version.

2. **Classify the file.**
   - Default, template, example, local, test, review, threshold, or compatibility alias.

3. **Confirm placement.**
   - Check Directory Rules.
   - Confirm it is configuration rather than schema, policy, artifact, registry, runtime, or release state.

4. **Resolve path drift first.**
   - Do not create parallel `config/` and `configs/` payloads.
   - Inventory every reader, writer, workflow, script, validator, and doc.

5. **Bind meaning and shape.**
   - Reference accepted contract and schema.
   - Do not rely on permissive empty schemas.

6. **Set security posture.**
   - Remove secrets/private endpoints.
   - Define network and logging behavior.

7. **Set trust posture.**
   - Require released artifact refs.
   - Preserve policy, evidence, correction, rollback, and sensitive-geometry state.

8. **Define precedence and overrides.**
   - Make merge order and immutable fields explicit.

9. **Add negative-first tests.**
   - Missing, malformed, denied, stale, unreleased, secret, network, plugin, rollback, and path-trigger cases.

10. **Update CI.**
    - Ensure the canonical path triggers the substantive checks.

11. **Document migration and rollback.**
    - Record prior path/version, deprecation period, and restore target.

12. **Review the effective diff.**
    - Confirm no generated artifacts, secrets, source data, release objects, or authority drift entered the lane.

[Back to top](#top)

---

## Smallest safe implementation sequence

This sequence is `PROPOSED`. It does not authorize implementation without review.

### Phase 0 — reconcile authority and paths

1. Inventory `config/` and `configs/` recursively.
2. Identify every `config/maplibre` and `configs/maplibre` reference.
3. Decide the canonical performance-envelope home.
4. Decide the accepted MapLibre schema family.
5. Decide whether `packages/maplibre/` is the active adapter/runtime home.
6. Record drift and migration/ADR needs.
7. Assign owners.

### Phase 1 — accept a config contract

1. Define semantic config object meaning under `contracts/` if a stable object family is needed.
2. Define a closed, versioned schema under the accepted schema root.
3. Define config class, consumer binding, precedence, network, security, lifecycle refs, deprecation, and rollback fields.
4. Add valid and invalid synthetic fixtures.
5. Add parser/schema tests.

### Phase 2 — implement one bounded consumer

Choose one low-risk use case, such as a test-only performance threshold declaration.

1. Implement one deterministic loader in the accepted consumer.
2. Require explicit config path or config ID.
3. Fail on missing/invalid/unsupported values.
4. Record effective config hash in test output.
5. Keep the consumer no-publication and test/review-only.
6. Add negative tests.

### Phase 3 — migrate workflow paths

1. Update workflow filters to the canonical config path.
2. Update script and validator arguments.
3. Update app path filters to current repository roots.
4. Migrate schema refs.
5. Remove or deprecate singular compatibility refs through a reviewed plan.
6. Test both intended success and old-path failure.
7. Update docs and drift records.

### Phase 4 — make performance runs hermetic or explicitly admitted

1. Vendor, pin, mock, or govern external runtime assets.
2. Define browser/MapLibre/plugin versions.
3. Define fixture-server behavior.
4. Bound network access.
5. Verify attribution and licenses.
6. Emit deterministic, redacted results.

### Phase 5 — integrate trust and release gates

1. Keep QA outputs separate from canonical receipts/proofs/releases.
2. Bind config and result hashes to the appropriate run receipt.
3. Validate correction and rollback references.
4. Require independent promotion/release decision.
5. Add root trust-spine tests.

[Back to top](#top)

---

## Definition of done

A mature `configs/maplibre/` lane should satisfy all applicable items.

### Ownership and placement

- [ ] `configs/maplibre/` is accepted as the canonical lane.
- [ ] Singular `config/maplibre/` references are migrated, intentionally retained with bounded compatibility, or removed.
- [ ] No parallel active config payload exists.
- [ ] Owners and reviewers are assigned.
- [ ] Drift/ADR/migration records exist where required.

### Inventory

- [ ] Recursive lane inventory is verified.
- [ ] Every file has a config class.
- [ ] Every file names a consumer.
- [ ] Stale, orphaned, or duplicate files are removed or deprecated.
- [ ] Generated output and trust objects are absent.

### Contracts and schemas

- [ ] Stable config meaning is defined where needed.
- [ ] A closed, versioned schema validates each machine payload.
- [ ] Legacy permissive schemas are migrated or explicitly scoped.
- [ ] Unknown fields and unsupported versions fail deterministically.
- [ ] Valid/invalid fixtures exist in their correct homes.

### Consumer binding

- [ ] Loader path and interface are verified.
- [ ] Precedence and override behavior are explicit.
- [ ] Effective config is deterministic.
- [ ] Missing and conflicting config behavior is tested.
- [ ] Consumer/version compatibility is enforced.
- [ ] Config does not leak raw MapLibre objects across the accepted adapter boundary.

### Security

- [ ] No secrets or private endpoints are committed.
- [ ] Endpoint allowlist/network posture is explicit.
- [ ] Redirect and external-asset behavior is tested.
- [ ] Logs and telemetry are redacted.
- [ ] Resource ceilings are enforced.
- [ ] Supply-chain/version pins exist for plugins and external assets.

### Trust and release

- [ ] Public consumers use governed APIs and released artifact refs.
- [ ] Config cannot activate sources/layers or admit plugins.
- [ ] Config cannot override policy or sensitivity.
- [ ] Style-only geoprivacy is rejected.
- [ ] Evidence, citation, correction, supersession, withdrawal, and rollback refs remain visible.
- [ ] No direct RAW/WORK/QUARANTINE/canonical/internal paths are accepted.
- [ ] A config validation `PASS` is not treated as release approval.

### Tests and CI

- [ ] Parser, schema, consumer, precedence, security, network, trust, plugin, performance, accessibility, migration, and rollback tests exist as applicable.
- [ ] Canonical path changes trigger required workflows.
- [ ] Required payloads exist before the workflow starts.
- [ ] CI reports collection and substantive results.
- [ ] External network behavior is hermetic or explicitly governed.
- [ ] QA artifact uploads are not treated as canonical release state.

### Documentation and operations

- [ ] Parent and sibling README files agree.
- [ ] Supported commands are observed and documented.
- [ ] Migration and rollback are concrete.
- [ ] Deprecation dates and replacements are visible.
- [ ] Operational failure and recovery paths are documented.
- [ ] Last review dates are current.

Until these are verified, the lane remains README-only and implementation maturity remains unestablished.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| `configs/maplibre/README.md` prior blob `bdf6bc8deb4a1c6cefdb2631b9db3234624f9b7d` | **CONFIRMED** | Target existed as v0.1 config-boundary README. | Did not establish inventory or consumers. |
| Path-scoped repository search | **CONFIRMED BOUNDED RESULT** | Returned this README and no additional lane file. | Not an exhaustive recursive tree receipt. |
| Four exact candidate probes | **CONFIRMED NOT FOUND** | Suggested viewer/style/layer/validation files were absent at named paths. | Differently named files remain unknown. |
| `configs/README.md` v0.2 | **CONFIRMED** | `configs/` owns safe non-secret defaults/templates. | Does not prove MapLibre lane consumption. |
| `configs/examples/README.md` v0.2 | **CONFIRMED** | Establishes commit-safe example/secret/consumer-binding posture. | Example lane does not settle MapLibre defaults. |
| Directory Rules v1.4 | **CONFIRMED DOCTRINE** | `configs/` placement, trust roots, lifecycle, and anti-drift posture. | Does not resolve current singular-path references. |
| MapLibre architecture entry point | **CONFIRMED DOCUMENT** | Renderer-downstream, released-artifact, verify-before-add-source, sensitive-geometry, and renderer posture. | Several concrete enforcement paths remain proposed. |
| ADR-0006 | **CONFIRMED DOCUMENT / PROPOSED ADR** | Single MapLibre adapter import boundary. | Acceptance and enforcement remain unverified. |
| ADR-0007 | **CONFIRMED DOCUMENT / PROPOSED ADR** | Sole browser-renderer decision proposal. | Not accepted by this README. |
| Explorer Web map-runtime README | **CONFIRMED DOCUMENT** | App-local map seam and governed API boundary. | Runtime files and config loading remain unverified. |
| `packages/maplibre/README.md` | **CONFIRMED README** | Proposed helper/adapter package boundary. | Package implementation and active runtime role remain unknown. |
| `packages/maplibre-runtime/README.md` probe | **CONFIRMED NOT FOUND** | Earlier runtime-package refs cannot be treated as current repo fact. | Another runtime home may exist. |
| `.github/workflows/maplibre-perf-governance.yml` | **CONFIRMED EXECUTABLE YAML** | Current path filters, commands, artifacts, and permissions. | Does not prove successful runs or correct governance. |
| `config/maplibre/perf-envelope.v1.json` probe | **CONFIRMED NOT FOUND** | Required perf config payload is absent at named path. | Another branch/generated payload remains outside claim. |
| `tools/validators/maplibre/validate_perf_envelope.py` | **CONFIRMED** | Validator points to legacy `schemas/maplibre/` schema. | Does not prove schema adequacy or workflow success. |
| `schemas/maplibre/perf-envelope.schema.json` | **CONFIRMED PERMISSIVE SCAFFOLD** | Current legacy schema accepts any object. | Does not establish meaningful perf-envelope contract. |
| `schemas/contracts/v1/maplibre/README.md` probe | **CONFIRMED NOT FOUND** | Named governed schema-family README is absent. | Individual schemas or different docs may exist. |
| `policy/maplibre/README.md` probe | **CONFIRMED NOT FOUND** | Named MapLibre policy README is absent. | Other policy files or families may exist. |
| `scripts/maplibre-smoke-perf.mjs` | **CONFIRMED** | Missing envelope path, external asset URLs, local fixture server, and result paths. | No run was executed in this revision. |
| MapLibre performance governance doc | **CONFIRMED DOCUMENT / PROPOSED FLOW** | Identifies proposed perf config and canonical trust-artifact separation. | Runtime and exact paths remain mixed. |

### Evidence limits

This revision did not:

- recursively enumerate the Git tree;
- execute any config loader;
- run the performance workflow;
- inspect historical workflow runs or logs;
- validate a performance envelope;
- import MapLibre;
- launch Explorer Web;
- inspect all package files;
- inspect all schemas or policies;
- verify deployment;
- query a release registry;
- resolve EvidenceBundles;
- verify public map behavior.

Future file names, metadata shapes, contracts, validators, test cases, and migration phases are `PROPOSED` unless explicitly labeled otherwise.

[Back to top](#top)

---

## Open decisions and ADR triggers

| Decision | Current status | Trigger |
|---|---:|---|
| Canonical `config/` versus `configs/` path | **CONFLICTED** | Any new payload, loader, alias, symlink, or migration. |
| MapLibre performance-envelope home | **CONFLICTED / ABSENT** | Creating the missing envelope or changing workflow/script paths. |
| Perf-envelope contract and schema | **PERMISSIVE LEGACY SCAFFOLD / NEEDS DESIGN** | Adding required fields, closed shape, versions, or consumers. |
| Canonical MapLibre schema family | **NEEDS VERIFICATION** | Moving from `schemas/maplibre/` to `schemas/contracts/v1/maplibre/` or another accepted home. |
| Current app path in workflow | **CONFLICTED** | Changing `apps/web/**` to `apps/explorer-web/**` or retaining compatibility. |
| Active adapter/runtime package | **UNKNOWN** | Declaring `packages/maplibre/` or another path as the supported runtime seam. |
| Sole-renderer status | **PROPOSED ADR** | Acceptance, supersession, or exception path. |
| Plugin admission policy | **NOT ESTABLISHED AT NAMED PATH** | Enabling a plugin/protocol through config. |
| Config loader and precedence | **ABSENT / UNKNOWN** | Introducing auto-loading, profile merging, or overrides. |
| External network posture | **NOT HERMETIC / NEEDS VERIFICATION** | Running smoke/perf in protected CI or release gates. |
| Performance thresholds | **ABSENT** | Creating values that can block or permit candidate progression. |
| Trust-artifact output homes | **CONFLICTED** | Treating `artifacts/perf/` output as receipts, proofs, or release state. |
| Workflow trigger coverage | **INCOMPLETE FOR PLURAL LANE** | Claiming CI enforcement for `configs/maplibre/`. |
| Style/layer config versus released artifacts | **NEEDS VERIFICATION** | Adding style JSON, layer lists, endpoint lists, or public defaults. |
| Endpoint allowlist and secrets binding | **UNKNOWN** | Adding any non-local endpoint or credential reference. |
| Owner assignments | **OWNER_TBD** | Moving beyond documentation-only maturity. |

### ADR or migration discipline

An ADR or formal migration record is appropriate when a change:

- creates or changes a canonical path;
- changes schema authority;
- changes renderer strategy;
- creates a stable cross-package config contract;
- changes public map behavior;
- enables new plugin/protocol families;
- changes trust-artifact placement;
- changes config precedence across apps/environments;
- introduces compatibility aliases with material lifetime;
- bends the renderer, trust membrane, lifecycle, or publication invariants.

### No decision by convenience

Do not settle an open decision because:

- a workflow already spells one path;
- a documentation example proposes another;
- a file is missing and “needs to exist somewhere”;
- a script passes when run locally;
- a permissive schema returns success;
- a public demo endpoint is convenient;
- a config key seems harmless;
- a style hides sensitive features;
- an artifact upload exists;
- a UI needs to render something;
- an AI recommends a default.

[Back to top](#top)

---

## Rollback

This revision changes one Markdown file and no runtime behavior.

### Before merge

Close or abandon the review branch or pull request. No config payload, consumer, workflow, schema, policy, artifact, release, or deployment state is changed.

### After merge

Restore the prior README through a reviewed commit using:

```text
base commit: b6bcc4cd27dc8c0fa1f74aa5b989cb3240e90aa8
prior blob: bdf6bc8deb4a1c6cefdb2631b9db3234624f9b7d
```

or revert the commit that introduces this v0.2 revision.

### Rollback triggers

Correct or roll back this README if it:

- claims a config payload exists when it does not;
- claims a consumer binding without code or test evidence;
- declares singular or plural path authority without a reviewed decision;
- treats a permissive schema as substantive validation;
- states the MapLibre performance workflow validates this lane when it does not watch the path;
- treats `artifacts/perf/` as canonical proof or release state;
- authorizes public endpoints, styles, layers, plugins, or tiles;
- implies style filtering is sufficient sensitivity protection;
- documents unverified commands as supported;
- exposes secrets, private endpoints, or sensitive details;
- conflicts materially with accepted Directory Rules, ADRs, app/package boundaries, or release controls.

### Documentation rollback is not operational rollback

Reverting this README will not revert any later config payload, workflow, script, schema, package, app, policy, deployment, artifact, or release change. Every material implementation change requires its own rollback target.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Recursively inventory `configs/maplibre/`. | **NEEDS VERIFICATION** | Commit-pinned tree or mounted workspace. |
| Recursively inventory singular `config/maplibre/`. | **NEEDS VERIFICATION** | Commit-pinned tree and ignore/generated-file review. |
| Decide canonical config path. | **CONFLICTED** | Directory Rules review, consumer inventory, migration plan. |
| Identify all readers/writers. | **NEEDS VERIFICATION** | Code search, workflow search, runtime traces, tests. |
| Confirm active app path. | **NEEDS VERIFICATION** | App manifests, build scripts, routes, deployment evidence. |
| Confirm MapLibre adapter/runtime home. | **UNKNOWN** | Package inventory, imports, build/tests, ADR acceptance. |
| Define performance-envelope contract. | **PROPOSED / ABSENT** | Contract review and consumer requirements. |
| Replace permissive legacy schema. | **NEEDS VERIFICATION** | Accepted closed schema, fixtures, validator, migration. |
| Create or migrate performance envelope. | **ABSENT** | Reviewed canonical path, values, owners, tests. |
| Align workflow path filters. | **CONFLICTED** | Workflow patch and trigger tests. |
| Align validator schema path. | **CONFLICTED** | Schema-home decision and validator patch. |
| Verify workflow runs. | **UNKNOWN** | Actions runs, jobs, logs, artifacts, conclusions. |
| Verify no-network/hermetic posture. | **NOT ESTABLISHED** | Vendored/mocked assets, allowlist, offline tests. |
| Verify endpoint security and attribution. | **UNKNOWN** | Policy, licenses, pins, integrity, redirect tests. |
| Verify config secret scanning. | **NEEDS VERIFICATION** | Workflow/config and test evidence. |
| Define loader and precedence. | **ABSENT / UNKNOWN** | Consumer implementation and tests. |
| Define config identity/version/hash posture. | **PROPOSED** | Contract/schema and replay tests. |
| Define plugin/protocol config boundary. | **PROPOSED** | Accepted ADR, policy, contract, schema, package tests. |
| Define released style/layer reference behavior. | **NEEDS VERIFICATION** | Manifest contracts, governed API, release tests. |
| Verify sensitive-geometry safeguards. | **NEEDS VERIFICATION** | Upstream transform receipts and no-style-filter tests. |
| Reconcile QA artifacts with canonical receipts/proofs/releases. | **CONFLICTED** | Data/release owner decision and workflow changes. |
| Add canonical-path CI coverage. | **NOT ESTABLISHED** | Path filters, substantive jobs, branch-protection evidence. |
| Assign owners/CODEOWNERS. | **OWNER_TBD** | Reviewed repository ownership changes. |
| Keep docs aligned after migration. | **ONGOING** | Parent/sibling docs and link checks. |

---

## Maintainer checklist

- [ ] Keep `configs/maplibre/` limited to commit-safe configuration defaults/templates.
- [ ] Keep singular/plural path drift visible until resolved.
- [ ] Never create duplicate active payloads to satisfy stale readers.
- [ ] Name the consumer for every payload.
- [ ] Define class, version, schema, contract, precedence, owner, and rollback.
- [ ] Never commit real secrets, signed URLs, or private endpoints.
- [ ] Keep external network access denied, mocked, vendored, or explicitly governed.
- [ ] Keep MapLibre downstream of governed APIs and released artifacts.
- [ ] Keep raw renderer objects behind the accepted adapter seam.
- [ ] Keep config separate from schema, policy, registry, evidence, lifecycle, release, and artifact authority.
- [ ] Reject style-only geoprivacy.
- [ ] Preserve attribution, evidence, correction, supersession, withdrawal, and rollback refs.
- [ ] Test missing, malformed, denied, stale, unreleased, secret, network, plugin, and rollback cases.
- [ ] Ensure workflows watch the canonical path.
- [ ] Do not treat permissive schema success as meaningful validation.
- [ ] Do not treat performance `PASS` as release approval.
- [ ] Keep QA uploads distinct from canonical receipts/proofs/releases.
- [ ] Update this README when inventory, consumers, paths, schemas, or workflows change.
- [ ] Use ADR/migration discipline for material path, precedence, renderer, schema, or authority changes.

[Back to top](#top)
