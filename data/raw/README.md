# 📥 `data/raw/` — Immutable Raw Data

![zone](https://img.shields.io/badge/data_zone-raw-blue)
![contract](https://img.shields.io/badge/contract-write_once%2Fread_only-important)
![truth_path](https://img.shields.io/badge/truth_path-raw%E2%86%92work%E2%86%92processed-success)

`data/raw/` is KFM’s **evidence vault**: the unmodified, source-level snapshots we can always trace back to.

> [!IMPORTANT]
> **Raw is write-once.** Pipelines may **read** from `data/raw/`, but must **never modify** raw artifacts in place.

---

## ✅ What belongs here

| Type | Examples |
|---|---|
| Upstream snapshots (as acquired) | ZIPs of shapefiles, CSV exports, API snapshot JSON, etc. |
| Original media / artifacts | PDFs, scans, images, transcripts, etc. |
| Provider-delivered structure | Unzipped archive folder structures (preserve original filenames). |

---

## 🚫 What does *not* belong here

| Don’t put this in `raw/` | Put it here instead | Why |
|---|---|---|
| Cleaned/normalized/intermediate outputs | `../work/` | Work is reproducible scratch space. |
| Publishable datasets / canonical outputs | `../processed/` | Processed is the “serves truth” zone. |
| Manually edited “fixed” source files | `../work/` (then automate) | Raw must remain verbatim evidence. |
| Secrets (API keys, tokens) | Secret manager / vault | Never commit secrets. |

---

## 📁 Recommended directory layout

Raw may be organized by **source** or **topic/domain**. Keep it predictable and boring.

```text
data/raw/
  <source_or_topic>/
    <dataset_slug>/
      <acquired_YYYY-MM-DD>__<upstream_id_or_spec_hash>/   # snapshot folder (recommended)
        manifest.json          # deterministic manifest (recommended name)
        checksums.sha256       # deterministic checksums (recommended name)
        <original_files...>
```

Examples (illustrative):

- `data/raw/usgs_water/`
- `data/raw/historical_maps/1930_county_map.pdf`

> [!TIP]
> If the upstream ships a ZIP, it’s okay to **unzip into raw** as long as you preserve original filenames and keep files unmodified.

<details>
<summary><strong>Why snapshot folders?</strong></summary>

Snapshot folders make it easy to:
- keep multiple acquisitions side-by-side (e.g., annual/quarterly releases),
- avoid overwriting evidence,
- reference a specific snapshot in provenance and citations.

</details>

---

## 🧾 Manifests & checksums

Each acquisition should include **a deterministic manifest and checksums** stored alongside the raw files.

Minimum expectations:
- deterministic listing of files (names + sizes; MIME types optional),
- deterministic per-file checksums (e.g., SHA-256),
- enough acquisition metadata to recreate the fetch (source URL/query/params, acquisition time, etc.).

> [!NOTE]
> Filenames (`manifest.json`, `checksums.sha256`) are **conventions**. If the repo already standardizes these names/formats, follow the existing standard.

---

## 🧠 Raw → Work → Processed (the “truth path”)

Raw is only the start. KFM’s governed lifecycle prevents “intermediates becoming truth”.

```mermaid
flowchart LR
  RAW[Raw: immutable evidence] --> WORK[Work: reproducible intermediates]
  WORK -->|promotion gate + receipts| PROC[Processed: publishable artifacts]
  PROC --> CATS[Catalogs: DCAT / STAC / PROV]
  CATS --> API[Governed API (policy boundary)]
  API --> UI[UI / Focus Mode]
```

> [!IMPORTANT]
> Promotion is expected to be **fail-closed**: no “manual promotion” without required receipts, checksums, and catalogs.

---

## 🩹 Corrections, replacements, and “bad raw”

If a raw data error is discovered:

1. Prefer adding a **new snapshot folder** with corrected upstream content.
2. If you must replace files, ensure the old version remains recoverable (Git history or retained snapshot).
3. Record the reason (e.g., in an `ABOUT.md` note in the dataset folder *or* embedded in manifest metadata).

> [!WARNING]
> Never “patch” raw evidence by hand-editing values in-place. If interpretation needs fixing, do it in `work/` and let the pipeline produce corrected `processed/` outputs.

---

## 🔒 Sensitivity & restrictions

Raw may include sensitive inputs (e.g., ownership/PII, precise sensitive locations). Even though raw is not served directly:

- keep sensitive raw datasets clearly isolated (folder naming + manifest metadata),
- ensure downstream pipelines apply redaction and policy labeling before promotion,
- for extremely large products (e.g., satellite imagery), prefer storing **metadata + pointers** rather than full mirrors when rehosting is infeasible.

---

## ✅ Checklist: adding new raw data

- [ ] Create/choose an appropriate `<source_or_topic>/<dataset_slug>/` folder.
- [ ] Add the **unmodified** upstream artifacts.
- [ ] Add **deterministic** `manifest` + `checksums`.
- [ ] Capture minimal acquisition context (where it came from, when, license/terms).
- [ ] Open a PR; promotion to `processed/` should include catalog/provenance updates.

---

## 🔎 FAQ

**Can pipelines write into `data/raw/`?**  
No. Pipelines read raw; they write intermediates to `work/` and publishables to `processed/`.

**Where do I put “cleaned CSVs”?**  
`../work/` (and only as pipeline outputs).

**Is `data/raw/` part of the reproducibility contract?**  
Yes: preserving raw snapshots enables re-processing years later and supports traceable evidence.

---

## 📚 References (internal)

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint** — “Data Storage & Metadata Management”
- **KFM Comprehensive Data Source Integration Blueprint v1.0 (2026-02-12)** — promotion gates + manifests/checksums