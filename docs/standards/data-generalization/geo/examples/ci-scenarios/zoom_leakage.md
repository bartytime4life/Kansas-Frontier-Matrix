---
title: "🧪 Kansas Frontier Matrix — Zoom-Leakage CI Scenario (Geo Generalization) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/data-generalization/geo/examples/ci-scenarios/zoom_leakage.md"

version: "v11.0.0"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "CI Scenario Example"
intent: "geo-sensitive-generalization-zoom-leakage"
semantic_document_id: "kfm-doc-geo-sensitive-generalization-zoom-leakage"
doc_uuid: "urn:kfm:docs:heritage:data-generalization-geo-ci-scenarios:zoom-leakage:v11.0.0"
event_source_id: "ledger:kfm:doc:heritage:data-generalization-geo-ci-scenarios:zoom-leakage:v11.0.0"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-generalization-geo-ci-zoom-leakage-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "geo-sensitive-data-generalization"
  applies_to:
    - "ci"
    - "ingest"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "maplibre"
    - "cesium"
    - "story-nodes"
    - "focus-mode"
    - "geoprivacy"
    - "archaeology"
    - "ecology"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I2-R3"
care_label: "Restricted / High-Sensitivity"
sensitivity: "Cultural, archaeological, ecological (high)"
sensitivity_level: "High"
public_exposure_risk: "High"
classification: "Restricted"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next geo-generalization CI examples revision"

provenance_chain:
  - "docs/standards/data-generalization/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/examples/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/examples/ci-scenarios/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

story_node_refs: []

ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Governance-Only"
ai_transform_permissions:
  - "summary"
  - "index-generation"
ai_transform_prohibited:
  - "content-alteration"
  - "sensitive-detail-expansion"
  - "governance-override"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - summary
    - index-generation
  prohibited:
    - content-alteration
    - sensitive-detail-expansion
    - governance-override
    - narrative-fabrication

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🧱 Architecture"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"
  - "sensitivity-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"
---

<div align="center">

# 🧪 **Zoom-Leakage CI Scenario (Geo Generalization)**  
`docs/standards/data-generalization/geo/examples/ci-scenarios/zoom_leakage.md`

**Purpose**  
Define CI scenarios that detect **zoom leakage**: cases where tile services, metadata, or frontend styles allow users to zoom beyond governance‑approved levels so that generalized regions (H3 cells, coarse polygons) look like precise point locations.  
If real KFM deployments are more “zoomed‑in” or visually precise than these scenarios permit, CI must fail before any sensitive layer is exposed.

</div>

---

## 📘 Overview

Zoom leakage happens when:

- A generalized spatial layer (e.g., H3 r5/r6, buffered region) is **technically coarse**, but  
- Tile endpoints or UI allow zooming far enough that:

  - Cell boundaries fill the viewport like a single parcel or building, or  
  - Icons/markers make a hex appear as a precise point, or  
  - Legends and styling imply exactness beyond what CARE governance allows.

This scenario pattern:

- Encodes **zoom, TMS, and styling constraints** for sensitive layers.  
- Specifies how CI should interpret **STAC asset zoom fields**, TMS definitions, and UI configuration.  
- Provides both **unsafe** and **corrected** examples for regression testing.

---

## 🧭 Context

This CI scenario is aligned with:

- 🏺 `docs/standards/data-generalization/README.md`  
  Sensitive Site & CARE governance.  

- 🗺️ `docs/standards/data-generalization/geo/README.md`  
  Geo generalization standard (H3 vs concealment, zoom caps).  

- 🛡️ `docs/standards/geospatial/geoprivacy-masking/README.md`  
  Donut masking + sensitivity‑radius mapping.  

- 🧱 `docs/standards/geo/tiling-and-pyramids.md`  
  COG + WebMercatorQuad, `minzoom`/`maxzoom` rules.  

- 🛰️ `docs/standards/geo/stac-geo-spec.md`  
  STAC 1.0 geo metadata, tile asset fields, and TMS semantics.  

Zoom leakage is primarily a **front‑of‑house risk**:

- It emerges at the interface between tile APIs and MapLibre/Cesium configuration.  
- It can occur **even if** STAC, CRS, and masking metadata are technically correct.

---

## 📦 Data & Metadata

### 1. Scenario definition (conceptual JSON)

A zoom‑leakage CI spec might look like:

```json
{
  "scenario_id": "geo-zoom-leakage-v11-basic",
  "description": "Test that a sensitive heritage H3 layer cannot be viewed at zoom levels that imply parcel- or structure-scale precision.",
  "sensitive_layer": {
    "id": "heritage_h3",
    "type": "h3_hex",
    "sensitivity_level": "L3",
    "h3_resolution": 5,
    "stac_asset": {
      "href": "https://tiles.example.org/heritage_h3/{z}/{x}/{y}.pbf",
      "type": "application/vnd.mapbox-vector-tile",
      "roles": ["tiles"],
      "tms": "WebMercatorQuad",
      "minzoom": 5,
      "maxzoom": 9
    }
  },
  "ui_config": {
    "maplibre_style_layer_id": "heritage_h3_layer",
    "minzoom": 5,
    "maxzoom": 9,
    "paint": {
      "fill-opacity": 0.5
    }
  },
  "rules": {
    "forbid_tiles_above_maxzoom": true,
    "forbid_ui_maxzoom_above_asset_maxzoom": true,
    "forbid_point_markers_for_hexes": true,
    "max_safe_pixels_per_hex_edge": 128
  },
  "expected_result": "fail_if_asset_or_ui_allows_zoom_leakage",
  "governance_ref": "council:decision:example-zoom-leakage"
}
```

Key rule ideas:

- **Tile service** MUST NOT serve tiles above the declared `maxzoom` in STAC.  
- **UI** MUST NOT set `maxzoom` higher than the STAC asset’s `maxzoom`.  
- **Hex edge size** in pixels at highest zoom must be below a threshold that visually suggests a single building / parcel.  
- **No icons**: sensitive hexes must be rendered as polygons, not point markers.

### 2. STAC tile asset snippet

For a compliant asset:

```json
"assets": {
  "heritage_h3_tiles": {
    "href": "https://tiles.example.org/heritage_h3/{z}/{x}/{y}.pbf",
    "type": "application/vnd.mapbox-vector-tile",
    "roles": ["tiles"],
    "tms": "WebMercatorQuad",
    "minzoom": 5,
    "maxzoom": 9,
    "tile_size": 256,
    "kfm:sensitivity_level": "L3",
    "kfm:h3_resolution": 5,
    "kfm:layer_visibility": "restricted"
  }
}
```

CI must verify that:

- The tile server **behaves** consistently with these values (no tiles at z > 9).  
- The UI honors or is stricter than these zoom limits.

---

## 🧱 Architecture

### 1. Zoom-leakage analysis flow

```mermaid
flowchart LR
    A[Load zoom-leakage scenario spec] --> B[Inspect STAC assets<br/>minzoom/maxzoom/tms]
    B --> C[Test tile endpoint behavior<br/>via synthetic tile requests]
    C --> D[Inspect UI config<br/>MapLibre/Cesium style & layer zooms]
    D --> E[Estimate visual precision<br/>hex size vs screen size]
    E --> F{Leakage detected?}
    F -->|No| G[Scenario passes<br/>zoom behavior acceptable]
    F -->|Yes| X[Scenario fails<br/>tighten zoom caps or generalization]
```

Checks include:

1. **STAC vs Tile Service**  

   - For a set of zooms (`z_test > maxzoom`), CI issues requests like:  
     `https://tiles.example.org/heritage_h3/{z}/{x}/{y}.pbf`  

   - Expected behavior:  

     - HTTP `404` / `410` / explicit error for out‑of‑range zooms, **not** a valid tile.  
     - No silent fallback to “closest available zoom” that still returns data.

2. **STAC vs UI**  

   - UI `maxzoom` for the sensitive layer must be:  

     - ≤ asset `maxzoom`, and  
     - ≤ a **governance‑defined** maximum for that sensitivity level (e.g., L3 capped at z9 or z10).

3. **Visual precision estimate**  

   - Approximate edge length (in pixels) of an H3 hex or generalized polygon at `maxzoom` on common viewport sizes.  
   - If hexes span most of the viewport and align tightly with visible land parcels / structures, the layer may **appear** more precise than allowed.  
   - This does not need to be precise physics; a conservative heuristic is sufficient for CI.

4. **Style semantics**  

   - Check that the layer uses polygon fills, not icons/circles.  
   - Point markers on hex centroids at high zoom levels are treated as **leakage** because they visually imply a point location.

---

## 🧪 Validation & CI/CD

This scenario supports a CI job such as:

- `geo-zoom-leakage-check.yml`

Suggested steps:

1. Load `zoom_leakage` scenario spec (YAML/JSON fixture).  
2. Parse referenced STAC Item / Collection for the sensitive layer.  
3. Execute **synthetic tile requests** to the declared `href` for:

   - `z = minzoom - 1` (below minimum).  
   - `z = maxzoom` (expected OK).  
   - `z = maxzoom + 1` (must not return sensitive data).  

4. Inspect frontend configuration (style JSON where stored) to ensure:

   - `minzoom`/`maxzoom` are within allowed range for the sensitivity level.  
   - No icon‑based representation for hexes at high zoom.  

5. Optionally run a geometric heuristic:

   - For a typical viewport, estimate hex edge size (in px) at `maxzoom`.  
   - If edge size exceeds `max_safe_pixels_per_hex_edge`, flag as potential leakage (requires governance tuning).

CI should treat **both** of the following as required sanity checks:

- A **known bad fixture** (e.g., responding at z=14 when `maxzoom=9`) must **fail**.  
- A **known corrected fixture** (tile service + UI both capped at 9) must **pass**.

A PR is **blocked** if:

- Any sensitive layer under test can be successfully requested at a zoom beyond its STAC `maxzoom`.  
- UI config exposes a sensitive layer at a zoom beyond its allowed range.  
- Style semantics turn generalized regions into point‑like markers at high zoom.

Telemetry for this CI job may track:

- Number of tile endpoints tested.  
- Count of endpoints that attempted to serve above `maxzoom`.  
- Distribution of `maxzoom` by sensitivity level.  
- Counts of style violations (markers vs polygons).

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                                                                                        |
|--------:|------------|-------------------|----------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-12-06 | Active / Enforced | Initial zoom‑leakage CI scenario for geo generalization; defines tile/zoom/style checks for sensitive layers. |

---

<div align="center">

🧪 **KFM v11 — Zoom-Leakage CI Scenario (Geo Generalization)**  
“If the map lets you zoom too far in, the test must zoom out the deployment.”

CC‑BY‑NC 4.0 · FAIR+CARE Council · MCP‑DL v6.3  

[⬅ Back to CI Scenario Index](README.md) · [🗺 Geo Generalization Standard](../../README.md) · [⚖ Governance](../../../../governance/ROOT-GOVERNANCE.md)

</div>

