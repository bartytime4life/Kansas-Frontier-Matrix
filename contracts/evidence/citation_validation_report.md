<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/citation-validation-report
title: CitationValidationReport
type: semantic-contract/evidence-validation-report
version: v0.3
status: proposed; fixture-first; implementation-bounded; human-review-pending
owners:
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Citation steward
  - OWNER_TBD — Policy and sensitivity steward
  - OWNER_TBD — Release steward
created: 2026-05-20
updated: 2026-08-10
policy_label: public; evidence; citation; cite-or-abstain; no-authority
owning_root: contracts/
responsibility: Define the meaning and fail-closed declaration semantics of CitationValidationReport without resolving evidence or granting policy, review, release, publication, or public-answer authority.
truth_posture: CONFIRMED repository family and authority boundaries / PROPOSED fixture-first v1 profile / NEEDS VERIFICATION hosted exact-head execution and human review
related:
  - ../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../fixtures/contracts/v1/evidence/citation_validation_report/cases.json
  - ../../tools/validators/citation/validate_citation_validation_report.py
  - ../../tests/validators/test_validate_citation_validation_report.py
  - ../../.github/workflows/citation-validation.yml
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, citation, evidence, validation-report, evidence-ref, evidence-bundle, rights, sensitivity, policy, review, release, cite-or-abstain]
notes:
  - "v0.3 realizes one closed fixture-first report profile over declared upstream states."
  - "A validator pass proves report shape and internal consistency only; it does not contact a source, resolve an EvidenceRef, authenticate an EvidenceBundle, evaluate policy, authenticate review, verify release, or authorize publication."
  - "The UI and Focus citation report families remain downstream projections and are not modified by this profile."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CitationValidationReport

> A deterministic report that preserves citation readiness and negative states for one declared subject. It is a validation record, not evidence closure, policy, review, release, publication, or truth authority.

## Status

| Field | Value |
|---|---|
| Contract version | v0.3 |
| Machine profile | 1.0.0-proposed |
| Posture | Fixture-first; no network; human review pending |
| Canonical meaning owner | contracts/evidence/ |
| Canonical shape owner | schemas/contracts/v1/evidence/ |
| Validator owner | tools/validators/citation/ |
| Runtime, API, UI, release adoption | Not established |

The profile is additive to the existing evidence family. It does not create a standalone Citation authority, replace EvidenceRef or EvidenceBundle, or promote UI/Focus projections into canonical evidence reports.

## Meaning

A CitationValidationReport answers:

- what subject and claim scope were checked;
- which citation carriers were declared;
- which source role, locator, time, EvidenceRef, EvidenceBundle, rights, sensitivity, policy, review, and release states were declared for each citation;
- which finite result follows from those declarations;
- which remediation remains required; and
- whether the complete report is internally consistent and deterministically identified.

The report does not decide whether a claim is true. Declared RESOLVED, CLOSED, ALLOW, APPROVED, or RELEASED values are not authenticated by this profile.

## Authority split

| Responsibility | Owner | Report boundary |
|---|---|---|
| Citation-report meaning | contracts/evidence/ | This contract |
| Machine shape | schemas/contracts/v1/evidence/ | Closed proposed profile |
| Evidence pointer | EvidenceRef | Referenced; never resolved here |
| Claim-scope closure | EvidenceBundle | Referenced; never created or authenticated here |
| Source identity and role | Source registry and source contracts | Declared references and roles only |
| Rights and sensitivity | Governed source/policy/review owners | Declared states only |
| Policy | policy/ and PolicyDecision | No evaluation or decision |
| Human review | ReviewRecord and governed reviewers | No authentication or approval |
| Release/correction/rollback | release/ and lifecycle companions | No release verification or transition |
| Public output | Governed runtime/API/UI projections | No route or public-answer authority |

## Profile shape

The 1.0.0-proposed profile requires:

| Object | Required meaning |
|---|---|
| report_id | Deterministic identity derived from the report subject bytes |
| checked_at | Explicit RFC 3339 evaluation time |
| validator_profile_ref | Digest-bound profile reference |
| subject | Subject reference, type, claim-scope reference, target surface, allowed source roles, and currentness requirement |
| citations | Canonically ordered citation declarations with upstream states, exact finite result, reason codes, and remediation |
| summary | Exact counts, aggregate finite result, unioned reasons, and remediation references |
| permissions | Six authority effects fixed to false |
| limitations | Exact declaration-only non-effects |
| spec_hash | RFC 8785 JCS plus SHA-256 digest over the report except report_id and spec_hash |

Unknown fields fail schema validation. Citation IDs must be unique and canonically ordered. Allowed source roles, reason codes, and remediation references must be canonical.

## Citation declarations

Each citation preserves:

- a citation ID, target reference, and source-record reference;
- source role;
- locator kind and opaque KFM locator reference;
- citation carrier state;
- freshness state;
- EvidenceRef reference and declared resolution state;
- EvidenceBundle reference and declared closure state;
- rights and sensitivity states;
- policy, review, and release states;
- a derived PASS, ABSTAIN, DENY, or ERROR;
- exact reason codes; and
- a remediation reference for every non-pass result.

The fixture profile accepts only opaque kfm: references. It accepts no URL, endpoint, credential, raw source payload, excerpt, coordinate, private record, or source content.

## Finite semantics

The validator derives each result from declared states. The caller cannot choose a more permissive result.

| Condition | Result |
|---|---|
| Dependency or declared citation/policy error | ERROR |
| Denied rights, evidence, bundle, policy, sensitivity, or withdrawn public release | DENY |
| Missing, malformed, out-of-scope, stale, unresolved, incomplete, unknown, role-incompatible, unreviewed, or unreleased support | ABSTAIN |
| Every required declaration is ready for the stated internal or public-candidate scope | PASS |

Precedence is ERROR over DENY over ABSTAIN over PASS. The summary applies the same precedence across citations and cannot average away a blocked citation.

### Public-candidate boundary

For AI_ANSWER_CANDIDATE, EXPORT_CANDIDATE, FOCUS_CANDIDATE, GOVERNED_API_CANDIDATE, or MAP_CANDIDATE:

- policy must be declared ALLOW;
- review must be declared APPROVED;
- release must be declared RELEASED; and
- restricted sensitivity produces DENY.

These are monotonic consistency checks. They do not authenticate the declarations or authorize public use.

## Deterministic identity

The validator:

1. removes report_id and spec_hash;
2. canonicalizes the remaining JSON with the repository hashing profile;
3. computes sha256 with a 64-character hexadecimal digest;
4. assigns that value to spec_hash; and
5. assigns the first 24 digest characters to the kfm:citation-validation-report identity.

Digest equality proves only equality under the declared canonicalization profile.

## Validation and fixtures

The bounded validator:

- parses duplicate-free finite JSON from regular non-symlink files;
- enforces input and schema-finding limits;
- validates the closed Draft 2020-12 schema;
- checks ordering, uniqueness, upstream binding coherence, derived outcomes, reasons, remediation, summary, and identity;
- emits deterministic non-echoing findings; and
- performs no network, source, resolver, policy, review, release, lifecycle, or publication operation.

Synthetic fixtures cover positive internal/public candidates, missing evidence, unresolved refs, incomplete bundles, source-role mismatch, staleness, rights denial, sensitive public use, unreleased and withdrawn public candidates, dependency error, authority overreach, malformed structure, binding inconsistency, summary drift, and identity drift.

## Result interpretation

| Validator output | Meaning |
|---|---|
| PASS | The report is coherent and its declared citation result is PASS. |
| ABSTAIN | The report is coherent and preserves at least one abstention condition. |
| DENY with no findings | The report is coherent and preserves a denied condition. |
| ERROR with no findings | The report is coherent and preserves an operational error. |
| DENY with findings | The report itself is malformed or semantically inconsistent. |
| ERROR with findings | Input could not be safely parsed or checked. |

No result establishes evidence truth, source admission, rights clearance, sensitivity clearance, policy permission, review authority, release validity, or publication.

## Deferred

- live EvidenceRef resolution;
- EvidenceBundle authenticity and content verification;
- source registry lookup;
- policy evaluation;
- reviewer identity and authority lookup;
- release/correction/rollback lookup;
- emitted governed report persistence;
- API, UI, Focus Mode, export, map, or AI consumption;
- current external-source or URL validation; and
- required-check or promotion significance.

## Rollback

Before merge, close the draft and abandon the isolated branch. After an authorized merge, revert the dependency-closed citation packet: contract, schema, validator and compatibility wrapper, fixtures, tests, workflow, source map, and generated receipt. No external source, lifecycle record, policy decision, review, release, deployment, publication, or public state requires restoration.
