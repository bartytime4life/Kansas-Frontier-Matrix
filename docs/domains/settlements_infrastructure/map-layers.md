# Settlements & Infrastructure Map Layers

Map delivery is a released derivative surface.

## Layer classes

| Layer class | Source family | Public precision rule |
|---|---|---|
| Settlement points/polygons | Municipal/census/historic boundaries | Generalize when sensitivity or uncertainty requires |
| Settlement status overlays | Legal/status event records | Time-scoped labels only when evidence-backed |
| Infrastructure assets | Public-safe asset representations | Hide or generalize restricted classes |
| Infrastructure networks | Corridor/service topology | Publish only policy-approved detail |
| Condition/observation overlays | Condition/service snapshots | Include observation time and source role |

## UI integration rules

- Layer cards link to Evidence Drawer payloads.
- Layer versions are tied to ReleaseManifest IDs.
- Map aliases are governed state transitions, not mutable pointers.
