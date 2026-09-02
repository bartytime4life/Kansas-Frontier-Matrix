# RecompileManifest fixture family

This fixture family tests one in-memory JSON recompilation over the existing fixture-only `QueryRunRecord` and `AIChangeProposal` contracts.

- `query_ready.json` binds the approved fixture proposal under complete declared evidence.
- `query_unbound.json` is a valid query record that references a different proposal ID.
- `expected_candidate.json` is the exact canonical object produced from the shared proposal subject.
- `expected_manifest.json` is the exact deterministic manifest for the valid compile timestamp.
- `cases.json` covers successful compilation, a forbidden `PUBLISHED` target, an unbound proposal, and an unreadable subject.
- `invalid_manifest_cases.json` covers manifest hash, manifest ID, and rollback-binding drift.

All data are synthetic. A successful fixture run proves no real review, evidence resolution, policy decision, repository mutation, release, or publication.
