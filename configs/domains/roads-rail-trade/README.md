<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-roads-rail-trade-readme
title: configs/domains/roads-rail-trade/ — Roads, Rail, Trade, and Mobility Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Roads/Rail/Trade steward · Roads steward · Rail steward · Historic/Trade Routes steward · Infrastructure/sensitivity reviewer · Source steward · Consumer owner · Validation steward · Policy steward · Release steward · Docs steward
created: 2026-07-13
updated: 2026-07-14
policy_label: "public; config-sublane; roads-rail-trade; transport; mobility; source-role-aware; time-aware; infrastructure-aware; historic-route-uncertainty-aware; non-secret; non-authoritative; no-live-binding; not-navigation; not-legal-access; not-current-condition-authority; no-release-authority"
current_path: configs/domains/roads-rail-trade/README.md
truth_posture: CONFIRMED canonical roads-rail-trade config lane, parent config contract, repository-present domain doctrine and implementation-shaped surfaces, README-only bounded config inventory, scaffold status of inspected pipeline/policy/schema/validator/workflow files, unresolved roads-rail-trade versus transport naming and registry topology, and prior README lineage / PROPOSED future consumer-bound templates and profile references / UNKNOWN consumers, loader behavior, precedence, deployment binding, complete recursive inventory, and runtime/publication use / NEEDS VERIFICATION accepted owners, authority paths, source-role vocabulary, source rights, freshness budgets, sensitivity rules, historic-route thresholds, graph validation, executable config validation, scanners, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 154d3a87f908fd8c21086dba0607558912e560db
  prior_blob: 61d17d3c283970be99d972e93aaa01536b55754b
  bounded_path_search: configs/domains/roads-rail-trade/README.md only
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
  - ../../../contracts/domains/roads-rail-trade/
  - ../../../contracts/transport/
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../schemas/contracts/v1/domains/transport/
  - ../../../schemas/contracts/v1/transport/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../data/registry/sources/roads-rail-trade/
  - ../../../data/registry/roads-rail-trade/
  - ../../../packages/domains/roads-rail-trade/
  - ../../../pipelines/domains/roads-rail-trade/
  - ../../../pipeline_specs/roads-rail-trade/
  - ../../../tools/validators/domains/roads-rail-trade/
  - ../../../tests/domains/roads-rail-trade/
  - ../../../fixtures/domains/roads-rail-trade/
  - ../../../data/raw/roads-rail-trade/
  - ../../../data/work/roads-rail-trade/
  - ../../../data/quarantine/roads-rail-trade/
  - ../../../data/processed/roads-rail-trade/
  - ../../../data/catalog/domain/roads-rail-trade/
  - ../../../data/triplets/roads-rail-trade/
  - ../../../data/published/layers/roads-rail-trade/
  - ../../../data/receipts/roads-rail-trade/
  - ../../../data/proofs/roads-rail-trade/
  - ../../../release/candidates/roads-rail-trade/
  - ../../../release/manifests/roads-rail-trade/
  - ../../../docs/runbooks/roads-rail-trade/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/roads-rail-trade/ROLLBACK_RUNBOOK.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
tags: [kfm, configs, roads, rail, trade-routes, historic-routes, transport, mobility, corridors, graph-projection, source-role, time, uncertainty, sensitivity, infrastructure, no-secrets, not-navigation, governance]
notes:
  - "The bounded repository search for configs/domains/roads-rail-trade returned this README only. No executable config payload or indexed direct consumer was found."
  - "The surrounding domain has many documentation and implementation-shaped surfaces, but inspected pipeline, policy, schema, validator, and workflow files are PROPOSED, empty-permissive, NotImplemented, TODO-only, or otherwise not proof of production behavior."
  - "Repository evidence contains competing roads-rail-trade and transport schema/contract paths and domain-first versus subtype-first source-registry paths. This lane does not resolve, alias, or duplicate those conflicts."
  - "Configuration may reference an accepted source, temporal, uncertainty, graph, public-safe display, or review profile. It cannot create source authority, current-condition truth, legal access, routing advice, operational instructions, policy, evidence, release, or publication state."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, Trade, and Mobility Domain Configuration

`configs/domains/roads-rail-trade/`

> Safe-to-commit configuration documentation and future consumer-bound templates for roads, rail, historic routes, trade corridors, crossings, facilities, restrictions, and derived transport-network products. This lane is not navigation, traffic control, railroad operations, legal-access authority, current-condition authority, source authority, or release authority.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-config__sublane-green)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![operations](https://img.shields.io/badge/operations-NOT__AUTHORIZED-red)
![secrets](https://img.shields.io/badge/secrets-forbidden-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs-and-drift-triggers) · [Last reviewed](#last-reviewed) · [Scope](#scope-and-bounded-context) · [Contract](#minimum-configuration-contract) · [Binding](#consumer-binding-precedence-and-discovery) · [Roles](#source-role-and-knowledge-character) · [Time](#time-freshness-and-stale-state) · [Routes](#route-designation-membership-and-identity) · [Operations](#restrictions-status-and-operational-context) · [Historic routes](#historic-and-trade-route-uncertainty) · [Graph](#network-topology-and-graph-projection) · [Geometry](#geometry-access-and-public-safe-representation) · [Failure](#failure-behavior) · [AI](#governed-ai-and-generated-language) · [Migration](#migration-and-anti-bypass-posture) · [Rollback](#rollback-correction-and-deactivation) · [Done](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Observed lane maturity:** README-only in the bounded path search; no executable configuration payload or direct consumer binding is established  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for transport truth, operational status, access, routing, policy, evidence, or release  
> **Runtime posture:** no loader, precedence rule, source activation, network fetch, graph build, operational feed, route instruction, public layer, release, or publication is established by this README

> [!CAUTION]
> KFM transportation context is evidence and governed publication material—not turn-by-turn navigation, dispatch, traffic control, emergency routing, legal access advice, railroad operating instructions, or a guarantee that a road, rail line, bridge, crossing, ferry, facility, route, or corridor is open, safe, passable, lawful, current, or complete.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical `roads-rail-trade` domain segment under `configs/domains/`.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should parse, validate, select, compare, generalize, render, or package already-governed material, but they cannot decide:

- whether a road, rail line, crossing, bridge, ferry, depot, siding, yard, corridor, or facility exists;
- whether geometry is accurate, current, connected, passable, public, or legally accessible;
- whether a route designation, route membership, operator assignment, restriction, closure, or condition is official or current;
- whether an administrative roster is an observed event;
- whether a modeled, inferred, reconstructed, candidate, synthetic, or graph-projected route is source truth;
- whether a historic route or trade corridor follows a precise alignment;
- whether private roads, railroad property, rights-of-way, facilities, or restricted corridors may be accessed;
- whether sensitive infrastructure, cultural corridors, archaeological context, or operational detail may be exposed;
- whether evidence supports a claim;
- whether a source is admitted, active, licensed, or redistributable;
- whether an artifact may be promoted, released, or published.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Domain and object meaning | **None.** Configuration may reference doctrine/contracts; it cannot define them. |
| Machine shape | **None.** Configuration may reference accepted schemas; it cannot repair or duplicate schema authority. |
| Path/slug authority | **None.** It cannot resolve `roads-rail-trade` versus `transport`, `domains/` versus flat homes, or registry topology. |
| Source identity, role, rights, cadence, activation | **None.** These require registry, connector, rights, policy, and steward decisions. |
| Current condition and status | **None.** A value cannot make a closure, restriction, operator status, or facility condition official/current. |
| Route designation and membership | **None.** Labels, filters, geometry, or source preference cannot establish designation, membership, ownership, or right-of-way. |
| Navigation and routing | **None.** No operational route recommendations, dispatch, evacuation, or access advice. |
| Railroad operations | **None.** No train movement, switching, signal, warrant, schedule, or safe-working authority. |
| Legal access | **None.** Geometry or admin data cannot establish permission to enter, cross, travel, or use. |
| Historic-route interpretation | **None.** Thresholds cannot turn reconstruction or plausibility into observed alignment. |
| Graph/topology | **None.** Derived edges are not canonical or operational routes. |
| Policy/sensitivity | **None.** A setting may reference an accepted profile; it cannot create or waive policy. |
| Evidence/release | **None.** Configuration cannot create evidence closure, promotion, public display, or rollback completion. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file through explicit binding and tested precedence. |

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
| Base commit | `154d3a87f908fd8c21086dba0607558912e560db` |
| Prior README blob | `61d17d3c283970be99d972e93aaa01536b55754b` |
| Bounded config-path search | `configs/domains/roads-rail-trade/README.md` only |

### Maturity matrix

| Item | State | Safe conclusion |
|---|---:|---|
| Config lane | **CONFIRMED** | The path exists and inherits the parent domain-config contract. |
| Current config content | **README ONLY IN BOUNDED SEARCH** | No executable payload or indexed direct consumer was found. |
| Domain documentation | **CONFIRMED REPOSITORY-PRESENT** | Domain, object, source, architecture, lifecycle, path, UI/API, and backlog documents exist. |
| Semantic contracts | **CONFIRMED / PATH-CONFLICTED** | `contracts/domains/roads-rail-trade/` files exist; `transport` variants also exist. |
| Schemas | **CONFIRMED SCAFFOLDS / PATH-CONFLICTED** | Inspected schema files are empty-permissive `PROPOSED` scaffolds; competing `transport` paths exist. |
| Policy | **CONFIRMED SCAFFOLD** | Inspected `source_role.rego` is default-deny and `PROPOSED`, not proof of complete enforcement. |
| Pipelines | **CONFIRMED PLACEHOLDERS** | Inspected generic and source-specific ingest files are greenfield/PROPOSED placeholders. |
| Validator | **NOT IMPLEMENTED IN INSPECTED FILE** | `validate_schema.py` raises `NotImplementedError`. |
| Workflow | **TODO SCAFFOLD** | Domain workflow uses TODO echo steps for validation, proof, and publish dry-run. |
| Source registry | **DOCUMENTED / TOPOLOGY-CONFLICTED** | Domain-first and subtype-first registry surfaces exist; canonical topology is unresolved. |
| Loader/precedence | **UNKNOWN** | No parser, discovery, merge, unknown-key, or fallback behavior is established. |
| Source-role vocabulary | **NEEDS VERIFICATION** | Human docs use seven roles; some registry text also names extensions. |
| Source rights/terms | **NEEDS VERIFICATION** | License, access, redistribution, cadence, endpoint, and authority limits require source records. |
| Operational freshness | **NEEDS VERIFICATION** | Freshness budgets and stale-state rules are not established by this lane. |
| Owners/CODEOWNERS | **OWNER_TBD** | Effective path ownership is not proven here. |
| Runtime/release/publication | **NOT ESTABLISHED** | Nothing authorizes loading, operational use, public display, release, or publication. |

Repository surface presence is not implementation maturity:

```text
docs + contracts + scaffold schemas/policy/pipelines/validator/workflow
≠ verified config consumer
≠ current operational authority
≠ released public product
```

[Back to top](#top)

---

## What belongs here

| Accepted material | Purpose | Required posture |
|---|---|---|
| `README.md` | Boundary, evidence state, review, and rollback. | Truth-labeled and current. |
| `*.template.yaml` / `*.example.json` / `*.example.toml` | Safe template/example for a named consumer. | Parseable, synthetic, non-secret, no implicit activation. |
| Source-profile references | Select already-admitted sources. | Reference IDs only; no source admission. |
| Source-role display/filter defaults | Preserve already-governed roles. | No relabeling/upgrading. |
| Temporal/stale-state profile references | Configure display/processing of governed time metadata. | Cannot assert current status. |
| Historic-route uncertainty profile references | Select accepted confidence/generalization behavior. | Cannot manufacture precision. |
| Graph-projection profile references | Configure derived analytical graph behavior. | Non-canonical, non-operational. |
| Public-safe display profile references | Select accepted release-facing representation behavior. | Policy, receipt, review, release, correction, rollback still required. |
| Conservative review defaults | Hold, abstain, warning, caveat, steward routing. | Cannot waive governance. |
| Compatibility notes | Time-bounded key/path migration. | Owner, sunset, tests, and rollback required. |

[Back to top](#top)

---

## What does NOT belong here

| Prohibited material | Why | Correct home/action |
|---|---|---|
| Credentials, cookies, private keys, signed URLs, service accounts | Repo is not a secret store. | External secret/deployment mechanism; rotate if exposed. |
| Private endpoints, internal hosts, connection strings, personal paths | Operational disclosure/non-portability. | Deployment controls or ignored local overrides. |
| Live traffic, WZDx, KanDrive, closure, condition, incident, rail-operation, or dispatch payloads | Config is not source/lifecycle data or operational authority. | Connectors and governed lifecycle lanes. |
| Track charts, signal layouts, train orders, switching/warrant instructions | Sensitive railroad-operating material. | Restricted official operational authority. |
| Critical-infrastructure vulnerabilities or restricted facility/access detail | Harmful exposure risk. | Restricted lifecycle/policy/review lanes; generalize/stage/deny. |
| Private-road permissions, access codes, easement detail, legal-entry conclusions | Geometry/admin data do not prove access. | Authoritative legal/land/access sources and review. |
| Exact protected cultural/archaeological route locations | Sensitivity and false-precision risk. | Owning domain/rights-holder review/generalization/denial. |
| SourceDescriptor, activation, rights, cadence, sensitivity, registry records | Config cannot admit sources. | Accepted registry/control-plane homes. |
| Road/rail/route/facility/restriction/status/operator records | Config is not domain data. | `data/<phase>/roads-rail-trade/`. |
| Route geometry, graph edges, adjacency, path caches, routing tables | Data/derived artifacts, not defaults. | Processed/catalog/triplet/published/artifact homes. |
| Contracts, schemas, policy, validators, pipeline/package code | Separate authority/implementation roots. | Their owning roots. |
| Fixtures/tests, receipts/proofs, release objects, map/tile/export artifacts | Config cannot prove or publish itself. | `fixtures/`, `tests/`, `data/`, `release/`, published/artifact roots. |
| Navigation, evacuation, dispatch, legal access, bridge compliance, railroad operation advice | KFM is not the responsible authority. | Official agency/operator. |
| AI route narratives presented as fact | Generated language is interpretive. | Governed AI with citations/outcomes/receipts. |

[Back to top](#top)

---

## Inputs

Before a non-README payload is added, identify:

1. exact consumer path and owner;
2. config class/environment;
3. parser and version;
4. accepted schema and contract refs;
5. source registry/profile refs;
6. source-role vocabulary/version;
7. temporal and stale-state behavior;
8. uncertainty/graph/public-safe profiles;
9. rights, sensitivity, and legal/operational boundaries;
10. network and side effects;
11. validation command/fixtures;
12. override mechanism;
13. logging/redaction;
14. migration/deactivation/rollback.

Reject input containing credentials, live feeds, source payloads, restricted operational details, exact protected locations, legal/access conclusions, graph/geometry data disguised as config, or bypass instructions.

[Back to top](#top)

---

## Outputs

This lane may support consumers through safe defaults, templates, profile references, conservative time/stale-state behavior, governed uncertainty/generalization selections, derived-graph parameters, review defaults, and migration notes.

It does **not** emit or authorize source activation, fetches, lifecycle records, current-condition claims, access/status decisions, canonical topology, navigation, EvidenceBundles, receipts, proofs, catalogs, triplets, release, public maps/APIs/exports, or AI answers.

[Back to top](#top)

---

## Validation

No executable config validator was verified. The inspected domain validator is unimplemented, the workflow is TODO-only, and inspected schema/policy/pipeline files are scaffolds.

| Check | Required outcome | Current posture |
|---|---|---|
| Syntax | Parses under declared format/version. | `NEEDS VERIFICATION`. |
| Schema | Accepted non-empty schema validates payload. | Blocked/needs verification; inspected schemas are empty-permissive scaffolds. |
| Known keys | Unknown/misspelled keys fail or are surfaced. | `UNKNOWN`. |
| Consumer compatibility | Exact consumer loads exact path/version. | `UNKNOWN`; no direct consumer found. |
| Explicit binding | Folder presence never activates loading. | Required. |
| Source refs | Profiles exist, are active for use, and carry role/rights/cadence/sensitivity. | `NEEDS VERIFICATION`. |
| Role anti-collapse | Roles/knowledge character remain distinct. | Required; vocabulary mapping open. |
| Temporal/freshness | Time axes and stale behavior are explicit. | Required; budgets need verification. |
| Designation/membership | Config cannot create designation, membership, ownership, or legal status. | Required. |
| Operational status | Stale/cached context cannot become current instruction. | Required. |
| Historic uncertainty | Method, confidence, alternatives, and overprecision controls preserved. | Required. |
| Graph | Edges remain derived, evidence-linked, non-canonical, non-operational. | Required. |
| Geometry/access | Geometry cannot prove access, safety, passability, ownership, or right-of-way. | Required. |
| Sensitivity/rights | No restricted infrastructure, cultural, private, or rights-conflicted detail. | Required; enforcement needs verification. |
| Secrets/private endpoints | None present. | Required; scanning coverage needs verification. |
| No side effect/network | Parse/validation does not fetch, write, publish, or deploy. | Required. |
| Lifecycle isolation | No data/registry/receipt/proof/catalog/release objects stored here. | Manual check. |
| Docs/staleness | Links resolve; owner/refs/review dates current. | Manual until substantive CI. |

Configuration-review outcomes: `PASS`, `HOLD`, `DENY`, or `ERROR`. `PASS` is not source activation or publication approval.

The inspected domain workflow triggers on PR/push and uses GitHub-hosted runners, but its jobs currently echo TODO commands. It does not prove substantive validation or release readiness.

[Back to top](#top)

---

## Review burden

| Change | Minimum review |
|---|---|
| README clarification | Config/docs + domain reviewer. |
| First payload | Config steward + exact consumer + domain + validation. |
| Source-profile setting | Add source, rights, policy reviewers. |
| Current condition/restriction/operator/access field | Add freshness, operational-context, legal/access, security, policy, release review. |
| Rail-operation/facility detail | Add rail and infrastructure/security review; operating instructions remain prohibited. |
| Historic/trade route uncertainty/geometry | Add historical, archaeology/cultural-rights, evidence, sensitivity, public-safe geometry review. |
| Graph/topology parameters | Add network/graph review; operational routing remains prohibited. |
| Public-safe display/generalization | Add policy, sensitivity, evidence, release, UI/map review. |
| Schema/path/registry authority change | ADR and authority-root reviewers; not config-only. |

Until path-specific CODEOWNERS and steward acceptance are verified, name reviewers explicitly.

[Back to top](#top)

---

## Related folders

| Responsibility | Surface | Posture |
|---|---|---|
| Parent config | [`../README.md`](../README.md) | Safe, non-secret, non-authoritative parent contract. |
| Domain doctrine | [`../../../docs/domains/roads-rail-trade/README.md`](../../../docs/domains/roads-rail-trade/README.md) | Scope, non-ownership, path, sensitivity, release posture. |
| Objects/sources | `OBJECT_FAMILIES.md`, `SOURCES.md` | Vocabulary and source-role controls. |
| Contracts | `contracts/domains/roads-rail-trade/` plus `transport` variants | Repository-present; canonical topology conflicted. |
| Schemas | `schemas/contracts/v1/domains/roads-rail-trade/` plus `transport` variants | Repository-present scaffolds; authority conflicted. |
| Policy | `policy/domains/roads-rail-trade/` | Repository-present scaffolds; not complete enforcement. |
| Source registry | subtype-first and domain-first paths | Topology unresolved; no duplicate authority. |
| Package/pipeline | `packages/domains/roads-rail-trade/`, `pipelines/domains/roads-rail-trade/` | Intended implementation support; inspected pipeline code is placeholder. |
| Validator/workflow | validator path and domain workflow | Validator unimplemented; workflow TODO-only. |
| Lifecycle | `data/{raw,work,quarantine,processed}/roads-rail-trade/` | Data, never config. |
| Catalog/triplet/published | domain catalog, triplets, published layers | Downstream carriers after gates. |
| Receipts/proofs/release | data trust-object lanes and release lanes | Audit/evidence/release authority. |
| Runbooks | promotion and rollback runbooks | Operating guidance. |
| Security | secrets and incident docs | Real values stay outside repo. |

[Back to top](#top)

---

## ADRs and drift triggers

Configuration cannot resolve these open conflicts:

- `roads-rail-trade` versus `transport`;
- `contracts/domains/...` versus flat/alternate contract paths;
- `schemas/contracts/v1/domains/...` versus flat/alternate schema paths;
- domain-first versus subtype-first source registry;
- seven canonical source roles versus repository extensions;
- recursive config discovery and precedence;
- operational/current-status use;
- graph/routing use;
- historic-route precision/sensitivity posture.

Require ADR or accepted governance for authority/path changes, source-role changes, operational use, routing/navigation, sensitive-infrastructure posture, historic-route precision, graph public surfaces, or domain rehoming.

[Back to top](#top)

---

## Last reviewed

**2026-07-14**, against `main@154d3a87f908fd8c21086dba0607558912e560db`.

Review before the first payload/consumer, live-feed/profile reference, operational-status field, historic-route profile, graph/routing setting, public-safe representation, path/registry resolution, source-role change, or after six months.

[Back to top](#top)

---

## Scope and bounded context

In-scope knowledge families include road/rail segments, route/corridor membership, crossings/bridges/ferries/facilities, restrictions/status/operator context, historic/trade routes, freight/mobility corridors, derived nodes/edges, and release-facing display support.

Key terms:

| Term | Meaning |
|---|---|
| domain config | Safe parameters for a named consumer; never transport truth. |
| source profile | Reference to governed source identity/role/rights/cadence/activation. |
| route designation | Authority-bound assertion, not inferred from geometry/labels. |
| route membership | Time/source-bound segment-to-route assertion. |
| restriction/status event | Time-bound context requiring authority/freshness for current use. |
| historic route claim | Evidence-backed interpretation/hypothesis, not observed continuous alignment. |
| uncertainty profile | Accepted representation of confidence/support/corridor width/overprecision. |
| graph projection | Derived analytical representation, not canonical or operational routing. |
| public-safe profile | Accepted generalization/redaction/display reference, not approval. |
| stale state | Explicit state when freshness is not satisfied. |
| binding | Reviewed code/deployment wiring selecting an exact file. |

---

## Minimum configuration contract

A future payload should declare:

- `domain_slug`;
- `config_class`;
- `intended_consumer` and version;
- format/parser;
- exact authority refs;
- source-profile refs;
- source-role vocabulary/version;
- object-family scope;
- temporal/freshness/stale profile;
- uncertainty/graph/public-safe profile refs;
- `operational_use: false` unless separately accepted;
- network behavior and side effects;
- secret/sensitivity posture;
- validation ref;
- override mechanism;
- owner/review date;
- deprecation/rollback.

A universal machine envelope is **PROPOSED**, not created here.

---

## Consumer binding, precedence, and discovery

Consumers must explicitly bind an exact file. No recursive loading, filename activation, or directory-presence discovery.

Precedence is not defined here. Consumers must test file selection, merge semantics, environment substitution, types, unknown keys, missing files, reference resolution, fallback, logging, and redaction.

Failure must not silently activate sources, keep stale feeds current, broaden geometry/access, erase historic uncertainty, make graphs canonical, disable review, publish, or produce route/access advice.

---

## Source role and knowledge character

Human docs identify:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

Some registry text also names extensions such as context/restricted. Mapping remains `NEEDS VERIFICATION`. Config must not invent aliases or upgrade/downgrade roles.

High-risk collapses:

- agency roster → observed event;
- regulatory designation → complete physical/access truth;
- work-zone feed → permanent history or navigation guarantee;
- community geometry → legal designation/access;
- historic evidence → exact alignment;
- reconstructed route → observation;
- graph edge → canonical/routable network;
- AI narrative → evidence.

---

## Time, freshness, and stale state

Keep source, observed, valid/effective, retrieval, run, review, release, correction/withdrawal, and supersession times distinct.

Current-condition use requires admitted source authority, timestamps, cadence, freshness budget, stale transition, authority limit, disclaimer, no permissive fallback, and release state.

When stale, show stale/unavailable context or abstain—never preserve cached state as current.

---

## Route designation, membership, and identity

Preserve physical segment, source ID, route designation, corridor identity, membership, jurisdiction, operator/owner assertion, status, historic designation, graph identity, and public feature ID as distinct concepts.

Identity is not geometry. Geometry similarity cannot merge records across sources, roles, vintages, object families, time, methods, uncertainty, or release states.

Route membership is an evidence/time/authority assertion; config/style cannot create it.

---

## Restrictions, status, and operational context

Preserve event versus roster character, effective interval, source authority, freshness, location support, reason/scope, status, and official redirect.

This lane cannot authorize navigation, evacuation, dispatch, bridge compliance, train movement/switching, legal access, or declarations that a route/facility is open, closed, safe, or passable.

---

## Historic and trade route uncertainty

Historic routes may combine maps, texts, archaeology, place names, land records, landscape evidence, and interpretation.

An accepted profile may reference method, sources/vintage, confidence, corridor width, alternatives, interpolation, reviewer, reality-boundary note, overprecision threshold, sensitivity, correction, and supersession.

Config must not convert corridors to exact lines without evidence, hide alternatives/reconstruction, expose protected locations, use plausibility as proof, or make AI/Story Nodes canonical.

---

## Network topology and graph projection

A graph config may describe eligible families, direction, snap tolerance, temporal slice, role allowlist, confidence, uncertainty, restriction inclusion, disconnected handling, evidence refs, and public-safe profile.

It cannot make graph edges canonical, infer legal access/current passability/ownership, create public operational routes, or bypass evidence/policy/review/release.

---

## Geometry, access, and public-safe representation

Geometry does not prove public access, permission, ownership, safety, passability, operational status, legal boundary, designation, or current existence.

Public-safe derivatives may require role preservation, rights, stale-state, infrastructure/private-property/cultural review, uncertainty, generalization receipt, EvidenceBundle, release manifest, correction, and rollback.

Do not expose more precision than evidence, rights, sensitivity, and use support.

---

## Failure behavior

| Condition | Required response |
|---|---|
| Missing/invalid config | Safe inactive state; no permissive fallback. |
| Unknown key | Error or explicitly reviewed handling. |
| Missing source profile/role | Hold or deny; no guessing/fetch. |
| Unresolved rights/sensitivity | Deny exposure; quarantine/hold. |
| Stale operational context | Mark stale/unavailable; abstain from current claims. |
| Missing time metadata | No current/time-bound assertion. |
| Missing uncertainty profile | Hold/generalize/abstain. |
| Missing graph evidence/receipt | No authoritative/routable graph exposure. |
| Missing release/public-safe state | No public layer/export/answer. |
| Secret/sensitive value | Deny, remove/quarantine, incident response. |
| Authority-path conflict | Hold; no local alias resolution. |
| Validator unavailable | Fail closed for consequential use. |

---

## Governed AI and generated language

AI may explain released, policy-safe, citation-resolved evidence. It may not determine exact route truth, current closure/access/safety, operational navigation, legal access/right-of-way, missing route segments, graph truth, or expose sensitive infrastructure/cultural detail.

Config may reference an accepted AI profile; it cannot waive finite outcomes, citations, policy checks, or receipts.

---

## Migration and anti-bypass posture

Misplaced material must be frozen, classified, removed/quarantined if sensitive, and moved to its owning root with provenance, consumer updates, tests, compatibility only when time-bounded, drift/correction notes, and rollback.

Reject config that:

- embeds live feed/source data;
- activates sources without registry;
- relabels roles;
- declares cached state current;
- turns geometry into access;
- creates designation/membership;
- makes a graph routable by default;
- removes historic uncertainty;
- bypasses sensitivity/release;
- is read directly by public clients;
- stores generated outputs;
- aliases away authority conflicts.

---

## Rollback, correction, and deactivation

Rollback triggers include secret/live binding, source/operational authority, navigation/access/rail instructions, schema/contract/policy authority, route/graph data storage, lifecycle/trust/release storage, suppression of role/time/uncertainty/sensitivity, parallel authority aliases, or public-client reads.

Correction path:

1. deactivate consumer binding;
2. remove/quarantine unsafe content;
3. rotate credentials if needed;
4. restore prior blob;
5. move material to owning root;
6. record drift/migration/correction;
7. invalidate consequential caches/derivatives;
8. update tests/validators;
9. verify no public/released dependency remains.

---

## Definition of done for the first payload

- [ ] exact consumer/owner verified;
- [ ] class/parser/binding/precedence defined;
- [ ] unknown/missing behavior fail-safe;
- [ ] accepted non-empty schema validates;
- [ ] contracts referenced;
- [ ] source profiles/rights/cadence/sensitivity verified;
- [ ] role vocabulary accepted/tested;
- [ ] time/freshness/stale/supersession tested;
- [ ] designation/membership cannot be config-created;
- [ ] historic uncertainty/overprecision tested;
- [ ] graph remains derived/non-operational;
- [ ] geometry cannot imply access/safety/passability;
- [ ] no secrets/private endpoints/restricted operational detail/protected locations;
- [ ] no-network validation where practical;
- [ ] logging redacted;
- [ ] no lifecycle/trust/catalog/release objects stored here;
- [ ] reviewers approve;
- [ ] deactivation/correction/rollback tested;
- [ ] docs/evidence ledger updated.

---

## Verification backlog

| Item | Status |
|---|---:|
| Recursive config inventory | `NEEDS VERIFICATION` |
| Direct consumer/loader | `UNKNOWN` |
| Precedence/discovery | `UNKNOWN` |
| Canonical schema/contract path | `CONFLICTED` |
| Schema completeness | `NEEDS VERIFICATION` |
| Policy completeness | `NEEDS VERIFICATION` |
| Pipeline implementation | `NEEDS VERIFICATION` |
| Validator | `NOT IMPLEMENTED IN INSPECTED FILE` |
| Workflow enforcement | `TODO SCAFFOLD` |
| Registry topology | `CONFLICTED` |
| Source-role vocabulary | `NEEDS VERIFICATION` |
| Source rights/endpoints | `NEEDS VERIFICATION` |
| Freshness budgets | `NEEDS VERIFICATION` |
| Legal/access disclaimers | `NEEDS VERIFICATION` |
| Infrastructure sensitivity rules | `NEEDS VERIFICATION` |
| Historic precision profiles | `NEEDS VERIFICATION` |
| Graph/topology validation | `NEEDS VERIFICATION` |
| Secret/sensitive scanners | `NEEDS VERIFICATION` |
| Ownership/branch protection | `NEEDS VERIFICATION` |
| Runtime/release/publication | `UNKNOWN` |

---

## Safe language rules

| Avoid | Prefer |
|---|---|
| “The pipeline uses this config.” | “Intended consumer; direct binding is `NEEDS VERIFICATION`.” |
| “This is the current closure.” | “Cited time-bound context; freshness/authority require verification.” |
| “This road is open/safe.” | “KFM provides no operational assurance; consult official authority.” |
| “This route is public.” | “Geometry does not prove access or permission.” |
| “Exact historic route.” | “Evidence-backed interpretation with uncertainty/alternatives.” |
| “Graph proves connectivity.” | “Derived analytical projection over cited inputs.” |
| “Schema is active.” | “Inspected schema is a `PROPOSED` scaffold.” |
| “CI validates the domain.” | “Inspected workflow is TODO-only.” |
| “Transport is canonical.” | “Path authority is conflicted.” |

---

## Evidence ledger

| Evidence | State | Supports | Does not prove |
|---|---|---|---|
| Target README | prior blob `61d17d3c…` | v0.1 boundary/rollback. | Consumers/payloads. |
| Parent README | blob `2c5e8b70…`, v0.4 | Parent contract. | Domain behavior. |
| Bounded config search | README only | No indexed payload/direct consumer. | Exhaustive absence. |
| Domain README | blob `b4e2d45f…` | Scope/non-ownership/path conflict. | Runtime. |
| Object families | blob `64e64d79…` | Vocabulary/identity/time/roles. | Schemas. |
| Sources | blob `c47861f0…` | Source-family/anti-collapse posture. | Current terms/activation. |
| Package/pipeline READMEs | blobs `9128920c…`, `8753ddce…` | Intended boundaries. | Working code. |
| Inspected ingest files | placeholder text | Not implemented there. | All pipeline files. |
| `source_role.rego` | default-deny PROPOSED scaffold | Policy path exists. | Complete policy. |
| Schema index/files | slug-conflicted; empty-permissive PROPOSED scaffolds | Paths/files exist. | Meaningful validation. |
| Validator | raises `NotImplementedError` | Path exists, implementation absent. | Other validators. |
| Workflow | TODO echo jobs | Trigger/job scaffolding. | Substantive CI/release. |
| Source registry README | topology unresolved | Multiple registry patterns documented. | Canonical/active registry. |

---

<details>
<summary><strong>Appendix A — no-loss preservation note</strong></summary>

v0.1 established the lane, non-authoritative scope, no secrets/live bindings, role separation, infrastructure sensitivity, and no operational routing/publication authority.

v0.2 preserves those controls and adds pinned evidence, bounded inventory, scaffold maturity, path/registry/source-role conflicts, operational/legal/rail/historic/graph/geometry boundaries, config taxonomy/contract, explicit binding, validation/review, migration/deactivation/correction/rollback, definition of done, backlog, safe language, and evidence ledger.

</details>

<details>
<summary><strong>Appendix B — documentation-only boundary</strong></summary>

This revision changes no payload, consumer, loader, source record, schema, contract, policy, code, validator, test, fixture, workflow, lifecycle/trust/catalog/release object, map/API/UI, route, or operational behavior.

</details>

## Status summary

`configs/domains/roads-rail-trade/` is a README-only, non-secret, non-authoritative configuration-support lane. The surrounding repository contains extensive documentation and many implementation-shaped paths, but inspected executable/validation surfaces remain scaffolds or placeholders. No direct config consumer is established. Future payloads require explicit binding, accepted authority refs, source-role/time/stale preservation, uncertainty/graph safeguards, sensitivity review, no-operational-use defaults, validation, and rollback.

<p align="right"><a href="#top">Back to top</a></p>
