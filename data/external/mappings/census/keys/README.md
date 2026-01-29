# 🗝️ Census Keys — Lookup Tables & Codebooks

![Scope](https://img.shields.io/badge/scope-US%20Census%20%26%20ACS-blue)
![Type](https://img.shields.io/badge/type-reference%20keys-6f42c1)
![Format](https://img.shields.io/badge/formats-CSV%20%7C%20JSON%20%7C%20YAML-lightgrey)
![Joins](https://img.shields.io/badge/joins-deterministic-success)
![Governance](https://img.shields.io/badge/governance-provenance--first-2ea44f)

> [!NOTE]
> This folder contains **small, versioned “key” files** used to **decode, normalize, and join** U.S. Census datasets (e.g., **FIPS**, **GEOID**, table/variable identifiers, and crosswalks).  
> Think of these as **reference lookups**, not “the dataset itself.” ✅

---

## Contents 🧭

- [Purpose](#purpose)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Key categories](#key-categories)
- [File contract](#file-contract)
- [GEOID & FIPS cheat sheet](#geoid--fips-cheat-sheet)
- [Usage examples](#usage-examples)
- [Validation checklist](#validation-checklist)
- [Updating / contributing keys](#updating--contributing-keys)
- [Privacy & ethics](#privacy--ethics)
- [Glossary](#glossary)

---

<a id="purpose"></a>
## Purpose 🎯

Census data is “join-heavy” and code-heavy. Small inconsistencies (missing zero padding, mixed vintages, renamed variables) can silently break analysis and maps.

These key files exist to:

- ✅ **Standardize joins** across pipeline stages (raw → processed → catalogs → DB → API → UI)
- 🧩 **Decode codes into labels** (so the UI and narratives don’t embed magic numbers)
- 🧷 **Preserve provenance & reproducibility** by versioning reference lookups alongside code
- 🧪 **Enable validation** (e.g., “all GEOIDs match expected length/pattern”)

---

<a id="what-belongs-here"></a>
## What belongs here 📦

Keep this directory focused on **small, stable, text-first reference artifacts**, such as:

- 🗺️ **Geography keys**
  - State/county FIPS lookup tables
  - GEOID format rules (templates, regex, expected lengths)
  - Summary-level code lists (if used)
- 🧾 **Variable/table dictionaries**
  - ACS / Decennial table lists
  - “Concept / label / universe” mappings (when available)
  - KFM-friendly canonical field name mappings
- 🔁 **Crosswalks**
  - Vintage-to-vintage geographic crosswalks (tract/block-group changes)
  - Code changes across time (renames, merges/splits, recodes)
- 🧰 **Normalization helpers**
  - Common enum mappings (e.g., “race categories” → canonical categories)
  - Unit mappings (if your pipeline standardizes units)

---

<a id="what-does-not-belong-here"></a>
## What does not belong here 🚫

- 🧱 Full TIGER/Line shapefiles, large boundary extracts, or bulk tables  
  → those go through the normal data lifecycle (raw/work/processed).
- 🧍 Any **microdata** or address-level / personally identifying information  
  → **never** store that here.
- 🧨 Ad-hoc “one-off” local mappings with no source or metadata  
  → either formalize as a key (with provenance), or keep it inside an experiment branch.

> [!IMPORTANT]
> **Keys are “infrastructure.”** Treat them like code: reviewed, versioned, and deterministic. 🧠

---

<a id="key-categories"></a>
## Key categories 🗂️

You can keep keys flat, or group them (recommended). Here’s a **suggested** layout:

```text
data/external/mappings/census/keys/
├── README.md
├── manifest.yml                  # optional: index of keys in this folder
├── geography/                     # FIPS / GEOID / summary levels
│   ├── fips_state__YYYY.csv
│   ├── fips_county__YYYY.csv
│   ├── geoid_formats__canonical.yml
│   └── summary_levels__canonical.csv
├── variables/                     # table/variable dictionaries
│   ├── acs_tables__YYYY.csv
│   └── acs_variables__YYYY.csv
└── crosswalks/                    # vintage-to-vintage mappings
    ├── tract__YYYY_to_YYYY.csv
    └── block_group__YYYY_to_YYYY.csv
```

If you prefer a flat folder, keep the **same naming + metadata rules** below.

---

<a id="file-contract"></a>
## File contract 📜

### 1) Filename conventions 🏷️

Use a predictable, grep-friendly pattern:

- **Preferred:** `<topic>__<vintage>.{csv|json|yml}`
  - Examples:
    - `fips_state__2024.csv`
    - `acs_tables__2023.csv`
    - `tract_crosswalk__2010_to_2020.csv`
- For stable, cross-vintage definitions:
  - `__canonical` (project-wide stable)
  - `__static` (rarely changes; still version when it *does*)

### 2) Treat codes as strings ✅

> [!WARNING]
> **Never** store/join FIPS/GEOID fields as integers.  
> Leading zeros are meaningful and must be preserved.

In CSVs, store codes with quotes when needed (or ensure your readers load them as strings).

### 3) Minimal metadata (required) 🧾

Every key file must have **either**:

- ✅ a sidecar: `the_file.csv.meta.yml` *(recommended)*  
**or**
- ✅ a header comment block (only if the format supports comments cleanly)

**Sidecar template (example):**
```yaml
id: census_key__fips_state__2024
title: "State FIPS codes (2024 snapshot)"
description: "Reference lookup for state FIPS → name/abbr."
source:
  name: "US Census Bureau"
  url: "https://…"
retrieved_at: "2024-10-01"
license: "…"
notes: "Any quirks, transformations, or known issues."
inputs:
  - "raw download file path or checksum reference"
checks:
  - "unique(code)"
  - "len(code)==2"
```

### 4) Table schemas (recommended) 🧩

**Code list files (CSV):**
- `code` *(string, required)*
- `label` *(string, required)*
- `description` *(string, optional)*
- `effective_start` / `effective_end` *(optional; ISO date or year)*
- `notes` *(optional)*

**Crosswalk files (CSV):**
- `from_code` *(string, required)*
- `to_code` *(string, required)*
- `from_vintage` *(string/year, required)*
- `to_vintage` *(string/year, required)*
- `weight` *(optional; float for proportion-based crosswalks)*
- `notes` *(optional)*

### 5) Immutability & versioning 🔒

- If upstream changes: **add a new vintage file**, don’t overwrite the old one.
- If you must patch: do it with a new file + clear metadata note (`notes:`) explaining why.

---

<a id="geoid--fips-cheat-sheet"></a>
## GEOID & FIPS cheat sheet 🧩

<details>
<summary><strong>Common patterns (most-used)</strong> 📌</summary>

- **State FIPS:** 2 digits  
  - Example (Kansas): `20`
- **County GEOID:** 5 digits = state(2) + county(3)  
  - Example: `20` + `001` → `20001`
- **Tract GEOID:** 11 digits = state(2) + county(3) + tract(6)
- **Block Group GEOID:** 12 digits = tract GEOID(11) + block group(1)
- **Block GEOID:** 15 digits = state(2) + county(3) + tract(6) + block(4)

✅ Rule of thumb: store as **zero-padded strings** and validate lengths.

</details>

<details>
<summary><strong>Practical gotchas</strong> 🧨</summary>

- Some sources provide `STATEFP`, `COUNTYFP`, `TRACTCE`, `BLKGRPCE`, `BLOCKCE` separately; you may need to concatenate.
- Tract codes sometimes appear with implied decimals in human docs—**stored as 6-digit strings** in most machine datasets.
- “County FIPS” alone is ambiguous without state (county codes repeat across states). Always keep state + county for joins.

</details>

---

<a id="usage-examples"></a>
## Usage examples 🧰

### Python (pandas) 🐍

```python
import pandas as pd

# Always load codes as strings
fips_state = pd.read_csv(
    "data/external/mappings/census/keys/geography/fips_state__2024.csv",
    dtype={"code": "string"},
)

df = pd.read_csv("some_census_extract.csv", dtype={"state_fips": "string"})

df = df.merge(
    fips_state.rename(columns={"code": "state_fips", "label": "state_name"}),
    on="state_fips",
    how="left",
)

# Quick sanity check: no missing joins
assert df["state_name"].notna().all()
```

### Build a county GEOID 🧱

```python
df["state_fips"] = df["state_fips"].str.zfill(2)
df["county_fips"] = df["county_fips"].str.zfill(3)
df["county_geoid"] = df["state_fips"] + df["county_fips"]
```

---

<a id="validation-checklist"></a>
## Validation checklist ✅

Before merging any new/updated key:

- [ ] Codes are strings (no integer coercion)
- [ ] Key column is **unique** (or uniqueness is explicitly not expected and explained)
- [ ] Zero padding is correct (length checks pass)
- [ ] No unexplained null labels/descriptions
- [ ] Sidecar metadata includes **source + retrieved_at + license**
- [ ] Crosswalks clearly indicate vintages (`from_vintage`, `to_vintage`)
- [ ] Any transformation is documented in `notes` (what changed, why, how)

> [!TIP]
> Add lightweight, deterministic validators (even a tiny script) that fail fast when a key file drifts. 🧪

---

<a id="updating--contributing-keys"></a>
## Updating / contributing keys 🔁

1. 🧭 Identify the authoritative source (and confirm license/usage terms).
2. 📥 Capture the source snapshot (or a checksum + URL reference) for provenance.
3. 🧼 Normalize into a small key file (CSV/YAML/JSON).
4. 🧾 Add the `.meta.yml` sidecar (required).
5. ✅ Run validations (length, uniqueness, and join sanity checks).
6. 🔀 Submit via PR with a clear description of:
   - what changed
   - which pipelines will be impacted
   - which vintages are involved

---

<a id="privacy--ethics"></a>
## Privacy & ethics 🔒

- This folder must remain **safe-to-publish**: aggregated, non-sensitive reference material only.
- Never include address-level or person-level identifiers.
- When keys relate to demographic categorization, document assumptions and be explicit about limitations. 🧭

---

<a id="glossary"></a>
## Glossary 📚

- **FIPS**: Federal Information Processing Standards codes (commonly used for states/counties).
- **GEOID**: Geographic identifier used by the Census Bureau (often a concatenation of component codes).
- **ACS**: American Community Survey (rolling survey estimates; differs from decennial census).
- **Crosswalk**: Mapping table translating IDs between geographies/vintages (sometimes weighted).

---

🧩 **Bottom line:** If it helps decode, standardize, or safely join Census data—put it here, version it, document it, and validate it. ✅

