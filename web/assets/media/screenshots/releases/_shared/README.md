# 🖼️ Release Screenshots — `_shared`

![Scope](https://img.shields.io/badge/scope-shared%20across%20releases-2ea44f)
![Asset Type](https://img.shields.io/badge/asset-screenshots-blue)
![Rule](https://img.shields.io/badge/rule-don%E2%80%99t%20break%20old%20release%20notes-important)

This folder contains **evergreen UI screenshots** that are reused across multiple release notes/pages and docs.  
If an image is specific to a single release, it **does not belong here**—put it in that release’s folder instead.

> [!NOTE]
> `_shared/` is meant to stay **stable**. Prefer adding new images over replacing existing ones.

---

## 🎯 Purpose

Use `_shared/` for screenshots that are:

- ✅ Used in **multiple** releases (e.g., onboarding, navigation, core map UI, “Focus Mode” overview)
- ✅ Referenced from **documentation** that isn’t tied to a single version
- ✅ Helpful “baseline” visuals to compare future UI changes against

Not for:

- ❌ One-off release-specific UI changes
- ❌ Temporary mockups or experiments
- ❌ Marketing/brand assets (those should live in a dedicated brand/media area)

---

## 🗂️ Folder Layout

Typical sibling structure (example):

```text
web/assets/media/screenshots/releases/
├─ _shared/                 # ✅ evergreen screenshots (this folder)
│  ├─ README.md
│  ├─ <shared-assets...>
├─ vX.Y.Z/                  # 🎯 release-specific screenshots (one folder per release)
│  ├─ <release-assets...>
└─ ...
```

```mermaid
flowchart LR
  RN[📄 releases/* (release notes)] -->|embeds| SH[🖼️ web/.../releases/_shared/*]
  RN -->|embeds| RV[🖼️ web/.../releases/vX.Y.Z/*]
```

---

## 🧭 “Shared” vs “Release-Specific” (quick rule)

**Put it in `_shared/` if…**
- It represents a **core** screen that won’t age quickly (or is intentionally “baseline”).
- It will likely be reused in future release docs without edits.

**Put it in `releases/<version>/` if…**
- It shows a **new feature**, UI tweak, or bugfix unique to that release.
- It’s a **before/after** for that release’s changelog.

---

## 🧱 Naming Conventions

Keep filenames:
- ✅ lowercase
- ✅ hyphenated (kebab-case)
- ✅ descriptive
- ✅ stable over time

**Recommended pattern:**
```text
<area>-<feature>--<state>--<viewport>.<ext>
```

Examples:
- `map-layers-panel--open--desktop.webp`
- `story-node--read-mode--desktop.png`
- `focus-mode--context-bundle--desktop.webp`
- `search--results--mobile.webp`

> [!TIP]
> If you need to update a screenshot, prefer **versioning the filename** instead of overwriting:
> - `map-layers-panel--open--desktop.webp` ✅ keep
> - add: `map-layers-panel--open--desktop--2026-01.webp` ✅ new

---

## 🖼️ Formats & Quality Standards

### ✅ Preferred formats
- **`.webp`** for most screenshots (smaller size, great for web)
- **`.png`** when you need pixel-perfect UI text rendering (or if transparency matters)

### 📐 Recommended capture sizes
- **Desktop:** 1440×900 (or 1280×800)  
- **Mobile:** 390×844 (or 375×812)

### 🧼 Cropping & composition rules
- Crop to the relevant UI.
- Avoid huge empty margins.
- Keep the cursor hidden unless it’s instructional.
- Prefer consistent theme (light/dark) with the rest of the release note visuals.

---

## 🔐 Privacy, Security, and Governance

> [!IMPORTANT]
> Do **not** commit screenshots containing:
> - API keys, tokens, passwords, connection strings
> - personal data (names/emails/addresses) unless explicitly permitted + anonymized
> - sensitive locations or protected cultural/sovereignty-related details

Checklist before committing:
- [ ] No secrets visible (env values, headers, console logs)
- [ ] No PII (or fully anonymized)
- [ ] No “internal only” URLs or identifiers
- [ ] No sensitive map coordinates that shouldn’t be public

---

## ♿ Accessibility Expectations

When embedding screenshots in docs/release notes:
- Use meaningful **alt text**
- Don’t rely on images alone for critical info—include a short supporting sentence

Example embed:

```md
![Layer panel open showing hydrology overlays](web/assets/media/screenshots/releases/_shared/map-layers-panel--open--desktop.webp)
```

---

## 🔗 How to Reference These Images

### In web content (typical)
If your web build serves assets from `/assets/...`, use the site-root path:

```md
![Alt text](/assets/media/screenshots/releases/_shared/map-layers-panel--open--desktop.webp)
```

### In repo docs/release notes (GitHub rendering)
Prefer paths that are correct **from the file you’re editing**.  
Common patterns:

```md
![Alt text](../web/assets/media/screenshots/releases/_shared/map-layers-panel--open--desktop.webp)
```

or (from repo root–adjacent docs):

```md
![Alt text](web/assets/media/screenshots/releases/_shared/map-layers-panel--open--desktop.webp)
```

> [!NOTE]
> Relative paths depend on where the Markdown file lives. If a link breaks in GitHub preview, adjust `../` accordingly.

---

## ✅ Add a New Shared Screenshot (mini SOP)

1. 📸 Capture at a standard viewport (Desktop/Mobile)
2. ✂️ Crop to the UI you’re describing
3. 🧼 Sanitize (remove secrets/PII/sensitive info)
4. 🗜️ Export as `.webp` (or `.png` if needed)
5. 🏷️ Name it with the convention above
6. 🔗 Update docs/release notes to reference it

---

## 🧩 Related (project docs)

- `docs/MASTER_GUIDE_v13.md` 📘 (repo structure + pipeline overview)
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` ✍️ (Markdown conventions, admonitions, style rules)
- `releases/` 🏷️ (release notes & changelog entries)
