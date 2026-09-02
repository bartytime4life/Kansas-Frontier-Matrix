<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-ubiquitous-language
title: Geology and Natural Resources — Ubiquitous Language
type: standard
version: v1
status: draft
owners: <geology-domain-steward> · <docs-steward>   # placeholder — confirm in CODEOWNERS
created: 2026-06-04
updated: 2026-06-04
policy_label: public
related:
  - docs/domains/geology/README.md
  - docs/domains/geology/SCOPE.md
  - docs/domains/geology/SOURCES.md
  - docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - docs/domains/geology/SUBLANE-BEDROCK.md
  - ai-build-operating-contract.md   # CONTRACT_VERSION = "3.0.0"
  - docs/doctrine/directory-rules.md
tags: [kfm, geology, ubiquitous-language, glossary, bounded-context, governance]
notes:
  - Bounded-context ubiquitous-language glossary for the geology lane. Authoritative term list is DOM-GEOL §10.C; owns-list short forms are §10.B.
  - Doctrine-adjacent; pins CONTRACT_VERSION = "3.0.0".
  - The §10.B (owns-list) short forms vs §10.C/§10.E (Reference / variant) forms is an unresolved CONFLICTED naming drift; this doc records both and routes resolution to ADR, never picking one silently.
  - Every term's meaning is constrained by source role, evidence, time, and release state (the §10.C framing). All repo paths PROPOSED.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources — Ubiquitous Language

> The shared vocabulary of the geology bounded context (`[DOM-GEOL]`): every domain term, what it means inside this lane, the casing it is recorded under, and the "false friends" that collide with neighbor lanes. In DDD terms, this is the lane's ubiquitous language — the words must mean one thing here, consistently.

![status](https://img.shields.io/badge/status-draft-orange)
![domain](https://img.shields.io/badge/domain-geology%20%5BDOM--GEOL%5D-blue)
![type](https://img.shields.io/badge/type-ubiquitous--language-informational)
![naming](https://img.shields.io/badge/naming%20drift-CONFLICTED-red)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-lightgrey)

| Field | Value |
|---|---|
| **Status** | `draft` |
| **Owners** | `<geology-domain-steward>` · `<docs-steward>` *(placeholders — confirm in CODEOWNERS)* |
| **Authoritative term list** | `DOM-GEOL §10.C` (ubiquitous language); `§10.B` (owns-list short forms) |
| **Lane** | Geology / Natural Resources — `[DOM-GEOL]`, Atlas Ch. 10 |
| **Updated** | 2026-06-04 |

> [!IMPORTANT]
> **Every term in this lane is constrained, not free.** Per the §10.C framing, each term *"is used inside this domain with meaning constrained by source role, evidence, time, and release state."* A word in this glossary never names a bare fact — it names a sourced, dated, role-typed, release-stated, evidence-bound claim. Where this glossary and the dossier disagree, the dossier governs and the drift is logged in `docs/registers/DRIFT_REGISTER.md`.

---

## Contents

- [1. How to read this glossary](#1-how-to-read-this-glossary)
- [2. Core object terms](#2-core-object-terms)
- [3. Naming-drift reconciliation (CONFLICTED)](#3-naming-drift-reconciliation-conflicted)
- [4. Claim-class terms (must stay distinct)](#4-claim-class-terms-must-stay-distinct)
- [5. Cross-lane "false friends"](#5-cross-lane-false-friends)
- [6. Governance terms used in this lane](#6-governance-terms-used-in-this-lane)
- [7. Open questions & verification](#7-open-questions--verification)
- [8. Related docs](#8-related-docs)

---

<a id="1-how-to-read-this-glossary"></a>

## 1. How to read this glossary

This is the term dictionary for the geology bounded context. It complements, and does not replace, the other lane docs:

| Doc | Answers |
|---|---|
| `SCOPE.md` | Which objects the lane owns / does not own (boundary). |
| `UBIQUITOUS_LANGUAGE.md` *(this doc)* | What each term *means* here, and how it is spelled. |
| `SOURCE_ROLE_MATRIX.md` | Which source role may carry which term as a claim. |
| `SUBLANE-*.md` | How the terms group into sublanes. |

Every core term below carries the §10.C constraint clause implicitly: *meaning constrained by source role, evidence, time, and release state*. The definitions add the lane-specific gloss on top of that clause.

> [!NOTE]
> **Terms are CONFIRMED; field realizations are PROPOSED.** The §10.C records each term as "CONFIRMED term / PROPOSED field realization" — the *word* and its meaning are doctrine, but the schema field that carries it is not asserted until the mounted `contracts/`/`schemas/` are verified.

[↑ Back to top](#top)

---

<a id="2-core-object-terms"></a>

## 2. Core object terms

The ubiquitous-language terms of the geology lane. "Recorded as" gives the §10.C/§10.E casing where it differs from the §10.B owns-list short form (see [§3](#3-naming-drift-reconciliation-conflicted)).

| Term | Meaning inside this lane | Recorded as (§10.C/§10.E) |
|---|---|---|
| **Geologic Unit** | A mapped lithostratigraphic/chronostratigraphic body of rock. | `Geologic Unit` |
| **Lithology** | The material character of a unit or sample. | `Lithology` |
| **Stratigraphic Interval** | A named interval with bounded contacts and an age model. | `Stratigraphic Interval` |
| **StratigraphicCorrelation** | The interpretive correlation of intervals across locations. | `StratigraphicCorrelation` |
| **Geologic Age** | A chronostratigraphic/geochronologic time-scope assertion with uncertainty. | `Geologic Age` |
| **SurficialUnit** | A mapped body of unconsolidated surface cover (alluvium, loess, glacial). | `SurficialUnit` |
| **Fault Structure** | A structural line/surface with sense-of-slip and confidence. | `StructureFeature` |
| **GeologyBoundaryVersion** | The versioned boundary geometry of a unit — the provenance of the line itself. | `GeologyBoundaryVersion` |
| **CrossSection** | A 2D interpretive section through the rock record, interpretation-versioned. | `CrossSection` |
| **Borehole** | A drilled location with subsurface observations (exact location restricted). | `BoreholeReference` |
| **Well Log** | A subsurface log series tied to a borehole (rights-controlled). | `Well LogReference` |
| **Core Sample** | A physical core/sample reference with location and custody. | *(short form; §10.E variant NEEDS VERIFICATION)* |
| **Geophysical Observation** | A field or remote-sensed geophysical measurement. | *(short form; §10.E variant NEEDS VERIFICATION)* |
| **Geochemistry Sample** | A geochemical sample reference with analyte set and uncertainty. | `Geochemistry SampleReference` |
| **Mineral Occurrence** | A documented presence — not a deposit, not an estimate. | `Mineral Occurrence` |
| **Resource Deposit** | A delineated, characterized body — not an estimate. | *(see §3 — drifts with `ResourceEstimate`)* |
| **ResourceEstimate** | A quantity under a stated reporting framework. | `ResourceEstimate` |
| **Extraction Site** | A site of past/present extraction (physical claim, distinct from permit/operator). | `Extraction Site` |
| **Reclamation Record** | Reclamation status, plan, and observations. | *(short form; §10.E variant NEEDS VERIFICATION)* |
| **Hydrostratigraphic Unit** | The geology↔hydrology bridge object (context, not measurement). | `Hydrostratigraphic Unit` |

[↑ Back to top](#top)

---

<a id="3-naming-drift-reconciliation-conflicted"></a>

## 3. Naming-drift reconciliation (CONFLICTED)

> [!CAUTION]
> **This is the central unresolved item for the geology lane vocabulary.** The Atlas records the *same objects* under two casings: the §10.B owns-list short forms and the §10.C/§10.E `…Reference` / variant forms. This glossary records **both** and resolves **neither** — resolution is an ADR/schema-PR decision, not a documentation choice.

| §10.B owns-list (short) | §10.C / §10.E (variant) | Status |
|---|---|---|
| `Borehole` | `BoreholeReference` | CONFLICTED |
| `Well Log` | `Well LogReference` | CONFLICTED |
| `Geochemistry Sample` | `Geochemistry SampleReference` | CONFLICTED |
| `Fault Structure` | `StructureFeature` | CONFLICTED |
| *(implied surficial subset of `Geologic Unit`)* | `SurficialUnit` | CONFLICTED — distinct family vs sub-type unresolved |
| *(boundary provenance — not in §10.B)* | `GeologyBoundaryVersion` | §10.C-only term |
| *(correlation — not in §10.B)* | `StratigraphicCorrelation` | §10.C-only term |
| `Resource Deposit` | `ResourceEstimate` | CONFLICTED — different *concept* under a drifting name |

> [!WARNING]
> The `Resource Deposit` ↔ `ResourceEstimate` row is the most dangerous drift: these are **not** two spellings of one object — a deposit is a delineated body and an estimate is a quantity. If a schema collapses them under one name, the claim-class distinctness rule (`SCOPE.md §5`) is broken at the type level. Resolve by ADR before any schema PR pins a name.

Resolution path: a single ADR (or coordinated schema PR) fixes one canonical name per object family, with the rejected forms recorded as aliases for a deprecation window. Until then, downstream docs MUST treat either casing as referring to the same object and MUST NOT assert one as authoritative.

[↑ Back to top](#top)

---

<a id="4-claim-class-terms-must-stay-distinct"></a>

## 4. Claim-class terms (must stay distinct)

**CONFIRMED doctrine (DOM-GEOL §10.I).** These six terms name *different kinds of claim* and must never be used interchangeably — in prose, in schemas, in the graph, or in any AI/UI summary.

| Term | Is | Is NOT |
|---|---|---|
| **Occurrence** | A documented presence at a location | A delineated body; a quantity |
| **Deposit** | A delineated, characterized body | A quantified estimate |
| **Estimate** | A quantity under a stated reporting framework | An economically recoverable reserve |
| **Reserve** | The economically recoverable subset of an estimate | Reported production |
| **Permit** | A regulatory authorization | Evidence that production occurred |
| **Production** | Reported extraction over an interval | Proof of an estimate or reserve |

> [!IMPORTANT]
> These are *vocabulary* rules with *enforcement* teeth: each forbidden substitution maps to an anti-collapse DENY in `SOURCE_ROLE_MATRIX.md` Grid C. Saying "occurrence" when you mean "deposit" is not loose phrasing — it is a claim-class collapse.

[↑ Back to top](#top)

---

<a id="5-cross-lane-false-friends"></a>

## 5. Cross-lane "false friends"

Terms that look shared with a neighbor lane but mean something different — the classic ubiquitous-language hazard at a bounded-context boundary.

| Term | In geology it means | In the other lane it means | Rule |
|---|---|---|---|
| **Unit** | A `Geologic Unit` (rock body) | A `SoilMapUnit` (Soil); a `HUCUnit` (Hydrology) | Qualify always — "geologic unit," never bare "unit" across a boundary. |
| **Well** | A `Borehole` / oil-and-gas well (geology) | A `Groundwater Well` (Hydrology) | A geology well is a subsurface rock record; a hydrology well is a water-level/measurement site. Distinct objects. |
| **Structure** | A `Fault Structure` / `StructureFeature` (rock deformation) | Built `Infrastructure` (Settlements) | Geology structure is geologic, never engineered structure. |
| **Hydrostratigraphic Unit** | Geology's framing of an aquifer/aquitard body | Hydrology owns the *measurements* in it | Geology supplies the unit as context; it never restates a hydrology measurement (`SCOPE.md §3`). |
| **Sample** | A `Core Sample` / `Geochemistry Sample` (geology) | A monitoring sample (Air/Water) | Geology samples are physical rock/geochemical; not an air/water reading. |

> [!NOTE]
> The bounded-context discipline (DDD) is precise here: a model term "only has meaning in context." This table is the geology lane's defense against silently importing a neighbor's meaning.

[↑ Back to top](#top)

---

<a id="6-governance-terms-used-in-this-lane"></a>

## 6. Governance terms used in this lane

Cross-cutting KFM terms as they apply to geology. These are defined canonically elsewhere; this section fixes their geology gloss so the lane uses them consistently.

| Term | Geology gloss |
|---|---|
| `SourceDescriptor` | The admission record fixing a geology source's role, rights, and sensitivity (`SOURCES.md`). |
| `EvidenceBundle` / `EvidenceRef` | The support every public geology claim resolves through. |
| `source role` | One of seven classes (observed/regulatory/modeled/aggregate/administrative/candidate/synthetic) carried by a geology source. |
| `RealityBoundaryNote` | Required on reconstruction-heavy cross-sections / synthetic surfaces so drawn ≠ observed. |
| `RedactionReceipt` / `AggregationReceipt` | The transform receipts that move sensitive geology geometry toward public release (`SENSITIVITY.md`). |
| `PromotionDecision` / `ReleaseManifest` | The governed transition and binding that publishes a geology layer (`RELEASE_INDEX.md`). |
| `truth labels` | CONFIRMED / PROPOSED / INFERRED / NEEDS VERIFICATION / UNKNOWN, applied to every geology claim in docs. |

[↑ Back to top](#top)

---

<a id="7-open-questions--verification"></a>

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-GEOL-UL-01 | Resolve the §10.B short vs §10.C/§10.E variant naming drift — one canonical name per family. | `<geology-domain-steward>` | ADR or coordinated schema PR; alias window; drift entry |
| OQ-GEOL-UL-02 | Is `SurficialUnit` a distinct owned family or a sub-type of `Geologic Unit`? | `<geology-domain-steward>` | Schema review (mirrors SCOPE OQ-GEOL-SCOPE-03 / BED OQ-GEOL-BED-01) |
| OQ-GEOL-UL-03 | Confirm the §10.E variant casing for `Core Sample`, `Geophysical Observation`, `Reclamation Record` (NEEDS VERIFICATION rows in §2). | `<geology-domain-steward>` | Dossier / schema check |
| OQ-GEOL-UL-04 | Confirm `Resource Deposit` vs `ResourceEstimate` are kept as distinct types (not merged). | `<geology-domain-steward>` + `<schema-steward>` | Schema review; claim-class anti-collapse tests |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before this document promotes from `draft` to `published`:

1. The canonical name set resolving the §3 drift (OQ-GEOL-UL-01, -03).
2. The `SurficialUnit` family-vs-subtype decision (OQ-GEOL-UL-02).
3. That `Resource Deposit` and `ResourceEstimate` are distinct schema types (OQ-GEOL-UL-04).

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial geology ubiquitous-language glossary authored | new | Fix the bounded-context vocabulary; provide the term dictionary the rest of the suite assumes |
| Naming-drift reconciliation table added (CONFLICTED) | new | Record both §10.B and §10.C/§10.E casings without resolving; route to ADR |
| Cross-lane "false friends" table added | clarification | Defend the boundary against importing neighbor-lane meanings |

> **Backward compatibility.** New file; no prior anchors to preserve. Section anchors introduced here should be treated as stable.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (under `docs/domains/geology/`);
- a geology domain steward reviews it;
- the term list matches `DOM-GEOL §10.C` (or the dossier is updated in lockstep);
- it is linked from `docs/domains/geology/README.md` and `SCOPE.md`;
- the §3 naming drift is either resolved by ADR or explicitly carried as CONFLICTED;
- any conflict with the dossier is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the authoring notes is wired into CI;
- future changes follow `ai-build-operating-contract.md §37` lifecycle.

[↑ Back to top](#top)

---

<a id="8-related-docs"></a>

## 8. Related docs

- `docs/domains/geology/SCOPE.md` — owns / does-not-own boundary; claim-class distinctness.
- `docs/domains/geology/SOURCES.md` — source families and the seven source roles.
- `docs/domains/geology/SOURCE_ROLE_MATRIX.md` — anti-collapse grids (Grid C enforces §4).
- `docs/domains/geology/SUBLANE-BEDROCK.md` — bedrock sublane (uses these terms).
- `docs/domains/geology/SENSITIVITY.md` — tier classification & decision lattice.
- `docs/domains/geology/README.md` — lane landing page.
- `ai-build-operating-contract.md` — operating law (`CONTRACT_VERSION = "3.0.0"`).
- Atlas Ch. 10 §10.A (identity); §10.B (owns-list short forms); §10.C (ubiquitous language); §10.E (object identity / variant forms); §10.I (claim-class distinctness).
- `DomainDriven_Design_Reference.pdf` — Ubiquitous Language; Bounded Context.

---

*Last updated: 2026-06-04 · Status: `draft` · `CONTRACT_VERSION = "3.0.0"` · `[DOM-GEOL]`*

[↑ Back to top](#top)
