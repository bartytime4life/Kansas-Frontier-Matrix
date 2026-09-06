<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/ui/src
title: UI source tree README
type: package-src-readme
version: v0.3
status: draft
owners: OWNER_TBD — UI steward · Design-system steward · Evidence UI steward
created: 2026-06-15
updated: 2026-09-05
policy_label: internal
related:
  - ../README.md
  - ../../maplibre/README.md
  - ../../../apps/explorer-web/README.md
  - ../../../apps/governed-api/README.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/contract-schema-policy-split.md
tags: [kfm, ui, src, components, trust-visible-ui, evidence-drawer, focus-mode, design-system]
notes:
  - "v0.2 formatting pass: added README impact block, Shields badges, quick jumps, Mermaid boundary diagram, callouts, task list, and collapsible appendix."
  - "v0.3 adds the bounded Layer Library candidate; broader component and consumer maturity remains UNKNOWN."
  - "Source components render governed data; they do not decide truth, policy, evidence, release, or correction state."
[/KFM_META_BLOCK_V2] -->

<div align="center">

# UI Source Tree

`packages/ui/src/`

**Importable source home for shared KFM UI components, primitives, hooks, utilities, and trust-visible display patterns.**

![Status: experimental](https://img.shields.io/badge/status-experimental-orange)
![Owner: OWNER_TBD](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![Truth: needs verification](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)
![Boundary: governed props](https://img.shields.io/badge/boundary-governed__props-blue)

[Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Diagram](#diagram) · [Definition of done](#definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** experimental / `NEEDS VERIFICATION`  
> **Owners:** `OWNER_TBD` — UI steward · Design-system steward · Evidence UI steward  
> **Path:** `packages/ui/src/README.md`  
> **Repo fit:** importable source tree inside `packages/ui/`  
> **Truth posture:** CONFIRMED bounded Layer Library / PROPOSED source-tree contract / UNKNOWN broader implementation depth

> [!NOTE]
> This README defines the intended source-tree boundary for shared UI code. It does not prove that all folders, exports, tests, stories, or consuming app imports already exist.

## Layer Library candidate — 2026-09-05

The bounded implementation now consists of [the metadata/transaction model](layer-library-model.ts),
[the browser-native view](layer-library-view.ts), and [scoped styles](layer-library.css).
These are shared UI modules, not a renderer, policy engine, catalog authority,
network client or workspace-persistence service. The historical package-wide
checklist below is not upgraded to completed by this slice.

The Library supports staged discovery, cards/table, 24-item pages, search and
filters, explicit eligible/fixture/discovery modes, requested visibility/opacity,
constrained order, removal and conflict-aware undo. Unknown coverage/time is not
a positive match. A held renderer is labeled not drawn. No geometry or thumbnails
are fetched. Disclosure revocation removes old cards, category chips and staged
references; release withdrawal independently blocks addition. Explicitly allowed
metadata about an unavailable item is not the same as permission to deliver it.

Every mutation now checks the current requested state, requires an explicit
synchronous host acknowledgment and compares an immutable value snapshot with
readback. No-op, rejection, mismatched readback and exceptions are distinguished.
Unconfirmed writes are not announced as applied, do not create an undo receipt,
and are not automatically retried or rolled back. Errors after a host mutation
are not described as proof that nothing changed. Persistent host-read failures
disable mutation and show a finite, redacted message.

The [existing Site adapter and integration handoff](../../../apps/kansas-frontier-matrix-explorer/docs/earth-layer-library-integration.md)
remain **dormant**: this change does not import the wrapper into `page.tsx` or its
stylesheet into `layout.tsx`. The adapter covers eight inspected synthetic or
generalized fixtures only; no operational source is admitted. Other legacy layer
controls, MapLibre, temporal work, KanPlan, reports and workspaces remain unchanged.
The new acknowledgment callback is deliberately not compatible with the earlier
unapplied void-callback snippet. Use the updated handoff, not the original ZIP's
page-edit recipe. Actual React commit/paint and renderer delivery are separate
from requested-state acknowledgment and remain unverified.

From the repository root, the bounded source test is:

```bash
node --test apps/kansas-frontier-matrix-explorer/tests/earth-layer-library.test.mjs
```

Use lock-installed TypeScript. The runner checks its version against the app
manifest and lock and rejects implicit `NODE_PATH` fallback; installed-byte
integrity is not proved by that version check. `KFM_ALLOW_GLOBAL_TSC=1` is an
explicit **diagnostic-only** fallback with compiler identity in the log. The companion browser runner injects compiled modules
into Chromium with a synthetic host. The continuation run passed 47 Node cases
and 27 browser-DOM cases using Node 22.16.0, TypeScript 5.8.3 and Chromium
144.0.7559.96. The unchanged original candidate was also rerun: 37 Node cases and
21 browser cases passed. This is candidate-to-candidate evidence, not a same-base
repository-wide failure attribution. The app declares TypeScript 7.0.2; no locked
app build, native full validation, hosted CI, React runtime, GPU, Site preview or
production success is claimed. Wrapper checking is syntax-only.

Placement follows accepted ADR-0029 and adopted Directory Rules section 10.1 /
`DIR-EXEC-001`: shared UI in `packages/`, host composition and its existing tests
in `apps/`. The generated-work receipt is process memory under the existing
`data/receipts/generated/` lane, not approval or a release. No canonical schema,
policy, data catalog or other competing authority home is introduced.

Rollback this complete candidate change only after checking intervening work.
It does not require deleting any user workspace or clearing browser storage.
Keep current disclosure/access restrictions even when restoring older UI code.

## Scope

`packages/ui/src/` is the source-code tree for the shared UI package.

Code in this tree should help KFM apps render evidence, policy posture, release state, validation state, uncertainty, corrections, rollback visibility, and finite outcomes in a consistent way.

This tree is not a deployable application, not a data authority, not a MapLibre renderer, not a policy engine, and not a source connector.

<p align="right"><a href="#ui-source-tree">Back to top</a></p>

## Repo fit

| Relationship | Path | Status | Notes |
|---|---|---|---|
| Owning package | [`../README.md`](../README.md) | CONFIRMED adjacent README expected | Package-level boundary and package-facing overview |
| Renderer neighbor | [`../../maplibre/README.md`](../../maplibre/README.md) | NEEDS VERIFICATION | Map source, layer, style, and camera logic belongs there |
| Public explorer app | [`../../../apps/explorer-web/README.md`](../../../apps/explorer-web/README.md) | NEEDS VERIFICATION | Deployable app shell should consume this package, not live inside it |
| Governed API app | [`../../../apps/governed-api/README.md`](../../../apps/governed-api/README.md) | NEEDS VERIFICATION | Public payloads should be governed before reaching UI props |
| Directory doctrine | [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | NEEDS VERIFICATION | Placement authority; verify current repo path before relying on link |

## Inputs

Accepted inputs are component-ready, already-governed values passed through an app, fixture, story harness, or API client.

| Input family | Examples | Rendering responsibility |
|---|---|---|
| Evidence state | Evidence reference, EvidenceBundle summary, citation status | Show evidence support clearly |
| Policy state | Policy decision, sensitivity tier, redaction reason | Display denial, redaction, or staged-access posture |
| Release state | Release ID, publication status, rollback availability | Avoid implying unpublished material is released |
| Review state | Reviewer state, validation summary, open review note | Make review posture visible |
| Correction state | Correction notice, supersession label, withdrawal reason | Keep lineage visible after change |
| Finite outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `UNKNOWN`, `NEEDS VERIFICATION` | Render state as text, not color alone |

## Exclusions

| Does not belong here | Correct home |
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
| AI answer generation | governed AI runtime or service package |

> [!CAUTION]
> UI components must not become a shortcut around governed APIs, released artifacts, EvidenceBundle resolution, policy decisions, review state, or release state.

## Directory map

The three Layer Library modules above are the bounded candidate implementation. The following older layout remains a proposed placement guide, not a claim that those folders exist.

```text
src/
  components/     # shared visual building blocks
  evidence/       # evidence and citation display components
  policy/         # deny, redact, sensitivity, staged-access display
  release/        # release, rollback, correction, supersession display
  review/         # review and validation display helpers
  status/         # finite outcome and trust-state labels
  hooks/          # UI-only state helpers
  utils/          # label, accessible-name, and variant helpers
  types/          # UI prop types and component-local types
  index.ts        # package export surface, if TypeScript is confirmed
```

## Diagram

```mermaid
flowchart LR
    payload["Governed API or released artifact payload"] --> app["Deployable app boundary"]
    app --> props["Explicit component props"]
    props --> component["packages/ui/src component"]
    component --> ui["Trust-visible UI"]

    authority["Contracts, schemas, policy, release"] -. "inform payloads" .-> payload
    component -. "must not own" .-> authority
```

## Component contract

Components in this source tree should be designed around explicit props.

A component may render:

- evidence status
- source role
- citation validation state
- policy decision
- sensitivity tier
- release state
- review state
- correction state
- rollback availability
- finite outcome label
- explanatory message prepared by a governed layer

A component should not fetch, infer, or overwrite authority-bearing state on its own unless a future reviewed adapter boundary explicitly allows that behavior.

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

Source components should support:

- semantic HTML first
- keyboard navigation
- visible focus states
- accessible names for badges, buttons, panels, and drawers
- screen-reader-readable status changes
- labels that do not rely on color alone
- reduced-motion-safe behavior
- predictable drawer or modal focus handling

## Inspection path

The package manager, framework, and test runner remain `NEEDS VERIFICATION`. These commands are safe local inspection examples only.

```bash
# From the repository root, inspect the UI source tree.
find packages/ui/src -maxdepth 2 -type f | sort

# Inspect package metadata when present.
find packages/ui -maxdepth 2 \( -name package.json -o -name pyproject.toml -o -name tsconfig.json \) -print
```

## Testing expectations

Useful tests for this tree should cover:

- finite outcome rendering
- missing evidence behavior
- deny and abstain panels
- redaction notices
- correction banners
- release-state rendering
- keyboard navigation
- accessible names
- no color-only status communication
- synthetic fixture rendering for public, review, denied, abstained, and unknown states

## Definition of done

- [ ] Owners are confirmed and the `OWNER_TBD` placeholder is replaced.
- [ ] Actual source folders are inventoried and this README is updated from proposed layout to current layout.
- [ ] Package framework and export conventions are verified.
- [ ] Components render trust labels as visible text, not color alone.
- [ ] Missing evidence, policy, release, or correction state fails closed.
- [ ] Tests or synthetic examples cover denied, abstained, unknown, and needs-verification states.
- [ ] MapLibre renderer logic remains outside this source tree.
- [ ] Deployable app logic remains outside this source tree.
- [ ] Rollback path is known before public-facing component behavior changes.

## Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual UI framework and package manager | Prevents wrong quickstart or test commands |
| Confirm TypeScript / JavaScript / JSX / TSX convention | Prevents incorrect export examples |
| Confirm actual source folders and exports | Moves directory map from PROPOSED to CONFIRMED |
| Confirm test runner and accessibility tooling | Enables real validation commands |
| Confirm design-token source of truth | Prevents style drift |
| Confirm consuming app import paths | Keeps package/app boundary accurate |
| Confirm story or demo tooling | Determines where examples should live |

<details>
<summary>Appendix A — illustrative component examples</summary>

These examples are illustrative. They show intended component shape, not verified exports.

```tsx
<EvidenceStatusBadge
  status="NEEDS_VERIFICATION"
  label="Source rights not verified"
  detail="This layer cannot be promoted until source terms are reviewed."
/>
```

```tsx
<PolicyNotice
  decision="DENY"
  reason="sensitive_exact_location"
  message="Exact location is withheld by policy."
/>
```

```tsx
<ClaimCard
  title="County boundary claim"
  status="ABSTAIN"
  reason="missing_evidence_ref"
  message="This claim cannot be displayed as confirmed until evidence is resolved."
/>
```

</details>

<details>
<summary>Appendix B — no-loss preservation note</summary>

This formatting pass preserves the prior README substance: source-tree boundary, accepted inputs, exclusions, safety defaults, accessibility expectations, testing expectations, reviewer checklist, open verification items, and status summary.

The main changes are presentational and reviewability-focused: normalized meta block, impact block, badges, quick links, Mermaid diagram, callouts, definition-of-done task list, and collapsible appendix.

</details>

## Status summary

`packages/ui/src/` should remain the importable source tree for shared trust-visible KFM UI components.

It should make evidence, policy, release, correction, uncertainty, denial, and rollback state visible while preserving governed API boundaries and avoiding direct authority over truth, policy, publication, or source data.

<p align="right"><a href="#ui-source-tree">Back to top</a></p>
