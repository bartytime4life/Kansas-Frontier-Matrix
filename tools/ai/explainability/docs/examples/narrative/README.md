---
title: "🧾 Kansas Frontier Matrix — Explainability Examples: Narrative Bundle (Policy-Safe)"
path: "tools/ai/explainability/docs/examples/narrative/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability:examples:narrative-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-examples-narrative"
event_source_id: "ledger:tools/ai/explainability/docs/examples/narrative/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

# Optional (point these to real schema files once present in-repo).
json_schema_ref: "../../../../../../schemas/json/tools-ai-explainability-narrative-bundle-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/tools-ai-explainability-narrative-bundle-v11.shape.ttl"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"

sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

ai_training_allowed: false
ai_training_guidance: "Narrative explainability examples, evidence bundles, and governance artifacts MUST NOT be used as AI training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
  - "tools/ai/explainability/docs/examples/example-narrative.md@v11.2.6"
---

<div align="center">

# 🧾 **KFM — Narrative Explainability Example Bundle (Policy-Safe)**
`tools/ai/explainability/docs/examples/narrative/README.md`

**Purpose**  
Define the **example bundle format** for narrative explainability in KFM (Focus Mode / Story Nodes):  
a **reference-first, policy-safe** set of files that explains *how a narrative output was grounded* **without** exposing raw prompts, raw retrieved passages, or restricted content.

</div>

---

## 📘 Overview

### What “narrative explainability” means in KFM

For narrative systems (Focus Mode summaries, Story Nodes, guided narratives), “explainability” is primarily:

- **Evidence selection transparency** (what sources were used / withheld, by ID)
- **Claim coverage** (which claims have supporting evidence references)
- **Governance gating** (what was redacted/suppressed and why)
- **Provenance binding** (model + dataset + config identity, checksums)

This folder documents a **toy bundle** pattern that demonstrates these concepts using **synthetic IDs and toy values only**.

### What these narrative examples are for

This folder exists to:

- provide a stable reference for bundle shape and file naming,
- support schema/validator development,
- support CI testing (shape + safety + determinism),
- guide UI integration (what an “AI explanation” panel can safely show),
- avoid “explainability as leakage” by design.

### What these narrative examples MUST NOT contain

Narrative explainability examples MUST NOT include:

- raw prompts
- raw retrieved passages
- direct quotes from restricted corpora
- PII
- secrets/tokens/credentials
- precise protected-site coordinates or high-risk spatial identifiers
- any “small cohort” breakdown that could enable re-identification

**Rule:** explanations are allowed to be useful, but never allowed to become a backdoor.

---

## 🗂️ Directory Layout

### Location in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 narrative/
                    └── 📄 README.md                 # This file
~~~

### Recommended narrative example bundle (create files as needed)

> Keep this folder aligned with what actually exists. Add/remove files as example content is added.

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 narrative/
                    ├── 📄 README.md                 # This file (bundle contract + safety rules)
                    │
                    ├── 🧾 example_manifest.json     # Inventory + identity + safety flags (synthetic)
                    ├── 🧾 evidence_bundle.json      # Evidence list (IDs + safe metadata + bounded scores)
                    ├── 🧾 claim_evidence_map.json   # Claim IDs → evidence IDs (no raw claim text required)
                    ├── 🧾 governance_flags.json     # Display eligibility + redaction/suppression reason codes
                    │
                    ├── 🧾 checksums.sha256          # Optional integrity file (sha256sum-compatible)
                    └── 📄 notes.md                  # Optional: what this example demonstrates (synthetic)
~~~

### Storage rule (normative)

- `docs/examples/**` = **synthetic examples** only (CI-friendly, public-safe).
- Real narrative explainability outputs (generated from real corpora) belong under governed run locations, e.g.:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 evidence_bundle.json
        ├── 🧾 claim_evidence_map.json
        ├── 🧾 governance_flags.json
        ├── 🧾 explainability_manifest.json
        ├── 🧾 telemetry.json
        ├── 🧾 provenance_bundle.jsonld
        └── 🧾 checksums.sha256
~~~

---

## 🧭 Context

### How Focus Mode uses this bundle

A narrative explainability bundle supports Focus Mode UX features such as:

- “AI explanation” toggle/panel
- evidence list view (sources used / withheld)
- claim coverage summary (how grounded the narrative is)
- governance banner (redaction/suppression applied; reason codes)

The UI SHOULD render only what is explicitly marked displayable by governance flags.

### Evidence-first is the default

When explaining narrative output, KFM prioritizes:

- **IDs** over content
- **safe metadata** over raw text
- **bounded scores** over uncalibrated probabilities
- **reason codes** over vague “policy said no” statements

### Why claim text is usually omitted

Storing raw claim text can leak restricted details (especially in sensitive domains).  
Instead, the claim-evidence map SHOULD store:

- `claim_id`
- `claim_kind`
- optional: `claim_hash` (hash of internal claim text for audit linkage)
- whether claim text is included (usually `false`)

---

## 🗺️ Diagrams

### Narrative explainability bundle flow (conceptual)

~~~mermaid
flowchart TD
  A["Focus target<br/>(entity_id | dataset_id | story_node_id)"] --> B["Retrieve candidates<br/>(IDs only)"]
  B --> C["Rank/Select evidence<br/>(bounded scores)"]
  C --> D["Compose narrative output<br/>(governed)"]
  D --> E["Build explainability bundle<br/>(evidence + claim map)"]
  E --> F["Safety gates<br/>(no raw passages; suppression/redaction)"]
  F --> G["Validate + checksum<br/>(schema + integrity)"]
  G --> H["Store + register refs<br/>(run_id + provenance)"]
  H --> I["UI renders bundle<br/>(only if displayable)"]
~~~

Accessibility note: this flow creates a separate, safety-gated bundle after narrative composition; it is stored with provenance references and rendered only when governance allows.

---

## 🧠 Story Node & Focus Mode Integration

### Minimal UI-friendly fields (recommended)

The bundle should support rendering these without extra fetches:

- `bundle_metrics.items_total`
- `bundle_metrics.items_displayable`
- `bundle_metrics.items_withheld`
- `bundle_metrics.withheld_reason_codes[]`
- `coverage.claims_total`
- `coverage.claims_grounded`
- `coverage.coverage_ratio`
- `display_eligibility.ui_allowed`
- `policy.reason_codes[]`

### What the UI MUST NOT do

- The UI MUST NOT attempt to fetch raw passages from evidence IDs directly.
- The UI MUST NOT bypass `display_eligibility` gating.
- The UI MUST NOT reveal protected coordinates or sensitive geometry through “explanations.”

---

## 🧪 Validation & CI/CD

### Determinism rules (normative for examples and runs)

- Arrays MUST be in stable order (e.g., sorted by `score` desc then `source_id`).
- Scores MUST be bounded and consistently rounded (document rounding if applied).
- If timestamps exist, they should not invalidate determinism expectations for bundle shape.
- Paths inside manifests/checksums MUST be relative and stable.

### Safety rules (normative)

Validation MUST ensure:

- no raw text passages
- no raw prompts
- no PII
- no secrets
- no protected-site coordinates
- suppressed cohorts are not emitted (or are explicitly withheld)

### “Fail closed” display guidance

If the bundle is missing or ambiguous about:

- classification/sensitivity,
- redaction/suppression flags,
- display eligibility,

then it MUST be treated as **non-displayable** in governed contexts.

---

## 📦 Data & Metadata

This section provides **illustrative, synthetic** JSON shapes for the narrative example bundle.

### 1) `example_manifest.json` (illustrative)

~~~json
{
  "example_id": "explainability_example_narrative_v1",
  "example_version": "11.2.6",
  "example_kind": "narrative",
  "created": "2025-12-15T00:00:00Z",

  "model": {
    "model_id": "demo_focus_mode_v3_narrative",
    "model_version": "demo",
    "model_hash": "<sha256>"
  },

  "dataset": {
    "dataset_id": "dcat:kfm:dataset:demo-corpus",
    "dataset_version": "demo"
  },

  "focus": {
    "target_kind": "story_node",
    "target_id": "urn:kfm:story-node:demo:0001"
  },

  "config": {
    "explainer_profile_ref": "tools/ai/configs/domains/narrative/explainability.json",
    "config_sha256": "<sha256>"
  },

  "artifacts": [
    { "path": "evidence_bundle.json", "media_type": "application/json", "sha256": "<sha256>" },
    { "path": "claim_evidence_map.json", "media_type": "application/json", "sha256": "<sha256>" },
    { "path": "governance_flags.json", "media_type": "application/json", "sha256": "<sha256>" },
    { "path": "checksums.sha256", "media_type": "text/plain", "sha256": "<sha256>" }
  ],

  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "contains_pii": false,
    "contains_secrets": false,
    "contains_sensitive_locations": false,
    "contains_raw_text_passages": false,
    "small_group_suppression_applied": true
  },

  "notes": "Synthetic-only example demonstrating evidence IDs + claim mapping without raw narrative text."
}
~~~

### 2) `evidence_bundle.json` (illustrative)

~~~json
{
  "bundle_id": "demo_evidence_bundle_v1",
  "schema_version": "11.2.6",
  "created": "2025-12-15T00:00:00Z",

  "scope": {
    "model_id": "demo_focus_mode_v3_narrative",
    "model_version": "demo",
    "dataset_id": "dcat:kfm:dataset:demo-corpus",
    "dataset_version": "demo",
    "target_id": "urn:kfm:story-node:demo:0001"
  },

  "selection": {
    "strategy_id": "retrieval_top_k",
    "k": 5,
    "score_semantics": "bounded_0_to_1"
  },

  "evidence_items": [
    { "source_id": "dcat:kfm:source:demo:001", "source_type": "docs", "time_bucket": "1900s_demo", "region_bucket": "kansas_region_demo", "score": 0.83, "displayable": true },
    { "source_id": "dcat:kfm:source:demo:002", "source_type": "dataset", "time_bucket": "modern_demo", "region_bucket": "kansas_region_demo", "score": 0.71, "displayable": true },
    { "source_id": "graph:kfm:entity:demo:place:0007", "source_type": "graph", "time_bucket": "unknown_demo", "region_bucket": "kansas_region_demo", "score": 0.52, "displayable": true },
    { "source_id": "stac:kfm:item:demo-tile-0001", "source_type": "stac", "time_bucket": "modern_demo", "region_bucket": "kansas_region_demo", "score": 0.41, "displayable": true },
    { "source_id": "dcat:kfm:source:demo:restricted:999", "source_type": "docs", "time_bucket": "unknown_demo", "region_bucket": "restricted", "score": 0.39, "displayable": false }
  ],

  "bundle_metrics": {
    "items_total": 5,
    "items_displayable": 4,
    "items_withheld": 1,
    "withheld_reason_codes": ["SOVEREIGNTY_POLICY_RESTRICTED_SOURCE"]
  }
}
~~~

### 3) `claim_evidence_map.json` (illustrative, no raw narrative)

~~~json
{
  "map_id": "demo_claim_evidence_map_v1",
  "schema_version": "11.2.6",
  "created": "2025-12-15T00:00:00Z",

  "claims": [
    { "claim_id": "claim_001", "claim_kind": "timeline_summary", "claim_text_included": false },
    { "claim_id": "claim_002", "claim_kind": "environmental_context", "claim_text_included": false },
    { "claim_id": "claim_003", "claim_kind": "place_context", "claim_text_included": false }
  ],

  "links": [
    { "claim_id": "claim_001", "evidence_source_ids": ["dcat:kfm:source:demo:001", "graph:kfm:entity:demo:place:0007"], "support_strength": "medium" },
    { "claim_id": "claim_002", "evidence_source_ids": ["dcat:kfm:source:demo:002", "stac:kfm:item:demo-tile-0001"], "support_strength": "high" },
    { "claim_id": "claim_003", "evidence_source_ids": ["dcat:kfm:source:demo:restricted:999"], "support_strength": "unknown" }
  ],

  "coverage": {
    "claims_total": 3,
    "claims_grounded": 3,
    "coverage_ratio": 1.0,
    "claims_with_withheld_only_evidence": 1
  }
}
~~~

### 4) `governance_flags.json` (illustrative)

~~~json
{
  "display_eligibility": {
    "ui_allowed": true,
    "withheld_components": ["evidence_item:dcat:kfm:source:demo:restricted:999"],
    "reasons_if_denied": []
  },
  "safety_controls": {
    "no_raw_text": true,
    "no_precise_coordinates": true,
    "suppress_small_groups": true,
    "min_group_n": 50
  },
  "policy": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_applied": true,
    "suppression_applied": true,
    "reason_codes": [
      "SOVEREIGNTY_POLICY_RESTRICTED_SOURCE",
      "SMALL_GROUP_SUPPRESSION_ENABLED"
    ]
  }
}
~~~

### 5) `checksums.sha256` (optional; sha256sum-compatible)

~~~text
<sha256>  claim_evidence_map.json
<sha256>  evidence_bundle.json
<sha256>  example_manifest.json
<sha256>  governance_flags.json
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

- Documents/datasets referenced as evidence SHOULD use stable DCAT-like IDs (`dcat:kfm:...`).
- The narrative explainability bundle can be treated as an audit distribution (policy-safe) referenced from model cards or run records.

### STAC

- Spatial evidence sources SHOULD be referenced by STAC Item IDs (`stac:kfm:item:...`) and asset keys (if needed).
- Do not embed STAC items or raster contents; store IDs only.

### PROV-O

Narrative explainability can be represented as provenance:

- `prov:Activity`: explainability computation
- `prov:Entity`: evidence bundle, claim map, governance flags
- `prov:used`: model entity, dataset slice entity, config entity
- `prov:wasAssociatedWith`: CI runner / governed agent role

Keep provenance reference-first.

---

## 🧱 Architecture

### Bundle contract (normative)

A narrative explainability bundle MUST:

- clearly separate:
  - evidence listing (IDs + safe metadata),
  - claim-evidence linking (IDs),
  - governance gating (flags + reason codes),
- record:
  - model identity,
  - dataset identity,
  - config reference and hash,
- allow:
  - integrity verification (optional but recommended),
  - deterministic re-validation.

### Adding a new narrative example (recommended)

1. Create/update `example_manifest.json`.
2. Create/update `evidence_bundle.json` (IDs + safe metadata only).
3. Create/update `claim_evidence_map.json` (no raw claim text required).
4. Create/update `governance_flags.json`.
5. Optionally generate `checksums.sha256`.
6. Update this README directory tree and Version History.

---

## ⚖ FAIR+CARE & Governance

### High-risk failure mode: “explanations leak more than outputs”

Narrative explainability can leak restricted content by:

- including raw retrieved passages,
- quoting restricted archives,
- exposing protected locations through fine-grained spatial metadata,
- exposing rare cohorts through subgroup breakdowns.

Therefore, this bundle pattern requires:

- **IDs only** for evidence (no passages),
- **bounded scores** and coarse metadata buckets,
- **small-group suppression** flags and reason codes,
- explicit **display eligibility** for UI.

### Training prohibition

Narrative explainability bundles and examples are governance-relevant artifacts and MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created narrative example bundle README: defined required files (manifest, evidence, claim map, governance flags, checksums), safe-by-default constraints (no raw passages/prompts), determinism/CI validation expectations, and UI display eligibility rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧾 Narrative Example Bundle · Synthetic · Governed for Integrity

[⬅️ Examples Index](../README.md) ·
[⬅️ Explainability Docs](../../README.md) ·
[⬅️ Explainability](../../../README.md) ·
[🛡 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

