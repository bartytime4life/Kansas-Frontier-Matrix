# API and UI Notes

## Intended consumers
- governed API endpoints serving domain claims;
- Evidence Drawer payloads;
- Focus Mode summaries;
- map popup claim cards.

## Required payload traits
- finite outcome (`ANSWER`/`ABSTAIN`/`DENY`/`ERROR`);
- resolvable `evidence_bundle_ref`;
- policy decision reference and reason codes;
- sensitivity/rights/review posture;
- time scope and role-qualified source context.

## UI guardrails
- Show assessor facts as assessor facts, not title truth.
- Avoid rendering raw DNA detail on public surfaces.
- Show abstain/deny outcomes explicitly rather than fabricating narrative certainty.
- Include correction notices and supersession references when applicable.

## Focus Mode contract posture
Focus Mode must summarize only from released, policy-safe payloads. It should abstain when evidence resolution or policy posture is insufficient.
