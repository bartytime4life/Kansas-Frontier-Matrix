<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Pipeline Gate Reference (RAW → PUBLISHED)
type: standard
version: v0.1
status: draft
owners: OWNER_TBD
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlases/receipt-catalog.md
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - schemas/contracts/v1/receipts/
  - policy/release/
tags: [kfm, atlas, pipeline, gates, lifecycle, doctrine, carrier]
notes:
  - Downstream carrier into Atlas v1.1 §24.6 (Master Pipeline Gate Reference).
  - Atlas §24.6 remains the doctrinal anchor; this file is a navigation aid, not authority.
  - Reconciles two complementary gate framings (transition-named gates §24.6.1 vs Promotion Gates A–G in Build Manual §6.2 / Doctrine Synthesis §8).
  - Pre-RAW gate (EventEnvelope, EventRunReceipt, SourceIntakeRecord) is CONFLICTED — present in adjacent doctrine, not in atlas §24.6.
  - Owners, doc_id, and related links remain placeholders pending mounted-repo verification.
[/KFM_META_BLOCK_V2] -->

# Pipeline Gate Reference (RAW → PUBLISHED)

> **A navigable, carrier-only ladder of every governed lifecycle gate — pre-condition, required artifacts, failure-closed outcome, and reason codes — consolidated from Atlas v1.1 §24.6 with the Promotion Gates A–G content-check framing made explicit.**
> Authority lives in Atlas v1.1 §24.6; this file routes readers into it.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Authority: carrier" src="https://img.shields.io/badge/authority-carrier--only-lightgrey">
  <img alt="Doctrine anchor: Atlas v1.1 §24.6" src="https://img.shields.io/badge/anchor-Atlas%20v1.1%20%C2%A724.6-success">
  <img alt="Lifecycle invariant" src="https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-informational">
  <img alt="Posture" src="https://img.shields.io/badge/posture-fail--closed-critical">
  <img alt="Pre-RAW gate" src="https://img.shields.io/badge/Pre--RAW-CONFLICTED-orange">
</p>

**Quick jump:** [Purpose](#1-purpose-and-role) · [Two framings](#2-two-complementary-gate-framings) · [Lifecycle gates](#3-lifecycle-gates) · [Diagram](#31-diagram) · [Promotion Gates A–G](#4-promotion-gates-ag) · [Closure rules](#5-closure-rules) · [Reason codes](#6-gate-failure-reason-codes) · [PromotionDecision shape](#7-promotiondecision-shape) · [Pre-RAW](#8-pre-raw-gate-conflicted) · [Trust membrane](#9-trust-membrane-invariant) · [ADRs](#11-adr-backlog) · [Verification](#12-verification-checklist)

> [!IMPORTANT]
> **Status:** `PROPOSED file` / `CONFIRMED doctrine` / `UNKNOWN repo implementation depth`
> **Owner:** `OWNER_TBD`
> **Proposed path:** `docs/atlases/pipeline-gate-reference.md`
> **Lane choice:** `docs/atlases/` over `docs/atlas/` — **CONFIRMED at doctrine level** per `directory-rules.md` v1.2 §6.1 and Atlas v1.1 Appendix G; **NEEDS VERIFICATION** that the path itself is currently present in the mounted repo.
> **Truth posture:** *Atlas §24.6 is doctrine.* This file is a carrier. EvidenceBundle, PolicyDecision, ReviewRecord, and ReleaseManifest remain the authoritative carriers of governance — gate tables in this document do not substitute for them.

> [!NOTE]
> **Evidence boundary.** Gate **transitions**, **pre-conditions**, **required artifacts**, **failure-closed outcomes**, and the **closure rules** are `CONFIRMED doctrine` (Atlas v1.1 §24.6.1 and §24.6.2). Reason-code strings are `PROPOSED catalog` per Atlas v1.1 §24.6.3 itself. The Promotion Gates A–G framing in §4 is `CONFIRMED doctrine` per `KFM_Unified_Implementation_Architecture_Build_Manual.md` §6.2 and `kfm_unified_doctrine_synthesis.md` §8, but letter labels themselves are explicitly described as *conventional* in the doctrine synthesis. **Repo implementation depth, validator wiring, policy-as-code coverage, CI gate enforcement, dashboard surfacing, and runtime emission paths remain `UNKNOWN`** — no mounted repo, tests, workflows, manifests, or runtime logs were inspected.

---

## 1. Purpose and role

KFM's lifecycle invariant is `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition**, not a file move. This document is the **navigable carrier** into Atlas v1.1 §24.6 "Master Pipeline Gate Reference," which consolidates the per-domain H. Pipeline shape tables (Atlas v1.0 chs. 3–18) into one universal gate ladder.

> **CONFIRMED doctrine** (Atlas v1.1 §24.6): *Every domain follows the lifecycle invariant RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. This section consolidates the universal gates and the artifacts each gate requires — the things without which the transition fails closed.*

This file exists because:

- The atlas §24.6 ladder is reusable across every KFM domain (spatial foundation, hydrology, soil, atmosphere, geology, fauna, flora, habitat, archaeology, settlements, hazards, roads/rail, agriculture, people/DNA/land, planetary/3D). Per-domain H. Pipeline shape tables instantiate this ladder; this carrier names it.
- Maintainers need a single page that answers: *"What does this transition require? What happens if it's missing? Which receipt or review do I need to produce?"*
- Promotion-as-decision (`PromotionDecision`) and the trust membrane invariant both depend on gate closure being inspectable.

**Non-collapse rules apply.** This Markdown is a navigation aid:

1. **Atlas registers do not substitute for evidence, policy, review state, source authority, or release state** (Atlas v1.1 front matter).
2. **Catalogs, triplets, graph projections, PMTiles, layer manifests, model outputs, summaries, and UI answers are derivative surfaces.** Their claims trace back through `EvidenceRef → EvidenceBundle → receipts → PolicyDecision → ReleaseManifest`. The ladder below is **how** that traceability closes; it is not itself the claim.

---

## 2. Two complementary gate framings

KFM doctrine carries **two** gate vocabularies. They are not duplicates; they answer different questions.

| Framing | Question it answers | Source | Cardinality |
|---|---|---|---|
| **Lifecycle gates** (§24.6.1) | *"Which transition am I closing, and what state does the object end up in?"* | Atlas v1.1 §24.6.1 | 7 named transitions (Admission, Normalization, Validation, Catalog closure, Release, Correction, Rollback) |
| **Promotion Gates A–G** (§6.2) | *"Which content checks must pass before any transition can close?"* | `KFM_Unified_Implementation_Architecture_Build_Manual.md` §6.2; `kfm_unified_doctrine_synthesis.md` §8 | 7 content-check categories (Source identity, Rights, Sensitivity, Schema/contract, Evidence closure, Catalog/provenance, Review/release/rollback) |

**Relationship** (`PROPOSED reconciliation`):

- Lifecycle gates are *transitions in the state machine*. They drive object state.
- Promotion Gates A–G are *required-proof categories*. Several A–G gates fire **inside** a single lifecycle transition. For example, Release (CATALOG → PUBLISHED) requires Gate D (schema), Gate E (evidence closure), Gate F (catalog/provenance), and Gate G (review/release/rollback) all to close.
- A `PromotionDecision` records which A–G gates passed, held, or denied — for whichever lifecycle transition is being attempted.

> [!WARNING]
> **`CONFLICTED` — ADR citation.** `kfm_unified_doctrine_synthesis.md` §8 states that A–G letter labels are *"conventional; the sequence is the doctrine — may be finalized by ADR-S-08 (PROPOSED)."* However, Atlas v1.1 §24.12 maps **ADR-S-08** to *Frontier Matrix cell semantics*, not promotion-gate labeling. This is either (a) a citation drift in the doctrine synthesis, or (b) a missing ADR in the atlas backlog. Reconciliation is `NEEDS VERIFICATION` — likely belongs as a new ADR-S-* entry or a correction to one of the two documents.

---

## 3. Lifecycle gates

> **Doctrinal anchor:** Atlas v1.1 §24.6.1 (the table below is reproduced verbatim; KFM-coined wording and citations are preserved).

### 3.1 Diagram

```mermaid
flowchart LR
    Start([candidate]):::cand --> A{{Admission}}
    A --"SourceDescriptor +<br/>payload hash"--> R[RAW]
    R --> N{{Normalization}}
    N --"TransformReceipt +<br/>ValidationReport (working) +<br/>PolicyDecision"--> W[WORK]
    N -.failure.-> Q[(QUARANTINE)]:::quar
    W --> V{{Validation}}
    V --"ValidationReport PASS +<br/>RedactionReceipt? +<br/>AggregationReceipt?"--> P[PROCESSED]
    P --> C{{Catalog closure}}
    C --"CatalogMatrix +<br/>EvidenceBundle +<br/>graph/triplet?"--> CT[CATALOG / TRIPLET]
    CT --> Rel{{Release}}
    Rel --"ReleaseManifest +<br/>rollback target +<br/>correction path +<br/>ReviewRecord?"--> Pub([PUBLISHED]):::pub
    Pub --> Corr{{Correction}}
    Corr --"CorrectionNotice +<br/>ReviewRecord +<br/>invalidation list"--> Pub2([PUBLISHED']):::pub
    Pub --> RB{{Rollback}}
    RB --"RollbackCard +<br/>CorrectionNotice +<br/>ReleaseManifest revert"--> Prior([prior release]):::pub

    classDef cand fill:#eef,stroke:#557
    classDef quar fill:#fee,stroke:#955
    classDef pub fill:#efe,stroke:#575
```

> Every diamond is a **governed state transition**. Every label on an arrow is the **minimum artifact set** required to close that transition (Atlas §24.6.1 wording).

### 3.2 Gate table

| Gate (transition) | Pre-condition | Required artifacts (`PROPOSED minimum`) | Failure-closed outcome |
|---|---|---|---|
| **Admission** (— → RAW) | Source identity and rights are minimally established at discovery; source-role intent is set. | `SourceDescriptor` (role, authority, rights, sensitivity, cadence); hash of payload or reference. | Source not admitted; logged as candidate awaiting steward. |
| **Normalization** (RAW → WORK / QUARANTINE) | Schema, geometry, time, identity, evidence, rights, and policy rules are runnable. | `TransformReceipt`; `ValidationReport` (working set); `PolicyDecision`; QUARANTINE for failures. | Quarantine with reason; **never silently promotes**. |
| **Validation** (WORK → PROCESSED) | Validators are deterministic and tied to fixtures; required receipts present. | `ValidationReport` PASS; `RedactionReceipt` if sensitivity applies; `AggregationReceipt` if applies. | Stay in WORK; structured `FAIL` outcome. |
| **Catalog closure** (PROCESSED → CATALOG / TRIPLET) | `EvidenceRef`s resolve; catalog matrix and digests close. | `CatalogMatrix` entry; `EvidenceBundle`; graph/triplet projections if applicable. | `HOLD` at PROCESSED; structured `FAIL` outcome; **no public edge**. |
| **Release** (CATALOG / TRIPLET → PUBLISHED) | Review state where required; release authority distinct from the original author when materiality applies. | `ReleaseManifest`; rollback target; correction path; `ReviewRecord` (if required). | `HOLD` at CATALOG; **no public surface change**. |
| **Correction** (PUBLISHED → PUBLISHED′) | Detected error or new evidence; downstream derivatives identified. | `CorrectionNotice`; `ReviewRecord`; invalidation list; `ReleaseManifest` update or supersession. | Stale-state announcement; **no silent edit**. |
| **Rollback** (PUBLISHED → prior release) | Failed release or post-publication failure; targeted prior release identified. | `RollbackCard`; `CorrectionNotice`; `ReleaseManifest` reverts to prior release; downstream derivative invalidation. | Held at current state until rollback validated. |

> Citation per Atlas: `[ENCY] [DIRRULES]` for every row.

### 3.3 Reading notes

- **Failure-closed everywhere.** Every gate's failure path holds, quarantines, or rejects — none silently promote, edit, or release.
- **Receipt families involved.** Each row maps to one or more rows in the Receipt Catalog (see `docs/atlases/receipt-catalog.md` §3 and §5.2). Receipts created earlier remain referenced (not duplicated) at later phases via `EvidenceRef`.
- **Per-domain instantiation.** Every Atlas v1.0 chapter 3–18 carries an "H. Pipeline shape" table that instantiates this same ladder for the domain (Spatial Foundation, Hydrology, Soil, Atmosphere, Geology, Fauna, Flora, Habitat, Archaeology, Settlements, Hazards, Roads/Rail, Agriculture, People/DNA/Land, Cross-Domain, Planetary/3D). All such tables mark the per-stage **Status** as `PROPOSED`, with the **Gate** column reproducing the ladder above.

---

## 4. Promotion Gates A–G

> **Doctrinal anchor:** `KFM_Unified_Implementation_Architecture_Build_Manual.md` §6.2 (Promotion gates A–G); `kfm_unified_doctrine_synthesis.md` §8.
> **Letter-label posture:** Letter labels are **conventional**; the sequence is the doctrine. Letter labels may be finalized by ADR — see §11 (the ADR number itself is `CONFLICTED`).

A–G is the **minimum content-check sequence** the build must preserve. These are the categories the trust membrane closes through, regardless of which lifecycle transition is firing.

| Gate | Purpose | Required proof |
|---|---|---|
| **A. Source identity** | `SourceDescriptor` exists; source role and authority class known. | `SourceDescriptor` validation report. |
| **B. Rights and terms** | License / terms / contact / attribution obligations resolved. | `RightsReviewRecord` *(or `ReviewRecord` with `role = rights-holder`)*. |
| **C. Sensitivity** | Living-person, DNA, archaeology, rare species, infrastructure, cultural sensitivity, private land, or sovereignty risks resolved. | `PolicyDecision` and transform receipts (`RedactionReceipt`, `AggregationReceipt`). |
| **D. Schema / contract** | Artifacts match schemas and API contracts. | `SchemaValidationReport` *(typically a `ValidationReport` instance)*. |
| **E. Evidence closure** | `EvidenceRef` resolves to `EvidenceBundle`; citations valid. | `EvidenceBundle` + `CitationValidationReport`. |
| **F. Catalog / provenance** | STAC / DCAT / PROV and `CatalogMatrix` closed. | `CatalogMatrixReport`. |
| **G. Review / release / rollback** | `PromotionDecision`, release manifest, proof pack, rollback target, correction path. | `PromotionReceipt` + `ReleaseManifest` + `RollbackCard`. |

### 4.1 Which A–G gates fire in which lifecycle transition (`PROPOSED mapping`)

> This mapping is `PROPOSED` — neither Atlas §24.6 nor Build Manual §6.2 enumerates it explicitly. It is offered as a navigation aid and should be confirmed or amended by ADR.

| Lifecycle gate (§3) | A. Source identity | B. Rights | C. Sensitivity | D. Schema | E. Evidence | F. Catalog | G. Review/release/rollback |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Admission | ● | ◐ |  |  |  |  |  |
| Normalization | ● |  | ◐ | ● |  |  |  |
| Validation | ● | ● | ● | ● | ◐ |  |  |
| Catalog closure | ● | ● | ● | ● | ● | ● |  |
| Release | ● | ● | ● | ● | ● | ● | ● |
| Correction | ● |  | ● |  | ● | ● | ● |
| Rollback | ● |  |  |  |  |  | ● |

> Legend: ● firmly required; ◐ required where materiality applies (minimum precheck at earlier stages).

---

## 5. Closure rules

> **Source:** Atlas v1.1 §24.6.2 (Universal closure rules). `CONFIRMED doctrine`.

A transition is **closed** only when **all three** of the following hold:

1. **The required artifacts above exist.**
2. **Every required artifact resolves — not just references — the artifacts it depends on:**
   - `EvidenceRef → EvidenceBundle`
   - `source_id → SourceDescriptor`
   - `model_id → ModelRunReceipt`
   - `policy_ref → PolicyDecision`
3. **The policy gate evaluated and recorded its decision** as a `PolicyDecision`.

> **Missing any of the three means the transition fails closed and the prior state is preserved.**

> [!IMPORTANT]
> **Anti-collapse rule** (Atlas v1.1 front matter; `kfm_unified_doctrine_synthesis.md` §7): *Catalogs, triplets, graph projections, PMTiles, layer manifests, model outputs, summaries, and UI answers are derivative or publication surfaces; they do not become root truth.* The gate ladder is the path through which **evidence becomes a release**; the release is not the evidence.

---

## 6. Gate failure reason codes

> **Source:** Atlas v1.1 §24.6.3 (`PROPOSED catalog`). Reason-code strings are PROPOSED until canonicalized in a schema or policy bundle.

| Failure family | Reason code (`PROPOSED`) | Gate(s) where it fires | Recovery path |
|---|---|---|---|
| Missing required artifact | `MISSING_RECEIPT`, `MISSING_EVIDENCE`, `MISSING_REVIEW` | Normalization / Validation / Catalog / Release | Re-emit missing receipt; re-run review; re-validate. |
| Schema / contract mismatch | `SCHEMA_MISMATCH`, `CONTRACT_DRIFT` | Normalization / Validation | Schema fix and/or ADR; re-run validator. |
| Rights / sensitivity unresolved | `RIGHTS_UNKNOWN`, `SENSITIVITY_UNRESOLVED` | Admission / Validation / Catalog / Release | Steward review; rights resolution; tier reassignment. |
| Source-role collapse risk | `ROLE_COLLAPSE`, `ROLE_DOWNCAST_FORBIDDEN` | Validation / Catalog / Release | Restore source role; refuse upcast. |
| Review state inadequate | `REVIEW_NEEDED`, `REVIEW_INSUFFICIENT`, `REVIEW_REJECTED` | Catalog / Release | Run required review; supply `ReviewRecord`. |
| Release infrastructure error | `RELEASE_MANIFEST_INVALID`, `ROLLBACK_TARGET_MISSING` | Release | Manifest fix; supply rollback target. |

> **Surface mapping.** Per `kfm_unified_doctrine_synthesis.md` §11 finite outcome envelope, every governed gate returns a finite outcome from the small set `{ALLOW, DENY, HOLD, ANSWER, ABSTAIN, ERROR, PASS, FAIL}`. Promotion-gate surfaces specifically return `ALLOW | DENY | HOLD | ERROR` and **must record held/denied gates**, not promote on a partial gate set.

---

## 7. PromotionDecision shape

> **Source:** `kfm_unified_doctrine_synthesis.md` §7 (Promotion as a governed state transition). `CONFIRMED doctrine / PROPOSED shape`.

`PromotionDecision` records a transition attempt — pass, hold, or deny — for whichever lifecycle gate (§3) is being attempted, with full A–G coverage (§4). Promotion is **a decision recorded against evidence**, not an action against a filesystem.

```text
PromotionDecision {
  promotion_id:    stable_id,
  target_stage:    PROCESSED | CATALOG | PUBLISHED,
  inputs:          [EvidenceRef, ValidationReport, PolicyDecision, ...],
  gates_passed:    [Gate A, Gate B, ..., Gate G],
  gates_held:      [...],
  gates_denied:    [...],
  release_target:  ReleaseManifest.id (where applicable),
  rollback_target: prior_release_id (where applicable),
  steward:         actor_id,
  reviewer:        actor_id (where required),
  decision:        ALLOW | DENY | HOLD,
  reason_codes:    [...],
  spec_hash:       <JCS + SHA-256 over canonicalized record>,
  timestamp_utc:   ISO8601
}
```

> **PROPOSED shape — not a schema authority.** Field names, signing posture (DSSE / cosign), and identity convention (JCS + SHA-256) are open at ADR-S-03 (receipt schema layout) and adjacent ADRs. The shape above is illustrative and ports verbatim from the doctrine synthesis.

---

## 8. Pre-RAW gate (`CONFLICTED`)

> [!WARNING]
> **`CONFLICTED` — Pre-RAW is not in Atlas §24.6.** Atlas v1.1 §24.6.1 begins the ladder at Admission (— → RAW). However, `kfm_unified_doctrine_synthesis.md` §6 and `KFM_Unified_Implementation_Architecture_Build_Manual.md` §7.1 both describe a **Pre-RAW** phase with its own artifacts: `EventEnvelope`, `EventRunReceipt`, `SourceIntakeRecord`, `SourceActivationDecision`. This is a real adjacent gate, not an error — but it is not collected into the atlas's universal ladder. Reconciliation is `NEEDS VERIFICATION`.

| Phase | Artifacts (`CONFIRMED corpus presence`) | What it pins |
|---|---|---|
| **Pre-RAW** | `EventEnvelope` | A watcher / upload / source-change event before RAW. |
| **Pre-RAW** | `EventRunReceipt` | Signed pre-RAW admission receipt for the event. |
| **Pre-RAW** | `SourceIntakeRecord` | Admission decision for a new source or idea packet. |
| **Pre-RAW** | `SourceActivationDecision` | Whether and when an admitted source becomes operationally live. |

**Doctrine constraint surfaced for completeness** (`kfm_unified_doctrine_synthesis.md`):

> *Watchers and drift detectors are candidate producers, not publishers. A watcher can say "something changed" and emit receipts; it cannot make a public release true by itself.*

**Resolution direction (`PROPOSED`):** Either extend Atlas §24.6.1 to add a Pre-RAW row (preferred path: Atlas v1.2 amendment), **or** open an ADR-S-* entry to formally treat Pre-RAW as outside the "universal" ladder while keeping it in the trust membrane. Until resolved, this carrier surfaces Pre-RAW as adjacent.

---

## 9. Trust membrane invariant

> **Source:** Atlas v1.1 §24.6.2; `kfm_unified_doctrine_synthesis.md` §7; `directory-rules.md` (trust-membrane references). `CONFIRMED doctrine`.

The gates above are the **only** routes by which content reaches PUBLISHED.

> **The trust membrane forbids any public client, any normal UI surface, and any released AI surface from reaching RAW, WORK, QUARANTINE, canonical/internal stores, graph internals, vector indexes, source APIs, or direct model runtimes. The gates above are the only routes by which content reaches PUBLISHED, and PUBLISHED is the only state from which the governed API may emit `ANSWER`.**

Corollaries:

- **Watchers are not publishers.** Pre-RAW receipts are admission proof; they do not authorize public claims.
- **Catalogs, tiles, scenes, graph projections, vector indexes, summaries, dashboards, and AI answers are derivative.** They sit on the PUBLISHED side of the membrane; they do not become sovereign truth simply because they exist.
- **Administrative shortcuts** (operator-only paths into earlier stages) must be constrained, documented, and prevented from becoming the normal public path.

---

## 10. Cross-references

| Reference | Role | Status |
|---|---|---|
| Atlas v1.1 §24.6 (Master Pipeline Gate Reference) | **Doctrinal anchor for this file.** | `CONFIRMED doctrine` |
| Atlas v1.1 §24.6.1 (Lifecycle gates table) | Primary table source for §3.2. | `CONFIRMED doctrine` |
| Atlas v1.1 §24.6.2 (Universal closure rules) | Primary source for §5. | `CONFIRMED doctrine` |
| Atlas v1.1 §24.6.3 (Gate failure reason codes) | Primary source for §6. | `CONFIRMED doctrine` |
| Atlas v1.1 §24.2 (Master Receipt Catalog) | Receipt classes referenced from every gate row. | `CONFIRMED doctrine` |
| `docs/atlases/receipt-catalog.md` | Companion carrier — receipt families, schema home, lifecycle-phase attachment. | `PROPOSED file` |
| `KFM_Unified_Implementation_Architecture_Build_Manual.md` §6.2 (Promotion gates A–G) | Primary source for §4. | `CONFIRMED corpus presence` |
| `KFM_Unified_Implementation_Architecture_Build_Manual.md` §7.1 (Object map) | Source for Pre-RAW artifacts in §8. | `CONFIRMED corpus presence` |
| `kfm_unified_doctrine_synthesis.md` §6 (Lifecycle phases) | Source for Pre-RAW artifacts in §8. | `CONFIRMED corpus presence` |
| `kfm_unified_doctrine_synthesis.md` §7 (Promotion as a governed state transition) | Primary source for §7 `PromotionDecision` shape. | `CONFIRMED corpus presence` |
| `kfm_unified_doctrine_synthesis.md` §8 (Promotion gates A–G) | Corroborates §4; also source of `CONFLICTED` ADR-S-08 citation noted in §2. | `CONFIRMED corpus presence` |
| `kfm_unified_doctrine_synthesis.md` §11 (Finite outcome envelope) | Source for surface-mapping note in §6. | `CONFIRMED corpus presence` |
| Per-domain Atlas v1.0 chs. 3–18 H. tables | Per-domain instantiation of the universal ladder. | `CONFIRMED doctrine` |
| `directory-rules.md` v1.2/v1.3 | `docs/atlases/` is the canonical home (§6.1); trust-membrane references; ADR-class boundaries (§2.4). | `CONFIRMED at commit b6a279…` |

---

## 11. ADR backlog

| ADR | Title (`PROPOSED`) | Why ADR-class | Status |
|---|---|---|---|
| **ADR-S-08** *(per Atlas §24.12)* | Frontier Matrix cell semantics | Adjacent to A–G framing only via cross-cutting receipt families. | Open |
| **ADR-S-09** | Reviewer separation-of-duties threshold | Triggered by gate G (Release). | Open |
| **ADR-S-* (proposed)** | Letter-label canonicalization for Promotion Gates A–G | Doctrine synthesis §8 cites "ADR-S-08" but atlas §24.12 ADR-S-08 covers Frontier Matrix cells. Mismatch flagged in §2. | Not yet filed |
| **ADR-S-* (proposed)** | Pre-RAW gate canonicalization | Atlas §24.6 begins at Admission; doctrine synthesis §6 + Build Manual §7.1 carry a Pre-RAW phase. Mismatch flagged in §8. | Not yet filed |
| **ADR-S-* (proposed)** | A–G ↔ lifecycle-gate mapping (§4.1) | §4.1 mapping is PROPOSED in this carrier; canonical mapping is unspecified in attached doctrine. | Not yet filed |

> ADR-S numbering: existing slots S-01 through S-15 are listed in Atlas v1.1 §24.12. New ADR proposals here are deliberately left unnumbered to avoid claiming an allocation Atlas §24.12 has not made.

---

## 12. Verification checklist

- [ ] Confirm the target path `docs/atlases/pipeline-gate-reference.md` does not already exist; resolve any naming collision with a `docs/atlas/` mirror.
- [ ] Confirm filename convention vs. neighboring atlas Markdown (`KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` uses underscores+UpperCase; `docs/atlases/receipt-catalog.md` and this file use hyphens+lowercase). Decide by docs-steward rule, ADR, or migration note.
- [ ] Confirm `OWNER_TBD` — docs steward + release-discipline / promotion subsystem owner.
- [ ] Confirm `doc_id` allocation convention; do not invent UUIDs.
- [ ] Confirm `docs/atlases/receipt-catalog.md` exists or is being authored as the companion carrier referenced from every gate row.
- [ ] Confirm `policy/release/` and `policy/domains/<domain>/` are the canonical homes for OPA/Rego policies that enforce gates (per `directory-rules.md` v1.2 drift entry).
- [ ] Confirm presence of `schemas/contracts/v1/receipts/` and that `ReleaseManifest`, `PromotionReceipt`, `RollbackCard`, `CorrectionNotice` schemas match the §3 and §7 shape claims.
- [ ] Confirm the `data/published/` and `release/` roots accept only objects with `PromotionDecision = ALLOW`; nothing reaches them on a partial gate set.
- [ ] Confirm `tests/` has fixture-driven validators for each gate row in §3.2 and each reason code in §6 (positive and negative paths).
- [ ] Resolve **`CONFLICTED`** items from §2 and §8 via ADR or atlas amendment; until then, treat them as live divergence and document in `docs/registers/DRIFT_REGISTER.md`.
- [ ] Cross-check §4.1 A–G ↔ lifecycle-gate mapping against any policy-as-code matrix; mark resolved cells `CONFIRMED`, unresolved cells remain `PROPOSED`.
- [ ] Confirm CI surfaces the gate state per-object on dashboards or runbooks (per the seed-card FEATURE for Universal Pipeline Gate Reference in `kfm_full_atlas_seed_cards.md`).
- [ ] Run `Diagram syntactic check`: the Mermaid block in §3.1 renders on GitHub.

---

## 13. Rollback / supersession

| Condition | Action |
|---|---|
| Atlas v1.1 §24.6.1 ladder changes (Atlas v1.2 or successor amends rows) | Update §3.2 in lock-step; preserve §3.1 diagram alignment; bump file `version`. |
| Atlas v1.1 §24.6.3 reason codes are canonicalized in schema or policy | Update §6 wording from `PROPOSED` to `CONFIRMED`; cite the schema or policy bundle as the new authority. |
| ADR resolves the A–G ↔ lifecycle-gate mapping in §4.1 | Replace `PROPOSED mapping` block with the canonical mapping; preserve diff in lineage notes. |
| ADR resolves Pre-RAW status (§8) | Either delete §8 (if Pre-RAW joins atlas ladder) or upgrade §8 from `CONFLICTED` to `CONFIRMED adjacent`. |
| Build Manual §6.2 or Doctrine Synthesis §8 wording changes for A–G | Update §4 verbatim; do not paraphrase. |
| `directory-rules.md` re-homes atlas Markdown | Move file; preserve anchor IDs; add lineage note to KFM Meta Block v2. |
| This file is found to drift from atlas wording on `CONFIRMED doctrine` rows | Restore atlas wording verbatim; the atlas wins. |
| This file is found to overclaim implementation (e.g., asserts CI enforcement without repo evidence) | Demote claim to `PROPOSED` / `UNKNOWN`; never resolve drift by lowering the truth label. |

**Rollback target:** `ROLLBACK_TARGET_TBD` (PROPOSED: prior commit ref of this file as recorded in `release/manifests/`).

---

## 14. Source ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Atlas v1.1 §24.6 *(Master Pipeline Gate Reference)* | `CONFIRMED doctrine` | §3.1 diagram; §3.2 gate table; §5 closure rules; §6 reason codes; §9 trust membrane. | Does not prove repo implementation; reason codes are `PROPOSED` per the atlas itself; Pre-RAW is absent. |
| Atlas v1.1 §24.2 *(Master Receipt Catalog)* | `CONFIRMED doctrine` | Receipt classes referenced in §3.2 (TransformReceipt, ValidationReport, RedactionReceipt, etc.). | Field shapes are `PROPOSED` per the atlas. |
| Atlas v1.0 chs. 3–18 H. Pipeline shape tables | `CONFIRMED doctrine` | §3.3 per-domain instantiation note. | Stage **Status** in those tables is `PROPOSED` per the atlas. |
| `KFM_Unified_Implementation_Architecture_Build_Manual.md` §6.2 *(Promotion gates A–G)* | `CONFIRMED corpus presence` | §4 A–G table. | Build manual is `CONFIRMED doctrine / PROPOSED implementation`. |
| `KFM_Unified_Implementation_Architecture_Build_Manual.md` §7.1 *(Object map)* | `CONFIRMED corpus presence` | §8 Pre-RAW artifacts. | Object map is broader than this file; only the Pre-RAW slice is used. |
| `kfm_unified_doctrine_synthesis.md` §§6, 7, 8, 11 | `CONFIRMED corpus presence` | §7 `PromotionDecision` shape; §4 A–G corroboration; §6 surface mapping; §8 Pre-RAW corroboration; §2 `CONFLICTED` ADR-S-08 citation. | Doctrine synthesis is a cross-document synthesis; not a schema authority. |
| `kfm_full_atlas_seed_cards.md` (Universal Pipeline Gate Reference feature card) | `CONFIRMED corpus presence` | §12 dashboard / runbook expectation. | Seed card itself is `PROPOSED` design; not implementation. |
| `directory-rules.md` v1.2/v1.3 | `CONFIRMED at commit b6a279…` | §6.1 atlas home; §2.4 ADR-class boundaries; §10 ADR cross-refs. | Path-level claims for new files (this one) remain `PROPOSED`. |

> **Memory is not evidence.** Every consequential claim in this file is traceable to one of the sources above, an atlas table reproduced verbatim, or an explicit `PROPOSED` / `NEEDS VERIFICATION` / `CONFLICTED` placeholder.

---

<p align="right"><a href="#pipeline-gate-reference-raw--published">↑ Back to top</a></p>
