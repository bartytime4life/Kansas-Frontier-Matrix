# `ThreeDAdmissionDecision` fixtures

This directory contains one deterministic, fixture-only manifest for the inactive 3D admission candidate profile.

## Exact polarity

| Outcome | Count |
|---|---:|
| `ALLOW_RENDER_CANDIDATE` | 2 |
| `ABSTAIN` | 1 |
| `DENY` | 14 |
| `ERROR` | 1 |

The two allow candidates cover one native terrain request and one OGC 3D Tiles request with a complete plugin declaration. Negative cases exercise explanatory burden, 2.5D/true-3D labeling, sensitivity, Reality Boundary Note, 2D trust parity, plugin admission, and authority overclaim boundaries.

All identifiers and geometry posture fields are synthetic. The validator assigns `spec_hash` and `decision_id` after mutation, except for the intentional identity-corruption case.
