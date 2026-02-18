<!--
KFM — Governed Artifact (README)
Scope: data/catalog (DCAT discovery layer)
Notes:
- Keep this file policy- and standards-aligned.
- Avoid adding “one-off” conventions here; extend the KFM profiles instead.
-->

# `data/catalog` 🗂️

**Governed • Evidence-first • FAIR+CARE aligned**

This directory is the **canonical home for KFM’s DCAT dataset discovery records** (JSON-LD), used to make datasets findable and to bind them (via links) to:

- **STAC** (spatiotemporal asset indexing) — stored elsewhere (`data/stac/...`)
- **PROV** (lineage bundles) — stored elsewhere (`data/prov/...`)
- **Processed artifacts** (the actual data assets) — stored under `data/processed/<domain>/...`

> ⚠️ **Non-negotiable invariant:** no stage may leapfrog the ordering  
> **ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**.  
> Catalog outputs are required “boundary artifacts” before anything is treated as published.  
> (See the repo Master Guide for the invariant + enforcement model.)

---

## What lives here

### ✅ In scope
- **DCAT dataset entries** (JSON-LD), one per governed dataset (and/or dataset version, depending on the profile).
- Optional **index/aggregation** files for DCAT catalogs *if* the repo adopts them (not confirmed in repo).

### ❌ Out of scope
- Raw data, work-in-progress outputs, or processed artifacts (those belong in `data/raw`, `data/work`, `data/processed`).
- STAC item/collection JSON (those belong in `data/stac/...`).
- PROV bundles (those belong in `data/prov/...`).

---

## Directory layout

```text
data/catalog/
├── README.md
└── dcat/
    ├── <dataset_slug>.jsonld
    ├── <dataset_slug>__<version_or_run>.jsonld        # optional (not confirmed in repo)
    └── catalog.jsonld                                 # optional aggregate (not confirmed in repo)
```

Related (canonical) locations (defined by the Master Guide v13 draft):

```text
data/stac/
├── collections/
└── items/

data/prov/
└── <prov_bundle_files>

data/processed/
└── <domain>/
    └── <published_artifacts>
```

---

## How `data/catalog/` fits in the KFM pipeline

```mermaid
flowchart LR
  A[Raw sources] --> B[ETL / Normalize]
  B --> C[Processed artifacts<br/>data/processed/&lt;domain&gt;/...]
  C --> S[STAC Items + Collections<br/>data/stac/...]
  C --> D[DCAT Dataset Views<br/>data/catalog/dcat/...]
  C --> P[PROV Lineage Bundles<br/>data/prov/...]
  S --> G[Graph build (Neo4j references catalogs)]
  D --> G
  P --> G
  G --> API[Governed APIs (policy + audit)]
  API --> UI[UI / Story Nodes / Focus Mode]
```

**Why this matters:** catalogs/provenance are the **glue layer** that binds pipeline outputs to the graph and all user-facing experiences without breaking the trust membrane.

---

## DCAT record conventions

### File naming
- **Preferred:** `data/catalog/dcat/<dataset_slug>.jsonld`
- Use a stable, lowercase, URL-safe slug (kebab-case recommended).
- If the repo chooses versioned files, use a deterministic suffix (e.g., run ID or content hash) **(not confirmed in repo)**.

### Content format
- DCAT entries are **JSON-LD**.
- KFM extends base standards via KFM profiles; do **not** introduce ad-hoc fields in production metadata. If you need new fields, extend the **KFM DCAT profile** and update schemas + validators.

---

## Minimum required DCAT fields

The KFM integration blueprint defines minimum required DCAT fields; treat this list as the baseline for “publishable.”  
(Exact validation rules live in the schemas/profiles.)

| Field | Required | Purpose | Notes |
|---|---:|---|---|
| `dct:title` | ✅ | Human-readable dataset name | Stable across versions when possible |
| `dct:description` | ✅ | What the dataset is + why it exists | Keep it evidence-first; avoid interpretation |
| `dct:publisher` | ✅ | Organization identifier | Prefer stable org IDs |
| `dct:license` | ✅ | License (SPDX or URL) | Must reflect actual reuse rights |
| `dct:spatial` | ✅ | Spatial coverage | bbox or administrative coverage |
| `dct:temporal` | ✅ | Temporal coverage | start/end (or intervals per profile) |
| `dct:accrualPeriodicity` | ✅ | Update cadence | e.g., monthly, annual, near-real-time |
| `dcat:distribution` | ✅ | How to access | download + API endpoints; may point to STAC |
| `prov:wasGeneratedBy` | ✅ | Link to provenance activity | Must resolve to PROV bundle/activity |

---

## Cross-layer linkage expectations

To keep catalogs, graph, and narratives synchronized, KFM expects cross-references across layers:

| From | Must link to | Why it exists |
|---|---|---|
| **DCAT** (`data/catalog/dcat`) | **STAC** record(s) or data endpoints | DCAT is the discovery layer; STAC provides spatial/temporal + asset detail |
| **DCAT** | **PROV** activity/bundle | Every published dataset must have traceable lineage |
| **STAC Items** | **Processed artifacts** (`data/processed/**`) | STAC metadata must point to the actual asset(s) |
| **PROV** | raw → work → processed entities + agents | Reproducibility + accountability |
| **Graph** | references **catalog IDs**, not payloads | Relationships live in graph; evidence lives in catalogs |

> Tip: If your system implements stable evidence reference schemes (e.g., `dcat://`, `stac://`, `prov://`), prefer those consistently so citations can be resolved through the evidence resolver.

---

## Validation gates

Catalog contributions are expected to be **CI-validated** and **fail-closed**. Minimum gates include:

- **Schema validation** (DCAT JSON-LD conforms to KFM DCAT profile)
- **Link-checks** (distributions and cross-links resolve)
- **License + attribution present** in DCAT (restrictions enforced via policy)
- **Provenance completeness** (every promoted artifact has a PROV chain + deterministic checksum)
- **Spatial + temporal sanity** (coverage fields present; no impossible time ranges)
- **No secrets / sensitive leakage** (policy + scanners block)

If any of these fail, the dataset should not be considered “published.”

---

## Governance and sensitivity

KFM governance is **machine-enforced**, not prose-enforced:

- **Classification and sovereignty propagate:** no derived artifact can be less restricted than its inputs.
- **Sensitive locations:** prefer generalization/redaction over precision if there’s risk.
- **Human review triggers:** if a dataset involves restricted knowledge, licensing ambiguity, or culturally protected information, route it to governance review (and keep the record restricted until approved).

---

## Example DCAT Dataset entry

<details>
<summary><strong>Minimal JSON-LD example (illustrative; follow the KFM DCAT profile)</strong></summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "dcat:Dataset",
  "@id": "dcat://kfm.example/<dataset_slug>",
  "dct:title": "Example Dataset Title",
  "dct:description": "Concise, evidence-first description of the dataset and its intended use.",
  "dct:publisher": { "@id": "org://kfm/<org_id>" },
  "dct:license": "https://spdx.org/licenses/CC-BY-4.0.html",
  "dct:spatial": {
    "@type": "dct:Location",
    "dct:description": "Kansas (example)"
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": { "@value": "1850-01-01", "@type": "xsd:date" },
    "dcat:endDate":   { "@value": "1900-12-31", "@type": "xsd:date" }
  },
  "dct:accrualPeriodicity": "irregular",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Collection",
      "dcat:accessURL": "stac://collections/<collection_id>"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "API Endpoint",
      "dcat:accessURL": "https://api.kfm.example/v1/datasets/<dataset_slug>"
    }
  ],
  "prov:wasGeneratedBy": { "@id": "prov://runs/<run_id>" }
}
```

</details>

---

## PR checklist (DCAT)

- [ ] DCAT JSON-LD created/updated in `data/catalog/dcat/`
- [ ] License + publisher + coverage fields present
- [ ] `dcat:distribution` links resolve (and do not bypass policy)
- [ ] `prov:wasGeneratedBy` resolves to a PROV activity/bundle
- [ ] Cross-links to STAC (if applicable) are present and valid
- [ ] CI gates pass (schema validation + link-check + policy checks)
- [ ] If sensitive/restricted: record is correctly classified and governance review is triggered

---

## Quick glossary

- **DCAT**: dataset discovery + distribution metadata (catalog layer)
- **STAC**: spatiotemporal asset indexing (map/timeline-friendly)
- **PROV**: lineage model (entities, activities, agents)
- **Boundary artifacts**: the required catalog/provenance outputs that gate publication