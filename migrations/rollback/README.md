<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-rollback-readme
title: migrations/rollback/ — Rollback and Forward-Fix Records for Migration Governance
type: per-directory-readme
version: v1
status: draft
owners:
  - <migration-steward>
  - <rollback-steward>
  - <release-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - migrations/README.md
  - migrations/database/
  - migrations/schema/
  - migrations/data/
  - migrations/graph/
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
  - policy/
  - release/
  - schemas/contracts/v1/
  - contracts/
tags:
  - kfm
  - migrations
  - rollback
  - forward-fix
  - recovery-records
  - validation
  - provenance
  - auditability
  - release-safety
notes:
  - "This folder records rollback and forward-fix posture for migrations. It is not a release rollback-card home, not a secret store, not raw data storage, and not a place for unreviewed operational instructions."
  - "Every migration under migrations/database/, migrations/schema/, migrations/data/, or migrations/graph/ must have a corresponding rollback entry here, even when rollback is unsafe and the only approved path is a documented forward fix."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/rollback/` — Rollback and Forward-Fix Records for Migration Governance

> **One-line purpose.** Hold rollback and forward-fix records for KFM migrations so database, schema, data, and graph changes remain inspectable, reviewable, auditable, and recoverable through governed follow-up.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-migrations%2F-blue)
![lane](https://img.shields.io/badge/lane-rollback_records-blueviolet)
![required](https://img.shields.io/badge/rollback_entry-required-red)
![forwardfix](https://img.shields.io/badge/forward_fix-allowed_with_reason-orange)
![secrets](https://img.shields.io/badge/secrets-never_here-red)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Rollback record contract](#rollback-record-contract) · [Required rollback record](#required-rollback-record) · [Decision classes](#decision-classes) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`migrations/rollback/` is the required record lane for migration recovery posture. Every database, schema, data, and graph migration must have a corresponding rollback or forward-fix entry here.

This folder exists because migrations are governed state transitions. They must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A rollback entry does not publish data, approve release state, or replace release rollback cards. It records how a migration can be reversed, why direct reversal is unsafe, or what governed forward-fix path is required.

Use this lane for recovery records only. Primary migrations belong in the sibling migration lane:

- `migrations/database/`
- `migrations/schema/`
- `migrations/data/`
- `migrations/graph/`

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-directory README |
| **Owning responsibility root** | `migrations/` |
| **Subpath role** | `rollback/` — rollback records, forward-fix records, recovery posture notes, review decisions, and post-recovery validation summaries |
| **Authority level** | Draft operational governance. Directory Rules, accepted ADRs, migration records, release runbooks, incident runbooks, policy, and release gates outrank this README. |
| **Lifecycle phase** | n/a — recovery documentation, not lifecycle data itself |
| **Default posture** | Every migration gets a recovery entry; prefer reversible changes; document forward-fix-only with reason; preserve auditability |
| **Owners** | `<migration-steward>`, `<rollback-steward>`, `<release-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Migration steward + affected lane steward for every rollback record; release/security/policy reviewers when public, sensitive, security, or incident impact exists |
| **Directory Rules basis** | `migrations/` includes `rollback/`; every migration must have a corresponding rollback entry, even when rollback is unsafe and forward-fix-only with reason. |

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
    ├── graph/
    └── rollback/      ◀── you are here
        └── README.md
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `migrations/rollback/` | Rollback records, forward-fix records, recovery posture decisions, validation summaries | Primary migrations, release rollback cards, raw data, policy, schemas, publication approvals |
| `migrations/database/` | Database structure migrations | Rollback record authority |
| `migrations/schema/` | Schema/contract migrations | Rollback record authority |
| `migrations/data/` | Data migrations, repairs, and backfills | Rollback record authority |
| `migrations/graph/` | Graph/triplet relationship migrations | Rollback record authority |
| `release/` | Release manifests, public release rollback cards, correction notices | Migration-level rollback records |
| `docs/runbooks/` | Operational runbooks | Per-migration rollback records |
| `policy/` | Allow / deny / restrict / abstain rules | Migration recovery records |
| `schemas/contracts/v1/` | Machine-checkable schemas | Rollback records |
| `contracts/` | Human-readable contract meaning | Rollback records |

[Back to top](#top)

---

## What belongs here

Use `migrations/rollback/` for non-sensitive recovery governance material such as:

- Rollback records paired with migrations in `migrations/database/`, `migrations/schema/`, `migrations/data/`, or `migrations/graph/`.
- Forward-fix-only justifications when direct rollback would be unsafe, lossy, misleading, or not technically valid.
- Recovery decision records explaining whether rollback is reversible, partial, blocked, or forward-fix-only.
- Post-recovery validation summaries.
- Risk summaries for data loss, identity remapping, evidence-link breakage, schema compatibility, graph topology, public API behavior, and release impact.
- References to migration records, issues, backups/snapshots, runbooks, release records, or validation receipts by identifier or path.
- Review notes proving that recovery posture was considered before the migration was accepted.

Accepted file types are Markdown recovery records, sanitized validation summaries, and non-sensitive review notes. Keep records useful for reviewers without storing sensitive operational details.

[Back to top](#top)

---

## What does not belong here

Do **not** use `migrations/rollback/` as a backup store, release rollback-card home, secret store, or operational dump.

The following must not live here:

- Full backups, snapshots, database dumps, graph dumps, raw data, cached extracts, tiles, rasters, generated public artifacts, or bulk lifecycle payloads.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data artifacts.
- Release rollback cards, release manifests, correction notices, publication approvals, or signed release receipts that belong under `release/`.
- Live credentials, database passwords, private endpoints, tokens, API keys, `.env` files, service-account keys, kubeconfigs, or production connection material.
- Unredacted incident details, private host inventories, sensitive logs, or vulnerability working notes.
- Primary database/schema/data/graph migration files that belong in sibling migration lanes.
- Recovery records that silently weaken evidence, policy, review, correction, or release state.

If a backup, secret, production dataset, or sensitive recovery artifact lands here, move it to the correct governed path or secure store and record the correction. If restricted material was exposed, treat it as a security or governance incident.

[Back to top](#top)

---

## Rollback record contract

A rollback record must make recovery posture explicit before a migration is accepted for shared or release-relevant state.

### Required properties

- **Paired migration.** Name the migration this record belongs to.
- **Decision class.** State whether the recovery posture is reversible rollback, partial rollback, forward-fix-only, blocked, or not applicable.
- **Reason.** Explain why that recovery posture is correct.
- **Preconditions.** Identify required prior state, backup/snapshot reference, release freeze, app version, schema version, or review state.
- **Risk analysis.** Name data, identity, evidence, policy, schema, graph, API, and release risks.
- **Validation.** Define how reviewers will know the rollback or forward fix restored a safe state.
- **Audit trail.** Record review and execution summary without exposing secrets or sensitive payloads.
- **Release impact.** State whether public artifacts, API behavior, tiles, exports, or release manifests are affected.
- **Forward fix.** If direct rollback is unsafe, link the corrective migration or issue that carries the fix.
- **No silent authority changes.** Recovery must not silently publish, de-publish, approve, deny, certify, or alter policy without the responsible lane.

### Naming convention

Use the same date prefix and short purpose as the paired migration:

```text
migrations/<lane>/YYYYMMDD-short-purpose.*
migrations/rollback/YYYYMMDD-short-purpose.md
```

Examples:

```text
migrations/database/20260703-add-evidence-ref-index.sql
migrations/rollback/20260703-add-evidence-ref-index.md

migrations/data/20260703-backfill-source-ref-links.py
migrations/rollback/20260703-backfill-source-ref-links.md

migrations/graph/20260703-repair-evidence-ref-edges.py
migrations/rollback/20260703-repair-evidence-ref-edges.md
```

[Back to top](#top)

---

## Required rollback record

Every rollback entry should use this record shape.

```markdown
# <YYYYMMDD-short-purpose> rollback

## Status
PROPOSED / APPROVED / READY / COMPLETED / FAILED / BLOCKED / FORWARD_FIX_ONLY

## Paired migration
<migrations/database|schema|data|graph/YYYYMMDD-short-purpose.*>

## Owner
<rollback owner and affected lane steward>

## Recovery decision
REVERSIBLE_ROLLBACK / PARTIAL_ROLLBACK / FORWARD_FIX_ONLY / BLOCKED / NOT_APPLICABLE

## Reason
<why this recovery posture is correct>

## Preconditions
<required prior state, backup/snapshot reference, release state, app version, schema version, graph/data state, review state>

## Risks
<data loss, identity remap, evidence breakage, policy impact, release impact, downtime, compatibility>

## Recovery posture
<high-level recovery or forward-fix approach; no secrets or sensitive operational details>

## Validation plan
<checks that prove the rollback or forward fix restored a safe state>

## Release impact
<N/A or affected release artifacts/routes/manifests/corrections>

## Incident/security impact
<N/A or link to incident/runbook record>

## Execution summary
<timestamp, operator/tool, commit, workflow id, sanitized result summary>

## Post-recovery verification
<counts, constraints, graph checks, evidence resolution, API compatibility, sample review>

## Follow-up
<corrective migration, docs, release note, drift register, open questions>
```

[Back to top](#top)

---

## Decision classes

| Decision | Meaning | Required handling |
|---|---|---|
| `REVERSIBLE_ROLLBACK` | Migration can be safely returned to prior state | Provide validation plan and paired record |
| `PARTIAL_ROLLBACK` | Only part of the change can be safely reverted | Name unreverted parts and forward-fix path |
| `FORWARD_FIX_ONLY` | Direct rollback is unsafe, lossy, misleading, or invalid | Explain why and link corrective migration or issue |
| `BLOCKED` | Recovery cannot proceed until a condition is met | Name blocker, owner, and next review trigger |
| `NOT_APPLICABLE` | Migration has no persistent effect or is documentation-only | Explain why and provide validation note |

Forward-fix-only is allowed only when explicit, reviewed, and justified. It must not be used to avoid recovery planning.

[Back to top](#top)

---

## Validation

Rollback records require evidence before and after recovery posture is accepted.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Recovery record belongs in `migrations/rollback/` | PR review |
| Paired migration | Record links to one migration or named migration set | Path link |
| Decision class | Recovery posture is explicit | Rollback record |
| Preconditions | Required prior state is named | Precondition note |
| Backup/snapshot | Required backup posture is named for risky changes | Backup reference note |
| Secret scan | No credentials, private endpoints, or sensitive artifacts committed | Secret scan result |
| Risk review | Data, identity, evidence, policy, schema, graph, API, and release risks considered | Risk section |
| Validation plan | Checks prove rollback/forward fix restored safe state | Validation section |
| Release impact | Public artifacts/API/routes reviewed if affected | Release note or N/A |
| Execution summary | Recovery result recorded without sensitive output | Execution summary |
| Post-check | Counts, constraints, evidence links, graph invariants, or API compatibility verified | Verification report |

A rollback record is not ready until reviewers can answer:

1. What migration does it pair with?
2. Can it be safely rolled back?
3. If not, why is forward fix safer?
4. What state must exist before recovery?
5. What could be harmed?
6. What proves recovery worked?
7. Who reviewed it?
8. What public or release state is affected?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no recovery behavior | Docs steward or migration steward |
| Rollback record for database migration | Database steward + migration steward |
| Rollback record for schema migration | Schema steward + migration steward |
| Rollback record for data migration | Data steward + migration steward |
| Rollback record for graph migration | Graph steward + migration steward |
| Rollback affecting public API, map layers, exports, tiles, or published artifacts | Release steward + affected lane steward |
| Rollback involving sensitive or rights-uncertain material | Policy/sensitivity reviewer + affected domain steward |
| Forward-fix-only recovery | Migration steward + affected lane steward + documented risk acceptance |
| Recovery after security or exposure incident | Security owner + incident/runbook owner + affected lane steward |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `migrations/rollback/`.
- [ ] Confirm standard rollback filename convention.
- [ ] Confirm whether rollback records are required in the same PR as the paired migration.
- [ ] Confirm backup/snapshot expectations by migration class.
- [ ] Confirm forward-fix-only approval process.
- [ ] Confirm how recovery summaries are stored or indexed.
- [ ] Confirm validation tooling for recovery verification.
- [ ] Confirm release-steward trigger for public-impacting recovery.
- [ ] Confirm incident-response handoff when recovery follows a security or exposure incident.
- [ ] Confirm whether rollback records should be linked from migration manifests, PR templates, or release gates.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield stub |
| Next review trigger | First rollback record, forward-fix-only record, public-impacting recovery, incident-driven recovery, or paired migration PR |
