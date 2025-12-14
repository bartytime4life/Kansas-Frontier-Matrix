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
Provide **governed, deterministic JSON templates** for emitting STAC Collections/Items that represent **DRIFT retrieval episodes** (global→local hybrid retrieval), including required **PROV anchors** and **CARE-aware redaction gates**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/STAC-KFM--STAC_v11-brightgreen" />
<img src="https://img.shields.io/badge/PROV-KFM--PROV_v11-blue" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory contains **STAC JSON templates** used by DRIFT Search to generate:

- **STAC Items** for each retrieval episode (user query + DRIFT steps),
- optional **Collections** for grouping items by release, environment, or run-family,
- consistent **assets + properties** that bind retrieval outputs to **PROV-O/OpenLineage** artifacts and **CARE governance flags**.

Design goals:

- **Deterministic output**: same inputs → identical STAC JSON (stable `id`, stable property keys, stable asset layout).
- **Provenance-first**: every Item has explicit links to provenance bundles and safety/CARE decisions.
- **Safety by default**: templates avoid leaking sensitive details (no raw protected coordinates, no restricted dataset URLs).
- **Machine-validated**: output must pass the pinned STAC validation profile (KFM-STAC v11).

---

## 🗂️ Directory Layout

~~~text
docs/search/drift/stac/templates/                 — DRIFT STAC JSON templates (governed)
├── README.md                                    — This guide
├── item.retrieval-episode.template.json          — STAC Item template for a DRIFT retrieval episode
├── collection.drift-retrieval.template.json      — STAC Collection template for DRIFT retrieval episodes
├── asset.roles.template.json                     — Canonical asset role map (roles + mediaTypes)
├── properties.kfm-drift.template.json            — Canonical kfm:* property block (placeholders)
└── examples/                                     — Example filled outputs (non-sensitive)
    ├── item.retrieval-episode.example.json
    └── collection.drift-retrieval.example.json
~~~

---

## 🧭 Context

DRIFT Search emits STAC as a **first-class retrieval trace**:

- a retrieval run is treated as an auditable “episode” with inputs, outputs, and governance decisions,
- STAC Items provide **portable references** to:
  - the query bundle (sanitized),
  - the retrieval result bundle,
  - the graph traversal trace (if allowed),
  - the provenance bundle (PROV-O JSON-LD),
  - the safety/CARE gate report.

Default posture:

- **Non-spatial** STAC Items are allowed when spatial details are sensitive or not meaningful:
  - `geometry: null`
  - `bbox: null`
- When spatial is permitted, prefer **generalized footprints** (e.g., region polygon or H3-coarsened geometry) over point precision.

---

## 📦 Data & Metadata

### Template placeholders (normative)

Templates MUST be populated using a deterministic substitution map.

Recommended placeholder set:

- `{{kfm_run_id}}` — stable run identifier (UUID or deterministic hash)
- `{{kfm_step_id}}` — stable step identifier within the run
- `{{query_hash}}` — normalized query hash (for dedupe)
- `{{created_utc}}` — ISO8601 timestamp (UTC)
- `{{start_utc}}`, `{{end_utc}}` — optional interval bounds
- `{{care_label}}`, `{{fair_category}}`, `{{classification}}`, `{{sensitivity_level}}`
- `{{sovereignty_gate}}` — `true|false` (string/boolean per profile)
- `{{policy_bundle_ref}}` — href to the governance decision artifact (if emitted)
- `{{prov_bundle_ref}}` — href to PROV-O JSON-LD
- `{{openlineage_ref}}` — href to OpenLineage event bundle (if emitted)
- `{{graph_trace_ref}}` — href to traversal trace (if emitted and allowed)
- `{{results_ref}}` — href to retrieval results payload
- `{{query_ref}}` — href to sanitized query bundle

### Canonical STAC Item skeleton (template shape)

This is the expected **shape**, not the exact file contents:

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [],
  "id": "urn:kfm:search:drift:retrieval:{{kfm_run_id}}:{{kfm_step_id}}",
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
  "links": []
}
~~~

### Asset rules (normative)

- Assets MUST be:
  - content-addressable where possible (checksummed bundles),
  - non-secret (no tokens, no signed URLs),
  - compliant with CARE gates (restricted artifacts are not linked unless the access model is explicit and approved).

- If an artifact is restricted:
  - omit the asset link, or
  - link only to a governed, access-controlled catalog endpoint (never direct storage URLs).

---

## 🧱 Architecture

### Deterministic generation contract

A compliant STAC emission pipeline SHOULD:

1. Choose template file(s) deterministically based on `item_kind`:
   - `retrieval-episode` (default)
   - `retrieval-collection` (optional)
2. Populate placeholders from a **single run context object**.
3. Normalize output JSON for stability:
   - stable key ordering (serializer-level),
   - stable float formatting,
   - canonical boolean casing,
   - no environment-dependent fields (locale/TZ).
4. Validate against:
   - STAC core + KFM-STAC v11 profile,
   - any local JSON schema rules for `kfm:*` properties.

### ID policy (recommended)

- STAC Item `id` MUST be stable and collision-resistant:
  - `urn:kfm:search:drift:retrieval:<run_id>:<step_id>`
- If `run_id` is generated:
  - prefer deterministic derivation from `(query_hash, start_utc, policy_version, engine_version)`.

---

## 🗺️ Diagrams

The templates are used as a deterministic emission stage in DRIFT retrieval.

~~~mermaid
flowchart LR
  A["DRIFT run context"] --> B["Select template"]
  B --> C["Populate placeholders"]
  C --> D["Validate STAC profile"]
  D -->|pass| E["Write STAC Item JSON"]
  D -->|fail| F["Fail CI gate"]
~~~

Explanation: DRIFT emits STAC only after placeholders are populated and the resulting JSON validates against the governed profile.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Templates produce STAC Items that act as **retrieval episode records**.
- Non-spatial mode is allowed (`geometry: null`) to prevent leaking sensitive location details.
- `assets.prov` anchors the Item to PROV-O lineage.

### DCAT

- Retrieval STAC Items may be mirrored as DCAT distributions:
  - the STAC Item JSON is a `dcat:Distribution` (machine output),
  - provenance and governance bundles are referenced as additional distributions.

### PROV-O

- Each Item SHOULD have a corresponding PROV bundle:
  - `prov:Entity` = the STAC Item and each emitted artifact,
  - `prov:Activity` = the retrieval run step,
  - `prov:Agent` = DRIFT executor + governance reviewers/bots,
  - `prov:used` and `prov:wasGeneratedBy` link inputs/outputs.

---

## 🧠 Story Node & Focus Mode Integration

Templates are designed so Focus Mode can:

- locate the retrieval episode via STAC `id`,
- read provenance/governance bundles via the `assets` map,
- summarize results while respecting:
  - `kfm:classification`,
  - `kfm:sensitivity_level`,
  - `kfm:sovereignty_gate`,
  - any explicit redaction flags in the policy asset.

Focus Mode MUST NOT:

- dereference restricted assets when `kfm:sovereignty_gate=true`,
- infer or reconstruct protected spatial coordinates from generalized geometries.

---

## 🧪 Validation & CI/CD

Minimum expected checks for any template change:

- `markdown-lint` (structure: H1/H2, fences, ordering)
- `schema-lint` (front-matter conformance)
- `footer-check` (governance links + ordering)
- `secret-scan` / `pii-scan`
- template JSON validation:
  - parseable JSON
  - placeholder set completeness (no dangling `{{...}}` in example outputs)
- STAC validation:
  - pinned validator versions
  - KFM-STAC v11 profile rules enforced

---

## ⚖ FAIR+CARE & Governance

- Templates MUST not encode:
  - raw protected site coordinates,
  - tribal/sovereign restricted dataset endpoints,
  - any access tokens or credentials.

- Templates MUST expose governance state as explicit fields:
  - `kfm:care_label`
  - `kfm:classification`
  - `kfm:sensitivity_level`
  - `kfm:sovereignty_gate`

- Any change to:
  - required `kfm:*` properties,
  - asset role semantics,
  - ID policy,
  - redaction posture

…requires review under FAIR+CARE governance.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-13 | Initial governed templates guide for DRIFT STAC template emission and validation posture. |

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
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

