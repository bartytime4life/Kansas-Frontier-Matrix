# 🧬 PROV Index

![badge](https://img.shields.io/badge/policy-provenance--first-2ea44f)
![badge](https://img.shields.io/badge/metadata-W3C%20PROV-1f6feb)
![badge](https://img.shields.io/badge/catalog-STAC%20%2B%20DCAT%20aligned-6f42c1)
![badge](https://img.shields.io/badge/status-generated%20artifacts-orange)

> ✅ **This folder is for *machine-generated* provenance indexes.**  
> ✍️ **Humans author PROV bundles** in `data/prov/`.  
> 🔒 **Governance rule:** if provenance is missing, the dataset should be treated as **not publishable**.

---

## 📌 What this folder is

`data/prov/index/` exists to make provenance **fast to discover and validate**.

- `data/prov/` contains the **source-of-truth** PROV lineage bundles (per dataset and/or per pipeline run).
- `data/prov/index/` contains **compiled indexes** that let downstream systems (Graph/API/UI/Focus Mode) answer questions like:
  - “What PROV bundle documents this dataset?”
  - “Which raw inputs produced this output?”
  - “Which pipeline run + parameters generated this artifact?”
  - “Which agent (person/software) produced it?”

> 🧠 Think of this as the “📇 card catalog” for provenance.

---

## 🧭 Quick links

- 📘 Master pipeline ordering: `../../../docs/MASTER_GUIDE_v13.md`
- 📏 PROV profile and rules: `../../../docs/standards/KFM_PROV_PROFILE.md`
- 🧾 Schemas (validation): `../../../schemas/prov/`

---

## 🗂️ Expected layout

```text
data/
└── prov/
    ├── 🧾 <dataset_id>.prov.json              # PROV lineage bundle (source-of-truth)
    ├── 🧾 <dataset_id>__<run_id>.prov.json    # Optional: run-scoped bundle
    └── index/
        ├── 📄 README.md                      # (this file)
        ├── 📄 prov.index.json                # Primary aggregated index (recommended)
        ├── 📄 prov.index.jsonl               # Optional: line-delimited index (stream-friendly)
        └── 🔐 checksums.sha256               # Optional: integrity snapshot
```

> 🧩 File names may evolve, but the **idea stays constant**:  
> **PROV bundles** live one folder up, and **indexes** live here.

---

## 🧱 Non‑negotiable invariants

These are repo-wide rules that *apply here too*:

1. **Pipeline ordering is absolute**  
   ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode  
   No stage should consume data that skipped a prior stage’s contract outputs.

2. **Provenance first**  
   A dataset or evidence artifact must have its PROV lineage recorded **before** it can be loaded into the graph or referenced by UI/narrative content.

3. **Deterministic, idempotent indexing**  
   Index generation should be:
   - repeatable (same inputs → same index)
   - stable (sorted keys, stable IDs)
   - safe to rerun (no side effects beyond updating index files)

4. **Sovereignty + classification propagation**  
   No derived artifact should be less restricted than its inputs. If sensitive inputs exist, index visibility must follow policy.

---

## 🧾 What a PROV bundle should capture

At minimum, PROV lineage should let us answer: **“How was this produced?”**

Typical components:
- **Entities**: inputs + outputs (file paths, URLs, hashes, stable IDs)
- **Activity**: the process (pipeline step name, timestamps, parameters, commit/run ID)
- **Agents**: who/what performed it (software agent + human operator, when applicable)

---

## 📇 Index record contract

This folder’s index files are **derived** summaries of the PROV bundles for fast lookup.

### ✅ Recommended minimal record shape

```json
{
  "dataset_id": "ks_hydrology_1880",
  "prov_path": "data/prov/ks_hydrology_1880.prov.json",
  "run_id": "2026-01-10T021500Z__a1b2c3d",
  "generated_at": "2026-01-10T02:16:03Z",

  "inputs": [
    {
      "uri": "data/raw/hydrology/noaa_rainfall_1880.csv",
      "sha256": "…",
      "role": "source"
    }
  ],
  "outputs": [
    {
      "uri": "data/processed/hydrology/ks_hydrology_1880.geojson",
      "sha256": "…",
      "role": "primary"
    }
  ],

  "agents": [
    { "type": "software", "id": "src/pipelines/hydrology/import_noaa.py", "version": "git:abc123" },
    { "type": "person", "id": "maintainer:team-kfm-data" }
  ],

  "links": {
    "stac_item": "data/stac/items/ks_hydrology_1880.json",
    "dcat": "data/catalog/dcat/ks_hydrology_1880.jsonld"
  },

  "governance": {
    "classification": "public",
    "license": "CC-BY-4.0"
  }
}
```

### 🧷 Notes on fields

- `dataset_id` should match the dataset identifiers used in catalogs/APIs.
- `prov_path` must be a stable repo-relative path.
- `run_id` should be stable and collision-resistant (timestamp + commit hash is common).
- `inputs[]` / `outputs[]` should carry **hashes** when possible.
- `links` provides cross-layer alignment with STAC/DCAT.
- `governance.classification` must respect the strictest input classification.

---

## 🔁 How to update this index

### 1) Add or update the PROV bundle first ✅
- Write/update the PROV file in `data/prov/…`
- Ensure it references:
  - raw inputs (`data/raw/...`)
  - intermediate steps (`data/work/...`) when relevant
  - final artifacts (`data/processed/...`)
  - agents + activity details (parameters, timestamps, run ID)

### 2) Regenerate the index files ♻️
Index generation should live under one canonical home (commonly `tools/` or `src/pipelines/`).

Typical patterns:
- `make prov-index`
- `python -m tools.prov.build_index`
- `python src/pipelines/_meta/build_prov_index.py`

> ⚠️ Do **not** hand-edit index outputs unless you’re debugging locally.  
> If you must patch, regenerate immediately after.

### 3) Validate before commit 🧪
- PROV bundles validate against `schemas/prov/`
- Index validates against its schema (if present)
- Cross-links resolve:
  - PROV ↔ STAC ↔ DCAT ↔ processed artifacts
- Hashes match the current files
- Classification rules are satisfied

---

## ✅ Validation checklist

- [ ] Every published dataset has a PROV bundle in `data/prov/`
- [ ] Every PROV bundle is referenced by **at least one** catalog record (STAC/DCAT)
- [ ] Index contains **no dangling paths**
- [ ] Index contains **no restricted data leakage**
- [ ] Index generation is deterministic (no random ordering / timestamps-only diffs)
- [ ] Any change in `data/prov/*.prov.json` triggers a corresponding index update

---

## 🆘 Troubleshooting

### “My dataset exists but isn’t discoverable”
- Confirm there is a PROV bundle in `data/prov/`
- Confirm the STAC/DCAT entries link to it
- Regenerate `data/prov/index/*` and re-run validation

### “Index shows a PROV file that doesn’t exist”
- You likely renamed/moved a PROV bundle without regenerating indexes
- Fix: restore the file path or regenerate the index

### “CI fails on provenance”
- Missing PROV bundle
- Broken cross-links (STAC/DCAT → PROV)
- Governance fields incomplete (license/classification)

---

## 🧠 Why this matters

KFM is built so that:
- every **data product** has lineage,
- every **story claim** traces back to evidence,
- every **derived artifact** can be reproduced or audited.

This folder helps keep that promise—at scale. 🌾🗺️✨