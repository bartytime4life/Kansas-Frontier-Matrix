# 🧱 ADR Assets

![scope](https://img.shields.io/badge/scope-docs%2Farchitecture%2Fadr%2Fassets-2b8a3e)
![adr](https://img.shields.io/badge/ADRs-architecture%20decisions-1971c2)
![formats](https://img.shields.io/badge/formats-SVG%20%7C%20PNG%20%7C%20Mermaid%20%7C%20CSV-495057)

This folder holds **supporting assets referenced by Architecture Decision Records (ADRs)** in `docs/architecture/adr/` — diagrams, screenshots, small evidence artifacts, and “source” files used to generate visuals.

- ⬅️ **Back to ADRs:** [`..`](..)
- 📈 **Shared architecture diagrams:** [`../../diagrams/`](../../diagrams/)
- 📚 **Docs root:** [`../../../`](../../../)

---

## ✅ TL;DR rules

- 🧩 **Prefer text-first diagrams** (Mermaid) inside the ADR when feasible.
- 🗂️ **One folder per ADR** under `assets/` using the ADR slug.
- 🧾 **Keep “source + export” together** (e.g., `.mmd`/`.drawio` + `.svg`/`.png`).
- 🧪 If it’s evidence, make it **reproducible** (include how it was generated).
- 🔒 **No secrets, PII, or restricted data** — ever.
- 🧭 If it’s used across multiple ADRs, it likely belongs in **`docs/architecture/diagrams/`** instead.

---

## 📁 Folder contract

### ✅ Good fits for this folder
- 🗺️ Architecture diagrams (context, container, component, sequence, dataflow)
- 🖼️ UI screenshots (map UI, admin UI, Focus Mode UI, etc.)
- 📊 Small charts/plots used to justify a decision (exported image + source data/snippet)
- 🧪 Benchmark summaries (small logs, charts, decision matrices)
- 🧱 Design artifacts that support the ADR narrative (risk matrices, trade study tables)

### 🚫 Not a fit for this folder
- 🧺 **Raw or large processed datasets** → put those under `data/…` and catalog them (STAC/DCAT/PROV)
- 🏗️ Build artifacts or generated bundles
- 🔑 Secrets, credentials, private keys, tokens
- 🧍‍♂️ Sensitive info (PII), protected locations, or anything restricted by governance

> 🔎 **Rule of thumb:** if it belongs in a catalog or drives the pipeline, it’s probably `data/` (with metadata).  
> If it explains a decision, it’s probably here.

---

## 🗂️ Layout & naming

### Recommended structure (per-ADR folder)
Name the asset folder to match the ADR file slug (without the `.md`):

- ADR: `docs/architecture/adr/adr-0032-api-boundary.md`
- Assets: `docs/architecture/adr/assets/adr-0032-api-boundary/`

Example tree:

```text
📁 docs/
└── 📁 architecture/
    └── 📁 adr/
        ├── 📄 adr-0032-api-boundary.md
        └── 📁 assets/
            ├── 📄 README.md   ✅ (this file)
            └── 📁 adr-0032-api-boundary/
                ├── 🖼️ system-context.svg
                ├── 🖼️ request-flow.png
                ├── 🧩 request-flow.mmd
                ├── 📊 decision-matrix.csv
                └── 📄 REPRODUCE.md
```

### Naming conventions
- ✅ **kebab-case**: `request-flow.svg`, `system-context.svg`
- ✅ Use **clear intent**: `sequence-authz.svg` beats `diagram2.svg`
- ✅ Optional prefixes:
  - `ctx-` (context), `c4-` (C4), `seq-` (sequence), `df-` (dataflow), `ui-` (screenshot)
- 🚫 Avoid spaces and “final_v2_reallyfinal” file names 😅

---

## 🔗 How to reference assets from an ADR

### Embed an image
```md
![Request flow from UI to API](./assets/adr-0032-api-boundary/request-flow.svg)

*Figure: UI → API request flow for the chosen boundary.*
```

### Link to a supporting file
```md
[Decision matrix (CSV)](./assets/adr-0032-api-boundary/decision-matrix.csv)
```

### Link to a shared diagram (cross-ADR)
```md
[Shared architecture diagrams](../diagrams/)
```

> ♿ **Accessibility:** always include meaningful alt text for images, and add a one-line description/caption when the image carries important meaning.

---

## 🧩 Formats we accept

| Asset type | Preferred | Also OK | Notes |
|---|---|---|---|
| Diagrams | `.svg` ✅ | `.png` | SVG scales cleanly & diff-friendly(ish) |
| Diagram sources | `.mmd` / `.drawio` / `.puml` | `.dot` | Keep the “source” alongside exports |
| Screenshots | `.png` | `.jpg` | Optimize size; crop to what matters |
| Small evidence snippets | `.csv` / `.json` | `.md` | Keep small & directly relevant |
| Short logs | `.txt` / `.md` | — | Put long logs behind `<details>` in ADR |

---

## 🧪 Reproducibility standard

If an asset is derived (charts, benchmark plots, generated diagrams), include **how to regenerate it**:

- Add `REPRODUCE.md` in the ADR asset folder, or
- Add a short “Reproduce” section in the ADR and link to scripts/notebooks.

Recommended minimal `REPRODUCE.md` template:

```md
# Reproduce

## Inputs
- data: `data/<domain>/processed/...`
- script: `mcp/runs/<run-id>/...` or `pipelines/<name>/...`

## Steps
1. `make <target>` or run `<command>`
2. Output files:
   - `request-flow.svg`
   - `latency-plot.png`

## Notes
- Any fixed seeds, versions, or environment assumptions.
```

---

## 🧭 Architecture reminders for diagrams in ADRs

KFM diagrams and decision evidence should reflect the project’s core “pipeline → catalog → database → API → UI” approach.

- 🔁 **Data flow should not skip** provenance/catalog steps.
- 🧱 **UI ↔ DB coupling is a red flag** (UI should go through the API boundary).
- 🧭 If your ADR proposes changing these, call it out explicitly and justify the tradeoff.

Helpful references:
- 📘 `docs/MASTER_GUIDE_v13.md`
- 🧾 `docs/standards/` (STAC/DCAT/PROV profiles)
- 🛡️ `docs/governance/` (ethics, sovereignty, review gates)

---

## ✅ PR checklist (assets)

- [ ] Asset lives in the correct `assets/<adr-slug>/` folder
- [ ] Filenames are clear, kebab-case, and stable
- [ ] Images are reasonably sized (optimized + cropped)
- [ ] ADR uses **relative links** that render on GitHub
- [ ] Image has meaningful alt text + (optional) short caption
- [ ] Sources / attribution included if needed
- [ ] If generated, **reproduction steps** are present (`REPRODUCE.md` or ADR section)
- [ ] No sensitive data, secrets, or restricted content

---

<details>
<summary>🧠 Pro tip: keep diagrams diffable</summary>

If a diagram can be expressed as Mermaid, consider placing the Mermaid block in the ADR itself and (optionally) exporting an SVG into this folder for reuse elsewhere.

- ✅ Mermaid = text-first, review-friendly
- ✅ SVG export = reusable in other docs

</details>
