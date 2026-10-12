<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/exports/readme
title: data/published/exports README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): export steward
  - TODO(owner): publication steward
  - TODO(owner): release steward
  - TODO(owner): domain stewards
created: 2026-06-25
updated: 2026-06-25
policy_label: public-review
path: data/published/exports/README.md
related:
  - ../README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../receipts/README.md
  - ../api_payloads/README.md
  - ../../../release/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/README.md
  - ../../../schemas/README.md
  - ../../../policy/README.md
notes:
  - "Parent README for released downloadable/export carriers under data/published/. It replaces a greenfield stub."
  - "This lane stores release-linked export files or packages only after release gates pass."
  - "This README describes placement and boundaries; it does not prove emitted exports, schemas, validators, CI, or governed export routes exist."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/exports/`

> Parent published-data lane for released, public-safe KFM **export carriers**: downloadable snapshots, tabular packages, GeoJSON/CSV/Parquet bundles, report-data attachments, and other reusable public artifacts that have passed release gates.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Carrier: export](https://img.shields.io/badge/carrier-export-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Truth: cite or abstain](https://img.shields.io/badge/truth-cite--or--abstain-6f42c1)

> [!IMPORTANT]
> **Status:** `draft`  
> **Owners:** `TODO(owner): data steward` · `TODO(owner): export steward` · `TODO(owner): publication steward` · `TODO(owner): release steward` · `TODO(owner): domain stewards`  
> **Path:** `data/published/exports/README.md`  
> **Truth posture:** CONFIRMED target path from current repo evidence / PROPOSED child layout and naming / NEEDS VERIFICATION for emitted export artifacts, schemas, validators, release manifests, CI checks, and governed export routes.

> [!WARNING]
> This directory does not approve publication and is not a raw-data outlet. Export files belong here only after release authority exists under `release/`, evidence and catalog closure are complete, validation gates pass, policy state is recorded, and rollback/correction paths are available.

---

## Quick jumps

| Section | Use it for |
|---|---|
| [1. Scope](#1-scope) | What this parent export lane is for. |
| [2. Repo fit](#2-repo-fit) | Neighboring authority roots. |
| [3. Accepted exports](#3-accepted-exports) | What may live here after release. |
| [4. Exclusions](#4-exclusions) | What must stay out. |
| [5. Publication gates](#5-publication-gates) | Minimum support before exports land here. |
| [6. Export carrier rules](#6-export-carrier-rules) | Cross-domain public export guardrails. |
| [7. Suggested layout](#7-suggested-layout) | Proposed child structure. |
| [8. Maintenance checklist](#8-maintenance-checklist) | Checks before adding or changing exports. |
| [9. Definition of done](#9-definition-of-done) | What remains before maturity. |

---

## 1. Scope

`data/published/exports/` is the parent published carrier lane for release-approved export files and export packages across KFM domains.

Use this lane for exports that are:

- tied to a release record;
- public-safe for the declared audience;
- traceable to evidence, catalog, validation, policy, review, correction, and rollback references;
- packaged for governed download, public UI export, report attachment, data handoff, or reproducible reuse; and
- explicit about source role, evidence support, schema/version, time scope, caveats, license/rights posture, digest, and correction status.

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
| `data/proofs/` | Proof-support lanes. | Support, not published exports. |
| `data/receipts/` | Process-memory lanes. | Receipts do not publish. |
| `data/published/api_payloads/` | Released API-shaped carriers. | API payloads are separate from downloadable export packages. |
| `release/` | Release authority. | Manifests, correction, withdrawal, rollback, signatures. |
| `contracts/` | Semantic meaning. | Exports conform; they do not define meaning. |
| `schemas/` | Machine shape. | Exports validate; they do not define schemas. |
| `policy/` | Admissibility. | Exports carry outcomes; policy lives elsewhere. |

> [!NOTE]
> `data/published/README.md` is still a greenfield parent stub at time of authoring. This README documents the `exports/` carrier lane without claiming the parent published-data contract is complete.

[Back to top](#top)

---

## 3. Accepted exports

Use this directory only for release-linked, public-safe export carriers.

| Export type | Suggested placement | Required support |
|---|---|---|
| Released domain export | `<domain>/<release_id>/<export_slug>.<ext>` | Release, schema, evidence, policy, rollback refs. |
| Released tabular package | `<domain>/<release_id>/tables/<package_slug>.*` | Schema, data dictionary, evidence, release refs. |
| Released geospatial package | `<domain>/<release_id>/geo/<package_slug>.*` | CRS/geometry contract, policy decision, release refs. |
| Released report-data attachment | `<domain>/<release_id>/report_data/<attachment_slug>.*` | Report ref, EvidenceBundle refs, release refs. |
| Released cross-domain export | `cross_domain/<scope>/<release_id>/<export_slug>.<ext>` | Owning-lane refs, source-role preservation, release refs. |
| Export index | `indexes/published-export-index.json` | Points to release-approved exports only. |
| Superseded export | `retired/<domain>/<release_id>/<export_slug>.<ext>` | Supersession, correction, withdrawal, or rollback reference. |

Recommended extensions depend on the approved carrier contract and schema. Common candidates include `.csv`, `.json`, `.geojson`, `.parquet`, `.gpkg`, `.zip`, `.md`, and manifest sidecars.

[Back to top](#top)

---

## 4. Exclusions

| Excluded material | Correct home |
|---|---|
| Source payloads and source-system exports | `data/raw/<domain>/` |
| Working or held candidates | `data/work/<domain>/` or `data/quarantine/<domain>/` |
| Processed normalized data | `data/processed/<domain>/` |
| Catalog records | `data/catalog/` |
| Proof objects | `data/proofs/` |
| Receipts | `data/receipts/` |
| API payload snapshots | `data/published/api_payloads/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, signatures | `release/` |
| Policy logic | `policy/` |
| Schemas | `schemas/` |
| Semantic contracts | `contracts/` |
| Direct model output or unreviewed AI summaries | governed AI/review paths before release |
| Sensitive, restricted, or rights-unclear source detail | upstream restricted/held lanes until cleared for public release |

[Back to top](#top)

---

## 5. Publication gates

Before an export is placed here, verify:

- [ ] release authority exists under `release/`;
- [ ] every consequential claim resolves to evidence support;
- [ ] schema and domain validation gates pass or hold with finite reasons;
- [ ] catalog closure exists;
- [ ] policy decisions allow the target audience class and export format;
- [ ] review records exist where required;
- [ ] source role, evidence support, time scope, caveats, rights/license posture, and public-safe posture are preserved;
- [ ] correction and rollback targets are traceable;
- [ ] export digests or integrity refs bind the file to the release record.

If any gate is unresolved, hold the export upstream.

[Back to top](#top)

---

## 6. Export carrier rules

| Rule | Public export posture |
|---|---|
| Export is not raw | Public exports must be released carriers, not source-system dumps. |
| Release authority is separate | Path placement does not create release status; `release/` owns release decisions. |
| Evidence is visible | Exports require resolvable evidence/citation support for consequential claims. |
| Rights travel with the file | License, source rights, audience class, and allowed reuse posture must be clear. |
| Schema/version travels with the file | Export format, schema version, data dictionary, CRS/unit/time conventions, and digest refs should be discoverable. |
| Corrections are expected | Export packages must support correction, supersession, withdrawal, and rollback. |
| Sensitive domains fail closed | Archaeology, living-person, ecology, infrastructure, and other restricted lanes require stricter review before any export. |
| AI is not root truth | AI summaries can consume released exports but cannot replace EvidenceBundles, validation, release, or citations. |

[Back to top](#top)

---

## 7. Suggested layout

```text
data/published/exports/
├── README.md
├── <domain>/
│   └── <release_id>/
│       ├── tables/
│       ├── geo/
│       ├── report_data/
│       ├── manifests/
│       └── retired/
├── cross_domain/
│   └── <scope>/
│       └── <release_id>/
├── indexes/
│   └── published-export-index.json
└── retired/
    └── <domain>/
        └── <release_id>/
```

Suggested deterministic file name:

```text
<domain>.published.export.<export_family>.<scope>.<release_id>.<short_hash>.<ext>
```

Suggested sidecar pattern:

```text
<domain>.published.export.<export_family>.<scope>.<release_id>.<short_hash>.manifest.json
<domain>.published.export.<export_family>.<scope>.<release_id>.<short_hash>.checksums.txt
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, and release tooling.

[Back to top](#top)

---

## 8. Maintenance checklist

Before adding or changing an export under this parent lane, verify:

- [ ] The export is release-approved and public-safe for the intended audience.
- [ ] The release record points to this export.
- [ ] Evidence, catalog, validation, policy, review, correction, and rollback refs are present where required.
- [ ] Source role, evidence support, time scope, caveats, schema/version, rights/license posture, and public-safe posture are preserved.
- [ ] The export does not duplicate upstream, proof, receipt, catalog, schema, contract, policy, or release authority.
- [ ] The export has a digest or integrity reference.
- [ ] Public clients consume it through governed interfaces or approved released artifact paths.
- [ ] Domain-specific export rules are documented in the relevant child lane README before live exports land there.

[Back to top](#top)

---

## 9. Definition of done

This lane is operationally mature when:

- [ ] `data/published/README.md` defines the parent published-data contract.
- [ ] Export contracts and schemas exist under approved homes.
- [ ] Release tooling writes or verifies exports only after release authority is present.
- [ ] Validators block missing evidence, missing release refs, missing rollback, missing schema/version, source-role collapse, missing rights/license posture, missing review state, and unsafe public export fields.
- [ ] Valid and invalid fixtures cover tabular export, geospatial export, report-data attachment, cross-domain export, correction, supersession, and rollback export packages.
- [ ] Governed download/export routes are documented and tested.
- [ ] Active domains have child export README files before live export instances land there.

---

## Maintainer note

Published exports are durable public artifacts that can travel outside the KFM UI. Keep them boring, citable, public-safe, license-aware, schema-aware, digest-bound, audience-aware, and reversible. If evidence, validation, policy, rights, release, correction, or rollback support is incomplete, keep the export upstream instead of placing it here.
