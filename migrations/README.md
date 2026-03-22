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
related: [../README.md, ../contracts/README.md, ../schemas/README.md, ../scripts/README.md, ../tests/README.md, ../policy/README.md, ../.github/workflows/README.md, NEEDS-VERIFICATION:../configs/, NEEDS-VERIFICATION:../infra/]
tags: [kfm, migrations, storage-evolution]
notes: [freshest repo-state signal for this draft is indirect and comes from the 2026-03-22 repo-grounded sprint; it confirms adjacent doc surfaces and missing gates, but does not confirm a live migrations inventory, owners, or metadata values]
[/KFM_META_BLOCK_V2] -->

# `migrations`

Deterministic, reviewable storage and trust-state evolution for Kansas Frontier Matrix.

> **Status:** experimental  
> **Document lifecycle:** draft  
> **Authority posture:** operational / supporting  
> **Owners:** **NEEDS VERIFICATION**  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![lifecycle](https://img.shields.io/badge/lifecycle-draft-lightgrey) ![authority](https://img.shields.io/badge/authority-operational-blue) ![surface](https://img.shields.io/badge/surface-migrations-6f42c1) ![repo signal](https://img.shields.io/badge/repo%20signal-2026--03--22-blueviolet) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current repo signal](#current-repo-signal) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Migration posture](#migration-posture) · [Contracts & proof objects](#contracts--proof-objects) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix--verification-notes)

> [!IMPORTANT]
> This guide is intentionally **evidence-bounded**. The strongest repo-state signal available to this draft is a fresh repo-grounded research sprint, not a mounted checkout in the current session. That sprint confirms adjacent documentation surfaces and several missing enforcement pieces, but it does **not** confirm a live `migrations/` inventory, runner choice, or file naming convention. Keep all implementation claims proportional.

> [!WARNING]
> In KFM, migration is **not** just “run the database script.” The March 2026 replacement-grade manual family treats migration as a governed change problem that can affect schema, data, contracts, policy, release state, runtime trust behavior, rollback, supersession, withdrawal, and visible correction.

## Scope

`migrations/` is the directory contract for **governed change** to durable KFM structures and trust-bearing artifacts.

That includes database work, but it is intentionally broader. In the March 2026 replacement-grade manuals, migration spans schema change, data repair and backfill, contract and envelope evolution, policy and registry change, release and promotion consequences, compatibility seams, rollback, supersession, withdrawal, and visible correction.

> [!NOTE]
> **Baseline determination.** This guide treats the March 20–21 replacement-grade KFM manual family as the doctrinal baseline. A March 6 compendium still described `migrations/` more narrowly as **DB migration scripts**. That earlier description is preserved here as a continuity signal, but not as the whole migration contract.

### Truth markers used in this guide

| Marker | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by the attached KFM corpus or by fresh repo-grounded evidence visible in this session |
| **INFERRED** | Strongly implied by the corpus, but not directly verified as mounted repo/runtime reality |
| **PROPOSED** | Recommended target-state shape consistent with the corpus, not verified as current implementation |
| **UNKNOWN** | Not supported strongly enough in the current session to present as settled fact |
| **NEEDS VERIFICATION** | Explicit placeholder or repo-specific fact that should be checked before merge |

### Directory contract at a glance

| Item | Status | What that means |
|---|---|---|
| Migration in KFM is broader than schema-only change | **CONFIRMED** | Replacement-grade KFM doctrine treats migration as part of release, rollback, correction, and runtime trust behavior. |
| `migrations/` is a documented target surface in earlier KFM structure docs | **CONFIRMED** | The March 6 compendium lists `migrations/` among target modules and describes it as a DB-migrations surface. |
| Fresh repo-state evidence confirms a live `migrations/` inventory | **UNKNOWN** | The 2026-03-22 repo-grounded sprint confirms adjacent doc surfaces, but does not confirm `migrations/` contents. |
| Concrete runner, naming convention, and rollback scripts | **UNKNOWN** | No mounted branch inventory was available in this session. |
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
| **Confirmed upstream docs** | [Repo root][repo-root], [contracts][contracts-readme], [schemas][schemas-readme], [scripts][scripts-readme], [tests][tests-readme], [policy][policy-readme], [workflow scaffolding][workflows-readme] |
| **Documented but not current-session confirmed nearby surfaces** | `../configs/`, `../infra/` |
| **Primary audience** | Maintainers, reviewers, platform engineers, data engineers, stewards |
| **Authority posture** | Operational / supporting, not sovereign doctrine |
| **Update trigger** | Any migration path, cutover, compatibility seam, rollback, correction mechanism, or release-proof expectation change |

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
| Free-standing orchestration helpers | Not every automation change is migration-bearing | [scripts][scripts-readme], tooling references, workflow configs |
| UI-only work with no trust-state change | Product work is not automatically migration work | app/package docs, surface-specific areas |
| Standalone policy prose with no executable impact | KFM policy must stay machine-checkable and testable | [policy][policy-readme], registries, contract/schema surfaces |
| Secrets, DSNs, and credentials | Never commit secret-bearing material | secret manager or local operator config |
| Generated dumps, backups, or exports | Recovery assets are not migration source | ops/recovery surfaces, release artifact storage |
| Derived-layer rebuild jobs with no trust-state seam | Rebuildable delivery is not canonical migration by default | scripts/orchestration or projection build surfaces |
| Silent overwrite utilities | KFM rejects mutation without lineage as a success condition | explicit correction or governed repair path |

## Current repo signal

The freshest repo-state signal available to this draft is a March 22, 2026 repo-grounded sprint. It is stronger than the earlier structural compendium for **current repo status**, but weaker than a mounted checkout because the current session did not expose the branch tree directly.

### What that means for this README

| Signal | Status | Practical consequence |
|---|---|---|
| Adjacent documentation surfaces exist in the repo | **CONFIRMED** | `contracts/README.md`, `schemas/README.md`, `scripts/README.md`, `tests/README.md`, `policy/README.md`, and `.github/workflows/README.md` are live doc surfaces to link to and coordinate with. |
| Active merge-blocking workflow YAML gate is present | **CONFIRMED absent in reviewed repo artifacts** | Do not write this README as if schema or policy gates already block merges automatically. |
| Concrete schema inventory exists as real schema files | **CONFIRMED missing in reviewed repo artifacts** | Migration packets should identify required schemas and fixtures explicitly instead of assuming they already exist. |
| Fixture-backed validation harness is present | **CONFIRMED missing in reviewed repo artifacts** | Migration definition of done should include fixture and gate work, not only the migration mechanism. |
| `migrations/` exists as a live repo directory with inventory | **NEEDS VERIFICATION** | Keep the directory contract, but verify branch reality before claiming presence or specific contents. |
| Runner choice, naming convention, rollback scripts, drill records | **UNKNOWN** | Verify with branch inspection before merge or release. |

> [!IMPORTANT]
> The same repo-grounded sprint argues that the **highest-value next step** is still the first merge-blocking contracts gate, not broad downstream expansion. For migration work, that means honesty about whether contract, schema, and policy validation are manual, planned, or already enforced.

[Back to top](#migrations)

## Directory tree

### Safest current-session shape

```text
migrations/
└── README.md   # this document; PROPOSED until merged
```

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

# inspect whether migrations/ exists and what it contains
git ls-files 'migrations/**' 2>/dev/null || true
find migrations -maxdepth 4 -type f 2>/dev/null | sort
find migrations -maxdepth 4 -type d 2>/dev/null | sort

# inspect already-confirmed adjacent doc surfaces
git ls-files '.github/workflows/**' 'contracts/**' 'schemas/**' 'scripts/**' 'tests/**' 'policy/**' | sort

# find trust objects and proof-bearing artifacts
git grep -nE 'SourceDescriptor|IngestReceipt|ValidationReport|DatasetVersion|CatalogClosure|DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|ProjectionBuildReceipt|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice' -- . 2>/dev/null

# find migration tooling and compatibility-seam language
git grep -nE 'migrat|rollback|supersed|withdraw|compatibility|dual-read|dual-write|deprecat|correction' -- . 2>/dev/null

# inspect whether active workflow YAML files exist yet
git ls-files '.github/workflows/*.yml' '.github/workflows/*.yaml' | sort
```

### Review-first branch audit

```bash
# choose the review base explicitly (example: origin/main)
BASE_REF=origin/main

# see what the branch actually touches
git diff --name-only "$BASE_REF"...HEAD | sort

# narrow to likely migration-bearing surfaces
git diff --name-only "$BASE_REF"...HEAD \
  | grep -E '^(migrations|contracts|schemas|policy|scripts|tests|docs|\.github/workflows)/' || true
```

### Verify these before calling the branch “done”

1. Does `migrations/` already exist on the branch, or is this PR introducing it?
2. Which migration runner or mechanism is actually active?
3. Are valid and invalid fixtures present for the changed contract families?
4. What proof objects are emitted before and after promotion?
5. What post-deploy checks exist for rollback or correction?
6. Which public-safe surface shows release and correction state after cutover?

## Usage

Treat this directory as a **review surface**, not only as a script bucket.

1. **Classify the change.** Name it: schema, data, contract, policy, release, runtime, or correction-bearing.
2. **Assemble the packet.** Pair the migration mechanism with notes, fixtures, and proof-object expectations.
3. **Declare the seam.** State the compatibility window, dual-read/dual-write plan, and the stop rule.
4. **Run the gates.** Record schema, policy, validation, release, and post-deploy checks honestly.
5. **Close the loop.** Retire the seam deliberately or emit rollback, supersession, withdrawal, or correction artifacts.

> [!NOTE]
> A migration PR that cannot identify its proof objects, stop rule, and correction path is not ready, even if the underlying script is short.

## Migration posture

### Core doctrine

| Rule | What it means here | Why it exists |
|---|---|---|
| Migration is broader than schema change | Schema, data, contracts, policy, release, runtime, and correction can all be migration-bearing. | Public trust can change without a table rename ever happening. |
| Preserve the canonical path | `Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` remains load-bearing. | KFM treats admissibility and promotion as structured transitions, not shortcuts. |
| Preserve the trust membrane | Public clients and normal UI surfaces stay behind governed APIs and evidence resolution. | Migration must not create “temporary” bypasses that become permanent. |
| Separate build, deploy, and promote | Deployment changes runtime placement; promotion changes trust state. | KFM doctrine rejects collapsing deployment success into publishable trust. |
| Prefer staged, reversible change | Expand, compare, cut over, verify, then retire old seams deliberately. | Safer rollback, clearer review, less silent breakage. |
| Keep trust-significant change reviewable | Meaningful migration work should arrive as reviewable deltas with attached evidence, not silent background mutation. | Publication and later correction need inspectable lineage. |
| Make correction first-class | Rollback, supersession, withdrawal, and visible correction are part of migration design. | KFM rejects silent erase-and-move-on behavior. |
| Do not let compatibility seams fossilize | Dual-read, dual-write, bridges, and temporary envelopes need stop rules. | Temporary ambiguity becomes architectural debt fast. |

### Compatibility and deprecation rules

| Rule | Practical migration consequence |
|---|---|
| Outward-published contracts evolve additively by default | Breaking changes require explicit versioning, migration notes, and retests. |
| Registries expand more safely than they mutate | Adding reason codes or runtime outcomes is usually safer than redefining old ones. |
| Trust objects stay stable and inspectable | `EvidenceBundle` and `RuntimeResponseEnvelope` semantics should not drift casually. |
| Standards/profile pins live elsewhere | This directory can reference compatibility burdens, but formal standards pins belong with schema, contract, or configuration artifacts. |
| Deprecation needs a visible end state | Sunset language should name the replacement path, compatibility window, and final retirement condition. |

### Recommended migration seams

| Seam type | When useful | Stop rule |
|---|---|---|
| Schema bridge | Old and new structure must coexist briefly | Remove once the new structure is the sole reviewed release path |
| Adapter / facade | Legacy implementation cannot change in the same release | Retire once governed outward contracts are the only supported path |
| Dual-read | Temporary parity comparison during cutover | End when parity or approved divergence is recorded |
| Dual-write | Bounded compatibility period with one authoritative side | Remove at first safe release after downstream cutover |
| Stale-visible shield | Derived layers lag approved release truth | Remove once projection freshness and release linkage are verified |
| Replacement chain / crosswalk | IDs, geometries, names, or boundaries change | Keep while published history or dependent integrations still need it |

## Contracts & proof objects

KFM migration doctrine is unusually explicit about the object families that make governed change inspectable.

| Object family | Why it matters in migration | Current posture |
|---|---|---|
| `source_descriptor` | Source cadence, rights, validation burden, and publication intent must stay legible across replay or reprocessing. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `ingest_receipt` | Fetch integrity and replay basis must survive re-runs and backfills. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `validation_report` | Explains whether a migration candidate passes, quarantines, or fails. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `dataset_version` | Holds the authoritative processed result with stable identity. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `catalog_closure` | Keeps outward metadata, lineage, and discoverability coherent after change. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `decision_envelope` | Carries machine-readable policy result, reasons, and obligations. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `review_record` | Preserves human approval / denial and separation-of-duty evidence. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `release_manifest` / `release_proof_pack` | Explains what shipped and why promotion was allowed. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `projection_build_receipt` | Proves derived map/tile/search freshness against approved release input. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `EvidenceBundle` | Makes evidence drill-through operational instead of rhetorical. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `runtime_response_envelope` | Makes `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior explicit at runtime. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |
| `correction_notice` | Preserves rollback, supersession, withdrawal, and correction lineage. | **CONFIRMED family / NEEDS VERIFICATION in mounted repo** |

> [!NOTE]
> The attached corpus uses both doctrinal CamelCase names (for example `EvidenceBundle`) and schema-style snake_case object-family names. This guide keeps that local mix rather than silently normalizing names before the mounted contracts are verified.

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
    B --> C[Update companion artifacts<br/>schemas • fixtures • policy diffs • notes]
    C --> D[Run gates<br/>schema • policy • validation • release]
    D --> E{Candidate passes?}

    E -- No --> Q[Hold / Quarantine / Revise]
    Q --> B

    E -- Yes --> F[Review + approval]
    F --> G[Deploy artifact<br/>without collapsing trust state]
    G --> H[Promote approved release]
    H --> I[Post-deploy verification<br/>smoke • canary • freshness • trust checks]
    I --> J{Trust preserved?}

    J -- Yes --> K[Retire seam deliberately]
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

Above: a governed migration flow in which change is paired with schema and fixture updates, review, promotion, post-deploy verification, and explicit correction lineage.

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

- [ ] Branch inventory confirms whether `migrations/` already existed or is being introduced in this PR.
- [ ] The migration class is named clearly: schema, data, contract, policy, release, runtime, or correction-bearing.
- [ ] Preconditions, compatibility seams, and stop rules are documented.
- [ ] The canonical path and trust membrane remain intact.
- [ ] Build, deploy, and promote are not collapsed into one unreviewed step.
- [ ] Authoritative and derived layers remain distinct.
- [ ] Required proof objects and fixture updates are named.
- [ ] Validation gates are named and runnable, or explicitly marked manual if not yet enforced.
- [ ] If contracts, schemas, or policy meanings changed, corresponding fixtures or validator work is attached or explicitly called out as missing.
- [ ] Rollback, supersession, withdrawal, or correction posture is explicit.
- [ ] Public-facing stale, generalized, withheld, superseded, or withdrawn states are handled where relevant.
- [ ] Related contracts, schemas, scripts, tests, policy docs, and workflow notes are linked when behavior changes.
- [ ] The branch remains reviewable to a maintainer who did not author the change.

### Readiness gate before broad migration expansion

The freshest repo-grounded signal still points to a docs-first repo with missing executable merge gates. Until that changes, broad migration work should also satisfy these conditions:

- [ ] The first-wave contract or schema validator path is identified.
- [ ] Policy bundle expectations are explicit for allow, deny, generalize, review-required, and correction-bearing outcomes.
- [ ] Candidate versus release proof-pack expectations are named.
- [ ] This README does not imply mounted automation that the repo does not yet prove.

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

No. In the current KFM corpus, migration is explicitly broader than database schema change. It includes data repair and backfill, contract and envelope evolution, policy and registry change, release and promotion consequences, runtime trust behavior, and post-publication correction or supersession.

### Is `migrations/` already confirmed in the live repo?

Not from the evidence available in this session. An earlier structural compendium documents `migrations/` as a target surface, but the freshest repo-grounded sprint did not confirm a live `migrations/` inventory. Treat the path as **NEEDS VERIFICATION** until branch inspection proves it.

### Why is this guide broader than “schema/DB migration scripts”?

Because later replacement-grade KFM manuals widened migration into a governed change discipline tied to proof objects, release state, rollback, and visible correction. The older schema/DB-only description remains useful as continuity, but it is too narrow to function as the redesign baseline by itself.

### Why is this guide more cautious than a typical migrations README?

Because the current session did not expose the live repository tree directly. The March 2026 KFM manuals are strong on doctrine and target-state structure, and the March 22 repo-grounded sprint is strong on current repo signals, but neither source directly proves a mounted `migrations/` file inventory here.

### Why keep rollback and correction so close together?

Because KFM treats rollback as an evidence-bearing reverse transition, not silent deletion. Some failures can be corrected by reverting to an earlier approved identity; others require supersession, withdrawal, generalized output, or visible correction notices.

### What should the first serious migration prove?

Not only that the underlying change works, but that KFM can attach schemas, fixtures, policy decisions, release evidence, runtime trust behavior, and correction lineage to the change without bluffing maturity it does not yet have.

## Appendix — verification notes

<details>
<summary>Open verification questions</summary>

1. What concrete files already live under `migrations/` in the mounted repo?
2. Which runner or mechanism is actually used for migration-bearing changes?
3. Are there any live migration files, or only documentation and placeholders?
4. Which first-wave schemas and valid/invalid fixtures already exist on disk?
5. Which CI checks block promotion for migration-bearing PRs?
6. What emitted proof objects already exist versus only being documented?
7. Is there a mounted `EvidenceBundle` resolver and `RuntimeResponseEnvelope` path?
8. What restore, rollback, supersession, or correction drills have actually been exercised?
9. Does the current repo still follow the earlier schema/DB-only description of `migrations/`, or has it already adopted the broader replacement-grade contract?

</details>

<details>
<summary>Illustrative migration packet header (PROPOSED)</summary>

```yaml
id: <migration-id>
class: schema | data | contract | policy | release | runtime | correction
purpose: <one-sentence statement>
authoritative_scope: <what authoritative state changes>
derived_scope: <what derived layers must rebuild or warn>
compatibility_window: <none | bounded window>
proof_objects:
  - <object-family>
verification:
  - <tests / reports / parity checks>
rollback: <revert | fail-forward | supersede | withdraw>
correction_path: <how visible correction propagates>
affected_surfaces:
  - <map | detail | export | focus | api>
notes:
  - <assumptions / open unknowns>
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
[contracts-readme]: ../contracts/README.md
[schemas-readme]: ../schemas/README.md
[scripts-readme]: ../scripts/README.md
[tests-readme]: ../tests/README.md
[policy-readme]: ../policy/README.md
[workflows-readme]: ../.github/workflows/README.md

[Back to top](#migrations)
