# 📄 PDF Figures (Experiment Artifacts)

![Artifacts](https://img.shields.io/badge/artifacts-figures%2Fpdf-blue)
![Format](https://img.shields.io/badge/format-PDF%20(vector%20preferred)-informational)
![Traceability](https://img.shields.io/badge/traceability-provenance%20sidecars-success)
![Template](https://img.shields.io/badge/template-experiment%20report-orange)

This folder contains **print-ready PDF** versions of figures referenced by the experiment report.

- ✅ **Vector-first** (preferred): crisp at any zoom, selectable text
- ✅ **Paired PNG preview** (recommended): for GitHub rendering in `../png/`
- ✅ **Evidence-first**: every figure is reproducible + provenance-linked
- ✅ **Governed**: license + sensitivity labels required

**Quick navigation:**  
[⬅️ figures/](../) • [🖼️ PNG previews](../png/) • [📦 artifacts/](../../) • [🏠 report root](../../../)

---

## Folder contract ✅

> [!NOTE]
> This folder is a **results container**. If you can’t explain *exactly* how a PDF was produced (inputs, code, parameters), it doesn’t belong here.

### ✅ Put these here
- 📄 `fig-*.pdf` — the PDF figures used in the report (maps, plots, diagrams)
- 🧾 `fig-*.meta.yml` — caption + license + sensitivity + IDs (required)
- 🧬 `fig-*.prov.jsonld` — PROV lineage bundle (required)
- 🔐 `checksums.sha256` — optional but strongly recommended (folder-level)

### 🚫 Don’t put these here
- 🧱 raw datasets / intermediate data extracts (those belong in the data pipeline, not report artifacts)
- 🧪 debugging screenshots or “draft” exports not used in the report
- 🔑 anything containing secrets, tokens, private URLs, or restricted info

---

## Add or update a figure 🧩

1. **Generate** the figure from code or a deterministic workflow (avoid manual “hand edits”).
2. **Export**
   - 📄 `PDF` (vector-first; embed fonts)
   - 🖼️ `PNG` preview to `../png/` (**same basename**)
3. **Create sidecars**
   - 🧾 `*.meta.yml`
   - 🧬 `*.prov.jsonld`
4. **Update checksums** (if using `checksums.sha256`)
5. **Reference** the figure in the experiment report (PNG inline, PDF linked)

<details>
<summary>📁 Minimal example bundle (click)</summary>

📁 artifacts/figures/  
├─ 📁 pdf/  
│  ├─ 📄 fig-010__pipeline-overview__v1.pdf  
│  ├─ 🧾 fig-010__pipeline-overview__v1.meta.yml  
│  ├─ 🧬 fig-010__pipeline-overview__v1.prov.jsonld  
│  └─ 🔐 checksums.sha256  
└─ 📁 png/  
   └─ 🖼️ fig-010__pipeline-overview__v1.png  

</details>

---

## Naming convention 🏷️

Use a stable ID + a human-readable slug:

`fig-<NNN>__<slug>__v<MAJOR>.<ext>`

| Part | Example | Rule |
|---|---|---|
| `<NNN>` | `010` | 3 digits, unique within the report |
| `<slug>` | `pipeline-overview` | kebab-case, describe intent |
| `v<MAJOR>` | `v1` | bump when meaning/data changes (not tiny styling) |
| `<ext>` | `pdf` / `png` / `meta.yml` / `prov.jsonld` | keep the **same basename** |

> [!TIP]
> If a figure is replaced, **don’t overwrite** the old file silently. Bump the major version and keep prior versions for auditability.

---

## Sidecar metadata 🧾🔎

### `*.meta.yml` (required)

This is for humans + reviewers. Keep it concise, but complete.

```yaml
id: fig-010
title: Pipeline overview
caption: >
  End-to-end experiment pipeline showing how inputs flow through validation,
  provenance, and outputs. (See linked provenance for exact inputs + parameters.)

created_at: "YYYY-MM-DDThh:mm:ssZ"
created_by: "@your-handle"

experiment_id: "exp-010"
run_id: "run-YYYYMMDD-<short-hash>"

# Evidence links (prefer stable IDs if available)
inputs:
  - kind: dataset
    ref: "dcat:<dataset-id>"
  - kind: asset
    ref: "stac:item:<item-id>"
  - kind: code
    ref: "git:<commit-sha>"

# Reproducibility hints (optional but recommended)
toolchain:
  - "python==3.12.x"
  - "matplotlib==x.y.z"
  - "gdal==x.y.z"
  - "node==20.x"  # if generated via JS tooling
random_seed: 12345           # if applicable
parameters_ref: "../params/run-YYYYMMDD-<hash>.yml"

# Governance (required)
license: "CC-BY-4.0"
attribution: "USGS (example); KFM pipeline (example)."
sensitivity: "public"        # public | sensitive | confidential | restricted
redaction: "none"            # none | generalized | masked | aggregated

# AI disclosure (required when applicable)
ai_assisted: false
ai:
  model: null
  prompt_ref: null
  citations_required: true

notes: "Vector export; PNG preview generated from PDF."
```

**Minimum required fields**
- `id`, `title`, `caption`
- `license` (and attribution notes when needed)
- `sensitivity` (and redaction/generalization notes if needed)
- `experiment_id` and/or `run_id`

> [!IMPORTANT]
> If this figure supports a claim, the claim must remain **traceable**: include stable evidence references (DCAT/STAC IDs, dataset identifiers, or other governed IDs) in `inputs`.

### `*.prov.jsonld` (required)

This is for machines (and audits). At minimum, capture:
- **Entity**: the PDF (and PNG) outputs
- **Activity**: the generation step (script/notebook/UI export)
- **Agents**: person + toolchain (software versions)
- **Inputs**: datasets/catalog IDs + parameter files
- **Parameters**: configs, thresholds, seeds, bounding boxes, time ranges, etc.

> [!NOTE]
> Provenance is not “extra paperwork” — it’s how we keep figures defensible and reproducible.

---

## Referencing PDFs in the report 🔗

GitHub previews PNG best, so embed the PNG and link the PDF:

```md
[![Figure 10 — Pipeline overview](artifacts/figures/png/fig-010__pipeline-overview__v1.png)](artifacts/figures/pdf/fig-010__pipeline-overview__v1.pdf)

*Figure 10.* Pipeline overview. License + provenance in:
`artifacts/figures/pdf/fig-010__pipeline-overview__v1.meta.yml`
```

> [!TIP]
> If your report generator supports it, auto-build a “List of Figures” from `*.meta.yml` captions to keep everything consistent.

---

## Quality bar 🧪✨

Before committing a PDF:

- [ ] **Vector-first** (text selectable; lines crisp)
- [ ] **Fonts embedded** (no missing glyphs on other machines)
- [ ] **Readable at print size** (legends not microscopic)
- [ ] **Accessible** (don’t rely on color alone; add labels/patterns)
- [ ] **Map exports** include: scale, north, projection/CRS (if relevant), date range, and source attribution
- [ ] **No secrets / internal-only URLs** in annotations or metadata

---

## Governance & sensitivity 🛡️

KFM-style governance applies to experiment artifacts too:

- 🔒 **No secrets in repo outputs** (PDFs count as outputs)
- 🧭 **No output may be less restricted than its inputs**
- 🧱 If inputs are sensitive/restricted, the figure must:
  - be labeled correctly (`sensitivity`)
  - be redacted/generalized (`redaction`)
  - include usage constraints in metadata

> [!WARNING]
> If a PDF figure reveals restricted data (even indirectly), treat it as an incident:
> remove/rotate the artifact as required, and document remediation in the experiment log.

---

## Corrections, deprecations, and “oops” moments 🧯

If a figure is wrong:
1. **Do not rewrite history silently**.
2. Create a new version (bump `v<MAJOR>`).
3. Mark the old one as deprecated in `*.meta.yml`, e.g.:
   - `status: deprecated`
   - `superseded_by: fig-010__...__v2.pdf`
   - `reason: corrected data join / fixed CRS / etc.`

This preserves the audit trail while keeping the report honest.

---

## Large artifacts & distribution 📦

If a PDF is huge or updated frequently:
- Prefer storing in **artifact storage** (e.g., DVC or an OCI registry) and keep a small pointer in-repo.
- For release-grade artifacts, consider signing + attaching provenance attestations.

---

## Design anchors (why this folder is strict) 🧭

<details>
<summary>📚 Evidence-first & provenance-first mindset (click)</summary>

This template treats figures like **first-class evidence artifacts**:
- results must be reproducible
- metadata must be explicit (license + sensitivity + provenance)
- AI-assisted outputs must be disclosed and source-linked

The “PDF figures” folder is intentionally small and strict so experiment reports remain trustworthy.

</details>

---

✅ _If you follow the contract above, figures stay printable, linkable, reviewable, and defensible._
