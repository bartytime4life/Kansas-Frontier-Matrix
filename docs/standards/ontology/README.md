---
title: "🧭 Kansas Frontier Matrix — Ontology Standards & Graph Semantics"
path: "docs/standards/ontology/README.md"
version: "v10.3.1"
last_updated: "2026-01-12"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
ontology_stack: "CIDOC-CRM • GeoSPARQL • OWL-Time • W3C PROV-O"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Ontology Standards**
`docs/standards/ontology/README.md`

Semantic rules for how **KFM represents People, Places, Events, Datasets, Documents, and Provenance** across:
**Neo4j (property graph)**, **PostGIS (geometry)**, and **API contracts (OpenAPI/JSON Schema + GraphQL)**.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-brightgreen" />
<img alt="Ontology" src="https://img.shields.io/badge/Ontology-v10.3.1-orange" />
<img alt="CIDOC-CRM" src="https://img.shields.io/badge/CIDOC--CRM-Mapped-blue" />
<img alt="GeoSPARQL" src="https://img.shields.io/badge/GeoSPARQL-Enabled-6aa84f" />
<img alt="OWL-Time" src="https://img.shields.io/badge/OWL--Time-Enabled-7f6000" />
<img alt="PROV-O" src="https://img.shields.io/badge/W3C%20PROV--O-Provenance-purple" />
<img alt="STAC+DCAT" src="https://img.shields.io/badge/STAC%20%2B%20DCAT-Interoperable-0b5394" />

</div>

---

## 🧠 What “Ontology” Means in KFM

KFM’s ontology is the **shared semantic contract** that answers:

- **What things exist** in KFM? (e.g., *Person*, *Place*, *Event*, *Dataset*, *Document*)
- **How they relate** (e.g., *participated in*, *occurred at*, *derived from*, *describes*)
- **How time and space are modeled** (intervals, uncertain dates, geometry, topology)
- **How provenance & trust are enforced** (W3C PROV-O, evidence links, validation gates)
- **How this maps to implementation** (Neo4j labels/relationships, PostGIS features, STAC/DCAT, API types)

> ✅ KFM is explicitly **standards-based**, mapping historical/cultural entities to **CIDOC-CRM**, and using **GeoSPARQL + OWL-Time** for geospatial and temporal semantics.  
> ✅ KFM uses **Neo4j** to link entities (people, places, events, datasets, documents) and enable semantic queries across space + time.  
> ✅ KFM uses **STAC** and **DCAT** for catalog/metadata, and **W3C PROV** for lineage & transparency.

---

## 🧭 Quick Navigation

- [🎯 Goals & Non-Goals](#-goals--non-goals)
- [🧱 Ontology Layers](#-ontology-layers)
- [🧩 Canonical Entity Types](#-canonical-entity-types)
- [🔗 Canonical Relationship Patterns](#-canonical-relationship-patterns)
- [🆔 IDs, Names & Versioning](#-ids-names--versioning)
- [🕰️ Time Modeling](#️-time-modeling)
- [🌍 Space & Geometry Modeling](#-space--geometry-modeling)
- [🧬 Provenance & Lineage](#-provenance--lineage)
- [🛡️ FAIR+CARE Governance](#️-faircare-governance)
- [✅ Validation & CI Gates](#-validation--ci-gates)
- [🧰 Integration Points](#-integration-points)
- [🤝 Contribution Workflow](#-contribution-workflow)
- [📎 References](#-references)

---

## 🎯 Goals & Non-Goals

### ✅ Goals
- Define **stable semantic meaning** for KFM’s core graph.
- Ensure **interoperability** via mappings to:
  - **CIDOC-CRM** (heritage/history),
  - **GeoSPARQL** (space),
  - **OWL-Time** (time),
  - **W3C PROV-O** (provenance),
  - **STAC + DCAT** (catalog + dataset metadata).
- Enforce **FAIR+CARE** constraints (sensitivity, access patterns, redaction rules).
- Make ontology changes **auditable and reproducible** via CI/Policy gates.

### 🚫 Non-Goals
- This is **not** a full RDF/OWL tutorial.
- This is **not** a replacement for API schemas:
  - Ontology = *meaning*  
  - Schemas = *shape/validation*  
  - OpenAPI = *transport contract*  
- This doc does **not** prescribe UI layout or styling (see UI schema docs).

---

## 🧱 Ontology Layers

KFM’s ontology is layered so we can keep the core stable while allowing domain growth.

### 🟦 Layer 0 — Core KFM Concepts (Stable)
- **Person / Organization**
- **Place / Feature**
- **Event / TimeSpan**
- **Dataset / Observation**
- **Document / Evidence**
- **Provenance Activity / Agent / Entity** (PROV)

### 🟩 Layer 1 — Domain Profiles (Extendable)
Examples: 🌊 hydrology, 🌦 climatology, 🏺 archaeology, 📜 treaties, 🚜 agriculture, 🛤 infrastructure

### 🟨 Layer 2 — Controlled Vocabularies (SKOS-style)
- Topics, hazards, instrument types, role types, event categories, uncertainty qualifiers, etc.

### 🟥 Layer 3 — Policy & Governance Tags
- CARE sensitivity class, access tier, geometry redaction level, retention rules, licensing flags

---

## 🗂️ Suggested Directory Layout

> This folder is the **human-readable standard**. Ontology artifacts (if/when added) should live adjacent to it.

```text
docs/standards/ontology/
├── README.md                      🧭 (you are here)
├── core/                          🧱 Core semantics (stable)
│   ├── entities.md                🧩 Canonical entity definitions
│   ├── relationships.md           🔗 Canonical relationship patterns
│   ├── time.md                    🕰️ OWL-Time mapping rules
│   ├── geo.md                     🌍 GeoSPARQL mapping rules
│   └── provenance.md              🧬 PROV-O mapping rules
├── profiles/                      🧪 Domain profiles (extendable)
│   ├── hydrology.md               🌊
│   ├── climatology.md             🌦️
│   ├── archives.md                📜
│   └── archaeology.md             🏺
└── governance/                    🛡️ Ontology policy overlays
    ├── sensitivity.md             🔒 CARE-driven constraints
    └── deprecation.md             🧯 Deprecation + migration rules
```

---

## 🧩 Canonical Entity Types

> **Rule of thumb:** If two contributors model the same real-world concept, they should land on the **same label/type** and **the same core properties**.

| Canonical Type | Neo4j Label (recommended) | Meaning | External Alignment |
|---|---|---|---|
| Person | `Person` | Individual human actor | CIDOC-CRM “Actor” pattern (via `E21 Person`) |
| Organization | `Organization` | Group/agency/tribe/institution | CIDOC-CRM Actor pattern |
| Place | `Place` | Named place; can be administrative or vernacular | CIDOC-CRM `E53 Place` + Geo semantics |
| Feature | `Feature` | Spatial feature (point/line/polygon) | GeoSPARQL Feature pattern |
| Event | `Event` | Historical event, hazard, action, occurrence | CIDOC-CRM event pattern (e.g., `E5 Event`) |
| TimeSpan | `TimeSpan` | A time interval (including uncertainty) | OWL-Time |
| Dataset | `Dataset` | Published dataset (metadata-first) | DCAT |
| STAC Item | `StacItem` | Spatio-temporal asset item | STAC |
| Asset | `Asset` | File/COG/GeoTIFF/NetCDF/etc | STAC Asset semantics |
| Observation | `Observation` | Measured/derived value with context | PROV + domain model |
| Document | `Document` | Evidence artifact (PDF, scan, article) | Dublin Core-ish + PROV |
| Story Node | `StoryNode` | Narrative unit linking evidence + map layers | KFM-native |
| Provenance Activity | `ProvActivity` | An action that used/generated entities | W3C PROV-O |
| Provenance Agent | `ProvAgent` | Actor responsible for an activity | W3C PROV-O |
| Provenance Entity | `ProvEntity` | Versioned artifact in lineage | W3C PROV-O |

> 💡 KFM’s GraphQL schema should **mirror these types** (e.g., `Person`, `Place`, `Event`) so clients can traverse the graph semantically without bespoke mapping code.

---

## 🔗 Canonical Relationship Patterns

### 🧠 “Minimum useful” graph patterns (KFM canonical)

| Pattern | Neo4j Relationship (recommended) | Meaning |
|---|---|---|
| Person ↔ Event | `(:Person)-[:PARTICIPATED_IN]->(:Event)` | Participation / involvement |
| Event ↔ Place | `(:Event)-[:OCCURRED_AT]->(:Place)` | Event location (may be approximate) |
| Document ↔ Event | `(:Document)-[:DESCRIBES]->(:Event)` | Evidence describing an event |
| Document ↔ Place | `(:Document)-[:MENTIONS_PLACE]->(:Place)` | Text mentions of places |
| Dataset ↔ Place | `(:Dataset)-[:COVERS]->(:Place)` | Dataset spatial coverage |
| Dataset ↔ TimeSpan | `(:Dataset)-[:TEMPORAL_COVERAGE]->(:TimeSpan)` | Dataset temporal coverage |
| STAC Item ↔ Dataset | `(:StacItem)-[:MEMBER_OF]->(:Dataset)` | Item belongs to dataset/collection |
| Asset ↔ STAC Item | `(:Asset)-[:ASSET_OF]->(:StacItem)` | File is an item asset |
| Observation ↔ Feature/Place | `(:Observation)-[:OBSERVED_AT]->(:Feature)` | Observation location |
| Observation ↔ TimeSpan | `(:Observation)-[:OBSERVED_DURING]->(:TimeSpan)` | Observation time |
| Any ↔ Provenance | `prov:*` mapped relationships | Lineage, derivation, attribution |

### ✅ Relationship rules (hard constraints)
- **Directionality matters** (choose a direction; don’t randomly reverse it).
- Every edge must be **meaningful without reading properties**.
- Relationship names use `UPPER_SNAKE_CASE` and read like a verb phrase.
- Avoid duplicates:
  - Prefer `DESCRIBES` + typed nodes over multiple synonyms (`REFERS_TO`, `TALKS_ABOUT`, etc.)
- Use **reification** (a node) if:
  - you need uncertainty, confidence, sources, or temporal qualifiers on the relationship.

<details>
<summary>🧷 Example: Relationship reification (when you need confidence + citation)</summary>

```cypher
// Instead of a bare edge with many properties…
(:Document)-[:MENTIONS_PLACE]->(:Place)

// …use a Mention node so you can store confidence + offsets + citations safely:
(:Document)-[:HAS_MENTION]->(m:Mention {confidence: 0.82, textSpan: "…"})
(m)-[:MENTION_OF]->(:Place)
(m)-[:SUPPORTED_BY]->(:Evidence {source_id: "doc:ks-archive-001#p3"})
```

</details>

---

## 🆔 IDs, Names & Versioning

### 📌 Dataset IDs (canonical)
Dataset IDs should follow:

`kfm.<state|region>.<theme>.<year_range>.v<version>`

Example:
- `kfm.ks.landcover.2000_2020.v1`

These IDs may appear in:
- file paths ✅
- STAC collection/item IDs ✅
- database keys ✅
- provenance records ✅

### 🧷 Entity IDs (recommended)
Use stable, explicit IDs so merges are deterministic.

**Preferred formats:**
- `urn:kfm:<type>:<namespace>:<id>`
- `kfm:<type>:<id>` (short form inside KFM)

Examples:
- `urn:kfm:person:ks:000123`
- `urn:kfm:place:ks:topeka`
- `urn:kfm:event:ks:1861-bleeding-kansas-episode-004`

**Rules:**
- IDs are immutable once published.
- New information ⇒ new versioned entity **or** new provenance describing revision (see PROV section).
- If an entity is merged, the losing ID becomes an **alias** (never silently disappears).

---

## 🕰️ Time Modeling

KFM treats time as **first-class** because:
- story nodes and map layers are temporal,
- events are time-bound,
- datasets have temporal coverage,
- provenance has timestamps.

### ✅ Canonical time representation
- Prefer explicit **TimeSpan** nodes when time is:
  - an interval,
  - uncertain,
  - derived from sources,
  - or shared across multiple entities.

**TimeSpan (recommended properties):**
- `start` (ISO 8601 date/time)
- `end` (ISO 8601 date/time)
- `precision` (day/month/year/approx)
- `uncertainty` (optional; qualitative or numeric)
- `source_ref` (evidence pointer)

### OWL-Time alignment (semantic intent)
- `TimeSpan.start` → `time:hasBeginning`
- `TimeSpan.end` → `time:hasEnd`
- `precision/uncertainty` → encoded as qualifiers + provenance

> 🧠 If time is ambiguous (e.g., “late 1800s”), store **a bounded interval** + a precision flag, and attach the original phrase as evidence.

---

## 🌍 Space & Geometry Modeling

KFM uses a hybrid approach:
- **PostGIS** is the source of truth for heavy geometry.
- **Neo4j** stores semantic links, plus lightweight spatial metadata (bbox, centroid, H3, etc.)
- **GeoSPARQL intent** guides relationships like *within*, *intersects*, *contains*.

### ✅ Geometry rules
- Store authoritative geometry in PostGIS (vector) or as assets (COG/GeoTIFF).
- In Neo4j, store:
  - `bbox` (minx, miny, maxx, maxy)
  - `centroid` (lat, lon)
  - `h3` indexes (optional but recommended for fast neighborhood queries)
  - `geom_ref` pointer to PostGIS row / asset URL

### GeoSPARQL alignment (semantic intent)
Map these concepts into Neo4j relationships:
- `sfWithin` → `WITHIN`
- `sfContains` → `CONTAINS`
- `sfIntersects` → `INTERSECTS`

> 🔒 CARE note: sensitive features may require generalized geometry or masked indices (see Governance).

---

## 🧬 Provenance & Lineage

KFM’s “no black box” rule depends on provenance.

### ✅ W3C PROV-O (conceptual mapping)
- **Activity** = something happened (ETL run, OCR pass, model run, PR merge)
- **Entity** = something versioned (dataset release, STAC item, document, model artifact)
- **Agent** = who/what did it (human maintainer, CI bot, approved agent)

### 🔁 DevOps provenance (GitHub PR → PROV graph)
KFM plans to represent GitHub Pull Requests as PROV:
- PR = **PROV Activity**
- Commits = **PROV Entities**
- Authors/Reviewers/CI bot = **PROV Agents**
- Relations:
  - `prov:used` (PR uses commits)
  - `prov:wasAssociatedWith` (PR ↔ author/bot)
  - `prov:wasGeneratedBy` (merge commit ↔ PR)

### 🧾 Practical rule: everything important must be attributable
If an entity is user-facing (map layer, story node, dataset release), it must have:
- **source evidence** links (documents, URLs, citations)
- **provenance activity** links (what produced it)
- **agent attribution** (who approved/published)

---

## 🛡️ FAIR+CARE Governance

KFM’s ontology is not just “types”—it encodes ethical handling rules.

### FAIR (Findable, Accessible, Interoperable, Reusable)
Ontology requires:
- stable IDs ✅
- rich metadata ✅
- standards alignment ✅
- explicit licenses & versioning ✅

### CARE (Collective benefit, Authority to control, Responsibility, Ethics)
Ontology requires:
- sensitivity classification for certain places/features/documents
- masking rules for vulnerable sites
- access-tier metadata for restricted artifacts
- explicit “do not display at high zoom” constraints for protected geometry

### Policy-as-code enforcement 🧩
KFM’s governance direction includes:
- **OPA (Rego)** + **Conftest** policy gates
- rules for FAIR/CARE, retention, sensitive coordinates, licensing constraints
- automated CI rejection if changes violate policies

> ⚠️ If the ontology introduces a new entity type that can carry sensitive information (e.g., archaeological sites, private land use), it **must** define:
> - sensitivity tag vocabulary
> - minimum redaction behavior
> - review gate requirements

---

## ✅ Validation & CI Gates

Ontology changes must be **validated before merge**.

### Recommended validation layers
1. **Schema validation** (JSON Schema / OpenAPI contract alignment)
2. **Graph consistency validation**
   - required labels & relationships exist
   - forbidden edges not introduced
   - unique constraints hold
3. **Temporal/spatial validation**
   - time intervals valid (start ≤ end)
   - bbox valid (min ≤ max)
   - geometry references resolvable
4. **Provenance validation**
   - published artifacts have `prov` links
   - required attribution present
5. **Policy gate**
   - OPA checks for FAIR+CARE rules

### CI pipeline model (conceptual)
KFM’s “Detect → Validate → Promote” approach is the template:
- Detect changes (files, data, external signals)
- Validate with fast checks + domain “lane validators”
- Promote via signed PR + lineage events

---

## 🧰 Integration Points

### 🔌 APIs & Contracts
- **REST APIs** should expose ontology types via schemas.
- **GraphQL** should mirror the knowledge graph types for traversal queries.
- **STAC + DCAT** remain the primary metadata publishing formats for datasets/assets.

See also:
- `api/contracts/openapi/` 📜
- `api/contracts/schemas/stac/` 🛰️
- `api/contracts/schemas/ui/` 🧩

### 🧠 Agents & Automation
Ontology drives:
- agent tool selection and safe write boundaries,
- schema/graph validation in pipelines,
- provenance stamping.

See:
- `docs/architecture/agents/README.md` 🧠

### 🗺️ UI / Focus Mode
Ontology enables:
- “show me events related to X at Y during Z”
- story nodes that can cite evidence and link layers
- safe, explainable answers (evidence-backed)

---

## 🤝 Contribution Workflow

### ✅ When adding or extending ontology
1. **Open an issue** describing the semantic gap.
2. Add/extend the **canonical type** (or domain profile).
3. Add **relationship patterns** (with direction + meaning).
4. Define **minimum required properties**.
5. Add/update **policy constraints** (FAIR+CARE).
6. Update **contracts/schemas** if exposed via API.
7. Run validation gates.
8. Submit a PR for review (never self-merge).

### 🧯 Deprecation rules
- Deprecate, don’t delete.
- Provide a migration mapping:
  - old label/relationship → new one
- Keep aliases for IDs.

---

## 📎 References

These project documents informed the ontology stance and governance direction:

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** 📘  
  (knowledge graph integration, standards-based design: STAC/DCAT/PROV; CIDOC-CRM + GeoSPARQL/OWL-Time alignment; dataset ID conventions)

- **🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals** 💡  
  (PROV graph integration for GitHub PRs; policy-as-code via OPA/Rego; validation-first CI)

- **Audit of the Kansas Frontier Matrix (KFM) Repository** 🔎  
  (calls out the need for explicit schema/ontology documentation and clear node/relationship listings)

- **Supporting research PDFs** 📚  
  (graph/network analysis foundations, modeling & simulation rigor, data platform patterns)

---

<div align="center">

### 🗺️ “If it can’t be traced, it can’t be trusted.”  
**Ontology + Provenance + Policy Gates = KFM’s auditable living atlas.** ✨

</div>
