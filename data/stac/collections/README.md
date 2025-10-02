<div align="center">

# 🗂️ Kansas-Frontier-Matrix — STAC Collections  
`data/stac/collections/`

**Mission:** Collections are the **containers** of the STAC catalog.  
They define shared metadata — **spatial/temporal extent, providers, license, keywords** —  
and group related STAC Items into **discoverable, reproducible sets**.  

📌 **Upward:** Collections link to the **root catalog** (`../catalog.json`).  
📌 **Downward:** Collections link to their STAC **Items** (`../items/<collection>/*.json`).  
📌 **Purpose:** Provide **context, grouping, and searchability** across the Kansas-Frontier-Matrix ecosystem.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)  

</div>

---

## 📂 Contents

- [Structure](#-structure)  
- [Authoring Checklist](#-authoring-checklist)  
- [Template Collection](#-template-collection)  
- [Integration Points](#-integration-points)  
- [Validation](#-validation)  
- [Common Pitfalls](#-common-pitfalls)  
- [TL;DR](#-tldr)  

---

## 🏗 Structure

```text
data/stac/collections/
├── dem.json          # Digital Elevation Models
├── topo.json         # Historic topographic maps
├── overlays.json     # DEM/map overlays, soils, styled rasters
└── vectors.json      # Vectors (treaties, trails, towns, railroads…)

../catalog.json              → root catalog that references these collections  
../items/<collection>/*.json → STAC Items grouped by these collections  
*.json                       → must follow STAC 1.0.0 Collection spec  


⸻

🧾 Authoring Checklist
	1.	STAC compliance
	•	Required header:

{ "stac_version": "1.0.0", "type": "Collection" }


	2.	IDs
	•	Lowercase, short, descriptive.
	•	Examples: dem, topo, overlays, vectors.
	3.	Extent
	•	Must include both:
	•	Spatial extent → union bbox of all Items.
	•	Temporal extent → earliest to latest datetime across Items.
	4.	Keywords
	•	Thematic tags for search/discovery.
	•	Example: "keywords": ["DEM", "LiDAR", "elevation", "Kansas"]
	5.	Providers
	•	Credit upstream producers/licensors.
	•	Example:

"providers": [
  { "name": "USGS", "roles": ["producer", "licensor"], "url": "https://www.usgs.gov/" }
]


	6.	License
	•	Use SPDX identifiers.
	•	Examples: "CC-BY-4.0", "PDDL-1.0", "public-domain".
	7.	Links
	•	Every Collection must include:
	•	rel: root → back to ../catalog.json
	•	rel: item → forward to each contained Item
	•	rel: derived_from → provenance (../../provenance/registry.json)

⸻

📑 Template Collection

{
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "type": "Collection",
  "id": "dem",
  "title": "Digital Elevation Models (Kansas)",
  "description": "DEM datasets for Kansas including 1m LiDAR-derived surfaces.",
  "license": "public-domain",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.59, 40.00]] },
    "temporal": { "interval": [["2018-01-01T00:00:00Z", "2020-12-31T23:59:59Z"]] }
  },
  "providers": [
    {
      "name": "USGS",
      "roles": ["producer", "licensor"],
      "url": "https://www.usgs.gov/"
    }
  ],
  "keywords": ["DEM", "elevation", "LiDAR", "Kansas"],
  "links": [
    { "rel": "root", "href": "../catalog.json", "type": "application/json" },
    { "rel": "item", "href": "../items/dem/ks_1m_dem_2018.json", "type": "application/geo+json" },
    { "rel": "item", "href": "../items/dem/ks_1m_dem_2020.json", "type": "application/geo+json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#ks_1m_dem", "type": "application/json" }
  ]
}


⸻

🔗 Integration Points
	•	Provenance: Collections link back to data/provenance/registry.json.
	•	Web Viewer: Collections inform grouping in web/config/layers.schema.json.
	•	Makefile: make stac and make stac-validate refresh and check collections.
	•	Experiments (MCP): docs/experiments/** cite Collection IDs for reproducibility.

⸻

✅ Validation

Local

pre-commit run stac-validate --all-files

Manual

kgt validate-stac data/stac/collections --no-strict

CI
	•	.github/workflows/stac-validate.yml enforces schema compliance.
	•	Failures block merge until fixed.

⸻

⚠️ Common Pitfalls
	•	❌ Missing extent → every Collection must declare both spatial and temporal.
	•	❌ Keywords omitted → reduces discoverability.
	•	❌ Missing provider attribution → always credit producers/licensors.
	•	❌ Item links missing → all contained Items must be explicitly linked.
	•	❌ Wrong license string → must be SPDX-compliant or "public-domain".

⸻

TL;DR
	•	Collections = grouped metadata for Items.
	•	Must include ID, title, description, license, extent, keywords, providers.
	•	Must link back to root and forward to Items.
	•	Validate with pre-commit or CI before merge.

✅ Collections ensure Items are grouped, discoverable, attributed, and reproducible.