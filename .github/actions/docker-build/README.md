# 🐳 `docker-build` (Composite GitHub Action)

[![Type](https://img.shields.io/badge/type-composite%20action-2ea44f?logo=githubactions&logoColor=white)](#)
[![Purpose](https://img.shields.io/badge/purpose-docker%20build%20%2B%20(optional)%20push-0b5fff?logo=docker&logoColor=white)](#)

A reusable **composite GitHub Action** that standardizes how this repo **builds** (and optionally **pushes**) Docker images with **BuildKit/Buildx**, **cache**, and consistent **tags/labels**.

> ✅ Use this to keep workflows DRY: all Docker builds (API, web, pipelines, etc.) follow the same playbook.

---

## 📁 Location

```text
.github/
└─ actions/
   └─ docker-build/
      ├─ action.yml
      └─ README.md   👈 you are here
```

Use it in a workflow like:

```yaml
uses: ./.github/actions/docker-build
```

---

## ✨ What this action does

Typical flow (inside the composite action):

1. 🧰 Sets up Docker Buildx (BuildKit)
2. 🔐 (Optional) Logs into a registry (GHCR/Docker Hub/other) when `push: true`
3. 🏷️ Generates tags/labels (or accepts your custom tags)
4. 🏗️ Builds (and optionally pushes) an image
5. 📤 Exposes helpful outputs (image ref / digest / resolved tags)

---

## ✅ Recommended usage

### 🟦 Minimal: build-only (PRs, local validation)

```yaml
- name: Build (no push)
  uses: ./.github/actions/docker-build
  with:
    image: ghcr.io/${{ github.repository }}/api
    context: ./api
    file: ./api/Dockerfile
    push: false
```

### 🟩 Build + push to GHCR (main / tags)

```yaml
permissions:
  contents: read
  packages: write

steps:
  - uses: actions/checkout@v4

  - name: Build & push
    uses: ./.github/actions/docker-build
    with:
      image: ghcr.io/${{ github.repository }}/api
      context: ./api
      file: ./api/Dockerfile
      push: true
      registry: ghcr.io
      username: ${{ github.actor }}
      password: ${{ secrets.GITHUB_TOKEN }}
      tags: |
        type=ref,event=branch
        type=ref,event=tag
        type=sha
```

---

## 🔧 Inputs

> ℹ️ Inputs below describe the **expected contract** for `action.yml`. If you change `action.yml`, update this table too.

| Input | Required | Default | Description |
|---|---:|---|---|
| `image` | ✅ | — | Image name/repo (ex: `ghcr.io/org/repo/api`) |
| `context` | ⛔ | `.` | Build context directory |
| `file` | ⛔ | `Dockerfile` | Path to Dockerfile |
| `push` | ⛔ | `false` | If `true`, pushes built image to registry |
| `platforms` | ⛔ | `linux/amd64` | Build platforms (ex: `linux/amd64,linux/arm64`) |
| `tags` | ⛔ | *(auto)* | Tag rules or explicit tags (see “Tagging”) |
| `labels` | ⛔ | *(auto)* | OCI labels or additional labels |
| `build-args` | ⛔ | — | Newline-separated `KEY=VALUE` build args |
| `target` | ⛔ | — | Multi-stage target (if your Dockerfile uses `target`) |
| `cache` | ⛔ | `true` | Enables BuildKit cache via GitHub Actions cache (`type=gha`) |
| `cache-from` | ⛔ | `type=gha` | Advanced override for cache source |
| `cache-to` | ⛔ | `type=gha,mode=max` | Advanced override for cache destination |
| `registry` | ⛔ | `ghcr.io` | Registry host (ex: `ghcr.io`, `docker.io`) |
| `username` | ⚠️ | — | Registry username (required when `push: true`) |
| `password` | ⚠️ | — | Registry password/token (required when `push: true`) |
| `provenance` | ⛔ | `false` | Enable BuildKit provenance attestation (if wired in `action.yml`) |
| `sbom` | ⛔ | `false` | Enable SBOM generation (if wired in `action.yml`) |

> ⚠️ `username/password` are only needed when pushing. For GHCR, `secrets.GITHUB_TOKEN` usually works with `packages: write`.

---

## 📤 Outputs

| Output | Description |
|---|---|
| `image` | Fully-qualified image name that was built |
| `tags` | Resolved tags that were applied |
| `digest` | Image digest (when pushing, or when supported by build driver) |

---

## 🏷️ Tagging

This action is designed to support either:

### Option A) **Rules-based tags** (recommended)
Using Docker metadata-style rules:

```yaml
with:
  tags: |
    type=ref,event=branch
    type=ref,event=tag
    type=sha
```

### Option B) **Explicit tags**
You can pass explicit tags instead (example: two tags):

```yaml
with:
  tags: |
    ghcr.io/${{ github.repository }}/api:latest
    ghcr.io/${{ github.repository }}/api:${{ github.sha }}
```

> ✅ Pick one approach and keep it consistent across services.

---

## 🧩 Common patterns

### 1) 🧱 Build multiple images with a matrix
Great for monorepos (API + Web + Workers):

```yaml
strategy:
  matrix:
    include:
      - name: api
        context: ./api
        dockerfile: ./api/Dockerfile
      - name: web
        context: ./web
        dockerfile: ./web/Dockerfile

steps:
  - uses: actions/checkout@v4

  - name: Build & push ${{ matrix.name }}
    uses: ./.github/actions/docker-build
    with:
      image: ghcr.io/${{ github.repository }}/${{ matrix.name }}
      context: ${{ matrix.context }}
      file: ${{ matrix.dockerfile }}
      push: ${{ github.event_name != 'pull_request' }}
      registry: ghcr.io
      username: ${{ github.actor }}
      password: ${{ secrets.GITHUB_TOKEN }}
      tags: |
        type=ref,event=branch
        type=sha
```

### 2) 🧬 Multi-arch builds (amd64 + arm64)
```yaml
with:
  platforms: linux/amd64,linux/arm64
```

> 📝 Multi-arch builds usually require QEMU setup in `action.yml` (or in your workflow). If you see `exec format error`, that’s a hint QEMU isn’t enabled.

---

## 🔐 Permissions, secrets, and registry notes

### ✅ GHCR (recommended for GitHub-hosted projects)
Add this to your workflow:

```yaml
permissions:
  contents: read
  packages: write
```

Then use:

- `registry: ghcr.io`
- `username: ${{ github.actor }}`
- `password: ${{ secrets.GITHUB_TOKEN }}`

### 🐳 Docker Hub
Use Docker Hub username + access token:

- `registry: docker.io`
- `username: ${{ secrets.DOCKERHUB_USERNAME }}`
- `password: ${{ secrets.DOCKERHUB_TOKEN }}`

---

## 🛡️ Security tips (supply chain & sanity) 🔒

- ✅ **Use `.dockerignore`** aggressively to reduce context size and accidental secret leakage.
- ✅ Prefer **build secrets** over build args for tokens (if supported by your `action.yml`).
- ✅ Pin external actions in `action.yml` (e.g., `docker/build-push-action@<major>` at minimum).
- ✅ Consider enabling **provenance/SBOM** for release builds (`provenance: true`, `sbom: true`) if you’ve wired that up.
- 🧼 Keep images small: multi-stage builds, slim bases, clean caches.

---

## 🧯 Troubleshooting

### “denied: permission_denied: write_package”
- You’re pushing to GHCR without `packages: write`, or your token isn’t allowed.
- Fix: add workflow permissions and ensure `password` uses a token with packages scope.

### “failed to solve: rpc error: … no space left on device”
- Docker build cache bloated on hosted runner.
- Fix: reduce context, prune layers, or tune cache settings.

### Builds are slow / cache misses
- Ensure `cache: true` and avoid changing build context files unnecessarily.
- Confirm your Dockerfile ordering: put less-changing layers first (dependencies before app code).

---

## 🧪 Local equivalent (for debugging)

From repo root:

```bash
docker build -f ./api/Dockerfile ./api -t local/api:dev
```

Or multi-stage target:

```bash
docker build -f ./api/Dockerfile ./api --target runtime -t local/api:runtime
```

---

## 🧑‍🔧 Maintainer notes

- Keep `README.md` and `action.yml` **in sync** ✅
- If you add a new input to `action.yml`, document it here (and add an example).
- If you change tag strategy, update all workflows that reference this action to avoid drift.

---