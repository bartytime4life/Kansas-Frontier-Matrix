# UI Source Tree

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/ui/src
title: UI source tree README
type: package-src-readme
version: v0.1
status: draft
owners: <PLACEHOLDER — UI steward · Design-system steward · Evidence UI steward>
created: 2026-06-15
updated: 2026-06-15
policy_label: internal
related:
  - packages/ui/README.md
  - packages/maplibre/README.md
  - apps/explorer-web/README.md
  - apps/governed-api/README.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/contract-schema-policy-split.md
tags: [kfm, ui, src, components, trust-visible-ui, evidence-drawer, focus-mode, design-system]
notes:
  - "This README governs the source tree under packages/ui/src/."
  - "Implementation depth is UNKNOWN until actual exports, tests, build config, and consuming apps are inspected."
  - "Source components render governed data; they do not decide truth, policy, evidence, release, or correction state."
] -->

> Importable source home for shared KFM UI components, primitives, hooks, utilities, and trust-visible display patterns.

| Status | Source-tree role | Public data path |
|---|---|---|
| `DRAFT / NEEDS VERIFICATION` | Importable implementation source for the shared UI package | Governed API -> released artifact / EvidenceBundle-backed payload -> component props |

## At a glance

`packages/ui/src/` is the source-code tree for the shared UI package.

Code in this tree should help KFM apps render evidence, policy posture, release state, validation state, uncertainty, corrections, rollback visibility, and finite outcomes in a consistent way.

This tree is not a deployable application, not a data authority, not a MapLibre renderer, not a policy engine, and not a source connector.

## Boundary

| Field | Value |
|---|---|
| Path | `packages/ui/src/README.md` |
| Owning package | `packages/ui/` |
| Responsibility root | `packages/` — shared reusable implementation packages |
| Source-tree scope | UI components, hooks, primitives, design utilities, trust-state display helpers, and package exports |
| Public authority | None. Components render governed payloads; they do not decide truth, evidence, policy, release, or correction state |
| Normal public data path | Governed API or released artifact payload -> app boundary -> UI component props |

## What belongs here

| Area | Examples |
|---|---|
| Components | Badges, cards, drawers, banners, tables, panels, callouts |
| Evidence UI | Evidence status badges, citation state indicators, EvidenceBundle summary cards |
| Policy UI | Redaction notices, sensitivity labels, deny / abstain panels |
| Release UI | Release banners, rollback indicators, correction notices |
| Review UI | Review-state labels, reviewer notes, validation summaries |
| Finite outcome UI | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `UNKNOWN`, `NEEDS VERIFICATION` display components |
| Hooks | UI-only helpers for disclosure state, focus behavior, and local component state |
| Utilities | Formatting helpers for labels, status text, accessible names, and component variants |
| Types | UI prop types and component-local TypeScript types, where applicable |
| Package exports | Stable public exports for the shared UI package |

## What does not belong here

| Does not belong | Correct home |
|---|---|
| Deployable app routing and pages | `apps/` |
| Governed API services | `apps/governed-api/` or verified API package home |
| MapLibre source, layer, style, and camera code | `packages/maplibre/` |
| Canonical records or lifecycle data | `data/` lifecycle roots |
| Contract meaning | `contracts/` |
| Machine-readable schema authority | `schemas/contracts/v1/` |
| Policy decisions and rules | `policy/` |
| Release manifests and publication authority | `release/` |
| Source connectors | `connectors/` |
| AI answer generation | Governed AI runtime or service package |

## Expected source layout

The exact tree must be verified against implementation evidence. A safe target shape is:

```text
src/
  components/
  evidence/
  policy/
  release/
  review/
  status/
  hooks/
  utils/
  types/
  index.ts
```

Use this as a placement guide, not as proof the folders already exist.

## Component contract

Components in this source tree should be designed around explicit props. A component should receive already-governed data such as evidence status, source role, citation validation state, policy decision, sensitivity tier, release state, review state, correction state, rollback availability, finite outcome label, and explanatory message prepared by a governed layer.

A component should not fetch or infer authority-bearing state on its own unless the package has a clearly reviewed adapter boundary.

## Safety defaults

When trust-bearing props are missing, components should fail closed.

| Missing input | Safer display |
|---|---|
| Evidence reference | `ABSTAIN` / `Evidence pending` |
| Policy decision | Blocked or unavailable state for sensitive surfaces |
| Release state | Avoid displaying as public or released |
| Citation validation | Citation warning |
| Correction state | Avoid `current` label |
| Sensitivity tier | Conservative display |
| Finite outcome | `UNKNOWN` or explicit fallback |

## Accessibility expectations

Source components should support semantic HTML, keyboard navigation, visible focus states, accessible names, screen-reader-readable status changes, labels that do not rely on color alone, reduced-motion-safe behavior, and predictable drawer or modal focus handling.

## Testing expectations

Useful tests for this tree should cover finite outcome rendering, missing evidence behavior, deny and abstain panels, redaction notices, correction banners, release-state rendering, keyboard navigation, accessible names, no color-only status communication, and synthetic fixture rendering for public, review, denied, abstained, and unknown states.

## Reviewer checklist

A review is not complete until the reviewer can answer yes to these checks:

- Does the component render trust labels as visible text?
- Does it fail closed when evidence, policy, release, or correction state is missing?
- Does it avoid direct lifecycle data reads?
- Does it avoid treating AI text as authoritative?
- Does it preserve the MapLibre renderer boundary?
- Does it keep deployable app logic out of `packages/ui/src/`?
- Does it include tests or synthetic examples for denied, abstained, unknown, and needs-verification states?
- Can the change be rolled back without changing public truth semantics?

## Open verification items

- Confirm actual UI framework and package manager.
- Confirm whether this package uses TypeScript, JavaScript, JSX, TSX, or another source convention.
- Confirm actual export file names.
- Confirm existing source folders and component families.
- Confirm test runner and accessibility tooling.
- Confirm design-token source of truth.
- Confirm consuming app import paths.
- Confirm whether story or demo tooling exists.

## Status summary

`packages/ui/src/` should remain the importable source tree for shared trust-visible KFM UI components.

It should make evidence, policy, release, correction, uncertainty, denial, and rollback state visible while preserving governed API boundaries and avoiding direct authority over truth, policy, publication, or source data.
