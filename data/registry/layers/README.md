# Layer Registry
_Registry of governed **LayerConfig** records used to render **promoted DatasetVersions** (tiles + style + time + identify) in Map Explorer / Stories / Focus Mode._

**Status:** draft · **Owners:** TBD · **Policy:** public · **Schema:** `kfm_layer_config_version=v1`

**Quick nav:** [What lives here](#what-lives-here) · [How it’s used](#how-its-used) · [Directory layout](#directory-layout) · [LayerConfig schema](#layerconfig-schema-v1) · [Governance invariants](#governance-invariants) · [Add or update a layer](#add-or-update-a-layer) · [CI gates](#ci-gates) · [Appendix: MetaBlock](#appendix-metablock)

---

## What lives here

This folder contains **LayerConfig** records: small, machine-readable JSON documents that connect:

- a **promoted DatasetVersion** (`dataset_slug` + `dataset_version_id`)
- to a **map-renderable delivery artifact** (e.g., PMTiles)
- with **declarative style**, **time mapping**, and **identify/evidence hooks**
- while carrying an explicit **policy label** and **attribution**

A LayerConfig is the contract between the **catalog world** (DCAT/STAC/PROV) and the **map world** (Map Explorer / Story Nodes). It is intentionally small so it can be served, audited, and cached safely.

> **NOTE**
> This registry stores *configuration*, not bulk data. Tile/COG artifacts live in their respective promoted artifact locations and are referenced by `delivery.href` + `delivery.digest`.

---

## How it’s used

```mermaid
flowchart LR
  DV[Promoted DatasetVersion<br/>DCAT + STAC + PROV] --> LC[LayerConfig<br/>(this registry)]
  LC --> API[Governed APIs<br/>catalog + tiles]
  API --> UI[Map Explorer / Stories / Focus Mode]
  UI --> ER[Evidence Resolver<br/>resolve EvidenceRef]
  ER --> UI
```

Key idea: **map state is reproducible**. Stories store map state (camera, layers, time, filters) so the view can be replayed later, and Focus Mode can answer with the same context. Layer configs must support that reproducibility.

---

## Directory layout

Suggested (version-preserving) layout:

```text
data/registry/layers/
  README.md

  # One config per (layer_id, dataset_version_id):
  <layer_id>__<dataset_version_id>.layer.json

  # Optional: generated index for UI discovery (if used by your stack)
  index.layers.json
```

Naming guidance:

- `layer_id` should be stable, short, and `snake_case`.
- `dataset_version_id` should match the promoted DatasetVersion ID (e.g., `YYYY-MM.<spec_hash>`).
- Preserve older layer configs so Story Nodes can replay historical views.

> **WARNING**
> Do not change promoted artifacts “in place.” If the DatasetVersion changes, produce a new DatasetVersion and add a new LayerConfig referencing it.

---

## Layer taxonomy

Use this lightweight taxonomy to keep the map coherent and to set expectations for review:

| Category | Typical use | Expected questions |
|---|---|---|
| Context | basemaps, terrain, hydrology | “Where am I?” |
| Reference | admin boundaries, grids | “What’s the frame of reference?” |
| Asset | roads, facilities, parcels | “What exists here?” |
| Sensor / Observation | measurements, stations | “What was observed?” |
| Condition / State | drought status, land cover | “What condition is it in?” |
| Event | incidents, storms, outbreaks | “What happened and when?” |
| Trend / History | change over time | “How is it changing?” |
| Forecast / Scenario | modeled futures | “What might happen?” |
| Indicator / Index | composites, indices | “What’s the score/level?” |
| Narrative overlay | story annotations | “What should I notice?” |

For any **new** layer, document (in the PR description at minimum):

- tile strategy (vector/raster, zoom range, expected load)
- symbology approach (legend + paint rules)
- how uncertainty is surfaced (if applicable)
- evidence mapping (how identify links to EvidenceRefs)

---

## LayerConfig schema (v1)

A LayerConfig is a JSON document with these minimum fields:

| Field | Required | Meaning |
|---|---:|---|
| `kfm_layer_config_version` | ✅ | Schema version string (e.g., `"v1"`) |
| `layer_id` | ✅ | Stable layer identifier used by map state / UI |
| `title` | ✅ | Human-friendly name shown in LayerPanel |
| `dataset_slug` | ✅ | Dataset slug for discovery + linking |
| `dataset_version_id` | ✅ | Promoted DatasetVersion ID |
| `policy_label` | ✅ | Policy label (controlled vocabulary) |
| `delivery` | ✅ | How the map client fetches render assets (e.g., PMTiles) |
| `style` | ✅ | Declarative style: legend + paint rules |
| `time` | ✅ | Time mapping strategy for filtering and timelines |
| `identify` | ✅ | Feature inspection settings (id field + optional evidence ref field) |
| `attribution` | ✅ | Attribution + license/rights display info |

### Controlled vocabulary: `policy_label`

Use only the approved policy labels:

- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

> **NOTE**
> Policy labels are not “decorative.” They affect discovery, tiles, exports, and what the evidence resolver is allowed to return.

### Example LayerConfig (illustrative)

```json
{
  "kfm_layer_config_version": "v1",
  "layer_id": "example_events",
  "title": "Example Events",
  "dataset_slug": "example_agency_events",
  "dataset_version_id": "2026-02.ef12ab34",
  "policy_label": "public",
  "delivery": {
    "type": "pmtiles",
    "href": "/assets/pmtiles/example_agency_events/2026-02.ef12ab34/events.pmtiles",
    "digest": "sha256:REPLACE_WITH_REAL_DIGEST"
  },
  "style": {
    "style_id": "kfm_default_points",
    "legend": [
      { "label": "Type A", "value": "A" },
      { "label": "Type B", "value": "B" }
    ],
    "paint_rules": [
      { "when": { "field": "event_type", "equals": "A" }, "symbol": "point" }
    ]
  },
  "time": {
    "type": "interval",
    "start_field": "start_time",
    "end_field": "end_time",
    "precision": "day"
  },
  "identify": {
    "enabled": true,
    "feature_id_field": "event_id",
    "evidence_ref_field": "evidence_ref"
  },
  "attribution": {
    "text": "Example Agency Events",
    "license": "See dataset catalogs for authoritative rights"
  }
}
```

---

## Governance invariants

These rules are “hard” because they preserve reproducibility and safety:

1. **Only promoted DatasetVersions**
   - Layer configs must reference DatasetVersions that have passed promotion gates and are in a publishable state.

2. **Policy label must match the promoted data**
   - The `policy_label` must be consistent with the DatasetVersion’s policy label.

3. **Sensitive location handling**
   - If a dataset is `restricted_sensitive_location`, do not publish precise geometry. Publish only generalized derivatives when approved, and use the appropriate `policy_label` (commonly `public_generalized`).

4. **Identify must not bypass evidence**
   - If `identify.enabled=true`, prefer `evidence_ref_field` so the UI can open the Evidence Drawer via the evidence resolver rather than embedding raw “proof” blobs in the client.

5. **Map state must remain safe**
   - Filters and parameters exposed to the UI must not allow access to hidden restricted fields.

---

## Add or update a layer

### Add a new layer (checklist)

- [ ] Pick a **stable** `layer_id` (don’t encode dates; versions are handled by `dataset_version_id`).
- [ ] Confirm the **DatasetVersion is promoted** and its catalogs are valid.
- [ ] Create a new `*.layer.json` file following the v1 schema.
- [ ] Set `policy_label` using the controlled vocabulary.
- [ ] Populate `delivery.href` and `delivery.digest` for the promoted render artifact.
- [ ] Define `style.legend` and `style.paint_rules` (declarative; no code execution).
- [ ] Define `time` mapping (instant vs interval; field names must exist in the delivered data).
- [ ] Configure `identify` fields (ensure `feature_id_field` exists; prefer `evidence_ref_field`).
- [ ] Add/refresh `index.layers.json` if your build uses it.
- [ ] Ensure CI gates pass (schema + policy + link/evidence checks).

### Update an existing layer for a new DatasetVersion

- Add a **new** LayerConfig file for the new `dataset_version_id`.
- Keep older configs to preserve Story Node replayability.

---

## CI gates

Minimum expectations for merges that add/change LayerConfigs:

- **Schema validation**: LayerConfig JSON validates against the v1 schema.
- **Controlled vocab validation**: `policy_label` must be allowed.
- **Link + digest checks**: `delivery.href` exists (in the publish target) and digest format is correct.
- **Policy tests**: default-deny posture remains intact; fixture tests pass.
- **Evidence resolvability** (when applicable): Story publishing should fail if citations / EvidenceRefs can’t be resolved by the evidence resolver.

---

## Appendix: MetaBlock

<details>
<summary>KFM MetaBlock v2 (for this README)</summary>

[KFM_META_BLOCK_V2]
doc_id: kfm://doc/5c9c1c4a-4f66-4f2c-85a6-69f9d3c0a1f2
title: Layer Registry README
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related: []
tags:
  - kfm
  - registry
  - layers
notes:
  - Governs LayerConfig records used by Map Explorer / Stories.
[/KFM_META_BLOCK_V2]

</details>

---

_Back to top:_ [Layer Registry](#layer-registry)
