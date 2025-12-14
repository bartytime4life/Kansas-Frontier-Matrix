---
title: "🧬 Surficial Geology — Lineage & Provenance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/surficial-geology/lineage/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Overview"
header_profile: "standard"
footer_profile: "standard"
intent: "dataset-lineage"
role: "surficial-geology-lineage-index"
category: "Data · Provenance · FAIR+CARE"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 · Data & ETL pipeline events"

fair_category: "F1-A1-I1-R1"
care_label: "Variable — Dataset Dependent"
sensitivity: "Mixed"
sensitivity_level: "Variable"
public_exposure_risk: "Dataset-level"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:surficial-geology-lineage-readme:v11.2.6"
semantic_document_id: "kfm-doc-surficial-geology-lineage"
event_source_id: "ledger:data/surficial-geology/lineage/README.md"
immutability_status: "branch-live"

provenance_chain:
  - "data/surficial-geology/lineage/README.md@v11.2.6"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🧬 **Surficial Geology — Lineage & Provenance**  
`data/surficial-geology/lineage/README.md`

**Purpose**  
Define the **canonical structure, naming conventions, and safety rules** for provenance artifacts that document how Surficial Geology domain outputs are produced, validated, cataloged (STAC/DCAT), and made graph/Story-Node ready.

[⬅ Back to Surficial Geology](../README.md) ·
[📦 Data Overview](../../README.md) ·
[🗄️ Data Architecture](../../ARCHITECTURE.md)

</div>

---

## 📘 Overview

This folder contains **dataset- and run-level lineage artifacts** for the Surficial Geology domain.

It exists so that any published Surficial Geology artifact can be traced:

- from **outputs** (e.g., `data/processed/**` assets and their STAC/DCAT metadata),
- back to **inputs** (raw sources and upstream manifests),
- through the **process** (ETL configs, tools, environment, and validations),
- with **governance visibility** (license, sensitivity, CARE labels, sovereignty flags where applicable).

### What belongs here

- **Logical provenance** (PROV‑O / JSON‑LD): “what was used, what was produced, and why”.
- **Execution lineage** (OpenLineage events): “which job/run produced what, when”.
- **Run manifests**: lightweight, machine-readable “glue” that ties a run to:
  - input identifiers and checksums,
  - output identifiers and checksums,
  - pipeline code location and commit hash,
  - environment identifiers (container digest / lockfile hash),
  - validation report references.

### What MUST NOT be stored here

- Large binaries (COGs, GPKGs, tiles, etc.) — those belong in `data/raw/**` or `data/processed/**`.
- Secrets, tokens, credentials, private keys.
- Direct PII.
- High-precision sensitive coordinates when governance requires generalization/masking.

---

## 🗂️ Directory Layout

Canonical layout for `data/surficial-geology/lineage/`:

~~~text
📁 data/surficial-geology/lineage/
├── 📄 README.md                      # This file (lineage conventions & governance rules)
│
├── 📁 prov/                          # PROV-O JSON-LD bundles (logical provenance)
│   ├── 🧾 dataset--<kfm_id>--prov.jsonld
│   └── 🧾 run--<run_id>--prov.jsonld
│
├── 📁 openlineage/                   # OpenLineage events (execution-level lineage)
│   └── 🧾 <job_name>/
│       └── 🧾 <run_id>.json
│
├── 📁 manifests/                     # Run manifests (config/env pointers, inputs/outputs index)
│   └── 🧾 run--<run_id>.manifest.json
│
├── 📁 indexes/                       # Compact indexes for fast lookup (optional but recommended)
│   └── 🧾 lineage.index.json
│
└── 📁 notes/                         # Human-authored lineage notes (rare; no secrets/PII)
    └── 📝 <topic>.md
~~~

### Naming conventions (normative)

- `<kfm_id>` MUST be stable and deterministic (prefer `urn:kfm:dataset:surficial-geology:...`).
- `<run_id>` SHOULD be globally unique (e.g., ULID/UUID) and consistent across:
  - OpenLineage event files,
  - PROV run entities,
  - run manifest file name.
- File names MUST be lowercase where practical, with hyphen separators for tokens.

---

## 🧭 Context

This folder does **not** stand alone. It is designed to connect Surficial Geology work across the KFM data plane:

- **Inputs**
  - `data/raw/**` — immutable ingests of upstream source data
  - `data/sources/**` — source manifests, licensing notes, and provider metadata

- **Outputs**
  - `data/processed/**` — deterministic, analysis-ready artifacts used by the platform
  - `data/stac/**` — STAC Items/Collections describing the outputs (domain path may vary)
  - `data/dcat/**` — DCAT dataset records and distributions (JSON-LD)

- **Integrity + evidence**
  - `data/checksums/**` — digests used to verify artifacts haven’t changed unexpectedly
  - `data/reports/**` — validation outputs, QA/QC summaries, audits, and telemetry

- **Reproducibility records**
  - `mcp/runs/**` — run logs and config snapshots (referenced from manifests; not duplicated here)

- **Code + graph**
  - `src/pipelines/**` — ETL jobs that emit outputs and lineage artifacts
  - `src/graph/**` — ingest tooling that can load PROV-aligned lineage into Neo4j

---

## 🗺️ Diagrams

The lineage relationship model (conceptual):

~~~mermaid
flowchart TD
  A["sources + raw inputs"] --> B["ETL run (job/run_id)"]
  B --> C["processed outputs"]
  C --> D["STAC/DCAT catalogs"]
  B --> E["OpenLineage events"]
  B --> F["PROV-O bundles"]
  C --> G["checksums + validation reports"]
  D --> H["graph + Story Nodes + Focus Mode"]
~~~

This diagram is descriptive: exact implementation details live in pipeline contracts and validation tooling.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Published Surficial Geology assets SHOULD be referenced by STAC Items/Collections.
- STAC Items SHOULD link to provenance artifacts (e.g., via `links` entries) where appropriate.

### DCAT

- DCAT Dataset records SHOULD expose:
  - dataset identity (`dct:identifier` aligned with KFM stable IDs),
  - distributions aligned with STAC assets or canonical artifact locations,
  - license and access constraints.

### PROV‑O

- Each produced artifact is modeled as a `prov:Entity`.
- Each ETL (or curation) run is a `prov:Activity`.
- Humans, CI bots, and pipeline services are `prov:Agent`s.
- PROV bundles in `prov/` SHOULD be sufficient to answer:
  - “What inputs contributed to this output?”
  - “Which run generated this artifact?”
  - “Which validations were applied, and where are the reports?”

---

## 🧪 Validation & CI/CD

Lineage artifacts in this folder are expected to be **machine-checkable**.

Minimum expectations:

- **Schema validity**
  - `prov/*.jsonld` parses and conforms to the project’s PROV profile expectations.
  - `openlineage/**/*.json` is valid OpenLineage event JSON.
  - `manifests/*.json` conforms to the project’s run-manifest schema (if present).

- **Reference integrity**
  - Every referenced input/output path resolves to a real artifact (or a permitted DVC pointer).
  - Referenced checksums match the canonical checksum records.

- **Safety checks**
  - No secrets/tokens.
  - No obvious PII.
  - No restricted coordinate precision where governance requires masking.

Local tooling (discoverable in-repo):

- Validation utilities and helpers are expected under `tools/validation/**`.

---

## ⚖ FAIR+CARE & Governance

Surficial Geology is often publishable, but governance is **dataset-specific**:

- If a lineage record references a dataset flagged as sensitive or sovereign:
  - the lineage MUST NOT expose restricted details (including fine location precision),
  - and MUST preserve explicit usage constraints and stewardship references.

This README is a public-facing guide; it does not override dataset-level policies.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial lineage README for Surficial Geology domain; defines folder purpose, canonical layout, naming rules, and governance constraints. |

---

<div align="center">

🧬 **Surficial Geology — Lineage & Provenance (v11.2.6)**  
Provenance‑First · Deterministic · Audit‑Ready

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11

[⬅ Back to Surficial Geology](../README.md) ·  
[📦 Data Overview](../../README.md) ·  
[🗄️ Data Architecture](../../ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·  
[🛡️ Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

