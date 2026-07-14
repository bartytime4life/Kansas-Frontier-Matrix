<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-habitat-readme
title: configs/domains/habitat/ — Governed Habitat Configuration Boundary
type: readme
version: v0.4
status: draft
owners:
  - OWNER_TBD — Config steward
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Source and rights steward
  - OWNER_TBD — Model and method steward
  - OWNER_TBD — Sensitivity and geoprivacy steward
  - OWNER_TBD — Consumer owner
  - OWNER_TBD — Validation and policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-16
updated: 2026-07-14
policy_label: "public; config-sublane; habitat; landscape-not-species; source-role-aware; model-aware; regulatory-aware; rights-aware; sensitivity-aware; geoprivacy-aware; reconstruction-resistant; deny-by-default; non-secret; non-authoritative; no-live-binding; no-source-activation; no-policy-authority; no-release-authority"
current_path: configs/domains/habitat/README.md
truth_posture: CONFIRMED current Habitat config README and empty .gitkeep, parent domain-config contract, Habitat doctrine, bounded absence of an indexed executable config consumer, Habitat package version 0.0.0 and empty initializer, placeholder Habitat pipelines and validators, permissive Habitat object schemas, draft Habitat contracts, policy scaffolds, TODO-only domain workflow, subtype-first and domain-first Habitat source-registry lanes, singular triplet compatibility lane, and biotopes compatibility roots / PROPOSED future consumer-bound templates and profile selectors / CONFLICTED seven-role Habitat vocabulary versus richer SourceDescriptor schema vocabulary, HabitatPatch duplicate contract paths, SuitabilityModel path aliases, ModelRunReceipt placement aliases, subtype-first versus domain-first registry topology, Habitat-owned versus generic trust-object schema placement, and compatibility biotopes paths / UNKNOWN consumer wiring, loader behavior, precedence, deployment binding, model execution, policy-runtime wiring, release integration, and production behavior / NEEDS VERIFICATION accepted owners, canonical object paths, source-role mapping, schema and validator authority, source rights, model fitness, sensitivity profiles, geoprivacy parameters, executable validation, correction propagation, derived-output invalidation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  authoring_base_commit: 47ccfa02de783c1cb90609d7d79a3d316082ec6b
  branch_base_commit: 8bb1d0b8b288781169e5592d60962cd7537fc37c
  prior_blob: a34dc7b95b99691f0cfa538ee5bf9e4ef536bedc
  lane_inventory:
    - README.md
    - .gitkeep
  bounded_consumer_search:
    - configs/domains/habitat/README.md
    - configs/domains/README.md
    - docs/domains/habitat/FILE_SYSTEM_PLAN.md
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/IDENTITY_MODEL.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/biotopes/README.md
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../schemas/biotopes/README.md
  - ../../../policy/domains/habitat/
  - ../../../policy/biotopes/README.md
  - ../../../packages/domains/habitat/
  - ../../../pipelines/domains/habitat/
  - ../../../pipeline_specs/habitat/
  - ../../../tools/validators/domains/habitat/
  - ../../../data/registry/sources/habitat/
  - ../../../data/registry/habitat/sources/
  - ../../../data/triplet/habitat/README.md
  - ../../../data/triplets/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../.github/workflows/domain-habitat.yml
tags: [kfm, configs, habitat, land-cover, ecological-systems, habitat-patch, suitability, connectivity, corridors, restoration, stewardship, source-role, rights, sensitivity, geoprivacy, models, no-secrets, governance]
notes:
  - "v0.4 preserves the v0.3 no-secrets, no-authority, source-role, model/regulatory, sensitivity, geoprivacy, migration, correction, and rollback controls."
  - "v0.4 adds current repository maturity, package/pipeline/schema/policy/validator/workflow evidence, source-role vocabulary conflict, object-path aliases, registry topology, generic trust-object duplication safeguards, biotopes compatibility posture, and downstream invalidation requirements."
  - "The bounded config-path search returned the target README, the parent README, and a Habitat file-system planning document; no indexed executable consumer was observed."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Habitat Domain Configuration

`configs/domains/habitat/`

> Safe-to-commit configuration documentation and future consumer-bound templates for Habitat processing, model presentation, review routing, public-safe representation, and conservative failure behavior. This lane does not own Habitat truth, species truth, source admission, policy, evidence, lifecycle state, release, or publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.4-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README%20%2B%20.gitkeep-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitivity-fail__closed-critical)
![models](https://img.shields.io/badge/models-not__observations-purple)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Vocabulary](#bounded-context-and-ubiquitous-language) · [Classes](#configuration-classes) · [Contract](#minimum-per-file-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#habitat-object-family-boundaries) · [Roles](#source-role-vocabulary-and-anti-collapse) · [Semantics](#observation-model-regulatory-and-administrative-boundaries) · [Space](#spatial-support-geometry-scale-and-public-safe-representation) · [Time](#time-freshness-stale-state-and-correction) · [Sensitivity](#rights-sensitivity-geoprivacy-and-join-induced-risk) · [Sources](#source-registry-connector-and-activation-boundaries) · [Maturity](#implementation-and-governance-maturity) · [Compatibility](#compatibility-and-parallel-authority-guardrails) · [Invalidation](#logging-caches-tiles-indexes-exports-and-derived-output-invalidation) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-supersession-and-invalidation) · [Done](#definition-of-done-for-the-first-payload) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Document status:** draft `v0.4`  
> **Repository evidence snapshot:** authored from `main@47ccfa02de783c1cb90609d7d79a3d316082ec6b`; target rechecked unchanged at branch base `main@8bb1d0b8b288781169e5592d60962cd7537fc37c`  
> **Observed lane maturity:** `README.md` plus a non-semantic empty `.gitkeep`; no executable Habitat configuration payload or consumer binding is established  
> **Authority:** reusable configuration support only; no truth, source, schema, contract, policy, evidence, review, release, or public authority  
> **Default runtime posture:** not loaded, not active, and not safe to assume consumed

> [!CAUTION]
> Habitat owns landscape context, not species occurrence. A modeled suitability surface is not a regulatory critical-habitat designation. A habitat patch is not a Fauna or Flora occurrence. A stewardship zone is not land-title truth. A valid configuration value is not a policy decision, EvidenceBundle, release manifest, or publication instruction. Exact or reconstructable sensitive Habitat and occurrence-linked context fails closed.

---

## Purpose

`configs/domains/habitat/` is the Habitat-specific configuration sublane under the canonical `configs/` responsibility root.

It exists to make safe defaults, placeholder-based templates, review-oriented examples, and configuration-facing documentation inspectable for a **named and verified consumer**. A good file here describes how already-governed Habitat material should be parsed, labeled, routed, rendered, cached, or reviewed without turning configuration into hidden authority.

A future file may support:

- selecting an already-accepted object, source-role, model, temporal, spatial, sensitivity, or public-safe representation profile;
- conservative thresholds whose semantics and intended use are defined outside this lane;
- review routing, hold behavior, abstention posture, and public-safe display preferences;
- explicit parser, precedence, deactivation, correction, and rollback behavior;
- deterministic no-network examples and tests.

It must not establish:

- what a Habitat object means;
- whether a source is admitted, active, rights-cleared, current, or authoritative;
- whether a model is correct, calibrated, current, or fit for a use;
- whether a habitat feature is observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic;
- whether a Fauna or Flora occurrence may be exposed;
- whether exact or generalized geometry is safe;
- whether evidence supports a claim;
- whether policy permits access, use, display, export, indexing, or publication;
- whether an artifact is released or public.

[Back to top](#top)

---

## Authority level

**Implementation-supporting configuration sublane; non-authoritative for truth and governance.**

| Concern | Authority in this lane |
|---|---|
| Folder placement and config boundary | **Supporting.** This README documents an existing child lane under `configs/domains/`. |
| Habitat domain meaning | **None.** Human-facing doctrine belongs to `docs/domains/habitat/`. |
| Habitat object meaning | **None.** Semantic authority belongs to accepted contracts. |
| Machine shape | **None.** JSON Schema and generated type authority belong to accepted schema roots. |
| Source identity, role, rights, cadence, and activation | **None.** Source registries, SourceDescriptors, admission decisions, connectors, and policy own those concerns. |
| Model meaning, method, calibration, and fitness | **None.** Model cards, contracts, run receipts, validation, evidence, and review own those concerns. |
| Sensitivity, geoprivacy, redaction, and exposure | **None.** Configuration may reference an accepted profile; it cannot create, weaken, or approve one. |
| Evidence and claim support | **None.** Configuration cannot create an `EvidenceBundle`, prove a claim, or promote generated language to truth. |
| Lifecycle and catalog/triplet state | **None.** Configuration cannot admit, promote, catalog, graph, publish, or mutate lifecycle records. |
| Policy and finite public outcome | **None.** Policy/runtime surfaces own allow, restrict, hold, abstain, deny, answer, and error decisions. |
| Release, correction, withdrawal, and rollback | **None.** Release roots own publication decisions and public correction state. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through an explicit binding and precedence contract. |

A config file may reference authority-bearing objects. It does not acquire their authority through proximity, repetition, parsing success, a friendly filename, deployment convenience, or use by a map, dashboard, model, cache, index, export, Evidence Drawer, Focus Mode, or AI surface.

[Back to top](#top)

---

## Status

### Repository snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Authoring evidence base | `47ccfa02de783c1cb90609d7d79a3d316082ec6b` |
| Branch base after unrelated drift | `8bb1d0b8b288781169e5592d60962cd7537fc37c` |
| Prior target blob | `a34dc7b95b99691f0cfa538ee5bf9e4ef536bedc` |
| Current target revision | documentation-only v0.4 |
| Direct lane files | `README.md`, empty `.gitkeep` |

### Current repository evidence

| Surface | Evidence | State | Safe conclusion |
|---|---|---:|---|
| Target lane | README and empty `.gitkeep` are present. | **CONFIRMED** | No executable payload, binding, or activation follows from directory presence. |
| Parent domain-config boundary | Parent README defines domain config as safe, non-secret, non-authoritative support. | **CONFIRMED** | This child must not become an authority lane. |
| Indexed config consumer search | Search returned this README, the parent README, and a Habitat file-system plan. | **NOT OBSERVED / search-limited** | No indexed executable consumer was found; exhaustive absence is not claimed. |
| Habitat doctrine | Human-facing Habitat README is repository-present. | **CONFIRMED doctrine / implementation mixed** | Landscape-not-species, model/regulatory separation, and source-role anti-collapse remain controlling concepts. |
| Habitat package metadata | `kfm-domain-habitat`, version `0.0.0`. | **CONFIRMED greenfield placeholder** | Package identity exists; implementation maturity is not established. |
| Habitat package initializer | Empty `src/habitat/__init__.py`. | **CONFIRMED scaffold** | No exports or initialization behavior are established. |
| Habitat package source | Indexed search returned source READMEs, not implementation modules. | **NOT OBSERVED / search-limited** | Reusable Habitat helper behavior is not established. |
| Habitat pipelines | Inspected NLCD ingest, patch builder, and suitability runner files contain only PROPOSED placeholder docstrings. | **CONFIRMED placeholders** | No ingestion, patch-building, or model execution is established. |
| Habitat package/pipeline READMEs | Detailed planning and responsibility boundaries exist. | **CONFIRMED documentation** | Documentation does not prove implementation. |
| Habitat object schemas | Inspected HabitatPatch and SuitabilityModel schemas have empty properties and allow additional properties. | **CONFIRMED permissive scaffolds** | Passing those schemas would not prove field-complete Habitat semantics. |
| Habitat contracts | Detailed draft contracts exist for object families. | **CONFIRMED draft semantic guidance** | Contract aliases and field-level realization remain unresolved. |
| Habitat policy | Policy README and Rego files exist; inspected modules are greenfield/generated scaffolds with inconsistent default forms. | **CONFIRMED scaffolds / enforcement NOT ESTABLISHED** | Do not treat a policy filename or a green run as policy closure. |
| Habitat validators | Inspected patch, suitability, critical-habitat-role, and model-receipt validators are one-line placeholders. | **CONFIRMED placeholders** | No executable Habitat validation is established. |
| Habitat workflow | `domain-habitat.yml` contains three TODO echo jobs on GitHub-hosted runners. | **CONFIRMED CI scaffold** | A successful workflow run does not prove Habitat validation, proof building, or publish dry-run behavior. |
| Source registries | Both subtype-first and domain-first Habitat source registry READMEs exist. | **CONFLICTED topology** | Config must not choose or duplicate source records. |
| Triplet path | Singular `data/triplet/habitat/` is a compatibility lane; plural `data/triplets/` is the canonical parent root. | **CONFIRMED compatibility posture** | Do not write projections to the singular lane. |
| Biotopes paths | Contract, schema, and policy compatibility READMEs exist. | **CONFIRMED non-canonical guardrails** | `Biotope` must not become a new Habitat authority through configuration. |
| Owners/CODEOWNERS | Named owners remain placeholders. | **NEEDS VERIFICATION** | Missing ownership does not imply approval. |
| Runtime, deployment, release, publication | No current behavior was proven by the inspected config lane. | **UNKNOWN / not authorized** | Nothing here establishes operational use or public release. |

### Evidence boundary

```text
Habitat config payload               = NOT ESTABLISHED
Habitat config consumer              = NOT OBSERVED IN BOUNDED SEARCH
Habitat package implementation       = NOT ESTABLISHED
Habitat pipeline implementation      = PLACEHOLDER
Habitat object schemas               = MOSTLY PERMISSIVE SCAFFOLDS IN INSPECTED SLICE
Habitat policy enforcement           = NOT ESTABLISHED
Habitat validators                   = PLACEHOLDERS IN INSPECTED SLICE
Habitat workflow                     = TODO ECHO SCAFFOLD
source registry topology             = CONFLICTED
object and trust-object path aliases = CONFLICTED
production behavior                  = UNKNOWN
```

[Back to top](#top)

---

## What belongs here

Only safe, non-secret, Habitat-specific configuration material for a named or explicitly proposed consumer belongs here.

| Accepted material | Purpose | Minimum posture |
|---|---|---|
| `README.md` | Define this configuration boundary. | Preserve no-authority, no-secrets, source-role, model/regulatory, sensitivity, evidence, and release rules. |
| `.gitkeep` | Preserve an otherwise-empty directory. | Non-semantic; never activation or maturity evidence. |
| `*.template.yaml` / `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, closed-shape where practical, no live binding, no secrets. |
| `*.example.yaml` / `*.example.json` / `*.example.toml` | Tiny illustrative configuration. | Obvious synthetic values, impossible identifiers/geometry, no automatic selection. |
| Conservative review defaults | Select an accepted hold, abstain, deny, redact, generalize, or review profile. | Cannot weaken policy, evidence, rights, sensitivity, model, or release burden. |
| Public-safe presentation selectors | Select already-governed labels, caveats, uncertainty display, or public-safe geometry profiles. | Cannot contain exact protected geometry or grant exposure. |
| Model presentation hints | Configure visibility of model identity, version, assumptions, uncertainty, intended use, and prohibited use. | Cannot alter model output, threshold meaning, calibration, or fitness. |
| Source-role display selectors | Preserve an accepted role mapping for display or routing. | Cannot invent a role mapping or upgrade authority. |
| Migration and compatibility notes | Document an accepted key, version, consumer, or path transition. | Time-bounded, owner-linked, reversible, no parallel authority. |
| Validation notes | Describe verified commands, negative cases, and outcomes. | Commands and workflows must resolve or remain labeled `PROPOSED` / `NEEDS VERIFICATION`. |

Synthetic examples must not resemble real sensitive habitat, rare-species context, occurrence locations, stewardship areas, protected areas, private parcels, restoration targets, low-count populations, cultural places, infrastructure, or management activity closely enough to support reconstruction.

[Back to top](#top)

---

## What does NOT belong here

- real Habitat observations, land-cover payloads, ecological-system records, patch geometries, model outputs, corridors, connectivity surfaces, restoration candidates, stewardship zones, or lifecycle data;
- exact or reconstructable sensitive habitat, occurrence-linked habitat, rare-species context, breeding, nesting, denning, roosting, spawning, refuge, hibernation, stewardship, restoration, protected-resource, private-land, or low-count details;
- real Fauna or Flora occurrences, specimens, taxonomy, protected locations, or ownership-transferring joins;
- credentials, tokens, private keys, certificates, cookies, signed URLs, private endpoints, internal hostnames, private IPs, database URLs, workstation paths, usernames, or environment-specific secrets;
- source activation, connector endpoints, source registry records, rights decisions, source-role decisions, or source-head records;
- model code, coefficients, training data, fitted artifacts, model cards, run receipts, calibration outputs, or fitness decisions;
- settings that label modeled habitat as regulatory critical habitat, observed occurrence, or legal designation;
- settings that label land cover, suitability, connectivity, corridor, restoration, or stewardship context as species presence or absence;
- settings that treat administrative stewardship or protected-area context as Habitat truth, access permission, ownership, or title;
- policy rules, Rego modules, sensitivity tiers, geoprivacy transforms, redaction methods, low-count rules, or release rules;
- canonical schemas, semantic contracts, DTOs, source registries, receipts, proofs, EvidenceBundles, catalog records, triplet projections, release manifests, corrections, withdrawals, or rollback cards;
- package code, pipeline logic, validators, fixtures, tests, workflow definitions, runtime adapters, infrastructure definitions, caches, indexes, tiles, exports, screenshots, reports, or generated summaries;
- local or domain-specific copies of generic `EvidenceBundle`, `ReleaseManifest`, `PolicyDecision`, `RunReceipt`, `CorrectionNotice`, or `RollbackCard` authority;
- `biotopes` object, schema, policy, registry, data, graph, or release authority;
- public API routes, browser-readable configuration, direct public-store access, UI-only hiding, or client-side geoprivacy.

[Back to top](#top)

---

## Inputs

A future Habitat configuration file requires an explicit input packet before it can be treated as implementation-supporting.

1. **Named consumer** — exact package, pipeline, app, runtime, connector, watcher, test harness, or tool.
2. **Consumer owner** — accountable owner and required reviewers.
3. **Declared format** — file type, format version, parser, encoding, duplicate-key policy, and unknown-key behavior.
4. **Explicit load path** — command-line, deployment, environment selection, test fixture, or direct code reference; never directory-presence inference.
5. **Precedence contract** — merge order, override limits, conflict behavior, reload behavior, and partial-application prevention.
6. **Authority references** — exact accepted contract, schema, policy, source registry, model card, and Habitat doctrine references.
7. **Source-role mapping** — accepted mapping between Habitat doctrine vocabulary and machine SourceDescriptor vocabulary, where required.
8. **Object/product family** — exact accepted object identity and alias posture.
9. **Spatial semantics** — CRS, units, resolution, scale, support, geometry class, uncertainty, internal/public-safe representation, and reconstruction risk.
10. **Temporal semantics** — source, observation, effective, valid, model, retrieval, run, release, expiry, supersession, and correction time kinds where material.
11. **Model semantics** — model/version/method, inputs/covariates, intended/prohibited uses, thresholds, calibration/validation, uncertainty, applicability, model card, and run receipt refs.
12. **Rights and sensitivity context** — source terms, attribution, redistribution, access, occurrence joins, private-land risk, low-count risk, and residual reconstruction risk.
13. **Evidence and release context** — EvidenceRefs, EvidenceBundle refs, validation, review, policy, release, correction, withdrawal, and rollback refs as required.
14. **Synthetic examples** — no real source records, exact locations, persons, parcels, credentials, or operational bindings.
15. **Deterministic validation** — parse, shape, semantic, negative, no-network, no-auto-discovery, and stable-output checks.
16. **Deactivation and rollback** — known-good prior version, disable path, affected-output inventory, invalidation plan, and restoration procedure.

A filename, path, parsed document, populated field, or green placeholder workflow does not satisfy these inputs.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future file may provide validated input to a verified consumer. It cannot itself:

- admit, activate, disable, retire, or reclassify a source;
- fetch live data or execute a watcher;
- create or mutate Habitat, Fauna, Flora, Soil, Hydrology, Hazards, Agriculture, or People/Land objects;
- execute, calibrate, validate, or approve a model;
- convert source role or object identity;
- determine public-safe geometry or geoprivacy sufficiency;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- create or persist a receipt, proof, EvidenceBundle, policy decision, review record, release manifest, correction notice, withdrawal, or rollback card;
- create a tile, index, graph, export, screenshot, Evidence Drawer payload, Focus Mode answer, or AI answer;
- authorize display, export, release, or publication.

A verified consumer may emit a parse result, validation result, candidate object, receipt candidate, or finite failure outcome in its own responsibility lane. Those outputs do not belong here merely because the consumer read a Habitat config file.

[Back to top](#top)

---

## Validation

### README validation

- KFM metadata block is balanced and current.
- Exactly one H1 is present.
- Required Directory Rules H2 headings are present in order.
- H2 headings are unique.
- Internal links resolve.
- Relative links point to inspected repository paths.
- Fenced blocks are balanced.
- Final newline is present.
- Bounded secret-pattern checks find no credential-like material.
- Evidence labels do not upgrade implementation maturity.

### Future payload validation matrix

| Gate | Required checks | Safe failure posture |
|---|---|---|
| Placement | File is safe configuration under this lane, not authority-bearing material. | `FAIL`; relocate or reject. |
| Parse/encoding | Deterministic parser, version, encoding, duplicate-key handling, final newline. | `FAIL` / `ERROR`; no partial application. |
| Shape | Accepted schema/profile; closed properties where practical; unknown keys explicit. | `FAIL` / `HOLD`. |
| Consumer binding | Named consumer, owner, explicit load path, precedence, deactivation. | `HOLD`; no activation. |
| No discovery by presence | Tests prove directory or filename presence does not activate behavior. | `FAIL`. |
| Source role | Accepted role mapping; no in-place authority upgrade. | `FAIL` / `DENY`. |
| Object identity | Exact accepted object path/type; aliases do not become separate authorities. | `HOLD` / `FAIL`. |
| Habitat semantics | Patch, observation, model, designation, corridor, restoration, stewardship, aggregate, candidate, and synthetic meanings remain distinct. | `FAIL` / `DENY`. |
| Cross-domain ownership | Fauna, Flora, Soil, Hydrology, Hazards, Agriculture, People/Land, and generic trust objects keep ownership. | `FAIL` / `HOLD`. |
| Model fitness | Model card/run, intended use, thresholds, calibration, validation, uncertainty, applicability. | `HOLD` / `ABSTAIN`. |
| Spatial support | CRS, units, resolution, scale, support, geometry class, uncertainty, public-safe profile. | `FAIL` / `HOLD`. |
| Time | Relevant time kinds, freshness, stale, expiry, supersession, correction. | `FAIL` / `ABSTAIN`. |
| Rights | Terms, attribution, reuse, access, redistribution, and review resolve. | `HOLD` / `DENY`. |
| Sensitivity | No exact/reconstructable protected context; governed profile refs resolve. | `DENY` / `FAIL`. |
| Join-induced risk | Result reassessed for strongest restriction, low count, differencing, and reconstruction. | `HOLD` / `DENY`. |
| Secrets/live bindings | No credentials, private endpoints, local paths, or deployment secrets. | `FAIL`; rotate/revoke if exposed. |
| No-network | Validation and fixtures run without live source access by default. | `FAIL` / `ERROR`. |
| Negative cases | Missing evidence, role conflict, alias conflict, invalid model, exact-location request, stale source, unknown key, precedence conflict, partial state. | Required before activation. |
| Determinism | Same config and fixtures produce stable parsed and validation results. | `FAIL`. |
| Policy/runtime separation | Config cannot emit allow/release/public outcomes directly. | `DENY` / `FAIL`. |
| Derived-output inventory | Consumer identifies caches, tiles, indexes, exports, screenshots, summaries, and AI outputs affected by changes. | `HOLD`. |
| Correction/rollback | Deactivation, prior version, supersession, invalidation, restoration, and revalidation tested. | `HOLD`. |
| Public path | Public apps/clients do not read this directory directly. | `DENY` / `FAIL`. |

A syntactically valid file is not necessarily semantically safe, rights-cleared, policy-allowed, evidence-supported, release-ready, or public-safe.

[Back to top](#top)

---

## Review burden

README-only changes require:

- configuration or documentation review; and
- Habitat domain review.

A future non-README file also requires the applicable:

- named consumer owner;
- Habitat object/contract steward;
- source registry and source-role reviewer;
- rights and attribution reviewer;
- model/method/fitness reviewer;
- sensitivity and geoprivacy reviewer;
- Fauna or Flora steward when occurrence, taxon, specimen, or protected-location context is joined;
- Soil, Hydrology, Hazards, Agriculture, or People/Land steward when a consequential cross-domain claim depends on that lane;
- schema and validation reviewer;
- security/privacy reviewer;
- policy/runtime reviewer;
- release/correction/rollback reviewer.

Do not infer acceptance from placeholder ownership, a missing CODEOWNERS rule, repository write access, successful parsing, or a green TODO-only workflow. Owners remain `OWNER_TBD` until accepted and enforceable.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat doctrine and lane ownership.
- [`../../../contracts/domains/habitat/README.md`](../../../contracts/domains/habitat/README.md) — Habitat semantic-contract lane.
- [`../../../schemas/contracts/v1/domains/habitat/README.md`](../../../schemas/contracts/v1/domains/habitat/README.md) — Habitat machine-schema index.
- [`../../../policy/domains/habitat/README.md`](../../../policy/domains/habitat/README.md) — current Habitat policy scaffold.
- `policy/sensitivity/habitat/` — expected sensitivity lane; exact README was not found in this evidence pass.
- [`../../../packages/domains/habitat/README.md`](../../../packages/domains/habitat/README.md) — Habitat package boundary.
- [`../../../pipelines/domains/habitat/README.md`](../../../pipelines/domains/habitat/README.md) — Habitat executable-pipeline boundary.
- [`../../../pipeline_specs/habitat/README.md`](../../../pipeline_specs/habitat/README.md) — Habitat declarative-pipeline boundary.
- `tools/validators/domains/habitat/` — current validator path with inspected placeholders.
- [`../../../data/registry/sources/habitat/README.md`](../../../data/registry/sources/habitat/README.md) — subtype-first source registry candidate.
- [`../../../data/registry/habitat/sources/README.md`](../../../data/registry/habitat/sources/README.md) — domain-first source registry candidate.
- [`../../../data/triplet/habitat/README.md`](../../../data/triplet/habitat/README.md) — singular triplet compatibility lane.
- [`../../../data/triplets/README.md`](../../../data/triplets/README.md) — canonical plural triplet parent.
- [`../../../contracts/biotopes/README.md`](../../../contracts/biotopes/README.md), [`../../../schemas/biotopes/README.md`](../../../schemas/biotopes/README.md), and [`../../../policy/biotopes/README.md`](../../../policy/biotopes/README.md) — non-canonical compatibility guardrails.
- [`../../../.github/workflows/domain-habitat.yml`](../../../.github/workflows/domain-habitat.yml) — TODO-only Habitat workflow scaffold.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — credential and sensitive-value posture.

Future files should link to exact accepted contracts, schemas, policy profiles, SourceDescriptors, model cards, tests, fixtures, receipts, proofs, review records, releases, corrections, and rollback records only after those paths and authority relationships are verified.

[Back to top](#top)

---

## ADRs

No ADR is enacted by this README.

Separate governance or migration discipline is required for changes that would:

- add, merge, rename, or retire a canonical domain, sublane, object family, or source-role vocabulary;
- resolve the seven-role Habitat vocabulary versus the richer SourceDescriptor schema vocabulary;
- resolve `HabitatPatch` contract aliases, `SuitabilityModel` path aliases, or `ModelRunReceipt` placement aliases;
- move or duplicate generic trust-object schemas under the Habitat domain;
- select subtype-first versus domain-first source registry topology;
- choose the canonical Habitat triplet child lane;
- accept, redirect, migrate, or retire `biotopes` compatibility paths;
- establish a universal config discovery or precedence contract;
- change Habitat landscape-versus-species ownership;
- equate modeled Habitat with regulatory designation, observed occurrence, legal status, or operational instruction;
- define or alter sensitivity tiers, geoprivacy methods, low-count thresholds, public-safe geometry, or reconstruction policy;
- decide source rights, source activation, model fitness, promotion gates, or public release;
- create a parallel contract, schema, policy, registry, receipt, proof, catalog, release, or public interface;
- authorize direct client access to config, lifecycle, registry, proof, source, model, or internal stores.

Configuration must not settle these decisions indirectly by choosing a filename, inline enum, permissive fallback, default path, or local profile.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, authored against `main@47ccfa02de783c1cb90609d7d79a3d316082ec6b` and target-rechecked unchanged at `main@8bb1d0b8b288781169e5592d60962cd7537fc37c`.

Review again before:

- the first non-README payload;
- any consumer binding, loader, precedence, or reload behavior;
- any source-role mapping or object alias resolution;
- any source or model activation;
- any sensitivity/geoprivacy profile selection;
- any operational map, API, index, graph, export, Evidence Drawer, Focus Mode, AI, release, or publication integration.

[Back to top](#top)

---

## Bounded context and ubiquitous language

Within KFM, `configs/domains/habitat/` means:

> Safe, explicit, non-secret configuration support for a named Habitat consumer, subordinate to Habitat doctrine, source governance, object contracts, machine schemas, model evidence, sensitivity policy, validation, review, release, correction, and rollback.

It does **not** mean:

- the Habitat domain;
- Habitat truth;
- a model registry or runtime;
- a source registry or connector;
- a policy bundle;
- a schema or contract home;
- a geoprivacy engine;
- a lifecycle store;
- a receipt, proof, catalog, triplet, or release store;
- a public map/API/UI configuration service;
- an AI instruction or truth source.

### Key terms

| Term | Meaning in this lane | Must not imply |
|---|---|---|
| Habitat config | A versioned consumer input under explicit binding. | Habitat truth or source activation. |
| Profile ref | Pointer to an accepted external profile. | Inline redefinition or approval. |
| Consumer | Exact code/runtime/test surface that parses the file. | Every Habitat process or directory-wide auto-discovery. |
| Habitat patch | Discrete Habitat spatial unit under an accepted contract. | Occurrence, designation, suitability, ownership, or access. |
| Suitability model | Modeled product under method/version/uncertainty controls. | Observation, critical habitat, permit result, or species presence. |
| Regulatory context | Official designation or record within its issuing scope and effective time. | All Habitat truth or legal advice. |
| Stewardship zone | Administrative/stewardship context. | Habitat condition, ownership, title, access, or regulatory designation. |
| Public-safe geometry | Released/generalized representation produced under policy and receipt controls. | Exact geometry or an informal low-zoom display. |
| Join-induced risk | Sensitivity or reconstructability introduced by combining otherwise separate inputs. | Safety because each individual input looked public. |
| Validation pass | Config checks passed. | Policy allow, evidence closure, release approval, or public safety. |
| Deactivation | Consumer stops selecting a config. | Correction or withdrawal of already-derived outputs. |

[Back to top](#top)

---

## Configuration classes

| Class | Examples | Activation posture |
|---|---|---|
| Documentation | `README.md`. | Descriptive only. |
| Directory marker | Empty `.gitkeep`. | Non-semantic. |
| Template | `*.template.yaml`. | Never active by itself. |
| Example | `*.example.json`. | Synthetic/test-only. |
| Review profile selector | References accepted hold/review/caveat profiles. | Internal and consumer-bound. |
| Display profile selector | References public-safe labels/geometry/caveat profiles. | Requires released input and policy/release closure. |
| Model presentation selector | References model-card and uncertainty display profiles. | Cannot change model output or validity. |
| Compatibility mapping | Time-bounded accepted key/path migration. | Must not become dual authority. |
| Operational config | Future explicitly loaded file. | `NOT AUTHORIZED` until all first-payload gates close. |

A file must declare its class. Ambiguous classification fails closed.

[Back to top](#top)

---

## Minimum per-file contract

Every future non-README file must carry or reference:

```yaml
config_id: <STABLE_NON_AUTHORITY_ID>
config_version: <SEMVER_OR_ACCEPTED_VERSION>
format_version: <PARSER_CONTRACT_VERSION>
status: PROPOSED
classification: template | example | review_profile | display_profile | operational
intended_consumer: <EXACT_IMPORT_ROUTE_COMMAND_OR_SERVICE>
consumer_owner: OWNER_TBD
load_path:
  mechanism: explicit
  selector: <PATH_FLAG_ENV_OR_TEST_FIXTURE>
precedence:
  rank: <EXPLICIT>
  conflicts: fail_closed
unknown_key_behavior: reject
schema_ref: <ACCEPTED_SCHEMA_REF_OR_NEEDS_VERIFICATION>
contract_refs:
  - <ACCEPTED_SEMANTIC_CONTRACT_REF>
policy_refs:
  - <ACCEPTED_POLICY_PROFILE_REF>
source_role_profile_ref: <ACCEPTED_MAPPING_REF>
object_profile_ref: <ACCEPTED_OBJECT_AND_ALIAS_REF>
spatial_profile_ref: <ACCEPTED_CRS_SCALE_SUPPORT_PUBLIC_SAFE_REF>
temporal_profile_ref: <ACCEPTED_TIME_AND_FRESHNESS_REF>
model_profile_ref: <ACCEPTED_MODEL_CARD_RUN_AND_FITNESS_REF>
sensitivity_profile_ref: <ACCEPTED_SENSITIVITY_GEOPRIVACY_REF>
network_posture: no_network_by_default
example_posture: synthetic
validation:
  parser: <COMMAND_OR_TOOL_REF>
  negative_cases: required
  deterministic: true
  no_auto_discovery: true
deactivation:
  mechanism: <EXPLICIT>
rollback:
  prior_version: <REF>
  affected_outputs: <INVENTORY_REF>
  invalidation_plan: <REF>
```

### Contract rules

- `status: ACTIVE` is prohibited without current evidence of binding, validation, review, and deactivation.
- `unknown_key_behavior: ignore` requires explicit compatibility justification and tests; reject is the default.
- `policy_refs`, `schema_ref`, `contract_refs`, and profile refs must resolve to accepted authority, not README prose or permissive placeholders.
- A config cannot embed an alternate source-role enum, policy decision, model card, release state, or sensitive geometry.
- A local boolean such as `public: true`, `critical_habitat: true`, `safe: true`, or `validated: true` has no authority.
- Missing required metadata produces `HOLD`, `FAIL`, `ABSTAIN`, `DENY`, or `ERROR`; never best-effort activation.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No universal Habitat config loader is established.

A verified binding must identify:

- exact config path and content digest;
- exact consumer import, command, job, route, service, or test;
- parser/version and schema/profile refs;
- explicit selection mechanism;
- precedence relative to defaults, domain, dev, test, local, environment, deployment, and runtime state;
- duplicate and unknown-key handling;
- atomic load/reload behavior and partial-application prevention;
- missing/stale/unsupported file behavior;
- logging/redaction/telemetry behavior;
- deactivation, correction, rollback, and affected-output invalidation;
- tests proving directory and filename presence do not activate anything.

### Default precedence posture

Until a consumer proves otherwise:

1. no file is loaded automatically;
2. no filename has implicit priority;
3. a local/deployment override does not become repository truth;
4. unknown keys fail closed;
5. conflicting values do not merge unpredictably;
6. missing source-role, object, model, rights, sensitivity, evidence, review, or release context blocks consequential behavior;
7. configuration cannot override source registry, policy, review, validation, correction, or release decisions;
8. reload must not leave half-old, half-new state;
9. fallback to a permissive prior or built-in profile is prohibited unless explicitly governed and tested.

[Back to top](#top)

---

## Habitat object family boundaries

Configuration must identify the exact object/product family being configured and preserve its contract boundary.

| Object/product | Configuration may describe | Must not become |
|---|---|---|
| `LandCoverObservation` | Class scheme, source vintage, observation time, scale, uncertainty, display. | Habitat quality, species presence, legal designation. |
| `EcologicalSystem` | Native classification/version, crosswalk ref, scale, uncertainty. | Species occurrence or vegetation-community ownership. |
| `HabitatPatch` | Accepted patch profile, geometry/support/caveat display, public-safe ref. | Occurrence, suitability, critical habitat, ownership, access. |
| `SuitabilityModel` | Model-card/run/profile refs, threshold labels, uncertainty display, intended use. | Observation, regulatory designation, species presence, management instruction. |
| `HabitatQualityScore` | Score family, method ref, uncertainty/caveat display. | Universal ecological quality or regulatory finding. |
| `ConnectivityEdge` | Method, nodes, resistance/cost assumptions, time, uncertainty. | Observed movement route or access right. |
| `Corridor` | Derived corridor method, scale, confidence, intended use. | Legal corridor, observed route, guaranteed movement. |
| `RestorationOpportunity` | Candidate/model profile, feasibility caveats, review routing. | Approved project, prescription, funding, obligation, guaranteed success. |
| `StewardshipZone` | Administrative source/effective date/display profile. | Ownership, title, access, habitat condition, regulatory designation. |
| `UncertaintySurface` | Method/version, units, interpretation, display. | Truth confidence detached from model/source context. |
| Regulatory critical habitat | Issuing source, designation identity, effective dates, scope, caveats. | Modeled habitat, range map, occurrence, permit advice. |
| Occurrence-context join | Foreign-owned occurrence ref, geoprivacy/sensitivity state, join method. | Habitat-owned occurrence truth. |
| Aggregate summary | Support unit, time window, suppression/low-count posture. | Exact local occurrence or absence proof. |
| Candidate | Review state, evidence gaps, prohibited uses. | Confirmed/released object. |
| Synthetic fixture | Obvious synthetic identity and test-only posture. | Observed reality or production input. |

### Confirmed alias conflicts

- `HabitatPatch` meaning has both `habitat_patch.md` and `habitat-patch.contract.md` paths.
- `SuitabilityModel.md` and `suitability_model.md` coexist; the snake-case schema points to the lower-case path.
- Model-run receipt meaning appears at root and land-cover sublane paths.

Config must not select one alias by lexicographic order, import accident, file existence, or human preference. Until resolved, consequential binding is `HOLD`.

[Back to top](#top)

---

## Source-role vocabulary and anti-collapse

Habitat doctrine uses seven high-level roles:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

The repository's fielded shared `SourceDescriptor` schema uses a richer `source_role` vocabulary including `authoritative_for_claim`, `regulatory_context`, `observation`, `occurrence_evidence`, `aggregator`, `remote_sensing_observation`, `model_context`, `candidate_signal`, `derived_public_product`, `steward_review_source`, `citation_source`, and `fixture_only`.

These vocabularies are **CONFLICTED**, not interchangeable by intuition.

### Required posture

- Configuration must reference an accepted mapping profile when crossing vocabularies.
- Mapping must preserve source type, role, authority rank, allowed/prohibited claim roles, rights, sensitivity, time, evidence, review, release, and limitations.
- Multiple machine roles may map to one Habitat display class only for display/organization; the original machine role must remain visible and recoverable.
- A mapping cannot upgrade `model_context` to regulatory, `candidate_signal` to observed, `aggregator` to authoritative local truth, or `fixture_only` to production.
- Unknown or unmapped values fail closed.
- AI must not generate or infer role mappings.
- Role changes require new governed objects/decisions; never in-place config relabeling.

### Anti-collapse examples

```text
remote_sensing_observation != ground observation unless contract says so
regulatory_context          != all Habitat truth
model_context               != observed occurrence
aggregator                  != source authority
candidate_signal            != confirmed Habitat object
derived_public_product      != canonical/internal object
fixture_only                != production
```

[Back to top](#top)

---

## Observation, model, regulatory, and administrative boundaries

### Observation

An observation must preserve source, method, observed time, spatial support, units/classification, uncertainty, and evidence. Remote sensing is observation of sensor-derived signal or classified product under its source role; it is not automatically field-observed Habitat truth.

### Model

A model profile must preserve:

- model identity/version and code/spec refs;
- model card and run receipt refs;
- source/covariate identities and versions;
- training/calibration/validation scope where applicable;
- intended and prohibited uses;
- thresholds and class meanings;
- spatial/temporal applicability;
- uncertainty, limitations, and sensitivity;
- evidence, review, policy, release, correction, and rollback refs.

A model output remains modeled at every map, API, report, export, Evidence Drawer, Focus Mode, and AI surface.

### Regulatory

Regulatory context must preserve issuing authority, designation/record identity, legal scope, effective/expiry dates, source vintage, status, and caveats. Configuration cannot issue, alter, interpret conclusively, or generalize a regulatory designation beyond its source authority.

### Administrative/stewardship

Administrative and stewardship context must preserve source, effective dates, boundaries, rights, and limitations. It is not habitat condition, conservation success, title, ownership, access, or regulatory status.

### Restoration

Restoration opportunity is a candidate or modeled planning context unless separately governed evidence establishes another status. It is not a prescription, mandate, permit, funded project, completed action, or success guarantee.

[Back to top](#top)

---

## Spatial support, geometry, scale, and public-safe representation

Unlabeled values such as `10`, `250`, `0.8`, `county`, or `zoom: 8` are unsafe when their meaning depends on units, CRS, scale, support, uncertainty, threshold semantics, or public exposure.

A spatial profile must identify:

- CRS and axis/order assumptions;
- horizontal/vertical units where relevant;
- source resolution and effective support;
- geometry type and topology expectations;
- precision, positional uncertainty, and classification uncertainty;
- raster cell/pixel interpretation and resampling profile;
- vector simplification/generalization profile;
- scale and zoom applicability;
- internal exact geometry ref versus public-safe geometry ref;
- transform/policy/receipt refs;
- residual reconstruction risk;
- correction and rollback behavior.

### Rules

- Habitat geometry does not prove ownership, access, designation, occurrence, condition, or suitability by itself.
- Public-safe geometry must be produced before tiles, exports, indexes, screenshots, or public DTOs.
- Style filters, opacity, hidden properties, zoom constraints, and browser-side clipping are not geoprivacy.
- Configuration may select an accepted transformation profile; it cannot inline an ad hoc radius, jitter, suppression, or simplification to bypass review.
- A coarse output can remain sensitive when low-count, repeated-query, differencing, parcel intersection, or cross-layer reconstruction is possible.
- Public-safe output must retain scale/support/uncertainty and avoid false precision.

[Back to top](#top)

---

## Time, freshness, stale state, and correction

Keep distinct where material:

- source publication/snapshot time;
- source vintage/edition;
- observed time and observation interval;
- regulatory effective/expiry/status time;
- model training, initialization, run, and valid time;
- retrieval/ingestion time;
- transformation and validation time;
- review time;
- release time;
- cache/index build time;
- embargo/delay expiry;
- supersession, correction, withdrawal, and rollback time.

A single `timestamp`, `year`, `latest`, or `current` field must not collapse those meanings.

### Freshness rules

- Freshness is product- and use-specific, not a universal age threshold.
- Source cadence, known update windows, expected latency, outage state, and staleness policy must remain visible.
- A fresh fetch can contain an old source vintage; a recently rebuilt tile can represent stale data.
- Stale, delayed, partial, corrected, superseded, withdrawn, or unknown state must not be rendered as current normal data.
- Config cannot rewrite dates or select a fallback merely to make output appear current.
- Corrections supersede governed objects and derived outputs; they do not silently mutate history.

[Back to top](#top)

---

## Rights, sensitivity, geoprivacy, and join-induced risk

Habitat configuration is fail closed where rights, sensitivity, stewardship, or exposure risk is unclear.

### Rights and stewardship

A profile must preserve:

- rights/license/terms status and verification time;
- attribution and link-back obligations;
- redistribution, derivative, commercial, and AI-use restrictions;
- source-owner/steward and consent/agreement refs;
- access posture and credential requirements without secret values;
- embargo, delay, retention, deletion, and withdrawal obligations;
- review requirements and prohibited uses.

Unknown, no-assertion, permission-required, denied, expired, or contested rights block public/release use until governed resolution.

### Sensitive contexts

Examples include:

- rare/protected-species habitat and occurrence-linked context;
- breeding, nesting, denning, roosting, spawning, refuge, hibernation, or concentration areas;
- precise stewardship, restoration, acquisition, management, or conservation-priority areas;
- private-land, access, ownership-adjacent, or land-management details;
- low-count/small-area summaries;
- culturally controlled, archaeological, or community-sensitive context;
- infrastructure-sensitive ecological relationships;
- time series revealing arrival, removal, intervention, monitoring, or management activity;
- combinations that reveal more than each input alone.

### Join-induced risk

The resulting join inherits at least the strongest applicable restriction and may require stricter handling. A public land-cover layer joined with a restricted occurrence can become restricted. A generalized occurrence joined with a small habitat polygon can become reconstructable.

Required controls may include:

- denial or steward-only access;
- geometry suppression/generalization/aggregation;
- low-count suppression;
- constrained deterministic jitter under accepted policy;
- temporal delay/bucketing;
- attribute suppression;
- query-rate/result-shape controls;
- public-safe derivative generation;
- redaction/geoprivacy receipts;
- re-evaluation after every material join or correction.

A config value cannot waive these controls.

[Back to top](#top)

---

## Source registry, connector, and activation boundaries

### Registry topology conflict

Repository-present Habitat source-registry documentation exists at both:

```text
data/registry/sources/habitat/    # subtype-first
data/registry/habitat/sources/    # domain-first
```

The topology remains unresolved. Configuration must:

- reference one accepted canonical record by stable ID/ref;
- never duplicate or fork SourceDescriptors across both lanes;
- never infer precedence from path depth, modification time, or filename;
- treat conflicting records as `CONFLICTED` and route to steward review;
- require redirects/pointers or a governed migration when topology is resolved;
- preserve correction, supersession, and rollback lineage.

### Source activation

A `SourceDescriptor` ref is not activation. Configuration cannot change connector activation state, admission, cadence, rights, sensitivity, source role, release state, or lifecycle state.

A source may be used only after the relevant governed flow resolves:

- descriptor identity/version and authority;
- source role and allowed/prohibited claim roles;
- rights, sensitivity, access, citation, cadence, and source head;
- connector/watcher activation state;
- admission decision and intake/quarantine posture;
- validation, policy, review, evidence, release, correction, and rollback requirements.

### Connectors and watchers

- Source-specific fetching belongs under `connectors/`, not this lane.
- Watchers are non-publishers: they may observe and emit candidate decisions/receipts, not catalog/published truth.
- Config cannot authorize live endpoints, credentials, source queries, polling, or refresh schedules merely by defining them.
- Credential references must remain server-side and resolve through approved secret handling.

[Back to top](#top)

---

## Implementation and governance maturity

### Current implementation-shaped surfaces

| Surface | Inspected posture | Config consequence |
|---|---|---|
| Habitat package | `0.0.0`, empty initializer, planning README. | Do not claim consumer/export behavior. |
| NLCD ingest pipeline | One-line PROPOSED placeholder. | No source ingest established. |
| Habitat patch builder | One-line PROPOSED placeholder. | No patch-building behavior established. |
| Suitability runner | One-line PROPOSED placeholder. | No model execution established. |
| HabitatPatch schema | Empty properties, permissive. | No field-complete validation. |
| SuitabilityModel schema | Empty properties, permissive. | No field-complete validation. |
| Habitat policy README | Greenfield scaffold with overbroad root wording. | Do not rely on it as mature policy. |
| `deny_unpublished.rego` | Says no real rules yet; `default deny := false`. | Does not prove deny-by-default enforcement. |
| model-card deny module | Generated scaffold; `default allow := false`. | Does not prove complete model-card policy. |
| Habitat validators | One-line placeholders in inspected slice. | No executable semantic validation. |
| Habitat workflow | TODO echo jobs. | Green status is not enforcement evidence. |

### First implementation sequence

1. Resolve object/contract aliases and source-role mapping.
2. Resolve source-registry topology and generic trust-object authority.
3. Complete package metadata, ownership, dependencies, and exports.
4. Implement one small pure/no-network parser or profile-ref validator.
5. Add synthetic valid/invalid fixtures and negative-first tests.
6. Add schema-bound and semantic validation without outrunning permissive schemas.
7. Implement one low-risk internal consumer with explicit binding and deactivation.
8. Prove no source activation, network access, lifecycle write, policy, release, or public exposure by config presence.
9. Replace TODO workflows with substantive checks.
10. Add correction, affected-output invalidation, rollback, and replay tests.

[Back to top](#top)

---

## Compatibility and parallel-authority guardrails

### Segment versus flat domain paths

This README follows Directory Rules domain-segment placement such as `contracts/domains/habitat/` and `schemas/contracts/v1/domains/habitat/`. Flat forms remain drift/compatibility candidates unless accepted separately.

### Habitat object aliases

Duplicate/alias object paths must not evolve independently. Configuration must reference a reviewed canonical identity or remain inactive.

### Generic trust-object duplication

Habitat-local schemas exist for objects such as `EvidenceBundle`, `ReleaseManifest`, `RunReceipt`, decision envelopes, correction, rollback, and Evidence Drawer payloads. These object families also have cross-domain/shared authority surfaces.

Until authority is resolved:

- do not generate Habitat-specific alternate truth-object types;
- do not bind config to a permissive Habitat-local copy as if it were canonical;
- use shared authority or an accepted domain profile via explicit `$ref`/profile rules;
- record any domain extension without redefining shared fields/outcomes;
- treat conflicting shared/domain shapes as `HOLD`;
- require migration and backward-compatibility tests before public use.

### Triplet compatibility

`data/triplet/habitat/` is a singular compatibility marker. The canonical parent is `data/triplets/`; exact Habitat child placement remains `NEEDS VERIFICATION`. Config must not write either lane directly.

### Biotopes compatibility

`contracts/biotopes/`, `schemas/biotopes/`, and `policy/biotopes/` are compatibility/drift guardrails. `Biotope` is not a sovereign KFM object/domain/policy family. Configuration must use accepted Habitat or Flora-owned canonical objects and must not create a `biotopes` runtime, schema, policy, registry, graph, or release authority.

[Back to top](#top)

---

## Logging, caches, tiles, indexes, exports, and derived-output invalidation

### Logging and telemetry

A consumer must not log:

- secrets, credentials, signed URLs, private endpoints, headers, cookies, or tokens;
- raw config contents when they can include private/sensitive values;
- exact protected geometry, occurrence coordinates, private parcel/person details, or controlled source content;
- full SourceDescriptors, EvidenceBundles, model inputs, or restricted artifacts;
- prompts, hidden reasoning, or generated internal summaries;
- stack traces or request data that leak restricted paths/values.

Prefer safe reason codes, object refs, profile IDs, digests, versions, and bounded public-safe diagnostics.

### Derived surfaces

A config change, correction, source-role correction, model invalidation, rights change, sensitivity increase, geoprivacy defect, source withdrawal, release rollback, or object-alias resolution may affect:

- in-memory and persistent caches;
- map tiles, vector/raster pyramids, PMTiles, COGs, and derived geometries;
- search indexes and autocomplete;
- vector/embedding indexes;
- knowledge-graph/triplet projections;
- dashboards and metrics;
- downloads, exports, reports, PDFs, screenshots, and share links;
- Evidence Drawer and Focus Mode payloads;
- alerts/notifications;
- AI context stores, retrieved snippets, answer caches, and generated summaries;
- release aliases and current-version pointers.

### Invalidation contract

A future consumer must provide:

1. deterministic dependency/affected-output discovery;
2. stop-selection/deactivation before regeneration;
3. quarantine/deny behavior for unsafe existing outputs;
4. correction/withdrawal/rollback refs;
5. cache/index/tile/export/AI invalidation;
6. regeneration only from corrected governed inputs;
7. validation, policy, review, release, and public-path rechecks;
8. proof that stale/unsafe derivatives are no longer served.

A Git revert or config rollback alone does not invalidate downstream material.

[Back to top](#top)

---

## Failure behavior

| Condition | Required safe disposition |
|---|---|
| README-only lane / no operational payload | `NOT_CONFIGURED`; no activation. |
| Malformed file, unsupported version, duplicate key, invalid encoding | `FAIL` / `ERROR`; no partial application. |
| Unknown key, unknown precedence, or unpredictable merge | `ERROR` / `HOLD`. |
| Missing consumer, owner, load path, schema, contract, policy, or profile ref | `HOLD`; do not activate. |
| Source-role vocabularies conflict or value is unmapped | `CONFLICTED` / `HOLD`; no inferred mapping. |
| Object alias or contract path unresolved | `CONFLICTED` / `HOLD`. |
| Source registry records conflict across topologies | `CONFLICTED` / `HOLD`. |
| Generic versus Habitat-local trust-object shape conflicts | `HOLD`; use no permissive fallback. |
| Source role upgrade attempt | `FAIL` / `DENY`. |
| Modeled output presented as regulatory/observed/occurrence truth | `FAIL` / `DENY`. |
| Habitat product presented as species occurrence, title, ownership, access, or legal advice | `FAIL` / `DENY`. |
| Missing model card/run, method, threshold semantics, calibration, validation, uncertainty, or fitness | `HOLD` / `ABSTAIN`. |
| Unknown/expired/denied rights or attribution failure | `HOLD` / `DENY`. |
| Missing or ambiguous sensitivity/geoprivacy/join-risk posture | `HOLD` / `DENY` / `ABSTAIN`. |
| Exact/reconstructable protected context requested for public use | `DENY`. |
| Stale, superseded, corrected, withdrawn, partial, or missing input | Preserve state; `ABSTAIN` unless governed alternative exists. |
| Source outage | Do not fabricate freshness/completeness; reason-coded stale/partial state. |
| Secret or private endpoint detected | `FAIL`; remove and rotate/revoke as required. |
| Consumer cannot determine affected outputs or safe rollback | `HOLD` / `ERROR`. |
| Existing derived output cannot be invalidated | `DENY` continued serving; incident/correction review. |
| Public client attempts direct config access | `DENY` / `FAIL`. |

`PASS` is a config-validator result, not source admission, model fitness, evidence closure, policy allow, release approval, or publication.

[Back to top](#top)

---

## Governed AI and generated language

AI may assist maintainers with config review, explanation, migration drafts, or evidence retrieval only after scope, evidence, rights, sensitivity, and policy boundaries are defined.

AI must not:

- infer or invent source roles, object aliases, registry precedence, model fitness, policy profiles, or release state;
- treat config prose, schema stubs, map appearance, vector retrieval, graph edges, model output, or generated text as evidence;
- expose exact protected habitat, rare-species, stewardship, private-land, cultural, archaeological, or infrastructure-linked context;
- upgrade modeled Habitat to observation/regulatory status;
- infer species presence or absence from habitat alone;
- invent citations, profile IDs, model cards, receipts, reviews, or release refs;
- bypass `ABSTAIN`, `DENY`, `HOLD`, `ERROR`, or `NEEDS VERIFICATION` because a plausible answer can be generated;
- retain stale/corrected/withdrawn config-derived context in answer caches or indexes.

A governed AI answer depends on resolved EvidenceRefs/EvidenceBundles, policy, review, release, freshness, correction, and public-safe projection state. Evidence outranks fluency.

[Back to top](#top)

---

## Migration and anti-bypass posture

If misplaced or authority-bearing material is found here:

1. stop treating it as active merely because it is committed;
2. classify it by responsibility: config, secret, source/registry, contract, schema, policy, implementation, lifecycle data, receipt, proof, catalog/triplet, release, public artifact, or sensitive material;
3. remove/quarantine credentials, private endpoints, exact protected context, and live bindings; rotate/revoke as required;
4. move source identity/activation to source governance;
5. move meaning to `contracts/`;
6. move machine shape to `schemas/`;
7. move policy/geoprivacy rules to `policy/`;
8. move package/pipeline/validator/runtime/app code to owning implementation roots;
9. move lifecycle, registry, receipt, proof, catalog/triplet, and published material to canonical `data/` lanes;
10. move release/correction/withdrawal/rollback decisions to `release/`;
11. preserve provenance, consumer impact, old/new paths, correction, invalidation, and rollback;
12. create drift/migration/correction records when material was consumed;
13. verify no stale or unsafe derived output remains served.

### Anti-bypass matrix

| Bypass | Required response |
|---|---|
| Config used as policy or source admission | Reject; use owning authority. |
| Config duplicates contract/schema | Remove duplicate authority; retain refs only. |
| File/folder presence activates source/model | Reject; require explicit verified binding. |
| Permissive schema used as proof of semantic safety | Reject; schema maturity must match claims. |
| Config chooses object/source-role alias silently | Reject; require reviewed mapping/migration. |
| Config contains exact sensitive context | Remove, assess exposure, correct/invalidate derivatives. |
| Client-side hiding used as geoprivacy | Reject; transform or deny before artifact generation. |
| Watcher publishes from config | Reject; watcher emits candidates/receipts only. |
| Config writes catalog/triplet/receipt/proof/release | Reject and relocate. |
| Public client reads config/internal store | Reject; use governed APIs/released artifacts. |
| AI treats config/model/map as truth | Abstain/deny and resolve evidence. |

[Back to top](#top)

---

## Rollback, correction, supersession, and invalidation

### README rollback

Before merge, close/abandon the scoped PR. After merge, revert the documentation commit or restore prior blob `a34dc7b95b99691f0cfa538ee5bf9e4ef536bedc` through reviewed history.

### Future payload rollback

1. stop selecting the affected config atomically;
2. stop source fetches, watchers, model runs, transformations, indexing, tiling, exports, alerts, and public/AI serving that depend on it;
3. preserve the faulty config version, content digest, consumer version, logs/receipts, and evidence needed for review without exposing sensitive content;
4. identify affected sources, objects, joins, model runs, candidates, caches, tiles, indexes, graphs, exports, screenshots, dashboards, narratives, Evidence Drawer/Focus payloads, AI contexts, releases, and aliases;
5. assess source-role, object-identity, model/regulatory, species-ownership, rights, sensitivity, geoprivacy, evidence, review, and release impacts;
6. quarantine, deny, withdraw, or mark stale unsafe outputs;
7. restore a prior known-good config or safe disabled state;
8. correct/supersede source, model, object, policy, review, release, and rollback records in their owning roots;
9. invalidate all affected derived surfaces and current aliases;
10. regenerate only from corrected governed inputs;
11. rerun parse, shape, semantic, negative, no-network, sensitivity, policy, evidence, release, and public-path checks;
12. verify stale/unsafe output is no longer served and record closure.

A Git revert does not revoke exposed data, correct a model/regulatory claim, withdraw a release, remove cached search/AI context, or create KFM correction lineage by itself.

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] Accepted consumer and enforceable owners are verified.
- [ ] Format, version, parser, explicit load path, digest, and atomic behavior are defined.
- [ ] Precedence, duplicates, missing-file, unsupported-version, and unknown-key behavior are tested.
- [ ] Directory/filename presence cannot activate anything.
- [ ] Canonical object aliases and schema/contract authority are resolved.
- [ ] Habitat seven-role and machine SourceDescriptor vocabularies have an accepted mapping.
- [ ] Source registry topology and stable descriptor references are resolved.
- [ ] Generic shared trust-object versus Habitat profile authority is resolved.
- [ ] `biotopes` compatibility paths cannot become authority.
- [ ] Habitat remains landscape, not species occurrence, title, ownership, access, or legal advice.
- [ ] Modeled Habitat remains distinct from observation and regulatory designation.
- [ ] Spatial, temporal, model, uncertainty, freshness, stale, supersession, and correction semantics are explicit.
- [ ] Rights, terms, attribution, reuse, access, and source freshness are reviewed.
- [ ] Sensitivity/geoprivacy parameters come from accepted profiles and are reconstruction-tested.
- [ ] Join-induced sensitivity, low counts, differencing, parcel intersection, and cross-layer risk are tested.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, stale, partial, conflicted, and error cases.
- [ ] No-network, no-auto-discovery, deterministic, no-secret, and public-path tests pass.
- [ ] Placeholder schemas/validators/workflows are not represented as enforcement.
- [ ] Affected-output discovery and cache/tile/index/export/AI invalidation are tested.
- [ ] Deactivation, migration, correction, supersession, rollback, and replay are tested.
- [ ] No source, model, public layer, API route, release, or publication is activated by config presence.

[Back to top](#top)

---

## Open verification register

| ID | Item | Status | Resolution |
|---|---|---:|---|
| `HAB-CFG-001` | Accepted owners/CODEOWNERS | `OWNER_TBD` | Assign config, Habitat, model, sensitivity, validation, release owners. |
| `HAB-CFG-002` | Executable config consumer | `NOT OBSERVED` | Identify exact import/command/service and tests. |
| `HAB-CFG-003` | Loader/discovery/precedence contract | `UNKNOWN` | Consumer contract and negative tests. |
| `HAB-CFG-004` | First payload format/schema | `NEEDS VERIFICATION` | Closed schema/profile plus fixtures. |
| `HAB-CFG-005` | Habitat versus SourceDescriptor role mapping | `CONFLICTED` | Accepted mapping/version and anti-upgrade tests. |
| `HAB-CFG-006` | HabitatPatch canonical contract path | `CONFLICTED` | Migration/ADR and schema pointer update. |
| `HAB-CFG-007` | SuitabilityModel canonical contract path/case | `CONFLICTED` | Migration/ADR and compatibility tests. |
| `HAB-CFG-008` | ModelRunReceipt canonical placement | `CONFLICTED` | Object-family ownership decision. |
| `HAB-CFG-009` | Habitat-local versus shared trust-object schemas | `CONFLICTED` | Shared authority/domain-profile decision. |
| `HAB-CFG-010` | Source registry topology | `CONFLICTED` | One canonical record home plus redirects/migration. |
| `HAB-CFG-011` | Canonical Habitat triplet child path | `NEEDS VERIFICATION` | Data/graph placement decision. |
| `HAB-CFG-012` | Biotopes compatibility disposition | `CONFLICTED` | Retain guardrail, redirect, migrate, or remove via governed decision. |
| `HAB-CFG-013` | Habitat package implementation/exports | `NOT ESTABLISHED` | Complete package and tests. |
| `HAB-CFG-014` | Habitat pipelines | `PLACEHOLDER` | Implement bounded stages and receipts. |
| `HAB-CFG-015` | Habitat schemas | `PERMISSIVE SCAFFOLDS IN INSPECTED SLICE` | Expand contract/schema/fixtures/validators together. |
| `HAB-CFG-016` | Habitat policy enforcement | `NOT ESTABLISHED` | Coherent policy modules, fixtures, tests, runtime wiring. |
| `HAB-CFG-017` | Habitat validators | `PLACEHOLDER` | Implement deterministic validators and negative cases. |
| `HAB-CFG-018` | Habitat workflow enforcement | `TODO SCAFFOLD` | Replace echoes with substantive required checks. |
| `HAB-CFG-019` | Source rights/current terms | `NEEDS VERIFICATION` | SourceDescriptor and steward review. |
| `HAB-CFG-020` | Model fitness and threshold semantics | `NEEDS VERIFICATION` | Model card/run/validation evidence. |
| `HAB-CFG-021` | Sensitivity/geoprivacy profiles | `NEEDS VERIFICATION` | Policy, transforms, receipts, reconstruction tests. |
| `HAB-CFG-022` | Derived-output dependency graph/invalidation | `NEEDS VERIFICATION` | Cache/tile/index/export/AI invalidation tests. |
| `HAB-CFG-023` | Release/correction/rollback integration | `UNKNOWN` | End-to-end governed flow and receipts. |

[Back to top](#top)

---

## Safe language guide

| Avoid | Prefer |
|---|---|
| “The Habitat system uses this config.” | “No indexed executable consumer was observed in the bounded search.” |
| “This config activates NLCD/the model.” | “Source/model activation remains a separate governed decision.” |
| “Habitat has seven source roles, so use that enum.” | “Habitat and shared SourceDescriptor vocabularies conflict; use an accepted mapping.” |
| “The schema validates HabitatPatch.” | “The inspected HabitatPatch schema is a permissive scaffold.” |
| “Policy denies unpublished Habitat.” | “The inspected deny module says no real rules exist and defaults deny to false.” |
| “The validator checks the model.” | “The inspected validator file is a placeholder.” |
| “CI validates and builds proof.” | “The inspected workflow contains TODO echo jobs.” |
| “This layer is habitat.” | “This layer represents a specific observed/modeled/regulatory/administrative Habitat product.” |
| “This is critical habitat.” | “This is an issuing-authority designation” or “this is modeled suitability,” as evidence supports. |
| “The patch proves the species occurs.” | “The patch is Habitat context; occurrence truth remains with Fauna/Flora.” |
| “The low zoom protects it.” | “Public-safe geometry requires governed transformation and reconstruction review.” |
| “Rollback the config and the problem is fixed.” | “Rollback also requires affected-output invalidation and correction/release closure.” |

[Back to top](#top)

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Prior target README | blob `a34dc7b…`, v0.3 | Strong prior config boundary and lane inventory. | Current surrounding implementation maturity. |
| Empty `.gitkeep` | empty blob `e69de29b…` | Non-semantic directory marker. | Payload, loader, or activation. |
| Parent domain-config README | blob `2c5e8b70…`, v0.4 | No-secrets/no-authority parent rules. | Habitat consumer wiring. |
| Bounded config-path search | target, parent, Habitat file-system plan | No indexed config consumer surfaced. | Exhaustive absence. |
| Habitat doctrine README | blob `876d1fa4…`, v1.1 | Landscape-not-species and seven-role doctrine. | Current implementation. |
| Habitat package metadata | blob `4de5519d…`, version `0.0.0` | Python package identity/scaffold. | Build/install/export behavior. |
| Habitat initializer | empty blob `e69de29b…` | Import namespace marker. | Exports or behavior. |
| Habitat package source search | README paths only | No indexed implementation. | Empty/unindexed files. |
| Habitat package/source READMEs | blobs `898b986c…`, `53176b1c…` | Proposed package boundaries. | Implemented helpers. |
| NLCD ingest placeholder | blob `7c41f4d4…` | Planned path exists. | Ingest behavior. |
| Habitat patch builder placeholder | blob `a89a8f46…` | Planned path exists. | Patch construction. |
| Suitability runner placeholder | blob `df8c45cd…` | Planned path exists. | Model execution. |
| Habitat pipeline README | blob `ee6458c5…` | Pipeline responsibility boundary. | Executable stages. |
| HabitatPatch schema | blob `a7ad7eaa…`, empty/permissive | Schema path/status. | Field-level semantics. |
| SuitabilityModel schema | blob `eae24fe7…`, empty/permissive | Schema path/status. | Model validation. |
| Habitat EvidenceBundle schema | blob `ab0e45ba…`, permissive domain copy | Potential domain profile/duplication. | Shared evidence authority. |
| Habitat ReleaseManifest schema | blob `8545bb02…`, permissive domain copy | Potential domain profile/duplication. | Release authority. |
| Habitat contracts README | blob `65b5b259…`, v0.2 draft | Semantic-contract lane. | Resolved aliases/schema enforcement. |
| HabitatPatch contract | blob `70a84b8f…`, v0.2 | Object meaning and duplicate-path conflict. | Field enforcement. |
| SuitabilityModel contract | blob `837ddaa3…`, v0.2 | Model meaning and path/case conflict. | Model fitness/runtime. |
| Shared SourceDescriptor schema | blob `582e70b8…`, fielded/closed | Rich machine source roles and governance fields. | Accepted mapping to Habitat seven roles. |
| Habitat source registry, subtype-first | blob `5d9c90f8…` | Candidate registry posture and topology conflict. | Canonical selection. |
| Habitat source registry, domain-first | blob `d49e4562…` | Companion topology exists. | Canonical selection. |
| Singular triplet compatibility README | blob `ee730f1f…` | Singular path is non-canonical. | Final Habitat child path under plural root. |
| Plural triplet parent README | blob `222277e0…` | Canonical parent lifecycle lane. | Habitat child placement. |
| Habitat policy README | blob `8456c651…`, greenfield scaffold | Policy path exists. | Mature policy. |
| `deny_unpublished.rego` | blob `47f05f89…`, no rules/default false | Confirms unsafe scaffold posture. | Deny enforcement. |
| model-card policy scaffold | blob `e51a9603…`, default allow false | Generated placeholder exists. | Complete policy. |
| Habitat validator placeholders | blobs `f1bf0c3d…`, `d0f7ad8d…`, `868b21ff…`, `2249e3c3…` | Planned validator paths. | Executable validation. |
| Habitat workflow | blob `5fbc8114…`, TODO echoes | Trigger/job scaffold. | Validation/proof/publish checks. |
| Contracts/schemas/policy Biotopes READMEs | compatibility guardrails | Non-canonical Biotopes posture. | Accepted runtime authority. |
| Directory Rules | blob `2affb080…`, v1.4 draft | Responsibility-root placement and README order. | Habitat runtime maturity. |
| Secrets standard | blob `562b654e…`, v0.1 draft | No-secrets/trust-membrane posture. | Deployed secret handling. |

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — no-loss preservation from v0.3</strong></summary>

v0.3 established:

- README + non-semantic `.gitkeep` inventory;
- no secrets or live bindings;
- non-authority of configuration;
- named consumer and explicit binding;
- minimum per-file contract;
- precedence and unknown-key posture;
- landscape-not-species ownership;
- seven-role Habitat vocabulary;
- model/regulatory/observation separation;
- spatial, temporal, model, sensitivity, geoprivacy, low-count, and join-risk semantics;
- validation, failure, review, maintenance, migration, anti-bypass, first-payload, related, ADR, rollback, and safe-language controls.

v0.4 preserves those controls and adds:

- current package/pipeline/schema/policy/validator/workflow maturity;
- source-role vocabulary conflict;
- object contract aliases;
- source-registry topology;
- generic trust-object duplication safeguard;
- triplet and Biotopes compatibility posture;
- explicit logging/data-minimization controls;
- cache/tile/search/vector/graph/export/Evidence Drawer/Focus Mode/AI invalidation;
- expanded verification register and evidence ledger.

No v0.3 safeguard is intentionally weakened.

</details>

<details>
<summary><strong>Appendix B — documentation-only change boundary</strong></summary>

This revision changes no:

- Habitat config payload or consumer;
- package metadata, exports, source code, dependency, or build behavior;
- connector, watcher, pipeline, model, or validator implementation;
- source registry record, source activation, rights, sensitivity, or source role;
- contract or schema;
- policy or policy runtime;
- fixture, test, or workflow;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- receipt, proof, EvidenceBundle, catalog, graph, release, correction, withdrawal, or rollback object;
- tile, cache, index, export, dashboard, screenshot, Evidence Drawer, Focus Mode, or AI output;
- API, UI, public, runtime, deployment, or publication behavior.

Only `configs/domains/habitat/README.md` changes.

</details>

## Status summary

`configs/domains/habitat/` remains a README-backed, non-secret, non-authoritative configuration boundary with no established payload or executable consumer. The surrounding Habitat lane is documentation-rich but implementation-light in the inspected slice: package metadata is `0.0.0`, pipelines and validators are placeholders, major object schemas are permissive, policy modules are scaffolds, and CI is TODO-only. Object paths, source-role vocabularies, source-registry topology, trust-object placement, triplet placement, and Biotopes compatibility remain conflicted or unresolved. The first operational config must bind to a named consumer, reference accepted authority, preserve landscape/species and model/regulatory distinctions, use accepted model and sensitivity profiles, validate deterministically, fail closed, and support correction plus complete derived-output invalidation.

<p align="right"><a href="#top">Back to top</a></p>
