<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7c5b2f20-1f6a-4b6a-9f0e-4ddf6dc1f1aa
title: scripts
type: standard
version: v2
status: draft
owners: kfm-platform (TODO)
created: 2026-03-03
updated: 2026-03-03
policy_label: public
related:
  - ../.github/workflows/
  - ../tools/
  - ../policy/
  - ../data/
  - ./release/README.md
tags: [kfm, scripts, ci, release, promotion, governance]
notes:
  - Evidence discipline: every meaningful claim in this README is tagged as CONFIRMED / PROPOSED / UNKNOWN.
  - This file is a directory README: it defines purpose, allowed inputs, and explicit exclusions.
[/KFM_META_BLOCK_V2] -->

<div align="center">

# `scripts/` — Governed automation for build, lint, validation, promotion, and release

**Purpose:** automation entrypoints used by local dev and CI/CD to enforce KFM governance invariants and the Promotion Contract (fail-closed).  
**Status:** `draft` • **Owners:** `kfm-platform` (TODO)

[![CI](https://img.shields.io/badge/CI-TODO-lightgrey)](../.github/workflows/)
[![Policy](https://img.shields.io/badge/Policy-default--deny%20fail--closed-blue)](../policy/)
[![Data](https://img.shields.io/badge/Data-zones%20RAW%2FWORK%2FPROCESSED-informational)](../data/)
[![Docs](https://img.shields.io/badge/Docs-directory%20README-brightgreen)](./README.md)

</div>

---

> **IMPACT (required)**
>
> - **Primary role:** provide *reproducible, auditable* automation that runs the same governance semantics in CI and in governed environments.  
> - **Fail-closed stance:** if evidence is missing or cannot be verified, scripts must stop (non‑zero exit).  
> - **Invariant boundary:** scripts must not introduce any path that bypasses the **trust membrane** (no “client/UI → storage/DB” shortcuts; no bypassing repository/adapter layers).  
> - **Promotion alignment:** scripts are the “gate runners” for Promotion Contract v1 (Gates A–G).

---

## Quick navigation

- [Evidence tags](#evidence-tags)
- [Where this directory fits](#where-this-directory-fits)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Directory layout](#directory-layout)
- [Script interface contract](#script-interface-contract)
- [Promotion Contract v1 coverage](#promotion-contract-v1-coverage)
- [How to run scripts](#how-to-run-scripts)
- [Adding a new script](#adding-a-new-script)
- [Verification steps](#verification-steps)
- [FAQ](#faq)
- [Version history](#version-history)

---

## Evidence tags

**KFM status vocabulary:** `CONFIRMED`, `PROPOSED`, `UNKNOWN`.

- **CONFIRMED** — backed by KFM design/governance sources; treated as a non‑negotiable requirement for GOVERNED mode.
- **PROPOSED** — consistent with KFM posture and recommended to implement; may not exist in the current repo.
- **UNKNOWN** — not verified in the current checkout; list the smallest verification step(s) needed.

> **Note:** This README intentionally avoids claiming which exact scripts exist until verified against the live repo tree.

[Back to top](#quick-navigation)

---

## Where this directory fits

**CONFIRMED** `scripts/` is part of the repo’s automation layer (alongside workflows and tooling). It exists to *run* gates and standardize developer/CI execution, not to define core business logic.  

**CONFIRMED** KFM governance is enforced by a “truth path” of zones and gates; automation should treat those gates as first‑class CI checks and release checks.

**PROPOSED** Two operating contexts for scripts:
- **Local developer workflows**: lint, typecheck, policy tests, validation, dry‑run promotion checks.
- **CI/CD workflows**: merge-blocking gates and promotion/release orchestration.

**UNKNOWN** What scripts are present in *this* checkout.  
Smallest verification step: `tree -L 3 scripts/` and record the output in the PR.

[Back to top](#quick-navigation)

---

## What belongs here

**CONFIRMED** Automation for validation/promotion/release belongs here, particularly when it:
- executes Promotion Contract gates (A–G),
- produces audit artifacts (run receipts / manifests),
- verifies catalogs/provenance/policy decisions.

**PROPOSED** Acceptable inputs for `scripts/`:
- thin orchestration around **existing** toolchain entrypoints (validators, policy tests, schema checks)
- wrappers that standardize environment setup (paths, env vars, container targets, consistent error model)
- release/promotion helpers that **fail closed** and emit machine‑verifiable artifacts (digests, manifests)

**PROPOSED** Preferred traits:
- deterministic + idempotent (re-run safe)
- safe-by-default: default to `--dry-run` and require explicit “write/publish/promote” flags
- structured logs (JSON lines preferred when feasible)
- non-zero exit codes on any failed gate

[Back to top](#quick-navigation)

---

## What must not go here

**CONFIRMED** Do **not** place code here that breaks the trust membrane:
- no direct UI/client access to DB/object storage
- no core backend logic bypassing repository/adapter layers to talk directly to storage

**PROPOSED** Do **not** place these in `scripts/` (and where instead):
- core ingestion/transformation logic → **pipeline packages/modules** (not wrappers)
- schema/profile definitions → **contracts/** or **schemas/** (repo-specific)
- policy logic (Rego) → **policy/** (so CI and runtime share semantics)
- one-off manual fixes that can’t be reproduced/audited → **avoid** (or convert to a deterministic tool + test)
- secrets/tokens/private keys → **never commit**; use env vars or runner-injected credentials

**PROPOSED** No “best-effort” governance: scripts must not silently continue past missing license/sensitivity/policy inputs.

[Back to top](#quick-navigation)

---

## Directory layout

**UNKNOWN** The exact layout in this checkout.  
Smallest verification step: `tree -L 3 scripts/`.

**PROPOSED** Recommended shape (example names only):

~~~text
scripts/
├── README.md                  # This file
├── ci/                        # Local replicas of CI gates (lint/validate/policy/contract)
├── release/                   # Promotion + release helpers (see scripts/release/README.md)
├── dev/                       # Developer convenience scripts (non-promoting, safe defaults)
└── lib/                        # Shared helpers for scripts (argument parsing, logging, exit codes)
~~~

[Back to top](#quick-navigation)

---

## Script interface contract

**PROPOSED** All scripts in this directory should follow a consistent CLI contract:

- `--help` always available
- `--dry-run` does not write to storage or mutate outputs
- `--json` emits structured output (when practical)
- `--fail-closed` (default: enabled): if unsure, stop

**PROPOSED** Standard exit codes:
- `0` success
- `2` invalid usage / missing required args
- `10` validation failure (schema/catalog/prov)
- `11` policy denial (OPA/rego deny or missing policy inputs)
- `12` integrity failure (digest mismatch, non-determinism detected)
- `20` operational error (I/O, network, tool crash)

**PROPOSED** Standard output conventions:
- human-readable summary to stderr (for dev ergonomics)
- machine-readable JSON lines to stdout (for CI parsing), e.g. `{ "event": "gate_result", "gate": "A", ... }`

<details>
<summary><strong>PROPOSED: Environment variables (house conventions)</strong></summary>

- `KFM_MODE` = `sandbox` | `governed`  
  - `sandbox`: exploration allowed, **no promotion**  
  - `governed`: all gates enforced; promotion allowed only with explicit flags
- `KFM_DATA_ROOT` = absolute or repo-relative path to data workspace
- `KFM_POLICY_ROOT` = policy bundle location (Rego + fixtures)
- `KFM_ARTIFACT_STORE` = location/URL for object storage/registry (if applicable)

</details>

[Back to top](#quick-navigation)

---

## Promotion Contract v1 coverage

**CONFIRMED** Promotion to runtime surfaces is blocked unless minimum gates are met (A–F required; G recommended “production posture”).  
**CONFIRMED** The catalog “triplet” (DCAT + STAC + PROV) is the interoperability + evidence surface; cross-links must resolve.

### Gate coverage matrix (definitions are CONFIRMED; script responsibilities are PROPOSED)

| Gate | Minimum requirement (CONFIRMED) | What scripts typically do (PROPOSED) |
|------|----------------------------------|--------------------------------------|
| A — Identity and versioning | Stable `dataset_id`; immutable `dataset_version_id`; deterministic `spec_hash` | Compute/verify `spec_hash`; enforce naming rules; prevent “hash drift” via golden tests |
| B — Licensing and rights metadata | Explicit license + rights holder/attribution; unclear license → quarantine (fail closed) | Fail CI if license/rights missing; snapshot upstream terms; enforce “metadata-only” mode when mirroring is disallowed |
| C — Sensitivity classification and redaction plan | `policy_label` assigned; redaction/generalization plan recorded in PROV when needed | Enforce default-deny fixtures; verify obligations applied; block promotion when sensitivity is unresolved |
| D — Catalog triplet validation | DCAT/STAC/PROV validate and cross-link; links resolvable | Run validators + link checks; fail if broken EvidenceRefs or missing IDs |
| E — Run receipt and checksums | `run_receipt` exists; inputs/outputs enumerated with checksums; environment recorded | Emit receipt templates; verify digests; ensure deterministic outputs for same spec |
| F — Policy tests and contract tests | OPA policy tests pass; evidence resolver resolves at least one ref in CI; API/schema contracts validate | Run conftest fixtures; run evidence-resolve integration test; run OpenAPI/schema contract checks |
| G — Optional but recommended | SBOM + build provenance; perf + accessibility smoke checks | Generate/verify SBOM/attestations; run perf smoke; run accessibility checks (e.g., evidence drawer keyboard nav) |

### Process diagram (scripts as gate runners)

~~~mermaid
flowchart LR
  U[Upstream sources] --> R[RAW zone]
  R --> W[WORK or QUARANTINE]
  W --> P[PROCESSED zone]
  P --> C[CATALOG triplet]
  C --> S[PUBLISHED surfaces]

  P --> GA[Gate A Identity]
  P --> GB[Gate B Licensing]
  P --> GC[Gate C Sensitivity]
  P --> GD[Gate D Triplet]
  P --> GE[Gate E Receipts]
  P --> GF[Gate F Policy and contracts]
  P --> GG[Gate G Recommended]

  GA --> S
  GB --> S
  GC --> S
  GD --> S
  GE --> S
  GF --> S
  GG --> S
~~~

[Back to top](#quick-navigation)

---

## How to run scripts

**UNKNOWN** Exact commands depend on which scripts exist.

**PROPOSED** Safe discovery commands (always runnable):

~~~bash
ls -la scripts/
tree -L 3 scripts/
~~~

**PROPOSED** Run a Python script (pattern):

~~~bash
python scripts/<script_name>.py --help
python scripts/<script_name>.py --dry-run
~~~

**PROPOSED** Run a shell script (pattern):

~~~bash
bash scripts/<script_name>.sh --help
bash scripts/<script_name>.sh --dry-run
~~~

**PROPOSED** CI parity goal: if a workflow in `.github/workflows/*` runs a gate, a local-friendly equivalent should exist in `scripts/` or `tools/` so contributors can reproduce failures quickly.

[Back to top](#quick-navigation)

---

## Adding a new script

**PROPOSED** Definition of Done (DoD) for any new script:
- [ ] Has `--help` documenting purpose, inputs, outputs, and failure modes.
- [ ] Defaults to **fail-closed** and supports `--dry-run`.
- [ ] Does not embed secrets; reads env vars or runner-injected credentials.
- [ ] Writes only to the correct lifecycle zone (RAW/WORK/PROCESSED) unless explicitly promoting.
- [ ] Produces machine-verifiable outputs where relevant (digests, receipts, manifests).
- [ ] Includes tests where practical (unit tests for hashing/parsing; integration tests for gate runners).
- [ ] If it impacts promotion, CI enforces it (merge/promotion blocked on failure).

[Back to top](#quick-navigation)

---

## Verification steps

**CONFIRMED** Do not assert repo state without verifying the current checkout.

**UNKNOWN** Minimal verification steps for this directory in the current repo:
1. `git rev-parse HEAD` (record commit)
2. `tree -L 3 scripts/` (capture layout)
3. Search which workflows call scripts: `rg -n "scripts/" .github/workflows/`
4. For each discovered script, run `--help` and confirm it matches the CLI contract above
5. Map each script to Promotion Contract gates A–G (update this README if needed)

[Back to top](#quick-navigation)

---

## FAQ

**Why are these scripts “governed”?**  
**CONFIRMED** Because KFM’s user-facing trust depends on fail-closed validation, policy enforcement, and auditable provenance; automation is how those requirements become test-enforced rather than tribal knowledge.

**Where do validators/policy logic live?**  
**PROPOSED** Put reusable validators in `tools/` and policy packs in `policy/`. Keep `scripts/` as orchestration entrypoints that call them.

**Can scripts directly edit published data?**  
**PROPOSED** Only via explicit “promote/release” paths that enforce Promotion Contract gates and record manifests/receipts. Otherwise, default to dry-run and quarantine.

[Back to top](#quick-navigation)

---

## Version history

| Version | Date       | Notes |
|--------:|------------|-------|
| v2      | 2026-03-03 | Upgrade: align to trust membrane + Promotion Contract v1 (Gates A–G); add IMPACT block; add gate coverage matrix; tighten fail-closed CLI contract. |
| v1      | 2026-03-03 | Initial `scripts/` directory README. |
