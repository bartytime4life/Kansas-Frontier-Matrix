# 📜 Sample Asset Licenses & Attributions

![Provenance First](https://img.shields.io/badge/Provenance-first-2ea44f?style=flat)
![License Transparency](https://img.shields.io/badge/License-transparency-blue?style=flat)
![No Mystery Assets](https://img.shields.io/badge/No%20mystery%20assets-required-critical?style=flat)

This folder documents **license texts** and **attribution requirements** for any third‑party assets used in:

- `web/assets/samples/_shared/` ✅ (shared demo/sample assets used across the web UI)

> [!IMPORTANT]
> Sample assets are often redistributed (repo clones, demo builds, previews).  
> That means **every non-original asset must have a clearly documented source + license**.

---

<details>
  <summary><strong>🧭 Table of Contents</strong></summary>

- [🚦 Golden rules](#-golden-rules)
- [📦 What this folder is for](#-what-this-folder-is-for)
- [📁 Suggested layout](#-suggested-layout)
- [🧾 Per-asset requirements](#-per-asset-requirements)
  - [Minimum “License Card” fields](#minimum-license-card-fields)
  - [License Card template (JSON)](#license-card-template-json)
- [🧩 Combining assets](#-combining-assets)
- [✅ Adding a new sample asset](#-adding-a-new-sample-asset)
- [🛠️ Suggested validation](#️-suggested-validation)
- [🔗 Related project references](#-related-project-references)
- [❓ FAQ](#-faq)

</details>

---

## 🚦 Golden rules

- 🧾 **No mystery assets.** If we can’t explain *where it came from* and *under what license*, it doesn’t ship.
- 🟢 **Prefer permissive / open** assets (e.g., CC0, Public Domain, CC‑BY, OFL, MIT, Apache‑2.0).
- 🧱 **Keep licensing scoped.** Sample assets may have different terms than the project’s **code** license.
- 🧩 **Composites inherit restrictions.** If you combine multiple assets in a single “output” (e.g., a screenshot, a composed map, a sprite sheet), the safest rule is: **the most restrictive license wins**.
- 🧠 **Not legal advice.** This README is an engineering checklist to keep us consistent and auditable.

---

## 📦 What this folder is for

This folder exists so that the web samples can follow the same “traceable inputs” discipline as the rest of the KFM system:

- ✅ a machine-readable record of **source + license**
- ✅ a human-readable **attribution string**
- ✅ optional full **license text** copies for offline review and redistribution

Think of it as the web UI’s lightweight “data contract” for sample media & sample datasets.

---

## 📁 Suggested layout

> These filenames are **conventions**. If the repo already uses a different naming scheme, keep the spirit (clarity + traceability) and adapt.

```text
web/assets/samples/_shared/
└── ⚖️ licenses/
    ├── 📄 README.md                          # 👈 you are here 📌 How sample assets are licensed + how to fill registry cards
    ├── 🗂️ registry/
    │   ├── 🧩📄 _schema.md                    # 🧩 (optional) docs for the registry/card format
    │   ├── ✅🧾 example.asset-license.json     # ✅ Example “license card” (shows required fields + conventions)
    │   └── 🧾 <asset-id>.asset-license.json   # 🧾 One per third-party asset (recommended; machine-readable)
    ├── 📜 texts/
    │   ├── 📜 CC-BY-4.0.txt                   # Canonical license text (verbatim)
    │   ├── 📜 OFL-1.1.txt                     # Canonical license text (verbatim)
    │   └── ➕ …                                # Additional license texts as needed
    └── 📣 notices/
        ├── 📣📄 THIRD_PARTY_NOTICES.md         # 📣 Optional aggregated notices (human-readable rollup)
        └── 🧾📄 <asset-id>.NOTICE.md           # 🧾 Per-asset notices (only when required by license/vendor)
```

---

## 🧾 Per-asset requirements

Any third‑party file used in `web/assets/samples/_shared/` should have a corresponding **License Card** here.

Examples of “assets”:
- 🖼️ images (PNG/JPG/SVG), icons, screenshots
- 🧱 map styles, sprites, glyph packs
- 🔤 fonts
- 🗺️ sample GeoJSON/TopoJSON, CSV snippets, tile bundles
- 🎞️ short demo videos / animations

### Minimum License Card fields

| Field | Required | Purpose |
|---|:---:|---|
| `id` | ✅ | Stable identifier (used in UI credits + tooling) |
| `asset_path` | ✅ | Repo-relative path to the asset |
| `title` | ✅ | Human-friendly name |
| `license` | ✅ | SPDX ID when possible (or a clear string) |
| `license_text_file` | ◻️ | Local path to the license text (if included) |
| `source_url` | ✅ | Where we got it (canonical URL preferred) |
| `creator` | ✅ | Author / org to credit |
| `attribution` | ✅ | The attribution string we show in UI/docs |
| `retrieved` | ✅ | When we fetched it (YYYY-MM-DD) |
| `modifications` | ◻️ | What we changed (resize, recolor, crop, simplify, etc.) |
| `notes` | ◻️ | Any caveats (e.g., “must include link to license”) |

> [!TIP]
> If you can’t express the license cleanly with an SPDX identifier, **include the full license name** + a license URL in `notes`.

### License Card template (JSON)

Create a file like:  
`web/assets/samples/_shared/licenses/registry/<asset-id>.asset-license.json`

```json
{
  "id": "example_asset_id",
  "asset_path": "web/assets/samples/_shared/<category>/<filename.ext>",
  "title": "Example Asset Title",
  "description": "Short description of what the sample is used for in the UI.",
  "license": "CC-BY-4.0",
  "license_text_file": "web/assets/samples/_shared/licenses/texts/CC-BY-4.0.txt",
  "source_url": "https://example.org/original/source/page",
  "creator": "Author / Organization Name",
  "retrieved": "2026-01-18",
  "attribution": "© Author / Org — Source Name (CC BY 4.0)",
  "modifications": [
    "Converted to WebP",
    "Cropped and resized to 1024px"
  ],
  "notes": [
    "Attribution required in UI credits modal.",
    "Keep link to the original source page."
  ]
}
```

---

## 🧩 Combining assets

When we combine multiple sources into a single “thing” (a composite image, a demo map export, a derived dataset, etc.):

- ✅ keep attribution for **all** inputs
- ✅ treat the result as governed by the **most restrictive** applicable terms
- ✅ if unsure: don’t ship the composite; ship the sources separately + generate the composite at runtime with proper credits

> [!WARNING]
> “ShareAlike” or “NonCommercial” licenses can create downstream constraints.  
> If a sample asset is restrictive, keep it clearly labeled and avoid baking it into anything that looks “production-default”.

---

## ✅ Adding a new sample asset

**Checklist (copy/paste into a PR description) ✅**

- [ ] I verified the asset’s license allows redistribution in a public repo.
- [ ] I added the file under `web/assets/samples/_shared/…` (or replaced an existing sample).
- [ ] I created/updated a License Card in `licenses/registry/`.
- [ ] I added license text under `licenses/texts/` (if needed/required).
- [ ] I confirmed attribution requirements and provided an `attribution` string.
- [ ] If the asset is restrictive (NC/ND/ShareAlike), I added a clear warning in `notes`.

---

## 🛠️ Suggested validation

If/when we add CI checks for sample assets, the simplest “good enough” rules are:

- 🔍 Every file under `web/assets/samples/_shared/**` must be covered by:
  - a License Card **or**
  - an explicit allow-list entry (e.g., “first-party / generated / project-owned”)
- 🚫 Block merges if:
  - `license` is missing
  - `source_url` is missing
  - `attribution` is missing
- 🧱 Optional: track `sha256` checksums in the License Card for tamper-evidence & cache validation.

---

## 🔗 Related project references

- 🧑‍⚖️ Project code license: [`LICENSE`](../../../../../LICENSE)
- 📌 How to cite the project: [`CITATION.cff`](../../../../../CITATION.cff)
- 🧭 Provenance philosophy (repo standards):  
  - `docs/standards/` (STAC/DCAT/PROV profiles, work protocols, governance docs)

---

## ❓ FAQ

**Q: Can I use these sample assets outside of KFM?**  
A: Maybe. Each asset’s License Card is the source of truth. Follow that license and attribution terms.

**Q: Why not just put one big `THIRD_PARTY_NOTICES.md` at the repo root?**  
A: We may still do that. This folder keeps sample-only credits scoped to sample-only files, which reduces confusion.

**Q: What about assets generated by us?**  
A: Treat them as first‑party, but still consider adding a small License Card if the asset is published/exported or frequently reused (it’s helpful for internal clarity).

---

