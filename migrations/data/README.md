<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/migrations-data-readme
title: migrations/data/ — Governed Data Backfills, Repairs, Remaps, and Rebuilds
type: README; per-directory-readme; nested-migration-lane; data-state-change-control
version: v1.1
status: draft; repository-grounded; documented-lane; executable-payloads-unestablished; runner-unestablished; rollback-pairing-unverified; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes this path through the repository default owner @bartytime4life; accountable data, domain, migration, policy, security, and release stewardship assignments were not established
created: 2026-07-03
updated: 2026-07-24
supersedes: v1 documentation at the same path; no migration payload, data state, runtime behavior, release state, or publication state is superseded
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
policy_label: repository-facing; migrations; data-state-change; rollback-aware; evidence-first; fail-closed; non-publisher
current_path: migrations/data/README.md
owning_root: migrations/
responsibility: govern data backfills, repairs, remaps, lifecycle-safe relocations, and deterministic rebuild mechanics without becoming lifecycle-data, schema, contract, policy, evidence, release, or publication authority
truth_posture: >
  CONFIRMED same-path target; canonical migrations responsibility root; documented data and rollback lanes; Directory Rules assignment
  of data migrations to migrations/data/; mandatory paired recovery posture; current CODEOWNERS routing; and the parent migrations
  README's bounded conclusion that executable migration payloads were not established / PROPOSED data-migration classification,
  packet fields, invariant matrix, dry-run contract, work-state checks, and definition of done / UNKNOWN current data-migration
  runner, concrete payload inventory, target environments, dataset versions, applied migration history, backup and restore capability,
  execution receipts, and production outcomes / NEEDS VERIFICATION recursive lane inventory, one-to-one rollback pairing, stable ID
  convention, dedicated migration CI, steward assignments, sensitive-data review workflow, and release integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: d0869f7d62d4432d4246be06c080c97145ef9a4f
  parent_readme_blob: 48da6b62000d145359bfbd7f8383961c9f285b2a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  codeowners_status: repository default routing resolves this path to @bartytime4life; role-level stewardship and independent approval remain unverified
  inspection_method: exact GitHub file reads, parent-lane evidence review, bounded repository search, and open-PR overlap search; no recursive Git tree, data store, migration runner, backup system, CI execution, release artifact, or runtime environment was inspected
related:
  - ../README.md
  - ../database/README.md
  - ../schema/README.md
  - ../graph/README.md
  - ../rollback/README.md
  - ../../data/README.md
  - ../../contracts/README.md
  - ../../schemas/README.md
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
  - "The lane is documented, but concrete data-migration payloads, a canonical runner, an applied-version ledger, and verified recovery coverage were not established."
  - "Static badges summarize inspected repository state only; they are not execution, review, rollback, release, or publication proof."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `migrations/data/` — Governed Data Backfills, Repairs, Remaps, and Rebuilds

> **One-line purpose.** Govern deliberate changes to persisted KFM data state while preserving stable identity, evidence and provenance links, lifecycle boundaries, rights and sensitivity controls, validation, and recoverability.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Lane: data-state migration](https://img.shields.io/badge/lane-data--state%20migration-1f6feb?style=flat-square)](#authority-level)
[![Payloads: not established](https://img.shields.io/badge/payloads-not%20established-b42318?style=flat-square)](#status)
[![Runner: not established](https://img.shields.io/badge/runner-not%20established-b42318?style=flat-square)](#validation)
[![Recovery pairing: needs verification](https://img.shields.io/badge/recovery%20pairing-needs%20verification-d4a72c?style=flat-square)](#recovery-and-forward-fix)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)
[![Reviewed: 2026-07-24](https://img.shields.io/badge/reviewed-2026--07--24-0969da?style=flat-square)](#last-reviewed)

> [!IMPORTANT]
> **Safe current conclusion:** `migrations/data/` is a documented migration lane beneath the canonical `migrations/` responsibility root. Current bounded evidence establishes its README and recovery relationship, but does **not** establish concrete data-migration payloads, a selected runner, an applied-version ledger, complete rollback pairing, execution history, or production outcomes.

> [!CAUTION]
> A migration plan, parsed script, dry-run example, branch, pull request, or green unrelated workflow does not prove that data was changed safely. An execution claim requires a named base state, exact target, pinned payload, observed run evidence, post-migration checks, and recovery evidence.

> [!WARNING]
> This directory is not a data store. RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, and PUBLISHED payloads remain under `data/`. Restricted rows, source extracts, dumps, backups, secrets, or precise sensitive locations must never be committed here.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-bounded-topology) · [Classification](#data-migration-classification) · [Packet](#minimum-data-migration-packet) · [Invariants](#data-specific-invariants) · [Execution](#dry-run-and-execution-contract) · [Recovery](#recovery-and-forward-fix) · [Done](#definition-of-done) · [Open verification](#open-verification-register)

---

## Purpose

`migrations/data/` owns the **mechanics and review packet** for governed changes to persisted data values, identity mappings, evidence links, lifecycle placement, and deterministic derived products.

Typical data migrations include:

- backfilling a newly required field from admissible evidence;
- repairing invalid or inconsistent values;
- normalizing identifiers or controlled vocabularies;
- remapping records through a versioned crosswalk;
- rebuilding derived records after a source, schema, contract, or policy change;
- relocating records between non-public lifecycle phases through an explicit governed plan;
- correcting catalog or triplet references when the primary defect is persisted data state;
- coordinating deprecation or supersession of obsolete data representations.

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A data migration may support a governed transition. It does not itself approve promotion, release, publication, correction, or public exposure.

Choose this lane by **primary responsibility**, not by language or file extension. A Python or SQL file belongs here only when its primary purpose is changing persisted data state. Database structure belongs in `migrations/database/`; schema or contract compatibility belongs in `migrations/schema/`; graph topology belongs in `migrations/graph/`; recovery records belong in `migrations/rollback/`.

## Authority level

<a id="status--authority"></a>

**Nested operational lane for data-state migration mechanics; subordinate to the authorities that define meaning, machine shape, admissibility, evidence, lifecycle ownership, and release.**

| Question | Controlling authority |
|---|---|
| Where this migration material belongs | Directory Rules, accepted placement ADRs, then [`migrations/README.md`](../README.md) and this README |
| What a record or field means | [`contracts/`](../../contracts/README.md) |
| What machine shape is valid | [`schemas/`](../../schemas/README.md) |
| What rights, sensitivity, or handling is permitted | [`policy/`](../../policy/README.md) and applicable review records |
| What source or evidence supports a repair | Source registry, `EvidenceRef`, `EvidenceBundle`, receipts, proofs, or correction evidence |
| Which lifecycle phase owns the payload | [`data/`](../../data/README.md) |
| How migration mechanics are planned | `migrations/data/` |
| How engineering recovery is recorded | [`migrations/rollback/`](../rollback/README.md) |
| Whether a release or public correction is approved | [`release/`](../../release/README.md) and applicable promotion/review records |
| How execution occurs | The selected runner, named target environment, migration payload, and runbook |
| Who receives GitHub review routing | [`.github/CODEOWNERS`](../../.github/CODEOWNERS); current routing resolves to `@bartytime4life` |
| Who is accountable as data, domain, migration, policy, security, or release steward | **NEEDS VERIFICATION** through approved responsibility assignments and review records |

This lane may carry plans, payloads, compatibility notes, validation summaries, and sanitized execution summaries. It must not redefine a stronger authority or turn a proposed migration design into accepted governance.

## Status

| Surface | Current evidence | Status |
|---|---|---|
| This README | Present and updated in place | **CONFIRMED — documentation** |
| Parent migration root | `migrations/README.md` present and repository-grounded | **CONFIRMED — documentation** |
| Recovery lane README | `migrations/rollback/README.md` present | **CONFIRMED — documentation** |
| Concrete data-migration payloads | Not established by bounded parent inspection and search | **UNKNOWN / NEEDS VERIFICATION** |
| Canonical data-migration runner | Not established | **UNKNOWN** |
| Dedicated data-migration workflow or CI gate | Not established | **NEEDS VERIFICATION** |
| Applied migration/version ledger | Not established | **NEEDS VERIFICATION** |
| Stable migration ID and ordering convention | Examples exist; standardized contract not established | **PROPOSED / NEEDS VERIFICATION** |
| One-to-one recovery pairing | Required by Directory Rules; coverage not recursively verified | **NEEDS VERIFICATION** |
| Target data stores and environments | Not inspected | **UNKNOWN** |
| Backup, snapshot, restore, or replay capability | Not inspected | **UNKNOWN** |
| Execution receipts and production history | Not inspected | **UNKNOWN** |
| GitHub ownership routing | Repository default routes to `@bartytime4life` | **CONFIRMED routing; stewardship unverified** |
| Release or publication authority | Not owned by this lane | **DENIED by boundary** |

Treat examples and templates below as **proposed documentation contracts**, not as evidence that a runner, schema, workflow, or migration history exists.

## What belongs here

Use `migrations/data/` when data-state change is the primary responsibility.

Accepted material includes:

- data backfill, repair, normalization, remap, and rebuild plans;
- safe, reviewable migration payloads whose exact inputs and outputs are declared;
- versioned crosswalk and identifier-remap plans;
- evidence-link or provenance-reference repair plans;
- lifecycle relocation plans that preserve promotion and quarantine controls;
- deterministic rebuild plans for derived data after upstream changes;
- catalog or triplet alignment repairs when persisted record state is the primary target;
- preflight, dry-run, canary, batching, restart, and post-check definitions;
- migration manifests binding payloads, digests, base state, target state, dependencies, validation, and recovery;
- sanitized diff, count, checksum, and invariant summaries;
- compatibility, adoption, deprecation, and consumer-cutover notes;
- pointers to authoritative execution receipts, proof objects, correction records, or release-impact reviews;
- documented forward-fix plans when direct reversal would be less safe.

Suitable formats may include Markdown, SQL, Python, or another repository-supported executable form. A notebook belongs here only when its reproducibility, non-interactive execution, output stripping, dependency pinning, and review burden are explicitly justified.

## What does not belong here

Do not use `migrations/data/` as a lifecycle store, source registry, evidence store, backup system, policy/schema home, release root, or secrets store.

The following do not belong here:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED datasets;
- source downloads, local extracts, caches, tiles, PMTiles, COGs, GeoParquet, shapefiles, rasters, or bulk tabular files;
- database dumps, graph dumps, backups, snapshots, WAL archives, restore images, or replay stores;
- canonical source descriptors, `EvidenceBundle` objects, receipts, proofs, or signed attestations;
- release manifests, promotion decisions, release rollback cards, correction notices, withdrawal notices, or publication approvals;
- JSON Schemas, semantic contracts, policy bundles, or policy decisions;
- primary database-structure migrations, schema-compatibility migrations, graph-topology migrations, or recovery records owned by sibling lanes;
- production credentials, DSNs, connection strings, tokens, API keys, private keys, certificates, kubeconfigs, or `.env` files;
- unredacted living-person data, DNA/genomic material, archaeology or burial-site data, rare-species exact locations, protected cultural information, private infrastructure details, or rights-uncertain records;
- destructive one-off commands lacking stable scope, pinned base state, preconditions, dry-run, validation, recovery, review, and audit fields;
- generated or AI-inferred values promoted as evidence without admissible support and review.

A sanitized summary or pointer may live here; the authoritative payload, receipt, proof, release object, or restricted record remains in its controlling root.

If restricted data, a secret, dump, or backup lands here, stop normal work, isolate the material, rotate or revoke access where appropriate, and follow the applicable incident, correction, and governance process.

## Inputs

A data-migration packet may consume:

| Input | Why it is needed |
|---|---|
| Accepted ADR or explicit scoped decision | Establishes why the transition is allowed |
| Issue, defect, validation failure, correction request, or release need | Establishes reason and bounded scope |
| Semantic contract | Defines intended meaning |
| Machine schema and version | Defines intended shape |
| Policy decision or sensitivity review | Constrains handling, selection, transformation, and exposure |
| Source and evidence references | Grounds backfills, repairs, remaps, or corrections |
| Base-state inventory | Pins dataset versions, lifecycle phases, counts, hashes, and target environment |
| Deterministic selection specification | Defines exactly which records or artifacts are affected |
| Identity and crosswalk rules | Defines preserved IDs, remaps, aliases, and collision handling |
| Temporal and spatial semantics | Defines valid/source/observed/retrieval/release time and geometry/CRS handling where applicable |
| Producer and consumer inventory | Defines compatibility and adoption order |
| Release and public-artifact context | Defines downstream map, API, tile, export, cache, and correction impact |
| Backup, snapshot, restore, or replay capability | Defines feasible recovery |
| Valid and invalid fixtures | Defines representative success and failure states |
| Environment and runner contract | Defines how execution is performed safely and repeatably |

Material inputs should be identified by commit, version, content digest, release ID, dataset version, source retrieval, or named environment. Terms such as “latest,” “all records,” or “the production database” are not sufficiently precise for consequential migrations.

## Outputs

A data-migration packet may produce:

- reviewed migration plans;
- executable payloads and content digests;
- deterministic selection and target-state specifications;
- identity, alias, or crosswalk maps;
- preflight and dry-run reports;
- row, feature, geometry, relationship, checksum, and invariant reports;
- compatibility and adoption matrices;
- sanitized execution summaries and pointers to authoritative receipts;
- post-migration verification reports;
- paired recovery or forward-fix records;
- documentation, deprecation, drift, correction, and release-impact updates.

These outputs remain bounded:

| Output | What it can prove | What it does not prove |
|---|---|---|
| Migration plan | Intended change and review surface exist | Execution occurred |
| Parsed SQL or script | Syntax may be acceptable to a parser | Target compatibility, safety, or idempotence |
| Dry run | A preview completed in a named context | Shared or production outcome |
| Selection manifest | Intended target set was identified | Every selected record was mutated correctly |
| Identity/crosswalk map | Planned remaps are explicit | Consumer adoption or semantic correctness |
| Execution receipt | A named action was attempted or completed | External truth, review approval, release approval, or publication |
| Post-check report | Named invariants passed in a named context | Universal correctness or absence of hidden impact |
| Recovery record | Recovery instructions exist | Recovery was rehearsed or will work |
| Git commit or pull request | Repository bytes changed | Data was migrated, released, corrected publicly, or published |

This lane never publishes KFM data by itself.

## Validation

Validation is data-class- and consequence-specific. A single generic green check is insufficient.

### Required source checks

Every data-migration change should verify:

- target path and lane;
- stable migration identity and ordering;
- exact base state and target state;
- deterministic record or artifact selection;
- migration and recovery-record pairing;
- affected dataset, lifecycle phase, source role, and evidence inventory;
- schema, contract, policy, and release dependencies;
- producer and consumer adoption order;
- rights, sensitivity, and public-impact posture;
- payload digests and dependency pins;
- preflight, dry-run, canary, batching, restart, and post-check behavior where applicable;
- secret and restricted-content absence;
- documentation, correction, deprecation, and release impact.

### Data-specific executable evidence

| Concern | Minimum evidence |
|---|---|
| Deterministic scope | Pinned input versions plus exact query, manifest, ID set, or selection hash |
| Count reconciliation | Before/after row or feature counts with explained additions, updates, deletions, and skips |
| Identity | Uniqueness, collision, alias, remap, and referential checks |
| Evidence and provenance | Evidence/source references preserved or intentionally remapped with closure checks |
| Lifecycle | Records remain in or move through allowed phases without bypassing promotion |
| Temporal semantics | Valid/source/observed/retrieval/release times remain distinct where material |
| Spatial semantics | Geometry validity, CRS, bounds, precision, and topology checks where applicable |
| Schema and constraints | Required fields, enums, types, null rules, ranges, and uniqueness checks |
| Sensitivity and rights | Restricted records remain quarantined, redacted, generalized, staged, or denied as required |
| Derived rebuilds | Canonical inputs pinned; outputs reproducible; stale derivatives invalidated |
| Idempotence and restart | Re-run behavior is safe, detectable, resumable, or explicitly blocked |
| Dry run | Preview diff and warnings produced without unsafe mutation |
| Post-run reconciliation | Counts, hashes, samples, constraints, evidence links, and downstream references verified |
| Public impact | API, map, tile, export, catalog, cache, correction, and release effects reviewed separately |

### Current repository boundary

No repository-native data-migration command, selected runner, dedicated workflow, applied-version ledger, or verified fixture suite was established in the bounded inspection. Until these exist and are verified:

- do not advertise a canonical run command;
- do not invent tool, database, graph, or environment support;
- record migration-specific commands in the packet;
- mark unexecuted checks `NOT RUN`;
- treat unrelated schema, contract, policy, or release checks as supporting context, not migration proof;
- keep shared or release-relevant execution blocked until the required evidence and review exist.

## Review burden

Review scales with consequence, not file extension.

**Confirmed routing:** the repository's default CODEOWNERS pattern routes this path to `@bartytime4life`. That route is not proof of steward assignment, independent review, policy approval, execution authorization, release approval, or completed review.

| Change class | Required review concerns; accountable assignments remain NEEDS VERIFICATION |
|---|---|
| README-only wording with no behavior change | Documentation accuracy, migration-boundary accuracy, link and render review |
| Data backfill, repair, normalization, remap, or rebuild | Data ownership, affected domain meaning, migration mechanics, validation |
| RAW or source-close material | Source authority, rights, provenance, data handling |
| QUARANTINE or restricted material | Policy, sensitivity, access, transform, and audit controls |
| Identity or crosswalk change | Collision handling, alias lineage, evidence links, consumer adoption |
| Catalog, triplet, API, map, tile, or export references | Catalog/graph integrity, governed API/UI behavior, release and cache impact |
| Published artifact or release-state impact | Release review, correction/withdrawal path, rollback target, public communication |
| Living-person, DNA/genomic, archaeology, rare-species, infrastructure, cultural, or rights-uncertain data | Policy/sensitivity review and relevant domain authority |
| Credentials, access, or incident recovery | Security review and affected-system ownership |
| Destructive, irreversible, or forward-fix-only change | Explicit risk acceptance, independent recovery review where practical, named target authorization |
| Cross-lane or multi-environment migration | Review for every affected responsibility and environment |

For high-impact migrations, authoring, approval, execution, and verification should be separated when repository maturity supports it.

## Related folders

| Location | Relationship |
|---|---|
| [`migrations/`](../README.md) | Canonical migration root, shared packet, state, compatibility, and recovery guidance |
| [`migrations/database/`](../database/README.md) | Database structure and database-managed behavior |
| [`migrations/schema/`](../schema/README.md) | Schema and semantic compatibility transitions |
| [`migrations/graph/`](../graph/README.md) | Graph/triplet topology, identity, and evidence-link changes |
| [`migrations/rollback/`](../rollback/README.md) | Paired engineering recovery, disablement, restore, or forward-fix records |
| [`data/`](../../data/README.md) | Lifecycle payloads and authoritative data-state ownership |
| [`contracts/`](../../contracts/README.md) | Semantic meaning |
| [`schemas/`](../../schemas/README.md) | Machine shape |
| [`policy/`](../../policy/README.md) | Admissibility, rights, sensitivity, and obligations |
| [`tests/`](../../tests/README.md) | Representative enforceability and regression evidence |
| [`tools/validators/`](../../tools/validators/README.md) | Repository-wide validator implementations |
| [`release/`](../../release/README.md) | Release decisions, correction, withdrawal, and public rollback |
| [`docs/runbooks/`](../../docs/runbooks/README.md) | Operator procedures and recovery drills |
| [`SEPARATION_OF_DUTIES.md`](../../docs/governance/SEPARATION_OF_DUTIES.md) | Review and duty-separation guidance |
| [`directory-rules.md`](../../docs/doctrine/directory-rules.md) | Canonical placement doctrine |
| [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review routing; not governance approval |

## ADRs

A data migration does not always require an ADR. An ADR is required when the migration:

- adds, removes, or renames a canonical root;
- creates a parallel schema, contract, policy, source, registry, receipt, proof, release, lifecycle, or migration authority;
- changes the canonical schema-home or responsibility split;
- splits, merges, redefines, or bypasses a lifecycle phase;
- changes deterministic identity or crosswalk semantics used across lanes;
- materially changes a public contract or trust-membrane boundary;
- standardizes a repository-wide migration ID, work-state, receipt, runner, or applied-ledger contract;
- introduces a non-reversible architectural decision whose tradeoffs must persist;
- intentionally bends a KFM invariant.

A migration packet may implement an accepted decision. It cannot make its own proposed ADR accepted.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-24 |
| Review status | Repository-grounded v1.1 documentation update |
| Current maturity | Documented data lane; concrete payloads, runner, workflow, applied ledger, target environments, execution history, and recovery coverage unverified |
| Next review trigger | First concrete data-migration payload, selected runner, dedicated workflow, applied ledger, recovery rehearsal, destructive migration, sensitive-data migration, or public-impacting data migration |

---

<a id="repo-fit"></a>

## Current bounded topology

The confirmed documentation topology relevant to this lane is:

```text
migrations/
├── README.md
├── database/
│   └── README.md
├── schema/
│   └── README.md
├── data/
│   └── README.md      ◀── you are here
├── graph/
│   └── README.md
└── rollback/
    └── README.md
```

This is a bounded named-path inventory, not a recursive tree attestation. Current evidence does not establish executable payloads below this lane.

## Data-migration classification

Classify the intended state transition before designing the payload.

| Class | Primary purpose | Typical evidence burden |
|---|---|---|
| `BACKFILL` | Populate missing values or references | Source/evidence basis, deterministic selection, null-to-value reconciliation |
| `REPAIR` | Correct invalid, inconsistent, or corrupted values | Defect evidence, before/after invariants, correction lineage |
| `NORMALIZE` | Convert values into a controlled or canonical representation | Contract/vocabulary authority, compatibility and consumer impact |
| `REMAP` | Change IDs, aliases, geography versions, crosswalks, or relationships | Stable mapping, collision checks, referential closure, adoption order |
| `REBUILD` | Regenerate a derivative from pinned canonical inputs | Reproducibility, invalidation, output digest, consumer cutover |
| `RELOCATE` | Move records between allowed non-public lifecycle states | Phase eligibility, policy decision, provenance continuity |
| `DEPRECATE_OR_CLEANUP` | Remove obsolete representations after adoption | Usage evidence, deprecation window, no orphaned references |
| `CORRECTION_OR_SUPERSESSION` | Apply a governed correction to persisted data | Correction authority, lineage, release impact, public follow-up |
| `COORDINATED` | Multiple equally primary migration responsibilities | Linked lane packets, explicit ordering, umbrella coordination record |

Do not classify a migration by whether its payload is SQL, Python, or a notebook. Classify it by the **primary data-state change**.

<a id="migration-contract"></a>
<a id="required-migration-record"></a>

## Minimum data-migration packet

A shared-state or release-relevant data migration should have a complete packet before execution.

```yaml
migration_id: mig-data-<stable-id>
title: <short purpose>
status: PROPOSED
class: BACKFILL | REPAIR | NORMALIZE | REMAP | REBUILD | RELOCATE | DEPRECATE_OR_CLEANUP | CORRECTION_OR_SUPERSESSION | COORDINATED
owner: NEEDS VERIFICATION

authority_refs: []
reason_refs: []
evidence_refs: []

base_state:
  revision: <commit-or-release>
  environment: <named-environment>
  lifecycle_phase: <raw|work|quarantine|processed|catalog|triplet|published>
  dataset_versions: []
  content_digests: []
  row_or_feature_counts: {}

selection:
  description: <exact target set>
  query_or_manifest_ref: <path-or-id>
  selection_digest: <sha256-or-equivalent>

target_state:
  description: <intended state>
  lifecycle_phase: <phase>
  dataset_versions: []
  expected_counts: {}

payloads:
  - path: <migration-payload>
    sha256: <digest>

identity:
  strategy: preserve | alias | remap | regenerate
  mapping_ref: null
  collision_policy: NEEDS VERIFICATION

provenance:
  source_refs: []
  evidence_link_policy: preserve
  transform_spec_ref: null

temporal:
  affected_fields: []
  semantics: NEEDS VERIFICATION

spatial:
  geometry_impact: none | validate | transform | generalize
  crs: null
  precision_policy_ref: null

dependencies: []

affected:
  domains: []
  producers: []
  consumers: []
  schemas: []
  contracts: []
  policies: []
  datasets: []
  catalog_records: []
  graph_or_triplet_families: []
  api_routes: []
  map_layers: []
  releases: []

preconditions: []

dry_run:
  command_or_workflow: NEEDS VERIFICATION
  evidence_ref: null
  expected_diff: {}

validation:
  pre_checks: []
  post_checks: []
  invariants: []

compatibility:
  class: backward-compatible | expand-and-contract | staged-breaking | rebuildable-derivative | destructive | forward-fix-only
  window: null

sensitivity:
  impact: none | reviewed | hold
  policy_refs: []

recovery_ref: migrations/rollback/<paired-id>.md
release_impact: none | internal | candidate | public

execution:
  runner: NEEDS VERIFICATION
  target_authorization_ref: null
  receipt_ref: null

review:
  required_functions: []
  records: []
```

This is a **PROPOSED documentation contract**, not a verified machine schema. Standardizing it as machine shape requires the canonical `schemas/` home, tests, compatibility rules, and accepted governance.

## Data-specific invariants

Every consequential data migration should preserve or explicitly govern these invariants:

| Invariant | Required posture |
|---|---|
| Lifecycle integrity | No direct RAW-to-PUBLISHED or QUARANTINE-to-public shortcut |
| Stable identity | Preserve IDs where practical; map aliases/remaps deterministically; retain lineage |
| Evidence closure | Preserve or intentionally repair `EvidenceRef` and `EvidenceBundle` relationships |
| Source-role integrity | Do not let context, modeled, derived, or display sources become primary authority silently |
| Provenance | Pin inputs, transform rules, payload digests, operator/tool identity, target, and outcome |
| Temporal integrity | Preserve distinct temporal semantics where material |
| Spatial integrity | Preserve CRS, validity, scale, precision, and generalization policy where applicable |
| Rights and sensitivity | Fail closed; quarantine, redact, generalize, stage, delay, or deny when unresolved |
| Deterministic selection | Name and hash the exact target set; avoid mutable “all current records” scope |
| Idempotence and restart | Re-run safely, detect prior application, resume, or fail explicitly |
| Rebuildability | Derived products point to canonical inputs and can be invalidated and regenerated |
| Consumer compatibility | Sequence producers, consumers, APIs, maps, catalogs, and releases deliberately |
| Correction and rollback | Retain paired recovery, correction, supersession, and forward-fix lineage |
| Non-publication | Migration completion is not release or KFM publication |

A migration that cannot preserve an invariant must state the tradeoff, risk, decision authority, and compensating control.

## Dry-run and execution contract

### Preflight

Before mutation, establish:

1. exact base revision, dataset versions, environment, and lifecycle phase;
2. payload digest and dependency versions;
3. target-selection manifest or query plus selection digest;
4. current counts, checksums, constraints, identity, evidence, temporal, spatial, and sensitivity state;
5. producer/consumer and release freeze requirements;
6. backup, snapshot, restore, replay, disablement, or compensating path;
7. target authorization and required review records.

### Dry run

A dry run should:

- be read-only or transactionally reversible where supported;
- emit aggregate counts, diffs, warnings, collisions, skips, and expected downstream impact;
- avoid restricted row dumps, secrets, private endpoints, and unsafe samples;
- identify non-deterministic selection, stale input, policy holds, and unresolved evidence;
- produce a named evidence artifact or sanitized summary;
- fail closed when base state, target set, rights, sensitivity, or recovery posture is unresolved.

### Execution

Execution should:

- target one named environment or state;
- use the pinned payload and selection;
- support bounded batching, checkpointing, restart, or explicit non-resumability where material;
- record start/end time, runner, operator/tool identity, revision, payload digest, target, outcome, and failures;
- stop on invariant or policy failure unless an approved exception explicitly governs continuation;
- never contain destructive defaults hidden behind a generic command;
- keep authoritative receipts in the governed receipt home and reference them from the migration packet.

### Post-run verification

Verify:

- selected, updated, inserted, deleted, skipped, and failed counts;
- identity and crosswalk closure;
- evidence and provenance links;
- schema and constraint conformance;
- temporal and spatial semantics;
- sensitivity and public-safe transforms;
- derived-product invalidation or rebuild status;
- catalog, graph/triplet, API, map, tile, export, and release references;
- recovery readiness;
- documentation, correction, deprecation, and release follow-up.

<a id="recovery-and-forward-fix"></a>

## Recovery and forward fix

Every consequential data migration must link to a paired record under [`migrations/rollback/`](../rollback/README.md), even when direct reversal is unsafe.

Use one recovery class:

| Recovery class | Meaning |
|---|---|
| `REVERSIBLE` | A tested reversal can restore the prior approved data state |
| `DISABLEABLE` | New reads, writes, or derived behavior can be disabled while state remains |
| `RESTORABLE` | Backup, snapshot, or replay restoration is the recovery path |
| `COMPENSATING` | A governed corrective migration restores safety |
| `FORWARD_FIX_ONLY` | Reversal is less safe; an explicit compensating path is the approved option |
| `NON_RECOVERABLE` | Not acceptable for shared or release-relevant state absent exceptional documented governance |

The recovery record should identify:

- paired migration ID and payload digest;
- target environment and base state;
- irreversible changes or information loss;
- activation conditions;
- backup, snapshot, restore, replay, disablement, or compensating references;
- public API, map, tile, export, catalog, cache, and release impact;
- pre- and post-recovery checks;
- rehearsal evidence or `NOT RUN`;
- correction, withdrawal, incident, or release references where applicable.

A rollback file existing in Git is not proof that recovery works. Migration recovery also does not replace release rollback cards, correction notices, withdrawals, backups, or incident records.

## Definition of done

A data migration is complete only when every applicable item is closed:

- [ ] Stable migration identity and ordering are recorded.
- [ ] The primary lane and Directory Rules basis are correct.
- [ ] Intended meaning, machine shape, policy, and evidence point to controlling authorities.
- [ ] Base and target state are pinned.
- [ ] Exact selection and selection digest are recorded.
- [ ] Payloads and content digests are recorded.
- [ ] Identity, provenance, temporal, spatial, lifecycle, and sensitivity impacts are explicit.
- [ ] Producers, consumers, catalogs, graphs/triplets, APIs, maps, tiles, exports, and releases are inventoried.
- [ ] Compatibility and rollout order are explicit.
- [ ] Recovery class and paired recovery record exist.
- [ ] Preflight and dry run completed, or `NOT RUN` is justified.
- [ ] Required review and target authorization records exist.
- [ ] Execution receipt identifies runner, target, revision, payload, selection, and outcome.
- [ ] Before/after counts and invariants reconcile.
- [ ] Evidence and provenance links remain valid.
- [ ] Restricted material remains quarantined, redacted, generalized, staged, delayed, or denied as required.
- [ ] Recovery was rehearsed where risk requires it, or the gap remains visible.
- [ ] Documentation, deprecation, correction, withdrawal, cache, and release follow-up are complete.
- [ ] Rollback target or forward-fix lineage is retained.
- [ ] No migration result is misrepresented as release approval or KFM publication.

## No-loss ledger

| v1 material | v1.1 disposition |
|---|---|
| Governed data-migration purpose | Preserved and sharpened |
| Lifecycle invariant | Preserved |
| Data, database, schema, graph, and rollback responsibility split | Preserved and aligned with the parent README |
| Backfill, repair, normalization, rebuild, and relocation scope | Preserved and expanded by consequence |
| Sensitive-domain fail-closed posture | Preserved |
| Date-prefixed filename examples | Reframed as examples; stable identity convention remains unverified |
| Required migration record | Preserved as a richer proposed packet |
| Dry-run and validation posture | Preserved and expanded |
| Rollback-entry requirement | Preserved; coverage explicitly remains unverified |
| Review burden | Preserved, with verified CODEOWNERS routing separated from unverified stewardship |
| Owner placeholders | Replaced with verified routing plus role-assignment uncertainty |
| Open verification list | Preserved and extended |
| Publication boundary | Preserved and clarified |
| Existing anchors | Preserved through explicit compatibility anchors |

<a id="open-verification"></a>

## Open verification register

- [ ] Obtain a recursive tracked inventory of `migrations/data/`.
- [ ] Confirm whether concrete data-migration payloads exist beyond this README.
- [ ] Select and document the canonical data-migration runner or explicitly declare no shared runner.
- [ ] Define a stable data-migration ID and filename ordering convention.
- [ ] Verify one-to-one data-migration-to-recovery pairing.
- [ ] Decide whether paired recovery records must land in the same pull request.
- [ ] Define a machine-readable data-migration packet schema if justified.
- [ ] Define an applied-version or migration-state ledger and its owning root.
- [ ] Define no-network valid and invalid fixtures for backfill, repair, remap, rebuild, relocation, destructive, and forward-fix-only classes.
- [ ] Verify target data stores and named environments.
- [ ] Verify backup, snapshot, restore, replay, and retention capabilities by environment.
- [ ] Define deterministic selection and selection-digest rules.
- [ ] Define identity collision, alias, remap, and crosswalk closure rules.
- [ ] Define evidence/provenance-link preservation checks.
- [ ] Define temporal and spatial invariant checks.
- [ ] Define sensitive-data review and public-safe transform workflow.
- [ ] Define batching, checkpoint, restart, idempotence, and prior-application detection rules.
- [ ] Define migration execution receipt placement and schema.
- [ ] Confirm catalog, graph/triplet, governed API, MapLibre, tile, export, and release review triggers.
- [ ] Define recovery rehearsal expectations by consequence class.
- [ ] Confirm accountable stewards and independent approval requirements.
- [ ] Verify branch protection or ruleset requirements for this path.
- [ ] Formalize host-render validation for this README.
- [ ] Revisit this README after the first concrete data-migration packet is implemented.

## Changelog

### v1.1 — 2026-07-24

- Reorganized the lane README to the Directory Rules folder contract.
- Grounded status in current parent-root, rollback-lane, Directory Rules, and CODEOWNERS evidence.
- Removed unsupported certainty around steward assignments.
- Distinguished documentation, payloads, runner, applied state, recovery, release, and publication authority.
- Added data-migration classification, a proposed minimum packet, invariant matrix, dry-run/execute/post-check contract, and definition of done.
- Marked executable tooling, target environments, payload depth, applied history, recovery coverage, and production outcomes as unverified.
- Preserved prior anchors, lifecycle law, sensitivity posture, and rollback requirement.

### v1 — 2026-07-03

- Established the initial data-migration lane contract for backfills, repairs, lifecycle movement, validation, and rollback pairing.
