---
title: "📖 KFM SOP — Story Node v3 Generation & Narrative Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/storynode_generation.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · Narrative Governance Team"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "SOP"
intent: "storynode-generation"
semantic_document_id: "kfm-sop-storynode-generation"
doc_uuid: "urn:kfm:mcp:sop:storynode-generation:v11.0.0"
machine_extractable: true
classification: "Governed Narrative Procedure"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📖 **KFM Standard Operating Procedure — Story Node v3 Generation (v11 LTS)**  
`mcp/sops/storynode_generation.md`

**Purpose:**  
Define the **governed, deterministic, explainable, and CARE-compliant** procedure for generating, validating, and publishing **Story Node v3** entities within the Kansas Frontier Matrix v11 system.

Story Nodes are the **primary narrative units** connecting people, places, events, documents, and datasets via **geospatial, temporal, and narrative context**.

</div>

---

## 📘 1. Scope

This SOP applies to:

- All **new Story Node v3** generation  
- **AI-assisted narrative drafting** (Focus Mode v3, CrewAI workers)  
- **Manual historian/archaeologist contributions**  
- Story Node updates triggered by:
  - New datasets  
  - New archive integrations  
  - New pipeline outputs  
  - New heritage or hydrology discoveries  

This SOP also governs **validation**, **CARE compliance**, **H3-masking**, and **graph ingestion** for Story Nodes.

---

## 📦 2. Inputs

### Required Inputs
| Input | Description |
|-------|-------------|
| Source datasets | STAC/DCAT registered datasets with lineage |
| Graph entities | People, places, events, documents, datasets |
| Geospatial geometry | GeoJSON + bounding H3 cells if sensitive |
| Temporal info | OWL-Time instant/interval |
| Provenance | PROV-O activity chain |
| Narrative drafts | AI or human-curated text |
| Metadata contracts | Story Node schema (JSON schema & SHACL) |

### Optional Inputs
- Images (with rights & license metadata)  
- Maps / overlays for context panels  
- Cross-links to related Story Nodes  

---

## 🧩 3. Required Story Node v3 Structure

Each Story Node must follow the **official v3 schema**:

### Mandatory Components

#### **1. id**
Stable UUID, ARK, or DOI.

#### **2. type**
Must be `"story-node"`.

#### **3. title**
Human-readable, concise, WCAG-accessible.

#### **4. narrative**
- `body`: factual narrative (no speculation)  
- `format`: markdown or text  
- `alternates`: language/audience variants  
- `media`: referenced images, maps, artifacts  

#### **5. spacetime**
- `geometry`: GeoJSON (masked if sensitive)  
- `bbox`: optional  
- `crs`: default EPSG:4326  
- `place_labels`: human-readable locations  
- `when`: OWL-Time start/end  

#### **6. relations**
Typed edges to graph entities:  
`follows`, `references`, `part-of`, `influenced-by`, etc.

#### **7. stac alignment**
Optional: link to STAC assets/collections.

---

## 🛠️ 4. Procedure — Step-by-Step (Deterministic)

### **4.1 Step 1 — Extract & Prepare Context**

- Query Neo4j for 2–3 hop neighborhood  
- Collect facts, dates, locations, actors  
- Collect dataset provenance (STAC/DCAT)  
- Collect relevant documents, images, or artifacts  

Store in:

```
data/work/storynodes/context/<node-id>.json
```

---

### **4.2 Step 2 — Create Narrative Draft (AI + Human)**

#### AI Component:
Use CrewAI + Focus Mode v3 to produce:

- Context Panel  
- Timeline Panel  
- Map Panel  

AI narrative MUST NOT:

- Speculate  
- Infer genealogies  
- Reveal restricted coordinates  
- Misrepresent cultural groups  
- Use colonial or biased language  

AI must cite sources for every fact.

#### Human Component:
Domain expert edits for:

- Accuracy  
- Neutral tone  
- Cultural sensitivity  
- Clarity & accessibility  
- Removal of speculation  

---

### **4.3 Step 3 — Apply CARE & Sovereignty Filters**

Required checks:

- Sensitive site? → **Apply H3 masking**  
- Tribal relevance? → **Sovereignty tag**  
- Story involves trauma/conflict? → Apply **narrative ethics style guide**  
- Heritage material? → Consult FAIR+CARE Council  

Metadata annotations:

```
"care_classification": "Tier A/B/C",
"sovereignty_notes": "...",
"masking_method": "H3-R7"
```

---

### **4.4 Step 4 — Build Story Node v3 JSON**

Use official schema:

```
schemas/story-node.schema.json
schemas/shacl/storynode-v3-shape.ttl
```

Populate:

- `id`
- `title`
- `summary`
- `narrative`
- `spacetime`
- `relations`
- `stac` references (if any)

Run:

```
schema-lint-v11
shacl-validate-v11
```

---

### **4.5 Step 5 — Validate Against Knowledge Graph**

- Check all relations reference existing graph entities  
- Validate geometry against GeoSPARQL  
- Validate OWL-Time intervals  
- Validate semantic roles (CIDOC-CRM mapping)  
- Validate that Story Node does not conflict with other verified nodes  

Flag collisions to human reviewers.

---

### **4.6 Step 6 — Lineage Logging (PROV-O + OpenLineage v2.5)**

Record:

- `prov:used` (datasets, documents, models)  
- `prov:wasGeneratedBy` (AI steps, human reviews)  
- `prov:wasAssociatedWith` (analysts, reviewers)  
- Seeds, model versions  
- Any H3 masking applied  

Write lineage:

```
data/provenance/storynodes/<node-id>.json
```

Emit OpenLineage:

```
storynode.generate
```

---

### **4.7 Step 7 — Commit Story Node & Publish**

Output to:

```
data/processed/storynodes/<id>.json
```

Then:

- Register STAC Item (if spatial raster context exists)  
- Insert Story Node into Neo4j graph  
- Generate change record in governance ledger  
- Run automated Focus Mode v3 preview  
- Human approval required for final publishing  

---

## 🧭 5. Verification Checklist

### Must Pass:

- ✔ Story Node JSON schema  
- ✔ SHACL shape  
- ✔ CARE & sovereignty review  
- ✔ H3 masking where required  
- ✔ Narrative ethics compliance  
- ✔ Provenance (PROV-O + OpenLineage)  
- ✔ STAC/DCAT alignment  
- ✔ Neo4j ingestion tests  
- ✔ Accessibility (WCAG 2.1 AA+)  
- ✔ CI validation (`mcp-validate.yml`)

Any failure → blocked until corrected.

---

## 🧯 6. Failure Modes & Recovery

### Common Failures
- Unverified claim or speculative narrative  
- Sensitive coordinate exposure  
- Relation to missing graph entities  
- Temporal inconsistencies  
- Ambiguous or incorrect historical details  
- Incomplete provenance  

### Recovery
- Correct or remove offending narrative  
- Apply H3 masking or narrative redaction  
- Update graph references  
- Add or revise provenance  
- Acquire cultural review if needed  
- Re-run schema validations  

High-risk cases → escalate to **FAIR+CARE Council**.

---

## 📊 7. Telemetry & Sustainability

Record:

- Energy Wh  
- Carbon gCO₂e  
- Pipeline duration  
- I/O volume  
- Model inference energy (if AI used)

Stored in:

```
releases/<version>/mcp-sops-telemetry.json
```

Used for governance dashboards & sustainability reporting.

---

## 🕰 8. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial Story Node v3 governed SOP for KFM-MCP v11. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MCP-DL v6.3  
Diamond⁹ Ω / Crown∞Ω Certified · FAIR+CARE Compliant · Narrative Governance Enforced  

</div>
