# Flora UI and Evidence Drawer

## Scope
Defines behavior expectations for map layers, evidence drawers, and Focus-like synthesis surfaces.

## Map layer expectations
- Show public-safe geometry only.
- Include trust metadata: source role, freshness, review state, and sensitivity class.
- Never treat style configuration as source truth.

## Evidence Drawer contract (human-level)
Each consequential claim should present:
- Claim summary.
- Linked EvidenceBundle references.
- Source role and rights posture.
- Sensitivity/redaction notes (if any).
- Decision outcome and reason code.

## Focus outcome contract
Focus responses should use finite outcomes:
- `ANSWER` when admissible evidence supports the response.
- `ABSTAIN` when scope/evidence is insufficient.
- `DENY` when policy disallows disclosure.
- `ERROR` when retrieval/validation fails.

## Prohibitions
- No direct RAW/WORK reads from UI runtime.
- No disclosure of restricted precise locations in public surfaces.
- No unsupported claims without evidence resolution.
