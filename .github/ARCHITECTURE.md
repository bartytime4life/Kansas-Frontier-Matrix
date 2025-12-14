---
title: "⚙️ Kansas Frontier Matrix — GitHub Infrastructure Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/ARCHITECTURE.md"

version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Architecture Board"
backward_compatibility: "Aligned with v10.x → v11.2.6 CI/CD, metadata, and governance model"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/github-infra-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-infra-telemetry-v11.2.6.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../SECURITY.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 · CI/CD and AI pipeline events"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
intent: "github-infrastructure-architecture"
role: "infrastructure-hub"
category: "CI/CD · Governance · Automation · Telemetry"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
indigenous_rights_flag: false
redaction_required: false

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
data_steward: "KFM FAIR+CARE Council"

provenance_chain:
  - ".github/ARCHITECTURE.md@v10.0.0"
  - ".github/ARCHITECTURE.md@v11.0.0"
  - ".github/ARCHITECTURE.md@v11.0.1"
  - ".github/ARCHITECTURE.md@v11.2.2"
  - ".github/ARCHITECTURE.md@v11.2.3"
  - ".github/ARCHITECTURE.md@v11.2.6"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/github-architecture-v11.schema.json"
shape_schema_ref: "../schemas/shacl/github-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-architecture:v11.2.6"
semantic_document_id: "kfm-doc-github-architecture"
event_source_id: "ledger:.github/ARCHITECTURE.md"
immutability_status: "mutable-plan"
machine_extractable: true

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
diagram_profiles:
  - "mermaid-flowchart-v1"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next infrastructure-architecture update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Architecture**
`.github/ARCHITECTURE.md`

**Purpose**  
Define the architectural role, structure, and control flows of the `.github/` subsystem for KFM v11.2.6 — CI/CD, security, FAIR+CARE enforcement, sovereignty checks, AI governance, telemetry, and CI-triggered repro-kits — in a way that is reproducible, auditable, and machine-readable.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" alt="KFM-MDP v11.2.6" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" alt="MCP-DL v6.3" />
<img src="https://img.shields.io/badge/Lineage-PROV%E2%80%91O_%7C_OpenLineage-success" alt="PROV-O | OpenLineage" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" alt="Active / Enforced" />

<br/>

[📌 .github Overview](README.md) ·
[🧳 Repro-Kit Pattern](repro-kit/README.md) ·
[📦 Data Plane](../data/README.md) ·
[🗄️ Data Architecture](../data/ARCHITECTURE.md)

</div>

---

## 📘 Overview

The `.github/` directory is the governance and automation fabric for the Kansas Frontier Matrix (KFM) monorepo.

At v11.2.6, it provides:

- **CI/CD orchestration** for code, data, docs, and ML governance.
- **KFM-MDP enforcement** for Markdown structure, front-matter, diagrams, and footer policy.
- **Catalog gates** for STAC, DCAT, JSON-LD, and provenance hygiene.
- **FAIR+CARE and sovereignty controls** to prevent unsafe publication or exposure of restricted material.
- **Supply-chain security**: SBOM generation/verification and attestations tied to builds and releases.
- **Telemetry emission** for reliability, governance, and sustainability (energy/carbon) reporting.
- **CI-triggered repro-kits** for fast, safe failure replay:
  - compact,
  - deterministic,
  - sanitized,
  - and attested.

This document describes how workflows, composite actions, policies, and telemetry fit together — and how `.github/` connects to the rest of the KFM pipeline.

---

## 🗂️ Directory Layout

Canonical `.github/` layout (emoji-aligned; box-safe; governance-first):

~~~text
📁 .github/                                            # ⚙️ GitHub governance & automation subsystem
├── 📄 README.md                                        # High-level .github overview (purpose + entrypoints)
├── 🏗️ ARCHITECTURE.md                                  # This document (architecture + control flows)
├── 🛡️ SECURITY.md                                      # Security policy (disclosure + response)
├── 🧩 dependabot.yml                                   # Dependency update configuration
├── 📄 PULL_REQUEST_TEMPLATE.md                         # PR checklist (governance + CI expectations)
│
├── 📁 ISSUE_TEMPLATE/                                  # Issue templates (governance-aware)
│   ├── 📄 bug_report.md                                # Bug reports (pipelines, data, UI, AI)
│   ├── 📄 feature_request.md                           # Enhancements
│   ├── 📄 data_issue.md                                # Data/STAC/DCAT/lineage issues
│   └── 📄 governance_issue.md                          # Governance, ethics, sovereignty issues
│
├── 📁 actions/                                         # Reusable composite GitHub Actions (encapsulated logic)
│   └── 📁 <action-name>/                               # One action per folder (action.yml + scripts)
│
├── 🤖 workflows/                                       # GitHub Actions workflows (orchestration layer)
│   └── 🧾 <workflow>.yml                               # CI, validation, security, release, telemetry
│
└── 📁 repro-kit/                                       # CI-triggered repro-kit pattern and contracts
    └── 📄 README.md                                    # Repro-kit rules (deterministic + sanitized + attested)
~~~

Directory layout rules:

- The tree above is the **architecture contract**: `.github/` holds orchestration, policy, and reusable actions — not domain data.
- Composite actions in `.github/actions/` MUST remain:
  - deterministic,
  - version-aware,
  - and safe to run in forked PR contexts (no secrets by default).
- Any additions that change enforcement scope MUST be reflected here and in `.github/README.md`.

---

## 🧭 Context

`.github/` is the enforcement boundary that keeps the rest of the system safe and reproducible.

It supports the KFM end-to-end pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → UI → Story Nodes → Focus Mode

Branch context (governed practice):

- **main** is the production branch for KFM v11.
- **develop** is an integration branch where CI runs before changes graduate to main.
- The monorepo layout stays consistent across branches; governance checks run on both.

Operational context:

- Data-plane changes under `data/**` must pass catalog + governance gates before they are treated as publishable.
- Documentation changes under `docs/**`, `.github/**`, and `src/**/README.md` must pass KFM-MDP checks.
- AI and narrative layers are explicitly governed; `.github/` is where those checks live and where evidence is recorded.

---

## 🧱 Architecture

The `.github/` subsystem is structured as three enforceable layers plus one reliability accelerator:

1. **Workflows (orchestration layer)**
   - Declarative workflow definitions under `.github/workflows/`.
   - Triggered on PRs, pushes, schedules, and releases.
   - Expected behavior:
     - path-aware execution,
     - deterministic inputs,
     - machine-readable outputs (summaries, reports, telemetry).

2. **Composite actions (logic layer)**
   - Reusable actions under `.github/actions/`.
   - Centralize complex behavior so workflows stay thin.
   - Expected behavior:
     - pinned tool versions,
     - explicit inputs/outputs,
     - uniform error shapes for parsing in telemetry.

3. **Policies and templates (governance layer)**
   - `SECURITY.md`, issue templates, PR templates, and branch protections (configured in GitHub settings).
   - Expected behavior:
     - fail-closed posture for governance violations,
     - clear escalation paths to councils and stewards.

4. **Repro-kit pattern (reliability accelerator)**
   - Documented under `.github/repro-kit/README.md`.
   - When a CI failure meets criteria, CI emits:
     - a deterministic, minimal reproduction bundle,
     - sanitization evidence,
     - and an attestation.
   - Goal: reduce “cannot reproduce” incidents without leaking secrets/PII.

Architectural guarantees:

- Workflows orchestrate; composite actions implement; policy gates constrain; repro-kits accelerate triage.
- `.github/` must remain auditable:
  - what was checked,
  - what passed/failed,
  - and what evidence was produced.

---

## 🗺️ Diagrams

### Pull request to release control flow

~~~mermaid
flowchart LR
  A["Contributor opens PR"] --> B["CI runs required workflows"]
  B -->|pass| C["Required reviews and governance checks"]
  B -->|fail| D["Fix and push updates"]
  C -->|approved| E["Merge to protected branch"]
  C -->|changes requested| D
  E --> F["Release workflow packages artifacts"]
  F --> G["SBOM, manifest, attestations, telemetry"]
~~~

This flow is fail-closed: a change is not eligible for merge or release unless checks and reviews succeed.

### CI failure to repro-kit control flow

~~~mermaid
flowchart TD
  A["CI job fails"] --> B["Eligibility check for repro-kit"]
  B -->|eligible| C["Collect minimal inputs or pointers"]
  C --> D["Sanitize (secret scan, PII scan, policy gate)"]
  D -->|publishable| E["Package repro-kit with manifest and checksums"]
  E --> F["Attest (SLSA/in-toto)"]
  F --> G["Upload (short TTL) and link in issue"]
  D -->|blocked| H["Quarantine stub (manifest + redaction report)"]
~~~

Repro-kits increase triage speed while preserving governance and security constraints.

---

## 🧪 Validation & CI/CD

Validation in KFM is layered, with `.github/` acting as the enforcement point.

### Minimum CI enforcement profiles (documentation-aware)

Docs in `.github/**/*.md` are expected to pass:

- `markdown-lint` (H1/H2 rules; fence rules; directory tree fences)
- `schema-lint` (front-matter schema compliance)
- `metadata-check` (required keys present and coherent)
- `diagram-check` (Mermaid parses; no HTML labels)
- `footer-check` (required governance links)
- `accessibility-check` (basic a11y structure)
- `secret-scan` and `pii-scan` (fail-closed)

### Workflow classes (conceptual)

1. **Core quality**
   - lint, tests, type checks
2. **Docs and standards validation**
   - KFM-MDP and front-matter checks
3. **Catalog and metadata validation**
   - STAC, DCAT, JSON-LD, provenance sanity
4. **FAIR+CARE and sovereignty**
   - required flags/labels, masking/generalization checks
5. **Security and supply chain**
   - dependency scanning, SBOM verification, attestations
6. **Data pipelines and AI governance**
   - ETL contracts; model checks; narrative safety checks
7. **Release and telemetry**
   - signed release packets; telemetry export; governance snapshots

### Branch protection expectations

Protected branches (e.g., `main`, `release/*`) should require:

- required workflow checks (core CI + governance gates),
- required reviews per CODEOWNERS or stewardship rules,
- prohibition of force-push,
- and policy-only changes treated as architectural changes requiring elevated review.

---

## 📦 Data & Metadata

`.github/` produces and consumes structured metadata.

### Produced (release- and run-level)

- **SBOMs** (software bill of materials) and manifests for releases
- **Attestations** (SLSA/in-toto style) binding builds to commits and CI identity
- **Telemetry snapshots** capturing:
  - workflow outcomes,
  - governance gate outcomes,
  - security scan summaries,
  - sustainability estimates (energy/carbon) where available
- **Lineage events**
  - OpenLineage events for CI/CD jobs (when enabled)
  - PROV-O-compatible records for governed run traces

### Consumed (policy and contract inputs)

- governance and FAIR+CARE policies under `docs/standards/**`
- schema references under `schemas/**`
- release packets under `releases/**`
- domain evidence from `data/reports/**` and `mcp/runs/**` (where relevant)

Notes:

- Schema references in front-matter are intended to be stable pointers.
- Release-pinned references MUST be resolved and valid for tagged releases.

---

## 🌐 STAC, DCAT & PROV Alignment

This document is a documentation artifact and may be represented in catalogs:

### DCAT

- Treat `.github/ARCHITECTURE.md` as a documentation dataset record (`dcat:Dataset` or `dcat:CatalogRecord`).
- `semantic_document_id` maps to `dct:identifier`.
- Markdown is a `dcat:Distribution` (`mediaType: text/markdown`).

### STAC

- This document may be represented as a non-spatial STAC Item:
  - `geometry: null`
  - `properties.datetime = last_updated`
  - `assets.markdown.href` points to the repo path

### PROV-O

- This architecture document is a `prov:Plan`.
- Workflow runs, validations, and releases are `prov:Activity` instances.
- CI bots, councils, and maintainers are `prov:Agent` instances.
- SBOMs, manifests, telemetry, and repro-kits are `prov:Entity` instances connected via `prov:used` and `prov:wasGeneratedBy`.

---

## 🧠 Story Node & Focus Mode Integration

`.github/` enables trustworthy narratives by ensuring evidence exists and is queryable.

Story Node and Focus Mode expectations:

- Narrative layers may summarize CI health, provenance, and governance outcomes using telemetry and structured evidence.
- Narrative layers MUST NOT:
  - invent governance status,
  - fabricate lineage,
  - or claim validations occurred if evidence is missing.

Operational integration points:

- CI telemetry and lineage can be ingested into the graph as:
  - Activities (runs),
  - Entities (artifacts, reports),
  - and Agents (maintainers, bots, councils).
- This supports questions like:
  - “What checks gated this dataset’s release?”
  - “Which commit introduced a validation rule change?”
  - “Was a repro-kit generated for this failure, and was it quarantined?”

---

## ⚖ FAIR+CARE & Governance

FAIR+CARE and sovereignty are enforced here as an architectural constraint, not a courtesy.

Core posture:

- **Fail-closed** on governance, safety, and security violations.
- **Authority to Control** is implemented via:
  - required reviews,
  - restricted workflows,
  - and masking/generalization enforcement where needed.
- **Responsibility and ethics** are encoded into:
  - checks,
  - release artifact requirements,
  - and telemetry evidence.

Security constraints:

- No secrets or credentials in workflows, docs, or artifacts.
- Repro-kits must be sanitized and policy-gated before upload.
- Supply-chain metadata must be traceable and attested where configured.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-14 | Updated to KFM-MDP v11.2.6; added repro-kit architecture integration; refreshed directory layout to include `.github/repro-kit/`; updated diagrams to comply with Mermaid guardrails; aligned release and telemetry references to v11.2.6. |
| v11.2.3     | 2025-12-08 | Aligned with KFM-MDP v11.2.5; expanded workflow map; clarified governance/telemetry wiring; synced with `.github/README.md`. |
| v11.2.2     | 2025-11-28 | Synced GitHub architecture with v11.2.2 CI/CD model; clarified FAIR+CARE and sovereignty gating. |
| v11.0.1     | 2025-11-23 | Linked CI workflows with PROV-O and OpenLineage; introduced AI behavior and Focus Mode governance flows. |
| v11.0.0     | 2025-11-19 | First v11 GitHub architecture doc; defined workflow classes and composite-action patterns. |
| v10.0.0     | Legacy     | Pre-v11 baseline, prior to FAIR+CARE and sovereignty integration. |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — GitHub Infrastructure Architecture (v11.2.6)**  
Designed for Longevity · Governed for Integrity

[📌 .github Overview](README.md) ·
[🧳 Repro-Kit Pattern](repro-kit/README.md) ·
[⚖ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🛡 Security Policy](../SECURITY.md) ·
[⬅ Back to Repository Root](../README.md)

</div>
