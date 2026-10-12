# connectors_core artifact-handoff fixtures

This lane contains synthetic, public-safe context values for the internal retrieval-to-SourceArtifact handoff tests.

`valid_context.json` names only fixture references, non-secret request field names, an invented public rights snapshot, and non-placeholder parser/governance digests. It contains no source response bytes, live endpoint, credential, source activation decision, lifecycle record, authoritative receipt, evidence, policy, release, or public-use approval.

Payload bytes and transport observations remain inline in the focused deterministic tests so they cannot be mistaken for admitted source data.
