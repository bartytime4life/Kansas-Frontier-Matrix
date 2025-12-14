---
title: "📦 Kansas Frontier Matrix — Data Directory Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/README.md"

version: "v11.2.4"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-readme:v11.2.4"
semantic_document_id: "kfm-doc-data-root"
event_source_id: "ledger:data/README.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../releases/v11.2.4/manifest.zip"
telemetry_ref: "../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-directory-v11.2.4.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "data-directory"
role: "repository-data-overview"
category: "Data · Metadata · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Mixed"
sensitivity_level: "Variable"
risk_category: "Low to Medium"
indigenous_rights_flag: true
redaction_required: false

machine_extractable: true
classification: "Public Document"
jurisdiction: "United States / Kansas"
accessibility_compliance: "WCAG 2.1 AA"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

prov_profile: "PROV-O Plan + KFM Data Lineage Profile"
openlineage_profile: "OpenLineage v2.5 · Data & ETL pipeline events"

provenance_chain:
  - "data/README.md@v11.2.4"
  - "data/README.md@v11.2.3"
  - "data/README.md@v11.2.2"
  - "data/README.md@v11.0.1"
  - "data/README.md@v11.0.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "hallucinated-datasets"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Data Directory Overview v11.2.4**  
`data/README.md`

**Purpose**  
Define the **canonical structure, lifecycle, and governance** of all datasets in the Kansas Frontier Matrix (KFM)—from raw external sources to fully validated, cataloged, graph‑integrated, and Story‑Node‑ready products. This document ties the data layout to **STAC/DCAT discovery, PROV‑O lineage, deterministic pipelines, and KFM‑MDP v11.2.6**.

<a href="../docs/standards/kfm_markdown_protocol_v11.2.6.md"><img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.6-blue" /></a>
<a href="../docs/standards/faircare/FAIRCARE-GUIDE.md"><img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" /></a>
<img src="https://img.shields.io/badge/Metadata-STAC_1.0.0_%7C_DCAT_3.0-informational" />
<img src="https://img.shields.io/badge/Lineage-PROV%E2%80%93O_%7C_OpenLineage-success" />
<a href="../LICENSE"><img src="https://img.shields.io/badge/License-CC--BY_4.0-green" /></a>

</div>

---

## 📘 Overview

The `data/` directory is the **root of the KFM data plane**, organized **by domain and stage**:

- Stage directories define the governed lifecycle: `raw/ → work/ → processed/`.
- Domain directories (e.g., `air-quality/`, `hydrology/`, `surficial-geology/`) hold domain context (docs, configs, mappings) and point into the stage directories and catalogs.
- `stac/` provides the canonical STAC catalog root for discovery and spatiotemporal search.
- Integrity, governance, and audit artifacts live alongside the data (`checksums/`, `reports/`, `archive/`, `updates/`).

Start here for deeper context and operational detail:

- `data/ARCHITECTURE.md`
- `../docs/pipelines/`
- `../tools/validation/`

---

## 🗂️ Directory Layout

Canonical, emoji‑rich layout for `data/` (KFM‑MDP `immediate-one-branch-with-descriptions-and-emojis` profile).

~~~text
📁 data/
├── 📄 README.md                      # This file (data plane overview, governance, contributor rules)
├── 📄 ARCHITECTURE.md                # Data-plane architecture notes (domain ↔ stage ↔ catalogs)
│
├── 📁 air-quality/                   # Domain package: air quality (metadata, configs, notes)
├── 📁 hydrology/                     # Domain package: hydrology (metadata, configs, notes)
├── 📁 surficial-geology/             # Domain package: surficial geology (metadata, configs, notes)
│
├── 📁 raw/                           # Immutable ingests (as-received or lossless re-encodes)
├── 📁 work/                          # Pipeline workspace (intermediates; reproducibility-aware)
├── 📁 processed/                     # Deterministic ETL outputs (analysis-ready)
│
├── 📁 stac/                          # STAC catalog root (Collections/Items referencing processed assets)
├── 📁 checksums/                     # Integrity digests (e.g., SHA-256 for key artifacts)
├── 📁 reports/                       # Validation, audit, and telemetry outputs
├── 📁 updates/                       # Incremental update payloads (deltas / hotfix inputs)
└── 📁 archive/                       # Retired datasets and snapshots (cold storage)
~~~

**Normative rules (data/ level):**

- Every documented directory under `data/` MUST contain its own `README.md` stating:
  - Purpose and scope,
  - Data steward / ownership,
  - Sensitivity and governance constraints,
  - Primary assets and expected schemas.
- Production‑grade datasets MUST be discoverable via catalog metadata:
  - STAC artifacts live under `data/stac/`,
  - DCAT records and data contracts live under `docs/data/`,
  - Provenance must be queryable (PROV‑O/OpenLineage references in metadata and/or run logs).

---

## 🧭 Context

`data/` lands in the KFM pipeline as the **data plane** feeding the rest of the stack:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → Frontend map/timeline → Story Nodes → Focus Mode

Key boundary rule: the frontend does **not** read `data/**` directly; it consumes APIs and catalog products.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  D["📁 <domain>/\nDomain context (docs, configs, mappings)"]
  R["📁 raw/\nImmutable ingests"]
  W["📁 work/\nCleaning · normalization · enrichment"]
  P["📁 processed/\nDeterministic ETL outputs"]
  S["📁 stac/\nSTAC Items & Collections"]
  C["📁 docs/data/\nDCAT records + data contracts"]
  K["📁 checksums/\nIntegrity digests"]
  T["📁 reports/\nValidation · audit · telemetry"]
  U["📁 updates/\nIncremental deltas"]

  D --> R
  R --> W
  W --> P
  U --> W

  P --> S
  P --> C

  S --> K
  C --> K

  K --> T
~~~

---

## 📦 Data & Metadata

### Lifecycle expectations

- **Raw (`data/raw/`)**  
  Immutable source materials. If assets are large, they may be tracked with large-file tooling (e.g., Git LFS and/or DVC), but the governing rule is: *raw must be reproducible and provenance-addressable.*

- **Work (`data/work/`)**  
  Intermediate artifacts used during ETL. If intermediates are required for reproducibility, they should be retained with clear notes; otherwise, pipelines should be able to regenerate them deterministically.

- **Processed (`data/processed/`)**  
  Analysis-ready products. These are the default assets referenced by `data/stac/` and downstream services.

- **Updates (`data/updates/`)**  
  Incremental change payloads (corrections, deltas, late-arriving data). Updates must be provenance-linked and replayable through the same deterministic pipeline contract.

- **Checksums (`data/checksums/`) and reports (`data/reports/`)**  
  Integrity and governance artifacts: checksums for tamper-evidence; reports for validation, audits, and telemetry.

### Contributor guidance

When adding or modifying data:

1. **Choose the right home**
   - Domain-specific documentation/config: `data/<domain>/`
   - Raw intake: `data/raw/`
   - Pipeline intermediates: `data/work/`
   - Final outputs: `data/processed/`
   - Catalog updates: `data/stac/` (and `docs/data/` for DCAT/data contracts)
2. **Record provenance and rights**
   - Capture source, license/rights, retrieval date, processing parameters, and any redaction/generalization steps.
3. **Keep outputs deterministic**
   - Prefer config-driven, replayable pipelines (no manual edits to processed outputs).
4. **Update catalogs**
   - Ensure new/updated processed assets are represented in STAC and mirrored in DCAT-compatible records.
5. **Document sensitivity**
   - If cultural heritage / Indigenous / sensitive ecology is involved, apply governance rules before public exposure.

---

## 🌐 STAC, DCAT & PROV Alignment

KFM uses complementary metadata layers:

- **STAC (`data/stac/`)**  
  Spatiotemporal discovery layer. STAC Items/Collections reference `data/processed/` assets (COGs, GeoParquet, GeoJSON, etc.) and expose temporal/spatial extents for filtering.

- **DCAT (`docs/data/`)**  
  Publishing/discovery layer for catalog portals and compliance. DCAT records should mirror STAC identifiers and expose distributions, licenses, access constraints, and steward roles.

- **PROV‑O / OpenLineage (`mcp/runs/` and/or provenance assets)**  
  Lineage layer. Every production dataset must be traceable to:
  - input sources (Entities),
  - the ETL run (Activity),
  - and the producing agent (Agent).

Rule of thumb: if a user can see a layer in the UI, they must be able to trace it back to STAC/DCAT and a provenance chain.

---

## 🧱 Architecture

This directory is intentionally designed so that:

- **Pipelines** live in `src/pipelines/` and operate on `data/raw/ → data/work/ → data/processed/`.
- **Catalogs** are first-class artifacts (STAC in `data/stac/`, DCAT + contracts in `docs/data/`).
- **Graph ingestion** (Neo4j) and API layers consume processed assets and catalog metadata, not ad-hoc files.

For architectural decisions and rationale, see `data/ARCHITECTURE.md` and `docs/architecture/`.

---

## 🧪 Validation & CI/CD

Data and metadata changes are gated by CI checks under `.github/workflows/` and reusable actions under `.github/actions/`.

Expected validation themes include:

- **Doc structure checks** (KFM‑MDP): front matter, heading registry, footer links, diagram fencing.
- **Metadata checks**: STAC validation, DCAT shape/schema checks, identifier stability.
- **Integrity checks**: checksum verification and manifest consistency (when producing a release packet).
- **Security and privacy**: secret scanning and PII scanning.
- **Governance**: FAIR+CARE labeling and sovereignty rules for sensitive datasets.

---

## 🧠 Story Node & Focus Mode Integration

Data products become narratively explorable when they can be bound to Story Nodes:

- A Story Node must reference datasets and evidence via stable identifiers (STAC/DCAT IDs, graph URNs).
- Narrative outputs must be evidence-led:
  - Facts: sourced and traceable,
  - Interpretation: clearly labeled as reasoning from facts,
  - Speculation: explicitly marked hypothetical (and usually avoided in governed outputs).

Focus Mode may summarize this document and associated dataset metadata, but must not invent datasets, provenance, or governance status.

---

## ⚖ FAIR+CARE & Governance

This repository operates under explicit governance constraints:

- **FAIR**: datasets must be findable (cataloged), accessible (documented), interoperable (standard schemas/CRS/ontologies), and reusable (licensed + provenance).
- **CARE**: authority, responsibility, and ethics must be explicit—especially for Indigenous and culturally sensitive content.
- **Sovereignty**: if data touches Indigenous lands, knowledge, or heritage:
  - consent and authority constraints apply,
  - masking/generalization may be required,
  - distribution and exposure rules must be enforced before publishing.

Authoritative governance references:

- `../docs/standards/governance/ROOT-GOVERNANCE.md`
- `../docs/standards/faircare/FAIRCARE-GUIDE.md`
- `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version  | Date       | Summary |
|---------:|------------|---------|
| v11.2.4  | 2025-12-14 | Updated directory layout to match current repo (domain packages + `updates/`); aligned headings and fences to KFM‑MDP v11.2.6; removed external/tool citations for commit-safe Markdown. |
| v11.2.3  | 2025-12-09 | Aligned with KFM‑MDP v11.2.5; expanded directory layout; integrated STAC/DCAT/PROV and telemetry references. |
| v11.2.2  | 2025-11-27 | Canonical directory layout; telemetry/schema paths wired; FAIR+CARE and checksum governance hardened. |
| v11.0.1  | 2025-11-19 | Rewritten with v11 fence rules; GitHub-safe layout; aligned initial data architecture with v11 stack. |
| v11.0.0  | 2025-11-19 | Initial v11 data directory documentation and lifecycle definition. |

---

<div align="center">

📦 **Kansas Frontier Matrix — Data Directory Overview v11.2.4**  
Data‑First · FAIR+CARE‑Governed · Provenance‑Aware  

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11.0  

[⬅ Back to Repository Root](../README.md) ·  
[📚 Data & Catalog Standards](../docs/data/README.md) ·  
[⚖ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
