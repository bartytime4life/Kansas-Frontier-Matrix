# connectors_core connector descriptor gate

## Status

**PROPOSED internal implementation; read-only; not a SourceDescriptor registry, rights decision, or activation.**

`descriptor_gate.py` reads a connector-local `connectors/<source>/src/<pkg>/descriptor.yaml` (`name`, `role`, `rights`, `sensitivity_floor`) strictly. It reports the blockers that keep that connector's candidate routes at `HOLD`.

## Behavior

- **`load_descriptor(path)`:** accepts only flat `key: value` lines and comments. It returns `{}` for an unreadable, oversized (over 16 KiB) or undecodable file, and for one with unknown keys, duplicate keys, indentation, or nested structure.
- **`descriptor_blockers(descriptor, name=...)`:** returns `DESCRIPTOR_INVALID` when the name does not match. Otherwise it returns `DESCRIPTOR_ROLE_UNRESOLVED` and/or `DESCRIPTOR_RIGHTS_UNRESOLVED` for each field whose value, after folding case, whitespace, hyphens, underscores and quotes, is empty, `TBD`, `UNKNOWN`, `NEEDS_VERIFICATION`, `PROPOSED`, or `OWNER_TBD`.
- **`sensitivity_floor_blockers(descriptor)`:** for sources whose records may be sensitive (GBIF, iNaturalist). It returns `DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED` unless `sensitivity_floor` is one of the non-public SourceDescriptor enum values `generalized`, `restricted` or `quarantine`, after the same normalization. A public, unresolved, unknown or misspelled floor therefore cannot authorize a candidate route.
- **Guard test:** `test_only_deliberately_resolved_connector_descriptors_open_routes` fails unless the checked-in connector descriptors that open a candidate route are exactly those listed in `OPENED_CONNECTORS`. Resolving role or rights is a steward decision, so that list must be updated deliberately in the same change. Since 2026-09-28 it lists the seven U.S. federal connectors (BLM, Census, EPA, FEMA, NOAA, NRCS, USGS).

## Validation

```bash
python -m pytest tests/packages/connectors_core/test_descriptor_gate.py -q --strict-config --strict-markers
```

## Rollback

Revert the module together with the connector `admit.py` modules that import it.
