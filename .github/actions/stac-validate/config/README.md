---
title: "🛰 Kansas Frontier Matrix — STAC Validate Action Config"
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
intent: "github-stac-validate-action-config"
role: "stac-validate-config"
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
  - ".github/actions/stac-validate/config/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/github-actions-stac-validate-config-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-stac-validate-config-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:config:v11.2.3"
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

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev · staging · production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🛰 **KFM — STAC Validate Action Config**
`.github/actions/stac-validate/config/`

**Purpose**  
Define the **governed, deterministic configuration** used by the STAC validation composite action.

This directory is the policy surface for:
- Which **STAC profile** is enforced (KFM‑STAC v11)
- How strict validation is (error vs warning)
- What Collection/Item conventions are required (IDs, extents, assets, licensing hooks)

</div>

---

## 📘 Overview

The STAC validator action is intentionally config-driven:

- **CI determinism:** the same STAC inputs + same config → same exit code.
- **Governance:** changes to validation rules are reviewed (not silently changed in scripts).
- **Clarity:** profile rules are documented as data, not hidden in code.

Normative constraints:
- Config MUST NOT encode secrets, tokens, or internal endpoints.
- Config MUST keep outcomes explainable (avoid opaque heuristics).

---

## 🗂️ Directory Layout

~~~text
.github/actions/stac-validate/
└── 📁 config/                                  # Governed STAC validation configuration
    ├── 📄 README.md                            # ← This file
    ├── 🧾 profiles.yml                         # Profile IDs, strictness, extension allow/deny
    ├── 🧾 collections.yml                      # Collection conventions (ids, layout, required fields)
    └── 🧾 assets.yml                           # Asset rules (roles, media types, required asset keys)
~~~

---

## 🧭 Context

This configuration is consumed by:

- `.github/actions/stac-validate/entrypoint.sh`
- `.github/actions/stac-validate/scripts/run_stac_validator.py`
- `.github/actions/stac-validate/scripts/check_spatiotemporal.py`
- `.github/actions/stac-validate/scripts/summarize_stac_results.py`

The action may accept an alternate `config_dir`, but KFM governed workflows SHOULD default to this directory.

---

## 📦 Data & Metadata

### `profiles.yml`

Defines:
- Supported profile identifiers (example: `kfm-stac-v11`)
- STAC version constraints
- Extension allowlists/denylists
- Strictness policy (what becomes a failing error)

Example shape:

~~~yaml
profiles:
  - id: "kfm-stac-v11"
    stac_version: "1.0.0"
    strict: true
    allow_extensions:
      - "https://stac-extensions.github.io/projection/v1.1.0/schema.json"
      - "https://stac-extensions.github.io/version/v1.2.0/schema.json"
    deny_extensions: []
    required_item_fields:
      - "id"
      - "type"
      - "geometry"
      - "bbox"
      - "properties.datetime"
      - "assets"
    required_collection_fields:
      - "id"
      - "description"
      - "extent"
      - "license"
~~~

### `collections.yml`

Defines Collection-level conventions. Typical rule categories:
- Collection `id` naming conventions
- Required `providers` / governance-linked metadata (where applicable)
- Expected directory layout (optional)
- Constraints on `extent` completeness (spatial + temporal)

Example shape:

~~~yaml
collections:
  id_pattern: "^kfm-[a-z0-9-]+$"
  require_license: true
  require_extent: true
  extent_requires_temporal: true
  recommended_links:
    - rel: "license"
      required: false
~~~

### `assets.yml`

Defines per-asset expectations (roles/media-type/required keys).

Example shape:

~~~yaml
assets:
  require_asset_title: true
  require_asset_roles: true
  allowed_media_types:
    - "application/geo+json"
    - "application/json"
    - "image/tiff; application=geotiff"
    - "text/markdown"
  role_rules:
    data:
      required: false
      allowed_roles: ["data"]
    thumbnail:
      required: false
      allowed_roles: ["thumbnail", "overview"]
~~~

---

## 🧪 Validation & CI/CD

### Change control

Any config change MUST:
- update the matching action docs (parent README),
- include a clear justification (what failure mode this prevents),
- pass CI validation profiles.

### CI checks expected

- `markdown-lint` / `footer-check` / `accessibility-check`
- `schema-lint` validating YAML structure against `json_schema_ref`
- `provenance-check` ensuring version history + provenance chain are coherent

---

## 🕰️ Version History

| Version | Date       | Summary                                                     |
|--------:|------------|-------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Added governed config README; documented profiles/collections/assets. |

---

<div align="center">

🛰 **KFM — STAC Validate Action Config (v11.2.3)**  
Config-Driven Validation · Deterministic CI · FAIR+CARE Aligned  

[⬅ STAC Validate Action](../README.md) · [🧱 Actions Library](../../README.md) · [⚖ Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
