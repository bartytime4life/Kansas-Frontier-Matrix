---
title: "🧾 Kansas Frontier Matrix — Explainability Artifact Contract (XAI Bundle Spec)"
path: "tools/ai/explainability/docs/artifact-contract.md"

version: "v11.2.6"
last_updated: "2025-12-16"
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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-artifact-contract:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-xai-artifact-contract"
event_source_id: "ledger:tools/ai/explainability/docs/artifact-contract.md"
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
ai_training_guidance: "Explainability audit artifacts MUST NOT be used as training data."

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.2"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
---

<div align="center">

# 🧾 **KFM — Explainability Artifact Contract**
`tools/ai/explainability/docs/artifact-contract.md`

**Purpose**  
Define the **canonical artifact bundle contract** for KFM explainability (XAI):  
what artifacts MUST be produced, how they MUST be named and structured, what metadata MUST be present, and how outputs MUST be validated and governed—so KFM can safely expose “AI explanation” views (Focus Mode / Story Nodes) while remaining reproducible, auditable, and FAIR+CARE aligned.

</div>

---

## 📘 Overview

### 1) What this contract covers

This document specifies the **Explainability Artifact Bundle** (XAB) contract used by KFM AI systems, including (but not limited to):

- **Tabular / time-series models** (feature attributions, partial dependence, local explanations)
- **Remote sensing models** (saliency / attribution rasters, overlays, region-based summaries)
- **Narrative / retrieval-augmented systems** (evidence bundles, citation traces, retrieval/selection explanations)

This contract defines:

- **Bundle layout**
- **Artifact naming + IDs**
- **Required metadata fields**
- **Safety constraints** (no PII, no restricted coordinates, no secrets)
- **Validation gates** (schema, checksums, deterministic output shape)
- **Provenance bindings** (PROV-O alignment; registry references)

### 2) Normative keywords

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used as normative requirements.

### 3) What “explainability” means in KFM

In KFM, explainability is not a single chart. It is a **governed evidence package** that answers:

- *What evidence was used?* (datasets, documents, STAC/DCAT references)
- *How was evidence selected?* (retrieval/filtering steps; policy-safe aggregates)
- *Which inputs most influenced outputs?* (attributions, saliency, feature importance)
- *What are the limitations?* (coverage, uncertainty, drift/fairness guardrails)
- *Can an auditor reproduce it?* (pinned versions + config + checksums)

### 4) Core invariants (normative)

1. **Every explainability run MUST produce an XAB** (even if minimal).
2. **Every XAB MUST be reproducible**:
   - model ID + version/hash recorded,
   - dataset ID + version recorded,
   - config path + config hash recorded,
   - deterministic output (or explicitly declared nondeterminism with pinned seeds).
3. **Every XAB MUST be safe**:
   - no secrets,
   - no PII,
   - no protected-site coordinates or restricted imagery beyond allowed policy views.
4. **Every XAB MUST be indexable** (at minimum by bundle_id + model_id + run_id).

---

## 🗂️ Directory Layout

### 1) In-repo layout (documentation and examples)

This contract lives under the explainability docs tree:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📄 README.md                                  # AI tools system overview
    ├── 🧪 focus_audit.py                              # Explainability/audit runner (entry point)
    └── 🧠 explainability/
        ├── 📄 README.md                               # Explainability subsystem overview
        └── 📁 docs/
            ├── 📄 README.md                           # Docs index for explainability
            ├── 📄 artifact-contract.md                # This contract (XAB spec)
            └── 📁 examples/
                ├── 📄 README.md                       # Examples index
                ├── 📄 example-tabular.md              # Worked example (tabular)
                ├── 📄 example-remote-sensing.md        # Worked example (remote sensing)
                ├── 📄 example-narrative.md             # Worked example (narrative)
                ├── 📁 integrity/                       # Example integrity patterns
                ├── 📁 narrative/                       # Narrative example bundle(s)
                ├── 📁 remote_sensing/                  # Remote sensing example bundle(s)
                └── 📁 tabular/                         # Tabular example bundle(s)
                    ├── 📁 outputs/                     # Example output artifacts
                    ├── 📁 sample_data/                 # Sample data (policy-safe)
                    └── 📁 templates/                   # Example templates (reports/manifests)
~~~

Notes:
- The presence of `focus_audit.py` is assumed from the AI tools conventions used elsewhere in KFM.
- Example bundles under `docs/examples/` MUST remain policy-safe and lightweight (no large binaries, no sensitive imagery).

### 2) Canonical output layout (Explainability Artifact Bundle)

Explainability outputs MUST NOT be stored in `tools/ai/explainability/` itself.  
Canonical outputs MUST be written under a run-scoped artifact directory, typically:

- `mcp/experiments/<run-id>/...` (preferred), or
- `mcp/runs/<run-id>/...` (if your repo uses a run-only convention).

Canonical XAB layout:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        └── 📁 xai/
            └── 📁 <bundle-id>/                       # Explainability Artifact Bundle (XAB)
                ├── 🧾 manifest.json                   # REQUIRED: index of artifacts + checksums
                ├── 🧾 report.json                     # REQUIRED: summary results + quality metrics
                ├── 🧾 telemetry.json                  # REQUIRED: energy/carbon/runtime (policy-safe)
                ├── 🧾 provenance.jsonld               # RECOMMENDED: PROV-O bundle (policy-safe)
                ├── 🧾 checksums.sha256                # REQUIRED: sha256 list (deterministic order)
                ├── 📄 summary.md                      # OPTIONAL: human summary (policy-safe)
                └── 📁 artifacts/                      # REQUIRED if any artifacts exist beyond JSON
                    ├── 📁 tabular/                    # Optional (if tabular)
                    ├── 📁 remote_sensing/             # Optional (if remote sensing)
                    └── 📁 narrative/                  # Optional (if narrative/RAG)
~~~

Directory rules (normative):
- The **bundle root MUST be self-contained**: a reviewer can validate it without network access.
- All files referenced by `manifest.json` MUST exist relative to the bundle root.
- The `checksums.sha256` file MUST include **every file** in the bundle (including itself MAY be excluded to avoid recursion; choose one approach and keep it consistent).

---

## 🧭 Context

### 1) Where this fits in the KFM pipeline

KFM’s pipeline flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/MapLibre UI → Story Nodes/Focus Mode**

Explainability artifacts sit in the **AI governance layer** and are consumed by:

- **Governance** (audits, certification gates)
- **APIs** (serving explanation summaries and safe artifacts)
- **UI** (Focus Mode “AI explanation” toggle; policy-safe explanations)
- **Provenance graph** (binding runs and artifacts to models/datasets)

**Important boundary:** the frontend MUST NOT read explainability bundles directly from storage.  
It MUST access explanation data through governed APIs.

### 2) Relationship to other AI governance subsystems

Explainability artifacts interact with:

- **Fairness**: fairness audit results may constrain what can be shown (or require warnings).
- **Drift**: drift status may gate whether explanations are “trusted” for production use.
- **Registry**: the model registry MUST point to the latest certified explainability bundle(s).
- **Telemetry**: explainability runs MUST emit energy/carbon/runtime metrics.

### 3) Explainability scope tiers (normative)

KFM distinguishes three tiers of explainability output:

1. **Certification tier (batch / audit)**  
   Produced during certification, release checks, or governance review.  
   MUST be stored as XAB under `mcp/experiments/`.

2. **Operational tier (scheduled monitoring)**  
   Produced periodically (e.g., monthly) to detect regressions in explanation quality.  
   SHOULD be stored as XAB under `mcp/experiments/`.

3. **Interactive tier (per-request / on-demand)**  
   Produced during interactive Focus Mode sessions.  
   MUST be **ephemeral by default** unless governance policy explicitly requires retention.  
   If retained, it MUST be stored as a minimal XAB with strong redaction rules.

---

## 🗺️ Diagrams

### Explainability artifact generation and consumption flow

~~~mermaid
flowchart TD
  A["Select model + dataset slice<br/>(ID + version/hash)"] --> B["Load XAI config<br/>(profile + thresholds)"]
  B --> C["Compute XAI artifacts<br/>(tabular | remote sensing | narrative)"]
  C --> D["Assemble XAB bundle<br/>(manifest/report/telemetry/checksums)"]
  D --> E["Validate bundle<br/>(schema + checksum + safety)"]
  E -->|PASS| F["Register artifact refs<br/>(model registry + provenance)"]
  E -->|FAIL| G["Fail closed<br/>(block certification / block promotion)"]
  F --> H["Serve via API<br/>(policy-safe views)"]
  H --> I["UI: Focus Mode<br/>AI explanation toggle"]
~~~

Accessibility note: the flow goes from selection → computation → bundle assembly → validation → registry/provenance → API → UI.

---

## 🧠 Story Node & Focus Mode Integration

### 1) Why the UI needs a contract

Focus Mode and Story Nodes may surface AI-generated outputs (summaries, classifications, rankings).  
When an “AI explanation” view is available, the UI must be able to:

- show **what influenced** the result (attributions/saliency),
- show **what evidence** was used (citations / dataset IDs),
- show **confidence/limitations** (coverage, uncertainty, drift/fairness status),
- support **auditing** (IDs and provenance references).

This requires a predictable contract that’s stable across model types.

### 2) Minimum explanation payload for UI/API (normative)

Even when full artifacts are not served, the API MUST be able to expose a **policy-safe summary** derived from the XAB:

- `bundle_id`
- `model_id`, `model_version` or `model_hash`
- `dataset_id`, `dataset_version`
- `created_at`
- `xai_methods_used` (e.g., `shap`, `lime`, `integrated_gradients`)
- `coverage_summary` (what percentage of outputs are explainable under the chosen method)
- `quality_summary` (method-specific quality proxies)
- `warnings` (e.g., drift WARN, fairness WARN, missing baseline)
- `artifact_refs` (API-addressable references; not raw file paths)

### 3) Evidence bundle rule for narrative systems (normative)

If a narrative output is shown, the explainability bundle MUST provide a **policy-safe evidence bundle**:

- IDs/refs to cited items (documents/datasets), not raw sensitive content
- retrieval trace at an aggregate level (counts, ranks, filters applied)
- explanation text MUST be tied to evidence references (citations) when those are available

If evidence cannot be produced safely, the system MUST either:
- degrade to retrieval-only mode, or
- block the narrative output (domain policy dependent).

---

## 🧪 Validation & CI/CD

### 1) Required validations for an XAB (normative)

An XAB MUST pass the following validations before it can be used for certification or production promotion:

1. **Manifest completeness**
   - every artifact listed exists,
   - every artifact has sha256 recorded,
   - artifact IDs are unique within the bundle.

2. **Checksum validation**
   - computed sha256 matches recorded sha256 for every file.

3. **Schema validation**
   - `manifest.json`, `report.json`, `telemetry.json` MUST validate against the current schemas (or a pinned schema version if using versioned schemas).

4. **Safety validation**
   - no secrets,
   - no PII,
   - no restricted coordinates,
   - no policy-prohibited content.

5. **Determinism validation**
   - config and seeds are recorded (where applicable),
   - output keys and summary fields are stable.

### 2) Fail-closed rules (normative)

An explainability run MUST be marked FAIL and MUST NOT be treated as certified if:

- model identity is missing/ambiguous,
- dataset identity/version is missing/ambiguous,
- config reference is missing,
- bundle validation fails (schema/checksum/safety),
- artifact provenance references are missing for certification-tier runs.

### 3) Suggested CI wiring (recommended)

A typical CI gate for explainability bundles SHOULD include:

- `schema-lint` for JSON artifacts
- checksum verification
- secret scanning
- policy lint (CARE / sovereignty / redaction checks)
- regression checks for explanation quality metrics (when comparable)

---

## 📦 Data & Metadata

### 1) Bundle identity (normative)

Each Explainability Artifact Bundle MUST have a stable `bundle_id` that is unique within a repository history.

Recommended `bundle_id` format (deterministic, readable):

~~~text
xai__<model-id>__<model-version-or-hash>__<dataset-id>__<window-or-slice>__<run-id>
~~~

Minimum required IDs:
- `run_id` (the execution context; ties to mcp/experiments)
- `bundle_id` (the explainability bundle identifier)
- `model_id` + (`model_version` or `model_hash`)
- `dataset_id` + (`dataset_version` or `dataset_hash`)

### 2) manifest.json (REQUIRED)

The manifest is the authoritative index of everything in the bundle.

Minimum required fields (normative):

- `bundle_id`, `run_id`, `created_at`
- `tool` (e.g., `kfm.tools.ai.focus_audit`)
- `tool_version` (or commit hash)
- `commit_sha` (repo state used to produce bundle)
- `config`:
  - `config_ref` (path or named profile)
  - `config_sha256` (or equivalent)
- `model` identity
- `dataset` identity
- `artifacts[]`:
  - `artifact_id`
  - `artifact_type` (see taxonomy below)
  - `role` (UI/API role)
  - `href` (relative path within bundle)
  - `media_type`
  - `sha256`
  - `size_bytes`
  - `sensitivity` (e.g., `public`, `restricted-summary-only`)
- `integrity`:
  - `checksums_file`
  - `checksum_algorithm`

Illustrative example (non-normative):

~~~json
{
  "bundle_id": "xai__focus_mode_v3__11.2.6__docs_corpus__2025-12__run_2025-12-16_001",
  "run_id": "run_2025-12-16_001",
  "created_at": "2025-12-16T00:00:00Z",
  "tool": "kfm.tools.ai.focus_audit",
  "tool_version": "v11.2.6",
  "commit_sha": "<latest-commit-hash>",
  "config": {
    "config_ref": "tools/ai/configs/domains/focus_mode.yml",
    "config_sha256": "<sha256>"
  },
  "model": {
    "model_id": "focus_mode_v3",
    "model_version": "11.2.6",
    "model_hash": "<sha256>",
    "registry_ref": "tools/ai/registry/ai_model_registry.json"
  },
  "dataset": {
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11",
    "slice": {
      "time": "2025-12-01/2025-12-16",
      "notes": "policy-safe sampling window"
    }
  },
  "integrity": {
    "checksum_algorithm": "sha256",
    "checksums_file": "checksums.sha256"
  },
  "artifacts": [
    {
      "artifact_id": "artifact__evidence_bundle__summary",
      "artifact_type": "xai.evidence_bundle",
      "role": "ui:explanation",
      "href": "artifacts/narrative/evidence_bundle.json",
      "media_type": "application/json",
      "sha256": "<sha256>",
      "size_bytes": 81234,
      "sensitivity": "public"
    }
  ]
}
~~~

### 3) report.json (REQUIRED)

The report summarizes results and quality metrics.

Minimum required fields (normative):

- `bundle_id`, `run_id`
- `status` (`PASS` | `WARN` | `FAIL`)
- `summary`:
  - `xai_methods_used[]`
  - `coverage` (method coverage)
  - `quality_metrics` (policy-safe)
  - `warnings[]`
- `links`:
  - references to drift/fairness status when relevant (IDs/refs; not raw content)

Illustrative example (non-normative):

~~~json
{
  "bundle_id": "xai__focus_mode_v3__11.2.6__docs_corpus__2025-12__run_2025-12-16_001",
  "run_id": "run_2025-12-16_001",
  "status": "WARN",
  "summary": {
    "xai_methods_used": ["evidence_bundle", "attribution_summary"],
    "coverage": {
      "explainable_outputs_pct": 0.98,
      "notes": "Some outputs missing citations due to corpus gaps"
    },
    "quality_metrics": {
      "ai_explainability_score": 0.94,
      "citation_density_mean": 2.8,
      "evidence_bundle_completeness_pct": 0.91
    },
    "warnings": [
      "drift_status=WARN (see drift run ref)",
      "low_evidence_density_on_subset"
    ]
  },
  "links": {
    "drift_ref": "mcp/experiments/run_2025-12-15_drift/xai_drift_report.json",
    "fairness_ref": "mcp/experiments/run_2025-12-10_bias/bias_report.json"
  }
}
~~~

### 4) telemetry.json (REQUIRED)

Telemetry captures runtime and sustainability metrics.

Minimum required fields (normative):
- `run_id`, `bundle_id`
- `runtime_ms`
- `energy_wh`
- `carbon_gco2e`
- summary counts:
  - `artifacts_count`
  - `methods_count`

Illustrative example (non-normative):

~~~json
{
  "run_id": "run_2025-12-16_001",
  "bundle_id": "xai__focus_mode_v3__11.2.6__docs_corpus__2025-12__run_2025-12-16_001",
  "runtime_ms": 184233,
  "energy_wh": 2.7,
  "carbon_gco2e": 3.1,
  "artifacts_count": 12,
  "methods_count": 2
}
~~~

### 5) Artifact taxonomy (normative)

All artifacts MUST declare an `artifact_type` from the controlled taxonomy (extend only via governance review):

- `xai.attribution.global`  
  Global feature importance / summary attributions.

- `xai.attribution.local`  
  Local attributions for specific instances (policy-safe subset).

- `xai.dependence.partial`  
  Partial dependence / ICE summaries (tabular only; policy-safe).

- `xai.saliency.raster`  
  Remote sensing attribution maps (COG/GeoTIFF preferred for spatial; PNG allowed for small previews).

- `xai.overlay.visual`  
  Policy-safe overlay visualization (e.g., saliency on image preview).

- `xai.evidence_bundle`  
  Narrative evidence mapping (citations/refs, retrieval trace summaries).

- `xai.integrity.check`  
  Integrity checks (schema/checksum/coverage outputs).

- `xai.summary.human`  
  Human-readable summary (markdown), policy-safe.

### 6) Media types and size constraints (recommended)

Preferred media types:
- `application/json` for manifests/reports/summaries
- `text/markdown` for `summary.md`
- `image/png` for small previews
- `image/tiff; application=geotiff; profile=cloud-optimized` for spatial rasters
- `application/geo+json` for small vector shapes (policy-safe, masked)

Size guidance (recommended):
- Store large rasters/vectors outside Git history where applicable; keep XAB “thin” and reference large assets via STAC/DCAT/provenance links when allowed by governance.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1) STAC alignment (recommended)

If an explainability artifact is spatial (e.g., saliency raster):

- represent it as a **STAC Asset** linked to the relevant Item(s) or as a derived Item in an XAI collection.
- include role-like tags via `roles` (or an extension) such as:
  - `xai:saliency`
  - `xai:overlay`
  - `xai:preview`

Do not embed full STAC payloads inside the XAB; store only IDs/refs unless the policy requires a local copy.

### 2) DCAT alignment (recommended)

For certification-tier explainability bundles:

- the XAB can be modeled as a **DCAT Distribution** of a model audit record:
  - `mediaType: application/zip` (if packaged)
  - `dct:modified` aligned to `created_at`
  - `dct:identifier` aligned to `bundle_id`

### 3) PROV-O alignment (recommended)

The explainability run should be representable as:

- `prov:Activity` = explainability audit run
- `prov:Entity` = model artifact, dataset slice, XAB files
- `prov:Agent` = CI runner / maintainer role / governance role

Minimal provenance bindings SHOULD include:
- `prov:used` (model + dataset slice + config)
- `prov:generated` (manifest/report/telemetry/provenance)
- `prov:wasAssociatedWith` (agent)

---

## 🧱 Architecture

### 1) Contract-first integration points

The XAB contract is designed to be consumed by:

- **AI tools** (audit runners that generate the bundle)
- **Pipelines** (batch certification gates, scheduled monitoring)
- **Registry** (pointing to certified artifacts)
- **API layer** (serving policy-safe summaries and artifact previews)
- **UI** (Focus Mode explanation panels)

Key architectural rule:
- The UI MUST request explanations through the API.
- The API MUST apply policy filters before returning anything.

### 2) Deterministic explainability strategy (recommended)

Explainability can be fragile if sampling changes. Recommended patterns:

- Use fixed seeds when sampling.
- Record:
  - sample frame definition (how instances were selected)
  - dataset slice timestamps
  - preprocessing versions
- For narrative/RAG:
  - record retrieval settings (top_k, filters, index version)
  - record evidence IDs, not raw content

### 3) “Safe by default” design patterns (normative)

Explainability artifacts MUST avoid leaking restricted content:

- For **tabular**, never include raw rows if they include PII; use aggregated/normalized forms.
- For **remote sensing**, apply masking rules for protected locations when required by sovereignty policy.
- For **narrative**, store:
  - citation IDs,
  - excerpt hashes,
  - redacted snippets only when explicitly permitted.

### 4) Compatibility and evolution (normative)

- The bundle format MUST be versioned (this document version).
- Tools producing XABs MUST include a `tool_version` (or commit hash) in `manifest.json`.
- If fields are added, they MUST be additive (backwards compatible) unless governance approves a breaking change.

---

## ⚖ FAIR+CARE & Governance

### 1) Governance controls (normative)

Explainability bundles are governance artifacts. They MUST comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

### 2) Training prohibition (normative)

XAB artifacts MUST NOT be used as AI training data:
- they may contain governance signals, derived traces, or sensitive redaction patterns.

### 3) Publication rule (normative)

Only **policy-safe** summaries MAY be published outside of controlled artifact storage.

Recommended practice:
- Keep full XAB bundles in `mcp/experiments/`.
- Publish only:
  - high-level summary metrics, and
  - safe example bundles in `tools/ai/explainability/docs/examples/`.

### 4) Human approval boundaries (recommended)

Any change that:
- expands the artifact taxonomy,
- changes what is exposed to the UI,
- or alters redaction rules

SHOULD receive governance review (FAIR+CARE Council and/or Architecture Board), because it can change risk posture.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Initial XAI Artifact Contract: defines the Explainability Artifact Bundle (XAB), required files (manifest/report/telemetry/checksums), artifact taxonomy, validation gates, and STAC/DCAT/PROV alignment for KFM explainability across tabular, remote sensing, and narrative systems. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧾 Explainability Artifact Contract · Governed for Integrity

[⬅️ Back to Explainability](../README.md) · [📚 Explainability Docs](./README.md) · [🛡 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

