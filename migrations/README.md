<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-readme
title: migrations/ — Database, Schema, Data, Graph, and Rollback Migration Governance Root
type: responsibility-root-readme
version: v1
status: draft
owners:
  - <migration-steward>
  - <database-steward>
  - <schema-steward>
  - <data-steward>
  - <graph-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
  - migrations/database/
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
  - data/registry/
  - policy/
  - release/
  - apps/governed-api/
  - apps/explorer-web/
  - packages/
tags:
  - kfm
  - migrations
  - database
  - schema
  - data
  - graph
  - rollback
  - forward-fix
  - validation
  - provenance
  - auditability
notes:
  - "This README defines the migrations/ responsibility root. It governs migration planning and recovery posture; it is not raw data storage, schema authority, policy authority, release authority, or publication approval."
  - "Every migration must have a corresponding rollback entry under migrations/rollback/, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/` — Database, Schema, Data, Graph, and Rollback Migration Governance Root

> **One-line purpose.** Keep KFM database, schema, data, graph, and rollback migrations small, reviewed, validated, provenance-bearing, rollback-aware, and aligned with the governed lifecycle.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![rollback](https://img.shields.io/badge/rollback_entry-required-red)
![lifecycle](https://img.shields.io/badge/lifecycle-preserve_success-success)
![validation](https://img.shields.io/badge/validation-required-orange)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Root contract](#root-contract) · [Directory map](#directory-map) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Migration lifecycle](#migration-lifecycle) · [Lane contracts](#lane-contracts) · [Inputs and outputs](#inputs-and-outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/` is the KFM responsibility root for governed change to database structure, schema/contract compatibility, data state, graph/triplet topology, and migration recovery posture.

This root exists to ensure migrations are not casual edits. They are governed state transitions that must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Migrations may prepare, repair, reshape, rebuild, or recover system state. They do **not** publish data by themselves, certify evidence, approve policy, replace release gates, or make generated output authoritative.

Every migration must answer:

1. What changes?
2. Why does it change?
3. What evidence, issue, validation failure, schema need, release need, or correction justifies it?
4. What can be harmed?
5. What validates it?
6. What rollback or forward-fix record exists?
7. How is the result audited?

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Responsibility-root README |
| **Owning responsibility root** | `migrations/` |
| **Root role** | Database, schema, data, graph, and rollback migration governance |
| **Authority level** | Draft operational governance. Directory Rules, accepted ADRs, schemas, contracts, policy, release gates, and runbooks outrank this README. |
| **Lifecycle phase** | n/a — migration records and scripts, not lifecycle data themselves |
| **Default posture** | Smallest reversible change; dry-run where practical; rollback record required; provenance and validation required; fail closed for sensitivity/rights uncertainty |
| **Owners** | `<migration-steward>`, `<database-steward>`, `<schema-steward>`, `<data-steward>`, `<graph-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Migration steward + affected lane steward for all migrations; release/policy/security reviewers when public, sensitive, security, or incident impact exists |
| **Directory Rules basis** | `migrations/` includes `database/`, `schema/`, `data/`, `graph/`, and `rollback/`; every migration must have a corresponding rollback entry. |

[Back to top](#top)

---

## Root contract

`migrations/` owns migration governance. It does **not** own the canonical truth of data, schemas, policy, release state, or runtime behavior.

### This root must preserve

- **Lifecycle boundaries.** No migration may skip KFM lifecycle gates.
- **Rollback discipline.** Every migration has a rollback or forward-fix record under `migrations/rollback/`.
- **Evidence basis.** Migrations should link to the issue, receipt, EvidenceBundle, validation failure, schema need, release need, or correction that justifies the change.
- **Provenance.** Migration records should show what changed, why, who/tool ran it, when, against what commit/state, and what validation passed.
- **Validation.** Migrations need preflight and post-run checks appropriate to their lane.
- **Sensitivity protection.** Rights, living-person data, DNA/genomic data, precise restricted locations, archaeology/burial/sacred-site data, rare-species exact locations, infrastructure, and policy-sensitive material fail closed until reviewed.
- **Reversibility where practical.** Prefer small, reversible changes; when rollback is unsafe, document forward-fix-only with reason.
- **Separation of authority.** Migrations can update state, but they do not replace release approval, policy decisions, evidence review, or public publication gates.

### This root must not decide

- Whether a claim is true.
- Whether evidence is sufficient for publication.
- Whether sensitive material may become public.
- Whether a release is approved.
- Whether an AI-generated or inferred relation is authoritative.
- Whether policy allows, denies, restricts, or abstains.

Those decisions remain in the relevant evidence, policy, review, release, source, and application layers.

[Back to top](#top)

---

## Directory map

```text
migrations/
├── README.md
├── database/
├── schema/
├── data/
├── graph/
└── rollback/
```

### Lane summary

| Lane | Primary responsibility | Required pairing |
|---|---|---|
| `migrations/database/` | Database DDL, storage structure, indexes, constraints, roles, views, database functions, and storage-state changes | `migrations/rollback/<same-prefix>.md` |
| `migrations/schema/` | Schema/contract compatibility, DTO shape, validation posture, version transitions, field/value changes, and producer/consumer migration plans | `migrations/rollback/<same-prefix>.md` |
| `migrations/data/` | Data backfills, repairs, normalizations, lifecycle-state movement plans, derived-data rebuilds, and catalog/triplet data alignment where data state is primary | `migrations/rollback/<same-prefix>.md` |
| `migrations/graph/` | Graph/triplet relationship rewrites, topology changes, identity remaps, projection rebuilds, graph indexes, and evidence-link repairs | `migrations/rollback/<same-prefix>.md` |
| `migrations/rollback/` | Rollback and forward-fix records for every migration | Paired migration in a sibling lane |

[Back to top](#top)

---

## What belongs here

Use `migrations/` for migration material such as:

- Migration root documentation and lane READMEs.
- Database migration plans and scripts under `migrations/database/`.
- Schema/contract migration records under `migrations/schema/`.
- Data migration/backfill/repair records under `migrations/data/`.
- Graph/triplet migration records under `migrations/graph/`.
- Rollback and forward-fix records under `migrations/rollback/`.
- Migration manifests, dry-run summaries, validation summaries, and adoption/run receipts.
- Cross-lane coordination plans when database, schema, data, graph, app, policy, and release changes must happen in a controlled order.
- Compatibility notes and release-impact notes.
- Non-sensitive references to backups, snapshots, receipts, issues, EvidenceBundles, policy decisions, or release records.

Accepted file types vary by lane: Markdown records, SQL, scripts, query fragments, compatibility matrices, sanitized validation reports, and migration manifests are acceptable when they belong to the lane and contain no secrets or bulk data.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/` as a data lake, backup store, schema authority, policy authority, release lane, or secret store.

The following must not live here:

- Raw datasets, bulk source downloads, database dumps, graph dumps, backups, tiles, rasters, COGs, PMTiles, generated public artifacts, or lifecycle payloads.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data artifacts.
- Canonical schema files that belong under `schemas/contracts/v1/`.
- Human-readable contract authority that belongs under `contracts/`.
- Policy bundles or allow/deny rules that belong under `policy/`.
- Release manifests, release rollback cards, correction notices, publication approvals, or signed release receipts that belong under `release/`.
- Live credentials, connection strings, API keys, tokens, private endpoints, `.env` files, service-account keys, kubeconfigs, or production DSNs.
- Unredacted sensitive data, incident details, private topology, or vulnerability working notes.
- Destructive migrations without scope, evidence basis, validation, rollback/forward-fix record, owner, and review path.

If a data artifact, secret, backup, or sensitive operational file lands here, move it to the correct governed path or secure store and record the correction. If restricted material was exposed, treat it as a security or governance incident.

[Back to top](#top)

---

## Migration lifecycle

A migration should move through a controlled review path.

```text
PROPOSED -> REVIEWED -> APPROVED -> READY -> RUN / ADOPTED -> VERIFIED -> COMPLETED
                                      \-> BLOCKED
                                      \-> FAILED -> ROLLED_BACK / FORWARD_FIXED
```

### Minimum states

| State | Meaning |
|---|---|
| `PROPOSED` | Migration idea or draft record exists. Not ready to run. |
| `REVIEWED` | Scope, evidence basis, risk, validation, and rollback posture reviewed. |
| `APPROVED` | Required stewards have approved the migration. |
| `READY` | Preconditions are satisfied. |
| `RUN` / `ADOPTED` | Migration has been applied or adopted by producers/consumers. |
| `VERIFIED` | Post-migration checks passed. |
| `COMPLETED` | Migration is complete and recorded. |
| `FAILED` | Migration failed and requires rollback or forward fix. |
| `ROLLED_BACK` | Recovery returned state to approved prior/safe state. |
| `FORWARD_FIXED` | Direct rollback was unsafe; a governed corrective migration restored safety. |
| `BLOCKED` | Migration cannot proceed until a named blocker is resolved. |

[Back to top](#top)

---

## Lane contracts

### `database/`

Use for database structure and storage-state changes. Database migrations should name affected objects, dependency order, lock/downtime risk, backup/snapshot posture, preflight checks, validation, and rollback reference.

### `schema/`

Use for schema and contract compatibility transitions. Schema migrations should name affected schemas, fields, enums, producers, consumers, validators, compatibility class, crosswalks, validation, and rollback reference.

### `data/`

Use for data-state migrations, backfills, repairs, and rebuilds. Data migrations should name affected lifecycle phase, dataset, records, artifacts, evidence basis, sensitivity review, dry-run output, validation, and rollback reference.

### `graph/`

Use for graph/triplet relationship migrations. Graph migrations should name affected node/edge/triplet families, evidence links, truth posture, identity impact, sensitivity review, graph invariants, validation, and rollback reference.

### `rollback/`

Use for rollback and forward-fix records. Rollback records should name the paired migration, recovery decision class, reason, preconditions, risks, validation plan, release impact, and execution/adoption summary.

[Back to top](#top)

---

## Inputs and outputs

### Inputs

`migrations/` may consume:

- Directory Rules and accepted ADRs.
- Schema and contract changes from `schemas/contracts/v1/` and `contracts/`.
- Validation failures from tests, validators, CI, or runbooks.
- EvidenceBundle, receipt, issue, catalog, graph, or release references.
- Policy and sensitivity review results.
- Data-quality findings.
- Release needs or correction requests.
- Database, app, runtime, API, UI, worker, or export compatibility requirements.

### Outputs

`migrations/` may produce:

- Migration records.
- Migration scripts or query fragments in the correct lane.
- Compatibility matrices.
- Dry-run and validation summaries.
- Run/adoption receipts.
- Rollback or forward-fix records.
- Drift/correction follow-up notes.
- Review evidence for release-impacting changes.

`migrations/` outputs do not publish KFM data by themselves.

[Back to top](#top)

---

## Validation

Every migration should include evidence appropriate to its lane.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Migration belongs in the chosen lane | PR review |
| Rollback record | Matching `migrations/rollback/` entry exists | Path link |
| Scope | Affected objects, data, schemas, or graph elements are named | Migration record |
| Evidence basis | Reason for migration is documented | Issue/ref/receipt/EvidenceBundle link |
| Sensitivity review | Restricted material fails closed or remains non-public | Policy/sensitivity note |
| Dry run/preflight | Changes can be previewed where practical | Dry-run summary |
| Secret scan | No credentials, private endpoints, or sensitive artifacts committed | Secret scan result |
| Lifecycle preservation | Migration does not skip lifecycle or publication gates | Reviewer signoff |
| Identity/provenance | Stable IDs, remaps, and provenance are recorded | Mapping/receipt note |
| Compatibility | Producers/consumers remain compatible or migration order is named | Compatibility note |
| Release impact | Public API/map/export/artifact impact is reviewed | Release note or N/A |
| Post-check | Post-migration invariants pass | Validation report |

A migration is not ready for shared or release-relevant state until reviewers can answer:

1. What changes?
2. Why does it change?
3. What validates it?
4. What is the rollback or forward-fix posture?
5. What public, policy, rights, sensitivity, or release impact exists?
6. Who reviewed it?
7. Where is the run or adoption receipt recorded?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no migration behavior | Docs steward or migration steward |
| Database migration | Database steward + migration steward |
| Schema/contract migration | Schema/contract steward + migration steward |
| Data migration/backfill/repair | Data steward + migration steward |
| Graph/triplet migration | Graph steward + migration steward |
| Rollback or forward-fix record | Affected lane steward + migration steward |
| Migration affecting public API, map layers, tiles, exports, or published artifacts | Release steward + affected lane steward |
| Migration involving rights, sensitivity, living-person, DNA/genomic, archaeology, rare-species, infrastructure, or policy fields | Policy/sensitivity reviewer + affected domain steward |
| Migration involving credentials, secret references, or security incident recovery | Security owner + affected lane steward |
| Destructive or forward-fix-only migration | Migration steward + affected lane steward + documented risk acceptance |
| Cross-lane migration | All affected lane stewards + migration steward |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/` and each migration lane.
- [ ] Confirm migration filename and ordering convention.
- [ ] Confirm required migration record template location.
- [ ] Confirm whether rollback entries must be in the same PR as paired migrations.
- [ ] Confirm database migration runner/tooling.
- [ ] Confirm schema versioning and compatibility policy.
- [ ] Confirm data migration dry-run and receipt format.
- [ ] Confirm graph/triplet migration tooling and invariants.
- [ ] Confirm validation commands under `tests/` or `tools/validators/`.
- [ ] Confirm backup/snapshot expectations by migration class.
- [ ] Confirm how migration receipts are indexed.
- [ ] Confirm release-steward review triggers for public-impacting migrations.
- [ ] Confirm incident-response handoff when a migration follows security or exposure failure.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft root README replacing short proposed placeholder |
| Next review trigger | Any concrete database, schema, data, graph, rollback, forward-fix, public-impacting, sensitive, destructive, or cross-lane migration PR |
