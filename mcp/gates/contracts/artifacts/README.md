# 🧱 MCP · Gates → Contracts → Artifacts  
<sub>📍 Path: `mcp/gates/contracts/artifacts/README.md` · ✅ Contract-first · 🚦 Fail-closed · 📦 Evidence-first</sub>

![Policy](https://img.shields.io/badge/Policy-OPA%20%2B%20Conftest-2b6cb0)
![Contracts](https://img.shields.io/badge/Contracts-STAC%20%7C%20DCAT%20%7C%20PROV-2f855a)
![Artifacts](https://img.shields.io/badge/Artifacts-OCI%20%2B%20Cosign-6b46c1)
![Pipeline](https://img.shields.io/badge/CI-Detect%20%E2%86%92%20Validate%20%E2%86%92%20Promote-4a5568)
![UI](https://img.shields.io/badge/UI-MapLibre%20%2B%20Cesium-0ea5e9)

> [!NOTE]
> This README defines **how KFM’s “Master Coder Protocol (MCP)” layer** turns rules into reality:
> **Contracts define truth → Gates enforce truth → Artifacts package truth.**  
> If a thing can’t pass its gates, it **does not ship** (fail-closed).

---

## 🧭 Table of Contents
- [What this folder is](#-what-this-folder-is)
- [MCP in one minute](#-mcp-in-one-minute)
- [Core principles](#-core-principles)
- [🚦 Gates](#-gates)
- [📜 Contracts](#-contracts)
- [📦 Artifacts](#-artifacts)
- [🧬 Evidence-first: STAC + DCAT + PROV](#-evidence-first-stac--dcat--prov)
- [🧩 Subsystem contract matrix](#-subsystem-contract-matrix)
- [✅ Definition of Done](#-definition-of-done)
- [🛠️ How-to recipes](#️-how-to-recipes)
- [🔐 Security, privacy, sovereignty](#-security-privacy-sovereignty)
- [🧠 Story Nodes + Focus Mode hard gates](#-story-nodes--focus-mode-hard-gates)
- [📚 Source docs used](#-source-docs-used)
- [Appendix: templates](#appendix-templates)

---

## 📦 What this folder is

This directory is the **governed “shape + rules + proof” nucleus** for KFM’s pipeline outputs:

- **Gates** = automated “quality & ethics inspectors” that run in CI and runtime  
- **Contracts** = versioned schemas/specs for data, metadata, APIs, graph, UI, and narratives  
- **Artifacts** = the versioned, verifiable output packages (data, tiles, models, stories, reports)

> [!IMPORTANT]
> **Contract-first** means “schemas and API contracts are first-class artifacts.”  
> Any change to them triggers strict versioning + compatibility checks.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧠 MCP in one minute

In KFM context, **MCP** is a *documentation + reproducibility protocol* that standardizes how we:
- document datasets, pipelines, and models (datasheets/model cards),
- enforce CI discipline (tests + checks),
- keep outputs deterministic and auditable.  [oai_citation:1‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:2‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

KFM then operationalizes MCP via:
- **Policy-as-code (OPA/Rego)** validated by **Conftest** in CI,  [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- a **Detect → Validate → Promote** CI pattern,  [oai_citation:4‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **fail-closed gates**: if conditions aren’t met, it doesn’t merge/publish.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:6‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧱 Core principles

### 1) ✅ Fail-closed by default
If a contract requirement is missing, **the gate stays closed** and the change is blocked.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 2) 🧾 Evidence-first (not vibes-first)
KFM’s UI and AI features must always surface the “map behind the map”:
- layers include source attributions,
- AI answers come with citations,
- exports carry proper credits.  [oai_citation:9‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### 3) 🔁 Deterministic & replayable pipelines
ETL jobs should be **idempotent, config-driven, fully logged**, producing stable outputs for given inputs.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) 🧬 End-to-end provenance
KFM maps dev-ops events (PRs) and data transformations into PROV, enabling traceability like:
“Which PR produced this dataset and who reviewed it?”  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🚦 Gates

### What is a “gate”?
A **gate** is an automated check that must pass before:
- ingestion continues,
- a PR can merge,
- a dataset/layer can publish,
- AI can respond (Focus Mode hard gate).

Gates exist in two main forms:
- **CI gates** (Conftest + Rego, schema validators, secret scanners, linting)
- **Runtime gates** (API-level authorization/redaction rules, prompt gates, output validators)

### Minimum gates (v13 baseline)
KFM’s minimum set of automated policy gates includes checks for:  
- **schema validation**  
- **STAC/DCAT/PROV completeness** (required metadata)  
- **license presence** (no data without known license)  
- **sensitivity classification** (and correct handling if sensitive)  
- **provenance completeness** (inputs + processing steps declared)  
- **Focus Mode citations required** (otherwise refuse)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

> [!TIP]
> Implement gates **both** in code (validation libraries in pipeline) and in CI (Conftest on PRs).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Gate naming (recommended)
Use stable IDs to make violations searchable and auditable:
- `GATE-SCHEMA-###`
- `GATE-METADATA-###`
- `GATE-LICENSE-###`
- `GATE-SENS-###`
- `GATE-PROV-###`
- `GATE-AI-CITATIONS-###`

Example policy error pattern:
- `KFM-PROV-001: Processed data changed without matching PROV update.`  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 📜 Contracts

A **contract** is the canonical spec for what “valid” means. Contracts can be:

### 🗺️ Data + metadata contracts
- Schema rules for tables/GeoParquet/CSV/JSON
- **KFM STAC / DCAT / PROV profiles** (alignment policy required)  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- CRS/geometry constraints (valid polygons, expected coordinate ranges, etc.)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 🧠 Graph contracts
- Ontologies, node/edge schemas, stable identifiers  
- (Neo4j/graph ingestion must preserve compatibility)  [oai_citation:17‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 🌐 API contracts
- OpenAPI specs / GraphQL schemas
- Contract tests + redaction rules if data is sensitive  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧩 UI contracts
- Layer registry entries must tie back to provenance (DCAT/STAC)
- Sensitive coordinates may need hiding/aggregation (CARE rules)  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 📖 Story + narrative contracts
Story Nodes are treated as governed, machine-ingestible narrative data:
- every factual claim has citations
- stories reference graph entity IDs
- fact vs interpretation is explicit  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📦 Artifacts

### What is an artifact?
An **artifact** is a deliverable output that is:
- **versioned**
- **digest-addressable** (hashable/immutable by content)
- **contract-linked**
- **provenance-linked**
- (optionally) **signed** and stored in an OCI registry

### Artifact categories (KFM-friendly)
| Category | Examples | Consumed by |
|---|---|---|
| 🗺️ Geo data | GeoParquet, COG, GeoJSON | analytics, catalog, graph |
| 🧱 Tiles | PMTiles (vector tiles), 3D tiles | UI (MapLibre/Cesium), offline packs |
| 📚 Catalog + provenance | STAC, DCAT, PROV JSON-LD | UI “map behind map”, Focus Mode, audits |
| 🧠 Models | model files, model cards, metrics | Focus Mode, pipelines |
| 📖 Narrative | Story Nodes + evidence manifests | Story Viewer, Focus Mode |
| 🧾 Audit logs | run manifests, validation reports | governance, reproducibility |

### OCI artifact distribution (recommended for durable releases)
KFM treats data artifacts like container images:
- stored in an OCI registry,
- referenced by tag and immutable digest,
- verified before use.  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**Cosign signatures** (Sigstore) attach cryptographic signatures as OCI referrers.  [oai_citation:22‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Run manifests (the reproducibility ledger)
KFM describes a run manifest that captures:
- source URLs
- tool versions
- summary counts
- errors
- stored at `data/audits/<run_id>/run_manifest.json`  [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

It also uses:
- RFC 8785 JSON canonicalization
- a “self-fingerprinting” digest inserted into `canonical_digest`
- idempotency keys to avoid repeating identical operations  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧬 Evidence-first: STAC + DCAT + PROV

KFM’s evidence alignment policy expects:
- **STAC**: geospatial assets + extents
- **DCAT**: dataset discovery/distribution/ownership
- **PROV**: lineage (entities, activities, agents)

This cross-layer linkage is **required** in v13 guidance.  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> [!IMPORTANT]
> The UI is designed to maintain trust: every visualization is linked to source data and metadata (“the map behind the map”).  [oai_citation:27‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🧩 Subsystem contract matrix

The Master Guide pattern explicitly treats subsystem artifacts and invariants as first-class.  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

| Subsystem | Contract “source of truth” | Must produce artifacts | Key invariants |
|---|---|---|---|
| ETL / intake | pipeline configs + schemas | run manifests, validation reports | deterministic, replayable, logged  [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| Catalog | STAC/DCAT/PROV profiles | collections/datasets/prov bundles | no dataset without complete metadata  [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| Graph | ontology + node schemas | graph snapshots, migration logs | stable IDs, compatible schema evolution  [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| API | OpenAPI/GraphQL | contract tests, redaction rules | backward compatibility, authn/authz  [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| UI | layer registry + UI config | layer cards, legends, provenance links | provenance surfaced; CARE safe display  [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:34‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) |
| Story/Focus | Story Node template + rules | Story Nodes + evidence manifests | citations required; fact vs interpretation  [oai_citation:35‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |

---

## ✅ Definition of Done

### ✅ DoD for a new *artifact* (dataset / tiles / story / model)
- [ ] Data files produced in approved format(s) (ex: **GeoParquet + PMTiles** dual-pack when relevant)  [oai_citation:36‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- [ ] Contract validation passes (schema + domain rules)
- [ ] STAC + DCAT + PROV complete and linked  [oai_citation:37‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] License present and approved (SPDX allowlist if used)  [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] Sensitivity classification present (+ correct handling)  [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Run manifest generated + canonical digest computed  [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] (If released via OCI) artifact is digest-pinned + cosign-signed  [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] Gates pass in CI (fail-closed)  [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### ✅ DoD for a new *contract*
- [ ] Contract is versioned (semver) and documented
- [ ] Examples included (valid + invalid)
- [ ] Compatibility rules stated (breaking vs non-breaking)
- [ ] Gate updated/added to enforce contract

### ✅ DoD for a new *gate*
- [ ] Gate has stable ID + readable failure message
- [ ] Gate runs in CI (and runtime if applicable)
- [ ] Tests exist for pass/fail cases
- [ ] Fail-closed behavior confirmed  [oai_citation:43‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> [!TIP]
> KFM documentation culture encourages templates + checklists (“Definition of Done”) as part of governance and review discipline.  [oai_citation:44‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## 🛠️ How-to recipes

### 1) Add a new dataset artifact (end-to-end)
1. **Ingest raw** into the system of record (often PostGIS) and track source + checksums.  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
2. **Transform** to publishable formats:
   - analytics format (e.g., GeoParquet)
   - visualization format (e.g., PMTiles / COG)  [oai_citation:46‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
3. **Emit evidence metadata**:
   - STAC collection + items
   - DCAT dataset + distributions
   - PROV activity/entity/agent chain  [oai_citation:48‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
4. **Generate run manifest** under `data/audits/<run_id>/...` and compute canonical digest.  [oai_citation:49‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
5. **Run gates** (CI + local) and fix violations until green.  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
6. **Publish**:
   - commit metadata + small artifacts to repo
   - optionally push big artifacts to OCI + cosign sign  [oai_citation:51‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 2) Add a new API endpoint (contract-first)
1. Update OpenAPI/GraphQL contract first  
2. Implement server controller/resolver  
3. Add contract tests + redaction rules if sensitive  [oai_citation:52‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

### 3) Add a new UI layer (provenance required)
1. Add layer to layer registry / config  
2. Ensure the UI can show:
   - source attribution (DCAT/STAC)
   - legend/info panel
   - any CARE-driven redaction rules  [oai_citation:53‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  

---

## 🔐 Security, privacy, sovereignty

### 🧷 Supply chain & auditability
KFM adopts supply chain best practices:
- SBOMs + SLSA-style attestations (planned)  [oai_citation:54‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Sigstore/Cosign signing for artifacts  [oai_citation:56‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Secrets policy: no creds in code; rotate/audit keys  [oai_citation:57‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  

### 🧭 FAIR + CARE + governance triggers
Governance rules based on FAIR/CARE are codified into tooling; planners/executors should refuse actions that would expose sensitive locations (e.g., sacred sites).  [oai_citation:58‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 🕵️ Privacy-preserving analytics (when sensitivity is “not public”)
Data mining research patterns highlight:
- **inference control**
- **query auditing**
- **differential privacy** (where appropriate)
to prevent sensitive leakage from query results.  [oai_citation:59‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:60‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🧠 Story Nodes + Focus Mode hard gates

### Story Nodes are governed data
A valid Story Node must:
- include provenance/citations for every claim
- reference graph entities via stable IDs
- distinguish fact vs interpretation  [oai_citation:61‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Focus Mode is a hard gate
Focus Mode (AI) must include citations; if it can’t, it refuses.  [oai_citation:62‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:63‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

> [!NOTE]
> Evidence manifests can link Story Nodes to datasets through PROV edges, enabling “which stories used this dataset?” queries and impact analysis when data changes.  [oai_citation:64‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📚 Source docs used

### Core KFM design & architecture
- KFM Comprehensive UI System Overview  [oai_citation:65‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:66‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- KFM Data Intake – Technical & Design Guide  [oai_citation:67‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:68‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:69‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- KFM AI System Overview 🧭🤖  [oai_citation:70‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- KFM Comprehensive Architecture, Features, and Design  [oai_citation:71‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:72‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- KFM Comprehensive Technical Documentation  [oai_citation:73‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Innovative Concepts to Evolve KFM  [oai_citation:74‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 🌟 Latest Ideas & Future Proposals  [oai_citation:75‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:76‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- Additional Project Ideas  [oai_citation:77‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:78‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Document Refinement Request  [oai_citation:79‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### MCP / documentation & protocol references
- Master Guide v13 draft (contracts, gates, story rules)  [oai_citation:80‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Scientific Method / Master Coder Protocol doc (reproducibility + QA)  [oai_citation:81‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:82‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- Comprehensive Markdown guide (templates, DoD patterns)  [oai_citation:83‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  

### Research libraries (PDF portfolios)
> [!TIP]
> These are PDF portfolios containing multiple embedded references (open in a portfolio-capable PDF reader).
- AI Concepts & more (portfolio)  [oai_citation:84‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- Data Management / Data Science / Bayesian / Architectures (portfolio)  [oai_citation:85‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- Maps / Google Maps / Virtual Worlds / WebGL (portfolio)  [oai_citation:86‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- Various programming languages & resources (portfolio)  [oai_citation:87‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  

---

## Appendix: templates

### A) Artifact manifest (proposed)
```yaml
artifact_id: "kfm.ks.surficial_geology.v1.2.0"
artifact_kind: "dataset"
version: "1.2.0"

contracts:
  - id: "kfm.stac.profile"
    version: "v1"
  - id: "kfm.dcat.profile"
    version: "v1"
  - id: "kfm.prov.profile"
    version: "v1"

distributions:
  - role: "analytics"
    path: "data/processed/surficial_geology/surficial_geology.geo.parquet"
    media_type: "application/vnd.apache.parquet"
    sha256: "..."
  - role: "viz"
    path: "data/tiles/surficial_geology/surficial_geology.pmtiles"
    media_type: "application/vnd.pmtiles"
    sha256: "..."

metadata_refs:
  stac_collection: "catalog/stac/collections/surficial_geology.json"
  dcat_dataset: "catalog/dcat/datasets/surficial_geology.json"
  prov_activity: "provenance/prov/activities/run_2026-01-22T00-00-00Z.jsonld"

governance:
  license: "CC-BY-4.0"
  sensitivity: "public"   # or restricted / sensitive
  care_label: "Public"

integrity:
  run_manifest: "data/audits/<run_id>/run_manifest.json"
  canonical_digest: "sha256:..."

security:
  oci_ref: "oci://ghcr.io/<org>/kfm/surficial_geology@sha256:..."
  cosign_required: true
```

### B) Run manifest (skeleton)
```json
{
  "run_id": "2026-01-22T00:00:00Z__surficial_geology__build",
  "source_urls": ["..."],
  "tool_versions": {
    "python": "3.x",
    "gdal": "x.y",
    "tippecanoe": "x.y"
  },
  "summary_counts": {
    "records_in": 0,
    "records_out": 0,
    "errors": 0
  },
  "canonical_digest": "sha256:..."
}
```

### C) Gate checklist (minimum)
- schema validation
- STAC/DCAT/PROV completeness
- license present
- sensitivity classification present
- provenance complete
- Focus Mode citations (hard gate)
