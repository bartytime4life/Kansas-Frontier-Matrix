---
title: "KFM Markdown Work Protocol"
path: "docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md"
version: "v1.1.0-draft"
last_updated: "2026-01-12"
status: "draft"
doc_kind: "Standard"
license: "CC-BY-4.0"

owners:
  - "KFM Maintainers"
reviewers:
  - "KFM Governance"
  - "Docs/Story Reviewers"
  - "Security Reviewers (as needed)"

markdown_protocol_version: "KFM-MARKDOWN v13.0.0"
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

doc_uuid: "urn:kfm:doc:standards:markdown-work-protocol:v1.1.0-draft"
semantic_document_id: "kfm-standards-markdown-work-protocol-v1.1.0-draft"
event_source_id: "ledger:kfm:doc:standards:markdown-work-protocol:v1.1.0-draft"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
  - "fabricate_sources"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Markdown Work Protocol 🧾🧭

![Standard](https://img.shields.io/badge/standard-KFM-1f6feb)
![Template-first](https://img.shields.io/badge/template--first-required-0aa3a3)
![Evidence-first](https://img.shields.io/badge/evidence--first-STAC%20%2B%20DCAT%20%2B%20PROV-0aa3a3)
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API%20contracts-0aa3a3)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043)
![Security](https://img.shields.io/badge/security-no%20secrets%20%2B%20no%20side--channels-red)

> Canonical rules for authoring governed Markdown in KFM.  
> The goal is **reviewable meaning**, **citable claims**, and **reversible change** — without doc drift. 🧠🗺️

> [!IMPORTANT]
> **KFM’s non‑negotiable ordering (docs must reinforce it):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> If a doc encourages bypassing the ordering (even as a “temporary shortcut”), it’s wrong.

> [!NOTE]
> **Acronym collision warning:** KFM uses **KFM‑MDP** elsewhere to mean *Managed Data Promotion* (data release gating).  
> This document governs Markdown authoring and uses **KFM‑MARKDOWN** as the documentation protocol tag to avoid confusion.

---

## 🔗 Quick links
- 🧭 Docs home: `docs/README.md`
- 📘 Canonical system map: `docs/MASTER_GUIDE_v13.md`
- 🧰 Templates: `docs/templates/`
- 📏 Standards registry: `docs/standards/`
- 🧾 Governance: `docs/governance/`
- 🧪 MCP receipts (runs/experiments): `mcp/` *(if present)*
- 📚 Reference library: `docs/library/` *(recommended home; license-aware)*

---

## 🧭 Quick navigation
- [📘 Overview](#-overview)
- [🗂️ Directory Layout](#️-directory-layout)
- [🧭 Context](#-context)
- [🗺️ Diagrams](#️-diagrams)
- [📦 Data & Metadata](#-data--metadata)
- [🌐 STAC, DCAT & PROV Alignment](#-stac-dcat--prov-alignment)
- [🧱 Architecture](#-architecture)
- [🧠 Story Node & Focus Mode Integration](#-story-node--focus-mode-integration)
- [🧪 Validation & CI/CD](#-validation--cicd)
- [⚖ FAIR+CARE & Governance](#-faircare--governance)
- [📚 Project reference library influence map](#-project-reference-library-influence-map)
- [🕰️ Version History](#️-version-history)

---

## 📘 Overview

### Purpose ✅
This standard defines the **mandatory** workflow and constraints for producing Markdown documentation in the Kansas Frontier Matrix (KFM) repository, ensuring documentation is:

- **Template-first** 🧰 (every doc conforms to *exactly one* governed template)
- **Architecture-synced** 🧱 (preserves the canonical pipeline + API boundary)
- **Repo-grounded** 🧾 (no invented repo facts/policies; label uncertainty)
- **Evidence-first** 🔎 (claims point to STAC/DCAT/PROV + stable IDs)
- **Contract-first** 📐 (schemas + API contracts are first-class artifacts)
- **CI-clean** ✅ (assume strict lint/link/schema/sensitivity gates)
- **Human-centered** ❤️ (transparent impacts; no “mystery meaning”)
- **Security-safe** 🔒 (no secrets; no sensitive location leakage)

### Scope 🎯

| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Any Markdown authored under `docs/**` (standards, guides, design docs, reports, story nodes) | Implementing code changes in `src/**`, schema changes in `schemas/**`, or actually running pipelines |
| Template-driven governed docs (`docs/templates/**`) | Claiming executed ETL runs, infra changes, or deployments without evidence (run IDs, artifacts, logs) |
| Docs that describe API contracts (REST/GraphQL) | Introducing new governance/policy beyond what’s defined in governed docs |
| Adding/updating reference library material (license-aware) | Copying proprietary/uncleared content into public repo paths |

> [!TIP]
> READMEs outside `docs/` (e.g., `src/**/README.md`) should follow a “lite” version of this protocol:
> clear scope, stable links, no invented facts, and no secrets.

### Audience 👥
- Primary: Contributors authoring or updating Markdown under `docs/**`
- Secondary: Reviewers, maintainers, and anyone producing LLM-assisted drafts

### Definitions 🧠
- **Governed document**: Markdown with YAML front-matter + declared scope, constraints, validation intent, and governance posture.
- **Template-first**: every doc conforms to **exactly one** governed template (Universal / Story Node / API Contract Extension).
- **Evidence-first**: every factual claim can be traced to **cataloged evidence** (STAC/DCAT/PROV) or a stable repo artifact (schema, commit, run receipt).
- **Contract-first**: API contracts + schemas define behavior first; docs must link to and respect them.
- **Repo-grounded**: if a statement can’t be verified in repo artifacts, mark it as **hypothesis** or **proposal**.

> Glossary link (expected): `docs/glossary.md` *(create if absent; link from Master Guide)*

### Key artifacts (what this protocol points to) 🧷

| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v13.md` | Canonical ordering + “one subsystem home” rules |
| Master Guide (previous) | `docs/MASTER_GUIDE_v12.md` | Keep for traceability; don’t treat as canonical |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default for most docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Required for Focus Mode narratives |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Required for endpoint/contract changes |
| This protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Governs Markdown contributions |
| STAC/DCAT/PROV profiles | `docs/standards/KFM_*_PROFILE.md` | Normative metadata expectations |

### Definition of done ✅
- [ ] Correct template selected and applied (exactly one)
- [ ] Pipeline ordering and API boundary preserved
- [ ] File placed in correct area (data vs docs vs src vs schemas)
- [ ] Claims are sourced to datasets/doc IDs (or clearly marked inference/hypothesis)
- [ ] Validation steps listed and repeatable
- [ ] No secrets, credentials, internal endpoints, or sensitive location inference
- [ ] Accessibility basics (headings, alt text, descriptive links) met
- [ ] Version history + `last_updated` updated appropriately

---

## 🗂️ Directory Layout

### This document 📄
- `path`: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`

### Related repository paths 🧭

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Standards | `docs/standards/` | Normative rules + conventions |
| Templates | `docs/templates/` | Governed templates (Universal / Story / API) |
| Architecture | `docs/architecture/` | ADRs, blueprints, diagrams |
| Governance | `docs/governance/` | Review gates, ethics, sovereignty |
| Security | `docs/security/` | Threat model, incident response |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` | Staged datasets (raw → intermediate → publishable) |
| Catalog outputs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | Boundary artifacts (required before publish) |
| Graph | `src/graph/` | Ontology bindings, graph build, migrations |
| Pipelines | `src/pipelines/` | ETL and build pipelines (idempotent, logged) |
| APIs | `src/server/` *(or repo equivalent)* | Contracted access layer (redaction/classification) |
| UI | `web/` | React/Map clients (API-only) |
| Evidence receipts | `mcp/` | Runs, experiments, method logs *(if present)* |
| Schemas | `schemas/` | JSON Schema / OpenAPI / ontology schema registries |

### Expected file tree (sub-area) 🌲
~~~text
📁 docs/
├── 📁 standards/
│   ├── 📄 README.md
│   └── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md   # you are here ✅
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
└── 📄 MASTER_GUIDE_v13.md                 # canonical system map 🧭
~~~

---

## 🧭 Context

### Background 🌾
KFM documentation is a **system boundary** and a **meaning boundary**:
- it constrains how data, metadata, graph semantics, APIs, UI, and narratives evolve together
- it prevents “doc drift” (where prose diverges from actual contracts/evidence)
- it protects trust in Focus Mode (where users experience story + map + timeline)

### Non-negotiable invariants 🧱
- **Canonical pipeline is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- **API boundary:** UI consumes contracted APIs; UI must not query graph directly
- **No invented repo facts:** if not verifiable, label as **proposal**/**hypothesis** and point to next safe step
- **No claims of actions not performed:** never claim code ran, infra changed, or deploy happened without receipts
- **One canonical home per concept:** link to the canonical doc; don’t create shadow-doc duplicates

### Required authoring workflow (human or tool-assisted) 🧰
1. **Select exactly one template**
   - Story Node / Focus Mode narrative → `docs/templates/TEMPLATE__STORY_NODE_V3.md`
   - API/endpoint/contract change → `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
   - Everything else → `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
2. **Declare impacted pipeline stage(s)**: ETL / Catalog / Graph / API / UI / Story / Focus
3. **Set governance posture in front-matter**: `sensitivity`, `classification`, `jurisdiction`, `care_label`
4. **List file paths** to create/modify (and ensure correct placement)
5. **Provide commit-ready Markdown** (no “TODO prose” unless clearly marked)
6. **List validation intent** (what should be checked locally/CI)
7. **Put notes/assumptions/next steps in explicit sections** (don’t bury them)

### Doc types → template mapping 🧩
| Doc kind | Typical path | Template |
|---|---|---|
| Standard | `docs/standards/**` | Universal Doc *(unless API contract extension)* |
| ADR | `docs/architecture/ADR/**` | ADR template *(if present; otherwise Universal Doc)* |
| Runbook | `docs/runbooks/**` | Universal Doc |
| Domain module | `docs/data/<domain>/README.md` | Domain README template *(or Universal Doc)* |
| Story Node | `docs/reports/story_nodes/**` | Story Node template |
| API contract note | `docs/**` + `src/server/**` | API contract extension template |

### Markdown writing rules (normative) ✍️
**Structure**
- Use exactly **one H1** (`#`) per document.
- Headings must be hierarchical: H2 (`##`) → H3 (`###`) → H4 (`####`).
- Prefer scannability: short sections, tables for structured info, checklists for DoD.

**Links**
- Prefer **relative links** inside the repo.
- Avoid naked URLs in prose; use descriptive link text.
- Do not link to private/internal endpoints.

**Citations**
- Prefer **system-native pointers**: STAC/DCAT/PROV IDs + stable graph IDs.
- External sources are allowed only if they are also represented in catalogs or `docs/library/` (license-aware).

**Tone**
- Separate **facts** from **interpretation**.
- Avoid absolutist claims unless backed by evidence and a contract.

**Accessibility**
- Images must include alt text.
- Link text must be descriptive (avoid “click here”).
- Avoid using emoji as the only indicator of severity.

### Fences & rendering rules 🧱
- Use `~~~` fences for code blocks and diagrams in repo files (prevents nested-fence pain in chat tooling).
- Use `~~~mermaid` for Mermaid diagrams.
- Keep Mermaid diagrams free of secrets, internal hostnames, or sensitive coordinates.
- Use HTML sparingly; `<details>`/`<summary>` is allowed for collapsible sections.

### Versioning + lifecycle rules (normative) 🕰️
- Standards and templates follow **SemVer**:
  - **MAJOR**: breaking change to required sections/keys or meaning contracts
  - **MINOR**: backward compatible additions
  - **PATCH**: clarifications, typo fixes, examples
- `status` allowed values: `draft | active | deprecated | archived`
- Deprecations must include:
  - replacement pointer(s)
  - date
  - migration guidance

### Open questions (tracked) ❓
| Question | Owner | Target date |
|---|---|---|
| Which CI job is authoritative for docs lint + link checks? | TBD | TBD |
| Where is the canonical glossary (`docs/glossary.md`) anchored from? | TBD | TBD |
| Do we require doc checksum validation for “published” Story Nodes? | TBD | TBD |

---

## 🗺️ Diagrams

### System and documentation alignment 🧭
~~~mermaid
flowchart LR
  A[🧪 ETL Pipelines] --> B[🗂️ STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Graph]
  C --> D[🛡️ APIs]
  D --> E[🖥️ UI]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode]
~~~

### Optional sequence diagram (Focus Mode read path) 🎯
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

---

## 📦 Data & Metadata

### Inputs ✅
| Input | Format | Where from | Validation intent |
|---|---|---|---|
| Templates | Markdown | `docs/templates/` | Front-matter keys present; required sections exist |
| Evidence references | IDs/paths | STAC/DCAT/PROV + graph IDs | IDs resolve; catalog artifacts exist |
| Repo constraints | Standards docs | `docs/standards/` | Reviewer + CI checks |

### Outputs ✅
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Governed docs | Markdown | `docs/**` | Must match selected template |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Must cite evidence IDs + graph IDs |
| API contract docs | Markdown | `docs/**` + `src/server/**` | Must include contract + tests/rollback list |

### Required YAML front-matter fields (minimum) 🧾
Every governed doc MUST include:
- `title`, `path`, `version`, `last_updated`, `status`, `doc_kind`, `license`
- `owners` (at least one)
- `fair_category`, `care_label`, `sensitivity`, `classification`, `jurisdiction`
- pointers: `governance_ref`, `ethics_ref`, `sovereignty_policy`

Recommended (strongly):
- `doc_uuid` (URN), `semantic_document_id`, `event_source_id`
- `commit_sha` placeholder (fill on merge if automated)
- `ai_transform_permissions` / `ai_transform_prohibited` (if AI-assisted workflows are used)
- `doc_integrity_checksum` placeholder (fill on publish/merge if enforced)

> [!CAUTION]
> Tooling may depend on front-matter keys. If something is not applicable, set `"TBD"` or `"n/a"` — don’t delete fields.

### Stable identifiers (how to think about them) 🧷
- `doc_uuid`: identity of the doc as a governed artifact (stable across moves/renames)
- `semantic_document_id`: a human-readable stable key (used for indexing/search)
- `event_source_id`: ledger/eventstream key for audit trails (if used)
- `commit_sha`: the git commit that introduced this version (optional until merge)

### Doc integrity checksum (recommended) 🔐
If checksum enforcement is enabled, compute SHA-256 over the final committed file content.

~~~bash
# Example (Linux/macOS). Replace with your repo’s preferred command.
shasum -a 256 docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md
~~~

> [!NOTE]
> If your checksum process excludes the checksum line itself, document that rule in `docs/standards/` and implement it in CI. (Avoid “hand-wavy” checksums.)

### Sensitivity & redaction (hard rules) 🔒
- 🚫 Never include secrets, credentials, tokens, keys, private URLs, internal hostnames
- 🚫 Never publish exact coordinates for sensitive sites unless policy explicitly permits
- ✅ If content could identify a restricted location, **generalize** (region-level) and reference sovereignty rules
- ✅ If a screenshot is necessary, verify it does not leak coordinates, filenames, accounts, or private tiles

### Quality signals (what reviewers look for) ✅
- **Completeness:** template sections are filled or explicitly marked “N/A”
- **Traceability:** claims link to evidence IDs (catalogs) or stable repo artifacts (schemas/contracts)
- **Consistency:** pipeline ordering and API boundary are reinforced where relevant
- **Honesty:** uncertainties and assumptions are explicitly labeled
- **Accessibility:** headings, links, and alt text support scanning and assistive tech

### Asset policy (images/diagrams/maps) 🖼️
- Prefer **SVG** for diagrams when possible (diff-friendly).
- Use **PNG** for crisp UI screenshots; **JPEG** for photos/large imagery where size matters.
- Keep assets small and purposeful; avoid repo bloat.
- If an asset influences meaning (legend/class breaks/symbology), document the decision and reference the source layer(s).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC ✅
When a doc references a geospatial/temporal asset, include:
- STAC Collection ID(s)
- STAC Item ID(s)
- Path(s) under `data/stac/collections/` and `data/stac/items/`

🚫 Avoid “floating assets” (assets described in prose with no STAC representation).

### DCAT ✅
When a doc describes a dataset, include:
- DCAT dataset identifier
- License mapping
- Spatial/temporal coverage (as applicable)
- Path under `data/catalog/dcat/`

### PROV-O ✅
When a doc describes how an artifact was produced, include:
- `prov:wasDerivedFrom` (source IDs)
- `prov:wasGeneratedBy` (activity/run ID)
- Path under `data/prov/`

### Cross-layer linkage expectations 🔗
Docs should help keep systems aligned:
- DCAT dataset should reference distributions that point to STAC (or direct downloads)
- PROV should point to inputs and outputs (including STAC/DCAT IDs)
- Graph nodes/edges must point back to catalog IDs (not hand-waved)

### Narrative evidence rule (Story Nodes + Focus Mode) 📚
Every factual claim must link to an evidence identifier (STAC Item, DCAT dataset, PROV activity bundle, stable graph ID).

**Footnotes pattern (recommended in GFM)**
~~~markdown
The 1870–1875 corridor shows increased settlement density.[^e1]

[^e1]: Evidence: DCAT `kfm.ks.historical.settlement_density`; STAC `kfm.ks.historical.settlement_density`; PROV `kfm.prov.etl_1875_...`
~~~

---

## 🧱 Architecture

### Components (doc expectations) 🧩
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run receipts/logs |
| Catalogs | STAC/DCAT/PROV | JSON/JSON-LD + validators |
| Graph | Neo4j (or equivalent) | Cypher behind API boundary |
| APIs | Serve contracts + redaction | REST/GraphQL + tests |
| UI | Map + narrative | API calls only |
| Story Nodes | Curated narrative | Machine-ingestible Markdown |
| Focus Mode | Contextual synthesis | Provenance-linked bundle |

### Canonical subsystem homes (one source of truth) 🏠
- ETL and transformations: `src/pipelines/`
- Published datasets: `data/processed/`
- Catalog boundary artifacts: `data/stac/`, `data/catalog/dcat/`, `data/prov/`
- Graph building/migrations: `src/graph/`
- API contracts/implementation: `src/server/`
- UI: `web/`
- Story Nodes: `docs/reports/story_nodes/`
- Standards: `docs/standards/`

### Repo placement rules (hard) 📍
- Derived datasets → `data/processed/` (not `src/`)
- Catalog outputs:
  - STAC → `data/stac/...`
  - DCAT → `data/catalog/dcat/`
  - PROV → `data/prov/`
- Run logs and experiment artifacts → `mcp/runs/` or `mcp/experiments/` *(if present)*
- Never store raw sensitive data in `docs/` (use catalog pointers)

### “Evidence artifacts” pattern (AI/analysis outputs) 🧪🤖
Any analysis output that can influence decisions (simulations, OCR corpora, predicted layers) MUST:
- live under `data/processed/**`
- be cataloged in STAC/DCAT
- have PROV lineage (inputs, parameters, confidence/uncertainty metadata)
- be exposed to UI only through APIs enforcing redaction/classification

### Domain-specific documentation addenda (what to include) 🧠
These are **documentation requirements**, not code requirements.

**Modeling & simulation docs**
- assumptions + boundary conditions
- parameters + seeds
- verification/validation plan (V&V)
- uncertainty quantification + sensitivity analysis
- failure modes + limits of applicability

**Statistics & inference docs**
- sampling frame + confounders
- exploratory diagnostics (EDA)
- model diagnostics (residuals, calibration)
- uncertainty (intervals, posterior summaries)
- reproducibility notes (versions, random states)

**Geospatial & mapping docs**
- CRS/unit hygiene (explicit CRS)
- symbology/classification rationale (avoid misleading maps)
- scale/LOD considerations
- coordinate sensitivity rules (generalize if needed)

**Data systems & scaling docs**
- data sizes + partitioning assumptions
- indexing strategy + query patterns
- concurrency/idempotency risks
- migration strategy + rollback

**Security docs**
- threat model framing (defensive posture)
- least privilege + deny-by-default defaults
- redaction/classification propagation

---

## 🧠 Story Node & Focus Mode Integration

### How docs surface in Focus Mode 🎯
Focus Mode must only show provenance-linked narratives:
- claims → evidence IDs
- evidence → PROV lineage
- UI displays citations + audit flags consistently

### Focus Mode hard gates (trust preservation) 🔒
- Only provenance-linked content can appear
- AI content must be **opt-in**, clearly labeled, and paired with uncertainty/confidence metadata
- No sensitive location leaks (generalize/omit as required)
- No side-channel bypass of sovereignty/classification rules

### Parser-friendly Markdown (recommended) 🧱
If Markdown is machine-parsed for Focus Mode:
- keep headings simple and consistent
- keep citations in a consistent pattern (e.g., footnotes)
- avoid heavy HTML or deeply nested tables
- test rendering in the target UI (don’t assume GitHub preview == Focus Mode parser)

---

## 🧪 Validation & CI/CD

### Minimum CI gates (expected for v13 discipline) ✅
- Markdown protocol checks (template compliance + required sections)
- YAML front-matter validation (required keys + allowed values)
- Link/reference validation (no broken internal links)
- Schema validation for referenced artifacts (STAC/DCAT/PROV where applicable)
- Secrets scanning + “no internal URLs/hostnames” checks
- Sensitivity checks (coordinate leakage, classification downgrades)

> [!NOTE]
> If CI isn’t fully wired, treat these as required local checks for any doc that influences public meaning.

### Local reproduction (placeholder) 🧪
~~~bash
# Replace with repo-specific commands:
# 1) markdown lint / link checks
# 2) schema validation (STAC/DCAT/PROV)
# 3) unit + integration tests (if doc change implies code change)
~~~

### Telemetry signals (optional) 📈
| Signal | Source | Where recorded |
|---|---|---|
| Doc compliance rate | CI | `docs/telemetry/` *(if present)* |
| Broken links | CI | `docs/telemetry/` *(if present)* |
| Sensitivity violations | Review/CI | `docs/telemetry/` *(if present)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates (minimum) 🧭
- Changes affecting security/sovereignty/public exposure → **requires human review**
- New sensitive layers or redaction rules → **requires governance review**
- New public-facing endpoints → **requires API + security review**
- Any doc that changes “what users believe” about a dataset/story → **requires evidence + provenance links**

### CARE & sovereignty considerations 🪶
- Treat culturally sensitive and Indigenous content as potentially restricted.
- Do not infer sensitive locations; follow sovereignty policy and redaction requirements.
- Keep “care_label” explicit when a domain demands it (even if classification is otherwise open).

### AI usage constraints 🤖
- Allowed transformations (default): summarize, structure extraction, translation, keyword indexing
- Prohibited: generating new policy in-place, inferring sensitive locations, fabricating sources
- If AI is used to draft narrative meaning, label it and preserve a review trail (PR notes, receipts, or MCP logs)

---

## 📚 Project reference library influence map

> [!NOTE]
> These files inform how we write/review KFM docs (rigor, safety, scaling, visualization honesty).  
> They are **influences**, not substitutes for KFM’s governed standards.

<details>
<summary><strong>📦 Expand: Reference library → what it influences in this protocol</strong></summary>

### 🧭 Core KFM system + documentation protocols
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `MARKDOWN_GUIDE_v13.md.gdoc` | 🧾 v13 doc protocol | Reinforces contract-first + evidence-first, canonical pipeline, domain expansion, and CI-gate expectations. |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` | 🧭 System blueprint | Anchors the “pipeline ordering is law” mindset and boundary artifacts as publish gates. |
| `Audit of the Kansas Frontier Matrix (KFM) Repository.pdf` | 🧯 Reality check | Highlights gaps that docs must not paper over; pushes doc→test→evidence discipline. |
| `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx` | 🧪 Roadmap | Encourages draft-vs-canonical separation and clear labeling of proposals vs implemented behavior. |
| `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx` | ✍️ Craft | Improves scannability, accessibility habits, GFM features (footnotes, task lists), and template rigor. |
| `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` | 🔬 Method | Forces experiment-like documentation: questions→methods→results→limits; emphasizes receipts + reproducibility. |

### 🛰️ Geospatial, EO/RS, cartography, and web mapping
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `python-geospatial-analysis-cookbook.pdf` | 🗺️ GIS engineering | Enforces CRS/unit hygiene, repeatable geoprocessing documentation, and IO discipline. |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | 🛰️ EO workflows | Strengthens RS domain docs: exports, time-series, raster governance, and derived-product provenance. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | 🎨 Cartography ethics | Requires documenting symbology, classification, aggregation, and map honesty as meaning decisions. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | 📱 Field constraints | Encourages offline/low-bandwidth UX documentation and upstream asset preparation notes. |

### 🧊 Visualization, UI, web performance
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `responsive-web-design-with-html5-and-css3.pdf` | 🌐 Web reality | Pushes accessible, responsive patterns; encourages documenting performance budgets and device constraints. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | 🧊 3D constraints | Drives documenting coordinate conventions, LOD/tiling rules, and GPU-friendly asset prep. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | 🖼️ Media hygiene | Sets expectations for doc assets: format choice, compression, thumbnails, and avoiding repo bloat. |

### 📊 Statistics, modeling, simulation, inference hygiene
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `Understanding Statistics & Experimental Design.pdf` | 📊 Rigor | Requires documenting confounders, study design, and uncertainty framing (not just conclusions). |
| `graphical-data-analysis-with-r.pdf` | 📉 EDA instincts | Normalizes “show diagnostics” docs: anomaly surfacing, sanity checks, visual validation. |
| `regression-analysis-with-python.pdf` | 📈 Baselines | Requires residual diagnostics, leakage checks, assumptions, and reproducible baselines. |
| `Regression analysis using Python - slides-linear-regression.pdf` | 📈 Quick checks | Reinforces lightweight but mandatory regression documentation (residuals, scaling, assumptions). |
| `think-bayes-bayesian-statistics-in-python.pdf` | 🎲 Uncertainty | Encourages explicit priors, posterior reporting, and calibrated decision language. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | 🧪 V&V discipline | Elevates simulation docs with verification/validation, sensitivity analysis, and UQ expectations. |
| `Generalized Topology Optimization for Structural Design.pdf` | 🧮 Optimization | Improves optimization docs: objective/constraints, solver settings, reproducibility trails. |
| `Spectral Geometry of Graphs.pdf` | 🕸️ Graph thinking | Encourages careful interpretation of graph metrics and provenance-aware graph claims. |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | 🤖 Practical ML | Pushes model reproducibility notes, training/eval artifacts, and usage constraints documentation. |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | ⚖️ AI governance | Strengthens labeling of AI-assisted outputs, provenance expectations, and restraint under uncertainty. |
| `Introduction to Digital Humanism.pdf` | ❤️ Human impact | Improves accountability language and keeps humans in control of meaning-making. |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | 🧠 Systems | Encourages feedback-loop awareness and resilience thinking in governance/architecture docs. |

### 🗄️ Data systems, scaling, interoperability
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | 🐘 Data store discipline | Strengthens DB runbooks: schema discipline, indexing, migrations, operational conventions. |
| `Scalable Data Management for Future Hardware.pdf` | ⚙️ Performance | Pushes documentation of locality/partitioning, concurrency assumptions, and scaling risks. |
| `Data Spaces.pdf` | 🔗 Interop | Reinforces metadata-as-interface mindset: stable IDs, provenance, pointer-over-payload discipline. |

### 🛡️ Security mindset (defensive)
| Project file | Primary lens | How it upgrades KFM Markdown work |
|---|---|---|
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | 🧯 Threat modeling | Improves defensive documentation: least privilege, incident thinking, safe defaults. |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | 🛡️ Hostile inputs | Reinforces secure-ingestion posture and parser skepticism (without teaching exploitation). |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | 🧵 Concurrency | Encourages docs that warn about race conditions, idempotency, and reliability boundaries. |

### 📚 Programming reference shelves (craft breadth)
| Project file | Lens | How it upgrades KFM Markdown work |
|---|---|---|
| `A programming Books.pdf` | 🧰 Polyglot craft | Broad support for maintainable examples and tooling clarity. |
| `B-C programming Books.pdf` | 🧰 Shell + systems | Encourages safe scripting patterns and reproducible command surfaces in runbooks. |
| `D-E programming Books.pdf` | 🧰 Engineering fundamentals | Supports consistent debugging, environments, and cross-stack documentation patterns. |
| `F-H programming Books.pdf` | 🧰 Tooling literacy | Helps keep runbooks grounded and practical. |
| `I-L programming Books.pdf` | 🧰 Implementation detail | Reinforces disciplined code examples and configuration hygiene. |
| `M-N programming Books.pdf` | 🧰 Systems + networking | Supports documenting reliability, failure modes, and interfaces. |
| `O-R programming Books.pdf` | 🧰 Breadth | Reinforces broader tooling awareness and documentation patterns. |
| `S-T programming Books.pdf` | 🧰 Testing + tooling | Encourages documenting verification methods and test strategy explicitly. |
| `U-X programming Books.pdf` | 🧰 Breadth | Supports documentation for less-common tools and edge-case workflows. |

</details>

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0-draft | 2026-01-12 | Aligned to Master Guide v13; clarified pipeline invariants; strengthened front-matter rules; added a11y + asset policy; expanded validation gates; incorporated project reference library influences across modeling, geospatial, scaling, security, and human-centered governance. | KFM Engineering |
| v1.0.0-draft | 2025-12-19 | Initial Markdown work protocol standard | TBD |
