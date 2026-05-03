# AIR Candidate Re-entry Slice

## KFM Meta Block v2
- Doctrine: cite-or-abstain, evidence-first, fail-closed.
- Scope: fixture-backed, local-only, no-network candidate re-entry preparation.

This layer consumes maintenance roll-forward outputs, builds candidate re-entry artifacts, runs compatibility gates, records sunset review queue/decisions, issues candidate re-entry promotion decision, builds manifest/ledger/postcheck, and stays candidate-only.

No deploy, no publish, no notices, no route removal, no artifact deletion, no production baseline rotation, no production re-entry.

NowCast is operational evidence; validated AQS truth requires `24h_validated` and must never be conflated.

NEEDS_VERIFICATION: any live API serving, gateway deploy, CDN purge, DNS/cloud calls, production signatures, ticketing/IdP integrations, external archives, production maintenance/roll-forward/re-entry.
