---
title: "🧬 KFM Pattern — Provenance & Lineage"
path: "docs/patterns/provenance/README.md"

version: "v1.0.0"
last_updated: "2025-12-16"
release_stage: "Draft / Governed"
lifecycle: "Living Document"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "evolving"

status: "Proposed"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-sequence-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "provenance"
  applies_to:
    - "etl"
    - "stac"
    - "dcat"
    - "prov"
    - "neo4j-graph"
    - "apis"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; examples must mask/generalize locations)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Review for supersession"

commit_sha: "<latest-commit-hash>"

# For v1.0.0, the origin root is this document/version.
# When superseding, prepend newer superseded entries (newest-first).
provenance_chain:
  - "docs/patterns/provenance/README.md@v1.0.0"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:patterns:provenance:readme:v1.0.0"
semantic_document_id: "kfm-patterns-provenance-readme-v1"
event_source_id: "ledger:kfm:doc:patterns:provenance:readme:v1.0.0"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "fabricate-provenance"
  - "invent-dataset-relationships"
  - "expose-sensitive-coordinates"
---

<div align="center">

# 🧬 **KFM Pattern — Provenance & Lineage**
`docs/patterns/provenance/README.md`

**Purpose**  
Define a **repeatable, audit-ready** approach to capturing lineage across the KFM pipeline  
(ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI → Story Nodes / Focus Mode).  
This pattern emphasizes **PROV‑O–aligned** modeling, **version-aware identifiers**, and **CI‑safe artifacts**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/PROV--O-Lineage%20Model-blue" />
<img src="https://img.shields.io/badge/Status-Proposed-lightgrey" />

</div>

---

## 📘 Overview

This pattern defines **how KFM work products declare provenance** in a way that is:

- **Deterministic & replayable** (run manifests + pinned inputs/versions)
- **Machine‑queryable** (PROV‑O compatible Entities / Activities / Agents)
- **Catalog‑friendly** (links from STAC + DCAT records)
- **Graph‑ready** (Neo4j lineage edges map cleanly from PROV relations)
- **Focus Mode safe** (summarization allowed; provenance invention prohibited)

### What this pattern covers

- Minimum provenance model for KFM: **Entity / Activity / Agent**
- Where to store provenance artifacts:
  - Run-scoped (execution) provenance
  - Dataset/item-scoped provenance
  - Catalog-facing links (STAC/DCAT)
- How provenance connects to:
  - dataset versioning
  - Story Nodes and narratives
  - governance and sensitivity controls

### What this pattern does not cover

- Full ontology authoring (use existing KFM ontology terms and PROV‑O)
- Frontend provenance rendering details (UI stays behind APIs)

---

## 🗂️ Directory Layout

All directory trees **MUST** be fenced as `~~~text`, use consistent branch glyphs, and include emojis + aligned comments.

### Pattern library layout

~~~text
docs/
└── 📁 patterns/                                        # Pattern library (implementation guidance)
    ├── 📁 provenance/                                  # Provenance & lineage patterns (PROV-O aligned)
    │   ├── 📄 README.md                                # This document
    │   ├── 📁 examples/                                # CI-safe examples (mask/generalize locations)
    │   │   ├── 📄 prov_bundle.example.jsonld           # Minimal PROV bundle (run-level)
    │   │   ├── 📄 stac_item_with_prov.example.json     # STAC Item linking provenance asset
    │   │   └── 📄 dcat_dataset_with_prov.example.ttl   # DCAT dataset/distribution w/ PROV links
    │   └── 📁 templates/                               # Copy/paste templates
    │       ├── 📄 run_manifest.template.yaml           # Run manifest skeleton (inputs/outputs/params)
    │       └── 📄 provenance_note.template.md          # Human note to accompany a run (optional)
    └── 📁 stac/                                        # STAC patterns (see docs/patterns/stac/README.md)
~~~

### Runtime and data artifact layout

~~~text
mcp/
└── 📁 runs/                                            # Run logs (deterministic, replayable)
    └── 📁 <run_id>/                                    # One pipeline execution (stable run_id)
        ├── 📄 run_manifest.json                         # Machine manifest (params, versions, env)
        ├── 📄 prov.jsonld                               # PROV-O bundle for this run
        ├── 📄 checksums.sha256                          # Hashes for referenced outputs
        └── 📁 outputs/                                  # Optional: output pointers (not primary storage)

data/
├── 📁 raw/                                             # Source snapshots (if stored; immutable)
├── 📁 processed/                                       # Derived datasets (versioned; no code here)
└── 📁 stac/                                            # STAC catalogs/items (data discovery layer)
    └── 📁 <collection>/                                # Collection-scoped grouping
        └── 📁 <item_id>/                                # Item folder (if file-based STAC layout)
            ├── 📄 item.json                             # STAC Item (links/assets include provenance)
            └── 📄 prov.jsonld                           # Optional: item-scoped provenance sidecar
~~~

> If your current pipeline uses different locations, document the mapping and keep the UI behind APIs (no direct graph access).

---

## 🧭 Context

KFM’s pipeline expects provenance to be a **first-class governance artifact**: each dataset and transformation should be traceable to sources, processes, and responsible agents.

This pattern aligns with the KFM approach of:

- Using **STAC** for dataset/item discovery and structure
- Using **DCAT** for catalog interoperability and publishing
- Using **PROV‑O** for lineage (what was used, what generated what, and who/what performed the activity)
- Handling updates via **version-aware relationships** (e.g., predecessor/successor semantics)

### Provenance vocabulary baseline

- **prov:Entity** — a thing (dataset, STAC Item, derived table, model output)
- **prov:Activity** — a process (ETL job, inference run, curation step)
- **prov:Agent** — who/what acted (person, org, CI runner, software agent)

### KFM minimum guarantee

For every **output entity**, it must be possible to answer:

- *What inputs contributed to this output?*
- *Which activity produced it (with parameters/config)?*
- *Which agent (and code revision) performed the activity?*
- *Which version does this output represent, and what did it supersede?*

---

## 🗺️ Diagrams

### End-to-end lineage flow

~~~mermaid
flowchart LR
  S[Source Entity] -->|used| A[ETL/Transform Activity]
  A -->|generated| O[Output Entity]
  O --> C[STAC Item/Collection]
  O --> P[PROV Bundle]
  C --> G[Graph Ingest]
  P --> G
  G --> API[API Layer]
  API --> UI[UI / MapLibre]
  UI --> SN[Story Node]
~~~

### Run capture sequence

~~~mermaid
sequenceDiagram
  participant CI as CI Runner
  participant ETL as ETL Job
  participant PROV as PROV Bundle
  participant STAC as STAC Catalog
  CI->>ETL: execute(run_id, pinned_inputs, config)
  ETL->>PROV: write prov.jsonld (Activity + Entities + Agent)
  ETL->>STAC: write/update Item (link provenance asset)
  CI->>CI: validate (front-matter, STAC, provenance, checksums)
~~~

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes are narrative layers that **must remain evidence-led**.

### Required behavior

- Story Nodes should reference **underlying Entities** (datasets / STAC Items / documents) and—where available—the **Activity** that generated derived narrative artifacts.
- Focus Mode may summarize and build navigation aids, but it **must not fabricate provenance or dataset relationships**.

### Practical pattern for Story Nodes

When a Story Node is derived from analysis (e.g., extraction or modeling), ensure:

- The Story Node’s dataset pointer links back to:
  - the source Entity (original document/dataset)
  - the extraction/model Activity
  - the run_id and commit_sha that produced the node

If Story Nodes include map features or coordinates, follow sensitivity masking rules and sovereignty policy requirements before publication.

---

## 🧪 Validation & CI/CD

CI should block provenance regressions the same way it blocks schema regressions.

### Minimum checks to expect

- **markdown-lint** — structure (one H1; approved H2s)
- **schema-lint / metadata-check** — required front matter keys and consistency
- **diagram-check** — Mermaid parses cleanly
- **provenance-check** — provenance fields + version history coherence
- **secret-scan / pii-scan** — prevent unsafe leakage

### Provenance-specific validation targets

- Every output Entity has:
  - a stable identifier
  - a checksum (or a reference to one)
  - a generating Activity
- Every Activity records:
  - parameters/config reference
  - start/end time (or at least end)
  - the Agent(s) responsible
- Versioned Entities include predecessor/successor semantics and are queryable as a chain

---

## 📦 Data & Metadata

### Minimum run manifest fields

A run manifest (machine-facing) should be able to reconstruct “what happened” without guesswork:

- `run_id` (stable; unique)
- `started_at`, `ended_at`
- `commit_sha` (code revision)
- execution environment (container digest / pinned deps)
- inputs: `{id, version, checksum, href}`
- outputs: `{id, version, checksum, href}`
- parameters/config references (paths, not embedded secrets)

### Sidecar provenance artifacts

Recommended default for KFM:

- Write a **run-level** `prov.jsonld` under `mcp/runs/<run_id>/`
- Optionally write an **item-level** provenance sidecar in the STAC item folder, or expose it as a STAC asset

> Provenance artifacts should be treated as immutable per run. If corrected, create a new version and link with revision semantics.

### Example run manifest skeleton (template)

~~~yaml
run_id: "<run_id>"
started_at: "YYYY-MM-DDTHH:MM:SSZ"
ended_at: "YYYY-MM-DDTHH:MM:SSZ"

code:
  commit_sha: "<latest-commit-hash>"
  pipeline: "<pipeline-name>"
  config_ref: "path/to/config.yaml"

inputs:
  - id: "<source-entity-id>"
    version: "<vX.Y.Z>"
    checksum_sha256: "<sha256>"
    href: "<uri-or-path>"

outputs:
  - id: "<output-entity-id>"
    version: "<vX.Y.Z>"
    checksum_sha256: "<sha256>"
    href: "<uri-or-path>"

agents:
  - id: "<agent-id>"
    type: "software|person|org"
    label: "<display-name>"

notes:
  sensitivity: "General|Restricted|Sensitive"
  sovereignty_review: "required|not-required|pending"
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

This section shows *how to connect the same lineage* across the three main interoperability surfaces.

### STAC pattern

Use STAC **assets** or **links** to attach provenance:

- Add an asset such as `assets.provenance` pointing to a PROV JSON-LD file.
- For versioning, include predecessor/successor semantics via link relations or extension fields (as defined in your STAC pattern and KFM profile).

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "example-item",
  "properties": {
    "datetime": "2025-12-16T00:00:00Z"
  },
  "geometry": null,
  "links": [
    {
      "rel": "derived_from",
      "href": "stac://source-item-id",
      "type": "application/json",
      "title": "Source STAC Item"
    }
  ],
  "assets": {
    "data": {
      "href": "data/processed/example-item.parquet",
      "type": "application/x-parquet",
      "roles": ["data"]
    },
    "provenance": {
      "href": "mcp/runs/<run_id>/prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata"],
      "title": "PROV-O lineage bundle for this output"
    }
  }
}
~~~

### DCAT pattern

In DCAT, the dataset/distribution can reference provenance using PROV terms.

~~~turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .

<#dataset> a dcat:Dataset ;
  dct:identifier "example-item" ;
  dct:title "Example Dataset" ;
  prov:wasGeneratedBy <#activity> .

<#dist> a dcat:Distribution ;
  dct:format "Parquet" ;
  dcat:downloadURL <file:data/processed/example-item.parquet> ;
  prov:wasDerivedFrom <#sourceEntity> .
~~~

### PROV-O bundle pattern

At minimum:

- one Activity (the run / transform)
- one or more input Entities
- one or more output Entities
- one Agent (software/person/org)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "urn:kfm:prov:bundle:<run_id>",
  "@type": "prov:Bundle",
  "prov:wasGeneratedBy": {
    "@id": "urn:kfm:prov:activity:<run_id>",
    "@type": "prov:Activity"
  }
}
~~~

> Keep the bundle deterministic: stable IDs, pinned versions, and checksums referenced from `checksums.sha256`.

---

## 🧱 Architecture

This pattern fits the KFM pipeline stages as follows:

1. **ETL stage**
   - Capture run manifest + PROV bundle
   - Emit STAC Items/Collections referencing provenance
2. **Catalog stage (STAC/DCAT/PROV)**
   - Ensure catalog entries can resolve to provenance artifacts
3. **Graph stage (Neo4j)**
   - Ingest PROV relations as lineage edges between entities/activities/agents
   - Maintain version links (predecessor/successor chains)
4. **API stage**
   - Provide provenance lookup by entity ID and by run_id
5. **UI stage (React/MapLibre)**
   - Display provenance summaries via APIs
   - Do not access the graph directly
6. **Story Nodes / Focus Mode**
   - Use provenance to support evidence-led narratives
   - Do not invent provenance edges

---

## ⚖ FAIR+CARE & Governance

### Sensitivity and masking

- Do not publish sensitive coordinates or culturally sensitive site locations in examples or public artifacts.
- Prefer generalized geometries, redaction, or aggregation where required by policy and stewardship.

### Sovereignty alignment

If a dataset touches Indigenous communities, the provenance record must not undermine sovereignty controls. When in doubt:

- mark the item’s sensitivity appropriately
- route for governance review before publication

### Governance review triggers

Escalate to human review when a change:

- increases public exposure of provenance detail (e.g., adds location precision)
- introduces new lineage relations for sensitive sources
- changes retention policy for run artifacts or provenance bundles

---

## 🕰️ Version History

| Version | Date | Change Summary | Owner | Notes |
|---|---|---|---|---|
| v1.0.0 | 2025-12-16 | Initial provenance & lineage pattern draft | KFM Documentation Team | Governance review recommended |

---

<div align="center">

[🏛️ Governance Charter](../../governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>