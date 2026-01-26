# 📄 MCP Datasheets — `mcp/datasheets/`  
> **Human-friendly dataset documentation** (with the same “evidence-first” mindset as the rest of KFM) 🧭

![Provenance-first](https://img.shields.io/badge/provenance-first-2ea44f)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governance-blue)
![STAC%20%2B%20DCAT%20%2B%20PROV](https://img.shields.io/badge/STAC%20%2B%20DCAT%20%2B%20PROV-catalog%20triplet-purple)
![MCP](https://img.shields.io/badge/MCP-documentation--first-orange)

Welcome to **Datasheets** ✅  
This folder contains **datasheets for datasets** used by the Kansas Frontier Matrix (KFM): concise, standardized Markdown docs describing *what the dataset is*, *how it was built*, *what’s inside*, *how to use it safely*, and *what to watch out for*.

Datasheets complement (but **do not replace**) KFM’s machine-readable metadata (STAC/DCAT/PROV). They’re the “reader’s guide” that makes the catalog legible to humans — historians, GIS folks, devs, and AI reviewers alike. 🧠🗺️

---

## 🧭 Why datasheets exist (the “so what?”)

Datasheets help us:
- ✅ **Onboard fast**: understand a dataset without spelunking ETL code.
- ✅ **Stay reproducible**: capture assumptions, transformations, versions, and pitfalls.
- ✅ **Enforce governance**: license clarity, sensitive-data handling, FAIR/CARE notes.
- ✅ **Support UI + Focus Mode**: give the product and AI assistant accurate dataset context (without inventing facts).
- ✅ **Prevent “mystery data”**: every dataset should have an identity, story, and limits.

---

## 🧱 How datasheets fit the KFM evidence chain

KFM generally treats dataset publication as a set of **boundary artifacts** that downstream systems can trust:

- **STAC** → spatial/temporal footprint + assets + discovery  
- **DCAT** → catalog/portal discovery + distribution links  
- **PROV** → lineage: sources → processes → outputs  
- **Datasheet (this folder)** → human narrative: purpose, schema, quality, ethics, usage

If STAC/DCAT/PROV is the “machine citation,” the datasheet is the “human explanation.” 🧾✨

---

## 📦 Directory layout (recommended)

> We keep this folder organized so contributors can find things quickly.

```text
mcp/
└─ datasheets/
   ├─ README.md                 👈 you are here
   ├─ _templates/               🧩 copy/paste templates
   │  ├─ dataset-datasheet.md
   │  └─ external-dataset-note.md
   ├─ domains/                  🗂️ grouped by theme/domain
   │  ├─ environment/
   │  ├─ history/
   │  ├─ infrastructure/
   │  └─ demographics/
   └─ _index.yml                🧭 optional: index of dataset_id → path
```

> If your repo structure differs, keep the *spirit*: predictable naming + easy navigation.

---

## 🏷️ Naming rules (important)

**One datasheet per dataset_id.**

Recommended filename:
- `mcp/datasheets/domains/<domain>/<dataset_id>.md`

Where:
- `dataset_id` is a **stable slug** (also used by API/catalog IDs)
- `domain` matches KFM’s dataset grouping (Environment / Historical / etc.)

Examples:
- `domains/environment/ks_drought_index_1895_2020.md`
- `domains/history/ks_land_treaties_1803_1905.md`

---

## 🔗 Required cross-links (keep humans + machines aligned)

Every datasheet should link to (or reference IDs for):
- 🧊 **STAC** item/collection location
- 🗃️ **DCAT** dataset record location
- 🧬 **PROV** lineage bundle location
- 📁 Produced assets (e.g., GeoJSON / COG / PMTiles / GeoParquet)
- 🧪 ETL pipeline entry point (script/notebook/config) and run instructions

> The goal: if someone reads the datasheet, they can *recreate the dataset* or *audit its lineage*.

---

## 🧠 Safety & governance rules (don’t skip)

### 🛡️ Sensitive data
If a dataset includes sensitive locations, personal data, or culturally sensitive info:
- **Do not** publish precise coordinates or personal identifiers in the datasheet.
- Describe redaction/generalization at a high level.
- Add a clear **access policy note** (who can see what, and why).
- Prefer *policy references* over *sensitive content*.

### ⚖️ FAIR + CARE callouts
Include short sections for:
- **FAIR**: discovery, access, formats, interoperability, reuse constraints
- **CARE**: community benefit, authority to control, responsibility, ethics

> Treat these as first-class metadata, not footnotes.

---

## ✍️ Datasheet template (copy/paste)

> Use this template for any dataset compiled or curated by KFM.

<details>
<summary><strong>📄 Click to expand: Dataset Datasheet Template</strong></summary>

```markdown
---
dataset_id: ks_example_dataset_YYYY
title: "Kansas Example Dataset (YYYY)"
domain: environment | history | infrastructure | demographics | ...
version: "v1.0.0"
status: draft | review | published | deprecated
license: "SPDX-ID or text"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
owners:
  - name: "Team/Person"
    role: "Maintainer"
contact: "email-or-issue-link"
stac:
  collection: "path/or/id"
  items: "path/or/pattern"
dcat:
  record: "path/or/id"
prov:
  bundle: "path/or/id"
assets:
  - type: "GeoJSON | COG | PMTiles | GeoParquet | CSV | ..."
    path: "data/processed/..."
---

# 1) Overview 🧭
## What is this?
A 2–4 sentence description of the dataset.

## Why does it exist?
Problem/use-case it supports (UI layer, story nodes, analysis, etc.).

## What questions should it answer?
- Q1
- Q2
- Q3

# 2) Scope 🗺️⏳
## Spatial coverage
- CRS:
- Bounding region:
- Resolution/scale:

## Temporal coverage
- Start:
- End:
- Granularity (daily/monthly/yearly/event-based):

# 3) Lineage & Methods 🧬
## Sources (raw inputs)
- Source A (what, where, retrieval method)
- Source B ...

## Processing summary (ETL)
- Step 1: …
- Step 2: …
- Step 3: …
> Link to pipeline scripts/configs; note deterministic expectations.

## Versioning policy
- How updates happen
- How old versions are preserved

# 4) Data dictionary 📚
> List every field users will see.

| Field | Type | Units | Nullable | Description | Notes |
|------|------|-------|----------|-------------|------|
| id   | str  | —     | no       | Stable record id | |
| ...  |      |       |          |             | |

# 5) Quality & validation ✅
## Validation checks performed
- Schema checks:
- Geometry checks:
- Range checks:
- Deduplication rules:

## Known issues / limitations ⚠️
- Limitation 1
- Limitation 2

# 6) Ethics, privacy, and CARE 🧑🏽‍🤝‍🧑🏾
## Sensitive data handling
- Redaction/generalization approach:
- Access policy notes:

## CARE notes
- Collective benefit:
- Authority to control:
- Responsibility:
- Ethics:

# 7) Access & usage 🔌
## How to access
- API endpoints / GraphQL queries:
- Download links:
- UI layers/story nodes that use this dataset:

## Recommended uses
- Use case A
- Use case B

## Non-recommended uses 🚫
- Misuse A
- Misuse B

# 8) Changelog 🧾
- v1.0.0 — Initial published version
```

</details>

---

## 🧾 External dataset note (when you *didn’t* compile it)

If KFM uses a third-party dataset “as-is”, add a short note instead of pretending we produced it.

<details>
<summary><strong>🌐 Click to expand: External Dataset Note Template</strong></summary>

```markdown
---
dataset_id: external_example_dataset
title: "External Dataset Name"
status: published
license: "As stated by publisher"
source_url: "..."
stac/dcat/prov: "links/ids if mirrored into KFM catalog"
---

# External Dataset Note 🌐
## What it is
Short summary of what the publisher provides.

## What KFM changed (if anything)
- None (mirrored as-is)
- Or: reprojected / normalized schema / clipped to Kansas, etc.

## Caveats
- Known publisher limitations
- Any KFM-specific handling (rate limits, caching, etc.)
```
</details>

---

## 🧑‍💻 Contribution workflow (PR checklist)

When adding or updating a datasheet, your PR should include:

- [ ] Datasheet added/updated under `mcp/datasheets/...`
- [ ] Dataset **version** bumped (if content changed materially)
- [ ] Links/IDs for **STAC/DCAT/PROV** are present and correct
- [ ] Data dictionary updated to match actual output schema
- [ ] Quality checks + known limitations documented
- [ ] License clearly stated
- [ ] FAIR + CARE notes included (especially for people/community/cultural content)
- [ ] Sensitive content not leaked (no precise protected coordinates, no personal info)
- [ ] If dataset behavior changed: changelog updated

---

## 🧩 How this connects to the rest of KFM

- **UI** expects governed, provenance-linked data (datasheets help humans understand what the UI is showing).  
- **Story Nodes** pair Markdown narrative with JSON “map/timeline state”; they should reference dataset_ids and reuse datasheet language for accuracy.  
- **Focus Mode AI** should rely on dataset metadata + provenance; datasheets provide the “human semantics” that prevent misinterpretation.

---

## 📚 Project reference library (optional but handy)

These PDFs were added to the project as a shared research bookshelf. Some are **PDF portfolios** that may require Adobe Reader/Acrobat to browse their embedded documents.

- `AI Concepts & more.pdf` 🤖  
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` 🗃️  
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` 🌍  
- `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf` 🧰  
- `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf` 🧪  
- `Various programming langurages & resources 1.pdf` 🧑‍💻  

---

## 🧭 Quick FAQ

**Q: Do we need a datasheet for every dataset?**  
A: If KFM compiles/curates it, yes. If it’s external “as-is,” prefer a short external note.

**Q: Where should I describe ETL details — datasheet or code?**  
A: Both. The datasheet should summarize *what* and *why*, and link to the pipeline for *how*.

**Q: Can I add new facts to a datasheet?**  
A: Only if those facts are supported by the dataset’s sources/metadata. If it’s a claim, it should trace back to provenance artifacts.

---

## ✅ TL;DR
Datasheets are the **human layer** of KFM’s provenance chain. Keep them **accurate**, **auditable**, and **useful** — and always tie them back to STAC/DCAT/PROV + pipeline reality. 🧠🔗🗺️