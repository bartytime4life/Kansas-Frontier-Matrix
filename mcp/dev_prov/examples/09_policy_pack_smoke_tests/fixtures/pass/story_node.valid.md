---
title: "✅ Story Node Fixture — Evidence-First Policy Pack Smoke Test"
path: "mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass/story_node.valid.md"
version: "v1.0.0"
last_updated: "2026-01-22"
status: "active"
doc_kind: "Story Node"
license: "CC-BY-4.0"

# Profile versions (contract-first governance)
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance & ethics
governance_ref: "urn:kfm:governance:ROOT_GOVERNANCE:v13"
ethics_ref: "urn:kfm:governance:ETHICS:v13"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

# Identity & integrity
doc_uuid: "urn:kfm:story_node:policy_pack_smoke_tests:09:story_node.valid:v1.0.0"
commit_sha: "bb86bf1707b50a9d3d43b06896fd387851de92b3"
doc_integrity_checksum: "sha256:b78b16bd90445d4a07a8c18b903f0ec70290c51283dedf3b658672bdafdc0bf7"

# Story-node specifics
story_node_id: "kfm.story_node.policy_pack_smoke_tests.09.story_node_valid"
story_pack_id: "kfm.story_pack.policy_pack_smoke_tests"
story_template: "TEMPLATE__STORY_NODE_V3"
evidence_manifest: "EM-09.yaml"
prov_bundle: "PROV-09.jsonld"

ai_assistance:
  used: true
  mode: "Focus Mode (example snippet only)"
  ai_generated_sections:
    - "focus_mode_example"
  human_reviewed: true

tags:
  - "fixture"
  - "policy-pack"
  - "provenance-first"
  - "story-nodes"
  - "kfm"
---

# ✅ Policy Pack Smoke Test — Story Node (Valid)

`Status:` ✅ active `Sensitivity:` 🌍 public `Classification:` 🟢 open `License:` ♻️ CC-BY-4.0

## 📘 Overview

This Story Node is a **test fixture** intended to pass KFM-style governance checks:

- ✅ YAML front-matter present and complete  
- ✅ A **Citations** block with **3–7 lines**  
- ✅ A machine-readable **Evidence Manifest** (YAML)  
- ✅ An embedded **PROV JSON-LD** snippet linking the Story Node to evidence and its authoring activity  
- ✅ No secrets, no PII, and no sensitive location disclosure  

## 🎯 Purpose

Demonstrate the **evidence-first narrative pattern**: Story Nodes are Markdown narratives whose claims can be traced to specific evidence items and provenance links. [4][7]

## 🧭 Audience

- 🧑‍💻 Developers validating policy packs / CI checks  
- 🗺️ Curators authoring Story Nodes  
- 🤖 Focus Mode / provenance pipeline implementers  

## 🧩 Definitions

- **Story Node**: a narrative artifact authored in Markdown (plus optional JSON config) that plays back synchronized map/timeline states. [2]
- **Evidence Manifest**: a small YAML/JSON inventory of sources used by the Story Node (checksums, query params, transforms). [4]
- **PROV bundle**: JSON-LD that links the Story Node entity/activity to evidence entities and agents. [7]

## 🗺️ Story Steps

### Step 1 — “The Contract: Evidence Before Narrative” 🧾

**What the user sees:** a short explanation of why KFM treats provenance and policy checks like tests.

**Fact (cited):**  
KFM-style governance gates treat policy checks as **fail-closed** validation that blocks merges when licenses, metadata, or provenance are missing. [4][5]

**Interpretation (not a fact):**  
Fail-closed governance is a pragmatic way to reduce “moral debt” and “technical debt” over time.

**Map State (example)**

```json
{
  "step_id": "step_01_evidence_first",
  "camera": { "center": [-98.5, 38.5], "zoom": 5.2, "pitch": 0, "bearing": 0 },
  "timeline": { "mode": "range", "start": "1854-01-01", "end": "1861-01-01" },
  "layers_on": ["base.boundary.state_ks"],
  "layers_off": ["hazards.flood_1951"],
  "focus_context": ["kfm:concept:provenance_first"]
}
```

### Step 2 — “Story Nodes: Markdown + Map Playback” 🗺️📜

**Fact (cited):**  
Story mode typically shows a narrative panel and a map, and each step can pan/zoom, toggle layers, and update timeline state. [2]

**Map State (example)**

```json
{
  "step_id": "step_02_story_mode",
  "camera": { "center": [-95.678, 39.048], "zoom": 10.5, "pitch": 35, "bearing": 12 },
  "timeline": { "mode": "point", "at": "1951-07-01" },
  "layers_on": ["hazards.flood_1951", "hydrology.rivers"],
  "layers_off": ["landcover.ndvi_composite"],
  "highlight": [{ "entity_id": "kfm:place:topeka_ks", "style": "pulse" }]
}
```

### Step 3 — “Focus Mode Example (AI Output Clearly Labeled)” 🤖🔍

> **AI-generated example (Focus Mode)** — *This block is intentionally labeled to satisfy AI-output governance rules.* [2][3]  
> **AI section id:** `focus_mode_example`  
> **User question:** “What datasets exist for Kansas River water levels, and how would I verify a claim?”  
> **System-style answer (example):**  
> 1) Use the dataset registry entry for `urn:kfm:dataset:hydrology.usgs.nwis.realtime.v1`. [6]  
> 2) Verify any numeric claim by opening the Evidence Manifest entry `E-DS-01` and replaying the recorded query parameters. [6][4]  
> 3) Confirm the Story Node’s provenance by checking that the PROV bundle contains a `prov:used` edge from the authoring Activity to `E-DS-01`. [7]

**Why this matters (fact, cited):**  
KFM UI design emphasizes showing citations and differentiating AI output to preserve trust. [2]

### Step 4 — “What CI / Policy Packs Validate” ✅🧪

**Fact (cited):**  
KFM-style CI checks include front-matter validation, schema validation for STAC/DCAT/PROV alignment, reference integrity checks, and secret/PII scanning. [1][5]

**Checklist**

- [x] Front-matter complete & valid  
- [x] Citations block present (3–7 lines)  
- [x] Evidence manifest present (machine-readable)  
- [x] PROV JSON-LD snippet present (machine-readable)  
- [x] No secrets / tokens / credentials  
- [x] No PII / sensitive data / restricted coordinates  

## 🔗 Graph Entities Referenced

These are **stable IDs** intended for link-outs in the UI (examples):

- `kfm:place:kansas` (State)
- `kfm:place:topeka_ks` (City)
- `kfm:river:kansas_river`
- `urn:kfm:dataset:hydrology.usgs.nwis.realtime.v1` [6]

## 📎 Citations (3–7 lines)

[1] **E-01** — *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation* (story nodes + graph linking; validation patterns).  
[2] **E-02** — *Kansas Frontier Matrix – Comprehensive UI System Overview* (story mode playback; citations & AI-output differentiation).  
[3] **E-07** — *Kansas Frontier Matrix (KFM) – AI System Overview* (Focus Mode: retrieval → governance → cited output).  
[4] **E-04** — *Additional Project Ideas* (Story Nodes with Evidence Manifests; PROV JSON-LD linkage; 3–7 line citations guidance).  
[5] **E-03** — *📚 KFM Data Intake – Technical & Design Guide* (narrative integrity; no “mystery nodes”; policy checks).  
[6] **E-DS-01** — *USGS NWIS Real-time Water Levels (Kansas) — example dataset ID* (`urn:kfm:dataset:hydrology.usgs.nwis.realtime.v1`).  
[7] **S-PROV-01** — *W3C PROV-O* (PROV concepts + JSON-LD mapping reference).  

## 🧾 Evidence Manifest (Inline copy of `EM-09.yaml`) 🗂️

```yaml
em_id: "EM-09"
em_version: "v1"
generated_at: "2026-01-22T00:00:00Z"

story_node:
  story_node_id: "kfm.story_node.policy_pack_smoke_tests.09.story_node_valid"
  doc_uuid: "urn:kfm:story_node:policy_pack_smoke_tests:09:story_node.valid:v1.0.0"
  file: "mcp/dev_prov/examples/09_policy_pack_smoke_tests/fixtures/pass/story_node.valid.md"

items:
  - id: "E-01"
    kind: "internal_doc"
    title: "Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation"
    filename: "Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf"
    sha256: "74c0fa7606579065028e73bc01201af37a17baf7308948fdb388c5758009d520"
    used_for:
      - "Story nodes + graph linking"
      - "CI/data validation references"
    notes: "Project-level technical overview."

  - id: "E-02"
    kind: "internal_doc"
    title: "Kansas Frontier Matrix – Comprehensive UI System Overview"
    filename: "Kansas Frontier Matrix – Comprehensive UI System Overview.pdf"
    sha256: "cdd3133e1e9a05226faecbe82d949e8a2e6932bc5d23ade3238b31d594ee6682"
    used_for:
      - "Story mode playback behavior"
      - "Citations & AI-output differentiation"
    notes: "UI behaviors for Story Nodes and Focus Mode."

  - id: "E-03"
    kind: "internal_doc"
    title: "📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide"
    filename: "📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf"
    sha256: "337805e79cdc1bcb262cc561cff205ad784e514035fad7bf2b2c5247729bb560"
    used_for:
      - "Narrative integrity in graph"
      - "Policy scanning expectations"
    notes: "Data ingestion and governance touchpoints."

  - id: "E-04"
    kind: "internal_doc"
    title: "Additional Project Ideas"
    filename: "Additional Project Ideas.pdf"
    sha256: "0cf31002f9977dc819eb68fe2f40fa5424b2dedba447b0c3378ab8acc43ecd44"
    used_for:
      - "Evidence manifests attached to Story Nodes"
      - "Citations block guidance (3–7 lines)"
      - "PROV JSON-LD linkage patterns"
    notes: "Evidence-first narrative proposal."

  - id: "E-05"
    kind: "internal_doc"
    title: "Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)"
    filename: "Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf"
    sha256: "6b455d1dbc1ca28620a6aecdcf117ce5dcf12de1bab66cfbf9bb286ce5ce1040"
    used_for:
      - "Future-facing concepts (background)"
    notes: "Roadmap/innovation concepts."

  - id: "E-06"
    kind: "internal_doc"
    title: "Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design"
    filename: "Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf"
    sha256: "9b574d9bd8e4ad781817193b120100d9efa5a66da558262e3212f0f561a32b7d"
    used_for:
      - "System architecture context (background)"
    notes: "Architecture and feature set."

  - id: "E-07"
    kind: "internal_doc"
    title: "Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖"
    filename: "Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf"
    sha256: "a7040612f4d3f290e4b035faf2ff6612f19ceec3b9f95ae02454e8c917cbf9e7"
    used_for:
      - "Focus Mode concepts (AI + governance + citations)"
    notes: "AI subsystem design."

  - id: "E-08"
    kind: "internal_doc"
    title: "🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals"
    filename: "🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf"
    sha256: "95a019145a7c549cd1a73fb4c26225736a2f731bf6d772bab2d9f56041df5513"
    used_for:
      - "Future proposals context (background)"
    notes: "Proposals & future directions."

  - id: "E-09"
    kind: "internal_doc"
    title: "AI Concepts & more"
    filename: "AI Concepts & more.pdf"
    sha256: "e2fd2bc05ea02aa1cdd5613e5b4da6304844eebd876612414945490950211092"
    used_for:
      - "AI background references (background)"
    notes: "Supporting AI references."

  - id: "E-10"
    kind: "internal_doc"
    title: "Maps / Google Maps / Virtual Worlds / Archaeological / Computer Graphics / Geospatial WebGL"
    filename: "Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf"
    sha256: "c64163c0acba998944b4bec8d3a24bad19b77a8f809c4f8e4122839d7b6f62ab"
    used_for:
      - "Geospatial rendering references (background)"
    notes: "Visualization and WebGL references."

  - id: "E-11"
    kind: "internal_doc"
    title: "Various programming languages & resources"
    filename: "Various programming langurages & resources 1.pdf"
    sha256: "1eb96b26064ed8135c9faaa413294234861fcec83acfea53e0b95ef81a6b9f58"
    used_for:
      - "General programming references (background)"
    notes: "Cross-language resources."

  - id: "E-12"
    kind: "internal_doc"
    title: "Data Management / Theories / Architectures / Data Science / Bayesian Methods"
    filename: "Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf"
    sha256: "ffeec704b38ba0ff86f7bb24fde837d386fb574bb9bf9aac1a0452cbba83fa6a"
    used_for:
      - "Data management & statistical methods references (background)"
    notes: "Data methodology references."

  - id: "E-DS-01"
    kind: "dataset"
    title: "USGS NWIS Real-time Water Levels (Kansas) — example dataset ID"
    ref: "urn:kfm:dataset:hydrology.usgs.nwis.realtime.v1"
    license: "Public Domain (USG)"
    used_for:
      - "Focus Mode example verification instructions"
    query_example:
      dialect: "sql"
      engine: "postgis"
      text: "SELECT * FROM hydrology.usgs_nwis_obs WHERE station_id = :station AND ts BETWEEN :t0 AND :t1 ORDER BY ts DESC LIMIT 1;"
    notes: "Included to demonstrate how query parameters are recorded."

specs:
  - id: "S-PROV-01"
    kind: "spec"
    ref: "urn:spec:w3c:prov-o"
    title: "W3C PROV-O / PROV-JSONLD (structure reference)"
  - id: "S-RFC-8785"
    kind: "spec"
    ref: "urn:ietf:rfc:8785"
    title: "RFC 8785 — JSON Canonicalization Scheme"
```

## 🧬 PROV Bundle (Inline copy of `PROV-09.jsonld`) 🔒

```json
{
  "@context": {
    "prov": "https://www.w3.org/ns/prov#",
    "kfm": "urn:kfm:",
    "xsd": "https://www.w3.org/2001/XMLSchema#"
  },
  "@graph": [
    {
      "@id": "urn:kfm:story_node:policy_pack_smoke_tests:09:story_node.valid:v1.0.0",
      "@type": ["kfm:StoryNode", "prov:Entity"],
      "prov:wasGeneratedBy": { "@id": "urn:kfm:activity:authoring:story_node:policy_pack_smoke_tests:09:2026-01-22" },
      "prov:wasAttributedTo": { "@id": "urn:kfm:agent:author:kfm_maintainer" }
    },
    {
      "@id": "urn:kfm:activity:authoring:story_node:policy_pack_smoke_tests:09:2026-01-22",
      "@type": ["kfm:StoryAuthoring", "prov:Activity"],
      "prov:startedAtTime": { "@value": "2026-01-22T00:00:00Z", "@type": "xsd:dateTime" },
      "prov:endedAtTime": { "@value": "2026-01-22T00:00:00Z", "@type": "xsd:dateTime" },
      "prov:used": [
        { "@id": "urn:kfm:evidence:E-01" },
        { "@id": "urn:kfm:evidence:E-02" },
        { "@id": "urn:kfm:evidence:E-03" },
        { "@id": "urn:kfm:evidence:E-04" },
        { "@id": "urn:kfm:evidence:E-05" },
        { "@id": "urn:kfm:evidence:E-06" },
        { "@id": "urn:kfm:evidence:E-07" },
        { "@id": "urn:kfm:evidence:E-08" },
        { "@id": "urn:kfm:evidence:E-09" },
        { "@id": "urn:kfm:evidence:E-10" },
        { "@id": "urn:kfm:evidence:E-11" },
        { "@id": "urn:kfm:evidence:E-12" },
        { "@id": "urn:kfm:evidence:E-DS-01" }
      ],
      "prov:wasAssociatedWith": { "@id": "urn:kfm:agent:author:kfm_maintainer" }
    },
    {
      "@id": "urn:kfm:agent:author:kfm_maintainer",
      "@type": ["prov:Agent", "kfm:Human"],
      "kfm:role": "maintainer"
    },

    { "@id": "urn:kfm:evidence:E-01", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:74c0fa7606579065028e73bc01201af37a17baf7308948fdb388c5758009d520" },
    { "@id": "urn:kfm:evidence:E-02", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:cdd3133e1e9a05226faecbe82d949e8a2e6932bc5d23ade3238b31d594ee6682" },
    { "@id": "urn:kfm:evidence:E-03", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:337805e79cdc1bcb262cc561cff205ad784e514035fad7bf2b2c5247729bb560" },
    { "@id": "urn:kfm:evidence:E-04", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:0cf31002f9977dc819eb68fe2f40fa5424b2dedba447b0c3378ab8acc43ecd44" },
    { "@id": "urn:kfm:evidence:E-05", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:6b455d1dbc1ca28620a6aecdcf117ce5dcf12de1bab66cfbf9bb286ce5ce1040" },
    { "@id": "urn:kfm:evidence:E-06", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:9b574d9bd8e4ad781817193b120100d9efa5a66da558262e3212f0f561a32b7d" },
    { "@id": "urn:kfm:evidence:E-07", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:a7040612f4d3f290e4b035faf2ff6612f19ceec3b9f95ae02454e8c917cbf9e7" },
    { "@id": "urn:kfm:evidence:E-08", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:95a019145a7c549cd1a73fb4c26225736a2f731bf6d772bab2d9f56041df5513" },
    { "@id": "urn:kfm:evidence:E-09", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:e2fd2bc05ea02aa1cdd5613e5b4da6304844eebd876612414945490950211092" },
    { "@id": "urn:kfm:evidence:E-10", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:c64163c0acba998944b4bec8d3a24bad19b77a8f809c4f8e4122839d7b6f62ab" },
    { "@id": "urn:kfm:evidence:E-11", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:1eb96b26064ed8135c9faaa413294234861fcec83acfea53e0b95ef81a6b9f58" },
    { "@id": "urn:kfm:evidence:E-12", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:sha256": "sha256:ffeec704b38ba0ff86f7bb24fde837d386fb574bb9bf9aac1a0452cbba83fa6a" },
    { "@id": "urn:kfm:evidence:E-DS-01", "@type": ["prov:Entity", "kfm:EvidenceItem"], "kfm:ref": "urn:kfm:dataset:hydrology.usgs.nwis.realtime.v1" }
  ]
}
```

## ✅ Definition of Done (Fixture)

- [x] Front-matter: present, populated, stable IDs provided  
- [x] Contains **Citations** block with **7 lines** (meets 3–7 requirement)  
- [x] Evidence manifest present (YAML)  
- [x] PROV JSON-LD present  
- [x] AI-generated snippet labeled  
- [x] No external links required to interpret the artifact  
- [x] No secrets, no PII  

