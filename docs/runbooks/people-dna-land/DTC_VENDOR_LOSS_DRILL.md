<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-dtc-vendor-loss-drill
title: People/DNA/Land Direct-to-Consumer Vendor-Loss Tabletop Drill
type: runbook
version: v1.0.1
prior_version: v1.0.0
prior_state: repository-grounded synthetic-metadata tabletop whose vendor-watch references still classified the sibling SOP as an explicit scaffold
status: DRAFT_REPOSITORY_GROUNDED; TABLETOP_AND_SYNTHETIC_METADATA_ONLY; NO_VENDOR_ACCESS; NO_REAL_DNA; NO_OPERATIONAL_CONTAINMENT; NON_RELEASE; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, legal, Indigenous/Tribal, source, data-custody, security, policy, evidence, release, operations, and independent-review assignments"
created: 2026-08-28
updated: 2026-08-29
policy_label: repository-facing; sensitive-domain; direct-to-consumer-vendor; tabletop-only; synthetic-metadata-only; fail-closed; non-release; non-publication
current_path: docs/runbooks/people-dna-land/DTC_VENDOR_LOSS_DRILL.md
owning_root: docs/
responsibility: Human tabletop procedure for rehearsing the loss, distress, control change, or material unavailability of a direct-to-consumer genealogy or DNA vendor without accessing a real account, using real sensitive data, changing source or lifecycle state, or executing containment, deletion, release, deployment, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, source descriptors and activation decisions, contracts, schemas, policy, consent and rights authority, sensitivity and sovereignty review, evidence, lifecycle, correction, withdrawal, release, rollback, and accountable operations
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8f74d6d7d10d576062dda51684ef4eb6e97f4831
  vendor_watch_reconciliation_base_commit: 7809fe45aeae513ebcc71c31beffab6c75bcbd84
  target_prior_blob: 571bbc05eba34df936d825b3b75fafb00593e0be
  runbook_index_prior_blob: 2418f3c5643bf8d119e3e97b38293f29721e7f92
  vendor_watch_sop_state: REPOSITORY_GROUNDED_MANUAL_REVIEW_ONLY
  vendor_watch_prior_blob: 84d77e7e9a9d4afb2ee367ff11841a837bdf1a8c
  inspected_ftdna_connector_state: GREENFIELD_PLACEHOLDER_NOT_ACTIVATED
  verified_vendor_loss_fixture_or_validator: NONE_FOUND_AT_PINNED_REVISION
  verified_operational_vendor_loss_execution: NONE_FOUND_AT_PINNED_REVISION
related:
  - ./README.md
  - ./CONSENT_RUNBOOK.md
  - ./LIVING_PERSON_REVIEW.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./VENDOR_WATCH_SOP.md
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
  - does_not_assert_that_any_named_vendor_is_distressed_unavailable_or_insolvent
  - does_not_access_vendor_accounts_apis_exports_or_credentials
  - does_not_process_real_people_dna_relationship_land_or_consent_payloads
  - does_not_download_preserve_transfer_delete_or_erase_vendor_data
  - does_not_issue_revoke_or_reinterpret_consent
  - does_not_activate_deactivate_or_reclassify_a_source
  - does_not_mutate_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_purge_cache_tiles_graphs_indexes_or_exports
  - does_not_contact_subjects_vendors_regulators_or_the_public
  - does_not_approve_review_policy_release_deployment_promotion_or_publication
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Direct-to-Consumer Vendor-Loss Tabletop Drill

Use this runbook to rehearse one **synthetic, no-account, no-network vendor-loss scenario** and produce a minimized reviewer handoff. It is a tabletop procedure, not a vendor monitor, incident-response service, consent authority, data-custody tool, cleanup executor, legal determination, or release gate.

> [!CAUTION]
> Never place real names, family relationships, DNA or genomic values, raw kit or vendor identifiers, credentials, account URLs, consent records, export files, segment coordinates, private addresses, exact locations, protected cultural information, or proprietary source excerpts in this drill, Git, pull requests, issues, CI logs, screenshots, or public artifacts.

> [!IMPORTANT]
> A vendor-loss event does not create a right to download everything, preserve everything, transfer custody, delete records, infer consent, or publish derived results. Availability, source authority, rights, consent, sensitivity, integrity, retention, erasure, correction, and release remain separate gates.

**Navigation:** [Authority](#1-purpose-and-authority-boundary) · [Evidence](#2-current-repository-evidence) · [Objectives](#3-drill-objectives) · [Stop](#4-mandatory-stop-conditions) · [Scenario](#5-scenario-contract) · [Roles](#6-role-cards) · [Preconditions](#7-preconditions) · [Procedure](#8-tabletop-procedure) · [Outcomes](#9-result-interpretation) · [Record](#10-minimum-result-record) · [Acceptance](#11-acceptance-criteria) · [Gaps](#12-operational-graduation-gaps) · [Maintenance](#13-maintenance-correction-and-rollback)

## 1. Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md). Human procedures belong under `docs/runbooks/`; source descriptors, machine contracts, schemas, policy, fixtures, tests, data instances, evidence, receipts, proofs, release decisions, and operational controls retain their own responsibility roots.

This same-path replacement turns an explicit scaffold into a repository-grounded tabletop procedure. It may:

- define a synthetic vendor-loss scenario and its stop conditions;
- help reviewers identify affected object families and downstream carriers without inspecting sensitive payloads;
- rehearse a fail-closed decision sequence;
- expose missing owners, contracts, registries, validators, and cleanup capabilities;
- produce a minimized, non-sensitive handoff for accountable review.

It may not:

- claim that a real vendor is distressed, insolvent, unavailable, acquired, compromised, or winding down;
- access an account, API, export, browser session, credential, or vendor support channel;
- download, copy, transfer, retain, erase, or destroy real data;
- issue, revoke, validate, broaden, or reinterpret consent;
- decide source admission, source authority, rights, sensitivity, retention, erasure, or legal obligations;
- activate a connector, watcher, policy bundle, source, cleanup job, cache purge, rollback, or notification path;
- change lifecycle, release, deployment, promotion, or publication state.

[Back to top](#top)

## 2. Current repository evidence

The following boundary was checked against `main@8f74d6d7d10d576062dda51684ef4eb6e97f4831`.

| Surface | Confirmed current state | Safe conclusion |
|---|---|---|
| This file before replacement | Explicit scaffold with no procedure | No vendor-loss drill was operational at the target path |
| [`SOURCE_REGISTRY.md`](../../domains/people-dna-land/SOURCE_REGISTRY.md) | Documents a proposed vendor capability/TOS register and a documentary `vendor_solvency_class` field | Vendor-risk concepts exist in prose; a binding machine schema, resolver, and activation effect were not found |
| [`PRESERVATION_MATRIX.md`](../../domains/people-dna-land/PRESERVATION_MATRIX.md) | Draft reading aid proposes embargo, promotion hold, correction, tombstone, and cache-response considerations | It informs the tabletop but does not authorize operational containment, retention, erasure, or cleanup |
| [`DNA_HANDLING.md`](../../domains/people-dna-land/DNA_HANDLING.md) | Requires deny-by-default handling, encrypted/access-scoped raw DTC material, revocable consent, and no raw-genotype republication | Vendor loss cannot weaken DNA, living-person, consent, or publication controls |
| [`VENDOR_WATCH_SOP.md`](./VENDOR_WATCH_SOP.md) | Repository-grounded manual-review draft | It classifies already available, repository-visible signals and prepares a minimized handoff; continuous monitoring, external acquisition, current-vendor certification, and response execution remain unavailable |
| [`connectors/ftDNA/README.md`](../../../connectors/ftDNA/README.md) | Greenfield placeholder lane; no approved account path, parser, consent integration, executable tests, source activation, or live access | This runbook cannot invoke or treat that connector as operational |
| [People/DNA/Land workflow](../../../.github/workflows/domain-people-dna-land.yml) | Executes two bounded synthetic consent profiles | No vendor-loss fixture, validator, or operational containment profile was found at the pinned revision |
| Real DTC accounts or exports | Not admitted or inspected by this documentation task | Keep all real material outside repository-visible drill records |

The April 2026 People/Genealogy/DNA/Land architecture blueprint in Google Drive was used as read-only design lineage. It supports restricted-by-default DNA handling and the value of rehearsing vendor loss, but it was created without a mounted repository and does not prove current implementation.

[Back to top](#top)

## 3. Drill objectives

A successful tabletop should determine whether the team can, **without touching real data or external systems**:

1. identify the authority and evidence needed to classify a vendor-loss signal;
2. separate availability, ownership/control, terms, rights, consent, integrity, sensitivity, retention, and release questions;
3. map synthetic source dependencies through the KFM lifecycle and derived carriers;
4. choose fail-closed work states without pretending that containment has executed;
5. identify which accountable roles and machine capabilities are missing;
6. prepare a minimized handoff with exact revision, assumptions, gaps, and rollback boundary.

The drill is allowed to find gaps. A truthful `FAIL`, `HOLD`, or `ESCALATE` is better than a fluent but unsupported declaration of readiness.

[Back to top](#top)

## 4. Mandatory stop conditions

Stop the drill and record `HOLD` or `ESCALATE` when any participant proposes or encounters:

- a real person, family, kit, match, segment, genotype, health, ancestry, address, parcel, account, or consent payload;
- a credential, token, account URL, session cookie, recovery code, or private vendor communication;
- a live vendor lookup, login, download, API call, scrape, support request, or external notification;
- a physical deletion, legal erasure, custody transfer, retention extension, or bulk preservation action;
- a real source activation, connector run, watcher change, lifecycle mutation, cache purge, graph/index cleanup, release, deployment, or publication;
- an unresolved rights, consent, living-person, sovereignty, cultural-protocol, legal, security, or data-custody question;
- an attempt to treat vendor availability, a terms page, a payment status, a rumor, generated text, or a map as evidence of a real vendor condition;
- an attempt to use this runbook as approval for real incident response.

When sensitive material is accidentally exposed, do not reproduce it in the drill record. Minimize further exposure, preserve only safe audit facts, and route the event to the approved incident and accountable-review channels.

[Back to top](#top)

## 5. Scenario contract

Use one fictional source identity and fictional dependency identifiers.

### 5.1 Required scenario

| Field | Required value |
|---|---|
| Scenario type | `SIMULATED_DTC_VENDOR_LOSS` |
| Source identity | `kfm:source:synthetic-dtc-vendor` |
| Trigger | Vendor service and control posture are simulated as materially unavailable or unresolved |
| Data | Synthetic metadata only; no payload values |
| Network | Off |
| Vendor/account access | None |
| External writes or communications | None |
| Lifecycle mutation | None |
| Public effect | None |

### 5.2 Optional injects

The coordinator may add one or more fictional injects:

- export access becomes unavailable;
- a source's ownership or control changes;
- terms, privacy commitments, or redistribution posture become unresolved;
- consent or revocation lookup becomes unavailable;
- data integrity or custody cannot be verified;
- a connector contract no longer matches the source;
- an existing derivative may depend on the source;
- retention and erasure obligations appear to conflict;
- a public carrier may need correction or withdrawal review.

Each inject is a question to investigate, not a statement about any real company.

### 5.3 Synthetic dependency set

Use opaque fictional IDs only:

```text
source_descriptor_ref: kfm:source-descriptor:synthetic-dtc-vendor:v1
raw_capture_ref:       kfm:raw:synthetic-dtc-vendor:run-001
work_record_ref:       kfm:work:synthetic-dtc-vendor:candidate-001
evidence_ref:          kfm:evidence-ref:synthetic-vendor-derived-001
catalog_ref:           kfm:catalog:synthetic-vendor-derived-001
release_ref:           kfm:release:synthetic-vendor-derived-001
cache_ref:             kfm:cache:synthetic-vendor-derived-001
```

These values are illustrative drill tokens. They are not contract-valid instances, proof of repository objects, or permission to create those objects.

[Back to top](#top)

## 6. Role cards

| Role | Tabletop responsibility | May not claim |
|---|---|---|
| Drill coordinator | Maintains scope, injects, timing, and stop conditions | Source, consent, legal, release, or operational authority |
| Source/admission reviewer | Identifies descriptor, authority, rights, terms, and activation questions | That a source is admitted or denied without the owning decision |
| Privacy/consent reviewer | Identifies living-person, consent, revocation, third-party, and minimization obligations | That consent is valid, broad enough, revoked, or legally sufficient |
| Data custodian | Maps hypothetical storage and retention dependencies | Authority to preserve, transfer, delete, or erase real data |
| Derivative/catalog reviewer | Maps affected evidence, graph, index, tile, cache, answer, and export surfaces | That cleanup or withdrawal has executed |
| Release/correction reviewer | Identifies correction, withdrawal, release, and rollback evidence needed | Approval to change public state |
| Independent observer | Records ambiguity, unsafe shortcuts, missing evidence, and separation-of-duty gaps | Independent approval when the same person is simulating another role |

For a small tabletop, one person may simulate multiple roles, but the result record must disclose the combined roles. Simulated role coverage is not independent review.

[Back to top](#top)

## 7. Preconditions

Do not start until all of the following are true:

- [ ] The repository revision and target document version are recorded.
- [ ] The drill is explicitly labeled `TABLETOP_SYNTHETIC_ONLY`.
- [ ] The fictional source ID and synthetic dependency IDs are fixed.
- [ ] No real account, export, payload, credential, consent record, or private communication will be used.
- [ ] Network access and external writes are out of scope.
- [ ] Participants understand that [`VENDOR_WATCH_SOP.md`](./VENDOR_WATCH_SOP.md) is a manual repository-visible review procedure, not a monitor, external acquisition path, vendor-state authority, or response executor.
- [ ] Participants understand that no vendor-loss fixture, validator, cleanup executor, or operational source-state transition is proved at the pinned revision.
- [ ] A safe place for the minimized result record is selected.
- [ ] Stop conditions and the escalation contact route are named or recorded as `NEEDS VERIFICATION`.

A missing prerequisite produces `NOT_RUN` and `HOLD`; do not improvise around it.

[Back to top](#top)

## 8. Tabletop procedure

### 8.1 Freeze the evidence boundary

Record:

- exact repository revision;
- runbook version;
- fictional source and dependency IDs;
- scenario injects;
- participants and simulated roles;
- files consulted;
- known implementation gaps.

Do not use memory, prior summaries, or vendor rumors as current evidence.

### 8.2 Build the synthetic dependency map

For each fictional dependency, record only its class and relationship:

| Class | Question |
|---|---|
| Source descriptor / activation | What current, accountable record would establish source role, rights, terms, sensitivity, and activation? |
| RAW / WORK / QUARANTINE | What hypothetical captures or candidates could depend on the source? |
| PROCESSED / evidence | What derived assertion or EvidenceRef could depend on it? |
| CATALOG / TRIPLET | What catalog or graph projection could carry the dependency? |
| PUBLISHED / release | What released carrier or claim could require review? |
| Runtime derivative | Could an answer, export, tile, graph, index, or cache expose a dependent result? |
| Correction / rollback | What correction, withdrawal, invalidation, or rollback evidence would be required? |

Do not enumerate real records or search sensitive stores during the drill.

### 8.3 Classify the trigger on separate axes

Do not collapse the scenario into a single word such as “bankrupt” or “offline.”

| Axis | Tabletop values | Fail-closed question |
|---|---|---|
| Availability | available / degraded / unavailable / unknown | Can the source or revocation service be reached reliably? |
| Ownership or control | unchanged / changed / disputed / unknown | Who controls the source and applicable obligations? |
| Rights and terms | verified / changed / unresolved / unknown | Is continued possession, use, transfer, or derivation allowed? |
| Consent and revocation | satisfied / revoked / expired / unreachable / unknown | Does the exact purpose and audience remain permitted? |
| Integrity and custody | verified / suspect / unknown | Are bytes, provenance, and custody still trustworthy? |
| Source role | observed / modeled / candidate / context / unknown | What can the source legitimately support? |
| Sensitivity | resolved / requires transform / restricted / denied / unknown | What exposure is permitted, if any? |
| Lifecycle and release | internal / candidate / released / corrected / withdrawn / unknown | Which governed state is actually established? |

Any `unknown`, `unresolved`, `unreachable`, `suspect`, `restricted`, or `denied` value blocks automatic continuation.

### 8.4 Choose the simulated fail-closed posture

The tabletop may recommend a **planned** posture, never claim an executed action:

- `HOLD` new source admission, refresh, transformation, promotion, and release work that depends on the fictional source;
- `ABSTAIN` from evidence-dependent answers whose support cannot be resolved;
- `DENY` a proposed exposure when consent, rights, sensitivity, or release state is known not to permit it;
- `ESCALATE` retention, erasure, custody, legal, sovereignty, security, and notification questions;
- `ERROR` when a required contract, registry, resolver, validator, or procedure is absent or inconsistent.

Do not convert the plan into a connector change, data move, quarantine action, cache purge, or public withdrawal.

### 8.5 Assess downstream propagation

Review the closed surface set used by the current consent-revocation assessment as a **human checklist only**:

| Surface | Question | Tabletop output |
|---|---|---|
| `READ` | Could an internal or public read resolve the affected dependency? | proposed hold/deny plus evidence needed |
| `ANSWER` | Could governed or generated language rely on it? | proposed abstention/correction review |
| `EXPORT` | Could a downloadable derivative include it? | proposed hold/withdrawal review |
| `TILE` | Could a released tile or map carrier expose it? | proposed release/correction review |
| `GRAPH` | Could a graph projection retain it? | proposed rebuild/invalidation review |
| `INDEX` | Could search or vector indexes retain it? | proposed rebuild/invalidation review |
| `CACHE` | Could stale cached output remain accessible? | proposed invalidation review |

This runbook does not prove that all seven surfaces exist, are discoverable, or can be cleaned operationally. Record every unresolved surface as a gap.

### 8.6 Review preservation, tombstone, and erasure boundaries

Ask separately:

1. Must source-faithful bytes be preserved for evidence or audit?
2. Is continued possession permitted by consent, rights, terms, jurisdiction, and controlling authority?
3. Is a tombstone sufficient for explainability?
4. Is physical erasure required?
5. What must remain in an erasure receipt without restating removed content?
6. Which derivatives, manifests, indexes, graphs, caches, or exports require correction or invalidation?
7. Who is authorized to decide each action?

The repository documentation does not currently close these questions for a real DTC vendor-loss event. The tabletop outcome is therefore normally `HOLD` or `ESCALATE`, not “delete everything” or “keep everything.”

### 8.7 Prepare the minimized handoff

The handoff must contain:

- exact revision and runbook version;
- fictional scenario and opaque dependency IDs;
- classified trigger axes;
- proposed work states;
- unresolved owners and evidence;
- downstream surface gaps;
- retention/erasure questions;
- validation performed;
- explicit non-effects and stop conditions;
- next accountable review.

It must not contain real vendor or subject details.

### 8.8 Close the drill

Close only after participants agree on:

- execution result;
- whether stop conditions were honored;
- gaps found;
- unsafe shortcuts rejected;
- accountable follow-up owner or `NEEDS VERIFICATION`;
- confirmation that no external or sensitive action occurred.

[Back to top](#top)

## 9. Result interpretation

These are human drill labels, not machine policy or release outcomes.

| Axis | Values | Meaning |
|---|---|---|
| Execution | `PASS`, `FAIL`, `NOT_RUN` | Whether the tabletop followed this runbook |
| Work state | `HOLD`, `ESCALATE`, `READY_FOR_ACCOUNTABLE_REVIEW` | What may happen next in coordination |
| Policy/runtime observation | `ABSTAIN`, `DENY`, `ERROR`, `UNKNOWN` | A bounded observation about the simulated decision path; never an activated policy result |
| Operational effect | `NONE` | Required for this tabletop |

`PASS` means the exercise was safely and truthfully completed. It does **not** mean KFM can detect, contain, preserve, erase, correct, withdraw, or recover from a real vendor-loss event.

[Back to top](#top)

## 10. Minimum result record

The following is an illustrative, non-sensitive human record. It is not a schema or machine contract.

```yaml
drill_id: "dtc-vendor-loss-20260828-001"
mode: "TABLETOP_SYNTHETIC_ONLY"
repository_revision: "8f74d6d7d10d576062dda51684ef4eb6e97f4831"
runbook_version: "v1.0.0"

scenario:
  source_id: "kfm:source:synthetic-dtc-vendor"
  trigger: "SIMULATED_DTC_VENDOR_LOSS"
  injects:
    - "service_unavailable"
    - "rights_and_control_posture_unresolved"

safety:
  real_sensitive_payloads_used: false
  vendor_or_account_accessed: false
  network_used: false
  external_writes_or_notifications: false
  lifecycle_or_release_state_changed: false
  deletion_or_erasure_executed: false

result:
  execution: "PASS"
  work_state: "HOLD"
  operational_effect: "NONE"

classified_axes:
  availability: "unavailable"
  ownership_or_control: "unknown"
  rights_and_terms: "unresolved"
  consent_and_revocation: "unknown"
  integrity_and_custody: "unknown"
  sensitivity: "restricted"
  lifecycle_and_release: "unknown"

surface_gaps:
  - "READ"
  - "ANSWER"
  - "EXPORT"
  - "TILE"
  - "GRAPH"
  - "INDEX"
  - "CACHE"

open_actions:
  - owner: "NEEDS VERIFICATION"
    action: "identify accountable source, consent, custody, legal, and release reviewers"
  - owner: "NEEDS VERIFICATION"
    action: "define machine-readable vendor-state and dependency inventory contracts"

notes:
  - "No real vendor condition was asserted."
  - "No containment, preservation, erasure, correction, withdrawal, release, or publication action was executed."
```

[Back to top](#top)

## 11. Acceptance criteria

The tabletop passes only when all are true:

- [ ] The scenario used fictional identifiers and synthetic metadata only.
- [ ] No account, API, export, credential, network call, external message, or sensitive payload was used.
- [ ] Availability, control, rights, consent, integrity, source role, sensitivity, lifecycle, and release were assessed separately.
- [ ] Unknowns failed closed.
- [ ] No participant treated vendor loss as permission to download, preserve, transfer, delete, or publish.
- [ ] The seven downstream surfaces were reviewed or explicitly recorded as unresolved.
- [ ] Tombstone, erasure, retention, correction, withdrawal, and cache invalidation were kept as separate questions.
- [ ] The handoff names exact revision, limitations, non-effects, gaps, and accountable next review.
- [ ] Operational effect is `NONE`.

The drill fails when it hides uncertainty, uses real data, bypasses a stop condition, claims an unverified capability, or implies that a real response action occurred.

[Back to top](#top)

## 12. Operational graduation gaps

Before this document could support a real operational drill, KFM would need current evidence for at least:

1. accountable source, privacy, consent, legal, Indigenous/Tribal, security, custody, operations, release, and independent-review assignments;
2. a canonical vendor capability, terms, control, and health register;
3. a machine contract and schema for vendor state, source dependencies, and material change;
4. accepted source descriptors and activation decisions for each admitted DTC product;
5. consent, revocation, rights, sensitivity, retention, and erasure bindings;
6. a deterministic inventory from source capture through EvidenceRef, catalog, release, answer, export, tile, graph, index, and cache;
7. no-network synthetic vendor-loss fixtures, validators, negative cases, and hosted workflow evidence;
8. operational containment, correction, withdrawal, rebuild, invalidation, and receipt mechanisms;
9. approved incident, notification, legal, and subject/vendor communication procedures;
10. tested recovery and rollback targets that preserve correction and audit lineage.

Until those gaps close, use this document only for the bounded tabletop defined here.

[Back to top](#top)

## 13. Maintenance, correction, and rollback

Re-review this runbook when vendor monitoring, source descriptors, consent policy, retention/erasure rules, connector maturity, dependency inventory, cleanup capabilities, release controls, or accountable ownership changes.

Correct factual drift by pinning the new repository evidence, narrowing unsupported claims, and preserving the prior version in Git history. Do not silently convert proposed controls into implemented behavior.

Before merge, rollback is closing the draft pull request and deleting its task-owned branch. After an authorized merge, revert the focused documentation commit or submit a reviewed forward correction. Either path changes documentation only. It does not restore vendor access, recover data, reverse erasure, reactivate a source, repopulate a cache, withdraw a release, or alter public state.

[Back to top](#top)
