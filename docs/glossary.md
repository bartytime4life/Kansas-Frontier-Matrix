**📖 KFM Glossary**  
_Last updated: 2026-01-19 (v1.3.0) – expanded AI, simulation, modeling, real-time, and governance terminology._

```yaml
title: "📖 KFM Glossary"
path: "docs/glossary.md"
version: "v1.3.0"
last_updated: "2026-01-19"
status: "draft"
doc_kind: "Glossary"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

owner: "Docs"
review_cycle: "Quarterly · Docs + Governance owners"
scope: "docs/** (terminology used across data → catalogs → graph → API → UI → Story Nodes → Focus Mode)"
risk_category: "low"

doc_uuid: "urn:kfm:doc:glossary:v1.3.0"
semantic_document_id: "kfm-glossary-v1.3.0"
event_source_id: "ledger:kfm:doc:glossary:v1.3.0"
commit_sha: "<latest-commit-hash>"

ai_training_inclusion: true
ai_focusmode_usage: "Allowed (definitions-only; no policy generation)"
ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

sbom_ref: "N/A (doc-only)"
manifest_ref: "N/A (doc-only)"
telemetry_ref: "N/A (doc-only)"
telemetry_schema: "N/A (doc-only)"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
```

<a id="top"></a>

# 📚 KFM Glossary

## 📘 Overview

### Purpose
- Provide **canonical definitions** for common terms and acronyms used across KFM docs, pipelines, catalogs, graph, APIs, UI, Story Nodes, and Focus Mode.
- Standardize the meaning of common **front-matter keys** (including optional “registry blocks” such as `heading_registry`, `layout_profiles`, and `transform_registry`) to reduce ambiguity in governance and CI reviews.
- Track **known terminology drift / aliases** (paths, protocol labels, older spellings) so reviewers can spot inconsistencies without treating drift notes as policy.

### Scope
| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Definitions for KFM concepts, standards, and common geospatial/graph terms used in KFM artifacts | Full external standards documentation (STAC/DCAT/PROV specs themselves) |
| Project-specific terms (Focus Mode, Story Nodes, Extension Matrix, WDE, etc.) | New governance policy creation (link to governance docs instead) |
| Common metadata keys used in KFM front-matter (e.g., `doc_uuid`, `review_cycle`, `ai_training_inclusion`) | Replacing governed templates (use the templates in `docs/templates/`) |
| Non-policy descriptions of CI/validation “signals” and doc profiles | Declaring a validation gate as mandatory unless CI/governance already enforces it |

### Audience
- Primary: contributors writing docs or implementing pipeline/graph/API/UI/story changes
- Secondary: reviewers validating provenance, sensitivity, and contract compliance

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- You are here: this document
- Terms used in this doc (non-exhaustive): ETL, STAC, DCAT, PROV-O, Neo4j, API, Story Node, Focus Mode, governance, sensitivity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline) | `docs/MASTER_GUIDE_v13.md` | Docs | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, contract-first, evidence-first |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + gap closure plan |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end vision |
| Contracts (OpenAPI/GraphQL + schemas) | `api/contracts/` | API | Contracts are boundary truth |
| API implementation | `api/src/` | API | FastAPI/GraphQL services + adapters |
| Scripts (pipelines/ops) | `api/scripts/` | API | Reproducible runs + tooling |
| Data catalogs (STAC/DCAT/PROV) | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | Data | Discoverability + interoperability + lineage |

### Definition of done (for this document)
- [x] Front-matter complete and `path` matches file location
- [ ] All front-matter keys used in governed templates are defined here (or explicitly marked TBD)
- [ ] New terms introduced across ETL/catalog/graph/API/UI/story are added here
- [ ] Known naming/alias drift is documented as **drift** (not as policy)
- [ ] Link check to referenced docs passes (as implemented in CI)
- [ ] No new governance policy is authored in this glossary

## 🧾 Front-Matter Key Index (Quick Reference)

> This is a **navigation aid**, not a template replacement. Templates remain the governed source.

### Core identity & lifecycle
- `title` · `path` · `version` · `last_updated` · `status` · `doc_kind` · `license`
- `owner` · `review_cycle` · `scope` · `risk_category`
- `doc_uuid` · `semantic_document_id` · `event_source_id` · `commit_sha`

### Protocols & profiles
- `markdown_protocol_version` · `mcp_version` · `ontology_protocol_version`
- `pipeline_contract_version` · `stac_profile` · `dcat_profile` · `prov_profile`

### Governance & ethics pointers
- `governance_ref` · `ethics_ref` · `sovereignty_policy`
- `fair_category` · `care_label` · `sensitivity` · `classification` · `jurisdiction`

### AI controls
- `ai_training_inclusion` · `ai_focusmode_usage`
- `ai_transform_permissions` · `ai_transform_prohibited`

### Release & observability pointers
- `sbom_ref` · `manifest_ref`
- `telemetry_ref` · `telemetry_schema`
- `doc_integrity_checksum`

### Optional registries (presentation/structure)
- `heading_registry` · `layout_profiles` · `badge_profiles`
- `diagram_profiles` · `fencing_profile`
- `transform_registry` · `branding_registry`

## 🗂️ Directory Layout

### This document
- `path`: `docs/glossary.md` *(must match front-matter)*

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Governed documentation, templates, design notes |
| Docs (templates) | `docs/templates/` | Governed doc templates (universal/story/API) |
| Docs (governance) | `docs/governance/` | Governance/ethics/sovereignty root docs |
| Docs (architecture) | `docs/architecture/` | Architecture notes, redesign blueprints |
| Docs (story) | `docs/reports/story_nodes/` | Curated Story Nodes (draft/published if used) |
| API (service) | `api/` | Backend code + scripts + contracts |
| API (contracts) | `api/contracts/` | OpenAPI/GraphQL + schema contracts |
| API (source) | `api/src/` | Adapters, services, mappers, domain logic |
| API (scripts) | `api/scripts/` | Catalog builds, simulation, CI helpers, ops tooling |
| Web UI | `web/` | React/MapLibre UI *(must not read Neo4j directly)* |
| Data staging | `data/raw/<domain>/` · `data/work/<domain>/` · `data/processed/<domain>/` | Source snapshots, work products, processed datasets |
| STAC catalogs | `data/stac/` | STAC Collections/Items + assets discovery metadata |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views (catalog interoperability) |
| PROV lineage | `data/prov/` | PROV bundles (lineage/traceability) |
| Schemas | `schemas/` | JSON/SHACL/contract schemas (stac/dcat/prov/story/ui/telemetry) |
| MCP runs | `mcp/` | Run logs, experiments, reproducibility artifacts |
| Tools | `tools/` | Validators, utilities, QA scripts |
| Tests | `tests/` | Unit/integration/contract tests |
| Web | `web/` | Frontend UI code (React, Cesium, etc.) |

```plaintext
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 api/
├── 📁 contracts/
├── 📁 src/
└── 📁 scripts/

📁 data/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 glossary.md
├── 📄 MASTER_GUIDE_v13.md
├── 📁 templates/
├── 📁 architecture/
├── 📁 governance/
└── 📁 reports/
    └── 📁 story_nodes/

📁 mcp/
📁 schemas/
📁 tools/
📁 tests/
📁 web/
```

## 🧭 Context

### Background
KFM spans multiple technical layers (data → catalogs → graph → APIs → UI → narrative). A shared glossary keeps those layers interoperable and reduces “terminology drift” across contributions.

### Assumptions
- The glossary is a living document.
- Terms should be defined in a way that remains stable even as implementation details evolve.
- If two spellings/paths appear in project docs, prefer the *governed* one and add an explicit drift note.

### Constraints / invariants
- Use the canonical pipeline ordering language consistently:
  - **ETL → STAC/DCAT/PROV catalogs → Knowledge Graph → APIs → Web UI → Story Nodes → Focus Mode**
- Do not define new policy here; link to governance docs for rules.
- UI does **not** read Neo4j directly; the API layer is the contract boundary.
- Contracts/schemas are authoritative at boundaries. **Docs describe; contracts decide.**
- Data outputs are **not code**: derived datasets and catalog/provenance outputs live under `data/` (and optional `releases/`), not under `api/src/`.

### How to update this glossary
1. Add new terms when you introduce a new concept, acronym, schema field name, or subsystem name.
2. Prefer **project meanings** over textbook meanings if KFM uses a term in a specific way.
3. If a term is disputed or evolving, define it as a **working definition** and mark it `TBD` for governance review.
4. If a doc uses a front-matter key not defined here, add it under the appropriate letter.
5. If you discover naming drift (paths, protocol aliases), add a **Drift note** entry rather than “fixing by definition.”

## 🧩 Drift & Alias Register (tracked here so drift doesn’t become policy)

| Topic | What’s drifting | Why it matters | Current stance |
|---|---|---|---|
| Master Guide naming | `docs/MASTER_GUIDE_v12.md` vs `docs/MASTER_GUIDE_v13.md` | Links + contributor expectations | Prefer v13 when present; keep v12 as legacy alias |
| API root path | `src/server/` vs `api/src/` | Broken links + wrong mental model | Prefer `api/src/` for backend code; record alternates as drift |
| Governance doc paths | `docs/governance/*` vs `docs/standards/governance/*` | Linkcheck + duplicated “roots” | Prefer `docs/governance/*`; treat others as drift |
| Governance filename style | `ROOT_GOVERNANCE.md` vs `ROOT-GOVERNANCE.md` | Broken links and duplicated “roots” | Treat as drift; standardize under governance owners (TBD) |
| Protocol label aliases | `KFM-ONTO` vs `KFM-OP`; `KFM-PPC` vs `KFM-PDC` | Tooling and schema checks rely on consistent keys | Treat older labels as legacy aliases (TBD canonical mapping) |
| Domain naming | `air-quality` vs `air_quality` | Dataset IDs + UI layer IDs | Prefer kebab-case in docs paths; treat data dirs as domain-defined (TBD) |
| Story Node placement | `docs/reports/story_nodes/` vs other story folders | Ingestion + UI linking | Prefer `docs/reports/story_nodes/` |
| AI assistant naming | **“CrewAI”** vs *Focus Mode AI assistant* | Internal code name vs user-facing terminology | Accept “CrewAI” as internal alias for AI content workers; use “AI-assisted” in docs for clarity (TBD) |
| Story schema fields | *No drift noted yet* | (If v2 vs v3 naming differences arise) | Document field aliases if discovered (TBD) |

## 📚 Glossary (A–Z)

> Formatting conventions:  
> - **TERM (Acronym)** — definition. *(Notes / related terms)*  
> - **`front_matter_key`** — a YAML key used in governed documents. *(Notes / related keys)*

### 0–9 / Symbols
- **Diamond⁹ Ω / Crown∞Ω** — internal “badge string” used in some KFM indexes/READMEs to signal “highly governed / certified”; **must not** be treated as policy unless a rubric is linked. *(See: Validation gate, Release stage.)*
- **F1-A1-I1-R1** — shorthand label for a FAIR alignment tier; treat as a **label**, not a computed score, unless a rubric is linked. *(See: FAIR, `fair_category`.)*

### A
- **A11y (Accessibility)** — practices that ensure UI and docs are usable by people with disabilities (keyboard navigation, contrast, ARIA labels, etc.).
- **ADR (Architecture Decision Record)** — a short, versioned decision log capturing *what* was decided and *why* (tradeoffs + consequences). *(See: Governance, Change control.)*
- **AI Focus Mode (`ai_focusmode_usage`)** — front-matter control describing whether the artifact may be surfaced in Focus Mode.
- **AI training inclusion (`ai_training_inclusion`)** — front-matter boolean indicating whether the artifact may be included in AI training corpora.
- **AI transform permissions (`ai_transform_permissions`)** — allowed AI operations on a document (e.g., `summarize`, `structure_extract`). Not a license to invent facts. *(See: Provenance.)*
- **AI transform prohibited (`ai_transform_prohibited`)** — AI operations explicitly disallowed (e.g., `infer_sensitive_locations`, `generate_policy`). *(See: Prompt Gate.)*
- **AI-assisted drafting** — using AI to assist in content creation (e.g. Focus Mode’s CrewAI for Story Nodes). All AI-generated narrative must remain evidence-led and governed (no unsourced speculation). *(Related: Focus Mode, Story Node.)*
- **API (Application Programming Interface)** — the contract boundary between clients (UI/tools) and KFM backend services. UI consumes KFM data via APIs or pre-built artifacts, not direct graph access.
- **Asset (STAC Asset)** — a file/resource referenced from a STAC Item (e.g., COG, GeoJSON, PDF, thumbnail). *(See: STAC Item.)*
- **Attestation (`attestation_ref`)** — a signed statement about how an artifact was built (often SLSA/in-toto) used to verify supply-chain integrity. *(See: SLSA, in-toto.)*

### B
- **BBox (Bounding box)** — rectangular spatial extent, typically `[west, south, east, north]`, used for spatial indexing and discovery.
- **Badge profiles (`badge_profiles`)** — front-matter list describing approved badge layouts for a doc. Presentation-only; no governance meaning.
- **Bias correction** — adjusting a model’s data output to remove systematic bias by aligning it with trusted observations (often over a calibration interval). *(Methods: Quantile Mapping, Delta Method.)*
- **Branch protection** — repository controls that require CI checks (and often reviews) before merging.

### C
- **CARE label (`care_label`)** — descriptive label for CARE applicability and review expectations. Must align with sovereignty/governance docs. *(See: CARE Principles.)*
- **CARE Principles** — framework emphasizing Collective Benefit, Authority to Control, Responsibility, and Ethics in Indigenous data governance.
- **Catalog (KFM)** — machine-readable inventory of data products and metadata, primarily via STAC/DCAT/PROV.
- **Cesium** — 3D geospatial rendering library referenced for 3D visualization in the UI. *(Often paired with MapLibre.)*
- **Checksum record** — stored hash values used to validate that acquired files and published artifacts have not changed unexpectedly.
- **CI/CD** — automation that validates, tests, and (optionally) deploys changes (schemas, docs, code).
- **Classification (`classification`)** — coarse access label for artifacts (e.g., `open`). *(Do not confuse with `sensitivity`.)*
- **COG (Cloud Optimized GeoTIFF)** — GeoTIFF formatted for HTTP range requests and efficient tiled access.
- **Community verification** — crowdsourced or microtask-driven validation of data and narratives by community members (e.g. upvote/downvote or “verified” flags on crowdsourced data). *(See: Governance, QA gate.)*
- **Contract artifact** — machine-validated specification that defines boundary expectations (API payloads, Story Node schema, catalog profiles). Contracts are authoritative.
- **Contract-first** — discipline where schemas/contracts are defined (and tested) before broad implementation; breaking changes require versioning and compatibility tests.
- **Contract test** — automated test that ensures payloads and schema expectations remain stable across changes.

### D
- **Dataset** — a versioned, describable collection of data assets (files) plus metadata (license, extents, lineage). In KFM, “dataset” should be publishable via STAC/DCAT and traceable via PROV.
- **Dataset registry** — human/machine indexes of available datasets used for discoverability and CI link checks.
- **DCAT** — W3C vocabulary for describing datasets in catalogs; used in KFM for interoperable dataset discovery.
- **`dcat_profile`** — front-matter profile/version label for DCAT rules expected for artifacts in this scope.
- **Deterministic ETL** — idempotent, config-driven transforms with logged inputs/outputs and stable IDs.
- **Deterministic simulation run (`kfm-sim-run`)** — a governed simulation execution pattern for **scenario replay** with fixed seeds, frozen time, and containerized tools. Produces diff artifacts + updated STAC + PROV lineage; may open a draft PR for review. *(See: Reproducibility, Provenance.)*
- **Doc integrity checksum (`doc_integrity_checksum`)** — cryptographic hash (e.g., sha256) of the document content used to detect tampering and support reproducibility.
- **Drift detection** — automated checks that schemas/data distributions/upstreams have changed unexpectedly.

### E
- **ETL** — Extract, Transform, Load: ingest raw sources, normalize formats, and produce processed outputs plus lineage logs.
- **Evidence-first** — discipline where every UI claim, API value, or narrative assertion traces to a source artifact ID and provenance chain.
- **Explainable AI (XAI)** — techniques and practices that make an AI’s reasoning transparent and understandable to humans. *(See: Focus Mode audit panel.)*
- **Extension Matrix** — planning pattern: adding a domain/capability implies changes across data, catalogs, graph, APIs, UI, narrative, and governance gates.

### F
- **FAIR Principles** — Findable, Accessible, Interoperable, Reusable.
- **`fair_category`** — front-matter label describing FAIR alignment. Treat as descriptive unless a rubric is linked.
- **Fail-closed** — posture where validation failures block merges/deployments rather than being skipped.
- **Fencing profile (`fencing_profile`)** — convention stating how code fences should be written (e.g., prefer `~~~` inside docs to avoid nesting conflicts).
- **Focus Mode** — an experience that consumes only provenance-linked context bundles (**no unsourced narrative**). AI insights are opt-in and must show uncertainty. *(See: Story Node, Provenance.)*

### G
- **GDAL / OGR** — geospatial processing libraries used for format conversion, reprojection, raster/vector operations.
- **GeoJSON** — JSON format for representing vector geometries + properties.
- **Graph (Knowledge graph)** — semantic core linking entities (Place/Event/Dataset/etc.) and relationships, including provenance links.
- **Graph-Augmented Intelligence (GAI)** — fusing the Neo4j knowledge graph with AI retrieval so Focus Mode answers are grounded in graph + catalogs. *(See: RAG, Focus Mode.)*
- **GraphQL** — typed API style that can expose access to KFM graph-backed data through resolvers.
- **Governance** — rules, review gates, and policies controlling ingest, publication, redaction/generalization, and narrative surfacing.
- **GTFS-RT (General Transit Feed Spec – Real-Time)** — standard for live transit data (vehicle positions, alerts). KFM watcher ingests GTFS-RT and emits STAC Items + DCAT entries for live feeds. *(See: Real-time data.)*

### H
- **Hallucination (KFM context)** — presenting narrative or claims without provenance-linked sources. Focus Mode forbids hallucinated/unsourced content.
- **Heading registry (`heading_registry`)** — optional front-matter block listing allowed/expected section headings. Consistency aid; not policy.
- **Hermetic build** — build/run executed in a controlled environment with pinned dependencies and inputs, supporting reproducibility and supply-chain verification.

### I
- **in-toto** — supply-chain framework for describing and verifying steps in a build; attestations may be produced/verified using in-toto metadata.
- **ISO 8601** — date/time string format standard referenced for consistent time encoding.

### J
- **JSON Schema** — schema used to validate JSON documents (inputs, outputs, configs, contracts).
- **JSON-LD** — JSON for Linked Data; used to serialize graph semantics and align with vocabularies like DCAT and PROV.
- **`jurisdiction`** — front-matter label stating legal/policy jurisdiction context for this artifact (e.g., `US-KS`).

### K
- **KFM** — Kansas Frontier Matrix: geospatial-historical knowledge system with a governed end-to-end pipeline producing maps and provenance-led narratives.
- **KFM-MDP** — KFM Markdown protocol profile/version that governs doc structure and front-matter conventions.
- **KFM-STAC / KFM-DCAT / KFM-PROV** — KFM validation profiles for catalog + provenance artifacts.
- **Kalman Filter / EnKF** — sequential estimation filters; EnKF uses ensembles to capture uncertainty. Used for smoothing sensor time series and model assimilation. *(See: PurpleAir.)*

### L
- **Layer (map layer)** — a visualizable dataset or derived rendering exposed to the UI; must have source metadata and access rules.
- **Layer registry** — UI-side registry listing available layers, sources, and access rules; prevents unauthorized or sensitive exposure.
- **License (`license`)** — front-matter license identifier (e.g., `CC-BY-4.0`).
- **Lineage** — traceability describing how an artifact was produced from inputs and processes. *(See: PROV-O.)*

### M
- **Manifest (`manifest_ref`)** — versioned artifact describing what was produced (files, hashes, versions, provenance pointers).
- **MapLibre** — open-source web mapping library referenced for 2D map rendering in KFM.
- **MCP** — KFM reproducibility/workflow discipline used across runs and artifacts (stored under `mcp/`).

### N
- **Neo4j** — graph database used for KFM’s semantic core and relationship queries.

### O
- **OGC API** — modern OGC web API family. *(If adopted, treat as an interoperability surface.)*
- **OpenAPI** — specification for describing REST APIs; used to document and validate REST contracts.

### P
- **Pipeline contract (`pipeline_contract_version`)** — front-matter key naming the active pipeline contract profile/version for this artifact.
- **PMTiles** — single-file archive for efficient tile delivery; often paired with MapLibre for fast client rendering.
- **PROV-O** — W3C Provenance Ontology.
- **PROV bundle** — provenance package capturing entities, activities, agents for a run or dataset.
- **`prov_profile`** — front-matter profile/version label for PROV artifacts expected for this scope.
- **Promotion (data artifact)** — governed elevation from work/sandbox outputs into processed/published artifacts; requires STAC/DCAT/PROV, validation, and review.
- **Prompt Gate** — Focus Mode prompt security mechanism: filters/sanitizes inputs, blocks prompt injection, enforces tool allowlists/OPA checks where configured.
- **Provenance** — trace of origin, inputs, process, and responsible parties; required for Focus Mode and Story Nodes.
- **Provenance guard** — CI/validation gate rejecting artifacts missing required provenance/metadata.
- **PurpleAir** — low-cost PM sensor network; KFM ingests and calibrates against reference stations; produces cataloged, provenance-linked corrected outputs. *(See: Bias correction, QM, EnKF.)*

### Q
- **QA gate / Quality gate** — validation checkpoint that must pass before promotion/publish.
- **Quantile Mapping (QM)** — bias correction technique mapping quantiles of modeled/sensor data to reference distributions.

### R
- **Redaction** — removing or hiding sensitive information entirely. *(Related: Generalization.)*
- **Release stage (`release_stage`)** — maturity label distinct from doc `status`.
- **Reproducibility** — ability to regenerate outputs from inputs with pinned versions/configs and recorded provenance.

### S
- **SBOM (`sbom_ref`)** — Software Bill of Materials reference (often SPDX) for a release.
- **Schema validation** — checks that artifacts conform to required schemas/profiles.
- **Semantic document ID (`semantic_document_id`)** — stable, human-readable identifier distinct from `doc_uuid`.
- **Sensitivity (`sensitivity`)** — label indicating potential harm if details are disclosed; may require generalization/redaction.
- **SHACL (`shape_schema_ref`)** — Shapes Constraint Language for RDF constraint validation.
- **Signature gate** — requirement that artifacts are signed/attested (Sigstore/Cosign/SLSA) before promotion or release.
- **Sigstore** — ecosystem for signing and transparency logging.
- **SLSA** — supply-chain integrity framework.
- **Sovereignty (data sovereignty)** — community control expectations for sensitive cultural/Indigenous data; requires additional review and constraints.
- **Story Node** — governed narrative artifact: machine-ingestible, provenance-linked, every factual claim cited; used by Focus Mode and UI storytelling.
- **STAC** — SpatioTemporal Asset Catalog.
- **STAC Collection** — groups STAC Items and defines shared metadata/extents.
- **STAC Item** — spatiotemporal unit describing assets and metadata.
- **`stac_profile`** — front-matter profile/version label for STAC rules expected for artifacts in this scope.

### T
- **Telemetry (`telemetry_ref`, `telemetry_schema`)** — observability metrics/logs/traces; supports governance auditing.
- **Transform registry (`transform_registry`)** — optional front-matter block enumerating allowed vs prohibited AI transforms.
- **`title`** — human-readable doc title.

### U
- **Uncertainty** — confidence indicators for model outputs or inferred claims; AI insights must be labeled and opt-in.

### V
- **Validation gate** — mandatory CI/CD check that must pass before changes accepted.
- **V&V (Verification & Validation)** — modeling discipline: correctness vs reality fit.
- **Version-pinned** — immutability posture: published artifacts tied to version, not changed in place.

### W
- **WDE (World Discovery Engine)** — extension concept implying new data products + graph/API/UI changes and validation.
- **WebGL** — GPU-accelerated browser rendering API.
- **Workflow** — defined pipeline steps executed reproducibly and recorded in provenance.

### Y
- **YAML front-matter** — metadata block for governed docs (versioning, provenance refs, governance refs, AI permissions).

### Z
- **Zoom level** — map scale index controlling level-of-detail and rendering decisions.

## 🗺️ Diagrams
- Not required for this glossary.

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Canonical terminology sources | Markdown | `docs/` (Master Guide + templates) | Markdown protocol checks + linkcheck |
| Governance terminology | Markdown | `docs/governance/` | Linkcheck (no policy authored here) |
| Contracts terminology | YAML/JSON/GraphQL | `api/contracts/` · `schemas/` | Schema validation + contract tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| KFM Glossary | Markdown | `docs/glossary.md` | KFM-MDP (front-matter + section structure) |

### Sensitivity & redaction
- Definitions-only; avoid protected coordinates or operationally sensitive examples.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This glossary does not emit STAC payloads.

### DCAT
- This glossary does not emit DCAT payloads.

### PROV-O
- This glossary does not emit PROV bundles.

## 🧱 Architecture (Context Map)

| Layer | Component | Canonical home | Notes |
|---|---|---|---|
| ETL | Pipelines | `api/scripts/` + `data/work/` | Deterministic runs + reproducible outputs |
| Catalog | STAC/DCAT/PROV | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Discovery + interoperability + lineage |
| Graph | Knowledge Graph | `api/src/` + `schemas/` | Ontology bindings + loaders |
| API | Contract boundary | `api/src/` + `api/contracts/` | Redaction/generalization and API contracts |
| UI | Map + Focus Mode | `web/` | Must not read Neo4j directly |
| Story | Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narratives |
| Docs | Glossary (this doc) | `docs/glossary.md` | Shared vocabulary across layers |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes and Focus Mode UI should link to this glossary for shared terminology.

### Co-authoring and AI Assistance
- Multi-author editing and AI-assisted drafting are emerging features; definitions here keep vocabulary consistent.

## 📜 Version History
| Version | Date       | Description                                                                                      | By        |
|---------|------------|--------------------------------------------------------------------------------------------------|-----------|
| v1.3.0  | 2026-01-19 | Expanded glossary with AI system components (Focus Mode, XAI, Prompt Gate), simulation/modeling terms (kfm-sim-run, bias correction, EnKF), real-time ingest (GTFS-RT, PurpleAir), governance concepts (sovereignty, telemetry). | Bartytime |
| v1.2.2  | 2026-01-12 | Updated canonical paths to reflect `api/` structure; added Front-Matter Key Index; expanded core terms; aligned key artifacts to Master Guide v13. | Bartytime |

## 🔗 Footer

- ⬅️ Back to Master Guide: `docs/MASTER_GUIDE_v13.md`
- 🧭 Governance Root: `docs/governance/ROOT_GOVERNANCE.md`
- ⚖️ Ethics: `docs/governance/ETHICS.md`
- 🪶 Sovereignty: `docs/governance/SOVEREIGNTY.md`

<a id="bottom"></a>
