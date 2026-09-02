<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/geoparquet/geology/readme
title: data/published/geoparquet/geology README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): geology domain steward
  - TODO(owner): geospatial export steward
  - TODO(owner): publication steward
  - TODO(owner): rights reviewer
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/geoparquet/geology/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../geology/README.md
  - ../../exports/README.md
  - ../../../README.md
  - ../../../raw/geology/README.md
  - ../../../work/geology/README.md
  - ../../../quarantine/geology/README.md
  - ../../../processed/geology/README.md
  - ../../../catalog/domain/geology/README.md
  - ../../../proofs/geology/README.md
  - ../../../proofs/validation_report/geology/README.md
  - ../../../receipts/README.md
  - ../../../../release/README.md
  - ../../../../docs/domains/geology/ARCHITECTURE.md
  - ../../../../docs/domains/geology/RELEASE_INDEX.md
  - ../../../../docs/domains/geology/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/geology/API_CONTRACTS.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
notes:
  - "Directory README for released Geology GeoParquet carriers under data/published/geoparquet/. It replaces a placeholder file."
  - "This lane stores release-linked GeoParquet files or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted GeoParquet files, schemas, validators, CI, or governed download routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/geoparquet/geology/`

> Published GeoParquet sublane for released, public-safe **Geology and Natural Resources** geospatial table carriers. Files here should be immutable, release-linked `.parquet` / GeoParquet packages consumed through governed download, approved released-artifact, or governed API paths.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: geology](https://img.shields.io/badge/domain-geology%2Fnatural--resources-795548)
![Carrier: GeoParquet](https://img.shields.io/badge/carrier-GeoParquet-blue)
![Policy: public review](https://img.shields.io/badge/policy-public--review-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): geology domain steward` · `TODO(owner): geospatial export steward` · `TODO(owner): publication steward` · `TODO(owner): rights reviewer` · `TODO(owner): release steward`  
> **Path:** `data/published/geoparquet/geology/README.md`  
> **Truth posture:** CONFIRMED target path, parent `geoparquet/` stub, Geology published lane, and Geology architecture/release docs from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted GeoParquet artifacts, formal format profile, schemas, validators, release manifests, CI checks, and governed download routes.

> [!WARNING]
> This directory does not approve publication and is not a raw-data outlet. GeoParquet files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, rights posture is known, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this GeoParquet sublane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted GeoParquet carriers](#3-accepted-geoparquet-carriers) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Publication gates](#5-publication-gates) | Minimum support before artifacts land here. |
| [6. Geology GeoParquet rules](#6-geology-geoparquet-rules) | Format and domain guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing artifacts. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/geoparquet/geology/` is the published carrier lane for release-approved Geology GeoParquet files and packages.

Use this lane for geospatial tabular artifacts that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- packaged for governed download, reproducible reuse, released-artifact distribution, or governed API handoff;
- explicit about source role, evidence support, geometry type, CRS, schema/profile version, aggregation scope, uncertainty, observed/valid/retrieval/release time, rights/license posture, caveats, digest, and correction status; and
- scoped to public-safe Geology products such as generalized geologic units, surficial geology, stratigraphy context, lithology context, structures, borehole-reference summaries, cross-section context, geochemistry/geophysics context, resource-context summaries, extraction/reclamation context, or public index tables.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, restricted source material, proprietary detail, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/published/geoparquet/` | Parent GeoParquet carrier lane. | Parent contract is still a greenfield stub; this child README does not complete it. |
| `data/published/geology/` | Domain published lane. | Defines Geology published-carrier posture. |
| `data/published/exports/` | Generic export carriers. | GeoParquet is a format-specific published export lane. |
| `data/raw/geology/` | Source captures. | Not public-readable. |
| `data/work/geology/` | Working candidates. | Not public-readable. |
| `data/quarantine/geology/` | Held material. | Not public-readable. |
| `data/processed/geology/` | Validated candidates. | Upstream of release. |
| `data/catalog/domain/geology/` | Catalog records. | Discovery and lineage, not release authority. |
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
| Released Geology GeoParquet layer | `layers/<release_id>/<layer_slug>.parquet` | ReleaseManifest, EvidenceBundle refs, policy decision, validation report, review refs, rollback target. |
| Released geologic-unit package | `geologic_units/<release_id>/<unit_slug>.parquet` | Source role, map/version context, evidence, caveats, release refs. |
| Released stratigraphy/lithology package | `stratigraphy/<release_id>/<context_slug>.parquet` | Interpretation role, evidence refs, uncertainty, release refs. |
| Released structure/cross-section package | `structures/<release_id>/<structure_slug>.parquet` | Interpretation role, geometry scope, caveats, release refs. |
| Released borehole or well-log reference package | `subsurface_references/<release_id>/<reference_slug>.parquet` | Rights posture, location posture, source role, release refs. |
| Released resource-context package | `resource_context/<release_id>/<context_slug>.parquet` | Aggregation scope, uncertainty, source-role preservation, release refs. |
| Released package manifest | `manifests/<release_id>/<package_slug>.manifest.json` | File list, checksums, schema/profile refs, release refs. |
| Released public index | `indexes/geology-geoparquet-index.json` | Points to release-approved files only. |
| Superseded GeoParquet artifact | `retired/<release_id>/<artifact_slug>.parquet` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| RAW source payloads, source maps, well logs, cores, geophysics files, geochemistry files, regulatory exports, production files, scans, media, or source-system dumps | `data/raw/geology/` |
| Working or held candidates | `data/work/geology/` or `data/quarantine/geology/` |
| Processed normalized data | `data/processed/geology/` |
| Catalog records | `data/catalog/` |
| Proof objects, validation reports, review records, or EvidenceBundles | `data/proofs/` |
| Receipts, transform receipts, aggregation receipts, model-run receipts, representation receipts, or AI receipts | `data/receipts/` or approved proof/receipt homes |
| API payload snapshots | `data/published/api_payloads/` child lanes where applicable. |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas, profile definitions, or validator source | `schemas/`, `contracts/`, `tests/`, or approved tooling roots |
| Restricted, proprietary, rights-unclear, or sensitive source detail | Upstream restricted/held lanes until cleared for public release. |
| Direct model output or unreviewed AI summaries | Governed AI/review paths before release. |

[Back to top](#top)

---

## 5. Publication gates

Before a Geology GeoParquet artifact is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema, GeoParquet/profile, geometry, CRS, and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class and downloadable format;
- [ ] rights and source terms are compatible with the public carrier;
- [ ] review records exist where required by sensitivity, rights, source terms, or materiality;
- [ ] source role, geometry scope, aggregation scope, uncertainty, caveats, rights/license posture, and public-safe posture are preserved;
- [ ] public-safe transformation support exists where required;
- [ ] correction and rollback targets are traceable;
- [ ] digests or integrity refs bind each file to the release record.

If any gate is unresolved, hold the artifact upstream.

[Back to top](#top)

---

## 6. Geology GeoParquet rules

| Rule | Public GeoParquet posture |
|---|---|
| Format is a carrier, not authority | GeoParquet files are released artifacts; they do not define release, truth, policy, schema, or evidence. |
| Geometry metadata is explicit | Geometry column, geometry type, CRS, bounds/extent, spatial resolution or aggregation scope, and geometry validity must be discoverable. |
| Interpretation is labeled | Correlations, structures, units, resource estimates, and cross sections remain interpreted products unless evidence supports another role. |
| Observation is not regulation | Administrative or regulatory records do not become observed events without separate evidence. |
| Estimate is not per-place truth | Aggregate or modeled resource estimates must preserve aggregation scope, uncertainty, and caveats. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not collapse. |
| Time semantics are explicit | Source vintage, observation, valid, retrieval, release, correction, and review times are preserved where material. |
| Rights travel with the file | License, source rights, audience class, and allowed reuse posture must be clear. |
| Cross-lane context stays owned | Hydrology, Soil, Hazards, People/Land, Infrastructure, Agriculture, Archaeology, Flora, and Fauna context keep their own truth. |
| AI is not root truth | AI summaries can consume released files but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/geoparquet/geology/
├── README.md
├── layers/
│   └── <release_id>/
├── geologic_units/
│   └── <release_id>/
├── stratigraphy/
│   └── <release_id>/
├── structures/
│   └── <release_id>/
├── subsurface_references/
│   └── <release_id>/
├── resource_context/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── geology-geoparquet-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file names:

```text
geology.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.parquet
geology.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.manifest.json
geology.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.checksums.txt
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing a GeoParquet artifact under this sublane, verify:

- [ ] The artifact is release-approved and public-safe for the intended audience.
- [ ] The release record points to this artifact.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Geometry column, CRS, geometry type, bounds/extent, time fields, source role, aggregation scope, uncertainty, caveats, schema/profile version, rights/license posture, and public-safe posture are preserved.
- [ ] Public-safe transforms are traceable where required.
- [ ] The artifact does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, API payload, or release authority.
- [ ] The artifact has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.
- [ ] Parent `data/published/geoparquet/README.md` is updated before this format lane becomes operationally mature.

[Back to top](#top)

---

## 9. Definition of done

This sublane is operationally mature when:

- [ ] `data/published/geoparquet/README.md` defines the parent GeoParquet published-data contract.
- [ ] Geology GeoParquet contracts, schemas, and fixtures exist under approved homes.
- [ ] Release tooling writes or verifies GeoParquet artifacts only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, invalid GeoParquet/profile metadata, missing CRS, invalid geometry, missing rights posture, interpretation/observation collapse, estimate/per-place collapse, regulatory/observed collapse, source-role collapse, missing caveats, missing review state, and unsafe public fields.
- [ ] Valid and invalid fixtures cover geologic-unit, stratigraphy/lithology, structure/cross-section, subsurface-reference, resource-context, corrected release, superseded release, and rollback packages.
- [ ] Governed download/export routes are documented and tested.

---

## Maintainer note

Published Geology GeoParquet files are reusable artifacts that may travel outside the KFM UI. Keep them boring, citable, schema-aware, geometry-aware, source-role-aware, rights-aware, uncertainty-aware, audience-aware, and reversible. If evidence, validation, rights, policy, review, release, correction, or rollback support is incomplete, keep the file upstream instead of placing it here.
