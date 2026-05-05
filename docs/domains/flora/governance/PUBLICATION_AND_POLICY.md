# Flora Publication and Policy

## Policy posture
Flora publication is fail-closed: unknown rights or unresolved sensitivity prevents public release.

## Required checks before publication
- Rights/license compatibility for intended exposure.
- Sensitivity class and geometry precision policy.
- Source role compatibility with claim type.
- EvidenceBundle resolvability.
- Review status and promotion authorization.
- Release manifest completeness and rollback readiness.

## Public geometry classes
| Class | Public behavior |
| --- | --- |
| `public_exact_allowed` | Exact geometry permitted only with explicit approval. |
| `public_generalized` | Publish generalized geometry with transform receipt. |
| `restricted_precise` | Never expose exact coordinates publicly. |
| `embargoed` | Delayed or suppressed until embargo conditions pass. |
| `steward_review_required` | Hold until explicit steward review. |

## Deny conditions
- Missing rights metadata.
- Unknown source role.
- Sensitive exact geometry without approved policy path.
- Broken provenance or evidence references.
