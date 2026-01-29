# 🧾 U.S. Census Bureau Data — License & Attribution (Census + TIGER/Line®)

[![Source](https://img.shields.io/badge/source-U.S.%20Census%20Bureau-0b7285)](https://www.census.gov/)
[![Products](https://img.shields.io/badge/products-TIGER%2FLine%C2%AE%20%7C%20ACS%20%7C%20Decennial%20%7C%20API-5f3dc4)](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
[![Copyright](https://img.shields.io/badge/copyright-not%20available%20(17%20U.S.C.%20%C2%A7105)-2b8a3e)](https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2025/TGRSHP2025_TechDoc_Ch1.pdf)
[![Attribution](https://img.shields.io/badge/attribution-required%20in%20KFM%20%7C%20requested%20by%20Census-f08c00)](#-attribution-requirements)

> 🧭 **Purpose:** Canonical guidance for how **KFM** stores, credits, and redistributes **U.S. Census Bureau** geographic + statistical products.  
> ⚠️ **Not legal advice.** Always check the specific dataset’s metadata/technical docs if something looks “special” or third‑party.

---

## 📦 Folder context

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 📦 census/                                    🧮 Census/TIGER mapping packs + plans
         └─ 📁 sources/                                 📚 source notes, licensing, attribution guidance
            └─ 📄 census_license_and_attribution.md      👈 you are here (license terms + attribution boilerplate)
```

---

## 🎯 Scope

This file applies to **any** KFM dataset/layer built from U.S. Census Bureau products, including:

- 🗺️ **TIGER/Line® Shapefiles** (and derived products like vector tiles, PMTiles, GeoParquet)
- 🧱 **Cartographic boundary products** derived from TIGER/Line (where applicable)
- 📊 **ACS / Decennial / Economic** tables obtained via:
  - **data.census.gov**
  - **Census Data API** (`api.census.gov`)
  - downloadable files from `census.gov` / `www2.census.gov`

---

## ✅ Quick copy/paste credits

### 1) Map footer / legend (TIGER/Line® boundaries)
**Source:** U.S. Census Bureau — TIGER/Line® Shapefiles (Vintage: `YYYY`).

### 2) App uses Census Data API (required notice)
**Notice:** “This product uses the Census Bureau Data API but is not endorsed or certified by the Census Bureau.”

### 3) Long‑form citation (recommended for exports, docs, research)
U.S. Census Bureau, “`<File or Table Name>`,” `<Full Product Name>`, `<Vintage>`, `<URL>`, accessed `<YYYY-MM-DD>`.

---

## 🧠 License & rights summary

### 🏛️ U.S. Government works (general rule)
Census Bureau materials are U.S. Government works; **U.S. copyright protection is not available** for such works (17 U.S.C. §105). Practically, this means you can generally **use, copy, adapt, and redistribute**.

**Census Bureau request:** Even when reuse is permitted, they ask that you **cite the Census Bureau as the source**.

> 🧩 KFM rule: **KFM treats attribution as mandatory** for all external sources (even if the upstream source frames it as “requested”). This keeps our provenance clean and CI/policy checks happy. ✅

### 🧾 Third‑party caveat
Some pages or bundled products can include **non‑Census** content (e.g., partner-provided data, proprietary add-ons, external base layers).  
If the dataset’s own docs/metadata indicate third‑party licensing, **that third‑party license governs that component**.

---

## 🏷️ Attribution requirements

### Minimum (every Census-derived dataset/layer)
Include:
- **Publisher/source:** “U.S. Census Bureau”
- **Product name:** (e.g., “TIGER/Line® Shapefiles”, “American Community Survey 5‑Year Estimates”)
- **Vintage/year:** (e.g., 2024, 2022)
- **Access date** for reproducibility (recommended)

### Strongly recommended (exports, reports, story pages)
Use the Census Bureau’s recommended citation structures and include:
- Table/file identifier (if available)
- Full product name
- Vintage
- URL
- Accessed date

### 🧑‍⚖️ Analysis responsibility note (recommended)
When you compute or model using Census data, include:
- “Conclusions drawn from analysis are the sole responsibility of the performing party.”

---

## ™️ Trademarks & branding

### TIGER/Line® trademark
- **TIGER/Line®** is a **registered trademark** of the Census Bureau.
- Do **not** use “TIGER/Line” **as or within** proprietary/commercial product names.
- If KFM **repackages** TIGER/Line data for redistribution, include a **conspicuous** statement explaining trademark usage and visibility expectations.

### Census seal / logo
- The **Bureau of the Census seal** is for official/legal documents (don’t use it in KFM UI/exports unless you have explicit authorization).
- Avoid any branding that could imply **official endorsement**.

---

## 🧯 Warranty & boundary disclaimer (important for mapping!)

If we publish or render TIGER/Line boundary layers, include a disclaimer (at least in docs; ideally also in exports):

- No warranty (expressed or implied) on positional/attribute accuracy.
- Boundaries are for **statistical purposes** and **are not legal land descriptions**.

---

## 🔌 Census Data API-specific rules (when applicable)

If a feature uses the **Census Data API**:

### Required attribution notice (in-app)
Display prominently:
> “This product uses the Census Bureau Data API but is not endorsed or certified by the Census Bureau.”

### Avoid endorsement & misrepresentation
- You may reference the Census Bureau as the **source**.
- You may **not** imply endorsement/certification by the Census Bureau.
- You may **not** modify or falsely represent API content and still claim “Census Bureau” as the source.

### Privacy / confidentiality guardrails
Do **not** attempt to identify any person/household/business using API data alone or combined with other data.

---

## 🧩 KFM implementation checklist

### 1) UI / map credits 🗺️
- [ ] Add a **layer credit** when any Census layer is enabled:
  - “Source: U.S. Census Bureau — `<Product>` (`YYYY`).”
- [ ] If Census API is used: surface the **required API notice** in an About panel, layer details modal, footer, or similar prominent UI.

### 2) STAC/DCAT metadata 📚
Every processed Census-derived dataset must include:
- [ ] `license` (public-domain / U.S. Government work)
- [ ] `providers` / `publisher` set to “U.S. Census Bureau”
- [ ] A link back to **this file** so the attribution rules travel with the dataset ✅

#### Example STAC snippet
```json
{
  "license": "CC0-1.0",
  "providers": [
    {
      "name": "U.S. Census Bureau",
      "roles": ["producer", "licensor"],
      "url": "https://www.census.gov"
    }
  ],
  "links": [
    {
      "rel": "license",
      "href": "data/external/mappings/census/sources/census_license_and_attribution.md",
      "type": "text/markdown",
      "title": "Census license + attribution guidance (KFM)"
    }
  ]
}
```

> 📝 Note: `CC0-1.0` is used here as an **SPDX-friendly “public-domain marker”** for metadata tooling.  
> The underlying basis is U.S. Government work (17 U.S.C. §105) + Census Bureau’s own reuse/citation guidance.

### 3) Redistribution / repackaging 📦
If KFM publishes any derived distribution (tiles, cached files, repackaged shapefiles):
- [ ] Put the Census credit + vintage on the **README** and/or **dataset landing page**
- [ ] Include trademark and disclaimer language for TIGER/Line®
- [ ] Include the **API non‑endorsement** notice if API-derived

---

## 🧰 Templates (copy/paste)

<details>
<summary><strong>🗺️ Map credit template (TIGER/Line® boundaries)</strong></summary>

**Source:** U.S. Census Bureau — TIGER/Line® Shapefiles (`YYYY`).  
**Disclaimer:** Boundaries shown are for statistical purposes only and are not legal land descriptions.

</details>

<details>
<summary><strong>📊 data.census.gov table citation template</strong></summary>

U.S. Census Bureau, “`<Table Name>`,” `<Full Product Name>`, `<Vintage>`, `<URL>`, accessed `<YYYY-MM-DD>`.

</details>

<details>
<summary><strong>🔌 Census Data API required notice</strong></summary>

“This product uses the Census Bureau Data API but is not endorsed or certified by the Census Bureau.”

</details>

<details>
<summary><strong>📦 Repackaging / redistribution template (TIGER/Line®)</strong></summary>

This product includes data from the U.S. Census Bureau’s TIGER/Line® Shapefiles (`YYYY`).  
TIGER/Line® is a registered trademark of the U.S. Census Bureau.  
This product is not endorsed or certified by the U.S. Census Bureau.

</details>

---

## 🔗 Official references

- 🧾 Census citation guidance: https://www.census.gov/about/policies/citation.html  
- 🔌 Census Data API Terms of Service: https://www.census.gov/data/developers/about/terms-of-service.html  
- 🗺️ TIGER/Line Shapefiles hub: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html  
- 📄 TIGER/Line® Shapefiles Technical Documentation (Legal Disclaimer + Citation):  
  https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2025/TGRSHP2025_TechDoc_Ch1.pdf  

---

## 🧾 Changelog

- **2026-01-29** — Initial version (canonical KFM Census license + attribution guidance).

