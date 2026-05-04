# ADR-0002 PR-002 Evidence Closure (Supplemental)

## Status
Accepted (synthetic baseline hardening)

## Decision
Public hydrology claims must not be displayed, summarized, exported, or released unless evidence closure and governance gates pass.

## Consequences
- ABSTAIN for missing evidence.
- DENY for policy block.
- ERROR for invalid resolver/schema state.
- ANSWER only when closure and policy both pass.
