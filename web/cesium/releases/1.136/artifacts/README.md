---
title: "🗄️ KFM v11.2.3 — CesiumJS v1.136 Artifacts & Evidence (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed storage layout for visual, metric, and log artifacts supporting CesiumJS v1.136 testing and validation within the Kansas Frontier Matrix web stack."
path: "web/cesium/releases/1.136/artifacts/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 artifact-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-release-1-136-artifacts"
semantic_document_id: "kfm-web-cesium-release-1.136-artifacts"
event_source_id: "ledger:kfm:web:cesium:release:1.136:artifacts"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Test Artifacts"
intent: "web-cesium-release-1-136-artifacts"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🗄️ **KFM — CesiumJS v1.136 Artifacts & Evidence**  
`web/cesium/releases/1.136/artifacts/README.md`

**Purpose:**  
Define the **governed layout and usage** of visual, metric, and log artifacts that provide **evidence** for the CesiumJS **v1.136** release validation in KFM:  
screenshots, performance metrics, and optional logs captured during smoke tests.

</div>

---

## 📘 1. Overview

Artifacts in this directory:

- Support the **release notes** in  
  `web/cesium/releases/1.136/README.md`
- Provide evidence for the **smoke-test suite** in  
  `web/cesium/releases/1.136/tests/README.md` and  
  `web/cesium/releases/1.136/tests/rendering-smoke.md`
- Are used by:
  - Web Visualization Systems WG  
  - Reliability / SLO analysis  
  - FAIR+CARE and governance reviews  

All artifacts must be:

- **Non-sensitive** (no PII, no sensitive locations beyond approved generalization).  
- **Reproducible** (generated via documented test flows).  
- **Traceable** to the specific Cesium release and commit.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/releases/1.136/artifacts/
│
├── 📄 README.md                      # This file — artifact contracts and layout
│
├── 📸 terrain-picking.png            # Screenshot: terrain sampling / elevation probe behavior
├── 📸 billboard-scaling.png          # Screenshot: glyph/billboard/label scaling & halos
│
├── 🧾 metrics.json                   # Aggregate metrics snapshot (FPS, pick latency, etc.)
└── 🧾 logs.txt                       # Optional summarized logs (rendering/picking/terrain) with redaction
~~~

**Directory contract:**

- Only **release-related evidence** for **Cesium v1.136** lives here.  
- File names should be:
  - **Descriptive**, lower-case, dash or camel separated.  
  - Stable across re-runs when possible (avoid random suffixes).  
- New artifacts should be added **sparingly**, with clear purpose.

---

## 📸 3. Screenshot Artifacts

### 3.1 `terrain-picking.png`

**Goal:** Visual confirmation that terrain sampling / elevation probes behave correctly.

**Recommended content:**

- Cesium globe with **terrain enabled**.  
- Visible elevation probe UI (e.g., cursor readout or marker).  
- Region of interest showing **terrain variation** (valley, ridge, slope).

**Guidelines:**

- No sensitive site markers or heritage overlays in this screenshot  
  **unless** they are generalized and CARE-cleared.  
- If any potentially sensitive overlay is visible:
  - Confirm it uses **approved generalization** (e.g., H3-only, masked).  
  - Confirm the screenshot is approved by governance if needed.

---

### 3.2 `billboard-scaling.png`

**Goal:** Visual confirmation of billboard/label fixes in v1.136.

**Recommended content:**

- A cluster of **icons and labels** at various zoom levels.  
- Examples:
  - Heritage/gauging/sensor glyph stack.  
  - Labels with halos.  

**Checks to document visually:**

- Icons remain crisp and properly scaled.  
- Labels are legible; halos look clean.  
- No obvious clipping or depth-test artifacts.

---

## 📊 4. Metrics Snapshot — `metrics.json`

**Goal:** Store a small, human- and machine-readable snapshot of performance metrics for v1.136.

### 4.1 Example Structure (Illustrative Only)

~~~json
{
  "cesium_version": "1.136",
  "scene": "dev-cesium-smoke",
  "frames_sampled": 600,
  "fps_mean": 50.2,
  "fps_p95": 42.1,
  "fps_p99": 35.0,
  "pick_latency_ms_mean": 4.3,
  "terrain_sample_latency_ms_mean": 6.7,
  "notes": "Typical dev laptop, Chrome stable, no throttling."
}
~~~

**Requirements:**

- Metrics must be **aggregate** (no user IDs, no per-request logs).  
- Enough detail to compare versions, not enough to identify users or sensitive patterns.  
- When multiple scenarios are measured, either:
  - Store an **array** of scenario objects, or  
  - Use separate per-scenario keys in the same file.

**Linkage:**

- Metrics here complement telemetry recorded in:  
  `releases/v11.2.3/web-cesium-telemetry.json`  
  under the schema:  
  `schemas/telemetry/web-cesium-release-v1.json`

---

## 📜 5. Optional Logs — `logs.txt`

**Goal:** Provide a **redacted, high-level** summary of logs captured during smoke tests, if needed.

**Examples of acceptable content:**

- Counts of warnings/errors, not raw stack traces, e.g.:

  > WARN: 2 Cesium warnings (texture size), no fatal errors.  
  > ERROR: 0 Cesium runtime errors in smoke scenarios A–H.

- Short excerpts of **non-sensitive** debug output.

**Rules:**

- No PII or user-specific details.  
- No sensitive URLs or access tokens.  
- No raw stack traces referencing sensitive internals where not necessary.

If more detailed logs are required, they should be:

- Stored in a secure, access-controlled log system.  
- Referenced here only by ID or pointer, not inlined.

---

## 🧬 6. Provenance & Reproducibility

Artifacts must be:

- **Reproducible** given:
  - Cesium version (`1.136`).  
  - KFM commit SHA (noted in front matter).  
  - Instructions in `tests/README.md` and `tests/rendering-smoke.md`.

**Provenance chain:**

1. **Release notes**: `web/cesium/releases/1.136/README.md`  
2. **Test definitions**: `web/cesium/releases/1.136/tests/README.md`  
3. **Test scenarios**: `web/cesium/releases/1.136/tests/rendering-smoke.md`  
4. **Artifacts (this directory)**: screenshots, metrics, logs  
5. **Telemetry**: `releases/v11.2.3/web-cesium-telemetry.json` (optional)

All artifacts should be regenerable by following the documented test flows on:

- A known hardware/software baseline, or  
- A clearly documented environment (e.g., “dev-lab-01, Chrome stable, no throttling”).

---

## ⚖ 7. FAIR+CARE & Sovereignty Safeguards

Artifacts must never:

- Reveal **exact locations** of sensitive sites beyond approved generalization.  
- Show **internal-only** or **restricted** layers that are not cleared for documentation.  
- Include any UI with identifiable **usernames, emails, or IDs**.

When in doubt:

- Use **region-level** or **H3-only** representations.  
- Prefer **generic** landscapes and tilesets for screenshots.  
- Seek FAIR+CARE / sovereignty review for any artifact derived from sensitive data.

---

## 🧪 8. Usage in Reviews & CI

Artifacts are used in:

- **Release review meetings**:
  - Quick visual and metric confirmation of claimed improvements.  

- **Post-incident analysis**:
  - When regressions are traced back to a Cesium version upgrade.  

- **Documentation**:
  - Portions of artifacts may be embedded (or referenced) in higher-level docs.

CI **does not** read these artifact files directly, but:

- CI enforces that this `README.md` exists and passes markdown checks.  
- CI may verify that `metrics.json` (if present) is valid JSON.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Established governed artifact layout and usage for CesiumJS v1.136; defined screenshot, metric, and log contracts. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Artifact Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium v1.136 Tests](../tests/README.md) · [⬅ Back to Cesium v1.136 Release Notes](../README.md) · [⬅ Back to Cesium Web Integration Overview](../../../README.md)

</div>
