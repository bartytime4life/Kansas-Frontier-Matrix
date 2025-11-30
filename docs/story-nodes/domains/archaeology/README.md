---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Domain (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/archaeology/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
status: "Active / Governed"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

license: "CC-BY 4.0"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
story_node_schema_ref: "schemas/json/story-node.schema.json"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Domain README"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "story-nodes/archaeology"
  applies_to:
    - "story-node-authoring"
    - "focus-mode"
    - "graph-linking"

fair_category: "F1-A1-I1-R1"
care_label: "Culturally-Sensitive · Indigenous-Linked"
sensitivity: "Medium"
indigenous_rights_flag: true
ontology_alignment:
  cidoc: "E18 Physical Thing / E27 Site / E31 Document / E63 Beginning of Existence"
  schema_org: "CreativeWork"
  prov_o: "prov:Entity"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

requires_directory_layout_section: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🏺 **Kansas Frontier Matrix — Archaeology Story Node Domain**
`docs/story-nodes/domains/archaeology/README.md`

**Purpose:**  
Define how to model, write, and validate **Story Nodes** for archaeological content in the Kansas Frontier Matrix,  
so that fieldwork, sites, features, artifacts, and interpretations are represented safely, consistently, and  
ready for **Focus Mode** and knowledge-graph integration.

</div>

---

## 📘 Overview

This README describes the **archaeology domain profile** for KFM Story Nodes:

- How to represent **sites, contexts, stratigraphy, features, artifacts, surveys, and lab work** as Story Nodes.
- How to ground archaeological narratives in **space**, **time**, and **provenance** while respecting **FAIR+CARE** and **Indigenous data sovereignty**.
- How archaeology Story Nodes connect into:
  - the **Neo4j** knowledge graph (sites, events, people, collections),
  - the **Story Node JSON schema**,
  - and **Focus Mode** (entity-centric exploration across map + timeline).

Use this document whenever you:

- Draft a new archaeology Story Node (Markdown or JSON).
- Link excavation records, surveys, or lab analyses into the KFM narrative graph.
- Review PRs that add or modify archaeology-related Story Nodes or templates.

---

## 🗂️ Directory Layout

The archaeology domain lives under `docs/story-nodes/domains/archaeology/` and is expected to follow this structure:

~~~text
docs/story-nodes/domains/archaeology/
├── README.md                           # This file: domain overview & authoring rules
├── templates/
│   ├── story-node-archaeology.md       # Human-facing authoring template (Markdown)
│   ├── story-node-archaeology.json     # JSON skeleton matching story-node.schema.json
│   └── relation-patterns.md            # Common relation patterns (site ↔ feature ↔ document)
├── examples/
│   ├── protohistoric-wichita-site.json # Example Story Node (generalized Protohistoric site)
│   ├── fort-larned-geophysics.json     # Example (non-invasive survey Story Node)
│   └── ...                             # Additional curated examples
├── glossary.md                         # Archaeology-specific terms (context, feature, locus, etc.)
└── notes/
    ├── backlog.md                      # Draft candidates for future Story Nodes
    └── ethics-checklist.md             # Domain-specific CARE/sovereignty considerations
~~~

> If a file or folder above does not yet exist, treat it as **expected future structure** and align new content with this layout.

---

## 🧭 Context

The archaeology domain module sits at the intersection of:

- **Archaeology (MCP Domain Module)** — core disciplinary theory, field methods, stratigraphy, dating, and lab analysis; including careful context recording and the irreversibility of excavation.
- **KFM Knowledge Graph** — where:
  - *Sites* and *features* map to **Places** and **Events** (e.g., excavations, surveys, discoveries).
  - *Actors* (archaeologists, tribal partners, landowners) map to **People / Organizations**.
  - *Records* (field forms, drawings, photos, 3D scans, reports) map to **Documents / Assets**.
- **Story Nodes** — narrative units that:
  - explain **what is known** about a site or investigation,
  - how it was **discovered**, **documented**, and **interpreted**,
  - and how that understanding has **changed over time**.

Archaeology Story Nodes are **not** excavation logs or full site reports. Instead, they are:

- **Synthesized narratives** anchored to:
  - a **spatial footprint** (site extents, survey areas, generalized locations),
  - a **time interval** (occupation phases, investigation dates),
  - and **graph links** (people, documents, datasets).
- Designed to be **safe to publish**, respecting:
  - **legal protections** (e.g., site confidentiality),
  - **tribal and community preferences**, and
  - KFM’s **Indigenous data sovereignty** policy.

---

## 🧠 Story Node & Focus Mode Integration

This domain profile extends the generic `story-node.schema.json` with archaeology-focused conventions:

### 1. Core Story Node fields

Every archaeology Story Node **must**:

- Set `"type": "story-node"`.
- Provide:
  - `title` – e.g., `"Protohistoric Village near Lower Walnut Creek (Generalized)"`.
  - `summary` – 1–2 sentence abstract for cards and Focus Mode preview.
  - `narrative.body` – a well-structured explanation (Markdown recommended) focusing on:
    - site context and significance,
    - periods of occupation/use,
    - key discoveries,
    - interpretive uncertainties and debates.
  - `spacetime.geometry` – a **generalized** GeoJSON geometry (see Data & Metadata).
  - `spacetime.when` – at least a `start` date/time plus `precision` (e.g. `"year"` or `"day"`).
- Use `relations[]` to connect the Story Node into the broader graph:
  - `rel: "about"` → the primary **site** or **excavation event** node.
  - `rel: "references"` → reports, publications, archival photographs, or datasets.
  - `rel: "counterpoint"` → later reinterpretations or critiques (e.g. revised dating or cultural attributions).

### 2. Domain-specific narrative guidance

When writing archaeology Story Nodes:

- **Do not** publish exact site coordinates or detailed access instructions for **sensitive or unprotected sites**.
- Clearly differentiate:
  - **Observation** (what was actually found: features, artifacts, stratigraphy),
  - **Interpretation** (what those findings likely mean),
  - **Speculation** (what might be the case but is not yet supported).
- Always capture:
  - How the context was recorded (grid, total station, photogrammetry, geophysics).
  - What **dating methods** (radiocarbon, dendrochronology, OSL, typology) were used.
  - Whether interpretations are **widely accepted**, **contested**, or **provisional**.

### 3. Focus Mode behavior

When a user triggers Focus Mode on an archaeology Story Node:

- The **timeline** should:
  - zoom to the relevant window (e.g., primary occupation range plus investigation dates),
  - highlight linked events (excavation seasons, survey campaigns, major publications).
- The **map** should:
  - center on the **generalized** geometry (e.g., 10 km buffered area, county-level polygon),
  - optionally toggle archaeology-related layers (e.g., generalized site density, survey coverage).
- The **Focus panel** should:
  - show the Story Node summary,
  - list related:
    - People (excavators, curators, tribal partners),
    - Events (excavations, surveys, reinterpretations),
    - Documents (reports, theses, articles),
    - Assets (photos, scans, geophysics rasters).
  - surface **AI-assisted insights** only when:
    - they can be grounded in actual documented data and references,
    - and they do not reveal restricted information (no “AI guessing” site locations or sacred details).

---

## 📦 Data & Metadata (Archaeology Profile)

This section standardizes **IDs**, **geometry**, **time**, and **provenance** for archaeology Story Nodes.

### 1. IDs

Use **stable**, non-derivative IDs that do **not** expose confidential site codes.

Recommended pattern:

- `arch-ks-{county-fips}-{short-slug}-{nn}`
  - Example: `arch-ks-165-lower-walnut-village-01`

If you need to reference an internal site number (e.g., state site number), keep it in:

- `narrative.body` **only if** it is already public, **or**
- a separate, **non-public** internal graph node; **do not** put confidential codes in public Story Node IDs.

### 2. Geometry generalization

To protect sites while still grounding narratives spatially:

- Use **generalized geometries**:
  - A **county polygon** or large buffer for sensitive pre-contact sites.
  - A coarser **H3 cell** (e.g. resolutions ~6–7) for unpublished locations.
- Only use more precise footprints (e.g., fort outlines, public parks, museums) for:
  - already well-known, publicly signposted locations, **and**
  - places with low risk of looting or harm.

If the exact geometry is known but must be masked:

- Store the precise coordinates only in **restricted internal graph nodes**.
- Use `spacetime.place_labels` for human-readable names (e.g., `"Smoky Hill region"`, `"Arkansas River near Great Bend"`).

### 3. Temporal modeling

For `spacetime.when`:

- Use `precision` to reflect **actual** chronological resolution:
  - `"year"` for radiocarbon ranges,
  - `"day"` or `"minute"` only for well-documented modern activities (e.g., 2012 excavation seasons).
- Use `original_label` to preserve the historian/archaeologist’s phrasing:
  - e.g., `"original_label": "Protohistoric, ca. 1450–1650 CE"`.

For multi-phase sites:

- Prefer **multiple Story Nodes** or **relations** over flattening everything into one node:
  - Example:
    - `arch-ks-xxx-site-occupation-phase-1`
    - `arch-ks-xxx-site-occupation-phase-2`
  - Linked via `relations.rel = "part-of"` or `"follows"`.

### 4. Provenance & assets

Where possible:

- Link to **open-access** assets (photos, 3D models, maps) via `narrative.media[]` and/or the `stac.assets[]` hint block.
- For each media item, include at least:
  - `href`
  - `title`
  - `mime`
  - `license` (or clear usage status).

Avoid attaching media that:

- shows **precise site entrances**, **unmarked burials**, or **unpublished sensitive contexts**, unless explicitly cleared by appropriate stewards.

---

## 🧪 Validation & CI/CD

Archaeology Story Nodes participate in the standard KFM validation pipeline:

- **JSON Schema validation**
  - All JSON Story Nodes must validate against `story-node.schema.json`.
- **Markdown protocol checks**
  - Any Markdown Story Node or authoring doc must follow KFM-MDP v11.2.2 (single fenced block, headings, metadata).
- **Spatial/temporal checks**
  - Ensure `spacetime.geometry` is valid GeoJSON and `when.start` is ISO 8601.
  - Confirm that `precision` and `original_label` are consistent.
- **Ethics/sovereignty linting**
  - Automated checks plus human review for:
    - suspiciously precise coordinates in sensitive contexts,
    - references to burials, sacred sites, or restricted knowledge.
  - PRs may be blocked until an **Indigenous data / archaeology reviewer** signs off.

Add new validation rules for this domain in:

- `tests/story-nodes/archaeology/` (unit tests),
- CI workflow (e.g., `stac-validate`, `story-node-schema-lint`, `sovereignty-check` stages).

---

## ⚖ FAIR+CARE & Governance

Archaeology is a high-risk domain from a **cultural heritage** and **looting** perspective. This domain profile therefore:

- Enforces **CARE-aligned masking** for:
  - burial sites,
  - sacred places,
  - unpublished or vulnerable sites,
  - locations identified primarily through tribal knowledge.
- Requires:
  - **consultation with relevant tribal nations** and local stewards for new Story Nodes involving Indigenous heritage.
  - use of the KFM Indigenous data sovereignty policy for decisions on what is or is not appropriate to publish.
- Emphasizes that:
  - Story Nodes should **not** be used to “gamify” site locations or encourage unsupervised visits.
  - AI summaries **must not** invent or speculate about site coordinates, hidden features, or unapproved interpretations.

When in doubt, **generalize more** and **explain the uncertainty** explicitly in the narrative.

---

## 🕰️ Version History

- **v11.2.2 (2025-11-30)**
  - First governed archaeology domain README.
  - Defines directory layout, Story Node conventions, and ethics/sovereignty guidance.
  - Hooks archaeology Story Nodes into Focus Mode v3, graph, and CI validation.

---

<div align="center">

[📚 Docs Root](../../../README.md) · [📐 Standards Index](../../../standards/README.md) · [⚖️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

