# Habitat land-cover materiality fixtures

Synthetic, no-network county land-cover comparisons for the inactive v1 profile.

- `valid/` exercises every shared outcome used by the adapter: unchanged,
  byte-only, semantic non-material, material by each trigger, and hold.
- `invalid/` proves fail-closed input handling for missing metrics, invalid area,
  placeholder digests, temporal inconsistency, noncanonical references, and
  unknown fields.

No fixture represents a real Kansas county, admitted source, public layer, policy
decision, release, or scientific threshold adoption.
