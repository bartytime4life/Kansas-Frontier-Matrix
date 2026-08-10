<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools/validators/citation
title: Citation validator lane
type: readme/validator-lane
version: v0.3
status: draft; fixture-first-validator-present; human-review-pending
owners: OWNER_TBD — Citation steward · Evidence steward · Validator steward · Policy steward · Release steward
created: 2026-07-08
updated: 2026-08-10
policy_label: public; repository-facing; citation; no-network; cite-or-abstain; fail-closed
owning_root: tools/
responsibility: Validate CitationValidationReport shape and declared-state consistency without resolving evidence or granting evidence, policy, review, release, publication, or public-answer authority.
truth_posture: CONFIRMED implementation paths and local source shape / PROPOSED fixture profile / NEEDS VERIFICATION exact-head CI and human review
related:
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../fixtures/contracts/v1/evidence/citation_validation_report/cases.json
  - ../../../tests/validators/test_validate_citation_validation_report.py
  - ../../../.github/workflows/citation-validation.yml
  - ../validate_citation_validation.py
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, validator, citation, evidence-ref, evidence-bundle, rights, sensitivity, policy, review, release, no-network]
notes:
  - "v0.3 replaces the README-only readiness lane with one bounded fixture-first CitationValidationReport validator."
  - "The prior root-level NotImplementedError entrypoint is retained as a thin compatibility wrapper."
  - "The validator checks declarations and monotonic outcomes only; it never contacts a source or authenticates an upstream state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation validator lane

> Validate citation-report declarations while preserving cite-or-abstain, rights, sensitivity, policy, review, release, and public-surface boundaries.

## Current implementation

| Surface | Status | Boundary |
|---|---|---|
| Semantic contract | Proposed v0.3 | Meaning only |
| Evidence schema | Closed proposed fixture profile | Shape only |
| Direct validator | Present in this lane | Declaration consistency only |
| Root compatibility entrypoint | Thin wrapper | No duplicate semantics |
| Synthetic fixture matrix | Positive and negative cases | No real sources or URLs |
| Focused tests | Present | Local deterministic proof only |
| Citation workflow | Two substantive declaration-only jobs | Not a required-check or release decision |
| Runtime/API/UI consumer | Not established | No public behavior claimed |

## Commands

Run the exact synthetic fixture matrix:

    KFM_NO_NETWORK=1 python tools/validators/citation/validate_citation_validation_report.py --fixtures

Run the compatibility entrypoint:

    KFM_NO_NETWORK=1 python tools/validators/validate_citation_validation.py --fixtures

Validate one materialized report:

    KFM_NO_NETWORK=1 python tools/validators/citation/validate_citation_validation_report.py path/to/report.json

Run the focused suite:

    KFM_NO_NETWORK=1 python -m pytest -q tests/validators/test_validate_citation_validation_report.py

## Input boundary

The validator accepts one regular, non-symlink, bounded UTF-8 JSON file. It rejects:

- duplicate object keys;
- non-finite numeric tokens;
- malformed JSON;
- oversized inputs;
- non-object roots;
- unknown fields;
- invalid timestamps, identifiers, or digest shapes;
- noncanonical ordering or duplicate citation IDs;
- inconsistent declared outcomes, reasons, remediation, summaries, or identities; and
- any permission flag that attempts to create evidence, policy, review, release, publication, or public-answer authority.

Fixture references use only opaque kfm: identifiers. The validator does not accept or fetch a URL.

## What is checked

The direct validator enforces:

1. Draft 2020-12 schema shape with format checking.
2. Canonical allowed-source-role and citation ordering.
3. Unique citation identity.
4. Source-role compatibility with the declared claim scope.
5. Required currentness when the subject declares it.
6. Declared EvidenceRef and EvidenceBundle state coherence.
7. Rights and sensitivity negative-state preservation.
8. Policy, review, and release readiness for public-candidate surfaces.
9. Remediation for every non-pass citation.
10. Exact summary counts, outcome, reasons, and remediation references.
11. RFC 8785 JCS plus SHA-256 identity replay.
12. All authority effects fixed false.

## What is not checked

The validator does not:

- contact a source;
- resolve an EvidenceRef;
- inspect or authenticate an EvidenceBundle;
- validate citation content, excerpts, coordinates, or scientific support;
- evaluate rights, sensitivity, consent, policy, or sovereign authority;
- authenticate a reviewer;
- verify a ReleaseManifest, correction, withdrawal, or rollback record;
- create a proof, receipt, catalog record, lifecycle transition, or release;
- call a runtime, API, UI, map, export, Focus Mode, or model;
- make a public answer safe; or
- publish anything.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| PASS | The report is internally coherent and every citation is ready for the declared scope. |
| ABSTAIN | The report is coherent and retains missing, stale, unresolved, incomplete, unknown, unreviewed, unreleased, or otherwise unready support. |
| DENY | The report is coherent and retains a denied condition, or the report itself is malformed when findings are present. |
| ERROR | The report retains an operational error, or input could not be safely parsed when findings are present. |

The validator never converts ABSTAIN, DENY, or ERROR into PASS. Aggregate precedence is ERROR, then DENY, then ABSTAIN, then PASS.

## Public-candidate guard

Public-facing candidates include governed API, map, export, Focus Mode, and AI answer surfaces. A citation can pass for one of those declared scopes only when:

- policy is declared ALLOW;
- review is declared APPROVED;
- release is declared RELEASED;
- sensitivity is not restricted, unknown, or denied;
- rights are clear;
- the citation is usable and current when required; and
- declared evidence references are resolved and the bundle is closed.

These declarations are not authenticated. A PASS remains a bounded consistency result, not publication authority.

## Fixture coverage

The exact fixture matrix includes:

- internal review PASS;
- public-candidate PASS;
- missing citation ABSTAIN;
- unresolved EvidenceRef ABSTAIN;
- incomplete EvidenceBundle ABSTAIN;
- source-role mismatch ABSTAIN;
- stale support ABSTAIN;
- rights DENY;
- restricted public citation DENY;
- unreleased public candidate ABSTAIN;
- withdrawn public citation DENY;
- dependency ERROR;
- unknown-field, authority, and missing-field schema denials;
- duplicate and noncanonical identity denials;
- outcome, reason, remediation, binding, and summary inconsistency denials; and
- spec-hash and report-ID replay denials.

The matrix contains no real person, source endpoint, private record, credential, exact protected location, or source payload.

## Workflow boundary

The existing citation-validation workflow keeps its two stable job IDs:

- citation-resolves runs the complete focused schema, semantic, parser, identity, and fixture suite;
- abstain-on-missing-evidence runs focused negative-path proof and validates the generated authoring receipt.

Both jobs use read-only contents permission, disable persisted checkout credentials, set deterministic no-network execution variables, and install only the repository-declared Python test environment. They do not resolve citations or grant check-run significance beyond their repository workflow results.

## Compatibility

The pre-existing path tools/validators/validate_citation_validation.py remains available as a thin wrapper. The implementation and semantics live only in tools/validators/citation/validate_citation_validation_report.py.

The wrapper may be retired only after a consumer inventory and reviewed migration. It must never diverge into a second validator.

## Diagnostics and privacy

Findings contain only a stable code and JSON Pointer. Input values, citation text, source metadata, query strings, file contents, and sensitive details are not echoed. CLI output records authority NONE and the explicit non-effects.

## Validation burden

Before review:

- run the focused test suite;
- replay the exact fixtures through both entrypoints;
- validate JSON and workflow syntax;
- run documentation metadata and local-link checks for changed Markdown;
- validate the generated receipt against final artifact bytes;
- inspect the diff for private source names, links, credentials, or sensitive payloads; and
- keep hosted exact-head execution and human review visibly pending until observed.

## Rollback

Before merge, close the draft pull request and abandon the isolated branch. After an authorized merge, revert the contract, schema, direct validator, compatibility wrapper, fixtures, tests, workflow, source map, and generated receipt as one dependency-closed packet. No source, evidence record, policy decision, review, release, deployment, publication, or public state requires restoration.
