# 🧾🔐 MCP Traceability & Policies (KFM / Kansas-Matrix-System)

![Status](https://img.shields.io/badge/status-draft-yellow)
![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-6f42c1)
![Trace](https://img.shields.io/badge/trace-STAC%20%7C%20DCAT%20%7C%20PROV-brightgreen)
![Policy](https://img.shields.io/badge/policy-OPA%20%7C%20Conftest-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-orange)
![Security](https://img.shields.io/badge/security-SBOM%20%7C%20SLSA%20%7C%20Sigstore-red)

> ✅ **Golden rule:** *If it isn’t traceable, it doesn’t ship.*  
> 🧠 **Note:** In this repo, **MCP = Master Coder Protocol** (scientific method + reproducibility + documentation-first) — **not** “Model Context Protocol”.  [oai_citation:0‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

This folder documents the **traceability model** and **policy enforcement system** that makes KFM “evidence-first” and “catalog-driven”:  
- 📦 Data only becomes “real” in the platform once the **evidence triplet** exists (**STAC + DCAT + PROV**) and is versioned.  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🛡️ Governance rules are enforced via a **Policy Pack** (OPA/Rego + Conftest), in CI *and* at runtime.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🖥️ The UI and 🤖 Focus Mode surface provenance (citations, lineage, source/license) so users can verify.  [oai_citation:3‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧭 Table of Contents

- [What lives here](#-what-lives-here)
- [Core principles](#-core-principles)
- [End-to-end trace & policy flow](#-end-to-end-trace--policy-flow)
- [Traceability model](#-traceability-model)
- [Policy model](#-policy-model)
- [Governance + FAIR/CARE oversight](#-governance--faircare-oversight)
- [DevOps provenance: PR → PROV → Graph](#-devops-provenance-pr--prov--graph)
- [Audit + observability](#-audit--observability)
- [Artifact integrity + supply chain](#-artifact-integrity--supply-chain)
- [Workflows](#-workflows)
- [Templates](#-templates)
- [Glossary](#-glossary)
- [Source library](#-source-library)

---

## 📂 What lives here

**Path:** `mcp/traceability/policies/docs/`

This README is the **index** for how KFM should:
- 🔗 **Bind** every dataset / asset / model / story / AI answer to verifiable evidence.
- 🧾 **Prove** lineage using standards (**STAC/DCAT/PROV**) and a knowledge graph mirror.
- 🛡️ **Enforce** governance with policy-as-code (CI + runtime).
- 🧑‍⚖️ **Respect** FAIR + CARE principles, including sovereignty and sensitivity constraints.

> 📌 Implementation references live elsewhere (examples):  
> - Policy Pack: `api/scripts/policy/README.md` (OPA/Rego + Conftest)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
> - Standards profiles: `docs/standards/*` (KFM STAC/DCAT/PROV profiles)  [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
> - Data intake spine: `data/raw/`, `data/stac/`, `data/catalogs/`, `data/prov/`  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 🧱 Core principles

### 1) 📜 Contract-first (schemas are first-class)
Schemas + API contracts are treated as **core artifacts**; changes are versioned and validated.  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 2) ⚙️ Deterministic pipelines (reproducible ETL)
Transformations must be **idempotent**, config-driven, and fully logged, producing stable outputs given stable inputs.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) 🧬 Evidence-first publishing (no evidence = no publish)
KFM requires a versioned **evidence triplet** stored under:
- `data/stac/` 🛰️  
- `data/catalogs/` 📚  
- `data/prov/` 🧬  
…as the gate for “official platform data”.  [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 4) 🛡️ Policies are code (CI + runtime)
Policies are codified, versioned, auditable, and enforceable without hand-waving. Runtime checks can prevent unsafe data access or disallowed AI output.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 5) 🌍 FAIR + CARE (especially for sensitive/cultural data)
Governance must address both:
- **FAIR** (Findable, Accessible, Interoperable, Reusable)
- **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics)  
including sovereignty and sensitivity constraints (e.g., “no output may be less restricted than its inputs”).  [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:13‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🗺️ End-to-end trace & policy flow

```mermaid
flowchart LR
  Raw[📥 Raw data (immutable)] --> Pipe[⚙️ Deterministic pipeline]
  Pipe --> STAC[🛰️ STAC (items/collections)]
  Pipe --> DCAT[📚 DCAT (dataset/distributions)]
  Pipe --> PROV[🧬 PROV (activities/entities/agents)]
  subgraph Evidence["✅ Evidence Triplet (versioned)"]
    STAC
    DCAT
    PROV
  end
  Evidence --> Graph[🕸️ Neo4j Knowledge Graph]
  Graph --> API[🔌 APIs (REST/GraphQL)]
  API --> UI[🖥️ UI (Evidence Panel • Dataset Inspector)]
  API --> Focus[🤖 Focus Mode (RAG + Graph queries)]
  Dev[🔧 DevOps (PRs/Commits)] -->|PROV JSON-LD| Graph

  Policy[🛡️ Policy Pack (OPA/Rego + Conftest)] -.gates.- Pipe
  Policy -.gates.- Evidence
  Policy -.gates.- Graph
  Policy -.gates.- API
  Policy -.gates.- UI
  Policy -.gates.- Focus
```

**Key idea:** KFM’s *knowledge graph mirrors the evidence graph* so you can traverse from a dataset → assets → pipeline run → source inputs → agents.  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🔗 Traceability model

### 🧩 Required identifiers (minimum viable trace)

| Concept | Required ID | Notes |
|---|---|---|
| Dataset | `kfm:dataset_id` | Canonical ID referenced across STAC/DCAT/PROV.  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| Sensitivity | `kfm:classification` | `public / internal / confidential / restricted` (example).  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| Pipeline run | `run_id` | Correlates telemetry, outputs, PROV activity.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| Config | `config_hash` | Enables replay / audit.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |
| Artifact checksum | `sha256:*` | Used for integrity + evidence manifests.  [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| Policy pack | `policy_pack_version` | Audit which rules were active.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| Correlation | `correlation_id` | Links logs/events/user actions.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) |

> 💡 For canonical hashing of JSON manifests, the project proposes using **RFC 8785 (JCS)** to compute a stable `canonical_digest`.  [oai_citation:22‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 🛰️ STAC / 📚 DCAT / 🧬 PROV must cross-link

KFM’s standards are **not isolated** — they must reference each other:
- STAC Items/Collections can point to PROV activity IDs or PROV file links.
- DCAT Datasets/Distributions point to STAC Collection URLs and PROV URLs.
- Neo4j mirrors these links as nodes/edges to keep the evidence graph queryable.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

KFM also defines **profiles** (STAC/DCAT/PROV) and versions them (e.g., PROV profile versioning).  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 🕸️ Graph traceability (semantic + provenance)

The knowledge graph supports:
- Historical ontologies like **CIDOC-CRM** and time modeling like **OWL-Time**
- Multi-hop reasoning and disambiguation for Focus Mode
- Traceable answers: search results are linked back to sources  [oai_citation:25‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

### 🤖 Focus Mode traceability rules (minimum)

Focus Mode uses hybrid retrieval (graph + GIS + semantic search) and must:
- 🔎 Link claims to evidence (datasets, docs, graph nodes)
- 🧾 Carry provenance for dynamic queries (e.g., “latest gauge reading at timestamp T”)  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧠 Avoid hallucinations by grounding to graph entities and evidence stores  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🛡️ Policy model

### 🧰 Policy Pack (OPA/Rego + Conftest)
KFM’s policy system spans:
- Data correctness (schema/fields/CRS, geometry validity expectations)
- Provenance completeness (e.g., deny if outputs changed without matching PROV)
- Security (secrets scanning, hardened adapters, pinned digests)
- Governance (FAIR/CARE, sovereignty, sensitivity)
- AI behavior constraints (cite evidence, uncertainty phrasing, role-based access)  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:29‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Example deny:**  
- `KFM-PROV-001: Processed data changed without matching PROV update.`  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### ✅ Where policies run

1) **CI gates (Conftest)**
- PRs fail if deny rules fire (metadata invalid, provenance missing, secrets detected, etc.).  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

2) **Runtime enforcement (OPA)**
- Before showing an AI answer, OPA can “allow/deny” based on context and content.
- Before accessing sensitive datasets, OPA can enforce role/permission.  [oai_citation:32‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

3) **Data intake and adapters**
- “No secrets in repos/pipelines.”
- Prefer parameterized queries; avoid SQL injection; enforce timeouts & resource limits.  [oai_citation:33‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧱 Provenance-first publishing rule
A core policy is:  
> **Policy Pack rule 3:** “Provenance-first publishing: all data must have provenance before graph/UI use.”  [oai_citation:34‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

This applies even to **streaming/real-time layers** (they must still be represented as evidence-bound, policy-governed data).  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🏛️ Governance + FAIR/CARE oversight

KFM governance includes:
- Ethical screening
- FAIR compliance checks
- Sustainability audit
- Accessibility review
- Council approval (for high-stakes additions)  [oai_citation:36‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

CARE examples that impact policy:
- **Authority to Control:** data owners/communities may require permissions/approvals recorded in metadata.
- **Responsibility:** log who ingested what (PROV agent fields, commit history).
- **Ethics:** extra review for AI-curated outputs, privacy, bias risks.  [oai_citation:37‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:38‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🧑‍💻 DevOps provenance: PR → PROV → Graph

KFM proposes integrating GitHub PR events into provenance:
- PRs as **PROV Activities**
- Commits as **PROV Entities**
- Authors/reviewers/bots as **PROV Agents**
- JSON-LD records ingested into Neo4j for queryable development lineage  [oai_citation:39‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

This enables questions like:
- “Which code version produced this dataset?”
- “Who reviewed the change that altered pipeline X?”  [oai_citation:40‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 📈 Audit + observability

KFM is instrumented for observability:
- Each pipeline run emits telemetry (timings, success/failure, data volumes)
- Includes `run_id` + `config_hash` so runs can be audited or replayed
- Logs significant events (user actions, ingestion steps) with correlation IDs for traceability
- Tracks AI telemetry (latency, usage, sustainability metrics)  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 🧪 MCP traceability matrix + experiment tracking
MCP recommends:
- Data changelogs
- Model registries (Model ID, training data version, code version, params, metrics)
- Config management as code
- Snapshots/checkpoints for reproducible experiments
- A structured `experiments/` layout with per-experiment artifacts  [oai_citation:42‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

### 🧹 Graph health checks (provenance completeness)
KFM proposes automated checks for:
- Orphaned STAC/PROV nodes (missing edges)
- Lag/recency checks for expected-updating sources
- “Hub node” anomaly detection (unexpected degree spikes)  [oai_citation:43‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📦 Artifact integrity + supply chain

### 🧾 OCI-based artifact registry (datasets/models/stories)
KFM proposes storing large artifacts using OCI registry patterns:
- Transfer with `oras`
- Signing with `cosign`
- Attach provenance (e.g., PROV JSON-LD as an attestation/referrer)
- Restrict access via registry permissions (CARE alignment)  [oai_citation:44‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🔒 SBOM + SLSA + Sigstore
Future proposals include tightening supply chain integrity via:
- SBOM generation
- SLSA practices for builds
- Sigstore signing/verification  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🔁 Workflows

### 1) 📥 Add / update a dataset (developer checklist)

**You must produce:**
- 🛰️ STAC Collection + Items (with `kfm:dataset_id`, `kfm:classification`, and provenance links)  [oai_citation:46‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 📚 DCAT Dataset + Distribution(s) referencing STAC + PROV  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧬 PROV JSON-LD describing entities/activities/agents and derivations  [oai_citation:48‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**You must pass:**
- ✅ schema validation (STAC/DCAT/PROV)
- 🛡️ Policy Pack (Conftest/OPA rules)
- 🔒 security scans (no secrets, pinned digests where applicable)  [oai_citation:49‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

**Common failure:** `KFM-PROV-001` when outputs change without PROV updates.  [oai_citation:50‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 2) 🛡️ Add / change a policy rule

1. Add/modify a Rego rule (OPA)  
2. Add tests (Conftest) so CI can prevent regressions  
3. Document the rule ID + intent + examples (deny messages)  
4. Bump policy pack version (auditable policy evolution)  [oai_citation:51‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

> 🔥 Goal: policies are not “shelfware”; they’re *provable* and *enforced*.  [oai_citation:52‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

### 3) 📝 Add a Story Node (evidence-first narrative)

KFM proposes treating Story Nodes like “queryable evidence artifacts”:
- Story includes a structured manifest (citations + checksums)
- PROV edges link story → datasets/documents used
- CI can validate citations resolve and manifests are complete  [oai_citation:53‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 Templates

> These are reference patterns. If a template file exists elsewhere in the repo, prefer the canonical version.

### 📄 `run_manifest.json` (pattern)
```json
{
  "run_id": "run-YYYYMMDDThhmmssZ-<shortid>",
  "pipeline": "kfm-<domain>-intake",
  "config_hash": "sha256:<...>",
  "inputs": [{"uri": "<source>", "digest": "sha256:<...>"}],
  "outputs": [{"uri": "<path-or-artifact>", "digest": "sha256:<...>"}],
  "canonical_digest": "sha256:<JCS-RFC8785-of-this-manifest>",
  "policy_pack": {"version": "v<...>", "digest": "sha256:<...>"},
  "evidence": {
    "stac": "<stac-collection-or-item-id>",
    "dcat": "<dcat-dataset-id>",
    "prov_activity": "<prov-activity-id>"
  }
}
```
📌 Canonical hashing guidance: RFC 8785 (JCS) for stable digests.  [oai_citation:54‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧬 PROV activity skeleton (pattern)
```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@id": "prov:kfm:activity:<run_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": "YYYY-MM-DDThh:mm:ssZ",
  "prov:endedAtTime": "YYYY-MM-DDThh:mm:ssZ",
  "prov:used": ["prov:kfm:entity:<input_1>", "prov:kfm:entity:<input_2>"],
  "prov:wasAssociatedWith": ["prov:kfm:agent:<user_or_ci_bot>"],
  "prov:generated": ["prov:kfm:entity:<output_dataset>"]
}
```
PROV core concepts (entities, activities, agents, and relationships) are central to KFM auditing.  [oai_citation:55‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧾 Story evidence manifest (pattern)
```yaml
story_id: story:<slug>
title: "<human title>"
evidence:
  - type: dataset
    id: "<kfm:dataset_id>"
    uri: "data/stac/<...>.json"
    checksum: "sha256:<...>"
  - type: document
    uri: "docs/<...>.md"
    checksum: "sha256:<...>"
prov:
  wasAssociatedWith:
    - agent: "human:<name>"
    - agent: "ai:<model_or_system>"   # if AI-drafted
```
Structured evidence manifests enable graph queries like “Which stories used this dataset?” and allow CI to validate citations.  [oai_citation:56‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📚 Glossary

- **MCP**: Master Coder Protocol (scientific method + reproducibility + documentation-first).  [oai_citation:57‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- **Evidence Triplet**: **STAC + DCAT + PROV** required for publishable datasets.  [oai_citation:58‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **STAC**: Geospatial catalog standard for items/collections + assets; KFM uses profiles and cross-links provenance.  [oai_citation:59‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **DCAT**: Dataset discovery metadata; links to STAC distributions and PROV lineage.  [oai_citation:60‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **PROV / PROV-O**: Provenance standard describing entities/activities/agents and derivations.  [oai_citation:61‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **OPA (Rego)**: Policy engine used for CI and runtime authorization/validation.  [oai_citation:62‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- **Conftest**: Tooling to apply OPA policies to repo artifacts in CI.  [oai_citation:63‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- **FAIR + CARE**: Governance principles including sovereignty and ethical constraints.  [oai_citation:64‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **OCI artifacts / cosign / oras**: Proposed artifact storage and signing approach for provenance + integrity.  [oai_citation:65‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **SBOM / SLSA / Sigstore**: Supply chain integrity practices proposed in future roadmap.  [oai_citation:66‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

---

## 📎 Source library

> These project files informed this documentation (design + governance + implementation references).

### 🧠 KFM core system docs
- 🧭 KFM AI System Overview  [oai_citation:67‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🧱 KFM Comprehensive Architecture, Features, and Design  [oai_citation:68‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 📘 KFM Comprehensive Technical Documentation  [oai_citation:69‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 🖥️ KFM Comprehensive UI System Overview  [oai_citation:70‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 📚 KFM Data Intake – Technical & Design Guide  [oai_citation:71‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🌟 Latest Ideas & Future Proposals  [oai_citation:72‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

### 🧩 MCP + governance + design critique
- 🧪 Scientific Method / Research / Master Coder Protocol Documentation  [oai_citation:73‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
- 🧾 Design Audit – Gaps and Enhancement Opportunities  [oai_citation:74‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)  
- 🗺️ Open-Source Geospatial Historical Mapping Hub Design  [oai_citation:75‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  

### 💡 Idea banks (policies, provenance, artifact integrity)
- 💡 Innovative Concepts to Evolve KFM  [oai_citation:76‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- 💡 Additional Project Ideas / Document Refinement  [oai_citation:77‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### 🧾 Docs standards + authoring references
- 🧾 MARKDOWN_GUIDE_v13  [oai_citation:78‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- 📝 Comprehensive MARKDOWN Guide (doc)  [oai_citation:79‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)  

### 📚 Technical reference library (implementation help)
- 🛰️ Python Geospatial Analysis Cookbook  [oai_citation:80‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  
- 📊 Data Mining Concepts & Applications  [oai_citation:81‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

### 🗂️ PDF portfolios (open in Acrobat if needed)
- 🤖 AI Concepts & more (PDF portfolio)  [oai_citation:82‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🗺️ Maps / Google Maps / Virtual Worlds / WebGL (PDF portfolio)  [oai_citation:83‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🧰 Various programming languages & resources (PDF portfolio)  [oai_citation:84‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- 🧮 Data Management / Theories / Architectures / Bayesian Methods (PDF portfolio)  [oai_citation:85‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  

---
🧡 If you’re adding something new and you’re unsure how to make it traceable: **start at STAC/DCAT/PROV, then enforce with Policy Pack, then mirror to Neo4j.**  [oai_citation:86‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
