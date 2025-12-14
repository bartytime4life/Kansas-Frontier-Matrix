---
title: "🧩 KFM — DRIFT STAC Templates (Retrieval Episodes · Provenance Anchors)"
path: "docs/search/drift/stac/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-13"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Templates Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A2-I2-R2"
care_label: "CARE-Aware Retrieval"
classification: "Public (Governed)"
sensitivity: "General (template-only; no restricted content)"
sensitivity_level: "Low"
public_exposure_risk: "Low"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

doc_uuid: "urn:kfm:doc:search:drift:stac-templates:v11.2.6"
semantic_document_id: "kfm-drift-stac-templates"
event_source_id: "ledger:docs/search/drift/stac/templates/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "12 months"
sunset_policy: "Superseded upon next STAC template profile revision"
---

<div align="center">

# 🧩 **DRIFT STAC Templates**
`docs/search/drift/stac/templates/README.md`

**Purpose**  
Provide governed, deterministic JSON templates for emitting STAC Collections/Items that represent **DRIFT retrieval episodes**,
including required provenance anchors and **CARE-aware** governance flags.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC-KFM--STAC_v11-brightgreen" />
<img src="https://img.shields.io/badge/PROV-KFM--PROV_v11-blue" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory contains STAC JSON templates used by DRIFT Search to generate:

- STAC Items for each retrieval episode (global→local hybrid retrieval)
- Optional STAC Collections for grouping retrieval episode Items
- A consistent assets + properties layout binding episode outputs to PROV/OpenLineage and governance flags

Design goals:

- Deterministic output: same inputs → identical STAC JSON
- Provenance-first: every Item has explicit links to provenance bundles and governance decisions
- Safety by default: templates contain no restricted content and avoid sensitive geometry patterns
- Machine-validated: emitted JSON must validate under KFM-STAC v11 rules

---

## 🗂️ Directory Layout

~~~text
📁 docs/search/drift/stac/templates/                         — DRIFT STAC JSON templates (governed)
├── 📄 README.md                                             — This guide
├── 🧾 item.retrieval-episode.template.json                  — STAC Item template (retrieval episode)
├── 🧾 collection.drift-retrieval.template.json              — STAC Collection template (episode grouping)
├── 🧾 asset.roles.template.json                             — Canonical asset role map (roles + mediaTypes)
├── 🧾 properties.kfm-drift.template.json                    — Canonical kfm:* property block (placeholders)
└── 📁 examples/                                             — Example filled outputs (non-sensitive)
    ├── 🧾 item.retrieval-episode.example.json                — Filled item example (redaction-safe)
    └── 🧾 collection.drift-retrieval.example.json            — Filled collection example
~~~

---

## 🧭 Context

DRIFT Search can emit STAC as a first-class retrieval trace:

- each run is an auditable “episode” with inputs, outputs, and governance decisions
- STAC Items provide portable references to:
  - the sanitized query bundle (or query hash),
  - the retrieval result bundle (references only),
  - the provenance bundle (PROV-O JSON-LD),
  - the policy / CARE gate report

Template posture:

- This directory is template-only and must remain **non-sensitive**.
- Geometry defaults SHOULD be `null` unless policy explicitly allows generalized geometry.

---

## 📦 Template placeholders

Templates MUST be populated using a deterministic substitution map.

Recommended placeholder set:

- `{{kfm_run_id}}` — stable run identifier (UUID or deterministic hash)
- `{{kfm_step_id}}` — stable step identifier within the run
- `{{query_hash}}` — normalized query hash (for dedupe)
- `{{created_utc}}` — ISO8601 timestamp (UTC)
- `{{start_utc}}`, `{{end_utc}}` — optional interval bounds
- `{{fair_category}}`, `{{care_label}}`, `{{classification}}`, `{{sensitivity_level}}`
- `{{sovereignty_gate}}` — `clear|restricted|conflict|unknown` (recommended)
- `{{policy_bundle_ref}}` — href to governance decision artifact (if emitted)
- `{{prov_bundle_ref}}` — href to PROV-O JSON-LD
- `{{openlineage_ref}}` — href to OpenLineage event bundle (if emitted)
- `{{results_ref}}` — href to retrieval results payload (references only)
- `{{query_ref}}` — href to sanitized query bundle (optional)

---

## 🧱 Deterministic generation contract

A compliant emitter SHOULD:

1. Select a template deterministically based on `item_kind`:
   - `retrieval-episode` (default)
   - `episode-collection` (optional)
2. Populate placeholders from a single run context object.
3. Serialize deterministically:
   - stable key ordering,
   - stable float formatting,
   - fixed locale and timezone,
   - no environment-dependent fields.
4. Validate:
   - STAC core + KFM-STAC v11 profile,
   - any local JSON schema rules for `kfm:*` properties (if enforced).

### ID policy

- STAC Item `id` MUST be stable and collision-resistant:
  - `urn:kfm:search:drift:retrieval:<run_id>:<step_id>`
- If `run_id` is derived, it SHOULD be deterministic from:
  - `query_hash`, `constraints`, `workflow_version`, `policy_bundle_hash`, `index_snapshot_id`.

---

## 🧾 Canonical STAC Item skeleton

This snippet demonstrates the expected shape (placeholders included). It is template-safe and does not embed restricted content.

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "id": "urn:kfm:search:drift:retrieval:{{kfm_run_id}}:{{kfm_step_id}}",
  "collection": "kfm-search-drift-episodes",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "{{created_utc}}",
    "start_datetime": "{{start_utc}}",
    "end_datetime": "{{end_utc}}",

    "kfm:semantic_document_id": "kfm-drift-search",
    "kfm:run_id": "{{kfm_run_id}}",
    "kfm:step_id": "{{kfm_step_id}}",
    "kfm:query_hash": "{{query_hash}}",

    "kfm:retrieval_mode": "global_to_local",
    "kfm:hyde_enabled": true,
    "kfm:graph_backend": "neo4j",
    "kfm:vector_backend": "llamaindex",

    "kfm:fair_category": "{{fair_category}}",
    "kfm:care_label": "{{care_label}}",
    "kfm:classification": "{{classification}}",
    "kfm:sensitivity_level": "{{sensitivity_level}}",
    "kfm:sovereignty_gate": "{{sovereignty_gate}}"
  },
  "assets": {
    "query": {
      "href": "{{query_ref}}",
      "type": "application/json",
      "roles": ["metadata", "input"]
    },
    "results": {
      "href": "{{results_ref}}",
      "type": "application/json",
      "roles": ["data", "output"]
    },
    "prov": {
      "href": "{{prov_bundle_ref}}",
      "type": "application/ld+json",
      "roles": ["metadata", "provenance"]
    },
    "openlineage": {
      "href": "{{openlineage_ref}}",
      "type": "application/json",
      "roles": ["metadata", "provenance"]
    },
    "policy": {
      "href": "{{policy_bundle_ref}}",
      "type": "application/json",
      "roles": ["metadata", "governance"]
    }
  },
  "links": [
    { "rel": "collection", "href": "./collection.json", "type": "application/json" }
  ]
}
~~~

---

## 🧪 Validation & CI/CD

Template changes SHOULD trigger:

- JSON parse validation (templates and examples)
- placeholder completeness check (no dangling `{{...}}` in examples)
- STAC validation (KFM-STAC v11 profile)
- governance lint checks (no secrets; no restricted URLs; no precise sensitive geometry patterns)
- Mermaid parse validation (if diagrams are edited)

---

## ⚖ FAIR+CARE & Governance

Templates MUST NOT encode:

- raw protected coordinates,
- restricted dataset endpoints,
- secrets, tokens, or signed URLs.

Templates MUST surface governance state explicitly (as placeholders or fixed keys):

- `kfm:care_label`
- `kfm:classification`
- `kfm:sensitivity_level`
- `kfm:sovereignty_gate`

Any change to required properties, asset role semantics, ID policy, or redaction posture requires FAIR+CARE review.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Standardized directory layout format and confirmed KFM-MDP v11.2.6 header/footer and fence profiles. |

---

<div align="center">

🧩 **KFM — DRIFT STAC Templates**  
Designed for Longevity · Governed for Integrity

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Back to DRIFT STAC](../README.md) ·
[🧭 DRIFT Search](../../README.md) ·
[🔍 Search Index](../../../README.md) ·
[🏛️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
