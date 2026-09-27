# connectors_core connector descriptor gate

## Status

**PROPOSED internal implementation; read-only; not a SourceDescriptor registry, rights decision, or activation.**

`descriptor_gate.py` reads a connector-local `connectors/<source>/src/<pkg>/descriptor.yaml` (`name`, `role`, `rights`, `sensitivity_floor`) strictly. It reports the blockers that keep that connector's candidate routes at `HOLD`.

## Behavior

- **`load_descriptor(path)`:** accepts only flat `key: value` lines and comments. It returns `{}` for an unreadable, oversized (over 16 KiB) or undecodable file, and for one with unknown keys, duplicate keys, indentation, or nested structure.
- **`descriptor_blockers(descriptor, name=...)`:** returns `DESCRIPTOR_INVALID` when the name does not match. Otherwise it returns `DESCRIPTOR_ROLE_UNRESOLVED` and/or `DESCRIPTOR_RIGHTS_UNRESOLVED` for each field whose value, after folding case, whitespace, hyphens, underscores and quotes, is empty, `TBD`, `UNKNOWN`, `NEEDS_VERIFICATION`, `PROPOSED`, or `OWNER_TBD`.
- **Guard test:** `test_every_checked_in_connector_descriptor_still_holds` fails if any checked-in connector descriptor would open a candidate route. Resolving role or rights is a steward decision, so that test must be updated deliberately in the same change.

## Validation

```bash
python -m pytest tests/packages/connectors_core/test_descriptor_gate.py -q --strict-config --strict-markers
```

## Rollback

Revert the module together with the connector `admit.py` modules that import it.
