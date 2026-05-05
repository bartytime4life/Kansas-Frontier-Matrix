# Geology & Natural Resources Verification Backlog

Open verification tasks required to move this lane from draft scaffolding to implementation-backed documentation.

| ID | Task | Why it matters | Owner | Closure artifact | Status |
| --- | --- | --- | --- | --- | --- |
| GEO-001 | Confirm canonical lane slug and alias policy (`geology-natural-resources` vs `geology`). | Prevents split authority and duplicate docs/schemas. | TBD | ADR decision record | Open |
| GEO-002 | Confirm canonical schema home for geology contracts. | Prevents contract drift across directories. | TBD | ADR + schema index update | Open |
| GEO-003 | Identify verified source-of-record set for KGS/KDHE/KCC/USGS families. | Ensures source roles and claim boundaries are defensible. | TBD | Source registry entries + fixtures | Open |
| GEO-004 | Define public-safe rules for borehole/sample/resource coordinates. | Prevents accidental restricted-location leakage. | TBD | Policy tests + redaction/generalization fixtures | Open |
| GEO-005 | Confirm governed API route and evidence envelope path for geology surfaces. | Prevents docs from inventing runtime interface names. | TBD | Runtime reference note + tests | Open |
| GEO-006 | Confirm web shell component paths for geology layer rendering and drawer use. | Aligns docs with actual UI implementation. | TBD | UI reference note + screenshot/test where applicable | Open |
| GEO-007 | Establish accepted resource classification scheme set. | Needed to separate occurrence vs reserve/resource claims. | TBD | Registry file + validator tests | Open |

## Backlog management

- Keep statuses in `Open`, `In Progress`, `Blocked`, or `Closed`.
- Link each closed item to a concrete artifact (ADR, test, fixture, policy diff, or release note).
