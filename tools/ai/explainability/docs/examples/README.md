---
title: "🧪 Kansas Frontier Matrix — Explainability Examples (Policy-Safe)"
path: "tools/ai/explainability/docs/examples/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-examples-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-examples"
event_source_id: "ledger:tools/ai/explainability/docs/examples/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update these refs to your current governed release bundle when available.
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
ai_training_guidance: "Examples and explainability artifacts MUST NOT be used as AI training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/README.md@v11.2.6"
---

<div align="center">

# 🧪 **KFM — Explainability Examples (Policy-Safe)**
`tools/ai/explainability/docs/examples/README.md`

**Purpose**  
Provide **small, synthetic, governance-safe examples** that demonstrate how KFM explainability artifacts are structured, validated, and rendered—without using real or sensitive data.

</div>

---

## 📘 Overview

### What these examples are for

This folder contains **tiny example bundles** that illustrate:

- how to structure explainability artifacts (JSON / JSON-LD / assets)
- how to bind artifacts to model + dataset + config identity
- how to include integrity (checksums) and provenance pointers
- how UI-facing explanation payloads remain safe, minimal, and a11y-friendly

These examples exist to support:

- onboarding (developers, operators, reviewers)
- schema validation development
- CI rule testing (shape, safety, determinism)
- UI integration prototypes (Focus Mode explanation panels)

### What these examples MUST be

All examples MUST be:

- **synthetic** (toy data only)
- **small** (CI-friendly)
- **deterministic** (stable ordering and values)
- **policy-safe** (no secrets, no PII, no protected-site coordinates)
- **reference-first** (IDs and hashes rather than embedded raw datasets)

### What these examples MUST NOT be

Examples MUST NOT include:

- real Kansas cultural site coordinates
- raw text excerpts from restricted archives
- raw imagery from restricted sources
- any secrets/tokens/credentials
- any content that could meaningfully re-identify a person or protected location

If an example needs “place-like” geometry, use either:

- a fake polygon (clearly labeled synthetic), or
- a generalized coarse cell label (e.g., “region_class: west_kansas_demo”), not real coordinates.

---

## 🗂️ Directory Layout

### Location in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📄 README.md                 # This file
~~~

### Recommended example bundle layout (create files as needed)

Keep this folder aligned with what is actually present. Add/remove entries as examples are added.

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                ├── 📄 README.md                         # This file
                │
                ├── 📁 tabular/                           # Tabular examples (SHAP-like / feature attributions)
                │   ├── 🧾 example_manifest.json
                │   ├── 🧾 explanation.json
                │   └── 📄 notes.md
                │
                ├── 📁 narrative/                         # Narrative examples (evidence bundles for Focus Mode)
                │   ├── 🧾 example_manifest.json
                │   ├── 🧾 evidence_bundle.json
                │   ├── 🧾 governance_flags.json
                │   └── 📄 notes.md
                │
                ├── 📁 remote_sensing/                    # Raster/imagery examples (aggregate-only summaries)
                │   ├── 🧾 example_manifest.json
                │   ├── 🧾 explanation.json
                │   └── 📄 notes.md
                │
                └── 📁 integrity/                         # Shared integrity/checksum examples
                    ├── 🧾 checksums.sha256
                    └── 📄 integrity-notes.md
~~~

**Directory rules (normative):**

- Examples MUST remain self-contained (manifest + artifact + notes).
- Use `🧾` for JSON-like files, `📄` for Markdown, `🖼️` for images (only if synthetic and safe).
- Prefer no binary assets unless required; keep CI weight low.

---

## 🧭 Context

### How these examples relate to real runs

Real explainability outputs are generated by tooling and stored under governed run paths (recommended):

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 explainability_manifest.json
        ├── 🧾 explanation.json
        ├── 🧾 provenance_bundle.jsonld
        ├── 🧾 telemetry.json
        └── 🧾 checksums.sha256
~~~

This folder is different:

- `docs/examples/` = **toy examples** for documentation and schema/CI work
- `mcp/experiments/` = **real** run artifacts (governed storage)

### Example selection policy

If you need an example for a sensitive domain:

- provide a **structural** example only (keys and shapes)
- use placeholder IDs and safe values
- include explicit safety notes in `notes.md`

---

## 🗺️ Diagrams

### Example bundle relationship to explainability runtime

~~~mermaid
flowchart TD
  A["Explainability tools<br/>(compute artifacts)"] --> B["Real run artifacts<br/>(mcp/experiments/<run-id>/...)"]
  B --> C["Schemas + validators<br/>(CI enforcement)"]
  C --> D["Docs examples<br/>(this folder)"]
  D --> E["Developers + reviewers<br/>(shape expectations + safe patterns)"]
~~~

Accessibility note: this folder mirrors output shapes for learning/testing, not production logging.

---

## 🧠 Story Node & Focus Mode Integration

### Narrative examples are “evidence-first”

For Focus Mode, the most important explainability example type is a **safe evidence bundle** showing:

- what sources were used (by ID/reference)
- how the system weighted or selected them (bounded scores)
- what governance filters applied (reason codes)
- what cannot be displayed (policy-safe flags)

**Examples MUST NOT include:**
- raw narrative output
- direct quotes from restricted sources

Instead, narrative examples should include:

- stable source IDs (`dcat:` / `stac:` / `graph:` identifiers)
- safe metadata (source type, year bucket, domain tag)
- reference-only links (paths or IDs), not embedded data

---

## 🧪 Validation & CI/CD

### What CI should validate for examples (recommended)

Examples SHOULD be CI-validated for:

- JSON validity (all `🧾` files parse)
- schema validity (when `json_schema_ref` exists)
- deterministic key ordering where required (stable formatting)
- safety scanning:
  - no secrets
  - no PII
  - no protected-site coordinates
- integrity:
  - optional checksum file matches example artifacts

### Fail-closed principle for example rendering

If an example is missing safety metadata, it should be treated as **non-displayable** for UI demos and **fail validation** for governed CI profiles.

---

## 📦 Data & Metadata

### Required fields for an example manifest (recommended contract)

Each example folder SHOULD include an `example_manifest.json` with:

- identity:
  - `example_id`
  - `example_version`
  - `example_kind` (`tabular` | `narrative` | `remote_sensing`)
- model binding:
  - `model_id` (synthetic)
  - `model_version` (synthetic)
- data binding:
  - `dataset_id` (synthetic or public-safe ID pattern)
  - `dataset_version`
- artifact inventory:
  - list of files (relative paths) + sha256
- safety:
  - `classification`, `care_label`, `contains_pii`, `contains_sensitive_locations`
- notes:
  - short description of what the example demonstrates

Minimal skeleton (illustrative):

~~~json
{
  "example_id": "explainability_example_narrative_v1",
  "example_version": "11.2.6",
  "example_kind": "narrative",
  "model": { "model_id": "demo_focus_mode_v3", "model_version": "demo" },
  "dataset": { "dataset_id": "dcat:kfm:dataset:demo-corpus", "dataset_version": "demo" },
  "artifacts": [
    { "path": "evidence_bundle.json", "sha256": "<sha256>" },
    { "path": "governance_flags.json", "sha256": "<sha256>" }
  ],
  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "contains_pii": false,
    "contains_sensitive_locations": false
  },
  "notes": "Structural example only; all IDs are synthetic."
}
~~~

### Example evidence bundle (illustrative, safe)

~~~json
{
  "bundle_id": "demo_evidence_bundle_v1",
  "created": "2025-12-15T00:00:00Z",
  "sources": [
    { "source_id": "dcat:kfm:source:demo:001", "source_type": "docs", "score": 0.81 },
    { "source_id": "dcat:kfm:source:demo:002", "source_type": "dataset", "score": 0.64 }
  ],
  "governance": {
    "redaction_applied": false,
    "suppression_applied": false,
    "reason_codes": []
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment (recommended)

Example manifests should use DCAT-like identifiers (synthetic) to demonstrate:

- stable dataset IDs
- distribution references (artifact files)
- “reference-first” linking patterns

### STAC alignment (recommended)

Remote sensing examples may show how to reference STAC Items/Assets by ID only:

- do not embed imagery
- demonstrate safe aggregates (histograms/quantiles), not raw pixels

### PROV alignment (recommended)

If an example includes provenance, it should demonstrate:

- an explainability computation as `prov:Activity`
- artifacts as `prov:Entity`
- `prov:used` references to model + dataset entities (synthetic IDs)

Keep provenance examples small and structural.

---

## 🧱 Architecture

### Example design principles (normative)

- **One concept per example**:
  - “tabular attribution shape”
  - “narrative evidence bundle shape”
  - “remote sensing aggregate explanation shape”
- **Minimal file set**:
  - manifest + 1–2 artifacts + notes
- **Deterministic formatting**:
  - stable ordering
  - bounded numeric values
- **Clear safety labeling**:
  - explicit “synthetic” statement in notes/manifest
  - explicit “no PII / no sensitive locations” flags

### Adding a new example (recommended workflow)

1. Create a new folder under the correct category.
2. Add `example_manifest.json`.
3. Add one artifact JSON that demonstrates the shape.
4. Add `notes.md` explaining what it demonstrates and how it maps to real runs.
5. Add checksums if the project uses them for examples.
6. Update this README directory tree and Version History.

---

## ⚖ FAIR+CARE & Governance

### Sensitive-domain hard rule

Examples MUST NOT become a backdoor for sensitive disclosure.

Therefore:

- no real protected-site geometries
- no real archival excerpts from restricted materials
- no individual-level data
- no “small cohort” breakdown examples that could be misused

### Training prohibition

Even though these are examples, they are governance artifacts and MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created policy-safe explainability examples hub: defined example bundle conventions (manifest + artifacts + notes), safety constraints, CI validation expectations, and recommended category layout for tabular/narrative/remote sensing examples. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧪 Explainability Examples · Governed for Integrity

[⬅️ Back to Explainability Docs](../README.md) · [⬅️ Back to Explainability](../../README.md) · [🧠 Back to AI Tools](../../../README.md) · [🛡 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

