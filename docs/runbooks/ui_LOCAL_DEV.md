# KFM Explorer local development with MapLibre and Qwen readiness

**Status:** The repository-local Explorer, package-owned MapLibre adapter, deterministic bootstrap, loopback Governed API, and read-only Ollama inventory check are implemented. Live Explorer-to-API transport and Qwen-generated KFM answers remain `HOLD` until their contracts, evidence retrieval, policy gates, and tests are implemented.

> [!IMPORTANT]
> Keep `KFM_MODEL_RUNTIME=mock`. The browser must not call Ollama directly. A locally installed model is a development candidate, not KFM evidence or publication authority.

## Local path

Use:

```text
~/src/Kansas-Frontier-Matrix
```

This keeps source under the user account and outside system executable directories.

## Clone the implementation branch

```bash
mkdir -p "$HOME/src"
git clone --branch codex/local-kfm-qwen-maplibre-bootstrap-20260904 --single-branch \
  https://github.com/bartytime4life/Kansas-Frontier-Matrix.git \
  "$HOME/src/Kansas-Frontier-Matrix"
cd "$HOME/src/Kansas-Frontier-Matrix"
```

For an existing checkout, preserve local work first, then fetch and switch to the task branch.

## Prerequisites

- Linux; Ubuntu 24.04 is the primary target.
- Git.
- Python `>=3.11` with `venv` support.
- A user-owned nvm installation, or exact Node `22.23.2` already active.
- Network access during the explicit setup step only.

The script uses the repository-pinned `pnpm@11.17.0` through Corepack. Do not use privileged global npm installs to bypass the pins.

## Inspect, install, verify

Read-only inspection:

```bash
bash scripts/dev/bootstrap.sh --inspect
```

Install locked repository-local dependencies:

```bash
bash scripts/dev/bootstrap.sh --apply
```

Re-run the bounded verification profile without installing:

```bash
bash scripts/dev/bootstrap.sh --verify
```

Equivalent package commands are `pnpm run local:inspect`, `pnpm run local:setup`, and `pnpm run local:verify` after pnpm is active.

`--apply` may use nvm, Corepack/pnpm, and pip networks. It creates only user-owned Node state, `.venv/`, `node_modules/`, package caches, and ignored `.env` when absent. It does not install system packages, nvm, Ollama, GPU drivers, Chromium, or model weights. It refuses a dirty tracked worktree, symlinked local roots, unignored local output, unsafe `.env` permissions, lockfile rewrites, or a new unreviewed dependency build.

The current `pnpm-workspace.yaml` explicitly permits only the reviewed `esbuild@0.28.2` build entry. A new ignored build is a stop condition, not an invitation to approve interactively.

Optional browser installation and test:

```bash
pnpm --filter explorer-web exec playwright install chromium
pnpm --filter explorer-web test:browser
```

## Start the MapLibre Explorer

Terminal 1:

```bash
cd "$HOME/src/Kansas-Frontier-Matrix"
nvm use 22.23.2
pnpm run local:explorer
```

Open `http://127.0.0.1:5173/`.

The Explorer resolves renderer access through:

```text
apps/explorer-web
  -> @kfm/maplibre/vite-adapter
  -> packages/maplibre
  -> maplibre-gl@6.6.0
```

Do not add a second direct MapLibre dependency to the Explorer.

## Start the Governed API scaffold

Terminal 2:

```bash
cd "$HOME/src/Kansas-Frontier-Matrix"
. .venv/bin/activate
pnpm run local:api
```

This command explicitly binds `127.0.0.1:8080`, matching `.env.example`. The direct Python entry point retains its legacy fallback `127.0.0.1:8000` when variables are not supplied. Non-loopback binds are rejected.

Current read-only routes:

```bash
curl --fail --silent http://127.0.0.1:8080/bootstrap
curl --fail --silent http://127.0.0.1:8080/layers
curl --fail --silent http://127.0.0.1:8080/evidence
```

These routes remain fail-closed scaffolding. The current Explorer client is fixture-first and does not yet use live API transport.

## Install and check Ollama/Qwen separately

Ollama remains outside the repository bootstrap because installation, service setup, GPU behavior, model storage, and rollback are workstation-level decisions. Follow the current official Ollama Linux instructions, then verify:

```bash
ollama --version
ollama list
```

Stage the first bounded local candidate:

```bash
ollama pull qwen3:14b
```

Inspect KFM's planned diagnostic request:

```bash
pnpm run local:qwen:inspect
```

Verify the exact model is listed by loopback Ollama:

```bash
pnpm run local:qwen:verify
```

The helper sends one proxy-disabled, redirect-denied, bounded `GET /api/tags`. It never sends a prompt, invokes generation, changes KFM runtime configuration, or pulls a model.

## Current integration truth

| Capability | State |
|---|---:|
| Local Vite Explorer | **IMPLEMENTED** |
| Package-owned MapLibre `6.6.0` seam | **IMPLEMENTED / BOUNDED** |
| Loopback Governed API GET scaffold | **IMPLEMENTED / FAIL-CLOSED** |
| Ollama/Qwen inventory probe | **IMPLEMENTED / READ-ONLY** |
| Qwen model download | **OPERATOR ACTION** |
| Governed Ollama provider | **NOT IMPLEMENTED** |
| Explorer live API transport | **NOT IMPLEMENTED** |
| Spatial/evidence retrieval for prompts | **PROPOSED** |
| Validated model map actions | **PROPOSED** |
| Deployment or publication | **OUT OF SCOPE** |

## Next implementation order

1. Define a renderer-neutral `MapContext` projection for viewport, active layer IDs, selected public-safe feature IDs, and optional timeline bounds.
2. Define finite Governed API request/response contracts with `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes.
3. Implement public-safe spatial/evidence retrieval before model invocation.
4. Add a provider interface behind the Governed API while retaining the mock default.
5. Add an Ollama adapter that receives only governed context and returns an untrusted candidate interpretation.
6. Validate citations and policy state before returning an answer projection.
7. Add Explorer network transport only after negative-path tests are stable.
8. Permit only validated map actions such as zoom, highlight, and layer toggle—never arbitrary JavaScript.

The prohibited shortcut is:

```text
Browser --------X--------> Ollama
```

## Troubleshooting and rollback

- Dirty worktree: commit, branch, or stash intentional work before `--apply`.
- Node mismatch: use `nvm install 22.23.2 && nvm use 22.23.2`.
- Lockfile wants changes: stop and reconcile manifest/lock drift in review.
- New dependency build appears: stop and route the exact package/version through supply-chain review.
- Port 5173 or 8080 is occupied: stop the conflicting local process; do not bind publicly.
- Qwen readiness is blocked: start Ollama or explicitly run `ollama pull qwen3:14b`, then retry.

Stop services with `Ctrl+C`. To remove repository-local generated state after reviewing it:

```bash
cd "$HOME/src/Kansas-Frontier-Matrix"
rm -rf node_modules .venv apps/explorer-web/dist
rm -f .env  # only after confirming it contains nothing you need
```

The helper never removes shared Node caches, Ollama, or model weights automatically.
