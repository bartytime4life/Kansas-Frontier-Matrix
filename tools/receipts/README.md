# tools/receipts — KFM Receipt Tooling (run_record • run_manifest • spec_hash) 🧾
![Governed](https://img.shields.io/badge/governed-artifact-critical)
![Fail Closed](https://img.shields.io/badge/fail--closed-required-111827)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Promotion Contract](https://img.shields.io/badge/promotion-contract%20proofs-6a5acd)
![spec_hash](https://img.shields.io/badge/spec__hash-RFC8785%20JCS%20%2B%20sha256-4b0082)
![Receipts](https://img.shields.io/badge/receipts-run__record%20%7C%20run__manifest-2563eb)

**Purpose:** `tools/receipts/` is the **verification + enforcement toolbox** for KFM “receipts” — the proof artifacts that make promotion (Raw → Work → Processed) auditable, reproducible, and fail-closed.

> [!IMPORTANT]
> Receipts are **not optional documentation**. They are **machine-checkable proof** required by the KFM Promotion Contract.
> If receipts are missing or invalid, **promotion must deny** by default.

---

## Governance Header

| Field | Value |
|---|---|
| Document | `tools/receipts/README.md` |
| Status | **Governed** |
| Version | `v1.0.0-draft` |
| Effective date | `2026-02-16` |
| Owners | `.github/CODEOWNERS` *(required; if missing → governance gap)* |
| Applies to | `data/work/**/runs/**` receipts + receipt validators + CI receipt gate |
| Non‑negotiables | **Fail closed**, **deterministic identity**, **no secrets**, **no trust membrane bypass** |

> [!WARNING]
> **Fail-closed rule:** if a validator cannot read/parse/verify a receipt, that is a **failure**, not a skip.

---

## Table of contents

- [What “receipt” means in KFM](#what-receipt-means-in-kfm)
- [Where receipts live](#where-receipts-live)
- [Receipt artifacts](#receipt-artifacts)
  - [`run_record.json`](#run_recordjson)
  - [`validation_report.json`](#validation_reportjson)
  - [`run_manifest.json`](#run_manifestjson-promotion-contract)
  - [`checksums.sha256` expectations](#checksumssha256-expectations)
  - [`spec_hash` semantics](#spec_hash-semantics)
- [What tools/receipts validates](#what-toolsreceipts-validates)
- [Directory layout](#directory-layout)
- [Quickstart](#quickstart)
- [CI integration](#ci-integration)
- [Sensitive data and redaction](#sensitive-data-and-redaction)
- [Contributing](#contributing)
- [Glossary](#glossary)

---

## What “receipt” means in KFM

In KFM governance docs, a **Receipt** is:

- **run evidence** (`run_record.json`)  
- **integrity evidence** (checksums / digests)  
- **deterministic identity evidence** (`spec_hash`)  
- plus the **Promotion Contract rollup** (`run_manifest.json`) that blocks or allows promotion.

This definition is referenced in repo governance and data plane docs (see `.github/README.md`, `README.md`, and `data/README.md`).  

> [!NOTE]
> You may see the phrase **run receipt** in some documents. In this repo’s *data plane layout*, the canonical filenames are **`run_record.json`** and **`run_manifest.json`**.

---

## Where receipts live

The governed data plane specifies that a pipeline run emits receipts under:

- `data/work/<dataset_id>/runs/<run_id>/run_record.json`
- `data/work/<dataset_id>/runs/<run_id>/validation_report.json`
- `data/work/<dataset_id>/runs/<run_id>/run_manifest.json` *(Promotion Contract receipt)*

…and processed outputs (servable truth) live under:

- `data/processed/<dataset_id>/<version_id>/...`
- with `data/processed/<dataset_id>/<version_id>/checksums.sha256`

> [!IMPORTANT]
> `raw/` and `work/` are **never served**. They exist for reproducibility + audit. Only **processed + catalogs** may back user-visible claims.

---

## Receipt artifacts

### `run_record.json`

**Intent:** Bind together *what ran*, *with what inputs*, *producing what outputs*, *using what code/spec*, *when*, and *under what governance context*.

**Minimum expectations (contract target):**

| Field | Required | Meaning |
|---|:---:|---|
| `run_id` | ✅ | Stable run identifier (ULID recommended) |
| `dataset_id` | ✅ | Dataset identity (registry-driven) |
| `pipeline_id` | ✅ | Which pipeline/connector ran |
| `spec` | ✅ | The pipeline spec object (schema-defined) |
| `spec_hash` | ✅ | `sha256(JCS(spec))` (RFC 8785) |
| `spec_schema_id` | ✅ | Schema ID for `spec` (versioned) |
| `spec_recipe_version` | ✅ | Pipeline recipe/contract version |
| `inputs[]` | ✅ | Each input must include a resolvable URI/ref + digest |
| `outputs[]` | ✅ | Work outputs and/or pointers to processed outputs + digests |
| `code` | ✅ | Code identity (commit SHA and/or image digest) |
| `timestamps` | ✅ | `started_at`, `ended_at` (RFC3339) |
| `runner` | ✅ | Runner identity (CI/job, host, container image) |
| `policy_labels` | ✅ | Sensitivity/rights/policy tags needed for gates |

> [!TIP]
> Treat `run_record.json` as **append-only**. If something is wrong, emit a **new run** (new `run_id`) or a **new version** with explicit provenance — don’t “edit history.”

---

### `validation_report.json`

**Intent:** Make validations explicit and reviewable, including failure reasons.

**Minimum expectations (contract target):**

- `summary.pass` boolean
- `checks[]` array with:
  - `check_id`
  - `status` (`pass|fail|warn|skip`)
  - `message`
  - optional `evidence[]` pointers (paths/refs)
- stable ordering + deterministic formatting in strict mode

> [!IMPORTANT]
> CI and promotion gates should treat **failed checks as blockers**.
> “Warn-only” checks must be explicitly configured (no silent downgrades).

---

### `run_manifest.json` (Promotion Contract)

**Intent:** The **promotion-proof envelope**: a compact, machine-checkable rollup that asserts:

- which **processed version** is being promoted,
- what artifacts are inside,
- what catalogs/provenance exist,
- and what integrity proofs + policy prerequisites are satisfied.

**Minimum expectations (contract target):**

| Field | Required | Meaning |
|---|:---:|---|
| `dataset_id` | ✅ | Dataset identity |
| `version_id` | ✅ | Immutable processed version ID |
| `run_id` | ✅ | The run that produced the version |
| `spec_hash` | ✅ | Must match `run_record.spec_hash` |
| `processed_root` | ✅ | Path/ref to the processed version root |
| `checksums_ref` | ✅ | Pointer to `checksums.sha256` (and optionally its digest) |
| `artifacts[]` | ✅ | Canonical list of files/distributions (paths + digests) |
| `catalog_refs` | ✅ | Links to DCAT (required), PROV (required), STAC (if spatial) |
| `rights` | ✅ | License, attribution, redistribution notes (deny if missing) |
| `sensitivity` | ✅ | Classification (deny if missing/unknown) |
| `audit_ref` | ✅ | Promotion audit pointer (or placeholder until ledger exists) |
| `signatures` |  | Optional: signature/attestation refs for supply chain integrity |

> [!CAUTION]
> `run_manifest.json` is the artifact reviewers should be able to read and answer:
> “What exactly is being promoted, and can we prove it?”

---

### `checksums.sha256` expectations

Receipts tooling treats checksums as integrity-critical.

**Minimum rules (contract target):**
- `checksums.sha256` exists for every processed version.
- Every **servable** artifact is present in the checksum list.
- Hash algorithm is explicit and consistent (sha256 recommended).
- No duplicate paths; stable ordering preferred.

> [!WARNING]
> Missing checksums = **promotion deny** (fail closed).

---

### `spec_hash` semantics

KFM defines deterministic identity as:

- `spec_hash = sha256(JCS(spec))` where JCS is **RFC 8785 JSON Canonicalization Scheme**.

**Why this matters:**
- Auditors can prove two runs used the same effective spec.
- Reviewers can compare spec changes without “hash drift.”
- Policy can require re-review when spec materiality changes.

**Receipts gate rules (contract target):**
- `spec_hash` must be recomputable from `spec` exactly.
- `spec` must be schema-defined and versioned (`spec_schema_id`).
- If `spec` changes, the hash must change.

---

## What tools/receipts validates

A receipts validator should be able to run locally and in CI and enforce:

### 1) Schema and shape
- JSON parses
- Required keys exist
- Types are correct
- Unknown keys are either disallowed or explicitly tolerated (choose one; be consistent)

### 2) Deterministic identity
- `spec_hash` recomputes and matches
- `spec_schema_id` and `spec_recipe_version` are present
- Run/version IDs match naming conventions

### 3) Integrity proofs
- `checksums.sha256` exists and is complete for processed outputs
- Digests in receipts match digests of files (when files are present in the repo/workspace)
- No “tag-only” references for immutable artifacts (prefer digests)

### 4) Cross-link coherence (promotion-proof)
- `run_manifest` references the matching `run_record`
- `catalog_refs` exist (at least DCAT + PROV, and STAC if applicable)
- Rights and sensitivity are present (missing = deny)

### 5) Report outputs
- Human-readable logs + machine-readable JSON report
- Stable exit codes (see `tools/README.md` for recommended semantics)

> [!NOTE]
> This folder should not invent its own tool interface conventions. Align with `tools/README.md` defaults.

---

## Directory layout

This README is contract-first: **create missing folders as you implement the capability**.

```text
tools/receipts/
├── README.md                 # this file
├── bin/                      # thin CLI wrappers (local + CI parity)
│   ├── kfm-receipts           # (target) umbrella CLI: validate, explain, report
│   └── receipts_verify.sh     # (optional) shell wrapper used by CI
├── contracts/                # receipt schemas (JSON Schema), versioned
│   ├── run_record.v1.schema.json
│   ├── validation_report.v1.schema.json
│   └── run_manifest.v1.schema.json
├── validators/               # implementation (python/node/go — pick one; keep deterministic)
│   ├── validate_run_record.*
│   ├── validate_run_manifest.*
│   └── spec_hash.*
├── fixtures/                 # tiny deterministic fixtures
│   ├── pass/
│   │   ├── run_record.min.json
│   │   └── run_manifest.min.json
│   └── fail/
│       ├── run_record.missing_spec_hash.json
│       └── run_manifest.missing_rights.json
├── tests/                    # unit + golden regression tests
└── reports/                  # (gitignored) local outputs; CI uploads equivalents
```

> [!TIP]
> If you place schemas elsewhere (e.g., `contracts/` at repo root), keep a mapping table here and make validators reference the canonical path.

---

## Quickstart

> [!NOTE]
> The command names below are the **target interface** for this folder. If the CLI wrapper does not exist yet, implement it in `tools/receipts/bin/` and keep flags stable (so CI and docs don’t drift).

### Validate a single run folder

```bash
# from repo root
tools/receipts/bin/kfm-receipts validate \
  data/work/<dataset_id>/runs/<run_id> \
  --strict \
  --json reports/receipts.single.json
```

### Validate all receipts for a dataset

```bash
tools/receipts/bin/kfm-receipts validate \
  data/work/<dataset_id>/runs \
  --strict \
  --json reports/receipts.dataset.json
```

### Validate only changed files (CI optimization)

```bash
git diff --name-only origin/main...HEAD > /tmp/changed_files.txt

tools/receipts/bin/kfm-receipts validate \
  --paths-from /tmp/changed_files.txt \
  --strict \
  --json reports/receipts.changed.json
```

### Exit codes (recommended)

Align with `tools/README.md`:

- `0` success
- `2` validation failure (receipt evaluated and failed)
- `3` execution error (missing dependency / unreadable file / crash)
- `4` policy denial (explicit deny outcome, default-deny preserved)

---

## CI integration

Receipt gating is a **planned** enforcement surface in repo governance. The goal is a stable required check:

- check name: `receipts`
- runs on PRs that touch governed receipt paths (`data/work/**`, `data/processed/**`, catalogs, pipeline specs)

### Example workflow job (illustrative)

```yaml
name: receipts

on:
  pull_request:
    paths:
      - "data/**"
      - "tools/receipts/**"
      - "pipelines/**"
      - "src/pipelines/**"

jobs:
  receipts:
    name: receipts
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate receipts
        run: |
          tools/receipts/bin/kfm-receipts validate data/work --strict --json reports/receipts.json
      - name: Upload reports
        uses: actions/upload-artifact@v4
        with:
          name: kfm-ci--reports
          path: reports/
```

> [!IMPORTANT]
> CI must upload proof artifacts (`report.json` + `report.md`), not just pass/fail.

---

## Sensitive data and redaction

Receipts are often stored in-repo (or in governed artifact stores). That means:

- **Never** include secrets (tokens, keys, credentials).
- Avoid printing precise restricted locations in logs/reports.
- If the run involves sensitive-location data, store only:
  - generalized bounds (bbox) or
  - hashed identifiers or
  - policy-approved coarse geometry
- Record redaction/generalization decisions as provenance (don’t hide them).

> [!WARNING]
> If sensitivity is unknown, treat it as **restricted** until classified.

---

## Contributing

### Definition of Done (DoD) for changes under `tools/receipts/`

- [ ] Contract updates are reflected in:
  - [ ] `contracts/*.schema.json` (versioned)
  - [ ] fixtures (`fixtures/pass` + `fixtures/fail`)
  - [ ] tests (unit + golden)
- [ ] Validator remains deterministic (stable ordering; strict mode avoids nondeterministic timestamps)
- [ ] Validator is fail-closed (missing signals block)
- [ ] Machine report format remains stable (or bumped with semver + migration note)
- [ ] No trust-membrane bypass patterns are introduced (this tool is verification-only)

### Minimal verification steps for reviewers

- Run:
  - `tools/receipts/bin/kfm-receipts validate data/work --strict`
- Inspect:
  - a failing fixture produces a clear rule id + message
  - JSON report exists and is parseable
  - `spec_hash` recomputation matches receipt values

---

## Glossary

| Term | Meaning |
|---|---|
| `run_record.json` | The run-level receipt binding inputs, spec, code identity, outputs, and timestamps |
| `validation_report.json` | Machine-readable validation outcomes (pass/fail + reasons) |
| `run_manifest.json` | Promotion Contract rollup for a processed version (the “what exactly are we promoting?” proof) |
| `spec_hash` | Deterministic spec identity: `sha256(JCS(spec))` (RFC 8785) |
| Promotion Contract | The rule: raw→work→processed promotion is denied unless proofs exist and validate |
| Fail closed | Missing proof = deny; never “best effort allow” |

---

### References (in-repo)

- Repo constitution + truth path: `README.md`
- CI gatehouse contract: `.github/README.md`
- Data plane Promotion Contract + layout: `data/README.md`
- Tooling conventions + exit codes: `tools/README.md`
- Default deny + governance policy patterns: `tools/policy/README.md`