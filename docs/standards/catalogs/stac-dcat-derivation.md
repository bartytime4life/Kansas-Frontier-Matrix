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

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

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

json_schema_ref: "../../schemas/json/stac-dcat-derivation-v1.json"
shape_schema_ref: "../../schemas/shacl/stac-dcat-derivation-v1.shape.ttl"

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
Define the **authoritative KFM pattern** in which **STAC Items and Collections are the source of truth**, and **DCAT is always derived automatically from STAC** for catalogs, portals, and federation.

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

- `docs/standards/catalogs/README.md` — Catalog & metadata standards index.  
- `docs/standards/catalogs/stac/stac-kfm-profile.md` — KFM STAC profile.  
- `docs/standards/catalogs/dcat/dcat-kfm-profile.md` — KFM DCAT profile.  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md` — Detailed field-level mapping.

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/catalogs/
├── 📄 README.md                         — Catalog & metadata standards index
│
├── 🧩 stac/                             — STAC profiles, patterns, examples
│   └── 📄 stac-kfm-profile.md
│
├── 🧩 dcat/                             — DCAT profiles, patterns, examples
│   └── 📄 dcat-kfm-profile.md
│
├── 🔁 crosswalks/                       — Implementation-oriented crosswalk docs
│   └── 📄 stac-dcat-crosswalk.md
│
└── 📦 stac-dcat-derivation.md           — ← This document (STAC → DCAT model)
~~~

Implementation code & CI hooks SHOULD live under:

- `src/pipelines/catalogs/stac-dcat/` — ETL & crosswalk implementation.  
- `schemas/catalogs/` — JSON/SHACL schemas validating derived DCAT against this model.

---

## 🌍 Why STAC Is the Source of Truth

STAC is a **GeoJSON-native, geospatially explicit** model. A STAC Item/Collection carries:

- `geometry` — exact spatial footprint.  
- `bbox` — derived spatial envelope.  
- `properties.datetime` or `properties.start_datetime` / `properties.end_datetime`.  
- `assets` — per-asset `href`, `type`, `roles`, checksums, titles.  
- `properties` — domain-specific metadata (e.g., NAIP, HRRR, archaeology, hydrology).

These fields drive:

- Map rendering & tiling.  
- Ingestion pipelines (ETL, cloud-native access).  
- Provenance & lineage (via PROV-O / KFM registries).  
- Temporal indexing & query.  
- Validation via `stac-validator` and related tools.

Because STAC is **spatially explicit, time-aware, and asset-centric**, KFM treats it as **canonical** and **directly maintained** by data engineers and domain stewards.

---

## 📚 Why DCAT Should Be Derived

DCAT is optimized for:

- **Discovery & search** (catalog portals, APIs).  
- **Federation** with external catalogs and data portals.  
- Semantic web ecosystems (RDF, JSON-LD, Turtle).

DCAT is **not designed** to be the authoritative geospatial metadata layer for:

- Complex asset lists (multiple formats, multi-resolution pyramids).  
- Detailed geospatial footprints beyond bounding boxes.  
- STAC-specific structures (Collections → Items → Assets).

Therefore:

- DCAT in KFM is treated as an **artifact generated from STAC**.  
- Editing DCAT directly risks divergence between catalogs and spatially authoritative STAC.

**KFM rule**

> STAC is edited → STAC is validated → DCAT is regenerated → portals & catalogs update.

No production DCAT should exist without an upstream STAC representation.

---

## 🧱 Recommended Architecture

~~~text
Authoritative STAC Catalog
(data/stac/**.json)
│
├── validate → stac-validator · stac-check
│
└── transform → STAC → DCAT JSON-LD crosswalk
     │
     ├── dcat:Dataset       (per STAC Item/Collection)
     ├── dcat:Distribution  (per STAC Asset)
     └── dcat:DataService   (optional, for live services/APIs)
~~~

**Key rule**

- **Do NOT hand-edit DCAT artifacts in production.**  
- All DCAT (JSON-LD, Turtle, RDF/XML) must be **derived artifacts** produced from STAC via governed crosswalks and pipelines.

---

## 🔁 Minimal STAC → DCAT Crosswalk

This table defines the **minimal, stable mapping template**. Domain-specific extensions may add more fields, but **must not conflict** with this base.

### Dataset-Level Mapping (STAC Item/Collection → dcat:Dataset)

| STAC Field / Concept                  | DCAT / RDF Field                     |
|--------------------------------------|--------------------------------------|
| `id`                                 | `dct:identifier`                     |
| `properties.title`                   | `dct:title`                          |
| `properties.description`             | `dct:description`                    |
| `bbox`                               | `dct:spatial` (`dct:Location`)       |
| `datetime` or `start/end_datetime`   | `dct:temporal` (`dct:PeriodOfTime`)  |
| `keywords` / `tags`                  | `dcat:keyword`                       |
| `providers`                          | `dct:publisher`, `dct:creator`       |
| `links` (homepage, docs)             | `dcat:landingPage` / `foaf:page`     |
| collection membership                | `dct:isPartOf` / `dcat:inSeries`     |
| `license`                            | `dct:license`                        |
| provenance/source                    | `dct:source`, `prov:wasDerivedFrom`  |

### Asset-Level Mapping (STAC Asset → dcat:Distribution)

| STAC Asset Field                     | DCAT / RDF Field                     |
|--------------------------------------|--------------------------------------|
| `href`                               | `dcat:downloadURL` / `dcat:accessURL`|
| `type`                               | `dct:format`                         |
| `roles`                              | profile-specific role mapping        |
| `checksum:*`                         | `spdx:checksum`                      |
| `title`                              | `dct:title`                          |
| `description`                        | `dct:description`                    |

Additional mappings (e.g., `eo:*`, `sar:*`, domain profiles) MUST be specified in:

- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

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
- Any change to STAC triggers a new DCAT derivation; DCAT is never the authoritative source.

---

## 🛠️ Tooling Recommendations

KFM recommends the following for a **STAC-first, DCAT-derived** pipeline:

- **STAC Validation & Linting**
  - `stac-validator` — schema + extension validation.  
  - `stac-check` or equivalent — semantic and profile checks.  

- **STAC → DCAT Crosswalk**
  - Crosswalk scripts maintained under `src/pipelines/catalogs/stac-dcat/`.  
  - Prefer deterministic transforms (e.g., Python or Node scripts, with tests).  
  - Avoid “ad-hoc” transformations that diverge from `stac-dcat-crosswalk.md`.

- **Artifact Layout**
  - STAC sources: `data/stac/**`  
  - Derived DCAT JSON-LD: `data/dcat/jsonld/**`  
  - Optional DCAT Turtle/RDF: `data/dcat/rdf/**`

DCAT outputs MUST be treated as **build artifacts** that can be safely regenerated.

---

## ✅ CI & Governance Rules

CI MUST enforce:

1. **No orphan DCAT**

   - Every DCAT `dcat:Dataset` MUST have a corresponding STAC Item/Collection.  
   - CI should fail if DCAT is found without a traceable STAC source.

2. **No hand-edited DCAT in production**

   - Derived DCAT files SHOULD be overwritten by pipelines.  
   - Manual edits MUST be treated as temporary and discarded on next derivation.

3. **Crosswalk validation**

   - DCAT outputs:
     - MUST validate against the KFM DCAT profile schema.  
     - MUST maintain identifier, temporal, and spatial consistency with STAC.  

4. **Provenance alignment**

   - Derivation processes MUST record:
     - STAC source IDs.  
     - Transform script/tool versions.  
     - Output DCAT identifiers.  

   - This information is captured in telemetry and governance ledgers.

5. **Governance changes**

   - Any change to:
     - KFM STAC profile,  
     - KFM DCAT profile, or  
     - Crosswalk semantics  

     MUST:

     - Bump this document’s version.  
     - Update associated schemas/SHACL shapes.  
     - Be logged in the governance ledger and reviewed by the Metadata & Catalogs WG and FAIR+CARE Council.

---

## 🧾 Summary (KFM Position)

KFM’s **authoritative stance** for catalog metadata:

- **Always author and maintain metadata in STAC.**  
- **Never treat DCAT as the source of truth.**  
- **Always derive DCAT (JSON-LD and related formats) from validated STAC via governed crosswalks.**  
- **Use explicit STAC → DCAT mappings to preserve semantic and spatial fidelity.**

This model ensures:

- Spatial correctness for maps and analytics.  
- Stable, federated catalogs for discovery & portals.  
- Consistent, traceable metadata across KFM systems and external partners.

---

## 🕰️ Version History

| Version  | Date       | Author                                   | Summary                                                                                   |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM-standard STAC → DCAT derivation model; defined STAC-first catalog architecture, minimal crosswalk, tooling, and CI/governance rules. |

