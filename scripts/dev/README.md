<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7b5b46e0-4a4a-4d14-8790-9b4b6c2ffbfe
title: scripts/dev — Developer Scripts
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - scripts/README.md
  - docs/MASTER_GUIDE_v13.md
  - docs/architecture/*
tags: [kfm, dev, scripts, run-receipts, policy]
notes:
  - This README is intentionally conservative: dev convenience is allowed, but not at the cost of bypassing governance.
  - Replace TBD fields and fill the Script Registry as scripts land.
[/KFM_META_BLOCK_V2] -->

# `scripts/dev` — Developer scripts
**Purpose:** local-only scripts for **developer productivity** (bootstrap, smoke tests, local data seeding, validation helpers) that still respect KFM’s **trust membrane** and **truth-path** invariants.

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-dev_scripts-blue)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)
![policy](https://img.shields.io/badge/policy_label-public-lightgrey)

---

## Quick navigation
- [What belongs here](#what-belongs-here)
- [Non-negotiables](#non-negotiables)
- [Directory layout](#directory-layout)
- [Golden path: run a dev script safely](#golden-path-run-a-dev-script-safely)
- [Standard interface for scripts](#standard-interface-for-scripts)
- [Outputs: logs, receipts, checksums](#outputs-logs-receipts-checksums)
- [If your script touches datasets](#if-your-script-touches-datasets)
- [Script registry](#script-registry)
- [Add or change a dev script](#add-or-change-a-dev-script)
- [Troubleshooting](#troubleshooting)
- [Appendix: templates](#appendix-templates)

---

## What belongs here
Use `scripts/dev/` for **local** or **PR-review** tasks that are helpful during development:

- bootstrapping a local dev environment (sanity checks, env validation)
- running lightweight validations / linters / link-checkers
- seeding *non-production* sample data for UI/API development
- generating test fixtures (policy fixtures, catalog fixtures, small geo fixtures)
- “developer UX” helpers (list datasets, verify EvidenceRefs, print quick summaries)

**Do NOT** put production ingestion logic here.
- Production pipelines and index builders should live in their governed homes (e.g., `src/pipelines/`, `tools/`, etc.) and be covered by CI, receipts, and promotion gates.
- If a script is required for releases or promotion, it is **not** “dev” anymore—move it.

> [!WARNING]
> This folder is allowed to contain “sharp tools,” but **sharp tools must be wrapped**:
> - **dry-run by default**
> - **explicit `--apply` to mutate anything**
> - **emit a run receipt when producing artifacts**
> - **refuse to run if policy/zone boundaries are unclear**

---

## Non-negotiables
### 1) Trust membrane stays intact
Dev scripts MUST NOT create a side door around KFM governance:
- Do not have “frontend-like” scripts fetch directly from object storage / DBs “because it’s faster.”
- Do not have “backend-like” scripts bypass repositories to write directly to storage.

> [!IMPORTANT]
> If a dev script needs data, prefer:
> 1) calling the **governed API** (best),
> 2) calling a **pipeline runner** that emits receipts and artifacts (acceptable),
> 3) reading local fixtures/snapshots (acceptable).
>
> Direct DB/Object-store access is a last resort and MUST be clearly labeled and gated behind `--i-accept-risk`.

### 2) Truth path boundaries are real boundaries
Dev scripts should behave like “mini-runs”:
- Outputs should be **content-addressable or checksummed** when feasible.
- If you generate something that might be promoted, create the metadata/lineage alongside it (or refuse).

### 3) Fail-closed is the default posture
If a script cannot prove it is safe (missing env vars, missing policy label, missing output dir, unknown dataset id), it MUST stop and print next steps.

---

## Directory layout
### Current state
This README cannot assume what scripts exist in your repo today.

Run:
```bash
ls -la scripts/dev
```

### Recommended (proposed) layout
```text
scripts/dev/
├─ README.md                        # you are here
├─ _templates/                      # copy-paste templates (safe defaults)
│  ├─ run_receipt.v1.example.json
│  └─ script_help_header.example.txt
├─ bootstrap/                       # local env checks + small setup helpers
├─ smoke/                           # fast checks (API health, link checks, sample queries)
├─ data/                            # LOCAL-ONLY data helpers (seed, generate fixtures)
├─ policy/                          # policy fixture generation + conftest helpers
└─ utils/                           # shared helpers used by other dev scripts
```

> [!NOTE]
> If you already have a different structure, keep it.
> The only hard requirement is that scripts remain **discoverable**, **safe-by-default**, and **receipt-friendly**.

---

## Golden path: run a dev script safely
1) **Start in dry-run**
```bash
./scripts/dev/<path>/<script> --help
./scripts/dev/<path>/<script> --dry-run
```

2) **Check what it will read/write**
- It should print:
  - inputs (paths/URIs)
  - outputs (paths)
  - whether it will touch RAW/WORK/PROCESSED
  - whether it will write a receipt

3) **Run with explicit apply**
```bash
./scripts/dev/<path>/<script> --apply
```

4) **Verify artifacts + receipt**
- Confirm artifacts exist
- Confirm receipt exists and references the artifacts

5) **If outputs are meant to persist**
- Open a PR that includes:
  - the artifacts (or pointers)
  - the receipt
  - any catalog/metadata produced
  - a short “why” note in the PR description

---

## Standard interface for scripts
All scripts under `scripts/dev` SHOULD implement the same interface to keep muscle-memory consistent.

### Required flags (recommended contract)
| Flag | Required | Default | Meaning |
|---|---:|---:|---|
| `--help` | ✅ | n/a | Print usage + examples |
| `--dry-run` | ✅ | `true` | Compute actions without writing |
| `--apply` | ✅ | `false` | Allow writes/mutations |
| `--log-level {debug,info,warn,error}` | ✅ | `info` | Logging verbosity |
| `--out <path>` | ✅ | script-defined | Output directory (must exist or be creatable) |
| `--receipt-out <path>` | ✅ | script-defined | Where to write run receipt JSON |
| `--policy-label <label>` | ✅ (if data involved) | none | Required for anything that could be shared |
| `--i-accept-risk` | ❌ | `false` | Required for any direct DB/object-store access |

> [!TIP]
> For scripts that only read local files and print to stdout, `--policy-label` can be optional.
> The minute you emit artifacts, you need policy context.

### Standard environment variables (optional)
Use env vars to avoid repeating flags, but **never** hide risky behavior behind env vars.

| Env var | Example | Purpose |
|---|---|---|
| `KFM_ENV` | `dev` | Forces dev-safe behavior |
| `KFM_OUT_ROOT` | `./.kfm_out` | Default output root for dev artifacts |
| `KFM_RECEIPT_ROOT` | `./.kfm_receipts` | Default receipt directory |

---

## Outputs: logs, receipts, checksums
### Output locations (recommended)
To avoid polluting governed directories, dev scripts SHOULD write under a local dev root:

- `./.kfm_out/...` (artifacts)
- `./.kfm_receipts/...` (receipts)
- `./.kfm_logs/...` (logs)

These can be `.gitignore`’d unless a run is intentionally attached to a PR for review.

### Run receipt (dev-minimum)
When a script produces artifacts, it MUST emit a JSON receipt capturing:
- actor (who ran it)
- operation (what it did)
- inputs and outputs with digests (when feasible)
- environment capture (git commit, container digest if applicable)
- policy decision inputs (policy label at minimum)

Minimal dev receipt shape (example):
```json
{
  "run_id": "kfm://run/2026-02-22T00:00:00Z.local.devscript",
  "actor": { "principal": "user:<you>", "role": "developer" },
  "operation": "dev_seed_sample_data",
  "dataset_version_id": "LOCAL_ONLY",
  "inputs": [
    { "uri": "fixtures/sample.csv", "digest": "sha256:<optional>" }
  ],
  "outputs": [
    { "uri": ".kfm_out/sample.parquet", "digest": "sha256:<optional>" }
  ],
  "environment": {
    "git_commit": "<commit>",
    "container_digest": "<optional>",
    "params_digest": "<optional>"
  },
  "policy": { "policy_label": "public" },
  "created_at": "2026-02-22T00:00:00Z"
}
```

> [!WARNING]
> If you cannot compute a digest, record **why** (e.g., streamed output, external tool limitation) and prefer fixing it.
> Missing digests are acceptable for pure dev prototypes, but should not survive into promotion pathways.

---

## If your script touches datasets
### Respect zone boundaries
If your script reads/writes data, you must decide which “zone” it is operating in:

- **RAW**: append-only acquisition snapshots (do not edit in place)
- **WORK/QUARANTINE**: intermediate transforms + validation reports + candidate redactions
- **PROCESSED**: publishable artifacts (only if you can also produce catalogs + receipts)

> [!IMPORTANT]
> If sensitivity/licensing is unclear → treat as **QUARANTINE** and stop.

### Promotion checklist (dev-facing)
If you are about to create something that looks promotable, you must be able to answer “yes” to:

- [ ] Identity/version is deterministic (or explicitly marked LOCAL_ONLY)
- [ ] Processed artifacts exist AND have digests
- [ ] Required catalogs (DCAT/STAC/PROV) validate (if applicable)
- [ ] Cross-links resolve (EvidenceRefs don’t guess)
- [ ] Policy label assigned; obligations applied if required
- [ ] QA report exists; failures quarantined
- [ ] Run receipt emitted

If you can’t meet these gates, keep outputs in WORK/QUARANTINE and open a PR tagged **needs-governance-review**.

---

## Script registry
Fill this in as scripts land. The goal: **discoverability** and **risk visibility**.

| Script | Type | Summary | Reads | Writes | Emits receipt | Risk | Owner |
|---|---|---|---|---|---:|---|---|
| _TBD_ | _sh/py/js_ | _What it does_ | _inputs_ | _outputs_ | ✅/❌ | low/med/high | _TBD_ |

> [!TIP]
> Treat the “Risk” column seriously:
> - **low**: read-only, stdout-only
> - **med**: writes local artifacts
> - **high**: touches DB/object store, modifies data, or could leak restricted info

---

## Add or change a dev script
### Must-have checklist
- [ ] Script supports `--help`, `--dry-run`, `--apply`
- [ ] Dry-run is the default; apply is explicit
- [ ] Clear stdout logging (inputs, outputs, mode)
- [ ] If artifacts are produced: receipt JSON is written
- [ ] No secrets are printed; logs redact tokens/keys
- [ ] Script fails closed on missing config or ambiguous policy label
- [ ] Script added to the [Script registry](#script-registry)

### Nice-to-have checklist
- [ ] Deterministic output paths (or explicit `--out`)
- [ ] Digests computed for inputs/outputs
- [ ] Unit test for helper libraries (if any)
- [ ] “Smoke test” mode for CI (read-only)

---

## Troubleshooting
### “It worked on my machine”
- Print environment: `git commit`, OS, container digest (if used), key env vars (redacted)
- Prefer scripts that can run inside the same containerized dev environment as the API/pipelines

### Permission issues on mounted volumes
- If a containerized script cannot write to `data/` or `.kfm_out/`, fix the mount UID/GID mapping.
- Never “chmod -R 777” as a default fix—prefer precise ownership.

### Port conflicts / dev stack instability
- If your dev environment uses containers and a service won’t start, check for conflicts on common ports (DB, API, UI).
- Restart only the affected service when possible.

---

## Appendix: templates
<details>
<summary><strong>Template: bash script skeleton</strong></summary>

```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_NAME="$(basename "$0")"

usage() {
  cat <<'EOF'
Usage:
  script.sh --dry-run|--apply --out <path> --receipt-out <path> [--log-level info|debug]

Safety:
  - dry-run is the default posture
  - --apply is required to write

EOF
}

DRY_RUN="true"
APPLY="false"
OUT=""
RECEIPT_OUT=""
LOG_LEVEL="info"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --help) usage; exit 0 ;;
    --dry-run) DRY_RUN="true"; APPLY="false"; shift ;;
    --apply) APPLY="true"; DRY_RUN="false"; shift ;;
    --out) OUT="$2"; shift 2 ;;
    --receipt-out) RECEIPT_OUT="$2"; shift 2 ;;
    --log-level) LOG_LEVEL="$2"; shift 2 ;;
    *)
      echo "Unknown arg: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -z "$OUT" || -z "$RECEIPT_OUT" ]]; then
  echo "Missing required --out/--receipt-out" >&2
  exit 2
fi

echo "[$SCRIPT_NAME] mode: $( [[ "$APPLY" == "true" ]] && echo APPLY || echo DRY-RUN )"
echo "[$SCRIPT_NAME] out: $OUT"
echo "[$SCRIPT_NAME] receipt: $RECEIPT_OUT"

# TODO: compute digests, write outputs, then write receipt JSON

if [[ "$APPLY" != "true" ]]; then
  echo "[$SCRIPT_NAME] dry-run complete (no changes made)"
  exit 0
fi

echo "[$SCRIPT_NAME] apply complete"
```
</details>

<details>
<summary><strong>Template: python script skeleton</strong></summary>

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", default=True)
    p.add_argument("--apply", action="store_true", default=False)
    p.add_argument("--out", required=True)
    p.add_argument("--receipt-out", required=True)
    p.add_argument("--log-level", default="info", choices=["debug", "info", "warn", "error"])
    return p.parse_args()

def main() -> int:
    args = parse_args()

    if args.apply:
        args.dry_run = False

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[devscript] mode={mode} out={args.out} receipt={args.receipt_out}")

    os.makedirs(args.out, exist_ok=True)
    os.makedirs(os.path.dirname(args.receipt_out), exist_ok=True)

    # TODO: do work, compute digests

    receipt = {
        "run_id": f"kfm://run/{datetime.now(timezone.utc).isoformat()}.local.devscript",
        "actor": {"principal": os.getenv("USER", "unknown"), "role": "developer"},
        "operation": "dev_script_example",
        "dataset_version_id": "LOCAL_ONLY",
        "inputs": [],
        "outputs": [],
        "environment": {"git_commit": os.getenv("GIT_COMMIT", "UNKNOWN")},
        "policy": {"policy_label": os.getenv("KFM_POLICY_LABEL", "public")},
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    if args.apply:
        with open(args.receipt_out, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=2, sort_keys=True)
        print(f"[devscript] wrote receipt: {args.receipt_out}")
    else:
        print("[devscript] dry-run complete (no receipt written)")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```
</details>

---

↑ **Back to top:** [scripts/dev](#scriptsdev--developer-scripts)
