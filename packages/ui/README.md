# UI Package

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/ui
title: UI package README
type: package-readme
version: v0.2
status: draft
owners: <PLACEHOLDER — UI steward · Design-system steward · Evidence UI steward>
created: 2026-06-15
updated: 2026-06-15
policy_label: internal
related:
  - apps/explorer-web/README.md
  - apps/governed-api/README.md
  - packages/maplibre/README.md
  - packages/temporal/README.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/contract-schema-policy-split.md
tags: [kfm, ui, components, trust-visible-ui, evidence-drawer, focus-mode, design-system]
notes:
  - "v0.2 polish pass: tightened navigation, added maintainer guidance, clarified component boundaries, and improved GitHub readability."
  - "Implementation depth is UNKNOWN until package files and downstream imports are inspected."
  - "This package is the shared UI component home, not the deployable app shell and not a truth source."
] -->

> Shared KFM UI components for trust-visible, evidence-aware, policy-aware application surfaces.

| Status | Package role | Public data path |
|---|---|---|
| `DRAFT / NEEDS VERIFICATION` | Shared component and design-system support | Governed API → released artifact / EvidenceBundle-backed payload → UI component |

## At a glance

`packages/ui` is the shared UI component package for KFM.

It should help deployable apps present evidence, policy posture, release state, validation state, uncertainty, corrections, and rollback visibility without duplicating UI logic across app surfaces.

This package is not a deployable application, not a truth store, not a policy engine, not a source connector, and not a renderer boundary. It renders governed data passed to it by apps, fixtures, or API clients.

## Quick navigation

- [Boundary](#boundary)
- [Repo fit](#repo-fit)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Trust membrane rule](#trust-membrane-rule)
- [Component posture](#component-posture)
- [Accepted inputs](#accepted-inputs)
- [Excluded inputs](#excluded-inputs)
- [Expected component families](#expected-component-families)
- [Trust-state display vocabulary](#trust-state-display-vocabulary)
- [Examples](#examples)
- [Accessibility expectations](#accessibility-expectations)
- [Testing expectations](#testing-expectations)
- [Open verification items](#open-verification-items)

## Boundary

| Field | Value |
|---|---|
| Path | `packages/ui/README.md` |
| Responsibility root | `packages/` — shared reusable implementation packages |
| Package scope | Shared UI components, UI primitives, trust-state display patterns, and design-system utilities |
| Current status | `DRAFT / NEEDS VERIFICATION` |
| Implementation evidence | `UNKNOWN` until package source, build config, tests, and consuming apps are inspected |
| Deployable app? | No. Deployable shells belong under `apps/` |
| Truth authority? | No. UI components render governed data; they do not decide truth, evidence, policy, or release state |
| Normal public data path | Governed API → released artifact / EvidenceBundle-backed payload → UI component |

## Repo fit

KFM separates deployable applications from shared packages.

| Concern | Home |
|---|---|
| Deployable public explorer shell | `apps/explorer-web/` |
| Governed API service | `apps/governed-api/` |
| Shared UI components | `packages/ui/` |
| MapLibre renderer wrapper and map-specific controls | `packages/maplibre/` |
| 3D / Cesium-specific renderer support, if used | `packages/cesium/` |
| Static styles or compatibility style roots | `styles/`, only if retained by repo convention |
| Legacy or compatibility UI roots | `ui/` / `web/`, only as compatibility roots when explicitly retained |

`packages/ui` should be imported by apps. It should not become a deployable app by itself.

## What belongs here

This package may contain shared components and utilities for:

| Area | Examples |
|---|---|
| Trust-visible UI primitives | Evidence badges, source-role badges, review-state badges |
| Finite outcome display | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` labels and panels |
| Evidence surfaces | Evidence summary cards, EvidenceBundle references, citation status indicators |
| Policy surfaces | Redaction notices, sensitivity labels, staged-access notices |
| Release surfaces | Release state tags, rollback links, correction banners |
| Validation surfaces | Warning blocks, validation result lists, fixture result panels |
| Layout primitives | Cards, panels, drawers, tabs, accordions, callouts |
| Accessibility helpers | Skip links, focus management, semantic status text |
| Form primitives | Search inputs, filters, toggles, disclosure controls |
| Non-map domain display | Claim cards, source cards, receipt cards, review cards |
| Design tokens | Shared spacing, typography hooks, semantic component variants |

## What does not belong here

| Does not belong | Correct home |
|---|---|
| Deployable application routing | `apps/explorer-web/`, `apps/review-console/`, or another app |
| Governed API implementation | `apps/governed-api/` |
| MapLibre runtime, sources, layers, camera, style control | `packages/maplibre/` |
| Canonical data stores | `data/` |
| Raw, work, quarantine, processed, catalog, triplet, or published data | `data/` lifecycle folders |
| Release decisions | `release/` |
| Policy rules | `policy/` |
| Contract meaning | `contracts/` |
| Machine-readable schema authority | `schemas/contracts/v1/` |
| AI answer generation | Governed AI runtime package or service |
| Direct source connectors | `connectors/` |

## Trust membrane rule

UI components must not normalize direct access to canonical or internal stores.

A public or normal UI surface must not read directly from:

```text
data/raw/
data/work/
data/quarantine/
data/processed/
unpublished candidates
canonical/internal stores
direct model runtime output
```

A UI component should receive already-governed props from an app, API client, fixture, or story harness.

## Component posture

Components in this package should be:

- evidence-aware
- policy-aware
- release-aware
- correction-aware
- accessible
- deterministic where practical
- easy to test with static fixtures
- safe by default when data is missing
- explicit when rendering `UNKNOWN`, `NEEDS VERIFICATION`, `ABSTAIN`, `DENY`, or `ERROR`

## Accepted inputs

Components may accept:

- governed API response payloads
- EvidenceBundle summary objects
- CitationValidationReport summaries
- PolicyDecision summaries
- ReleaseManifest summaries
- ReviewDecision summaries
- CorrectionNotice summaries
- Rollback target summaries
- layer metadata already cleared for display
- synthetic fixtures for tests and docs
- design tokens and semantic component props

## Excluded inputs

Components should not accept:

- raw connector records
- unreviewed model output as authoritative display text
- direct database rows from canonical stores
- unpublished candidate records except in explicitly labeled review/admin surfaces
- sensitive exact locations unless a policy-cleared payload says they are display-safe
- raw source documents without source-role, rights, and citation context
- mixed evidence/policy/release state in an unlabeled generic object

## Expected component families

Implementation may eventually include component families such as:

```text
components/
  badges/
  banners/
  cards/
  drawers/
  evidence/
  forms/
  layout/
  policy/
  release/
  review/
  status/
  tables/
  typography/
```

This tree is illustrative until actual source files are inspected.

## Trust-state display vocabulary

Use stable labels for trust-bearing state.

| State | UI intent |
|---|---|
| `CONFIRMED` | Verified from admissible evidence in the relevant context |
| `PROPOSED` | Design, recommendation, or candidate not proven as implemented |
| `UNKNOWN` | Not verified strongly enough |
| `NEEDS VERIFICATION` | Checkable before use, release, activation, or publication |
| `ABSTAIN` | System cannot answer or render authoritatively because support is insufficient |
| `DENY` | Policy blocks exposure or action |
| `ERROR` | Tool, data, validation, or runtime failure |
| `REDACTED` | Information withheld or generalized by policy |
| `SUPERSEDED` | Older material retained but no longer current |
| `WITHDRAWN` | Prior release or claim removed from active public use |

## Examples

### Evidence-aware component

Illustrative API shape:

```tsx
<EvidenceStatusBadge
  status="NEEDS_VERIFICATION"
  label="Source rights not verified"
  detail="This layer cannot be promoted until source terms are reviewed."
/>
```

### Policy-aware component

Illustrative API shape:

```tsx
<PolicyNotice
  decision="DENY"
  reason="sensitive_exact_location"
  message="Exact location is withheld by policy."
/>
```

### Release-aware component

Illustrative API shape:

```tsx
<ReleaseBanner
  releaseId="release-2026-06-example"
  state="published"
  corrected={false}
  rollbackAvailable={true}
/>
```

### Fail-closed missing-evidence state

Illustrative API shape:

```tsx
<ClaimCard
  title="County boundary claim"
  status="ABSTAIN"
  reason="missing_evidence_ref"
  message="This claim cannot be displayed as confirmed until evidence is resolved."
/>
```

## Accessibility expectations

Shared UI components should support:

- semantic HTML first
- keyboard navigation
- visible focus states
- screen-reader-readable status changes
- sufficient color contrast
- labels that do not rely on color alone
- reduced-motion-safe behavior
- predictable drawer and modal focus handling
- testable accessible names

## Styling expectations

This package should avoid hard-coding truth semantics into color alone.

Preferred pattern:

- semantic variant
- accessible label
- optional icon
- visible text
- tooltip or detail text only as an enhancement

Example:

```tsx
<StatusBadge variant="warning" label="NEEDS VERIFICATION" />
```

The label is the authority-bearing part. Color only reinforces it.

## Public UI safety rules

A component should fail safely when trust-bearing props are missing.

| Missing input | Safer behavior |
|---|---|
| Missing evidence reference | Render `ABSTAIN` or `Evidence pending`, not a confident claim |
| Missing policy decision | Render blocked / unavailable state for sensitive surfaces |
| Missing release state | Avoid showing as public/released |
| Missing citation status | Render citation warning |
| Missing correction state | Avoid “current” label |
| Missing sensitivity tier | Use conservative display |

## Relationship to Focus Mode

`packages/ui` may provide reusable display pieces for Focus Mode, such as:

- prompt boundary panels
- evidence summaries
- answer status cards
- citation validation warnings
- policy denial messages
- source coverage summaries
- correction and rollback notices

It should not generate Focus Mode answers. It should render governed answer envelopes supplied by the appropriate runtime or API layer.

## Relationship to Evidence Drawer

`packages/ui` may provide generic Evidence Drawer components.

The drawer should make it easy to inspect:

- evidence summary
- source role
- citation state
- policy decision
- review state
- release state
- correction state
- rollback target
- uncertainty or limitations

The drawer should not fetch ungoverned source material directly.

## Relationship to MapLibre

Map-specific source/layer/style/camera behavior belongs in `packages/maplibre/`.

`packages/ui` may provide generic UI wrappers used near a map, such as panels, legend containers, toggles, badges, and drawers. It should not become the renderer boundary.

## Testing expectations

Useful tests for this package should cover:

- rendering of all finite outcome labels
- missing evidence behavior
- missing policy behavior
- redaction notice rendering
- correction banner rendering
- release-state rendering
- keyboard navigation for drawers and modals
- accessible names for badges and status components
- no color-only status communication
- fixture rendering for public, review, and denied states

## Fixture expectations

Fixtures should be synthetic unless explicitly approved.

Preferred fixture classes:

```text
fixtures/
  evidence-summary.answer.json
  evidence-summary.abstain.json
  policy-decision.deny.json
  release-banner.published.json
  correction-notice.superseded.json
  focus-mode.error.json
```

Fixture paths are illustrative until repo conventions are inspected.

## Maintenance checklist

Before changing this package, verify:

- components do not bypass governed API boundaries
- components do not read lifecycle data directly
- trust-state labels remain consistent with contracts
- sensitive states fail closed
- accessibility tests still pass
- story/demo fixtures are clearly synthetic
- public-facing examples do not imply unsupported implementation maturity
- map-specific logic stays in the renderer package
- deployable app logic stays in `apps/`

## Safe change pattern

1. Add or update component contract notes.
2. Add synthetic fixtures.
3. Add or update component tests.
4. Add visual/story examples if the repo supports them.
5. Update consuming apps after component behavior is stable.
6. Document any breaking prop changes.
7. Keep rollback simple by avoiding broad component rewrites when a smaller change works.

## Reviewer checklist

A review is not complete until the reviewer can answer yes to these checks:

- Does the component render trust labels as visible text, not color alone?
- Does it fail closed when evidence, policy, release, or correction state is missing?
- Does it avoid reading lifecycle data directly?
- Does it avoid generating or treating AI text as authoritative?
- Does it preserve the MapLibre/package boundary?
- Does it include synthetic fixtures or tests for denied, abstained, and unknown states?
- Can consuming apps roll back the component change cleanly?

## Open verification items

- Confirm actual package manager.
- Confirm actual component framework.
- Confirm whether Storybook, Ladle, Playwright, Vitest, Jest, or another tool is used.
- Confirm actual package exports.
- Confirm existing component directory names.
- Confirm consuming apps and import paths.
- Confirm design-token source of truth.
- Confirm whether `ui/`, `web/`, `styles/`, or `viewer_templates/` are compatibility roots in the current repo.
- Confirm whether accessibility checks exist in CI.

## Status summary

`packages/ui` should be the shared UI component home for KFM trust-visible interfaces.

It should make evidence, policy, release, correction, uncertainty, and denial visible without becoming a truth store, policy engine, map renderer, deployable shell, source connector, or public bypass around governed APIs.
