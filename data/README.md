# `data/` — Governed Data (Kansas Frontier Matrix)

**Path:** `data/README.md`  
**Status “badges”:** ✅ Governed • 🧬 Provenance-required • 🧪 CI-validated • 🛡️ Policy-as-code • 🧭 FAIR+CARE

KFM treats **datasets, metadata, and provenance as first-class, governed artifacts**. This folder is where we keep the *auditable truth* of what the platform can show and serve.

> [!IMPORTANT]
> **Nothing becomes “live”** (API/UI-visible) unless it passes governance checks *and* ships with complete metadata + lineage.  
> If a dataset doesn’t have the required contract artifacts, **CI should fail** and block merge.

---

## What lives in `data/`

This directory holds the **canonical dataset lifecycle**:

- 📥 **Raw** inputs: immutable snapshots exactly as acquired
- 🧪 **Work** outputs: transient scratch/intermediate files (reproducible, not user-facing)
- ✅ **Processed** outputs: standardized, analysis-ready **source of truth**
- 🧾 **Catalog metadata**: STAC + DCAT records for discovery/interoperability
- 🧬 **Provenance**: PROV lineage (what produced what, from which sources, when, under which rules)

---

## Canonical “truth path” (end-to-end)

```mermaid
flowchart LR
  raw[data/raw<br/>(immutable snapshots)]
  etl[ETL pipelines<br/>(code + rules)]
  work[data/work<br/>(scratch / intermediate)]
  processed[data/processed<br/>(canonical outputs)]
  stac[data/stac<br/>(STAC Items/Collections)]
  dcat[data/catalog/dcat<br/>(DCAT JSON-LD)]
  prov[data/provenance<br/>(PROV lineage logs)]
  stores[(Runtime stores<br/>PostGIS / Neo4j / search index)]
  api[Governed API gateway]
  ui[UI + external clients]

  raw --> etl --> work --> processed
  processed --> stac
  processed --> dcat
  processed --> prov
  processed --> stores --> api --> ui
```

**Trust membrane rule:** the UI and external clients do **not** read raw files or databases directly—access is mediated through the governed API.

---

## Directory layout

> [!NOTE]
> The exact dataset subfolder structure can vary by domain, but the *stage boundaries* below should remain stable.

```text
data/
  raw/                     # Immutable source snapshots (never edited in place)
    <domain>/
      <dataset_slug>/
        <source_files...>
        manifest.(yml|json)   # Source manifest (required)

  work/                    # Transient/intermediate artifacts (scratch space)
    <domain>/
      <dataset_slug>/
        <intermediate_outputs...>

  processed/               # Canonical, standardized outputs (source of truth)
    <domain>/
      <dataset_slug>/
        <final_outputs...>

  stac/                    # STAC Items and Collections describing processed assets
    <...>.json

  catalog/
    dcat/                  # DCAT JSON-LD dataset records
      <...>.jsonld

  provenance/              # PROV lineage logs (what -> how -> derived outputs)
    <...>.prov.json
```

---

## Dataset contract

Every dataset introduced to KFM must include the following **minimum contract**.

| Artifact | Where | Required | Why |
|---|---|:---:|---|
| Raw source file(s) | `data/raw/...` | ✅ | Immutable audit reference of what was ingested |
| Source manifest (machine-readable) | beside raw | ✅ | Captures source, acquisition time, checksum, license, etc. |
| Processed canonical output(s) | `data/processed/...` | ✅ | Standardized outputs used internally and for publication |
| STAC Item/Collection | `data/stac/...` | ✅ | Findable + interoperable geospatial asset metadata |
| DCAT record (JSON-LD) | `data/catalog/dcat/...` | ✅ | Catalog interoperability (harvestable metadata) |
| PROV lineage | `data/provenance/...` | ✅ | Reproducibility + traceability (inputs → transforms → outputs) |

> [!TIP]
> Treat this like a compile target: if any required artifact is missing, the “build” should fail.

---

## Raw stage rules (`data/raw/`) 📥

**Raw inputs are immutable snapshots.** Do not “clean up” raw files in place.

**Alongside each raw dataset**: include a **manifest** (JSON or YAML) that records, at minimum:

- Source/origin reference (URL or authoritative citation)
- Acquisition date/time
- File checksums (e.g., SHA-256) for integrity
- License/terms
- Format/schema hints
- Who/what ingested it and (if applicable) which project/permission context
- Sensitivity flags (if any)

<details>
<summary><strong>Example: minimal manifest template (YAML)</strong></summary>

```yaml
dataset_slug: rainfall_1930
domain: climate
title: "Rainfall observations (1930) — Kansas"
description: >
  Canonicalized rainfall observations for Kansas in 1930.
source:
  name: "Authoritative provider name"
  url_or_citation: "<source URL or citation text>"
  acquired_at: "YYYY-MM-DDTHH:MM:SSZ"
files:
  - path: "rainfall_1930.csv"
    sha256: "<sha256>"
    media_type: "text/csv"
license:
  spdx: "CC-BY-4.0"
provenance:
  ingested_by: "<person|team|service>"
  ingestion_method: "<script|pipeline|manual>"
sensitivity:
  classification: "public"   # public|internal|restricted (adjust to policy)
  flags: []                  # e.g., ["indigenous", "sacred_site", "pii_risk"]
```

</details>

---

## Work stage (`data/work/`) 🧪

`data/work/` is **scratch space** for intermediate transforms:

- temporary reprojections
- merges
- normalization steps
- QA artifacts used during transformation

Work files:
- should be **reproducible** from `data/raw/` + pipeline code
- are **not** user-facing
- may be excluded from version control if large/transient (follow repo policy)

---

## Processed stage (`data/processed/`) ✅

Processed outputs are the **canonical source of truth**:

- standardized format(s)
- consistent schema(s)
- consistent coordinate reference system (e.g., WGS84 or a Kansas state plane choice—follow repo conventions)
- ready for loading into runtime stores (e.g., PostGIS/Neo4j/search indexes) as **derivative caches**

**Reproducibility principle:** re-running the same transformation code on the same raw inputs should produce the same processed outputs.

<details>
<summary><strong>Typical processed targets (examples)</strong></summary>

- Rasters: Cloud-Optimized GeoTIFF (COG) w/ tiling pyramids (for web maps)
- Tables: Parquet (normalized, typed)
- Vectors: GeoJSON / GeoParquet (with valid geometries)

</details>

---

## Validation gates (CI “fail closed”) 🧪🛑

KFM uses validation gates at transitions:

1. **After raw ingestion**  
   - manifest completeness + schema validation  
   - checksums/integrity  
   - minimum license + source attribution

2. **After processing**  
   - schema validation on outputs  
   - quality rules (e.g., no null geometries, plausible ranges)

3. **Before catalog publication**  
   - policy checks (e.g., Open Policy Agent / similar) for:
     - disallowed sensitive content
     - prohibited personal identifiers (if policy forbids)
     - license compatibility, etc.

If validation fails, the dataset **must not progress** and PR merge should be blocked.

> [!WARNING]
> CI may also enforce documentation rules (e.g., link checks, image checks, provenance/sensitivity scans).  
> Avoid hot-linking external images inside governed docs unless explicitly permitted by repo policy.

---

## FAIR + CARE governance ⚖️🧭

KFM’s design explicitly aligns data stewardship to:

- **FAIR** (Findable, Accessible, Interoperable, Reusable)
- **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics)

### Sensitivity handling (do not “guess”)
If a dataset intersects with Indigenous knowledge, sacred/vulnerable sites, or living-person information:

- mark the manifest with sensitivity flags
- expect **extra human review**
- expect policies to restrict publication and/or precision (e.g., AI responses should not disclose precise locations)

> [!IMPORTANT]
> When in doubt: **generalize/redact** and route for governance review.

---

## Adding or updating a dataset (workflow) 🧩

### Checklist (Definition of Done)
- [ ] Raw snapshot stored under `data/raw/...` (no edits-in-place)
- [ ] Manifest present and validated (source + acquisition + checksum + license)
- [ ] Transformation produces canonical outputs in `data/processed/...`
- [ ] STAC metadata produced under `data/stac/...`
- [ ] DCAT JSON-LD record produced under `data/catalog/dcat/...`
- [ ] PROV lineage log produced under `data/provenance/...`
- [ ] Sensitivity flags set appropriately (and governance review requested if needed)
- [ ] CI passes: data validation + policy checks + docs checks

### Suggested PR hygiene
- Keep data additions small and reviewable
- Prefer reproducible ingestion scripts over manual steps
- Document assumptions and tradeoffs in PR description

---

## FAQ

### Why can’t the UI consume `data/raw/` directly?
Because `data/raw/` is not standardized and may contain content that hasn’t passed governance checks. KFM’s “truth path” requires processing + metadata + provenance before anything is served.

### Are runtime databases the “source of truth”?
No. Runtime stores are derivative caches built from `data/processed/`. The canonical truth is versioned processed files + metadata + provenance.

### Where do policies live?
In a policy-as-code system (repo-defined). If you’re adding a new data class or sensitivity category, you may also need to update policy rules (and tests).

---

## Version history 🕰️

| Version | Date (YYYY-MM-DD) | Summary | Author |
|---:|---:|---|---|
| v1.0.0 | 2026-02-10 | Initial governed `data/` README drafted from KFM project guides | KFM AI assistant |