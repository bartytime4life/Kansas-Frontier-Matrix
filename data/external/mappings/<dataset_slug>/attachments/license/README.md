# 📜 Attachments License Pack — `<dataset_slug>` (External Mappings)

![Scope](https://img.shields.io/badge/scope-attachments%20%2F%20license-blue)
![Data](https://img.shields.io/badge/data-external%20mappings-informational)
![Policy](https://img.shields.io/badge/policy-evidence--backed%20rights-critical)

> [!IMPORTANT]
> **Every file in `../` (the dataset’s `attachments/` folder) must have explicit, evidence-backed rights info before it’s considered usable, publishable, or redistributable.**  
> If we can’t prove the rights, we **don’t ship it**. ✅

---

## 🎯 What this folder is

This folder is the **rights + licensing “source-of-truth”** for all third‑party or externally-sourced **attachment files** associated with:

📁 `data/external/mappings/<dataset_slug>/attachments/`

Examples of “attachments” (varies by dataset):

- 🗺️ scanned map sheets (TIFF/JPG/PDF)
- 🧾 legends, gazetteers, index pages
- 🧩 reference shapefiles / GeoJSON from external providers
- 🧠 methodological PDFs or metadata exports
- 📸 photos / imagery used as a reference layer

---

## ✅ TL;DR checklist (the non-negotiables)

- [ ] **Every attachment has a rights record** (machine‑readable preferred)  
- [ ] **Every rights record has evidence** (screenshot/PDF/email/terms page copy)  
- [ ] **Attribution is written** (copy/paste ready)  
- [ ] **Restrictions are explicit** (or explicitly “none known”)  
- [ ] **Redistribution status is clear** (allowed / not allowed / unclear → block)

> [!TIP]
> Treat this like provenance: if it isn’t documented, it didn’t happen. 🧾🧠

---

## 🧱 Recommended structure (inside this folder)

You can keep this lightweight, but this structure scales well:

```text
📁 attachments/
  ├─ 📁 license/
  │  ├─ 📄 README.md                         👈 you are here
  │  ├─ 📁 evidence/                         📸 “proof” files (screenshots, PDFs, emails)
  │  ├─ 📁 texts/                            📜 full license texts (when applicable)
  │  ├─ 📁 records/                          🧾 per-attachment license records (YAML/JSON)
  │  └─ 📄 LICENSE_INDEX.md                  🗂 human-friendly index (optional)
  └─ 📄 <your attachment files live here>    🗺️🗃️
```

---

## 🧾 How to document rights for an attachment

### Option A (preferred) — One record per file (YAML)

Create a file under:

📁 `records/`

Named like:

- `records/<attachment_filename>.license.yml`
- or `records/<attachment_basename>--<source_key>.license.yml`

**Template (copy/paste):**

```yaml
# records/<attachment_filename>.license.yml
schema: kfm.attachments.license.v1

attachment:
  path: "../<attachment_filename>"   # relative to THIS README location
  sha256: "<optional-but-recommended>"
  description: "<what is this file?>"

source:
  name: "<provider / archive / author>"
  url: "<canonical landing page or download URL>"
  retrieved_at: "YYYY-MM-DD"
  local_evidence:
    - "../license/evidence/<file-or-screenshot>"

license:
  spdx: "<e.g., CC-BY-4.0 | CC-BY-SA-4.0 | CC0-1.0 | Public-Domain | LicenseRef-Unknown>"
  name: "<human readable license name>"
  url: "<license URL if available>"
  text_file: "../license/texts/<license-text>.txt"   # if you store full text locally
  redistribution:
    allowed: true            # true | false | unknown
    notes: "<explain any limits>"

attribution:
  required: true
  statement: >
    "<copy/paste attribution string exactly as required by the licensor>"
  preferred_citation: "<optional: formal citation>"

restrictions:
  - "<e.g., non-commercial only, no-derivatives, share-alike, etc.>"
  - "<or: 'none stated'>"

derivatives:
  # Document any transformations we performed (georeferencing, cropping, tiling, etc.)
  - type: "georeferencing"
    tool: "<QGIS | GDAL | ArcGIS | custom>"
    date: "YYYY-MM-DD"
    notes: "<what changed?>"

review:
  status: "approved"         # draft | needs-review | approved | blocked
  reviewer: "<name/handle>"
  reviewed_at: "YYYY-MM-DD"

notes: "<anything else important>"
```

> [!NOTE]
> If a source provides **a custom Terms of Use**, capture it as **evidence** even if you also record an SPDX license.

---

### Option B — Group record (many files share the same rights)

If multiple attachments share the exact same license + source terms:

✅ Create one record such as:

- `records/_bundle--<source_key>.license.yml`

Then list the covered files:

```yaml
schema: kfm.attachments.license.v1

bundle:
  name: "<source_key>"
  covered_paths:
    - "../sheet_001.tif"
    - "../sheet_002.tif"
    - "../legend.pdf"

source:
  name: "<provider>"
  url: "<landing page>"
  retrieved_at: "YYYY-MM-DD"
  local_evidence:
    - "../license/evidence/<terms-screenshot-or-pdf>"

license:
  spdx: "<...>"
  redistribution:
    allowed: true
```

---

## 📸 What counts as “evidence”?

Store evidence under:

📁 `evidence/`

Examples:

- 🖼️ screenshot of the webpage showing license/terms (include date captured)
- 📄 PDF of “Terms of Use”
- ✉️ email granting permission (save as PDF or EML if possible)
- 🧾 scanned letter or memorandum
- 🗃️ archive catalog entry page (if it contains rights statements)

**Naming suggestions:**

- `evidence/<source_key>--license-terms--YYYY-MM-DD.png`
- `evidence/<source_key>--permission-email--YYYY-MM-DD.pdf`

---

## 🧩 Attribution rules (practical)

### 1) Put the *exact* attribution text in the record  
Because the UI / exports may need to render it consistently.

### 2) If attribution differs by file, store it per file  
If it’s identical for a bundle, store once.

### 3) If attribution is unclear → mark as blocked  
No guessing. No “probably public domain.” 🚫

---

## 🚧 If the license is unknown or restrictive

> [!WARNING]
> If redistribution is **unknown** or **not allowed**, the attachment should be treated as **BLOCKED** for public builds.

Recommended approach:

- Keep the file out of the dataset (ideal) **or**
- Store it locally only (outside version control) **or**
- Keep it in repo only if the project policy allows it **and** it is access‑restricted (and clearly marked)

Minimum record values in that case:

- `license.spdx: LicenseRef-Unknown`
- `license.redistribution.allowed: unknown`
- `review.status: blocked`

---

## 🔍 Quick QA (before PR / merge)

Run this mental check:

- [ ] Can a reviewer answer: **“Where did this file come from?”**
- [ ] Can a reviewer answer: **“Can we legally redistribute it?”**
- [ ] Can a reviewer answer: **“What attribution is required?”**
- [ ] Can a reviewer answer: **“What did we change (if anything)?”**
- [ ] Is there **evidence** stored locally, not just a link?

---

## 🧠 FAQ

<details>
  <summary><strong>Do we store the full license text?</strong></summary>

If the license is standardized (e.g., Creative Commons), a URL is often enough.  
If the license is **custom**, **store it** (PDF, HTML snapshot, or text) and reference it from the record.

</details>

<details>
  <summary><strong>What if the attachment is our own work?</strong></summary>

Still document it.  
Set `source.name` to the project/team and use the dataset’s intended license.  
This avoids ambiguity later.

</details>

<details>
  <summary><strong>What about derived outputs (georeferenced rasters, digitized vectors)?</strong></summary>

Document both:

- the **upstream rights** (original scan / base layer)
- the **transformation** performed (what we changed + tools)

If upstream prohibits derivatives, **do not create/ship derivative outputs**.

</details>

---

## ⚖️ Legal note (friendly but firm)

This repo stores **documentation** about rights and licensing.  
It is **not legal advice**. If something is unclear, mark it **blocked** and escalate for review. 🧑‍⚖️✅
