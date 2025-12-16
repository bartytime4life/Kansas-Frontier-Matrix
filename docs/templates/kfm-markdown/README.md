---
title: "📄 KFM — Markdown Document Template (KFM-MDP v11.2.6)"
path: "docs/templates/kfm-markdown/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation Board · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Template"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-markdown-template"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_uuid: "urn:kfm:doc:templates:kfm-markdown:v11.2.6"
semantic_document_id: "kfm-template-markdown-doc-v11.2.6"
event_source_id: "ledger:kfm:doc:templates:kfm-markdown:v11.2.6"
immutability_status: "version-pinned"

# Compliance classification (update if your doc is not public)
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../releases/v11.2.6/docs-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-template-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../security/SECURITY.md"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
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
---

# 📄 KFM — Markdown Document Template

**Purpose**  
Use this file as the **canonical starting point** for new KFM documentation.  
Copy it, update `title` + `path`, and replace placeholders (`<...>`) deterministically.

---

## 📘 Overview

**Purpose:** Describe what this document governs, specifies, or enables.

- **Audience:** (e.g., Data Engineering, Reliability, Domain Curators, External Contributors)
- **Scope:** (e.g., one pipeline, one dataset family, one UI feature, one policy)
- **Non-Goals:** Explicitly list what is out of scope.

### Authoring constraints this template assumes

- Exactly **one** H1 (`# ...`) per file.
- Every H2 (`## ...`) must match the **approved heading registry** for KFM‑MDP v11.2.6 (including emoji).
- Use `~~~` fences (tildes) for all fenced blocks (directory trees, code, Mermaid) to prevent nested-fence breakage.

---

## 🗂️ Directory Layout

### Repository placement

Recommended paths by document type:

- **Patterns:** `docs/patterns/<area>/<pattern-name>/README.md`
- **Runbooks:** `docs/runbooks/<area>/<topic>/README.md`
- **Blueprints:** `docs/architecture/<area>/<topic>/README.md` or `docs/domains/<domain>/<topic>/README.md`
- **How‑Tos:** `docs/guides/<topic>/README.md` or `docs/howto/<topic>/README.md` or `src/kfm/<module>/<topic>.md`
- **Experiments:** `mcp/experiments/<domain>/<experiment-name>/README.md`

### Expected local folder layout

Describe any folders this doc expects to exist (or creates):

~~~text
📁 <module-or-domain>/
├── 📄 README.md                          — This document
├── 📁 schemas/                           — Contracts & validation schemas
├── 📁 tests/                             — Deterministic tests + fixtures
├── 📁 configs/                           — Pinned config sets (hashable)
├── 📁 provenance/                        — PROV/OpenLineage artifacts
└── 📁 releases/                          — SBOM/manifest/checksums/signatures
~~~

> Data products and derived datasets belong under `data/processed/**` (canonical outputs), not under `src/**`.

---

## 🧭 Context

### Pipeline placement

State which stage(s) this document applies to:

- **ETL** (ingest → normalize → QA → publish)
- **Catalogs** (STAC/DCAT/PROV emission and validation)
- **Graph** (Neo4j ontology alignment / entity modeling)
- **APIs** (REST/GraphQL contracts, versioning)
- **Web UI** (React/MapLibre, Story Nodes, Focus Mode)

### Contract boundaries

- Keep the frontend **behind APIs** (no direct graph access from the UI).
- Preserve stable IDs/keys and versioned contracts so outputs can be regenerated “one-click.”

---

## 🗺️ Diagrams

If you include Mermaid diagrams:

- Declare allowed `diagram_profiles` in front‑matter.
- Keep Mermaid node labels plain (avoid HTML).
- Use `~~~mermaid` fences.

Example flowchart:

~~~mermaid
flowchart LR
  A[Input] --> B[Transform]
  B --> C[Output]
~~~

---

## 🧠 Story Node & Focus Mode Integration

When this document may be summarized or transformed for Story Nodes / Focus Mode, write it so the system can safely extract:

- stable identifiers (`semantic_document_id`, `doc_uuid`)
- provenance links (`commit_sha`, `provenance_chain`, run IDs)
- explicit “facts vs hypotheses” boundaries
- governance constraints (CARE/FAIR labels, sovereignty rules, redaction notes)

**Focus Mode MAY:**
- summarize and highlight sections,
- produce timelines and navigation aids,
- extract metadata fields and link them to catalogs.

**Focus Mode MUST NOT:**
- alter normative requirements,
- invent governance status,
- fabricate provenance or dataset relationships.

---

## 🧪 Validation & CI/CD

Markdown compliance is CI‑enforced.

### Minimum validation profiles

| Profile | What it protects |
|---|---|
| `markdown-lint` | structure (H1/H2 rules), formatting constraints |
| `schema-lint` | YAML front‑matter schema compliance |
| `metadata-check` | required keys present and consistent |
| `diagram-check` | Mermaid parse + allowed diagram profiles |
| `footer-check` | governance links + footer ordering |
| `accessibility-check` | basic a11y checks (heading order, list semantics) |
| `provenance-check` | provenance chain + version history coherence |
| `secret-scan` | blocks secrets/tokens/credentials |
| `pii-scan` | blocks obvious PII leakage |

### Validation & quality gates

Minimum recommended gates for data-bearing docs (pipelines, datasets, experiments):

1. Schema validation (JSON Schema / Pandera / Great Expectations)
2. Range & null checks (domain constraints)
3. Spatial sanity (bbox, CRS, geometry validity)
4. Temporal sanity (datetime ranges, monotonic time‑series rules if relevant)
5. Deduplication (entity keys, station/site joins, canonical IDs)
6. Drift checks (optional) (distribution shifts, bias flags)

Record results:

- `qa/<run-id>.summary.json`
- `qa/<run-id>.report.md`
- `assets.qa` attached to STAC Item(s)

### Operations

#### Release checklist

- Inputs hashed + recorded
- Config pinned + hashed
- Validation gates pass
- STAC Items/Collections updated
- DCAT dataset/distributions updated
- PROV JSON‑LD emitted
- SBOM emitted
- Checksums generated
- Artifacts signed (if required)
- Version tag + release notes

#### Rollback

Define a deterministic rollback target:

- `releases/<version>/manifest.zip` is the source of truth
- remove/pin catalog pointers to prior version
- keep provenance log entries immutable (append‑only)

---

## 📦 Data & Metadata

### Front‑matter requirements (normative)

A governed KFM doc MUST include:

- identity: `title`, `path`, `version`, `last_updated`
- governance: `governance_ref`, `ethics_ref`, `sovereignty_policy`
- compliance: `license`, `classification`, `sensitivity`, `fair_category`, `care_label`
- provenance: `commit_sha`, `signature_ref` (when release‑pinned), `provenance_chain`
- IDs: `doc_uuid`, `semantic_document_id`, `event_source_id`
- AI transform limits: `ai_transform_permissions`, `ai_transform_prohibited`

Placeholders are allowed only where explicitly indicated (e.g., `<latest-commit-hash>`), and MUST be resolved for release-tagged documents.

### Deterministic provenance requirements

#### Required hashes

- Input file hashes: SHA‑256 for each source file or object
- Config hash: SHA‑256 over canonical JSON/YAML config (sorted keys)
- Output artifact hashes: SHA‑256 for each emitted dataset artifact
- Document integrity checksum: SHA‑256 of this Markdown (optional but recommended)

#### Required provenance artifacts

- PROV JSON‑LD: `provenance/<run-id>.prov.jsonld`
- OpenLineage event(s): `provenance/<run-id>.openlineage.json`
- SBOM (data or code): `releases/<version>/<name>.sbom.(cdx|spdx).json`
- Manifest bundle: `releases/<version>/manifest.zip` including checksums

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Item roles: `data`, `metadata`, `thumbnail`, `qa`, `sbom`, `provenance`
- Key fields: `properties.datetime`, `bbox`, `geometry`, `providers`, `license`
- Integrity fields: `checksum:sha256`, `file:size`, `version`

#### Attach SBOM as STAC asset (example)

~~~json
{
  "assets": {
    "sbom": {
      "href": "../../../releases/v11.2.6/<artifact>.sbom.cdx.json",
      "type": "application/vnd.cyclonedx+json",
      "roles": ["metadata"],
      "title": "Data SBOM (CycloneDX)"
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "../../../releases/v11.2.6/<artifact>.sbom.cdx.json",
      "type": "application/vnd.cyclonedx+json",
      "title": "Deterministic provenance via SBOM"
    }
  ]
}
~~~

### DCAT

- Dataset identity: stable `dct:identifier`, versioned distributions
- Distributions: each output artifact is a `dcat:Distribution` with checksum + `mediaType`
- Governance: attach FAIR+CARE / CARE labels and access constraints where applicable

### PROV

- Entities: inputs, configs, outputs
- Activities: each pipeline stage (ingest → normalize → QA → publish)
- Agents: org/team/service account; include tool version + commit SHA

---

## 🧱 Architecture

### System Context

- **Inputs:** (files, APIs, streams)
- **Transforms:** (ETL steps, normalization, indexing, QA gates)
- **Outputs:** (STAC Items/Collections, DCAT datasets, graph entities, API responses)
- **Determinism controls:** seeds, pinned versions, stable ordering, checksum rules

### Data Flow

~~~mermaid
flowchart LR
  A[Sources] --> B[Deterministic ETL]
  B --> C[Validation Gates]
  C --> D[STAC/DCAT Catalogs]
  D --> E[Neo4j Knowledge Graph]
  E --> F[API]
  F --> G[Web / Story Nodes / Focus Mode]
~~~

---

## ⚖ FAIR+CARE & Governance

### FAIR

- **Findable:** stable identifiers + indexed catalogs
- **Accessible:** explicit access policy + distribution links
- **Interoperable:** standard schemas + STAC/DCAT profiles
- **Reusable:** license, provenance, quality notes

### CARE / Sovereignty

- **Authority to control:** `governance_ref` + `sovereignty_policy` for restricted materials
- **Responsibility & ethics:** `ethics_ref` + required review cycles
- **Benefit & collective accountability:** disclose community impacts where relevant

If sensitive: document redaction / aggregation rules and access boundaries.

### Security & Supply-Chain Controls

- SBOM generated each release (code + data where relevant)
- Artifact signing (Cosign/Sigstore recommended)
- Policy gates (OPA/Conftest) for:
  - required metadata fields present
  - license + access constraints enforced
  - provenance artifacts attached
  - checksum fields match

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---|---|---|
| v11.2.6 | 2025-12-16 | Initial template published | <name/handle> |

---

<div align="center">

📄 **KFM — Markdown Document Template (KFM‑MDP v11.2.6)**  
Stable / Governed · Template · CI‑Safe · FAIR+CARE Aligned

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

[📘 Docs Root](../../README.md) ·
[📂 Standards Index](../../standards/README.md) ·
[📄 Templates Index](../README.md) ·
[⚙ CI/CD Workflows](../../workflows/README.md) ·
[📈 Telemetry Standard](../../standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../telemetry/README.md) ·
[♿ UI Accessibility Standard](../../standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6

</div>