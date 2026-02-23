<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/5bcb7f77-2c42-4b8d-9fe5-7a7ffcb5e3c4
title: configs/env/scripts — Environment scripts
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-23
updated: 2026-02-23
policy_label: public
related:
  - ../README.md # (if present) configs/env/README.md
  - ../../../README.md # repo root README (verify path)
tags: [kfm, configs, env, scripts]
notes:
  - This folder should contain ONLY non-secret automation that helps generate/validate environment configuration.
  - Update the Script Registry table whenever scripts are added/removed/renamed.
[/KFM_META_BLOCK_V2] -->

# `configs/env/scripts`
Environment bootstrap + validation scripts for KFM config (**no secrets**)

![Status](https://img.shields.io/badge/status-draft-yellow)
![Scope](https://img.shields.io/badge/scope-configs%2Fenv%2Fscripts-blue)
![Secrets](https://img.shields.io/badge/secrets-never_commit-red)

> **Purpose:** Make local/CI environment configuration repeatable, auditable, and safe by default (fail-closed checks; deterministic outputs; no secret leakage).

---

## Quick navigation
- [Purpose](#purpose)
- [Where this fits](#where-this-fits)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Directory layout](#directory-layout)
- [Script registry](#script-registry)
- [Usage](#usage)
- [Script contract](#script-contract)
- [Security and governance](#security-and-governance)
- [Change workflow](#change-workflow)
- [Troubleshooting](#troubleshooting)

---

## Purpose
This directory is for **small, composable scripts** that help developers and CI:
- validate that required environment variables are present and well-formed,
- render `.env` files (or equivalent) from **non-secret** templates + local overrides,
- prevent misconfiguration from silently propagating into Docker Compose / containers.

**Design intent:** the “trust membrane” starts early—configuration changes should be checked before they reach running services.

[Back to top](#configsenvironmentscripts)

---

## Where this fits
KFM commonly uses Docker Compose-style local development where a `.env` file (or similar) drives service configuration.

These scripts exist to make that **consistent**:
- same inputs → same output `.env`
- missing/unsafe inputs → **fail closed** (exit non-zero)
- human-readable diffs / dry-runs when changing config

[Back to top](#configsenvironmentscripts)

---

## What belongs here
**Acceptable inputs** (non-secret unless explicitly flagged and handled safely):
- `.env.example` / template files (placeholders only)
- schema/contract files describing expected variables (e.g., `env.schema.json`, `env.required.txt`)
- scripts for rendering/validating env configs (shell, python, node, etc.)
- CI helpers that validate env templates **without** needing real secrets

[Back to top](#configsenvironmentscripts)

---

## What must not go here
**Exclusions (hard rules):**
- ❌ real secrets (API keys, tokens, passwords, private URLs, certs)
- ❌ production-only secret material (even encrypted blobs) unless the repo policy explicitly permits it
- ❌ scripts that mutate production infrastructure by default
- ❌ scripts that print secrets to stdout/stderr or write them into logs/artifacts

If a script must handle sensitive values:
- require an explicit `--allow-sensitive` flag,
- default to redaction in output,
- document the policy label and obligations clearly.

[Back to top](#configsenvironmentscripts)

---

## Directory layout
> This is the **minimum** expected structure. Adjust to match the real repo, but keep this README and the registry current.

```text
configs/
  env/
    scripts/
      README.md               # you are here
      (your scripts here)     # e.g., validate, render, diff, doctor
      (optional) contracts/   # env variable schemas / allowlists
      (optional) templates/   # non-secret templates (preferred outside scripts/)
```

[Back to top](#configsenvironmentscripts)

---

## Script registry
> Keep this table accurate. CI and onboarding should be able to rely on it.

| Script | Purpose | Inputs | Outputs | Safe defaults | Called by |
|---|---|---|---|---|---|
| `TBD` | Validate env contract | `.env` path + contract | exit code + report | **fail closed** | dev / CI |
| `TBD` | Render `.env` from template | template + overrides | `.env` (local) | dry-run available | dev |
| `TBD` | Env “doctor” (common checks) | repo root + docker | diagnostics | read-only | dev |

### Registry entry template (copy/paste)
```md
| `script_name` | <1-liner> | <inputs> | <outputs> | <safety model> | <caller> |
```

[Back to top](#configsenvironmentscripts)

---

## Usage
### Run a script
From repo root:

```bash
cd configs/env/scripts

# list scripts
ls -la

# run script help (recommended convention)
./<script> --help  # or: python <script>.py --help
```

### Common patterns (recommended)
```bash
# validate config without changing anything
./validate_env --dotenv ../../../.env --contract ./contracts/env.required.txt

# show what would change (no write)
./render_env --template ./templates/dev.env.tmpl --out ../../../.env --dry-run

# apply (write output)
./render_env --template ./templates/dev.env.tmpl --out ../../../.env
```

> **NOTE:** Script names and flags above are conventions. Update these examples to match the actual scripts in this folder.

[Back to top](#configsenvironmentscripts)

---

## Script contract
To keep scripts composable and CI-friendly, scripts in this folder **SHOULD** follow this interface:

### Required behaviors
- `--help` prints usage + exits `0`
- exit code is meaningful:
  - `0` success
  - `2` validation failure / contract violation
  - `>2` runtime failure (unexpected)
- default behavior is safe:
  - no writes unless `--out` or `--apply` is explicitly provided
  - secrets are redacted in logs by default

### Recommended flags
- `--dotenv <path>`: which `.env` to read/validate
- `--template <path>`: template input (non-secret)
- `--out <path>`: output path (writes)
- `--dry-run`: show diff/plan only
- `--format json|text`: machine-readable vs human output
- `--strict`: treat warnings as failures

[Back to top](#configsenvironmentscripts)

---

## Security and governance
### Principles
- **Fail closed:** missing required configuration must stop the operation, not limp forward.
- **No secret spillage:** scripts must avoid printing sensitive values (even in debug).
- **Least privilege:** CI checks should validate templates/contracts without needing real secrets.

### Example environment variables (illustrative)
The wider KFM system may reference variables such as:
- DB hostnames/service names (e.g., `POSTGRES_HOST` pointing at a Compose service name)
- AI backend routing / model selection (e.g., local model vs hosted API keys)

**Treat these as examples**; the authoritative list must live in this folder’s contract files.

[Back to top](#configsenvironmentscripts)

---

## Change workflow
When adding/changing env scripts or env contracts:

- [ ] Update the **Script registry** table above
- [ ] Add/adjust contract files (`contracts/`) so validation is explicit
- [ ] Ensure scripts are deterministic and idempotent
- [ ] Add a minimal CI check invoking validation in a non-secret mode
- [ ] Document any sensitive handling (redaction, flags, obligations)

[Back to top](#configsenvironmentscripts)

---

## Troubleshooting
### Docker-to-host connectivity (AI backend example)
If a service runs in Docker and needs to call a host-local service (like a local model server), you may need special host routing (e.g., using a Docker “host gateway” pattern). Document the exact approach in your env templates/contracts for your platform.

### “It works on my machine”
Common causes:
- `.env` drift (local manual edits not reflected in templates)
- missing required vars in one environment tier (dev vs CI)
- scripts not failing closed (warnings ignored)

Recommended fix:
1) run env validation,
2) render from template again,
3) re-run with `--dry-run` to confirm intended change.

[Back to top](#configsenvironmentscripts)
