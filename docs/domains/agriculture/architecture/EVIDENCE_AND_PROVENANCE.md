# Agriculture Evidence and Provenance

Agriculture claims must be reproducible to source-aligned evidence.

## EvidenceBundle requirements

Each bundle should include:

- claim target and claim scope (spatial + temporal + semantic);
- supporting evidence references and source roles;
- policy outcome and review status;
- uncertainty statement;
- generation metadata (run ID, contract version, policy version).

## Provenance requirements

- Preserve source keys through normalization and publication.
- Record product/version metadata for grid and derived products.
- Include immutable digests for publishable artifacts.
- Preserve correction lineage using supersession references.

## Public trust guardrails

- API/UI must resolve EvidenceBundle data before rendering consequential claims.
- Evidence Drawer payloads must expose source role and support class.
- Focus responses must abstain where evidence is missing or policy blocks disclosure.
