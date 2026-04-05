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
tags: [kfm, migrations, storage-evolution, proof-objects]
notes: [target path inferred from the uploaded draft; strongest repo-state signal available to this revision is the 2026-04-03 successor geospatial manual with direct public-main repo-root and .github gatehouse evidence; no mounted checkout, migrations inventory, owners, or metadata dates were directly reverified in this session]
[/KFM_META_BLOCK_V2] -->

# migrations

Governed change control for durable KFM state, contracts, release seams, and correction lineage.

> **Status:** experimental  
> **Document lifecycle:** draft  
> **Authority posture:** supporting directory contract  
> **Owners:** **NEEDS VERIFICATION**  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![lifecycle](https://img.shields.io/badge/lifecycle-draft-lightgrey) ![authority](https://img.shields.io/badge/authority-supporting%20directory%20contract-blue) ![repo%20signal](https://img.shields.io/badge/repo%20signal-2026--04--03-blueviolet) ![surface](https://img.shields.io/badge/surface-migrations-6f42c1) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current public-main signal](#current-public-main-signal) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Migration posture](#migration-posture) · [Contracts & proof objects](#contracts--proof-objects) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix--verification-notes)

> [!IMPORTANT]
> This README is intentionally **evidence-bounded**. The strongest repo-state signal available to this revision is the **2026-04-03 successor geospatial manual**, which documents direct inspection of the public-main repo root and `.github` gatehouse. That is stronger than the earlier PDF-only boundary, but it is still **not** a mounted checkout of the branch under review.

> [!WARNING]
> In KFM, migration is not just “run the database script.” A migration can change storage, contracts, policy behavior, release state, derived rebuild obligations, runtime trust behavior, rollback posture, or visible correction lineage.

> [!NOTE]
> **Baseline determination.** This README treats the uploaded draft as the redesign baseline and updates it against the stronger attached doctrinal layer: the replacement-grade master-reference posture, the 2026-04-03 geospatial successor manual, the Pass 10 category atlas, and the MapLibre shell doctrine. Public-main repo evidence is used for visible path and gatehouse claims only.

## Scope

`migrations/` is the directory contract for **governed change** to durable KFM structures and trust-bearing artifacts.

That includes schema and storage work, but it is intentionally broader. In the strongest attached KFM doctrine, migration spans schema evolution, data repair and backfill, contract and envelope changes, policy and registry changes, release and promotion consequences, projection rebuilds tied to released scope, rollback, supersession, withdrawal, and visible correction.

### Truth markers used in this guide

| Marker | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by the attached KFM corpus or by the strongest repo-grounded public-main evidence visible in this session |
| **INFERRED** | Strongly implied by the corpus, but not directly reverified as mounted branch or runtime reality |
| **PROPOSED** | Recommended target-state shape or workflow consistent with doctrine, but not verified as current implementation |
| **UNKNOWN** | Not supported strongly enough in the current session to present as settled fact |
| **NEEDS VERIFICATION** | Explicit placeholder or repo-specific fact that should be checked on the actual branch before merge |

### What this directory is for

This surface should make migration work:

- reviewable
- staged and reversible
- explicit about compatibility seams
- linked to proof objects
- honest about rollback, supersession, withdrawal, and correction
- traceable across schema, data, contracts, policy, release, and runtime consequences

### What migration must preserve

| Invariant | Why it matters here |
|---|---|
| `Source -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` | Migration must not shortcut the canonical truth path. |
| Trust membrane | Public and normal UI surfaces still go through governed APIs, policy evaluation, and evidence resolution. |
| Authoritative vs derived split | Search, graph, vector, tile, scene, cache, and summary layers stay rebuildable unless explicitly promoted. |
| Promotion as governed state change | Deployment success is not enough; publication requires release and proof state. |
| Visible correction lineage | Rollback, supersession, withdrawal, narrowing, and replacement must remain inspectable. |

[Back to top](#migrations)

## Repo fit

**Path:** `migrations/README.md`  
**Role in repo:** README-like directory contract for migration-bearing change.

### Repo fit summary

| Aspect | Guidance |
|---|---|
| **Path** | `migrations/README.md` |
| **Primary audience** | Maintainers, platform engineers, data engineers, reviewers, and stewards |
| **Repo fit** | This README governs how migration-bearing work should be packaged, reviewed, and verified without overclaiming mounted automation |
| **Upstream dependencies** | contracts, schemas, policy bundles, fixtures, review logic, release state, and proof-object conventions |
| **Downstream consequences** | release manifests, projection rebuilds, exports, `EvidenceBundle` resolution, `RuntimeResponseEnvelope` behavior, and correction visibility |
| **Update trigger** | Any change to authoritative storage, contracts, policy meaning, proof objects, promotion rules, or correction behavior |
| **Adjacent links** | [repo root][repo-root] · [contracts][contracts-readme] · [schemas][schemas-readme] · [scripts][scripts-readme] · [tests][tests-readme] · [policy][policy-readme] · [workflow docs][workflows-readme] |
| **Link posture** | Relative links are kept because the draft already positions this file as a directory README; exact branch presence of each linked README should still be rechecked before merge |

### Why this directory matters in KFM

Migration in KFM is constrained by earlier law:

- the canonical path must remain intact
- the trust membrane must remain intact
- authoritative truth must remain stronger than derived layers
- public-safe release must remain proof-bearing
- users must see honest states when a cutover fails, narrows scope, is generalized, becomes stale, or is superseded later

That makes `migrations/` more than a convenience folder. It is where change seams become inspectable.

## Accepted inputs

The following belong here when they are part of **reviewable, governed migration work**.

| Input class | Examples | Why it belongs here | Minimum companion context |
|---|---|---|---|
| Schema and storage evolution | DDL, indexes, constraints, partition changes, canonical table/view changes | Durable structure changed | plan, verify path, rollback posture |
| Data repair and backfill | ID remaps, canonical field repair, temporal correction, replay, reconciliation | Existing governed state is transformed | source basis, validation, correction implications |
| Contract or envelope migration | object shape changes, additive fields, runtime envelope shifts, deprecation bridges | Public/runtime meaning changes | contract delta, compatibility window, fixture updates |
| Policy or registry migration | reason-code additions, obligation-code changes, publication-class shifts | Runtime and release outcomes can change | policy diff, tests, steward review path |
| Release and cutover notes | promotion effects, projection rebuild expectations, stale-state handling | Deployment and publication must stay distinct | release notes, post-deploy verify, rollback/correction note |
| Compatibility seams | dual-read, dual-write, adapters, bridge layers, temporary facades | Temporary ambiguity must be bounded and retired | stop rule, parity note, removal plan |
| Correction packets | rollback, supersession, withdrawal, narrowing, replacement notices | KFM requires visible recovery, not silent overwrite | affected surfaces, public note, rebuild refs |
| Migration-local documentation | packet README, plan, verify steps, rollback runbook | Reviewers need intent and operator guidance | concise purpose, scope, gates, open unknowns |

### Minimum bar for anything added here

A migration packet should make all of the following obvious:

1. what changed
2. whether the change touches authoritative state, derived state, or both
3. which proof objects or fixtures changed with it
4. what the compatibility window is
5. what the rollback or correction path is
6. what users would see if the change fails, narrows scope, or is superseded later

## Exclusions

The following do **not** belong in `migrations/`.

| Exclusion | Why it stays out | Where it goes instead |
|---|---|---|
| Ad hoc analyst SQL | Not durable governed migration history | notebooks, scratch analysis, issue discussion |
| Free-standing helper scripts | Not every automation change is migration-bearing | [scripts][scripts-readme], tooling docs |
| UI-only work with no trust-state seam | Product work is not automatically migration work | app or surface docs |
| Standalone policy prose with no executable consequence | KFM policy must stay machine-checkable and testable | [policy][policy-readme], registries, contract or schema surfaces |
| Duplicate copies of canonical schemas | `migrations/` should reference the authoritative schema home, not create a shadow schema tree | chosen schema home (`contracts/`, `schemas/`, or ADR-backed replacement) |
| Emitted receipts or proof bundles copied for convenience | Review packets may link proofs, but canonical emitted artifacts should stay in their governed storage location | receipt/provenance storage or release artifact location |
| Secrets, DSNs, credentials | Never commit secret-bearing material | secret manager or local operator config |
| Generated dumps, backups, exports | Recovery assets are not migration source | recovery or release artifact storage |
| Projection rebuilds with no release seam | Rebuildable delivery is not canonical migration by default | projection/build surfaces |
| Silent overwrite utilities | KFM rejects mutation without lineage as a success condition | explicit correction or governed repair path |

## Current public-main signal

The strongest repo-state signal available in this session is no longer the older repo-grounded sprint alone. The attached 2026-04-03 successor geospatial manual adds **direct public-main repo-root and `.github` gatehouse evidence**, while still keeping non-public or runtime claims explicitly bounded.

### What that means for this README

| Signal | Current status | Practical consequence |
|---|---|---|
| Root README frames KFM as governed, evidence-first, map-first, time-aware, and experimental | **CONFIRMED** | Keeping this README in an evidence-bounded, trust-visible posture matches the visible repo identity. |
| Public-main root tree visibly includes `apps/`, `contracts/`, `data/`, `docs/`, `infra/`, `packages/`, `policy/`, `schemas/`, `tests/`, `tools/`, and a substantial `.github/` gatehouse | **CONFIRMED** | This README can safely speak about those visible repo surfaces without pretending the whole branch tree is mounted here. |
| Public-main `.github/actions/` visibly includes `metadata-validate-v2`, `metadata-validate`, `opa-gate`, `provenance-guard`, and `sbom-produce-and-sign` lanes | **CONFIRMED** | Migration guidance can name metadata, policy, provenance, and SBOM pressure as real gatehouse themes. |
| `.github/workflows/` and `.github/watchers/` are README-only on current public main | **CONFIRMED** | Do **not** write this README as if merge-blocking workflow YAMLs or checked-in watcher jobs are already surfaced on the branch. |
| Exact workflow YAML inventory, live watcher jobs, emitted proof bundles, concrete schema registry contents, deployment overlays, rollback drills, and runtime proof objects | **UNKNOWN** | Keep behavior-significant claims proportional and mark them for branch verification before merge. |
| Live `migrations/` inventory | **NEEDS VERIFICATION** | Treat the directory contract as useful, but verify actual branch contents before claiming presence or layout. |
| Single authoritative schema home between `contracts/` and `schemas/` | **NEEDS VERIFICATION** | This README should not amplify a parallel schema universe; the authoritative home must be named on the branch. |

> [!IMPORTANT]
> The two most important trust risks for migration documentation remain: a visible dual schema-facing surface (`contracts/` and `schemas/`) and gatehouse scaffolding that can outrun surfaced workflow YAML. This README stays explicit about both.

### Visible gatehouse lanes worth checking first

```text
.github/actions/metadata-validate-v2
.github/actions/metadata-validate
.github/actions/opa-gate
.github/actions/provenance-guard
.github/actions/sbom-produce-and-sign
.github/workflows/README.md
.github/watchers/README.md
```

Use branch inspection to confirm whether these remain docs-only cues or now have executable counterparts.

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
├── packets/
│   └── 2026-03-05_<slug>/
│       ├── README.md
│       ├── plan.md
│       ├── verify.md
│       ├── rollback.md
│       ├── correction.md
│       ├── fixtures/
│       └── artifacts/
├── drills/
│   └── 2026-03-05_<slug>/
│       ├── post-deploy-verification.md
│       └── correction-visibility.md
└── templates/
    └── migration-packet.md
```

Adopt a shape like this only if it matches the mounted repo’s actual execution model. The broader successor manual proposes contract, policy, data, and app trees at repo level; it does **not** by itself prove a checked-in `migrations/` packet hierarchy.
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

# inspect visible root surfaces called out by current public-main evidence
git ls-files 'apps/**' 'contracts/**' 'data/**' 'docs/**' 'infra/**' \
  'packages/**' 'policy/**' 'schemas/**' 'tests/**' 'tools/**' \
  '.github/**' | sed -n '1,200p'

# inspect public gatehouse lanes that the successor manual says are visible
find .github -maxdepth 2 -type d 2>/dev/null | sort
git ls-files '.github/actions/**' '.github/workflows/**' '.github/watchers/**' | sort

# verify whether workflows/watchers are still README-only on the branch
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort
find .github/watchers -maxdepth 2 -type f 2>/dev/null | sort

# find contract and proof-object language
git grep -nE 'SourceDescriptor|IngestReceipt|ValidationReport|DatasetVersion|CatalogClosure|DecisionEnvelope|ReviewRecord|ReleaseManifest|ReleaseProofPack|ProjectionBuildReceipt|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|run_manifest|run_receipt|ai_receipt|spec_hash|attestation' -- . 2>/dev/null

# find migration, rollback, correction, and compatibility-seam language
git grep -nE 'migrat|rollback|supersed|withdraw|compatibility|dual-read|dual-write|deprecat|correction' -- . 2>/dev/null
```

### Review-first branch audit

```bash
# choose the review base explicitly
BASE_REF=origin/main

# see what the branch actually touches
git diff --name-only "$BASE_REF"...HEAD | sort

# narrow to likely migration-bearing surfaces
git diff --name-only "$BASE_REF"...HEAD \
  | grep -E '^(migrations|contracts|schemas|policy|scripts|tests|docs|\.github)/' || true
```

### Verify these before calling the branch “done”

1. Does `migrations/` already exist on the branch, or is this PR introducing it?
2. Which schema home is authoritative for this change: `contracts/`, `schemas/`, or an ADR-backed replacement?
3. Are valid and invalid fixtures present for the changed contract families?
4. What proof objects are emitted before and after promotion?
5. Are `run_manifest` / `run_receipt` / `ai_receipt` applicable here, and if so where are they stored canonically?
6. What post-deploy checks exist for rollback or correction?
7. Which public-safe surface shows release and correction state after cutover?

## Usage

Treat this directory as a **review surface**, not only as a script bucket.

1. **Classify the change.** Name it: schema, storage, data, contract, policy, release, projection, runtime, or correction-bearing.
2. **Assemble the packet.** Pair the migration mechanism with notes, fixtures, and proof-object expectations.
3. **Declare the seam.** State the compatibility window, bridge strategy, and stop rule.
4. **Run the gates.** Record schema, policy, validation, release, and post-deploy checks honestly.
5. **Close the loop.** Retire the seam deliberately or emit rollback, supersession, withdrawal, or correction artifacts.

> [!NOTE]
> A migration PR that cannot identify its proof objects, stop rule, and correction path is not ready, even if the underlying script is short.

## Migration posture

### Core doctrine

| Rule | Practical consequence |
|---|---|
| Migration is broader than schema change | Storage, data, contracts, policy, release, runtime, and correction can all be migration-bearing. |
| Preserve the canonical path | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` remains load-bearing. |
| Preserve the trust membrane | Public clients and normal UI surfaces do not receive temporary bypasses that outlive the cutover. |
| Separate build, deploy, and promote | Deployment changes runtime placement; promotion changes public trust state. |
| Prefer staged, reversible change | Expand, compare, cut over, verify, then retire old seams deliberately. |
| Keep correction first-class | Rollback, supersession, withdrawal, and visible narrowing belong in migration design, not incident afterthoughts. |
| Do not let temporary seams fossilize | Dual-read, dual-write, adapters need explicit stop rules. |
| Never let derived layers back-write authority | Projection and packaging workers rebuild from promoted scope only. |

### Compatibility and deprecation rules

| Rule | Migration consequence |
|---|---|
| Outward-published contracts evolve additively by default | Breaking changes require explicit versioning, fixture updates, and runbook changes. |
| Registries expand more safely than they mutate | Additive reason or obligation changes are usually safer than redefining existing meanings. |
| Trust objects stay stable and inspectable | `EvidenceBundle` and `RuntimeResponseEnvelope` semantics should not drift casually. |
| Deprecation needs a visible end state | Name the replacement path, compatibility window, and final retirement condition. |
| Proof objects should converge, not proliferate | Normalize receipt and evidence shapes early instead of allowing local packet variants to drift apart. |

### What migration authors must preserve at trust surfaces

A migration is not finished when the mechanism succeeds. It is finished when the system can still explain:

- what changed
- why it changed
- what release and policy state allowed it
- what users would see during stale, generalized, withdrawn, superseded, denied, or abstained outcomes
- how correction propagates afterward

[Back to top](#migrations)

## Contracts & proof objects

The KFM corpus is unusually explicit about the object families that make governed change inspectable.

> [!NOTE]
> The object families below are **CONFIRMED doctrinally**. Concrete schema files, emitted examples, registries, and resolver traces remain **UNKNOWN** or **NEEDS VERIFICATION** until surfaced from the branch or runtime directly.

### Core proof-object families

| Object family | Why it matters in migration |
|---|---|
| `SourceDescriptor` | Declares the intake contract for a source, endpoint, or file family touched by migration-bearing work. |
| `IngestReceipt` | Proves that a fetch and landing event occurred during replay, backfill, or rebuild. |
| `ValidationReport` | Records what checks passed, failed, or quarantined during the change. |
| `DatasetVersion` | Carries the authoritative candidate or promoted subject set after change. |
| `CatalogClosure` | Preserves outward STAC/DCAT/PROV closure and release linkage. |
| `DecisionEnvelope` | Records machine-readable policy outcomes, reasons, and obligations. |
| `ReviewRecord` | Preserves human approval, denial, escalation, or steward note. |
| `ReleaseManifest / ReleaseProofPack` | Assembles the public-safe release and its proof-bearing context. |
| `ProjectionBuildReceipt` | Proves that maps, tiles, exports, search, graph, or scene derivatives were rebuilt from known release scope. |
| `EvidenceBundle` | Packages support for a claim, feature, story node, export preview, or answer after change. |
| `RuntimeResponseEnvelope` | Makes runtime outcomes accountable: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, plus stale or correction-bearing state. |
| `CorrectionNotice` | Preserves visible lineage under rollback, supersession, withdrawal, or narrowing. |

### Execution augmenters now worth standardizing

The 2026 successor manual and Pass 10 add a second, smaller family of execution augmenters that intensify the earlier doctrine without replacing it.

| Augmenter | Why it matters |
|---|---|
| `spec_hash` | Pins a canonicalized input specification so reruns, PRs, and release comparisons are materially comparable. |
| `run_manifest` or `run_receipt` | Binds inputs, outputs, digests, actor or workflow identity, and checks to one run. |
| `ai_receipt` | Separates model/runtime metadata, proposal context, determinism settings, and output digests from the human-readable surface. |
| Attestation bundle | Carries keyless signing, transparency-log proof, or in-toto-style attestation for release artifacts. |
| `audit_ref` | Lets logs, policy decisions, releases, and UI behavior join into one reconstructable audit graph. |

### First machine-checkable wave

The strongest attached doctrine still converges on a deliberately small first schema wave. The point is **not** the literal filename. The point is that the contract becomes explicit enough to validate, diff, fixture-test, and review.

```text
source_descriptor
validation_report
dataset_version
catalog_closure
decision_envelope
release_manifest
evidence_bundle
runtime_response_envelope
correction_notice
```

### Why these objects belong in a migrations README

A migration in KFM is done only when later readers can reconstruct:

- what changed
- what was promoted
- what was rebuilt
- what policy or review path allowed it
- what users saw at the trust surface
- what correction path exists if the release later narrows or fails

## Diagram

```mermaid
flowchart LR
    A[Classify migration<br/>schema • data • contract • policy • runtime] --> B[Prepare migration packet]
    B --> C[Update companion artifacts<br/>schemas • fixtures • policy diffs • notes]
    C --> D[Run gates<br/>schema • policy • validation • release]
    D --> E{Candidate passes?}

    E -- No --> Q[Hold / Quarantine / Revise]
    Q --> B

    E -- Yes --> F[Review + approval]
    F --> G[Deploy change<br/>without collapsing trust state]
    G --> H[Promote approved release]
    H --> I[Post-deploy verification<br/>freshness • trust state • correction checks]
    I --> J{Trust preserved?}

    J -- Yes --> K[Retire seam deliberately]
    J -- No --> L[Rollback / Supersede / Withdraw / Correct]
    L --> M[Emit correction lineage<br/>and propagate visible state]

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

Above: a governed migration flow in which change is paired with contract updates, fixtures, review, promotion, post-deploy verification, and explicit correction lineage.

## Tables

### Change-class decision matrix

| Change class | Belongs here? | Review burden |
|---|---|---|
| Authoritative schema or storage evolution | **Yes** | High; verify fixtures, compatibility, rollback |
| Data repair or backfill tied to authoritative state | **Yes** | High; validate lineage and correction implications |
| Contract or envelope migration | **Yes** | High; additive evolution, versioning, negative-state review |
| Policy or registry migration affecting runtime outcomes | **Yes** | High; tests, reason or obligation stability, steward review |
| Release or cutover packet | **Yes** | High; release linkage, proof objects, post-deploy verify |
| Correction, withdrawal, or supersession packet | **Yes** | High; visible lineage and downstream rebuild implications |
| Projection-only rebuild with no trust-state seam | **Usually no** | Keep in projection/build surfaces unless part of governed cutover |
| UI-only refactor with unchanged trust behavior | **No** | Keep with app or surface docs |
| Ad hoc repair SQL | **No** | Not durable governed migration history |

### Companion artifacts by change class

| Change class | Usually review with |
|---|---|
| Schema or storage | schema diff, fixture changes, verify steps, rollback note |
| Data or backfill | source basis, reconciliation note, correction path |
| Contract or envelope | schema or OpenAPI diff, compatibility window, negative-path tests |
| Policy or registry | reason/obligation diff, fixtures, decision tests |
| Release or promotion | release notes, proof pack expectations, post-deploy verify |
| Runtime or trust surface | response-envelope diff, evidence drill-through test, stale/correction cues |

### Review questions maintainers should ask

| Question | Why it matters |
|---|---|
| Does this change authoritative truth, derived delivery, or both? | Prevents quiet authority drift |
| Which proof objects must change with it? | Migration without evidence is only half governed |
| Is the change additive, bridged, or breaking? | Determines compatibility and rollback posture |
| What is the stop rule for any seam introduced? | Prevents temporary bridges from becoming architecture |
| What visible state reaches users if cutover fails? | Public surfaces must not bluff trust |
| Is rollback enough, or is correction or supersession needed? | Some public states cannot be “undone” silently |
| Did docs, fixtures, and runbooks change with behavior? | Documentation is part of the governed system |

## Task list / Definition of done

A migration change should not be called complete until the following are true.

- [ ] Branch inventory confirms whether `migrations/` already existed or is being introduced in this PR.
- [ ] The migration class is named clearly: schema, storage, data, contract, policy, release, projection, runtime, or correction-bearing.
- [ ] Preconditions, compatibility seams, and stop rules are documented.
- [ ] The canonical path and trust membrane remain intact.
- [ ] Authoritative and derived layers remain distinct.
- [ ] Required proof objects and fixture updates are named.
- [ ] Validation gates are named and runnable, or explicitly marked manual if not yet enforced.
- [ ] If contracts, schemas, or policy meanings changed, corresponding fixtures or validator work is attached or explicitly called out as missing.
- [ ] The change does not reinforce a parallel schema universe between `contracts/` and `schemas/`.
- [ ] Rollback, supersession, withdrawal, or correction posture is explicit.
- [ ] Public-facing stale, generalized, partial, withdrawn, or superseded states are handled where relevant.
- [ ] Related contracts, schemas, scripts, tests, policy docs, and workflow notes are linked when behavior changes.
- [ ] The branch remains reviewable to a maintainer who did not author the change.

### Readiness gate before broad migration expansion

Until stronger executable evidence exists, broad migration work should also satisfy these conditions:

- [ ] The single authoritative schema home is explicitly named.
- [ ] The first merge-blocking contract or policy gate is real, not README-only scaffolding.
- [ ] One real release proof object or proof pack is surfaced.
- [ ] One real `RuntimeResponseEnvelope` sample or equivalent negative-path trace is surfaced.
- [ ] If automation or AI touched the change, `run_manifest` / `run_receipt` / `ai_receipt` expectations are explicit.
- [ ] This README does not imply mounted automation that the repo does not yet prove.

### Stronger definition of done for the first real rehearsal

The first serious rehearsal should prove at least one end-to-end governed slice:

```text
source_descriptor
-> ingest_receipt
-> validation_report
-> dataset_version
-> catalog_closure
-> decision_envelope / review_record
-> release_manifest or release_proof_pack
-> projection_build_receipt
-> evidence_bundle
-> runtime_response_envelope
-> correction_notice
```

### PR-ready review packet

A non-trivial migration PR should include, at minimum:

- purpose and scope
- evidence label summary (`CONFIRMED` / `INFERRED` / `PROPOSED` / `UNKNOWN`)
- proof objects changed or added
- compatibility window and stop rule, if any seam is introduced
- rollback or correction path
- docs updates, or explicit rationale for none
- tests or fixtures added or updated
- operational impact notes if runtime behavior changes

[Back to top](#migrations)

## FAQ

### Is `migrations/` only for database work?

No. In the strongest KFM doctrine visible in this session, migration is broader than database schema change. It includes storage evolution, data repair/backfill, contract and envelope evolution, policy and registry change, release and promotion consequences, runtime trust behavior, and post-publication correction or supersession.

### Is a live `migrations/` inventory already confirmed in the repo?

No. The attached successor manual strengthens public-main repo evidence at the repo root and `.github` gatehouse, but it still does **not** directly reverify a live `migrations/` inventory on the branch under review. Treat the path as **NEEDS VERIFICATION** until branch inspection proves it.

### Why is this README more cautious than a typical migrations guide?

Because the current session still does not expose a mounted branch checkout or runtime. The doctrine set is strong, and public-main repo evidence is stronger than before, but neither should be flattened into claims about files, workflow YAML, emitted proofs, or automation that were not directly surfaced here.

### Why keep rollback and correction so close together?

Because KFM treats rollback as an evidence-bearing reverse transition, not silent deletion. Some failures can revert to an earlier approved state; others require supersession, withdrawal, generalized output, or visible correction notices.

### What should the first serious migration prove?

Not only that the mechanism works, but that KFM can attach contracts, fixtures, policy decisions, release evidence, runtime trust behavior, and correction lineage to the change without bluffing maturity it does not yet have.

## Appendix — verification notes

<details>
<summary>Open verification questions</summary>

1. Does `migrations/` already exist in the mounted repo, or is this README introducing the directory?
2. Which directory is authoritative for machine-checkable schemas: `contracts/`, `schemas/`, or something else?
3. Which runner or mechanism is actually used for migration-bearing changes?
4. Are there any live migration packets, or only documentation and placeholders?
5. Which first-wave schemas and valid or invalid fixtures already exist on disk?
6. Which CI checks block promotion for migration-bearing PRs?
7. What emitted proof objects already exist versus only being documented?
8. Is there a mounted `EvidenceBundle` resolver and `RuntimeResponseEnvelope` path?
9. What restore, rollback, supersession, or correction drills have actually been exercised?

</details>

<details>
<summary>Illustrative migration packet header (PROPOSED)</summary>

```yaml
id: <migration-id>
class: schema | storage | data | contract | policy | release | projection | runtime | correction
purpose: <one-sentence statement>
authoritative_scope: <what authoritative state changes>
derived_scope: <what derived layers must rebuild or warn>
compatibility_window: <none | bounded window>
proof_objects:
  - <object-family>
execution_augmenters:
  - <spec_hash | run_manifest | run_receipt | ai_receipt | attestation bundle | audit_ref>
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
<summary>Current repo contradictions this directory should not amplify</summary>

| Contradiction | Why migration authors should care | Practical rule in this README |
|---|---|---|
| `contracts/` and `schemas/` both present as schema-facing surfaces | CI can validate one tree while docs or code drift in another | Name the authoritative schema home before claiming machine-safe migration gates |
| Gatehouse action lanes are visible while `.github/workflows/` and `.github/watchers/` remain README-only on current public main | Reviewers may assume gates exist because the gatehouse looks mature | Never write migration guidance as if merge-blocking YAML already exists unless branch evidence proves it |
| Proof-object doctrine is richer than emitted proof-object evidence | A strong manual is not the same thing as surfaced runtime or release output | Definition of done must name runnable checks and actual emitted examples, or mark the gap explicitly |

</details>

<details>
<summary>What should be surfaced next before claiming implementation maturity</summary>

- current repo tree and module inventory for the branch under review
- actual `migrations/` inventory
- current schema directories plus valid or invalid fixtures
- workflow and CI inventory plus required checks
- deployment descriptors or service manifests
- one emitted release proof object
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
