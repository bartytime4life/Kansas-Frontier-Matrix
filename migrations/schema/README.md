<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-schema-readme
title: migrations/schema/ — Schema and Contract Migration Governance
type: per-directory-readme
version: v1
status: draft
owners:
  - <schema-steward>
  - <contract-steward>
  - <migration-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - migrations/README.md
  - migrations/database/
  - migrations/data/
  - migrations/graph/
  - migrations/rollback/
  - schemas/contracts/v1/
  - contracts/
  - policy/
  - release/
  - apps/governed-api/
  - apps/explorer-web/
  - packages/
  - data/catalog/
  - data/processed/
  - data/published/
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
tags:
  - kfm
  - migrations
  - schema
  - contracts
  - compatibility
  - versioning
  - rollback
  - validation
  - provenance
  - auditability
notes:
  - "Schema migrations are governed compatibility and contract-shape transitions. They are not database DDL by themselves, raw data storage, data backfill authority, policy authority, release authority, or publication approval."
  - "Every schema migration must have a corresponding rollback entry under migrations/rollback/, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/schema/` — Schema and Contract Migration Governance

> **One-line purpose.** Hold governed schema and contract migration plans that change KFM object shapes, compatibility rules, version posture, and validation expectations while preserving provenance, reviewability, rollback, and release safety.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![lane](https://img.shields.io/badge/lane-schema_migrations-blueviolet)
![rollback](https://img.shields.io/badge/rollback-required-red)
![compatibility](https://img.shields.io/badge/compatibility-review_required-orange)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema migration contract](#schema-migration-contract) · [Required migration record](#required-migration-record) · [Compatibility classes](#compatibility-classes) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/schema/` is the lane for schema and contract migration governance: object-shape transitions, schema version moves, DTO compatibility changes, field additions/removals, enum/value changes, validation posture changes, crosswalk updates, and migration plans that keep producers and consumers aligned.

This folder protects contract migration discipline without weakening the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Schema migrations do not publish KFM data by themselves. They define how schema and contract changes are introduced, validated, adopted, and recovered from. Publication remains a governed release transition with evidence, policy, review state, release state, correction path, and rollback path.

Use this lane when the primary change is **schema/contract compatibility or object-shape migration**. Use another lane when the primary change is database structure, data backfill, graph/triplet topology, or rollback documentation.

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-directory README |
| **Owning responsibility root** | `migrations/` |
| **Subpath role** | `schema/` — schema/contract migration plans, compatibility transitions, version moves, validation posture changes, and consumer/producer coordination notes |
| **Authority level** | Draft operational guidance. Directory Rules, accepted ADRs, `schemas/contracts/v1/`, `contracts/`, policy, release gates, and runbooks outrank this README. |
| **Lifecycle phase** | n/a — schema migration plans, not lifecycle data itself |
| **Default posture** | Backward compatibility preferred; breaking changes require review, migration plan, validation, and rollback/forward-fix record |
| **Owners** | `<schema-steward>`, `<contract-steward>`, `<migration-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Schema/contract steward + migration steward for all schema migrations; app/data/graph/release/policy stewards when producers, consumers, data state, public payloads, or sensitivity are affected |
| **Directory Rules basis** | `migrations/` includes `schema/` and requires every migration to have a corresponding entry under `migrations/rollback/`. |

[Back to top](#top)

---

## Repo fit

```text
Kansas-Frontier-Matrix/
└── migrations/
    ├── README.md
    ├── database/
    ├── schema/        ◀── you are here
    │   └── README.md
    ├── data/
    ├── graph/
    └── rollback/
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `migrations/schema/` | Schema/contract migration plans, compatibility analysis, version-transition notes, producer/consumer migration plans | Canonical schema files, primary data backfills, database DDL, graph rewrites, rollback records themselves |
| `schemas/contracts/v1/` | Machine-checkable schema files | Migration plans unless paired by reference |
| `contracts/` | Human-readable contract meaning and semantics | Migration execution records unless paired by reference |
| `migrations/database/` | Database structure and storage-engine migrations | Schema compatibility as the primary concern |
| `migrations/data/` | Data-state migrations, backfills, repairs, lifecycle movement plans | Schema migration authority |
| `migrations/graph/` | Graph/triplet relationship migrations | Schema migration authority |
| `migrations/rollback/` | Rollback entry for every migration | Primary schema migration records |
| `apps/` | Producers/consumers and API/UI behavior | Schema migration governance |
| `policy/` | Allow / deny / restrict / abstain rules | Schema migration plans |
| `release/` | Release decisions, manifests, rollback cards, correction notices | Schema migration scripts or plans |

[Back to top](#top)

---

## What belongs here

Use `migrations/schema/` for schema and contract migration material such as:

- Schema version transition plans.
- Compatibility matrices for producers and consumers.
- Breaking-change review notes and deprecation plans.
- Field addition, removal, rename, split, merge, or type-change migration plans.
- Enum/value-set change plans.
- DTO or envelope migration notes.
- Crosswalk plans between old and new schema fields.
- Validation posture changes and validator rollout notes.
- Backward-compatibility and forward-compatibility analysis.
- Coordinated migration plans that reference database, data, graph, app, policy, or release changes.
- Dry-run validation summaries and sanitized schema-diff reports.
- Migration manifests that describe affected contracts, schemas, fields, producers, consumers, validation, compatibility class, and rollback reference.
- Forward-fix notes when rollback is unsafe.

Accepted file types are Markdown plans, compatibility matrices, migration manifests, schema-diff summaries, validator rollout notes, and sanitized validation reports. Canonical schemas themselves belong under `schemas/contracts/v1/` unless a specific migration record links to them by path.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/schema/` as a parallel schema authority, data lake, database migration lane, policy lane, or release lane.

The following must not live here:

- Canonical schema files that belong under `schemas/contracts/v1/`.
- Human-readable contract authority that belongs under `contracts/`.
- Database DDL or storage-engine migrations that belong in `migrations/database/`.
- Primary data backfill scripts or data repair migrations that belong in `migrations/data/`.
- Primary graph/triplet topology migrations that belong in `migrations/graph/`.
- Rollback records that belong in `migrations/rollback/`.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads.
- Policy bundles, release manifests, correction notices, publication approvals, or signed release receipts.
- Live credentials, API keys, tokens, private endpoints, `.env` files, database passwords, service-account keys, or production DSNs.
- Schema migration notes that silently weaken evidence, policy, sensitivity, review, or release requirements.
- Breaking changes that lack compatibility analysis, affected-consumer review, validation, and rollback/forward-fix posture.

If a canonical schema, secret, production dataset, or release artifact lands here, move it to the correct governed path and record the correction. If restricted material was exposed, treat it as a security or governance incident.

[Back to top](#top)

---

## Schema migration contract

Every schema migration should be a governed, reviewable, and auditable compatibility transition.

### Required properties

- **Named scope.** Identify affected schema files, contract docs, DTOs, envelopes, fields, enum values, producers, consumers, validators, and public artifacts.
- **Reason.** Link the issue, validation failure, ADR, policy change, release need, producer/consumer mismatch, or evidence requirement that justifies the change.
- **Compatibility class.** State whether the change is additive-compatible, behavior-compatible, deprecating, breaking, forward-fix-only, or documentation-only.
- **Producer/consumer impact.** Name affected apps, packages, workers, validators, catalog records, graph records, API responses, map layers, exports, or release artifacts.
- **Migration order.** State whether schema changes must run before or after database, data, graph, app, policy, or release changes.
- **Validation.** Define schema validation, fixture validation, contract tests, sample payload checks, and release compatibility checks.
- **Deprecation path.** For replacement fields or changed semantics, describe transition window and removal trigger.
- **Lifecycle preservation.** Do not create paths that skip KFM lifecycle or publication gates.
- **Sensitivity preservation.** Do not weaken rights, sensitivity, evidence, or policy fields without explicit review.
- **Rollback or forward fix.** Every migration must link to `migrations/rollback/`.

### Naming convention

Use date-prefixed, descriptive names:

```text
YYYYMMDD-short-purpose.md
YYYYMMDD-short-purpose.compat.md
YYYYMMDD-short-purpose.crosswalk.md
```

Examples:

```text
20260703-add-evidencebundle-required-fields.md
20260703-deprecate-layer-slug-v0.compat.md
20260703-decision-envelope-v2-crosswalk.md
```

The rollback entry should share the same prefix and purpose:

```text
migrations/rollback/20260703-add-evidencebundle-required-fields.md
```

[Back to top](#top)

---

## Required migration record

Every schema migration should have a Markdown record before it is adopted by shared producers, consumers, or release-relevant artifacts.

```markdown
# <YYYYMMDD-short-purpose>

## Status
PROPOSED / APPROVED / RUNNING / COMPLETED / FAILED / ROLLED_BACK / FORWARD_FIXED

## Owner
<schema steward or migration owner>

## Scope
<schema files, contract docs, DTOs, fields, enums, validators, producers, consumers>

## Reason and evidence basis
<link to issue, validation report, ADR, policy change, producer/consumer mismatch, release need, or receipt reference>

## Compatibility class
ADDITIVE_COMPATIBLE / BEHAVIOR_COMPATIBLE / DEPRECATION / BREAKING / FORWARD_FIX_ONLY / DOC_ONLY

## Producer impact
<apps, packages, workers, validators, generated clients, exporters>

## Consumer impact
<governed API, UI, catalog, graph, release, tiles, exports, downstream tools>

## Migration order
<before/after database, data, graph, app, policy, release changes>

## Crosswalk / mapping
<old fields to new fields; no sensitive payloads>

## Validation plan
<schemas, fixtures, contract tests, sample payloads, release compatibility>

## Rollback reference
<migrations/rollback/YYYYMMDD-short-purpose.md>

## Adoption receipt
<timestamp, commit, validator results, affected producers/consumers>

## Post-adoption verification
<tests, sample payloads, public API compatibility, release checks>

## Follow-up
<docs, deprecation removal, release notes, drift register, open questions>
```

[Back to top](#top)

---

## Compatibility classes

| Class | Meaning | Required handling |
|---|---|---|
| `ADDITIVE_COMPATIBLE` | Adds fields or values without breaking existing consumers | Validate producers and consumers; document default/optional behavior |
| `BEHAVIOR_COMPATIBLE` | Shape remains stable but validation or interpretation changes | Document semantic impact and affected validators |
| `DEPRECATION` | Old field/value remains temporarily while replacement is introduced | Define transition window, warnings, removal trigger, and crosswalk |
| `BREAKING` | Existing producers or consumers must change | Require migration order, affected-consumer review, release plan, rollback/forward-fix posture |
| `FORWARD_FIX_ONLY` | Direct rollback is unsafe or invalid | Explain why and link corrective migration or issue |
| `DOC_ONLY` | Contract documentation changes without machine-shape change | Validate no schema or runtime behavior changed |

[Back to top](#top)

---

## Validation

Schema migrations require evidence before adoption and after rollout.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Migration belongs in `migrations/schema/` | PR review |
| Rollback entry | Matching `migrations/rollback/` record exists | Path link |
| Scope | Affected schemas, contracts, DTOs, fields, and consumers are named | Migration record |
| Compatibility class | Compatibility posture is explicit | Migration record |
| Producer review | Producers that emit the shape are named and checked | Impact note |
| Consumer review | Consumers that read the shape are named and checked | Impact note |
| Crosswalk | Old/new mapping exists for renamed/split/merged fields | Crosswalk note |
| Validation suite | Schemas, fixtures, contract tests, and sample payloads pass | Validation report |
| Sensitivity preservation | Rights, policy, evidence, review, and sensitivity fields are not weakened silently | Reviewer signoff |
| Release impact | Public payload and artifact impacts are reviewed | Release note or N/A |
| Adoption receipt | Adoption summary is recorded | Receipt section |

A schema migration is not ready until reviewers can answer:

1. What shape or contract changes?
2. Why does it change?
3. Who produces it?
4. Who consumes it?
5. Is it backward-compatible?
6. What validates it?
7. How is it rolled back or forward-fixed?
8. What release or public API impact exists?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no migration behavior | Docs steward or migration steward |
| Additive compatible schema migration | Schema steward + affected producer owner |
| Validator behavior change | Schema steward + validator owner + affected consumer owner |
| Contract semantic change | Contract steward + schema steward + affected consumer owner |
| Deprecation migration | Schema steward + affected producer/consumer owners + migration steward |
| Breaking schema migration | Schema steward + contract steward + migration steward + release steward |
| Schema migration paired with database change | Schema steward + database steward + migration steward |
| Schema migration paired with data backfill/repair | Schema steward + data steward + migration steward |
| Schema migration paired with graph/triplet change | Schema steward + graph steward + migration steward |
| Migration affecting public API, map layers, exports, tiles, or published artifacts | Release steward + schema steward + governed API owner |
| Migration involving rights, sensitivity, living-person, DNA/genomic, archaeology, rare-species, infrastructure, or policy fields | Policy/sensitivity reviewer + schema steward + relevant domain steward |
| Forward-fix-only migration | Migration steward + schema steward + documented risk acceptance |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/`, `migrations/schema/`, `schemas/contracts/v1/`, `contracts/`, and `migrations/rollback/`.
- [ ] Confirm schema versioning convention.
- [ ] Confirm compatibility policy for additive, deprecating, and breaking changes.
- [ ] Confirm whether schema migration records are required in the same PR as schema changes.
- [ ] Confirm validator tooling under `tests/` or `tools/validators/`.
- [ ] Confirm fixture and sample-payload locations.
- [ ] Confirm generated-client or DTO regeneration process, if any.
- [ ] Confirm how adoption receipts are recorded and indexed.
- [ ] Confirm release-steward review trigger for public-impacting schema migrations.
- [ ] Confirm rollback record template under `migrations/rollback/`.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First concrete schema migration, compatibility change, validator behavior change, deprecation, breaking contract change, public API payload change, or rollback-linked migration PR |
