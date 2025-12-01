---
title: "🎨 Kansas Frontier Matrix — Diff-First Entity Styles Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/diff-first/styles/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous + FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-entity-diff-styles-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entity-diff-styles-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entity-diff-styles"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed (governance-dependent)"
sensitivity_level: "Visual encodings for potentially sensitive entities"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/diff-first/styles/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../../../schemas/json/web-entity-diff-styles-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-entity-diff-styles-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-entity-diff-styles-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entity-diff-styles-readme-v11"
event_source_id: "ledger:web/src/entities/diff-first/styles/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints (no style-level speculation)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public Styles (governance-linked)"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon next Diff-First style-system overhaul"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Diff-First Entity Styles Architecture**  
`web/src/entities/diff-first/styles/README.md`

**Purpose:**  
Define the **Diamond⁹ Ω–grade styling system** for the Diff-First Entity module — including **accessible design tokens**,  
**WCAG 2.1 AA-compliant color ramps**, **CARE-aware visual encodings**, and **sustainability-optimized animations**.  
All styles follow **MCP-DL v6.3**, KFM’s **token-driven UI architecture**, and the **FAIR+CARE visualization doctrine** for diff presentation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Visual_Governance-orange)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The Diff-First styles layer provides:

- WCAG-validated color tokens for **added**, **removed**, **changed**, and **governance-critical** diffs  
- CARE-aware masking tokens for sensitive/redacted content  
- Accessible iconography + shape encoding (no color-only indicators)  
- High-contrast visual modes for low-vision and high-glare environments  
- Reduced-motion variants for users preferring minimal animation  
- Sustainable GPU-efficient animations (short duration, low repaint cost)  
- Reusable CSS variables for all diff components  
- Design token integration across Focus Mode v3, TimelineView, DetailDrawer, and Governance UI  

This ensures **ethical, inclusive, and interpretable change visualization** across KFM.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/diff-first/styles/
│
├── 📘 README.md       # This file
└── 🎨 tokens.css      # Canonical style token source for all diff components
~~~

`tokens.css` is the canonical style authority for all Diff-First components (header, property, relation, text diff, legend, etc.).

---

## 🎨 Design Token Architecture

*(Use ```mermaid``` in-repo; `~~~mermaid` here preserves single-fence safety.)*

~~~mermaid
flowchart TD
    TOK["tokens.css<br/>design variables"] --> DIFF["Diff Components<br/>header · props · relations · text"]
    TOK --> GOV["Governance UI<br/>consent · CARE · license"]
    TOK --> A11Y["Accessibility Layer<br/>contrast · reduced motion"]
    TOK --> TEL["Telemetry Style Hooks<br/>render cost · a11y mode"]
~~~

Tokens are **globally namespaced** under `--kfm-*` to avoid collisions.

---

## 🧬 Core Token Groups (Deep Specification)

### 1️⃣ Diff Severity Tokens

Used by `DiffHeader`, `PropertyDelta`, `RelationDelta`, and `TextDelta`.

**Visual concepts:**

- Additions: calm, green-toned background + `+` symbol  
- Removals: red-toned background + `−` symbol  
- Changes: amber-toned background + dot/badge

**Tokens:**

- `--kfm-diff-add-bg`  
- `--kfm-diff-add-border`  
- `--kfm-diff-remove-bg`  
- `--kfm-diff-remove-border`  
- `--kfm-diff-change-bg`  
- `--kfm-diff-change-border`  

**Icon Tokens** (semantic, not just color):

- `--kfm-diff-add-icon` (e.g., `"+"`)  
- `--kfm-diff-remove-icon` (e.g., `"−"`)  
- `--kfm-diff-change-icon` (e.g., `"•"`)  

WCAG color contrast: **≥ 4.5:1** against backgrounds.

---

### 2️⃣ CARE + Governance Tokens

Used to visually flag ethical or lineage-sensitive changes.

- `--kfm-care-public-color`  
- `--kfm-care-sensitive-color`  
- `--kfm-care-restricted-color`  
- `--kfm-care-restricted-pattern`  
- `--kfm-governance-consent-change-color`  
- `--kfm-governance-license-change-color`  
- `--kfm-governance-sovereignty-outline`  

Governance patterns use **texture encoding** (hatch/stripe/pattern) to ensure meaning is visible for color-blind users.

---

### 3️⃣ Explainability Tokens (Focus Mode v3)

Used to show explainability deltas:

- `--kfm-xai-added-evidence`  
- `--kfm-xai-removed-evidence`  
- `--kfm-xai-relevance-up`  
- `--kfm-xai-relevance-down`  

These support:

- Explainability deltas from Focus Mode  
- Relevance drift warnings  
- Evidence chain expansion cues  

---

### 4️⃣ Text Diff Tokens

Used by `TextDelta`:

- `--kfm-text-insert-bg`  
- `--kfm-text-delete-bg`  
- `--kfm-text-change-outline`  
- `--kfm-text-token-highlight`  

**Rule:** They must produce **outlines and structure**, not pure color fill, to support color-blind readability and SR-friendly segmentation.

---

### 5️⃣ Reduced Motion Tokens

Required for sustainability + A11y:

- `--kfm-motion-scale`  
- `--kfm-motion-disabled`  
- `--kfm-motion-transition`  
- `--kfm-motion-transition-reduced`  

Applied automatically when:

- OS `prefers-reduced-motion` is set, or  
- KFM A11y setting is enabled via A11yContext.

---

### 6️⃣ High-Contrast Mode Tokens

Overrides critical colors for:

- Extreme contrast / grayscale themes  
- Sunlight readability  
- CARE-warning enhancement

Tokens:

- `--kfm-contrast-bg`  
- `--kfm-contrast-text`  
- `--kfm-contrast-border`  
- `--kfm-contrast-pattern`  

---

## 📦 Example: `tokens.css` Extract (Rule-Safe)

*(Truncated example; the real file may contain more tokens.)*

~~~css
:root {
  /* Diff Severity Tokens */
  --kfm-diff-add-bg: #e6f7ea;
  --kfm-diff-add-border: #2e8b57;
  --kfm-diff-remove-bg: #fde8e8;
  --kfm-diff-remove-border: #b22222;
  --kfm-diff-change-bg: #fff7e0;
  --kfm-diff-change-border: #d18f00;

  /* CARE & Governance Tokens */
  --kfm-care-public-color: #4a90e2;
  --kfm-care-sensitive-color: #d47f00;
  --kfm-care-restricted-color: #b22222;
  --kfm-governance-consent-change-color: #8b008b;
  --kfm-governance-license-change-color: #006400;
  --kfm-governance-sovereignty-outline: #6a0dad;

  /* Explainability Tokens */
  --kfm-xai-added-evidence: #0b7b3e;
  --kfm-xai-removed-evidence: #a83232;
  --kfm-xai-relevance-up: #1a8f1a;
  --kfm-xai-relevance-down: #d17a00;

  /* Text Diff Tokens */
  --kfm-text-insert-bg: #e0ffe8;
  --kfm-text-delete-bg: #ffe6e6;
  --kfm-text-change-outline: 2px solid #444;

  /* Motion & Contrast Tokens */
  --kfm-motion-scale: 1;
  --kfm-motion-disabled: 0;
  --kfm-motion-transition: 140ms ease;
  --kfm-motion-transition-reduced: 0ms;

  --kfm-contrast-bg: #000000;
  --kfm-contrast-text: #ffffff;
  --kfm-contrast-border: #ffffff;
}
~~~

---

## ♿ Accessibility Architecture (WCAG 2.1 AA+)

**Requirements:**

- Every diff badge must include **shape + text**, never color-only.  
- Tokens must maintain **≥ 4.5:1 contrast** for all severity & governance states.  
- Reduced-motion tokens must be honored whenever any A11y preference indicates reduced animation.  

Conceptual flow:

~~~mermaid
flowchart TD
    TOK[Design Tokens] --> A11Y[A11y Enforcement Layer]
    A11Y --> UI[Diff Components<br/>Header/Property/Relation/Text]
    UI --> A11YTEL[A11y Telemetry]
~~~

Diff components are responsible for implementing A11y; Diff style tokens ensure they can do so **consistently and correctly**.

---

## 🌱 Sustainability & Telemetry Integration

Styles can affect performance and energy use. The styles layer therefore:

- Must avoid heavy, continuous transitions or animations.  
- Must use **short, efficient animations** where needed (e.g., subtle fade, not complex transforms).  
- Must expose reduced-motion tokens, which disable transitions entirely when requested.  

Telemetry events about style impact are captured by higher-level telemetry, e.g.:

- `style_render_cost_ms`  
- `contrast_mode_enabled`  
- `reduced_motion_applied`  
- `pattern_encoding_used`  

Stored in:

~~~text
../../../../../releases/v11.2.2/web-entity-diff-styles-telemetry.json
~~~

---

## 🔐 Governance Integration (CARE-Aware Styling)

Styling must be aligned with governance semantics:

- CARE flags visually override severity tokens:
  - `restricted` → strong pattern + outline priority  
  - `sensitive` → warm-tone + shape emphasis  
- Sovereignty impacts (tribal boundaries, Indigenous data) must be clearly highlighted with distinct tokens (e.g., purple outlines)  

Conceptual mapping:

~~~mermaid
flowchart TD
    CARE["CARE Label & Governance Metadata"] --> STYLE["Token Resolver"]
    STYLE --> RENDER["Diff Components"]
~~~

Governance audit logs for visual encodings may be generated downstream, e.g.:

~~~text
../../../../../docs/reports/audit/web-entity-diff-style-governance.json
~~~

---

## ⚙️ CI / Validation Requirements

**Validation targets:**

| Area                      | Validator / Job            |
|---------------------------|---------------------------|
| A11y compliance           | `accessibility_scan.yml`  |
| Token contrast rules      | WCAG contrast validator   |
| Governance overlay rules  | `faircare-validate.yml`   |
| Telemetry schema          | `telemetry-export.yml`    |
| Documentation correctness | `docs-lint.yml`           |

No style changes may be merged that:

- Reduce contrast below AA thresholds  
- Break CARE/sovereignty visual semantics  
- Introduce motion that disrespects reduced-motion preferences  

---

## 🧾 Example Style Metadata Record

~~~json
{
  "id": "entity_diff_styles_v11.2.2",
  "contrast_valid": true,
  "patterns_a11y_safe": true,
  "care_overrides_applied": true,
  "energy_use_wh": 0.13,
  "telemetry_synced": true,
  "checksum_verified": true,
  "timestamp": "2025-11-30T23:55:00Z"
}
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                         |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; added telemetry v2, FAIR+CARE v11 semantics, energy/carbon tracking, and refined A11y/contrast rules for all diff tokens. |
| v10.3.2 | 2025-11-14 | Deep-architecture rewrite with design tokens, governance overrides, explainability styles, and sustainability telemetry alignment.              |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Diff-First Style Architecture**  
🎨 Accessible Visualization · 🔐 CARE-Aware Design · 🌱 Sustainable UI  

[Back to Diff-First Entity Module](../README.md) •  
[Docs Root](../../../../README.md) •  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>