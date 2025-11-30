---
title: "💧 KFM v11.2.2 — Hydrology Story Node Templates"
path: "docs/story-nodes/domains/hydrology/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Hydrology Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:hydrology:templates:v11.2.2"
semantic_document_id: "kfm-storynodes-hydrology-templates"
event_source_id: "ledger:storynodes/hydrology/templates"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Template Directory README"
intent: "kfm-hydrology-storynode-templates"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 hydrology templates"
---

<div align="center">

# 💧 **Hydrology Story Node Templates (KFM v11)**  
### *Authoring Patterns · Schema Skeletons · Relation Models*  

`docs/story-nodes/domains/hydrology/templates/README.md`

**Purpose**  
Provide **authoring templates**, **schema skeletons**, and **relation-pattern guidance**  
for constructing hydrology Story Nodes safely, accurately, and consistently.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/hydrology/templates/
├── 📄 README.md                         # Template overview (this file)
├── 📝 story-node-hydrology.md           # Markdown authoring template
├── 🧩 story-node-hydrology.json         # JSON schema-aligned skeleton
└── 🔗 relation-patterns.md              # Hydrology-specific graph relations
~~~

These files must remain aligned with:

- `story-node.schema.json`  
- hydrology domain rules  
- Focus Mode v3 requirements  
- STAC/DCAT specifications  
- PROV-O lineage rules  
- CF conventions for hydrology variables  
- CRS/GeoSPARQL alignment

---

## 📘 Overview

Hydrology Story Node templates support narratives describing:

- **Flood events** (flash floods, riverine peaks, inundation footprints)  
- **Streamflow events** (rapid rises, seasonal maxima/minima, anomalies)  
- **Groundwater trends** (declines, recharge intervals, GRACE anomalies)  
- **Watershed-scale processes** (runoff, basin hydrology, snowmelt)  
- **Hydro-climate links** (drought, extreme precipitation, soil moisture interplay)  
- **Water cycle behaviors** in Kansas (evapotranspiration, infiltration, surface retention)

Templates enforce:

- public-safe spatial generalization  
- scientifically neutral narrative structure  
- correct hydrology terminology (glossary-backed)  
- correct CF units and variable naming  
- clear distinction between **observed** vs **modeled** hydrology  
- provenance completeness for USGS/NWM/GRACE/GLDAS datasets  
- Focus Mode compatibility

---

## 🧱 Template Types

### 📝 **Markdown Template — `story-node-hydrology.md`**
Contains sections for:

- hydrologic context  
- observation vs modeling  
- spacetime definition  
- uncertainty language  
- STAC/DCAT dataset links  
- PROV-O provenance blocks  
- hydrologic impact pathways  
- Focus Mode cue blocks

### 🧩 **JSON Template — `story-node-hydrology.json`**
Includes:

- `type: "story-node"`  
- `id`, `title`, `summary`  
- `spacetime.when` → ISO interval + precision  
- `spacetime.geometry` → watershed, river corridor, region, or inundation polygon  
- hydrology-specific fields (`hydrology.context`, `flow_metrics`, etc.)  
- `relations[]` using hydrology relation patterns  
- `provenance[]`  
- optional STAC `assets[]` (inundation masks, flow rasters, water indices)

### 🔗 **Relation Patterns — `relation-patterns.md`**
Defines hydrology-safe graph patterns:

- `about` → hydrologic event  
- `references` → USGS/NWM datasets  
- `derived-from` → model outputs  
- `linked-to-watershed` → HUC/watershed regions  
- `analog-of` → historical flood comparisons  
- `impacts` → soil/ecology/agriculture nodes  
- `counterpoint` → updated hydrologic interpretations

---

## 🧬 Compliance Notes

Hydrology templates must uphold:

- **KFM-MDP v11.2.2**  
- **STAC 1.x** for spatiotemporal hydro assets  
- **DCAT 3.0** dataset metadata  
- **CF conventions** for hydrology variables/units  
- **GeoSPARQL** spatial semantics  
- **OWL-Time** temporal semantics  
- **PROV-O** for dataset lineage  
- Environmental ethics & public safety rules

They must avoid:

- parcel-level or property-level implications  
- personal data  
- unsupported claims about flood causes  
- political or normative framing

---

## 🧪 CI/CD Notes

Any update to this directory triggers:

- Story Node schema validation  
- Markdown protocol validation  
- CF variable/unit checks  
- Provenance consistency tests  
- STAC/DCAT regression tests  
- Narrative governance checks (Focus Mode safety)  

All changes require domain review + FAIR+CARE Council approval.

---

## 🕰️ Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed hydrology template directory added.          |
| v11.2.1 | 2025-11-29 | Added base Markdown/JSON templates + relation-pattern scaffold. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
