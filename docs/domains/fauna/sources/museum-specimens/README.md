# Museum Specimens Source Notes

## Purpose
This folder documents the `museum-specimens` source family for the fauna domain and tracks readiness, rights, sensitivity, and validation expectations before any public-safe release.

## Current Status
- State: `PROPOSED / NEEDS VERIFICATION`
- Connector: Disabled
- Public exact sensitive geometry: Denied by default

## Required Before Activation
1. Source descriptor in `data/registry/fauna/` with authority scope and cadence.
2. Rights and redistribution review completed.
3. Geoprivacy controls verified against `docs/domains/fauna/GEOPRIVACY.md`.
4. Fixture-based validation added and passing.
5. Release review and rollback path documented.

## Notes
- This README is documentation only; it does not activate ingestion.
- Treat source claims as scoped inputs, not canonical legal truth.
