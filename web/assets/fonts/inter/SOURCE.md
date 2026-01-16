<!--
📌 Purpose: Provenance-first source record for vendored font assets.
Path: web/assets/fonts/inter/
-->

# Inter — SOURCE (Provenance + License) 🔤🧾

![Asset Type](https://img.shields.io/badge/asset-font-5b5fc7)
![Family](https://img.shields.io/badge/family-Inter-111827)
![License](https://img.shields.io/badge/license-SIL%20OFL%201.1-16a34a)
![Scope](https://img.shields.io/badge/scope-web%2Fui-0ea5e9)

> This folder vendors the **Inter** typeface for the KFM web UI to keep typography consistent, fast, and available offline/air-gapped.

---

## 📦 Folder contents

Expected structure (examples — keep in sync with the actual files present):

```text
web/
└─ assets/
   └─ fonts/
      └─ inter/
         ├─ SOURCE.md            👈 you are here
         ├─ OFL.txt              ✅ required (SIL Open Font License 1.1)
         ├─ Inter-roman.woff2    (optional example)
         ├─ Inter-italic.woff2   (optional example)
         ├─ Inter.var.woff2      (optional: variable font)
         └─ inter.css            (optional: @font-face declarations)
```

---

## 🧬 Provenance record

Fill in **every** field when updating the font binaries. This is our “receipt” 🧾.

```yaml
asset:
  name: Inter
  type: font
  role: ui-typography
  local_path: web/assets/fonts/inter/

upstream:
  canonical_name: Inter
  authorship: The Inter Project Authors (original design by Rasmus Andersson)
  homepage: https://rsms.me/inter/
  source_repo: https://github.com/rsms/inter
  distribution_mirrors:
    - https://fonts.google.com/specimen/Inter

versioning:
  upstream_version: "UNKNOWN"   # e.g. "4.1"
  upstream_tag: "UNKNOWN"       # e.g. "v4.1"
  upstream_commit: "UNKNOWN"    # optional but preferred

retrieval:
  retrieved_at_utc: "UNKNOWN"   # YYYY-MM-DD
  retrieved_by: "UNKNOWN"       # name/handle
  method: "UNKNOWN"             # e.g. "GitHub Releases ZIP", "Google Fonts download"
  original_artifact_url: "UNKNOWN"
  notes: |
    Describe any transformations: subsetting, format conversion, renaming, etc.

integrity:
  files:
    # Add one entry per file committed in this folder
    - path: "OFL.txt"
      sha256: "UNKNOWN"
    - path: "Inter-roman.woff2"
      sha256: "UNKNOWN"
    - path: "Inter-italic.woff2"
      sha256: "UNKNOWN"
    - path: "Inter.var.woff2"
      sha256: "UNKNOWN"
```

---

## ✅ License

**Inter is licensed under the SIL Open Font License, Version 1.1 (OFL-1.1).**

📄 The authoritative license text **must** be present in this folder as:

- `OFL.txt`

If it’s missing, add it immediately (copy from upstream Inter sources).

---

## 🏷 Attribution

Keep attribution lightweight but clear:

- **Font family:** Inter  
- **Authors:** The Inter Project Authors (design by Rasmus Andersson)  
- **License:** SIL Open Font License 1.1 (see `OFL.txt`)  

---

## 🔁 How to update this folder (repeatable checklist)

1. **Choose an upstream release**
   - Prefer **official upstream** releases from the Inter project.
2. **Replace font binaries**
   - Keep filenames stable unless there’s a strong reason to change.
3. **Update provenance**
   - Fill out the YAML block above (version, tag, date, artifact URL, etc.).
4. **Update checksums**
   - Recompute `sha256` for every file listed under `integrity.files`.
5. **Verify UI rendering**
   - Smoke test key pages (headings, body text, map UI labels, charts).
6. **Confirm license compliance**
   - Ensure `OFL.txt` remains present and unmodified (except upstream updates).

---

## ⚡ Notes (performance & web delivery)

- Prefer **`.woff2`** for web delivery (smallest size, broad modern support).
- If using variable fonts, consider **one** variable file instead of many statics.
- If you subset the font (recommended for performance), record:
  - glyph ranges / languages included
  - tooling used (e.g., fonttools)
  - resulting file names and hashes (in the provenance record)

---

## 🧯 “Don’t do this”

- ❌ Don’t copy random font files from unknown sources.
- ❌ Don’t remove `OFL.txt`.
- ❌ Don’t rename files without updating imports and this provenance record.
- ❌ Don’t “hotfix” font binaries manually—regenerate from upstream.

---

## 📚 References

- Upstream project: https://github.com/rsms/inter  
- Inter homepage: https://rsms.me/inter/  
- OFL license info: https://scripts.sil.org/OFL