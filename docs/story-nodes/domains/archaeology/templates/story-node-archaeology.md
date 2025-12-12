---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Template (Markdown Authoring)"
path: "docs/story-nodes/domains/archaeology/templates/story-node-archaeology.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template"
template_type: "markdown-authoring-template"

domain: "archaeology"
intent: "kfm-archaeology-storynode-template"
governance_level: "FAIR+CARE · Indigenous Data Sovereignty"
masking_required: true

schema_ref: "../../../../../schemas/json/story-node.schema.json"
schema_shape_ref: "../../../../../schemas/shacl/story-node.shape.ttl"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked (Template)"
classification: "Public-Safe Template"
sensitivity: "Cultural Heritage Authoring Guidance (No site details)"
sensitivity_level: "Moderate (process-level only)"
public_exposure_risk: "Low (if kept non-site-specific)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board + Indigenous Data Governance Board"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:storynodes:archaeology:template:markdown:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-template-markdown-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/archaeology/templates/story-node-archaeology.md"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/templates/story-node-archaeology.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

header_profile: "standard"
footer_profile: "standard"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "🧩 Author Instructions"
    - "🏺 Story Node Template"
    - "✅ Pre-Review Checklist"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🏺 **Archaeology Story Node — Authoring Template**  
### *Generalized · Ethical · FAIR+CARE-Compliant Narrative Structure*  

`docs/story-nodes/domains/archaeology/templates/story-node-archaeology.md`

**Purpose**  
Provide a copy-ready template to author archaeology Story Nodes that are **public-safe by default**,  
**sovereignty-aware**, and consistent with KFM v11 Story Node conventions.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Domain-Archaeology-8b5a2b" />
<img src="https://img.shields.io/badge/Masking-Required-orange" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            ├── 📄 README.md
            ├── 📄 relation-patterns.md                 # Expected: approved link patterns (if present)
            ├── 📝 notes/
            │   ├── 📄 README.md
            │   ├── 📄 backlog.md
            │   └── ⚖️ ethics-checklist.md
            └── 🧩 templates/
                └── 📄 story-node-archaeology.md         # This file
~~~

---

## 🧩 Author Instructions

### Non-negotiables (policy)

- **Do not** include precise site coordinates, parcel boundaries, or “how to find it” directions.
- **Do not** mention burial locations, sacred locations, restricted knowledge, or internal site codes.
- **Do not** include unpublished field photos or scans that reveal actionable site detail.
- **Do** use generalized geometries (H3/county/watershed/region) or **no geometry** if required.
- **Do** separate:
  - **Observation** (what is documented),
  - **Interpretation** (supported inference),
  - **Uncertainty** (limits/conflicts).
- **Do** keep temporal precision honest (avoid day-level precision unless truly warranted).
- **Do** use approved relationship patterns (see `relation-patterns.md` if available).

### Validation target

Story Nodes authored from this template MUST validate against:

- `schemas/json/story-node.schema.json`

---

## 🏺 Story Node Template

> Copy this section into a new Story Node file and fill in all fields.
> Keep content public-safe by default; when in doubt, generalize further.

---

### 🧾 Metadata

**ID (public-safe)**  
Format (recommended): `arch-ks-{county-fips}-{slug}-{nn}`  
Example: `arch-ks-165-lower-walnut-village-01`

**Title**  
Short, descriptive, generalized.  
Example: *Generalized Protohistoric Settlement Near Lower Walnut Creek*

**Summary (2–3 sentences)**  
Used for previews and Focus Mode cards. Avoid precise identifiers.

**CARE / Sensitivity Statement (1–2 sentences)**  
State what was generalized/withheld and why.

---

### 📖 Narrative

#### 1) Context & Description (Observation)

Describe what is *documented* in a generalized, non-sensitive way:

- features (general forms only),
- material categories (general classes),
- archival references (published/public only),
- setting (regional terms only).

**Avoid**: exact counts, internal codes, site access routes, or specific landowner references.

---

#### 2) Interpretation (Supported Inference)

Explain supported interpretations:

- cultural period framing **only when documented**,
- settlement pattern interpretation **only when evidence-linked**,
- alternative hypotheses if relevant.

Include references (reports/datasets) that justify the inference.

---

#### 3) Uncertainty & Debates

Document limits:

- dating uncertainty,
- survey bias,
- preservation issues,
- conflicting interpretations.

Avoid “filling in gaps.”

---

#### 4) Archaeological Methods (Generalized)

Describe methods safely:

- survey type (pedestrian, geophysics, LiDAR, archival),
- generalized date window (year/decade, not day),
- documentation methods (mapping, scanning, sampling).

Do not expose restricted forms or operational details that enable targeting.

---

#### 5) Sovereignty & Ethical Notes (Required)

State:

- masking/generalization approach (H3 level / county / watershed / none),
- consultation status **without** including restricted knowledge,
- content withheld (high-level description only),
- narrative constraints (what you refused to claim).

---

### 🌐 Spacetime

#### Geometry (Generalized GeoJSON)

Choose one:

- county polygon,
- watershed polygon,
- broad region polygon,
- H3-derived generalized polygon,
- **null / omitted** (metadata-only node).

~~~json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [/* generalized / public-safe only */]
  },
  "properties": {
    "masking_level": "H3-6",
    "masking_method": "h3_generalized",
    "public_safe": true
  }
}
~~~

#### Temporal bounds

- **Start:** `YYYY` or ISO-8601 interval start
- **End (optional):** `YYYY` or interval end
- **Precision:** `"century" | "year" | "year-range" | "decade"`
- **Original label (if applicable):** e.g., `"Protohistoric, ca. 1450–1650 CE"`

---

### 🔗 Relations (Graph Links)

Use only approved patterns from `relation-patterns.md` (if present). Keep targets public-safe.

~~~json
[
  { "rel": "about", "id": "place:arch-ks-165-lower-walnut-village" },
  { "rel": "references", "id": "doc:kshs-1973-arch-report" },
  { "rel": "counterpoint", "id": "story:arch-ks-165-reinterpretation-01" }
]
~~~

---

### 🗃 Sources & Provenance

List (public/releasable only):

- published reports,
- datasets (STAC/DCAT IDs if available),
- maps/atlases,
- peer-reviewed articles,
- digitized archival items with clear rights.

**Do not** cite restricted internal forms or unpublished coordinates.

Suggested structure:

- **Primary sources**
- **Secondary sources**
- **Data products (STAC/DCAT)**
- **Provenance notes (how this was derived)**

---

### 🖼️ Media (Optional, STAC-Linked)

Only include generalized, non-sensitive media.

~~~json
[
  {
    "href": "https://example.org/stac/collection/item/assets/preview.png",
    "title": "Generalized Context Figure",
    "mime": "image/png",
    "license": "CC-BY 4.0"
  }
]
~~~

---

## ✅ Pre-Review Checklist

Before submitting for review, confirm:

- [ ] No precise coordinates, no access directions, no internal codes.
- [ ] Geometry is generalized (or omitted) and cannot be triangulated by narrative.
- [ ] Observation vs interpretation vs uncertainty are clearly separated.
- [ ] Rights/licensing for sources and media are explicit.
- [ ] Relations use approved patterns and link only to public-safe entities.
- [ ] CARE and sovereignty notes are present and honest.
- [ ] Validates against `story-node.schema.json` (or is ready for conversion to schema-valid JSON/MD).

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; added directory layout, corrected schema path, strengthened sovereignty guardrails, and added pre-review checklist. |
| v11.2.2 | 2025-11-30 | Initial governed archaeology Markdown template for Story Nodes.          |
| v11.2.1 | 2025-11-29 | Added author instructions, spacetime rules, and sovereignty notes.       |

---

<div align="center">

🏺 **Archaeology Story Node Template (v11.2.6)**  
Public-Safe by Default · Sovereignty-Aware · Governance-Ready

[📄 Archaeology Domain](../README.md) ·
[📝 Notes](../notes/README.md) ·
[📋 Backlog](../notes/backlog.md) ·
[⚖️ Ethics Checklist](../notes/ethics-checklist.md) ·
[📚 Story Nodes Root](../../../README.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🧩 Story Node Schema](../../../../../schemas/json/story-node.schema.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
