<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/atmosphere/readme
name: Atmosphere Registry README
path: data/registry/atmosphere/README.md
type: data-registry-domain-parent-readme
version: v0.2.0
status: draft; compatibility-boundary; no-independent-registry-record-writes
owners:
  - "NEEDS VERIFICATION: registry steward"
  - "NEEDS VERIFICATION: Atmosphere domain steward"
  - "NEEDS VERIFICATION: source, dataset, layer, domain, rights, sensitivity, and crosswalk stewards"
  - "NEEDS VERIFICATION: public-safety, policy, validation, proof, and release reviewers"
updated: 2026-07-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-domain-registry-compatibility-parent
path_posture: confirmed-live-domain-first-parent; subtype-first-registry-authority; independent-registry-record-writes-denied; migration-needs-accepted-decision
safety_posture: no-direct-public-path; no-source-activation; no-advisory-health-regulatory-or-operational-authority; fail-closed; release-gated
related:
  - ../README.md
  - sources/README.md
  - ../sources/README.md
  - ../sources/atmosphere/README.md
  - ../sources/atmosphere/aqs.source.json
  - ../sources/atmosphere/knowledge_character.json
  - ../datasets/README.md
  - ../layers/README.md
  - ../domains/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../crosswalks/README.md
  - ../../raw/atmosphere/README.md
  - ../../work/atmosphere/README.md
  - ../../quarantine/atmosphere/README.md
  - ../../processed/atmosphere/README.md
  - ../../receipts/atmosphere/README.md
  - ../../proofs/atmosphere/README.md
  - ../../catalog/domain/atmosphere/README.md
  - ../../published/atmosphere/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/registry/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../fixtures/domains/atmosphere/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/workflows/link-check.yml
  - ../../../release/candidates/atmosphere/README.md
tags:
  - kfm
  - data
  - registry
  - atmosphere
  - compatibility
  - subtype-first
  - source-role
  - provider-lineage
  - rights
  - sensitivity
  - freshness
  - units
  - temporal-integrity
  - spatial-support
  - correction
  - rollback
  - cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: e9f0e0792c094c7367e0eec973ed0461a595d609
  prior_blob: eb99029511d8c2e80a7c94542050af083c12ca5b
  child_compatibility_blob: a27f712d62a9319f08794619a5bdf513eaf1da1a
  canonical_source_lane_blob: 6a50dd496225cd9e4c3165dead10cde3d0f23959
  registry_parent_blob: b327d22956f5454482a35dbf265f45b901c1f2a3
  source_registry_parent_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: cd044a38047cc9b3725d2e083eb201eb86109308
  source_descriptor_standard_blob: 4327c603f76e5b5a76fa058fe24ac2af91e496d8
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  aqs_placeholder_blob: 2899950cd366d9afe7c468baa45cacc65da139e9
  knowledge_character_placeholder_blob: 4b2067e4f1ba70d4689d56ad36b952ead131864c
  atmosphere_registry_schema_index_blob: 4c22c541d86d79765784bfa612e44731af74e43c
  atmosphere_source_fixtures_blob: 83a40d45d7fb5a60c4f7f40ba2efb9b031ce70e6
  domain_atmosphere_workflow_blob: 3bd0183481a73c1aaad011e4ef1e361a3ee6b5f2
  link_check_workflow_blob: c91477f6a6da84203e61b3151076eb46b3a65941
  inspection_date: 2026-07-28
notes:
  - "This README preserves the stable identity of the existing domain-first Atmosphere registry parent."
  - "Adopted Directory Rules v2 makes subtype-first registry placement canonical and prohibits this parent from becoming an independent registry hierarchy."
  - "The child data/registry/atmosphere/sources/README.md is a no-independent-write compatibility view aligned to the subtype-first source registry."
  - "Bounded repository inspection found the canonical Atmosphere source README plus two PROPOSED placeholder JSON files; this is not proof of active source admission or a complete recursive inventory."
  - "The source-authority register is PROPOSED and empty; the Atmosphere and link-check workflows are explicit readiness holds."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Registry

[![Document lifecycle: draft](https://img.shields.io/badge/document-draft-d4a72c?style=flat-square)](#status)
[![Path class: compatibility parent](https://img.shields.io/badge/path-compatibility%20parent-d4a72c?style=flat-square)](#authority-and-path-posture)
[![Registry authority: subtype first](https://img.shields.io/badge/registry%20authority-subtype--first-0969da?style=flat-square)](#authority-and-path-posture)
[![Independent writes: denied](https://img.shields.io/badge/independent%20writes-denied-b42318?style=flat-square)](#registry-boundary)
[![Public or operational use: denied](https://img.shields.io/badge/public%20or%20operational%20use-denied-b42318?style=flat-square)](#atmosphere-safety-boundary)

> **One-line purpose.** Preserve the existing domain-first Atmosphere registry path as a bounded navigation and compatibility parent while authoritative registry records remain in their accepted subtype-first families.

> [!CAUTION]
> Do not add authoritative source descriptors, activation decisions, dataset or layer identities, rights or sensitivity decisions, payloads, proofs, policies, releases, or public-facing Atmosphere data under this parent. This path does not establish current conditions, regulatory status, health guidance, emergency direction, release approval, or KFM publication.

> [!WARNING]
> Atmosphere material is unusually vulnerable to source-role, unit, time, spatial-support, quality, and stale-state collapse. AQI is not concentration; AOD or smoke context is not a direct PM2.5 measurement; a model field is not an observation; an aggregate is not point truth; and a public upstream source is not automatic release permission.

**Navigation:** [Status](#status) · [Purpose](#purpose) · [Authority](#authority-and-path-posture) · [Inventory](#current-bounded-inventory) · [Repository fit](#repository-fit) · [Children](#confirmed-child-lanes) · [Boundary](#registry-boundary) · [Safety](#atmosphere-safety-boundary) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs/outputs](#inputs-and-outputs) · [Workflow evidence](#current-workflow-evidence) · [Validation](#validation-and-maintenance) · [Verification](#open-verification) · [Rollback](#correction-migration-and-rollback)

<a id="status"></a>

## Status

| Surface | Evidence-backed state |
|---|---|
| Target path | **CONFIRMED** at `main@e9f0e0792c094c7367e0eec973ed0461a595d609` |
| Document lifecycle | `draft` |
| README profile | Sensitive `BOUNDARY_COMPACT` compatibility parent |
| Responsibility | Registry-domain navigation, compatibility, and migration boundary only |
| Governing Directory Rules | **CONFIRMED adopted** through [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) |
| Registry placement | Subtype-first is canonical under `DIR-SOURCE-003` and `DIR-SOURCE-004` |
| Confirmed local child | [`sources/`](sources/README.md), a no-independent-write compatibility view |
| Canonical Atmosphere source lane | [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) |
| Canonical-lane records found in bounded inspection | README plus two JSON files explicitly marked `PROPOSED`; no active admission established |
| Source-authority register | **CONFIRMED present**, `PROPOSED`, and empty |
| Registry schema and fixture posture | Draft indexes and synthetic guidance; concrete enforcement remains **NEEDS VERIFICATION** |
| Atmosphere and link-check workflows | Explicit readiness holds; no source admission, truth, release, or publication authority |
| Independent registry-record writes here | **DENY** |
| Direct public, medical, regulatory, emergency, or operational use | **DENY BY DEFAULT** |
| Accountable stewardship assignments | **NEEDS VERIFICATION** |

A path, README, placeholder record, schema-valid file, green held workflow, commit, pull request, or merge does not establish source authority, rights clearance, policy admission, evidence closure, current conditions, release approval, or publication.

<a id="purpose"></a>

## Purpose

This README governs the existing domain-first parent:

```text
data/registry/atmosphere/
```

Its bounded responsibilities are to:

- preserve the path's stable navigation identity while registry topology converges;
- route maintainers to the canonical subtype-first family for each governed registry object;
- make the child source compatibility boundary and canonical source writer explicit;
- prevent this parent from becoming a parallel Atmosphere registry hierarchy;
- preserve identity, provider lineage, source role, measurement context, correction, migration, supersession, withdrawal, and rollback requirements;
- keep Atmosphere rights, sensitivity, freshness, units, quality, spatial support, and public-safety boundaries visible.

This README does **not** define registry-object semantics, machine shape, policy, source activation, connector or watcher behavior, lifecycle promotion, evidence, proof, catalog closure, release, current conditions, compliance, health interpretation, emergency guidance, or public delivery.

<a id="authority-and-path-posture"></a>

## Authority and path posture

Accepted Directory Rules v2 establishes subtype-first registry placement:

```text
data/registry/
├── sources/
├── datasets/
├── layers/
├── domains/
├── rights/
├── sensitivity/
└── crosswalks/
```

The topology is sparse and evidence-driven. It does not authorize every family or an Atmosphere child merely because the domain exists.

| Path shape | Verified repository state | Bounded posture |
|---|---|---|
| `data/registry/atmosphere/` | This parent README and the `sources/` child | Domain-first compatibility parent; independent registry-record writes denied |
| [`data/registry/atmosphere/sources/`](sources/README.md) | Compatibility README | Read-only source-navigation view under `DIR-SOURCE-004`; no independent descriptor writes |
| [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) | Canonical-lane README plus two `PROPOSED` placeholders in bounded inspection | Canonical placement for Atmosphere source identities under `DIR-SOURCE-003`; admission remains unverified |
| [`data/registry/datasets/`](../datasets/README.md) | Registry-family parent | Dataset identity and state only; do not duplicate it under this domain parent |
| [`data/registry/layers/`](../layers/README.md) | Registry-family parent | Layer identity and delivery metadata only; not automatically an Atmosphere child here |
| [`data/registry/domains/`](../domains/README.md) | Registry-family parent | Domain-state records only |
| [`data/registry/rights/`](../rights/README.md) | Registry-family parent | Rights identities and profiles only |
| [`data/registry/sensitivity/`](../sensitivity/README.md) | Registry-family parent | Sensitivity identities and profiles only |
| [`data/registry/crosswalks/`](../crosswalks/README.md) | Registry-family parent | Mapping-state claims only |

`DIR-SOURCE-003` places machine source identities and descriptors under `data/registry/sources/`. `DIR-SOURCE-004` permits `data/registry/<domain>/sources/` only as a generated view when the subtype-first record is canonical; it may not act as an independent writer.

The adjacent `air` versus `atmosphere` naming and alias pattern remains **NEEDS VERIFICATION**. This README does not rename identities, choose a code alias, or authorize a migration by implication.

> [!IMPORTANT]
> Preserve this parent until its writers, readers, links, aliases, generated views, LFS or external-storage relationships, and external consumers are inventoried. Do not delete, redirect, repurpose, promote, or retire it without an accepted migration decision, reference closure, parity evidence where applicable, consumer handling, and a rollback target.

<a id="current-bounded-inventory"></a>

## Current bounded inventory

This inventory is grounded in the pinned repository search and exact file reads used for this revision. It is not a complete recursive-tree guarantee.

| Surface | Verified content | What it does not establish |
|---|---|---|
| `data/registry/atmosphere/README.md` | This compatibility-parent README | No registry payload, activation, policy, proof, release, or public-serving state |
| [`sources/README.md`](sources/README.md) | No-independent-write Atmosphere source compatibility view | No local source authority or descriptor inventory |
| [`data/registry/sources/atmosphere/README.md`](../sources/atmosphere/README.md) | Draft subtype-first source-lane README | No accepted schema, active admission, complete inventory, or runtime reader |
| [`aqs.source.json`](../sources/atmosphere/aqs.source.json) | `PROPOSED` placeholder linked to an Atmosphere verification backlog | Not a conformant or active AQS `SourceDescriptor` |
| [`knowledge_character.json`](../sources/atmosphere/knowledge_character.json) | `PROPOSED` placeholder created from documentation inventory | Not accepted vocabulary, source-role, or admission authority |
| [`source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | `PROPOSED` metadata with an empty `entries` list | No active source, steward assignment, rights clearance, or activation decision |
| [Atmosphere registry schema index](../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Draft documentation index | No concrete registry-schema inventory or accepted schema home |
| [Atmosphere source fixtures](../../../fixtures/domains/atmosphere/sources/README.md) | Draft synthetic fixture guidance | No authoritative records; payload inventory and executable validation remain unverified |
| [Atmosphere workflow](../../../.github/workflows/domain-atmosphere.yml) | Read-only readiness checks and explicit holds | No live fetch, descriptor validation, proof production, release approval, or publication |
| [Link-check workflow](../../../.github/workflows/link-check.yml) | Documentation-QA readiness hold | No local or external links are currently checked |

Do not infer absence from bounded inspection alone. A complete inventory requires a pinned recursive tree, file classification, generated-file detection, LFS or external-storage review, and writer/consumer analysis.

<a id="repository-fit"></a>

## Repository fit

| Responsibility | Owning surface | Relationship to this path |
|---|---|---|
| Registry governance | [`data/registry/README.md`](../README.md) | Parent registry responsibility boundary |
| Canonical source family | [`data/registry/sources/README.md`](../sources/README.md) | Subtype-first source identity, admission, and routing family |
| Atmosphere source lane | [`data/registry/sources/atmosphere/`](../sources/atmosphere/README.md) | Canonical placement for Atmosphere source records; current content remains draft or proposed |
| Domain-first source view | [`sources/`](sources/README.md) | Compatibility navigation; no independent descriptor writes |
| Dataset, layer, domain, rights, sensitivity, and crosswalk families | Their subtype-first registry parents | Separate registry responsibilities; this parent does not own copies |
| Human source guidance | [Atmosphere Source Registry](../../../docs/domains/atmosphere/SOURCE_REGISTRY.md) and [Source Descriptor Standard](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft guidance and admission discipline; not runtime or release proof |
| Semantic meaning | [`contracts/source/source_descriptor.md`](../../../contracts/source/source_descriptor.md) | `SourceDescriptor` meaning and anti-collapse invariants |
| Machine shape | [Source schemas](../../../schemas/contracts/v1/source/README.md) and [Atmosphere registry schema index](../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Machine shape and draft indexing; accepted pairing and enforcement need verification |
| Policy | [`policy/domains/atmosphere/`](../../../policy/domains/atmosphere/README.md) | Domain policy boundary; a registry file cannot make allow, deny, restrict, hold, or release decisions |
| Governance projection | [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | `PROPOSED` source-authority projection; empty at the pinned base |
| Workflow evidence | [`domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml) | Explicit validation, proof, and release-readiness holds |
| Payload lifecycle | [RAW](../../raw/atmosphere/README.md), [WORK](../../work/atmosphere/README.md), [QUARANTINE](../../quarantine/atmosphere/README.md), and [PROCESSED](../../processed/atmosphere/README.md) | Atmosphere source and derived bytes; never stored in this parent |
| Process and evidence support | [Receipts](../../receipts/atmosphere/README.md) and [proofs](../../proofs/atmosphere/README.md) | Separate process-memory and evidence-support families |
| Discovery and delivery | Current [catalog](../../catalog/domain/atmosphere/README.md), [release candidate](../../../release/candidates/atmosphere/README.md), and [published carriers](../../published/atmosphere/README.md) | Downstream surfaces; none inherits authority from this registry parent |
| Public consumers | Governed APIs and release-approved carriers | Must not read registry internals directly |

<a id="confirmed-child-lanes"></a>

## Confirmed child lanes

The bounded inspection confirms this local structure:

```text
data/registry/atmosphere/
├── README.md
└── sources/
    └── README.md
```

| Child | Confirmed role | Boundary |
|---|---|---|
| [`sources/`](sources/README.md) | Human-readable compatibility view for readers entering through the Atmosphere domain | Not an independent writer, activation lane, payload store, policy source, proof, release record, current-conditions service, or public data surface |

This direct-child map does not authorize additional domain-first registry families or claim that payloads exist. Do not create empty dataset, layer, domain, rights, sensitivity, or crosswalk children merely to make this parent look complete.

<a id="registry-boundary"></a>

## Registry boundary

| Rule | Required handling |
|---|---|
| No parallel authority | Do not create authoritative registry records under this parent when a subtype-first family owns the object |
| One canonical identity | Register a source or other governed identity once; derived views carry the canonical ID |
| Read-only compatibility views | Generate from canonical inputs, record source/output digests and expiry, verify parity, and prohibit manual copies |
| Preserve provider lineage | Retain original publisher, network, institution, sensor owner, dataset, and aggregation path where applicable |
| Preserve source role | Do not upgrade modeled, aggregate, administrative, candidate, contextual, restricted, or preliminary material into observed or regulatory truth |
| Preserve measurement context | Keep parameter, units, method, instrument or algorithm, averaging interval, QA, revision, missingness, and uncertainty visible |
| Preserve time and spatial support | Keep observation, issue, valid, model-run, forecast, retrieval, expiration, correction, and stale times distinct; retain point, station, grid, raster, plume, polygon, and aggregate support |
| Rights and sensitivity fail closed | Unknown terms, attribution, redistribution, access, privacy, precision, facility security, or operational posture blocks activation and public use |
| Registry is not payload, proof, policy, catalog, or release | Registry records may reference those authorities but cannot replace them |
| Watchers do not publish | Drift and freshness checks may propose work or emit receipts; they cannot activate, release, or publish |
| Public clients do not read this parent | APIs, maps, dashboards, search, graph/vector indexes, exports, alerts, and AI surfaces use governed released interfaces |

<a id="atmosphere-safety-boundary"></a>

## Atmosphere safety and integrity boundary

A source may be public while its Atmosphere use remains restricted, stale, non-comparable, or non-authoritative. Registry routing must preserve source role, provider lineage, parameter, units, method, averaging interval, temporal scope, spatial support, quality, uncertainty, rights, sensitivity, review state, and release state.

| Integrity dimension | Required preservation | Fail-closed boundary |
|---|---|---|
| Regulatory monitoring | Parameter, units, method, instrument, averaging interval, QA, station/network, jurisdiction, revision, and time scope | Registry presence does not establish current conditions, compliance, or release permission |
| AQI, smoke, and advisory context | Issuing authority, index/category definition, pollutant, issue/valid/expiration time, caveats, stale state, and official-source routing | Do not present AQI as raw concentration, exposure dose, health diagnosis, or emergency direction |
| Weather stations and mesonets | Station/sensor identity, siting, units, method, QA flags, observation time, missingness, and stale markers | Do not infer universal quality, representativeness beyond support, or unrestricted reuse |
| Satellite aerosol, smoke, fire, and cloud-adjacent products | Product/algorithm identity, footprint, resolution, QA, acquisition time, cloud/surface limits, and source role | AOD or smoke context is not direct surface PM2.5 or measured exposure |
| Forecast, reanalysis, interpolation, and smoke-model fields | Model/version, run time, forecast hour, valid time, inputs, uncertainty, resolution, and validation scope | Do not relabel modeled or interpolated values as observations or official advisories |
| Climate normals and anomalies | Baseline period, method, scale, uncertainty, revision, and comparison basis | Do not present them as real-time observations or unchanged across editions |
| Low-cost, community, research, or local networks | Calibration, correction, confidence, siting, owner, terms, privacy, method, and review posture | Do not infer regulatory equivalence, universal representativeness, or unrestricted reuse |
| Missingness and revision | Missing, zero, below detection, invalid, provisional, revised, withdrawn, unavailable, and stale states | Do not coerce missing or invalid data to zero, “good,” current, or final |
| Spatial support | Monitor point, station network, grid cell, raster footprint, plume, polygon, regional aggregate, resolution, and uncertainty | Do not convert regional or gridded values into exact point truth |
| Cross-domain joins | Source role, time, scale, uncertainty, join purpose, sensitivity, and owning downstream domain | Atmosphere context does not establish crop, health, habitat, hydrology, infrastructure, or hazard conclusions owned elsewhere |
| Correction and stale-state propagation | Canonical revision, corrected value, supersession, withdrawal, compatibility parity, consumer refresh, and rollback | Do not keep stale views, caches, projections, maps, or generated answers after a governed correction |

Consequential public claims require an appropriate `EvidenceRef` to resolve to an `EvidenceBundle`, plus policy and sensitivity evaluation, review and release state, citation, correction path, and rollback support. AI-generated language remains interpretive and evidence-subordinate.

<a id="what-belongs-here"></a>

## What belongs here

Until an accepted migration or retirement decision changes the path, accepted content is limited to:

- this boundary README;
- the existing child compatibility README;
- pointer-only alias, redirect, migration, or tombstone notes that resolve to one canonical subtype-first identity;
- public-safe correction, supersession, withdrawal, and rollback metadata for an approved migration;
- a deterministic generated navigation index only after its canonical inputs, generator, accountable owner, edit policy, source/output digests, parity check, expiry, consumers, regeneration command, rollback, and exit criteria are verified;
- explicit hold or verification items that do not activate, ingest, promote, release, or publish.

Manual creation of new authoritative registry records or new domain-first registry families is denied.

<a id="what-does-not-belong-here"></a>

## What does not belong here

| Do not place or maintain here | Owning surface or required action |
|---|---|
| New or independently maintained source descriptors, intake records, or activation decisions | Accepted subtype-first source registry and governing decision process |
| Dataset, layer, domain, rights, sensitivity, or crosswalk records written as domain-first authority | Use the owning subtype-first registry family |
| Observations, station series, grids, rasters, model runs, satellite products, advisories, reports, API responses, or downloaded files | Governed RAW, WORK, QUARANTINE, or PROCESSED Atmosphere lanes |
| Contracts or schemas | `contracts/` and `schemas/` |
| Rights, sensitivity, stale-state, access, public-health, advisory, regulatory, or release policy | `policy/` and official authorities |
| Receipts, proofs, catalogs, release decisions, correction notices, rollback cards, or published carriers | Their separate responsibility roots |
| Connector, watcher, pipeline, package, validator, fixture, test, API, map, dashboard, search, graph, vector-index, alert, or AI implementation | The applicable implementation responsibility root |
| Credentials, tokens, signed URLs, private endpoints, facility-security detail, restricted operational information, or unsafe precision | Approved secret or restricted storage; never ordinary public-repository content |

<a id="inputs-and-outputs"></a>

## Inputs and outputs

| Direction | Accepted surface | Boundary |
|---|---|---|
| Input | Canonical registry identities and subtype-family records | Must resolve to one accepted writer or remain explicitly unavailable |
| Input | Provider lineage, source role, rights, sensitivity, parameter/method, units, averaging interval, time, spatial support, quality, correction, and rollback metadata | Must come from accepted evidence or remain unresolved |
| Input | Contracts, schemas, policies, fixtures, validators, receipts, proofs, catalogs, reviews, releases, corrections, and rollback references | A link does not prove acceptance, execution, evidence closure, or release |
| Input | Accepted migration record and canonical-to-compatibility mapping | Required before generated, redirect, or retirement behavior |
| Output | Human navigation to canonical registry and governance surfaces | Read-only and non-authoritative |
| Output | Optional deterministic compatibility projection | Requires one-way generation, parity evidence, expiry, consumer inventory, cache handling, and rollback |
| Output | Structured hold, migration, or verification item | Must not activate a source, admit payloads, approve policy, release, or publish |

This parent has no normal public API, UI, map, alert, health-guidance, compliance, emergency, or generated-answer contract.

<a id="current-workflow-evidence"></a>

## Current workflow evidence

The current [`domain-atmosphere`](../../../.github/workflows/domain-atmosphere.yml) workflow is an explicit readiness-hold workflow:

- it triggers on pull requests, pushes to `main`, and manual dispatch;
- it uses GitHub-hosted `ubuntu-latest`, `contents: read`, and `persist-credentials: false`;
- it performs no live source request;
- it checks required boundary files and detects whether executable Atmosphere tests, validators, proof producers, or release machinery have surfaced;
- it emits explicit holds because accepted executable Atmosphere validation, proof production, and release dry-run commands are not established.

A green held result is readiness evidence only. It is not registry validation, source admission, descriptor validity, observation accuracy, AQI or concentration equivalence, health advice, regulatory determination, emergency authority, evidence closure, release approval, or publication.

The current [`link-check`](../../../.github/workflows/link-check.yml) workflow is also an explicit governed hold. It does not check local paths, anchors, images, redirects, citations, or external URLs. Link resolution, when implemented, remains documentation QA rather than truth, evidence, policy, or release authority.

<a id="validation-and-maintenance"></a>

## Validation and maintenance

Before changing this README or adding compatibility material:

- re-pin the repository base and re-read adopted Directory Rules v2, ADR-0029, the parent registry contract, child compatibility README, and canonical subtype-first target;
- inventory direct children, canonical records, authoritative writers, readers, references, aliases, generated markers, LFS or external storage, and external consumers;
- confirm every object belongs to a verified subtype-first family and does not mint a competing identity;
- preserve provider lineage, source role, parameter/method, units, averaging interval, rights, sensitivity, time/freshness, spatial support, quality, uncertainty, citation, correction, supersession, withdrawal, and rollback state;
- verify generated views against canonical input/output digests and fail closed on missing, ambiguous, stale, restricted, unit-incompatible, spatially mismatched, or inconsistent records;
- preserve negative states such as missing, invalid, provisional, below-detection, stale, withdrawn, and denied without coercion;
- verify metadata, one H1, heading order, anchors, links, badges, alerts, tables, code fences, HTML comments, UTF-8 encoding, and final newline;
- verify no payload, secret, private endpoint, facility-security detail, restricted operational information, misleading health/advisory statement, unsafe precision, or public-serving path is introduced;
- record generator, parity, expiry, consumer-refresh, cache-invalidation, and rollback evidence—or retain the compatibility surface as README-only.

The Atmosphere and link-check workflows must be interpreted according to their explicit hold scope. A green held workflow or successful Markdown source inspection does not prove registry enforcement, source activation, measurement correctness, rights clearance, stale-state handling, evidence closure, release readiness, or public safety.

<a id="open-verification"></a>

## Open verification

| Item | Status | Evidence required |
|---|---|---|
| Complete direct-child and recursive inventory | **NEEDS VERIFICATION** | Pinned tree, file classifications, generated markers, LFS/external-store review |
| Active writers and consumers | **UNKNOWN** | Connector, watcher, pipeline, tool, workflow, runtime, API/UI, and external-consumer inventory |
| Canonical families for non-source Atmosphere registry records | **NEEDS VERIFICATION** | Accepted subtype taxonomy, IDs, contracts, schemas, writers, consumers, and migrations |
| Child compatibility generator, expiry, and parity check | **NOT VERIFIED** | Repository-owned generator, deterministic fixtures, tests, input/output digests, consumer refresh, rollback |
| Concrete descriptor inventory under `data/registry/sources/atmosphere/` | **UNKNOWN** beyond two placeholders in bounded inspection | Pinned tree, descriptors, identities, rights/sensitivity review, and validation |
| Canonical Atmosphere source README modernization | **NEEDS VERIFICATION** | Align its pre-adoption topology and slug text with accepted Directory Rules without changing descriptor state |
| `air` versus `atmosphere` path and code aliases | **NEEDS VERIFICATION** | Registered domain slug, alias map, consumers, migration plan, and accepted decision where identity changes |
| SourceDescriptor contract and schema authority | **NEEDS VERIFICATION** | Accepted contract/schema pairing, canonical path, compatibility policy, fixtures, and validator |
| Atmosphere source activation state | **UNKNOWN** | Populated source-authority entry and reviewed activation decision |
| Parameter, unit, method, temporal, spatial-support, quality, and stale-state enforcement | **UNKNOWN** | Schema fields, negative fixtures, validators, receipts, and representative runs |
| Rights, sensitivity, correction, supersession, withdrawal, and rollback enforcement | **UNKNOWN** | Policy, review records, negative fixtures, receipts, and drills |
| Accountable stewardship and CODEOWNERS routing | **NEEDS VERIFICATION** | Approved responsibility assignments; CODEOWNERS is routing only |
| Public or operational consumers and cache invalidation | **UNKNOWN** | Governed routes, releases, access controls, caches, correction propagation, withdrawal, and rollback drills |
| Final migration disposition | **PROPOSED / NEEDS VERIFICATION** | Retained compatibility parent, generated mirror, redirect/tombstone, or retirement decision |
| Physical deletion eligibility | **HOLD** | Zero-writer, zero-consumer, link closure, parity/retirement, external-consumer review, and rollback evidence |

Unknowns narrow behavior and block higher-authority claims; they do not authorize plausible defaults.

<a id="correction-migration-and-rollback"></a>

## Correction, migration, and rollback

1. Correct the canonical subtype-first record or governing authority first.
2. Emit the required correction, supersession, withdrawal, deactivation, review, release, or rollback record through its owning process.
3. Regenerate any admitted compatibility view from corrected canonical inputs.
4. Invalidate stale view bytes and dependent caches, projections, indexes, maps, dashboards, and generated-answer carriers where governed consumers exist.
5. Verify identity, source and output digests, parity, negative states, effective time, consumer refresh, and rollback target before use resumes.
6. Preserve old-to-new identity mapping, aliases, source role, provider lineage, correction history, and consumer handling.
7. If safe regeneration or migration cannot be proven, retain this README-only compatibility boundary and fail closed.

Before merge, rollback is closing the draft pull request and leaving the branch unmerged. After merge, use a transparent revert or follow-up pull request; do not restore independent registry-record writes here or alter canonical records merely to roll back this README.

<a id="related-authority"></a>

## Related authority

| Reference | Role |
|---|---|
| [Directory Rules v2](../../../docs/doctrine/directory-rules.md) | Adopted placement doctrine; see `DIR-SOURCE-003`, `DIR-SOURCE-004`, and subtype-first registry placement |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopts the exact Directory Rules v2 bytes and establishes single-write doctrine authority |
| [`data/registry/`](../README.md) | Parent registry responsibility boundary |
| [Canonical source registry](../sources/README.md) | Source-family parent; current README maturity does not elevate placeholder records |
| [Atmosphere source lane](../sources/atmosphere/README.md) | Subtype-first Atmosphere source-registry surface |
| [Domain-first source view](sources/README.md) | No-independent-write compatibility boundary |
| [`aqs.source.json`](../sources/atmosphere/aqs.source.json) | `PROPOSED` placeholder; not active admission evidence |
| [`knowledge_character.json`](../sources/atmosphere/knowledge_character.json) | `PROPOSED` placeholder; not accepted vocabulary or authority |
| [Source Descriptor Standard](../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft human guidance for source identity, role, rights, sensitivity, cadence, and citation |
| [SourceDescriptor contract](../../../contracts/source/source_descriptor.md) | Draft semantic contract and anti-collapse rules |
| [Atmosphere registry schema index](../../../schemas/contracts/v1/domains/atmosphere/registry/README.md) | Draft schema-placement index; concrete registry schemas unverified |
| [Atmosphere source fixtures](../../../fixtures/domains/atmosphere/sources/README.md) | Synthetic fixture guidance; not source authority |
| [Source-authority register](../../../control_plane/source_authority_register.yaml) | `PROPOSED` machine projection; empty at the pinned base |
| [Atmosphere workflow](../../../.github/workflows/domain-atmosphere.yml) | Explicit readiness holds; not source admission, proof, release, or publication authority |
| [Link-check workflow](../../../.github/workflows/link-check.yml) | Explicit documentation-QA readiness hold; no links are currently checked |
| [Atmosphere release candidates](../../../release/candidates/atmosphere/README.md) | Candidate boundary; a candidate is not a release |

## Change history

### v0.2.0 — 2026-07-28

- aligned the parent with the merged `v0.4.0` child compatibility view and current repository evidence;
- added a commit- and blob-pinned inventory of the canonical lane, placeholders, empty source-authority register, schema index, fixtures, and workflows;
- replaced generic ownership with explicit `NEEDS VERIFICATION` stewardship roles;
- expanded provider-lineage, parameter/method, units, averaging, time, spatial-support, quality, missingness, revision, and stale-state controls;
- added current workflow interpretation, generated-view parity/expiry requirements, consumer refresh, cache invalidation, and stronger rollback controls;
- preserved the stable path, `doc_id`, no-independent-write compatibility posture, operational-safety boundary, and cite-or-abstain rule.

### v0.1.0 — 2026-07-27

- replaced the two-line greenfield stub with a governed Atmosphere registry parent boundary;
- aligned the path with accepted subtype-first registry placement and ADR-0029;
- documented the child compatibility view and canonical source writer without creating parallel authority;
- added Atmosphere source-role, time/freshness, rights, sensitivity, correction, rollback, and public-safety controls;
- added evidence-backed badges, navigation, repository-fit mappings, validation, and open verification.

KFM rule: `data/registry/atmosphere/` is a compatibility parent for public-safe navigation and lineage only. It is not an independent registry writer, payload store, Atmosphere truth authority, policy authority, evidence authority, release authority, health or emergency authority, or public data service.

[Back to top](#top)
