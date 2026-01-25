# 🪨 Monument Rocks — Thumbnails

![KFM](https://img.shields.io/badge/KFM-web%20assets-2ea44f) ![3D](https://img.shields.io/badge/3D-model%20previews-blue) ![Preferred](https://img.shields.io/badge/preferred-WebP-informational) ![A11y](https://img.shields.io/badge/a11y-alt%20text%20required-yellow) ![Provenance](https://img.shields.io/badge/ethos-provenance--first-purple)

> 🖼️ **UI preview images** for the **Monument Rocks** 3D model — used in KFM’s cards, story steps, and 2D ↔ 3D experiences.

---

## 📦 What lives here (and what doesn’t)

> [!IMPORTANT]
> ✅ This folder should contain only **final, web-optimized raster previews** (WebP/PNG).  
> ❌ No raw renders, no `.blend`, no huge source images, no “working” files.

Thumbnails are *derived artifacts* that make the UI fast, consistent, and scannable.

---

## 🗂️ Folder map

```text
🌐 web/
└── 🧰 assets/
    └── 🧊 3d/
        └── 🤝 shared/
            └── 🧩 models/
                └── 🪨 monument-rocks/
                    └── 🖼️ thumbnails/                     ✅ 👈 📍 you are here
                        ├── 🖼️ thumbnail.webp              (required: primary UI card)
                        ├── 🖼️ thumbnail@2x.webp           (optional: retina)
                        ├── 🏞️ banner.webp                 (optional: wide hero / story cover)
                        ├── 🏞️ banner@2x.webp              (optional: retina)
                        └── 📄 README.md                    (this file)
```

> [!NOTE]
> The **UI code** decides where each thumbnail is used; this folder just provides a consistent, predictable asset surface.

---

## ✅ Expected files & specs

| File | Required | Purpose | Recommended dimensions | Target file size |
|---|:---:|---|---:|---:|
| `thumbnail.webp` | ✅ | Default preview (catalog cards, story steps, popovers) | **512×512** | ≤ 250 KB |
| `thumbnail@2x.webp` | ➕ | Crisp preview on high-DPI screens | **1024×1024** | ≤ 600 KB |
| `banner.webp` | ➕ | Wide hero usage (story cover / feature tiles) | **1600×900** (16:9) | ≤ 450 KB |
| `banner@2x.webp` | ➕ | High-DPI hero | **3200×1800** | ≤ 1.2 MB |

### ✅ Format rules
- **Preferred:** `.webp` (fast decode + good compression)
- **Fallback (only if needed):** `.png`
- **Color space:** sRGB
- **No baked-in text** (keep thumbnails language-neutral for future federation / reuse 🌍)

---

## 🎨 Visual standards (make it feel “KFM”)

### 📸 Composition
- Pick an angle that instantly reads as **Monument Rocks** at **tiny sizes** (128–200 px).
- Favor a **3/4 view** with strong silhouette and depth cues.
- Keep the subject centered with safe padding (avoid edge-clips on responsive crops).

### 💡 Lighting & tone
- Neutral daylight or soft overcast look (avoid harsh contrast).
- Slight ambient occlusion is fine ✅ (avoid “gamey” over-darkening).
- Avoid extreme saturation; keep it “scientific but inviting” 🧭

### 🧽 Background
- Prefer a clean, natural environment (sky/ground is fine).
- Transparent backgrounds are allowed **only** if the UI component expects it.

---

## 🧾 Provenance & credit expectations

Even though these are “just thumbnails,” treat them as **published artifacts**:

- ✅ Only render from assets you have the right to use (model + textures + HDRIs).
- ✅ If the thumbnail is derived from a photo (instead of a render), ensure:
  - License is compatible
  - Photographer/source is documented (else don’t use it)
- ✅ Keep edits minimal and reproducible (no mystery Photoshop magic ✋)

> [!TIP]
> If you’re updating thumbnails as part of a bigger model refresh, include a short PR note like:
> `asset(monument-rocks): refresh thumbnails (new lighting + tighter crop)`

---

## 🔒 Governance & sensitivity guardrails

KFM prioritizes **trust, safety, and respect**:

- Don’t include imagery that reveals **restricted/sensitive locations** or violates a dataset’s classification intent.
- If a model is ever marked as **restricted**, thumbnails must follow the same visibility rules (no “leaking by preview” 🕵️‍♂️).

---

## 🧪 QA checklist (before merging)

- [ ] `thumbnail.webp` exists and is readable
- [ ] Looks good at **128×128** (no mushy blur / muddy shadows)
- [ ] No jagged edges / zippering artifacts
- [ ] File sizes are within targets (performance matters 📱)
- [ ] Colors look correct (sRGB) and not overly dark
- [ ] No embedded text / watermark unless explicitly required
- [ ] Verified at least once in the UI component(s) that consume it

---

## 🧰 Suggested generation paths (pick one)

```mermaid
flowchart LR
  A[🧱 3D Model<br/>(glTF / 3D Tiles / mesh)] --> B[🎥 Render snapshot<br/>(consistent camera + lighting)]
  B --> C[🗜️ Optimize<br/>(WebP compression + size targets)]
  C --> D[🖼️ Drop into thumbnails/]
  D --> E[🧭 KFM UI<br/>(cards • stories • 2D↔3D)]
```

<details>
<summary><strong>Option A — Blender (repeatable)</strong> 🟦</summary>

- Import the model
- Use a saved camera + lighting rig
- Render to PNG
- Convert to WebP (`cwebp`) with target sizes

✅ Best when you want consistent “house style” across many models.
</details>

<details>
<summary><strong>Option B — Three.js / headless snapshot (automation-ready)</strong> 🟩</summary>

- Load model in a minimal scene
- Use deterministic camera framing
- Capture with headless Chromium (Playwright/Puppeteer)
- Post-process/encode to WebP

✅ Best when you want CI-friendly regeneration.
</details>

<details>
<summary><strong>Option C — Manual export (okay for one-offs)</strong> 🟨</summary>

- Capture a clean frame from an approved viewer
- Ensure consistent crop + color
- Compress to WebP

⚠️ Use sparingly; it’s easiest to lose reproducibility.
</details>

---

## 🔗 Where this fits in KFM 🧭

These thumbnails are a small piece of a bigger KFM pattern:
- 📚 **Discovery-first UI** (scanable catalogs + story entry points)
- 🗺️ **2D ↔ 3D storytelling** (fast previews before heavier 3D loads)
- 📦 **Offline-friendly bundles** (small assets cache well)

---

## 🤝 Contributing notes

- Keep changes focused: thumbnails should change only when the model, visual standards, or UI needs change.
- If you add new optional sizes, ensure the UI can reference them (don’t orphan files 🧩).
- Prefer PRs that include before/after screenshots in the description 📸

---

