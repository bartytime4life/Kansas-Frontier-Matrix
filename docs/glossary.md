---
title: "KFM Glossary"
path: "docs/glossary.md"
version: "v1.2.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:glossary:v1.2.0"
semantic_document_id: "kfm-glossary-v1.2.0"
event_source_id: "ledger:kfm:doc:glossary:v1.2.0"
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
- Provide **canonical definitions** for common terms and acronyms used across KFM docs, pipelines, catalogs, graph, APIs, UI, and Story Nodes.
- Standardize the meaning of common **front‑matter keys** (including optional “registry” blocks such as `heading_registry`, `layout_profiles`, and `transform_registry`) to reduce ambiguity in governance and CI reviews.
- Track **known terminology drift / aliases** (e.g., older protocol labels and path variants) so reviewers can spot inconsistencies without treating them as policy.

### Scope
| In Scope | Out of Scope |
|---|---|
| Definitions for KFM concepts, standards, and common geospatial/graph terms used in KFM docs | Full external standards documentation (STAC/DCAT/PROV specs themselves) |
| Project-specific terms (Focus Mode, Story Nodes, Extension Matrix, WDE, etc.) | New governance policy creation (refer to governance docs) |
| Common metadata keys used in KFM front‑matter (e.g., `doc_uuid`, `review_cycle`, `ai_training_inclusion`) | Replacing governed templates (use the templates in `docs/templates/`) |
| Non‑policy descriptions of CI/validation “signals” and doc profiles (e.g., `test_profiles`, `ci_integration`) | Declaring a validation gate as mandatory unless governance/CI enforces it (link to CI config if present) |

### Audience
- Primary: contributors writing docs or implementing pipeline/graph/API/UI changes
- Secondary: reviewers validating provenance, sensitivity, and contract compliance

### Definitions (link to glossary)
- You are here: `docs/glossary.md`

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Repository README | `README.md` | Maintainers | Project overview + pipeline contract summary *(may be absent in some repo branches — not confirmed in repo)* |
| Master Guide (canonical pipeline) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + subsystem inventory + Extension Matrix |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Default governed doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Governed narrative artifact structure |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required structure for API changes |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Draft “one canonical home per subsystem”; adoption status TBD |
| Domain governance example | `docs/data/air-quality/README.md` | Domain owners | Shows extended front‑matter keys (`scope`, `semantic_intent`, `metadata_profiles`) and path drift in governance refs |
| Historical domain module example | `docs/data/historical/land-treaties/README.md` | Domain owners | Shows high-sensitivity handling expectations and story-node contract references |
| Data-domain readme example | `data/raw/tabular/README.md` | Domain owners | Shows additional keys (`data_steward`, `risk_category`, `ontology_alignment`, `json_schema_ref`) |
| Reference library (methods) | `KFM-*/*.pdf` | Maintainers | Modeling, spatial analysis, web rendering, scalable data mgmt (shared vocabulary) |

### Definition of done for this document
- [x] Front‑matter complete and `path` matches file location
- [ ] New terms introduced in docs/pipelines/graph/api/ui/story/design are added here
- [ ] Known naming/alias drift is documented as **drift** (not as policy)
- [ ] Governance-related terminology (sensitivity/redaction/CARE) remains consistent with governance refs in front‑matter
- [ ] Link check to referenced docs passes (as implemented in CI)
- [ ] No new governance policy is authored in this glossary

## 🗂️ Directory Layout

### This document
- `path`: `docs/glossary.md`

### Related repository paths (canonical targets)
| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Governed documentation, templates, design notes |
| Docs (governance) | `docs/governance/` | Governance/ethics/sovereignty root docs *(path drift exists — see glossary)* |
| Docs (standards) | `docs/standards/` | Protocol and standards docs *(may be absent in some repo branches — not confirmed in repo)* |
| Docs (architecture) | `docs/architecture/` | Architecture notes, redesign blueprints |
| Docs (domain runbooks) | `docs/data/<domain>/` | Domain notes, requirements, governance runbooks |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Telemetry (docs) | `docs/telemetry/` + `schemas/telemetry/` | Metrics/logs + schemas (build/runtime) |
| Data staging | `data/raw/<domain>/` · `data/work/<domain>/` · `data/processed/<domain>/` | Source snapshots, work products, processed datasets |
| Domain data root | `data/<domain>/` | Domain-specific configs/governance/caches (varies by repo branch — not confirmed in repo) |
| STAC catalogs | `data/stac/` | STAC Collections/Items + assets discovery metadata |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views (catalog interoperability) |
| PROV lineage | `data/prov/` | PROV bundles (lineage/traceability) |
| Graph | `src/graph/` | Ontology, migrations, constraints, loaders |
| Graph import/export | `data/graph/` | CSV/Cypher/fixtures for graph import and QA |
| Pipelines | `src/pipelines/` | ETL + catalog build pipelines |
| APIs | `src/server/` | REST/GraphQL services + contracts *(`src/api/` may exist if legacy — not confirmed in repo)* |
| Frontend | `web/` | React/MapLibre/Cesium UI *(must not read Neo4j directly)* |
| Schemas | `schemas/` | JSON/SHACL/contract schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Tests | `tests/` | Unit/integration/contract tests |
| MCP runs | `mcp/` | Run logs, experiments, reproducibility artifacts |
| Releases | `releases/` | Versioned manifests, SBOMs, signatures, attestations |
| CI workflows | `.github/workflows/` | Build/test/lint/policy workflows |
| CI lineage docs | `.github/lineage/` | Human-readable lineage + boundary rules *(if present — not confirmed in repo)* |

### Expected file tree (repo root, partial)
~~~text
📁 .github/
├─ 📁 workflows/
├─ 📁 lineage/           # (if present)
📁 data/
├─ 📁 raw/
│  └─ 📁 <domain>/
├─ 📁 work/
│  └─ 📁 <domain>/
├─ 📁 processed/
│  └─ 📁 <domain>/
├─ 📁 stac/
├─ 📁 catalog/
│  └─ 📁 dcat/
├─ 📁 prov/
└─ 📁 graph/
📁 docs/
├─ 📄 glossary.md
├─ 📄 MASTER_GUIDE_v12.md
├─ 📁 templates/
├─ 📁 governance/
├─ 📁 standards/          # (if used in this repo branch)
├─ 📁 architecture/
├─ 📁 telemetry/
├─ 📁 reports/
│  └─ 📁 story_nodes/
└─ 📁 data/
   └─ 📁 <domain>/
📁 mcp/
├─ 📁 runs/
└─ 📁 experiments/
📁 schemas/
📁 src/
├─ 📁 pipelines/
├─ 📁 graph/
└─ 📁 server/
📁 tests/
📁 tools/
📁 web/
📁 releases/
~~~

## 🧭 Context

### Background
KFM spans multiple technical layers (data → catalogs → graph → APIs → UI → narrative). A shared glossary keeps those layers interoperable and reduces “terminology drift” across contributions.

### Assumptions
- The glossary is a living document.
- Terms should be defined in a way that remains stable even as implementation details evolve.
- If two spellings/paths appear in project docs, prefer the *governed* one and add an explicit glossary entry noting the drift.

### Constraints / invariants
- Use the canonical pipeline ordering language consistently:
  - ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- Do not define new policy here; link to governance docs for rules.
- UI does **not** read Neo4j directly; the API layer is the contract boundary.
- Contracts/schemas are authoritative at boundaries (API contracts, STAC/DCAT/PROV profiles, Story Node schemas). “Docs describe; contracts decide.”
- Data outputs are **not** code: derived datasets and catalog/provenance outputs live under `data/` and `releases/`, not `src/`.

### How to update this glossary
1. Add new terms when you introduce a new concept, acronym, schema field name, or subsystem name.
2. Prefer **project meanings** over textbook meanings if KFM uses a term in a specific way.
3. If a term is disputed or evolving, define it as a **working definition** and mark it `TBD` for governance review.
4. If a doc uses a front‑matter key not defined here, add it under the appropriate letter.
5. If you discover naming drift (paths, protocol aliases), add a **Drift note** entry rather than “fixing by definition.”

### Open questions (tracked here so drift doesn’t become policy)
| Topic | What’s drifting | Why it matters | Current stance |
|---|---|---|---|
| Governance doc paths | `docs/governance/*` vs `docs/standards/governance/*` | Links, CI linkcheck, reviewer expectations | Prefer `docs/governance/*` (Master Guide + templates), record alternates as drift |
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
- **`accessibility_compliance`** — front‑matter label stating the accessibility target met or aimed for (e.g., “WCAG 2.1 AA”). This is a declarative target/claim that should align to CI checks when present. *(See: WCAG, `test_profiles`.)*
- **AirNow** — a referenced air-quality source system used in Air Quality domain docs; treated as an upstream data provider in KFM ingestion plans. *(See: OpenAQ, CAMS NRT.)*
- **AI focusmode usage (`ai_focusmode_usage`)** — front‑matter control describing whether an artifact’s content may be surfaced in Focus Mode (e.g., “Allowed with restrictions”, “Restricted”). *(See: Focus Mode, AI transform permissions.)*
- **AI training inclusion (`ai_training_inclusion`)** — front‑matter boolean indicating whether an artifact may be included in AI training corpora. When `false`, exclude from training and do not treat the artifact as a training example. *(See: AI transform permissions/prohibited.)*
- **AI transform permissions (`ai_transform_permissions`)** — allowed AI operations on a document (e.g., `summarize`, `metadata-extraction`, `layout-normalization`). These permissions are not a license to invent facts; provenance and governance rules still apply. *(See: `transform_registry`, Hallucination, Provenance.)*
- **AI transform prohibited (`ai_transform_prohibited`)** — AI operations explicitly disallowed (e.g., `infer_sensitive_locations`, `speculative-additions`, `governance-override`). *(See: `transform_registry`.)*
- **API (Application Programming Interface)** — the contract boundary between clients (UI/tools) and KFM’s backend services. KFM’s UI should consume data via APIs or pre-built artifacts, not direct graph access.
- **API lifecycle registry** — a versioned record tracking API surfaces through lifecycle states (e.g., Proposed → Draft → Alpha → Beta → Stable → Deprecated → Retired). *(See: Deprecation, Validation gate.)*
- **AQP (Approximate Query Processing)** — techniques for returning fast, approximate results (with uncertainty bounds) on large datasets; relevant to scalable KFM analytics and exploratory UI queries. *(Reference library term.)*
- **Asset (STAC Asset)** — a file/resource referenced from a STAC Item (e.g., COG, GeoJSON, PDF, thumbnail). *(See: STAC Asset, STAC Item.)*
- **Attestation (`attestation_ref`)** — a signed statement about how an artifact was built (often SLSA/in‑toto formatted) used to verify provenance and supply‑chain integrity. *(See: SLSA, in‑toto, Signature, Rekor, Cosign.)*
- **Audit panel** — a Focus Mode UI panel intended to show governance flags, provenance pointers, and redaction/generalization status. *(See: Focus Mode, Governance, Redaction.)*

### B
- **BBox (Bounding box)** — a rectangular spatial extent, typically `[west, south, east, north]`, used for spatial indexing and discovery. *(Often used in STAC.)*
- **Bayesian inference** — statistical inference that updates beliefs from prior → posterior using Bayes’ theorem; used for uncertainty-aware modeling and decision support in analytical extensions. *(See: Uncertainty, MCMC.)*
- **Badge profiles (`badge_profiles`)** — a front‑matter list describing which standardized badge layouts a doc may use (e.g., a centered badge row). These are *presentation conventions* and should not introduce new governance meaning. *(See: `layout_profiles`, `header_profile`.)*
- **BLB (Bag of Little Bootstraps)** — a scalable bootstrapping approach used for uncertainty estimation on large data. *(Reference library term; see: Uncertainty.)*
- **Branch protection** — repository controls that require CI checks (and often reviews) before merging; used to enforce validation gates. *(See: Required-status check, Fail-closed.)*
- **Branding registry (`branding_registry`)** — a front‑matter block enumerating approved “taglines” or brand statements for specific doc categories. Treat as a controlled vocabulary for presentation. *(See: `badge_profiles`.)*

### C
- **CARE label (`care_label`)** — a front‑matter classification describing how CARE applies (examples include “Public · Low‑Risk” or “CARE Screened”). This label is descriptive and must align to governance/sovereignty rules. *(See: CARE Principles, Sovereignty.)*
- **CARE Principles** — a framework emphasizing Collective Benefit, Authority to Control, Responsibility, and Ethics in Indigenous data governance. *(In KFM, CARE impacts sensitivity handling and generalization/redaction.)*
- **Catalog (KFM)** — the machine-readable inventory of data products and their metadata/lineage, primarily via STAC/DCAT/PROV.
- **CAMS NRT** — Copernicus Atmosphere Monitoring Service near‑real‑time dataset (domain-specific upstream source). *(Domain-specific; do not treat as a KFM standard.)*
- **Carbon telemetry (`carbon_schema`, `carbon_gCO2e`)** — schema/payload fields for tracking carbon-equivalent emissions of pipeline runs (commonly stored alongside other telemetry). *(See: Energy telemetry.)*
- **Cesium** — a 3D geospatial rendering library referenced for 3D visualization in the UI. *(Often paired with MapLibre for 2D/3D.)*
- **Checksum record** — stored hash values used to validate that acquired files and published artifacts have not changed unexpectedly. *(See: Doc integrity checksum, SBOM.)*
- **CI/CD** — automation that validates, tests, and (optionally) deploys changes (schemas, docs, code). KFM expects validation gates for catalogs and contracts.
- **CI integration (`ci_integration`)** — a front‑matter block pointing to relevant CI workflow files and environments (e.g., `.github/workflows/kfm-ci.yml`, “dev → staging → production”). *(See: Validation gate.)*
- **CIDOC-CRM** — a cultural heritage conceptual reference model used for semantic alignment in some KFM ontology mappings. *(See: Ontology alignment.)*
- **Classification (`classification`)** — a coarse access label for artifacts (e.g., `open`, “Public With Safeguards”). *(Do not confuse with `sensitivity` or `public_exposure_risk`.)*
- **`content_stability`** — front‑matter label describing how stable an artifact is expected to be (e.g., `stable`). *(See: Version-pinned, Review cycle.)*
- **Contract artifact** — a machine-validated specification (schema/contract) that defines what is allowed at a boundary (API payloads, Story Node schema, catalog profiles). Contracts are authoritative; docs explain them. *(See: Contract-first, Schema validation.)*
- **Contract-first** — design discipline where schemas/contracts are defined (and tested) before broad implementation; prevents UI/API drift and supports governance reviews. *(See: Contract test, API, Schema validation.)*
- **Contract test** — an automated test that ensures API payloads and schema expectations remain stable across changes.
- **Cosign** — a tool used to sign and verify container/data artifact signatures and attestations. *(See: Signature, Rekor, SLSA.)*
- **COG (Cloud Optimized GeoTIFF)** — a GeoTIFF formatted for HTTP range requests and efficient tiled access. *(Often a preferred raster asset type.)*
- **CSVW (CSV on the Web)** — W3C metadata pattern for describing CSV files (schema, types, semantics) to improve interoperability. *(Used as an asset type in some KFM data references.)*
- **CSS (Cascading Style Sheets)** — stylesheet language used for UI presentation; referenced in KFM’s UI/reference materials for implementing responsive, accessible layouts.

### D
- **DCAT (Data Catalog Vocabulary)** — W3C vocabulary for describing datasets in catalogs; used in KFM for interoperable dataset descriptions. *(See: STAC, PROV-O.)*
- **Data contract (`data_contract_ref`)** — a schema/contract document describing expectations for a dataset domain (fields, formats, invariants). *(See: Schema validation.)*
- **Data outputs are not code** — KFM convention: datasets, catalogs, and provenance artifacts are produced outputs and belong under `data/` and `releases/`; application logic belongs under `src/`. *(See: Deterministic ETL, Provenance.)*
- **`data_steward`** — front‑matter field naming the accountable steward body/role for a dataset or domain artifact (e.g., “KFM FAIR+CARE Council”). *(See: Governance.)*
- **Deprecation** — lifecycle stage where a feature or API remains available but is scheduled for removal; must include documentation and migration notes. *(See: API lifecycle registry.)*
- **Deprecated fields (`deprecated_fields`)** — front‑matter list enumerating older keys/standards that should no longer be used. This is documentation for reviewers and CI; it does not “delete” legacy content. *(See: Drift detection.)*
- **Deterministic ETL** — ETL runs that produce the same outputs given the same inputs, versions, and configs (including fixed random seeds when applicable).
- **Diagram profiles (`diagram_profiles`)** — a front‑matter list describing supported diagram formats used in a doc (e.g., `mermaid-flowchart-v1`). *(See: `fencing_profile`, Diagrams.)*
- **Doc integrity checksum (`doc_integrity_checksum`)** — cryptographic hash (e.g., sha256) of the document content used to detect tampering and support reproducibility.
- **Doc kind (`doc_kind`)** — front‑matter label describing the type of governed artifact (e.g., `Glossary`, `Guide`, `Data Governance`, `Index`). Treat as a classification for reviewers and tooling. *(See: `status`, `intent`.)*
- **Doc UUID (`doc_uuid`)** — a stable, globally unique identifier for a document, typically formatted as a URN (e.g., `urn:kfm:doc:...`). *(See: Semantic document ID.)*
- **Domain expansion pattern** — the “add a domain end‑to‑end” checklist: new sources/ETL + catalogs + graph model + APIs + UI layers + Story Nodes + governance + CI gates. *(See: Extension Matrix.)*
- **Domain pack** — a repeatable “vertical slice” of a domain consisting of (at minimum) sources, ETL outputs, catalogs (STAC/DCAT/PROV), graph entities, API surface, UI layers, and Story Nodes. *(See: Evidence artifact, Extension Matrix.)*
- **Drift detection** — automated checks that data distributions, schemas, or upstream sources have changed unexpectedly (often paired with freshness gates). *(See: Freshness gate.)*
- **DVC (Data Version Control)** — tool often used to track large datasets and pipeline artifacts without committing large binaries directly to Git.
- **DVC pointer (`dvc_pointers/`)** — a small text reference file (tracked in Git) that points to large data stored outside Git; used for reproducible dataset retrieval.

### E
- **Energy telemetry (`energy_schema`, `energy_wh`)** — schema/payload fields for tracking energy consumption of pipeline runs (commonly stored alongside other telemetry). *(See: Carbon telemetry.)*
- **Entity (PROV / Graph)** — a “thing” in provenance or the knowledge graph (e.g., dataset, map, place, event). *(In PROV: `prov:Entity`.)*
- **ETL (Extract, Transform, Load)** — pipeline stage that ingests raw sources, normalizes formats, and produces processed outputs plus lineage logs.
- **Event source ID (`event_source_id`)** — a stable identifier used to reference a document/artifact in an event ledger, enabling traceability across versions. *(See: Provenance.)*
- **Evidence artifact** — a versioned, reproducible output that can be cited (processed dataset, catalog entry, provenance bundle, QA report) and linked to Story Nodes and Focus Mode. *(See: Provenance, Contract artifact.)*
- **Evidence-first** — design discipline where every UI claim, API value, or narrative assertion traces to a source artifact ID and its provenance chain. *(See: Provenance-linked narrative rule.)*
- **Extension Matrix** — KFM planning pattern for controlled expansion: adding a new domain or capability implies changes across data, catalogs, graph, APIs, UI, narrative, and governance gates. *(See: Pipeline contract, WDE.)*

### F
- **FAIR Principles** — Findable, Accessible, Interoperable, Reusable; KFM’s cataloging and provenance practices support FAIR.
- **`fair_category`** — front‑matter label describing how an artifact aligns with FAIR (examples include `FAIR+CARE`, `FAIR-Aligned`, or rubric-like strings such as `F1-A1-I1-R1`). Treat as a descriptive label unless a rubric is linked. *(See: CARE, Governance.)*
- **Fail-closed** — security/quality posture where validation failures block merges/deployments rather than being skipped. *(See: Validation gate.)*
- **Flexbox** — CSS layout model for arranging items in one dimension (row/column); commonly used in responsive UI components. *(See: CSS, Responsive design.)*
- **Fencing profile (`fencing_profile`)** — front‑matter key (when present) stating the repo convention: outer fences use backticks in chat; inner doc fences use tildes (e.g., `~~~text`) for commit-ready markdown.
- **Focus layers (`focus_layers`)** — structured control listing which map layers (or layer IDs) should be emphasized or pinned for a Focus Mode context. *(See: Layer registry.)*
- **Focus Mode** — an interactive, topic-centric UI mode that freezes context (area/time/topic) and presents a consolidated dashboard with citations and governance signals. Focus Mode is provenance-only: nothing appears without a source; AI insights are opt-in and must show uncertainty. *(See: Story Node, Provenance, Uncertainty.)*
- **Footer profile (`footer_profile`)** — front‑matter label selecting an approved footer style (e.g., “standard”). Used to keep governance links and doc navigation consistent across domains. *(See: `header_profile`, Footer refs.)*
- **Freshness gate** — governance/QA check ensuring datasets (or derived products) are within an acceptable “freshness” window, or are explicitly marked stale with rationale. *(Often paired with drift detection.)*
- **Fulcio** — a Sigstore component for issuing short‑lived signing certificates (often used in keyless signing flows). *(See: Sigstore, Keyless signing.)*

### G
- **GDAL / OGR** — geospatial data processing libraries/tooling (format conversion, reprojection, raster/vector operations). *(Often used for ETL and validation.)*
- **Generalization** — reducing spatial or descriptive precision to protect sensitive entities while preserving analytical usefulness. *(Related: Redaction.)*
- **GeoJSON** — JSON format for representing vector geometries + properties.
- **GeoSPARQL** — OGC/W3C standard vocabulary/functions for geospatial querying in semantic systems (e.g., within-distance, intersects). *(KFM aligns geospatial semantics with GeoSPARQL concepts where applicable.)*
- **Getis–Ord (Gi\*)** — a local indicator of spatial association used to detect clustering/hotspots in spatial analysis workflows. *(See: Spatial autocorrelation.)*
- **Graph (Knowledge graph)** — the semantic core linking entities (Place/Event/Dataset/etc.) and relationships, including provenance links.
- **GraphQL** — a query language/API style that can expose typed access to KFM graph-backed data through resolvers.
- **Governance** — the rules, review gates, and policies controlling how data is ingested, published, generalized/redacted, and narrated.
- **Governance refs (`governance_ref`, `ethics_ref`, `sovereignty_policy`)** — front‑matter pointers to the canonical governance docs. Drift notes: some project docs point into `docs/standards/…` and some use `ROOT-GOVERNANCE.md` vs `ROOT_GOVERNANCE.md`. Treat these as **drift**, not as separate governance regimes. *(Canonical location should be standardized — not confirmed in repo.)*

### H
- **Hallucination (in KFM context)** — presenting narrative or claims without provenance-linked sources. Focus Mode forbids hallucinated/unsourced content.
- **Header profile (`header_profile`)** — front‑matter label selecting an approved header style (e.g., “standard”), typically used alongside `badge_profiles` and layout rules. *(See: `footer_profile`.)*
- **Heading registry (`heading_registry`)** — optional front‑matter block listing allowed/expected section headings (commonly `approved_h2`). This supports doc consistency and automated checks, but should not be used to forbid domain-required headings unless CI enforces it. *(See: `test_profiles`.)*
- **HEC‑RAS** — a hydraulic modeling tool referenced in future hydrology roadmap items (e.g., 2D flood models). *(Reference library / roadmap term.)*
- **Hermetic build** — a build/run executed in a controlled environment with pinned dependencies and inputs, supporting reproducibility and supply-chain verification. *(See: Deterministic ETL, SLSA.)*

### I
- **Immutability status (`immutability_status`)** — front‑matter label indicating whether an artifact is intended to be immutable once published (commonly `version-pinned` in KFM docs). *(See: Version-pinned.)*
- **Indigenous rights flag (`indigenous_rights_flag`)** — front‑matter boolean/flag indicating that Indigenous rights/sovereignty considerations apply and must be reviewed per governance policy. *(See: CARE, Sovereignty.)*
- **in‑toto** — a supply‑chain framework for describing and verifying steps in a software/data build; attestations may be produced/verified using in‑toto metadata. *(See: Attestation, SLSA.)*
- **Intent (`intent`)** — front‑matter label describing the purpose of an artifact (e.g., `stac-mission-catalog-index`, `raw-tabular-data`). Prefer stable, machine-friendly strings. *(See: `semantic_intent`.)*
- **Interpolation (spatial)** — estimating values at unsampled locations from sampled points, often via kriging or related methods. *(See: Kriging, Semivariogram.)*
- **ISO 8601** — date/time string format standard referenced for consistent time encoding (important for timeline filtering and temporal metadata).
- **ISO 14064 / ISO 50001** — referenced standards related to greenhouse gas accounting and energy management; sometimes used as alignment targets for telemetry reporting. *(See: Sustainability.)*
- **Item (STAC Item)** — a STAC object representing a single spatiotemporal “thing” (scene, tile, dataset slice) with assets and metadata. *(See: STAC.)*

### J
- **JSON Schema** — a machine-readable schema used to validate JSON documents (inputs, outputs, configs, contracts). *(See: Schema validation.)*
- **`json_schema_ref`** — front‑matter pointer to a JSON Schema used to validate this doc’s structure or related artifacts. *(Often paired with `shape_schema_ref`.)*
- **JSON-LD** — JSON for Linked Data; used to serialize graph-like semantics and align with W3C vocabularies like DCAT and PROV.

### K
- **Kernel density estimation (KDE)** — technique producing a smooth density surface from point observations; useful for spatial pattern exploration and some map layers. *(See: Raster, Spatial analysis.)*
- **Keyless signing** — signing workflow that uses OIDC identities and short‑lived certs instead of long-lived private keys; commonly associated with Sigstore tooling. *(See: OAuth2/OIDC, Fulcio, Rekor.)*
- **KFM (Kansas Frontier Matrix)** — a geospatial-historical knowledge system with a governed end-to-end pipeline producing interactive maps and provenance-led narratives.
- **KFM-DCAT / KFM-PROV / KFM-STAC profiles** — KFM-specific validation profiles/version targets for DCAT, PROV, and STAC artifacts (schema rules, required fields).
- **KFM-MDP (Markdown protocol)** — KFM’s governed Markdown conventions (front-matter fields, required section structure, fence rules).
- **KFM-ONTO / KFM-OP** — ontology protocol/version labels. Drift note: some domain docs use `KFM-OP v11` where core docs use `KFM-ONTO v4.x`. Treat `KFM-OP` as a legacy alias until a canonical mapping is defined. *(Not confirmed in repo.)*
- **KFM-PPC / KFM-PDC** — pipeline contract/version labels. Drift note: some domain docs use `KFM-PDC v11` where core docs use `KFM-PPC v11.x`. Treat `KFM-PDC` as a legacy alias until a canonical mapping is defined. *(Not confirmed in repo.)*
- **Kriging** — geostatistical interpolation method that uses a variogram/semivariogram model to estimate values across space, often producing both estimates and uncertainty surfaces. *(See: Semivariogram, Uncertainty.)*

### L
- **LangGraph** — referenced workflow/orchestration approach used in some KFM workflow notes (e.g., to coordinate extraction and validation steps). Treat as implementation detail unless standardized. *(Not confirmed in repo.)*
- **Layer registry** — a UI configuration registry that lists available map layers, their sources, and access rules; used to prevent unauthorized or sensitive data exposure.
- **Layout profiles (`layout_profiles`)** — a front‑matter list describing approved layout patterns (e.g., “immediate-one-branch-with-descriptions-and-emojis” for file trees). These are formatting conventions to keep docs consistent and machine-extractable. *(See: `machine_extractable`.)*
- **Ledger** — an event/log record system used to track artifact creation and changes (`event_source_id` links to ledger entries). *(See: Provenance.)*
- **Lifecycle (`lifecycle`)** — descriptive front‑matter label describing expected support horizon (e.g., “Long‑Term Support (LTS)”). *(See: Release stage, Review cycle.)*
- **Lineage** — traceability describing how an artifact was produced from inputs and processes. *(See: PROV-O, Provenance.)*
- **LOD (Level of detail)** — technique to render large datasets efficiently by showing simpler representations at lower zoom levels.

### M
- **Machine-extractable (`machine_extractable`)** — front‑matter boolean indicating the doc is written to be reliably parsed/indexed (stable headings, tables, predictable structure). *(See: `heading_registry`, `layout_profiles`.)*
- **Manifest (`manifest_ref`)** — a versioned release artifact describing what was produced (files, hashes, versions, provenance pointers); used for reproducibility and audit.
- **MapLibre** — open-source web mapping library referenced for 2D map rendering in KFM.
- **MCP (Master Coder Protocol)** — a reproducibility-oriented documentation and workflow discipline: explicit versions, clear methods, repeatable results, and traceable artifacts.
- **MCMC (Markov Chain Monte Carlo)** — a family of sampling algorithms used to approximate posterior distributions in Bayesian models when direct computation is intractable. *(Reference library term; see: Bayesian inference, Uncertainty.)*
- **Metadata** — descriptive data about a dataset/artifact (title, description, license, extents, timestamps, provenance pointers, etc.).
- **Metadata profiles (`metadata_profiles`)** — a front‑matter list of external standards the artifact claims to align with (e.g., `STAC 1.0.0`, `DCAT 3.0`, `PROV-O`). This is a declarative alignment list and should match actual emitted artifacts. *(See: Schema validation.)*
- **Micro-STAC** — an “item-level, scoped STAC” pattern used in some modules to keep catalogs small and auditable while still interoperable. *(If used, ensure Collections/Items remain valid STAC 1.0.)*
- **Migration (Graph)** — a controlled change to the ontology or graph structure that preserves compatibility or upgrades data safely.
- **Moran’s I** — a global spatial autocorrelation statistic measuring whether similar values cluster in space. *(See: Spatial autocorrelation.)*

### N
- **Neo4j** — a graph database used for KFM’s semantic core and relationship queries.
- **NER (Named Entity Recognition)** — extraction technique to identify entities (people, places, organizations) from text. Often used during document processing stages (OCR → NER → human review). *(See: OCR, Evidence artifact.)*
- **Not confirmed in repo** — explicit marker used in KFM docs to flag content that is proposed, missing, or not yet standardized in the repository. Treat as a TODO for maintainers/reviewers, not as a guarantee. *(See: Governance.)*
- **NUMA** — Non‑Uniform Memory Access; a hardware topology concept relevant to high‑performance query/pipeline execution on many‑core systems. *(Reference library term.)*

### O
- **OAuth2/OIDC** — authentication/authorization standards referenced for API/UI security posture; OIDC is often used for “keyless” signing and identity-bound workflows in CI. *(See: RBAC, Keyless signing.)*
- **OCR (Optical Character Recognition)** — converting scanned documents/images into machine-readable text, typically as a precursor to extraction/NER. OCR outputs should be treated as *noisy* and validated against originals when used as evidence. *(See: Evidence artifact.)*
- **OGC** — Open Geospatial Consortium; standards body behind specs like GeoSPARQL.
- **Ontology** — formal definition of entity types, properties, and relationships; used to enforce consistency in the knowledge graph.
- **Ontology alignment (`ontology_alignment`)** — a front‑matter mapping from KFM entities/artifacts to external semantic standards (e.g., CIDOC-CRM classes, GeoSPARQL feature types, PROV-O types).
- **OpenAPI** — a specification for describing REST APIs; used to document and validate REST contracts.
- **OpenAQ** — referenced upstream air-quality data provider/aggregator used in Air Quality domain documentation. *(Domain-specific.)*
- **OpenLineage** — an open standard for data lineage events; referenced as an optional/parallel lineage emission alongside PROV-O.
- **OpenTelemetry** — observability standard for metrics/traces/logs; may be used for API/pipeline telemetry emission. *(See: Telemetry.)*
- **ORAS** — a tool/approach for pushing arbitrary artifacts (including datasets) to OCI registries; referenced for versioned artifact distribution and provenance attachment. *(See: Manifest, Attestation.)*
- **OWL-Time** — W3C ontology for temporal concepts referenced in ontology alignment. *(See: Ontology alignment.)*

### P
- **Parquet** — a columnar storage format commonly used for large analytical datasets; often used in processed outputs.
- **Pipeline contract** — the non‑negotiable ordering and boundary rules that connect ETL → catalogs → graph → APIs → UI → story. *(See: `pipeline_contract_version`, KFM-PPC/KFM-PDC.)*
- **Point-in-polygon** — spatial operation assigning polygon attributes to points that fall within each polygon; used in spatial aggregation workflows. *(See: Spatial join.)*
- **Policy engine (Rego)** — policy-as-code format (often associated with OPA) used to express validation rules (e.g., supply-chain attestation requirements).
- **PostGIS** — PostgreSQL extension providing spatial types and functions; often used in geospatial ETL and spatial querying workflows.
- **`previous_version_hash`** — front‑matter field storing the checksum/hash of the prior version of an artifact. Used to support chain-of-custody across versions. *(See: Version-pinned, Provenance.)*
- **PROV-O (W3C Provenance Ontology)** — W3C ontology for representing provenance (entities, activities, agents, and relationships like “used” or “generated by”).
- **Provenance** — evidence-backed trace showing the origin, inputs, process, and responsible parties for an artifact or claim. In KFM, provenance is required for Focus Mode and Story Nodes.
- **Provenance chain (`provenance_chain`)** — front‑matter or doc section that points to the key lineage artifacts for a domain output (e.g., PROV bundle, run manifest, ledger IDs). *(The exact schema is not confirmed in repo.)*
- **Provenance-linked narrative rule** — rule that every narrative claim must trace to a dataset/record/asset ID and its provenance. *(See: Story Node.)*
- **Public exposure risk (`public_exposure_risk`)** — front‑matter label describing risk level if content is made public (e.g., “Low”, “Medium”, “High”), used to drive review/redaction requirements. *(See: Sensitivity.)*
- **Prompt Gate** — KFM’s concept of an allowlist + policy + logging boundary controlling what AI tools can do, which sources they can access, and how outputs are audited. *(Policy details live in governance docs.)*

### Q
- **Quality signal** — telemetry, tests, or review markers that indicate reliability (e.g., validation pass rates, drift detection results, redaction counts).

### R
- **Raster** — gridded data (e.g., imagery, elevation). Often stored as GeoTIFF/COG.
- **React** — JavaScript UI library used by KFM’s frontend (paired with MapLibre/Cesium) to build interactive map experiences.
- **Redaction** — removing or hiding sensitive information entirely (e.g., omitting coordinates). *(Related: Generalization.)*
- **Redaction required (`redaction_required`)** — front‑matter boolean indicating whether redaction or generalization must be applied before public release, per governance. *(See: Sensitivity, CARE.)*
- **Rekor** — a transparency log (often used with Sigstore) where signatures/attestations can be recorded for auditability. *(See: Sigstore.)*
- **Release stage (`release_stage`)** — front‑matter label describing maturity (e.g., “Stable / Governed”, “Pre‑Operational · Commissioning Phase”).
- **Retention policy** — rules defining how long raw sources, logs, checksums, and audit artifacts are retained (often tracked via a retention config file). *(See: Checksum record.)*
- **Review cycle (`review_cycle`)** — front‑matter label describing how often an artifact is reviewed (e.g., “Semiannual · EO Working Group · FAIR+CARE Council”). *(See: Content stability.)*
- **Reproducibility** — ability to regenerate outputs from inputs with pinned versions/configs and recorded provenance.
- **Required-status check** — a CI job that must pass before merging (enforced via branch protection). *(See: Branch protection, Fail-closed.)*
- **Responsive design** — UI approach that adapts layout/typography/interaction to different screen sizes and input modes; supports a11y and mobile usability. *(See: CSS, Flexbox, WCAG.)*
- **RBAC (Role-Based Access Control)** — authorization model where users/services are granted roles that permit specific actions or data access. *(See: OAuth2/OIDC.)*
- **Risk category (`risk_category`)** — front‑matter label describing risk tier (often domain-dependent). Must align to governance review expectations. *(See: `public_exposure_risk`, `sensitivity`.)*

### S
- **SBOM (`sbom_ref`)** — Software Bill of Materials reference to an inventory of components/dependencies for a release; commonly stored as SPDX JSON in KFM release folders.
- **Schema drift** — a breaking or unexpected change in schemas/fields/structures; should be caught by schema validation and contract tests.
- **Schema validation** — automated checks that JSON/JSON-LD artifacts conform to required schemas/profiles (e.g., STAC/DCAT/PROV).
- **Scope (`scope`)** — front‑matter block defining what domain/system a doc applies to (commonly includes `domain` and an `applies_to` list). Used to prevent “floating governance” that applies to everything. *(See: Domain pack.)*
- **Semantic document ID (`semantic_document_id`)** — human-readable/stable identifier used across systems and tooling (distinct from `doc_uuid`, but often versioned similarly).
- **Semantic intent (`semantic_intent`)** — front‑matter list describing the semantic purpose of an artifact (e.g., `api-governance`, `metadata-standardization`). Prefer controlled vocabulary values where available. *(Not confirmed in repo.)*
- **Sensitivity (`sensitivity`)** — a label indicating potential harm if details are disclosed (e.g., protected sites). Sensitivity may require generalization or redaction.
- **Sensitivity level (`sensitivity_level`)** — front‑matter severity tier (e.g., `None`, `Dataset-dependent`). Use alongside `public_exposure_risk` for review triage. *(Taxonomy is not confirmed in repo.)*
- **Semivariogram / variogram** — model of spatial variance vs distance used in kriging/interpolation workflows. *(See: Kriging.)*
- **SHACL (`shape_schema_ref`)** — Shapes Constraint Language; W3C standard used to express constraints over RDF graphs (used for ontology/metadata validation when adopted).
- **`shape_schema_ref`** — front‑matter pointer to a SHACL/shape file used to validate this doc or related RDF artifacts. *(Often paired with `json_schema_ref`.)*
- **Signature (`signature_ref`)** — a cryptographic signature file for a release or artifact; used with SBOM/manifest/attestations to verify integrity.
- **Sigstore** — open tooling/ecosystem for keyless signing and transparency logs (commonly includes Fulcio + Rekor + Cosign workflows). *(See: Keyless signing.)*
- **SLSA (Supply-chain Levels for Software Artifacts)** — a framework for supply-chain integrity; referenced for provenance verification (e.g., “SLSA Level 3”).
- **Spatial autocorrelation** — statistic describing how similarity of values relates to spatial proximity (global: Moran’s I; local: Getis–Ord, etc.).
- **Spatial join** — operation combining attributes of two spatial datasets based on spatial relationships (within, intersects, etc.). *(See: Point-in-polygon.)*
- **Spectral graph theory** — analysis of graphs using eigenvalues/eigenvectors (often of the graph Laplacian); useful for community structure, diffusion, and graph embeddings in advanced analytics. *(Reference library term.)*
- **SPDX** — a standard format for SBOMs; referenced in KFM as `sbom.spdx.json`.
- **STAC (SpatioTemporal Asset Catalog)** — open specification for describing geospatial assets and collections using JSON. KFM uses STAC Collections/Items to package and discover processed assets.
- **STAC Collection** — a STAC object that groups items and defines shared metadata and spatial/temporal extents.
- **STAC Item** — a single catalog entry within a collection representing one spatiotemporal unit with assets.
- **STAC Asset** — a link/descriptor to an actual file/resource (raster, vector, document, thumbnail) within an item.
- **Status (`status`)** — front‑matter lifecycle state for a document/artifact (e.g., `draft`, `Active / Enforced`). This is not the same as `release_stage` (maturity). *(See: Deprecation.)*
- **Story Node** — a versioned narrative artifact (structured markdown) that is machine-ingestible, linked to graph entities/datasets, and required to cite every factual claim. Story Nodes feed Focus Mode narratives.
- **Sunset policy (`sunset_policy`)** — front‑matter field describing when/how an artifact is superseded or retired (e.g., “Superseded upon next domain update”). This is not a deletion instruction by itself. *(See: Deprecation.)*
- **Sustainability** — in KFM docs, includes energy and carbon telemetry tracking aligned to relevant standards where applicable. *(See: Energy telemetry, Carbon telemetry.)*

### T
- **Telemetry (`telemetry_ref`, `telemetry_schema`)** — logging and metrics collected to observe performance, security, and governance compliance; stored with schema pointers when governed.
- **Test profiles (`test_profiles`)** — a front‑matter list naming which validations a doc/artifact expects (e.g., `markdown-lint`, `schema-lint`, `pii-scan`). Actual enforcement depends on CI. *(See: Validation gate.)*
- **Tiling** — partitioning large spatial datasets into smaller pieces for fast rendering and retrieval (often used with WebGL maps).
- **Transform registry (`transform_registry`)** — optional front‑matter block enumerating allowed vs prohibited AI transforms, typically mirroring `ai_transform_permissions` / `ai_transform_prohibited`. Used to make AI constraints machine-checkable. *(See: Prompt Gate.)*
- **TTL policy (`ttl_policy`)** — a front‑matter key describing how long an artifact is considered valid before review/expiration. *(Do not treat as deletion authority; governance rules apply.)*
- **TypeScript** — typed superset of JavaScript commonly used for web apps to improve correctness and maintainability; often used in React codebases.
- **Time slider** — UI control to filter layers and context by time.

### U
- **Uncertainty** — quantitative/qualitative indicator for confidence in model outputs or inferred claims. In KFM, AI-derived insights must be labeled and opt-in.
- **User overlay** — a user-provided dataset (e.g., custom GeoJSON, scanned map) ingested via a controlled ETL mechanism, typically sandboxed/unverified until reviewed.

### V
- **Validation gate** — a mandatory check in CI/CD (schemas, tests, docs lint, policy checks) that must pass before changes are accepted.
- **Verification & Validation (V&V / VV&A)** — modeling discipline: *verification* checks the implementation matches the intended model; *validation* checks the model matches reality for its intended use; *accreditation* is formal acceptance for a use case. *(Reference library term; see: Reproducibility, Uncertainty.)*
- **Version-pinned** — immutability posture where published artifacts are tied to an explicit version and not changed in place; updates create new versions. *(See: Immutability status.)*
- **Viewport** — the current visible map extent/zoom used to filter data requests and render decisions.

### W
- **W3C** — World Wide Web Consortium; standards body behind DCAT, PROV-O, OWL-Time, and related vocabularies.
- **WCAG (Web Content Accessibility Guidelines)** — accessibility standard referenced in KFM docs (often “WCAG 2.1 AA/AA+”) as a compliance target for UI/docs.
- **WDE (World Discovery Engine)** — a referenced innovation/extension concept; in KFM context, WDE-related work typically implies new data products, graph entities, API extensions, and validation.
- **WebGL** — browser graphics API used for high-performance map rendering.
- **Windowed operation** — stream processing pattern where computations occur over time/record windows (common in streaming aggregations); relevant for scalable pipeline designs. *(Reference library term.)*
- **WKT (Well-Known Text)** — text format for geometries; commonly used in semantic/GeoSPARQL contexts.
- **Workflow** — a defined set of pipeline steps (ETL, catalog build, graph import, API deploy) executed reproducibly and recorded in provenance.

### Y
- **YAML front-matter** — the metadata block at the top of governed Markdown documents containing versioning, provenance refs, governance refs, and AI permissions.

### Z
- **Zoom level** — map scale index controlling what data is shown; affects tiling, LOD, and rendering decisions.

## 🗺️ Diagrams
- Not required for this glossary. *(If future work adds term-dependency diagrams, place them here and list `diagram_profiles` if used.)*

## 📦 Data & Metadata
- This document is a definitions catalog; it does not directly introduce new datasets.
- When adding a new dataset, ensure any new terminology or acronyms are added here.
- When adding new front‑matter keys in a governed template, add them to this glossary (or the relevant standards doc, if present).

## 🌐 STAC, DCAT & PROV Alignment
- This glossary supports consistent interpretation of STAC/DCAT/PROV artifacts but does not contain STAC/DCAT/PROV payloads itself.

## 🧱 Architecture
- The glossary is a **documentation-layer control surface**: it standardizes language across ETL, catalogs, graph, APIs, UI, and narrative outputs.
- It does not define policy or implement enforcement. Enforcement belongs to:
  - Governance docs referenced in front‑matter,
  - Schemas/contracts (JSON Schema, SHACL, OpenAPI),
  - CI workflows and required-status checks.

## 🧠 Story Node & Focus Mode Integration
- Story Nodes and Focus Mode should link to this glossary for shared terminology.
- When writing Story Nodes, prefer terms defined here, especially for governance (sensitivity/redaction) and provenance (PROV-O) language.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Link check to referenced docs (as implemented in CI)
- [ ] Schema validation (STAC/DCAT/PROV; plus JSON/SHACL schemas where applicable)
- [ ] Graph integrity checks (migrations/constraints where applicable)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI schema checks (layer registry)
- [ ] Security / supply-chain checks (SBOM/signature/attestation verification) where applicable
- [ ] Sovereignty/sensitivity checks for any content that could expose protected locations

### Reproduction
~~~bash
# (Repo-specific commands may differ.)
# markdownlint docs/glossary.md
# linkcheck docs/glossary.md
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If a term impacts governance (e.g., sensitivity categories, redaction rules), it should be reviewed by the governance owners referenced in front‑matter.

### CARE / sovereignty considerations
- Ensure terms related to Indigenous data governance remain aligned to the sovereignty policy.
- Do not include sensitive site examples or specific protected coordinates in definitions.

### AI usage constraints
- This glossary can be summarized or indexed, but must not be used to invent policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial glossary: core pipeline, cataloging, graph, API/UI, governance terms. | Bartytime |
| v1.1.0 | 2025-12-24 | Expanded glossary: front‑matter metadata keys, supply‑chain/telemetry terms, lifecycle registry, and architecture drift notes. | Bartytime |
| v1.2.0 | 2025-12-27 | Aligned glossary to universal doc conventions; added front‑matter registry keys and domain artifact terminology; clarified known drift (paths + protocol aliases). | Bartytime |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
