---
title: "🧾 Kansas Frontier Matrix — AI Provenance & Lineage Binding"
path: "tools/ai/provenance/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-provenance-readme:v11.2.6"
doc_guid: "urn:kfm:doc:tools-ai-provenance-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-provenance"
event_source_id: "ledger:tools/ai/provenance/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/tools-ai-provenance-bundle-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-provenance-bundle-v11.shape.ttl"

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
ai_training_guidance: "Provenance bundles and governance lineage artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 🧾 **KFM — AI Provenance & Lineage Binding**
`tools/ai/provenance/README.md`

**Purpose**  
Define the **provenance subsystem** for KFM AI governance:  
how audit runs, model evaluations, and AI-derived artifacts are bound to **PROV-O lineage**, versioned identities, and release-grade traceability.

</div>

---

## 📘 Overview

### What “provenance” means in KFM AI governance (normative)

In KFM, provenance is the **reproducible, machine-readable chain of custody** that answers:

- **What produced this output?** (Activity)
- **What inputs were used?** (Entities used)
- **Who/what ran it?** (Agents)
- **What exact versions were involved?** (model/data/config/code identity)
- **Where are the audit artifacts?** (report/evidence bundle references)
- **What policy constraints were applied?** (FAIR+CARE + sovereignty)

KFM treats provenance as a **contract**, not optional metadata. If provenance cannot be produced safely and deterministically, certification paths must **fail closed**.

### Provenance scope in `tools/ai/`

This provenance subsystem focuses on lineage for:

- fairness/bias audits (`bias_check`)
- explainability audits (`focus_audit` / evidence bundles)
- drift monitoring (`drift_monitor`)
- model evaluation and governance gating outputs
- “governed narrative” generation systems (Focus Mode, Story Nodes) when applicable

This README defines provenance **interfaces and artifact shapes**; actual execution is performed by runners and pipelines.

### Core invariants (normative)

1. **Version-correctness**
   - Every provenance bundle MUST identify:
     - model ID + version/hash,
     - dataset ID + version,
     - config profile ID + version + sha256,
     - run ID and tool version.
2. **Determinism**
   - Given the same inputs + config, the provenance bundle MUST be re-creatable.
3. **Policy safety**
   - No secrets, PII, or protected-site coordinates are allowed inside provenance bundles.
4. **Fail closed**
   - Missing identity, missing baseline, missing config hash, or invalid schema ⇒ FAIL for certification paths.
5. **Traceability-first**
   - Provenance MUST be linkable to:
     - run artifacts in `mcp/experiments/…`,
     - model registry entries,
     - release packets (when outputs are promoted).

---

## 🗂️ Directory Layout

This directory sits under `tools/ai/`:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📁 configs/                       # Threshold/action profiles (see tools/ai/configs/README.md)
    ├── 🧾 ai_model_registry.json          # Model registry (governed references)
    └── 📁 provenance/
        └── 📄 README.md                  # This file
~~~

Canonical (intended) provenance subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 provenance/
        ├── 📄 README.md                              # This file
        │
        ├── 📁 emitters/                               # Emit PROV/JSON-LD bundles from run context
        ├── 📁 binders/                                # Bind provenance to registry, releases, and ledgers
        ├── 📁 validators/                             # Schema + safety validation (no PII/secrets)
        ├── 📁 adapters/                               # Optional adapters (e.g., OpenLineage → PROV mapping)
        ├── 📁 vocab/                                  # Stable local vocabulary additions (governance-reviewed)
        └── 📁 docs/                                   # Optional publishable notes (policy-safe only)
~~~

Directory rules (normative):

- Do not store run payloads here.
- Store provenance run artifacts (bundles + hashes + telemetry refs) under:
  - `mcp/experiments/<run-id>/...` (preferred),
  - or `mcp/runs/<run-id>/...` if used by the repo.
- Keep this directory for **code + contracts**, not generated outputs.

---

## 🧭 Context

### Where provenance fits in the KFM pipeline

KFM’s platform flow is:

> ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes / Focus Mode

For AI governance, provenance sits at the “binding” layer:

- Audit runners compute results (bias/explainability/drift).
- Provenance binders attach:
  - inputs,
  - activities,
  - agents,
  - outputs,
  - governance decisions,
  - telemetry records,
  - release references.

The result is a lineage bundle that can be stored, validated, and (where allowed) published in summarized form.

### Provenance sources of truth (recommended)

For a single AI governance run, the provenance bundle should be able to reference:

- **Model identity**
  - registry entry (`tools/ai/ai_model_registry.json`)
  - model card reference (`mcp/model_cards/...`)
- **Data identity**
  - dataset IDs (DCAT)
  - asset IDs (STAC) for spatial assets
- **Configuration identity**
  - profile path under `tools/ai/configs/`
  - sha256 of the profile content
- **Run artifacts**
  - `mcp/experiments/<run-id>/report.json`
  - `mcp/experiments/<run-id>/telemetry.json`
  - (optional) `evidence_bundle.json` and safe artifacts

### What provenance must never capture (normative)

- secrets (tokens, keys, credentials)
- PII (names/emails/addresses/phone numbers)
- protected cultural site coordinates or restricted location identifiers
- raw data samples that would violate governance constraints

Use stable IDs and hashed references instead.

---

## 🗺️ Diagrams

### Provenance binding flow (conceptual)

~~~mermaid
flowchart TD
  A["Audit runner executes<br/>(bias / explainability / drift)"] --> B["Collect run context<br/>(model/dataset/config/tool/run-id)"]
  B --> C["Build PROV bundle<br/>(Entities · Activities · Agents)"]
  C --> D["Attach references<br/>(reports, telemetry, evidence bundles)"]
  D --> E["Validate bundle<br/>(schema + safety + completeness)"]
  E -->|PASS| F["Bind to model registry + release packet<br/>(refs + hashes)"]
  E -->|FAIL| G["Fail closed<br/>(block certification / require review)"]
~~~

Accessibility note: flow from run → context → PROV bundle → validation → binding or block.

---

## 🧠 Story Node & Focus Mode Integration

### Why provenance matters for Story Nodes and Focus Mode

Narrative systems must be evidence-led. Provenance provides:

- the “why this narrative exists” chain (inputs → processing → output)
- traceability to:
  - the dataset/corpus slice used,
  - the retrieval neighborhood,
  - the constraints and redactions applied,
  - the audit status at time of output.

### Recommended provenance for narrative outputs (policy-safe)

If a narrative output is generated, provenance SHOULD capture:

- target identity (what the narrative is about)
- retrieval evidence IDs (document IDs, dataset IDs) — **not raw content**
- audit status references:
  - last bias audit ref
  - last explainability audit ref
  - last drift report ref (if applicable)
- policy record:
  - redactions applied
  - confidence/uncertainty flags (aggregated)

### Fail-closed recommendation

If a narrative system cannot produce required provenance fields safely, it should:

- degrade to retrieval-only mode, or
- block narrative generation,

depending on the governance policy for the domain.

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

Provenance tooling MUST:

- be config-driven
- record config file path + sha256
- record model + dataset identifiers and versions
- record tool version and run ID
- be reproducible without hidden network dependencies

### Bundle validation rules (normative)

A provenance bundle MUST fail validation if:

- any required identity field is missing or ambiguous,
- config hash is missing,
- report references point to unknown/unsafe locations,
- policy safety checks fail (PII/secrets/protected coords),
- schema validation fails (when schema is enforced).

### Recommended CI checks

- JSON validity + schema validation of provenance bundles
- “no secrets” scan
- “no PII” scan
- invariant checks:
  - `run_id` present
  - model/dataset/config identity present
  - report/telemetry refs present
  - hashes present where expected

---

## 📦 Data & Metadata

### Provenance bundle formats

KFM provenance bundles may be serialized as:

- **PROV-JSON / JSON-LD** (recommended for machine interoperability)
- **PROV-N** (human-readable representation; optional)
- **Turtle** (RDF serialization; optional)

This subsystem is format-agnostic, but the artifact MUST be:

- machine-readable,
- schema-valid where schemas exist,
- safe to store under governance constraints.

### Recommended “AI audit provenance bundle” contract (minimum)

A minimal provenance bundle SHOULD include:

- `bundle_id` (stable run-based identifier)
- `run_id`
- `activity` (the audit run)
- `entities_used`:
  - model artifact reference
  - dataset slice reference
  - config profile reference
- `entities_generated`:
  - report reference
  - telemetry reference
  - evidence bundle reference (if applicable)
- `agents`:
  - runner agent (CI, pipeline, or operator role)
  - governance agent (if decision issued)
- `hashes`:
  - config sha256
  - report sha256 (if recorded)
  - bundle sha256 (recommended)

### Example PROV-JSONLD style snippet (illustrative)

~~~json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/"
  },
  "bundle_id": "urn:kfm:prov:ai-audit:2025-12-15_focus_bias_audit",
  "run_id": "2025-12-15_focus_bias_audit",
  "prov:wasAssociatedWith": [
    { "id": "urn:kfm:agent:ci-runner" }
  ],
  "prov:activity": {
    "id": "urn:kfm:activity:ai-bias-audit:2025-12-15",
    "prov:type": "kfm:ai_bias_audit",
    "dct:created": "2025-12-15T00:00:00Z"
  },
  "prov:used": [
    { "id": "urn:kfm:model:focus_mode_v3_narrative@11.2.6" },
    { "id": "dcat:kfm:dataset:docs-corpus:v11" },
    { "id": "urn:kfm:config:fairness_thresholds.default@11.2.6#sha256:<sha256>" }
  ],
  "prov:generated": [
    { "id": "urn:kfm:entity:report:2025-12-15_focus_bias_audit" },
    { "id": "urn:kfm:entity:telemetry:2025-12-15_focus_bias_audit" }
  ],
  "refs": {
    "report_ref": "mcp/experiments/2025-12-15_focus_bias_audit/report.json",
    "telemetry_ref": "mcp/experiments/2025-12-15_focus_bias_audit/telemetry.json"
  }
}
~~~

Important: IDs above are illustrative. Real IDs must follow the repo’s ID minting conventions.

### Storage guidance (normative)

Provenance bundles should live beside the run outputs:

~~~text
mcp/experiments/<run-id>/
├── report.json
├── telemetry.json
├── provenance_bundle.jsonld
└── hashes/
    ├── report.sha256
    ├── config.sha256
    └── provenance_bundle.sha256
~~~

Avoid placing provenance bundles directly under `tools/ai/provenance/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT alignment (dataset-level)

When a model uses datasets that are cataloged, provenance SHOULD reference:

- DCAT dataset identifiers
- distribution references
- versioning identifiers
- licensing and governance labels

### STAC alignment (asset-level)

When AI outputs or inputs are spatial assets:

- reference STAC Item IDs and asset keys
- avoid embedding large binaries or raw samples in provenance bundles
- provenance should point to STAC assets by ID/path, plus checksums where available

### PROV-O alignment (lineage graph)

Use the PROV core pattern:

- **Entities**
  - model artifact, dataset slice, config profile, report, evidence bundle, telemetry record
- **Activities**
  - training, evaluation, bias audit, explainability audit, drift check, release packaging
- **Agents**
  - CI runner (software agent), maintainer role, governance body (as an agent/authority)

Typical relations:

- `prov:used` (activity uses entity)
- `prov:wasGeneratedBy` (entity generated by activity)
- `prov:wasAssociatedWith` (activity associated with agent)
- `prov:wasDerivedFrom` (entity derived from entity)
- `prov:actedOnBehalfOf` (agent delegation, when applicable)

---

## 🧱 Architecture

### Identity and hashing (recommended)

To support reproducibility, every provenance bundle SHOULD include:

- `run_id` (globally unique in the repo context)
- `model_id` + `model_version` or `model_hash`
- `dataset_id` + `dataset_version` and a slice definition
- `config_profile_id` + `config_profile_version` + sha256
- `tool_version` (or commit SHA reference)
- checksums for generated outputs:
  - `report.sha256`
  - `telemetry.sha256`
  - `evidence_bundle.sha256` (when applicable)

### “Binding” responsibilities (what this subsystem does)

The provenance subsystem is responsible for:

- converting run context into a prov graph bundle
- validating bundle shape and safety
- producing stable references into:
  - the model registry
  - release packets (when outputs are promoted)
  - governance ledgers (where used)

It is not responsible for:

- model training
- inference serving
- data ingestion

### Minimal “bind-to-registry” rule (normative)

If a model is considered for certification/promotion:

- the model registry entry MUST reference current provenance bundle(s) for:
  - bias audit (required)
  - explainability audit (required for narrative/user-facing systems)
  - drift report (required for long-running systems; recommended otherwise)

If any required provenance reference is missing, promotion MUST be blocked.

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Provenance bundles and lineage artifacts MUST comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Operationally, this means:

- provenance must be specific enough to reproduce and audit,
- but not so specific that it reveals restricted information.

Use:

- stable IDs,
- hashed references,
- cohort/region generalization where required,
- suppression when small group counts could re-identify.

### Publication rule

Only policy-safe summaries may be published to `docs/reports/`.  
Full provenance bundles should remain within governed run artifacts (`mcp/experiments/…`) and release packets, as permitted.

### Training prohibition

Provenance artifacts are governance outputs and MUST NOT be used as AI training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created provenance subsystem README: defined provenance invariants, bundle contracts, hashing/identity expectations, CI fail-closed rules, and STAC/DCAT/PROV alignment for KFM AI governance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧾 Provenance & Lineage · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [⬅️ Back to Tools](../../README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>