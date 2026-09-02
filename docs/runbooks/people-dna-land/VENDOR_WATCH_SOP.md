<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-vendor-watch
title: People/DNA/Land Vendor-Signal Review SOP
type: runbook
version: v1.0.0
prior_state: explicit scaffold with no review procedure, cadence boundary, trigger model, evidence rules, or escalation handoff
status: DRAFT_REPOSITORY_GROUNDED; MANUAL_REPOSITORY_REVIEW_ONLY; NO_LIVE_MONITOR; NO_VENDOR_ACCESS; NO_REAL_DNA; NO_SOURCE_OR_LIFECYCLE_MUTATION; NON_RELEASE; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, source, data-custody, security, policy, evidence, release, operations, and independent-review assignments"
created: 2026-08-29
updated: 2026-08-29
policy_label: repository-facing; sensitive-domain; vendor-signal-review; manual-review-only; fail-closed; non-release; non-publication
current_path: docs/runbooks/people-dna-land/VENDOR_WATCH_SOP.md
owning_root: docs/
responsibility: Define a bounded human procedure for reviewing repository-visible vendor-risk evidence, classifying material signals, and preparing a minimized escalation handoff without monitoring vendors, accessing accounts, changing source state, handling sensitive payloads, or executing containment, cleanup, release, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, source descriptors and activation decisions, contracts, schemas, policy, rights and consent authority, sensitivity and sovereignty review, evidence, lifecycle, correction, withdrawal, release, rollback, and accountable operations
canonical_relationship: same-path replacement of an explicit scaffold; no sibling watcher, source, policy, contract, incident, receipt, proof, or release authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 7809fe45aeae513ebcc71c31beffab6c75bcbd84
  target_prior_blob: 84d77e7e9a9d4afb2ee367ff11841a837bdf1a8c
  runbook_index_prior_blob: 49c5fe79f9c788c669d86b22b9c1af93ad8dd398
  vendor_loss_drill_prior_blob: 7cb10c27fe20c1da2b4aa69958cc5ad446c6d714
  source_registry_blob: 0b448fbd535f80f32acde7ad2c35414f492297d0
  preservation_matrix_blob: 6169ce3513ac9a4f9b74e23fe2bbc1a1ad8fea61
  registry_boundary_blob: 98a90286e6b3d7ad49a64158be666e34ba6c1720
  ftDNA_connector_blob: 4911140dd70b77f2ed5a45362f8e30100061fba8
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  verified_vendor_watch_service: NONE_FOUND_AT_PINNED_REVISION
  verified_vendor_signal_fixture_or_validator: NONE_FOUND_AT_PINNED_REVISION
  verified_external_monitoring_cadence: NONE_FOUND_AT_PINNED_REVISION
related:
  - ./README.md
  - ./DTC_VENDOR_LOSS_DRILL.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./CONSENT_RUNBOOK.md
  - ./revocation.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/DNA_HANDLING.md
  - ../../domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../domains/people-dna-land/PRESERVATION_MATRIX.md
  - ../../domains/people-dna-land/SOURCE_LEDGER.md
  - ../../../connectors/ftDNA/README.md
  - ../../../data/registry/sources/people-dna-land/README.md
  - ../../../.github/workflows/domain-people-dna-land.yml
non_effects:
  - does_not_assert_any_real_vendor_condition
  - does_not_create_or_run_a_monitor_scheduler_scraper_connector_or_alert
  - does_not_access_vendor_accounts_apis_exports_credentials_or_private_messages
  - does_not_process_real_people_dna_relationship_land_consent_or_account_payloads
  - does_not_admit_activate_deactivate_or_reclassify_a_source
  - does_not_mutate_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_preserve_transfer_delete_erase_or_invalidate_data_or_derivatives
  - does_not_contact_subjects_vendors_regulators_reviewers_or_the_public
  - does_not_approve_review_policy_release_deployment_promotion_or_publication
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Vendor-Signal Review SOP

Use this SOP to perform a **bounded human review of already available, repository-visible vendor-risk evidence** and prepare a minimized handoff. It replaces the prior scaffold with a review procedure; it does not create continuous monitoring, authorize live research or vendor access, establish a vendor's current condition, or execute any response.

> [!CAUTION]
> Never place real names, family relationships, DNA or genomic values, raw kit or vendor identifiers, credentials, account URLs, consent records, export files, segment coordinates, private addresses, exact locations, protected cultural information, private vendor correspondence, or proprietary source excerpts in this procedure, Git, pull requests, issues, CI logs, screenshots, or public artifacts.

> [!IMPORTANT]
> A signal is not a decision. Availability, ownership or control, terms, rights, consent, revocation, integrity, custody, sensitivity, retention, erasure, source role, lifecycle state, correction, withdrawal, release, and publication remain separate questions owned by their governing surfaces and accountable reviewers.

**Navigation:** [Authority](#1-purpose-and-authority-boundary) · [Evidence](#2-current-repository-evidence) · [Modes](#3-current-review-mode-and-cadence) · [Signals](#4-signal-taxonomy) · [Sources](#5-admissible-evidence-and-rejected-inputs) · [Stop](#6-mandatory-stop-conditions) · [Roles](#7-role-cards) · [Preflight](#8-preflight) · [Procedure](#9-review-procedure) · [Outcomes](#10-finite-outcomes) · [Handoff](#11-minimized-handoff-record) · [Escalation](#12-escalation-routing) · [Acceptance](#13-acceptance-criteria) · [Gaps](#14-operational-graduation-gaps) · [Maintenance](#15-maintenance-correction-and-rollback)

## 1. Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md). Human procedures belong under `docs/runbooks/`; source descriptors, machine contracts, schemas, policy, fixtures, tests, registry data, evidence, receipts, proofs, incident records, release decisions, and operational controls retain their own responsibility roots.

This same-path replacement may:

- define signal categories, evidence rules, stop conditions, and finite review outcomes;
- compare an already captured signal with repository-visible source and governance posture;
- expose missing owners, descriptors, contracts, policy bindings, evidence, or response capabilities;
- route a fictional severe scenario to the [vendor-loss tabletop](./DTC_VENDOR_LOSS_DRILL.md);
- produce a minimized, non-sensitive handoff for accountable review.

It may not:

- claim that a real vendor is healthy, degraded, distressed, breached, acquired, insolvent, unavailable, or winding down;
- create or operate a watcher, scheduler, scraper, connector, browser session, API client, notification service, or incident responder;
- log in, retrieve exports, inspect private communications, use credentials, or test a real account;
- issue, validate, broaden, revoke, or reinterpret consent;
- decide source admission, source authority, rights, sensitivity, custody, retention, erasure, or legal obligations;
- change a source descriptor, activation decision, lifecycle state, policy bundle, release, public artifact, or downstream carrier;
- execute preservation, containment, quarantine, transfer, deletion, erasure, invalidation, correction, withdrawal, rollback, notification, release, deployment, promotion, or publication.

[Back to top](#top)

## 2. Current repository evidence

The following boundary was checked against `main@7809fe45aeae513ebcc71c31beffab6c75bcbd84`.

| Surface | Confirmed current state | Safe conclusion |
|---|---|---|
| This file before replacement | Explicit scaffold | No vendor-signal review procedure existed at this path |
| [`SOURCE_REGISTRY.md`](../../domains/people-dna-land/SOURCE_REGISTRY.md) | Documents a proposed vendor capability/TOS register and documentary vendor-risk fields | Vendor-risk vocabulary exists in prose; no binding vendor-health resolver or activation effect was verified |
| [`PRESERVATION_MATRIX.md`](../../domains/people-dna-land/PRESERVATION_MATRIX.md) | Draft reading aid discusses vendor-loss and terms-change responses | It may inform questions; it does not authorize preservation, embargo, demotion, erasure, correction, or cache action |
| [`DTC_VENDOR_LOSS_DRILL.md`](./DTC_VENDOR_LOSS_DRILL.md) | Repository-grounded fictional, synthetic-metadata tabletop | A material hypothetical signal can be rehearsed without asserting or responding to a real event |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Repository-grounded `HOLD` boundary for repository-only source-head review | This SOP cannot retrieve a live source or turn a signal into refresh authority |
| [`data/registry/sources/people-dna-land/`](../../../data/registry/sources/people-dna-land/README.md) | Registry boundary documents unresolved topology and source-governance limits | Do not create or mutate a descriptor from this runbook |
| [`connectors/ftDNA/`](../../../connectors/ftDNA/README.md) | Documentation-plus-placeholder connector lane; live behavior inactive | Do not invoke or treat the connector as monitoring or vendor-access implementation |
| [People/DNA/Land workflow](../../../.github/workflows/domain-people-dna-land.yml) | Runs two bounded synthetic consent profiles | No vendor-signal fixture, validator, monitor, or response executor was verified at the pinned revision |

The April 2026 People/Genealogy/DNA/Land architecture blueprint in Google Drive was consulted as read-only design lineage. It supports restricted-by-default DNA handling and evidence-bound vendor-risk review, but it was prepared without a mounted repository and does not prove current implementation.

[Back to top](#top)

## 3. Current review mode and cadence

### 3.1 Mode A — repository-visible review

**Available now as documentation:** a reviewer may inspect an exact repository revision, compare already captured non-sensitive evidence with current repository-visible source posture, classify gaps, and prepare a minimized handoff. The review must remain no-account, no-credential, no-payload, and no-mutation.

### 3.2 Mode B — external signal acquisition

**`HOLD`:** live web checks, vendor pages, terms snapshots, regulatory or court lookups, API probes, account checks, alerts, feeds, scraping, and notifications require a separately approved source-access and evidence-capture procedure. This SOP does not supply one.

### 3.3 Cadence

No recurring cadence, scheduler, watcher owner, evidence-capture route, or service-level target was verified at the pinned revision. Therefore:

- do not describe this SOP as continuous, hourly, daily, weekly, or automated monitoring;
- a review may begin only from an explicit human request or an already captured, admissible signal;
- a future cadence must name the accountable owner, vendor/source scope, authorized evidence sources, retention rule, escalation route, review deadline, missed-run behavior, and scheduler authority in their governing surfaces;
- a scheduled task, Notion page, issue, or document alone is not monitoring implementation or source-access authority.

[Back to top](#top)

## 4. Signal taxonomy

Classify a signal on independent axes. Do not collapse it into a single label such as “vendor risk.”

| Signal category | Review question | Never infer automatically |
|---|---|---|
| Availability | Is a service, export, revocation route, or support channel reported degraded or unavailable? | Insolvency, breach, data loss, or permission to retrieve |
| Ownership or control | Is a change in ownership, operator, jurisdiction, or controller reported? | Rights continuity, consent transfer, source admission, or safe custody |
| Terms or privacy posture | Is a material change to terms, privacy, retention, deletion, research, redistribution, or automation reported? | Legal effect, acceptance, permission, or retroactive scope |
| Product or export capability | Is a format, endpoint, download, match, segment, or account feature reported changed? | Connector compatibility or authority to probe an account |
| Integrity or custody | Is corruption, provenance loss, unauthorized access, or custody uncertainty reported? | Verified incident scope, affected records, or containment |
| Consent or revocation reachability | Is a consent, withdrawal, deletion, or revocation mechanism reported changed or unreachable? | Actual consent status, completed revocation, erasure, or cleanup |
| Legal, regulatory, or financial event | Is an authoritative filing, order, enforcement action, restructuring, or wind-down reported? | Operational effect on KFM, rights, custody, or source state |
| Security or privacy incident | Is an incident reported by an admissible source? | Affected identities, DNA, accounts, or KFM exposure |

One signal may occupy several categories. Record each axis separately and preserve `UNKNOWN` when the evidence does not resolve it.

[Back to top](#top)

## 5. Admissible evidence and rejected inputs

### 5.1 Evidence hierarchy

Use the highest available class and preserve direct references:

1. authenticated KFM source, evidence, policy, review, or incident records already present in their approved responsibility roots;
2. official vendor notices, filed terms or privacy documents, authoritative court or regulator records, and signed contractual notices **only when an approved external acquisition and capture path supplies them**;
3. independently corroborated, reputable reporting captured through an approved research path;
4. secondary summaries as discovery leads only, never as sole support for a material state claim.

For every admitted item, record origin, observation time, publication or effective time when known, capture method, immutable reference or digest when the owning system supplies one, and any access, rights, completeness, or authenticity limit.

### 5.2 Rejected as decision evidence

- rumor, anonymous posts, social-media repetition, search snippets, advertisements, or screenshots without origin;
- generated text, AI summaries, maps, dashboards, indexes, alerts, or confidence scores without resolving their underlying evidence;
- availability checks, DNS results, payment status, stock movement, or a single unreachable page used as proof of vendor health or legal condition;
- private vendor or subject communications copied into repository-visible surfaces;
- any evidence obtained through unapproved login, scraping, automation, credential use, account access, or terms circumvention.

If admissible evidence is absent, choose `NOT_RUN`, `HOLD`, `ABSTAIN`, or `ERROR`; do not fill the gap with plausibility.

[Back to top](#top)

## 6. Mandatory stop conditions

Stop and record `HOLD` or `ESCALATE` when the review would require or encounters:

- a real person, family, kit, match, segment, genotype, health, ancestry, address, parcel, account, consent, or protected-cultural payload;
- a credential, token, account URL, session cookie, recovery code, private message, export, or proprietary source excerpt;
- a live login, API call, scrape, download, support request, vendor contact, regulator contact, or external notification;
- an unapproved external evidence-capture path or unclear source terms;
- a source activation, connector run, watcher change, lifecycle mutation, quarantine action, cache purge, graph/index rebuild, correction, withdrawal, release, deployment, or publication;
- an unresolved rights, consent, living-person, sovereignty, cultural-protocol, legal, security, custody, retention, erasure, or accountable-review question;
- pressure to name affected people, records, kits, accounts, locations, or private dependencies in a repository-visible handoff;
- an attempt to treat this documentation review as incident containment, legal advice, current vendor certification, or response approval.

If sensitive material is exposed, do not reproduce it. Minimize further exposure, preserve only safe audit facts, and route the event to the approved security, privacy, legal, and stewardship channels.

[Back to top](#top)

## 7. Role cards

| Role | Review responsibility | May not claim |
|---|---|---|
| Review coordinator | Freezes scope, evidence boundary, timestamps, and stop conditions | Source, legal, consent, incident, release, or operational authority |
| Source reviewer | Compares the signal with current descriptor, source role, rights, terms, and activation posture | That the source is admitted, denied, healthy, or changed without the owning decision |
| Privacy and consent reviewer | Identifies living-person, DNA, third-party, consent, revocation, and minimization concerns | That consent is valid, transferred, revoked, or legally sufficient |
| Security and custody reviewer | Identifies integrity, account, access, retention, deletion, and custody questions | That an incident occurred, scope is known, or containment completed |
| Sovereignty and rights reviewer | Identifies Indigenous/Tribal, descendant-community, cultural-protocol, jurisdiction, and rights concerns | Authority on behalf of an unrepresented community or rights holder |
| Derivative and release reviewer | Identifies potentially affected evidence, answer, export, tile, graph, index, cache, and release classes | That correction, withdrawal, invalidation, rollback, or release change executed |
| Independent observer | Records ambiguity, unsupported shortcuts, missing evidence, and combined roles | Independent approval when also serving an owning role |

For a small review, one person may simulate several roles, but the handoff must disclose the combination. Simulated coverage is not accountable or independent approval.

[Back to top](#top)

## 8. Preflight

Do not begin until all applicable items are satisfied:

- [ ] Exact repository revision and SOP version are recorded.
- [ ] The vendor/source is represented by an opaque, non-sensitive review reference.
- [ ] Review mode is `REPOSITORY_VISIBLE_ONLY`; any external acquisition is separately authorized and evidenced.
- [ ] No real account, export, payload, credential, consent record, private communication, or proprietary excerpt will be used.
- [ ] The signal origin, observation time, event/effective time if known, and capture boundary are recorded.
- [ ] Applicable source, rights, consent, sensitivity, custody, retention, and stewardship authority surfaces are named or marked `UNKNOWN`.
- [ ] Participants understand that no source, lifecycle, policy, incident, cleanup, correction, withdrawal, release, or publication state can change through this SOP.
- [ ] A safe location for the minimized result record is selected.
- [ ] Escalation routes are named or recorded as `NEEDS VERIFICATION`.

A missing prerequisite produces `NOT_RUN` and `HOLD`; do not improvise around it.

[Back to top](#top)

## 9. Review procedure

### 9.1 Freeze the evidence boundary

Record the exact repository revision, SOP version, opaque source reference, review request, reviewer roles, permitted evidence set, timestamps, and known gaps. Use UTC for recorded times. Do not use memory or prior summaries as current evidence.

### 9.2 Normalize the signal without expanding it

Record only:

- signal category or categories from [§4](#4-signal-taxonomy);
- what the admitted evidence directly supports;
- what remains unknown or disputed;
- observation time separately from event or effective time;
- evidence origin and stable reference;
- why the signal may be material to KFM.

Do not copy payloads, names, account details, sensitive values, or long proprietary excerpts.

### 9.3 Check corroboration and freshness

For a material claim, require either one authoritative primary source or two genuinely independent admissible sources. Record any conflict, stale timestamp, supersession, inaccessible evidence, or missing effective date. A later summary that repeats the same upstream report is not independent corroboration.

### 9.4 Compare independent control axes

| Axis | Review values | Fail-closed question |
|---|---|---|
| Availability | stable / degraded / unavailable / unknown | Can the relevant service or function be relied on? |
| Ownership or control | unchanged / changed / disputed / unknown | Who controls the source and obligations? |
| Rights and terms | unchanged / changed / unresolved / unknown | Is continued possession, use, transfer, automation, or derivation allowed? |
| Consent and revocation | satisfied / revoked / expired / unreachable / unknown | Does the exact purpose and audience remain permitted? |
| Integrity and custody | verified / suspect / unknown | Are provenance, custody, and data integrity trustworthy? |
| Product compatibility | compatible / changed / unsupported / unknown | Does an approved connector or format contract still match? |
| Sensitivity and sovereignty | resolved / restricted / denied / unknown | What handling or exposure is permitted, if any? |
| Lifecycle and release | internal / candidate / released / corrected / withdrawn / unknown | Which governed state is actually established? |

Any `unknown`, `unresolved`, `unreachable`, `suspect`, `restricted`, `denied`, or `unsupported` value blocks automatic continuation.

### 9.5 Map affected classes, not records

Use class-level questions only:

| Surface | Question | Permitted review output |
|---|---|---|
| Source descriptor and activation | Could source role, rights, terms, control, cadence, or activation require accountable review? | handoff requirement; no descriptor mutation |
| RAW / WORK / QUARANTINE | Could restricted captures or candidates depend on the source? | dependency class; no record enumeration or movement |
| PROCESSED / evidence | Could derived assertions or evidence references depend on it? | review class; no claim invalidation |
| CATALOG / TRIPLET | Could a catalog or graph projection carry the dependency? | review class; no rebuild |
| PUBLISHED / release | Could a released carrier require correction or withdrawal review? | escalation only; no public-state change |
| Runtime derivatives | Could answers, exports, tiles, graphs, indexes, or caches expose a dependency? | affected carrier classes; no purge or invalidation |

Do not search sensitive stores or enumerate real records under this SOP.

### 9.6 Choose a finite outcome

Apply [§10](#10-finite-outcomes). Record the evidence and reason for the outcome. A severe but unverified signal normally produces `HOLD` or `ESCALATE`, not a declaration about vendor condition.

### 9.7 Prepare the handoff

Complete the minimized record in [§11](#11-minimized-handoff-record). Route it to the accountable owners identified by the affected axes. If a fictional rehearsal would help expose dependency gaps, invoke the [vendor-loss tabletop](./DTC_VENDOR_LOSS_DRILL.md) without converting the real signal into a drill fact.

[Back to top](#top)

## 10. Finite outcomes

| Outcome | Meaning in this SOP | Non-effect |
|---|---|---|
| `NO_MATERIAL_CHANGE` | Admitted evidence does not support a material change from the recorded repository-visible baseline | Does not certify vendor health, freshness, rights, consent, or source safety |
| `REVIEW_REQUIRED` | A credible signal may affect one or more control axes and needs an accountable decision | Does not change source, policy, lifecycle, or release state |
| `HOLD` | Required evidence, authority, rights, consent, custody, sensitivity, retention, or implementation is unresolved | Does not execute quarantine, containment, or withdrawal |
| `ABSTAIN` | Available evidence cannot support the requested vendor-state or dependency conclusion | Does not resolve the claim through inference or generated language |
| `ESCALATE` | A privacy, security, legal, sovereignty, consent, custody, incident, or public-exposure concern requires an accountable route | Does not contact external parties or approve a response |
| `NOT_RUN` | Preconditions were not met | Does not imply no risk |
| `ERROR` | Evidence could not be parsed, resolved, authenticated, or compared within the approved boundary | Does not authorize fallback inference |

`NO_MATERIAL_CHANGE` is the strongest positive result available here. This SOP cannot emit `PASS`, `APPROVED`, `HEALTHY`, `CONTAINED`, `CLOSED`, `RELEASED`, or `PUBLISHED` for a real vendor or response.

[Back to top](#top)

## 11. Minimized handoff record

Use this Markdown shape with opaque references and no sensitive values:

```markdown
- record_type: VENDOR_SIGNAL_REVIEW_HANDOFF
- review_id: kfm:vendor-signal-review:synthetic-or-opaque-id
- repository_revision: <exact SHA>
- sop_version: v1.0.0
- review_mode: REPOSITORY_VISIBLE_ONLY
- source_ref: <opaque non-sensitive reference>
- observed_at_utc: <timestamp>
- event_or_effective_at_utc: <timestamp | UNKNOWN>
- signal_categories: [<finite categories>]
- admitted_evidence_refs: [<stable references>]
- evidence_limits: [<limits or UNKNOWN>]
- axis_results:
    availability: <value>
    ownership_or_control: <value>
    rights_and_terms: <value>
    consent_and_revocation: <value>
    integrity_and_custody: <value>
    product_compatibility: <value>
    sensitivity_and_sovereignty: <value>
    lifecycle_and_release: <value>
- potentially_affected_classes: [<source / lifecycle / carrier classes only>]
- outcome: <NO_MATERIAL_CHANGE | REVIEW_REQUIRED | HOLD | ABSTAIN | ESCALATE | NOT_RUN | ERROR>
- reason_codes: [<bounded codes>]
- required_review_routes: [<roles or NEEDS_VERIFICATION>]
- prohibited_actions_confirmed: true
- open_questions: [<minimized questions>]
- next_review_trigger: <explicit trigger | NEEDS_VERIFICATION>
```

This template is illustrative documentation, not a binding contract, schema, receipt, incident record, source record, or release object. Do not present a completed Markdown block as authenticated proof.

[Back to top](#top)

## 12. Escalation routing

| Finding | Minimum route | Keep held |
|---|---|---|
| Availability or product change only | Source owner, connector owner, operations | live probe, refresh, connector change, source mutation |
| Ownership, control, terms, or rights change | Source owner, legal/rights reviewer, privacy/consent reviewer | continued use, transfer, retention, automation, release |
| Consent or revocation uncertainty | Consent/privacy owner, legal reviewer, data custodian | use, derivation, rendering, cleanup, deletion, closure |
| Security, integrity, or custody concern | Security and custody owners, privacy/legal as applicable | account access, containment, evidence collection, notification |
| Indigenous/Tribal or culturally restricted impact | Applicable sovereign or community steward and rights reviewer | review, use, generalization, transfer, publication |
| Potential released-carrier impact | Evidence, correction/withdrawal, release, operations, independent review | correction, withdrawal, purge, rollback, republication |
| No verified accountable route | Repository owner for routing plus `HOLD` | implied approval or self-authorization |

This table routes questions. It does not appoint reviewers, satisfy separation of duties, create an incident, or authorize action.

[Back to top](#top)

## 13. Acceptance criteria

A review under this SOP is acceptable only when:

- [ ] the exact repository revision, SOP version, mode, and timestamps are recorded;
- [ ] evidence is admissible, directly referenced, minimized, and separated from inference;
- [ ] every signal is classified on independent control axes;
- [ ] unknowns, conflicts, and stale evidence remain visible;
- [ ] no real sensitive payload, credential, private message, account detail, or proprietary excerpt enters a repository-visible surface;
- [ ] affected classes are recorded without enumerating real records;
- [ ] the outcome is one of the finite values in [§10](#10-finite-outcomes);
- [ ] no source, policy, lifecycle, incident, cleanup, correction, withdrawal, release, deployment, or publication effect is claimed;
- [ ] combined roles and missing accountable routes are disclosed;
- [ ] the handoff identifies the next trigger or records it as `NEEDS VERIFICATION`.

A truthful `HOLD`, `ESCALATE`, `NOT_RUN`, or `ERROR` can satisfy this SOP. Review completion is not operational readiness.

[Back to top](#top)

## 14. Operational graduation gaps

Do not describe this lane as operational vendor monitoring until current implementation authority establishes and verifies all of the following in their owning roots:

1. accepted vendor/source scope and unique authoritative descriptors;
2. current rights, terms, privacy, consent, revocation, retention, deletion, sensitivity, sovereignty, custody, and source-role decisions;
3. an approved external evidence-source allowlist and capture method with provenance, timestamps, immutable identity, rights handling, and supersession;
4. an authenticated cadence owner, scheduler authority, missed-run behavior, review deadlines, and alert-delivery route;
5. machine contracts and schemas for signal, evidence, materiality, finite outcomes, and handoffs;
6. active policy-runtime binding for purpose, audience, role, data class, time, living status, consent, rights, source role, harmful precision, and sovereignty;
7. deterministic synthetic fixtures, negative cases, validators, tests, and no-network default behavior;
8. verified deduplication, stale-signal, conflicting-source, replay, outage, false-positive, false-negative, and evidence-supersession behavior;
9. credential isolation, allowlisted egress, bounded retrieval, logging minimization, retention, deletion, incident response, and rollback for the monitor itself;
10. accountable source, privacy, consent, Indigenous/Tribal, legal, security, custody, policy, evidence, operations, release, and independent review as applicable;
11. separately governed containment, correction, withdrawal, revocation, deletion, invalidation, notification, and rollback mechanisms with auditable results; and
12. exact-head local and hosted evidence whose limitations are recorded without being mistaken for current vendor truth or response completion.

Missing any item keeps live monitoring and automated response at `HOLD`.

[Back to top](#top)

## 15. Maintenance, correction, and rollback

Review this SOP when the source-registry vocabulary, connector maturity, consent or revocation contract, evidence model, policy binding, vendor-loss drill, incident routing, or release/correction boundary changes. Refresh pinned evidence before changing any current-state claim.

For a documentation-only change:

- review the complete diff and all affected navigation and maturity counts;
- validate one H1, heading order, anchors, tables, fences, relative links, metadata, and final newline;
- run repository-native documentation and People/DNA/Land checks selected for the changed paths;
- classify inherited, external, skipped, unavailable, and pending checks separately;
- keep specialist and independent human review pending unless authenticated evidence proves it.

Before merge, close the draft pull request to abandon the change. After a separately authorized merge, revert the focused documentation commit or apply a reviewed forward correction.

Reverting this file restores the prior scaffold or earlier prose only. It does not stop monitoring, retract a signal, change a source, reverse consent, contain an incident, restore data, invalidate derivatives, withdraw a release, undo a notification, or alter public state.

[Back to top](#top)
