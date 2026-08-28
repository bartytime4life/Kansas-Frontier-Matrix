<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-source-role-matrix
title: Geology and Natural Resources — Source-Role Matrix
type: standard
version: v1
status: draft
owners: <geology-domain-steward> · <source-steward> · <docs-steward>   # placeholder — confirm in CODEOWNERS
created: 2026-06-04
updated: 2026-06-04
policy_label: public
related:
  - docs/domains/geology/SOURCES.md
  - docs/domains/geology/SOURCE_REGISTRY.md
  - docs/domains/geology/SOURCE_LEDGER.md
  - docs/domains/geology/SENSITIVITY.md
  - docs/domains/geology/SCOPE.md
  - docs/domains/geology/README.md
  - ai-build-operating-contract.md   # CONTRACT_VERSION = "3.0.0"
  - schemas/contracts/v1/source/source-descriptor.json
  - docs/doctrine/directory-rules.md
tags: [kfm, geology, source-role, matrix, anti-collapse, governance]
notes:
  - The matrix artifact for the geology lane: source-family × allowed-role grid, role × object-family permitted/forbidden grid, and the collapse-pair DENY matrix. Distinct from SOURCES.md (prose typology), SOURCE_REGISTRY.md (admission doctrine), SOURCE_LEDGER.md (per-entry control surface).
  - Doctrine-adjacent; pins CONTRACT_VERSION = "3.0.0".
  - Role classes and anti-collapse rows are CONFIRMED (Atlas §24.1.1 / §24.1.2; geology named in the aggregate-as-per-place row). Family×role and role×object cell assignments are INFERRED defaults the descriptor fixes per record.
  - Object-family naming drift (§10.B short vs §10.E Reference) surfaced as CONFLICTED. All repo paths PROPOSED.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources — Source-Role Matrix

> The lookup grids that bind geology sources to roles and roles to claims. **Grid A**: which source family may carry which of the seven source roles. **Grid B**: which object families a role may support (`permitted_claims`) and must not (`not_authoritative_for`). **Grid C**: the collapse pairs that fail closed. This is the matrix a reviewer and a validator read; the prose lives in `SOURCES.md`.

![status](https://img.shields.io/badge/status-draft-orange)
![domain](https://img.shields.io/badge/domain-geology%20%5BDOM--GEOL%5D-blue)
![doctrine](https://img.shields.io/badge/roles-CONFIRMED%20%C2%A724.1.1-blue)
![anti-collapse](https://img.shields.io/badge/anti--collapse-fail%20closed-red)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-lightgrey)

| Field | Value |
|---|---|
| **Status** | `draft` |
| **Owners** | `<geology-domain-steward>` · `<source-steward>` · `<docs-steward>` *(placeholders — confirm in CODEOWNERS)* |
| **Role authority** | Atlas §24.1.1 (seven canonical classes); §24.1.2 (anti-collapse DENY conditions) |
| **Family authority** | `DOM-GEOL §10.D` (eight source families) |
| **Object authority** | `DOM-GEOL §10.B` (owned object families) |
| **Lane** | Geology / Natural Resources — `[DOM-GEOL]`, Atlas Ch. 10 |
| **Updated** | 2026-06-04 |

> [!IMPORTANT]
> **The grids are defaults; the descriptor decides.** A cell in Grid A or B is the *typical* allowance; the binding fact for any record is its `SourceDescriptor` (`source_role`, `permitted_claims`, `not_authoritative_for`). Where a grid and a descriptor disagree, the descriptor wins and the conflict is logged in `docs/registers/DRIFT_REGISTER.md`. Grid C (collapse pairs) is **not** a default — it is fail-closed doctrine.

---

## Contents

- [1. What this matrix is](#1-what-this-matrix-is)
- [2. The seven source roles (legend)](#2-the-seven-source-roles-legend)
- [3. Grid A — source family × allowed role](#3-grid-a--source-family--allowed-role)
- [4. Grid B — role × object family (permitted / forbidden)](#4-grid-b--role--object-family-permitted--forbidden)
- [5. Grid C — collapse pairs that fail closed](#5-grid-c--collapse-pairs-that-fail-closed)
- [6. Reading the matrix (worked lookups)](#6-reading-the-matrix-worked-lookups)
- [7. Open questions & verification](#7-open-questions--verification)
- [8. Related docs](#8-related-docs)

---

<a id="1-what-this-matrix-is"></a>

## 1. What this matrix is

A reviewer admitting a geology record, or a validator checking one, needs a fast lookup: *can this family carry this role, can this role back this claim, and which conflations are forbidden?* This document is those three grids, scoped to geology. It is the tabular companion to the prose in `SOURCES.md`.

| Doc | Form | This matrix's relationship |
|---|---|---|
| `SOURCES.md` | Prose typology of families + the seven roles | The narrative this matrix tabulates |
| `SOURCE_REGISTRY.md` | Admission / authority-control doctrine | Consumes Grids A–C at the admission gate |
| `SOURCE_LEDGER.md` | Per-entry append-only control surface | Records each admitted entry's resolved role |
| `SOURCE_ROLE_MATRIX.md` *(this doc)* | **The grids** — family×role, role×object, collapse pairs | The lookup tables |

> [!NOTE]
> The corpus calls the integrity rule that these grids enforce **"matrix-cell semantics"** (Atlas §24.1.2): a value's source role and geometry scope travel with it, and a join that violates a cell's semantics is denied.

[↑ Back to top](#top)

---

<a id="2-the-seven-source-roles-legend"></a>

## 2. The seven source roles (legend)

**CONFIRMED doctrine (Atlas §24.1.1).** Role is set at admission and preserved through promotion. Legend for the grids below:

| Symbol | Role | One-line |
|---|---|---|
| **O** | `observed` | Direct reading / first-hand record tied to place + time. |
| **R** | `regulatory` | Authoritative determination by a governing body. |
| **M** | `modeled` | Derived from inputs/assumptions; uncertainty preserved. |
| **G** | `aggregate` | Summary over a unit; per-record fidelity lost. |
| **A** | `administrative` | Agency compilation for registration/accounting. |
| **C** | `candidate` | Awaiting validation; not yet authoritative. |
| **S** | `synthetic` | Simulated/reconstructed/AI; no first-hand observation. |

Cell legend for the grids: **✓** = typical allowed role/claim · **△** = allowed only with the role-conditional receipt named · **✗** = forbidden (anti-collapse).

[↑ Back to top](#top)

---

<a id="3-grid-a--source-family--allowed-role"></a>

## 3. Grid A — source family × allowed role

Which roles each geology source family **may** carry (one role per `SourceDescriptor`; a multi-role publisher gets one descriptor per role). Families 1–8 are the CONFIRMED `§10.D` set; out-of-list families are tracked in `SOURCES.md`.

| Source family | O | R | M | G | A | C | S |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| KGS data & geologic maps | ✓ | – | △ | ✓ | ✓ | ✓ | – |
| KGS surficial geology & maps | ✓ | – | △ | – | ✓ | ✓ | – |
| USGS NGMDB / GeMS | – | – | △ | ✓ | ✓ | ✓ | – |
| KGS oil & gas wells / production | ✓ | ✓ | – | ✓ | ✓ | ✓ | – |
| KCC oil & gas regulatory data | – | ✓ | – | ✓ | ✓ | ✓ | – |
| KGS/KDHE WWC5 water-well program | ✓ | ✓ | – | ✓ | ✓ | ✓ | – |
| KGS LAS digital well logs / tops | ✓ | – | △ | – | – | ✓ | – |
| USGS MRDS | ✓ | – | – | ✓ | ✓ | ✓ | – |
| *(any modeled/AI derivative)* | – | – | △ | – | – | – | △ |

> [!NOTE]
> **`△` for M and S** means the descriptor MUST carry the role-conditional receipt: `role_model_run_ref` → `ModelRunReceipt` for **M**; `role_synthetic_basis` + `RealityBoundaryNote` for **S** (Atlas §24.1.3). **`C` (candidate)** is available to every family at intake but carries no public surface until promoted. No geology source family is natively **synthetic**; synthetic content arises only from KFM-side modeling/AI and is never relabeled observed.

[↑ Back to top](#top)

---

<a id="4-grid-b--role--object-family-permitted--forbidden"></a>

## 4. Grid B — role × object family (permitted / forbidden)

Which geology object families (`DOM-GEOL §10.B`) a role may **support** vs must **not** be cited as authoritative for. This is the grid that fills a descriptor's `permitted_claims` / `not_authoritative_for`.

> [!CAUTION]
> **Object-family naming drift (CONFLICTED).** Columns use the §10.B short forms; §10.E uses `…Reference` / variant forms (`BoreholeReference`, etc.) and `ResourceEstimate` where §10.B says `Resource Deposit`. Canonical set unresolved — see [§7](#7-open-questions--verification).

| Object family | O | R | M | G | A | C | S |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `GeologicUnit`, `Lithology` | ✓ | ✗ | △ | ✓(agg) | ✓ | C | ✗ |
| `StratigraphicInterval`, `GeologicAge` | ✓ | ✗ | △ | – | ✓ | C | ✗ |
| `FaultStructure` | ✓ | ✗ | △ | – | ✓ | C | ✗ |
| `CrossSection` | ✓ | ✗ | △ | – | – | C | △(S) |
| `Borehole`, `CoreSample` | ✓ | △ | ✗ | – | △ | C | ✗ |
| `WellLog` | ✓ | ✗ | △ | – | – | C | ✗ |
| `GeophysicalObservation` | ✓ | ✗ | △ | ✓(agg) | – | C | ✗ |
| `GeochemistrySample` | ✓ | ✗ | △ | ✓(agg) | – | C | ✗ |
| `MineralOccurrence` | ✓ | ✗ | △ | ✓(agg) | ✓ | C | ✗ |
| `ResourceDeposit` | △ | ✗ | △ | ✓(agg) | – | C | ✗ |
| `ResourceEstimate` | ✗ | ✗ | ✓(needs receipt) | ✓(agg) | – | C | ✗ |
| extraction permit / production *(context)* | ✗ | ✓ | ✗ | ✓(agg) | ✓ | C | ✗ |
| `ExtractionSite`, `ReclamationRecord` | ✓ | ✓ | – | – | ✓ | C | ✗ |
| `HydrostratigraphicUnit` | ✓ | ✗ | △ | – | ✓ | C | ✗ |

Reading: **✓** typical · **△** allowed with the role's receipt (M → `ModelRunReceipt`; S → `RealityBoundaryNote`) · **✓(agg)** allowed only at the declared `role_aggregation_unit`, never per-place · **C** citable only as candidate evidence in `WORK / QUARANTINE` · **✗** forbidden (anti-collapse).

> [!IMPORTANT]
> Two cells encode the load-bearing geology rules: `ResourceEstimate` is **✗ for observed** (an estimate is modeled, never a measurement) and permit/production is **✗ for observed/modeled** (it is regulatory/administrative context, never an observed geologic fact). These are the matrix form of the claim-class distinctness rule (`SCOPE.md §5`).

[↑ Back to top](#top)

---

<a id="5-grid-c--collapse-pairs-that-fail-closed"></a>

## 5. Grid C — collapse pairs that fail closed

**CONFIRMED doctrine (Atlas §24.1.2).** These conflations are denied at the trust membrane and `ABSTAIN`ed at AI surfaces. Geology is **named** in the aggregate-as-per-place row.

| Collapse (from → as) | Denied outcome | Required guardrail | Geology exposure |
|---|---|---|---|
| **G → O** aggregate cited as per-place truth *(geology named)* | DENY join aggregate→single record; ABSTAIN at AI | `AggregationReceipt`; geometry-scope guard; matrix-cell semantics | County occurrence rollup / basin estimate read per-well |
| **M → O** modeled product labeled observed | DENY at publication; ABSTAIN at AI | `ModelRunReceipt` + uncertainty surface + role-preserving DTO field | Resource estimate / geophysical inversion shown as a measurement |
| **R → O** regulatory layer labeled observed event | DENY publication of regulatory layer as event evidence | Separate regulatory and observed lanes; UI banner | KCC filing layer shown as observed structure/production |
| **A → O** administrative compilation cited as observation | DENY publication of compilation as observed timeline | Source-role tag preserved; named admin types | NGMDB index entry treated as an observed unit polygon |
| **C → public** candidate exposed on a public surface | DENY at trust membrane; route to `QUARANTINE` | Promotion gate; no `PUBLISHED` edge to `WORK`/`QUARANTINE` | Quarantined KGS connector output reaches a layer |
| **S → O** synthetic presented as observed reality | DENY publication; HOLD for steward review; ABSTAIN at AI | `RealityBoundaryNote`; `RepresentationReceipt`; UI badge | Synthetic subsurface surface shown as observed structure |
| **AI text → evidence** | DENY publication; ABSTAIN at Focus Mode | Cite-or-abstain; `AIReceipt` mandatory | A Focus Mode geology answer cited as the source |

> [!WARNING]
> Grid C also folds in the **geology-specific claim-class collapses** (`SCOPE.md §5`): Occurrence→Deposit, Deposit→Reserve, Estimate→Production, Permit→Operation. Each is a special case of a Grid C row (typically G→O or R→O) plus the object-level distinctness rule, and each fails closed.

[↑ Back to top](#top)

---

<a id="6-reading-the-matrix-worked-lookups"></a>

## 6. Reading the matrix (worked lookups)

<details>
<summary>Four worked lookups across the grids</summary>

**1. "Can USGS MRDS back a resource estimate?"** Grid A: MRDS may carry O/G/A, **not M**. Grid B: `ResourceEstimate` is **✗ for observed** and needs M-with-receipt. → **No.** MRDS can support `MineralOccurrence` (✓) or an aggregate (✓agg); an estimate needs a modeled descriptor with `role_model_run_ref`.

**2. "Can a KCC production figure be shown for a single well as observed?"** Grid A: KCC carries R/G/A. Grid B: permit/production is **✗ for observed**, **✓(agg)** only. Grid C: **R→O** and **G→O** both fail closed. → **No.** Regulatory/aggregate context only, never per-well observed truth.

**3. "Can a KGS modeled unit polygon be published as observed bedrock?"** Grid A: KGS may carry M (△, needs receipt). Grid B: `GeologicUnit` is **△ for modeled**. Grid C: **M→O** fails closed. → **Yes as modeled** (with `ModelRunReceipt`), **never relabeled observed**.

**4. "Can a quarantined KGS feed change appear on the public map?"** Grid A: candidate (C) is available at intake. Grid C: **C→public** fails closed. → **No** until promoted; it lives in `WORK/QUARANTINE` as candidate evidence only.

</details>

[↑ Back to top](#top)

---

<a id="7-open-questions--verification"></a>

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-GEOL-SRM-01 | Ratify Grid A family×role defaults — which cells are canon vs reviewer judgment per descriptor? | `<source-steward>` + `<geology-domain-steward>` | Steward review; encode in descriptor templates |
| OQ-GEOL-SRM-02 | Ratify Grid B role×object `permitted_claims`/`not_authoritative_for` defaults. | `<geology-domain-steward>` | Schema review of `contracts/domains/geology/`; anti-collapse tests |
| OQ-GEOL-SRM-03 | Resolve object-family naming drift (§10.B short vs §10.E `…Reference`; `Resource Deposit` vs `ResourceEstimate`). | `<geology-domain-steward>` | ADR or schema PR; drift entry |
| OQ-GEOL-SRM-04 | Confirm `role_aggregation_unit` / `role_model_run_ref` / `role_synthetic_basis` fields exist in the mounted `SourceDescriptor` schema. | `<schema-steward>` | Directory Rules §7.4 + ADR-0001 check |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before this document promotes from `draft` to `published`:

1. Ratification of Grid A and Grid B defaults (OQ-GEOL-SRM-01, -02).
2. The canonical geology object-family name set (OQ-GEOL-SRM-03).
3. Presence of the role-conditional fields in the mounted `SourceDescriptor` schema (OQ-GEOL-SRM-04).

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial geology source-role matrix authored | new | Provide the tabular family×role / role×object / collapse-pair grids complementing the SOURCES.md prose |
| Grids grounded to Atlas §24.1.1 / §24.1.2 | clarification | Use the canonical seven roles and the verbatim anti-collapse failure rows (geology named) |
| Object-family naming drift surfaced as CONFLICTED | new | Consistent with the rest of the geology suite |

> **Backward compatibility.** New file; no prior anchors to preserve. Section anchors introduced here should be treated as stable.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (under `docs/domains/geology/`);
- a geology domain steward and a source steward review it;
- Grids A and B are ratified or replaced by a steward decision;
- it is linked from `docs/domains/geology/SOURCES.md` and `README.md`;
- it does not conflict with accepted ADRs (esp. ADR-0001 schema home);
- any conflict with descriptors or the dossier is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the authoring notes is wired into CI;
- future changes follow `ai-build-operating-contract.md §37` lifecycle.

[↑ Back to top](#top)

---

<a id="8-related-docs"></a>

## 8. Related docs

- `docs/domains/geology/SOURCES.md` — prose typology of families + the seven roles.
- `docs/domains/geology/SOURCE_REGISTRY.md` — admission / authority-control doctrine (consumes these grids).
- `docs/domains/geology/SOURCE_LEDGER.md` — per-entry append-only control surface.
- `docs/domains/geology/SCOPE.md` — owned object families; claim-class distinctness (§5).
- `docs/domains/geology/SENSITIVITY.md` — tier classification & decision lattice.
- `docs/domains/geology/README.md` — lane landing page.
- `ai-build-operating-contract.md` — operating law (`CONTRACT_VERSION = "3.0.0"`).
- `schemas/contracts/v1/source/source-descriptor.json` — `SourceDescriptor` schema home *(PROPOSED; Directory Rules §7.4 / ADR-0001)*.
- Atlas Ch. 10 §10.B (object families); §10.D (source families); §24.1.1 (role classes); §24.1.2 (anti-collapse failure modes); §24.1.3 (descriptor field surface).

---

*Last updated: 2026-06-04 · Status: `draft` · `CONTRACT_VERSION = "3.0.0"` · `[DOM-GEOL]`*

[↑ Back to top](#top)
