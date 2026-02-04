# 🗄️ `data/work/cache/` — Local Cache (Fast, Disposable, Helpful)

![Scope](https://img.shields.io/badge/scope-local%20%26%20ephemeral-blue)
![Durability](https://img.shields.io/badge/durability-disposable-important)
![Truth Path](https://img.shields.io/badge/kfm-truth%20path%20adjacent-lightgrey)
![Git](https://img.shields.io/badge/git-ignored%20(except%20README)-yellow)
![Safety](https://img.shields.io/badge/security-no%20secrets%20%F0%9F%9A%AB-red)

> [!IMPORTANT]
> This folder is a **performance cache**, not a dataset.  
> ✅ Safe to delete • ✅ Safe to rebuild • ❌ Not a source of truth

---

## 🎯 Why this folder exists

The Kansas Frontier Matrix system is designed around an evidence-first pipeline (Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI). This cache lives **beside** that “truth path” to speed up ingestion, transforms, search indexing, tile generation, and AI workflows — without undermining provenance.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Use it for:
- 📥 **Downloaded artifacts** you don’t want to re-fetch every run (HTTP/S3/API pulls)
- 🧪 **Intermediate outputs** (temporary conversions, resampling, clipping, joins, merges)
- 🧱 **Build caches** (tiles, embeddings, indexes, model weights) that can be reconstructed
- 🧰 **Tooling scratch space** (tmp files, partial results, retries, resumable jobs)

---

## ✅ What can live here

Typical cacheable artifacts (non-authoritative):

- 🌐 `http/` — downloaded files (zips, CSVs, GeoJSON, PDFs, imagery)
- 🗺️ `tiles/` — temporary tile build outputs (e.g., mbtiles/pmtiles staging)
- 🛰️ `rasters/` — clipped/resampled rasters, pre-COG staging
- 🧾 `vectors/` — intermediate vector outputs (GeoPackage/GeoJSON/Parquet staging)
- 🧠 `embeddings/` — vectorization cache (chunk files, interim indexes)
- 🔎 `search/` — full-text indexing scratch
- 🤖 `models/` — model download cache (if your workflow pulls weights)
- 🧷 `locks/` — file locks / job coordination
- 🧹 `tmp/` — throwaway scratch

> [!TIP]
> If a file is expensive to recompute but **still reproducible**, it belongs here.

---

## 🚫 What must NOT live here

These belong in **Raw / Processed / Catalog / DB / Assets**, not cache:

- ❌ **Authoritative datasets** (anything you’d cite or publish)
- ❌ **Final derivatives** meant for users (final COGs, final PMTiles, final exports)
- ❌ **Provenance records** intended as permanent lineage artifacts
- ❌ **Secrets** (tokens, keys, cookies, `.env`, credentials)
- ❌ **Sensitive/regulated data** (PII, restricted documents, private logs)

> [!WARNING]
> If the UI/API could ever serve it directly, it probably doesn’t belong in `cache/`.

---

## 🧭 Relationship to the KFM “Truth Path”

KFM enforces a governed data flow: **Raw ➜ Processed ➜ Catalog ➜ Databases ➜ API ➜ UI/AI**.  
This cache must never become a shortcut around that order.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Rule of thumb:**  
🟩 Cache = speed  
🟦 Processed/Catalog = truth  
🟥 Cache must not masquerade as truth

---

## 🗂️ Recommended layout

<details>
<summary><strong>📁 Suggested directory tree</strong> (click to expand)</summary>

```text
data/
  work/
    cache/
      README.md
      manifest/
        cache_index.json
      http/
        by_urlhash/
      tiles/
        staging/
      rasters/
        staging/
      vectors/
        staging/
      embeddings/
        staging/
      search/
        staging/
      locks/
      tmp/
```

</details>

---

## 🔑 Cache keys & filenames (be boring on purpose)

To avoid collisions and to make caches stable across runs:

### ✅ Prefer content-addressed or deterministic keys
- `sha256/<first2>/<fullhash>/artifact.ext`
- `by_urlhash/<sha256(url)>/…`

This mirrors a “strongly cacheable filename” approach where a **hash-based name** represents content identity.  [oai_citation:2‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

### ✅ Keep metadata close (sidecar)
For any cached artifact `X.ext`, add one:
- `X.ext.meta.json` (or `.jsonld`)

Suggested fields:
- `source_url` / `source_id`
- `fetched_at`
- `license` (if known)
- `sha256`
- `etag` / `last_modified` (if available)
- `pipeline_step` (who produced it)
- `params` (bbox/time range/resolution/etc.)

> [!NOTE]
> Metadata here is **for reproducibility + debugging**, not permanent lineage. Permanent lineage belongs in the governed provenance/catlog layers.

---

## 🧺 Retention & eviction

Caches can grow forever unless you enforce rules.

### ✅ Recommended policy
- ⏳ TTL-based cleanup (e.g., delete anything not accessed in N days)
- 🧠 LRU eviction for bounded caches (tiles/embeddings/search)
- 🪟 “Window caching” for intermediate results (keep only the most recent set of runs)

This mirrors common practice where intermediate results are cached for a limited window and evicted when full.  [oai_citation:3‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)

### ✅ Simple, human-friendly convention
- Put run-specific scratch under: `tmp/run-YYYYMMDD-HHMMSS/`
- Put job outputs under: `tmp/job-<jobid>/`
- Always safe to delete `tmp/`

---

## 🔒 Safety & governance expectations

Even though this is “just cache,” it still touches real-world data.

- 🔐 **No secrets**: never write tokens/keys here
- 🧾 **Respect licenses**: cache doesn’t change licensing obligations
- 🧯 **Avoid sensitive data**: if in doubt, treat as restricted
- 🧼 **Sanitize logs**: don’t dump raw records containing PII into cache logs
- 🧰 **Prefer compressed + open formats** for large intermediates (COG/Parquet/GeoPackage where applicable)

---

## 🧾 Git hygiene

This directory should be **ignored**, except this README.

### ✅ Suggested `.gitignore` snippet
```gitignore
# 🗄️ cache is disposable — do not commit it
data/work/cache/*
!data/work/cache/README.md
```

> [!TIP]
> For Docker builds, also add `data/work/cache` to `.dockerignore` to reduce build context bloat.

---

## 🧪 “Cache contract” for pipeline authors

If your script/job writes here, it must:
1. ✅ Be safe to rerun (idempotent or clearly keyed)
2. ✅ Never treat cache contents as canonical truth
3. ✅ Include enough metadata to reproduce (inputs + parameters)
4. ✅ Fail gracefully if cache is missing/corrupt (rebuild instead of crash)
5. ✅ Use locks for multi-worker writes (see `locks/`)

---

## 🧯 Troubleshooting

- 💽 **Disk full**: wipe `tmp/` first, then old `tiles/` or `embeddings/`
- 🧩 **Corrupt cache**: delete the specific hash-bucket and rerun
- 🧵 **Parallel jobs collide**: add file locks and write to temp then atomic rename
- 🐢 **Slow rebuilds**: ensure URL hashing + sidecar metadata is stable across runs

---

## 📚 Sources & inspiration

- Kansas Frontier Matrix architecture & governed “truth path” concepts.  [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Hash-based caching / strongly cacheable filenames patterns for static assets.  [oai_citation:5‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)
- Cache windowing + eviction for intermediate results (general systems principle).  [oai_citation:6‡Scalable Data Management for Future Hardware.pdf](sediment://file_000000007d74722fa87beabc663630f7)