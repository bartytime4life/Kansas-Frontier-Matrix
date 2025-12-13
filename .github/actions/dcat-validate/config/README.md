---
title: "🧾 Kansas Frontier Matrix — DCAT Validate Action Config"
path: ".github/actions/dcat-validate/config/README.md"
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
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-dcat-validate-config"
role: "dcat-validation-action-config"
category: "Metadata · DCAT · CI/CD · Config"

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
  - ".github/actions/dcat-validate/config/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/github-actions-dcat-validate-config-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/github-actions-dcat-validate-config-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:dcat-validate:config:v11.2.3"
semantic_document_id: "kfm-action-dcat-validate-config"
event_source_id: "ledger:.github/actions/dcat-validate/config/README.md"
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
sunset_policy: "Superseded upon next dcat-validate config update"

openlineage_profile: "OpenLineage v2.5 · CI/CD and catalog validation events"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — DCAT Validate Action Config**
`.github/actions/dcat-validate/config/`

**Purpose**  
Define the **governed, deterministic configuration** consumed by the KFM **DCAT validation** CI action.
This config controls:

- Which **DCAT profile** to enforce (KFM‑DCAT v11)  
- **Rule strictness**, severities, and allowlisted exceptions  
- **Controlled vocabularies** (licenses, media types, themes)  
- Repo path discovery for **DCAT records** and validation targets  

</div>

---

## 📘 Overview

This directory is part of KFM’s **catalog validation layer**. The `dcat-validate` action reads these files to
ensure every DCAT record (e.g., dataset/distribution metadata) is:

- **Spec-valid** (DCAT 3.0 semantics and shapes)
- **Profile-valid** (KFM‑DCAT v11 project constraints)
- **Governance-valid** (license, provenance, stewardship hooks)
- **Deterministic** (config-driven; no environment-dependent behavior)

> **Normative:** Any change to validation thresholds, allowlists, or controlled vocabularies MUST be done
> here (not inline in workflow YAML), and MUST be reviewable under KFM governance.

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🧱 actions/
    └── 🧾 dcat-validate/
        └── ⚙️ config/
            ├── 📄 README.md                 # ← This file (what each config file does)
            ├── 🧾 profiles.yml              # DCAT profile ids + validator/shape wiring
            ├── 🧾 rules.yml                 # Rule toggles, severities, fail/pass thresholds
            ├── 🧾 vocab.yml                 # Controlled vocabularies (licenses, media types, themes)
            ├── 🧾 ignore.yml                # Allowlisted exceptions (scoped + expiring)
            └── 🧾 paths.yml                 # Where to find DCAT records in-repo (globs, roots)
~~~

---

## 🧭 Context

**KFM pipeline placement:** ETL → **catalogs (STAC/DCAT/PROV)** → graph → API → frontend.

DCAT validation sits in the **catalogs** stage to prevent:

- broken or incomplete catalog exports,
- missing license/provenance fields,
- inconsistent dataset/distribution metadata that breaks downstream ingestion,
- “quiet drift” of metadata semantics that would undermine governance and Focus Mode transparency.

---

## 📦 Data & Metadata

The config files in this directory are **inputs** to the validator. They should be treated as governed
infrastructure—small changes can affect release gating.

### `profiles.yml`

Defines supported profile identifiers and how each profile is validated.

~~~yaml
profiles:
  - id: "kfm-dcat-v11"
    dcat_version: "3.0"
    serialization:
      - "jsonld"
      - "ttl"
    # Shape locations are typically repo-root paths; keep them stable and versioned.
    shacl_shape_ref: "schemas/shacl/kfm-dcat-v11-shape.ttl"
    strict: true
    notes: "KFM-DCAT v11 profile for public catalog publishing."
~~~

### `rules.yml`

Defines rule behavior and severity mapping. This is where “what fails CI” is controlled.

~~~yaml
thresholds:
  fail_on:
    critical: true
    high: true
    medium: false
    low: false

rules:
  # Examples (rule ids are project-owned; keep stable)
  - id: "dcat.required.title"
    severity: "high"
    enabled: true
    description: "Dataset MUST have a non-empty title."

  - id: "dcat.required.license"
    severity: "critical"
    enabled: true
    description: "Dataset MUST declare a license (governance requirement)."

  - id: "dcat.distribution.access_url"
    severity: "high"
    enabled: true
    description: "Each Distribution MUST include accessURL and/or downloadURL."

  - id: "kfm.provenance.hook"
    severity: "high"
    enabled: true
    description: "Dataset MUST include a provenance hook (e.g., prov:wasDerivedFrom or KFM lineage pointer)."
~~~

### `vocab.yml`

Defines controlled vocabularies to reduce ambiguity and improve interoperability. Keep lists short, explicit,
and aligned to published governance.

~~~yaml
licenses:
  allowed:
    - "CC-BY-4.0"
    - "CC0-1.0"
    - "MIT"
  # If DCAT requires IRIs in your implementation, store IRIs here instead of SPDX ids.

media_types:
  allowed:
    - "application/json"
    - "application/geo+json"
    - "text/csv"
    - "application/pdf"

themes:
  allowed:
    - "historical"
    - "cultural"
    - "ecological"
    - "infrastructure"
    - "archaeology"
~~~

### `ignore.yml`

Allowlisted exceptions MUST be **scoped**, **justified**, and **expiring**. This prevents permanent policy
bypass.

~~~yaml
exceptions:
  - id: "EX-2025-0001"
    rule_id: "dcat.distribution.access_url"
    scope:
      dataset_id: "urn:kfm:dataset:example:placeholder"
    justification: "Legacy record pending migration to new distribution model."
    expires_on: "2026-03-01"
    owner: "KFM FAIR+CARE Council"
~~~

### `paths.yml`

Controls what files are validated and where they live in the repo. Keep globbing deterministic and avoid
ambiguous broad patterns unless necessary.

~~~yaml
targets:
  - name: "primary-dcat"
    root: "data/dcat"
    include:
      - "**/*.json"
      - "**/*.jsonld"
      - "**/*.ttl"
    exclude:
      - "**/_drafts/**"
      - "**/tmp/**"
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

KFM treats **STAC, DCAT, and PROV** as linked outputs:

- **STAC** describes spatiotemporal assets (Items/Collections).
- **DCAT** describes publishable datasets and distributions (catalog interoperability).
- **PROV** provides lineage for trust, reproducibility, and governance.

This config SHOULD be used to enforce cross-standard coherence, such as:

- `license` values consistent across STAC/DCAT representations
- dataset temporal/spatial coverage present in publishable catalog fields
- presence of provenance hooks that can be traced to governed ETL activities

---

## 🧪 Validation & CI/CD

When config is changed, CI should validate:

- the YAML is parseable and schema-valid,
- rule thresholds behave as intended (no accidental “always pass”),
- ignore exceptions are not expired,
- profile/shape references remain stable.

### Local validation (developer runbook)

~~~bash
# Example only — use the repository's canonical workflow/entrypoint if different.
set -euo pipefail

# From repo root:
bash .github/actions/dcat-validate/entrypoint.sh \
  --dcat-root "data/dcat" \
  --config-dir ".github/actions/dcat-validate/config" \
  --profile "kfm-dcat-v11"
~~~

---

## ⚖ FAIR+CARE & Governance

This config is a governance boundary:

- It MUST NOT weaken license/provenance requirements without explicit review.
- It MUST NOT introduce allowlists that permanently bypass critical policy checks.
- It SHOULD encourage **aggregation** over exposure in cases where sensitive metadata could leak.

If sovereignty or sensitive-data controls are required for any DCAT output, they MUST be enforced in the
catalog generation pipeline and reflected in validation rules (e.g., required redaction flags, access rights,
or distribution controls).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-13 | Initial governed README for DCAT validation config layout, conventions, and examples. |

---

<div align="center">

🧾 **KFM — DCAT Validate Action Config (v11.2.3)**  
Catalog-First · FAIR+CARE-Governed · Deterministic Validation  

[⬅ GitHub Infra Overview](../../../README.md) · [🧾 DCAT Validate Action](../README.md) · [📚 Data Standards](../../../../docs/data/README.md)

</div>

