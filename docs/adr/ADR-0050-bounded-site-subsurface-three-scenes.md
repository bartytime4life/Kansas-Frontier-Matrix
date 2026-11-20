<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0050
adr_id: ADR-0050
title: "ADR-0050 — Bounded Site subsurface Three.js scenes"
type: adr
version: v1.0
status: proposed
effective_decision_status: proposed
owners: ["@bartytime4life"]
owner_status: "Repository owner review route; independent architecture, Site, dependency and data-domain review remains required."
reviewers_required:
  - Architecture steward
  - Site subsystem owner
  - Dependency and security reviewer
  - Geology and hydrology data steward
  - Docs steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public
truth_posture: "PROPOSED scoped exception; existing implementation observed, not admitted by this document"
responsibility_root: docs/
owning_root: docs/
current_path: docs/adr/ADR-0050-bounded-site-subsurface-three-scenes.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c47f52e185bd1c6540801af8551c75cf12e6cbb6
related:
  - docs/adr/INDEX.md
  - docs/adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - apps/site/source/AGENTS.md
  - apps/site/source/app/subsurface-three.tsx
  - apps/site/source/app/aquifer-volume-view.tsx
  - apps/site/source/app/aquifer-volume-mesh.ts
  - apps/site/source/app/cutaway-model.ts
tags: [kfm, adr, proposed, site, subsurface, three, renderer-exception]
notes:
  - "No acceptance, dependency admission, runtime expansion, source activation, release, deployment or publication occurs in this packet."
[/KFM_META_BLOCK_V2] -->

# ADR-0050 — Bounded Site subsurface Three.js scenes

> **Proposed decision:** permit Three.js only for the preserved Site's two
> existing explanatory subsurface views, under a narrowly reviewed exception
> to ADR-0007. MapLibre remains the normal browser-map renderer family.

## 1. Status and authority

| Field | Current value |
|---|---|
| Source/effective status | `proposed` / `proposed`; not binding |
| Scope | Single-record lithology scene and applied-area aquifer/cutaway scene in the existing Site |
| Decision owner | `@bartytime4life`; named specialist review still pending |
| Implementation maturity | Source exists; exception acceptance and dependency/data/browser acceptance are separate |
| Governing decision | Accepted ADR-0007 §2.3 prohibits a peer renderer absent a separately accepted exception |
| Supersedes / superseded by | None; proposed additive exception, not replacement of ADR-0007 |
| Operational effect | None |

## 2. Evidence boundary

Repository source at `main@c47f52e185bd1c6540801af8551c75cf12e6cbb6` establishes:

| Source | Observation |
|---|---|
| [`Site manifest`](../../apps/site/source/package.json) and lockfile | Declares `three` 0.186.1 separately from `maplibre-gl` 6.9.0. Version presence is not dependency admission. |
| [`subsurface-three.tsx`](../../apps/site/source/app/subsurface-three.tsx) | Dynamically loads Three.js and OrbitControls to display a selected record's intervals, with its own renderer lifecycle. |
| [`aquifer-volume-view.tsx`](../../apps/site/source/app/aquifer-volume-view.tsx) | Dynamically loads the same modules for a bounded applied-area cutaway; uses a separate MapLibre locator/surface view. |
| [`aquifer-volume-mesh.ts`](../../apps/site/source/app/aquifer-volume-mesh.ts) and [`cutaway-model.ts`](../../apps/site/source/app/cutaway-model.ts) | Geometry/picking helpers contain Three.js types or receive its implementation. |
| [`subsurface-slice.test.mjs`](../../apps/site/source/tests/subsurface-slice.test.mjs), [`cutaway-render.test.mjs`](../../apps/site/source/tests/cutaway-render.test.mjs), [`aquifer-volume.test.mjs`](../../apps/site/source/tests/aquifer-volume.test.mjs) | Existing tests exercise bounded geometry, rendering lifecycle and record interactions. A test result cannot grant the exception. |

This review makes no current hosted-version, GPU support, physical accuracy,
source-admission, data-release or dependency-security acceptance claim.

## 3. Context

ADR-0007 explicitly names Three.js among peer renderers requiring a separately
accepted exception. The Site already has independent Three.js canvases. Its
MapLibre packaging exception in ADR-0006 §2.6 does not grant permission for them.
Omitting this distinction would make existing code look compliant by assertion.

The scenes serve a different presentation task from a map: showing a chosen
borehole interval stack or a source-bounded aquifer/cutaway. Review must preserve
that distinction and prevent an explanatory mesh becoming a measurement or a
second general-purpose map platform.

## 4. Proposed decision

If accepted, the exception would apply only to:

1. The existing record scene in `subsurface-three.tsx` and applied-area scene in
   `aquifer-volume-view.tsx`, with their geometry/picking helpers named above.
2. Local Three.js and OrbitControls imports from the Site's pinned dependency;
   no CDN/global loader, external scene plug-in or separate renderer package.
3. Source-backed intervals and bounded display geometry with explicit source,
   coverage, missing-data and vertical-exaggeration limitations. Never imply
   that interpolation, an envelope or missing coverage is a measured fact.
4. Selection flowing back to the existing record/evidence inspection path.
   The mesh, camera and renderer cannot decide source rights, evidence,
   sensitivity, policy, review, release, correction or publication.
5. Explicit initialization failure, context loss, resize/input cleanup, scene
   replacement and teardown. Keep MapLibre and accessible record/detail views
   available as the ordinary map and fallback presentation.

The exception would not cover a general globe, normal map replacement, peer
application, analytical/geological solver, new provider, arbitrary scene import,
or expansion to other apps. Any extension requires another reviewed decision.

## 5. Consequences and risks

The bounded explanatory scenes could be retained without replacing MapLibre as
the normal map family. Costs include a second GPU lifecycle, separate dependency
review, accessibility/fallback work and a continuing precision/uncertainty risk.
A scoped exception is preferable to describing the scenes as automatically
subordinate merely because their inputs came from the map.

## 6. Alternatives considered

| Option | Trade-off |
|---|---|
| Scoped exception for the two existing views | Selected proposal; preserves current explanatory work while making its boundaries and missing acceptance explicit. |
| Reimplement every scene as MapLibre custom layers | Could reduce independent renderer ownership; needs a proven interaction, depth, clipping and accessibility migration. No such migration is established here. |
| Keep only map and tabular/detail views | Simpler lifecycle and dependency posture; loses explanatory depth and cutaway interactions. Remains the fallback/retirement option. |
| Treat the Site MapLibre seam as blanket renderer permission | Rejected as a reading of ADR-0006; its exception names MapLibre acquisition paths only. |

## 7. Implementation, migration and compatibility

This proposal changes no runtime code or dependency. Before acceptance,
inventory exact runtime/type imports and source/data flows, record dependency
review, and decide the responsible scene owner. After acceptance, implement a
bounded import/ownership check and required lifecycle/fallback tests before any
new scene capability. Do not migrate source records or change storage bindings.
Retain the same-Site preservation boundary and review changes through successor
receipts. No schema, contract or policy migration is selected by this ADR.

## 8. Validation and acceptance

Proposal checks cover ADR identity/status coherence, exact local references and
the existing focused scene tests recorded in the review report. Hosted/browser,
provider, GPU matrix, long-session, screen-reader and data/domain acceptance are
not established by these checks.

Acceptance requires an explicit recorded decision on this scope; dependency and
security disposition; source/uncertainty review; accessible fallback and context
loss/teardown evidence; and an enforceable inventory for the permitted entrypoints.
An accepted ADR-0050 would be linked as a scoped exception in ADR-0007 without
marking ADR-0007 superseded. Until then, conformance remains unresolved.

## 9. Rollback, correction and supersession

Documentation rollback reverts the proposal, index/support updates and receipt
as one packet while retaining Git history. Runtime retirement, if separately
chosen, would remove/disable only these scene entrypoints and retain MapLibre,
record details, data and saved contexts through an explicit compatibility plan.
Do not perform that runtime change merely because this proposal is unaccepted.
No accepted decision is superseded here.

## 10. Security, rights, sensitivity and sovereignty

Scene inputs retain their source and record-level restrictions. Camera state,
picking, exported images, derived geometry and saved contexts must not bypass
redaction, precision, rights, sensitivity or audience controls. External imagery
and provider data remain subject to their existing admission/review process.
Not applicable: this packet performs no provider call, database write, source
migration or public export.

## 11. Open questions and verification backlog

- Accept, narrow or reject the exception with recorded owner/specialist review.
- Choose an enforceable ownership/import check without treating a type-only
  import as renderer construction or exempting unrelated runtime loaders.
- Verify context loss, resource cleanup, long sessions and fallback on actual
  supported devices; inspect uncertainty labels with a data-domain reviewer.
- Decide whether a proven MapLibre-only implementation should replace a scene.

## 12. Evidence and references

Accepted [ADR-0006](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md),
[ADR-0007](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>),
[ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md), Site source/tests
in §2, the [Site preservation record](../../apps/site/source/docs/SITE_PRESERVATION.md)
and the [ADR review](../reports/adr-review-2026-11-19.md) are repository evidence.
External references: not required for this repository-ownership proposal; no
external technical or legal conformance claim is made. Source lineage is the
pinned repository tree, not an external design document or an automated review.

## 13. Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-11-19 | Proposed bounded exception for the two existing Site subsurface scenes; no status or runtime transition. |
