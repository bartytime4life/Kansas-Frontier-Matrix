# Evidence Drawer Payloads

Defines payload requirements for trust-visible claim drill-through.

## Required fields
- Claim id, statement, scope, and knowledge character.
- Source chips (role, date, steward, rights summary).
- EvidenceBundle references and proof links.
- Limitations, uncertainty, correction/rollback state.

## Rendering rules
- Missing required evidence => abstain-safe UI state.
- Sensitive records show transformed/public-safe context only.
