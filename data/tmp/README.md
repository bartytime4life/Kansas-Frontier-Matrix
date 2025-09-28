# `data/tmp/` — Ephemeral Temporary Files

This folder is reserved for **purely transient artifacts**:
files created during builds, tests, or experiments that **do not
belong in version control** and can be safely deleted at any time.

---

## Purpose

- Provide a scratchpad for scripts and pipelines that need
  a writable directory.
- Hold downloads, unzipped archives, or intermediate exports
  that will be discarded after use.
- Prevent clutter in canonical directories (`sources/`, `cogs/`, `derivatives/`).

---

## Rules

- 🚫 **Never commit files in `tmp/`**.  
  `.gitignore` excludes this directory by default.
- ✅ If a temporary file proves valuable or reproducible, **promote it**:
  - to `data/work/` (if it is an intermediate worth tracking briefly),
  - to `data/processed/` or `data/derivatives/` (if analysis-ready),
  - or to `data/sources/` (if it is a canonical input).
- 🧹 Safe to delete at any time — pipelines and scripts should
  regenerate anything needed here.

---

## Typical Contents

- Temporary raster/vector conversions before COG/GeoJSON promotion.
- Cache files from fetch scripts or API queries.
- Test exports, zipped archives, or partial OCR text dumps.
- Large scratch files that should not pollute the repo.

---

## Connections

This folder is the **lowest rung** of the data lifecycle:

```

tmp/  →  work/  →  processed/ | cogs/  →  derivatives/  →  stac/

```

- `tmp/` = ephemeral, auto-ignored, wipeable.  
- `work/` = semi-scratch, tracked if reproducibility is useful.  
- `processed/` & `cogs/` = validated, stable inputs.  
- `derivatives/` = reproducible analysis outputs.  
- `stac/` = catalog + metadata for discovery.

---

✦ **Summary:** Use `data/tmp/` for anything you don’t want to keep.
If it matters, promote it. If not, let it vanish.
```
