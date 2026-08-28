# MukeyProperties fixtures

Synthetic, no-network fixtures for `kfm.soil.mukey-properties.v1`.

## Boundary

These files are deterministic validator inputs only. They are not Kansas soil observations, NRCS source captures, EvidenceBundles, policy decisions, release candidates, or public products. Numeric values are invented solely to exercise component weighting, horizon continuity, physical ranges, hydric-status handling, and canonical hashing.

## Layout

```text
valid/    candidates expected to return PASS
invalid/  candidates expected to return a named code in the adjacent .expected_code.txt file
```

The validator requires nonempty valid and invalid lanes, rejects missing expectation sidecars, and never performs network access.

## Covered cases

- one- and two-component deterministic aggregation;
- component-percentage closure;
- horizon gaps and overlaps;
- derived-metric recomputation;
- canonical content-hash binding; and
- hydric `CURRENT` status without a criteria reference.

## Authority limit

A fixture pass proves only the proposed inactive shape and validator behavior. It does not activate SSURGO/SDA, resolve evidence, execute policy, promote, release, publish, or establish scientific fitness for use.
