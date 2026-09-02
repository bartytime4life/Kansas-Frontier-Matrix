<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-readme
title: migrations/ — Governed State-Change, Compatibility, Adoption, Execution, and Recovery Root
type: README; directory-readme; canonical-migrations-root; change-control-index
version: v1.3
status: draft; repository-grounded; canonical-root; directory-rules-v2-accepted; recursive-inventory-confirmed; placeholder-only-confirmed; five-lane-documentation-confirmed; schema-validation-bounded; rollback-readiness-hold-confirmed; v6-repository-delivery-contract-added; concrete-payloads-unestablished; runner-unestablished; applied-ledger-unestablished; recovery-coverage-unverified; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable migration, database, schema, contract, data, graph, recovery, policy, security, application, domain, and release stewardship plus independent approval remain unestablished
created: 2026-07-03
updated: 2026-08-09
supersedes: v1.2 documentation at the same path; no migration payload, database state, schema, contract, data, graph, recovery action, runtime behavior, release state, or publication state is superseded
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: repository-facing; migrations; change-control; compatibility-aware; adoption-aware; rollback-aware; forward-fix-aware; evidence-first; fail-closed; implementation-forward; non-publisher
current_path: migrations/README.md
owning_root: migrations/
responsibility: govern deliberate transitions in persisted structure, machine compatibility, data state, graph topology, adoption, execution evidence, and recovery posture without becoming semantic-contract, canonical-schema, policy, evidence, lifecycle-data, runtime, release, or publication authority
truth_posture: >
  CONFIRMED same-path target; ADR-0029 acceptance of Directory Rules v2 as current placement authority; full recursive inventory of eleven
  paths under migrations/ at the pinned base; five v1.1 lane READMEs; five explicit 0001_init.placeholder stubs and no concrete executable
  migration payload in that root; CODEOWNERS routing; bounded schema-validation workflow; rollback-drill readiness workflow that explicitly
  holds rather than simulates rollback; and no open pull-request overlap on migrations/README.md at inspection / PROPOSED root migration
  classification, packet, evidence ladder, work-state model, deterministic identity, dependency closure, staged repository delivery, concurrency,
  compatibility, adoption, execution, recovery, and definition-of-done contracts / UNKNOWN active database or graph engines, canonical runner,
  target environments, applied versions, backup and restore capabilities, producer and consumer adoption, execution receipts, recovery outcomes,
  and production history / NEEDS VERIFICATION one-to-one migration-to-recovery pairing, same-PR enforcement, canonical ordering, machine
  migration register, dedicated migration validation, steward assignments, independent approval, branch or ruleset enforcement, rehearsal policy,
  and release integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8f26a3ed8d2fbc2f40fecf722177aeae2cb6297a
  target_prior_blob: 0b7b9cda652ca0ab8da4c1b82261476afa5f8955
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  database_readme_blob: a5d479ce410ead7fb8eb61082f22d8bddc813746
  schema_readme_blob: d4f28ff15ab5e26c101ff72fc96a1f500103dfae
  data_readme_blob: 42350e082436d84f8f2147d53044249eb7daf430
  graph_readme_blob: 92ca1b02a15557cdd970a03ee95a946ec78a0c3f
  rollback_readme_blob: 9fb60b41f9bb901b69d45cb8c4d942b8272b467f
  database_placeholder_blob: 045a4989bdad2d39a6c97adedfb148d7c033b69d
  schema_placeholder_blob: d20ac2b147de449bf5ba1b55e22ad8ddcd44ef25
  data_placeholder_blob: db0319fe09b20b2fb270be5a8382a9afaba4a2c3
  graph_placeholder_blob: 4d89cfda15686b2137df889e60a2173b70ec269b
  rollback_placeholder_blob: bc3c9c0ee6e08cb2bd639a5f329c3065ffba6cb4
  schema_validation_workflow_blob: 3deebb4fa1e5db00108e0b43804ac633083d94c2
  rollback_drill_workflow_blob: 702c141ac1dd59ea0bb865c12e4e81d8a83f99fc
  recursive_path_count: 11
  inspection_method: exact GitHub file and directory reads at the pinned base, complete per-lane contents inspection, accepted-ADR inspection, workflow inspection, open-pull-request overlap inspection, and current-head verification; no live database, graph store, migration runner, backup system, deployment environment, release artifact, runtime trace, or production system was inspected
related:
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/runbooks/ROLLBACK_RUNBOOK.md
  - ../docs/runbooks/README.md
  - ../docs/governance/SEPARATION_OF_DUTIES.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../contracts/README.md
  - ../schemas/README.md
  - ../schemas/contracts/v1/README.md
  - ../policy/README.md
  - ../fixtures/README.md
  - ../tests/README.md
  - ../tools/validators/README.md
  - ../data/README.md
  - ../release/README.md
  - ../release/rollback_cards/README.md
  - ../.github/workflows/schema-validation.yml
  - ../.github/workflows/rollback-drill.yml
  - ./database/README.md
  - ./schema/README.md
  - ./data/README.md
  - ./graph/README.md
  - ./rollback/README.md
  - ../.github/CODEOWNERS
notes:
  - "v1.3 is a same-path documentation-only modernization grounded in current repository evidence and the accepted Directory Rules v2 decision."
  - "The first twelve H2 sections preserve the Directory Rules folder-README contract."
  - "The complete pinned-base migrations/ inventory is eleven paths: this README plus five v1.1 lane READMEs and five non-executable placeholder stubs."
  - "The repository implementation contract governs authoring, branch, validation, and draft-PR delivery; it does not authorize applying a migration to any database, dataset, graph, runtime, release, or public system."
  - "The schema-validation workflow proves bounded machine-shape checks; the rollback-drill workflow proves a deliberate readiness hold and explicitly does not simulate rollback."
  - "Static badges summarize inspected repository state only; they are not migration approval, execution, adoption, recovery, release, or publication proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/` — Governed State-Change, Compatibility, Adoption, Execution, and Recovery Root

> **One-line purpose.** Govern deliberate changes to persisted structure and state so every database, schema, data, graph, and recovery transition is classified, pinned, reviewable, previewable, validated, auditable, and recoverable without bypassing KFM authority, lifecycle, policy, evidence, or release boundaries.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Directory Rules: v2 accepted](https://img.shields.io/badge/directory%20rules-v2%20accepted-2da44e?style=flat-square)](#authority-level)
[![Inventory: 11 paths](https://img.shields.io/badge/inventory-11%20paths-0969da?style=flat-square)](#current-bounded-topology)
[![Payloads: placeholders only](https://img.shields.io/badge/payloads-placeholders%20only-b42318?style=flat-square)](#status)
[![Schema checks: bounded](https://img.shields.io/badge/schema%20checks-bounded-0969da?style=flat-square)](#current-workflow-boundary)
[![Rollback drill: hold](https://img.shields.io/badge/rollback%20drill-readiness%20hold-d4a72c?style=flat-square)](#current-workflow-boundary)
[![Delivery: draft PR ceiling](https://img.shields.io/badge/delivery-draft%20PR%20ceiling-6e7781?style=flat-square)](#staged-admission-and-delivery)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-08-09](https://img.shields.io/badge/reviewed-2026--08--09-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** at the pinned base, `migrations/` contains exactly eleven paths: this root README, five repository-grounded v1.1 lane READMEs, and one explicit `0001_init.placeholder` stub in each lane. The repository also has bounded schema-validation and rollback-readiness workflows. Current evidence does **not** establish an executable migration payload, a canonical migration runner, an active database or graph engine, an applied-version ledger, complete migration-to-recovery pairing, backup and restore capability, producer/consumer adoption, recovery rehearsals, or production execution history.

> [!CAUTION]
> A direct request to edit repository files authorizes scoped feature-branch implementation and review delivery. It does **not** authorize applying a migration to a database, dataset, graph, runtime, release, cache, or public system. Target execution requires its own pinned migration packet, target-specific authorization, safety evidence, and recovery posture.

> [!WARNING]
> `migrations/rollback/` is the engineering-recovery record lane for migrations. It is not a backup store, release rollback-card home, correction register, incident workspace, or publication authority. The current `rollback-drill` workflow is a readiness inspection that explicitly holds; it is not proof that migration rollback or release rollback was simulated.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Task contract](#repository-implementation-task-contract) · [Closure](#dependency-closure-and-review-boundary) · [Delivery](#staged-admission-and-delivery) · [Topology](#current-bounded-topology) · [Routing](#migration-classification-and-lane-routing) · [Packet](#minimum-migration-packet) · [Evidence](#migration-evidence-ladder) · [States](#migration-work-state-model) · [Identity](#deterministic-identity-ordering-and-pairing) · [Coordination](#cross-lane-coordination) · [Compatibility](#compatibility-adoption-and-deprecation) · [Execution](#preflight-dry-run-canary-execution-and-post-checks) · [Recovery](#recovery-and-forward-fix-contract) · [Workflows](#current-workflow-boundary) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

<a id="root-contract"></a>
<a id="migration-lifecycle"></a>
<a id="lane-contracts"></a>
<a id="inputs-and-outputs"></a>
<a id="open-verification"></a>

## Purpose

`migrations/` is KFM's canonical responsibility root for **governed state-change mechanics** affecting:

- database structure and database-managed behavior;
- machine schemas, contract-backed payload compatibility, and adoption;
- data backfills, repairs, remaps, lifecycle-safe relocations, and deterministic rebuilds;
- graph or triplet topology, identity, evidence links, and derived projections;
- rollback, reversal, disablement, restore coordination, compensation, and forward-fix planning.

The root exists because even a small migration can alter object identity, semantic interpretation, evidence closure, policy behavior, lifecycle placement, public API compatibility, map output, release safety, or recovery options.

Every consequential migration must answer:

1. What exact state changes?
2. Why is the change necessary?
3. Which authority defines the intended meaning, shape, policy, evidence, lifecycle state, or release posture?
4. Which immutable base state and target state are involved?
5. Which producers, consumers, validators, datasets, graph families, services, and releases are affected?
6. Which preconditions and invariants must hold?
7. How can the change be previewed, dry-run, rehearsed, or canaried?
8. Which evidence proves the attempted and resulting state?
9. How can the system recover safely?
10. Which residual risks, deprecations, corrections, or follow-up actions remain?
11. Who authored, reviewed, authorized, executed, and verified the transition?
12. What must remain blocked if any required evidence is absent?

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A migration may support a governed transition. It is not itself lifecycle promotion, policy approval, evidence of external truth, release authorization, correction approval, or publication.

## Authority level

**Canonical responsibility root for migration mechanics, coordinated adoption, execution evidence, and engineering recovery planning; subordinate to the authorities that define meaning, shape, admissibility, evidence, lifecycle state, runtime behavior, and release.**

ADR-0029 accepts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) as the single writable human placement authority. The document's embedded `PROPOSED_FOR_ADOPTION` label is retained as part of the adopted byte identity; the accepted ADR supplies the effective adoption decision.

| Question | Controlling authority | `migrations/` relationship |
|---|---|---|
| Where migration materials belong | Accepted Directory Rules and placement ADRs | Owns migration mechanics under the five lanes |
| What an object means | [`contracts/`](../contracts/README.md) | References semantic authority; does not redefine it |
| What machine shape is valid | [`schemas/`](../schemas/README.md) | Coordinates shape transitions; canonical schemas remain under `schemas/` |
| What policy permits | [`policy/`](../policy/README.md) | Carries policy-impact references; does not make policy decisions |
| What source or evidence supports a remap | Source registry, `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Preserves support and records transforms; does not manufacture evidence |
| Which lifecycle phase owns a payload | [`data/`](../data/README.md) | Migrates state without replacing lifecycle ownership |
| How runtime behavior changes | Accepted application, package, runtime, and pipeline roots | Coordinates rollout; does not own runtime implementation |
| How repository work is authored and delivered | Current scoped user instruction, path-scoped rules, accepted doctrine, and repository controls | Allows feature-branch implementation and review delivery within the requested scope |
| How a migration is executed | Selected runner, pinned payload, target environment, runbook, and target-specific authorization | Records execution contract and receipts; repository delivery alone is insufficient |
| How engineering recovery works | [`migrations/rollback/`](./rollback/README.md) plus applicable backup/runbook evidence | Requires paired recovery posture |
| How public release rollback or correction works | [`release/`](../release/README.md), release rollback cards, correction and withdrawal records | References release actions; cannot authorize them |
| Whether a release is approved | Release authority and governed promotion records | Declares impact only |
| Whether a claim is true | Admissible evidence | Never decided by migration success |

### Anti-collapse rules

`migrations/` must not collapse:

- migration mechanics into semantic or schema authority;
- repository implementation authority into target execution authority;
- a script parse into target compatibility;
- a dry run into production execution;
- a branch, commit, pull request, merge, or green check into an applied migration;
- a migration receipt into release approval;
- a rollback document into a rehearsed recovery path;
- a backup reference into proof that a restore is possible;
- an identity remap into evidence that two entities are the same;
- an AI-generated crosswalk into authoritative state;
- a derived rebuild into canonical truth;
- a workflow hold into an implemented migration system;
- CODEOWNERS routing into stewardship or approval;
- documentation quality into operational maturity.

Public clients and normal UI surfaces continue to use governed APIs and released artifacts. They do not read migration packets, internal stores, or canonical state directly.

## Status

### Repository-grounded status matrix

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Directory Rules authority | ADR-0029 is accepted and pins Directory Rules v2 | **CONFIRMED — current placement authority** |
| Root README | v1.2 exists at the same path at the pinned base | **CONFIRMED — documentation; this change proposes v1.3** |
| `database/` lane | v1.1 README plus `0001_init.placeholder` | **CONFIRMED — documented placeholder only; engine, runner, payload, target, and execution unestablished** |
| `schema/` lane | v1.1 README plus `0001_init.placeholder` | **CONFIRMED — documented placeholder only; configured validation exists outside the lane; migration adoption unestablished** |
| `data/` lane | v1.1 README plus `0001_init.placeholder` | **CONFIRMED — documented placeholder only; runner, payload, target dataset, and execution unestablished** |
| `graph/` lane | v1.1 README plus `0001_init.placeholder` | **CONFIRMED — documented placeholder only; graph store, query language, runner, target, and execution unestablished** |
| `rollback/` lane | v1.1 README plus `0001_init.placeholder` | **CONFIRMED — documented placeholder only; pairing, rehearsal, backup capability, and execution unverified** |
| Recursive `migrations/` inventory | Eleven paths at the pinned base | **CONFIRMED — complete repository-root inventory for this snapshot** |
| Schema-validation workflow | Parses and meta-validates schemas, checks configured fixture families, and runs selected schema/contract tests | **CONFIRMED bounded machine-shape validation; not migration adoption or execution proof** |
| Rollback-drill workflow | Inspects rollback readiness and asserts known placeholders/holds | **CONFIRMED readiness hold; no rollback simulated** |
| Concrete executable migration payloads | Five placeholder stubs are the only non-README lane files | **CONFIRMED absent from this root at the pinned base** |
| Canonical migration runner | Not established | **UNKNOWN** |
| Active database or graph engines | Not inspected or established | **UNKNOWN** |
| Applied migration/version ledger | Not established | **NEEDS VERIFICATION** |
| Machine-readable migration register | Not established | **NEEDS VERIFICATION** |
| One-to-one migration/recovery pairing | Required by doctrine; no concrete migration packet exists to pair | **NEEDS VERIFICATION before first executable payload** |
| Same-PR pairing enforcement | Not established | **NEEDS VERIFICATION** |
| Backups, snapshots, restore, or point-in-time recovery | Not inspected | **UNKNOWN** |
| Producer and consumer adoption ledger | Not established | **NEEDS VERIFICATION** |
| Dedicated migration CI | No cross-lane migration packet validator was established | **NEEDS VERIFICATION** |
| Recovery rehearsal history | Not established | **UNKNOWN** |
| Production execution and recovery history | Not inspected or established | **UNKNOWN** |

### Truth labels and work states are separate

- `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION` describe evidence confidence.
- Migration work states describe where a migration packet is in its governed process.
- Validation outcomes describe a named check.
- Repository delivery states describe whether bytes and review surfaces exist.
- Policy, release, correction, and publication states remain separate authorities.

Do not substitute one category for another.

## What belongs here

Use `migrations/` when the primary responsibility is a governed transformation of persisted structure, compatibility, or state.

Accepted material includes:

- root and lane README contracts;
- database, schema, data, and graph migration plans;
- SQL or engine-native migration files when an engine is selected;
- safe, reviewable scripts or query fragments;
- migration manifests that pin payload paths, digests, dependencies, base state, target state, and recovery references;
- schema/contract compatibility and adoption matrices;
- producer and consumer rollout plans;
- data backfill, repair, normalization, remap, relocation, or rebuild plans;
- graph/triplet topology, identity, relationship, evidence-link, and projection migration plans;
- preflight, dry-run, rehearsal, canary, validation, and post-check definitions;
- sanitized execution and adoption summaries;
- migration-level recovery, disablement, restore-coordination, compensation, and forward-fix records;
- cross-lane dependency and cutover coordination;
- drift, deprecation, correction, and documentation follow-up notes;
- references to release-impact review when public behavior may change.

A file belongs here only when **migration mechanics are its primary responsibility**. The normative object, schema, policy, dataset, release record, receipt, proof, or runtime implementation remains in its owning root.

## What does NOT belong here

Do not use `migrations/` as a parallel authority, lifecycle store, backup system, secrets store, incident workspace, release root, or publication surface.

The following do not belong here:

- canonical JSON Schemas, JSON-LD contexts, or other machine-shape authority;
- human semantic contract authority;
- policy bundles or admissibility decisions;
- source descriptors, source payloads, EvidenceBundles, or canonical evidence;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, or rollback data payloads;
- database or graph dumps, bulk exports, backups, snapshots, WAL archives, restore images, or point-in-time recovery media;
- release manifests, promotion decisions, release rollback cards, correction notices, withdrawal notices, or publication approvals;
- production credentials, DSNs, connection strings, tokens, private keys, certificates, kubeconfigs, service-account material, or `.env` files;
- unredacted row samples, private topology, sensitive logs, incident working material, or restricted relationship payloads;
- generated public artifacts such as PMTiles, COGs, GeoParquet, tiles, reports, exports, or API payloads;
- generated clients or runtime code whose primary home is an application or package root;
- destructive commands lacking named scope, preconditions, validation, recovery, review, target, and audit fields;
- one-off manual commands represented as authoritative migration history;
- mutable “latest” inputs without a pinned revision or digest;
- AI-generated remaps, inferred graph edges, entity merges, crosswalks, or transformations promoted without evidence and review;
- migration records that silently weaken evidence, source role, rights, sensitivity, policy, review, correction, or release requirements.

If restricted data, credentials, dumps, backups, or incident material land here, stop normal work, isolate the material, rotate or revoke access where necessary, and follow the applicable security, incident, correction, and governance process.

## Inputs

A migration packet may consume the following only when their identity and authority are explicit.

| Input | Why it is needed | Minimum pinning |
|---|---|---|
| Current implementation task | Establishes the repository outcome and permitted delivery ceiling | Task ID, user request, repository, immutable base, writable manifest, acceptance criteria, delivery target |
| Accepted ADR or explicit scoped decision | Establishes why the architecture or compatibility transition is permitted | ADR ID and accepted revision, or issue/decision reference |
| Semantic contract | Defines intended meaning and invariants | Path, version, commit, and digest where material |
| Machine schema | Defines intended shape | `$id`, path, version, commit, and digest |
| Policy decision or sensitivity review | Constrains handling, transformation, and exposure | Decision/reference ID and applicable scope |
| Issue, defect, validation failure, or correction request | Establishes reason and bounded scope | Stable issue or record reference |
| Source and evidence references | Grounds consequential repairs, remaps, merges, or splits | Resolvable `EvidenceRef`/`EvidenceBundle` or accepted source record |
| Current-state inventory | Defines exact objects, rows, features, fields, nodes, edges, versions, or projections that may change | Immutable state/version identifier |
| Producer and consumer inventory | Defines compatibility and adoption order | Named systems and deployed/configured revisions |
| Fixtures and invariant checks | Defines expected success, failure, denial, abstention, and edge conditions | Versioned fixture and test paths |
| Environment and runner contract | Defines where and how execution is allowed | Named environment, runner version, permissions, and configuration digest |
| Backup, snapshot, or prior artifact reference | Supports recovery where applicable | Immutable external reference; never backup bytes in Git |
| Release and public-surface context | Defines public impact and correction/rollback handoff | Candidate/release IDs and affected surfaces |
| Prior migration and recovery records | Establishes lineage and ordering | Stable migration/recovery IDs and digests |

Inputs must be commit-, version-, hash-, release-, ledger-, or environment-identified where material. “Latest,” “current database,” “all records,” “production,” or “the graph” is not sufficiently precise for a consequential migration.

## Outputs

A migration repository slice may produce:

- reviewed migration and coordination plans;
- pinned migration payloads and checksums;
- compatibility, dependency, and adoption matrices;
- preflight, dry-run, rehearsal, and canary reports;
- target-state, invariant, and affected-object reports;
- execution, adoption, and verification receipts;
- rollback, disablement, restore-coordination, compensation, or forward-fix records;
- deprecation, drift, correction, and documentation updates;
- references to release-impact, incident, or security review;
- residual-risk and follow-up registers;
- a verified feature branch and draft pull request for repository review.

### Output claim boundaries

| Output | What it may prove | What it does not prove |
|---|---|---|
| Migration plan | Intended change, scope, dependencies, and review surface exist | Execution occurred |
| Parsed SQL/script/query | Syntax passed a named parser or checker | Target compatibility, semantics, safety, or authorization |
| Schema/fixture tests | Selected machine-shape behavior passed | Producer/consumer adoption, semantic truth, policy approval, or release |
| Dry run | A preview completed against a named state | Production outcome |
| Rehearsal | The recovery or cutover path was exercised in a named rehearsal context | Universal recovery or production parity |
| Canary | A bounded target subset changed and passed thresholds | Full migration completion |
| Execution receipt | A named runner attempted or completed a pinned action | External truth, policy approval, release, or publication |
| Post-check report | Named invariants passed in a named environment | Universal correctness or absence of undiscovered defects |
| Adoption record | Named producers and consumers were observed at declared revisions | Every downstream consumer migrated |
| Recovery record | Recovery posture and instructions exist | Recovery was rehearsed, executed, or successful |
| Recovery receipt | A named recovery action completed and passed named checks | Release rollback or public correction unless release records also exist |
| Git branch / commit / pull request | Repository bytes and a review surface exist | Migration applied, adopted, approved, released, or published |
| Passing hosted CI | Named repository checks passed against a head revision | Human review, merge, target execution, release, deployment, promotion, or publication |

`migrations/` never publishes KFM data by itself.

## Validation

Validation is **migration-class-, target-, evidence-grade-, and delivery-stage-specific**. A single generic green check is insufficient.

### Validation classes for repository work

| Class | Meaning | Completion effect |
|---|---|---|
| `REQUIRED_CHANGED_AREA` | Repository-native checks for changed Markdown, code, contracts, schemas, fixtures, tests, generators, and direct dependencies | Must pass before `READY_PR`; normally pass before push |
| `REQUIRED_SAFETY` | Secret, rights, sensitivity, policy, destructive-change, workflow, and migration-execution boundary checks | Must pass before affected bytes leave the workspace |
| `REQUIRED_DELIVERY` | Branch, commit parentage, bytes, diff, changed-path, and pull-request identity checks | Must pass for claimed remote delivery |
| `HOSTED_CI` | Required or informative server-side checks | May be `PENDING` on a draft PR; must pass before `READY_PR` when required |
| `OBSERVATIONAL` | External links, optional integrations, unrelated existing status, and unavailable target environments | May remain disclosed as `PENDING`, `UNKNOWN`, `NOT_RUN`, or `NOT_APPLICABLE` |

Repository criterion states are `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, and `UNKNOWN`. Migration execution checks may additionally use `HOLD` and `ERROR` where the operation cannot safely proceed or be evaluated.

### Required packet checks

Every consequential migration should verify:

- correct lane placement and accepted Directory Rules basis;
- stable migration and recovery identities;
- immutable repository base plus immutable target state;
- frozen writable path manifest and direct dependency closure;
- pinned payload paths and digests;
- affected object and environment inventory;
- controlling contract, schema, policy, evidence, lifecycle, and release references;
- dependency, concurrency, and rollout order;
- compatibility and adoption class;
- rights, sensitivity, living-person, DNA, archaeology, rare-species, infrastructure, sovereignty, and restricted-geometry posture where applicable;
- preconditions, failure conditions, abort thresholds, and post-checks;
- secret and restricted-content absence;
- paired rollback, disablement, restore, compensation, or forward-fix posture;
- documentation, deprecation, correction, incident, and release impact;
- review, authorization, execution, and verification records;
- residual risk and follow-up closure.

### Minimum executable evidence by lane

| Lane | Minimum executable evidence when applicable |
|---|---|
| Database | Engine-aware parse or validation, transaction/preflight behavior, lock and downtime assessment, permission review, before/after object checks |
| Schema | Valid and invalid fixtures, meta-schema checks, `$id`/reference checks, producer/consumer compatibility, crosswalk and deprecation tests |
| Data | Deterministic input selection, counts, identity/provenance checks, dry-run diff, lifecycle and sensitivity checks, no-unexpected-loss assertions |
| Graph/triplet | Node/edge/triplet counts, endpoint closure, evidence-link resolution, duplicate/orphan/cycle policy, identity lineage, projection rebuild proof |
| Recovery | Applicability, prerequisites, reversal/disablement/restore/compensation behavior, rehearsal or explicit gap, post-recovery invariants |
| Coordinated | All applicable lane checks plus dependency, cutover, compatibility-window, and failure-isolation evidence |

### Migration validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Applicable checks passed for the named target and revision |
| `FAIL` | One or more required checks failed |
| `HOLD` | Evidence, review, target, tooling, or dependency is incomplete |
| `NOT_APPLICABLE` | Check does not apply and the rationale is explicit and reviewed |
| `NOT_RUN` | Check was not executed; the migration cannot inherit a passing claim from other checks |
| `ERROR` | The validation mechanism could not determine a result |

A check marked `NOT_RUN`, `HOLD`, `ERROR`, `PENDING`, or `UNKNOWN` remains visible. It must not be silently converted into `PASS`.

### Current repository boundary

The repository has bounded validation and readiness workflows, but no verified cross-lane migration packet validator, canonical runner, or applied-state ledger.

Until those surfaces exist and are verified:

- do not advertise a canonical migration command;
- do not execute any `0001_init.placeholder` file;
- do not use the schema-validation workflow as proof that schema migration adoption completed;
- do not use the rollback-drill readiness workflow as proof that any rollback was simulated;
- record lane-specific commands and versions inside each migration packet;
- mark unexecuted checks `NOT_RUN`;
- keep shared or release-relevant execution blocked when required evidence is absent;
- treat manual execution as non-authoritative unless it produces an inspectable receipt tied to the pinned packet.

## Review burden

Review scales with consequence, authority impact, sensitivity, and recoverability—not file extension.

| Change class | Minimum review burden |
|---|---|
| README-only wording with no behavior change | Documentation reviewer or migration reviewer |
| Database structure, index, constraint, view, function, role, permission, extension, or partition | Database owner + migration reviewer + security reviewer when access changes |
| Schema or semantic compatibility transition | Schema owner + contract owner + affected producer and consumer owners |
| Validator behavior or fixture polarity change | Schema/contract owner + validator/test owner + affected consumers |
| Data backfill, repair, remap, merge, split, relocation, or rebuild | Data owner + affected domain owner + evidence/policy reviewer when material |
| Graph/triplet identity, relationship, evidence-link, or topology change | Graph owner + evidence owner + affected domain owner |
| Recovery record | Affected lane owner + recovery reviewer; independent reviewer where risk is material |
| Public API, MapLibre layer, tile, export, story, search, AI, or released-artifact impact | Governed interface owner + release reviewer + affected domain owner |
| Rights, living-person, DNA/genomic, archaeology, rare-species, infrastructure, sovereignty, or restricted geometry | Policy/sensitivity reviewer + affected domain or rights-holder review |
| Credentials, grants, private endpoints, access, or incident recovery | Security reviewer + affected system owner |
| Destructive, irreversible, or forward-fix-only transition | Migration owner + every affected authority + explicit risk acceptance |
| Cross-lane or multi-environment cutover | Owners for every primary lane, environment, and public surface |
| Change to migration identity, ordering, packet schema, or root authority | ADR-class architecture and governance review |

CODEOWNERS routing is not proof that the required review occurred. For material migrations, authoring, authorization, execution, and verification should be separated when repository maturity supports it.

## Related folders

| Location | Relationship |
|---|---|
| [`database/`](./database/README.md) | Database structure, access, and engine-managed behavior |
| [`schema/`](./schema/README.md) | Machine-shape, semantic-compatibility, validation, adoption, and deprecation transitions |
| [`data/`](./data/README.md) | Data-state backfills, repairs, remaps, relocations, and deterministic rebuilds |
| [`graph/`](./graph/README.md) | Graph/triplet topology, identity, evidence links, relationship vocabulary, and projections |
| [`rollback/`](./rollback/README.md) | Migration-level reversal, disablement, restore coordination, compensation, and forward-fix records |
| [`../contracts/`](../contracts/README.md) | Semantic meaning and invariants |
| [`../schemas/`](../schemas/README.md) | Machine-checkable shape |
| [`../policy/`](../policy/README.md) | Admissibility, rights, sensitivity, access, and obligations |
| [`../fixtures/`](../fixtures/README.md) | Representative valid, invalid, edge, and denial cases |
| [`../tests/`](../tests/README.md) | Executable enforceability and regression evidence |
| [`../tools/validators/`](../tools/validators/README.md) | Reusable validator implementation |
| [`../data/`](../data/README.md) | Lifecycle payloads, receipts, proofs, catalogs, and published artifacts |
| [`../release/`](../release/README.md) | Release, correction, withdrawal, and public rollback decisions |
| [`../release/rollback_cards/`](../release/rollback_cards/README.md) | Release-facing rollback review aids; distinct from migration recovery |
| [`../docs/runbooks/`](../docs/runbooks/README.md) | Operator procedures and drills |
| [`../docs/governance/SEPARATION_OF_DUTIES.md`](../docs/governance/SEPARATION_OF_DUTIES.md) | Review and duty-separation guidance |
| [`../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted Directory Rules v2 adoption decision |
| [`../.github/workflows/schema-validation.yml`](../.github/workflows/schema-validation.yml) | Bounded schema/fixture/test validation |
| [`../.github/workflows/rollback-drill.yml`](../.github/workflows/rollback-drill.yml) | Readiness hold for rollback surfaces; no migration rollback simulation |
| [`../.github/CODEOWNERS`](../.github/CODEOWNERS) | GitHub review routing only |

## ADRs

A migration does not always require an ADR. An ADR is required when the transition:

- adds, removes, or renames a canonical responsibility root;
- creates, retires, or redirects a parallel schema, contract, policy, source, registry, receipt, proof, release, or lifecycle authority;
- changes canonical schema-home, semantic/machine-shape split, or policy-home rules;
- changes the trust membrane or normal public access path;
- splits, merges, or redefines a lifecycle phase;
- standardizes repo-wide migration identity, ordering, state, packet, receipt, or recovery contracts;
- changes the authority of a register or applied-version ledger;
- introduces a non-reversible architectural choice whose tradeoffs must persist;
- intentionally bends a KFM invariant;
- changes the sole-renderer, governed API, publication, or correction boundary.

A migration record may implement an accepted decision. It cannot make its own proposed ADR accepted.

This README update is a same-path documentation change. It does not create a path, alter responsibility ownership, change normative policy, standardize machine shape, or authorize migration execution, so it does not require a new ADR.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-09 UTC |
| Review status | Repository-grounded v1.3 documentation modernization |
| Base | `main@8f26a3ed8d2fbc2f40fecf722177aeae2cb6297a` |
| Placement authority | Directory Rules v2 accepted by ADR-0029 |
| Current maturity | Five v1.1 documented lanes; five explicit placeholder stubs; bounded schema validation; rollback readiness hold; payloads, runner, applied ledger, pairing enforcement, rehearsals, and production history unestablished |
| Next review trigger | First concrete migration payload, runner selection, machine migration register, applied ledger, verified same-PR pairing, recovery rehearsal, destructive transition, or public-impacting migration |

---

## Repository implementation task contract

A direct current request to build, update, fix, create, migrate, push, or open a pull request activates scoped repository implementation. Before the first commit, record the task contract below. This contract governs **repository authoring and delivery**. It does not replace the target-specific migration packet required before a database, schema, data, graph, or recovery action executes.

| Field | Required content |
|---|---|
| `task_id` | Stable scope-derived or user-supplied identifier |
| `goal` | Observable outcome in one or two sentences |
| `repository` | Exact host and owner/repository |
| `base` | Ref plus immutable commit/tree |
| `profile` | Narrowest profile that can satisfy the request |
| `operation` | Canonical operation such as `MODERNIZE_MARKDOWN`, `IMPLEMENT_REPOSITORY_SLICE`, or `MIGRATE_STRUCTURE` |
| `user_intent` | `META`, `READ_ONLY`, `DRAFT`, `IMPLEMENT`, or `IMPLEMENT_AND_READY` |
| `authority_reference` | Normally `CURRENT_USER_REQUEST`, bounded by enforced controls and accepted doctrine |
| `delivery_target` | `ARTIFACT_ONLY`, `WORKSPACE_PATCH`, `PUSHED_BRANCH`, `DRAFT_PR`, or explicitly authorized `READY_PR` |
| `target_selectors` | Paths, issue, component, criteria, or discovery selector |
| `writable_manifest` | Exact intended paths before commit; identify generated outputs separately |
| `in_scope` | Required implementation and direct dependency closure |
| `non_goals` | Explicit exclusions, including execution, release, deployment, promotion, publication, and settings changes unless separately governed |
| `acceptance_criteria` | Observable functional, structural, documentation, and safety outcomes |
| `validation_plan` | Changed-area, safety, delivery, hosted, and observational checks |
| `stop_conditions` | Concrete conditions requiring narrowing, blocking, or a user/steward decision |
| `rollback` | Branch abandonment, revert, forward-fix, compatibility, and correction boundary |

### Repository delivery states

| Delivery state | What it proves | What it never proves by itself |
|---|---|---|
| `ARTIFACT_ONLY` | Complete uncommitted artifact or patch exists | Repository mutation or target execution |
| `WORKSPACE_PATCH` | Local repository state contains the reviewed change | Remote branch, PR, target execution, or release |
| `PUSHED_BRANCH` | Remote feature branch and commits exist | Human review, merge, migration execution, or publication |
| `DRAFT_PR` | Open draft review surface exists | Required hosted CI, approval, merge, migration execution, release, or publication |
| `READY_PR` | Explicitly requested ready-for-review state and required checks passed | Approval, merge, target execution, release, or publication |

The autonomous ceiling for ordinary repository work is one verified `DRAFT_PR`. A current explicit request may raise the ceiling to `READY_PR`. No repository-delivery state authorizes a live migration.

## Dependency closure and review boundary

The smallest valid repository slice is the smallest set that satisfies one observable acceptance boundary without leaving changed behavior undocumented, unvalidated, schema-inconsistent, generator-inconsistent, or operationally broken.

Direct dependency closure may include:

- canonical source plus synchronized generated outputs;
- semantic contract, machine schema, policy, validator, fixtures, and tests that describe the same changed behavior;
- migration plan, paired recovery record, compatibility matrix, and rollout notes;
- navigation, indexes, stable anchors, and direct references;
- configuration, workflow, or manifest changes required to run the changed-area checks;
- repository-required authoring receipts when current doctrine requires them.

It does not include adjacent cleanup merely because budget remains.

### Review-boundary rule

One slice should have:

1. one observable outcome;
2. one primary responsibility owner;
3. one coherent validation story;
4. one rollback boundary;
5. a frozen writable manifest before commit.

Split work when outcomes are independent, rollback boundaries are incompatible, responsibility roots are unrelated, or a governance proposal must be adopted before dependent implementation. A confirmed required consumer must be included, isolated into a dependency-ordered pull request, or named as a blocker. Unknown optional consumers become disclosed follow-up work.

### Change classes

| Class | Meaning | Migration implication |
|---|---|---|
| `EDITORIAL` | Wording or presentation only | No target state change |
| `ADDITIVE` | Backward-compatible capability or documentation | Preserve compatibility and add tests where behavior changes |
| `BEHAVIORAL` | Current behavior changes | Require representative positive/negative validation and recovery analysis |
| `STRUCTURAL` | Files, ownership, generation, or dependency topology change | Apply full Directory Rules and migration review |
| `AUTHORITY_CHANGING` | Governance, policy meaning, normative contracts, or responsibility boundaries change | Isolate the governance decision; do not use an unaccepted change to authorize dependents |

## Staged admission and delivery

Admission is proportional to the next mutation stage.

### Stage A — discovery and drafting

- resolve repository, current base, target role, and governing instructions;
- read the complete target and direct governing evidence;
- classify canonical, generated, mirror, compatibility, or proposed status;
- inspect active branches and pull requests for overlap;
- define goal, acceptance criteria, non-goals, validation, and rollback.

### Stage B — local repository mutation

Before editing tracked state:

- pin the base commit and target blob;
- freeze the initial writable manifest;
- preserve unrelated work, modes, line endings, stable anchors, and document identity;
- identify secrets, rights, sensitivity, destructive, workflow, and external-side-effect risks;
- establish a safe abandonment or restore path.

### Stage C — commit and push

Before commit or push:

- re-read target blobs if main or the task branch moved;
- reconcile active pull-request and branch overlap;
- complete required changed-area and safety validation, or prominently disclose a permitted draft-only environmental limitation;
- inspect triggered workflows for deployment, release, publication, elevated permission, secret, or self-hosted-execution risk;
- confirm the exact diff and absence of unrelated changes;
- use a feature branch and non-force push.

### Stage D — pull-request delivery

Before declaring delivery complete:

- verify branch head and parentage;
- verify the complete base-to-head diff and exact changed paths;
- read back consequential remote bytes or hashes;
- verify pull-request base, head, open state, draft/ready state, and task identity;
- preserve unrelated human metadata when updating an existing pull request;
- report hosted checks as `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, or `UNKNOWN`.

### Concurrency and overlap

- use one writer per branch and overlapping path claim;
- rebase or repin only when drift intersects target bytes, governing evidence, direct dependencies, generator inputs, navigation, or validation configuration;
- reuse a verified task pull request only when its scope and ownership match;
- stop on unresolved same-byte conflict, contradictory semantic authority, or active human edits that cannot be preserved;
- never use last-writer-wins or force-push.

### Hard blockers

Block only the affected stage or slice when there is a concrete failure such as:

- unresolved repository identity or remote mapping;
- absent authority for the requested mutation;
- a generated or mirrored target with no writable canonical source;
- placement that creates parallel authority;
- unresolved same-byte or semantic conflict;
- likely secret, privacy, rights, sensitivity, or harmful-precision exposure;
- unbounded or irreversible destructive action;
- untrusted code requiring secrets, elevated permission, or unrestricted network;
- triggered automation that deploys, releases, promotes, publishes, mutates administration, or exposes secrets;
- inability to validate or recover a high-risk behavioral or authority-changing change.

An `UNKNOWN` value blocks only when the missing fact is necessary for the next action to be safe or materially correct.

### Terminal boundaries

Normal repository implementation never infers or performs:

- direct default-branch writes;
- force-push or shared-history rewrite;
- pull-request approval, merge, or auto-merge;
- target migration execution against a live or shared environment;
- release, deployment, promotion, publication, or cache/alias mutation;
- repository visibility, ruleset, branch-protection, environment, secret, app, permission, or settings changes;
- activation of live connectors or external publishing systems.

## Current bounded topology

The complete pinned-base topology is:

```text
migrations/
├── README.md
├── database/
│   ├── 0001_init.placeholder
│   └── README.md        # v1.1
├── schema/
│   ├── 0001_init.placeholder
│   └── README.md        # v1.1
├── data/
│   ├── 0001_init.placeholder
│   └── README.md        # v1.1
├── graph/
│   ├── 0001_init.placeholder
│   └── README.md        # v1.1
└── rollback/
    ├── 0001_init.placeholder
    └── README.md        # v1.1
```

The five placeholder files are explicit greenfield markers. They are not executable payloads, ordering authority, applied-state evidence, or proof that a runner exists.

### Lane maturity matrix

| Lane | Confirmed documentation | Confirmed implementation evidence | Unestablished or unverified |
|---|---|---|---|
| `database/` | v1.1 repository-grounded contract | One non-executable placeholder stub | Engine, version, runner, objects, payloads, targets, backups, executions |
| `schema/` | v1.1 repository-grounded contract | One non-executable placeholder; configured schema-validation surface outside this lane | Concrete migration payloads, adoption ledger, generated clients, compatibility retirement, release adoption |
| `data/` | v1.1 repository-grounded contract | One non-executable placeholder stub | Runner, payloads, target datasets, executions, restores |
| `graph/` | v1.1 repository-grounded contract | One non-executable placeholder stub | Graph store, query language, runner, payloads, targets, executions |
| `rollback/` | v1.1 repository-grounded recovery contract | One non-executable placeholder; readiness workflow outside this lane does not simulate recovery | Pairing coverage, runner, backup capability, rehearsals, executions, production outcomes |

## Migration classification and lane routing

Classify by the **primary state transition**, not by file language or storage technology.

| Primary change | Primary lane | Common adjacent responsibilities |
|---|---|---|
| Table, column, index, constraint, view, function, trigger, role, grant, extension, partition, storage behavior | `database/` | Schema, app/runtime, data, security, release |
| Field, enum, requiredness, type, `$id`, `$ref`, version, validation behavior, producer/consumer compatibility | `schema/` | Contracts, validators, fixtures, generated clients, data, graph, API |
| Record values, identifiers, crosswalks, lifecycle-safe location, repair, backfill, rebuild | `data/` | Database, schema, evidence, policy, release |
| Node/edge/triplet identity, relationship vocabulary, topology, evidence link, projection, graph index | `graph/` | Data, contracts, schemas, evidence, policy, API |
| Reversal, disablement, restore coordination, compensation, forward fix | `rollback/` | Paired primary migration and relevant runbooks |
| Multiple equally primary changes | Coordinated records in each owning lane | One umbrella coordination section or issue may link the packet set |

### Routing questions

Before choosing a lane, ask:

1. Is the durable change primarily to storage structure, machine shape, data values, relationship topology, or recovery posture?
2. Which authority owns the intended meaning and shape?
3. Does the change require a second lane record rather than a larger mixed-responsibility file?
4. Can each lane be reviewed, applied, validated, and recovered independently?
5. Which sequence prevents partial adoption or authority drift?

Do not place all coordinated work into one lane merely because one tool can execute it.

## Minimum migration packet

A shared-state or release-relevant migration should have a complete packet before target execution.

```yaml
migration_id: mig-<stable-id>
title: <short-purpose>
status: PROPOSED
primary_lane: database | schema | data | graph
coordination_id: null
owner: NEEDS_VERIFICATION

repository_change:
  task_id: <stable-task-id>
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: <sha>
  branch: <feature-branch>
  commit: null
  pull_request: null
  delivery_target: DRAFT_PR
  writable_manifest: []

authority:
  user_request_ref: CURRENT_USER_REQUEST
  decision_refs: []
  contract_refs: []
  schema_refs: []
  policy_refs: []
  evidence_refs: []
  release_refs: []

base_state:
  repository_commit: <sha>
  environment: <named-environment>
  state_id: <immutable-version-or-ledger-ref>
  observed_at: <timestamp>
  inventory_ref: <path-or-external-ref>

target_state:
  description: <bounded-intended-state>
  state_id: <planned-version-or-ledger-ref>
  invariants: []

payloads:
  - path: <migration-payload>
    sha256: <digest>
    runner: <runner-and-version>

dependencies:
  before: []
  after: []
  conflicts_with: []

affected:
  database_objects: []
  schemas: []
  contracts: []
  policies: []
  datasets: []
  graph_families: []
  producers: []
  consumers: []
  validators: []
  fixtures: []
  APIs: []
  UI_or_MapLibre_surfaces: []
  releases: []

compatibility:
  class: backward-compatible | expand-contract | staged-breaking | rebuildable-derivative | destructive | forward-fix-only
  coexistence_window: null
  adoption_requirements: []
  deprecation_requirements: []

preconditions: []
abort_conditions: []
dry_run:
  command_or_workflow: NEEDS_VERIFICATION
  target: <named-target>
  evidence_ref: null
canary:
  applicable: false
  scope: null
  thresholds: []

validation:
  changed_area: []
  safety: []
  delivery: []
  hosted_ci: []
  observational: []
  pre_checks: []
  post_checks: []
  negative_checks: []
  expected_outcomes: []

sensitivity:
  impact: none | reviewed | hold
  reviewer_refs: []
release_impact: none | internal | candidate | public

recovery:
  recovery_id: rec-<stable-id>
  record_ref: migrations/rollback/<paired-id>.md
  class: reversible | disableable | restorable | compensating | forward-fix-only
  rehearsal_ref: null

execution:
  authorization_refs: []
  runner: NEEDS_VERIFICATION
  target: <named-environment>
  started_at: null
  completed_at: null
  receipt_ref: null

review:
  required_roles: []
  records: []
  independent_verifier: null

follow_up:
  documentation: []
  deprecations: []
  corrections: []
  incidents: []
  open_risks: []
```

This is a **PROPOSED documentation contract**, not a verified repository schema. Standardizing it as machine shape requires an accepted authority decision, a canonical home under `schemas/`, valid and invalid fixtures, tests, validators, compatibility planning, and rollback.

## Migration evidence ladder

Use the highest evidence grade actually supported. Do not inherit a higher grade from an unrelated workflow.

| Evidence grade | Minimum support | Claim permitted |
|---|---|---|
| `DOCUMENTED` | Plan and packet exist | Intended migration is described |
| `STATIC_VALIDATED` | Payload parses or passes static checks | Selected static properties passed |
| `DRY_RUN` | Preview completed against a pinned target state | Expected diff was observed in that context |
| `REHEARSED` | Full procedure or recovery path exercised in a rehearsal target | Procedure worked in the named rehearsal context |
| `CANARIED` | Bounded subset executed and passed thresholds | Canary succeeded for the named subset |
| `EXECUTED` | Pinned payload ran against the named target | Execution occurred |
| `POSTCHECKED` | Required post-checks ran | Named invariants were evaluated |
| `VERIFIED` | Execution and required post-checks passed with inspectable evidence | Migration reached its verified target state |
| `ADOPTED` | Required producers and consumers were observed on compatible revisions | Named adoption scope closed |
| `RECOVERED` | Recovery action executed and post-recovery checks passed | Named safe state was restored or compensated |
| `COMPLETED` | Adoption, receipts, recovery posture, docs, deprecations, and follow-up closed | Migration packet is operationally closed |

A `DOCUMENTED` or `STATIC_VALIDATED` migration must never be described as executed. A `VERIFIED` migration must not be described as released unless release authority separately approved the affected public state.

## Migration work-state model

Keep migration work state separate from evidence grade, validation outcome, repository delivery state, policy outcome, release state, and truth labels.

| Work state | Meaning |
|---|---|
| `PROPOSED` | Packet exists; target execution is not authorized |
| `DRAFTING` | Scope or packet fields remain incomplete |
| `REVIEW_READY` | Applicable packet, dependencies, checks, and recovery record are complete |
| `APPROVED_FOR_TARGET` | Required review and authorization exist for one named target |
| `PRECHECKED` | Preconditions and required preflight evidence passed |
| `EXECUTING` | Runner is applying the pinned payload |
| `APPLIED` | Payload completed; post-checks and adoption may remain |
| `VERIFYING` | Post-checks are in progress |
| `VERIFIED` | Required post-checks passed for the named target |
| `ADOPTING` | Producers, consumers, aliases, or derivatives are transitioning |
| `COMPLETED` | Applicable adoption, receipts, docs, deprecations, and follow-up are closed |
| `BLOCKED` | Named prerequisite, evidence, review, target, or tool is unresolved |
| `FAILED` | Execution or verification failed |
| `RECOVERY_REQUIRED` | The migration cannot safely continue without recovery |
| `ROLLED_BACK` | Prior safe state was restored or the migration was disabled |
| `FORWARD_FIXED` | A compensating migration restored safety because reversal was unsafe |
| `SUPERSEDED` | A later governed packet replaces this packet |
| `CANCELLED` | Execution authorization was withdrawn before completion |

These states are **PROPOSED** until standardized by an accepted contract. They must not be confused with repository delivery states, `PASS / FAIL / HOLD`, policy decisions, `ANSWER / ABSTAIN / DENY / ERROR`, release states, or `CONFIRMED / PROPOSED / UNKNOWN / NEEDS VERIFICATION`.

## Deterministic identity, ordering, and pairing

### Stable identity

A migration ID should be deterministic from stable inputs where practical, such as:

- primary lane;
- object family or bounded target;
- purpose slug;
- authored sequence or timestamp;
- immutable packet digest.

The repository has not established a canonical ID grammar. Until it does:

- use a unique, human-readable date or sequence prefix;
- keep the same identity across plan, payload, receipt, and recovery record;
- never reuse an ID for a different state transition;
- retain supersession lineage;
- record payload digests independently of filenames.

### Ordering

A migration must declare:

- strict predecessors;
- strict successors;
- compatible parallel work;
- conflicts and mutual exclusions;
- schema/data/graph/database coordination;
- application deploy or feature-flag boundaries;
- release freeze or cutover requirements.

Do not infer order solely from filenames when dependencies are materially important.

### Recovery pairing

Every consequential database, schema, data, or graph migration requires a paired recovery record under `migrations/rollback/`, even when the only acceptable posture is forward-fix-only.

Pairing should be machine-checkable in the future. Current one-to-one coverage and same-PR enforcement remain **NEEDS VERIFICATION**.

## Cross-lane coordination

A coordinated transition uses multiple lane records when more than one responsibility changes materially.

### Coordination matrix

| Concern | Owning lane/root | Coordination requirement |
|---|---|---|
| Storage structure | `migrations/database/` | Pin DDL/object changes and lock/access behavior |
| Machine shape and compatibility | `migrations/schema/` + `schemas/` | Pin old/new schemas, validators, fixtures, and adoption |
| Data values and identity | `migrations/data/` + `data/` | Pin inputs, transforms, lineage, counts, and lifecycle state |
| Graph/triplet topology | `migrations/graph/` + graph/evidence authorities | Pin relationships, evidence links, identity, and projections |
| Recovery posture | `migrations/rollback/` | Pair each primary migration and define coordinated failure handling |
| Runtime adoption | applications/packages/runtime | Pin deploy order, dual-read/write behavior, and rollback compatibility |
| Policy and sensitivity | `policy/` and governed review | Re-evaluate if fields, exposure, identity, or location change |
| Release/public state | `release/` | Hold, correct, withdraw, or release through governed records |

### Coordinated transition example

```mermaid
flowchart LR
    A[Accepted decision and pinned base state]
    B[Database expand]
    C[Schema-compatible version]
    D[Dual-read/write runtime]
    E[Data backfill or graph rebuild]
    F[Verification and consumer adoption]
    G[Contract old path]
    H[Release or public correction]
    R[Paired recovery records]

    A --> B --> C --> D --> E --> F --> G --> H
    B -. paired .-> R
    C -. paired .-> R
    E -. paired .-> R
    G -. paired .-> R
```

If a coordinated sequence partially fails, each lane must declare whether it can stop, reverse, remain compatible, or requires a forward fix.

## Compatibility, adoption, and deprecation

Migration safety often depends more on coexistence and adoption than on payload syntax.

### Compatibility classes

| Class | Requirement |
|---|---|
| `BACKWARD_COMPATIBLE` | Existing consumers continue to function with the new state |
| `FORWARD_COMPATIBLE` | New consumers can tolerate the old state during rollout |
| `EXPAND_AND_CONTRACT` | Add compatible state, migrate adoption, then retire old state |
| `STAGED_BREAKING` | Explicit compatibility window, coordinated cutover, and recovery plan |
| `REBUILDABLE_DERIVATIVE` | Canonical inputs remain and derived state can be deterministically rebuilt |
| `DESTRUCTIVE` | Data, identity, meaning, or recoverability may be lost; heightened governance required |
| `FORWARD_FIX_ONLY` | Reversal would be less safe than compensation; reason and guardrails required |
| `DOCUMENTATION_ONLY` | No payload, machine shape, data, graph, runtime, or release behavior changes |

### Adoption states

Track each material producer and consumer separately:

| Adoption state | Meaning |
|---|---|
| `NOT_ASSESSED` | Impact has not been evaluated |
| `UNAFFECTED` | Reviewed and not affected |
| `PLANNED` | Change is assigned and sequenced |
| `COMPATIBLE_OLD` | Still on old behavior but remains compatible |
| `DUAL_MODE` | Supports old and new state |
| `MIGRATED` | New behavior is deployed or configured |
| `VERIFIED` | Observed against the target state |
| `BLOCKED` | Cannot adopt due to a named dependency |
| `RETIRED` | Old consumer or producer is removed |
| `UNKNOWN` | Adoption state is not evidenced |

### Expand-and-contract sequence

```text
EXPAND -> DUAL COMPATIBILITY -> BACKFILL/REBUILD -> VERIFY -> CUT OVER -> RETIRE -> CLOSE
```

The contract step must not occur until:

- all required producers and consumers are verified;
- deprecated fields, tables, relationships, aliases, or paths have no unresolved dependents;
- recovery remains valid through the compatibility window;
- release and public caches are handled where applicable;
- deprecation and supersession records are updated.

## Preflight, dry-run, canary, execution, and post-checks

### Preflight

Before repository mutation, complete the task-contract and staged-admission checks above. Before target mutation, additionally verify:

- the migration ID, packet digest, payload digest, and repository revision;
- target environment and immutable base-state identity;
- runner and engine version;
- required permissions and least privilege;
- active locks, concurrent deployments, conflicting migrations, and maintenance windows;
- backup/snapshot applicability and external reference validity;
- producer/consumer compatibility window;
- policy, rights, sensitivity, and release holds;
- expected affected counts or object inventory;
- recovery record and abort conditions;
- logging, receipt, and redaction posture.

### Dry run

A dry run should produce:

- exact target and base-state identifiers;
- deterministic affected-object counts;
- proposed changes by class;
- identity merges, splits, remaps, or deletions;
- evidence/provenance changes;
- compatibility warnings;
- sensitivity and public-impact warnings;
- expected invariant changes;
- predicted runtime and lock/downtime risk;
- an explicit no-write assertion;
- sanitized evidence suitable for review.

### Canary

Use a canary only when:

- the subset is representative and policy-safe;
- rollback or disablement is possible for the subset;
- success and abort thresholds are explicit;
- no partial public exposure bypasses release governance;
- canary identity and results are recorded.

### Execution

Execution must use:

- the reviewed packet and exact payload digests;
- the authorized named target;
- the declared runner and configuration;
- concurrency and lock controls;
- bounded privileges;
- structured progress and failure recording;
- no hidden manual edits;
- an execution receipt.

### Post-checks

Post-checks must verify applicable:

- state/version and object counts;
- schema and contract compatibility;
- data identity, provenance, lifecycle, temporal, and spatial invariants;
- graph endpoint closure, relationship rules, evidence links, and projection rebuilds;
- runtime producer/consumer compatibility;
- policy, sensitivity, and rights posture;
- public API, MapLibre, export, search, story, and AI surface behavior;
- release, cache, alias, and correction implications;
- no unexpected loss or orphaned state;
- recovery applicability after the migration.

A migration remains `APPLIED`, not `VERIFIED`, until required post-checks pass.

## Recovery and forward-fix contract

Every consequential migration must identify one recovery class.

| Recovery class | Meaning |
|---|---|
| `REVERSIBLE` | A tested reversal can restore the prior approved state |
| `DISABLEABLE` | New behavior can be turned off while state remains |
| `RESTORABLE` | Backup, snapshot, prior artifact, or point-in-time restore is the recovery path |
| `COMPENSATING` | A governed corrective migration repairs state |
| `PARTIAL` | Only part of the transition can safely reverse; remaining state needs explicit handling |
| `FORWARD_FIX_ONLY` | Reversal is unsafe; an explicit compensating path is the approved option |
| `BLOCKED` | Recovery cannot proceed until a named dependency is satisfied |
| `NON_RECOVERABLE` | Not acceptable for shared or release-relevant state absent exceptional documented governance |

A paired recovery record should include:

- migration ID, payload digest, and coordination ID;
- recovery ID and class;
- target environment and base/safe state;
- activation conditions and decision authority;
- required backup, snapshot, prior artifact, or compensating input references;
- reversal, disablement, restore, compensation, or forward-fix steps;
- irreversible effects and expected residual state;
- database, schema, data, graph, runtime, cache, alias, and release impacts;
- pre- and post-recovery checks;
- operator, reviewer, and independent verifier requirements;
- rehearsal evidence or explicit `NOT_RUN`;
- execution and verification receipts;
- correction, incident, security, or release handoffs.

### Repository rollback versus migration recovery versus release rollback

| Concern | Repository change rollback | Migration recovery | Release rollback |
|---|---|---|---|
| Primary home | Feature branch / pull request / Git history | `migrations/rollback/` | `release/` and release rollback-card/runbook surfaces |
| Purpose | Abandon or revert repository bytes | Restore or compensate internal structure/state after target execution | Withdraw, supersede, or restore governed public release state |
| Normal pre-merge action | Close or abandon the unmerged branch/PR; remote deletion needs separate authority | Not applicable unless target execution already occurred | Not applicable unless release state changed |
| Normal post-merge action | Transparent revert or forward-fix PR; never rewrite shared history | Reversal, disablement, restore, compensation, or forward fix with receipts | Governed rollback, correction, withdrawal, alias/cache handling |
| Evidence | Base/head, commit, diff, validation, PR state | Recovery packet, runner receipt, post-recovery checks | Release decision, rollback card, manifest, correction/withdrawal records |
| Publication effect | None by itself | None by itself | May change public state when approved and executed |

One change may require all three processes. Completing one never implies completion of the others.

## Current workflow boundary

### `schema-validation`

The current schema workflow:

- parses JSON under `schemas/`;
- meta-validates `*.schema.json`;
- requires canonical v1 schemas to declare Draft 2020-12 and unique `$id` values;
- checks eight configured fixture-backed validator families;
- runs selected schema and contract tests;
- emits process output and a job summary only.

It does **not**:

- create or apply a schema migration;
- prove producer or consumer adoption;
- emit a migration receipt or adoption ledger;
- establish semantic truth, policy approval, release, or publication.

### `rollback-drill`

The current rollback workflow:

- inspects rollback-card, placeholder engine/helper, test-inventory, fixture, validator, and published-alias readiness surfaces;
- asserts that known placeholders and holds remain explicit;
- emits inspection output and job summaries only.

It explicitly keeps placeholder and readiness boundaries visible. It does not create a rollback target, execute migration recovery, mutate an alias or cache, issue a release transition, or publish.

Therefore, a passing `rollback-drill` check means **the declared readiness contract passed for that revision**, not that migration recovery or release rollback was simulated.

### Workflow-trigger preflight

Before pushing a migration-related branch, inspect workflows triggered by the changed paths. Ordinary read-only pull-request checks are expected. Block or narrow when a workflow would:

- automatically release, deploy, promote, publish, or execute a target migration;
- give untrusted code secrets or elevated write permissions;
- use unsafe `pull_request_target`, `workflow_run`, or unrestricted self-hosted execution;
- mutate repository administration, settings, environments, or secrets;
- create external side effects outside the authorized scope.

## Definition of done

Repository delivery and migration execution have separate completion criteria.

### Repository change delivery is complete when

- [ ] Repository, immutable base, feature branch, head, and delivery identity are verified.
- [ ] The exact writable manifest and base-to-head changed paths match the task contract.
- [ ] Direct dependency closure is complete and no unrelated changes are present.
- [ ] Changed-area and safety checks pass, or a permitted non-safety draft limitation is explicit.
- [ ] Consequential remote bytes or hashes match the prepared artifact.
- [ ] Pull-request base, head, open state, and draft/ready state are verified.
- [ ] Hosted CI is reported accurately as `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, or `UNKNOWN`.
- [ ] No target execution, merge, release, deployment, promotion, publication, or settings change is falsely claimed.
- [ ] Repository rollback is clear: abandon before merge; revert or forward-fix after merge.

### A target migration is operationally complete only when

- [ ] Stable migration identity, ordering, and supersession lineage are recorded.
- [ ] Primary lane and accepted Directory Rules basis are correct.
- [ ] Coordinated lane records exist where responsibilities are materially distinct.
- [ ] Controlling contracts, schemas, policies, evidence, lifecycle, and release references are pinned.
- [ ] Immutable base and target states are recorded.
- [ ] Payloads, runners, versions, and digests are recorded.
- [ ] Affected database objects, schemas, contracts, datasets, graph families, producers, consumers, validators, fixtures, APIs, UI/MapLibre surfaces, and releases are inventoried.
- [ ] Compatibility, coexistence window, adoption order, and deprecation triggers are explicit.
- [ ] Rights, sensitivity, sovereignty, living-person, DNA, archaeology, rare-species, infrastructure, and public impacts are reviewed where applicable.
- [ ] Paired recovery identity, class, and record exist.
- [ ] Preconditions, abort thresholds, dry-run, rehearsal, and canary requirements are resolved.
- [ ] Required reviews and target-specific authorization are recorded.
- [ ] Execution receipt identifies target, runner, revision, payload digests, timestamps, and outcome.
- [ ] Required post-migration invariants passed.
- [ ] Required producers and consumers reached verified adoption states.
- [ ] Recovery was rehearsed where risk requires it, or the gap remains visible and blocks unsupported claims.
- [ ] Documentation, deprecation, drift, correction, incident, and release follow-up are complete.
- [ ] Rollback target or forward-fix lineage remains resolvable.
- [ ] Residual risk and unresolved verification items remain visible.
- [ ] No migration output is represented as external truth, policy approval, release approval, or publication authority.

## No-loss ledger

| Prior material | v1.3 disposition |
|---|---|
| Canonical migration-root purpose | Preserved and expanded |
| Lifecycle invariant | Preserved |
| Five migration lanes | Preserved; all five v1.1 lane contracts remain confirmed |
| Placeholder boundary | Newly surfaced from complete pinned-base inventory; all five stubs remain non-executable |
| Directory Rules authority | Updated to ADR-0029 accepted v2 posture |
| Rollback-entry requirement | Preserved; pairing enforcement remains explicitly unverified |
| Database/schema/data/graph distinctions | Preserved and aligned with lane READMEs |
| Sensitive-domain fail-closed posture | Preserved |
| Inputs and outputs | Preserved with repository task and delivery boundaries |
| Validation checklist | Preserved and expanded with v6 validation classes and criterion states |
| Review burden | Preserved by authority, sensitivity, recoverability, and coordination |
| Migration packet | Preserved and extended with repository-change metadata |
| Work-state model | Preserved and separated from delivery, evidence, validation, policy, and release state |
| Compatibility and adoption | Preserved |
| Recovery classes | Preserved and expanded to distinguish repository rollback, migration recovery, and release rollback |
| Definition of done | Split into repository delivery and operational migration completion |
| Open verification | Preserved; recursive inventory item closed with evidence |
| Workflow posture | Refreshed: eight configured schema families and rollback readiness behavior confirmed |
| Owner uncertainty | Preserved; CODEOWNERS routing is not stewardship or approval proof |
| Publication boundary | Preserved and sharpened |
| Stable headings and legacy anchors | Preserved |

## Open verification register

### Closed in the v1.3 evidence snapshot

- [x] Full recursive `migrations/` inventory: eleven paths.
- [x] Lane contents: each lane contains one v1.1 README and one explicit `0001_init.placeholder` stub.
- [x] Concrete executable payload boundary: none present in `migrations/` at the pinned base.
- [x] Current placement authority: Directory Rules v2 accepted by ADR-0029.
- [x] Open pull-request overlap on `migrations/README.md`: none at inspection.

### Remaining

- [ ] Select and document a database migration runner, or explicitly declare no database runner.
- [ ] Confirm schema, data, and graph migration executor conventions.
- [ ] Define canonical stable migration and recovery ID grammar.
- [ ] Define dependency and filename ordering rules.
- [ ] Verify one-to-one migration-to-recovery pairing after the first concrete payload exists.
- [ ] Decide whether paired recovery records must land in the same pull request.
- [ ] Define a machine-readable migration packet schema if justified.
- [ ] Define the canonical migration register or applied-version ledger and its owning responsibility root.
- [ ] Define target-environment identity and state-digest rules.
- [ ] Add dedicated migration validation orchestration only after packet, runner, fixtures, and outcomes are defined.
- [ ] Define valid, invalid, hold, not-applicable, and not-run fixtures for each migration class.
- [ ] Verify backup, snapshot, restore, and retention capabilities by environment.
- [ ] Define lock, downtime, maintenance-window, and concurrency classes.
- [ ] Define expand-and-contract and staged-breaking compatibility policy.
- [ ] Define producer/consumer adoption evidence and deprecation windows.
- [ ] Populate or select authoritative object-family and deprecation registers where schema migrations depend on them.
- [ ] Define graph/triplet endpoint, identity, evidence-link, duplicate, orphan, cycle, and projection checks.
- [ ] Define data-remap identity, provenance, temporal, spatial, lifecycle, and sensitivity checks.
- [ ] Define database permission and least-privilege migration checks.
- [ ] Define structured migration execution, adoption, verification, and recovery receipt homes and schemas.
- [ ] Define recovery rehearsal requirements by migration and risk class.
- [ ] Determine whether the current rollback-drill workflow should remain readiness-only or gain a separate migration-recovery workflow.
- [ ] Confirm release-review triggers for public API, MapLibre, tiles, exports, search, stories, AI surfaces, and published artifacts.
- [ ] Confirm security and incident handoff for failed, destructive, or exposure-relevant migrations.
- [ ] Confirm accountable stewards and independent approval requirements.
- [ ] Verify branch protection or ruleset requirements for migration paths.
- [ ] Add drift checks preventing canonical schemas, contracts, policy, lifecycle payloads, backups, or release records from moving into `migrations/`.
- [ ] Formalize host-render validation for this README.
- [ ] Revisit this README after the first concrete migration packet, rehearsal, or applied-ledger entry is implemented.

## Changelog

### v1.3 — 2026-08-09

- Regrounded the README at `main@8f26a3ed8d2fbc2f40fecf722177aeae2cb6297a`.
- Confirmed the complete eleven-path `migrations/` inventory and five non-executable placeholder stubs.
- Updated placement authority to the accepted Directory Rules v2 decision in ADR-0029.
- Adopted the v6 implementation-forward repository task contract while preserving the separate target-execution authority boundary.
- Added dependency-closure, review-boundary, staged-admission, concurrency, workflow-preflight, delivery-validation, remote-read-back, and terminal-boundary guidance.
- Added repository delivery states and separated them from migration work state, evidence grade, validation outcome, policy, release, and publication state.
- Extended the minimum migration packet with repository-change and validation-class fields.
- Split definition of done into repository delivery and operational migration completion.
- Preserved the same path, H1, stable H2 headings, legacy anchors, lifecycle law, five-lane model, recovery distinctions, and non-publication boundary.

### v1.2 — 2026-07-24

- Reconciled the root with all five merged repository-grounded v1.1 lane READMEs.
- Corrected workflow posture: bounded schema validation exists, while rollback-drill is an explicit readiness hold and does not simulate rollback.
- Expanded authority, status, inputs, outputs, validation, review, and related-root boundaries.
- Added finite validation outcomes and a migration evidence ladder.
- Expanded migration packet, state, deterministic identity, ordering, pairing, coordination, compatibility, adoption, execution, and recovery contracts.
- Clarified migration recovery versus release rollback.
- Updated definition of done, no-loss ledger, open verification, and evidence snapshot.
- Preserved the same path, legacy anchors, lifecycle law, five-lane model, and non-publication boundary.

### v1.1 — 2026-07-23

- Reorganized the root README to the Directory Rules folder contract.
- Grounded status in five confirmed child README lanes.
- Removed unsupported owner certainty.
- Distinguished documentation, payload, runner, applied state, and release authority.
- Added migration classification, packet, work-state, compatibility, recovery, and definition-of-done models.
- Marked executable tooling, payload depth, rollback coverage, and production history as unverified.
- Preserved legacy anchors and the v1 rollback identity.

### v1 — 2026-07-03

- Established the database, schema, data, graph, and rollback migration-root contract.
