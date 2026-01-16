# Icon Licenses (Generated) 🧾✨

![status](https://img.shields.io/badge/status-generated-blue)
![scope](https://img.shields.io/badge/scope-web%20icons-7c3aed)
![compliance](https://img.shields.io/badge/compliance-third--party%20licenses-brightgreen)

> [!IMPORTANT]
> This folder is **generated** by the icon pipeline.  
> ✅ Commit the generated output.  
> ❌ Do **not** hand-edit files here — your changes will be overwritten.

---

## 📍 Location

`web/assets/icons/_generated/_licenses/`

---

## Why this exists ✅

KFM ships third-party icon assets in the web UI. Many icon sources require:
- Including the **license text**
- Providing an **attribution / notice**
- Recording **source provenance** (who/where it came from, and what changed)

This directory is the **single auditable place** where those obligations are tracked for icons that end up in `_generated/`.

---

## What lives here 📦

Depending on the generator, you will typically see one (or both) of these patterns:

```text
📁 web/assets/icons/_generated/_licenses/
├─ README.md                         ← this file
├─ THIRD_PARTY_NOTICES.md            ← (optional) aggregated notices
├─ <source-or-pack>.LICENSE.txt      ← license text (per source)
├─ <source-or-pack>.NOTICE.md        ← attribution / notice (per source)
└─ <source-or-pack>/                 ← (optional) per-source folder style
   ├─ LICENSE.txt
   ├─ NOTICE.md
   └─ metadata.json
```

> [!TIP]
> If icons were added/changed and **no corresponding license/notice output** appears here after regeneration, treat it as a **release blocker**. 🛑

---

## Provenance-first rules 🧭

We treat icon licensing the same way we treat data provenance: **no “mystery inputs.”**  
That means every icon source should have metadata that answers:

- **Source**: where the icon came from (upstream project + URL)
- **License**: SPDX identifier if possible + full license text
- **Attribution**: required notice text (if any)
- **Version**: tag/commit/hash/pack version used
- **Modifications**: whether we changed the icon (and how)
- **Usage**: where it’s used (optional but helpful)

---

## Regeneration 🔁

> [!NOTE]
> The exact command(s) depend on the repo’s tooling. The intent is always the same:
> regenerate icons → regenerate license/notice artifacts → commit the results.

```bash
# From repo root (examples — pick what matches your setup)
pnpm run icons:generate && pnpm run icons:licenses
# or
npm run icons:generate && npm run icons:licenses
# or
yarn icons:generate && yarn icons:licenses

# If you don’t know the script name:
# search the repo for: "icons:_generated", "generate-icons", or "_licenses"
```

---

## Adding a new icon source 🧩

1. **Verify license compatibility** (before importing anything).
2. Add the icon source to the **non-generated** inputs (wherever the icon pipeline reads from).
3. Add/extend the **license manifest** that feeds this folder’s generation.
4. Regenerate output.
5. Confirm required attribution is **shipped** and **visible** where appropriate.

> [!WARNING]
> Never copy icons from unknown sources. If the license is unclear, the icon can’t ship.

---

## Recommended license manifest schema 🧱

If your pipeline supports a manifest file, this is a solid minimum contract:

<details>
<summary><strong>📄 Example manifest entry (JSON)</strong></summary>

```json
{
  "id": "example-pack",
  "name": "Example Icon Pack",
  "homepage": "https://example.com/icons",
  "upstream_version": "v1.2.3",
  "license": {
    "spdx": "MIT",
    "text_path": "LICENSE.txt"
  },
  "required_attribution": true,
  "attribution_text": "© Example Authors — used under the MIT License.",
  "modified": false,
  "notes": "If modified=true, describe changes here.",
  "used_in": [
    "web/components/MapLegend",
    "web/features/search"
  ]
}
```
</details>

---

## PR checklist for icon changes ✅

- [ ] Every new icon has a **known source** and **known license**
- [ ] License text and notices are present in `_generated/_licenses/`
- [ ] Any required attribution is **included in the app build artifacts**
- [ ] Any required on-screen attribution is wired into the UI (About/Credits/Legal, etc.)
- [ ] Regeneration output is included in the same PR (no “regen later”)

---

## Troubleshooting 🧯

**“I added icons but nothing changed in `_licenses/`.”**
- The icon pipeline may not know the source is new
- The license manifest may be missing/incorrect
- The generator may be excluded by `.gitignore` patterns (verify it’s tracked)

**“The license requires attribution in the UI.”**
- Add it to the **Credits / Legal / About** surface that ships with the web build
- Keep the authoritative text here in `_licenses/` and render from it if possible

---

## Quick reminder 🧠

> [!IMPORTANT]
> **Generated directory policy:**  
> Edit the *inputs* (source icons + license manifest), not the generated outputs.
