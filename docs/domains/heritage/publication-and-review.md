# Heritage Publication and Review Model

Scope: how heritage outputs are published across KFM surfaces while preserving trust-critical visibility, review state, and correction posture.

## Surface-by-surface publication rules

| Surface | Heritage output type | Trust-critical contents that must remain visible |
|---|---|---|
| Dossier | Structured summary of evidence-backed heritage context | Evidence links, uncertainty posture, rights/sensitivity class, correction state |
| Story surface | Narrative framing with bounded claims | Claim-to-source linkage, narrowing notes, abstain/deny handling |
| Evidence Drawer | Direct support inspection | Source locator, provenance, rights status, review/decision refs |
| Focus Mode | Governed synthesis over released scope | Citations, policy-bounded finite outcomes, response envelope state |
| Export | Release-scoped package | Manifest lineage, disclosure class, corrections/supersession metadata |
| Review / Stewardship | Restricted review interface | Decision records, reviewer actions, escalation notes, withheld rationale |

## Review gates

A publication candidate should fail closed if any of these remain unresolved:

- rights/reuse or quote-safety ambiguity
- sensitivity class and precision decision ambiguity
- missing claim-to-evidence linkage
- unresolved steward review requirement
- unresolved correction/supersession propagation

## Finite outcomes (runtime/publication)

- `ANSWER`: release-safe and evidence-resolvable.
- `ABSTAIN`: insufficient support, unresolved conflict, or incomplete evidence route.
- `DENY`: blocked by policy/rights/sensitivity constraints.
- `ERROR`: system failure to produce governed response.

## Lane-specific caution

Heritage lane is not equivalent to hydrology or other public-safe-first lanes.

- Heritage requires stronger default narrowing.
- Narrative surfaces must keep provenance and decision visibility foregrounded.
- Documentary interpretation remains subordinate to source and governance evidence.

## Correction posture

| Correction type | Required publication behavior |
|---|---|
| Supersession | mark prior output as superseded and link forward to correction notice |
| Withdrawal | remove from public-safe exposure and keep visible withdrawal rationale |
| Narrowing/generalization | visibly show that precision was reduced and why |
| Denial after review | preserve decision reason and non-public rationale path for stewards |

## Unknowns and verification flags

- **NEEDS VERIFICATION:** exact API/output contract fields used by current runtime surfaces.
- **UNKNOWN:** current CI checks that assert heritage-specific trust-critical visibility requirements.
- **PROPOSED:** lane-specific publication checklist in runbook form.

