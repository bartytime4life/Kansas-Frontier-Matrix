<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-rollback-readme
title: migrations/rollback/ — Governed Migration Recovery, Rollback, Disablement, Restore, and Forward-Fix Records
type: README; per-directory-readme; nested-migration-lane; recovery-change-control
version: v1.1
status: draft; repository-grounded; documented-lane; pairing-coverage-unverified; rehearsal-coverage-unverified; backup-capability-unverified; execution-history-unverified; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable migration, recovery, database, schema, data, graph, security, policy, incident, and release stewardship assignments were not established
created: 2026-07-03
updated: 2026-07-24
supersedes: v1 documentation at the same path; no migration payload, recovery action, backup, snapshot, database state, schema state, data state, graph state, runtime state, release state, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; migrations; recovery; rollback; forward-fix; evidence-first; fail-closed; non-publisher
current_path: migrations/rollback/README.md
owning_root: migrations/
responsibility: govern recovery posture and paired records for database, schema, data, and graph migrations without becoming the primary migration lane, backup store, incident system, release rollback authority, correction authority, or publication authority
truth_posture: >
  CONFIRMED same-path target; canonical migrations responsibility root; documented database, schema, data, graph, and rollback README lanes;
  Directory Rules requirement that every migration have a corresponding recovery entry, including forward-fix-only cases; current CODEOWNERS
  routing; distinct release rollback-card and release rollback-runbook surfaces / PROPOSED recovery classification, recovery packet, pairing identity,
  invariants, rehearsal, execution, validation, and definition-of-done contracts / UNKNOWN exhaustive migration and recovery inventory, applied
  migrations, target environments, backup and restore capabilities, snapshots, migration engines, execution receipts, recovery outcomes, incident
  integrations, and production history / NEEDS VERIFICATION one-to-one pairing coverage, same-PR enforcement, stable recovery IDs, recovery runner,
  dedicated migration-recovery CI, rehearsal cadence, steward assignments, independent approval, and release integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: fdecd7e2c2308cb546706ab061730d14987bc586
  parent_readme_blob: 48da6b62000d145359bfbd7f8383961c9f285b2a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  release_rollback_cards_blob: c1fc4d27bca8144faa16e1b888ca95c5d2f88eb5
  release_rollback_runbook_blob: 52703a0426f4b3d5829f8da4c235d6e5097aa40a
  codeowners_status: repository default routing resolves this path to @bartytime4life; role-level stewardship and independent approval remain unverified
  inspection_method: exact GitHub file reads, parent and release-recovery evidence review, bounded open-PR overlap search, and current branch-state checks; no recursive Git tree, migration executor, database, graph store, backup system, deployment environment, incident system, recovery rehearsal, or production runtime was inspected
related:
  - ../README.md
  - ../database/README.md
  - ../schema/README.md
  - ../data/README.md
  - ../graph/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/runbooks/ROLLBACK_RUNBOOK.md
  - ../../docs/runbooks/README.md
  - ../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../contracts/README.md
  - ../../schemas/README.md
  - ../../data/README.md
  - ../../policy/README.md
  - ../../tests/README.md
  - ../../tools/validators/README.md
  - ../../release/README.md
  - ../../release/rollback_cards/README.md
  - ../../.github/CODEOWNERS
notes:
  - "v1.1 is a same-path documentation-only modernization grounded in current repository evidence."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract."
  - "The mandatory recovery-entry rule is confirmed; exhaustive one-to-one pairing, rehearsal coverage, executable recovery tooling, backups, restores, and production outcomes were not established."
  - "Static badges summarize inspected repository state only; they are not recovery approval, rehearsal, execution, restoration, release, or publication proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/rollback/` — Governed Migration Recovery, Rollback, Disablement, Restore, and Forward-Fix Records

> **One-line purpose.** Record how each database, schema, data, or graph migration can be safely reversed, disabled, restored, compensated, or forward-fixed—before the migration is accepted—while keeping recovery evidence, authority boundaries, validation, and residual risk visible.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: migration recovery](https://img.shields.io/badge/lane-migration%20recovery-1f6feb?style=flat-square)](#authority-level)
[![Pairing: required](https://img.shields.io/badge/pairing-required-b42318?style=flat-square)](#pairing-and-stable-identity)
[![Coverage: needs verification](https://img.shields.io/badge/coverage-needs%20verification-d4a72c?style=flat-square)](#status)
[![Rehearsal: unverified](https://img.shields.io/badge/rehearsal-unverified-b42318?style=flat-square)](#preflight-rehearsal-execution-and-post-checks)
[![Release authority: no](https://img.shields.io/badge/release%20authority-no-6e7781?style=flat-square)](#release-publication-and-incident-separation)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** `migrations/rollback/` is the documented recovery-record lane beneath the canonical `migrations/` root. Doctrine requires a corresponding recovery entry for every database, schema, data, or graph migration, including cases where direct rollback is unsafe and the only acceptable path is an explicit forward fix. Current bounded evidence does **not** establish exhaustive pairing coverage, a canonical recovery runner, backup or restore capability, recovery rehearsals, execution receipts, or production recovery history.

> [!CAUTION]
> A rollback record, command example, parsed script, passing unit test, branch, pull request, or green unrelated workflow does not prove recoverability. Recovery is proven only for a named migration and target state through pinned inputs, satisfied preconditions, observed rehearsal or execution evidence, post-recovery validation, and an auditable decision record.

> [!WARNING]
> This directory is not a backup store, snapshot archive, database dump location, incident workspace, release rollback-card home, correction register, or publication surface. Never commit credentials, production connection material, restricted payloads, backups, WAL archives, graph exports, raw datasets, or sensitive incident details here.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Classes](#recovery-decision-classes) · [Packet](#minimum-recovery-record) · [Invariants](#recovery-invariants) · [Pairing](#pairing-and-stable-identity) · [Execution](#preflight-rehearsal-execution-and-post-checks) · [Lane guidance](#lane-specific-recovery-guidance) · [Separation](#release-publication-and-incident-separation) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="status--authority"></a>
<a id="repo-fit"></a>
<a id="rollback-record-contract"></a>
<a id="required-rollback-record"></a>
<a id="decision-classes"></a>
<a id="open-verification"></a>

## Purpose

`migrations/rollback/` owns **migration-level recovery records and recovery posture** for changes under:

- `migrations/database/`;
- `migrations/schema/`;
- `migrations/data/`;
- `migrations/graph/`.

The lane exists so recovery is designed with the migration rather than improvised after failure.

Every recovery record must answer:

1. Which exact migration or coordinated migration set does this record pair with?
2. Which pre-migration state is the intended safe target?
3. Is direct reversal safe, partial, unsafe, blocked, or unnecessary?
4. Which irreversible effects may already have occurred?
5. Which backup, snapshot, export, prior artifact, alias, or compensating input is required?
6. Which services, producers, consumers, indexes, projections, caches, and releases are affected?
7. Which evidence proves that the recovery path is applicable?
8. Which validation proves that recovery restored a safe state?
9. Which residual risks remain after recovery?
10. Which follow-up migration, release action, correction, incident action, or review remains open?

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A migration recovery may restore or repair engineering state. It is not itself lifecycle promotion, release approval, publication, correction approval, erasure, or proof that public state changed.

## Authority level

**Canonical nested lane for migration recovery records; subordinate to the authorities that define meaning, valid shape, evidence, admissibility, lifecycle state, incident handling, release, and publication.**

| Question | Controlling authority |
|---|---|
| Where migration recovery records belong | Directory Rules, accepted placement ADRs, parent `migrations/` contract, then this README |
| What the paired migration changes | The applicable sibling migration lane and its pinned payload |
| What an object means | `contracts/` |
| What machine shape is valid | `schemas/` |
| What source or evidence supports state | source registry, `EvidenceRef`, `EvidenceBundle`, receipts, and proofs |
| What policy permits | `policy/` |
| What lifecycle phase owns the payload | `data/<phase>/` |
| How operational recovery is executed | Selected runner, environment controls, credentials held outside the repository, and an applicable runbook |
| How backups or snapshots are created and restored | The responsible platform or storage system and its verified operational controls |
| How security or exposure incidents are handled | Security and incident-response authorities and runbooks |
| Whether a public release is rolled back, corrected, withdrawn, or superseded | `release/`, release rollback cards, correction/withdrawal records, and release runbooks |
| Whether public clients may serve the result | Governed API, policy decision, validation, and release state |

This lane may describe recovery mechanics, prerequisites, validation, and evidence references. It must not silently redefine stronger authorities or claim that a recovery was performed when only documentation exists.

## Status

| Surface | Current evidence | Status |
|---|---|---|
| Rollback lane README | Present on `main` | **CONFIRMED — documentation** |
| Parent migration root | Present and identifies rollback as one of five migration lanes | **CONFIRMED — documentation** |
| Database migration lane README | Present | **CONFIRMED — documentation** |
| Schema migration lane README | Present | **CONFIRMED — documentation** |
| Data migration lane README | Present | **CONFIRMED — documentation** |
| Graph migration lane README | Present | **CONFIRMED — documentation** |
| Mandatory recovery entry for every migration | Required by Directory Rules and migration documentation | **CONFIRMED doctrine** |
| Distinct release rollback-card lane | Present under `release/rollback_cards/` | **CONFIRMED — documentation** |
| Distinct release rollback runbook | Present under `docs/runbooks/` | **CONFIRMED — draft documentation** |
| Concrete migration payload inventory | Not established in bounded inspection | **UNKNOWN / NEEDS VERIFICATION** |
| One-to-one migration-to-recovery pairing | Required; exhaustive coverage not inspected | **NEEDS VERIFICATION** |
| Same-PR pairing enforcement | Not established | **NEEDS VERIFICATION** |
| Stable recovery-record identifier convention | Not established | **NEEDS VERIFICATION** |
| Canonical migration or recovery runner | Not established | **UNKNOWN** |
| Backup, snapshot, restore, or point-in-time-recovery capability | Not inspected | **UNKNOWN** |
| Recovery rehearsal coverage | Not inspected | **UNKNOWN** |
| Recovery execution receipts and history | Not inspected | **UNKNOWN** |
| Dedicated migration-recovery CI gate | Not established | **NEEDS VERIFICATION** |
| Incident-response integration | Not established | **NEEDS VERIFICATION** |
| GitHub routing | Repository default routes this path to `@bartytime4life` | **CONFIRMED routing; stewardship unverified** |
| Independent approval or separation of duties | Doctrine exists; enforcement not inspected | **NEEDS VERIFICATION** |
| Release or publication authority | Not owned by this lane | **DENIED by boundary** |

The lane is therefore **documentation-grounded but implementation-unverified**. Treat record templates as proposed control contracts, not proof that recovery tooling or operational capability exists.

## What belongs here

Use `migrations/rollback/` when the primary responsibility is documenting and reviewing recovery posture for a migration.

Accepted material includes:

- one recovery record paired to a database, schema, data, or graph migration;
- recovery records for coordinated migration sets where the dependency order is explicit;
- reversible rollback plans;
- partial rollback plans that name unreverted effects;
- disablement or feature-gate plans;
- restore plans referencing external backup or snapshot identifiers without embedding protected material;
- compensating migration plans;
- forward-fix-only decisions with explicit justification;
- blocked recovery records naming prerequisites and escalation paths;
- recovery preflight and rehearsal plans;
- sanitized rehearsal summaries;
- sanitized execution and post-recovery validation summaries;
- risk analysis for data loss, identity remapping, evidence closure, contract compatibility, graph topology, policy, sensitivity, public API behavior, caches, derivatives, and release state;
- references to migration payloads, commits, issues, runbooks, receipts, proofs, backup metadata, release records, incident records, and corrective migrations;
- residual-risk and follow-up registers.

Each record must remain inspectable without exposing credentials, protected infrastructure details, restricted data, or operational secrets.

## What does NOT belong here

Do not use `migrations/rollback/` as a parallel migration lane, backup system, release authority, incident system, or data store.

The following do not belong here:

- primary database, schema, data, or graph migration payloads;
- canonical contracts or JSON Schemas;
- policy bundles or policy decisions;
- source descriptors, canonical evidence, `EvidenceBundle` payloads, or source archives;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED datasets;
- database dumps, graph dumps, snapshots, backup archives, WAL files, restore images, exported tables, bulk triplets, tiles, rasters, or model weights;
- release manifests, release rollback cards, correction notices, withdrawal notices, release approvals, or publication decisions;
- live credentials, DSNs, connection strings, tokens, API keys, private keys, certificates, kubeconfigs, `.env` files, or private endpoints;
- unredacted incident details, vulnerability analysis, private host inventories, sensitive logs, or restricted relationship/data samples;
- destructive commands without preconditions, scope, safe defaults, validation, and recovery controls;
- claims that a recovery path is “tested,” “ready,” or “successful” without observed evidence;
- forward-fix-only labels used to avoid analysis or review;
- silent changes to policy, release state, evidence authority, review state, sensitivity, rights, or public visibility.

When prohibited material appears here, stop normal processing, isolate it through the appropriate secure path, record the correction, and follow security or governance incident procedures where required.

## Inputs

A recovery record must be grounded in pinned, resolvable inputs.

| Input | Minimum expectation | Failure posture |
|---|---|---|
| Paired migration | Exact repository path, stable migration ID if defined, commit or payload digest | Reject ambiguous recovery record |
| Migration lane | `database`, `schema`, `data`, `graph`, or explicit coordinated set | Reject unsupported lane |
| Target environment class | Local, test, staging, production, release-relevant shared state, or other governed class | Do not execute against an unnamed target |
| Base state | Version, manifest, schema digest, object inventory, row/edge counts, aliases, or other state identifier appropriate to the lane | Block when prior state cannot be identified |
| Intended recovery state | Exact safe target or bounded forward-fix target | Block vague “restore previous” language |
| Preconditions | Service state, maintenance window, compatibility version, backup/snapshot availability, access, freeze, or approval | Fail closed |
| Backup or snapshot reference | External identifier and verification status when required; never protected payload bytes | Block high-risk recovery when required support is absent |
| Affected systems | Producers, consumers, services, indexes, projections, caches, jobs, and public surfaces | Expand scope before approval |
| Evidence and reason | Issue, defect report, validation result, incident reference, receipt, proof, or review record | Abstain from unsupported recovery |
| Policy and sensitivity context | Public/internal/restricted posture and relevant rights or sovereignty constraints | Quarantine or escalate |
| Recovery payload | Pinned script, query, configuration change, restore operation, compensating migration, or forward-fix reference | Reject mutable or unreviewed payload |
| Validation plan | Preconditions, invariants, expected deltas, and safe-state criteria | Do not approve without tests |
| Review record | Applicable review and separation evidence | Hold when required review is missing |

A path reference alone is insufficient when the referenced artifact cannot be resolved or its version is ambiguous.

## Outputs

This lane produces **recovery governance records**, not recovered state by itself.

A complete recovery effort may emit:

| Output | Purpose | Authority boundary |
|---|---|---|
| Recovery record | Defines decision class, scope, preconditions, steps, validation, and residual risk | Migration recovery authority only |
| Pairing pointer | Binds record to exact migration payload or coordinated set | Does not approve the migration |
| Rehearsal plan | Defines safe non-production or isolated proof procedure | Not evidence until executed |
| Rehearsal receipt | Records observed result, environment, payload digest, checks, and limitations | Evidence for tested scope only |
| Execution receipt | Records observed recovery action and outcome | Not release approval |
| Post-recovery validation report | Shows whether declared invariants hold | Must name unresolved failures |
| Residual-risk record | Captures irreversible effects and follow-up obligations | Does not waive policy |
| Compensating or forward-fix reference | Names the corrective migration when reversal is unsafe | Primary payload belongs in sibling migration lane |
| Release-impact handoff | Points to release rollback/correction/withdrawal records where public state is affected | `release/` remains authoritative |
| Incident handoff | Points to incident/security records where applicable | Incident authority remains external to this lane |
| Drift or documentation update | Records mismatches and updates operating guidance | Documentation is not runtime proof |

Statuses should remain finite and explicit:

```text
PROPOSED
READY_FOR_REVIEW
APPROVED_FOR_REHEARSAL
REHEARSED
APPROVED_FOR_EXECUTION
EXECUTING
RECOVERED
PARTIALLY_RECOVERED
FORWARD_FIXED
FAILED
BLOCKED
SUPERSEDED
NOT_APPLICABLE
```

Use only statuses actually supported by evidence. A file existing in Git does not make it `REHEARSED`, `APPROVED_FOR_EXECUTION`, or `RECOVERED`.

## Validation

Validation must match the recovery decision, affected lane, target state, and risk.

### Documentation and pairing validation

| Check | Expected result |
|---|---|
| Path placement | Recovery record is under `migrations/rollback/` |
| Paired migration | Exact migration path or coordinated set resolves |
| Pairing uniqueness | Ambiguous duplicate recovery records are reconciled or explicitly superseded |
| Decision class | One finite recovery class is selected |
| Stable identity | Recovery ID and migration ID are deterministic or explicitly mapped |
| Payload pinning | Migration and recovery payload digests or immutable refs are recorded |
| Preconditions | Required prior state, access, service, backup, and review conditions are explicit |
| Scope | Affected objects, systems, derivatives, and public surfaces are named |
| Authority | Record does not claim release, policy, incident, or publication authority |
| Secret and sensitivity scan | No protected material is committed |
| Link integrity | Relative repository links resolve |
| Supersession | Replaced records retain lineage |

### Technical validation

| Risk surface | Minimum validation |
|---|---|
| Database structure | Object existence, column/constraint/index state, permissions, extension state, compatibility, lock/downtime outcome |
| Schema or contract | Old/new shape compatibility, producer/consumer versions, validation corpus, aliases, deprecation state |
| Data state | Counts, digests, identity mapping, evidence links, lifecycle phase, temporal/spatial scope, duplicate/orphan policy |
| Graph state | Node/edge/triplet counts, endpoint closure, relationship types, directionality/cardinality, evidence closure, projections |
| Access and policy | Grants, policy decisions, sensitivity labels, deny-by-default behavior |
| Public API or UI | Governed API behavior, cache state, layer availability, error posture, no bypass to internal stores |
| Derived indexes | Rebuild or invalidation status, source version, projection parity, stale-result prevention |
| Backup or restore | Backup identity, creation status, restore applicability, integrity check, retention and access posture |
| Forward fix | Corrective migration exists, is pinned, has its own recovery record, and closes the original defect |
| Failure | Partial state is identified, writes are stopped or contained, and escalation is recorded |

### Recovery evidence grades

| Grade | Meaning | Permitted claim |
|---|---|---|
| `DOCUMENTED` | Record and plan exist | “Recovery posture is documented.” |
| `STATIC_VALIDATED` | Syntax, links, schemas, or dry-run compilation checked | “The record passed static validation.” |
| `REHEARSED_ISOLATED` | Executed in an isolated representative environment | “Recovery was rehearsed for the named environment and state.” |
| `REHEARSED_STAGING` | Executed against governed staging state | “Recovery was rehearsed in staging with recorded limitations.” |
| `EXECUTED` | Performed against the named target | “Recovery was executed on the named target.” |
| `VERIFIED` | Post-checks and independent review confirmed safe state | “Recovery completed and the declared checks passed.” |

Never generalize a lower grade into a stronger claim.

### README validation

For this README update, validate:

- one H1;
- unique heading anchors;
- balanced fenced code blocks;
- the required first twelve H2 sections in Directory Rules order;
- preserved legacy anchors;
- valid relative links;
- no placeholder owner represented as confirmed;
- no implication that migration recovery has been rehearsed or executed.

## Review burden

CODEOWNERS routing is not stewardship, approval, or proof of review. Required role assignments remain governance facts that must be established separately.

| Change or recovery class | Minimum review posture |
|---|---|
| README-only wording with no recovery behavior | Documentation reviewer and migration-responsibility reviewer |
| Additive, low-risk, fully reversible migration | Affected lane reviewer plus migration-recovery reviewer |
| Database constraint, permission, function, trigger, extension, partition, or destructive structure change | Database-responsibility reviewer plus migration-recovery reviewer; security review where access changes |
| Schema or contract compatibility recovery | Schema and contract responsibility reviewers plus migration-recovery reviewer |
| Data deletion, remap, merge, split, normalization, or backfill recovery | Data, evidence, and migration-recovery reviewers |
| Graph identity, topology, relationship, or evidence-link recovery | Graph, evidence, and migration-recovery reviewers |
| Backup restore or point-in-time recovery | Platform/storage responsibility reviewer plus affected lane and migration-recovery reviewers |
| Forward-fix-only decision | Affected lane, migration-recovery, and risk-acceptance reviewers |
| Public API, map layer, export, tile, search, or AI-surface effect | Release responsibility reviewer plus affected application/domain reviewers |
| Sensitive, rights-uncertain, sovereign, living-person, DNA, archaeology, rare-species, or infrastructure impact | Policy/sensitivity and applicable rights/domain reviewers |
| Security or exposure incident | Security/incident authority plus affected lane and migration-recovery reviewers |
| Irreversible or partially recoverable migration | Independent approval and explicit residual-risk acceptance |
| Recovery execution against shared or production state | Operator/executor separated from approval when maturity and risk require it; observed receipt mandatory |

Reviewers must be named through verified assignments or review records. Do not replace missing governance with placeholder role text presented as fact.

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Canonical migration root and shared migration contract |
| [`../database/`](../database/README.md) | Database migration plans and payloads |
| [`../schema/`](../schema/README.md) | Schema/contract compatibility migrations |
| [`../data/`](../data/README.md) | Data backfills, repairs, remaps, and rebuilds |
| [`../graph/`](../graph/README.md) | Graph/triplet identity, topology, evidence, and projection migrations |
| [`../../contracts/`](../../contracts/README.md) | Human-readable semantic authority |
| [`../../schemas/`](../../schemas/README.md) | Machine-valid shape authority |
| [`../../data/`](../../data/README.md) | Lifecycle payload and provenance roots |
| [`../../policy/`](../../policy/README.md) | Allow, deny, restrict, generalize, and abstain rules |
| [`../../tests/`](../../tests/README.md) | Test organization |
| [`../../tools/validators/`](../../tools/validators/README.md) | Reusable validator implementation |
| [`../../docs/runbooks/`](../../docs/runbooks/README.md) | Operational runbooks |
| [`../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../docs/runbooks/ROLLBACK_RUNBOOK.md) | Draft release rollback procedure; explicitly excludes migration rollback |
| [`../../release/`](../../release/README.md) | Release decisions, manifests, correction, withdrawal, and public-state authority |
| [`../../release/rollback_cards/`](../../release/rollback_cards/README.md) | Release-facing review cards; not migration recovery records |
| [`../../docs/governance/SEPARATION_OF_DUTIES.md`](../../docs/governance/SEPARATION_OF_DUTIES.md) | Governance guidance for independent duties |
| [`../../docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Repository and doctrine drift tracking |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | Canonical placement and README structure rules |
| [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review routing only |

## ADRs

No accepted ADR was verified in this session as the sole controlling decision for migration recovery-record shape, identifier syntax, same-PR pairing, rehearsal grade, or forward-fix approval.

Relevant ADR-class decisions still requiring confirmation include:

- stable migration and recovery identifier format;
- whether each migration and recovery record must land in the same pull request;
- one-to-one versus coordinated-set pairing;
- canonical migration and recovery runner;
- environment classification and approval rules;
- backup and snapshot requirements by migration class;
- required rehearsal grade before shared or production execution;
- independent approval thresholds;
- forward-fix-only risk acceptance;
- incident-response handoff;
- release handoff when public state is affected;
- recovery receipt and ledger schemas;
- retention and supersession rules.

Until accepted decisions are verified, preserve existing paths, keep proposals explicit, and avoid introducing parallel recovery homes.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review basis | Current `main` target, parent migrations README, Directory Rules, CODEOWNERS, release rollback-card README, and draft release rollback runbook |
| Review status | **Repository-grounded documentation modernization** |
| Implementation status | **UNKNOWN / NEEDS VERIFICATION** |
| Next review trigger | First concrete recovery record; migration/recovery pairing validator; selected runner; rehearsal; backup/restore integration; forward-fix-only decision; incident-driven recovery; or public-impacting migration recovery |

---

## Current bounded topology

```text
Kansas-Frontier-Matrix/
└── migrations/
    ├── README.md
    ├── database/
    │   └── README.md
    ├── schema/
    │   └── README.md
    ├── data/
    │   └── README.md
    ├── graph/
    │   └── README.md
    └── rollback/
        └── README.md      ◀── this lane
```

The topology above is confirmed only at the README level through direct file inspection. It does not prove that migration payloads or recovery records exist below those READMEs.

### Responsibility split

| Lane | Primary responsibility | Recovery relationship |
|---|---|---|
| `database/` | Database-managed structure, permissions, indexes, constraints, functions, triggers, extensions, partitions, storage behavior | Paired recovery record here |
| `schema/` | Contract and machine-shape compatibility transitions | Paired recovery record here |
| `data/` | Data repair, backfill, normalization, remap, rebuild, relocation, correction, supersession | Paired recovery record here |
| `graph/` | Relationship vocabulary, graph/triplet identity, topology, evidence links, projections, indexes | Paired recovery record here |
| `rollback/` | Recovery decision, prerequisites, rehearsal, execution evidence, post-checks, residual risk, handoffs | Does not own primary migration payload |

## Recovery decision classes

Choose one primary class and name any secondary mechanism.

| Class | Use when | Required evidence | Common hazard |
|---|---|---|---|
| `REVERSIBLE_ROLLBACK` | The migration can return to an identified prior state without unacceptable loss | Prior state, reversal payload, validation, rehearsal or execution evidence | Assuming reversal is lossless |
| `DISABLE_OR_DEACTIVATE` | New behavior can be safely gated, disabled, or routed away without restoring every byte immediately | Gate/control identity, safe fallback, consumer behavior, validation | Leaving hidden writes active |
| `RESTORE_FROM_BACKUP` | Recovery requires a verified backup, snapshot, export, or point-in-time state | Backup identity, integrity, applicability, restore procedure, post-check | Backup exists but is unusable |
| `COMPENSATING_MIGRATION` | A new migration restores invariants without literal reversal | Corrective migration, its own recovery record, expected deltas | Compensation creates new drift |
| `PARTIAL_ROLLBACK` | Only a bounded portion can be safely reversed | Reverted and unreverted effects, residual risk, forward path | Presenting partial recovery as full |
| `FORWARD_FIX_ONLY` | Direct reversal is more dangerous, lossy, invalid, or impossible | Explicit reason, corrective migration, risk acceptance, containment | Using label to avoid planning |
| `BLOCKED` | Required state, access, backup, approval, or tooling is unavailable | Named blocker, owner/authority, containment, next trigger | Continuing mutation while blocked |
| `NOT_APPLICABLE` | Documentation-only or non-persistent change has no runtime recovery action | Explanation and validation | Misclassifying persistent effects |
| `SUPERSEDED` | A newer recovery record replaces this one | Superseding ID and preserved lineage | Losing historical decision context |
| `FAILED_RECOVERY` | Attempted recovery failed or left unsafe partial state | Observed evidence, containment, incident/escalation, next action | Retrying blindly |

“Forward fix” is not synonymous with success. The corrective migration must be reviewed, executed, validated, and paired with its own recovery record.

## Minimum recovery record

The following YAML is a **PROPOSED** machine-readable shape. It is guidance until a canonical schema and validator are verified.

```yaml
recovery_id: "KFM-MIGREC-YYYYMMDD-<slug>-<ordinal>"
record_version: "1"
status: "PROPOSED"

paired_migration:
  migration_id: "<stable migration id or NEEDS VERIFICATION>"
  lane: "database | schema | data | graph | coordinated"
  paths:
    - "migrations/<lane>/<migration-file>"
  commit: "<full commit sha>"
  payload_digests:
    - algorithm: "sha256"
      digest: "<hex>"
  migration_status: "<proposed | approved | applied | failed | unknown>"

decision:
  primary_class: "REVERSIBLE_ROLLBACK"
  secondary_mechanisms: []
  reason: "<evidence-grounded explanation>"
  irreversible_effects: []
  residual_risks: []

target:
  environment_class: "<local | test | staging | production | shared | other>"
  environment_id: "<non-secret stable identifier>"
  base_state:
    identifiers: []
    digests: []
    observed_at: "<RFC3339 timestamp or UNKNOWN>"
  intended_safe_state:
    identifiers: []
    invariants: []

preconditions:
  approvals: []
  maintenance_window: null
  write_freeze: null
  service_state: []
  consumer_versions: []
  required_access: []
  backups:
    - external_id: "<reference only>"
      status: "<verified | unverified | unavailable>"
      integrity_evidence: "<reference>"
  blockers: []

scope:
  database_objects: []
  schema_contracts: []
  data_families: []
  graph_families: []
  identities: []
  evidence_links: []
  policies: []
  applications: []
  jobs: []
  indexes: []
  projections: []
  caches: []
  public_surfaces: []
  sensitive_classes: []

recovery_payload:
  paths: []
  immutable_refs: []
  expected_operations: []
  safe_defaults: []
  stop_conditions: []
  idempotence: "<safe | detected | blocked | unknown>"

validation:
  preflight_checks: []
  rehearsal_checks: []
  execution_checks: []
  post_recovery_checks: []
  safe_state_criteria: []
  failure_criteria: []
  evidence_outputs: []

handoffs:
  release_records: []
  incident_records: []
  correction_records: []
  drift_records: []
  follow_up_migrations: []

review:
  author: "<verified identity>"
  reviewers: []
  approvals: []
  separation_required: null
  risk_acceptance: null

receipts:
  rehearsal: null
  execution: null
  post_verification: null

supersession:
  supersedes: []
  superseded_by: null
```

### Human-readable minimum record

```markdown
# <recovery-id> — <paired migration purpose>

## Status
<finite status>

## Paired migration
<exact path, commit, migration ID if defined, payload digest>

## Recovery decision
<class and evidence-grounded reason>

## Target and safe state
<environment class, base state, intended safe state>

## Preconditions and blockers
<backup, access, service, compatibility, review, freeze, maintenance window>

## Scope and irreversible effects
<objects, identities, data, graph, evidence, policy, applications, derivatives, public surfaces>

## Recovery payload
<pinned reversal, disablement, restore, compensation, or forward-fix reference>

## Preflight and rehearsal
<checks, environment, expected deltas, stop conditions>

## Execution controls
<operator boundary, safe defaults, observation, abort criteria>

## Validation
<post-checks and safe-state criteria>

## Residual risk
<unreverted or uncertain effects>

## Release / incident handoff
<paths or N/A>

## Receipts and evidence
<rehearsal, execution, post-verification references>

## Review and approvals
<verified identities and records>

## Supersession and follow-up
<lineage, corrective migration, open work>
```

## Recovery invariants

Every recovery must preserve or explicitly repair the applicable invariants.

| Invariant | Required posture |
|---|---|
| **Cite-or-abstain** | Do not claim safe recovery without evidence |
| **Lifecycle integrity** | Recovery must not bypass governed lifecycle or promote payloads by file movement |
| **Trust membrane** | Public clients remain separated from internal/canonical stores during recovery |
| **Semantic authority** | Recovery does not redefine contract meaning |
| **Machine-shape authority** | Recovery state validates against applicable schemas or documents a compatibility exception |
| **Evidence closure** | `EvidenceRef` relationships continue to resolve to appropriate `EvidenceBundle` support or fail closed |
| **Source-role anti-collapse** | Primary, corroborating, context, and restricted roles remain distinct |
| **Identity lineage** | Merges, splits, remaps, tombstones, aliases, and supersession remain auditable |
| **Temporal integrity** | Valid, observed, published, superseded, and effective times are not silently conflated |
| **Spatial integrity** | CRS, precision, generalization, geometry validity, and geographic scope remain controlled |
| **Policy preservation** | Allow, deny, restrict, generalize, and abstain posture does not weaken silently |
| **Sensitivity and rights** | Restricted and rights-uncertain material remains protected or becomes more restrictive |
| **Least privilege** | Recovery access and grants are bounded to required operations |
| **Derived non-sovereignty** | Tiles, indexes, projections, embeddings, scenes, summaries, and caches remain derived carriers |
| **Auditability** | Inputs, operator/tool, timestamps, payloads, outcomes, reviews, and receipts remain traceable |
| **Reversibility visibility** | Irreversible effects and forward-fix-only posture are explicit |
| **Correction lineage** | Prior state is preserved through supersession, tombstone, or correction references where required |
| **Release separation** | Engineering recovery does not silently alter release or publication state |
| **Fail-safe behavior** | Missing preconditions, evidence, or validation stops or narrows the action |

## Pairing and stable identity

Every migration must resolve to a corresponding recovery entry, including:

- documentation-only migrations, which may use `NOT_APPLICABLE` with reason;
- forward-fix-only migrations;
- coordinated migrations spanning multiple lanes;
- corrective migrations created after a failed migration;
- superseding migrations.

### Proposed naming

Until a canonical ID decision is accepted, preserve the established date-and-purpose relationship:

```text
migrations/<lane>/YYYYMMDD-short-purpose.*
migrations/rollback/YYYYMMDD-short-purpose.md
```

For collisions or coordinated sets, add a stable ordinal or explicit migration ID rather than silently overwriting an existing record.

### Pairing validation rules

A future validator should fail when:

- a migration payload lacks a corresponding recovery record;
- a recovery record names a missing migration;
- multiple active recovery records claim the same migration without supersession;
- a coordinated record omits one member;
- payload digests do not match;
- a forward-fix record lacks a corrective migration reference;
- a corrective migration lacks its own recovery record;
- a record claims rehearsal or execution without a receipt;
- a release-impacting recovery lacks a release handoff;
- a sensitive or incident recovery lacks required escalation.

Whether this validator exists today is **NEEDS VERIFICATION**.

## Preflight, rehearsal, execution, and post-checks

### 1. Preflight

Before any rehearsal or execution:

1. Resolve the paired migration and payload digests.
2. Identify the exact target environment and base state.
3. Confirm applicability of the recovery decision.
4. Freeze or contain writes when required.
5. Identify services, jobs, consumers, caches, projections, and releases.
6. Verify backups or snapshots when required.
7. Confirm access and least-privilege posture.
8. Resolve policy, sensitivity, rights, and incident constraints.
9. Run static and read-only checks.
10. Confirm review and approval requirements.
11. Define stop conditions and partial-state handling.
12. Confirm evidence destinations and receipt fields.

If the actual state differs materially from the record, stop and update or supersede the record.

### 2. Rehearsal

Prefer an isolated or staging rehearsal for material recoveries.

A rehearsal receipt should include:

- recovery and migration IDs;
- environment class and non-secret identifier;
- base-state identifiers and digests;
- payload refs and digests;
- start/end timestamps;
- operator/tool identity;
- observed operations;
- expected versus actual deltas;
- validation results;
- failures and limitations;
- restore duration and resource impact where relevant;
- residual risks;
- receipt digest and immutable storage reference.

A rehearsal proves only the state and environment actually tested.

### 3. Execution

Execution must:

- use pinned payloads;
- verify target and preconditions immediately before mutation;
- default to no-op, read-only, transaction, checkpoint, canary, or bounded batch where supported;
- stop on unknown target, digest mismatch, failed invariant, or unapproved scope;
- prevent concurrent conflicting migrations or recoveries;
- preserve logs and receipts without exposing protected material;
- record every partial or failed result;
- avoid silent retries that obscure state;
- maintain containment until post-checks pass.

### 4. Post-recovery checks

Post-checks must confirm:

- declared safe-state identifiers;
- structural and semantic validity;
- data/graph/evidence integrity;
- identity and supersession lineage;
- policy and sensitivity posture;
- producer and consumer compatibility;
- job, index, projection, and cache state;
- public API and UI posture where applicable;
- release and incident handoffs;
- residual risk and follow-up ownership;
- no hidden partial state.

When checks fail, status becomes `FAILED`, `PARTIALLY_RECOVERED`, or `BLOCKED`; do not label the result recovered.

## Lane-specific recovery guidance

### Database migrations

Address:

- transactional reversibility;
- table/column/index/constraint state;
- generated values and sequences;
- triggers, functions, procedures, and views;
- roles, grants, ownership, and row-level controls;
- extensions and engine-version compatibility;
- locks, downtime, long-running statements, and concurrent writes;
- backup/restore or point-in-time requirements;
- application compatibility;
- data written under the new structure.

Dropping a column may be syntactically reversible but semantically irreversible after data loss. Record the difference.

### Schema and contract migrations

Address:

- producer and consumer version skew;
- aliases and deprecated fields;
- defaulting and coercion behavior;
- stored payload compatibility;
- schema registry or generated-code state;
- validation corpus;
- compatibility windows;
- public API shape;
- documentation and examples;
- contract meaning versus machine shape.

Restoring an old schema without restoring compatible data and consumers is not complete recovery.

### Data migrations

Address:

- deterministic identity;
- row/object counts and digests;
- mapping tables and crosswalks;
- evidence and provenance links;
- source-role distinctions;
- temporal and spatial fields;
- duplicate, orphan, null, and quarantine policy;
- lifecycle phase and promotion state;
- derived artifacts and caches;
- deletion, merge, split, remap, and enrichment reversibility.

When original values were overwritten without preserved lineage, direct rollback may be impossible; use explicit partial or forward-fix posture.

### Graph migrations

Address:

- node, edge, assertion, and triplet identity;
- endpoint closure;
- relationship direction and cardinality;
- relationship-type vocabulary;
- provenance and evidence closure;
- confidence and review posture;
- temporal and spatial scope;
- sensitive relationships;
- graph projections and indexes;
- orphan and duplicate rules;
- correction and supersession lineage.

Rebuilding a projection is not recovery of canonical graph truth unless the governed inputs and transformation are pinned.

### Coordinated migrations

Address the full dependency graph:

```text
database -> schema/contract -> data -> graph -> application -> indexes/caches -> release
```

The actual order may differ, but it must be explicit. A coordinated recovery must define:

- member migrations and digests;
- execution and reversal order;
- compatibility checkpoints;
- stop points;
- partial-state handling;
- compensating actions;
- release and incident handoffs.

## Release, publication, and incident separation

Migration recovery and release rollback are related but distinct.

| Surface | Owns | Does not own |
|---|---|---|
| `migrations/rollback/` | Migration-level recovery decision, mechanics, rehearsal, execution evidence, technical post-checks | Public release rollback decision |
| `release/rollback_cards/` | Compact release-facing review cards and handoff | Migration mechanics |
| `docs/runbooks/ROLLBACK_RUNBOOK.md` | Draft procedure for governed rollback of a published release | Database/schema/data/graph migration rollback |
| `release/` | Manifests, decisions, corrections, withdrawals, public rollback/correction state | Primary migration payload |
| Incident/security system | Exposure containment, investigation, credential rotation, incident decisions | Routine migration record authority |
| Backup/storage platform | Backup creation, integrity, retention, restore execution | Release approval or semantic truth |

When a migration recovery affects public state:

1. Contain unsafe engineering state.
2. Preserve the trust membrane.
3. Open the applicable release review, rollback, correction, withdrawal, or supersession record.
4. Invalidate or rebuild affected derivatives through governed paths.
5. Keep public clients on safe governed interfaces.
6. Record both technical and release evidence.
7. Do not mark public recovery complete until release authorities close their records.

When recovery follows a security or exposure incident, link only non-sensitive incident identifiers and approved summaries here.

## Definition of done

A recovery record is complete only when applicable items are satisfied.

### Documentation readiness

- [ ] Exact paired migration or coordinated set resolves.
- [ ] Migration and recovery payloads are pinned.
- [ ] Decision class and reason are explicit.
- [ ] Target, base state, intended safe state, and environment class are named.
- [ ] Preconditions, blockers, stop conditions, and failure posture are defined.
- [ ] Backup/snapshot requirement and status are explicit.
- [ ] Affected systems, derivatives, and public surfaces are inventoried.
- [ ] Irreversible effects and residual risks are explicit.
- [ ] Validation and safe-state criteria are reviewable.
- [ ] Recovery, release, incident, and correction authority boundaries are preserved.
- [ ] Required reviews and approvals are recorded.
- [ ] Supersession lineage is intact.

### Rehearsal readiness

- [ ] Representative environment and base state are defined.
- [ ] Protected credentials and payloads remain outside the repository.
- [ ] Payload digest and target identity checks are automated or repeatable.
- [ ] Expected deltas and stop conditions are measurable.
- [ ] Rehearsal receipt format is defined.
- [ ] Failure cleanup or containment is defined.

### Execution completion

- [ ] Preconditions were rechecked immediately before execution.
- [ ] Observed execution receipt exists.
- [ ] Post-recovery checks passed or failures are explicit.
- [ ] Residual risks and partial state are recorded.
- [ ] Corrective/forward-fix migrations are linked and paired.
- [ ] Release or incident handoffs are closed or explicitly open.
- [ ] Documentation and drift records are updated.
- [ ] Independent verification is recorded where required.

A `PROPOSED` or `DOCUMENTED` record can be complete as documentation without being complete as rehearsal or execution. Keep those states distinct.

## Open verification register

| ID | Verification item | Current status | Evidence needed |
|---|---|---|---|
| `MIG-REC-001` | Exhaustive inventory of migration payloads | **UNKNOWN** | Recursive tree and file classification |
| `MIG-REC-002` | One-to-one recovery pairing coverage | **NEEDS VERIFICATION** | Pairing validator or complete inventory |
| `MIG-REC-003` | Same-PR migration/recovery enforcement | **NEEDS VERIFICATION** | Workflow, ruleset, or accepted ADR |
| `MIG-REC-004` | Stable migration and recovery ID convention | **NEEDS VERIFICATION** | Schema, ADR, or registry |
| `MIG-REC-005` | Canonical migration/recovery runner | **UNKNOWN** | Current config, tooling, and tests |
| `MIG-REC-006` | Backup and snapshot capability by environment | **UNKNOWN** | Platform evidence and restore tests |
| `MIG-REC-007` | Point-in-time recovery support | **UNKNOWN** | Engine/platform configuration and drill |
| `MIG-REC-008` | Recovery rehearsal cadence and evidence grade | **NEEDS VERIFICATION** | Policy, runbook, workflow, receipts |
| `MIG-REC-009` | Dedicated migration-recovery CI | **NEEDS VERIFICATION** | Workflow and path filters |
| `MIG-REC-010` | Recovery receipt schema and storage | **NEEDS VERIFICATION** | Contract/schema and examples |
| `MIG-REC-011` | Applied migration/version ledger | **NEEDS VERIFICATION** | Registry or environment evidence |
| `MIG-REC-012` | Forward-fix-only approval process | **NEEDS VERIFICATION** | Accepted governance record |
| `MIG-REC-013` | Independent approval enforcement | **NEEDS VERIFICATION** | Rulesets, review records, assignments |
| `MIG-REC-014` | Incident-response handoff | **NEEDS VERIFICATION** | Runbook and tested flow |
| `MIG-REC-015` | Release rollback/correction integration | **NEEDS VERIFICATION** | Linked example and validation |
| `MIG-REC-016` | Secret and sensitive-output redaction | **NEEDS VERIFICATION** | Tooling and tests |
| `MIG-REC-017` | Recovery supersession and retention | **NEEDS VERIFICATION** | ADR or registry rules |
| `MIG-REC-018` | Production recovery history | **UNKNOWN** | Auditable execution receipts |
| `MIG-REC-019` | Role-level stewardship assignments | **NEEDS VERIFICATION** | Approved assignments |
| `MIG-REC-020` | Recursive link and path integrity | **NEEDS VERIFICATION** | Repository-wide validation |

## No-loss ledger

| Legacy concept | v1.1 disposition |
|---|---|
| Required recovery entry for every migration | Preserved and strengthened |
| Forward-fix-only option | Preserved with stricter evidence and risk requirements |
| Reversible, partial, blocked, and not-applicable classes | Preserved and expanded |
| Database/schema/data/graph pairing | Preserved |
| Risk analysis | Expanded across identity, evidence, policy, sensitivity, derivatives, public state, and incidents |
| Validation plan | Expanded into documentation, technical, evidence-grade, rehearsal, execution, and post-check layers |
| Release impact | Preserved with explicit authority separation |
| Incident/security impact | Preserved with secure handoff boundary |
| No secret or backup payloads | Preserved and strengthened |
| Audit trail | Expanded to payload digests, target state, receipts, reviews, supersession, and residual risk |
| Naming convention | Preserved as proposed pending canonical ID decision |
| Open verification checklist | Converted into traceable verification register |
| Placeholder owners | Removed as unsupported certainty; CODEOWNERS routing retained accurately |
| “Ready” ambiguity | Replaced with evidence-graded states |
| Release rollback-card confusion | Resolved through explicit boundary table |

## Changelog

### v1.1 — 2026-07-24

- Modernized the README in place.
- Applied the Directory Rules folder-README section order.
- Replaced placeholder ownership with verified CODEOWNERS routing and bounded governance claims.
- Added a repository-grounded status table.
- Clarified migration recovery versus release rollback, incident response, backups, and publication.
- Added recovery evidence grades and finite statuses.
- Expanded decision classes, record fields, pairing rules, invariants, rehearsal, execution, post-checks, lane-specific guidance, and definition of done.
- Added open-verification and no-loss ledgers.
- Preserved legacy anchors and core doctrine.

### v1 — 2026-07-03

- Created the draft rollback and forward-fix README.
