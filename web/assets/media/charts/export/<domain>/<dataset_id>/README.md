---
title: "📊 Charts Export — <domain>/<dataset_id>"
path: "web/assets/media/charts/export/<domain>/<dataset_id>/README.md"
version: "v0.1.0"
last_updated: "2026-01-18"
status: "draft"
doc_kind: "Dataset Evidence Artifact (Charts Export)"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
dataset_id: "<dataset_id>"
domain: "<domain>"
---

# 📊 Charts Export — `<domain>/<dataset_id>`

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Artifact](https://img.shields.io/badge/artifact-evidence--artifact-6f42c1)
![Pipeline](https://img.shields.io/badge/pipeline-deterministic-2ea44f)
![Governance](https://img.shields.io/badge/governance-contract--first%20%7C%20provenance--first-blue)

> [!IMPORTANT]
> 🧾 **Treat this folder as an evidence artifact.** These charts are not “random screenshots” — they must remain reproducible, provenance-linked, and safe to publish.

---

## 📘 Overview

### 🎯 Purpose
This folder contains **exported chart assets** (typically SVG/PNG + lightweight metadata) for the dataset **`<dataset_id>`** in the **`<domain>`** domain. These assets are intended for UI use (e.g., popups, panels, story pages) where “quick charts” help interpret a dataset without exposing raw tables directly.

### 🧭 Scope
**In scope ✅**
- Chart images (prefer SVG) + optional fallbacks (PNG/WebP)
- A small **manifest/index** so the UI can discover what exists
- Provenance & metadata pointers so every chart can be traced back to source data + pipeline steps

**Out of scope 🚫**
- Raw source datasets (those live in governed dataset storage/catalogs)
- Ad-hoc “one-off” charts with unknown provenance
- Hand-edited charts that cannot be regenerated

### 👥 Audience
- 🧑‍💻 Front-end + API developers integrating charts into the UI
- 🧑‍🔬 Domain stewards validating interpretation + labels/units
- 🧾 Governance reviewers ensuring provenance + sensitivity compliance

### 🧩 Definitions
- **Domain**: A thematic module grouping datasets (e.g., air-quality, historical, soils).
- **Dataset ID**: Stable slug/identifier for the dataset being charted.
- **Chart ID**: Stable slug for a specific chart export (used for filenames + UI lookup).
- **Evidence artifact**: A derived output treated as “data + metadata,” registered before use in UI/narratives.[^evidence-artifact]
- **Contract-first**: Schemas/contracts are first-class; breaking changes require versioning.[^contract-first]
- **Deterministic pipeline**: Idempotent, config-driven, logged transformations to ensure reproducibility.[^deterministic-pipeline]

---

## 🗂️ Directory Layout

> [!NOTE]
> This is the **recommended** layout for consistency across domains/datasets. Adjust folder names if the repo already standardizes them elsewhere — but keep the *roles* (manifest, exports, provenance) intact.

```text
📁 web/assets/media/charts/export/<domain>/<dataset_id>/
├─ 📄 README.md                       # You are here ✨
├─ 📄 manifest.json                   # Index of chart exports (UI-friendly)
├─ 📁 svg/                            # Primary exports (resolution-independent)
│  ├─ 🖼️ <chart_id>.svg
│  └─ 🖼️ ...
├─ 📁 png/                            # Optional fallbacks / social previews
│  ├─ 🖼️ <chart_id>.png
│  └─ 🖼️ ...
├─ 📁 data/                           # Optional small tables supporting charts
│  ├─ 📄 <chart_id>.csv
│  └─ 📄 ...
└─ 📁 provenance/                     # “Evidence artifact” metadata + lineage
   ├─ 📄 stac.item.json               # STAC item/collection pointer(s)
   ├─ 📄 dcat.dataset.json            # DCAT dataset/distribution pointer(s)
   └─ 📄 prov.jsonld                  # PROV lineage (who/what/when/how)
```

---

## 🧾 Manifest Contract

Create/maintain a `manifest.json` so the UI can enumerate charts without hardcoding filenames.

### ✅ Minimal recommended shape

```json
{
  "domain": "<domain>",
  "dataset_id": "<dataset_id>",
  "charts": [
    {
      "chart_id": "example_chart_id",
      "title": "Human-readable chart title",
      "summary": "1–2 sentence purpose/interpretation guardrail.",
      "units": "TBD",
      "files": {
        "svg": "svg/example_chart_id.svg",
        "png": "png/example_chart_id.png"
      },
      "data": "data/example_chart_id.csv",
      "provenance": {
        "stac_item_id": "TBD",
        "dcat_dataset_id": "TBD",
        "prov_activity_id": "TBD"
      },
      "alt": "Accessible description of the chart for screen readers."
    }
  ]
}
```

> [!TIP]
> Keep `manifest.json` **small and stable**. It should point to large artifacts, not embed them.

---

## 🌐 UI Integration Notes

- The front-end typically contains reusable UI components, including **charts**, within the `web/` application structure.[^web-frontend]
- Charts may appear in **map pop-ups / detail panels** as part of “statistical summaries & charts” that make data interpretable.[^ui-charts]

### 📚 Story / Focus Mode usage
If a Story Node references these charts, ensure:
- The Story Node is provenance-linked (no unsourced media).
- The chart’s manifest entry includes clear units, alt text, and provenance pointers.[^focus-mode]

---

## 🎨 Export Guidelines

### ✅ Prefer SVG (default)
SVG is the preferred export format because it is **resolution-independent** and often **smaller** than bitmap formats for charts/linework.[^svg]

### 🧷 When to include PNG
Include PNG fallbacks when:
- A platform cannot render SVG reliably
- You need a fixed-size preview thumbnail
- Sharing contexts require raster images

### ♿ Accessibility
- Every chart must have **alt text** in `manifest.json`
- Captions should avoid “interpretation leaps” — describe what the chart shows, not what it *means* (interpretation belongs in Story Nodes + citations)

---

## 🧬 Provenance & Governance Requirements

> [!WARNING]
> KFM governance expects that **evidence artifacts are registered with metadata and lineage** before they are used in UI or narratives.[^evidence-artifact]

Minimum expectations:
- **Provenance-first**: exports are traceable via STAC/DCAT/PROV pointers (see `provenance/`).[^schema-validation]
- **Contract-first**: if the manifest or provenance schema changes, bump versions + keep compatibility where possible.[^contract-first]
- **Deterministic pipeline**: exports should be reproducible from inputs + config (no mystery steps).[^deterministic-pipeline]
- **Safety & sensitivity**: avoid leaking PII or sensitive locations; ensure classification is not “downgraded” accidentally.[^security-scans]

---

## 🧪 Validation & CI Expectations

This repo’s documentation + structured artifacts are expected to be machine-validated:
- YAML front-matter + required sections (governed doc template)
- Link/reference validation
- JSON schema validation for STAC/DCAT/PROV artifacts[^schema-validation]
- Security scans (secrets, PII/sensitive data, sensitive location checks, classification consistency)[^security-scans]

---

## ✅ Definition of Done

- [ ] `manifest.json` exists and lists every exported chart (with `chart_id`, title, units, alt text)
- [ ] SVG exports exist (and render correctly)
- [ ] PNG fallbacks added *only if needed*
- [ ] Provenance pointers filled (`stac_item_id`, `dcat_dataset_id`, `prov_activity_id`)
- [ ] No sensitive/PII leakage (reviewed + consistent classification)
- [ ] Regeneration steps are documented (link to pipeline/SOP/Makefile target if available)
- [ ] Review completed by a domain steward (labels/units/interpretation guardrails)

---

## 🔗 References

- 📘 Master guide / contracts / governed doc templates live under `docs/` (see repo conventions).[^kfm-master-guide]
- 🧰 Pipelines are typically small focused scripts invoked via CLI/Makefile in the core pipeline structure.[^pipeline-cli]

---

## 📎 Footnotes (evidence)

[^kfm-master-guide]: KFM Master Guide describes the canonical pipeline ordering and cross-cutting invariants (provenance-first, contract-first, evidence-first). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^contract-first]: “Contract-first” as a core principle (schemas/contracts as first-class artifacts; strict versioning expectations). [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^deterministic-pipeline]: “Deterministic pipeline” as a core principle (idempotent/config-driven/logged transformations for reproducibility + lineage). [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^evidence-artifact]: Definition of “evidence artifact” and the requirement that evidence is registered with catalogs + lineage before UI/narrative use. [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^schema-validation]: CI validation includes structured outputs (STAC/DCAT/PROV) checked against schemas; failures block the build. [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^security-scans]: Security/governance scans include secret scanning, PII/sensitive data detection, sensitive location checks, and classification consistency checks. [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^web-frontend]: The `web/` front-end structure includes UI components (including charts) and story node content patterns (Markdown narrative + config JSON). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^ui-charts]: KFM UI includes “statistical summaries & charts” for datasets (computed backend with Python/pandas or front-end for small data, e.g., D3). [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^focus-mode]: Focus Mode + story narrative linking relies on provenance-linked content and graph context (AI support + narrative/data linking). [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^pipeline-cli]: Pipeline scripts are kept small/focused and invoked via Makefile/CLI; the `web/` folder can host static site assets + precomputed JSON needed by the app. [oai_citation:10‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
[^svg]: SVG guidance: using SVG rather than bitmap formats provides resolution independence and often smaller file sizes; SVG is a good fit for charts/linework. [oai_citation:11‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
