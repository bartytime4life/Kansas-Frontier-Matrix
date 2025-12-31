---
title: "🧩 KFM Schemas — Contracts & Validators"
path: "schemas/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "Standard"
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
doc_uuid: "urn:kfm:doc:schemas:schemas-readme:v1.0.0-draft"
semantic_document_id: "kfm-schemas-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:schemas:schemas-readme:v1.0.0-draft"
commit_sha: "<latest-commit-hash>"
ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# 🧩 Schemas

Machine-validated contracts for KFM catalogs, provenance, narratives, UI registries, and telemetry.

## 📘 Overview

The `schemas/` directory contains contract schemas (primarily JSON Schema) that define and validate KFM’s structured artifacts. KFM is explicitly **contract-first**: schemas (and API contracts) are treated as first-class repo artifacts, and changes to them require disciplined versioning and compatibility checks.  

Why this matters: KFM treats the catalog stage as a formal gatekeeper—**no data enters the graph or UI until it has complete metadata and passes validation checks**. Schemas are a primary mechanism for enforcing that checkpoint, preventing malformed metadata (or missing required fields) from propagating downstream.

This README documents:
- What belongs in each schema domain folder
- How schema folders map to KFM pipeline outputs
- A minimal workflow for validating and updating schema contracts

## 🗂️ Directory Layout

### 📁 Canonical `schemas/` layout (emoji format)

    📁 schemas/                                   # JSON Schemas / shapes for KFM contracts
    ├── 📄 README.md                              # This file
    ├── 📁 stac/                                  # KFM-STAC profile schemas (Collections/Items)
    ├── 📁 dcat/                                  # KFM-DCAT profile schemas (dataset metadata)
    ├── 📁 prov/                                  # KFM-PROV profile schemas (lineage records)
    ├── 📁 storynodes/                             # Story Node front-matter + structure schemas
    ├── 📁 ui/                                    # UI registry/layer spec schemas
    └── 📁 telemetry/                             # Telemetry / logs / event schemas

### 🔗 Where schema-validated artifacts live (canonical output locations)

    📁 data/
    ├── 📁 stac/
    │   ├── 📁 collections/                       # STAC Collections (must validate)
    │   └── 📁 items/                             # STAC Items (must validate)
    ├── 📁 catalog/
    │   └── 📁 dcat/                              # DCAT dataset metadata (must validate)
    └── 📁 prov/                                  # PROV lineage records (must validate)

Note: If your repo uses different paths for these outputs, align to the Master Guide’s canonical structure and update this README accordingly.

## 🧭 Context

KFM’s canonical pipeline is enforced as a series of contract checkpoints:

- ETL produces deterministic, logged outputs.
- Catalogs (STAC/DCAT/PROV) describe those outputs using standards + KFM profiles.
- Graph ingests from the cataloged outputs, preserving provenance.
- API serves as the stable contract boundary for UI and any external consumers.
- UI and Story/Focus experiences must remain evidence-first and provenance-linked.

Schemas are used to enforce the “contract-first” boundary between these stages. In practice:
- Catalog schemas validate “what exists” and “what it means” (spatial/temporal extent, licensing, provenance, etc.).
- Story Node schemas validate narrative structure and ensure citations/IDs are structurally present.
- UI schemas validate registries/config so UI can render predictably without ad-hoc assumptions.
- Telemetry schemas standardize logs/events for observability and auditability.

## 🧪 Minimum Work Example

### Example: validate one artifact against the appropriate schema (tool-agnostic)

1) Identify the artifact type and location:
- STAC Item or Collection: under `data/stac/items/` or `data/stac/collections/`
- DCAT dataset metadata: under `data/catalog/dcat/`
- PROV lineage record: under `data/prov/`

2) Select the matching schema under `schemas/<domain>/` (ensure it matches the profile version noted in this README’s front-matter).

3) Run a validator (examples below — exact tooling is repo-dependent).

Example commands (tooling not confirmed in repo; pick one that matches project tooling):

    # Python (jsonschema) — validates a JSON instance against a JSON Schema
    python -m jsonschema -i data/stac/items/<item>.json schemas/stac/<schema>.json

    # Node (AJV) — validates a JSON instance against a JSON Schema
    npx ajv validate -s schemas/stac/<schema>.json -d data/stac/items/<item>.json

### Example: add or update a schema safely

1) Decide whether the change is:
- Patch (tighten wording, add non-breaking optional fields)
- Minor (add new optional fields, new schema file, new example)
- Major / breaking (required field changes, meaning changes) → create a versioned schema and keep the prior version available

2) Add/update schema under the correct domain:
- `schemas/stac/` for STAC
- `schemas/dcat/` for DCAT
- `schemas/prov/` for PROV
- `schemas/storynodes/` for Story Node docs
- `schemas/ui/` for UI registry/config
- `schemas/telemetry/` for telemetry/events

3) Add at least one “known-valid” example JSON (location not confirmed in repo; recommended to keep examples close to the schema they test).

4) Run local validation (and ensure CI schema checks pass).

5) Update this README (and any domain README if present) with:
- What changed
- Which version/profile it aligns to
- Any migration notes for downstream systems

## ✅ Validation / Definition of Done

For changes under `schemas/` to be merge-ready:

- [ ] Schema files are syntactically valid and loadable by the repo’s validator(s).
- [ ] Schema changes follow contract-first expectations: versioning and compatibility are addressed.
- [ ] At least one example or test fixture demonstrates validity for each new/changed schema.
- [ ] Downstream break risk is documented (Graph/API/UI impacts).
- [ ] No governance/sensitivity violations are introduced (e.g., no new fields that would require publishing restricted locations without review).
- [ ] CI checks pass, including schema validation and any “schema-lint” or repository validation steps.

## ❓ Open Questions / TODO

- Confirm the canonical JSON Schema draft/version used across KFM validators (not confirmed in repo).
- Confirm whether DCAT validation is JSON Schema only, or also SHACL/ShEx (not confirmed in repo).
- Confirm whether per-domain READMEs exist or are desired under `schemas/<domain>/README.md` (not confirmed in repo).
- Confirm the exact local validation command(s) used in CI (e.g., `schema-lint`) and document them here (not confirmed in repo).

## 🟢 Status

Draft. Intended as a scaffold aligned to KFM’s contract-first + validation-gated pipeline. Update once the repo’s concrete schema files and validator commands are confirmed.

## 🕰️ Version History

- v1.0.0-draft (2025-12-31): Initial scaffold for `schemas/README.md` with emoji directory layout + contract-first guidance.

## 🔗 References

Expected canonical references (some paths not confirmed in repo; see Master Guide / standards index):
- `docs/MASTER_GUIDE_v13.md` — canonical pipeline and repo structure
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` — governed documentation template
- `docs/standards/KFM_STAC_PROFILE.md` — KFM STAC profile (v11)
- `docs/standards/KFM_DCAT_PROFILE.md` — KFM DCAT profile (v11)
- `docs/standards/KFM_PROV_PROFILE.md` — KFM PROV profile (v11)
- `docs/standards/KFM_MARKDOWN_FORMATTING_GUIDE.md` — front-matter + section rules
- `docs/governance/ROOT_GOVERNANCE.md`, `ETHICS.md`, `SOVEREIGNTY.md` — governance and sensitivity rules
---