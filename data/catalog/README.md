---
title: "🗃️ Data Catalog (DCAT)"
description: "Machine-readable dataset discovery records (DCAT JSON-LD) for Kansas Frontier Matrix (KFM)."
status: "active"
version: "v13"
last_updated: "2026-01-02"
tags:
  - data
  - catalog
  - dcat
  - stac
  - prov
  - metadata
---

# 🗃️ Data Catalog (DCAT)

![DCAT](https://img.shields.io/badge/catalog-DCAT%20JSON--LD-blue)
![Linked](https://img.shields.io/badge/links-STAC%20%2B%20PROV-brightgreen)
![Governed](https://img.shields.io/badge/governance-CI%20gated-important)

> **Purpose:** This folder is the project’s **dataset discovery layer**.  
> It contains **DCAT Dataset entries (JSON-LD)** that make KFM datasets searchable, citable, and linkable to their **STAC** (geospatial indexing) and **PROV** (lineage) records.

---

## 🔎 What lives here?

- **`dcat/`** → DCAT dataset records (**JSON-LD**) used for catalog/discovery.
- **`README.md`** → this guide (how to structure and maintain the DCAT layer).

> ✅ **Rule of thumb:**  
> **Data files** live in `data/**/processed/…` (or equivalent stable storage).  
> **Discovery metadata** lives here.

---

## 📍 How this fits into KFM (big picture)

```mermaid
flowchart LR
  A[Raw Sources] --> B[ETL + Normalization]
  B --> C[STAC Items + Collections]
  C --> D[DCAT Dataset Views]
  C --> E[PROV Lineage Bundles]
  C --> G[Neo4j Graph (references)]
  G --> H[API Layer (contracts + redaction)]
  H --> I[Map UI / Focus Mode]
```

**DCAT is the “front door” to the dataset list.**  
It should point to:
- the **STAC** record(s) for spatial/temporal detail, and/or
- stable **download / access** distributions (files, services, APIs),
- the **PROV** lineage bundle for reproducibility.

---

## 📁 Directory layout

```text
data/
  stac/
    collections/              # STAC Collections
    items/                    # STAC Items
  catalog/
    README.md                 # 👈 you are here
    dcat/                     # DCAT outputs (JSON-LD)
      <dataset-id>.jsonld
      <dataset-id>__v2.jsonld
  prov/                       # PROV bundles (per run / per dataset)
```

---

## 🧩 The “boundary artifacts” contract (non-negotiables)

A dataset is considered “published” when it has **boundary artifacts** that downstream layers can consume:

- ✅ **STAC**: Collections + Items (spatial/temporal + asset pointers)
- ✅ **DCAT**: Dataset discovery record (this folder)
- ✅ **PROV**: End-to-end lineage (raw → work → processed, with run/config identity)

> 🧠 KFM treats *derived outputs* (including AI/analysis artifacts) as first-class datasets:  
> they still need STAC/DCAT/PROV, and must be governed like any other dataset.

---

## 🧱 Minimal DCAT Dataset entry

At minimum, each DCAT record should include:

- **Title**
- **Description**
- **License**
- **Keywords / tags**
- **Distribution links** (STAC and/or direct downloads / services)
- **Version links** (when applicable)

### ✅ Minimal JSON-LD skeleton (example)

```json
{
  "@context": {
    "@vocab": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "kfm:dataset/hydrology/river-flow/v2",
  "@type": "Dataset",
  "dct:title": "River Flow Measurements (v2)",
  "dct:description": "Processed river flow measurements for Kansas basins; includes QA flags and harmonized units.",
  "dct:license": "https://spdx.org/licenses/CC-BY-4.0.html",
  "keyword": ["hydrology", "kansas", "timeseries", "derived"],
  "distribution": [
    {
      "@type": "Distribution",
      "dct:title": "STAC Collection",
      "accessURL": "../stac/collections/river-flow.json",
      "mediaType": "application/json"
    },
    {
      "@type": "Distribution",
      "dct:title": "Processed dataset (Parquet)",
      "downloadURL": "../hydrology/processed/river_flow__v2.parquet",
      "mediaType": "application/parquet"
    }
  ],
  "prov:wasRevisionOf": "kfm:dataset/hydrology/river-flow/v1",
  "prov:wasGeneratedBy": "../prov/run_2026-01-02__abc123.jsonld"
}
```

> 🧷 **Notes**
> - The exact required/optional fields are defined by the **KFM DCAT Profile** (see links below).
> - If the dataset is sensitive or restricted, distributions should reference an **API accessURL** (with enforced redaction) instead of a public download.

---

## 🏷️ Naming & IDs

Keep dataset IDs consistent and stable:

- **File name:** `dcat/<dataset-id>.jsonld`
- **Preferred slug style:** `lower-kebab-case` or `lower_snake_case` — pick one and stay consistent per domain
- **Version suffix:** `__v2`, `__v2026-01-02`, etc. (whatever the profile + domain conventions specify)

### ✅ Recommended dataset-id pattern

`<domain>/<dataset-name>/<version>`

Examples:
- `historical/treaty-boundaries/v1`
- `air-quality/pm25-annual-mean/v2025`
- `hydrology/river-flow/v2`

---

## 🔗 Linking rules (DCAT ↔ STAC ↔ PROV ↔ Graph)

### DCAT → STAC / Distribution
DCAT should include **distribution links** that reference:
- STAC record(s) (**Collections/Items**) and/or
- direct stable resource endpoints (**download URLs**, WMS/WMTS tiles, API endpoints)

### PROV end-to-end
PROV must capture:
- raw inputs → intermediate work → processed outputs
- run identity (run id / commit hash / parameters)

### Graph references catalogs (don’t duplicate blobs)
Graph nodes should hold **references** (STAC Item IDs, DCAT IDs, DOIs), not big payloads.

---

## 🧾 Versioning rules

KFM is versioned at **two levels**:

### 1) Dataset versioning (this folder)
When a dataset is updated or reprocessed:
- publish a **new DCAT entry**
- link it to the predecessor (e.g., `prov:wasRevisionOf`)
- keep older versions discoverable (unless governed otherwise)

### 2) System-level versioning (repo + contracts)
If a change impacts:
- graph ontology,
- API contracts,
- UI assumptions,
…then it must follow governed migration + release versioning practices.

---

## ✅ Validation & CI expectations

This repo is **CI-gated**. Expect checks like:

- 📌 Markdown/front-matter validation (where applicable)
- 🔗 Link/reference validation
- 🧪 JSON Schema validation for **STAC / DCAT / PROV**
- 🧠 Provenance completeness checks (e.g., missing PROV fails)
- 🔐 Security scans (secrets/sensitive leaks)

> If you add or modify DCAT records manually, run the project validators (see `tools/` and `schemas/`) and ensure CI stays green.

---

## 🛠️ Adding a new dataset checklist

Use this when publishing anything new (including “evidence artifacts” like model outputs or AI-derived layers):

- [ ] Data staged through **raw → work → processed** (domain-isolated)
- [ ] **STAC** Collection + Item(s) created in `data/stac/…`
- [ ] **DCAT** Dataset record created in `data/catalog/dcat/…`
- [ ] **PROV** bundle created in `data/prov/…`
- [ ] Distributions link to **STAC and/or stable access endpoints**
- [ ] License + attribution included (and matches source constraints)
- [ ] Sensitivity classification respected (no restricted coordinates/leaks)
- [ ] Domain runbook updated (see `docs/data/<domain>/…`)

---

## 🧭 Governance & sensitivity

🚫 **Do not** publish:
- secrets (keys, tokens),
- sensitive site coordinates,
- restricted datasets without proper access controls.

✅ **Do**:
- route sensitive access through the API layer (redaction + classification enforcement),
- mark derived/AI artifacts clearly and attach uncertainty/confidence metadata (as defined by the KFM profiles).

---

## 🔗 Useful links (in-repo)

- 📘 KFM Master Guide: `../../docs/MASTER_GUIDE_v13.md`
- 📐 DCAT Profile: `../../docs/standards/KFM_DCAT_PROFILE.md`
- 🛰️ STAC Profile: `../../docs/standards/KFM_STAC_PROFILE.md`
- 🧬 PROV Profile: `../../docs/standards/KFM_PROV_PROFILE.md`
- 🧪 Schemas (DCAT): `../../schemas/dcat/`
- 🧰 Tooling / validators: `../../tools/`

---

## ❓FAQ

### “Where do the actual data files go?”
Not here. DCAT is **metadata**.  
Put data assets under the domain’s **processed** area (or stable storage), and reference them via **STAC assets** + DCAT distributions.

### “Can I ship a non-spatial dataset?”
Yes. Many non-spatial datasets still get a STAC Collection for consistency. DCAT remains the discovery layer.

### “What about AI-generated or model-derived outputs?”
Treat them like any other dataset:
- store them in `processed/…`
- catalog them in STAC/DCAT
- capture the run in PROV (inputs, method, params, confidence)

---