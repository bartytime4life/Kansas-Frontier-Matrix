<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7c5b2f20-1f6a-4b6a-9f0e-4ddf6dc1f1aa
title: scripts
type: standard
version: v1
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
  - Evidence discipline: every meaningful claim in this README is tagged as Confirmed, Proposed, or Unknown.
  - This file is a directory README: it defines purpose, allowed inputs, and explicit exclusions.
[/KFM_META_BLOCK_V2] -->

<div align="center">

# `scripts/` — Build, lint, promotion, and release automation

**Purpose:** governed automation scripts used by local dev and CI/CD to enforce the KFM promotion contract.  
**Status:** `draft` • **Owners:** `kfm-platform` (TODO)

[![CI](https://img.shields.io/badge/CI-TODO-lightgrey)](../.github/workflows/)
[![Policy](https://img.shields.io/badge/Policy-default--deny%20fail--closed-blue)](../policy/)
[![Provenance](https://img.shields.io/badge/Provenance-receipts%20%2B%20attestations-informational)](../provenance/)
[![Docs](https://img.shields.io/badge/Docs-directory%20README-brightgreen)](./README.md)

</div>

---

## Quick navigation

- [Evidence tags](#evidence-tags)
- [Where this directory fits](#where-this-directory-fits)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Directory layout](#directory-layout)
- [Conventions](#conventions)
- [Promotion contract alignment](#promotion-contract-alignment)
- [How to run scripts](#how-to-run-scripts)
- [Adding a new script](#adding-a-new-script)
- [Verification steps](#verification-steps)
- [Version history](#version-history)

---

## Evidence tags

[Confirmed] A claim backed by cited KFM documents (see “Notes & Citations” in the PR / change request).  
[Proposed] A recommended pattern that is consistent with KFM governance goals but may not yet exist in the repo.  
[Unknown] A claim that cannot be verified from available evidence; the smallest verification step is stated.

---

## Where this directory fits

[Confirmed] `scripts/` is part of the repo’s “ops glue” layer, alongside `configs/`, `migrations/`, and `tools/`, used for automation rather than core domain logic.

[Proposed] Scripts are invoked in two primary contexts:
- local developer workflows (pre-commit, lint, smoke tests, release dry-runs)
- CI/CD workflows (required gates for merges/promotion)

[Unknown] Which scripts are currently present in this repo checkout (verify with `tree -L 3 scripts/`).

[Back to top](#quick-navigation)

---

## What belongs here

[Confirmed] Build/release and related automation scripts belong here (e.g., promotion, lint, rebuild tasks).

[Proposed] Acceptable inputs for `scripts/`:
- small, composable automation steps that call *existing* tooling (`tools/validators`, policy tests, dataset builders)
- wrappers that standardize environment setup (paths, env vars, container targets)
- release/promotion helpers that *enforce* “fail-closed” checks and emit machine-verifiable artifacts

[Proposed] Preferred script traits:
- deterministic, idempotent, and safe-by-default (`--dry-run` first)
- emits structured logs (JSON lines preferred when feasible)
- returns non-zero exit codes on any failed gate

[Back to top](#quick-navigation)

---

## What must not go here

[Proposed] Do **not** place these in `scripts/`:
- core ingestion/transformation logic (belongs in pipeline/package modules, not wrappers)
- “one-off” manual fixes that can’t be reproduced or audited
- secrets, tokens, private keys, or credential material (scripts may *read* secrets from environment/injected runners, but must never commit them)
- any code path that bypasses the policy boundary for published surfaces (no “UI → DB” shortcuts)

[Back to top](#quick-navigation)

---

## Directory layout

[Unknown] The exact layout depends on what is currently in the repo. The following is a *recommended* shape.

[Proposed] Example structure:

~~~text
scripts/
├── README.md                  # This file
├── release/                   # Release & promotion helpers (may have its own README)
│   └── README.md
├── ci/                        # Local replicas of CI gates (lint/validate/policy)
├── dev/                       # Developer convenience scripts (safe, non-promoting)
├── watch_and_pr.py            # Example: watcher that opens PRs (if adopted)
└── compute_digests.py         # Example: canonical hash + digest helper (if adopted)
~~~

[Unknown] Whether `scripts/release/README.md` exists in *this* checkout (verify with `ls scripts/release/`).

[Back to top](#quick-navigation)

---

## Conventions

[Proposed] **Language & portability**
- Use **Python** for non-trivial orchestration/JSON handling.
- Use **bash** only for thin wrappers; if bash, include `set -euo pipefail`.
- Avoid platform-specific assumptions unless documented (macOS vs Linux differences).

[Proposed] **CLI contract**
- Every script must support:
  - `--help`
  - `--dry-run` (no writes)
  - `--json` (structured output) when practical
  - `--fail-closed` (default: enabled) meaning “if unsure, stop”
- Scripts must never silently “best-effort” past a governance gate.

[Proposed] **Outputs**
- For any action that writes or promotes artifacts, the script must either:
  - emit (or point to) a **run receipt** / audit record, or
  - fail closed with a clear message describing missing prerequisites.

[Back to top](#quick-navigation)

---

## Promotion contract alignment

[Confirmed] KFM promotion is gate-driven: promotion to “published” is blocked unless minimum gates are met, and the gates are designed to be automated in CI.

[Confirmed] The data lifecycle is zoned (RAW → WORK → PROCESSED → CATALOG triplet → PUBLISHED), and promotion is not allowed without the required artifacts and validations.

[Proposed] **What scripts in this directory typically do** (examples):
- run metadata validators (DCAT/STAC/PROV) and link checks
- compute deterministic `spec_hash` values for dataset specs/manifests
- compute digests for produced artifacts and inject/verify integrity fields
- create or verify run receipts and (where configured) signature/attestation artifacts
- open PRs for “watcher” workflows that pin updates by digest

[Proposed] **Process diagram (scripts as gate runners)**

~~~mermaid
flowchart LR
  Dev[Developer or CI] --> Run[Run scripts]
  Run --> V[Validators and link checks]
  Run --> P[Policy tests]
  Run --> R[Run receipt and digests]
  R --> C[Catalog triplet]
  C --> Pub[Published surfaces]
~~~

[Back to top](#quick-navigation)

---

## How to run scripts

[Unknown] Exact commands depend on which scripts exist. The patterns below are safe defaults.

[Proposed] List available scripts:

~~~bash
ls -la scripts/
~~~

[Proposed] Run a Python script:

~~~bash
python scripts/<script_name>.py --help
python scripts/<script_name>.py --dry-run
~~~

[Proposed] Run a shell script:

~~~bash
bash scripts/<script_name>.sh --help
bash scripts/<script_name>.sh --dry-run
~~~

[Proposed] CI parity goal: if a workflow runs in `.github/workflows/*`, a local-friendly equivalent should exist either here or in `tools/`, so contributors can reproduce failures quickly.

[Back to top](#quick-navigation)

---

## Adding a new script

[Proposed] Minimum definition-of-done (DoD) for any new script:
- [ ] Script has `--help` and documents purpose, inputs, outputs, and failure modes.
- [ ] Script defaults to **fail-closed** and supports `--dry-run`.
- [ ] Script does not embed secrets; uses env vars or runner-injected credentials.
- [ ] Script writes *only* to the appropriate lifecycle zone (RAW/WORK/PROCESSED), or to release/publish surfaces when explicitly authorized.
- [ ] Script includes tests where practical (unit tests for parsing/hashing logic; integration tests for end-to-end gates).
- [ ] If the script impacts promotion, add/adjust CI checks so the invariant is test-enforced (not tribal knowledge).

[Back to top](#quick-navigation)

---

## Verification steps

[Confirmed] We should not assert the existence of specific modules/scripts without verifying against the live repo.

[Unknown] Minimal verification steps for this directory:
1. `git rev-parse HEAD` (record commit)
2. `tree -L 3 scripts/` (capture layout)
3. Identify which CI workflows call scripts: search `.github/workflows/` for `scripts/`
4. Run `--help` for each discovered script and confirm CLI contracts match this README

[Back to top](#quick-navigation)

---

## Version history

[Proposed] Track changes to this directory README as operational policy surface.

| Version | Date       | Notes |
|--------:|------------|-------|
| v1      | 2026-03-03 | Initial `scripts/` directory README (governed automation + promotion gates alignment). |
