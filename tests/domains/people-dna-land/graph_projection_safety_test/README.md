# People/DNA/Land graph-projection safety test routing

Status: compatibility scaffold; no executable test is implemented in this directory.

`tests/domains/people-dna-land/graph_projection_safety_test/` currently contains only this README and `.gitkeep`. The previous one-byte body (`y`) did not explain the path, its maturity, or its relationship to the established graph test lane.

## Current routing

- The People/DNA/Land test boundary is documented by [`../README.md`](../README.md).
- The established graph test index is [`../graph/README.md`](../graph/README.md).
- Graph-safety documentation is maintained at [`../graph/safety/README.md`](../graph/safety/README.md).
- This underscore-and-suffix path is not a second graph-safety implementation home.

Do not add executable tests, fixtures, contracts, schemas, policy, graph data, or release artifacts here until a reviewed path decision establishes a distinct responsibility that cannot live in the existing `graph/safety/` lane. If a verified legacy consumer requires this path, add only the smallest compatibility shim and document that consumer and its rollback.

## Safety boundary

Any future graph-projection safety test must use deterministic, synthetic, no-network fixtures. Real or reconstructable living-person, genealogy, DNA/genomic, consent, private-land, title, address, relationship, or exact-location data is prohibited. Graph projections remain downstream carriers of governed assertions; a test pass cannot establish identity, kinship, consent, ownership, title, source authority, review, release, deployment, promotion, or publication.

## Validation and rollback

For this documentation-only repair, verify that the two established relative links resolve, the directory still contains no executable test, and the Markdown has one H1, a final newline, and no trailing whitespace.

Rollback by reverting this README to its prior blob. That restores the malformed placeholder without changing any test, fixture, policy, runtime, source, data, release, or public state.
