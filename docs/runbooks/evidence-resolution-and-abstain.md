# Evidence Resolution and Abstain Runbook

## Rules
- If EvidenceRef resolves to EvidenceBundle and policy allows, return ANSWER.
- If evidence is missing, return ABSTAIN.
- If policy blocks, return DENY.
- If schema/resolver state is invalid, return ERROR.

## Why synthetic-only
- This runbook applies to synthetic fixtures only; live connectors remain PROPOSED/NEEDS VERIFICATION.
