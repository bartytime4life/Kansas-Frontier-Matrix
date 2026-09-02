<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/geoparquet/atmosphere/readme
title: data/published/geoparquet/atmosphere README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): atmosphere domain steward
  - TODO(owner): geospatial export steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/geoparquet/atmosphere/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../atmosphere/README.md
  - ../../exports/README.md
  - ../../api_payloads/atmosphere/README.md
  - ../../../README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../proofs/atmosphere/README.md
  - ../../../proofs/validation_report/atmosphere/README.md
  - ../../../receipts/README.md
  - ../../../../release/README.md
  - ../../../../docs/domains/atmosphere/ARCHITECTURE.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
notes:
  - "Directory README for released Atmosphere GeoParquet carriers under data/published/geoparquet/. It replaces a placeholder file."
  - "This lane stores release-linked GeoParquet files or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted GeoParquet files, schemas, validators, CI, or governed download routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/geoparquet/atmosphere/`

> Published GeoParquet sublane for released, public-safe **Atmosphere / Air** geospatial table carriers. Files here should be immutable, release-linked `.parquet` / GeoParquet packages consumed through governed download, approved released-artifact, or governed API paths.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: atmosphere](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![Carrier: GeoParquet](https://img.shields.io/badge/carrier-GeoParquet-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): atmosphere domain steward` · `TODO(owner): geospatial export steward` · `TODO(owner): publication steward` · `TODO(owner): release steward`  
> **Path:** `data/published/geoparquet/atmosphere/README.md`  
> **Truth posture:** CONFIRMED target path, parent `geoparquet/` stub, Atmosphere published lane, and Atmosphere architecture from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted GeoParquet artifacts, formal format profile, schemas, validators, release manifests, CI checks, and governed download routes.

> [!WARNING]
> This directory does not approve publication and is not a raw-data outlet. GeoParquet files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this GeoParquet sublane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted GeoParquet carriers](#3-accepted-geoparquet-carriers) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Publication gates](#5-publication-gates) | Minimum support before artifacts land here. |
| [6. Atmosphere GeoParquet rules](#6-atmosphere-geoparquet-rules) | Format and domain guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing artifacts. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/geoparquet/atmosphere/` is the published carrier lane for release-approved Atmosphere GeoParquet files and packages.

Use this lane for geospatial tabular artifacts that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- packaged for governed download, reproducible reuse, released-artifact distribution, or governed API handoff;
- explicit about source role, knowledge character, geometry type, CRS, schema/profile version, observed/valid/retrieval/release time, freshness, stale-state posture, caveats, license/rights posture, digest, and correction status; and
- scoped to public-safe Atmosphere products such as air-observation summaries, AQI or air-quality context, smoke/AOD context, forecast/model context, climate normals/anomalies, weather context, or advisory context.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/published/geoparquet/` | Parent GeoParquet carrier lane. | Parent contract is still a greenfield stub; this child README does not complete it. |
| `data/published/atmosphere/` | Domain published lane. | Defines Atmosphere published-carrier posture. |
| `data/published/exports/` | Generic export carriers. | GeoParquet is a format-specific published export lane. |
| `data/published/api_payloads/atmosphere/` | Released API-shaped Atmosphere payloads. | API JSON payloads are separate from GeoParquet packages. |
| `data/raw/atmosphere/` | Source captures. | Not public-readable. |
| `data/work/atmosphere/` | Working candidates. | Not public-readable. |
| `data/quarantine/atmosphere/` | Held material. | Not public-readable. |
| `data/processed/atmosphere/` | Validated candidates. | Upstream of release. |
| `data/catalog/domain/atmosphere/` | Catalog records. | Discovery and lineage, not release authority. |
| `data/proofs/` | Proof-support lanes. | Support, not published GeoParquet. |
| `data/receipts/` | Process-memory lanes. | Receipts do not publish. |
| `release/` | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| `contracts/` | Semantic meaning. | GeoParquet files conform; they do not define meaning. |
| `schemas/` | Machine shape. | GeoParquet files validate; schemas live elsewhere. |
| `policy/` | Admissibility. | GeoParquet files carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted GeoParquet carriers

Use this directory only for release-linked, public-safe GeoParquet carriers.

| Carrier type | Suggested placement | Required support |
|---|---|---|
| Released Atmosphere GeoParquet layer | `layers/<release_id>/<layer_slug>.parquet` | ReleaseManifest, EvidenceBundle refs, policy decision, validation report, rollback target. |
| Released observation-summary package | `observations/<release_id>/<summary_slug>.parquet` | Source role, knowledge character, time scope, caveats, release refs. |
| Released model/context package | `model_context/<release_id>/<context_slug>.parquet` | Model-run context, issue/valid time, caveats, release refs. |
| Released remote-sensing context package | `remote_sensing/<release_id>/<context_slug>.parquet` | Product role, resolution/footprint, caveats, release refs. |
| Released climate/anomaly package | `climate_context/<release_id>/<context_slug>.parquet` | Baseline period, anomaly method, evidence refs, release refs. |
| Released package manifest | `manifests/<release_id>/<package_slug>.manifest.json` | File list, checksums, schema/profile refs, release refs. |
| Released public index | `indexes/atmosphere-geoparquet-index.json` | Points to release-approved files only. |
| Superseded GeoParquet artifact | `retired/<release_id>/<artifact_slug>.parquet` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| RAW source payloads, sensor exports, source rasters, model files, advisory text dumps, logs, or source-system dumps | `data/raw/atmosphere/` |
| Working or held candidates | `data/work/atmosphere/` or `data/quarantine/atmosphere/` |
| Processed normalized data | `data/processed/atmosphere/` |
| Catalog records | `data/catalog/` |
| Proof objects, validation reports, review records, or EvidenceBundles | `data/proofs/` |
| Receipts, transform receipts, model-run receipts, representation receipts, or AI receipts | `data/receipts/` or approved proof/receipt homes |
| API payload snapshots | `data/published/api_payloads/atmosphere/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas, profile definitions, or validator source | `schemas/`, `contracts/`, `tests/`, or approved tooling roots |
| Emergency instructions, evacuation advice, routing advice, or life-safety directives | Official authorities outside this published carrier lane |
| Direct model output or unreviewed AI summaries | Governed AI/review paths before release |

[Back to top](#top)

---

## 5. Publication gates

Before an Atmosphere GeoParquet artifact is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema, GeoParquet/profile, geometry, CRS, and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class and downloadable format;
- [ ] review records exist where required;
- [ ] knowledge character, source role, geometry scope, time scope, freshness/stale state, caveats, rights/license posture, and public-safe posture are preserved;
- [ ] correction and rollback targets are traceable;
- [ ] digests or integrity refs bind each file to the release record.

If any gate is unresolved, hold the artifact upstream.

[Back to top](#top)

---

## 6. Atmosphere GeoParquet rules

| Rule | Public GeoParquet posture |
|---|---|
| Format is a carrier, not authority | GeoParquet files are released artifacts; they do not define release, truth, policy, schema, or evidence. |
| Geometry metadata is explicit | Geometry column, geometry type, CRS, bounds/extent, spatial resolution or aggregation scope, and geometry validity must be discoverable. |
| Time semantics are explicit | Observed time, valid time, issue time, retrieval time, release time, model-run time, and stale-state posture are preserved where material. |
| AQI is not concentration | AQI fields must not be represented as measured concentration values. |
| AOD is not PM2.5 | Remote-sensing context remains labeled as remote-sensing context, not surface concentration truth. |
| Model fields are not observations | Forecast/model carriers remain model/context products, not observed truth. |
| Low-cost sensors require caveats | Public files need correction, caveats, confidence, and limitations before release. |
| Advisory context redirects | Published carriers may reference official advisories but must not replace life-safety instructions. |
| Rights travel with the file | License, source rights, audience class, and allowed reuse posture must be clear. |
| AI is not root truth | AI summaries can consume released files but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/geoparquet/atmosphere/
├── README.md
├── layers/
│   └── <release_id>/
├── observations/
│   └── <release_id>/
├── model_context/
│   └── <release_id>/
├── remote_sensing/
│   └── <release_id>/
├── climate_context/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── atmosphere-geoparquet-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file names:

```text
atmosphere.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.parquet
atmosphere.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.manifest.json
atmosphere.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.checksums.txt
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing a GeoParquet artifact under this sublane, verify:

- [ ] The artifact is release-approved and public-safe for the intended audience.
- [ ] The release record points to this artifact.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Geometry column, CRS, geometry type, bounds/extent, time fields, source role, knowledge character, caveats, schema/profile version, rights/license posture, and public-safe posture are preserved.
- [ ] The artifact does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, API payload, or release authority.
- [ ] The artifact has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.
- [ ] Parent `data/published/geoparquet/README.md` is updated before this format lane becomes operationally mature.

[Back to top](#top)

---

## 9. Definition of done

This sublane is operationally mature when:

- [ ] `data/published/geoparquet/README.md` defines the parent GeoParquet published-data contract.
- [ ] Atmosphere GeoParquet contracts, schemas, and fixtures exist under approved homes.
- [ ] Release tooling writes or verifies GeoParquet artifacts only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, invalid GeoParquet/profile metadata, missing CRS, invalid geometry, source-role collapse, AQI/concentration confusion, AOD/PM2.5 confusion, model/observation confusion, missing caveats, stale-state ambiguity, missing rights/license posture, and unsafe public fields.
- [ ] Valid and invalid fixtures cover observation, model/context, remote-sensing context, climate/anomaly, corrected release, superseded release, and rollback packages.
- [ ] Governed download/export routes are documented and tested.

---

## Maintainer note

Published Atmosphere GeoParquet files are reusable artifacts that may travel outside the KFM UI. Keep them boring, citable, schema-aware, geometry-aware, time-aware, rights-aware, caveat-rich, freshness-aware, official-source-aware, and reversible. If evidence, source role, validation, policy, rights, release, correction, or rollback support is incomplete, keep the file upstream instead of placing it here.
