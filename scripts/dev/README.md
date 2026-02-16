# scripts/dev

![status](https://img.shields.io/badge/status-dev%20helpers-informational)
![governance](https://img.shields.io/badge/governance-trust%20membrane%20%2B%20promotion%20gates-blue)
![safety](https://img.shields.io/badge/safety-safe--by--default-important)

Local, developer-only helper scripts that make **KFM** development repeatable, safer, and closer to CI/prod behavior.

> [!IMPORTANT]
> **KFM invariants apply in dev scripts too.**
> - **Trust membrane:** the UI and external clients must not touch databases directly; access is mediated by the governed backend API + policy boundary.
> - **Promotion gates:** data must move through zones (Raw → Work → Processed) with deterministic checksums and catalogs (STAC/DCAT/PROV) before it is considered “usable”.
> - **Evidence-first AI:** Focus Mode must cite or abstain; dev scripts should never “fake” provenance or bypass policy checks.
>
> If a script would violate these invariants, it belongs in a different place (or needs governance review), not in `scripts/dev/`.

---

## Directory intent

This folder is for **developer convenience**, not production automation.

- ✅ OK here: one-liners and wrappers for local dev (compose up/down, log tailing, local resets, running a pipeline against a small fixture slice, lint/test helpers).
- ❌ Not OK here: “secret” backdoors that write directly to processed datasets or databases, bypass catalog/provenance generation, or disable policy checks “just for dev”.

---

## Quick start

### 1) Start the local stack (baseline)

Most KFM dev workflows assume a local multi-service stack (e.g., PostGIS + Neo4j + API + web UI) running under Docker Compose.

```bash
# from repo root
docker-compose up --build
```

> [!TIP]
> Keep the compose stack running while you develop; use another terminal for scripts, tests, and pipeline runs.

### 2) Run a one-off pipeline / management task

Prefer executing pipeline commands **inside** the API container so you’re using the same deps and mounted volumes as the running stack.

```bash
docker-compose exec api python pipelines/<your_pipeline>.py
```

### 3) Explore the API (trust membrane in practice)

Use the API surface for verification and debugging (not direct DB poking from the UI).

```text
Swagger/OpenAPI (if enabled): http://localhost:8000/docs
GraphQL (if enabled):         http://localhost:8000/graphql
```

---

## Script registry

> [!NOTE]
> Keep this table current. The goal is to make scripts discoverable and auditable.

| Script | Purpose | Safe-by-default | Destructive? | Requires running stack? | Notes |
|---|---:|:---:|:---:|:---:|---|
| *(add scripts here)* |  |  |  |  |  |

---

## Conventions (required)

### Safety defaults

All dev scripts **must** be safe-by-default:

- **No destructive actions** unless explicitly opted-in.
- Prefer a `--dry-run` mode.
- Require `--yes` (or similar) for deletes/resets.
- Hard-stop unless `KFM_ENV=dev` (or equivalent) is set for destructive operations.

Example safety pattern:

```bash
# bash
set -euo pipefail

: "${KFM_ENV:=dev}"

if [[ "${KFM_ENV}" != "dev" ]]; then
  echo "Refusing to run: KFM_ENV=${KFM_ENV} (expected 'dev')" >&2
  exit 2
fi
```

### Script interface

Each script should support:

- `--help`
- `--dry-run` (when meaningful)
- deterministic output paths (don’t scatter files)
- clear exit codes

Recommended standard header in each script:

```text
Purpose:
Inputs:
Outputs:
Side effects:
Governance notes (trust membrane / promotion gates / policy):
```

### Logging

- Prefer writing logs to a predictable dev-only location, e.g. `.kfm/dev-logs/<script>/<timestamp>.log`.
- Log the **command**, **git commit**, and **run id** (even if local-only).

---

## Governance alignment checklist

Use this checklist when adding/updating scripts:

- [ ] Does the script preserve the **trust membrane** (no UI→DB shortcuts; no external client→DB shortcuts)?
- [ ] If it touches data lifecycles, does it respect **Raw → Work → Processed** promotion gates and produce required catalogs (STAC/DCAT/PROV) or call the pipeline that does?
- [ ] If it calls Focus Mode or AI tooling, does it remain **evidence-first** (cite or abstain) and avoid fabricating provenance?
- [ ] Is the script safe-by-default and clearly labeled if destructive?
- [ ] Is the script idempotent (or explicitly documented as not)?
- [ ] Did you add/update the **Script registry** table above?

---

## Suggested layout (optional, but recommended)

If this folder grows, organize by intent:

```text
scripts/dev/
  README.md
  stack/        # compose wrappers: up/down/logs/exec
  db/           # local-only resets, migrations, seed fixtures
  pipeline/     # run a pipeline on fixtures; validate; profile
  policy/       # run policy tests / bundle checks
  docs/         # link-check, markdown lint, story-node validation
```

---

## Troubleshooting tips

### Port conflicts / containers not ready
- If something already uses `5432` (Postgres), `7474` (Neo4j), or `3000/8000` (web/API), stop it or change compose port mappings.
- If the API starts before DB is ready, check logs and restart the stack.

### Volume permissions
On some hosts, mounted volumes can cause permission errors when containers write to `data/` or other bind mounts. Ensure host folders are writable or adjust container user settings.

---

## When to *not* use `scripts/dev`

- Anything intended for CI/CD should live in the CI pipeline definitions (and/or a dedicated `tools/` or `pipelines/` automation surface).
- Anything that changes **governed** datasets should be implemented as a pipeline step with validation gates and provenance artifacts, not a “handy” dev script.

---

## References

- **KFM Comprehensive Data Source Integration Blueprint** (invariants: trust membrane, promotion gates, evidence-first Focus Mode)
- **KFM Comprehensive Technical Blueprint** (canonical pipeline order; dev stack via Docker Compose; running one-off pipeline tasks)
