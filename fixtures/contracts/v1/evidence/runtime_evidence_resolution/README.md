# RuntimeEvidenceResolution fixtures

Synthetic, no-network examples for the PROPOSED internal result contract at:

```text
schemas/contracts/v1/evidence/runtime_evidence_resolution.schema.json
```

## Inventory

- `valid/resolved.json` — candidate closure passed; `bundle_id` is present and `issues` is empty.
- `valid/unresolved.json` — closure is incomplete; no bundle identity is exposed.
- `valid/denied.json` — caller-supplied policy context blocks the candidate.
- `valid/error.json` — safe evaluation failed.
- `invalid/resolved_without_bundle.json` — a resolved result cannot omit bundle identity.
- `invalid/nonresolved_with_bundle.json` — a blocked result cannot carry bundle identity.
- `invalid/authoritative_true.json` — this internal profile can never claim authority.
- `invalid/unknown_status.json` — unregistered outcome vocabulary fails closed.
- `invalid/empty_checks.json` — a result must state which checks ran.

These fixtures contain no source data, sensitive locations, release records, credentials, or public claims. Validation proves shape only; it does not prove evidence truth, policy clearance, review, release, publication, or runtime safety.
