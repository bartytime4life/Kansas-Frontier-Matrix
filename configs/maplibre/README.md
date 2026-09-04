<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-maplibre-readme
title: configs/maplibre/ — MapLibre Configuration, Drift, and Consumer-Binding Boundary
type: readme
version: v0.4
status: draft; current-main-repinned; bounded-config-lane; package-adapter-aware; runtime-HOLD; performance-HOLD; non-release; non-publication
owners: OWNER_TBD — Config steward · Map steward · MapLibre adapter steward · Explorer Web steward · Governed API steward · Security steward · Policy steward · Release steward · Validation steward · Test steward · Docs steward
created: 2026-06-16
updated: 2026-09-04
policy_label: public; configs; maplibre; commit-safe; non-secret; non-authoritative; consumer-bound; accepted-renderer-boundary; package-owned-dependency; runtime-HOLD; released-artifacts-only; no-direct-publication; drift-visible
current_path: configs/maplibre/README.md
truth_posture: CONFIRMED current-main configs/maplibre inventory, package-owned exact maplibre-gl 6.6.0 dependency and initial lifecycle/camera adapter with Vite worker seam, accepted ADR-0006 and ADR-0007 architecture decisions, retired legacy performance harness, current no-network static/negative workflow posture, and acquisition/readiness HOLD posture / CONFLICTED permissive performance schemas, retained legacy apps/web workflow guard, and trust-shaped candidate builders under artifacts/perf / PROPOSED or held loader/precedence/full config contract, broader renderer capability activation, and release-grade performance governance / UNKNOWN hosted workflow result for this revision, production renderer activation, source/layer/terrain/PMTiles/accessibility/long-session readiness, deployment/publication behavior, and owner assignments
evidence_snapshot:
  snapshot_role: exact_current_main_before_doc_pr
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ccc4f3a7518271fadb6461ded3258706dd5c7303
  tree: 358cc6036e7112be7688940b9e691c653baca569
  prior_blob: 40bb91dd6b810b70f50bdba07b58d78fcb125ad2
  payload_blob: 2833f99b5316df91e71c0f8913bb06d70917abcf
  package_manifest_blob: f6d450af19c33011e159e123c8a07ca2bca6dfd
  maplibre_architecture_blob: a3cc800aaa8f9c541ae363f3b0194aae4f91eec3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  perf_workflow_blob: 8e4c3b801fe6dbaac5e6645b054768859e84fa1e
  acquisition_inventory_blob: 2c6d2b709e2cf4a519b32c2274820008a18ad0f4
  readiness_validator_blob: 2e79257aa64890ff7e2fca4d8b793970baa27f89
  readiness_profile: kfm-maplibre-v6-6-readiness-v4
  acquisition_profile: kfm-maplibre-acquisition-inventory-v14
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
  - ../../docs/architecture/map-master/README.md
  - ../../docs/architecture/maplibre-master.md
  - ../../docs/architecture/map-shell.md
  - ../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../docs/architecture/ui/LAYERING.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/quality/maplibre-perf-governance.md
  - ../../docs/security/SECRETS.md
  - ../../apps/explorer-web/src/features/map_runtime/README.md
  - ../../apps/explorer-web/src/site/README.md
  - ../../packages/maplibre/README.md
  - ../../packages/maplibre/src/README.md
  - ../../packages/maplibre/package.json
  - ../../packages/maplibre/src/map-runtime-port.ts
  - ../../packages/maplibre/src/null-map-runtime.ts
  - ../../packages/maplibre/src/maplibre-adapter.ts
  - ../../packages/maplibre/src/maplibre-vite-adapter.ts
  - ../../apps/kansas-frontier-matrix-explorer/package.json
  - ../../apps/kansas-frontier-matrix-explorer/vite.config.ts
  - ../../tools/validators/maplibre/README.md
  - ../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../tools/validators/maplibre/assess_acquisition_inventory.py
  - ../../tools/validators/maplibre/validate_v6_readiness.py
  - ../../tests/maplibre/README.md
  - ../../tests/maplibre/test_legacy_perf_harness_retirement.py
  - ../../tests/maplibre/test_package_exports.py
  - ../../tests/maplibre/test_perf_governance_negative_paths.py
  - ../../schemas/maplibre/perf-envelope.schema.json
  - ../../release/
  - ../../data/published/
tags: [kfm, configs, maplibre, renderer, defaults, templates, consumer-binding, map-runtime, styles, layers, tiles, sprites, performance, security, secrets, validation, release, rollback, governance]
notes:
  - "Current main was re-pinned directly at ccc4f3a7518271fadb6461ded3258706dd5c7303 with tree 358cc6036e7112be7688940b9e691c653baca569; the target lane contains exactly this README and perf-envelope.v1.json at the inspected tree."
  - "The plural configs/maplibre/perf-envelope.v1.json path is the current bounded tooling path. The old v0.3 singular-path migration note is historical; this documentation update does not change workflow, scripts, payload, or schema files."
  - "The package-owned @kfm/maplibre seam declares exact maplibre-gl 6.6.0, owns the initial lifecycle/camera adapter and Vite worker binding, and exposes a renderer-neutral root. This is adjacent implementation evidence, not runtime readiness or release authority."
  - "Acquisition profile v14 records structural HOLD with raw renderer acquisition confined to packages/maplibre. Readiness profile v4 remains HOLD because the twelve runtime probes are absent or not run."
  - "The legacy CDN/global smoke harness is retired behind a finite WORKFLOW_HOLD. The current workflow is static/no-network and does not claim browser, performance, render-diff, attestation, proof, release, deployment, or publication evidence."
  - "schemas/maplibre/perf-envelope.schema.json remains an open object scaffold. Trust-shaped builders under artifacts/perf remain candidate outputs, not canonical receipts, proofs, release manifests, or publication state."
  - "Notion coordination and Drive manuals were consulted as read-only context. They do not override current GitHub implementation evidence and do not prove repository behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Configuration, Drift, and Consumer-Binding Boundary

> `configs/maplibre/` is the canonical-root sublane for commit-safe MapLibre defaults and templates. At current `main`, it contains this README and one performance-envelope payload. That payload is a bounded input to named tooling; it is not a live viewer configuration, style manifest, layer registry, endpoint allowlist, policy decision, release manifest, or runtime authority.

**Document lifecycle:** `draft v0.4`
**Observed lane maturity:** `CONFIRMED` two-file config lane; package-owned exact renderer dependency and initial adapter/Vite seam implemented elsewhere; runtime and performance activation `HOLD`
**Owning responsibility root:** `configs/` — safe, non-secret configuration defaults and templates  
**Authority:** configuration-boundary documentation only; no truth, schema, contract, policy, source, evidence, lifecycle, release, deployment, renderer, or publication authority  
**Default posture:** commit-safe · non-secret · consumer-bound · versioned · explicit precedence · fail closed · renderer downstream · no public binding by presence alone

> [!IMPORTANT]
> A configuration file can influence renderer behavior, performance, network access, visual emphasis, and public exposure. That influence does **not** make configuration an authority surface. MapLibre may render only governed and released artifacts through accepted consumers; configuration cannot activate a source, admit a plugin, approve a style, release a layer, resolve evidence, override sensitivity, or publish a map.

> [!CAUTION]
> Current `main` is pinned in the metadata block at commit ccc4f3a7518271fadb6461ded3258706dd5c7303. The v0.3 singular-path migration is historical; this PR changes this README only. The workflow retains legacy and future-root filters as drift guards, the performance schema remains permissive, and no successful browser/performance, release, deployment, or publication result is claimed.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Current state](#current-repository-state) · [Repository fit](#repository-fit) · [Path migration](#config-versus-configs-path-migration) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Config classes](#configuration-classes) · [Consumer binding](#consumer-binding-contract) · [Precedence](#precedence-overrides-and-environments) · [Security](#secrets-endpoints-and-network-posture) · [Map trust](#map-trust-release-and-sensitive-geometry-boundaries) · [Styles](#styles-layers-tiles-sprites-and-glyphs) · [Plugins](#plugins-protocols-and-renderer-capabilities) · [Performance](#maplibre-performance-configuration-drift) · [Formats](#formats-naming-and-versioning) · [Validation](#validation) · [Negative cases](#required-negative-cases) · [Tests and CI](#tests-workflows-and-ci) · [Review](#review-burden) · [Change pattern](#safe-change-pattern) · [Implementation sequence](#smallest-safe-implementation-sequence) · [Definition of done](#definition-of-done) · [Evidence](#evidence-basis) · [Open decisions](#open-decisions-and-adr-triggers) · [Rollback](#rollback) · [Backlog](#verification-backlog)

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

**Canonical configuration sublane / no independent map, renderer, policy, evidence, release, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Parent root | **CONFIRMED** | The parent configs lane owns safe, non-secret defaults and templates. |
| Current path | **CONFIRMED on current main** | configs/maplibre/README.md is the documented target path. |
| Current payload inventory | **CONFIRMED** | The inspected configs/maplibre directory contains only this README and perf-envelope.v1.json. |
| Performance-envelope consumer set | **CONFIRMED BOUNDED TOOLING** | The current workflow and named perf/render/proof/release builders use the plural payload path. No general app/runtime loader or deployment binding is established. |
| MapLibre renderer doctrine | **ACCEPTED ARCHITECTURE / RUNTIME HOLD** | ADR-0006 and ADR-0007 are accepted decisions; the package-owned implementation is an initial bounded slice, not production readiness. |
| Shared MapLibre package | **IMPLEMENTED INITIAL SLICE** | packages/maplibre/package.json owns exact maplibre-gl 6.6.0, the renderer-neutral facade, lifecycle/camera adapter, and Vite worker seam. |
| Runtime package | **ABSENT AT NAMED PATH** | packages/maplibre-runtime/ is not present in the inspected current tree; no parallel runtime owner is authorized by this README. |
| Explorer map runtime | **BOUNDED / FAIL-CLOSED** | Explorer compositions use the renderer-neutral boundary and NullMapRuntime; full renderer activation remains held. |
| Single-importer boundary | **ACCEPTED ARCHITECTURE / STRUCTURAL HOLD** | ADR-0006 establishes package-owned acquisition; profile v14 records structural HOLD while raw acquisition remains confined to the accepted seam. |
| Sole-renderer decision | **ACCEPTED ARCHITECTURE** | ADR-0007 selects MapLibre GL JS as the browser renderer family; it does not admit plugins, protocols, sources, terrain, or public behavior. |
| MapLibre policy home | **NOT ESTABLISHED** | policy/maplibre/ is absent at the inspected named path. |
| Governed MapLibre schema family | **NOT ESTABLISHED** | schemas/contracts/v1/maplibre/ is absent; the existing schemas/maplibre envelope schema is permissive. |
| Performance workflow | **STATIC / NO-NETWORK HOLD** | The workflow performs syntax, AST, path, export, negative-path, retirement, readiness, and inventory checks without installing a browser or running performance. |
| Release or publication authority | **NONE** | A config file cannot approve a style, layer, tile, plugin, release, or public exposure. |

A canonical config location grants placement responsibility. It does not establish field semantics, consumer behavior, policy, release, renderer activation, or publication.

[Back to top](#top)


## Current repository state

### Bounded snapshot

The documentation baseline for this update is the direct current-main observation:

~~~text
repository: bartytime4life/Kansas-Frontier-Matrix
ref: main
commit: ccc4f3a7518271fadb6461ded3258706dd5c7303
tree: 358cc6036e7112be7688940b9e691c653baca569
~~~

At that tree, the tracked lane is:

~~~text
configs/maplibre/
├── README.md
└── perf-envelope.v1.json
~~~

The payload is a JSON object with object_type PerfEnvelope, schema_version v1, domain maplibre, public_safe posture, and five declared threshold values. Its presence proves a bounded input exists; it does not prove threshold adequacy, consumer execution, release approval, or public behavior.

No active configs/maplibre viewer, style, layer, or validation companion file was found at the inspected named paths. No v6-probe-results.json was present. The inspected current tree also has no packages/maplibre-runtime/, policy/maplibre/, or schemas/contracts/v1/maplibre/ directory at the named probes.

### Adjacent MapLibre surfaces

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| configs/maplibre/perf-envelope.v1.json | Present with threshold payload | Configuration input exists; semantics remain bounded by the permissive legacy schema. |
| packages/maplibre/package.json | Private @kfm/maplibre 0.0.0; exact maplibre-gl 6.6.0; explicit root, adapter, and Vite-adapter exports | Accepted package owns the initial renderer seam and dependency declaration. |
| packages/maplibre/src/* | Renderer-neutral port, NullMapRuntime, MapLibreAdapter, and Vite worker adapter | Lifecycle/camera slice is implemented; source/layer/style/protocol/plugin admission is not established. |
| apps/explorer-web/ | No direct maplibre-gl dependency; bounded map-runtime feature and NullMapRuntime composition | App does not directly acquire the renderer; production activation remains held. |
| apps/kansas-frontier-matrix-explorer/ | Vite alias to packages/maplibre/src/index.ts; no direct maplibre-gl dependency | Sites-derived consumer uses the renderer-neutral package boundary and remains fail-closed. |
| acquisition validator | Profile kfm-maplibre-acquisition-inventory-v14 | Current package-only renderer acquisition is a structural HOLD, not a readiness PASS. |
| v6 readiness validator and fixture | Profile kfm-maplibre-v6-6-readiness-v4; twelve probes absent or NOT_RUN | Exact target version is declared, but browser readiness is not proven. |
| .github/workflows/maplibre-perf-governance.yml | Static/no-network checks and explicit HOLD summaries | Workflow source is inspectable; a hosted result is not inferred from YAML. |
| scripts/maplibre-smoke-perf.mjs | Finite exit-3 WORKFLOW_HOLD | Legacy CDN/global harness is retired; replacement performance execution is NOT_RUN. |
| schemas/maplibre/perf-envelope.schema.json | Open object scaffold | Current validation is not a substantive closed contract. |
| artifacts/perf builders | Candidate render-diff, attestation, proof, release, correction, rollback, and failure-bundle outputs | Generated candidates are not canonical trust or release state. |

There is no supported general application quickstart for this lane. The performance payload has bounded tooling references, but no config loader, effective-config receipt, deployment binding, or public-runtime activation is established.

[Back to top](#top)


## Repository fit

Directory Rules assign one primary responsibility to each root. configs/maplibre/ remains subordinate to the map, app, schema, policy, data, release, test, runtime, and infrastructure roots that own behavior and authority.

| Responsibility | Owning surface | Relationship to this lane |
|---|---|---|
| Safe defaults and templates | configs/maplibre/ | This lane, after a consumer and validator are verified. |
| Deployable Explorer Web behavior | apps/explorer-web/ | Consumer implementation; config cannot replace app code. |
| App-local map-runtime composition | apps/explorer-web/src/features/map_runtime/ | Implemented bounded, renderer-neutral seam; config must not bypass it. |
| Shared MapLibre adapter/helpers | packages/maplibre/ | Accepted package-owned implementation; config supplies bounded inputs only. |
| Runtime adapters or harnesses | packages/maplibre/ and named app/test surfaces | Runtime behavior does not belong under config. |
| Map architecture and renderer doctrine | docs/architecture/ and accepted ADRs | Defines boundaries; config references rather than restates authority. |
| Semantic configuration contracts | contracts/ | Owns field meaning where a stable object family exists. |
| Machine configuration schemas | schemas/maplibre/ today; future contract home unresolved | The current envelope schema is permissive and not final authority. |
| Renderer, layer, access, sensitivity, rights, plugin, and release policy | policy/ | Config carries refs or safe defaults; it does not decide. |
| Layer/style/tile/source registries | Governed registry and catalog roots | Config must not become a registry. |
| Lifecycle artifacts | data/ through governed transitions | Config is not RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data. |
| Receipts and proofs | data/receipts/ and data/proofs/ | Generated trust evidence is not config. |
| Release, correction, supersession, withdrawal, rollback | release/ | Config cannot authorize release or record rollback state. |
| Test-local fixtures | tests/fixtures/ under accepted lanes | Deterministic test carriers; not config defaults. |
| Cross-cutting reusable fixtures | fixtures/ | Shared synthetic corpora; not config. |
| Generated QA/build output | artifacts/ | Reports and temporary outputs; not trusted config or release state. |
| Deployment secrets and exposure controls | External secret manager and infra/ | Never commit real secret material here. |

### Configuration is not a release artifact

A MapLibre style JSON, source list, layer definition, tile endpoint, sprite URL, glyph URL, camera preset, or plugin list can materially affect what users see. When such a file is itself a released public artifact, its authoritative copy and release state belong in the governed artifact/release lifecycle, not in configs/ merely because the file is parseable configuration.

configs/maplibre/ may contain safe defaults, templates, or references. It must not become the authoritative public style, manifest, tile index, plugin admission record, or release declaration.

[Back to top](#top)


## `config/` versus `configs/` path migration

### Current decision

The canonical path for the tracked performance envelope is:

~~~text
configs/maplibre/perf-envelope.v1.json
~~~

The singular config/maplibre/ path is absent from the inspected current command surfaces. The old v0.3 README recorded a historical migration from that nonexistent path; this update re-pins the statement to current main and does not repeat the migration as a new implementation change.

### Current consumers and guards

The current workflow and named performance builders use the plural path. The retired smoke harness no longer reads a payload. The workflow also retains:

~~~text
apps/explorer-web/**
apps/web/**                         # legacy drift guard retained
configs/maplibre/**
packages/maplibre-runtime/**       # future parallel-runtime guard
schemas/contracts/v1/maplibre/**   # future schema-family guard
~~~

These filters are useful drift signals, but a filter is not proof that a consumer loaded a config.

### Safe posture

- Keep configs/maplibre/ as the only active payload root.
- Do not create a duplicate payload, symlink, fallback search, or silent compatibility alias.
- Treat config/maplibre/ references in historical docs or migration examples as historical until individually revalidated.
- Keep the legacy apps/web/ filter and future-root guards visible until their owning migration decisions close.
- Do not infer a general app/runtime loader, deployment binding, or release authority from the path agreement.

### Migration decision requirements

Any future path migration should identify:

- canonical target;
- every reader and writer;
- schema path and contract owner;
- workflow path filters;
- package/app consumers;
- precedence and fallback behavior;
- deprecation period, if any;
- compatibility tests;
- rollback commit and file targets;
- drift-register or ADR need;
- owner and reviewer assignments.

[Back to top](#top)

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
config_id: "kfm://configs/maplibre/<name>"
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

The current scripts/maplibre-smoke-perf.mjs is a retired finite exit-3 WORKFLOW_HOLD. It names the former CDN/global acquisition as a retirement reason and performs no renderer, browser, network, source, screenshot, receipt, or artifact acquisition.

Therefore:

- this specific legacy harness is no longer evidence of an external-network run;
- future browser/performance execution is still NOT_RUN and is not presumed hermetic;
- external assets must be vendored, mocked, pinned, or explicitly governed before a future run can support a stronger claim;
- legacy URLs must not be copied into configs/maplibre/ as general defaults.

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

### Current command-bearing workflow

The current .github/workflows/maplibre-perf-governance.yml is a static/no-network governance guard. Its relevant behavior is:

- watches the canonical configs/maplibre/** lane plus implementation, test, validator, fixture, schema, and workflow paths;
- retains apps/web/** and future packages/maplibre-runtime/** and schemas/contracts/v1/maplibre/** filters as visible drift guards;
- performs Node syntax checks for the MapLibre script set and Python AST checks for validators/tests;
- runs nine deterministic no-network negative-path, retirement, and package-export checks;
- checks exact pnpm/Node and maplibre-gl 6.6.0 package declarations, lock closure, required files, placeholder schema posture, and acquisition/readiness markers;
- requires readiness to remain HOLD with runtime probes pending;
- records WORKFLOW_HOLD and WORKFLOW_SKIPPED_EXPLICIT for browser, performance, render comparison, attestation, proof, release-manifest, correction, rollback, and failure-bundle execution;
- does not install dependencies, launch a browser, fetch external sources, upload artifacts, sign outputs, publish, deploy, or change repository contents.

The workflow is implementation evidence for the guard's source and negative-path scope. It is not a successful performance run, browser-readiness proof, release gate, or publication decision.

### Payload and consumer path

configs/maplibre/perf-envelope.v1.json is the bounded threshold input. Named render-diff, proof-pack, and release-manifest builders reference it while writing candidate outputs under artifacts/perf/. Those outputs remain non-canonical. The retired smoke harness no longer consumes the envelope.

### Current holds

| Area | Current posture |
|---|---|
| Payload path | CONFIRMED plural path |
| Payload shape | JSON v1 object; legacy open-object schema |
| Consumer binding | Named tooling only; no general loader |
| Renderer dependency | Exact package-owned maplibre-gl 6.6.0 |
| Raw acquisition | Package seam only; acquisition profile v14 STRUCTURAL HOLD |
| Browser readiness | Twelve probes absent or NOT_RUN; readiness profile HOLD |
| Performance execution | NOT_RUN |
| Baselines and render diff | Candidate builders present; no governed baseline result |
| Attestation/proof/release outputs | Candidate-shaped only under artifacts/perf/ |
| Hosted workflow result | UNKNOWN until inspected on the PR |
| Public/runtime behavior | UNKNOWN / NOT PROVEN |

### Current safe conclusion

The performance envelope is a reviewable configuration input with a confirmed plural path and bounded tooling references. It is not a meaningful performance contract yet, and it cannot authorize renderer activation, source/layer admission, release, deployment, publication, or trust closure.

[Back to top](#top)


## Formats, naming, and versioning

### Supported format posture

JSON is the only machine payload format confirmed in this lane: perf-envelope.v1.json is tracked and consumed by named tooling. No YAML, TOML, or runtime viewer configuration file is established here.

| Format | Appropriate use | Guardrails |
|---|---|---|
| JSON | Strict machine-consumed config and threshold declarations | Valid JSON; schema version required; current open schema is not sufficient final enforcement. |
| YAML | Human-reviewed defaults/templates | Duplicate keys rejected; anchors/merges constrained; parser behavior pinned before adoption. |
| TOML | Tool/package defaults where a consumer uses TOML | Consumer and version named; no implicit environment secrets. |
| .env.example | Variable names and obvious placeholders only | Prefer configs/examples/; never real values. |
| Markdown | Lane docs and verified validation instructions | Not machine configuration. |

### Proposed naming pattern

Names should communicate class and version, for example:

~~~text
<consumer>.<purpose>.defaults.v1.yaml
<consumer>.<purpose>.template.v1.yaml
<consumer>.<purpose>.example.v1.json
<consumer>.<purpose>.thresholds.v1.json
~~~

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

A filename such as v1 is insufficient unless the file also declares or resolves its version semantics.

### Deterministic identity

Where config affects reproducible tests, generated artifacts, or release candidates, the consumer should record a canonical digest or spec hash over the resolved config and its relevant refs. Hashing does not authorize the config; it enables drift detection and replay.

[Back to top](#top)


## Validation

Validation must be layered. Parsing alone is not enough, and the current open-object schema must not be described as substantive contract validation.

### Current evidence result

The current-main source inspection confirms:

- the target and payload are present under configs/maplibre/;
- the payload has JSON v1/object_type PerfEnvelope shape and five threshold values;
- schemas/maplibre/perf-envelope.schema.json is an additionalProperties-true open object with no required fields;
- the package manifest declares exact maplibre-gl 6.6.0 and explicit exports;
- the acquisition and readiness validators encode structural HOLD conditions;
- the workflow source contains deterministic no-network checks and explicit execution holds.

No local checkout-based command execution is claimed for this documentation update. No hosted PR result is claimed until GitHub reports it.

### Validation matrix

| Layer | Current status | Failure posture |
|---|---:|---|
| Path/inventory | **PASS STATIC** | Keep the plural root; reject duplicate or singular active payloads. |
| Classification | **PARTIAL** | Every future file must name its class and consumer. |
| Syntax/JSON | **PASS BY SOURCE SHAPE** | Reject malformed or ambiguous payloads. |
| Duplicate keys | **NOT PROVEN** | Use a strict parser before accepting new machine payloads. |
| Schema | **HOLD** | The legacy schema is permissive; do not treat it as a closed contract. |
| Contract semantics | **PROPOSED** | Define field meaning and owners before widening the lane. |
| Consumer binding | **PARTIAL** | Named tooling exists; no general loader or effective-config receipt is proven. |
| Version compatibility | **PARTIAL** | Payload v1 and renderer 6.6.0 are declared in separate bounded surfaces. |
| Precedence/overrides | **ABSENT** | Do not infer merge order or environment behavior. |
| Secrets/endpoints | **STATIC NEGATIVE POSTURE** | Deny real secrets/private endpoints and unknown network access. |
| Acquisition boundary | **HOLD** | Keep raw renderer acquisition inside packages/maplibre/. |
| Browser readiness | **HOLD** | Twelve runtime probes must be run and reviewed before a stronger claim. |
| Policy/release/evidence | **NOT ESTABLISHED** | Config cannot override policy or authorize released output. |
| Determinism/rollback | **PROPOSED** | Add receipts and rollback refs only under accepted owners and contracts. |
| Trigger coverage | **PRESENT / RUN UNKNOWN** | Inspect the hosted workflow result and branch-protection requirement. |

A validator should return a finite, structured outcome such as:

~~~text
PASS
FAIL
ABSTAIN
DENY
ERROR
~~~

A PASS means only that the validator's checks passed. It does not authorize release, plugin admission, source activation, or publication. The current workflow's explicit HOLD state is the safe outcome for unproven runtime/performance work.

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
| Workflow watches wrong config path | CI coverage marked failed/absent; fixed by migrating all readers and filters together. |
| Validator uses permissive empty schema | Governance validation fails. |
| Required config payload absent | Workflow fails finitely; no release claim. The tracked v1 payload is present at the inspected base. |

[Back to top](#top)

---


## Tests, workflows, and CI

### Current state

The current workflow is a static/no-network guard, not a browser or performance execution job. Its source-defined checks include:

- Node syntax checks for the MapLibre script set;
- Python AST parsing for the MapLibre validators and tests;
- nine deterministic calls covering budget rejection, legacy-harness retirement, acquisition confinement, package export ownership, and renderer-neutral root exports;
- exact package-manager, Node, lockfile, dependency, schema, fixture, and path-marker checks;
- explicit readiness HOLD and explicit skips for browser/performance/render/trust stages.

The workflow path filters include configs/maplibre/** and apps/explorer-web/**, while retaining apps/web/** and future package/schema roots as drift guards. Because the PR changes configs/maplibre/README.md, the hosted result must be inspected after the PR is opened; YAML source alone is not a CI result.

### Required test layers

A mature configuration surface should have:

1. **Parser tests** — valid and invalid syntax, duplicate keys, numeric bounds.
2. **Schema tests** — required fields, versions, enums, closed objects, extension rules.
3. **Consumer tests** — loader reads the expected path or config ID.
4. **Precedence tests** — defaults, profiles, deployment bindings, and overrides resolve deterministically.
5. **Security tests** — secret, private endpoint, redirect, and log-redaction cases.
6. **Network tests** — deny-by-default/offline behavior and allowlist enforcement.
7. **Map-boundary tests** — no RAW/canonical/internal URLs; no direct unverified addSource.
8. **Release tests** — unreleased, stale, corrected, withdrawn, superseded, and rolled-back refs.
9. **Sensitivity tests** — no style-filter geoprivacy; transformed artifacts only.
10. **Plugin tests** — unknown/unadmitted/version-mismatched plugins fail closed.
11. **Performance tests** — thresholds, units, scenarios, browser/runtime pins, deterministic metrics.
12. **Accessibility tests** — reduced motion, keyboard, focus, non-map alternative.
13. **Migration tests** — old path/field compatibility and deprecation.
14. **Workflow-trigger tests** — canonical path changes run the required checks.
15. **Root trust-spine tests** — public clients remain on governed released interfaces.

### CI claims

Do not claim that a config is CI validated unless:

- the relevant workflow watches its canonical path;
- the job actually runs the parser/schema/consumer/security checks;
- the required payload exists;
- the workflow result is inspected;
- generated evidence is distinguished from release authority;
- branch protection or promotion gates actually require the check where material.

A green workflow that did not trigger on the changed path is not validation. A source-defined HOLD is not a successful performance run.

[Back to top](#top)

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

A mature configs/maplibre/ lane should satisfy all applicable items.

### Ownership and placement

- [x] configs/maplibre/ is the canonical lane under the current Directory Rules decision and parent README.
- [x] The inspected current tree has no active singular config/maplibre/ payload or workflow path in the bounded command surfaces.
- [x] No parallel active config payload exists in the inspected tree.
- [ ] Owners and reviewers are assigned.
- [ ] Drift/ADR/migration records exist where required.

### Inventory

- [x] The two-file lane inventory is verified against current main at commit ccc4f3a7518271fadb6461ded3258706dd5c7303.
- [ ] Every file has a config class.
- [ ] Every file names a consumer.
- [ ] Stale, orphaned, or duplicate files are removed or deprecated.
- [x] Generated output and trust objects are absent from the tracked lane.

### Contracts and schemas

- [ ] Stable config meaning is defined where needed.
- [ ] A closed, versioned schema validates each machine payload.
- [x] The current permissive schema is explicitly treated as a legacy scaffold, not final authority.
- [ ] Unknown fields and unsupported versions fail deterministically.
- [ ] Valid/invalid fixtures exist in their correct homes.

### Consumer binding

- [ ] Loader path and interface are verified.
- [ ] Precedence and override behavior are explicit.
- [ ] Effective config is deterministic.
- [ ] Missing and conflicting config behavior is tested.
- [ ] Consumer/version compatibility is enforced.
- [x] Config documentation keeps raw MapLibre objects behind the accepted package boundary.

### Security

- [x] No secrets or private endpoints are present in the inspected config payload.
- [ ] Endpoint allowlist/network posture is explicit for future browser consumers.
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
- [ ] A config validation PASS is not treated as release approval.

### Tests and CI

- [ ] Parser, schema, consumer, precedence, security, network, trust, plugin, performance, accessibility, migration, and rollback tests exist as applicable.
- [x] The MapLibre workflow path filter includes configs/maplibre/**.
- [x] The required v1 payload exists before the workflow starts.
- [ ] CI reports collection and substantive results.
- [x] The current source-defined workflow keeps browser/performance execution explicitly held.
- [ ] QA artifact uploads are not treated as canonical release state.

### Documentation and operations

- [ ] Parent and sibling README files agree.
- [ ] Supported commands are observed and documented.
- [ ] Migration and rollback are concrete.
- [ ] Deprecation dates and replacements are visible.
- [ ] Operational failure and recovery paths are documented.
- [ ] Last review dates are current.

Until the remaining items are verified, the lane remains a bounded two-file configuration surface with a package-adjacent renderer implementation and runtime/performance holds; it is not a fully governed MapLibre runtime or release surface.

[Back to top](#top)


## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| Direct current-main ref ccc4f3a7518271fadb6461ded3258706dd5c7303 and tree 358cc6036e7112be7688940b9e691c653baca569 | **CONFIRMED** | Exact base for this documentation update. | Snapshot will need re-pinning after later implementation changes. |
| configs/maplibre directory at current main | **CONFIRMED** | Only README and perf-envelope.v1.json are present at the inspected path. | Does not reveal ignored files, other refs, or unqueried differently named paths. |
| Target README blob 40bb91dd6b810b70f50bdba07b58d78fcb125ad2 | **CONFIRMED** | Prior current-main version being refreshed. | Its v0.3 claims were stale relative to current implementation. |
| configs/maplibre/perf-envelope.v1.json blob 2833f99b5316df91e71c0f8913bb06d70917abcf | **CONFIRMED** | JSON v1 threshold input exists at the plural root. | Does not prove contract adequacy, execution, approval, or release authority. |
| docs/architecture/maplibre.md blob a3cc800aaa8f9c541ae363f3b0194aae4f91eec3 | **CONFIRMED DOCUMENT** | Accepted boundary, package ownership, NullMapRuntime fallback, acquisition/readiness HOLD posture, and held broader capability claims. | Architecture text is not a hosted runtime result. |
| ADR-0006 and ADR-0007 | **CONFIRMED ACCEPTED ARCHITECTURE** | Package-owned MapLibre acquisition seam and selected renderer family. | Acceptance does not prove browser readiness or production activation. |
| packages/maplibre/package.json blob f6d450af19c33011e159e123c8a07ca2bca6dfd | **CONFIRMED IMPLEMENTATION** | Exact maplibre-gl 6.6.0 declaration and explicit package exports. | License/provenance, build, deployment, and full consumer readiness remain separate. |
| packages/maplibre source modules | **CONFIRMED BOUNDED IMPLEMENTATION** | Renderer-neutral port, NullMapRuntime, lifecycle/camera adapter, and Vite worker seam. | Source/layer/style/protocol/plugin/terrain/public behavior remain held or unproven. |
| Explorer application surfaces | **CONFIRMED BOUNDED CONSUMPTION** | No direct renderer dependency in the named apps; renderer-neutral/fail-closed composition. | Does not prove production activation or deployed behavior. |
| assess_acquisition_inventory.py blob 2c6d2b709e2cf4a519b32c2274820008a18ad0f4 | **CONFIRMED VALIDATOR SOURCE** | Profile v14 and structural HOLD/FAIL logic. | The validator source is not itself a successful run. |
| validate_v6_readiness.py and v6 fixture | **CONFIRMED VALIDATOR/TEST SOURCE** | Exact 6.6.0 target and twelve-probe readiness model. | Current probes are absent or NOT_RUN; no readiness PASS is claimed. |
| .github/workflows/maplibre-perf-governance.yml | **CONFIRMED WORKFLOW SOURCE** | Static/no-network checks, path filters, explicit holds, and read-only permissions. | No hosted conclusion is inferred from YAML. |
| scripts/maplibre-smoke-perf.mjs | **CONFIRMED RETIRED HARNESS** | Finite exit-3 hold and removal of legacy live acquisition. | Replacement performance execution is not run. |
| schemas/maplibre/perf-envelope.schema.json and validator wrappers | **CONFIRMED PERMISSIVE SCAFFOLD** | Current schema home and open-object behavior. | Not a meaningful closed contract. |
| Candidate builders under scripts/ and artifacts/perf/ | **CONFIRMED CANDIDATE SURFACES** | Render-diff, attestation, proof, release, correction, rollback, and failure-bundle scaffolding. | Candidate outputs are not canonical trust, release, or publication state. |
| Notion: “Close governed MapLibre runtime probe matrix” | **READ-ONLY COORDINATION CONTEXT** | Current hold language, re-pin requirement, and missing browser/long-session evidence context. | Coordination properties are stale relative to current GitHub main and do not override code. |
| Drive: KFM MapLibre Operating Architecture manual and Master MapLibre Components manual | **READ-ONLY CORPUS/LINEAGE** | Governance doctrine, renderer-downstream posture, and proposed implementation boundaries. | The source manuals explicitly do not prove repository implementation, tests, or deployment. |

### Evidence limits

This update did not:

- execute a config loader;
- run the performance workflow;
- claim a hosted PR check result;
- import MapLibre in a local checkout;
- launch Explorer Web;
- verify all package or schema files by runtime execution;
- verify deployment;
- query a release registry;
- resolve EvidenceBundles;
- verify public map behavior.

Future file names, metadata shapes, contracts, validators, test cases, and migration phases are PROPOSED unless explicitly labeled otherwise.

[Back to top](#top)


## Open decisions and ADR triggers

| Decision | Current status | Trigger |
|---|---:|---|
| Canonical configs/maplibre/ payload path | **RESOLVED FOR CURRENT PERF TOOLING** | Reintroduction of singular config/maplibre/, an alias, or a duplicate payload. |
| MapLibre performance-envelope home | **CONFIRMED AT configs/maplibre/** | Moving or duplicating the existing payload. |
| Perf-envelope contract and schema | **PERMISSIVE LEGACY SCAFFOLD / NEEDS DESIGN** | Adding required fields, closing the object, changing versions, or widening consumers. |
| Canonical MapLibre schema family | **UNRESOLVED** | Moving from schemas/maplibre/ to schemas/contracts/v1/maplibre/ or another accepted home. |
| Workflow app-path coverage | **PARTIAL** | Removing or retaining apps/web/**, or changing the legacy guard. |
| Active adapter/runtime package | **RESOLVED PACKAGE OWNERSHIP / RUNTIME HOLD** | Declaring production activation, creating a parallel runtime package, or bypassing packages/maplibre/. |
| Sole-renderer status | **ACCEPTED ARCHITECTURE / CAPABILITY HOLD** | Adding a plugin, protocol, alternate renderer, source/layer/terrain behavior, or exception path. |
| Plugin admission policy | **NOT ESTABLISHED** | Enabling any plugin or protocol through config. |
| Config loader and precedence | **ABSENT / UNKNOWN** | Introducing auto-loading, profile merging, environment overrides, or effective-config receipts. |
| External network posture | **STATIC NO-NETWORK GUARD / FUTURE RUN NOT_RUN** | Running browser/performance work with external, mocked, vendored, or allowlisted assets. |
| Performance thresholds | **PRESENT / ADEQUACY UNKNOWN** | Changing values that can block or permit candidate progression. |
| Trust-shaped output homes | **CANDIDATE / NON-CANONICAL** | Treating artifacts/perf/ output as receipts, proofs, release state, or publication state. |
| Workflow enforcement | **SOURCE PRESENT / HOSTED RESULT UNKNOWN** | Claiming required-check enforcement or successful execution. |
| Style/layer/tile/config refs | **NOT ESTABLISHED** | Adding a style, source, layer, endpoint, sprite, glyph, PMTiles, COG, terrain, or globe reference. |
| Endpoint allowlist and secrets binding | **UNKNOWN** | Adding any non-local endpoint or credential reference. |
| Owner assignments | **OWNER_TBD** | Moving beyond documentation-only config maturity. |

### ADR or migration discipline

An ADR or formal migration record is appropriate when a change:

- creates or changes a canonical path;
- changes schema authority;
- changes renderer strategy or package ownership;
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


## Rollback

This PR changes one Markdown file: configs/maplibre/README.md. It does not change the payload, workflow, scripts, schemas, package, app code, fixtures, lifecycle objects, release records, endpoints, secrets, or public behavior.

### Before merge

Close or abandon the review branch or pull request. No deployment, release, package publication, or map/data publication occurs from this documentation-only branch.

### After merge

Restore the prior current-main README blob 40bb91dd6b810b70f50bdba07b58d78fcb125ad2 through a reviewed revert, or revert the commit that introduces this v0.4 documentation. The base observation for this PR is:

~~~text
base ref: main
base commit: ccc4f3a7518271fadb6461ded3258706dd5c7303
prior README blob: 40bb91dd6b810b70f50bdba07b58d78fcb125ad2
~~~

If later implementation changes have landed, do not use this documentation rollback as an operational rollback. Re-pin the README to the actual target commit and preserve the implementation's own rollback target.

### Rollback triggers

Correct or roll back this README if it:

- claims a config payload exists when it does not;
- claims a consumer binding without code or test evidence;
- reintroduces singular config/maplibre/ as an active or compatibility root;
- treats a permissive schema as substantive validation;
- claims successful MapLibre performance enforcement without workflow-run evidence;
- treats artifacts/perf/ as canonical proof or release state;
- authorizes public endpoints, styles, layers, plugins, or tiles;
- implies style filtering is sufficient sensitivity protection;
- documents unverified commands as supported;
- exposes secrets, private endpoints, or sensitive details;
- conflicts materially with accepted Directory Rules, ADRs, app/package boundaries, or release controls.

### Documentation rollback is not operational rollback

Reverting this README will not revert any later config payload, workflow, script, schema, package, app, policy, deployment, artifact, or release change. Every material implementation change requires its own rollback target.

[Back to top](#top)


## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Inventory configs/maplibre/. | **CONFIRMED CURRENT MAIN** | Re-run after tracked lane changes. |
| Inventory singular config/maplibre/. | **CONFIRMED ABSENT AT INSPECTED PATHS** | Re-run if any singular reference reappears. |
| Keep canonical config path aligned. | **CONFIRMED FOR BOUNDED TOOLING** | Static reference scan and workflow review. |
| Identify performance-envelope readers/writers. | **CONFIRMED STATIC BOUNDED SET** | Named workflow/builders are known; runtime traces and any hidden consumers remain unverified. |
| Confirm active app path in all workflow consumers. | **PARTIAL** | Resolve retained apps/web/** guard versus apps/explorer-web/** canonical path. |
| Confirm MapLibre adapter/runtime home. | **RESOLVED PACKAGE OWNERSHIP / RUNTIME HOLD** | Production activation, broader capability, and parallel-runtime cleanup evidence. |
| Define performance-envelope contract. | **PAYLOAD PRESENT / CONTRACT PROPOSED** | Closed schema, field owners, consumer requirements, and migration plan. |
| Replace permissive legacy schema. | **NEEDS VERIFICATION** | Accepted closed schema, fixtures, validator, and migration. |
| Verify workflow run for this PR. | **PENDING PR** | Hosted check conclusion, logs, and branch-protection requirement. |
| Verify no-network/hermetic posture for future performance. | **NOT ESTABLISHED** | Vendored/mocked assets, allowlist, offline tests, and browser evidence. |
| Verify endpoint security and attribution. | **UNKNOWN** | Policy, licenses, pins, integrity, redirect tests. |
| Verify config secret scanning. | **NEEDS VERIFICATION** | Workflow/config and test evidence. |
| Define loader and precedence. | **ABSENT / UNKNOWN** | Consumer implementation and tests. |
| Define config identity/version/hash posture. | **PROPOSED** | Contract/schema and replay tests. |
| Define plugin/protocol config boundary. | **PROPOSED** | Accepted ADR, policy, contract, schema, package tests. |
| Define released style/layer reference behavior. | **NEEDS VERIFICATION** | Manifest contracts, governed API, release tests. |
| Verify sensitive-geometry safeguards. | **NEEDS VERIFICATION** | Upstream transform receipts and no-style-filter tests. |
| Reconcile candidate QA artifacts with canonical receipts/proofs/releases. | **CONFLICTED** | Data/release owner decision and workflow changes. |
| Assign owners/CODEOWNERS. | **OWNER_TBD** | Reviewed repository ownership changes. |
| Keep docs aligned after implementation changes. | **ONGOING** | Parent/sibling docs, ADRs, and link checks. |

[Back to top](#top)

## Maintainer checklist

- [ ] Keep `configs/maplibre/` limited to commit-safe configuration defaults/templates.
- [ ] Keep the plural path canonical and reject reintroduced singular references.
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
