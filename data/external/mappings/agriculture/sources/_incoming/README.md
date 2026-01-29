# 🌾📥 `_incoming` — Agriculture Mapping Sources (Staging Drop Zone)

![Stage](https://img.shields.io/badge/stage-_incoming%20(quarantine)-blue)
![Domain](https://img.shields.io/badge/domain-agriculture-2ea44f)
![Policy](https://img.shields.io/badge/policy-provenance--first-important)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-purple)

> [!IMPORTANT]
> Anything in `data/external/mappings/agriculture/sources/_incoming/` is **not yet trusted**, **not yet standardized**, and **not yet “published”**.  
> Treat it like a **quarantine + paperwork desk**: we park new source material here while we verify licensing, integrity, and documentation before it can enter the canonical pipeline.

---

## 🧭 What this folder is for

This folder is the **first landing zone** for *new* external agriculture-related mapping sources, including:

- 🗺️ **Codelists / classification docs** (crop codes, soil classes, land-use classes)
- 📄 **Provider documentation** (PDF manuals, method notes, field definitions)
- 📦 **Raw downloads** (zips, geodatabases, CSVs) that have **not** been normalized
- 🔗 **Link-only sources** where we store retrieval instructions + snapshots (when allowed)

**Goal:** make the “paper trail” easy so the data can safely move into the KFM pipeline (raw → processed → catalogs/prov → DB → API → UI).  

---

## 🚫 What does *not* belong here

- ❌ “Final” layers meant for production use (those belong in `data/processed/...`)
- ❌ Hand-edited GIS outputs that can’t be reproduced (keep edits in pipelines/workflows)
- ❌ Anything with unclear usage rights or unknown provenance
- ❌ Sensitive datasets you’re not allowed to publish to the repo (see 🛡️ Ethics & restrictions)

---

## 🧱 Expected folder structure

Create **one folder per source drop**:

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 🌾 agriculture/
         └─ 📁 sources/
            └─ 📁 _incoming/                                      📥 staging for newly received source bundles
               └─ 📁 <provider>__<dataset>__<version-or-date>/     🧷 one intake drop (provider + dataset + snapshot)
                  ├─ 📁 source/                                   🧾 original files (untouched / as-received)
                  ├─ 📁 docs/                                     📚 PDFs, codebooks, screenshots, emails-as-PDF
                  ├─ 🧾 manifest.yml                              ✅ intake index (what’s included + where it came from)
                  ├─ 📄 LICENSE.md                                ✅ license/terms text (or 📄 LICENSE.txt)
                  ├─ 🔐 checksums.sha256                          ✅ sha256 for every file in this drop
                  └─ 📄 notes.md                                  ◻️ optional (recommended): context, caveats, next steps

> [!TIP]
> Prefer `provider__dataset__YYYY-MM-DD` (or `provider__dataset__vX.Y__YYYY-MM-DD`) so diffs and audits stay clean.
```

---

## 🏷️ Naming rules (keep it boring = keep it reliable)

Use only:
- ✅ lowercase letters, numbers
- ✅ underscores `_` and double-underscores `__` as separators
- ✅ ISO dates (`YYYY-MM-DD`) when the “version” is a retrieval date

Examples:
- `usda_nass__cropland_data_layer__2025-01-10/`
- `nrcs__ssurgo__v2024_10__2024-10-01/`
- `kda__crop_reporting_districts__2023-06-15/`

---

## 📋 Required artifacts per incoming source

| Artifact | Required | Why it exists |
|---|---:|---|
| `source/` | ✅ | Immutable “as-received” snapshot (no edits) |
| `manifest.yml` | ✅ | Minimal machine-readable description + provenance pointers |
| `LICENSE.md` | ✅ | Clear usage rights (or explicit restriction notes) |
| `checksums.sha256` | ✅ | Integrity verification + reproducibility |
| `docs/` | ⭐ | Provider documentation that explains fields/assumptions |
| `notes.md` | ⭐ | Human context: what it is, why we want it, gotchas |

⭐ = strongly recommended

---

## ✅ Definition of Done (DoD) for promoting out of `_incoming`

> [!NOTE]
> Promotion means: this source is **ready** to be moved/ingested into canonical staging (`data/raw/...` → `data/work/...` → `data/processed/...`) with catalogs + provenance.

**Checklist:**

- [ ] **License is explicit** (allowed use, attribution, redistribution limits)
- [ ] **Provenance is clear** (where it came from, how it was obtained, when)
- [ ] **Raw integrity captured** (`checksums.sha256` created and verified)
- [ ] **Basic “can we open it?” QA** (format readable, not corrupted)
- [ ] **Spatial reference is known** (CRS/EPSG stated somewhere, or documented in `notes.md`)
- [ ] **Temporal coverage is stated** (what years/dates does it represent?)
- [ ] **Restrictions & sensitivity reviewed** (no accidental PII / sensitive locations / prohibited redistribution)
- [ ] **Mapping intent defined** (what normalization/crosswalk do we intend to derive from this?)

---

## 🔁 Promotion path (how `_incoming` becomes “real”)

1. **Stage and document here** (`_incoming/`)  
2. **Move raw snapshot into canonical raw**  
   - `data/raw/agriculture/...` (or the domain-appropriate canonical raw location)
3. **ETL to `data/work/...` then `data/processed/...`** (deterministic + replayable)
4. **Publish boundary artifacts** *(required before downstream use)*  
   - 🗂️ STAC (collections/items)  
   - 🧾 DCAT dataset entry  
   - 🧬 PROV lineage bundle
5. **Only then** load into DB/graph and expose via API/UI

> [!IMPORTANT]
> Do **not** shortcut: publishing requires catalogs + provenance first, then graph/API/UI usage.

---

## 🌾 Agriculture-specific tips (common “gotchas”)

- 🧩 **Codelists matter**: agriculture datasets often encode crop types, rotations, practices, soil classes, etc.  
  If a dataset has codes, treat its documentation as **first-class** input material.
- 🧭 **CRS drift is real**: county/state layers, raster grids, and vector parcels often mix projections.
- 📆 **Annual products**: many agriculture layers are yearly; document whether each file is a year, a season, or a multi-year composite.
- 🧪 **Derived “evidence artifacts”**: if you create a crosswalk table or normalized classification from these sources, treat it as a *dataset* and publish it with the same rigor (metadata + provenance).

---

## 🧰 Templates

<details>
<summary><strong>📄 <code>manifest.yml</code> starter template (copy/paste)</strong></summary>

```yaml
id: "<provider>__<dataset>__<version-or-date>"
title: "<Human friendly title>"
domain: "agriculture"
stage: "incoming"

source:
  provider: "<org name>"
  homepage: "<url or blank>"
  download_url: "<url or blank>"
  retrieved_at: "<YYYY-MM-DD>"
  version: "<vX.Y or YYYY-MM-DD>"
  citation: "<preferred citation string or DOI>"

license:
  name: "<license name>"
  url: "<license url>"
  redistribution: "<allowed|restricted|unknown>"
  notes: "<any constraints or attribution requirements>"

files:
  - path: "source/<filename.ext>"
    sha256: "<optional here if you also keep checksums.sha256>"
    format: "<csv|zip|gdb|tif|geojson|...>"
    notes: "<what this file is>"

coverage:
  spatial:
    description: "<e.g., Kansas statewide, CONUS, county boundaries>"
    crs: "<EPSG:#### or 'unknown'>"
  temporal:
    start: "<YYYY-MM-DD or YYYY>"
    end: "<YYYY-MM-DD or YYYY>"

mapping_intent:
  - "<e.g., build crop-code crosswalk to KFM canonical ag classes>"
  - "<e.g., normalize field names + units>"
qa:
  opened_successfully: false
  notes: ""
```

</details>

<details>
<summary><strong>📝 <code>notes.md</code> suggested headings</strong></summary>

```md
# Notes — <provider> / <dataset>

## Why we want this
- ...

## What it contains
- ...

## Known issues / caveats
- ...

## CRS / projection
- ...

## Temporal coverage
- ...

## Next step (promotion plan)
- ...
```

</details>

---

## 📚 Project anchors (why these rules exist)

- Canonical pipeline order (Raw → Processed → Catalog/Prov → Database → API → UI):contentReference[oaicite:0]{index=0}  
- KFM is provenance-first and follows FAIR + CARE principles:contentReference[oaicite:1]{index=1}  
- Required staging: `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/` + publish STAC/DCAT/PROV as boundary artifacts:contentReference[oaicite:2]{index=2}  
- STAC/DCAT/PROV alignment policy and minimum DCAT fields (incl. license):contentReference[oaicite:3]{index=3}  
- “Provenance first” + “pipeline ordering is absolute” invariants (must not regress):contentReference[oaicite:4]{index=4}

---

