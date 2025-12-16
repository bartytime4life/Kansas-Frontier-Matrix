---
title: "📤 Kansas Frontier Matrix — Tabular Explainability Example Outputs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ai/explainability/docs/examples/tabular/outputs/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"
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

doc_uuid: "urn:kfm:doc:tools-ai-explainability-tabular-outputs-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-tabular-outputs"
event_source_id: "ledger:tools/ai/explainability/docs/examples/tabular/outputs/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: true

ai_training_allowed: false
ai_training_guidance: "Example outputs and explainability artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/README.md@v11.2.6"
  - "tools/ai/explainability/docs/examples/tabular/README.md@v11.2.6"
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 📤 **KFM — Tabular Explainability Example Outputs**
`tools/ai/explainability/docs/examples/tabular/outputs/README.md`

**Purpose**  
Define what **documentation-safe tabular explainability outputs** may be stored in this folder (and how), so examples remain **deterministic, policy-safe, CI-safe**, and usable for **documentation, schema tests, and UI demonstrations**—without leaking sensitive or protected information.

</div>

---

## 📘 Overview

### What this folder is

This folder contains **publishable example outputs** for tabular explainability workflows—intended to accompany:

- the tabular examples documentation, and
- “how-to” demonstrations of explainability artifacts (global importance, local attributions, summaries),
- schema and formatting validation during CI.

These outputs are **not** authoritative audit logs. They are **documentation fixtures**.

### What this folder is not

This folder MUST NOT be used for:

- raw datasets or raw feature tables (even “small samples”),
- production explainability artifacts from real runs,
- any artifact containing:
  - PII,
  - secrets/tokens,
  - protected-site coordinates,
  - sensitive cultural knowledge,
  - restricted Indigenous knowledge.

**Real run artifacts** belong in governed run folders (typically under `mcp/experiments/<run-id>/...`) and should follow access control and retention policy.

### Core invariants (normative)

1. **Everything here MUST be documentation-safe**  
   - Use synthetic data, heavily redacted data, or statistically aggregated outputs only.
2. **Everything here MUST be reproducible**  
   - Same inputs/config → same outputs (stable sorting, fixed rounding, pinned tool versions where applicable).
3. **Everything here MUST be small and reviewable**  
   - Outputs should be PR-readable and diff-friendly.
4. **Everything here MUST be clearly labeled as example output**  
   - Use `.example.*` naming conventions and include a manifest describing how the files were produced.

---

## 🗂️ Directory Layout

Location within the explainability examples tree:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    └── 📁 outputs/
                        └── 📄 README.md
~~~

Recommended contents (documentation fixtures only):

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 tabular/
                    └── 📁 outputs/
                        ├── 📄 README.md
                        ├── 🧾 output_manifest.example.json              # Inventory + how generated + checksums
                        ├── 🧾 xai_report.example.json                   # Combined example report (global + local)
                        ├── 📄 xai_summary.example.md                    # Human-readable summary (policy-safe)
                        ├── 🧾 attributions_global_topk.example.json     # Global importance (top-k only)
                        ├── 🧾 attributions_local_topk.example.json      # Local attributions for a few synthetic rows
                        ├── 🧾 feature_dictionary.example.json           # Optional: feature descriptions + units (safe)
                        └── 🧾 checksums.sha256                          # Hashes for integrity (optional but recommended)
~~~

Directory rules (normative):

- This folder MUST contain **only** example artifacts intended for documentation.
- File lists SHOULD be kept aligned with the manifest (`output_manifest.example.json`).
- If an output cannot be made policy-safe, it MUST NOT be committed here—store it in governed run storage.

---

## 🧭 Context

### How these outputs are used

These example outputs are intended to be:

- referenced from the tabular documentation pages (e.g., `example-tabular.md`),
- used as fixtures for:
  - JSON schema validation,
  - documentation rendering tests,
  - UI “example view” demos (if the UI supports loading fixtures).

### Two-tier artifact model (recommended)

**Tier A — Documentation fixtures (this folder)**  
- Safe to commit
- Stable, small, synthetic/redacted
- Used for docs and demonstrations

**Tier B — Governed run artifacts (`mcp/experiments/<run-id>/...`)**  
- Complete, detailed, provenance-bound
- May include sensitive aggregates and restricted metadata (still must avoid secrets/PII)
- Used for audits, governance decisions, and operational traceability

**Rule of thumb:**  
If it is needed for governance/audit, it belongs in Tier B.  
If it is needed for docs and onboarding, it belongs here.

---

## 🗺️ Diagrams

### Example-output promotion flow (docs-safe)

~~~mermaid
flowchart LR
  A["Run explainability (real model + real data)\n→ governed run folder"] --> B["Sanitize / redact / synthesize\n(policy gates)"]
  B --> C["Freeze (deterministic)\n+ add manifest + checksums"]
  C --> D["Commit docs-safe fixtures\n→ docs/examples/**/outputs/"]
  D --> E["Docs/UI consume fixtures\n(no access to governed artifacts)"]
~~~

Accessibility note: flow moves from governed run artifacts → sanitization → deterministic packaging → committed fixtures → documentation/UI usage.

---

## 🧪 Validation & CI/CD

### Required safety checks (normative)

Artifacts committed here MUST pass:

- **secret scanning** (no tokens, credentials, private keys),
- **PII scanning** (no emails, names, phone numbers, addresses, IDs),
- **policy safety review** for domain-sensitive cases (especially if features relate to protected cultural/heritage contexts).

### Determinism requirements (normative)

Example outputs SHOULD be:

- stably sorted (e.g., features sorted by absolute importance desc, then feature name asc),
- rounded to a consistent precision,
- stripped of unstable runtime details (timestamps, hostnames) unless explicitly required,
- pinned to a declared config identity (record config path + hash in the manifest/report).

### What CI should be able to validate

CI (or local checks) should be able to validate:

- JSON is well-formed,
- example artifacts match the manifest inventory,
- optional `checksums.sha256` matches committed files,
- the README documents generation assumptions.

If any file violates policy constraints, the PR must fail (fail-closed principle).

---

## 📦 Data & Metadata

### Recommended manifest contract

The manifest is the “table of contents” for this folder.

**Recommended fields:**

- `manifest_id`, `version`, `created`
- `scope` (tabular explainability example outputs)
- `inputs` (synthetic / redacted description; never raw data)
- `generator` (tool name + version, config identity)
- `files[]` (filename, role, sha256, size_bytes, notes)
- `safety` (redaction method, risk classification, review notes)

Example (illustrative):

~~~json
{
  "manifest_id": "kfm:example:tabular:xai:outputs:v11.2.6",
  "version": "v11.2.6",
  "created": "2025-12-16",
  "scope": "tabular explainability example outputs (docs-safe fixtures)",
  "inputs": {
    "data_policy": "synthetic_or_redacted_only",
    "notes": "No raw rows. No identifiers. No protected coordinates. Aggregated where applicable."
  },
  "generator": {
    "tool": "kfm-explainability",
    "tool_version": "<pin-me>",
    "config_ref": "tools/ai/configs/<profile>.yml",
    "config_sha256": "<sha256>"
  },
  "files": [
    {
      "path": "xai_report.example.json",
      "role": "combined_report",
      "sha256": "<sha256>",
      "notes": "Global + local top-k attributions (synthetic rows only)."
    },
    {
      "path": "xai_summary.example.md",
      "role": "human_summary",
      "sha256": "<sha256>",
      "notes": "Policy-safe narrative summary for docs."
    }
  ],
  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_required": true,
    "pii_present": false,
    "secrets_present": false
  }
}
~~~

### Recommended report contract (docs-safe)

The combined report should be safe and minimal:

- identify the method (SHAP / permutation / etc.) without embedding raw data,
- include only top-k features globally,
- include only a few local explanations (synthetic rows) with top-k contributions,
- include a “safety” block.

Example (illustrative):

~~~json
{
  "run_id": "example_tabular_xai_v11.2.6",
  "status": "EXAMPLE",
  "model": {
    "model_id": "example_tabular_model",
    "model_version": "v11.2.6",
    "model_hash": "<hash>"
  },
  "dataset": {
    "dataset_id": "synthetic:tabular:example:v11",
    "dataset_version": "v11",
    "notes": "Synthetic fixture dataset; no real-world identifiers."
  },
  "methods": [
    {
      "name": "shap",
      "variant": "kernel",
      "notes": "Example-only; values normalized and rounded."
    }
  ],
  "global_importance_topk": [
    { "feature": "feature_a", "importance": 0.41 },
    { "feature": "feature_b", "importance": 0.23 }
  ],
  "local_attributions_topk": [
    {
      "example_row_id": "row_0001",
      "topk": [
        { "feature": "feature_a", "contribution": 0.12 },
        { "feature": "feature_b", "contribution": -0.05 }
      ]
    }
  ],
  "safety": {
    "pii_present": false,
    "secrets_present": false,
    "protected_locations_present": false,
    "notes": "Synthetic rows only; no direct identifiers."
  },
  "manifest_ref": "output_manifest.example.json"
}
~~~

### Naming and labeling rules (normative)

- Use `.example.` in filenames for any committed fixture output.
- Use `example_row_id` values that are synthetic (no natural keys).
- Never include original primary keys, file paths, or source URLs that reveal restricted sources.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

These artifacts can be treated as **documentation distributions** (not datasets):

- `README.md` and `xai_summary.example.md` act as narrative documentation assets.
- `xai_report.example.json` acts as a machine-readable distribution.

If cataloged, prefer a single DCAT record for the “tabular explainability examples” suite, with each file as a distribution.

### STAC

STAC is typically not required for tabular example outputs (non-spatial). If a tabular example is derived from spatial assets, reference the STAC Item IDs in documentation, but do not embed sensitive geometry or coordinates.

### PROV-O

Treat example outputs as provenance-aware artifacts:

- The generation of example outputs can be represented as a `prov:Activity`.
- Each committed file is a `prov:Entity`.
- The manifest provides a lightweight provenance bundle for docs use.

For full provenance, rely on governed run artifacts (Tier B).

---

## ⚖ FAIR+CARE & Governance

### Governance constraints (normative)

All committed fixtures MUST comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Implications:

- **Authority to Control:** if an example touches culturally sensitive topics, it must be fully synthetic and reviewed.
- **Responsibility:** do not publish outputs that increase risk (e.g., exposing patterns that could infer restricted locations).
- **Ethics & Safety:** do not present example outputs in a way that implies operational certification.

### Publication rule (normative)

Only publish what is safe for a public repo.  
When in doubt:

- keep the artifact in governed run storage (Tier B),
- publish only a minimal, sanitized summary here.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Created outputs README for tabular explainability examples: docs-safe fixture rules, manifest/report contracts, determinism and validation requirements, and FAIR+CARE publication constraints. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📤 Tabular Explainability Example Outputs · Docs-Safe Fixtures · Governed for Integrity

[⬅️ Tabular Examples](../README.md) ·
[🧪 Examples Index](../../README.md) ·
[🧩 Explainability Docs](../../../README.md) ·
[🧠 AI Tools](../../../../../README.md) ·
[🛡 Governance](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

