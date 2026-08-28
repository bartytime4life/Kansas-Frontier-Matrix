<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-storm-events-readme
title: connectors/noaa-storm-events/ — NOAA Storm Events README-Only Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; connector-boundary; noaa; storm-events; historical-event; narrative-sensitive; placement-conflicted; not-life-safety; no-publication
truth_posture: CONFIRMED README-only hyphenated sibling / CONFLICTED placement and source identity / INACTIVE source authority / IMPLEMENTATION NEEDS VERIFICATION
evidence_snapshot: main@8fad3427a5f8ca6a8093217c1fa0a6fcc6a74401
related:
  - ../README.md
  - ../noaa/README.md
  - ../noaa/src/README.md
  - ../noaa/tests/README.md
  - ../noaa_storm_events/README.md
  - ../hazards/README.md
  - ../../docs/sources/catalog/noaa/storm-events.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/architecture/source-roles.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/directory-rules.md
  - ../../control_plane/source_authority_register.yaml
  - ../../data/registry/sources/hazards/noaa.storm_events.yaml
  - ../../data/registry/hazards/sources/noaa_storm_events.yaml
  - ../../pipeline_specs/hazards/noaa_storm_events.yaml
  - ../../tools/ingest/storm_events_watch/README.md
tags: [kfm, connectors, noaa, ncei, storm-events, hazards, historical-event, event-identity, correction-aware, narrative-sensitive, source-admission, raw, quarantine, governance]
notes:
  - "This file documents a proposed connector boundary; it does not prove executable NOAA Storm Events connector code."
  - "A second README-only boundary exists at connectors/noaa_storm_events/; this README does not settle hyphenated, underscored, or NOAA-nested placement."
  - "The two Storm Events registry YAMLs are PROPOSED placeholders with dotted-versus-underscored identity drift; neither establishes activation."
  - "Historical event records retain source file, table, row, event, episode, time, geography, narrative, magnitude, casualty, damage, quality, and correction context."
  - "A historical event record is not a current warning, direct scalar measurement, flood-inundation extent, tornado damage footprint, disaster declaration, insurance determination, or proof that an unrecorded hazard did not occur."
  - "Connector output is limited to RAW or QUARANTINE handoff and never grants downstream publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA Storm Events README-Only Connector Boundary

> Boundary for proposed NOAA National Centers for Environmental Information (NCEI) Storm Events source admission at `connectors/noaa-storm-events/`. Repository evidence at the pinned snapshot proves this README, not a runnable product connector or an active source.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: not proven" src="https://img.shields.io/badge/implementation-not__proven-lightgrey">
  <img alt="Placement: conflicted" src="https://img.shields.io/badge/placement-CONFLICTED-orange">
  <img alt="Scope: historical event records" src="https://img.shields.io/badge/scope-historical__event__records-blue">
  <img alt="Alert authority: denied" src="https://img.shields.io/badge/alert__authority-denied-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Truth posture:** `CONFIRMED` README-only hyphenated sibling · `CONFLICTED` hyphen/underscore/nested placement and dotted/underscored source identity · source authority `INACTIVE / NOT ESTABLISHED` · product runtime `NEEDS VERIFICATION`.

> [!CAUTION]
> Storm Events is a historical record surface. A record does not become a current warning, a direct scalar measurement, an inundation polygon, a tornado damage footprint, a disaster declaration, an insurance determination, or an all-clear merely because it was admitted.

**Quick jumps:** [Purpose](#1-purpose) · [Status](#3-status) · [Validation](#8-validation) · [Topology](#connector-topology-and-placement) · [Record boundary](#historical-event-record-boundary) · [Runtime contract](#proposed-runtime-contract) · [Evidence](#evidence-ledger) · [Backlog](#verification-backlog)

---

## 1. Purpose

`connectors/noaa-storm-events/` defines a conservative source-admission boundary for Storm Events source objects and their source-provided table, event, episode, temporal, geographic, narrative, magnitude, casualty, damage, quality, and correction context.

If executable code is later approved here, it may retrieve an explicitly configured source object, preserve native bytes and record identity, validate only admission preconditions, and hand the result to a Hazards-owned `RAW` or `QUARANTINE` lane. This README does not activate a source, choose a live endpoint, establish current file/table formats or cadence, define source role, or prove product-specific code exists.

The boundary is narrow:

```text
approved Storm Events source object
              |
              v
bounded retrieval and integrity checks
              |
              v
identity-preserving source admission
source + object + table + row + event + episode + time + vintage
              |
              +----> RAW         only when admission preconditions pass
              |
              `----> QUARANTINE  when identity, structure, linkage,
                                  integrity, rights, sensitivity,
                                  correction, quality, or routing is unresolved
```

[Back to top ↑](#top)

---

## 2. Authority level

**Authority: implementation-boundary documentation only; no source, event-interpretation, emergency, release, or publication authority.**

This README may describe what a future connector at this path is allowed to do. It may not:

- ratify the hyphenated lane as the canonical Storm Events implementation home;
- deprecate or supersede `connectors/noaa_storm_events/`;
- create a nested NOAA product lane by implication;
- promote the `connectors/noaa/` `0.0.0` scaffold into working Storm Events support;
- choose between dotted and underscored source identifiers or registry homes;
- activate either registry placeholder or populate the empty source-authority register;
- select a source role where draft catalog, Hazards doctrine, and descriptor state are not reconciled;
- define event, episode, table, row, time, geometry, magnitude, casualty, damage, quality, or correction semantics independently of accepted contracts and current source evidence;
- convert historical records into current warnings, measurements, inundation, damage footprints, declarations, legal findings, or all-clear claims;
- normalize, aggregate, interpolate, compare, catalog, publish, or release records;
- create public API, map, UI, notification, emergency-guidance, or generated-answer behavior.

The two Directory Rules copies agree on the connector lifecycle limit but differ in version and placement posture. This README relies only on their shared rule: connectors fetch and admit source material and may write to `RAW` or `QUARANTINE`, not later lifecycle stages. It does not decide which Directory Rules copy is authoritative.

---

## 3. Status

| Question | Evidence-backed status |
|---|---|
| Does `connectors/noaa-storm-events/README.md` exist? | **CONFIRMED.** The lane contains this README at the inspected snapshot. |
| Is executable code proven in this exact lane? | **No.** Bounded probes found no package file, source README, tests README, or initializer. |
| Does an underscore Storm Events lane exist? | **Yes.** `connectors/noaa_storm_events/README.md` is a separate README-only compatibility candidate. |
| Does an implemented NOAA-nested Storm Events lane exist? | **Not in bounded probes.** Neither `connectors/noaa/storm-events/README.md` nor `connectors/noaa/ncei-storm-events/README.md` was found. |
| Is the NOAA family package ready? | **No.** It is version `0.0.0`; its initializer is empty, fetch/admit modules are placeholder comments, its local descriptor retains `TBD` role and rights, and no product module was found at the probed path. |
| Are Storm Events registry records present? | **Two `PROPOSED` placeholders are present.** One uses a dotted filename under `data/registry/sources/hazards/`; the other declares underscored `id: noaa_storm_events` under `data/registry/hazards/sources/` and retains `TBD` authority, rights, cadence, and access fields. |
| Is Storm Events active in the source-authority register? | **No.** The register is `PROPOSED` and its `entries` list is empty. |
| Is a Storm Events pipeline implemented? | **Not proven.** The named pipeline spec is a `PROPOSED` placeholder, while the inspected Hazards ingest/normalize/validate modules are one-line greenfield comments. |
| Is a Storm Events watcher implemented? | **Not proven.** The watcher folder documents a proposed boundary; bounded probes found no initializer, `watch.py`, or `main.py`. |
| Is a released Storm Events slice proven? | **CONFLICTED.** The Hazards release index describes a released Storm Events thin slice, while the corresponding inspected manifest and promotion-decision YAMLs are only `PROPOSED` inventory placeholders. The placeholders do not prove release. |
| Are Hazards contracts and schemas present? | **Generic Hazards artifacts are present.** A draft domain-observation contract and a compact schema exist, but they do not prove Storm Events parsing, table linkage, source activation, fixtures, or release closure. |
| Is the topology conflict recorded in the drift register? | **No matching entry was found in the bounded Storm Events probe.** The conflict remains visible in connector READMEs and Hazards documentation. |

Absence statements above are limited to named repository paths inspected at `main@8fad3427a5f8ca6a8093217c1fa0a6fcc6a74401`; they are not claims of an exhaustive recursive inventory.

---

## 4. What belongs

If this path is ratified, it may contain product-specific connector artifacts such as:

- source-object discovery or manifest adapters that require an approved SourceDescriptor revision;
- bounded retrieval helpers with explicit schemes, hosts, redirects, timeouts, retries, and maximum sizes;
- checksum, content-length, archive-member, source-file, and source-fingerprint verification;
- byte-preserving capture of source files, headers, documentation references, and change metadata;
- table parsers that retain source-declared table roles and row linkage without joining them into a new truth surface;
- event/episode identity helpers that keep event ID, episode ID, table, row, source object, and source vintage distinct;
- time parsers that preserve source time fields, timezone context, file creation/vintage, retrieval, processing, and correction times without silent substitution;
- geometry helpers that retain source point, line, path, location, and coordinate fields as supplied;
- deterministic `RAW` or `QUARANTINE` handoff envelopes;
- sanitized process evidence that references, rather than redefines, governing records;
- no-network fixtures representing approved structural, linkage, correction, and failure cases;
- unit and contract tests for source admission, identity preservation, redaction, and anti-collapse behavior.

Every artifact must preserve source, object, table, row, event, episode, and vintage identity and fail closed when required evidence is missing or contradictory.

---

## 5. What does NOT belong

| Excluded responsibility | Governing surface or next decision |
|---|---|
| Canonical connector placement or path retirement | Accepted ADR or migration decision with compatibility, validation, and rollback. |
| NOAA family or Storm Events product doctrine | `docs/sources/catalog/noaa/` and the draft Storm Events product page. |
| Source ID and registry-home authority | Resolve dotted versus underscored identity and duplicate registry paths outside this connector. |
| Source activation | `control_plane/source_authority_register.yaml` plus approved descriptors and review. |
| Source role authority | Accepted source-role doctrine and an admitted descriptor; do not choose among `observation`, `observed`, `administrative`, or `TBD` here. |
| Current endpoint, access, format, cadence, terms, or attribution claims | Current authoritative source evidence captured in approved registry and rights records. |
| Event, observation, identity, correction, or release contracts/schemas | `contracts/` and `schemas/contracts/v1/` after authority review. |
| Watcher material-change decisions | `tools/ingest/storm_events_watch/` after implementation and review; watcher signals are not event truth. |
| Normalization, aggregation, comparison, or derived geometry | Hazards pipelines with explicit methods, source roles, and receipts. |
| Current warning, watch, advisory, forecast, or emergency instruction | Official operational authorities; never this historical connector. |
| Flood inundation, tornado damage extent, or measured-value derivation | Separate evidence and downstream governed transforms. |
| Disaster declaration, insurance, compensation, liability, or legal determination | Official administrative or legal authorities. |
| Catalog, triplet, tile, proof, published, or release artifacts | Governed lifecycle, evidence, and release surfaces. |
| Rights, sensitivity, casualty/narrative release, or public-safety decisions | `policy/` and release review. |
| EvidenceBundle closure | Downstream proof processes; connector process evidence is not claim closure. |
| Public API, UI, map, notification, or generated-answer behavior | Governed application surfaces after release. |

---

## 6. Inputs

A future connector invocation should accept only explicit, governed inputs. At minimum:

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Required before retrieval; must resolve to an approved Storm Events source identity and activation posture. |
| Product and object identity | Preserve source family, product, source object or package, source-declared table class, data period, file creation/vintage, and exposed format version. |
| Approved source locator | Treat as configuration, not a hard-coded claim in this README. Redact credentials, signed material, and sensitive query parameters. |
| Expected integrity | Preserve expected filename/object key, size, compression/archive expectations, checksum algorithm/digest, and source metadata when known. |
| Retrieval policy | Bound schemes, hosts, redirects, timeouts, retries, maximum object and archive-member sizes, listing/pagination, and resume behavior. |
| Identity policy | Require deterministic handling for source object, table, row, event ID, episode ID, source vintage, and correction lineage where exposed. |
| Time interpretation | Preserve event begin/end, source issue or file-creation, retrieval, processing, and correction/supersession times as distinct roles where exposed. |
| Routing context | Name the Hazards-owned proposed `RAW` or `QUARANTINE` destination without granting downstream promotion. |
| Rights and attribution reference | Carry governing record identifiers and unresolved review state; do not decide rights locally. |
| Sensitivity and public-safety posture | Carry narrative, casualty, location, and not-life-safety review requirements into the handoff. |

The draft product page describes candidate detail, fatality, and location table roles, but current endpoints, access or authentication method, environment-variable names, file/table formats, filename conventions, cadence, quotas, rights, field vocabulary, and correction behavior remain version-sensitive facts. They must be verified before implementation or activation; this README intentionally does not pin them.

---

## 7. Outputs

The connector may emit only an atomic source-admission handoff to one of:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

The exact layout remains subject to governing repository contracts. Conceptually, a handoff should include:

- byte-preserving source payload or an immutable reference permitted by policy;
- source sidecars, headers, documentation references, and original package members;
- a sanitized request/retrieval manifest;
- source, product, object/package, table, data-period, format, and source-vintage identity;
- row identity plus event ID and episode ID where the source supplies them;
- native event type, state/status, location/geography, narrative, magnitude/rating, casualty, damage, quality, and source-note fields without semantic promotion;
- native geometry and coordinate fields with source projection/CRS evidence where exposed;
- distinct event, source-issue/file-creation, retrieval, processing, and correction time roles;
- source and content fingerprints;
- observed size, archive-member, and checksum results;
- rights, attribution, sensitivity, and public-safety references or unresolved flags;
- validation results and deterministic quarantine reasons;
- owning-domain routing and run identity.

The connector must not emit directly to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLETS`, `PUBLISHED`, proof, release, API, UI, map, notification, emergency-guidance, or generated-answer surfaces.

---

## 8. Validation

Validation is source-admission validation, not confirmation that an event occurred exactly as narrated, scientific validation of every scalar field, operational warning validation, or publication approval.

### Required checks

- source identity, registry home, source ID, SourceDescriptor revision, and activation state resolve without dotted/underscored ambiguity;
- product, source object/package, table class, source vintage, and file identity are present where applicable;
- row identity, event ID, and episode ID remain distinct and link only under source-declared rules;
- retrieval follows configured scheme, host, redirect, timeout, retry, listing/pagination, and size constraints;
- payload and required package members are complete, bounded, archive-safe, and content-digested;
- current format/header expectations are versioned and checked without silently accepting source drift;
- source time fields, file creation/vintage, retrieval, processing, and correction times remain distinct;
- native geography and geometry fields are preserved without inventing inundation or damage extent;
- magnitude/rating, casualty, damage, narrative, quality, and status fields retain source labels and caveats;
- preliminary, finalized, corrected, replaced, or other source states are preserved only when current evidence defines them;
- a changed source object at the same locator becomes reviewable correction lineage rather than silent overwrite;
- rights, attribution, narrative/casualty sensitivity, location, public-safety, and routing references are present or the object is quarantined;
- output destination is limited to `RAW` or `QUARANTINE`;
- logs and process evidence contain no credentials, signed URLs, unsafe narrative excerpts, or unnecessary person-identifying details.

### Quarantine conditions

Quarantine on missing, ambiguous, or conflicting evidence, including:

- unresolved hyphenated/underscored/nested placement, source ID, registry home, or activation state;
- missing or conflicting source object, table, row, event, episode, format, or source-vintage identity;
- checksum, size, archive-member, package, or source-fingerprint mismatch;
- unreadable, truncated, structurally unsafe, partially retrieved, or unexpectedly encrypted content;
- unknown headers, tables, fields, event types, status codes, quality flags, timezones, geometry, units, or source-schema drift;
- broken cross-table linkage or event/episode conflation;
- stale, future-dated, timezone-ambiguous, contradictory, or unsupported time roles;
- duplicate identity with different bytes or changed bytes without correction lineage;
- attempt to treat a historical record as a current alert or official emergency instruction;
- attempt to treat a rating, estimate, or reported maximum as a direct measurement or legal finding;
- attempt to infer inundation, damage footprint, or no-hazard/all-clear state from record presence or absence;
- unresolved rights, attribution, narrative/casualty sensitivity, location, public-safety, or domain routing;
- any attempt to treat connector or watcher activity as promotion, release, or publication authority.

An empty, missing, delayed, incomplete, quality-rejected, or unavailable source slice is not proof that no hazard occurred or that conditions are safe.

### No-network test posture

Tests should be deterministic and no-network by default. Fixtures should cover, at minimum:

- valid source objects with table, row, event, episode, time, geography, and vintage identity preserved;
- event ID versus episode ID distinction and valid/invalid cross-table linkage;
- multiple source-declared table roles kept distinct;
- missing, duplicated, malformed, or conflicting identity fields;
- checksum, size, archive-member, compression, encoding, and archive-safety failures;
- unknown or changed headers, tables, fields, event types, quality flags, geometry, units, and format versions;
- preliminary, finalized, corrected, superseded, duplicate, and conflicting-byte cases where current source evidence supports those states;
- stale, future-dated, timezone-ambiguous, and contradictory time roles;
- historical-record-to-current-alert conversion attempts;
- rating/estimate/reported-maximum-to-measurement conversion attempts;
- flood-record-to-inundation and path-to-damage-footprint conversion attempts;
- damage-to-insurance/legal and absence-to-no-hazard/all-clear conversion attempts;
- narrative, casualty, person-identifying, and exact-location review triggers;
- rights, sensitivity, source-role, activation, or routing states that force quarantine;
- credential, signed-URL, and unsafe-payload redaction;
- rejection of every output destination beyond `RAW` or `QUARANTINE`.

No product-specific tests or fixtures were proven in the bounded inspected paths. This list is an activation requirement, not a claim of current coverage.

---

## 9. Review burden

`OWNER_TBD` remains unresolved. Until ownership is ratified, changes require review from the roles affected by the change:

- connector and source stewards for retrieval, identity, integrity, and lifecycle behavior;
- NOAA/product stewards for source-object, table, event, episode, field, status, and correction interpretation;
- Hazards stewards for historical-event role, domain routing, and downstream boundaries;
- rights and sensitivity reviewers for source terms, narratives, casualties, person-identifying details, exact locations, and redistribution;
- validation stewards for fixtures, quarantine outcomes, replay, correction, and no-network coverage;
- docs stewards for truth labels, links, metadata, evidence boundaries, and anti-collapse language;
- architecture/governance review for any path, source-ID, registry-home, schema-home, activation, or authority decision.

The inspected `CODEOWNERS` file provides only the global `@kfm/maintainers` fallback for this connector path; it does not identify Storm Events-specific owners. A README-only clarification must not be treated as owner approval, source activation, or placement ratification.

---

## 10. Related folders

| Surface | Relationship to this boundary |
|---|---|
| [`connectors/README.md`](../README.md) | Connector-root source-admission contract. |
| [`connectors/noaa/`](../noaa/README.md) | Declared NOAA family lane; its runtime remains a `0.0.0` greenfield scaffold. |
| [`connectors/noaa_storm_events/`](../noaa_storm_events/README.md) | Separate README-only underscore compatibility candidate. |
| [`connectors/hazards/`](../hazards/README.md) | Hazards connector-family map that explicitly records Storm Events topology conflict. |
| [`docs/sources/catalog/noaa/storm-events.md`](../../docs/sources/catalog/noaa/storm-events.md) | Draft product doctrine and anti-collapse guidance; not runtime or current external-source proof. |
| [`docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md) | Hazards source-role mapping; must be reconciled with descriptor and catalog vocabulary before activation. |
| [`control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | Source activation register; inspected entries are empty. |
| [`data/registry/sources/hazards/noaa.storm_events.yaml`](../../data/registry/sources/hazards/noaa.storm_events.yaml) | Minimal dotted-name `PROPOSED` inventory placeholder. |
| [`data/registry/hazards/sources/noaa_storm_events.yaml`](../../data/registry/hazards/sources/noaa_storm_events.yaml) | Underscored greenfield descriptor template with unresolved authority, rights, cadence, and access. |
| [`pipeline_specs/hazards/noaa_storm_events.yaml`](../../pipeline_specs/hazards/noaa_storm_events.yaml) | `PROPOSED` pipeline-spec inventory placeholder, not an executable spec. |
| [`pipelines/domains/hazards/`](../../pipelines/domains/hazards/README.md) | Generic Hazards pipeline boundary; inspected core modules are greenfield comments. |
| [`tools/ingest/storm_events_watch/`](../../tools/ingest/storm_events_watch/README.md) | Proposed watcher boundary; watcher signals never publish or establish event truth. |
| [`contracts/domains/hazards/domain_observation.md`](../../contracts/domains/hazards/domain_observation.md) | Draft generic Hazards observation semantics. |
| [`schemas/contracts/v1/domains/hazards/domain_observation.schema.json`](../../schemas/contracts/v1/domains/hazards/domain_observation.schema.json) | Generic Hazards observation shape; not Storm Events parser proof. |
| [`release/manifests/hazards-r0001-v1.yaml`](../../release/manifests/hazards-r0001-v1.yaml) | Inspected `PROPOSED` release-manifest placeholder. |
| [`release/promotion_decisions/hazards-r0001-v1.yaml`](../../release/promotion_decisions/hazards-r0001-v1.yaml) | Inspected `PROPOSED` promotion-decision placeholder. |

---

## 11. ADRs

No inspected accepted ADR resolves the Storm Events connector path, source ID, duplicate registry home, or runtime package.

| ADR surface | Status and effect |
|---|---|
| [`ADR-0012`](../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | `draft / proposed`; restates the Directory Rules boundary that connector outputs stop at `RAW` or `QUARANTINE`. Directory Rules remain the governing source. |
| [`ADR-0017`](../../docs/adr/ADR-0017-source-descriptor-admission-process.md) | `proposed`; describes descriptor-gated admission but does not activate this source or reconcile the duplicate descriptors. |
| [`ADR-NNNN-connectors-domain-segment`](../../docs/adr/ADR-NNNN-connectors-domain-segment.md) | `PROPOSED` scaffold; supplies no accepted decision for product placement. |

Any consolidation must explicitly choose the product path and source ID, classify the losing paths as compatibility/deprecated/removed, identify import and registry migration, update references, record drift resolution, validate rollback, and avoid activating parallel source identities.

---

## 12. Last reviewed

**2026-07-14** against `main@8fad3427a5f8ca6a8093217c1fa0a6fcc6a74401`.

Re-review when connector placement, source ID, registry topology, source activation, endpoint/access behavior, rights, table formats, source-role vocabulary, Hazards contracts/schemas, pipeline/watch tooling, fixtures/tests, release artifacts, or correction behavior changes. Review again by **2027-01-14** if none of those triggers occurs.

---

## Connector topology and placement

The inspected repository contains three distinct authority signals and no accepted consolidation decision:

```text
connectors/noaa/                         # declared NOAA family boundary; runtime scaffold
connectors/noaa-storm-events/            # this hyphenated README-only candidate
connectors/noaa_storm_events/            # underscore README-only compatibility candidate

not found in bounded probes:
connectors/noaa/storm-events/README.md
connectors/noaa/ncei-storm-events/README.md
```

The source identity surface is also split:

```text
data/registry/sources/hazards/noaa.storm_events.yaml
data/registry/hazards/sources/noaa_storm_events.yaml
```

The first is a minimal inventory placeholder. The second declares `id: noaa_storm_events` but leaves its authority, rights, cadence, and access posture unresolved. The empty source-authority register activates neither. This README therefore does not select a path or source ID.

The general drift register did not contain a matching Storm Events entry in the bounded probe. The visible conflict should be recorded or resolved through the appropriate governance workflow before implementation.

---

## Historical event record boundary

### Source role remains unresolved

Repository documents do not currently form one accepted source-role decision:

- the draft product page proposes an observation role for the event record;
- Hazards source-role documents use observed/administrative language;
- one registry template leaves `role: TBD`;
- the source-authority register has no active entry.

The connector must preserve the governing descriptor's role and record state once accepted. It must not promote a proposed vocabulary into active truth or apply one role to derived aggregates, cross-source comparisons, warnings, declarations, or modeled products.

### Table, row, event, and episode identity

Preserve at least these identity layers when the source supplies them:

```text
source family
  -> product
    -> source object or package
      -> source-declared table
        -> source row
          -> event ID
          -> episode ID
```

An event ID is not an episode ID. An episode may group multiple events. A row in a supporting table is not automatically the event record itself. Cross-table joins must follow current source evidence and be deterministic, receipted, and quarantine-safe.

### Time, vintage, and correction

Do not collapse:

```text
event begin time
!= event end time
!= source issue or file-creation time
!= source object vintage
!= KFM retrieval time
!= processing/catalog/release time
!= correction or supersession time
```

A locator or filename that later resolves to changed bytes must not silently rewrite history. Preserve the earlier bytes and lineage, create a new reviewable source identity or correction relation, and propagate affected-record review downstream.

### Geometry and geography

Source point, end point, line/path, location, county/zone, or other geography fields are not interchangeable:

- a point does not prove a footprint;
- a path line does not prove damage extent or width;
- a flash-flood event record does not prove inundation depth or polygon;
- an administrative area tag does not prove the entire area experienced the event;
- a derived buffer or polygon belongs to a downstream transform with explicit method, parameters, uncertainty, and receipt.

### Narrative, casualties, damage, and magnitude

- preserve source wording, codes, units, qualifiers, missingness, and quality/status context;
- do not treat a narrative as a complete or independently verified account;
- do not expose person-identifying or sensitive casualty details without policy review and minimization;
- preserve casualty and damage fields as source-reported or source-compiled values, not legal, insurance, compensation, or liability findings;
- preserve ratings and reported magnitudes as source fields, not automatic direct measurements;
- preserve missing values as missingness, never as zero;
- keep corrections and changed source vintages visible.

### Anti-collapse rules

| Rule | Connector implication |
|---|---|
| Historical record is not current alert. | Never emit a Storm Events record as a warning, watch, advisory, forecast, emergency instruction, or current official status. |
| Event record is not every scalar as direct measurement. | Retain rating, estimate, report, and method context; do not silently relabel fields as instrument measurements. |
| Rating is not measured wind speed. | Preserve the rating classification; any numeric derivation belongs downstream with a distinct identity and receipt. |
| Reported maximum is not actual maximum. | Preserve reported/estimated qualifiers and observation scope. |
| Flood record is not inundation. | Require separate water-depth or inundation evidence. |
| Path is not damage footprint. | Preserve source path geometry; derived buffers or damage extents remain distinct. |
| Damage estimate is not legal or insurance truth. | Preserve source estimate context and deny compensation, liability, or declaration inferences. |
| Record absence is not no hazard. | Say only that no qualifying record was found in the inspected slice; do not claim an all-clear. |
| Event is not disaster declaration. | Administrative declaration status requires its own official source and role. |
| RAW presence is not validation or release. | Admission never proves catalog closure, publication, or public eligibility. |

---

## Proposed runtime contract

No product-specific runtime is proven at either connector path. If implementation is approved, it should follow these fail-closed phases:

1. **Resolve** an approved SourceDescriptor revision, active source-authority entry, product scope, source ID, and registry home.
2. **Plan** a bounded request or source-object listing without exposing credentials, signed material, or unsafe parameters.
3. **Retrieve** into temporary storage with size, timeout, redirect, listing/pagination, resume, and retry limits.
4. **Verify** response identity, byte length, digest, archive members, headers, source object, format assumptions, and source metadata.
5. **Materialize** archives or packages with bounded member counts, safe paths, and atomic staging.
6. **Parse** tables and rows while preserving source fields, event/episode identity, time, geography, geometry, narrative, magnitude, casualty, damage, quality, and vintage context.
7. **Inspect** structural and semantic admission invariants without joining tables into new authority, deriving geometry, normalizing measurements, or issuing event conclusions.
8. **Decide** `RAW` versus `QUARANTINE` using deterministic admission rules.
9. **Commit** the handoff atomically so partial objects never appear complete.
10. **Record** sanitized process evidence and source/content fingerprints.

Retry only transient, bounded failures. Do not retry authentication or authorization failure, unsafe archive structure, deterministic checksum mismatch, unsupported format drift, broken event/episode linkage, identity conflict, unresolved rights/sensitivity, or attempted authority collapse as though those were network transients.

### Idempotency, deduplication, correction, and replay

- source identity is not only a URL, filename, event ID, episode ID, year, or table name;
- a source locator with changed bytes must create reviewable correction lineage;
- identical verified bytes may be deduplicated only through a governed immutable-reference mechanism;
- duplicate source identity with conflicting bytes must quarantine;
- corrected, replaced, or superseded objects must not overwrite prior captures;
- replay must pin descriptor revision, source-authority state, retrieval policy, source object, format/header assumptions, parser version, validation version, and output target;
- replay must preserve prior outcomes and quarantine reasons;
- caches may accelerate retrieval but never substitute for integrity, freshness, provenance, or correction checks.

---

## Evidence ledger

| Evidence surface | Observed state | What it supports | What it does not support |
|---|---|---|---|
| This README | Prior v0.1 draft exists; exact lane is README-only in bounded probes. | A documented hyphenated product boundary. | Code, source access, activation, or canonical placement. |
| Underscore README | Draft compatibility README exists under `connectors/noaa_storm_events/`. | A parallel product boundary and explicit path conflict. | An implementation or accepted compatibility contract. |
| NOAA family README/package | Family README calls `connectors/noaa/` canonical; package is `0.0.0` with placeholder runtime files. | Source-family placement posture and greenfield scaffold. | Storm Events parser, endpoint, tests, or readiness. |
| Hazards connector README | Explicitly records hyphen/underscore/possible nested conflict. | Conflict is already visible in adjacent documentation. | A resolved path or active source. |
| Draft Storm Events product page | Detailed identity, anti-collapse, source-role, geometry, narrative, casualty, damage, and correction proposals. | Candidate product doctrine and verification questions. | Current endpoints, formats, cadence, rights, or implementation. |
| Dotted registry YAML | Minimal `PROPOSED` inventory placeholder. | One candidate registry path. | Source ID fields, mature descriptor, or activation. |
| Underscored registry YAML | Greenfield descriptor with `id: noaa_storm_events` and multiple `TBD` fields. | A second candidate source identity and registry path. | Approved authority, rights, cadence, access, or activation. |
| Source-authority register | `PROPOSED`; `entries: []`. | No repository-level Storm Events activation at snapshot. | Future activation status. |
| Pipeline spec | Minimal `PROPOSED` inventory placeholder. | A named candidate pipeline-spec path. | Executable steps, schema, schedule, or validation. |
| Hazards pipeline modules | Inspected ingest/normalize/validate modules are one-line greenfield comments. | Generic runtime is not implemented in those files. | Absence from every possible code path. |
| Storm Events watcher README | Proposed watcher contract; named executable probes absent. | Watcher/non-publisher boundary. | A functioning watcher, schedule, or report. |
| Hazards release index and artifacts | Index describes a released slice; inspected manifest/decision files are `PROPOSED` placeholders. | A material release-evidence conflict requiring review. | Release closure or published Storm Events data. |
| Generic Hazards contract/schema | Draft semantic contract and compact schema exist. | Candidate generic record meaning and shape. | Product parser conformance, table linkage, fixtures, or source activation. |
| Drift register | No Storm Events match in bounded probe. | Conflict is not recorded there under the searched terms. | A complete history of every governance discussion. |
| CODEOWNERS | Global fallback; no Storm Events-specific rule. | Ownership remains unresolved. | Steward approval or accountability. |

---

## Rights, sensitivity, and public safety

Repository documentation is not a substitute for current source terms. Before activation, governing records must verify licensing or terms, attribution, redistribution, caching, service constraints, access method, narrative reuse, casualty/person-detail handling, intended use, and product-specific restrictions.

The connector must:

- carry rights, attribution, sensitivity, public-safety, and review record identifiers;
- quarantine when terms, retention, redistribution, citation, narrative use, or public-display posture is unresolved;
- keep credentials, tokens, cookies, signed URLs, and sensitive query strings out of commits, manifests, logs, receipts, and exceptions;
- minimize or quarantine person-identifying narrative/casualty content until governing policy permits use;
- preserve historical, source-reported, estimated, quality, and uncertainty qualifiers;
- avoid presenting source records as current operational guidance, property-specific certainty, legal findings, or proof of safety;
- avoid joins that create unreviewed household, landowner, infrastructure, casualty, cultural-site, health, or operational claims;
- defer aggregation, generalization, suppression, redaction, delay, notification, and public-safe rendering to governed downstream policy and release controls.

Public availability or government-source status does not make connector output automatically eligible for KFM publication, emergency use, legal reliance, or life-safety use.

---

## Activation, promotion, and rollback

### Activation prerequisites

Do not activate this connector until all of the following are true:

- one canonical connector home, package/import identity, source ID, and registry home are ratified;
- compatibility, migration, reference updates, and rollback for the losing paths are documented;
- owners and Storm Events-specific review burden are assigned;
- an authoritative SourceDescriptor conforms to the accepted schema and the source-authority register records approved activation;
- source-role vocabulary is reconciled across product, Hazards, registry, and contract surfaces;
- current endpoint/access, authentication if any, object listing, file/table formats, field vocabulary, quality/status codes, timezones, cadence, correction behavior, terms, attribution, and citation are verified;
- accepted Hazards event/observation/identity/correction contracts and schemas cover the admitted product;
- bounded retrieval, archive safety, table linkage, event/episode identity, time, geography, geometry, narrative, casualty, damage, quality, redaction, replay, and correction tests pass;
- no-network fixtures cover valid, invalid, denied, abstained, quarantined, and error outcomes;
- `RAW`/`QUARANTINE` paths and downstream Hazards ownership are approved;
- pipeline, watcher, and release artifacts are implemented and validated rather than inferred from placeholders;
- release-evidence conflict is resolved with real manifests, decisions, receipts, proofs, correction, and rollback support;
- downstream code cannot fetch directly, bypass source admission, issue warnings, or publish.

### Promotion boundary

Successful admission means only that source material entered `RAW` with required evidence. It does not confirm every field as a direct measurement, turn a point or path into a footprint, establish that an unrecorded hazard did not occur, prove a disaster declaration, create a current warning, validate a cross-source comparison, or make anything public. Every later transition belongs to downstream governed stages.

### Correction and deactivation

If source identity, bytes, table linkage, event/episode identity, time, geography, geometry, narrative, magnitude, casualty, damage, quality, rights, sensitivity, validation, or release evidence is later found wrong:

1. stop new admissions for the affected configuration;
2. preserve prior immutable bytes, manifests, and process evidence;
3. mark affected rows, events, episodes, aggregates, comparisons, catalog records, and downstream releases for review;
4. quarantine new or replayed material until the contradiction is resolved;
5. issue correction, withdrawal, and release actions only through their governing surfaces;
6. reactivate only with a new reviewed configuration or SourceDescriptor revision.

Do not rewrite history, silently replace source files, delete evidence, or publish no-hazard/all-clear claims to simulate rollback.

---

## Verification backlog

- [ ] Ratify one canonical Storm Events connector home and document compatibility, migration, deprecation, references, and rollback for the others.
- [ ] Record or resolve the hyphen/underscore/nested connector conflict in the appropriate drift/governance surface.
- [ ] Resolve dotted versus underscored source ID and duplicate registry-home drift without parallel activation.
- [ ] Replace `OWNER_TBD` with accountable reviewers and Storm Events CODEOWNERS coverage.
- [ ] Replace NOAA family greenfield placeholders with reviewed package/runtime decisions or keep them explicitly inactive.
- [ ] Create a conforming SourceDescriptor and add approved Storm Events activation to the source-authority register.
- [ ] Reconcile observation/observed/administrative/candidate/aggregate vocabulary with accepted source-role doctrine.
- [ ] Verify current endpoints, access/authentication, objects, file/table formats, headers, fields, event types, quality/status codes, timezones, cadence, corrections, terms, attribution, and citation.
- [ ] Confirm accepted Hazards event, observation, identity, correction, receipt, and release contracts/schemas.
- [ ] Implement bounded retrieval, archive safety, byte preservation, table/row/event/episode identity, credential redaction, atomic handoff, and deterministic quarantine.
- [ ] Add no-network fixtures and executable tests for identity, linkage, time, geometry, narrative/casualty sensitivity, magnitude/damage qualifiers, source drift, replay, correction, and failure cases.
- [ ] Replace the pipeline spec, generic pipeline modules, and watcher stubs with meaningful code/spec/tests before treating them as readiness evidence.
- [ ] Reconcile the release-index claim with real, validated release manifests, promotion decisions, receipts, proofs, rollback, and published artifacts—or correct the index.
- [ ] Verify downstream normalization, aggregates, comparisons, EvidenceBundles, catalog/triplets, release, correction, API/UI, and public-safe caveats independently.

---

## Definition of done

This README update is complete when it accurately preserves the current boundary without claiming implementation. The connector itself is not done until every activation prerequisite and verification item above is resolved through its governing surface.

In all states:

- source, object, table, row, event, episode, time, geography, geometry, magnitude, narrative, casualty, damage, quality, and source-vintage identity remain intact;
- event IDs never collapse into episode IDs or supporting-table row identity;
- historical records never become current warnings or emergency guidance;
- ratings, estimates, and reported maxima never silently become direct measurements or legal findings;
- flood records never become inundation, and paths never become damage footprints, without separate governed evidence and transforms;
- missing records and missing values never become zero, no-hazard, normal, or all-clear claims;
- observation, administrative context, derived aggregates, comparisons, declarations, and modeled artifacts remain distinct;
- sensitive narrative, casualty, location, and person details fail closed pending policy review;
- connector and watcher activity never becomes release or publication authority;
- connector output stops at `RAW` or `QUARANTINE`;
- placement, source ID, schema, registry, policy, pipeline, proof, release, alert, API, and UI authority remain outside this folder.

---

## Changelog

### v0.2 — 2026-07-14

- Reframed the path as a README-only proposed Storm Events connector boundary.
- Surfaced the hyphenated/underscored/nested placement conflict and dotted/underscored source-identity drift.
- Recorded the NOAA `0.0.0` scaffold, duplicate registry placeholders, empty source-authority register, placeholder pipeline spec, greenfield Hazards modules, README-only watcher, and release-evidence conflict.
- Tightened table/row/event/episode, time/vintage/correction, geometry, narrative, casualty, magnitude, damage, quality, missingness, and anti-collapse requirements.
- Removed version-sensitive live-source specifics from the connector contract and moved them into the verification backlog.
- Added fail-closed retrieval, archive safety, quarantine, no-network testing, replay, correction, activation, deactivation, and rollback requirements.
- Preserved the `RAW`/`QUARANTINE`-only lifecycle limit and denied warning, declaration, legal, emergency, and publication authority.

### v0.1 — 2026-06-19

- Established the initial NOAA Storm Events connector-lane documentation.

<p align="right"><a href="#top">Back to top</a></p>
