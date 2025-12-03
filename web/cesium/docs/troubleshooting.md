---
title: "🧯 KFM v11.2.3 — Cesium Troubleshooting & Incident Playbook (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Operational troubleshooting and incident-response patterns for CesiumJS in the Kansas Frontier Matrix web stack, covering performance, interaction, rendering, and governance-related issues."
path: "web/cesium/docs/troubleshooting.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v11.2.3 Cesium-troubleshooting-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:web-cesium-troubleshooting-v11.2.3"
semantic_document_id: "kfm-web-cesium-troubleshooting-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:docs:troubleshooting:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-cesium-release-v1.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Subsystem Troubleshooting Guide"
intent: "web-cesium-troubleshooting"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Moderate"
redaction_required: true

ontology_alignment:
  schema_org: "TechArticle"
  cidoc: "E73 Information Object"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/web-cesium-troubleshooting-v1.json"
shape_schema_ref: "../../schemas/shacl/web-cesium-troubleshooting-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded on next major Cesium troubleshooting overhaul"
---

<div align="center">

# 🧯 **Kansas Frontier Matrix — Cesium Troubleshooting & Incident Playbook**  
`web/cesium/docs/troubleshooting.md`

**Purpose:**  
Provide a **governed, repeatable incident-response guide** for CesiumJS in the KFM web stack — covering performance problems, tile-load issues, camera glitches, picking failures, and governance/CARE violations — with clear **symptoms → diagnostics → remediation** flows.

</div>

---

## 📘 1. Scope & Relationships

This playbook complements:

- `web/cesium/README.md` — Cesium subsystem overview  
- `web/cesium/layers/README.md` — declarative layer registry  
- `web/cesium/docs/integration-patterns.md` — how to integrate Cesium cleanly  
- `web/cesium/docs/governance-hooks.md` — FAIR+CARE + sovereignty enforcement patterns  

It is specifically about:

- **Production issues** and local dev failures involving Cesium scenes.  
- How to debug them **without violating governance** (no ad-hoc data dumps of sensitive layers).  
- How to encode fixes back into:
  - Config (`config/`),  
  - Layers (`layers/`),  
  - Docs (this file + others), and  
  - CI.

---

## 🧭 2. Triage Checklist (Quick Start)

When something is “wrong” in a Cesium view, first answer:

1. **Is this a performance issue, a rendering issue, or a data/governance issue?**  
2. **Does it happen in all browsers/devices or only some?**  
3. **Does it also affect MapLibre/2D views, or only Cesium?**  
4. **Is it reproducible with a minimal set of layers?**  
5. **Is telemetry available for the session/timeframe?**

Only then drill down into the sections below.

---

## 🚦 3. Performance Issues (Low FPS, Jank, Hangs)

### 3.1 Symptoms

- FPS drops below 20 when:
  - Multiple 3D Tilesets are visible.  
  - Time slider is scrubbed quickly.  
  - User zooms into dense regions (cities, heavy archaeology overlays).  

- UI feels “laggy”; map interactions respond slowly.  
- CPU and GPU usage spike in browser devtools.

### 3.2 Likely Causes

- Too many **heavy tilesets** active at once.  
- Overly aggressive **imagery + vector + 3D overlays** simultaneously.  
- H3 mosaics or polygons with too many features rendered at once.  
- Absence of throttling for debug layers or test tilesets.

### 3.3 Diagnostic Steps

1. **Layer toggling test**  
   - Disable all non-critical layers via dev feature flags or your layer control UI.  
   - Re-enable layers one by one to identify the heavy offender(s).

2. **Browser devtools**  
   - Measure FPS and memory via Performance tab.  
   - Check for excessive draw calls or GPU warnings in console.

3. **Telemetry check**  
   - Inspect `web-cesium-telemetry.json` for:
     - `frame_time_ms_*` metrics  
     - Per-layer or per-tileset telemetry tags (if present)

### 3.4 Remediation Patterns

- **Reduce active layers by default** in public mode:
  - Demote some layers to internal-only or `debug_only`.  

- **Tiered loading**:
  - Load critical tilesets immediately.  
  - Load non-critical tilesets **on demand** when zoomed in or when toggled.

- **Optimize layer definitions**:
  - Use `h3-only` for sensitive or dense overlays instead of polygons.  
  - Reduce symbol density or use clustering where appropriate.

- **Update `layers/*.json`**:
  - Add or refine a `"tier"` or `"perf_profile"` field for heavy layers.  
  - Use this to drive runtime throttling decisions.

Document outcomes and changes:

- In `web/cesium/docs/integration-patterns.md` (if a new pattern is adopted), and  
- In this file (if a recurring category of issues is discovered).

---

## 📦 4. Tileset & Imagery Issues (Tile Floods, 404s, Artifacts)

### 4.1 Symptoms

- Tiles fail to load; layers appear empty or partially loaded.  
- Console logs repeated `GET` failures or 404/500 errors.  
- Visual “holes”, flickering tiles, or misaligned terrain.

### 4.2 Likely Causes

- Incorrect or outdated **tileset URLs** in `layers/tilesets.json`.  
- Provider misconfiguration in `config/cesium-providers.json`.  
- Network/firewall changes or auth misconfiguration upstream.  
- Cesium Ion or self-hosted tile server outages.

### 4.3 Diagnostic Steps

1. **Console & Network tab**  
   - Look for repeated failed requests:
     - Check hostnames, paths, response codes.  

2. **Verify registry & config**  
   - Compare URLs in:
     - `web/cesium/layers/tilesets.json` → `url` / `provider_id`  
     - `web/cesium/config/cesium-providers.json`  

3. **Check environment overrides**  
   - Some providers may be configured per environment (dev/staging/prod).  
   - Verify environment variables or configuration files.

### 4.4 Remediation Patterns

- **Fix URLs / provider IDs** in registry and config.  
- **Add health checks** (CI or monitoring) that:
  - Test tile endpoints on pipeline runs or scheduled intervals.  

- **Fallback behavior**:
  - If a tileset is unreachable:
    - Hide that layer gracefully.  
    - Show a UI message indicating a partial scene (no full error dump).

- **Governance note**:
  - Do not log full URLs containing sensitive path elements or tokens to client-visible logs.

Once resolved, consider:

- Adding a brief “Tileset/Imagery Issues” entry in `troubleshooting.md` with conditions that triggered the bug.

---

## 🎥 5. Camera & Navigation Issues (Jumps, Flips, “Lost in Space”)

### 5.1 Symptoms

- Camera “jumps” unexpectedly after:
  - Syncing with MapLibre.  
  - Clicking a Story Node.  
  - Resetting view.  

- User appears to “leave the planet” (camera far away or inside the globe).  
- Sudden flips in heading/pitch after interactions.

### 5.2 Likely Causes

- Incorrect **coordinate conversion** between MapLibre and Cesium.  
- Height calculation errors (e.g., zoom-to-height mapping).  
- Race conditions in camera sync (2D/3D both updating each other).  
- Using an invalid bounding box (NaN or inverted lat/lon).

### 5.3 Diagnostic Steps

1. **Reproduce with minimal layers**  
   - Disable all heavy layers and debug camera flows alone.  

2. **Log camera state** (careful: no sensitive coordinates for public issues)  
   - Internally:
     - Log `lon`, `lat`, `height`, `heading`, `pitch`.  
   - Verify values are within normal ranges.

3. **Check sync logic** between MapLibre and Cesium:
   - Ensure only **one side** is authoritative at a time (see integration patterns doc).

### 5.4 Remediation Patterns

- Normalize camera sync:

  - Use the “2D primary” vs “3D primary” modes described in `integration-patterns.md`.  

- Clamp camera parameters:

  - Prevent heights below a minimum or above a maximum for default contexts.  
  - Enforce valid lat/lon ranges before calling `setView`.

- Add **guardrails**:

  - If camera enters invalid state, snap back to a safe default:
    - E.g., Kansas-centered overview at moderate zoom.

---

## 🎯 6. Picking & Interaction Issues

### 6.1 Symptoms

- Click/hover on objects produces **no response**.  
- Picks return unexpected objects or `undefined`.  
- Interactions feel inconsistent when multiple layers overlap.

### 6.2 Likely Causes

- Using synchronous `scene.pick` under heavy load (dropped picks).  
- Not mapping Cesium pick results back to **KFM objects** correctly.  
- Layer ordering / depth-test configuration causing unexpected primitives to be returned.  
- Governance filter aggressively redacting.

### 6.3 Diagnostic Steps

1. **Confirm async picking** is used:
   - Search codebase for `scene.pick(` in main-line code — this is discouraged.  
   - Ensure `scene.pickAsync` usage follows patterns in `integration-patterns.md`.

2. **Inspect layer configuration**:
   - Some layers may have `pickable: false` in custom options.  
   - Layer order might favor one type of primitive over another.

3. **Check governance filter**:
   - If the governance evaluation always flags `redact`, picks may appear to “do nothing”.

### 6.4 Remediation Patterns

- **Migrate to `scene.pickAsync`** and ensure all picks go through a **governance filter**.  
- Use a **priority system** in layer resolution to prefer certain types of features on pick.  
- Provide **visible feedback** when redaction occurs (e.g., a “redacted” chip).

---

## 🧱 7. Governance & CARE Violations (Sensitive Data Exposure)

### 7.1 Symptoms

- Sensitive archaeological sites or regions appear with **too much precision** in public mode.  
- Users report seeing locations or details that should be hidden.  
- External reviews flag 3D scenes as **overly revealing**.

### 7.2 Likely Causes

- Improper CARE configuration in `layers/regions.json` or `layers/tilesets.json`.  
- Bypass of governance hooks in integration code.  
- Use of **raw geometries** instead of generalized or H3-based representations.  
- Mode/role context not being applied (e.g., everything runs as `internal`).

### 7.3 Diagnostic Steps

1. **Immediate risk assessment**:
   - Identify which layers are affected and at what zoom levels.  
   - Determine whether data is already cached or screen-captured externally.

2. **Config/code review**:
   - Inspect affected layers in registries:
     - `care.sensitivity`  
     - `care.visibility_rules`  
   - Check enforcement logic in wrappers:
     - Are we calling `evaluateGovernanceForLayer` and `evaluateGovernanceForObject`?

3. **Check provenance**:
   - Confirm that generalization steps are documented and correct in PROV-O logs.

### 7.4 Remediation Patterns

1. **Immediate mitigation**:
   - Disable or heavily restrict the offending layers via config or feature flag.  
   - Redeploy UI with updated layer registry.

2. **Governance repairs**:
   - Correct `care.*` fields, visibility rules, and layer geometry sources.  
   - If necessary, regenerate generalized geometries or H3 mosaics.

3. **Audit & documentation**:
   - Log the incident in governance ledger.  
   - Add a brief description of the issue and the fix to this document (under a dedicated “Case Studies” section if needed).

Never use example screenshots of real sensitive data in this troubleshooting document; use synthetic or generalized representations only.

---

## 🧪 8. CI & Regression Hardening

To prevent repeat incidents:

- Ensure CI jobs for Cesium include:

  - **Schema checks** for `layers/*.json`.  
  - **Governance checks** for CARE & provenance consistency.  
  - **Snapshot tests** or **fixture-based tests** for:
    - Layer resolution by mode  
    - Governance filters for specific combos (region + role + zoom)

- When troubleshooting reveals a new failure mode:
  - Add a **regression test**:
    - In integration tests (e.g., Playwright/Cypress) where feasible.  
    - Or in a unit/integration harness that simulates layer resolution.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial Cesium troubleshooting playbook for KFM v11.2.3; documented performance, tileset, camera, picking, and governance-violation patterns with diagnostics and remediation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Troubleshooting Playbook & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Docs Hub](README.md) · [⬅ Back to Cesium Web Overview](../README.md) · [🛡️ Governance Hooks](./governance-hooks.md)

</div>