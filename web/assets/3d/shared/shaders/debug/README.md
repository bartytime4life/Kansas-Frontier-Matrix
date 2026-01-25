# 🐞 Debug Shaders (KFM 3D)  
![Scope](https://img.shields.io/badge/scope-web%2Fassets%2F3d%2Fshared%2Fshaders%2Fdebug-blue)
![GLSL](https://img.shields.io/badge/GLSL-WebGL%20Shaders-orange)
![Viewer](https://img.shields.io/badge/viewer-3D%20(globe%20%2B%20terrain)-6f42c1)
![Intent](https://img.shields.io/badge/intent-observability%20%26%20QA-brightgreen)
![Safety](https://img.shields.io/badge/safety-dev--only%20toggle-important)

> [!WARNING]
> **This folder is for developer diagnostics only.**  
> Debug shaders can accidentally reveal sensitive geometry/textures or “hidden” layer meaning. Keep them behind **feature flags**, **role gates**, and **non-prod builds**.

---

## 🎯 What lives here?

This directory contains **GLSL shader programs/snippets** used to render **diagnostic views** for KFM’s 3D stack:
- normals, tangents, and UV sanity checks 🧵
- depth/linear depth bands 🕳️
- world position / coordinate-space verification 🌍
- tile boundaries / LOD hints 🧱
- overdraw & performance heatmaps 🔥
- picking/ID debug (what object did we click?) 🖱️

The intent is to make the “**map behind the map**” visible at the GPU layer: *why it looks the way it does, where it’s wrong, and what data/mesh is involved.*

---

## 🧭 Where this fits in the repo

```text
web/
└─ 📁 assets/
   └─ 🧊 3d/
      └─ 🧰 shared/
         └─ 🧬 shaders/
            ├─ 🧩 common/                 # 🧩 Shared shader utilities (math, color ramps, noise, coordinate helpers)
            └─ 🐞 debug/                  # 🐞 Diagnostic materials (normals/depth/IDs) for QA and dev-only tooling
               ├─ 📄 README.md            # ← you are here 📌 What debug shaders exist, how to enable them, and safety notes
               └─ 🧾 *.glsl / *.vert / *.frag # Debug shader files (keep small, documented, and consistent uniforms)
```

> [!TIP]
> Keep debug shaders **pure** and **portable**: they should not depend on app state beyond uniforms and varyings.

---

## 🧪 Debug view catalog (recommended)

> These are *recommended* passes; your engine/tileset may implement a subset.

| Pass 🧷 | Output | Best for diagnosing | Typical “oh no” symptom |
|---|---|---|---|
| **Normals** | RGB = normal | wrong lighting, normal matrix issues | lighting flips / seams / “inside out” |
| **Tangents/Bitangents** | RGB axes | normal mapping correctness | normal maps look rotated |
| **UV Checker** | UV grid / color bands | UV unwrap / texture addressing | stretched textures, mirrored UVs |
| **Depth (raw)** | depth buffer | z-fighting, precision | flicker on coplanar surfaces |
| **Linear Depth** | meters → ramp | scale issues, clipping | near plane too close / far plane too far |
| **World Position** | XYZ → RGB | coordinate-space bugs | model “teleports” in globe |
| **Wireframe Overlay** | edges | topology / LOD stitching | cracks at tile borders |
| **Tile/Feature ID** | stable color per id | picking, batching, instancing | clicks select the wrong thing |
| **Overdraw Heatmap** | additive intensity | fill-rate, transparency | perf drops when rotating camera |
| **LOD / Geometric Error** | ramp per LOD | streaming + refinement | tiles pop / shimmer unexpectedly |
| **Classification / Confidence** | ramp per scalar | AI-driven layers, uncertainty | “model says it’s certain… but isn’t” |

---

## 🧱 Shader interface contract (recommended)

Because KFM mixes geospatial stacks (2D + 3D) and may swap render backends over time, debug shaders should follow a **stable contract**.

### 1) File naming

Pick one convention and stick to it across `shared/shaders`:

- `debug_<pass>.vert.glsl`
- `debug_<pass>.frag.glsl`

Examples:
- `debug_normals.frag.glsl`
- `debug_linear_depth.frag.glsl`
- `debug_wireframe_overlay.frag.glsl`

### 2) Version + precision

Prefer WebGL2 / GLSL ES 3.0 when possible:

```glsl
#version 300 es
precision highp float;
precision highp int;
```

> [!NOTE]
> If the host engine is WebGL1 (GLSL ES 1.0), drop `#version 300 es` and use `varying`/`attribute`.  
> **Don’t** silently mix versions in one shader.

### 3) Coordinate spaces (keep them explicit)

Use explicit naming in varyings/uniforms:
- `v_posWorld`, `v_posView`
- `v_normalWorld`, `v_normalView`
- `u_model`, `u_view`, `u_proj`, `u_modelView`, `u_modelViewProj`
- `u_normalMatrix` (mat3)

> [!TIP]
> In geospatial 3D, “world” might be **ECEF**, not a local ENU frame. If you need local frames, make it obvious in naming: `v_posECEF`, `v_posENU`.

### 4) Deterministic outputs (important for QA)

Debug shaders should be **deterministic** so they can be snapshot-tested:
- ❌ avoid time-based noise unless explicitly requested
- ✅ if you need pseudo-randomness, hash **stable IDs** (tile id, feature id, vertex id)

---

## 🔐 Safety & governance rules (non-negotiable)

KFM’s broader design emphasizes **data governance**, **sensitivity tiers**, and **transparent evidence**. Debug modes must not bypass those safeguards.

### Rules ✅
- **Never** introduce a debug shader that reveals restricted textures/attributes by default.
- Gate debug views behind **dev-only UI**, **env flags**, and/or **role checks**.
- When a dataset is generalized/redacted in the UI, debug passes must respect that decision:
  - e.g., if a sensitive site is shown as a generalized polygon, don’t provide a debug view that restores the exact point.

### Good patterns 👍
- “Debug overlays” that show *render state* (LOD, tile edges, depth) without exposing sensitive payloads.
- “Provenance overlays” that show *dataset id/version* rather than raw coordinates.

---

## 🧰 How these shaders are usually consumed

This folder is in `web/assets`, so the most common patterns are:

### Pattern A: import shader text at build-time
<details>
<summary>Example (Vite-style <code>?raw</code> import)</summary>

```ts
import fragNormals from "@/assets/3d/shared/shaders/debug/debug_normals.frag.glsl?raw";
import vertBasic from "@/assets/3d/shared/shaders/common/basic.vert.glsl?raw";

const program = createProgram(gl, vertBasic, fragNormals);
```
</details>

### Pattern B: fetch shader text at runtime
<details>
<summary>Example (runtime fetch)</summary>

```ts
async function loadShader(url: string) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Shader load failed: ${url}`);
  return await res.text();
}
```
</details>

### Pattern C: engine-specific “custom shader” API
If the 3D engine offers a custom shader hook, keep debug shaders in a **thin adapter layer**:
- adapter sets uniforms
- adapter maps engine varyings → our contract
- debug shader stays clean and reusable

---

## 🧪 Adding a new debug shader (checklist)

### ✅ Authoring checklist
- [ ] Shader name starts with `debug_`
- [ ] Declares required precision / version
- [ ] Has clear comments: **what it visualizes** and **what inputs it needs**
- [ ] Works with missing attributes (graceful fallback when possible)
- [ ] Deterministic output (or explicitly marked as non-deterministic)
- [ ] Doesn’t leak restricted/sensitive data
- [ ] Added to the debug shader “registry” in code (wherever your viewer enumerates passes)
- [ ] Snapshot image(s) captured for regression testing (optional but recommended)

### 📝 Minimal header comment template
```glsl
// debug_normals.frag.glsl
// Purpose: visualize per-fragment normals (RGB = N in world space)
// Requires: v_normalWorld
// Notes: deterministic, safe for non-sensitive geometry
```

---

## 🧯 Troubleshooting cheat-sheet

### “Everything is black”
- precision too low (try `highp`)
- missing varyings (verify pipeline writes what shader reads)
- output is NaN (clamp/guard divisions)

### “Normals look wrong”
- normal matrix not applied (or wrong space)
- geometry has unwelded vertices (hard edges)
- normals aren’t normalized after interpolation (`normalize()`)

### “Depth looks banded / weird”
- use linear depth for interpretation
- far plane too far (precision loss)
- verify whether depth is reversed (some engines)

### “Tile seams / cracks”
- mismatched edge vertices between LODs
- precision mismatch in transforms
- check wireframe overlay + world position views together

---

## 🧠 Future-friendly ideas (aligned with KFM roadmap)

These are optional enhancements that match KFM’s broader direction (3D storytelling, AR, AI explainability):

- **Story-debug pass:** highlight story-node camera frustums / focus areas 🎬
- **Uncertainty shader:** scalar confidence → perceptual ramp (for AI-derived layers) 🧠
- **AR alignment shader:** emphasize depth discontinuities and tracked surfaces 📱
- **Offline QA pass:** show missing textures/tiles explicitly (no silent failure) 🧳

---

## 📎 See also (project canon)

If you’re unsure *why* a debug mode should exist, check the KFM “evidence-first / transparency” principle and the platform’s 2D/3D architecture docs.

- 📄 KFM Technical Documentation
- 📄 KFM UI System Overview
- 📄 KFM Architecture & Features
- 📄 KFM AI System Overview
- 📄 KFM Data Intake Guide
- 💡 Innovative Concepts + Future Proposals

---

