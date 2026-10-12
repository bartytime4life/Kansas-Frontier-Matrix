# Consent-card projection fixtures

Synthetic, public-safe fixtures for the Explorer Web app-local profile
`kfm.explorer.consent-card.public-safe.v1`.

The profile is a narrow projection of already-resolved consent and obligation
state. It is not a consent credential, EvidenceBundle, PolicyDecision,
PolicyObligationSet, release record, or proof object.

## Lanes

- `valid/answer-viewer-choice.json` carries the four details the UI may show:
  basis, bounded scope, expiration, and separate subject-inclusion state.
- `valid/abstain-unresolved.json`, `valid/deny-policy.json`, and
  `valid/error-upstream.json` prove finite fail-closed states with no actionable
  details or override.
- `invalid/` proves rejection of unknown fields, empty answer scope,
  unresolved subject state on an answer, and outcome/reason mismatch.

All fixtures are synthetic. They contain no living-person record, genomic data,
protected geometry, live source, credential, actual consent, policy approval,
release authority, or publication authority.
