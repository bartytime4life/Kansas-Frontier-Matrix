<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/scripts-dev-readme
title: scripts/dev/ — Local Development Helper Boundary
type: directory-readme
version: v0.3
status: draft; repository-grounded; local-bootstrap-implemented; ollama-readiness-implemented; fixture-regeneration-placeholder; non-authoritative
owners: ["@bartytime4life — verified GitHub review route", "NEEDS VERIFICATION — developer-experience, security, runtime, and test stewards"]
created: 2026-07-16
updated: 2026-09-04
policy_label: "public; scripts; dev; local-only; no-production-authority; no-release-authority; no-secret-store; rollback-aware"
current_path: scripts/dev/README.md
owning_root: scripts/
responsibility: "Document and bound small repository-local development helpers without creating runtime, evidence, policy, release, deployment, or publication authority."
truth_posture: cite-or-abstain
related:
  - ../../docs/runbooks/ui_LOCAL_DEV.md
  - ../../apps/explorer-web/README.md
  - ../../apps/governed-api/README.md
  - ../../packages/maplibre/README.md
  - ../../runtime/ollama/README.md
  - ../../docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - "v0.3 replaces the bootstrap TODO with inspect, apply, and verify modes."
  - "v0.3 adds a read-only, loopback-only Ollama/Qwen inventory probe."
  - "regen_fixtures.sh remains a placeholder."
[/KFM_META_BLOCK_V2] -->

# `scripts/dev/` — Local Development Helper Boundary

Small, explicit, reversible helpers for setting up and checking a local KFM development checkout.

> [!IMPORTANT]
> This lane is convenience, not authority. A successful local command does not establish factual truth, source admission, evidence sufficiency, policy approval, review, release readiness, deployment, promotion, or publication.

> [!WARNING]
> Browser and public clients must not call Ollama directly. The model runtime remains subordinate to the Governed API, and the default repository posture remains `KFM_MODEL_RUNTIME=mock`.

## Inventory

| Path | State | Bounded role |
|---|---:|---|
| `bootstrap.sh` | **IMPLEMENTED / LOCAL** | Inspect, install, and verify repository-local Linux development dependencies. |
| `ollama-readiness.sh` | **IMPLEMENTED / READ-ONLY** | Check one loopback Ollama `/api/tags` response for an exact model name. |
| `regen_fixtures.sh` | **PLACEHOLDER** | Prints `TODO`; it does not regenerate or authorize fixtures. |

These helpers cannot change evidence, policy, review, release, deployment, or publication state; install system packages; store credentials; expose services beyond loopback; make model output authoritative; or commit, push, open, approve, or merge a pull request.

## Recommended checkout

```text
~/src/Kansas-Frontier-Matrix
```

```bash
mkdir -p "$HOME/src"
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git \
  "$HOME/src/Kansas-Frontier-Matrix"
cd "$HOME/src/Kansas-Frontier-Matrix"
```

The bootstrap does not clone the repository. It starts only after a checkout exists.

## Bootstrap contract

Read-only inspection:

```bash
bash scripts/dev/bootstrap.sh --inspect
```

Explicit installation:

```bash
bash scripts/dev/bootstrap.sh --apply
```

Installation-free verification:

```bash
bash scripts/dev/bootstrap.sh --verify
```

`--apply` is Linux-only and requires a Git checkout, a clean tracked worktree, Python `>=3.11`, and a user-owned nvm installation or an already active exact Node version. It selects Node `22.23.2`, enables the repository-pinned `pnpm@11.17.0` through Corepack, creates `.venv/`, installs declared Python dependencies, runs `pnpm install --frozen-lockfile`, creates ignored `.env` with owner-only permissions when absent, and then verifies the bounded local profile.

It never installs nvm, Ollama, GPU drivers, system packages, browsers, or model weights; never invokes privilege escalation; and never changes Git remotes, commits, branches, pull requests, or repository settings.

Verification checks the pinned runtime selections, ignored local state, private `.env` permissions, helper syntax and tests, Governed API tests, `@kfm/maplibre` tests, Explorer build and unit tests, and whitespace integrity. Playwright browser installation/tests remain an explicit operator step because Chromium is a material download.

## Ollama/Qwen readiness

Inspect the planned request:

```bash
bash scripts/dev/ollama-readiness.sh --inspect --model qwen3:14b
```

Verify local inventory:

```bash
bash scripts/dev/ollama-readiness.sh --verify --model qwen3:14b
```

The verifier permits only loopback HTTP, disables proxies and redirects, performs one bounded `GET /api/tags`, sends no prompt, invokes no generation endpoint, and never pulls a model. When the exact model is missing, it reports the operator command:

```bash
ollama pull qwen3:14b
```

Model presence does not authorize KFM to use it for public or evidence-bearing answers.

## Root commands and endpoints

```bash
pnpm run local:inspect
pnpm run local:setup
pnpm run local:verify
pnpm run local:qwen:inspect
pnpm run local:qwen:verify
pnpm run local:explorer
pnpm run local:api
```

| Service | Loopback address | Current role |
|---|---|---|
| Explorer Web | `http://127.0.0.1:5173/` | Canonical repository-local Vite shell. |
| Governed API | `http://127.0.0.1:8080/` | Existing fail-closed GET scaffold; not a model proxy. |
| Ollama | `http://127.0.0.1:11434/` | Separately installed local runtime; inventory check only. |

The Explorer continues to resolve MapLibre through `@kfm/maplibre` and its Vite adapter. Do not add a second direct `maplibre-gl` dependency to the Explorer.

## Rollback

Stop local services with `Ctrl+C`, then review and remove only local generated state:

```bash
rm -rf node_modules .venv apps/explorer-web/dist
rm -f .env  # only after confirming it contains no local work you need
```

Node/Corepack caches, Ollama, and model weights are deliberately not removed automatically because other projects may share them.
