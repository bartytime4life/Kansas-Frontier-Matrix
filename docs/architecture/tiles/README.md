<!-- [KFM_META_BLOCK_V2]
doc_id: TODO-NEEDS-VERIFICATION-kfm://doc/<uuid>
title: KFM Tile Delivery Architecture
type: standard
version: v1
status: draft
owners: TODO-NEEDS-VERIFICATION
created: TODO-NEEDS-VERIFICATION
updated: 2026-04-30
policy_label: TODO-NEEDS-VERIFICATION
related: [docs/architecture/tiles/README.md, TODO-verify-adjacent-doc-links]
tags: [kfm, tiles, maplibre, delivery, governance]
notes: [Created as a repo-ready draft from attached KFM doctrine. Repository tree was not mounted during authoring, so doc_id, owners, created date, policy label, and adjacent relative links require maintainer verification before publication.]
[/KFM_META_BLOCK_V2] -->

# KFM Tile Delivery Architecture

Purpose: define how Kansas Frontier Matrix tile artifacts are produced, governed, released, rendered, inspected, rolled back, and kept subordinate to evidence.

## Impact block

![KFM](https://img.shields.io/badge/KFM-governed%20tiles-2f6f4e)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Truth](https://img.shields.io/badge/truth-cite--or--abstain-blue)
![Repo evidence](https://img.shields.io/badge/repo--evidence-NEEDS%20VERIFICATION-lightgrey)

| Field | Value |
|---|---|
| **Status** | `experimental` |
| **Owners** | `TODO-NEEDS-VERIFICATION` |
| **Target path** | `docs/architecture/tiles/README.md` |
| **Primary audience** | maintainers building map delivery, release manifests, tile fixtures, governed APIs, MapLibre UI surfaces, and validation gates |
| **Repository evidence posture** | `NEEDS VERIFICATION` — this draft is doctrine-grounded, but current repo topology and implementation depth were not verified during authoring |
| **Primary rule** | tiles are rebuildable delivery artifacts, not canonical truth |

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Tile lifecycle](#tile-lifecycle) · [Delivery posture](#delivery-posture) · [Promotion gates](#promotion-and-validation-gates) · [Quickstart](#quickstart) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

> [!IMPORTANT]
> KFM tiles are downstream of source descriptors, EvidenceBundles, policy decisions, review state, promotion, and release manifests. A tile may be fast, beautiful, and cached globally while still being unsafe to publish if rights, sensitivity, evidence support, provenance, release identity, or rollback are unresolved.

---

## Scope

This directory documents the **tile delivery architecture** for KFM’s governed map-first system.

It covers:

- vector-tile, raster-tile, PMTiles, MBTiles, COG-backed raster, and small GeoJSON delivery posture;
- tile artifact identity, manifests, checksums, source references, stale state, and rollback targets;
- how released tile artifacts connect to `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, and `EvidenceDrawerPayload`;
- how MapLibre receives tile artifacts without becoming a truth store;
- what must be validated before a tile artifact can appear on a public or semi-public surface.

It does **not** define canonical domain truth. Canonical evidence belongs upstream.

> [!NOTE]
> This README is intentionally architecture-first. Build scripts, source connectors, live source credentials, and concrete tiler commands belong in repo-native tool, pipeline, or runbook homes after those homes are verified.

[Back to top](#kfm-tile-delivery-architecture)

---

## Repo fit

| Relationship | Path or target | Status | Notes |
|---|---:|---|---|
| **This document** | `docs/architecture/tiles/README.md` | `CONFIRMED by task` | Directory README and standard architecture doc. |
| **Upstream doctrine** | `docs/architecture/maplibre/` | `NEEDS VERIFICATION` | Expected home for MapLibre shell law and renderer boundary if present. |
| **Upstream lifecycle doctrine** | `docs/architecture/pipeline/` or equivalent | `NEEDS VERIFICATION` | Expected home for RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED lifecycle docs. |
| **Architecture decisions** | `docs/adr/` | `NEEDS VERIFICATION` | Should contain tile schema-home, PMTiles/Martin split, MVT/MLT posture, and release-manifest decisions. |
| **Machine contracts** | `schemas/contracts/v1/maplibre/` or repo-native equivalent | `NEEDS VERIFICATION` | Should hold layer, style, tile artifact, release, drawer, and focus payload schemas once schema authority is resolved. |
| **API contracts** | `contracts/api/maplibre/` or repo-native equivalent | `NEEDS VERIFICATION` | Should define click resolution, layer catalog, release lookup, and Evidence Drawer payload surfaces. |
| **Policy gates** | `policy/maplibre/` or repo-native equivalent | `NEEDS VERIFICATION` | Should enforce no public raw path, no direct model client, sensitive-geometry denial, stale abstention, and source-rights blocks. |
| **Fixtures and tests** | `tests/fixtures/maplibre/` or repo-native equivalent | `NEEDS VERIFICATION` | Should include public-safe valid fixtures plus stale, denied, withdrawn, and sensitive examples. |
| **Published delivery artifacts** | `data/published/`, `release/`, or repo-native equivalent | `NEEDS VERIFICATION` | Should contain only released artifacts and manifests, never raw or quarantine material. |

Relative links to adjacent files are intentionally left as path text until maintainers verify the actual repo tree and avoid broken links.

---

## Inputs

The following belong in this architecture area when they are documented, validated, or referenced as tile-delivery surfaces.

| Input family | What belongs here | Minimum posture |
|---|---|---|
| **Source descriptors** | source owner, role, rights, cadence, access method, update signal, sensitivity, expected checks | Required before source-derived tile generation. |
| **Processed public-safe artifacts** | normalized vector/raster products eligible for tile generation | Must already pass source, rights, policy, and sensitivity checks. |
| **Tile artifact manifests** | tile format, hash, build recipe reference, source refs, bounds, zooms, time scope, stale policy, rollback target | Required for every release candidate. |
| **Layer manifests** | layer ID, domain, feature identity contract, release ID, artifact refs, geometry policy, Evidence Drawer contract | Required before public UI exposure. |
| **Style manifests** | style spec version, style hash, sprite/glyph/font policy, layer bindings, accessibility notes | Required when visual meaning is shipped. |
| **Release manifests** | release ID, previous release, promoted artifacts, cache invalidation plan, review state, correction state | Required for published map surfaces. |
| **Evidence payload contracts** | EvidenceBundle refs, citations, policy badges, transforms, withheld counts, correction state | Required for consequential feature inspection. |
| **Negative-state fixtures** | stale source, denied policy, missing evidence, restricted access, withdrawn release, generalized geometry | Required so failures are visible and testable. |

---

## Exclusions

These do **not** belong in `docs/architecture/tiles/` as authoritative content.

| Excluded item | Why it is excluded | Where it should go instead |
|---|---|---|
| RAW, WORK, or QUARANTINE data | Tiles must not become a bypass around governed lifecycle stages. | Lifecycle data homes after repo verification. |
| Canonical domain records | Tiles are derived delivery artifacts, not canonical truth. | Domain canonical stores and EvidenceBundle-producing pipelines. |
| Live source credentials or secrets | Public docs must not expose credentials, tokens, service accounts, or private endpoints. | Secret manager / deployment configuration outside repo-visible docs. |
| Tiler-specific business logic | Tool choice must not define KFM truth. | Repo-native tools, pipelines, and runbooks. |
| Direct browser access to canonical stores | Violates trust membrane and public-client boundary. | Governed API only. |
| Direct model-runtime calls | AI is interpretive and evidence-bounded, not a tile or browser authority. | Governed AI adapter behind policy and citation validation. |
| Exact sensitive location delivery | Rare species, archaeology, cultural, critical infrastructure, private land, living-person, and steward-restricted contexts fail closed. | Restricted access path with policy, review, transform receipts, and withheld accounting. |
| Emergency or life-safety instructions | KFM may provide contextual hazard evidence, not official alerting or emergency guidance. | Official alerting and emergency management sources. |

---

## Directory tree

### Current target

```text
docs/
└── architecture/
    └── tiles/
        └── README.md
```

### Adjacent homes this README expects maintainers to verify

```text
docs/
├── adr/
├── architecture/
│   ├── maplibre/
│   ├── pipeline/
│   └── tiles/
schemas/
└── contracts/
    └── v1/
        └── maplibre/
contracts/
└── api/
    └── maplibre/
policy/
└── maplibre/
tests/
└── fixtures/
    └── maplibre/
data/
└── published/
release/
```

> [!WARNING]
> The adjacent tree is `NEEDS VERIFICATION`. Do not create parallel schema, contract, release, or policy homes if the mounted repository already has a canonical convention. Resolve conflicts through an ADR first.

[Back to top](#kfm-tile-delivery-architecture)

---

## Tile lifecycle

KFM tile delivery follows the same governed lifecycle as other public artifacts. The tile pipeline is a **derived artifact branch** from processed, policy-safe material.

```mermaid
flowchart LR
  S["SourceDescriptor<br/>rights · role · cadence · sensitivity"] --> RAW["RAW"]
  RAW --> V{"Validation<br/>source · schema · rights · sensitivity"}
  V -->|pass| WORK["WORK"]
  V -->|fail / unresolved| Q["QUARANTINE"]
  WORK --> P["PROCESSED<br/>normalized public-safe candidates"]
  P --> EB["CATALOG / TRIPLET<br/>EvidenceBundle · citations · provenance"]
  P --> TB["Tile build<br/>MVT · PMTiles · raster tiles · COG view · small GeoJSON"]
  TB --> TAM["TileArtifactManifest<br/>hashes · bounds · zooms · source refs"]
  EB --> G{"PromotionDecision"}
  TAM --> G
  G -->|approved| PUB["PUBLISHED<br/>MapReleaseManifest"]
  G -->|denied / abstain| HOLD["No publication<br/>visible negative state"]
  PUB --> ML["MapLibre shell<br/>released artifacts only"]
  ML --> API["Governed API<br/>feature candidate resolution"]
  API --> ED["Evidence Drawer<br/>EvidenceBundle-backed claims"]
  API --> FM["Focus Mode<br/>ANSWER · ABSTAIN · DENY · ERROR"]
```

### Operating rule

The renderer sees released artifacts and candidate feature identity. It does not decide evidence support, rights, sensitivity, review state, release state, or citation validity.

---

## Delivery posture

KFM should choose delivery format by evidence burden, scale, public-surface constraints, steward access, cache behavior, and rollback needs.

| Delivery form | Best use | Default posture | Guardrails |
|---|---|---|---|
| **GeoJSON** | Small fixtures, temporary review overlays, selection-driven layers | `selective` | Avoid large public cartography; stable feature IDs required. |
| **MVT** | Dense production vector layers | `production default for thin slice` | Must be manifest-bound and evidence-resolvable. |
| **MLT** | Future benchmark or pilot path | `pilot / NEEDS VERIFICATION` | Do not make production default until repo toolchain and parity evidence are validated. |
| **PMTiles** | Immutable public-safe snapshots, object-store/CDN-like delivery, offline packages | `recommended for stable released bundles` | Require hash, source refs, release ID, cache invalidation, and rollback target. |
| **MBTiles** | Server-side packaging intermediate, local/offline workstation artifact | `situational` | Do not expose restricted content through public archive paths. |
| **Martin/PostGIS tile serving** | Dynamic, steward-mediated, access-controlled, or freshness-sensitive slices | `situational` | Prefer where server policy mediation matters. |
| **COG-backed raster** | Large raster masters, DEM, imagery, climate anomaly, flood-depth, remote-sensing products | `recommended for large raster source/delivery` | Keep COG/source artifact stronger than derived display tiles. |
| **Raster tiles** | Public low-latency display of pixel-dominant products | `selective` | Manifest visual meaning and avoid overclaiming pixel interpretation. |
| **WMS-like overlays** | Transitional or reference layers from external providers | `contextual` | Do not treat external overlay labels as KFM evidence claims. |

> [!TIP]
> A hybrid pattern is usually safest: released static tile artifacts for fast map display, plus governed APIs for Evidence Drawer, dossier, review, precision overlays, Focus Mode, exports, and correction state.

---

## Source/layer/style separation

KFM keeps these concerns separate even when a map library can blur them.

| Plane | Owns | Must not own |
|---|---|---|
| **Source plane** | data location, delivery format, attribution, bounds, min/max zoom, source role | claim truth, policy approval, visual meaning |
| **Layer plane** | visual layer ID, filter/rendering bindings, interaction affordance, trust badges | source rights, canonical feature semantics, publication approval |
| **Style plane** | paint/layout expression, sprites, glyphs, fonts, basemap composition, accessibility notes | evidence authority, sensitivity decision, correction state |
| **Release plane** | manifest closure, artifact hashes, promotion result, prior release, rollback, cache invalidation | raw data storage or hidden reviewer-only state |
| **Evidence plane** | EvidenceBundle, citations, source roles, temporal scope, transforms, withheld counts | browser-only popup text or client-only filtering |

### Practical consequences

- A style change that changes meaning requires a `StyleManifest` update and release consideration.
- A layer toggle is not publication approval.
- A client-side filter must not hide policy-sensitive features in a way that leaks restricted information.
- A tile feature is a delivery representation; it is not automatically equal to one canonical record.
- Popups remain lightweight unless backed by an Evidence Drawer payload.

[Back to top](#kfm-tile-delivery-architecture)

---

## Promotion and validation gates

| Gate | Required evidence | Failure outcome |
|---|---|---|
| **Source gate** | `SourceDescriptor` with owner, official status, rights, cadence, access, update signal, sensitivity, source role, validation checks | `DENY` tile build or keep in `QUARANTINE` |
| **Schema gate** | valid `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, and release payload fixtures | `ERROR` for implementation defect |
| **Policy gate** | rights, sensitivity, stale state, role restriction, public geometry, and no-forbidden-path checks | `DENY` or `ABSTAIN` |
| **Evidence gate** | every consequential public feature resolves to `EvidenceBundle` or a visible negative state | `ABSTAIN` |
| **Artifact gate** | hashes, bounds, zoom ranges, source refs, build recipe refs, attribution, stale policy | `DENY` release |
| **Release gate** | `PromotionDecision`, `MapReleaseManifest`, prior release, rollback target, cache invalidation plan | no publication |
| **UI gate** | Evidence Drawer payload, trust badges, withheld counts, negative states, correction state | no public shell exposure |
| **AI/Focus gate** | released evidence context only; finite outcome; citation validation; receipt | `ABSTAIN`, `DENY`, or `ERROR` |
| **Accessibility gate** | keyboard navigation, focus order, non-color cues, contrast, reduced-motion behavior | block public release |
| **Rollback gate** | previous release can be restored without deleting correction history | block publication |

---

## Quickstart

Use this after mounting the real repository. These commands are discovery and verification steps, not proof that any path exists.

```bash
# 1. Confirm repository state.
git status --short
git branch --show-current

# 2. Inventory likely architecture, schema, policy, test, and release homes.
find docs schemas contracts policy tests data release .github -maxdepth 4 -type f 2>/dev/null | sort

# 3. Look for existing tile, MapLibre, manifest, and release vocabulary.
grep -RInE "TileArtifactManifest|LayerManifest|StyleManifest|MapReleaseManifest|PMTiles|MVT|MapLibre|EvidenceDrawerPayload" \
  docs schemas contracts policy tests data release 2>/dev/null || true

# 4. Verify whether schema authority is already established.
find schemas contracts -maxdepth 5 -type f 2>/dev/null | sort

# 5. Run repo-native validation only after the package manager and test runner are confirmed.
# Examples below are placeholders; replace with repo-native commands.
# npm test
# pnpm test
# pytest
# make test
```

> [!CAUTION]
> Do not generate or publish tiles from live sources until source descriptors, rights, sensitivity policy, schema validation, and promotion dry-run fixtures exist.

---

## Illustrative contract sketch

This is a shape sketch, not a production schema.

```json
{
  "schema": "kfm.map.tile_artifact_manifest.v1",
  "tile_artifact_id": "tileartifact_huc12_pmtiles_v1",
  "format": "PMTiles",
  "release_candidate_id": "maprelease_candidate_2026_04_huc12_demo",
  "source_refs": ["source_usgs_wbd_huc12_demo"],
  "evidence_bundle_refs": ["bundle_huc12_fixture_001"],
  "artifact_uri": "published/map/hydrology/huc12/demo.pmtiles",
  "sha256": "sha256:<hash>",
  "bounds": [-102.1, 36.9, -94.5, 40.1],
  "minzoom": 0,
  "maxzoom": 12,
  "time_scope": {
    "valid_time": "2024-01-01/..",
    "source_publication_time": "TODO-NEEDS-VERIFICATION",
    "release_time": "TODO-NEEDS-VERIFICATION"
  },
  "policy": {
    "public_safe": true,
    "sensitive_exact_geometry_allowed": false,
    "withheld_accounting_required": true,
    "stale_policy": "visible_badge_and_focus_abstain"
  },
  "build": {
    "recipe_ref": "TODO-NEEDS-VERIFICATION",
    "tool_versions": [],
    "input_hashes": []
  },
  "rollback": {
    "previous_release_id": "TODO-NEEDS-VERIFICATION",
    "cache_invalidation_required": true
  }
}
```

---

## Usage rules

### Public shell

Public map surfaces may load only released, manifest-bound tile artifacts and supporting style assets.

They must not:

- request RAW, WORK, QUARANTINE, canonical, proof-pack, review-only, steward-only, or model-runtime stores directly;
- treat tile properties as citation authority;
- expose exact restricted geometry;
- hide stale, denied, restricted, generalized, or withdrawn states;
- detach exports from release ID, citations, policy state, and correction lineage.

### Review shell

Reviewer and steward surfaces may inspect more context only through role-gated governed APIs.

They must still:

- log review state changes;
- preserve separation between review state and public release state;
- carry source role, evidence support, and sensitivity posture;
- avoid silently upgrading candidate geometry or model output into truth.

### Focus Mode

Focus Mode may explain tile-selected features only after the selected candidate resolves to admissible evidence.

Allowed finite outcomes:

| Outcome | Meaning |
|---|---|
| `ANSWER` | Evidence and policy support a bounded cited answer. |
| `ABSTAIN` | Evidence is missing, stale, conflicted, incomplete, or not release-eligible. |
| `DENY` | Policy blocks the request or output. |
| `ERROR` | Runtime or validation failure occurred and must be visible. |

---

## Definition of done

A tile-delivery change is not done until every applicable item passes.

- [ ] Repo conventions inspected and recorded.
- [ ] Schema-home and contract-home ambiguity resolved or explicitly deferred by ADR.
- [ ] Source descriptors exist for every source family used by the tile artifact.
- [ ] Tile artifact has manifest identity, hash, bounds, zoom range, source refs, policy posture, and rollback target.
- [ ] Layer and style manifests bind the artifact without turning style expressions into truth claims.
- [ ] Evidence Drawer payload resolves every consequential selected feature to `EvidenceBundle` or visible negative state.
- [ ] Sensitive geometry policy fails closed.
- [ ] Stale source policy is visible in UI and causes Focus Mode abstention where required.
- [ ] Public clients cannot reach raw, work, quarantine, canonical, proof-pack, steward-only, or model-runtime paths.
- [ ] Release manifest includes prior release and cache invalidation plan.
- [ ] Rollback restores the previous release without erasing correction history.
- [ ] Accessibility smoke checks pass for keyboard, focus order, contrast, non-color cues, and reduced motion.
- [ ] Documentation, schemas, fixtures, policies, and tests update in the same PR as behavior changes.

[Back to top](#kfm-tile-delivery-architecture)

---

## Verification backlog

| Item | Label | Why it matters |
|---|---|---|
| Confirm whether `docs/architecture/tiles/README.md` already exists | `NEEDS VERIFICATION` | Prevents overwriting stable anchors or strong existing substance. |
| Confirm owners / CODEOWNERS | `NEEDS VERIFICATION` | Required for governance and review routing. |
| Confirm schema authority: `schemas/` vs `contracts/` vs another home | `NEEDS VERIFICATION` | Avoids parallel machine-contract definitions. |
| Confirm package manager and test runner | `UNKNOWN` | Validation commands must be repo-native. |
| Confirm MapLibre architecture doc path | `UNKNOWN` | This README should link to the real renderer-boundary doc. |
| Confirm policy engine and path | `UNKNOWN` | Rego/OPA, Conftest, or repo-native policy tooling must be known before policy claims. |
| Confirm release artifact storage | `UNKNOWN` | Tile manifest paths and rollback records depend on repo convention. |
| Confirm current source-rights vocabulary | `NEEDS VERIFICATION` | Public release must fail closed on unresolved rights. |
| Confirm sensitive geometry categories and transforms | `NEEDS VERIFICATION` | Public tiles must not leak restricted locations. |
| Confirm whether PMTiles, Martin, COG, or MVT tooling is already adopted | `UNKNOWN` | Prevents tool duplication and undocumented dependency drift. |

---

## FAQ

### Are tiles authoritative?

No. Tiles are delivery artifacts. They can carry feature IDs and public-safe attributes, but consequential claims resolve through governed APIs to EvidenceBundles, citations, source roles, policy state, review state, and release state.

### Can a public popup show claims?

Only lightweight, non-authoritative summaries should appear directly in popups. Consequential text should open or resolve through the Evidence Drawer.

### Why not use one format for everything?

KFM has different evidence burdens. Dense public vector cartography, immutable snapshots, dynamic steward-mediated tiles, large rasters, and small fixture overlays have different risks and operational needs.

### Can client-side filters enforce policy?

Not for consequential or sensitive data. Backend policy and released artifact design must prevent leakage before the browser receives data.

### When is PMTiles appropriate?

Use PMTiles for stable, public-safe, immutable or offline bundles when a manifest records hash, source refs, release ID, attribution, stale posture, and rollback target.

### When is Martin or another server-mediated path appropriate?

Use server-mediated serving when freshness, role-based access, steward review, or PostGIS-backed slicing requires backend control.

---

<details>
<summary>Appendix A — Glossary</summary>

| Term | KFM meaning |
|---|---|
| **Tile artifact** | Rebuildable map-delivery product such as MVT, PMTiles, raster tiles, MBTiles, or a COG-backed view. |
| **TileArtifactManifest** | Machine-readable record describing tile artifact identity, source refs, hashes, bounds, zooms, policy posture, and rollback. |
| **LayerManifest** | Record binding a layer ID to domain, release, tile artifacts, geometry policy, interaction posture, and Evidence Drawer contract. |
| **StyleManifest** | Record binding style JSON, sprites, glyphs, fonts, accessibility notes, and layer meaning to a release-aware artifact. |
| **MapReleaseManifest** | Release record for map artifacts, including promoted layers/styles/tiles, previous release, cache invalidation, and rollback. |
| **EvidenceBundle** | Evidence-resolving object that outranks generated language and rendered pixels. |
| **Evidence Drawer** | Trust surface that exposes evidence, citations, policy state, transforms, withheld counts, and correction lineage. |
| **Focus Mode** | Evidence-bounded AI surface with finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. |
| **Public-safe** | Passed rights, sensitivity, review, source-role, geometry, and release checks for intended audience. |
| **Withheld accounting** | Count or explanation of restricted/suppressed features without exposing sensitive details. |
| **Derived artifact** | Rebuildable product downstream of canonical evidence, such as tiles, search views, graph projections, summaries, and scenes. |

</details>

<details>
<summary>Appendix B — Anti-patterns to reject</summary>

- Treating PMTiles, MVT, raster tiles, or style JSON as canonical truth.
- Letting MapLibre feature properties become citation authority.
- Shipping a public tile bundle before source rights and sensitivity posture are known.
- Using browser-only filtering to hide restricted features.
- Building live connectors before source descriptors and validation fixtures.
- Publishing tiles without a prior release and rollback target.
- Making style edits that change meaning without manifest and release review.
- Letting Focus Mode answer from tile attributes alone.
- Using unpinned sprites, glyphs, fonts, plugins, or external URLs in production.
- Creating duplicate schema homes because the existing repo convention was not inspected.

</details>

<details>
<summary>Appendix C — Maintainer pre-publish checklist</summary>

- [ ] Badges present.
- [ ] Owners field reviewed.
- [ ] Status reviewed.
- [ ] Quick jumps work.
- [ ] Required README minimums included: title, purpose, repo fit, inputs, exclusions.
- [ ] Directory tree included.
- [ ] Mermaid diagram renders in GitHub.
- [ ] Tables clarify object families, gates, and delivery posture.
- [ ] Code fences are language-tagged.
- [ ] Long reference material wrapped in `<details>`.
- [ ] Adjacent relative links verified or intentionally left as path placeholders.
- [ ] KFM Meta Block v2 values reviewed and synchronized with title and role.
- [ ] No claim implies current implementation depth without repo evidence.
- [ ] No public tile path bypasses governed APIs, release manifests, or EvidenceBundle resolution.

</details>

[Back to top](#kfm-tile-delivery-architecture)
