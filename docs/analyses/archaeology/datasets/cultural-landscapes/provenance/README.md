---
title: "🧬 KFM v11.2.3 — Cultural Landscape Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Cultural Landscape Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
backward_compatibility: "v10.4.0 → v11.2.3 provenance-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-cultural-landscapes-provenance-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Provenance Logs"
intent: "cultural-landscape-provenance"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Cultural Landscape Provenance Logs**  
`docs/analyses/archaeology/datasets/cultural-landscapes/provenance/README.md`

**Purpose:**  
Define and govern the **provenance logging system** for all cultural landscape datasets within the Kansas Frontier Matrix (KFM).  
These logs capture **data origins**, **GIS transformations**, **ethical reviews**, **sensitivity generalization procedures**, and **FAIR+CARE governance requirements** for:

- Settlement regions  
- Interaction spheres  
- Resource procurement areas  
- Ancient mobility corridors  
- Generalized territorial/cultural boundaries  
- Any culturally significant environmental landscape layer  

Provenance files here ensure transparency, cultural safety, reproducibility, and explainability across KFM pipelines, Story Nodes, and Focus Mode v2/v3.

</div>

---

## 📘 Overview

Every cultural landscape dataset must produce a corresponding **PROV-O JSON-LD provenance record** stored in this directory.  
These logs document:

- Original data sources  
- Spatial generalization methods (H3, simplification)  
- Data cleaning & processing steps  
- Ethical and cultural reviews  
- Analyst and reviewer attribution  
- Versioning and lineage  
- Uncertainty, bias, and interpretive assumptions  
- Alignment with STAC Items + metadata  

Each provenance file is a **governed artifact**: it must be CI-validated, FAIR+CARE-audited, and graph-safe for ingestion into the KFM Neo4j knowledge graph.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/cultural-landscapes/provenance/
├── 📄 README.md                              # This file (provenance logging standard)
├── 🧾 great-bend-aspect-v2.json              # Provenance: Great Bend Aspect interaction sphere
├── 🧾 central-plains-exchange-v1.json        # Provenance: Central Plains exchange zone
├── 🧾 protohistoric-wichita-v1.json          # Provenance: Protohistoric Wichita region
└── 🧩 templates/                             # Provenance templates and JSON-LD skeletons for contributors
~~~

**Directory contract:**

- All **published** cultural landscape datasets must have at least one `*.json` provenance file here.  
- The `templates/` directory holds **canonical, versioned** JSON-LD skeletons used by CI to scaffold new provenance logs.  
- File naming:  
  - `<slug>-v<semver>.json` (e.g., `great-bend-aspect-v2.json`).  
  - Slug must match the corresponding dataset/STAC Item identifiers.

---

## 🧭 Required PROV-O Components (All Provenance Logs)

All provenance JSON-LD documents in this directory **must** conform to:

- PROV-O  
- CARE-aligned extensions  
- KFM archaeology provenance rules  
- KFM-MDP v11.2.2 machine-readability expectations  

### ✔ `@context` (Required)

Must include (at minimum):

- `"prov"` – `http://www.w3.org/ns/prov#`  
- `"care"` – KFM CARE vocabulary  
- `"kfm"` – KFM core vocabulary  
- Additional CIDOC-CRM, GeoSPARQL, and OWL-Time terms where appropriate.

### ✔ Entities (`prov:Entity`)

Must define at least:

| Entity ID    | Description |
|--------------|-------------|
| `raw`        | Original dataset — raster/vector/GeoJSON, literature-derived shapes, or archival interpretation |
| `generalized`| Spatially de-identified version (H3 or simplified polygon) suitable for public use |
| `processed`  | Cleaned + validated cultural landscape representation actually used in KFM |

Additional entities (e.g., `validation`, `review-dossier`, `source-map`) are encouraged when needed for clarity.

### ✔ Activities (`prov:Activity`)

Typical activities include:

- `generalization` – H3/simplification + dynamic masking  
- `feature_extraction` – digitization, classification, segmentation  
- `boundary_estimation` – model- or expert-driven boundary inference  
- `tribal_review` – sovereign review & cultural validation  
- `faircare_review` – internal FAIR+CARE governance check  
- `geoprocessing` – reprojection, clipping, harmonization  
- `time_model_alignment` – mapping to OWL-Time intervals / archaeological periods  

Each `prov:Activity` must include timestamps and, where applicable, explicit `kfm:steps`.

### ✔ Agents (`prov:Agent`)

Agents must include:

| Agent Type      | Example |
|-----------------|---------|
| Analyst         | Individual researcher, GIS specialist, or data engineer |
| Reviewer        | FAIR+CARE Council, archaeology working group |
| Tribal Reviewer | Sovereign tribal heritage/THPO office |
| Source Institution | Archive, survey authority, academic or agency source |

Agents should be referenced by **stable identifiers** where possible (e.g., ORCID, ROR, internal KFM IDs).

### ✔ Relations

At minimum, the following must be used to describe lineage:

- `prov:wasDerivedFrom`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  

These relations must form a **complete chain** from `raw` → `generalized` → `processed`, and connect activities and agents such that KFM’s Neo4j and Story Node systems can reconstruct the full history.

---

## ⚖ FAIR+CARE Cultural Safety Requirements

All provenance logs for cultural landscapes must include explicit CARE-aligned fields:

| CARE Field               | Purpose |
|--------------------------|---------|
| `care:sensitivity`       | Sensitivity level: `"generalized"` or `"restricted-generalized"` for public artifacts |
| `care:review`           | Review path: `"faircare"`, `"tribal"`, or combined patterns |
| `care:notes`            | Human-readable cultural considerations & constraints |
| `care:visibility_rules` | UI/pipeline visibility: `"h3-only"`, `"polygon-generalized"`, `"no-exact-boundaries"` |

**Forbidden content in *public* provenance logs:**

- `"restricted"` sensitivity (these remain internal-only)  
- Exact depictions of ceremonial areas  
- Burial ground outlines or quasi-exact approximations  
- Sensitive ethnographic knowledge, narratives, or origin stories that are not approved for open publication  

Where additional restrictions or sovereign policies apply, provenance logs must reference the appropriate internal governance documents via `kfm:governance_ref` and related fields.

---

## 🧪 Example Provenance Snippet

> **Note:** This example is illustrative only. Real datasets must supply accurate values, sources, and identifiers.

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Initial landscape region from ethnohistoric mapping",
      "prov:type": "Dataset",
      "kfm:source": "Historical Atlas 1899",
      "kfm:stac_item": "kfm-archaeology-cultural-landscapes-hatlas1899-v1"
    },
    "generalized": {
      "prov:label": "Generalized region (H3 level 6)",
      "prov:type": "Dataset",
      "kfm:h3_resolution": 6,
      "care:notes": "Exact cultural boundaries removed; generalized to interaction-scale footprint."
    },
    "processed": {
      "prov:label": "Processed cultural landscape dataset v2",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v2",
      "kfm:stac_item": "kfm-archaeology-cultural-landscapes-region-v2"
    }
  },
  "prov:Activity": {
    "generalization": {
      "prov:type": "Generalization",
      "prov:startTime": "2025-10-14T13:22:00Z",
      "prov:endTime": "2025-10-14T14:05:00Z",
      "kfm:steps": [
        "H3 grid derivation (res=6)",
        "Polygon simplification (Douglas-Peucker, tolerance=1500m)"
      ]
    },
    "review": {
      "prov:type": "Review",
      "prov:label": "FAIR+CARE ethics & tribal cultural review",
      "prov:endTime": "2025-10-15T17:40:00Z"
    }
  },
  "prov:Agent": {
    "analyst": {
      "prov:label": "A. Barta",
      "prov:type": "Person"
    },
    "faircare": {
      "prov:label": "FAIR+CARE Council",
      "prov:type": "Group"
    },
    "tribal": {
      "prov:label": "Tribal Heritage Office",
      "prov:type": "Group"
    }
  },
  "prov:wasDerivedFrom": [
    { "prov:generatedEntity": "generalized", "prov:usedEntity": "raw" },
    { "prov:generatedEntity": "processed", "prov:usedEntity": "generalized" }
  ],
  "prov:wasGeneratedBy": [
    { "prov:entity": "generalized", "prov:activity": "generalization" },
    { "prov:entity": "processed", "prov:activity": "review" }
  ],
  "care:sensitivity": "generalized",
  "care:review": "tribal",
  "care:notes": "Generalization required to protect culturally sensitive landscapes.",
  "care:visibility_rules": "polygon-generalized"
}
~~~

---

## 🧠 Graph, Story Node & Focus Mode Integration

### Knowledge Graph (Neo4j)

From each provenance log, the ETL/graph loaders materialize:

- **Nodes**
  - `LandscapeRegion`
  - `GeneralizedRegion`
  - `ProcessedLandscapeLayer`
  - `ProvenanceActivity`
  - `ReviewEvent`
  - `CulturalSensitivityLevel`
  - `SourceInstitution`

- **Edges**
  - `GENERALIZED_FROM` (processed/generalized → raw)
  - `PRODUCED_BY` (entities → activities)
  - `REVIEWED_BY` (activities → agents)
  - `HAS_SENSITIVITY` (entities → sensitivity level)
  - `HAS_PROVENANCE` (dataset/STAC Item → provenance root entity)

### Story Nodes

Provenance drives:

- Narrative transparency for **how** landscapes were derived and generalized  
- Explicit cultural attribution and acknowledgment  
- Clear separation between **data** and **interpretive overlays**  
- Provenance-backed context for movement, interaction, and territory Story Nodes  

Story Nodes must reference provenance via stable identifiers so Focus Mode can surface:

- “Why is this generalized?”  
- “Who reviewed this?”  
- “What sources back this boundary?”  

### Focus Mode v2/v3

Focus Mode uses provenance to:

- Render **explainability overlays** (e.g., on-hover provenance chips)  
- Inject ethical flags and CARE sensitivity markers into side panels  
- Filter views by sensitivity or review status (e.g., “show only FAIR+CARE-reviewed layers”)  
- Drive model constraints (e.g., prevent de-generalization or speculative expansion beyond provenance scope)

---

## 🧪 Validation & CI/CD Requirements

Provenance logs must pass the following before being accepted:

- **Structural validation**
  - PROV-O JSON-LD shape validation  
  - CARE field presence and value checks  
- **KFM archaeology provenance rules**
  - Mandatory entities/activities/agents present  
  - H3/generalization parameters recorded where applicable  
- **Metadata ↔ STAC ↔ provenance crosswalk**
  - STAC Item IDs in provenance must resolve to existing STAC records  
  - Temporal coverage & spatial footprint consistent with catalog metadata  

### CI Workflows

The following CI jobs (names may vary per repo) must succeed:

- `metadata-validate.yml`  
- `artifact-stac-validate.yml`  
- `faircare-audit.yml`  
- `archaeology-provenance-validate.yml` (or equivalent)

**CI blocks ingestion if:**

- No provenance log exists for a new or updated cultural landscape dataset  
- CARE sensitivity is missing or set to a forbidden value for public artifacts  
- No tribal review is recorded for protohistoric/historic contexts flagged as requiring it  
- Spatial generalization steps are absent or undocumented  
- STAC ↔ provenance references do not align

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Cultural Landscape WG · FAIR+CARE Council   | Aligned with KFM-MDP v11.2.2; added CI/validation requirements & graph/Story Node integration; updated release metadata to v11.2.3. |
| v10.4.0  | 2025-11-17 | Cultural Landscape WG · FAIR+CARE Council   | Added complete provenance logging standard with CARE + PROV-O integration. |
| v10.0.0  | 2025-11-10 | Landscape Provenance Team                   | Initial directory scaffolding and baseline provenance expectations.     |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.2 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cultural Landscape Datasets](../README.md)

</div>
