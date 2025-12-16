---
title: "🔎 KFM — Provenance Graph Diffing (Node/Edge · ETL‑Run Δ · Promotion Checklist Flags)"
path: "docs/patterns/provenance/graph-diff/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE & Data Architecture Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"
intent: "provenance-graph-diff-pattern"
diagram_profiles:
  - "mermaid-flowchart-v1"

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
    - "ETL"
    - "data/stac/**"
    - "data/sources/**"
    - "data/processed/**"
    - "src/pipelines/**"
    - "src/graph/**"
    - "tools/validation/**"
    - "tools/governance/**"
    - ".github/workflows/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next major KFM pattern revision"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

immutability_status: "mutable-plan"
doc_uuid: "urn:kfm:doc:patterns:provenance:graph-diff:v11.2.6"
semantic_document_id: "kfm-pattern-provenance-graph-diff-v11.2.6"
event_source_id: "ledger:kfm:doc:patterns:provenance:graph-diff:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain: []
---

# 🔎 KFM — Provenance Graph Diffing (Node/Edge · ETL‑Run Δ · Promotion Checklist Flags)

**Purpose:** compute **small, testable diffs** between provenance graphs emitted by successive ETL runs (e.g., `t-1 → t`) and produce:
1) a **machine-readable diff bundle** (for CI + audit), and  
2) a **human-sized promotion checklist** (for reviewers).

This pattern is designed to fit KFM’s pipeline contract: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI → Story Nodes / Focus Mode**.

---

## 📘 Overview

This pattern detects, summarizes, and gates provenance changes across ETL runs:

- **Node-level Δ**
  - new / missing datasets (Entities)
  - new / missing activities (Activities)
  - new / missing agents (Agents)
  - stable ID changes (rename vs new identity)
- **Edge-level Δ**
  - lineage rewires (e.g., inputs/outputs change)
  - missing upstreams (orphan entities)
  - new transitive dependencies (new ancestors)
- **Semantic drift**
  - schema field drift (added/removed/renamed keys)
  - unit changes (e.g., meters vs feet)
  - CRS changes (unexpected projection/CRS shifts)
  - governance label changes (classification/sensitivity/license)

**Promotion intent:** convert “diff noise” into a checklist a reviewer can finish, and a structured artifact that CI can reason about.

---

## 🗂️ Directory Layout

The following paths are aligned to the documented KFM monorepo layout and ETL script placement.

~~~text
📁 docs/
  📁 patterns/
    📁 provenance/
      📁 graph-diff/
        📄 README.md                         # this pattern

📁 data/
  📁 sources/                                # source catalog + provenance ledger
  📁 stac/                                   # STAC catalogs/items (incl. version links)
  📁 raw/                                    # raw ingested materials (not edited)
  📁 processed/                               # canonical processed outputs
  📁 work/                                   # staging / intermediate artifacts
  📁 reports/                                 # QA/QC reports (recommended: store diff outputs)
  📁 checksums/                               # integrity hashes
  📁 updates/                                 # incremental update payloads

📁 scripts/
  📄 fetch_data.py                            # acquisition
  📄 parse_texts.py                           # extraction
  📄 georef_map.py                            # georeferencing
  📄 generate_stac.py                         # STAC generation/updates
  📄 ingest_graph.py                          # Neo4j ingest (STAC + provenance)

📁 tools/
  📁 validation/                              # schema + catalog validation utilities
  📁 governance/                              # policy/gov checks (implementation varies)
  📁 cli/                                     # (recommended) command wrappers / operators

📁 src/
  📁 pipelines/                               # ETL orchestration + transforms
  📁 graph/                                   # Neo4j model/loaders/queries

📁 mcp/
  📁 experiments/                             # experiment templates + run writeups

📁 .github/
  📁 workflows/
    📄 kfm-ci.yml                              # required CI checks + promotion gating
~~~

**Recommended diff artifact locations (create if missing):**
- Machine diff bundle: `data/reports/provenance-diff/<run_id>/<t-1>__<t>.diff.json`
- Human checklist: `data/reports/provenance-diff/<run_id>/<t-1>__<t>.checklist.md`
- Optional run narrative: `mcp/experiments/<run_id>/provenance-diff.md`

---

## 🧭 Context

### Why diff provenance graphs (instead of reading logs)?
Logs are implementation detail; provenance is **contract + audit trail**. KFM treats provenance records as first-class and expects the catalog itself to be changelogged alongside data additions.

### Where this fits in the pipeline
- **Before promotion** (dev → staging → production), a candidate ETL run must be comparable to the last approved run.
- The diff bundle provides:
  - deterministic evidence of what changed
  - an explicit list of reviewer tasks
  - an objective gate for “stop / proceed / proceed with review”

### Terminology (minimal)
- **Run (`t`)**: an ETL execution producing new/updated STAC + PROV metadata.
- **Baseline (`t-1`)**: prior approved run for the same dataset family or collection.
- **Canonical provenance graph**: normalized representation in KFM-OP v11 terms (entities/activities/agents + lineage edges).

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[ETL Run t-1 STAC and PROV] --> C[Normalizer]
  B[ETL Run t STAC and PROV] --> C
  C --> D[Canonical Provenance Graph KFM-OP v11]
  D --> E[Diff Engine Node Edge Metadata]
  E --> F[Diff Bundle JSON]
  E --> G[Risk Evaluation Rules]
  G --> H[Promotion Checklist Markdown]
  H --> I[Promotion Gate GitHub Checks]
~~~

---

## 🧱 Architecture

### 1) Inputs
This pattern assumes each run produces:
- STAC Items/Collections (under `data/stac/**`), and
- PROV-aligned lineage metadata attached to the dataset(s) or generated as sidecar JSON-LD.

Optionally, the same lineage is also ingested into Neo4j via `scripts/ingest_graph.py`.

### 2) Normalization (determinism step)
Normalize both runs into a comparable form:

- **Stable identifiers**
  - prefer canonical URIs/IDs for entities, activities, agents
  - separate “rename” from “new identity” (ID change is high risk)
- **Sort + canonicalize**
  - stable ordering for nodes and edges
  - normalized key ordering in JSON
- **Strip run-noise**
  - volatile timestamps that do not describe the dataset
  - transient file paths
  - debug-only annotations

### 3) Diff computation
Compute independent deltas:

- **Node delta**
  - added / removed / changed nodes (Entity/Activity/Agent)
- **Edge delta**
  - added / removed lineage edges
  - detect upstream loss (entity becomes orphaned)
  - detect dependency growth (new ancestors)
- **Attribute drift**
  - detect changes in critical metadata fields:
    - CRS/projection fields
    - units
    - schema/version fields
    - license / governance labels

### 4) Risk evaluation (promotion checklist flags)
Convert diff results into severity:

- ✅ **OK** (informational)
- ⚠️ **Review Required** (promotion allowed only with reviewer sign-off)
- ⛔ **Block** (promotion must stop until resolved)

**Important:** this pattern is policy-neutral about the implementation of “rules.”
- Rules can be implemented as:
  - CI scripts in `tools/validation/` or `tools/governance/`, and/or
  - dedicated checks inside `.github/workflows/kfm-ci.yml`.

(OPA/Rego/Conftest *may* be used, but is not assumed by this pattern unless explicitly adopted by governance.)

### 5) Outputs
Produce two artifacts per candidate promotion:

1) **Diff bundle (JSON)** for CI + audit trails  
2) **Promotion checklist (Markdown)** for human review  
Both artifacts should be attached to the PR and/or stored under `data/reports/`.

---

## 📦 Data & Metadata

### Diff bundle (recommended JSON shape)
This is a recommended contract; if formalized, add a governed schema under `schemas/json/`.

~~~json
{
  "diff_id": "<sha256-of-normalized-graphs-and-run-ids>",
  "generated_at": "2025-12-16T00:00:00Z",
  "baseline": {
    "run_id": "t-1",
    "stac_path": "data/stac/...",
    "commit_sha": "<git-sha>",
    "notes": "last approved run"
  },
  "candidate": {
    "run_id": "t",
    "stac_path": "data/stac/...",
    "commit_sha": "<git-sha>",
    "notes": "promotion candidate"
  },
  "summary": {
    "nodes_added": 0,
    "nodes_removed": 0,
    "nodes_changed": 0,
    "edges_added": 0,
    "edges_removed": 0,
    "high_risk_flags": 0,
    "review_flags": 0
  },
  "node_delta": {
    "added": [],
    "removed": [],
    "changed": []
  },
  "edge_delta": {
    "added": [],
    "removed": []
  },
  "attribute_drift": [
    {
      "entity_id": "urn:kfm:entity:...",
      "field": "proj:epsg",
      "from": 4326,
      "to": 26914,
      "severity": "review"
    }
  ],
  "risk_flags": [
    {
      "rule_id": "prov.orphan_entity",
      "severity": "block",
      "message": "Entity has no generating activity or upstream source."
    }
  ]
}
~~~

### Promotion checklist (recommended Markdown shape)

~~~markdown
# Promotion Checklist — Provenance Diff (t-1 → t)

## Summary
- ✅ Node delta: 0 added / 0 removed / 0 changed
- ⚠️ Edge delta: 2 edges rewired
- ⛔ Governance: 1 blocked item (license missing)

## Required reviewer actions
- [ ] Confirm rewired lineage is expected (see diff bundle: edge_delta.removed/added)
- [ ] Confirm license metadata present + valid for all new entities
- [ ] Confirm CRS/projection changes are justified and documented

## Flags
- ⛔ prov.orphan_entity — Entity has no upstream
- ⚠️ meta.crs_changed — CRS changed between runs
~~~

### Suggested checklist rules (starter set)
| Category | Example condition | Flag |
|---|---|---|
| Provenance completeness | Any Entity lacks upstream provenance (orphan) | ⛔ |
| Lineage rewiring | `prov:wasDerivedFrom` changes for an existing entity | ⚠️ |
| Version link integrity | STAC predecessor/successor missing for a version bump | ⛔ |
| CRS/projection drift | CRS changes without explicit justification | ⚠️ |
| License/governance drift | License removed/unknown on promoted artifacts | ⛔ |
| Sensitive content | Newly introduced sensitive geometry/PII markers | ⛔ |

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (KFM-STAC v11)
- Use STAC Items/Collections as the consistent metadata envelope for assets.
- When dataset updates occur, represent them using the **STAC Versioning Extension** (predecessor/successor links).

### DCAT (KFM-DCAT v11)
- Mirror dataset discovery metadata (title/description/keywords/license) in DCAT terms.
- Diffing should treat license changes as high-risk because they impact reuse.

### PROV-O (KFM-PROV v11)
- Treat:
  - datasets as `prov:Entity`
  - ETL steps / curation steps as `prov:Activity`
  - people/services/CI as `prov:Agent`
- Prefer explicit lineage edges (e.g., `prov:wasDerivedFrom`, `prov:wasGeneratedBy`) as the stable basis for graph diffing.

### Neo4j alignment (version edges)
- When using Neo4j for lineage queries, preserve version chains using `:PREDECESSOR` / `:SUCCESSOR` relationships.
- Diffing can optionally leverage those edges to select `t-1` automatically for a `t` candidate.

---

## 🧪 Validation & CI/CD

### CI enforcement (documented KFM baseline)
At minimum, KFM CI includes these validation profiles (names are stable contracts):
- `markdown-lint`, `schema-lint`, `metadata-check`, `diagram-check`, `footer-check`,
  `accessibility-check`, `provenance-check`, `secret-scan`, `pii-scan`

### Promotion gate integration
- The promotion checklist and diff bundle should be treated as required artifacts for promotion PRs.
- The `provenance-check` profile is the natural home for:
  - verifying the diff bundle exists for promotions
  - asserting the checklist has no ⛔ items remaining
  - ensuring version chain integrity (STAC + graph)

### Local validation (recommended)
- Run the project’s standard test harness (e.g., `make test`) before opening a promotion PR.
- Validate STAC outputs before ingest to Neo4j.
- Validate that any diff artifacts are deterministic (stable ordering, stable hashes).

---

## 🧠 Story Node & Focus Mode Integration

### What the UI should receive
Diffing output should be exposed **through the API layer**, not by direct graph access from the frontend.

Minimum payload for Focus Mode / dataset detail views:
- “What changed since previous approved version?”
  - counts (nodes/edges/metadata)
  - top risk flags (⚠️/⛔)
  - links to diff bundle + checklist artifacts

### Why this matters for Focus Mode
- Focus Mode benefits from explicit “version locks”:
  - show the user which dataset version the narrative is grounded on
  - provide a traceable chain across `t-1 → t → …`

---

## ⚖ FAIR+CARE & Governance

### Governance expectations
- Provenance is a first-class trust primitive: no promoted artifact should be an orphan.
- Governance documents are binding; doc footers and front‑matter must link governance/ethics/sovereignty references.

### Sensitive content handling (diff outputs)
Diff artifacts must not leak:
- personal identifiers
- internal file system paths
- precise sensitive coordinates
Prefer:
- stable entity IDs
- redacted snippets
- high-level “what changed” summaries

### Reviewer responsibility
A reviewer should be able to answer:
- Did this run change lineage?
- Are all new/changed entities properly licensed and classified?
- Did any change increase risk (sensitivity, CRS, schema drift)?
- Is the version chain intact and queryable?

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Updated to KFM‑MDP v11.2.6 heading registry + fencing profile; added governed front‑matter requirements (governance, compliance, AI limits); aligned directory layout and CI check names to documented repo standards; clarified STAC versioning + Neo4j version edges as the foundation for run diffs. |

---

**Governance & policy links (standard footer):**
- Governance: `governance/ROOT-GOVERNANCE.md`
- Ethics (FAIR+CARE): `faircare/FAIRCARE-GUIDE.md`
- Sovereignty: `sovereignty/INDIGENOUS-DATA-PROTECTION.md`
- Markdown protocol: `docs/standards/kfm_markdown_protocol_v11.2.6.md`