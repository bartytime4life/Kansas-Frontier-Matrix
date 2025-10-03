<div align="center">

# 🔗 Kansas Frontier Matrix — Integration Docs (`/docs/integration/`)

**Mission:** Document how external datasets, archives, and APIs are  
**integrated into the Kansas Frontier Matrix (KFM)** — ensuring consistency,  
provenance, and cross-domain interoperability.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Data Standards](https://img.shields.io/badge/Standards-STAC%201.0%20%7C%20CIDOC%20CRM%20%7C%20OWL--Time-green)](README.md)  

</div>

---

## 🎯 Purpose

The `/docs/integration/` directory provides **developer and researcher guides**  
for connecting **external sources** (GIS archives, treaties, climate records, oral histories)  
into the KFM knowledge hub.  

This directory focuses on:  
- 🌐 **External data ingestion** — APIs, portals, archives.  
- 📜 **Metadata alignment** — STAC, DCAT, CIDOC CRM, OWL-Time.  
- 🔄 **Cross-domain linking** — connecting climate ↔ history ↔ geography.  
- 🧩 **Dataset-to-graph mapping** — ensuring entities are linked into Neo4j.  
- ✅ **Reproducibility** — every integration documented with provenance.  

---

## 📚 Contents

```text
docs/integration/
├── README.md                 # Index (this file)
├── gis-archive.md            # Integration with Kansas GIS Archive & DASC
├── deeds.md                  # Land deeds, patents, Register of Deeds integration
├── climate-hazards.md        # NOAA, FEMA, drought, tornado, flood datasets
├── oral-histories.md         # Indigenous & community oral history ingestion
├── treaties.md               # Indian land cessions, Royce maps, treaty texts
├── metadata-standards.md     # STAC, DCAT, CIDOC CRM, OWL-Time mappings
├── workflows.md              # Step-by-step integration SOPs
└── reviews/                  # Integration ADRs & peer-reviewed notes


⸻

🗂️ Key Docs
	•	gis-archive.md → Fetching and converting Kansas GIS datasets ￼.
	•	deeds.md → Historical land deeds & homestead integration ￼.
	•	climate-hazards.md → Climate, flood, tornado, and disaster data ￼ ￼.
	•	oral-histories.md → Methods for preserving and linking oral narratives ￼.
	•	treaties.md → Land cessions, treaty texts, and Royce polygon GIS layers ￼.
	•	metadata-standards.md → How KFM aligns STAC, CIDOC CRM, OWL-Time ￼ ￼.
	•	workflows.md → SOPs for reproducible dataset integration.

⸻

🧭 Usage
	1.	Add a new dataset → Document in /docs/integration/* before writing code.
	2.	Check metadata standards → Ensure mapping to STAC, DCAT, or ontologies.
	3.	Run validation → Use /tools/validate_stac.py and schema tests under /tests/.
	4.	Log provenance → Record source, license, checksum, and integration steps.
	5.	Review → Submit changes via PR with ADR-style notes in /reviews/.

⸻

🔗 Related Docs
	•	Data Architecture
	•	File & Repo Layout
	•	Design Docs
	•	Glossary

⸻


<div align="center">


🔗 Integration is where Kansas’s fragmented history becomes connected.
Every dataset must be traceable, interoperable, and auditable.

</div>