# 🎨 Shared Shaders (WebGL / Cesium)  

![GLSL](https://img.shields.io/badge/GLSL-ES-7b68ee?style=for-the-badge)
![WebGL](https://img.shields.io/badge/WebGL-1%20%2F%202-ff7f50?style=for-the-badge)
![CesiumJS](https://img.shields.io/badge/CesiumJS-3D%20Tiles-1e90ff?style=for-the-badge)
![MapLibre](https://img.shields.io/badge/MapLibre-GL-2e8b57?style=for-the-badge)
![KFM](https://img.shields.io/badge/KFM-Provenance--first-success?style=for-the-badge)

> 🧠 **Rule of thumb:** shaders are *production code*. Treat them like you would a backend endpoint: documented, validated, and hard to misuse.

---

## 📍 Location

This README lives here:

```txt
web/
└─ 📁 assets/
   └─ 🧊 3d/
      └─ 🧰 shared/
         └─ 🧬 shaders/
            ├─ 📄 README.md          # 👈 you are here 📌 Shared shader snippets: usage rules, compatibility, and safety notes
            └─ 🧬 …                  # Shader files (GLSL/WGSL snippets, includes, presets; keep small + documented)
```

---

## 🧭 Why this folder exists

KFM’s web client includes **2D and 3D viewers** (MapLibre GL JS + CesiumJS) and supports **3D Tiles streaming** for geospatial 3D content. This directory holds **shader code that is shared** across those rendering paths, so we don’t duplicate logic (color ramps, picking, lighting helpers, debug overlays, etc.).  

✅ Put **shared + reusable** shader logic here.  
❌ Keep **feature-specific** shaders next to the module/viewer that owns them.

---

## 🧩 What counts as a “shader” here?

In WebGL terms, we typically deal with:

- **Vertex shaders** 🧱 (per-vertex logic: positions, normals, varyings)
- **Fragment shaders** 🎨 (per-fragment logic: color, lighting, blending)
- **Chunks / includes** 🧩 (reusable GLSL functions/constants)

If you’re new to this: WebGL rendering is driven by JavaScript/TypeScript **plus** shader programs that execute on the GPU.

---

## 🗂️ Recommended layout (keep it boring on purpose)

> If this folder already has a different structure, follow the existing pattern; otherwise this is the default we’ll grow into.

```txt
shaders/
├─ 🧩 chunks/            # 🧩 Small reusable shader helpers (math, color, noise, coordinate transforms)
├─ 🧱 materials/         # 🧱 Surface shading helpers (lighting models, PBR-ish utilities, BRDF snippets)
├─ ✨ post/              # ✨ Post-processing effects (tone mapping, outlines, fog, FX passes)
├─ 🧪 debug/             # 🧪 Debug views (normals, depth, wireframe/IDs) for development and QA
├─ 🖱️ picking/           # 🖱️ GPU picking helpers (ID encoding/decoding, hit testing buffers)
└─ 📄 README.md          # 📘 How shaders are organized, included, versioned, and tested across renderers
```

---

## 🧾 File naming rules

### ✅ Extensions
Use explicit stage markers so tooling/grep stays simple:

- `*.vert.glsl` — vertex shader
- `*.frag.glsl` — fragment shader
- `*.glsl` — shared chunks (functions, constants, structs)

### ✅ Names
- `kebab-case` for filenames: `terrain-hillshade.frag.glsl`
- Avoid “misc”, “temp”, “new2” 😅
- If it’s KFM-specific behavior, prefix the *shader_id* (not necessarily the filename) with `kfm.`

---

## 🧾 Required shader header (metadata block)

Every shader file in this folder **must start** with a header like this:

```glsl
/**
 * @kfm.shader_id   kfm.example.basic-color
 * @kfm.stage       fragment   // vertex | fragment | chunk
 * @kfm.version     1
 *
 * @kfm.summary     Minimal example fragment shader that outputs a solid color.
 *
 * @kfm.inputs
 *   uniforms:
 *     - u_color: vec4  // RGBA linear
 *
 * @kfm.outputs
 *   - gl_FragColor: vec4
 *
 * @kfm.coordinate_spaces
 *   - clip: gl_Position (vertex)
 *   - world/local: describe if used
 *
 * @kfm.governance
 *   - classification: inherits_from_layer_metadata
 *   - provenance: must remain inspectable via UI layer metadata (no “mystery rendering”)
 *
 * @kfm.license
 *   - origin: first-party
 *   - third_party: false
 */
```

Why so strict? Because KFM is provenance-first: visual output **must remain explainable and traceable** (even when it’s “just a shader”).

---

## 🔤 Naming conventions (variables + functions)

| Kind | Prefix | Example |
|---|---|---|
| Attributes | `a_` | `a_position` |
| Uniforms | `u_` | `u_modelViewProjection` |
| Varyings | `v_` | `v_uv` |
| Samplers | `t_` | `t_colorRamp` |
| Constants | `K_` | `K_PI` |
| Functions | `kfm_` | `kfm_srgbToLinear()` |

✅ Keep public/shared functions prefixed with `kfm_` to avoid collisions when chunks are concatenated.

---

## 🧭 Coordinate spaces (the “don’t get lost” section)

You *must* state (in the header) which spaces your shader expects/produces.

Typical spaces you’ll see:

- **local/model** 🧱 — object space
- **world** 🌍 — geospatial world space (Cesium commonly uses ECEF-style coordinates)
- **view** 👁️ — camera space
- **clip** 📐 — `gl_Position`
- **screen** 🖥️ — `gl_FragCoord`

📌 If you’re mixing MapLibre + Cesium concepts: keep shader math **local and explicit**, and pass transforms as uniforms rather than re-deriving them.

---

## 🎛️ Feature flags & shader variants

Shader variants are allowed, but we keep them **disciplined**:

✅ Prefer:
- `#define` / compile-time flags (fast + predictable)
- Small, composable chunks (avoid mega-shaders)

⚠️ Avoid:
- Runtime string-building that becomes untraceable
- Unbounded loops / heavy branching in fragment shaders

Suggested pattern:

```glsl
// Example compile-time feature toggle
#ifdef KFM_ENABLE_FOG
  color.rgb = kfm_applyFog(color.rgb, v_distance);
#endif
```

---

## ✅ Quality gates (what PRs should pass)

Before merging shader changes, aim to satisfy:

- [ ] **Compiles** on target contexts (WebGL1 baseline unless explicitly WebGL2-only)
- [ ] **No silent fallbacks** (if an extension is required, guard it + document it)
- [ ] **Deterministic output** (same inputs → same pixels)
- [ ] **Performance sanity** (no “oops 10ms per frame” surprises)
- [ ] **Provenance safe** (visualization still maps cleanly to layer metadata & legends)

---

## 🧪 Debugging checklist

When something is “just black” 😅:

1. **Check compile logs**
   - `gl.getShaderInfoLog(shader)`
   - `gl.getProgramInfoLog(program)`

2. **Start with a known-good fragment output**
   ```glsl
   gl_FragColor = vec4(1.0, 0.0, 1.0, 1.0); // loud magenta
   ```

3. **Validate precision qualifiers**
   - Some mobile GPUs are picky if precision isn’t declared in fragment shaders.

4. **Use debug modes**
   - Add a `debug/` shader variant that visualizes normals/depth/IDs.

---

## ⚡ Performance cheatsheet (GPU-friendly habits)

- Prefer **mediump** in fragment shaders unless you *prove* you need `highp`
- Minimize varyings (pack values when possible)
- Avoid dynamic branching in fragments (`if` per pixel can be expensive)
- Prefer LUTs/ramps via textures for complex mapping
- Use derivatives (`dFdx/dFdy`) cautiously (WebGL extension considerations)

---

## 🔐 Governance & safety (KFM-specific)

Shaders can accidentally become a “backdoor” for confusing or misleading visuals.

**Rules:**
- Do not bake dataset-specific meaning into code without a matching **legend + metadata** path.
- If a shader changes semantics (e.g., classification colors), ensure the UI can still:
  - explain the mapping
  - cite the underlying layer/source
- Debug overlays must respect the same display constraints as the data they visualize.

---

## 🧰 Example: minimal shader pair (template)

### `basic.vert.glsl`
```glsl
/**
 * @kfm.shader_id   kfm.template.basic
 * @kfm.stage       vertex
 * @kfm.version     1
 */
attribute vec3 a_position;
uniform mat4 u_mvp;

void main() {
  gl_Position = u_mvp * vec4(a_position, 1.0);
}
```

### `basic.frag.glsl`
```glsl
/**
 * @kfm.shader_id   kfm.template.basic
 * @kfm.stage       fragment
 * @kfm.version     1
 */
precision mediump float;
uniform vec4 u_color;

void main() {
  gl_FragColor = u_color;
}
```

---

## ➕ Adding a new shader (PR flow)

1. 📄 Create the shader file(s) using the naming rules.
2. 🧾 Add the required metadata header.
3. 🧩 If you create reusable logic, put it in `chunks/` (don’t duplicate).
4. 🧪 Ensure it compiles in the target viewer path (MapLibre custom layer / Cesium material / raw WebGL).
5. 📝 Update any relevant legends/metadata wiring in the viewer (so users can interpret the pixels).

---

## 📚 References (project + learning)

- 📄 KFM technical documentation (architecture, viewers, governance)
- 🧭 KFM markdown / provenance conventions (how we keep things explainable)
- 📘 WebGL shader fundamentals (vertex vs fragment, compile/link lifecycle)

> Tip: keep this README “living”. If we invent a new convention twice, it belongs here. ✍️
