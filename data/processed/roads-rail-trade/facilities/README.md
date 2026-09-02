<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-roads-rail-trade-facilities-readme
title: data/processed/roads-rail-trade/facilities/README.md — Roads / Rail / Trade Facilities Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; roads-rail-trade-domain-lane; transport-facility-lane; infrastructure-adjacent-lane
status: repository-grounded draft; PROPOSED lane contract; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — Roads/Rail/Trade steward · Transport facility steward · Settlements/Infrastructure steward · Sensitivity reviewer · Rights steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; infrastructure-adjacent; source-role-preserved; release-gated
tags: [kfm, data, processed, roads-rail-trade, facilities, TransportFacility, depot, station, yard, terminal, interchange, source-role, sensitivity, evidence, correction, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md
  - ../../../../docs/domains/roads-rail-trade/SENSITIVITY.md
  - ../../../../docs/domains/roads-rail-trade/PIPELINE.md
  - ../../../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/archaeology/README.md
  - ../../../../contracts/domains/roads-rail-trade/README.md
  - ../../../../contracts/domains/roads-rail-trade/depot.md
  - ../../../../policy/domains/roads-rail-trade/
  - ../../../../policy/sensitivity/transport/
  - ../../../../schemas/contracts/v1/domains/roads-rail-trade/
  - ../../../raw/roads-rail-trade/
  - ../../../work/roads-rail-trade/
  - ../../../quarantine/roads-rail-trade/
  - ../../../catalog/domain/roads-rail-trade/
  - ../../../triplets/
  - ../../../published/
  - ../../../proofs/
  - ../../../receipts/
  - ../../../registry/sources/roads-rail-trade/
  - ../../../../release/candidates/roads-rail-trade/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized transport-facility candidates and lineage sidecars, not source captures, catalog records, proof closure, policy decisions, release authority, operations systems, or public-serving behavior."
  - "Transport-facility identity, route role, operator assignment, status, location precision, and temporal validity must remain distinct from infrastructure ownership, condition, vulnerability, security, and legal authority."
  - "Critical-facility detail, restricted-source-derived fields, cultural-corridor joins, private access details, and exact harmful-precision coordinates fail closed unless policy and release evidence explicitly permit exposure."
  - "Prior blob and rollback target: 25a13cf1829c5bb454aa3dc2aa2c9a7989221e97."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/roads-rail-trade/facilities/` — Transport Facility Candidates

> **One-line purpose.** Own normalized, source-traced, role-preserved transport-facility candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, operational, or authoritative infrastructure records.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: preserved](https://img.shields.io/badge/source%20role-preserved-1a7f37?style=flat-square)](#facility-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#sensitivity-and-cross-domain-boundaries)

> [!IMPORTANT]
> Directory placement, successful normalization, a matched facility name, a topology join, a map render, a pull request, or a merge does not create truth, policy permission, catalog admission, release approval, legal authority, operational status, or KFM publication.

> [!WARNING]
> Exact harmful-precision locations, critical-facility details, private access information, condition or vulnerability fields, restricted-source content, culturally sensitive route joins, and infrastructure-security context must remain restricted, generalized, quarantined, or denied unless an evidence-backed policy and release path explicitly permits exposure.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Facility semantics](#facility-semantics) · [Identity and time](#identity-and-temporal-contract) · [Sensitivity](#sensitivity-and-cross-domain-boundaries) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This child lane owns processed transport-facility candidates under the Roads / Rail / Trade responsibility segment. Typical candidates represent depots, stations, yards, terminals, interchanges, rostered facilities, or facility-like transport nodes while preserving source identity, source role, temporal state, route/network context, uncertainty, and sensitivity posture.

The lane may support downstream route, corridor, topology, historical, freight, settlement, or infrastructure analysis. It does not itself establish ownership, legal right-of-way, current operating authority, condition, vulnerability, security posture, access permission, freight capacity, emergency role, or public-release readiness.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized facility candidates, relationship candidates, temporal-status sidecars, reconciliation inventories, and local explanatory metadata. It does not own:

- source-native captures or original provider payloads;
- semantic contract or machine-schema authority;
- policy, sensitivity, rights, or access-control decisions;
- EvidenceBundle, proof, or receipt authority;
- catalog, triplet, release, or publication decisions;
- infrastructure ownership, condition, vulnerability, or security truth;
- public map, API, UI, routing, operations, emergency, or AI behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Item | Bounded result |
|---|---|
| Path | `data/processed/roads-rail-trade/facilities/README.md` |
| Version | `v0.2.0` |
| Prior blob | `25a13cf1829c5bb454aa3dc2aa2c9a7989221e97` |
| Parent lane | `data/processed/roads-rail-trade/` |
| Lifecycle phase | `PROCESSED` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Contract/schema enforcement | `NEEDS VERIFICATION` |
| Public readiness | `DENY BY DEFAULT` |

## What belongs here

Subject to contracts, rights, sensitivity, and validation, this lane may hold:

- normalized `TransportFacility` candidates for depots, stations, yards, terminals, interchanges, rosters, and related transport nodes;
- facility identity candidates with source identifiers, names, aliases, type, source role, time scope, uncertainty, and digest posture;
- facility-to-route, facility-to-corridor, facility-to-network-node, facility-to-crossing, facility-to-operator, and facility-to-status relationship candidates;
- historical facility assertions or modeled reconstructions when source role and uncertainty remain explicit;
- relocation, merge, split, decommissioning, renaming, supersession, and correction lineage;
- generalized or redacted public-candidate derivatives that remain upstream of catalog and release;
- lane-local inventories, disposition records, and README material that explain boundaries without becoming proof, policy, or release authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Source-native rosters, agency exports, logs, original coordinates, provider identifiers, or partner files | `data/raw/roads-rail-trade/` |
| Geocoding experiments, identity-matching scratch, route joins, notebooks, temporary topology, or redaction trials | `data/work/roads-rail-trade/` |
| Unresolved rights, disputed identity, unknown role, unsafe precision, critical-facility detail, restricted-source fields, or culturally sensitive joins | `data/quarantine/roads-rail-trade/` |
| Catalog records or triplet/graph projections | `data/catalog/` and `data/triplets/` |
| Proofs, EvidenceBundles, and receipts | `data/proofs/` and `data/receipts/` |
| Source descriptors and registry truth | `data/registry/sources/roads-rail-trade/` |
| Policy, sensitivity, or access rules | `policy/` |
| Release decisions, manifests, rollback cards, or correction authority | `release/` |
| Published layers, API payloads, routes, or downloads | `data/published/` and governed delivery interfaces |
| Infrastructure ownership, building/asset identity, condition, vulnerability, or security truth | Settlements/Infrastructure or other owning responsibility roots |
| Hydrology, hazards, archaeology, land/title, or emergency truth | Their respective governed domain roots |
| Credentials, secrets, access instructions, exact transform offsets, suppression thresholds, or harmful operational detail | Approved restricted operational systems |

## Inputs

Admitted inputs are governed WORK products or resolved QUARANTINE exits with, as applicable:

- stable candidate identity and content digest;
- source descriptor and source role;
- rights and sensitivity posture;
- facility type and transport role;
- source, observed, valid, effective, retrieval, correction, and release-relevant time fields;
- geometry and precision classification;
- route, corridor, topology, operator, and status relationship context;
- uncertainty, caveats, and conflict state;
- contract/schema references and validation evidence;
- correction predecessor/successor and rollback references.

## Outputs

Valid outputs are inputs to downstream catalog/triplet projection, EvidenceBundle assembly, sensitivity review, release-candidate review, and public-safe derivative creation.

PROCESSED placement does not prove catalog closure, evidence closure, public safety, release approval, current operating status, or production hosting. Public clients must not read this lane directly.

## Facility semantics

Transport-related concepts must remain distinct:

| Concept | Meaning in this lane | Must not collapse into |
|---|---|---|
| Facility candidate | Proposed or normalized transport facility identity | Infrastructure ownership or legal authority |
| Route membership | Facility relationship to a route or corridor | Facility identity |
| Operator assignment | Time-bounded operator/service relationship | Property ownership or permanent authority |
| Status event | Time-bounded open, closed, relocated, inactive, or other status assertion | Static identity or current truth without freshness support |
| Restriction event | Time-bounded restriction context | Facility condition or legal closure authority by default |
| Historical assertion | Source-bounded claim about a past facility or role | Current operating status |
| Modeled reconstruction | Derived or inferred facility context | Observed or administrative fact |
| Synthetic description | Generated explanatory text | Evidence or source truth |

Source roles such as observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic are not interchangeable. Promotion never upgrades a source role.

## Identity and temporal contract

Each candidate should preserve enough information to distinguish identity, location, and status through time:

| Requirement | Expected posture |
|---|---|
| Stable identity | Deterministic or steward-reviewed candidate ID where practical |
| Source identity | Source-specific IDs remain traceable and are not silently replaced |
| Aliases and names | Current, historical, alternate, and source-native names remain distinguishable |
| Facility type | Depot, station, yard, terminal, interchange, roster facility, or other reviewed class |
| Geometry role | Exact, generalized, centroid, approximate, historical, modeled, or unknown |
| Time semantics | Source, observed, valid/effective, retrieval, correction, supersession, and release times remain distinct |
| Status | Active, inactive, relocated, closed, historical, proposed, candidate, unknown, or source-declared equivalent |
| Relocation | Predecessor/successor relation and effective interval preserved |
| Merge/split | Lineage and affected relationship candidates preserved |
| Conflict state | Competing source assertions remain visible rather than silently overwritten |
| Correction state | Corrected, superseded, withdrawn, or tombstoned state remains resolvable |

## Sensitivity and cross-domain boundaries

The most restrictive applicable policy row governs exposure.

- Exact harmful-precision facility locations may require generalization, staged access, or denial.
- Critical-facility, condition, vulnerability, capacity, access, ownership, and security details fail closed unless explicitly reviewed.
- Private-land and parcel-person joins remain outside ordinary public surfaces.
- Restricted-source-derived attributes remain restricted even when geometry is public.
- Cultural corridors, tribal or sovereign context, archaeology joins, and historic routes require steward review before spatial exposure.
- Hydrology owns water truth; Hazards owns event and impact truth; Settlements/Infrastructure may own canonical asset identity or condition; People/Land owns title and parcel-person truth.
- Styling, zoom thresholds, client-side filtering, or omitted labels are not sufficient redaction controls.

## Validation

A bounded validation pass should check, at minimum:

- placement and one-lane responsibility;
- stable identity, digest, aliases, and source IDs;
- source role and rights posture;
- facility type and object-family distinction;
- geometry role, precision, sensitivity, and public-safe transform references;
- route, corridor, node, crossing, operator, and status relationship integrity;
- source, valid, retrieval, correction, and supersession times;
- conflict, relocation, merge/split, decommissioning, and correction lineage;
- contract/schema references and declared validator scope;
- evidence, receipt, policy, catalog, release, correction, and rollback dependencies;
- absence of condition, vulnerability, security, access, or other restricted detail from public-candidate derivatives.

No complete lane-wide validator was verified. A passing check proves only its declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes involving payloads, facility identity, geometry precision, source activation, rights, sensitive joins, current status, operator assignments, public derivatives, correction, or rollback require the relevant domain, infrastructure, sensitivity, rights, evidence, validation, and release reviewers.

CODEOWNERS routing, a pull request approval, or a successful CI check is not policy permission or release evidence by itself.

## Correction and rollback

Corrections must be explicit and reversible:

1. identify the affected facility candidate, relationship candidates, and derived products;
2. record whether the issue concerns identity, location, type, status, operator, route membership, source role, time, sensitivity, or rights;
3. preserve predecessor/successor and correction lineage;
4. invalidate or regenerate dependent catalog, graph, layer, API, index, cache, and AI-context artifacts where applicable;
5. issue correction, withdrawal, or rollback records through their governed roots;
6. verify that harmful or stale detail is no longer available through public routes or caches.

Documentation rollback target: prior blob `25a13cf1829c5bb454aa3dc2aa2c9a7989221e97`.

## Related folders

- Parent processed lane: [`../README.md`](../README.md)
- Parent lifecycle contract: [`../../README.md`](../../README.md)
- Domain object families: [`../../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md`](../../../../docs/domains/roads-rail-trade/OBJECT_FAMILIES.md)
- Domain sensitivity: [`../../../../docs/domains/roads-rail-trade/SENSITIVITY.md`](../../../../docs/domains/roads-rail-trade/SENSITIVITY.md)
- Settlements/Infrastructure boundary: [`../../../../docs/domains/settlements-infrastructure/README.md`](../../../../docs/domains/settlements-infrastructure/README.md)
- Contracts: [`../../../../contracts/domains/roads-rail-trade/README.md`](../../../../contracts/domains/roads-rail-trade/README.md)
- Policy: [`../../../../policy/domains/roads-rail-trade/`](../../../../policy/domains/roads-rail-trade/) and [`../../../../policy/sensitivity/transport/`](../../../../policy/sensitivity/transport/)
- Catalog: [`../../../catalog/domain/roads-rail-trade/`](../../../catalog/domain/roads-rail-trade/)
- Proofs and receipts: [`../../../proofs/`](../../../proofs/) · [`../../../receipts/`](../../../receipts/)
- Release candidates: [`../../../../release/candidates/roads-rail-trade/`](../../../../release/candidates/roads-rail-trade/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, rights, sensitivity, owners |
| Active writers and consumers | `UNKNOWN` | Pipelines, tools, workflows, APIs, UI, graph, indexes, deployments |
| Contract and schema enforcement | `UNKNOWN` | Accepted contract/schema versions, fixtures, validators, CI, negative cases |
| Facility identity reconciliation | `NEEDS VERIFICATION` | Duplicate, alias, relocation, merge/split, and conflict handling evidence |
| Sensitivity enforcement | `UNKNOWN` | Policy decisions, transforms, redaction receipts, access controls, negative tests |
| Cross-domain ownership | `NEEDS VERIFICATION` | Roads/Rail/Trade vs. Settlements/Infrastructure responsibility decisions |
| Evidence/catalog/release closure | `UNKNOWN` | EvidenceBundles, catalog records, release manifests, correction and rollback links |
| Public invalidation | `UNKNOWN` | Governed routes, caches, indexes, stale/withdrawn handling, rollback drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle boundary | Preserved and aligned to parent contract |
| Facility examples and transport context | Preserved and clarified |
| Source-role anti-collapse | Preserved and strengthened |
| Infrastructure-adjacent and cross-domain boundaries | Preserved and strengthened |
| Rights, sensitivity, evidence, policy, release, correction, and rollback controls | Preserved |
| Prior blob and rollback target | Recorded |
| Payload, migration, path, source, runtime, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the child lane to the current processed-data authority model;
- clarified facility identity, temporal, relationship, and cross-domain semantics;
- strengthened harmful-precision, critical-facility, rights, sensitivity, correction, and rollback controls;
- added validation, review, verification, and no-loss sections;
- changed Markdown only.

[Back to top](#top)
