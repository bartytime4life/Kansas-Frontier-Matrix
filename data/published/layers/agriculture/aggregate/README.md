<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/agriculture/aggregate/readme
title: data/published/layers/agriculture/aggregate/README.md — Agriculture Aggregate Published Layer README
type: directory-readme; published-layer-carrier; agriculture-domain-lane; aggregate-public-safe-lane
version: v0.2.0
status: repository-grounded draft; publication/runtime enforcement unverified
owners:
  - NEEDS VERIFICATION — data publication steward
  - NEEDS VERIFICATION — agriculture domain steward
  - NEEDS VERIFICATION — map-layer steward
  - NEEDS VERIFICATION — policy steward
  - NEEDS VERIFICATION — release steward
created: 2026-06-26
updated: 2026-07-25
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: public-review; release-required; aggregate-only; no-direct-canonical-path
path: data/published/layers/agriculture/aggregate/README.md
truth_posture: >
  CONFIRMED target path, parent published-layer contracts, agriculture aggregate-publication doctrine,
  and prior README / PROPOSED carrier naming, local manifests, indexes, and validation details /
  UNKNOWN emitted payload bytes, active routes, cache behavior, and deployed consumers /
  NEEDS VERIFICATION release manifests, EvidenceBundles, receipts, field allowlists, digests,
  validators, CI enforcement, correction propagation, and rollback drills
related:
  - ../README.md
  - ../../README.md
  - ../../../agriculture/README.md
  - ../../../../../data/published/layers/README.md
  - ../../../../../data/proofs/README.md
  - ../../../../../data/receipts/README.md
  - ../../../../../release/README.md
  - ../../../../../release/manifests/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/agriculture/README.md
  - ../../../../../docs/domains/agriculture/RELEASE_INDEX.md
notes:
  - "This file preserves the existing published Agriculture aggregate lane and modernizes its carrier contract."
  - "Published aggregate layers are downstream, release-approved, public-safe derivatives; they do not replace canonical observations, processed data, catalog records, EvidenceBundles, receipts, policy decisions, or release authority."
  - "Agriculture public defaults are aggregate county, HUC, grid, or equivalently reviewed scopes; operator identity, private person-parcel joins, and sensitive field-level detail remain denied or restricted by default."
  - "Actual released bytes, release manifests, governed routes, validator coverage, and runtime behavior remain UNKNOWN unless verified by release-specific evidence."
  - "Prior blob and documentation rollback target: e48b7e45f186ef013b17f460d2e9ceba92462884."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/agriculture/aggregate/` — Released Aggregate Agriculture Layers

> **One-line purpose.** Hold release-approved, public-safe aggregate Agriculture layer carriers and their delivery sidecars without becoming source truth, canonical domain truth, proof authority, catalog authority, policy authority, or release authority.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-1a7f37?style=flat-square)](#authority-level)
[![Scope: aggregate only](https://img.shields.io/badge/scope-aggregate%20only-0969da?style=flat-square)](#aggregation-and-privacy-boundary)
[![Authority: carrier only](https://img.shields.io/badge/authority-carrier%20only-d1242f?style=flat-square)](#authority-level)

> [!IMPORTANT]
> A file in this directory is public-facing only when a release decision, released-byte digest, evidence support, policy decision, review state, correction path, and rollback target resolve together. Directory placement alone does not prove any of those conditions.

> [!WARNING]
> Operator identities, private person-parcel joins, source-restricted records, and sensitive field-level geometry MUST NOT be exposed here. Styling, zoom thresholds, client-side filtering, or obscured labels are not acceptable substitutes for governed aggregation or redaction.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Aggregation](#aggregation-and-privacy-boundary) · [Layer contract](#published-layer-carrier-contract) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This lane holds released aggregate Agriculture map and API layer carriers for governed KFM delivery surfaces. Aggregate layers may summarize agriculture observations, crop progress, stress, yield, irrigation, conservation, or other accepted Agriculture object families only after source rights, sensitivity, aggregation, evidence, catalog, policy, review, release, correction, and rollback gates close.

The lane is a delivery surface. It does not create Agriculture claims and it does not upgrade a processed or cataloged candidate into published truth merely by receiving copied bytes.

## Authority level

**Canonical PUBLISHED carrier responsibility; not canonical truth and not release authority.**

This path may hold released public-safe layer bytes and lane-local delivery metadata. It does not own:

- raw or processed Agriculture observations;
- semantic object meaning or machine schema;
- source registry or rights decisions;
- EvidenceBundle or proof closure;
- catalog or triplet authority;
- policy or sensitivity decisions;
- release approval, correction authority, or rollback authority;
- governed API, MapLibre, cache, CDN, or UI runtime behavior.

Those responsibilities remain in their governing roots and release-resolved interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/published/layers/agriculture/aggregate/` |
| Version | `v0.2.0` |
| Prior blob | `e48b7e45f186ef013b17f460d2e9ceba92462884` |
| Lifecycle state | `PUBLISHED` carrier lane |
| Public posture | Aggregate, released, public-safe derivatives only |
| Actual released payload inventory | `UNKNOWN` |
| Release-manifest closure | `NEEDS VERIFICATION` per release |
| Governed routes and deployed consumers | `UNKNOWN` |
| Default when support is incomplete | `HOLD`, `DENY`, `RESTRICT`, or retain upstream |

## What belongs here

Only release-approved material such as:

- PMTiles, GeoParquet, GeoJSON, COG, vector-tile, raster-tile, or equivalent aggregate Agriculture layer artifacts;
- released layer manifests or manifest pointers that identify the release record rather than replace it;
- public-field allowlists and explicit denied-field lists;
- aggregation, caveat, temporal-scope, source-role, and fitness-for-use summaries;
- released-byte digests and integrity sidecars;
- release-derived indexes or `latest.json` pointers generated from release state;
- correction, supersession, withdrawal, retirement, and rollback pointers;
- lane-local README and release notes that explain carrier behavior without creating parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW captures, vendor/agency source payloads, field records, or source-native exports | `data/raw/agriculture/` or source-specific intake |
| Transform work, joins, candidate aggregates, scratch tiles, or unreviewed generated outputs | `data/work/agriculture/` |
| Rights-unclear, sensitivity-unclear, disputed, or policy-held material | `data/quarantine/agriculture/` |
| Canonical normalized Agriculture objects | `data/processed/agriculture/` |
| Catalog records, triplets, graph projections, or EvidenceBundle state | `data/catalog/`, triplet lanes, and proof lanes |
| EvidenceBundle / proof content | `data/proofs/` |
| Validation, aggregation, redaction, build, release, or publication receipts | `data/receipts/` |
| Source descriptors and source activation decisions | `data/registry/sources/agriculture/` |
| Release manifests, promotion decisions, rollback cards, or correction authority | `release/` |
| Contracts, schemas, policy, validators, tests, fixtures, pipelines, UI, or API code | Their governing responsibility roots |
| Operator identity, private person-parcel joins, sensitive field geometry, private access details, or source-restricted attributes | Restricted governed lanes; not public published layers |
| Uncited AI summaries or model outputs presented as Agriculture truth | Governed evidence and answer paths or abstain |

## Inputs

Every carrier admitted here should resolve to a release-specific evidence chain that includes, as applicable:

- stable layer and release identity;
- source descriptors and source roles;
- source-rights and current-terms posture;
- processed and catalog artifact references;
- EvidenceRefs resolving to EvidenceBundles for carried claims;
- aggregation or redaction receipts;
- field allowlist and denied-field list;
- sensitivity and privacy decisions;
- validation and review outcomes;
- release manifest and released-byte digest;
- correction, supersession, withdrawal, and rollback targets.

## Outputs

This lane supplies release-resolved artifacts to governed map, API, report, export, and UI surfaces. Consumers should resolve a released manifest or governed layer route rather than infer currentness from filenames, directory order, or a manually edited pointer.

A public carrier must remain traceable back to the release and evidence state that authorized it.

## Aggregation and privacy boundary

Agriculture doctrine establishes aggregate publication as the public default. County, HUC, grid, or another explicitly reviewed aggregation unit may be used when the aggregation method and disclosure risk are documented.

| Boundary | Required posture |
|---|---|
| Aggregate vs. field-level detail | Public carriers default to aggregate scope; field-level output requires explicit rights, sensitivity, aggregation/redaction evidence, and release review. |
| Aggregate vs. operator identity | Operator identity and private farm-operation details are denied from public carriers. |
| Aggregate vs. person-parcel join | Private person-parcel joins remain restricted or denied. |
| Aggregate vs. source-rights limits | Aggregation does not override license, contract, or source-use restrictions. |
| Aggregate vs. canonical truth | Aggregate layers are derived summaries and do not replace underlying observations or object-level evidence. |
| Aggregate vs. absence | Suppressed, missing, generalized, or non-published values must not be rendered as zero or absence without explicit semantics. |

The aggregation scope, method, suppression rules, time window, source roles, caveats, and fitness-for-use statement should travel with each released layer.

## Published layer carrier contract

The following expectations are **PROPOSED** until release tooling and validators are verified, but they bound what a credible carrier should expose:

| Requirement | Expected evidence |
|---|---|
| Stable identity | Deterministic layer ID and release ID, or an equivalent versioned identity. |
| Release binding | Resolvable `ReleaseManifest` or release record identifying the exact carrier bytes. |
| Integrity | Digest of each released artifact and manifest-to-byte agreement. |
| Public fields | Explicit allowlist; sensitive and internal-only fields excluded before publication. |
| Aggregation | Scope, grouping unit, method, threshold/suppression posture, and `AggregationReceipt` or equivalent reference. |
| Temporal scope | Observation/reference period, aggregation window, release time, correction time, and supersession state where material. |
| Source role | Observed, modeled, aggregate, administrative, candidate, or other admitted roles remain visible and are not collapsed. |
| Evidence | Claims represented by labels, values, categories, or caveats resolve to EvidenceBundle support. |
| Caveats | Missingness, uncertainty, suppression, source limitations, fitness for use, and non-goals are public-safe and visible. |
| Correction | Superseded or corrected artifacts identify the successor and invalidation scope. |
| Rollback | Release-specific prior target exists and can be restored without reconstructing truth from this directory. |
| Governed access | Public clients consume a governed route or release-resolved artifact, not an internal canonical store. |

## Validation

Validate at least:

- path and domain/lifecycle placement;
- release-manifest and released-byte identity agreement;
- artifact format, readability, and expected layer metadata;
- digest and sidecar integrity;
- field allowlist and denied-field enforcement;
- aggregation scope, time scope, method, suppression, and missing-value semantics;
- source-role and derived-status preservation;
- EvidenceRef/EvidenceBundle resolution for carried claims;
- rights, sensitivity, privacy, and policy state;
- absence of operator identity, private joins, harmful precision, and internal fields;
- correction, supersession, withdrawal, cache invalidation, and rollback references;
- governed-route or approved released-artifact consumption.

No complete lane-wide validator or CI enforcement was verified in this task. A successful check proves only its declared scope.

## Review burden

Changes to this lane should include Agriculture, evidence, policy/privacy, map-layer, and release review as applicable. Independent review is especially important when a change alters aggregation units, suppression behavior, public fields, time semantics, geometry precision, source rights, cross-domain joins, or a current public pointer.

CODEOWNERS routing, a pull request, or a merge is not approval evidence.

## Correction and rollback

A correction should identify:

1. the affected layer and release identities;
2. the incorrect or stale carrier bytes;
3. the upstream evidence, aggregation, catalog, or release state that changed;
4. downstream manifests, indexes, `latest` pointers, routes, caches, exports, and reports requiring invalidation;
5. the corrected successor or withdrawal state;
6. the rollback target and validation evidence.

Do not silently overwrite released bytes while leaving the same identity and digest. Preserve supersession and correction lineage.

Documentation rollback target: prior blob `e48b7e45f186ef013b17f460d2e9ceba92462884`. Operational rollback remains release-specific and must be proven by the applicable release records.

## Related folders

- Parent Agriculture layer lane: [`../README.md`](../README.md)
- Parent published layers: [`../../README.md`](../../README.md)
- Agriculture published domain lane: [`../../../agriculture/README.md`](../../../agriculture/README.md)
- Proofs: [`../../../../proofs/README.md`](../../../../proofs/README.md)
- Receipts: [`../../../../receipts/README.md`](../../../../receipts/README.md)
- Release authority: [`../../../../../release/README.md`](../../../../../release/README.md)
- Agriculture doctrine: [`../../../../../docs/domains/agriculture/README.md`](../../../../../docs/domains/agriculture/README.md)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive carrier inventory | `UNKNOWN` | Pinned tree, formats, sizes, digests, current/retired state |
| Release closure | `NEEDS VERIFICATION` | Release manifests, promotion decisions, rollback cards, review state |
| Evidence and receipt closure | `NEEDS VERIFICATION` | EvidenceBundles, aggregation/redaction/build/publication receipts |
| Public-field and sensitivity enforcement | `NEEDS VERIFICATION` | Allowlists, negative fixtures, validators, policy decisions, CI |
| Governed routes and consumers | `UNKNOWN` | API/layer resolver, MapLibre/UI, exports, caches, hosting |
| Correction and rollback behavior | `UNKNOWN` | Invalidation maps, supersession records, drills, restored prior release |

Unknowns narrow publication claims and block new public transitions; they do not justify plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Same canonical path and document identity | Preserved |
| Published aggregate carrier role | Preserved and clarified |
| Release-gated, not-release-authority warning | Preserved and strengthened |
| Existing parent and authority links | Preserved and expanded |
| Release checks | Preserved and made inspectable |
| Proposed layout and naming intent | Reframed as bounded carrier requirements rather than asserted tree state |
| Correction and rollback posture | Expanded |
| Payload, release, route, schema, policy, or runtime change | None |
| Prior blob rollback target | Recorded |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane with the current published-layer parent contract;
- strengthened aggregate publication, privacy, field-allowlist, evidence, release, correction, and rollback boundaries;
- replaced speculative tree assertions with an open verification register;
- changed Markdown only.

[Back to top](#top)
