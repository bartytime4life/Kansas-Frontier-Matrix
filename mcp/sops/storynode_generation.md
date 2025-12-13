---
title: "📖 KFM SOP — Story Node v3 Generation & Narrative Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/sops/storynode_generation.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · MCP Board · FAIR+CARE Council · Narrative Governance Team"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "SOP"
header_profile: "standard"
footer_profile: "standard"
intent: "storynode-generation"
semantic_document_id: "kfm-sop-storynode-generation"
doc_uuid: "urn:kfm:mcp:sop:storynode-generation:v11.0.0"
event_source_id: "ledger:kfm:mcp:sop:storynode-generation:v11.0.0"
machine_extractable: true

classification: "Governed Narrative Procedure"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-sops-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-sops-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "genealogical-inference"
  - "sacred-site-inference"
  - "sensitive-coordinate-exposure"
  - "governance-override"
  - "fabricate-provenance"

provenance_chain:
  - "mcp/sops/storynode_generation.md@v11.0.0"
---

<div align="center">

# 📖 **KFM SOP — Story Node v3 Generation & Narrative Governance (v11 LTS)**
`mcp/sops/storynode_generation.md`

**Purpose**  
Define the governed, deterministic, explainable, and CARE-compliant procedure for generating, validating, and publishing **Story Node v3** entities within Kansas Frontier Matrix v11. Story Nodes are the primary narrative units connecting people, places, events, documents, and datasets via geospatial, temporal, and evidence-led narrative context.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/StoryNode-v3-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Sovereignty-Enforced-critical" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[🧪 MCP Experiments](../experiments/README.md) ·
[🧬 Model Cards](../model_cards/README.md) ·
[🏛️ Governance](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

---

## 📘 Overview

### 🎯 Scope
This SOP applies to:
- 🆕 all new Story Node v3 creation
- 🤖 AI-assisted drafting (Focus Mode v3, CrewAI workers)
- 🧑‍🏫 manual domain expert authoring (historians, archaeologists, hydrologists)
- 🔁 updates triggered by new datasets, new archive ingests, new pipeline outputs, or governance/masking changes

This SOP governs:
- 🧾 evidence requirements and narrative boundaries (no speculation)
- 🪶 sovereignty + CARE routing and masking decisions (H3 generalization where required)
- ✅ validation gates (schema + SHACL + graph checks)
- 🔗 provenance logging (PROV-O + OpenLineage references)
- 🚦 publish gating (human approvals)

### 🧷 Non-negotiables
- **Evidence-led narrative:** every factual claim must map to a dataset/document/graph entity.
- **Deterministic workflow:** same inputs + config = same outputs (seeded where relevant).
- **No speculation:** Story Node v3 narrative must not invent missing facts.
- **No sensitive location exposure:** masking/generalization is default for restricted geographies.
- **Human approval:** required before publication, especially for “Mixed” sensitivity content.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 sops/
│   │   └── 📄 storynode_generation.md                    # 📖 This SOP
│   ├── 📁 experiments/
│   │   └── 📄 README.md                                  # 🧪 MCP experiment index
│   └── 📁 model_cards/
│       └── 📄 README.md                                  # 🧬 Model card index
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 storynode/
│           ├── ⚙️ generate_v3.py                          # Story Node generation entrypoint (example)
│           └── ⚙️ validate_v3.py                           # Story Node validation entrypoint (example)
├── 📁 schemas/
│   ├── 📄 story-node.schema.json                          # ✅ Story Node v3 JSON Schema
│   └── 📁 shacl/
│       └── 📄 storynode-v3-shape.ttl                      # ✅ Story Node v3 SHACL shape
├── 📁 data/
│   ├── 📁 work/
│   │   └── 📁 storynodes/
│   │       └── 📁 context/
│   │           └── 🧾 <node-id>.json                       # 📦 Deterministic context bundle
│   ├── 📁 processed/
│   │   └── 📁 storynodes/
│   │       └── 🧾 <node-id>.json                           # 📚 Final Story Node v3 entity
│   └── 📁 provenance/
│       └── 📁 storynodes/
│           └── 🧬 <node-id>.jsonld                         # 🔗 PROV-O bundle + OpenLineage refs
└── 📁 .github/
    └── 📁 workflows/
        └── ✅ mcp-validate.yml                              # CI gates (docs + provenance + policy)
~~~

---

## 🧭 Context

### ✅ Required inputs
- 🗂️ datasets: STAC/DCAT identifiers + rights/license fields
- 🧠 graph neighborhood: Neo4j entities and relationships (retrieval-constrained)
- 🗺️ geometry: GeoJSON and masking plan (H3 generalization if required)
- ⏱️ time: OWL-Time instant/interval and source time bounds
- 🧾 provenance anchors: source doc/dataset IDs and run identifiers
- ✍️ narrative draft: AI-assisted or human-authored text under constraints

### ➕ Optional inputs
- 🖼️ media assets (only with explicit rights metadata)
- 🧩 cross-links to related Story Nodes (typed, validated IDs)
- 🗺️ overlays for UI panels (non-sensitive by default)

---

## 📦 Data & Metadata

### 🧩 Story Node v3 required fields
A Story Node v3 JSON MUST include (minimum):
- `id`
- `type` = `story-node`
- `title`
- `narrative` (with evidence references)
- `spacetime` (GeoJSON or masked geometry + OWL-Time)
- `relations` (typed edges to graph entities)
- `provenance` (pointer to PROV-O bundle + checksums)
- `care_classification` and sovereignty/masking fields (structured)

### 🪶 Masking rules (default safe posture)
When masking is required:
- generalize spatial precision to H3 resolution required by policy (typically R7–R9)
- avoid storing raw coordinates for restricted places
- record masking as structured metadata:
  - `masking_method`
  - `masking_resolution`
  - `masking_reason`
  - `review_route`

---

## 🧱 Architecture

### 🧭 Procedure (deterministic steps)

#### Step 1 — Extract & prepare context
- query Neo4j for configured neighborhood (2–3 hops typical)
- assemble datasets/documents referenced by entities
- compute candidate spacetime bounds
- compute masking directives (if required)

Write:
~~~text
data/work/storynodes/context/<node-id>.json
~~~

#### Step 2 — Draft narrative (AI + human)
If AI is used, the generator must:
- generate panels: **Context · Timeline · Map**
- enforce constraints: no speculation, no genealogy, no sensitive coordinates
- attach evidence anchors for every claim

Human expert must:
- correct factual errors and ambiguity
- enforce neutrality and cultural sensitivity
- ensure accessibility (readability, structure)

#### Step 3 — Apply CARE & sovereignty gates
- determine CARE tier and required review route
- apply masking/generalization if needed
- route Tier A / sovereignty-tagged items for council review

#### Step 4 — Build Story Node v3 JSON
- populate required fields
- attach evidence references
- include masking metadata if applicable

#### Step 5 — Validate (schema + SHACL + graph)
- schema validation (JSON)
- SHACL validation
- graph entity resolution (no dangling IDs)
- spacetime sanity checks (OWL-Time, GeoSPARQL constraints)

#### Step 6 — Write provenance bundle (PROV-O + OpenLineage refs)
- record `prov:used`, `prov:wasGeneratedBy`, `prov:wasAssociatedWith`
- record model versions and seeds if AI used
- record masking activity explicitly

Write:
~~~text
data/provenance/storynodes/<node-id>.jsonld
~~~

#### Step 7 — Publish (gated)
- write final Story Node JSON
- ingest into Neo4j
- generate Focus Mode preview
- require approvals before publication

Write:
~~~text
data/processed/storynodes/<node-id>.json
~~~

### 🗺️ Flow diagram
~~~mermaid
flowchart TD
  A[🟢 Start: Story Node request] --> B[🧠 Neo4j + 🗂️ STAC/DCAT context bundle]
  B --> C[🪶 Masking + 🛡️ CARE/Sovereignty routing]
  C --> D{🤖 AI drafting enabled?}
  D -->|Yes| E[🧠 Draft panels + evidence anchors]
  D -->|No| F[✍️ Human draft]
  E --> G[🧑‍⚖️ Human review + edits]
  F --> G
  G --> H[🧩 Build Story Node v3 JSON]
  H --> I[✅ Validate: Schema + SHACL + Graph + Spacetime]
  I --> J{Pass?}
  J -->|No| K[🛠️ Remediate + re-run]
  J -->|Yes| L[🔗 Write PROV-O + OpenLineage refs]
  L --> M[📥 Commit outputs + ingest graph]
  M --> N[🚦 Publish gate: approvals]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 🧠 Focus Mode panels
- **Context:** evidence-led summary anchored to graph entities and datasets
- **Timeline:** OWL-Time aligned events bounded by source time ranges
- **Map:** GeoJSON or masked H3 geometry only (no restricted coordinates)

### 🚫 Forbidden narrative behaviors (hard block)
- inventing causes or intent behind events
- genealogical inference
- sacred site inference
- presenting unverified claims as facts
- exposing restricted coordinates or detailed sensitive locations

---

## 🧪 Validation & CI/CD

### ✅ Local runbook
~~~text
schema-lint-v11 schemas/story-node.schema.json data/processed/storynodes/<node-id>.json
shacl-validate-v11 schemas/shacl/storynode-v3-shape.ttl data/processed/storynodes/<node-id>.json
~~~

### ✅ Verification checklist (must pass before publish)
- schema validation
- SHACL validation
- CARE tier + review route satisfied
- masking applied where required
- provenance bundle present (PROV-O + checksums + OpenLineage refs)
- graph ingestion checks (IDs resolve)
- accessibility checks (structure, headings, readable text)
- CI gates green (`.github/workflows/mcp-validate.yml`)

### 🧯 Failure modes & recovery
Common failures:
- speculative or unverified claims
- sensitive coordinate exposure
- dangling graph references
- temporal contradictions
- missing provenance artifacts

Recovery:
- remove/repair narrative, add evidence anchors
- apply/strengthen masking
- repair graph IDs and rerun validations
- correct time bounds and rerun
- regenerate provenance bundle and rerun CI

---

## 🌐 STAC, DCAT & PROV Alignment

- Story Nodes should reference dataset identifiers from STAC/DCAT.
- If represented as STAC Items, geometry must respect masking rules (or be null).
- Every Story Node must have a PROV-O bundle:
  - inputs (datasets/documents)
  - activities (extraction/draft/review/publish)
  - agents (reviewers/services)
  - masking decisions as explicit activities/attributes
- OpenLineage event references may be included in the PROV-O bundle (do not embed secrets).

---

## ⚖ FAIR+CARE & Governance

### 🧾 CARE tiers (operational routing)
- **Tier A:** sovereignty-sensitive / restricted → council review required
- **Tier B:** mixed risk → domain reviewer + governance check
- **Tier C:** low risk → standard review + CI

### 🪶 Sovereignty constraints (hard constraints)
- never publish restricted coordinates
- masking/generalization default-on for restricted geographies
- protected datasets may bypass AI drafting
- human approval mandatory for any sovereignty-tagged publish action

### 🧭 Ethics constraints
- neutral tone
- avoid colonial framing and bias
- avoid sensationalizing trauma/conflict
- represent uncertainty explicitly (where allowed) and keep claims bounded to evidence

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.0.0 | 2025-11-23 | Initial Story Node v3 governed SOP for KFM v11. |
| v11.0.0 | 2025-12-12 | Updated to KFM-MDP v11.2.6 (approved H2 registry, emoji directory layout, tilde fences, governed footer links). |

---

<div align="center">

[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · KFM-OP v11 · KFM-PDC v11 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
