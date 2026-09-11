<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-maplibre-readme
title: schemas/maplibre/ — MapLibre Performance-Schema Compatibility and Readiness Boundary
type: README
version: v0.4
status: draft; repository-grounded; transitional-compatibility-lane; one-closed-config-schema; seven-permissive-placeholders; workflow-held; migration-unresolved; non-authoritative; non-release
owner: NEEDS VERIFICATION — CODEOWNERS routes /schemas/ to @bartytime4life, but routing is not accepted stewardship or independent approval
created: 2026-07-05
updated: 2026-09-08
policy_label: public
owning_root: schemas/
current_path: schemas/maplibre/README.md
responsibility: Preserve a bounded compatibility index for eight unversioned MapLibre performance schemas, enforce the repository-owned PerfEnvelope v1 configuration shape, bound the seven remaining placeholders, and route future canonical machine-shape work without claiming runtime, release, or publication maturity.
truth_posture: CONFIRMED closed PerfEnvelope v1 machine constraints, tracked-config validation, synthetic fixture polarity, focused tests, and CI binding; CONFIRMED seven adjacent placeholders; PROPOSED or UNKNOWN canonical destinations, ownership, benchmark semantics, runtime activation, migration, release, and retirement
evidence_snapshot: base main@b30210971c41073a9a2e36b5a0d7d451ef43d592; current checkout and bounded offline validation on 2026-09-08
related:
  - schemas/README.md
  - schemas/contracts/v1/map/README.md
  - schemas/contracts/v1/layers/README.md
  - configs/maplibre/README.md
  - contracts/README.md
  - policy/README.md
  - tools/validators/maplibre/README.md
  - tests/maplibre/README.md
  - tests/fixtures/maplibre/README.md
  - tests/fixtures/maplibre/perf-envelope/README.md
  - tests/maplibre/test_perf_envelope_contract.py
  - packages/maplibre/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/quality/maplibre-perf-governance.md
  - .github/workflows/maplibre-perf-governance.yml
  - .github/workflows/schema-validation.yml
tags: [kfm, schemas, maplibre, performance, compatibility, readiness, validation, migration, evidence]
notes:
  - The PerfEnvelope v1 schema is closed and executable; the other seven direct schemas retain the historical Draft 2020-12 accept-any-object shape.
  - The MapLibre performance workflow retains WORKFLOW_HOLD for browser/runtime stages; schema validity is not readiness, release, or publication evidence.
  - ADR-0029, ADR-0006, and ADR-0007 are accepted. ADR-0001 and object-family migration remain proposed or unresolved.
  - This dependency-closed slice changes one schema, its validator/fixtures/tests, two workflow bindings, and boundary documentation; it changes no runtime threshold value, renderer, release, or publication state.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `schemas/maplibre/` — MapLibre Performance-Schema Compatibility and Readiness Boundary

> **One-line purpose.** Enforce the tracked PerfEnvelope v1 machine shape, keep seven historical trust-output placeholders visible and bounded, and prevent green checks from being mistaken for runtime readiness, release approval, or publication authority.

<kbd>TRANSITIONAL COMPATIBILITY</kbd> <kbd>1 CLOSED CONFIG SCHEMA</kbd> <kbd>7 PLACEHOLDERS</kbd> <kbd>RUNTIME: HOLD</kbd> <kbd>PUBLISHER: NO</kbd>

> [!IMPORTANT]
> `schemas/maplibre/` is a transitional lane beneath the canonical
> [`schemas/`](../README.md) machine-shape root. `perf-envelope.schema.json`
> now validates the exact repository-owned v1 configuration identity, fields,
> numeric domains, and notes shape. The other seven JSON files still accept any
> object. None defines benchmark authority, evidence, policy, promotion, release,
> or safe-presentation rules.

> [!CAUTION]
> Do not add consumers to the seven placeholders or infer runtime readiness from
> the closed configuration schema. Canonical migration and any trust-output
> implementation still require object-family routing, reviewed contracts,
> fixtures, validators, consumer evidence, and separate release governance.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-inheritance) · [Status](#status-and-evidence) · [Map](#current-directory-map) · [Inventory](#complete-schema-inventory) · [Shape](#verified-schema-shapes) · [Routing](#object-family-and-authority-routing) · [Flow](#governed-responsibility-flow) · [Boundaries](#what-belongs-here) · [Interfaces](#inputs-outputs-writers-and-consumers) · [Validation](#validation-and-negative-checks) · [CI](#current-ci-and-readiness-boundary) · [Migration](#compatibility-migration-and-retirement) · [Review](#review-burden-and-escalation) · [Done](#definition-of-done) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger) · [Correction](#correction-and-rollback)

---

## Purpose

This directory retains eight historical, unversioned filenames. One has a
bounded current consumer: the repository-owned `PerfEnvelope` v1 configuration.
Canonical placement and semantics for that object, and all shape/authority work
for the other seven objects, remain subject to reviewed migration decisions.

This compatibility lane exists to:

- make the exact current bytes and their limitations discoverable;
- stop unversioned file paths from quietly becoming stable public contracts;
- preserve migration context without creating a parallel schema authority;
- separate machine shape from meaning, evidence, policy, configuration, runtime rendering, and release state;
- provide fail-closed contribution and review rules; and
- record the evidence required before any placeholder can be promoted, redirected, deprecated, tombstoned, or removed.

It does **not** make the filenames canonical, the schemas meaningful, the workflow operational, the MapLibre adapter implemented, or any result safe to publish.

The durable responsibility split is:

| Responsibility root | Owns | Does not gain authority from this README |
|---|---|---|
| `contracts/` | Semantic meaning, invariants, lifecycle, and cross-object relationships | Machine shape, policy execution, or release approval |
| `schemas/` | Machine-checkable shape and versioned schema identity | Truth, rights, sensitivity, review, or publication |
| `policy/` | Allow, deny, restrict, abstain, and escalation logic | Schema validity or artifact release by itself |
| `configs/` | Commit-safe thresholds and defaults | Evidence, promotion, or release records |
| `fixtures/` and `tests/` | Representative examples, counterexamples, and enforceability proof | Runtime production behavior unless explicitly exercised |
| `tools/validators/` | Executable checks with bounded inputs and finite outcomes | Authority to waive failed policy or release gates |
| `data/receipts/`, proof, and evidence surfaces | Append-oriented records about evaluated events | Retroactive truth or automatic publication |
| `release/` | Promotion, release, correction, withdrawal, and rollback governance | Semantic contract authorship or renderer implementation |
| `packages/` and `apps/` | Adapter, renderer, governed API, and UI behavior | Canonical schema or policy authority |

MapLibre is downstream of these authorities. It renders reviewed, released, public-safe carriers; it does not become a source of truth because an object can be displayed.

## Authority and inheritance

### Governing authority

| Source | Status at the evidence snapshot | Effect here |
|---|---|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Adopts the exact Directory Rules v2 bytes and their responsibility-root, README, placement, compatibility, and change-control rules. |
| [Directory Rules v2](../../docs/doctrine/directory-rules.md) | **ADOPTED BY ADR-0029**; its pinned internal header still records its original proposal posture | Defines `schemas/` as machine shape, requires the contracts/schemas/policy split, and defaults new schema families to `schemas/contracts/v1/<family>/` unless an accepted ADR establishes another versioned profile. |
| [`schemas/README.md`](../README.md) | **CURRENT ROOT CONTRACT** | Supplies parent machine-shape and maturity rules. Its earlier all-permissive description is superseded locally by the current one-closed/seven-placeholder inventory and should be reconciled separately. |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | **MACHINE PROJECTION ONLY** | Registers `root.schemas`. It does not accept a child-family destination, activate a schema, or create independent authority. |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Describes stronger schema-home canonicalization and migration intent; it is useful design context, not accepted migration authority. |
| [ADR-0004](../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) | **DRAFT source / effectively PROPOSED** | Describes the governed API trust-membrane design. It does not prove that the trust membrane or these object flows are implemented. |
| MapLibre adapter and renderer decisions | **ACCEPTED ARCHITECTURE** | ADR-0006 accepts the package seam and ADR-0007 accepts the renderer family; neither turns configuration validation into runtime readiness. |

### Local authority statement

This README may document observed repository state, route contributors, preserve compatibility facts, and name unresolved decisions. It must not:

- accept, supersede, or silently implement an ADR;
- assign a canonical versioned family to any object without review;
- create a second writable schema authority;
- define contract semantics, policy decisions, evidence requirements, or release gates in prose;
- use schema validity to activate a package, adapter, API, renderer, release, or public map;
- authorize promotion, release, publication, correction, withdrawal, rollback execution, tombstoning, or deletion; or
- convert placeholders into implemented artifacts by relabeling them.

`CODEOWNERS` routes `/schemas/` review to `@bartytime4life`. That is review routing only. It does not prove an accepted schema steward, object-family owner, independent approver, separation of duties, branch protection, or release authority.

### Authority precedence

When sources disagree, apply the following fail-closed order:

1. accepted ADRs and the exact adopted doctrine bytes they identify;
2. current responsibility-root contracts and accepted versioned-family rules;
3. machine projections and executable validators within their declared scope;
4. local compatibility documentation;
5. architecture lineage and proposals.

File proximity, age, naming, import history, or workflow success does not override accepted authority.

## Status and evidence

The following statements use base `main@b30210971c41073a9a2e36b5a0d7d451ef43d592`
and the current reviewed change unless a historical hosted run is named separately.

| Question | Evidence-backed answer | Truth label |
|---|---|---|
| Is this directory tracked? | Yes; it contains one README and eight direct schema files. | **CONFIRMED** |
| Were all direct schema files inspected? | Yes; the inventory and current content were compared. | **CONFIRMED** |
| Are the eight schema files distinct implementations? | One (`perf-envelope`) is closed; the other seven retain the common placeholder shape. | **CONFIRMED** |
| Do they parse and declare a JSON Schema draft? | Yes. Each declares `https://json-schema.org/draft/2020-12/schema`. | **CONFIRMED** |
| Do they validate meaningful fields? | `perf-envelope` validates exact v1 identity/posture, a closed five-threshold object, numeric domains, and bounded notes. The other seven do not validate filename-implied fields. | **CONFIRMED MIXED MATURITY** |
| Do they define stable canonical `$id` values? | No. `perf-envelope` has a title/description and payload version constant but deliberately does not claim a canonical schema URI at this transitional path. | **CONFIRMED / MIGRATION HOLD** |
| Is `schemas/` the correct responsibility root for machine shape? | Yes, under accepted ADR-0029 and Directory Rules v2. | **CONFIRMED** |
| Is this unversioned child the accepted final home? | No accepted decision assigning these eight objects here was verified. | **NEEDS VERIFICATION / HOLD** |
| Is one `map` family the correct destination for all eight objects? | Not established. Receipts, proofs, release manifests, correction notices, failure bundles, and rollback plans cross semantic and lifecycle boundaries. | **UNKNOWN / NEEDS OBJECT-FAMILY REVIEW** |
| Are wrapper validators present? | Yes; all eight use the common runner. The envelope wrapper now binds reviewed fixtures and resolves schema/fixture paths independently of the caller's working directory. | **CONFIRMED** |
| Are broader performance-governance verifiers implemented? | No. The inspected workflow asserts that seven remain placeholders. | **CONFIRMED HOLD** |
| Are there executable negative tests? | Yes; fourteen envelope fixtures cover identity, version, posture, field closure, types, timing domains, pixel ratio, and notes, alongside the separate three scalar tests. | **CONFIRMED** |
| Is MapLibre runtime readiness proved here? | No. Package/runtime evidence is owned elsewhere and the readiness classifier remains `HOLD` with runtime probes pending. | **CONFIRMED HOLD** |
| Did a historical MapLibre performance run pass? | Run `31654973078` concluded `success` while explicitly recording `WORKFLOW_HOLD`; exact-head hosted results for this change remain pending. | **HISTORICAL SUCCESS + CURRENT HOLD** |
| Does that run prove browser performance, render parity, proof, release, rollback, or publication? | No. Those stages were not executed by the inspected workflow. | **CONFIRMED NON-PROOF** |
| Are owner, consumer set, migration schedule, and retirement criteria accepted? | No complete accepted record was verified. | **NEEDS VERIFICATION** |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Directly observed in the pinned Git tree, file bytes, workflow definition, hosted run, or adopted authority. |
| **INFERRED** | A bounded conclusion from confirmed evidence; the inference and its limits are stated. |
| **PROPOSED** | Declared design or candidate state that is not accepted or active. |
| **UNKNOWN** | Available evidence does not establish the answer. |
| **NEEDS VERIFICATION** | A specific repository, governance, test, runtime, or consumer check remains open. |
| **HOLD** | Do not rely, migrate, activate, release, publish, retire, or delete until the named gates close. |

## Current directory map

Directory Rules `DIR-README-003` requires this map to show the current directory and direct children only.

```text
schemas/maplibre/
├── README.md
├── perf-correction-notice.schema.json
├── perf-envelope.schema.json
├── perf-failure-bundle.schema.json
├── perf-proof-pack.schema.json
├── perf-receipt.schema.json
├── perf-release-manifest.schema.json
├── perf-rollback-plan.schema.json
└── render-diff-report.schema.json
```

No nested directory is present in the inspected target tree. The inventory is exact for the pinned snapshot; it is not a claim about later commits.

## Complete schema inventory

| File | Confirmed machine behavior | Filename-implied concern only | Canonical destination |
|---|---|---|---|
| [`perf-envelope.schema.json`](./perf-envelope.schema.json) | Closed `PerfEnvelope` v1 configuration shape with exact identity/posture, five numeric thresholds, and bounded notes | Repository-owned threshold configuration, not a measurement or release object | **TRANSITIONAL PATH; CANONICAL DESTINATION NEEDS VERIFICATION** |
| [`perf-receipt.schema.json`](./perf-receipt.schema.json) | Accept any JSON object | Evaluation or execution receipt | **NEEDS VERIFICATION** |
| [`render-diff-report.schema.json`](./render-diff-report.schema.json) | Accept any JSON object | Render comparison report | **NEEDS VERIFICATION** |
| [`perf-proof-pack.schema.json`](./perf-proof-pack.schema.json) | Accept any JSON object | Proof or evidence aggregation | **NEEDS VERIFICATION** |
| [`perf-rollback-plan.schema.json`](./perf-rollback-plan.schema.json) | Accept any JSON object | Release rollback planning | **NEEDS VERIFICATION** |
| [`perf-failure-bundle.schema.json`](./perf-failure-bundle.schema.json) | Accept any JSON object | Failure triage or diagnostic bundle | **NEEDS VERIFICATION** |
| [`perf-release-manifest.schema.json`](./perf-release-manifest.schema.json) | Accept any JSON object | Release or promotion manifest | **NEEDS VERIFICATION** |
| [`perf-correction-notice.schema.json`](./perf-correction-notice.schema.json) | Accept any JSON object | Correction or withdrawal notice | **NEEDS VERIFICATION** |

The third column is vocabulary suggested by filenames, not confirmed semantics. Do not use it to generate payloads, APIs, schemas, validators, or release logic without an accepted contract and object-family review.

## Verified schema shapes

The seven trust-output schemas retain exactly this machine shape:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true
}
```

The envelope schema is distinct. It closes top-level and threshold objects,
requires the six known top-level members and five known threshold members,
constrains identity/posture to current v1 constants, requires positive timing
numbers, limits the pixel-delta ratio to `[0, 1]`, and bounds notes.

### What the seven placeholder shapes prove

- their bytes parse as JSON;
- their declared meta-schema URI is Draft 2020-12;
- non-object instances are rejected by the `type` keyword; and
- object instances with any property set are accepted by those seven schemas.

### What this does not prove

- canonical URI or final versioned-family placement;
- accepted benchmark units, sampling, environment, or threshold authority;
- source, layer, style, tile, renderer, browser, device, or environment identity;
- deterministic measurement method, sample size, baseline, tolerance, or comparison rules;
- evidence lineage, citations, hashes, signatures, review, or separation of duties;
- rights, sensitivity, consent, public-safety, or access-policy outcomes;
- promotion, release, rollback, correction, withdrawal, or publication state;
- compatibility with a consumer, API, package, adapter, workflow, or UI; or
- that any filename-implied object exists at runtime.

The common runner now gives meaningful machine assurance for `PerfEnvelope` v1
and only structural object assurance for the other seven files. Neither outcome
is runtime, evidence, policy, release, or publication assurance.

## Object-family and authority routing

Accepted Directory Rules provide a default versioned pattern, not an automatic destination for every historical filename. Each object must be routed according to its semantic aggregate and lifecycle boundaries.

### Adjacent versioned families

| Surface | Confirmed state | Safe use here |
|---|---|---|
| [`schemas/contracts/v1/map/`](../contracts/v1/map/README.md) | README plus 17 schema files; mixed maturity | Candidate adjacency for machine shapes whose accepted semantic aggregate is `map`, not a blanket destination for performance, proof, receipt, or release objects. |
| `map/layer_manifest.schema.json` | Proposed accept-any scaffold | No stronger than a placeholder for semantic assurance. |
| `map/style_manifest.schema.json` | Proposed accept-any scaffold | Does not prove style compilation, safety, or release. |
| `map/tile_artifact_manifest.schema.json` | Proposed accept-any scaffold | Does not prove tile generation, integrity, or publication. |
| `map/map_release_manifest.schema.json` | Substantive, strict, fixture-first `PROPOSED_INACTIVE` profile | Demonstrates a stronger machine-backed profile while explicitly denying activation. It does not absorb all MapLibre performance objects. |
| [`schemas/contracts/v1/layers/`](../contracts/v1/layers/README.md) | Shared layer schemas with permissive scaffolds and overlapping domain profiles | Requires bounded ownership and overlap review before any routing. |

### Required routing questions

Before moving or replacing any of the eight transitional schemas, reviewers must establish:

1. the semantic aggregate and canonical contract path;
2. the versioned schema family and stable `$id` policy;
3. the difference between configuration, observation, receipt, proof, decision, and release record;
4. the authoritative writer and authorized mutation model;
5. intended readers and actual existing consumers;
6. applicable rights, consent, sensitivity, security, and public-safety policy;
7. fixtures, validators, negative tests, and compatibility expectations;
8. promotion, release, correction, withdrawal, and rollback relationships;
9. retention and redaction requirements; and
10. migration, redirect, deprecation, and retirement evidence.

### Cross-family caution

The filename prefix `perf-` and the renderer name `maplibre` are not sufficient domain boundaries. A receipt may belong to a generic evaluation or evidence family; a proof pack may be evidence infrastructure; a release manifest, correction notice, and rollback plan may be release-governance objects. **INFERRED:** forcing all eight into one map-specific family would risk coupling renderer compatibility to cross-cutting trust and release semantics. Final placement remains **NEEDS VERIFICATION**.

## Governed responsibility flow

```mermaid
flowchart LR
  C[Contracts<br/>meaning and invariants] --> S[Reviewed versioned schemas<br/>machine shape]
  S --> V[Fixtures + validators + tests<br/>enforceability evidence]
  P[Policy<br/>allow / deny / restrict / abstain] --> G[Governed API + release gates]
  V --> G
  G --> R[Released, public-safe carriers]
  R --> M[MapLibre renderer and UI]
  L[schemas/maplibre/<br/>transitional schemas] -. compatibility and migration only .-> S
```

This diagram is a responsibility model. It is not proof that the proposed governed API, release gates, carrier pipeline, or MapLibre adapter are currently implemented.

### Renderer boundary

MapLibre may consume released styles, sources, tiles, overlays, interaction metadata, and public-safe presentation carriers. It must not independently decide:

- whether a source is authoritative or merely contextual;
- whether a claim is sufficiently evidenced;
- whether rights, consent, sensitivity, or disclosure policy permit exposure;
- whether a draft or reviewed object is promoted or released;
- whether a correction, withdrawal, or rollback is required; or
- whether an AI-generated suggestion is factual, approved, or publishable.

Those decisions belong upstream and require explicit records. Rendering is presentation, not governance.

## Source, layer, style, and performance separation

These concepts must remain distinguishable even when one workflow or UI touches all of them.

| Concern | Primary question | Required evidence before reliance |
|---|---|---|
| Source metadata | What is the source, lineage, role, rights posture, freshness, and access boundary? | Source contract, metadata schema, validation, and policy result |
| Layer definition | What geographic or thematic object is represented, at what scale and geometry? | Layer contract, versioned schema, fixtures, topology checks, and domain review |
| Style or presentation | How may released data be symbolized and interacted with? | Style contract, accessibility, disclosure, renderer compatibility, and release review |
| Tile or artifact | What generated carrier is addressed, hashed, bounded, and released? | Deterministic build evidence, integrity, provenance, and release manifest |
| Performance observation | Under which reproducible environment were metrics measured? | Identified environment, method, samples, baselines, tolerances, and raw evidence |
| Render comparison | What images or scene states were compared and under which deterministic rules? | Baseline identity, captured output, algorithm, thresholds, and reviewed result |
| Receipt or proof | What evaluation occurred, against which inputs and rules, with what outcome? | Immutable identifiers, hashes, validator version, finite outcome, and reviewer trace |
| Release or correction | What changed operational state, who authorized it, and how can it be reversed? | Accepted gate result, separation of duties, release record, correction/rollback path |

Passing one concern must not silently satisfy another.

## What belongs here

While this transitional lane remains tracked, acceptable changes are limited to:

- this evidence-bounded README;
- reviewed compatibility notes tied to exact source and destination identities;
- explicit deprecation or redirect metadata authorized by an accepted migration;
- dependency-closed constraints for a verified existing repository-owned
  configuration consumer, with fixtures, tests, workflow checks, and explicit
  non-authority boundaries;
- temporary compatibility schemas only when an accepted decision requires them and their authority is clearly subordinate; and
- machine-verifiable exit criteria and removal evidence.

Any retained compatibility file must state its status, canonical destination,
allowed readers, write prohibition, sunset criteria, and rollback plan. The seven
placeholders do not yet satisfy that future standard; the closed envelope schema
still has unresolved canonical destination and migration criteria.

## What does not belong here

Do not place or author the following in this directory:

- semantic contracts or prose that creates contract meaning;
- normative policy bundles or allow/deny decisions;
- configuration instances, thresholds, environment profiles, or secrets;
- fixtures, snapshots, screenshots, golden images, metrics, traces, or runtime logs;
- validators, test code, workflows, browser harnesses, or benchmark runners;
- source, layer, style, tile, or release payload instances;
- receipts, proof packs, evidence bundles, attestations, signatures, or audit logs;
- release manifests, correction notices, withdrawal records, or rollback executions;
- generated artifacts, public exports, tiles, reports, dashboards, or map applications; or
- executable package, adapter, API, renderer, or UI code.

The presence of similarly named schema placeholders is not a precedent for storing their instances here.

## Compatibility rules

1. **Single-write authority.** New authoritative schema work goes to the reviewed versioned family. This lane must not evolve independently.
2. **No new binding to placeholders.** New code, workflows, contracts, or APIs
   must not bind to the seven open shapes. New consumers of the envelope require
   compatibility and canonical-placement review.
3. **Dual-read only when approved.** A migration may temporarily read old and new shapes only when an accepted plan defines precedence, telemetry, error handling, duration, and exit criteria.
4. **No silent coercion.** Unknown or invalid legacy fields must fail closed or produce a bounded migration error; they must not be silently reinterpreted.
5. **Identity before redirect.** A redirect or compatibility `$ref` requires stable source and destination identities, version rules, cycle checks, and fixture-backed validation.
6. **No schema copy drift.** Copying a versioned schema into this lane creates parallel authority unless the compatibility mechanism is explicitly generated and checked.
7. **No maturity laundering.** Renaming a placeholder, adding a `$id`, or making CI green does not make semantics accepted or runtime implemented.
8. **Consumer closure before retirement.** Deletion requires exact reference search, runtime and workflow consumer evidence, documentation repair, rollback, and accepted change control.

## Consumer rules

### New consumers

New consumers are prohibited for the seven permissive placeholders. Any new
envelope consumer must either bind to a reviewed versioned schema or explicitly
close the transitional compatibility obligations with:

- an accepted semantic contract;
- stable identity and version rules;
- valid and invalid fixtures;
- executable validation and negative tests;
- explicit unknown-field and forward-compatibility behavior;
- finite outcomes and fail-closed policy behavior;
- evidence and release relationships; and
- an accountable owner and review path.

### Existing consumers

The complete existing consumer set is **UNKNOWN**. Before changing a filename or shape, search at minimum:

- source code and package imports;
- scripts, validators, tests, fixtures, and configuration;
- workflow path filters and command lines;
- docs, ADRs, root registries, catalogs, and generated indexes;
- release, evidence, receipt, and artifact builders; and
- externally documented APIs or integration instructions.

Reference presence is not consumer proof, and absence from a simple text search is not sufficient closure. Dynamic path construction, generated code, workflow matrices, and external clients may require separate evidence.

### Public and runtime clients

Browser, API, and MapLibre clients must receive only governed, released, public-safe carriers. They must not consume draft schema repositories as content stores or use local schema validity as an authorization result.

## Inputs, outputs, writers, and consumers

This directory currently describes machine-shape placeholders; it is not an event-processing component.

| Interface | Current evidence-backed posture |
|---|---|
| Inputs | Repository commits and reviews that change these nine tracked files. No runtime payload input is authorized here. |
| Outputs | JSON Schema bytes and this documentation. Validating an object against the current schema can only establish that it is an object. |
| Writers | Git contributors subject to repository review. Accepted stewardship and independent approval remain **NEEDS VERIFICATION**. |
| Readers | Validators, workflows, tests, scripts, docs, and potential external clients may reference these paths; the complete set is **UNKNOWN**. |
| Mutations | Git history only. Runtime mutation, in-place evidence edits, or generated artifact writes do not belong here. |
| Side effects | None are authorized. A schema read or validation result must not promote, release, publish, delete, notify, or mutate external state. |

### Non-effects contract

Neither this README nor any current schema in this directory may be used as sufficient evidence that:

- a payload is truthful, authoritative, complete, current, or fit for use;
- a benchmark ran or passed;
- a render diff was captured or reviewed;
- an evidence bundle, proof pack, or receipt is trustworthy;
- rights, consent, sensitivity, or security checks passed;
- an object was promoted, released, published, corrected, withdrawn, or rolled back; or
- a MapLibre view is safe for public access.

## Security, privacy, exposure, and retention

Schema repositories are public and must not contain secrets, credentials, access tokens, private endpoints, personal data, restricted coordinates, unpublished vulnerabilities, signed private evidence, or production traces.

Any future object family must explicitly classify:

- identifier sensitivity and linkability;
- location precision and re-identification risk;
- source licensing, consent, and redistribution limits;
- environment and device fingerprints;
- screenshot or render contents;
- failure details and security-sensitive diagnostics;
- signature, attestation, and key-reference handling;
- retention, correction, withdrawal, legal hold, and deletion rules; and
- public, restricted, and internal projections.

Schema shape must not embed policy outcomes as defaults. Exposure decisions require policy evaluation and release-state evidence outside this directory.

## Validation and negative checks

Validation is layered. A green lower layer must not be reported as a green higher layer.

| Layer | Required check | Current posture |
|---|---|---|
| Inventory | Exactly one README plus the eight named direct schemas | **CONFIRMED** at the pinned tree |
| JSON syntax | Parse each schema as JSON | **CONFIRMED** |
| Meta-schema | Validate each schema against Draft 2020-12 | **CONFIRMED by source/workflow posture** |
| Identity | Unique stable `$id`, version, title, status, and metadata | Envelope payload version/title implemented; canonical `$id` and seven placeholder identities **HOLD** |
| Semantic shape | Required fields, constraints, cross-field rules, units, and outcomes | Envelope machine shape implemented; benchmark semantics and seven trust-output shapes **HOLD** |
| Fixtures | Representative valid, invalid, edge, privacy, and migration cases | Envelope has two valid and fourteen invalid synthetic cases; broader families **HOLD** |
| Validator | Bounded executable validator with finite outcomes | Eight runner entrypoints; envelope has cwd-independent fixture binding; broader verifiers held |
| Negative paths | Demonstrate rejection of invalid and unsafe inputs | Envelope contract suite plus fourteen negative fixtures; separate scalar tests retained |
| Runtime | Browser, renderer, device, network, and environment execution | **NOT EXECUTED by the inspected perf workflow** |
| Evidence | Hashes, provenance, logs, receipts, signatures, and review | **NOT PRODUCED for these schemas by the inspected workflow** |
| Policy and release | Governed decision, separation of duties, promotion, correction, rollback | **NOT ESTABLISHED** |

### Documentation checks for this README

Run from repository root:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . --profile required schemas/maplibre/README.md

python tools/validators/docs/stale-scan/check_stale_docs.py \
  --repo-root . --as-of 2026-09-08 --profile bounded-required \
  schemas/maplibre/README.md

python tools/validators/docs/link-check/check_links.py \
  --repo-root . schemas/maplibre/README.md
```

Also verify:

- exactly one H1 and a monotonic heading structure;
- the metadata block is first and complete;
- every relative link resolves at the reviewed commit;
- the direct-child map matches the Git tree;
- all eight schema contents and current identities are rechecked;
- Markdown renders without broken tables, alerts, code fences, anchors, or Mermaid syntax; and
- the no-loss and evidence ledgers are updated.

### Schema and wrapper checks

All eight entrypoints exercise the common JSON Schema runner. The envelope
entrypoint additionally binds reviewed positive/negative fixture lanes and uses
repository-rooted paths; the other seven still validate only the placeholder
object shape. This distinction is enforced by workflow inventory checks.

Future schema promotion must add, at minimum:

- a stable `$id` and version policy;
- an accepted paired contract;
- strict or explicitly justified unknown-field behavior;
- valid, invalid, boundary, malicious, privacy-sensitive, compatibility, and rollback fixtures;
- tests that prove every normative constraint rejects counterexamples;
- deterministic output and finite validator outcomes;
- no-network or explicitly bounded-network execution;
- consumer compatibility evidence; and
- promotion and release checks separate from validation.

## Current CI and readiness boundary

### MapLibre performance-governance workflow

The inspected [workflow](../../.github/workflows/maplibre-perf-governance.yml) includes `schemas/maplibre/**` in its path filters. It currently:

- checks JavaScript syntax for seven MapLibre scripts;
- parses the MapLibre Python validator surface;
- invokes three scalar negative-path, three retirement, and three package-export tests directly;
- checks readiness-inventory drift;
- checks one closed envelope schema/config/fixture inventory and seven exact placeholder schemas;
- asserts that eight schema wrappers and seven broader placeholder verifiers retain their expected maturity;
- reviews the exact `maplibre-gl` 6.6.0 package and workspace lock posture; and
- emits explicit skip and hold records.

The general `schema-validation` workflow installs declared Python dependencies,
validates the tracked envelope plus both fixture polarities, and runs the nine
focused contract tests. This closes machine validation without adding a browser
or changing the performance hold.

It does **not** install a browser, start a server, exercise a MapLibre renderer, capture screenshots, measure frames or memory, compare renders, validate a real receipt or proof pack, sign an attestation, upload governed artifacts, promote a release, publish a map, issue a correction, or execute rollback.

### Latest applicable hosted run

Historical [run `31654973078`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31654973078)
concluded `success` while recording `WORKFLOW_SKIPPED_EXPLICIT` and
`WORKFLOW_HOLD`. Exact-head hosted results for this change are pending.

Safe conclusion:

```text
workflow definition and readiness guard executed successfully
≠ browser benchmark executed
≠ performance envelope satisfied
≠ render parity established
≠ proof or attestation accepted
≠ release approved
≠ artifact published
```

The hold is a designed outcome, not a hidden failure and not permission to bypass missing stages.

### Adjacent workflows

- Historical source-metadata run `30958539690` validates a separate local
  projection; it does not establish envelope or trust-output semantics.
- Historical schema/validator run IDs in v0.3 remain provenance only. Current
  local results and exact-head PR checks must be evaluated independently.

Those current-main failures are repository-level preflight evidence. A change to this README must still run its own PR checks, and any failure must be compared by exact job, log, and fingerprint before it is called inherited. Documentation must not normalize, conceal, or relabel a failing required check.

## Safe change workflow

1. Pin the current base commit, target tree, README blob, and all eight schema contents.
2. Search open pull requests and active branches for overlapping target changes.
3. Re-read accepted ADR-0029, the exact adopted Directory Rules bytes, the schema-root README, and relevant proposed ADRs.
4. Classify every assertion as **CONFIRMED**, **INFERRED**, **PROPOSED**, **UNKNOWN**, **NEEDS VERIFICATION**, or **HOLD**.
5. Identify the semantic aggregate and object-family owner before proposing a schema destination.
6. Inspect existing consumers, workflows, validators, tests, fixtures, configuration, evidence builders, release tooling, and docs.
7. Keep validation separate from policy, promotion, release, publication, correction, and rollback.
8. Update one focused branch with the README and its traceability receipt only.
9. Run metadata, staleness, link, structure, rendering, and repository-specific checks.
10. Open a draft pull request; inspect every PR check and disclose held or inherited failures precisely.
11. Require explicit review before any schema, consumer, workflow, runtime, or migration change.

If evidence is incomplete or authority conflicts, stop at **HOLD**.

## Compatibility, migration, and retirement

### Required migration sequence

1. **Inventory:** prove the old paths, exact bytes, references, consumers, writers, readers, and generated dependencies.
2. **Contract:** accept the semantic aggregate, invariants, lifecycle, evidence, and correction model.
3. **Placement:** approve the versioned schema family and identity/version strategy.
4. **Implementation:** author machine shape, fixtures, validators, negative tests, and documentation.
5. **Consumer proof:** demonstrate intended consumers on the new version and characterize legacy behavior.
6. **Compatibility:** if required, implement bounded dual-read/single-write behavior with telemetry and expiry.
7. **Promotion:** run separate policy and release gates; validation alone cannot promote.
8. **Redirect or tombstone:** preserve discoverability and fail clearly for unsupported use.
9. **Retirement:** remove only after reference, runtime, workflow, documentation, and rollback closure.

### Promotion gates

No placeholder may be described as implemented or promoted until all of the following are recorded:

- accepted semantic contract and versioned placement;
- accountable owner and independent review path;
- non-permissive machine constraints or an explicit, reviewed reason for extensibility;
- stable identity and compatibility rules;
- representative positive and negative fixtures;
- executable validators and tests with deterministic outcomes;
- security, privacy, rights, consent, sensitivity, and retention review;
- real consumer and runtime evidence where applicable;
- evidence and receipt design that does not self-attest;
- release, correction, withdrawal, and rollback controls; and
- a decision record that changes maturity without rewriting history.

### Retirement gates

Deletion remains **HOLD** until an accepted record proves:

- the canonical destination for every object;
- no unauthorized writes remain;
- all consumers migrated or were intentionally retired;
- no workflow, tool, fixture, config, doc, or external integration requires the old path;
- redirects or tombstones satisfy compatibility needs;
- release and rollback procedures are tested; and
- documentation, registries, catalogs, and receipts are repaired.

## Review burden and escalation

| Change | Minimum review burden |
|---|---|
| README wording only | Schema-root documentation review; verify truth labels, links, inventory, non-effects, and no-loss ledger |
| Placeholder metadata or `$id` | Schema steward, contract steward, identity/version review, consumer search, fixtures, validators, and negative tests |
| Field or constraint change | Accepted contract evidence, schema review, compatibility analysis, consumer tests, migration and rollback plan |
| New or changed receipt/proof shape | Evidence and security review; prevent self-attestation and distinguish observation from decision |
| Release/correction/rollback object | Release governance, separation of duties, policy review, immutable history, and tested reversal path |
| Validator or workflow change | Validator, CI, security, and domain review; prove finite outcomes and distinguish success from hold |
| Runtime or MapLibre binding | Adapter, governed API, renderer, accessibility, privacy, policy, release, and operational review |
| Redirect, tombstone, or deletion | Accepted migration decision, consumer closure, reference closure, documentation repair, and rollback evidence |

Escalate when object-family ownership conflicts, a compatibility reader could become a writer, public exposure is possible, a receipt can authorize its own action, a workflow masks skipped stages, or a proposed change weakens a fail-closed outcome.

## Definition of done

### This README revision

- [x] Metadata block updated with a current evidence snapshot.
- [x] Accepted ADR-0029 distinguished from proposed ADRs.
- [x] Exact direct-child tree and all eight files recorded.
- [x] One closed envelope schema and seven shared placeholder shapes recorded.
- [x] Semantic, policy, evidence, release, and renderer non-effects stated.
- [x] Adjacent map and layer families described without assigning all objects to them.
- [x] Workflow success distinguished from `WORKFLOW_HOLD` and unexecuted stages.
- [x] Contributor, migration, review, correction, and rollback controls preserved and strengthened.
- [x] Open verification and no-loss ledgers included.
- [ ] Human review and acceptance of this documentation change.

### Executable and migration maturity

- [ ] Accepted semantic contract exists for each object.
- [ ] Canonical versioned family and stable identity are approved.
- [ ] Accountable owner, consumers, and separation of duties are recorded.
- [x] Strict machine constraints are implemented for the bounded envelope configuration only.
- [x] Positive, boundary, and negative envelope fixtures exist; privacy, migration, and rollback fixtures for trust-output families remain held.
- [x] The envelope validator and tests prove its normative machine constraints; the other seven families remain held.
- [ ] Browser, renderer, benchmark, and render-diff stages run where applicable.
- [ ] Evidence, proof, receipt, attestation, and reviewer boundaries are implemented without self-approval.
- [ ] Policy, promotion, release, correction, withdrawal, and rollback gates are separate and tested.
- [ ] Compatibility readers, telemetry, exit criteria, and retirement evidence are complete.

The first checklist can complete while the second remains entirely held. Documentation quality does not imply implementation maturity.

## Open verification register

| ID | Question | Required evidence | Current action |
|---|---|---|---|
| MAPLIBRE-SCHEMA-001 | Who is accountable for this compatibility lane and each destination family? | Accepted ownership record and review path | **HOLD new authority claims** |
| MAPLIBRE-SCHEMA-002 | Which semantic contract owns each of the eight objects? | Contract inventory and accepted aggregate mapping | **HOLD schema promotion** |
| MAPLIBRE-SCHEMA-003 | Which versioned schema family is canonical for each object? | Accepted placement decision and stable `$id` plan | **HOLD migration** |
| MAPLIBRE-SCHEMA-004 | Which code, workflows, tools, fixtures, docs, or external clients consume the old paths? | Repository-wide and integration consumer inventory | **HOLD rename or deletion** |
| MAPLIBRE-SCHEMA-005 | What is configuration versus observation versus receipt versus proof versus release record? | Lifecycle model with writers, readers, immutability, and correction rules | **HOLD payload authoring** |
| MAPLIBRE-SCHEMA-006 | Which benchmark environments, baselines, tolerances, and sampling rules are accepted? | Reproducible performance contract and fixtures | **HOLD performance claims** |
| MAPLIBRE-SCHEMA-007 | What constitutes an accepted render comparison? | Deterministic capture and diff protocol with reviewed baselines | **HOLD parity claims** |
| MAPLIBRE-SCHEMA-008 | Which rights, consent, sensitivity, privacy, and public-safety controls apply? | Policy profiles, tests, decisions, and public projections | **HOLD exposure** |
| MAPLIBRE-SCHEMA-009 | How are proof and receipt records protected from self-attestation or mutation? | Evidence architecture, signer/reviewer boundaries, hashes, and append-only correction | **HOLD trust claims** |
| MAPLIBRE-SCHEMA-010 | What promotes, releases, corrects, withdraws, and rolls back a MapLibre artifact? | Accepted release workflow and tested records | **HOLD release** |
| MAPLIBRE-SCHEMA-011 | When can the old paths be redirected, tombstoned, or removed? | Consumer closure, compatibility expiry, documentation repair, and rollback evidence | **HOLD retirement** |
| MAPLIBRE-SCHEMA-012 | Do current PR checks reproduce or change the known topology failures? | PR run IDs, job logs, fingerprints, and base comparison | **VERIFY on every PR** |

## Review checklist

- [ ] The base commit, target tree, prior README blob, and eight schema contents were rechecked immediately before publication.
- [ ] No open pull request overlaps `schemas/maplibre/README.md`.
- [ ] Relative links resolve against the proposed commit.
- [ ] The direct-child map still matches the target tree.
- [ ] No proposed ADR is presented as accepted.
- [ ] No architecture source is presented as current implementation proof.
- [ ] No filename-implied semantics are presented as confirmed contract meaning.
- [ ] No workflow conclusion is presented without its explicit skipped and held stages.
- [ ] No owner, consumer, schema destination, runtime behavior, release state, or publication claim is invented.
- [x] The bounded schema/validator/fixture/test/workflow changes are disclosed; runtime code, artifacts, policy, and release state are unchanged.
- [ ] Documentation and traceability checks pass or are disclosed precisely.
- [ ] Human reviewers confirm the evidence snapshot and non-effects contract.

## No-loss ledger

| Prior concern | v0.4 disposition |
|---|---|
| Purpose and non-authoritative compatibility posture | Preserved and strengthened with accepted Directory Rules authority. |
| Status and truth labels | Preserved; added **INFERRED** and **HOLD**, current Git and hosted-run evidence, and removed the obsolete placement conflict. |
| Boundary: may and must not | Preserved across `What belongs here`, `What does not belong here`, compatibility rules, and non-effects. |
| Repository fit and placement basis | Preserved as direct-child map, authority inheritance, adjacent versioned families, and responsibility routing. |
| Exact inventory and completeness boundary | Preserved and upgraded to the exact target-tree inventory. |
| Verified schema shape | Reconciled to one closed envelope schema and seven byte-identical placeholders, with proof/non-proof limits preserved. |
| Object-family and cross-family caution | Preserved; made explicit that `map` is adjacency rather than a blanket destination. |
| Compatibility and consumer rules | Preserved; added single-write, dual-read constraints, identity, telemetry, and consumer closure. |
| Validation, narrow tests, and wrappers | Preserved; separated structural, semantic, runtime, evidence, policy, and release layers. |
| Current workflow boundary and held conditions | Updated for mixed schema maturity and exact-head checks while preserving explicit runtime/performance holds. |
| Migration and promotion gates | Preserved; expanded into ordered migration, promotion, and retirement gates. |
| Review burden | Preserved and expanded by change class and escalation trigger. |
| Definition of done | Preserved; split documentation completion from executable and migration maturity. |
| Open questions | Preserved as a numbered verification register with required evidence and hold action. |
| Evidence ledger | Preserved and updated to the current repository, workflow, implementation, and supplied-reference snapshot. |
| Correction and rollback | Preserved and expanded below. |

No v0.2 operational capability is removed because v0.2 documented boundaries rather than implemented capabilities. Statements made stale by accepted ADR-0029 or newly available run evidence are corrected explicitly rather than silently carried forward.

## Evidence ledger

| Evidence | Observation used | Limits |
|---|---|---|
| `main@b30210971c41073a9a2e36b5a0d7d451ef43d592` | Pinned implementation base for this revision | Later commits require re-verification |
| Repository tree `2e648bd3db2ee9891eec31c897cf71cff08f06bb` | Base tree identity | Does not independently explain semantics |
| Target tree `510adad583cedefd90c116e44e85a5e35f5e61d3` | Exact README-plus-eight-schema inventory | Direct target only |
| Prior README blob `9560ed016077964b56988d7fb4c02fe34e42fb28` | v0.2 source preserved through no-loss review | Prior claims may be stale |
| Historical shared schema blob `511e7f34ca84390fd5d000326ab33c46c3050fc4` | Pre-change all-placeholder baseline; seven files retain this shape | Historical comparison, not semantic maturity |
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and adopted doctrine blob `fd49a0b83e55cef52c1124281f093e263526898d` | Accepted responsibility and placement rules | Does not choose every object family |
| [`schemas/README.md`](../README.md) | Parent classification of this lane and maturity posture | Documentation, not runtime proof |
| [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Proposed schema-home and migration context | Not accepted |
| [ADR-0004](../../docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md) | Proposed governed API boundary | Not accepted implementation proof |
| [`schemas/contracts/v1/map/`](../contracts/v1/map/README.md) and [`layers/`](../contracts/v1/layers/README.md) | Adjacent versioned families with mixed maturity | Do not absorb all eight objects automatically |
| `packages/maplibre/package.json` and workspace lock | Exact package-owned MapLibre GL JS 6.6.0 dependency | Dependency closure, not runtime readiness |
| [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | Static readiness, mixed schema maturity, fixture classification, explicit skip and hold | No browser or release execution |
| Hosted run `31654973078`, job `94307343990` | Latest applicable reviewed main run: success plus explicit hold | Snapshot in time; not a release receipt |
| Hosted source-metadata run `30958539690` | Separate projection checks succeeded | Does not validate the performance-envelope contract |
| Hosted current-main runs `31758530911` and `31758530894` | Repository-topology ratchet failed after earlier checks | Must be compared with PR runs before calling inherited |
| `configs/maplibre/perf-envelope.v1.json` historical blob `2833f99b5316df91e71c0f8913bb06d70917abcf` | Threshold values remain unchanged and now pass the closed v1 schema | Machine validity only |
| MapLibre validator, fixture, and test trees | Envelope fixture-bound runner and focused tests; seven held verifiers; separate scalar/source/readiness lanes | Mixed scope; no runtime proof |
| Supplied MapLibre operating manual | Architecture lineage: MapLibre downstream of governance and release | Corpus source only; not repository implementation evidence |
| Supplied MapLibre component atlas | Separates confirmed source evidence from proposed implementation and denies publication by file presence | Corpus source only; not acceptance or runtime proof |

## Correction and rollback

If this README is wrong, stale, or overclaims maturity:

1. stop new reliance on the disputed statement or path;
2. open a focused correction that identifies the exact claim, evidence, and affected consumers;
3. restore the last reviewed documentation bytes when that is the safest reversible action;
4. do not rewrite or delete receipts, workflow logs, release records, or Git history;
5. add a superseding correction record when an append-oriented evidence surface is involved;
6. re-run metadata, staleness, link, inventory, schema, and relevant CI checks;
7. reassess any migration, consumer binding, promotion, release, publication, or retirement decision that depended on the claim; and
8. keep runtime rollback, data correction, release withdrawal, and schema compatibility as distinct procedures.

Rolling back this README restores documentation only. It does not roll back schema bytes, consumers, validators, workflows, packages, adapters, releases, public artifacts, or external integrations.

---

**Last evidence review:** 2026-09-08 · **Document version:** v0.4 · **Implementation posture:** one closed configuration schema; seven placeholders; migration and runtime readiness held

[Back to top](#top)
