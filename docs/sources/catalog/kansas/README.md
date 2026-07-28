<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-readme
title: Kansas source family
type: readme; source-family-index; documentation-only
version: v0.3.0
status: repository-grounded draft; family index restored; no source activation
owners: NEEDS VERIFICATION — Docs steward + Kansas source steward + affected domain stewards
created: 2026-05-20
updated: 2026-07-28
policy_label: public-review; source-documentation-only; cite-or-abstain; fail-closed
current_path: docs/sources/catalog/kansas/README.md
truth_posture: >
  CONFIRMED current path, historical family-index identity, current sibling product
  pages, and the overwritten-index defect / PROPOSED normalized family-index and
  cross-source documentation contract / NEEDS VERIFICATION source activation,
  rights, sensitivity, runtime, review, release, and publication state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 57c1a05b07b29793a5747a25b83594b6598df812
  overwritten_blob: 9716c093e746902d7c77ca553c74aef755c7dd26
  duplicate_product_path: docs/sources/catalog/kansas/ksgs.md
  historical_family_index_blob: 75761644dd21a076863faad91c1442b88c91dd67
  bounded_exception: KFM-EXCEPTION-20260725-SOURCE-CATALOG-CORRECTION-001
related:
  - ../README.md
  - ../IDENTITY.md
  - ../PROFILES.md
  - ../RIGHTS-AND-SENSITIVITY-MAP.md
  - ../OPEN-QUESTIONS.md
  - ../../SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../doctrine/directory-rules.md
  - ../../../../data/registry/sources/
  - ../../../../connectors/kansas/
  - ../../../../policy/
  - ../../../../release/
  - ./kcds.md
tags: [kfm, sources, catalog, kansas, source-family, index, correction, mesonet, kdhe, hab, kcds, crash-data, cite-or-abstain]
notes:
  - "Restores the Kansas source-family index after the path became byte-identical to ksgs.md."
  - "KGS product content remains preserved at docs/sources/catalog/kansas/ksgs.md."
  - "This documentation change does not admit, activate, fetch, normalize, release, or publish any source."
  - "KCDS discovery page (kcds.md) added per issue #1648; documentation-only; no activation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `kansas` source family

> Human-facing index for Kansas state-scoped source documentation. This page routes readers to product pages and records cross-source boundaries; it is not a SourceDescriptor, connector, policy decision, evidence bundle, release decision, or public-data surface.

[![Status: draft index](https://img.shields.io/badge/status-draft%20index-d4a72c?style=flat-square)](#status)
[![Authority: documentation only](https://img.shields.io/badge/authority-documentation%20only-6e7781?style=flat-square)](#authority-level)
[![Index: restored](https://img.shields.io/badge/index-restored-1f883d?style=flat-square)](#status)
[![Source activation: none](https://img.shields.io/badge/source%20activation-none-b42318?style=flat-square)](#authority-level)
[![Publication: none](https://img.shields.io/badge/publication-none-b42318?style=flat-square)](#authority-level)

> [!IMPORTANT]
> The prior bytes at this path were the KGS product page and duplicated [`ksgs.md`](./ksgs.md). This revision restores the family-index identity from repository history and leaves the KGS product page at its existing canonical documentation path.

> [!CAUTION]
> Product-page presence is not source admission. Every source still requires a governed SourceDescriptor, rights and sensitivity review, bounded connector behavior, evidence, policy evaluation, review, release, correction, and rollback before public use.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Products](#product-pages) · [Cross-source semantics](#cross-source-semantics) · [Correction](#correction-and-rollback)

## Purpose

The `kansas/` source family groups documentation for Kansas state agencies, universities, museums, archives, and state-scoped observing or regulatory programs.

This index exists to:

- provide one inventory of current Kansas product pages;
- route source-specific implementation to `connectors/kansas/` or another verified connector home;
- keep source identity, source role, rights, sensitivity, temporal semantics, and domain use visible without duplicating their authoritative records;
- prevent statewide summaries, point observations, advisories, regulatory records, and modeled products from collapsing into one kind of “Kansas data”; and
- preserve correction and rollback lineage when a source page or identity is wrong.

## Authority level

**Documentation-only family index.**

| Question | Authority |
|---|---|
| Source identity and activation | `data/registry/sources/` and the governed activation process |
| Connector implementation | `connectors/kansas/` or another verified source-family connector root |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/` |
| Admissibility, rights, and sensitivity | `policy/` plus reviewed source records |
| Evidence and receipts | `data/proofs/` and `data/receipts/` |
| Catalog and triplet records | `data/catalog/` and `data/triplets/` |
| Release, correction, withdrawal, and rollback | `release/` |
| Public delivery | governed APIs and released public carriers only |

This page may describe and link those surfaces. It cannot create or override them.

## Status

| Field | Current result |
|---|---|
| Document lifecycle | `draft` |
| Family path | `docs/sources/catalog/kansas/` |
| Index identity | Restored from historical repository evidence |
| Prior defective state | `README.md` and `ksgs.md` shared blob `9716c093e746902d7c77ca553c74aef755c7dd26` |
| Historical family-index blob | `75761644dd21a076863faad91c1442b88c91dd67` |
| Current product-page inventory | Bounded indexed inventory; listed below |
| Source activation | None created by this page |
| Live network access | None |
| Rights and sensitivity closure | Per source; generally `NEEDS VERIFICATION` unless a governed record proves otherwise |
| Release or publication effect | None |
| Human review | Pending |

## What belongs here

- the Kansas source-family index;
- source-product documentation pages;
- documentation-only source-role, rights, sensitivity, identity, temporal, and correction notes;
- links to authoritative SourceDescriptors, contracts, schemas, policies, fixtures, validators, receipts, proofs, and releases;
- explicit conflicts and verification holds; and
- reversible documentation corrections.

## What does NOT belong here

- source credentials, secrets, private endpoints, signed URLs, or authenticated portal content;
- raw, quarantined, processed, catalog, triplet, proof, released, or published data payloads;
- active SourceDescriptors or source-activation decisions;
- connector, watcher, scheduler, retry, or network runtime code;
- policy rules or machine schemas;
- unsupported precise locations, personal information, protected-resource details, or sensitive-site records;
- generated language presented as evidence; or
- a claim that a product page proves source rights, accuracy, completeness, freshness, review, release, or publication.

## Inputs

This index consumes:

- current Directory Rules and accepted ADRs;
- exact repository path, blob, and sibling-page evidence;
- official public source documentation cited by the individual product pages;
- SourceDescriptor, rights, sensitivity, evidence, receipt, and release references when they exist; and
- correction records that preserve conflicting or superseded source statements.

## Outputs

This page emits only:

- reader navigation;
- a bounded product-page inventory;
- source-role and anti-collapse guidance;
- explicit uncertainty and conflict labels;
- review requirements; and
- correction and rollback instructions.

It emits no data record, policy decision, activation, validation proof, release, public map, alert, or API response.

## Validation

For this correction slice:

- [x] Confirmed that the prior family README and `ksgs.md` were byte-identical.
- [x] Recovered the historical family-index identity and product-table lineage.
- [x] Confirmed the listed sibling Markdown paths through bounded repository search.
- [x] Preserved KGS product content at [`ksgs.md`](./ksgs.md).
- [x] Added no source credential, sensitive payload, live fetch, scheduler, release, or public path.
- [x] Kept USDM, Mesonet, and KDHE HAB source roles distinct.
- [ ] Human source-steward review.
- [ ] Repository-native Markdown, links, citations, and docs-control checks on the draft pull request.

A passing documentation check proves only the checked document properties. It does not prove source admission, data quality, safety, evidence closure, or release readiness.

## Review burden

| Change | Minimum review posture |
|---|---|
| Product-list or link correction | Docs and Kansas source-family review |
| Source identity, agency, product, or cadence statement | Source steward plus evidence review |
| Rights, terms, access, or automated-ingest statement | Source-rights and policy review |
| HAB or other volatile public-safety wording | Source steward, Hydrology/Hazards, public-safety, correction, and release review |
| Mesonet station, sensor, or quality semantics | Source steward, Soil/Agriculture/Hydrology, sensor-data, and rights review |
| Source activation, connector, scheduler, release, or public use | Separate implementation and governance work; this README cannot authorize it |

## Related folders

| Responsibility | Surface |
|---|---|
| Source-catalog parent | [`docs/sources/catalog/`](../README.md) |
| Identity and profiles | [`IDENTITY.md`](../IDENTITY.md) · [`PROFILES.md`](../PROFILES.md) |
| Rights and sensitivity map | [`RIGHTS-AND-SENSITIVITY-MAP.md`](../RIGHTS-AND-SENSITIVITY-MAP.md) |
| Source descriptor standard | [`SOURCE_DESCRIPTOR_STANDARD.md`](../../SOURCE_DESCRIPTOR_STANDARD.md) |
| Kansas connectors | [`connectors/kansas/`](../../../../connectors/kansas/) |
| Source registry | [`data/registry/sources/`](../../../../data/registry/sources/) |
| Policy | [`policy/`](../../../../policy/) |
| Release and rollback | [`release/`](../../../../release/) |
| Cross-source condition semantics | [`cross-source-condition-semantics.md`](./cross-source-condition-semantics.md) |
| KDHE HAB product page | [`kdhe-harmful-algal-blooms.md`](./kdhe-harmful-algal-blooms.md) |

## ADRs

The current repository’s accepted/proposed ADR status must be checked at review time. This index relies on the existing KFM separation of source admission, lifecycle data, receipts, proofs, catalogs, release decisions, and public delivery; it does not change an ADR’s status or create a new architecture decision.

Structural placement, new connector roots, or authority migration require the applicable ADR and Directory Rules process rather than an index edit.

## Last reviewed

- **Date:** 2026-07-25
- **Evidence boundary:** `main@57c1a05b07b29793a5747a25b83594b6598df812`
- **Prior defective blob:** `9716c093e746902d7c77ca553c74aef755c7dd26`
- **Historical family-index blob:** `75761644dd21a076863faad91c1442b88c91dd67`
- **Bounded exception:** `KFM-EXCEPTION-20260725-SOURCE-CATALOG-CORRECTION-001`
- **Human review:** pending

Re-review when the sibling inventory changes, a source is activated or retired, rights or sensitivity changes, an official source corrects a material fact, or six months pass.

## Product pages

| Page | Source or product | Documentation posture |
|---|---|---|
| [`ksgs.md`](./ksgs.md) | Kansas Geological Survey | Product page; not activation |
| [`kdwp.md`](./kdwp.md) | Kansas Department of Wildlife and Parks | Product page; sensitivity review required by product |
| [`khri.md`](./khri.md) | Kansas Historic Resources Inventory | Product page; cultural sensitivity applies |
| [`kansas-memory.md`](./kansas-memory.md) | Kansas Memory | Product page |
| [`kansas-state-archives.md`](./kansas-state-archives.md) | Kansas State Archives | Product page |
| [`ksu-research-extension.md`](./ksu-research-extension.md) | K-State Research and Extension | Product page |
| [`ku-nhm.md`](./ku-nhm.md) | KU Biodiversity Institute and Natural History Museum | Product page; specimen sensitivity may apply |
| [`fhsu-sternberg.md`](./fhsu-sternberg.md) | FHSU Sternberg Museum of Natural History | Product page |
| [`kbs.md`](./kbs.md) | Kansas Biological Survey | Product page; ecological sensitivity may apply |
| [`kansas-mesonet.md`](./kansas-mesonet.md) | Kansas Mesonet | Point-station observations; rights and station-health gates |
| [`kdot.md`](./kdot.md) | Kansas Department of Transportation | Product page |
| [`kcc-oil-gas-reg.md`](./kcc-oil-gas-reg.md) | Kansas Corporation Commission oil and gas regulatory data | Product page; regulatory source role varies by product |
| [`ku-herbarium.md`](./ku-herbarium.md) | University of Kansas Herbarium | Product page; occurrence sensitivity may apply |
| [`kdhe-harmful-algal-blooms.md`](./kdhe-harmful-algal-blooms.md) | KDHE harmful-algal-bloom advisories | New documentation-only volatile advisory profile |
| [`kcds.md`](./kcds.md) | Kansas Crash Data System (KCDS) | Discovery-only; privacy/rights/API discovery; no activation; incident-level data denied; blocked by #1675 |

Absence from this table is not proof that a source is unauthorized or nonexistent. Presence is not proof that it is admitted or releasable.

## Cross-source semantics

| Source surface | Native role | Must not be silently promoted into |
|---|---|---|
| U.S. Drought Monitor | Weekly broad-scale expert-synthesis drought classification | Forecast, parcel observation, groundwater recovery, crop-loss amount, emergency declaration, or local legal restriction |
| Kansas Mesonet | Timestamped in-situ point-station observations at explicit sensor depths | Statewide drought class, gridded field truth, parcel condition, or proof that aquifers and reservoirs recovered |
| KDHE HAB advisory surfaces | Volatile agency health-advisory snapshots with possible zones and corrections | Lake-closure order, complete statewide absence finding, or whole-lake geometry when only a zone is identified |
| KCDS road-reference FeatureServer | Road network geometry for crash-report location placement | Crash-incident dataset, fatality record, person record, vehicle record, or investigation finding — this surface contains road geometry only |

See [`cross-source-condition-semantics.md`](./cross-source-condition-semantics.md) for the temporal, spatial, identity, and join rules.

## Correction and rollback

### Correction performed

The KGS page had replaced the family index at this path. The correction restores the family identity and keeps KGS content at [`ksgs.md`](./ksgs.md). No shared history is rewritten.

### Before merge

Close the draft pull request and abandon the branch.

### After merge

Revert the scoped documentation commit through a reviewed pull request. Do not delete sibling product pages, rewrite shared history, infer source deactivation, or treat a documentation revert as a data, release, alert, or publication rollback.

[Back to top](#top)
