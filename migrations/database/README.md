<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-database-readme
title: migrations/database/ — Governed Database Structure, Permissions, and Storage-Behavior Changes
type: README; per-directory-readme; nested-migration-lane; database-change-control
version: v1.1
status: draft; repository-grounded; documented-lane; executable-payloads-unestablished; engine-unestablished; runner-unestablished; rollback-pairing-unverified; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable database, migration, schema, data, security, application, and release stewardship assignments were not established
created: 2026-07-03
updated: 2026-07-24
supersedes: v1 documentation at the same path; no migration payload, database object, database state, runtime behavior, release state, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; migrations; database-change; least-privilege; rollback-aware; evidence-first; fail-closed; non-publisher
current_path: migrations/database/README.md
owning_root: migrations/
responsibility: govern database DDL, indexes, constraints, views, functions, triggers, extensions, roles, grants, partitions, and storage-behavior changes without becoming semantic-contract, machine-schema, lifecycle-data, policy, release, or publication authority
truth_posture: >
  CONFIRMED same-path target; canonical migrations responsibility root; documented database and rollback lanes; Directory Rules
  assignment of database migrations to migrations/database/; mandatory paired recovery posture; current CODEOWNERS routing;
  and the parent migrations README's bounded conclusion that executable migration payloads and a selected database runner
  were not established / PROPOSED database-migration classification, packet fields, database invariant matrix, preflight,
  dry-run, lock/downtime, compatibility, execution, recovery, and definition-of-done contracts / UNKNOWN active database
  engine and version, concrete payload inventory, target environments, live database objects, extensions, roles, backups,
  execution receipts, applied migration history, production outcomes, and performance baselines / NEEDS VERIFICATION recursive
  lane inventory, one-to-one rollback pairing, stable ID convention, dedicated migration CI, steward assignments, least-privilege
  review workflow, maintenance-window policy, and release integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 3ad838a87e806c0f8f74fe69b0116fca0b83f475
  parent_readme_blob: 48da6b62000d145359bfbd7f8383961c9f285b2a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  codeowners_status: repository default routing resolves this path to @bartytime4life; role-level stewardship and independent approval remain unverified
  inspection_method: exact GitHub file reads, parent-lane evidence review, bounded repository search, and open-PR overlap search; no recursive Git tree, database engine, migration runner, database connection, backup system, CI execution, release artifact, or runtime environment was inspected
related:
  - ../README.md
  - ../schema/README.md
  - ../data/README.md
  - ../graph/README.md
  - ../rollback/README.md
  - ../../contracts/README.md
  - ../../schemas/README.md
  - ../../data/README.md
  - ../../policy/README.md
  - ../../tests/README.md
  - ../../tools/validators/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/runbooks/README.md
  - ../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../../.github/CODEOWNERS
notes:
  - "v1.1 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "The lane is documented, but a concrete database engine, migration payloads, canonical runner, applied-version ledger, and verified recovery coverage were not established."
  - "Static badges summarize inspected repository state only; they are not execution, review, recovery, release, or publication proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/database/` — Governed Database Structure, Permissions, and Storage-Behavior Changes

> **One-line purpose.** Govern deliberate changes to database-managed structure and behavior while preserving KFM meaning and shape boundaries, data integrity, lifecycle isolation, least privilege, compatibility, validation, and recoverability.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: database migration](https://img.shields.io/badge/lane-database%20migration-1f6feb?style=flat-square)](#authority-level)
[![Engine: not established](https://img.shields.io/badge/engine-not%20established-b42318?style=flat-square)](#status)
[![Runner: not established](https://img.shields.io/badge/runner-not%20established-b42318?style=flat-square)](#validation)
[![Recovery pairing: needs verification](https://img.shields.io/badge/recovery%20pairing-needs%20verification-d4a72c?style=flat-square)](#recovery-and-forward-fix)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** `migrations/database/` is a documented migration lane beneath the canonical `migrations/` responsibility root. Current bounded evidence establishes its README and recovery relationship, but does **not** establish an active database engine, concrete migration payloads, a selected runner, an applied-version ledger, complete rollback pairing, backup/restore capability, execution history, or production outcomes.

> [!CAUTION]
> A migration plan, SQL parse, schema diff, `EXPLAIN` output, branch, pull request, or green unrelated workflow does not prove that a database change is safe. An execution claim requires a named engine and version, exact target environment, pinned payload, preflight evidence, observed run evidence, post-migration checks, and recovery evidence.

> [!WARNING]
> This directory is not a database, dump store, backup system, secret store, or schema authority. Database dumps, WAL archives, snapshots, DSNs, credentials, restricted rows, and lifecycle payloads must never be committed here.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Classification](#database-migration-classification) · [Packet](#minimum-database-migration-packet) · [Invariants](#database-specific-invariants) · [Execution](#preflight-dry-run-and-execution-contract) · [Recovery](#recovery-and-forward-fix) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

## Purpose

`migrations/database/` owns the **mechanics and review packet** for governed changes to database-managed structure, access, and behavior.

Typical database migrations include:

- creating or altering tables, columns, indexes, constraints, sequences, or database-owned enums;
- creating or changing views and materialized views;
- adding, replacing, or retiring functions, procedures, triggers, or generated expressions;
- enabling, upgrading, configuring, or removing approved database extensions;
- changing database roles, grants, ownership, row-level access controls, or other engine-managed permissions;
- changing partitions, tablespaces, retention structures, storage parameters, or database-managed maintenance behavior;
- preparing compatible structure for a schema, data, graph, application, or release transition;
- removing deprecated database structure after producer and consumer adoption is proven.

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A database migration may support a governed transition. It does not itself define object meaning, make a machine schema canonical, approve data promotion, authorize public access, approve release, or publish KFM content.

Choose this lane by **primary responsibility**, not by language or file extension. SQL that primarily backfills records belongs in `migrations/data/`; a JSON or DTO compatibility transition belongs in `migrations/schema/`; graph topology belongs in `migrations/graph/`; recovery records belong in `migrations/rollback/`.

## Authority level

<a id="status--authority"></a>

**Nested operational lane for database-structure and database-managed behavior changes; subordinate to the authorities that define meaning, machine shape, admissibility, evidence, lifecycle state, application behavior, and release.**

| Question | Controlling authority |
|---|---|
| Where this migration material belongs | Directory Rules, accepted placement ADRs, then [`migrations/README.md`](../README.md) and this README |
| What an object, field, or relation means | [`contracts/`](../../contracts/README.md) |
| What machine payload shape is valid | [`schemas/`](../../schemas/README.md) |
| What data phase owns persisted records | [`data/`](../../data/README.md) |
| What rights, sensitivity, access, or handling is permitted | [`policy/`](../../policy/README.md) and applicable review records |
| How database change mechanics are planned | `migrations/database/` |
| How schema, data, or graph adoption is coordinated | Sibling migration lanes plus the affected producers and consumers |
| How engineering recovery is recorded | [`migrations/rollback/`](../rollback/README.md) plus verified backup/restore evidence where applicable |
| Whether a release or public correction is approved | [`release/`](../../release/README.md) and applicable promotion/review records |
| How execution occurs | The selected engine, runner, named target environment, payload, transaction/lock controls, and runbook |
| Who receives GitHub review routing | [`.github/CODEOWNERS`](../../.github/CODEOWNERS); current routing resolves to `@bartytime4life` |
| Who is accountable as database, migration, schema, data, security, application, or release steward | **NEEDS VERIFICATION** through approved responsibility assignments and review records |

This lane may carry plans, SQL or engine-native payloads, dependency matrices, validation summaries, and sanitized execution summaries. It must not redefine a stronger authority or treat a proposed engine, extension, runner, or access model as adopted.

## Status

| Surface | Current evidence | Status |
|---|---|---|
| This README | Present and updated in place | **CONFIRMED — documentation** |
| Parent migration root | `migrations/README.md` present and repository-grounded | **CONFIRMED — documentation** |
| Recovery lane README | `migrations/rollback/README.md` present | **CONFIRMED — documentation** |
| Concrete database-migration payloads | Not established by bounded parent inspection and repository search | **UNKNOWN / NEEDS VERIFICATION** |
| Active database engine and version | Not established; architecture documents mentioning PostgreSQL/PostGIS are not runtime proof | **UNKNOWN** |
| Canonical database-migration runner | Not established | **UNKNOWN** |
| Dedicated database-migration workflow or CI gate | Not established | **NEEDS VERIFICATION** |
| Applied migration/version ledger | Not established | **NEEDS VERIFICATION** |
| Stable migration ID and ordering convention | Date-prefixed examples exist; standardized contract not established | **PROPOSED / NEEDS VERIFICATION** |
| One-to-one recovery pairing | Required by Directory Rules; coverage not recursively verified | **NEEDS VERIFICATION** |
| Target databases, schemas, extensions, roles, and environments | Not inspected | **UNKNOWN** |
| Backup, snapshot, restore, replication, or failover capability | Not inspected | **UNKNOWN** |
| Lock, downtime, maintenance-window, and online-DDL policy | Not established | **NEEDS VERIFICATION** |
| Execution receipts, applied history, and production outcomes | Not inspected | **UNKNOWN** |
| GitHub ownership routing | Repository default routes to `@bartytime4life` | **CONFIRMED routing; stewardship unverified** |
| Release or publication authority | Not owned by this lane | **DENIED by boundary** |

Treat examples and templates below as **proposed documentation contracts**, not as evidence that an engine, extension, runner, schema, workflow, database, or migration history exists.

## What belongs here

Use `migrations/database/` when database-managed structure or behavior is the primary responsibility.

Accepted material includes:

- DDL or engine-native migration plans and payloads;
- table, column, sequence, constraint, index, view, and materialized-view changes;
- database-owned enum, generated-column, function, procedure, or trigger changes;
- approved extension installation, upgrade, configuration, or removal plans;
- role, grant, ownership, row-level access, and least-privilege changes;
- partitioning, tablespace, storage-parameter, retention-structure, and maintenance-behavior changes;
- compatibility structure supporting schema, data, graph, application, or release transitions;
- object inventories, dependency graphs, lock/downtime assessments, and maintenance-window plans;
- preflight, dry-run, canary, transaction, validation, and post-check definitions;
- migration manifests binding engine/version, target, payload digest, objects, dependencies, compatibility, validation, and recovery;
- sanitized query plans, object diffs, timing summaries, and validation reports that expose no sensitive data or infrastructure detail;
- deprecation, adoption, cutover, and cleanup notes;
- documented forward-fix plans when direct reversal would be less safe.

Suitable formats may include Markdown, SQL, or a repository-supported engine-native format. Shell or Python wrappers belong here only when they are narrowly scoped to the migration, avoid embedded secrets, and delegate to a verified runner rather than becoming an undocumented parallel framework.

## What does not belong here

Do not use `migrations/database/` as a live database, dump store, backup system, secret store, schema authority, data lake, policy root, or release lane.

The following do not belong here:

- full or partial database dumps, exported tables, backups, snapshots, WAL archives, restore images, replication slots, or binary storage files;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads;
- source downloads, caches, tiles, PMTiles, COGs, GeoParquet, rasters, or generated public artifacts;
- canonical JSON Schemas, DTO definitions, or semantic contracts;
- policy bundles, policy decisions, release manifests, promotion decisions, release rollback cards, correction notices, or publication approvals;
- live DSNs, connection strings, usernames, passwords, tokens, certificates, private endpoints, host inventories, kubeconfigs, or `.env` files;
- unredacted query results, row samples, `EXPLAIN ANALYZE` output, logs, or error traces containing restricted data or infrastructure details;
- primary data-backfill, schema-compatibility, graph-topology, or recovery records owned by sibling lanes;
- one-off destructive SQL lacking stable scope, engine/version, target environment, preconditions, lock/downtime analysis, backup/recovery posture, validation, review, and audit fields;
- database changes that silently expose canonical, RAW, WORK, QUARANTINE, unpublished, steward-only, or restricted stores to public services;
- AI-generated DDL, indexes, grants, or performance claims promoted without engine evidence, review, and target-specific validation.

A sanitized summary or pointer may live here; the authoritative database state, backup, receipt, release record, or restricted output remains in its controlling system or root.

If a dump, credential, private host detail, or restricted row lands here, stop normal work, isolate the material, rotate or revoke access where appropriate, and follow the applicable incident, correction, and governance process.

## Inputs

A database-migration packet may consume:

| Input | Why it is needed |
|---|---|
| Accepted ADR or explicit scoped decision | Establishes why the structural or behavioral transition is allowed |
| Issue, defect, validation failure, performance evidence, incident correction, or release need | Establishes reason and bounded scope |
| Semantic contract | Defines intended meaning |
| Machine schema and version | Defines intended payload shape |
| Engine, edition, extension set, and version | Defines supported syntax, features, limits, and recovery behavior |
| Named database, logical schema, and target environment | Defines exactly where the change applies |
| Current object inventory and metadata digest | Pins tables, columns, indexes, constraints, views, functions, roles, grants, and extensions |
| Producer and consumer inventory | Defines compatibility and adoption order |
| Workload, query, and performance evidence | Grounds index, view, partition, and storage changes without guesswork |
| Policy, security, and sensitivity review | Constrains roles, access, logging, samples, and public exposure |
| Data, graph, and lifecycle impact inventory | Defines whether backfills, rebuilds, referential checks, or release coordination are required |
| Lock, transaction, timeout, downtime, and maintenance-window requirements | Defines operational risk and execution controls |
| Backup, snapshot, restore, replication, or failover capability | Defines feasible recovery |
| Valid and invalid fixtures or representative test database | Defines success and failure states |
| Environment and runner contract | Defines how execution is performed safely and repeatably |

Material inputs should be identified by commit, schema version, engine version, object digest, release ID, migration ledger state, or named environment. Terms such as “latest,” “the database,” “all tables,” or “production” are not sufficiently precise for consequential migrations.

## Outputs

A database-migration packet may produce:

- reviewed migration plans;
- SQL or engine-native payloads and content digests;
- before/after object inventories and metadata digests;
- dependency, compatibility, and adoption matrices;
- lock, downtime, timeout, transaction, maintenance-window, and online-change assessments;
- preflight, dry-run, parser, planner, canary, and validation reports;
- sanitized query-plan or performance summaries;
- least-privilege, role, grant, ownership, and access-review summaries;
- sanitized execution summaries and pointers to authoritative receipts;
- post-migration object, constraint, permission, integrity, and compatibility reports;
- paired recovery or forward-fix records;
- documentation, deprecation, drift, incident, correction, and release-impact updates.

These outputs remain bounded:

| Output | What it can prove | What it does not prove |
|---|---|---|
| Migration plan | Intended change and review surface exist | Execution occurred |
| Parsed SQL or engine-native payload | Syntax may be accepted by a named parser or engine | Target safety, lock behavior, compatibility, or successful application |
| Object diff | Intended structural delta is explicit | Live target matches the assumed base state |
| Dry run or transaction preview | A preview completed in a named context | Production outcome or zero downtime |
| Query plan | A planner produced a plan for named inputs/statistics | Real workload benefit, stable latency, or absence of regressions |
| Execution receipt | A named action was attempted or completed | Semantic correctness, release approval, or publication |
| Post-check report | Named invariants passed in a named target | Universal correctness or absence of hidden operational impact |
| Recovery record | Recovery instructions exist | Recovery was rehearsed or will work |
| Git commit or pull request | Repository bytes changed | Database state changed, recovery succeeded, or a release was approved |

This lane never publishes KFM data or approves public database access by itself.

## Validation

Validation is engine-, object-, and consequence-specific. A single generic green check is insufficient.

### Required source checks

Every database-migration change should verify:

- target path and lane;
- stable migration identity and ordering;
- exact engine, edition, version, extensions, database, logical schema, environment, and base state;
- migration and recovery-record pairing;
- affected object and dependency inventory;
- controlling contracts, schemas, policies, and ADRs;
- producer, consumer, data, graph, application, API, and release adoption order;
- payload digest and dependency pins;
- transaction, lock, timeout, downtime, and maintenance-window posture;
- least-privilege and secret/restricted-content absence;
- backup, restore, disablement, or forward-fix capability;
- preflight, dry-run, canary, and post-check definitions;
- documentation, deprecation, incident, correction, and release impact.

### Database-specific executable evidence

| Concern | Minimum evidence |
|---|---|
| Engine compatibility | Parse or plan against the named engine/version and required extensions |
| Base-state match | Object inventory and metadata digest match the packet before mutation |
| Transaction behavior | Explicit transactional boundary, autocommit exceptions, retry, and partial-failure behavior |
| Lock and downtime | Expected lock class, duration, blocked operations, timeout behavior, and mitigation |
| Tables and columns | Before/after types, nullability, defaults, generated values, ownership, and storage checks |
| Constraints | Existing-data precheck, validation state, violation handling, and final enforcement proof |
| Indexes | Definition, validity, build mode, size, maintenance cost, and workload-grounded query evidence |
| Views and materialized views | Dependency closure, column compatibility, refresh strategy, privileges, and consumer checks |
| Functions, procedures, and triggers | Language/version, volatility or determinism, security context, side effects, recursion, and test evidence |
| Roles, grants, ownership, or row-level access | Least privilege, deny-path tests, privilege diff, ownership, and escalation review |
| Extensions | Approval, version pin, upgrade path, dependency, privilege, and recovery evidence |
| Partitioning or storage behavior | Routing, bounds, default partition, retention, pruning, maintenance, and rollback checks |
| Spatial behavior when applicable | Extension/version, geometry/geography types, SRID/CRS, index operator class, validity, bounds, and transform checks |
| Temporal behavior when applicable | Valid/source/observed/retrieval/release-time constraints and index/partition semantics remain explicit |
| Data integrity | Row counts, foreign keys, uniqueness, evidence links, lifecycle isolation, and representative application checks |
| Recovery | Backup/restore or compensating path, recovery preconditions, post-recovery checks, and rehearsal evidence or `NOT RUN` |
| Public impact | Governed API, map, tile, export, cache, correction, and release effects reviewed separately |

### Current repository boundary

No repository-native database-migration command, active engine, selected runner, dedicated workflow, applied-version ledger, or verified database fixture suite was established in the bounded inspection. Architecture references to PostgreSQL or PostGIS remain planning/doctrine evidence, not proof of a live engine.

Until these surfaces exist and are verified:

- do not advertise a canonical database engine or run command;
- do not invent extension, role, lock, backup, replication, or maintenance-window support;
- record migration-specific commands and engine assumptions in the packet;
- mark unexecuted checks `NOT RUN`;
- treat generic SQL lint, schema, contract, policy, or release checks as supporting context, not database-migration proof;
- keep shared or release-relevant execution blocked until the named target, runner, preflight, review, and recovery evidence exist.

## Review burden

Review scales with consequence, not file extension.

**Confirmed routing:** the repository's default CODEOWNERS pattern routes this path to `@bartytime4life`. That route is not proof of steward assignment, independent review, security approval, execution authorization, release approval, or completed review.

| Change class | Required review concerns; accountable assignments remain NEEDS VERIFICATION |
|---|---|
| README-only wording with no behavior change | Documentation accuracy, database-boundary accuracy, link and render review |
| Additive table, column, sequence, or non-unique index | Database compatibility, lock/downtime, application adoption, recovery |
| Constraint, uniqueness, type, default, or nullability change | Existing-data validation, producer/consumer compatibility, failure behavior |
| View, materialized view, function, procedure, trigger, or generated expression | Semantic behavior, dependencies, security context, side effects, test coverage |
| Role, grant, ownership, row-level access, or permission change | Least privilege, deny paths, escalation risk, security and application impact |
| Extension install, upgrade, configuration, or removal | Engine compatibility, supply/dependency posture, privileges, recovery, operations |
| Partitioning, tablespace, storage parameter, retention, or maintenance behavior | Capacity, routing, pruning, downtime, operations, recovery |
| Destructive, table-rewrite, irreversible, or forward-fix-only change | Explicit risk acceptance, backup/recovery evidence, independent recovery review where practical |
| Schema-, data-, or graph-paired migration | Cross-lane ordering, compatibility, adoption, integrity, and rollback coordination |
| Public API, map, tile, export, cache, or release impact | Trust membrane, release review, correction/withdrawal, rollback target, public communication |
| Credentials, access, or incident recovery | Security review and affected-system ownership |
| Cross-database, replicated, sharded, or multi-environment migration | Review for every target, dependency, cutover, and recovery domain |

For high-impact migrations, authoring, approval, execution, and verification should be separated when repository maturity supports it.

## Related folders

| Location | Relationship |
|---|---|
| [`migrations/`](../README.md) | Canonical migration root, shared packet, state, compatibility, and recovery guidance |
| [`migrations/schema/`](../schema/README.md) | Machine-shape and semantic compatibility transitions |
| [`migrations/data/`](../data/README.md) | Data backfills, repairs, remaps, relocations, and rebuilds |
| [`migrations/graph/`](../graph/README.md) | Graph/triplet topology, identity, and evidence-link changes |
| [`migrations/rollback/`](../rollback/README.md) | Paired engineering recovery, disablement, restore, or forward-fix records |
| [`contracts/`](../../contracts/README.md) | Semantic meaning |
| [`schemas/`](../../schemas/README.md) | Machine shape |
| [`data/`](../../data/README.md) | Lifecycle payloads and authoritative data-state ownership |
| [`policy/`](../../policy/README.md) | Admissibility, rights, sensitivity, access, and obligations |
| [`tests/`](../../tests/README.md) | Representative enforceability and regression evidence |
| [`tools/validators/`](../../tools/validators/README.md) | Repository-wide validator implementations |
| [`release/`](../../release/README.md) | Release decisions, correction, withdrawal, and public rollback |
| [`docs/runbooks/`](../../docs/runbooks/README.md) | Operator procedures, maintenance, backup, restore, and recovery drills |
| [`SEPARATION_OF_DUTIES.md`](../../docs/governance/SEPARATION_OF_DUTIES.md) | Review and duty-separation guidance |
| [`directory-rules.md`](../../docs/doctrine/directory-rules.md) | Canonical placement doctrine |
| [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review routing; not governance approval |

## ADRs

A database migration does not always require an ADR. An ADR is required when the migration:

- adds, removes, or renames a canonical root;
- creates a parallel schema, contract, policy, source, registry, receipt, proof, release, lifecycle, database, or migration authority;
- changes the canonical schema-home, database responsibility split, or trust-membrane boundary;
- selects or replaces a project-wide database engine, migration runner, applied-version ledger, or cross-repository migration-state contract;
- introduces or removes a project-wide extension, partitioning strategy, role model, access-control model, or storage architecture with durable tradeoffs;
- splits, merges, redefines, or bypasses a lifecycle phase;
- materially changes a public contract, canonical identity, data retention, or evidence-link behavior;
- introduces a non-reversible architectural decision whose tradeoffs must persist;
- intentionally bends a KFM invariant.

A migration packet may implement an accepted decision. It cannot make its own proposed ADR accepted.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v1.1 documentation update |
| Current maturity | Documented database lane; engine, payloads, runner, workflow, applied ledger, target environments, backups, execution history, and recovery coverage unverified |
| Next review trigger | First concrete database-migration payload, selected engine or runner, dedicated workflow, applied ledger, recovery rehearsal, destructive migration, permission/extension change, or public-impacting database migration |

---

<a id="repo-fit"></a>

## Current bounded topology

The confirmed documentation topology relevant to this lane is:

```text
migrations/
├── README.md
├── database/
│   └── README.md      ◀── you are here
├── schema/
│   └── README.md
├── data/
│   └── README.md
├── graph/
│   └── README.md
└── rollback/
    └── README.md
```

This is a bounded named-path inventory, not a recursive tree attestation. Current evidence does not establish executable payloads below this lane or a connected database environment.

## Database-migration classification

Classify the intended state transition before designing the payload.

| Class | Primary purpose | Typical evidence burden |
|---|---|---|
| `EXPAND_STRUCTURE` | Add compatible tables, columns, sequences, indexes, views, or nullable/defaulted structure | Engine parse, lock analysis, backward compatibility, recovery |
| `TIGHTEN_STRUCTURE` | Add or validate constraints, uniqueness, requiredness, types, or stricter defaults | Existing-data precheck, staged validation, producer/consumer adoption |
| `BEHAVIOR_CHANGE` | Change functions, procedures, triggers, generated expressions, or database-owned behavior | Semantic review, side-effect and security tests, dependency closure |
| `ACCESS_CHANGE` | Change roles, grants, ownership, row-level access, or database permissions | Least privilege, deny tests, escalation and service-impact review |
| `EXTENSION_CHANGE` | Install, upgrade, configure, or remove an engine extension | Engine/version/dependency pinning, privilege, compatibility, recovery |
| `PERFORMANCE_STRUCTURE` | Add or change indexes, materialized views, partitions, storage parameters, or maintenance structures | Workload evidence, build/refresh risk, capacity, regression checks |
| `DEPRECATE_OR_REMOVE` | Remove obsolete objects after adoption | Usage evidence, deprecation window, dependency closure, recovery |
| `DESTRUCTIVE_OR_REWRITE` | Drop, rewrite, re-encode, repartition, or irreversibly alter structure | Backup/recovery evidence, downtime, data-integrity checks, explicit risk acceptance |
| `COORDINATED` | Multiple equally primary database, schema, data, graph, app, or release transitions | Linked lane packets, explicit ordering, umbrella coordination record |

Do not classify a migration by whether the payload is SQL, shell, Python, or engine-native metadata. Classify it by the **primary database-managed state change**.

<a id="database-migration-contract"></a>
<a id="required-migration-record"></a>

## Minimum database-migration packet

A shared-state or release-relevant database migration should have a complete packet before execution.

```yaml
migration_id: dbmig-<stable-id>
title: <short purpose>
status: PROPOSED
class: EXPAND_STRUCTURE | TIGHTEN_STRUCTURE | BEHAVIOR_CHANGE | ACCESS_CHANGE | EXTENSION_CHANGE | PERFORMANCE_STRUCTURE | DEPRECATE_OR_REMOVE | DESTRUCTIVE_OR_REWRITE | COORDINATED
owner: NEEDS VERIFICATION
authority_refs: []
reason_refs: []
engine:
  name: NEEDS VERIFICATION
  edition: NEEDS VERIFICATION
  version: NEEDS VERIFICATION
  extensions: []
target:
  environment: <named-environment>
  database: <database-identity>
  logical_schema: <schema-or-namespace>
base_state:
  revision: <commit-or-release>
  applied_ledger_ref: NEEDS VERIFICATION
  object_inventory_ref: <path-or-id>
  metadata_digest: <sha256>
target_state:
  description: <intended structure-or-behavior>
  object_inventory_ref: <expected-inventory>
payloads:
  - path: <migration-payload>
    sha256: <digest>
objects:
  tables: []
  columns: []
  indexes: []
  constraints: []
  sequences: []
  views: []
  materialized_views: []
  functions: []
  procedures: []
  triggers: []
  extensions: []
  roles: []
  grants: []
dependencies:
  database_migrations: []
  schema_migrations: []
  data_migrations: []
  graph_migrations: []
  applications: []
  releases: []
compatibility:
  class: backward-compatible | expand-and-contract | staged-breaking | destructive | forward-fix-only
  producer_consumer_order: []
execution_controls:
  transaction_mode: NEEDS VERIFICATION
  lock_timeout: NEEDS VERIFICATION
  statement_timeout: NEEDS VERIFICATION
  downtime_class: NEEDS VERIFICATION
  maintenance_window: null
  batching_or_online_mode: NEEDS VERIFICATION
preconditions: []
preflight:
  command_or_workflow: NEEDS VERIFICATION
  evidence_ref: null
validation:
  pre_checks: []
  post_checks: []
security:
  least_privilege_review: NEEDS VERIFICATION
  secret_scan_ref: null
backup_and_recovery:
  recovery_class: REVERSIBLE | DISABLEABLE | RESTORABLE | COMPENSATING | FORWARD_FIX_ONLY | NON_RECOVERABLE
  backup_or_snapshot_ref: null
  recovery_ref: migrations/rollback/<paired-id>.md
release_impact: none | internal | candidate | public
execution:
  runner: NEEDS VERIFICATION
  receipt_ref: null
review:
  required_concerns: []
  records: []
```

This is a **PROPOSED documentation contract**, not a verified repository schema. Standardizing it as machine shape requires placement under `schemas/` with representative valid and invalid fixtures and applicable policy/tests.

## Database-specific invariants

| Invariant | Requirement |
|---|---|
| Authority separation | Database structure implements meaning and shape defined elsewhere; it does not silently redefine them |
| Engine pinning | Name engine, edition, version, extensions, and target environment; never rely on an unbounded “SQL database” assumption |
| Base-state pinning | Verify object inventory and metadata digest before applying the payload |
| Transaction clarity | State transaction boundaries, autocommit exceptions, partial-failure behavior, and retry posture |
| Lock and downtime control | Bound expected locks, blocked operations, timeouts, maintenance window, and abort conditions |
| Data integrity | Preserve constraints, identity, evidence links, lifecycle isolation, and authoritative records |
| Compatibility | Sequence database, schema, data, graph, app, and release adoption through an explicit compatibility class |
| Least privilege | Roles, grants, ownership, row-level access, functions, and extension privileges are minimal and reviewed |
| Lifecycle and trust membrane | Database changes must not create direct public paths to canonical, RAW, WORK, QUARANTINE, or unpublished state |
| Constraint safety | Validate existing data before enforcement; avoid claiming safety from syntax alone |
| Performance evidence | Index, materialized-view, partition, and storage changes require workload-grounded evidence and regression checks |
| Behavior visibility | Functions, triggers, generated expressions, and procedures expose side effects, security context, and dependencies |
| Spatial humility | PostGIS or other spatial behavior is conditional on verified engine/extension support; SRID, CRS, validity, index, and transform semantics remain explicit |
| Temporal clarity | Valid/source/observed/retrieval/release-time behavior remains distinct where material |
| Recovery | Link a paired recovery record and verified backup/restore or compensating posture where applicable |
| Auditability | Record target, payload digest, runner, operator/tool, timing, outcome, and post-check evidence |
| Non-publication | Migration completion is not release approval, public correction approval, or KFM publication |

A migration that cannot preserve an invariant must state the tradeoff, risk, decision authority, and compensating control.

## Preflight, dry-run, and execution contract

### Preflight

Before mutation, establish:

1. exact engine, edition, version, extension set, database, logical schema, environment, and base revision;
2. payload digest, runner version, and dependency versions;
3. current object inventory, metadata digest, applied-ledger state, and dependency graph;
4. current row counts, constraint state, privileges, query/workload evidence, and relevant application compatibility;
5. transaction, lock, timeout, downtime, online-change, and maintenance-window posture;
6. backup, snapshot, restore, disablement, or compensating path;
7. target authorization, freeze/cutover requirements, and review records.

### Dry run or rehearsal

A dry run or rehearsal should:

- parse and plan against the named engine/version or an appropriately representative disposable target;
- verify base-state identity before accepting results;
- run in read-only, transactionally reversible, shadow, clone, or isolated-fixture mode where supported;
- report object diffs, dependency changes, expected locks, rewrite/build work, warnings, and downstream impact;
- avoid restricted rows, secrets, private hostnames, production DSNs, and unsafe logs;
- identify unsupported syntax, stale base state, unvalidated constraints, privilege escalation, long-running operations, and unresolved recovery gaps;
- produce a named evidence artifact or sanitized summary;
- fail closed when engine, target, base state, compatibility, security, or recovery posture is unresolved.

### Execution

Execution should:

- target one named database and environment;
- use the pinned payload, runner, engine/version, transaction mode, and timeouts;
- verify base state immediately before mutation;
- apply dependency order explicitly;
- support online/staged execution, bounded batches, checkpoints, or explicit non-resumability where material;
- record start/end time, runner, operator/tool identity, revision, payload digest, target, outcome, warnings, and failures;
- stop on unexpected object state, lock risk, invariant failure, policy/security failure, or incompatible consumer state unless an approved exception explicitly governs continuation;
- never hide destructive behavior behind a generic command or unsafe default;
- keep authoritative receipts in the governed receipt home and reference them from the migration packet.

### Post-migration verification

Verify:

- object inventory and metadata digest;
- table, column, sequence, index, constraint, view, function, trigger, extension, role, grant, ownership, and partition state as applicable;
- constraints, foreign keys, uniqueness, row counts, identity, evidence links, and lifecycle isolation;
- application, schema, data, graph, API, and release compatibility;
- query and workload regressions against named evidence where performance was a reason;
- least privilege, deny paths, ownership, and public-route isolation;
- spatial and temporal semantics where applicable;
- backup/recovery readiness and paired record status;
- documentation, deprecation, incident, correction, cache, and release follow-up.

<a id="recovery-and-forward-fix"></a>

## Recovery and forward fix

Every consequential database migration must link to a paired record under [`migrations/rollback/`](../rollback/README.md), even when direct reversal is unsafe.

Use one recovery class:

| Recovery class | Meaning |
|---|---|
| `REVERSIBLE` | A tested down migration or inverse operation can restore the prior approved structure/state |
| `DISABLEABLE` | New behavior, trigger, view, function, permission, or route can be disabled while state remains |
| `RESTORABLE` | Backup, snapshot, replica, or point-in-time restoration is the recovery path |
| `COMPENSATING` | A governed corrective migration restores safety |
| `FORWARD_FIX_ONLY` | Reversal is less safe; an explicit compensating path is the approved option |
| `NON_RECOVERABLE` | Not acceptable for shared or release-relevant state absent exceptional documented governance |

The recovery record should identify:

- paired migration ID and payload digest;
- engine/version, target database, environment, and base state;
- recovery class, activation conditions, and irreversible effects;
- transaction, lock, downtime, and maintenance-window requirements;
- backup, snapshot, replica, restore, disablement, or compensating references;
- application, data, graph, API, map, tile, cache, and release impact;
- pre- and post-recovery checks;
- rehearsal evidence or `NOT RUN`;
- correction, withdrawal, incident, or release references where applicable.

A rollback file existing in Git is not proof that recovery works. A down migration is not automatically safe, and database recovery does not replace release rollback cards, correction notices, withdrawals, backups, restore procedures, or incident records.

## Definition of done

A database migration is complete only when every applicable item is closed:

- [ ] Stable migration identity and ordering are recorded.
- [ ] The primary lane and Directory Rules basis are correct.
- [ ] Controlling semantic contracts, machine schemas, policies, ADRs, and release dependencies are referenced.
- [ ] Engine, edition, version, extensions, target database, logical schema, environment, and base state are pinned.
- [ ] Payloads, runner, dependencies, and content digests are recorded.
- [ ] Affected objects and producer/consumer dependencies are inventoried.
- [ ] Compatibility, rollout, deprecation, and cutover order are explicit.
- [ ] Transaction, lock, timeout, downtime, online-change, and maintenance-window posture are explicit.
- [ ] Least-privilege, ownership, access, secret, and public-route isolation concerns are reviewed.
- [ ] Recovery class and paired recovery record exist.
- [ ] Backup, snapshot, restore, disablement, or compensating evidence is recorded where required.
- [ ] Preflight and dry run/rehearsal completed, or `NOT RUN` is justified.
- [ ] Required review and target authorization records exist.
- [ ] Execution receipt identifies engine, runner, target, revision, payload, timing, and outcome.
- [ ] Object inventory, metadata digest, constraints, permissions, and application compatibility reconcile.
- [ ] Workload or performance claims are supported by named evidence and regression checks.
- [ ] Spatial and temporal semantics remain valid where applicable.
- [ ] Recovery was rehearsed where risk requires it, or the gap remains visible.
- [ ] Documentation, deprecation, incident, correction, cache, and release follow-up are complete.
- [ ] Rollback target or forward-fix lineage is retained.
- [ ] No migration result is misrepresented as release approval, public access approval, or KFM publication.

## No-loss ledger

| v1 material | v1.1 disposition |
|---|---|
| Governed database-migration purpose | Preserved and sharpened |
| Lifecycle invariant | Preserved |
| Database, schema, data, graph, and rollback responsibility split | Preserved and aligned with the parent README |
| DDL, index, constraint, view, function, extension, permission, partition, and storage scope | Preserved and expanded by consequence |
| Lock, downtime, transaction, backup, least-privilege, and lifecycle posture | Preserved and made explicitly target-specific |
| Date-prefixed filename examples | Reframed as examples; stable identity convention remains unverified |
| Required migration record | Preserved as a richer proposed packet |
| Dry-run and validation posture | Preserved and expanded by database object class |
| Rollback-entry requirement | Preserved; coverage explicitly remains unverified |
| Review burden | Preserved, with verified CODEOWNERS routing separated from unverified stewardship |
| Owner placeholders | Replaced with verified routing plus role-assignment uncertainty |
| Open verification list | Preserved and extended |
| Publication boundary | Preserved and clarified |
| Existing anchors | Preserved through explicit compatibility anchors |

<a id="open-verification"></a>

## Open verification register

- [ ] Obtain a recursive tracked inventory of `migrations/database/`.
- [ ] Confirm whether concrete database-migration payloads exist beyond this README.
- [ ] Confirm the active database engine(s), edition(s), version(s), extension set, and target environments.
- [ ] Select and document the canonical database-migration runner or explicitly declare no shared runner.
- [ ] Define a stable database-migration ID and filename ordering convention.
- [ ] Verify one-to-one database-migration-to-recovery pairing.
- [ ] Decide whether paired recovery records must land in the same pull request.
- [ ] Define a machine-readable database-migration packet schema if justified.
- [ ] Define an applied-version or migration-state ledger and its owning root.
- [ ] Define representative disposable database fixtures and valid/invalid migrations for each class.
- [ ] Verify database backup, snapshot, restore, point-in-time recovery, replica, failover, and retention capabilities by environment.
- [ ] Define transaction, lock, statement-timeout, downtime, online-DDL, and maintenance-window classes.
- [ ] Define base-state object-inventory and metadata-digest rules.
- [ ] Define expand-and-contract and staged-breaking compatibility policy.
- [ ] Define producer/consumer adoption evidence and deprecation windows.
- [ ] Define table, column, constraint, index, view, function, trigger, extension, role, grant, partition, and storage checks.
- [ ] Define least-privilege, row-level access, ownership, and deny-path review workflow.
- [ ] Define spatial-extension and temporal-database validation only after engine capabilities are verified.
- [ ] Define database execution receipt placement and schema.
- [ ] Define recovery rehearsal expectations by object and consequence class.
- [ ] Confirm governed API, application, data, graph, map, tile, export, and release review triggers.
- [ ] Confirm accountable stewards and independent approval requirements.
- [ ] Verify branch protection or ruleset requirements for this path.
- [ ] Formalize host-render validation for this README.
- [ ] Revisit this README after the first concrete database-migration packet is implemented.

## Changelog

### v1.1 — 2026-07-24

- Reorganized the lane README to the Directory Rules folder contract.
- Grounded status in current parent-root, rollback-lane, Directory Rules, CODEOWNERS, and bounded repository-search evidence.
- Removed unsupported certainty around database, migration, schema, data, security, application, and release steward assignments.
- Distinguished documentation, engine, payloads, runner, applied state, recovery, release, and publication authority.
- Added database-migration classification, a proposed minimum packet, object-specific validation matrix, execution contract, recovery classes, and definition of done.
- Marked engine, extensions, target environments, tooling, payload depth, applied history, backups, recovery coverage, and production outcomes as unverified.
- Preserved prior anchors, lifecycle law, least-privilege posture, lock/downtime analysis, and rollback requirement.

### v1 — 2026-07-03

- Established the initial database-migration lane contract for DDL, storage behavior, permissions, validation, lock/downtime analysis, and rollback pairing.
