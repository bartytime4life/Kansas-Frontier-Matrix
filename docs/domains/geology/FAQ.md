<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-geology-faq
title: Geology and Natural Resources — FAQ
type: standard
subtype: domain-faq
version: v0.1
status: draft
owners: <geology-domain-steward> · <docs-steward>   # PLACEHOLDERS — assign in PR
created: 2026-06-04
updated: 2026-06-04
policy_label: public
authoring_session: Docs-only. No mounted repo, CI run, workflow, dashboard, runtime log, or release artifact inspected. Implementation maturity is bounded per the current-session evidence limit.
authority_posture: Reader-facing explainer. Subordinate to ai-build-operating-contract.md (CONTRACT_VERSION 3.0.0), directory-rules.md, the geology dossier ([DOM-GEOL] / [ENCY §7.8]), and accepted ADRs. Supersedes no source doctrine.
produced_by: GEOL-EXP-021 (Geology Expansion Backlog)
related:
  - docs/domains/geology/README.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/SOURCES.md
  - docs/domains/geology/EXPANSION_BACKLOG.md
  - docs/domains/geology/EVIDENCE_DRAWER_LANGUAGE.md   # produced by GEOL-EXP-013
  - docs/doctrine/ai-build-operating-contract.md       # CONTRACT_VERSION 3.0.0
  - docs/doctrine/directory-rules.md                   # v1.3
  - docs/doctrine/trust-membrane.md
tags: [kfm, domain, geology, faq, public-safe, resource-class, sensitivity, governance, doctrine-adjacent]
notes:
  - "Reader-facing FAQ. Answers are grounded in CONFIRMED geology doctrine; every repo-state path is PROPOSED until verified against a mounted repository."
  - "Doctrine-adjacent — pins CONTRACT_VERSION = 3.0.0 (ai-build-operating-contract.md)."
  - "Resource-class distinction (Occurrence / Deposit / Estimate / Permit / Production / Reserve) and the deny-by-default geometry posture are CONFIRMED doctrine ([DOM-GEOL §I])."
  - "The contracts/schemas path-form sub-path (segment vs flat) is CONFLICTED per CDR-GEOL-01; FAQ avoids asserting either form as fact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources — FAQ

> Plain-language answers to the two questions readers ask most about KFM geology layers: **“Why isn’t the exact location shown?”** and **“Why does this say ‘occurrence’ and not ‘deposit’ / ‘reserve’ / ‘production’?”** — grounded in KFM’s published doctrine.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![type: FAQ](https://img.shields.io/badge/type-FAQ-blue)
![domain: geology](https://img.shields.io/badge/domain-geology-8b5e3c)
![audience: public](https://img.shields.io/badge/audience-public-brightgreen)
![truth: cite–or–abstain](https://img.shields.io/badge/truth-cite--or--abstain-purple)
![posture: deny–by–default](https://img.shields.io/badge/posture-deny--by--default-yellow)
![contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![last updated: 2026–06–04](https://img.shields.io/badge/last%20updated-2026--06--04-informational)

|Field            |Value                                                                                                           |
|-----------------|----------------------------------------------------------------------------------------------------------------|
|**Document type**|Reader-facing FAQ (standard doc, doctrine-adjacent)                                                             |
|**Status**       |`draft`                                                                                                         |
|**Audience**     |General public and map readers; secondarily, new contributors.                                                  |
|**Owners**       |`<geology-domain-steward>` · `<docs-steward>` *(placeholders — assign in PR)*                                   |
|**Grounded in**  |`[DOM-GEOL]` / `[ENCY §7.8]` (geology dossier); Master Viewing Mode Atlas §20.1; Deny-by-Default Register §20.5.|
|**Contract pin** |`CONTRACT_VERSION = "3.0.0"` (`ai-build-operating-contract.md`).                                                |
|**Updated**      |2026-06-04                                                                                                      |


> [!NOTE]
> This FAQ explains **what KFM does and why**. Answers describe CONFIRMED doctrine. Wherever an answer would touch repository implementation (routes, schemas, file paths), it is marked **PROPOSED** or **NEEDS VERIFICATION** — KFM doctrine is settled, but this FAQ does not assert that any particular file or route already exists.

-----

## Contents

1. [Public-safe geometry](#1-public-safe-geometry)
1. [Resource-class confusion](#2-resource-class-confusion)
1. [Evidence, freshness, and “why no answer?”](#3-evidence-freshness-and-why-no-answer)
1. [What Geology covers (and what it doesn’t)](#4-what-geology-covers-and-what-it-doesnt)
1. [For contributors](#5-for-contributors)
1. [Glossary](#6-glossary)
1. [Related docs](#7-related-docs)

-----

## 1. Public-safe geometry

### Q1.1 — Why is the borehole / well / sample shown as a circle or a county shape instead of an exact point?

Because KFM publishes a **generalized** version of sensitive locations, not the exact one. Exact borehole, sample, sensitive-resource, well-log, and private-well locations **default to restricted or generalized public geometry** — that is CONFIRMED KFM doctrine, not a per-map choice (`[DOM-GEOL §I]`, `[ENCY §7.8]`).

When you see a generalized footprint, the public layer is showing a deliberately coarsened shape (for example, a township, a county, or a circle with a stated radius) so that the *pattern* is visible without exposing a precise, potentially harmful or private location.

> [!IMPORTANT]
> Generalization is done **before** publication and is recorded. KFM does not hide a precise point behind a map style and call it safe — sensitive geometry must be *transformed*, with a receipt, not merely styled out. (CONFIRMED doctrine: a popup or style filter is never a substitute for transformation.)

### Q1.2 — Can I get the exact coordinates if I ask, log in, or zoom in far enough?

No. Zooming, panning, or toggling layers does not reveal restricted geometry — the public layer only ever contains the generalized version. Exact coordinates for sensitive features sit behind the governed boundary and are available only to authorized, steward-reviewed roles, never on the public map (`[DOM-GEOL §I]`; Deny-by-Default Register, `[ENCY §20.5]`).

If a precise location is needed for legitimate work, that is a **steward-reviewed** request, not a public-map feature.

### Q1.3 — How do I know a shape has been generalized, and by how much?

The Evidence Drawer for the feature should tell you. A public occurrence display is meant to **distinguish exact internal geometry from generalized public geometry and show the redaction reason** (PROPOSED feature, KFM-P17-FEAT-0002). Where a generalization radius applies, it is meant to be stated (e.g., a `generalized_radius_m` value) so you know the shape is approximate by design.

> [!TIP]
> If you are unsure whether a shape is exact or generalized, open the **Evidence Drawer**. The drawer is the place where source, policy, freshness, and any geometry transform are explained for the thing you clicked.

### Q1.4 — Isn’t withholding the exact location just hiding data?

No — it is publishing the *most precise version that is safe and permitted*, and saying so. KFM’s posture is **deny-by-default for sensitive classes**: unclear rights, unresolved sensitivity, or a missing review state blocks public release of precise geometry (`[ENCY §20.5]`, `[DIRRULES]`). The generalized shape plus a stated reason is more honest than either a false-precision point or a blank map.

[⬆ back to top](#top)

-----

## 2. Resource-class confusion

### Q2.1 — Why does this say “occurrence” when I expected “deposit,” “reserve,” or “production”?

Because in KFM these are **different claims with different evidentiary weight, and they are kept distinct on purpose**. Occurrence, deposit, estimate, permit, production, and reserve claims **must remain distinct** — CONFIRMED geology doctrine (`[DOM-GEOL §I]`, `[ENCY §7.8]`). Collapsing them would let a weak claim (something was *reported* here) masquerade as a strong one (a *measured, economic, producing* resource).

Here is the plain-language difference between the terms you will see. *(The KFM object families `MineralOccurrence`, `ResourceDeposit`, and `ResourceEstimate` are CONFIRMED; “permit,” “production,” and “reserve” are named in the distinct-claims rule. The one-line meanings below are illustrative reader explanations, not formal definitions.)*

|Term you may see                    |What it roughly means to a reader                                       |What it does **not** mean                                         |
|------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------|
|**Occurrence** (`MineralOccurrence`)|A material was *reported observed* at or near a place.                  |That it is economic, measured, owned, or being mined.             |
|**Deposit** (`ResourceDeposit`)     |A *named* body of material, compiled administratively.                  |That a specific tonnage or value has been estimated or produced.  |
|**Estimate** (`ResourceEstimate`)   |A *modeled or compiled* quantity, with assumptions.                     |A direct measurement at any single point.                         |
|**Permit**                          |A *regulatory* authorization on record.                                 |That extraction was confirmed or that material exists in quantity.|
|**Production**                      |A *reported/aggregated* amount extracted over a period and area.        |A per-point, present-tense measurement at a single location.      |
|**Reserve**                         |An *economically/legally qualified* estimate under a reporting standard.|A raw occurrence or an unqualified guess.                         |


> [!CAUTION]
> **These are not synonyms.** Treating an occurrence as a deposit, an estimate as an observation, a permit as confirmed extraction, or an aggregate total as a per-place fact is a recognized KFM **collapse failure** — it is denied at publication and the AI assistant abstains rather than blur them (`[DOM-GEOL §I]`; Source-Role Anti-Collapse Register, `[ENCY §24.1]`).

### Q2.2 — A county shows a production total. Does that number apply to a specific parcel inside the county?

No. An aggregate figure (a county total, a yearly summary) describes the **whole reporting unit**, not any single place inside it. KFM explicitly forbids reading an aggregate as a per-place truth — an aggregate cell may not be joined to a single record as if it asserted that record (CONFIRMED doctrine; “aggregate cited as a per-place truth” is a denied collapse pattern, `[ENCY §24.1]`).

If you need per-place detail, look for an **observed** record at that place — and note its own evidence and precision posture from Section 1.

### Q2.3 — Why does the source matter so much? Data is data, isn’t it?

Because KFM tracks **how a value came to exist** as a first-class property, called its *source role*. A direct reading (observed), an agency authorization (regulatory), a model output (modeled), a summary total (aggregate), a registry compilation (administrative), an unverified candidate, and AI- or simulation-generated content (synthetic) are **not interchangeable**, and the system fails closed when they are conflated (CONFIRMED doctrine, `[ENCY §24.1]`).

So a “value” on a geology layer always travels with the question *what kind of claim is this?* — and the Evidence Drawer is where that answer lives.

[⬆ back to top](#top)

-----

## 3. Evidence, freshness, and “why no answer?”

### Q3.1 — What is the Evidence Drawer, and why should I open it?

The Evidence Drawer is KFM’s trust-inspection panel. Wherever you encounter a public claim — a map layer, a popup, or an AI answer — the drawer is meant to be available, and it resolves the **evidence, source role, policy, freshness, correction state, release, and rollback** behind what you are looking at (CONFIRMED doctrine: Evidence Drawer is mandatory on layers, popups, and AI answers, KFM-P1-FEAT-0065; Master Viewing Mode Atlas, `[ENCY §20.1]`).

A popup may give you a quick summary; the **drawer** is where the actual support is resolved. If the two ever seem to disagree, the drawer (and the evidence it resolves) is the authority, not the popup.

### Q3.2 — Why did the assistant say it can’t answer (or only partly answer)?

KFM surfaces have exactly four outcomes — **ANSWER, ABSTAIN, DENY, ERROR** — and “no answer” is a deliberate, honest result, not a malfunction:

- **ANSWER** — there is resolved, released evidence, and policy permits it.
- **ABSTAIN** — the evidence isn’t sufficient to support the claim, so KFM declines rather than guess.
- **DENY** — policy, rights, sensitivity, or release state blocks the request (for example, an exact sensitive location).
- **ERROR** — something went wrong in resolving the request.

This is the **cite-or-abstain** posture: KFM would rather give you a bounded, honest “not enough evidence” than a fluent-sounding answer it cannot back up (`[GAI]`, `[DOM-GEOL §L]`).

### Q3.3 — Does the AI assistant know geology facts on its own?

No — and that is by design. The assistant is **interpretive, never the source of truth**. It may summarize, compare, and explain *released* evidence and must **abstain** when no evidence resolves and **deny** where rights, sensitivity, or release state block the request (`[DOM-GEOL §L]`, `[GAI]`). It does not invent locations, generate a “synthetic” well log and present it as real, or upgrade a weak claim into a strong one.

### Q3.4 — Why does a layer show a “stale” or freshness badge?

Geologic maps, interpretations, and production records have a vintage. KFM shows freshness so you can judge how current a claim is, and a sufficiently out-of-date source may cause a surface to flag staleness or abstain rather than present old data as current (`[ENCY §7.8.M]`; freshness is part of what the Evidence Drawer surfaces, `[ENCY §20.1]`).

### Q3.5 — Something looks wrong. Can it be corrected?

Yes. Corrections are first-class in KFM: a published claim can be corrected, and the change is recorded (a correction notice) rather than silently overwritten; releases also carry a rollback target. The mechanics live in the geology policy and the project’s correction/rollback doctrine (`[DOM-GEOL §M]`). The right path for a specific correction is a steward-reviewed request — see [§5](#5-for-contributors).

[⬆ back to top](#top)

-----

## 4. What Geology covers (and what it doesn’t)

### Q4.1 — What does the Geology domain include?

The Geology and Natural Resources domain governs bedrock and surficial geology, stratigraphy, lithology, structures, boreholes, well logs, cores, geophysics, geochemistry, the mineral/resource distinctions in [§2](#2-resource-class-confusion), extraction and reclamation context, public-safe layers, and bounded AI (CONFIRMED scope, `[DOM-GEOL §A/§B]`).

### Q4.2 — Why doesn’t the geology layer answer my question about water levels, soil, hazard risk, or who owns the land?

Because those belong to **other** KFM domains, and Geology deliberately does not claim them (CONFIRMED non-ownership, `[DOM-GEOL §B/§F]`):

|You’re asking about…                        |The owning domain                     |What Geology *does* contribute                           |
|--------------------------------------------|--------------------------------------|---------------------------------------------------------|
|Groundwater levels / streamflow measurements|**Hydrology**                         |Hydrostratigraphic *context* only — not the measurements.|
|Soil properties                             |**Soil**                              |Parent-material / surficial *context* only.              |
|Hazard / landslide / subsidence *risk*      |**Hazards**                           |Fault / structural *context* only — not the risk verdict.|
|Who owns, leases, or holds title to land    |**People / Land** (or **Settlements**)|Nothing — a parcel relation cannot prove a deposit.      |

This separation is what keeps each claim honest: Geology will give you geologic *context* across a boundary, but it will not pretend to own another domain’s truth.

[⬆ back to top](#top)

-----

## 5. For contributors

> [!NOTE]
> This section is for people adding to or operating the geology lane, not general readers.

### Q5.1 — Where do I report a data error or request a precise location for legitimate work?

Through a **steward-reviewed** path, not by editing a public layer. Sensitive-class requests (exact locations, rights questions, resource-class disputes) require a recorded review and a stored policy decision; tooling acceptance alone is never sufficient (`[DOM-GEOL §I/§L]`). The owners listed at the top of this file are the placeholder contacts; assign real owners in the PR that lands this doc.

### Q5.2 — Where are the rules these answers come from?

Everything here is drawn from published KFM doctrine — chiefly the geology dossier (`[DOM-GEOL]` / `[ENCY §7.8]`), the Master Viewing Mode Atlas and Deny-by-Default Register (`[ENCY §20.1]`, `[ENCY §20.5]`), and the Source-Role Anti-Collapse Register (`[ENCY §24.1]`). See [§7](#7-related-docs).

### Q5.3 — Why are some paths in the related docs marked PROPOSED or CONFLICTED?

Because this FAQ does not assert repository state it hasn’t verified. In particular, the home for geology contracts and schemas has an unresolved, ADR-class question — whether it uses a `domains/geology/` segment form or a flat `geology/` form (tracked as **CDR-GEOL-01** in the geology backlog). Until an ADR resolves it, related paths are labeled rather than asserted.

[⬆ back to top](#top)

-----

## 6. Glossary

<details>
<summary><strong>Reader-friendly glossary of terms used above</strong></summary>

|Term                                                               |One-line reader meaning                                                                                            |Status                                           |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
|**Evidence Drawer**                                                |The trust panel that resolves source, policy, freshness, and corrections for what you clicked.                     |CONFIRMED doctrine                               |
|**EvidenceBundle**                                                 |The bundled support behind a claim; it outranks anything merely drawn on the map.                                  |CONFIRMED                                        |
|**Source role**                                                    |What *kind* of claim a value is: observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic.|CONFIRMED                                        |
|**Generalized geometry**                                           |A deliberately coarsened shape published in place of a sensitive exact location.                                   |CONFIRMED posture                                |
|**Transform / redaction receipt**                                  |The record stating that geometry was generalized, by how much, and why.                                            |CONFIRMED object family / PROPOSED implementation|
|**ANSWER / ABSTAIN / DENY / ERROR**                                |The four honest outcomes any KFM surface can return.                                                               |CONFIRMED                                        |
|**Cite-or-abstain**                                                |KFM cites evidence or declines; it does not guess.                                                                 |CONFIRMED doctrine                               |
|**Deny-by-default**                                                |Sensitive material is withheld unless explicitly cleared.                                                          |CONFIRMED doctrine                               |
|**Occurrence / Deposit / Estimate / Permit / Production / Reserve**|Distinct resource claims that must never be treated as synonyms.                                                   |CONFIRMED distinction                            |

</details>

[⬆ back to top](#top)

-----

## 7. Related docs

> [!NOTE]
> Paths below are **PROPOSED** until verified against a mounted repository. The geology contract/schema home form is **CONFLICTED** (CDR-GEOL-01) and is intentionally not asserted here.

- `docs/domains/geology/README.md` — Geology lane landing.
- `docs/domains/geology/POLICY.md` — Geology sensitivity, rights, and publication policy.
- `docs/domains/geology/SOURCES.md` — Source families and rights/sensitivity matrix.
- `docs/domains/geology/EVIDENCE_DRAWER_LANGUAGE.md` — Drawer wording patterns *(GEOL-EXP-013)*.
- `docs/domains/geology/EXPANSION_BACKLOG.md` — Backlog (this FAQ is GEOL-EXP-021).
- `docs/doctrine/ai-build-operating-contract.md` — Operating contract (`CONTRACT_VERSION = "3.0.0"`).
- `docs/doctrine/directory-rules.md` — Canonical placement rules (v1.3).
- `docs/doctrine/trust-membrane.md` — Why public clients read only released, governed artifacts.

-----

*Last updated: 2026-06-04 · Doc version: v0.1 · Status: draft · Contract: `CONTRACT_VERSION = "3.0.0"`*

[⬆ back to top](#top)