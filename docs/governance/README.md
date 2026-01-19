---
title: "KFM Governance — README"
path: "docs/governance/README.md"
version: "v1.2.0"
last_updated: "2026-01-19"
status: "draft"
doc_kind: "README"
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
review_gates_ref: "docs/governance/REVIEW_GATES.md"
raci_ref: "docs/governance/RACI.md"
policy_pack_ref: "tools/validation/policy/"
faircare_oversight_ref: "docs/guides/governance/faircare-oversight.md"

fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:governance:readme:v1.2.0"
semantic_document_id: "kfm-governance-readme-v1.2.0"
event_source_id: "ledger:kfm:doc:governance:readme:v1.2.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
  - "auto_approve_or_merge_changes"
  - "publish_uncited_narrative"

doc_integrity_checksum: "sha256:<to-be-filled>"
---

# KFM Governance — README 🧱🌾⚖️

<div align="center">

![Status](https://img.shields.io/badge/status-draft-yellow)
![License](https://img.shields.io/badge/license-CC--BY--4.0-blue)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-governed-brightgreen)
![Jurisdiction](https://img.shields.io/badge/jurisdiction-US--KS-lightgrey)
![KFM--MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)
![STAC](https://img.shields.io/badge/STAC-KFM--STAC%20v11.0.0-5e4fa2)
![DCAT](https://img.shields.io/badge/DCAT-KFM--DCAT%20v11.0.0-3288bd)
![PROV](https://img.shields.io/badge/PROV-KFM--PROV%20v11.0.0-66c2a5)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-black)

</div>

> [!IMPORTANT]
> **This README is an index + process guide.** Canonical policy text lives in:
> - ✅ **Root Governance:** [`docs/governance/ROOT_GOVERNANCE.md`](ROOT_GOVERNANCE.md)
> - ⚖️ **Ethics:** [`docs/governance/ETHICS.md`](ETHICS.md)
> - 🪶 **Sovereignty:** [`docs/governance/SOVEREIGNTY.md`](SOVEREIGNTY.md)
>
> Keep this file **link-heavy** and **definition-light**. **No new policy definitions here.**

---

## 📑 Contents

- [🔗 Quick links](#-quick-links)
- [🧱 Governance in one screen](#-governance-in-one-screen-non-negotiables)
- [🗺️ Canonical artifacts map](#️-canonical-artifacts-map)
- [🗂️ Directory layout](#️-directory-layout)
- [🧑‍⚖️ Governance model](#️-governance-model-who-reviews-what)
- [🚦 Review gates & triggers](#-review-gates--governance-triggers)
- [🧾 Approvals, waivers, audit trail](#-approvals-waivers-audit-trail)
- [⚙️ Validation & policy-as-code](#️-validation--policy-as-code)
- [🧠 Story Nodes & Focus Mode](#-story-nodes--focus-mode-governance)
- [📦 Data & metadata governance](#-data--metadata-governance)
- [🧬 Ontology & knowledge graph governance](#-ontology--knowledge-graph-governance)
- [🔐 Security & supply-chain governance](#-security--supply-chain-governance)
- [📚 Reference library governance](#-reference-library-governance)
- [🕰️ Version history](#️-version-history)
- [Footer refs](#footer-refs-do-not-remove)

---

## 🔗 Quick links

### 🧭 Start here (most used)

- 🧭 **Master Guide (v13):** [`docs/MASTER_GUIDE_v13.md`](../MASTER_GUIDE_v13.md)
- 🧱 **Root Governance:** [`docs/governance/ROOT_GOVERNANCE.md`](ROOT_GOVERNANCE.md)
- ⚖️ **Ethics:** [`docs/governance/ETHICS.md`](ETHICS.md)
- 🪶 **Sovereignty:** [`docs/governance/SOVEREIGNTY.md`](SOVEREIGNTY.md)
- 🧠 **FAIR+CARE Oversight:** [`docs/guides/governance/faircare-oversight.md`](../guides/governance/faircare-oversight.md)
- 🧩 **Doc templates:** [`docs/templates/`](../templates/)
- 🏗️ **Architecture (v13 blueprint):** [`docs/architecture/`](../architecture/)
- 🔐 **Security docs:** [`docs/security/`](../security/) + [`SECURITY.md`](../../SECURITY.md)
- 🧪 **Methods / SOPs (MCP):** [`mcp/`](../../mcp/)
- 🛡️ **Policy Pack (OPA/Rego):** [`tools/validation/policy/`](../../tools/validation/policy/)
- 🧰 **Runtime policy wiring:** [`api/scripts/policy/README.md`](../../api/scripts/policy/README.md)

### 🧩 If you’re changing…

| You’re changing… | Go here first | Why |
|---|---|---|
| 🗺️ **Data ingestion / intake** | `data/raw/` + Data Intake guide + Policy Pack | Intake is the first governance gate (fail-closed) |
| 🧾 **Metadata / catalogs** | `data/stac/`, `data/catalogs/`, `data/prov/` + schema validators | Evidence Triplet comes before graph/UI/narrative |
| 🧬 **Ontology / graph mappings** | `schemas/` + `src/graph/` + architecture docs | Ontology bindings are contract artifacts |
| 🌐 **API endpoints / downloads** | `src/server/` or `api/` + `SECURITY.md` + policy runtime | API boundary is mandatory; enforce redaction here |
| 🧭 **UI / Map / Story playback** | `web/` + UI system docs | UI must only consume contracted APIs + governed story content |
| 🧠 **Focus Mode / AI** | `ETHICS.md` + AI system docs + policy pack | AI is evidence-first, cited, advisory-only |
| 🧾 **Story Nodes publishing** | `docs/reports/story_nodes/` (or `web/story_nodes/`) + templates | Narrative must be provenance-linked |

---

## 🧱 Governance in one screen

> [!NOTE]
> These are **index-level invariants** (the “what”). Canonical requirements (the “how”) live in the linked governance docs + policy pack.

### ✅ Non-negotiables (project posture)

- 🧬 **Pipeline ordering is enforced:** **ETL → Evidence Triplet (STAC/DCAT/PROV) → Graph → APIs → UI → Story Nodes → Focus Mode**  
  ↳ See: [`docs/MASTER_GUIDE_v13.md`](../MASTER_GUIDE_v13.md) + [`tools/validation/policy/`](../../tools/validation/policy/)
- 🔌 **API boundary is mandatory:** UI does **not** read Neo4j (or raw catalog stores) directly  
  ↳ See: architecture docs + policy pack
- 🧾 **Provenance-first publishing:** if you publish/serve/ship something, it has traceable lineage first  
  ↳ See: PROV profile + `data/prov/`
- 🧯 **Fail-closed:** missing governance labels, missing provenance, or failed policy checks block promotion  
  ↳ See: intake guide + CI policy gate
- 🧠 **Evidence-first narrative:** Story Nodes / Focus Mode must cite governed evidence (catalog IDs + links)  
  ↳ See: [`ETHICS.md`](ETHICS.md) + story node templates
- 🧍 **Human-in-the-loop:** automation may propose changes, but never bypasses approvals  
  ↳ See: MCP + policy pack + governance roles

---

## 🗺️ Canonical artifacts map

| Artifact | Path | Owner (expected) | Notes |
|---|---|---|---|
| This README | `docs/governance/README.md` | Maintainers | Index + process guidance |
| Root Governance | `docs/governance/ROOT_GOVERNANCE.md` | Governance owners | Labels, approvals, exceptions |
| Ethics | `docs/governance/ETHICS.md` | Ethics reviewers | Transparency, bias/disclosure, AI constraints |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | Sovereignty reviewers | CARE + culturally sensitive handling |
| Review gates registry | `docs/governance/REVIEW_GATES.md` | Governance owners | Canonical triggers + gates (recommended) |
| RACI / roles | `docs/governance/RACI.md` | Maintainers | Who can approve what (recommended) |
| FAIR+CARE oversight | `docs/guides/governance/faircare-oversight.md` | Oversight leads | Audit cadence + escalation path |
| Policy Pack (OPA) | `tools/validation/policy/` | Governance + DevOps | “Policy as code” gate |
| Runtime policy wiring | `api/scripts/policy/README.md` | Server maintainers | API + Focus Mode enforcement hooks |
| Doc templates | `docs/templates/` | Maintainers | Front-matter + schema layout |
| Architecture blueprints | `docs/architecture/` | Maintainers | v13 blueprint + subsystem boundaries |
| Security | `docs/security/` + `SECURITY.md` | Security reviewers | Reporting + hardening |

---

## 🗂️ Directory layout

> [!TIP]
> KFM has **observed/current** folders _and_ a **v13 target** layout. Until the migration is complete, treat paths as “canonical target + supported legacy.”

### Current/observed repo anchors (common)

- `api/` — API service (legacy layout)
- `web/` — UI (React / MapLibre / Cesium)
- `pipelines/` — ingestion + processing workflows (legacy layout)
- `data/` — raw/work/processed + evidence outputs
- `mcp/` — Methods, Controls & Processes (SOPs, model cards, runbooks)
- `docs/` — documentation roots: governance, architecture, templates, specs, security, standards
- `tools/` — validation, CI utilities, policy gates

### Evidence Triplet directories (preferred)

KFM’s governance model treats **STAC + DCAT + PROV** as first-class evidence outputs.

- 🛰️ `data/stac/` — STAC Items/Collections for assets and derived products
- 🧾 `data/catalogs/` — DCAT dataset/distribution discovery feeds *(some docs may refer to `data/catalog/` during transition)*
- 🧬 `data/prov/` — PROV lineage records (W3C PROV(-O) compatible)

### Story Node content roots (observed + target)

- 🗺️ **Observed (UI-rooted):** `web/story_nodes/` (or `content/stories/`)  
- 🧾 **Editorial target:** `docs/reports/story_nodes/{draft,published}/`  

> [!NOTE]
> A **Story Node** is typically a folder containing narrative **Markdown** plus a **JSON config** (map view state, timeline year, layer toggles, citations). Keep governance labels + evidence links with the node.

### Illustrative v13 target tree (minimal)

~~~text
📦 repo-root/
├── 📁 data/
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   ├── 📁 stac/                # 🛰️ evidence
│   ├── 📁 catalogs/            # 🧾 evidence (DCAT)
│   └── 📁 prov/                # 🧬 evidence (PROV)
├── 📁 schemas/                 # contract artifacts (JSON Schema / OpenAPI / etc.)
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/
├── 📁 web/
│   └── 📁 story_nodes/         # UI-consumable story content (if used)
├── 📁 docs/
│   ├── 📁 governance/          # 👈 you are here
│   ├── 📁 templates/
│   ├── 📁 architecture/
│   ├── 📁 security/
│   └── 📁 reports/
│       └── 📁 story_nodes/
│           ├── 📁 draft/
│           └── 📁 published/
├── 📁 mcp/
└── 📁 tools/
    └── 📁 validation/
        └── 📁 policy/          # OPA/Rego + Conftest
~~~

---

## 🧑‍⚖️ Governance model (who reviews what)

> [!NOTE]
> KFM’s design emphasizes “governance from day zero” — automated checks + explicit reviewer lanes + auditable lineage.

### Minimum reviewer roles (recommended)

| Role | Reviews | Trigger examples |
|---|---|---|
| 🧱 **Maintainers** | All PRs (baseline) | Any change |
| ⚖️ **Ethics reviewers** | AI/ML, narrative generation, disclosure | Focus Mode behavior, summarization, model updates |
| 🪶 **Sovereignty reviewers** | Indigenous/culturally sensitive data, restricted locations | New/updated sensitive layers, story content touching sensitive sites |
| 🔐 **Security reviewers** | authN/authZ, public endpoints, downloads, supply chain | New endpoints, exports, auth roles, CI signing |
| 🧭 **Domain stewards** | domain ETL + interpretation | New domains, mapping rules, schema alignment |

### Oversight & audit cadence

- 🧠 **FAIR+CARE oversight** (audits, escalation, governance maturity work):  
  [`docs/guides/governance/faircare-oversight.md`](../guides/governance/faircare-oversight.md)

---

## 🚦 Review gates & governance triggers

### Governance decision flow (PR → gates → review)

~~~mermaid
flowchart TD
  A["Change proposed (PR)"] --> B["Run CI gates (contracts + policy checks)"]
  B --> C{"Governance trigger hit?"}
  C -- "No" --> D["Standard review + merge (maintainers)"]
  C -- "Yes" --> E["Request lane reviews (ethics / sovereignty / security / domain)"]
  E --> F["Address findings + record approvals"]
  F --> D
  D --> G["Release / publish / promote (if applicable)"]
  G --> H["Audit trail (PROV + telemetry + ledger)"]
~~~

### Trigger examples (index-level guidance)

> [!TIP]
> Keep the canonical list in `docs/governance/REVIEW_GATES.md` (recommended). This README only lists “common triggers”.

- 🧾 **Evidence Triplet changes** (`data/stac/**`, `data/catalogs/**`, `data/prov/**`) → governance + domain review
- 🔌 **API boundary / access changes** (new endpoints, exports, auth roles) → security review
- 🧠 **AI / Focus Mode changes** (prompting, retrieval, summarization, model changes) → ethics review (+ security if data exposure risk)
- 🪶 **Sovereignty + cultural protocol changes** (restricted location handling, community-only content) → sovereignty review
- 🧩 **Contract changes** (`schemas/**`, OpenAPI, GraphQL SDL) → contract gate + versioning review
- 🗺️ **Story Node publication** (`story_nodes/published/**`) → narrative review + evidence check
- 📦 **Offline packs / AR experiences** (packaging content for devices/on-site) → sovereignty + security review (classification must carry into offline output)
- 🌍 **External integrations** (Google Earth Engine, OGC services, third-party APIs) → security + compliance review

---

## 🧾 Approvals, waivers, audit trail

### Recording approvals (minimum)

- ✅ PR approvals in Git history are the baseline record.
- ✅ For high-impact changes, also record in a governed registry (recommended):
  - `docs/governance/approvals.yaml` *(planned)*  
  - `docs/governance/exceptions.yaml` *(planned)*

### Exceptions & waivers (time-bounded)

> [!CAUTION]
> Treat exceptions as **rare**, **explicit**, and **expiring**. Canonical rules belong in [`ROOT_GOVERNANCE.md`](ROOT_GOVERNANCE.md).

Recommended waiver entry fields:

- scope, reason, approver(s), expiry, mitigations, follow-up issue/link

### Audit trail expectations (what “auditable” means in KFM)

- 🧬 **PROV** for data + derived outputs (inputs, parameters, code version, agents)
- 🧾 **Catalog entries** for discoverability (STAC/DCAT)
- 📈 **Telemetry** for runtime events (policy checks, redaction notices, Focus Mode usage)
- 🧠 **AI governance ledger** for Focus Mode responses and policy outcomes (append-only, queryable)

---

## ⚙️ Validation & policy-as-code

### Baseline CI gates (minimum expectations)

- [ ] ✅ **Markdown protocol validation** (front-matter completeness + link integrity)
- [ ] ✅ **Contract validation** (schemas + API specs)
- [ ] ✅ **Catalog validation** (STAC/DCAT/PROV shape + cross-links)
- [ ] ✅ **Graph integrity checks** (constraints + ingest invariants)
- [ ] ✅ **Policy gate** (OPA/Rego + Conftest) for governance rules
- [ ] ✅ **Security scanning** (secrets, deps/SBOM, vuln scans)
- [ ] ✅ **Sovereignty scanning** (restricted precision / sensitive-area heuristics)

### Policy Pack (OPA/Rego)

- 🔒 **CI policy gate:** [`tools/validation/policy/`](../../tools/validation/policy/)
- 🧠 **Runtime enforcement hooks:** [`api/scripts/policy/README.md`](../../api/scripts/policy/README.md)

Common examples the policy pack should encode (names only — definitions live in policy docs):

- **Pipeline Ordering Rule**
- **API Boundary Rule**
- **Provenance-First Publishing Rule**
- **Evidence-First Narrative Rule**
- **Restricted Location Handling Rule**

### Detect → Validate → Promote (recommended workflow)

~~~mermaid
flowchart LR
  A["Detect changes (checksums / repo events)"] --> B["Validate (schema + policy + lanes)"]
  B --> C{"All checks pass?"}
  C -- "No" --> D["Fail + report (checks + artifacts)"]
  C -- "Yes" --> E["Open PR (promotion)"]
  E --> F["Sign PR/commit (Sigstore)"]
  F --> G["Emit lineage + store audit artifacts"]
~~~

### Reproduction (placeholders — wire to repo scripts)

~~~bash
# Policy gate (OPA/Conftest)
conftest test . -p tools/validation/policy

# Contract checks (schemas + API)
# e.g., python tools/validation/schema_check.py  (TBD)

# Catalog checks (STAC/DCAT/PROV)
# e.g., python tools/validation/catalog_qa.py    (TBD)

# Lane validators (spatial QA, graph checks)
# e.g., python tools/validation/spatial_lane.py  (TBD)
# e.g., python tools/validation/graph_lane.py    (TBD)
~~~

---

## 🧠 Story Nodes & Focus Mode governance

### Where Story Nodes live

- 🧪 Drafts (editorial): `docs/reports/story_nodes/draft/`
- ✅ Published (editorial): `docs/reports/story_nodes/published/`
- 🗺️ UI runtime (observed): `web/story_nodes/` (or `content/stories/`)

> [!NOTE]
> If the repo uses both, treat the editorial folder as **source-of-truth** and sync into `web/story_nodes/` at build time (recommended).

### Story Node requirements (high level)

- 🔗 Every claim references governed evidence (STAC/DCAT/PROV IDs + links)
- 🏷️ Inherit governance labels (classification/sensitivity) from the evidence used
- 🧾 Include media licensing and attribution (especially for images/scans)
- 🧭 Include map-view configuration (time range, layers, camera, filters) in a versioned JSON config
- 🚫 No unsourced narrative in `published/`

### Focus Mode expectations (high level)

- 🧠 **Advisory-only**: summarizes/interprets KFM evidence; avoids speculation
- 🔍 **Citations required**: every answer includes references to governed evidence
- 🧯 **Redaction-aware**: if precision is restricted, show a notice + log an event (telemetry + ledger)
- 🧾 **Explainable**: provide a provenance/“why” panel (sources + retrieval trace) where feasible
- 🧍 **Human-in-the-loop**: Focus Mode does not auto-publish Story Nodes and does not bypass review lanes

### AR & offline packs (governance reminder)

If KFM ships AR overlays or offline datasets:

- classification + sovereignty constraints must carry into packaged artifacts
- enforce policy at export/build time (not only at runtime)
- record provenance + packaging activity in PROV/ledger

---

## 📦 Data & metadata governance

### Standards posture (what KFM prefers)

- 🗺️ Vectors: **GeoJSON**
- 🛰️ Rasters: **Cloud-Optimized GeoTIFF (COG)**
- 🌍 CRS: **WGS84** (unless explicitly documented otherwise)
- 🧾 Metadata: **STAC + DCAT**
- 🧬 Lineage: **W3C PROV**

### Intake “fail-closed” posture

- If required provenance/labels are missing → ingestion/promotion blocks
- If a check cannot be performed → treat as failure (until explicitly waived)

### Evidence artifacts (models, analyses, derived products)

Treat derived outputs (e.g., simulations, ML predictions, analytics) as evidence artifacts:

- capture inputs, parameters, code version, and outputs in PROV
- register outputs in STAC/DCAT before narrative/UI usage
- ensure sensitivity/classification is inherited and enforced in API/UI layers

### External integrations & interoperability (governance trigger)

If integrating services like Google Earth Engine, OGC APIs, or third-party datasets:

- document: data licensing, terms, caching/storage policy, and attribution requirements
- route through security review if requests touch auth, downloads, or new public endpoints

---

## 🧬 Ontology & knowledge graph governance

KFM’s semantic layer is implemented as a graph (e.g., Neo4j) that links people, places, events, and datasets, and aims to align with standard ontologies.

Governance expectations:

- 🧩 ontology mappings and graph constraints are **contract artifacts** (schema-controlled, versioned)
- 🔁 changes to entity resolution, ontology bindings, or constraints → governance review
- 🧾 graph analytics outputs are **evidence artifacts** and must be cataloged + provenance-linked before surfacing in UI or Story Nodes

---

## 🔐 Security & supply-chain governance

- Follow [`SECURITY.md`](../../SECURITY.md) + [`docs/security/`](../security/) for reporting and handling vulnerabilities.
- 🧾 Supply-chain rigor is encouraged (SBOMs, attestations, Sigstore signing) — especially for automated promotions.
- 🚫 No secrets/PII in repo. Never commit credentials (even in examples).
- 🧯 For sensitive-content incidents (e.g., location exposure): follow a documented takedown + rollback procedure and emit an audit event.

---

## 📚 Reference library governance

> [!NOTE]
> KFM distinguishes **project-authored docs** from **third‑party reference PDFs/portfolios**, which retain their original licenses/terms.

### Recommended handling ✅

- Store third-party references under a clear root (suggested): `docs/library/`
- Add a manifest: `docs/library/README.md` with:
  - title, source, license/terms, why included, and redistribution notes
- Prefer linking to official sources when redistribution is not permitted
- **PDF Portfolios:** unpack into individual PDFs before committing (GitHub rendering/search is limited)

<details>
<summary>📦 Project workspace reference pack (current)</summary>

#### 🧾 KFM project-authored / KFM-specific references

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`

#### 🧠 Research packs / PDF portfolios (unpack recommended)

- `AI Concepts & more.pdf` *(PDF portfolio)*
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(PDF portfolio)*
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(PDF portfolio)*
- `Various programming langurages & resources 1.pdf` *(PDF portfolio)*

</details>

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.2.0 | 2026-01-19 | Synced governance README to KFM reference docs: clarified Evidence Triplet dirs, policy-as-code (OPA/Conftest) links, Story Node path reality (`web/story_nodes` vs `docs/reports/story_nodes`), added FAIR+CARE oversight link + runtime policy wiring; refreshed reference pack list and PDF-portfolio handling guidance | TBD |
| v1.1.0 | 2026-01-12 | Aligned README with Master Guide v13 draft (canonical homes, story_nodes workflow); expanded CI gates + policy-pack roadmap | TBD |
| v1.0.0 | 2025-12-27 | Initial governance README scaffold | TBD |

---

## Footer refs (do not remove)

- Master Guide: [`docs/MASTER_GUIDE_v13.md`](../MASTER_GUIDE_v13.md)
- Templates: [`docs/templates/`](../templates/)
- Architecture: [`docs/architecture/`](../architecture/)
- Governance: [`docs/governance/ROOT_GOVERNANCE.md`](ROOT_GOVERNANCE.md)
- Ethics: [`docs/governance/ETHICS.md`](ETHICS.md)
- Sovereignty: [`docs/governance/SOVEREIGNTY.md`](SOVEREIGNTY.md)
- Policy Pack: [`tools/validation/policy/`](../../tools/validation/policy/)
- FAIR+CARE Oversight: [`docs/guides/governance/faircare-oversight.md`](../guides/governance/faircare-oversight.md)
- Runtime policy wiring: [`api/scripts/policy/README.md`](../../api/scripts/policy/README.md)