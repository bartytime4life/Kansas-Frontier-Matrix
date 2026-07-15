<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-noaa-hms-smoke-readme
title: connectors/noaa-hms-smoke/ — NOAA HMS Fire and Smoke README-Only Connector Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Source steward · Connector steward · NOAA steward · Hazards steward · Atmosphere steward · Public-safety reviewer · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-14
policy_label: public-doctrine; connector-boundary; noaa; hms; multi-component; analyst-augmented; placement-open; not-life-safety; no-publication
truth_posture: CONFIRMED README-only sibling / PROPOSED placement / INACTIVE source authority / IMPLEMENTATION NEEDS VERIFICATION
evidence_snapshot: main@a6f3defda415462f595f098ca7758aa14826bfa7
related:
  - ../README.md
  - ../noaa/README.md
  - ../noaa/src/README.md
  - ../noaa/tests/README.md
  - ../hms_smoke/README.md
  - ../../docs/sources/catalog/noaa/README.md
  - ../../docs/sources/catalog/noaa/hms-fire-smoke.md
  - ../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../docs/architecture/hazards-trust-membrane.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/directory-rules.md
  - ../../control_plane/source_authority_register.yaml
  - ../../pipeline_specs/hazards/noaa_hms_smoke.yaml
  - ../../tools/ingest/firms_hms_watch/README.md
  - ../../data/raw/atmosphere/observed/hms/README.md
  - ../../contracts/domains/atmosphere/SmokeContext.md
tags: [kfm, connectors, noaa, hms, smoke, fire, hazards, atmosphere, analyst-augmented, multi-component, source-admission, raw, quarantine, governance]
notes:
  - "This file documents a proposed connector boundary; it does not prove executable NOAA HMS connector code."
  - "The repository also contains the canonical NOAA family lane and a documentation-only underscore compatibility lane; this README does not settle final HMS placement."
  - "HMS fire detections and smoke polygons are distinct components and must not be collapsed into one source role or truth claim."
  - "Smoke polygons and density categories are qualitative analyst-augmented context, not surface PM2.5, AQI, exposure, or health guidance."
  - "Fire detections are satellite-signal evidence with analyst augmentation, not ground-confirmed fire status."
  - "Connector output is limited to RAW or QUARANTINE handoff and is never KFM alert or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NOAA HMS Fire and Smoke README-Only Connector Boundary

> Boundary for proposed NOAA Hazard Mapping System (HMS) fire-and-smoke source admission at `connectors/noaa-hms-smoke/`. Repository evidence at the pinned snapshot proves this README, not a runnable product connector. Final placement among the NOAA family lane, this hyphenated sibling, and the underscore compatibility lane remains unresolved.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: not proven" src="https://img.shields.io/badge/implementation-not__proven-lightgrey">
  <img alt="Placement: open" src="https://img.shields.io/badge/placement-open-orange">
  <img alt="Product: multi-component" src="https://img.shields.io/badge/product-multi__component-purple">
  <img alt="Life safety: never alert authority" src="https://img.shields.io/badge/life__safety-never__alert__authority-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Truth posture:** `CONFIRMED` README-only sibling · `PROPOSED` placement · source authority `INACTIVE / NOT ESTABLISHED` · product-specific runtime `NEEDS VERIFICATION`.

> [!WARNING]
> **KFM is not an alert, emergency-response, air-quality, or life-safety authority.** This connector must never issue warnings, recommend evacuation or sheltering, determine exposure, declare an area safe, or replace official NOAA, NWS, AirNow, public-health, fire, or emergency-management channels.

> [!CAUTION]
> HMS smoke polygons are analyst-augmented qualitative plume context, not surface PM2.5, AQI, exposure, or health guidance. HMS fire detections are satellite-signal evidence with analyst augmentation, not ground-confirmed fire status.

**Quick jumps:** [Purpose](#1-purpose) · [Status](#3-status) · [Validation](#8-validation) · [Topology](#connector-topology-and-placement) · [Component boundary](#component-and-source-role-boundary) · [Runtime contract](#proposed-runtime-contract) · [Evidence](#evidence-ledger) · [Backlog](#verification-backlog)

---

## 1. Purpose

`connectors/noaa-hms-smoke/` defines a conservative source-admission boundary for NOAA HMS fire-detection and smoke-polygon source material and its source metadata.

If executable code is later approved here, it may discover or retrieve an explicitly configured source object, preserve its native bytes and component identity, validate only admission preconditions, and hand the result to a domain-owned `RAW` or `QUARANTINE` lane. This README does not activate a source, select a live endpoint, establish a current format or cadence, or prove that product-specific code exists.

The boundary is narrow:

```text
configured HMS source object
           |
           v
bounded retrieval and integrity checks
           |
           v
component-preserving admission
       fire detection != smoke polygon
           |
           +----> RAW         only when admission preconditions pass
           |
           `----> QUARANTINE  when identity, component, role, time,
                              integrity, rights, safety, or routing is unresolved
```

[Back to top ↑](#top)

---

## 2. Authority level

**Authority: IMPLEMENT boundary documentation; no source, alert, or publication authority.**

This README may describe what a future connector at this path is allowed to do. It may not:

- ratify this sibling as the canonical HMS implementation home;
- override `connectors/noaa/` as the declared NOAA family lane;
- turn `connectors/hms_smoke/` into a runtime path;
- activate HMS in the source-authority register;
- promote the NOAA family scaffold into a working HMS connector by declaration;
- select among duplicate SmokeContext contract or schema paths;
- assign authoritative source roles without accepted descriptors and contracts;
- define NOAA/HMS product truth, rights, sensitivity, or freshness policy;
- confirm fire on the ground, quantify smoke, or provide health or emergency guidance;
- promote data beyond source admission;
- create release authority or public behavior.

The two Directory Rules copies agree on the connector lifecycle limit but differ in version and status. This README relies only on their shared rule: connectors fetch and parse source material and may write to `RAW` or `QUARANTINE`, not later lifecycle stages. It does not decide which Directory Rules file is authoritative.

---

## 3. Status

| Question | Evidence-backed status |
|---|---|
| Does `connectors/noaa-hms-smoke/README.md` exist? | **CONFIRMED.** |
| Is executable code proven in this exact lane? | **No.** Bounded probes found no package file, source root, client, parser, initializer, or test README. |
| Is there another HMS connector path? | **Yes.** `connectors/hms_smoke/README.md` is a documentation-only compatibility/reconciliation lane that forbids implementation there. |
| Is there a canonical NOAA family lane? | **Yes, as repository doctrine.** `connectors/noaa/README.md` calls `connectors/noaa/` the canonical family lane while preserving this sibling as placement-pending. |
| Is a nested HMS product lane present under `connectors/noaa/`? | **No file was found at the bounded `hms-smoke/` or `hms_smoke/` README probes.** |
| Does the NOAA package prove HMS runtime support? | **No.** It is version `0.0.0`; the initializer is empty, fetch/admit files are placeholder comments, the local descriptor has `TBD` role and rights, and the proposed `products/hms_smoke.py` file was not found. |
| Is an HMS pipeline implemented by the named pipeline spec? | **No.** `pipeline_specs/hazards/noaa_hms_smoke.yaml` is a four-line `PROPOSED` placeholder. |
| Is the FIRMS/HMS watcher executable? | **Not proven.** Its README explicitly defines a proposed tooling boundary. |
| Is an active HMS SourceDescriptor present? | **Not proven.** Named NOAA/HMS registry probes returned no files, and the source-authority register is `PROPOSED` with `entries: []`. |
| Are SmokeContext contracts and schemas enforceable? | **Not proven.** Duplicate contract/schema names exist; inspected schemas are permissive `PROPOSED` scaffolds with empty properties. |
| Are HMS RAW payloads, receipts, tests, CI, and release wiring proven? | **No.** The RAW lane and test surfaces are documentation; operational evidence remains unverified. |

Absence statements above are limited to named repository paths inspected at `main@a6f3defda415462f595f098ca7758aa14826bfa7`; they are not claims of an exhaustive recursive inventory.

---

## 4. What belongs

If this path is ratified, it may contain product-specific connector artifacts such as:

- request or object-discovery adapters that take an approved SourceDescriptor reference;
- bounded retrieval helpers with explicit timeouts, retries, redirect policy, and maximum size;
- checksum, content-length, component-package, and source-fingerprint verification;
- lossless capture of source files, component files, sidecars, and exposed metadata;
- fire-detection parsing that preserves signal identity and uncertainty;
- smoke-polygon parsing that preserves qualitative categories and analyst-augmentation context;
- component splitting without semantic rewriting;
- deterministic RAW or QUARANTINE handoff envelopes;
- sanitized process receipts that reference, rather than redefine, governing records;
- no-network fixtures representing approved structural cases;
- unit and contract tests for source admission and anti-collapse behavior.

Every artifact must preserve source identity, component identity, time roles, and uncertainty, and must fail closed when required evidence is missing or contradictory.

---

## 5. What does NOT belong

| Excluded responsibility | Governing surface or next decision |
|---|---|
| Canonical connector placement | Directory decision or accepted ADR with migration and rollback; do not infer it from directory presence. |
| NOAA family or HMS product doctrine | `docs/sources/catalog/noaa/` and the HMS product page. |
| Source activation | `control_plane/source_authority_register.yaml` plus approved descriptors and review. |
| SourceDescriptor schema authority | Resolve the documented source-schema conflict outside this README. |
| SmokeContext contract/schema authority | Resolve duplicate naming and schema-home drift outside this connector. |
| Source-role vocabulary or final component roles | Accepted SourceDescriptors, contracts, and source-role governance. |
| Fire-event or active-wildfire truth | Hazards-domain evidence and official operational authorities. |
| Surface PM2.5, AQI, exposure, or health guidance | Ground-monitor and air-quality authorities with governed downstream derivation. |
| Warning, watch, advisory, evacuation, or route-safety behavior | Official authorities; never this connector or KFM. |
| FIRMS/HMS/CAP/NWS/AirNow joins | Downstream pipelines with explicit temporal/spatial rules and receipts. |
| Watcher material-change decisions | Approved tooling and review workflow; watcher signals are not event truth. |
| Normalized or processed products | Downstream domain pipelines after admission. |
| Catalog, triplet, tile, or published artifacts | Governed lifecycle and release surfaces. |
| Rights, sensitivity, or public-safety decisions | `policy/` and release review. |
| EvidenceBundle closure | Downstream proof processes; connector receipts are process evidence only. |
| Public API, UI, map, notification, or generated-answer behavior | Governed application surfaces after release. |

---

## 6. Inputs

A future connector invocation should accept only explicit, governed inputs. At minimum:

| Input | Required treatment |
|---|---|
| SourceDescriptor reference and revision | Required before retrieval; must resolve to an approved source identity, component scope, and activation posture. |
| Product and component identity | Preserve source family, HMS product, fire/smoke component, product or issue identity, and any exposed version. |
| Approved source locator | Treat as configuration, not a hard-coded claim in this README. Redact credentials and sensitive query material. |
| Expected object identity | Preserve filename or object key, expected component files, size when known, checksum algorithm/digest when known, and source metadata. |
| Retrieval policy | Bound schemes, hosts, redirects, timeouts, retries, maximum object size, pagination, and resume behavior. |
| Time interpretation | Preserve observation/acquisition window, smoke start/end, issue/update, retrieval, expiry/review, and correction/supersession time as distinct roles where exposed. |
| Routing context | Name the owning domain and proposed RAW/QUARANTINE destination without granting downstream promotion. |
| Rights and attribution reference | Carry governing record identifiers and unresolved review state; do not decide rights locally. |
| Public-safety posture | Carry a permanent not-life-safety marker and official-source redirection policy. |

Live endpoints, file/service formats, filename conventions, field names, cadence, coverage, access requirements, rights, and analyst-pass metadata are version-sensitive external facts. They must be verified in product-specific evidence before implementation or activation; this README intentionally does not pin them.

---

## 7. Outputs

The connector may emit only an atomic source-admission handoff to one of:

```text
data/raw/<owning-domain>/<source-id>/<run-id>/
data/quarantine/<owning-domain>/<source-id>/<run-id>/
```

The exact layout remains subject to governing repository contracts. Conceptually, a handoff should include:

- byte-preserving source payload or an immutable reference permitted by policy;
- source sidecars and original component files;
- a sanitized request/retrieval manifest;
- source, product, component, issue/pass, and object identity;
- distinct fire-detection and smoke-polygon records or references;
- native field names, qualitative categories, geometry, projection/CRS, and source uncertainty;
- exposed analyst-augmentation identifiers or times without invented internal details;
- observed/acquisition, start/end, issue/update, retrieval, expiry/review, and correction time roles;
- source and content fingerprints;
- observed size and checksum results;
- rights, attribution, sensitivity, and public-safety references or unresolved flags;
- validation results and deterministic quarantine reasons;
- owning-domain routing and run identity.

The connector must not emit directly to `WORK`, `PROCESSED`, `CATALOG`, `TRIPLETS`, `PUBLISHED`, release, API, UI, notification, or generated-answer surfaces.

---

## 8. Validation

Validation is source admission validation, not scientific confirmation, operational warning validation, or publication approval.

### Required checks

- source identity and SourceDescriptor revision resolve and are approved for use;
- product, component, object/package, issue/pass, and source-file identity are present where applicable;
- fire detections and smoke polygons cannot enter as one undifferentiated role;
- retrieval follows configured scheme, host, redirect, timeout, retry, pagination, and size constraints;
- payload and all required component files are complete and content digests are recorded;
- archives and multi-file packages are bounded and safe to materialize;
- native geometry, projection/CRS, fields, qualitative categories, and uncertainty can be read without semantic mutation;
- observation/acquisition, start/end, issue/update, retrieval, expiry/review, and correction times remain distinct where applicable;
- analyst-augmentation context preserves only what the source exposes;
- smoke categories remain qualitative and cannot produce numeric PM2.5, AQI, exposure, or health claims;
- fire detections remain evidence of satellite signals and cannot become ground-confirmed fire state;
- rights, attribution, sensitivity, public-safety, and routing references are present or the object is quarantined;
- output destination is limited to RAW or QUARANTINE;
- logs and receipts contain no credentials, signed URLs, unsafe payload excerpts, or sensitive operational detail.

### Quarantine conditions

Quarantine on missing, ambiguous, or conflicting evidence, including:

- unresolved source, product, component, issue/pass, or object identity;
- mixed fire/smoke payload with no deterministic component split;
- checksum, size, member-list, or component-package mismatch;
- unreadable, truncated, structurally unsafe, or partially retrieved content;
- unexpected fields, geometry, projection, qualitative category, or source-schema drift;
- stale, future-dated, timezone-ambiguous, conflicting, or unsupported time roles;
- missing analyst-augmentation context that governing descriptors require;
- attempt to translate qualitative smoke category into concentration or exposure;
- attempt to treat a fire detection as confirmed ground state;
- unresolved rights, attribution, sensitivity, public-safety, or domain routing;
- duplicate identity with different bytes;
- any attempt to treat the connector as alert, promotion, or publication authority.

An empty, missing, or partially available source object is not proof of no fire, no smoke, or safe conditions.

### No-network test posture

Tests should be deterministic and no-network by default. Fixtures should cover, at minimum:

- valid fire-detection and smoke-polygon components kept separate;
- a mixed package that splits deterministically and one that must quarantine;
- checksum, size, component-list, and archive-safety failures;
- missing or conflicting source/component/issue/pass identity;
- stale, future-dated, timezone-ambiguous, and corrected/reissued products;
- unknown or changed fields, categories, geometry, or projection;
- smoke category to PM2.5/AQI/exposure conversion attempts;
- fire detection to ground-confirmed wildfire conversion attempts;
- empty or partial source objects that must not become an all-clear;
- duplicate source identity with identical bytes and with conflicting bytes;
- rights, sensitivity, or routing state that forces quarantine;
- credential and signed-URL redaction;
- rejection of every output destination beyond RAW or QUARANTINE;
- rejection of warning, notification, evacuation, sheltering, or health-guidance output.

---

## 9. Review burden

Changes here require review proportional to their effect:

| Change | Minimum review burden |
|---|---|
| README clarification with no authority change | Connector steward, NOAA source steward, and docs review. |
| Placement, rename, merge, redirect, or removal of an HMS lane | Architecture/governance review and accepted migration decision. |
| New endpoint, access method, credential flow, or retrieval behavior | Source steward, security review, rights review, and no-network tests. |
| New format, component, field, category, cadence, or time behavior | Source, Hazards, Atmosphere, spatial, and validation review with versioned fixtures. |
| Source-role or component mapping | Source-role governance and domain contract review; never connector-only approval. |
| Hash, deduplication, replay, correction, or quarantine change | Data/validation review with deterministic regression tests. |
| FIRMS, CAP, NWS, AirNow, monitor, or model join | Downstream pipeline, evidence, policy, and domain review. |
| Activation, promotion, public display, or operational use | Source authority, rights, safety, proof, and release review outside this lane. |

`OWNER_TBD` must be replaced before operational activation. The global CODEOWNERS file does not establish a NOAA HMS-specific owner at the pinned snapshot.

---

## 10. Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Root connector boundary and RAW/QUARANTINE limit. |
| [`../noaa/README.md`](../noaa/README.md) | Declared canonical NOAA connector-family boundary. |
| [`../noaa/src/README.md`](../noaa/src/README.md) | Proposed NOAA source-root contract; not product implementation proof. |
| [`../noaa/tests/README.md`](../noaa/tests/README.md) | Proposed no-network family test contract; not passing-test proof. |
| [`../hms_smoke/README.md`](../hms_smoke/README.md) | Documentation-only underscore compatibility/reconciliation lane. |
| [`../hazards/README.md`](../hazards/README.md) | Hazard connector compatibility index and source-family-first posture. |
| [`../../docs/sources/catalog/noaa/README.md`](../../docs/sources/catalog/noaa/README.md) | NOAA source-family catalog context. |
| [`../../docs/sources/catalog/noaa/hms-fire-smoke.md`](../../docs/sources/catalog/noaa/hms-fire-smoke.md) | Draft multi-component HMS product doctrine and open questions. |
| [`../../docs/architecture/smoke-atmosphere-hazards.md`](../../docs/architecture/smoke-atmosphere-hazards.md) | Draft cross-domain smoke seam architecture. |
| [`../../docs/architecture/hazards-trust-membrane.md`](../../docs/architecture/hazards-trust-membrane.md) | Hazards public-safety and trust boundary. |
| [`../../pipeline_specs/hazards/noaa_hms_smoke.yaml`](../../pipeline_specs/hazards/noaa_hms_smoke.yaml) | `PROPOSED` pipeline placeholder, not executable wiring. |
| [`../../tools/ingest/firms_hms_watch/README.md`](../../tools/ingest/firms_hms_watch/README.md) | Proposed review-signal watcher boundary, not confirmed executable. |
| [`../../data/raw/atmosphere/observed/hms/README.md`](../../data/raw/atmosphere/observed/hms/README.md) | Draft RAW lane boundary; payloads and activation remain unproven. |
| [`../../contracts/domains/atmosphere/SmokeContext.md`](../../contracts/domains/atmosphere/SmokeContext.md) | Draft semantic contract for smoke context. |
| [`../../contracts/domains/atmosphere/smoke-context.md`](../../contracts/domains/atmosphere/smoke-context.md) | Parallel contract name; canonical naming is not selected here. |
| [`../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json`](../../schemas/contracts/v1/domains/atmosphere/SmokeContext.schema.json) | Permissive `PROPOSED` scaffold. |
| [`../../schemas/contracts/v1/domains/atmosphere/smoke-context.schema.json`](../../schemas/contracts/v1/domains/atmosphere/smoke-context.schema.json) | Parallel permissive scaffold; not selected here. |
| [`../../schemas/contracts/v1/domains/atmosphere/smoke_context.schema.json`](../../schemas/contracts/v1/domains/atmosphere/smoke_context.schema.json) | Third permissive scaffold; not selected here. |

---

## 11. ADRs

- [`../../docs/adr/README.md`](../../docs/adr/README.md) is the ADR index and process surface.
- [`../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md`](../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) records the connector-output proposal; its draft/proposed state does not independently create authority.
- No accepted HMS connector-placement ADR was identified in the bounded evidence review.
- [`../../docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) had no `noaa-hms-smoke`, `hms_smoke`, `NOAA HMS`, or `HMS Smoke` text match in a bounded scan. That does not mean the path drift is resolved or exhaustively audited.

Required decisions before product-specific implementation or activation:

1. Choose the canonical HMS connector topology and define redirects or deprecation for non-canonical paths.
2. Choose stable product/component source IDs, aliases, package/import names, and domain routing.
3. Resolve SourceDescriptor schema authority and active component descriptors.
4. Resolve SmokeContext contract/schema naming and domain ownership.
5. Define current source access, component split, time, correction, rights, sensitivity, and not-life-safety rules.
6. Define owner, fixture, validator, pipeline, watcher, correction, and rollback responsibilities.

This README does not pre-decide any of those outcomes.

---

## 12. Last reviewed

**2026-07-14**, against repository snapshot `main@a6f3defda415462f595f098ca7758aa14826bfa7`.

Review scope was bounded to the named connector, NOAA family scaffold, underscore compatibility lane, source catalog, rules, source authority, named registry paths, source-schema contract, pipeline placeholder, watcher README, RAW lane, smoke contracts/schemas, domain architecture, drift, ownership, and workflow surfaces cited here. Re-review after any topology decision, source activation, descriptor/schema migration, source-interface change, component/category change, rights change, or executable implementation.

---

## Connector topology and placement

Repository evidence exposes several different homes or proposals:

| Path | Observed state | Safe interpretation |
|---|---|---|
| `connectors/noaa/` | Declared canonical NOAA family lane; package is a `0.0.0` greenfield scaffold. | Family coordination and future implementation root, not current HMS runtime proof. |
| `connectors/noaa-hms-smoke/` | This README exists; named implementation probes found no code or tests. | Proposed hyphenated product sibling. |
| `connectors/hms_smoke/` | v0.2 README exists and explicitly forbids implementation there. | Documentation-only compatibility/reconciliation lane. |
| `connectors/noaa/hms-smoke/` | Bounded README probe returned no file. | Possible nested home, not repository-present at the inspected path. |
| `connectors/noaa/hms_smoke/` | Bounded README probe returned no file. | Possible nested home, not repository-present at the inspected path. |
| `connectors/noaa/src/noaa/products/hms_smoke.py` | Bounded probe returned no file. | Proposed module named by source-root docs, not implemented evidence. |

Directory Rules §7.3 lists the `noaa/` family. The NOAA family README calls its family lane canonical while treating this sibling as draft and migration-pending. Do not copy code across lanes, split component responsibility by path, create import aliases, delete compatibility documentation, or move descriptors until an accepted decision covers lineage, redirects, deprecation, tests, activation, correction, and rollback.

---

## Component and source-role boundary

### Multi-component product

HMS fire detections and smoke polygons travel in related source products but represent different kinds of evidence. They must retain distinct component identifiers, source-role decisions, time semantics, uncertainty, validation, and downstream routing.

The draft HMS product page proposes:

| Component | Draft repository posture | Connector limitation |
|---|---|---|
| Fire detection | Observation of an analyst-confirmed satellite signal. | Not ground-confirmed fire, ignition cause, containment status, evacuation trigger, or all-clear. |
| Smoke polygon | Modeled/interpretive analyst-drawn visible-plume boundary. | Not surface concentration, PM2.5, AQI, exposure, health guidance, or advisory. |
| Reprojected/aggregated derivative | Aggregate with transform/aggregation lineage. | Not connector output and not per-place truth. |
| Unresolved or mixed admission | Candidate/quarantine. | Not publishable and not safe to summarize as current conditions. |

Those role labels remain draft product doctrine until accepted descriptors and source-role contracts settle the authoritative enum and mapping. The connector’s non-negotiable duty is to prevent component collapse and preserve the evidence needed for the governing layer to decide.

### Analyst augmentation

Analyst review changes provenance burden, not epistemic category into ground truth. Preserve only source-exposed issue/pass identifiers, review state, source inputs, or timestamps. Do not invent analyst identity, internal procedures, thresholds, confidence, or review parameters.

### Time and freshness

Do not collapse:

```text
satellite acquisition or observation window
!= smoke start/end or product-valid window
!= source issue/update time
!= KFM retrieval time
!= expiry/review time
!= correction or supersession time
```

A successful retrieval does not prove that conditions are current. A historical, stale, corrected, partial, or empty product must remain visibly qualified.

### Anti-collapse rules

- smoke polygon does not prove smoke at breathing height at every enclosed location;
- qualitative smoke category does not map directly to numeric concentration or exposure;
- fire detection does not prove a currently burning ground event;
- analyst augmentation does not create independent field observation;
- watcher material-change signal does not confirm an event or authorize publication;
- cross-product proximity does not create causal or identity truth;
- RAW presence does not imply validation, release, or public eligibility;
- HMS source material never becomes a KFM warning or all-clear.

---

## Proposed runtime contract

No product-specific runtime is proven at this path. If implementation is approved, it should follow these fail-closed phases:

1. **Resolve** approved SourceDescriptor revisions, product/component scope, and source locator.
2. **Plan** a bounded request without exposing credentials, signed material, or unsafe parameters.
3. **Retrieve** into temporary storage with size, timeout, redirect, pagination, and retry limits.
4. **Verify** response identity, package members, byte length, digest, sidecars, and source metadata.
5. **Split** fire and smoke components without losing native fields, uncertainty, or package lineage.
6. **Inspect** geometry, projection, categories, and time roles without deriving concentration or ground state.
7. **Decide** RAW versus QUARANTINE using deterministic admission rules.
8. **Commit** the handoff atomically so partial objects never appear complete.
9. **Record** sanitized process evidence and source/content fingerprints.

Retry only transient, bounded failures. Do not retry authentication failure, forbidden access, component or role contradiction, unsafe archive structure, deterministic checksum mismatch, unsupported schema/category change, or unresolved policy state as though those were network transients.

### Idempotency, deduplication, correction, and replay

- source identity is not only a URL or calendar date;
- a locator with changed bytes must create a new reviewable identity or correction lineage;
- identical verified bytes may be deduplicated only through a governed immutable-reference mechanism;
- duplicate source identity with conflicting bytes must quarantine;
- corrected or reissued source material must not overwrite prior captures;
- replay must pin descriptor revisions, retrieval policy, component mapping, validation version, and output target;
- replay must preserve prior outcomes and quarantine reasons;
- caches may accelerate retrieval but never substitute for integrity, freshness, or provenance checks.

---

## Evidence ledger

| Evidence surface | Observed state | What it supports | What it does not support |
|---|---|---|---|
| This README | Prior v0.1 draft exists. | A documented hyphenated product boundary. | Code, activation, source access, or canonical placement. |
| NOAA family README | Calls `connectors/noaa/` canonical and this lane draft/migration-pending. | Source-family-first placement posture. | A final HMS subpath or working implementation. |
| NOAA package files | `0.0.0` placeholder; empty initializer; placeholder fetch/admit; descriptor role/rights `TBD`. | Greenfield family scaffolding exists. | HMS parser, package readiness, active descriptor, or endpoint behavior. |
| Underscore compatibility README | Documentation-only; implementation forbidden there. | A reconciliation path and explicit drift warning. | A third runtime authority. |
| Draft HMS product page | Multi-component, analyst-augmented, anti-collapse doctrine and open questions. | Required semantic caution and proposed component roles. | Current endpoints, cadence, rights, formats, or accepted implementation. |
| Source-authority register | `PROPOSED`; `entries: []`. | No repository-level HMS activation at snapshot. | Future activation status. |
| Named registry probes | No NOAA/HMS descriptor file found at inspected paths. | No descriptor is proven by those paths. | Exhaustive registry absence. |
| HMS pipeline YAML | Four-line `PROPOSED` placeholder. | A named future spec location. | Pipeline implementation, schedule, validation, or release wiring. |
| FIRMS/HMS watcher README | Proposed review-signal-only boundary. | Watcher safeguards are documented. | Executable watcher, cadence, thresholds, or run evidence. |
| HMS RAW lane README | Draft source-capture boundary. | A no-public-path RAW posture. | Payloads, descriptor, receipts, role split, or release evidence. |
| SmokeContext contracts/schemas | Duplicate naming; inspected schemas allow arbitrary properties. | Semantic work has candidate homes. | Enforceable canonical schema. |
| Connector/source-descriptor workflows | Inspected workflows are TODO echo-only stubs. | No meaningful automated connector/descriptor gate is proven. | Runtime or activation readiness. |
| CODEOWNERS | Global placeholder; no NOAA HMS-specific rule identified. | Owner remains unresolved. | Operational accountability. |

---

## Rights, sensitivity, and public safety

Repository documentation is not a substitute for current source terms. Before activation, governing records must verify licensing or terms, attribution, redistribution, caching, service constraints, access method, intended use, and product-specific restrictions.

The connector must:

- carry rights, attribution, sensitivity, and review record identifiers;
- quarantine when terms, component use, retention, or attribution are unresolved;
- keep credentials, tokens, cookies, signed URLs, and sensitive query strings out of commits, manifests, logs, receipts, and exceptions;
- preserve source uncertainty and not-life-safety limitations with every handoff;
- avoid presenting cultural/prescribed burns, industrial signals, false positives, or other ambiguous detections as confirmed wildfire events;
- avoid joins or location detail that could create sensitive infrastructure, community, cultural, tribal, health, or response claims;
- defer aggregation, generalization, suppression, notification, and public-safe rendering to governed downstream policy and release controls.

Public availability or operational source status does not mean connector output is automatically approved for KFM publication or life-safety use.

---

## Activation, promotion, and rollback

### Activation prerequisites

Do not activate this connector until all of the following are true:

- topology, package/import identity, ownership, and compatibility plan are ratified;
- authoritative SourceDescriptor and source-schema paths are resolved for each admitted component;
- the source-authority register records approved HMS component entries;
- SmokeContext contract/schema naming and domain ownership are resolved where required;
- current endpoint/access, format/package, fields/categories, cadence, coverage, time, correction, and analyst-augmentation evidence is verified;
- rights, attribution, sensitivity, and permanent not-life-safety reviews are complete;
- component split, integrity, geometry, time, redaction, quarantine, replay, correction, and no-network tests pass;
- RAW/QUARANTINE paths and downstream domain ownership are approved;
- watcher and pipeline boundaries cannot promote, alert, or publish;
- correction, deactivation, and rollback procedures have named owners.

### Promotion boundary

Successful admission means only that source material entered RAW with required evidence. It does not mean a fire is confirmed, smoke is at the surface, air is unsafe or safe, an advisory exists, a join is valid, a product is scientifically validated, or anything is public. Every later transition belongs to downstream governed stages.

### Correction and deactivation

If source identity, component mapping, bytes, time, geometry, categories, rights, or validation are later found wrong:

1. stop new admissions for the affected configuration;
2. preserve prior immutable bytes, manifests, and receipts;
3. mark affected runs, joins, and downstream dependencies for review;
4. quarantine new or replayed material until the contradiction is resolved;
5. issue correction, notification, and release actions only through their governing surfaces;
6. reactivate only with a new reviewed configuration or SourceDescriptor revision.

Do not rewrite history, silently replace source objects, delete evidence, or publish an all-clear to simulate rollback.

---

## Verification backlog

- [ ] Ratify one canonical HMS connector home and document migration, redirect, and deprecation for other paths.
- [ ] Record the NOAA/HMS path drift or accepted decision in the appropriate governance surface.
- [ ] Replace `OWNER_TBD` with accountable reviewers and NOAA HMS CODEOWNERS coverage.
- [ ] Replace NOAA family greenfield placeholders with reviewed package/runtime decisions or keep them explicitly inactive.
- [ ] Resolve SourceDescriptor schema authority and create approved component-specific descriptors.
- [ ] Add approved HMS entries to the source-authority register before activation.
- [ ] Resolve SmokeContext contract/schema naming and domain ownership.
- [ ] Verify current source endpoints, access, formats/packages, fields/categories, cadence, coverage, time semantics, corrections, terms, attribution, and analyst-augmentation metadata.
- [ ] Implement bounded retrieval, component separation, credential redaction, integrity checks, atomic handoff, and deterministic quarantine.
- [ ] Add no-network fixtures and executable tests for component, role, time, geometry, category, safety, replay, and failure cases.
- [ ] Replace placeholder pipeline/watcher behavior and TODO connector/descriptor gates with meaningful validation before treating them as readiness evidence.
- [ ] Verify RAW captures, downstream pipelines, joins, receipts, proofs, release, correction, API/UI, and official-source redirection independently.

---

## Definition of done

This README update is complete when it accurately preserves the current boundary without claiming implementation. The connector itself is not done until every activation prerequisite and verification item above is resolved through its governing surface.

In all states:

- fire detections and smoke polygons remain distinct components;
- analyst augmentation is preserved as provenance without invented internal details;
- smoke categories remain qualitative and never become PM2.5, AQI, exposure, or health advice;
- fire detections never become ground-confirmed event truth;
- time roles, freshness, corrections, native geometry, uncertainty, and source identity remain intact;
- empty or missing source output never becomes an all-clear;
- connector output stops at RAW or QUARANTINE;
- placement, schema, registry, policy, pipeline, watcher, proof, release, alert, API, and UI authority remain outside this folder.

---

## Changelog

### v0.2 — 2026-07-14

- Reframed the path as a README-only proposed product connector boundary.
- Surfaced the canonical NOAA family lane, underscore compatibility lane, absent nested lane, and greenfield NOAA package state.
- Added evidence-pinned status for descriptors, source activation, pipeline, watcher, RAW lane, contracts, schemas, tests, workflows, and ownership.
- Tightened the fire/smoke component split, analyst-augmentation, qualitative-density, ground-fire, time/freshness, empty-product, and not-life-safety rules.
- Removed version-sensitive live-source claims from the connector contract and moved them into the verification backlog.
- Added fail-closed retrieval, quarantine, no-network testing, replay, correction, activation, deactivation, and rollback requirements.
- Preserved the RAW/QUARANTINE-only lifecycle limit and prohibited alert/publication authority.

### v0.1 — 2026-06-19

- Established the initial NOAA HMS smoke connector-lane documentation.

<p align="right"><a href="#top">Back to top</a></p>
