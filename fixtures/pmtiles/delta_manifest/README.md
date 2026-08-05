# Synthetic PMTiles Delta Manifest Fixtures

These no-network fixtures prove only the proposed delta-manifest shape, canonical hash, archive digest binding, per-tile lineage, coordinate/quadkey identity, count reconciliation, and declared QC outcome.

- `valid/`: a mixed add/modify/remove delta and a valid review-state delta.
- `invalid/`: one intentionally malformed shape proving fail-closed CLI polarity. Additional lineage, identity, count, QC, hash, reference, coordinate, and ordering cases are generated deterministically in the focused unit test.

All archives, tiles, receipts, source manifests, attestations, hashes, counts, and dates are synthetic. The fixtures do not verify an archive, signature, source, EvidenceBundle, policy decision, release, deployment, or publication.
