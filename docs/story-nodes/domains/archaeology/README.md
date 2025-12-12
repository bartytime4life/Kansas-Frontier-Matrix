---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Domain (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/archaeology/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Domain Specification"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:archaeology:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-domain-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/archaeology/README.md"
immutability_status: "version-pinned"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-v11.json"
schema_ref: "../../../schemas/json/story-node.schema.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"

intent: "kfm-archaeology-storynode-domain"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
sensitivity: "Cultural heritage narratives (generalized)"
sensitivity_level: "Moderate"
public_exposure_risk: "Low (when masking rules are followed)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Archaeology Domain Board + Indigenous Data Governance Board"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded by future v12 domain rewrite"

metadata_profiles:
  - "CIDOC-CRM (alignment)"
  - "GeoSPARQL (alignment)"
  - "OWL-Time (alignment)"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/README.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

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

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🏺 **Archaeology Story Node Domain (KFM v11.2.6)**  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
### *Generalized · Ethical · FAIR+CARE-Aligned Archaeological Narratives*  

`docs/story-nodes/domains/archaeology/README.md`

**Purpose**  
Define how archaeology-related Story Nodes MUST be authored, structured, masked, validated,  
and linked into the KFM graph and Focus Mode v3 — without exposing sensitive cultural heritage details.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Archaeology-brightgreen" />
<img src="https://img.shields.io/badge/CARE-Indigenous--Linked-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            ├── 📄 README.md                           # Domain overview & authoring rules (this file)
            ├── 📄 glossary.md                         # Public-safe domain terminology (governed)
            │
            ├── 📂 🧩 templates/                       # Authoring templates + relation patterns
            │   ├── 📄 README.md
            │   ├── 📝 story-node-archaeology.md       # Markdown authoring template
            │   ├── 🧩 story-node-archaeology.json     # JSON skeleton (schema-aligned)
            │   └── 🔗 relation-patterns.md            # Governed relation patterns
            │
            ├── 📂 📝 notes/                           # Drafts, ethics, backlog (internal-prep)
            │   ├── 📄 README.md
            │   ├── 📋 backlog.md
            │   └── ⚖️ ethics-checklist.md
            │
            └── 📂 🧪 examples/                        # Curated example Story Nodes (public-safe)
                ├── 🏞️ protohistoric-wichita-site.json
                ├── 🧲 fort-larned-geophysics.json
                └── 📄 ... (additional examples)
~~~

**Layout rules (normative)**  
- The ASCII connectors (`├──`, `│`, `└──`) remain plain for readability.  
- Folder entries include a folder marker (`📂`) plus a semantic emoji (e.g., `🧩`, `📝`, `🧪`).  
- Examples and templates MUST remain public-safe and non-targetable.

---

## 📘 Overview

This domain defines the **rules, structures, and constraints** for creating archaeology Story Nodes in KFM v11.

Archaeology Story Nodes MUST integrate:

- **Generalized spatial footprints** (never publish sensitive coordinates)  
- **Time intervals** with declared precision and clear uncertainty  
- **CIDOC-CRM**, **GeoSPARQL**, and **OWL-Time** alignment (where applicable)  
- **FAIR+CARE** + **Indigenous Data Sovereignty** governance rules  
- **STAC / DCAT** links for eligible public assets (when used)  
- **PROV-O provenance** for all referenced sources and transformations  

They MUST remain compatible with:

- Focus Mode v3 narrative + map rendering
- Story Node schema validation (`story-node.schema.json`)
- Graph insertion patterns (relations + safe linking)

---

## ✅ Domain Rules

### 1) Spatial safety is mandatory
Story Nodes MUST:

- Use generalized geometry: county, watershed, broad region, or coarse H3 masking.
- Avoid “how to find it” details (routes, landmarks, access points).
- Increase masking strength for any culturally sensitive or sovereignty-impacted content.

Story Nodes MUST NOT:

- Include precise coordinates.
- Include unpublished site codes or internal form identifiers.
- Encode sensitive location detail in IDs, filenames, or relations.

### 2) Observation vs. interpretation must be explicit
Every node MUST clearly separate:

- **Observation** — what is documented.
- **Interpretation** — what is supported by evidence.
- **Uncertainty** — what is unknown, disputed, or weakly supported.

Speculation is not allowed as “fact” and must not be presented as settled narrative.

### 3) Spacetime modeling must be correct
Nodes MUST model:

- `spacetime.geometry` as generalized GeoJSON (or equivalent safe geometry reference).
- `spacetime.when` with start/end bounds and a precision that matches evidence.
- Multi-phase sites as separate nodes (preferred) or as `part-of` structures that remain safe.

### 4) Relations must follow the governed patterns
Use only the relation patterns defined in:

- `templates/relation-patterns.md`

Minimum expectations:

- Exactly one primary `about` relation.
- `references` only to public-cleared sources.
- `counterpoint` only for documented reinterpretations.

### 5) Sovereignty governance is binding
If content is Indigenous-linked or culturally sensitive:

- CARE review requirements apply.
- Consultation and/or reviewer sign-off may be mandatory.
- Any exception MUST be recorded through governance procedure.

---

## 🧭 Focus Mode Integration

Focus Mode v3 MAY:

- Center on generalized geometry and domain timeline.
- Render phase-level stories using safe time bounds.
- Expand graph neighbors (safe 1–2 hop) using governed relation types.
- Surface uncertainty statements and governance flags.

Focus Mode MUST NOT:

- Invent, “fill in,” or infer missing cultural attribution.
- Convert uncertainty into confidence.
- Reveal sensitive location detail (directly or via derived hints).

---

## 📦 Metadata, Assets, and Provenance

### Public-safe IDs
Recommended ID pattern (public-safe):

~~~text
arch-ks-{county-fips}-{slug}-{nn}
~~~

IDs MUST NOT embed coordinates, site codes, or restricted identifiers.

### Assets
Allowed (if public-safe):

- generalized diagrams and maps
- non-sensitive photos already cleared for release
- masked rasters (geophysics, lidar derivatives) that cannot be used for targeting

Prohibited:

- burials / sacred features (any detail that increases risk)
- unpublished coordinates
- internal excavation forms, sensitive photos, or restricted field documentation

### Provenance
Every Story Node MUST carry provenance sufficient to answer:

- What sources support the observation?
- What processing or transformations occurred?
- What rights / license constraints apply?

---

## 🧪 Validation & Governance Gates

CI/CD SHOULD enforce (and governed branches MUST enforce):

- Story Node schema validation (`schema_ref`)
- Markdown protocol compliance (`KFM-MDP v11.2.6`)
- Link integrity checks (internal docs + schema refs)
- Sovereignty/CARE lint rules for archaeology domain
- Relation pattern validation (approved `rel` values and required structure)

Manual review requirements may include:

- Archaeology Domain Board approval
- Indigenous Data Governance Board / FAIR+CARE Council review (when flagged)

---

## ⚖ FAIR+CARE Compliance

This domain is treated as **culturally sensitive by default**, even when generalized.

Operational commitments:

- **Findable**: stable paths + consistent IDs + glossary alignment  
- **Accessible**: public-safe narratives only; restricted material excluded  
- **Interoperable**: governed relations + ontology alignment  
- **Reusable**: clear uncertainty, provenance, and licensing  

CARE commitments:

- No targeting.
- No restricted knowledge leakage.
- No individual-level surveillance or attribution.
- Governance decisions are documented and auditable.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; improved directory layout formatting; strengthened normative rules + links. |
| v11.2.2 | 2025-11-30 | Initial governed release; finalized emoji directory layout & v11.2.2 compliance. |
| v11.2.1 | 2025-11-29 | Added templates, examples, glossary, ethics notes; aligned to Story Node v11 schema. |

---

<div align="center">

🏺 **Archaeology Domain (v11.2.6)**  
Generalized Narratives · Sovereignty-Aware · Governance-Ready

[🧩 Templates Index](./templates/README.md) ·
[📝 Authoring Template](./templates/story-node-archaeology.md) ·
[🔗 Relation Patterns](./templates/relation-patterns.md) ·
[📖 Glossary](./glossary.md) ·
[📝 Notes Index](./notes/README.md) ·
[⚖️ Ethics Checklist](./notes/ethics-checklist.md) ·
[📋 Backlog](./notes/backlog.md) ·
[📚 Story Nodes Root](../../README.md) ·
[📘 Docs Home](../../../README.md) ·
[📘 Standards Index](../../../standards/README.md) ·
[🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🧾 Story Node Schema](../../../schemas/json/story-node.schema.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
