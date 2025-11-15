---
title: "🤝 Kansas Frontier Matrix — Contribution Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "CONTRIBUTING.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/contributing-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Governance"
intent: "contributor-workflow"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed Dataset Classification"
sensitivity_level: "Contribution-dependent"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false
provenance_chain:
  - "CONTRIBUTING.md@v10.3.2"
  - "CONTRIBUTING.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "HowTo"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "schemas/json/contributing.schema.json"
shape_schema_ref: "schemas/shacl/contributing-shape.ttl"
doc_uuid: "urn:kfm:doc:contributing-v10.4.1"
semantic_document_id: "kfm-doc-contributing"
event_source_id: "ledger:CONTRIBUTING.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with strict controls"
ai_transform_permissions:
  - "summaries"
  - "a11y-adaptations"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "governance"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next contributor-guideline update"
---

<div align="center">

# 🤝 **Kansas Frontier Matrix — Contributor Guide**  
`CONTRIBUTING.md`

**Purpose:**  
Provide a unified, FAIR+CARE-governed, reproducible, ethical, and schema-aligned workflow for contributing to the  
Kansas Frontier Matrix (KFM).  
This guide ensures transparency, provenance integrity, CARE compliance, accessibility, and CI/CD validation across all
contributions.

</div>

---

# 📘 Introduction

Thank you for contributing to the **Kansas Frontier Matrix**.  
All contributions must follow KFM’s architectural, ethical, accessibility, and governance standards:

- **MCP-DL v6.3**  
- **KFM-MDP v10.4**  
- **FAIR+CARE**  
- **WCAG 2.1 AA**  
- **CIDOC / PROV-O / OWL-Time alignment**  
- **Version pinning & provenance logging**  

---

# 🧱 Contribution Types

KFM accepts contributions in:

- Code (web, pipelines, tools, validation, governance)  
- Documentation (architecture, standards, analyses, guides)  
- Data (datasets, metadata, lineage, STAC/DCAT entries)  
- Testing (unit/integration/E2E/schema/A11y)  
- Governance & CARE metadata improvements  

---

# 🛠 Environment Setup

## Clone

~~~bash
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix
~~~

## Install dependencies

~~~bash
npm install                     # Web platform & frontend tooling
pip install -r requirements.txt # Backend ETL & tools
~~~

## Recommended tools

- Node 18+  
- Python 3.10+  
- Docker (optional: ETL, Neo4j testing, spatial pipelines)  
- make (optional automation)  

---

# 🌾 Project Structure (Quick Overview)

~~~text
.
├── data/            # Data system (raw → work → processed → STAC/DCAT)
├── docs/            # Documentation, standards, governance, analyses
├── web/             # Web platform (React + MapLibre + Cesium)
├── tools/           # CLI, audits, validation, governance, telemetry
├── tests/           # Unit, integration, E2E, schema, governance, A11y
├── releases/        # SBOM, manifest, telemetry
└── schemas/         # JSON/SHACL/ontology schemas
~~~

---

# 🧩 Branching Model

### main  
- Always deployable  
- Fully validated  
- Protected by governance + CI  

### feature/*  
For new features; requires review, validation, and CARE classification.

### fix/*  
For bug/security fixes.

### docs/*  
Docs-only PRs.

### data/*  
For dataset ingestion, metadata changes (requires CARE & provenance checks).

---

# 📥 Pull Request Requirements

All PRs MUST pass:

- TypeScript strict mode  
- ESLint/Prettier/Stylelint  
- Markdown rules (KFM-MDP v10.4)  
- JSON/YAML schema validation  
- Unit + integration tests  
- A11y tests  
- FAIR+CARE validation  
- Governance/provenance checks  
- Telemetry schema validation  
- SBOM/manifest verification  

A PR is **blocked** if ANY requirement fails.

## PR Template (Required Fields)

You MUST complete:

- CARE classification  
- Provenance notes  
- A11y impact  
- Telemetry impact  
- Schema impacts  
- Sensitive-site risk  
- Sustainability considerations  

---

# 🔐 Governance, CARE & Sovereignty Requirements

### CARE Principles  
Contributors must ensure:

- No exposure of restricted coordinates  
- H3 generalization for heritage sites (default r7)  
- Cultural & Indigenous data reviewed by FAIR+CARE Council  
- No misuse of cultural symbols or iconography  
- Positive, contextual, respectful framing  

### Provenance  
Every addition must include:

- Source  
- License  
- Rights-holder  
- Transformation lineage  
- SBOM/manifest updates if applicable  

### Ethical AI  
Focus Mode & AI-related contributions must not:

- Invent historical events  
- Fabricate causal claims  
- Produce unverified summaries  
- Introduce hallucinated citations  

---

# ♿ Accessibility Requirements (WCAG 2.1 AA)

All contributions must maintain or improve A11y:

- Keyboard operability  
- Proper ARIA roles  
- High-contrast colors  
- Reduced-motion support  
- Alt text for images  
- Semantic HTML structure  
- Accessible map colors & overlays  

A11y failures → PR blocked.

---

# 🗃 Dataset Contribution Rules

### Required metadata:
- License  
- Source + provenance  
- CARE classification  
- Spatial extent (bbox + CRS)  
- Temporal extent  
- STAC/DCAT metadata (if applicable)  

### Sensitive datasets:
- Require FAIR+CARE Council review  
- Require masking or H3 r7+ generalization  
- Require clear contextual documentation  

---

# 🧪 Testing Requirements

You MUST run:

~~~bash
npm run test
pytest
npm run test:a11y
~~~

Additionally:

- Story Node v3 payloads must validate  
- Focus Mode v2.5 payloads must validate  
- STAC/DCAT metadata must be schema-align  
- No regressions in performance/drift/ethics metrics  

---

# 📈 Telemetry Responsibilities

Major contributions MUST evaluate:

- Energy usage impacts  
- Carbon impacts  
- A11y telemetry changes  
- Governance telemetry implications  
- WebVitals implications  
- Data pipeline runtime impacts  

Telemetry is exported to:

`releases/<version>/focus-telemetry.json`

---

# 🧾 Legal & Licensing

All contributions are:

**Licensed under MIT**, unless otherwise stated.

You MUST verify:

- External data licenses  
- Attribution requirements  
- CARE + rights-holder compliance  

---

# 🧠 Code, Design & Documentation Standards

### Code
- TypeScript strict  
- PEP8  
- No dead code  
- Deterministic behavior  
- Strong typing  
- No business logic in components  
- No global mutable state  

### Documentation
- All files MUST follow KFM-MDP v10.4  
- Must include YAML front-matter  
- Directory trees MUST use `~~~text`  
- No nested backticks  
- Semantic headings maintained  

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.1 | 2025-11-15 | Fixed all nested code fences; aligned with KFM-MDP v10.4.1; fully one-box-safe |
| v10.4.0 | 2025-11-15 | Initial KFM v10.4 rewrite with CARE/A11y telemetry standards |
| v10.3.2 | 2025-11-14 | Governance + telemetry integrations |
| v10.3.1 | 2025-11-13 | Initial CONTRIBUTING framework |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Governed under MCP-DL v6.3 and KFM-MDP v10.4.1  
FAIR+CARE Certified · Public Document · Version-Pinned  

</div>