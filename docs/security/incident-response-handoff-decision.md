<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/security/incident-response-handoff-decision
title: Incident-response guidance and restricted-runbook handoff decision
type: governance-decision-packet
version: v1.0
status: proposed
effective_decision_status: proposed
owners:
  - "@bartytime4life — verified repository review route"
  - "OWNER_TBD — accountable public security guidance owner"
  - "OWNER_TBD — accountable restricted incident-operations owner"
created: 2026-08-15
updated: 2026-09-01
policy_label: public-safe governance
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: >-
  Propose the public-guidance versus restricted-runbook split, finite handoff
  states, accountable roles, content boundary, correction path, and rollback
  rules for the two tracked incident-response surfaces without exposing
  restricted procedure or accepting the decision by publication.
current_path: docs/security/incident-response-handoff-decision.md
related:
  - docs/security/INCIDENT_RESPONSE.md
  - docs/runbooks/INCIDENT_RESPONSE.md
  - docs/security/README.md
  - SECURITY.md
  - .github/CODEOWNERS
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/governance/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [incident-response, security, runbook, handoff, restricted, governance, rollback]
notes:
  - "This packet proposes ACCEPT_SPLIT. Filing, merging, linking, or validating it does not accept that disposition."
  - "No private endpoint, roster, credential, exact sensitive coordinate, exploit detail, evidence payload, or tactical procedure is included."
  - "Both existing incident-response paths remain unchanged until accountable owners and review accept the decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Incident-response guidance and restricted-runbook handoff decision

> **Proposed disposition: `ACCEPT_SPLIT`.** Retain
> `docs/security/INCIDENT_RESPONSE.md` as public security guidance and
> `docs/runbooks/INCIDENT_RESPONSE.md` as the restricted human-operational lane.
> Connect them through a public-safe handoff contract without copying restricted
> procedure into public documentation.

> [!IMPORTANT]
> This is a proposed decision packet, not an accepted ADR, operational activation,
> incident declaration, private-runbook publication, or authority transfer.

## Status

| Field | Current value |
| --- | --- |
| Decision state | `PROPOSED` |
| Proposed disposition | `ACCEPT_SPLIT` |
| Repository checkpoint | `main@db23a8bfa9fa126e87009a41240576619ccaac02` |
| Public guidance path | `docs/security/INCIDENT_RESPONSE.md` |
| Restricted operational path | `docs/runbooks/INCIDENT_RESPONSE.md` |
| Path migration | None |
| Operational activation | None |
| Publication effect | None |
| Acceptance blocker | Accountable owners and independent review remain unverified |

## Milestone inventory and overlap map

| Surface | Classification | Role in this slice |
| --- | --- | --- |
| `docs/security/INCIDENT_RESPONSE.md` | `PARTIAL` | Public guidance surface; supplies reporting, evidence-preservation, correction, and rollback doctrine. |
| `docs/runbooks/INCIDENT_RESPONSE.md` | `PARTIAL` | Restricted operational lane; supplies private playbooks and the synthetic tabletop appendix. |
| `docs/security/incident-response-handoff-decision.md` | `IMPLEMENTED` | Records the first bounded slice: inventory, overlap map, finite states, and rollback contract. |
| `docs/architecture/deployment-topology.md` | `PARTIAL` | Holds the related P0 verification row and points back to this slice. |
| `issue #2900` | `SUPERSEDED` | Closed lineage for the deferred handoff decision. |
| `issue #3380` | `IMPLEMENTED` | Milestone tracker for this bounded slice. |
| `PR #4080` | `PARTIAL` | Open WIP implementation slice; evidence only, no acceptance authority. |
| `Other repository surfaces` | `NOT_INSPECTED` | Outside this slice and left explicit rather than implied. |

## Synthetic tabletop handoff slice

This slice is synthetic only. It proves the public-to-restricted seam, not live
incident handling.

1. `REPORTED` — a public-safe report lands with a report identifier, receipt
   time, affected-surface label, and evidence references only.
2. `ACKNOWLEDGED` — an authorized responder acknowledges receipt without
   confirming incident facts publicly.
3. `TRIAGED` — the restricted lane assigns severity, scope, and an operational
   owner.
4. `TRANSFERRED` — operational control and evidence custody move to the
   restricted lane.
5. `ACTIVE` — containment, investigation, restoration, or coordination is
   underway under restricted control.
6. `MONITORING` — immediate action is complete but validation and recurrence
   checks continue.
7. `CLOSED` — closure criteria and required records are complete.
8. `CORRECTED` — a later correction supersedes the prior record transparently.
9. `ABSTAIN` — evidence is insufficient to classify or communicate beyond the
   safe boundary.
10. `ACCESS_DENIED` — the restricted lane is unavailable to the requester; the
    fallback route is used instead of improvisation.
11. `STALE_RUNBOOK` — required procedure or ownership evidence is stale; unsafe
    execution is held.
12. Evidence custody carries references, timestamps, handling labels, and role
    identifiers only; it does not mirror logs, screenshots, credentials, prompts,
    or payloads into public history.
13. Secrets and keys are rotated or revoked through the issuing authority, with
    access and audit evidence preserved.
14. Forward correction uses `CorrectionNotice`; rollbacks use `RollbackCard`.
    A rollback restores the prior split and does not copy restricted procedure
    into public history.
15. Hosted checks stay bounded to markdown/link and stale-reference validation
    plus the focused governance test. A passing run does not prove operational
    readiness.

## Evidence and rationale

Current repository evidence already distinguishes the two surfaces:

- the security document defines public security expectations, reporting,
  severity, evidence-preservation, communications, review, and post-incident
  guidance;
- the runbook defines a restricted-detail operational lane and explicitly
  withholds sensitive containment, evidence, access, infrastructure, coordinate,
  credential, vendor, and tactical details from public text;
- both documents disclaim operational validation and authority beyond their
  bounded documentation roles; and
- merged PR #2894 preserved both paths because consolidation would outrun the
  ownership, handoff, migration, and rollback evidence.

A single merged document would either make operational detail too public or make
public reporting and doctrine inaccessible. The smallest reversible decision is
therefore to retain both surfaces and govern the seam.

## Proposed authority split

| Responsibility | Public security guidance | Restricted operational runbook |
| --- | --- | --- |
| Safe reporting route and expectations | Owns public-safe description | Consumes the resulting private intake |
| Severity vocabulary | Owns public-safe vocabulary | Applies operational triage criteria |
| Initial evidence-preservation cautions | Owns non-tactical cautions | Owns executable capture and custody steps |
| Containment and restoration | May describe principles only | Owns executable procedure |
| Private contacts and on-call routing | Must not expose | Owns restricted roster and escalation |
| Credentials, tokens, infrastructure, exact coordinates | Must not expose | Owns restricted handling |
| Public status language | Owns approved public-safe framing | Supplies private facts through approved handoff |
| Correction and post-incident learning | Owns public-safe correction principles | Owns operational after-action evidence |

Neither surface may substitute for the other. CODEOWNERS routing is review
routing only; it is not operational accountability or approval.

## Accountable role assignments required before acceptance

Acceptance must name accountable roles for:

1. public security guidance;
2. restricted incident operations and runbook maintenance;
3. private vulnerability and incident intake;
4. incident commander or operational lead;
5. evidence and forensic custody;
6. communications and public-notice approval;
7. legal, privacy, rights, consent, and sensitive-coordinate escalation;
8. vendor, cloud, and third-party escalation; and
9. correction, withdrawal, post-incident review, and rollback.

A person may hold more than one role only when separation-of-duties review
records why that overlap is safe.

## Public-to-restricted handoff contract

### Entry triggers

A handoff begins when public guidance identifies any of these conditions:

- a credible security report or vulnerability;
- suspected credential, token, access, privacy, rights, or sensitive-location
  exposure;
- integrity or availability loss affecting a governed KFM surface;
- evidence that policy, lifecycle, release, correction, or publication controls
  may have failed; or
- an event that cannot be safely resolved through public guidance alone.

### Finite states

| State | Meaning |
| --- | --- |
| `REPORTED` | A public-safe report has entered the approved private intake route. |
| `ACKNOWLEDGED` | An authorized responder has acknowledged receipt without confirming incident facts publicly. |
| `TRIAGED` | The restricted lane has assigned severity, scope, and an operational owner. |
| `TRANSFERRED` | Operational control and evidence custody are explicitly assigned. |
| `ACTIVE` | Restricted containment, investigation, restoration, or coordination is underway. |
| `MONITORING` | Immediate action is complete but validation and recurrence monitoring continue. |
| `CLOSED` | Operational closure criteria and required records are complete. |
| `CORRECTED` | A later correction or supersession changes the prior record transparently. |
| `ABSTAIN` | Evidence is insufficient to classify or communicate beyond the safe boundary. |
| `ACCESS_DENIED` | The restricted lane is unavailable to the requester; escalation follows the fallback route. |
| `STALE_RUNBOOK` | Required procedure or ownership evidence is stale; unsafe execution is held. |

No state itself authorizes public disclosure, release, deployment, lifecycle
promotion, or publication.

### Minimum metadata allowed across the seam

The public-to-restricted transfer may include only:

- report identifier and receipt time;
- reporter-provided contact route when consent and policy permit;
- public-safe affected-surface label;
- preliminary severity hypothesis explicitly marked unconfirmed;
- evidence-reference identifiers rather than embedded sensitive payloads;
- sensitivity and handling labels;
- acknowledgement and escalation timestamps; and
- accountable role identifiers.

Logs, screenshots, credentials, prompts, personal data, exact coordinates,
forensic images, exploit detail, private endpoints, vendor secrets, and tactical
procedure remain in approved restricted stores and are referenced indirectly.

### Acknowledgement and fallback

The accepted implementation must define bounded acknowledgement and escalation
objectives without publishing private rosters. When the restricted runbook is
unavailable, stale, or access-denied:

1. stop unsafe operational improvisation;
2. preserve public-safe evidence references;
3. escalate through the approved private security route;
4. record `ACCESS_DENIED` or `STALE_RUNBOOK`;
5. assign an authorized operational owner before executable action; and
6. use a reviewed emergency correction, never a silent public copy of restricted
   procedure.

## Public-versus-restricted content boundary

### Public guidance may contain

- safe reporting expectations;
- broad severity and finite-state vocabulary;
- high-level roles and responsibilities;
- evidence-preservation cautions;
- public-safe disclosure and correction principles;
- lifecycle, review, and rollback expectations; and
- a non-sensitive pointer to the restricted lane.

### Public guidance must not contain

- private contacts, rosters, credentials, tokens, endpoints, or keys;
- exploitable system topology or exact harmful coordinates;
- tactical containment, bypass, restoration, or forensic procedure;
- unredacted logs, screenshots, evidence payloads, personal information, or
  vendor-confidential material; or
- details whose aggregation would reconstruct restricted operations.

### Restricted runbook may contain

- executable triage, containment, evidence-capture, escalation, restoration, and
  rollback procedure;
- private contacts and on-call routing;
- system-specific operational detail;
- credential, token, protected infrastructure, and exact-coordinate handling;
- restricted checklists, templates, and vendor escalation instructions; and
- evidence custody and access-control procedure.

Restricted content does not become public merely because a public document
links to the runbook identity.

## Review, exercise, and staleness

Before acceptance, reviewers must verify:

- the public document contains no restricted procedure;
- the restricted document exposes no private material through public metadata;
- the reporting route and accountable roles are real and current;
- the finite states have one owner and terminal behavior;
- evidence custody, public communications, correction, and rollback are
  separately accountable;
- each document links to the other only through public-safe language; and
- rollback does not recreate parallel or ambiguous authority.

After acceptance, each surface must be reviewed at least annually and after a
material incident, reporting-route change, responsible-role change, major
platform change, or failed exercise. A stale owner, route, or critical procedure
moves the operational lane to `STALE_RUNBOOK` until reviewed.

Exercises must use synthetic or approved non-sensitive scenarios. A successful
exercise proves only the exercised scope.

## Implementation sequence after acceptance

1. accept or supersede this proposal through explicit human review;
2. record accountable role assignments;
3. add public-safe mutual handoff links to both existing documents;
4. align CODEOWNERS and metadata without treating them as approval;
5. add focused checks for link closure, public/restricted boundary phrases,
   stale ownership, and forbidden public operational detail;
6. perform a synthetic handoff exercise and record its bounded result; and
7. keep any future rename, alias, consolidation, or retirement as a separate
   migration with inbound-reference closure and rollback.

## Alternatives

| Disposition | Result |
| --- | --- |
| `ACCEPT_SPLIT` | **Proposed.** Best matches current repository roles while preserving public and restricted boundaries. |
| `MIGRATE_TO_SECURITY` | Held. Risks placing executable procedure in the public security lane. |
| `MIGRATE_TO_RUNBOOKS` | Held. Risks removing adequate public reporting and doctrine guidance. |
| `HOLD` | Remains the effective state until owners and review accept this proposal. |
| `DENY_CONSOLIDATION` | Applies if future evidence shows no safe single-file arrangement. |

## Correction, migration, and rollback

Before acceptance, revert or close the proposal packet; both existing paths
remain unchanged.

After acceptance, ordinary corrections update the owning surface and preserve
the prior decision and evidence lineage. Meaning-changing reversals require a
reviewed successor decision.

A future path migration must include:

- complete inbound-reference and consumer inventory;
- public/restricted content diff and sensitivity review;
- compatibility and redirect strategy where permitted;
- owner and reporting-route continuity;
- rollback target and restoration test; and
- explicit denial of deletion until consumer closure is proved.

Rollback must restore the prior two-path split without copying restricted
content into public history.

## Validation

The implementation PR should run:

- ADR/decision-document metadata validation where applicable;
- changed-Markdown link and fragment checks;
- document-graph and stale-reference checks;
- changed-area and repository-topology validation;
- public-secret and restricted-content scans;
- generated-authoring-receipt integrity; and
- focused tests for the finite handoff states and public/restricted boundary.

Passing validation does not accept the decision or activate incident response.

## Non-effects

This proposal does not:

- accept `ACCEPT_SPLIT`;
- activate or declare an incident;
- verify the reporting mailbox or private escalation route;
- expose or modify restricted procedure;
- name an individual incident commander;
- move, rename, alias, consolidate, retire, or delete either existing path;
- change credentials, access, policy, infrastructure, runtime, release,
  deployment, lifecycle, or publication state; or
- authorize public disclosure.

## Change history

| Version | Date | Change |
| --- | --- | --- |
| `v1.0` | 2026-08-15 | Initial evidence-backed `ACCEPT_SPLIT` proposal and finite handoff contract. |

[Back to top](#top)
