<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-uscrn-nested-readme
title: connectors/noaa/uscrn/ — NOAA USCRN Nested Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Atmosphere steward · Soil steward · Data steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public; observation-source; not-life-safety
related:
  - ../README.md
  - ../../README.md
  - ../../noaa-uscrn/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/sources/catalog/noaa/README.md
  - ../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/soil/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, noaa, uscrn, nested-lane, ncei, climate-reference-network, atmosphere, soil, weather-station, observation, sensor-depth, source-admission, raw, quarantine, governance]
notes:
  - "Nested product-specific connector lane for NOAA U.S. Climate Reference Network intake under the canonical connectors/noaa/ family."
  - "This file does not delete, move, or supersede the draft sibling connectors/noaa-uscrn/README.md; sibling versus nested placement remains an ADR or migration-note question."
  - "Source-product doctrine belongs under docs/sources/catalog/noaa/noaa-uscrn.md and source descriptors, not here."
  - "Connector output may enter raw or quarantine admission lanes only."
  - "USCRN records are reference-grade station observations, not county/regional truth, regulatory determinations, forecasts, or alerts."
  - "Station ID, variable, cadence, timestamp, quality flags, sensor depth, units, file vintage, source URL, and digest must be preserved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA USCRN Nested Connector

> Product-specific NOAA connector lane for U.S. Climate Reference Network station-observation intake under the canonical `connectors/noaa/` connector family.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: nested connector lane" src="https://img.shields.io/badge/scope-nested__connector__lane-blue">
  <img alt="Placement: migration candidate" src="https://img.shields.io/badge/placement-migration__candidate-orange">
  <img alt="Source role: observation" src="https://img.shields.io/badge/source--role-observation-green">
  <img alt="Depth aware" src="https://img.shields.io/badge/soil-depth__aware-blue">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/noaa/uscrn/`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Relationship to sibling lane](#relationship-to-sibling-lane) · [Lifecycle sketch](#lifecycle-sketch) · [Authority boundary](#authority-boundary) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Admission posture](#admission-posture) · [Anti-collapse posture](#anti-collapse-posture) · [Validation](#validation) · [Definition of done](#definition-of-done)

---

## Scope

`connectors/noaa/uscrn/` is the nested NOAA product lane for U.S. Climate Reference Network source intake and admission helpers.

This folder may contain product-specific connector documentation, product-directory manifest builders, station metadata parsers, observation-table parsers, quality-flag helpers, soil-depth handling helpers, no-network fixture pointers, checksum/digest helpers, and raw/quarantine output adapters for USCRN products.

It must not become NOAA source-family truth, USCRN product doctrine, county climate truth, regional surface truth, regulatory determination authority, forecast authority, alert authority, policy authority, schema authority, source descriptor authority, catalog/triplet authority, proof authority, release authority, pipeline authority, public API behavior, or public UI behavior.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/noaa/uscrn/`  
> **Truth posture:** the path exists in the repository as this README; actual modules, endpoint coverage, tests, fixtures, source descriptors, CI wiring, rights status, parser behavior, quality-flag handling, sibling-lane migration, and release behavior remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── noaa/
    ├── README.md
    └── uscrn/
        └── README.md
```

Related responsibility roots:

```text
connectors/noaa/                         # canonical NOAA connector-family lane
connectors/noaa-uscrn/                   # draft sibling lane; placement/migration question
docs/sources/catalog/noaa/noaa-uscrn.md  # USCRN source-product doctrine and product boundary
docs/sources/catalog/noaa/               # NOAA source-family catalog
docs/domains/atmosphere/                 # atmosphere/air/weather observation context
docs/domains/soil/                       # soil moisture and soil temperature depth-aware context
data/registry/sources/                   # source descriptors and activation state
data/raw/                                # raw staged source outputs by owning domain
data/quarantine/                         # held material requiring source/role/quality/cadence review
data/receipts/                           # ingest, checksum, station metadata, transform, and aggregation receipts
data/proofs/                             # EvidenceBundles and proof packs
policy/rights/                           # terms, attribution, and source-use review
policy/sensitivity/                      # public-safety, infrastructure, and location-release rules
release/                                 # release decisions, manifests, rollback, correction state
```

---

## Relationship to sibling lane

This nested lane exists because `connectors/noaa/` is the canonical NOAA connector-family home and the family README allows nested product-specific lanes if an ADR or migration note consolidates NOAA siblings under the parent.

| Path | Status | Use |
|---|---|---|
| `connectors/noaa/README.md` | `CONFIRMED` parent family README | NOAA connector-family boundary and product-lane index. |
| `connectors/noaa/uscrn/README.md` | `CONFIRMED` after this update | Nested product-lane boundary for USCRN under the NOAA family. |
| `connectors/noaa-uscrn/README.md` | Existing draft sibling lane | Keep as draft/sibling reference until ADR or migration note decides final placement. |

No move, delete, rename, redirect, or deprecation is implied by this README.

---

## Lifecycle sketch

```mermaid
flowchart LR
  SRC[NOAA/NCEI USCRN source surface] --> CONN[connectors/noaa/uscrn]
  CONN --> RAWA[data/raw/atmosphere]
  CONN --> RAWS[data/raw/soil]
  CONN --> QUAR[data/quarantine/<domain>]

  RAWA --> NEXT[downstream governed stages]
  RAWS --> NEXT
  QUAR --> REVIEW[source / quality / cadence / depth review]

  NEXT -. outside this connector .-> WORK[data/work]
  NEXT -. outside this connector .-> PROC[data/processed]
  NEXT -. outside this connector .-> CAT[data/catalog + data/triplets]
  NEXT -. outside this connector .-> PUB[data/published]

  PUB -. served only through .-> API[apps/governed-api]
  API -. public rendering .-> UI[apps/explorer-web]
```

> [!CAUTION]
> Connector code admits source material. It does not interpolate stations into surfaces, turn point observations into county truth, aggregate cadence levels, publish layers, answer public claims, or decide release state. Promotion remains a governed state transition, not a file move.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/<domain>/<source_id>/<run_id>/
  data/quarantine/<domain>/<source_id>/<run_id>/

NOT HERE:
  NOAA source-family truth
  USCRN product doctrine
  station-as-area truth
  climate-normal authority
  forecast or alert authority
  regulatory determination authority
  source descriptor authority
  rights or sensitivity policy
  processed station derivatives
  catalog records
  triplet records
  public tiles or map artifacts
  receipts/proofs as authority
  release decisions
  published artifacts
  public API behavior
  public UI behavior
```

---

## Inputs

| Accepted item | Required posture |
|---|---|
| Product manifest helper | Preserve source URL, product directory, cadence, filename, station ID, year or period, size, checksum, and retrieval time. |
| Station metadata parser | Preserve station ID, name, latitude, longitude, elevation, state, commissioning status, and source metadata. |
| Observation-table parser | Preserve timestamp, timezone convention, station ID, variable, value, units, quality flags, and missing-value codes. |
| Soil-depth parser | Preserve soil moisture or soil temperature depth as a required dimension; never collapse depths. |
| Cadence helper | Preserve sub-hourly, hourly, daily, monthly, or derived-product cadence as source-significant metadata. |
| Quality-flag helper | Preserve raw observations, calculated values, and quality-control flags separately. |
| Derived-product helper | Preserve source-defined derived product identity, algorithm/version notes, and source documentation references. |
| Rights/citation helper | Preserve source terms, citation, attribution posture, and review status. |
| Test references | Point to owning fixture/test roots; fixtures do not become source authority. |

---

## Exclusions

| Do not store here | Correct home |
|---|---|
| USCRN source-product doctrine | `docs/sources/catalog/noaa/noaa-uscrn.md` |
| NOAA source-family documentation | `docs/sources/catalog/noaa/` |
| Authoritative `SourceDescriptor` records | `data/registry/sources/` |
| Atmosphere or Soil doctrine | `docs/domains/atmosphere/`, `docs/domains/soil/` |
| Alerting, public-safety, sensitivity, or release policy | `policy/`, `policy/sensitivity/`, `release/` |
| Processed station derivatives or interpolations | `data/processed/` |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Tile packages or public map artifacts | `data/published/` after governed release |
| Receipts and proof packs as authority | `data/receipts/`, `data/proofs/` |
| Schemas or semantic contracts | `schemas/`, `contracts/` |
| Generated reports | `artifacts/` |
| Public UI or API behavior | `apps/governed-api/`, `apps/explorer-web/` |

---

## Admission posture

USCRN intake should preserve:

- source identity and source surface;
- source descriptor reference and source activation state;
- product directory, cadence, product type, year/period, and file vintage;
- station ID, station metadata, location, elevation, and status fields;
- timestamp, timezone convention, variable, value, units, missing-value code, and quality flag;
- soil depth and soil layer where applicable;
- raw observation versus calculated/derived value status;
- retrieval timestamp, response status, file identity, and content digest;
- rights/citation/attribution posture;
- domain-lane routing hint such as atmosphere or soil;
- public-safety limitation notes;
- quarantine reason when review is required.

---

## Anti-collapse posture

USCRN has several high-risk interpretation boundaries. Keep them visible at connector admission time.

| Rule | Connector implication |
|---|---|
| Station reading is not area truth. | Do not emit county, watershed, region, or raster values without downstream aggregation or modeling receipts. |
| Depth matters. | Soil moisture/temperature at 5 cm, 10 cm, 20 cm, 50 cm, and 100 cm must stay distinct when present. |
| Cadence matters. | Sub-hourly, hourly, daily, monthly, and derived products are distinct artifacts. |
| Quality flags matter. | Do not drop QC flags, missing codes, or calculated-value conditions. |
| Reference-grade is not regulatory. | Do not treat USCRN as legal compliance or alert authority. |
| Derived products are not raw observations. | Preserve source-defined derived-product identity and algorithm/version context. |
| Public display is downstream. | The connector must not build public tiles, UI layers, climate claims, or alert payloads. |

---

## Validation

Before relying on this nested lane, verify:

- the nested path is intentionally kept and documented by ADR, migration note, or updated Directory Rules;
- whether `connectors/noaa-uscrn/` remains, redirects here, or is migrated later;
- source descriptors exist and are active for USCRN source surfaces;
- NOAA/NCEI rights, citation, attribution, endpoint, and distribution posture are captured in source descriptors;
- current product directories, product docs, headers, change log, cadence, field names, units, quality flags, and file naming conventions are re-verified;
- parsers preserve station ID, timestamp, cadence, variable, units, quality flags, missing codes, and derived/raw status;
- soil-depth parsing preserves depth and layer metadata without collapse;
- tests use no-network fixtures where practical;
- output paths are limited to raw/quarantine admission lanes;
- downstream receipts, proofs, catalog/triplet records, tile artifacts, and release records are produced only outside this connector;
- public products are released only through governed publication controls and never as alerts or area truth without downstream receipts.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Nested versus sibling placement is resolved or recorded in the drift/open-question register.
- [ ] Actual connector contents are inventoried.
- [ ] NOAA USCRN `SourceDescriptor` IDs and source-family activation are verified.
- [ ] NOAA/NCEI rights, citation, attribution, source terms, endpoint, and current product-directory posture are documented.
- [ ] Manifest builders preserve source URL, product directory, cadence, station ID, data year/period, file identity, size, and digest.
- [ ] Parsers preserve station metadata, timestamp, variable, value, units, quality flags, missing codes, soil depth, raw/derived status, and product vintage.
- [ ] Tests prevent silent conversion of station readings into area truth, depth-collapsed soil values, cadence-collapsed values, regulatory determinations, or alert claims.
- [ ] Outputs are verified to enter only raw or quarantine admission lanes.
- [ ] No source-family, domain, processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, report, API, UI, tile, alert, area-truth, or regulatory authority lives here.
- [ ] Tests, fixtures, and CI behavior are verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/noaa/uscrn/` is for nested NOAA USCRN source-admission code only. It is not source-family truth, regional climate truth, soil-column truth, forecast authority, alert authority, regulatory authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, tile publication authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
