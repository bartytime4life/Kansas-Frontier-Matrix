# USDA Soils — SDA Component Query 🌱🧱
> **Path:** `data/external/mappings/local/usda_soils/sda_component_query/`

![USDA](https://img.shields.io/badge/USDA-NRCS-2E7D32?style=for-the-badge)
![SDA](https://img.shields.io/badge/Soil%20Data%20Access-post.rest-1565C0?style=for-the-badge)
![KFM](https://img.shields.io/badge/KFM-External%20Integration-6A1B9A?style=for-the-badge)
![Status](https://img.shields.io/badge/status-active-00897B?style=for-the-badge)

This folder is the **local “query module”** for pulling **SSURGO/Soil Data Mart component-level attributes** from **USDA-NRCS Soil Data Access (SDA)** via the **`Tabular/post.rest`** REST/POST service.

It exists so KFM can **query soils by location / mapunit keys** instead of storing huge soil shapefiles locally, while still supporting **repeatable, provenance-friendly caching** when needed. 🧾🧭

---

## 🎯 What “component” means (in one breath)
A **map unit** can have multiple **components** (dominant/minor soils). The SDA **`component`** table (and friends) is where you pull things like:

- `compname`, `comppct_r`, `majcompflag`
- drainage / hydrologic group
- taxonomic classifications
- (optionally) joins to horizons, interpretations, etc.

This module focuses on the **component slice** so downstream steps can:
- summarize soils in plain language for the UI 🗣️
- compute suitability metrics for agriculture or land-use 🔬
- attach soils context to stories/places in KFM 🗺️

---

## 🧱 How this fits the KFM pipeline (canonical)
KFM expects external integrations to behave like first-class data sources:

- **Query SDA** (stateless REST/POST)
- **Optionally cache** the exact response + query inputs (for reproducibility)
- **Normalize** into a stable schema for KFM processing / DB ingestion

> **Rule of thumb:** use this folder to **define queries + mapping logic**.  
> Put *retrieved artifacts* into an **external cache** (date + parameters) and only promote curated outputs into processed datasets.

---

## 📦 Suggested folder layout (recommended)
If this directory is still being built out, this is the intended structure:

```text
📁 sda_component_query/
├─ 📄 README.md                          👈 you are here
├─ 📁 sql/
│  ├─ 🧾 component_basic.sql             # minimal component fields by mukey
│  ├─ 🧾 component_enriched.sql          # joins (mapunit, legend, etc.)
│  └─ 🧾 component_with_domains.sql      # optional: domains / lookups
├─ 📁 examples/
│  ├─ 🧪 request.body.json               # example REST body for curl
│  ├─ 🧪 response.sample.json            # small sample response
│  └─ 🧪 mukeys.sample.txt               # example mukey list
├─ 📁 mapping/
│  ├─ 🧬 schema.component.json           # normalized schema (KFM-facing)
│  └─ 🧩 map_component_fields.yml        # field mapping (SDA → KFM)
└─ 📁 out/                               # (local dev only) scratch outputs
   └─ 🚫 .gitkeep
```

---

## 🚀 Quickstart
### 1) Pick your SDA endpoint
Use the **REST/POST** query service:

- Endpoint: `https://SDMDataAccess.sc.egov.usda.gov/Tabular/post.rest`

### 2) Minimal request body (JSON)
```json
{
  "service": "query",
  "request": "query",
  "format": "JSON",
  "query": "SELECT TOP 10 mukey, cokey, compname, comppct_r, majcompflag FROM component WHERE mukey IN ('458913') ORDER BY comppct_r DESC"
}
```

### 3) Run with `curl`
```bash
curl -sS \
  -H "Content-Type: application/json" \
  -d @examples/request.body.json \
  "https://SDMDataAccess.sc.egov.usda.gov/Tabular/post.rest" \
  | jq .
```

> 🧠 Tip: Start with `format=~` to echo the expanded SQL (no execution) if you’re using macros.

---

## 🧾 Query templates
<details>
<summary><strong>🧾 Template A — Basic component attributes (by mukey)</strong></summary>

```sql
SELECT
  c.mukey,
  c.cokey,
  c.compname,
  c.comppct_r,
  c.majcompflag,
  c.hydgrp,
  c.drainagecl,
  c.taxorder,
  c.taxsuborder,
  c.taxgrtgroup,
  c.taxsubgrp
FROM component AS c
WHERE c.mukey IN ({{MUKEY_LIST}})
ORDER BY c.mukey, c.comppct_r DESC;
```

**Parameter notes**
- `{{MUKEY_LIST}}` should be a comma-separated list of quoted keys:
  - ✅ `'458913','458914'`
  - 🚫 don’t include whitespace if you’re also using `mukeylist` elsewhere

</details>

<details>
<summary><strong>🧾 Template B — Enriched join (mapunit name + areasymbol)</strong></summary>

```sql
SELECT
  l.areasymbol,
  mu.mukey,
  mu.muname,
  c.cokey,
  c.compname,
  c.comppct_r,
  c.majcompflag,
  c.hydgrp,
  c.drainagecl
FROM legend AS l
INNER JOIN mapunit AS mu
  ON mu.lkey = l.lkey
INNER JOIN component AS c
  ON c.mukey = mu.mukey
WHERE mu.mukey IN ({{MUKEY_LIST}})
ORDER BY l.areasymbol, mu.mukey, c.comppct_r DESC;
```

</details>

---

## 🗃️ Caching + provenance (do this when results matter)
When a query is used in a reproducible workflow (not just ad-hoc UI lookup), cache:

✅ **Inputs**
- query text (exact)
- request parameters (format/service/request)
- mukeys / AOI geometry / areasymbol filters
- timestamp + environment (dev/prod)

✅ **Outputs**
- raw response payload (JSON/XML)
- a normalized artifact (CSV/Parquet/JSONL) if used downstream

### Suggested cache naming
```text
data/processed/external_cache/usda_sda/
└─ 2026-01-29/
   ├─ sda_component__mukeys_458913__format_JSON__run_001.json
   ├─ sda_component__mukeys_458913__format_JSON__run_001.request.json
   └─ sda_component__mukeys_458913__format_JSON__run_001.meta.yml
```

---

## 🧰 Guardrails (SDA constraints + best practices)
- ✅ Always use a **WHERE clause** / constrained join to avoid huge responses.
- ✅ SDA enforces a **maximum row return** (don’t assume you can pull a whole state in one go).
- ✅ If you need big pulls, chunk requests (by `areasymbol`, `mukey`, etc.).
- ✅ Prefer **`JSON+COLUMNNAME+METADATA`** when you want schema-aware ingestion.
- ✅ Respect timeouts: “immediate” queries can time out; design for retries & chunking.

---

## 🧪 Validation checklist
Run these before calling the module “good” ✅

- [ ] Example query returns JSON successfully (HTTP 200)
- [ ] Returned rows contain expected fields (e.g., `compname`, `comppct_r`)
- [ ] Sorting by `comppct_r DESC` yields most dominant components first
- [ ] Chunking strategy exists for >100k rows scenarios
- [ ] Cached artifacts include query + parameters + timestamp (reproducible)

---

## 🔗 Related KFM docs
- 📚 KFM soils domain module (conceptual + governance):  
  `../../../../../../docs/data/soils/sda/README.md`

- 🧭 KFM pipeline + data governance conventions live in the repo docs (see `docs/`)

---

## 📚 SDA references (official)
- SDA Query UI (helpful for testing SQL):  
  `https://sdmdataaccess.nrcs.usda.gov/Query.aspx`

- SDA Query Help hub (guides, diagrams, sample queries):  
  `https://sdmdataaccess.nrcs.usda.gov/queryhelp.aspx`

- SDA Web Service Help (REST/POST `post.rest` parameters):  
  `https://sdmdataaccess.nrcs.usda.gov/webservicehelp.aspx`

---

## 🏷️ Attribution
Soils data retrieved through this module comes from **USDA-NRCS Soil Data Access / Soil Data Mart**.  
Whenever results are displayed in KFM (maps, UI summaries, exports), include clear source attribution to USDA-NRCS SDA. ✅

---
