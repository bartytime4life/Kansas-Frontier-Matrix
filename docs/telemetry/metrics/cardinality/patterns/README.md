---
title: "📊 KFM v11 — Cardinality Patterns & Anti-Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metrics/cardinality/patterns/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry Governance · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/otel-metrics.json"
telemetry_schema: "../../../../schemas/telemetry/metric-cardinality-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Guideline"

header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "telemetry"
  applies_to:
    - "metrics"
    - "patterns"
    - "observability"

semantic_intent:
  - "governance"
  - "observability"
  - "patterns"
category: "Telemetry · Observability · Patterns"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Telemetry Governance Council"

ttl_policy: "24 months"
sunset_policy: "Supersedes prior pattern drafts"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/metrics/cardinality/patterns/README.md@v11.2.2"
  - "docs/telemetry/metrics/cardinality/patterns/README.md@v11.1.0"
  - "docs/telemetry/metrics/cardinality/patterns/README.md@v10.x"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../../schemas/json/telemetry-patterns-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/telemetry-patterns-v1-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:telemetry:metrics:cardinality:patterns:v11.2.6"
semantic_document_id: "kfm-telemetry-metric-cardinality-patterns-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metrics:cardinality:patterns:v11.2.6"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - timeline-generation
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Patterns"
    - "📉 Anti-Patterns"
    - "🧪 Validation & CI/CD"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "accessibility-check"
  - "footer-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  telemetry: "Transparent Metrics · Ethical Aggregates · Sustainable Intelligence"
  analysis: "Observability-Driven · Evidence-Led · FAIR+CARE Grounded"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_patterns_standard_v10"
---

<div align="center">

# 📊 **KFM v11 — Cardinality Patterns & Anti-Patterns**  
`docs/telemetry/metrics/cardinality/patterns/README.md`

**Purpose**  
Provide the **canonical pattern & anti-pattern library** governing all metric label behaviors in KFM v11.2.6.  
These patterns define how to instrument metrics **safely**, **deterministically**, and **FAIR+CARE-compliantly**, ensuring stability across Prometheus, Mimir, and Focus Mode AI narratives.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/telemetry/metrics/cardinality/patterns/
├── 📄 README.md               # This file — pattern & anti-pattern library
└── 📄 patterns.md             # Detailed examples (good vs bad implementations)
~~~

**Layout rules**  
- Use 📂 only for directories and 📄 only for files  
- No emojis inside ASCII connectors  
- Every directory MUST contain a README explaining its scope  

---

## 📘 Overview

This document defines the **approved cardinality patterns** and **explicit anti-patterns** that MUST be followed across all KFM telemetry systems.

It supports:

- Observability stability  
- Cost control (Mimir memory, Prometheus runtime)  
- Label governance  
- FAIR+CARE protection  
- Focus Mode explainability  

Patterns are binding unless superseded by governance.

---

## 🧱 Patterns

### ✔ Pattern 1 — Bounded Vocabulary Labels

Metric labels MUST come from a **finite, documented value list**.

Correct:

~~~text
status="ok"
layer="soil"
zoom_bin="9-12"
~~~

Why:

- Prevents unbounded growth  
- Guarantees deterministic queries  
- Simplifies Focus Mode lineage  

---

### ✔ Pattern 2 — Binning Required Dimensions

Zoom, resolution, elevation, and file size MUST use bins.

Correct:

~~~text
zoom_bin="5-8"
elev_bin="200-400"
size_class="medium"
~~~

---

### ✔ Pattern 3 — Normalized Paths

Paths MUST be normalized when referenced in logs or traces (never in metrics).

Correct:

~~~text
/api/user/:id/items/:id
/tiles/:z/:x/:y
~~~

---

### ✔ Pattern 4 — Stable Category Labels Only

Metrics MUST reflect categories, not literals.

Correct:

~~~text
dataset_release="v11.2"
method="merge"
component="tiler"
~~~

---

## 📉 Anti-Patterns

### ❌ Anti-Pattern 1 — Unique IDs as Labels

Incorrect:

~~~text
trace_id="5fa1c3d9"
feature_id="abc123"
user_id="991"
~~~

---

### ❌ Anti-Pattern 2 — Raw Paths in Labels

Incorrect:

~~~text
http_url="/tiles/11/345"
file_path="/var/data/hugefile.bin"
~~~

---

### ❌ Anti-Pattern 3 — Coordinates or Geospatial Labels

Incorrect:

~~~text
lat="38.99"
lon="-95.22"
~~~

---

### ❌ Anti-Pattern 4 — Per-Object Metric Naming

Incorrect:

~~~text
pod_name="tiler-95cd7f1c8f-zbg9x"
~~~

These patterns destroy series budgets and are quarantine-eligible.

---

## 🧪 Validation & CI/CD

CI MUST enforce:

- Metadata presence  
- Label validation against whitelist  
- Forbidden label detection  
- Pattern compliance from this doc  
- Provenance & footer correctness  

Any violation MUST create:

- A governance ticket  
- A `review-log/` entry  
- A Story Node seed  

---

## 🧠 Story Node & Focus Mode Integration

Each anti-pattern encountered MUST:

- Produce a Story Node seed  
- Capture lineage (`prov:Activity`)  
- Generate root-cause narrative  
- Become visible in Focus Mode timelines  

Patterns enable the AI to reason about:

- Cardinality health  
- Deployment impacts  
- Budget stability  

---

## ⚖ FAIR+CARE & Governance

This doc enforces ethical rule-sets:

- No personal identifiers  
- No precise coordinates  
- Minimal information exposure  
- Complete provenance  
- Transparent governance  

Quarantine workflows MUST follow:

`docs/telemetry/metrics/cardinality/governance.md`

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                      |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Updated to KFM-MDP v11.2.6; release and telemetry refs bumped to v11.2.6; footer and cross-links aligned; no pattern changes. |
| v11.2.2 | 2025-11-30 | Complete rewrite; aligned with KFM-MDP v11.2.2; added pattern classification, anti-patterns, and CI gates                    |
| v11.1.0 | 2025-08-15 | Introduced draft pattern list and partial whitelist enforcement                                                               |
| v10.x   | 2024-03-01 | Initial pattern notes                                                                                                        |

---

<div align="center">

📊 **KFM v11 — Cardinality Patterns & Anti-Patterns (v11.2.6)**  
Observability With Purpose · Deterministic Metrics · FAIR+CARE Telemetry  

[📘 Docs Root](../../../../../README.md) ·  
[📡 Telemetry Metrics Index](../../README.md) ·  
[📊 Metric Cardinality Standard](../README.md) ·  
[⚖ Cardinality Governance](../governance/README.md) ·  
[🧭 Standards Index](../../../standards/README.md) ·  
[⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🌿 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>