<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/geoparquet/readme
title: data/published/geoparquet README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): geospatial export steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
  - TODO(owner): domain stewards
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/geoparquet/README.md
related:
  - ../README.md
  - ../exports/README.md
  - ../api_payloads/README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../receipts/README.md
  - ../../../release/README.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - atmosphere/README.md
  - flora/README.md
  - geology/README.md
notes:
  - "Parent README for released GeoParquet carriers under data/published/. It replaces a greenfield stub."
  - "This lane stores release-linked GeoParquet files or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted GeoParquet files, formal profile schemas, validators, CI, or governed download routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/geoparquet/`

> Parent published-data lane for released, public-safe KFM **GeoParquet carriers**: immutable `.parquet` geospatial table files, package manifests, checksums, and public indexes that have passed release gates and are safe for governed download, approved released-artifact distribution, or governed API handoff.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Carrier: GeoParquet](https://img.shields.io/badge/carrier-GeoParquet-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): geospatial export steward` · `TODO(owner): publication steward` · `TODO(owner): release steward` · `TODO(owner): domain stewards`  
> **Path:** `data/published/geoparquet/README.md`  
> **Truth posture:** CONFIRMED target path and authored child GeoParquet lane READMEs from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted GeoParquet artifacts, formal format profile, schemas, validators, release manifests, CI checks, and governed download routes.

> [!WARNING]
> This directory does not approve publication and is not a raw-data outlet. GeoParquet files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, rights posture is known, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this parent GeoParquet lane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted carriers](#3-accepted-carriers) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Child lane index](#5-child-lane-index) | Authored domain GeoParquet lanes. |
| [6. Publication gates](#6-publication-gates) | Minimum support before files land here. |
| [7. GeoParquet carrier rules](#7-geoparquet-carrier-rules) | Cross-domain format guardrails. |
| [8. Suggested layout](#8-suggested-layout) | Proposed child structure. |
| [9. Maintenance checklist](#9-maintenance-checklist) | Checks before adding or changing files. |
| [10. Definition of done](#10-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/geoparquet/` is the parent published carrier lane for release-approved GeoParquet files and packages across KFM domains.

Use this lane for geospatial tabular artifacts that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- packaged for governed download, reproducible reuse, released-artifact distribution, or governed API handoff;
- explicit about geometry column, geometry type, CRS, bounds/extent, schema/profile version, source role, evidence support, time scope, caveats, rights/license posture, digest, and correction status; and
- owned by a domain child lane that preserves its own source-role, sensitivity, rights, and public-surface rules.

This lane is downstream of release. It should not contain source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, schemas, policy rules, release decisions, or direct model output.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| `data/raw/<domain>/` | Source capture lanes. | Not public-readable. |
| `data/work/<domain>/` | Working candidate lanes. | Not public-readable. |
| `data/quarantine/<domain>/` | Held-material lanes. | Not public-readable. |
| `data/processed/<domain>/` | Validated candidate lanes. | Upstream of release. |
| `data/catalog/` | Catalog lanes. | Discovery and lineage, not release authority. |
| `data/proofs/` | Proof-support lanes. | Support, not published GeoParquet. |
| `data/receipts/` | Process-memory lanes. | Receipts do not publish. |
| `data/published/exports/` | Generic export carriers. | GeoParquet is a format-specific published export lane. |
| `data/published/api_payloads/` | Released API-shaped carriers. | API JSON payloads are separate from GeoParquet files. |
| `release/` | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| `contracts/` | Semantic meaning. | GeoParquet files conform; they do not define meaning. |
| `schemas/` | Machine shape. | GeoParquet files validate; schemas live elsewhere. |
| `policy/` | Admissibility. | GeoParquet files carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted carriers

Use this directory only for release-linked, public-safe GeoParquet carriers.

| Carrier type | Suggested placement | Required support |
|---|---|---|
| Released domain GeoParquet layer | `<domain>/layers/<release_id>/<layer_slug>.parquet` | ReleaseManifest, EvidenceBundle refs, policy decision, validation report, rollback target. |
| Released domain package | `<domain>/<artifact_family>/<release_id>/<package_slug>.parquet` | Domain-specific support, source role, evidence, release refs. |
| Released cross-domain package | `cross_domain/<scope>/<release_id>/<package_slug>.parquet` | Owning-lane refs, source-role preservation, policy and release refs. |
| Released package manifest | `<domain>/manifests/<release_id>/<package_slug>.manifest.json` | File list, checksums, schema/profile refs, release refs. |
| Released checksum file | `<domain>/manifests/<release_id>/<package_slug>.checksums.txt` | Digest binding to release record. |
| Released public index | `indexes/geoparquet-index.json` | Points to release-approved GeoParquet files only. |
| Superseded GeoParquet artifact | `<domain>/retired/<release_id>/<artifact_slug>.parquet` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source-system exports, raw `.parquet`, source rasters, logs, or dumps | `data/raw/<domain>/` |
| Working or held candidates | `data/work/<domain>/` or `data/quarantine/<domain>/` |
| Processed normalized data | `data/processed/<domain>/` |
| Catalog records | `data/catalog/` |
| Proof objects, validation reports, review records, or EvidenceBundles | `data/proofs/` |
| Receipts, transform receipts, model-run receipts, representation receipts, aggregation receipts, or AI receipts | `data/receipts/` or approved proof/receipt homes |
| API payload snapshots | `data/published/api_payloads/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas, profile definitions, validators, tests, or fixtures | `schemas/`, `contracts/`, `tests/`, `fixtures/`, or approved tooling roots |
| Restricted, rights-unclear, proprietary, or steward-only source detail | Upstream restricted/held lanes until cleared for public release. |
| Direct model output or unreviewed AI summaries | Governed AI/review paths before release. |

[Back to top](#top)

---

## 5. Child lane index

| Lane | Current role |
|---|---|
| [`atmosphere/`](./atmosphere/) | Released Atmosphere / Air GeoParquet carriers. |
| [`flora/`](./flora/) | Released Flora GeoParquet carriers. |
| [`geology/`](./geology/) | Released Geology and Natural Resources GeoParquet carriers. |

Additional domains should get a child README before live GeoParquet instances land there.

[Back to top](#top)

---

## 6. Publication gates

Before a GeoParquet artifact is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema, GeoParquet/profile, geometry, CRS, and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class and downloadable format;
- [ ] rights and source terms are compatible with the public carrier;
- [ ] review records exist where required by sensitivity, rights, source terms, or materiality;
- [ ] source role, geometry scope, time scope, uncertainty, caveats, rights/license posture, and public-safe posture are preserved;
- [ ] correction and rollback targets are traceable;
- [ ] digests or integrity refs bind each file to the release record.

If any gate is unresolved, hold the artifact upstream.

[Back to top](#top)

---

## 7. GeoParquet carrier rules

| Rule | Public GeoParquet posture |
|---|---|
| Format is a carrier, not authority | GeoParquet files are released artifacts; they do not define release, truth, policy, schema, or evidence. |
| Geometry metadata is explicit | Geometry column, geometry type, CRS, bounds/extent, spatial resolution or aggregation scope, and geometry validity must be discoverable. |
| Schema/profile is explicit | GeoParquet/profile version, KFM schema version, field dictionary, units, null semantics, and enum meanings must be discoverable. |
| Time semantics are explicit | Source, observation, valid, retrieval, release, correction, and review times are preserved where material. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, and domain-specific roles must not collapse. |
| Rights travel with the file | License, source rights, audience class, and allowed reuse posture must be clear. |
| Domain rules still apply | Atmosphere, Flora, Geology, and future child lanes keep their own truth, sensitivity, caveat, and review rules. |
| Corrections are expected | Files must support correction, supersession, withdrawal, and rollback. |
| AI is not root truth | AI summaries can consume released files but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 8. Suggested layout

```text
data/published/geoparquet/
├── README.md
├── <domain>/
│   ├── README.md
│   ├── layers/
│   │   └── <release_id>/
│   ├── <artifact_family>/
│   │   └── <release_id>/
│   ├── manifests/
│   │   └── <release_id>/
│   ├── indexes/
│   │   └── <domain>-geoparquet-index.json
│   └── retired/
│       └── <release_id>/
├── cross_domain/
│   └── <scope>/
│       └── <release_id>/
└── indexes/
    └── geoparquet-index.json
```

Suggested deterministic file names:

```text
<domain>.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.parquet
<domain>.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.manifest.json
<domain>.published.geoparquet.<artifact_family>.<scope>.<release_id>.<short_hash>.checksums.txt
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 9. Maintenance checklist

Before adding or changing a GeoParquet artifact under this parent lane, verify:

- [ ] The artifact is release-approved and public-safe for the intended audience.
- [ ] The release record points to this artifact.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Geometry column, CRS, geometry type, bounds/extent, time fields, source role, caveats, schema/profile version, rights/license posture, and public-safe posture are preserved.
- [ ] The artifact does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, API payload, or release authority.
- [ ] The artifact has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.
- [ ] Domain-specific GeoParquet rules are documented in the relevant child lane README before live files land there.

[Back to top](#top)

---

## 10. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] GeoParquet contracts, schemas, profiles, tests, and fixtures exist under approved homes.
- [ ] Release tooling writes or verifies GeoParquet artifacts only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, invalid GeoParquet/profile metadata, missing CRS, invalid geometry, missing rights posture, source-role collapse, missing caveats, missing review state where required, and unsafe public fields.
- [ ] Valid and invalid fixtures cover domain layer packages, cross-domain packages, manifests, checksums, corrections, supersessions, withdrawals, and rollback packages.
- [ ] Governed download/export routes are documented and tested.
- [ ] Active domains have child GeoParquet README files before live GeoParquet instances land there.

---

## Maintainer note

Published GeoParquet files are reusable artifacts that may travel outside the KFM UI. Keep them boring, citable, schema-aware, geometry-aware, source-role-aware, rights-aware, domain-aware, audience-aware, and reversible. If evidence, validation, rights, policy, review, release, correction, or rollback support is incomplete, keep the file upstream instead of placing it here.
