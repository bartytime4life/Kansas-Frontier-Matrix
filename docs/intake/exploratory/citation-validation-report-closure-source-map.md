<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/citation-validation-report-closure-source-map
title: Citation validation report closure source map
type: exploratory-source-map/implementation-record
version: v0.1.0
status: proposed; repository-only; fixture-first; human-review-pending
owners: OWNER_TBD — Citation steward · Evidence steward · Validator steward · Policy steward · Release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; repository-facing; citation; cite-or-abstain; no-authority
owning_root: docs/
responsibility: Record the current-repository gap, placement basis, bounded implementation, validation boundary, and rollback for the CitationValidationReport closure packet.
truth_posture: CONFIRMED current public repository evidence / PROPOSED fixture-first implementation / NEEDS VERIFICATION hosted exact-head execution and human review
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 7c69e025e2b274be4a19f49fa37e22401a2fe757
source_scope: public repository files only
related:
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../tools/validators/citation/README.md
  - ../../../tools/validators/citation/validate_citation_validation_report.py
  - ../../../tests/validators/test_validate_citation_validation_report.py
  - ../../../.github/workflows/citation-validation.yml
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, citation, evidence, validator, workflow, source-map, no-network, cite-or-abstain]
notes:
  - "This implementation selection uses public repository files only."
  - "No external document, source endpoint, current external-version claim, private reference, or non-repository requirement is carried into the packet."
[/KFM_META_BLOCK_V2] -->

# Citation validation report closure source map

## Goal

Close the smallest current-repository gap in the existing CitationValidationReport family: replace a permissive schema, NotImplementedError stub, absent fixture family, and hold-only workflow with a strict fixture-first declaration profile.

## Evidence and gap

The authoring base is public main at 7c69e025e2b274be4a19f49fa37e22401a2fe757.

| Public repository evidence | Confirmed observation | Disposition |
|---|---|---|
| contracts/evidence/citation_validation_report.md | Existing semantic owner and strong evidence/policy/release non-authority boundary | Extend in place |
| schemas/contracts/v1/evidence/citation_validation_report.schema.json | Empty properties with additional fields permitted | Replace with a closed proposed profile |
| tools/validators/validate_citation_validation.py | Raises NotImplementedError | Preserve path as a thin compatibility wrapper |
| tools/validators/citation/README.md | Names the direct citation validator lane and required no-network behavior | Put implementation in the existing lane |
| fixtures/contracts/v1/evidence/citation_validation_report/ | No fixture family at the inspected base | Add wholly synthetic cases |
| tests/validators/ | No focused citation-report validator suite | Add deterministic tests |
| .github/workflows/citation-validation.yml | Two explicit readiness-hold jobs with no repository checkout or checks | Preserve job IDs and replace holds with bounded checks |
| Git history and current open pull requests | Documentation-only citation work exists; no current implementation packet or open overlap was found | Proceed with one isolated packet |

The current gap is machine enforcement, not missing semantic ownership. Creating another citation object, schema home, policy family, resolver, or public projection would duplicate authority and is rejected.

## Directory Rules basis

| Artifact responsibility | Existing owning root |
|---|---|
| Human-readable report meaning | contracts/evidence/ |
| Machine-checkable shape | schemas/contracts/v1/evidence/ |
| Reusable synthetic inputs | fixtures/contracts/v1/evidence/ |
| Validator implementation | tools/validators/citation/ |
| Focused validator proof | tests/validators/ |
| Read-only orchestration | .github/workflows/ |
| Adaptation and reconciliation record | docs/intake/exploratory/ |
| AI authoring accountability | data/receipts/generated/ |

Accepted ADR-0029 and Directory Rules v2 place each artifact by responsibility. The compatibility wrapper preserves the old entrypoint without becoming a second semantic implementation.

## Bounded implementation

The packet:

- realizes one 1.0.0-proposed CitationValidationReport profile;
- uses only opaque KFM references and synthetic fixtures;
- checks declared citation, locator, source-role, time, EvidenceRef, EvidenceBundle, rights, sensitivity, policy, review, and release states;
- deterministically derives PASS, ABSTAIN, DENY, or ERROR;
- requires remediation for every non-pass citation;
- rejects attempts to average or overwrite negative states;
- fixes every evidence, policy, review, release, publication, and public-answer permission to false;
- binds report identity with the repository RFC 8785 JCS plus SHA-256 profile; and
- preserves the existing citation-resolves and abstain-on-missing-evidence workflow job identities.

## Non-effects

The packet performs no:

- source or evidence network request from the validator (workflow dependency bootstrap remains outside that runtime boundary);
- EvidenceRef resolution;
- EvidenceBundle content or authenticity check;
- rights, sensitivity, consent, policy, or sovereign decision;
- reviewer authentication;
- release, correction, withdrawal, or rollback lookup;
- lifecycle write;
- API, UI, map, export, Focus Mode, or model invocation;
- deployment; or
- publication.

A PASS means only that the exact declaration is well-formed and internally consistent for its stated scope.

## Validation boundary

Local validation must include:

1. Draft 2020-12 schema meta-validation.
2. Exact positive and negative fixture replay.
3. Focused parser, symlink, identity, monotonicity, compatibility-wrapper, no-network, and no-authority tests.
4. JSON and workflow parsing.
5. Required-profile metadata and local-link validation for changed Markdown.
6. Generated receipt validation against final artifact hashes.
7. Diff inspection confirming repository-only provenance and no private or sensitive source material.

Hosted exact-head results and human review remain NEEDS VERIFICATION until observed.

## Rollback

Before merge, close the draft and abandon its branch. After an authorized merge, revert the dependency-closed packet. The change has no source, evidence, policy, review, release, lifecycle, deployment, publication, or public-state side effect to reverse.
