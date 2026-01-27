# 🧾 build-info (GitHub Action)

<p align="left">
  <img alt="Type" src="https://img.shields.io/badge/type-github%20action-2ea44f?style=for-the-badge">
  <img alt="Purpose" src="https://img.shields.io/badge/purpose-build%20provenance-6f42c1?style=for-the-badge">
  <img alt="Output" src="https://img.shields.io/badge/output-build--info.json-0969da?style=for-the-badge">
</p>

Generate a **deterministic build manifest** (📄 `build-info.json`) during CI runs so every artifact can answer:

> **“What exactly produced this build?”** ✅

This is a *provenance-first* utility action designed to fit the Kansas Frontier Matrix (KFM) philosophy: traceability, reproducibility, and “show your work” metadata.

---

## ✨ What this action does

- ✅ Captures **Git metadata** (commit SHA, ref, branch/tag, repo)
- ✅ Captures **GitHub Actions run context** (run id/number/attempt, workflow, actor)
- ✅ Captures **build timestamp** (UTC) + runner identity (OS/arch)
- ✅ Optionally captures **toolchain versions** (Node/Python/etc.) when available
- ✅ Writes a **single machine-readable manifest** to the workspace
- ✅ Exposes useful values as **step outputs** (so later steps can tag artifacts, images, releases)

---

## 📦 Outputs

### Files (written to repo workspace)

By default, this action writes:

- `build/build-info.json` (recommended)
  - or wherever you set `output-file`

You should typically upload it as a workflow artifact and/or embed it into release bundles and containers.

### Step outputs (usable as `${{ steps.<id>.outputs.<name> }}`)

Common outputs:
- `version`
- `sha`
- `sha_short`
- `ref_name`
- `built_at`
- `json_path`

> 🧠 Tip: Treat these outputs as the “labels” and the JSON file as the “receipt”.

---

## 🧩 Inputs

| Input | Required | Default | Description |
|------|----------|---------|-------------|
| `output-file` | ❌ | `build/build-info.json` | Where to write the manifest (relative to repo root). |
| `format` | ❌ | `json` | `json` (future: `env` / `both` if needed). |
| `version` | ❌ | auto | Optional override. If omitted, the action should derive a version (ex: from tags) or fall back to a safe value. |
| `extra` | ❌ | empty | Optional extra metadata to merge (string or JSON). Keep secrets **out** of this. |

> If you expand/modify inputs in `action.yml`, update this table 🛠️.

---

## 🗂️ Expected folder layout

Typical patterns (choose one; keep it consistent):

### JavaScript Action (Node)
```text
.github/actions/build-info/
├─ action.yml
├─ package.json
├─ dist/
│  └─ index.js
└─ README.md   👈 you are here
```

### Composite Action (shell steps)
```text
.github/actions/build-info/
├─ action.yml
├─ scripts/
│  └─ build-info.sh
└─ README.md   👈 you are here
```

---

## 📄 Manifest schema

The manifest is intended to be **stable**, **portable**, and **safe** to publish.

<details>
  <summary><strong>Example: build/build-info.json</strong> (click to expand)</summary>

```json
{
  "name": "kfm-build",
  "version": "0.0.0+sha.1a2b3c4d5e6f",
  "builtAtUtc": "2026-01-27T00:00:00Z",
  "git": {
    "sha": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b",
    "shaShort": "1a2b3c4d5e6f",
    "ref": "refs/heads/main",
    "refName": "main"
  },
  "github": {
    "repository": "owner/repo",
    "workflow": "CI",
    "runId": "1234567890",
    "runNumber": "42",
    "runAttempt": "1",
    "actor": "octocat"
  },
  "runner": {
    "os": "Linux",
    "arch": "X64"
  },
  "toolchain": {
    "node": "20.x",
    "python": "3.11.x"
  },
  "extra": {}
}
```
</details>

### ✅ Schema principles
- **No secrets** (tokens, keys, connection strings, etc.)
- Prefer **strings + structured objects** (stable across environments)
- Keep it **monotonic** (adding new fields is OK; avoid breaking renames)

---

## 🚀 Usage

### 1) Basic usage (recommended)

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout 🧾
        uses: actions/checkout@v4

      - name: Build Info 🧾
        id: build_info
        uses: ./.github/actions/build-info
        with:
          output-file: build/build-info.json

      - name: Upload build manifest 📦
        uses: actions/upload-artifact@v4
        with:
          name: build-info
          path: build/build-info.json

      - name: Echo version 🔖
        run: |
          echo "Version: ${{ steps.build_info.outputs.version }}"
          echo "SHA:     ${{ steps.build_info.outputs.sha_short }}"
```

---

### 2) Use build-info to tag artifacts (zip / docker / releases)

```yaml
      - name: Build app 🏗️
        run: npm ci && npm run build

      - name: Package 📦
        run: |
          mkdir -p dist
          cp -r build dist/app
          cp build/build-info.json dist/build-info.json
          tar -czf dist/kfm-${{ steps.build_info.outputs.version }}.tar.gz -C dist app build-info.json
```

---

### 3) Add extra metadata (pipeline-friendly)

```yaml
      - name: Build Info 🧾
        id: build_info
        uses: ./.github/actions/build-info
        with:
          output-file: build/build-info.json
          extra: |
            {
              "datasetBundle": "kansas-frontier-matrix",
              "provenanceMode": "strict",
              "releaseChannel": "ci"
            }
```

---

## 🔐 Security notes

- ✅ Safe to upload publicly **if** you keep it to build metadata.
- ❌ Never include:
  - API keys / access tokens
  - private URLs with embedded credentials
  - internal IPs or sensitive infrastructure identifiers

> Rule of thumb: **If you wouldn’t print it on the artifact label, don’t put it in build-info.**

---

## 🧯 Troubleshooting

- **`version` is empty / weird**  
  Ensure tags are available (checkout depth, fetch tags) or pass `version:` explicitly.

- **`sha` looks wrong**  
  Confirm `actions/checkout@v4` ran before this action.

- **Manifest not found**  
  Verify `output-file` path and that the directory exists (or ensure the action creates it).

---

## 🧠 Why this exists in KFM

KFM treats provenance as a first-class feature. This action is a small but crucial building block:
it produces the “receipt” that helps connect builds, datasets, and deployments into a traceable chain ✅

---

## 🛠️ Maintainers

If you change:
- output schema
- input names
- default paths

…update this README **in the same PR** to keep CI “self-documenting” 📚✨