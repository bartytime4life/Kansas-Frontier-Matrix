# EXAMPLE (Published) — Kansas Storm Events Overview (1950–2024)

## Summary

This published **Story Node v3** demonstrates how KFM binds a narrative to:
- a fixed **map state** (bbox, zoom, layers, time window), and
- **evidence references** (`dcat://`, `prov://`, etc.) that can be resolved via the evidence resolver.

**Scope:** Kansas (statewide)  
**Time window shown in map:** 1950-01-01 → 2024-12-31  
**Primary layer:** `noaa_storm_events` (dataset version `2026-02.abcd1234`)

> NOTE: This is an **example** story for templates/tests. Replace IDs and citations with real, resolvable
> references in production.

## Claims

1. **CONFIRMED:** This story references NOAA NCEI Storm Events dataset version `2026-02.abcd1234` as its primary layer source.  
   [CITATION: dcat://noaa_ncei_storm_events@2026-02.abcd1234]

2. **CONFIRMED:** The dataset version used by this story was produced by a recorded pipeline run, enabling reproducibility and audit.  
   [CITATION: prov://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234]

## Narrative

This story is intentionally simple: it is meant to show the minimum structure of a **published** Story Node.

Use the layer panel to confirm you are viewing `noaa_storm_events` at dataset version `2026-02.abcd1234`.  
[CITATION: dcat://noaa_ncei_storm_events@2026-02.abcd1234]

If you click any feature/event on the map, the UI should open an evidence drawer that resolves citations
through the evidence resolver.  
[CITATION: prov://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234]

## Evidence

- [CITATION: dcat://noaa_ncei_storm_events@2026-02.abcd1234]
- [CITATION: prov://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234]

---

## Sidecar JSON

In KFM, Story Node v3 metadata is stored as a **sidecar JSON** file alongside the markdown. This section
embeds an example payload for convenience.

```json
{
  "kfm_story_node_version": "v3",
  "story_id": "kfm://story/6f2b2b4e-28b5-4a73-8c1c-2d405ce9e1f0",
  "version_id": "v1",

  "status": "published",
  "policy_label": "public",
  "review_state": "approved",

  "map_state": {
    "bbox": [-102.0, 36.9, -94.6, 40.0],
    "zoom": 6,
    "layers": [
      { "layer_id": "noaa_storm_events", "dataset_version_id": "2026-02.abcd1234" }
    ],
    "time_window": { "start": "1950-01-01", "end": "2024-12-31" }
  },

  "citations": [
    { "ref": "dcat://noaa_ncei_storm_events@2026-02.abcd1234", "kind": "dcat" },
    { "ref": "prov://run/2026-02-20T12:34:56Z.noaa_ncei_storm_events.abcd1234", "kind": "prov" }
  ]
}
```

### Publication checklist (example)

- ✅ `status` is `published`
- ✅ `review_state` is set (value is illustrative; use your controlled vocabulary)
- ✅ all `[CITATION: ...]` refs appear in the **Evidence** section
- ✅ publishing gate: citations must resolve through the evidence resolver
