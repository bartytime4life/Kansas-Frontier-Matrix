---
title: "📊 KFM v11 — Metric Cardinality Patterns & Anti-Patterns (Detailed Examples)"
path: "docs/telemetry/metrics/cardinality/patterns/patterns.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Telemetry Governance · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/otel-metrics.json"
telemetry_schema: "../../../../../schemas/telemetry/metric-cardinality-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

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
doc_kind: "Guideline-Examples"

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
sunset_policy: "Supersedes prior pattern example drafts"

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
  - "docs/telemetry/metrics/cardinality/patterns/patterns.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../../../schemas/json/telemetry-patterns-v1.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/telemetry-patterns-v1-shape.ttl"

story_node_refs: []
immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:telemetry:metrics:cardinality:patterns:examples:v11.2.6"
semantic_document_id: "kfm-telemetry-metric-cardinality-patterns-examples-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:metrics:cardinality:patterns:examples:v11.2.6"

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
    - "🧱 Patterns (Approved)"
    - "📉 Anti-Patterns (Prohibited)"
    - "🧪 CI Enforcement Examples"
    - "🧠 Story Node & Focus Mode Integration"
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
requires_directory_layout_section: false
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_patterns_standard_v10"
---

<div align="center">

# 📊 **Metric Cardinality Patterns & Anti-Patterns — Detailed Examples**  
`docs/telemetry/metrics/cardinality/patterns/patterns.md`

**Purpose**  
Provide the **complete, example-rich expansion** of the governed patterns & anti-patterns defined in this directory’s README.  
This file supplies **explicit, concrete “good vs bad” examples** for engineering, CI validation, and Story Node generation.

</div>

---

## 🧱 Patterns (Approved)

### ✔ Pattern 1 — Use **Bounded Vocabularies**

Metric label values MUST come from a **finite**, **documented**, **stable** list.

**Correct**

~~~text
status="ok"
status="error"
layer="soil"
layer="precip"
~~~

**Why it matters**

- Prevents unbounded growth from free-text values  
- Enables deterministic aggregation  
- Simplifies Focus Mode entity linking  

---

### ✔ Pattern 2 — Apply **Binning** to Range-Like Dimensions

Zoom, elevation, resolution, and file size MUST be **bucketed**.

**Correct**

~~~text
zoom_bin="5-8"
elev_bin="200-400"
size_class="medium"
resolution="high"
~~~

**Incorrect**

~~~text
zoom="11"
elev="237"
filesize_bytes="4892334"
~~~

---

### ✔ Pattern 3 — Normalize Paths / URLs (Never Use Literal Values)

Paths belong in **logs** or **traces**, not labels.

**Correct**

~~~text
/api/user/:id/items/:id
/tiles/:z/:x/:y
~~~

**Incorrect**

~~~text
file_path="/home/worker/tmp/load/8138.tif"
http_url="/tiles/11/345/892"
~~~

---

### ✔ Pattern 4 — Encode **Categories**, Not **Instances**

Labels should reflect **types**, **modes**, or **buckets** — never specific objects.

**Correct**

~~~text
method="merge"
component="tiler"
dataset_release="v11.2"
phase="ingest"
~~~

**Incorrect**

~~~text
instance="tiler-95cd7f1c8f-zbg9x"
pod_id="tiler-8bcdf4"
host="node-14"
~~~

---

### ✔ Pattern 5 — Use **Enumerated Status Labels**

Status MUST be chosen from the predefined vocabulary.

Allowed values:

- `ok`
- `success`
- `error`
- `timeout`
- `retry`
- `skipped`

**Correct**

~~~text
status="ok"
status="timeout"
~~~

**Incorrect**

~~~text
status="weird-half-broken-state"
status="409"
~~~

---

## 📉 Anti-Patterns (Prohibited)

### ❌ Anti-Pattern 1 — Using Unique IDs as Labels

These destroy Active Series Budgets.

~~~text
trace_id="54bdfe1"
session_id="a8f1d19c"
feature_id="abc123"
user_id="991"
~~~

Governed Response:

- Immediate **quarantine**  
- **deny-match** for offending metric  
- **Story Node seed** created  
- Entry added to **review-log**  

---

### ❌ Anti-Pattern 2 — Coordinates or H3 Cells

Geospatial values cause unbounded series growth.

~~~text
lat="38.992"
lon="-95.226"
h3="8f28308280f1fff"
~~~

Correct placement:

- Traces → allowed  
- Logs → allowed  
- Metrics → **forbidden**  

---

### ❌ Anti-Pattern 3 — Raw Paths / URLs in Labels

~~~text
file_path="/opt/data/bigfile/2025/11/30/data.csv"
http_url="/tiles/13/2201/1511"
~~~

Use normalized placeholders instead.

---

### ❌ Anti-Pattern 4 — Free-Form Label Values

~~~text
why="sometimes it just crashes when the moon is out"
reason="missing metadata for collection but it works on my machine"
~~~

Any uncontrolled string is automatically a cardinality leak.

---

### ❌ Anti-Pattern 5 — Per-Entity Metric Naming

~~~text
kfm_graph_upserts_feature_abc123_total
kfm_tile_latency_13_2201_1511_seconds
~~~

Metrics must be **family-stable**, with differences expressed using **allowed labels** (bounded).

---

## 🧪 CI Enforcement Examples

### CI MUST FAIL the following samples:

~~~text
kfm_ingest_total{http_url="/tiles/11/345"}               # forbidden label
kfm_tile_build_seconds{stac_id="20251130T2100Z"}         # per-object ID
kfm_graph_upserts_total{feature_id="abc123"}             # unbounded value
kfm_ingest_total{lat="38.99", lon="-95.22"}              # coordinates
~~~

### CI MUST PASS the following samples:

~~~text
kfm_ingest_total{dataset="usgs_hydro", status="ok"}
kfm_tile_build_seconds{layer="soil", zoom_bin="9-12"}
kfm_graph_upserts_total{op="merge", dataset_release="v11.2"}
~~~

---

## 🧠 Story Node & Focus Mode Integration

Pattern and anti-pattern events generate narrative-grade material.

### When an anti-pattern appears:

- Create a **Story Node seed** describing the anomaly  
- Attach PROV-O lineage (activity → agent → entity)  
- Add an entry to `review-log.md`  
- Link the event to:
  - deployment commit  
  - service  
  - environment  

### Focus Mode MAY surface:

- “Spike Timeline”  
- “New Label Introduced”  
- “ASB Violation”  
- “Remediation Sequence”  

Patterns, meanwhile, act as **rulesets** Focus Mode uses for:

- Explaining why certain labels are allowed  
- Highlighting which labels are dangerous  
- Understanding how metrics relate to governance  

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                   |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Added full KFM v11.2.6 metadata front matter; aligned paths, governance links, and telemetry references; no example changes. |
| v11.2.2 | 2025-11-30 | Initial detailed example file aligned with cardinality patterns README; established “good vs bad” example library.        |

---

<div align="center">

📊 **KFM v11 — Metric Cardinality Patterns**  
Deterministic Metrics · Sustainable Telemetry · FAIR+CARE-Aligned  

[⬅ Back to patterns README](./README.md)

</div>