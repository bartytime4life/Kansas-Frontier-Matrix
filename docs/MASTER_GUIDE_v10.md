---
title: "📚 Kansas Frontier Matrix — Master Guide v10 (Legacy Reference; v12 is canonical)"
path: "docs/MASTER_GUIDE_v10.md"
version: "v10.3.2"
last_updated: "2025-12-27"
status: "legacy"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:master-guide:v10.3.2"
semantic_document_id: "kfm-master-guide-v10.3.2"
event_source_id: "ledger:kfm:doc:master-guide:v10.3.2"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 📚 Kansas Frontier Matrix — MASTER GUIDE v10 (Legacy)

**Architecture · Data · AI · UX · Governance**  
`docs/MASTER_GUIDE_v10.md`

**Status:** Legacy reference (v10-era).  
**Canonical successor:** `docs/MASTER_GUIDE_v12.md` (draft) — pipeline ordering + invariants + extension matrix.

</div>

---

> **Important (do not ignore):** This v10 guide is retained for historical continuity.  
> The **canonical pipeline ordering** and the strictest invariants now live in **Master Guide v12** (draft).  
> When in doubt, follow: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

---

## 📘 Overview

### Purpose

- Serve as a **v10-era master reference** for the Kansas Frontier Matrix (KFM): architecture, data lifecycle, metadata alignment, and narrative rules.
- Preserve **non-negotiable system invariants** that prevent provenance loss, governance bypass, and UI/graph boundary violations.
- Provide an **audit-friendly orientation** for contributors working across ETL, cataloging, graph, API, UI, and story layers.

### Scope

| In Scope | Out of Scope |
|---|---|
| Canonical pipeline ordering (v10 baseline) and invariants | Deployment secrets, credentials, or internal infrastructure details |
| Repository layout expectations and “what goes where” rules | Vendor-specific runbooks not captured in repo |
| STAC/DCAT/PROV alignment requirements | Large raw data snapshots embedded in docs |
| Subsystem contract expectations (ETL, catalogs, graph, APIs, UI, story) | Unreviewed policy changes (must go through governance) |
| Focus Mode + Story Node provenance rules | “Freeform narrative” without citations/evidence |

### Audience

- **Primary:** KFM maintainers and contributors editing governed docs, pipelines, catalogs, and ontology.
- **Secondary:** Reviewers performing FAIR+CARE / sovereignty / security reviews.
- **Tertiary:** UI and narrative curators integrating Story Nodes into Focus Mode.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo — add if missing)*  
- Core terms referenced here:
  - **Evidence artifact:** STAC/DCAT/PROV objects consumed downstream
  - **Contract artifact:** schemas/specs treated as canonical (validated in CI)
  - **Story Node:** governed narrative doc with citations to evidence artifacts
  - **Focus Mode:** interactive story/analysis view (must be provenance-linked)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + extension matrix (draft successor) | `docs/MASTER_GUIDE_v12.md` | KFM Core | v12 is canonical baseline |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Not confirmed in repo (recommended canonical path) |
| Full architecture vision (draft) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | Not confirmed in repo (recommended canonical path) |
| Example governed domain module | `docs/data/historical/land-treaties/README.md` | Domain owners | Not confirmed in repo (example reference) |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required for governed docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Required for new Story Nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for contract changes |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | FAIR+CARE Council | Required reference for governed docs |
| Ethics policy | `docs/governance/ETHICS.md` | FAIR+CARE Council | Required reference for governed docs |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | FAIR+CARE Council | Required reference for governed docs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid, and `path:` matches file location
- [ ] Canonical pipeline ordering stated and matches successor guidance
- [ ] Directory placement rules are explicit (no “mystery folders”)
- [ ] Validation gates are listed and actionable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty constraints are explicit (no bypasses)
- [ ] Footer references include governance/ethics/sovereignty links

---

## 🗂️ Directory Layout

### This document

- `path`: `docs/MASTER_GUIDE_v10.md` *(must match front-matter)*

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed domain data; catalog outputs by stage |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV evidence + lineage bundles |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog builders |
| Graph | `src/graph/` (+ `data/graph/` imports if present) | Ontology bindings, constraints, graph build/import fixtures |
| API boundary | `src/server/` *(preferred)* or `src/api/` *(legacy)* | Contracts, redaction, query services; UI never reads Neo4j directly |
| UI | `web/` | React + map clients; layer registry; a11y gates |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts rendered in Focus Mode |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/telemetry/UI config) |
| CI | `.github/` | Workflows and CI gates |
| Tools | `tools/` | Validators, CLI utilities |
| Tests | `tests/` | Unit/integration/contract/e2e tests |
| MCP | `mcp/` | Runs, experiments, model cards, SOPs |
| Releases | `releases/` | Versioned packaged artifacts (manifests, SBOMs, snapshots) |

### Repo top-levels (expected)

~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### Expected file tree (recommended; some directories may not exist yet)

~~~text
📁 KansasFrontierMatrix/
├── 📁 .github/
│   └── 📁 workflows/
├── 📁 data/
│   ├── 📁 <domain>/
│   │   ├── 📁 raw/                 # untouched landings (or pointers/manifests)
│   │   ├── 📁 work/                # intermediates/staging
│   │   └── 📁 processed/           # certified outputs (ready for catalog + graph)
│   ├── 📁 stac/                    # STAC collections + items (all domains)
│   ├── 📁 catalog/
│   │   └── 📁 dcat/                # DCAT datasets + distributions
│   ├── 📁 prov/                    # PROV lineage bundles
│   └── 📁 graph/                   # graph import fixtures (CSV, cypher, etc.) (optional)
├── 📁 docs/
│   ├── 📄 MASTER_GUIDE_v10.md
│   ├── 📄 MASTER_GUIDE_v12.md      # successor draft (canonical)
│   ├── 📁 templates/
│   ├── 📁 standards/
│   ├── 📁 governance/
│   ├── 📁 architecture/
│   ├── 📁 reports/
│   │   └── 📁 story_nodes/
│   ├── 📁 telemetry/
│   └── 📁 security/
├── 📁 schemas/
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/                  # preferred API boundary (or legacy src/api/)
├── 📁 web/
├── 📁 mcp/
│   ├── 📁 runs/
│   └── 📁 experiments/
├── 📁 tests/
├── 📁 tools/
└── 📁 releases/
~~~

---

## 🧭 Context

### Background

The **Kansas Frontier Matrix (KFM)** is a unified, semantic, geospatial–temporal system for reconstructing **Kansas through time** — historically, ecologically, hydrologically, and culturally — while ensuring:

- **Provenance-first evidence**
- **Deterministic, reproducible pipelines**
- **FAIR+CARE governance and sovereignty safeguards**
- **Narratives that remain evidence-linked**

### What’s driving the next evolution (v10 → v12+)

- **Scaling:** more domains, more evidence products, more narrative interactivity.
- **Governance:** stronger provenance + sovereignty enforcement as content grows.

### Key invariants (do not break)

1. **Canonical ordering (end-to-end):**  
   **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
2. **UI boundary rule:** UI only consumes data via **APIs or published catalogs**, **never directly from Neo4j**.
3. **No unsourced narrative:** Focus Mode contexts must be provenance-linked; no “orphan facts.”
4. **Contracts are canonical:** contract artifacts must live in-repo and validate in CI (schemas, OpenAPI/GraphQL, UI schemas).
5. **Classification propagation:** no derived output may be **less restricted** than any input in its lineage.

### “Extension Matrix” (where changes must land)

| Extension type | ETL | STAC/DCAT/PROV | Graph | APIs | UI | Story Nodes | Focus Mode | Governance |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| New domain dataset | ✓ | ✓ | ✓ | ✓ | optional | optional | optional | ✓ |
| New evidence artifact type (as STAC asset) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New entity/edge type (ontology) | — | — | ✓ | ✓ | optional | optional | optional | ✓ |
| New API endpoint / query capability | — | — | optional | ✓ | ✓ | optional | ✓ | ✓ |
| New UI layer / layer registry entry | — | — | — | ✓ | ✓ | optional | ✓ | ✓ |
| New Story Node type / renderer | — | — | optional | optional | ✓ | ✓ | ✓ | ✓ |
| New security gate / redaction rule | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Data["Data (domain packs)"]
    A["Raw Sources<br/>data/&lt;domain&gt;/raw"] --> B["ETL + Normalization<br/>src/pipelines/"]
    B --> C["Certified Outputs<br/>data/&lt;domain&gt;/processed"]
    C --> S["STAC Items + Collections<br/>data/stac/"]
    S --> D["DCAT Dataset Views<br/>data/catalog/dcat/"]
    S --> P["PROV Lineage Bundles<br/>data/prov/"]
  end

  S --> G["Neo4j Graph<br/>src/graph/ (+ data/graph/ imports)"]
  G --> H["API Layer (contracts + redaction)<br/>src/server/ (or src/api/ legacy)"]
  H --> I["Map UI — React · MapLibre · Cesium<br/>web/"]
  I --> J["Story Nodes<br/>docs/reports/story_nodes/"]
  J --> K["Focus Mode<br/>provenance-linked context only"]
~~~

~~~mermaid
flowchart TD
  Q["User Question / Exploration"] --> API["API: Focus/Context Resolver"]
  API --> CTX["Context Bundle<br/>(evidence ids + excerpts + uncertainty)"]
  CTX --> UI["UI: Focus Mode View"]
  UI --> ST["Story Node(s)"]
  ST --> EVID["Evidence Artifacts<br/>(STAC/DCAT/PROV ids)"]
  EVID --> API
~~~

---

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/`  
  *(with `data/catalog/dcat/` + `data/prov/` as required evidence/lineage outputs)*

### Domain expansion pattern

- New domains go under `data/<domain>/`.
- New domain docs go under `docs/<domain>/` **or** `docs/data/<domain>/` *(choose one canonical location and link it from the docs index)*.

### Dataset families (examples, not exhaustive)

- **Hydrology:** streamflow, watersheds, hydrologic units
- **Climate:** normals, drought indices, extremes
- **Hazards:** floods, fires, severe storms
- **Land cover & terrain:** classification, DEMs, LiDAR derivatives
- **Agriculture & demography:** census, crop records, land use
- **Treaties & land:** treaty boundaries, patents/deeds, plats
- **Archaeology & history:** surveys, diaries, newspapers, archives
- **Ecology & biodiversity:** species observations, pests, habitats

### Versioning expectations

- New versions must link predecessor/successor (catalog level).
- Graph must mirror version lineage (entity/version edges or equivalent).

### Release bundle contents (typical)

- `manifest.zip` — asset listing + checksums
- `sbom.spdx.json` — dependency SBOM (if packaging code artifacts)
- STAC root catalog snapshot (if releasing a catalog cut)
- PROV bundle(s) for released transforms
- Model fingerprints + evaluation (if releasing AI artifacts)

> v10-era release references (kept for continuity; paths not confirmed in repo):  
> `../releases/v10.3.0/sbom.spdx.json`  
> `../releases/v10.3.0/manifest.zip`  
> `../releases/v10.3.0/focus-telemetry.json`  
> `../schemas/telemetry/master-guide-v1.json`

---

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy (how to document)

Every new dataset must have:

- **STAC** Collection + Item(s)
- **DCAT** mapping (minimum: title/description/license/keywords)
- **PROV** activity for the transform that generated it

These are **evidence artifacts**: they enable traceability, reuse, and governed storytelling.

### STAC (required core fields + KFM extensions)

Minimum expectations for each STAC Item:

- `geometry`, `bbox`
- `datetime` or an interval (when applicable)
- `assets` (COG/GeoJSON/Parquet/NetCDF/docs, etc.)
- `links` (collection, derived-from, related)

KFM-specific guidance:

- Use provenance-focused properties such as:
  - `kfm:lineage` (source ids, pipeline ids, run ids)
  - `kfm:ethics` (CARE label, sensitivity, sovereignty notes)
  - `kfm:method` / `kfm:processing` (transform summaries, parameters)

### DCAT (discovery + governance metadata)

Each dataset should expose:

- `dct:title`, `dct:description`
- `dct:license`, `dct:creator` (or steward/maintainer)
- `dct:temporal`, `dct:spatial`
- `dcat:distribution` linking to STAC assets (or published URLs)

### PROV (lineage and reproducibility)

For each transform:

- A PROV Activity describing the run/transform
- Inputs (`prov:used`) and outputs (`prov:wasGeneratedBy`)
- Agent/tool references (versioned) where possible
- Redaction/generalization steps recorded when applied

---

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation outputs | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges + provenance links |
| APIs | OpenAPI/GraphQL schema + contract tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story Nodes | template + evidence citations | no orphan facts |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |
| Governance | review checklists + redaction rules | sovereignty/ethics cannot be bypassed |

### ETL pipelines (src/pipelines/)

Each ETL pipeline should:

- Land inputs in `data/<domain>/raw/` (or record pointers + hashes)
- Produce intermediates in `data/<domain>/work/`
- Publish certified outputs in `data/<domain>/processed/`
- Emit **catalog + provenance artifacts** (STAC/DCAT/PROV)
- Block promotion if validation fails (gated pipeline)

Typical lifecycle:

1. **Fetch** — pull from external sources / archives
2. **Normalize** — clean, reshape, CRS/unit conversions
3. **Geoprocess** — reproject, clip, derive
4. **Temporal alignment** — explicit intervals/instants
5. **Validation** — schema + range + spatial/temporal checks + governance scans
6. **Publish** — processed outputs + catalogs + prov
7. **Graph hydration** — load key entities/relations from certified outputs

### Neo4j knowledge graph (src/graph/)

- Graph is hydrated from **certified artifacts** + metadata lineages.
- Ontology and constraints must be versioned and reviewed.
- Semantics should align to:
  - place/event/time concepts (CIDOC-style patterns)
  - spatial relationships (GeoSPARQL-style patterns)
  - temporal intervals/instants (OWL-Time-style patterns)

> **Boundary reminder:** UI never talks to Neo4j directly — graph access is via API contracts.

### API layer (src/server/ preferred; src/api/ legacy)

The API boundary must provide:

- Contract artifacts (OpenAPI / GraphQL SDL) and tests
- Redaction/generalization enforcement for sensitive outputs
- Query services that aggregate:
  - graph results
  - catalog metadata (STAC/DCAT/PROV)
  - time series / summaries

Representative endpoint families (illustrative only):

- STAC browse/search
- Graph query endpoints (contracted; no raw Cypher exposure without policy)
- Timeseries endpoints (climate/hydrology indices)
- Layer registry + layer metadata
- Focus Mode context bundle generator (provenance-linked)

### Web client (web/)

Primary UX capabilities (v10 baseline):

- timeline + temporal filters
- 2D/3D map views (MapLibre/Cesium)
- layer browser + feature inspector
- Focus Mode view rendering Story Nodes
- WCAG-oriented accessibility patterns and auditability

### Observability (recommended)

- Telemetry and signals should be captured for:
  - pipeline runs (dataset_id, run_id, validator status)
  - catalog publication events
  - redaction/generalization events
  - Focus Mode context bundle composition (evidence ids only; no sensitive leakage)

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Story Nodes are governed Markdown documents that:

- Follow the Story Node template
- Include **citations to evidence artifacts** (STAC/DCAT/PROV ids, dataset ids, document ids)
- Link to graph entities where applicable
- Are versioned and reviewable like code

### Focus Mode rule (strict)

- Focus Mode only consumes **provenance-linked content**.
- Any AI-generated elements must be **clearly indicated**.
- Any predictive content must be **opt-in** and carry uncertainty/confidence metadata.

### Integration expectations

When integrating a new domain:

- Ensure at least one Story Node exists to prove end-to-end integrity:
  - data → catalogs → graph → API → UI → story/focus view
- Use Story Nodes to surface gaps:
  - missing provenance
  - missing metadata
  - missing governance labels
  - missing API support for UI needs

---

## 🧪 Validation & CI/CD

### Self-validation (pipeline gates)

At minimum, promote outputs only if:

- schema checks pass (tabular + geospatial)
- spatial validity checks pass (geometry validity, bounds)
- temporal validity checks pass (interval/instant correctness)
- FAIR+CARE metadata checks pass
- sovereignty and privacy scans pass (PII/sensitive locations where applicable)
- checksums/manifests are generated

### Minimum CI gates (v12-ready baseline; apply to v10 where possible)

- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

> Commands are intentionally omitted here (not confirmed in repo).  
> Add repo-accurate commands under `tools/` and reference them from CI workflows.

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Governance review is required when introducing:

- new sensitive layers
- new AI narrative behaviors
- new external data sources
- new public-facing endpoints

### Sovereignty safety

- Document redaction/generalization rules for any restricted locations.
- Ensure no output is “less restricted” than any input in its lineage.
- Prefer coarse/aggregate products for public releases when needed.

### AI usage constraints (summary)

- Allowed transforms: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations, or fabricating sources.
- Human review is required for governance-affecting classifications.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---:|---|---|
| v10.3.2 | 2025-12-27 | KFM Core Team | Refined to align with governed template structure and v12 invariants; clarified pipeline ordering; corrected canonical paths and boundary rules. |
| v10.3.1 | 2025-11-13 | KFM Core Team | Master guide aligned to v10.3; diagrams fixed; telemetry & governance references updated. |
| v10.2.2 | 2025-11-13 | KFM Core Team | Expanded architecture coverage; added Focus Mode and telemetry sections. |

---

## Footer refs (do not remove)

- Canonical successor: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

---
