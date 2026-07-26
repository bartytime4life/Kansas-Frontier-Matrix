<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-habitat-land-cover-change-readme
title: data/processed/habitat/land_cover/change/README.md — Habitat Land Cover Change Processed Data README
version: v0.2.0
type: readme; data-lifecycle-sublane; processed-stage-guide; habitat-domain-lane; land-cover-lane; change-detection-lane; temporal-comparison-lane
status: repository-grounded draft; PROPOSED lane contract; runtime and payload enforcement unverified
owners: NEEDS VERIFICATION — Habitat steward · Land-cover steward · Change-detection steward · Remote-sensing steward · Sensitivity reviewer · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; source-role-preserved; sensitivity-aware; release-gated
tags: [kfm, data, processed, habitat, land-cover, change-detection, temporal-comparison, class-transition, remote-sensing, source-role, evidence, policy, correction, rollback]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../../docs/domains/habitat/README.md
  - ../../../../../docs/runbooks/habitat/PROMOTION_RUNBOOK.md
  - ../../../../../policy/domains/habitat/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../contracts/domains/habitat/
  - ../../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../raw/habitat/
  - ../../../../work/habitat/
  - ../../../../quarantine/habitat/
  - ../../../../catalog/domain/habitat/
  - ../../../../triplets/
  - ../../../../published/
  - ../../../../proofs/
  - ../../../../receipts/
  - ../../../../registry/sources/habitat/
  - ../../../../../release/candidates/habitat/
notes:
  - "This file preserves the existing path and document identity while aligning the lane to the current data/processed authority contract."
  - "This lane owns normalized land-cover temporal-comparison products, not source captures, catalog records, proof closure, policy decisions, release authority, or public-serving behavior."
  - "Change detection must preserve source role, class-system comparability, spatial support, temporal window, method, uncertainty, sensitivity, correction lineage, and rollback support."
  - "Land-cover change is not automatically habitat suitability, regulatory critical habitat, species occurrence, restoration priority, hazard truth, crop truth, land ownership, or land-use legality."
  - "Prior blob and rollback target: 12125a651e961d0d0c94864f7472d59d8dbe2e7f."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/habitat/land_cover/change/` — Land-Cover Change Candidates

> **One-line purpose.** Own normalized, source-traced, temporally comparable land-cover change candidates that have passed applicable WORK checks but have not thereby become cataloged, released, public, or authoritative habitat conclusions.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lifecycle: PROCESSED](https://img.shields.io/badge/lifecycle-PROCESSED-8250df?style=flat-square)](#authority-level)
[![Role: preserved](https://img.shields.io/badge/source%20role-preserved-1a7f37?style=flat-square)](#change-semantics)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-d1242f?style=flat-square)](#sensitivity-and-cross-domain-joins)

> [!IMPORTANT]
> Directory placement, a successful differencing operation, a classified transition, a map render, a pull request, or a merge does not create truth, evidence closure, policy permission, catalog admission, release approval, or KFM publication.

> [!WARNING]
> Exact or join-derived biodiversity, parcel, stewardship, wetland, rare-species, rare-plant, or other harmful-precision context must remain restricted, generalized, quarantined, or denied unless an evidence-backed policy and release path explicitly allows exposure.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Change semantics](#change-semantics) · [Comparability](#comparability-contract) · [Sensitivity](#sensitivity-and-cross-domain-joins) · [Validation](#validation) · [Review](#review-burden) · [Correction](#correction-and-rollback) · [Related](#related-folders) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

This child lane owns processed land-cover change candidates under the Habitat responsibility segment. Typical artifacts compare two or more land-cover observations, classifications, source vintages, or remote-sensing-derived products while preserving enough context to explain what changed, where, when, under which class system, and by which method.

The lane may support downstream habitat analysis, but it does not itself establish habitat quality, ecological condition, suitability, corridor value, restoration priority, species presence, regulatory designation, land-use legality, ownership, or management direction.

## Authority level

**Canonical PROCESSED responsibility; non-public by default.**

This path may own normalized change rasters, vectors, transition tables, summaries, uncertainty surfaces, and lane-local explanatory sidecars. It does not own:

- source-native captures or original pixels;
- object meaning or machine shape;
- policy or sensitivity decisions;
- EvidenceBundle or proof authority;
- catalog, triplet, release, or publication decisions;
- public API, UI, map, tile, AI, or download behavior.

Those responsibilities remain under their governed roots and interfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/habitat/land_cover/change/` |
| Version | `v0.2.0` |
| Prior blob | `12125a651e961d0d0c94864f7472d59d8dbe2e7f` |
| Parent lane | `data/processed/habitat/land_cover/` |
| Lifecycle state | `PROCESSED` candidate products |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Schema, validator, fixture, receipt, and CI enforcement | `NEEDS VERIFICATION` |
| Public readiness | `DENY BY DEFAULT` |

## What belongs here

Subject to verified local conventions, this lane may contain:

- normalized two-date or multi-date land-cover comparisons;
- class-transition rasters, vectors, tables, or matrices;
- observed-derived change products with both source vintages traceable;
- model-assisted or candidate change products with model role and method explicit;
- persistence, disturbance, conversion, recovery, fragmentation, or uncertainty candidates;
- change summaries by ecoregion, habitat patch, watershed, county, grid, or another policy-approved reporting unit;
- class crosswalks or comparison sidecars needed to interpret transitions;
- processed-local manifests, digests, limitations, validation references, and correction lineage;
- generalized public-candidate derivatives that remain upstream of catalog and release.

Lane-local documentation may describe these boundaries without becoming a catalog, proof, receipt, or release authority.

## What does NOT belong here

| Do not place or claim here | Correct home or action |
|---|---|
| Source-native rasters, imagery, downloads, exports, logs, original pixels, or source identifiers | `data/raw/habitat/` |
| Differencing experiments, threshold tuning, classifier trials, scratch outputs, notebooks, unresolved QA, or redaction debugging | `data/work/habitat/` |
| Rights-unclear, role-unclear, non-comparable, disputed, malformed, unsafe, or sensitive-join material | `data/quarantine/habitat/` |
| Catalog, STAC, DCAT, PROV, or graph/triplet records | `data/catalog/` and `data/triplets/` |
| Proof bundles, receipts, source registry records, policy decisions, or release records | `data/proofs/`, `data/receipts/`, `data/registry/`, `policy/`, and `release/` |
| Released public-safe bytes, tiles, APIs, UI payloads, or downloads | `data/published/` and governed delivery interfaces |
| Species occurrences, plant specimens, sensitive biodiversity points, parcel ownership, soil truth, hydrology truth, crop truth, or hazard event truth | Their owning domain lanes; join only through governed references |
| Habitat suitability, critical-habitat designation, restoration prescription, management decision, or corridor claim | Separate object contracts, evidence, policy, review, and release path |
| Legal, ecological, agricultural, or land-management advice | Outside this processed-data lane |

## Inputs

Inputs should be governed WORK products or resolved QUARANTINE exits with, as applicable:

- stable source and artifact identity;
- `SourceDescriptor` or source-registry linkage;
- explicit source role from the Habitat role set: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`;
- source and comparison vintages;
- class-system identifiers and crosswalk support;
- spatial reference, resolution, extent, alignment, and geometry support;
- temporal observation, valid, retrieval, processing, and correction times;
- rights and sensitivity posture;
- transformation, validation, aggregation, model-run, and redaction receipts where applicable;
- uncertainty, missingness, cloud/no-data, classifier, and quality context.

A source role must not be upgraded through processing. For example, an observed source may feed a modeled change product, but the modeled product must carry its own role rather than relabeling the source.

## Outputs

Outputs are candidates for:

- parent land-cover or Habitat processed products;
- catalog and STAC/DCAT/PROV packaging;
- EvidenceBundle and proof assembly;
- graph/triplet projection;
- release-candidate review;
- public-safe generalized change layers after all downstream gates pass.

PROCESSED placement alone does not authorize any public client, map, API, UI, AI answer, or download to consume the artifact directly.

## Change semantics

Land-cover change is a **temporal comparison statement**, not a sovereign observation and not a causal conclusion.

| Concept | Required distinction |
|---|---|
| Baseline state | Land-cover class or state for the earlier declared observation or reference period. |
| Comparison state | Land-cover class or state for the later declared observation or comparison period. |
| Transition | Declared `from_class -> to_class` relation under a known class system or reviewed crosswalk. |
| Persistence | Same-class or materially unchanged result under the declared method and tolerance. |
| Disturbance | Candidate or observed-derived change indicator; not automatically a hazard, damage, or management finding. |
| Conversion | Class-transition description; not automatically legal land-use conversion or causal attribution. |
| Recovery | Method-bounded change indicator; not automatically ecological restoration success. |
| Uncertainty | Confidence, classification error, source disagreement, missingness, alignment error, or method limitation. |

Change products must preserve whether they are observed-derived, modeled, aggregate, administrative, candidate, or synthetic. A change classification must not silently impersonate regulatory status, ecological condition, or field-confirmed truth.

## Comparability contract

A candidate should fail closed or remain in WORK/QUARANTINE when the comparison cannot be supported strongly enough. At minimum, reviewers should examine:

| Comparability dimension | Expected support |
|---|---|
| Source identity | Both or all source products are identified and traceable. |
| Source role | Roles are explicit and materially compatible with the intended claim. |
| Class system | Same classification system or a reviewed, versioned crosswalk. |
| Spatial support | Compatible projection, resolution, grid alignment, geometry, extent, and generalization posture. |
| Temporal support | Declared source, observation, valid, retrieval, processing, and correction times. |
| Method | Differencing, reclassification, thresholding, model, aggregation, and post-processing steps are documented. |
| Missingness | No-data, cloud, masked, low-confidence, and unavailable regions are distinguished from unchanged land cover. |
| Uncertainty | Classification error, model confidence, crosswalk ambiguity, registration error, and edge effects are represented. |
| Digest and version | Inputs, method/spec, code/run, and output identity are reproducible or auditable. |
| Correction lineage | Superseded source vintages, corrected classes, or changed methods identify affected derivatives. |

A transition matrix is not reliable merely because its row and column totals reconcile. Shape and arithmetic checks do not prove source comparability, classification truth, ecological meaning, or release readiness.

## Sensitivity and cross-domain joins

Habitat owns landscape context, not species occurrence truth. Any join with Fauna, Flora, private parcels, rare species, rare plants, wetlands, stewardship zones, archaeology, agriculture, hazards, or steward-controlled biodiversity context must preserve ownership and sensitivity boundaries.

Fail closed when a join could expose or help infer:

- exact rare-species or rare-plant locations;
- private parcel or landowner targeting;
- nesting, den, roost, breeding, migration, or collection sites;
- sensitive wetlands, restoration sites, stewardship areas, or controlled ecological features;
- exact transform parameters, offsets, seeds, or thresholds that could reverse public-safe generalization.

Allowed downstream handling may require redaction, aggregation, generalization, delayed release, restricted access, or denial. The transform and reason must be recorded in the appropriate receipt and release context.

## Validation

Validation should cover, as applicable:

- path and responsibility-root placement;
- identity, digest, version, and deterministic naming;
- source role, rights, sensitivity, and lineage;
- class-system identity and crosswalk validity;
- temporal and spatial comparability;
- no-data, missingness, cloud, and mask handling;
- transition logic and matrix consistency;
- geometry, raster alignment, resolution, and extent;
- uncertainty and candidate-role disclosure;
- harmful-precision and cross-domain exposure checks;
- receipt, EvidenceRef, catalog, policy, correction, release, and rollback dependencies;
- links, anchors, metadata, and documentation integrity.

No complete lane-wide validator, fixture suite, CI enforcement, payload inventory, or runtime consumer was verified in this task. A passing check proves only the scope declared by that check.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes should involve Habitat, land-cover, change-detection, data, validation, evidence, sensitivity, and pipeline stewards as applicable.

Independent policy or release review is required before consequential changes involving:

- source activation or rights posture;
- classification or crosswalk semantics;
- sensitive biodiversity or parcel joins;
- public-safe geometry transforms;
- migration, correction, or invalidation of downstream products;
- public map, API, AI, tile, or download behavior.

CODEOWNERS routing, automated checks, or a documentation PR are not approval evidence.

## Correction and rollback

A corrected source vintage, class dictionary, crosswalk, algorithm, alignment method, threshold, mask, or sensitivity decision may invalidate every derivative built from it.

A governed correction should identify:

1. affected source and processed artifact identities;
2. affected comparison pairs, transition matrices, summaries, tiles, catalogs, proofs, and releases;
3. replacement or superseding artifacts;
4. correction and review records;
5. cache, index, graph, and downstream invalidation targets;
6. release and rollback disposition.

Rollback target for this README change is prior blob `12125a651e961d0d0c94864f7472d59d8dbe2e7f`. Payload or release rollback requires its own governed target and must not be inferred from this documentation rollback.

## Related folders

- Parent lanes: [`land_cover/`](../README.md) · [`habitat/`](../../README.md) · [`processed/`](../../../README.md)
- Lifecycle: [`raw/habitat/`](../../../../raw/habitat/) · [`work/habitat/`](../../../../work/habitat/) · [`quarantine/habitat/`](../../../../quarantine/habitat/)
- Discovery and graph: [`catalog/domain/habitat/`](../../../../catalog/domain/habitat/) · [`triplets/`](../../../../triplets/)
- Trust support: [`proofs/`](../../../../proofs/) · [`receipts/`](../../../../receipts/) · [`registry/sources/habitat/`](../../../../registry/sources/habitat/)
- Release and publication: [`release/candidates/habitat/`](../../../../../release/candidates/habitat/) · [`published/`](../../../../published/)
- Domain guidance: [`docs/domains/habitat/README.md`](../../../../../docs/domains/habitat/README.md) · [`Habitat Promotion Runbook`](../../../../../docs/runbooks/habitat/PROMOTION_RUNBOOK.md)
- Authority roots: [`contracts/domains/habitat/`](../../../../../contracts/domains/habitat/) · [`schemas/contracts/v1/domains/habitat/`](../../../../../schemas/contracts/v1/domains/habitat/) · [`policy/domains/habitat/`](../../../../../policy/domains/habitat/)

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and payload inventory | `NEEDS VERIFICATION` | Pinned tree, file families, LFS/external stores, rights, sensitivity, owners |
| Writers and consumers | `UNKNOWN` | Connector, pipeline, tool, workflow, API/UI, tile, AI, and deployed consumer inventory |
| Contract and schema enforcement | `UNKNOWN` | Accepted object semantics, schema versions, fixtures, validators, and negative cases |
| Change-detection implementation | `UNKNOWN` | Method specs, code, deterministic runs, thresholds, crosswalks, and receipts |
| Policy and sensitivity enforcement | `UNKNOWN` | Policy bundles, decisions, access controls, redaction/generalization tests |
| Evidence, catalog, and release closure | `UNKNOWN` | EvidenceBundles, catalog parity, reviews, manifests, correction and rollback links |
| Public serving and invalidation | `UNKNOWN` | Governed routes, hosting, caches, stale/correction/withdrawal behavior, drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and aligned to the current parent contract |
| Source-role anti-collapse | Preserved and strengthened |
| Land-cover change vs. habitat conclusions boundary | Preserved and strengthened |
| Rights, sensitivity, evidence, policy, release, correction, and rollback controls | Preserved |
| Existing accepted-content and exclusion concepts | Preserved and reorganized |
| Child and cross-domain relationships | Preserved without claiming ownership |
| Prior blob and rollback target | Recorded |
| Payload, source, schema, policy, workflow, runtime, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the lane to the current `data/processed/` authority contract;
- clarified temporal-comparison and class-transition semantics;
- added explicit comparability, sensitivity, validation, correction, and rollback controls;
- preserved uncertainty around payloads, enforcement, consumers, and release maturity;
- changed Markdown only.

[Back to top](#top)
