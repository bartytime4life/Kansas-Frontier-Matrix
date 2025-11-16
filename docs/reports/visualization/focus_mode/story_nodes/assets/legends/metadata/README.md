---
title: "📘 Kansas Frontier Matrix — Legend Metadata Root Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/README.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reports-visualization-focus-legends-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Legend Metadata Root Overview**  
`docs/reports/visualization/focus_mode/story_nodes/assets/legends/metadata/README.md`

**Purpose:**  
Serve as the **index and governance anchor** for all metadata definitions across climate, hydrology, landcover, archaeological, and event symbol systems used in Focus Mode and Story Nodes.

<img alt="Metadata" src="https://img.shields.io/badge/Metadata-Legends-blue" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0%20Aligned-purple" />

</div>


---

## 📚 Overview

This directory is the **root metadata hub** for all legend categories within the Kansas Frontier Matrix (KFM).  
It organizes and governs metadata for:

- Climate symbols  
- Hydrology symbols  
- Landcover symbols  
- Event symbols  
- Archaeological symbols  

Each metadata group ensures:

- Canonical symbol identity  
- FAIR+CARE-aligned semantics  
- Correct SVG/PNG asset linkage  
- STAC metadata interoperability  
- Story Node usage governance  
- Reproducible rendering across KFM visual systems  

Any legend symbol used in Focus Mode, Story Nodes, or map overlays must have metadata stored in the appropriate subdirectory here.

---

### 🗂️ Directory Layout

```plaintext
metadata/
├── README.md                               # This index document
├── archaeological/                         # Archaeological symbol metadata
│   ├── README.md
│   ├── archaeological-symbols.json
│   ├── archaeological-symbols.stac.json
│   ├── archaeological-symbols-story-nodes.json
│   └── examples/
│
├── hydrology/                              # Hydrology symbol metadata
│   ├── README.md
│   ├── hydrology-symbols.json
│   ├── hydrology-symbols.stac.json
│   ├── hydrology-symbols-story-nodes.json
│   └── examples/
│
├── climate/                                # Climate symbol metadata
│   ├── README.md
│   ├── climate-symbols.json
│   ├── climate-symbols.stac.json
│   ├── climate-symbols-story-nodes.json
│   └── examples/
│
├── landcover/                              # Landcover & ecological symbol metadata
│   ├── README.md
│   ├── landcover-symbols.json
│   ├── landcover-symbols.stac.json
│   ├── landcover-symbols-story-nodes.json
│   └── examples/
│
├── events/                                 # Historic, cultural, political event symbols
│   ├── README.md
│   ├── event-symbols.json
│   ├── event-symbols.stac.json
│   ├── event-symbols-story-nodes.json
│   └── examples/
│
└── metadata/                               # Symbol metadata and definitions
    ├── README.md
    ├── field_definitions.md
    └── examples/
````

---

### 🧱 Metadata Requirements (All Categories)

Each symbol metadata file must define:

* **id** — canonical key
* **category** — thematic grouping
* **label** — human-readable name
* **description** — semantic meaning
* **svg** — path to SVG icon
* **png** — optional PNG complement
* **emoji** — fallback representation
* **severity / type / landcover_class / event_type** (domain-dependent)
* **data_mapping** (for scientific symbols)
* **cultural / ecological sensitivity** (CARE labels)
* **story node usage rules**

Example template (indented, not fenced):

```
{
  "id": "<symbol_id>",
  "category": "<category>",
  "label": "<Label>",
  "description": "<Meaning>",
  "svg": "../svg/<symbol_id>.svg",
  "png": "../png/<symbol_id>@2x.png",
  "emoji": "<emoji>",
  "cultural_sensitivity": "public"
}
```

---

### 🔗 STAC Integration Requirements

STAC metadata files must:

* Declare assets with `roles: ["legend", "symbol"]`
* Provide descriptive titles
* Maintain link to `kfm-legends`
* Include CARE-compliant context metadata
* Stay synchronized with registry entries

Example (indented):

```
{
  "stac_version": "1.0.0",
  "type": "Item",
  "id": "<legend-id>",
  "collection": "kfm-legends",
  "assets": {
    "<symbol_id>_svg": {
      "href": "../svg/<symbol_id>.svg",
      "type": "image/svg+xml",
      "roles": ["legend", "symbol"]
    }
  }
}
```

---

### 🧠 Story Node Integration Requirements

Each symbol metadata subdirectory includes Story Node bindings controlling:

* Header / timeline icon placement
* Badge appearance rules
* Emoji fallbacks
* Context-specific semantic cues
* CARE visibility and cultural governance

Example (indented):

```
{
  "<symbol_id>": {
    "label": "<Label>",
    "badge": true,
    "emoji": "<emoji>",
    "contexts": ["ecology", "history", "climate"],
    "display_rules": {
      "timeline": true,
      "header": false
    }
  }
}
```

---

### 🧪 Validation & CI Requirements

Symbol metadata across **all categories** must pass:

* JSON Schema validation
* STAC schema validation
* Path/link existence checks
* Snapshot linkage (in symbol test directories)
* CARE label governance
* Story Node mapping validation

Single-run validation entry point (indented):

```
make test-legends-all
```

---

### 🕒 Version History

| Version | Date       | Author      | Notes                                                               |
| ------- | ---------- | ----------- | ------------------------------------------------------------------- |
| v10.2.3 | 2025-11-13 | KFM Docs AI | Initial root legend-metadata overview, fully memory-rule compliant. |
| v10.2.2 | 2025-11-12 | KFM Docs AI | Added optional integration examples for STAC and DCAT.              |
