# release/candidates/habitat/habitat_fauna_thin_slice

## Purpose

This directory holds draft review notes for the habitat fauna thin-slice release candidate.

A candidate is not a release. It is a pre-release review packet used before a governed release decision.

## Directory boundary

- Keep candidate notes here.
- Keep data artifacts in the appropriate `data/` lifecycle directory.
- Keep final release manifests in the accepted release manifest lane.
- Keep schemas, contracts, and policy rules in their own authority roots.
- Keep habitat and fauna domain implementation work outside this release-candidate folder.

## Required review fields

- Candidate name and version
- Candidate owner
- Habitat scope
- Fauna scope
- Artifact pointer
- Proposed release target
- Source and evidence references
- Rights and policy status
- Validation summary
- Release handoff status
- Correction path
- Rollback or supersession path
- Steward decision

## Minimal candidate record

```markdown
# <candidate-name>

## Status
PROPOSED / READY_FOR_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED / DEFERRED / WITHDRAWN

## Candidate scope
<habitat and fauna thin-slice scope>

## Candidate artifact pointer
<data/processed/... or staging reference>

## Proposed published target
<data/published/... or release target>

## Evidence and source closure
<references and status>

## Validation summary
<summary and receipt reference>

## Decision
<decision and reason>
```

## Open verification

- [ ] Confirm CODEOWNERS for this path.
- [ ] Confirm thin-slice candidate naming convention.
- [ ] Confirm habitat scope and fauna scope.
- [ ] Confirm processed and published artifact paths.
- [ ] Confirm ReleaseManifest path or schema.
- [ ] Confirm correction and rollback record paths.
- [ ] Expand `release/candidates/habitat/README.md` so this sublane inherits from a complete parent candidate contract.

## Status

Draft README replacing blank file.
