---
title: "🏺🔗 KFM v11.2.6 — Archaeology Story Node Relation Patterns (Safe Graph Modeling)"
path: "docs/story-nodes/domains/archaeology/templates/relation-patterns.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Relation Pattern Guide"
header_profile: "standard"
footer_profile: "standard"

domain: "archaeology"
intent: "kfm-archaeology-storynode-relpatterns"
lifecycle_stage: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:archaeology:relation-patterns:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-relation-patterns-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/archaeology/templates/relation-patterns.md"

immutability_status: "version-pinned"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked (Public-Safe Patterns)"
classification: "Generalized / Public-Safe"
sensitivity: "Cultural Heritage Graph Links (No site-disclosing details)"
sensitivity_level: "Moderate"
public_exposure_risk: "Low (when patterns are followed)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board + Indigenous Data Governance Board"

ttl_policy: "36 months"
sunset_policy: "Superseded by future v12 domain rewrite"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/templates/relation-patterns.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
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
    - "📘 Overview"
    - "⚖ Safety & Sovereignty Rules"
    - "🔗 Relation Pattern Library"
    - "🧩 Valid Relation Matrix"
    - "🧠 Story Node & Focus Mode Integration"
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

# 🔗 **Archaeology Story Node — Relation Patterns (KFM v11.2.6)**  
### *Safe Graph Modeling for Sites, Features, Surveys, Excavations & Interpretations*  

`docs/story-nodes/domains/archaeology/templates/relation-patterns.md`

**Purpose**  
Provide **canonical, governed relation patterns** for archaeology Story Nodes so graph links remain:  
**public-safe**, **sovereignty-aware**, and **consistent** across KFM Story Node ingest + Focus Mode.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Archaeology-8b5a2b" />
<img src="https://img.shields.io/badge/Relations-Governed-brightgreen" />
<img src="https://img.shields.io/badge/CARE-Sovereignty_Aware-gold" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            ├── 📄 README.md
            ├── 📝 notes/
            │   ├── 📄 README.md
            │   ├── 📄 backlog.md
            │   └── ⚖️ ethics-checklist.md
            └── 🧩 templates/
                ├── 📄 story-node-archaeology.md
                └── 📄 relation-patterns.md              # This file
~~~

---

## 📘 Overview

Archaeology Story Nodes rely on **structured relations** to:

- link **places**, **activities**, **documents**, and **interpretations**
- support **Focus Mode** navigation and safe narrative synthesis
- preserve **provenance** (PROV-O) and controlled semantics
- maintain **CIDOC-CRM** alignment where appropriate
- enforce **FAIR+CARE** and **Indigenous data sovereignty** constraints

All patterns in this guide are **public-safe by design** *when used as specified*.

**Prohibited (global rules):**
- any relation that implies an unpublished precise location
- any relation that exposes burial/sacred features or restricted site context
- any relation that asserts undocumented cultural affiliation or attribution
- any relation that embeds internal-only identifiers (site codes, permit IDs, landowner IDs)

---

## ⚖ Safety & Sovereignty Rules

### 1) Default posture: conservative
If a link would increase the chance of site targeting or sensitive inference:
- **omit the relation**, or
- link only to a **generalized region/policy/document**, or
- keep it as an internal draft until governance review completes.

### 2) Target IDs must be public-safe
Examples of acceptable targets:
- generalized places: `region:*`, `county:*`, `h3:*`, `watershed:*`
- public documents: `doc:*` (published scans, reports, articles)
- public orgs: `org:*` (institutions, agencies, programs)

Examples of unacceptable targets:
- `site:internal-######`
- `parcel:*`
- `landowner:*`
- any ID that encodes coordinates, route hints, or actionable locators

### 3) One primary `about`
Each Story Node MUST have exactly **one** primary `about` relation (see Pattern 1).

### 4) No “people graph” by default
Use `org:*` for most participation links. Person-level IDs are permitted **only** when:
- the person is a public author/PI already listed in public sources, and
- linking does not increase sensitive inference.

---

## 🔗 Relation Pattern Library

Each pattern defines:

- **Relation** (`rel`)
- **Meaning**
- **Alignment**
- **Rules**
- **Example**

---

### 🧱 Pattern 1 — Primary Association

#### `rel: "about"`
**Meaning:** This Story Node is primarily about a place or activity (generalized).  
**Alignment:** CIDOC (`E7 Activity`, `E27 Site`, `E53 Place`), PROV (`prov:Entity`/`prov:Activity` depending on modeling)  
**Rules:**
- Exactly **one** per Story Node.
- Do not point to internal site numbers or restricted records.
- For multi-phase occupations: prefer multiple Story Nodes, each with its own `about`.

**Example:**
~~~json
{ "rel": "about", "id": "place:arch-ks-165-lower-walnut-village" }
~~~

---

### 📚 Pattern 2 — Documentation & Data References

#### `rel: "references"`
**Meaning:** This Story Node cites a public document, dataset, or publication.  
**Alignment:** CIDOC (`E31 Document`), DCAT/STAC via referenced identifiers (non-normative link)  
**Rules:**
- Only published/public-safe materials.
- Prefer stable identifiers; include STAC/DCAT IDs where available.

**Example:**
~~~json
{ "rel": "references", "id": "doc:kshs-archaeology-report-1973" }
~~~

---

### 🪶 Pattern 3 — Counter-Interpretation / Reinterpretation

#### `rel: "counterpoint"`
**Meaning:** This Story Node provides a documented alternative or updated interpretation.  
**Alignment:** CIDOC (`E13 Attribute Assignment`)  
**Rules:**
- Must be evidence-backed and stated in narrative.
- Must not be AI-invented.
- Use to connect documented interpretive disagreement or revision.

**Example:**
~~~json
{ "rel": "counterpoint", "id": "story:arch-ks-165-village-phase-1" }
~~~

---

### 🧩 Pattern 4 — Part–Whole Structure (Feature ↔ Site/Complex)

#### `rel: "part-of"`
**Meaning:** This node describes a subcomponent (feature/locus/phase) of a generalized parent.  
**Alignment:** CIDOC (`P46 is composed of`)  
**Rules:**
- Safe only if the subcomponent description is generalized and non-targetable.
- Do not use for burials/sacred features; omit or generalize at a higher level.

**Example:**
~~~json
{ "rel": "part-of", "id": "place:arch-ks-089-river-bluff-site" }
~~~

---

### 🏛️ Pattern 5 — Activity Attribution (Who carried it out)

#### `rel: "carried-out-by"`
**Meaning:** An activity (survey/excavation/archive processing) was carried out by an agent (prefer org).  
**Alignment:** CIDOC (`P14 carried out by`), PROV (`prov:wasAssociatedWith`)  
**Rules:**
- Prefer `org:*` over `person:*`.
- Only use documented public attributions.

**Example:**
~~~json
{ "rel": "carried-out-by", "id": "org:kansas-anthropological-association" }
~~~

---

### 👥 Pattern 6 — Participation (Use sparingly)

#### `rel: "participated-in"`
**Meaning:** A documented participant is connected to an activity (rare for public-safe nodes).  
**Alignment:** CIDOC (`P11 had participant`)  
**Rules:**
- Use only for clearly public contributors (authors, PIs).
- Avoid volunteer lists; omit when not essential.

**Example:**
~~~json
{ "rel": "participated-in", "id": "person:public-author-001" }
~~~

---

### 🌎 Pattern 7 — Coarse Location (Generalized only)

#### `rel: "located-in"`
**Meaning:** The subject falls within a coarse region/county/watershed/H3 cell.  
**Alignment:** CIDOC (`P89 falls within`), GeoSPARQL (non-normative)  
**Rules:**
- Do not use precise admin units smaller than policy allows.
- Prefer watershed/county/region for public-safe outputs.

**Example:**
~~~json
{ "rel": "located-in", "id": "region:kansas-arkansas-river-basin" }
~~~

---

### ⚖ Pattern 8 — Sovereignty / CARE Review Flag

#### `rel: "requires-review"`
**Meaning:** This Story Node requires CARE/sovereignty review or has constraints.  
**Alignment:** Rights/Policy marker (CIDOC `E30 Right` pattern; PROV policy annotation)  
**Rules:**
- Use for Indigenous-linked or culturally sensitive content.
- Link to a policy node or governance handle, not private reviewer info.

**Example:**
~~~json
{ "rel": "requires-review", "id": "policy:indigenous-data-sovereignty" }
~~~

---

## 🧩 Valid Relation Matrix

~~~text
about             → place:* | event:* | activity:*         (exactly one)
references        → doc:* | dataset:* | stac:* | dcat:*      (public-safe only)
counterpoint      → story:*                              (documented reinterpretation only)
part-of           → place:*                              (generalized parent; never burials)
carried-out-by    → org:* (preferred) | person:* (rare)   (documented/public)
participated-in   → person:* (rare)                      (documented/public)
located-in        → region:* | county:* | watershed:* | h3:*  (coarse only)
requires-review   → policy:*                             (sovereignty/CARE flags)
~~~

**Quick anti-examples (do not do this):**
~~~text
about → site:internal-12345
located-in → parcel:17-123-45-678-90
references → doc:restricted-field-form-scan
carried-out-by → person:volunteer-list-2021
~~~

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode MAY:
- use these relations to construct safe navigation paths (story → document → generalized place)
- show provenance-aware “why linked” explanations

Focus Mode MUST NOT:
- infer cultural affiliation from `located-in`
- treat `references` as proof of a claim without narrative support
- auto-generate new relations not present in the Story Node (no “invented graph edges”)

If Focus Mode proposes a new relation during drafting workflows, it MUST be treated as a **suggestion** and must be approved via governance review before inclusion.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; corrected relative links; added directory layout, sovereignty safety rules, and an explicit relation matrix with anti-examples. |
| v11.2.2 | 2025-11-30 | Initial governed relation-pattern library for archaeology Story Nodes. |
| v11.2.1 | 2025-11-29 | Added pattern scaffolding and CIDOC/GeoSPARQL mapping notes.           |

---

<div align="center">

🔗 **Archaeology Relation Patterns (v11.2.6)**  
Public-Safe Graph Links · Sovereignty-Aware · Governance-Ready

[🏺 Archaeology Domain](../README.md) ·
[🧩 Templates](./story-node-archaeology.md) ·
[📝 Notes](../notes/README.md) ·
[📋 Backlog](../notes/backlog.md) ·
[⚖️ Ethics Checklist](../notes/ethics-checklist.md) ·
[📚 Story Nodes Root](../../../README.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
