---
title: "🧩 KFM v11.2.3 — Cesium Integration Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed integration patterns for wiring CesiumJS into the Kansas Frontier Matrix (KFM) web stack, including React components, MapLibre dual-view, Focus Mode, Story Nodes, and async picking."
path: "web/cesium/docs/integration-patterns.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 integration-patterns compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:web-cesium-integration-patterns-v11.2.3"
semantic_document_id: "kfm-web-cesium-integration-patterns-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:docs:integration-patterns:v11.2.3"

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

doc_kind: "Subsystem Integration Patterns"
intent: "web-cesium-integration-patterns"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "TechArticle"
  cidoc: "E73 Information Object"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/web-cesium-integration-patterns-v1.json"
shape_schema_ref: "../../schemas/shacl/web-cesium-integration-patterns-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded on next major Cesium integration pattern revision"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Cesium Integration Patterns**  
`web/cesium/docs/integration-patterns.md`

**Purpose:**  
Provide **governed, repeatable patterns** for using **CesiumJS** in the KFM web stack:

- React + TypeScript wrapper components  
- MapLibre ↔ Cesium dual-view synchronization  
- Focus Mode & Story Node bindings  
- Async picking (`scene.pickAsync`) and governance-aware interactions  
- Performance and reliability patterns under FAIR+CARE & sovereignty constraints

</div>

---

## 📘 1. Scope & Relationships

This document is the **implementation playbook** that complements:

- `web/cesium/README.md` — subsystem overview  
- `web/cesium/layers/README.md` — declarative layer registry  
- `web/cesium/docs/governance-hooks.md` — FAIR+CARE + sovereignty enforcement  
- `web/cesium/docs/troubleshooting.md` — incident & remediation patterns  

It describes **how** to use Cesium in KFM:

- Which abstractions to use (and avoid)  
- How to wire data & layers into React components  
- How to keep interactions **governed, testable, and reproducible**

---

## 🧱 2. Core Architecture Pattern

### 2.1 Wrapper-First Principle

**Rule:**  
KFM code **must not** talk directly to raw Cesium `Viewer` / `Scene` from arbitrary React components.

Instead:

- Use dedicated wrappers in `web/cesium/components/`, e.g.:

  - `CesiumGlobe.tsx`  
  - `CesiumTimelineScene.tsx`  
  - `CesiumRegionOverlay.tsx`  

- Expose **declarative props** for layers, modes, and interactions, backed by:

  - Layer registries (`web/cesium/layers/*.json`)  
  - Governance-aware utility modules  
  - Shared context/hooks (e.g., `FocusModeContext`, `StoryNodeContext`)

### 2.2 Recommended Component Shape

A typical wrapper looks like:

- One **root React component** that owns the Cesium `Viewer` and `Scene`.  
- Subcomponents or hooks that:
  - Attach/detach layers  
  - Manage camera state  
  - Register event handlers (picks, mouse move, etc.)

High-level TypeScript shape:

~~~ts
type CesiumGlobeProps = {
  mode: "public" | "internal" | "review";
  layers: CesiumLayerConfig[]; // Derived from web/cesium/layers/*.json
  onPick?: (hit: GovernanceAwarePickResult) => void;
};

export function CesiumGlobe(props: CesiumGlobeProps) {
  // 1. Initialize Viewer once
  // 2. Attach layers using registry + governance hooks
  // 3. Wire async pick, camera sync, telemetry instrumentation
}
~~~

---

## ⚛️ 3. React Integration Patterns

### 3.1 Viewer Lifecycle (React-Friendly)

Pattern:

1. **Create Cesium Viewer** in a `useEffect` with **ref** to container div.  
2. Store viewer reference in `useRef`, **not** in React state.  
3. Clean up on unmount (destroy viewer, stop any loops).

Conceptual snippet:

~~~ts
function useCesiumViewer(containerRef: React.RefObject<HTMLDivElement>) {
  const viewerRef = React.useRef<Cesium.Viewer | null>(null);

  React.useEffect(() => {
    if (!containerRef.current || viewerRef.current) return;

    viewerRef.current = new Cesium.Viewer(containerRef.current, {
      // governed, opinionated defaults
      animation: false,
      timeline: false,
      geocoder: false,
      baseLayerPicker: false
    });

    return () => {
      viewerRef.current?.destroy();
      viewerRef.current = null;
    };
  }, [containerRef]);

  return viewerRef;
}
~~~

**Do:**

- Centralize Cesium initialization in **one hook** or wrapper per view.  

**Don’t:**

- Create multiple `Viewer` instances per mount unless intentionally isolated.  
- Store `Viewer` in Redux/Global state.

---

### 3.2 Hook-Based Layer Attachment

Wrap layer operations in hooks that:

- Accept **governance-resolved** layer configs.  
- Attach/detach primitives when configs change.  
- Use `useEffect` keyed by layer ID.

Conceptual pattern:

~~~ts
function useCesiumLayers(viewer: Cesium.Viewer | null, layers: CesiumLayerConfig[]) {
  React.useEffect(() => {
    if (!viewer) return;
    const scene = viewer.scene;

    const handles = layers.map(layer =>
      attachGovernedLayer(scene, layer) // resolves registry + governance hooks
    );

    return () => {
      handles.forEach(h => h.detach());
    };
  }, [viewer, JSON.stringify(layers)]); // or more targeted deps
}
~~~

**Key point:**  
Layer attachment must invoke **governance logic** (as described in `governance-hooks.md`) before creating primitives.

---

## 🗺️ 4. MapLibre ↔ Cesium Dual-View Patterns

KFM uses **MapLibre (2D)** and **Cesium (3D)** together:

- Side-by-side views  
- Mode switch (2D ↔ 3D)  
- Shared camera and extent when appropriate

### 4.1 Camera Sync Strategy

Treat **MapLibre** as “2D camera”, **Cesium** as “3D camera” over same planet:

1. Define a shared camera state:

~~~ts
type SharedCameraState = {
  center: { lon: number; lat: number };
  zoom: number;      // 2D zoom equivalent
  heading: number;   // bearing
  pitch: number;     // tilt
};
~~~

2. Expose updaters:

- `onMapLibreCameraChange(state)`  
- `onCesiumCameraChange(state)`

3. Decide which view is **authoritative** at any time (to avoid feedback loops):

- When in “2D primary” mode:
  - MapLibre drives state.  
  - Cesium consumes and aligns camera accordingly.

- When in “3D primary” mode:
  - Cesium drives state.  
  - MapLibre consumes, or may be minimized.

Simple pattern:

~~~ts
function syncCesiumToCamera(viewer, shared: SharedCameraState) {
  const { center, zoom, heading, pitch } = shared;
  const destination = Cesium.Cartesian3.fromDegrees(center.lon, center.lat, zoomToHeight(zoom));
  viewer.camera.setView({
    destination,
    orientation: {
      heading: Cesium.Math.toRadians(heading),
      pitch: Cesium.Math.toRadians(pitch),
      roll: 0.0
    }
  });
}
~~~

### 4.2 Governance Hooks in Dual-View

- If a layer is **restricted to 3D** (e.g., 3D Tiles for internal-only use), ensure 2D view never shows equivalent detail.  
- If 2D is in **public mode**, Cesium must not render any layer that violates public-mode CARE constraints (even when hidden in UI).

---

## 🧠 5. Focus Mode & Story Node Binding Patterns

Story Nodes + Focus Mode drive most high-value interactions.

### 5.1 Story Node → Layer Activation

Pattern:

- Each Story Node references **semantic IDs** (datasets, regions, scenes).  
- A mapping layer resolves these IDs to **Cesium layer IDs** in `layers/*.json`.  
- Focus Mode passes a computed `layers[]` prop into `CesiumTimelineScene`.

Flow:

1. Story Node active → compute `activeDataIds`.  
2. Resolve `activeDataIds` → `CesiumLayerConfig[]` using registry and governance logic.  
3. Render `CesiumTimelineScene` with these layers.

Conceptual snippet:

~~~ts
const layers = React.useMemo(
  () => resolveLayersForStoryNode(storyNode, cesiumLayerRegistry, governanceContext),
  [storyNode, cesiumLayerRegistry, governanceContext]
);

return <CesiumTimelineScene mode={mode} layers={layers} onPick={handlePick} />;
~~~

### 5.2 Timeline-Linked Scenes

Pattern:

- Focus Mode time slider drives a **global time context**.  
- Cesium scene subscribes to `time` and sets Cesium’s clock / entity availability.

Pseudo-logic:

~~~ts
function useCesiumTimeSync(viewer: Cesium.Viewer | null, currentTime: Date) {
  React.useEffect(() => {
    if (!viewer) return;
    viewer.clock.currentTime = Cesium.JulianDate.fromDate(currentTime);
  }, [viewer, currentTime]);
}
~~~

Layers drawing time-sensitive data:

- Should use Cesium constructs that respect the `Viewer.clock` (e.g., sampled properties, time-dynamic primitives), or  
- Should be explicitly toggled per time step using React-driven updates.

---

## 🔍 6. Async Picking Integration Patterns

Async picking is **mandatory** for heavy scenes; synchronous `pick` is discouraged.

### 6.1 Basic Pattern

~~~ts
async function handleSceneClick(
  scene: Cesium.Scene,
  windowPosition: Cesium.Cartesian2,
  context: GovernanceContext
) {
  const picked = await scene.pickAsync(windowPosition);
  if (!picked) return;

  const kfmObject = mapPickedToKfmObject(picked);
  if (!kfmObject) return;

  const policy = evaluateGovernanceForObject(kfmObject, context);

  if (policy.redact) {
    showRedactedChip(policy.reason);
    return;
  }

  showProvenanceChip({
    label: kfmObject.label,
    sensitivity: policy.sensitivity,
    provenanceRef: kfmObject.provenanceRef
  });
}
~~~

### 6.2 Cancellation & Debounce

In interactive contexts (e.g., hover), debounce picking and allow cancellation:

- Use a **token** or `AbortController`-style pattern to cancel in-flight picks when a new event arrives.  
- Avoid multiple overlapping picks for the same frame.

---

## 📊 7. Performance & Reliability Patterns

### 7.1 Layer Throttling

Patterns to avoid overload:

- Limit **number of active heavy layers** (tilesets, dynamic imagery).  
- Use a **priority** or **tier** system in registries:
  - `tier: "critical" | "important" | "nice-to-have"`  

Cesium wrapper can:

- Ensure only a subset of `nice-to-have` layers is active when FPS drops.  
- Disable expensive debug overlays automatically in public modes.

### 7.2 Telemetry-Informed Adjustments

Use `web-cesium-telemetry.json` metrics to:

- Adjust default layer sets in `public` vs `internal` mode.  
- Change initial camera and zoom for performance-critical scenes.  
- Flag particularly heavy tilesets for redesign or tiling improvements.

---

## ✅ 8. Do / Don’t Summary

**Do:**

- Use **React wrappers + hooks** as the only way to manage Cesium viewers.  
- Drive layers solely via **registry + governance** data.  
- Use **`scene.pickAsync`** for interactions.  
- Respect CARE + sovereignty rules in all visual and interactive patterns.  
- Write tests around integration patterns (especially for Story Node & Focus Mode flows).

**Don’t:**

- Bypass governance checks by directly instantiating primitives in arbitrary components.  
- Use raw Cesium `scene.pick` in mainline paths.  
- Hard-code URLs or dataset IDs in components.  
- Show precise site geometries or sensitive regions in public mode without explicit governance overrides.  
- Couple Cesium tightly to Redux/global state without clear boundaries.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial Cesium integration pattern guide for KFM v11.2.3; defined wrapper-first, dual-view, Focus Mode, async picking, and performance patterns aligned with governance hooks. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Integration Patterns & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Docs Hub](README.md) · [⬅ Back to Cesium Web Overview](../README.md) · [📜 Governance Hooks](./governance-hooks.md)

</div>