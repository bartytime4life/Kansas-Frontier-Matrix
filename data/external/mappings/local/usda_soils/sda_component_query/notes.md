# 🧱 USDA Soils — SDA `component` Query Notes

![scope](https://img.shields.io/badge/scope-usda__soils-2b6cb0)
![service](https://img.shields.io/badge/service-Soil%20Data%20Access%20%28SDA%29-0ea5e9)
![type](https://img.shields.io/badge/type-tabular%20REST%2FPOST-10b981)

Internal notes for pulling **SSURGO component-level attributes** (the `component` table) from USDA NRCS **Soil Data Access (SDA)** and shaping them into **local mapping artifacts**.

---

## 🧭 Quick Intent

| What | Why |
|---|---|
| Query SDA’s `component` table (optionally joined to `legend` + `mapunit`) | Build a local, reproducible lookup for **soil components** per **map unit** (e.g., major component, % composition, hydrologic group, taxonomy, etc.) |
| Prefer **small, deterministic** queries | SDA has row/serialization limits; we want stable outputs + easy cache keys |
| Store **raw responses + metadata** | Reproducibility & provenance (especially because SSURGO updates) |

---

## 🗂️ Folder Context

Suggested layout (keep it simple, cache-friendly):

```text
📁 data/
└─ 📁 external/
   └─ 📁 mappings/
      └─ 📦 local/                                🏛️ local/partner/API-driven mappings + examples
         └─ 🌾 usda_soils/                         🧱 USDA soils (SDA) query mappings + helpers
            └─ 📁 sda_component_query/             🧪 SDA component query package (SQL + runner + outputs)
               ├─ 📝 notes.md                       👈 you are here (assumptions, caveats, troubleshooting)
               ├─ 🧾 query.sql                       ✅ canonical SQL template(s)
               ├─ 🐍 run.py                          ◻️ optional: runner (POST + parse + write outputs)
               └─ 📁 out/                            📦 generated outputs (usually gitignored or kept small)
                  ├─ 📄 component.parquet            📦 output table (preferred)
                  ├─ 📄 component.csv                📄 output export (interchange)
                  ├─ 🧾 request.json                 🧾 captured request payload (sanitized)
                  └─ 🧾 response_meta.json           🧾 response metadata (timings, status, paging, notes)
```

---

## 🧩 Core Keys & Terms (SSURGO mindset)

- **`areasymbol`** 🏷️ = survey area identifier (SSURGO is typically `ST###`, 5 chars; STATSGO is commonly `US`)
- **`mukey`** 🗺️ = map unit key (unique ID for a map unit)
- **`cokey`** 🧬 = component key (unique ID for a component within map units)
- **`comppct_r`** 📊 = representative % composition of a component in a map unit (often used to sort components descending)
- **`majcompflag`** ⭐ = major component flag
- **Spatial joins**: SDA supports spatial tables (e.g., `mupolygon`) + helper functions that return intersected `mukey` values from WKT polygons.

---

## 🌐 SDA Endpoint & Request Shape

**Tabular REST/POST endpoint (commonly used):**

```text
https://sdmdataaccess.sc.egov.usda.gov/tabular/post.rest
```

**Recommended POST fields (form-encoded):**
- `query` = SQL (can include multiple statements + one or more `SELECT`s)
- `format` = `JSON+COLUMNNAME` (easiest to parse)

> ✅ Tip: `JSON+COLUMNNAME` returns column names in the first row of the `Table` payload, then data rows after.

---

## 🧾 Query Templates

### 1) 🎯 “By `mukey` list” (fast + deterministic)

Use when you already have `mukey` values (from polygons, inventory, or a prior step).

```sql
-- Pull component basics for a known set of map unit keys
SELECT
  mu.mukey,
  c.cokey,
  c.compname,
  c.comppct_r,
  c.majcompflag,
  c.localphase,
  c.slope_r,
  c.hydgrp,
  c.taxclname,
  c.taxorder,
  c.taxsuborder
FROM mapunit AS mu
JOIN component AS c
  ON c.mukey = mu.mukey
WHERE mu.mukey IN ('458913','458914')  -- TODO: inject list
ORDER BY mu.mukey, c.comppct_r DESC, c.compname;
```

✅ Good for caching: the **sorted mukey list** can become your cache key.

---

### 2) 🧭 “By AOI polygon” (WKT ➜ intersected `mukey` ➜ components)

Use when you have an AOI geometry and want mapunit components within it.

```sql
-- Intersect AOI polygon (WGS84) to get mukeys, then fetch components
-- Replace the polygon coordinates with your AOI in WKT (EPSG:4326)
SELECT
  l.areasymbol,
  mu.mukey,
  mu.musym,
  mu.muname,
  c.cokey,
  c.compname,
  c.comppct_r,
  c.majcompflag,
  c.hydgrp
FROM SDA_Get_Mukey_from_intersection_with_WktWgs84(
  'polygon((
    -121.157072910308 46.0181639308995,
    -121.321280753631 45.9248106152548,
    -121.348997869021 45.9168439802811,
    -121.157072910308 46.0181639308995
  ))'
) AS s
JOIN mapunit AS mu
  ON mu.mukey = s.mukey
JOIN legend AS l
  ON l.lkey = mu.lkey
JOIN component AS c
  ON c.mukey = mu.mukey
WHERE l.areasymbol <> 'US'             -- filter STATSGO
ORDER BY l.areasymbol, mu.museq, c.comppct_r DESC;
```

> ⚠️ WKT requirements:
> - Must be **WGS84** for the `...WktWgs84` functions
> - Polygon must be **closed** (first point == last point)

---

### 3) 🧰 “Big mukey list” (use an Int table variable)

When `IN (...)` lists get huge, create a table variable (SDA supports helpful macro expansions).

```sql
-- SDA macro: declare a table variable with a single int column named "i"
~DeclareIntTable(@mukeys)~

-- Fill the table
INSERT INTO @mukeys (i) VALUES
(458913),
(458914);

-- Query against the table
SELECT
  mu.mukey,
  c.cokey,
  c.compname,
  c.comppct_r,
  c.majcompflag
FROM @mukeys AS k
JOIN mapunit AS mu
  ON mu.mukey = k.i
JOIN component AS c
  ON c.mukey = mu.mukey
ORDER BY mu.mukey, c.comppct_r DESC;
```

---

## 📦 Response Parsing Notes (JSON+COLUMNNAME)

Typical response pattern:

- JSON root contains `"Table": [...]`
- **First row** = column names
- Rows 2..N = values as strings (often needs type conversion)

Suggested normalization steps:
- Convert: `mukey`, `cokey` → strings (preserve leading/trailing formatting as delivered)
- Convert: `comppct_r` → integer
- Convert: `slope_r` → numeric
- Convert: `majcompflag` → boolean (or keep as `"Yes"/"No"` depending on SDA output)

---

## 🧱 Limits, Chunking & “Don’t Melt the Server” 😅

Practical rules:
- Always include **a constraining clause**: AOI, `areasymbol`, or `mukey` chunk
- If a query might exceed limits:
  - Split by **`areasymbol`** (state/county survey areas)
  - Or split by **mukey batches** (e.g., 200–1000 at a time)
- Prefer returning only the columns you truly need

---

## 🧾 Versioning & Provenance (important for reproducibility)

Soil data is **versioned by survey area** and can be updated.
Minimum metadata to store per extraction:
- `endpoint` (string)
- `format` (string)
- `query` (full SQL text)
- `retrieved_at` (UTC timestamp)
- `areasymbol`(s) used (if any)
- `saversion` / `saverest` (when available via joins to `sacatalog`)

✅ Recommendation: store `request.json` + `response_meta.json` right next to your output file.

---

## ✅ Output Contract (suggested)

Even if you only need a handful of fields now, keeping a stable “contract” saves pain later:

**Minimum recommended output columns**
- `areasymbol` (if joined)
- `mukey`
- `cokey`
- `compname`
- `comppct_r`
- `majcompflag`

**Nice-to-have**
- `localphase`
- `slope_r`
- `hydgrp`
- `taxorder`, `taxsuborder`, `taxclname`

---

## 🧪 Quick Test (manual)

- Use SDA’s built-in POST test page to validate SQL syntax and output formats.
- Start with a **single mukey** and a small column set, then expand.

---

## 🆘 Common Failure Modes

- **Empty results**: AOI doesn’t intersect SSURGO areas, or `areasymbol` filter too strict
- **Oversized AOI**: AOI boundary too large (split AOI)
- **Too many rows**: missing constraint or too-wide join
- **Parsing errors**: wrong `format`, or expecting JSON when you got XML

---

## 🧾 TODOs (module hardening)

- [ ] Add canonical `query.sql` with placeholders
- [ ] Add a small runner script (POST + parse + write parquet/csv)
- [ ] Add deterministic cache key (`sha256(query + format + endpoint)`)
- [ ] Add unit test that validates schema + type casting
- [ ] Add “chunk strategy” helper (mukey batches, areasymbol batches)

---

