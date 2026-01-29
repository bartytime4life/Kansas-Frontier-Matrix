---
title: "📸 Screenshots Index — External Mapping: <dataset_slug>"
path: "data/external/mappings/<dataset_slug>/attachments/screenshots/index.md"
version: "v0.1.0"
last_updated: "2026-01-29"
status: "draft" # draft | active | deprecated
doc_kind: "EvidenceIndex"
license: "CC-BY-4.0" # applies to this index.md text; screenshots may have different rights—see manifest
dataset_slug: "<dataset_slug>"
source_kind: "external"
timezone: "America/Chicago"

# Governance & policy refs (repo-local)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"

# Content classification (defaults — adjust per dataset)
sensitivity: "TBD"     # public | internal | restricted
classification: "TBD"  # open | controlled | confidential

doc_uuid: "urn:kfm:doc:evidence:screenshots:<dataset_slug>:v0.1.0"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# 📸 Screenshots — `<dataset_slug>`

![Evidence](https://img.shields.io/badge/evidence-screenshots-6f42c1)
![Area](https://img.shields.io/badge/area-mappings%20%2F%20attachments-0ea5e9)
![Status](https://img.shields.io/badge/status-draft-f59e0b)
![Last%20Updated](https://img.shields.io/badge/last%20updated-2026--01--29-64748b)

> [!NOTE]
> This folder is a **governed evidence attachment** area for the dataset mapping `<dataset_slug>`.  
> Screenshots here should **support a specific mapping decision** (source verification, license proof, download workflow, field dictionary, portal filters, etc.).

---

## 🧭 Quick Links

- ⬆️ Dataset mapping root: `../../`  
- 🧾 Mapping index (recommended): `../../index.md` *(if present)*  
- 🗺️ Mapping notes (recommended): `../../mapping.md` *(if present)*  
- 📄 Other attachments: `../`  
- 🧠 Repo standards & governance:
  - `docs/MASTER_GUIDE_v13.md`
  - `docs/standards/KFM_DCAT_PROFILE.md`
  - `docs/standards/KFM_STAC_PROFILE.md`
  - `docs/standards/KFM_PROV_PROFILE.md`

---

## 📦 Folder Layout

```text
data/external/mappings/<dataset_slug>/
├─ index.md                         👈 dataset-level mapping overview (recommended)
├─ mapping.md                       👈 mapping notes + decisions (recommended)
└─ attachments/
   └─ screenshots/
      ├─ index.md                   👈 you are here
      ├─ SS-001__YYYY-MM-DD__...png
      └─ ...
```

---

## 🎯 Scope

| ✅ In Scope (put here) | ❌ Out of Scope (put elsewhere) |
|---|---|
| Source portal landing pages | Raw datasets / downloads (use `data/raw/...`) |
| License / terms / citation pages | Processed outputs (use `data/processed/...`) |
| Data dictionary / schema tables | Story media intended for UI/narratives (use `docs/reports/story_nodes/...`) |
| Filters/search steps used to extract a subset | Secrets, tokens, passwords (never commit) |
| QA evidence (e.g., “this field exists”, “this endpoint returns X”) | Anything that violates source terms or repo governance |

---

## 🧾 Screenshot Manifest

> [!TIP]
> Keep this table **current**. Treat it like a mini “evidence ledger” for mapping work.  
> Every screenshot should be referenced from **at least one** mapping doc section (or a PR discussion).

| ID | File | What it shows | Source / URL | Captured (local) | Captured by | Related mapping section | Redaction? | Notes (license/terms, quirks) | Hash (sha256) |
|---:|---|---|---|---|---|---|---|---|---|
| SS-001 | `SS-001__YYYY-MM-DD__source-landing.png` | Landing page + dataset title | `https://…` | YYYY-MM-DD HH:MM | @handle | `../../mapping.md#source` | none | Confirms official dataset name | `sha256:…` |
| SS-002 | `SS-002__YYYY-MM-DD__license.png` | License/terms page | `https://…` | YYYY-MM-DD HH:MM | @handle | `../../mapping.md#license` | none | Used to set DCAT license field | `sha256:…` |
| SS-003 | `SS-003__YYYY-MM-DD__data-dictionary.png` | Field list / schema | `https://…` | YYYY-MM-DD HH:MM | @handle | `../../mapping.md#schema` | ✅ yes | Redacted user account email in header | `sha256:…` |

---

## 🖼️ Gallery

> [!NOTE]
> GitHub renders images inline. Use **clear alt text** and (optionally) a short caption.

<!--
Copy/paste template per screenshot. Keep 3–10 “most important” screenshots in the gallery;
leave the rest only in the manifest to avoid making this page too heavy.
-->

<details>
  <summary><strong>SS-001 — Source landing page</strong></summary>

  ![SS-001 — Source landing page](SS-001__YYYY-MM-DD__source-landing.png)

  *Caption:* Landing page used to confirm dataset name + publisher.  
  *Source:* https://…  
  *Captured:* YYYY-MM-DD HH:MM (America/Chicago)
</details>

<details>
  <summary><strong>SS-002 — License / terms</strong></summary>

  ![SS-002 — License / terms](SS-002__YYYY-MM-DD__license.png)

  *Caption:* License/terms screenshot used to populate DCAT license + attribution.  
  *Source:* https://…  
  *Captured:* YYYY-MM-DD HH:MM (America/Chicago)
</details>

---

## 🧰 Capture Standards

### 🏷️ Naming Convention

**Required format (recommended):**
`SS-###__YYYY-MM-DD__short-topic__v01.png`

Examples:
- `SS-004__2026-01-29__download-workflow__v01.png`
- `SS-005__2026-01-29__api-endpoint-response__v01.png`

Rules:
- ✅ Use **leading zeros** (`SS-001`, `SS-010`, `SS-100`)
- ✅ Use `kebab-case` for the topic
- ❌ No spaces, no `final_final.png`, no ambiguous `image1.png`

### 🖼️ Image Quality & Size

- Prefer **PNG** for UI/text-heavy captures; **JPG** for photo-like images
- Keep files “repo-friendly” (compress if needed)
- Always include **alt text** in embeds for accessibility

### 🧼 Redaction & Safety

> [!WARNING]
> Do **not** commit screenshots containing:
> - passwords, API keys, tokens, cookies
> - personal emails/phone numbers (unless explicitly approved and governed)
> - precise sensitive locations (e.g., protected sites) without required obfuscation

If redaction is required:
- redact **before** committing
- mark `Redaction? = ✅ yes` in the manifest
- describe *what was redacted and why* in the Notes column

---

## ✅ Definition of Done

Before considering a screenshot “accepted”:

- [ ] File name follows convention (`SS-###__YYYY-MM-DD__...`)
- [ ] Manifest row added/updated (URL + captured timestamp + purpose)
- [ ] Redaction completed (if needed) and noted
- [ ] Screenshot is referenced from mapping docs (`../../index.md` or `../../mapping.md`)
- [ ] License/terms screenshots exist **if** they influence DCAT metadata
- [ ] Hash recorded (optional but recommended for integrity)

---

## 🔁 Changelog

| Date | Change | By |
|---|---|---|
| 2026-01-29 | Initialized screenshots index template | @TBD |

---
