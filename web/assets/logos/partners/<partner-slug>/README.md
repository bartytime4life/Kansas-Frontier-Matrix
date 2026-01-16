# 🤝 Partner Logo — `<partner-slug>`

![Asset](https://img.shields.io/badge/asset-partner%20logo-2ea44f) ![Scope](https://img.shields.io/badge/scope-web%20ui-blue) ![Path](https://img.shields.io/badge/path-web%2Fassets%2Flogos%2Fpartners%2F%3Cpartner--slug%3E%2F-555) ![Status](https://img.shields.io/badge/status-governed%20asset-orange)

> 🧭 **Purpose**: This folder contains the **approved brand assets** for a specific partner organization, used by the KFM web UI (credits pages, “powered by” footer, attribution panels, etc.).  
> ✅ Keep it **local**, **traceable**, and **permissioned**.

---

## 📌 Quick facts (fill in)

| Field | Value |
|---|---|
| **Partner name** | `Partner Organization Name` |
| **Partner slug (folder name)** | `<partner-slug>` *(kebab-case; stable identifier)* |
| **Website** | `https://example.org` |
| **Brand guidelines** | `https://example.org/brand` *(or “Provided via email”)* |
| **Approval / permission** | `See Provenance & Permissions below` |
| **Primary UI usage** | `Footer / Credits / Attribution panel / etc.` |

---

## 🧾 Provenance & permissions (non-negotiable ✅)

> 🧷 **If it shows up in the UI, we must know where it came from and that we’re allowed to use it.**  
> Partner logos are often **trademarked** — treat them as a governed asset.

| Item | Details |
|---|---|
| **Asset source** | `URL to official press kit` **or** `email thread summary` |
| **Retrieved by** | `@github-handle` |
| **Retrieved on** | `YYYY-MM-DD` |
| **License / usage terms** | `Public press kit terms / written permission / CC / etc.` |
| **Required attribution text** | `If partner requires a specific credit line, paste it here verbatim` |
| **Restrictions** | `e.g., No recoloring / no distortion / no commercial reuse outside KFM` |
| **Notes** | `Anything that helps future maintainers verify legitimacy` |

✅ **If permission is unclear:** do **not** merge the logo into `main`. Add an issue and park the asset in a PR/draft branch until resolved.

---

## 📁 Folder layout

```text
📦 web/
  └─ 📂 assets/
     └─ 📂 logos/
        └─ 📂 partners/
           └─ 📂 <partner-slug>/
              ├─ 🖼️ logo.svg              # preferred (vector)
              ├─ 🖼️ logo.png              # fallback (transparent)
              ├─ 🖼️ logo-light.svg        # optional: for dark UI backgrounds
              ├─ 🖼️ logo-dark.svg         # optional: for light UI backgrounds
              ├─ 🖼️ icon.svg              # optional: square mark (favicon-style)
              ├─ 📄 LICENSE.txt           # optional: if partner provides explicit terms
              └─ 📄 README.md             # you are here ✨
```

---

## ✅ Required files & naming conventions

| File | Required | Why | Requirements |
|---|---:|---|---|
| `logo.svg` | ✅ | Best quality + smallest size | Clean SVG, **no embedded raster**, transparent background, paths optimized |
| `logo.png` | ✅ | Fallback for contexts that can’t render SVG | Transparent background, crisp at common sizes, no visible halos |
| `logo-light.svg` | ➕ | Better contrast on dark backgrounds | Only if needed; don’t invert without permission |
| `logo-dark.svg` | ➕ | Better contrast on light backgrounds | Only if needed; don’t “recreate” the logo |
| `icon.svg` | ➕ | Compact/square mark | Only if partner provides an official icon/mark |

### 🔤 Slug rules (`<partner-slug>`)
- Use **kebab-case**: `kansas-historical-society`, `usgs`, `openstreetmap`
- Slug should be **stable** even if the partner slightly rebrands (avoid frequent renames).
- If there’s a collision: append a qualifier like `-foundation`, `-lab`, `-program`.

---

## 👀 Quick preview (optional, once assets exist)

> If you add `logo.svg`, you can preview it right in this README.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./logo-light.svg">
  <img alt="Partner logo preview" src="./logo.svg" width="320">
</picture>

<details>
<summary>🧩 If you only have one SVG</summary>

If you don’t have separate light/dark variants yet, keep the preview simple:

```md
![Partner logo](./logo.svg)
```

</details>

---

## 🎨 Usage guidance (do / don’t)

### ✅ Do
- Keep the logo’s **aspect ratio** locked.
- Use the partner’s **official** assets (press kit or written permission).
- Provide **accessible alt text** (screen readers).

### ❌ Don’t
- Recreate/redraw the logo.
- Apply filters, shadows, outlines, or recolors unless the partner’s brand guidelines explicitly allow it.
- Crop the logo or remove trademark symbols if they were present in the provided asset.

---

## 🔗 How to use in the UI

> These examples are intentionally framework-agnostic. Adapt to the KFM web stack as needed.

<details>
<summary>🧱 HTML</summary>

```html
<img
  src="/assets/logos/partners/<partner-slug>/logo.svg"
  alt="Partner Organization Name logo"
  height="32"
/>
```

</details>

<details>
<summary>⚛️ React (example)</summary>

```tsx
export function PartnerLogo() {
  return (
    <img
      src="/assets/logos/partners/<partner-slug>/logo.svg"
      alt="Partner Organization Name logo"
      style={{ height: 32, width: "auto" }}
      loading="lazy"
      decoding="async"
    />
  );
}
```

</details>

<details>
<summary>🌗 Light/Dark with <code>&lt;picture&gt;</code></summary>

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/assets/logos/partners/<partner-slug>/logo-light.svg" />
  <img
    src="/assets/logos/partners/<partner-slug>/logo-dark.svg"
    alt="Partner Organization Name logo"
    height="32"
  />
</picture>
```

</details>

---

## 🧪 Quality checklist (PR reviewers ✅)

- [ ] **Permission recorded** in “Provenance & permissions”
- [ ] `logo.svg` renders correctly on **light + dark** backgrounds
- [ ] Raster fallback (`logo.png`) is **transparent** and not blurry at typical UI sizes
- [ ] Filenames match the conventions in this README
- [ ] No unnecessary binary bloat (keep assets small)
- [ ] No tracking pixels / external hotlinks / remote assets
- [ ] Alt text is meaningful (not “logo”)

---

## 🔄 Updates & rebrands

If a partner rebrands:
1. Add the new official assets **alongside** existing ones (temporarily).
2. Update the UI references in one PR.
3. Remove deprecated assets only after the UI no longer references them.
4. Record the change in the changelog below.

---

## 📝 Changelog

- `YYYY-MM-DD` — Initial partner logo added (`logo.svg`, `logo.png`) by `@handle`
- `YYYY-MM-DD` — Added light/dark variants per brand guidelines