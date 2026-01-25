# LICENSES 🧾 — Tileset: `<tileset_slug>`

![Scope](https://img.shields.io/badge/scope-3D%20Tiles%20%2F%20glTF-555)
![Provenance](https://img.shields.io/badge/provenance-required-success)
![Governance](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-informational)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-enforced-blue)
![Integrity](https://img.shields.io/badge/integrity-OCI%20digest%20%2B%20Cosign-9cf)

> [!IMPORTANT]
> This file is the **authoritative licensing + attribution manifest** for the tileset located at:
>
> 📁 `web/assets/3d/shared/models/tilesets/<tileset_slug>/`
>
> KFM’s overall stance: **the software is MIT**, but **datasets/outputs inherit the upstream license terms**, and combined works should default to **the most restrictive compatible license** among inputs. (See “Composite license rule” below.):contentReference[oaicite:0]{index=0}

---

## 📁 Package layout

```text
🌐 web/
└─ 🧰 assets/
   └─ 🧊 3d/
      └─ 🤝 shared/
         └─ 🏗️ models/
            └─ 🧩 tilesets/
               └─ 🏷️ <tileset_slug>/
                  ├─ 🗺️ tileset.json            (or 🧷 root entrypoint)
                  ├─ 📦 *.b3dm / 🧷 *.i3dm / ☁️ *.pnts / 🧊 *.glb / 🧵 textures/*  (as applicable)
                  └─ 🧾 meta/
                     ├─ 📜 LICENSES.md          👈 📍 you are here
                     ├─ 🔐 checksums.sha256     (recommended)
                     ├─ 🧪 run_manifest.json    (recommended)
                     ├─ 🧬 provenance.jsonld    (recommended)
                     └─ 🧷 sbom.*               (optional; if code is bundled)
```

---

## 🧩 Tileset identity

| Field | Value |
|---|---|
| Tileset slug | `<tileset_slug>` |
| Human name | `<tileset_title>` |
| Description | `<one_sentence_summary>` |
| Version | `<YYYY.MM.DD>` or `<semver>` |
| Build pipeline | `<pipeline_id>@<pipeline_version>` |
| Maintainer | `<name_or_team>` |
| Contact | `<email_or_issue_link>` |
| Last updated | `<YYYY-MM-DD>` |

> [!NOTE]
> KFM’s pipeline philosophy is “**ingest → validate → transform → publish**” with reproducibility artifacts like checksums/manifests and serialized run context for replayability.:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## ✅ What you must do if you use or redistribute this tileset

### 1) Keep required attributions visible
KFM is designed to surface **source + license + provenance** in the UI (e.g., layer/asset info dialogs and link-outs to original datasets).:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

### 2) Respect upstream license restrictions
Data shown or exported may include license constraints (e.g., *non-commercial*), which KFM expects to be tracked in metadata and warned about in UX when applicable.:contentReference[oaicite:5]{index=5}

### 3) Don’t leak sensitive locations or restricted cultural info
KFM explicitly calls out **location generalization**, access controls, and sensitivity tagging for sensitive sites/species/people, and expects CARE-aligned handling (including community authority to control).:contentReference[oaicite:6]{index=6}

### 4) This repo is “policy-gated”
Missing license fields or required metadata should fail closed via **policy-as-code** gates (OPA/Conftest), preventing merges until fixed.:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

---

## 📜 A. Declared license for *this tileset package*

> Fill these fields **before publishing**.

| Item | Value |
|---|---|
| Output license (SPDX) | `<SPDX_ID e.g., CC-BY-4.0>` |
| License URL | `<https://...>` |
| Copyright holder | `<name/entity>` |
| Copyright year(s) | `<YYYY>` |
| Attribution required | `Yes / No` |
| Commercial use allowed | `Yes / No / Conditional` |
| Redistribution allowed | `Yes / No / Conditional` |
| Derivative works allowed | `Yes / No / Conditional` |
| Notes | `<brief, plain-English restrictions>` |

**Composite license rule (KFM default):**  
If this tileset is produced from multiple sources, treat the output as governed by the **most restrictive compatible** upstream license and restrictions (e.g., mixing CC‑BY with CC‑BY‑NC yields CC‑BY‑NC obligations for the combined work).:contentReference[oaicite:9]{index=9}

---

## 🧾 B. Required attribution block

> Copy/paste-ready attribution for UI “Source” panels or dataset cards.

```text
<tileset_title> (<tileset_slug>)
License: <SPDX_ID> (<license_url>)
Sources: <Source A>; <Source B>; <Source C>
Attribution: <one-line attribution string required by upstream>
Built by: <pipeline_id>@<pipeline_version> — <maintainer/org>
Last updated: <YYYY-MM-DD>
```

KFM UI patterns include linking back to the **source dataset metadata** and showing provenance context in panels/dialogs.:contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}

---

## 🗃️ C. Upstream data sources (you MUST list every input)

> One row per upstream dataset or asset that contributed to this tileset.

| Source ID | Provider / Owner | Title | License (SPDX) | License URL | Required attribution | Retrieved from | Retrieved (UTC) | Transform notes | Sensitivity / restrictions |
|---|---|---|---|---|---|---|---:|---|---|
| `<kfm_dataset_id>` | `<org>` | `<dataset title>` | `<SPDX>` | `<url>` | `<text>` | `<url>` | `<YYYY-MM-DD>` | `<reprojected / simplified / decimated / merged>` | `<none / non-commercial / restricted / sensitive>` |
|  |  |  |  |  |  |  |  |  |  |

> [!TIP]
> KFM metadata conventions expect license info in records (e.g., **DCAT** `dct:license`), with SPDX-like strings such as `"CC-BY-4.0"` shown as an example format.:contentReference[oaicite:12]{index=12}

---

## 🧱 D. Embedded third‑party assets (models, textures, fonts)

> Only list items that are actually bundled in this tileset folder (not runtime libraries).

| Asset path | Type | Original author / owner | License (SPDX) | License URL | Attribution required | Modified? | Notes |
|---|---|---|---|---|---|---|---|
| `<relative/path/to/asset>` | `model/texture/font/etc.` | `<name>` | `<SPDX>` | `<url>` | `<text>` | `Yes/No` | `<e.g., resized texture, decimated mesh>` |
|  |  |  |  |  |  |  |  |

---

## 🔧 E. Build toolchain (for reproducibility)

Even when tools are not redistributed, KFM favors “auditability”: log **tool versions**, source URLs, and run context so builds can be repeated exactly.:contentReference[oaicite:13]{index=13}

| Tool / pipeline component | Version | Purpose | License | Notes |
|---|---:|---|---|---|
| `<tool>` | `<x.y.z>` | `<e.g., tiling, mesh conversion>` | `<license>` | `<optional>` |

---

## 🧬 F. Provenance, integrity, and artifact distribution

### F1) Run manifest + hashing
Recommended: generate a **run manifest** for every build and treat it as a governance artifact. Patterns include canonicalizing JSON and hashing it (self-fingerprinting) to create stable identifiers and idempotency keys.:contentReference[oaicite:14]{index=14}

### F2) Policy checks must fail closed
Policy-as-code gates should reject any change that adds/updates a dataset or tileset without required license/provider/sensitivity fields.:contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}

### F3) Optional: OCI artifact storage (ORAS + Cosign)
KFM proposes storing large geospatial artifacts (tilesets, models, etc.) as **OCI artifacts**, pulled by immutable digest, and verified with **keyless Cosign** signatures stored as OCI referrers.:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

Fill this in if applicable:

| Item | Value |
|---|---|
| OCI reference | `oci://<registry>/<org>/<repo>/<artifact>:<tag>` |
| Digest | `sha256:<digest>` |
| Media type | `<custom mediaType>` |
| Signature | `<cosign bundle/referrer>` |
| Provenance referrer | `<prov jsonld referrer>` |
| SBOM referrer | `<spdx/cdx referrer>` |

---

## 🛡️ G. Sensitivity + CARE / cultural protocols

KFM’s documentation emphasizes:
- **Sensitivity tagging** (including “confidential” style gating) and warnings in UX.:contentReference[oaicite:19]{index=19}
- **Location generalization** (fuzz/coarsen) for sites that could be harmed (e.g., looting risk).:contentReference[oaicite:20]{index=20}
- **CARE / Indigenous Data Sovereignty** expectations when data pertains to Indigenous communities (authority to control, ethics, etc.).:contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

If cultural heritage protocols apply, record them here:

| Protocol / label | Applies? | Link / identifier | Notes |
|---|---|---|---|
| Traditional Knowledge (TK) labels | `Yes/No` | `<url/id>` | `<terms / display requirements>` |
| Community restrictions beyond license | `Yes/No` | `<url/id>` | `<who to contact / how to request access>` |

KFM proposes explicitly supporting cultural protocols (e.g., TK Labels) and restricting access where needed.:contentReference[oaicite:23]{index=23}

---

## 🗺️ H. Viewer stack context (why this exists)

This tileset is intended to be rendered in KFM’s web experience, which includes:
- A modern UI that links back to dataset sources and shows provenance context in panels.:contentReference[oaicite:24]{index=24}
- A 3D map stack that includes Cesium for 3D globe/3D tiles rendering (and MapLibre GL JS for 2D time/layer interactions).:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

---

## ✅ I. Maintainer checklist (before publish)

- [ ] Output license declared in section **A**
- [ ] Every upstream input listed in section **C**
- [ ] Attribution block in **B** matches upstream requirements
- [ ] Sensitive location review completed (generalization/access controls applied if needed):contentReference[oaicite:27]{index=27}
- [ ] Policy gates pass (license/provider/sensitivity required fields):contentReference[oaicite:28]{index=28}
- [ ] `checksums.sha256` generated (recommended)
- [ ] `run_manifest.json` generated and hashed (recommended):contentReference[oaicite:29]{index=29}
- [ ] If OCI-published: digest recorded + Cosign verification information included:contentReference[oaicite:30]{index=30}

---

## 📚 Template provenance (project docs used)

> These docs inform the licensing, provenance, and governance conventions used here.

- :contentReference[oaicite:31]{index=31} **KFM – Comprehensive Technical Documentation** (software vs data licensing; sensitivity/location policy; 3D stack):contentReference[oaicite:32]{index=32}:contentReference[oaicite:33]{index=33}
- :contentReference[oaicite:34]{index=34} **KFM – Comprehensive Architecture, Features, and Design** (policy packs; license gates; UX source/license surfacing):contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}
- :contentReference[oaicite:37]{index=37} **KFM – Comprehensive UI System Overview** (source links + metadata panels):contentReference[oaicite:38]{index=38}
- :contentReference[oaicite:39]{index=39} **KFM Data Intake – Technical & Design Guide** (pipeline structure; checksums/manifests; DCAT license fields):contentReference[oaicite:40]{index=40}:contentReference[oaicite:41]{index=41}
- :contentReference[oaicite:42]{index=42} **KFM – AI System Overview** (evidence/provenance enforcement; governance & ethics):contentReference[oaicite:43]{index=43}
- :contentReference[oaicite:44]{index=44} **Innovative Concepts to Evolve KFM** (TK labels / cultural protocol + access controls):contentReference[oaicite:45]{index=45}
- :contentReference[oaicite:46]{index=46} **Additional Project Ideas** (OCI artifacts via ORAS; Cosign signatures; policy gates; run manifests):contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}
- :contentReference[oaicite:49]{index=49} **Open-Source Geospatial Historical Mapping Hub Design** (MapLibre + pipeline traceability patterns):contentReference[oaicite:50]{index=50}:contentReference[oaicite:51]{index=51}
- :contentReference[oaicite:52]{index=52} **Latest Ideas & Future Proposals** (future distribution + UX ideas to keep licensing/provenance intact):contentReference[oaicite:53]{index=53}

### 📦 Reference libraries (PDF portfolios)
The following are included in the project archive as **PDF portfolios** (may require Acrobat/Reader to extract embedded docs) and were consulted as background reference material:
- :contentReference[oaicite:54]{index=54} AI Concepts & more:contentReference[oaicite:55]{index=55}
- :contentReference[oaicite:56]{index=56} Maps / Virtual Worlds / Geospatial WebGL:contentReference[oaicite:57]{index=57}
- :contentReference[oaicite:58]{index=58} Various programming languages & resources:contentReference[oaicite:59]{index=59}
- :contentReference[oaicite:60]{index=60} Data management / architectures / data science / Bayesian methods:contentReference[oaicite:61]{index=61}

---

> [!DISCLAIMER]
> This file is for documentation and compliance workflow support and is **not legal advice**. If upstream licensing is unclear or conflicting, do not publish the tileset until clarified.

