<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards-geoparquet
title: GeoParquet — KFM Repository and Conformance Boundary
type: standard; repository-boundary; conformance-readiness
version: v2.0-draft
status: "draft; repository-grounded; upstream-currentness-refreshed; mixed-maturity; no-adoption; no-byte-conformance; no-release; no-publication"
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
  - "NEEDS VERIFICATION — accountable GeoParquet, data-platform, catalog, evidence, policy, release, runtime, performance, and independent-review stewards"
created: 2026-05-14
updated: 2026-08-18
policy_label: "repository-facing; standards-guidance; geoparquet; vector-carrier; version-gated; release-gated"
owning_root: docs/
current_path: docs/standards/GEOPARQUET.md
responsibility: >
  Explain the upstream GeoParquet 1.1 and 2.0-release-candidate boundaries,
  disclose KFM's current declaration-only readiness, mirror-parity, and
  exact-toolchain assessment surfaces, and identify the evidence required
  before KFM may claim version adoption, byte conformance, production
  interoperability, release, or publication.
truth_posture: >
  CONFIRMED current path, standards-lane placement, default CODEOWNERS route,
  GeoParquet 1.1.0 stable line and corrected v1.1.0+p1 package, upstream
  v2.0.0-rc.1 status, current inactive metadata-readiness profile, fixture-only
  STAC mirror assessment, inactive 2.0-RC exact-toolchain packet, proposed
  ADR-0033, and published-lane scaffolding / PROPOSED accepted production
  profile, byte validators, migration, release integration, correction, and
  rollback / UNKNOWN real GeoParquet payloads, production readers and writers,
  deployed consumers, released carriers, and public publication.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 66fa5657e505b989d9c3465a364923af16c17ccf
  target_prior_blob: 7320145300e2ab6f414078e8479735ec374711c4
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  geospatial_carrier_contract_blob: 17055a680b83a4f83834735e88aeb0569322845b
  geospatial_carrier_schema_blob: b6ebec77a6e09c50b89594c4032bd40ec238f6be
  geospatial_carrier_workflow_blob: f5791e0988166dbcdd5d781c690073e8d3b10389
  stac_mirror_contract_blob: e5b3aabbee5a697d8e72e84f7df769882fdf76d5
  stac_mirror_workflow_blob: 28bbbf731a1ffb6ba489e9dc0e0b44acb9d6e660
  geoparquet_2_rc_contract_blob: 98345edd9f5262a63064b01cac57145eed2fe0e9
  geoparquet_2_rc_schema_blob: 5855e1a0d9eea37520329612b595cb64befa7ea2
  geoparquet_2_rc_validator_blob: 0bff4e868f0a49a4de40d020cf7e21c10bb8042f
  geoparquet_2_rc_tests_blob: b2923fafb91bdf35dc1f80b60fecc73c0395f540
  geoparquet_2_rc_workflow_blob: 45e25050a199cd12e777a120f6208ba50318e5fd
  published_lane_readme_blob: d5aced3d0e8200fba1be2a236a561e3fd2918224
external_currentness:
  access_date: 2026-08-18
  stable_line: "GeoParquet 1.1.0; corrected release package v1.1.0+p1 retains the 1.1.0 version identifier"
  candidate_line: "GeoParquet v2.0.0-rc.1; release candidate, not final 2.0.0"
related:
  - ./README.md
  - ./STAC.md
  - ./COG.md
  - ./PMTILES.md
  - ../doctrine/directory-rules.md
  - ../doctrine/lifecycle-law.md
  - ../doctrine/trust-membrane.md
  - ../architecture/contract-schema-policy-split.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../adr/ADR-0033-geoparquet-version-readiness.md
  - ../../contracts/release/geospatial_carrier_readiness.md
  - ../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json
  - ../../contracts/data/stac_geoparquet_mirror_assessment.md
  - ../../schemas/contracts/v1/data/stac_geoparquet_mirror_assessment.schema.json
  - ../../contracts/release/geoparquet_2_rc_compatibility_assessment.md
  - ../../schemas/contracts/v1/release/geoparquet_2_rc_compatibility_assessment.schema.json
  - ../../data/published/geoparquet/README.md
tags: [kfm, standards, geoparquet, parquet, vector, interoperability, catalog, evidence, release]
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, validator, fixture, workflow, receipt, data, dependency, runtime, release, deployment, or publication changes."
  - "The prior page overstated KFM-wide canonical adoption while understating the current inactive synthetic implementation."
  - "The legacy document identity, created date, H1 anchor, numbered-section anchors, lifecycle boundary, and cite-or-abstain posture are retained."
  - "The unsupported GeoParquetAssetManifest name is not represented as a current repository object."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="geoparquet--kfm-standards-reference"></a>

# GeoParquet — KFM Repository and Conformance Boundary

> **Operating rule.** GeoParquet is a geospatial table carrier. Its file structure does not create source authority, semantic meaning, evidence closure, policy approval, release authority, or public truth.

![status](https://img.shields.io/badge/status-v2.0--draft-d4a72c?style=flat-square)
![evidence](https://img.shields.io/badge/evidence-repository--grounded-1a7f37?style=flat-square)
![stable baseline](https://img.shields.io/badge/stable%20baseline-1.1.0-0969da?style=flat-square)
![candidate](https://img.shields.io/badge/candidate-2.0.0--rc.1-f59e0b?style=flat-square)
![byte conformance](https://img.shields.io/badge/byte%20conformance-not%20verified-b42318?style=flat-square)
![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)

> [!IMPORTANT]
> **Human-readable standards guidance only.** Contracts define KFM object meaning, schemas define machine shape, policy decides admissibility, validators establish only their declared checks, and governed release records decide release. This page does not replace any of those authorities.

> [!CAUTION]
> **Current KFM GeoParquet checks are declaration-only.** The repository contains deterministic, no-network profiles for 1.1 metadata readiness, declared STAC-mirror parity, and a 2.0-RC exact-toolchain packet. None opens or writes Parquet bytes, proves cross-engine behavior, migrates data, or authorizes release.

> [!WARNING]
> **Do not collapse 1.1 and 2.0.** GeoParquet 1.1 centers on the `geo` metadata layer and optional 1.1 accelerators. The 2.0 release candidate moves the storage foundation to native Parquet geospatial logical types and native spatial statistics. A version string or metadata-only `READY` result is not interoperability evidence.

| Field | Current bounded result |
|---|---|
| **Evidence snapshot** | `main@66fa5657e505b989d9c3465a364923af16c17ccf` |
| **Directory result** | **PLACE** at existing `docs/standards/GEOPARQUET.md`; accepted Directory Rules assign human-readable standards guidance to `docs/standards/` |
| **Review route** | `@bartytime4life` through current CODEOWNERS; accountable specialist stewardship and independent review remain **NEEDS VERIFICATION** |
| **Stable upstream line** | GeoParquet `1.1.0`; the corrected `v1.1.0+p1` release still uses the `1.1.0` version identifier |
| **Latest upstream candidate checked** | `v2.0.0-rc.1`; a release candidate, not final `2.0.0` |
| **KFM adoption state** | **NOT ESTABLISHED** as an accepted production format, migration, or release policy |
| **Current executable proof** | Synthetic declaration validation only; no Parquet carrier bytes are opened |
| **Current version decision** | ADR-0033 remains **proposed**; its `KEEP_1_1` route is not an accepted decision |
| **Published-data surface** | Directory scaffolding and child READMEs exist; no released GeoParquet carrier was verified |
| **Release/public effect** | None |

<a id="-quick-jump"></a>

**Quick navigation:** [Status](#0-current-repository-status-and-authority) · [Scope](#1-purpose--scope) · [Role](#2-why-geoparquet-in-kfm) · [Upstream](#3-external-standard-alignment-geoparquet-110) · [Implementation](#4-current-repository-implementation) · [1.1 profile](#4-kfm-profile-requirements) · [Mirror](#6-stac-geoparquet-mirror-assessment) · [2.0 RC](#7-geoparquet-20-rc-readiness-packet) · [Lifecycle](#7-lifecycle--promotion-gates) · [Validation](#8-validation-matrix) · [Policy](#9-policy-rights--sensitivity) · [Anti-patterns](#10-anti-patterns) · [Example](#11-illustrative-profile-snippet) · [Tooling](#12-tooling) · [Transition](#13-note-on-geoparquet-20) · [Open work](#14-open-questions) · [References](#15-related-docs--sources)

---

<a id="0-current-repository-status-and-authority"></a>

## 0. Current repository status and authority

### 0.1 Evidence boundary

This revision reconciles the target against repository bytes at the evidence snapshot in the metadata block and official upstream release material checked on 2026-08-18. Repository presence proves tracked bytes and bounded executable behavior at that revision. It does not prove production data, current consumers, deployed services, accepted stewardship, required-check status, release, or publication.

| Surface | CONFIRMED current state | What it does **not** establish |
|---|---|---|
| [`docs/standards/GEOPARQUET.md`](./GEOPARQUET.md) | Existing standards-lane page, modernized in place | KFM adoption, byte conformance, or release |
| [`docs/standards/README.md`](./README.md) | Defines this lane as human-readable standards and interoperability guidance | Contract, schema, policy, or release authority |
| [`GeospatialCarrierReadinessCheck`](../../contracts/release/geospatial_carrier_readiness.md) and companions | `PROPOSED_INACTIVE` metadata preflight with `READY`, `HOLD`, and `ERROR` outcomes | Reading Parquet bytes, source resolution, policy, promotion, or release |
| [`StacGeoParquetMirrorAssessment`](../../contracts/data/stac_geoparquet_mirror_assessment.md) and companions | Proposed, fixture-only parity over declared STAC and mirror projections | Existence or validity of STAC objects or GeoParquet bytes |
| [`GeoParquet 2.0 RC Compatibility Assessment`](../../contracts/release/geoparquet_2_rc_compatibility_assessment.md) and companions | `PROPOSED_INACTIVE` exact-toolchain declaration packet for later 2.0-RC byte probes | Installed tools, carrier generation, cross-engine compatibility, or migration |
| [`ADR-0033`](../adr/ADR-0033-geoparquet-version-readiness.md) | Proposed version-readiness decision | Accepted default, approved dual evaluation, or release authority |
| [`data/published/geoparquet/`](../../data/published/geoparquet/README.md) | Draft published-carrier lane with domain child READMEs | Released files, valid manifests, governed downloads, or publication |
| `GeoParquetAssetManifest` | No separate repository object with this exact name was found in the bounded search | Permission to invent a contract, schema, or parallel authority |

### 0.2 Authority map

| Question | Owning authority | Role of this page |
|---|---|---|
| What GeoParquet requires | The pinned upstream specification and release | Record the checked version boundary; do not redefine it |
| Whether KFM adopts a GeoParquet version | Accepted ADRs and accountable format-governance decisions | Distinguish declared, proposed, and accepted state |
| What a KFM assessment object means | The applicable contract under `contracts/` | Summarize and link; do not redefine semantics |
| What object shape is valid | The applicable schema under `schemas/contracts/v1/` | Cite the machine shape; do not duplicate it |
| What a validator checks | Validator code, fixtures, tests, workflow, and exact run evidence | State the bounded proof and non-effects |
| Whether source records support a carrier | Source identity, catalog, provenance, EvidenceBundle, and review authorities | Require resolution; do not infer it from bytes |
| What is admissible or public-safe | `policy/` plus accountable review | Explain fail-closed obligations; do not execute policy |
| Whether a carrier may be released | Governed release, correction, and rollback records | Explain closure; never approve release |
| Whether a client may read a carrier | Release-approved distribution and governed delivery configuration | Do not infer public access from a repository path |

No row substitutes for another.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="1-purpose--scope"></a>

## 1. Purpose & scope

### 1.1 Purpose

This page:

1. records the checked GeoParquet `1.1.0` stable line and `2.0.0-rc.1` candidate boundary;
2. explains KFM's intended use of GeoParquet as a processed or released vector carrier without claiming accepted adoption;
3. reconciles the current metadata-readiness, STAC-mirror, and 2.0-RC assessment packets;
4. separates declaration validation from byte conformance, interoperability, evidence, policy, release, and publication;
5. defines a finite evidence ladder for future implementation; and
6. preserves KFM lifecycle, correction, rollback, and public-path boundaries.

### 1.2 In scope

- GeoParquet format-version facts material to KFM.
- The current inactive KFM 1.1 metadata-readiness profile.
- The current fixture-only STAC GeoParquet mirror assessment.
- The current inactive 2.0-RC exact-toolchain readiness packet.
- Required evidence for real carrier validation, cross-engine testing, catalog closure, policy, review, release, and rollback.
- Fail-closed version and public-exposure behavior.

### 1.3 Out of scope

- Accepting ADR-0033 or adopting a GeoParquet production version.
- Defining domain data semantics, field dictionaries, units, or enumerations.
- Creating `GeoParquetAssetManifest` or any other contract/schema family.
- Generating, migrating, publishing, or deleting GeoParquet files.
- Installing or admitting GDAL, DuckDB, Sedona, PyArrow, GeoArrow, or another dependency.
- Activating a source, catalog mirror, download endpoint, map layer, API route, release, or publication.
- Treating generic Parquet tuning guidance as a universal KFM requirement.

### 1.4 Normative language

`MUST`, `SHOULD`, and similar terms in an upstream-summary row report the cited upstream specification. KFM-specific normative language is binding only when an accepted decision, contract, schema, active policy, or another authorized control makes it binding. Unattributed normative wording in a draft standards page is guidance or proposal, not policy.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="2-why-geoparquet-in-kfm"></a>

## 2. Why GeoParquet in KFM

GeoParquet combines Parquet's columnar table model with geospatial column metadata or native geospatial logical types, depending on the format version. It can support analytics, exchange, catalog distributions, reproducible derivatives, and released downloads without making the carrier itself authoritative.

KFM's current **inactive** carrier-readiness contract describes GeoParquet `1.1.0` as the candidate canonical vector carrier. That is a declared design posture, not an accepted KFM-wide production decision. Until version governance, byte conformance, consumer compatibility, source/evidence closure, and release proof exist, a GeoParquet file remains only a candidate carrier.

### 2.1 Carrier, meaning, and authority separation

| Layer | Owns | Does not own |
|---|---|---|
| GeoParquet bytes | Physical geospatial table representation | Source authority, policy, review, or release |
| Semantic contract | Field meaning, invariants, time, source role, and relationships | Parquet encoding or release approval |
| Machine schema/profile | Declared KFM assessment shape | Real byte correctness unless a byte validator reads the file |
| Catalog/provenance | Identity, discovery, lineage, and distribution references | Policy approval or release |
| EvidenceBundle | Support for consequential claims | File-format conformance by itself |
| Policy/review | Allowed, denied, held, redacted, restricted, or abstained outcomes | Byte identity or source provenance |
| Release/correction/rollback | Governed exposure and reversible public state | Upstream source truth |
| UI, map, notebook, or AI | Interpretation and presentation | Sovereign truth or publication authority |

### 2.2 Intended flow

```mermaid
flowchart LR
  SRC["Source identity<br/>rights · cadence · provenance"]
  RAW["RAW"]
  WORK["WORK / QUARANTINE"]
  GP["PROCESSED candidate<br/>GeoParquet carrier"]
  CAT["CATALOG / TRIPLETS<br/>STAC · DCAT · PROV"]
  GOV["Evidence · policy · review"]
  REL["Release decision<br/>correction · rollback"]
  PUB["PUBLISHED carrier<br/>or governed API"]
  UI["Client / map / analysis"]

  SRC --> RAW --> WORK --> GP --> CAT
  CAT --> GOV --> REL --> PUB --> UI
  GP -. byte and semantic checks .-> GOV
```

The diagram is a responsibility flow, not proof that every stage is implemented for GeoParquet today.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="3-external-standard-alignment-geoparquet-110"></a>

## 3. External standard alignment and version boundary

### 3.1 Stable 1.1 line

The checked stable line is GeoParquet `1.1.0`. Upstream also publishes a corrected package tagged `v1.1.0+p1`; producers and consumers still identify files as version `1.1.0`.

| 1.1 property | Upstream boundary | KFM current posture |
|---|---|---|
| Foundation | Parquet plus file-level `geo` metadata | Declared baseline in an inactive metadata profile |
| Geometry encoding | WKB and optional 1.1 native encodings based on GeoArrow | Current inactive KFM schema permits `WKB` or `GEOARROW`; executable byte support is unverified |
| Bbox covering | Optional covering-column mechanism for spatial pruning | Advisory in the current KFM metadata preflight, not a universal hard gate |
| CRS | GeoParquet metadata carries the declared CRS semantics | Current inactive KFM profile requires explicit `PROJJSON`; no carrier bytes are inspected |
| File naming | `.parquet` is the upstream recommendation | Current inactive KFM profile requires a declared `.parquet` filename |
| Media type | Upstream publishes a Parquet media-type recommendation | Current inactive KFM profile declares `application/vnd.apache.parquet` |
| Compatibility correction | `v1.1.0+p1` removes a conflicting group-field requirement without changing the `1.1.0` identifier | KFM must pin the corrected specification package when byte tests are added |

### 3.2 2.0 release-candidate line

The latest checked upstream release is `v2.0.0-rc.1`. It is explicitly a release candidate and may still change before final `2.0.0`.

| 2.0-RC property | Candidate boundary | KFM current posture |
|---|---|---|
| Foundation | Native Parquet `GEOMETRY` or `GEOGRAPHY` logical types | Declaration packet only; no byte probes |
| Physical representation | Native logical type over Parquet binary storage with WKB encoding | Recorded in the inactive packet; not verified from bytes |
| Spatial statistics | Native row-group geospatial statistics | Required by the declaration packet; no pruning benchmark executed |
| `geo` metadata | Optional explicit layer that must agree with Parquet-level metadata | Equivalence is declared, not measured |
| CRS authority | Native Parquet CRS property is the source of truth; inline GeoParquet CRS remains explicit when present | Current packet records the split; no round trip executed |
| 1.1 covering column | Removed from the 2.0 model in favor of native statistics | The packet rejects carrying a universal 1.1 covering requirement into 2.0 |
| Release maturity | Candidate, not final | Production use and default change remain **HOLD** |

### 3.3 KFM version-state separation

| State | Current result |
|---|---|
| Upstream stable version known | **CONFIRMED** — `1.1.0`, corrected package `v1.1.0+p1` |
| Upstream candidate known | **CONFIRMED** — `v2.0.0-rc.1` |
| KFM declared metadata baseline | **CONFIRMED** — `1.1.0` inside a `PROPOSED_INACTIVE` profile |
| Accepted KFM production default | **NOT ESTABLISHED** |
| 1.1 carrier-byte conformance | **NOT ESTABLISHED** |
| 2.0-RC carrier-byte compatibility | **NOT ESTABLISHED** |
| Production migration or dual-read window | **NOT ESTABLISHED** |
| Release/publication authority | **NONE** |

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="4-current-repository-implementation"></a>

## 4. Current repository implementation

KFM currently implements three independent synthetic assessment surfaces. Each is useful, but each stops before Parquet-byte validation.

| Surface | Profile/status | Inputs actually inspected | Finite outcomes | Boundary |
|---|---|---|---|---|
| [`GeospatialCarrierReadinessCheck`](../../contracts/release/geospatial_carrier_readiness.md) | `kfm.geospatial-carrier-readiness.v1.1` / `PROPOSED_INACTIVE` | Declared carrier metadata and bindings | `READY`, `HOLD`, `ERROR` | No TIFF, Parquet, or Protobuf bytes; no source, policy, release, or publication |
| [`StacGeoParquetMirrorAssessment`](../../contracts/data/stac_geoparquet_mirror_assessment.md) | `v0.1.0` / proposed, experimental, fixture-only | Declared STAC Item projections and declared mirror rows | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | No STAC fetch, Parquet access, catalog mutation, or evidence resolution |
| [`GeoParquet 2.0 RC Compatibility Assessment`](../../contracts/release/geoparquet_2_rc_compatibility_assessment.md) | `kfm.geoparquet-2-rc-compatibility-assessment.v2` / `PROPOSED_INACTIVE` | Exact declared tools, artifacts, evidence refs, and probe statuses | `READY`, `HOLD`, `ERROR` | `READY` means ready to run byte probes; it is not a compatibility result |

### 4.1 Companion implementation

The three profiles have repository-local schemas, fixtures, validators, tests, workflows, and generated-receipt bindings. Their existence establishes deterministic synthetic implementation at the pinned revision. It does not convert a proposed profile into adopted policy.

### 4.2 What is not currently proved

The inspected repository evidence does not establish:

- a checked-in real or synthetic `.parquet` fixture opened by a KFM GeoParquet validator;
- a producer that writes a KFM-reviewed GeoParquet file;
- a reader/query-engine matrix that consumes the same bytes;
- CRS, geometry, null, unknown-metadata, or row-group behavior observed from file bytes;
- source-to-carrier semantic parity;
- a complete production-consumer inventory;
- an accepted version-readiness decision;
- a release manifest binding a real GeoParquet carrier;
- a correction, withdrawal, or rollback drill; or
- a governed public download or runtime consumer.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="4-kfm-profile-requirements"></a>
<a id="5-object-families--contracts"></a>

## 5. Current KFM 1.1 metadata-readiness profile

The current GeoParquet lane in `GeospatialCarrierReadinessCheck` is an **inactive declaration preflight**. It is the closest executable representation of the old page's KFM profile, but it does not read the candidate artifact.

### 5.1 Declared carrier fields

| Field group | Current declared requirement | Evidence limit |
|---|---|---|
| Version and identity | `format_version`, immutable artifact ref, digest shape, `.parquet` filename, Parquet media type | Does not resolve bytes or recompute digest |
| Geometry | One named geometry column, root-column declaration, encoding, and non-empty geometry-type list | Does not inspect the Parquet schema or geometry payloads |
| CRS | `crs_format=PROJJSON` and `explicit_crs=true` | Does not parse or round-trip the CRS |
| Missing values | `null_policy=NULL_ONLY` | Does not scan values for NaN or sentinels |
| Metadata compatibility | Unknown metadata declared preserved | Does not execute a read/write round trip |
| Numeric units | Numeric-unit coverage declared | Does not inspect field names, unit metadata, or domain contracts |
| Determinism | Stable row grouping and deterministic ordering declared | Does not compare two generated files |
| Spatial pruning | Bbox covering declared; absence is advisory in 1.1 | Does not inspect statistics or measure pruning |
| Bindings | SourceDescriptor, RunReceipt, and STAC Item refs are present | Does not resolve or authenticate those objects |
| Governance | Every authority/release/public-use effect is fixed `false`; release ref is `null` | Cannot promote, release, or publish |

### 5.2 Dataset-specific layout profile

The inactive schema requires an inspectable layout declaration rather than one universal tuning constant:

- compression codec;
- ordering strategy, version, and parameter digest;
- row-group target rows and target bytes;
- partition strategy, version, and parameter digest;
- writer implementation, version, and parameter digest; and
- benchmark reference and result digest.

The current contract deliberately does **not** mandate one row-group size, Hilbert ordering, partition grid, writer, or compression codec for every dataset. Those choices require dataset-specific evidence.

### 5.3 Outcome semantics

| Outcome | Meaning | Non-effect |
|---|---|---|
| `READY` | Declared metadata satisfies the inactive preflight | Not byte-conformant, adopted, releasable, or public-safe |
| `HOLD` | Declaration is well formed but misses one or more readiness requirements | No lifecycle transition |
| `ERROR` | Declaration is malformed, internally unsafe, or violates a fail-closed integrity boundary | No automatic repair or authority |

### 5.4 Object-family boundary

The current repository uses specific assessment objects named above. The earlier page's `GeoParquetAssetManifest` name is not backed by a separate contract or schema in the bounded search. Any future canonical carrier-manifest family requires placement, semantics, schema, compatibility, fixtures, validation, ownership, and release integration; this page cannot create it by naming it.

### 5.5 Identity domains

Keep these identities distinct:

| Identity | Subject |
|---|---|
| Artifact reference | One logical candidate or released artifact record |
| Byte digest | Exact GeoParquet file bytes |
| Specification or parameter digest | Exact admitted build/profile value |
| Source reference | Upstream source identity |
| Run reference | One transformation execution |
| Evidence reference or bundle reference | Claim support |
| Catalog identity | Discovery projection |
| Release identity | Governed release transition |
| Correction or withdrawal identity | Post-release change |

The current executable GeoParquet-adjacent schemas use `sha256:<64-lowercase-hex>` for artifact and parameter digests. The prior page's `jcs:sha256:<hex>` examples must not be treated as implemented GeoParquet digest grammar without a separately accepted migration.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="6-stac-geoparquet-mirror-assessment"></a>

## 6. STAC GeoParquet mirror assessment

`StacGeoParquetMirrorAssessment` evaluates parity between two **declared projections**:

1. a declared set of STAC Item comparison fields; and
2. a declared set of rows representing a STAC GeoParquet collection mirror.

It compares collection/item identity, ordered extension identifiers, geometry and bbox digests, links, assets, non-temporal properties, property names, and temporal shape.

| Outcome | Meaning | Explicit non-claim |
|---|---|---|
| `PASS` / `PARITY_CONFIRMED` | Complete declared projections match with no extras | Does not prove source STAC objects or mirror bytes |
| `ABSTAIN` / `PARTIAL_SAMPLE` | Supplied sample matches but is not collection-complete | Does not claim collection-wide parity |
| `DENY` / conflict | Missing, extra, divergent, duplicated, noncanonical, or malformed declarations | Does not mutate the catalog |
| `ERROR` | Input is unsafe, malformed, or explicitly failed | Does not create a policy or release decision |

The assessment does not open Parquet or Arrow, decode WKB or GeoArrow, fetch STAC, resolve a catalog identity, establish rights, or approve a mirror. Operational use needs a separate byte reader, authoritative source resolution, catalog closure, evidence, policy, review, release, correction, and rollback.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="7-geoparquet-20-rc-readiness-packet"></a>

## 7. GeoParquet 2.0-RC readiness packet

The inactive `GeoParquet 2.0 RC Compatibility Assessment` records whether an exact synthetic toolchain packet is structurally ready for later carrier-byte probes against `2.0.0-rc.1`.

### 7.1 Current declared matrix

| Lane | Declared version | Intended later probe role | Current proof |
|---|---|---|---|
| GDAL | `3.13.2` | Producer, consumer, native type, CRS, statistics, metadata, and legacy 1.1 checks | Declaration only |
| DuckDB | `1.5.5` with `spatial@1.5.5` | Read, query, pruning, CRS, metadata, and legacy 1.1 checks | Declaration only |
| SedonaSpark | `1.9.0` with pinned Spark/Java/Scala/parquet-java context | Distributed read/write and compatibility probes | Declaration only |
| SedonaDB | `0.4.0` | Separate single-node read/write probes | Declaration only |
| PyArrow inspector | `25.0.0` | Footer logical-type and row-group-statistics inspection | Declaration only |

Version recognition is not support evidence. A source tag is not package-integrity proof. The declared packet keeps tool artifacts, transitive dependencies, probe results, and evidence identities distinct.

### 7.2 Finite outcomes

- `READY` — the declaration packet is complete and synthetic statuses pass; **byte probes may begin**.
- `HOLD` — required probes are pending or failed, a tool remains intentionally unpinned, or an unsupported assumption does not close.
- `ERROR` — shape, version, source pin, transitive dependency, digest, evidence identity, format expectation, governance boundary, or declared result is invalid.

No outcome changes KFM's declared 1.1 baseline, accepts ADR-0033, installs a tool, creates a carrier, migrates data, or authorizes release.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="6-pipeline-placement"></a>
<a id="7-lifecycle--promotion-gates"></a>

## 8. Lifecycle and release boundary

A file format does not determine lifecycle state. A `.parquet` file may be source-native RAW input, a WORK candidate, a quarantined artifact, a PROCESSED GeoParquet candidate, or a released PUBLISHED carrier depending on its governed state and owning lane.

KFM's lifecycle shorthand remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

A file path, extension, valid footer, metadata block, assessment result, digest, workflow, pull request, or merge does not move an artifact through that lifecycle by itself.

| Transition | GeoParquet-specific evidence needed | Fail-closed result |
|---|---|---|
| Candidate admission | Source identity, rights, cadence, retrieval record, payload identity | Reject or quarantine the candidate |
| RAW to WORK | Reproducible transform plan, pinned inputs and tools, domain mapping, sensitivity controls | Keep in RAW or route to QUARANTINE |
| WORK to PROCESSED | Real byte validation, geometry/CRS/value checks, semantic parity, deterministic output identity | Keep in WORK; emit finite failure |
| PROCESSED to CATALOG/TRIPLETS | Catalog identity, STAC/DCAT/PROV closure, source/evidence refs, correction lineage | Hold at PROCESSED |
| CATALOG/TRIPLETS to PUBLISHED | Policy, rights, sensitivity, accountable review, immutable release binding, correction and rollback | Hold at catalog; no public edge |
| Published correction | New evidence, corrected carrier, supersession/withdrawal, cache and consumer handling | Preserve prior history; never mutate silently |

### 8.1 Published-lane caution

`data/published/geoparquet/` is a draft placement boundary for release-linked carriers. Directory presence or a child README is not a release record. A real artifact may enter that lane only after the governing release process authorizes the exact bytes and audience.

### 8.2 Public-path boundary

Ordinary public clients should consume governed API responses or explicitly released public-safe artifacts. Direct access to processed candidates, catalog internals, source stores, proof stores, or unrestricted carrier bytes is not the normal public path.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="8-validation-matrix"></a>

## 9. Validation and evidence maturity

### 9.1 Maturity ladder

| Level | Capability | Current posture |
|---:|---|---|
| 0 | Repository-grounded human standards boundary | **CONFIRMED — this page** |
| 1 | Synthetic 1.1 metadata readiness | **CONFIRMED checked in / PROPOSED_INACTIVE** |
| 2 | Synthetic declared STAC-mirror parity | **CONFIRMED checked in / proposed fixture-only** |
| 3 | Synthetic 2.0-RC exact-toolchain readiness | **CONFIRMED checked in / PROPOSED_INACTIVE** |
| 4 | Real 1.1 carrier-byte conformance and negative corpus | **NOT ESTABLISHED** |
| 5 | Cross-engine 1.1 and 2.0-RC round trip, query, CRS, metadata, and pruning evidence | **NOT ESTABLISHED** |
| 6 | Source-to-carrier semantic parity, catalog, evidence, rights, sensitivity, policy, and review closure | **NOT ESTABLISHED end to end** |
| 7 | Governed release, serving, correction, withdrawal, rollback, and observed consumers | **NOT ESTABLISHED** |

### 9.2 Validation matrix

| Validation layer | Checks | Current state | What passing would not prove |
|---|---|---|---|
| Markdown/documentation | Structure, anchors, links, truth labels, repository references | This revision's changed area | Format conformance or adoption |
| Metadata readiness | Declared 1.1 profile and layout fields | Implemented synthetically | Actual bytes |
| STAC mirror parity | Declared source/mirror projections | Implemented synthetically | STAC or mirror existence |
| 2.0-RC toolchain packet | Exact declared tools, artifacts, statuses, and non-effects | Implemented synthetically | Installed or functioning tools |
| 1.1 byte conformance | Footer, `geo` metadata, geometry encodings, CRS, covering, values | Missing | Semantic correctness or release |
| Cross-engine interoperability | Write/read/round trip/query/statistics/pruning/unknown metadata | Missing | Source authority or policy |
| Semantic and source parity | Contracts, field meaning, time, units, source roles, evidence | Missing end to end | Public safety without policy/review |
| Release and serving | Immutable bytes, review, policy, Range/download behavior, correction, rollback | Missing | Future correctness without monitoring |

### 9.3 Checked-in deterministic commands

The repository workflows currently run these focused commands for the synthetic profiles:

```bash
python -m pytest -q tests/release/test_geospatial_carrier_readiness.py
python tools/validators/release/validate_geospatial_carrier_readiness.py --cases

python -m unittest -v tests.validators.test_validate_stac_geoparquet_mirror_assessment
python tools/validators/catalog/validate_stac_geoparquet_mirror_assessment.py --fixtures

python -m pytest -q tests/release/test_geoparquet_2_rc_compatibility_assessment.py
python tools/validators/release/validate_geoparquet_2_rc_compatibility_assessment.py --cases
```

These commands are no-network synthetic checks. They do not replace the missing carrier-byte and cross-engine layers.

### 9.4 Minimum future byte corpus

A dependency-closed byte-validation slice should include deterministic, rights-safe positive and negative carriers covering:

- corrected GeoParquet 1.1 WKB;
- any accepted 1.1 GeoArrow encoding;
- optional bbox covering present and absent;
- explicit CRS, unknown CRS, malformed CRS, and round-trip equivalence;
- geometry-type declarations that agree and disagree with payloads;
- nulls, NaN, sentinels, and domain-invalid values;
- unknown metadata preservation;
- stable ordering and row-group layout;
- malformed footer, truncated file, duplicate/conflicting metadata, and hostile nesting;
- 2.0-RC native `GEOMETRY` and `GEOGRAPHY` cases if dual evaluation is authorized; and
- legacy 1.1 readability after any 2.x tooling is introduced.

Every fixture must state what it proves and what it does not prove.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="9-policy-rights--sensitivity"></a>

## 10. Policy, rights, and sensitivity

GeoParquet is portable and can expose many records efficiently. That makes rights, precision, joins, and downstream reuse material release concerns.

Fail closed when:

- upstream rights or allowed redistribution are unresolved;
- a source, transform, or evidence reference cannot be resolved;
- precise locations would expose rare species, archaeology, infrastructure, living people, land/title detail, or another protected subject;
- aggregation can be reversed through low counts, temporal narrowing, auxiliary joins, or repeated releases;
- domain meaning, units, time semantics, uncertainty, or source role are missing;
- a declared digest cannot be reconciled with the candidate bytes;
- a required review or policy outcome is absent, stale, or contradictory;
- a release lacks correction, withdrawal, and rollback handling; or
- the proposed public path bypasses governed delivery.

Generalization, redaction, aggregation, or partitioning is not automatically sufficient. The released carrier and its indexes, statistics, metadata, filenames, bounds, partitions, and auxiliary artifacts must all satisfy the same audience and sensitivity posture.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="10-anti-patterns"></a>

## 11. Anti-patterns

Reviewers should reject changes that:

- cite this page as proof that KFM has adopted GeoParquet `1.1.0` or `2.x`;
- call metadata-only `READY` a carrier-conformance result;
- call mirror `PASS` proof that STAC objects or GeoParquet bytes exist;
- call 2.0-RC `READY` cross-engine compatibility or migration approval;
- treat `data/published/geoparquet/` placement as release authority;
- invent `GeoParquetAssetManifest` semantics or schema from the old page's prose;
- copy proposal-era `jcs:sha256:<hex>` examples into current GeoParquet assessment objects instead of their implemented `sha256:<hex>` grammar;
- require one row-group size, spatial order, partition grid, writer, or codec for every dataset without benchmark evidence;
- carry the 1.1 bbox-covering assumption into 2.0 as a universal requirement;
- silently accept an unknown or unsupported format version;
- use a version tag without immutable tool and artifact identity;
- infer source truth, rights, sensitivity clearance, or review from a valid Parquet footer;
- expose processed or internal GeoParquet directly to ordinary public clients;
- replace nulls with undocumented sentinels or conceal domain-invalid values;
- mutate a released carrier in place instead of issuing a traceable correction; or
- treat maps, notebooks, tiles, AI summaries, or query results as evidence beyond their resolved support.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="11-illustrative-profile-snippet"></a>

## 12. Illustrative declaration fragment

The fragment below illustrates the current **metadata-readiness declaration**, not a complete schema-valid object and not GeoParquet file metadata.

```jsonc
{
  "carrier_kind": "GEOPARQUET",
  "carrier": {
    "format_version": "1.1.0",
    "geometry_column": "geometry",
    "root_geometry_column": true,
    "encoding": "WKB",
    "crs_format": "PROJJSON",
    "explicit_crs": true,
    "geometry_types": ["MultiPolygon"],
    "stable_row_grouping": true,
    "deterministic_ordering": true,
    "null_policy": "NULL_ONLY",
    "bbox_covering": true,
    "unknown_metadata_preserved": true,
    "numeric_unit_coverage": true,
    "layout_profile": {
      "profile_id": "kfm.geoparquet-layout.example-v1",
      "compression": "ZSTD",
      "ordering_strategy": "PRIMARY_KEY",
      "ordering_version": "example-v1",
      "row_group_target_rows": 50000,
      "row_group_target_bytes": 134217728,
      "partition_strategy": "NONE",
      "writer_implementation": "example-only",
      "writer_version": "0.0.0",
      "benchmark_ref": "kfm://benchmark/example"
    }
  }
}
```

The omitted digests, artifact bindings, source/run/STAC references, and governance fields are required by the actual schema. The values above are illustrative and must not be copied into a production profile without dataset-specific evidence.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="12-tooling"></a>

## 13. Tooling boundary

### 13.1 Current repository tooling

KFM currently has Python validators for the three synthetic assessment surfaces. Their checked-in workflows:

- run with `KFM_NO_NETWORK=1`;
- use read-only `contents` permission;
- install the repository's declared test dependencies;
- execute focused fixtures and tests;
- verify a generated authoring receipt; and
- record explicit non-effects.

Those workflows do not install the proposed GeoParquet interoperability matrix or read carrier bytes.

### 13.2 External tools

Potential byte-level tools include GeoParquet-specific validators, GDAL/OGR, PyArrow, DuckDB Spatial, SedonaSpark, SedonaDB, and independent Parquet footer inspection. Tool names and documentation are discovery evidence only. Before a tool enters a trust-bearing KFM path, pin its source and package artifact, inspect transitive dependencies and licenses, use a rights-safe fixture corpus, run without ambient credentials, and preserve exact commands and output digests.

### 13.3 Required tool-result separation

| Result | Permitted claim |
|---|---|
| File opens | The selected tool parsed the selected bytes |
| Metadata schema passes | The metadata matches the checked schema version |
| Geometry decodes | The selected geometry payload decoded under the selected tool |
| Cross-engine round trip passes | The tested engines preserved the tested semantics |
| Spatial pruning is observed | The tested query used the tested statistics/layout |
| Policy allows | The named policy bundle allowed the named audience and artifact |
| Release is approved | The named release authority approved the exact immutable bytes |

A stronger claim requires stronger evidence.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="13-note-on-geoparquet-20"></a>

## 14. Version transition and rollback

ADR-0033 proposes retaining `1.1.0` as the declared default while allowing a bounded 2.0-RC evaluation. Because the ADR is proposed, this page records the route without treating it as adopted.

### 14.1 Entry conditions for dual byte evaluation

Before a 2.x byte-evaluation slice begins:

1. confirm the candidate or final upstream specification and immutable commit;
2. approve the exact toolchain and artifact digests;
3. preserve a corrected 1.1 positive and negative corpus;
4. define semantic equivalence for geometry, CRS, time, nulls, units, metadata, ordering, and statistics;
5. inventory production and release consumers;
6. define finite `PASS`, `ABSTAIN`, `DENY`, and `ERROR` outcomes for each probe;
7. keep all governance effects false;
8. prohibit network and production data in deterministic tests; and
9. define abandonment, revert, correction, and migration rollback before execution.

### 14.2 Conditions before any default change

A later accepted decision would need at least:

- final stable upstream 2.x identity;
- successful byte generation and inspection;
- independent cross-engine read/write/query evidence;
- preserved 1.1 compatibility or a bounded migration plan;
- complete consumer and persisted-record inventory;
- source-to-carrier semantic parity;
- catalog, evidence, rights, sensitivity, policy, and review integration;
- release, correction, withdrawal, cache, and rollback drills; and
- accountable owner and independent-review acceptance.

### 14.3 Rollback

- **This documentation change:** close or abandon the unmerged PR; after merge, revert the single documentation commit.
- **Synthetic profile change:** revert the profile, schema, fixtures, validator, tests, workflow, and successor receipt as one dependency-closed packet.
- **Carrier migration:** issue a reviewed forward fix or revert through versioned migration records; never rewrite released history.
- **Published reliance:** preserve correction, withdrawal, supersession, cache invalidation, and downstream notification. A Git revert alone may be insufficient.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="14-open-questions"></a>

## 15. Open questions and verification backlog

| Question | Current state | Evidence needed |
|---|---|---|
| Who owns GeoParquet format decisions and independent review? | **NEEDS VERIFICATION** | Accepted stewardship assignments and review route |
| Should ADR-0033 be accepted, revised, or replaced after upstream final 2.0? | **OPEN** | Current upstream, consumer, migration, and rollback evidence |
| Which corrected 1.1 bytes form the canonical fixture corpus? | **OPEN** | Rights-safe deterministic fixtures and immutable digests |
| Does KFM permit 1.1 GeoArrow encodings or require WKB in production? | **OPEN** | Consumer support matrix and accepted profile |
| What is the canonical carrier-manifest object family? | **OPEN** | Contract/schema placement decision; do not infer `GeoParquetAssetManifest` |
| Which producers, readers, query engines, notebooks, pipelines, and services consume GeoParquet? | **UNKNOWN** | Repository and operational consumer inventory |
| Which layout strategies are justified by real KFM workloads? | **UNKNOWN** | Dataset-specific benchmarks and reproducibility receipts |
| Are real released GeoParquet carriers present outside the inspected repository paths? | **UNKNOWN** | Release inventory and immutable artifact evidence |
| How will 1.1 corrections and 2.x migrations preserve downstream identity? | **OPEN** | Migration, correction, supersession, and rollback design |
| What governed API or approved download surface will expose released carriers? | **UNKNOWN** | Runtime, deployment, policy, and release evidence |

Do not convert these questions into implementation facts merely to complete the document.

<p align="right"><a href="#top">Back to top</a></p>

---

<a id="15-related-docs--sources"></a>

## 16. Related docs and sources

### 16.1 Repository authority and guidance

- [`docs/standards/README.md`](./README.md) — standards-lane boundary and mixed-maturity inventory.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — adopted placement bytes through ADR-0029.
- [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules adoption.
- [`ADR-0033`](../adr/ADR-0033-geoparquet-version-readiness.md) — proposed version-readiness decision.
- [`contract-schema-policy split`](../architecture/contract-schema-policy-split.md) — meaning, shape, and admissibility separation.
- [`STAC`](./STAC.md), [`COG`](./COG.md), and [`PMTiles`](./PMTILES.md) — adjacent carrier and catalog guidance.

### 16.2 Current GeoParquet-related implementation

- [`GeospatialCarrierReadinessCheck` contract](../../contracts/release/geospatial_carrier_readiness.md)
- [`GeospatialCarrierReadinessCheck` schema](../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json)
- [`GeospatialCarrierReadinessCheck` validator](../../tools/validators/release/validate_geospatial_carrier_readiness.py)
- [`GeospatialCarrierReadinessCheck` tests](../../tests/release/test_geospatial_carrier_readiness.py)
- [`GeospatialCarrierReadinessCheck` workflow](../../.github/workflows/geospatial-carrier-readiness.yml)
- [`StacGeoParquetMirrorAssessment` contract](../../contracts/data/stac_geoparquet_mirror_assessment.md)
- [`StacGeoParquetMirrorAssessment` schema](../../schemas/contracts/v1/data/stac_geoparquet_mirror_assessment.schema.json)
- [`StacGeoParquetMirrorAssessment` validator](../../tools/validators/catalog/validate_stac_geoparquet_mirror_assessment.py)
- [`StacGeoParquetMirrorAssessment` tests](../../tests/validators/test_validate_stac_geoparquet_mirror_assessment.py)
- [`StacGeoParquetMirrorAssessment` workflow](../../.github/workflows/stac-geoparquet-mirror-assessment.yml)
- [`GeoParquet 2.0 RC Compatibility Assessment` contract](../../contracts/release/geoparquet_2_rc_compatibility_assessment.md)
- [`GeoParquet 2.0 RC Compatibility Assessment` schema](../../schemas/contracts/v1/release/geoparquet_2_rc_compatibility_assessment.schema.json)
- [`GeoParquet 2.0 RC Compatibility Assessment` validator](../../tools/validators/release/validate_geoparquet_2_rc_compatibility_assessment.py)
- [`GeoParquet 2.0 RC Compatibility Assessment` tests](../../tests/release/test_geoparquet_2_rc_compatibility_assessment.py)
- [`GeoParquet 2.0 RC Compatibility Assessment` workflow](../../.github/workflows/geoparquet-2-rc-compatibility-assessment.yml)
- [`data/published/geoparquet/` boundary](../../data/published/geoparquet/README.md)

### 16.3 Official upstream sources

- GeoParquet `1.1.0` specification — <https://geoparquet.org/releases/v1.1.0/>
- GeoParquet `1.1.0` metadata schema — <https://geoparquet.org/releases/v1.1.0/schema.json>
- GeoParquet official releases — <https://github.com/opengeospatial/geoparquet/releases>
- GeoParquet `v2.0.0-rc.1` release — <https://github.com/opengeospatial/geoparquet/releases/tag/v2.0.0-rc.1>
- GeoParquet project — <https://geoparquet.org/>
- Apache Parquet geospatial logical types — <https://github.com/apache/parquet-format/blob/master/Geospatial.md>

External URLs were checked for currentness on 2026-08-18. They are upstream authority for format facts, not KFM adoption or release authority.

<p align="right"><a href="#top">Back to top</a></p>

---

## Appendix A — v1 preservation and correction ledger

| Prior material | v2 disposition |
|---|---|
| Document ID, path, created date, GeoParquet topic, lifecycle boundary, cite-or-abstain rule | **KEEP** |
| Original H1 and numbered-section anchors | **KEEP through compatibility anchors** |
| Placeholder steward names | **REPAIR** to verified CODEOWNERS route plus explicit specialist `NEEDS VERIFICATION` |
| “Proposed canonical home” | **REPAIR** to confirmed same-path `PLACE` |
| Neighbor paths marked proposed despite existing | **REPAIR** with current repository links |
| KFM-wide “canonical vector artifact” assertion | **NARROW** to intended role inside an inactive profile; adoption not established |
| Claim that no GeoParquet contracts, schemas, validators, fixtures, or workflows exist | **REPAIR** with the three current synthetic packets |
| `GeoParquetAssetManifest` as a current required object | **REMOVE WITH EVIDENCE**; no separate repository object found |
| GeoParquet 2.0 described only as an unspecified dev track | **REPAIR** to `v2.0.0-rc.1`, still not final |
| Universal WKB, row-group, ordering, partition, and codec assertions | **NARROW** to current declared fields and dataset-specific benchmark requirements |
| STAC/DCAT/PROV, evidence, policy, release, correction, and rollback distinctions | **KEEP AND CLARIFY** |
| Illustrative metadata block that mixed external `geo` metadata with a speculative KFM sidecar | **REPLACE** with a clearly partial inactive-readiness declaration fragment |
| Publication implications of a path, file, validator, or workflow | **REPAIR** to explicit non-effects |

No implementation, adoption, release, or publication state changes with this ledger.

---

<sub>
<b>Last evidence review:</b> 2026-08-18 &nbsp;·&nbsp;
<b>Review route:</b> @bartytime4life; specialist stewardship needs verification &nbsp;·&nbsp;
<b>Stable upstream line:</b> GeoParquet 1.1.0 / corrected package v1.1.0+p1 &nbsp;·&nbsp;
<b>Latest candidate checked:</b> v2.0.0-rc.1 &nbsp;·&nbsp;
<b>Release/publication effect:</b> none
</sub>
