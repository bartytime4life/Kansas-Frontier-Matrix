---
title: "🧠 Model Card — Focus Mode Transformer v3 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "mcp/model_cards/focus_mode_transformer_v3.md"

version: "v11.0.0"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · AI Governance Board · FAIR+CARE Council · Narrative Review Committee"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Model Card"
header_profile: "standard"
footer_profile: "standard"
intent: "focus-mode-transformer-v3"
semantic_document_id: "kfm-modelcard-focus-mode-transformer-v3"
doc_uuid: "urn:kfm:modelcard:focus-mode-transformer-v3:v11.0.0"
event_source_id: "urn:kfm:modelcard:focus-mode-transformer-v3"

machine_extractable: true
classification: "Governed AI Narrative Model"
sensitivity: "Mixed"
fair_category: "F1-A1-I3-R3"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../releases/v11.0.0/signature.sig"
attestation_ref: "../../releases/v11.0.0/slsa-attestation.json"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"

telemetry_ref: "../../releases/v11.0.0/mcp-modelcards-telemetry.json"
telemetry_schema: "../../schemas/telemetry/mcp-modelcards-v11.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "mcp/experiments/2025-11-05_AI-EXP-003.md@v11.0.0"

ai_transform_permissions:
  - "summarize"
  - "extract-metadata"
  - "generate-draft-story-node"
  - "generate-focus-mode-context"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "fabricate-facts"
  - "fabricate-provenance"
  - "invent-citations"
  - "genealogical-inference"
  - "sacred-site-inference"
  - "expose-sensitive-coordinates"
  - "override-governance"
  - "publish-without-human-review"
---

<div align="center">

# 🧠 **Focus Mode Transformer v3 — Model Card (v11 LTS)**
`mcp/model_cards/focus_mode_transformer_v3.md`

**Purpose**  
Document the architecture, training, safety constraints, governance requirements, provenance, and usage
boundaries of the **Focus Mode Transformer v3 (FMT‑v3)** — the governed AI engine powering KFM’s
context-aware narrative reasoning system.

</div>

---

## 📘 Overview

**Focus Mode Transformer v3 (FMT‑v3)** is a multi-domain contextual reasoning model used to:

- generate **fact-grounded narrative summaries**
- power Focus Mode’s **3-panel reasoning** (Context · Timeline · Map)
- produce **explanatory overlays** with provenance
- support Story Node v3 draft creation with data-backed relationships
- interpret spatial/temporal/event clusters from the Neo4j knowledge graph
- enforce Indigenous sovereignty, CARE ethics, and narrative safety

FMT‑v3 is designed **not** to imagine, speculate, or reconstruct unverified claims.

All outputs are bounded by evidence, where each statement must connect to one or more of:
- graph entities
- datasets (STAC/DCAT)
- provenance records (PROV‑O / OpenLineage)
- documents
- MCP experiments

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 mcp/
│   ├── 📁 model_cards/
│   │   └── 📄 focus_mode_transformer_v3.md                 # This model card (FMT‑v3)
│   └── 📁 experiments/
│       ├── 📄 2025-11-05_AI-EXP-003.md                     # Story Node generation trial (governed)
│       └── 📄 YYYY-MM-DD_AI-EXP-###.md                     # Other AI experiments
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 storynode/
│           └── 📄 generate_v3.py                           # FMT‑v3-assisted Story Node pipeline entrypoint
├── 📁 data/
│   └── 📁 provenance/
│       └── 📁 experiments/
│           └── 📁 fmt_v3/
│               └── 📁 <timestamp>/
│                   ├── 🧾 prov.jsonld                      # PROV‑O JSON‑LD
│                   ├── 🧾 openlineage.json                 # OpenLineage event(s)
│                   ├── 🧾 config_snapshot.json             # Run configuration snapshot
│                   └── 🧾 checksums.json                   # Output checksums
└── 📁 releases/
    └── 📁 v11.0.0/
        └── 🧾 mcp-modelcards-telemetry.json                # Energy/carbon/runtime telemetry
~~~

---

## 🧭 Context

### Intended use
Approved uses include:
- Focus Mode v3 entity summaries (evidence-led)
- contextual explanation for map/timeline interactions
- Story Node v3 draft generation (requires human review)
- explainability layers and provenance traces
- temporal evolution descriptions when grounded in data
- spatial relationships using GeoSPARQL constraints and H3-safe geometry

### Out-of-scope use
FMT‑v3 must not be used for:
- creating genealogies
- predicting undocumented tribal history
- inventing causes behind events
- describing sensitive archaeological sites
- creative fiction or emotional persuasion
- producing unverifiable historical claims
- exposing restricted coordinates or sensitive locations

All narrative output is bounded by FAIR+CARE and sovereignty rules, plus human review gates.

---

## 📦 Data & Metadata

### Training data policy
FMT‑v3 is fine-tuned only on vetted, public and low-risk datasets.

No Indigenous-only or sovereignty-restricted datasets are used for training.

For sensitive cultural datasets during inference, FMT‑v3 may only receive masked/generalized inputs or synthetic embeddings, and may be bypassed entirely based on governance rules.

### Datasets used for training (as referenced)
| Dataset | STAC/DCAT ID | Notes |
|--------|---------------|------|
| Kansas Gazetteer | `stac:ref/gnis_kansas` | Public place names |
| Chronological event datasets | `stac:history/events_core` | Non-sensitive |
| Kansas rivers & hydrology metadata | `stac:hydrology/basins_core` | Public |
| Environmental data summaries | `stac:climate/summary_stats` | Non-sensitive |
| Public-domain historical texts | `stac:archives/public_texts` | No sensitive material |
| Story Node v2 corpus | `stac:storynodes/v2_public` | Cleaned and CARE-filtered |

### Input boundaries at runtime
FMT‑v3 input context is expected to be:
- retrieval-constrained (e.g., 2–3 hop neighborhood from Neo4j)
- provenance-attached (dataset/document identifiers included)
- spatially masked where required (H3 generalization)
- temporally normalized (OWL-Time interval alignment)

---

## 🧱 Architecture

FMT‑v3 is a hybrid architecture composed of:

- transformer encoder (context fusion)
- graph-integrated attention layers (retrieval-grounded)
- spatial reasoning module (H3 + GeoSPARQL constraints)
- temporal fusion layers (OWL-Time alignment)
- narrative safety gate (policy-conditioned decoding constraints)
- provenance enforcement module (PEM)
- data-citation tagger (DCT)

Design goals:
- multi-hop reasoning without free-form invention
- spatial + temporal integration with strict constraints
- auto-citation scaffolding and provenance traceability
- sovereignty-aligned masking and safety gating

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode v3 outputs
FMT‑v3 supports the 3-panel output pattern:
- Context panel: entity summary + evidence anchors
- Timeline panel: time-ordered facts bounded by dataset/document time ranges
- Map panel: spatial grounding via safe geometry (H3-masked when required)

### Story Node v3 drafting
FMT‑v3 may generate draft Story Nodes only when:
- evidence links are present for statements
- sovereignty masking rules are applied
- human review is required before publication
- provenance artifacts are emitted (PROV‑O + OpenLineage + checksums)

### Mandatory gating
All outputs flow through:
- narrative safety filter
- CARE/sovereignty gate
- human review step (required for publishing)

---

## 🧪 Validation & CI/CD

### Factuality and grounding (as reported)
| Metric | Score |
|--------|-------|
| Citation Accuracy | 0.98 |
| Grounded Statement Score | 0.96 |
| Hallucination Rate | <0.5% |
| Sovereignty Compliance | 1.00 |

### Narrative metrics (as reported)
- neutrality score: 0.94
- bias avoidance score: 0.97
- sensitive-topic handling: PASS
- temporal consistency: 0.95

### Spatial and temporal reasoning (as reported)
- GeoSPARQL validity: 1.00
- OWL-Time alignment: 0.97
- H3 masking adherence: 1.00

### Explainability (as reported)
- SHAP maps available
- layer attention visualization
- temporal/sentence alignment trace logs

---

## 🌐 STAC, DCAT & PROV Alignment

### Evidence and citation expectations
- FMT‑v3 outputs must carry dataset/document identifiers sufficient to:
  - resolve the source in STAC/DCAT
  - trace lineage via PROV‑O and OpenLineage
  - support user-visible provenance in Focus Mode

### PROV‑O block (simplified)
~~~json
{
  "prov:entity": "focus_mode_transformer_v3",
  "prov:wasGeneratedBy": "training:2025-11-10_AI-EXP-021",
  "prov:used": [
    "stac:ref/gnis_kansas",
    "stac:history/events_core",
    "stac:climate/summary_stats",
    "stac:storynodes/v2_public"
  ],
  "prov:wasAssociatedWith": "kfm-ai-training-service-v11"
}
~~~

### OpenLineage storage (as referenced)
~~~text
data/provenance/experiments/fmt_v3/<timestamp>/
~~~

---

## ⚖ FAIR+CARE & Governance

### FAIR posture (as reported)
- findable: cataloged under DCAT
- accessible: public model card and governance references
- interoperable: JSON-LD, STAC, DCAT, PROV-O
- reusable: CC‑BY with governance constraints

### CARE posture (as reported)
- collective benefit: supports cultural understanding through evidence-led context
- authority to control: prevents exposure of sovereignty-protected content
- responsibility: safety constraints enforced by design
- ethics: strict boundaries for cultural and historical claims

### Sovereignty enforcement (as reported)
- FMT‑v3 never outputs sensitive tribal locations
- uses H3 R7–R9 masking when interacting with cultural geography
- protected datasets may bypass the model entirely

### Limitations (as reported)
- cannot interpret oral histories or sacred traditions
- limited on nuanced tribal governance structures
- cannot perform novel historical inference
- requires human review for complex cultural subjects
- bias may emerge from public-domain corpora (monitored quarterly)

### Deployment boundaries
Authorized for:
- Focus Mode v3
- Story Node v3 drafting (human-reviewed)
- Neo4j narrative enrichment (retrieval-grounded)
- UI highlight panels and explainability overlays
- metadata-assisted map/timeline interpretation

Restricted from:
- autonomous publishing
- sensitive heritage narrative generation
- unreviewed historical claims
- culturally sensitive reconstruction

---

## 🕰️ Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-23 | Initial model card for Focus Mode Transformer v3 (governed, deterministic, CARE-aligned). |
| v11.0.0 | 2025-12-12 | Normalized document to KFM‑MDP v11.2.6 (approved H2 set, required directory layout section, tilde fences, governance links in footer). No model behavior changes. |

---

<div align="center">

🧠 **Focus Mode Transformer v3 — Model Card**  
[🏛️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Sovereignty‑Respecting · Narrative‑Safe · Fully Governed  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
