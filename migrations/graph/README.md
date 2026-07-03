<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-graph-readme
title: migrations/graph/ — Graph, Triplet, Relationship, and Topology Migrations
type: per-directory-readme
version: v1
status: draft
owners:
  - <graph-steward>
  - <migration-steward>
  - <data-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - migrations/README.md
  - migrations/database/
  - migrations/schema/
  - migrations/data/
  - migrations/rollback/
  - data/catalog/
  - data/processed/
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
  - graph
  - triplets
  - relationships
  - topology
  - rollback
  - provenance
  - validation
  - auditability
notes:
  - "Graph migrations are governed relationship/topology changes. They are not raw data storage, data backfill authority by themselves, schema-contract authority, policy authority, release authority, or publication approval."
  - "Every graph migration must have a corresponding rollback entry under migrations/rollback/, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/graph/` — Graph, Triplet, Relationship, and Topology Migrations

> **One-line purpose.** Hold governed graph and triplet migration plans that change relationships, identifiers, topology, projections, or graph-derived indexes while preserving evidence, provenance, validation, rollback, and release safety.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![lane](https://img.shields.io/badge/lane-graph_migrations-blueviolet)
![rollback](https://img.shields.io/badge/rollback-required-red)
![provenance](https://img.shields.io/badge/provenance-required-orange)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Graph migration contract](#graph-migration-contract) · [Required migration record](#required-migration-record) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/graph/` is the lane for graph and triplet migrations: relationship rewrites, graph topology changes, node/edge identity repairs, graph projection rebuilds, ontology alignment passes, relationship-type changes, evidence-link repairs, graph index rebuilds, and corrections to derived relationship structures.

This folder protects graph change discipline without weakening the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Graph migrations do not publish KFM data by themselves. They change graph/triplet structure or graph-derived state. Publication remains a governed release transition with evidence, policy, review state, release state, correction path, and rollback path.

Use this lane when the primary change is **relationship structure, triplet meaning, graph topology, graph projection, or graph-derived indexes**. Use another lane when the primary change is database structure, schema contracts, data backfills, or rollback documentation.

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-directory README |
| **Owning responsibility root** | `migrations/` |
| **Subpath role** | `graph/` — graph/triplet migration plans, topology changes, relationship repair, projection rebuilds, graph-index changes, validation notes |
| **Authority level** | Draft operational guidance. Directory Rules, accepted ADRs, graph contracts, schemas, policy, release gates, and runbooks outrank this README. |
| **Lifecycle phase** | n/a — graph migration scripts and plans, not lifecycle data itself |
| **Default posture** | Preserve evidence links; preserve deterministic identity where practical; dry-run where practical; rollback entry required; no secrets |
| **Owners** | `<graph-steward>`, `<migration-steward>`, `<data-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Graph steward + migration steward for all graph migrations; data/schema/release/policy stewards when data state, contract shape, public payloads, or sensitivity are affected |
| **Directory Rules basis** | `migrations/` includes `graph/` and requires every migration to have a corresponding entry under `migrations/rollback/`. |

[Back to top](#top)

---

## Repo fit

```text
Kansas-Frontier-Matrix/
└── migrations/
    ├── README.md
    ├── database/
    ├── schema/
    ├── data/
    ├── graph/         ◀── you are here
    │   └── README.md
    └── rollback/
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `migrations/graph/` | Graph/triplet migrations, relationship rewrites, topology repairs, projection rebuilds, graph-index migration notes | Data backfills, database DDL, schema-contract authority, release artifacts, rollback records themselves |
| `migrations/database/` | Database structure and storage-engine migrations | Graph meaning unless paired with graph migration |
| `migrations/schema/` | Contract/schema migration plans and compatibility notes | Graph state rewrites unless required by the schema change |
| `migrations/data/` | Data-state migrations, backfills, repairs, lifecycle movement plans | Relationship/topology migration as the primary concern |
| `migrations/rollback/` | Rollback entry for every migration | Primary migration scripts unless rollback-specific |
| `data/catalog/` | Catalog records and discovery metadata | Migration authority |
| `data/processed/` | Validated derived data outputs | Migration plans or scripts |
| `data/published/` | Released public artifacts | Graph migration scripts or rollback records |
| `schemas/contracts/v1/` | Machine-checkable schema shape | Graph migration execution |
| `contracts/` | Human-readable contract meaning | Graph migration scripts |
| `policy/` | Allow / deny / restrict / abstain rules | Graph migration code |
| `release/` | Release decisions, manifests, rollback cards, correction notices | Graph migration scripts |

[Back to top](#top)

---

## What belongs here

Use `migrations/graph/` for graph-specific migration material such as:

- Triplet rewrite plans and scripts.
- Relationship-type renames, splits, merges, or deprecations.
- Node/edge identity repair plans.
- Graph projection rebuild plans.
- EvidenceRef-to-EvidenceBundle linkage repairs for graph claims.
- Catalog-to-triplet alignment plans when the primary change is relationship structure.
- Ontology or vocabulary alignment migrations when they materially change graph edges or node classes.
- Graph index rebuild plans and validation notes.
- Corrections to relationship provenance, confidence, review state, or policy flags.
- Dry-run reports, diff summaries, and sanitized validation summaries.
- Migration manifests that describe affected nodes/edges/triplets, relationship classes, evidence impact, policy/sensitivity impact, validation, and rollback reference.
- Forward-fix notes when rollback is unsafe.

Accepted file types are Markdown plans, migration manifests, scripts, query fragments, sanitized graph diffs, validation summaries, and receipt-like run summaries. Keep each migration inspectable and paired with rollback documentation.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/graph/` as a graph dump, source-data store, schema home, policy home, or release lane.

The following must not live here:

- Full graph exports, graph database dumps, bulk triplet payloads, raw source data, cached extracts, tiles, rasters, or generated public artifacts.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads.
- Live database credentials, connection strings, graph database passwords, API keys, tokens, `.env` files, private endpoints, or production DSNs.
- JSON Schemas or canonical contracts that belong under `schemas/contracts/v1/` or `contracts/`.
- Policy bundles, release manifests, rollback cards, correction notices, or publication approvals.
- One-off destructive graph rewrite scripts without scope, evidence basis, dry-run, validation, rollback, owner, and review path.
- Unredacted sensitive graph relationships involving living persons, DNA/genomic material, precise restricted locations, archaeology/burial/sacred-site data, rare-species exact locations, infrastructure, or rights-uncertain material.
- Graph changes that silently convert weak, inferred, generated, or unreviewed relationships into authoritative public claims.

If a graph dump, credential, or sensitive relationship payload lands here, move it to the correct governed path or secure store and record the correction. If secrets or restricted relationships were exposed, treat it as a security/governance incident.

[Back to top](#top)

---

## Graph migration contract

Every graph migration should be a governed, reviewable, and auditable relationship-state transition.

### Required properties

- **Named scope.** Identify affected node classes, edge classes, triplet families, graph projections, indexes, or relationship stores.
- **Evidence basis.** Link the source evidence, EvidenceBundle, issue, validation failure, policy change, schema change, data migration, or release need that justifies the graph change.
- **Truth posture.** Do not upgrade generated, inferred, weak, or unreviewed relationships into authoritative claims without evidence and review.
- **Evidence closure.** Claims that depend on evidence should preserve or repair EvidenceRef-to-EvidenceBundle resolution.
- **Deterministic identity.** Preserve stable IDs where practical; record intentional ID remaps, merges, splits, and deprecations.
- **Provenance.** Record what changed, why, by whom/tool, when, and with what inputs.
- **Policy/sensitivity review.** Restricted relationships fail closed until rights, sensitivity, and publication posture are resolved.
- **Dry-run mode where practical.** Prefer graph diffs, affected-count reports, and sample relationship review before mutation.
- **Idempotence where practical.** Re-running should be safe, detected, or explicitly blocked.
- **Validation.** Define structural, evidence, policy, and sample-review checks before running.
- **Rollback or forward fix.** Every migration must link to `migrations/rollback/`.

### Naming convention

Use date-prefixed, descriptive names:

```text
YYYYMMDD-short-purpose.md
YYYYMMDD-short-purpose.py
YYYYMMDD-short-purpose.cypher
YYYYMMDD-short-purpose.sparql
YYYYMMDD-short-purpose.sql
```

Examples:

```text
20260703-repair-evidence-ref-edges.md
20260703-rebuild-county-layer-projection.py
20260703-rename-settlement-relationship-type.cypher
```

The rollback entry should share the same prefix and purpose:

```text
migrations/rollback/20260703-repair-evidence-ref-edges.md
```

[Back to top](#top)

---

## Required migration record

Every graph migration should have a Markdown record before it is run against shared, release-relevant, or public-impacting graph state.

```markdown
# <YYYYMMDD-short-purpose>

## Status
PROPOSED / APPROVED / RUNNING / COMPLETED / FAILED / ROLLED_BACK / FORWARD_FIXED

## Owner
<graph-steward or migration owner>

## Scope
<node classes, edge classes, triplet families, graph projection, index, store, or relationship class>

## Reason and evidence basis
<link to issue, EvidenceBundle, validation report, schema change, policy change, data migration, release need, or receipt reference>

## Truth posture
<confirmed/proposed/inferred/generated relationships affected; what must not be upgraded silently>

## Sensitivity and rights review
<public/internal/restricted/quarantine; living-person, DNA, archaeology, rare-species, infrastructure, or rights notes>

## Dependency order
<before/after schema, database, data, app, policy, or release changes>

## Migration plan
<steps, scripts, relationship rewrite rules, expected changes>

## Dry-run output
<affected counts, graph diff summary, sample review notes, no sensitive payloads>

## Validation plan
<structural checks, evidence-link checks, policy checks, sample review>

## Rollback reference
<migrations/rollback/YYYYMMDD-short-purpose.md>

## Run receipt
<timestamp, operator/tool, commit, command/workflow id, sanitized output summary>

## Post-run verification
<counts, graph invariants, orphan checks, evidence resolution checks, sample review>

## Follow-up
<docs, release notes, drift register, open questions>
```

[Back to top](#top)

---

## Validation

Graph migrations require evidence before and after execution.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Migration belongs in `migrations/graph/` | PR review |
| Rollback entry | Matching `migrations/rollback/` record exists | Path link |
| Scope | Affected nodes, edges, triplets, projections, or indexes are named | Migration record |
| Evidence basis | Migration has a documented reason | Evidence/ref/issue link |
| Truth posture | Inferred/generated/unreviewed relationships are not silently promoted | Reviewer signoff |
| Evidence closure | EvidenceRef links resolve or unresolved cases are quarantined/flagged | Resolution report |
| Identity integrity | Stable IDs are preserved or remapped intentionally | ID mapping / diff note |
| Sensitivity review | Restricted relationships fail closed or remain non-public | Policy/sensitivity note |
| Dry run | Migration can preview changes where practical | Graph diff / affected-count report |
| Secret scan | No credentials or private connection strings committed | Secret scan result |
| Structural invariants | No unexpected orphan nodes, duplicate edges, invalid relationship types, or broken projections | Validation report |
| Release impact | Public graph/API/map impacts are reviewed by release steward | Release note or N/A |

### Suggested command posture

Executable migrations should provide safe, environment-appropriate dry-run and run instructions. Do not embed production credentials, private endpoints, or destructive defaults in scripts or docs.

A graph migration is not ready for shared state until reviewers can answer:

1. What graph relationships change?
2. Why do they change?
3. What evidence supports the change?
4. What truth posture is preserved?
5. What sensitivity or rights risks exist?
6. What validates the graph after the change?
7. How is it rolled back or forward-fixed?
8. How is execution audited?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no migration behavior | Docs steward or migration steward |
| Additive low-risk graph/index rebuild | Graph steward + migration steward |
| Relationship rename, split, merge, or deprecation | Graph steward + schema/contract steward + migration steward |
| EvidenceRef or EvidenceBundle linkage repair | Graph steward + evidence/catalog steward + migration steward |
| Node/edge identity remap, merge, or split | Graph steward + data steward + migration steward |
| Migration paired with data backfill/repair | Graph steward + data steward + migration steward |
| Migration paired with database structure change | Graph steward + database steward + migration steward |
| Migration affecting public API, map layers, released artifacts, or publication state | Release steward + graph steward + migration steward |
| Migration involving living-person, DNA/genomic, archaeology, rare-species, infrastructure, or rights-uncertain relationships | Policy/sensitivity reviewer + relevant domain steward + release steward if public impact exists |
| Destructive graph rewrite | Graph steward + migration steward + rollback reviewer |
| Forward-fix-only migration | Migration steward + graph steward + documented risk acceptance |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/`, `migrations/graph/`, and `migrations/rollback/`.
- [ ] Confirm graph/triplet storage technology and query language(s).
- [ ] Confirm graph migration runner/tooling: Python, SQL, Cypher, SPARQL, custom workflow, or mixed.
- [ ] Confirm filename and ordering convention.
- [ ] Confirm graph validation tooling under `tests/` or `tools/validators/`.
- [ ] Confirm required graph invariants: orphan policy, duplicate edge policy, relationship-type registry, identity rules, and projection rules.
- [ ] Confirm EvidenceRef-to-EvidenceBundle resolution validation.
- [ ] Confirm sensitivity-review workflow for policy-significant graph migrations.
- [ ] Confirm how graph migration receipts are recorded and indexed.
- [ ] Confirm rollback record template under `migrations/rollback/`.
- [ ] Confirm release-steward review trigger for public-impacting graph migrations.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First concrete graph migration, triplet rewrite, relationship-type change, identity remap, projection rebuild, evidence-link repair, public-impacting graph change, or rollback-linked migration PR |
