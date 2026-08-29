<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-living-person-review
title: People, DNA, and Land Living-Person Review Runbook
type: runbook
version: 0.3.1
status: DRAFT_REPOSITORY_GROUNDED; SYNTHETIC_VALIDATION_ONLY; POLICY_RUNTIME_UNBOUND; ACCOUNTABLE_REVIEW_UNVERIFIED; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable privacy, consent, Indigenous/Tribal, legal, security, and domain stewardship NEEDS VERIFICATION"
created: 2026-08-25
updated: 2026-08-29
owning_root: docs/
responsibility: human review procedure for the existing people-dna-land lane
policy_label: "people-dna-land; living-person; privacy; consent; evidence; rights; sensitivity; fail-closed; synthetic-only; human-review; non-release; non-publication"
truth_posture: "CONFIRMED repository-grounded review procedure and exact synthetic commands / NEEDS VERIFICATION accountable specialist routes, policy runtime, real consent authority, production handling, release, deployment, and publication"
related:
  - docs/runbooks/people-dna-land/README.md
  - docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md
  - docs/runbooks/people-dna-land/revocation.md
  - docs/runbooks/people-dna-land/NO_NETWORK_TEST_RUNBOOK.md
  - docs/domains/people-dna-land/README.md
  - docs/policy/living_persons_geoprivacy.md
  - policy/domains/people-dna-land/README.md
  - policy/consent/people-dna-land/README.md
  - .github/workflows/domain-people-dna-land.yml
  - tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People, DNA, and Land Living-Person Review Runbook

> **One-line purpose.** Keep repository work that could expose or affect a
> living or plausibly living person on a fail-closed path until evidence,
> purpose, audience, consent, rights, sensitivity, and accountable review are
> established without placing protected detail in repository-visible systems.

> [!CAUTION]
> Do not place real names paired with private locations, DNA or genomic
> material, consent credentials, private relationship data, protected cultural
> information, precise person-land joins, or proprietary source excerpts in
> Git, pull requests, issues, CI output, fixtures, screenshots, or artifacts.

> [!IMPORTANT]
> This is a human review procedure. It does not determine living status, grant
> or validate real consent, activate policy, recognize authority on behalf of
> an Indigenous Nation or Tribe, approve sensitive-data handling, or authorize
> source admission, lifecycle mutation, release, deployment, or publication.

**Quick navigation:** [Authority](#purpose-and-authority-boundary) ·
[Evidence](#current-evidence-boundary) · [Rules](#keystone-rules) ·
[Stop](#mandatory-stop-conditions) · [Inputs](#required-inputs) ·
[Procedure](#review-procedure) · [Outcomes](#finite-outcomes) ·
[Handoff](#minimum-review-handoff) · [Validation](#validation-and-interpretation) ·
[Sources](#proposal-source-reconciliation) · [Rollback](#rollback-and-non-effects)

## Purpose and authority boundary

Use this procedure for a repository change involving living or plausibly living
people, DNA-derived material, family or kin relationships, consent, private
location, or land-linked identity. The procedure prepares a bounded repository
review and an accountable-review handoff; it is not the accountable review.

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human procedures under `docs/runbooks/`. This same-path update remains in the
`docs/` responsibility root and creates no parallel contract, schema, policy,
registry, evidence, receipt, proof, release, or publication home.

When documentation and executable evidence differ, preserve both facts:
accepted governance defines the boundary, while executable evidence establishes
only the behavior actually demonstrated at the tested revision. Do not infer
operational maturity from policy prose, a file name, or a green workflow.

[Back to top](#top)

## Current evidence boundary

| Surface | Repository evidence | Bounded conclusion |
|---|---|---|
| [Consent-overlay profile](../../../.github/workflows/domain-people-dna-land.yml) | The workflow runs deterministic checks over repository-owned synthetic fixtures with `KFM_NO_NETWORK=1`, including a negative-fixture loop. | A pass confirms only that named synthetic profile at the tested revision. |
| [Revocation-propagation assessment](./revocation.md) | The validator and tests exercise synthetic `ACTIVE`, `REVOKED`, `EXPIRED`, `UNKNOWN`, and `ERROR` states across a declared seven-surface inventory. | The profile checks declared fail-closed consistency; it does not execute or prove cleanup. |
| [Domain policy boundary](../../../policy/domains/people-dna-land/README.md) and [consent boundary](../../../policy/consent/people-dna-land/README.md) | Both describe fail-closed intent while recording inactive, incomplete, or evaluator-unbound implementation. | Production policy binding remains **NEEDS VERIFICATION**. |
| [Living-person geoprivacy crosswalk](../../policy/living_persons_geoprivacy.md) | Human-readable containment and routing guidance; it explicitly is not policy authority or protected-data storage. | Use it for routing and exposure review, not as an allow decision. |
| Real-person or culturally controlled material | The executable lane deliberately uses synthetic fixtures. | Legal authority, real consent sufficiency, sovereignty review, and safe handling of real records remain **HOLD** outside Git and CI. |
| Proof, promotion, release, and publication | Current lane documentation and workflow keep these states separate and held. | No result from this runbook authorizes any governed transition. |

[Back to top](#top)

## Keystone rules

1. **Unknown living status is not a deceased-person determination.** When safe,
   require evidence appropriate to the claim. Otherwise treat the person as
   plausibly living and fail closed.
2. **Living status, identity, consent, rights, sensitivity, and release are
   separate determinations.** Satisfying one does not satisfy another.
3. **Consent is scoped.** Purpose, operation, audience, fields, relationships,
   precision, geography, retention, export, and valid time must fit the exact
   proposed use.
4. **Consent does not prove a claim.** It cannot establish identity, kinship,
   DNA-derived relationship, residence, ownership, title, or legal boundary.
5. **Evidence outranks generated language.** Evidence-dependent claims must
   resolve through EvidenceRef to EvidenceBundle and follow cite-or-abstain.
6. **Derived carriers are not sovereign truth.** Maps, tiles, graphs, indexes,
   caches, embeddings, summaries, dashboards, and AI output inherit upstream
   restrictions and can preserve reconstruction risk.
7. **Client-side concealment is not a public-safe transform.** Hiding a field,
   popup, layer, label, or model response does not make protected data safe to
   deliver.
8. **Absence of denial is not approval.** `UNKNOWN`, missing, invalid, errored,
   or unreviewed evidence remains fail-closed.

[Back to top](#top)

## Mandatory stop conditions

Stop and record `HOLD` or `ESCALATE` without copying sensitive detail into a
repository-visible surface when any of these conditions applies:

- living status cannot be established safely, or evidence conflicts;
- identity, subject, representative, joint holder, or affected party is
  unresolved;
- purpose, operation, audience, fields, relationships, precision, geography,
  retention, export, allowed use, or valid time is missing or ambiguous;
- consent is missing, expired, revoked, suspended, disputed, unverifiable, or
  narrower than the proposed use;
- rights, license, source terms, provenance, EvidenceRef, EvidenceBundle, source
  role, or chain of custody is insufficient;
- the material includes or may reveal genomic data, kinship, health or biometric
  data, living-person location, precise land relationships, protected cultural
  knowledge, burial or archaeology locations, rare-species associations,
  critical infrastructure, or another restricted attribute;
- Indigenous or Tribal sovereignty, consent, cultural protocol, data-governance
  authority, or appropriate representative cannot be resolved;
- a public or lower-trust audience exceeds the established consent, rights,
  sensitivity, or harmful-precision boundary;
- the proposed repository record, workflow, log, screenshot, issue, PR, fixture,
  or artifact would expose a protected value;
- a required accountable reviewer or active policy binding cannot be identified;
- a command would contact a live provider, use a credential, fetch a sensitive
  payload, or mutate repository, data, lifecycle, release, or public state; or
- deletion, erasure, notification, correction, withdrawal, cache invalidation,
  source activation, access widening, release, deployment, publication, or a
  repository-setting change is required.

Use `ERROR` when the review mechanism or validation fails. Do not reinterpret an
error as approval, denial, or proof that a protected action occurred.

[Back to top](#top)

## Required inputs

Record only minimized, non-sensitive facts.

| Input | Requirement |
|---|---|
| Repository identity | Exact commit SHA or pull-request head and affected paths |
| Proposed action | One explicit operation, such as documentation review, answer, export, tile, graph, index, or cache use |
| Purpose and audience | Named, finite, and no broader than the proposed action requires |
| Data posture | `SYNTHETIC_ONLY`, `NO_REAL_PAYLOAD`, or `REAL_OR_SOURCE_DERIVED_REQUIRES_ESCALATION` |
| Living-status posture | `HISTORICAL_SUPPORTED`, `LIVING_OR_PLAUSIBLY_LIVING`, or `UNKNOWN`; include only an opaque evidence reference |
| Consent posture | Status, scope, audience, valid time, and revocation category; no credential or identifying value |
| Evidence and source posture | EvidenceRef resolution, source role, rights, provenance, custody, and currentness |
| Exposure posture | Sensitivity categories, precision, geography, downstream carriers, and reconstruction risk |
| Accountability | Required reviewer roles and the approved non-repository review channel |
| Containment path | Safe stop, correction, withdrawal, rollback, or escalation route if exposure is possible |

If the action cannot be described with these minimized fields, keep the details
out of repository systems and stop for an approved handling environment.

[Back to top](#top)

## Review procedure

### 1. Freeze the repository boundary

1. Record the exact revision and affected paths.
2. Classify each path by responsibility root and artifact role.
3. Confirm that the diff and fixtures contain no real sensitive payload.
4. Identify overlapping pull requests and direct documentation consumers.
5. Stop if the requested work requires a live external effect or unestablished
   authority.

### 2. Establish the living-status posture

Determine whether admissible evidence supports a historical, non-living posture.
Do not use a guessed age, missing recent record, generated profile, tree label,
obituary-like text, or public availability as proof. A recent or unresolved
record remains `LIVING_OR_PLAUSIBLY_LIVING` or `UNKNOWN` for this procedure.

Record only the posture and an opaque evidence reference. Do not copy dates,
names, addresses, relationship details, or source excerpts into the handoff.

### 3. Classify evidence, sensitivity, and downstream exposure

Confirm whether the proposal concerns DNA, genomic, biometric, health, family,
kinship, inferential identity, land tenure, parcel, address, mobility,
precise-location, Indigenous or Tribal material, protected cultural knowledge,
or a combination that increases reconstruction risk.

Trace the proposed output through every named carrier: API response, export,
tile, map, graph, index, cache, summary, evidence drawer, or AI context. A safe UI
appearance does not prove a safe delivered payload.

### 4. Verify consent, rights, and accountable authority separately

For the synthetic validation profile, verify that recorded consent is active,
unexpired, unrevoked, and within purpose, audience, and operation. For a real
case, repository validators are insufficient. Require accountable privacy,
consent, legal, domain, security, and—when implicated—Indigenous or Tribal
governance review in an approved environment.

Do not convert missing, unknown, disputed, or errored consent into approval.
Revocation or expiry must block the next consequential use. Deletion,
propagation, notification, correction, withdrawal, release replacement, and
proof remain separate obligations until independently demonstrated.

### 5. Run only the bounded synthetic checks

From a clean checkout at the exact revision under review, reproduce the current
workflow profile:

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json
python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

Use the [domain workflow](../../../.github/workflows/domain-people-dna-land.yml)
or the [no-network runbook](./NO_NETWORK_TEST_RUNBOOK.md) for the complete
negative-fixture loop. Do not invent a broader parent validator, source-access
command, policy evaluator, proof producer, or publication command.

### 6. Classify validation identity

- `HEAD` applies only when the tested commit is the exact branch head.
- `MERGE_RESULT` applies only to the exact synthetic merge SHA.
- `STALE` applies when the tested revision is no longer the asserted head.
- `NOT_RUN` applies when the check was not performed.

Do not transfer a result across revisions or describe a merge-result check as
branch-head validation.

### 7. Route accountable review

| Condition | Required review route | Repository-safe output |
|---|---|---|
| Any living or plausibly living person | Privacy, consent, legal, domain, and security roles | Opaque handoff with `ESCALATE`; accountable names and channel remain **NEEDS VERIFICATION** |
| Indigenous or Tribal person, place, knowledge, governance, or cultural protocol | Appropriate Nation/Tribe-designated or otherwise accountable governance route plus privacy/legal review | Record only that authority is unresolved or satisfied outside Git; never reproduce protected content |
| DNA, genomic, kinship, biometric, or health material | Privacy, consent, legal, domain, security, and data-custody roles | `HOLD` pending approved handling and separate policy evidence |
| Precise person-land, residential, parcel, or mobility exposure | Privacy, geoprivacy, source/rights, domain, security, and release roles | `HOLD` pending public-safe transform and reconstruction-risk review |
| Historical person with supported non-living posture | Domain, evidence/source, rights, and sensitivity roles | May proceed only to remaining gates; no automatic release or publication |

`@bartytime4life` is the confirmed CODEOWNERS review route. The accountable
specialist assignments and approved private handling channel remain **NEEDS
VERIFICATION** and must not be invented in a public handoff.

[Back to top](#top)

## Finite outcomes

Keep test execution, subject posture, and work state separate.

| Axis | Values | Meaning |
|---|---|---|
| Test execution | `PASS`, `FAIL`, `NOT_RUN` | Whether the named synthetic profile behaved as expected at the tested revision |
| Subject posture | `HISTORICAL_SUPPORTED`, `LIVING_OR_PLAUSIBLY_LIVING`, `UNKNOWN` | The minimized living-status category for review routing; not an identity or legal determination |
| Work state | `PROCEED_TO_OTHER_GATES`, `HOLD`, `ESCALATE`, `ERROR` | The next repository-safe action; never a release or publication decision |
| Progression hold | `true`, `false` | Whether further repository progression is blocked; an independent Boolean, not a second work-state value |

| Condition | Required work state | Interpretation |
|---|---|---|
| Exact synthetic profile passes and the change contains no real or source-derived sensitive material | `PROCEED_TO_OTHER_GATES` | Only the named synthetic and documentation gates may continue |
| Living or plausibly living person, real DNA, real consent, protected cultural material, or precise private location is implicated | `ESCALATE` | Use the approved non-repository handling and accountable review route |
| Living status, evidence, consent, rights, sensitivity, source role, custody, audience, policy binding, or reviewer authority is unresolved | `HOLD` or `ESCALATE` | Preserve the fail-closed boundary |
| `REVOKED`, `EXPIRED`, or scope-mismatched consent does not block next use | `HOLD` | The bounded fail-closed acceptance criterion failed |
| `UNKNOWN` is treated as satisfied, or `ERROR` is coerced to another outcome | `HOLD` | Uncertainty or failure was converted unsafely |
| Test, fixture, schema, validator, dependency, or review mechanism fails unexpectedly | `ERROR` | Set `progression_hold: true`; preserve the failure and correct it before relying on the profile |
| Promotion, release, deployment, publication, access widening, or repository settings are requested | `HOLD` | Route the request to its separately governed authority |

`work_state` must contain exactly one enum value. An unexpected failure uses
`work_state: ERROR` with `progression_hold: true`; the Boolean records that
progression is blocked without inventing an unencodable composite work state.

`PROCEED_TO_OTHER_GATES` clears no evidence, rights, sensitivity, policy,
review, lifecycle, release, or publication gate.

[Back to top](#top)

## Minimum review handoff

Use a repository-safe record such as this. It is an illustrative handoff, not a
canonical contract or schema.

```yaml
repository_revision: "<exact commit SHA>"
affected_paths:
  - "<repository path>"
material_posture: "SYNTHETIC_ONLY | NO_REAL_PAYLOAD | ESCALATION_REQUIRED"
proposed_action: "<one bounded operation>"
purpose: "<minimized purpose>"
audience: "<bounded audience class>"
subject_posture: "HISTORICAL_SUPPORTED | LIVING_OR_PLAUSIBLY_LIVING | UNKNOWN"
living_status_evidence_ref: "<opaque authority reference | UNRESOLVED>"
consent:
  status: "ACTIVE | EXPIRED | REVOKED | SUSPENDED | DISPUTED | UNKNOWN | NOT_APPLICABLE"
  scope_posture: "COVERS_PROPOSED_USE | DOES_NOT_COVER | UNRESOLVED | NOT_APPLICABLE"
  purpose_posture: "COVERS_PROPOSED_USE | DOES_NOT_COVER | UNRESOLVED | NOT_APPLICABLE"
  audience_posture: "COVERS_PROPOSED_AUDIENCE | DOES_NOT_COVER | UNRESOLVED | NOT_APPLICABLE"
  valid_time_posture: "CURRENT | EXPIRED | UNRESOLVED | NOT_APPLICABLE"
  revocation_posture: "NOT_REVOKED | REVOKED | UNKNOWN | NOT_APPLICABLE"
  authority_ref: "<opaque authority reference | UNRESOLVED | NOT_APPLICABLE>"
evidence:
  bundle_ref: "<opaque EvidenceBundle reference | UNRESOLVED | NOT_APPLICABLE>"
  source_role: "<non-sensitive role label | UNRESOLVED>"
  rights_posture: "RESOLVED | HELD | UNRESOLVED | NOT_APPLICABLE"
  provenance_custody_currentness: "RESOLVED | UNRESOLVED | NOT_APPLICABLE"
sensitivity_categories:
  - "<non-sensitive category label>"
exposure:
  precision_posture: "PUBLIC_SAFE | GENERALIZATION_UNVERIFIED | HARMFUL | UNRESOLVED"
  geography_posture: "NONE | PUBLIC_CONTEXT_ONLY | PRIVATE_OR_PRECISE | UNRESOLVED"
  downstream_carriers:
    - "<bounded carrier class | NONE>"
  reconstruction_risk: "RESOLVED | HELD | UNRESOLVED"
accountability:
  required_roles:
    - "<non-sensitive role label>"
  review_authority_ref: "<opaque authority reference | UNRESOLVED>"
  approved_channel_posture: "CONFIRMED | UNRESOLVED"
validation:
  identity: "HEAD | MERGE_RESULT | STALE | NOT_RUN"
  profile: "consent_overlay | consent_revocation_propagation | documentation_only"
  result: "PASS | FAIL | NOT_RUN"
independent_gates:
  consent: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  rights: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  sensitivity: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  accountable_review: "UNRESOLVED | HELD | SATISFIED_BY_SEPARATE_AUTHORITY"
  release: "HELD"
work_state: "PROCEED_TO_OTHER_GATES | HOLD | ESCALATE | ERROR"
progression_hold: true
reason_codes:
  - "<non-sensitive reason code>"
limitations:
  - "NO_IDENTITY_OR_LIVING_STATUS_AUTHORITY"
  - "NO_REAL_CONSENT_AUTHORITY"
  - "NO_POLICY_RUNTIME_OR_CLEANUP_PROOF"
  - "NO_RELEASE_OR_PUBLICATION_AUTHORITY"
next_action: "<one bounded repository-safe action>"
```

The handoff is evidence for accountable review, not the review decision. Opaque
references record that a separately governed authority must be consulted; they
do not prove that authority is valid or resolved. Do not include names,
sequences, dates of birth, addresses, coordinates, relationship details,
consent credentials, protected cultural information, or proprietary excerpts.

[Back to top](#top)

## Validation and interpretation

Before handing off this runbook change:

1. review the complete diff for unrelated churn or lost limitations;
2. confirm one H1, balanced fences, valid tables, stable anchors, and a final
   newline;
3. resolve every changed relative link and cited repository path;
4. confirm the four exact Python entry points and fixture manifest still exist;
5. run the repository's focused Markdown, metadata, document-graph, and link
   checks when available; and
6. label hosted results with the exact tested SHA and separate introduced,
   inherited, skipped, pending, and external failures.

A green documentation or domain workflow does not establish real-person
correctness, consent sufficiency, policy activation, complete revocation
propagation, public-safe transformation, proof closure, release readiness,
deployment, or publication safety.

### Acceptance criteria

This documentation slice is complete only when:

1. the synthetic executable profile is distinct from real-person review and an
   unverified policy runtime;
2. living status, consent, evidence, rights, sensitivity, and release remain
   separate determinations;
3. missing, revoked, expired, unknown, and errored states cannot be described as
   approval;
4. living-person, DNA/genomic, land-linked, Indigenous/Tribal,
   precise-location, rights, and publication risks have explicit stop and
   reviewer-routing conditions;
5. exact existing commands are provided without inventing live access, policy,
   proof, release, or publication paths;
6. validation identity and finite outcomes are explicit;
7. the minimized handoff records consent status, scope, purpose, audience,
   valid-time and revocation posture plus evidence, exposure, and accountable
   review posture without protected values;
8. `work_state` contains one finite value and any independent progression hold
   is encoded separately; and
9. rollback is limited to documentation and cannot be mistaken for consent
   revocation, data deletion, correction, withdrawal, or public-state change.

[Back to top](#top)

## Proposal-source reconciliation

The read-only Google Drive
`KFM_People_Genealogy_DNA_Land_Ownership_Architecture_Blueprint.pdf` proposes
assertion-first identity, restricted-by-default DNA, fail-closed living-person
output, scoped consent, tokenized identifiers, synthetic-only fixtures, and
separate evidence, policy, review, and release states. It was prepared without a
mounted repository and marks current implementation maturity unknown; it is
lineage, not implementation authority.

`KFM_Full_Atlas_seed_cards.md`, v2 expansion section “People / DNA / Land Safety
Lane” (inspected copy SHA-256
`9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2`), and the
later `KFM Circled Sources — Distinctive Delta Synthesis` reinforce
bounded consent, sensitivity, evidence, denial, and the separation of authority
posture from executable capability. They do not adopt this runbook or activate
policy. Current GitHub evidence and accepted ADR-0029 control the procedure and
placement above.

[Back to top](#top)

## Rollback and non-effects

Before merge, close the draft pull request and delete only its task branch.
After an independently authorized merge, revert the focused documentation
commit or submit a reviewed same-path forward correction.

Either action changes documentation only. It does not determine living status,
revoke consent, delete or erase data, invalidate a cache, correct or withdraw a
release, alter policy, undo a lifecycle event, admit or contact a source, create
proof, release, deploy, publish, widen access, or change repository settings.

[Back to top](#top)
