<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/habitat/readme
title: data/published/habitat README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): habitat domain steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: public-review
path: data/published/habitat/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../raw/habitat/README.md
  - ../../work/habitat/README.md
  - ../../quarantine/habitat/README.md
  - ../../processed/habitat/README.md
  - ../../catalog/domain/habitat/README.md
  - ../../triplets/habitat/README.md
  - ../../proofs/habitat/README.md
  - ../../proofs/validation_report/habitat/README.md
  - ../../receipts/README.md
  - ../../../release/README.md
  - ../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
notes:
  - "Directory README for released Habitat carriers. It replaces a greenfield stub."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, or prove claims."
  - "Use this lane only for released public-facing carriers with evidence, validation, policy, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/habitat/`

> Published Habitat lane for released, public-facing Habitat carriers that have passed KFM release gates and are safe for governed API, approved released-artifact, map, report, export, or UI use.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: habitat](https://img.shields.io/badge/domain-habitat-2ea44f)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): habitat domain steward` · `TODO(owner): publication steward` · `TODO(owner): release steward`  
> **Path:** `data/published/habitat/README.md`  
> **Truth posture:** CONFIRMED target path and Habitat domain/lifecycle docs from current repo evidence / PROPOSED child layout and instance naming / NEEDS VERIFICATION for emitted artifacts, release manifests, schemas, validators, CI checks, and governed API routes.

> [!WARNING]
> This directory is not release authority. Placement here must follow release records, evidence support, validation, policy review, catalog closure, correction path, and rollback support. If that support is incomplete, keep the artifact upstream.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this published lane is for. |
| [2. Repo fit](#2-repo-fit) | How this path relates to lifecycle and authority roots. |
| [3. Accepted artifacts](#3-accepted-artifacts) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Release checks](#5-release-checks) | Minimum checks before adding files. |
| [6. Suggested layout](#6-suggested-layout) | Proposed child structure and naming. |
| [7. Definition of done](#7-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/habitat/` is the Habitat domain's published carrier lane. It is downstream of release and should contain only public-facing artifacts that have already passed KFM promotion gates.

This lane may hold released carriers such as:

- map-layer files;
- API payload snapshots;
- report carriers;
- export packages;
- GeoParquet packages;
- tile or package carriers;
- public summary files;
- public index manifests; and
- retired or superseded public artifacts with correction, withdrawal, or rollback references.

This lane should not contain raw source captures, working candidates, held material, processed candidates, catalog drafts, proof objects, receipts, policy logic, release decisions, schemas, semantic contracts, or unreleased model/AI outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role | Boundary |
|---|---|---|
| [`../../raw/habitat/`](../../raw/habitat/) | Source captures. | Not public-readable. |
| [`../../work/habitat/`](../../work/habitat/) | Working candidates. | Not public-readable. |
| [`../../quarantine/habitat/`](../../quarantine/habitat/) | Held material. | Not public-readable. |
| [`../../processed/habitat/`](../../processed/habitat/) | Validated candidates. | Upstream of release. |
| [`../../catalog/domain/habitat/`](../../catalog/domain/habitat/) | Catalog records. | Discovery and lineage, not release authority. |
| [`../../triplets/habitat/`](../../triplets/habitat/) | Graph projection. | Not public by itself. |
| [`../../proofs/habitat/`](../../proofs/habitat/) | Proof support. | Support, not published carrier. |
| [`../../proofs/validation_report/habitat/`](../../proofs/validation_report/habitat/) | Validation reports. | Gate support, not publication authority. |
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
| Released public summary | `public_summaries/<release_id>/<summary_slug>.json` | Public-facing posture, evidence refs. |
| Released public index | `indexes/published-habitat-index.json` | Points to release-approved artifacts only. |
| Retired public artifact | `retired/<release_id>/<artifact_slug>.*` | Supersession, correction, withdrawal, or rollback reference. |

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads or source-system dumps | `data/raw/habitat/` |
| Working or held candidates | `data/work/habitat/` or `data/quarantine/habitat/` |
| Processed normalized data | `data/processed/habitat/` |
| Catalog records | `data/catalog/` |
| Proof objects or validation reports | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records and decisions | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
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
- [ ] review state exists where required;
- [ ] correction and rollback paths are recorded;
- [ ] digests or integrity refs bind the artifact to the release record; and
- [ ] public clients consume the artifact only through governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 6. Suggested layout

```text
data/published/habitat/
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
├── public_summaries/
│   └── <release_id>/
├── indexes/
│   └── published-habitat-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
habitat.published.<artifact_family>.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 7. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] Habitat published artifact contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies Habitat published artifacts only after release authority is present.
- [ ] Validators block unreleased candidates, missing evidence, missing release refs, missing rollback, source-role collapse, unsafe public carriers, and missing correction path.
- [ ] Valid and invalid fixtures cover map, API payload, report, export, GeoParquet, public summary, corrected release, superseded release, and rollback target.
- [ ] Governed API or released-artifact routes are documented and tested.

---

## Maintainer note

Published Habitat artifacts are public-facing carriers, not root truth. Keep them citable, release-linked, review-aware, correction-ready, and reversible. If release support is incomplete, keep the artifact upstream instead of placing it here.
