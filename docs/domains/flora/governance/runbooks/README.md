<a id="top"></a>
<div align="center">

# 🌿 Flora Domain — Governance Runbooks

**Operational procedures for governed flora data lifecycle transitions.**

[![Status](https://img.shields.io/badge/status-proposed-orange)](#) [![Domain](https://img.shields.io/badge/domain-flora-228B22)](#) [![Lifecycle](https://img.shields.io/badge/lifecycle-governed-1f6feb)](#) [![Truth](https://img.shields.io/badge/truth-cite--or--abstain-555)](#) [![ADR](https://img.shields.io/badge/ADR-pending-lightgrey)](#) [![Owners](https://img.shields.io/badge/owners-TBD-lightgrey)](#)

</div>

> **One-line purpose.** Authored runbooks that document **how** the flora domain
> moves data through KFM's RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET →
> PUBLISHED lifecycle under governance — and **who** signs off at each gate.

> [!IMPORTANT]
> **Path under review — `NEEDS VERIFICATION`.**
> The Flora architecture blueprint proposes runbooks at
> `docs/domains/flora/runbooks/`, **not** under a `governance/` subfolder.
> This README accepts the requested nested path
> (`docs/domains/flora/governance/runbooks/`) as a **`PROPOSED`** intermediate
> organization. An ADR (`ADR-flora-runbooks-home.md`) should resolve the home
> before machine files (CI, validators, registries) reference these paths.
> See [Path basis and Directory Rules](#path-basis-and-directory-rules).

---

## Quick jump

- [Status snapshot](#status-snapshot)
- [Scope](#scope)
- [Repo fit](#repo-fit)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Directory tree](#directory-tree)
- [Runbook index](#runbook-index)
- [Where runbooks sit in the lifecycle](#where-runbooks-sit-in-the-lifecycle)
- [Reviewer roles per runbook](#reviewer-roles-per-runbook)
- [Validation and CI hooks](#validation-and-ci-hooks)
- [Definition of done](#definition-of-done)
- [Path basis and Directory Rules](#path-basis-and-directory-rules)
- [Appendix](#appendix)

---

## Status snapshot

| Field | Value | Truth label |
|---|---|---|
| Folder existence | Proposed; depends on flora domain docs landing | `PROPOSED` |
| Filenames in this folder | `flora-ingest.md`, `flora-promotion.md`, `flora-rollback.md` (from blueprint) | `PROPOSED` |
| Parent path (`.../governance/runbooks/`) | Not attested by any visible doctrine | `NEEDS VERIFICATION` |
| Required ADR | `ADR-flora-runbooks-home.md` | `PROPOSED` |
| Owners | flora-steward · release-manager (placeholder) | `UNKNOWN` |
| CI hooks | `flora-ci.yml`, `flora-promotion.yml` | `PROPOSED` |
| Linked schema home | Pending `ADR-flora-schema-home.md` | `NEEDS VERIFICATION` |

---

## Scope

This folder hosts **human-authored, evidence-aware runbooks** that operationalize
KFM's lifecycle law for the flora domain. Each runbook describes:

1. **Action.** Which lifecycle gate or governance action the runbook governs
   (ingest, promotion, rollback, correction).
2. **Gates.** Which evidence and policy gates must hold before the action proceeds.
3. **Reviewers.** Which reviewer role(s) must sign off before the action is durable.
4. **Receipts.** Which proof objects (`EvidenceBundle`, `DecisionEnvelope`,
   `ReleaseManifest`, `ProofPack`, `CorrectionNotice`, `RollbackPlan`,
   `LayerManifest`) the action produces or updates.
5. **Rollback.** How to reverse the action without erasing its audit trail.

Runbooks are **operational doctrine**, not source records, schemas, contracts,
policy bundles, or release manifests. Runbooks **reference** those objects;
they do not **replace** them.

> [!NOTE]
> The flora lane is **rights- and sensitivity-sensitive** by default — rare-plant
> locations, unclear license terms, exact-coordinate occurrences, and Tribal or
> private-landowner data must fail closed. Every runbook in this folder must
> document its sensitivity behavior explicitly.

---

## Repo fit

```text
docs/
└── domains/
    └── flora/
        ├── README.md
        ├── ARCHITECTURE.md
        ├── PUBLICATION_AND_POLICY.md
        ├── PIPELINES_AND_LIFECYCLE.md
        └── governance/                  ← scope of this README (PROPOSED)
            └── runbooks/                ← you are here
                ├── README.md            ← (this file)
                ├── flora-ingest.md      ← PROPOSED
                ├── flora-promotion.md   ← PROPOSED
                └── flora-rollback.md    ← PROPOSED
```

**Upstream (drives this folder)**

- `docs/domains/flora/PIPELINES_AND_LIFECYCLE.md` — lifecycle stage definitions.
- `docs/domains/flora/PUBLICATION_AND_POLICY.md` — public-safety thresholds, rights, sensitivity.
- `docs/adr/ADR-flora-sensitive-location-policy.md` — exact vs. public-safe geometry. *(PROPOSED)*
- `docs/adr/ADR-flora-public-layer-strategy.md` — public layer eligibility. *(PROPOSED)*
- `docs/adr/ADR-flora-source-roles.md` — source role vocabulary. *(PROPOSED)*

**Downstream (consumes this folder)**

- `.github/workflows/flora-ci.yml` — schema/policy/fixture checks. *(PROPOSED)*
- `.github/workflows/flora-promotion.yml` — promotion dry-runs. *(PROPOSED)*
- `release/manifests/` — release lineage referenced from rollback. *(PROPOSED)*
- CODEOWNERS entries for the flora lane.

---

## What belongs here

- Step-by-step **flora-specific** runbooks for ingest, promotion, rollback,
  correction, source activation, and sensitivity escalation.
- Decision tables that map a flora condition (rare-species occurrence,
  unknown rights, taxon-authority change) to a governed action and reviewer role.
- Pointers to the schemas, contracts, policies, fixtures, and CI checks that
  enforce the runbook in code.
- Links to the upstream architecture and policy documents that the runbook obeys.

## What does not belong here

| If it is… | It belongs at… |
|---|---|
| Source data | `data/raw/flora/` *(PROPOSED)* |
| Processed records | `data/processed/flora/{taxa,occurrences,communities,…}/` *(PROPOSED)* |
| Schemas / contracts | `contracts/flora/*.schema.json` **or** `schemas/contracts/v1/domains/flora/*.schema.json`, pending `ADR-flora-schema-home.md` *(NEEDS VERIFICATION)* |
| Policy rules (executable) | `policy/flora/*.rego` *(PROPOSED)* |
| Release manifests / proof packs | `release/manifests/`, `release/proof_packs/` *(PROPOSED)* |
| Cross-domain runbooks (UI, governed AI, security) | `docs/runbooks/` at the docs root |
| Architecture decision records | `docs/adr/` |

---

## Directory tree

```text
docs/domains/flora/governance/runbooks/
├── README.md                   ← orientation and index (this file)
├── flora-ingest.md             ← RAW → WORK/QUARANTINE → PROCESSED
├── flora-promotion.md          ← PROCESSED → CATALOG/TRIPLET → RELEASE → PUBLISHED
└── flora-rollback.md           ← rollback / correction / supersession
```

> All file paths in the tree above are **`PROPOSED`**. Filenames mirror the
> Flora blueprint's runbook list; only the parent path is under review.

---

## Runbook index

| Runbook | Lifecycle gate | Primary reviewer | Status | Priority |
|---|---|---|---|---|
| [`flora-ingest.md`](./flora-ingest.md) | RAW → WORK/QUARANTINE → PROCESSED | Source steward | **PROPOSED** | P0 |
| [`flora-promotion.md`](./flora-promotion.md) | PROCESSED → CATALOG/TRIPLET → RELEASE → PUBLISHED | Release manager · Policy/sensitivity reviewer | **PROPOSED** | P0 |
| [`flora-rollback.md`](./flora-rollback.md) | PUBLISHED → corrected / superseded | Release manager · Domain steward (flora) | **PROPOSED** | P0 |

> **Naming basis.** The three filenames (`flora-ingest`, `flora-promotion`,
> `flora-rollback`) come from Appendix B of the Flora architecture blueprint.
> Adding files (e.g. `flora-correction.md`, `flora-source-activation.md`)
> requires an entry in `VERIFICATION_BACKLOG.md` and a corresponding update
> here.

---

## Where runbooks sit in the lifecycle

```mermaid
flowchart LR
    RAW["RAW<br/>data/raw/flora/"]:::raw
    WORK["WORK / QUARANTINE<br/>data/work · data/quarantine/flora/"]:::work
    PROC["PROCESSED<br/>data/processed/flora/"]:::proc
    CAT["CATALOG / TRIPLET<br/>data/catalog · triplet/flora/"]:::cat
    REL["RELEASE MANIFEST<br/>+ PROOF PACK"]:::rel
    PUB["PUBLISHED<br/>data/published/flora/"]:::pub

    RAW -->|flora-ingest.md| WORK
    WORK -->|flora-ingest.md| PROC
    PROC -->|flora-promotion.md| CAT
    CAT -->|flora-promotion.md| REL
    REL -->|flora-promotion.md| PUB
    PUB -. flora-rollback.md .-> REL
    PUB -. flora-rollback.md .-> CAT

    classDef raw  fill:#fff5d6,stroke:#a07a00,color:#3b2f00;
    classDef work fill:#fde2e2,stroke:#a83232,color:#5b1c1c;
    classDef proc fill:#e2efff,stroke:#3b6db0,color:#15355c;
    classDef cat  fill:#e7f5e0,stroke:#3a7a2c,color:#1c3a14;
    classDef rel  fill:#ece1f7,stroke:#6b3fa0,color:#2d1652;
    classDef pub  fill:#d6f0e6,stroke:#2c7a5d,color:#0f3a2c;
```

> **Diagram status — `PROPOSED`.** Verify alignment with
> `docs/domains/flora/PIPELINES_AND_LIFECYCLE.md` once that file lands.
> Promotion is a **governed state transition**, not a file move; the arrows
> above represent governance, not filesystem motion.

---

## Reviewer roles per runbook

| Runbook | Required reviewer roles | Optional reviewers |
|---|---|---|
| `flora-ingest.md` | Source steward · Domain steward (flora) | Contract/schema reviewer · Security/operator |
| `flora-promotion.md` | Release manager · Policy/sensitivity reviewer · Domain steward (flora) | UI trust reviewer · Repo steward |
| `flora-rollback.md` | Release manager · Domain steward (flora) | Policy/sensitivity reviewer · Security/operator |

Reviewer-role definitions come from the **KFM Build Companion** reviewer-role
table. Each role's enforcement signal (e.g. *"`SourceActivationDecision`
required before connector"*) should be linked from the runbook body — not
restated. See the [Appendix](#appendix) for the compact reference.

> [!CAUTION]
> **Separation of duties.** A single actor must not generate, approve, publish,
> and correct a flora release without a review trail. Runbooks must document
> the actor / approver split explicitly, even when both roles are held by the
> same person during early implementation.

---

## Validation and CI hooks

| Check | Where it lives | Gate behavior |
|---|---|---|
| Schema/fixture tests | `tests/flora/`, `tests/fixtures/flora/` *(PROPOSED)* | Block PR on schema break |
| Policy parity tests | `policy/flora/*.rego` + Python mirror *(PROPOSED)* | Fail-closed on missing rights / sensitivity |
| No-network smoke ingest | `pipelines/flora/` fixture run *(PROPOSED)* | Block on ingest deviation |
| Promotion gate | `.github/workflows/flora-promotion.yml` *(PROPOSED)* | Deny if proof / catalog / review missing |
| Public-safe leak test | `tests/flora/test_no_sensitive_public_leak.py` *(PROPOSED)* | Deny exact rare-species point on public layer |
| Rollback rehearsal | `tests/flora/test_rollback_card.py` *(PROPOSED)* | Deny rollback without lineage refs |
| Catalog closure test | `tests/flora/test_catalog_matrix.py` *(PROPOSED)* | Deny if STAC/DCAT/PROV digests don't align |

> All check paths are **`PROPOSED`** until the Flora blueprint's CI workflows
> are committed. Invoke `flora-ci.yml` locally before merging changes here.

---

## Definition of done

A runbook in this folder is **ready for review** when it can answer all of:

- [ ] **Identity.** What lifecycle gate or governance action does this runbook govern?
- [ ] **Scope.** Which object families (`SourceDescriptor`, `EvidenceBundle`, `DecisionEnvelope`, `ReleaseManifest`, `ProofPack`, `CatalogMatrix`, `CorrectionNotice`, `RollbackPlan`, `LayerManifest`) does it touch?
- [ ] **Inputs.** Which schemas, fixtures, registries, and policies must be valid before starting?
- [ ] **Steps.** What is the smallest reversible procedure?
- [ ] **Gates.** Which CI workflows / policy bundles must pass?
- [ ] **Reviewers.** Which roles must approve, and which signals do they look for?
- [ ] **Receipts.** Which receipts / proofs / manifests does the runbook emit or update?
- [ ] **Rollback.** How is each step reversed without destroying lineage?
- [ ] **Sensitivity.** How does the runbook behave on rare-species, unclear-rights, or imprecise-geometry inputs? *(fail-closed by default)*
- [ ] **Truth labels.** Are `CONFIRMED` / `INFERRED` / `PROPOSED` / `UNKNOWN` / `NEEDS VERIFICATION` applied where confidence varies?

---

## Path basis and Directory Rules

This folder's parent path inserts a `governance/` segment between the flora
domain root and `runbooks/`. Direct evidence on this choice:

- **Flora Architecture Blueprint, Appendix B.** Proposes runbooks at
  `docs/domains/flora/runbooks/` — *no* `governance/` segment.
- **Directory Rules.** Treats `runbooks/` as a **repo-wide responsibility root**
  and treats domain folders as belonging *under* responsibility roots, not as
  parents of new responsibility roots.
- **Whole-UI / Governed-AI Expansion Report.** Places its runbooks at
  `docs/runbooks/ui_*.md` and `docs/runbooks/governed_ai_*.md` — at the docs
  root, not nested in a domain governance subfolder.

Inserting `governance/` is therefore a **`PROPOSED`** organizational refinement
that prioritizes domain-internal cohesion over the doctrinal preference for
flat lane structure. Acceptance requires:

1. **An ADR** — proposed as `ADR-flora-runbooks-home.md` — that records the
   tradeoff, lists the alternatives, and resolves whether `governance/` is a
   compatibility folder or canonical structure.
2. **Sync with `docs/runbooks/README.md`** so cross-domain readers can find
   lane-specific runbooks.
3. **Confirmation against the live repo's existing `docs/domains/<domain>/`
   patterns** (which were not mounted in this session).

> Until the ADR lands, treat any link from machine files (CI, validators,
> registries) to this path as **`NEEDS VERIFICATION`** and prefer relative
> filename references over full-path references.

---

## Appendix

<details>
<summary><b>A. Reviewer-role enforcement signals (compact reference)</b></summary>

Drawn from the KFM Build Companion reviewer-role table:

| Role | Enforcement signal |
|---|---|
| Repo steward | Path-decision cards and ADR review. |
| Contract/schema reviewer | Contract–schema crosswalk passes. |
| Source steward | `SourceActivationDecision` required before connector. |
| Domain steward (flora) | Domain fixtures and source-role table approved. |
| Policy/sensitivity reviewer | Policy fixtures cover risky cases (rare species, unclear rights, imprecise geometry). |
| Release manager | Release dry-run passes. |
| UI trust reviewer | UI payload contract and negative-state tests. |
| Security/operator | No-direct-model-client and deny-internal-paths tests. |

</details>

<details>
<summary><b>B. Object families touched by flora runbooks</b></summary>

| Object family | Runbook(s) | Stage |
|---|---|---|
| `SourceDescriptor` | ingest | RAW intake |
| `IntakeReceipt` | ingest | WORK/QUARANTINE |
| `EvidenceRef` / `EvidenceBundle` | ingest · promotion · rollback | PROCESSED → PUBLISHED |
| `PolicyDecision` / `DecisionEnvelope` | promotion · rollback | publication gate |
| `CatalogMatrix` (STAC/DCAT/PROV) | promotion · rollback | CATALOG/TRIPLET |
| `ReviewRecord` | promotion · rollback | release / rollback |
| `ReleaseManifest` | promotion · rollback | RELEASE → PUBLISHED |
| `ProofPack` | promotion · rollback | RELEASE |
| `CorrectionNotice` | rollback | published lineage |
| `RollbackPlan` | rollback | published lineage |
| `LayerManifest` | promotion · rollback | public layer aliasing |

> Object family names are **`PROPOSED`** at the flora-lane level; canonical
> definitions live (or will live) in `contracts/` per `ADR-flora-schema-home.md`.

</details>

<details>
<summary><b>C. Cross-references</b></summary>

- [`../../README.md`](../../README.md) — flora domain README.
- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md) — flora architecture overview.
- [`../../PIPELINES_AND_LIFECYCLE.md`](../../PIPELINES_AND_LIFECYCLE.md) — lifecycle stage detail.
- [`../../PUBLICATION_AND_POLICY.md`](../../PUBLICATION_AND_POLICY.md) — rights, sensitivity, public-safe rules.
- [`../../VERIFICATION_BACKLOG.md`](../../VERIFICATION_BACKLOG.md) — open verification items including runbook home ADR.
- [`../../../../runbooks/`](../../../../runbooks/) — cross-domain runbooks (docs root).
- [`../../../../adr/`](../../../../adr/) — architecture decision records.

All paths above are **`PROPOSED`** and depend on `docs/domains/flora/` being
populated per the Flora blueprint.

</details>

<details>
<summary><b>D. Truth-label legend</b></summary>

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified this session from attached docs, workspace evidence, tests, logs, or generated artifacts. |
| `INFERRED` | Reasonably derivable from visible evidence but not directly stated. |
| `PROPOSED` | Design, path, placement, or recommendation not yet verified in implementation. |
| `UNKNOWN` | Not resolvable without more evidence. |
| `NEEDS VERIFICATION` | Checkable, but not yet checked strongly enough to act as fact. |

</details>

---

<sub>Status: <b>PROPOSED · DRAFT</b> · Owners: <i>flora-steward · TBD</i> · Last reviewed: <i>YYYY-MM-DD</i> · Schema-home ADR: <i>pending</i> · Runbook-home ADR: <i>pending</i></sub>

[⬆ Back to top](#top)
