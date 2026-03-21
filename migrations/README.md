<!-- [KFM_META_BLOCK_V2]
doc_id: NEEDS-VERIFICATION
title: migrations
type: standard
version: v1
status: draft
owners: NEEDS VERIFICATION
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [../README.md, ../contracts/, ../schemas/, ../configs/, ../infra/, ../scripts/]
tags: [kfm, migrations, storage-evolution]
notes: [doc_id, owners, and dates require repo-side confirmation; March 20-21 replacement-grade KFM manual family is the doctrinal baseline for this draft; relative links reflect documented target surfaces, not direct mounted repo confirmation in this session; current workspace evidence for repo state was PDF-only]
[/KFM_META_BLOCK_V2] -->

# `migrations`

Deterministic, reviewable storage and trust-state evolution for Kansas Frontier Matrix.

> **Status:** experimental  
> **Document lifecycle:** draft  
> **Authority posture:** operational / supporting  
> **Owners:** **NEEDS VERIFICATION**  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![lifecycle](https://img.shields.io/badge/lifecycle-draft-lightgrey) ![authority](https://img.shields.io/badge/authority-operational-blue) ![surface](https://img.shields.io/badge/surface-migrations-6f42c1) ![workspace](https://img.shields.io/badge/workspace%20evidence-PDF--only-lightgrey) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current evidence boundary](#current-evidence-boundary) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Migration posture](#migration-posture) · [Contracts & proof objects](#contracts--proof-objects) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix--verification-notes)

> [!IMPORTANT]
> This directory guide is **evidence-bounded**. In the current session, the directly inspectable workspace exposed the attached PDF corpus under `/mnt/data`, but no mounted repository checkout, schema registry, workflow inventory, deployment manifests, dashboards, or runtime logs. Statements about live repo contents therefore stay **INFERRED**, **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION** unless the attached KFM manuals establish them directly.

> [!WARNING]
> In KFM, migration is **not** just “run the database script.” The current corpus treats migration as a governed change problem that can affect schema, data, contracts, policy, release state, runtime trust behavior, rollback, supersession, withdrawal, and correction visibility.

## Scope

`migrations/` is the directory contract for **governed change** to durable KFM structures and trust-bearing artifacts.

That includes database work, but it is intentionally broader. In the March 2026 KFM replacement-grade manuals, migration spans schema change, data repair and backfill, contract and envelope evolution, policy and registry change, release/promotion consequences, compatibility seams, rollback, supersession, withdrawal, and visible correction.

> [!NOTE]
> **Baseline determination.** This guide treats the March 20-21 replacement-grade KFM manual family as the doctrinal baseline. A March 6 continuity compendium described `migrations/` more narrowly as **schema/DB migration scripts**. That narrower role is retained here as one valid input class, but not as the whole migration contract.

### Truth markers used in this guide

| Marker | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by the attached KFM corpus or by current-session evidence visible in this run |
| **INFERRED** | Strongly implied by the corpus, but not directly verified as mounted repo/runtime reality |
| **PROPOSED** | Recommended target-state shape consistent with the corpus, not verified as current implementation |
| **UNKNOWN** | Not supported strongly enough in the current session to present as settled fact |
| **NEEDS VERIFICATION** | Explicit placeholder or repo-specific fact that should be checked before merge |

### Directory contract at a glance

| Item | Status | What that means |
|---|---|---|
| Migration / rollback / correction manual family in KFM documentation architecture | **CONFIRMED** | Later KFM manuals explicitly treat migration as part of verification, release, rollback, and correction discipline. |
| `migrations/` as a documented top-level target surface | **CONFIRMED as target / UNKNOWN as mounted reality** | A March 20 master-design skeleton places `migrations/` beside `contracts/`, `tests/`, `scripts/`, `configs/`, and `infra/`, but the live repo tree was not mounted in this session. |
| Earlier continuity description of `migrations/` as schema/DB migration scripts | **CONFIRMED continuity artifact / NEEDS VERIFICATION** | Valid as one content class, but narrower than the later replacement-grade doctrine. |
| Concrete current contents of `migrations/` | **UNKNOWN** | No direct file inventory was available beyond this requested document. |
| `migrations/README.md` as the intended local guide | **PROPOSED by this file** | This document is the reviewable directory contract for the surface. |

### What this directory is for

This surface should make migration work:

- reviewable
- staged and reversible
- linked to proof objects
- explicit about compatibility seams
- honest about rollback, supersession, withdrawal, and correction
- traceable across schema, data, contracts, policy, release, and runtime consequences

[Back to top](#migrations)

## Repo fit

**Path:** `migrations/README.md`  
**Role in repo:** README-like directory contract for migration-bearing changes.

### Repo fit summary

| Aspect | Guidance |
|---|---|
| **Path** | `migrations/README.md` |
| **Upstream context** | [Repo root][repo-root], [contracts][contracts-dir], [schemas][schemas-dir], [configs][configs-dir] |
| **Adjacent execution surfaces** | [scripts][scripts-dir], [infra][infra-dir], [tests][tests-dir], release and proof-pack emitters |
| **Primary audience** | Maintainers, reviewers, platform engineers, data engineers, stewards |
| **Authority posture** | Operational / supporting, not sovereign doctrine |
| **Update trigger** | Any migration path, cutover, compatibility seam, rollback, correction mechanism, or release-proof expectation change |

> [!NOTE]
> A March 20 master-design skeleton places `migrations/` beside `contracts/`, `tests/`, `scripts/`, `configs/`, and `infra/`. Treat that as a **documented target shape** until the mounted repo tree confirms current reality.

### Why this directory matters in KFM

Migration in KFM is constrained by earlier law:

- the canonical governed path must remain intact
- the trust membrane must stay intact
- authoritative truth must remain stronger than derived layers
- release trust must remain proof-bearing
- public surfaces must show honest negative states when a cutover fails, narrows scope, or is superseded later

That makes `migrations/` more than a convenience folder. It is where change seams become inspectable.

## Accepted inputs

The following belong here when they are part of **reviewable, governed migration work**.

| Input class | Examples | Why it belongs here | Minimum attached context |
|---|---|---|---|
| Schema and storage evolution | DDL, index changes, constraints, table/column additions, partition changes | Durable structure changed | plan, verification path, rollback posture |
| Data-preserving repair or backfill | backfills, crosswalks, ID remaps, temporal repairs, re-derived canonical fields | Existing governed state is transformed | source basis, validation, correction implications |
| Contract or envelope migration | payload/state changes, registry expansions, compatibility bridges, deprecation notes | Public/runtime meaning changes with storage or release behavior | contract delta, fixture updates, compatibility window |
| Policy or registry migration | reason-code additions, obligation-code changes, sensitivity/rule migrations | Runtime and release outcomes can change | policy diff, tests, review path |
| Compatibility seams and bridge notes | dual-read windows, dual-write windows, adapters, deprecation bridges | Temporary cutover controls need explicit stop rules | parity note, retirement plan, stop rule |
| Release or proof-pack transition material | cutover notes, release-manifest changes, projection freshness implications | Promotion and runtime trust are directly affected | proof-object expectations, post-deploy verify |
| Rollback / supersession / correction packets | rollback matrix, correction propagation notes, supersession plan | KFM requires visible recovery, not silent undo | correction path, affected surfaces, operator notes |
| Migration-local documentation | purpose, scope, change class, cutover steps, stop rules, verify steps | Reviewers need the “why,” not just the mechanism | README, plan, verification notes |

### Minimum bar for anything added here

A migration packet should make all of the following obvious:

1. what changed
2. whether the change is authoritative, derived, or both
3. which proof objects or fixtures changed with it
4. what the compatibility window is
5. what rollback or correction path exists
6. what users would see if the cutover fails, narrows scope, or is superseded later

## Exclusions

The following do **not** belong in `migrations/`.

| Exclusion | Why it stays out | Where it goes instead |
|---|---|---|
| Ad hoc analyst SQL | Not durable migration history | notebooks, scratch analysis, issue discussion |
| Free-standing orchestration helpers | Not every automation change is migration-bearing | [scripts][scripts-dir], tooling references, workflow configs |
| UI-only work with no trust-state change | Product work is not automatically migration work | app/package docs, surface-specific areas |
| Standalone policy prose with no executable impact | KFM policy must stay machine-checkable and testable | policy references, registries, contract/schema surfaces |
| Secrets, DSNs, and credentials | Never commit secret-bearing material | secret manager or local operator config |
| Generated dumps, backups, or exports | Recovery assets are not migration source | ops/recovery surfaces, release artifact storage |
| Derived-layer rebuild jobs with no trust-state seam | Rebuildable delivery is not canonical migration by default | scripts/orchestration or projection build surfaces |
| Silent overwrite utilities | KFM rejects “mutation without lineage” as a success condition | explicit correction or governed repair path |

## Current evidence boundary

The strongest fact about this surface in the current session is **what could and could not be verified**.

| Area | Current-session status | What is known | What remains unknown |
|---|---|---|---|
| Mounted workspace | **CONFIRMED** | The accessible workspace exposed the attached PDF corpus only. | Live repo checkout and file tree |
| Migration doctrine | **CONFIRMED** | March 2026 KFM manuals normalize migration as a governed, correction-bearing change class. | Exact repo implementation of that doctrine |
| Documentation family | **CONFIRMED** | KFM expects migration / rollback / correction / supersession manuals as an operational documentation class. | Exact repo-local documentation placement beyond this file |
| Continuity artifact for `migrations/` | **CONFIRMED** | One earlier compendium describes `migrations/` as schema/DB migration scripts. | Whether that narrower description still matches mounted repo reality |
| `migrations/` directory contents | **UNKNOWN** | None directly inspected | file inventory, naming conventions, runner choice |
| Schema / registry inventory | **UNKNOWN** | First-wave contract families and fixtures are strongly documented as needed | live schema files, valid/invalid fixtures, registry layout |
| CI / workflow coverage | **UNKNOWN** | Verification gates, proof-pack expectations, and rollback/correction drills are strong in doctrine | workflow YAML, required checks, branch protections |
| Runtime / release evidence depth | **UNKNOWN** | EvidenceBundle, RuntimeResponseEnvelope, ReleaseManifest / ReleaseProofPack, and CorrectionNotice are doctrinally central | emitted samples, resolver routes, trace joins, real rollback records |

### Practical consequence of the evidence boundary

This guide should describe:

- **what KFM migration means**
- **what belongs in this surface**
- **what must be reviewed with it**
- **how to verify repo reality before claiming implementation maturity**

It should **not** invent the live file inventory.

[Back to top](#migrations)

## Directory tree

### Evidence-safe minimum

```text
migrations/
└── README.md
```

That is the safest current-session assertion for this directory.

<details>
<summary>Illustrative future shape (PROPOSED, not current-session fact)</summary>

```text
migrations/
├── README.md
├── waves/
│   └── 0001_<slug>/
│       ├── README.md
│       ├── plan.md
│       ├── schema/
│       ├── fixtures/
│       ├── verify.md
│       ├── rollback.md
│       └── correction.md
├── drills/
│   └── <yyyymmdd>_<slug>/
│       ├── post-deploy-verification.md
│       └── correction-visibility.md
└── templates/
    └── migration-packet.md
```

Use a shape like this only if it matches the mounted repo’s actual execution model once the repository tree is directly available.
</details>

## Quickstart

Before documenting branch reality as fact, verify the branch.

```bash
# identify the exact revision under review
git rev-parse HEAD

# inspect the migration surface directly
git ls-files 'migrations/**' 2>/dev/null || true
find migrations -maxdepth 4 -type f 2>/dev/null | sort
find migrations -maxdepth 4 -type d 2>/dev/null | sort

# inspect adjacent surfaces likely to move with migration-bearing changes
find contracts schemas configs scripts infra tests -maxdepth 4 -type f 2>/dev/null | sort

# find trust objects and proof-bearing artifacts
git grep -nE 'SourceDescriptor|IngestReceipt|ValidationReport|DatasetVersion|CatalogClosure|DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|ProjectionBuildReceipt|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice' -- . 2>/dev/null

# find schema-style or file-based object names
git grep -nE 'source_descriptor|ingest_receipt|validation_report|dataset_version|catalog_closure|decision_envelope|review_record|release_manifest|release_proof_pack|projection_build_receipt|runtime_response_envelope|correction_notice' -- . 2>/dev/null

# find migration tooling and compatibility-seam language
git grep -nE 'migrat|rollback|supersed|withdraw|compatibility|dual-read|dual-write|deprecat|correction' -- . 2>/dev/null
```

### Review-first branch audit

```bash
# choose the review base explicitly (example: origin/main)
BASE_REF=origin/main

# see what the branch actually touches
git diff --name-only "$BASE_REF"...HEAD | sort

# narrow to likely migration-bearing surfaces
git diff --name-only "$BASE_REF"...HEAD | grep -E '^(migrations|contracts|schemas|configs|scripts|infra|tests|docs)/' || true
```

### Verify these before calling the branch “done”

1. Which exact files under `migrations/` exist today?
2. Which migration runner or mechanism is actually active?
3. Are valid and invalid fixtures present for the changed contract families?
4. What proof objects are emitted before and after promotion?
5. What post-deploy checks exist for rollback or correction?
6. Which public-safe surface shows release and correction state after cutover?

## Migration posture

### Core doctrine

| Rule | What it means here | Why it exists |
|---|---|---|
| Migration is broader than schema change | Schema, data, contracts, policy, release, runtime, and correction can all be migration-bearing. | Public trust can change without a table rename ever happening. |
| Preserve the canonical path | `Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` remains load-bearing. | KFM treats admissibility and promotion as structured transitions, not shortcuts. |
| Preserve the trust membrane | Public clients and normal UI surfaces stay behind governed APIs and evidence resolution. | Migration must not create “temporary” bypasses that become permanent. |
| Separate build, deploy, and promote | Deployment changes runtime placement; promotion changes trust state. | KFM docs explicitly reject collapsing deployment success into publishable trust. |
| Prefer staged, reversible change | Expand, compare, cut over, verify, then retire old seams deliberately. | Safer rollback, clearer review, less silent breakage. |
| Keep trust-significant change reviewable | Meaningful migration work should arrive as reviewable deltas with attached evidence, not silent background mutation. | Publication and later correction need inspectable lineage. |
| Make correction first-class | Rollback, supersession, withdrawal, and visible correction are part of migration design. | KFM rejects silent erase-and-move-on behavior. |
| Do not let compatibility seams fossilize | Dual-read, dual-write, bridges, and temporary envelopes need stop rules. | Temporary ambiguity becomes architectural debt fast. |

### Compatibility and deprecation rules

| Rule | Practical migration consequence |
|---|---|
| Outward-published contracts evolve additively by default | Breaking changes require explicit versioning, migration notes, and retests. |
| Route families stay durable at family level | Avoid documenting literal route trees as fact when the mounted repo is not directly surfaced. |
| Registries expand more safely than they mutate | Adding reason codes or runtime outcomes is usually safer than redefining old ones. |
| Trust objects stay stable and inspectable | `EvidenceBundle` and `RuntimeResponseEnvelope` semantics should not drift casually. |
| Standards/profile pins live elsewhere | This directory can reference compatibility burdens, but formal standards pins belong with schema/contract/configuration artifacts. |

### Recommended migration seams

| Seam type | When useful | Stop rule |
|---|---|---|
| Schema bridge | Old and new structure must coexist briefly | Remove once the new structure is the sole reviewed release path |
| Adapter / facade | Legacy implementation cannot change in the same release | Retire once governed outward contracts are the only supported path |
| Dual-read | Temporary parity comparison during cutover | End when parity or approved divergence is recorded |
| Dual-write | Bounded compatibility period with one authoritative side | Remove at first safe release after downstream cutover |
| Stale-visible shield | Derived layers lag approved release truth | Remove once projection freshness and release linkage are verified |
| Replacement chain / crosswalk | IDs, geometries, names, or boundaries change | Keep while published history or dependent integrations still need it |

> [!NOTE]
> A seam is a **temporary control surface**, not permission to keep ambiguity alive forever.

## Contracts & proof objects

KFM migration doctrine is unusually explicit about the object families that make governed change inspectable.

| Object family | Why it matters in migration | Current posture |
|---|---|---|
| `source_descriptor` | Source cadence, rights, validation burden, and publication intent must stay legible across replay or reprocessing. | **CONFIRMED family / UNKNOWN mounted schema** |
| `ingest_receipt` | Fetch integrity and replay basis must survive re-runs and backfills. | **CONFIRMED family / UNKNOWN mounted schema** |
| `validation_report` | Explains whether a migration candidate passes, quarantines, or fails. | **CONFIRMED family / UNKNOWN mounted schema** |
| `dataset_version` | Holds the authoritative processed result with stable identity. | **CONFIRMED family / UNKNOWN mounted schema** |
| `catalog_closure` | Keeps outward metadata, lineage, and discoverability coherent after change. | **CONFIRMED family / UNKNOWN mounted schema** |
| `decision_envelope` | Carries machine-readable policy result, reasons, and obligations. | **CONFIRMED family / UNKNOWN mounted schema** |
| `review_record` | Preserves human approval / denial and separation-of-duty evidence. | **CONFIRMED family / UNKNOWN mounted schema** |
| `release_manifest` / `release_proof_pack` | Explains what shipped and why promotion was allowed. | **CONFIRMED family / UNKNOWN mounted file** |
| `projection_build_receipt` | Proves derived map/tile/search freshness against approved release input. | **CONFIRMED family / UNKNOWN mounted file** |
| `EvidenceBundle` | Makes evidence drill-through operational instead of rhetorical. | **CONFIRMED family / UNKNOWN mounted resolver** |
| `runtime_response_envelope` | Makes ANSWER / ABSTAIN / DENY / ERROR behavior explicit at runtime. | **CONFIRMED family / UNKNOWN mounted file** |
| `correction_notice` | Preserves rollback, supersession, withdrawal, and correction lineage. | **CONFIRMED family / UNKNOWN mounted file** |

> [!NOTE]
> The attached corpus uses both doctrinal CamelCase names (for example `EvidenceBundle`) and schema-style snake_case object-family names. This guide preserves the local mix already present in this README draft rather than silently renaming object families before the mounted contracts are verified.

### Why these objects belong in a migration README

A migration in KFM is not “done” when the mechanism succeeds. It is done when later readers can reconstruct:

- what changed
- why it changed
- what policy or review path allowed it
- what released scope it affected
- what runtime or public surface had to change with it
- how rollback, supersession, or correction would propagate afterward

## Diagram

```mermaid
flowchart LR
    A[Classify migration<br/>schema / data / contract / policy / runtime] --> B[Prepare migration packet]
    B --> C[Update artifacts<br/>schemas • fixtures • notes • proofs]
    C --> D[Run gates<br/>schema • policy • catalog • release • runtime]
    D --> E{Promotion allowed?}

    E -- No --> Q[Hold / Quarantine / Revise]
    Q --> B

    E -- Yes --> F[Review + approval]
    F --> G[Deploy artifact<br/>without collapsing trust state]
    G --> H[Promote approved release]
    H --> I[Post-deploy verification<br/>smoke • canary • freshness • trust checks]
    I --> J{Trust preserved?}

    J -- Yes --> K[Release remains active]
    J -- No --> L[Rollback / Supersede / Withdraw / Correct]
    L --> M[Emit correction_notice<br/>and propagate visible state]

    subgraph Guardrails
      N[Canonical path preserved]
      O[Trust membrane preserved]
      P[Authoritative vs derived separation]
      R[Visible correction lineage]
    end

    B -.bounded by.-> N
    H -.bounded by.-> O
    I -.bounded by.-> P
    M -.bounded by.-> R
```

## Tables

### Change-class decision matrix

| Change class | Belongs here? | Review burden |
|---|---|---|
| Authoritative schema evolution | **Yes** | High; verify fixtures, compatibility, rollback |
| Data-preserving backfill tied to release behavior | **Yes** | High; validate lineage and correction implications |
| Contract / envelope migration | **Yes** | High; additive evolution, versioning, surface-state implications |
| Policy / registry migration affecting runtime outcomes | **Yes** | High; tests, review path, reason/obligation stability |
| Projection-only rebuild with no trust-state seam | **Usually no** | Keep in projection/build surfaces unless part of governed cutover |
| UI-only refactor with unchanged trust behavior | **No** | Keep with app/surface docs |
| Ad hoc repair SQL | **No** | Not durable governed migration history |
| Backups, dumps, exports | **No** | Recovery or release artifacts, not migration source |

### Companion artifacts by change class

| Change class | Usually review with |
|---|---|
| Schema / storage | migration plan, schema diff, fixture changes, rollback posture |
| Data / backfill | source basis, parity or reconciliation note, correction path |
| Contract / envelope | schema or OpenAPI diff, compatibility window, negative-state tests |
| Policy / registry | reason/obligation diff, fixtures, deny/generalize/review-required tests |
| Release / promotion | candidate/release proof pack, post-deploy verify, visibility-state review |
| Runtime / surface trust | envelope diff, evidence-drill-through test, stale/superseded/withdrawn cues |

### Review matrix

| Review question | Why it matters |
|---|---|
| Does this change canonical truth, derived delivery, or both? | Prevents quiet authority drift |
| Which proof objects must change with it? | Migration without evidence is only half governed |
| Is the change additive, bridged, or breaking? | Determines compatibility and rollback posture |
| What must remain immutable? | Protects identity, lineage, and replayability |
| What is the stop rule for any seam introduced? | Prevents temporary bridges from becoming architecture |
| What visible state reaches users if the cutover fails? | Public surfaces must not bluff trust |
| Is rollback enough, or is correction / supersession needed? | Some post-publication states cannot be “undone” silently |
| Did docs, diagrams, fixtures, and runbooks change with behavior? | Documentation is part of the governed system |

## Task list / Definition of done

A migration change should not be called complete until the following are true.

- [ ] The migration class is named clearly: schema, data, contract, policy, release, runtime, or correction-bearing.
- [ ] Preconditions, compatibility seams, and stop rules are documented.
- [ ] The canonical path and trust membrane remain intact.
- [ ] Build, deploy, and promote are not collapsed into one unreviewed step.
- [ ] Authoritative and derived layers remain distinct.
- [ ] Required proof objects and fixture updates are named.
- [ ] Validation gates are named and runnable.
- [ ] Rollback, supersession, withdrawal, or correction posture is explicit.
- [ ] Public-facing stale, generalized, withheld, superseded, or withdrawn states are handled where relevant.
- [ ] Related contracts, schemas, configs, scripts, docs, and tests are linked when behavior changes.
- [ ] The branch remains reviewable to a maintainer who did not author the change.

### Stronger definition of done for the first real rehearsal

For the first governed rehearsal, KFM’s current corpus keeps converging on a **hydrology-first** proof lane. That rehearsal is only “done” when one slice proves:

```text
source_descriptor
-> ingest_receipt
-> validation_report
-> dataset_version
-> catalog_closure
-> decision_envelope / review_record
-> release_manifest or release_proof_pack
-> projection_build_receipt
-> EvidenceBundle-backed detail view
-> runtime_response_envelope
-> correction_notice drill
```

### PR-ready review packet

A non-trivial migration PR should include, at minimum:

- purpose and scope
- evidence label summary (`CONFIRMED` / `INFERRED` / `PROPOSED` / `UNKNOWN`)
- proof objects changed or added
- compatibility window and stop rule, if any seam is introduced
- rollback / correction path
- docs updates, or explicit rationale for none
- tests / fixtures added or updated
- operational impact notes if runtime behavior changes

[Back to top](#migrations)

## FAQ

### Is `migrations/` only for database work?

No. In the current KFM corpus, migration is explicitly broader than database schema change. It includes data repair and backfill, contract and envelope evolution, policy and registry change, release/promotion consequences, runtime trust behavior, and post-publication correction or supersession.

### Why is this guide broader than “schema/DB migration scripts”?

Because later replacement-grade KFM manuals widened migration into a governed change discipline tied to proof objects, release state, rollback, and visible correction. An earlier continuity artifact still describes `migrations/` in the narrower schema/DB sense, but that older description is not strong enough to serve as the redesign baseline on its own.

### Why is this guide more cautious than a typical migrations README?

Because the current session did not expose the live repository tree. The attached March 2026 KFM manuals are strong on doctrine and target-state structure, but they do **not** directly prove current migration files, runner choice, workflow inventory, or deployment manifests in this run.

### Why keep rollback and correction so close together?

Because KFM treats rollback as an evidence-bearing reverse transition, not silent deletion. Some failures can be corrected by reverting to an earlier approved identity; others require supersession, withdrawal, generalized output, or visible correction notices.

### Why prefer additive change and temporary bridges?

Because the corpus favors reversible seams over surprise replacement. Add, compare, verify, cut over, then retire old paths deliberately. That is safer for both public trust and operator recovery.

### Why keep hydrology as the first rehearsal?

Because the current corpus repeatedly treats hydrology as the safest first governed slice: public-safe enough for visible proof, rich in place/time/evidence linkage, and strong enough to exercise release, runtime, and correction behavior end to end.

## Appendix — verification notes

<details>
<summary>Open verification questions</summary>

1. What concrete files already live under `migrations/` in the mounted repo?
2. Which runner or mechanism is actually used for migration-bearing changes?
3. Which first-wave schemas and valid/invalid fixtures already exist on disk?
4. Which CI checks block promotion for migration-bearing PRs?
5. What emitted proof objects already exist versus only being documented?
6. Is there a mounted `EvidenceBundle` resolver and `RuntimeResponseEnvelope` path?
7. What restore, rollback, supersession, or correction drills have actually been exercised?
8. Which Kansas lane is closest to a real migration rehearsal beyond doctrine?
9. Does the current repo still follow the earlier schema/DB-only description of `migrations/`, or has it fully adopted the broader replacement-grade contract?
</details>

<details>
<summary>Illustrative migration packet header (PROPOSED)</summary>

```text
id: <migration-id>
class: schema | data | contract | policy | release | runtime | correction
purpose: <one-sentence statement>
authoritative_scope: <what authoritative state changes>
derived_scope: <what derived layers must rebuild or warn>
compatibility_window: <none | bounded window>
proof_objects: <list>
verification: <tests / reports / parity checks>
rollback: <revert | fail-forward | supersede | withdraw>
correction_path: <how visible correction propagates>
affected_surfaces: <map | detail | export | focus | API>
notes: <assumptions / open unknowns>
```
</details>

<details>
<summary>What should be surfaced next before claiming implementation maturity</summary>

- live repo tree and top-level manifests
- actual `migrations/` inventory
- mounted schema files plus valid/invalid fixtures
- workflow / CI inventory and required checks
- deployment descriptors or service manifests
- one emitted release proof pack
- one `EvidenceBundle` resolver trace
- one `RuntimeResponseEnvelope` sample
- one restore drill and one visible correction drill record
</details>

## Reference links

[repo-root]: ../README.md
[contracts-dir]: ../contracts/
[schemas-dir]: ../schemas/
[configs-dir]: ../configs/
[infra-dir]: ../infra/
[scripts-dir]: ../scripts/
[tests-dir]: ../tests/

[Back to top](#migrations)
