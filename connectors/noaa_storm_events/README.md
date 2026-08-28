<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-storm-events-underscore-readme
title: connectors/noaa_storm_events/ — NOAA Storm Events Underscore Compatibility Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Rights reviewer · Sensitivity reviewer · Security steward · Validation steward · Migration steward · CI steward · Docs steward
created: 2026-06-19
updated: 2026-07-15
policy_label: "public-doctrine; connector-boundary; compatibility-lane; noaa; storm-events; historical-event; narrative-sensitive; placement-conflicted; source-inactive; no-network-by-default; raw-quarantine-only; descriptor-gated; rights-aware; sensitivity-aware; provenance-preserving; correction-aware; fixture-first; not-life-safety; no-publication; rollback-aware; no-secrets"
current_path: connectors/noaa_storm_events/README.md
truth_posture: CONFIRMED repository path and prior v0.1 README, merged NOAA family/source/package/test boundaries, hyphenated Storm Events v0.2 sibling, two conflicting registry placeholders, proposed empty source-authority register, proposed pipeline-spec and watcher boundaries, TODO-only connector workflow, and bounded absence of underscore implementation files, central Storm Events adapter/test, and NOAA-nested README / PROPOSED compatibility contract, freeze-by-default topology posture, identity-preserving admission contract, finite outcomes, fixtures, tests, migration, correction, and rollback / CONFLICTED underscore versus hyphen versus nested placement, dotted versus underscored source identity, duplicate registry homes, source-role vocabulary, and documentation-rich boundaries versus absent implementation / UNKNOWN canonical path, active source, approved endpoints, current formats, executable parser, fixtures, tests, CI enforcement, schedules, receipts, deployment, and runtime health / NEEDS VERIFICATION owners, ADR or migration note, source-id decision, source activation, rights, product profile, transport policy, parser contracts, validators, fixtures, CI, correction, deprecation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 8af224617684d8e708c7550510a1f27d314e585a
  prior_blob: 7f1c595ac4110b9d270311f3bdb70e6df96d0ecc
  hyphen_sibling_blob: a47e3eaf0e67c67b2126fd0c6a35249c11b4f1e9
  noaa_family_blob: d57782414d5a7a3116f1a080b8048ae0c22f69bf
  noaa_tests_blob: a156c9149d69884a9327fa1257e55e22347ee2ec
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  dotted_registry_placeholder_blob: db7d6c2c1e261e9687d74497498761f228bedd4b
  underscored_registry_placeholder_blob: 902da1bd0e7164d26f70bf4f2835fb1b48b8d69a
  pipeline_spec_placeholder_blob: 74aad5c7ebbbc7e8c6dc0c848e3449c9dde0fcab
  watcher_readme_blob: e36c8e8213a51fc00290623dff5ca518881910af
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  bounded_path_checks:
    - connectors/noaa_storm_events/README.md exists at v0.1 before this revision
    - connectors/noaa_storm_events/__init__.py was not found
    - connectors/noaa_storm_events/client.py was not found
    - connectors/noaa_storm_events/parser.py was not found
    - connectors/noaa/src/noaa/products/storm_events.py was not found
    - connectors/noaa/tests/test_storm_events.py was not found
    - connectors/noaa/storm-events/README.md was not found
    - connectors/noaa-storm-events/README.md exists at v0.2 and is README-only
    - control_plane/source_authority_register.yaml is PROPOSED and entries is empty
    - data/registry/sources/hazards/noaa.storm_events.yaml is a minimal PROPOSED placeholder
    - data/registry/hazards/sources/noaa_storm_events.yaml retains TBD authority, rights, cadence, and access
    - pipeline_specs/hazards/noaa_storm_events.yaml is a PROPOSED inventory placeholder
    - tools/ingest/storm_events_watch/README.md is a proposed watcher boundary
    - .github/workflows/connector-gate.yml contains TODO echo steps
related:
  - ../README.md
  - ../noaa/README.md
  - ../noaa/src/README.md
  - ../noaa/src/noaa/README.md
  - ../noaa/tests/README.md
  - ../noaa-storm-events/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/catalog/noaa/storm-events.md
  - ../../docs/domains/hazards/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/hazards/noaa.storm_events.yaml
  - ../../data/registry/hazards/sources/noaa_storm_events.yaml
  - ../../pipeline_specs/hazards/noaa_storm_events.yaml
  - ../../tools/ingest/storm_events_watch/README.md
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, connectors, noaa, ncei, storm-events, underscore-lane, compatibility, historical-event, event-identity, episode-identity, correction-aware, narrative-sensitive, hazards, raw, quarantine, no-network, anti-collapse, migration, rollback]
notes:
  - "This revision changes only connectors/noaa_storm_events/README.md."
  - "The underscore and hyphenated lanes are README-only; no nested or central Storm Events implementation was found at tested paths."
  - "The dotted and underscored registry records conflict; the empty source-authority register activates neither."
  - "This README does not ratify, migrate, deprecate, delete, supersede, or redirect any Storm Events path."
  - "Historical event records are not current alerts, direct measurements, inundation extents, damage footprints, declarations, legal findings, or all-clear claims."
  - "Connector activity stops at RAW or QUARANTINE admission."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Storm Events Underscore Compatibility Boundary

`connectors/noaa_storm_events/`

> Repository-present but placement-conflicted compatibility boundary for NOAA/NCEI Storm Events source admission. Current evidence establishes a README-only lane—not a runnable connector, active source, canonical product path, or release-ready Hazards workflow.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![placement](https://img.shields.io/badge/placement-CONFLICTED-orange)
![source](https://img.shields.io/badge/source-NOAA__NCEI__Storm__Events-0a7ea4)
![network](https://img.shields.io/badge/network-off__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE-blue)
![alert authority](https://img.shields.io/badge/alert__authority-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Authority](#authority-boundary) · [Directory basis](#directory-rules-basis) · [Topology](#topology-and-compatibility) · [Invariants](#keystone-invariants) · [Inputs](#explicit-input-contract) · [Transport](#transport-and-security) · [Identity](#identity-time-and-correction) · [Records](#historical-record-boundary) · [Admission](#admission-and-finite-outcomes) · [Testing](#testing-and-fixtures) · [Watcher](#watcher-and-pipeline-separation) · [Migration](#migration-and-compatibility) · [Done](#definition-of-done) · [Open](#verification-register) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **This README is not an activation or placement decision.** Path presence does not establish a canonical implementation, active SourceDescriptor, approved endpoint, parser, fixtures, tests, receipts, schedules, CI enforcement, deployment, or publication readiness.

> [!CAUTION]
> **Storm Events is a historical record surface, not an emergency alert service.** This connector must never turn historical source records into current warnings, emergency instructions, direct measurements, inundation polygons, damage footprints, declarations, legal or insurance findings, or all-clear claims.

---

<a id="purpose"></a>

## Purpose

This lane documents the allowed boundary for an underscore-named compatibility candidate while Storm Events topology remains unresolved.

A future implementation here may exist only after governance chooses this path or explicitly authorizes a compatibility adapter. It must remain:

- subordinate to `connectors/noaa/`;
- descriptor-gated and source-activation-aware;
- no-network by default;
- fixture-first and deterministic;
- bounded in timeouts, retries, redirects, payload size, archive members, and decompression;
- lossless about source object, table, row, event, episode, time, geography, narrative, magnitude, casualty, damage, quality, vintage, and correction context;
- limited to RAW or QUARANTINE admission candidates;
- separate from normalization, evidence closure, release, public API, UI, map, notification, and AI behavior.

It must not become source doctrine, registry authority, a second independent implementation, a watcher, a pipeline, a policy engine, a proof system, a release service, or a public surface.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| `connectors/noaa_storm_events/README.md` | **CONFIRMED v0.1 before this revision** | The underscore README exists. |
| Underscore `__init__.py`, `client.py`, `parser.py` | **NOT FOUND in bounded checks** | No local implementation was established. |
| `connectors/noaa-storm-events/README.md` | **CONFIRMED v0.2** | A separate hyphenated README-only candidate exists. |
| `connectors/noaa/storm-events/README.md` | **NOT FOUND in bounded check** | No nested product README was established. |
| `connectors/noaa/README.md` | **CONFIRMED v0.2** | The merged family boundary records unresolved product topology. |
| Central NOAA package | **CONFIRMED `0.0.0` placeholder** | Package presence does not prove product support. |
| Central `products/storm_events.py` | **NOT FOUND** | No central Storm Events adapter was established. |
| Product test `test_storm_events.py` | **NOT FOUND** | No product-specific NOAA test was established. |
| Dotted registry record | **PROPOSED placeholder** | Minimal inventory only. |
| Underscored registry record | **PROPOSED/TBD template** | Source ID exists, but authority, rights, cadence, and access remain unresolved. |
| Source-authority register | **PROPOSED and empty** | Storm Events is not activated. |
| Pipeline spec | **PROPOSED placeholder** | Not executable evidence. |
| Watcher README | **PROPOSED boundary** | Watcher output is a review signal, not event truth or admission. |
| Connector workflow | **TODO-only** | A green run cannot prove connector behavior. |

### Evidence boundary

This README does not claim canonical placement, active source authority, current source formats, accepted source role, parser correctness, tests, CI enforcement, schedules, receipts, deployment, release closure, or public safety.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority boundary

### Allowed only after placement approval

- bounded retrieval or caller-supplied source-object adapters;
- byte-preserving payload and archive handling;
- source table and row parsing;
- event/episode identity preservation;
- source-vintage and correction metadata;
- deterministic RAW/QUARANTINE admission candidates;
- connector-local failures and quarantine reasons;
- approved fixtures and tests;
- explicitly authorized compatibility shims.

### Never owned here

| Concern | Owning boundary |
|---|---|
| NOAA and Storm Events doctrine | `docs/sources/catalog/noaa/` |
| Canonical path and source ID | Accepted ADR or migration decision |
| Source activation | Source registry and authority decision |
| Rights and sensitivity | `policy/rights/`, `policy/sensitivity/` |
| Meaning and shape | `contracts/`, `schemas/` |
| Normalization and derivation | Hazards pipelines |
| Watcher materiality | `tools/ingest/storm_events_watch/` |
| Lifecycle storage | `data/...` |
| Receipts and proof closure | `data/receipts/`, `data/proofs/` |
| Release and rollback | `release/` |
| Public API, UI, maps, alerts, search, AI | Governed application surfaces |

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

`connectors/` is the owning root because this document concerns source-specific fetch, parse, integrity, provenance, and admission.

```text
external source
  -> connector
  -> RAW or QUARANTINE
  -> downstream governed lifecycle
```

A connector must not write directly to WORK, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof closure, release authority, or public application surfaces.

The NOAA family spine is `connectors/noaa/`. This underscore lane may be retained only as decided compatibility or canonical structure; its existence does not override the family boundary.

[Back to top](#top)

---

<a id="topology-and-compatibility"></a>

## Topology and compatibility

| Surface | Current posture |
|---|---|
| `connectors/noaa/` | Documented family spine |
| `connectors/noaa-storm-events/` | Hyphenated README-only candidate |
| `connectors/noaa_storm_events/` | This underscore README-only candidate |
| `connectors/noaa/storm-events/` | Not found in bounded check |
| `noaa.storm_events` registry filename | Dotted placeholder |
| `noaa_storm_events` descriptor ID | Underscored template with TBD fields |

> [!WARNING]
> Until an accepted ADR or migration note resolves path and source identity, do not create parallel clients, parsers, endpoint configuration, descriptors, fixtures, tests, imports, schedules, or watchers.

### Freeze-by-default

Permitted work before resolution:

- evidence collection;
- topology ADR or migration planning;
- source-ID and registry reconciliation;
- source-profile, rights, and sensitivity review;
- path-neutral synthetic contract fixtures;
- shared contract tests that do not establish implementation authority.

README prose alone cannot classify a lane as canonical, mirror, transitional, legacy, or deprecated.

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

| Invariant | Requirement |
|---|---|
| Compatibility does not imply authority | The underscore path cannot ratify itself. |
| No parallel implementation | One accepted implementation path only. |
| Descriptor before live access | Missing or inactive source authority blocks retrieval. |
| Historical is not current | No current warning or guidance semantics. |
| Layered identity | Source object, table, row, event, episode, and vintage remain distinct. |
| Distinct time kinds | Event, file/vintage, retrieval, processing, and correction times do not collapse. |
| Reported fields remain reported | Ratings, estimates, narratives, damages, and casualties retain source meaning. |
| Geometry is not footprint truth | Points, paths, and locations are not automatic inundation or damage extents. |
| Absence is not no hazard | Missing records cannot prove safety or non-occurrence. |
| Corrections preserve lineage | Changed bytes require correction/supersession evidence. |
| RAW/QUARANTINE only | Connector output stops at admission. |
| No hidden fetches | Network access is explicit and configured. |
| No secrets | Credentials never enter code, fixtures, logs, errors, or receipts. |
| Finite outcomes | Every operation returns a bounded result and reason codes. |
| Public clients remain downstream | No public surface reads this lane directly. |

[Back to top](#top)

---

<a id="explicit-input-contract"></a>

## Explicit input contract

A future connector invocation requires:

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Resolve accepted identity, product scope, source role, rights, sensitivity, and activation. |
| Topology decision reference | Required before executable code is admitted to this path. |
| Product profile | Explicit object, table, period, format/profile, and correction model. |
| Approved source locator | Configuration only; not an unverified README constant. |
| Retrieval policy | Scheme/host allowlist, redirects, timeouts, retries, limits, listing, and resume behavior. |
| Expected integrity | Object name, size, archive expectations, checksum, and source metadata when known. |
| Identity policy | Deterministic object, table, row, event, episode, and vintage handling. |
| Time policy | Separate event, file, retrieval, processing, and correction roles. |
| Rights and sensitivity references | Carry governing IDs and unresolved state. |
| Routing context | Hazards-owned RAW or QUARANTINE target only. |
| Run identity | Deterministic or caller-supplied ID for replay and receipts. |

Importing modules or parsing fixtures must not call the network, read secrets, write files, create caches, start threads, register schedules, or emit receipts.

[Back to top](#top)

---

<a id="transport-and-security"></a>

## Transport and security

| Concern | Required control |
|---|---|
| Schemes and hosts | Explicit allowlists; reject arbitrary targets and unsafe redirects. |
| Timeouts and retries | Finite, observable, and bounded. |
| Rate limits | Respect configured limits; no uncontrolled polling. |
| Object/archive size | Bound compressed and expanded sizes, member count, nesting, and ratio. |
| Archive paths | Reject absolute paths, traversal, and symlink escape. |
| Content type and encoding | Validate profile evidence; preserve original bytes. |
| Partial transfer | Detect and quarantine truncated objects. |
| Integrity | Compare configured and observed size/digest where available. |
| SSRF | Block private/local targets, unsafe DNS behavior, and user-controlled hosts. |
| Secrets | Redact credentials, cookies, tokens, and signed material. |
| Unsafe deserialization | Do not instantiate executable objects from source payloads. |
| Logs | Sanitize control characters and avoid full narratives/casualty details. |
| Resource exhaustion | Bound memory, CPU, rows, fields, concurrency, and temporary files. |

Current endpoints, file inventories, formats, cadence, access, and rights are version-sensitive and must be verified before implementation or activation.

[Back to top](#top)

---

<a id="identity-time-and-correction"></a>

## Identity, time, and correction

Preserve, where exposed:

```text
source family
  -> product
    -> source object/package
      -> archive member
        -> source-declared table
          -> source row
            -> event ID
            -> episode ID
```

An event ID is not an episode ID. A supporting-table row is not automatically the event record. Cross-table joins must follow an accepted product profile and be deterministic, fixture-tested, and quarantine-safe.

Keep these times distinct:

- event begin and end;
- source issue/update;
- source-file creation or vintage;
- retrieval;
- processing;
- correction;
- supersession;
- review.

Changed bytes at the same locator require new lineage. Never silently overwrite a prior digest or substitute retrieval time for event time.

[Back to top](#top)

---

<a id="historical-record-boundary"></a>

## Historical record boundary

| Unsafe conversion | Required result |
|---|---|
| historical record → current alert | Refuse or quarantine |
| event record → direct scalar measurement | Preserve source field and caveat |
| flash-flood record → inundation polygon | Require separate evidence |
| tornado path/location → complete damage footprint | Preserve source geometry only |
| rating → measured wind/force | Refuse unsupported promotion |
| damage estimate → legal/insurance finding | Refuse |
| casualty/narrative → unrestricted public payload | Policy and release review |
| record absence → no hazard/all-clear | Refuse |
| corrected file → silent overwrite | Require correction lineage |
| supporting row → event truth | Preserve table role and linkage |

### Source-role conflict

Repository materials do not establish one accepted Storm Events source role. Product documentation, Hazards materials, and the template registry use differing or unresolved language. This connector must preserve the eventual accepted descriptor role and must not settle the conflict itself.

[Back to top](#top)

---

<a id="admission-and-finite-outcomes"></a>

## Admission and finite outcomes

A future connector may return only an admission candidate for:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

The candidate should carry source/profile references, object/table/row/event/episode/vintage identity, source fields and caveats, time roles, digests, rights/sensitivity state, outcome, reason codes, routing, and replay inputs.

It must not directly create WORK, PROCESSED, catalog, triplet, proof, release, published, map, alert, API, UI, search, embedding, or AI artifacts.

### Proposed connector-local outcomes

| Outcome | Meaning |
|---|---|
| `ADMIT_RAW` | Admission checks passed for a specific object and profile. |
| `QUARANTINE` | Review is required. |
| `NO_CHANGE` | Explicit comparison found no material object change; not proof of no event. |
| `NOT_FOUND` | Configured object unavailable; not proof of no hazard. |
| `SKIPPED` | Explicitly not run. |
| `RETRY_LATER` | Finite transient condition. |
| `DENIED` | Activation, rights, sensitivity, security, or configuration forbids the operation. |
| `ERROR` | Bounded unexpected failure. |

These are not canonical `PolicyDecision` outcomes.

Representative reason codes:

- `STORM_EVENTS_PLACEMENT_UNRESOLVED`
- `STORM_EVENTS_SOURCE_ID_UNRESOLVED`
- `STORM_EVENTS_SOURCE_NOT_ACTIVE`
- `STORM_EVENTS_RIGHTS_UNRESOLVED`
- `STORM_EVENTS_ENDPOINT_NOT_APPROVED`
- `STORM_EVENTS_CHECKSUM_MISMATCH`
- `STORM_EVENTS_FORMAT_DRIFT`
- `STORM_EVENTS_TABLE_ROLE_UNKNOWN`
- `STORM_EVENTS_EVENT_ID_MISSING`
- `STORM_EVENTS_EPISODE_LINKAGE_INVALID`
- `STORM_EVENTS_TIME_AMBIGUOUS`
- `STORM_EVENTS_CORRECTION_LINEAGE_MISSING`
- `STORM_EVENTS_NARRATIVE_REVIEW_REQUIRED`
- `STORM_EVENTS_PUBLIC_SAFETY_MISUSE`
- `STORM_EVENTS_OUTPUT_TARGET_FORBIDDEN`

[Back to top](#top)

---

<a id="testing-and-fixtures"></a>

## Testing and fixtures

Required test classes include:

- topology and canonical-path enforcement;
- import safety and no-network interception;
- missing descriptor/activation/rights/sensitivity;
- timeout, redirect, retry, rate-limit, payload, archive, and partial-transfer failures;
- object/table/row/event/episode/vintage identity;
- valid and invalid cross-table linkage;
- event/file/retrieval/correction time separation;
- valid, empty, malformed, truncated, unexpected-header, encoding, and format-drift parsing;
- geometry, narrative, magnitude, damage, casualty, quality, and status preservation;
- correction, changed-byte, duplicate-identity, and replay behavior;
- alert, measurement, inundation, damage-footprint, legal, insurance, and all-clear anti-collapse;
- RAW/QUARANTINE-only output enforcement;
- secret and sensitive-content redaction;
- watcher/connector separation.

Fixture classes should include synthetic minimal, synthetic negative, approved redacted source-shaped, golden parse, correction pairs, archive-safety, and topology-conflict fixtures.

No product-specific test or fixture coverage is claimed. The current test lane is README-only and connector-gate remains TODO-only.

[Back to top](#top)

---

<a id="watcher-and-pipeline-separation"></a>

## Watcher and pipeline separation

| Connector | Watcher | Pipeline |
|---|---|---|
| Retrieves or accepts source objects. | Compares metadata and emits review signals. | Normalizes or derives downstream objects. |
| Produces RAW/QUARANTINE candidates. | Does not create source records. | Operates under separate lifecycle contracts. |
| Preserves source bytes and identity. | Never activates or publishes. | Still cannot bypass evidence, policy, or release. |

The inspected watcher README and pipeline specification are proposed boundaries/placeholders, not executable proof.

[Back to top](#top)

---

<a id="migration-and-compatibility"></a>

## Migration and compatibility

A valid consolidation must decide:

1. canonical connector path;
2. canonical source ID and registry home;
3. compatibility class for losing paths;
4. code/import/config migration;
5. fixture/test migration;
6. schedule and watcher migration;
7. lifecycle and receipt continuity;
8. documentation and link updates;
9. rollback target;
10. completion evidence.

Any approved compatibility adapter must be one-way toward the canonical implementation, contain no parser fork or independent source configuration, create no separate source identity, emit a migration diagnostic, and have a removal condition.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Owners and required reviewers are accepted.
- [ ] Canonical path, source ID, and registry home are decided.
- [ ] Underscore and hyphenated compatibility classes are documented.
- [ ] Duplicate registry placeholders are reconciled.
- [ ] SourceDescriptor is complete and activation is recorded.
- [ ] Rights, attribution, sensitivity, and current source profile are reviewed.
- [ ] Package metadata/import path are real and tested.
- [ ] Importing code has no network, secret, cache, thread, schedule, or write side effects.
- [ ] Transport is allowlisted and resource-bounded.
- [ ] Parser preserves object/table/row/event/episode/vintage identity.
- [ ] Time kinds and correction lineage remain distinct.
- [ ] Historical-record anti-collapse checks fail closed.
- [ ] Outputs are limited to RAW/QUARANTINE candidates.
- [ ] Fixtures are approved, minimal, and non-sensitive.
- [ ] Tests cover no-network, negative, correction, and security paths.
- [ ] CI runs real tests and retains evidence.
- [ ] Watcher and pipeline boundaries are enforced.
- [ ] Receipts validate and rollback is exercised.
- [ ] Related documentation reflects actual implementation.

[Back to top](#top)

---

<a id="verification-register"></a>

## Verification register

| ID | Open item | Required evidence |
|---|---|---|
| `V-01` | Owners | CODEOWNERS/steward approval |
| `V-02` | Canonical path | Accepted ADR/migration note |
| `V-03` | Compatibility classes | Migration decision |
| `V-04` | Canonical source ID | Registry decision |
| `V-05` | Registry-home reconciliation | Migration receipt |
| `V-06` | Source activation | Authority entry |
| `V-07` | Source role | Accepted descriptor |
| `V-08` | Rights and sensitivity | Reviewed assessments |
| `V-09` | Approved endpoints/access | Versioned source profile |
| `V-10` | Current object/table formats | Source evidence and fixtures |
| `V-11` | Event/episode linkage | Profile and tests |
| `V-12` | Time/correction behavior | Source evidence and replay |
| `V-13` | Geometry/magnitude/damage semantics | Contracts and tests |
| `V-14` | Package build/import | Build and import tests |
| `V-15` | Transport limits | Config contract and tests |
| `V-16` | Parser implementation | Code and fixture tests |
| `V-17` | Admission-candidate contract | Accepted contract/schema |
| `V-18` | Outcome/reason vocabulary | Accepted connector contract |
| `V-19` | Fixture authority | Fixture manifest |
| `V-20` | No-network enforcement | Test logs |
| `V-21` | Product test collection | CI artifacts |
| `V-22` | Real connector CI | Workflow and logs |
| `V-23` | Pipeline implementation | Executable spec |
| `V-24` | Watcher implementation | Code and tests, if approved |
| `V-25` | Receipt emission | Validated receipts |
| `V-26` | Correction invalidation | Replay evidence |
| `V-27` | Schedule ownership | Runbook/config |
| `V-28` | Operational health | Logs/dashboard |
| `V-29` | Release integration | Governed release evidence |
| `V-30` | Rollback automation | Rollback drill |

[Back to top](#top)

---

<a id="rollback-and-correction"></a>

## Rollback and correction

### Documentation rollback

Restore prior blob:

```text
7f1c595ac4110b9d270311f3bdb70e6df96d0ecc
```

or revert the commit introducing v0.2.

### Correction

If this README overstates maturity:

1. identify the statement;
2. cite contradicting repository evidence;
3. apply a narrow correction;
4. retain the prior version in Git history;
5. update affected links and verification items.

### Deprecation

This underscore lane may be deprecated only by an accepted topology decision naming the replacement, compatibility period, migration steps, removal conditions, and rollback.

---

## Status summary

`connectors/noaa_storm_events/` is a README-only, placement-conflicted compatibility candidate for historical NOAA/NCEI Storm Events source admission. It is not a canonical path, active source, runnable connector, current-warning authority, measurement authority, inundation/damage-footprint authority, legal authority, evidence closure, release authority, public map/API/UI surface, or publication path.

<p align="right"><a href="#top">Back to top</a></p>
