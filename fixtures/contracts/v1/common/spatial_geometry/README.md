# SpatialGeometry fixtures

Synthetic, public-safe cases for the bounded shared `SpatialGeometry` carrier
validator. The profile covers supported GeoJSON coordinate structures, explicit
EPSG identifiers, dimensional consistency, polygon closure and simple-ring
checks, and EPSG:4326 bounds.

These fixtures contain invented coordinates only. Passing them does not prove
source accuracy, survey authority, domain truth, rights or sensitivity
clearance, policy approval, release, publication, or public safety.

`cases.json` is the reviewed executable profile. Every case declares its exact
expected outcome and stable finding-code set. The validator must not echo
coordinate values in diagnostics.
