<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/accessibility
title: KFM UI — Accessibility Architecture
type: standard
version: v0.1
status: draft
owners: Docs steward + UI subsystem owner + Accessibility reviewer
created: 2026-05-14
updated: 2026-05-14
policy_label: public
related:
  - docs/architecture/ui/README.md
  - docs/architecture/ui/STATE_OWNERSHIP.md
  - docs/architecture/ui/BOUNDARIES.md
  - docs/architecture/ui/ROUTE_MAP.md
  - docs/architecture/ui/CONTINUITY_NOTES.md
  - docs/architecture/governed-ai/README.md
  - docs/architecture/map-shell.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - schemas/contracts/v1/ui/EvidenceDrawerPayload.schema.json
  - schemas/contracts/v1/runtime/RuntimeResponseEnvelope.schema.json
tags: [kfm, ui, accessibility, a11y, trust-visible, governed-ai]
notes:
  - All repo paths PROPOSED until verified against mounted-repo evidence (Directory Rules §0).
  - Section 20.1 of the Whole-UI + Governed AI Expansion Report is the doctrinal anchor for smoke criteria.
[/KFM_META_BLOCK_V2] -->

# KFM UI — Accessibility Architecture

> How the Kansas Frontier Matrix UI shell makes governed truth — finite outcomes, evidence resolution, policy decisions, and freshness state — perceivable, operable, understandable, and robust for every user, on every supported surface.

![status: draft](https://img.shields.io/badge/status-draft-blue)
![doc class: architecture](https://img.shields.io/badge/doc%20class-architecture-6f42c1)
![authority: PROPOSED](https://img.shields.io/badge/authority-PROPOSED-orange)
![scope: ui](https://img.shields.io/badge/scope-ui-2ea44f)
![standard: WCAG 2.2 AA · target](https://img.shields.io/badge/standard-WCAG%202.2%20AA%20%C2%B7%20target-lightgrey)
![last reviewed: 2026-05-14](https://img.shields.io/badge/last%20reviewed-2026--05--14-informational)

**Status:** draft · **Owners:** Docs steward + UI subsystem owner + Accessibility reviewer · **Last updated:** 2026-05-14

> [!IMPORTANT]
> This document is **doctrine-grade design**. All paths, route names, component names, validators, and CI hooks named here are **PROPOSED** until verified against mounted-repo evidence per Directory Rules §0 and §17. Where this doc says "the shell does X," read "the shell **must** do X to satisfy the trust-visible-states contract." Implementation maturity is **UNKNOWN** in this session.

---

## Quick jump

- [1. Purpose & scope](#1-purpose--scope)
- [2. Why accessibility is governance, not finish](#2-why-accessibility-is-governance-not-finish)
- [3. Doctrinal anchors](#3-doctrinal-anchors)
- [4. The trust-visible state model](#4-the-trust-visible-state-model)
- [5. Keyboard, focus, and dialog discipline](#5-keyboard-focus-and-dialog-discipline)
- [6. Map alternatives (the non-map path)](#6-map-alternatives-the-non-map-path)
- [7. Motion, animation, and Story Node behavior](#7-motion-animation-and-story-node-behavior)
- [8. Perception, contrast, and zoom legibility](#8-perception-contrast-and-zoom-legibility)
- [9. Alt text, popups, and the Evidence Drawer](#9-alt-text-popups-and-the-evidence-drawer)
- [10. Touch and narrow-viewport behavior](#10-touch-and-narrow-viewport-behavior)
- [11. Accessibility smoke criteria (canonical)](#11-accessibility-smoke-criteria-canonical)
- [12. Validation surfaces and CI hooks](#12-validation-surfaces-and-ci-hooks)
- [13. Negative, abstain, deny, and stale states](#13-negative-abstain-deny-and-stale-states)
- [14. Export and screenshot continuity](#14-export-and-screenshot-continuity)
- [15. Anti-patterns](#15-anti-patterns)
- [16. Open questions and NEEDS VERIFICATION](#16-open-questions-and-needs-verification)
- [17. Related docs](#17-related-docs)

---

## 1. Purpose & scope

This document specifies the **accessibility architecture** for the Kansas Frontier Matrix (KFM) UI shell — the governed, map-first, time-aware interface where Evidence Drawer, Focus Mode, Story Node, Review/steward, layer catalog, and diagnostics surfaces meet the public.

**In scope.**

- Trust-visible state semantics (how `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `stale`, `restricted`, `cancelled`, `loading` reach users with assistive technology).
- Keyboard, focus, and dialog behavior for the map shell, drawer, dialogs, layer catalog, time control, and Focus Mode.
- Non-map alternatives for every map-driven interaction.
- Motion, animation, and Story Node reduced-motion behavior.
- Contrast, color-not-alone, alt text, and zoom legibility for trust artifacts.
- Smoke criteria, validation surfaces, and CI hooks the UI subsystem must satisfy before public release.

**Out of scope.**

- Visual design tokens, palette choices, and component implementation (lives in `packages/ui/` per Directory Rules §11; **PROPOSED**).
- Schema field definitions for `EvidenceDrawerPayload`, `RuntimeResponseEnvelope`, etc. (lives under `schemas/contracts/v1/` per ADR-0001; **PROPOSED**).
- Map renderer internals (covered by `docs/architecture/map-shell.md`; **PROPOSED**).
- Document-level accessibility (PDF/UA) for generated reports, which is covered separately by C13-03 in the Idea Index and is **out of scope** here.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 2. Why accessibility is governance, not finish

In KFM, the UI is the public face of a governed truth membrane. Cite-or-abstain is the default truth posture, and outcomes are **finite and visible** — `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. (CONFIRMED doctrine; Whole-UI + Governed AI Expansion Report §19.)

If those outcomes are not perceivable, operable, understandable, and robust, then a screen-reader user reads a blank map; a keyboard-only steward cannot reach the drawer; a low-vision user cannot tell `stale` from `released`; a reduced-motion user is forced through a cinematic Story Node camera; or a touch user loses the freshness chip behind a collapsed panel. In every one of those cases the governance contract collapses silently — the failure is **not** that the UI is impolite, it is that **the trust membrane stops being visible**.

> [!NOTE]
> Accessibility in KFM is not a final coat of paint. It is part of the same contract that says **a popup is not the Evidence Drawer**, **a screenshot is not proof**, and **fluent text is not evidence**. A state that cannot be announced, traversed, contrasted, and labeled is a state the public cannot trust.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 3. Doctrinal anchors

These are the source documents and invariants this architecture inherits from.

| Anchor | Source | Truth label |
|---|---|---|
| Cite-or-abstain truth posture | KFM core invariants; `docs/doctrine/truth-posture.md` | **CONFIRMED doctrine** |
| Finite outcomes — `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | Whole-UI + Governed AI Expansion Report §19; KFM Encyclopedia §8C | **CONFIRMED doctrine** |
| Trust membrane (no public RAW/WORK/QUARANTINE; no popup-as-proof) | `docs/doctrine/trust-membrane.md`; Encyclopedia §8A–B | **CONFIRMED doctrine** |
| Accessibility smoke criteria | Whole-UI + Governed AI Expansion Report §20.1 | **CONFIRMED doctrine** |
| MapLibre is the renderer, not the truth store | Encyclopedia §8A; Directory Rules §11 | **CONFIRMED doctrine** |
| Trust badges do not rely on color alone | Expansion Report §20.1; ML-S-020; ML-061-140 | **CONFIRMED doctrine** |
| Reduced-motion mode disables/shortens Story Node camera | Expansion Report §20.1; ML-059-087 | **CONFIRMED doctrine** |
| Map interactions have non-map alternatives | Expansion Report §20.1 | **CONFIRMED doctrine** |
| WCAG 2.2 AA as the **target conformance level** | Industry standard reference | **PROPOSED** for KFM (target; no measurement) |
| PDF/UA preflight for generated PDFs | Idea Index C13-03 | **PROPOSED**, out of scope here |
| ARIA Authoring Practices for dialog, listbox, tab, slider patterns | External standard reference | **PROPOSED** as pattern source |

> [!NOTE]
> WCAG 2.2 AA is the **target** conformance level for the public surfaces. It is **not** a claim that any rendered build has been measured. Conformance measurement is an open verification item — see §16.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 4. The trust-visible state model

Every governed UI surface — Evidence Drawer, Focus Mode response, layer chip, time chip, drawer header, Story Node node, review row — must surface enough of the governance state for an assistive technology user to know **what kind of answer they are looking at** before they read its content.

### 4.1 Required state axes

Every consequential rendered claim must expose, in text and not by color alone, these axes:

| Axis | Vocabulary (illustrative) | Required for |
|---|---|---|
| Outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Focus Mode response, drawer header |
| Source role | `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic` | drawer evidence rows |
| Rights | `public`, `restricted`, `unknown` | drawer header, layer chip |
| Sensitivity | `none`, `geoprivacy`, `CARE`, `sovereignty`, `archaeology`, … | drawer header, Story Node node |
| Review state | `unreviewed`, `in-review`, `approved`, `corrected`, `superseded` | drawer header, review console |
| Freshness | `fresh`, `stale`, `unknown` | layer chip, drawer header, time chip |
| Release state | `published`, `unreleased`, `withdrawn` | layer chip, drawer header |
| Correction state | `none`, `correction-applied`, `correction-pending` | drawer header |

Vocabulary above is **illustrative**; canonical enumerations live in the appropriate `schemas/contracts/v1/` schemas (**PROPOSED**, ADR-0001).

### 4.2 No color-alone rule

> [!WARNING]
> Color is **never** sufficient to communicate trust state. Every state token must carry a **text label**, an **accessible name**, and an **icon shape or letterform** distinguishable in monochrome. A red border is not a `DENY`; the literal word and reason code make it a `DENY`. (ML-S-020; ML-061-140; Expansion Report §20.1.)

### 4.3 Distinct treatment for unknown / stale / failed verification

`unknown`, `stale`, and `failed-verification` MUST each have a **visually and textually distinct** treatment. Folding them together — for example, painting all three grey with the same label — collapses a meaningful distinction that the trust contract relies on. (ML-061-140; Expansion Report §20.1.)

### 4.4 Live-region announcement

When a finite outcome changes — drawer opens with `ANSWER`, Focus Mode returns `ABSTAIN`, a layer chip flips to `stale`, a request is cancelled — the change MUST be announced through an ARIA live region of appropriate politeness:

- `assertive` — `DENY`, `ERROR`, restricted-geometry redaction event.
- `polite` — `ANSWER`, `ABSTAIN`, freshness change, correction applied.
- not announced — purely visual hover preview without semantic change.

Exact ARIA wiring is a **PROPOSED** implementation detail; the requirement is that no consequential state change is silent.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 5. Keyboard, focus, and dialog discipline

The map shell, drawer, dialogs, layer catalog, time control, and Focus Mode form a **keyboard-complete** surface: every action available with a pointer is available with the keyboard, and every action's effect is announced to assistive technology.

### 5.1 Keyboard contract

| Surface | Required keyboard behavior |
|---|---|
| App shell | Stable landmark roles (banner, navigation, main, complementary, contentinfo); skip-to-main link as the first focusable item. |
| Route navigation | Reachable and operable by keyboard alone; current route announced. |
| Map canvas | Receives focus; arrow keys pan; `+`/`-` zoom; `Enter` activates focused feature; `Esc` returns focus to map controls. |
| Layer catalog | Tab into list; arrow keys move within; `Space` toggles; toggling announces new layer state, source role, rights, freshness, release state. |
| Time control | Keyboard-operable slider with discrete steps; current valid time, source time, and version-lock state announced. |
| Drawer | Opens with focus moved to the drawer's first heading; `Esc` closes and returns focus to the invoking element. |
| Dialog | Modal focus trap; `Tab` cycles within; `Esc` closes; background inert. |
| Focus Mode | Question control reachable by keyboard; response region is a live region; citations are focusable links. |
| Story Node | Arrow keys move through the version strip (predecessor/current/successor/latest), as in ML-059-019. |
| Verification badge | Focusable; activation opens proof details — **not** a replacement for the Evidence Drawer (ML-061-139). |

### 5.2 Focus order and visibility

- Focus order MUST match the visible reading order; tab traps exist only inside true modals.
- The focus indicator MUST be visible on every interactive element at every theme — light, dark, high-contrast.
- Focus must not be lost when a panel opens, closes, or rerenders; on close, focus returns to the invoking control.

### 5.3 Drawer / dialog focus management

> [!IMPORTANT]
> The Evidence Drawer is **the trust object**, not a popup. Its focus behavior is part of the contract. On open: focus moves to the drawer; on close: focus returns to the trigger; on internal navigation (citation, lineage break, badge activation): focus remains predictable and never lands in unrelated map space. (ML-S-019.)

[Back to top](#kfm-ui--accessibility-architecture)

---

## 6. Map alternatives (the non-map path)

A map alone is not an accessible interface. Every consequential map interaction MUST have a **non-map alternative** — a keyboard-reachable list or table that exposes the same state, in the same vocabulary, with the same outcomes. (Expansion Report §20.1.)

### 6.1 Required alternatives

| Map interaction | Non-map alternative |
|---|---|
| Click a feature → drawer | A keyboard-reachable list of currently selected features, each opening the drawer for that feature. |
| Pan to a region | A search/select input that scopes the result list to that region. |
| Toggle layers visually | The layer catalog panel, with the same toggles, badges, and freshness chips. |
| Read time state | A time-state panel showing valid time, source time, release time, and version-lock status. |
| See "what's here" | A results list/table showing the same features, each with source role, rights, sensitivity, freshness, and release state. |
| Focus Mode camera | A summary panel that produces the same `ANSWER`/`ABSTAIN`/`DENY`/`ERROR` outcome without animation. |

### 6.2 Non-map alternatives are first-class, not fallback

The list/table view MUST be discoverable by sighted keyboard users and screen-reader users **on the same page** as the map — not behind a separate "accessible view" toggle that hides it from the default experience. The principle is **equivalent access in the default experience**, not a parallel impoverished view.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 7. Motion, animation, and Story Node behavior

Motion is a governance signal in KFM (it carries Story Node sequence, time-slice scrubbing, drawer transitions, and Focus Mode cinematics). It is also an accessibility hazard for users with vestibular disorders, photosensitive conditions, and cognitive-load constraints.

### 7.1 Reduced-motion contract

When the user-agent indicates reduced motion (e.g. `prefers-reduced-motion: reduce`), the shell MUST:

- Disable or substantially shorten Story Node camera animation and drawer transitions (Expansion Report §20.1; ML-059-087).
- Replace any time-slice scrubbing animation with discrete state changes.
- Render Focus Mode answers without cinematic camera moves; outcomes still display in full.
- Prefer cross-fades or instant cuts over translations, rotations, and zooms.
- Never make a finite outcome conditional on motion completing — outcomes are textual and present in DOM order on render.

### 7.2 Motion alternatives are not optional

> [!CAUTION]
> If a Story Node, Focus Mode camera path, or 3D scene cannot preserve evidence/release/drawer continuity in a reduced-motion or 2D-fallback mode, the node MUST fall back to 2D or `ABSTAIN` rather than render an inaccessible cinematic. 3D is a **conditional companion**, not an alternative truth path. (Encyclopedia §8C; Expansion Report §19.3.)

[Back to top](#kfm-ui--accessibility-architecture)

---

## 8. Perception, contrast, and zoom legibility

### 8.1 Contrast

| Surface | Minimum contrast (target) |
|---|---|
| Body text against background | 4.5 : 1 |
| Large text (≥ 18 pt / 14 pt bold) | 3 : 1 |
| Interactive controls and focus indicators | 3 : 1 against adjacent colors |
| Non-text trust artifacts (chips, badge shapes, freshness pips) | 3 : 1 against adjacent colors |

These targets align with WCAG 2.2 AA conventions. Actual measurement of any rendered theme is **NEEDS VERIFICATION**.

### 8.2 Colorbars and trust-visible color use

Flood depth/velocity/risk colorbars and trust chips MUST carry WCAG-compatible contrast, explicit text labels, and provenance metadata (ML-059-071). Colorblind-safe palettes are preferred; pattern, shape, or icon redundancy is required where color carries semantic load.

### 8.3 Zoom and reflow

Trust-visible information must remain legible at **200% zoom** without loss of state, and panels must reflow without horizontal scrolling at 320 CSS px width (ML-059-047; common WCAG 2.2 reflow target). Sidecar metadata and provenance text are **not** allowed to be truncated out of the visible state.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 9. Alt text, popups, and the Evidence Drawer

### 9.1 Alt text on map media

Field media, photographs, and figures bound to map features MUST have meaningful alt text. Where evidence comes from STAC items, accessibility metadata belongs **in the field STAC assets** themselves so that Evidence Drawer rows can render an accessible description without re-derivation (ML-064-059; ML-064-091).

### 9.2 Popup is not the drawer

> [!IMPORTANT]
> A map popup is a **cue**, not a citation surface. It must not substitute for the Evidence Drawer for consequential claims (ML-059-061; ML-061-139). Popups MAY summarize, but consequential claims resolve through the Evidence Drawer with focus management, ARIA semantics, and announced state changes.

### 9.3 Accessible Evidence Drawer fields

The Evidence Drawer SHOULD expose these accessible elements:

- Drawer heading naming the layer, feature, and outcome (`ANSWER`/`ABSTAIN`/`DENY`/`ERROR`).
- Trust strip with source role, rights, sensitivity, review, freshness, release, correction — each as labeled text.
- Evidence list, each row focusable and exposing its `EvidenceRef`-derived label.
- Citation links, each with a descriptive accessible name (not "click here").
- Reason codes for `ABSTAIN` and `DENY`, in plain language.
- Lineage break notices rendered as readable text, never as silent breaks (ML-061-089).

[Back to top](#kfm-ui--accessibility-architecture)

---

## 10. Touch and narrow-viewport behavior

Touch and narrow-viewport layouts MUST keep map, time context, drawer, and focus states usable without hiding critical trust information (Expansion Report §20.1).

Concretely:

- Hit targets for trust chips, drawer toggles, and time controls are at least 24 × 24 CSS px (WCAG 2.2 target-size minimum-target). 44 × 44 CSS px is preferred for primary controls.
- The freshness chip, rights chip, and outcome label MUST remain visible at narrow widths; they may relocate but may not be collapsed into an undisclosed overflow.
- Drawer behavior on narrow widths preserves focus trap and `Esc`-to-close semantics.
- The non-map list/table alternative remains reachable from narrow viewports.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 11. Accessibility smoke criteria (canonical)

These are the canonical pre-release smoke criteria for the KFM UI shell, adapted from Whole-UI + Governed AI Expansion Report §20.1 (CONFIRMED doctrine). Each is a release gate; missing criteria block public exposure of the affected surface.

| # | Criterion | Source |
|---|---|---|
| A1 | Keyboard-only route navigation and panel open/close is possible; focus order is stable; drawer and dialogs trap and release focus correctly. | Expansion Report §20.1 |
| A2 | Map interactions have non-map alternatives: selected features and results appear in a keyboard-accessible list/table. | Expansion Report §20.1 |
| A3 | Trust badges do not rely on color alone; text labels are available for source role, rights, sensitivity, review, freshness, release, and correction state. | Expansion Report §20.1; ML-S-020 |
| A4 | Reduced-motion mode disables or shortens Story Node camera animation and drawer transitions. | Expansion Report §20.1; ML-059-087 |
| A5 | Touch and narrow-viewport layouts keep map, time context, drawer, and focus states usable without hiding critical trust information. | Expansion Report §20.1 |
| A6 | Loading, cancelled, denied, abstained, error, stale, and restricted states are announced and visibly differentiated. | Expansion Report §20.1; ML-061-140 |
| A7 | Verification badge state is keyboard-reachable, contrast-compliant, and screen-reader-described; activation opens proof detail, not a drawer replacement. | ML-061-138; ML-061-139 |
| A8 | CARE labels and sovereignty notice chips are rendered as text in the UI for sensitive material. | ML-061-160; ML-061-164 |
| A9 | Map media and field photographs carry alt text sourced from STAC asset metadata. | ML-064-059; ML-064-091 |
| A10 | Trust-visible information remains legible at 200% zoom and reflows at 320 CSS px width. | ML-059-047 |

> [!NOTE]
> A1–A6 are **CONFIRMED doctrine** under Expansion Report §20.1. A7–A10 are **CONFIRMED doctrine** from the MapLibre Master atlas Category S evidence but require fixture coverage before they can be claimed as enforced.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 12. Validation surfaces and CI hooks

The architecture above is enforced through a layered validation surface. **All paths and validator names are PROPOSED until verified against mounted-repo evidence.**

### 12.1 Diagram — accessibility validation surfaces

```mermaid
flowchart LR
    A[Author / PR] --> B[Schema validation]
    B --> C[Unit & component tests]
    C --> D[Accessibility smoke<br/>Playwright + axe-like + keyboard script]
    D --> E[E2E smoke<br/>finite-outcome rendering]
    E --> F[Visual regression<br/>contrast & badge state]
    F --> G[Policy tests<br/>DENY / ABSTAIN / restricted paths]
    G --> H[Release gate]
    H -. fails closed .-> X((No public exposure))
    H --> Y[Public surface]

    classDef gate fill:#fff4e5,stroke:#d97706,color:#7c2d12;
    classDef proof fill:#ecfdf5,stroke:#059669,color:#064e3b;
    class B,C,D,E,F,G gate
    class H,Y proof
```

> [!NOTE]
> Diagram reflects the validation **responsibility surface**, not a verified workflow. PR workflow YAML, runner targets, and gate ordering are **PROPOSED** until the repo is mounted.

### 12.2 Proposed validation matrix

| Check | Command family (PROPOSED) | Expected result |
|---|---|---|
| Schema validation | `ajv` / `jsonschema` over `schemas/contracts/v1` and UI fixtures | Valid fixtures pass; invalid fail |
| Unit / component tests | `npm`/`pnpm`/`yarn test` | Shell, drawer, focus, layers pass |
| Accessibility smoke | Playwright + axe-like checks + keyboard script | No critical violations; map actions have non-map alternatives |
| E2E smoke | Playwright route/load/focus/map-click | Finite outcomes display correctly |
| Visual regression | Storybook / Loki / Playwright screenshots | Contrast and badge-state snapshots stable |
| Policy tests | `conftest` or repo policy runner | DENY invalid, unreleased, uncited, restricted flows |
| Reduced-motion smoke | `prefers-reduced-motion: reduce` Playwright override | Story Node camera and drawer transitions degrade gracefully |

Adapted from Whole-UI + Governed AI Expansion Report §20 validation checklist. Status of each check in the current session is **PROPOSED** — no workflow YAML or runner has been verified.

### 12.3 Proposed test files

| File (PROPOSED path) | Purpose |
|---|---|
| `tests/accessibility/ui_shell_axe.spec.ts` | Accessibility smoke with keyboard and axe-like checks |
| `tests/ui/FocusOutcomeRenderer.test.ts` | Finite outcome rendering tests (ANSWER/ABSTAIN/DENY/ERROR) |
| `tests/ui/LayerCatalogPanel.test.tsx` | Layer catalog/toggle/legend tests |
| `tests/e2e/ui_shell_smoke.spec.ts` | Shell load / navigation smoke |
| `tests/e2e/focus_negative_states.spec.ts` | ABSTAIN / DENY / ERROR e2e behavior |

Paths from Whole-UI + Governed AI Expansion Report §29; **PROPOSED** until verified.

[Back to top](#kfm-ui--accessibility-architecture)

---

## 13. Negative, abstain, deny, and stale states

> [!IMPORTANT]
> Negative states are not error UX — they are **first-class governance outcomes**. A user with assistive technology must be able to tell `ABSTAIN` from `DENY` from `ERROR` from `stale` without reading the surrounding paragraph. (ML-S-063; Expansion Report §19.)

<details>
<summary><strong>Required announced behaviors per state</strong> (click to expand)</summary>

| State | Visible treatment (required) | Announcement (required) | Reason exposure |
|---|---|---|---|
| `loading` | Text + non-color indicator; not silent | Polite — "Loading <surface>" | n/a |
| `cancelled` | Distinct from loading and error | Polite — "Cancelled" | Optional cause |
| `ANSWER` | Outcome label + citation list | Polite — "Answer with N citations" | n/a |
| `ABSTAIN` | Outcome label + reason codes | Polite — "Abstained: <reason>" | Required reason code in plain language |
| `DENY` | Outcome label + policy reason | Assertive — "Denied: <reason>" | Required reason code; no sensitive leak |
| `ERROR` | Outcome label + safe diagnostic | Assertive — "Error: <safe message>" | Generic; no RAW/QUARANTINE/credential leak |
| `stale` | Distinct chip + age text | Polite — "Stale source as of <date>" | Optional source-head note |
| `restricted` | Redaction or generalization chip | Assertive on first encounter | Required obligation in plain language |
| `failed-verification` | Distinct from stale and from unknown | Assertive | Required reason code |
| `unknown` | Distinct from stale and from failed | Polite | Optional explanation |

</details>

Diagnostics MUST NOT leak `RAW`/`WORK`/`QUARANTINE` data, restricted coordinates, credentials, prompts, or internal store handles, even in error messages. (Expansion Report §19.4.)

[Back to top](#kfm-ui--accessibility-architecture)

---

## 14. Export and screenshot continuity

When the user exports a map view, snapshot, or report, the accessible state SHOULD travel with it:

- Verification badge state and manifest ID preserved in exports (ML-061-141).
- Alt text for exported imagery carried from STAC asset metadata.
- CARE labels, sovereignty notices, generalization logs, and freshness state preserved in any printed or PDF artifact.
- For generated PDFs, the document-level PDF/UA preflight applies (Idea Index C13-03; **PROPOSED**, out of scope for this doc but linked).

[Back to top](#kfm-ui--accessibility-architecture)

---

## 15. Anti-patterns

> [!WARNING]
> The patterns below collapse the trust-visible-state contract. They are not stylistic preferences; they are forbidden in public surfaces.

- **Color-only trust signaling.** Red border without label, grey chip without state name, traffic-light dots without text. (ML-S-020.)
- **Folding `unknown`, `stale`, and `failed-verification` into one grey blob.** Each must be distinguishable. (ML-061-140.)
- **Popup as proof.** A popup that displays evidence but lacks Evidence Drawer focus, ARIA semantics, and citation surface. (ML-059-061; ML-061-139.)
- **Badge as proof.** A verification badge that does not link to its receipts/attestations. (ML-061-138; ML-061-139.)
- **Parallel "accessible view" toggle.** A separate impoverished page that hides accessibility from the default experience.
- **Cinematic-only Focus Mode.** A Focus Mode answer that depends on motion completing or 3D rendering to surface its outcome.
- **Silent state changes.** A drawer outcome that changes from `ANSWER` to `ABSTAIN` without announcement.
- **Diagnostic leak.** An error message that exposes RAW/WORK/QUARANTINE handles, prompts, credentials, or restricted coordinates.
- **Sensitive geometry by style filter.** Hiding restricted features with a style filter rather than denying publication. (Master atlas; sensitive-geometry deny tests.)

[Back to top](#kfm-ui--accessibility-architecture)

---

## 16. Open questions and NEEDS VERIFICATION

These items are checkable but not yet checked strongly enough to act as fact in this session.

| # | Item | Status |
|---|---|---|
| OQ-1 | Which WCAG version (2.1 vs 2.2) is the formal target conformance level for KFM public surfaces? This doc currently writes **WCAG 2.2 AA** as a working target. | NEEDS VERIFICATION |
| OQ-2 | Which axe-like engine (axe-core, Pa11y, custom) is the chosen smoke runner? | NEEDS VERIFICATION |
| OQ-3 | Does any rendered build of the shell exist that can be measured against §11 criteria today? | UNKNOWN |
| OQ-4 | Where does the canonical enumeration of trust state vocabulary live in `schemas/contracts/v1/`? | PROPOSED (ADR-0001 implies; not verified) |
| OQ-5 | Are ARIA live-region announcements localized? If KFM gains non-English locales, freshness/outcome messages need locale-aware text. | UNKNOWN |
| OQ-6 | What is the minimum target-size policy — WCAG 2.2 minimum (24 px) or KFM-preferred (44 px) for primary controls? | NEEDS VERIFICATION |
| OQ-7 | Does the Story Node version strip ARIA pattern follow combobox, listbox, or tab semantics? ML-059-019 names keyboard arrow behavior but not the role. | NEEDS VERIFICATION |
| OQ-8 | Is there a documented "no-data" / "blank map" empty state for routes that load with zero features? (ML-S-063.) | UNKNOWN |
| OQ-9 | How does the export pipeline (§14) carry accessible state into static PDF/PNG artifacts? Does this overlap with C13-03 PDF/UA preflight? | NEEDS VERIFICATION |
| OQ-10 | Are review console keyboard flows separately gated by role, or do reviewers inherit the public shell's keyboard contract? | UNKNOWN |

Track resolution in `docs/registers/VERIFICATION_BACKLOG.md` (**PROPOSED** path per Whole-UI + Governed AI Expansion Report §29).

[Back to top](#kfm-ui--accessibility-architecture)

---

## 17. Related docs

- [`docs/architecture/ui/README.md`](./README.md) — UI subsystem overview and trust-visible shell purpose (**PROPOSED**)
- [`docs/architecture/ui/STATE_OWNERSHIP.md`](./STATE_OWNERSHIP.md) — Ownership of map, time, layer, drawer, focus, story, review, export, settings, diagnostics state (**PROPOSED**)
- [`docs/architecture/ui/BOUNDARIES.md`](./BOUNDARIES.md) — Browser allowed/forbidden operations and MapLibre adapter boundary (**PROPOSED**)
- [`docs/architecture/ui/ROUTE_MAP.md`](./ROUTE_MAP.md) — Route families and shell continuity rules (**PROPOSED**)
- [`docs/architecture/ui/CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) — How prior UI doctrine and PDF lineage are preserved (**PROPOSED**)
- [`docs/architecture/governed-ai/README.md`](../governed-ai/README.md) — Governed AI subsystem and Focus Mode finite-outcome contract (**PROPOSED**)
- [`docs/architecture/map-shell.md`](../map-shell.md) — MapLibre shell, layer registry, evidence resolution (**PROPOSED**)
- [`docs/doctrine/truth-posture.md`](../../doctrine/truth-posture.md) — Cite-or-abstain default (**PROPOSED**)
- [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) — Public/canonical separation (**PROPOSED**)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Path and responsibility-root law (**CONFIRMED in attached doctrine**; repo placement **PROPOSED**)

---

> **Last reviewed:** 2026-05-14 · **Authority:** PROPOSED (architecture doctrine; implementation maturity UNKNOWN) · [Back to top](#kfm-ui--accessibility-architecture)
