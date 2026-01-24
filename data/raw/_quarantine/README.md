# 🧪📥 `data/raw/_quarantine/` — The “Hold My Beer” Zone (Untrusted Data Staging)

![Status](https://img.shields.io/badge/status-active-informational)
![Scope](https://img.shields.io/badge/scope-data%2Fraw%2F_quarantine-blue)
![Trust](https://img.shields.io/badge/trust-untrusted-critical)
![Rule](https://img.shields.io/badge/rule-fail--closed-black)

Welcome to **Quarantine** — the **pre-trust** landing area for anything that is **new, unknown, messy, sensitive, or suspicious**.  
If you’re not 100% sure a file is safe + legal + properly documented… it belongs **here first**. 🧯

> ✅ **Key idea:** `data/raw/` is KFM’s **first trust boundary** (immutable evidence).  
> 🛑 `_quarantine/` is **before** that boundary — treat everything here as **hostile** until proven otherwise.

---

## 🎯 What this folder is for

Use `_quarantine/` when you have **any** of these:

- 🧾 **Unknown license / unclear usage rights**
- 🧬 **Possible PII / sensitive cultural info / restricted sites**
- 🧩 **Incomplete dataset** (missing sidecars like `.prj`, README, schema, etc.)
- 🦠 **Potentially unsafe files** (macros, executables, weird archives)
- 🗺️ **Geospatial mystery meat** (unknown CRS, broken geometry, missing metadata)
- 📚 **Bulk document drops** (PDF scans, images of text, archival blobs) pending OCR + entity extraction
- 🧪 **Experimental / “maybe useful later”** assets (3D models, AR overlays, odd formats)

---

## 🚫 What this folder is *not* for

- ❌ Anything already approved + documented (that should go to `data/raw/…`)
- ❌ Processed outputs (those belong in `data/processed/…`)
- ❌ “Just run it and see” code (no scripts, binaries, installers, macros)
- ❌ Secrets (tokens, keys, passwords), internal-only docs, or private dumps
- ❌ Anything you wouldn’t want mirrored publicly

---

## 🧱 Threat model (yes, we’re serious 😅)

Treat quarantined inputs as:

- 🔥 **Malicious until proven otherwise**
- 🧨 **Legal risk until license is confirmed**
- 🕵️ **Privacy risk until sensitivity is classified**
- 🧩 **Semantically unreliable** until validated (schema, CRS, provenance)

**Golden rule:**  
> If it can execute, call out, phone home, or embed macros… **don’t open it casually**.

---

## 🗂️ Recommended layout (clean, predictable, reviewable)

```text
data/raw/_quarantine/
├─ ✅📄 README.md                     # 👈 you are here 📌 Quarantine rules: why items land here, triage workflow, promotion gates
└─ 🧪 <dataset_slug>/                 # One quarantined dataset (unknown quality/terms until triaged)
   └─ 🏷️ <ingest_YYYYMMDDThhmmssZ>/   # One intake drop (UTC timestamp; immutable once recorded)
      ├─ 📦 payload/                  # The actual received files (zips, pdfs, shapefiles, etc.) — do not edit in place
      ├─ 🧾 source.json               # REQUIRED: origin, retrieval method, license/terms, contacts, sensitivity hints
      ├─ 🔐📄 checksums.sha256         # REQUIRED: sha256 hashes for payload + metadata (tamper evidence)
      ├─ 🩺📄 triage.md                # REQUIRED: what it is, risks, missing info, and initial classification/next actions
      ├─ 🧭📄 promote_plan.md          # Optional: plan to promote into a governed pipeline (steps, owners, target paths)
      └─ 📎 attachments/              # Optional: supporting proof (screenshots, emails, permission letters; keep access-safe)
```

### ✅ Dataset slug conventions
- Use **lowercase kebab-case**: `kdot-traffic-counts`, `usgs-nwis-gauges`, `historic-maps-topeka`
- Avoid spaces, avoid “final”, avoid “new2”, avoid vibes 😄

---

## 📎 Required sidecar files (minimum “receipt pack”)

### 1) `source.json` ✅
This is your provenance “receipt”. Keep it factual and specific.

**Suggested schema (minimal):**
```json
{
  "dataset_id": "kfm.quarantine.<slug>",
  "title": "Human readable title",
  "retrieved_at": "2026-01-24T00:00:00Z",
  "retrieved_by": "name_or_handle",
  "source_type": "url|email|drive|scan|manual",
  "source_url": "https://example.com/file.zip",
  "license": "UNKNOWN|CC-BY-4.0|ODbL|Public-Domain|Custom",
  "sensitivity": "public|internal|restricted|tribal_sensitive|pii_possible",
  "care_label": "Public|Restricted · Tribal Sensitive|TBD",
  "notes": "What we know / don't know yet",
  "intended_destination": "data/sources/ + pipeline OR data/raw/<domain>/..."
}
```

### 2) `checksums.sha256` ✅
Generate checksums for **every file** in `payload/`.

```bash
cd payload
sha256sum * > ../checksums.sha256
```

### 3) `triage.md` ✅
A human-readable triage note (short, decisive). Suggested template:

```md
## Triage Summary
- What is it?
- Why do we want it?
- What’s missing (license, CRS, schema, etc.)?
- Risks (PII, sacred sites, restricted license, malware, etc.)
- Next action: Reject / Redact / Request permission / Promote
```

---

## 🔁 Promotion workflow (Quarantine ➜ Trusted KFM data)

> Promotion means: **moving across the trust boundary** into KFM’s governed intake pipeline.

### ✅ Step 0 — Decide: should this be stored at all?
- If license is unknown and cannot be clarified: **do not promote**.
- If sensitive and cannot be responsibly generalized/controlled: **do not promote**.
- If it’s huge: prefer **manifest-based fetching** (see `data/sources/` patterns) instead of committing raw bytes.

### ✅ Step 1 — Run quick “ingestion gate” checks (lite)
Checklist:
- [ ] Virus/macro risk assessed (don’t run unknown executables)
- [ ] File opens *safely* (no macros, no scripts)
- [ ] Checksums computed
- [ ] Basic format sanity (parseable CSV/JSON; shapefile has all components)
- [ ] License identified and recorded
- [ ] Sensitivity + CARE label assigned
- [ ] Source URL / citation captured

### ✅ Step 2 — Create the proper intake path
Most KFM sources should be represented as:
- `data/sources/<something>.json|yml` (manifest) 🧾  
…and then fetched deterministically by pipeline code/config.

**Only** put raw bytes into `data/raw/…` when that’s the agreed storage strategy.

### ✅ Step 3 — Promote to `data/raw/…` (immutable evidence)
When approved:
- Move payload into the correct `data/raw/<domain>/<dataset>/...` path
- Keep raw bytes **unchanged** (“as received”)
- Ensure downstream transforms happen only in `data/work/` or `data/processed/`

### ✅ Step 4 — Wire into deterministic ETL
- Add/adjust ingestion config
- Produce standard metadata outputs (catalog + provenance)
- Ensure any AI-extracted metadata is labeled and reviewable 👀🤖

---

## 🛡️ Sensitive data rules (FAIR + CARE + common sense)

If the content includes any of the following:
- 🧍 living persons (PII)
- 🏺 precise locations of artifacts / cultural sites
- 🦅 endangered species habitats
- 🪶 tribal / sacred / community-controlled knowledge

Then:
- **Do not** publish exact coordinates
- Use **generalization** (hex bins, coarse polygons, county level, etc.)
- Prefer **access control** or **private storage** over “oops it’s public now”
- Require explicit permission where appropriate ✅

> 🧠 Remember: repeated releases over time can leak details (temporal inference).  
> “Safe once” doesn’t always mean “safe forever”.

---

## 🧰 Handy triage commands (safe-ish)

### Identify file types quickly
```bash
file payload/*
```

### PDF sanity check
```bash
pdfinfo payload/*.pdf
```

### Geospatial sanity checks (CRS / components)
```bash
# Shapefile: ensure .shp .shx .dbf .prj exist
ls payload/*.shp payload/*.shx payload/*.dbf payload/*.prj

# If you have GDAL installed:
gdalinfo payload/*.tif
ogrinfo -so payload/*.shp
```

---

## 🧹 Cleanup policy (keep quarantine from turning into a junk drawer)

- 🧼 **Target TTL:** 30–90 days
- 🧭 If it’s not being promoted, it should be:
  - ✅ rejected (with a note why), or
  - ✅ moved to an archive bucket, or
  - ✅ converted into a `data/sources/` manifest + pipeline plan

> 🧯 Quarantine is a staging area, not a permanent home.

---

## ✅ Definition of Done (for promotion PRs)

- [ ] `source.json` complete (license + sensitivity + provenance)
- [ ] `checksums.sha256` present and matches payload
- [ ] `triage.md` explains what/why/risks/next step
- [ ] Any required permission letters are included (or referenced)
- [ ] Policy gates pass (license present, provenance present, sensitive handling ok)
- [ ] Promotion results in deterministic, reproducible pipeline behavior
- [ ] No raw bytes were modified in place after becoming “trusted evidence”

---

## 🔗 Related KFM concepts (why this exists)

- 📥 **Immutability & trust boundaries** (raw data as evidence)
- 🧾 **Provenance-first** ingestion (receipts, manifests, lineage)
- 🧠 **Human-in-the-loop** AI assistance (OCR/entity extraction is helpful, not authoritative)
- 🧰 **Policy-as-code gates** (fail closed; prevent accidental publishing)
- 🗺️ **UI/AI transparency** (citations + warnings for sensitive layers)

---

## ❓FAQ

### “Can the pipeline read from `_quarantine/`?”
**No.** If it does, that’s a bug. Quarantine is explicitly **outside** the trusted intake path.

### “Can I rename files in quarantine?”
Yes (it’s still untrusted), but once promoted to `data/raw/…`, treat filenames as part of the evidence record.

### “What about zips?”
Prefer keeping the original zip **and** an extracted copy only if needed for inspection. Always checksum both.

### “Where do I put emails / permission letters?”
Put them in `attachments/` (or link to them from `source.json`), and summarize in `triage.md`.

---
🧠✨ If you’re unsure: **quarantine first, ask questions second, promote last**.

