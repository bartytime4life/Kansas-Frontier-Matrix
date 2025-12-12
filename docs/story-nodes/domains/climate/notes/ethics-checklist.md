---
title: "🌦️ KFM v11.2.6 — Climate Story Node Ethics & Attribution Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/notes/ethics-checklist.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council · AI Attribution Governance Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Ethics Checklist"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:climate:notes:ethicschecklist:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-ethicschecklist-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/climate/notes/ethics-checklist.md"
immutability_status: "version-pinned"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
schema_ref: "../../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

intent: "kfm-climate-ethics-checklist"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental · Attribution-Sensitive"
classification: "Internal-Review"
sensitivity: "Attribution-sensitive climate narratives (must remain evidence-bounded)"
sensitivity_level: "Moderate"
public_exposure_risk: "Low/Moderate"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate ethics checklist"

provenance_chain:
  - "docs/story-nodes/domains/climate/notes/ethics-checklist.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

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
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 How to Use This Checklist"
    - "✅ Ethics & Attribution Checklist"
    - "🧪 CI/CD Readiness"
    - "🕊️ Reviewer Sign-off"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌦️ **Climate Story Node — Ethics & Attribution Checklist (KFM v11.2.6)**  
### *Scientific Integrity · Attribution Safety · Public-Safe Communication · FAIR+CARE*  

`docs/story-nodes/domains/climate/notes/ethics-checklist.md`

**Purpose**  
Provide a governed checklist to ensure climate Story Nodes meet **scientific rigor**, avoid **over-attribution**,  
communicate **uncertainty responsibly**, and remain **public-safe** and **FAIR+CARE-aligned**.

</div>

---

## 📘 Overview

Climate Story Nodes are uniquely vulnerable to:

- **model/observation confusion** (forecasts vs reanalysis vs measured observations)
- **over-precision** (implied exact footprints, track timing, or local impacts beyond data resolution)
- **over-attribution** (turning correlation into causation, or implying certainty without attribution studies)
- **sensational framing** (especially around extremes)
- **environmental justice blindspots** (harmful or careless framing of impacts)

This checklist is **merge-blocking** when used as part of domain governance.

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 📂 🌦️ climate/
            └── 📂 🗒️ notes/
                └── 📄 ethics-checklist.md     # This file
~~~

**Layout rules (normative)**  
- ASCII connectors remain plain for readability.  
- Directories use `📂` plus a semantic emoji on the directory name (`🌦️ climate/`, `🗒️ notes/`).  
- This checklist is **internal-review**: do not paste sensitive drafts into it.

---

## 🧭 How to Use This Checklist

Run this checklist **before** submitting any climate Story Node (Markdown or JSON).

- Items marked as “must” are **required**.  
- If an item is “No”, the PR must include either:
  - a remediation commit, or
  - a documented governance exception (with reference).

---

## ✅ Ethics & Attribution Checklist

### 🌡️ 1. Scientific Accuracy & Rigor

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all factual claims supported by cited sources (datasets, papers, or official agency material)? |  |  |
| Are **observations** clearly separated from **model output** and **derived products**? |  |  |
| Are uncertainty bounds or limitations stated for all key findings (resolution, coverage gaps, known biases)? |  |  |
| Are extreme-event metrics (SPI/SPEI, anomalies, return periods, thresholds) used correctly and described clearly? |  |  |
| Are variable names and units consistent (and conversions explicitly stated where relevant)? |  |  |

---

### 🌀 2. Event Classification & Boundaries

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the event classification (heatwave, drought, tornado outbreak, etc.) consistent with accepted conventions (NWS/NOAA or domain definitions)? |  |  |
| Is the time interval defensible (start/end, precision) and aligned with the evidence? |  |  |
| Are spatial boundaries **public-safe** and appropriate to the dataset’s native resolution (no implied “street-level” accuracy)? |  |  |
| Are radar/satellite footprints described without false precision (avoid implying exact track/extent unless documented)? |  |  |

---

### 🔭 3. Attribution & Interpretation Controls

| Question | Yes/No | Notes |
|----------|--------|-------|
| If climate-change attribution is mentioned, is it supported by an attribution study or an authoritative synthesis (and cited)? |  |  |
| Are confidence levels stated when attribution is discussed (e.g., low/medium/high confidence) rather than implied certainty? |  |  |
| Are alternative explanations or confounders acknowledged where appropriate (synoptic setup, ENSO state, land-surface feedbacks, etc.)? |  |  |
| Does the narrative avoid causal language that exceeds evidence (e.g., “caused by” without attribution evidence)? |  |  |

**Attribution language guardrails (normative)**  
Use careful phrasing such as:
- “consistent with…”
- “may have increased likelihood…”
- “is associated with…”
- “attribution evidence indicates…”

Avoid unqualified phrasing such as:
- “X caused Y”
- “proof that climate change caused this event”
- “definitively due to…”

---

### 🧩 4. Data Sources & Provenance

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all datasets public or approved for release, with stable references (STAC/DCAT where used)? |  |  |
| Are STAC/DCAT references complete where assets/datasets are linked? |  |  |
| Are model run details documented when relevant (init time, cycle, configuration, or product identifier)? |  |  |
| Is PROV-O lineage present or linked (source data → transformations → outputs)? |  |  |

---

### 🌐 5. Geometry & Temporal Modeling

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is geometry valid GeoJSON and appropriate in scale (region/county/watershed/footprint as warranted)? |  |  |
| Is temporal precision correct (hour/day/month/year) and not overstated? |  |  |
| Is `original_label` included where it improves human interpretation (e.g., “June 2022 Heatwave”)? |  |  |
| For multi-day/multi-phase events, are intervals represented explicitly (not collapsed into vague single timestamps)? |  |  |

---

### 🔗 6. Graph Relations

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are relations chosen from approved climate relation patterns (domain rules), not invented ad-hoc? |  |  |
| Is `about` used exactly once? |  |  |
| Are `derived-from` and `references` used correctly (derived products vs sources)? |  |  |
| Are linked nodes public-safe and version-pinned where possible? |  |  |

---

### 🖼️ 7. Media, Visualization & Licensing

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all images/plots properly licensed or sourced (and labeled as derived vs raw)? |  |  |
| Do figures avoid including personal/private details (addresses, people, private property imagery, etc.)? |  |  |
| Are colorbars/legends/units explicit (no ambiguous scales)? |  |  |
| Are visualizations accompanied by a short caveat if they can be misread (e.g., model output vs observations)? |  |  |

---

### 🌍 8. Environmental Justice & Harm-Minimizing Framing

| Question | Yes/No | Notes |
|----------|--------|-------|
| If impacts are discussed, are they described respectfully and without stereotyping? |  |  |
| Does the narrative avoid “blame framing” toward communities or individuals? |  |  |
| Are claims about impacts evidence-backed (not implied from a map alone)? |  |  |
| Does the node avoid politicized language while remaining honest and precise? |  |  |

---

## 🧪 CI/CD Readiness

| Check | Yes/No | Notes |
|------|--------|-------|
| Story Node schema validation passed (`story-node.schema.json`) |  |  |
| Markdown protocol checks passed (if Markdown node) |  |  |
| Provenance completeness check passed |  |  |
| Link checks passed (internal docs + dataset refs) |  |  |
| Any climate-domain ethics lint (if enabled) passed |  |  |

---

## 🕊️ Reviewer Sign-off

| Reviewer Type | Name/Org | Approved? | Notes |
|---------------|----------|-----------|-------|
| Climate Domain Reviewer |  |  |  |
| Attribution Specialist |  |  |  |
| FAIR+CARE Council |  |  |  |
| AI Attribution Governance Board (if needed) |  |  |  |

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; fixed relative links; added attribution-language guardrails; improved directory layout formatting. |
| v11.2.2 | 2025-11-30 | Initial governed climate ethics & attribution checklist.                |
| v11.2.1 | 2025-11-29 | Added attribution safety & environmental justice sections.              |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) ·
[🌦️ Climate Domain](../README.md) ·
[🧪 Climate Examples](../examples/README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
