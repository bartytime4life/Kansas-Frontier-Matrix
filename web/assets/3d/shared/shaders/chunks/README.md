---
title: "KFM 3D Shader Chunks 🧩"
path: "web/assets/3d/shared/shaders/chunks/README.md"
version: "v0.1.0"
last_updated: "2026-01-25"
status: "active"
doc_kind: "Developer Guide"
license: "MIT"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
doc_uuid: "urn:kfm:doc:web:3d:shaders:chunks:v0.1.0"
commit_sha: "<fill-on-merge>"
doc_integrity_checksum: "sha256:<fill-on-merge>"
---

# 🧩 Shader Chunks (GLSL) — KFM 3D Shared Library

![GLSL](https://img.shields.io/badge/GLSL-shader%20snippets-informational)
![WebGL](https://img.shields.io/badge/WebGL-1%20%2F%202-informational)
![Cesium](https://img.shields.io/badge/CesiumJS-3D%20Globe%20%26%20Terrain-blue)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20Map%20Viewer-blue)
![KFM](https://img.shields.io/badge/KFM-provenance--first%20visuals-brightgreen)

Reusable GLSL “chunks” (small, composable snippets) used to assemble **vertex** and **fragment** shaders for Kansas Frontier Matrix (KFM) 3D rendering.

The goal is **consistency + reuse + trust**:
- ✅ **Consistent look & behavior** across 3D layers, story steps, and time playback  
- ✅ **Single source of truth** for common math, lighting, colormaps, fog, picking, and debug overlays  
- ✅ **Performance-friendly** building blocks (especially important because 3D is opt‑in and should degrade gracefully)  
- ✅ **Provenance-friendly visuals**: shaders should make it easy for the UI to keep “the map behind the map” visible (legends, IDs, metadata hooks) 🔍

---

## 📘 Overview

### What is a “shader chunk”?
A shader chunk is a **partial GLSL file** that contributes one of:
- functions (`float kfm_saturate(float x)`)
- structs
- uniforms/varyings declarations (sparingly)
- small reusable blocks (e.g., color ramps, noise, depth decoding)

Chunks **do not** contain `main()` (or engine-specific main entrypoints). They’re *assembled* into full shaders.

### Why does KFM need this?
KFM blends:
- 🗺️ **2D maps** (MapLibre)
- 🌍 **3D globe/terrain** (Cesium / 3D Tiles)
- ⏱️ **Time playback** + story-driven camera/layer changes
- 🧠 **Explainable AI + provenance panels**

That means our rendering needs **repeatable, auditable visual logic**: the same “drought index ramp” or “highlight selected feature” behavior should not drift across layers or demos.

---

## 🗂️ Directory Layout

You are here 👇

```txt
📁 web/
  📁 assets/
    📁 3d/
      📁 shared/
        📁 shaders/
          📁 chunks/
            📄 README.md      👈 this doc
            🧩 *.glsl         (chunk files live here)
```

> Tip 💡: Keep chunks **small** and **single-purpose**. If it feels like a whole shader… it probably is.

---

## 🧠 Core Concepts & Vocabulary

| Term | Meaning |
|---|---|
| **Chunk** 🧩 | A reusable GLSL snippet used by many shaders |
| **Assembler** 🧵 | A build/runtime step that expands includes + injects defines |
| **Pass** 🎨 | A render pass (color, picking, depth, outline, debug) |
| **Picking** 🖱️ | Rendering IDs so the UI can map a pixel → feature/entity |
| **Space** 🧭 | Coordinate system (model, world, view, clip; sometimes ECEF/local) |
| **Time uniform** ⏱️ | Shader inputs that change with KFM timeline/story playback |

---

## 🚀 Using Chunks

### Include mechanism (convention)
GLSL doesn’t support `#include` natively, so we treat it as a **preprocessor directive**.

**Recommended include style (Three.js-ish):**
```glsl
// Vertex shader source (assembled)
#include <kfm_precision>
#include <kfm_math>
#include <kfm_geo>
#include <kfm_project>

void main() {
  // ...
}
```

**Alternative include style (explicit path):**
```glsl
#include "chunks/kfm_math.glsl"
```

Either convention is fine **as long as the assembler supports it**.

---

### Minimal “shader assembler” concept (TypeScript-ish) 🧰

> This is illustrative; adapt to your bundler + runtime.

```ts
/**
 * assembleShader(source, chunkMap) replaces #include directives with chunk strings.
 * Keep this deterministic: same inputs => same output.
 */
export function assembleShader(
  source: string,
  chunkMap: Record<string, string>
): string {
  return source.replace(/#include\s+<([^>]+)>/g, (_, key: string) => {
    const chunk = chunkMap[key.trim()];
    if (!chunk) throw new Error(`Missing shader chunk: ${key}`);
    return `\n// ---- BEGIN CHUNK: ${key} ----\n${chunk}\n// ---- END CHUNK: ${key} ----\n`;
  });
}
```

---

## 🧩 Chunk Authoring Rules (KFM Standard)

### 1) Namespacing (avoid collisions) 🧷
- Prefix public functions/types with `kfm_`
- Prefer `kfmCamelCase` for functions and `KFM_*` for compile-time flags

✅ Good:
```glsl
float kfm_saturate(float x) { return clamp(x, 0.0, 1.0); }
```

❌ Risky:
```glsl
float saturate(float x) { return clamp(x, 0.0, 1.0); } // may collide
```

---

### 2) Chunk header block (required) 🧾
Every chunk should begin with a short comment header so it’s easy to audit.

```glsl
/**
 * kfm_colormap_viridis.glsl
 * Purpose: map scalar -> RGB using Viridis-like ramp.
 * Stage: fragment (recommended), but may be used in vertex too.
 * Inputs: scalar in [0..1]
 * Outputs: vec3 color in linear space
 * Notes: keep deterministic; avoid texture fetch unless necessary.
 */
```

---

### 3) Be explicit about coordinate space 🧭
If a chunk touches positions/normals, it **must** state what space it expects.

Examples:
- `kfm_worldPos` (world/ECEF/local tangent)  
- `kfm_viewPos` (camera/view space)  
- `kfm_clipPos` (clip space)  

> A huge class of “3D bugs” is really “space mismatch.”

---

### 4) Avoid global side effects 🧼
Chunks should not:
- declare `main()`
- mutate global state in surprising ways
- redefine engine-provided symbols

If you need a “hook” pattern, use clearly named functions:
- `kfm_applyFog(inout vec4 color, ...)`
- `kfm_applySelectionHighlight(inout vec4 color, ...)`

---

## 🎛️ Precision & Compatibility

### WebGL 1 vs WebGL 2
If you support both:
- Prefer macros to smooth over `attribute/varying` vs `in/out`
- Keep precision declarations centralized in a `kfm_precision` chunk

Example idea:
```glsl
#ifdef GL_ES
precision highp float;
precision highp int;
#endif
```

> Mobile can be picky. Assume “works on desktop” ≠ “works in field mode” 📱

---

## 🖱️ Picking & UI Trust Hooks

KFM’s UI relies on clicking/selecting features to show:
- metadata
- legends
- provenance and source attribution
- sensitivity warnings / governance context

Shader chunks often support this with:
- ID encoding/decoding helpers
- consistent highlight rules for “selected/hovered”
- debug overlays (depth/normal visualization)

### Picking rule of thumb
- Picking must be **stable** across frames and camera moves.
- IDs should be mapped to UI entities (dataset row / graph node / feature id).
- For sensitive layers: **never rely on a shader alone** for redaction. Shaders can *display* a mask, but access control must happen upstream. 🔒

---

## ⏱️ Time & Story Playback Support

KFM treats time as first-class (timeline slider, story steps). Shaders should support time-driven transitions **without duplicating logic**.

Recommended uniforms (if used):
- `uniform float u_kfmTime;` (seconds or normalized story time)
- `uniform float u_kfmTimelineT;` (0..1 normalized across user-selected range)
- `uniform float u_kfmFade;` (transition control for story step fades)

Keep time logic in reusable chunks:
- `kfm_time.glsl`
- `kfm_easing.glsl`
- `kfm_transition_fade.glsl`

---

## ⚡ Performance Guidelines (GPU Reality Check)

Keep chunks fast:
- ✅ prefer arithmetic over branches
- ✅ avoid loops with non-constant bounds
- ✅ avoid expensive trig in fragment unless essential
- ✅ minimize varyings (bandwidth matters)
- ✅ use texture lookups strategically (cache-friendly)
- ✅ prefer compile-time flags over runtime `if`

> If a chunk adds a new uniform/varying, ask: “Can we derive this cheaper?” 🧠

---

## 🧪 Testing & CI Ideas

Even “small” shader changes can break at runtime. Good practice:
- compile checks for all assembled shaders
- snapshot tests for key scenes (golden images)
- lint / format rules (even if minimal)

Suggested checks (optional but strong):
- ✅ “assemble + compile” every shader in CI
- ✅ validate chunk headers + naming conventions
- ✅ ensure no chunk introduces forbidden symbols or banned extensions

---

## ✅ Definition of Done (new chunk PR)

- [ ] Chunk has required header comment 🧾  
- [ ] Functions/types are namespaced (`kfm_*`) 🧷  
- [ ] Space assumptions documented (world/view/clip) 🧭  
- [ ] No `main()` added, no surprising globals 🧼  
- [ ] Works in WebGL1/2 (or clearly labeled) 🎛️  
- [ ] Tested in at least one real scene (plus picking if relevant) 🖱️  
- [ ] Does not reduce performance noticeably (or includes justification) ⚡  
- [ ] Any third-party code includes license/attribution 📜  

---

## 🧰 Troubleshooting (quick hits)

<details>
<summary>🧯 Shader fails to compile only on mobile</summary>

Common causes:
- missing precision qualifiers
- too many varyings
- using `highp` where not supported for fragment on some devices
- relying on WebGL2-only features without guards

Try:
- centralize `precision` in one chunk
- reduce varyings (pack values, use fewer interpolants)
- add compile-time feature flags

</details>

<details>
<summary>🧭 “Everything renders but appears in the wrong place”</summary>

Almost always a space/CRS mismatch:
- lon/lat vs projected meters
- world space vs view space
- Cesium ECEF vs local tangent vs model space

Fix:
- ensure chunks state expected space
- convert once and pass consistently

</details>

<details>
<summary>🖱️ Picking selects the wrong feature</summary>

Typical issues:
- ID encoding mismatch (CPU vs GPU)
- precision loss when packing IDs into floats
- post-processing altering the picking buffer

Fix:
- use a dedicated picking pass with no post FX
- prefer integer-safe packing (RGBA8) when possible

</details>

---

## 📚 Project References (context used to shape this folder)

These project docs inform shader chunk standards and why we care about provenance, UI trust, and cross‑mode (2D/3D/AR) rendering:

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf**
- 🏗️ **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf**
- 🧭 **Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview.pdf**
- 📥 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf**
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf**
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf**
- 🧠 **Additional Project Ideas.pdf**

Reference libraries (PDF portfolios; useful for deeper dives):
- 🤖 **AI Concepts & more.pdf** (AI library)
- 🌍 **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf** (WebGL + mapping + visualization)
- 🧰 **Various programming langurages & resources 1.pdf** (language/tooling library)
- 🗃️ **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf** (data + CI/CD + architecture library)

---

## 🧭 Next Steps (nice upgrades)

- 🧾 Add an auto-generated `CHUNK_INDEX.md` (scan chunks → table of exported symbols + stage)
- 🧵 Add a deterministic shader build manifest (hash assembled shaders for debugging)
- 🧪 Add CI compile checks for “all shader variants”
- 🎛️ Add a standard feature-flag matrix (`KFM_USE_FOG`, `KFM_USE_PICKING`, etc.)

---

