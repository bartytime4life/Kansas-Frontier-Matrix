# API Feature Query Example

This example demonstrates a minimal end-to-end feature query flow against a KFM-compatible API.

## Scenario

A client requests parcel features for a bounding box in Shawnee County, Kansas and receives policy-safe GeoJSON.

## Layout

- `kfm.example.yaml` — runnable metadata/config for this example.
- `src/` — request payload and helper snippets.
- `data/` — tiny synthetic input fixture.
- `evidence/` — sample policy/evidence records produced by the call.
- `outputs/` — expected response payload.

## Quick start

```bash
# inspect the example contract
cat examples/api-feature-query/kfm.example.yaml

# inspect expected API response
cat examples/api-feature-query/outputs/response.geojson
```
