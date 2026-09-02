<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/fauna/occurrence-density-grid/readme
title: data/published/layers/fauna/occurrence_density_grid README
type: directory-readme
version: v0.1
status: draft
owners:
  - TODO(owner): data steward
  - TODO(owner): fauna domain steward
  - TODO(owner): sensitivity reviewer
  - TODO(owner): map-layer steward
  - TODO(owner): release steward
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
path: data/published/layers/fauna/occurrence_density_grid/README.md
related:
  - ../README.md
  - ../../../fauna/README.md
  - ../../../../raw/fauna/README.md
  - ../../../../work/fauna/README.md
  - ../../../../quarantine/fauna/README.md
  - ../../../../processed/fauna/README.md
  - ../../../../catalog/domain/fauna/README.md
  - ../../../../proofs/fauna/README.md
  - ../../../../proofs/validation_report/fauna/README.md
  - ../../../../receipts/README.md
  - ../../../../../release/README.md
  - ../../../../../contracts/README.md
  - ../../../../../schemas/README.md
  - ../../../../../policy/README.md
  - ../../../../../docs/domains/fauna/ARCHITECTURE.md
  - ../../../../../docs/domains/fauna/MAP_UI_CONTRACTS.md
notes:
  - "Directory README for released Fauna occurrence-density-grid layer carriers. It replaces an empty file."
  - "This path is downstream of release decisions and does not itself approve release, define schemas, define policy, prove claims, or permit precise occurrence exposure."
  - "Occurrence-density-grid carriers must preserve generalized aggregation, sensitivity review, taxonomic scope, source roles, time scope, uncertainty, caveats, correction path, rollback support, and integrity references."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/published/layers/fauna/occurrence_density_grid/`

> Published layer sublane for released **Fauna occurrence-density grid map carriers**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Lifecycle: PUBLISHED](https://img.shields.io/badge/lifecycle-PUBLISHED-2ea44f)
![Domain: fauna](https://img.shields.io/badge/domain-fauna-2E8B57)
![Policy: restricted review](https://img.shields.io/badge/policy-restricted--review-b91c1c)
![Layer: occurrence density grid](https://img.shields.io/badge/layer-occurrence--density--grid-blue)
![Publication: release gated](https://img.shields.io/badge/publication-release--gated-blue)
![Authority: not release](https://img.shields.io/badge/authority-not--release-b91c1c)

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `data/published/layers/fauna/occurrence_density_grid/README.md`  
> **Truth posture:** CONFIRMED target path and Fauna published lane from current repo evidence / PROPOSED layer layout and naming / NEEDS VERIFICATION for emitted density-grid files, schemas, validators, release manifests, EvidenceBundle references, sensitivity-review records, transform receipts, and governed map/API routes.

> [!WARNING]
> Fauna is a sensitive domain. This directory is not release authority, raw occurrence storage, precise-location disclosure, source registry authority, catalog authority, proof authority, policy authority, or review authority. An occurrence-density grid belongs here only after release authority, EvidenceBundle support, validation, policy state, sensitivity review, public-safe generalization, correction path, rollback support, and integrity references exist.

---

## 1. Scope

This lane is for released public-safe Fauna occurrence-density grid layer carriers used by governed map, API, report, export, or UI surfaces.

Examples of valid carrier families, once released:

- generalized occurrence-density grid map layers;
- taxon-group or audience-scoped density summaries;
- density-grid sidecars and manifests;
- public indexes that point only to released density-grid layers; and
- retired or superseded density-grid carriers with correction, withdrawal, or rollback references.

This lane should not contain raw occurrence points, precise locations, direct source exports, steward-only details, work candidates, quarantine holds, processed candidates, catalog authority, proof authority, receipt authority, policy logic, schemas, semantic contracts, source registries, release decisions, or unreleased generated outputs.

[Back to top](#top)

---

## 2. Repo fit

| Neighbor | Role |
|---|---|
| `data/published/layers/` | Parent published layer lane. |
| `data/published/layers/fauna/` | Fauna published layer parent scaffold. |
| `data/published/fauna/` | Fauna published domain carrier lane. |
| `data/raw/fauna/` | Source captures; never public-readable. |
| `data/work/fauna/` | Working normalization; never public-readable. |
| `data/quarantine/fauna/` | Held or unsafe material; never public-readable. |
| `data/processed/fauna/` | Validated candidates; upstream of release. |
| `data/catalog/domain/fauna/` | Catalog records; not release authority. |
| `data/proofs/fauna/` | Evidence, validation, proof, and review support. |
| `data/receipts/` | Process memory and transform receipts. |
| `release/` | Release authority. |
| `contracts/` | Semantic meaning. |
| `schemas/` | Machine shape. |
| `policy/` | Admissibility rules. |

[Back to top](#top)

---

## 3. Release checks

Before adding or changing files here, verify:

- [ ] release authority exists;
- [ ] EvidenceBundle references resolve;
- [ ] taxonomic scope, source roles, source family, and time scope are clear;
- [ ] grid resolution, aggregation method, density metric, and uncertainty posture are documented;
- [ ] public-safe transform support exists, including sensitivity review and any required redaction or generalization receipts;
- [ ] thresholds prevent precise occurrence reconstruction or restricted-detail exposure;
- [ ] validation passes or records finite outcomes;
- [ ] policy state allows the declared public audience;
- [ ] caveats, review state, and public/restricted boundary are explicit;
- [ ] correction, withdrawal, supersession, and rollback paths are recorded;
- [ ] integrity references bind the layer to the release record; and
- [ ] public clients use governed interfaces or approved released-artifact paths.

[Back to top](#top)

---

## 4. Suggested layout

```text
data/published/layers/fauna/occurrence_density_grid/
├── README.md
├── layers/
│   └── <release_id>/
├── manifests/
│   └── <release_id>/
├── indexes/
│   └── fauna-occurrence-density-grid-layer-index.json
└── retired/
    └── <release_id>/
```

Suggested deterministic file name:

```text
fauna.published.layer.occurrence_density_grid.<scope>.<release_id>.<short_hash>.<ext>
```

This layout is PROPOSED until validated by contracts, schemas, fixtures, release tooling, and sensitivity-review workflow.

---

## Maintainer note

Fauna occurrence-density grids are public-facing generalized carriers, not root truth, release authority, raw occurrence data, precise-location disclosure, source registry authority, policy authority, or proof authority. Keep them citable, source-role-aware, taxon-aware, time-aware, uncertainty-aware, sensitivity-reviewed, public-safe, release-linked, integrity-bound, correction-ready, and reversible. If release support or public-safe transformation support is incomplete, keep the artifact upstream.
