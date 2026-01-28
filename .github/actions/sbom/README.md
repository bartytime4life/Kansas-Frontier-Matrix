<div align="center">

# 🧾 SBOM Composite Action

Generate a **Software Bill of Materials (SBOM)** for KFM builds & releases — with **repeatable filenames**, CI-friendly outputs, and “fail-closed” defaults ✅

![GitHub Action](https://img.shields.io/badge/GitHub%20Action-composite-2ea44f?logo=githubactions&logoColor=white)
![SBOM](https://img.shields.io/badge/SBOM-enabled-success)
![SPDX](https://img.shields.io/badge/SPDX-JSON-informational)
![CycloneDX](https://img.shields.io/badge/CycloneDX-JSON-informational)
![Supply Chain](https://img.shields.io/badge/Supply%20Chain-hardened-blue)

</div>

> 🧠 **Context (KFM):** SBOMs are part of KFM’s “provenance over vibes” posture — releases should ship with **manifest + provenance + SBOM** so downstream users can verify what they’re running.

---

## 🔗 Quick links

- ⬅️ Back to **`.github/` overview**: `../../README.md`
- ⚙️ Action definition: `./action.yml`
- 🛡️ Security policy: `../../SECURITY.md`

---

## ✨ What this action does

This composite action is a reusable wrapper you can call from workflows to:

- 📦 Generate an SBOM for:
  - a **source directory** (monorepo / subproject), **or**
  - a **container image** (post-build)
- 🧾 Output SBOM(s) in a predictable location (so CI + releases can depend on them)
- ⬆️ Optionally upload SBOM files as workflow artifacts
- 🚫 **Fail closed** by default: if SBOM generation fails, the job fails (unless you explicitly opt out)

---

## 🗂️ Folder layout

```text
.github/actions/sbom/
├─ action.yml          # Action contract (inputs/outputs)
└─ README.md           # You are here 🧾
```

---

## ✅ Recommended conventions (KFM-style)

KFM typically treats SBOMs as **release-grade artifacts**:

- 📁 Recommended output folder: `releases/<version>/`
- 🧾 Recommended filenames:
  - `sbom.spdx.json`
  - `sbom.cdx.json` (CycloneDX)

> 💡 Tip: If you’re already producing a `manifest.json`, include a pointer to SBOM paths there for “one-glance” verification.

---

## 🧩 Inputs

> ⚠️ **Note:** Keep this table aligned with `action.yml`. If you rename inputs there, update this README too.

| Input | Type | Default | Description |
|---|---:|---|---|
| `mode` | string | `dir` | What to generate an SBOM for: `dir` or `image` |
| `path` | string | `.` | Directory to scan when `mode=dir` |
| `image` | string | _(empty)_ | Image reference (e.g., `ghcr.io/org/app:sha`) when `mode=image` |
| `formats` | string | `spdx-json` | Comma-separated formats (e.g., `spdx-json,cyclonedx-json`) |
| `output-dir` | string | `.` | Where SBOM files should be written |
| `basename` | string | `sbom` | Base filename (without extension/format), e.g. `sbom` |
| `upload-artifact` | boolean | `true` | Upload SBOM file(s) as workflow artifact(s) |
| `artifact-name` | string | `sbom` | Artifact name for uploaded SBOM(s) |
| `retention-days` | number | `14` | Artifact retention (days) |
| `fail-on-error` | boolean | `true` | If `true`, fail workflow when SBOM generation fails |

---

## 📤 Outputs

| Output | Example | Description |
|---|---|---|
| `sbom_paths` | `./releases/v1.2.3/sbom.spdx.json,./releases/v1.2.3/sbom.cdx.json` | Comma-separated list of generated SBOM file paths |
| `primary_sbom` | `./releases/v1.2.3/sbom.spdx.json` | The “main” SBOM path (first format) |

---

## 🚀 Usage examples

### 1) Generate an SBOM for the repo (directory scan) 📁

```yaml
jobs:
  sbom:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM (dir)
        uses: ./.github/actions/sbom
        with:
          mode: dir
          path: .
          formats: spdx-json,cyclonedx-json
          output-dir: releases/${{ github.ref_name }}
          basename: sbom
          upload-artifact: true
          artifact-name: sbom-${{ github.ref_name }}
```

---

### 2) Generate an SBOM for a container image 🐳

```yaml
jobs:
  build-and-sbom:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: |
          docker build -t kfm:${{ github.sha }} .

      - name: Generate SBOM (image)
        uses: ./.github/actions/sbom
        with:
          mode: image
          image: kfm:${{ github.sha }}
          formats: spdx-json
          output-dir: releases/${{ github.sha }}
          basename: sbom
```

> 💡 If you publish images to GHCR, consider using the immutable digest (e.g., `@sha256:...`) for tighter traceability.

---

### 3) Use outputs in downstream steps 🔁

```yaml
- name: Generate SBOM
  id: sbom
  uses: ./.github/actions/sbom
  with:
    mode: dir
    path: api
    formats: spdx-json
    output-dir: releases/${{ github.ref_name }}
    basename: api-sbom

- name: Print SBOM path(s)
  run: |
    echo "Primary SBOM: ${{ steps.sbom.outputs.primary_sbom }}"
    echo "All SBOMs:     ${{ steps.sbom.outputs.sbom_paths }}"
```

---

## 🔐 Permissions

### Minimal recommended permissions ✅
Most SBOM generation only needs repo read access:

```yaml
permissions:
  contents: read
```

### If you add attestations later 🧾🔏
If you extend workflows to sign/attest SBOMs using OIDC, you’ll typically need:

```yaml
permissions:
  contents: read
  id-token: write
```

> 🧯 Principle: keep permissions **as small as possible**. Start minimal and add only what’s required.

---

## 🧯 Troubleshooting

### “No SBOM files produced”
- ✅ Confirm `mode` matches what you intended (`dir` vs `image`)
- ✅ Confirm `output-dir` exists or is creatable by the runner
- ✅ Confirm the underlying SBOM tool is available in the runner environment (or installed by the action)

### “Permission denied” writing outputs
- Use a workspace-relative `output-dir`
- Avoid writing into protected directories on hosted runners

### Large SBOMs / slow runs
- Consider scanning **subprojects** (e.g., `api/`, `web/`) separately
- Prefer image SBOMs **after** dependency install/build so results match the shipped artifact

---

## 🧭 Definition of Done (SBOM quality gates)

When SBOMs matter for a release, aim for:

- ✅ SBOM generated for **the actual shipped artifact** (directory vs image chosen intentionally)
- ✅ Stored under `releases/<version>/`
- ✅ Included as build artifact (and/or release asset)
- ✅ Referenced from the release manifest / provenance record (when applicable)

---

## 🧑‍🔧 Maintaining this action

- 🔁 Keep the contract in **`action.yml`** and this README in sync
- 📌 Pin third-party actions/tools (when used) to a tag or (ideally) a commit SHA
- 🧪 Add a small workflow that validates SBOM generation on PRs (fast + cheap)

---

<p align="center">
  🧾 <strong>SBOMs aren’t a checkbox — they’re a map 🗺️</strong><br/>
  Make it easy to verify what we ship, every time ✅
</p>
