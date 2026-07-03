<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-data-readme
title: migrations/data/ — Data Migration Plans, Backfills, and Reversible Data-State Changes
type: per-directory-readme
version: v1
status: draft
owners:
  - <data-steward>
  - <migration-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - migrations/README.md
  - migrations/database/
  - migrations/schema/
  - migrations/graph/
  - migrations/rollback/
  - data/raw/
  - data/work/
  - data/quarantine/
  - data/processed/
  - data/catalog/
  - data/published/
  - data/registry/
  - schemas/contracts/v1/
  - contracts/
  - policy/
  - release/
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
tags:
  - kfm
  - migrations
  - data-migration
  - backfill
  - lifecycle
  - rollback
  - provenance
  - validation
  - auditability
notes:
  - "Data migrations are governed data-state changes. They are not raw source storage, processed outputs, release artifacts, schemas, policy bundles, or publication approvals."
  - "Every data migration must have a corresponding rollback entry under migrations/rollback/, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/data/` — Data Migration Plans, Backfills, and Reversible Data-State Changes

> **One-line purpose.** Hold governed data migration plans and scripts that change KFM data state while preserving lifecycle boundaries, provenance, validation, rollback, and auditability.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![lane](https://img.shields.io/badge/lane-data_migrations-blueviolet)
![rollback](https://img.shields.io/badge/rollback-required-red)
![lifecycle](https://img.shields.io/badge/lifecycle-preserve_success-success)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Migration contract](#migration-contract) · [Required migration record](#required-migration-record) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/data/` is the lane for governed KFM data migrations: controlled backfills, corrections, relocations, lifecycle-state changes, derived-data rebuilds, catalog alignment passes, and data-shape repair operations that affect persisted data state.

A data migration must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Data migrations do not publish data by themselves. Publication remains a governed release transition with evidence, policy, review, rights/sensitivity checks, release state, correction path, and rollback path.

Use this lane when the change is primarily about **moving, repairing, rebuilding, normalizing, or backfilling data records or artifacts**. Use another migration lane when the change is primarily about database structure, schema contracts, graph/triplet topology, or rollback mechanics.

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-directory README |
| **Owning responsibility root** | `migrations/` |
| **Subpath role** | `data/` — governed data-state migrations, backfills, data repair plans, lifecycle movement plans, and validation notes |
| **Authority level** | Draft operational guidance. Directory Rules, accepted ADRs, schemas, contracts, policy, release gates, and runbooks outrank this README. |
| **Lifecycle phase** | Data migrations may touch lifecycle data, but this folder does not store lifecycle data itself. |
| **Default posture** | Smallest reversible change; cite-or-abstain; preserve provenance; validate before promotion; rollback entry required |
| **Owners** | `<data-steward>`, `<migration-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Data steward + migration steward for all data migrations; release steward when published artifacts, release state, rollback targets, or public payloads are affected |
| **Directory Rules basis** | `migrations/` includes `data/` and requires every migration to have a corresponding entry under `migrations/rollback/`. |

[Back to top](#top)

---

## Repo fit

```text
Kansas-Frontier-Matrix/
└── migrations/
    ├── README.md
    ├── database/
    ├── schema/
    ├── data/          ◀── you are here
    │   └── README.md
    ├── graph/
    └── rollback/
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `migrations/data/` | Data-state migration plans, backfills, repair scripts, lifecycle movement plans, validation notes | Source data, release artifacts, schemas, policy bundles, rollback records themselves |
| `migrations/database/` | Database structure and storage-engine migrations | Data lifecycle semantics unless paired with data migration |
| `migrations/schema/` | Contract/schema migration plans | Data backfill execution unless required by the schema change |
| `migrations/graph/` | Graph/triplet migration plans and topology changes | Raw data or processed artifact storage |
| `migrations/rollback/` | Rollback entries for every migration | Primary migration scripts unless rollback-specific |
| `data/raw/` | Immutable or source-close raw inputs | Migration scripts or plans |
| `data/work/` | Work-in-progress transformation area | Migration authority |
| `data/quarantine/` | Held, unsafe, rights-uncertain, or policy-blocked material | Migration scripts or publication decisions |
| `data/processed/` | Validated derived data outputs | Migration code unless explicitly generated artifact references are needed |
| `data/catalog/` | Catalog records and discovery metadata | Migration plans |
| `data/published/` | Released public artifacts | Migration scripts or rollback records |
| `policy/` | Allow / deny / restrict / abstain rules | Migration code |
| `release/` | Release manifests, rollback cards, correction notices | Data migration scripts |

[Back to top](#top)

---

## What belongs here

Use `migrations/data/` for migration material such as:

- Data backfill plans and scripts.
- Data repair or normalization plans.
- Lifecycle movement plans between non-public states, when governed and auditable.
- Rebuild plans for derived data after source, schema, contract, or policy changes.
- Catalog/triplet alignment data updates when the primary change is data-state repair.
- Idempotent migration runners or small scripts that operate on declared inputs and outputs.
- Dry-run reports and sanitized validation summaries.
- Data checksums, row/feature counts, and invariant checks when safe to publish.
- Migration manifests that describe scope, affected objects, evidence, policy sensitivity, validation, and rollback reference.
- Forward-fix notes when rollback is unsafe.

Accepted file types are Markdown plans, migration manifests, scripts, SQL fragments, notebooks only when explicitly justified, sanitized reports, and validation summaries. Keep each migration inspectable and paired with rollback documentation.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/data/` as a data lake, source registry, release folder, or policy/schema home.

The following must not live here:

- Raw source data, downloaded datasets, local extracts, caches, tiles, rasters, GeoParquet files, PMTiles, COGs, shapefiles, or bulk data artifacts.
- WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads.
- Release manifests, rollback cards, correction notices, publication approvals, or signed receipts.
- Policy bundles or allow/deny rules.
- JSON Schemas or canonical contracts.
- Source descriptors, source registry records, or evidence bundles unless the migration record links to them by reference.
- Secrets, tokens, credentials, private endpoints, database passwords, API keys, `.env` files, or production connection strings.
- Unredacted sensitive data, living-person details, DNA/genomic material, precise restricted locations, archaeology/burial/sacred-site data, rare-species exact locations, or critical infrastructure details.
- One-off destructive scripts without scope, dry-run, validation, rollback, owner, and review path.

If a data artifact or secret lands here, move it to the correct lifecycle or secret-handling path and record the correction. If sensitive material is exposed, treat it as a security or governance incident.

[Back to top](#top)

---

## Migration contract

Every data migration should be designed as a governed state transition, not a convenience edit.

### Required properties

- **Named scope.** Identify exactly what data family, lifecycle phase, collection, table, files, records, or artifacts are affected.
- **Evidence basis.** Link the source evidence, issue, receipt, validation failure, schema change, policy change, or release need that justifies the migration.
- **Lifecycle preservation.** Do not skip RAW / WORK / QUARANTINE / PROCESSED / CATALOG / TRIPLET / PUBLISHED boundaries.
- **Idempotence where practical.** Re-running should be safe, detected, or explicitly blocked.
- **Dry-run mode where practical.** Prefer count-only, diff-only, or preview reports before mutation.
- **Deterministic identity.** Preserve stable IDs when possible; record intentional ID changes.
- **Provenance.** Record what changed, why, by whom/tool, when, and with what inputs.
- **Validation.** Define checks before running the migration.
- **Rollback or forward fix.** Every migration must link to `migrations/rollback/`.
- **Sensitivity review.** Rights, policy, living-person, DNA, archaeology, rare-species, and infrastructure risks must fail closed until resolved.

### Naming convention

Use date-prefixed, descriptive names:

```text
YYYYMMDD-short-purpose.md
YYYYMMDD-short-purpose.py
YYYYMMDD-short-purpose.sql
```

Examples:

```text
20260703-normalize-county-fips.md
20260703-backfill-source-ref-links.py
20260703-repair-catalog-layer-slugs.sql
```

The rollback entry should share the same prefix and purpose:

```text
migrations/rollback/20260703-normalize-county-fips.md
```

[Back to top](#top)

---

## Required migration record

Every data migration should have a Markdown record before it is run against shared or release-relevant state.

```markdown
# <YYYYMMDD-short-purpose>

## Status
PROPOSED / APPROVED / RUNNING / COMPLETED / FAILED / ROLLED_BACK / FORWARD_FIXED

## Owner
<data-steward or migration owner>

## Scope
<affected lifecycle phase, datasets, records, tables, artifacts, or stores>

## Evidence basis
<link to issue, validation report, EvidenceBundle, receipt, schema change, policy change, or release need>

## Sensitivity and rights review
<public / internal / restricted / quarantine; rights and sensitivity notes>

## Pre-conditions
<required schema version, release state, backups, locks, input manifests, dry-run state>

## Migration plan
<steps, scripts, expected changes>

## Dry-run output
<counts, diffs, warnings, no sensitive payloads>

## Validation plan
<checks before and after>

## Rollback reference
<migrations/rollback/YYYYMMDD-short-purpose.md>

## Run receipt
<timestamp, command or workflow id, operator/tool, commit, output summary>

## Post-run verification
<checksums, counts, invariant checks, sample review>

## Follow-up
<docs, release notes, drift register, open questions>
```

[Back to top](#top)

---

## Validation

Data migrations require evidence before and after execution.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Migration belongs in `migrations/data/` | PR review |
| Rollback entry | Matching `migrations/rollback/` record exists | Path link |
| Scope | Affected data and lifecycle phase are named | Migration record |
| Evidence basis | Migration has a documented reason | Evidence/ref/issue link |
| Dry run | Migration can preview changes where practical | Dry-run report |
| Secret scan | No secrets or private connection strings committed | Secret scan result |
| Sensitivity review | Restricted material fails closed or stays quarantined | Policy/sensitivity note |
| Lifecycle check | Migration does not skip promotion gates | Reviewer signoff |
| Identity check | Stable IDs are preserved or remapped intentionally | ID diff / mapping note |
| Provenance check | Inputs, operator/tool, timestamp, and output summary are recorded | Run receipt |
| Data invariant check | Counts, checksums, constraints, or sample checks pass | Validation report |
| Release impact | Any published artifact impact is reviewed by release steward | Release note or N/A |

### Suggested command posture

Commands are migration-specific. Any executable migration should provide its own safe dry-run and run instructions. Do not embed production credentials, private paths, or unsafe destructive defaults in scripts or docs.

A migration is not ready for shared state until reviewers can answer:

1. What changes?
2. Why does it change?
3. What evidence supports the change?
4. What could be harmed?
5. What validates it?
6. How is it rolled back or forward-fixed?
7. How is the result audited?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no migration behavior | Docs steward or migration steward |
| Data backfill or repair affecting non-public work state | Data steward + migration steward |
| Migration touching RAW or source-close material | Source steward + data steward + migration steward |
| Migration touching QUARANTINE material | Data steward + policy/sensitivity reviewer |
| Migration affecting catalog/triplet/public layer references | Catalog/graph steward + data steward |
| Migration affecting published artifacts or release state | Release steward + data steward + migration steward |
| Migration involving living-person, DNA/genomic, archaeology, rare-species, infrastructure, or rights-uncertain material | Policy/sensitivity reviewer + relevant domain steward + release steward if public impact exists |
| Destructive migration | Data steward + migration steward + rollback reviewer + release steward if public impact exists |
| Forward-fix-only migration | Migration steward + data steward + documented risk acceptance |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/`, `migrations/data/`, and `migrations/rollback/`.
- [ ] Confirm standard migration manifest filename convention.
- [ ] Confirm whether migration scripts use Python, SQL, workflow jobs, notebooks, or a mixed pattern.
- [ ] Confirm dry-run and run receipt format.
- [ ] Confirm validation tooling under `tests/` or `tools/validators/`.
- [ ] Confirm backup/snapshot expectations before destructive migrations.
- [ ] Confirm whether migration records link to issue IDs, EvidenceBundle IDs, receipt IDs, release IDs, or all of the above.
- [ ] Confirm sensitivity-review workflow for policy-significant data migrations.
- [ ] Confirm rollback record template under `migrations/rollback/`.
- [ ] Confirm how completed migration receipts are indexed.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First concrete data migration, backfill, repair, lifecycle movement, catalog/triplet alignment, release-impacting migration, or rollback-linked migration PR |
