<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-uscrn-readme
title: connectors/noaa-uscrn/ — NOAA USCRN README-Only Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Atmosphere steward · Soil steward · Agriculture liaison · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; connector-boundary; noaa; uscrn; station-observation; depth-aware; placement-open; not-life-safety; no-publication
truth_posture: CONFIRMED README-only sibling / PROPOSED placement / INACTIVE source authority / IMPLEMENTATION NEEDS VERIFICATION
evidence_snapshot: main@92ddac60a5dd7ec4c1f4704c651bd173423afbaf
related:
  - ../README.md
  - ../noaa/README.md
  - ../noaa/src/README.md
  - ../noaa/tests/README.md
  - ../noaa/uscrn/README.md
  - ../../docs/sources/catalog/noaa/README.md
  - ../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../docs/sources/catalog/noaa/station-climate-products.md
  - ../../docs/architecture/source-roles.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/directory-rules.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/soil/noaa-uscrn.yaml
  - ../../data/registry/sources/agriculture/noaa-uscrn.yaml
  - ../../pipelines/domains/soil/uscrn_ingest/README.md
  - ../../contracts/domains/soil/soil_moisture_observation.md
tags: [kfm, connectors, noaa, uscrn, climate-reference-network, weather-station, observation, depth-aware, cadence-aware, source-admission, raw, quarantine, governance]
notes:
  - "This file documents a proposed connector boundary; it does not prove executable NOAA USCRN connector code."
  - "The repository also contains connectors/noaa/uscrn/ under the declared NOAA family lane; this README does not settle sibling versus nested placement."
  - "The two domain-specific noaa-uscrn registry YAMLs are PROPOSED inventory placeholders, not mature active SourceDescriptors."
  - "USCRN station records remain point observations with station, variable, unit, time, cadence, quality, depth, product-vintage, and raw/derived distinctions intact."
  - "A station observation is not county, watershed, regional, raster, soil-column, regulatory, forecast, alert, or life-safety truth."
  - "Connector output is limited to RAW or QUARANTINE handoff and never grants downstream publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA USCRN README-Only Connector Boundary

> Boundary for proposed NOAA U.S. Climate Reference Network (USCRN) source admission at `connectors/noaa-uscrn/`. Repository evidence at the pinned snapshot proves this README, not a runnable product connector. Final placement between this sibling and `connectors/noaa/uscrn/` remains unresolved.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: not proven" src="https://img.shields.io/badge/implementation-not__proven-lightgrey">
  <img alt="Placement: open" src="https://img.shields.io/badge/placement-open-orange">
  <img alt="Scope: station observations" src="https://img.shields.io/badge/scope-station__observations-blue">
  <img alt="Area truth: denied" src="https://img.shields.io/badge/area__truth-denied-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Truth posture:** `CONFIRMED` README-only sibling · `PROPOSED` placement · source authority `INACTIVE / NOT ESTABLISHED` · product-specific runtime `NEEDS VERIFICATION`.

> [!CAUTION]
> A USCRN record is a station-, variable-, time-, cadence-, unit-, quality-, and, where applicable, depth-scoped observation. Reference-grade station data is not automatically area truth, soil-column truth, a regulatory determination, a forecast, an alert, or life-safety guidance.

**Quick jumps:** [Purpose](#1-purpose) · [Status](#3-status) · [Validation](#8-validation) · [Topology](#connector-topology-and-placement) · [Observation boundary](#station-observation-boundary) · [Runtime contract](#proposed-runtime-contract) · [Evidence](#evidence-ledger) · [Backlog](#verification-backlog)

---

## 1. Purpose

`connectors/noaa-uscrn/` defines a conservative source-admission boundary for USCRN station metadata, observation products, source-defined calculated or aggregate products, and their provenance.

If executable code is later approved here, it may discover or retrieve an explicitly configured source object, preserve its native bytes and station/product identity, validate only admission preconditions, and hand the result to a domain-owned `RAW` or `QUARANTINE` lane. This README does not activate a source, select a live endpoint, establish current variables/depths/cadences/formats, or prove that product-specific code exists.

The boundary is narrow:

```text
configured USCRN source object
           |
           v
bounded retrieval and integrity checks
           |
           v
station/product-preserving admission
  station + variable + time + cadence + unit + QC + depth + vintage
           |
           +----> RAW         only when admission preconditions pass
           |
           `----> QUARANTINE  when identity, structure, depth, cadence,
                              integrity, quality, rights, or routing is unresolved
```

[Back to top ↑](#top)

---

## 2. Authority level

**Authority: IMPLEMENT boundary documentation; no source, scientific-interpretation, or publication authority.**

This README may describe what a future connector at this path is allowed to do. It may not:

- ratify this sibling as the canonical USCRN implementation home;
- override `connectors/noaa/` as the declared NOAA family lane;
- supersede the nested `connectors/noaa/uscrn/` README;
- activate either domain-specific registry placeholder;
- promote the NOAA family scaffold into a working USCRN connector by declaration;
- choose Soil, Agriculture, Atmosphere, or another domain registry path as source authority;
- select between conflicting SourceDescriptor schema locations;
- define variable, unit, quality, missing-value, station, cadence, or depth semantics independently of accepted source and domain contracts;
- interpolate, aggregate, gap-fill, compare, or normalize records into area or soil-column truth;
- decide regulatory, forecast, alert, drought, crop, hydrologic, or life-safety meaning;
- promote data beyond source admission;
- create release authority or public behavior.

The two Directory Rules copies agree on the connector lifecycle limit but differ in version and status. This README relies only on their shared rule: connectors fetch and parse source material and may write to `RAW` or `QUARANTINE`, not later lifecycle stages. It does not decide which Directory Rules file is authoritative.

---

## 3. Status

| Question | Evidence-backed status |
|---|---|
| Does `connectors/noaa-uscrn/README.md` exist? | **CONFIRMED.** |
| Is executable code proven in this exact lane? | **No.** Bounded probes found no package file, source root, client, parser, initializer, or test README. |
| Does a nested USCRN connector boundary exist? | **Yes.** `connectors/noaa/uscrn/README.md` exists and is also README-only in bounded implementation probes. |
| Is the NOAA family lane canonical? | **Yes, as repository doctrine.** `connectors/noaa/README.md` declares the family lane canonical while preserving this sibling as migration-pending. |
| Does the NOAA package prove USCRN runtime support? | **No.** It is version `0.0.0`; the initializer is empty, fetch/admit files are placeholder comments, the local descriptor has `TBD` role and rights, and the proposed `products/uscrn.py` file was not found. |
| Are USCRN registry records present? | **Two placeholders are present.** Soil and Agriculture each contain a minimal `PROPOSED` `noaa-uscrn.yaml`; neither carries mature descriptor fields or establishes activation. |
| Is USCRN active in the source-authority register? | **No.** The register is `PROPOSED` and its `entries` list is empty. |
| Is the named Soil ingest pipeline implemented? | **Not proven.** Its README describes an intended executable lane, but bounded probes found no initializer, pipeline module, or documented declarative spec. |
| Is an enforceable Soil moisture schema proven? | **No.** The draft soil-moisture observation contract explicitly reports its paired schema missing. |
| Are RAW captures, fixtures, product-specific tests, CI, receipts, and release wiring proven? | **No.** Named RAW/fixture probes returned no README files, and documentation does not prove operational evidence. |

Absence statements above are limited to named repository paths inspected at `main@92ddac60a5dd7ec4c1f4704c651bd173423afbaf`; they are not claims of an exhaustive recursive inventory.

---

## 4. What belongs

If this path is ratified, it may contain product-specific connector artifacts such as:

- request, directory, manifest, or object-discovery adapters that take an approved SourceDescriptor reference;
- bounded retrieval helpers with explicit timeouts, retries, redirect policy, and maximum size;
- checksum, content-length, source-file, and source-fingerprint verification;
- lossless capture of source files, headers, documentation references, change metadata, and station metadata;
- observation parsing that preserves station, variable, value, unit, timestamp, timezone, cadence, quality, and missing-value state;
- depth-aware parsing that retains the source-exposed depth coordinate and units without substitution;
- product classification that keeps native observation, calculated, corrected, and aggregate products distinct;
- deterministic RAW or QUARANTINE handoff envelopes;
- sanitized process receipts that reference, rather than redefine, governing records;
- no-network fixtures representing approved structural cases;
- unit and contract tests for source admission and anti-collapse behavior.

Every artifact must preserve source and station identity and fail closed when required evidence is missing or contradictory.

---

## 5. What does NOT belong

| Excluded responsibility | Governing surface or next decision |
|---|---|
| Canonical connector placement | Directory decision or accepted ADR with migration and rollback; do not infer it from duplicate README paths. |
| NOAA family or USCRN product doctrine | `docs/sources/catalog/noaa/` and the USCRN product page. |
| Source activation | `control_plane/source_authority_register.yaml` plus approved descriptors and review. |
| Registry topology authority | Resolve Soil/Agriculture/Atmosphere or source-family placement outside this connector. |
| SourceDescriptor schema authority | Resolve the documented source-schema conflict outside this README. |
| Station, observation, or soil-moisture contract authority | Accepted domain contracts and schemas. |
| Interpolation, gap-fill, gridding, or area aggregation | Downstream modeled/aggregate pipelines with method and scope receipts. |
| Climate normals, anomalies, drought indices, or derived trends | Source-defined or downstream aggregate/model artifacts with distinct identity. |
| Cross-source comparison or validation result | Downstream comparison artifacts with their own evidence and receipts. |
| Regulatory, compliance, forecast, warning, or life-safety decisions | Official authorities; never this connector. |
| Crop, yield, irrigation, watershed, or regional condition truth | Domain pipelines and evidence after governed derivation. |
| Normalized or processed station products | Downstream domain pipelines after admission. |
| Catalog, triplet, tile, or published artifacts | Governed lifecycle and release surfaces. |
| Rights, sensitivity, or public-safety decisions | `policy/` and release review. |
| EvidenceBundle closure | Downstream proof processes; connector receipts are process evidence only. |
| Public API, UI, map, notification, or generated-answer behavior | Governed application surfaces after release. |

---

## 6. Inputs

A future connector invocation should accept only explicit, governed inputs. At minimum:

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Required before retrieval; must resolve to an approved source identity, product scope, and activation posture. |
| Product identity | Preserve source family, product family, cadence/product class, period or file vintage, and any source-exposed version. |
| Approved source locator | Treat as configuration, not a hard-coded claim in this README. Redact credentials and sensitive query material. |
| Expected object identity | Preserve filename/object key, station or product scope, expected size when known, checksum algorithm/digest when known, and source metadata. |
| Retrieval policy | Bound schemes, hosts, redirects, timeouts, retries, pagination/listing, maximum object size, and resume behavior. |
| Station identity policy | Preserve source station ID and station-metadata vintage; do not silently remap, merge, or split stations. |
| Observation interpretation | Preserve variable, unit, time basis, cadence, quality/missing state, depth coordinate, and raw/calculated/aggregate classification as exposed. |
| Routing context | Name the owning domain and proposed RAW/QUARANTINE destination without granting downstream promotion. |
| Rights and attribution reference | Carry governing record identifiers and unresolved review state; do not decide rights locally. |

Live endpoints, product directories, file formats, headers, variables, units, missing codes, quality flags, cadence values, available depths, station inventory, coverage, access requirements, rights, and citation details are version-sensitive external facts. They must be verified in product-specific evidence before implementation or activation; this README intentionally does not pin them.

---

## 7. Outputs

The connector may emit only an atomic source-admission handoff to one of:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

The exact layout remains subject to governing repository contracts. Conceptually, a handoff should include:

- byte-preserving source payload or an immutable reference permitted by policy;
- source headers, documentation/change references, and station metadata as applicable;
- a sanitized request/retrieval manifest;
- source, product, cadence/product class, period/file, station, and record identity;
- native timestamp/timezone fields and normalized parse candidates kept distinguishable;
- variable, value, unit, quality flag, missing-value state, and raw/calculated/aggregate status;
- source-exposed depth coordinate and units for depth-aware variables;
- station location/elevation/status and metadata vintage where exposed and permitted;
- source and content fingerprints;
- observed size and checksum results;
- retrieval, correction, supersession, and product-vintage metadata;
- rights, attribution, sensitivity, and public-safety references or unresolved flags;
- validation results and deterministic quarantine reasons;
- owning-domain routing and run identity.

The connector must not emit directly to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLETS`, `PUBLISHED`, release, API, UI, notification, or generated-answer surfaces.

---

## 8. Validation

Validation is source admission validation, not scientific interpretation, spatial representativeness, regulatory validation, or publication approval.

### Required checks

- source identity and SourceDescriptor revision resolve and are approved for use;
- product, cadence/product class, period/file, station, and record identity are present where applicable;
- retrieval follows configured scheme, host, redirect, timeout, retry, listing/pagination, and size constraints;
- payload is complete, expected headers/columns are understood, and content digest is recorded;
- archives and multi-file packages are bounded and safe to materialize;
- station ID and station-metadata vintage are retained without silent remapping;
- timestamps, timezone conventions, cadence, and aggregation interval remain explicit;
- variables, values, units, quality flags, and missing-value states remain source-traceable;
- depth-aware values carry depth coordinate and units and cannot substitute one depth for another;
- native observations, source-calculated values, corrections, summaries, and aggregates remain distinct;
- source-file vintage, correction, and supersession information is preserved;
- station records cannot become county, watershed, regional, raster, or soil-column truth during admission;
- rights, attribution, sensitivity, and routing references are present or the object is quarantined;
- output destination is limited to RAW or QUARANTINE;
- logs and receipts contain no credentials, signed URLs, unsafe payload excerpts, or sensitive station/operational detail beyond approved policy.

### Quarantine conditions

Quarantine on missing, ambiguous, or conflicting evidence, including:

- unresolved source, product, cadence, period/file, station, or record identity;
- checksum, size, member-list, header, row-count, or package mismatch;
- unreadable, truncated, structurally unsafe, or partially retrieved content;
- unexpected header, column, variable, unit, quality-flag, missing-code, or source-schema drift;
- missing, unsupported, contradictory, or unit-ambiguous depth metadata;
- stale, future-dated, timezone-ambiguous, conflicting, or unsupported timestamps;
- silent cadence or interval substitution;
- unresolved raw/calculated/aggregate/corrected product classification;
- station metadata conflict or unreviewed station identity change;
- unresolved rights, attribution, sensitivity, or domain routing;
- duplicate identity with different bytes;
- any attempt to treat the connector as interpolation, alert, regulatory, promotion, or publication authority.

An empty, missing, delayed, or partial source object is not proof of zero precipitation, normal conditions, no soil moisture, no drought, or safe conditions.

### No-network test posture

Tests should be deterministic and no-network by default. Fixtures should cover, at minimum:

- a structurally valid station observation with units, quality, cadence, and time metadata;
- a valid depth-aware soil observation and a non-depth variable;
- checksum, size, header, row-count, and archive-safety failures;
- missing or conflicting source/product/station/file identity;
- unknown or changed columns, units, quality flags, and missing codes;
- timezone ambiguity, cadence mismatch, correction, and supersession;
- missing depth, depth-unit ambiguity, and attempted depth substitution;
- attempted hourly/daily/monthly substitution without an aggregation receipt;
- raw observation versus calculated/aggregate product confusion;
- station-as-county, station-as-watershed, station-as-raster, and soil-column collapse attempts;
- empty or partial products that must not become zero or all-clear claims;
- duplicate source identity with identical bytes and with conflicting bytes;
- rights, sensitivity, or routing state that forces quarantine;
- credential and signed-URL redaction;
- rejection of every output destination beyond RAW or QUARANTINE;
- rejection of regulatory, warning, forecast, or life-safety output.

---

## 9. Review burden

Changes here require review proportional to their effect:

| Change | Minimum review burden |
|---|---|
| README clarification with no authority change | Connector steward, NOAA source steward, and docs review. |
| Placement, rename, merge, redirect, or removal of either USCRN lane | Architecture/governance review and accepted migration decision. |
| Registry placement or descriptor change | Source governance plus Atmosphere, Soil, and affected domain review. |
| New endpoint, access method, credential flow, or retrieval behavior | Source steward, security review, rights review, and no-network tests. |
| New format, header, variable, unit, quality flag, cadence, depth, or station metadata behavior | Source, Atmosphere, Soil, spatial, and validation review with versioned fixtures. |
| Source-role or raw/calculated/aggregate mapping | Source-role governance and domain contract review; never connector-only approval. |
| Hash, deduplication, replay, correction, or quarantine change | Data/validation review with deterministic regression tests. |
| Aggregation, interpolation, gap-fill, comparison, trend, or cross-domain use | Downstream pipeline, evidence, policy, and domain review. |
| Activation, promotion, public display, or operational use | Source authority, rights, proof, and release review outside this lane. |

`OWNER_TBD` must be replaced before operational activation. The global CODEOWNERS file does not establish a NOAA USCRN-specific owner at the pinned snapshot.

---

## 10. Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Root connector boundary and RAW/QUARANTINE limit. |
| [`../noaa/README.md`](../noaa/README.md) | Declared canonical NOAA connector-family boundary. |
| [`../noaa/src/README.md`](../noaa/src/README.md) | Proposed NOAA source-root contract; not product implementation proof. |
| [`../noaa/tests/README.md`](../noaa/tests/README.md) | Proposed no-network family test contract; not passing-test proof. |
| [`../noaa/uscrn/README.md`](../noaa/uscrn/README.md) | Parallel nested README-only USCRN connector boundary. |
| [`../../docs/sources/catalog/noaa/README.md`](../../docs/sources/catalog/noaa/README.md) | NOAA source-family catalog context. |
| [`../../docs/sources/catalog/noaa/noaa-uscrn.md`](../../docs/sources/catalog/noaa/noaa-uscrn.md) | Draft USCRN product doctrine and open questions. |
| [`../../docs/sources/catalog/noaa/station-climate-products.md`](../../docs/sources/catalog/noaa/station-climate-products.md) | Broader draft station/climate product boundary; distinct from USCRN. |
| [`../../docs/architecture/source-roles.md`](../../docs/architecture/source-roles.md) | Source-role vocabulary and anti-collapse context. |
| [`../../data/registry/sources/soil/noaa-uscrn.yaml`](../../data/registry/sources/soil/noaa-uscrn.yaml) | Minimal `PROPOSED` Soil inventory placeholder, not active descriptor proof. |
| [`../../data/registry/sources/agriculture/noaa-uscrn.yaml`](../../data/registry/sources/agriculture/noaa-uscrn.yaml) | Minimal `PROPOSED` Agriculture inventory placeholder, not active descriptor proof. |
| [`../../pipelines/domains/soil/uscrn_ingest/README.md`](../../pipelines/domains/soil/uscrn_ingest/README.md) | Draft downstream Soil ingest boundary; executable behavior remains unproven. |
| [`../../contracts/domains/soil/soil_moisture_observation.md`](../../contracts/domains/soil/soil_moisture_observation.md) | Draft depth/unit/QC-aware semantic contract; paired schema reported missing. |
| [`../../contracts/domains/atmosphere/WeatherObservation.md`](../../contracts/domains/atmosphere/WeatherObservation.md) | Draft Atmosphere observation semantics; not connector authority. |
| [`../../contracts/domains/atmosphere/WeatherStation.md`](../../contracts/domains/atmosphere/WeatherStation.md) | Draft station semantics; not source activation proof. |

---

## 11. ADRs

- [`../../docs/adr/README.md`](../../docs/adr/README.md) is the ADR index and process surface.
- [`../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md`](../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) records the connector-output proposal; its draft/proposed state does not independently create authority.
- No accepted USCRN connector-placement or registry-topology ADR was identified in the bounded evidence review.
- [`../../docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) had no `noaa-uscrn`, `NOAA USCRN`, or `uscrn` text match in a bounded scan. That does not mean the path/registry drift is resolved or exhaustively audited.

Required decisions before product-specific implementation or activation:

1. Choose the canonical USCRN connector topology and define redirects or deprecation for the non-canonical path.
2. Choose the canonical source registry ownership or establish one source-family descriptor referenced by domain projections.
3. Resolve SourceDescriptor schema authority and activation records.
4. Define accepted station/observation/soil contracts and enforceable schemas.
5. Define current access, product/header, station identity, time, cadence, quality, missing-value, depth, correction, rights, and routing rules.
6. Define owner, fixture, validator, pipeline, comparison, correction, and rollback responsibilities.

This README does not pre-decide any of those outcomes.

---

## 12. Last reviewed

**2026-07-14**, against repository snapshot `main@92ddac60a5dd7ec4c1f4704c651bd173423afbaf`.

Review scope was bounded to the named connector, nested connector README, NOAA family scaffold, source catalog, rules, source authority, the two domain registry placeholders, source-schema contract, named Soil pipeline paths, Soil observation contract, named RAW/fixture paths, drift, ownership, and workflow surfaces cited here. Re-review after any topology decision, source activation, descriptor/schema migration, source-interface change, station/header/cadence/depth change, rights change, or executable implementation.

---

## Connector topology and placement

Repository evidence exposes two connector homes:

| Path | Observed state | Safe interpretation |
|---|---|---|
| `connectors/noaa/` | Declared canonical NOAA family lane; package is a `0.0.0` greenfield scaffold. | Family coordination and future implementation root, not current USCRN runtime proof. |
| `connectors/noaa-uscrn/` | This README exists; named implementation probes found no code or tests. | Proposed hyphenated product sibling. |
| `connectors/noaa/uscrn/` | A parallel README exists; named implementation probes found no code or tests. | Proposed nested product lane under the NOAA family. |
| `connectors/noaa/src/noaa/products/uscrn.py` | Bounded probe returned no file. | Proposed module named by source-root docs, not implemented evidence. |

Directory Rules §7.3 lists the `noaa/` family. The NOAA family README calls its family lane canonical while treating this sibling as draft and migration-pending. Do not copy code across lanes, split variables/domains by connector path, create import aliases, delete either README, or move descriptors until an accepted decision covers lineage, redirects, deprecation, tests, activation, correction, and rollback.

### Registry topology

Two domain-specific YAML paths exist:

| Registry path | Observed content | Safe interpretation |
|---|---|---|
| `data/registry/sources/soil/noaa-uscrn.yaml` | `PROPOSED` plus path/source-doc/placeholder notes. | Inventory scaffold, not a conforming active descriptor. |
| `data/registry/sources/agriculture/noaa-uscrn.yaml` | `PROPOSED` plus path/source-doc/placeholder notes. | Inventory scaffold, not a conforming active descriptor. |

Neither record contains mature identity, source role, rights, cadence, retrieval, citation, hash, review, or activation fields. Their coexistence does not establish separate source truth by domain. Resolve whether USCRN has one source-family descriptor with domain projections or another governed topology; do not duplicate source authority in this connector.

---

## Station observation boundary

### Point scope, not area truth

Every admitted native record must remain attached to its source station, variable, time, and measurement support. A station point does not by itself represent a county, watershed, farm, habitat, road segment, raster cell, region, or state.

Any spatial interpolation, nearest-station assignment, areal average, gap-fill, or gridded surface is a separate modeled or aggregate artifact with its own method, scope, validation, uncertainty, evidence, and receipt. Rendering a point value on a map does not change this boundary.

### Depth distinctness

For depth-aware variables, preserve the source-exposed depth value, unit, reference convention, sensor/variable identity, and quality state. A value at one depth must not substitute for another or become an unqualified soil-column value. If depth is required but missing, ambiguous, unsupported, or conflicting, quarantine.

This README intentionally does not pin a current depth set; available depths and their conventions are product-specific external facts requiring current verification.

### Cadence and time distinctness

Do not collapse:

```text
source observation time
!= source aggregation interval or product period
!= source issue/file vintage
!= KFM retrieval time
!= processing/catalog/release time
!= correction or supersession time
```

Sub-hourly, hourly, daily, monthly, normal, anomaly, or other product classes are distinct artifacts when supplied. Aggregating or disaggregating them requires downstream methods and receipts; filename labels alone are insufficient to infer semantics.

### Quality, units, and missingness

- preserve native variable identifiers and source headers;
- preserve units with every value and never infer conversions silently;
- preserve quality flags, calculated-value markers, and source status fields;
- preserve missing-value codes as missingness, never as zero;
- distinguish raw/native observations from source-calculated, corrected, summary, or aggregate products;
- retain parser/header/source-document version assumptions;
- quarantine unknown flags, units, headers, or missing codes until reviewed.

### Station identity and change

Preserve source station ID and metadata vintage. Station relocation, instrument/sensor changes, siting changes, calibration changes, commissioning/decommissioning, metadata corrections, or identifier remapping—when exposed—must create visible lineage, not silent historical rewriting.

### Required anti-collapse rules

- reference-grade does not mean ubiquitous spatial coverage;
- observation does not mean area, regulatory, forecast, or alert authority;
- a comparison target does not make USCRN the comparison result;
- station validation use does not transfer USCRN’s source role to another source;
- soil moisture/temperature does not by itself establish drought, crop stress, irrigation need, yield, or watershed condition;
- empty, missing, delayed, or quality-rejected records do not prove zero or normal conditions;
- RAW presence does not imply validation, release, or public eligibility.

---

## Proposed runtime contract

No product-specific runtime is proven at either connector path. If implementation is approved, it should follow these fail-closed phases:

1. **Resolve** an approved SourceDescriptor revision, product scope, and source locator.
2. **Plan** a bounded request/listing without exposing credentials, signed material, or unsafe parameters.
3. **Retrieve** into temporary storage with size, timeout, redirect, pagination/listing, and retry limits.
4. **Verify** response identity, byte length, digest, archive members, headers, and source metadata.
5. **Parse** station/product records while preserving native identifiers, time, cadence, units, quality, missingness, depth, and product class.
6. **Inspect** structural and semantic admission invariants without interpolation, aggregation, or source-role rewriting.
7. **Decide** RAW versus QUARANTINE using deterministic admission rules.
8. **Commit** the handoff atomically so partial objects never appear complete.
9. **Record** sanitized process evidence and source/content fingerprints.

Retry only transient, bounded failures. Do not retry authentication failure, forbidden access, station/header/unit/quality/depth contradiction, unsafe archive structure, deterministic checksum mismatch, unsupported source drift, or unresolved policy state as though those were network transients.

### Idempotency, deduplication, correction, and replay

- source identity is not only a URL, filename, station ID, or date;
- a locator with changed bytes must create a new reviewable identity or correction lineage;
- identical verified bytes may be deduplicated only through a governed immutable-reference mechanism;
- duplicate source identity with conflicting bytes must quarantine;
- corrected, revised, or superseded files must not overwrite prior captures;
- replay must pin descriptor revisions, retrieval policy, header/parser assumptions, validation version, and output target;
- replay must preserve prior outcomes and quarantine reasons;
- caches may accelerate retrieval but never substitute for integrity, freshness, or provenance checks.

---

## Evidence ledger

| Evidence surface | Observed state | What it supports | What it does not support |
|---|---|---|---|
| This README | Prior v0.1 draft exists. | A documented hyphenated product boundary. | Code, activation, source access, or canonical placement. |
| Nested USCRN README | Draft README exists under `connectors/noaa/uscrn/`. | A parallel nested boundary. | A resolved topology or runnable connector. |
| NOAA family README | Calls `connectors/noaa/` canonical and this lane draft/migration-pending. | Source-family-first placement posture. | A final product home or working implementation. |
| NOAA package files | `0.0.0` placeholder; empty initializer; placeholder fetch/admit; descriptor role/rights `TBD`. | Greenfield family scaffolding exists. | USCRN parser, package readiness, active descriptor, or endpoint behavior. |
| Draft USCRN product page | Station/depth/cadence/quality anti-collapse doctrine and open questions. | Required semantic caution and proposed native observation role. | Current endpoints, station inventory, depths, cadence, rights, or accepted implementation. |
| Source-authority register | `PROPOSED`; `entries: []`. | No repository-level USCRN activation at snapshot. | Future activation status. |
| Soil registry YAML | Minimal `PROPOSED` inventory placeholder. | A candidate domain registry path. | Mature SourceDescriptor or activation. |
| Agriculture registry YAML | Minimal `PROPOSED` inventory placeholder. | A second candidate domain registry path. | Mature SourceDescriptor or separate source authority. |
| Soil USCRN pipeline README | Detailed draft pipeline boundary. | Intended downstream normalization separation. | Pipeline code, spec, schedule, tests, CI, or release wiring. |
| Soil moisture observation contract | Draft semantics; paired schema reported missing. | Depth/unit/QC requirements have a candidate contract home. | Enforceable schema validation. |
| Connector/source-descriptor workflows | Inspected workflows are TODO echo-only stubs. | No meaningful automated connector/descriptor gate is proven. | Runtime or activation readiness. |
| CODEOWNERS | Global placeholder; no NOAA USCRN-specific rule identified. | Owner remains unresolved. | Operational accountability. |

---

## Rights, sensitivity, and public safety

Repository documentation is not a substitute for current source terms. Before activation, governing records must verify licensing or terms, attribution, redistribution, caching, service constraints, access method, intended use, and product-specific restrictions.

The connector must:

- carry rights, attribution, sensitivity, and review record identifiers;
- quarantine when terms, retention, redistribution, or attribution are unresolved;
- keep credentials, tokens, cookies, signed URLs, and sensitive query strings out of commits, manifests, logs, receipts, and exceptions;
- preserve station scope, uncertainty, quality, and not-life-safety limitations with every handoff;
- avoid presenting station data as property-specific, household-specific, farm-specific, county-wide, watershed-wide, regional, or statewide conditions without governed derivation;
- avoid joins or location detail that create unreviewed private-network, infrastructure, landowner, crop, health, or operational claims;
- defer aggregation, generalization, suppression, notification, and public-safe rendering to governed downstream policy and release controls.

Public availability or reference-grade source status does not mean connector output is automatically approved for KFM publication, regulatory use, or life-safety use.

---

## Activation, promotion, and rollback

### Activation prerequisites

Do not activate this connector until all of the following are true:

- topology, package/import identity, ownership, and compatibility plan are ratified;
- authoritative SourceDescriptor, registry, and source-schema paths are resolved;
- the source-authority register records approved USCRN activation;
- accepted station, observation, and depth-aware domain contracts/schemas exist where required;
- current endpoint/access, file/header, variables/units, quality/missing codes, cadence, depth, station metadata, corrections, and citation evidence is verified;
- rights, attribution, sensitivity, and not-life-safety reviews are complete;
- integrity, parsing, station identity, time, cadence, units, quality, depth, redaction, quarantine, replay, correction, and no-network tests pass;
- RAW/QUARANTINE paths and downstream domain ownership are approved;
- downstream pipeline code/spec/tests cannot fetch directly, bypass admission, or publish;
- correction, deactivation, and rollback procedures have named owners.

### Promotion boundary

Successful admission means only that source material entered RAW with required evidence. It does not mean a station represents an area, a soil depth represents a column, a daily or monthly value can be inferred, a regulatory or drought conclusion exists, a cross-source comparison is valid, a product is scientifically validated for a new use, or anything is public. Every later transition belongs to downstream governed stages.

### Correction and deactivation

If source identity, station metadata, bytes, time, cadence, header, variable, unit, quality, missingness, depth, rights, or validation are later found wrong:

1. stop new admissions for the affected configuration;
2. preserve prior immutable bytes, manifests, and receipts;
3. mark affected runs, aggregates, comparisons, and downstream dependencies for review;
4. quarantine new or replayed material until the contradiction is resolved;
5. issue correction and release actions only through their governing surfaces;
6. reactivate only with a new reviewed configuration or SourceDescriptor revision.

Do not rewrite history, silently replace source files, delete evidence, or publish zero/normal/all-clear claims to simulate rollback.

---

## Verification backlog

- [ ] Ratify one canonical USCRN connector home and document migration, redirect, and deprecation for the other path.
- [ ] Record connector and registry topology drift or the accepted decision in the appropriate governance surface.
- [ ] Replace `OWNER_TBD` with accountable reviewers and NOAA USCRN CODEOWNERS coverage.
- [ ] Replace NOAA family greenfield placeholders with reviewed package/runtime decisions or keep them explicitly inactive.
- [ ] Resolve SourceDescriptor schema authority and the Soil/Agriculture/source-family registry topology.
- [ ] Create a conforming descriptor and add approved USCRN activation to the source-authority register.
- [ ] Resolve accepted station, Atmosphere observation, Soil moisture, depth, unit, quality, and missingness contracts/schemas.
- [ ] Verify current source endpoints, access, formats/headers, station inventory/metadata, variables, units, quality/missing codes, cadences, depths, corrections, terms, attribution, and citation.
- [ ] Implement bounded retrieval, station/product preservation, credential redaction, integrity checks, atomic handoff, and deterministic quarantine.
- [ ] Add no-network fixtures and executable tests for station identity, time, cadence, units, quality, missingness, depth, source drift, replay, and failure cases.
- [ ] Replace documentation-only pipeline and TODO connector/descriptor gates with meaningful code/spec/tests before treating them as readiness evidence.
- [ ] Verify RAW captures, downstream normalization, aggregates, comparisons, receipts, proofs, release, correction, API/UI, and public-safe caveats independently.

---

## Definition of done

This README update is complete when it accurately preserves the current boundary without claiming implementation. The connector itself is not done until every activation prerequisite and verification item above is resolved through its governing surface.

In all states:

- source, station, product, variable, unit, quality, missingness, time, cadence, depth, and file-vintage identity remain intact;
- station readings never become area truth without a separate governed derivative;
- one depth never substitutes for another or for a soil column;
- one cadence/product class never silently substitutes for another;
- missing values never become zero, normal, or all-clear claims;
- native observations remain distinct from calculated, corrected, aggregate, interpolated, and comparison artifacts;
- reference-grade never becomes regulatory, forecast, alert, or life-safety authority;
- connector output stops at RAW or QUARANTINE;
- placement, schema, registry, policy, pipeline, proof, release, alert, API, and UI authority remain outside this folder.

---

## Changelog

### v0.2 — 2026-07-14

- Reframed the path as a README-only proposed product connector boundary.
- Surfaced the parallel nested lane, canonical NOAA family posture, and greenfield NOAA package state.
- Added evidence-pinned status for duplicate registry placeholders, source activation, pipeline implementation/spec, contracts/schemas, RAW/fixtures, tests, workflows, and ownership.
- Tightened station-scope, depth, cadence, time, unit, quality, missingness, source-vintage, correction, reference-grade, zero/all-clear, and not-life-safety rules.
- Removed version-sensitive live-source specifics from the connector contract and moved them into the verification backlog.
- Added fail-closed retrieval, quarantine, no-network testing, replay, correction, activation, deactivation, and rollback requirements.
- Preserved the RAW/QUARANTINE-only lifecycle limit and prohibited regulatory/alert/publication authority.

### v0.1 — 2026-06-19

- Established the initial NOAA USCRN connector-lane documentation.

<p align="right"><a href="#top">Back to top</a></p>
