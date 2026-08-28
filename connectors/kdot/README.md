<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdot-readme
title: connectors/kdot/ — KDOT README-Only Compatibility Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Kansas source steward · Roads/Rail/Trade steward · Settlements/Infrastructure steward · Hazards steward · Rights reviewer · Sensitivity/privacy reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; compatibility-lane; readme-only; noncanonical-path; path-conflict; transportation-source; mixed-source-role; no-network; no-life-safety; no-activation; no-publication
current_path: connectors/kdot/README.md
truth_posture: CONFIRMED current README and bounded absent named conventional implementation/test/descriptor probes, absent proposed Kansas child README, empty source-authority register, conflicted SourceDescriptor schema homes, greenfield rights/sensitivity stubs, and TODO-only generic connector workflows / CONFLICTED final KDOT connector path, compatibility class, child topology, SourceDescriptor/schema/registry authority, product source IDs, and WZDx derivative role / PROPOSED future product-specific adapters and migration / UNKNOWN recursive inventory, runtime, source access, current terms, activation, fixtures, executable tests, substantive CI, lifecycle artifacts, release state, deployment, and owners
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 40deb4a3cab0972f0c7d38930e30c3b497408b0a
  prior_blob: e486ee81775d6547770bdb745c10fd3b8a16b283
  readme_introduction_commit: 1b3bf689452085a78ae1b5e45fb46288b69b7cdf
related:
  - ../README.md
  - ../kansas/README.md
  - ../wzdx/README.md
  - ../../CONTRIBUTING.md
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/README.md
  - ../../docs/sources/catalog/kansas/kdot.md
  - ../../docs/sources/catalog/usdot/wzdx.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../data/registry/sources/README.md
  - ../../control_plane/source_authority_register.yaml
  - ../../policy/rights/README.md
  - ../../policy/sensitivity/README.md
tags: [kfm, connectors, kdot, kansas, transportation, roads, kandrive, kanplan, kansas-gis, work-zones, wzdx, compatibility, readme-only, source-admission, rights, sensitivity, freshness, raw, quarantine, governance]
notes:
  - "At the pinned base, this README is the only directly verified file in connectors/kdot/. Exact conventional probes for pyproject.toml, src/README.md, src/kdot/README.md, tests/README.md, descriptor.yaml, fetch.py, and admit.py returned Not Found; this is not an exhaustive recursive inventory."
  - "The KDOT product page proposes connectors/kansas/kdot/, but the exact target README is absent and the Kansas-family README records final child topology as conflicted. This revision does not ratify either path."
  - "The source-authority register is empty, the populated singular SourceDescriptor schema declares itself legacy while the plural schema is an empty PROPOSED scaffold, and rights/sensitivity READMEs are greenfield stubs."
  - "The generic connector-gate, source-descriptor-validate, docs-build, and link-check workflows are TODO-only echo scaffolds; a green workflow run does not prove KDOT connector behavior."
  - "No live KDOT source, current terms page, credential, source payload, runtime log, deployment, release, or public client was inspected."
  - "Only this Markdown file is in scope. No path, code, descriptor, schema, contract, policy, registry entry, fixture, test, workflow, receipt, lifecycle artifact, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDOT README-Only Compatibility Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Component maturity:** README-only at the directly inspected paths; no supported package, client, parser, admission decision, test lane, or lifecycle handoff is verified here  
> **Path posture:** `connectors/kdot/` exists, but the final KDOT connector path and compatibility class remain `CONFLICTED / NEEDS VERIFICATION`; the proposed `connectors/kansas/kdot/README.md` target is absent at the pinned base  
> **Authority:** compatibility documentation inside the `connectors/` responsibility root; no source, schema, policy, registry, evidence, lifecycle, release, routing, or publication authority

> [!CAUTION]
> KanDrive and other current-condition surfaces are not life-safety, emergency-response, live-traffic-control, or operational-routing authorities. A source page, folder, future parser, map layer, or AI summary must never be treated as current road truth without product-specific descriptors, freshness gates, evidence, policy, review, and release state.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review burden](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Product boundaries](#kdot-product-and-source-role-boundaries) · [Evidence](#evidence-basis) · [Failure contract](#failure-contract) · [Rollback](#rollback) · [Backlog](#verification-backlog) · [Definition of done](#definition-of-done)

---

## Purpose

`connectors/kdot/` currently provides a documentation boundary for an unresolved Kansas Department of Transportation connector placement.

Its present responsibility is to:

- prevent the existing top-level path from being mistaken for an active or canonical adapter;
- preserve the distinction among KDOT product surfaces, source roles, time semantics, rights, sensitivity, and public-safety posture;
- record the gap between the source-profile proposal and current repository evidence;
- define fail-closed preconditions for any future implementation, migration, redirect, or removal;
- keep connector work upstream of evidence closure, normalization, cataloging, release, and public delivery.

This README does not prove that a KDOT connector exists, that `connectors/kdot/` should survive, that `connectors/kansas/kdot/` is an implemented destination, or that any KDOT surface is approved for access or admission.

[Back to top](#top)

---

## Authority level

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility root | **CONFIRMED** | `connectors/` owns source-specific fetch, probe, preservation, and admission mechanics. Connectors remain upstream of canonical truth and publication. |
| Current path | **CONFIRMED** | `connectors/kdot/README.md` exists at the pinned base. |
| Compatibility posture | **CONFIRMED broad class / CONFLICTED exact class** | The path is noncanonical compatibility documentation. Whether it is ultimately `transitional`, `deprecated`, `legacy`, or removed is not settled by an accepted migration decision in the inspected evidence set. |
| Kansas family lane | **CONFIRMED parent / PROVISIONAL child topology** | `connectors/kansas/README.md` exists and coordinates Kansas source products, but its child naming and migration map are explicitly unresolved. |
| Proposed KDOT child | **ABSENT AT NAMED PROBE / PROPOSED BY SOURCE PAGE** | `docs/sources/catalog/kansas/kdot.md` proposes `connectors/kansas/kdot/`; the exact child README was not present at the pinned base. |
| Current implementation | **NOT ESTABLISHED** | The README is directly verified; named conventional package, source-layout, test, descriptor, fetch, and admit paths were absent. Differently named files remain `UNKNOWN`. |
| Source authority and activation | **NOT ESTABLISHED** | The machine source-authority register has `entries: []`; no accepted KDOT surface descriptor or activation decision was verified. |
| SourceDescriptor authority | **CONFLICTED** | The populated singular-path schema declares the plural path canonical and itself legacy, while the plural-path schema is an empty permissive `PROPOSED` scaffold. |
| Rights and sensitivity enforcement | **GREENFIELD STUBS / UNKNOWN** | The directly inspected rights and sensitivity READMEs contain only greenfield stub text; no KDOT-specific executable policy was verified. |
| Connector CI | **TODO-ONLY GENERIC SCAFFOLDS** | The directly inspected connector-gate, descriptor-validation, docs-build, and link-check workflows execute `echo TODO ...`; green completion is not substantive proof. |
| Public output | **NONE AUTHORIZED** | This README creates no source activation, lifecycle object, API response, map layer, traveler guidance, release, or publication artifact. |

Editing this README does not choose the winning path, compatibility class, source IDs, descriptor home, product grouping, or normalization architecture.

[Back to top](#top)

---

## Status

### Bounded repository snapshot

The only file directly verified in this lane at base commit `40deb4a3cab0972f0c7d38930e30c3b497408b0a` is:

```text
connectors/kdot/
└── README.md
```

Exact probes returned `Not Found` for:

```text
connectors/kdot/pyproject.toml
connectors/kdot/src/README.md
connectors/kdot/src/kdot/README.md
connectors/kdot/tests/README.md
connectors/kdot/descriptor.yaml
connectors/kdot/fetch.py
connectors/kdot/admit.py
connectors/kansas/kdot/README.md
```

These are bounded absence statements for named paths at the pinned commit, not a recursive tree receipt. Differently named or unindexed code, tests, fixtures, descriptors, or migration artifacts remain `UNKNOWN`.

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| This README | Existing v0.1 compatibility document before this revision | Documentation existed; it did not prove runtime behavior. |
| Introduction lineage | Commit `1b3bf689452085a78ae1b5e45fb46288b69b7cdf` expanded a blank placeholder into v0.1 | The original blank state is lineage, not the rollback target for this revision. |
| Proposed Kansas child | Exact README absent | Do not redirect implementation there as though the child already exists. |
| KDOT source product page | Present, draft, product-level planning/source profile | Supports product distinctions and open questions; does not activate a connector or settle repository topology. |
| Kansas family README | Present and current enough to record five direct child README lanes plus unresolved compatibility paths | Supports family placement, but explicitly leaves final KDOT child naming and migration unresolved. |
| Source registry/control plane | Registry README present; machine authority register empty | Source-admission doctrine exists; KDOT machine authority is not established. |
| SourceDescriptor schemas | Rich singular schema plus empty plural scaffold | Schema-home and validator authority require resolution before relying on any descriptor. |
| Generic connector workflows | TODO-only echo jobs | Workflow success cannot establish KDOT parsing, admission, rights, sensitivity, freshness, or lifecycle behavior. |

[Back to top](#top)

---

## What belongs here

Until an accepted path and migration decision says otherwise, this lane should contain only:

- this compatibility boundary and links to the current family, source, domain, policy, schema, registry, and release surfaces;
- explicit path-drift, deprecation, redirect, migration, and rollback notes;
- anti-collapse rules for KDOT products and their proposed source roles;
- fail-closed requirements for rights, sensitivity, source identity, time, freshness, geometry/LRS, external IDs, and source-shape drift;
- a narrowly scoped compatibility shim only after ownership, warning behavior, sunset criteria, tests, and rollback are accepted;
- migration receipts or pointer metadata only when their owning governance process authorizes them.

Substantive connector code should not land here merely because the directory exists. A future implementation must first resolve path ownership and then live at the accepted connector home.

## What does NOT belong here

This directory must not contain or imply authority over:

- canonical KDOT connector placement without an accepted ADR or migration decision;
- a live network client, scheduled watcher, endpoint configuration, credential, cookie, token, private URL, or secret by default;
- authoritative SourceDescriptor records, source activation decisions, source-authority entries, contracts, schemas, or policy;
- bulk route, asset, traffic, camera, detector, RWIS, work-zone, permit, planning, or GIS payloads;
- unreviewed upstream examples or fixtures containing sensitive infrastructure, operational detail, private information, or redistribution-restricted material;
- direct public traveler guidance, emergency advice, live traffic control, dispatch, route optimization, or life-safety claims;
- one untyped “KDOT feed” that collapses KanPlan, KanDrive, KDOT GIS, work-zone authorization, direct WZDx feeds, and KFM-normalized derivatives;
- KDOT-to-WZDx normalization logic; normalization is downstream pipeline work with a recorded transform, not source capture;
- direct writes to `data/work/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- EvidenceBundle closure, catalog closure, promotion, correction, withdrawal, rollback, public API behavior, public UI behavior, or AI answers presented as KDOT truth.

Public availability upstream does not equal KFM rights clearance, sensitivity clearance, source admission, evidence closure, or release approval.

[Back to top](#top)

---

## Inputs

### Current

This README consumes repository evidence and KFM doctrine only. The current lane declares no supported runtime input, command, configuration contract, source endpoint, credential variable, fixture shape, descriptor ID, or activation state.

### Future admissible inputs

After path, descriptor, activation, rights, sensitivity, security, and test gates are accepted, a retained KDOT adapter may consume:

- a conforming, reviewed, **product-specific** `SourceDescriptor` reference;
- an explicit activation decision and approved access configuration;
- caller-supplied bytes, files, metadata, or a reviewed transport result;
- source/product/record identity, source-head evidence, retrieval time, run identity, and destination intent;
- source-native route, event, asset, permit, planning-document, layer, feature, and external identifiers;
- source, observed, valid, retrieval, correction, and release times where material;
- geometry, coordinate reference system, linear referencing system, direction, measure, precision, and uncertainty metadata;
- rights, attribution, redistribution, access, disclaimer, sensitivity, and review context;
- synthetic or explicitly rights-cleared no-network fixtures.

Import, installation, documentation rendering, and default tests must remain no-network.

### Product-specific admission boundary

The current product page proposes different roles for distinct surfaces. Those roles are review inputs, not active machine authority:

| Surface | Source-page role proposal | Required boundary before admission |
|---|---|---|
| KanPlan and planning artifacts | `authority` for the specific planning or designation claim | Separate descriptor, artifact identity, validity window, rights review, citation, and scope; a plan is not an observed road condition. |
| KDOT Kansas GIS routes and asset rosters | `authority` for the specific route/asset record | Layer/version/source-head identity, CRS/LRS, precision, redistribution, sensitivity, and asset-class review. |
| KanDrive traveler conditions | `observed` | Observation time, validity/expiry, retrieval time, freshness window, stale-state outcome, source record ID, and not-for-life-safety disclaimer. |
| Work-zone permits or authorizations | `regulatory` | Permit/authorization identity, valid interval, issuer, geometry/LRS, rights, and explicit separation from observed active conditions. |
| Direct WZDx feed | Feed-specific role, `NEEDS VERIFICATION` | Preserve standard identity separately from publisher/feed identity; require feed descriptor and schema-version gate. |
| KFM KDOT-to-WZDx derivative | Product page proposes `aggregate`; final role `NEEDS VERIFICATION` | Preserve upstream KDOT record, WZDx version, mapping version, input/output digests, transform receipt, and derivative identity. |

No agency-level descriptor may silently grant one role, rights posture, cadence, or release class to every KDOT product.

[Back to top](#top)

---

## Outputs

### Current

This directory currently emits no verified response bytes, parsed record, validation result, admission decision, receipt, lifecycle candidate, map artifact, API payload, traveler guidance, or public claim. Its only confirmed output is documentation.

### Future allowed outputs

A retained implementation may return in-memory or caller-owned:

- parsed source-native records that preserve product and upstream identity;
- validation findings and source-shape observations;
- explicit `admit-candidate`, `hold/quarantine-candidate`, `deny`, `abstain`, `no-op`, `rate-limit`, or `error` outcomes;
- proposed RAW, QUARANTINE, or run/probe-receipt envelopes.

Orchestration—not the connector package—must choose persistence. Any path examples remain responsibility-root patterns, not proof of current implementation:

```text
data/raw/<owning-domain>/<surface-source-id>/<run-id>/
data/quarantine/<owning-domain>/<surface-source-id>/<run-id>/
data/receipts/<run-id>/
```

KDOT-to-WZDx normalized artifacts must be produced downstream through governed normalization, validation, proof, catalog, and release stages. A connector may preserve source material needed by that process; it must not emit the derivative as though it were upstream KDOT truth.

[Back to top](#top)

---

## Validation

### Current revision evidence

The documentation boundary is based on:

- pinned reads of this README and its introduction commit;
- exact probes for the conventional package, source-layout, test, descriptor, fetch, admit, and proposed child paths listed above;
- current reads of the connector root, Kansas family README, KDOT product page, WZDx companion surfaces, Directory Rules, contribution guidance, CODEOWNERS, and PR template;
- current reads of the SourceDescriptor standard, contract, both schema paths, source registry README, source-authority register, rights/sensitivity README stubs, and generic connector/documentation workflows.

The named workflow files are scaffolds. Their success cannot be reported as substantive validation.

### Future implementation gates

Before relying on a KDOT adapter, tests and validators must prove at least:

- accepted path and package/import identity, with migration, deprecation, backlinks, and rollback where applicable;
- no network access on import, installation, documentation rendering, or default tests;
- one reviewed descriptor and activation decision per product surface or feed;
- source-role anti-collapse across planning, route/asset authority, observed conditions, regulatory authorizations, direct feeds, and KFM derivatives;
- stable upstream IDs, source-head identity, schema/version pinning, response metadata, external-ID capture, and deterministic digest inputs;
- separate source, observed, valid, retrieval, correction, and release times;
- KanDrive freshness and stale-state handling, including `ABSTAIN` or `DENY` after the stewarded window;
- not-for-life-safety posture in every current-condition candidate and downstream release input;
- geometry/CRS/LRS/direction/measure/precision validation and explicit quarantine for unresolved crosswalks;
- rights, attribution, redistribution, access, sensitivity, security, and asset-class restrictions;
- WZDx standard-versus-feed separation and a transform receipt for any KDOT-to-WZDx derivative;
- no credentials, private URLs, operational secrets, or sensitive real-world payloads in fixtures, logs, snapshots, or examples;
- finite outcomes for malformed, unsupported, stale, rate-limited, denied, no-op, and ambiguous inputs;
- no direct connector write beyond caller-authorized RAW, QUARANTINE, or run/probe-receipt candidates;
- no direct public API, map, AI, release, or publication path.

Negative fixtures are required. A test suite that proves only the happy path is incomplete.

[Back to top](#top)

---

## Review burden

Current CODEOWNERS supplies only the repository-wide fallback `@kfm/maintainers`; no KDOT-specific owner was verified.

Changes to this lane should receive review from the roles affected by the claim:

- connector/package maintainer;
- Kansas source and KDOT product steward;
- Roads/Rail/Trade steward;
- Hazards steward for current-condition, work-zone, and not-for-life-safety behavior;
- Settlements/Infrastructure steward for route and asset rosters;
- rights and attribution reviewer;
- sensitivity/privacy and security reviewers for infrastructure, camera, detector, station, asset, or operational-detail exposure;
- validation/test steward;
- docs steward;
- architecture/migration reviewer when path, package, source-ID, compatibility, or child topology changes;
- WZDx/transport-standard reviewer when a normalization or direct-feed boundary changes.

A README-only clarification does not assign those roles. Owners remain `OWNER_TBD` until repository governance assigns them.

[Back to top](#top)

---

## Related folders

| Surface | Responsibility | Current evidence posture |
|---|---|---|
| [`../README.md`](../README.md) | Connector-root source-admission and lifecycle boundary | **CONFIRMED** |
| [`../kansas/README.md`](../kansas/README.md) | Kansas source-family coordination | **CONFIRMED parent / CONFLICTED child map** |
| `connectors/kansas/kdot/` | Source-page-proposed KDOT child | **Exact README absent / final topology unresolved** |
| [`../wzdx/README.md`](../wzdx/README.md) | WZDx connector-lane documentation | **CONFIRMED README / implementation unverified** |
| [`../../docs/sources/catalog/kansas/kdot.md`](../../docs/sources/catalog/kansas/kdot.md) | Human-facing KDOT product/source profile | **CONFIRMED draft doc / no activation authority** |
| [`../../docs/sources/catalog/usdot/wzdx.md`](../../docs/sources/catalog/usdot/wzdx.md) | WZDx product/standard companion | **CONFIRMED path / current implementation effects unverified** |
| [`../../docs/domains/roads-rail-trade/README.md`](../../docs/domains/roads-rail-trade/README.md) | Primary domain doctrine | **CONFIRMED path** |
| [`../../docs/domains/settlements-infrastructure/README.md`](../../docs/domains/settlements-infrastructure/README.md) | Route/asset adjacency and infrastructure sensitivity | **CONFIRMED path** |
| [`../../docs/domains/hazards/README.md`](../../docs/domains/hazards/README.md) | Current-condition and not-for-life-safety context | **CONFIRMED path** |
| [`../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Descriptor meaning and admission standard | **CONFIRMED draft doctrine / implementation paths bounded** |
| [`../../contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | `SourceDescriptor` semantic contract | **CONFIRMED draft/PROPOSED contract** |
| [`../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Rich populated descriptor schema | **CONFIRMED file / self-declared legacy path / PROPOSED status** |
| [`../../schemas/contracts/v1/sources/source_descriptor.schema.json`](../../schemas/contracts/v1/sources/source_descriptor.schema.json) | Schema-declared canonical plural path | **CONFIRMED empty PROPOSED scaffold** |
| [`../../data/registry/sources/README.md`](../../data/registry/sources/README.md) | Source-registry doctrine and proposed instance home | **CONFIRMED README / implementation conflict and drift remain** |
| [`../../control_plane/source_authority_register.yaml`](../../control_plane/source_authority_register.yaml) | Machine source-authority register | **CONFIRMED `entries: []` at pinned base** |
| [`../../policy/rights/README.md`](../../policy/rights/README.md) | Rights policy boundary | **CONFIRMED greenfield stub** |
| [`../../policy/sensitivity/README.md`](../../policy/sensitivity/README.md) | Sensitivity policy boundary | **CONFIRMED greenfield stub** |
| `release/` and `data/published/` | Release decisions and released artifacts | **Outside connector authority** |

[Back to top](#top)

---

## ADRs

No accepted KDOT-specific placement ADR was verified in the inspected evidence set.

`OPEN-KDOT-01` in the KDOT product page records the top-level-versus-Kansas-child question; it is an open item, not an accepted architectural decision.

This README-only revision:

- creates, moves, renames, or deletes no path;
- does not change canonical root, schema-home, lifecycle, source-ledger, policy, release, or proof authority;
- does not ratify a compatibility class or future child layout.

A future decision that moves, removes, redirects, or operationalizes this lane must follow Directory Rules migration discipline. If it changes package identity, source IDs, product grouping, schema/registry authority, or cross-component behavior, it requires an accepted ADR or an explicitly governed migration plan with history, backlinks, compatibility behavior, deprecation, tests, and rollback.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**

Evidence snapshot:

- repository: `bartytime4life/Kansas-Frontier-Matrix`;
- base ref: `main`;
- base commit: `40deb4a3cab0972f0c7d38930e30c3b497408b0a`;
- prior README blob: `e486ee81775d6547770bdb745c10fd3b8a16b283`;
- README introduction commit: `1b3bf689452085a78ae1b5e45fb46288b69b7cdf`.

This review covers the exact files and probes named in this document. It does not establish a complete recursive connector inventory, current external-source state, runtime behavior, or deployment state.

[Back to top](#top)

---

## KDOT product and source-role boundaries

The durable anti-collapse rule is **one product or feed, one governed identity and admission posture**.

1. KDOT as an institution is not a single source role.
2. A route designation or asset roster may be authoritative for the exact administrative fact it represents; it is not automatically evidence of current condition.
3. A KanDrive condition report is an observation with freshness limits; it is not a route-designation authority, emergency warning, or routing instruction.
4. A permit or authorization is regulatory; it does not prove that a work zone is currently active or that a lane is physically blocked.
5. WZDx is a standard, not a publisher. A direct feed requires feed-specific identity and review.
6. A KFM WZDx-aligned artifact is a derivative. It must preserve upstream identity and a transform receipt; it must not masquerade as the original KDOT record.
7. Planning artifacts, observed conditions, administrative geometry, regulatory records, normalized derivatives, maps, tiles, summaries, joins, dashboards, and AI explanations remain distinct carriers.
8. Public release is a governed state transition outside this folder.

Where the source page proposes a role but no accepted descriptor exists, the role remains `PROPOSED / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Evidence basis

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| `connectors/kdot/README.md` at the pinned base | **CONFIRMED** | Existing v0.1 compatibility document and prior blob. | Runtime, tests, source access, activation, or canonicality. |
| README introduction commit `1b3bf689...` | **CONFIRMED** | The v0.1 README replaced a blank placeholder. | That its June claims remain current. |
| Exact named probes under `connectors/kdot/` | **CONFIRMED bounded absences** | Conventional package/test/descriptor/fetch/admit paths were not present. | Exhaustive directory absence or differently named files. |
| [`connectors/kansas/README.md`](../kansas/README.md) | **CONFIRMED** | Kansas family parent exists, five direct child README lanes are named, KDOT compatibility path is recorded, and final child topology is conflicted. | KDOT child runtime or accepted migration. |
| Exact `connectors/kansas/kdot/README.md` probe | **CONFIRMED absent at base** | The proposed destination README did not exist at the pinned commit. | Permanent nonexistence or final path decision. |
| [`docs/sources/catalog/kansas/kdot.md`](../../docs/sources/catalog/kansas/kdot.md) | **CONFIRMED draft source page** | Product surfaces, proposed role distinctions, freshness and not-for-life-safety posture, path proposal, and open questions. | Accepted descriptors, current endpoints/terms, source activation, runtime, or release. |
| SourceDescriptor standard, contract, and both schema paths | **CONFIRMED files / CONFLICTED authority** | Rich descriptor expectations and current schema-home inconsistency. | A valid KDOT descriptor or working validator. |
| Source-authority register | **CONFIRMED empty** | No machine source-authority entries at the pinned base. | Absence of every possible draft descriptor elsewhere. |
| Rights and sensitivity READMEs | **CONFIRMED stubs** | Policy roots exist. | Executable KDOT-specific decisions or cleared terms. |
| Generic connector/documentation workflows | **CONFIRMED TODO-only** | Workflow names and trigger scaffolds exist. | Substantive tests, parser behavior, descriptor validation, link validation, or connector safety. |
| Directory Rules, CONTRIBUTING, CODEOWNERS, PR template | **CONFIRMED** | Placement, lifecycle, smallest reversible change, review fallback, and PR discipline. | Branch protection, required-check enforcement, or steward availability. |

No external source endpoint or current KDOT terms page was used as implementation evidence for this revision.

[Back to top](#top)

---

## Failure contract

Any future KDOT adapter must fail closed.

| Condition | Required outcome |
|---|---|
| No accepted path/package decision | `DENY` implementation expansion in this lane or hold for migration review |
| Missing or unresolved product-specific descriptor/activation | `DENY` source access or `ABSTAIN` |
| Unknown rights, attribution, redistribution, or access terms | `HOLD / QUARANTINE` or `DENY` |
| Unresolved sensitivity, infrastructure exposure, or operational-detail risk | `HOLD / QUARANTINE` or `DENY` |
| Unknown product/surface/source role | `ABSTAIN` or `QUARANTINE`; never infer from agency name |
| Missing route/event/asset/permit/external identity | `QUARANTINE` |
| Unsupported or drifting schema/version | `QUARANTINE` or `ERROR`; preserve source response and reason |
| Missing CRS/LRS/direction/measure/precision context | `QUARANTINE` |
| Missing observed/valid/retrieval time or freshness posture | `ABSTAIN` or `QUARANTINE` |
| KanDrive candidate beyond its stewarded freshness window | `ABSTAIN` or `DENY` downstream current-condition use |
| Work-zone permit treated as observed closure | `DENY` source-role collapse |
| WZDx standard treated as feed publisher | `DENY` standard/feed collapse |
| KFM derivative treated as original KDOT record | `DENY` derivative/source collapse |
| Rate limit, authentication failure, timeout, or partial response | Explicit `rate-limit`, `error`, or `hold`; no silent partial success |
| Any connector attempt to publish or select a release state | `DENY` and emit an auditable failure candidate |

Errors must preserve stable reason codes, source/run identity where safe, and enough non-sensitive context for review. They must not log credentials, private URLs, restricted payloads, or sensitive infrastructure detail.

[Back to top](#top)

---

## Rollback

Before merge, close the review PR and abandon the scoped branch.

After merge, create a transparent revert of the documentation commit and restore prior blob:

```text
base commit: 40deb4a3cab0972f0c7d38930e30c3b497408b0a
prior README blob: e486ee81775d6547770bdb745c10fd3b8a16b283
```

Do not rewrite shared history.

Rollback is required if this README is used to justify source activation, canonical child status, implementation in the unresolved path, source-role collapse, bypass of freshness/rights/sensitivity gates, life-safety or routing use, WZDx derivative/source collapse, or direct writes beyond the connector boundary.

[Back to top](#top)

---

## Verification backlog

| Item | Evidence that would settle it | Status |
|---|---|---:|
| Complete recursive inventory of `connectors/kdot/` and related aliases | Commit-pinned tree receipt or mounted checkout | **NEEDS VERIFICATION** |
| Final connector path and compatibility class | Accepted ADR or migration decision | **CONFLICTED / OPEN** |
| KDOT child and sub-surface topology | Accepted path decision covering single adapter versus per-surface children | **OPEN** |
| Distribution, import package, supported runtime, dependencies, and command surface | Package metadata, code, install/build proof, tests | **UNKNOWN** |
| Product-specific source IDs and descriptors | Validated registry instances plus source-authority entries | **NEEDS VERIFICATION** |
| SourceDescriptor schema/validator authority | Accepted schema-home resolution, validator wiring, fixtures, CI | **CONFLICTED** |
| Current KanPlan, KanDrive, KDOT GIS, work-zone, ITS, camera, detector, and RWIS access methods | Source steward review and current official source documentation | **NEEDS VERIFICATION** |
| Current terms, attribution, redistribution, commercial-use, and credential posture per surface | Rights review with dated evidence | **NEEDS VERIFICATION** |
| Infrastructure, asset, operational-detail, privacy, and public-safety sensitivity posture | Sensitivity/security review and executable policy | **NEEDS VERIFICATION** |
| KanDrive protocol, schema, cadence, freshness window, and supersession behavior | Current source documentation plus observed safe fixture/run evidence | **NEEDS VERIFICATION** |
| KDOT route/asset CRS and LRS versions, measures, direction, and crosswalks | KDOT GIS/LRS documentation, fixtures, validators | **NEEDS VERIFICATION** |
| Work-zone permit versus observed-condition mapping | Product-specific contracts, fixtures, and anti-collapse tests | **NEEDS VERIFICATION** |
| Direct KDOT WZDx participation versus KFM normalization | Feed/source review and accepted mapping decision | **NEEDS VERIFICATION** |
| KDOT-to-WZDx mapping and derivative role | Mapping contract, WZDx version pin, TransformReceipt schema, tests | **NEEDS VERIFICATION** |
| No-network fixture strategy | Rights-cleared synthetic fixtures and test documentation | **UNKNOWN** |
| Executable tests and substantive CI discovery | Test files, commands, workflow steps, and logs | **UNKNOWN** |
| RAW/QUARANTINE/run-receipt candidate envelope contract | Contracts, schemas, fixtures, validators, and tests | **UNKNOWN** |
| Owner and reviewer assignments | CODEOWNERS or accepted governance assignment | **UNKNOWN** |
| Downstream evidence, catalog, API, map, correction, release, and rollback consumers | Repo files, emitted artifacts, tests, logs, and release records | **UNKNOWN** |

[Back to top](#top)

---

## Definition of done

This compatibility boundary is ready to graduate only when:

- [ ] one final KDOT connector path and compatibility disposition are accepted;
- [ ] migration preserves history, links, source IDs, package/import identity, fixtures, receipts, deprecation state, and rollback;
- [ ] the retained package or lane has a supported build/import/command contract;
- [ ] every KDOT surface or feed has a conforming product-specific descriptor and explicit activation decision;
- [ ] SourceDescriptor schema, validator, registry, and CI authority are resolved;
- [ ] current access methods, terms, attribution, redistribution, cadence, schema, source-head, and correction behavior are verified;
- [ ] rights, sensitivity, security, infrastructure-exposure, and not-for-life-safety policies are executable and tested;
- [ ] no-network valid and invalid fixtures cover each product boundary;
- [ ] tests prove product/source-role anti-collapse, stale-state behavior, CRS/LRS handling, external-ID preservation, finite failures, and connector non-publication;
- [ ] KDOT-to-WZDx normalization is downstream, versioned, receipt-bearing, and does not replace upstream records;
- [ ] outputs are bounded to caller-authorized RAW, QUARANTINE, or run/probe-receipt candidates;
- [ ] no connector code creates evidence closure, catalog/triplet authority, release state, public map/API behavior, routing advice, or life-safety claims;
- [ ] owners and required reviewers are assigned;
- [ ] substantive CI commands and observed passing/failing cases exist;
- [ ] rollback is exercised without history rewrite or lineage loss.

Until then, the safe state is documentation-only, no-network, no-activation, and no-publication.

[Back to top](#top)
