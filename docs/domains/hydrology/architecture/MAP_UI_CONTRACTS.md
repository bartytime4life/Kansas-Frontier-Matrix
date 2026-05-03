# Hydrology Map & UI Contracts

## Map surface rules
- Map layers render from release manifests only.
- Layer metadata must include freshness and evidence references.
- Trust badge text should align with decision/proof state.

## Evidence Drawer minimum fields
- source role
- claim support summary
- limitations
- freshness/as-of
- correction/rollback state
- proof links (EvidenceBundle / catalog refs)

## Focus Mode behavior
Focus outputs are bounded by governed response envelope and must abstain when support is insufficient.
