# PMTiles Validators

Fail-closed validation helpers for KFM PMTiles publication gates.

These tools inspect derived tile artifacts and sidecars. They do not decide public truth, mutate canonical records, or replace policy review.

## Tools

| Tool | Purpose |
|---|---|
| `validate_header.py` | Checks PMTiles header/metadata expectations and required `spec_hash`. |
| `verify_merkle.py` | Checks `.pmidx` schema, PMTiles digest, and Merkle root. |

## Expected Inputs

```text
tiles.pmtiles
tiles.pmtiles.pmidx
tiles.pmtiles.pmsig
tiles.pmtiles.runreceipt.json
```

## Example

```bash
python tools/validators/pmtiles/validate_header.py path/to/tiles.pmtiles
python tools/validators/pmtiles/verify_merkle.py path/to/tiles.pmtiles.pmidx --pmtiles path/to/tiles.pmtiles
```

## Failure Posture

Any unknown, malformed, missing, or unresolved value exits non-zero. Publication gates should treat non-zero as DENY.
