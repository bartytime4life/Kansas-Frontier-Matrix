---
title: "🧩 Kansas Frontier Matrix — Story Node Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/metadata/field_definitions.md"
version: "v10.2.0"
last_updated: "2025-11-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focusmode-storynode-fielddefs-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Story Node Field Definitions**
`docs/reports/visualization/focus_mode/story_nodes/metadata/field_definitions.md`

**Purpose:**  
Provide **exhaustive, authoritative definitions** for every metadata field used in Kansas Frontier Matrix (KFM) Story Nodes.  
This reference ensures consistent implementation, schema validation, ontology alignment, and FAIR+CARE governance across all Focus Mode narratives.

![Docs](https://img.shields.io/badge/Docs·MCP-v6.3-blue)
![License](https://img.shields.io/badge/License-CC--BY--4.0-green)
![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

This document expands the Story Node metadata model by describing:

- Field purpose  
- Expected data types  
- Required vs optional status  
- Ontology & standards mapping (CIDOC CRM, OWL-Time, DCAT, GeoJSON, schema.org)  
- Validation rules  
- FAIR+CARE governance expectations  

Every Story Node must conform to these definitions to pass CI validation (`faircare-validate.yml`, `stac-validate.yml`, `docs-lint.yml`).

---

## 🧱 Core Fields

### **`id`**
- **Type:** `string`
- **Required:** ✅
- **Description:** Unique Story Node identifier.
- **Format:** `storynode_<topic>_<year or epoch>`
- **Example:** `"storynode_flood_epoch_1935"`
- **Ontology:** `dct:identifier`
- **Validation:** Must be globally unique across all Story Node directories.

---

### **`title`**
- **Type:** `string`
- **Required:** ✅
- **Description:** Human-readable narrative title displayed in Focus Mode.
- **Example:** `"Great Plains Flood Epoch of 1935"`
- **Ontology:** `dct:title`
- **Validation:** ≤ 120 characters.

---

### **`summary`**
- **Type:** `string`
- **Required:** ✅
- **Description:** Short textual description used in Focus Mode UI cards.
- **Ontology:** `dct:description`
- **Validation:** Max length: 350 chars. No HTML. No personally identifiable information (PII).

---

## ⏳ Temporal Fields

### **`temporal.start`**
- **Type:** `string` (ISO 8601)
- **Required:** ✅
- **Description:** Start of the Story Node time interval.
- **Ontology:** `time:hasBeginning`
- **Validation:** Must precede or equal `temporal.end`.

### **`temporal.end`**
- **Type:** `string` (ISO 8601)
- **Required:** ⚙️ (required unless Story Node is an instant)
- **Ontology:** `time:hasEnd`
- **Validation:** Must be ≥ `temporal.start`.

### **`temporal.ontology`**
- **Type:** `string`
- **Required:** ⚙️
- **Allowed:** `"OWL-Time"`, `"schema.org/temporalCoverage"`, `"CIDOC-CRM"`
- **Purpose:** Identifies the semantic ontology used to interpret temporal fields.

---

## 🗺 Spatial Fields

### **`spatial.geometry`**
- **Type:** GeoJSON (Polygon, LineString, Point)
- **Required:** ⚙️ (depending on narrative type)
- **Ontology:** `geo:geometry`, `dct:spatial`
- **Validation:** Must be valid GeoJSON; CRS = `EPSG:4326`.

### **`spatial.bbox`**
- **Type:** array of 4 floats `[W, S, E, N]`
- **Required:** ⚙️
- **Use:** Fast map preview & spatial indexing.
- **Validation:** W < E, S < N.

### **`spatial.crs`**
- **Type:** `string`
- **Required:** ⚙️
- **Default:** `"EPSG:4326"`

---

## 🧩 Narrative Entity Fields

### **`entities`** (array)
List of entities (people, groups, events, organizations, ecological processes, etc.) relevant to the narrative.

Each item:

#### **`entities[i].type`**
- **Type:** `string`
- **Ontology mapping:**
  - Person → `crm:E21_Person`
  - Group → `crm:E74_Group`
  - Event → `crm:E5_Event`
  - Place → `crm:E53_Place`
  - EcologicalProcess → KFM Eco Ontology (internal)
- **Required:** ⚙️

#### **`entities[i].name`**
- **Type:** `string`
- **Required:** ⚙️
- **Validation:** ≤ 100 chars.

---

## 🧬 Provenance Fields

### **`provenance.datasets`**
- **Type:** array of dataset identifiers
- **Required:** ✅
- **Description:** Dataset IDs that substantiate the Story Node.
- **Ontology:** `dct:source`, `dcat:Dataset`
- **Validation:** Dataset IDs must exist in `data/processed/**`.

---

### **`provenance.citations`**
- **Type:** array of string citations
- **Required:** ⚙️
- **Formats accepted:** APA, MLA, Chicago, DOI URLs, dataset citations.
- **Ontology:** `cito:cites`

---

### **`provenance.lineage`**
- **Type:** `string`
- **Required:** ⚙️
- **Description:** Processing steps, data transformations, or smoothing applied.
- **Ontology:** `prov:wasGeneratedBy`

---

## 🖼 Visualization Fields

### **`visualization.map_2d`**
- **Type:** `string` (filename)
- **Required:** ⚙️
- **Formats:** `.png`, `.svg`, `.webp`

### **`visualization.scene_3d`**
- **Type:** `string`
- **Formats:** `.glb`, `.gltf`, `.czml`

### **`visualization.overlay`**
- **Type:** `string`
- **Use:** Linked vector overlays for Focus Mode.

---

## ⚖️ CARE Fields (Ethical Governance)

### **`care.status`**
- **Type:** `string`
- **Required:** ⚙️
- **Values:** `approved`, `revision`, `restricted`

### **`care.reviewer`**
- **Type:** `string`
- **Description:** Entity responsible for ethical sign-off.

### **`care.notes`**
- **Type:** `string`
- **Description:** Explanation of generalization, masking, or CARE decisions.

---

## 🧮 Validation Requirements

| Validation Type | Requirement |
|----------------|-------------|
| Schema | Must pass `schema_v10.json` |
| FAIR+CARE | CARE block required for culturally or ethically sensitive narratives |
| Provenance | At least 1 dataset + 1 citation |
| Temporal | Must have valid interval or instant |
| Spatial | CRS must be 4326 if spatial fields exist |
| Visualization | If provided, file extensions must be valid formats |

---

## 🧪 Minimal Example

```json
{
  "id": "storynode_climate_turning_point_1956",
  "title": "The 1956 Kansas Heatwave",
  "summary": "A pivotal climate event reshaping agricultural patterns.",
  "temporal": {
    "start": "1956-06-01T00:00:00Z",
    "end": "1956-09-01T00:00:00Z",
    "ontology": "OWL-Time"
  },
  "provenance": {
    "datasets": ["noaa_temp_1900_2025"],
    "citations": ["NOAA Climate Records (1956)"]
  },
  "updated": "2025-11-12T14:10:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.2.0 | 2025-11-12 | KFM Focus Mode Team | Full field definition reference including ontology, validation, and FAIR+CARE requirements. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Metadata](README.md) · [⬅ Story Node Index](../README.md)

</div>

