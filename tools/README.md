---
title: "🛠️ Kansas Frontier Matrix — Tools Directory Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:tools-readme-v11.2.6"
semantic_document_id: "kfm-doc-tools-platform-overview"
event_source_id: "ledger:tools/README.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../releases/v11.2.2/manifest.zip"
telemetry_ref: "../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/tools-architecture-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"
data_contract_ref: "../docs/contracts/data-contract-v3.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "tools-platform"
role: "architecture"
category: "Tools · Automation · Governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public Document"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/README.md@v10.3.1"
  - "tools/README.md@v10.3.2"
  - "tools/README.md@v10.4.0"
  - "tools/README.md@v11.0.0"
  - "tools/README.md@v11.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"

json_schema_ref: "../schemas/json/tools-readme.schema.json"
shape_schema_ref: "../schemas/shacl/tools-readme-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Review required every 6 months"
sunset_policy: "Superseded upon next major tools-platform release"
---

# 🛠️ Kansas Frontier Matrix — Tools Directory Architecture (v11)

`tools/README.md`

This document defines the **tools-platform layout and contracts** for `tools/**`:
validation gates, governance/provenance automation, telemetry/sustainability reporting, and operator CLIs.

## 📘 Overview

KFM tools are **repo-local, deterministic helpers** that support the full v11 pipeline:

ETL → validation → governance → telemetry → release packets → UI (Story Nodes / Focus Mode).

Non-negotiables:

- Reproducible: same inputs + same repo state ⇒ same outputs.
- Re-runnable: idempotent where practical (support `--dry-run` / safe replays).
- Machine-readable: JSON outputs + structured logs over ad-hoc text.
- Safe by default: no secrets in logs, no raw PII in reports, no precision leakage for sensitive locations.

## 🗂️ Directory Layout

Canonical structure (see `tools/ARCHITECTURE.md` for deep architecture):

~~~text
tools/
├── 📄 README.md
├── 📄 ARCHITECTURE.md
│
├── 🤖 ai/
│   ├── 📄 focus_audit.py
│   ├── 📄 bias_check.py
│   └── 📄 drift_monitor.py
│
├── ⚙️ ci/
│   ├── 📄 docs_validate.yml
│   ├── 📄 checksum_verify.yml
│   └── 📄 site_deploy.yml
│
├── 💻 cli/
│   ├── 📄 kfm_cli.py
│   └── 📄 metadata_manager.py
│
├── ⚖️ governance/
│   ├── 📄 governance_sync.py
│   ├── 📄 ledger_update.py
│   └── 📄 certification_audit.py
│
├── 📡 telemetry/
│   ├── 📄 telemetry_collector.py
│   ├── 📄 performance_analyzer.py
│   └── 📄 sustainability_reporter.py
│
└── ✅ validation/
    ├── 📄 faircare_validator.py
    ├── 📄 schema_check.py
    └── 📄 ai_explainability_audit.py
~~~

Notes:

- CI workflows live in `.github/workflows/`; `tools/ci/` holds reusable helpers and checks.
- Tools should not write into `src/` or `web/`. Outputs belong in `data/**`, `docs/reports/**`, or `releases/**`.

## 🧭 Context

High-level toolchain flow:

~~~text
Trigger (CLI / CI)
  → tools/validation (schema · STAC/DCAT · FAIR+CARE · sovereignty)
    → tools/governance (append-only ledgers · certification decisions)
      → tools/telemetry (performance + sustainability signals)
        → releases/vX.Y.Z (SBOM · manifest · telemetry slices)
~~~

Typical entrypoints:

- Operator actions: `tools/cli/kfm_cli.py`
- Merge gates: `tools/validation/*`
- Provenance writes: `tools/governance/*`
- Metrics aggregation: `tools/telemetry/*`

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["CI / CLI Trigger"] --> B["✅ tools/validation"]
  B --> C["⚖️ tools/governance"]
  C --> D["📡 tools/telemetry"]
  D --> E["📦 releases/vX.Y.Z"]
~~~

## 🧪 Validation & CI/CD

The validation layer is expected to block promotion/merge when:

- Schemas fail (JSON/YAML, telemetry payloads, Story Node shapes).
- STAC/DCAT/PROV requirements are missing for publishable assets.
- FAIR+CARE or sovereignty constraints are violated.
- Secret/PII scans detect prohibited content.

Common report targets (repo-wide):

- `data/reports/fair/**`
- `data/reports/audit/**`

## 📦 Data & Metadata

Canonical ledgers referenced by tooling:

- `data/reports/audit/data_provenance_ledger.json`
- `data/reports/audit/archive_integrity_log.json`

Telemetry aggregation targets:

- `releases/v11.2.2/tools-telemetry.json` (release packet slice, when generated)
- `docs/reports/telemetry/tools-*.json` (human-facing summaries)

Retention rule of thumb:

- Ledgers and release manifests are statement-of-record (keep).
- Staging bundles and raw telemetry are rotatable once summarized into governed artifacts.

## 🕰 Version History

| Version | Date       | Summary |
|--------:|-----------:|---------|
| v11.2.6 | 2025-12-15 | Updated metadata to KFM-MDP v11.2.6; aligned layout + contracts to `tools/ARCHITECTURE.md`; clarified output locations and gating expectations. |
| v11.2.2 | 2025-11-27 | Tools platform v11.2.2 baseline (architecture + directory layout + governance/telemetry framing). |
| v11.0.0 | 2025-11-24 | Initial v11 tools platform documentation. |
| v10.4.0 | 2025-11-15 | v10 tools architecture (pre-v11 contracts). |
| v10.3.2 | 2025-11-14 | Enhanced telemetry integration and FAIR+CARE flow. |
| v10.3.1 | 2025-11-13 | Initial tools overview draft. |