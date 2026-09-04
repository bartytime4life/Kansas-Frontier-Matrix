<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-roads-rail-trade-readme
title: configs/domains/roads-rail-trade/ — Governed Roads, Rail, Trade, and Mobility Configuration Boundary
type: readme
version: v0.3
status: draft; repository-grounded; README-only configuration lane; non-authoritative
owners:
  - "@bartytime4life — verified /configs/ CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, configuration, source/rights, historic-route, infrastructure-sensitivity, consumer, validation, policy, and release stewardship"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; config-sublane; roads-rail-trade; transport; mobility; source-role-aware; time-aware; historic-route-uncertainty-aware; infrastructure-aware; non-secret; non-authoritative; not-navigation; not-rail-operations; no-live-binding; no-source-activation; no-release-authority"
current_path: configs/domains/roads-rail-trade/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
responsibility: "Document safe, non-secret Roads/Rail/Trade configuration authoring and future explicit consumer binding without acquiring route, source, policy, evidence, operational, legal-access, or release authority."
truth_posture: "CONFIRMED tracked README-only configuration inventory, parent configuration contract, accepted Directory Rules adoption, domain documentation, current workflow source, bounded synthetic CorridorRoute validation surface, and review routing; PROPOSED future configuration classes and payload/binding profiles; UNKNOWN runtime consumption, loader precedence, deployment integration, and public use; NEEDS VERIFICATION accountable stewardship, source rights, freshness profiles, sensitivity/public-safe transforms, slug convergence, and exact-head hosted validation."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  base_ref: main
  base_commit: 9e152476cda7bd9b80a2afac8031619a1898eceb
  prior_blob: 522af8a076d27b28e1ea5695ebef235d9b39b94e
  parent_readme_blob: c497e41466f3aaf934aeca4b9976a2fa8516ff21
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  domain_readme_blob: f2d1250dad3eefd2f148483ddcc388e66d2a2186
  domain_workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  semantic_contract_readme_blob: 79422f2b9fddd8a2755f54e43f94890881223b98
related:
  - ../README.md
  - ../../README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../../docs/domains/roads-rail-trade/HISTORIC_ROUTES.md
  - ../../../contracts/domains/roads-rail-trade/README.md
  - ../../../contracts/transport/README.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../../schemas/contracts/v1/transport/
  - ../../../policy/domains/roads-rail-trade/README.md
  - ../../../fixtures/domains/roads-rail-trade/README.md
  - ../../../tests/domains/roads-rail-trade/README.md
  - ../../../tools/validators/domains/roads-rail-trade/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../release/candidates/roads-rail-trade/README.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
tags: [kfm, configs, roads, rail, trade-routes, transport, mobility, corridors, graph-projection, source-role, time, uncertainty, sensitivity, infrastructure, no-secrets, not-navigation, governance]
notes:
  - "v0.3 supersedes v0.2 documentation at this same path; no executable payload, consumer, schema, contract, policy, source record, workflow, lifecycle object, or release object changes."
  - "README-only describes this tracked configuration directory, not the maturity of the whole Roads/Rail/Trade domain."
  - "The current domain workflow now checks required repository surfaces, parses schemas/fixtures, runs CorridorRoute schema tests and a fixture validator, while proof and release producers remain unestablished. The older blanket TODO-only workflow description is superseded."
  - "Observed roads-rail-trade versus transport contract/schema placement remains conflicted in current repository evidence; this README does not resolve or duplicate that authority decision."
  - "Configuration may reference an accepted source, temporal, uncertainty, graph, public-safe display, or review profile. It cannot create route truth, source authority, current-condition truth, legal access, routing advice, rail-operating instructions, policy, evidence, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Roads, Rail, Trade, and Mobility Domain Configuration

`configs/domains/roads-rail-trade/`

> Safe, non-secret configuration documentation for Roads/Rail/Trade consumers. This lane can describe how already-governed transport context is selected or presented; it cannot decide what is true, open, safe, lawful, operational, admitted, or released.

**Status:** draft v0.3 · **Tracked contents:** README only · **Owning root:** `configs/` · **Consumer binding:** UNKNOWN

[Evidence](#status-and-evidence) · [Placement](#repository-fit-and-directory-rules-basis) · [Contract](#minimum-configuration-contract) · [Roles](#source-role-and-knowledge-character) · [Historic routes](#historic-route-and-trade-corridor-uncertainty) · [Graph](#network-topology-and-graph-projection) · [Validation](#validation-and-test-matrix) · [First payload](#definition-of-done-for-the-first-payload) · [Rollback](#rollback-correction-supersession-and-invalidation)

> [!CAUTION]
> KFM Roads/Rail/Trade context is **not** turn-by-turn navigation, dispatch, traffic control, emergency routing, legal-access advice, bridge-safety certification, railroad operating authority, train movement authority, or a guarantee that any road, rail line, crossing, bridge, ferry, facility, route, or corridor is open, passable, lawful, current, or complete.

## Purpose

Inherit the [domain configuration contract](../README.md) and [configuration root contract](../../README.md). This page adds Roads/Rail/Trade-specific constraints for future named consumers.

A future configuration may help a consumer label, filter, compare, generalize, cache, or present **already-governed** route, facility, restriction, graph, or historic-corridor context. It cannot decide:

- whether a road, rail line, crossing, bridge, ferry, depot, siding, yard, corridor, or facility exists;
- whether geometry is accurate, surveyed, current, connected, passable, public, or legally accessible;
- whether a route designation, route membership, operator assignment, restriction, closure, or condition is official or current;
- whether a modeled, reconstructed, inferred, candidate, synthetic, or graph-projected route is observed truth;
- whether a historic route follows a precise alignment where evidence supports only a corridor or narrative;
- whether sensitive infrastructure, cultural corridors, archaeology-adjacent context, or restricted operational detail may be exposed;
- whether evidence supports a consequential claim;
- whether a source is admitted, active, licensed, or redistributable;
- whether an artifact may be promoted, released, or published.

## Authority level

**Implementation-supporting and non-authoritative.** Configuration may reference an accepted decision; it may not manufacture one.

Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`. Promotion is a governed transition, not a file move.

| Concern | Owning authority or required evidence | Configuration limit |
|---|---|---|
| Domain meaning | [Roads/Rail/Trade doctrine](../../../docs/domains/roads-rail-trade/README.md) and semantic contracts | No redefinition of route, facility, operator, restriction, graph, or story semantics. |
| Machine shape | Accepted schema home/version | No second schema authority; the current `roads-rail-trade` / `transport` split remains unresolved here. |
| Source identity, rights, role, cadence | Source governance and registry | No source admission, activation, redistribution permission, or role upgrade. |
| Current route/condition status | Official source plus valid-time/freshness evidence | No current-condition assertion from a config value. |
| Navigation / legal access / rail operations | Official operational and legal authorities | None. |
| Historic alignment | Source comparison, uncertainty, steward review | No conversion of narrative or plausible corridor into surveyed alignment. |
| Graph/topology | Derived graph contracts and validation | Graph edges are analytical derivatives, not canonical or operational routes. |
| Sensitivity/public exposure | Policy, review, transform receipts, release | No exact-location or operational-detail permission. |
| Evidence/release | EvidenceBundle closure and governed release records | No approval, promotion, release, publication, or rollback completion. |
| Consumer behavior | Exact loader, binding, parser, tests, and runtime evidence | No implicit discovery, precedence, network access, or deployment. |

## Status and evidence

### Current snapshot

This revision is pinned to `main@9e152476cda7bd9b80a2afac8031619a1898eceb`. The previous README blob is `522af8a076d27b28e1ea5695ebef235d9b39b94e`.

The bounded tracked directory remains:

```text
configs/domains/roads-rail-trade/
└── README.md
```

### Current maturity matrix

| Surface | Confirmed at the snapshot | Still unproved or unresolved |
|---|---|---|
| Configuration lane | One tracked README; no executable configuration payload in this directory. | Loader, precedence, ignored/untracked external config, deployment/runtime consumption. |
| Parent contracts | `configs/domains/README.md` v0.6 and the root configuration boundary separate config from truth/governance authority. | Universal consumer-binding convention. |
| Domain documentation | Roads/Rail/Trade doctrine, canonical-path, object-family, and historic-route documentation exist. | Whole-domain implementation completeness or production readiness. |
| Semantic contracts | `contracts/domains/roads-rail-trade/` exists, while `contracts/transport/` also exists. | Canonical slug convergence; current docs explicitly record the conflict/divergence. |
| Machine schemas | Domain workflow expects `schemas/contracts/v1/domains/roads-rail-trade/` schema surfaces and parses them. | Acceptance of every schema family, broader `transport/` relationship, consumer use. |
| CorridorRoute validation slice | Workflow runs `tests/schemas/test_corridor_route_contract.py` and `validate_corridor_route.py --fixtures`. | Hosted exact-head result for this README revision; broader transport-family correctness. |
| Other validator roots | Workflow requires crossings/bridge/facility validator roots to remain documented scaffolds and fails if implementation appears without explicit wiring. | Accepted executable implementations for those families. |
| Proof / release | Workflow source states proof and release-dry-run producers are not established. | Promotion, release assembly, signer custody, deployment, publication, rollback drill. |
| Review routing | `/configs/` routes to `@bartytime4life` in CODEOWNERS. | Accountable specialist stewardship, independent approval, required-review enforcement. |

### Evidence boundary

The v0.2 blanket statement that inspected workflow, schema, validator, and source surfaces were merely TODO/empty scaffolds is no longer accurate. Current repository evidence now contains a bounded synthetic `CorridorRoute` validation slice and a workflow that explicitly checks its dependencies. That improvement is real but narrow: it does **not** establish a configuration consumer, live source activation, route authority, production readiness, or release status.

The KFM domain corpus treats modern and historic movement systems as evidence-bearing but risk-sensitive: narrative geometry may be less precise than mapped geometry, rail alignment is distinct from operator/status, and movement-story products remain derived carriers rather than root truth. The current repository domain dossier preserves those distinctions.

## What belongs here

Safe, non-secret configuration documentation and, when separately scoped, small **inactive** templates or synthetic examples for a named consumer.

Candidate configuration classes may include:

| Class | Bounded purpose |
|---|---|
| `context_presentation` | Labels, source-role badges, time, uncertainty, historical/current distinction. |
| `freshness_profile_ref` | Reference a governed source/product validity profile; never extend official validity. |
| `historic_uncertainty_profile_ref` | Select reviewed corridor/generalization treatment for uncertain historic alignments. |
| `graph_projection_profile_ref` | Configure analytical graph behavior while retaining derived/non-operational labeling. |
| `public_safe_profile_ref` | Reference policy-owned redaction, aggregation, suppression, delay, or generalization. |
| `review_routing` | Select a governance-review path; never approve. |
| `feature_toggle` | Non-consequential presentation behavior only; never activate source/network/release effects. |
| `synthetic_test_profile` | Deterministic, no-network test inputs. |
| `migration_compatibility` | Time-bounded compatibility mapping with one writer and explicit rollback. |

These are **PROPOSED authoring classes**, not an implemented enum or accepted config schema.

## What does not belong here

Do not store credentials, cookies, private keys, service accounts, signed URLs, private endpoints, workstation-specific paths, live operational feeds, traffic/closure payloads, dispatch/rail instructions, sensitive track charts or signal layouts, restricted facility/access detail, source-admission decisions, policy rules, schemas, semantic contracts, lifecycle data, receipts, proofs, release manifests, published tiles, or model output.

Do not use this lane to bypass the unresolved `roads-rail-trade` versus `transport` authority split by creating a third home or silent alias.

## Repository fit and Directory Rules basis

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact [Directory Rules v2](../../../docs/doctrine/directory-rules.md) bytes. The retained `PROPOSED_FOR_ADOPTION` label inside those pinned bytes is historical text; the accepted ADR is the adoption authority.

This README stays under `configs/` because its responsibility is configuration documentation. The `roads-rail-trade` segment refines that responsibility; it does not create a root-level domain. Domain meaning remains under `docs/`/`contracts/`, shape under `schemas/`, admissibility under `policy/`, tests/fixtures under their own roots, lifecycle records under `data/`, and release/correction authority under `release/`.

No file move, new root, alias, schema home, contract home, or ADR is introduced by this revision.

## Minimum configuration contract

Before any future payload becomes active, the binding should establish at least:

- stable `config_id` and immutable `config_version`;
- exact named `consumer_id` and accountable owner;
- config class and bounded purpose;
- exact allowed filename/path and parser;
- schema/profile version or digest;
- source/profile references only, never embedded admission authority;
- required/optional-file behavior;
- unknown-key, duplicate-key, alias, and unsupported-version rejection;
- merge/precedence order with policy/rights/sensitivity fields non-overridable;
- atomic load/reload semantics and fail-closed fallback;
- rollback target and supersession relationship.

These field names are design requirements, not proof of an accepted machine schema.

## Source role and knowledge character

A config consumer must preserve the role assigned by admitted evidence. Configuration must never upgrade a modeled, administrative, regulatory, contextual, candidate, reconstructed, or synthetic record into an observation.

At minimum, transport-facing presentation should keep distinct:

- observed or surveyed geometry;
- administrative designation or inventory status;
- operator/jurisdiction assertions;
- restriction/closure context;
- model or graph projection;
- historic reconstruction/candidate alignment;
- synthetic test material;
- derived narrative/story products.

When roles conflict or evidence is insufficient, retain the conflict and use finite failure behavior rather than silently choosing the most authoritative-looking layer.

## Time, freshness, and stale state

Material time kinds should remain explicit where they exist: observation/effective time, valid interval, source publication time, retrieval time, KFM release time, and correction/supersession time.

A configured display threshold does not make stale information current. A future live consumer must obtain accepted freshness rules from source/product governance. When current status cannot be supported, use `ABSTAIN`, `HOLD`, or a plainly historical/stale presentation instead of an operational implication.

## Historic route and trade corridor uncertainty

Historic trails, roads, mail/stage routes, military/emigrant corridors, cattle trails, river crossings, and trade corridors often combine narrative, cartographic, archaeological, and later interpretive evidence. Configuration should preserve that uncertainty rather than manufacture a single precise line.

A future profile may reference accepted behavior for corridor-width/generalization classes, evidence-density/confidence display, segment-level disagreement, source-comparison mode, generalized public geometry, narrative/story-node presentation, and withheld or restricted cultural/sensitive route context.

No threshold in this directory can convert plausibility into observation or authorize exposure of culturally sensitive or restricted alignments.

## Network topology and graph projection

Graph edges and inferred connectivity are **derived analytical products**. A config may select an accepted graph profile for a named consumer, but it must retain source segment IDs, transform/spec identity, valid-time assumptions, uncertainty, and a visible derived label.

Graph traversal must not be presented as safe routing, legal access, current passability, railroad-operating instruction, emergency routing, or source geometry truth.

## Geometry, access, and public-safe representation

Geometry is not access permission. A displayed line or point does not establish ownership, right-of-way, public entry, current condition, bridge safety, route clearance, or permission to cross railroad/private property.

Where infrastructure, archaeology-adjacent context, private land, culturally sensitive corridors, or operational detail creates risk, configuration may only **reference** an accepted public-safe transform/profile. Redaction, generalization, suppression, delay, or denial remain policy/review decisions with appropriate receipts and release evidence.

## Failure behavior

A future consumer should fail closed for malformed payloads, unknown versions, ambiguous aliases, missing required config, invalid profile refs, prohibited substitutions, conflicting source roles, unsupported time state, missing evidence, or unresolved sensitivity.

Safe outward outcomes include `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`, with `HOLD` for governed work-state blocking where applicable. No consumer should fall back to uncited route claims or permissive operational guidance.

## Governed AI and generated language

AI may summarize released, EvidenceBundle-backed transport context. It may not infer current closures, safe passage, legal access, route authority, precise historic alignment, rail operations, or sensitive infrastructure from configuration.

Generated movement stories are narratives, not source truth. They must preserve citations, source role, time scope, uncertainty, release/correction state, and bounded confidence or abstain.

## Validation and test matrix

| Validation layer | Current status | Minimum future expectation |
|---|---|---|
| Markdown structure/links | REQUIRED for this README | Headings, anchors, local links, metadata, and conflict markers checked. |
| Directory placement | CONFIRMED existing path | No parallel root/home or silent alias. |
| Config syntax/schema | NOT APPLICABLE today — no payload | Parse plus restrictive schema when a payload is introduced. |
| Consumer binding | UNKNOWN | Exact consumer and file/version binding test. |
| Unknown/duplicate keys | UNKNOWN | Negative fixtures and fail-closed behavior. |
| CorridorRoute domain validation | BOUNDED EXISTING SLICE | Keep current synthetic schema/validator tests green; do not generalize their proof. |
| Historic uncertainty | NEEDS VERIFICATION | Negative fixtures for false precision and role collapse before consumer activation. |
| Graph projection | NEEDS VERIFICATION | Derived-label, provenance, and non-routing tests. |
| Sensitive/public-safe geometry | NEEDS VERIFICATION | Redaction/generalization/suppression denial tests. |
| Hosted exact-head CI | PENDING until PR runs | Attribute results to exact head; do not treat green CI as release approval. |

This documentation-only revision does not claim that repository-wide validation, live source probes, browser/runtime tests, route computations, release drills, or deployment checks were run.

## Review burden

**Moderate documentation review.** Executable risk is low because this change edits only one README, but the wording touches transport authority, historic uncertainty, infrastructure sensitivity, and an unresolved path/slug split.

Review should confirm that the README remains subordinate to parent configuration contracts, does not imply current navigation/legal-access/closure/bridge/rail authority, does not convert the bounded CorridorRoute validation slice into domain-wide maturity, preserves historic-route uncertainty and graph-derived labeling, does not silently resolve the `roads-rail-trade` / `transport` conflict, and does not imply source activation, evidence closure, release, or publication.

## Definition of done for the first payload

The first executable file in this directory should not be added until a bounded PR can prove:

- [ ] one named consumer and accountable owner;
- [ ] one unambiguous file name and profile version;
- [ ] accepted placement without creating another transport alias/home;
- [ ] restrictive schema and parser behavior;
- [ ] valid and invalid synthetic fixtures;
- [ ] unknown/duplicate-key rejection;
- [ ] source-role preservation;
- [ ] explicit time/freshness behavior;
- [ ] historic-route uncertainty and false-precision denial where applicable;
- [ ] graph-derived/non-routing behavior where applicable;
- [ ] no secret, network, source-activation, operational-routing, or release side effect;
- [ ] public-safe geometry policy references where needed;
- [ ] exact consumer binding plus rollback/disable test;
- [ ] documentation and migration notes.

## Rollback, correction, supersession, and invalidation

For this README-only change, rollback is a normal Git revert of the documentation commit.

For a future active payload, rollback must restore the prior known-good config version or disable the binding atomically. Do not delete or rewrite lifecycle evidence to simulate rollback. If source role, time, route identity, sensitivity, or release evidence later changes, invalidate downstream caches/derived views through governed correction paths rather than silently retaining stale output.

## Open verification

- accountable specialist ownership beyond CODEOWNERS review routing;
- canonical convergence or accepted compatibility for `roads-rail-trade` versus `transport` contract/schema homes;
- actual config consumer discovery, precedence, merge, and reload behavior;
- source-role vocabulary and source-rights closure for live transport sources;
- product-specific freshness and stale-state profiles;
- historic-route uncertainty/generalization thresholds;
- graph projection validation and movement-story constraints;
- public-safe handling of infrastructure and culturally sensitive corridors;
- hosted exact-head checks for this PR;
- release, correction, rollback, deployment, and publication integration.

## Related folders

- [Domain configuration parent](../README.md)
- [Configuration root](../../README.md)
- [Roads/Rail/Trade domain dossier](../../../docs/domains/roads-rail-trade/README.md)
- [Current domain semantic-contract lane](../../../contracts/domains/roads-rail-trade/README.md)
- [Transport contract compatibility/alternate lane](../../../contracts/transport/README.md)
- [Roads/Rail/Trade policy](../../../policy/domains/roads-rail-trade/README.md)
- [Roads/Rail/Trade fixtures](../../../fixtures/domains/roads-rail-trade/README.md)
- [Roads/Rail/Trade tests](../../../tests/domains/roads-rail-trade/README.md)
- [Roads/Rail/Trade validator lane](../../../tools/validators/domains/roads-rail-trade/README.md)
- [Source registry lane](../../../data/registry/sources/roads-rail-trade/README.md)
- [Release candidates](../../../release/candidates/roads-rail-trade/README.md)
- [Domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)

## Last reviewed

**2026-09-04** against `main@9e152476cda7bd9b80a2afac8031619a1898eceb`.

This README records a configuration boundary and bounded current repository evidence. It does not prove runtime consumption, source activation, transport authority, deployment, release, or publication.

[Back to top](#top)
