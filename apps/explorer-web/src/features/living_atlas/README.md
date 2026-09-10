# Living Atlas composition

Status: implementation slice; public-safe site-local demonstration; no source admission, release, deployment, promotion, or publication authority.

This feature owns the Explorer-specific registries and serializable draft objects used by the map-first Living Atlas shell:

- 18 investigation views with explicit demo or design/data-hold states;
- 24 layer records with source, evidence, temporal, representation, scale, opacity, and warning fields;
- 15 repository-backed layer candidates whose available connector, declarative pipeline-specification, and contract lineage remains non-loadable and not admitted; the USGS earthquake entry records a README-only connector with unresolved canonical source identity and standalone-versus-USGS-family placement plus an inactive pipeline, without committing a source export to UI fixtures;
- four map-interaction controls with visible point-of-use state (Select available; Draw AOI, Measure, and Profile held) and ten links into the existing workbench catalog;
- official source-family candidates that remain distinct from admitted sources;
- multiscale temporal presets from deep time to the present operational window; committing a preset re-renders only exact-bucket or timeless fixture layers, disables out-of-time toggles/inspection, clears only incompatible selection/evidence, and preserves timeless or policy-denied context;
- `MapSnapshot`, `ReportDraft`, `StoryScene`, `PolicyDecision`, and visible trust-state types;
- strict persisted-draft parsing that rejects unknown or inconsistent fields and reads structurally valid v1 collections only when the corresponding v2 key is absent;
- a network-free inline MapLibre style containing only bounded synthetic/generalized geometry.

The renderer is downstream of these records. The inline style is an interaction fixture, not a Kansas factual dataset, and every mapped feature carries a fixture marker. External portals are ordinary links in Source Observatory; they are not fetched, scraped, or promoted by this feature.

Repository connection state is a bounded catalog-maturity label, not runtime availability, representation, review, release, or finite-response state. Those dimensions remain separate future contracts; the connection cards cannot load candidate data. Some candidates have no repository `pipeline_specs/` artifact, which is left visibly absent rather than invented. Connection-to-workbench references are reciprocal, inspecting a connection clears any prior runtime-layer selection and evidence references before a draft can be captured, and catalog search reveals the first matching rail panel instead of leaving matches hidden behind the current tab.

A design/data-held view is also an active fail-closed constraint. Selecting or inspecting a layer while such a view remains active produces `ABSTAIN / VIEW_DATA_HELD` with no eligible evidence references; a protected layer still produces `DENY` first. Report snapshots preserve the held view and selected layer identity for reproducibility but carry an empty evidence-reference set, so rendered availability cannot become evidence or release authority.

## Directory Rules basis

`apps/explorer-web/src/features/living_atlas/` is colocated with the independently deployable Explorer because this registry composes one application's public-safe views and drafts. Reusable renderer acquisition remains in `packages/maplibre/`. Canonical source, evidence, policy, schema, release, proof, receipt, and published-data authority remains in its existing governed root.

## Validation boundary

Unit tests check registry identity, source/layer/evidence closure, exact `pipeline_specs/` labeling, held-view abstention, denial precedence, temporal ordering and commit invariants, persisted-draft closure, finite Focus outcomes, repository-path locality, and the absence of external URLs in the inline style. Browser checks define local adapter construction, canvas visibility, view/layer/time interactions, incompatible-selection clearing, timeless-selection preservation, strict legacy-draft fallback, visible held controls, cross-panel catalog search, workbench handoff, held-view evidence exclusion from draft capture, and graceful finite failure. They do not establish source or renderer admission, public earthquake rendering, complete or current earthquake data, GPU parity, terrain, comparison, accessibility closure, performance, long-session stability, release, deployment, or publication.
