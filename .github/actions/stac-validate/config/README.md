---
title: "🛰 Kansas Frontier Matrix — STAC Validation Config"
path: ".github/actions/stac-validate/config/README.md"
version: "v11.2.3"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Architecture Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/github-infra-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-stac-validate-config"
role: "stac-validation-config"
category: "Metadata · STAC · CI/CD · Configuration"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Metadata"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"

provenance_chain:
  - ".github/actions/stac-validate/README.md@v11.2.3"
  - ".github/actions/stac-validate/config/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/github-actions-stac-validate-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-stac-validate-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:stac-validate-config:v11.2.3"
semantic_document_id: "kfm-action-stac-validate-config"
event_source_id: "ledger:.github/actions/stac-validate/config/README.md"
immutability_status: "mutable-plan"
machine_extractable: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next stac-validate config update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and metadata pipeline events"
---

<div align="center">

# 🛰 **Kansas Frontier Matrix — STAC Validation Config**  
`.github/actions/stac-validate/config/`

**Purpose**  
Define the **config-driven policy layer** for the `stac-validate` composite action, including:

- Which **STAC profile(s)** are enforced (KFM-STAC v11)
- **Collection conventions** and required metadata hooks
- **Asset validation rules** (roles, media types, required fields, naming conventions)
- Optional **severity mapping** (warning/error/critical) where supported by validators

This config is consumed by:

- `.github/actions/stac-validate/entrypoint.sh`
- `.github/actions/stac-validate/scripts/**`
- `.github/workflows/stac_validate.yml` (governed STAC gate)

</div>

---

## 📘 Overview

The `stac-validate` action is designed to be **deterministic** and **policy-driven**. This directory provides the policy inputs that allow KFM to:

- keep validation behavior **consistent across repositories and releases**
- change validation **rules and conventions** without rewriting orchestration logic
- make governance decisions **explicit and reviewable** (policy as code)

**Normative:**

- Config MUST be **repo-relative**, **versioned**, and **reviewed** like code.
- Config MUST NOT contain secrets, credentials, tokens, or private endpoints.
- Config SHOULD avoid non-deterministic behavior (e.g., “latest” validator versions).

If the action is executed with `config_dir=.github/actions/stac-validate/config`, then the files documented here are treated as the canonical local policy source.

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🧱 actions/
    └── 🛰 stac-validate/
        └── ⚙️ config/
            ├── 📄 README.md            # ← This file (how config is structured + governed)
            ├── 🧾 profiles.yml         # STAC profiles, extensions, strictness, required fields
            ├── 🧾 collections.yml      # Collection conventions (ids, required links/providers)
            └── 🧾 assets.yml           # Asset conventions (roles, media types, required fields)
~~~

> **Normative:** Any structural change to this config directory MUST be reflected here and in  
> `.github/actions/stac-validate/README.md`.

---

## 🧭 Context

### Why separate config?

KFM treats “how we validate” as a governed policy surface:

- The action implementation (`entrypoint.sh`, `scripts/**`) is the *engine*.
- This directory is the *rulebook*.

This keeps validation:

- **reproducible** (pin the rules + pin validator versions)
- **auditable** (diffs show policy changes cleanly)
- **governable** (reviewers can focus on “what changes for datasets?”)

### What this config influences

Typical uses include:

- requiring specific STAC extensions (or prohibiting unapproved ones)
- enforcing required fields beyond STAC core (e.g., `license`, `providers`)
- enforcing asset metadata consistency (e.g., `type`/`roles`/`href` patterns)
- enforcing collection conventions (e.g., id prefix, link relations)

---

## 🗺️ Diagrams

The config directory sits between the workflow gate and validator execution:

~~~mermaid
flowchart LR
  A[".github/workflows/stac_validate.yml"] --> B["stac-validate entrypoint.sh"]
  B --> C["Load config/*.yml"]
  C --> D["Run STAC validator + KFM checks"]
  D --> E["Emit structured results + optional summary JSON"]
  E --> F["Fail or pass workflow gate"]
~~~

Plain-language view: CI triggers the action, the action loads config, validators produce results, and CI blocks merges/releases on policy-relevant failures.

---

## 🧠 Story Node & Focus Mode Integration

This config helps keep STAC metadata **consistent and machine-readable**, which in turn supports:

- stable ingestion into catalogs (`data/stac/**`)
- evidence-led linking of datasets into Story Nodes
- safe Focus Mode summaries (consistent fields, consistent license/provenance hooks)

Focus Mode MAY summarize this config and highlight changes, but MUST NOT reinterpret governance rules or weaken policy.

---

## 📦 Data & Metadata

### General conventions

- All config files SHOULD be YAML (`.yml`).
- Keys SHOULD be `lower_snake_case`.
- Rules SHOULD be explicit and stable (avoid ambiguous “best effort” language).
- Any “defaults” applied by config SHOULD be documented and should not fabricate provenance.

### `profiles.yml`

Defines the active profile identifiers and how they are enforced.

Typical contents:

- profile IDs (e.g., `kfm-stac-v11`)
- strictness toggles
- allowed/required extensions
- required field sets (where the validator supports it)
- governance hooks (license/provenance/provider requirements)

Example (illustrative):

~~~yaml
profiles:
  kfm-stac-v11:
    stac_version: "1.0.0"
    strict: true

    extensions:
      require:
        - "https://stac-extensions.github.io/version/v1.2.0/schema.json"
      allow:
        - "https://stac-extensions.github.io/projection/v1.1.0/schema.json"
        - "https://stac-extensions.github.io/eo/v1.1.0/schema.json"

    governance_requirements:
      require_license: true
      require_providers: true
      require_provenance_links: true
~~~

### `collections.yml`

Defines collection-level conventions and minimum metadata expectations.

Typical contents:

- id conventions (prefixes/patterns)
- required link relations
- required provider fields
- required summaries/descriptions (where policy dictates)

Example (illustrative):

~~~yaml
collections:
  conventions:
    id_prefix: "urn:kfm:stac:collection:"
    require_links:
      - "self"
      - "root"
    require_providers: true
    require_license: true
~~~

### `assets.yml`

Defines asset-level conventions and rules applied to each STAC Item’s `assets` object.

Typical contents:

- required asset keys (e.g., `href`, `type`, `roles`)
- allowed/required roles per asset “kind”
- media type allow-lists
- optional `href` patterns (file extensions, naming)

Example (illustrative):

~~~yaml
assets:
  rules:
    require_fields:
      - "href"
      - "type"
      - "roles"

  asset_kinds:
    raster:
      require_roles: ["data"]
      allow_media_types:
        - "image/tiff"
        - "image/tiff; application=geotiff"
      href_patterns:
        - "\\.tif$"
        - "\\.tiff$"

    vector:
      require_roles: ["data"]
      allow_media_types:
        - "application/geo+json"
      href_patterns:
        - "\\.geojson$"

    documentation:
      require_roles: ["metadata"]
      allow_media_types:
        - "text/markdown"
        - "application/pdf"
~~~

> **Normative:** Asset validation MUST NOT require publishing sensitive coordinates or identifiers beyond what is already permitted in governed STAC outputs.

---

## 🌐 STAC, DCAT & PROV Alignment

This config exists to keep STAC validation aligned with KFM’s catalog and governance model:

- **STAC:** enforce consistent `license`, `providers`, extension usage, and asset metadata.
- **DCAT:** ensure metadata needed for catalog records is present (title/description/license/publisher equivalents via STAC mappings where applicable).
- **PROV-O:** ensure provenance hooks exist (e.g., stable lineage links, references to derivation activities) without fabricating provenance.

Where KFM uses additional conventions (e.g., stable `urn:kfm:...` identifiers), those conventions SHOULD be enforced here if they are required for downstream catalog/graph ingestion.

---

## 🧪 Validation & CI/CD

Changes to config are validated in CI via the `stac_validate` workflow gate and related repository checks.

Recommended local validation pattern (where supported by the action implementation):

- Run the action entrypoint against the canonical STAC root:
  - `bash .github/actions/stac-validate/entrypoint.sh data/stac`

Expected CI behaviors:

- Config changes SHOULD cause either:
  - no change (if policy is equivalent), or
  - an explainable change in which STAC Items/Collections pass/fail, and why.
- Any policy change that increases strictness SHOULD be accompanied by:
  - updates/fixes to affected STAC files under `data/stac/**`, or
  - an explicit governance-approved transition plan.

---

## ⚖ FAIR+CARE & Governance

This directory is a governed policy surface.

**Normative:**

- Do not weaken validation requirements (e.g., remove required license/provenance hooks) without governance approval.
- Do not encode rules that cause accidental disclosure of restricted or sensitive metadata.
- Treat config changes as release-impacting: they can change which datasets are acceptable for merge/release.

Relevant governance anchors:

- `ROOT-GOVERNANCE.md` (review authority and escalation)
- `FAIRCARE-GUIDE.md` (FAIR+CARE obligations)
- `INDIGENOUS-DATA-PROTECTION.md` (sovereignty constraints and redaction rules)

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Initial governed README for `stac-validate` config; documents profiles/collections/assets config patterns. |

---

<div align="center">

🛰 **Kansas Frontier Matrix — STAC Validation Config (v11.2.3)**  
Policy-as-Code · FAIR+CARE-Governed · Catalog-First  

[⬅ STAC Validate Action](../README.md) · [⬅ GitHub Infra Overview](../../README.md) · [📊 CI/CD Workflows](../../../workflows/README.md) · [📚 Data & STAC Standards](../../../../docs/data/README.md)

</div>

