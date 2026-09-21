# Displaying a stale governed layer state

This static walkthrough shows how a viewer could present an upstream `ABSTAIN` and `STALE` state. The map style does not decide freshness, policy, evidence, or release. The example contains no real feature geometry, tile URL, source endpoint, or production style payload.

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: synthetic_only
expected_outcome: ABSTAIN
operational_home: apps/explorer-web/ and governed runtime
validation_boundary: JSON snippet parsing and relative-link checks; no browser or accessibility execution
correction_trigger: trust-state, runtime-envelope, accessibility, or style contract change
```

## Toy presentation input

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/viewer-styles/stale-layer-001",
  "feature_ref": "kfm://example/feature/synthetic-stale-001",
  "governed_state_input": {
    "outcome": "ABSTAIN",
    "trust_state": "STALE",
    "reason": "synthetic_source_currentness_unresolved"
  },
  "presentation": {
    "visible_label": "Stale context — no current answer",
    "icon_label": "clock",
    "pattern_label": "diagonal hatch",
    "color_token": "warning"
  }
}
```

This is a teaching object, not a MapLibre style, layer manifest, policy decision, or runtime envelope. The `ABSTAIN` outcome and `STALE` state are assumed inputs from a governed surface; changing color, opacity, or zoom cannot make data admissible or public-safe.

## Expected display behavior

| Input | Visible treatment | Boundary |
|---|---|---|
| `STALE` with `ABSTAIN` | Text label, clock icon, and hatch pattern; color is supplementary | A reader can identify the state without color alone. |
| Keyboard focus | State label remains in focus order | This document does not prove browser behavior. |
| Feature selection | Offer a route to governed evidence or a reason explanation | Selection itself is not evidence. |

The [Map Shell architecture](../../docs/architecture/map-shell.md) and [Explorer Web app](../../apps/explorer-web/README.md) own implementation. The [DecisionEnvelope contract](../../contracts/runtime/decision_envelope.md) owns finite runtime outcomes. If those contracts change, update or retire this example; promoting it to a real style requires implementation, accessibility, test, and release review.
