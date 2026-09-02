<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-fauna-readme
title: configs/domains/fauna/ — Governed Fauna Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Fauna steward · Taxonomy steward · Source and rights steward · Sensitivity/geoprivacy steward · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; fauna; taxonomy-aware; source-role-aware; occurrence-class-aware; sensitivity-aware; geoprivacy-aware; reconstruction-resistant; rights-aware; time-aware; deny-by-default; non-secret; non-authoritative; no-live-binding; no-source-activation; no-exact-sensitive-location; no-release-authority"
current_path: configs/domains/fauna/README.md
truth_posture: CONFIRMED canonical Fauna config lane, parent configuration contract, repository-present Fauna doctrine and implementation-shaped surfaces, README-only bounded config inventory, source-first connector placement, noncanonical connectors/fauna compatibility index, canonical contracts/domains/fauna lane with contracts/fauna compatibility guard, subtype-first versus domain-first source-registry topology conflict, package version 0.0.0 placeholder, PROPOSED refresh spec, PROPOSED sensitivity YAML placeholders, default-deny Rego scaffold, permissive empty Fauna schemas, placeholder fixtures and release manifests, and TODO-only domain workflow / PROPOSED future consumer-bound templates and accepted profile references / CONFLICTED source-registry topology and compatibility-path cleanup / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, policy-runtime wiring, source activation, generated public derivatives, and publication use / NEEDS VERIFICATION accepted owners, canonical taxonomy resolver, source roles and rights, occurrence identity, temporal semantics, sensitivity tier transitions, geoprivacy parameters, reconstruction-risk controls, executable validation, branch protection, review enforcement, correction propagation, and rollback/invalidation integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a
  prior_blob: fdf1a884595de3d8e194ee162ae8f468a2aa547a
  bounded_path_search: configs/domains/fauna/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/ARCHITECTURE.md
  - ../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../docs/domains/fauna/OBJECT_FAMILIES.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/POLICY.md
  - ../../../docs/domains/fauna/API_CONTRACTS.md
  - ../../../docs/domains/fauna/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/fauna/RELEASE_INDEX.md
  - ../../../docs/domains/fauna/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/fauna/
  - ../../../contracts/fauna/README.md
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../schemas/contracts/v1/fauna/README.md
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../data/registry/sources/fauna/
  - ../../../data/registry/fauna/sources/
  - ../../../packages/domains/fauna/
  - ../../../pipelines/domains/fauna/
  - ../../../pipelines/ingest/fauna/
  - ../../../pipelines/normalize/fauna/
  - ../../../pipelines/rollback/fauna/
  - ../../../pipeline_specs/fauna/
  - ../../../tools/validators/fauna/
  - ../../../tools/validators/geoprivacy/habitat-fauna/
  - ../../../tests/domains/fauna/
  - ../../../fixtures/domains/fauna/
  - ../../../apps/explorer-web/src/features/domains/fauna/
  - ../../../connectors/fauna/README.md
  - ../../../data/raw/fauna/
  - ../../../data/work/fauna/
  - ../../../data/quarantine/fauna/
  - ../../../data/processed/fauna/
  - ../../../data/catalog/domain/fauna/
  - ../../../data/triplets/fauna/
  - ../../../data/published/layers/fauna/
  - ../../../data/receipts/fauna/
  - ../../../data/proofs/fauna/
  - ../../../data/rollback/fauna/
  - ../../../release/candidates/fauna/
  - ../../../release/manifests/
  - ../../../.github/workflows/domain-fauna.yml
tags: [kfm, configs, fauna, animals, wildlife, taxonomy, occurrence, range, monitoring, mortality, disease, invasive-species, source-role, sensitivity, geoprivacy, reconstruction-risk, rights, time, no-secrets, governance]
notes:
  - "The bounded repository search for configs/domains/fauna returned this README only. No executable Fauna configuration payload or indexed direct consumer was found."
  - "The prior v0.2 README already carried strong taxonomy, source-role, occurrence-class, T4 sensitivity, geoprivacy, reconstruction-risk, validation, correction, and rollback controls. v0.3 preserves them and adds current repository evidence, implementation maturity, path conflicts, object-family boundaries, consumer-binding rules, cache/log invalidation, and stricter first-payload gates."
  - "The repository contains many Fauna implementation-shaped files, but inspected package metadata, pipeline specs, sensitivity files, Rego policy, JSON Schemas, fixtures, release templates, and workflow jobs remain version-0.0.0, PROPOSED placeholders, empty-permissive scaffolds, or TODO-only and do not prove production behavior."
  - "Source-specific connector implementations are canonical under connectors/<source_id>/. connectors/fauna/ is a noncanonical compatibility index and must not become a parallel implementation hierarchy."
  - "The repository contains both data/registry/sources/fauna/ and data/registry/fauna/sources/. This README does not select or duplicate records across them; topology remains a drift item requiring migration or ADR-backed resolution."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Fauna Domain Configuration

`configs/domains/fauna/`

> Safe-to-commit configuration documentation and future consumer-bound templates for animal taxonomy references, occurrence processing, monitoring, ranges, seasonal context, mortality, disease, invasive-species records, public-safe derivatives, and review routing. This lane is not animal truth, taxonomic authority, source admission, sensitivity policy, geoprivacy authority, evidence, release, or publication authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![sensitivity](https://img.shields.io/badge/sensitive__occurrence-T4__default-critical)
![roles](https://img.shields.io/badge/source__roles-no__collapse-purple)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Classes](#configuration-classes) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#fauna-object-family-boundaries) · [Taxonomy](#taxonomy-identity-and-status) · [Roles](#source-role-and-evidence-character) · [Occurrences](#occurrence-monitoring-range-and-candidate-boundaries) · [Time](#time-seasonality-freshness-and-correction) · [Space](#spatial-support-precision-and-reconstruction-risk) · [Geoprivacy](#sensitivity-geoprivacy-and-tier-motion) · [Rights](#source-rights-attribution-and-stewardship) · [Connectors](#connector-and-source-registry-boundaries) · [Logging](#logging-telemetry-caches-and-derived-indexes) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-supersession-and-invalidation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`
> **Observed lane maturity:** README-only in the bounded config-path search; no executable Fauna configuration payload or direct consumer binding is established
> **Authority:** implementation-supporting configuration sublane; non-authoritative for taxonomy, occurrence meaning, source admission, sensitivity, geoprivacy, evidence, policy, review, release, or publication
> **Runtime posture:** no loader, precedence rule, network fetch, source activation, taxonomy resolution, occurrence processing, public-layer generation, release, or publication is established by this README

> [!CAUTION]
> Exact or reconstructable sensitive occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry paths, steward-controlled records, observer or landowner details, and protected collection or rehabilitation locations fail closed. A configuration value cannot lower sensitivity, turn restricted evidence into public evidence, convert a model or range into an observation, make an aggregator authoritative, authorize a transform, or create a release. Missing source role, taxonomy, time, rights, evidence, policy, review, redaction, release, correction, or rollback support must not become implicit permission.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `fauna` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, profile references, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, route, label, generalize, render, cache, or package already-governed Fauna material, but they cannot decide:

- which taxonomy, taxon identifier, synonym, or crosswalk is controlling;
- whether a conservation or legal status is authoritative, current, or applicable to a place and time;
- whether a record is observed, reported, inferred, modeled, predicted, aggregated, contextual, candidate, restricted, generalized, or released;
- whether two occurrence, specimen, monitoring, telemetry, acoustic, eDNA, mortality, disease, or invasive-species records refer to the same real-world event;
- whether a source is admitted, active, rights-cleared, redistributable, current, or authoritative for a requested claim;
- whether a source accessed through an aggregator inherits the aggregator's authority;
- whether exact or generalized geometry is safe to expose;
- whether a geoprivacy transform is adequate;
- whether a timestamp means observation time, event time, reporting time, ingestion time, valid time, embargo expiry, release time, or correction time;
- whether a range, seasonal range, migration route, habitat association, or density surface supports direct occurrence;
- whether a public map, API, export, cache, log, or AI answer resists reconstruction;
- whether evidence supports a claim;
- whether an artifact may be promoted, released, rendered, indexed, exported, summarized, or published.

This README is intended for configuration maintainers, Fauna stewards, taxonomy and source reviewers, sensitivity and geoprivacy stewards, rights and stewardship reviewers, consumer owners, validation and test owners, policy and release reviewers, security reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Fauna domain meaning | **None.** Human doctrine remains under `docs/domains/fauna/`; semantic meaning remains in accepted contract homes. |
| Taxonomic identity | **None.** Config may reference a reviewed taxonomy or crosswalk profile; it cannot resolve conflicts or create canonical identity. |
| Conservation and legal status | **None.** Config cannot make an aggregator, cached list, model, or local mapping authoritative. |
| Occurrence and monitoring meaning | **None.** Config cannot turn candidate, modeled, range, contextual, or aggregate material into direct occurrence evidence. |
| Source identity and activation | **None.** Config may reference reviewed source IDs or profiles; it cannot admit, activate, suspend, retire, or supersede a source. |
| Source role and evidence character | **None.** Config cannot relabel authority, observation, aggregator, context, model, candidate, or restricted material. |
| Sensitivity and geoprivacy | **None.** Config may select an accepted policy profile; it cannot define, weaken, approve, or override a transform. |
| Temporal and spatial support | **None.** Config cannot invent observation time, seasonal scope, precision, geometry support, or freshness. |
| Evidence and claim truth | **None.** Config cannot create an `EvidenceBundle`, close proof, validate a claim, or convert a candidate into truth. |
| Policy and review | **None.** Config cannot substitute for accepted executable policy, a `PolicyDecision`, source review, redaction review, or release review. |
| Release and publication | **None.** Config cannot authorize lifecycle promotion, public map/API/UI use, export, Focus Mode, AI response, or publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and deterministic precedence. |

A configuration value may point to authority. It cannot acquire that authority through naming, placement, parsing, repetition, successful validation, a passing scaffold workflow, or use by a UI.

[Back to top](#top)

---

## Status

### Repository snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Evidence commit | `b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a` |
| Prior README blob | `fdf1a884595de3d8e194ee162ae8f468a2aa547a` |
| Bounded config-path result | `configs/domains/fauna/README.md` only |

### Evidence ledger

| Surface | CONFIRMED repository evidence | Safe conclusion |
|---|---|---|
| Config lane | This README exists; bounded search returned no other file under `configs/domains/fauna/`. | **README-only boundary.** No payload, loader, or direct consumer is established. |
| Parent config contract | `configs/domains/README.md` exists and defines domain config as non-secret and non-authoritative. | This child must inherit the parent no-authority and no-live-binding rules. |
| Fauna doctrine | `docs/domains/fauna/` contains README, architecture, canonical-path, lifecycle, object, source, sensitivity, policy, API, map/UI, release, and backlog documents. | Strong human-facing doctrine exists; it is not runtime proof. |
| Canonical contracts | `contracts/domains/fauna/` contains semantic object-family Markdown. | Semantic surfaces exist; acceptance and enforcement remain separate questions. |
| Contract compatibility path | `contracts/fauna/README.md` is a deprecated compatibility guard pointing to `contracts/domains/fauna/`. | Do not create parallel contract authority. |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` contains Draft 2020-12 files such as `occurrence_public.schema.json`. | Inspected schemas remain **PROPOSED empty-permissive scaffolds** with `{}` properties and `additionalProperties: true`. |
| Sensitivity policy | `policy/sensitivity/fauna/` contains YAML and Rego files. | Inspected YAML files are placeholders; the Rego file is a default-deny scaffold, not proven enforcement. |
| Package | `packages/domains/fauna/pyproject.toml` declares `kfm-domain-fauna` version `0.0.0`. | Package presence is scaffold evidence, not implemented behavior. |
| Pipeline specification | `pipeline_specs/fauna/refresh.yaml` exists. | It is a `PROPOSED` placeholder generated from docs inventory. |
| Fixtures | `fixtures/domains/fauna/` contains valid, invalid, and synthetic paths. | Inspected fixture is a placeholder record, not a behavioral proof fixture. |
| Release templates | `release/manifests/` contains Fauna template JSON files. | Inspected template is a `PROPOSED` placeholder, not a release manifest. |
| Workflow | `.github/workflows/domain-fauna.yml` exists. | Jobs only echo TODO messages; workflow presence does not prove validation, proof building, or release dry-run behavior. |
| Source-first connector policy | `connectors/fauna/README.md` exists as a noncanonical compatibility index. | Runtime connector implementations belong under `connectors/<source_id>/`; no parallel fauna connector hierarchy. |
| Source registry | Both `data/registry/sources/fauna/` and `data/registry/fauna/sources/` exist. | Topology is **CONFLICTED / NEEDS VERIFICATION**; do not maintain divergent records. |
| Explorer feature lane | `apps/explorer-web/src/features/domains/fauna/README.md` exists. | UI documentation or scaffolding is downstream and does not prove safe public runtime behavior. |
| Published/lifecycle lanes | README-backed Fauna paths exist under processed, published, proof, receipt, rollback, and related roots. | Directory and README presence does not prove emitted artifacts, evidence closure, policy approval, or release. |

### Maturity matrix

| Capability | Status | Safe conclusion |
|---|---:|---|
| Config-boundary README | **CONFIRMED** | The lane is documented. |
| Executable config payload | **NOT ESTABLISHED** | No non-README payload found in the bounded config search. |
| Direct consumer binding | **UNKNOWN** | No package, pipeline, app, or runtime is proven to load this lane. |
| Config precedence and discovery | **UNKNOWN** | No deterministic load, merge, or unknown-key rule is established. |
| Taxonomy resolver | **NEEDS VERIFICATION** | Taxonomy and crosswalk decisions remain governed concerns. |
| Source activation | **NOT AUTHORIZED** | Config presence must not activate connectors or sources. |
| Sensitivity/geoprivacy enforcement | **SCAFFOLD ONLY** | Default-deny doctrine is strong; parameter files and executable integration are not proven. |
| Schema validation | **SCAFFOLD ONLY** | Present Fauna schemas are not yet restrictive enough to prove object validity. |
| Fixtures/tests | **PLACEHOLDER / NEEDS VERIFICATION** | Named paths exist; behavioral coverage is not proven. |
| CI enforcement | **TODO SCAFFOLD** | `domain-fauna.yml` does not execute substantive validation. |
| Release/publication | **NOT ESTABLISHED** | Templates and README lanes are not releases. |
| Owners/CODEOWNERS | **UNKNOWN** | `OWNER_TBD` remains unresolved. |

Directory presence must not trigger discovery, network access, source activation, indexing, taxonomy resolution, geometry transformation, map-layer creation, AI interpretation, lifecycle promotion, release, or publication.

[Back to top](#top)

---

## What belongs here

Only small, safe-to-commit Fauna configuration material for a named or explicitly proposed consumer belongs here.

| Accepted material | Purpose | Minimum posture |
|---|---|---|
| Domain child `README.md` | Define the Fauna configuration boundary. | Preserve parent config law, source-role separation, T4 default, and no-live-binding. |
| `*.template.yaml` / `*.template.yml` | Placeholder-based template for a named consumer. | Parseable, versioned, placeholders only, no secrets, inactive by default. |
| `*.example.yaml` / `*.example.json` / `*.example.toml` | Tiny synthetic example. | Fictional taxa, locations, sources, times, and identifiers; no reconstruction path. |
| Profile references | Select an accepted taxonomy, source-role, sensitivity, generalization, display, freshness, or review profile. | Stable identifier only; config does not embed or redefine policy. |
| Conservative review defaults | Select deny, hold, abstain, quarantine, generalize, or steward-review routing. | Cannot reduce review burden. |
| Public-safe display hints | Select an accepted generalized display profile or field allowlist. | Must not contain protected geometry or grant exposure. |
| Migration notes | Document a real key or path transition. | Owner-linked, time-bounded, reversible, and not a parallel authority. |
| Validation notes | Explain consumer-specific validation commands. | Commands must be verified or labeled `PROPOSED`. |

Synthetic examples must not resemble real occurrences, observers, telemetry paths, sites, properties, rehabilitation facilities, collections, or protected locations closely enough to enable reconstruction.

[Back to top](#top)

---

## What does not belong here

- real occurrences, observations, surveys, telemetry, tracking, eDNA, acoustic, specimen, mortality, disease, rehabilitation, rescue, invasive-species, or source payloads;
- exact or reconstructable nests, dens, roosts, hibernacula, spawning sites, breeding sites, congregation sites, nursery areas, migration paths, or steward-controlled geometry;
- observer, researcher, volunteer, landowner, permit-holder, patient, rehabilitation-client, or other living-person data;
- rights-restricted media, media metadata, EXIF, collection details, access-control detail, or steward-only notes;
- credentials, tokens, cookies, signed URLs, connection strings, private endpoints, workstation paths, or deployment bindings;
- source admission, activation, authority-role, rights, license, redistribution, cadence, or retirement decisions;
- taxonomy authority, synonym adjudication, taxon merge/split decisions, conservation status, or legal status;
- geoprivacy radii, randomization distributions, withholding logic, tier transition criteria, or transform implementation;
- schemas, semantic contracts, executable policy, registry records, receipts, proofs, manifests, release decisions, correction notices, or rollback cards;
- values that present modeled range, habitat suitability, density estimation, candidate detections, inferred presence, environmental association, or AI interpretation as observed occurrence truth;
- values that let GBIF, eBird, iNaturalist, iDigBio, BISON-like systems, or another access platform stand in as the original evidence authority;
- hidden bypasses for sensitivity, rights, review, quarantine, deny, abstain, redaction, release, or correction gates;
- automatic config discovery based only on directory or filename presence;
- connector code or source clients under `configs/` or `connectors/fauna/`.

[Back to top](#top)

---

## Inputs

A future Fauna configuration payload requires all of the following before it may be treated as consumer-ready:

1. **Named consumer** — exact package, app, pipeline, service, runtime, test harness, or tool.
2. **Accepted owners** — accountable consumer, config, Fauna, sensitivity, validation, and release roles as applicable.
3. **Declared format** — file type, format version, canonical parser, and encoding.
4. **Authority references** — verified semantic contract, schema, policy, source registry, and domain documentation.
5. **Synthetic or public-safe values** — no real occurrence, location, person, telemetry, media, source payload, or protected join.
6. **Source-role model** — original authority, observation, aggregator/access platform, context, model, candidate, and restricted roles remain distinguishable.
7. **Taxonomy posture** — vocabulary, resolver, authority version, synonym behavior, merge/split behavior, unresolved conflict behavior, and update cadence.
8. **Occurrence posture** — evidence, restricted, public derivative, range, seasonal range, migration, monitoring, mortality, disease, invasive, and candidate classes remain distinct.
9. **Temporal posture** — observation, event, valid, reporting, ingestion, embargo, freshness, release, correction, and supersession times are explicit.
10. **Sensitivity and geoprivacy review** — protected taxa, sensitive sites, exact geometry, private joins, temporal clues, identifier joins, and reconstruction risk are reviewed.
11. **Rights and stewardship review** — provider terms, attribution, redistribution, media, embargo, permit, and steward restrictions.
12. **Validation path** — deterministic parse, schema, semantic, source-role, taxonomy, temporal, sensitivity, reconstruction, rights, secret, and negative-case checks.
13. **Precedence rule** — interaction with repository defaults, environment, local overrides, deployment configuration, and runtime values.
14. **Unknown-key behavior** — reject, warn, or ignore; explicit and tested.
15. **Network posture** — no network by default; authorized live probes isolated from deterministic validation.
16. **Rollback and correction** — prior version, deactivation, cache/index invalidation, migration, correction, supersession, and rollback behavior.

A missing requirement leaves the payload **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION**. It does not become active by convention.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated file may support a verified consumer by selecting conservative, already-governed behavior such as:

- a named taxonomy or taxon-crosswalk profile;
- a source-role mapping profile;
- a restricted/public occurrence routing profile;
- a deny, hold, abstain, quarantine, or steward-review route;
- an accepted public-safe generalization or display profile;
- a field allowlist for an already-approved public derivative;
- a product-specific freshness or stale-state profile;
- cache and derived-index invalidation behavior;
- a migration compatibility window.

A configuration output cannot:

- admit or activate a source;
- create taxonomic, occurrence, conservation-status, or legal-status truth;
- create or approve a geoprivacy transform;
- issue a valid `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `EvidenceBundle`, `ReleaseManifest`, or rollback record merely by naming one;
- reveal a sensitive site or lower a sensitivity tier;
- write directly to a later lifecycle phase;
- authorize a public layer, API response, map display, AI answer, release, or publication.

[Back to top](#top)

---

## Validation

### Documentation validation

For this README:

- one H1 is present;
- headings are ordered and linkable;
- relative links remain inside known responsibility roots;
- the KFM metadata block retains its `doc_id` and `created` value;
- no real occurrence, person, media, telemetry, source, credential, or protected-location data is included;
- doctrine, current repository state, proposals, unknowns, conflicts, and verification needs remain distinct;
- scaffold presence is not described as working implementation.

### Future payload validation

| Validation layer | Required checks |
|---|---|
| Parse | Declared format and encoding parse deterministically. |
| Shape | Accepted schema validates every field; permissive scaffold schemas are insufficient for production claims. |
| Consumer binding | Named consumer, filename, format version, load path, and owner are verified. |
| Unknown keys | Behavior is explicit and covered by negative tests. |
| Precedence | Merge and override behavior is deterministic and tested. |
| Taxonomy | Authority, vocabulary version, synonyms, merge/split events, crosswalks, and unresolved conflicts remain explicit. |
| Source roles | Original source role survives aggregation and delivery; access platform does not become authority. |
| Occurrence split | Evidence, restricted record, public derivative, range, model, context, and candidate remain separate. |
| Sensitivity | T4 records and protected sites fail closed; policy references resolve. |
| Geoprivacy | Selected profile is governed, versioned, reviewable, and cannot be weakened by local override. |
| Reconstruction | Coordinates, time, identifiers, joins, media metadata, counts, logs, caches, and tiles are tested for indirect disclosure. |
| Rights | Provider, steward, attribution, redistribution, media, embargo, permit, and private-person constraints resolve. |
| Temporal | Observation/event/reporting/ingestion/valid/embargo/freshness/release/correction times remain distinguishable. |
| Spatial support | Point, generalized point, cell, polygon, range, corridor, route, and aggregate support remain explicit. |
| Network | Deterministic tests use no live network; authorized probes are isolated and redacted. |
| Secrets | No credential, token, private endpoint, or sensitive operational value is present. |
| Logging/cache | Logs, telemetry, cache keys, previews, indexes, and errors do not disclose protected material. |
| Rollback | Prior config, deactivation, invalidation, correction, and rollback behavior are documented and tested. |

Executable configuration validation remains **NOT APPLICABLE** while this lane contains no payload and no verified consumer.

### Required negative cases

- unknown taxon or unresolved taxonomy conflict;
- taxon merge/split without versioned identity handling;
- aggregator/access platform presented as original evidence authority;
- stale legal or conservation status presented as current;
- model, range, habitat, or density product presented as direct observation;
- candidate promoted without confirming evidence;
- restricted occurrence routed to a public profile;
- exact sensitive site requested for public use;
- missing or invalid policy, review, redaction, evidence, or release reference;
- protected geometry reconstructed from time, identifiers, counts, tile boundaries, media, or joins;
- observer, landowner, telemetry, collection, disease, rehabilitation, or media metadata leakage;
- stale, partial, unavailable, embargoed, withdrawn, or superseded source state;
- malformed file, unknown key, unsupported version, ambiguous precedence, or missing rollback target;
- duplicate records maintained across both Fauna source-registry topologies;
- config pointing to noncanonical connector or contract implementation paths.

[Back to top](#top)

---

## Review burden

README changes require:

- config or documentation review; and
- Fauna domain review.

A future payload also requires the applicable:

- named consumer owner;
- taxonomy reviewer;
- source-role and source-rights reviewer;
- sensitivity and geoprivacy reviewer;
- steward or rights-holder representative where protected records are implicated;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- policy reviewer;
- release and rollback reviewer.

Do not infer acceptance from a missing reviewer rule, repository path, scaffold file, or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Related folders

### Configuration and doctrine

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/fauna/README.md`](../../../docs/domains/fauna/README.md) — Fauna lane doctrine.
- [`../../../docs/domains/fauna/ARCHITECTURE.md`](../../../docs/domains/fauna/ARCHITECTURE.md) — architecture boundary.
- [`../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../docs/domains/fauna/CANONICAL_PATHS.md) — placement register.
- [`../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../docs/domains/fauna/DATA_LIFECYCLE.md) — lifecycle and promotion posture.
- [`../../../docs/domains/fauna/SENSITIVITY.md`](../../../docs/domains/fauna/SENSITIVITY.md) — deny-by-default sensitivity posture.
- [`../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../docs/domains/fauna/SOURCE_REGISTRY.md) and [`SOURCE_ROLES.md`](../../../docs/domains/fauna/SOURCE_ROLES.md) — source identities and roles.
- [`../../../docs/domains/fauna/POLICY.md`](../../../docs/domains/fauna/POLICY.md) — policy-oriented documentation.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved topology and compatibility drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — responsibility-root placement law.

### Authority and implementation-shaped surfaces

- [`../../../contracts/domains/fauna/`](../../../contracts/domains/fauna/) — canonical semantic contract lane.
- [`../../../contracts/fauna/README.md`](../../../contracts/fauna/README.md) — compatibility guard; no parallel authority.
- [`../../../schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/) — Fauna machine-shape scaffolds.
- [`../../../policy/domains/fauna/`](../../../policy/domains/fauna/) and [`../../../policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/) — policy and sensitivity scaffolds.
- [`../../../data/registry/sources/fauna/`](../../../data/registry/sources/fauna/) — subtype-first source registry lane.
- [`../../../data/registry/fauna/sources/`](../../../data/registry/fauna/sources/) — domain-first sibling requiring topology resolution.
- [`../../../packages/domains/fauna/`](../../../packages/domains/fauna/) — package scaffold.
- [`../../../pipelines/domains/fauna/`](../../../pipelines/domains/fauna/) and [`../../../pipeline_specs/fauna/`](../../../pipeline_specs/fauna/) — executable/specification lanes.
- [`../../../tools/validators/fauna/`](../../../tools/validators/fauna/) — validator documentation/scaffolding.
- [`../../../tests/domains/fauna/`](../../../tests/domains/fauna/) and [`../../../fixtures/domains/fauna/`](../../../fixtures/domains/fauna/) — proof and synthetic fixtures.
- [`../../../apps/explorer-web/src/features/domains/fauna/`](../../../apps/explorer-web/src/features/domains/fauna/) — downstream explorer feature lane.
- [`../../../connectors/fauna/README.md`](../../../connectors/fauna/README.md) — noncanonical compatibility index; runtime connector work remains source-first.
- [`../../../.github/workflows/domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) — TODO workflow scaffold.

[Back to top](#top)

---

## ADRs and drift triggers

This README introduces no ADR.

A reviewed ADR, correction, or migration decision is required before:

- adding, renaming, merging, or retiring the `fauna` domain slug;
- selecting a canonical taxonomy resolver or crosswalk-conflict policy;
- changing sensitive-taxon tiers or geoprivacy parameters;
- selecting canonical topology between `data/registry/sources/fauna/` and `data/registry/fauna/sources/`;
- turning `connectors/fauna/` into an implementation hierarchy;
- moving durable semantic contracts into `contracts/fauna/`;
- adopting a compatibility schema path as canonical over `schemas/contracts/v1/domains/fauna/`;
- establishing universal config discovery, precedence, or unknown-key behavior;
- allowing configuration to lower policy or review burden;
- authorizing direct public access to internal or canonical stores;
- changing the separation among configuration, evidence, policy, review, release, correction, and publication.

Configuration must not settle these decisions indirectly.

[Back to top](#top)

---

## Scope and bounded context

The Fauna config lane supports consumer behavior only after domain meaning and governance are supplied elsewhere.

```text
docs/domains/fauna/                 = human doctrine and orientation
contracts/domains/fauna/            = semantic meaning
schemas/contracts/v1/domains/fauna/ = machine shape
policy/domains/fauna/               = domain admissibility
policy/sensitivity/fauna/           = sensitivity and geoprivacy decisions
data/registry/sources/fauna/        = source identity/admission posture
connectors/<source_id>/             = source-specific acquisition
packages/pipelines/apps/tools/      = implementation and delivery
data/<phase>/fauna/                 = lifecycle material
release/                            = promotion, publication, correction, rollback
configs/domains/fauna/              = safe non-secret consumer configuration only
```

A value in this lane may select an accepted profile. It must not copy the authority data into config or create an alternate truth surface.

[Back to top](#top)

---

## Configuration classes

| Class | Example use | Default posture |
|---|---|---|
| `taxonomy_profile` | Select accepted taxon vocabulary/crosswalk behavior for a named consumer. | Inactive until resolver, authority version, and conflict behavior are verified. |
| `source_role_profile` | Select reviewed mapping from source descriptor roles into consumer behavior. | No local role upgrades. |
| `occurrence_routing_profile` | Route evidence into restricted review, public-derivative preparation, or hold. | Restricted by default; config cannot approve publication. |
| `sensitivity_profile` | Reference accepted T-tier and geoprivacy policy. | Reference only; no inline policy. |
| `public_safe_display_profile` | Select field allowlist, generalized geometry class, precision label, or zoom behavior already approved elsewhere. | Must not expose exact or reconstructable material. |
| `freshness_profile` | Select accepted product-specific stale and expiry handling. | Stale never becomes current silently. |
| `review_routing_profile` | Select required reviewer classes for defined conditions. | Cannot remove required review. |
| `cache_invalidation_profile` | Define how a verified consumer invalidates derived caches after source, taxonomy, policy, correction, or release changes. | Fail closed when invalidation cannot be proven. |
| `migration_profile` | Support temporary key or path transitions. | Time-bounded, reversible, and never a second authority. |

Avoid generic booleans such as `trusted`, `safe`, `public`, `sensitive=false`, `allow_exact`, or `skip_review`. They collapse multiple governed decisions.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should document or carry the following information in the repository-approved form.

| Field | Required meaning |
|---|---|
| `config_id` | Stable identifier for the configuration object. |
| `config_version` | Version of the configuration shape and values. |
| `domain` | Exactly `fauna`; config cannot create a domain alias. |
| `consumer_id` | Exact component that reads the file. |
| `owner_refs` | Verified accountable roles or owners. |
| `format_version` | Parser/shape version. |
| `contract_ref` / `schema_ref` | Canonical semantic and machine-shape references. |
| `policy_profile_refs` | Accepted policy references; no embedded replacement rules. |
| `source_registry_refs` | Stable references to reviewed source records. |
| `taxonomy_profile_ref` | Accepted taxonomy/crosswalk profile. |
| `source_role_profile_ref` | Accepted role vocabulary and mapping. |
| `occurrence_profile_ref` | Accepted class/routing profile. |
| `sensitivity_profile_ref` | Accepted sensitivity/geoprivacy profile. |
| `temporal_profile_ref` | Time, seasonality, freshness, embargo, and correction semantics. |
| `public_safe_profile_ref` | Approved display or transform profile reference. |
| `unknown_key_behavior` | Reject, warn, or ignore; explicit and tested. |
| `precedence` | Exact merge and override order. |
| `network_posture` | No network by default unless explicitly reviewed. |
| `logging_posture` | Redaction/minimization rules for logs, errors, analytics, and support bundles. |
| `failure_posture` | Finite reason-coded fail-closed behavior. |
| `migration` | Deprecated keys, replacement, compatibility window, and correction path. |
| `rollback` | Prior known-good version, deactivation, invalidation, and restoration method. |

Do not place unresolved owners, policy decisions, geoprivacy parameters, or sensitive values into machine-parsed payloads merely to fill fields.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No consumer should discover or load this directory merely because it exists.

A valid binding requires:

1. explicit consumer code or declarative binding;
2. exact supported path and filename;
3. supported config version;
4. accepted parser and validation path;
5. deterministic precedence;
6. unknown-key behavior;
7. environment/local/deployment override rules;
8. safe failure if the file is missing, stale, invalid, or incompatible;
9. audit of the effective configuration without logging sensitive values;
10. deactivation and rollback behavior.

Recommended precedence is **PROPOSED**, not current fact:

```text
embedded safe defaults
  < reviewed domain config
  < deployment-specific non-secret config
  < secret-manager values outside the repository
```

Local or environment overrides must never lower sensitivity, bypass review, change source role, or make unreleased material public.

[Back to top](#top)

---

## Fauna object-family boundaries

| Object family | Configuration may select | Configuration must not decide |
|---|---|---|
| `Taxon` / `TaxonCrosswalk` | Resolver/profile identifier and display preferences. | Canonical identity, synonym adjudication, merge/split truth, or authority. |
| `ConservationStatus` | Accepted status-source profile and display label policy. | Legal or conservation status. |
| `OccurrenceEvidence` | Parsing/routing profile and field handling for a named consumer. | Whether evidence is true or publishable. |
| `OccurrenceRestricted` | Restricted storage/review route. | Public exposure or tier reduction. |
| `OccurrencePublic` | Approved derivative/display profile reference. | Creation or approval of the derivative. |
| `RangePolygon` / `SeasonalRange` | Rendering, temporal-filter, and precision labels. | Direct occurrence confirmation or unsupported precision. |
| `MigrationRoute` | Public-safe representation profile. | Exact route exposure or observation equivalence. |
| `SensitiveSite` | Hold/deny/review routing. | Release, public geometry, or sensitivity downgrade. |
| `MonitoringEvent` | Method/time/quality profile reference. | Confirmation of taxon presence beyond evidence support. |
| `MortalityObservation` | Review, redaction, and display profile reference. | Cause attribution or sensitive-location release. |
| `DiseaseObservation` | Restricted/public-health review route. | Diagnosis, clinical advice, or exact sensitive facility/location disclosure. |
| `InvasiveSpeciesRecord` | Accepted source-role and public display profile. | Confirmation or legal designation by configuration alone. |
| `RedactionReceipt` | Receipt reference. | Receipt issuance or validity. |

[Back to top](#top)

---

## Taxonomy identity and status

- Preserve original source taxon identifiers and authority names.
- Pin taxonomy or vocabulary version where material.
- Treat synonyms and crosswalks as versioned relations, not silent replacements.
- Preserve unresolved conflicts and taxon merge/split history.
- Do not let consumer-friendly labels overwrite canonical identifiers.
- Do not use conservation or legal status from an aggregator unless the underlying authority and scope resolve.
- Status must retain jurisdiction, effective time, source, and supersession state.
- A config update cannot silently rekey public or restricted records after taxonomy changes.
- Taxonomy changes must trigger review of caches, indexes, tiles, reports, and cross-lane relations.

[Back to top](#top)

---

## Source role and evidence character

| Role | Required treatment |
|---|---|
| Original authority | Retain authority scope and limitations; never inferred from access path. |
| Direct observation source | Preserve method, time, observer/provenance, uncertainty, sensitivity, and rights. |
| Aggregator/access platform | Preserve original provider and record-level restrictions; access platform is not automatically evidence authority. |
| Context source | Supports interpretation only; cannot confirm taxon presence or legal status. |
| Model/derived product | Preserve method, version, training/support data, uncertainty, spatial/temporal scope, and derivative status. |
| Candidate/detection | Remains unconfirmed until governed evidence and review close the claim. |
| Restricted/steward source | Remains access-controlled and deny-by-default for public exact details. |

Configuration must never collapse these into a generic `trusted`, `verified`, `authoritative`, or `public` flag.

[Back to top](#top)

---

## Occurrence, monitoring, range, and candidate boundaries

- `OccurrenceEvidence` is source-bound evidence before public/restricted disposition.
- `OccurrenceRestricted` preserves exact or steward-controlled material under governed access.
- `OccurrencePublic` is a downstream public-safe derivative after evidence, policy, review, transform, receipt, and release gates.
- Range, seasonal range, migration, habitat, occupancy, density, suitability, and distribution products are not substitutes for occurrence evidence.
- Acoustic, eDNA, telemetry, camera, specimen, survey, checklist, mortality, disease, and invasive records retain method-specific semantics.
- Absence of a record is not species absence unless sampling design and evidence support that claim.
- A threshold, score, model probability, or AI interpretation cannot promote a candidate into an occurrence.
- Duplicate detection and identity resolution must preserve source lineage and uncertainty.
- Public counts and aggregates must be tested for small-cell or rare-taxon disclosure.

[Back to top](#top)

---

## Time, seasonality, freshness, and correction

Where applicable, preserve:

- observation time;
- event interval;
- reporting or submission time;
- ingestion and processing time;
- model issue and valid time;
- seasonal or life-stage scope;
- embargo or withholding expiry;
- source update and freshness time;
- release time;
- correction, withdrawal, and supersession time.

Missing or ambiguous time should produce hold, abstain, denial, or error according to the accepted consumer contract. It must not produce apparently current truth.

A taxonomy update, status change, source correction, embargo expiry, policy change, or release withdrawal must trigger review of affected derived caches and public carriers.

[Back to top](#top)

---

## Spatial support, precision, and reconstruction risk

Fauna material may use:

- exact restricted point or track;
- generalized point;
- grid/cell;
- buffered or fuzzed geometry;
- polygon or range;
- seasonal polygon;
- corridor or route;
- county/watershed/ecoregion aggregate;
- withheld geometry with textual scope only.

The support type and precision class must remain explicit. A generalized point is not an exact point; a range is not an occurrence; a tile is not evidence.

Reconstruction review must consider:

- timestamps combined with observer or route histories;
- stable source identifiers joinable to external records;
- media EXIF, filenames, thumbnails, or URLs;
- low-count cells, rare-taxon labels, and small geographic units;
- tile boundaries, zoom levels, feature counts, and vector-tile attributes;
- parcel, trail, water-body, habitat, facility, rehabilitation, collection, or landowner joins;
- logs, cache keys, analytics, errors, screenshots, support bundles, and preview artifacts.

When reconstruction safety cannot be proven, deny, hold, abstain, omit, or use a governed generalization profile.

[Back to top](#top)

---

## Sensitivity, geoprivacy, and tier motion

- Sensitive occurrence and sensitive-site material defaults to **T4** under repository-present Fauna doctrine.
- Public exact sensitive-occurrence tiles and API responses are denied.
- Configuration cannot lower a tier.
- A T4 record may reach a public-safe derivative only through accepted policy, transform, review, receipt, evidence, release, correction, and rollback paths.
- Geoprivacy parameters belong in accepted policy or transform authority—not this directory.
- Local overrides must not weaken transform strength, field withholding, precision labels, or reviewer requirements.
- If a transform reference is missing, stale, unsupported, or incompatible, fail closed.
- A valid public derivative must retain precision/generalization status and the lineage needed to audit the transform without exposing restricted inputs.

The currently inspected sensitivity YAML files are placeholders. Do not treat their names as approved parameters.

[Back to top](#top)

---

## Source rights, attribution, and stewardship

Before a config references a source or output profile, verify:

- provider and original source identity;
- license and terms;
- attribution;
- redistribution and derivative permissions;
- commercial or public-use limits;
- media-specific terms;
- embargo and steward restrictions;
- API/download quotas and rate limits;
- permitted claim families;
- correction and takedown contacts;
- source version and freshness;
- restricted-person or private-land implications.

Public accessibility does not prove redistribution rights. Aggregation does not erase upstream restrictions.

[Back to top](#top)

---

## Connector and source-registry boundaries

### Connectors

Source-specific connector implementations belong under:

```text
connectors/<source_id>/
```

`connectors/fauna/` is a documented noncanonical compatibility index. Do not place source clients, fetchers, parsers, authentication, rate-limit logic, connector package metadata, tests, fixtures, or activation state there.

Connector output may enter Fauna RAW or QUARANTINE through governed source admission. A connector does not publish.

### Source registry

The repository contains both:

```text
data/registry/sources/fauna/
data/registry/fauna/sources/
```

Until topology is resolved:

- do not create duplicate SourceDescriptor records;
- do not let config choose between divergent copies;
- treat one lane as canonical only after accepted migration/ADR evidence;
- use pointers or compatibility records rather than synchronized manual duplicates;
- preserve correction and rollback for any migration.

[Back to top](#top)

---

## Logging, telemetry, caches, and derived indexes

A consumer must minimize and redact operational output.

Do not log:

- exact or reconstructable protected geometry;
- observer, landowner, permit, rehabilitation, collection, or private-person details;
- source credentials or signed URLs;
- restricted source payload fragments;
- sensitive taxon/site identifiers when a generalized code suffices.

Cache and index keys must not reveal restricted values.

Changes to any of these should trigger scoped invalidation:

- source activation or role;
- taxonomy or crosswalk version;
- legal/conservation status;
- sensitivity policy or transform profile;
- embargo state;
- public field allowlist;
- geometry generalization;
- correction, withdrawal, or release manifest.

Derived search, vector, graph, tile, report, and AI indexes remain rebuildable carriers. They do not become canonical truth.

[Back to top](#top)

---

## Failure behavior

A verified consumer must use finite, reason-coded, fail-closed outcomes. Names below are **PROPOSED** until code and tests confirm them.

| Condition | Safe disposition |
|---|---|
| Valid, authorized, non-sensitive configuration | `PASS` for internal validation; continue to governed processing. |
| Malformed file, unsupported version, or schema violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown taxon or unresolved crosswalk | `HOLD` or `ABSTAIN`; preserve competing identities. |
| Missing source role, rights, policy, review, transform, or release authority | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Restricted occurrence or sensitive site requested for public use | `DENY`. |
| Model, range, habitat, or candidate presented as observation | `FAIL` and `DENY` for consequential use. |
| Missing or stale evidence | `ABSTAIN`; do not substitute cache, model, or generated prose silently. |
| Unauthorized sensitivity reduction or bypass key | `FAIL` and `DENY`; audit without exposing values. |
| Source outage or incomplete data | Preserve stale/partial state; do not fabricate completeness. |
| Conflicting registry copies | `HOLD` or `ERROR`; do not pick by path convenience. |
| Consumer cannot determine precedence | `ERROR` or `HOLD`; do not merge unpredictably. |
| Cache/index invalidation cannot be proven | `HOLD` or `DENY` public reuse until rebuilt. |

`PASS` and `FAIL` are validator outcomes, not publication decisions.

[Back to top](#top)

---

## Governed AI and generated language

AI may help:

- summarize released, policy-safe `EvidenceBundle` material;
- explain taxonomy or source-role caveats;
- draft review notes;
- suggest a narrowed query;
- describe why an answer abstains or is denied.

AI must not:

- infer hidden sensitive locations;
- reconstruct exact sites from generalized outputs;
- upgrade source authority;
- resolve taxonomy or legal status without governed evidence;
- turn a range/model/candidate into an occurrence;
- issue geoprivacy, review, release, or publication decisions;
- present generated language as evidence;
- bypass finite `ANSWER | ABSTAIN | DENY | ERROR` outcomes.

Config may select a reviewed AI presentation profile. It cannot grant the model new evidence or access authority.

[Back to top](#top)

---

## Migration and anti-bypass posture

When adding or changing a Fauna config:

1. identify the exact consumer and owner;
2. pin the base commit and existing config blob;
3. inspect parent config and Fauna doctrine;
4. verify canonical contracts, schemas, policy, source registry, and compatibility paths;
5. preserve source-role and restricted/public occurrence separation;
6. review taxonomy, rights, sensitivity, geoprivacy, reconstruction, personal-data, and cross-lane risk;
7. run deterministic parse, shape, semantic, negative, and no-network checks;
8. inspect the complete diff for secrets and protected clues;
9. document precedence, unknown-key behavior, stale-state, migration, deactivation, correction, invalidation, and rollback;
10. verify remote read-back and changed paths;
11. keep release and publication as separate governed decisions.

Forbidden migration shortcuts:

- copy canonical contract content into config;
- duplicate source descriptors across both registry topologies;
- create connector code under `connectors/fauna/`;
- create durable contracts under `contracts/fauna/`;
- use permissive scaffold schemas as production proof;
- treat TODO workflows as enforcement;
- add a `skip_review`, `allow_exact`, or `public=true` escape hatch.

[Back to top](#top)

---

## Rollback, correction, supersession, and invalidation

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request that restores the prior known-good README or configuration version. Do not force-push shared history.

For a future payload correction:

1. disable or stop selecting the affected configuration through the verified consumer;
2. preserve the faulty version and evidence needed for review;
3. identify affected outputs, caches, indexes, reports, tiles, exports, and AI carriers without exposing protected material;
4. restore the prior known-good version;
5. re-run parse, schema, semantic, source-role, taxonomy, temporal, sensitivity, rights, reconstruction, and negative tests;
6. rebuild or invalidate derived caches and indexes;
7. create required correction, redaction, withdrawal, release, or rollback records in canonical homes;
8. verify that no public surface continues to serve an unauthorized, stale, withdrawn, or reconstructable derivative.

A Git revert does not itself revoke exposed data, correct released artifacts, invalidate caches, or establish KFM publication lineage.

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A named consumer and accepted owners are verified.
- [ ] The config file is justified by a real consumer, not directory completeness.
- [ ] File format, version, parser, exact path, and discovery mechanism are verified.
- [ ] Canonical semantic contract and restrictive schema references resolve.
- [ ] Taxonomy, source-role, occurrence-class, temporal, spatial-support, sensitivity, rights, and status semantics are explicit.
- [ ] Geoprivacy parameters come from accepted policy, not config.
- [ ] Source registry topology is resolved or a single reviewed pointer is used.
- [ ] Source-first connector references are canonical.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, and error cases.
- [ ] No-network tests pass.
- [ ] Secret, personal-data, and reconstruction-risk scans pass.
- [ ] Precedence and unknown-key behavior are deterministic and tested.
- [ ] Logging, cache, preview, tile, search, graph, report, and AI index behavior is reviewed.
- [ ] Migration, deactivation, correction, supersession, invalidation, and rollback are tested.
- [ ] CI executes substantive validation rather than TODO echo steps.
- [ ] No source, public layer, release, or publication is activated by file presence.
- [ ] Public outputs require evidence, policy, review, receipt, release, correction, and rollback support.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@b04e9b4a576557ec8cf2f48f6cbe45fd07fbec7a`.

Review again before the first non-README payload, direct consumer binding, taxonomy-profile selection, source-registry migration, geoprivacy-profile selection, source activation, workflow hardening, or public-output integration.
