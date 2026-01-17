# ⚙️ UI Settings Screenshots (Web)

![Screenshots](https://img.shields.io/badge/assets-screenshots-blue)
![Scope](https://img.shields.io/badge/scope-ui%2Fsettings-6f42c1)
![Format](https://img.shields.io/badge/format-png%20%7C%20webp-brightgreen)

**Folder:** `web/assets/media/screenshots/ui/settings/` 📁

A curated set of **golden screenshots** for the **Settings** UI in the KFM web app — used for:
- 🧪 **Visual regression** (quick “did we break layout?” checks)
- 🧩 **Design/UX review** (states, spacing, accessibility, copy)
- 🧾 **Documentation + PR evidence** (clear before/after comparisons)

---

## 🧭 What belongs here

Store screenshots that represent **intentional UI states** of Settings, such as:
- Default Settings panel (fresh load)
- Tabs/sections (e.g., *Map*, *Privacy*, *Accessibility*, *Account*, *Advanced*)
- Expanded / collapsed accordions
- Toggle on/off states (and disabled states)
- Validation and error states (inline help, banners, empty state)
- Confirm dialogs / destructive actions (if applicable)
- Sensitivity / redaction notices surfaced via settings controls (if applicable)

> ✅ Tip: Think “canonical UI states,” not random captures.

---

## 🗂️ Recommended structure

You can keep everything flat if you want, but this structure scales nicely:

```text
web/assets/media/screenshots/ui/settings/
├── README.md
├── light/
│   ├── desktop/
│   └── mobile/
└── dark/
    ├── desktop/
    └── mobile/
```

---

## 🏷️ Naming convention

Use **stable, descriptive names** so diffs are obvious and files are easy to locate.

**Suggested pattern:**
```text
settings--<section>--<state>--<theme>--<viewport>.<ext>
```

Where:
- `<section>`: `general` | `map` | `privacy` | `accessibility` | `advanced` | `about` | etc.
- `<state>`: `default` | `expanded` | `modal-open` | `error` | `empty` | `disabled` | etc.
- `<theme>`: `light` | `dark`
- `<viewport>`: `1440x900` | `1024x768` | `390x844` | etc.
- `<ext>`: `png` (preferred for crisp UI) or `webp` (preferred if size is large)

<details>
  <summary><strong>✨ Examples</strong></summary>

```text
settings--privacy--expanded--dark--1440x900.png
settings--map--default--light--1440x900.png
settings--advanced--error--dark--390x844.png
settings--accessibility--modal-open--light--1024x768.webp
```
</details>

---

## 📸 Capture checklist (keep screenshots comparable)

- [ ] **Use consistent viewport** per category (desktop/tablet/mobile)
- [ ] **100% browser zoom** (no OS scaling weirdness if possible)
- [ ] **Stable test data** (avoid dynamic values, rotating tips, timestamps, etc.)
- [ ] **No cursor** (unless intentionally documenting hover behavior)
- [ ] **Same theme + density** (don’t mix compact/comfortable unless it’s the point)
- [ ] **Avoid map noise** behind the panel (keep background consistent if visible)

---

## 🔒 Redaction & safety rules (non‑negotiable)

**Do not commit screenshots that contain:**
- API keys, tokens, connection strings, secrets
- PII (emails, names, addresses, phone numbers) unless explicitly approved
- Sensitive/precise locations or restricted content that should not ship publicly

> 🧯 If something sensitive is visible, re-capture with **seeded demo data**, **masked fields**, or **blur** *before* committing.

---

## 🔁 When to update screenshots

Update (or add) screenshots when:
- Layout, spacing, typography, icons, or alignment changes
- Copy changes (labels, helper text, warnings, tooltips)
- New settings are introduced or removed
- Accessibility-related behavior changes (focus rings, contrast, keyboard nav hints)
- Any change would be meaningful in a PR review (“show me what changed”)

---

## 🧩 Using screenshots in docs & PRs

### Embed in Markdown (docs, issues, PR descriptions)
```md
![Settings — Privacy (dark)](./dark/desktop/settings--privacy--expanded--dark--1440x900.png)
```

### PR workflow tip
- Include **before/after** pairs when UI behavior changes
- Keep filenames stable when replacing “the same” canonical state (so diffs track cleanly)

---

## 🧾 Optional: add a tiny manifest (future-friendly)

If this folder grows, consider adding:
- `manifest.json` or `manifest.yml` with:
  - file name
  - route / UI entry point
  - viewport
  - theme
  - notes (what this screenshot proves)
  - capture date (optional)

This makes it easier to automate checks later (and keeps the set auditable).

---

## 🔗 Related references (repo context)

- `docs/MASTER_GUIDE_v13.md` 📘  
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` 🧩  
- `schemas/ui/` 🧱 (UI contracts / schemas, if applicable)

---

🧠 _Goal:_ keep Settings UI screenshots **clean**, **repeatable**, and **useful as evidence**.
