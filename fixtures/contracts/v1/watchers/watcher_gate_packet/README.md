# Watcher gate packet fixtures

These fixtures prove a deterministic, no-network `WatcherGatePacket` profile.
They do not query a source, execute policy, create a steward ticket, promote a
candidate, or publish an artifact.

## Valid lane

- `valid_green.json` — score and prefilter facts satisfy all reviewed fixture gates.
- `valid_amber.json` — missing ETag plus a 50–79 score routes steward review while preserving exit code 0.
- `valid_deny.json` — zero items, a missing asset, high median cloud, and a score below 50 fail closed with exit code 2.

## Invalid lane

The exact-negative manifest covers classification mismatch, exit-code mismatch,
self-hash mismatch, governance escalation, and noncanonical reason ordering.

```bash
python tools/validators/watchers/validate_watcher_gate_packet.py --fixtures
```
