---
title: "KFM Glossary"
path: "docs/glossary.md"
version: "v1.2.1"
last_updated: "2025-12-29"
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
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:glossary:v1.2.1"
semantic_document_id: "kfm-glossary-v1.2.1"
event_source_id: "ledger:kfm:doc:glossary:v1.2.1"
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

# KFM Glossary

## 📘 Overview

### Purpose
- Provide **canonical definitions** for common terms and acronyms used across KFM docs, pipelines, catalogs, graph, APIs, UI, Story Nodes, and Focus Mode.
- Standardize the meaning of common **front‑matter keys** (including optional “registry blocks” such as `heading_registry`, `layout_profiles`, and `transform_registry`) to reduce ambiguity in governance and CI reviews.
- Track **known terminology drift / aliases** (paths, protocol labels, older spellings) so reviewers can spot inconsistencies without treating drift notes as policy.

### Scope
| In Scope | Out of Scope |
|---|---|
| Definitions for KFM concepts, standards, and common geospatial/graph terms used in KFM artifacts | Full external standards documentation (STAC/DCAT/PROV specs themselves) |
| Project-specific terms (Focus Mode, Story Nodes, Extension Matrix, WDE, etc.) | New governance policy creation (link to governance docs instead) |
| Common metadata keys used in KFM front‑matter (e.g., `doc_uuid`, `review_cycle`, `ai_training_inclusion`) | Replacing governed templates (use the templates in `docs/templates/`) |
| Non‑policy descriptions of CI/validation “signals” and doc profiles | Declaring a validation gate as mandatory unless CI/governance already enforces it |

### Audience
- Primary: contributors writing docs or implementing pipeline/graph/API/UI/story changes
- Secondary: reviewers validating provenance, sensitivity, and contract compliance

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- You are here: this document
- Terms used in this doc (non‑exhaustive): ETL, STAC, DCAT, PROV‑O, Neo4j, API, Story Node, Focus Mode, governance, sensitivity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline) | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Consolidates “one canonical home”, contract-first, evidence-first |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + gap closure plan |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end vision |
| Land Treaties module | `docs/data/historical/land-treaties/README.md` | Domain steward | Example domain module (governance-sensitive) |
| Air Quality module | `docs/data/air-quality/README.md` | Domain steward | Example domain module |
| Soils (SDA) module | `data/soils/sda/README.md` | Domain steward | Example domain module |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |
| Reference library (PDFs) | `docs/library/` | TBD | Shared vocabulary (modeling, spatial analysis, rendering, scalable data mgmt) *(path not confirmed in repo)* |

### Definition of done (for this document)
- [x] Front‑matter complete and `path` matches file location
- [ ] All front‑matter keys used in governed templates are defined here (or explicitly marked TBD)
- [ ] New terms introduced across ETL/catalog/graph/API/UI/story are added here
- [ ] Known naming/alias drift is documented as **drift** (not as policy)
- [ ] Link check to referenced docs passes (as implemented in CI)
- [ ] No new governance policy is authored in this glossary

## 🗂️ Directory Layout

### This document
- `path`: `docs/glossary.md` *(must match front-matter)*

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Governed documentation, templates, design notes |
| Docs (templates) | `docs/templates/` | Governed doc templates (universal/story/API) |
| Docs (governance) | `docs/governance/` | Governance/ethics/sovereignty root docs *(path drift exists — see glossary)* |
| Docs (standards) | `docs/standards/` | Protocol and standards docs *(may be absent in some repo branches — not confirmed in repo)* |
| Docs (architecture) | `docs/architecture/` | Architecture notes, redesign blueprints |
| Docs (domain runbooks) | `docs/data/<domain>/` | Domain notes, requirements, governance runbooks |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Data staging | `data/raw/<domain>/` · `data/work/<domain>/` · `data/processed/<domain>/` | Source snapshots, work products, processed datasets |
| STAC catalogs | `data/stac/` | STAC Collections/Items + assets discovery metadata |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views (catalog interoperability) |
| PROV lineage | `data/prov/` | PROV bundles (lineage/traceability) |
| Graph | `src/graph/` | Ontology, migrations, constraints, loaders |
| Pipelines | `src/pipelines/` | ETL + catalog build pipelines |
| APIs | `src/server/` | REST/GraphQL services + contracts *(alternate `src/api/` may exist if legacy — not confirmed in repo)* |
| Frontend | `web/` | React/MapLibre UI *(must not read Neo4j directly)* |
| Schemas | `schemas/` | JSON/SHACL/contract schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Validators, utilities, QA scripts |
| MCP runs | `mcp/` | Run logs, experiments, reproducibility artifacts |
| Releases | `releases/` | Versioned manifests, SBOMs, signatures, attestations *(if used — not confirmed in repo)* |
| CI workflows | `.github/workflows/` | Build/test/lint/policy workflows |

### Repo top-levels (expected)
~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 glossary.md
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
├── 📁 governance/
├── 📁 standards/                           # if used in this repo branch
├── 📁 reports/
│   └── 📁 story_nodes/
└── 📁 data/
    └── 📁 <domain>/

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/
📁 tests/
📁 tools/
📁 web/
📁 releases/                                 # if used
~~~

## 🧭 Context

### Background
KFM spans multiple technical layers (data → catalogs → graph → APIs → UI → narrative). A shared glossary keeps those layers interoperable and reduces “terminology drift” across contributions.

### Assumptions
- The glossary is a living document.
- Terms should be defined in a way that remains stable even as implementation details evolve.
- If two spellings/paths appear in project docs, prefer the *governed* one and add an explicit drift note.

### Constraints / invariants
- Use the canonical pipeline ordering language consistently:
  - **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- Do not define new policy here; link to governance docs for rules.
- UI does **not** read Neo4j directly; the API layer is the contract boundary.
- Contracts/schemas are authoritative at boundaries (API contracts, STAC/DCAT/PROV profiles, Story Node schemas). **Docs describe; contracts decide.**
- Data outputs are **not code**: derived datasets and catalog/provenance outputs live under `data/` and `releases/`, not `src/`.

### How to update this glossary
1. Add new terms when you introduce a new concept, acronym, schema field name, or subsystem name.
2. Prefer **project meanings** over textbook meanings if KFM uses a term in a specific way.
3. If a term is disputed or evolving, define it as a **working definition** and mark it `TBD` for governance review.
4. If a doc uses a front‑matter key not defined here, add it under the appropriate letter.
5. If you discover naming drift (paths, protocol aliases), add a **Drift note** entry rather than “fixing by definition.”

### Open questions / drift register (tracked here so drift doesn’t become policy)
| Topic | What’s drifting | Why it matters | Current stance |
|---|---|---|---|
| Governance doc paths | `docs/governance/*` vs `docs/standards/governance/*` | Links, CI linkcheck, reviewer expectations | Prefer `docs/governance/*`, record alternates as drift |
| Governance filename style | `ROOT_GOVERNANCE.md` vs `ROOT-GOVERNANCE.md` | Broken links and duplicated “roots” | Treat as drift; standardize under governance owners (TBD) |
| Protocol label aliases | `KFM-ONTO` vs `KFM-OP`; `KFM-PPC` vs `KFM-PDC` | Tooling and schema checks rely on consistent keys | Treat older labels as legacy aliases (TBD canonical mapping) |
| Domain directory naming | `air-quality` vs `air_quality` (and other hyphen/underscore drift) | Paths, dataset IDs, UI layer IDs | Prefer kebab-case in docs paths; treat data dirs as domain-defined (TBD) |
| Telemetry docs placement | `docs/telemetry/` vs `docs/reports/telemetry/` | Discoverability + CI checks | Prefer `docs/telemetry/` per templates; keep legacy paths noted |
| Story Node placement | `docs/reports/story_nodes/` vs other story-node folders | Ingestion + UI linking | Prefer `docs/reports/story_nodes/` per repo conventions |

### Future extensions
- Add a lightweight “glossary-lint” check that verifies:
  - Common front‑matter keys used in governed templates are defined here.
  - Known alias mappings are listed (without creating policy).
- Add a short “front‑matter key index” appendix auto-generated from schemas *(not confirmed in repo)*.
- Add cross-links from Story Node template fields to glossary definitions.

## 📚 Glossary (A–Z)

> Formatting conventions used below:
> - **TERM (Acronym)** — definition. *(Notes / related terms)*
> - **`front_matter_key`** — a YAML key used in governed documents. *(Notes / related keys)*

### 0–9 / Symbols
- **Diamond⁹ Ω / Crown∞Ω** — an *internal certification/badge string* used in some KFM indexes/READMEs to signal “highly governed / certified” status; the exact scoring/criteria is **not confirmed in repo** and must not be treated as a policy rule. *(See: Governance, Validation gate, Release stage.)*
- **2D/3D map rendering** — 2D rendering typically uses MapLibre; 3D rendering may use Cesium/WebGL techniques depending on the UI subsystem. *(See: MapLibre, Cesium, WebGL.)*
- **F1-A1-I1-R1** — a shorthand “FAIR category” string used in some governed docs to indicate a baseline level of FAIR alignment. Treat the string as a *label*, not a computed score, unless a scoring rubric is linked. *(See: `fair_category`, FAIR Principles.)*

### A
- **A11y (Accessibility)** — practices that ensure UI and docs are usable by people with disabilities (keyboard navigation, contrast, ARIA labels, etc.).
- **`accessibility_compliance`** — front‑matter label stating the accessibility target met or aimed for (e.g., “WCAG 2.1 AA”). Declarative target/claim that should align to CI checks when present. *(See: WCAG, `test_profiles`.)*
- **AirNow** — referenced air-quality source system used in Air Quality domain docs; treated as an upstream data provider in KFM ingestion plans. *(See: OpenAQ, CAMS NRT.)*
- **AI focusmode usage (`ai_focusmode_usage`)** — front‑matter control describing whether an artifact’s content may be surfaced in Focus Mode (e.g., “Allowed with restrictions”, “Restricted”). *(See: Focus Mode, AI transform permissions.)*
- **AI training inclusion (`ai_training_inclusion`)** — front‑matter boolean indicating whether an artifact may be included in AI training corpora. When `false`, exclude from training and do not treat the artifact as a training example. *(See: AI transform permissions/prohibited.)*
- **AI transform permissions (`ai_transform_permissions`)** — allowed AI operations on a document (e.g., `summarize`, `structure_extract`). These permissions are not a license to invent facts; provenance and governance rules still apply. *(See: Hallucination, Provenance.)*
- **AI transform prohibited (`ai_transform_prohibited`)** — AI operations explicitly disallowed (e.g., `infer_sensitive_locations`, `generate_policy`). *(See: Prompt Gate.)*
- **API (Application Programming Interface)** — the contract boundary between clients (UI/tools) and KFM backend services. The UI should consume data via APIs or pre-built artifacts, not direct graph access.
- **API lifecycle registry** — a versioned record tracking API surfaces through lifecycle states (e.g., Proposed → Draft → Alpha → Beta → Stable → Deprecated → Retired). *(See: Deprecation.)*
- **AQP (Approximate Query Processing)** — techniques for returning fast, approximate results (often with uncertainty bounds) on large datasets; relevant to scalable KFM analytics and exploratory UI queries. *(Reference library term.)*
- **Asset (STAC Asset)** — a file/resource referenced from a STAC Item (e.g., COG, GeoJSON, PDF, thumbnail). *(See: STAC, STAC Item.)*
- **Attestation (`attestation_ref`)** — a signed statement about how an artifact was built (often SLSA/in‑toto formatted) used to verify provenance and supply‑chain integrity. *(See: SLSA, in‑toto, Signature, Rekor, Cosign.)*
- **Audit panel** — a Focus Mode UI panel intended to show governance flags, provenance pointers, and redaction/generalization status. *(See: Focus Mode, Governance, Redaction.)*

### B
- **BBox (Bounding box)** — a rectangular spatial extent, typically `[west, south, east, north]`, used for spatial indexing and discovery. *(Often used in STAC.)*
- **Bayesian inference** — statistical inference that updates beliefs from prior → posterior using Bayes’ theorem; used for uncertainty-aware modeling and decision support in analytical extensions. *(See: Uncertainty, MCMC.)*
- **Badge profiles (`badge_profiles`)** — a front‑matter list describing which standardized badge layouts a doc may use (e.g., a centered badge row). Presentation convention only; must not introduce new governance meaning. *(See: `layout_profiles`, `header_profile`.)*
- **BLB (Bag of Little Bootstraps)** — a scalable bootstrapping approach used for uncertainty estimation on large data. *(Reference library term; see: Uncertainty.)*
- **Branch protection** — repository controls that require CI checks (and often reviews) before merging; used to enforce validation gates. *(See: Required-status check, Fail-closed.)*
- **Branding registry (`branding_registry`)** — a front‑matter block enumerating approved “taglines” or brand statements for specific doc categories. Treat as controlled vocabulary for presentation. *(See: `badge_profiles`.)*

### C
- **CARE label (`care_label`)** — a front‑matter classification describing how CARE applies (examples include “Public · Low‑Risk” or “CARE Screened”). Descriptive label; must align to governance/sovereignty rules. *(See: CARE Principles, Sovereignty.)*
- **CARE Principles** — a framework emphasizing Collective Benefit, Authority to Control, Responsibility, and Ethics in Indigenous data governance. *(In KFM, CARE impacts sensitivity handling and generalization/redaction.)*
- **Catalog (KFM)** — the machine-readable inventory of data products and their metadata/lineage, primarily via STAC/DCAT/PROV.
- **CAMS NRT** — Copernicus Atmosphere Monitoring Service near‑real‑time dataset (domain-specific upstream source). *(Domain-specific; do not treat as a KFM standard.)*
- **Carbon telemetry (`carbon_schema`, `carbon_gCO2e`)** — schema/payload fields for tracking carbon-equivalent emissions of pipeline runs (commonly stored alongside other telemetry). *(See: Energy telemetry.)*
- **Cesium** — a 3D geospatial rendering library referenced for 3D visualization in the UI. *(Often paired with MapLibre for 2D/3D.)*
- **Checksum record** — stored hash values used to validate that acquired files and published artifacts have not changed unexpectedly. *(See: Doc integrity checksum, SBOM.)*
- **CI/CD** — automation that validates, tests, and (optionally) deploys changes (schemas, docs, code). KFM expects validation gates for catalogs and contracts.
- **CI integration (`ci_integration`)** — a front‑matter block pointing to relevant CI workflow files and environments (e.g., `.github/workflows/kfm-ci.yml`, “dev → staging → production”). *(See: Validation gate.)*
- **CIDOC-CRM** — a cultural heritage conceptual reference model used for semantic alignment in some KFM ontology mappings. *(See: Ontology alignment.)*
- **Classification (`classification`)** — a coarse access label for artifacts (e.g., `open`). *(Do not confuse with `sensitivity` or `public_exposure_risk`.)*
- **`commit_sha`** — front‑matter field recording the Git commit SHA associated with this doc version (or the release commit). Use a placeholder until known. *(See: Reproducibility.)*
- **Contract artifact** — a machine-validated specification (schema/contract) that defines what is allowed at a boundary (API payloads, Story Node schema, catalog profiles). Contracts are authoritative; docs explain them. *(See: Contract-first, Schema validation.)*
- **Contract-first** — design discipline where schemas/contracts are defined (and tested) before broad implementation; breaking changes require versioning and compatibility tests. *(See: Contract test.)*
- **Contract test** — automated test that ensures API payloads and schema expectations remain stable across changes.
- **Context bundle** — a provenance-linked package of evidence and metadata used to render Focus Mode views (no unsourced narrative). *(See: Focus Mode, Provenance.)*
- **Cosign** — a tool used to sign and verify container/data artifact signatures and attestations. *(See: Signature, Rekor, SLSA.)*
- **COG (Cloud Optimized GeoTIFF)** — a GeoTIFF formatted for HTTP range requests and efficient tiled access. *(Often a preferred raster asset type.)*
- **CSVW (CSV on the Web)** — W3C metadata pattern for describing CSV files (schema, types, semantics) to improve interoperability. *(Used as an asset type in some KFM data references.)*
- **CSS (Cascading Style Sheets)** — stylesheet language used for UI presentation; referenced in KFM UI/reference materials for implementing responsive, accessible layouts.

### D
- **DCAT (Data Catalog Vocabulary)** — W3C vocabulary for describing datasets in catalogs; used in KFM for interoperable dataset descriptions. *(See: STAC, PROV-O.)*
- **`dcat_profile`** — front‑matter profile/version label for the DCAT rules expected for artifacts in this scope (e.g., `KFM-DCAT v11.0.0`). Treat as declarative; enforcement occurs in schemas/CI. *(See: Schema validation.)*
- **Data contract (`data_contract_ref`)** — schema/contract document describing expectations for a dataset domain (fields, formats, invariants). *(See: Schema validation.)*
- **Data outputs are not code** — KFM convention: datasets, catalogs, and provenance artifacts are produced outputs and belong under `data/` and `releases/`; application logic belongs under `src/`. *(See: Deterministic ETL, Provenance.)*
- **`data_steward`** — front‑matter field naming the accountable steward body/role for a dataset or domain artifact. *(See: Governance.)*
- **Deprecation** — lifecycle stage where a feature or API remains available but is scheduled for removal; must include documentation and migration notes. *(See: API lifecycle registry.)*
- **Deprecated fields (`deprecated_fields`)** — front‑matter list enumerating older keys/standards that should no longer be used. Documentation for reviewers and CI; it does not delete legacy content. *(See: Drift detection.)*
- **Deterministic ETL / deterministic pipeline** — idempotent, config-driven transforms with logged inputs/outputs and stable IDs.
- **Diagram profiles (`diagram_profiles`)** — a front‑matter list describing supported diagram formats used in a doc (e.g., `mermaid-flowchart-v1`). *(See: `fencing_profile`.)*
- **Doc integrity checksum (`doc_integrity_checksum`)** — cryptographic hash (e.g., sha256) of the document content used to detect tampering and support reproducibility.
- **Doc kind (`doc_kind`)** — front‑matter label describing the type of governed artifact (e.g., `Glossary`, `Guide`, `Index`). *(See: `status`.)*
- **Doc UUID (`doc_uuid`)** — a stable, globally unique identifier for a document, typically formatted as a URN (e.g., `urn:kfm:doc:...`). *(See: Semantic document ID.)*
- **Domain expansion pattern** — the “add a domain end‑to‑end” checklist: new sources/ETL + catalogs + graph model + APIs + UI layers + Story Nodes + governance + CI gates. *(See: Extension Matrix.)*
- **Domain pack** — repeatable “vertical slice” of a domain: sources, ETL outputs, catalogs (STAC/DCAT/PROV), graph entities, API surface, UI layers, and Story Nodes.
- **Drift detection** — automated checks that data distributions, schemas, or upstream sources have changed unexpectedly (often paired with freshness gates). *(See: Freshness gate.)*
- **DVC (Data Version Control)** — tool often used to track large datasets and pipeline artifacts without committing large binaries directly to Git.
- **DVC pointer (`dvc_pointers/`)** — small text reference file (tracked in Git) pointing to large data stored outside Git; used for reproducible dataset retrieval.

### E
- **Energy telemetry (`energy_schema`, `energy_wh`)** — schema/payload fields for tracking energy consumption of pipeline runs (commonly stored alongside other telemetry). *(See: Carbon telemetry.)*
- **Entity (PROV / Graph)** — a “thing” in provenance or the knowledge graph (e.g., dataset, map, place, event). *(In PROV: `prov:Entity`.)*
- **ETL (Extract, Transform, Load)** — pipeline stage that ingests raw sources, normalizes formats, and produces processed outputs plus lineage logs.
- **`ethics_ref`** — front‑matter pointer to the canonical ethics document for this artifact’s governance regime. *(Commonly paired with `governance_ref` and `sovereignty_policy`.)*
- **Event source ID (`event_source_id`)** — stable identifier used to reference a document/artifact in an event ledger, enabling traceability across versions. *(See: Provenance.)*
- **Evidence artifact** — versioned, reproducible output that can be cited (processed dataset, catalog entry, provenance bundle, QA report) and linked to Story Nodes and Focus Mode.
- **Evidence-first** — discipline where every UI claim, API value, or narrative assertion traces to a source artifact ID and provenance chain.
- **Extension Matrix** — KFM planning pattern for controlled expansion: adding a domain/capability implies changes across data, catalogs, graph, APIs, UI, narrative, and governance gates. *(See: Pipeline contract, WDE.)*

### F
- **FAIR Principles** — Findable, Accessible, Interoperable, Reusable; KFM cataloging and provenance practices support FAIR.
- **`fair_category`** — front‑matter label describing how an artifact aligns with FAIR (examples include `FAIR+CARE` or rubric-like strings such as `F1-A1-I1-R1`). Treat as a descriptive label unless a rubric is linked.
- **Fail-closed** — posture where validation failures block merges/deployments rather than being skipped. *(See: Validation gate.)*
- **Flexbox** — CSS layout model for arranging items in one dimension (row/column); used in responsive UI components. *(See: CSS, Responsive design.)*
- **Fencing profile (`fencing_profile`)** — front‑matter key (when present) stating repo convention: outer fences in chat use backticks; inner doc fences use tildes (e.g., `~~~text`) for commit-ready markdown.
- **Focus layers (`focus_layers`)** — structured control listing which map layers (or layer IDs) should be emphasized or pinned for a Focus Mode context. *(See: Layer registry.)*
- **Focus Mode** — an experience that consumes only provenance-linked context bundles (**no unsourced narrative**). AI insights are opt-in and must show uncertainty. *(See: Story Node, Provenance, Uncertainty.)*
- **Footer profile (`footer_profile`)** — front‑matter label selecting an approved footer style used to keep governance links consistent across docs. *(See: `header_profile`.)*
- **Freshness gate** — governance/QA check ensuring datasets (or derived products) are within an acceptable “freshness” window, or are explicitly marked stale with rationale.
- **Fulcio** — Sigstore component for issuing short‑lived signing certificates (often used in keyless signing flows). *(See: Sigstore.)*

### G
- **GDAL / OGR** — geospatial processing libraries/tooling (format conversion, reprojection, raster/vector operations). *(Often used for ETL and validation.)*
- **Generalization** — reducing spatial or descriptive precision to protect sensitive entities while preserving analytical usefulness. *(Related: Redaction.)*
- **GeoJSON** — JSON format for representing vector geometries + properties.
- **GeoSPARQL** — OGC/W3C standard vocabulary/functions for geospatial querying in semantic systems (e.g., within-distance, intersects).
- **Getis–Ord (Gi\*)** — local indicator of spatial association used to detect clustering/hotspots in spatial analysis workflows. *(See: Spatial autocorrelation.)*
- **Graph (Knowledge graph)** — semantic core linking entities (Place/Event/Dataset/etc.) and relationships, including provenance links.
- **GraphQL** — typed API style that can expose access to KFM graph-backed data through resolvers.
- **Governance** — the rules, review gates, and policies controlling how data is ingested, published, generalized/redacted, and narrated.
- **Governance refs (`governance_ref`, `ethics_ref`, `sovereignty_policy`)** — front‑matter pointers to canonical governance documents. Drift note: some docs may point into `docs/standards/…` and/or vary `ROOT_GOVERNANCE` naming. Treat these as drift, not separate regimes.

### H
- **Hallucination (in KFM context)** — presenting narrative or claims without provenance-linked sources. Focus Mode forbids hallucinated/unsourced content.
- **Header profile (`header_profile`)** — front‑matter label selecting an approved header style (e.g., “standard”), typically used alongside `badge_profiles` and layout rules.
- **Heading registry (`heading_registry`)** — optional front‑matter block listing allowed/expected section headings (commonly `approved_h2`). Supports doc consistency and automated checks; should not be used to create governance policy.
- **HEC‑RAS** — hydraulic modeling tool referenced in future hydrology roadmap items (e.g., 2D flood models). *(Reference library / roadmap term.)*
- **Hermetic build** — build/run executed in a controlled environment with pinned dependencies and inputs, supporting reproducibility and supply-chain verification. *(See: SLSA.)*

### I
- **Immutability status (`immutability_status`)** — front‑matter label indicating whether an artifact is intended to be immutable once published (commonly `version-pinned`). *(See: Version-pinned.)*
- **Indigenous rights flag (`indigenous_rights_flag`)** — front‑matter flag indicating Indigenous rights/sovereignty considerations apply and must be reviewed per governance policy. *(See: CARE, Sovereignty.)*
- **in‑toto** — supply‑chain framework for describing and verifying steps in a software/data build; attestations may be produced/verified using in‑toto metadata. *(See: Attestation, SLSA.)*
- **Intent (`intent`)** — front‑matter label describing the purpose of an artifact (e.g., `stac-mission-catalog-index`). Prefer stable, machine-friendly strings. *(See: `semantic_intent`.)*
- **Interpolation (spatial)** — estimating values at unsampled locations from sampled points. *(See: Kriging, Semivariogram.)*
- **ISO 8601** — date/time string format standard referenced for consistent time encoding.
- **Item (STAC Item)** — see **STAC Item**.

### J
- **JSON Schema** — machine-readable schema used to validate JSON documents (inputs, outputs, configs, contracts). *(See: Schema validation.)*
- **`json_schema_ref`** — front‑matter pointer to a JSON Schema used to validate this doc’s structure or related artifacts.
- **JSON-LD** — JSON for Linked Data; used to serialize graph semantics and align with W3C vocabularies like DCAT and PROV.
- **`jurisdiction`** — front‑matter label stating legal/policy jurisdiction context for this artifact (e.g., `US-KS`). Used for governance routing and review expectations.

### K
- **Kernel density estimation (KDE)** — technique producing a smooth density surface from point observations; useful for spatial pattern exploration and some map layers.
- **Keyless signing** — signing workflow using OIDC identities and short‑lived certs instead of long-lived keys; commonly associated with Sigstore tooling. *(See: OAuth2/OIDC.)*
- **KFM (Kansas Frontier Matrix)** — geospatial-historical knowledge system with a governed end-to-end pipeline producing interactive maps and provenance-led narratives.
- **KFM-DCAT / KFM-PROV / KFM-STAC profiles** — KFM-specific validation profiles/version targets for DCAT, PROV, and STAC artifacts.
- **KFM-MDP (Markdown protocol)** — KFM governed Markdown conventions (front-matter fields, required section structure, fence rules).
- **KFM-ONTO / KFM-OP** — ontology protocol/version labels. Drift note: some domain docs use `KFM-OP` where core docs use `KFM-ONTO`. Treat `KFM-OP` as a legacy alias until canonical mapping is defined. *(Not confirmed in repo.)*
- **KFM-PPC / KFM-PDC** — pipeline contract/version labels. Drift note: some docs use `KFM-PDC` where core docs use `KFM-PPC`. Treat `KFM-PDC` as a legacy alias until canonical mapping is defined. *(Not confirmed in repo.)*
- **Kriging** — geostatistical interpolation method producing both estimates and uncertainty surfaces. *(See: Semivariogram, Uncertainty.)*

### L
- **LangGraph** — referenced workflow/orchestration approach used in some KFM workflow notes. Treat as implementation detail unless standardized. *(Not confirmed in repo.)*
- **Layer registry** — UI configuration registry listing available map layers, their sources, and access rules; used to prevent unauthorized or sensitive data exposure.
- **`last_updated`** — front‑matter ISO date string representing when this document version was last updated. Used for review cadence and freshness signals.
- **Layout profiles (`layout_profiles`)** — front‑matter list describing approved layout patterns (e.g., “emoji file trees with descriptions”). Formatting convention used to keep docs consistent and machine-extractable. *(See: `machine_extractable`.)*
- **Ledger** — event/log record system used to track artifact creation and changes (`event_source_id` links to ledger entries). *(See: Provenance.)*
- **Lifecycle (`lifecycle`)** — front‑matter label describing expected support horizon (e.g., “LTS”). *(See: Release stage.)*
- **License (`license`)** — front‑matter license identifier for the doc/artifact (e.g., `CC-BY-4.0`). Used to determine reuse permissions.
- **Lineage** — traceability describing how an artifact was produced from inputs and processes. *(See: PROV-O.)*
- **LOD (Level of detail)** — technique to render large datasets efficiently by showing simpler representations at lower zoom levels.

### M
- **Machine-extractable (`machine_extractable`)** — front‑matter boolean indicating the doc is written to be reliably parsed/indexed (stable headings, predictable structure).
- **Manifest (`manifest_ref`)** — versioned release artifact describing what was produced (files, hashes, versions, provenance pointers).
- **MapLibre** — open-source web mapping library referenced for 2D map rendering in KFM.
- **Markdown protocol (`markdown_protocol_version`)** — front‑matter key indicating the KFM Markdown profile/version this doc conforms to (section structure, fence rules, etc.).
- **MCP (`mcp_version`)** — KFM front‑matter version label for the reproducibility/workflow discipline used across runs and artifacts (see `mcp/`). Acronym expansion and `-DL` suffix meaning are **not confirmed in repo**.
- **MCMC (Markov Chain Monte Carlo)** — sampling algorithms used to approximate posterior distributions in Bayesian models.
- **Metadata** — descriptive data about a dataset/artifact (title, description, license, extents, timestamps, provenance pointers, etc.).
- **Metadata profiles (`metadata_profiles`)** — front‑matter list of external standards the artifact claims to align with (e.g., STAC/DCAT/PROV). Declarative alignment list; should match actual emitted artifacts.
- **Micro-STAC** — “item-level, scoped STAC” pattern to keep catalogs small and auditable while interoperable. *(If used, ensure Collections/Items remain valid STAC 1.0.)*
- **Migration (Graph)** — controlled change to ontology or graph structure preserving compatibility or upgrading data safely.
- **Moran’s I** — global spatial autocorrelation statistic measuring whether similar values cluster in space.

### N
- **Neo4j** — graph database used for KFM’s semantic core and relationship queries.
- **NER (Named Entity Recognition)** — extraction technique identifying entities (people, places, organizations) from text. Often used during document processing stages (OCR → NER → human review).
- **Not confirmed in repo** — explicit marker used in KFM docs to flag content that is proposed, missing, or not standardized in the repository.

### O
- **OAuth2/OIDC** — authentication/authorization standards referenced for API/UI security posture; OIDC also supports “keyless” signing flows.
- **OCR (Optical Character Recognition)** — converting scanned documents/images into machine-readable text; OCR outputs should be treated as noisy and validated against originals when used as evidence.
- **OGC** — Open Geospatial Consortium; standards body behind specs like GeoSPARQL.
- **Ontology** — formal definition of entity types, properties, and relationships; used to enforce consistency in the knowledge graph.
- **Ontology alignment (`ontology_alignment`)** — front‑matter mapping from KFM entities/artifacts to external semantic standards (e.g., CIDOC-CRM, GeoSPARQL, PROV-O).
- **Ontology protocol version (`ontology_protocol_version`)** — front‑matter key stating which KFM ontology protocol version governs ontology/graph alignment for this artifact.
- **OpenAPI** — specification for describing REST APIs; used to document and validate REST contracts.
- **OpenAQ** — referenced upstream air-quality data provider/aggregator used in Air Quality documentation.
- **OpenLineage** — open standard for lineage events; referenced as optional/parallel lineage emission alongside PROV-O.
- **OpenTelemetry** — observability standard for metrics/traces/logs; may be used for API/pipeline telemetry emission.
- **ORAS** — tool/approach for pushing arbitrary artifacts (including datasets) to OCI registries; referenced for versioned artifact distribution and provenance attachment.
- **OWL-Time** — W3C ontology for temporal concepts referenced in ontology alignment.

### P
- **Parquet** — columnar storage format commonly used for large analytical datasets; often used in processed outputs.
- **`path`** — front‑matter key specifying the canonical repository location for the document (must match actual file path).
- **Pipeline contract** — non‑negotiable ordering and boundary rules connecting ETL → catalogs → graph → APIs → UI → story. *(See: `pipeline_contract_version`.)*
- **`pipeline_contract_version`** — front‑matter key naming the active pipeline contract profile/version for this artifact (e.g., `KFM-PPC v11.0.0`).
- **Point-in-polygon** — spatial operation assigning polygon attributes to points within each polygon; used in spatial aggregation workflows.
- **Policy engine (Rego)** — policy-as-code format (often associated with OPA) used to express validation rules.
- **PostGIS** — PostgreSQL extension providing spatial types and functions; often used in geospatial ETL and spatial querying.
- **`previous_version_hash`** — front‑matter field storing the checksum/hash of the prior version of an artifact; supports chain-of-custody across versions.
- **PROV-O (W3C Provenance Ontology)** — W3C ontology for representing provenance (entities, activities, agents, relationships like “used” or “generated by”).
- **`prov_profile`** — front‑matter profile/version label for PROV artifacts expected for this scope (e.g., `KFM-PROV v11.0.0`).
- **Provenance** — trace of origin, inputs, process, and responsible parties for an artifact or claim; required for Focus Mode and Story Nodes.
- **Provenance chain (`provenance_chain`)** — front‑matter or doc section pointing to key lineage artifacts (e.g., PROV bundle, run manifest, ledger IDs). *(Exact schema not confirmed in repo.)*
- **Provenance-linked narrative rule** — every narrative claim must trace to a dataset/record/asset ID and provenance.
- **Public exposure risk (`public_exposure_risk`)** — front‑matter label describing risk level if content is public (Low/Medium/High); used to drive review/redaction expectations.
- **Prompt Gate** — allowlist + policy + logging boundary controlling what AI tools can do, what sources they can access, and how outputs are audited. *(Details live in governance docs.)*

### Q
- **Quality signal** — telemetry, tests, or review markers indicating reliability (e.g., validation pass rates, drift detection results, redaction counts).

### R
- **Raster** — gridded data (imagery, elevation). Often stored as GeoTIFF/COG.
- **React** — JavaScript UI library used by KFM frontend (paired with MapLibre/Cesium).
- **Redaction** — removing or hiding sensitive information entirely (e.g., omitting coordinates). *(Related: Generalization.)*
- **Redaction required (`redaction_required`)** — front‑matter boolean indicating whether redaction/generalization must be applied before public release, per governance.
- **Rekor** — Sigstore transparency log where signatures/attestations can be recorded for auditability.
- **Release stage (`release_stage`)** — front‑matter label describing maturity (e.g., “Stable / Governed”, “Pre‑Operational”).
- **Retention policy** — rules defining how long raw sources, logs, and audit artifacts are retained.
- **Review cycle (`review_cycle`)** — front‑matter label describing review frequency and owners (e.g., “Semiannual · FAIR+CARE Council”).
- **Reproducibility** — ability to regenerate outputs from inputs with pinned versions/configs and recorded provenance.
- **Required-status check** — CI job that must pass before merging (enforced via branch protection). *(See: Fail-closed.)*
- **Responsive design** — UI approach that adapts layout/typography/interaction to different screens and inputs; supports a11y and mobile usability.
- **RBAC (Role-Based Access Control)** — authorization model where roles grant specific actions/data access.
- **Risk category (`risk_category`)** — front‑matter label describing risk tier; must align to governance review expectations.

### S
- **SBOM (`sbom_ref`)** — Software Bill of Materials reference to an inventory of components/dependencies for a release (often SPDX).
- **Schema drift** — breaking or unexpected change in schemas/fields/structures; should be caught by schema validation and contract tests.
- **Schema validation** — automated checks that artifacts conform to required schemas/profiles (STAC/DCAT/PROV, JSON Schema, SHACL, OpenAPI).
- **Scope (`scope`)** — front‑matter block defining what domain/system a doc applies to (commonly includes `domain` and `applies_to`). Prevents “floating governance.”
- **Semantic document ID (`semantic_document_id`)** — stable, human-readable identifier used across systems/tools (distinct from `doc_uuid`).
- **Semantic intent (`semantic_intent`)** — front‑matter list describing the semantic purpose of an artifact. Controlled vocabulary values are preferred when available. *(Not confirmed in repo.)*
- **Sensitivity (`sensitivity`)** — label indicating potential harm if details are disclosed; may require generalization/redaction.
- **Sensitivity level (`sensitivity_level`)** — front‑matter severity tier; taxonomy not confirmed in repo.
- **Semivariogram / variogram** — model of spatial variance vs distance used in kriging/interpolation workflows.
- **SHACL (`shape_schema_ref`)** — Shapes Constraint Language for expressing constraints over RDF graphs.
- **`shape_schema_ref`** — front‑matter pointer to a SHACL/shape file used to validate RDF artifacts.
- **Signature (`signature_ref`)** — cryptographic signature file for a release/artifact.
- **Sigstore** — keyless signing and transparency log ecosystem (Fulcio + Rekor + related tooling).
- **SLSA** — supply-chain integrity framework; referenced for provenance verification.
- **Sovereignty policy (`sovereignty_policy`)** — front‑matter pointer to the canonical sovereignty policy doc; governs publication/generalization for affected datasets.
- **Spatial autocorrelation** — relationship between similarity and spatial proximity (global: Moran’s I; local: Getis–Ord).
- **Spatial join** — operation combining attributes of spatial datasets based on spatial relationships (within, intersects).
- **Spectral graph theory** — analysis of graphs using eigenvalues/eigenvectors (graph Laplacian) for structure, diffusion, embeddings.
- **SPDX** — standard format for SBOMs.
- **STAC (SpatioTemporal Asset Catalog)** — open specification for describing geospatial assets and collections using JSON.
- **STAC Collection** — STAC object grouping items and defining shared metadata/extents.
- **STAC Item** — STAC object representing a single spatiotemporal unit with assets (scenes/tiles/slices).
- **STAC Asset** — see **Asset (STAC Asset)**.
- **`stac_profile`** — front‑matter profile/version label for STAC rules expected for artifacts in this scope (e.g., `KFM-STAC v11.0.0`).
- **Status (`status`)** — front‑matter lifecycle state for a document (e.g., `draft`, `template`). Not the same as `release_stage` (maturity).
- **Story Node** — governed narrative artifact that is machine-ingestible and provenance-linked; must cite every factual claim.
- **Sunset policy (`sunset_policy`)** — front‑matter field describing when/how an artifact is superseded or retired; not a deletion instruction by itself.

### T
- **Telemetry (`telemetry_ref`, `telemetry_schema`)** — logging/metrics collected to observe performance, security, and governance compliance; stored with schema pointers when governed.
- **Test profiles (`test_profiles`)** — front‑matter list naming validations expected (e.g., `markdown-lint`, `schema-lint`, `pii-scan`). Enforcement depends on CI.
- **Tiling** — partitioning large spatial datasets into smaller pieces for fast rendering and retrieval.
- **`title`** — front‑matter key holding the human-readable document title used in indexes and navigation.
- **Transform registry (`transform_registry`)** — optional front‑matter block enumerating allowed vs prohibited AI transforms, typically mirroring `ai_transform_permissions` / `ai_transform_prohibited`. *(See: Prompt Gate.)*
- **TTL policy (`ttl_policy`)** — front‑matter key describing how long an artifact is considered valid before review/expiration; does not grant deletion authority.
- **TypeScript** — typed JavaScript used in many React codebases to improve correctness and maintainability.
- **Time slider** — UI control to filter layers and context by time.

### U
- **Uncertainty** — quantitative/qualitative indicator for confidence in model outputs or inferred claims. AI-derived insights must be labeled and opt-in.
- **User overlay** — user-provided dataset ingested via controlled ETL; typically sandboxed/unverified until reviewed.

### V
- **Validation gate** — mandatory check in CI/CD (schemas, tests, docs lint, policy checks) that must pass before changes are accepted.
- **Verification & Validation (V&V / VV&A)** — modeling discipline: verification checks implementation matches intended model; validation checks model matches reality; accreditation is acceptance for a use case.
- **Version-pinned** — immutability posture where published artifacts are tied to an explicit version and not changed in place; updates create new versions.
- **`version`** — front‑matter semantic version for the document (e.g., `v1.2.1`). When bumped, update `doc_uuid`, `semantic_document_id`, `event_source_id`, and version history.

### W
- **W3C** — standards body behind DCAT, PROV-O, OWL-Time.
- **WCAG** — accessibility standard referenced in KFM docs (often WCAG 2.1 AA) as UI/docs target.
- **WDE (World Discovery Engine)** — referenced innovation/extension concept; WDE work implies new data products, graph entities, API extensions, and validation.
- **WebGL** — browser graphics API used for high-performance rendering.
- **Windowed operation** — stream processing pattern where computations occur over time/record windows; relevant for scalable pipeline designs.
- **WKT (Well-Known Text)** — text format for geometries; commonly used in semantic/GeoSPARQL contexts.
- **Workflow** — defined set of pipeline steps executed reproducibly and recorded in provenance.

### Y
- **YAML front-matter** — metadata block at the top of governed Markdown docs containing versioning, provenance refs, governance refs, and AI permissions.

### Z
- **Zoom level** — map scale index controlling what data is shown; affects tiling, LOD, and rendering decisions.

## 🗺️ Diagrams
- Not required for this glossary. *(If future work adds term-dependency diagrams, place them here and list `diagram_profiles` if used.)*

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Canonical terminology sources | Markdown | `docs/` (e.g., Master Guide + templates) | Markdown protocol checks + linkcheck |
| Governance terminology | Markdown | `docs/governance/` | Linkcheck (no policy authored here) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| KFM Glossary | Markdown | `docs/glossary.md` | KFM-MDP (front‑matter + section structure) |

### Sensitivity & redaction
- This doc is **definitions-only** and should not include:
  - protected site coordinates,
  - operationally sensitive locations,
  - examples that would enable re-identification.
- If a term requires an example, prefer a generic placeholder example and defer specifics to governed datasets.

### Quality signals
- Alphabetical term organization (A–Z) with consistent formatting conventions.
- Front‑matter key coverage includes core keys used in templates (or explicitly marked TBD).
- Drift/alias notes are clearly labeled as drift (not policy).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This glossary does not emit STAC payloads.
- It provides canonical terminology for STAC objects (Collection/Item/Asset) and common STAC-adjacent concepts (BBox, COG).

### DCAT
- This glossary does not emit DCAT payloads.
- It provides canonical terminology for dataset catalog semantics and interoperability language.

### PROV-O
- This glossary does not emit PROV bundles.
- It standardizes provenance language used across docs and Story Nodes.

### Versioning expectations
- Treat versions as **immutable identifiers**: updates create a new version, update IDs, and append a version-history row.
- Prefer stable, machine-friendly IDs (`doc_uuid`, `semantic_document_id`, `event_source_id`) for cross-layer linking.

## 🧱 Architecture

### Components (contextual map)
| Layer | Component | Canonical home | Notes |
|---|---|---|---|
| ETL | Pipelines | `src/pipelines/` | Deterministic ingestion + transforms |
| Catalog | STAC/DCAT/PROV | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Discovery + interoperability + lineage |
| Graph | Neo4j graph build | `src/graph/` | Ontology bindings + migrations |
| API | Contract boundary | `src/server/` | Redaction/generalization and API contracts |
| UI | Map + Focus Mode | `web/` | Must not read Neo4j directly |
| Story | Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narratives |
| Docs | Glossary (this doc) | `docs/glossary.md` | Shared vocabulary across layers |

### Interfaces / contracts (non-exhaustive)
| Boundary | Contract artifact | Path | Notes |
|---|---|---|---|
| Docs authoring | Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | *not confirmed in repo* |
| API boundary | OpenAPI / GraphQL contracts | `src/server/` + `schemas/` | Repo-defined layout |
| Catalog outputs | STAC/DCAT/PROV schemas | `schemas/` | Includes story/ui/telemetry schemas (if present) |
| Story ingestion | Story Node schema/template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Schema path may exist under `schemas/` (not confirmed) |
| UI layer registry | Layer registry + schema | `web/` | Exact path not confirmed |

### Extension points checklist (for glossary updates)
- [ ] New subsystem concept added (ETL/catalog/graph/API/UI/story): add a glossary term.
- [ ] New front‑matter key added in a governed template: add a `front_matter_key` entry.
- [ ] Path/protocol naming drift discovered: add a drift note (do not redefine policy).
- [ ] Term impacts governance/sensitivity: flag for governance-owner review.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes and Focus Mode UI should link to this glossary for shared terminology (especially provenance and governance language).
- Definitions here help keep narrative claims consistent with contract terminology (catalog/graph/API layers).

### Provenance-linked narrative rule
- Every narrative claim must map to a cited dataset/document ID and its provenance chain.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front‑matter + required sections)
- [ ] Link check to referenced docs (as implemented in CI)
- [ ] Schema validation (STAC/DCAT/PROV; plus JSON/SHACL/OpenAPI where applicable)
- [ ] API contract tests (OpenAPI/GraphQL) *(when glossary terms drive contract changes)*
- [ ] Security checks (secret/PII scanning) for docs *(as configured)*
- [ ] Sovereignty/sensitivity review for any content that could expose protected locations

### Reproduction
~~~bash
# (Repo-specific commands may differ.)
# markdownlint docs/glossary.md
# linkcheck docs/glossary.md
~~~

### Telemetry signals (if applicable)
- Not applicable (documentation-only artifact). For terminology related to telemetry, see glossary entries: **Telemetry**, **Quality signal**, **Validation gate**.

## ⚖ FAIR+CARE & Governance

### Review gates
- If a term impacts governance (e.g., sensitivity categories, redaction rules), it should be reviewed by the governance owners referenced in front‑matter.

### CARE / sovereignty considerations
- Ensure terms related to Indigenous data governance remain aligned to the sovereignty policy.
- Do not include sensitive site examples or protected coordinates in definitions.

### AI usage constraints
- This glossary can be summarized or indexed, but must not be used to invent policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial glossary: core pipeline, cataloging, graph, API/UI, governance terms. | Bartytime |
| v1.1.0 | 2025-12-24 | Expanded glossary: front‑matter metadata keys, supply‑chain/telemetry terms, lifecycle registry, and architecture drift notes. | Bartytime |
| v1.2.0 | 2025-12-27 | Aligned glossary to universal doc conventions; added front‑matter registry keys and domain artifact terminology; clarified known drift (paths + protocol aliases). | Bartytime |
| v1.2.1 | 2025-12-29 | Alignment pass: synced key artifact paths/wording to Master Guide v12; added missing core front‑matter key definitions (`title`, `path`, `version`, `last_updated`, `license`, profile/version keys); normalized duplicate STAC entries via cross‑refs; tightened CI/governance sections. | Bartytime |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`