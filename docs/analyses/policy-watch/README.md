---
title: "📡 KFM v11.2.4 — Policy Watch Analyses — README"
path: "docs/analyses/policy-watch/README.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Draft · Framework"
lifecycle: "Living Document"
review_cycle: "Quarterly · Analyses Board · FAIR+CARE Oversight"
content_stability: "beta"
backward_compatibility: "Not Applicable"

status: "Active"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/policy-watch-telemetry.json"
telemetry_schema: "schemas/telemetry/policy-watch-telemetry-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/analyses/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:analyses:policy-watch:readme:v11.2.4"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public / Framework"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "policy-watch-file-naming-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "analyses"
    - "policy-watch"
    - "etl"
    - "catalogs"
    - "story-nodes"
    - "governance"
  impacted_modules:
    - "docs/analyses/*/policy-watch"
    - "data/raw/external/*"
    - "data/processed/external/*"
    - "data/stac/external/*"
    - "src/pipelines/external/*"
    - "src/graph/*"
    - "src/api/*"
    - "src/web/story-nodes/*"
---

<div align="center">

# 📡 **Kansas Frontier Matrix — Policy Watch Analyses**  

`docs/analyses/policy-watch/README.md`

---

**Kansas Frontier Matrix (KFM v11)** · **Policy, Data, and Scenario Alignment Hub**  
**Alignment:** STAC 1.x · DCAT 3.0 · PROV-O · GeoSPARQL · FAIR+CARE · ISO 19115

</div>

---

## 📘 Overview

### Purpose

This README defines how **Policy Watch** analyses are organized, named, and connected across the Kansas Frontier Matrix (KFM).  

Policy Watch notes are **lightweight, governance-aware briefs** that track structural changes in:

- Federal, state, Tribal, and local policy.
- Regulatory processes and filings.
- National and international data products (e.g., EIA, USGS, NOAA, Census).
- Standards and guidance that materially affect KFM data, models, and Story Nodes.

The goal is to:

- Provide a **single pattern** for creating, cataloging, and maintaining Policy Watch notes.
- Ensure each note is:
  - Markdown- and CI-compliant (KFM-MDP v11.2.4),
  - Catalog-ready (STAC/DCAT/PROV),
  - Graph-attachable (Neo4j),
  - Story-Node friendly and Focus-Mode aware.

### Scope

This guide applies to:

- All files under `docs/analyses/*/policy-watch/`.
- The cross-domain index at `docs/analyses/policy-watch/`.
- Any ETL, catalog, or graph components referenced by Policy Watch notes.

It does **not** define the legal or policy stance of KFM; instead, it defines:

- **How** we observe and track external changes.
- **Where** we record implications for data, pipelines, and stories.
- **How** we align Policy Watch notes with FAIR+CARE and sovereignty governance.

---

## 🗂️ Directory Layout

This section anchors Policy Watch within the monorepo, using the standard emoji-rich directory style.

### Top-level analyses layout (excerpt)

```text
📁 docs/
└── 📁 analyses/
    ├── 📄 README.md                     # Analyses overview (global)
    ├── 📁 policy-watch/                 # Cross-domain Policy Watch index
    │   └── 📄 README.md                 # (this file)
    ├── 📁 energy/
    │   └── 📁 policy-watch/             # Energy-specific Policy Watch notes
    │       ├── 📄 README.md             # Energy Policy Watch index (per-domain)
    │       └── 📄 eia-data-centers-critical-minerals-2025-12-05.md
    ├── 📁 water/
    │   └── 📁 policy-watch/             # (future) Water-specific Policy Watch notes
    ├── 📁 land-use/
    │   └── 📁 policy-watch/             # (future) Land-use & zoning Policy Watch notes
    └── 📁 historical/
        └── 📁 policy-watch/             # (future) Historical / archival Policy Watch notes
```

### Data, catalogs, and graph (conceptual)

Policy Watch notes often reference live data and graphs, but **do not own** data directories. They point to:

```text
📁 data/
├── 📁 raw/
│   └── 📁 external/
│       └── 📁 <source>/                 # e.g., eia, usgs, noaa, census
├── 📁 processed/
│   └── 📁 external/
│       └── 📁 <source>/                 # Canonical processed layers
└── 📁 stac/
    └── 📁 external/
        └── 📁 <source>/                 # STAC Collections + Items
```

Graph, APIs, and Story Nodes hook in as:

```text
📁 src/
├── 📁 graph/
│   └── 📁 <domain>/                     # Neo4j schema + logic (energy, water, etc.)
├── 📁 api/
│   └── 📁 <domain>/                     # API endpoints exposing domain-specific series
└── 📁 web/
    └── 📁 story-nodes/
        └── 📁 <domain>/                 # Story Nodes & UI for Policy Watch-linked narratives
```

---

## 🧭 Context

Policy Watch notes sit between:

- **External environment:** policy shifts, regulatory changes, major data releases.
- **KFM internals:** ETL, catalogs, graph schema, Story Nodes, and dashboards.

They are designed to answer:

> “What changed out there, why do we care, and what should KFM do about it?”

Common triggers for a new Policy Watch note:

- A new federal or state data product that will become a **baseline dependency**.
- A standard or regulation that affects:
  - Spatial or temporal definitions,
  - Measurement methods,
  - Access and licensing.
- A structural change in recurring reports or scenarios (e.g., EIA AEO restructuring).
- A significant governance or sovereignty development with direct data implications.

---

## 🧱 Architecture

### Policy Watch note structure

Every Policy Watch note must:

- Live under `docs/analyses/<domain>/policy-watch/`.
- Use a filename of the form:

```text
<source-or-topic>-<short-slug>-YYYY-MM-DD.md
```

Examples:

- `eia-data-centers-critical-minerals-2025-12-05.md`
- `ferc-transmission-planning-nopr-2026-02-14.md`
- `kansas-state-data-center-incentives-2026-07-01.md`

Each note:

- Starts with a single **YAML front-matter block**, including:
  - `title`, `path`, `version`, `last_updated`,
  - `doc_kind: "Policy Watch Note"`,
  - governance and catalog profiles (STAC/DCAT/PROV),
  - `scope` and `impacted_modules`.
- Uses the **approved H2 headings**:
  - `## 📘 Overview`
  - `## 🗂️ Directory Layout`
  - `## 🧭 Context`
  - `## 🧱 Architecture`
  - `## 📦 Data & Metadata`
  - `## 🌐 STAC, DCAT & PROV Alignment`
  - `## 🧪 Validation & CI/CD`
  - `## 🧠 Story Node & Focus Mode Integration`
  - `## ⚖ FAIR+CARE & Governance`
  - `## 🕰️ Version History`

### Integration into the pipeline

Policy Watch notes **do not run pipelines themselves**. Instead, they:

- Reference ETL patterns and modules:
  - `src/pipelines/external/<source>/...`
- Specify desired:
  - STAC Collections and Items.
  - DCAT Datasets and Distributions.
  - Neo4j nodes and relationships.
- Inform backlog items and SOPs:
  - New ETL configurations.
  - Schema evolution.
  - Story Node creation and updates.

---

## 📦 Data & Metadata

Policy Watch notes must be explicit about:

- **Data sources**:
  - e.g., EIA, FERC, USGS, NOAA, Census, Kansas state agencies, Tribal governments.
- **Data types**:
  - Time series, surveys, scenarios, administrative boundaries, regulatory dockets.
- **Metadata impacts**:
  - New identifiers, code lists, spatial definitions, temporal coverage changes.
  - Required crosswalks (e.g., across federal lists, jurisdictions, or standards).

Each note should include:

- Clear references to **source documentation** and **machine-readable endpoints**, where allowed.
- A description of **how data will be cataloged**:
  - STAC Collections/Items for geospatial/temporal artifacts.
  - DCAT Datasets/Distributions for tabular or mixed artifacts.
- Any implications for existing **KFM canonical schemas**:
  - New fields or re-interpretation of existing ones.

---

## 🌐 STAC, DCAT & PROV Alignment

Policy Watch notes must:

- Identify which **STAC Collections** and **DCAT Datasets** are:
  - Affected by a change,
  - Newly required,
  - Or deprecated.
- Document the **PROV chain** conceptually:
  - External agent/activity → Source dataset → KFM ETL → KFM derivatives.

For each note, authors should:

- Reference the relevant catalog standards:
  - `docs/standards/catalogs/stac-catalogs-*.md`
  - `docs/standards/catalogs/dcat-datasets-*.md`
  - `docs/standards/provenance/prov-o-usage-*.md`
- Propose how the new or changed external artifacts will:
  - Be represented in STAC (collection IDs, item IDs, assets).
  - Be surfaced as DCAT (dataset IDs, distributions).
  - Be linked via PROV-O (`prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`).

---

## 🧪 Validation & CI/CD

Policy Watch notes are part of the **docs CI** and should pass:

- Front-matter validation (KFM-MDP v11.2.4).
- Heading structure checks (approved H2 registry).
- Governance footer checks.
- Optional custom checks:
  - File naming pattern: `<topic>-YYYY-MM-DD.md`.
  - Presence of `🗂️ Directory Layout` and `🕰️ Version History` sections.

When Policy Watch notes imply **pipeline or schema changes**, they should:

- Reference associated:
  - Issues / tickets (e.g., `kfm#1234`).
  - SOPs in `mcp/sops/`.
  - Experiments in `mcp/experiments/` or model cards in `mcp/model_cards/`.

---

## 🧠 Story Node & Focus Mode Integration

Policy Watch notes should actively **seed Story Nodes**, not just describe data.

For each note, authors should:

- Suggest **candidate Story Node titles** and:
  - Temporal extent (e.g., coverage window of the policy or data).
  - Spatial extent (jurisdiction, region, or network).
- Identify:
  - Key entities (places, datasets, people, institutions) to link in Neo4j.
  - Potential Focus Mode views:
    - Timeline comparisons (before/after policy).
    - Spatial overlays (where policy bites or data changes).
    - Cross-source alignment (e.g., EIA vs USGS vs state datasets).

This README acts as the **template and check-list** for Story Node integration from Policy Watch.

---

## ⚖ FAIR+CARE & Governance

Policy Watch is **governance-heavy by design**:

- FAIR:
  - F: Notes must point to cataloged and findable datasets.
  - A: Access constraints (if any) are documented clearly.
  - I: STAC/DCAT/PROV alignment keeps artifacts interoperable.
  - R: Provenance and licensing make reuse safe and explicit.
- CARE & sovereignty:
  - Notes must **flag** when policies or data touch Indigenous communities or Tribal lands.
  - Any resulting data modeling must respect:
    - Sovereignty,
    - Consent,
    - Appropriate aggregation and redaction.

This README is anchored by:

- `governance_ref: docs/standards/governance/ROOT-GOVERNANCE.md`
- Any additional, domain-specific governance docs referenced in downstream notes.

---

## 🕰️ Version History

| Version   | Date       | Author       | Notes                                              |
|----------|------------|-------------|----------------------------------------------------|
| v11.2.4  | 2025-12-07 | KFM AI Lead | Initial Policy Watch analyses README scaffolded.   |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  

[🏠 Monorepo Root](/) · [📊 Analyses Overview](../README.md) · [⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>

