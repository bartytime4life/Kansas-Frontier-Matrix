---
title: "🏺 KFM v11.2.6 — Archaeology Story Node Notes"
path: "docs/story-nodes/domains/archaeology/notes/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Notes Directory README"
intent: "kfm-archaeology-storynode-notes"
lifecycle_stage: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:notes:v11.2.6"
semantic_document_id: "kfm-storynodes-archaeology-notes"
event_source_id: "ledger:storynodes/archaeology/notes"
immutability_status: "version-pinned"

provenance_chain:
  - "docs/story-nodes/domains/archaeology/notes/README.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

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
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 notes structure"

header_profile: "standard"
footer_profile: "standard"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
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
    - "🧭 Role in the KFM Story Node Pipeline"
    - "🎯 Types of Material Allowed"
    - "🧪 Redaction & Generalization Rules"
    - "📜 Workflow Integration"
    - "✅ Promotion Checklist (Notes → Story Node)"
    - "🧰 Validation & Quality Gates"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🏺 **Archaeology Story Node — Notes (KFM v11)**  
### *Drafts · Backlog · Sovereignty Reviews*  

`docs/story-nodes/domains/archaeology/notes/README.md`

**Purpose**  
Provide a workspace for **draft Story Nodes**, **ethics/sovereignty deliberation notes**,  
and **pending backlog items** for the archaeology domain.

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 🏺 archaeology/
            └── 📝 notes/
                ├── 📄 README.md            # This file (notes directory index + guardrails)
                ├── 📑 backlog.md           # Candidate Story Nodes & work queue (generalized)
                └── ⚖️ ethics-checklist.md  # Sovereignty + CARE review checklist (non-sensitive)
~~~

Notes:

- This directory is **development and review** material, not the canonical Story Node library.
- Contents MUST remain **public-safe** and **generalized**. If something cannot be safely public, it does not belong here.

---

## 📘 Overview

The archaeology **notes** directory serves as the staging area for:

- Draft Story Node concepts and early outlines.
- Sovereignty considerations and ethical deliberation notes (high-level only).
- Masking decisions and generalization choices (e.g., H3 generalization level, “region-only” decisions).
- Questions and action items for domain reviewers or partner consultation (without restricted detail).
- Backlog items awaiting triage into official Story Nodes and examples.

Nothing in this directory is considered final until it passes:

1. Archaeology domain review,
2. Indigenous data sovereignty review (as applicable),
3. Story Node contract alignment (schema + governance requirements),
4. FAIR+CARE compliance checks.

---

## 🧭 Role in the KFM Story Node Pipeline

This directory is an **upstream, pre-publication workspace** in the narrative layer.

KFM narrative flow (conceptual):

Deterministic ETL  
→ STAC / DCAT / PROV catalogs  
→ Neo4j graph  
→ API layer  
→ Frontends (React / MapLibre / Cesium)  
→ Story Nodes and Focus Mode

Archaeology Story Nodes often sit at the end of that chain and MUST:

- Reference governed datasets (via STAC/DCAT identifiers where available).
- Reference graph entities (stable IDs), not ad-hoc strings.
- Represent time and place conservatively when content is sensitive.

These notes help authors get there safely by capturing:

- Candidate narratives,
- review questions,
- and safe generalization choices,
before anything is promoted into canonical Story Nodes.

---

## 🎯 Types of Material Allowed

Allowed (public-safe, generalized):

- ✔ Draft Story Node outlines (incomplete and awaiting citations is acceptable).
- ✔ High-level chronology, regional context, and archival research notes.
- ✔ Generalization decisions and rationale (why geometry was omitted or coarsened).
- ✔ CARE risk assessments (at the level of “low/moderate/high” and why).
- ✔ Backlog items to be converted into official examples/templates.
- ✔ Reviewer commentary that is safe to store.

Not permitted here (restricted, sensitive, or governance-prohibited):

- 🚫 Precise coordinates (any exact lat/lon, grid references, or direct site geolocation).
- 🚫 Burial or sacred locations.
- 🚫 Confidential site identifiers / codes and any “field-form” restricted details.
- 🚫 Restricted tribal knowledge or partner-only information.
- 🚫 Sensitive field photos or imagery that could enable site location inference.
- 🚫 Any content prohibited under sovereignty rules or data-sharing agreements.

If you cannot confidently classify it as public-safe, do not write it here.

---

## 🧪 Redaction & Generalization Rules

This directory is **Generalized / Public-Safe** by default.

Rules:

- Prefer **region-level** framing over point-level framing.
- If a place is sensitive, use:
  - county-scale, watershed-scale, or “general area” descriptions, or
  - non-spatial narratives (“within Kansas,” “in the Central Plains,” etc.).
- Avoid “triangulation risk”:
  - Even without coordinates, unique feature descriptions + dates + photos can reveal locations.
- Do not attribute cultural affiliation beyond what is documented and approved for public release.
- When referencing datasets or archives:
  - Link to the governed reference (STAC/DCAT record, published catalog entry, or approved citation),
  - do not paste raw restricted excerpts.

---

## 📜 Workflow Integration

### 🧩 Draft → Review → Story Node

1. Capture candidate ideas in `backlog.md`.
2. Record governance questions and CARE/sensitivity concerns in `ethics-checklist.md`.
3. After review, convert the draft into a canonical Story Node artifact in the appropriate archaeology Story Node location (outside `notes/`).
4. Ensure the promoted Story Node includes:
   - clear facts vs interpretation,
   - documented source references,
   - explicit spatial and temporal scope,
   - governance notes when needed.

### 🔗 Telemetry & Provenance Expectations

Major lifecycle transitions SHOULD be logged as governed telemetry events (without sensitive content), for example:

- Draft created,
- Sent for review,
- Approved,
- Published,
- Redacted/withdrawn (if required later).

Telemetry MUST reference:

- `doc_uuid` for traceability,
- the relevant governance record reference (e.g., meeting minute pointer or policy ID),
- and the applicable CARE label (without embedding restricted details).

---

## ✅ Promotion Checklist (Notes → Story Node)

Before moving any content out of `notes/` into a canonical Story Node:

- [ ] **Public-safe check**: no coordinates, no restricted site codes, no sensitive photos, no location triangulation risk.
- [ ] **CARE label set** and consistent with the governance outcome.
- [ ] **Sovereignty review completed** when Indigenous-linked or culturally sensitive.
- [ ] **Sources recorded**: citations or catalog references (STAC/DCAT/PROV, archive references, or approved public sources).
- [ ] **Spatial scope declared**:
  - generalized geometry or non-spatial,
  - plus explicit note if geometry was withheld.
- [ ] **Temporal scope declared** (date range or period).
- [ ] **Graph linking plan**:
  - stable identifiers for any Places/Periods/Events referenced (no ad-hoc strings).
- [ ] **Story Node structure** separates:
  - facts (supported),
  - interpretation (clearly labeled),
  - speculation (avoid; if present, clearly labeled and justified).
- [ ] **Telemetry event emitted** for the promotion step (metadata only; no restricted content).
- [ ] **CI passes** for markdown + links + required front matter in the destination Story Node file.

---

## 🧰 Validation & Quality Gates

While drafts here are not required to be schema-valid Story Nodes, merges affecting this directory MUST still pass:

- Markdown lint (structure, headings, link format, safe fences).
- Front matter integrity (required keys present; paths correct).
- Link sanity to governance/standards references.
- Content safety review (no restricted archaeology content, no sensitive locations).
- Accessibility basics (headings, readable structure).

If a note cannot pass these gates safely, it should not be merged.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.6 | 2025-12-11 | Upgraded to KFM-MDP v11.2.6; added pipeline role, promotion checklist, redaction rules, and CI quality gates. |
| v11.2.2 | 2025-11-30 | Initial governed notes directory; aligned with archaeology domain and sovereignty guidance.                  |
| v11.2.1 | 2025-11-29 | Added backlog + ethics checklist structure.                                                                  |

---

<div align="center">

🏺 **KFM v11.2.6 — Archaeology Story Node Notes**  
Drafts · Sovereignty Reviews · FAIR+CARE-Aligned

[📚 Docs Home](../../../../README.md) ·  
[📂 Story Nodes Root](../../README.md) ·  
[🧭 Standards Index](../../../../standards/README.md) ·  
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·  
[📡 Telemetry Index](../../../../telemetry/README.md)

</div>
