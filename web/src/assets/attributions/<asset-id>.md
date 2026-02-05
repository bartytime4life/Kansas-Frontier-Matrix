# 🧾 Attribution — <ASSET_NAME>

![status](https://img.shields.io/badge/status-draft-lightgrey)
![asset%20license](https://img.shields.io/badge/asset%20license-TBD-lightgrey)
![attribution](https://img.shields.io/badge/attribution-required-blue)

> 🔧 **Replace all** `<...>` placeholders before merging.  
> 🎯 Purpose: keep KFM “evidence-first” by ensuring every external UI/data asset has **clear credit + explicit license**.

---

## 📁 Where this file lives

```text
web/
└── src/
    └── assets/
        └── attributions/
            └── <asset-id>.md
```

---

## 📦 Asset summary

| Field | Value |
|---|---|
| **Asset ID** | `<asset-id>` |
| **Asset name** | `<ASSET_NAME>` |
| **Asset file** | `web/src/assets/<relative-path-to-asset>` |
| **Type** | `<icon / image / font / dataset / tile / other>` |
| **Format** | `<svg/png/...>` |
| **Used in** | `<component / route / map-layer>` |

---

## 🧑‍🎨 Upstream source (credits)

- **Creator / org:** `<Author / Organization / Project>`
- **Upstream URL:** `<https://example.com/original>`
- **Repo (optional):** `<https://github.com/org/repo>`
- **Retrieved:** `<YYYY-MM-DD>`
- **Upstream version:** `<tag/commit/date>` (optional)

---

## ⚖️ License & rights

- **License (SPDX):** `<SPDX-ID | LicenseRef-... | NONE>`
- **License name:** `<License Name>`
- **License URL:** `<https://example.com/license>`
- **Notes:** `<Any constraints or “must include” requirements>`

<details>
<summary>✅ Quick compliance checklist (fill these in)</summary>

- [ ] I confirmed the upstream license applies to this **exact** asset version.
- [ ] The attribution string below matches upstream requirements (**exact wording**).
- [ ] If ShareAlike applies, derivative/source files are tracked + published as required.
- [ ] If NonCommercial / NoDerivatives applies, KFM usage is compatible (or this asset is removed).
- [ ] Any trademark / brand constraints were reviewed (if applicable).

</details>

---

## 🏷️ Required attribution text (copy/paste)

Use this **exact string** in the UI wherever the asset appears:

```text
<REQUIRED_ATTRIBUTION_STRING>
```

If the license requires a clickable link, use:

```text
<REQUIRED_ATTRIBUTION_STRING> — <LICENSE_URL>
```

---

## 🛠️ Modifications made in KFM

- **Modified?** `<yes/no>`
- **Summary:** `<none | describe changes>`
- **Tooling:** `<optional>`
- **Why:** `<optional>`

If reproducible:

```text
<commands or short steps to reproduce the derived asset>
```

---

## 🧬 Provenance links (optional but preferred)

If this asset corresponds to a **dataset** or is derived from one, link canonical metadata here:

- 🗺️ **STAC item:** `<data/stac/items/...json>`
- 🧾 **DCAT dataset:** `<data/catalog/dcat/...jsonld>`
- 🧬 **PROV bundle:** `<data/prov/...jsonld>`
- 🧩 **KFM dataset id (API):** `<ks_hydrology_1880 | ...>`

---

## 🧭 Where to surface this attribution in the UI

- 🌍 Map attribution control (bottom-right / footer)
- 📜 About → Credits / Attributions page
- 📦 Export/Download manifests (SBOM-like or “data bundle” receipts)

---

## ✅ Definition of Done

- [ ] Front-matter complete & valid
- [ ] Source URL(s) reachable (and archived if needed)
- [ ] License confirmed + SPDX id used when possible
- [ ] Attribution string verified in UI (correct placement + legibility)
- [ ] Any modifications documented + reproducible (when feasible)
- [ ] STAC/DCAT/PROV links included (when applicable)

---

## 📚 Internal references

- `docs/MASTER_GUIDE_v13.md`
- `docs/standards/KFM_STAC_PROFILE.md`
- `docs/standards/KFM_DCAT_PROFILE.md`
- `docs/standards/KFM_PROV_PROFILE.md`
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
