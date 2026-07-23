<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/root-artifacts-readme
title: artifacts/ — Compatibility Root README
type: readme
version: v0.2
status: draft
owners: ["@bartytime4life"]
created: 2026-05-10
updated: 2026-07-22
policy_label: public
related:
  - docs/doctrine/directory-rules.md          # §5, §8, §13, §15, §16, §18
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/quality/maplibre-perf-governance.md
  - data/proofs/                              # canonical home for trust content NOT placed here
  - data/receipts/
  - data/catalog/
  - data/published/
  - release/
tags: [kfm, directory-rules, compatibility-root, transitional, artifacts, governance, repo-hygiene]
notes:
  - "Compatibility root, class `transitional` per directory-rules.md §8.1 default."
  - "Trust-bearing content (receipts, proofs, manifests, releases) forbidden here per §8.2 / §13.2 / §13.5."
  - "Disposition (retain as compatibility, or fully retire) is the §18 OPEN question; ADR pending."
  - "Current repository conformance is mixed: four allowed lanes exist, but tracked artifacts/release and generated artifacts/perf paths remain open drift."
  - "Snapshot claims are pinned to main@86c039f9fda31eb2d4a75112911a5c400ae93a16."
[/KFM_META_BLOCK_V2] -->

<!-- KFM-DOC-GRAPH-HINT
This README is parseable. Do not delete the META block above.
Keep the block synchronized with the visible status table and the generated-work
receipt whenever this README changes materially.
-->

# `artifacts/`

> Optional, tightly scoped **compatibility root** for **build outputs, generated docs, QA reports, and temporary working files** — never for trust-bearing content.

[![Authority](https://img.shields.io/badge/authority-compatibility-orange)][dr-5]
[![Class](https://img.shields.io/badge/class-transitional-yellow)][dr-8]
[![Trust content](https://img.shields.io/badge/trust%20content-FORBIDDEN-red)][dr-82]
[![Conformance](https://img.shields.io/badge/conformance-HOLD-red)][dr-13]
[![Doctrine](https://img.shields.io/badge/doctrine-directory--rules%20%C2%A78.2-blue)][dr-82]
[![README contract](https://img.shields.io/badge/README-%C2%A715%20contract-informational)][dr-15]
[![Disposition](https://img.shields.io/badge/disposition-OPEN%20%C2%A718-lightgrey)][dr-18]
[![Snapshot](https://img.shields.io/badge/tracked%20files-44-6e7781)](#verified-repository-snapshot)

| Field | Value |
|---|---|
| **Authority level** | Compatibility |
| **Class** | `transitional` *(default per [§8.1][dr-81]; see [Open questions](#adrs-and-open-questions))* |
| **Status** | `CONFIRMED` root; **conformance `HOLD`** because `artifacts/release/` and generated `artifacts/perf/` conflict with the four-lane boundary |
| **Owners** | `@bartytime4life` — the only repository owner identity currently verified in `.github/CODEOWNERS` |
| **CODEOWNERS reference** | Inherits the repository-wide `* @bartytime4life` route; no more-specific `/artifacts/` rule is present |
| **Pinned snapshot** | `main@86c039f9fda31eb2d4a75112911a5c400ae93a16` |
| **Last reviewed** | 2026-07-22 |

**Jump to:** [Purpose](#purpose) · [Authority level](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does NOT belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs and open questions](#adrs-and-open-questions) · [Last reviewed](#last-reviewed)

---

## Purpose

`artifacts/` is a **compatibility root** that exists for one job: holding **derived, regenerable, non-authoritative working material** — compiled build outputs, generated documentation sites, QA and lint reports, and ephemeral working files — without polluting the canonical trust path.

It is **not** an evidence store, a publication store, a release store, or a catalog. Trust-bearing material — receipts, proofs, evidence bundles, release manifests, promotion decisions, rollback cards, correction notices, catalog records, and published layers — lives in canonical homes under `data/` and `release/`, **never here**[^artrule].

> [!IMPORTANT]
> If you are about to drop a `release_manifest`, `EvidenceBundle`, `RollbackCard`, `CorrectionNotice`, signed receipt, STAC item, DCAT record, or published layer into this tree — **stop**. It belongs in `data/proofs/`, `data/receipts/`, `data/catalog/`, `data/published/`, or `release/`. Putting it here is the named anti-pattern in [§13.2 / §13.5][dr-13].

### Key terms (used below)

Authority root
: A repo-root folder that carries one of the §3 governance responsibilities. `artifacts/` is **not** one of these.

Compatibility root
: A root that exists for legacy, mirror, deprecated, external-export, or `transitional` reasons. `artifacts/` is one of these.

Trust content
: Receipts, proofs, evidence bundles, release manifests, promotion decisions, rollback cards, correction notices, catalog records, and published layers. **Forbidden here.**

Trust membrane
: The boundary that prevents raw / unreviewed / generated / internal state from becoming public truth. Operational form: `apps/governed-api/`. **Does not read from `artifacts/`.**

---

## Authority level

**Compatibility**, with class **`transitional`**.

| Aspect | Statement |
|---|---|
| Repo-root authority | Compatibility (not canonical). Per [§5][dr-5] of Directory Rules. |
| Class default ([§8.1][dr-81]) | `transitional` — retained pending ADR on full retirement. |
| Independent evolution | **Forbidden.** Compatibility roots MUST NOT evolve independently of canonical homes ([§8.3][dr-83]). |
| Parallel authority | **Forbidden.** No parallel home for schemas, contracts, policy, sources, registries, releases, proofs, or receipts ([§16][dr-16]). |
| ADR required to change root state | Adding / removing / renaming the root, or promoting it to canonical, requires an ADR (§2.4). |

---

## Status

`CONFIRMED` root with **mixed conformance**.

The root is governed by doctrine, but its long-term disposition is an **OPEN question** in Directory Rules [§18][dr-18]: kept as compatibility, or fully retired in favor of `data/receipts/`, `data/proofs/`, `release/`, and `data/published/`?[^retire] Until that ADR lands, this folder operates under the `transitional` default and the strict `build/docs/qa/temporary` scope.

The live tree does not fully meet that target. It contains the four allowed lanes plus tracked `artifacts/release/`; repository scripts and the MapLibre performance workflow also write an untracked `artifacts/perf/` staging tree with receipt-, proof-, correction-, rollback-, and release-shaped filenames. Those files do not become canonical trust objects merely because of their names. They remain outside the governed receipt, proof, and release homes unless separately admitted and reviewed.

> [!CAUTION]
> `artifacts/release/` and `artifacts/perf/` are **not publication evidence**. Do not cite either lane as proof that a release, promotion, correction, rollback, or publication occurred.

### Verified repository snapshot

The following inventory is `CONFIRMED` from Git at `main@86c039f9fda31eb2d4a75112911a5c400ae93a16`.

| Tracked lane | Files | Bytes | Conformance | Current evidence |
|---|---:|---:|---|---|
| Root `README.md` | 1 | 20,290 | Allowed | Compatibility-root contract; stale before this update |
| `build/` | 8 | 164,397 | Allowed lane | READMEs, ignore policy, and `PROPOSED` environment/tool-version scaffolds; no compiled payload is tracked |
| `docs/` | 2 | 47,721 | Allowed lane | README plus `.gitkeep`; no generated docs-site payload or build manifest is tracked |
| `qa/` | 26 | 410,757 | Allowed lane, mixed content maturity | README scaffolds plus small placeholder coverage/lint/validation samples; local JUnit output is ignored |
| `release/` | 5 | 78,114 | **Nonconforming / `BLOCKED_ADR`** | Domain README scaffolds plus one `PROPOSED` `release_manifest.json` placeholder |
| `temporary/` | 2 | 13,251 | Allowed lane | README plus `.gitkeep`; contents are expected to be ephemeral |
| **Total** | **44** | **734,530** | **HOLD** | Inventory excludes generated, ignored, and untracked run output |

> [!NOTE]
> `artifacts/perf/` is absent from the tracked snapshot, but it is an executable output target in the Makefile, MapLibre scripts, and `.github/workflows/maplibre-perf-governance.yml`. Its absence from Git does not resolve its placement conflict.

---

## What belongs here

Accepted contents — **derived, regenerable, non-authoritative** material only:

| Subdir | Accepted contents | Verified repository use |
|---|---|---|
| `build/` | Compiled outputs and distributables | Tracked scaffold and build-environment metadata; generated payloads are replaceable and ignored by the lane-local `.gitignore` |
| `docs/` | **Generated** documentation outputs | `.github/workflows/docs-build.yml` checks the non-authoritative preview lane and rejects trust-bearing manifest fields if a docs-build manifest appears |
| `qa/` | QA and inspection reports | `make boundary-guards-ci` and `.github/workflows/policy-boundary-guards.yml` write JUnit output here; the workflow uploads it only as a CI artifact |
| `temporary/` | Ephemeral working files | Tracked scaffold only; run debris must be ignored or pruned and must never become an input to a governed decision |

### Governed target structure

```text
artifacts/
├── README.md       # this file — declares class and what does NOT belong
├── build/          # compiled outputs, distributables
├── docs/           # generated documentation (mkdocs site, API reference)
├── qa/             # QA reports, lint output, test coverage
└── temporary/      # ephemeral; gitignored or pruned regularly
```

> [!TIP]
> Source documentation (`docs/`), source code (`apps/`, `packages/`, `tools/`, `scripts/`), and **input** fixtures (`fixtures/`, `tests/fixtures/`) are **inputs to** this folder — they do not live in it. If a file is hand-authored and reviewed as source-of-record, it does not belong under `artifacts/`.

---

## What does NOT belong here

**Trust content is forbidden in `artifacts/`.** The list below is as load-bearing as the "what belongs" list. Each item has a canonical home:

| Forbidden here | Why | Canonical home |
|---|---|---|
| `EvidenceBundle` / evidence sidecars | Authoritative support for claims; resolved via the trust membrane | `data/proofs/<domain>/` |
| Run receipts, transform receipts, redaction receipts | Append-only process memory | `data/receipts/<domain>/` |
| `ReleaseManifest` | Release **decision** artifact | `release/manifests/` |
| `RollbackCard` | Rollback decision artifact | `release/rollback_cards/` |
| `CorrectionNotice` | Public correction artifact | `release/correction_notices/` |
| Promotion decisions, gate decision envelopes | Governed state transition records | `release/` + `data/proofs/` |
| STAC items / collections, DCAT records, PROV-JSON | Catalog records | `data/catalog/stac/`, `data/catalog/dcat/`, `data/catalog/prov/` |
| Published layers (PMTiles, MVT, COG, style JSON, sprites, glyphs) | Released artifacts, manifest-bound | `data/published/layers/<domain>/` |
| Source descriptors, source registry entries | Source authority | `data/registry/<domain>/` |
| Canonical schemas / contracts / policy | Authority homes | `schemas/`, `contracts/`, `policy/` |
| Long-lived, trust-bearing scripts | Must graduate to a real home | `tools/`, `pipelines/`, or `packages/` |
| Hand-authored source documentation | Authored, reviewed text is canonical | `docs/` |

### Observed nonconforming lanes

| Path | Truth status | Why it is held | Safe disposition now |
|---|---|---|---|
| `artifacts/release/` | `CONFIRMED` tracked | A fifth top-level lane exists and includes a `release_manifest.json` placeholder; Directory Rules records this as `OPEN-DR-09-b` | Keep non-authoritative, record drift, and do not move or delete until an accepted ADR and migration plan exist |
| `artifacts/perf/` | `CONFIRMED` executable output target; absent from tracked snapshot | MapLibre tooling writes `RunReceipt`, `ProofPack`, `ReleaseManifest`, correction, rollback, and failure-bundle-shaped files here | Treat only as disposable CI staging; do not cite as canonical receipt, proof, or release; resolve with the MapLibre artifact-placement migration |

### The boundary diagram

```mermaid
flowchart LR
  classDef canon fill:#e6f3ff,stroke:#1a73e8,color:#000;
  classDef compat fill:#fff4e5,stroke:#c87f00,color:#000;
  classDef rule fill:#ffe6e6,stroke:#c00,color:#000;

  subgraph CANON["Canonical trust homes"]
    direction TB
    R["data/receipts/"]:::canon
    P["data/proofs/"]:::canon
    CAT["data/catalog/"]:::canon
    PUB["data/published/"]:::canon
    REL["release/"]:::canon
  end

  subgraph ART["artifacts/ — compatibility"]
    direction TB
    OK["build · docs · qa · temporary"]:::compat
    HOLD["release · generated perf"]:::rule
  end

  RULE["§8.2 placement boundary"]:::rule
  HOLD -->|ADR + migration required| RULE
  RULE --> CANON
```

> [!WARNING]
> A release manifest in `artifacts/`, an evidence bundle in `artifacts/`, or a signed receipt in `artifacts/` is the named **drift anti-pattern** in [§13.2 / §13.5][dr-13]. This repository's confirmed instances are recorded in `docs/registers/DRIFT_REGISTER.md`; migration remains held for ADR-backed planning.

---

## Inputs

Payloads arrive in `artifacts/` from **generators, not authors**:

- CI build steps that compile, bundle, or package source from `apps/`, `packages/`, and `tools/`.
- The docs-build workflow, which treats `artifacts/docs/` as a non-authoritative preview lane.
- `make boundary-guards-ci` and the policy-boundary workflow, which emit a JUnit report under `artifacts/qa/`.
- MapLibre performance scripts and `.github/workflows/maplibre-perf-governance.yml`, which currently stage outputs under conflicted `artifacts/perf/`.
- Pipeline scratch space during runs that have not yet promoted output to canonical lifecycle phases.

`artifacts/` does **not** accept hand-edited, hand-committed working files of record. If a human wants it preserved as authority, it goes to its responsibility root.

---

## Outputs

Material under `artifacts/` is **terminal or transient**:

- `build/` outputs may be uploaded as replaceable build assets; this does not make them published KFM data.
- `docs/` output is a generated preview only. The current docs-build workflow does not treat it as authoritative documentation or release evidence.
- `qa/` reports may be uploaded as CI run artifacts; `.github/workflows/policy-boundary-guards.yml` does this for its JUnit report.
- `temporary/` is pruned. Never relied on by downstream consumers.
- `perf/` output is currently generated by MapLibre tooling, but its trust-shaped objects remain noncanonical and held pending placement resolution.

Nothing under `artifacts/` is consumed by the **trust membrane** ([`apps/governed-api/`](../apps/governed-api/)) or by the public client. Public clients consume governed APIs and released artifacts in `data/published/` — never `artifacts/`.

---

## Validation

Validation is split between executable checks and explicit gaps. A green schema or boundary suite does **not** resolve artifact-placement drift.

| Gate | Current evidence | Status |
|---|---|---|
| Aggregate schema/contract validation | `make validate` invokes configured schema validation and schema/contract tests | Executable |
| Public-boundary invariants | `make boundary-guards` runs control-plane, Explorer adapter, connector/pipeline non-publisher, and Governed API boundary tests | Executable |
| QA report emission | `make boundary-guards-ci` writes `artifacts/qa/policy-boundary-guards.xml`; the workflow verifies and uploads it | Executable, non-authoritative output |
| Generated docs boundary | `.github/workflows/docs-build.yml` verifies `artifacts/docs/` and rejects a docs-build manifest carrying trust-bearing fields | Executable workflow guard |
| MapLibre performance artifact governance | `.github/workflows/maplibre-perf-governance.yml` validates a generated bundle under `artifacts/perf/` | Executable but placement remains `CONFLICTED` |
| Compatibility-root allowlist | No repository-owned executable validator was found that enforces only `build/docs/qa/temporary` | `NEEDS VERIFICATION` / gap |
| Trust-content placement | Current tree and generators include held release-shaped paths under `artifacts/` | `FAIL` as placement conformance; no release claim follows |

A failure on any of these checks SHOULD open an entry in `docs/registers/DRIFT_REGISTER.md`.

### Reviewer's quick check

- [ ] Did the PR add any file under `artifacts/` other than `README.md` or the four allowed subdirectories?
- [ ] Does any new file look like a receipt, proof, manifest, rollback card, correction notice, catalog record, or published layer? If yes, **block and reroute**.
- [ ] Does this README still parse a valid KFM Meta Block v2?
- [ ] Is the §15 section order preserved?
- [ ] Does the change cite a Directory Rules section in the PR body?

---

## Review burden

- **Reviewers required:** repo steward + at least one subsystem owner for any structural change to `artifacts/` (adding a sibling, retiring a sibling, changing class).
- **CODEOWNERS:** the repository-wide catch-all currently routes this tree to `@bartytime4life`. A more-specific `/artifacts/` rule is optional unless ownership is delegated to another verified account or team.
- **ADR required:** any of these MUST open an ADR (per §2.4 / §17 of Directory Rules):
  - Promoting `artifacts/` to canonical.
  - Retiring `artifacts/` entirely (the [§18][dr-18] open question).
  - Adding a new top-level child beyond `build/`, `docs/`, `qa/`, `temporary/`.
  - Reversing the trust-content prohibition.

---

## Related folders

| Folder | Relationship |
|---|---|
| [`data/raw/`](../data/raw/) · [`data/work/`](../data/work/) · [`data/quarantine/`](../data/quarantine/) · [`data/processed/`](../data/processed/) | Canonical lifecycle phases. **Not interchangeable with `artifacts/`.** |
| [`data/catalog/`](../data/catalog/) | STAC / DCAT / PROV records. Canonical catalog home. |
| [`data/published/`](../data/published/) | Released, manifest-bound public artifacts (tiles, layers). |
| [`data/proofs/`](../data/proofs/) · [`data/receipts/`](../data/receipts/) | Trust content: evidence bundles, run receipts, transform receipts. |
| [`release/`](../release/) | Release decisions: manifests, rollback cards, correction notices. |
| [`apps/governed-api/`](../apps/governed-api/) | Trust membrane. Reads from canonical stores, **not** from `artifacts/`. |
| [`docs/`](../docs/) | Hand-authored documentation source (input to `artifacts/docs/`). |
| [`apps/`](../apps/) · [`packages/`](../packages/) · [`tools/`](../tools/) | Source code (input to `artifacts/build/`). |
| [`tools/validators/`](../tools/validators/) | Validator root. Documentation-oriented lanes exist, but no executable compatibility-root allowlist was found in the pinned snapshot. |
| [`docs/registers/DRIFT_REGISTER.md`](../docs/registers/DRIFT_REGISTER.md) | Where violations are recorded. |
| [`docs/quality/maplibre-perf-governance.md`](../docs/quality/maplibre-perf-governance.md) | Records the open `artifacts/perf/` trust-object placement conflict. |

> [!NOTE]
> Relative links above resolve against the repo root. Targets marked *PROPOSED* may not exist in every checkout; verify before relying on a link.

---

## ADRs and open questions

| ID | Status | Topic |
|---|---|---|
| *Open question* ([§18][dr-18]) | OPEN | Treatment of `artifacts/` — kept as compatibility (current state), or fully retired in favor of `data/receipts/`, `data/proofs/`, `release/`, and `data/published/`? An ADR is needed to close this. |
| `OPEN-DR-09-b` ([§18][dr-18]) | `BLOCKED_ADR` | Resolve the tracked `artifacts/release/` parallel release home through an accepted decision and one-pass migration with rollback. |
| MapLibre performance placement | `CONFLICTED` | Rehome or explicitly stage `artifacts/perf/` receipt-, proof-, correction-, rollback-, and release-shaped outputs without treating staging as authority. |
| ADR-0001 (schema home) | Referenced | Confirms canonical schema home is `schemas/contracts/v1/...`; reinforces that `artifacts/` is **not** a schema home. |

<details>
<summary><strong>If the disposition ADR retires <code>artifacts/</code></strong> — outline of the structural-move plan</summary>

A retirement ADR would follow §14.2 structural-move discipline:

1. Open the ADR with context, decision, consequences, alternatives, migration plan, rollback plan.
2. Inventory current contents and route each subdirectory to its canonical home:
   - `build/` → CI artifact storage and/or release assets.
   - `docs/` → docs-site deployment target (configured under `infra/` or `.github/workflows/`).
   - `qa/` → CI run artifacts uploaded per workflow.
   - `temporary/` → `.gitignore` and a prune schedule.
3. Add a migration manifest under `migrations/` with old → new mapping and `git_sha_before` / `git_sha_after`.
4. Record a deprecation entry in `control_plane/deprecation_register.yaml` with a sunset date.
5. Verify rollback with a dry-run rollback card.
6. Remove the root only after the verification window passes.

</details>

<details>
<summary><strong>If the disposition ADR retains <code>artifacts/</code></strong> — what tightens</summary>

A retain-as-compatibility ADR would lock in the current scope:

1. Pin the class as `transitional` (or promote to `legacy` if no migration is planned).
2. Codify the four-child rule (`build/`, `docs/`, `qa/`, `temporary/`) in the directory-rules validator.
3. Mark this README `status: stable` and bump `version: v1`.
4. Add a CODEOWNERS entry routing all `/artifacts/**` PRs to the docs steward.
5. Wire the trust-content-not-in-`artifacts/` scan into required CI checks.

</details>

---

## Last reviewed

2026-07-22 — verified against `main@86c039f9fda31eb2d4a75112911a5c400ae93a16`. Re-review after an artifacts-disposition ADR, an `artifacts/release/` migration, a MapLibre artifact-path change, or six months of drift.

---

<sub>Governed by [directory-rules.md][dr] — [§5][dr-5] (root tree), [§8][dr-8] (compatibility roots), [§13][dr-13] (anti-patterns), [§15][dr-15] (README contract), [§16][dr-16] (path-validation checklist), §17 (change discipline), [§18][dr-18] (open questions). Any conflict with this README is resolved by Directory Rules, then by an accepted ADR, then by this README.</sub>

[⬆ Back to top](#artifacts)

[^retire]: The §18 open question reads, verbatim: "Treatment of `artifacts/` — kept as compatibility, or fully retired in favor of `data/receipts/`, `data/proofs/`, `release/`, and `data/published/`?" Until an ADR closes this, the folder remains `transitional` and the strict scope applies.

[^artrule]: Per directory-rules.md §8.2: "`artifacts/` MUST NOT be the canonical home for: receipts, proofs, evidence bundles, release manifests, promotion decisions, rollback cards, correction notices, catalog records, published layers."

<!-- Reference-style links (kept at bottom to keep prose clean; update if anchors change) -->
[dr]:     ../docs/doctrine/directory-rules.md
[dr-5]:   ../docs/doctrine/directory-rules.md#5-canonical-root-tree
[dr-8]:   ../docs/doctrine/directory-rules.md#8-compatibility-roots
[dr-81]:  ../docs/doctrine/directory-rules.md#81-common-compatibility-roots-and-their-canonical-homes
[dr-82]:  ../docs/doctrine/directory-rules.md#82-the-artifacts-rule
[dr-83]:  ../docs/doctrine/directory-rules.md#83-compatibility-roots-are-not-parallel-authority
[dr-13]:  ../docs/doctrine/directory-rules.md#13-anti-patterns-and-drift-prevention
[dr-15]:  ../docs/doctrine/directory-rules.md#15-required-readme-contract
[dr-16]:  ../docs/doctrine/directory-rules.md#16-path-validation-checklist-for-reviewers
[dr-18]:  ../docs/doctrine/directory-rules.md#18-open-questions-and-needs-verification
