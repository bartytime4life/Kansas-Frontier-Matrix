# 📌 Citations & Provenance — `<site-slug>`

![Evidence-first](https://img.shields.io/badge/evidence--first-✅-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-blue)
![FAIR%20%2B%20CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-governed-purple)
![Sensitive%20locations](https://img.shields.io/badge/sensitive%20locations-protected-orange)
![3D](https://img.shields.io/badge/3D-glTF%20%7C%203D%20Tiles-lightgrey)

> [!IMPORTANT]
> This file is the **human-readable** “evidence manifest” for the site.  
> Anything shown in the UI (facts, dates, interpretations, 3D assets, measurements) should be traceable to **at least one** source entry below — **or** to a documented PROV activity that derives it from cited inputs.

---

## 🧭 Where this file lives

```text
📁 web/assets/3d/archaeology/sites/<site-slug>/
└─ 📁 meta/
   └─ 📄 citations.md   ← you are here
```

---

## 📇 Record metadata

| Field | Value |
|---|---|
| Site slug | `<site-slug>` |
| Site name | `TODO: Human-readable name` |
| Region | `TODO: county/region` |
| Sensitivity | `public` / `restricted` / `embargoed` |
| Location precision shown in public UI | `exact` / `generalized` (e.g., hex / bbox / ~10km rounding) |
| Primary steward | `TODO: org/person/team` |
| Last updated | `YYYY-MM-DD` |
| Citation style | `KFM / Chicago-ish (author–title–year + link + access date)` |

> [!TIP]
> If the site is **sensitive**, do **not** publish exact coordinates here. Store exact coordinates in restricted metadata only and reference them via a gated catalog/ID.

---

## 🧾 How to cite this site record (copy/paste)

Use this when someone cites the **KFM site page / dataset** itself (not the historical sources).

**Suggested citation**
> `Kansas Frontier Matrix (KFM). (YEAR). "<SITE NAME> — 3D Archaeology Site Record" (Version X.Y.Z). Kansas Frontier Matrix. Accessed YYYY-MM-DD. <public URL or repository permalink>`

**If there is a DOI / persistent ID**
> `... DOI: <doi>`

---

## 🧠 What requires a citation (KFM evidence rules)

Cite sources for:

- ✅ **All factual claims** (dates, names, cultural affiliations, site type, periodization, measurements, relationships).
- ✅ **All derived claims** (e.g., “structure footprint is ~12m” derived from point cloud → mesh).
- ✅ **All interpretations / reconstructions** (clearly label as interpretation + cite rationale sources).
- ✅ **Any AI-assisted output** used in the UI (summaries, classifications, suggested relationships).

Do **not** do:

- ❌ “Trust me” statements
- ❌ Uncited AI narrative
- ❌ “Mystery layers” (assets with no origin/rights/provenance)

> [!NOTE]
> If an AI/assistant cannot attach citations, it should **refuse** or downgrade to “uncertain / hypothesis” with explicit limitations.

---

## 🔒 Sensitivity, ethics, & cultural protocols

| Control | Setting | Notes |
|---|---|---|
| Coordinate obfuscation | `TODO: on/off + method` | e.g., hex bin, bbox, rounding, centroid jitter |
| Role-based access | `TODO: public/research/admin` | who can see exact coords, raw captures, etc. |
| Cultural protocol tags | `TODO` | e.g., “restricted—community only”, “do not reproduce” |
| Rights holder constraints | `TODO` | license + any noncommercial / attribution / takedown rules |
| Redaction policy | `TODO` | what is removed from public view and why |

> [!CAUTION]
> Archaeological sites can be targets for looting. If there’s any risk, treat precise location as **restricted** unless explicit permission exists.

---

## 🧬 Provenance links (machine-readable twins)

> Fill these in so the UI + pipeline can validate lineage.

| Artifact | Path (recommended) | ID / Ref | Notes |
|---|---|---|---|
| STAC collection | `../stac/collection.json` | `TODO` | spatial/temporal extent + assets |
| STAC item(s) | `../stac/items/<item>.json` | `TODO` | per-capture / per-survey / per-model |
| DCAT dataset | `../dcat/dataset.json` | `TODO` | dataset discovery + distribution |
| PROV lineage | `../prov/lineage.jsonld` | `TODO` | activities: capture → process → publish |
| Checksums | `../meta/checksums.sha256` | `TODO` | hashes for key assets |
| License summary | `../meta/license.md` | `TODO` | optional, but recommended |

---

## 🗂️ Source index (fill this first)

Use stable keys. Keep keys **unchanged** once published.

| Key | Kind | Short citation | Link / DOI | License | Used for (what claims/assets) |
|---|---|---|---|---|---|
| `SRC-001` | `primary-report` | `TODO` | `TODO` | `TODO` | `TODO` |
| `SRC-002` | `dataset` | `TODO` | `TODO` | `TODO` | `TODO` |
| `SRC-003` | `3d-capture` | `TODO` | `TODO` | `TODO` | `TODO` |
| `SRC-004` | `photo-archive` | `TODO` | `TODO` | `TODO` | `TODO` |
| `SRC-005` | `code/pipeline` | `TODO` | `TODO` | `TODO` | `TODO` |

---

## 📚 Full source entries

> [!TIP]
> One entry per key. Use the same structure so humans + tooling can parse it.

### ✅ Template (copy for each source)

```markdown
### SRC-XXX — <Title>

- **Kind:** `primary-report` / `secondary` / `dataset` / `3d-capture` / `photo-archive` / `code/pipeline` / `oral-history`
- **Full citation (Chicago-ish):** <Author/Org>. <Title>. <Publisher/Repository>, <Year>. <Permalink/DOI>. (Accessed YYYY-MM-DD).
- **Creators / Contributors:** <names + roles>
- **Publisher / Holder:** <org>
- **Date range covered:** <YYYY–YYYY> (if applicable)
- **Geographic scope:** <generalized scope if sensitive>
- **License:** <SPDX-like if possible, e.g. CC-BY-4.0>
- **Rights notes / restrictions:** <noncommercial, no-derivatives, community-only, etc.>
- **KFM catalog refs:** <STAC item id(s) / DCAT id / PROV activity ids>
- **Used for:** <list of claims, assets, or UI panels this source supports>
- **Notes:** <quality, uncertainty, caveats, redactions>
```

---

### 🏺 Primary archaeological sources

<!-- Add excavation reports, site forms, nominations, grey literature, publications -->

### SRC-001 — `TODO`

- **Kind:** `primary-report`
- **Full citation (Chicago-ish):** `TODO`
- **Creators / Contributors:** `TODO`
- **Publisher / Holder:** `TODO`
- **Date range covered:** `TODO`
- **Geographic scope:** `TODO`
- **License:** `TODO`
- **Rights notes / restrictions:** `TODO`
- **KFM catalog refs:** `TODO`
- **Used for:** `TODO`
- **Notes:** `TODO`

---

### 🛰️ Remote sensing / GIS / basemaps

<!-- LiDAR, orthos, DEMs, GPR grids, survey shapefiles, etc. -->

### SRC-002 — `TODO`

- **Kind:** `dataset`
- **Full citation (Chicago-ish):** `TODO`
- **License:** `TODO`
- **KFM catalog refs:** `TODO`
- **Used for:** `TODO`

---

### 📷 3D capture sources (photogrammetry / LiDAR / scan)

> Capture sources should record **who**, **when**, **how**, and **where the raw data lives**.

### SRC-003 — `TODO`

- **Kind:** `3d-capture`
- **Full citation (Chicago-ish):** `TODO`
- **Capture date(s):** `TODO`
- **Capture method:** `photogrammetry` / `TLS` / `drone` / `structured-light` / `other`
- **Equipment:** `TODO` (camera/lens/scan rig)
- **Settings:** `TODO` (flight height, overlap, scan resolution, etc.)
- **Operator(s):** `TODO`
- **Raw data location:** `TODO` (restricted if needed)
- **License / permissions:** `TODO`
- **KFM catalog refs:** `TODO`
- **Used for:** `Raw point cloud / images feeding model build`
- **Notes:** `TODO`

---

### 🧱 Derived 3D assets & transformations

> [!IMPORTANT]
> Derived meshes/textures still need provenance: **what inputs** and **what process** created them.

#### 3D Asset register (recommended)

| Asset | Path | Format | Derived from | PROV activity | Source keys | License |
|---|---|---|---|---|---|---|
| `MODEL-001` | `../models/<file>.glb` | `glTF/glb` | `RAW-...` | `prov:activity:...` | `SRC-003` | `TODO` |
| `TEX-001` | `../textures/<file>.ktx2` | `KTX2` | `RAW-...` | `prov:activity:...` | `SRC-003` | `TODO` |

#### Processing log (optional but powerful)

| Step | Tool / method | Input | Output | PROV activity | Notes |
|---|---|---|---|---|---|
| `PROC-001` | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

---

### 🧑‍🏫 Interpretations, reconstructions, & hypotheses

> [!CAUTION]
> Mark interpretive elements clearly. Use “Interpretation:” or “Hypothesis:” labels.

### SRC-004 — `TODO`

- **Kind:** `secondary`
- **Full citation (Chicago-ish):** `TODO`
- **Used for:** `Interpretation of structure/function/chronology`
- **Notes:** `TODO (what is evidence vs inference?)`

---

### 🧪 Code, pipelines, notebooks (reproducibility)

If code directly produces outputs shown in the UI, cite it like a dataset.

### SRC-005 — `TODO`

- **Kind:** `code/pipeline`
- **Full citation (Chicago-ish):** `TODO`
- **Repository / commit:** `TODO`
- **Environment / container:** `TODO`
- **Used for:** `TODO`
- **Notes:** `TODO`

---

## 🧷 Claim ↔ evidence map (fast QA)

> This is the “no mystery claims” safety net.

| Claim ID | Claim (short) | Evidence source keys | Confidence | Notes |
|---|---|---|---|---|
| `CLM-001` | `TODO` | `SRC-001, SRC-002` | `high/med/low` | `TODO` |
| `CLM-002` | `TODO` | `SRC-003` | `high/med/low` | `TODO` |
| `CLM-003` | `TODO (interpretation)` | `SRC-001, SRC-004` | `med/low` | `TODO` |

---

## 🧾 Licenses & rights summary

| Category | License | Rights holder | Notes |
|---|---|---|---|
| 3D models | `TODO` | `TODO` | `TODO` |
| Textures | `TODO` | `TODO` | `TODO` |
| Photos | `TODO` | `TODO` | `TODO` |
| Derived datasets | `TODO` | `TODO` | `TODO` |
| Narrative text | `TODO` | `TODO` | `TODO` |

---

## 🔁 Change log

| Date | Change | Author |
|---|---|---|
| `YYYY-MM-DD` | `Initial citations scaffold` | `TODO` |

---

## ✅ QA checklist (before publishing)

- [ ] Every **asset** in `../models/`, `../textures/`, `../media/` is listed in **3D Asset register**
- [ ] Every **claim** shown in UI maps to at least one **SRC-###** in **Claim ↔ evidence map**
- [ ] Every **SRC-###** has: author/org, title, year, link/DOI (or internal location), access date, license
- [ ] Sensitive locations are **generalized** (or explicitly justified and permission recorded)
- [ ] STAC/DCAT/PROV pointers exist and resolve
- [ ] Checksums exist for public artifacts
- [ ] Any AI-assisted text is labeled and cited (or removed)

---

## 📚 Appendix: KFM internal project references (used to design this site record)

> These are **project-level** sources that define how citations/provenance/sensitivity work in KFM.  
> You typically cite these when explaining *system behavior*, not archaeological facts.

| Key | Document |
|---|---|
| `KFM-DOC-001` | *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation* |
| `KFM-DOC-002` | *Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design* |
| `KFM-DOC-003` | *Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖* |
| `KFM-DOC-004` | *Kansas Frontier Matrix – Comprehensive UI System Overview* |
| `KFM-DOC-005` | *📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide* |
| `KFM-DOC-006` | *🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals* |
| `KFM-DOC-007` | *Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)* |
| `KFM-DOC-008` | *Additional Project Ideas* |
| `KFM-DOC-009` | *Maps–GoogleMaps–VirtualWorlds–Archaeological–Computer Graphics–Geospatial–webgl (PDF portfolio)* |
| `KFM-DOC-010` | *AI Concepts & more (PDF portfolio)* |
| `KFM-DOC-011` | *Various programming languages & resources 1 (PDF portfolio)* |
| `KFM-DOC-012` | *Data Management – Theories/Architectures/Data Science/Bayesian Methods (PDF portfolio)* |

---

### 🧩 Appendix: Portfolio note (optional)

Some project PDFs are **PDF portfolios** (collections of embedded PDFs).  
If you cite a specific embedded document, create a dedicated `SRC-###` entry for it and include:

- Embedded filename
- Page span (if meaningful)
- How it was used (what it supports)

✅ Example embedded titles you might cite for 3D/virtual-world work:

- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `DesigningVirtualWorlds.pdf`
- `webgl-programming-guide.pdf`
- `google-maps-javascript-api-cookbook.pdf`

