# Hydrology Source Registry Guide

## Source families in scope
- WBD/HUC boundaries
- NHDPlus HR hydrography
- USGS Water Data / NWIS observations
- FEMA NFHL regulatory context
- 3DEP/DEM terrain inputs

## Descriptor minimums
Each descriptor should include:
- `source_role`
- steward/owner
- cadence
- rights/license posture
- URL/access method
- parser/schema version
- activation state

## Role enforcement
- NFHL must map to `flood_context` role.
- Observational roles require timestamp + unit + qualifier semantics.
- Inactive descriptors must not run in production workflows.
