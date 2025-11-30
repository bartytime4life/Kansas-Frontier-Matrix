---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Ethics & Sovereignty Checklist"
path: "docs/story-nodes/domains/archaeology/notes/ethics-checklist.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · FAIR+CARE Council · Indigenous Data Governance Board"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:ethicschecklist:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-ethicschecklist"
event_source_id: "ledger:storynodes/archaeology/ethicschecklist"
immutability_status: "version-pinned"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Ethics Checklist"
intent: "kfm-archaeology-ethics-checklist"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R3"
care_label: "High Sensitivity · Indigenous-Linked"
classification: "Internal-Review"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 sovereignty rules"
---

<div align="center">

# 🏺 **Archaeology Story Node — Ethics & Sovereignty Checklist (KFM v11)**  
### *CARE Principles · Indigenous Data Sovereignty · Masking Rules · Ethical Review*  

`docs/story-nodes/domains/archaeology/notes/ethics-checklist.md`

**Purpose**  
Provide a governed checklist for evaluating archaeological Story Nodes,  
ensuring compliance with **FAIR+CARE**, **Indigenous sovereignty**,  
and the KFM v11 ethical data framework.

</div>

---

## 🧭 How to Use This Checklist

Use this checklist **before** submitting any archaeology Story Node  
(Markdown or JSON) for review.  
All items must pass or be explicitly addressed.

Failure to meet mandatory items will block merge in CI/CD.

---

# ✅ **Ethics & Sovereignty Checklist (KFM v11)**

## 🔐 1. Sensitive Location Safety

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the geometry generalized (H3, county, watershed, region)? |  |  |
| Could the geometry be reverse-engineered to reveal a sensitive location? |  |  |
| Are burial/sacred areas excluded or masked beyond recognition? |  |  |
| Does the narrative avoid describing sensitive access routes? |  |  |

---

## ⚖ 2. Indigenous Data Sovereignty

| Question | Yes/No | Notes |
|----------|--------|-------|
| Does this Story Node require tribal consultation? |  |  |
| Has any tribal consultation occurred? |  |  |
| Does any narrative involve cultural knowledge requiring permission? |  |  |
| Is any restricted tribal knowledge omitted? |  |  |
| Have CARE principles been followed? |  |  |

---

## 🧱 3. Observation vs Interpretation

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are observations clearly separated from interpretations? |  |  |
| Are interpretations evidence-based and documented? |  |  |
| Are uncertainties clearly stated? |  |  |
| Does the narrative avoid speculation? |  |  |

---

## 📦 4. Data Sources & Provenance

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all cited sources public or cleared for release? |  |  |
| Are restricted excavation forms excluded? |  |  |
| Are archival materials used according to rights/licensing? |  |  |
| Are STAC/DCAT assets properly linked and licensed? |  |  |

---

## 🌐 5. Geometry & Temporal Structure

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the geometry valid GeoJSON and generalized? |  |  |
| Does `precision` match the actual dating method? |  |  |
| Is a correct `original_label` provided (if applicable)? |  |  |
| Are multi-phase occupations modeled correctly (separate nodes)? |  |  |

---

## 🔗 6. Graph Relations (CIDOC/GeoSPARQL)

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are relations chosen from approved patterns (`relation-patterns.md`)? |  |  |
| Is there exactly one `about` relationship? |  |  |
| Are all linked nodes public-safe? |  |  |
| Are reinterpretations modeled via `counterpoint` where appropriate? |  |  |

---

## 🖼 7. Media & Asset Safety

| Question | Yes/No | Notes |
|----------|--------|-------|
| Are all media generalized and non-sensitive? |  |  |
| Do any images reveal precise site features? |  |  |
| Are rasters (geophysics/lidar) masked correctly? |  |  |
| Are licensing and rights stated for each asset? |  |  |

---

## 🌱 8. Environmental & Cultural Context

| Question | Yes/No | Notes |
|----------|--------|-------|
| Is the environmental context generalized? |  |  |
| Do descriptions avoid revealing precise landowner details? |  |  |
| Does the narrative avoid unsupported cultural attributions? |  |  |
| Are regional terms used instead of specific site identifiers? |  |  |

---

## 🧪 9. CI/CD Readiness

| Question | Yes/No | Notes |
|----------|--------|-------|
| Does the node validate against `story-node.schema.json`? |  |  |
| Does it meet Markdown rules (if MD format)? |  |  |
| Does it pass sovereignty/CARE linting in CI? |  |  |
| Are STAC/DCAT/JSON-LD links valid? |  |  |

---

## 🕊 10. Reviewer Sign-off

| Reviewer Type | Name/Org | Approved? | Notes |
|---------------|-----------|-----------|-------|
| Archaeology Domain Reviewer |  |  |  |
| Indigenous Data Reviewer |  |  |  |
| FAIR+CARE Council |  |  |  |
| Governance Board (if required) |  |  |  |

---

## 🕰️ Version History

| Version | Date       | Summary                                                            |
|--------:|------------|--------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed sovereignty & ethics checklist for archaeology.    |
| v11.2.1 | 2025-11-29 | Added reviewer table, masking prompts, and CI readiness fields.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

