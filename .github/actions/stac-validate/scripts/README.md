---
title: "🧰 Kansas Frontier Matrix — STAC Validate Scripts"
path: ".github/actions/stac-validate/scripts/README.md"
version: "v11.2.3"
last_updated: "2025-12-13"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Architecture Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/github-infra-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-stac-validate-scripts"
role: "stac-validation-helper-scripts"
category: "Metadata · STAC · CI/CD · Scripts"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Metadata"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"

provenance_chain:
  - ".github/actions/stac-validate/scripts/README.md@v11.2.3"

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:scripts:v11.2.3"
semantic_document_id: "kfm-action-stac-validate-scripts"
event_source_id: "ledger:.github/actions/stac-validate/scripts/README.md"
immutability_status: "mutable-plan"
machine_extractable: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next stac-validate scripts update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and metadata pipeline events"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — STAC Validate Scripts**
`.github/actions/stac-validate/scripts/`

**Purpose**  
Provide **deterministic, config-driven helper scripts** used by the STAC validation action to:
- Validate STAC 1.x Items/Collections under **KFM‑STAC v11**
- Run **spatiotemporal consistency checks** (geometry/bbox/time)
- Emit **machine-readable JSON** suitable for CI telemetry (without leaking sensitive content)

</div>

---

## 📘 Overview

This directory is reserved for helper scripts invoked by:

- `.github/actions/stac-validate/entrypoint.sh`
- (Optionally) `.github/actions/stac-validate/action.yml`

These scripts are **internal implementation details** of the `stac-validate` action.

### Normative usage rules

1. **Do not call scripts directly from workflows**  
   Workflows SHOULD invoke the action entrypoint (`entrypoint.sh`) or the composite action interface.
2. **Deterministic outputs**  
   Given the same STAC inputs and configuration, scripts MUST produce the same JSON outputs and severities.
3. **No network side-effects**  
   Scripts SHOULD NOT fetch remote schemas, catalogs, or assets at runtime. If external references are required,
   they MUST be vendored or pinned as part of the action environment.
4. **Structured output first**  
   Scripts SHOULD write JSON outputs to explicit paths (passed by flag). Human-readable logs are secondary and
   MUST avoid printing full geometries, secrets, or sensitive identifiers.

### Recommended script contracts

This folder MAY contain scripts such as:

- `run_stac_validator.py` — STAC schema/profile validation wrapper
- `check_spatiotemporal.py` — bbox/geometry/time consistency checks
- `summarize_stac_results.py` — merges multiple tool outputs into one summary

If these files are absent, this README defines the intended contract for future implementations.

---

## 🗂️ Directory Layout

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 stac-validate/
        └── 📁 scripts/                           — Helper scripts used by stac-validate
            ├── 📄 README.md                      — ← This file
            ├── 📄 run_stac_validator.py          — (optional) STAC core + KFM profile validation
            ├── 📄 check_spatiotemporal.py        — (optional) geometry/bbox/time consistency checks
            └── 📄 summarize_stac_results.py      — (optional) aggregate outputs → summary JSON
~~~

---

## 🧭 Context

### Execution flow (typical)

1. `entrypoint.sh` receives a `stac_root` (e.g., `data/stac`) and config options.
2. A validator runner script checks each STAC JSON:
   - STAC core conformance (Item/Collection)
   - KFM profile conventions (required fields, conventions, extension rules)
3. A spatiotemporal checker script validates:
   - GeoJSON geometry validity
   - `bbox` matches geometry bounds (within numeric tolerance)
   - `datetime` and/or `start_datetime`/`end_datetime` consistency
4. A summarizer script merges outputs into a single JSON summary.
5. `entrypoint.sh` normalizes results into a governed exit status and emits any telemetry artifacts.

### File I/O boundaries

Scripts MUST treat the repository workspace as read-only except for **explicit output files**.

Recommended pattern for outputs:

- Write all generated artifacts to a workflow scratch path such as:
  - `_stac-validate/` (local scratch)
  - or a user-provided output path

Scripts MUST NOT modify `data/stac/**` in-place.

### Canonical issue record shape (recommended)

Scripts SHOULD emit issues using a shared record shape to simplify aggregation:

~~~json
{
  "tool": "stac-validate",
  "file": "data/stac/example/collection.json",
  "severity": "error",
  "code": "KFM_STAC_MISSING_LICENSE",
  "message": "Required field 'license' is missing or empty.",
  "json_path": "/license"
}
~~~

Severity values SHOULD be constrained to:

- `none`
- `warning`
- `error`
- `critical`

---

## 🧪 Validation & CI/CD

### Local run examples (developer use)

These examples demonstrate the intended CLI surface area for scripts. Actual flags MAY vary, but must remain
deterministic and machine-friendly.

~~~bash
# Example: run core STAC validation wrapper
python .github/actions/stac-validate/scripts/run_stac_validator.py \
  --stac-root data/stac \
  --profile kfm-stac-v11 \
  --config-dir .github/actions/stac-validate/config \
  --out _stac-validate/run_stac_validator.json
~~~

~~~bash
# Example: run extra spatiotemporal checks
python .github/actions/stac-validate/scripts/check_spatiotemporal.py \
  --stac-root data/stac \
  --config-dir .github/actions/stac-validate/config \
  --out _stac-validate/check_spatiotemporal.json
~~~

~~~bash
# Example: summarize into a single telemetry artifact
python .github/actions/stac-validate/scripts/summarize_stac_results.py \
  --inputs _stac-validate/run_stac_validator.json _stac-validate/check_spatiotemporal.json \
  --out _stac-validate/summary.json
~~~

### CI expectations

When invoked by `.github/workflows/stac_validate.yml` (or an equivalent governed workflow), scripts MUST:

- Exit non-zero only for **execution failures** (crash, invalid CLI args, unreadable input paths).
- Represent validation failures in the JSON output and allow `entrypoint.sh` to enforce policy thresholds.
- Keep logs concise and safe for public CI output.

### Common failure modes and required handling

- Missing `stac_root` directory  
  - MUST be handled gracefully (emit zero-checked summary or controlled error, depending on action policy).
- Invalid JSON  
  - MUST emit an `error` issue record with file reference and a short parse message.
- Large geometry payloads  
  - MUST NOT be printed to stdout; issue messages should reference the file and path only.

---

## ⚖ FAIR+CARE & Governance

This directory is part of a governed CI/CD surface area and is subject to scanning.

Scripts and their logs MUST NOT expose:

- Secrets, tokens, credentials
- PII/PHI
- Sensitive location information beyond what is already present in governed `data/stac/**`

Recommended safeguards:

- Redact values in logs by default (only show file paths and issue codes).
- Prefer summary counts for telemetry (e.g., issues per collection) over verbose per-feature dumps.
- Treat governance and sovereignty references as **normative constraints**, not optional hints.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-13 | Established governed scripts README; defined deterministic contracts and safe logging expectations. |

---

<div align="center">

🧰 **STAC Validate Scripts (v11.2.3)**  
Deterministic Validation · Telemetry-Ready · FAIR+CARE-Governed  

[⬅ STAC Validate Action README](../README.md) · [⚙️ Config README](../config/README.md) · [⬅ GitHub Infra Overview](../../README.md)  
[⚖ Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Sovereignty Policy](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>

