---
title: "🧩 Kansas Frontier Matrix — Explainability Documentation Hub"
path: "tools/ai/explainability/docs/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability-docs-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-docs"
event_source_id: "ledger:tools/ai/explainability/docs/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../schemas/json/tools-ai-explainability-docs-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-explainability-docs-readme-v11.shape.ttl"

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
ai_training_guidance: "Explainability artifacts, audit logs, and governance outputs MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/explainability/README.md@v11.2.6"
---

<div align="center">

# 🧩 **KFM — Explainability Docs**
`tools/ai/explainability/docs/README.md`

**Purpose**  
Provide the **documentation hub** for KFM’s explainability subsystem: how explanations are defined, generated, validated, stored, and rendered (especially in **Focus Mode** and **Story Nodes**) under FAIR+CARE and sovereignty constraints.

</div>

---

## 📘 Overview

This folder is the “docs spine” for **explainability** inside `tools/ai/`:

- What explainability means in KFM terms (governed transparency; not marketing)
- What artifacts are expected (safe-by-default, provenance-bound)
- How UI surfaces explanations (toggle, evidence panels, audit notices)
- How CI validates explanation outputs (schema + safety + reproducibility)
- How to extend explainability safely (new explainers, new artifact types)

**Design intent (KFM-specific):**

KFM’s explainability is **not optional**. It is a governance control that ensures:

- AI outputs remain **traceable** to inputs and sources
- confidence/uncertainty signals are disclosed safely
- sensitive content stays protected (no leaks via explanations)
- “evidence overlays” can be rendered alongside narrative/map content

**Non-goals:**

- This docs folder is not a dumping ground for raw run logs.
- This docs folder is not a place to store protected inputs/outputs.
- This docs folder does not override governance; it documents governed practice.

---

## 🗂️ Directory Layout

This docs hub sits under the explainability subsystem:

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        ├── 📄 README.md                      # Explainability subsystem overview (entry point)
        └── 📁 docs/
            └── 📄 README.md                  # This file (docs hub / index)
~~~

**Recommended internal docs layout (create files as needed):**

> Note: The items below are an *intended* structure for completeness. Only add what is actually implemented; keep this README updated as docs are added.

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            ├── 📄 README.md                  # This index (what’s here, how to use it)
            ├── 📄 artifact-contract.md       # What explanation artifacts look like (required keys, naming)
            ├── 📄 evidence-bundles.md        # Evidence bundles for Focus Mode (assets, captions, provenance)
            ├── 📄 ui-integration.md          # Rendering rules (toggle behavior, audit banners, a11y)
            ├── 📄 redaction-rules.md         # How to prevent leaks (aggregation, k-anon-like guardrails)
            ├── 📄 scoring-metrics.md         # Explainability coverage score and PASS/WARN/FAIL thresholds
            ├── 📄 model-card-linkage.md      # How model cards reference explanation assets
            ├── 📄 faq.md                     # Operational FAQ (what breaks, how to debug safely)
            └── 📁 examples/                  # Tiny, synthetic examples only (no sensitive real data)
                ├── 📄 example-tabular.md
                ├── 📄 example-remote-sensing.md
                └── 📄 example-narrative.md
~~~

**Docs storage rule (normative):**

- Long-lived policy-safe docs live here.
- Run outputs (JSON, plots, saliency maps) belong in **run artifact locations**, typically:
  - `mcp/experiments/<run-id>/...` (preferred)
  - or `mcp/runs/<run-id>/...` where that structure is used
- If you need a “public” or “teaching” example, it MUST be:
  - synthetic / toy-scale,
  - scrubbed of sensitive content,
  - and clearly labeled.

---

## 🧭 Context

### Explainability in Focus Mode

In KFM’s interface, explainability is expected to be **user-visible**:

- “AI explanation” can be presented as a toggle/secondary view
- governance flags can be surfaced through an audit-style panel (e.g., blur notices)

This means explainability artifacts must be producible in a way that is:

- **fast enough** for interaction (or cached and referenced),
- **safe enough** for public display (policy gating),
- **traceable** (every artifact is attributable to a model + data slice + version).

### Explainability as a governance primitive

In KFM, explainability must support governance questions like:

- “Which sources or features most influenced this output?”
- “Which model version produced this explanation?”
- “Is this explanation safe to show at this permission level?”
- “Are we leaking protected-site coordinates via an explanation visualization?”

The answers must be reachable from:

- model registry metadata (IDs/hashes)
- provenance bindings (PROV)
- artifact references (stable paths, checksums)

---

## 🗺️ Diagrams

### Explainability artifact lifecycle

~~~mermaid
flowchart TD
  A["Model run (training or inference)<br/>model_id + model_version/hash"] --> B["Select explainer profile<br/>(config-driven)"]
  B --> C["Compute explanation artifacts<br/>(attributions, summaries, evidence refs)"]
  C --> D["Apply safety gates<br/>(aggregation + redaction + policy checks)"]
  D --> E["Validate schemas + checksums<br/>(CI-safe outputs)"]
  E --> F["Store artifacts under run_id<br/>(mcp/experiments/... or equivalent)"]
  F --> G["Register references<br/>(model registry + provenance)"]
  G --> H["Render in UI<br/>(Focus Mode toggle / evidence panel)"]
~~~

Accessibility note: The flow moves from model run → explainer selection → artifact generation → safety gates → validation → storage → registration → UI rendering.

---

## 🧠 Story Node & Focus Mode Integration

### What “explainability” means for narrative systems

For narrative generation (Focus Mode summaries, Story Node augmentation), explainability is usually **evidence-focused**:

- which sources were retrieved
- which facts were selected
- what confidence signals were present
- what governance filters suppressed/redacted content

**Recommended (safe) explainability artifacts for narrative systems:**

- retrieval evidence bundle:
  - list of source IDs (DCAT/STAC/graph IDs)
  - per-source weights/scores (bounded, non-sensitive)
- citation coverage metrics:
  - percentage of sentences with evidence links
- uncertainty/quality indicators:
  - low/med/high confidence tags (policy-safe)
- safety gating report:
  - counts of items redacted
  - reason codes (e.g., “sensitivity flag”, “insufficient provenance”)

### Hard constraint: explanations must not create new leakage paths

Explanations can leak more than outputs if not controlled.

Therefore, narrative explainability MUST:

- avoid raw text dumps from restricted corpora
- avoid showing exact coordinates for protected places
- avoid small-cohort drilldowns that re-identify individuals or sites
- prefer aggregated summaries and stable IDs over raw content

---

## 🧪 Validation & CI/CD

### Minimum compliance checks for explainability docs

This docs directory is subject to KFM Markdown protocol checks and standard CI profiles:

- markdown lint + structure checks
- metadata schema validation (front-matter)
- accessibility checks (headings, readability cues, diagram accessibility notes)
- footer/governance link checks
- provenance expectations (when versioned)

### Validation checks for explainability *artifacts* (referenced by these docs)

Explainability artifacts should be validated by CI or offline validators for:

- **schema validity** (JSON schema / SHACL where applicable)
- **determinism** (same inputs/config → stable output shape)
- **safety scans**:
  - no secrets
  - no PII
  - no restricted coordinates
- **provenance completeness**:
  - model_id + version/hash
  - dataset_id + version
  - window/baseline identity if applicable
  - config reference + config hash
  - checksums for artifacts

**Fail-closed rule (normative):**

If safety classification metadata is missing or ambiguous, explainability outputs MUST be treated as **non-displayable**, and pipelines MUST fail closed for governed contexts.

---

## 📦 Data & Metadata

### Minimal metadata for explainability artifacts

Every explanation artifact set SHOULD have a compact metadata record (JSON) that includes:

- identity:
  - `run_id`
  - `artifact_set_id` (stable)
- model:
  - `model_id`
  - `model_version` or `model_hash`
- data:
  - `dataset_id`
  - `dataset_version`
  - optional slice/window definition
- explainer:
  - `explainer_id` (e.g., `shap`, `lime`, `integrated_gradients`, `evidence_bundle_v1`)
  - config path and config hash
- safety:
  - classification / sensitivity
  - redaction flags + reason codes (if any)
- integrity:
  - sha256 checksums for the artifacts that will be referenced elsewhere

**Policy note:** “Metadata-rich, content-light” is preferred for public visibility.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (when explanations include visual/geo artifacts)

If explainability produces images/plots/rasters that are meaningful as assets (e.g., saliency overlays, time-series plots, annotated imagery):

- store them as **assets** that can be referenced
- ensure each asset has:
  - a safe title/description
  - a media type
  - a provenance reference (how it was derived)

A common pattern is to attach explainability artifacts as extra assets on a STAC Item representing:
- a model output product, or
- a “report item” representing an evaluation run.

### DCAT alignment (dataset-level transparency)

When explainability is about *datasets* and *model behavior* across releases:

- DCAT dataset records may reference explainability reports as distributions
- keep distribution files policy-safe (aggregate metrics and IDs, not raw content)

### PROV-O alignment (traceability)

Explainability is lineage:

- `prov:Activity` = “explainability computation”
- `prov:Entity` = model artifact, dataset slice, explanation artifact set
- `prov:wasDerivedFrom` = explanation derived from model+data slice
- `prov:wasAssociatedWith` = CI runner / maintainer / governed agent role

This is what makes “AI explanation” auditable instead of decorative.

---

## 🧱 Architecture

### How to extend explainability (without breaking governance)

When adding a new explainer or artifact type:

1. Add or update the explainer implementation (code lives outside this docs folder).
2. Define the artifact contract (keys, file naming, checksum rules).
3. Define safety gates for that artifact type:
   - what must be aggregated,
   - what must be redacted,
   - what must never be emitted.
4. Add validation:
   - schema (JSON schema and/or SHACL)
   - deterministic shape expectations
5. Update UI integration guidance:
   - how it renders,
   - what permissions can see it,
   - a11y expectations for any visuals.

### Interface boundaries (normative)

Explainability docs may describe graph/cat alignment, but the UI must stay behind APIs and catalogs:

- front-end consumes explainability assets via API/cached catalogs
- no direct graph access from the UI
- no “hidden” retrieval of protected content through explanation endpoints

---

## ⚖ FAIR+CARE & Governance

Explainability must satisfy both transparency and protection:

- **FAIR**: explanations are findable and reusable through stable IDs and explicit provenance
- **CARE**: explanations never undermine sovereignty protections (especially around protected places)

**Redaction principles (normative):**

- Prefer **aggregates** (distributions, percentiles, counts) to raw values.
- For spatial explanations:
  - never expose protected coordinates
  - prefer generalized geometry (e.g., coarse cells) where policy demands
- For text explanations:
  - avoid quoting restricted corpora
  - prefer citing IDs and showing short, permitted summaries

**Publication rule:**

Only policy-safe explainability summaries may be copied into `docs/` outside tools. Full artifact sets belong in run artifacts.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created Explainability docs hub index: intended docs map, artifact lifecycle, safety/CI rules, and alignment notes for Focus Mode + provenance-bound explainability. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧩 Explainability Docs Hub · Governed for Integrity

[⬅️ Back to Explainability](../README.md) · [🧠 Back to AI Tools](../../README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
