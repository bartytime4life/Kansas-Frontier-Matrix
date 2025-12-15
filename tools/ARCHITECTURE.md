---
title: "🛠️ Kansas Frontier Matrix — Tools Platform Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ARCHITECTURE.md"
version: "v11.2.3"
last_updated: "2025-12-15"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:tools-architecture-v11.2.3"
semantic_document_id: "kfm-doc-tools-platform-architecture"
event_source_id: "ledger:tools/ARCHITECTURE.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/tools-architecture-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-platform-architecture"
role: "architecture"
category: "Tools · Platform · Architecture"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public Document"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"

json_schema_ref: "../schemas/json/tools-readme.schema.json"
shape_schema_ref: "../schemas/shacl/tools-readme-shape.ttl"

provenance_chain:
  - "tools/ARCHITECTURE.md@v11.2.2"
  - "tools/ARCHITECTURE.md@v11.0.0"
  - "tools/ARCHITECTURE.md@v10.4.0"
  - "tools/ARCHITECTURE.md@v10.3.2"
  - "tools/ARCHITECTURE.md@v10.3.1"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "6 months"
sunset_policy: "Superseded upon next major tools-platform architecture update"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Tools Platform Architecture (v11)**  
`tools/ARCHITECTURE.md`

**Purpose**  
Define the governed architecture for the **Tools Platform** (`tools/**`) that powers validation, governance, telemetry,
and AI assurance across the Kansas Frontier Matrix.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Governed%20Tools-gold"> ·
<img alt="License MIT" src="https://img.shields.io/badge/License-MIT-green"> ·
<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blue"> ·
<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-blue">

</div>

---

## 📘 1. Overview

The Tools Platform is the **governance-first** execution layer that makes KFM reproducible and auditable:

- **Deterministic**: given the same inputs + config, tools must produce the same outputs.
- **Config-driven**: tools run from explicit configs; configs are snapshotted into run artifacts.
- **Idempotent**: re-running a tool should not duplicate ledger entries or corrupt derived outputs.
- **Evidence-led**: tools must not invent provenance, licenses, sources, or relationships.
- **FAIR+CARE enforced**: publication, automation, and AI usage are gated by policy and audit.
- **Release-grade**: every governed output can be tied to a release manifest, SBOM, and telemetry record.

This document describes the architecture of `tools/**` and its integration boundaries with:

- `data/**` (raw/work/processed/stac + source catalogs)
- `schemas/**` (JSON Schema, SHACL, telemetry shapes)
- `src/**` (ETL, graph, and domain logic)
- `web/**` (frontend build inputs; never reads raw source files directly)
- `mcp/**` (run logs, experiments, model cards, reproducibility traces)
- `.github/**` (CI orchestration invoking tools)
- `releases/**` (versioned manifests, SBOMs, telemetry bundles)

---

## 🗂️ 2. Directory Layout

### 2.1 Tools Platform layout (canonical `tools/**`)

~~~text
tools/                                    # Tools Platform root (governed automation)
├── 📄 README.md                          # Tools index (operator entrypoint)
├── 🧱 ARCHITECTURE.md                    # This architecture specification
│
├── 🤖 ai/                                # AI assurance & Focus Mode audits
│   ├── 📁 drift/                         # Drift & semantic shift (model + narrative)
│   └── 📄 README.md                      # AI assurance overview (if present)
│
├── ⚙️ ci/                                # CI helper scripts & local CI mirrors
│   └── 📄 README.md                      # CI helper documentation (if present)
│
├── 💻 cli/                               # Operator-facing CLI interface (stable boundary)
│   └── 📄 README.md                      # CLI usage and command registry (if present)
│
├── 🏛 governance/                         # Governance sync, ledgers, certification
│   └── 📄 README.md                      # Governance tool docs (if present)
│
├── 📡 telemetry/                         # Observability + energy/carbon + run metrics
│   └── 📄 README.md                      # Telemetry tool docs (if present)
│
└── ✅ validation/                        # Schema, STAC/DCAT, FAIR+CARE validators
    └── 📄 README.md                      # Validation suite registry (authoritative)
~~~

### 2.2 Adjacent integration points (non-`tools/**`, but architecture-relevant)

~~~text
.github/workflows/                         # CI workflows that invoke tools (gates & releases)
docs/                                      # Standards, governance, and long-form documentation
data/                                      # Raw/work/processed datasets + STAC + source catalogs
schemas/                                   # JSON Schema, SHACL shapes, telemetry schema versions
src/                                       # ETL, graph, and domain logic (tools operate on outputs)
tests/                                     # Integration tests + reproducibility checks (tool-aware)
releases/                                  # Versioned manifests, SBOMs, telemetry bundles
mcp/                                       # Runs, experiments, model_cards, provenance traces
web/                                       # Frontend (consumes APIs or published artifacts only)
~~~

---

## 🧭 3. Context

### 3.1 Where `tools/**` sits in the KFM pipeline

KFM’s core pipeline is:

~~~text
ETL → Catalogs (STAC/DCAT/PROV) → Graph → API Boundary → Frontend → Story Nodes → Focus Mode
~~~

`tools/**` is the enforcement layer that makes the pipeline:

- **safe to automate** (governance gates),
- **safe to publish** (FAIR+CARE + licensing),
- **safe to reason over** (provenance + explainability),
- **safe to operate** (telemetry + integrity).

### 3.2 Repository-as-system reality

The repository contains multiple architecture documents. This file is scoped only to tooling, and must remain consistent with:

- `ARCHITECTURE.md` (repo-wide architecture)
- `data/ARCHITECTURE.md` (data lifecycle architecture)
- `src/ARCHITECTURE.md` (pipeline + graph implementation architecture)
- `web/ARCHITECTURE.md` (frontend consumption rules)
- `.github/ARCHITECTURE.md` (CI orchestration and enforcement)
- `tests/ARCHITECTURE.md` (validation and reproducibility expectations)
- `docs/ARCHITECTURE.md` (documentation system behavior)

---

## 🗺️ 4. Diagrams

### 4.1 Tools Platform execution flow (governance-first)

~~~mermaid
flowchart TD
  A["Operator / CI Trigger"] --> B["tools/cli\n(stable interface)"]
  B --> C["tools/validation\n(schema + FAIR+CARE gates)"]
  C --> D["tools/governance\n(PROV + ledgers + certification)"]
  D --> E["tools/telemetry\n(run metrics + energy/carbon)"]
  E --> F["releases/<version>/\n(manifest + SBOM + telemetry bundle)"]
~~~

### 4.2 Integration boundaries (who reads what)

~~~mermaid
flowchart LR
  subgraph Repo["Kansas Frontier Matrix Monorepo"]
    DATA["data/**\n(raw/work/processed/stac)"]
    SCHEMAS["schemas/**\n(JSON Schema + SHACL + telemetry)"]
    SRC["src/**\n(ETL + graph + domain)"]
    TOOLS["tools/**\n(validation + governance + telemetry + AI)"]
    MCP["mcp/**\n(runs + experiments + model_cards)"]
    RELEASES["releases/**\n(versioned artifacts)"]
    WEB["web/**\n(frontend)"]
  end

  TOOLS --> DATA
  TOOLS --> SCHEMAS
  TOOLS --> MCP
  TOOLS --> RELEASES

  SRC --> DATA
  SRC --> SCHEMAS

  WEB --> RELEASES
  WEB --> SRC
~~~

---

## 🧠 5. Story Node & Focus Mode Integration

### 5.1 What tools must guarantee for narrative safety

Tools must make it possible to trace every narrative claim to governed artifacts:

- Story Nodes must link to:
  - datasets (STAC/DCAT references),
  - evidence (documents, records, scans),
  - provenance (PROV activities and agents),
  - governance decisions (certification outcomes and constraints).

Tools must prevent AI from:

- altering normative requirements,
- fabricating provenance,
- inventing licensing status,
- overriding sovereignty protections,
- creating unsourced narratives.

### 5.2 Where Focus Mode safety hooks live

- **Validation** (schema + policy): blocks malformed or non-compliant Story Nodes.
- **Governance** (ledger + provenance): ensures evidence relationships are real and queryable.
- **AI assurance** (drift + grounding audits): detects semantic drift and narrative hallucination risk.
- **Telemetry**: records audit outcomes and system impact (including sustainability metrics).

Recommended doc references (repo-relative):

- `tools/validation/README.md`
- `tools/ai/drift/README.md`
- `docs/standards/faircare/FAIRCARE-GUIDE.md`
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🧪 6. Validation & CI/CD

### 6.1 CI orchestration model

CI workflows live under `.github/workflows/` and invoke `tools/**` to enforce gates:

- docs gates (KFM-MDP structure + metadata rules),
- schema gates (JSON Schema + SHACL),
- catalog gates (STAC/DCAT checks),
- provenance + integrity gates (checksums + manifests),
- security gates (secret scan + PII scan + supply-chain checks).

`tools/ci/` exists to hold reusable CI helper logic (scripts, config templates, local mirrors),
not to replace `.github/workflows/`.

### 6.2 Minimum gate profiles expected for governed merges

The baseline checks that must be satisfied before promotion or release:

- **markdown-lint**
- **schema-lint**
- **footer-check**
- **accessibility-check**
- **diagram-check**
- **metadata-check**
- **provenance-check**
- **secret-scan**
- **pii-scan**

### 6.3 Local operator workflow (deterministic-first)

Tools should support a local workflow that mirrors CI:

- run validation against a dataset subtree
- run governance sync for the changed artifacts
- emit telemetry + run logs under `mcp/runs/<run_id>/`
- optionally generate (or dry-run) release artifacts under `releases/<version>/`

Conventions (normative):

- Every tool supports:
  - `--config <path>`
  - `--run-id <id>`
  - `--out <dir>`
  - `--format json|human`
  - `--dry-run` (where mutations are possible)

---

## 📦 7. Data & Metadata

### 7.1 Data lifecycle conventions (what tools enforce)

Tools enforce these lifecycle rules:

- **Raw inputs** remain immutable (never edited in place).
- **Work** is for intermediate derivations (replayable).
- **Processed** is publishable and schema-validated.
- **Catalogs** (STAC/DCAT) are mandatory for introduced datasets.
- **Checksums** and **manifests** are required for integrity and reproducibility.

Repository directories used by this lifecycle typically include:

- `data/raw/`
- `data/work/`
- `data/processed/`
- `data/stac/`
- `data/sources/` (source catalogs / acquisition manifests)
- `data/checksums/` (integrity registries)
- `data/reports/` (audits, FAIR+CARE outputs, certification results)

### 7.2 Run logs, experiments, and model documentation

`mcp/**` is the governed location for reproducibility artifacts:

- `mcp/runs/<run_id>/`  
  - tool run logs, config snapshots, derived checks, telemetry fragments
- `mcp/experiments/<exp_id>/`  
  - research or evaluation outputs (never silently promoted)
- `mcp/model_cards/<model_id>.md`  
  - model cards (required for AI workflows that ship)

Tools must never write derived artifacts into `src/**`.

---

## 🌐 8. STAC, DCAT & PROV Alignment

### 8.1 STAC (catalog interoperability)

Tools validate and/or generate STAC artifacts under `data/stac/`:

- collections and items with stable IDs
- linked assets with correct media types and hrefs
- spatial/temporal extents consistent with dataset contents

### 8.2 DCAT (publication metadata)

Tools validate DCAT-compatible metadata describing:

- dataset identity and description
- license/rights and publisher/creator
- temporal and spatial coverage
- distributions (download links or internal artifact references)

### 8.3 PROV (lineage as a first-class output)

Tools ensure provenance is queryable and persistent:

- **Entities**: raw inputs, processed outputs, docs, models
- **Activities**: ETL runs, validation runs, governance audits
- **Agents**: scripts, maintainers, CI systems

Minimum linkage expectations:

- `prov:used`
- `prov:wasGeneratedBy`
- `prov:wasDerivedFrom`
- `prov:wasAssociatedWith`

---

## 🧱 9. Architecture

### 9.1 Layer responsibilities (normative)

**CLI layer (`tools/cli/`)**
- Stable operator boundary.
- Converts human intent → explicit configs + tool invocations.
- Must support reproducible reruns (same run config).

**Validation layer (`tools/validation/`)**
- Schema validation (JSON Schema + SHACL) for governed artifacts.
- Catalog validation (STAC/DCAT).
- FAIR+CARE policy validation (licensing, sensitivity, sovereignty rules).
- Blocks promotion on failure.

**Governance layer (`tools/governance/`)**
- Writes and synchronizes append-only ledgers.
- Ensures provenance completeness (no orphan datasets).
- Produces certification outcomes and governance records.

**Telemetry layer (`tools/telemetry/`)**
- Captures run-level metrics:
  - timing, counts, failures, warnings
  - energy/carbon estimates (as configured)
  - compliance states and gate decisions
- Emits machine-validated telemetry payloads.

**AI assurance layer (`tools/ai/`)**
- Audits Focus Mode narratives for grounding and governance compliance.
- Drift monitoring for models and narrative outputs (`tools/ai/drift/`).
- Produces “safe to use” vs “blocked” statuses for AI assets.

**CI helper layer (`tools/ci/`)**
- Reusable scripts/config templates used by `.github/workflows/`.
- Local mirrors for CI checks to reduce CI-only failures.

### 9.2 Common I/O contract for tools

All tools must treat outputs as governed artifacts:

- Write outputs to **explicit paths** (no implicit global state).
- Emit:
  - a machine-readable JSON result
  - a summary suitable for CI logs
  - an exit code with stable meaning

Recommended exit code conventions:

- `0` success (no blocking issues)
- `2` success-with-warnings (non-blocking, but recorded)
- `10` validation failed (blocking)
- `20` governance failed (blocking)
- `30` integrity/checksum failed (blocking)
- `40` policy/sovereignty failed (blocking)

### 9.3 Security, privacy, and sovereignty baselines

Tools must:

- never commit or log secrets,
- avoid logging raw PII or sensitive geometries,
- apply generalization/redaction rules where required,
- treat sovereignty policy as a hard constraint,
- produce audit trails explaining redaction and gating decisions.

---

## ⚖ FAIR+CARE & Governance

### 10.1 Enforcement model

FAIR+CARE is enforced as a pipeline gate:

- validation enforces structure and policy
- governance records the decision and its rationale
- telemetry records the fact of the decision (and impacts)

The governing documents for this enforcement are:

- `docs/standards/governance/ROOT-GOVERNANCE.md`
- `docs/standards/faircare/FAIRCARE-GUIDE.md`
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

### 10.2 “No silent promotion” rule

No dataset, catalog record, model artifact, or narrative output is promoted unless:

- schema checks pass,
- provenance is complete,
- licensing is compatible with intended use,
- sovereignty protections are satisfied,
- required telemetry is present.

---

## 🕰️ 11. Version History

| Version | Date       | Summary |
|--------:|-----------:|---------|
| v11.2.3 | 2025-12-15 | Aligned architecture to repo-wide structure (tools ↔ .github/workflows ↔ data/schemas/mcp/releases), added canonical run + artifact conventions, and clarified AI/Focus Mode governance boundaries. |
| v11.2.2 | 2025-11-27 | Prior v11 tools platform spec; baseline layering and governance-first flow. |
| v11.0.0 | 2025-11-24 | Initial v11 tools platform architecture. |
| v10.4.0 | 2025-11-15 | KFM-MDP v10.4 alignment; early governance + telemetry layering. |
| v10.3.2 | 2025-11-14 | Enhanced telemetry integration and FAIR+CARE flow. |
| v10.3.1 | 2025-11-13 | First formal tools architecture spec. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
**KFM Tools Platform Architecture v11** · Governed Tools · Deterministic Pipelines · Provenance-First

[⬅️ Tools Overview](README.md) ·
[📐 Repo Architecture](../ARCHITECTURE.md) ·
[✅ Validation Suite](validation/README.md) ·
[🛡 Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>