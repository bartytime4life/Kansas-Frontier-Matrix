<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-evidence-drawer-language
title: Geology Domain — Evidence Drawer Language
type: standard
version: v1
status: draft
owners: <geology-domain-steward> (PLACEHOLDER), <ai-surface-steward> (PLACEHOLDER), <ux-copy-steward> (PLACEHOLDER)
created: 2026-06-03
updated: 2026-06-03
policy_label: public
contract_version: 3.0.0
related: [
  "docs/doctrine/directory-rules.md",
  "ai-build-operating-contract.md",
  "docs/domains/geology/README.md",
  "docs/domains/geology/EVIDENCE_DRAWER.md",
  "docs/domains/geology/CROSS_LANE_NOTES.md",
  "docs/domains/geology/SENSITIVITY.md",
  "docs/architecture/governed-ai/README.md",
  "docs/standards/ux-copy.md",
  "docs/registers/VERIFICATION_BACKLOG.md",
  "docs/registers/DRIFT_REGISTER.md"
]
tags: [kfm, domain, geology, evidence-drawer, ux-copy, language, trust, sensitivity]
notes: [
  "CONTRACT_VERSION pinned to 3.0.0 per ai-build-operating-contract.md.",
  "This doc governs the human-readable STRINGS the Evidence Drawer shows for geology features. The drawer payload CONTRACT lives in EVIDENCE_DRAWER.md; the Evidence Drawer is a CONFIRMED cross-cutting surface, not a geology component.",
  "Language must explain trust, source role, sensitivity, and redaction WITHOUT leaking exact well/borehole/deposit locations (Atlas §8.G / §24.5).",
  "All non-directory-rules.md repo paths are PROPOSED / NEEDS VERIFICATION until checked against a mounted KFM repo.",
  "Geology-specific anti-collapse: a lease/permit/operator relation must never be phrased as proof of a deposit (Atlas §10.F People/Land edge)."
]
[/KFM_META_BLOCK_V2] -->

# 🪨 Geology Domain — Evidence Drawer Language

> The controlled vocabulary the Evidence Drawer speaks when a user clicks a geology feature — trust, source role, time, sensitivity, and redaction said in words that inform without leaking.

![Status](https://img.shields.io/badge/status-draft-orange)
![Type](https://img.shields.io/badge/type-controlled%20vocabulary-blue)
![Lane](https://img.shields.io/badge/lane-geology-8d6e63)
![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![Rule](https://img.shields.io/badge/resolve%20EvidenceBundle-before%20words-8a2be2)
![Sensitivity](https://img.shields.io/badge/well%2Fdeposit%20location-explained%2C%20not%20leaked-b22222)
![Surface](https://img.shields.io/badge/drawer-shared%20cross--cutting-8d6e63)

| | |
|---|---|
| **Status** | draft |
| **Owners** | `<geology-domain-steward>`, `<ai-surface-steward>`, `<ux-copy-steward>` (PLACEHOLDER) |
| **Last updated** | 2026-06-03 |
| **Contract** | `CONTRACT_VERSION = "3.0.0"` (`ai-build-operating-contract.md`) |
| **Authority** | KFM doctrine; `directory-rules.md` (v1.3); Atlas v1.1 §10 (Geology), §8.G / §24.5 (sensitivity), §24.1 (source-role anti-collapse); Master MapLibre Components v2.1 §N (Evidence Drawer) |
| **Governs** | the *words*, not the *payload* — the payload contract is `EVIDENCE_DRAWER.md` |

> [!IMPORTANT]
> **Words follow evidence, not the other way around.** The Evidence Drawer resolves the `EvidenceBundle` **before** it renders any string; there is **no rendered-feature-only sentence**. Every phrase in this catalog is shown only when its underlying field resolved. Where rights, sensitivity, source authority, stale state, or release proof is missing, the drawer speaks the `ABSTAIN` / `DENY` language in §7 — never a confident geology claim. Each implementation-shaped item below is labeled `CONFIRMED`, `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`, or `CONFLICTED`.

---

## Contents

1. [Purpose & scope](#1-purpose--scope)
2. [Why geology needs its own drawer language](#2-why-geology-needs-its-own-drawer-language)
3. [Trust-state vocabulary](#3-trust-state-vocabulary)
4. [Source-role phrasing (anti-collapse)](#4-source-role-phrasing-anti-collapse)
5. [Temporal phrasing](#5-temporal-phrasing)
6. [Sensitivity & redaction language](#6-sensitivity--redaction-language)
7. [Finite-outcome microcopy](#7-finite-outcome-microcopy)
8. [Conflict & correction language](#8-conflict--correction-language)
9. [Per-object label set](#9-per-object-label-set)
10. [Forbidden phrasings](#10-forbidden-phrasings)
11. [File-home & placement notes](#11-file-home--placement-notes)
12. [Open questions register](#12-open-questions-register)
13. [Open verification backlog](#13-open-verification-backlog)
14. [Changelog](#14-changelog)
15. [Definition of done](#15-definition-of-done)
16. [Related docs](#16-related-docs)

---

## 1. Purpose & scope

This document is the **controlled vocabulary** for the Geology lane's Evidence Drawer surface. It defines the exact human-readable strings — labels, chips, sentences, microcopy — the drawer shows when a user clicks a geologic feature, and the rules that keep those words truthful, evidence-bound, and sensitivity-safe.

**It governs the words.** The drawer *payload contract* (fields, resolution flow, panels) is `docs/domains/geology/EVIDENCE_DRAWER.md` (PROPOSED, mirrors the flora pattern). The Evidence Drawer itself is a **CONFIRMED cross-cutting surface** shared across all lanes — Geology supplies strings, not a component. [ATLAS §10.G] [MAP-MASTER §N]

**In scope:** trust-state labels; source-role phrasing; temporal phrasing; sensitivity/redaction wording; finite-outcome microcopy (`ANSWER`/`ABSTAIN`/`DENY`/`ERROR`); conflict and correction language; per-object label sets; forbidden phrasings.

**Out of scope (see neighbors):**

- Drawer payload fields and resolution flow — `EVIDENCE_DRAWER.md`.
- Object *meaning* — `contracts/domains/geology/` (PROPOSED).
- Field *schema* — `schemas/contracts/v1/domains/geology/` (PROPOSED).
- Sensitivity *policy* (what is denied) — `policy/domains/geology/` + `SENSITIVITY.md` (PROPOSED).
- Cross-lane *edge ownership* — `CROSS_LANE_NOTES.md` (PROPOSED).

[Back to top ↑](#contents)

---

## 2. Why geology needs its own drawer language

Geology carries three phrasing hazards that generic drawer copy handles poorly:

1. **Authority-vs-inference collapse.** A KGS geologic map (authority) and a modeled hydrostratigraphic surface (model) must not be described with the same confidence verbs. Atlas §24.1 forbids source-role collapse; the *words* are where that collapse is most likely to sneak in.
2. **Location-sensitive features.** Exact well/borehole coordinates, oil-and-gas operator detail, and precise mineral-deposit geometry are sensitive. The drawer must **explain a redaction without leaking the withheld location** (Atlas §8.G).
3. **The deposit-proof trap.** Atlas §10.F is explicit: a lease/parcel/operator relation **cannot prove deposits**. The drawer must never phrase an administrative or regulatory record as evidence of resource presence.

> [!CAUTION]
> **Sensitive-domain handling (operating contract §23.2).** Exact borehole/well locations, restricted operator-linked records, and precise deposit geometry are sensitive geology content. The most restrictive applicable disposition applies: **DENY public exact exposure · GENERALIZE before publication · REDACT · QUARANTINE uncertain source material · REQUIRE steward review · REQUIRE transform receipt (RedactionReceipt) · ABSTAIN when support is inadequate.** No drawer string may contain an exact coordinate, an exact well/API number, or a restricted-source-derived field.

[Back to top ↑](#contents)

---

## 3. Trust-state vocabulary

**CONFIRMED doctrine** (Master MapLibre ML-061-140): the drawer exposes finite trust-visible states with **distinct treatment**. Geology uses the shared four-state set; the strings below are PROPOSED.

| Trust state | Chip label (PROPOSED) | One-line drawer phrasing (PROPOSED) |
|---|---|---|
| `verified` | **Verified** | "Backed by a resolved evidence bundle and a current source." |
| `stale` (`SOURCE_STALE`) | **Source stale** | "Shown with caution — the source is past its freshness window; the geologic boundary may have been revised." |
| `unknown` | **Unverified** | "Verification state not established; no proof is claimed for this feature." |
| `failed` | **Verification failed** | "A verification or integrity check failed; the claim is withheld pending review." |

> [!IMPORTANT]
> **A badge is not evidence.** The trust chip exposes state; it never replaces the bundle. A badge click opens proof details (receipts, attestations); it is not itself the citation surface. [MAP-MASTER ML-061-138, ML-061-139]

[Back to top ↑](#contents)

---

## 4. Source-role phrasing (anti-collapse)

**CONFIRMED doctrine** (Atlas §24.1): source roles must not collapse. The drawer's verbs encode the role so a user can tell an observed log from a modeled surface at a glance. Geology source roles map onto the canonical `authority / observation / context / model` quad (and the §24.1 classes `Observed / Regulatory / Modeled / Aggregate / Administrative`).

| Role | Geology example | Drawer verb (PROPOSED) | Never say |
|---|---|---|---|
| **authority** | KGS geologic map; USGS NGMDB/GeMS unit | "mapped as" / "classified by KGS as" | "we measured" |
| **observation** | borehole log, core sample, geochemistry sample | "logged at" / "sampled as" | "modeled" |
| **regulatory** | KCC oil-and-gas regulatory record | "recorded by the regulator as" | "proves a deposit" (see §10) |
| **model** | modeled hydrostratigraphic / resource surface | "estimated by a model as" / "interpolated as" | "observed" / "measured" |
| **context** | adjacent-lane reference (Soil parent material, Hydrology aquifer) | "provided as context by [lane]" | "owned here" |

> [!WARNING]
> A `ResourceEstimate` or `DistributionSurface` is **modeled** unless its bundle says otherwise. The drawer must phrase it with model verbs and show the model's source-role chip; describing an estimate as an observed quantity is a source-role collapse. [ATLAS §24.1]

[Back to top ↑](#contents)

---

## 5. Temporal phrasing

**CONFIRMED doctrine** (Atlas §10.E): source, observed, valid, retrieval, release, and correction times stay distinct where material. Geologic features add a wrinkle — *geologic age* (deep time) is distinct from *record time* (when the source asserted/observed the unit). The drawer must not blur them.

| Time facet | Drawer phrasing (PROPOSED) |
|---|---|
| Geologic age (deep time) | "Geologic age: [unit age] (per [authority])" — a property of the unit, not a KFM timestamp |
| observed | "Logged/sampled: [date]" |
| valid | "Mapped boundary valid as of: [date/version]" |
| retrieval | (not shown as a feature time; lives in the run receipt) |
| release | "Published in release: [release_id]" |
| correction | "Corrected: [date] — see what changed" |

> [!NOTE]
> `GeologyBoundaryVersion` is a first-class object; when a boundary has been revised, the drawer says "boundary revised in [version]" and links the prior version rather than silently showing the latest. Corrections never overwrite — they supersede.

[Back to top ↑](#contents)

---

## 6. Sensitivity & redaction language

**CONFIRMED doctrine** (Atlas §8.G): the sensitivity-redacted view **explains the redaction without leaking the withheld location**. For geology this is the load-bearing section.

**Redaction explanation strings (PROPOSED) — say the reason, never the location:**

| Situation | Drawer phrasing (PROPOSED) |
|---|---|
| Exact well/borehole withheld | "Exact location withheld. Shown generalized to [grid/county]. Reason: well-location sensitivity. See transform record." |
| Operator-linked record restricted | "Operator-linked detail restricted by source terms. A public-safe summary is shown." |
| Precise deposit geometry withheld | "Precise deposit geometry withheld. A generalized occurrence footprint is shown. See transform record." |
| Steward-only exact access | "An exact record exists and is available to authorized reviewers; the public view is generalized." |

Each redaction string is paired with a link to the `RedactionReceipt` (transform metadata only — input class, output class, reason, reviewer, residual risk). **The receipt payload never carries the withheld value.**

> [!CAUTION]
> The drawer must never name *why a specific site* is sensitive in a way that re-identifies it (e.g., "withheld because this is the only platinum occurrence in [named section]"). Reason strings are **class-level** ("well-location sensitivity", "operator terms", "deposit-location sensitivity"), never feature-level. Combinatorial sensitivity applies: a generalized borehole joined to operator or production data must not be re-narrated into an exact site. [ATLAS §24.5] [§24.1]

[Back to top ↑](#contents)

---

## 7. Finite-outcome microcopy

**CONFIRMED doctrine** (governed-AI; MAP-MASTER §N): the drawer renders the four finite outcomes carried in a `RuntimeResponseEnvelope` as typed states, never as blanks or fabrications.

| Outcome | Drawer microcopy (PROPOSED) |
|---|---|
| `ANSWER` | (renders the resolved payload + panels + citations) |
| `ANSWER` (redacted) | "Shown generalized for sensitivity. [redaction reason] — see transform record." |
| `ABSTAIN` | "Not enough evidence to answer for this feature. No claim is shown." |
| `DENY` | "This information isn't available on the public map. [class reason, e.g., 'source rights unresolved' / 'location sensitivity']." |
| `ERROR` | "Couldn't resolve the evidence for this feature. Nothing is shown rather than something unverified." |

> [!NOTE]
> A `DENY` string states a **reason class**, never the sensitive detail that motivated the denial. "Location sensitivity" is allowed; the coordinate that makes it sensitive is not.

[Back to top ↑](#contents)

---

## 8. Conflict & correction language

**CONFIRMED doctrine** (MAP-MASTER ML-060-027): when sources disagree, **both observations are retained**; the drawer exposes the conflict rather than silently picking a winner.

Geology conflict phrasings (PROPOSED):

- Boundary disagreement between two authorities: "Two sources map this boundary differently. KFM shows [canonical] as primary and retains [other]; basis for the choice: [trust tier / recency]."
- Unit-name disagreement: "Named [A] by [authority 1] and [B] by [authority 2]. Both are retained; see the conflict panel."
- Correction notice: "This feature was corrected on [date]. [What changed, plainly.] The prior version is preserved."

> [!NOTE]
> Correction language is downgrade-friendly: per Atlas §24.6, a tier downgrade (toward less public) needs only a `CorrectionNotice` (+ `ReviewRecord`), and the drawer says so plainly — "restricted on review" — without re-exposing the corrected-away detail.

[Back to top ↑](#contents)

---

## 9. Per-object label set

PROPOSED display labels and the one phrasing rule that matters most for each Geology object family (object families CONFIRMED from Atlas §10.B/§10.E and the Ch. 24 Geology row).

| Object family | Drawer label (PROPOSED) | Phrasing rule |
|---|---|---|
| Geologic Unit | "Geologic unit" | authority verb ("mapped as"); show GeologyBoundaryVersion |
| SurficialUnit | "Surficial unit" | authority verb; distinguish from bedrock |
| Lithology | "Lithology" | property of a unit, not a standalone location |
| Stratigraphic Interval | "Stratigraphic interval" | show interval + correlation basis |
| StratigraphicCorrelation | "Correlation" | "correlated with", never "same as" |
| StructureFeature / Fault Structure | "Structure / fault" | context for Hazards, **never** a hazard-risk claim (see §10) |
| GeologyBoundaryVersion | "Boundary version" | always show when a boundary was revised |
| BoreholeReference | "Borehole (generalized)" | **exact location withheld by default**; observation verb |
| Well LogReference | "Well log (generalized)" | exact API/well number withheld; observation verb |
| Core Sample / Geophysical Observation | "Core / geophysical sample" | observation verb; sample, not interpretation |
| Geochemistry SampleReference | "Geochemistry sample" | observation verb; show uncertainty |
| Mineral Occurrence | "Mineral occurrence (generalized)" | occurrence ≠ deposit ≠ economic resource |
| Resource Deposit / ResourceEstimate | "Resource estimate (modeled)" | **model verb**; never "proven reserve" unless the bundle says so |
| Extraction Site / Reclamation Record | "Extraction / reclamation context" | context; never an ownership or permit claim |
| Hydrostratigraphic Unit | "Hydrostratigraphic unit" | Geology owns the unit; Hydrology owns the measurement |
| CrossSection | "Cross-section" | interpretive; label as interpretation |
| RedactionReceipt | "Why this is generalized" | transform metadata only; no withheld value |

[Back to top ↑](#contents)

---

## 10. Forbidden phrasings

These strings must never appear in the geology drawer, regardless of payload. Each maps to a CONFIRMED doctrine rule.

| Forbidden phrasing | Why | Rule |
|---|---|---|
| Any exact coordinate, well API number, or precise deposit point | Location sensitivity | §23.2; Atlas §24.5 |
| "This lease/parcel/operator proves a deposit here" | Administrative ≠ resource evidence | Atlas §10.F |
| "Proven reserve" / "economic deposit" for a modeled estimate | Source-role collapse (model→observed) | Atlas §24.1 |
| "Measured" / "observed" for an interpolated or modeled surface | Source-role collapse | Atlas §24.1 |
| "Fault → hazard risk here" | Geology provides fault *context*; it does not own risk | Atlas §10.F (Hazards edge) |
| "Aquifer yields [X]" from a geology feature | Hydrology owns measurements | Atlas §10.F (Hydrology edge) |
| A feature-level redaction reason that re-identifies the site | Leaks via explanation | Atlas §8.G |
| A confident sentence with no resolved bundle | Rendered-feature-only claim | MAP-MASTER §N |

[Back to top ↑](#contents)

---

## 11. File-home & placement notes

> [!NOTE]
> All paths below other than `directory-rules.md` are **PROPOSED / NEEDS VERIFICATION** per Directory Rules §12 (Domain Placement Law). The drawer is a shared shell; Geology supplies strings, not a component.

```text
docs/domains/geology/EVIDENCE_DRAWER_LANGUAGE.md   # this file
docs/domains/geology/EVIDENCE_DRAWER.md            # the payload contract (sibling)
contracts/runtime/evidence_drawer_payload.md        # shared payload contract (cross-cutting)
policy/domains/geology/                             # sensitivity / redaction policy the words obey
i18n/ or strings/ (PROPOSED)                        # if drawer copy is externalized for localization
fixtures/domains/geology/drawer/                    # geology drawer string fixtures
tools/validators/ui/                                # forbidden-phrasing / no-leak validators (cross-cutting)
```

> [!WARNING]
> **DR-GEOL-PATH-01 (CONFLICTED).** As with every domain lane, Directory Rules §12 places geology artifacts under a `domains/` segment (`policy/domains/geology/`, `schemas/contracts/v1/domains/geology/`), while Atlas §24.13 omits it (`policy/sensitivity/geology/`, `schemas/contracts/v1/geology/`). Per the authority order (`directory-rules.md` §2.1), **Directory Rules wins on placement** — this doc uses the §12 form. File a `DRIFT_REGISTER.md` row; resolve by ADR-S-01.

> [!IMPORTANT]
> **The string catalog is geology-scoped; the drawer surface is shared.** Do not create a geology-specific drawer component or a parallel payload home. This doc is a *language layer* over the shared `EvidenceDrawerPayload`.

[Back to top ↑](#contents)

---

## 12. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-GEOLDL-01 | Are drawer strings externalized (i18n/strings file) or inline? Where do they live? | UX-copy + AI-surface steward | ADR; confirm against mounted repo |
| OQ-GEOLDL-02 | What generalization level (grid vs county vs section-masked) backs the "Borehole (generalized)" label? | Geology + policy steward | `policy/domains/geology/`; ADR |
| OQ-GEOLDL-03 | Exact `SOURCE_STALE` freshness windows per geology source family (KGS maps vs KCC regulatory vs LAS logs)? | Release steward | ADR-S-10 stale-state |
| OQ-GEOLDL-04 | Tie-breaker phrasing when two authorities (KGS vs USGS GeMS) map a unit differently? | Geology steward | conflict-panel policy; ADR |
| OQ-GEOLDL-05 | Which placement form is canonical (DR-GEOL-PATH-01)? | Docs + schema steward | ADR-S-01; Directory Rules §2.1 governs meanwhile |
| OQ-GEOLDL-06 | Does a forbidden-phrasing validator exist, and is the §10 list the source of truth for it? | AI-surface steward | mounted-repo check; ADR |

[Back to top ↑](#contents)

---

## 13. Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Confirm the shared `EvidenceDrawerPayload` contract exists and that the geology label set in §9 projects onto it. — NEEDS VERIFICATION
2. Confirm the geology object-family list (§9) against authored geology contracts. — NEEDS VERIFICATION
3. Confirm generalization levels behind the "generalized" labels (§6, §9). — NEEDS VERIFICATION
4. Confirm a forbidden-phrasing / no-leak validator runs against the §10 list. — NEEDS VERIFICATION
5. Confirm `SOURCE_STALE` freshness windows per geology source family. — NEEDS VERIFICATION
6. Confirm the conflict-panel phrasing path for authority disagreements. — NEEDS VERIFICATION
7. Resolve DR-GEOL-PATH-01 by ADR. — CONFLICTED
8. Confirm rights/terms for KGS, KCC, USGS NGMDB/GeMS/MRDS, KGS/KDHE WWC5 before any string sourced from them publishes. — NEEDS VERIFICATION

[Back to top ↑](#contents)

---

## 14. Changelog

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial draft of the Geology Evidence Drawer language catalog | new | The lane needed a governed home for drawer strings distinct from the payload contract |
| Encoded source-role verbs (§4) and the deposit-proof / fault-risk / aquifer-yield forbidden phrasings (§10) | gap closure | Atlas §10.F and §24.1 are the most likely places geology copy collapses roles or over-claims |
| Built the redaction language around "explain the reason, never the location" (§6) | reconciliation | Atlas §8.G; geology well/deposit locations are the sensitive surface |
| Surfaced DR-GEOL-PATH-01 (§12 vs §24.13) as CONFLICTED | reconciliation | Consistent with the flora doc set's DR-FLORA-PATH-01 treatment |
| Pinned `CONTRACT_VERSION = "3.0.0"`, `directory-rules.md` v1.3, `RuntimeResponseEnvelope`, `SOURCE_STALE` | housekeeping | Required pins for a doctrine-adjacent doc |

> **Backward compatibility.** New document; no prior anchors to preserve. Section anchors §1–§16 are stable for inbound links from the geology doc set.

[Back to top ↑](#contents)

---

## 15. Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/geology/EVIDENCE_DRAWER_LANGUAGE.md`, PROPOSED);
- a docs steward, the geology domain steward, and a UX-copy/AI-surface steward review it;
- it is linked from `docs/domains/geology/README.md` and `EVIDENCE_DRAWER.md`;
- it does not conflict with accepted ADRs (and DR-GEOL-PATH-01 is filed in `DRIFT_REGISTER.md`);
- the §10 forbidden-phrasing list is wired into a validator or explicitly tracked as PROPOSED;
- the `GENERATED_RECEIPT.json` planned in Section 2 is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

[Back to top ↑](#contents)

---

## 16. Related docs

> [!NOTE]
> All paths below other than `directory-rules.md` are **PROPOSED / NEEDS VERIFICATION**; their presence in the live repo has not been checked in this session.

- `docs/doctrine/directory-rules.md` — **CONFIRMED** (v1.3)
- `ai-build-operating-contract.md` — operating contract (`CONTRACT_VERSION = "3.0.0"`) — CONFIRMED (in project)
- `docs/domains/geology/README.md` — geology lane landing — PROPOSED
- `docs/domains/geology/EVIDENCE_DRAWER.md` — drawer payload contract — PROPOSED
- `docs/domains/geology/CROSS_LANE_NOTES.md` — cross-lane edge ownership (Soil/Hydrology/Hazards/People-Land) — PROPOSED
- `docs/domains/geology/SENSITIVITY.md` — geology sensitivity / deny-by-default register — PROPOSED
- `docs/architecture/governed-ai/README.md` — Focus Mode / finite outcomes — PROPOSED
- `docs/standards/ux-copy.md` — cross-cutting UX-copy standard — PROPOSED
- `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md` — PROPOSED

**Source-corpus tag legend:**

| Tag | Resolves to |
|---|---|
| `[ATLAS]` | Domains Culmination Atlas v1.1 — §10 Geology (10.B owned objects, 10.C ubiquitous language, 10.D sources, 10.E objects, 10.F cross-lane, 10.G viewing products); §8.G sensitivity-redacted view; §24.1 source-role anti-collapse; §24.5 tiers; §24.6 gates; §24.13 crosswalk |
| `[MAP-MASTER]` | Master MapLibre Components v2.1 §N Evidence Drawer; trust-state idea cards ML-059-061, ML-060-027, ML-061-138/139/140 |
| `[ENCY]` | KFM Encyclopedia Geology chapter |
| `[GAI]` | KFM governed-AI doctrine (finite outcomes, cite-or-abstain) |
| `[DIRRULES]` | `docs/doctrine/directory-rules.md` (v1.3) |

---

<sub>
<b>Last reviewed:</b> 2026-06-03 ·
<b>Version:</b> v1 (draft) ·
<b>Contract:</b> CONTRACT_VERSION = "3.0.0" ·
<b>Owner:</b> &lt;geology-domain-steward&gt; (PLACEHOLDER) ·
<a href="#-geology-domain--evidence-drawer-language">Back to top ↑</a>
</sub>
