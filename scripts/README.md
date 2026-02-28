<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9f9a88f5-4dd7-4ae9-8b64-5310a2b1f7fd
title: scripts/README.md
type: standard
version: v1
status: draft
owners: TBD (add CODEOWNERS rule)
created: 2026-02-26
updated: 2026-02-28
policy_label: public
related:
  - kfm://doc/???  # TODO: link to KFM governance/design guide in-repo
tags: [kfm, scripts, ops, governance]
notes:
  - This README documents conventions and governance expectations for scripts.
  - Update the directory tree and registry to match the actual repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `scripts/` — Governed operational scripts (receipt-emitting, fail-closed)

Operational scripts for KFM ingestion, validation, cataloging, indexing, and maintenance — **governed, reproducible, and auditable**.

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-default--deny-critical)
![governance](https://img.shields.io/badge/governance-receipts_required-orange)
![safety](https://img.shields.io/badge/safety-no_secrets-red)

> [!IMPORTANT]
> In KFM, “scripts” are **governed operations**. If a script can change what users see (directly or indirectly), it must be:
> **scope-controlled**, **receipt-emitting**, and **fail-closed**.

---

## Quick navigation

- [Purpose](#purpose)
- [Where this fits in the system](#where-this-fits-in-the-system)
- [Directory contract](#directory-contract)
- [Directory layout](#directory-layout)
- [Truth path IO discipline](#truth-path-io-discipline)
- [Run receipts](#run-receipts)
- [Conventions](#conventions)
- [Adding a new script](#adding-a-new-script)
- [Script registry](#script-registry)
- [Troubleshooting](#troubleshooting)

---

## Purpose

This directory exists for **operational scripts** that:

- snapshot upstream sources into the **Truth Path** (RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET),
- normalize and validate datasets (QA + schema + geo/time checks),
- generate/validate catalogs (DCAT/STAC/PROV) and cross-links,
- build **rebuildable projections** (search/graph/tiles/indexes) from canonical artifacts,
- run maintenance tasks (linting, audits, migrations) **without bypassing governance**.

> [!NOTE]
> If a task can be done by re-running a deterministic pipeline from immutable inputs, prefer the pipeline runner.
> Use “scripts” for orchestration, repeatability, and operator ergonomics — not as a bypass.

[Back to top](#top)

---

## Where this fits in the system

Scripts typically execute *inside* the KFM Truth Path, and must not bypass enforcement boundaries.

```mermaid
flowchart LR
  A[Upstream sources] --> B[scripts/acquire]
  B --> C[data/raw]
  C --> D[data/work or QUARANTINE]
  D --> E[data/processed]
  E --> F[data/catalog triplet]
  F --> G[scripts/index]
  G --> H[Rebuildable projections]
  H --> I[Governed API]
  I --> J[Map / Story / Focus UI]
```

### Trust membrane reminder

- UI/external clients **must not** access DB/object storage directly.
- Scripts must not create “secret side channels” (e.g., copying restricted artifacts into public outputs).
- Enforcement is owned by **governed APIs** and promotion gates; scripts must **invoke** those mechanisms, not replace them.

> [!WARNING]
> Scripts that mutate canonical storage **without** receipts/checksums/provenance break auditability and must be treated as a governance incident.

[Back to top](#top)

---

## Directory contract

### What belongs here

✅ **Put these here:**

- **Acquisition scripts**: upstream snapshot → `data/raw/**` (append-only), including terms snapshot + checksums.
- **Transform scripts**: RAW/WORK → WORK/PROCESSED, producing QA outputs and checksums.
- **Validation scripts**: schema validation, link checking, promotion gate checks, policy fixture checks.
- **Catalog scripts**: generate/validate DCAT/STAC/PROV and cross-links; emit receipts.
- **Index builder scripts**: rebuild DB/search/graph/tiles from canonical artifacts (never from “mystery inputs”).
- **Maintenance scripts**: migrations/backfills only when **reversible** and **receipt-emitting**.

### What must not go here

🚫 **Do not put these here:**

- secrets (API keys, tokens, service-account JSON, kubeconfigs),
- raw datasets or large artifacts (store in governed zones; don’t commit to git),
- “one-off” scripts that aren’t reproducible or reviewed,
- scripts that bypass policy enforcement (e.g., “just copy the restricted tiles to public”),
- scripts that print restricted coordinates/PII into logs or receipts.

> [!TIP]
> If it would be unsafe to paste into a public issue, it doesn’t belong in `scripts/` outputs (logs, receipts, examples).

[Back to top](#top)

---

## Directory layout

> [!IMPORTANT]
> Keep this tree accurate. If the repo structure differs, update this section **and** the Script Registry.

```text
scripts/
├─ README.md
│
├─ registry/                                     # Machine-readable registry + schemas + fixtures (small)
│  ├─ scripts.v1.json                            # Canonical registry: scripts, owners, scope, receipts, zones touched
│  ├─ schemas/                                   # Optional but recommended schemas for registry + receipts
│  │  ├─ scripts_registry.v1.schema.json
│  │  └─ run_receipt.v1.schema.json              # If the repo stores receipt schema here (or link to contracts/)
│  └─ fixtures/
│     ├─ valid/
│     └─ invalid/
│
├─ acquire/                                      # Upstream snapshot → RAW (append-only)
│  ├─ README.md
│  └─ acquire_<source_or_dataset>.{sh,py,ts}     # Emit terms snapshot + manifest + checksums + receipt
│
├─ transform/                                    # RAW/WORK → WORK/PROCESSED (deterministic)
│  ├─ README.md
│  └─ transform_<dataset>.{sh,py,ts}             # Emit QA + checksums + receipt
│
├─ validate/                                     # Validators + promotion-gate checks (fail-closed)
│  ├─ README.md
│  ├─ validate_catalog_triplet.{sh,py}           # DCAT/STAC/PROV + linkcheck
│  ├─ validate_policy_fixtures.{sh,py}           # parity tests (CI/runtime semantics)
│  └─ validate_promotion_gates.{sh,py}           # gates checklist + reason codes
│
├─ catalog/                                      # Catalog generation + normalization
│  ├─ README.md
│  ├─ build_dcat.{sh,py}
│  ├─ build_stac.{sh,py}
│  ├─ build_prov.{sh,py}
│  └─ crosslink_triplet.{sh,py}
│
├─ index/                                        # Rebuildable projections (never canonical)
│  ├─ README.md
│  ├─ build_search_index.{sh,py}
│  ├─ build_graph_projection.{sh,py}
│  └─ build_tiles.{sh,py}
│
├─ maintenance/                                  # One-off ops (migrations/backfills) — must be reversible + receipted
│  ├─ README.md
│  ├─ migrate_<thing>.{sh,py}
│  └─ backfill_<thing>.{sh,py}
│
├─ lib/                                          # Shared helpers (pure helpers preferred; minimal side effects)
│  ├─ README.md
│  ├─ receipt.{sh,py}                            # helper to write run receipts consistently
│  ├─ checksums.{sh,py}                          # helper to compute/write checksums.json
│  ├─ paths.{sh,py}                              # canonical path helpers for truth-path zones
│  └─ log.{sh,py}                                # structured logging helpers (policy-safe)
│
└─ _shared/                                      # Optional: tiny safe fixtures and test helpers
   ├─ data/                                      # synthetic fixtures only (policy-safe; tiny)
   └─ scripts/                                   # helper scripts used across scripts/ (fmt, lint, normalize)
```

[Back to top](#top)

---

## Truth path IO discipline

Scripts must respect KFM’s lifecycle zones and mutability rules.

| Zone | What it is | Script rules of the road |
|---|---|---|
| RAW | Immutable acquisitions + terms snapshot + checksums | **Append-only**. Never edit in place; supersede via new acquisition. |
| WORK / QUARANTINE | Intermediate transforms + QA + redaction candidates | WORK is regeneratable; QUARANTINE blocks promotion. Always record reasons. |
| PROCESSED | Publishable outputs (immutable per version) | Deterministic; digest-addressed; no “hand fixes” without provenance. |
| CATALOG/TRIPLET | DCAT + STAC + PROV + receipts + promotion manifest | Must validate + cross-link; this is the evidence surface. |
| PROJECTIONS | Search/graph/tiles/db indexes | Rebuildable only; never treated as source truth. |

> [!WARNING]
> A script that writes “public outputs” must never read from restricted artifacts unless policy explicitly allows and obligations are applied.

[Back to top](#top)

---

## Run receipts

Every script that produces artifacts **must** emit a run receipt that makes the run reproducible and auditable.

### Receipt rules (non-negotiable)

- Enumerate **inputs and outputs** with checksums.
- Record enough environment detail to reproduce the run (prefer container image digests).
- Include policy outcomes (decision + obligations + reason codes) when relevant.
- Never store secrets, raw restricted coordinates, or PII in receipts.

### Recommended receipt placement

- Promotion-affecting runs: under the dataset’s catalog receipts, e.g.:
  - `data/catalog/<dataset_slug>/<dataset_version_id>/receipts/<run_id>.json`
- Work-stage runs: under the work run, e.g.:
  - `data/work/<dataset_slug>/<work_run_id>/receipts/<run_id>.json`

> [!NOTE]
> Exact paths are repo-specific. The invariant is: **discoverable, deterministic location** and **cross-linked to catalogs/provenance** when promotion is involved.

### Minimal receipt shape (template)

```json
{
  "run_id": "kfm://run/2026-02-28T12:00:00Z.abcd",
  "run_kind": "acquire|transform|validate|catalog|index|maintenance",
  "started_at": "2026-02-28T12:00:00Z",
  "ended_at": "2026-02-28T12:05:00Z",
  "actor": { "principal": "svc:pipeline", "role": "pipeline" },
  "git": { "commit": "deadbeef", "dirty": false },

  "command": "scripts/transform/transform_example_dataset.py --dataset example_dataset --spec configs/...",

  "parameters": {
    "dataset_slug": "example_dataset",
    "spec_hash": "sha256:...",
    "dry_run": false
  },

  "inputs": [
    { "uri": "data/raw/example_dataset/2026-02-28T11:00:00Z.abcd/artifacts/source.csv", "sha256": "sha256:..." }
  ],
  "outputs": [
    { "uri": "data/processed/example_dataset/2026-02.abcd1234/artifacts/events.parquet", "sha256": "sha256:..." },
    { "uri": "data/processed/example_dataset/2026-02.abcd1234/qa/validation_report.json", "sha256": "sha256:..." }
  ],

  "validation": {
    "status": "pass",
    "checks": [
      { "id": "schema.validate", "status": "pass" },
      { "id": "geo.bounds", "status": "pass" }
    ]
  },

  "policy": {
    "decision": "allow",
    "policy_label": "public",
    "obligations_applied": ["require_attribution"],
    "reason_codes": ["POLICY.ALLOW.PUBLIC.READ"]
  },

  "notes": "Optional human context. Must be policy-safe."
}
```

[Back to top](#top)

---

## Conventions

### Script interface (required)

All scripts should:

- be runnable from the repo root,
- support `--help`,
- support `--dry-run` when meaningful,
- exit non-zero on failure,
- write human logs to stderr; write machine outputs to files.

### Determinism (required posture)

Prefer deterministic outputs:

- same inputs + same parameters ⇒ same outputs + same digests,
- avoid embedding timestamps in artifacts unless domain-required (timestamps belong in receipts),
- use stable ordering when writing JSON (canonical JSON if used for hashing).

### Naming

Use names that describe intent:

- `acquire_*` (upstream → RAW)
- `transform_*` (RAW/WORK → WORK/PROCESSED)
- `validate_*` (schema/link/policy/gates)
- `build_*` / `catalog_*` (DCAT/STAC/PROV)
- `index_*` (rebuildable projections)
- `migrate_*` / `backfill_*` (maintenance — reversible + receipted)

### Safety defaults (non-negotiable)

- Default-deny when licensing/sensitivity is unclear.
- Never print restricted coordinates/attributes into logs or receipts.
- If a required gate cannot be evaluated, **fail closed** and write the remediation path.

[Back to top](#top)

---

## Adding a new script

Use this checklist to keep changes small, reviewable, and governed:

- [ ] Script has a clear purpose statement and a stable name.
- [ ] Inputs and outputs are explicit (paths/URIs + formats).
- [ ] Script writes only to the correct zone(s).
- [ ] Script emits a run receipt and checksums for outputs.
- [ ] Script is idempotent **or** documents non-idempotence + rollback.
- [ ] Script does not embed or print secrets.
- [ ] Script does not leak restricted information (incl. “restricted existence” inference).
- [ ] If script affects promotion/publishing, it runs required Promotion Contract gates (or is run by the promotion runner).
- [ ] Add an entry to the Script Registry (`scripts/registry/scripts.v1.json`).

### Script header (copy/paste)

```text
Purpose:
Inputs:
Outputs:
Zones touched:
Policy considerations:
Receipt path:
Owner:
```

[Back to top](#top)

---

## Script registry

To keep scripts discoverable and reviewable, maintain a machine-readable registry.

- **Registry file:** `scripts/registry/scripts.v1.json`
- **Rule:** if a script exists, it must be registered with an owner and declared zones.

### Recommended registry fields

- `script_id` (stable)
- `path`
- `kind` (`acquire|transform|validate|catalog|index|maintenance`)
- `owner`
- `zones_touched[]`
- `requires_receipt` (true/false; default true for zone-writing scripts)
- `supports_dry_run` (true/false)
- `policy_sensitive` (true/false; triggers steward review)
- `notes` (policy-safe)

> [!NOTE]
> Registry content must remain policy-safe. Do not encode sensitive dataset details in registry entries.

[Back to top](#top)

---

## Troubleshooting

### “It ran, but I can’t reproduce the output”
- Confirm a run receipt exists and includes exact inputs/outputs + checksums.
- Confirm environment pinning (container digest / tool versions) is present.
- Confirm the same spec/config inputs (and `spec_hash`) were used.

### “Why did it fail closed?”
Common causes:
- missing or unclear license/rights metadata,
- missing policy label or unresolved sensitivity classification,
- schema/linkcheck failures (DCAT/STAC/PROV),
- missing checksums or receipts required by promotion gates.

### “How do I know it’s safe to run?”
- It should be receipt-emitting, deterministic, and scoped to specific zones.
- If it touches published surfaces, it must be gated by promotion checks and produce policy-safe errors.

[Back to top](#top)
