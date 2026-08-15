<!--
KFM_WIKI_SOURCE
page_id: Project-Status
title: Project Status
version: v0.2.0
status: PROPOSED wiki source; review required
created: 2026-08-07
updated: 2026-08-15
authority: orientation-only; current repository evidence, adopted KFM authority, and owning responsibility roots outrank this page
source_path: docs/wiki/Project-Status.md
owning_root: docs/
responsibility: evidence-bounded reader snapshot of repository, validation, runtime, release, deployment, and native-wiki maturity
evidence_snapshot: main@35a6237f2f29e680bafe9af16f71e28fc585a735
prior_blob: 4b7ac87e42902bb28e0531ba5491ac7477fb26bb
publication_effect: none until separately synchronized to the native GitHub Wiki; no KFM data publication effect
-->

<a id="top"></a>

<p align="center">
  <img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix seal" width="150" />
</p>

# Project Status

<p align="center"><strong>An evidence-pinned view of what KFM currently contains, what has bounded executable proof, what remains held, and what has not been established.</strong></p>

[![Checkpoint](https://img.shields.io/badge/checkpoint-35a6237f2f29-0969da?style=flat-square)](#evidence-checkpoint)
[![Posture](https://img.shields.io/badge/maturity-mixed-f59e0b?style=flat-square)](#status-by-responsibility-plane)
[![Exact-head CI](https://img.shields.io/badge/exact--head%20CI-44%20success%20%7C%203%20failure%20%7C%201%20skipped%20%7C%201%20queued-d4a72c?style=flat-square)](#exact-head-validation-snapshot)
[![Operational release](https://img.shields.io/badge/operational%20release-held-b42318?style=flat-square)](#release-publication-and-deployment)
[![Deployment](https://img.shields.io/badge/current%20deployment-UNKNOWN-6e7781?style=flat-square)](#release-publication-and-deployment)
[![Native wiki](https://img.shields.io/badge/native%20wiki-NEEDS%20VERIFICATION-6e7781?style=flat-square)](#native-github-wiki)

> [!IMPORTANT]
> **This page is a snapshot, not a live dashboard and not an authority surface.** It was reconciled against `main@35a6237f2f29e680bafe9af16f71e28fc585a735` on 2026-08-15. Re-check current `main`, open pull requests, workflow runs, release records, deployment status, emitted artifacts, and native-wiki readback before acting on any status.

> [!CAUTION]
> **Presence, validation, integration, release, deployment, and publication are different states.** A path, schema, fixture, test, workflow, receipt, pull request, merge, GitHub deployment record, badge, or wiki update does not by itself prove an operational service or KFM publication.

**Quick navigation:** [Checkpoint](#evidence-checkpoint) · [At a glance](#snapshot-at-a-glance) · [How to read status](#how-to-read-this-status) · [Responsibility planes](#status-by-responsibility-plane) · [CI](#exact-head-validation-snapshot) · [UI and API](#bounded-user-facing-and-api-baseline) · [Domains and lifecycle](#domains-evidence-and-lifecycle) · [Release and deployment](#release-publication-and-deployment) · [Native wiki](#native-github-wiki) · [Verification priorities](#highest-value-verification-priorities) · [Verify directly](#where-to-verify) · [Correction](#maintenance-and-correction)

---

## Evidence checkpoint

| Field | Bounded result |
|---|---|
| Repository | [`bartytime4life/Kansas-Frontier-Matrix`](https://github.com/bartytime4life/Kansas-Frontier-Matrix), public |
| Default branch | `main` |
| Inspected revision | [`35a6237f2f29e680bafe9af16f71e28fc585a735`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/35a6237f2f29e680bafe9af16f71e28fc585a735) |
| Revision event | Merge of PR #2905, a western-Kansas hydrology observation-assessment slice |
| Checked | 2026-08-15 |
| Target history | This page had not changed since the source-managed wiki foundation was added on 2026-08-07 |
| Open target overlap | No open pull request referencing `docs/wiki/Project-Status.md` was found during preflight |
| Evidence types inspected | Repository bytes, accepted ADR state, root and subsystem READMEs, current application files, exact-head GitHub Actions results, releases, deployment records, wiki source controls, and native-wiki connector response |
| Native-wiki effect | None; this source page still requires a separate reviewed synchronization |
| KFM publication effect | None |

The checkpoint intentionally distinguishes current tracked bytes from runtime behavior. Historical or proposal documents may explain intent, but they do not upgrade a current implementation claim without repository, test, artifact, release, or runtime evidence at a known revision.

> [!NOTE]
> During authoring, `main` advanced by ten commits from the initial preflight. The final snapshot was refreshed rather than silently based on the older head; the intervening changes registered DatasetVersion in aggregate validation and added a western-Kansas hydrology observation-assessment slice.

[Back to top](#top)

---

## Snapshot at a glance

| Surface | Current bounded status | What is established | What is not established |
|---|---:|---|---|
| Placement authority | **ACCEPTED** | ADR-0029 adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` | Complete repository conformance or finished migration |
| Repository topology | **PRESENT / mixed conformance** | Canonical responsibility roots, compatibility roots, a deprecated containment root, and topology validation surfaces are tracked | Zero drift, zero legacy consumers, or completed authority convergence |
| Domain documentation | **13 lanes present** | Thirteen direct domain lanes, thirteen substantive lane READMEs, and thirteen machine-projection entries are recorded | Equal implementation, source activation, evidence closure, or publication across lanes |
| Explorer Web | **BOUNDED EXECUTABLE PROOF** | Static Vite shell, strict Evidence Drawer projection, finite outcomes, no-leak behavior, keyboard focus handling, and synthetic tests | Live governed API transport, functional production map, live data, direct model use, deployment, or publication |
| Governed API | **BOUNDED STUB API** | WSGI application and three registered `GET` routes (`/bootstrap`, `/layers`, `/evidence`) returning finite abstention envelopes; source and tests are present | Production authorization, live evidence resolution, policy execution, complete route families, deployment, or public availability |
| Contracts, schemas, fixtures, validators | **SUBSTANTIAL / fixture-first** | Versioned schema surface, registry-driven validation, focused object-family slices, and fail-closed tests exist | Complete object-family coverage, accepted status for every proposed ADR/profile, or universal operational enforcement |
| Exact-head GitHub Actions | **MIXED / one queued** | 49 push-triggered runs were returned for the checkpoint: 44 success, 3 failure, 1 skipped, 1 queued | A complete final run set, a fully green main revision, or proof that every successful workflow is a required release gate |
| Release governance | **FIXTURE-FIRST / OPERATIONAL HOLD** | Release decision root, bounded manifests/decisions/gates/rollback profiles, and dry-run-oriented checks exist | Authenticated release authority, operational candidate assembly, promotion execution, rollback execution, or public release |
| GitHub Releases | **NONE RETURNED** | The repository Releases API returned no releases at the checkpoint | Absence of every possible external artifact or historical distribution |
| Current deployment | **UNKNOWN** | Historical `stage` deployment records exist; the latest inspected historical status was failure | A current, healthy, supported, public or production KFM deployment |
| Native GitHub Wiki | **NEEDS VERIFICATION** | Repository metadata enables wiki functionality; reviewed source exists under `docs/wiki/` | Native page contents, last synchronized source commit, render parity, or current public-wiki state |

### Overall determination

**KFM is no longer only a design corpus.** It has a broad repository, machine-checkable governance projections, contracts and schemas, fixtures, validators, workflows, application code, bounded UI/API behavior, domain documentation, lifecycle lanes, and release-supporting records.

**KFM is also not a completed public system.** The current evidence does not establish a live production map, complete governed API, operational release pipeline, current successful deployment, populated and reconciled native wiki, or broad proof-bearing publication across all domains.

[Back to top](#top)

---

## How to read this status

The following reader ladder prevents one kind of evidence from being mistaken for a stronger one. These are explanatory maturity bands, not new KFM object states.

| Reader band | Minimum evidence | Safe language |
|---|---|---|
| **Repository present** | Path and bytes exist at a known revision | “The repository contains…” |
| **Bounded executable proof** | Focused tests, fixtures, validators, or a reproducible local flow exercise the stated boundary | “The bounded slice demonstrates…” |
| **Integrated and governed** | Real components exchange validated envelopes through intended policy and evidence boundaries | “The integrated path enforces…” |
| **Release-ready** | Evidence, policy, review, integrity, manifest, correction, and rollback prerequisites close for a named candidate | “The candidate is ready for a release decision…” |
| **Released** | An accountable release decision identifies the exact approved public-safe carrier and rollback target | “Release X includes…” |
| **Deployed or publicly served** | Current runtime, endpoint, environment, version, access policy, health, and rollback evidence are verified | “Service X is available at…” |
| **KFM-published** | Governing publication controls appropriate to consequence are satisfied and recorded | “KFM publishes…” |

A green test can support the second band without proving the fourth, fifth, sixth, or seventh. A historical deployment record can exist without proving a current service. A merged wiki source page can exist without proving native-wiki synchronization.

[Back to top](#top)

---

## Status by responsibility plane

| Responsibility plane | Status at the checkpoint | Evidence-based interpretation |
|---|---:|---|
| Doctrine and placement | **ACCEPTED authority / PARTIAL implementation** | ADR-0029 is accepted and adopts Directory Rules v2. Root projections and topology ratchets exist, while inherited drift, compatibility migration, consumer closure, and held deletions remain unfinished or unverified. |
| Documentation and wiki source | **ACTIVE source packet** | `docs/wiki/` contains the reviewed source set and maintenance tooling. Several pages have been modernized; the source packet remains orientation-only and separate from native-wiki transport. |
| Contracts and schemas | **MIXED, versioned, expanding** | Semantic and machine-shape roots are present. `schemas/contracts/v1/` is the configured validation surface, while narrower schema-home ADRs and compatibility-lane convergence remain proposed or incomplete. |
| Policy and sensitivity | **PRESENT / enforcement varies** | Policy roots, tests, deny paths, and sensitive-domain guidance exist. Current source rights, domain steward decisions, and production policy execution remain case-specific. |
| Evidence, receipts, and proofs | **PRESENT / closure varies** | Evidence, generated receipts, proofs, resolver surfaces, and citation checks exist. A receipt records a process; it does not prove truth, review, release, or publication. |
| Domain lanes | **13 documented / mixed implementation** | All registered documentation lanes are substantive. Domain-specific contracts, sources, processing, catalogs, released carriers, and runtime consumers remain uneven and must be verified lane by lane. |
| Applications and runtime | **BOUNDED implementations** | Explorer Web and Governed API have executable fail-closed slices. Mock and adapter boundaries exist, but public runtime integration and production service evidence remain limited. |
| Data lifecycle | **STRUCTURE PRESENT / operational closure uneven** | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, PUBLISHED, receipt, proof, registry, and rollback responsibilities are represented. Placement alone does not prove a governed end-to-end promotion. |
| Release and correction | **FIXTURE-FIRST / HELD operationally** | Release manifests, decisions, gates, rollback cards, correction-related lanes, and checks have bounded evidence. Real candidate assembly, authenticated review, promotion, rollback execution, cache invalidation, and public parity are not established. |
| Delivery and publication | **UNKNOWN to limited** | No GitHub Release was returned. Historical stage deployments do not prove a current endpoint. Public serving, current deployment health, and KFM publication remain unverified. |

### Authority reminder

For current behavior, repository implementation and observed outputs outrank descriptive prose. For placement, adopted Directory Rules and accepted ADRs control. For object meaning, shape, and admissibility, use the owning contracts, schemas, and policy. For release, correction, withdrawal, and rollback, use `release/` records. For claim support, resolve `EvidenceRef` to `EvidenceBundle`.

[Back to top](#top)

---

## Exact-head validation snapshot

GitHub returned **49 workflow runs** for the checkpoint revision. One remained queued at the final source snapshot:

| Conclusion | Count | Interpretation |
|---|---:|---|
| Success | 44 | Each completed run passed its declared scope |
| Failure | 3 | Current `main` is not fully green |
| Skipped | 1 | APIsec was skipped; a skipped run is not a pass |
| Queued | 1 | `pmtiles-delta-manifest` had not started; no conclusion was available |
| Total | 49 | Push-triggered exact-head workflow records returned by the API |

### Current red stages

| Workflow | Exact-head result | Failing stage | Important bounded detail |
|---|---:|---|---|
| [`domain-hydrology`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31900752617) | **FAILURE** | `Evaluate Hydrology validation readiness` | Bounded Hydrology schema validation was skipped; separate proof-hold and release-dry-run-hold jobs succeeded |
| [`schema-validation`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31900752673) | **FAILURE** | `Validate configured aggregate fixture families` | Schema inventory and the focused DatasetVersion/aggregate-selection regression passed first; repository-owned schema/contract tests were then skipped |
| [`validator-suite`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31900752526) | **FAILURE** | `Enforce repository workflow and topology ratchets` | Later aggregate-validator and generated-receipt stages were skipped |
| `validator-suite / ensure-fail-closed` | **SUCCESS** | Reviewed invalid `EvidenceBundle` rejection canary passed | Proves that bounded negative case only |
| [`pmtiles-delta-manifest`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/31900752558) | **QUEUED** | No job conclusion yet | Re-check before treating the 49-run set as final |

> [!WARNING]
> **Do not summarize this checkpoint as either “CI is green” or “the project is broken.”** Forty-four runs passed, three workflows failed at named stages, one run was skipped, and one remained queued. Open pull requests may already target part of the residue, but proposed remediation is not current `main` until merged and rechecked.

See [Development and Validation](Development-and-Validation.md) for interpreting checks and the repository [Actions page](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions) for current results.

[Back to top](#top)

---

## Bounded user-facing and API baseline

### Explorer Web

The current Explorer entry point renders a static shell and mounts an Evidence Drawer. The drawer resolver:

- accepts a strict governed projection rather than arbitrary display properties;
- distinguishes `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- exposes source-role, policy, review, release, freshness, correction, evidence, citation, limitation, and history labels when permitted;
- replaces denied, malformed, or upstream-error detail with fixed no-leak copy;
- opens through a native button, moves keyboard focus into the drawer, closes on Escape, and returns focus to the opener; and
- is covered by synthetic unit and browser checks described by the app.

This is meaningful executable trust-surface evidence. It is **not** proof of a production map, live network transport, canonical full-system payload adoption, current deployment, or public data publication.

Read [Map, UI, and AI](Map-UI-and-AI.md) and the [`apps/explorer-web/` README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/explorer-web/README.md).

### Governed API

The current application is a small WSGI service. Its registry exposes three `GET` routes:

| Route | Current bounded behavior |
|---|---|
| `/bootstrap` | Returns a finite `ABSTAIN` envelope |
| `/layers` | Returns a finite `ABSTAIN` envelope |
| `/evidence` | Returns a finite `ABSTAIN` envelope |
| Other path | Returns a finite error envelope with `404` |
| Non-`GET` request to a registered route | Returns a finite error envelope with `405` |

This proves route registration, finite stub behavior, and a fail-closed baseline. It does not prove live source access, real `EvidenceBundle` resolution, production policy middleware, user authorization, a complete API surface, deployment, or public availability.

Read the [`apps/governed-api/` README](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/apps/governed-api/README.md).

### AI and model boundary

KFM's repository and UI doctrine keep model runtimes behind governed interfaces. Mock and bounded adapter surfaces exist, while direct browser-to-model access remains outside the normal public path. A model response is not evidence, review, release, or publication authority.

[Back to top](#top)

---

## Domains, evidence, and lifecycle

### Domain coverage

The domain documentation index currently records these thirteen lanes:

1. agriculture;
2. archaeology;
3. atmosphere;
4. fauna;
5. flora;
6. geology;
7. habitat;
8. hazards;
9. hydrology;
10. people, DNA, and land;
11. roads, rail, and trade;
12. settlements and infrastructure;
13. soil.

All thirteen direct documentation lanes have substantive READMEs, and the machine projection has thirteen ordered entries. This is strong organizational coverage, not equal end-to-end maturity.

For each lane, verify separately:

- source descriptors and activation decisions;
- rights, sensitivity, sovereignty, consent, and public-use posture;
- contract and schema coverage;
- valid, invalid, boundary, and public-safe fixtures;
- deterministic identity and time semantics;
- validators and hosted workflow results;
- `EvidenceRef -> EvidenceBundle` closure;
- processed, catalog/triplet, proof, and published instances;
- release, correction, withdrawal, and rollback records; and
- governed API, map, export, or AI consumers.

Read [Domains](Domains.md), [Governance and Evidence](Governance-and-Evidence.md), and [Data Lifecycle](Data-Lifecycle.md).

### Published-data boundary

`data/published/` is the canonical responsibility lane for release-approved public-safe carrier bytes, but its current README remains **deny by default**. Recursive payload inventory, active writers and consumers, public serving, cache invalidation, and broad release closure are not established by the path itself.

### Cite or abstain

A claim-bearing public surface should reach:

```text
claim or selected feature
  -> EvidenceRef
  -> resolved EvidenceBundle
  -> policy, review, release, freshness, and correction checks
  -> governed finite outcome
  -> public-safe projection
```

When that chain does not close, the correct result is a bounded abstention, denial, hold, or error—not plausible prose.

[Back to top](#top)

---

## Release, publication, and deployment

### Release governance

The `release/` root is the canonical append-only decision plane. Current repository evidence includes fixture-first or proposed profiles for release manifests, promotion decisions, A–G gate semantics, rollback cards, alias verification, corrections, withdrawals, and signatures.

The operational posture remains held because the checkpoint does not establish:

- authenticated and appropriately separated release authority;
- a real candidate assembly process;
- an accepted evaluator that emits a live promotion transition;
- executed rollback and invalidation;
- current public-carrier parity;
- production signing custody;
- a current release dashboard or operational recovery drill.

### GitHub Releases

The GitHub Releases API returned **no releases** at the checkpoint. That is a narrow platform observation. It does not prove that no artifact was ever shared through another channel, and it does not itself decide KFM release state.

### Deployment

GitHub exposes historical `stage` deployment records from December 2025. The newest historical record inspected was tied to an older commit and had a **failure** status. No current production deployment, current stage health, public endpoint, environment version, access policy, runtime log, service-level objective, or rollback readiness was established for `main@35a6237f2f29e680bafe9af16f71e28fc585a735`.

Therefore the safe current statement is:

> **Current deployed-service status: `UNKNOWN`.**

Do not infer a live system from an application folder, an old deployment record, a successful build, or repository visibility.

[Back to top](#top)

---

## Native GitHub Wiki

| Question | Current answer |
|---|---|
| Is the wiki feature enabled? | **CONFIRMED** by repository metadata |
| Does reviewed source exist? | **CONFIRMED** under `docs/wiki/` |
| Is this page automatically synchronized? | **No** |
| Did the connector return a readable native `Home` page? | **No; it returned 404** |
| Does that prove the native wiki is empty? | **No** |
| Was a current `APPLIED` synchronization and Git readback verified? | **No** |
| Safe status | **NEEDS VERIFICATION** |

The connector response could reflect an empty wiki, an uninitialized wiki, connector limitations, or another access mismatch. An authorized operator must use the bounded synchronization workflow, record an immutable reviewed source commit, and perform remote Git readback before claiming the native page set is current.

See [Wiki Maintenance](Wiki-Maintenance.md).

[Back to top](#top)

---

## What is explicitly not confirmed

This checkpoint does **not** establish:

- a complete or production-ready KFM product;
- a current public Explorer deployment;
- a current production or healthy stage API;
- a live map backed by released KFM layers;
- broad live-source activation with current rights and terms;
- complete policy enforcement across every domain and route;
- a fully green exact-head validation state;
- operational release, promotion, rollback, cache invalidation, or correction propagation;
- a GitHub Release;
- synchronized native-wiki parity;
- equal domain maturity;
- AI output as truth, evidence, or release authority; or
- KFM data publication.

These are verification boundaries, not a dismissal of the substantial repository work already present.

[Back to top](#top)

---

## Status vocabulary

| Label | Use on this page |
|---|---|
| `CONFIRMED` | Verified from current repository, platform, workflow, or accepted-decision evidence at the checkpoint |
| `PROPOSED` | A design, profile, route family, or future state not verified as current operational behavior |
| `UNKNOWN` | Available evidence cannot establish the claim |
| `NEEDS VERIFICATION` | A concrete repository, platform, runtime, rights, review, or readback check can resolve the claim |
| `CONFLICTED` | Relevant current evidence or authority surfaces disagree |
| `HOLD` | A transition is intentionally blocked pending required evidence or decision |
| `DEPRECATED` | A path remains for containment or compatibility but is frozen from becoming new authority |
| `SUPERSEDED` | A later reviewed source or state replaces an earlier one while preserving lineage |

[Back to top](#top)

---

## Highest-value verification priorities

1. **Restore a green or intentionally explained main baseline.** Resolve the Hydrology readiness failure, aggregate fixture-family failure, and repository topology-ratchet failure without weakening validation.
2. **Prove one complete trust path.** Select one public-safe claim and demonstrate source admission through `EvidenceBundle`, policy, review, release, governed API, Explorer display, correction, and rollback.
3. **Inventory actual published carriers.** Recursively classify `data/published/`, identify writers/consumers, and bind every public-safe carrier to evidence, release, correction, and rollback records.
4. **Verify current deployment state.** Record environment, commit, service URL, access policy, health, logs, ownership, and rollback for any claimed service.
5. **Reconcile the native wiki.** Dry-run the reviewed source packet, inspect every changed page, then synchronize and read back only with explicit public-mutation authorization.
6. **Verify domain readiness lane by lane.** Do not infer source rights, sensitivity posture, evidence closure, or release maturity from a domain README or register entry.
7. **Close operational release prerequisites.** Establish accountable reviewers, candidate assembly, promotion execution, signing custody, rollback execution, invalidation, and recovery evidence.
8. **Keep current work disjoint.** Search open pull requests and recently merged work before treating any recorded gap as still unowned.

[Back to top](#top)

---

## Where to verify

### Repository and current work

- [Current `main`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main)
- [Open pull requests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pulls)
- [GitHub Actions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions)
- [Commit history](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commits/main)
- [GitHub Releases](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases)

### Authority and control

- [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
- [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/INDEX.md)
- [Verification backlog](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/registers/VERIFICATION_BACKLOG.md)
- [Drift register](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/registers/DRIFT_REGISTER.md)

### Implementation and accountability

- [Explorer Web](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/apps/explorer-web)
- [Governed API](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/apps/governed-api)
- [Domain documentation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains)
- [Schemas](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/schemas)
- [Validators](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/tools/validators)
- [Generated authoring receipts](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/receipts/generated)
- [Release decision plane](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/release)
- [Published-carrier lane](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/published)

[Back to top](#top)

---

## Maintenance and correction

This page should be refreshed when any of these materially changes:

- accepted authority or Directory Rules status;
- repository topology or root classification;
- exact-head baseline validation;
- public UI or API integration;
- domain-lane inventory;
- published-carrier inventory;
- release, correction, withdrawal, or rollback machinery;
- deployment or public endpoint state;
- native-wiki synchronization state; or
- the evidence needed to upgrade an `UNKNOWN`, `HOLD`, or `NEEDS VERIFICATION` claim.

Correction rule:

```text
current evidence changes
  -> update docs/wiki/Project-Status.md at the same path
  -> validate links, anchors, truth labels, and public safety
  -> review and merge source
  -> separately reconcile native wiki when authorized
  -> preserve the prior source and wiki commits for rollback
```

Before merge, abandon or update the feature branch. After merge, revert or forward-fix the exact source commit. If the native wiki was synchronized, correct the source first and then revert or resynchronize the native commit through the reviewed maintenance workflow. Do not force-push merely to hide history.

[Back to top](#top)
