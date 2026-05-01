# EBIRD Layer 33 Audit Response

Layer 33 adds local/offline audit intake and response workflows.

- Intake CLI: `kfm-ebird-audit-intake`
- Response CLI: `kfm-ebird-audit-response`

## Safety
- No network calls.
- No credentials.
- No real eBird observations or exact coordinates.
- Public outputs are aggregate-only and must keep `exact_points: restricted`.
- Responses are governance/public-safety status updates only, not ecological inference.

## ID recipes
`audit_intake_id` and `audit_response_id` are deterministic SHA-256 prefixes over canonical JSON payloads of inputs and decision metadata.

## Contracts
Artifacts include intake manifest, verifier queue, classification report, evidence index, response plan, response packet, closure receipt, and public notice/status index.
