---
title: "🔐 Kansas Frontier Matrix — Explainability Examples: Integrity (Checksums & Manifests)"
path: "tools/ai/explainability/docs/examples/integrity/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-explainability:examples:integrity-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-examples-integrity"
event_source_id: "ledger:tools/ai/explainability/docs/examples/integrity/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update to your governed “current release” bundle when available.
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../../../schemas/json/tools-ai-explainability-examples-integrity-v11.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/tools-ai-explainability-examples-integrity-v11.shape.ttl"

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
ai_training_guidance: "Integrity examples, checksums, and governance artifacts MUST NOT be used as AI training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🔐 **KFM — Explainability Examples: Integrity**
`tools/ai/explainability/docs/examples/integrity/README.md`

**Purpose**  
Provide **policy-safe integrity examples** (checksums + minimal manifests) for KFM explainability example bundles—so artifact sets are **tamper-evident, reproducible, reference-first**, and CI-verifiable without exposing sensitive data.

</div>

---

## 📘 Overview

### What “integrity” means here

In KFM explainability, “integrity” means:

- artifacts are **verifiably unchanged** (hashes/checksums),
- bundles are **self-describing** (manifest inventories),
- references are **stable and relative** (no absolute paths),
- outputs are **deterministic** (stable ordering, stable formatting),
- validation can run in CI and offline audit environments.

These examples show the **shape and conventions** for integrity artifacts. They are **synthetic** and safe to commit.

### Why integrity matters for explainability

Explainability artifacts often influence governance decisions (e.g., “is this model still certified?”). Without integrity controls:

- artifacts can drift or be overwritten silently,
- audit trails become unreliable,
- UI or reports may render the wrong explanations for a model/version,
- reproducibility is broken (can’t re-check what was reviewed).

### What belongs in this folder

This folder contains **toy** integrity artifacts that demonstrate:

- `checksums.sha256` formatting conventions
- minimal “manifest” inventory conventions
- safe verification commands and CI validation expectations

### What must not be stored here

This folder MUST NOT contain:

- real run outputs from production data
- sensitive images, overlays, or restricted corpora passages
- any secrets, tokens, credentials
- any high-precision protected-site coordinates

Real integrity files for real runs belong under governed run paths (e.g., `mcp/experiments/<run-id>/...`).

---

## 🗂️ Directory Layout

### Location in the repo

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 integrity/
                    └── 📄 README.md                 # This file
~~~

### Recommended integrity example contents (create if missing)

Keep this directory minimal and CI-friendly.

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 integrity/
                    ├── 📄 README.md                 # This file
                    ├── 🧾 checksums.sha256          # Example checksum list (synthetic)
                    ├── 🧾 integrity_manifest.json    # Example inventory manifest (synthetic)
                    └── 📄 integrity-notes.md         # Optional short notes (synthetic)
~~~

**Directory rules (normative):**

- Use only **relative paths** inside checksum/manifests.
- Keep files **small** and **synthetic**.
- Prefer plain text and JSON (`🧾`) over binaries.

---

## 🧭 Context

### How integrity examples map to real explainability bundles

A real explainability run generally yields:

- `explainability_manifest.json` (or equivalent)
- explanation payload(s) (`explanation.json`, `evidence_bundle.json`, etc.)
- optional assets (plots/overlays), if allowed and governance-gated
- telemetry and provenance pointers
- `checksums.sha256`

In real runs, those files live under a governed run folder:

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 <run-id>/
        ├── 🧾 explainability_manifest.json
        ├── 🧾 explanation.json
        ├── 🧾 governance_flags.json
        ├── 🧾 telemetry.json
        ├── 🧾 provenance_bundle.jsonld
        └── 🧾 checksums.sha256
~~~

This folder (`docs/examples/integrity/`) demonstrates integrity patterns without storing real run artifacts.

### Integrity primitives used by KFM

KFM integrity relies on a small set of primitives:

- **SHA-256 hashes** for files (tamper-evidence)
- **Manifest inventory** of what files belong to a bundle (completeness)
- Optional: **release-level signatures / attestations** (handled at release packaging, not here)

This folder focuses on the first two: hashes + inventories.

---

## 🗺️ Diagrams

### Integrity flow (conceptual)

~~~mermaid
flowchart TD
  A["Artifact set created<br/>(explanations + flags + refs)"] --> B["Generate checksums<br/>sha256 over files"]
  B --> C["Generate manifest<br/>(inventory + metadata)"]
  C --> D["CI validation<br/>(schema + checksum verify)"]
  D --> E["Storage under run_id<br/>(governed location)"]
  E --> F["Audit + UI rendering<br/>(reference-first)"]
~~~

Accessibility note: integrity artifacts are generated after the explanation outputs, validated in CI, then stored and referenced for audit and rendering.

---

## 🧪 Validation & CI/CD

### Checksum file format (recommended contract)

KFM recommends the standard `sha256sum`-compatible format:

- One file per line
- `<sha256><two spaces><relative/path>`

Example (`checksums.sha256`):

~~~text
<sha256>  explanation.json
<sha256>  governance_flags.json
<sha256>  evidence_bundle.json
<sha256>  claim_evidence_map.json
<sha256>  integrity_manifest.json
~~~

**Normative formatting rules:**

- Paths MUST be **relative** to the bundle root.
- Lines MUST be sorted lexicographically by path for determinism.
- Line endings MUST be consistent (LF recommended).
- Do not include timestamps or absolute machine paths in checksum files.

### Example verification commands

~~~bash
# Verify all checksums (run from the directory that contains checksums.sha256)
sha256sum -c checksums.sha256

# Generate checksums deterministically (example: hash only JSON + MD; adjust patterns as needed)
find . -maxdepth 1 -type f \( -name "*.json" -o -name "*.md" \) \
  -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
~~~

### CI expectations for integrity artifacts

Integrity validation SHOULD include:

- `checksums.sha256` is present (for bundles that claim integrity)
- checksum verification passes (`sha256sum -c`)
- manifest file is present and schema-valid (when schema exists)
- manifest inventory matches the checksum file:
  - every artifact in manifest appears in checksums
  - no unexpected extra files (unless explicitly allowed)

**Fail-closed guidance:**

If a bundle is intended for governed review/certification and integrity verification fails, the pipeline MUST treat the bundle as **invalid**.

---

## 📦 Data & Metadata

### Minimal integrity manifest (recommended fields)

An `integrity_manifest.json` SHOULD include:

- `manifest_id` and `manifest_version`
- `algorithm` (e.g., `sha256`)
- `bundle_root` (relative indicator, usually `"."`)
- `files[]` inventory:
  - `path` (relative)
  - `sha256`
  - optional: `size_bytes`, `media_type`
- safety metadata:
  - `classification`, `care_label`
  - flags like `contains_pii` and `contains_sensitive_locations`
- provenance pointers (optional for examples; required in real runs):
  - run ID refs, config hash refs

Illustrative `integrity_manifest.json` (synthetic):

~~~json
{
  "manifest_id": "demo_integrity_manifest_v1",
  "manifest_version": "11.2.6",
  "created": "2025-12-15T00:00:00Z",
  "algorithm": "sha256",
  "bundle_root": ".",
  "files": [
    { "path": "explanation.json", "sha256": "<sha256>", "media_type": "application/json" },
    { "path": "governance_flags.json", "sha256": "<sha256>", "media_type": "application/json" },
    { "path": "checksums.sha256", "sha256": "<sha256>", "media_type": "text/plain" }
  ],
  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "contains_pii": false,
    "contains_sensitive_locations": false,
    "contains_secrets": false
  },
  "notes": "Synthetic example manifest for documentation and CI shape testing."
}
~~~

### Determinism and canonicalization rules (recommended)

To keep hashes stable:

- Treat JSON as **bytes-on-disk** unless you enforce canonical JSON serialization.
- If canonical JSON is required, define and document:
  - stable key ordering,
  - stable numeric formatting,
  - stable whitespace rules,
  - UTF-8 encoding,
  - LF line endings.

For examples, keep files small and stable so the hash can remain unchanged across environments.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT

Integrity manifests and checksum files can be referenced as distributions or assets:

- DCAT: integrity manifest as a `dcat:Distribution` attached to a report record
- STAC: integrity files can be attached as assets to a “run report” Item (non-spatial), when KFM catalogs evaluation artifacts

Do not embed full STAC Items or DCAT records in the integrity manifest; prefer references by ID.

### PROV-O

Integrity artifacts support provenance:

- the manifest and checksum file are `prov:Entity`
- they can be generated by an “integrity computation” `prov:Activity`
- they reference the files they attest to (by path + hash)

This helps audits prove “what was reviewed” without relying on mutable assumptions.

---

## 🧱 Architecture

### Why checksums + manifest (both) are useful

- **Checksums** prove files are unchanged.
- **Manifest** proves which files belong to the bundle (completeness + meaning).

Together they support:

- CI enforcement
- offline audits
- release packaging
- UI display gating (don’t show explanations with failed integrity)

### Separation of concerns

- Example integrity files live here (docs/examples) for learning/testing.
- Real run integrity files live under run artifacts.
- Release-level signatures and attestations live in the `releases/` bundle and are governed separately.

---

## ⚖ FAIR+CARE & Governance

### Safety note: integrity artifacts can still leak information

Even without raw data, manifests can leak:

- sensitive filenames,
- sensitive identifiers,
- or inference clues (e.g., “protected-site-overlay.png”).

Therefore:

- use neutral names in examples,
- avoid embedding sensitive tokens/IDs,
- keep safety flags explicit.

### Training prohibition

Integrity artifacts are governance-relevant and MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created integrity examples README: checksum and manifest conventions, deterministic formatting rules, CI validation expectations, and policy-safe guidance for explainability example bundles. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🔐 Integrity Examples · Policy-Safe · Governed for Integrity

[⬅️ Examples Index](../README.md) ·
[⬅️ Explainability Docs](../../README.md) ·
[⬅️ Explainability](../../../README.md) ·
[🛡 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

