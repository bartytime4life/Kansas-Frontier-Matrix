---
title: "📦 KFM v11.2.3 — STAC → DCAT Derivation Model (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Authoritative pattern for treating STAC as the source of truth and emitting DCAT automatically from STAC for the Kansas Frontier Matrix."
path: "docs/standards/catalogs/stac-dcat-derivation.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 3.0 crosswalk compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-dcat-derivation-v11.2.3"
semantic_document_id: "kfm-standards-stac-dcat-derivation-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac-dcat-derivation:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_kind: "Standard"
intent: "metadata-stac-to-dcat-derivation"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_rights_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/stac-dcat-derivation-v1.json"
shape_schema_ref: "../../../schemas/shacl/stac-dcat-derivation-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC/DCAT standards update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "timeline-generation"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "metadata-extraction"
    - "timeline-generation"
    - "a11y-adaptations"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🌍 Why STAC Is the Source of Truth"
    - "📚 Why DCAT Should Be Derived"
    - "🧱 Recommended Architecture"
    - "🔁 Minimal STAC → DCAT Crosswalk"
    - "🧪 Example STAC → DCAT JSON-LD Derivation"
    - "🛠️ Tooling Recommendations"
    - "✅ CI & Governance Rules"
    - "🧾 Summary (KFM Position)"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 📦 **KFM v11.2.3 — STAC → DCAT Derivation Model**  
`docs/standards/catalogs/stac-dcat-derivation.md`

**Purpose**  
Define the **authoritative KFM pattern** where **STAC Items and Collections are the source of truth**, and **DCAT is always derived automatically from STAC** for catalogs, portals, and federation.

</div>

---

## 📘 Overview

This standard specifies KFM’s catalog architecture:

- **STAC (SpatioTemporal Asset Catalog) Items and Collections are authoritative.**  
- **DCAT (Data Catalog Vocabulary) representations are emitted automatically from STAC.**

Goals:

- Preserve **spatial accuracy** and **temporal consistency**.  
- Avoid drift between **asset-level metadata** and higher-level catalogs.  
- Ensure catalogs remain **FAIR+CARE-compliant**, provenance-aware, and machine-safe.  

This document is a sibling to:

- `docs/standards/catalogs/README.md` — catalog & metadata standards index.  
- `docs/standards/catalogs/stac/stac-kfm-profile.md` — KFM STAC profile.  
- `docs/standards/catalogs/dcat/dcat-kfm-profile.md` — KFM DCAT profile.  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md` — detailed field-level mapping.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 standards/
        ├── 📁 catalogs/                         📚 Catalog & metadata standards
        │   ├── 📄 README.md                     📚 Index for catalog standards
        │   │
        │   ├── 🧩 stac/                         🛰️ STAC profiles, patterns, examples
        │   │   ├── 📄 stac-kfm-profile.md       STAC profile (Collections, Items, kfm:* fields)
        │   │   └── 📄 stac-best-practices.md    STAC naming, tiling & asset patterns
        │   │
        │   ├── 🧩 dcat/                         🗄️ DCAT / GeoDCAT profiles
        │   │   ├── 📄 dcat-kfm-profile.md       DCAT profile for catalogs & federation
        │   │   └── 📄 dcat-examples.md          Derived DCAT JSON-LD / Turtle examples
        │   │
        │   ├── 🔁 crosswalks/                   🔀 STAC ↔ DCAT (& optional CKAN) crosswalks
        │   │   └── 📄 stac-dcat-crosswalk.md    Canonical STAC ↔ DCAT mapping (field-level)
        │   │
        │   └── 📦 stac-dcat-derivation.md       📦 STAC → DCAT derivation model (this file)
        │
        └── 📁 governance/ …                     ⚖️ Governance & approvals
~~~

**Implementation (code, not standards)** SHOULD live under:

- `src/pipelines/catalogs/stac-dcat/` — ETL & crosswalk implementation.  
- `schemas/catalogs/` — schemas validating derived DCAT (in addition to refs in this front matter).  

---

## 🌍 Why STAC Is the Source of Truth

STAC is a **GeoJSON-native, geospatially explicit** model. A STAC Item or Collection carries:

- `geometry` — exact spatial footprint.  
- `bbox` — derived spatial envelope.  
- `properties.datetime` or `properties.start_datetime` / `properties.end_datetime`.  
- `assets` — per-asset `href`, `type`, `roles`, checksums, titles, and sizes.  
- `properties` — domain-specific metadata (e.g., NAIP, HRRR, archaeology, hydrology, remote sensing).

These fields drive:

- map rendering and tiling  
- ingestion pipelines (ETL, cloud-native reads)  
- provenance & lineage (via PROV-O / KFM-PROV v11)  
- temporal indexing & queries  
- multi-asset integrity (checksums, roles, media types)

Because STAC is **spatially explicit, time-aware, and asset-centric**, KFM treats it as:

- the **only** place where authoritative spatial and temporal catalog facts are curated  
- the starting point for all downstream catalog projections, including DCAT and CKAN-like portals

---

## 📚 Why DCAT Should Be Derived

DCAT is optimized for:

- **discovery & search** (catalog portals, SPARQL/RDF, JSON-LD APIs)  
- **federation** with external catalogs and knowledge graphs  
- generic **dataset-level and service-level descriptions** (`dcat:Dataset`, `dcat:Distribution`, `dcat:DataService`)

DCAT is **not** designed to be the authoritative, detailed geospatial metadata layer for:

- complex, multi-asset datasets (e.g., pyramids, multiple CRS/CRS-less assets)  
- rich per-asset metadata beyond what fits naturally into a small number of distributions  
- STAC-specific constructs like Item/Collection semantics and link graphs

KFM position:

- DCAT is the **discovery and federation** surface, **not** the spatial truth source.  
- Hand-editing DCAT in production risks drift from STAC and must be avoided.

> **Rule:** STAC is edited → STAC is validated → DCAT is regenerated → catalogs & portals update.

No production DCAT should exist without a corresponding STAC representation.

---

## 🧱 Recommended Architecture

~~~text
Authoritative STAC Catalog (data/stac/**.json)
│
├── Validate STAC
│   └─ stac-validator + KFM STAC profile checks
│
└── Derive DCAT (STAC → DCAT)
    │
    ├── dcat:Dataset       (per STAC Collection/Item)
    ├── dcat:Distribution  (per STAC Asset)
    └── dcat:DataService   (optional, for live services/APIs)
~~~

**Key architectural rules**

- **Do NOT hand-edit DCAT artifacts in production.**  
- Treat DCAT JSON-LD/Turtle as **build artifacts** that are safe to delete and regenerate.  
- Keep derivation tooling **config-driven and deterministic** (KFM-PDC v11 compliant).  

Recommended file layout:

- STAC source: `data/stac/**`  
- DCAT JSON-LD: `data/dcat/jsonld/**`  
- DCAT Turtle/RDF (optional): `data/dcat/rdf/**`

---

## 🔁 Minimal STAC → DCAT Crosswalk

This section captures the **minimal, stable mapping template**. Domain profiles may extend it, but MUST NOT conflict with it. Full details live in:

- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

### Dataset-Level Mapping  
(STAC Item/Collection → `dcat:Dataset`)

| STAC Field / Concept                | DCAT / RDF Field                      |
|------------------------------------|---------------------------------------|
| `id`                               | `dct:identifier`                      |
| `properties.title`                 | `dct:title`                           |
| `properties.description`           | `dct:description`                     |
| `bbox`                             | `dct:spatial` (`dct:Location`)        |
| `geometry`                         | GeoSPARQL geometry within `dct:spatial` or related object |
| `datetime` / `start/end_datetime`  | `dct:temporal` (`dct:PeriodOfTime`)   |
| `keywords` / `tags`                | `dcat:keyword`                        |
| `providers`                        | `dct:publisher`, `dct:creator`        |
| `links` (homepage/docs)           | `dcat:landingPage`, `foaf:page`       |
| collection membership              | `dct:isPartOf` / `dcat:inSeries`      |
| `license`                          | `dct:license`                         |
| provenance/source                  | `dct:source`, `prov:wasDerivedFrom`   |

### Asset-Level Mapping  
(STAC Asset → `dcat:Distribution`)

| STAC Asset Field             | DCAT / RDF Field                      |
|-----------------------------|----------------------------------------|
| `href`                      | `dcat:downloadURL` / `dcat:accessURL` |
| `type`                      | `dct:format`                          |
| `roles`                     | profile-specific role → distribution classification |
| `title`                     | `dct:title`                           |
| `description`               | `dct:description`                     |
| `checksum:*`                | `spdx:checksum` (`spdx:Checksum`)     |
| `kfm:*` asset metadata      | mapped into profile-specific DCAT extensions or retained as annotations |

Additional domain mappings (e.g., EO, SAR, heritage, hydrology) MUST be documented in `stac-dcat-crosswalk.md`.

---

## 🧪 Example STAC → DCAT JSON-LD Derivation

### Input STAC Item (Simplified)

~~~json
{
  "id": "naip_2023_tile_001",
  "type": "Feature",
  "geometry": { "...": "..." },
  "bbox": [-98.0, 38.1, -97.9, 38.2],
  "properties": {
    "datetime": "2023-07-11T18:22:00Z",
    "title": "NAIP 2023 Tile 001",
    "description": "NAIP 2023 imagery tile over central Kansas."
  },
  "assets": {
    "image": {
      "href": "https://example.com/naip_001.tif",
      "type": "image/tiff; application=geotiff",
      "checksum:sha256": "abc123..."
    }
  }
}
~~~

### Derived DCAT JSON-LD (Auto-Generated)

~~~json
{
  "@context": "https://www.w3.org/ns/dcat.jsonld",
  "@type": "dcat:Dataset",
  "dct:identifier": "naip_2023_tile_001",
  "dct:title": "NAIP 2023 Tile 001",
  "dct:description": "NAIP 2023 imagery tile over central Kansas.",
  "dct:spatial": {
    "@type": "dct:Location",
    "bbox": [-98.0, 38.1, -97.9, 38.2]
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2023-07-11T18:22:00Z",
    "dcat:endDate": "2023-07-11T18:22:00Z"
  },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcat:downloadURL": "https://example.com/naip_001.tif",
      "dct:format": "image/tiff; application=geotiff",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "sha256",
        "spdx:checksumValue": "abc123..."
      }
    }
  ]
}
~~~

Notes:

- JSON-LD above is **derived**, not hand-authored.  
- Any change to STAC triggers a new derivation; DCAT is never the spatial or temporal source of truth.

---

## 🛠️ Tooling Recommendations

KFM recommends a **config-driven**, **deterministic** toolchain:

### 1. STAC Validation

- `stac-validator` — schema + extension compliance.  
- KFM STAC profile checks (e.g., via custom Python/Node tooling) to enforce:
  - required `kfm:*` fields  
  - mission tags, event refs, ingest state, QC state.

### 2. STAC → DCAT Crosswalk

Implementation under:

- `src/pipelines/catalogs/stac-dcat/`

Should:

- read STAC Collections/Items from `data/stac/**`  
- output DCAT JSON-LD under `data/dcat/jsonld/**`  
- optionally emit Turtle/RDF for triple stores under `data/dcat/rdf/**`  
- be fully driven by configuration and crosswalk docs in:
  - `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

### 3. Provenance & Telemetry

Derivation jobs must:

- emit telemetry into `catalog-metadata-telemetry.json` (see `telemetry_ref`)  
- capture:
  - counts of STAC → DCAT conversions  
  - validation errors  
  - derivation timings and resource usage (aligned with `energy_schema` and `carbon_schema`)  
- write PROV-compatible lineage linking:
  - STAC source entities  
  - derivation activities  
  - DCAT output entities

---

## ✅ CI & Governance Rules

This derivation model is **enforced** via CI and governance:

1. **No Orphan DCAT**

   - CI fails if any DCAT record lacks a resolvable STAC source ID.  
   - DCAT checks must confirm `dct:identifier` maps back to a STAC `id`.

2. **No Hand-Edited DCAT in Production**

   - DCAT directories are treated as **generated**.  
   - Protected branches must not accept manual edits to DCAT artifacts without a documented migration path and governance exception.

3. **Crosswalk Validation**

   - Derived DCAT must:
     - validate against the KFM DCAT profile (`dcat-kfm-profile.md`)  
     - be internally consistent with STAC (identifiers, spatial/temporal ranges, license)  
   - Crosswalk fixtures and regression tests live under `tests/catalogs/stac-dcat/`.

4. **Provenance Requirements**

   - Each derivation run must record:
     - STAC source collection and item counts  
     - tool version and configuration hash  
     - release identifiers (linking to `sbom_ref`, `manifest_ref`)  

5. **Governance Changes**

   - Any modification to:
     - STAC profile fields used in catalogs  
     - DCAT profile fields derived from STAC  
     - crosswalk semantics or mappings  

   MUST:

   - bump this document’s `version` and `last_updated`  
   - update associated JSON/SHACL schemas (`json_schema_ref`, `shape_schema_ref`)  
   - be reviewed by the Metadata & Catalogs WG and FAIR+CARE Council  
   - be logged as an event in the governance ledger (e.g., `reports/audit/governance-ledger.json`)

---

## 🧾 Summary (KFM Position)

KFM’s **catalog stance**:

- **Author in STAC. Always.**  
- **Validate STAC first.**  
- **Derive DCAT from STAC via governed crosswalks.**  
- **Treat DCAT as a projection, not the source of truth.**  
- **Enforce the model via CI, telemetry, and governance.**

This guarantees:

- spatial and temporal correctness  
- stable identifiers and provenance  
- federation-ready catalogs that never drift from the authoritative STAC layer

---

## 🕰️ Version History

| Version | Date       | Author                                   | Summary                                                                                               |
|--------:|------------|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM-standard STAC → DCAT derivation model; defined STAC-first architecture, minimal crosswalk, tooling guidance, and CI/governance rules. |

---

<sub>© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.4</sub>

<br/>

<div align="center">

📦 **KFM v11.2.3 — STAC → DCAT Derivation Model**  
STAC First · DCAT Derived · Provenance Everywhere  

[📚 Catalog Standards Index](./README.md) · [📖 Standards Root](../README.md) · [⚖ Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>