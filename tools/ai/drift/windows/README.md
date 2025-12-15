---
title: "🪟 Kansas Frontier Matrix — Drift Windows (tools/ai/drift/windows)"
path: "tools/ai/drift/windows/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-drift-windows-readme:v11.2.6"
doc_guid: "urn:kfm:doc:tools-ai-drift-windows-readme:v11.2.6"
semantic_document_id: "kfm-tools-ai-drift-windows"
event_source_id: "ledger:tools/ai/drift/windows/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
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
ai_training_guidance: "Drift windows and drift artifacts MUST NOT be used as AI training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

json_schema_ref: "../../../../schemas/json/tools-ai-drift-windows-readme-v11.json"
shape_schema_ref: "../../../../schemas/shacl/tools-ai-drift-windows-readme-v11.shape.ttl"

provenance_chain: []
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next drift subsystem update"
---

<div align="center">

# 🪟 **KFM — Drift Windows (v11)**  
`tools/ai/drift/windows/README.md`

**Purpose**  
Define the **windowing subsystem** used by KFM drift monitoring: how we segment data into **time- and event-bounded windows** so drift metrics are **deterministic, reproducible, comparable**, and safe under FAIR+CARE constraints.

Windows are consumed by:

- `tools/ai/drift/detectors/` (drift algorithms need “baseline vs current window”)  
- `tools/ai/drift/metrics/` (metrics must be computed per window, consistently)  
- `tools/ai/drift/reporters/` (reports need stable, human-readable window IDs)  

</div>

---

## 📘 Overview

### What “drift windows” mean in KFM

A **drift window** is a *precisely defined slice* of observations used for drift evaluation. In the simplest case, drift compares:

- **Baseline window** (reference distribution)  
- **Current window** (recent distribution)

Windowing is not “just dates.” It is a *contract* that includes:

- **Anchor** (what time the window is defined relative to)  
- **Bounds** (start/end, inclusive/exclusive semantics)  
- **Timezone** (UTC by default for reproducibility)  
- **Eligibility** (minimum sample size and safety rules)  
- **Selection query** (how data is selected from STAC/DCAT/provenance context)

### Why this matters

Without governed window semantics, drift can become:

- Non-reproducible (“today’s 30 days” changes every run)
- Non-comparable (windows don’t align across models or domains)
- Unsafe (small subgroups can be exposed via narrow windows)
- Operationally noisy (alerts from inconsistent window slicing)

### What this README covers

- Required window concepts and naming rules
- Recommended window profiles (rolling, anchored, seasonal)
- Output metadata contracts (window spec + summaries)
- Integration points with detectors/metrics/reporters
- FAIR+CARE safety constraints specific to windowing

---

## 🗂️ Directory Layout

> The repo snapshot confirms `tools/ai/` exists as the “AI evaluation and drift analysis tools” area. The drift subtree below is the **intended** internal organization and MUST be kept “all together” under `tools/ai/drift/` once present.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        ├── 📄 README.md                         # Drift subsystem index (links to baselines/detectors/metrics/windows/reporters)
        ├── 📁 baselines/                        # Reference distributions and baseline-building guidance
        ├── 📁 detectors/                        # Drift detection algorithms (PSI, JS/KL, KS, embeddings, etc.)
        ├── 📁 metrics/                          # Drift metrics, aggregation, normalization, scoring
        ├── 📁 reporters/                        # Report generation (JSON/MD artifacts, dashboards)
        ├── 📁 windows/                          # 🪟 Window definitions + selectors + validators (THIS MODULE)
        │   ├── 📄 README.md                     # This file
        │   ├── 📁 profiles/                     # Window profiles (rolling/anchored/seasonal), domain-tagged
        │   ├── 📁 selectors/                    # Data selection helpers (map window → STAC/DCAT query plan)
        │   ├── 📁 aligners/                     # Alignment rules (ensure windows match across datasets/models)
        │   ├── 📁 validators/                   # Determinism, min-sample, and safety validators
        │   └── 📁 examples/                     # Minimal example window specs and expected outputs
        └── 📁 docs/                             # Drift documentation set (system-level drift docs)
~~~

**Directory layout rules (normative):**

- Directory trees MUST use `~~~text` fences and the emoji + branch glyph style.
- This module MUST NOT be split across multiple locations; all windowing logic/docs live under `tools/ai/drift/windows/`.
- If additional windowing subdirs are added, they MUST be reflected here and linked from `tools/ai/drift/README.md`.

---

## 🧭 Context

### Where windowing sits in the drift pipeline

Windowing is a **precondition** for drift detection. Every detector should be able to assume:

1. A baseline window spec exists (or can be resolved from registry/config)
2. A current window spec exists (resolved deterministically)
3. Both windows carry enough metadata to be provenance-linked and reproducible

### Primary integration points

- **Configs**: expected to be declared under `tools/ai/configs/` (domain- and environment-scoped), then referenced by drift runs.
- **Run logs**: drift runs that use these windows should record outputs in a governed run location (commonly the MCP experiments area for reproducible logs, plus release telemetry if certified).

> The repo snapshot confirms `mcp/experiments/` exists for reproducible run records. Window specs and summaries are expected to be attachable to those runs as non-sensitive metadata.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
    A[Incoming observations\n(dataset/model outputs)] --> B[🪟 Window Resolver\nprofile + anchor + bounds]
    B --> C[Selectors\nwindow -> query plan]
    C --> D[Baseline Window\n(reference slice)]
    C --> E[Current Window\n(recent slice)]
    D --> F[Detectors]
    E --> F[Detectors]
    F --> G[Metrics + Scoring]
    G --> H[Reporters\n(artifacts + telemetry)]
~~~

Accessibility note: the diagram shows that windowing occurs before detectors/metrics, producing baseline/current slices that are compared, then reported.

---

## 🧪 Validation & CI/CD

### What must be validated for windows

A window definition MUST be validated for:

- **Determinism**  
  The same inputs (anchor time + profile + timezone + data selection rules) yield identical bounds and selection decisions.

- **No overlap errors (unless intended)**  
  Rolling windows may overlap by design; anchored windows must not overlap unless explicitly configured.

- **Minimum sample size**  
  The system MUST support “fail closed” (no drift claim) when sample size is too small for safe inference.

- **Safety constraints**  
  Cohort/window combinations that would reveal sensitive, small-population signals MUST be suppressed or generalized (see FAIR+CARE section).

### Recommended CI checks (aligned to KFM’s markdown protocol regime)

- Schema validation for any machine-readable window specs
- Secret/PII scans for emitted artifacts and examples
- Lint checks for Markdown and structured docs

---

## 📦 Data & Metadata

### Window Spec

A **Window Spec** is the minimal, machine-readable definition of a window.

Normative fields (recommended contract):

- `window_id` (stable, slug-safe)
- `window_type` (`rolling_time`, `anchored_time`, `count`, `event`, `release`)
- `anchor_datetime` (ISO 8601, UTC)
- `start_datetime` / `end_datetime` (ISO 8601; recommended half-open interval `[start, end)`)
- `timezone` (`UTC` strongly preferred)
- `step` (for sliding windows; e.g., `P1D`)
- `duration` (e.g., `P30D`)
- `min_samples` (integer)
- `selection` (query plan: STAC/DCAT filters, provenance constraints)
- `safety` (suppression thresholds and masking flags)

~~~json
{
  "window_id": "rolling_30d__anchor_2025-12-15",
  "window_type": "rolling_time",
  "anchor_datetime": "2025-12-15T00:00:00Z",
  "start_datetime": "2025-11-15T00:00:00Z",
  "end_datetime": "2025-12-15T00:00:00Z",
  "timezone": "UTC",
  "duration": "P30D",
  "step": "P1D",
  "min_samples": 500,
  "selection": {
    "source_kind": "stac",
    "collection": "<collection-id>",
    "query": {
      "datetime": "2025-11-15T00:00:00Z/2025-12-15T00:00:00Z"
    }
  },
  "safety": {
    "suppress_if_small_groups": true,
    "min_group_n": 50,
    "mask_sensitive_geometries": true
  }
}
~~~

### Window Summary

A **Window Summary** is an output artifact describing what actually happened:

- `resolved_bounds` (final start/end)
- `selected_item_count`
- `eligible` (true/false)
- `eligibility_reason` (if false)
- `hashes` (optional checksums of selection manifests)
- `provenance_refs` (dataset IDs, model IDs, run IDs)

This summary should be safe to store long-term and reference from reports.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (recommended)

When drift is run against STAC-indexed assets:

- Window bounds map to the STAC `datetime` search interval.
- The selection manifest can be represented as:
  - A list of STAC Item IDs (preferred), or
  - A STAC Search query snapshot (for replayability)

### DCAT alignment (recommended)

When drift is run against DCAT-described datasets:

- Window bounds map to dataset temporal coverage (`dct:temporal`) and/or update records (`dct:modified`)
- The selection should reference:
  - `dct:identifier` (dataset ID)
  - `dcat:distribution` (specific distribution/version if applicable)

### PROV alignment (recommended)

Windowing SHOULD be recorded as a provenance-linked activity:

- `prov:Activity` = “window resolution”
- `prov:used` = baseline inputs + current inputs + window profile config
- `prov:generated` = window spec + window summary

This makes drift results auditable and reproducible.

---

## 🧱 Architecture

### Window profile types

KFM drift windowing should support (at minimum):

1. **Rolling time windows**  
   “Last 7 days”, “last 30 days”, “last 90 days”.

2. **Anchored time windows**  
   Calendar-aligned windows: “2025-11 (month)”, “2025-Q4 (quarter)”.

3. **Seasonal windows (domain-aware)**  
   Windows aligned to known seasonal cycles (only when explicitly configured and justified).

4. **Count-based windows**  
   “Last 10,000 observations” (useful for high-frequency streams).

5. **Event/release windows**  
   Windows aligned to dataset release IDs or model version cutovers.

### Determinism rules (normative)

- All windows MUST be resolvable from:
  - (profile + anchor + timezone + dataset/model IDs)
- Default timezone MUST be UTC unless a domain requires otherwise (and that exception must be explicit in config).
- Interval semantics MUST be documented and consistent across the drift subsystem:
  - Recommended: `[start, end)` to avoid boundary double-counting.

### Window alignment rules (normative)

When comparing two signals (baseline vs current), alignment MUST ensure:

- Same feature set and preprocessing assumptions (owned by metrics, but windows must not break it)
- Equivalent temporal semantics (event-time vs processing-time must be explicit)
- Comparable sampling frames (avoid mixing “calendar month” baseline with “rolling 30d” current unless explicitly intended)

### Safety + suppression rules (normative)

Windows MUST support suppression gates:

- If `selected_item_count < min_samples` → mark window ineligible; do not compute drift claims.
- If cohort slicing yields small groups (below `min_group_n`) → suppress subgroup drift output or generalize.

---

## ⚖ FAIR+CARE & Governance

Windowing has unique ethical risk modes:

- **Time-slicing can deanonymize**  
  Very narrow windows + rare events can leak sensitive information by inference.

- **Small-group hazards**  
  Drift per subgroup (especially intersectional cohorts) can reveal protected signals.

Therefore:

- Drift windows MUST include a safety section (suppression and masking flags).
- Any window definition that targets culturally sensitive geographies MUST respect sovereignty rules:
  - Do not emit high-precision coordinates in window manifests.
  - Use generalized spatial indexing (e.g., coarse H3) where required by policy.

Windowing MUST “fail closed”:
- If safety eligibility is uncertain → do not publish drift claims; emit only a governance-safe summary.

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                 |
|------------:|-----------:|-------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-15 | Initial governed documentation for drift window semantics and contracts. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🪟 Drift Windows · KFM v11 · MCP-DL v6.3 · FAIR+CARE Governed

[⬅️ Drift Index](../README.md) ·
[📏 Drift Metrics](../metrics/README.md) ·
[🧪 Drift Detectors](../detectors/README.md) ·
[🧾 Drift Reporters](../reporters/README.md) ·
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>