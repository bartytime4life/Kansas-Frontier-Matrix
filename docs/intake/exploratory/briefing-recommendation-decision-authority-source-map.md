# Briefing recommendation-decision authority source map

Status: **PROPOSED**
Scope: evidence map for an inactive, fixture-only assessment candidate

## Source claims

| Claim | Truth label | Evidence |
|---|---|---|
| A `Recommendation` is advisory or staff guidance supported by evidence; it does not imply binding adoption or implementation. | CONFIRMED | `KFM_Briefing_to_System_Integration_Architecture.docx`, sections 15.1–15.3; Google Drive file `1UnJ3dl9ZFvWHM01pYnqdoh0OOWinSFUg` |
| A `Decision` is a formal authority action; it does not imply execution or completion. | CONFIRMED | Same briefing, sections 15.1–15.3 |
| Recommendation, decision, implementation, completion, and measured outcome must remain separate objects or transitions. | CONFIRMED | Same briefing, required governance-event transition sequence |
| Accepted directory governance assigns contracts to meaning, schemas to shape, fixtures to examples, validators to deterministic checks, tests to behavior, workflows to orchestration, intake docs to source adaptation, and receipts to generated process memory. | CONFIRMED | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`; `docs/doctrine/directory-rules.md` |

## Repository assay at base `7d3b894deeb82d3ecb0ddf3daeec9158f266edb1`

The current `GovernanceEvent` profile already provides separate
`recommendation_refs`, `decision_refs`, `implementation_refs`, and
`outcome_observation_refs`. This proposal does not replace any of those object
families. It fills the next sourced idea in
`docs/intake/exploratory/briefing-governance-event-source-map.md`: a bounded
assessment that proves advisory recommendation evidence is not silently
collapsed into binding decision evidence.

Searches across governance and policy contracts, schemas, validators, tests,
workflows, exploratory source maps, domain-specific planning artifacts, and
open pull requests found no common assessment with this exact advisory-versus-
binding boundary. Domain-specific recommendation objects remain authoritative
in their domains.

## Implemented proposal

The packet adds one meaning contract, one closed Draft 2020-12 schema, one
synthetic exact-polarity fixture matrix, one deterministic no-network validator,
focused tests, one read-only workflow, this source map, and one generated
authorship receipt.

The assessment allows explicit dispositions for no recorded decision, adoption
as recommended, adoption with changes, rejection, deferral, and unresolved
status. Adoption with changes requires a comparison digest. Implementation and
outcome references may be linked only as separate downstream objects; all
authority and lifecycle effects remain false.

## Explicit non-goals

- No recommendation authoring, approval, or endorsement engine.
- No authority registry lookup or binding-decision authentication.
- No policy evaluation, workflow execution, implementation tracking, or outcome
  measurement.
- No database migration, source activation, release, publication, API, or UI.
- No mutation of the umbrella `GovernanceEvent` or domain-specific contracts.

## Activation gates

Activation requires an accepted ADR, named governance owner, authoritative
decision-instrument registry, policy and legal review, migration and rollback
plan, representative non-sensitive fixtures, and explicit human approval.
Until then, every artifact remains proposed or fixture-confirmed only.
