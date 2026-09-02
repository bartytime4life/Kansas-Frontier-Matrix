<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-settlements-infrastructure-readme
title: configs/domains/settlements-infrastructure/ — Settlements, Communities, and Infrastructure Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Settlements/Infrastructure steward · Settlements/place-identity steward · Infrastructure/security steward · Cultural/sovereignty reviewer · Source steward · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; settlements-infrastructure; place-identity-aware; legal-status-aware; critical-asset-aware; cultural-context-aware; source-role-aware; time-aware; non-secret; non-authoritative; no-live-binding; no-service-guarantee; not-emergency-operations; no-release-authority"
current_path: configs/domains/settlements-infrastructure/README.md
truth_posture: CONFIRMED canonical settlements-infrastructure config lane, parent configuration contract, repository-present domain doctrine and implementation-shaped surfaces, README-only bounded config inventory, placeholder/scaffold status of inspected package metadata, pipeline code, pipeline specs, policy, schema, validators, workflow, and tests, unresolved settlements-infrastructure versus settlement and infrastructure policy path variance, unresolved registry topology, and prior README lineage / PROPOSED future consumer-bound templates and accepted profile references / UNKNOWN direct consumers, loader behavior, precedence, deployment binding, exhaustive recursive inventory, runtime behavior, and publication use / NEEDS VERIFICATION accepted owners, canonical authority paths, source-role vocabulary, source rights, legal-status authority, place-identity rules, facility exposure rules, service-area and dependency semantics, freshness budgets, cultural review requirements, executable validation, scanners, CI enforcement, correction propagation, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 53dbff3ddbdcd05ea7a7c112d9db288b325d0cb5
  prior_blob: 47a1b267ff4309e0c3a68b6d1a3a3883b468dd2f
  bounded_path_search: configs/domains/settlements-infrastructure/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - ../../../docs/domains/settlements-infrastructure/VERIFICATION_BACKLOG.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/settlements-infrastructure/
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../policy/release/settlements-infrastructure/
  - ../../../data/registry/settlements-infrastructure/
  - ../../../data/registry/sources/settlements-infrastructure/
  - ../../../packages/domains/settlements-infrastructure/
  - ../../../pipelines/domains/settlements-infrastructure/
  - ../../../pipeline_specs/settlements-infrastructure/
  - ../../../tools/validators/domains/settlements-infrastructure/
  - ../../../tests/domains/settlements-infrastructure/
  - ../../../fixtures/domains/settlements-infrastructure/
  - ../../../apps/explorer-web/src/features/domains/settlements_infrastructure/
  - ../../../data/raw/settlements-infrastructure/
  - ../../../data/work/settlements-infrastructure/
  - ../../../data/quarantine/settlements-infrastructure/
  - ../../../data/processed/settlements-infrastructure/
  - ../../../data/catalog/domain/settlements-infrastructure/
  - ../../../data/triplets/settlements-infrastructure/
  - ../../../data/published/layers/settlements-infrastructure/
  - ../../../data/receipts/settlements-infrastructure/
  - ../../../data/proofs/settlements-infrastructure/
  - ../../../release/candidates/settlements-infrastructure/
  - ../../../release/manifests/settlements-infrastructure/
  - ../../../docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
tags: [kfm, configs, settlements, municipalities, census-places, historic-townsites, infrastructure, facilities, service-areas, dependencies, critical-assets, place-identity, legal-status, source-role, time, sensitivity, no-secrets, no-live-binding, governance]
notes:
  - "The bounded repository search for configs/domains/settlements-infrastructure returned this README only. No executable config payload or indexed direct consumer was found."
  - "The surrounding domain has many documentation and implementation-shaped surfaces, but inspected package metadata, pipeline files, pipeline specs, policy modules, schemas, validators, workflow jobs, and test lanes are draft scaffolds, placeholders, empty stage lists, permissive schemas, NotImplemented entrypoints, TODO-only jobs, or otherwise not proof of production behavior."
  - "Repository evidence contains settlements-infrastructure versus settlement path variance, infrastructure sensitivity-policy projections, and domain-first versus subtype-first source-registry paths. This lane does not resolve, alias, or duplicate those conflicts."
  - "Configuration may reference an accepted place-identity, source, legal-status, temporal, sensitivity, public-safe geometry, service-area, dependency, review, or release profile. It cannot create municipal authority, place truth, service availability, operational status, critical-asset clearance, policy, evidence, release, or publication state."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements, Communities, and Infrastructure Domain Configuration

`configs/domains/settlements-infrastructure/`

> Safe-to-commit configuration documentation and future consumer-bound templates for settlements, municipalities, census places, historic townsites, communities, infrastructure assets, facilities, networks, service areas, operators, condition observations, dependencies, and public-safe derivatives. This lane is not municipal legal authority, utility or service-availability authority, emergency operations, infrastructure security clearance, land-title proof, source authority, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![critical-assets](https://img.shields.io/badge/critical__assets-fail__closed-red)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Identity](#place-identity-legal-status-and-object-boundaries) · [Roles](#source-role-and-knowledge-character) · [Time](#time-freshness-and-stale-state) · [Critical assets](#critical-infrastructure-facilities-and-dependencies) · [Geometry](#geometry-service-areas-access-and-public-safe-representation) · [Cultural context](#historic-cultural-community-and-sovereignty-context) · [Logging](#logging-telemetry-and-observability) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-and-deactivation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable configuration payload or direct consumer binding is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for place identity, legal status, infrastructure status, access, services, policy, evidence, or release  
> **Runtime posture:** no loader, precedence rule, source activation, network fetch, place merge, facility exposure, service calculation, dependency graph, public layer, release, or publication is established by this README

> [!CAUTION]
> KFM settlement and infrastructure context is evidence and governed publication material—not proof that a municipality is legally current, a facility is operational, a service is available, a dependency is complete, a site is safe to approach, a boundary is legally controlling, or critical-asset detail is suitable for public exposure. Missing evidence, unclear rights, stale status, unresolved cultural authority, or uncertain sensitivity fails closed.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `settlements-infrastructure` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, select, compare, generalize, aggregate, render, or package already-governed material, but they cannot decide:

- whether a settlement, municipality, census place, townsite, ghost town, fort, mission, reservation community, neighborhood, or unincorporated place exists;
- whether a place name, legal status, incorporation status, jurisdiction, boundary, annexation, dissolution, or historical interpretation is current or authoritative;
- whether an infrastructure asset, network, facility, service area, operator, condition observation, or dependency is complete, current, safe, available, public, or legally accessible;
- whether census geography is municipal or jurisdictional truth;
- whether map geometry proves ownership, title, access, service entitlement, legal boundary, or facility status;
- whether an administrative roster is an observed condition;
- whether a modeled, inferred, candidate, synthetic, or graph-projected relationship is source truth;
- whether exact critical-asset geometry, operator-sensitive details, condition, dependency, vulnerability, access, or private-property context may be exposed;
- whether a historic or culturally sensitive place may be represented precisely or publicly;
- whether evidence supports a claim;
- whether a source is admitted, active, licensed, current, or redistributable;
- whether an artifact may be promoted, released, or published.

This README is intended for configuration maintainers, domain stewards, security and sensitivity reviewers, source and evidence stewards, consumer owners, validation owners, policy and release reviewers, and contributors checking Directory Rules placement.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Domain scope and meaning | **None.** Human doctrine remains under `docs/domains/settlements-infrastructure/`; semantic contracts remain in their accepted contract home. |
| Settlement or community identity | **None.** Config cannot merge places, select a canonical name by convenience, infer continuity, or equate historic and present places. |
| Municipality or jurisdiction status | **None.** Config cannot create, infer, renew, supersede, or prove legal status, incorporation, jurisdiction, annexation, dissolution, or authority. |
| Census geography | **None.** Config cannot relabel a census place as a municipality or legal jurisdiction. |
| Infrastructure identity or status | **None.** Config cannot prove asset existence, ownership, operation, condition, service availability, dependency, access, safety, or criticality. |
| Source identity, role, rights, cadence, freshness, and activation | **None.** These require source registry, rights, policy, review, and current source evidence. |
| Schema or contract shape | **None.** Config may reference accepted schemas/contracts but cannot duplicate or redefine them. |
| Sensitivity, redaction, aggregation, clustering, or public-safe geometry | **None.** Config may select an accepted profile; it cannot create, weaken, or approve a rule. |
| Evidence or claim truth | **None.** Config cannot create an `EvidenceBundle`, close evidence, validate a consequential claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Config cannot authorize promotion, release, public display, service promises, emergency guidance, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and documented precedence. |

A configuration value may point to an authority surface. It does not become authority through repetition, successful parsing, operational convenience, use in a map, graph, search index, dashboard, Evidence Drawer, Focus Mode, export, or AI surface.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `53dbff3ddbdcd05ea7a7c112d9db288b325d0cb5` |
| Prior README blob | `47a1b267ff4309e0c3a68b6d1a3a3883b468dd2f` |
| Bounded config-path result | `configs/domains/settlements-infrastructure/README.md` only |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical config lane | **CONFIRMED** | The requested README exists under the parent domain-config boundary. |
| Parent config contract | **CONFIRMED** | `configs/domains/README.md` v0.4 defines documentation-only, non-secret, non-authoritative child lanes. |
| Domain doctrine | **CONFIRMED repository-present** | Scope, object families, source families, sensitivity, lifecycle, validation, and cross-lane boundaries are documented. |
| Current config contents | **README ONLY IN BOUNDED SEARCH** | No indexed payload or direct consumer was found. Exhaustive inventory remains `NEEDS VERIFICATION`. |
| Direct config consumer | **NOT FOUND IN BOUNDED SEARCH** | Differently named or unindexed consumers remain `UNKNOWN`. |
| Package metadata | **GREENFIELD PLACEHOLDER** | `pyproject.toml` declares version `0.0.0`; it does not prove implemented helpers. |
| Pipeline implementation | **PLACEHOLDER** | Inspected `ingest.py`, `normalize.py`, `validate.py`, `publish.py`, and `rollback.py` contain only greenfield placeholder comments. |
| Pipeline specs | **EMPTY STAGE LISTS** | Inspected ingest, validate, and publish specs declare `stages: []`. |
| Domain policy | **PROPOSED / INCOMPLETE** | Inspected rules are default-only scaffolds or greenfield stubs, not complete enforceable policy. |
| Domain schemas | **PROPOSED STUBS** | Schema index is a greenfield scaffold; inspected schema permits additional properties and carries placeholder fields. |
| Domain validators | **NOT IMPLEMENTED IN INSPECTED FILES** | Inspected validators raise `NotImplementedError`. |
| Domain workflow | **TODO-ONLY SCAFFOLD** | Validation, proof, and publish-dry-run jobs echo TODO commands. |
| Domain tests | **README/INDEX MATURITY** | Test README confirms intended guardrails and one identity child README; executable coverage and pass rates remain unverified. |
| Explorer Web feature | **README BOUNDARY CONFIRMED** | Feature contract exists; route wiring, modules, adapters, receipts, release state, and runtime behavior remain unverified. |
| Registry topology | **CONFLICTED / NEEDS VERIFICATION** | Domain-first and subtype-first source-registry patterns both exist; duplication is forbidden pending resolution. |
| Path/slug posture | **CONFLICTED** | Working `settlements-infrastructure` segment coexists with `settlement` and `infrastructure` projections in older/crosswalk paths. |
| Source-role vocabulary | **CONFLICTED / NEEDS VERIFICATION** | Older authority/observation/context/model wording and newer role sets require governance; config must not create aliases. |
| Runtime, release, publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use or public exposure. |

Directory presence must not trigger config discovery, source activation, network access, place canonicalization, municipal-status inference, facility aggregation, dependency graphing, map-layer creation, emergency guidance, lifecycle promotion, release, or publication.

[Back to top](#top)

---

## What belongs here

Only configuration-supporting material that is safe to commit and explicitly bound to a verified consumer belongs here.

| Accepted material | Required posture |
|---|---|
| This README | Current, evidence-bounded, and aligned with the parent contract. |
| `*.template.yaml` / `*.example.yaml` / `*.example.json` / `*.example.toml` | Parseable, non-secret, synthetic, explicit consumer, explicit class/version, no automatic activation. |
| Place-identity profile references | Reference accepted identity/normalization profiles; never define legal or canonical identity here. |
| Legal-status evidence profile references | Select accepted municipal/legal-status validation profiles; never infer legal status from labels, census geography, or geometry. |
| Source-role and source-family selector references | Preserve accepted source roles and rights; never activate a source or upgrade its role. |
| Time/freshness/stale-state profile references | Select accepted temporal handling; never erase vintage, valid time, retrieval time, or stale state. |
| Public-safe geometry, clustering, aggregation, and redaction profile references | Select accepted reviewed profiles; never encode exact restricted facilities or approve publication. |
| Infrastructure exposure-class references | Reference accepted security/sensitivity classifications; never classify a real asset here without governing evidence and review. |
| Review-routing defaults | Conservative HOLD/ABSTAIN/review-required defaults; never waive mandatory review. |
| Compatibility notes | Time-bounded migration guidance with owner, sunset, test, and rollback. |
| Tiny synthetic fixtures for configuration parsing | Clearly fake; no real facility, operator, dependency, private parcel, living person, or culturally sensitive location. |

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Correct handling |
|---|---|
| Credentials, tokens, keys, certificates, cookies, signed URLs, private endpoints | External secret/config system or ignored local override; treat exposure as an incident. |
| Live source endpoints or production connection strings | Deployment controls; do not commit private operational topology. |
| Actual source payloads, facility inventories, condition feeds, service telemetry, dependency graphs | Governed lifecycle lanes under `data/`, not config. |
| Exact critical-infrastructure or restricted facility geometry | Restricted lifecycle/policy/review lanes; public-safe derivative only after governed transform and release. |
| Vulnerability, access-control, emergency-response, security-system, dependency, or operator-sensitive detail | Restricted operational/security systems; not public config. |
| Private-property, living-person, title, ownership, or parcel joins | People/DNA/Land and policy-governed evidence paths; never config authority. |
| Cultural, sacred, reservation-community, mission, fort, archaeology, burial, or stewardship-sensitive exact detail | Rights-holder, cultural, sovereignty, archaeology, and sensitivity governance; fail closed. |
| Municipality, incorporation, jurisdiction, annexation, dissolution, legal boundary, or legal-status decisions | Legal-source evidence, contracts, policy, review, and current authority records. |
| Service availability, utility status, facility operation, safety, access, or emergency guidance | Official operational authority; KFM may provide cited context only. |
| Schema, contract, policy, registry, receipt, proof, catalog, graph, release, correction, or rollback objects | Their owning responsibility roots. |
| Package, pipeline, validator, app, or runtime implementation | `packages/`, `pipelines/`, `tools/`, `apps/`, or `runtime/`. |
| Generated reports, caches, screenshots, tiles, exports, or build outputs | `artifacts/`, released data homes, or ignored workspace as appropriate. |
| Settings that collapse Settlement, Municipality, CensusPlace, Townsite, GhostTown, Facility, ServiceArea, Operator, ConditionObservation, or Dependency | Reject; object family and role remain explicit. |
| Settings that turn map geometry into legal status, ownership, access, service entitlement, or operational truth | Reject; geometry is evidence/representation, not proof. |
| Automatic recursive discovery or filename-based activation | Reject until a governed discovery contract, allowlist, validator, and tests are accepted. |

[Back to top](#top)

---

## Inputs

A future config payload may be authored only from bounded, reviewable inputs:

- a named consumer requirement with owner and version;
- an accepted schema and semantic contract reference;
- accepted source, identity, legal-status, time, sensitivity, public-safe geometry, aggregation, or release profile identifiers;
- synthetic examples created solely to explain configuration shape;
- verified migration requirements for an existing key, consumer, or path;
- current rights, security, cultural, and source-role review as applicable.

Minimum authoring context:

1. `domain_slug: settlements-infrastructure`;
2. configuration class and environment scope;
3. exact intended consumer path and version;
4. explicit loader/binding mechanism;
5. parser and schema reference;
6. contract and policy references;
7. source-profile and rights references;
8. time/freshness/stale behavior;
9. sensitivity/exposure profile;
10. network and side-effect statement;
11. logging/redaction statement;
12. owner, review date, deprecation, and rollback.

Reject or quarantine inputs containing secrets, real operational values, exact restricted assets, private access data, living-person joins, unresolved rights, ambiguous legal status, stale status presented as current, or instructions to bypass evidence, policy, review, release, correction, or rollback.

[Back to top](#top)

---

## Outputs

This lane currently emits **documentation only**.

A future validated file may support a named consumer by providing:

- safe defaults;
- explicit profile references;
- parseable templates and examples;
- conservative review routing;
- compatibility/migration metadata;
- validation expectations.

It must not emit or authorize:

- municipal or jurisdiction truth;
- source admission or activation;
- place or facility canonicalization;
- infrastructure exposure classification;
- legal status, service availability, operational status, safety, access, or emergency guidance;
- lifecycle transitions;
- EvidenceBundles, proofs, receipts, catalogs, graph/triplet truth, or release objects;
- deployment credentials or live bindings;
- public layers, API answers, map truth, exports, or AI claims.

A consumer must explicitly opt in through reviewed implementation. Merely adding a file to this folder must have no runtime effect.

[Back to top](#top)

---

## Validation

No executable validator for this configuration lane is established by the inspected repository evidence. The following matrix is a **required target**, not a claim of current enforcement.

| Check | Required outcome | Current state |
|---|---|---:|
| Syntax and parser version | File parses under declared format/version. | `PROPOSED` |
| Accepted schema | Non-empty accepted schema validates known keys/types. | `NEEDS VERIFICATION`; inspected schemas are stubs. |
| Unknown keys | Fail or produce an explicit finite error; never silently broaden behavior. | `UNKNOWN` |
| Consumer compatibility | Named consumer loads exact path/version without hidden fallback. | `UNKNOWN` |
| Explicit binding | No recursive scan, filename activation, or ambient global state. | Required |
| Determinism | Same file/parser/profile versions normalize identically. | `PROPOSED` |
| Secret/private endpoint scan | No credentials, signed URLs, private hosts, or personal paths. | Required; automation unverified. |
| Critical-asset/sensitive-value scan | No exact restricted geometry, access, condition, dependency, vulnerability, or operator-sensitive value. | Required; automation unverified. |
| Cultural/living-person/private-property scan | No protected cultural, sovereignty, archaeology, living-person, parcel, title, or private-access detail. | Required; automation unverified. |
| Object-family separation | Settlement, Municipality, CensusPlace, Townsite, GhostTown, Facility, ServiceArea, Operator, ConditionObservation, Dependency remain distinct. | Required |
| Legal-status anti-inference | Census, label, geometry, or model context cannot create municipal/legal status. | Required |
| Source-role preservation | Config cannot upcast administrative/model/candidate/context material into observed/regulatory truth. | Required |
| Temporal integrity | Source, observed, valid/effective, retrieval, release, correction, supersession, and stale state remain visible where material. | Required |
| Public-safe transform | Accepted profile and transform/aggregation/redaction receipt are required; config alone cannot approve exposure. | Required |
| No-network parse | Parsing/basic validation is local and deterministic where practical. | `PROPOSED` |
| No side effect | Validation cannot fetch, write lifecycle state, publish, deploy, notify, or alter operations. | Required |
| Logging safety | Logs contain IDs/reason codes/digests, not sensitive payload values. | Required |
| Lifecycle isolation | No registry, receipt, proof, catalog, graph, release, or published object stored here. | Required |
| Documentation links | Relative links and anchors resolve. | Manual/local validation for this revision. |
| Staleness review | Owner, consumer, profile versions, review date, and sunset remain current. | Review on change or within six months. |

### Finite configuration-review outcomes

These outcomes apply only to config readiness; they are not policy or release decisions.

| Outcome | Meaning |
|---|---|
| `PASS` | Config support checks pass; use is still bounded by consumer, evidence, policy, and release state. |
| `HOLD` | Checkable uncertainty remains; file must remain inactive. |
| `DENY` | Secret, protected detail, unsafe exposure, authority bypass, permissive fallback, or operational side effect is present. |
| `ERROR` | Parser, validator, or review process failed unexpectedly; failure is not permission. |

### Workflow preflight

The inspected domain workflow triggers on pull requests and pushes to `main`, uses GitHub-hosted runners, and currently runs TODO echo commands for domain validation, proof building, and publish dry-run. It does not prove substantive validation, proof closure, release safety, or branch protection.

[Back to top](#top)

---

## Review burden

| Change class | Minimum review posture |
|---|---|
| README clarification | Config/docs reviewer plus Settlements/Infrastructure steward. |
| New config payload | Config steward + exact consumer owner + domain steward + validation steward. |
| Municipality/legal-status or boundary-related key | Add source/legal-status and policy reviewers. |
| Infrastructure asset, facility, service-area, operator, condition, dependency, or public-safe geometry key | Add infrastructure security/sensitivity reviewer and release reviewer. |
| Historic townsite, ghost town, fort, mission, reservation community, cultural/community key | Add cultural/sovereignty/rights-holder and archaeology reviewers as applicable. |
| Source selection, rights, cadence, or freshness key | Add source and rights reviewers. |
| Cross-lane join with roads/rail, hazards, hydrology, people/land, archaeology, or agriculture | Add affected domain steward. |
| Discovery, precedence, loader, schema-home, policy-home, registry topology, or slug change | ADR/path-governance review; not a config-only decision. |

`OWNER_TBD` is not accepted ownership. Automatic reviewer enforcement and branch protection remain `NEEDS VERIFICATION`.

Prefer one bounded concern per PR. Do not bundle config documentation with schema, policy, registry, data, release, or runtime rewrites.

[Back to top](#top)

---

## Related folders

| Responsibility | Repository surface | Relationship |
|---|---|---|
| Parent config contract | [`../README.md`](../README.md) | Defines all domain config lanes as non-secret, non-authoritative support. |
| Root config contract | [`../../README.md`](../../README.md) | Repo-wide configuration boundary. |
| Domain doctrine | [`../../../docs/domains/settlements-infrastructure/README.md`](../../../docs/domains/settlements-infrastructure/README.md) | Scope, object families, source families, sensitivity, lifecycle, and cross-lane ownership. |
| Path conflict register | [`../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | Tracks `settlements-infrastructure`, `settlement`, and `infrastructure` path variance. |
| Semantic contracts | `../../../contracts/domains/settlements-infrastructure/` and conflicted variants | Meaning authority; config references only. |
| Machine schemas | `../../../schemas/contracts/v1/domains/settlements-infrastructure/` and conflicted variants | Shape authority when accepted; inspected files remain draft/stub. |
| Domain policy | `../../../policy/domains/settlements-infrastructure/` | Admissibility inputs; inspected rules are scaffolds/stubs. |
| Release sensitivity policy | `../../../policy/release/settlements-infrastructure/` and unresolved infrastructure sensitivity paths | Public-safe clustering/generalization inputs; placement and implementation need verification. |
| Domain registry | `../../../data/registry/settlements-infrastructure/` | Existing domain-first routing/compatibility parent. |
| Source registry | `../../../data/registry/sources/settlements-infrastructure/` | Competing subtype-first pattern; topology unresolved. |
| Shared package | `../../../packages/domains/settlements-infrastructure/` | Package contract and placeholder metadata; not proof of implementation. |
| Pipelines | `../../../pipelines/domains/settlements-infrastructure/` | README plus inspected placeholder code. |
| Pipeline specs | `../../../pipeline_specs/settlements-infrastructure/` | Inspected specs have empty stage lists. |
| Validators | `../../../tools/validators/domains/settlements-infrastructure/` | Inspected validators raise `NotImplementedError`. |
| Tests/fixtures | `../../../tests/domains/settlements-infrastructure/`, `../../../fixtures/domains/settlements-infrastructure/` | Intended enforceability; executable coverage unverified. |
| Explorer feature | `../../../apps/explorer-web/src/features/domains/settlements_infrastructure/` | README boundary; implementation and routes unverified. |
| Lifecycle | `../../../data/{raw,work,quarantine,processed}/settlements-infrastructure/` | Evidence-bearing state; never config storage. |
| Catalog/graph/published | `../../../data/catalog/domain/settlements-infrastructure/`, `../../../data/triplets/settlements-infrastructure/`, `../../../data/published/layers/settlements-infrastructure/` | Derived/released carriers after gates close. |
| Release/correction/rollback | `../../../release/`, promotion and rollback runbooks | Decisions and reversible state transitions. |

[Back to top](#top)

---

## ADRs and drift triggers

No ADR is enacted by this README.

The following remain ADR/governance surfaces:

| Decision | Current posture |
|---|---:|
| `settlements-infrastructure` versus `settlement` contract/schema/pipeline variants | `CONFLICTED` |
| `policy/domains/settlements-infrastructure` versus `policy/sensitivity/infrastructure` and other sensitivity projections | `CONFLICTED / NEEDS VERIFICATION` |
| Domain-first versus subtype-first source-registry topology | `CONFLICTED / NEEDS VERIFICATION` |
| Accepted source-role vocabulary and compatibility mapping | `NEEDS VERIFICATION` |
| Universal config envelope | `OPEN / PROPOSED` |
| Auto-discovery, precedence, and missing-file fallback | `NO ACCEPTED DECISION VERIFIED` |
| Critical-asset exposure classes and public-safe clustering/generalization profiles | `NEEDS VERIFICATION` |
| Legal-status and municipality-evidence profiles | `NEEDS VERIFICATION` |
| Cultural/community/sovereignty review profiles | `NEEDS VERIFICATION` |

Do not resolve these by adding aliases, duplicate payloads, permissive defaults, or parallel authority inside `configs/`.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@53dbff3ddbdcd05ea7a7c112d9db288b325d0cb5`.

Review again before:

- the first non-README config payload;
- the first consumer binding;
- any loader/discovery/precedence decision;
- any municipality/legal-status profile;
- any critical-asset, service-area, condition, operator, dependency, public-safe geometry, clustering, or aggregation setting;
- any historic/cultural/community exposure setting;
- any resolution of the path, policy, registry, or source-role conflicts;
- six months pass.

[Back to top](#top)

---

## Scope and bounded context

Configuration in this lane may eventually support these object families without owning their truth:

### Place and community families

- `Settlement`
- `Municipality`
- `CensusPlace`
- `Townsite`
- `GhostTown`
- `Fort`
- `Mission`
- `ReservationCommunity`
- neighborhood or unincorporated-place profiles when accepted

### Infrastructure families

- `InfrastructureAsset`
- `NetworkNode`
- `NetworkSegment`
- `Facility`
- `ServiceArea`
- `Operator`
- `ConditionObservation`
- `Dependency`

### Cross-lane context

- roads/rail owns transport-route truth;
- hydrology owns water, wastewater, drainage, and flood evidence;
- hazards owns events, warnings, declarations, and life-safety authority;
- people/land owns living-person, ownership, parcel, title, residence, and private-land truth;
- archaeology/cultural authorities own sensitive site identity and access decisions;
- agriculture and spatial foundation lanes own their respective source truth.

A config may reference released or governed cross-lane profiles. It cannot mirror-author or override another lane's truth.

---

## Configuration class taxonomy

| Class | Purpose | Activation posture |
|---|---|---|
| `template` | Demonstrate supported fields and placeholders. | Never active by presence. |
| `example` | Explain realistic synthetic values. | Never active by presence. |
| `dev-default` | Conservative local-development defaults for a verified consumer. | Explicit opt-in only. |
| `test-default` | Deterministic no-network test settings. | Test harness only. |
| `review-default` | Hold, abstain, review, and caveat routing. | Cannot waive policy/release review. |
| `public-safe-template` | Select accepted generalization, clustering, aggregation, or redaction profiles. | Policy, receipt, review, and release still required. |
| `compatibility` | Temporary key/path mapping. | Time-bounded with sunset and rollback. |
| `production-binding` | Real endpoints, credentials, facility IDs, operator values, or operational state. | **Forbidden here.** |

---

## Minimum configuration contract

A non-trivial future payload must expose or document:

| Field | Requirement |
|---|---|
| `domain_slug` | `settlements-infrastructure`; no local aliasing. |
| `config_class` | One class from the taxonomy above. |
| `intended_consumer` | Exact repository path and component name. |
| `consumer_version` | Version/range or `NEEDS VERIFICATION`. |
| `format` / `parser_version` | Explicit and testable. |
| `schema_ref` | Accepted, non-empty schema reference. |
| `contract_refs` | Object meaning references; no duplication. |
| `policy_refs` | Rights, legal status, sensitivity, cultural review, release, and stale-state policy references. |
| `source_profile_refs` | Source IDs/roles/rights/cadence profiles; no activation. |
| `time_profile_ref` | Time-kind, freshness, stale, supersession, correction handling. |
| `exposure_profile_ref` | Critical-asset/public-safe geometry/clustering/aggregation/redaction profile. |
| `network_behavior` | `none` by default; any consumer network behavior documented separately. |
| `side_effects` | `none` for parse/validation. |
| `secret_posture` | External references only; no values. |
| `sensitivity_posture` | No restricted values or reconstructable clues. |
| `logging_posture` | IDs, reason codes, digests only; no protected payloads. |
| `override_mechanism` | Approved external/ignored local mechanism. |
| `owner` / `reviewed_at` | Named owner or `OWNER_TBD`; ISO review date. |
| `deprecation` / `rollback` | Replacement, sunset, deactivation, correction, and restore path. |

A machine-checkable universal envelope is **PROPOSED** and is not created by this README.

---

## Consumer binding, precedence, and discovery

### Explicit binding

A consumer must name the exact file it reads. Folder presence, globbing, recursive scanning, and “first matching filename” must not activate behavior.

### Precedence is undefined

This README does not establish an order among:

```text
base → domain → dev/test → local → environment → deployment
```

That sequence is illustrative only. A verified consumer must document and test:

- files considered;
- merge order;
- replace-versus-deep-merge behavior;
- environment substitution;
- unknown-key handling;
- missing-file behavior;
- type coercion;
- profile resolution;
- stale/deprecated key behavior;
- logging/redaction;
- fallback and error outcomes.

### Fail safe

Missing or invalid config must not silently:

- infer legal status or place identity;
- broaden facility exposure;
- expose exact geometry;
- treat stale condition as current;
- create service guarantees;
- disable review or policy;
- publish or deploy;
- fall back to an unrestricted environment.

Use explicit inactive, HOLD, DENY, ABSTAIN, or ERROR behavior.

---

## Place identity, legal status, and object boundaries

Configuration must preserve these distinctions:

| Object | Must remain distinct from |
|---|---|
| `Settlement` | legal municipality, census place, infrastructure asset, map label |
| `Municipality` | census place, named settlement, postal place, inferred jurisdiction |
| `CensusPlace` | incorporation/legal authority, municipality, service area |
| `Townsite` | current municipality, parcel, settlement continuity |
| `GhostTown` | abandoned property, folklore, current jurisdiction |
| `Fort` | archaeology site, active military facility, tourist site, settlement |
| `Mission` | current institution, archaeology site, culturally cleared public location |
| `ReservationCommunity` | tribal authority, reservation boundary, census geography, public-access permission |
| `Facility` | settlement, legal jurisdiction, service guarantee |
| `ServiceArea` | ownership, legal jurisdiction, access, guaranteed service |
| `Operator` | owner, regulator, current service provider, legal authority |
| `ConditionObservation` | enduring asset status, official alert, service availability |
| `Dependency` | proven causal/operational dependency or public-safe relationship |

Rules:

- names are labels/assertions, not identity by themselves;
- geometry is not identity or legal boundary;
- census geography is not municipal status;
- legal status needs source-specific authority, event/time scope, evidence, and review;
- historic and present place identities must not be collapsed by name similarity;
- a config may reference an accepted identity profile but cannot define the winning record.

---

## Source role and knowledge character

Source role is fixed at admission and must remain visible through config selection and downstream transformation.

At minimum, config must not collapse:

- observed or first-hand records;
- regulatory/legal determinations;
- administrative compilations;
- modeled or inferred outputs;
- aggregates/statistical geographies;
- candidates awaiting review;
- synthetic/reconstructed interpretations;
- context-only or restricted material where accepted vocabulary uses those terms.

High-risk failures:

| Failure | Required response |
|---|---|
| Census geography treated as municipal/legal status | `DENY` / validation failure |
| Facility roster treated as observed condition | `DENY` / validation failure |
| Operator directory treated as current service guarantee | `DENY` / `ABSTAIN` |
| Historical map treated as current boundary | `ABSTAIN` / stale-state hold |
| Modeled service area treated as entitlement | `DENY` |
| Candidate place merge treated as canonical identity | `HOLD` / `ABSTAIN` |
| Synthetic dependency graph treated as operational truth | `DENY` |
| Map label or generated summary presented as evidence | `DENY` |

Because repository documents contain more than one role vocabulary, configuration must reference an accepted profile/version rather than invent local aliases.

---

## Time, freshness, and stale state

Keep time meanings separate where material:

| Time kind | Meaning |
|---|---|
| source/publication time | When the source record or edition was published. |
| observed time | When a condition or event was observed. |
| valid/effective time | When a legal status, boundary, service area, operator assignment, or restriction applies. |
| retrieval time | When KFM acquired the material. |
| processing/run time | When a consumer transformed or validated it. |
| review/release time | When reviewers approved a derivative/release. |
| correction/supersession/withdrawal time | When prior state changed or became invalid. |

Config may reference accepted freshness profiles but must not:

- replace an old source vintage with the current clock;
- hide stale or superseded status;
- treat missing valid time as current;
- treat a current map as proof of current legal or operational status;
- use a default freshness window to override source authority;
- keep caches/public surfaces active after withdrawal, correction, or rollback.

Operational or service-related context requires explicit stale-state behavior and official-source limits.

---

## Critical infrastructure, facilities, and dependencies

Critical infrastructure and sensitive facility context defaults to restricted review.

Configuration must never carry real:

- exact restricted facility locations;
- access routes, security zones, credentials, control systems, internal topology, vulnerabilities, or emergency procedures;
- operator-sensitive details;
- condition observations that reveal exploitable state;
- dependency chains that reveal critical failure paths;
- private endpoints or non-public service metadata.

A future public-safe configuration may reference accepted profile IDs for:

- generalization;
- clustering;
- aggregation;
- suppression;
- geometry withholding;
- zoom/display limits;
- delayed publication;
- staged access;
- review routing.

But configuration alone cannot decide:

- that an asset is non-sensitive;
- that clustering is sufficient;
- that exact geometry may be released;
- that service/dependency data is harmless;
- that a transform satisfied policy.

A public derivative needs policy decision, transformation/aggregation/redaction receipt, evidence, review state, release manifest, correction path, and rollback target.

---

## Geometry, service areas, access, and public-safe representation

Geometry can support representation and analysis. It does not prove:

- legal boundary;
- jurisdiction;
- ownership or title;
- access or public permission;
- service entitlement or availability;
- facility operation or safety;
- network connectivity or dependency completeness;
- emergency suitability.

Service areas and dependency graphs are often derived, modeled, administrative, or provider-specific. Config must preserve:

- method and source role;
- source vintage and valid time;
- uncertainty and coverage limits;
- rights and sensitivity;
- aggregation/generalization state;
- public-safe versus internal geometry;
- correction and supersession state.

Do not create a single `public: true` or `safe: true` switch that bypasses profile, policy, receipt, review, and release requirements.

---

## Historic, cultural, community, and sovereignty context

Townsites, ghost towns, forts, missions, reservation communities, historic neighborhoods, cultural places, and adjacent archaeology require bounded representation.

Config must not:

- infer exact location from uncertain historical evidence;
- convert a corridor, map symbol, oral history, or approximate point into precise site truth;
- expose sacred, burial, archaeological, or culturally restricted context;
- treat public-source availability as cultural permission;
- equate census/community geography with tribal, sovereign, or cultural authority;
- bypass rights-holder, tribal, family, institutional, or community review.

Accepted configuration may reference a reviewed uncertainty or cultural-access profile. It cannot grant permission or represent a community.

---

## Logging, telemetry, and observability

Allowed operational metadata may include:

- config file ID and version;
- consumer/version;
- schema/profile IDs;
- validation outcome and reason code;
- digest/hash;
- timing and retry metadata;
- release/correction/rollback references.

Do not log:

- secret values;
- private endpoints;
- exact restricted facility geometry;
- operator-sensitive details;
- condition/dependency payloads;
- private-property or living-person joins;
- cultural/archaeology-sensitive locations;
- unredacted source payloads.

Telemetry is not evidence, policy, or release authority. Logs must not become a shadow registry or sensitive data store.

---

## Failure behavior

| Condition | Required behavior |
|---|---|
| File missing | Explicit inactive/HOLD/ERROR per consumer contract; no permissive fallback. |
| Syntax/type/schema failure | `ERROR`; no partial activation. |
| Unknown key | Error or explicit bounded handling; never silent broadening. |
| Missing consumer/version | `HOLD`. |
| Unknown source role/rights | `ABSTAIN` or `DENY`; no fetch/use/publication. |
| Unresolved legal status/place identity | `ABSTAIN`; preserve competing assertions. |
| Stale/missing time | Mark stale/HOLD/ABSTAIN; never present as current. |
| Exact/reconstructable sensitive detail | `DENY`; remove/quarantine and assess exposure. |
| Missing exposure/cultural review profile | `DENY` / `ABSTAIN`. |
| Missing evidence | `ABSTAIN`. |
| Missing policy/release state | `DENY`. |
| Unresolved path/registry conflict | `HOLD`; do not write duplicate authority. |
| Validator/runtime exception | `ERROR`; failure is not permission. |

---

## Governed AI and generated language

AI may help interpret released, policy-safe Settlements/Infrastructure evidence. It is not root truth.

Configuration cannot authorize an AI system to:

- infer municipal/legal status;
- assert facility condition, service availability, dependency, access, or safety;
- reveal critical-asset or culturally sensitive detail;
- merge place identities without governed evidence;
- turn map geometry, graph edges, search results, or model output into facts;
- answer without resolving evidence, policy, sensitivity, review, and release state.

A governed AI consumer should retrieve released evidence, resolve `EvidenceRef` to `EvidenceBundle`, apply policy and sensitivity checks, preserve source role/time/uncertainty, and return a cited answer, bounded caveat, abstention, denial, or error.

---

## Migration and anti-bypass posture

If misplaced material is found here:

1. freeze activation and authority claims;
2. identify its true responsibility;
3. remove/quarantine secrets or protected details immediately;
4. preserve provenance, consumers, digests, and review state;
5. move meaning to contracts;
6. move shape to the accepted schema home;
7. move policy to accepted policy roots;
8. move source/rights/activation records to the accepted registry;
9. move lifecycle, receipt, proof, catalog, graph, and published objects to `data/`;
10. move release/correction/rollback decisions to `release/`;
11. move code to packages/pipelines/tools/apps/runtime/infra as appropriate;
12. update bindings, tests, docs, drift records, correction paths, and rollback;
13. remove compatibility config after the transition closes.

Anti-bypass rules:

- no `allow_all`, `public: true`, `skip_review`, `disable_redaction`, `assume_current`, or equivalent shortcut;
- no local alias to resolve `settlement`/`settlements-infrastructure` or policy/registry conflicts;
- no config-only municipal-status, service-availability, facility-exposure, or publication decision;
- no public client reading config as data;
- no watcher, model, graph, or pipeline publishing because a config exists.

---

## Rollback, correction, and deactivation

Rollback triggers include:

- secret/live binding introduced;
- exact or reconstructable protected detail committed;
- legal status or place identity inferred by config;
- stale status displayed as current;
- facility/service/dependency context overexposed;
- config begins acting as policy, registry, schema, evidence, lifecycle, or release authority;
- recursive discovery or permissive fallback activates behavior;
- path/registry conflicts create duplicate authority;
- public or downstream consumers depend on unsafe state.

Preferred response:

1. deactivate consumer binding;
2. remove/quarantine unsafe values;
3. rotate/revoke credentials if needed;
4. restore the prior reviewed file/blob;
5. invalidate caches, exports, generated explanations, and public derivatives when affected;
6. issue correction/withdrawal/rollback records through release governance;
7. move durable content to the owning root;
8. add tests/scanners/validators to prevent recurrence;
9. confirm downstream cleanup and rollback completion.

This revision's prior blob is recorded in the metadata for mechanical restoration.

---

## Definition of done for the first payload

Before the first non-README file is accepted:

- [ ] exact consumer and owner verified;
- [ ] config class, parser, binding, precedence, missing-file, unknown-key, and fallback behavior defined;
- [ ] accepted non-empty schema validates;
- [ ] contracts and policy/profile references verified;
- [ ] source IDs, roles, rights, cadence, attribution, and freshness verified;
- [ ] place identity and legal-status anti-inference tests pass;
- [ ] object-family separation tests pass;
- [ ] time/freshness/stale/supersession tests pass;
- [ ] critical-asset, condition, service-area, dependency, access, private-property, and operator-sensitive denial tests pass;
- [ ] cultural/sovereignty/archaeology and historic-overprecision tests pass;
- [ ] public-safe geometry/aggregation/redaction profile requires policy, receipt, review, and release;
- [ ] no secrets/private endpoints/restricted values;
- [ ] no-network parse/validation where practical;
- [ ] logging is redacted;
- [ ] no lifecycle/trust/catalog/graph/release objects stored here;
- [ ] consumer tests and negative states pass;
- [ ] reviewers approve;
- [ ] deactivation, correction, cache invalidation, and rollback are tested;
- [ ] documentation and evidence ledger updated.

---

## Verification backlog

| Item | Status |
|---|---:|
| Recursive config inventory | `NEEDS VERIFICATION` |
| Direct consumer/loader | `UNKNOWN` |
| Discovery/precedence/fallback | `UNKNOWN` |
| `settlements-infrastructure` vs `settlement` path resolution | `CONFLICTED` |
| Infrastructure sensitivity-policy path | `CONFLICTED / NEEDS VERIFICATION` |
| Registry topology | `CONFLICTED / NEEDS VERIFICATION` |
| Source-role vocabulary | `CONFLICTED / NEEDS VERIFICATION` |
| Package implementation | `PLACEHOLDER METADATA / NEEDS VERIFICATION` |
| Pipeline implementation | `PLACEHOLDER` |
| Pipeline specs | `EMPTY STAGE LISTS` |
| Policy completeness | `PROPOSED / INCOMPLETE` |
| Schema completeness | `PROPOSED STUBS` |
| Validators | `NOT IMPLEMENTED IN INSPECTED FILES` |
| Workflow enforcement | `TODO SCAFFOLD` |
| Executable tests/pass rates | `NEEDS VERIFICATION` |
| Consumer route/app wiring | `NEEDS VERIFICATION` |
| Source rights/endpoints/cadence | `NEEDS VERIFICATION` |
| Legal-status evidence profiles | `NEEDS VERIFICATION` |
| Identity/merge rules | `NEEDS VERIFICATION` |
| Freshness/stale budgets | `NEEDS VERIFICATION` |
| Critical-asset exposure profiles | `NEEDS VERIFICATION` |
| Service-area/dependency semantics | `NEEDS VERIFICATION` |
| Cultural/sovereignty review profiles | `NEEDS VERIFICATION` |
| Secret/sensitive scanners | `NEEDS VERIFICATION` |
| Ownership/branch protection | `NEEDS VERIFICATION` |
| Runtime/release/publication | `UNKNOWN` |

---

## Safe language rules

| Avoid | Prefer |
|---|---|
| “The pipeline uses this config.” | “This file names an intended consumer; direct binding is `NEEDS VERIFICATION`.” |
| “This is a municipality.” | “A source-attributed legal-status assertion supports this classification for a stated time.” |
| “The census boundary is the city boundary.” | “Census and municipal geographies remain distinct.” |
| “This facility is operational.” | “A cited time-bound source reports status; KFM provides no operational assurance.” |
| “Service is available here.” | “A source/method-specific service-area context is shown; availability and entitlement are not guaranteed.” |
| “This dependency is complete.” | “A derived, evidence-bounded dependency projection is shown.” |
| “This map proves access/ownership.” | “Geometry does not prove access, title, ownership, or legal boundary.” |
| “This asset is safe to publish.” | “An accepted policy, transform receipt, review, and release authorize a public-safe derivative.” |
| “Exact ghost-town/mission/fort location.” | “Evidence-backed interpretation with uncertainty and sensitivity review.” |
| “Schema is active.” | “Inspected schema is a `PROPOSED` stub until contracts, fixtures, validators, registry, and review close.” |
| “CI validates this domain.” | “The inspected workflow currently runs TODO echo jobs.” |

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Target README | prior blob `47a1b267…` | v0.1 boundary and rollback. | Consumers or payloads. |
| Parent config README | blob `2c5e8b70…`, v0.4 | Child-lane no-secret/no-authority contract. | Domain runtime behavior. |
| Bounded config search | README only | No indexed payload/direct consumer. | Exhaustive absence. |
| Domain README | blob `bccb04cd…` | Scope, object families, lifecycle, sensitivity, cross-lane doctrine. | Current implementation. |
| Canonical paths | blob `a388ccbf…` | Slug/path and policy variance. | Accepted ADR resolution. |
| Package README / pyproject | blobs `521d570b…`, `d4728c97…` | Intended package boundary; version `0.0.0`. | Working helpers. |
| Pipeline README | blob `333222ac…` | Intended executable boundary and alias warning. | Implemented processing. |
| Pipeline files | placeholder comments | Inspected entrypoints are greenfield placeholders. | All possible code elsewhere. |
| Pipeline specs | `stages: []` | Declarative paths exist. | Executable stage wiring. |
| Policy files | default-only proposed/stub rules | Policy paths exist with fail-closed intent. | Complete policy or runtime enforcement. |
| Schema README and domain observation schema | greenfield/proposed stub | Schema path and placeholder shape exist. | Meaningful field coverage or strict validation. |
| Validators | raise `NotImplementedError` | Paths exist. | Executable validation. |
| Domain workflow | TODO echo jobs | Trigger/job scaffolding exists. | Substantive CI/proof/release. |
| Tests README | domain test index; executable coverage unverified | Intended negative-state/no-network guardrails. | Passing tests. |
| Explorer feature README | README boundary confirmed | Intended public UI boundary. | Route/module/runtime implementation. |
| Registry README | domain-first path plus topology warning | Existing registry routing and conflict. | Canonical/active registry records. |

---

<details>
<summary><strong>Appendix A — no-loss preservation note</strong></summary>

v0.1 established the lane, non-authoritative scope, no secrets/live bindings, object-role separation, critical-asset sensitivity, and no operational/publication authority.

v0.2 preserves those controls and adds pinned evidence, bounded inventory, scaffold maturity, path/policy/registry/source-role conflicts, place/legal-status/object-family rules, critical-asset/facility/service/dependency safeguards, cultural and historical context, time/stale-state rules, configuration taxonomy and file contract, explicit binding, validation/review, migration, deactivation/correction/rollback, definition of done, backlog, safe language, and an evidence ledger.

</details>

<details>
<summary><strong>Appendix B — documentation-only boundary</strong></summary>

This revision changes no payload, consumer, loader, source record, schema, contract, policy, code, validator, test, fixture, workflow, lifecycle/trust/catalog/graph/release object, map/API/UI surface, municipal status, facility status, service behavior, emergency operation, or deployment.

</details>

## Status summary

`configs/domains/settlements-infrastructure/` is a README-only, non-secret, non-authoritative configuration-support lane. The surrounding repository contains extensive documentation and many implementation-shaped paths, but the inspected package, pipeline, spec, policy, schema, validator, test, workflow, app, and registry surfaces remain draft, scaffolded, placeholder, conflicted, or unverified. No direct config consumer is established. Future payloads require explicit binding, accepted authority references, place/legal-status anti-inference, source-role/time/stale preservation, critical-asset and cultural safeguards, validation, review, policy, release, correction, and rollback.

<p align="right"><a href="#top">Back to top</a></p>
