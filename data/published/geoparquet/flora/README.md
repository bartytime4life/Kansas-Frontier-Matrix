<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/geoparquet/flora/readme
title: data/published/geoparquet/flora README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): flora domain steward
  - TODO(owner): geospatial export steward
  - TODO(owner): publication steward
  - TODO(owner): sensitivity reviewer
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
path: data/published/geoparquet/flora/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../flora/README.md
  - ../../exports/README.md
  - ../../api_payloads/flora/README.md
  - ../../../README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../catalog/domain/flora/README.md
  - ../../../proofs/flora/README.md
  - ../../../proofs/validation_report/flora/README.md
  - ../../../receipts/README.md
  - ../../../../release/README.md
  - ../../../../docs/domains/flora/ARCHITECTURE.md
  - ../../../../docs/domains/flora/RELEASE_INDEX.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../contracts/README.md
  - ../../../../schemas/README.md
  - ../../../../policy/README.md
notes:
  - "Directory README for released Flora GeoParquet carriers under data/published/geoparquet/. It replaces a placeholder file."
  - "This lane stores release-linked GeoParquet files or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted GeoParquet files, schemas, validators, CI, or governed download routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/geoparquet/flora/`

> Published GeoParquet sublane for released, public-safe **Flora** geospatial table carriers. Files here should be immutable, release-linked `.parquet` / GeoParquet packages consumed through governed download, approved released-artifact, or governed API paths.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: flora](https://img.shields.io/badge/domain-flora-2e7d32)
![Carrier: GeoParquet](https://img.shields.io/badge/carrier-GeoParquet-blue)
![Policy: restricted review](https://img.shields.io/badge/policy-restricted--review-b91c1c)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): flora domain steward` · `TODO(owner): geospatial export steward` · `TODO(owner): publication steward` · `TODO(owner): sensitivity reviewer` · `TODO(owner): release steward`  
> **Path:** `data/published/geoparquet/flora/README.md`  
> **Truth posture:** CONFIRMED target path, parent `geoparquet/` stub, Flora published lane, and Flora architecture from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted GeoParquet artifacts, formal format profile, schemas, validators, release manifests, CI checks, and governed download routes.

> [!WARNING]
> This directory does not approve publication and is not a raw-data outlet. GeoParquet files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, review state is complete where required, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this GeoParquet sublane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted GeoParquet carriers](#3-accepted-geoparquet-carriers) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Publication gates](#5-publication-gates) | Minimum support before artifacts land here. |
| [6. Flora GeoParquet rules](#6-flora-geoparquet-rules) | Format and domain guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing artifacts. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/geoparquet/flora/` is the published carrier lane for release-approved Flora GeoParquet files and packages.

Use this lane for geospatial tabular artifacts that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- packaged for governed download, reproducible reuse, released-artifact distribution, or governed API handoff;
- explicit about plant taxonomic identity, source role, evidence support, geometry type, CRS, schema/profile version, observation/valid/retrieval/release time, uncertainty, caveats, license/rights posture, digest, and correction status; and
- scoped to public-safe Flora products such as botanical summaries, vegetation-community context, phenology summaries, range/context products, invasive-plant context, restoration context, or generalized occurrence/specimen derivatives.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, restricted source material, steward-only detail, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/published/geoparquet/` | Parent GeoParquet carrier lane. | Parent contract is still a greenfield stub; this child README does not complete it. |
| `data/published/flora/` | Domain published lane. | Defines Flora published-carrier posture. |
| `data/published/exports/` | Generic export carriers. | GeoParquet is a format-specific published export lane. |
| `data/published/api_payloads/flora/` | Released API-shaped Flora payloads. | API JSON payloads are separate from GeoParquet packages. |
| `data/raw/flora/` | Source captures. | Not public-readable. |
| `data/work/flora/` | Working candidates. | Not public-readable. |
| `data/quarantine/flora/` | Held material. | Not public-readable. |
| `data/processed/flora/` | Validated candidates. | Upstream of release. |
| `data/catalog/domain/flora/` | Catalog records. | Discovery and lineage, not release authority. |
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
| Released Flora GeoParquet layer | `layers/<release_id>/<layer_slug>.parquet` | ReleaseManifest, EvidenceBundle refs, policy decision, validation report, review refs, rollback target. |
| Released botanical summary package | `botanical_summaries/<release_id>/<summary_slug>.parquet` | Taxonomic identity, source role, evidence, caveats, release refs. |
| Released vegetation-community package | `vegetation_communities/<release_id>/<community_slug>.parquet` | Evidence refs, classification context, release refs. |
| Released phenology package | `phenology/<release_id>/<phenology_slug>.parquet` | Time scope, method context, evidence refs, release refs. |
| Released range/context package | `range_context/<release_id>/<context_slug>.parquet` | Public-safe geometry, uncertainty, caveats, release refs. |
| Released package manifest | `manifests/<release_id>/<package_slug>.manifest.json` | File list, checksums, schema/profile refs, release refs. |
| Released public index | `indexes/flora-geoparquet-index.json` | Points to release-approved files only. |
| Superseded GeoParquet artifact | `retired/<release_id>/<artifact_slug>.parquet` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| RAW source payloads, herbarium/specimen exports, survey exports, media, field notes, or source-system dumps | `data/raw/flora/` |
| Working or held candidates | `data/work/flora/` or `data/quarantine/flora/` |
| Processed normalized data | `data/processed/flora/` |
| Catalog records | `data/catalog/` |
| Proof objects, validation reports, review records, or EvidenceBundles | `data/proofs/` |
| Receipts, transform receipts, redaction/generalization receipts, model-run receipts, or AI receipts | `data/receipts/` or approved proof/receipt homes |
| API payload snapshots | `data/published/api_payloads/flora/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas, profile definitions, or validator source | `schemas/`, `contracts/`, `tests/`, or approved tooling roots |
| Restricted botanical source material, steward-only details, or rights-unclear source detail | Upstream restricted/held lanes until cleared for public release. |
| Direct model output or unreviewed AI summaries | Governed AI/review paths before release. |

[Back to top](#top)

---

## 5. Publication gates

Before a Flora GeoParquet artifact is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema, GeoParquet/profile, geometry, CRS, and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class and downloadable format;
- [ ] review records exist where required;
- [ ] plant taxonomic identity, source role, geometry scope, time scope, uncertainty, caveats, rights/license posture, and public-safe posture are preserved;
- [ ] public-safe transformation support exists where required;
- [ ] correction and rollback targets are traceable;
- [ ] digests or integrity refs bind each file to the release record.

If any gate is unresolved, hold the artifact upstream.

[Back to top](#top)

---

## 6. Flora GeoParquet rules

| Rule | Public GeoParquet posture |
|---|---|
| Format is a carrier, not authority | GeoParquet files are released artifacts; they do not define release, truth, policy, schema, or evidence. |
| Geometry metadata is explicit | Geometry column, geometry type, CRS, bounds/extent, spatial resolution or aggregation scope, and geometry validity must be discoverable. |
| Taxonomy is explicit | Public files preserve plant taxon identity, source authority, and unresolved-conflict posture where material. |
| Source role is preserved | Candidate, observed, regulatory, modeled, aggregate, administrative, and synthetic roles must not collapse. |
| Public/restricted split is preserved | Public files must not include restricted source material or steward-only details. |
| Transform support is auditable | Public-safe transformations must be traceable through proof or receipt references where required. |
| Time semantics are explicit | Observation, valid, retrieval, release, correction, and review times are preserved where material. |
| Rights travel with the file | License, source rights, audience class, and allowed reuse posture must be clear. |
| Cross-lane context stays owned | Habitat, Fauna, Soil, Hydrology, Agriculture, Hazards, Roads, People/Land, Settlement, and Archaeology context keep their own truth. |
| AI is not root truth | AI summaries can consume released files but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/geoparquet/flora/
├── README.md
├── layers/
│   └── <release_id>/
├── botanical_summaries/
│   └── <release_id>/
├── vegetation_communities/
│   └── <release_id>/
├── phenology/
│   └── <release_id>/
├── range_context/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── flora-geoparquet-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file names:

```text
flora.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.parquet
flora.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.manifest.json
flora.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.checksums.txt
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing a GeoParquet artifact under this sublane, verify:

- [ ] The artifact is release-approved and public-safe for the intended audience.
- [ ] The release record points to this artifact.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Geometry column, CRS, geometry type, bounds/extent, time fields, plant taxonomic identity, source role, caveats, schema/profile version, rights/license posture, and public-safe posture are preserved.
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
- [ ] Flora GeoParquet contracts, schemas, and fixtures exist under approved homes.
- [ ] Release tooling writes or verifies GeoParquet artifacts only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, invalid GeoParquet/profile metadata, missing CRS, invalid geometry, unresolved taxonomic identity, public/restricted collapse, source-role collapse, missing transform references, missing caveats, missing rights/license posture, missing review state, and unsafe public fields.
- [ ] Valid and invalid fixtures cover botanical summary, vegetation-community, phenology, range/context, corrected release, superseded release, and rollback packages.
- [ ] Governed download/export routes are documented and tested.

---

## Maintainer note

Published Flora GeoParquet files are reusable artifacts that may travel outside the KFM UI. Keep them boring, citable, schema-aware, geometry-aware, taxonomy-aware, rights-aware, review-aware, public-safe, transform-aware, audience-aware, and reversible. If evidence, taxonomy, validation, policy, review, rights, release, correction, or rollback support is incomplete, keep the file upstream instead of placing it here.
