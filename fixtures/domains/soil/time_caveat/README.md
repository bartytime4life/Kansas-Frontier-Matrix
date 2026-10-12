# Soil time-caveat fixtures

Synthetic, no-network candidates for the inactive Soil time-caveat profile.

| Lane | Expected outcome | Purpose |
|---|---|---|
| `pass/` | `PASS` | Support role and required time axes are internally consistent. |
| `hold/` | `HOLD` | Candidate is shape-valid but temporally stale or incomplete. |
| `deny/` | `DENY` | Candidate collapses support roles or contradicts temporal state. |
| `error/` | `ERROR` | Candidate cannot be evaluated as a valid object. |

The fixtures contain no live source payload, precise station coordinate, private
data, release object, or published Soil claim.
