# artifacts/build/pdf

Compiled PDF outputs belong here while they are being staged for digesting and citation.

Expected generated file shapes:

- `<doc-id>.pdf` for a compiled, linearized PDF/A-2u output.
- `<doc-id>.digest.json` for the accompanying `ARTIFACT_DIGEST` sidecar when the build pipeline emits one here.

Do not place source Markdown, receipts, proofs, evidence bundles, release manifests, or published copies here. A PDF staged here becomes trust-bearing only when a canonical receipt or release manifest cites its digest.
