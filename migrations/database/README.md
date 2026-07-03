<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-database-readme
title: migrations/database/ — Database Structure Migrations and Storage-State Change Control
type: per-directory-readme
version: v1
status: draft
owners:
  - <database-steward>
  - <migration-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - migrations/README.md
  - migrations/schema/
  - migrations/data/
  - migrations/graph/
  - migrations/rollback/
  - schemas/contracts/v1/
  - contracts/
  - data/raw/
  - data/work/
  - data/quarantine/
  - data/processed/
  - data/catalog/
  - data/published/
  - policy/
  - release/
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
tags:
  - kfm
  - migrations
  - database
  - storage
  - ddl
  - rollback
  - validation
  - auditability
  - provenance
notes:
  - "Database migrations are governed storage-structure changes. They are not schema-contract authority, raw/source storage, data backfill authority by themselves, release authority, or policy authority."
  - "Every database migration must have a corresponding rollback entry under migrations/rollback/, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/database/` — Database Structure Migrations and Storage-State Change Control

> **One-line purpose.** Hold governed database migration plans and scripts that change storage structure while preserving KFM lifecycle boundaries, validation, provenance, rollback, and release safety.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![lane](https://img.shields.io/badge/lane-database_migrations-blueviolet)
![rollback](https://img.shields.io/badge/rollback-required-red)
![ddl](https://img.shields.io/badge/DDL-review_required-orange)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Database migration contract](#database-migration-contract) · [Required migration record](#required-migration-record) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/database/` is the lane for database-structure migrations: table creation, table alteration, index changes, constraints, storage engine changes, materialized view changes, database-owned enum changes, trigger/function changes, extension setup, database permissions, and storage-layout changes that affect how KFM persists governed data.

This folder protects database change discipline without weakening the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Database migrations do not publish KFM data by themselves. They prepare or alter storage structures. Publication remains a governed release transition with evidence, policy, review state, release state, correction path, and rollback path.

Use this lane when the primary change is **database structure or database-managed storage behavior**. Use another lane when the primary change is contract/schema shape, data backfill, graph/triplet topology, or rollback documentation.

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-directory README |
| **Owning responsibility root** | `migrations/` |
| **Subpath role** | `database/` — database structure migrations, DDL plans, storage-state changes, database permission changes, validation notes |
| **Authority level** | Draft operational guidance. Directory Rules, accepted ADRs, schema contracts, database runbooks, policy, and release gates outrank this README. |
| **Lifecycle phase** | n/a — database migration scripts and plans, not lifecycle data itself |
| **Default posture** | Smallest reversible change; dry-run where practical; backup/snapshot awareness; rollback entry required; no secrets |
| **Owners** | `<database-steward>`, `<migration-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Database steward + migration steward for all database migrations; schema/data/release stewards when contracts, data state, or public payloads are affected |
| **Directory Rules basis** | `migrations/` includes `database/` and requires every migration to have a corresponding entry under `migrations/rollback/`. |

[Back to top](#top)

---

## Repo fit

```text
Kansas-Frontier-Matrix/
└── migrations/
    ├── README.md
    ├── database/      ◀── you are here
    │   └── README.md
    ├── schema/
    ├── data/
    ├── graph/
    └── rollback/
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `migrations/database/` | Database DDL, indexes, constraints, views, database functions, storage layout, permission migrations, validation notes | Data backfills, schema-contract authority, release artifacts, rollback records themselves |
| `migrations/schema/` | Schema/contract migration plans and compatibility notes | Database DDL unless paired with database migration |
| `migrations/data/` | Data-state migrations, backfills, repairs, lifecycle movement plans | Database structure as the primary concern |
| `migrations/graph/` | Graph/triplet topology migrations | Relational/object database DDL unless graph storage structure is the target |
| `migrations/rollback/` | Rollback entry for every migration | Primary migration scripts unless rollback-specific |
| `schemas/contracts/v1/` | Machine-checkable schemas and DTO shape | Database migrations |
| `contracts/` | Human-readable contract meaning | Database scripts |
| `data/*` | Lifecycle data stores | Migration authority or scripts |
| `policy/` | Allow / deny / restrict / abstain rules | Database DDL |
| `release/` | Release decisions, manifests, rollback cards, correction notices | Database migration scripts |

[Back to top](#top)

---

## What belongs here

Use `migrations/database/` for database migration material such as:

- DDL migration plans and scripts.
- Table, column, constraint, enum, view, materialized view, index, trigger, and function changes.
- Database extension setup or removal, when approved.
- Database-level role or permission changes tied to least privilege.
- Storage partitioning, retention, vacuum/analyze, or performance-structure migrations.
- Database-side compatibility migrations that support contract/schema changes.
- Preflight checks, dry-run notes, and sanitized validation summaries.
- Migration manifests that name scope, database objects, dependency order, lock risk, backup/snapshot expectations, validation, and rollback reference.
- Forward-fix notes when rollback is unsafe.

Accepted file types are Markdown plans, SQL migration files, safe shell wrappers, migration manifests, sanitized explain/plan summaries, and validation notes. Each migration should be reviewable and paired with a rollback record.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/database/` as a database dump, secret store, schema authority, data lake, or release lane.

The following must not live here:

- Full database dumps, exported tables, bulk data files, raw datasets, cached extracts, tiles, rasters, or generated artifacts.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads.
- Live connection strings, credentials, passwords, tokens, private endpoints, `.env` files, service-account keys, or production DSNs.
- Unredacted `EXPLAIN ANALYZE` output or logs containing sensitive row values, internal hostnames, credentials, or restricted data.
- JSON Schemas or canonical contracts that belong under `schemas/contracts/v1/` or `contracts/`.
- Policy bundles, release manifests, rollback cards, correction notices, or publication approvals.
- One-off destructive scripts without scope, lock analysis, backup/snapshot posture, validation, rollback, owner, and review path.
- Database changes that silently expose RAW, WORK, QUARANTINE, internal stores, unpublished candidates, or sensitive data to public services.

If a dump, credential, or sensitive database artifact lands here, move it to the correct governed path or secure store and record the correction. If secrets or restricted data were exposed, treat it as a security/governance incident.

[Back to top](#top)

---

## Database migration contract

Every database migration should be a governed, reviewable, and auditable storage-state transition.

### Required properties

- **Named scope.** Identify the database objects affected: tables, columns, indexes, constraints, views, functions, roles, permissions, extensions, partitions, or stores.
- **Reason.** Link the issue, schema/contract change, validation failure, performance requirement, data migration, graph migration, release need, or incident correction that justifies the migration.
- **Dependency order.** State whether the migration must run before or after schema, data, graph, application, or release changes.
- **Lock and downtime risk.** Mark expected lock class, downtime risk, long-running query risk, and mitigation.
- **Backup/snapshot posture.** Identify whether a backup, snapshot, export, or forward-fix-only plan is required before execution.
- **Dry-run/preflight.** Prefer no-op checks, schema diff, transaction preview, or validation query before mutation.
- **Idempotence.** Re-running should be safe, detected, or explicitly blocked.
- **Least privilege.** Database roles and grants should be minimal and service-specific.
- **Lifecycle preservation.** Do not create public access paths around KFM lifecycle states.
- **Validation.** Define before/after checks.
- **Rollback or forward fix.** Every migration must link to `migrations/rollback/`.

### Naming convention

Use date-prefixed, descriptive names:

```text
YYYYMMDD-short-purpose.md
YYYYMMDD-short-purpose.sql
YYYYMMDD-short-purpose.sh
```

Examples:

```text
20260703-add-evidence-ref-index.md
20260703-add-evidence-ref-index.sql
20260703-tighten-catalog-layer-constraints.sql
```

The rollback entry should share the same prefix and purpose:

```text
migrations/rollback/20260703-add-evidence-ref-index.md
```

[Back to top](#top)

---

## Required migration record

Every database migration should have a Markdown record before it is run against shared or release-relevant state.

```markdown
# <YYYYMMDD-short-purpose>

## Status
PROPOSED / APPROVED / RUNNING / COMPLETED / FAILED / ROLLED_BACK / FORWARD_FIXED

## Owner
<database-steward or migration owner>

## Scope
<database, schema, table, index, view, role, permission, function, extension, or storage object>

## Reason and evidence basis
<link to issue, schema change, validation report, performance report, incident, release need, or EvidenceBundle/receipt reference>

## Dependency order
<before/after app deploy, schema contract update, data migration, graph migration, release, etc.>

## Lock and downtime assessment
<expected lock, duration, risk, mitigation, maintenance window if needed>

## Backup / snapshot posture
<required backup, snapshot, export, or forward-fix-only reason>

## Migration plan
<steps, scripts, transaction boundaries, expected object changes>

## Preflight / dry-run output
<schema diff, validation queries, counts, no sensitive rows>

## Validation plan
<before and after checks>

## Rollback reference
<migrations/rollback/YYYYMMDD-short-purpose.md>

## Run receipt
<timestamp, operator/tool, commit, command/workflow id, sanitized output summary>

## Post-run verification
<constraints, indexes, row counts, query checks, app compatibility checks>

## Follow-up
<docs, release notes, drift register, open questions>
```

[Back to top](#top)

---

## Validation

Database migrations require evidence before and after execution.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Migration belongs in `migrations/database/` | PR review |
| Rollback entry | Matching `migrations/rollback/` record exists | Path link |
| Scope | Affected database objects are named | Migration record |
| Evidence basis | Migration has a documented reason | Evidence/ref/issue link |
| Schema compatibility | Schema contracts and database shape are compatible or migration order is named | Compatibility note |
| Lock risk | Lock/downtime risk is reviewed | Migration record |
| Backup/snapshot | Backup posture is named before destructive or risky changes | Backup note |
| Dry run/preflight | Change can be previewed where practical | Preflight summary |
| Secret scan | No credentials or private DSNs committed | Secret scan result |
| Least privilege | Grants/roles are scoped | Permission review |
| Lifecycle check | Migration does not expose non-public lifecycle stores | Reviewer signoff |
| Post-run check | Constraints, indexes, objects, and compatibility checks pass | Validation report |
| Release impact | Published/public impact is reviewed by release steward | Release note or N/A |

### Suggested command posture

Executable migrations should provide safe, environment-appropriate instructions. Do not embed production credentials, private hostnames, or destructive defaults in scripts or docs.

A migration is not ready for shared state until reviewers can answer:

1. What database object changes?
2. Why does it change?
3. What depends on the change?
4. What locks or downtime could occur?
5. What validates it?
6. How is it rolled back or forward-fixed?
7. How is execution audited?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no migration behavior | Docs steward or migration steward |
| Additive low-risk database object change | Database steward + migration steward |
| Constraint, permission, role, trigger, function, or extension change | Database steward + security owner + migration steward |
| Destructive or table-rewrite migration | Database steward + migration steward + rollback reviewer |
| Migration with application compatibility impact | Database steward + app owner + migration steward |
| Migration paired with schema contract change | Database steward + schema steward + migration steward |
| Migration paired with data backfill/repair | Database steward + data steward + migration steward |
| Migration affecting graph/triplet stores | Database steward + graph steward + migration steward |
| Migration affecting published artifacts, public API behavior, or release state | Release steward + database steward + migration steward |
| Forward-fix-only migration | Migration steward + database steward + documented risk acceptance |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/`, `migrations/database/`, and `migrations/rollback/`.
- [ ] Confirm the database engine(s) KFM supports.
- [ ] Confirm migration runner/tooling: plain SQL, Alembic, Prisma, Flyway, Sqitch, custom runner, or mixed.
- [ ] Confirm filename and ordering convention.
- [ ] Confirm transaction and lock-policy expectations.
- [ ] Confirm backup/snapshot expectations before destructive or high-risk migrations.
- [ ] Confirm dry-run/preflight format.
- [ ] Confirm validation tooling under `tests/` or `tools/validators/`.
- [ ] Confirm how database migration receipts are recorded and indexed.
- [ ] Confirm rollback record template under `migrations/rollback/`.
- [ ] Confirm release-steward review trigger for public-impacting database migrations.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First concrete database migration, DDL script, permission change, index/constraint migration, storage change, schema-paired migration, data-paired migration, or rollback-linked migration PR |
