<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-rollback-fauna-readme
title: Fauna Rollback-Readiness Adapter README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <fauna-domain-steward>
  - <sensitivity-reviewer>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-22
policy_label: public
path: pipelines/rollback/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - docs/standards/RELEASE_MANIFEST.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipelines/README.md
  - pipelines/rollback/README.md
  - pipelines/domains/fauna/README.md
  - pipelines/publish/fauna/README.md
  - pipeline_specs/README.md
  - pipeline_specs/fauna/README.md
  - contracts/domains/fauna/README.md
  - schemas/contracts/v1/domains/fauna/README.md
  - policy/domains/fauna/README.md
  - policy/sensitivity/fauna/README.md
  - fixtures/domains/fauna/README.md
  - tests/domains/fauna/README.md
  - data/catalog/domain/fauna/README.md
  - data/published/layers/fauna/README.md
  - data/receipts/pipeline/README.md
  - data/proofs/evidence_bundle/README.md
  - data/rollback/README.md
  - release/README.md
  - release/candidates/fauna/README.md
  - release/manifests/README.md
  - release/rollback_cards/README.md
  - release/correction_notices/README.md
tags: [kfm, pipelines, rollback, fauna, readiness, evidence, sensitivity, geoprivacy, release, correction]
notes:
  - "This document describes a Fauna adapter/profile inside the shared rollback-readiness lane; it does not establish rollback or release authority."
  - "Executable depth is UNKNOWN. The previously referenced pipeline_specs/rollback/fauna.yaml and target-specific rollback test and fixture leaves were not present at the pinned evidence snapshot."
  - "A prior release must be revalidated against current rights, sensitivity, policy, evidence, and dependency state before it may be proposed as a rollback target."
  - "If this lane grows into a full Fauna rollback workflow, placement must be reconciled with pipelines/domains/fauna/ through an accepted ADR or migration decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna rollback-readiness adapter

> Fauna-specific guidance for checking whether an authorized rollback proposal is complete, policy-safe, evidence-supported, reversible, and ready for release-authority review. `READY` means ready for that handoff; it never means that rollback is approved, executed, or verified.

![status](https://img.shields.io/badge/status-draft-blue)
![maturity](https://img.shields.io/badge/implementation-UNKNOWN-orange)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![authority](https://img.shields.io/badge/rollback%20authority-separate-d62728)
![sensitivity](https://img.shields.io/badge/fauna-fail%20closed-d62728)

**Path:** `pipelines/rollback/fauna/README.md`  
**Responsibility root:** `pipelines/` - executable pipeline logic  
**Lane role:** thin Fauna adapter/profile under shared rollback-readiness support  
**Document lifecycle:** DRAFT  
**Component maturity:** UNKNOWN  
**Public posture:** no direct release, rollback, correction, serving, alias, cache, or artifact mutation

> [!IMPORTANT]
> This lane may inspect and report rollback readiness. It must not approve a rollback, author a final `RollbackCard` or `ReleaseManifest`, create evidence, decide policy, restore artifacts, rewrite lineage, invalidate public surfaces, or expose restricted Fauna locations.

## Quick navigation

- [Scope and evidence status](#scope-and-evidence-status)
- [Purpose](#purpose)
- [Placement and authority](#placement-and-authority)
- [Rollback model](#rollback-model)
- [Finite outcomes](#finite-outcomes)
- [Inputs and preconditions](#inputs-and-preconditions)
- [Required gates](#required-gates)
- [Fauna-specific hazards](#fauna-specific-hazards)
- [Execution and handoff](#execution-and-handoff)
- [Outputs and receipt posture](#outputs-and-receipt-posture)
- [Prohibited behavior](#prohibited-behavior)
- [Validation](#validation)
- [Operational and security properties](#operational-and-security-properties)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs and open decisions](#adrs-and-open-decisions)
- [Correction and rollback](#correction-and-rollback)
- [Definition of done](#definition-of-done)
- [Last reviewed](#last-reviewed)

---

<a id="scope-and-evidence-status"></a>

## Scope and evidence status

This README is a documentation contract for a narrow adapter boundary. It does not prove that an executable adapter, accepted machine contract, schema, declarative profile, test suite, fixture suite, CI owner, or receipt emitter exists.

| Claim | Status | Evidence boundary |
|---|---|---|
| `pipelines/` owns executable pipeline logic; `pipeline_specs/` owns declarative configuration. | CONFIRMED | Directory Rules and both repository roots at the reviewed snapshot |
| `pipelines/rollback/` and this Fauna child directory exist. | CONFIRMED | Repository paths at the reviewed snapshot |
| Fauna is sensitivity-bearing and requires fail-closed public representation. | CONFIRMED doctrine/documentation | Fauna architecture, policy, domain-pipeline, fixture, and test documentation |
| Release decisions, rollback cards, correction notices, and manifests belong under `release/`; published artifacts remain under `data/published/`. | CONFIRMED | Directory Rules and release/data READMEs |
| `data/rollback/` is distinct from release-decision authority. | CONFIRMED path; exact artifact contract NEEDS VERIFICATION | Directory Rules and current data-lane README |
| `pipeline_specs/rollback/fauna.yaml` exists or is accepted. | CONFIRMED ABSENT | Individually checked at `main@640fc2f` |
| A rollback-specific Fauna fixture or test leaf exists. | CONFIRMED ABSENT for the checked README paths | `fixtures/rollback/fauna/README.md`, `tests/pipelines/rollback/fauna/README.md`, and `tests/domains/fauna/rollback/README.md` were absent |
| Executable rollback behavior is implemented and enforced in CI. | UNKNOWN | No target-specific executable or command-bearing proof established in this review |
| `READY`, `HELD`, `DENIED`, and `ERROR` are canonical machine values. | PROPOSED | Useful finite vocabulary; requires accepted contract, schema, policy, and tests |
| This child lane is the permanent home for full Fauna rollback behavior. | NEEDS VERIFICATION / ADR review | Domain Placement Law favors primary domain behavior under `pipelines/domains/fauna/` |

### Change scope

This revision changes documentation only. It creates no executable, specification, schema, contract, policy, fixture, test, receipt, release record, rollback artifact, correction notice, EvidenceBundle, public artifact, API route, map layer, cache entry, or lifecycle state.

[Back to top](#top)

---

<a id="purpose"></a>

## Purpose

This directory is reserved for Fauna-specific adaptation of shared rollback-readiness checks. Its job is to help an authorized caller determine whether a proposed recovery path:

- names the exact current release and exact proposed target by immutable identity and digest;
- has an admissible reason supported by resolvable evidence and review records;
- preserves source roles, taxonomic identity, temporal meaning, rights, sensitivity, and restricted/public separation;
- identifies every affected public-safe derivative and downstream consumer;
- proves that the proposed target is safe under current policy, not merely historically published;
- carries correction, withdrawal, invalidation, and rollback-control references where applicable;
- can be rehearsed deterministically without network access or public side effects;
- returns one finite outcome, structured blockers, and auditable non-secret metadata;
- returns control to the Fauna domain lane and release authority.

This lane does not decide whether rollback is preferable to forward correction, withdrawal, or denial. It may report that a prior release is unsafe or unavailable and that a forward fix is required.

[Back to top](#top)

---

<a id="placement-and-authority"></a>

## Placement and authority

Directory Rules assign executable pipeline logic to `pipelines/` and release decisions to `release/`. The Fauna segment is acceptable here only as thin adapter/profile glue around shared rollback-readiness behavior. Primary Fauna workflow meaning remains with the Fauna domain lane.

| Responsibility | Owning boundary | Adapter posture |
|---|---|---|
| Shared executable readiness checks | `pipelines/rollback/` | May call or adapt; must not silently redefine |
| Fauna pipeline behavior | `pipelines/domains/fauna/` | Primary executable domain lane |
| Declarative run scope | `pipeline_specs/` and accepted Fauna spec lane | Read-only input; exact rollback profile is unconfirmed |
| Fauna object meaning | `contracts/domains/fauna/` | Reference only |
| Fauna machine shape | `schemas/contracts/v1/domains/fauna/` | Reference only; no local schema invention |
| Rights, admissibility, sensitivity, geoprivacy | `policy/` responsibility lanes | Policy decisions are inputs, not adapter authority |
| Evidence and proof | `data/proofs/` and evidence contracts | Resolve; do not manufacture |
| Pipeline audit memory | `data/receipts/pipeline/` | Emit only through an accepted receipt contract |
| Rollback data-plane artifacts or alias-revert receipts | `data/rollback/` | Exact contract NEEDS VERIFICATION |
| Release decision, final manifest, rollback card, correction notice | `release/` | Release authority owns |
| Public-safe released artifacts | `data/published/` | Read/compare only in readiness mode |
| Public API, map, search, cache, and UI state | governed runtime/application owners | Inventory only; never mutate here |

### Authority boundary

This adapter may:

- validate caller scope and immutable references;
- compare current and target release metadata;
- resolve required evidence, policy, review, receipt, and representation references;
- build a complete affected-surface inventory;
- verify a dry-run plan;
- return blockers and a proposed readiness result.

This adapter may not:

- choose the authoritative rollback reason;
- waive missing evidence, rights, sensitivity, review, or integrity support;
- sign or approve a `RollbackCard`, `CorrectionNotice`, or `ReleaseManifest`;
- change release state, aliases, routes, public artifacts, caches, indexes, tiles, graphs, or API payloads;
- treat its own output as release authorization.

### Admission rule for future code

Do not add executable files here until all of the following are accepted:

1. placement and owner;
2. input, output, outcome, blocker, and receipt contracts;
3. schema and compatibility/versioning policy;
4. declarative profile location;
5. public-safe fixtures and deterministic negative tests;
6. CI ownership and required-check posture;
7. release-steward handoff and separation of duties;
8. correction, stale-result invalidation, and rollback-rehearsal behavior.

[Back to top](#top)

---

<a id="rollback-model"></a>

## Rollback model

KFM lifecycle history remains append-only and inspectable:

`RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`

A rollback is a governed release transition with correction and audit lineage. It is not a reverse file copy and it does not erase the release being superseded.

### Required distinctions

- **Current release:** the release presently bound to a governed public surface.
- **Proposed target:** an immutable prior or replacement state offered for review.
- **Last known good:** a claim that must be re-proven; it is not inferred from age or prior publication.
- **RollbackCard:** release-authority decision artifact, not an adapter receipt.
- **CorrectionNotice or withdrawal record:** public/audit explanation where required.
- **Readiness receipt:** process memory about checks; not proof of approval or successful execution.
- **Post-rollback verification:** independent proof that the approved transition and every required invalidation completed.

### Current-policy rule

A proposed target must pass current applicable evidence, rights, sensitivity, integrity, identity, temporal, and public-representation rules. If a previously published Fauna artifact would now expose restricted precision, rely on revoked rights, use withdrawn evidence, carry a superseded taxonomic identity, or violate current policy, the adapter must not label it `READY`.

The safe response may be `HELD`, `DENIED`, or a recommendation that release authority pursue forward correction rather than restoration.

[Back to top](#top)

---

<a id="finite-outcomes"></a>

## Finite outcomes

The following vocabulary is **PROPOSED** until accepted by contracts, schemas, policies, validators, and tests.

| Outcome | Meaning | Required behavior |
|---|---|---|
| `READY` | The bounded proposal has complete, current, internally consistent support for release-authority review. | Emit a handoff package and receipt; perform no rollback or public mutation. |
| `HELD` | One or more required dependencies, reviews, inventories, rehearsals, or references are missing, stale, contradictory, or incomplete. | Emit explicit blockers and required next evidence; preserve state. |
| `DENIED` | Caller scope, rights, policy, sensitivity, sovereignty, consent, or another governing rule prohibits the requested proposal or target. | Emit a safe reason code and policy reference; do not disclose restricted details. |
| `ERROR` | Integrity, parsing, contract, canonicalization, dependency, or execution failure prevents a trustworthy readiness decision. | Fail closed, preserve diagnostics appropriate to the audience, and make no state change. |

Rules:

- exactly one terminal outcome per invocation;
- `READY` is never rollback approval or proof of successful restoration;
- absence of blockers is not enough for `READY`; every required positive gate must pass;
- `HELD` is not a weaker form of `READY`;
- `DENIED` must not leak the sensitive fact, geometry, identity, or policy detail being protected;
- `ERROR` must never be coerced to `HELD` or `READY` merely to keep an automation moving;
- retryability, materiality, audience, and reason codes require accepted machine definitions before implementation.

[Back to top](#top)

---

<a id="inputs-and-preconditions"></a>

## Inputs and preconditions

All operational object and field names below are conceptual until their canonical contracts and schemas are verified.

### Required caller context

- authenticated caller identity and role;
- authorized Fauna rollback scope;
- invocation mode: dry run, drill, or release-authority review preparation;
- reason category and originating incident/correction/evidence reference;
- request time and expected evidence snapshot;
- explicit prohibition on public side effects.

### Required pinned references

- current `ReleaseManifest` identity and digest;
- proposed target manifest or replacement-candidate identity and digest;
- current and target artifact inventories;
- `RollbackCard` draft/input reference if the governing workflow requires one;
- `CorrectionNotice`, withdrawal, incident, or supersession reference where applicable;
- applicable `EvidenceRef` / `EvidenceBundle`, validation, policy, rights, sensitivity, and `ReviewRecord` references;
- Fauna restricted/public representation mapping and geoprivacy/redaction receipt references;
- catalog, triplet/graph, tiles, indexes, API payloads, exports, aliases, routes, and cache dependency inventory;
- current contract, schema, policy, canonicalization, adapter, and dependency versions;
- intended post-transition validation and rollback-of-rollback/forward-fix plan.

### Input rules

- mutable branch names, floating aliases, "latest," timestamps alone, or filenames alone are insufficient identity;
- each trust-bearing input must be immutable or content-addressed where the owning contract permits;
- raw restricted payloads and exact sensitive coordinates must not be copied into ordinary adapter inputs, logs, fixtures, or receipts;
- the adapter must distinguish missing, inaccessible, intentionally withheld, invalid, stale, and contradictory inputs;
- evidence summaries, generated text, map presentation, and prior green CI are not substitutes for resolvable primary support.

[Back to top](#top)

---

<a id="required-gates"></a>

## Required gates

Each gate must produce structured evidence of pass, hold, denial, or error. Gate order may be optimized only if fail-closed behavior and deterministic results are preserved.

### 1. Caller and scope

- verify caller identity, role, and bounded authority;
- verify the request names the Fauna release family and intended surfaces;
- reject ownerless, wildcard, mixed-domain, or unbounded requests unless an accepted orchestration contract governs them;
- prevent a drill from being mistaken for an operational rollback.

### 2. Current release and target identity

- resolve the exact current manifest, target manifest/candidate, release IDs, digests, signatures, and supersession chain;
- prove that the target belongs to the same governed release family or has an accepted migration/crosswalk;
- reject ambiguous, mutable, partially resolved, or digest-mismatched targets;
- preserve both current and proposed histories for audit.

### 3. Reason and evidence

- resolve each material rollback claim through `EvidenceRef` to the applicable `EvidenceBundle`;
- preserve source authority and source-role distinctions;
- detect stale, withdrawn, contradicted, wrong-scope, or inaccessible support;
- require cite-or-abstain semantics for human-facing explanations;
- treat generated summaries as presentation only.

### 4. Rights and source status

- re-evaluate licenses, permissions, redistribution terms, source withdrawal, embargo, consent, and use constraints;
- deny or hold public restoration when rights are unknown, revoked, expired, or narrower than the proposed public representation;
- preserve source identifiers, versions, retrieval context, and role;
- do not upcast contextual or corroborating material into primary authority.

### 5. Fauna sensitivity and geoprivacy

- preserve `OccurrenceRestricted` and `OccurrencePublic` separation;
- verify current sensitivity class, precision policy, seasonality, stewardship constraints, and public-safe representation;
- verify required geoprivacy, redaction, generalization, aggregation, delay, or withholding receipts;
- ensure exact sensitive sites, nests, dens, roosts, hibernacula, spawning sites, telemetry, mortality, disease, or rare-species locations cannot reappear through the target or derivative surfaces;
- fail closed if the policy engine, sensitivity decision, or representation receipt is unavailable.

### 6. Identity and time

- verify taxon identifiers, crosswalks, aliases, conservation/legal status, dataset versions, and release identities;
- preserve valid time, observation time, source publication/retrieval time, release time, correction time, and stale time where applicable;
- detect a target that restores superseded taxonomy, status, geometry, temporal scope, or provenance;
- preserve deterministic identity and do not silently recycle old identifiers for changed meanings.

### 7. Validation and integrity

- verify applicable contract, schema, policy, geometry, temporal, evidence, citation, catalog, triplet/graph, release, and artifact checks;
- verify hashes, signatures, content addressing, manifests, sidecars, media types, and dependency pins where applicable;
- require deterministic no-network replay against public-safe fixtures before operational use;
- treat an unavailable validator or unverifiable result as `HELD` or `ERROR`, never as implicit pass.

### 8. Dependency and invalidation inventory

Inventory every affected representation and consumer, including as applicable:

- published layers, PMTiles/tiles, GeoParquet, reports, stories, exports, and downloadable bundles;
- governed API payloads, feature routes, release routes, aliases, and discovery metadata;
- catalog records, registries, triplets, graph projections, vector/search indexes, caches, and CDN objects;
- map style/source references, thumbnails, screenshots, derived indicators, and downstream release candidates;
- receipts, proofs, manifests, citations, correction state, and monitoring/alert references.

The inventory must distinguish restore, supersede, rebind, invalidate, retain-for-audit, recompute, and deny-public-access actions.

### 9. Correction and rollback controls

- resolve the required `RollbackCard`, correction, withdrawal, supersession, and public-notice inputs;
- prove a complete target and an ordered, rehearsable action plan;
- identify compensating action or forward-fix behavior if reversal is unsafe or incomplete;
- preserve correction lineage and the reason the current release ceased to be authoritative;
- define post-transition validation and recovery if the approved rollback itself fails.

### 10. Review and separation of duties

- resolve applicable pipeline, Fauna, evidence, rights, sensitivity, security, correction, and release reviews;
- ensure the readiness author cannot self-approve a material rollback when separation is required;
- require explicit human review for material public, sensitive, legal, or trust-impacting transitions;
- do not substitute CI, generated prose, or an adapter `READY` result for an authorized release decision.

### 11. Atomicity and race protection

- pin all checked dependencies to the same coherent snapshot;
- detect changes between evaluation and handoff;
- make readiness results single-use or invalidatable by dependency digest;
- require release authority to re-check preconditions immediately before any mutation;
- define safe interruption boundaries so partial action cannot masquerade as success.

### 12. Receipt and no-side-effect proof

- produce deterministic, non-secret audit metadata using an accepted receipt contract;
- record input digests, gate results, outcome, blockers, tool/profile versions, and output refs;
- prove that readiness mode changed no release record, public artifact, alias, route, index, cache, or serving state;
- keep restricted details out of public or ordinary operational receipts.

[Back to top](#top)

---

<a id="fauna-specific-hazards"></a>

## Fauna-specific hazards

Rollback can increase risk when an older release is less protected than the current one. The adapter must explicitly evaluate:

| Hazard | Required posture |
|---|---|
| Older target contains exact or finer sensitive geometry | `DENIED` or `HELD` until a current public-safe derivative is built and reviewed |
| Generalization/redaction receipt missing or does not match target digest | Fail closed; do not infer that visible geometry is safe |
| Sensitivity class increased after the target was published | Apply current policy; historical publication does not grandfather exposure |
| Rights or source permission was revoked | Do not restore public distribution; require release/legal/rights handling |
| Taxon crosswalk or identity was corrected | Prevent resurrection of superseded identity without an accepted compatibility mapping |
| Disease, mortality, invasive-species, or monitoring data now has tighter controls | Re-evaluate scope, delay, aggregation, access, and public representation |
| Public and restricted occurrence records were collapsed | `ERROR` or `DENIED`; never reconstruct sensitive boundaries by guesswork |
| Tiles changed but graph, search, API, export, or cache derivatives remain stale | `HELD` until the invalidation inventory and verification plan are complete |
| Prior evidence was withdrawn or contradicted | Do not describe the target as last known good; require current evidence review |
| Rollback would erase correction or supersession history | Reject the plan; history must remain inspectable |

### Withheld accounting

Public verification may record that features were withheld, generalized, aggregated, delayed, or denied, but must not reveal their exact locations or enable differencing attacks. Counts, bounds, and metadata must follow the applicable policy and audience rules.

[Back to top](#top)

---

<a id="execution-and-handoff"></a>

## Execution and handoff

This lane's bounded process is:

1. **Bind** the authorized request and immutable evidence snapshot.
2. **Resolve** current release, proposed target, reason, evidence, policy, review, and dependency references.
3. **Revalidate** the proposed target under current rights, sensitivity, identity, temporal, and public-representation rules.
4. **Inventory** every affected derivative and consumer.
5. **Rehearse** the proposed action plan against deterministic public-safe fixtures or an accepted isolated environment.
6. **Classify** one proposed finite outcome.
7. **Emit** blockers and a non-authoritative readiness receipt/handoff.
8. **Return** control to release authority.

Release authority, outside this adapter, must independently:

- confirm that every dependency still matches the evaluated snapshot;
- decide rollback versus correction, withdrawal, forward fix, or denial;
- create or approve the required release-control artifacts;
- execute through the accepted release mechanism;
- verify all public and internal derivatives;
- publish required correction or withdrawal state;
- preserve the prior and resulting audit lineage.

### Stale readiness

Any material change to a pinned manifest, artifact, evidence bundle, source role, rights decision, sensitivity decision, representation receipt, validation report, review record, policy bundle, contract/schema version, dependency inventory, target, or correction state invalidates the readiness result.

A stale `READY` receipt may remain for audit but must not be reused as current authorization.

[Back to top](#top)

---

<a id="outputs-and-receipt-posture"></a>

## Outputs and receipt posture

### Allowed bounded outputs

- one proposed finite outcome;
- structured, audience-safe blocker or denial codes;
- immutable input and dependency digests;
- target-safety and validation summary;
- complete affected-surface inventory;
- rehearsal and post-transition verification references;
- release-steward handoff reference;
- receipt metadata produced through an accepted contract.

### Illustrative receipt

The following is documentation-only and **not an accepted schema**:

```yaml
schema_version: PROPOSED
adapter_run_id: fauna_rollback_readiness_<stable-id>
pipeline_id: rollback.fauna
mode: dry_run
outcome: HELD
scope:
  current_release_ref: <immutable-ref>
  proposed_target_ref: <immutable-ref>
  reason_ref: <immutable-ref>
snapshot:
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  representation_receipt_refs: []
  dependency_digest: <digest>
checks:
  caller_authorized: false
  current_release_resolved: false
  target_integrity_valid: false
  target_safe_under_current_policy: false
  evidence_current_and_resolved: false
  rights_resolved: false
  restricted_public_split_preserved: false
  geoprivacy_receipts_valid: false
  identity_and_time_valid: false
  invalidation_inventory_complete: false
  rehearsal_passed: false
  separation_of_duties_ready: false
  no_side_effects_observed: true
blockers: []
handoff_ref: null
receipt_ref: null
```

Do not copy this shape into production until the owning contract, schema, reason vocabulary, canonicalization profile, sensitivity rules, receipt home, validator, and compatibility policy are accepted.

[Back to top](#top)

---

<a id="prohibited-behavior"></a>

## Prohibited behavior

Disallowed collapses:

```text
adapter READY -> rollback approval
prior publication -> currently safe target
artifact restore -> rollback complete
tile swap -> all derivatives invalidated
cache purge -> correction complete
RollbackCard input -> approved RollbackCard
readiness receipt -> ReleaseManifest
generated explanation -> evidence
digest match -> policy approval
OccurrencePublic restore -> restricted/public boundary proven
historical geoprivacy transform -> current sensitivity clearance
green CI -> human release authority
```

This directory must not contain:

- release decisions, final manifests, approved rollback cards, or correction notices;
- canonical Fauna truth, source descriptors, policies, contracts, or schemas;
- reusable sensitive production fixtures or exact protected locations;
- credentials, signing keys, tokens, private endpoints, or secrets;
- public API/UI/map implementation or direct canonical-store access;
- emitted release artifacts, proofs, receipts, catalogs, or lifecycle data;
- ad hoc scripts that mutate public state outside accepted orchestration;
- code that treats missing policy, review, evidence, or dependency data as success.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

### Documentation validation

A change to this README should verify:

- one H1 and a coherent heading hierarchy;
- unique explicit anchors and valid navigation links;
- balanced code fences;
- repository-relative links against a pinned commit;
- truth labels on implementation and path claims;
- no credentials, secrets, private endpoints, or sensitive coordinates;
- no loss of lifecycle, evidence, sensitivity, correction, rollback, and authority boundaries;
- exact changed-path budget and remote read-back.

### Future executable test burden

No target-specific executable test leaf was confirmed. Before implementation claims are accepted, tests should cover at least:

- deterministic no-network dry run;
- all four proposed finite outcomes;
- unauthorized, ownerless, wildcard, and wrong-domain callers;
- ambiguous current release, target, identity, or mutable aliases;
- target digest/signature mismatch;
- target made unsafe by current policy, rights, sensitivity, or source withdrawal;
- missing, stale, contradicted, withdrawn, inaccessible, and wrong-scope evidence;
- source-role collapse and authority upcast attempts;
- sensitive precision re-exposure and invalid geoprivacy receipts;
- public/restricted occurrence collapse;
- taxonomic, conservation-status, temporal, and dataset-version drift;
- incomplete tiles, graph, triplet, search, API, export, alias, and cache invalidation;
- missing correction, withdrawal, rollback-card, review, or post-verification support;
- deterministic receipt canonicalization and replay;
- dependency change between readiness evaluation and handoff;
- proof of zero public/release side effects;
- interruption and partial-failure recovery;
- stale `READY` invalidation;
- rollback target that requires forward correction instead of restoration.

### Fixture burden

Future fixtures should be synthetic or demonstrably public-safe and include:

- one minimal valid current/target pair;
- one case for every `HELD` dependency family;
- one caller or policy `DENIED` case;
- one integrity or dependency `ERROR` case;
- one prior target with unsafe exact geometry;
- one revoked-rights or withdrawn-source target;
- one superseded-taxonomy target;
- one complete multi-surface invalidation inventory;
- one partial-execution recovery case;
- expected outcome, blocker codes, and deterministic receipt digest.

Fixtures must not contain unreleased coordinates, protected-site geometry, living-person details, credentials, signing material, raw restricted payloads, or data with unresolved reuse rights.

### CI ownership

Exact target-specific CI ownership is **UNKNOWN**. Documentation, workflow names, or green unrelated checks are not proof that this adapter contract is enforced.

[Back to top](#top)

---

<a id="operational-and-security-properties"></a>

## Operational and security properties

Future implementation must be:

- **deterministic:** same pinned inputs and versions produce the same outcome and canonical receipt;
- **idempotent:** repeated readiness checks do not mutate release or public state;
- **fail closed:** missing policy, rights, evidence, review, or integrity support cannot become `READY`;
- **bounded:** time, memory, artifact count, and dependency traversal limits are explicit;
- **race-aware:** evaluation detects drift before handoff and cannot authorize from stale inputs;
- **least privilege:** readiness mode needs read access only to the minimum governed surfaces;
- **auditable:** decisions, blockers, versions, and dependency digests are inspectable;
- **privacy preserving:** logs and receipts omit secrets and restricted location detail;
- **interruptible:** cancellation leaves no partial public change;
- **replayable:** accepted public-safe fixtures can reproduce outcomes offline;
- **observable:** metrics distinguish `READY`, `HELD`, `DENIED`, `ERROR`, retries, stale results, and dependency failures without leaking protected facts.

### Logging rules

Log stable references, digests, reason codes, counts allowed by policy, and tool/profile versions. Do not log:

- exact sensitive coordinates or site identifiers;
- raw restricted occurrence, telemetry, mortality, disease, or stewardship payloads;
- credentials, tokens, signing keys, or private headers;
- generated narrative presented as evidentiary fact;
- denial detail that enables inference of a protected location.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

### Documentation changes

At minimum:

- pipeline-owner review for executable-lane scope;
- Fauna-domain review for object, identity, time, and domain boundaries;
- sensitivity/policy review for geoprivacy and restricted/public handling;
- release-steward review for rollback, correction, handoff, and authority separation;
- docs-steward review for placement, truth labels, links, and lifecycle language.

### Future implementation changes

| Change class | Minimum review posture |
|---|---|
| Shared checker or receipt behavior | Pipeline owner plus contract/schema and test owners |
| Fauna object, identity, time, or dependency logic | Fauna domain steward plus affected domain owners |
| Evidence or source-role logic | Evidence steward plus source/domain steward |
| Rights, sensitivity, sovereignty, consent, precision, or public representation | Policy/rights/sensitivity reviewer plus Fauna steward |
| Integrity, signing, content addressing, or dependency pinning | Release steward plus security/supply-chain reviewer |
| Invalidation, correction, withdrawal, rollback, alias, route, cache, or public-surface behavior | Correction reviewer, release authority, and every affected surface owner |

### Separation of duties

- Adapter authors may prove deterministic behavior but cannot use that authorship to self-approve a material rollback.
- The actor who detected or authored a material correction should not be the sole release authority.
- Sensitive-lane rollback requires the role combination defined by current governing policy.
- Missing review cannot be replaced by generated prose, green CI, a digest match, or an adapter `READY` result.

[Back to top](#top)

---

<a id="related-folders"></a>

## Related folders

All links below were present at the reviewed snapshot.

### Doctrine and architecture

- [Directory Rules](../../../docs/doctrine/directory-rules.md) - responsibility-root placement and the `pipelines/` / `pipeline_specs/` split.
- [Lifecycle Law](../../../docs/doctrine/lifecycle-law.md) - governed lifecycle transitions.
- [Release discipline](../../../docs/architecture/release-discipline.md) - release, review, correction, and rollback posture.
- [ReleaseManifest standard](../../../docs/standards/RELEASE_MANIFEST.md) - release identity, integrity, correction, and rollback guidance.
- [Fauna architecture](../../../docs/domains/fauna/ARCHITECTURE.md) - object families, sensitivity, geoprivacy, evidence, and publication boundaries.
- [ADR index](../../../docs/adr/README.md) - accepted decision index.

### Executable and declarative lanes

- [Pipelines root](../../README.md) - executable pipeline authority.
- [Shared rollback lane](../README.md) - parent readiness boundary.
- [Fauna domain pipeline](../../domains/fauna/README.md) - primary Fauna executable domain lane.
- [Fauna publish-readiness adapter](../../publish/fauna/README.md) - adjacent pre-publication adapter boundary.
- [Pipeline specifications root](../../../pipeline_specs/README.md) - declarative configuration authority.
- [Fauna pipeline specifications](../../../pipeline_specs/fauna/README.md) - confirmed Fauna declarative lane; no rollback profile was confirmed.

### Contracts, policy, tests, and fixtures

- [Fauna contracts](../../../contracts/domains/fauna/README.md) - semantic meaning.
- [Fauna schemas](../../../schemas/contracts/v1/domains/fauna/README.md) - machine-shape lane.
- [Fauna domain policy](../../../policy/domains/fauna/README.md) - current domain policy home.
- [Fauna sensitivity policy](../../../policy/sensitivity/fauna/README.md) - sensitivity scaffold and default-deny boundary.
- [Pipeline tests](../../../tests/pipelines/README.md) - shared pipeline test root; no target rollback leaf was confirmed.
- [Fauna tests](../../../tests/domains/fauna/README.md) - domain proof boundary.
- [Fauna fixtures](../../../fixtures/domains/fauna/README.md) - public-safe domain fixture boundary.

### Data and release authority

- [Fauna catalog lane](../../../data/catalog/domain/fauna/README.md) - catalog records.
- [Published Fauna layers](../../../data/published/layers/fauna/README.md) - released public-safe layer artifacts.
- [Pipeline receipts](../../../data/receipts/pipeline/README.md) - pipeline process-memory lane.
- [EvidenceBundle proofs](../../../data/proofs/evidence_bundle/README.md) - evidence proof lane.
- [Rollback data lane](../../../data/rollback/README.md) - data-plane rollback artifacts/receipts; exact object contract remains to be verified.
- [Release root](../../../release/README.md) - release-decision authority.
- [Fauna release candidates](../../../release/candidates/fauna/README.md) - candidate review lane.
- [Release manifests](../../../release/manifests/README.md) - final manifest collection lane.
- [Rollback cards](../../../release/rollback_cards/README.md) - release-control rollback artifacts.
- [Correction notices](../../../release/correction_notices/README.md) - correction record lane.

### Confirmed and proposed shape

```text
pipelines/rollback/fauna/
└── README.md                     # CONFIRMED: this documentation contract

pipeline_specs/fauna/             # CONFIRMED declarative Fauna lane
└── <rollback profile>            # PROPOSED; exact path and schema not accepted here

fixtures/domains/fauna/           # CONFIRMED Fauna fixture lane
└── <rollback fixtures>           # PROPOSED

tests/domains/fauna/              # CONFIRMED Fauna test lane
└── <rollback tests>              # PROPOSED
```

The earlier README's named adapter executables and rollback-specific spec/test/fixture paths are not repository facts at the reviewed snapshot. Re-verify placement before creating them.

[Back to top](#top)

---

<a id="adrs-and-open-decisions"></a>

## ADRs and open decisions

The bounded inspection did not establish a target-specific accepted ADR that grants this directory rollback authority, creates a parallel receipt/contract/schema/policy home, or makes `pipelines/rollback/<domain>/` the default home for full domain workflows.

| ID | Question | Status | Resolution evidence needed |
|---|---|---|---|
| `PIPE-ROLLBACK-FAUNA-001` | Should executable Fauna rollback behavior remain here or live under `pipelines/domains/fauna/`? | NEEDS VERIFICATION / ADR review | Accepted owner, call graph, placement decision, and migration plan if moved |
| `PIPE-ROLLBACK-FAUNA-002` | Which accepted contract and schema own outcomes, blockers, handoffs, and receipts? | UNKNOWN | Contract, schema, validator, fixtures, compatibility policy, and owner |
| `PIPE-ROLLBACK-FAUNA-003` | What exact declarative profile path scopes the adapter? | NEEDS VERIFICATION | `pipeline_specs/` placement decision and profile schema |
| `PIPE-ROLLBACK-FAUNA-004` | Where should rollback-specific tests and fixtures live? | NEEDS VERIFICATION | Current tree review and owning README updates |
| `PIPE-ROLLBACK-FAUNA-005` | Which CI job proves these invariants? | UNKNOWN | Command-bearing workflow and required-check decision |
| `PIPE-ROLLBACK-FAUNA-006` | Which outcome, reason, retryability, and materiality vocabularies are canonical? | UNKNOWN | Accepted policy/contract/schema registry and negative tests |
| `PIPE-ROLLBACK-FAUNA-007` | What exact object families belong in `data/rollback/` versus `release/rollback_cards/` and `data/receipts/`? | NEEDS VERIFICATION / ADR | Data/release contract decision and migration compatibility |
| `PIPE-ROLLBACK-FAUNA-008` | How are readiness receipts canonicalized, content-addressed, superseded, and invalidated? | UNKNOWN | Hash profile, receipt contract, replay tests, and correction semantics |
| `PIPE-ROLLBACK-FAUNA-009` | Which Fauna geoprivacy/redaction receipt vocabulary is canonical? | NEEDS VERIFICATION | Policy, contract, schema, validator, and fixture closure |
| `PIPE-ROLLBACK-FAUNA-010` | When must an unsafe historical target force forward correction rather than restoration? | NEEDS VERIFICATION | Release policy, materiality rules, decision matrix, and drills |

[Back to top](#top)

---

<a id="correction-and-rollback"></a>

## Correction and rollback

### Correcting this documentation

If this README overstates implementation, links to a moved authority, or misstates a Fauna trust boundary:

1. open a focused correction change;
2. identify the unsupported claim and pinned correcting evidence;
3. update version, review date, truth labels, links, and open decisions;
4. preserve supersession or migration lineage;
5. re-run structure, link, sensitivity, no-loss, and remote-diff checks.

Before merge, close the unmerged PR or replace it transparently. After merge, use a revert commit or revert PR; do not rewrite shared history.

### Correcting readiness results

Future implementation must preserve every prior receipt for audit while marking stale or superseded results unusable. A correction must identify:

- affected readiness run;
- changed dependency and old/new digests;
- reason, detection time, reviewer, and materiality;
- replacement outcome or required re-evaluation;
- downstream handoffs that must be invalidated;
- any public correction or incident reference owned by release authority.

### Rollback of an approved rollback

The operational workflow must define recovery when an approved rollback partially fails or produces an unsafe state. That recovery may be a forward fix, withdrawal, another governed target, or denial of public access. This adapter may validate the plan but cannot choose or execute it.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This README revision is complete when it:

- states the confirmed `pipelines/` placement without granting rollback or release authority;
- distinguishes confirmed paths from proposed executables, profiles, tests, fixtures, contracts, schemas, and integrations;
- preserves lifecycle and the separation among current release, proposed target, evidence, policy, review, rollback card, correction notice, manifest, receipt, public artifact, and serving state;
- requires current-policy revalidation of every proposed Fauna target;
- defines bounded inputs, finite outcomes, gates, hazards, outputs, validation, review, correction, and stale-result invalidation;
- treats exact sensitive location exposure, unknown rights, missing geoprivacy receipts, incomplete invalidation, and unsafe historical targets as fail-closed conditions;
- links only to repository paths confirmed at the reviewed snapshot;
- introduces no sensitive payload, credential, signing key, release mutation, or public behavior change.

Future executable work is done only when accepted placement, ownership, contracts, schemas, declarative scope, public-safe fixtures, deterministic positive and negative tests, canonical receipts, CI ownership, role-separated review, race protection, correction invalidation, rollback rehearsal, partial-failure recovery, and post-transition verification all exist and pass.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-22 |
| Document version | v0.2 |
| Status | DRAFT |
| Repository evidence base | `main@640fc2f3c9720cf17d640f0267bf540328e973f0` |
| Placement basis | Directory Rules responsibility roots, `pipelines/` / `pipeline_specs/` split, release/data split, Domain Placement Law, and README contract |
| Implementation depth | UNKNOWN |
| Confirmed target-specific absences | `pipeline_specs/rollback/fauna.yaml` and the checked rollback-specific Fauna test/fixture README paths |
| Release/publication impact | None; documentation-only readiness contract |
| Next review trigger | First executable, accepted contract/schema, profile, test/fixture leaf, CI owner, data/release rollback decision, adapter placement decision, or material Fauna/release policy change |

### Maintenance checklist

- [ ] Replace owner placeholders with accepted maintainers.
- [ ] Re-check accepted ADRs and drift entries before adding or moving implementation.
- [ ] Confirm the canonical outcome, blocker, receipt, correction, and rollback vocabularies.
- [ ] Confirm declarative profile, test, fixture, data artifact, and CI ownership.
- [ ] Keep rights, sensitivity, and exact-location uncertainty fail closed.
- [ ] Revalidate proposed targets under current policy.
- [ ] Verify every related link and implementation claim at the next pinned commit.
- [ ] Invalidate stale readiness results after material dependency or policy change.
- [ ] Update this README when behavior, review, correction, rollback, or public-surface responsibilities change.

[Back to top](#top)
