<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION_UUID
title: System Overview
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [../../README.md, ../README.md, ./README.md, ./SYSTEM_CONTEXT.md, ./TRUST_MEMBRANE.md, ./TRUTH_PATH_LIFECYCLE.md, ./DEPLOYMENT_TOPOLOGY.md, ./canonical_vs_rebuildable.md, ./threat-model/README.md, ../../apps/README.md, ../../apps/governed-api/README.md, ../../apps/api/src/api/README.md, ../../web/README.md, ../../packages/README.md, ../../data/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../infra/README.md, ../../.github/README.md, ../../.github/workflows/README.md]
tags: [kfm, architecture, system-overview, truth-path, trust-membrane, map-first]
notes: [doc_id placeholder pending UUID assignment, created/updated placeholders pending git-history verification, policy_label inherited from task baseline and not independently reverified here, revised from March 2026 doctrine plus current public-main repo inspection]
[/KFM_META_BLOCK_V2] -->

# System Overview

_High-level architecture bridge for Kansas Frontier Matrix (KFM): truth path, trust membrane, repo lanes, and trust-visible runtime boundaries._

> **Status:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** `docs/architecture/system_overview.md`  
> **Repo fit:** short-form architecture bridge between [repo root][repo-root], [docs index][docs-root], [architecture index][arch-index], and deeper architecture / runtime / policy surfaces.  
> ![status](https://img.shields.io/badge/status-draft-orange)
> ![surface](https://img.shields.io/badge/surface-system--overview-2f81f7)
> ![posture](https://img.shields.io/badge/posture-evidence--first-0a7d5a)
> ![shell](https://img.shields.io/badge/shell-map--first%20%2B%20time--aware-6f42c1)
> ![trust](https://img.shields.io/badge/trust-membrane-critical)
> ![public main](https://img.shields.io/badge/public_main-tree--inspected-brightgreen)
> ![runtime](https://img.shields.io/badge/runtime-mixed--topology--visible-lightgrey)
> **Quick jumps:** [At a glance](#at-a-glance) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current public-main snapshot](#current-public-main-snapshot) · [Governing law](#governing-law) · [Five-plane view](#five-plane-view) · [Repo surface map](#repo-surface-map) · [Quickstart](#quickstart) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This file is **doctrine-grounded and repo-aware**.
>
> It treats March 2026 KFM architecture law as stable, uses the current public `main` tree for path and maturity signals, and keeps deeper mounted-runtime claims explicitly bounded.  
> It should make the system legible **without** turning placeholders, README-only lanes, or mixed-topology public signals into false certainty.

## At a glance

KFM is a **governed spatial evidence system**. Its primary value unit is the **inspectable claim**: a claim that can still be traced across place, time, evidence state, policy state, review state, release state, and correction state.

| Topic | Working rule |
|---|---|
| System identity | Governed, map-first, time-aware spatial evidence system |
| Value unit | The inspectable claim, not merely a layer, dashboard, export, or fluent answer |
| Canonical lifecycle | `Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED` |
| Trust boundary | Public and steward surfaces cross governed APIs; they do not directly touch canonical stores or model runtimes |
| Runtime answer posture | Cite-or-abstain, fail closed, and keep negative outcomes visible |
| Shell posture | One map-first, time-aware operating shell with evidence drill-through and correction-visible state |
| 3D posture | 2D default; 3D is conditional and burden-bearing |
| Repo posture | Current public `main` shows real lane structure, but not every lane is equally implementation-deep or topology-stable |

### Truth posture used here

| Marker | Use in this file |
|---|---|
| `CONFIRMED` | Directly supported by current public-repo inspection or repeated March 2026 KFM doctrine |
| `INFERRED` | Strongly suggested by adjacent repo surfaces or repeated doctrine, but not re-opened deeply enough here to claim full implementation maturity |
| `PROPOSED` | Repo-ready organization, next-step guidance, or implementation direction that fits doctrine but is not proven as current mounted reality |
| `UNKNOWN` | Not established strongly enough to present as current fact |
| `NEEDS VERIFICATION` | Exact owner, date, route, workflow, or mounted-runtime detail that should be checked before merge |

[Back to top](#system-overview)

## Repo fit

| Field | Value |
|---|---|
| Path | `docs/architecture/system_overview.md` |
| Primary role | One-page architecture bridge between doctrine and deeper architecture / runtime / policy surfaces |
| Upstream anchors | [repo root][repo-root] · [docs index][docs-root] · [architecture index][arch-index] |
| Companion architecture docs | [SYSTEM_CONTEXT.md][system-context] · [TRUST_MEMBRANE.md][trust-membrane] · [TRUTH_PATH_LIFECYCLE.md][truth-path] · [DEPLOYMENT_TOPOLOGY.md][deployment-topology] · [canonical_vs_rebuildable.md][canonical-vs-rebuildable] · [threat-model/README.md][threat-model] |
| Adjacent machine-facing surfaces | [contracts][contracts-root] · [schemas][schemas-root] · [policy][policy-root] · [tests][tests-root] · [workflows README][workflows-readme] |
| Adjacent runtime surfaces | [apps][apps-root] · [apps/governed-api][apps-gov-api] · [apps/api/src/api][apps-legacy-api] · [web][web-root] · [packages][packages-root] · [data][data-root] · [infra][infra-root] |
| Why this file matters | It gives contributors a stable whole-system reading before they descend into a single contract family, runtime lane, policy bundle, lifecycle zone, or public shell surface |

### What this file should do

- Explain **what KFM is**, **how trust state moves**, and **where repo lanes fit**.
- Keep **architecture law** separate from **mounted implementation certainty**.
- Show the shortest path from **source intake** to **trust-visible runtime behavior**.
- Name the repo surfaces that must move together when architecture changes.

### What this file should not do

- Replace machine-readable contracts, policy bundles, or tests.
- Pretend a README-first or scaffold-first lane is already operationally complete.
- Freeze the exact runtime topology if the live checkout later proves a different shape.
- Reintroduce stack claims that the current public tree or doctrine layer does not support.

## Accepted inputs

Content that belongs here includes:

- system identity, non-goals, and whole-system invariants
- truth-path ordering and trust-membrane rules
- five-plane or equivalent architecture summaries
- map-first shell posture and runtime-boundary law
- repo-lane maps that connect `data/`, `packages/`, `apps/`, `contracts/`, `policy/`, `tests/`, `infra/`, `.github/`, and relevant parallel runtime doc roots
- architecture diagrams that explain responsibility, not just boxes
- current public-main maturity notes when they materially affect safe documentation
- cross-links to deeper architecture files, ADR lanes, threat models, and interface registries

## Exclusions

The following do **not** belong here as the authoritative source of truth:

| Keep out of this file | Keep it instead |
|---|---|
| Policy rule bodies, reason / obligation registries, deny-by-default fixtures | [policy][policy-root] |
| Canonical object schemas, OpenAPI, shared vocabularies | [contracts][contracts-root] and [schemas][schemas-root] |
| Runtime code, worker implementations, UI component logic | [apps][apps-root], [web][web-root], and [packages][packages-root] |
| Deployment manifests, ingress details, secrets posture as if verified here | [infra][infra-root] plus mounted runtime evidence |
| Service-local tutorials or route-by-route implementation notes | service-local docs and runbooks |
| Any claim that upgrades README-first or scaffold-first surfaces into “already working” architecture | keep it `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` until rechecked |

## Current public-main snapshot

> [!NOTE]
> This section records the **current public `main` inspection used for this revision**.
>
> Re-check it whenever the tree changes.  
> The point is not to fossilize the branch. The point is to stop architecture prose from outrunning the evidence.

| Surface | Current public `main` state | How to read it |
|---|---|---|
| Repo root | `.github`, `apps`, `brand`, `configs`, `contracts`, `data`, `docs`, `examples`, `infra`, `migrations`, `packages`, `policy`, `schemas`, `scripts`, `tests`, `tools`, plus root governance/docs files | Core monorepo lanes are real and broader than the subset this file summarizes |
| `docs/architecture/` | Mixed subtree: substantive docs (`README.md`, `TRUST_MEMBRANE.md`, `TRUTH_PATH_LIFECYCLE.md`, `system_overview.md`, `threat-model/README.md`), thinner/scaffold-style leaves (`SYSTEM_CONTEXT.md`, `DEPLOYMENT_TOPOLOGY.md`, `canonical_vs_rebuildable.md`, `trust_membrane.md`), and scaffold-lane dirs (`adr/`, `decisions/`, `diagrams/`, `enforcement/`, `interfaces/`, `overview/`, `registries/`, `templates/`) | Keep this file bridge-like; do not pretend every architecture leaf is equally mature |
| `apps/` | `cli`, `explorer-web`, `governed-api`, `review-console`, `workers` | Preferred app-lane names are now public-tree facts |
| Parallel UI / API docs | `web/README.md` and `apps/api/src/api/README.md` are also visible on current public `main` | Runtime topology is mixed; convergence should stay explicit rather than silently canonicalized |
| `packages/` | `catalog`, `domain`, `evidence`, `genealogy_ingest`, `indexers`, `ingest`, `policy` | Shared-law seam is real; child package public surfaces are still mostly README-first |
| `data/` | `catalog`, `processed`, `proofs`, `published`, `quarantine`, `raw`, `receipts`, `registry`, `work` | The truth-path skeleton is visible in the public tree, not just doctrine |
| `policy/` | `bundles`, `fixtures`, `policy-runtime`, `tests` | Policy is a real lane with implementation-shaped substructure, even though executable depth still needs deeper inspection |
| `tests/` | `accessibility`, `contracts`, `e2e`, `integration`, `policy`, `reproducibility`, `unit` | Verification is a first-class lane, not an afterthought |
| `.github/` | `ISSUE_TEMPLATE/`, `actions/`, `workflows/`, `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `SECURITY.md`, `dependabot.yml` | Repo-side gatehouse is already substantial |
| `.github/workflows/` | `README.md` only on current public `main`; workflow README preserves historical workflow filenames as deleted / prior public signals | Keep current inventory and historical signal separate |

[Back to top](#system-overview)

## Governing law

### System identity

KFM is a system for moving safely from **place** to **time** to **evidence** to **review state** to **policy state** to **release state** without crossing an epistemic gap.

### Non-goals

KFM is **not**:

- a free-form assistant that may answer without inspectable support
- a direct browser-to-store or browser-to-model path
- a renderer-led map app where style or client state quietly becomes authority
- a publish-by-deployment pipeline
- a spectacle-first 3D shell
- a system where derived search, graph, tile, cache, or summary layers quietly become sovereign truth

### Load-bearing invariants

| Invariant | Practical meaning | What must never happen |
|---|---|---|
| Truth path | Data changes state through governed lifecycle transitions | Ad hoc publication from notebooks, transient transforms, or unpublished working state |
| Trust membrane | Public and role-limited surfaces cross governed interfaces | Direct client access to canonical stores, raw zones, or model runtimes |
| Authoritative vs derived | Release-linked authoritative data stays stronger than projections | Tiles, graphs, summaries, scenes, or caches presented as sovereign truth |
| Cite-or-abstain | Claim-bearing surfaces resolve evidence or narrow / refuse | Fluent unsupported output presented as fact |
| Fail closed | Missing evidence, rights ambiguity, or broken policy blocks widening trust state | Graceful-looking fallback that hides broken support |
| Map-first, time-aware shell | Place and chronology remain first-class controls | Detached assistant, dashboard-only view, or review path that severs geography and time |
| 2D default | 2D is the standard operating surface | 3D used as default ornament without added burden and governance justification |
| Docs as production surfaces | Behavior-significant changes move with docs, contracts, policy, tests, and runbooks | Silent drift between implementation and explanation |

## Five-plane view

```mermaid
flowchart LR
    P1["1. Source and intake<br/>SourceDescriptor · IngestReceipt · ValidationReport<br/><br/>Repo surfaces:<br/>data/raw · data/work · data/quarantine · data/receipts · packages/ingest"]
    P2["2. Canonical truth<br/>Identity-stable authoritative data and artifacts<br/><br/>Repo surfaces:<br/>data/processed · data/registry · packages/domain · packages/evidence"]
    P3["3. Catalog / policy / review<br/>Release closure, rights, policy, and reviewable trust state<br/><br/>Repo surfaces:<br/>data/catalog · contracts/ · schemas/ · policy/ · docs/governance/"]
    P4["4. Derived delivery<br/>Release-linked projections only<br/><br/>Repo surfaces:<br/>data/published · data/proofs · packages/catalog · packages/indexers · apps/workers"]
    P5["5. Runtime and trust surfaces<br/>Public and steward behavior with evidence drill-through<br/><br/>Repo surfaces:<br/>apps/explorer-web · apps/governed-api · apps/review-console · apps/cli"]
    T["tests/<br/>accessibility · contracts · e2e · integration · policy · reproducibility · unit"]
    G[".github/<br/>actions · workflows README-only on current public main · CODEOWNERS · PR template"]

    P1 --> P2 --> P3 --> P4 --> P5
    T -. verifies .-> P1
    T -. verifies .-> P5
    G -. governs when configured .-> P3
```

### Plane responsibilities

| Plane | Primary responsibility | Current repo homes to inspect first | Forbidden shortcut |
|---|---|---|---|
| Source and intake | Admit, fetch, validate, quarantine, and receipt source material | `data/raw/`, `data/work/`, `data/quarantine/`, `data/receipts/`, `packages/ingest/` | Silent download or direct write into canonical state |
| Canonical truth | Hold identity-stable, time-aware, authoritative subject data | `data/processed/`, `data/registry/`, `packages/domain/`, `packages/evidence/` | Browser or renderer dependency on canonical storage |
| Catalog / policy / review | Close metadata, rights, policy, review, and release readiness | `data/catalog/`, `contracts/`, `schemas/`, `policy/`, `docs/governance/` | Publish-by-deployment |
| Derived delivery | Build release-linked tiles, exports, indexes, graphs, and other projections | `data/published/`, `data/proofs/`, `packages/catalog/`, `packages/indexers/`, `apps/workers/` | Derived output with no release linkage or freshness basis |
| Runtime and trust surfaces | Deliver public or role-gated behavior with evidence resolution and negative outcomes | `apps/explorer-web/`, `apps/governed-api/`, `apps/review-console/`, `apps/cli/` | Uncited answer, hidden stale state, silent correction, or direct client-to-model call |

### Public request path

A normal outward read should be understood in this order:

1. The shell establishes **place**, **time**, **layer scope**, and **role context**.
2. The request crosses a **governed API boundary**, not canonical stores directly.
3. The API resolves **release-linked data, catalog closure, policy state, and evidence drill-through**.
4. Any derived delivery surface inherits **freshness**, **release linkage**, and **correction behavior**.
5. Any bounded runtime assistance returns finite outcomes such as **answer**, **abstain**, **deny**, or **error** instead of bluffing.

> [!IMPORTANT]
> The renderer is downstream of the chain `source -> delivery -> style -> renderer -> UX`.
>
> That rule matters because it prevents style, tiles, and client state from becoming accidental authority.

> [!NOTE]
> Current public `main` shows the preferred app-lane grouping above **and** still exposes parallel runtime-doc roots under [`web/`](../../web/README.md) and [`apps/api/src/api/`](../../apps/api/src/api/README.md).
>
> Treat the five-plane runtime rows as the primary architectural grouping, not proof that topology convergence is complete.

[Back to top](#system-overview)

## Repo surface map

| Repo surface | Current visible lanes | System role | Reading rule |
|---|---|---|---|
| [`data/`][data-root] | `registry`, `raw`, `work`, `quarantine`, `processed`, `catalog`, `receipts`, `proofs`, `published` | Governed lifecycle, storage, receipts, and release-artifact surface | Start here when the question is “what changed state?” |
| [`contracts/`][contracts-root] + [`schemas/`][schemas-root] | Publicly README-first from the current docs surface | Machine-readable contract backbone and schema authority lanes | Do not spread contract truth ad hoc into apps, docs, or data |
| [`policy/`][policy-root] | `bundles`, `fixtures`, `policy-runtime`, `tests` | Executable governance surface for deny-by-default, reasons, obligations, runtime trust, and correction | UI reflects policy; it does not replace it |
| [`packages/`][packages-root] | `catalog`, `domain`, `evidence`, `genealogy_ingest`, `indexers`, `ingest`, `policy` | Shared reusable logic and shared law seams | Shared logic may live here; sovereign truth and public release state should not |
| [`apps/`][apps-root] | `cli`, `explorer-web`, `governed-api`, `review-console`, `workers` | Trust-visible runtime shell, governed API mediation, review surfaces, workers, and narrow operator tooling | Preferred lane names are visible, but deeper runtime wiring still needs inspection |
| [`web/`][web-root] | React + TypeScript MapLibre UI surface still visible | Parallel UI doc/runtime surface | Reconcile with `apps/explorer-web/` before freezing one canonical UI root |
| [`apps/api/src/api/`][apps-legacy-api] | Older-path governed API doc still visible | Parallel API doc/runtime surface | Reconcile with `apps/governed-api/` before freezing one canonical API root |
| [`tests/`][tests-root] | `accessibility`, `contracts`, `e2e`, `integration`, `policy`, `reproducibility`, `unit` | Governed verification and proof burdens | A green check is insufficient if it cannot explain trust state |
| [`/.github/`][github-root] | `actions/`, `workflows/`, templates, ownership, security, automation scaffolding | Repo-side control and review plane | Separate checked-in files from unverified branch protection or platform settings |
| [`docs/`][docs-root] | architecture, governance, standards, runbooks, domains, research, search, security, templates, and adjacent lanes | Human-readable operating layer | Explanation stays downstream of contracts, policy, and release evidence |

## Quickstart

Use a verification-first loop before editing this file again.

```bash
# Re-check the local architecture subtree
find docs/architecture -maxdepth 3 \( -type f -o -type d \) | sort

# Re-check the repo lanes summarized here
find apps packages data policy tests .github -maxdepth 2 -type d | sort

# Re-open the boundary docs this overview depends on
sed -n '1,240p' README.md
sed -n '1,240p' docs/README.md
sed -n '1,320p' docs/architecture/README.md
sed -n '1,260p' docs/architecture/system_overview.md
sed -n '1,220p' apps/README.md
sed -n '1,220p' apps/explorer-web/README.md 2>/dev/null || true
sed -n '1,220p' apps/governed-api/README.md 2>/dev/null || true
sed -n '1,220p' web/README.md 2>/dev/null || true
sed -n '1,220p' apps/api/src/api/README.md 2>/dev/null || true
sed -n '1,220p' packages/README.md
sed -n '1,220p' data/README.md
sed -n '1,220p' contracts/README.md
sed -n '1,220p' schemas/README.md
sed -n '1,220p' policy/README.md
sed -n '1,220p' tests/README.md
sed -n '1,220p' .github/README.md
sed -n '1,260p' .github/workflows/README.md
```

```bash
# Pressure-test vocabulary drift before widening certainty
grep -RIn "truth membrane\|EvidenceBundle\|RuntimeResponseEnvelope\|cite-or-abstain\|fail-closed" \
  docs contracts policy tests packages apps web 2>/dev/null || true
```

> [!WARNING]
> Do not upgrade a statement from `INFERRED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` to `CONFIRMED` just because folder names look plausible.
>
> Re-check the actual branch first.

[Back to top](#system-overview)

## Task list / definition of done

### Highest-value next tasks

- [ ] Replace or reconcile the remaining thin/scaffold-style architecture leaves under `docs/architecture/`.
- [ ] Resolve the authoritative schema-home split between `contracts/` and `schemas/`.
- [ ] Reconcile the parallel UI roots (`web/` and `apps/explorer-web/`) into one explicit public-shell story.
- [ ] Reconcile the parallel API docs (`apps/api/src/api/` and `apps/governed-api/`) into one explicit governed-boundary story.
- [ ] Publish mounted route-family and runtime-envelope evidence for the active governed API boundary.
- [ ] Decide whether `packages/genealogy_ingest/` is a durable first-class lane in the whole-system package map or a lane-specific exception that needs clearer placement.
- [ ] Recheck `.github/workflows/` and record the real workflow catalog once checked-in YAML returns.
- [ ] Reconcile the duplicate trust-membrane leaf paths (`TRUST_MEMBRANE.md` vs `trust_membrane.md`) into one canonical architecture reference.
- [ ] Add one positive and one negative end-to-end trace showing evidence resolution and finite runtime outcomes.
- [ ] Keep the repo-surface tables here aligned with real lane names on the active branch.

### Definition of done for this file

This file is in good standing when:

- [ ] all path claims are either directly rechecked or explicitly labeled
- [ ] the diagram and tables still match the active repo tree
- [ ] current public-main maturity signals are re-verified before merge
- [ ] architecture claims do not outrun contracts, policy, tests, or workflow evidence
- [ ] mixed-topology caveats remain visible until convergence is verified
- [ ] cross-links resolve
- [ ] dates, owner record, and doc UUID are synchronized with the real repo record

## FAQ

### Is this the final runtime topology?

No. This is the **short-form architecture bridge**, not a claim that every mounted service, route, or deployment overlay has been re-inspected. Use it to keep the whole-system order clear, then verify runtime detail in the live tree.

### What is the smallest stable mental model for KFM?

Use three things together:

1. the **truth path**
2. the **trust membrane**
3. the **five-plane reading**

If a proposal breaks one of those, it is probably breaking KFM.

### Is Focus just a chatbot in the map shell?

No. Focus is a **bounded runtime assistance surface**. It stays inside the governed shell, inherits evidence and policy obligations, and should converge on finite outcomes rather than persuasive improvisation.

### Why keep derived layers subordinate?

Because tiles, graphs, search indexes, scenes, caches, and summaries are useful precisely when they remain reconstructable from stronger, release-linked authority. Convenience is not sovereignty.

### Why is 3D not central here?

Because KFM’s doctrine is 2D-first. 3D is allowed when it carries real explanatory or analytic burden, but it adds governance cost and cannot be admitted simply because it looks impressive.

### Why call out mixed runtime topology explicitly?

Because current public `main` already shows both the newer `apps/*` grouping and parallel runtime-doc roots elsewhere in the tree. Hiding that fact would make the file cleaner-looking but less truthful.

[Back to top](#system-overview)

## Appendix

<details>
<summary><strong>Companion architecture surfaces and current public-main state</strong></summary>

| Path | Current public-main state | Intended use |
|---|---|---|
| [`./README.md`][arch-index] | substantive | architecture index and local boundary map |
| [`./system_overview.md`](./system_overview.md) | substantive | short-form whole-system bridge |
| [`./TRUST_MEMBRANE.md`][trust-membrane] | substantive companion | focused trust-boundary law |
| [`./TRUTH_PATH_LIFECYCLE.md`][truth-path] | substantive companion | lifecycle-specific detail |
| [`./threat-model/README.md`][threat-model] | substantive companion | threat-model lane entry point |
| [`./SYSTEM_CONTEXT.md`][system-context] | thin / scaffold-style | deeper system-context description |
| [`./DEPLOYMENT_TOPOLOGY.md`][deployment-topology] | thin / scaffold-style | runtime / environment topology |
| [`./canonical_vs_rebuildable.md`][canonical-vs-rebuildable] | thin / scaffold-style | authoritative-versus-derived detail |
| `./trust_membrane.md` | thin duplicate path on current public `main` | reconcile with uppercase canonical path |
| [`./decisions/README.md`](./decisions/README.md) | scaffold-lane index | local decision-record lane |
| [`./diagrams/README.md`](./diagrams/README.md) | scaffold-lane index | diagram lane |
| [`./interfaces/README.md`](./interfaces/README.md) | scaffold-lane index | interface registry lane |
| `./adr/`, `./enforcement/`, `./overview/`, `./registries/`, `./templates/` | present on current public `main`; not treated here as mature content authorities | recheck before using as current content authority |

</details>

<details>
<summary><strong>Parallel runtime-path signals worth rechecking before stronger claims</strong></summary>

| Path | Why it matters |
|---|---|
| [`../../apps/explorer-web/README.md`](../../apps/explorer-web/README.md) | Public app-lane surface that matches the newer `apps/*` grouping |
| [`../../web/README.md`](../../web/README.md) | Parallel UI surface still visible in the repo |
| [`../../apps/governed-api/README.md`](../../apps/governed-api/README.md) | Public governed API surface that matches the newer `apps/*` grouping |
| [`../../apps/api/src/api/README.md`](../../apps/api/src/api/README.md) | Parallel API surface still visible under an older path |
| [`../../apps/review-console/README.md`](../../apps/review-console/README.md) | Review surface anchor for steward-facing trust operations |
| [`../../apps/workers/README.md`](../../apps/workers/README.md) | Derived-delivery and batch-work lane anchor |
| [`../../apps/cli/README.md`](../../apps/cli/README.md) | Narrow operator/tooling lane anchor |

</details>

<details>
<summary><strong>Open verification items still relevant to this file</strong></summary>

| Item | Why it matters |
|---|---|
| Mounted route inventory behind the active governed API boundary | This file should not invent route families or DTOs the live tree does not prove |
| Runtime topology convergence | Public `main` still shows parallel UI/API roots |
| Workflow catalog and required checks | Architecture claims about enforcement become misleading if workflow state is guessed |
| Evidence resolver examples | KFM’s runtime trust model depends on real evidence drill-through, not just prose |
| Deployment overlays and runtime manifests | System overview should not hard-code topology the live checkout disproves |
| Schema-home decision | The `contracts/` / `schemas/` boundary affects where architecture links point |
| Companion architecture leaf completion | This file should remain the bridge, not the only substantive architecture doc |
| Actual git-history dates and UUID assignment | Required to finalize the KFM Meta Block v2 |

</details>

<details>
<summary><strong>Link map</strong></summary>

- Upstream: [repo root][repo-root] · [docs index][docs-root] · [architecture index][arch-index]
- Machine surfaces: [contracts][contracts-root] · [schemas][schemas-root] · [policy][policy-root] · [tests][tests-root] · [workflows README][workflows-readme]
- Runtime surfaces: [apps][apps-root] · [apps/governed-api][apps-gov-api] · [apps/api/src/api][apps-legacy-api] · [web][web-root] · [packages][packages-root] · [data][data-root] · [infra][infra-root]
- Companion architecture docs: [system context][system-context] · [trust membrane][trust-membrane] · [truth path lifecycle][truth-path] · [deployment topology][deployment-topology] · [canonical vs rebuildable][canonical-vs-rebuildable] · [threat model][threat-model]

</details>

[repo-root]: ../../README.md
[docs-root]: ../README.md
[arch-index]: ./README.md
[system-context]: ./SYSTEM_CONTEXT.md
[trust-membrane]: ./TRUST_MEMBRANE.md
[truth-path]: ./TRUTH_PATH_LIFECYCLE.md
[deployment-topology]: ./DEPLOYMENT_TOPOLOGY.md
[canonical-vs-rebuildable]: ./canonical_vs_rebuildable.md
[threat-model]: ./threat-model/README.md
[apps-root]: ../../apps/README.md
[apps-gov-api]: ../../apps/governed-api/README.md
[apps-legacy-api]: ../../apps/api/src/api/README.md
[web-root]: ../../web/README.md
[packages-root]: ../../packages/README.md
[data-root]: ../../data/README.md
[contracts-root]: ../../contracts/README.md
[schemas-root]: ../../schemas/README.md
[policy-root]: ../../policy/README.md
[tests-root]: ../../tests/README.md
[infra-root]: ../../infra/README.md
[github-root]: ../../.github/README.md
[workflows-readme]: ../../.github/workflows/README.md
