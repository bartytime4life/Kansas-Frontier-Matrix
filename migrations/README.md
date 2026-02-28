<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/46a7276e-762c-48b6-9731-f13d3f0db4fb
title: migrations/README — Governed migrations (schema, projections, graph)
type: standard
version: v2
status: draft
owners: TBD (set via CODEOWNERS)
created: 2026-02-22
updated: 2026-02-28
policy_label: public
related:
  - ../README.md
  - ../docs/
  - ../contracts/
  - ../configs/
  - ../data/
tags:
  - kfm
  - migrations
  - governance
  - rollback
  - receipts
  - prov
notes:
  - Defines how migrations are declared, reviewed, executed, validated, and rolled back.
  - Aligns migrations to KFM invariants: trust membrane, fail-closed promotion, canonical vs rebuildable, deterministic receipts.
  - If uncertain: fail closed, emit receipts, and require governance review.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Migrations
Governed, reversible changes to **rebuildable stores** (schemas, constraints, indexes, projections, graph shape) with **scope control**, **baselines**, **diffs**, **run receipts**, and **rollback artifacts**.

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-public-blue)
![change-control](https://img.shields.io/badge/change_control-fail--closed-critical)
![reversible](https://img.shields.io/badge/reversible-required-success)
![audit](https://img.shields.io/badge/audit-run_receipt%20%2B%20PROV-informational)

**Owners:** TBD (enforced by `CODEOWNERS`)  
**Principles:** map-first • time-aware • governed • evidence-first • cite-or-abstain

---

## Quick navigation
- [Directory contract](#directory-contract)
- [When to use a migration](#when-to-use-a-migration)
- [Non-negotiables](#non-negotiables)
- [Directory layout](#directory-layout)
- [Migration declaration contract](#migration-declaration-contract)
- [Baselines, diffs, and blast radius](#baselines-diffs-and-blast-radius)
- [Invariant checks](#invariant-checks)
- [Rollback artifacts](#rollback-artifacts)
- [Run receipts and PROV](#run-receipts-and-prov)
- [Migration types](#migration-types)
  - [PostGIS migrations](#postgis-migrations)
  - [Search/index migrations](#searchindex-migrations)
  - [Graph migrations](#graph-migrations)
- [How to add a migration](#how-to-add-a-migration)
- [PR checklist](#pr-checklist)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)

---

## Directory contract

### Purpose
`migrations/` exists to make “high-impact mutations” **reviewable, auditable, and reversible**.

A migration is any controlled change that intentionally mutates:
- schemas/constraints/indexes in a relational store (e.g., PostGIS)
- search/index structures (mappings, analyzers, vector schema, reindex flows)
- graph shape (labels, relationships, constraints, ontology) **when a graph is used**
- backfills that are not simply “re-run the deterministic pipeline”

### What belongs here
✅ Machine-declared migrations with:
- **declared scope**
- **pre/post baselines**
- **diff outputs**
- **validation + invariant checks**
- **rollback artifacts** (or explicit, approved irreversibility)
- **run receipts** and optional **PROV** bundles

✅ Deterministic helpers that support migration safety (render/plan/diff/check), if repo-standard.

### What must not go here
❌ Secrets, credentials, tokens, kubeconfigs  
❌ Raw or sensitive dataset payloads  
❌ One-off “operator scripts” without declarations, receipts, and rollback  
❌ Mutations to **canonical truth** (RAW/PROCESSED/CATALOG) — those must be done by governed pipelines and promotion gates

> [!IMPORTANT]
> In KFM, PostGIS/search/graph/tiles are **rebuildable projections**. Migrations must preserve the ability to reconstruct from canonical artifacts.

[Back to top](#top)

---

## When to use a migration

Prefer pipelines over migrations when possible.

Use a migration when:
- the change must mutate a rebuildable store in-place (schema/index/constraint)
- the change requires controlled sequencing and rollback
- the change has non-trivial blast radius that must be declared and reviewed
- the change is needed to restore invariant correctness

Do **not** use a migration when:
- you can re-derive the projection by replaying canonical artifacts (recommended)
- you can roll out a new versioned projection side-by-side and flip consumers safely

> [!RULE]
> If you can re-run deterministically from immutable inputs, **do that**. Migrations are for what cannot be safely re-derived without an explicit change plan.

[Back to top](#top)

---

## Non-negotiables

1. **Fail closed.** If validation, policy, invariant checks, or receipts fail → do not proceed; rollback if needed.
2. **Scope is declared upfront.** Every migration declares what it is allowed to touch and what is forbidden.
3. **Baseline + diff required.** Capture pre/post state and compute deltas; reviewers must see blast radius.
4. **Rollback artifacts required.** Reversible by default. Irreversible changes require explicit governance approval.
5. **Receipts always.** Every execution emits a run receipt (and optionally PROV) for attribution and auditability.
6. **Protected domains are hard stop.** Governance-protected schemas/namespaces/labels must not change without explicit approval.
7. **Policy-safe outputs.** Diffs/receipts/logs must not leak secrets, PII, or restricted location details.

[Back to top](#top)

---

## Directory layout

> [!NOTE]
> This is the **recommended contract layout** aligned to the repo-wide “registry + schemas + fixtures” pattern used elsewhere (configs/examples/apps). If your repo already differs, update this section to match reality while preserving the guarantees.

```text
migrations/
├─ README.md
│
├─ registry/                                      # Machine-readable registries + schemas + fixtures (small)
│  ├─ migrations.v1.json                          # Canonical migration registry (ids, types, owners, status)
│  ├─ schemas/
│  │  ├─ migration_declaration.v1.schema.json     # Schema for migration.yml
│  │  └─ receipt_refs.v1.schema.json              # (Optional) schema for receipt pointer records
│  └─ fixtures/
│     ├─ valid/                                   # Valid declaration examples
│     └─ invalid/                                 # Invalid declaration examples (must fail CI)
│
├─ postgis/                                       # Relational schema migrations (optional; if PostGIS is used)
│  ├─ README.md                                   # Tooling + ordering rules + rollback posture
│  ├─ PG-MIG-YYYY-MM-DD-01/
│  │  ├─ migration.yml                            # Declaration (scope + limits)
│  │  ├─ forward.sql                              # Forward change (idempotent preferred)
│  │  ├─ rollback.sql                             # Rollback plan (required if requires_rollback=true)
│  │  ├─ baselines/
│  │  │  ├─ pre.json                              # Baseline snapshot BEFORE
│  │  │  └─ post.json                             # Baseline snapshot AFTER
│  │  ├─ diffs/
│  │  │  ├─ summary.json                          # Declared-vs-observed delta summary
│  │  │  └─ touched.csv                           # Optional reviewer-friendly list of touched objects
│  │  ├─ receipts/
│  │  │  ├─ run_receipt.json                      # Execution receipt (who/what/when + validation)
│  │  │  └─ prov.jsonld                           # Optional PROV bundle
│  │  └─ notes.md                                 # Human context + risks + review notes
│  └─ ...
│
├─ search/                                        # Search/index migrations (optional)
│  ├─ README.md
│  ├─ SEARCH-MIG-YYYY-MM-DD-01/
│  │  ├─ migration.yml
│  │  ├─ forward.json                             # Example: mapping/settings update OR reindex plan
│  │  ├─ rollback.json                            # Rollback/restore plan OR “not possible” w/ approval
│  │  ├─ baselines/
│  │  ├─ diffs/
│  │  ├─ receipts/
│  │  └─ notes.md
│  └─ ...
│
└─ graph/                                         # Graph migrations (optional)
   ├─ README.md
   ├─ GRAPH-MIG-YYYY-MM-DD-01/
   │  ├─ migration.yml
   │  ├─ forward.cypher
   │  ├─ rollback.cypher
   │  ├─ baselines/
   │  ├─ diffs/
   │  ├─ receipts/
   │  └─ notes.md
   └─ ...
```

[Back to top](#top)

---

## Migration declaration contract

Each migration directory **must** include a machine-readable `migration.yml`.

Minimum fields (v1; extend as needed):
- `migration_id` (stable, unique, never reused)
- `type` (`postgis` | `search` | `graph` | `other`)
- `intent` (plain-language)
- `scope` (allowed + forbidden)
- `limits` (blast-radius caps)
- `requires_rollback` (boolean)
- `approvals` (routing rules or labels)
- `runner` (how it is executed; command or tool reference)
- `artifacts` (forward/rollback script names, baseline/diff expectations)

### Example `migration.yml`

```yaml
migration_id: PG-MIG-2026-02-28-01
type: postgis
intent: "Add spatial index to parcels table to improve map query performance"

scope:
  allowed_schemas:
    - public
  allowed_tables:
    - parcels
  forbidden_schemas:
    - governance
    - audit
  forbidden_tables:
    - authority_sites

limits:
  max_table_count_touched: 1
  max_index_count_delta: 2
  max_row_backfill: 0

requires_rollback: true

approvals:
  required_reviewers:
    - kfm-platform
    - kfm-governance
  change_class: governance-critical

runner:
  tool: "psql"                 # or alembic/flyway/etc.
  command: "scripts/migrate.sh" # repo-standard wrapper, if present
  environment:
    - KFM_DB_DSN_REF            # secret reference name; not the secret value

artifacts:
  forward:
    - forward.sql
  rollback:
    - rollback.sql
  baselines:
    pre: baselines/pre.json
    post: baselines/post.json
  diffs:
    summary: diffs/summary.json
```

> [!IMPORTANT]
> “Scope” is not documentation — it is a **limit** enforced by CI and/or the migration runner. If scope can’t be enforced, treat it as incomplete and fail closed.

[Back to top](#top)

---

## Baselines, diffs, and blast radius

Every migration must capture **pre** and **post** baselines and produce a diff.

Baseline goals:
- detect unintended mutations even when “it seems fine”
- provide reviewers a predictable blast-radius summary
- make rollback verification possible

### Minimum baseline fields (recommended)
- object counts (tables/indexes/constraints OR nodes/rels)
- schema fingerprint (constraints/index definitions digest)
- “protected domain” fingerprint (hash of protected objects)
- performance-relevant stats where safe (optional)

### Diff outputs (required)
- `diffs/summary.json` (machine-readable, CI-enforced)
- `diffs/touched.csv` (optional reviewer-friendly list)

> [!RULE]
> If observed diffs exceed declared limits → **fail** and require rollback or explicit approved exception.

[Back to top](#top)

---

## Invariant checks

Migrations must not violate KFM invariants. CI (and preflight locally) should enforce:

### Global invariants
- no secret leakage in artifacts/receipts
- no policy bypass (trust membrane intact)
- no mutation of protected domains without explicit approval

### Store-specific invariants (examples)
**PostGIS**
- required constraints exist
- spatial indexes present where required
- migrations are ordered and idempotent (where possible)

**Search**
- mapping changes are versioned
- reindex plan is explicit
- index alias flips are audited
- rollback strategy exists (old index retained) unless explicitly approved

**Graph**
- no orphaned provenance nodes
- ontology constraints preserved (exclusive labels, required relationships)
- protected/authority nodes unchanged unless explicitly approved

> [!TIP]
> Treat “invariant checks” as contract tests: they must be deterministic and run in CI.

[Back to top](#top)

---

## Rollback artifacts

Reversible by default.

If `requires_rollback: true`, the migration directory must include:
- rollback script (`rollback.sql`, `rollback.json`, `rollback.cypher`, etc.)
- rollback verification notes (what to check after rollback)
- baseline/diff artifacts sufficient to confirm rollback correctness

If a migration is **not** reversible:
- set `requires_rollback: false`
- document why in `notes.md`
- include the governance approval reference (issue/ADR/decision record)
- include an alternative safety strategy (e.g., dual-write, shadow index, alias flip)

> [!WARNING]
> “We can’t roll this back” is a governance event, not a casual decision.

[Back to top](#top)

---

## Run receipts and PROV

Every migration execution must emit:
- a **run receipt** (`receipts/run_receipt.json`)
- optionally a **PROV bundle** (`receipts/prov.jsonld`) for richer lineage

### Receipt minimum fields
- `run_id` (stable id for the execution)
- `migration_id`
- `actor` (service principal or operator identity; no personal secrets)
- `started_at`, `finished_at`
- `environment` (dev/stage/prod)
- `inputs` (scripts/config versions; digests)
- `outputs` (baseline/diff digests; any created artifacts)
- `validation` results (pass/fail + invariant check outputs)
- `policy` notes (policy-safe; avoid restricted detail)

> [!IMPORTANT]
> Receipts must be **policy-safe**. Never store credentials, raw DSNs, or restricted coordinates in receipts.

### Lifecycle sketch

```mermaid
flowchart TD
  A[Declare migration.yml] --> B[Preflight checks]
  B --> C[Capture baseline pre]
  C --> D[Apply forward change]
  D --> E[Capture baseline post]
  E --> F[Compute diff]
  F --> G{Scope + invariants pass?}
  G -->|Yes| H[Emit run_receipt (+ PROV)]
  G -->|No| I[Rollback if required]
  I --> J[Emit failed receipt + evidence]
  H --> K[Review + governance gate]
```

[Back to top](#top)

---

## Migration types

### PostGIS migrations
Use for:
- schema changes (tables/columns/types)
- index/constraint changes
- controlled backfills

Recommended safety posture:
- prefer additive changes
- large backfills must be explicitly bounded and staged
- never run ad hoc in prod; always through the governed runner

### Search/index migrations
Use for:
- mapping/settings changes
- analyzer changes
- vector field changes
- reindex flows, alias swaps, shard strategy

Recommended safety posture:
- plan for dual-index + alias flip where possible
- keep old index around for rollback window (time-bounded)
- treat “index rebuild” as a controlled operation with receipts

### Graph migrations
Use for:
- ontology changes (labels/rel-types)
- constraints and indexes in a graph store
- controlled rewrites/backfills that cannot be safely rederived

Recommended safety posture:
- declare protected labels/namespaces and fail on mutation
- compute structural fingerprints (counts + constraint digests + protected-node hashes)
- prefer idempotent forward scripts

[Back to top](#top)

---

## How to add a migration

1. Pick a type: `postgis/`, `search/`, or `graph/`.
2. Create a new folder:
   - `migrations/<type>/<TYPE>-MIG-YYYY-MM-DD-01/`
3. Add:
   - `migration.yml`
   - forward script
   - rollback script (or approved irreversibility notes)
4. Wire baselines/diffs:
   - `baselines/pre.json`, `baselines/post.json`
   - `diffs/summary.json`
5. Ensure CI coverage:
   - declaration schema validation
   - invariant checks
   - secrets scan
6. Run in a safe environment and emit a receipt:
   - store under `receipts/`
7. Open PR with declared scope + blast radius summary.

> [!NOTE]
> If your repo has a migration runner (CLI/workflow), link it from each `migrations/<type>/README.md` and keep commands consistent.

[Back to top](#top)

---

## PR checklist

- [ ] `migration.yml` present and passes schema validation
- [ ] Scope (allowed/forbidden) is explicit and tight
- [ ] Limits are realistic and enforceable
- [ ] Forward script present (idempotent preferred)
- [ ] Rollback script present **or** approved irreversibility documented
- [ ] Baseline capture defined (pre + post)
- [ ] Diff output defined and reviewable
- [ ] Invariant checks pass locally and in CI
- [ ] Run receipt + (optional) PROV generation is wired
- [ ] Governance review requested if protected domains may be touched
- [ ] No secrets, PII, or restricted coordinates in any artifacts

[Back to top](#top)

---

## Troubleshooting

**Hard fail (must fix; do not merge/run):**
- Scope violation (touched forbidden schema/table/label)
- Observed diffs exceed declared limits
- Protected domain fingerprint changed
- Missing rollback when `requires_rollback: true`
- Receipt generation missing or invalid
- Secrets scan failure

**Review-required (manual approval needed):**
- Performance-impacting index rebuilds beyond typical thresholds
- Large but declared backfills (must include staged plan and monitoring)

**Informational (expected changes):**
- New indexes/constraints exactly as declared
- Schema fingerprint change consistent with forward script

[Back to top](#top)

---

## Glossary

- **Migration:** Controlled mutation of a rebuildable store (schema/index/graph shape) with receipts + rollback.
- **Baseline:** Pre/post snapshot used to detect and summarize blast radius.
- **Diff:** Declared-vs-observed change summary; must be bounded and reviewable.
- **Run receipt:** Audit record of who/what/when/why + inputs/outputs + validation results.
- **PROV:** W3C provenance model representation (optional but recommended for deep lineage).
- **Protected domain:** Governance-sensitive schemas/labels/namespaces that require explicit approval to mutate.

---

<details>
<summary>Appendix: “Do not do this” guardrails</summary>

- Do not delete or rewrite already-merged migrations.
- Do not run migrations manually against production.
- Do not weaken scope limits “to get CI green.”
- Do not log secrets, raw DSNs, PII, or restricted coordinates into baselines/diffs/receipts.
- Do not mutate canonical truth zones (RAW/PROCESSED/CATALOG) via migrations.

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
