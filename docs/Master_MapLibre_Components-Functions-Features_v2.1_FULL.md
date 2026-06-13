<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-master-maplibre-components-functions-features-v2-1-full
title: Master MapLibre Components, Functions, and Features
type: architecture_reference
version: v2.1
status: draft
owners: <PLACEHOLDER — Docs steward · Map steward · UI steward · Governed API steward · Evidence steward>
created: 2026-05-10
updated: 2026-06-12
policy_label: public
authority_class: synthesis / architecture reference; NOT canonical doctrine
requested_path: docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md
owning_root: docs/
directory_rules_basis: docs/ owns human-readable architecture, doctrine, reports, and implementation references. This file explains MapLibre architecture to humans and does not define machine schema, policy, release state, or runtime code.
truth_posture: cite-or-abstain with explicit truth labels
implementation_boundary: repository topology, package versions, route names, component names, workflows, dashboards, release manifests, and runtime behavior remain NEEDS VERIFICATION unless checked in the mounted repo.
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/architecture/map-shell.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/architecture/repository-structure-guiding-document.md
  - docs/sources/catalog/README.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - apps/explorer-web/
  - apps/governed-api/
  - packages/ui/
  - packages/maplibre/
  - data/registry/layers/
  - data/published/layers/
  - data/published/pmtiles/
  - release/
tags:
  - kfm
  - maplibre
  - map-shell
  - governed-ui
  - evidence-drawer
  - focus-mode
  - pmtiles
  - mvt
  - cog
  - tiles
  - layer-manifest
  - release-manifest
  - governed-api
  - trust-membrane
  - accessibility
  - validation
  - rollback
notes:
  - "v2.1 — Markdown working edition prepared for repository use from the cumulative MapLibre architecture packet and KFM doctrine."
  - "The filename uses v2.1 because this is the requested target. The current-session source packet directly available here is earlier cumulative MapLibre evidence; current repo presence of a prior v2.1 file remains NEEDS VERIFICATION."
  - "This document is a reference surface. Contracts, schemas, policies, manifests, receipts, and runtime code remain authoritative in their own responsibility roots."
] -->

# Master MapLibre Components, Functions, and Features

> **Kansas Frontier Matrix map architecture reference**
> **Version:** v2.1 draft working Markdown
> **Requested path:** `docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`
> **Authority:** Architecture reference / synthesis, not canonical doctrine
> **Core rule:** MapLibre renders governed truth; it does not create or authorize truth.

---

## 0. Reader note

This document is the master MapLibre architecture reference for KFM’s public and review-facing map surfaces.

It defines how MapLibre, tiles, layer manifests, Evidence Drawer payloads, Focus Mode, Story Nodes, terrain/3D views, style JSON, PMTiles, COGs, MVT layers, and related UI features should behave inside the KFM trust membrane.

It does **not** define canonical object semantics, machine schemas, policy decisions, release decisions, or implementation status. Those belong in their own responsibility roots:

| Concern                                 | Canonical responsibility root    |
| --------------------------------------- | -------------------------------- |
| Human-readable architecture             | `docs/`                          |
| Object meaning                          | `contracts/`                     |
| Machine shape                           | `schemas/`                       |
| Allow / deny / restrict / abstain logic | `policy/`                        |
| Deployable web shell                    | `apps/explorer-web/`             |
| Governed public API                     | `apps/governed-api/`             |
| Shared UI components                    | `packages/ui/`                   |
| MapLibre runtime package                | `packages/maplibre/`             |
| Layer registry                          | `data/registry/layers/`          |
| Published layers / PMTiles / COGs       | `data/published/`                |
| Proofs and receipts                     | `data/proofs/`, `data/receipts/` |
| Release manifests, rollback, correction | `release/`                       |

---

## 1. Executive determination

**CONFIRMED — MapLibre is a disciplined renderer and interaction runtime inside KFM.**

MapLibre is not the truth store, source registry, policy engine, citation authority, review authority, release authority, or AI authority.

**CONFIRMED — Public map surfaces must read through governed interfaces.**

The ordinary public path is:

```text
Released artifact / catalog / evidence
  → governed API
  → policy-safe runtime envelope
  → MapLibre layer / interaction
  → Evidence Drawer / Focus Mode / export
```

Public clients must not directly read:

```text
data/raw/
data/work/
data/quarantine/
unpublished candidates
canonical internal stores
direct model-provider output
unreviewed generated artifacts
sensitive exact geometry
```

**CONFIRMED — rendered map artifacts are downstream carriers.**

The following are carriers, not root truth:

* MapLibre sources
* style JSON
* layer toggles
* PMTiles
* MVT
* COGs
* MBTiles
* GeoJSON previews
* screenshots
* exports
* Story Nodes
* graph projections
* 3D scenes
* AI answers
* popups
* hover cards

**PROPOSED — v2.1 should act as the maintainable Markdown edition of the MapLibre master.**

This file should replace oversized PDF-only map architecture packets as the repository-facing, reviewable, diffable architecture reference. It should preserve the earlier master packet’s operating law while making the implementation backlog easier to inspect.

---

## 2. Truth labels

| Label                  | Meaning                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **CONFIRMED**          | Verified from available doctrine, supplied artifacts, generated artifacts, or directly inspected evidence in the session that made the claim. |
| **PROPOSED**           | A recommended design, path, test, component, schema, workflow, or implementation step not verified as implemented.                            |
| **NEEDS VERIFICATION** | Checkable before operational use, but not checked strongly enough here.                                                                       |
| **UNKNOWN**            | Not established from the available evidence.                                                                                                  |
| **CONFLICTED**         | Sources or conventions disagree; preserve the conflict and route it to drift/ADR handling.                                                    |
| **DENY**               | Policy blocks the action or exposure.                                                                                                         |
| **ABSTAIN**            | Evidence is insufficient or unsafe to support the claim.                                                                                      |
| **ERROR**              | System, validation, integrity, runtime, or dependency failure.                                                                                |

---

## 3. Placement and authority posture

### 3.1 File placement

**Requested path:** `docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`

**Placement status:** **PROPOSED / reasonable**

The file explains architecture to humans, so it belongs under `docs/`.

### 3.2 Naming note

The requested filename uses uppercase words, underscores, and `v2.1_FULL`.

That is acceptable as a requested compatibility filename. For long-term repo hygiene, maintainers may later choose a lowercase hyphenated mirror or successor path such as:

```text
docs/architecture/master-maplibre-components-functions-features.md
```

Do not rename automatically without checking current repo references.

### 3.3 Authority limit

This file may describe target homes such as `apps/explorer-web/`, `packages/maplibre/`, and `data/registry/layers/`, but path existence and implementation status remain **NEEDS VERIFICATION** until checked in a mounted repo.

---

## 4. KFM map operating law

### 4.1 Renderer boundary

MapLibre may:

* render released layers
* manage map interactions
* show visible layer state
* send click/hover/time/filter context to the governed API
* display returned Evidence Drawer payloads
* display finite negative states
* support public-safe previews
* support review-console previews when explicitly scoped
* export released, citation-bearing outputs

MapLibre must not:

* decide truth
* publish a layer
* bypass policy
* read RAW/WORK/QUARANTINE
* call model providers directly
* hide sensitive geometry only by style
* treat popups as evidence
* treat screenshots as proof
* treat layer toggles as release state
* expose exact restricted coordinates
* silently render stale or unverified artifacts

### 4.2 Trust membrane

The map shell must treat every layer, source, style, plugin, export, and Focus Mode answer as governed material.

A map feature is only a selection candidate until it resolves to evidence.

```text
map click
  → feature candidate
  → governed API lookup
  → EvidenceRef resolution
  → EvidenceBundle / PolicyDecision / release check
  → EvidenceDrawerPayload
  → answer, abstain, deny, or error
```

### 4.3 Lifecycle alignment

The public map must only use material that has passed the KFM lifecycle:

```text
RAW
  → WORK / QUARANTINE
  → PROCESSED
  → CATALOG / TRIPLET
  → PUBLISHED
```

Publication is a governed state transition, not a layer toggle.

---

## 5. System architecture at a glance

```text
SourceDescriptor / source ledger
        │
        ▼
RAW capture
        │
        ▼
WORK transform / validation ──► QUARANTINE
        │
        ▼
PROCESSED candidates
        │
        ▼
CATALOG / TRIPLET / EvidenceBundle
        │
        ▼
PolicyDecision + ValidationReport + ReleaseManifest
        │
        ▼
Published layer artifact
        │
        ├── PMTiles / MVT
        ├── COG / raster
        ├── GeoParquet
        ├── style JSON
        ├── LayerManifest
        └── TileArtifactManifest
        │
        ▼
apps/governed-api/
        │
        ▼
apps/explorer-web/ + packages/maplibre/
        │
        ├── Map canvas
        ├── Layer manager
        ├── Timeline
        ├── Evidence Drawer
        ├── Focus Mode
        ├── Story Nodes
        └── Export surface
```

---

## 6. Required map object families

| Object family              | Map role                                                                                                    | Authority note                               |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `SourceDescriptor`         | Defines source identity, role, rights, sensitivity, cadence, and admission posture.                         | Source admission, not rendering.             |
| `EvidenceBundle`           | Holds evidence closure for claims shown through map UI.                                                     | Outranks generated UI text.                  |
| `EvidenceRef`              | Public-safe reference used by features, drawer payloads, citations, and Focus Mode.                         | Must resolve or abstain.                     |
| `LayerManifest`            | Declares layer identity, source artifact, style binding, evidence binding, policy class, and release state. | Required before public map loading.          |
| `TileArtifactManifest`     | Declares tile/raster artifact digests, build inputs, tool versions, and validation results.                 | Required for PMTiles/MVT/COG trust.          |
| `MapReleaseManifest`       | Release closure for a map/layer bundle.                                                                     | Public state anchor.                         |
| `PolicyDecision`           | Records whether a layer, field, geometry, or action is allowed, denied, restricted, or generalized.         | Must be respected before render.             |
| `PromotionDecision`        | Records publish/hold/deny decision at release gate.                                                         | Layer toggle cannot substitute.              |
| `ValidationReport`         | Records schema, artifact, source-layer, style, tile, or accessibility validation.                           | Testable gate.                               |
| `CitationValidationReport` | Records whether visible claims resolve to evidence.                                                         | Required for Focus Mode and exports.         |
| `RedactionReceipt`         | Records sensitive geometry/field redaction or generalization.                                               | Required for sensitive map outputs.          |
| `TransformReceipt`         | Records conversion from source data to layer artifact.                                                      | Required for reproducibility.                |
| `RunReceipt`               | Records pipeline/tool run inputs, outputs, versions, hashes, and policy context.                            | Required for auditability.                   |
| `RollbackCard`             | Defines rollback/repointing path for map releases.                                                          | Required before release.                     |
| `CorrectionNotice`         | Records public correction, withdrawal, or supersession.                                                     | Required for trust-visible changes.          |
| `EvidenceDrawerPayload`    | UI payload returned for clicked/selected evidence.                                                          | Drawer is a projection, not evidence itself. |
| `MapContextEnvelope`       | Carries map click, viewport, time, filters, layer state, and user context to governed API.                  | Must avoid raw/canonical leakage.            |
| `RuntimeResponseEnvelope`  | Finite API/AI response: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`.                                               | Prevents fluent unsupported answers.         |

---

## 7. Component families

### 7.1 Map shell

| Component        | Purpose                                                           | Required behavior                                    |
| ---------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| `MapShell`       | Owns map canvas and global map state.                             | Never bypasses governed API.                         |
| `MapProvider`    | Initializes MapLibre instance and lifecycle.                      | Verifies style/source config before load.            |
| `ViewportState`  | Tracks center, zoom, bearing, pitch, bounds.                      | May be included in `MapContextEnvelope`.             |
| `TimeState`      | Tracks time slider, valid-time, release-time, comparison windows. | Must preserve time semantics.                        |
| `LayerState`     | Tracks visible layers, opacity, filters, legend state.            | Layer visibility is not publication.                 |
| `SelectionState` | Tracks clicked/hovered features.                                  | Selection is candidate only until evidence resolves. |
| `PolicyState`    | Tracks denied/restricted/abstain/error states.                    | Negative states must be visible.                     |
| `ReleaseState`   | Tracks current release, stale release, rollback, supersession.    | Must not silently show stale material.               |
| `EvidenceState`  | Tracks active Evidence Drawer payload.                            | Must clear or abstain on unresolved evidence.        |

### 7.2 Source and layer components

| Component               | Purpose                                             | Required behavior                                               |
| ----------------------- | --------------------------------------------------- | --------------------------------------------------------------- |
| `LayerCatalogPanel`     | Lists available released or preview-scoped layers.  | Shows release, policy, and evidence posture.                    |
| `LayerManager`          | Toggles and orders layers.                          | Does not imply publish/unpublish.                               |
| `LayerManifestResolver` | Fetches layer manifest metadata.                    | Must fail closed if missing or invalid.                         |
| `SourceVerifier`        | Checks tile/source/style sidecars before addSource. | Must deny or fallback on hash/signature mismatch.               |
| `StyleRegistry`         | Manages approved style JSON references.             | Prevents style drift.                                           |
| `LegendPanel`           | Shows style meaning and classification.             | Must reflect source time, uncertainty, and policy where needed. |
| `AttributionPanel`      | Shows source rights and required attribution.       | Missing attribution should block export/release.                |

### 7.3 Evidence and claim components

| Component             | Purpose                                              | Required behavior                                     |
| --------------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| `EvidenceDrawer`      | Trust-visible evidence surface.                      | Popups must not replace it.                           |
| `EvidenceSummaryCard` | Short readable claim/evidence summary.               | Must show uncertainty and source role where relevant. |
| `SourceLineageCard`   | Shows source family, role, date, cadence, rights.    | Must preserve source-role anti-collapse.              |
| `PolicyDecisionCard`  | Shows allow/deny/restrict/generalize/abstain status. | Must show reason code where safe.                     |
| `ReleaseStateCard`    | Shows release ID, stale/superseded/current status.   | Must link to release/correction where available.      |
| `CitationList`        | Shows evidence references.                           | Missing citations produce abstain or deny.            |
| `CorrectionBanner`    | Shows corrected, withdrawn, or superseded state.     | Must be visible on affected claims/layers.            |

### 7.4 Focus Mode components

| Component                | Purpose                                  | Required behavior                                        |
| ------------------------ | ---------------------------------------- | -------------------------------------------------------- |
| `FocusModePanel`         | Natural-language map/evidence assistant. | Must use governed API only.                              |
| `FocusQuestionComposer`  | User prompt input.                       | Must scope to released evidence and visible map context. |
| `FocusEvidenceBuilder`   | Builds evidence context.                 | Must resolve EvidenceRefs before answer.                 |
| `FocusResponseCard`      | Shows answer/abstain/deny/error.         | Must expose citations and uncertainty.                   |
| `FocusTracePanel`        | Maintainer/debug view of bounded trace.  | Must not expose secrets/raw data.                        |
| `FocusCitationValidator` | Blocks unsupported claims.               | Missing support means abstain, not guess.                |

### 7.5 Timeline components

| Component             | Purpose                              | Required behavior                                       |
| --------------------- | ------------------------------------ | ------------------------------------------------------- |
| `TimelineControl`     | Scrubs or selects time.              | Must distinguish valid time, source time, release time. |
| `TemporalLayerFilter` | Applies time filters to layers.      | Must avoid false continuity.                            |
| `ChangeComparePanel`  | Compares releases or time windows.   | Must show evidence/release differences.                 |
| `StaleDataBadge`      | Shows stale source or stale release. | Must be visible, not hidden in debug.                   |

### 7.6 Review and admin preview components

| Component               | Purpose                                 | Required behavior                       |
| ----------------------- | --------------------------------------- | --------------------------------------- |
| `ReviewMapPreview`      | Preview candidate layers for reviewers. | Must be clearly non-public.             |
| `PolicyPreviewOverlay`  | Shows denied/restricted redactions.     | Must not leak exact sensitive geometry. |
| `ValidationOverlay`     | Shows validation failures and warnings. | Must link to ValidationReport.          |
| `ReleaseCandidatePanel` | Shows release readiness.                | Must require manifest/proof/review.     |

### 7.7 Export and story components

| Component            | Purpose                                                 | Required behavior                                            |
| -------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `ExportPanel`        | Exports screenshots, PDFs, GeoJSON subsets, or reports. | Must preserve citations, attribution, policy, release state. |
| `StoryNodePanel`     | Narrative map state and explanation.                    | Story node is a carrier, not proof.                          |
| `ShareLinkBuilder`   | Creates safe URLs for map state.                        | Must not embed restricted data.                              |
| `PrintLayoutPreview` | Shows printable map layout.                             | Must include citations and attribution.                      |

---

## 8. Functions and feature matrix

| Function                 | User value                                  | Required governance                                              |
| ------------------------ | ------------------------------------------- | ---------------------------------------------------------------- |
| Pan/zoom/bearing/pitch   | Navigate Kansas spatial context.            | No special trust claim by itself.                                |
| Layer search             | Find available public-safe layers.          | Only list released or explicitly scoped preview layers.          |
| Layer toggle             | Show/hide layer.                            | Toggle is not publication.                                       |
| Layer opacity            | Visual comparison.                          | Must not hide sensitivity problems.                              |
| Feature click            | Inspect a map feature.                      | Must resolve EvidenceRef through governed API.                   |
| Hover summary            | Lightweight orientation.                    | No consequential claim unless evidence-backed.                   |
| Evidence Drawer          | Inspect evidence and release state.         | Must show source role, policy, citations, correction state.      |
| Timeline scrub           | Explore time.                               | Must preserve valid/source/release time distinctions.            |
| Compare releases         | Inspect change.                             | Must identify release manifests and correction/rollback posture. |
| Filter by domain         | Narrow visible data.                        | Filters are UI state, not truth state.                           |
| Filter by source role    | Separate observed/modeled/regulatory/etc.   | Prevents source-role collapse.                                   |
| Filter by policy status  | Show public/restricted/denied availability. | Must not reveal restricted coordinates.                          |
| Legend view              | Interpret colors/symbols.                   | Must show classification source and date if consequential.       |
| Attribution view         | Show source terms.                          | Missing rights/attribution blocks export.                        |
| Download/export          | Produce reusable artifact.                  | Must carry release/citation/attribution/policy metadata.         |
| Focus Mode answer        | Ask about map/evidence.                     | Must resolve evidence and emit finite outcome.                   |
| Story Node               | Narrative map moment.                       | Must remain evidence-bound.                                      |
| Offline package          | Use released map offline.                   | Must include manifest, hashes, policy, citations.                |
| Accessibility navigation | Keyboard/screen-reader use.                 | Must include drawer, layers, timeline, negative states.          |
| Debug/proof view         | Maintainer validation.                      | Must not expose secrets/raw/sensitive data publicly.             |

---

## 9. Layer lifecycle

### 9.1 Proposed public layer admission flow

```text
Candidate layer idea
  → SourceDescriptor check
  → rights and sensitivity precheck
  → raw/source capture
  → transform into layer candidate
  → schema validation
  → artifact validation
  → source-layer/style validation
  → EvidenceBundle closure
  → PolicyDecision
  → TileArtifactManifest / LayerManifest
  → PromotionDecision
  → ReleaseManifest
  → RollbackCard
  → governed API exposure
  → MapLibre addSource/addLayer
```

### 9.2 Layer release readiness checklist

A layer is not public-ready until it has:

* [ ] source identity
* [ ] source role
* [ ] rights posture
* [ ] sensitivity posture
* [ ] transform receipt
* [ ] validation report
* [ ] evidence closure
* [ ] citation validation where claims are made
* [ ] policy decision
* [ ] artifact manifest
* [ ] release manifest
* [ ] rollback target
* [ ] correction path
* [ ] attribution text
* [ ] stale-state behavior
* [ ] negative-state fixture
* [ ] no raw/work/quarantine dependency in public client

---

## 10. Tile and artifact strategy

### 10.1 Artifact classes

| Artifact              | Best use                                                  | Cautions                                                                    |
| --------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- |
| PMTiles               | Static/vector tile archives, CDN/range-friendly delivery. | Validate Range/CORS/cache behavior; avoid in-place overwrite.               |
| MVT                   | Vector tile payload format.                               | Must preserve source-layer names and schema.                                |
| COG                   | Cloud-optimized raster delivery.                          | Needs internal overview/metadata validation and public-safe classification. |
| GeoParquet            | Columnar spatial data exchange and processing.            | Not automatically public; requires policy/release closure.                  |
| MBTiles               | Local or build-time tile packaging.                       | Not ideal as public browser delivery without server mediation.              |
| GeoJSON               | Small previews, fixtures, simple overlays.                | Avoid dense production GeoJSON at scale.                                    |
| Style JSON            | Map presentation.                                         | Must be versioned and source-layer validated.                               |
| Sprites/glyphs/icons  | UI rendering assets.                                      | Must be cache/version controlled.                                           |
| 3D Tiles/glTF/terrain | 3D/terrain views.                                         | High exposure; must have same evidence/policy as 2D.                        |

### 10.2 PMTiles governance

PMTiles should be treated as a released artifact, not a proof object.

Public PMTiles should have:

* versioned filename
* content digest
* sidecar manifest
* tile/source metadata
* build tool/version record
* source ledger reference
* release manifest reference
* cache invalidation plan
* rollback target
* Range/CORS validation
* attribution
* policy classification

Avoid in-place overwrite. Prefer versioned immutable artifacts and release pointers.

### 10.3 COG governance

COG outputs should have:

* source raster lineage
* resolution/scale metadata
* overview validation
* nodata validation
* coordinate reference check
* digest / sidecar
* public-safe classification
* policy decision
* release manifest reference
* rollback target

### 10.4 Style governance

Style JSON must be:

* versioned
* linked to approved layer/source IDs
* validated against source-layer names
* tested for missing sprites/glyphs
* checked for hidden sensitive fields
* checked for attribution
* tied to a release manifest

A style-only filter must never be the sole redaction mechanism.

---

## 11. LayerManifest reference shape

This is an explanatory shape, not a canonical schema.

```yaml
layer_manifest:
  id: "kfm.layer.<domain>.<name>.<version>"
  title: "<human title>"
  domain: "<domain-or-cross-domain>"
  status: "candidate | released | superseded | withdrawn"
  release_ref: "kfm://release/..."
  source_descriptor_refs:
    - "kfm://source/..."
  evidence_bundle_refs:
    - "kfm://evidence-bundle/..."
  policy_decision_ref: "kfm://policy-decision/..."
  validation_report_refs:
    - "kfm://validation-report/..."
  artifact_refs:
    - type: "pmtiles | mvt | cog | geojson | style"
      uri: "kfm://artifact/..."
      digest: "sha256:..."
  style_refs:
    - "kfm://style/..."
  sensitivity:
    public_tier: "T0 | T1 | T2 | T3 | T4"
    geometry_transform: "none | generalized | redacted | suppressed"
    redaction_receipt_ref: "kfm://receipt/redaction/..."
  time:
    valid_time: "<interval-or-null>"
    source_time: "<timestamp-or-interval>"
    release_time: "<timestamp>"
  attribution:
    required_text: "<attribution>"
    license_posture: "<license/terms summary>"
  rollback_ref: "kfm://rollback-card/..."
  correction_ref: "kfm://correction-notice/..."
```

---

## 12. MapContextEnvelope reference shape

This is an explanatory shape, not a canonical schema.

```yaml
map_context_envelope:
  request_id: "<uuid-or-deterministic-id>"
  user_context:
    exposure_class: "public | reviewer | admin"
    locale: "en-US"
  map_context:
    viewport:
      bounds: [west, south, east, north]
      center: [longitude, latitude]
      zoom: 8
      bearing: 0
      pitch: 0
    time:
      valid_time: "<selected-valid-time>"
      release_time: "<selected-release-time>"
    layers:
      visible_layer_ids:
        - "kfm.layer..."
      filter_state:
        domain: []
        source_role: []
        policy_status: []
    selection:
      feature_id: "<feature-id>"
      evidence_ref: "kfm://evidence-ref/..."
      layer_id: "kfm.layer..."
  requested_action: "inspect_feature | focus_answer | export | compare | explain_layer"
```

---

## 13. Evidence Drawer behavior

### 13.1 Drawer purpose

The Evidence Drawer is the trust-visible UI projection of evidence, policy, release, and correction state.

It is not itself the evidence store.

### 13.2 Drawer must show

Where safe and available, the drawer should show:

* selected feature label
* claim summary
* source role
* source title
* source date/cadence
* EvidenceRef
* EvidenceBundle reference
* citation list
* validation state
* policy decision
* sensitivity posture
* release ID
* current/superseded/stale state
* correction notice
* rollback/release lineage
* uncertainty and limitations
* abstain/deny/error reason codes when applicable

### 13.3 Drawer finite states

| State        | Meaning                                              |
| ------------ | ---------------------------------------------------- |
| `loading`    | Evidence/policy/release lookup pending.              |
| `answer`     | Evidence resolves and policy permits display.        |
| `abstain`    | Evidence insufficient or unresolved.                 |
| `deny`       | Policy blocks display.                               |
| `error`      | System/integrity/runtime failure.                    |
| `stale`      | Source or release is stale; show warning or abstain. |
| `superseded` | A newer release/correction exists.                   |
| `withdrawn`  | Prior claim/layer is withdrawn.                      |

### 13.4 Popup rule

Popups may summarize, but they must not replace the Evidence Drawer for consequential claims.

A popup may show:

* feature name
* layer name
* basic safe attributes
* button to inspect evidence
* release/stale indicator

A popup must not show:

* unsupported claims
* hidden sensitive fields
* exact restricted coordinates
* model-generated conclusions without citations
* evidence-free authority language

---

## 14. Focus Mode behavior

### 14.1 Focus Mode purpose

Focus Mode provides bounded, evidence-resolved, policy-aware explanation over map context.

### 14.2 Focus Mode required flow

```text
User question
  → map context envelope
  → governed API
  → evidence retrieval
  → EvidenceRef resolution
  → policy/sensitivity check
  → citation validation
  → finite RuntimeResponseEnvelope
  → UI answer/abstain/deny/error
```

### 14.3 Focus Mode must not

* read raw/canonical stores directly
* call model providers from browser
* answer from rendered features alone
* infer source authority
* downgrade sensitivity
* publish or approve release
* hide citation failures
* convert missing evidence into confident prose

### 14.4 Focus Mode outputs

| Output    | Required behavior                                               |
| --------- | --------------------------------------------------------------- |
| `ANSWER`  | Include citations, evidence refs, uncertainty, and scope.       |
| `ABSTAIN` | Explain missing evidence or unsupported scope without guessing. |
| `DENY`    | Explain policy boundary where safe.                             |
| `ERROR`   | Show non-claiming failure state.                                |

---

## 15. Time-aware map behavior

KFM is time-aware. MapLibre UI must avoid flattening time.

### 15.1 Time concepts

| Time concept      | Meaning                                           |
| ----------------- | ------------------------------------------------- |
| Source time       | When source observed, published, or updated data. |
| Valid time        | Time period the data claims to describe.          |
| Transaction time  | When KFM admitted or changed a record.            |
| Release time      | When KFM published a governed artifact.           |
| Supersession time | When a release or claim was replaced.             |
| Correction time   | When a correction became effective.               |

### 15.2 Timeline controls

Timeline UI should support:

* selected valid-time range
* selected release version
* stale-state display
* compare two releases
* compare two time windows
* explain source date vs release date
* show uncertainty when time resolution differs

### 15.3 Time anti-patterns

Avoid:

* presenting old source data as current
* silently mixing source time and release time
* comparing layers with incompatible temporal meaning
* hiding stale-state warnings
* treating animated time as proof of change

---

## 16. Sensitive geometry and public safety

### 16.1 Deny-by-default surfaces

Exact sensitive locations should default to denial or generalization unless explicitly reviewed and released.

Examples include:

* archaeological sites
* burial/sacred sites
* rare species locations
* sensitive habitat
* critical infrastructure vulnerabilities
* private-property-sensitive exposure
* living-person locations
* DNA/genomic-linked places
* military/security-sensitive data

### 16.2 Redaction before render

Sensitive material must be transformed before it becomes a public artifact.

Do not rely on:

* style filters
* layer visibility
* CSS hiding
* client-side field suppression
* obscured labels
* hidden popups

### 16.3 Required artifacts for sensitive public layers

A sensitive-but-public-safe layer should have:

* sensitivity review
* policy decision
* redaction/generalization transform
* redaction receipt
* validation proving exact sensitive geometry is absent
* release manifest
* rollback/correction path

---

## 17. Plugin, wrapper, and dependency governance

### 17.1 Admission checklist

Before adding a MapLibre plugin, wrapper, protocol handler, renderer extension, or tile library:

* [ ] license checked
* [ ] security posture checked
* [ ] maintenance status checked
* [ ] package version pinned
* [ ] browser support checked
* [ ] mobile impact checked
* [ ] accessibility impact checked
* [ ] network behavior checked
* [ ] no raw/direct model access
* [ ] no sensitive data leakage
* [ ] fixture and negative tests added
* [ ] rollback/removal path documented

### 17.2 Plugin categories

| Category              | Examples                             | Posture                                        |
| --------------------- | ------------------------------------ | ---------------------------------------------- |
| Protocol handlers     | PMTiles protocol, custom URL loaders | Allow only with review and tests.              |
| Raster readers        | COG readers, raster plugins          | Validate headers, CORS, range, caching.        |
| 3D extensions         | Three.js bridge, 3D tiles plugins    | Treat as high-exposure.                        |
| Drawing/editing tools | review annotation, field capture     | Keep public and review paths separate.         |
| Search/geocoder       | place search, gazetteer lookup       | Must use governed sources and policy.          |
| Measurement tools     | distance, area, profile              | Must disclose projection/scale limits.         |
| Export plugins        | screenshots/PDFs                     | Must carry citation/release/attribution state. |

---

## 18. Accessibility and trust-visible UX

### 18.1 Required accessibility surfaces

The map shell should support:

* keyboard navigation
* focus states
* screen-reader labels
* drawer focus trap
* skip links
* visible loading states
* visible deny/abstain/error states
* non-color-only symbology
* readable legend text
* accessible export controls
* reduced-motion mode where applicable

### 18.2 Evidence Drawer accessibility

Evidence Drawer should be:

* keyboard reachable
* ARIA-labelled
* closeable by keyboard
* navigable by headings
* able to expose citations as links
* able to announce finite outcome state
* able to preserve focus after map interactions

### 18.3 Trust-visible negative states

Blank maps are dangerous when they hide policy or data failures.

The UI should distinguish:

* no data exists
* data exists but is denied
* data exists but is restricted
* data exists but is stale
* data exists but failed validation
* data exists but release was withdrawn
* data exists but source is offline
* data exists but user lacks scope
* system error

---

## 19. Performance budgets

Performance budgets are **PROPOSED** and should be tuned by device testing.

| Budget                                 |                                  Target | Notes                                     |
| -------------------------------------- | --------------------------------------: | ----------------------------------------- |
| Initial shell interactive              | < 3 seconds on modern desktop broadband | Excludes first cold tile load.            |
| Layer catalog response                 |              < 500 ms from governed API | Cache safe metadata.                      |
| addSource/addLayer after manifest pass |     < 1 second for typical vector layer | Fail visibly if artifact unavailable.     |
| Click to Evidence Drawer loading state |                                < 150 ms | Immediate feedback.                       |
| Click to Evidence Drawer answer        |                   < 1.5 seconds typical | Longer states must show progress/abstain. |
| Focus Mode first token/response state  |            < 2 seconds to visible state | Do not spin silently.                     |
| Timeline filter UI response            |           < 300 ms local state response | Data refresh may take longer.             |
| Tile error display                     |                    immediate when known | Do not hide errors in console only.       |
| Mobile memory                          |                      NEEDS VERIFICATION | Test with real device classes.            |
| Offline cache size                     |                      NEEDS VERIFICATION | Must be release-scoped and policy-safe.   |

---

## 20. Testing and validation plan

### 20.1 Required fixture classes

| Fixture                      | Purpose                                                    |
| ---------------------------- | ---------------------------------------------------------- |
| Valid public layer           | Proves normal released layer loads.                        |
| Missing LayerManifest        | Must deny/fail closed.                                     |
| Invalid digest               | Must deny/fail closed.                                     |
| Missing EvidenceBundle       | Drawer/Focus must abstain.                                 |
| Denied sensitive geometry    | Public map must not render exact geometry.                 |
| Redacted geometry            | Public map renders generalized safe geometry with receipt. |
| Stale release                | UI shows stale badge or abstains.                          |
| Superseded release           | UI shows supersession/correction state.                    |
| Style source-layer mismatch  | Release validation fails.                                  |
| Missing attribution          | Export/release fails.                                      |
| Plugin not allowlisted       | Build/release fails.                                       |
| Browser direct model call    | Test fails.                                                |
| RAW URL in client bundle     | Test fails.                                                |
| Accessibility keyboard path  | Must pass.                                                 |
| Export citation preservation | Must pass.                                                 |

### 20.2 Test categories

| Test class          | Required coverage                                                               |
| ------------------- | ------------------------------------------------------------------------------- |
| Schema validation   | LayerManifest, TileArtifactManifest, EvidenceDrawerPayload, MapContextEnvelope. |
| Policy tests        | public/reviewer/admin, deny/restrict/generalize/abstain.                        |
| Artifact tests      | PMTiles/COG digest, sidecar, Range/CORS, source-layer names.                    |
| UI tests            | drawer, layer manager, timeline, Focus Mode states.                             |
| Accessibility tests | keyboard, ARIA, focus, visible negative states.                                 |
| Security tests      | no direct raw/canonical/model endpoints in client.                              |
| Release tests       | manifest, rollback card, correction notice, cache invalidation.                 |
| Citation tests      | Focus Mode/export claims require citations.                                     |
| Regression tests    | style and layer visual snapshots where useful.                                  |

### 20.3 CI gates

A map-related PR should fail if it:

* adds a public layer without a manifest
* references RAW/WORK/QUARANTINE from public UI
* adds a plugin without review metadata
* changes style source-layer names without validation
* adds Focus Mode client direct model access
* exports uncited consequential claims
* omits attribution
* omits rollback/correction path for release changes
* exposes exact sensitive geometry
* bypasses governed API

---

## 21. Anti-pattern register

| Anti-pattern                                | Response                                                                |
| ------------------------------------------- | ----------------------------------------------------------------------- |
| Treating MapLibre as truth authority        | **DENY** — renderer cannot decide truth, policy, release, or citations. |
| Treating tiles as proof                     | **DENY** — tiles are artifacts; evidence must resolve separately.       |
| Treating layer toggle as publication        | **DENY** — publication requires governed promotion/release.             |
| Hiding sensitive geometry by style only     | **DENY** — transform/redact/generalize before release.                  |
| Direct browser access to model runtime      | **DENY** — Focus Mode uses governed API.                                |
| AI answer from rendered features only       | **ABSTAIN / DENY** — rendered features are candidates only.             |
| Uncited popup or export                     | **ABSTAIN / DENY** — preserve citations.                                |
| Public RAW/WORK/QUARANTINE URL in client    | **DENY** — violates trust membrane.                                     |
| Missing release manifest                    | **DENY** public loading.                                                |
| Missing rollback target                     | **DENY** release.                                                       |
| Missing attribution                         | **DENY** export/release.                                                |
| Style source-layer mismatch                 | **DENY** release.                                                       |
| Plugin adoption without review              | **DENY** until allowlisted and tested.                                  |
| PMTiles in-place overwrite                  | **NEEDS VERIFICATION / avoid** — prefer versioned immutable artifacts.  |
| Dense GeoJSON as large production default   | **NEEDS VERIFICATION** — prefer tiles/server mediation.                 |
| MLT as production default before validation | **NEEDS VERIFICATION**.                                                 |
| 3D/globe as default when 2D is clearer      | **PROPOSED only with evidence burden.**                                 |
| Verification theater                        | **DENY** — badges without enforcement are not trust.                    |
| Blank map on policy denial                  | **DENY UX pattern** — show negative state.                              |
| Export without release/citation metadata    | **DENY**.                                                               |
| Cache not invalidated after rollback        | **DENY / ERROR** until corrected.                                       |

---

## 22. Domain-specific map guidance

### 22.1 Hydrology

Hydrology layers may include watersheds, streamflow context, floodplain products, groundwater, water quality, drought indicators, and hydro-climate overlays.

Rules:

* distinguish observed, modeled, regulatory, and derived context
* avoid claiming regulatory status from non-regulatory sources
* show source date and gauge/station context
* preserve HUC and geometry versioning
* route uncertain source status to abstain or stale display

### 22.2 Soil

Soil layers may include SSURGO/gSSURGO, soil properties, horizons, capability, erosion, soil moisture, and related raster products.

Rules:

* disclose scale and map-unit limitations
* preserve MUKEY/COKEY/CHKEY lineage where relevant
* do not overclaim field-level precision
* tie rasters and COGs to source and transform receipts

### 22.3 Habitat, fauna, and flora

Ecology layers may include habitat patches, modeled suitability, corridors, occurrences, monitoring summaries, rare species public-safe views, and restoration context.

Rules:

* exact sensitive occurrences default to deny
* public layers should use generalized or redacted views
* taxonomy resolution must be visible where relevant
* evidence and sensitivity must travel together

### 22.4 Agriculture

Agriculture layers may include cropland, crop history, irrigation, drought/crop stress, CDL, NASS aggregate context, and field-safe summaries.

Rules:

* distinguish aggregate from field-level inference
* source-year and classification uncertainty must be visible
* material-change watchers should emit candidate work, not publish
* field-level private exposure requires policy review

### 22.5 Roads, rail, and trade routes

Transport layers may include road networks, rail networks, trade routes, historic corridors, restrictions, nodes, facilities, and graph projections.

Rules:

* current operational restrictions may be sensitive
* historic route interpretation must show source basis
* graph/path outputs are derived carriers
* public routing claims need source-date and restriction context

### 22.6 Settlements and infrastructure

Settlement layers may include municipalities, census places, historic townsites, ghost towns, forts, depots, missions, facilities, service areas, and infrastructure dependencies.

Rules:

* critical infrastructure defaults to restricted/generalized posture
* historic settlement interpretation needs evidence closure
* public maps should avoid vulnerability-enabling precision

### 22.7 Archaeology and cultural heritage

Archaeology layers may include generalized site context, surveys, cultural regions, historic interpretation, and reviewed public-safe educational layers.

Rules:

* exact site coordinates default to deny
* generalized public geometry requires transform receipt
* cultural/sovereignty sensitivity must fail closed
* map storytelling must not reveal protected locations

### 22.8 People, genealogy, DNA, and land

People and land layers may include historical person assertions, land ownership assertions, cemetery context, migration paths, and public historical records.

Rules:

* living-person data defaults to deny/restrict
* DNA-derived outputs default to deny/restrict
* assessor records are not title truth
* land ownership is temporal assertion, not map label alone

### 22.9 Atmosphere, air, hazards, geology, and natural resources

These layers may include air quality, smoke, weather, climate, hazards, geology, minerals, surficial context, aquifers, terrain, and remote sensing.

Rules:

* observations, models, regulatory records, and fused products must not collapse
* hazards layers must avoid pretending to be live emergency alerts unless governed as such
* geology/resource layers should not substitute context for direct observation
* terrain/3D views require public-safe exposure review

---

## 23. Implementation-ready object map

### 23.1 Docs

| File                                                              | Purpose                            | Status                 |
| ----------------------------------------------------------------- | ---------------------------------- | ---------------------- |
| `docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` | This master reference.             | **PROPOSED**           |
| `docs/architecture/map-shell.md`                                  | Map shell architecture.            | **NEEDS VERIFICATION** |
| `docs/architecture/evidence-drawer.md`                            | Drawer behavior and trust model.   | **PROPOSED**           |
| `docs/architecture/focus-mode.md`                                 | Focus Mode behavior and boundary.  | **PROPOSED**           |
| `docs/runbooks/map-release.md`                                    | How to release a map/layer bundle. | **PROPOSED**           |
| `docs/runbooks/map-rollback.md`                                   | How to rollback map releases.      | **PROPOSED**           |

### 23.2 Contracts

| Contract                                         | Purpose                         | Status       |
| ------------------------------------------------ | ------------------------------- | ------------ |
| `contracts/map/layer-manifest.md`                | LayerManifest meaning.          | **PROPOSED** |
| `contracts/map/tile-artifact-manifest.md`        | TileArtifactManifest meaning.   | **PROPOSED** |
| `contracts/map/map-context-envelope.md`          | MapContextEnvelope meaning.     | **PROPOSED** |
| `contracts/ui/evidence-drawer-payload.md`        | EvidenceDrawerPayload meaning.  | **PROPOSED** |
| `contracts/runtime/runtime-response-envelope.md` | Finite runtime outcome meaning. | **PROPOSED** |

### 23.3 Schemas

| Schema                                                               | Purpose                 | Status       |
| -------------------------------------------------------------------- | ----------------------- | ------------ |
| `schemas/contracts/v1/map/layer_manifest.schema.json`                | Layer manifest shape.   | **PROPOSED** |
| `schemas/contracts/v1/map/tile_artifact_manifest.schema.json`        | Tile artifact shape.    | **PROPOSED** |
| `schemas/contracts/v1/map/map_context_envelope.schema.json`          | Map context shape.      | **PROPOSED** |
| `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`        | Drawer payload shape.   | **PROPOSED** |
| `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | Runtime envelope shape. | **PROPOSED** |

### 23.4 Policy

| Policy area                | Purpose                                  | Status                            |
| -------------------------- | ---------------------------------------- | --------------------------------- |
| `policy/maplibre/`         | Renderer and layer policy.               | **PROPOSED / NEEDS VERIFICATION** |
| `policy/runtime/`          | Runtime finite outcomes.                 | **NEEDS VERIFICATION**            |
| `policy/sensitivity/`      | Sensitivity tiers and geometry exposure. | **NEEDS VERIFICATION**            |
| `policy/release/`          | Release gates.                           | **NEEDS VERIFICATION**            |
| `policy/domains/<domain>/` | Domain-specific map policy.              | **NEEDS VERIFICATION**            |

### 23.5 Tests and fixtures

| Test/fixture                                      | Purpose                                    | Status       |
| ------------------------------------------------- | ------------------------------------------ | ------------ |
| `fixtures/map/layers/valid_public_layer.json`     | Happy path layer.                          | **PROPOSED** |
| `fixtures/map/layers/denied_sensitive_layer.json` | Deny exact sensitive geometry.             | **PROPOSED** |
| `fixtures/map/layers/missing_evidence_ref.json`   | Abstain on missing evidence.               | **PROPOSED** |
| `tests/map/test_layer_manifest_validation.py`     | Validate manifests.                        | **PROPOSED** |
| `tests/map/test_no_public_raw_access.py`          | Prevent public raw/work/quarantine access. | **PROPOSED** |
| `tests/map/test_focus_mode_citations.py`          | Focus citation enforcement.                | **PROPOSED** |
| `tests/map/test_accessibility_states.py`          | UI trust state accessibility.              | **PROPOSED** |

---

## 24. Next smallest useful PR

**PROPOSED — Build a manifest-first MapLibre proof slice.**

Include:

1. This document.
2. `contracts/map/layer-manifest.md`.
3. `schemas/contracts/v1/map/layer_manifest.schema.json`.
4. One public-safe synthetic layer fixture.
5. One denied sensitive fixture.
6. One missing-evidence abstain fixture.
7. Validator for LayerManifest.
8. Test proving public client cannot reference RAW/WORK/QUARANTINE.
9. Test proving missing evidence returns abstain.
10. Test proving denied sensitive layer cannot be loaded.
11. Documentation note linking MapLibre addSource to manifest verification.
12. Rollback note for the proof slice.

Do not include live source fetches in the first PR unless source rights, source cadence, and source descriptor review are already complete.

---

## 25. Open verification backlog

| ID        | Question                                                                | Status                 | Resolution path                             |
| --------- | ----------------------------------------------------------------------- | ---------------------- | ------------------------------------------- |
| ML-OQ-001 | Does this exact file already exist in the repo?                         | **NEEDS VERIFICATION** | Inspect current repo.                       |
| ML-OQ-002 | Is `docs/` the final home, or should this move to `docs/architecture/`? | **NEEDS VERIFICATION** | Check docs index and Directory Rules.       |
| ML-OQ-003 | What MapLibre GL JS version is pinned?                                  | **NEEDS VERIFICATION** | Inspect package lockfiles.                  |
| ML-OQ-004 | Is `packages/maplibre/` present and canonical?                          | **NEEDS VERIFICATION** | Inspect repo and ADRs.                      |
| ML-OQ-005 | Is `apps/explorer-web/` the current public shell?                       | **NEEDS VERIFICATION** | Inspect repo.                               |
| ML-OQ-006 | Does governed API expose map layer, evidence, and Focus Mode endpoints? | **NEEDS VERIFICATION** | Inspect API routes/tests.                   |
| ML-OQ-007 | Are LayerManifest and TileArtifactManifest schemas already present?     | **NEEDS VERIFICATION** | Inspect schemas/contracts/v1.               |
| ML-OQ-008 | Are PMTiles sidecar/digest checks implemented?                          | **NEEDS VERIFICATION** | Inspect tools/tests/release artifacts.      |
| ML-OQ-009 | Are Range/CORS/cache behaviors tested for PMTiles/COGs?                 | **NEEDS VERIFICATION** | Inspect CI/runtime tests.                   |
| ML-OQ-010 | Is MLT supported, piloted, or only tracked?                             | **NEEDS VERIFICATION** | Inspect package/toolchain docs.             |
| ML-OQ-011 | Is a plugin allowlist present?                                          | **NEEDS VERIFICATION** | Inspect control plane/policy/docs.          |
| ML-OQ-012 | Are source-layer mismatch tests implemented?                            | **NEEDS VERIFICATION** | Inspect tests.                              |
| ML-OQ-013 | Are accessibility tests merge-blocking?                                 | **NEEDS VERIFICATION** | Inspect CI.                                 |
| ML-OQ-014 | Are Evidence Drawer payload schemas implemented?                        | **NEEDS VERIFICATION** | Inspect contracts/schemas/fixtures.         |
| ML-OQ-015 | Are Focus Mode citations validated before display?                      | **NEEDS VERIFICATION** | Inspect API/UI tests.                       |
| ML-OQ-016 | Are Story Nodes release/citation aware?                                 | **NEEDS VERIFICATION** | Inspect UI/export docs and tests.           |
| ML-OQ-017 | Are map exports blocked when attribution/citations are missing?         | **NEEDS VERIFICATION** | Inspect export pipeline.                    |
| ML-OQ-018 | Is exact sensitive geometry proven absent from public artifacts?        | **NEEDS VERIFICATION** | Inspect validators and release proof packs. |
| ML-OQ-019 | Are rollback and cache invalidation tied together?                      | **NEEDS VERIFICATION** | Inspect release tooling.                    |
| ML-OQ-020 | Are local/offline packages policy-safe and release-scoped?              | **NEEDS VERIFICATION** | Inspect PWA/offline docs.                   |

---

## 26. Source ledger

This ledger is a source-control surface, not a bibliography.

| Source key       | Source                                  | Role in this document                                        | Limitation                                                               |
| ---------------- | --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `SRC-MAP-MASTER` | Prior Master MapLibre cumulative packet | Main MapLibre architecture source.                           | Earlier packet evidence; current repo implementation remains unverified. |
| `SRC-DIRRULES`   | Directory Rules                         | Placement, responsibility roots, drift, UI/map roots.        | File path existence still requires repo check.                           |
| `SRC-REPO-GUIDE` | Repository Structure Guiding Document   | Prior repo-structure and drift summary.                      | Snapshot-bound; current repo may differ.                                 |
| `SRC-GAI`        | Governed AI reports                     | Focus Mode and finite runtime outcome boundary.              | Implementation status unknown.                                           |
| `SRC-UIAI`       | Whole UI + Governed AI report           | Evidence Drawer, UI shell, governed API posture.             | Implementation status unknown.                                           |
| `SRC-PIPELINE`   | Pipeline Living Manual                  | Lifecycle, receipts, promotion, query/save/recompile.        | Implementation status unknown.                                           |
| `SRC-DOMAINS`    | Domain reports and consolidated atlas   | Domain-specific sensitivity and map layer posture.           | Paths and maturity need verification.                                    |
| `SRC-GIS`        | GIS/cartography references              | Representation, scale, projection, communication background. | Not KFM implementation evidence.                                         |
| `SRC-API`        | Web API design reference                | API resource and developer experience background.            | Not KFM implementation evidence.                                         |
| `SRC-DDD`        | Domain-Driven Design reference          | Bounded contexts and published language.                     | Not KFM implementation evidence.                                         |

---

## 27. Maintainer checklist

Before merging this file:

* [ ] Verify the requested path is correct.
* [ ] Check if a prior `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` exists.
* [ ] Decide whether this belongs directly under `docs/` or under `docs/architecture/`.
* [ ] Update docs index / README.
* [ ] Confirm no generated citation tokens remain.
* [ ] Confirm no current implementation claims are unsupported.
* [ ] Confirm all proposed paths are marked PROPOSED or NEEDS VERIFICATION.
* [ ] Link to current Directory Rules.
* [ ] Link to map shell architecture once present.
* [ ] Add drift entry if path or naming convention conflicts.
* [ ] Run Markdown lint.
* [ ] Run link check.
* [ ] Review for sensitive location leakage.
* [ ] Review for public RAW/WORK/QUARANTINE leakage.
* [ ] Review for direct model-client language.
* [ ] Review with docs, map, UI, governed API, policy, and evidence stewards.

---

## 28. Changelog

| Version      |       Date | Change                                                                                                                                                                                                                                  |
| ------------ | ---------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v2.1         | 2026-06-12 | Created repository-facing Markdown working edition for `docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md`; strengthened trust membrane, component matrix, validation plan, anti-patterns, and open verification backlog. |
| v1.9 lineage | 2026-05-10 | Prior cumulative PDF packet retained MapLibre as downstream renderer and carried forward source ledger, idea index, PMTiles/COG/Focus Mode expansions, and verification backlog.                                                        |
| v1.8 lineage | 2026-05-10 | Retained prior cumulative idea baseline.                                                                                                                                                                                                |

---

## 29. Footer

```yaml
kfm_footer:
  document: "Master MapLibre Components, Functions, and Features"
  requested_path: "docs/Master_MapLibre_Components-Functions-Features_v2.1_FULL.md"
  version: "v2.1"
  status: "draft"
  authority_class: "architecture_reference / synthesis; not canonical doctrine"
  owning_root: "docs/"
  implementation_claims: "bounded; current repo/runtime behavior requires verification"
  core_invariant: "RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED"
  renderer_boundary: "MapLibre renders released, governed, evidence-bound artifacts; it is not truth, policy, release, citation, or AI authority."
  next_review_triggers:
    - "Directory Rules update"
    - "Map shell implementation change"
    - "LayerManifest or TileArtifactManifest schema adoption"
    - "PMTiles/COG/MLT tooling change"
    - "Evidence Drawer payload schema adoption"
    - "Focus Mode governed API change"
    - "release/rollback/correction workflow change"
```

**Authority reminder:** This document is a human-facing architecture reference. If it conflicts with accepted doctrine, accepted ADRs, contracts, schemas, policy, release manifests, proof objects, or verified current repo evidence, those authorities win.
