<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7b9c43d6-8e1c-4e2a-a06e-4b3f8b7f0f5e
title: KFM Indexing Runbook
type: standard
version: v1
status: draft
owners: TBD (Platform Ops / Data Platform)
created: 2026-03-02
updated: 2026-03-02
policy_label: internal
related:
  - docs/runbooks/README.md
  - packages/indexers/ (if present)
  - apps/cli/ (if present)
tags: [kfm, runbook, indexing, operations, rebuildable-projections]
notes:
  - Indexing is a rebuildable projection; canonical truth remains in object storage + catalogs + audit ledger.
  - This runbook is intentionally tool-agnostic until the repo’s concrete commands are verified.
[/KFM_META_BLOCK_V2] -->

# KFM Indexing Runbook
Rebuild and validate **rebuildable projections** (PostGIS/search/graph/tiles) safely, without violating the trust membrane.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Runbook](https://img.shields.io/badge/runbook-indexing-blue)
![Governance](https://img.shields.io/badge/governance-evidence--first-brightgreen)
![Policy](https://img.shields.io/badge/policy-default--deny-critical)
![TODO](https://img.shields.io/badge/TODO-verify%20repo%20commands-lightgrey)

**Where this fits:** `docs/runbooks/indexing/README.md` documents operational procedures for **index builders** (rebuildable projections) that power API/UI query performance and discovery.

---

## Quick navigation
- [Scope](#scope)
- [Core invariants](#core-invariants)
- [What gets indexed](#what-gets-indexed)
- [Inputs and sources of truth](#inputs-and-sources-of-truth)
- [Index types](#index-types)
- [Standard operating procedures](#standard-operating-procedures)
- [Validation checklist](#validation-checklist)
- [Incident playbooks](#incident-playbooks)
- [Rollback](#rollback)
- [Directory contents](#directory-contents)
- [Glossary](#glossary)

---

## Scope

### In scope ✅
- Rebuilding **rebuildable projections**:
  - PostGIS tables + spatial indexes derived from processed geodata
  - Search index derived from processed metadata/text
  - Graph/entity edges derived from catalogs (and optional entity resolution outputs)
  - Tile bundles / tile caches (vector and/or raster)
- Performing **preflight checks**, **cutover**, **validation**, and **rollback**
- Ensuring indexes do **not** create a policy bypass (trust membrane protection)

### Out of scope ❌
- Ingestion (connectors, fetching upstream, RAW acquisition)
- Promotion (RAW → WORK → PROCESSED → CATALOG → PUBLISHED) *except verifying the target is already promoted*
- Editing canonical artifacts (RAW/PROCESSED/catalog triplet/audit ledger)
- Changing schemas, APIs, or policy (that belongs in ADRs + PR review)

> WARNING: **Index builders must never become a shadow API.**
> Clients must not query PostGIS/search/tiles directly. All access stays behind the governed API and policy layer.

[Back to top](#kfm-indexing-runbook)

---

## Core invariants

1. **Canonical truth is immutable-ish; indexes are rebuildable.**
   - If an index is corrupted, we rebuild it from canonical artifacts.
2. **Idempotent rebuilds.**
   - A rebuild with the same inputs should produce the same outputs (or differences must be explainable and receipted).
3. **Policy-safe by construction.**
   - Index content must not leak restricted fields/geometry/time ranges. Indexers should support redaction/generalization obligations.
4. **Auditable operations.**
   - Every rebuild emits a run receipt / audit entry (who/what/when/why, inputs, digests, tool versions).

---

## What gets indexed

Indexing exists to make KFM fast and usable while keeping governance intact:

- **Discovery:** dataset search, facets, time filtering
- **Spatial query:** bounding-box intersects, point-in-polygon, region stats (as supported)
- **Map rendering:** vector tiles / raster tiles / cached bundles
- **Relationship navigation:** graph edges (dataset ↔ place/event/entity), story linking, evidence graph (if implemented)

---

## Inputs and sources of truth

### Canonical inputs (should already exist before indexing)
- PROCESSED artifacts (standardized formats, stable IDs, checksums)
- CATALOG “triplet” (DCAT + STAC + PROV) + run receipts
- PUBLISHED release manifest / promoted dataset versions list

### Operational inputs (provided by operator)
- **Scope:** full rebuild vs incremental vs per-dataset-version
- **Target environment:** dev/stage/prod (and the cutover method)
- **Change context:** linked incident ticket / PR / release id

> TIP: If you can’t point to a promoted dataset version (with catalogs + receipts), do not index it. Indexing does not “fix” missing promotion artifacts.

---

## Index types

| Index type | Projection | Typical source inputs | Primary consumers | Risk if wrong |
|---|---|---|---|---|
| PostGIS | Derived tables + spatial indexes | PROCESSED GeoParquet/derived layers | Governed API spatial queries | Incorrect geometry/time, policy bypass via direct DB access |
| Search | Full-text + metadata facets | Catalog triplet + processed text/metadata | Dataset discovery UI + API | Leaks restricted fields, stale facets |
| Graph | Edges, entity links | Catalog triplet + entity resolution outputs | Story/Focus navigation | Wrong relationships; “phantom” evidence trails |
| Tiles | PMTiles/vector tile bundles, raster caches | Processed geometries/rasters + styling rules | Map UI tile endpoints | Wrong symbology, stale tiles, expensive rebuild loops |

> NOTE: The concrete technologies behind these indexes (OpenSearch vs Postgres FTS, tile toolchain, etc.) are **implementation details** and must be verified in the live repo before adding exact commands to this runbook.

---

## Architecture sketch

```mermaid
flowchart LR
  U[Upstream sources] --> R[RAW immutable artifacts]
  R --> W[WORK quarantine normalize QA]
  W --> P[PROCESSED publishable artifacts]
  P --> C[CATALOG triplet DCAT STAC PROV]
  C --> I[Index builders rebuildable projections]
  I --> A[Governed API policy enforcement]
  A --> UI[UI surfaces Map Story Focus]
```

---

## Standard operating procedures

### SOP-0: Preflight (always)
**Goal:** confirm we are rebuilding projections *from promoted truth* and not creating a bypass.

**Checklist**
- [ ] Identify the **target release** or **dataset_version_id** set
- [ ] Confirm each target is **PUBLISHED/promoted** (catalog triplet validates; receipts exist)
- [ ] Confirm you have access to rebuildable stores (DB/search/tiles) **without granting client access**
- [ ] Choose rebuild strategy (full / incremental / per-dataset)
- [ ] Confirm you have a rollback plan (snapshot, alias swap, or previous index pointer)
- [ ] Record incident/release context for the run receipt

---

### SOP-1: Incremental rebuild (preferred)
Use for: routine updates after promotion, small backfills, predictable changes.

**Pattern**
1. Build new projections for *only* changed dataset versions
2. Validate
3. Cut over atomically

**Pseudo-commands (MUST be replaced with verified repo commands)**
```bash
# 1) Discover available indexer entrypoints (example patterns)
# - apps/cli
# - packages/indexers
# - scripts/
# Replace <pm> with the repo standard package manager once verified.

<pm> -w run index:build -- --scope=changed --since-release=<release_id>
<pm> -w run index:validate -- --scope=changed --since-release=<release_id>
<pm> -w run index:cutover -- --strategy=atomic
```

---

### SOP-2: Full rebuild (break-glass)
Use for: corrupted indexes, major schema changes, search engine migration, tile cache wipe.

**Pattern**
1. Freeze/coordinate writers (as needed)
2. Snapshot current projections (optional but recommended for fast rollback)
3. Rebuild everything from canonical inputs
4. Validate aggressively
5. Cut over atomically (aliases/pointers)
6. Monitor and close

**Pseudo-commands**
```bash
# Optional snapshot (implementation-specific)
<pm> -w run index:snapshot -- --label=pre-full-rebuild-<date>

# Full rebuild
<pm> -w run index:build -- --scope=all
<pm> -w run index:validate -- --scope=all
<pm> -w run index:cutover -- --strategy=atomic
```

> WARNING: Avoid “in-place rebuilds” in production if they cause mixed-version results. Prefer **build-new → validate → swap**.

---

### SOP-3: Per-dataset rebuild (surgical)
Use for: one dataset’s tiles/search facet incorrect; targeted backfill.

**Pattern**
1. Confirm dataset_version_id and its catalogs/receipts
2. Rebuild only its projections
3. Validate only its endpoints
4. Cutover if your system supports per-dataset partitioning; otherwise schedule a broader swap

**Pseudo-commands**
```bash
<pm> -w run index:build -- --dataset-version=<dataset_version_id>
<pm> -w run index:validate -- --dataset-version=<dataset_version_id>
```

[Back to top](#kfm-indexing-runbook)

---

## Validation checklist

### Minimum functional validation (operator)
- [ ] **Discovery:** dataset appears in search results with correct version + digests
- [ ] **Policy:** restricted datasets do not leak via search facets or tiles
- [ ] **Spatial:** representative bbox/point queries return expected counts/features
- [ ] **Tiles:** map renders at low/medium/high zoom for representative layers
- [ ] **Time:** time slider / temporal filtering matches dataset temporal extent

### Minimum technical validation (system/CI where possible)
- [ ] Index build logs show deterministic inputs (release id, dataset_version_ids, content digests)
- [ ] Validators pass (catalog linkcheck, schema checks, tile integrity checks)
- [ ] Run receipt emitted and stored in the audit ledger (or the configured audit sink)

---

## Incident playbooks

### Symptom → likely cause → first checks → safe fix

| Symptom | Likely cause | First checks | Safe fix |
|---|---|---|---|
| Search returns stale results | Index not rebuilt after promotion | Compare promoted versions vs indexed versions | Incremental rebuild since last release |
| Tiles show old geometry | Tile bundle not invalidated | Tile bundle timestamp/manifest | Per-dataset tile rebuild, then atomic swap |
| Spatial queries slow | Missing DB indexes | DB index existence & query plans (ops-only) | Rebuild PostGIS indexes; ensure no client DB access |
| Restricted layer visible | Policy not applied to index outputs | Inspect indexer redaction step; check policy version | Immediate rollback + rebuild with corrected policy integration |

> NOTE: Never “hot patch” by exposing underlying DB/search directly to UI. That’s a trust membrane violation.

---

## Rollback

Preferred rollback mechanisms (choose what your index tech supports):

1. **Alias/pointer rollback (best):**
   - Switch API/search alias back to previous index generation.
2. **Snapshot restore (fast, if available):**
   - Restore projection snapshot taken pre-rebuild.
3. **Rebuild from canonical (slowest, always possible):**
   - If no snapshot exists, rebuild again from canonical inputs.

Rollback checklist:
- [ ] Restore the prior pointer/snapshot
- [ ] Confirm policy-safe behavior (restricted stays restricted)
- [ ] Emit rollback receipt referencing the failed build receipt

---

## Directory contents

This directory contains **runbooks** only (operator-facing, step-by-step, safe-by-default).

Suggested layout (create as needed; do not assume files exist):
```text
docs/runbooks/indexing/
  README.md                # This runbook (overview + SOPs)
  postgis.md               # PostGIS projection operations (TBD)
  search.md                # Search index operations (TBD)
  tiles.md                 # Tile build/cutover operations (TBD)
  graph.md                 # Graph rebuild operations (TBD)
  incident-response.md     # Deeper symptom→cause→fix matrix (TBD)
```

---

## Glossary

- **Canonical stores:** the source-of-truth artifacts (object storage zones, catalogs, audit ledger).
- **Rebuildable projections:** derived stores you can delete and regenerate (PostGIS/search/graph/tiles).
- **Catalog triplet:** DCAT + STAC + PROV; interoperable metadata + lineage surface.
- **PUBLISHED:** governed runtime surface served through the policy enforcement point (API), not direct storage access.
- **Trust membrane:** architectural/policy boundary that prevents bypassing governance.

[Back to top](#kfm-indexing-runbook)
