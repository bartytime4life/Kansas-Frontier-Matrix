# Browser Sigstore Verify Before Render

## KFM Meta Block V2
- doctrine: cite-or-abstain
- default: deny-by-default
- evidence precedence: evidence outranks generated language
- publication: governed state transition

This slice enforces browser-side artifact trust in a Web Worker before PMTiles/TileJSON render. The worker accepts a governed signed release manifest + expected digest and returns finite outcomes: `ALLOW_RENDER`, `DENY_RENDER`, `ABSTAIN`, `ERROR`.

Negative gates include missing bundle/signature, digest mismatch, stale trust root, unsupported identity, policy denial, and tamper indicators. Verification failures are fail-closed and block registration/fetch path for map render.

Evidence drawer integration receives only a receipt reference (`receipt_ref`) and does not receive Sigstore bundle internals.

Rollback/correction path: publish a corrected released manifest, re-sign with approved signer identity, and advance trust envelope pointer atomically.
