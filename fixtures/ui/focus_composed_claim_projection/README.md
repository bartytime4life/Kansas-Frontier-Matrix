# Focus composed-claim projection fixtures

These synthetic, no-network fixtures exercise the app-local profile
`kfm.explorer.focus-composed-claim.public-safe.v1`.

They adapt the existing fixture-only `ComposedClaimDependencyClosureCandidate`
semantics into a browser-safe projection. They do not resolve live
`EvidenceRef`s, execute policy, invoke a model, authenticate review, establish
release state, or authorize publication.

| Fixture | Closure | Focus outcome |
|---|---|---|
| `valid/answer-supported.json` | `SUPPORTED` | `ANSWER` |
| `valid/answer-qualified.json` | `QUALIFIED` | `ANSWER` with explicit optional-role limitation |
| `valid/abstain-unresolved.json` | `ABSTAIN` | fixed no-leak `ABSTAIN` |
| `valid/deny-policy.json` | `DENY` | fixed no-leak `DENY` |

The browser feature must enforce request/claim identity, EvidenceRef subset
binding, citation-to-evidence closure, Evidence Drawer parity, finite outcome
consistency, and no-browser-model/no-lifecycle-store boundaries.
