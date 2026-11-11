# Mirror React Flight dependency correction — November 11, 2026

GitHub Dependabot alert [143](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/143)
identifies `react-server-dom-webpack` 19.2.8 in this mirror lockfile. The current
[upstream advisory GHSA-xqc2-xf4c-x3h3](https://github.com/advisories/GHSA-xqc2-xf4c-x3h3)
marks that release affected and 19.2.9 patched. The advisory concerns rare RSC
responses combining multiple typed arrays and an attacker-controlled value.
This change applies the upstream dependency mitigation without claiming a
reproduced application exploit or a deployed-runtime inventory.

React, React DOM and RSC move together to 19.2.9 for peer compatibility. Only
those three package entries and root declarations change in the lock; npm
supplies their registry metadata/integrity. Framework versions, vendored
archives, other dependency records and existing overrides remain intact.
The generated RSC and SSR bundles both select the direct codec and exclude
the plugin and Next fallback copies. Those unselected copies are not updated.

## Evidence and limits

The harmless transport checks adapt the public composition's existing
`react-flight-transport.test.mjs` raw-codec cases to this mirror. Separate
production-mode processes encode and decode ordinary typed arrays; no RCE
payload, network provider, private record or model is exercised. On 19.2.8,
the two distinct-full-buffer-view refusal checks fail while four legitimate
controls pass. On 19.2.9, all seven checks pass, including the emitted-bundle
selection check. Independent arrays, independent DataView, partial shared
views and repeated-reference identity remain valid. Node 24.11.1 was used.
Production build, TypeScript and the public-asset containment gate pass.
The focused React, minimatch, Vite and security-boundary suites pass 17 tests.
Mirror QA passes 76 tests; current parity binds 941 files with all 262 withheld
carriers absent. Historical minimatch and replay receipts are hash-pinned; their
recorded package hashes are not compared to newer dependency bytes. No receipt
predecessor was changed. These checks do not constitute the full Site or water
suite, a browser acceptance run or a comprehensive dependency audit.

This does not port the public composition's separate binary preload-wrapper
repair or certify every framework wrapper. It does not change public GoDaddy,
native Staging or installed PC dependencies. Alert disposition is left to
GitHub's subsequent scan of merged source; the task does not dismiss it.

## Mirror lineage and rollback

The append-only React security receipt succeeds the November 10 replay-record
receipt, binding only these dependencies, this document and the transport test.
Historical receipts, original source identity, all 262 withheld carriers,
canonical mappings, review-pending and false hosted-equivalence declarations
are preserved. Content parity is not source approval, activation or deployment.
Existing `apps/site/source` implementation/test/docs, `data/receipts/generated`
evidence and `tools/qa`/`tests/qa` validation responsibilities own the changes
under Directory Rules and ADR-0029. No new authority root is introduced.

Revert the dependency/test/document, successor selector and corresponding QA
change together to restore the prior source inventory, retaining both receipts.
No database, service or stored-data migration was performed. Public publication
remains on hold; merging source would not update any installed runtime here.
