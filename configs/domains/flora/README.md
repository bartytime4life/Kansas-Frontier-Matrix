<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-flora-readme
title: configs/domains/flora/ — Governed Flora Configuration Boundary
type: readme
version: v0.3
status: draft
owners: OWNER_TBD — Config steward · Flora steward · Taxonomy/herbarium steward · Source and rights steward · Sensitivity/geoprivacy steward · Cultural/stewardship reviewer · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; flora; taxonomy-aware; specimen-aware; occurrence-class-aware; source-role-aware; sensitivity-aware; geoprivacy-aware; cultural-rights-aware; join-risk-aware; reconstruction-resistant; rights-aware; time-aware; deny-by-default; non-secret; non-authoritative; no-live-binding; no-source-activation; no-watcher-activation; no-exact-sensitive-location; no-release-authority"
current_path: configs/domains/flora/README.md
truth_posture: CONFIRMED canonical Flora config lane, parent configuration contract, repository-present Flora doctrine and implementation-shaped surfaces, README-only bounded config inventory, source-first connector placement, noncanonical connectors/flora compatibility index, canonical contracts/domains/flora lane with contracts/flora compatibility guard, canonical schemas/contracts/v1/domains/flora lane with schemas/contracts/v1/flora alias guardrail, subtype-first versus domain-first source-registry topology conflict, singular versus plural release-manifest topology conflict, package version 0.0.0 placeholder, PROPOSED GBIF ingest spec, PROPOSED cultural and geoprivacy policy scaffolds, default-deny Rego scaffolds, permissive empty Flora schemas, fixture lanes without verified payloads, and TODO-only domain workflow / PROPOSED future consumer-bound templates and accepted profile references / CONFLICTED source-registry topology, connector aliases, contract/schema aliases and variants, casing and filename drift, and release manifest topology / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, policy-runtime wiring, source or watcher activation, generated public derivatives, and publication use / NEEDS VERIFICATION accepted owners, canonical plant taxonomy resolver, source roles and rights, specimen and occurrence identity, temporal semantics, cultural authority and consent, sensitivity tier transitions, geoprivacy parameters, join-risk controls, executable validation, branch protection, review enforcement, correction propagation, and rollback/invalidation integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: b29e74dc84551681e49513e8e822b831256698ca
  prior_blob: e08a002260c5c23bf5c7fba0005a415e153c9dc2
  bounded_path_search: configs/domains/flora/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/ARCHITECTURE.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/IDENTITY_MODEL.md
  - ../../../docs/domains/flora/CROSSWALKS.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../docs/domains/flora/SOURCES.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../docs/domains/flora/API_CONTRACTS.md
  - ../../../docs/domains/flora/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/flora/RELEASE_INDEX.md
  - ../../../docs/domains/flora/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/flora/
  - ../../../contracts/flora/README.md
  - ../../../schemas/contracts/v1/domains/flora/
  - ../../../schemas/contracts/v1/flora/README.md
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../policy/rights/
  - ../../../data/registry/sources/flora/
  - ../../../data/registry/flora/sources/
  - ../../../packages/domains/flora/
  - ../../../pipelines/domains/flora/
  - ../../../pipeline_specs/flora/
  - ../../../tools/validators/domains/flora/
  - ../../../tests/domains/flora/
  - ../../../fixtures/domains/flora/
  - ../../../apps/explorer-web/src/features/domains/flora/
  - ../../../connectors/flora/README.md
  - ../../../data/raw/flora/
  - ../../../data/work/flora/
  - ../../../data/quarantine/flora/
  - ../../../data/processed/flora/
  - ../../../data/catalog/domain/flora/
  - ../../../data/triplets/flora/
  - ../../../data/published/layers/flora/
  - ../../../data/receipts/flora/
  - ../../../data/proofs/flora/
  - ../../../data/rollback/flora/
  - ../../../release/candidates/flora/
  - ../../../release/manifest/
  - ../../../release/manifests/flora/
  - ../../../.github/workflows/domain-flora.yml
tags: [kfm, configs, flora, plants, taxonomy, specimens, occurrences, rare-plants, vegetation, invasive-plants, phenology, restoration, source-role, sensitivity, geoprivacy, cultural-rights, join-risk, reconstruction-risk, rights, time, no-secrets, governance]
notes:
  - "The bounded repository search for configs/domains/flora returned this README only. No executable Flora configuration payload or indexed direct consumer was found."
  - "The prior v0.2 README already carried strong taxonomy, specimen-versus-occurrence, source-role, cultural-rights, exact-location, join-induced sensitivity, reconstruction-risk, validation, correction, and rollback controls. v0.3 preserves them and adds current repository evidence, implementation maturity, path conflicts, object-family boundaries, consumer-binding rules, cache/log invalidation, and stricter first-payload gates."
  - "The repository contains many Flora implementation-shaped files, but inspected package metadata, pipeline specs, policy files, Rego modules, JSON Schemas, fixtures, release lanes, and workflow jobs remain version-0.0.0, PROPOSED placeholders, empty-permissive scaffolds, README-only guidance, or TODO-only and do not prove production behavior."
  - "Source-specific connector implementations remain source-first under connectors/<source-or-family>/. connectors/flora/ is a noncanonical compatibility index and must not become a parallel implementation hierarchy."
  - "The repository contains both data/registry/sources/flora/ and data/registry/flora/sources/, plus singular/plural release-manifest lanes and multiple contract/schema naming variants. This README surfaces those conflicts and does not resolve or duplicate them by convenience."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Flora Domain Configuration

`configs/domains/flora/`

> Safe-to-commit configuration documentation and future consumer-bound templates for plant taxonomy references, specimen and occurrence processing, vegetation communities, rare and protected plant handling, invasive plants, phenology, restoration, public-safe derivatives, and review routing. This lane is not botanical truth, taxonomic authority, cultural authority, source admission, sensitivity policy, geoprivacy authority, evidence, release, or publication authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.3-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![sensitivity](https://img.shields.io/badge/rare__plant__locations-deny__by__default-critical)
![roles](https://img.shields.io/badge/source__roles-no__collapse-purple)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Classes](#configuration-classes) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Objects](#flora-object-family-boundaries) · [Taxonomy](#taxonomy-identity-and-nomenclature) · [Evidence roles](#specimen-occurrence-range-model-and-candidate-boundaries) · [Source roles](#source-role-and-evidence-character) · [Time](#time-phenology-freshness-and-correction) · [Space](#spatial-support-precision-and-reconstruction-risk) · [Sensitivity](#sensitivity-geoprivacy-cultural-rights-and-join-risk) · [Rights](#source-rights-attribution-cultural-authority-and-stewardship) · [Connectors](#connector-source-registry-and-watcher-boundaries) · [Logging](#logging-telemetry-caches-and-derived-indexes) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-supersession-and-invalidation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.3`
> **Observed lane maturity:** README-only in the bounded config-path search; no executable Flora configuration payload or direct consumer binding is established
> **Authority:** implementation-supporting configuration sublane; non-authoritative for taxonomy, specimen or occurrence meaning, cultural authority, source admission, sensitivity, geoprivacy, evidence, policy, review, release, or publication
> **Runtime posture:** no loader, precedence rule, network fetch, source activation, watcher activation, taxonomy resolution, specimen or occurrence processing, public-layer generation, release, or publication is established by this README

> [!CAUTION]
> Exact or reconstructable rare, protected, medicinal, steward-reviewed, restoration-sensitive, or culturally sensitive plant locations and knowledge fail closed. A configuration value cannot lower sensitivity, turn a specimen, range, model, candidate, aggregate, or contextual clue into current occurrence truth, make an aggregator authoritative, infer cultural consent, authorize a transform, or create a release. Missing source role, taxonomy, time, rights, cultural authority, evidence, policy, review, redaction, release, correction, or rollback support must not become implicit permission.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `flora` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, profile references, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, route, label, generalize, render, cache, or package already-governed Flora material, but they cannot decide:

- which plant taxonomy, nomenclatural authority, accepted name, synonym, or crosswalk is controlling;
- whether a record is a specimen, observation, occurrence, survey, range, distribution model, habitat association, aggregate, candidate, restoration record, or cultural context;
- whether a historical specimen supports current presence;
- whether an occurrence is vouchered by a specimen;
- whether two specimen, occurrence, survey, phenology, restoration, vegetation, or invasive-plant records refer to the same real-world entity or event;
- whether a source is admitted, active, rights-cleared, redistributable, current, or authoritative for a requested claim;
- whether a source accessed through an aggregator inherits the aggregator's authority;
- whether cultural, traditional, medicinal, ceremonial, or stewardship knowledge may be represented or redistributed;
- whether exact or generalized geometry is safe to expose;
- whether a geoprivacy, delay, suppression, redaction, or aggregation transform is adequate;
- whether a timestamp means collection time, observation time, identification time, source-publication time, retrieval time, valid time, embargo expiry, release time, or correction time;
- whether a public map, API, export, cache, log, tile, or AI answer resists reconstruction;
- whether evidence supports a botanical claim;
- whether an artifact may be promoted, released, rendered, indexed, exported, summarized, or published.

This README is intended for configuration maintainers, Flora stewards, taxonomy and herbarium reviewers, source and rights reviewers, sensitivity and geoprivacy stewards, cultural and stewardship reviewers, consumer owners, validation and test owners, policy and release reviewers, security reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Flora domain meaning | **None.** Human doctrine remains under `docs/domains/flora/`; semantic meaning remains in accepted contract homes. |
| Plant taxonomic identity and nomenclature | **None.** Config may reference an accepted taxonomy profile; it cannot select authority by convenience, settle synonymy, or create a crosswalk. |
| Specimen, occurrence, and survey meaning | **None.** Config cannot convert labels, models, ranges, candidates, aggregates, contextual joins, or historical records into current observed truth. |
| Cultural authority, consent, and stewardship | **None.** Config cannot identify the rightful cultural authority, grant consent, classify knowledge as public, or authorize redistribution. |
| Source identity and activation | **None.** Config may reference reviewed source IDs or profiles; it cannot admit, activate, suspend, retire, or supersede a source or watcher. |
| Source role and evidence character | **None.** Config cannot relabel observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, contextual, specimen, or restricted material. |
| Schema or contract shape | **None.** Config may reference a verified schema or contract; it cannot duplicate or redefine one. |
| Sensitivity, geoprivacy, or redaction | **None.** Config may select an accepted profile; it cannot create, weaken, approve, or issue a transform or receipt. |
| Evidence and claim truth | **None.** Config cannot create an `EvidenceBundle`, close proof, validate a claim, or convert a candidate into truth. |
| Policy and review | **None.** Config cannot substitute for accepted executable policy, a `PolicyDecision`, cultural/steward review, or release review. |
| Release and publication | **None.** Config cannot authorize lifecycle promotion, public map/API/UI use, export, Focus Mode, AI response, or publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and deterministic precedence. |

A configuration value may point to authority. It cannot acquire authority through naming, file placement, parsing, repetition, successful schema validation, a passing scaffold workflow, or use by a watcher, UI, map, dashboard, or AI system.

[Back to top](#top)

---

## Status

### Repository snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Visibility | Public |
| Base ref | `main` |
| Pinned base commit | `b29e74dc84551681e49513e8e822b831256698ca` |
| Prior target blob | `e08a002260c5c23bf5c7fba0005a415e153c9dc2` |
| Bounded config-path inventory | `configs/domains/flora/README.md` only |
| Executable config payload | **Not found in the bounded config-path search** |
| Direct consumer binding | **Not established** |

The bounded search supports a narrow conclusion: this config lane is currently documentation-only. It does not prove that every Flora-adjacent file in the repository has been recursively inventoried or that no consumer refers to a future path through unindexed code.

### Evidence ledger

| Repository evidence | Status | Supports | Does not support |
|---|---:|---|---|
| `configs/domains/flora/README.md` | **CONFIRMED** | This configuration boundary exists. | A loader, parser, consumer, or runtime binding. |
| `configs/domains/README.md` | **CONFIRMED** | Domain config is non-secret and non-authoritative. | Flora-specific activation or precedence. |
| `docs/domains/flora/` | **CONFIRMED repository-present** | Rich Flora doctrine, object, source, sensitivity, map/UI, release, and rollback guidance exists. | Production behavior by itself. |
| `contracts/domains/flora/` | **CONFIRMED repository-present** | Canonical semantic-contract lane and many object-family files exist. | Accepted fields, complete coverage, or absence of duplicate naming. |
| `contracts/flora/README.md` | **CONFIRMED compatibility guard** | `contracts/flora/` is not the canonical semantic home. | Permission to add contracts there. |
| `schemas/contracts/v1/domains/flora/` | **CONFIRMED repository-present** | Active Flora schema lane and many schema files exist. | Restrictive fields, fixture coverage, validator wiring, or accepted status. |
| `schemas/contracts/v1/flora/README.md` | **CONFIRMED alias guardrail** | Bare `flora/` is an alias/guard, not the active schema lane. | Permission to create a parallel schema authority. |
| Contract and schema filename variants | **CONFIRMED search evidence** | CamelCase/snake_case and base/`.flora` variants exist. | Which variant is canonical or whether variants are compatible. |
| `packages/domains/flora/pyproject.toml` | **CONFIRMED** | Package placeholder exists at version `0.0.0`. | Implemented package behavior. |
| `pipeline_specs/flora/gbif_ingest.yaml` | **CONFIRMED** | A `PROPOSED` declarative placeholder exists. | An active GBIF pipeline or approved source use. |
| `policy/domains/flora/*.rego` | **CONFIRMED** | Default-deny `PROPOSED` policy scaffolds exist. | Complete policy logic, input assembly, tests, or runtime wiring. |
| `policy/sensitivity/flora/` | **CONFIRMED** | Cultural and rare-plant policy-shaped files exist. | Accepted cultural authority, consent, or geoprivacy parameters. |
| `fixtures/domains/flora/` | **CONFIRMED lane** | Valid/invalid/golden/object-family fixture documentation exists. | Behavioral payload coverage; the inspected valid lane says no payloads were verified. |
| `connectors/flora/README.md` | **CONFIRMED compatibility index** | Flora connector implementation is source-first under `connectors/<source-or-family>/`. | Activation or maturity of any source connector. |
| `data/registry/sources/flora/` and `data/registry/flora/sources/` | **CONFLICTED topology** | Both subtype-first and domain-first source-registry paths exist. | Which path is canonical without migration or ADR review. |
| `release/manifest/` and `release/manifests/flora/` | **CONFLICTED topology** | Singular and plural manifest lanes coexist; the Flora plural lane documents the conflict. | A canonical manifest path or actual released Flora artifact. |
| `.github/workflows/domain-flora.yml` | **CONFIRMED TODO scaffold** | Pull-request jobs are declared. | Meaningful validation; inspected jobs echo TODO commands. |

### Maturity matrix

| Capability | Observed state | Safe conclusion |
|---|---:|---|
| Config boundary README | **DOCUMENTED** | The lane has a strong human contract. |
| Executable Flora config | **NOT FOUND IN BOUNDED SEARCH** | No payload should be assumed loadable. |
| Named config consumer | **UNKNOWN** | No application, package, pipeline, watcher, or tool is proven to load this lane. |
| Flora package | **PLACEHOLDER `0.0.0`** | Presence is not implementation. |
| Declarative pipeline specs | **PROPOSED PLACEHOLDERS** | Presence is not source activation or processing. |
| Domain/sensitivity policies | **DEFAULT-DENY SCAFFOLDS / PLACEHOLDERS** | Safe baseline exists; complete policy semantics are unproven. |
| Flora schemas | **MANY FILES / INSPECTED PUBLIC SCHEMA EMPTY-PERMISSIVE** | Shape authority exists as a lane; enforceable fields remain unverified. |
| Fixtures | **DOCUMENTED LANES / PAYLOAD COVERAGE UNVERIFIED** | Positive/negative expectations exist; behavioral proof is not established. |
| Source connectors | **SOURCE-FIRST, MIXED DRAFT/COMPATIBILITY** | `connectors/flora/` must not become a duplicate runtime hierarchy. |
| Source registry | **DUAL TOPOLOGY** | Do not duplicate records; resolve by migration or ADR. |
| Release manifests | **SINGULAR/PLURAL CONFLICT** | Do not mint release records until canonical placement is resolved. |
| Domain workflow | **TODO-ONLY** | A successful run of the stub cannot prove Flora validation or release readiness. |
| Runtime/publication | **UNKNOWN / NOT AUTHORIZED** | No public or production behavior is established by this lane. |

Directory presence must not trigger discovery, source activation, watcher execution, network access, indexing, map-layer creation, AI interpretation, geometry exposure, lifecycle promotion, or publication.

[Back to top](#top)

---

## What belongs here

Only safe, non-secret, Flora-specific configuration material for a named and verified consumer belongs here.

| Material | Permitted purpose | Minimum posture |
|---|---|---|
| `README.md` | Define the configuration boundary. | Preserve taxonomy, specimen/occurrence, source-role, cultural-rights, sensitivity, evidence, policy, review, and release separation. |
| `*.template.yaml` or `*.template.yml` | Placeholder-based template for a verified consumer. | Parseable, versioned, consumer-bound, synthetic, no secrets, no live binding. |
| `*.example.yaml`, `*.example.json`, or `*.example.toml` | Tiny illustrative configuration. | Fictional identifiers and geometry; no real locality, accession, collector, source payload, or cultural knowledge. |
| Conservative profile references | Select an existing hold, abstain, generalize, withhold, redact, delay, or review profile. | Cannot reduce policy, rights, cultural, or review burden. |
| Public-safe display hints | Select a verified generalized presentation profile. | Must not contain protected geometry, hidden join keys, or exposure authority. |
| Consumer migration notes | Document a real key or path transition. | Time-bounded, owner-linked, reversible, and not a parallel authority. |
| Validation notes | Explain verified parse, shape, semantic, rights, sensitivity, join-risk, and no-network checks. | Commands and tools must be repository-grounded. |

Synthetic examples must not resemble a real specimen, collection event, locality, rare population, land parcel, survey route, seed-source location, stewardship record, medicinal-use location, or culturally sensitive place closely enough to enable reconstruction.

[Back to top](#top)

---

## What does not belong here

- exact or reconstructable rare, protected, medicinal, restoration-sensitive, steward-controlled, or culturally sensitive plant locations;
- real specimen labels, accession records, occurrence records, survey records, collector details, observer details, private stewardship notes, seed-source details, or restricted cultural knowledge;
- real herbarium archives, community-science payloads, checklist downloads, conservation-status payloads, source snapshots, images, EXIF, or rights-restricted media metadata;
- credentials, tokens, cookies, connection strings, private endpoints, workstation paths, signed URLs, or live deployment bindings;
- source admission, activation, authority-role, cadence, rights, license, redistribution, or watcher decisions;
- taxonomy authority, accepted-name adjudication, synonym resolution, conservation/legal status, cultural-use classification, or consent determination;
- schemas, contracts, policies, registries, receipts, proofs, manifests, review decisions, release records, correction records, or publication decisions;
- values that present a specimen, range polygon, distribution surface, habitat association, candidate, model output, aggregate, or contextual inference as current observed occurrence truth;
- values that present an occurrence as vouchered without specimen evidence;
- values that let a source distributor or aggregator stand in as the record's originating evidence role;
- hidden bypasses for sensitivity, cultural review, geoprivacy, redaction, withholding, delayed release, deny, abstain, quarantine, or release gates;
- lifecycle data from RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED stores;
- auto-discovery based only on directory or filename presence.

This lane may reference verified outputs from other responsibility roots, but it must not redefine them. Cross-lane references must preserve ownership, source role, sensitivity, temporal scope, cultural and rights posture, and `EvidenceBundle` support.

[Back to top](#top)

---

## Inputs

A future Flora configuration payload requires all of the following before it may be treated as consumer-ready:

1. **Named consumer** — exact package, app, pipeline, watcher, service, runtime, test harness, or tool.
2. **Accepted owners** — accountable consumer, Flora, config, rights, sensitivity, and validation ownership.
3. **Declared format** — file type, format version, parser, duplicate-key behavior, and load path.
4. **Authority references** — verified contract, schema, policy, source registry, taxonomy, rights, cultural, and domain documentation as applicable.
5. **Synthetic or public-safe values** — no real locality, specimen, person, source payload, cultural knowledge, or protected join key.
6. **Object/evidence-role model** — specimen, occurrence, survey, range, model, candidate, aggregate, context, restoration, and cultural-context roles remain distinguishable.
7. **Source-role model** — the accepted source-role vocabulary and original publisher/distributor relationship are explicit.
8. **Taxonomy posture** — authority ID, vocabulary version, accepted-name behavior, synonym behavior, unresolved conflict behavior, and update cadence are explicit.
9. **Temporal posture** — collection, observation, identification, source, valid, retrieval, embargo, release, and correction times are defined where applicable.
10. **Sensitivity and join review** — rare/protected plants, exact geometry, small counts, cultural knowledge, private-land joins, seed sources, and reconstruction risk are reviewed.
11. **Rights and cultural review** — provider terms, attribution, redistribution, media, traditional/medicinal knowledge, cultural authority, consent, and steward restrictions are verified.
12. **Validation path** — deterministic parsing, schema checks, semantic checks, no-network fixtures, negative tests, and expected finite outcomes.
13. **Precedence rule** — interaction with repository defaults, environment settings, local overrides, deployment configuration, and runtime values is explicit.
14. **Rollback and correction** — prior version, deactivation, watcher stop, cache invalidation, migration, correction, and rollback behavior are named.

A missing requirement leaves the payload **PROPOSED** or **NEEDS VERIFICATION**. It does not become active by convention.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future validated file may support a verified consumer by selecting conservative, already-governed behavior such as:

- a named plant-taxonomy or crosswalk profile;
- a source-role and distributor-origin mapping profile;
- a specimen/occurrence/range/model role profile;
- a deny, hold, abstain, quarantine, steward-review, or cultural-review route;
- a public-safe generalization, suppression, delay, or display profile;
- freshness, embargo, and supersession handling;
- a field allowlist for an already-approved public derivative;
- a migration compatibility window.

A configuration output cannot:

- admit or activate a source or watcher;
- create taxonomic, specimen, occurrence, legal-status, conservation-status, cultural, or consent truth;
- create or approve a geoprivacy, redaction, delay, suppression, or aggregation transform;
- emit a valid `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `EvidenceBundle`, `ReleaseManifest`, or correction record merely by naming one;
- reveal a sensitive location, cultural knowledge, seed source, collector/landowner detail, or reconstruction key;
- lower a sensitivity or access tier;
- write lifecycle data directly to a later phase;
- authorize a public layer, API response, map display, AI answer, release, or publication.

[Back to top](#top)

---

## Validation

### Documentation validation

For this README:

- one H1 is present;
- headings are ordered and linkable;
- internal quick links resolve;
- fenced code blocks are balanced;
- relative links remain inside known responsibility roots;
- the KFM metadata block retains the existing `doc_id` and `created` value;
- no real specimen, occurrence, locality, person, cultural record, source payload, credential, private endpoint, or protected clue is included;
- doctrine, current repository evidence, proposals, conflicts, unknowns, and verification needs remain distinct.

### Future payload validation

A future payload is not ready until applicable checks pass.

| Validation layer | Required checks |
|---|---|
| Parse | File parses under the declared format and encoding; duplicate-key behavior is deterministic. |
| Shape | Canonical schema or approved contract reference validates every field; permissive scaffolds are not accepted as release proof. |
| Consumer binding | Named consumer, supported filename, parser, version, and load path are verified. |
| Unknown keys | Behavior is explicit and covered by negative tests; safety-relevant unknowns fail closed. |
| Precedence | Merge and override behavior is deterministic and tested. |
| Taxonomy | Authority, vocabulary version, accepted names, synonyms, crosswalks, and unresolved conflict behavior remain explicit. |
| Specimen/occurrence | Specimen, occurrence, survey, range, model, candidate, aggregate, and cultural context do not collapse. |
| Source roles | Original source role and distributor/aggregator relationship remain explicit. |
| Temporal | Collection, observation, identification, source, valid, retrieval, embargo, release, and correction times remain distinct. |
| Sensitivity | Rare/protected plant data, exact localities, small counts, seed sources, restoration sites, and protected knowledge fail closed. |
| Geoprivacy | Any selected profile is governed, versioned, reviewable, and incapable of lowering protections by local override. |
| Cultural rights | Cultural authority, consent, attribution, restrictions, and redistribution boundaries resolve without inference. |
| Rights | Provider, herbarium, collector, media, attribution, derivative, and redistribution constraints resolve. |
| Join/reconstruction | Direct and indirect location clues are absent from commit-safe content and public output. |
| Network | Deterministic tests use no live network; authorized live tests are separate, bounded, and redacted. |
| Secrets | No credential, private endpoint, signed URL, or local secret path is present. |
| Logging/caches | Logs, analytics, caches, indexes, tiles, errors, and support bundles cannot reveal protected detail. |
| Migration/rollback | Prior configuration, watcher stop, cache invalidation, deactivation, correction, and restoration are documented and tested. |

Executable configuration validation remains **NOT APPLICABLE** while this lane contains no payload and no verified consumer.

### Required negative cases

At minimum, future tests should cover:

- unknown plant taxon or unresolved taxonomy/crosswalk conflict;
- conflicting accepted names or duplicate identity variants;
- aggregator/distributor presented as originating authority;
- historical specimen presented as current presence;
- occurrence presented as vouchered without specimen evidence;
- model, range, habitat association, or candidate presented as direct occurrence;
- restricted or culturally sensitive record routed to a public profile;
- missing or invalid policy, review, consent, receipt, evidence, or release reference;
- real or reconstructable protected geometry in an example;
- collector, landowner, steward, media, accession, locality, or cultural-detail leakage;
- benign inputs whose join produces higher sensitivity;
- stale, partial, unavailable, embargoed, corrected, or superseded source state;
- malformed file, unknown key, unsupported version, ambiguous precedence, or duplicate key;
- missing rollback target, invalidation target, or watcher-stop procedure.

[Back to top](#top)

---

## Review burden

README changes require configuration/documentation review and Flora domain review.

A future payload also requires the applicable:

- named consumer owner;
- taxonomy and nomenclature reviewer;
- herbarium/specimen-data reviewer;
- source and rights reviewer;
- sensitivity and geoprivacy reviewer;
- cultural authority, community, stewardship, or consent reviewer where relevant;
- habitat/agriculture/archaeology/land liaison when joins can raise sensitivity;
- schema or contract reviewer;
- validation and test reviewer;
- security and privacy reviewer;
- policy and release reviewer.

Do not infer acceptance from a missing reviewer rule, TODO owner, or placeholder `CODEOWNERS` entry. Owners remain `OWNER_TBD` until verified.

[Back to top](#top)

---

## Related folders

### Configuration and doctrine

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/flora/README.md`](../../../docs/domains/flora/README.md) — Flora doctrine and evidence-first botanical posture.
- [`../../../docs/domains/flora/ARCHITECTURE.md`](../../../docs/domains/flora/ARCHITECTURE.md) — architecture guidance.
- [`../../../docs/domains/flora/CANONICAL_PATHS.md`](../../../docs/domains/flora/CANONICAL_PATHS.md) — path and placement register.
- [`../../../docs/domains/flora/OBJECT_FAMILIES.md`](../../../docs/domains/flora/OBJECT_FAMILIES.md) — object-family inventory.
- [`../../../docs/domains/flora/IDENTITY_MODEL.md`](../../../docs/domains/flora/IDENTITY_MODEL.md) and [`CROSSWALKS.md`](../../../docs/domains/flora/CROSSWALKS.md) — identity and taxonomy crosswalk boundaries.
- [`../../../docs/domains/flora/SOURCE_REGISTRY.md`](../../../docs/domains/flora/SOURCE_REGISTRY.md), [`SOURCE_FAMILIES.md`](../../../docs/domains/flora/SOURCE_FAMILIES.md), and [`SOURCES.md`](../../../docs/domains/flora/SOURCES.md) — source orientation.
- [`../../../docs/domains/flora/SENSITIVITY.md`](../../../docs/domains/flora/SENSITIVITY.md) and [`RIGHTS_AND_SENSITIVITY.md`](../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md) — rare-plant, cultural, rights, and join-risk posture.
- [`../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md) and [`RELEASE_INDEX.md`](../../../docs/domains/flora/RELEASE_INDEX.md) — release, correction, and rollback guidance.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved repository conflicts.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement and responsibility law.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret and sensitive-value handling.

### Authority and implementation-shaped surfaces

- [`../../../contracts/domains/flora/`](../../../contracts/domains/flora/) — canonical semantic contract lane.
- [`../../../contracts/flora/README.md`](../../../contracts/flora/README.md) — compatibility guard, not a second contract authority.
- [`../../../schemas/contracts/v1/domains/flora/`](../../../schemas/contracts/v1/domains/flora/) — active machine-shape lane.
- [`../../../schemas/contracts/v1/flora/README.md`](../../../schemas/contracts/v1/flora/README.md) — alias guardrail, not a second schema authority.
- [`../../../policy/domains/flora/`](../../../policy/domains/flora/) and [`../../../policy/sensitivity/flora/`](../../../policy/sensitivity/flora/) — admissibility and sensitivity policy lanes.
- [`../../../data/registry/sources/flora/`](../../../data/registry/sources/flora/) and [`../../../data/registry/flora/sources/`](../../../data/registry/flora/sources/) — conflicting source-registry topologies; do not duplicate records.
- [`../../../packages/domains/flora/`](../../../packages/domains/flora/) — package scaffolds and future shared implementation.
- [`../../../pipelines/domains/flora/`](../../../pipelines/domains/flora/) and [`../../../pipeline_specs/flora/`](../../../pipeline_specs/flora/) — pipeline logic and declarative specs.
- [`../../../tools/validators/domains/flora/`](../../../tools/validators/domains/flora/) — validator lane.
- [`../../../tests/domains/flora/`](../../../tests/domains/flora/) and [`../../../fixtures/domains/flora/`](../../../fixtures/domains/flora/) — enforceability proof and synthetic fixtures.
- [`../../../apps/explorer-web/src/features/domains/flora/`](../../../apps/explorer-web/src/features/domains/flora/) — downstream UI feature boundary.
- [`../../../connectors/flora/README.md`](../../../connectors/flora/README.md) — compatibility index; source-specific implementations remain elsewhere.
- [`../../../release/manifest/`](../../../release/manifest/) and [`../../../release/manifests/flora/`](../../../release/manifests/flora/) — unresolved manifest topology.
- [`../../../.github/workflows/domain-flora.yml`](../../../.github/workflows/domain-flora.yml) — TODO-only workflow scaffold.

[Back to top](#top)

---

## ADRs and drift triggers

No structural ADR is introduced by this README.

The following are explicit drift or governance triggers:

| Trigger | Current posture | Required handling |
|---|---:|---|
| `data/registry/sources/flora/` versus `data/registry/flora/sources/` | **CONFLICTED** | Choose one canonical source-record home through migration or ADR-backed decision; make the other a pointer/mirror with rollback. |
| `release/manifest/` versus `release/manifests/` | **CONFLICTED** | Resolve singular/plural meaning before first Flora manifest record. |
| `contracts/flora/` | **COMPATIBILITY ONLY** | Do not add semantic contracts; point to `contracts/domains/flora/`. |
| `schemas/contracts/v1/flora/` | **ALIAS GUARDRAIL** | Do not add canonical schemas; point to `schemas/contracts/v1/domains/flora/`. |
| CamelCase versus snake_case contract filenames | **CONFLICTED / NEEDS VERIFICATION** | Select or document compatibility; do not maintain divergent semantics. |
| Base versus `.flora` schema variants | **CONFLICTED / NEEDS VERIFICATION** | Define profile/alias semantics or migrate duplicates; preserve `$id` and fixture compatibility. |
| USDA PLANTS, USFWS, KDWP, and herbarium connector aliases | **CONFLICTED** | Source-first connector migration/ADR; do not select by convenience. |
| Taxonomy resolver selection | **NEEDS GOVERNED DECISION** | Record authority scope, versions, crosswalk behavior, and rollback. |
| Cultural/medicinal knowledge publication | **DENY / HOLD BY DEFAULT** | Require identified authority, rights/consent review, policy, evidence, and release support. |
| Universal config discovery, precedence, or unknown-key behavior | **NOT ESTABLISHED** | Requires an explicit cross-config contract and tests. |

Separate governance is also required before changing a canonical domain slug, sensitivity tier, geoprivacy parameter, rights rule, source activation model, authority separation, lifecycle phase, or public access path.

Configuration must not settle those decisions indirectly.

[Back to top](#top)

---

## Scope and bounded context

The Flora configuration bounded context covers configuration **about how a verified consumer handles already-governed botanical material**. It does not own the botanical material or its authority.

### In scope

- consumer-bound parsing and validation options;
- references to accepted taxonomy, rights, sensitivity, display, stale-state, and review profiles;
- conservative routing between hold, abstain, deny, review, generalize, delay, and public-safe behavior;
- deterministic precedence, unknown-key, deprecation, migration, cache, and rollback behavior;
- synthetic examples and no-network test settings;
- downstream field allowlists and public-safe display hints after release approval.

### Out of scope

- plant taxonomy adjudication or nomenclatural acts;
- source admission, credentials, requests, rate limits, downloads, or watcher execution;
- specimen/occurrence truth, identification, locality interpretation, or voucher verification;
- cultural authority, consent, or knowledge classification;
- geoprivacy parameter definition or sensitivity-tier movement;
- lifecycle promotion, evidence closure, policy approval, review approval, release, publication, correction authority, or rollback authority;
- direct public access to internal records, source registries, RAW, WORK, QUARANTINE, restricted processed records, or canonical stores.

[Back to top](#top)

---

## Configuration classes

A future payload should declare exactly one primary class.

| Class | Bounded purpose | Forbidden authority |
|---|---|---|
| `parser_profile` | Select accepted parser behavior for a named consumer and format version. | Cannot define botanical meaning or source truth. |
| `taxonomy_profile_ref` | Reference an accepted taxonomy/crosswalk profile. | Cannot contain replacement taxonomy or settle conflicts. |
| `source_role_profile_ref` | Reference accepted role mapping and distributor-origin handling. | Cannot admit or upgrade source authority. |
| `occurrence_processing_profile` | Select accepted routing for specimen, occurrence, range, model, candidate, and public-safe derivatives. | Cannot convert one evidence class into another. |
| `sensitivity_profile_ref` | Reference accepted geoprivacy, suppression, delay, and review behavior. | Cannot define parameters, lower protections, or issue receipts. |
| `rights_cultural_profile_ref` | Reference accepted rights, attribution, cultural-authority, consent, and stewardship handling. | Cannot invent authority or permission. |
| `public_display_profile` | Select released fields, precision labels, caveats, and display behavior. | Cannot expose unreleased or reconstructable detail. |
| `freshness_correction_profile` | Select accepted stale, embargo, supersession, correction, and cache invalidation behavior. | Cannot make stale or corrected records current. |
| `migration_profile` | Define versioned compatibility for a real consumer. | Cannot create parallel contract/schema/policy/registry homes. |
| `test_profile` | Control synthetic, deterministic, no-network test behavior. | Cannot activate a live source or use real sensitive data. |

A file that mixes unrelated classes should be split unless the named consumer's verified contract requires one atomic document.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file should document or carry the following information in the repository-approved form.

| Field | Required meaning |
|---|---|
| `config_id` | Stable identifier for the configuration artifact. |
| `config_version` | Version of the configuration document, distinct from contract/schema/profile versions. |
| `consumer` | Exact component that reads the file. |
| `consumer_version_range` | Supported consumer versions or commit/spec boundary. |
| `owner` | Accountable component and domain owner; no invented team. |
| `class` | One primary configuration class. |
| `domain` | `flora`; config cannot create a domain alias. |
| `format` | Syntax, encoding, parser, and duplicate-key behavior. |
| `contract_ref` / `schema_ref` | Canonical semantic and machine-shape authority, when verified. |
| `taxonomy_profile_ref` | Stable identifier for accepted taxonomy/crosswalk behavior. |
| `source_role_profile_ref` | Stable identifier for accepted source-role/distributor-origin behavior. |
| `sensitivity_profile_ref` | Stable identifier for accepted policy; not an inline substitute. |
| `rights_cultural_profile_ref` | Stable identifier for accepted rights/cultural review behavior. |
| `public_safe_profile_ref` | Stable identifier for an approved transform or display profile. |
| `temporal_semantics` | Applicable time kinds, timezone, freshness, embargo, expiry, and correction behavior. |
| `unknown_key_behavior` | Reject, warn, or ignore; explicit and tested. |
| `precedence` | Exact merge and override order for the named consumer. |
| `network_posture` | No network by default unless the consumer and security review explicitly authorize it. |
| `failure_posture` | Finite fail-closed dispositions for missing, malformed, stale, conflicting, restricted, or unauthorized input. |
| `validation` | Parser, schema, semantic, taxonomy, specimen/occurrence, sensitivity, rights, cultural, join-risk, and negative-case checks. |
| `migration` | Deprecated keys, compatibility window, replacement, correction path, and removal condition. |
| `rollback` | Prior known-good version, consumer deactivation, watcher stop, and cache/index invalidation method. |

Do not add schema-invalid placeholders to a machine-parsed file. Keep unresolved ownership or authority outside the payload until the repository supplies an approved sentinel or value.

[Back to top](#top)

---

## Consumer binding, precedence, and discovery

No consumer binding is established by this README.

A valid future binding must specify:

1. the exact consumer path and owning component;
2. the exact configuration filename or explicit path;
3. supported config versions and migration behavior;
4. parser and schema/contract resolution;
5. load timing and whether reloading is supported;
6. precedence relative to built-in defaults, environment variables, deployment configuration, local developer overrides, and runtime requests;
7. behavior for missing files, malformed files, duplicate keys, unknown keys, deprecated keys, incompatible versions, and conflicting profiles;
8. whether a change requires restart, revalidation, re-indexing, cache invalidation, tile rebuild, release review, or rollback;
9. logging rules that do not expose protected botanical information;
10. a deterministic no-network test proving the binding.

### Default discovery posture

Until verified otherwise:

- no recursive directory discovery;
- no wildcard loading;
- no filename-convention activation;
- no network access;
- no source or watcher activation;
- no inheritance from unreviewed local files;
- no merge order inferred from lexical filename order;
- no silent fallback from malformed configuration to a less restrictive posture;
- no public-output change without ordinary evidence, policy, review, release, correction, and rollback controls.

[Back to top](#top)

---

## Flora object-family boundaries

Configuration may reference accepted profiles or fields for Flora object families; it cannot define their meaning, identity, evidence burden, or release status.

| Object family | Boundary configuration must preserve |
|---|---|
| `PlantTaxon` | Authority and nomenclatural version remain explicit; synonymy does not silently merge identities. |
| `FloraTaxonCrosswalk` | Crosswalk method, confidence, source vocabularies, unresolved mappings, and supersession remain visible. |
| `SpecimenRecord` | Voucher, institution, collection event, label transcription, identification history, rights, and locality sensitivity remain distinct. |
| `FloraOccurrence` | Observation/occurrence evidence, method, time, identity, source, uncertainty, and sensitivity remain explicit. |
| `OccurrenceRestricted` | Exact or steward-controlled records remain restricted and must not feed public outputs directly. |
| `OccurrencePublic` | Public-safe derivative exists only after evidence, policy, review, transformation, and release gates. |
| `RarePlantRecord` | Rare/protected status and exact location fail closed; config cannot downgrade risk. |
| `VegetationCommunity` | Community classification, method, geometry, source, time, and uncertainty remain distinct from species occurrence. |
| `InvasivePlantRecord` | Observation, regulatory/admin status, treatment, and public-risk context remain separate. |
| `PhenologyObservation` | Stage, observation method, date/time, uncertainty, and temporal support remain visible. |
| `RangePolygon` / distribution surface | Modeled, compiled, administrative, or observational support remains explicit; range is not occurrence. |
| `HabitatAssociation` | Cross-lane relation preserves Habitat ownership and does not create occurrence evidence. |
| `BotanicalSurvey` | Effort, method, scope, completeness, observers/collectors, and sensitive route/locality handling remain explicit. |
| `RestorationPlanting` | Planned/implemented planting, seed source, site, rights, stewardship, and monitoring status remain distinct from natural occurrence. |
| `RedactionReceipt` | Records a governed transform; config cannot mint, approve, or replace the receipt. |
| Governance/support families | Evidence, validation, policy, review, catalog, release, correction, and rollback remain separate authorities. |

[Back to top](#top)

---

## Taxonomy identity and nomenclature

- Every taxon identifier must retain its authority and vocabulary version.
- Accepted names, synonyms, infraspecific ranks, hybrids, cultivars, provisional names, and unresolved names remain distinguishable.
- A distribution platform or aggregator is not automatically the nomenclatural authority.
- Conflicting taxonomies and crosswalks must remain visible and follow a governed conflict procedure.
- Historical specimen determinations must not be rewritten in place when current taxonomy changes; preserve identification history and correction lineage.
- Configuration may select a verified crosswalk profile; it must not embed an unofficial replacement taxonomy.
- The canonical resolver, authority order, confidence thresholds, conflict behavior, and update cadence remain **NEEDS VERIFICATION** until accepted repository evidence resolves them.

[Back to top](#top)

---

## Specimen, occurrence, range, model, and candidate boundaries

- A `SpecimenRecord` is vouchered evidence with collection, institution, catalog, determination, rights, and locality context.
- A `FloraOccurrence` is occurrence evidence and may or may not be vouchered; its method and support must remain explicit.
- An `OccurrenceRestricted` record remains restricted and fails closed for ordinary public exact-location use.
- An `OccurrencePublic` record is a public-safe derivative after required policy, review, transformation, evidence, and release gates.
- A historical specimen does not prove current presence.
- A range polygon, distribution surface, habitat association, vegetation community, restoration planting, checklist, candidate detection, or AI interpretation is not a direct observation.
- A label transcription is not an accepted taxonomic determination merely because it parses.
- A restoration planting is not a wild occurrence unless separate evidence supports that classification.
- A vegetation map or habitat join does not prove a species occurs at a point.
- Configuration must not upgrade one evidence character into another through thresholds, display rules, or profile names.

[Back to top](#top)

---

## Source role and evidence character

The accepted repository source-role vocabulary must be referenced, not recreated locally. The Flora path register records the seven-class doctrine vocabulary:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

Configuration must also preserve evidence character such as specimen, occurrence, checklist, taxonomy, conservation status, vegetation classification, phenology, restoration, cultural context, imagery, or model output.

| Source/evidence character | Configuration-safe treatment |
|---|---|
| Originating observation or specimen publisher | Preserve method, institution/publisher, record ID, time, uncertainty, rights, and sensitivity. |
| Taxonomy/checklist authority | Preserve authority scope; do not treat checklist presence as occurrence. |
| Aggregator/distributor | Preserve original publisher, license, record restrictions, and evidence role; distributor is not the origin role. |
| Regulatory/administrative record | Preserve legal/admin scope; do not generalize authority beyond its jurisdiction and time. |
| Model/range product | Preserve model method, version, valid scope, uncertainty, and non-observation status. |
| Context layer | Supports interpretation or joins; cannot confirm taxon identity or occurrence. |
| Candidate | Remains unconfirmed; thresholds and display cannot promote it alone. |
| Synthetic fixture | Test-only; never production truth or release evidence. |

Configuration must never collapse these roles into a generic `trusted`, `verified`, `authoritative`, or `public` flag.

[Back to top](#top)

---

## Time, phenology, freshness, and correction

Where material, preserve distinct time meanings:

- collection time and collection interval;
- observation or survey time;
- identification and determination time;
- phenology observation time;
- source publication/version time;
- model initialization and valid time;
- retrieval/ingestion and processing time;
- embargo or delayed-release expiry;
- review and release time;
- correction, supersession, withdrawal, and rollback time.

A historical specimen does not prove current presence. A current model does not rewrite an older observation. A new determination does not erase prior identification history. A phenology observation is local to its time, method, and support. Stale, embargoed, corrected, withdrawn, or superseded material must remain visibly so.

A future profile may select an accepted freshness or embargo policy. It cannot invent a universal threshold, suppress stale state, or publish an embargoed record.

[Back to top](#top)

---

## Spatial support, precision, and reconstruction risk

Configuration must preserve the spatial support of the underlying evidence or derivative:

- exact point, uncertainty circle, locality text, collection route, plot, transect, polygon, grid, county, watershed, ecoregion, range, raster cell, or generalized envelope;
- horizontal and vertical precision where material;
- georeferencing method and uncertainty;
- whether geometry is source-native, inferred, modeled, transformed, generalized, or withheld;
- coordinate reference system and transformation lineage where applicable.

### Reconstruction checks

Review the resulting product for clues that may reconstruct a protected location, including:

- precise coordinates, tiny polygons, high-resolution rasters, or low-count grids;
- collector numbers, accession/catalog IDs, stable external join keys, locality strings, route descriptions, or landmark names;
- exact collection dates combined with photographs, phenology, or itinerary/history;
- seed-source, restoration-site, survey-route, treatment, or monitoring details;
- habitat, soil, hydrology, parcel, ownership, road, trail, infrastructure, archaeology, or place-name joins;
- repeated generalized points whose overlap reveals the source location;
- rare-taxon labels, tiny population envelopes, unique combinations, or small-area counts;
- media EXIF, filenames, alt text, cache keys, logs, errors, analytics, screenshots, receipts, or support bundles;
- map zoom, hover, query, export, tile, search-index, or feature-state attributes.

When public safety cannot be established, the consumer must deny, hold, abstain, omit, delay, or use an accepted governed generalization. It must not expose the value silently.

[Back to top](#top)

---

## Sensitivity, geoprivacy, cultural rights, and join risk

### Deny-by-default location posture

Exact rare, protected, medicinal, culturally sensitive, steward-reviewed, seed-source-sensitive, restoration-sensitive, or otherwise vulnerable plant locations are denied on ordinary public surfaces by default.

Public-safe use requires the applicable combination of:

- verified rights, cultural authority, consent, and source-role posture;
- steward and cultural/community review where applicable;
- generalized, withheld, delayed, staged, aggregated, or denied geometry;
- a resolvable `EvidenceBundle`;
- an applicable `PolicyDecision`;
- a recorded transform such as a `RedactionReceipt`;
- review and release state;
- correction and rollback targets.

The exact transform parameters belong in accepted policy and review records, not in this README or an ad hoc config value.

### Cultural, traditional, and medicinal knowledge

Configuration cannot decide that cultural, traditional, medicinal, ceremonial, relationship-bound, or stewardship knowledge is public.

A future consumer must:

- preserve the stated authority, provenance, context, consent, and use restrictions;
- distinguish publicly published knowledge from restricted, community-held, or relationship-bound knowledge;
- avoid inferring affiliation, ownership, permission, or representational authority;
- deny or hold ambiguous use;
- preserve attribution and restrictions;
- route consequential representation or redistribution to the appropriate human/community review.

### Join-induced sensitivity

A benign input can become sensitive after a join. The output inherits the strongest applicable sensitivity until reviewed.

Examples include:

- rare-plant taxonomy joined to fine habitat or soil polygons;
- generalized occurrences joined to parcel, trail, water-body, archaeology, or road context;
- specimen/locality history joined to collector itineraries or media;
- restoration or seed-source records joined to exact project sites;
- cultural-use information joined to a small community, place, or land parcel;
- repeated time slices that narrow an obscured location.

Configuration cannot pre-authorize such joins as public-safe merely because each input is independently public.

### Permitted profile references

A configuration may reference an already-governed profile for suppression, withholding, geographic generalization, buffering/jitter, low-count aggregation, delay, steward-only access, field allowlisting, cultural review, or release routing. The consumer must resolve the profile, verify its applicability, execute it through the governed implementation, and validate its receipts.

[Back to top](#top)

---

## Source rights, attribution, cultural authority, and stewardship

- Public accessibility does not prove redistribution rights, derivative rights, media rights, cultural permission, or release authority.
- Preserve original publisher, institution, collection, record-level license, attribution, and usage restrictions when data passes through GBIF, iDigBio, or another distributor.
- Herbarium specimen images, labels, collector information, accession data, and locality metadata may carry distinct rights and sensitivity burdens.
- NatureServe, state natural heritage, stewardship, and restricted-source material require source-specific terms and access controls.
- Traditional, medicinal, ceremonial, or culturally sensitive knowledge requires identified authority and consent appropriate to the intended use; absence of a restriction is not permission.
- Configuration must not automatically activate a live source, watcher, or network call.
- No-network fixtures are the default validation surface for a new payload.
- Logs, errors, screenshots, receipts, analytics, support bundles, and test output must not expose protected localities, private people, or restricted knowledge.

[Back to top](#top)

---

## Connector, source-registry, and watcher boundaries

### Connectors

Current repository posture keeps Flora-relevant source access under source-first or source-family lanes such as GBIF, iNaturalist, iDigBio, NatureServe, EDDMapS, USDA PLANTS, USFWS, KDWP, and herbarium connectors.

`connectors/flora/` is a documentation-only compatibility index. Do not add client code, fetchers, credentials, package metadata, source descriptors, activation decisions, tests, payload caches, or lifecycle writers beneath it without an accepted ADR that deliberately changes connector placement doctrine.

Connector path aliases remain unresolved, including USDA PLANTS variants, USFWS/ECOS variants, KDWP compatibility paths, and KU/KBS herbarium names. Config must reference a reviewed source identity, not select a path by convenience.

### Source registry

Both of the following exist:

```text
data/registry/sources/flora/
data/registry/flora/sources/
```

Until migration or ADR-backed resolution:

- do not write divergent SourceDescriptor records to both;
- do not let a config file select which registry is authoritative;
- require stable source IDs independent of filesystem alias;
- make any compatibility lane pointer-only, reversible, and explicit;
- preserve source-role, rights, sensitivity, stale, supersession, and correction state.

### Watchers

Watchers are non-publishers. A watcher or config file may identify a reviewed watcher profile only after the consumer and policy are verified. Watchers must not:

- mutate canonical records silently;
- promote lifecycle state;
- convert source changes into botanical truth;
- expose new precise geometry;
- bypass rights, cultural, sensitivity, evidence, review, release, correction, or rollback gates;
- commit directly to `main` or publish by side effect.

[Back to top](#top)

---

## Logging, telemetry, caches, and derived indexes

Configuration can influence hidden secondary surfaces. A future consumer must document and test:

- which config keys or values may enter logs;
- whether taxon IDs, record IDs, localities, collector/landowner names, cultural terms, source URLs, policy IDs, or profile IDs are logged;
- log retention, access, redaction, and deletion behavior;
- metrics cardinality and whether labels can reveal a rare taxon or locality;
- cache keys, TTL, namespace, encryption, invalidation, and access class;
- search/vector/graph index fields and deletion/supersession propagation;
- tile, GeoJSON, PMTiles, COG, thumbnail, screenshot, export, and browser-storage invalidation;
- whether error responses, traces, crash reports, or support bundles reveal protected details;
- how correction, withdrawal, sensitivity change, rights change, taxonomy change, and rollback invalidate derived products.

A config rollback is incomplete while a stale cache, index, tile, export, screenshot, or generated narrative continues to expose the superseded behavior or data.

[Back to top](#top)

---

## Failure behavior

A verified consumer must use finite, reason-coded, fail-closed dispositions. Exact implementation remains **PROPOSED** until code and tests confirm it.

| Condition | Expected safe disposition |
|---|---|
| Valid, authorized, public-safe configuration | `PASS` for internal validation; continue to ordinary governed processing. |
| Malformed file, duplicate key, unsupported version, or contract violation | `FAIL` or `ERROR`; do not partially apply. |
| Unknown taxon or unresolved nomenclature/crosswalk conflict | `HOLD` or `ABSTAIN`; preserve competing identities. |
| Missing source role, origin publisher, rights, cultural authority, consent, policy, review, or transform authority | `HOLD`, `DENY`, or `ABSTAIN`; do not infer permission. |
| Exact sensitive occurrence or reconstructable locality requested for public use | `DENY` by default. |
| Historical specimen, model, range, habitat association, or candidate presented as current observation | `FAIL` and `ABSTAIN`; preserve the original evidence role. |
| Specimen/voucher status asserted without evidence | `FAIL` or `HOLD`; do not upgrade occurrence evidence. |
| Join creates higher sensitivity than inputs | `HOLD` or `DENY` until the resulting product is reviewed. |
| Missing or stale evidence with no released alternative | `ABSTAIN`; do not substitute a model, cache, or generic summary silently. |
| Unauthorized sensitivity reduction, cultural bypass, or hidden override | `FAIL` and `DENY`; record the reason without exposing protected values. |
| Source outage, partial download, embargo, or incomplete data | Preserve stale, partial, held, or embargoed state explicitly. |
| Consumer cannot determine precedence or canonical profile | `ERROR` or `HOLD`; do not merge unpredictably. |
| Correction, withdrawal, rights change, or rollback cannot invalidate derivatives | `ERROR` and `DENY` further public use until invalidation closes. |

`PASS` and `FAIL` are validator outcomes, not publication decisions. A valid config still requires evidence, policy, review, and release support for consequential outputs.

[Back to top](#top)

---

## Governed AI and generated language

AI may explain released, policy-safe Flora evidence. It cannot decide taxonomy, specimen validity, occurrence truth, cultural authority, consent, sensitivity, rights, geoprivacy, review, release, or correction state.

A Flora-related AI path must:

1. define the requested spatial, temporal, taxonomic, evidentiary, and cultural scope;
2. retrieve released evidence through governed interfaces;
3. resolve `EvidenceRef` to `EvidenceBundle` where claims depend on evidence;
4. apply rights, cultural, sensitivity, geoprivacy, review, stale, and release checks;
5. preserve specimen/occurrence/range/model/context distinctions;
6. avoid reconstructing protected locations from joins, prose, citations, map state, or tool output;
7. return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` with bounded reasons and citations;
8. avoid treating config, schemas, maps, tiles, indexes, or generated prose as root truth.

A configuration key such as `enable_ai`, `allow_exact_location`, `trust_model`, `skip_review`, `publish`, or `disable_redaction` must never bypass the governed path.

[Back to top](#top)

---

## Migration and anti-bypass posture

Configuration migration is a governed compatibility change, not permission to create parallel authority.

A migration must include:

- old and new config IDs/versions;
- named consumer and owners;
- exact changed keys and semantic impact;
- schema/contract/profile version changes;
- treatment of unknown/deprecated keys;
- precedence and rollback behavior;
- watcher/source activation impact;
- cache/index/tile/export invalidation impact;
- rights, cultural, sensitivity, and join-risk review;
- test fixtures for old, new, invalid, mixed, and rollback states;
- deprecation window and removal criteria;
- correction/rollback target.

Do not use migration aliases to:

- create a second source registry, contract, schema, policy, receipt, proof, or release home;
- map a restricted profile to a public profile;
- convert a specimen/range/model/candidate into occurrence truth;
- select a connector alias as source authority;
- suppress warnings, evidence, review, cultural, sensitivity, stale, correction, or release state;
- keep serving superseded derived artifacts indefinitely.

[Back to top](#top)

---

## Rollback, correction, supersession, and invalidation

Before merge, rollback means closing the unmerged pull request and abandoning the scoped branch when separately authorized.

After merge, create a transparent revert commit or revert pull request restoring the prior known-good README or configuration version. Do not force-push or rewrite shared history.

For a future payload correction:

1. disable or stop selecting the affected config through the verified consumer mechanism;
2. stop any watcher, scheduled process, or reload path that depends on it;
3. preserve the faulty version and evidence needed for review;
4. identify affected objects, joins, caches, indexes, tiles, exports, screenshots, reports, API payloads, and generated narratives without exposing protected information;
5. assess whether exact or reconstructable sensitive information, restricted cultural knowledge, private-person detail, or rights-restricted content was exposed;
6. restore the prior known-good version;
7. re-run parsing, schema, semantic, taxonomy, source-role, rights, cultural, sensitivity, join-risk, and negative-case validation;
8. create required correction, redaction, withdrawal, review, release, or rollback records in canonical homes;
9. invalidate or rebuild every affected derived carrier;
10. verify governed public surfaces no longer serve unauthorized, stale, superseded, or reconstructable material.

A Git revert does not itself revoke exposed data, correct released artifacts, invalidate caches, or establish KFM publication lineage.

[Back to top](#top)

---

## Definition of done for the first payload

- [ ] A real named consumer and accepted owners are verified.
- [ ] The file format, version, parser, duplicate-key behavior, filename, and load path are verified.
- [ ] Canonical contract and restrictive schema references resolve; alias paths are not used as authority.
- [ ] Taxonomy, nomenclature, specimen, occurrence, range, model, candidate, temporal, and source-role semantics are explicit.
- [ ] Original publisher/distributor relationships and record-level rights are preserved.
- [ ] Cultural authority, consent, attribution, redistribution, and steward restrictions are reviewed where applicable.
- [ ] Sensitivity and geoprivacy parameters come from accepted policy, not the config file.
- [ ] Join-induced sensitivity and reconstruction risks are covered across map, API, export, logs, caches, indexes, and AI.
- [ ] Source-registry, connector-alias, contract/schema naming, and release-manifest topology conflicts are resolved or explicitly bounded by reviewed compatibility rules.
- [ ] Synthetic fixtures cover valid, invalid, held, denied, abstained, error, stale, embargoed, corrected, superseded, and rollback cases.
- [ ] No-network tests pass.
- [ ] Secret, private-person, cultural-knowledge, rights, and protected-location scans pass.
- [ ] Precedence, unknown-key, migration, deactivation, watcher stop, correction, rollback, and invalidation behavior are tested.
- [ ] Policy execution and input assembly are tested; default-deny scaffolds are replaced or explicitly retained as non-production guards.
- [ ] Workflow jobs execute meaningful checks rather than TODO echoes.
- [ ] No source, watcher, public layer, release, or publication is activated by file presence.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@b29e74dc84551681e49513e8e822b831256698ca`.

Review again before the first non-README payload, consumer binding, taxonomy/crosswalk selection, cultural or stewardship review profile, sensitivity/geoprivacy profile, source or watcher activation, schema/profile migration, manifest placement decision, or public-output integration.
