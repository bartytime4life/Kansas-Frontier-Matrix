---
title: "README — DCAT Validate Action Config"
path: ".github/actions/dcat-validate/config/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "active"
doc_kind: "Guide"
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
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:github-actions:dcat-validate:config-readme:v1.0.0"
semantic_document_id: "kfm.github-actions.dcat-validate.config.readme.v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:dcat-validate:config-readme:2025-12-22"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  allowed:
    - "summarize"
    - "structure_extract"
    - "translate"
    - "keyword_index"
  prohibited:
    - "generate_policy"
    - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# README — DCAT Validate Action Config

## 📘 Overview

### Purpose
This folder holds configuration for the repository’s **DCAT validation GitHub Action** (`.github/actions/dcat-validate/`). The action exists to validate **DCAT dataset records** produced under `data/catalog/dcat/` against the repository’s **DCAT constraints / shape bundles** under `schemas/dcat/`.

This supports KFM’s contract-first pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

### Scope
In scope:
- Configuration files under `.github/actions/dcat-validate/config/`
- Target selection (which DCAT records to validate)
- Constraint selection (which schemas/shapes to validate against)
- CI behavior rules and determinism expectations

Out of scope:
- Implementing the validator logic (action code)
- Authoring or changing the KFM DCAT profile itself (`docs/standards/KFM_DCAT_PROFILE.md`)
- Publishing/harvesting DCAT externally

### Audience
- CI / DevEx maintainers
- Catalog maintainers
- Contributors who add/edit DCAT outputs or schemas

### Definitions
- **DCAT**: W3C Data Catalog Vocabulary (dataset metadata standard)
- **JSON-LD**: JSON serialization for Linked Data (common DCAT representation)
- **Schema / shapes**: machine-readable constraints (JSON Schema and/or SHACL)
- **Profile**: governed specialization of a standard (`KFM-DCAT v11.0.0`)
- **Evidence artifacts**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV)

### Key artifacts
| Artifact | Path | Notes |
|---|---|---|
| This README | `.github/actions/dcat-validate/config/README.md` | Keep in sync with action behavior |
| DCAT outputs | `data/catalog/dcat/` | Produced by Catalog stage |
| DCAT constraints | `schemas/dcat/` | Constraints + shape bundles as needed |
| DCAT profile spec | `docs/standards/KFM_DCAT_PROFILE.md` | Governs required fields + mappings |

### Definition of done
- [ ] Config targets `data/catalog/dcat/**` (or a more specific subset) and stays deterministic
- [ ] Config points to `schemas/dcat/**` and pins versions when applicable
- [ ] CI behavior follows the v13 readiness rule: **validate if present; fail if invalid; skip if not applicable**
- [ ] No secrets added; logs avoid dumping sensitive content
- [ ] README updated when config schema/behavior changes

## 🗂️ Directory Layout

### This document
- `path`: `.github/actions/dcat-validate/config/README.md` (must match front-matter)

### Local action layout
~~~text
📁 .github/
└── 📁 actions/
    └── 📁 dcat-validate/
        ├── 📁 config/
        │   └── 📄 README.md
        └── 📄 <action implementation files>   # not confirmed in repo
~~~

### Related canonical roots
~~~text
📁 data/
└── 📁 catalog/
    └── 📁 dcat/                # DCAT outputs (JSON-LD)

📁 schemas/
└── 📁 dcat/                    # DCAT constraints + shape bundles (as needed)
~~~

## 🧭 Context

### Why DCAT validation exists
DCAT records are a **contract artifact** consumed downstream. Invalid catalog metadata can:
- break dataset discovery/export,
- cause API contract drift for catalog endpoints, and/or
- undermine provenance expectations where catalog IDs are referenced.

### Invariants and constraints
- **Deterministic and idempotent behavior**: validation must not mutate artifacts.
- **Contracts are canonical**: constraints/specs live in `schemas/`.
- **Optional roots**: workflows should skip when optional roots are absent, and fail deterministically when present but invalid.
- **No sensitive leakage**: CI logs should avoid printing full JSON-LD payloads; prefer file path + error summary.

### Not confirmed in repo
The exact **config file names**, **config schema**, and **action inputs** are not confirmed in repo. This README documents a recommended contract and must be kept in sync with the action implementation.

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  PR[Pull Request / Push] --> CI[GitHub Actions Workflow]
  CI --> A[.github/actions/dcat-validate]
  A --> T[Select targets<br/>data/catalog/dcat/**]
  A --> S[Load constraints<br/>schemas/dcat/**]
  T --> V[Validate DCAT records]
  S --> V
  V -->|pass| OK[CI ✅]
  V -->|fail| FAIL[CI ❌]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Canonical path | Notes |
|---|---|---|
| DCAT records | `data/catalog/dcat/**` | Typically JSON-LD (extensions vary) |
| Constraint bundles | `schemas/dcat/**` | JSON Schema and/or SHACL shapes as needed |
| Action config | `.github/actions/dcat-validate/config/**` | Config schema is action-owned |

### Outputs
| Output | Where | Notes |
|---|---|---|
| Pass/fail signal | CI job result | Hard fail on invalid artifacts |
| Validation report | CI logs and/or artifact | Report path not confirmed in repo |

### Quality signals (expected)
- DCAT records validate against constraints in `schemas/dcat/`
- Stable identifiers in catalog artifacts
- Deterministic diffs between runs (no nondeterministic ordering / timestamps in output)

## 🌐 STAC, DCAT & PROV Alignment

### Relationship
- **STAC** covers geospatial assets (items/collections).
- **DCAT** covers dataset-level metadata and discoverability.
- **PROV** captures lineage for datasets and pipeline runs.

This action validates the **DCAT leg** of the evidence artifact set (STAC/DCAT/PROV).

### Do not mix responsibilities
- STAC validation should live in a separate validator/action.
- PROV validation should live in a separate validator/action.
- This action remains focused on DCAT constraints and profile conformance.

## 🧱 Architecture

### Responsibilities
- **Action**: reads config, selects DCAT files, validates them, returns deterministic pass/fail.
- **Config**: defines *what* to validate and *how strict* the gate is.
- **Schemas**: define canonical constraints.

### Recommended config knobs (action-owned)
These are recommended fields to support; confirm against the action implementation:

| Knob | Type | Example | Purpose |
|---|---:|---|---|
| `targets` | list(glob) | `data/catalog/dcat/**/*.jsonld` | Which DCAT records to validate |
| `schema_root` | path | `schemas/dcat/` | Where constraints live |
| `mode` | enum | `jsonschema` / `shacl` / `both` | Validation engine selection |
| `skip_if_missing` | bool | `true` | Match “skip if not applicable” rule |
| `fail_on_warning` | bool | `true` | Keep CI strict as needed |

### Example config (illustrative)
~~~yaml
# Example only — align keys with the action implementation.
targets:
  - "data/catalog/dcat/**/*.jsonld"
schema_root: "schemas/dcat/"
mode: "jsonschema"
skip_if_missing: true
fail_on_warning: true
~~~

## 🧠 Story Node & Focus Mode Integration

Although this action validates DCAT (not story content directly), it supports Focus Mode’s constraints by ensuring catalog metadata is structurally valid before it becomes part of provenance-linked context bundles.

Design rules to keep in mind:
- Focus Mode consumes **only provenance-linked content**.
- Any predictive/AI-generated narrative must be opt-in and carry uncertainty metadata.

## 🧪 Validation & CI/CD

### Minimum CI gates (context)
KFM’s readiness gates include:
- Markdown protocol validation
- Schema validation (including DCAT)
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

### CI behavior rule
When wired into workflows, the validator should behave deterministically:
- **Validate if present**
- **Fail if invalid**
- **Skip if not applicable** (e.g., optional roots absent)

### Change checklist (when editing config)
- [ ] Confirm target globs only match intended files under `data/catalog/dcat/`
- [ ] Confirm schema roots reference `schemas/dcat/` only
- [ ] Ensure config changes don’t relax requirements without review
- [ ] Ensure logs do not expose sensitive content

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- Changes that alter published metadata fields (DCAT profile changes)
- Changes that modify validation strictness in a way that could ship invalid metadata
- Any change that could expose restricted locations or culturally sensitive knowledge via catalog metadata

### Sovereignty safety
If DCAT records include spatial/temporal coverage for sensitive materials, ensure redaction/generalization policies are enforced at the appropriate layer (typically the API boundary), and that CI does not leak sensitive content in logs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for DCAT validation action config folder | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
