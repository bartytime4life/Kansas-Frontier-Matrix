<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/hydrology/readme
title: data/published/hydrology README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): hydrology domain steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/hydrology/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../raw/hydrology/README.md
  - ../../work/hydrology/README.md
  - ../../quarantine/hydrology/README.md
  - ../../processed/hydrology/README.md
  - ../../catalog/domain/hydrology/README.md
  - ../../triplets/hydrology/README.md
  - ../../proofs/hydrology/README.md
  - ../../proofs/validation_report/hydrology/README.md
  - ../../receipts/README.md
  - ../../../release/README.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
notes:
  - "Directory README for released Hydrology carriers. It replaces a greenfield stub."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Hydrology published carriers must preserve boundary discipline: regulatory context is not observed flooding, hydrology is not alert authority, and cross-lane truths remain owned by their lanes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/hydrology/`

> Published Hydrology lane for released, public-facing water and watershed carriers that have passed KFM release gates and are safe for governed API, approved released-artifact, map, report, export, timeline, or UI use.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: hydrology](https://img.shields.io/badge/domain-hydrology-1f6feb)
![Boundary: not alert authority](https://img.shields.io/badge/boundary-not--alert--authority-critical)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): hydrology domain steward` · `TODO(owner): publication steward` · `TODO(owner): release steward`  
> **Path:** `data/published/hydrology/README.md`  
> **Truth posture:** CONFIRMED target path and Hydrology boundary/API/ADR docs from current repo evidence / PROPOSED child layout and instance naming / NEEDS VERIFICATION for emitted artifacts, release manifests, schemas, validators, CI checks, and governed API routes.

> [!WARNING]
> This directory is not release authority and is not an emergency-warning surface. Placement here must follow release records, evidence support, validation, policy review, catalog closure, correction path, and rollback support. If that support is incomplete, keep the artifact upstream.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this published lane is for. |
| [2. Repo fit](#2-repo-fit) | How this path relates to lifecycle and authority roots. |
| [3. Accepted artifacts](#3-accepted-artifacts) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Release checks](#5-release-checks) | Minimum checks before adding files. |
| [6. Hydrology boundary rules](#6-hydrology-boundary-rules) | Source-role and cross-lane guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure and naming. |
| [8. Definition of done](#8-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/hydrology/` is the Hydrology domain's published carrier lane. It is downstream of release and should contain only public-facing artifacts that have already passed KFM promotion gates.

This lane may hold released carriers such as:

- watershed and HUC context map layers;
- hydrography, reach, waterbody, and network-trace carriers;
- gauge-site, flow, stage, water-level, water-quality, or groundwater summaries;
- regulatory flood-context carriers with role and version labels;
- observed historical flood-event carriers with evidence support;
- API payload snapshots;
- report carriers;
- export or GeoParquet packages;
- public index manifests; and
- retired or superseded public artifacts with correction, withdrawal, or rollback references.

This lane should not contain raw source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, policy logic, release decisions, schemas, semantic contracts, live emergency-warning workflows, regulatory determinations, or unreleased model/AI outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| [`../../raw/hydrology/`](../../raw/hydrology/) | Source captures. | Not public-readable. |
| [`../../work/hydrology/`](../../work/hydrology/) | Working candidates. | Not public-readable. |
| [`../../quarantine/hydrology/`](../../quarantine/hydrology/) | Held material. | Not public-readable. |
| [`../../processed/hydrology/`](../../processed/hydrology/) | Validated candidates. | Upstream of release. |
| [`../../catalog/domain/hydrology/`](../../catalog/domain/hydrology/) | Catalog records. | Discovery and lineage, not release authority. |
| [`../../triplets/hydrology/`](../../triplets/hydrology/) | Graph projection. | Not public by itself. |
| [`../../proofs/hydrology/`](../../proofs/hydrology/) | Proof support. | Support, not published carrier. |
| [`../../proofs/validation_report/hydrology/`](../../proofs/validation_report/hydrology/) | Validation reports. | Gate support, not publication authority. |
| [`../../receipts/`](../../receipts/) | Process memory. | Receipts do not publish. |
| [`../../../release/`](../../../release/) | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| [`../../../contracts/`](../../../contracts/) | Semantic meaning. | Published artifacts conform; they do not define meaning. |
| [`../../../schemas/`](../../../schemas/) | Machine shape. | Published artifacts validate; schemas live elsewhere. |
| [`../../../policy/`](../../../policy/) | Admissibility. | Published artifacts carry outcomes; policy lives elsewhere. |

[Back to top](#top)

---

## 3. Accepted artifacts

| Artifact type | Suggested placement | Required support |
|---|---|---|
| Released map carrier | `layers/<release_id>/<layer_slug>.*` | Release, evidence, validation, policy, rollback refs. |
| Released API payload | `api_payloads/<release_id>/<payload_slug>.json` | Schema validation, release refs, correction path. |
| Released report carrier | `reports/<release_id>/<report_slug>.md` or `.json` | Citations, evidence refs, release refs. |
| Released export package | `exports/<release_id>/<export_slug>.*` | Schema/version, audience class, release refs. |
| Released GeoParquet package | `geoparquet/<release_id>/<package_slug>.parquet` | Profile metadata, CRS, digest, release refs. |
| Released timeline or hydrograph package | `time_series/<release_id>/<series_slug>.*` | Time scope, units, qualifiers, evidence refs. |
| Released public summary | `public_summaries/<release_id>/<summary_slug>.json` | Public-facing posture, evidence refs. |
| Released public index | `indexes/published-hydrology-index.json` | Points to release-approved artifacts only. |
| Retired public artifact | `retired/<release_id>/<artifact_slug>.*` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads or source-system dumps | `data/raw/hydrology/` |
| Working or held candidates | `data/work/hydrology/` or `data/quarantine/hydrology/` |
| Processed normalized data | `data/processed/hydrology/` |
| Catalog records | `data/catalog/` |
| Proof objects or validation reports | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records and decisions | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
| Emergency warning or life-safety instruction surfaces | Outside KFM published carrier authority. |
| Direct model output or unreviewed AI summaries | Governed review paths before release. |

[Back to top](#top)

---

## 5. Release checks

Before adding or changing files here, verify:

- [ ] release authority exists under `release/`;
- [ ] evidence refs resolve for consequential claims;
- [ ] validation reports passed or recorded finite outcomes;
- [ ] catalog closure exists;
- [ ] policy state allows the target audience;
- [ ] source role and knowledge character are preserved;
- [ ] unit, datum, qualifier, time scope, freshness, effective date, or stale-state posture is recorded where material;
- [ ] correction and rollback paths are recorded;
- [ ] digests or integrity refs bind the artifact to the release record; and
- [ ] public clients consume the artifact only through governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 6. Hydrology boundary rules

| Rule | Public posture |
|---|---|
| Not alert authority | Published Hydrology files are water-context carriers, not emergency warnings or life-safety instructions. |
| Regulatory is not observed | Regulatory flood-context carriers must not be presented as observed inundation, forecast, or hydraulic-model truth. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and derived roles must not collapse. |
| Time and units are explicit | Observation time, valid time, retrieval time, release time, unit, datum, qualifier, and correction state are preserved where material. |
| Evidence is mandatory | Claims require evidence support and citation posture. Missing support means abstain or hold. |
| Cross-lane truth stays owned | Soil, Agriculture, Geology, Infrastructure, Hazards, People/Land, Flora, Fauna, Habitat, and Spatial Foundation keep their own truth. |
| AI is not root truth | AI summaries can consume released evidence but cannot replace EvidenceBundles, validation, release, or citations. |
| Corrections are expected | Public artifacts must support correction, supersession, withdrawal, and rollback. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/hydrology/
├── README.md
├── layers/
│   └── <release_id>/
├── api_payloads/
│   └── <release_id>/
├── reports/
│   └── <release_id>/
├── exports/
│   └── <release_id>/
├── geoparquet/
│   └── <release_id>/
├── time_series/
│   └── <release_id>/
├── public_summaries/
│   └── <release_id>/
├── indexes/
│   └── published-hydrology-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
hydrology.published.<artifact_family>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] Hydrology published artifact contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies Hydrology published artifacts only after release authority is present.
- [ ] Validators block unreleased candidates, missing evidence, missing release refs, missing rollback, source-role collapse, regulatory/observed collapse, missing units or time semantics, unsafe public carriers, and missing correction path.
- [ ] Valid and invalid fixtures cover map, API payload, report, export, GeoParquet, time series, public summary, corrected release, superseded release, and rollback target.
- [ ] Governed API or released-artifact routes are documented and tested.

---

## Maintainer note

Published Hydrology artifacts are public-facing carriers, not root truth and not emergency systems. Keep them citable, source-role-aware, time-aware, unit-aware, release-linked, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream instead of placing it here.
