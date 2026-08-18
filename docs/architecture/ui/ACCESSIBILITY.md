<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/accessibility
title: KFM UI — Accessibility Architecture
type: architecture
version: v1.0-draft
status: draft; repository-grounded; cross-cutting; explanatory; no-conformance-authority
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
owner_status: "CODEOWNERS routing is CONFIRMED. Accountable accessibility, UI, policy/privacy, evidence, release, and independent assistive-technology review assignments remain NEEDS VERIFICATION."
created: 2026-05-14
updated: 2026-08-18
policy_label: public
owning_root: docs/
responsibility: "Explain the KFM UI accessibility boundary, current bounded implementation evidence, target behavior, validation burden, failure posture, and graduation gates without becoming contract, schema, policy, release, publication, or conformance authority."
truth_posture: "CONFIRMED repository evidence / PROPOSED accessibility architecture / UNKNOWN production and whole-application conformance; cite-or-abstain"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 241b1f6cd76110c188449b8942a9ea93b6aedf9f
  target_prior_blob: 902f10807813152cfe8f59ec5e183c654a427cd7
  ui_architecture_readme_blob: 36d975710d906a6c4146c550d40929b1822b667e
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  explorer_manifest_blob: ddd201b74a06001d84a14bf54ac62a6cc3607a29
  explorer_entrypoint_blob: 9c95ae67333b7cbf6bc88051fa5c76e4cd97efa4
  shell_blob: 64c78c78820af33fb7a622094e4c0944ad9412f8
  evidence_drawer_blob: 7746843c259594568fe75e975155a67eb8372e8f
  evidence_drawer_contract_blob: 412a0a86c85c98748ac08e263a94c7eaac760c04
  evidence_drawer_schema_blob: 4eefa03cffd7d5b97a24df0daf250bc31f7137ca
  evidence_drawer_unit_test_blob: 24b3b4a028d31c37bd6467138ca97a54f3e21d22
  evidence_drawer_browser_test_blob: 236416b2ccb39820e426a6e774e3962480631833
  accessibility_workflow_blob: 3b2fc53fb686bfd8c2628e01e77c067857460c78
  ui_build_workflow_blob: 52382d796a8dd5ecafc39a801515aff0a8b013f8
  evidence_drawer_workflow_blob: b51b20965c8b49c415c0f4138d6056b08dec134c
  renderer_adr_blob: 6bfd66b1169728d7fad08f0bb2d7e2a56e3577b2
related:
  - docs/architecture/ui/README.md
  - docs/architecture/ui/BOUNDARIES.md
  - docs/architecture/ui/COMPARE_AND_EXPORT.md
  - docs/architecture/ui/CONTINUITY_NOTES.md
  - docs/architecture/ui/EVIDENCE_DRAWER.md
  - docs/architecture/ui/FOCUS_FLOW.md
  - docs/architecture/ui/GOVERNED_SHELL.md
  - docs/architecture/ui/LAYERING.md
  - docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - docs/architecture/ui/STORY_PLAYER.md
  - docs/architecture/ui/TELEMETRY.md
  - docs/architecture/ui/TRUST_BADGES.md
  - docs/architecture/ui/map-context-evidence-drawer-admission.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/ui/evidence_drawer_payload.md
  - schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - apps/explorer-web/src/main.ts
  - apps/explorer-web/src/features/evidence_drawer/index.tsx
  - apps/explorer-web/tests/evidence-drawer.test.ts
  - apps/explorer-web/tests/browser/evidence-drawer.spec.ts
  - .github/workflows/accessibility.yml
  - .github/workflows/ui-build.yml
  - .github/workflows/evidence-drawer-payload.yml
tags: [kfm, ui, accessibility, architecture, explorer-web, evidence-drawer, finite-outcomes, keyboard, focus, non-map-parity, trust-membrane]
notes:
  - "v1.0-draft is a same-path documentation-only reconciliation against current repository evidence."
  - "The inherited WCAG 2.2 AA statement is retained as a PROPOSED target, not a conformance claim or accepted release gate."
  - "The current accessibility workflow is an explicit non-enforcing readiness HOLD; a green run is not an accessibility pass."
  - "The default Explorer entrypoint is a bounded fail-closed shell plus fixture-driven Evidence Drawer, not a functional map, live governed client, deployment, or published product."
  - "The prior maplibre-3d dependency and implemented 3D-admission assertions are removed. docs/architecture/maplibre-3d.md is absent, ADR-0007 remains proposed, and the renderer runtime remains on HOLD."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="kfm-ui--accessibility-architecture"></a>

# KFM UI — Accessibility Architecture

> **One-line rule.** KFM accessibility keeps evidence, finite outcomes, trust state, correction state, and user control perceivable and operable without turning documentation, tests, badges, maps, or assistive-technology output into truth or release authority.

> [!IMPORTANT]
> **Current maturity is bounded.** At `main@241b1f6cd76110c188449b8942a9ea93b6aedf9f`, the default Explorer entrypoint composes a static fail-closed shell and a fixture-driven Evidence Drawer. The drawer has tested native controls, a named complementary landmark, Escape-to-close behavior, focus entry and restoration, finite text outcomes, citations, trust labels, and fixed no-leak negative copy. This evidence does **not** establish a functional map, complete route system, live governed transport, app-wide keyboard completion, automated accessibility-rule coverage, manual assistive-technology parity, WCAG conformance, deployment, release, or publication.

| Field | Current value |
|---|---|
| **Document status** | `draft` / repository-grounded architecture guidance |
| **Placement authority** | Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and adopted [`directory-rules.md`](../../doctrine/directory-rules.md) |
| **Repository review route** | `@bartytime4life` through CODEOWNERS; not proof of independent accessibility review |
| **Confirmed implementation** | Bounded shell semantics plus fixture-driven Evidence Drawer keyboard/focus behavior |
| **Accessibility workflow** | `WORKFLOW_HOLD`; no axe or full keyboard-navigation audit runs |
| **Renderer/map state** | `HOLD`; no functioning renderer or map is composed by the default entrypoint |
| **Conformance posture** | `UNKNOWN`; WCAG 2.2 AA remains a proposed target only |
| **Release/publication effect** | None |

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
- [Appendix A. No-loss modernization ledger](#appendix-a-no-loss-modernization-ledger)
- [Appendix B. Rollback](#appendix-b-rollback)

---

## 1. Purpose & scope

This document explains accessibility as a cross-cutting UI architecture responsibility. It connects the public shell, finite outcomes, evidence inspection, trust-state projection, map alternatives, story playback, comparison/export, telemetry, and any future renderer surface to a common accessibility burden.

It does **not** define semantic object meaning, machine payload shape, policy admissibility, release state, or formal accessibility conformance. Those responsibilities remain with their owning contracts, schemas, policy, implementation, tests, review records, and release artifacts.

### In scope

- current repository evidence and its limits;
- accessible projection of `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
- keyboard order, focus movement, dismissal, restoration, and route/panel transitions;
- landmarks, headings, accessible names, descriptions, status announcements, and link purpose;
- non-map alternatives for consequential map interactions;
- reduced-motion, pause/stop/skip, and non-cinematic alternatives;
- color-not-alone, contrast, text scaling, reflow, and narrow-viewport behavior;
- Evidence Drawer, trust-state, citation, history, correction, and limitation presentation;
- safe negative-state copy and protected-detail suppression;
- test, workflow, manual-review, and graduation expectations;
- export and screenshot continuity where an export carries or implies a claim.

### Out of scope

| Concern | Owning surface |
|---|---|
| Executable components and styles | [`apps/explorer-web/`](../../../apps/explorer-web/) or a reviewed shared package |
| Object meaning | [`contracts/`](../../../contracts/) |
| Machine validation | [`schemas/`](../../../schemas/) |
| Allow, deny, restrict, abstain, and disclosure obligations | [`policy/`](../../../policy/) |
| Source admission and evidence authenticity | Source/evidence lifecycle and governed resolver surfaces |
| Release, correction, withdrawal, rollback, and publication decisions | [`release/`](../../../release/) and distinct lifecycle records |
| Formal WCAG conformance statement | A scoped, reviewed conformance process backed by representative evidence |
| PDF/UA or document-export conformance | The applicable generated-document and release process |
| Renderer or plugin admission | The renderer/package decision and its accepted exception process |

### Current-state split

| Status | Bounded conclusion |
|---|---|
| **CONFIRMED** | Existing path and placement; static shell; native `main` landmark and heading; fixture-driven Evidence Drawer; finite text outcomes; named complementary landmark; open/close buttons; Escape close; focus entry/return; citation links; trust/history/limitation lists; focused unit and Playwright tests; build/test workflow; explicit accessibility workflow HOLD. |
| **PROPOSED** | Whole-shell accessibility contract, WCAG 2.2 AA target, non-map parity, reduced-motion behavior, comprehensive keyboard model, trust-badge semantics, export continuity, automated rule-engine adoption, and release gates. |
| **UNKNOWN** | Production behavior, deployed CSS, complete routes, all feature directories, map behavior, browser/device matrix, zoom/reflow results, high-contrast behavior, screen-reader parity, voice-control parity, cognitive accessibility, public operation, and formal conformance. |
| **NEEDS VERIFICATION** | Accountable accessibility owner, independent reviewer, exact supported browser/assistive-technology matrix, target-size policy, announcement priority, audit cadence, exception process, and evidence required for release significance. |

[Back to top](#top)

---

## 2. Why accessibility is governance, not finish

KFM's ordinary UI is downstream of evidence, policy, review, release, correction, and rollback. Accessibility therefore determines whether users can perceive and operate the trust membrane, not merely whether the interface is visually polished.

A consequential state is not safely exposed when:

- a keyboard user cannot reach or leave the evidence surface;
- a screen-reader user receives a generic “map” without the claim, scope, evidence, and limitation text;
- `ABSTAIN`, `DENY`, stale, corrected, or withdrawn state is communicated by color alone;
- a focus move hides the context that caused it;
- motion is required to understand a time transition or story step;
- a map click is the only way to select a feature or request evidence;
- fixed negative copy is replaced by reflected upstream detail;
- an export strips the release, citation, temporal, or correction context that made the view inspectable.

The accessibility obligation follows the trust-bearing meaning of a surface. A decorative preview may have a smaller burden than a claim-bearing evidence panel, but no visual or generated carrier may hide the state required to interpret it safely.

> [!CAUTION]
> Accessibility evidence is not truth authority. A successful browser test, automated rule scan, or manual audit may show that a projection is operable; it does not prove that the evidence is authentic, policy-safe, reviewed, released, or published.

[Back to top](#top)

---

## 3. Doctrinal anchors

### Authority order for this document

| Question | Controlling evidence |
|---|---|
| Where does this file belong? | Accepted ADR-0029, adopted Directory Rules v2, and the existing `docs/architecture/ui/` lane |
| What exists now? | Current repository bytes, tests, workflows, and emitted artifacts tied to a known revision |
| What should the UI do? | Proposed architecture plus reviewed contracts, schemas, policy, implementation, and acceptance evidence |
| May content be shown? | Evidence, rights, sensitivity, policy, review, release, correction, and access state |
| Is the UI accessible? | A scoped conformance claim supported by representative automated and manual evidence—not this document |
| Is something released or published? | A governed release/publication transition—not a document, build, test, badge, or pull request |

### Placement basis

The existing target is placement-safe:

- `docs/` owns human-facing explanation;
- `docs/architecture/` owns cross-system architecture descriptions;
- `docs/architecture/ui/` is the existing UI architecture lane;
- changing this file in place does not create a new root or parallel authority.

### Current repository evidence

| Surface | Confirmed evidence | Boundary |
|---|---|---|
| Explorer package | Vite, TypeScript, Vitest, and Playwright scripts are declared | Tooling does not prove app-wide accessibility or deployment |
| Default entrypoint | Creates one `main` landmark labelled by the `h1` and mounts the baseline drawer | No map, route tree, live transport, auth, released data, or production composition |
| Baseline shell | Returns fixed `ABSTAIN / NO_GOVERNED_RESPONSE`; supplied input returns fixed `ERROR / UNSUPPORTED_BASELINE_INPUT` | Safe default only; not a complete response pipeline |
| Evidence Drawer resolver | Converts a strict local projection into `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`; uses fixed no-leak negative copy | Does not resolve evidence, execute policy, authorize review/release, or access lifecycle stores |
| Evidence Drawer DOM | Native buttons, named complementary landmark, heading, lists, links, `aria-live`, Escape dismissal, focus entry, and focus restoration | It is a non-modal complementary surface, not a complete dialog system or shell-wide focus model |
| Unit tests | Cover supported, stale, superseded, denied, error, malformed, contradictory, oversized, no-network, and no-direct-store behavior | Fixture proof only |
| Browser test | Covers Enter-to-open, focus on close, Escape-to-close, focus restoration, citations, history, and fixed no-leak negative states | One fixture surface, not all features or assistive technologies |
| `ui-build` workflow | Runs locked Explorer build and full package test script | CI signal only |
| `evidence-drawer-payload` workflow | Validates the closed schema, fixture polarity, focused tests, and generated receipt | Projection validation only; no upstream evidence/policy/release authenticity |
| `accessibility` workflow | Emits explicit `WORKFLOW_SKIPPED_EXPLICIT` and `WORKFLOW_HOLD` for axe and keyboard-navigation jobs | It checks nothing and must not be reported as an accessibility pass |
| Renderer decision | ADR-0007 remains proposed; the package and adapter are placeholders | No functional map or 3D accessibility claim is established |

### Corrected lineage

The prior v0.2 document treated an absent `docs/architecture/maplibre-3d.md` file and proposed renderer/3D object families as a current doctrinal anchor. This update removes that dependency and narrows 3D language to conditional future requirements. Any future terrain, globe, extrusion, point-cloud, animation, plugin, or custom-layer surface must establish its own accepted package boundary and accessibility evidence before this document can record it as current behavior.

[Back to top](#top)

---

## 4. The trust-visible state model

Accessibility applies to the meaning of KFM's finite states, not only their visual treatment.

### Current public projection vocabulary

The closed UI schema and current drawer use these top-level outcomes:

| Outcome | Accessible meaning | Current announcement behavior | Disclosure rule |
|---|---|---|---|
| `ANSWER` | Bounded supported projection is available | `polite` | Show title, summary, public-safe evidence refs, citations, limitations, and trust/history state |
| `ABSTAIN` | Support is missing, stale, superseded, unresolved, or otherwise insufficient | `polite` | Explain a bounded safe reason; do not manufacture a claim |
| `DENY` | Policy, rights, sensitivity, or access blocks disclosure | `polite` in the current drawer | Use fixed no-leak copy; omit evidence refs, citations, and protected history identifiers |
| `ERROR` | The projection, resolver, validator, service, or payload failed | `assertive` | Fail closed and suppress partial or diagnostic content |

Whether `DENY` should remain `polite` or graduate to an assertive announcement is **NEEDS VERIFICATION** through user research and assistive-technology testing. This document does not silently rewrite current implementation.

### Trust-state axes currently represented

The bounded drawer profile exposes text labels for:

- source role;
- policy outcome;
- review state;
- release state;
- freshness state;
- correction state;
- evidence references and citations where allowed;
- limitations;
- bounded negative history and correction lineage where allowed.

`STALE`, `HELD`, `SUPERSEDED`, `WITHDRAWN`, and `REVOKED` are reason/history conditions, not additional public response outcomes. UI copy, tests, filters, telemetry, and documentation must keep those layers distinct.

### Required projection pattern

Every claim-bearing state should provide, at the level appropriate to the surface:

1. a textual state label;
2. a stable accessible name or heading;
3. a bounded reason that does not leak protected details;
4. the evidence/citation relationship when disclosure is allowed;
5. time, freshness, review, release, and correction context where material;
6. an operable next step—inspect, retry, narrow scope, return, or request review—only when that action is actually available;
7. an announcement strategy that avoids both silence and repeated interruption.

### Color, icons, and badges

Color, iconography, shape, animation, and spatial position may reinforce state but may not carry it alone. Trust badges are projections of upstream state. They must not:

- imply acceptance, release, or publication that has not occurred;
- hide stale, denied, corrected, or withdrawn state;
- expose protected policy reason text;
- replace the underlying evidence/citation view;
- become the only accessible name of a control.

[Back to top](#top)

---

## 5. Keyboard, focus, and dialog discipline

### Confirmed bounded drawer behavior

The current Evidence Drawer:

- uses a native button to open;
- sets `aria-controls` and updates `aria-expanded`;
- exposes a named complementary landmark;
- moves focus to the native close button when opened;
- closes on the close button or `Escape`;
- restores focus to the prior connected element, falling back to the opener;
- destroys its listeners and DOM through an explicit cleanup function.

This is evidence for one non-modal drawer fixture. It does not prove complete shell navigation, focus visibility, focus containment, route transitions, multiple overlays, or assistive-technology parity.

### Architecture requirements

1. **Use native controls first.** Buttons, links, headings, lists, tables, inputs, and disclosure elements should carry their native semantics unless a reviewed custom pattern is necessary.
2. **Preserve logical order.** DOM order, reading order, keyboard order, and visual order must not diverge in a way that changes meaning.
3. **Keep focus visible.** Every operable element requires a visible focus indicator under supported themes and zoom levels.
4. **Move focus only for a reason.** Opening a drawer, modal, error summary, or route may move focus when the move reveals the requested context; background refreshes must not steal focus.
5. **Restore focus safely.** Dismissal should return focus to the invoking control or the nearest stable successor when the invoker no longer exists.
6. **Match semantics to behavior.** A non-modal complementary drawer should not claim dialog semantics. A true modal must define labelling, description, initial focus, containment, dismissal, inert background, and restoration.
7. **Do not require pointer precision.** Every consequential pointer action needs an equivalent keyboard path.
8. **Do not trap users.** Focus traps, nested overlays, and global shortcuts require representative tests and an escape route.
9. **Keep shortcuts discoverable and conflict-safe.** Single-key shortcuts should not activate unexpectedly in text-entry contexts.
10. **Announce completion and failure without loops.** Live regions must not re-announce unchanged content on every render.

### Shell-wide focus scenarios that remain unproven

- route and deep-link arrival;
- map-to-list and list-to-map selection transfer;
- Focus Mode request/response transitions;
- story-step navigation and cancellation;
- compare/export completion and error summaries;
- correction, withdrawal, or stale-state updates after a view is open;
- multiple simultaneous panels;
- authentication, authorization, or steward-review flows;
- map or future renderer controls.

[Back to top](#top)

---

## 6. Map alternatives (the non-map path)

KFM is map-first, not map-only. A map is a spatial carrier and interaction surface; it cannot be the sole path to consequential information.

### Required non-map parity

For every claim-bearing map interaction, the target architecture should provide a corresponding non-map route that supports the same public-safe scope:

| Map interaction | Non-map equivalent |
|---|---|
| Inspect a feature | Searchable/listed result with name, scope, time, trust state, and evidence action |
| Select a layer | Layer catalog control with textual state, description, availability, and limitations |
| Read a legend | Structured text or table describing classes, units, thresholds, unknown/no-data state, and representation limits |
| Change time | Keyboard-operable time control plus a textual current-time summary |
| Compare places or times | Structured comparison table or list preserving units, scope, evidence, and correction state |
| Open evidence | Direct Evidence Drawer control from the list/table result, not only from a map click |
| Understand extent | Textual geography description and safe identifiers; geometry alone is insufficient |
| Review stale/corrected state | Explicit history or status section independent of layer color/visibility |

### Map-selection boundary

A rendered pixel, feature property, hover state, or click is a **candidate selection**, not evidence. The accessible alternative must route through the same governed resolution boundary as the pointer path. It must not create a simplified client-only evidence shortcut.

### Current status

No functional map is composed by the default Explorer entrypoint. Non-map parity is therefore a target architecture requirement, not a confirmed map implementation. The current Evidence Drawer can be opened without a map, which is useful bounded evidence but not proof of complete map/list equivalence.

### Conditional future 3D or animated views

Any later 3D, terrain, globe, extrusion, point-cloud, synthetic, or reconstruction surface must provide:

- a 2D or structured non-map alternative carrying equivalent governed meaning;
- explicit representation and limitation text;
- keyboard-reachable controls;
- reduced-motion behavior;
- no dependence on free-orbit camera movement to understand the claim;
- accessible screenshots/exports with the same evidence and release context.

These are **PROPOSED admission requirements**, not proof that a renderer, plugin, 3D object family, or corresponding schema is accepted or implemented.

[Back to top](#top)

---

## 7. Motion, animation, and Story Node behavior

Motion can clarify time, change, and spatial relationships, but it must never be the only carrier of meaning or a required path through evidence.

### Target behavior

- honor the user's reduced-motion preference for decorative and navigational animation;
- provide pause, stop, skip, or step controls for non-trivial playback;
- preserve the same evidence, time, release, and correction state when animation is disabled;
- avoid automatic camera movement after focus enters an evidence or form control;
- do not use flashing, rapid pulsing, or repeated attention capture for trust state;
- announce story-step changes through stable headings/status text rather than motion alone;
- retain the current step and context when a user pauses or exits;
- allow a static list or outline of story steps;
- treat autoplay as opt-in unless a reviewed exception is supported by user evidence;
- keep loading indicators bounded and paired with textual status.

### Story and timeline requirements

A Story Node or timeline step should expose:

- step title and position;
- place and temporal scope;
- claim/interpretation type;
- evidence and citation action;
- limitations and representation notes;
- next, previous, pause/stop, and exit controls;
- correction or supersession state where material.

### Current status

Story playback, camera motion, map transitions, and reduced-motion behavior are not established by the default entrypoint. Sibling documents and feature directories are architecture or implementation evidence only where separately verified. This page does not promote them to completed behavior.

[Back to top](#top)

---

## 8. Perception, contrast, and zoom legibility

### Architecture requirements

1. **Text carries the state.** Color and iconography reinforce but do not replace labels such as `ABSTAIN`, `DENY`, `STALE`, `CORRECTED`, or `WITHDRAWN`.
2. **Contrast is measured.** Text, controls, focus indicators, charts, legends, and trust-state boundaries require measured contrast under supported themes; screenshots and badges are not evidence.
3. **Zoom and text resizing preserve meaning.** Content must reflow without hiding trust state, citations, error summaries, or controls.
4. **No-data is distinct from zero.** Missing, withheld, stale, and not-applicable states require separate text, not just empty space or a pale color.
5. **Patterns remain distinguishable.** Charts and map classes should use labels, patterns, line styles, or symbols in addition to hue.
6. **Focus and selection differ.** Keyboard focus, selected feature, hover, active route, and denied/restricted state must not collapse into one visual treatment.
7. **Typography remains readable.** Long evidence IDs and URLs must wrap or be shortened accessibly without forcing horizontal page scroll.
8. **High-contrast and forced-color modes are tested.** Custom styling must not erase native control boundaries or focus indicators.
9. **User settings do not hide governance.** Theme, density, or reduced-detail settings may simplify decoration but may not remove outcome, evidence, release, freshness, or correction meaning.

### Current status

The bounded entrypoint creates semantic text and native controls, but no comprehensive styling, contrast, reflow, text-resize, forced-color, or zoom evidence was verified for this update. Formal thresholds, supported theme matrix, and exception handling remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## 9. Alt text, popups, and the Evidence Drawer

### Evidence Drawer role

The Evidence Drawer is the current bounded accessibility proof surface. It is not the evidence authority itself. The current implementation projects:

- a title and finite outcome/reason code;
- a safe message;
- source-role, policy, review, release, freshness, and correction labels;
- public-safe evidence references where allowed;
- citation links where allowed;
- bounded history and correction lineage where allowed;
- limitations;
- fixed no-leak behavior for `DENY`, `ERROR`, and malformed payloads.

The paired UI contract and closed schema remain `PROPOSED` profiles. Their executable tests prove shape and projection behavior, not upstream authenticity or public release.

### Popup boundary

A popup, tooltip, toast, map label, or badge may provide a brief summary and an accessible name. It must not become a smaller parallel Evidence Drawer that:

- omits evidence/citation and limitation state;
- exposes protected reasons;
- presents stale or superseded evidence as current;
- makes a consequential claim from client-only feature properties;
- traps hover-only content away from keyboard and touch users.

A popup that implies a claim should provide an operable route to the governed evidence surface.

### Images, charts, maps, and screenshots

Text alternatives should communicate **purpose and governed meaning**, not reproduce every pixel. Depending on the artifact, that may require:

- a concise accessible name;
- a longer description or adjacent data table;
- place, time, units, source role, and representation limits;
- the release/correction state;
- evidence and citation references;
- an explanation of withheld, generalized, or unavailable detail;
- a statement that an image is illustrative, modeled, derived, or synthetic where material.

Decorative images should be marked decorative. Claim-bearing images and exported screenshots must not rely on filename, surrounding color, or visual realism as their only explanation.

### Current gaps

- no app-wide figure/chart/map alternative model is proven;
- no representative screen-reader matrix is recorded;
- no link-purpose audit across all feature directories is proven;
- no current screenshot/export manifest binding was verified;
- no automated rule-engine run is wired through the accessibility workflow.

[Back to top](#top)

---

## 10. Touch and narrow-viewport behavior

Accessibility applies to mobile and coarse-pointer operation even when desktop is the primary review surface.

### Target requirements

- controls remain operable without precision dragging or hover;
- adjacent controls have enough separation to avoid accidental activation;
- drawers and panels preserve headings, close controls, outcome, and trust state when space is constrained;
- content order remains logical when panels stack;
- horizontal scrolling is confined to data regions that genuinely require it and is described;
- long evidence references and citations wrap without covering controls;
- sticky headers, floating controls, and virtual keyboards do not obscure focused content;
- orientation changes preserve context and focus where practical;
- gestures have button or menu equivalents;
- time sliders, range controls, and map gestures expose keyboard and textual alternatives;
- safe-area and browser zoom behavior do not hide dismissal or recovery controls.

### Target-size policy

The repository does not establish one measured minimum target-size policy in the evidence inspected here. The project should choose, document, test, and version one policy rather than copying an unverified number into architecture prose. Exceptions must remain operable and reviewable.

### Current status

No representative narrow-viewport, touch, coarse-pointer, virtual-keyboard, or orientation evidence was verified for the default Explorer composition.

[Back to top](#top)

---

## 11. Accessibility smoke criteria (canonical)

> [!NOTE]
> The word **canonical** is retained in this heading only to preserve the legacy fragment identifier. This document is not a conformance authority. The table below separates confirmed bounded proof from proposed graduation evidence.

### Current executable proof

| Criterion | Current state | Evidence boundary |
|---|---|---|
| Native drawer opener and closer | **CONFIRMED** | One fixture-driven Evidence Drawer |
| Named `main` and complementary landmarks | **CONFIRMED** | Default entrypoint and drawer fixture only |
| Keyboard open with Enter | **CONFIRMED** | Playwright fixture test |
| Focus moves to close control | **CONFIRMED** | Playwright fixture test |
| Escape closes and restores focus | **CONFIRMED** | Playwright fixture test |
| Finite text outcome and reason code | **CONFIRMED** | Drawer projection profile only |
| Citation/history/limitation lists | **CONFIRMED** | Supported fixture and bounded history profile |
| Fixed no-leak `DENY` and `ERROR` copy | **CONFIRMED** | Synthetic canary tests only |
| Closed schema and fixture polarity | **CONFIRMED bounded lane** | Proposed UI projection profile; no upstream authenticity |
| App build and package tests | **CONFIRMED workflow surface** | CI signal only |
| Automated axe scan | **HOLD / not implemented** | Accessibility workflow explicitly skips |
| Full keyboard-navigation audit | **HOLD / not implemented** | Accessibility workflow explicitly skips |
| Whole-app focus order and visible focus | **UNKNOWN** | No representative completion evidence |
| Map/list parity | **HOLD / not applicable to current entrypoint** | No functioning map |
| Reduced-motion behavior | **UNKNOWN** | No representative animation/story runtime |
| Zoom, reflow, contrast, forced colors | **UNKNOWN** | No measured results verified |
| Screen-reader/browser/device matrix | **UNKNOWN** | No manual evidence package verified |
| WCAG 2.2 AA conformance | **UNKNOWN / not claimed** | Proposed target only |

### Graduation evidence for a claim-bearing UI slice

A slice should not be described as accessibility-complete until the applicable evidence set includes:

1. semantic structure and accessible-name review;
2. complete keyboard operation, focus visibility, and focus restoration tests;
3. finite outcome, stale/correction, and no-leak negative-state tests;
4. automated rule-engine results with reviewed exclusions;
5. manual keyboard review outside the scripted happy path;
6. representative screen-reader testing for supported browser/platform combinations;
7. zoom, text resize, reflow, high-contrast/forced-color, and reduced-motion checks;
8. pointer/touch and narrow-viewport checks where supported;
9. non-map equivalence for every consequential map-only action;
10. export continuity where the slice can export or capture claim-bearing material;
11. documented defects, exceptions, owner, due date, and rollback/disable path;
12. release-significance review that does not confuse a test pass with publication approval.

### Failure behavior

- missing required evidence produces `HOLD`, not a guessed pass;
- an unavailable automated tool does not waive manual review;
- a manual review does not waive deterministic regression tests;
- a green non-enforcing workflow is not an accessibility result;
- critical keyboard, focus, disclosure, or protected-detail failures block the affected public surface;
- rollback or feature disablement must remain available when a regression reaches a released surface.

[Back to top](#top)

---

## 12. Validation surfaces and CI hooks

### Repository-native focused commands

The following commands are present in current documentation or workflow configuration. Run the smallest applicable set from a repository checkout:

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  docs/architecture/ui/ACCESSIBILITY.md \
  --repo-root . \
  --profile required

pnpm --filter explorer-web build
pnpm --filter explorer-web test

python tools/validators/ui/validate_evidence_drawer_payload.py --fixtures
python -m unittest -q tests.validators.test_validate_evidence_drawer_payload
python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py
```

A documentation-only change should also receive the repository's configured metadata, stale-claim, link, anchor, document-graph, and docs-build checks when those workflows apply.

### Workflow truth table

| Workflow | What it currently does | What it does **not** prove |
|---|---|---|
| `ui-build` | Installs locked dependencies, builds Explorer, runs package unit/browser tests | Whole-app accessibility, policy, evidence authenticity, release, deployment, publication |
| `evidence-drawer-payload` | Validates proposed closed schema, fixtures, focused validator tests, and generated receipt | Live transport, upstream evidence resolution, policy execution, accountable review, public release |
| `accessibility` | Emits explicit HOLD summaries and warnings; executes no repository code | Axe results, keyboard/focus behavior, WCAG conformance, release readiness |

### Proposed accessibility workflow graduation

Replacing the HOLD scaffold requires a separate, reviewable implementation slice that establishes:

- a repository-owned command;
- deterministic public-safe fixtures;
- pinned dependencies and a defined browser setup;
- positive and negative cases;
- no secrets and no canonical/internal-store access;
- stable output and failure semantics;
- reviewed exclusions;
- accountable ownership;
- an emergency disable/rollback path;
- documentation that states the exact scope rather than “accessibility passed.”

### Evidence classification

| Result | Safe claim |
|---|---|
| Static source inspection | The named semantics exist in the inspected source |
| Unit test | The bounded resolver/view-model behavior passed its fixtures |
| Browser test | The scripted DOM interaction passed in the configured browser environment |
| Automated rules scan | The scanned page/state produced the recorded findings under the tool version and ruleset |
| Manual keyboard review | The reviewer completed the named scenarios on the named build |
| Assistive-technology review | The named AT/browser/platform combinations produced the recorded results |
| Conformance statement | Only the explicitly evaluated scope meets the declared standard/version and exception policy |

No lower row is implied by a higher-looking badge or workflow name.

[Back to top](#top)

---

## 13. Negative, abstain, deny, and stale states

Negative states carry accessibility and information-disclosure obligations at the same time.

### Current bounded behavior

| State | Current drawer behavior |
|---|---|
| No governed response | `ABSTAIN / NO_GOVERNED_RESPONSE`, polite live region, no evidence refs |
| Missing/stale/citation-unresolved support | `ABSTAIN` with fixed bounded reason; eligible public-safe evidence refs may remain visible |
| Policy/rights/sensitivity restriction | `DENY` with fixed no-leak copy; no evidence refs, citations, or protected history identifiers |
| Upstream or invalid payload | `ERROR` with assertive live region and fixed safe copy; no partial claim |
| Superseded evidence | `ABSTAIN`; history may remain visible but cannot support a current claim |
| Correction | Active answer may show bounded prior-to-active lineage and corrected trust state |

### Architecture requirements

- never render an empty map/panel as the only denial or error state;
- do not reflect upstream error text, prompt content, sensitive reasons, raw identifiers, or restricted coordinates;
- keep no-data, withheld, stale, loading, cancelled, and failed states distinct;
- provide a stable heading and recovery action where an action exists;
- avoid repeated assertive announcements during polling or retries;
- preserve history without presenting it as current support;
- make retry idempotent and prevent duplicate submissions;
- retain the user's safe context after a failure;
- do not visually hide denied content while leaving it in the accessibility tree;
- do not remove protected content from the accessibility tree while leaving it discoverable in DOM attributes, URLs, telemetry, or client state.

### State transitions

Future live transport must define and test transitions such as:

```text
idle -> loading -> ANSWER
               -> ABSTAIN
               -> DENY
               -> ERROR -> retry/cancel

ANSWER -> STALE/CORRECTED/WITHDRAWN notice -> governed refresh
```

Loading and cancellation are UI process states, not new truth outcomes. They must not overwrite the final governed response vocabulary.

[Back to top](#top)

---

## 14. Export and screenshot continuity

An export, screenshot, copied summary, printed view, or story capture is a downstream carrier. Accessibility and traceability must survive the transition away from the live UI.

### Target export obligations

Where material and policy-safe, an export should preserve:

- human-readable title and purpose;
- place and temporal scope;
- units and classification/legend meaning;
- outcome and trust state;
- evidence and citation references;
- release identifier and generated-at time;
- limitations and representation notes;
- stale, corrected, superseded, or withdrawn state;
- non-map table or textual equivalent for consequential graphics;
- accessible document structure appropriate to the format;
- public-safe redaction/generalization disclosures without protected details;
- correction or withdrawal locator.

### Screenshot boundary

A screenshot alone is not proof. Claim-bearing screenshots need adjacent or embedded context sufficient to identify the released view and inspect its evidence. Decorative screenshots need useful alt text or must be marked decorative. Photorealism, map precision, and visual polish must not be described as evidence quality.

### Current status

No production export, screenshot manifest, accessible generated-document pipeline, or correction propagation was verified for this update. [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md) remains the detailed architecture companion; implementation and release claims require separate evidence.

[Back to top](#top)

---

## 15. Anti-patterns

Do not:

- declare the application accessible because one component has keyboard tests;
- report the green accessibility HOLD scaffold as a pass;
- claim WCAG conformance from a build, unit test, automated scan, badge, or document;
- make map clicks, drag gestures, hover, color, or animation the only path to meaning;
- hide `ABSTAIN`, `DENY`, stale, corrected, or withdrawn state behind visual-only badges;
- place protected details in alt text, `aria-label`, hidden DOM, URLs, or live regions;
- reflect upstream denial/error messages into the browser;
- force focus movement during background refreshes;
- use `role="dialog"` without implementing dialog behavior;
- trap focus in a non-modal panel;
- disable zoom or text scaling to preserve layout;
- remove focus outlines without a tested replacement;
- autoplay story or camera motion without an operable alternative;
- make a 3D or animated view the only representation of a claim;
- treat an inaccessible denial as permission to reveal more detail;
- create a second accessibility schema, policy, checklist authority, or component package from this document;
- list nonexistent paths as implemented dependencies;
- turn a proposed renderer decision into an accessibility implementation claim;
- let exports strip evidence, release, temporal, limitation, or correction context;
- close an accessibility defect without exact-head regression evidence or a documented disposition.

[Back to top](#top)

---

## 16. Open questions and NEEDS VERIFICATION

### Decision backlog

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| A11Y-01 | What is the exact supported browser, operating-system, input, and assistive-technology matrix? | NEEDS VERIFICATION | Product support decision plus representative test evidence |
| A11Y-02 | Is WCAG 2.2 AA the accepted target, and what scope/exceptions process applies? | PROPOSED / NEEDS VERIFICATION | Accepted decision and conformance methodology |
| A11Y-03 | Who is accountable for accessibility architecture, implementation review, manual audit, and release disposition? | NEEDS VERIFICATION | Verified role assignments; do not invent names |
| A11Y-04 | Which automatic rule engine and pinned version should graduate the HOLD workflow? | NEEDS VERIFICATION | Dependency/supply-chain review, fixtures, command, tests, rollback |
| A11Y-05 | Which states require polite versus assertive announcements? | NEEDS VERIFICATION | User research and AT/browser testing; avoid interruption loops |
| A11Y-06 | What is the target-size and pointer-spacing policy? | NEEDS VERIFICATION | Accepted measurable policy and device tests |
| A11Y-07 | What constitutes non-map parity for layers, selections, legends, temporal controls, and compare views? | PROPOSED | One end-to-end map/list proof slice and contract boundary |
| A11Y-08 | What manual audit cadence and evidence-retention period apply? | NEEDS VERIFICATION | Governance/release decision and audit record format |
| A11Y-09 | How are accessibility defects prioritized against rights, sensitivity, evidence, and release failures? | NEEDS VERIFICATION | Shared severity and release-blocking policy |
| A11Y-10 | What is the accessible export/document format matrix? | UNKNOWN | Implemented export paths, format standards, and release tests |
| A11Y-11 | How should dynamic correction/withdrawal updates be announced without stealing focus? | PROPOSED | Live transport design and representative AT tests |
| A11Y-12 | Which proposed renderer/map surfaces will be admitted, and what accessibility evidence must accompany each? | HOLD | Accepted renderer/package decision and functioning runtime evidence |

### Graduation gates

The accessibility architecture may advance from **bounded component proof** to **subsystem evidence** only when:

1. exact scope and supported environment are named;
2. representative shell/routes and claim-bearing components exist;
3. automated and manual evidence cover the same exact build;
4. keyboard, focus, landmarks, names, state announcements, non-map parity, reflow, contrast, reduced motion, and negative-state disclosure are tested as applicable;
5. unresolved high-severity findings have an explicit HOLD, exception, or remediation decision;
6. policy/privacy review confirms accessibility surfaces do not leak protected detail;
7. release and rollback ownership is known;
8. the accessibility workflow executes real checks and no longer reports `WORKFLOW_HOLD`;
9. documentation names remaining limitations without implying conformance;
10. a correction path exists for a false or outdated accessibility claim.

### Smallest coherent next implementation slice

A bounded next slice is **not** to claim whole-app conformance. It is to replace one accessibility workflow HOLD with one deterministic, repository-owned check over the current public-safe Evidence Drawer browser fixture, while preserving:

- no secrets and read-only permissions;
- pinned dependencies;
- positive and negative states;
- keyboard/focus tests;
- fixed no-leak denial/error behavior;
- a reviewed exclusion mechanism;
- exact scope in the workflow summary;
- rollback to the prior HOLD scaffold if the new lane is unreliable.

That proposal remains separate from this documentation-only update.

[Back to top](#top)

---

## 17. Related docs

### Architecture lane

- [`README.md`](./README.md) — UI subsystem landing page and current maturity.
- [`BOUNDARIES.md`](./BOUNDARIES.md) — browser authority and forbidden operations.
- [`GOVERNED_SHELL.md`](./GOVERNED_SHELL.md) — persistent shell architecture.
- [`EVIDENCE_DRAWER.md`](./EVIDENCE_DRAWER.md) — evidence inspection architecture.
- [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) — governed Focus Mode flow.
- [`LAYERING.md`](./LAYERING.md) — layer catalog and trust-state architecture.
- [`MAP_RUNTIME_BOUNDARY.md`](./MAP_RUNTIME_BOUNDARY.md) — proposed renderer-neutral seam.
- [`STORY_PLAYER.md`](./STORY_PLAYER.md) — story playback architecture.
- [`COMPARE_AND_EXPORT.md`](./COMPARE_AND_EXPORT.md) — comparison and export continuity.
- [`TELEMETRY.md`](./TELEMETRY.md) — safe UI observability.
- [`TRUST_BADGES.md`](./TRUST_BADGES.md) — trust-state projection.
- [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) — lineage and redesign continuity.
- [`map-context-evidence-drawer-admission.md`](./map-context-evidence-drawer-admission.md) — map-context admission seam.

### Placement and decision records

- [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules v2 adoption.
- [`directory-rules.md`](../../doctrine/directory-rules.md) — adopted placement authority.
- [`ADR-0007`](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) — proposed renderer decision; not implementation authority.

### Current bounded implementation and proof

- [`apps/explorer-web/package.json`](../../../apps/explorer-web/package.json)
- [`apps/explorer-web/src/main.ts`](../../../apps/explorer-web/src/main.ts)
- [`apps/explorer-web/src/features/shell/index.tsx`](../../../apps/explorer-web/src/features/shell/index.tsx)
- [`apps/explorer-web/src/features/evidence_drawer/index.tsx`](../../../apps/explorer-web/src/features/evidence_drawer/index.tsx)
- [`apps/explorer-web/tests/evidence-drawer.test.ts`](../../../apps/explorer-web/tests/evidence-drawer.test.ts)
- [`apps/explorer-web/tests/browser/evidence-drawer.spec.ts`](../../../apps/explorer-web/tests/browser/evidence-drawer.spec.ts)
- [`contracts/ui/evidence_drawer_payload.md`](../../../contracts/ui/evidence_drawer_payload.md)
- [`schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`](../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json)
- [`fixtures/ui/evidence_drawer_payload/`](../../../fixtures/ui/evidence_drawer_payload/)
- [`tools/validators/ui/validate_evidence_drawer_payload.py`](../../../tools/validators/ui/validate_evidence_drawer_payload.py)
- [`tests/validators/test_validate_evidence_drawer_payload.py`](../../../tests/validators/test_validate_evidence_drawer_payload.py)
- [`tests/policy/test_explorer_web_adapter_boundary.py`](../../../tests/policy/test_explorer_web_adapter_boundary.py)

### Workflows

- [`accessibility.yml`](../../../.github/workflows/accessibility.yml) — explicit non-enforcing readiness HOLD.
- [`ui-build.yml`](../../../.github/workflows/ui-build.yml) — Explorer build and package tests.
- [`evidence-drawer-payload.yml`](../../../.github/workflows/evidence-drawer-payload.yml) — closed projection validation.

### Removed stale dependencies

The previous document linked to or treated these as current supporting authorities even though they were absent, case-mismatched, or unsupported by current evidence:

- `docs/architecture/maplibre-3d.md`;
- `schemas/contracts/v1/ui/EvidenceDrawerPayload.schema.json` (wrong case; the current file is lowercase);
- proposed 3D admission, plugin admission, reality-boundary, camera-path, and representation-receipt schemas as implemented accessibility dependencies;
- a completed retire-Cesium or sole-renderer transition;
- a functioning map/3D runtime.

Their removal from this page does not delete a repository object or decide their future disposition.

[Back to top](#top)

---

## Appendix A. No-loss modernization ledger

| Prior material | Disposition in v1.0-draft |
|---|---|
| Accessibility as governance | **RETAINED and grounded** in the current trust membrane |
| Finite outcomes | **RETAINED and corrected** to the actual closed profile: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Stale/restricted/corrected state | **RETAINED** as reason, trust, and history conditions rather than invented top-level outcomes |
| Keyboard/focus guidance | **RETAINED**, with current Evidence Drawer behavior separated from target shell behavior |
| Dialog guidance | **RETAINED and narrowed**; current drawer is non-modal complementary content, not a modal dialog |
| Non-map alternative | **RETAINED as PROPOSED architecture**; no functioning map parity is claimed |
| Reduced-motion/story guidance | **RETAINED as PROPOSED architecture**; no runtime behavior is claimed |
| Contrast, zoom, touch, and reflow | **RETAINED as requirements** with current evidence marked UNKNOWN |
| Evidence Drawer guidance | **EXPANDED and grounded** in code, schema, contract, fixtures, and tests |
| Negative-state safety | **EXPANDED and grounded** in fixed no-leak copy and canary tests |
| Smoke criteria | **PRESERVED through the legacy anchor**, split into current proof and graduation evidence |
| Validation | **REPLACED** with current repository-native commands and workflow truth boundaries |
| Export continuity | **RETAINED as PROPOSED architecture** and bounded by release/evidence context |
| 3D-specific controls and object families | **NARROWED to conditional future requirements** because renderer/3D authority and implementation are not established |
| `maplibre-3d.md` doctrinal dependency | **REMOVED** because the path is absent |
| Placeholder owners | **REPLACED** with the verified CODEOWNERS route and explicit unassigned-review gaps |
| “All repo paths proposed / implementation unknown” | **REPLACED** with a commit-pinned repository checkpoint and per-claim status |
| Existing section fragments | **PRESERVED** by retaining headings 1–17 and the historical top anchor |

[Back to top](#top)

---

## Appendix B. Rollback

This update changes documentation only.

Before merge, rollback is closing the draft pull request and deleting its feature branch. After an authorized merge, rollback is a normal reviewed revert of the documentation commit or restoration of prior blob `902f10807813152cfe8f59ec5e183c654a427cd7`.

Rollback requires no data migration, schema migration, policy change, package reinstall, runtime restart, cache invalidation, release withdrawal, or publication correction because this file does not change executable behavior or public release state.

A later implementation must define its own rollback. In particular, graduating the accessibility workflow from HOLD requires an explicit disable/revert path and must not erase prior findings or conformance limitations.

[Back to top](#top)
