# 📐 Policy Schemas (dev_prov)

<kbd>MCP</kbd> <kbd>dev_prov</kbd> <kbd>Policy Pack</kbd> <kbd>OPA · Conftest</kbd> <kbd>JSON Schema</kbd> <kbd>STAC · DCAT · PROV</kbd> <kbd>FAIR + CARE</kbd> <kbd>Evidence-first</kbd>

📍 **You are here:** `mcp/dev_prov/policies/schemas/`

This folder contains **schema contracts** used to validate **development provenance artifacts** and **governance metadata** *before* they get evaluated by policies (CI) or accepted into the platform’s catalogs/graph/runtime.

KFM’s architecture is explicitly **contract-first** and **provenance-first**: datasets and outputs must ship with structured metadata + lineage (STAC/DCAT/PROV), and automated policy gates can fail a change if required evidence/provenance is missing or malformed. 🧾⛓  [oai_citation:0‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Why schemas exist here (and why they’re “policy-adjacent”)

Policies (OPA/Rego) are strongest when they evaluate **known-good inputs**:

- **Schemas** guarantee *shape* (types, required fields, allowed enums).
- **Policies** guarantee *meaning* (e.g., “no dataset without a license”, “classification must propagate”, “AI outputs must include citations”).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

In KFM, these checks are designed to be **fail-closed**: if a required condition isn’t met, CI rejects the change instead of allowing “mystery layers” or unsourced content to sneak into the catalog/graph/UI. 🔒✅  [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗺️ Where schemas sit in the pipeline

```mermaid
flowchart LR
  A[🧑‍💻 PR / Data Commit] --> B[📐 Schema Validation]
  B --> C[🛡️ OPA/Rego Policy Pack via Conftest]
  C -->|pass| D[✅ Merge / Promote]
  C -->|deny| E[⛔ Fail-closed + actionable messages]

  D --> F[🗂️ Catalog Updates: STAC/DCAT]
  D --> G[⛓️ PROV Records: runs, PRs, AI outputs]
  F --> H[🧠 Graph ingest (Neo4j) + spatial (PostGIS)]
  G --> H
  H --> I[🧭 UI: provenance panels + citations]
```

- Metadata standards (STAC/DCAT/PROV) are treated as a **metadata backbone**, and KFM extends them with its own **profiles** (versioned).  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Provenance is used both for **datasets** and for **DevOps events** (e.g., PR → PROV Activity).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:10‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  

---

## 📦 Schema families (what belongs in this folder)

> [!NOTE]
> Filenames vary by implementation. The list below is a **recommended contract surface** for `dev_prov` and policy evaluation, based on the project’s design docs (policy gates, provenance artifacts, evidence manifests, waivers, and governance controls).  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 1) 🗂 Catalog & Metadata Contracts (STAC · DCAT)

**Purpose:** ensure every dataset is discoverable + interoperable + licensed, and that KFM-required extensions exist.

Common schema targets:

- **STAC Item / Collection (KFM profile)**  
  Required KFM fields such as:
  - canonical dataset id (e.g., `kfm:dataset_id`)
  - classification label (e.g., `kfm:classification`)
  - links/pointers to provenance (PROV id or related record)  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **DCAT Dataset (KFM profile)**  
  Adds fields for sovereignty/sensitivity and catalog-level governance metadata.  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 2) ⛓ Provenance & Audit Contracts (PROV · Run Manifests · PR Provenance)

**Purpose:** ensure KFM never breaks chain-of-custody; provenance is mandatory for publishing and can be used for auditing + graph lineage.

Common schema targets:

- **PROV JSON-LD bundle (KFM profile)**  
  Captures activities, entities, agents, roles, timestamps, and relationships consistent with W3C PROV usage.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **Run Manifest (audit trail)**  
  A structured JSON document that captures who/what/when, sources, tool versions, and summary counts; generated per run and stored as an artifact for policy checks.  [oai_citation:17‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

- **PR → PROV integration record**  
  Encodes PR events as PROV Activities, commits as Entities, and authors/reviewers as Agents; supports invariants like “missing merge commit node = fail CI”.  [oai_citation:18‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

> [!IMPORTANT]
> Run manifests can be **self-fingerprinting**: canonicalize JSON (RFC 8785), compute SHA-256, then write it back into `canonical_digest` and reuse it as an idempotency key. This is ideal for immutable run identifiers and provenance joins.  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 3) 🧾 Evidence-First Narrative Contracts (Story Nodes · Evidence Manifests · Citations)

**Purpose:** formalize citations and evidence so stories and AI answers are auditable and machine-readable.

Common schema targets:

- **Story Node front-matter contract**  
  Includes an `evidence_manifest` pointer + compact provenance bundle references.  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

- **Evidence manifest schema (YAML/JSON)**  
  Enumerates sources with identifiers and integrity hints (checksums/line ranges/query params).  [oai_citation:22‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

- **Citations block schema**  
  A small, consistent structure for 3–7 line human-readable citations plus machine-readable entries.  [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 4) 🏛 Governance, Allowlists, and Waivers

**Purpose:** make governance explicit, inspectable, and automatable.

Common schema targets:

- **Governance “card” / allowlist file**  
  Enumerates allowed licenses (e.g., SPDX strings), required providers, sovereignty flags, and sensitivity rules used by policy-as-code.  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

- **Waivers file (`waivers.yml`)**  
  Supports time-bound exceptions by stable policy ID, including owner + justification + expiration.  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **Policy IDs as stable interfaces**  
  Policies may be organized into categories (Catalogs, Provenance, Sovereignty, Story, Security, etc.) with stable IDs like `KFM-CAT-001`, `KFM-PROV-001`, enabling auditable waivers.  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 5) 🔐 Sensitivity, Classification, and Cultural Protocols

**Purpose:** ensure ethics (CARE) and sensitive-data rules are enforced structurally *and* propagated through derivations.

Schema targets often include:

- **classification** (public/internal/confidential…)  
- **sensitivity markers** (sacred sites, private land stations, vulnerable species, etc.)  
- **sovereignty & cultural protocol tags** (Traditional Knowledge / TK labels, community-specific access rules)  [oai_citation:27‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

KFM design notes also include sensitivity-aware handling patterns like coordinate rounding/generalization and role-based visibility. 🧭🔒  [oai_citation:28‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:29‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 6) 🧪 QA & Health-Check Contracts (Graph + Data Reliability)

**Purpose:** treat data-layer reliability like CI reliability.

A “schema contract” can define expected property types/presence for critical node classes, enabling automated drift detection.  [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 7) 🧰 Supply-Chain & Attestation Reference Contracts (optional but aligned)

**Purpose:** attach verifiable provenance to code/data artifacts.

KFM proposes attaching SBOMs and SLSA attestations to automated PRs and using transparency logs for verification. These can be represented as **references** in your schema layer (rather than embedding full SBOM formats).  [oai_citation:31‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:32‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## ✅ Validation workflow

### Local (developer) validation 🧑‍🔧

You can validate artifacts with common schema tooling (choose what your stack already uses):

```bash
# Example with a JSON Schema validator (Node)
npx ajv-cli validate -s schemas/<schema>.schema.json -d <artifact>.json

# Example with Python
python -m jsonschema -i <artifact>.json schemas/<schema>.schema.json
```

> [!TIP]
> Keep schema validation fast and deterministic so it can run on every PR and pre-commit.

### CI (policy gates) 🧱

KFM’s policy pack model uses CI to run schema conformance checks + OPA/Rego checks via Conftest, producing clear deny messages and blocking merges on violations.  [oai_citation:33‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:34‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

#### 🧠 Runtime validation (Focus Mode + API)

KFM design calls out runtime policy checks (OPA) for AI outputs and sensitive content rules. A key rule: **if the AI cannot provide a source, it is not allowed to answer**—enforced both in programming and via runtime checks. 🧾⛔  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:36‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

Also: AI outputs and key decisions are logged in an **immutable governance ledger** with compliance metadata and provenance.  [oai_citation:37‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧱 Schema design conventions (recommended)

### 📌 1) Every artifact should be identifiable + versioned

Minimum contract traits that make policy evaluation and graph joins sane:

- `id` (stable, globally unique — use `urn:` patterns if needed)
- `schema_version` (semver for the schema itself)
- `created_at` / `generated_at`
- `generated_by` (agent/tool id)
- `inputs[]` and `outputs[]` (with digests and/or dataset IDs)

This aligns with KFM’s emphasis on versioned metadata profiles and reproducible audit trails.  [oai_citation:38‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:39‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 🔗 2) Cross-link STAC/DCAT/PROV explicitly

Recommended linking patterns:

- STAC → PROV activity id (or resolvable reference)
- DCAT → STAC Collection + PROV record references
- PROV → stable dataset ids used in catalog nodes

This “connected standards” approach keeps catalogs discoverable while preserving lineage.  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🔐 3) Classification propagation is non-negotiable

KFM policy concepts include ensuring outputs do not downgrade restrictions relative to inputs; schema fields should support this propagation cleanly (e.g., `classification`, `sensitivity`, `sovereignty`).  [oai_citation:41‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:42‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 🧾 4) Evidence manifests should be verifiable

Evidence manifests are intended to act like “receipts”:

- machine-readable list of evidence items
- integrity hints (checksum/digest)
- optional extraction coordinates (line range, query parameters)
- optional transformation notes

This makes story auditing and impact analysis possible (e.g., “which stories relied on data that changed?”).  [oai_citation:43‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 🔒 5) Prefer “strict by default” schemas

- `additionalProperties: false` for high-risk artifacts (policies/waivers/governance)
- allow extension points using `definitions/$defs` and a namespaced `extensions` object
- keep enums centralized (licenses, classifications, policy IDs)

This supports fail-closed governance and deliberate extension via PR.  [oai_citation:44‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧩 Recommended schema “envelope” for OPA inputs

When evaluating with OPA/Conftest, it helps to normalize inputs into a single shape:

```json
{
  "subject": { "kind": "dataset|story|run|doc", "id": "urn:kfm:..." },
  "action": "publish|merge|serve|export",
  "actor": { "id": "user|bot", "role": "maintainer|contributor|viewer" },
  "context": {
    "classification": "public|internal|confidential",
    "sensitivity": ["..."],
    "policy_version": "..."
  },
  "artifacts": [
    { "path": "data/catalog/...", "schema": "stac-item", "digest": "sha256:..." }
  ]
}
```

OPA can then enforce consistent rules across many artifact types (catalogs, provenance, docs, AI outputs).  [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧾 Examples (minimal, illustrative)

### Story Node front-matter (evidence-first narrative)

```yaml
id: "urn:kfm:story:84"
title: "Flood of 1908"
evidence_manifest: "EM-84.yaml"
prov_bundle_ref: "urn:kfm:prov:bundle:story:84"
citations:
  - "[1] 1908 Newspaper Archive (excerpt hash: …)"
  - "[2] USGS gauge dataset (query: …)"
```

This mirrors the “Story Nodes with Evidence Manifests” concept: human citations + machine manifest + PROV linkage.  [oai_citation:46‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Run manifest (audit trail + idempotency)

```json
{
  "run_id": "urn:kfm:run:2025-01-02T100500Z:abcd",
  "run_time": "2025-01-02T10:05:00Z",
  "idempotency_key": "sha256:…",
  "canonical_digest": "sha256:…",
  "source_urls": [],
  "tool_versions": { "gdal": "x.y.z" },
  "summary_counts": { "in": 123, "out": 120, "errors": 0 }
}
```

Canonicalize then hash (RFC 8785) to make the manifest self-fingerprinting.  [oai_citation:47‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Waiver entry (time-bound exception)

```yaml
- policy_id: "KFM-CAT-001"
  scope: "data/catalog/datasets/example.json"
  expires_at: "2026-03-01"
  owner: "maintainer-handle"
  reason: "Upstream dataset license pending; tracking issue #123"
```

Waivers support transparency without weakening defaults.  [oai_citation:48‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🛠️ Adding or updating a schema (contributor checklist)

- [ ] Name it clearly: `<domain>.<artifact>.schema.json` (or `.yaml` if the artifact is YAML-first)
- [ ] Include `schema_version` and/or a versioned `$id` pattern (URNs are OK)
- [ ] Write at least one **golden test artifact** (valid) + one **deny test artifact** (invalid)
- [ ] Add/adjust policy rules only *after* schema is stable (schemas first → policies second)
- [ ] If a breaking change is necessary, bump major version and document migration notes
- [ ] If you need an exception, use **waivers** (time-bound) rather than silently loosening schemas

---

## ❓ FAQ

### “Why not just validate in code?”
Because schemas are:
- language-agnostic (works across services)
- easy to run in CI (fast gates)
- easy to audit (contract surface is visible in repo)
- directly compatible with policy-as-code workflows  [oai_citation:49‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### “Do schemas replace OPA policies?”
No. They’re complementary:
- Schema = **syntax**
- Policy = **semantics + governance invariants**  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 📚 Project sources that informed these schemas

> [!NOTE]
> Some files in this project are **PDF Portfolios** (they contain embedded documents) and may require exporting/expanding to view all contents.

### Core KFM design docs
- KFM Data Intake (standards, profiles, CI validation, policy gates)  [oai_citation:51‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- KFM Architecture, Features, and Design (STAC/DCAT/PROV backbone + metadata profile + CLI validation)  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- KFM AI System Overview (Policy Pack, runtime OPA checks, governance ledger)  [oai_citation:53‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- KFM UI System Overview (provenance-forward UX, system modularity)  [oai_citation:54‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- KFM Comprehensive Technical Documentation (contract-first, no “mystery layers”)  [oai_citation:55‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM Latest Ideas & Future Proposals (devops→PROV, attestations, standards alignment)  [oai_citation:56‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### Governance + policy evolution
- Additional Project Ideas (run manifest hashing, evidence manifests, OCI artifact concept, fail-closed gates)  [oai_citation:57‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Innovative Concepts to Evolve KFM (cultural protocols, TK labels, sensitivity-aware access)  [oai_citation:58‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

### Reference libraries (may be PDF portfolios)
- AI Concepts & more (portfolio)  [oai_citation:59‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Maps / Google Maps / Virtual Worlds / WebGL (portfolio)  [oai_citation:60‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Data Management / Architectures / Bayesian Methods (portfolio)  [oai_citation:61‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- Various programming languages & resources (portfolio)  [oai_citation:62‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

### Extra technical references present in project corpus
- Scientific Method + Research + MCP documentation  [oai_citation:63‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
- Data Mining concepts (privacy controls & risk framing)  [oai_citation:64‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- Open-source geospatial mapping hub design (MCP framing, geo stack references)  [oai_citation:65‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
- Python geospatial analysis cookbook (implementation patterns & logging ideas)  [oai_citation:66‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- Markdown governance + front-matter schema patterns  [oai_citation:67‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
