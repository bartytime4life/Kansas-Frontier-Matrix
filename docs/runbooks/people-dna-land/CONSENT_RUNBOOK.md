<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-consent
title: People/DNA/Land Consent Review and Revocation Runbook
type: runbook
version: v1.0.0
prior_state: explicit scaffold with no operational procedure
status: DRAFT_REPOSITORY_GROUNDED; TWO_BOUNDED_SYNTHETIC_PROFILES_EXECUTABLE; REAL_CONSENT_POLICY_RUNTIME_AND_REVOCATION_EXECUTION_HELD; NON_RELEASE; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, legal, Indigenous/Tribal, policy, evidence, source, release, operations, and independent-review assignments"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing; sensitive-domain; consent; revocation-aware; synthetic-fixture-only; fail-closed; non-release; non-publication
current_path: docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for reviewing a precisely scoped consent question, reproducing the current synthetic consent and revocation checks, and preparing a minimized fail-closed handoff without issuing consent, activating policy, executing revocation or cleanup, or changing release or publication state.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, semantic contracts, schemas, policy, source and evidence authority, accountable consent and sovereignty-aware review, lifecycle, proof, release, correction, withdrawal, revocation, and rollback authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80
  target_prior_blob: d615875309c9298a9f621447fa9dcacc08e60cb1
  current_executable_profiles: 2
  current_production_consent_runtime: NEEDS_VERIFICATION
  current_operational_revocation_cleanup: NEEDS_VERIFICATION
related:
  - ./README.md
  - ./LIVING_PERSON_REVIEW.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/CONSENT_MODEL.md
  - ../../domains/people-dna-land/DNA_HANDLING.md
  - ../../../contracts/domains/people-dna-land/consented_genealogy_overlay.md
  - ../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json
  - ../../../schemas/contracts/v1/domains/people-dna-land/consent_revocation_propagation_assessment.schema.json
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../policy/domains/people-dna-land/consent/dna_consent_revocation.rego
  - ../../../fixtures/domains/people-dna-land/consent_overlay/README.md
  - ../../../fixtures/domains/people-dna-land/consent_revocation_propagation/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - ../../../tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
  - ../../../.github/workflows/domain-people-dna-land.yml
non_effects:
  - does_not_issue_or_revoke_real_consent
  - does_not_process_real_people_dna_land_or_culturally_restricted_material
  - does_not_activate_or_replace_policy
  - does_not_authenticate_subject_or_representative_authority
  - does_not_execute_deletion_withdrawal_cache_purge_graph_cleanup_or_index_cleanup
  - does_not_resolve_evidence_or_clear_rights_or_sensitivity
  - does_not_promote_release_deploy_or_publish
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Consent Review and Revocation Runbook

Use this runbook to review one precisely bounded consent question in the
People/DNA/Land lane, reproduce the repository's current synthetic checks, and
prepare a minimized reviewer handoff. It is a human procedure, not a consent
issuer, policy engine, revocation service, cleanup executor, or release gate.

> [!IMPORTANT]
> **Consent is necessary where the applicable gate requires it, but consent is
> never sufficient for use, release, or publication.** Evidence, source role,
> rights, sensitivity, accountable review, lifecycle state, release state,
> correction, and rollback remain independent gates.

> [!CAUTION]
> Never place real living-person identifiers, family relationships, DNA or
> genomic material, raw kit or vendor identifiers, consent credentials,
> revocation records, addresses, parcel-owner joins, exact private locations,
> disputed title material, protected cultural information, or proprietary source
> excerpts in Git, pull requests, issues, CI logs, fixtures, screenshots, or
> public artifacts.

**Navigation:** [Authority](#1-purpose-and-authority-boundary) ·
[Status](#2-current-repository-evidence) · [Rules](#3-keystone-rules) ·
[Stop](#4-mandatory-stop-conditions) · [Inputs](#5-required-inputs) ·
[Procedure](#6-review-procedure) · [Checks](#7-bounded-synthetic-validation) ·
[Outcomes](#8-outcomes-and-interpretation) · [Revocation](#9-revocation-expiry-and-withdrawal-handoff) ·
[Record](#10-minimum-result-record) · [Acceptance](#11-acceptance-criteria) ·
[Maintenance](#12-maintenance-correction-and-rollback)

## 1. Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Human
operational procedures belong under `docs/runbooks/`; contracts, schemas,
policy, fixtures, tests, evidence, receipts, proofs, and release decisions retain
their own responsibility roots.

This same-path replacement turns an explicit scaffold into a
repository-grounded procedure. It may:

- describe the current consent and revocation fixture profiles;
- require fail-closed review behavior;
- route a reviewer to exact repository-owned tests and validators;
- record bounded outcomes and unresolved gates; and
- prepare a minimized handoff for accountable review.

It may not:

- issue, amend, suspend, revoke, or validate a real consent grant;
- determine whether a person or representative has legal or cultural authority;
- recognize authority on behalf of an Indigenous Nation or Tribe;
- activate, replace, or bypass policy;
- infer identity, kinship, DNA support, ownership, title, or legal boundaries;
- execute deletion, withdrawal, cache invalidation, graph cleanup, index cleanup,
  or artifact removal;
- change lifecycle, promotion, release, deployment, or publication state; or
- turn synthetic test success into operational or legal approval.

[Back to top](#top)

## 2. Current repository evidence

The following boundary was rechecked against
`main@813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80`.

| Surface | Confirmed current state | Safe conclusion |
|---|---|---|
| [`consented_genealogy_overlay.md`](../../../contracts/domains/people-dna-land/consented_genealogy_overlay.md) | Proposed, restricted, synthetic-fixture-only contract with active, expired, revoked, and `not_required` consent cases | The repository can validate one frozen non-identifying candidate profile; it cannot validate real consent or authorize release |
| [`consent_revocation_propagation_assessment.md`](../../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md) | Proposed, inactive synthetic assessment over `READ`, `ANSWER`, `EXPORT`, `TILE`, `GRAPH`, `INDEX`, and `CACHE` | The repository can check declared local consistency and fail-closed propagation expectations; it does not execute or prove cleanup |
| [Domain workflow](../../../.github/workflows/domain-people-dna-land.yml) | Executes two bounded, repository-owned synthetic profiles with explicit broader holds | A green workflow proves only the named code and fixtures at the tested revision |
| [Consent-policy boundary](../../../policy/consent/people-dna-land/README.md) | Documents a fail-closed posture while recording placement, evaluator, bundle, and runtime gaps | Production consent-policy activation remains `NEEDS VERIFICATION` |
| [Domain consent Rego](../../../policy/domains/people-dna-land/consent/dna_consent_revocation.rego) | Proposed scaffold whose only operative rule is `default allow := false` | The file is a deny-by-default placeholder, not a complete consent evaluator |
| Proof, release, deployment, publication | Explicitly held by the domain workflow and lane documentation | No result from this runbook authorizes those transitions |
| Real person, DNA, consent, land-title, or culturally controlled material | Not admitted or evaluated by the current synthetic profiles | Keep real or source-derived material outside repository-visible fixtures and obtain accountable review in an approved environment |

The older
[`CONSENT_MODEL.md`](../../domains/people-dna-land/CONSENT_MODEL.md) and
[`DNA_HANDLING.md`](../../domains/people-dna-land/DNA_HANDLING.md) provide
doctrine and proposal lineage. Their proposed credential, token, endpoint,
tombstone, and runtime designs do not become implemented behavior merely
because this runbook links to them.

[Back to top](#top)

## 3. Keystone rules

1. **Consent does not publish data.** It constrains a precisely scoped action;
   every other required gate still applies.
2. **Consent is purpose-specific.** A grant for one purpose, operation, audience,
   field set, relationship set, precision, export, or time window does not cover
   another.
3. **Consent is subject- and authority-bound.** Unresolved subject,
   representative, joint-holder, family-member, community, Indigenous, or
   Tribal authority produces `HOLD`, `ABSTAIN`, `DENY`, or `ESCALATE`.
4. **Consent does not prove a claim.** It cannot establish identity, kinship,
   DNA-derived relationship, residence, ownership, title, or legal boundary.
5. **Consent does not clear rights or sensitivity.** Source rights, privacy,
   sovereignty, cultural protocol, harmful precision, and retention are
   independent.
6. **Missing, stale, unverifiable, disputed, expired, suspended, revoked, or
   out-of-scope consent fails closed.**
7. **Consent to source material does not automatically authorize a new
   inference, aggregation, graph edge, map layer, AI answer, export, or public
   summary.**
8. **Raw genomic material and identifying kit or vendor values remain denied**
   in repository-visible fixtures, logs, URLs, screenshots, and public outputs.
9. **Unknown living status is not a deceased-person determination.** Use the
   [living-person review runbook](./LIVING_PERSON_REVIEW.md).
10. **Revocation and expiry block the next consequential use.** Broader
    withdrawal and cleanup remain held until their execution and receipts are
    independently proved.
11. **Embargo is an independent deny condition.** No executable embargo
    evaluator is established by this runbook; an active or unresolved embargo
    therefore remains `HOLD` or `DENY`.
12. **Maps, tiles, graphs, indexes, caches, summaries, and AI language are
    downstream carriers.** None is sovereign truth or consent authority.

[Back to top](#top)

## 4. Mandatory stop conditions

Stop without copying sensitive details into repository-visible surfaces when any
of these conditions applies:

- the request involves real people, real DNA, a real consent credential, a real
  revocation record, or a real private person-land relationship;
- the subject, holder, authorized representative, or affected party cannot be
  established through the approved review process;
- more than one living person or community may be affected and the required
  consent or governance authority is unresolved;
- purpose, operation, fields, relationships, audience, precision, export,
  retention, valid time, or geographic scope is missing or ambiguous;
- consent is missing, expired, revoked, suspended, disputed, unverifiable, or
  narrower than the proposed use;
- an embargo, legal hold, source-term restriction, sovereignty concern, or
  cultural protocol is active or unresolved;
- evidence, provenance, rights, sensitivity, living status, harmful precision,
  or accountable reviewer authority is unresolved;
- the proposed action could reveal genomic data, kinship, exact living-person
  location, precise land relationships, protected cultural knowledge, burial or
  archaeology locations, or another restricted attribute;
- a command would contact a live provider, use a credential, fetch a payload,
  write lifecycle state, or mutate a deployed system;
- a workflow, log, screenshot, test, issue, or PR would expose protected values;
- an operational deletion, withdrawal, notification, cache purge, graph cleanup,
  index cleanup, release, deployment, or publication action is required; or
- the exact repository paths or commands in this runbook no longer match the
  revision under review.

Use `ESCALATE` for a required accountable review channel. Use `HOLD`,
`ABSTAIN`, `DENY`, or `ERROR` as described below; absence of a denial is never
approval.

[Back to top](#top)

## 5. Required inputs

Record only minimized, non-sensitive facts.

| Input | Requirement |
|---|---|
| Repository identity | Exact commit SHA, branch or pull-request head, and affected paths |
| Proposed action | One explicit operation, such as review, render, answer, export, tile, graph, index, or cache use |
| Purpose and audience | Named, finite, and no broader than the consent scope |
| Material posture | Synthetic fixture, historical/deceased documentary context, living-person data, DNA-derived summary, land-linked person data, or unresolved |
| Consent status | Active, expired, revoked, suspended, unknown, disputed, or not required under an applicable reviewed rule |
| Scope dimensions | Purpose, operation, fields, relationships, audience, retention, and time; add precision, export, and geography when material |
| Independent gates | Evidence, source role, rights, sensitivity, sovereignty/cultural protocol, review, lifecycle, release, correction, and rollback |
| Validation evidence | Exact commands or hosted workflow run at the exact tested SHA |
| Containment path | Named safe stop, correction, withdrawal, rollback, or escalation route if exposure is possible |

For the current synthetic overlay profile, the binding contract and validator—not
this prose—own the exact machine fields. The profile currently checks an explicit
status, scope, audience, issue/expiry interval, token hash, revocation reference,
subject posture, material kind, evidence references, and non-release governance.

[Back to top](#top)

## 6. Review procedure

### 6.1 Freeze the review boundary

1. Record the exact SHA and affected paths.
2. Confirm that the target is documentation, contract, schema, policy,
   validator, test, fixture, registry, or release-related work.
3. Confirm that no real sensitive payload is present in the diff or fixture set.
4. Identify the owning responsibility roots and any open overlapping pull
   request.
5. Stop if the action would require a live external effect or an authority that
   is not established.

### 6.2 Classify the proposed use

Write one sentence that names:

- the subject or material posture without identifying the person;
- the proposed operation;
- the purpose;
- the audience;
- the fields or relationships affected;
- the time and retention window;
- the geographic or precision level; and
- whether the result could reach a public or lower-trust surface.

A statement such as “consent exists” is insufficient. Review the exact use.

### 6.3 Check the consent dimension

For a repository-owned synthetic profile, verify all applicable dimensions:

1. the declared consent state is current at `evaluated_at`;
2. active consent is not expired and is not revoked;
3. living-person and DNA-derived fixture cases carry active consent;
4. purpose, operation, fields, relationships, audience, retention, and time all
   match;
5. the requested disclosure remains restricted/internal as required;
6. the revocation manifest exists, validates, and matches the candidate's
   declared root;
7. the candidate is absent from the revoked overlay set; and
8. no identifying, raw genomic, exact-location, or public-release field is
   present.

For a real case, these repository checks are insufficient. Stop and require the
accountable consent, privacy, legal, domain, and—where implicated—Indigenous or
Tribal governance review appropriate to the material.

### 6.4 Check the independent gates

Even when the consent dimension is satisfied, confirm that the handoff leaves
these gates separate:

- evidence and `EvidenceRef` resolution;
- source role and provenance;
- rights and source terms;
- sensitivity and harmful precision;
- living-person and sovereignty-aware review;
- policy decision and obligation enforcement;
- lifecycle state;
- proof and release state;
- correction, withdrawal, and rollback; and
- deployment and publication.

Do not use consent success to fill any missing gate.

### 6.5 Run the bounded synthetic checks

Follow [§7](#7-bounded-synthetic-validation). Do not substitute real data,
add live connectors, or invent a broader policy or release command.

### 6.6 Interpret and record

Apply [§8](#8-outcomes-and-interpretation), then create the minimized record in
[§10](#10-minimum-result-record). A test `PASS` describes validation; it does
not convert the consent assessment into public-use approval.

[Back to top](#top)

## 7. Bounded synthetic validation

The [no-network runbook](./NO_NETWORK_TEST_RUNBOOK.md) owns the detailed
egress boundary. The current tests patch named Python networking seams; this is
not runner-wide firewall, container, subprocess, dependency-install, or
non-Python egress proof.

From a clean checkout at the exact SHA under review:

```bash
git rev-parse HEAD
git status --short

export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose

python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json

if python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/invalid/*.json; then
  echo "ERROR: known-invalid consent-overlay fixtures were accepted" >&2
  exit 1
fi

echo "EXPECTED_REJECTION: invalid consent-overlay fixtures"

python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

### Validation identity

- **HEAD validation:** the tested SHA is the exact branch head.
- **Merge-result validation:** the tested SHA is a synthetic pull-request merge
  ref; label it as such.
- **Stale validation:** the branch head changed after testing.
- **Unavailable validation:** the command or environment was not available.

Only the first two states are current evidence, and each proves only its named
scope. A documentation-only link or format check does not replace the domain
profiles; a green domain profile does not prove the documentation links.

[Back to top](#top)

## 8. Outcomes and interpretation

Keep three axes distinct.

| Axis | Values | Meaning |
|---|---|---|
| Test execution | `PASS`, `FAIL`, `NOT_RUN` | Whether the named code and fixtures behaved as expected at the tested SHA |
| Consent assessment | `SATISFIED`, `DENY`, `ABSTAIN`, `ERROR` | The finite outcome declared by the synthetic propagation contract |
| Work state | `PROCEED_TO_OTHER_GATES`, `HOLD`, `ESCALATE` | Whether the consent dimension can be handed to the remaining independent gates |

### Required interpretation

| Condition | Consent assessment | Work state | Required action |
|---|---|---|---|
| Active, current, fully in-scope synthetic consent | `SATISFIED` | `PROCEED_TO_OTHER_GATES` | Preserve every evidence, rights, sensitivity, review, lifecycle, release, and publication gate |
| Active consent with any purpose, operation, field, relationship, audience, retention, time, precision, export, or geography mismatch | `DENY` | `HOLD` | Block the requested use; do not broaden the grant |
| Revoked or expired consent | `DENY` | `HOLD` | Block next use and prepare the propagation handoff in §9 |
| Consent state cannot be established | `ABSTAIN` | `HOLD` or `ESCALATE` | Keep consequential surfaces blocked or pending review |
| Evaluation, schema, fixture, validator, or dependency failure | `ERROR` | `HOLD` | Preserve the error; do not reinterpret it as allow or deny |
| Real-person, DNA, cultural, sovereignty, title, or harmful-precision review is required | Not determined by this runbook | `ESCALATE` | Use an approved handling environment and accountable reviewers |
| Synthetic tests pass | No automatic change | No automatic change | Record bounded validation only |
| Invalid fixture is accepted or an unexpected network attempt occurs | Unsafe failure | `HOLD` | Stop and correct the profile before relying on it |

A `SATISFIED` result clears only the consent dimension. It is not `ANSWER`,
release approval, or publication approval.

[Back to top](#top)

## 9. Revocation, expiry, and withdrawal handoff

The current propagation assessment models a closed seven-surface dependency
inventory. For revoked or expired synthetic consent, the declared expectation is:

| Surface | Fail-closed expectation |
|---|---|
| `READ`, `ANSWER`, `EXPORT` | `BLOCKED` with `DENY_NEXT_USE` |
| `TILE`, `GRAPH`, `INDEX`, `CACHE` | `INVALIDATED` or `PURGED` using the action required by the fixture |
| Every affected surface | A declared action-receipt reference is present |

These are **assessment assertions**, not proof that a deployed action occurred or
that a receipt is authentic. This runbook does not call a revocation endpoint,
issue a tombstone, delete data, invalidate a tile, purge a graph, rebuild an
index, clear a cache, notify a subject, or withdraw a release.

For a real or operational revocation:

1. block the next consequential use;
2. preserve a minimized audit fact without sensitive values;
3. identify every affected derivative and public carrier through the approved
   dependency inventory;
4. route required correction, withdrawal, tombstone, invalidation, purge,
   notification, retention, and proof work to their owning authorities;
5. require receipt and outcome verification for each required action;
6. keep the work `HOLD` until accountable review confirms closure; and
7. preserve rollback and correction lineage without silently rewriting history.

If the dependency inventory is incomplete, the revocation service is
unavailable, a receipt cannot be resolved, or cleanup cannot be proved, fail
closed. Do not state that revocation is complete.

[Back to top](#top)

## 10. Minimum result record

Use a repository-safe record such as the following. It is an **illustrative
handoff**, not a canonical schema.

```yaml
review_ref: "opaque-review-reference"
repository_sha: "<exact-sha>"
affected_paths:
  - "<repository path only>"
material_posture: "synthetic_fixture_only"
proposed_operation: "READ | ANSWER | EXPORT | TILE | GRAPH | INDEX | CACHE"
purpose: "<minimized purpose>"
audience: "<bounded audience class>"
validation:
  profile: "consent_overlay | consent_revocation_propagation"
  identity: "HEAD | MERGE_RESULT | STALE | NOT_RUN"
  result: "PASS | FAIL | NOT_RUN"
consent_assessment:
  outcome: "SATISFIED | DENY | ABSTAIN | ERROR"
  reason_codes:
    - "<non-sensitive reason code>"
work_state: "PROCEED_TO_OTHER_GATES | HOLD | ESCALATE"
independent_gates:
  evidence: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  rights: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  sensitivity: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  accountable_review: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  release: "HELD"
limitations:
  - "SYNTHETIC_FIXTURE_ONLY"
  - "NO_REAL_CONSENT_AUTHORITY"
  - "NO_CLEANUP_EXECUTION_PROOF"
  - "NO_RELEASE_OR_PUBLICATION_AUTHORITY"
next_action: "<one bounded action or stop reason>"
```

Do not include names, dates of birth, family links, kit IDs, genomic values,
addresses, coordinates, parcel-owner relationships, credential bodies,
signatures, tokens, protected cultural details, or proprietary excerpts.

[Back to top](#top)

## 11. Acceptance criteria

This runbook update is ready for accountable documentation review when:

1. it uses the existing `docs/runbooks/people-dna-land/` responsibility boundary;
2. it distinguishes current executable synthetic profiles from proposed or
   unverified policy/runtime behavior;
3. it preserves the rule that consent is necessary but never sufficient;
4. it provides exact current commands and the expected negative-fixture
   polarity;
5. it distinguishes test, consent-assessment, and work-state outcomes;
6. missing, mismatched, expired, revoked, unknown, and errored consent remain
   fail-closed;
7. real data, legal sufficiency, representative authority, sovereignty,
   operational cleanup, evidence, release, deployment, and publication remain
   outside this procedure's authority;
8. revocation expectations are described without claiming execution;
9. the result record is minimized and contains no sensitive values; and
10. directly related navigation accurately describes this document's maturity.

[Back to top](#top)

## 12. Maintenance, correction, and rollback

Re-review this file when any of the following changes:

- the consent or revocation semantic contracts or schemas;
- the two accepted synthetic fixture inventories;
- validator reason codes or command-line interfaces;
- domain workflow coverage or no-network controls;
- consent-policy placement, bundle activation, or evaluator binding;
- accountable consent, privacy, legal, Indigenous/Tribal, domain, or release
  ownership;
- revocation, withdrawal, correction, cache, graph, index, or notification
  implementation;
- proof, release, deployment, or publication behavior; or
- the local runbook index and procedure-selection guidance.

Before merge, rollback is closing the draft pull request and deleting its
task-owned branch. After an authorized merge, revert the focused documentation
commit or submit a reviewed forward correction. Either action changes
documentation only; it does not revoke consent, delete data, reverse cleanup,
withdraw a release, invalidate a cache, or change public state.

The April 2026 People/Genealogy/DNA/Land architecture blueprint remains useful
design lineage for consent and revocation object families, but it was prepared
without a mounted repository. Current repository contracts, validators, tests,
workflows, and accepted governance therefore control current-behavior claims.

[Back to top](#top)
