---
title: "🧪 KFM — Explainability Example: Narrative Evidence Bundle (Synthetic)"
path: "tools/ai/explainability/docs/examples/example-narrative.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-example-narrative:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-example-narrative"
event_source_id: "ledger:tools/ai/explainability/docs/examples/example-narrative.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../../schemas/json/tools-ai-explainability-example-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/tools-ai-explainability-example-v11.shape.ttl"

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
ai_training_guidance: "Explainability examples and governance artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🧪 **KFM Explainability Example — Narrative Evidence Bundle (Synthetic)**
`tools/ai/explainability/docs/examples/example-narrative.md`

**Purpose**  
Demonstrate a **policy-safe narrative explainability bundle** for Focus Mode / Story Nodes—showing how KFM records:
evidence selection, claim-to-evidence mapping, safety gating, and provenance references—using **synthetic IDs and toy values only**.

</div>

---

## 📘 Overview

This document is a **toy example** of narrative explainability for generative or narrative-composition systems (Focus Mode / Story Nodes). It demonstrates how to represent:

- **What evidence was used** (by stable IDs and references)
- **How evidence was selected/weighted** (bounded, policy-safe scores)
- **How claims were grounded** (claim IDs mapped to evidence IDs)
- **What governance filters applied** (redaction/suppression reason codes)
- **How to bind artifacts to provenance** (model/dataset/config hashes + run refs)

### What this example demonstrates

- A minimal **example manifest** (identity, safety flags, artifact inventory)
- A minimal **evidence bundle** (source IDs, safe metadata, scores)
- A minimal **claim-evidence map** (no raw narrative text required)
- A minimal **governance flags** record (display eligibility, reason codes)
- Reference-first links to:
  - telemetry
  - provenance bundle
  - baseline/window identity (where relevant)

### What this example intentionally avoids

- Any real archival text excerpts
- Any PII
- Any secrets/tokens/credentials
- Any protected-site coordinates or fine-grained geometry
- Any “debug dumps” of raw prompts, raw retrieved passages, or raw model outputs

**Hard rule:** narrative explainability MUST NOT become a leakage path. Prefer IDs + aggregates + reason codes.

---

## 🗂️ Directory Layout

This file lives in the explainability examples folder:

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                ├── 📄 README.md
                ├── 📄 example-tabular.md
                ├── 📄 example-remote-sensing.md
                └── 📄 example-narrative.md              # This file
~~~

Recommended pairing for a self-contained narrative example bundle (create if/when needed):

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 narrative/
                    ├── 🧾 example_manifest.json         # Artifact inventory + safety flags (synthetic)
                    ├── 🧾 evidence_bundle.json          # Evidence sources (IDs + safe metadata only)
                    ├── 🧾 claim_evidence_map.json        # Claim IDs → evidence IDs (no raw text required)
                    ├── 🧾 governance_flags.json          # Display eligibility + reason codes
                    ├── 🧾 checksums.sha256               # Integrity placeholders (optional)
                    └── 📄 notes.md                       # What the example demonstrates (synthetic)
~~~

**Normative rule:** examples in `docs/examples/` MUST remain small and synthetic; real run artifacts belong under governed run folders (e.g., `mcp/experiments/<run-id>/...`).

---

## 🧭 Context

### When narrative explainability is used in KFM

Narrative explainability applies whenever KFM produces:

- Focus Mode summaries
- Story Node narrative text
- “Explain this output” panels in UI
- Evidence-first narratives grounded in graph + catalogs

Typical drift/explainability triggers (examples):

- source mix changes (new documents ingested, index rebuild)
- embedding refresh
- model version bump
- prompt/template change
- governance policy change (redaction/suppression behavior)

### What “evidence-first” means in KFM

Evidence-first narrative explainability prioritizes:

- **which sources** were considered/used (IDs, not passages),
- **why** they were used (scores/ranks, bounded),
- **how** they supported claims (claim-evidence mapping),
- **what was suppressed** (reason codes and counts).

**Non-goal:** dumping the retrieved passages or prompt context in public artifacts.

### Safe identifiers over raw content

To keep explainability auditable without leakage:

- use **stable source IDs** (DCAT/STAC/graph/doc identifiers),
- include **safe metadata** (domain tag, time bucket, source type),
- include **bounded weights** (0..1),
- reference provenance and telemetry by path/ID.

---

## 🗺️ Diagrams

### Narrative explainability lifecycle (conceptual)

~~~mermaid
flowchart TD
  A["Focus target<br/>(entity_id | dataset_id | story_node_id)"] --> B["Retrieve candidates<br/>(IDs only)"]
  B --> C["Rank/Select evidence<br/>(bounded scores)"]
  C --> D["Compose narrative output<br/>(governed)"]
  D --> E["Build explainability bundle<br/>(evidence + claim map)"]
  E --> F["Apply safety gates<br/>(no raw passages; suppression/redaction)"]
  F --> G["Validate<br/>(schema + integrity + policy scans)"]
  G --> H["Store under run_id<br/>(mcp/experiments/<run-id>/...)"]
  H --> I["Register refs<br/>(registry + provenance pointers)"]
  I --> J["Render in UI (if allowed)<br/>(AI explanation toggle)"]
~~~

Accessibility note: narrative explainability is built as a separate bundle after narrative composition, then safety-gated and stored with provenance references.

---

## 🧠 Story Node & Focus Mode Integration

### What Focus Mode should be able to show

A safe “AI explanation” panel can show:

- evidence list (IDs + safe metadata)
- evidence weighting summary (scores, ranks)
- claim coverage summary (how many claims have at least one evidence link)
- governance flags (redaction/suppression counts and reason codes)
- model/dataset version stamps

### Recommended fields for Focus Mode explanation rendering

- `evidence_items[]` with:
  - `source_id` (stable ID)
  - `source_type` (docs/dataset/graph/stac)
  - `time_bucket` (coarse)
  - `region_bucket` (coarse, non-sensitive)
  - `score` (0..1)
- `claim_coverage`:
  - `claims_total`
  - `claims_grounded`
  - `coverage_ratio`
- `governance`:
  - `display_eligibility`
  - `redaction_applied`
  - `suppression_applied`
  - `reason_codes[]`

### Hard constraint: do not surface raw restricted text

Even if internal systems use retrieved text, the explainability bundle intended for broad visibility must remain:

- aggregate-only
- reference-first
- policy-safe

---

## 🧪 Validation & CI/CD

### Example validation checklist (recommended)

For this example (and for real runs), validation SHOULD include:

- JSON validity for all `🧾` artifacts
- schema validation (when schema exists)
- determinism checks:
  - stable ordering of `evidence_items`
  - stable rounding/precision rules for scores
- safety checks:
  - no secrets
  - no PII
  - no protected-site coordinates
  - no raw passages or prompts
- reference completeness:
  - model identity present
  - dataset identity present
  - config ref + hash present
  - run/provenance pointers present (or intentionally omitted for docs-only)

### Fail-closed guidance (normative for governed runs)

If any of the following are missing/ambiguous:

- classification/sensitivity metadata
- governance flags (display eligibility)
- model/dataset identity
- config reference + hash

…then the explainability bundle MUST be treated as **non-displayable**, and certification-dependent flows should fail closed.

---

## 📦 Data & Metadata

This section shows **illustrative** JSON shapes. Replace placeholder IDs/hashes with real governed values in real runs.

### Example 1: `example_manifest.json` (illustrative)

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
    { "path": "governance_flags.json", "media_type": "application/json", "sha256": "<sha256>" }
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

  "refs": {
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  },

  "notes": "Synthetic-only example showing evidence and claim mapping without raw text."
}
~~~

### Example 2: `evidence_bundle.json` (illustrative, policy-safe)

This bundle lists evidence sources by ID and safe metadata only.

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
    "ranking_notes": "Synthetic example. Scores are bounded [0,1] and not calibrated."
  },

  "evidence_items": [
    {
      "source_id": "dcat:kfm:source:demo:001",
      "source_type": "docs",
      "time_bucket": "1900s_demo",
      "region_bucket": "kansas_region_demo",
      "score": 0.83,
      "displayable": true
    },
    {
      "source_id": "dcat:kfm:source:demo:002",
      "source_type": "dataset",
      "time_bucket": "modern_demo",
      "region_bucket": "kansas_region_demo",
      "score": 0.71,
      "displayable": true
    },
    {
      "source_id": "graph:kfm:entity:demo:place:0007",
      "source_type": "graph",
      "time_bucket": "unknown_demo",
      "region_bucket": "kansas_region_demo",
      "score": 0.52,
      "displayable": true
    },
    {
      "source_id": "stac:kfm:item:demo-tile-0001",
      "source_type": "stac",
      "time_bucket": "modern_demo",
      "region_bucket": "kansas_region_demo",
      "score": 0.41,
      "displayable": true
    },
    {
      "source_id": "dcat:kfm:source:demo:restricted:999",
      "source_type": "docs",
      "time_bucket": "unknown_demo",
      "region_bucket": "restricted",
      "score": 0.39,
      "displayable": false
    }
  ],

  "bundle_metrics": {
    "items_total": 5,
    "items_displayable": 4,
    "items_withheld": 1,
    "withheld_reason_codes": ["SOVEREIGNTY_POLICY_RESTRICTED_SOURCE"]
  }
}
~~~

### Example 3: `claim_evidence_map.json` (illustrative, no raw narrative)

This map links **claim IDs** to evidence IDs and reason codes—without storing raw claim text.

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
    {
      "claim_id": "claim_001",
      "evidence_source_ids": ["dcat:kfm:source:demo:001", "graph:kfm:entity:demo:place:0007"],
      "support_strength": "medium",
      "notes": "Synthetic mapping; support strength is a bounded category, not a probability."
    },
    {
      "claim_id": "claim_002",
      "evidence_source_ids": ["dcat:kfm:source:demo:002", "stac:kfm:item:demo-tile-0001"],
      "support_strength": "high",
      "notes": "Synthetic mapping."
    },
    {
      "claim_id": "claim_003",
      "evidence_source_ids": ["dcat:kfm:source:demo:restricted:999"],
      "support_strength": "unknown",
      "notes": "Evidence withheld from display. Claim may be suppressed in UI depending on policy."
    }
  ],

  "coverage": {
    "claims_total": 3,
    "claims_grounded": 3,
    "coverage_ratio": 1.0,
    "claims_with_withheld_only_evidence": 1
  }
}
~~~

### Example 4: `governance_flags.json` (illustrative)

This file models “computed but not fully displayable” explainability bundles.

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

### Safe human interpretation (no raw text required)

- The example shows that most evidence items are displayable, but one item is withheld by sovereignty policy.
- Claim-to-evidence mapping can be audited without storing raw claim text.
- UI can still show coverage metrics and reason codes even when some evidence is withheld.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment (recommended)

- Evidence sources that are documents/datasets can be referenced using DCAT identifiers.
- The explainability bundle can be treated as a distribution-like audit artifact (policy-safe) linked from model cards or run records.

### STAC alignment (recommended)

- Evidence items that are spatial assets should be referenced by STAC Item IDs and asset keys.
- Do not embed Item JSON or raster content in the explainability bundle; store IDs and references only.

### PROV alignment (recommended)

Explainability computation is lineage:

- `prov:Activity` = “explainability_computation”
- `prov:Entity` = model artifact, dataset slice, evidence bundle, claim map
- `prov:used` = evidence candidate IDs, config entity, model entity
- `prov:generated` = bundle artifacts
- `prov:wasAssociatedWith` = CI runner / governed agent role

Keep PROV bundles small and reference-first.

---

## 🧱 Architecture

### Narrative explainability artifact set (recommended “v1” profiles)

A narrative explainability run SHOULD be able to emit:

- `evidence_bundle.json`
- `claim_evidence_map.json`
- `governance_flags.json`
- optional:
  - `quality_metrics.json` (coverage, withheld counts, confidence tags)
  - `checksums.sha256` (integrity)
  - `provenance_bundle.jsonld` (lineage)

### Extending narrative explainability safely (recommended process)

1. Add new fields only if they remain policy-safe and do not leak raw content.
2. Prefer categorical/bounded values over raw passages or coordinates.
3. Add schema validations and safety gates for any new artifact type.
4. Update UI integration guidance to honor display eligibility and reason codes.

---

## ⚖ FAIR+CARE & Governance

### Why narrative explainability is governance-sensitive

Narrative systems often synthesize across sources. Risks include:

- leaking restricted text or protected locations through “explanations”
- exposing rare subgroup patterns via detailed breakdowns
- overclaiming certainty without evidence density

Therefore, narrative explainability MUST:

- keep explanations **reference-first**
- include governance flags and reason codes
- suppress small cohort outputs
- avoid raw passages/prompts/outputs in public artifacts

### Training prohibition

This example and all narrative explainability artifacts MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Added synthetic narrative explainability example: evidence bundle (IDs + safe metadata), claim-to-evidence map (no raw text), governance display flags with reason codes, and CI validation guidance to prevent leakage paths. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧪 Narrative Explainability Example · Synthetic · Governed for Integrity

[⬅️ Examples Index](./README.md) ·
[⬅️ Explainability Docs](../README.md) ·
[⬅️ Explainability](../../README.md) ·
[🛡 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

