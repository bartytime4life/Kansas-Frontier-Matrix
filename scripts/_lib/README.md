# `scripts/_lib` 🧰

> Shared, reusable helpers for KFM automation scripts — **built for determinism, provenance, and policy gates**.

![Governed](https://img.shields.io/badge/KFM-governed-2b6cb0)
![Evidence-first](https://img.shields.io/badge/Mode-evidence--first-1f7a1f)

## Overview

`scripts/_lib/` is the **shared “standard library”** for one-off scripts and operational tooling in KFM.

Use it to centralize cross-cutting concerns that show up everywhere:

- **Deterministic execution** (stable inputs → stable outputs; replay-safe behavior)
- **Standard paths & staging discipline** (`data/raw/ → data/work/ → data/processed/`)
- **Catalog/provenance emission helpers** (STAC/DCAT/PROV “boundary artifacts”)
- **Validation + policy gate wrappers** (fail-closed)
- **Telemetry/logging conventions** (run IDs, artifacts, hashes)

> [!IMPORTANT]
> This folder should contain **reusable primitives**. Domain-specific logic belongs in the domain pipeline code (e.g., `src/pipelines/<domain>/…`) or domain tooling, not in `_lib`.

## Non‑negotiables (KFM invariants)

The helpers in `_lib` exist to make the following “always true” across scripts:

1. **Determinism & replayability**
   - No hidden state; prefer config inputs and explicit parameters.
2. **Evidence-first publishing**
   - Scripts should emit/attach catalogs & provenance **before** anything is “surfaced”.
3. **Fail-closed**
   - Missing required fields / provenance / labels / signatures must **fail the run**.
4. **Sensitivity & sovereignty are data**
   - Redaction/masking and access rules must be machine-checkable fields, not prose.
5. **API boundary stays sacred**
   - Anything UI-facing must be served via the governed API layer; scripts must not “smuggle” data by bypassing the boundary.

## Directory layout

> [!NOTE]
> The subfolders below are **recommended conventions**. Adjust to match what is actually present in your repo.

```text
scripts/
  _lib/
    README.md                 # you are here
    bash/                     # POSIX shell helpers (logging, env, safe-exit, etc.)
    python/                   # Python helpers (io, schema validation, provenance, hashing)
    policy/                   # Policy helpers (OPA/Rego wrappers, policy fixtures)
    fixtures/                 # Small test fixtures for validators (never real sensitive data)
    templates/                # Reusable templates (JSON-LD stubs, PROV skeletons, etc.)
```

### What belongs here vs not

| ✅ Belongs in `_lib/` | ❌ Does **not** belong in `_lib/` |
|---|---|
| Input/config parsing helpers | A full ETL pipeline for a domain |
| Path helpers (`raw/work/processed`, catalog dirs) | Hard-coded dataset-specific constants |
| Deterministic ID + hashing utilities | Secrets, tokens, credentials |
| Thin wrappers around validators/policy checks | UI code or DB adapters |
| PROV “run receipt” skeleton emitters | One-off “just run this once” hacks |

## How `_lib` fits the KFM pipeline

```mermaid
flowchart LR
  S[Script / Automation] --> L[scripts/_lib helpers]
  L --> P[data/raw ➜ data/work ➜ data/processed]
  L --> C[Catalog outputs<br/>STAC / DCAT]
  L --> V[PROV bundle<br/>(run lineage)]
  C --> G[Graph build / index refresh]
  V --> G
  G --> A[Governed API boundary]
  A --> U[UI / Story / Focus]
```

## Usage patterns

### Shell scripts

**Recommended guardrails** for bash/posix scripts that use `_lib`:

- `set -euo pipefail`
- Centralized `die()`/`warn()`/`log()` helpers
- Validate required env vars at startup
- Emit a run identifier (or accept one) and include it in all outputs/log lines

Example (illustrative):

```bash
#!/usr/bin/env bash
set -euo pipefail

# shellcheck source=/dev/null
source "$(git rev-parse --show-toplevel)/scripts/_lib/bash/logging.sh"
# shellcheck source=/dev/null
source "$(git rev-parse --show-toplevel)/scripts/_lib/bash/paths.sh"

require_env KFM_RUN_ID
require_env KFM_DOMAIN

RAW_DIR="$(kfm_raw_dir "$KFM_DOMAIN")"
WORK_DIR="$(kfm_work_dir "$KFM_DOMAIN")"
OUT_DIR="$(kfm_processed_dir "$KFM_DOMAIN")"

log_info "run_id=$KFM_RUN_ID domain=$KFM_DOMAIN raw=$RAW_DIR work=$WORK_DIR out=$OUT_DIR"
```

### Python scripts

Prefer `_lib/python` for anything that needs parsing, validation, JSON-LD emission, hashing, etc.

Example (illustrative):

```python
from scripts._lib.python.paths import raw_dir, work_dir, processed_dir
from scripts._lib.python.validation import validate_stac, validate_dcat, validate_prov

domain = "air-quality"  # example
raw = raw_dir(domain)
work = work_dir(domain)
out = processed_dir(domain)

# ... do transform ...

validate_stac(out / "stac")
validate_dcat(out / "catalog" / "dcat")
validate_prov(out / "prov")
```

> [!WARNING]
> The example import paths assume `scripts/` is on `PYTHONPATH`. If your repo uses a different import strategy, document it here and keep it consistent.

## Validation gates (minimum)

Use `_lib` to make the “default quality bar” easy to apply everywhere:

- Schema validation for STAC/DCAT/PROV
- Geometry sanity checks (if spatial)
- Temporal sanity checks (no impossible timestamps for the domain)
- License/rights fields present + enforced
- Provenance completeness (inputs → activities → outputs; stable checksums)

A script that produces publishable output **should** be able to run:

```bash
scripts/validate_all.sh --domain <domain> --run-id <id>
```

…and fail with actionable errors.

## Security & governance checklist

> [!CAUTION]
> Treat script outputs as governed artifacts when they affect system behavior, public narratives, datasets/catalogs, policy/compliance, or Focus Mode.

- [ ] No secrets in scripts, fixtures, or logs (use env + secret stores)
- [ ] All outputs go through the standard staging & catalog layout
- [ ] Any sensitive locations or restricted fields are generalized/redacted **before** publication
- [ ] Every artifact has: checksums/digests + a provenance bundle + policy labels
- [ ] CI/QA is able to reproduce the script output from recorded config + inputs

## Adding a new helper (Definition of Done)

When you add or change anything in `_lib`, it should be a **small, reversible** increment:

- [ ] Helper is generic (not domain-specific)
- [ ] Inputs/outputs are explicit; no hidden mutable state
- [ ] Idempotent behavior documented (what happens on re-run)
- [ ] Unit tests or fixture-based checks exist (where applicable)
- [ ] Usage example added to this README or to the helper’s own docstring
- [ ] No new policy bypass paths introduced

## Troubleshooting

<details>
<summary><strong>Common failure modes</strong></summary>

- **“Works on my machine” paths**  
  Use `_lib` path helpers and repo-root resolution; don’t assume CWD.

- **Non-deterministic outputs**  
  Ensure sorting, stable IDs, stable timestamps (or explicitly recorded), and pinned dependency versions.

- **Catalog/provenance drift**  
  Treat STAC/DCAT/PROV as first-class outputs; validate them in the same run that creates data.

</details>

## Appendix: Related KFM docs (paths)

The following are typically relevant when updating `_lib`:

- `docs/MASTER_GUIDE_v13.md` (canonical pipeline + invariants)
- `docs/standards/` (STAC/DCAT/PROV profiles + schemas)
- `docs/patterns/` (replay-safe ETL, deterministic IDs, attestations)
- `docs/security/` (supply chain, secrets, provenance enforcement)

> [!NOTE]
> Keep these as **paths** (not links) if your CI runs strict link-checking and the targets may not exist yet.

## Version history

- **2026-02-16** — Initial `scripts/_lib/README.md` scaffold (this file).
