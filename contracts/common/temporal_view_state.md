<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-view-state
title: TemporalViewState Contract
type: semantic-contract; shared-state-successor; fixture-first
version: v1.0.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Contract steward · Temporal steward · Apps steward · Evidence steward · Release steward · Accessibility steward
created: 2026-09-05
updated: 2026-09-05
policy_label: public; contracts; common; temporal; shared-kernel; no-release-authority
responsibility_root: contracts/
related:
  - ./temporal_window.md
  - ../data/temporal_slice.md
  - ../governance/temporal_query_disclosure.md
  - ../governance/query_run_record.md
  - ../governance/evidence_resolution_record.md
  - ../../schemas/contracts/v1/common/temporal_view_state.schema.json
  - ../../fixtures/contracts/v1/common/temporal_view_state/
  - ../../tools/validators/validate_temporal_view_state.py
  - ../../tests/validators/test_validate_temporal_view_state.py
  - ../../packages/temporal/
  - ../../apps/explorer-web/src/features/temporal/
notes:
  - "Explicit successor for durable cross-surface temporal view state; it does not add fields to closed TemporalWindow."
  - "Query class/time basis reuse proposed TemporalQueryDisclosure vocabulary without resolving the separate TemporalWindow.time_kind conflict."
  - "The profile is a renderer-independent candidate contract and creates no authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TemporalViewState Contract

> `TemporalViewState` is the versioned, renderer-independent selection contract for a KFM temporal exploration. It keeps evidence time, knowledge/version time, and presentation time distinct while allowing Explorer, Sites, charts, Evidence Drawer, reports, workspaces, and AI handoff to refer to one committed frame context.

**Profile:** `kfm.temporal.view-state.v1`  
**Schema:** `schemas/contracts/v1/common/temporal_view_state.schema.json`  
**Validator:** `tools/validators/validate_temporal_view_state.py`  
**Fixtures:** `fixtures/contracts/v1/common/temporal_view_state/`  
**Status:** proposed / fixture-first / no-network / non-authoritative

## Why this is a successor

The existing `TemporalWindow` is a closed three-field value object: `start`, `end`, and its proposed `time_kind` vocabulary. `TemporalSlice` already owns derived, time-bounded spatial-view lineage. `TemporalQueryDisclosure` already owns fixture-only query classes and time bases. `QueryRunRecord` and `EvidenceResolutionRecord` already own bounded query/evidence process outcomes.

This profile composes those responsibilities instead of widening or translating them:

- it does not add fields to `TemporalWindow`;
- it does not replace `TemporalSlice`, `EvidenceBundle`, `QueryRunRecord`, `EvidenceResolutionRecord`, `ReleaseManifest`, `StoryManifest`, or `PublicWorkspaceContext`;
- it does not declare the unresolved `TemporalWindow.time_kind` enum canonical;
- it does not create a frame approval, source-admission, policy, release, or publication object.

The successor is explicit because the existing contracts are closed and no repository-wide durable view-state contract was found at the pinned base. Existing workspace links remain valid through an adapter; they are not silently reinterpreted.

## Three clocks

| Concern | State surface | Examples |
|---|---|---|
| Evidence time | `selection` and per-layer frame support | event, observation, validity interval, imagery acquisition, survey period |
| Knowledge/version time | `as_of` and `pins` | source issue, KFM recording, correction, release, withdrawal, knowledge cutoff |
| Presentation time | `display` and `presentation` | mode, step, speed, frame rate, duration, direction, loop, camera easing |

Playback never changes the evidence or knowledge clock. A cumulative display is not a valid-time, transaction-time, or prior-state query definition.

## Closed state shape

The schema is closed. The required members are:

| Member | Responsibility |
|---|---|
| `spatial_scope` | AOI/layer-native references and public-safe boundary; no raw protected geometry |
| `active_layer_ids` | governed layer identities, not source URLs or payloads |
| `query` | `TemporalQueryDisclosure` class/basis, interval/point semantics, and master-time rule |
| `selection` | typed raw temporal bounds with precision, source timezone, calendar, uncertainty, and conversion provenance |
| `display` | capability-selected Snapshot, Moving Window, Accumulation, Event Step, or Comparison semantics |
| `presentation` | playback settings separated from data time |
| `as_of` | knowledge cutoff, release reference, and current-policy-on-replay declaration |
| `pins` | dataset/release choices used for reproducible playback |
| `comparison` | independently selected A/B supports and compatibility posture |
| `representation` | stable analytical scale/unit/geometry and accessible-alternative policy |

Transient playback handles, request controllers, timers, workers, credentials, raw prompts, source URLs, and privileged options are not members of the profile. Unknown members fail closed.

## Temporal bounds and precision

A boundary preserves its original `raw` value, typed `profile` (`instant`, `date_only`, `month`, `year`, `uncertain_range`, or `geologic_age`), declared precision, source timezone, calendar, bound status, uncertainty, and normalization provenance.

Only a known, timezone-aware instant may carry `normalized`. Date-only, month/year, uncertain, and geologic values remain typed values; they are never fabricated as midnight JavaScript dates. An unknown timezone is an explicit bounded outcome, not an invitation to guess.

The new profile uses `HALF_OPEN` interval semantics when supported, with point-event behavior declared separately. This does not impose half-open semantics on the legacy `TemporalWindow` contract. Boundary conversions and calendar arithmetic remain versioned behavior.

## Display modes

- `SNAPSHOT` means an exact supported instant/interval, or a separately governed bounded-nearest result; the state never chooses a convenient date.
- `MOVING_WINDOW` means a fixed or editable duration with an explicit anchor and step rule.
- `ACCUMULATION` requires a declared aggregate: `EVENT_COUNT`, `UNIQUE_ENTITY_COUNT`, `INTEGRATED_QUANTITY`, or `CURRENT_STATE`. Identities are deduplicated; repeated station readings do not become additional stations.
- `EVENT_STEP` means previous/next available observation or state change, with `AVAILABLE_EVENT` stepping and a controlling-layer or master-time rule.
- `COMPARISON` means two independently resolved selections. Compatibility is explicit; units, methods, spatial support, geography versions, and temporal resolutions are not silently mixed.

Missing observations are not zero, and no measurement, categorical state, historical geometry, or unobserved path is interpolated by this profile. Any interpolation must be a named derived product with bounds, uncertainty, and provenance.

## Committed frame context

The implementation companion in `packages/temporal/` resolves a requested state into a committed frame context only after a governed resolver returns. It carries deterministic state/query identities, exact selected support, dataset and release references, per-layer actual support, finite availability, policy/release posture, and EvidenceBundle references without protected payloads.

Map, chart, legend, accessible feature table, Evidence Drawer, report preview, and AI handoff consume the same committed context. Requested/loading state remains separate from committed/displayed state. Cancellation and generation guards ensure a stale response cannot overwrite a newer selection.

A strict synchronized frame pauses or withholds a layer when required support is unavailable. It never keeps old pixels under a new date label and never presents a mixed-date frame as synchronized. Heterogeneous mode must show actual per-layer support and age.

## Compatibility and consumers

The first consumer adapter is `apps/explorer-web/src/site/workspace-context.ts`. It maps the existing public-safe `validAt`, `observedAt`, `asOf`, `releaseId`, layer IDs, place IDs, and compare mode into this profile without changing URL parsing or older workspace links. Missing/naive dates or unresolved A/B selections return bounded unsupported outcomes.

The existing Sites source path `apps/kansas-frontier-matrix-explorer/` and its local `temporal-comparison.ts` remain unchanged in this slice. Sites will consume the contract through conformance fixtures until its bound source repository can be edited and staged separately. No Site version or publication is implied by repository changes.

The profile is designed to be carried by existing governed APIs and evidence/release objects. It introduces no database, broker, universal transport, new renderer, or parallel release registry.

## Access, freshness, correction, and replay

Domain validity and freshness remain different dimensions. `CURRENT_POLICY` applies current withdrawal/access rules during historical replay; an old historical event is not stale merely because it is old, and recent retrieval does not make an old measurement current. `as_of` and `pins` are revalidated when a workspace/story/report is restored.

Correction and withdrawal use existing correction and release references. Ordinary playback remains pinned; newly available revisions are an explicit choice. Unsupported historical reconstruction stays disclosed as unsupported. Restricted data is excluded from payloads, caches, DOM, links, exports, histograms, comparison differences, and AI handoff.

## Validation and rollback

The JSON Schema, validator, fixtures, and focused tests are deterministic and no-network. A passing validator proves only closed shape, state identity, temporal precision/boundary rules, mode compatibility, and finite local outcomes. It does not resolve evidence, run policy, approve review, admit a source, promote a release, deploy a Site, or publish.

Rollback before merge is to close the draft PR and abandon the branch. After an authorized merge, revert the contract/schema/fixtures/validator/tests/package/Explorer-adapter/workflow changes together. Existing workspace links, TemporalSlice records, release references, and prior Site versions remain untouched.

## Evidence basis

- `contracts/common/temporal_window.md`: current closed shape and unresolved `time_kind` vocabulary.
- `contracts/governance/temporal_query_disclosure.md`: proposed fixture-only query classes and time bases.
- `contracts/data/temporal_slice.md`: existing derived-view lineage owner.
- `contracts/governance/query_run_record.md` and `evidence_resolution_record.md`: existing bounded process records.
- `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`: accepted placement authority through `docs/doctrine/directory-rules.md`.
- Supplied ArcGIS and MapLibre references: unique-event stepping, explicit visible span, separate playback duration, and keyframe/context labels are interaction inputs only; no ArcGIS runtime/data/dependency/licensing assumption is adopted.
- WCAG 2.2 SC 2.2.2: motion and auto-updating content require a user mechanism to pause, stop, hide, or control updates.

No claim in this profile establishes production temporal-engine, evidence, release, or Site readiness.