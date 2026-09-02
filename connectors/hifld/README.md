<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-hifld-readme
title: connectors/hifld/ — HIFLD Connector Coordination Lane
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Infrastructure steward · Hazards steward · Settlements/Infrastructure steward · Roads/Rail/Trade steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-11
policy_label: restricted-doctrine; infrastructure-sensitivity-gated; rights-gated; no-publication
related:
  - ../README.md
  - ../../docs/sources/catalog/hifld/README.md
  - ../../docs/sources/catalog/hifld/hifld.md
  - ../../docs/sources/catalog/README.md
  - ../../docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../docs/domains/settlements-infrastructure/SOURCE_REGISTRY.md
  - ../../docs/domains/roads-rail-trade/SOURCE_REGISTRY.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../data/raw/infrastructure/
  - ../../data/quarantine/infrastructure/
  - ../../data/raw/hazards/
  - ../../data/quarantine/hazards/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, hifld, infrastructure, critical-infrastructure, source-admission, sensitivity, rights, raw, quarantine, governance]
notes:
  - "This README documents a HIFLD connector coordination and compatibility lane, not an implemented or activated canonical source family."
  - "At the inspected base commit, connectors/hifld/ contains only README.md."
  - "HIFLD remains beyond the canonical source-family list described by the current source-family documentation; promotion is ADR-class and NEEDS VERIFICATION."
  - "HIFLD-derived material is infrastructure-sensitive and may enter RAW or QUARANTINE handoff only after descriptor, rights, sensitivity, and activation review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HIFLD Connector Coordination Lane

> Documentation and compatibility boundary for proposed Homeland Infrastructure Foundation-Level Data source admission.

> [!IMPORTANT]
> **Document lifecycle:** draft  
> **Component maturity:** experimental documentation scaffold  
> **Owner:** `OWNER_TBD`  
> **Truth posture:** the path and current one-file inventory are confirmed at base commit `3d2e2ff`; connector implementation, SourceDescriptor activation, tests, CI, source access, and emitted artifacts remain unverified.  
> **Sensitivity posture:** critical-infrastructure material is restricted and deny-by-default until policy and release review explicitly allow a public-safe form.

`connectors/hifld/`

## Quick navigation

- [Scope](#scope)
- [Repository fit](#repository-fit)
- [Confirmed current state](#confirmed-current-state)
- [Canonicality and compatibility status](#canonicality-and-compatibility-status)
- [Authority boundary](#authority-boundary)
- [Accepted inputs](#accepted-inputs)
- [Sensitive infrastructure posture](#sensitive-infrastructure-posture)
- [Lifecycle handoff](#lifecycle-handoff)
- [Proposed connector contract](#proposed-connector-contract)
- [Testing and fixture expectations](#testing-and-fixture-expectations)
- [Definition of done](#definition-of-done)
- [Verification backlog](#verification-backlog)
- [Rollback](#rollback)

---

## Scope

`connectors/hifld/` is reserved for documentation, compatibility routing, and any future source-specific fetch or admission behavior for HIFLD products when that behavior is explicitly approved.

A future implementation may:

- contact steward-approved HIFLD distribution surfaces when explicitly enabled;
- retrieve bounded, product-scoped infrastructure source material;
- preserve publisher, product, release, vintage, geometry, identifier, rights, and sensitivity metadata;
- prepare source-faithful material for RAW admission;
- route rights-unclear, location-sensitive, malformed, incomplete, stale, drifted, or canonicality-unclear material toward QUARANTINE;
- emit finite connector outcomes and source-drift signals;
- support deterministic no-network tests using synthetic, minimized, redacted, or generalized fixtures.

This lane must not become:

- HIFLD or infrastructure truth;
- a canonical SourceDescriptor home;
- schema, contract, or policy authority;
- a processed domain pipeline;
- a catalog, triplet, proof, receipt, release, or publication authority;
- a direct UI, MapLibre, tile, graph, search, or AI-answer source;
- a route for exposing precise sensitive infrastructure locations.

---

## Repository fit

Directory Rules place source-specific fetchers and admitters under `connectors/`. HIFLD is a cross-domain source family candidate, not a new repository responsibility root.

```text
connectors/
└── hifld/
    └── README.md               # this file; current confirmed inventory
```

Related responsibility homes:

```text
docs/sources/catalog/hifld/          # source-family and product documentation
data/registry/sources/               # canonical SourceDescriptor and activation state
data/raw/infrastructure/             # possible source-faithful admission target
data/quarantine/infrastructure/      # unresolved infrastructure material
data/raw/hazards/                    # possible source-faithful hazards admission target
data/quarantine/hazards/             # unresolved hazards material
schemas/contracts/v1/source/         # source/admission machine shapes
policy/sensitivity/                  # sensitivity decisions and transforms
policy/rights/                       # rights and use-condition decisions
pipelines/                           # downstream normalization and domain processing
release/                             # release, correction, withdrawal, and rollback decisions
```

HIFLD products may support hazards, settlements/infrastructure, roads/rail/trade, energy, communications, water, emergency services, and other lanes. Cross-domain usefulness does not make this connector a domain authority.

---

## Confirmed current state

At base commit `3d2e2ffdd514ad6d74e74dddcb32d7257704c033`:

| Item | Status | Evidence boundary |
|---|---:|---|
| `connectors/hifld/README.md` | **CONFIRMED** | The file exists in the repository. |
| Additional files under `connectors/hifld/` | **UNKNOWN / not observed** | Repository search returned only this README for the connector lane. Absence is bounded to the inspected search and ref. |
| HIFLD family documentation | **CONFIRMED** | `docs/sources/catalog/hifld/README.md` exists. |
| HIFLD product-page documentation | **CONFIRMED** | `docs/sources/catalog/hifld/hifld.md` exists. |
| Canonical HIFLD SourceDescriptor | **NEEDS VERIFICATION** | Must be confirmed in `data/registry/sources/`. |
| Connector implementation or package wiring | **UNKNOWN** | No fetcher, parser, admission module, package metadata, or tests were verified here. |
| Live-source activation | **UNKNOWN** | No activation decision, credential path, endpoint configuration, receipt, or runtime evidence was inspected. |
| CI coverage | **UNKNOWN** | No workflow run or check result was inspected for this lane. |

The source-family documentation identifies HIFLD as a proposed family beyond the currently enumerated canonical source-family list and says promotion is ADR-class. That documentation supports a compatibility-scaffold posture; it does not prove active connector implementation or publication authority.

---

## Canonicality and compatibility status

HIFLD’s repository presence must not be mistaken for canonical source-family promotion.

| Concern | Required posture |
|---|---|
| Connector directory exists | **CONFIRMED**, but existence does not establish canonicality. |
| Source-family documentation exists | **CONFIRMED draft documentation**. |
| Canonical source-family status | **NEEDS VERIFICATION / ADR-pending** according to the current family documentation. |
| SourceDescriptor presence | **NEEDS VERIFICATION**. |
| Source activation | **UNKNOWN**. |
| Public release eligibility | **DENY by default** until rights, sensitivity, evidence, review, and release state are satisfied. |

Acceptable future resolutions include:

1. **Canonical promotion:** an ADR explicitly admits HIFLD as a governed source family and defines descriptor, ownership, sensitivity, and compatibility rules.
2. **Compatibility connector:** this lane routes approved HIFLD products through an existing canonical source or local-upload admission path without creating parallel source authority.
3. **Documentation-only scaffold:** implementation remains elsewhere or deferred, and this folder continues to document boundaries only.
4. **Retirement or migration:** the lane is replaced by a reviewed successor path with a migration note and rollback plan.

Do not infer which resolution applies until repository evidence confirms it.

---

## Authority boundary

```text
THIS LANE MAY EVENTUALLY:
  fetch approved HIFLD product material
  preserve product, publisher, release, vintage, rights, and sensitivity metadata
  prepare RAW admission candidates
  route unresolved material to QUARANTINE
  emit finite connector failures and source-drift signals
  support connector-local tests

THIS LANE MUST NOT:
  establish canonical HIFLD source-family status
  define SourceDescriptor identity, role, rights, or activation state
  declare infrastructure claims true
  expose precise sensitive infrastructure locations
  write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release stores
  create public maps, tiles, reports, dashboards, exports, or AI answers
  bypass evidence, policy, review, correction, or rollback gates
```

The trust membrane remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A successful retrieval is not validation, EvidenceBundle closure, policy approval, release, or publication.

---

## Accepted inputs

Material belongs here only when it supports HIFLD connector coordination or an approved implementation.

| Accepted item | Required posture |
|---|---|
| Connector documentation | State current evidence boundaries and avoid implementation overclaiming. |
| Compatibility mapping | Explain how HIFLD relates to canonical source and lifecycle paths without creating parallel authority. |
| Fetch or parser code | Product-scoped, bounded, no-network by default, and gated by descriptor and policy review. |
| Admission helpers | Produce RAW or QUARANTINE candidates only. |
| Connector-local fixtures | Synthetic, minimized, redacted, generalized, or explicitly approved. |
| Connector-local tests | Verify source-edge behavior only; do not claim downstream truth or release readiness. |
| Source-drift notes | Candidate review evidence only; not automatic schema or policy changes. |

Canonical descriptors, schemas, policy decisions, release records, catalogs, proofs, receipts, and published artifacts belong in their owning roots.

---

## Sensitive infrastructure posture

> [!CAUTION]
> HIFLD products may contain critical-infrastructure locations or attributes whose unrestricted precision could create security, safety, sovereignty, contractual, or policy risk. Source availability does not establish public-release eligibility.

Default controls:

- preserve the source’s original product and sensitivity context;
- minimize collection to the approved product, geography, attributes, and time range;
- do not commit credentials, private URLs, restricted payloads, or uncontrolled bulk extracts;
- do not place precise sensitive locations into fixtures, logs, screenshots, examples, or pull-request text;
- route unresolved sensitivity or rights posture to QUARANTINE, `DENY`, or `ABSTAIN`;
- require downstream policy decisions before redaction, aggregation, displacement, generalization, staged access, or release;
- record transformations and reasons so public-safe artifacts remain auditable and reversible;
- never treat a lower-resolution map or tile as proof that the underlying data is safe to disclose.

Examples of potentially sensitive classes include energy facilities, communications infrastructure, water and wastewater control assets, emergency-service facilities, transportation control points, and other operational infrastructure. Exact class handling remains policy-specific and **NEEDS VERIFICATION**.

---

## Lifecycle handoff

| Stage | Connector-lane responsibility |
|---|---|
| Pre-RAW / source contact | Verify source-family route, SourceDescriptor, activation state, product scope, rights, sensitivity, network permission, and bounded request parameters. |
| RAW | Preserve source-faithful payloads or references with retrieval metadata and digest support. |
| QUARANTINE | Hold canonicality-unclear, rights-unclear, sensitive, malformed, incomplete, stale, drifted, or unsupported material. |
| WORK | Downstream responsibility; may consume admitted material through explicit governed interfaces. |
| PROCESSED | Domain pipeline responsibility, not connector authority. |
| CATALOG / TRIPLET | Downstream catalog and projection responsibility. |
| PUBLISHED | Governed release only; outside this connector lane. |
| CORRECTION / WITHDRAWAL / ROLLBACK | Release and governance responsibility. |

Proposed finite outcomes, subject to contract verification:

- `ADMIT_RAW`
- `QUARANTINE`
- `ABSTAIN`
- `DENY`
- `ERROR`

These names are **PROPOSED** until matched to accepted repository contracts.

---

## Proposed connector contract

The following structure is illustrative and not a claim about current files:

```text
connectors/hifld/
├── README.md
├── src/
│   └── hifld/
│       ├── README.md
│       ├── fetch.py
│       ├── parse.py
│       ├── admit.py
│       ├── sensitivity.py
│       └── errors.py
└── tests/
    └── README.md
```

Before creating any of these paths, confirm that they do not duplicate an existing shared connector package, sensitivity transformer, source registry, schema, policy, or test authority.

| Concern | Proposed requirement |
|---|---|
| Fetch | Product-scoped requests, explicit geography and attributes, timeout, user agent, rate-limit handling, bounded retries, and no hidden pagination. |
| Parse | Preserve source identifiers, geometry, units, vintage, nulls, qualifiers, uncertainty, and product metadata without asserting truth. |
| Admit | Emit RAW or QUARANTINE candidates only. |
| Sensitivity | Carry sensitivity signals forward; do not decide public precision inside connector code. |
| Provenance | Record SourceDescriptor reference, retrieval time, request fingerprint, response digest, product/release identifier, and connector version where supported. |
| Errors | Return finite, actionable outcomes without secrets, precise sensitive data, or excessive source payload content. |
| Network | Disabled or mocked by default in tests and dry runs. |
| Writes | No direct writes outside approved RAW or QUARANTINE handoff interfaces. |

---

## Testing and fixture expectations

Connector-local tests, when implemented, should cover:

- no-network default behavior;
- missing or inactive SourceDescriptor;
- canonicality unresolved;
- product allowlist and geography limits;
- rights or use-condition uncertainty;
- sensitive-attribute and sensitive-location handling;
- valid, empty, malformed, partial, oversized, stale, and changed-schema payloads;
- bounded timeout, retry, pagination, forbidden, and rate-limit behavior;
- preservation of identifiers, geometry, vintage, source role, rights, and sensitivity metadata;
- RAW versus QUARANTINE admission outcomes;
- prohibition on later-lifecycle and release writes;
- safe logging and error redaction.

Fixture rules:

1. Prefer synthetic fixtures.
2. Minimize field count and geographic precision.
3. Generalize or redact sensitive infrastructure details.
4. Record fixture provenance and whether it is synthetic, minimized, redacted, generalized, or copied with approval.
5. Store shared fixtures in the governed fixture authority rather than duplicating them here.
6. Never auto-refresh committed fixtures from live HIFLD sources.

The exact test runner and commands remain **NEEDS VERIFICATION**. Do not present `pytest`, `uv`, `tox`, `nox`, or other commands as confirmed until repository configuration supports them.

---

## Definition of done

This lane is ready for implementation review when:

- [ ] Canonicality or compatibility status is resolved and documented.
- [ ] Owners are assigned.
- [ ] Canonical SourceDescriptor home, source ID, role, rights, cadence, product scope, and activation state are verified.
- [ ] Cross-domain consumers and responsibility boundaries are documented.
- [ ] Live access is explicit, bounded, and disabled by default in tests.
- [ ] RAW and QUARANTINE handoff contracts are verified.
- [ ] Sensitive infrastructure cannot be published directly from connector code.
- [ ] Redaction, generalization, staged-access, and release decisions remain downstream policy responsibilities.
- [ ] Tests cover network, drift, rights, sensitivity, canonicality, and lifecycle boundaries.
- [ ] No credentials, restricted payloads, or precise sensitive fixture data are committed.
- [ ] Validation and rollback evidence are recorded.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm complete child inventory under `connectors/hifld/`. | **NEEDS VERIFICATION** | Non-truncated repository tree at the current ref. |
| Resolve canonical versus compatibility status. | **NEEDS VERIFICATION** | ADR, migration note, or governing repository decision. |
| Confirm HIFLD SourceDescriptor and stable source ID. | **NEEDS VERIFICATION** | `data/registry/sources/` records and schema validation. |
| Confirm source role, rights, cadence, and product allowlist. | **NEEDS VERIFICATION** | Reviewed descriptors and source-steward decision. |
| Confirm approved access method and endpoint configuration. | **NEEDS VERIFICATION** | Connector configuration and activation record. |
| Confirm exact RAW and QUARANTINE targets. | **NEEDS VERIFICATION** | Intake contracts and lifecycle configuration. |
| Confirm sensitivity classification and transforms. | **NEEDS VERIFICATION** | Policy rules, tests, review records, and transformation receipts. |
| Confirm cross-domain landing ownership. | **NEEDS VERIFICATION** | Hazards, settlements/infrastructure, roads/rail/trade, and other domain contracts. |
| Confirm package manager, import path, test runner, and CI. | **UNKNOWN** | Package metadata and workflows. |
| Confirm correction, withdrawal, and rollback paths for released derivatives. | **NEEDS VERIFICATION** | Release and correction artifacts. |

---

## Rollback

Before merge, rollback means closing the draft pull request and abandoning the scoped branch.

After merge, create a transparent revert of the implementation commit and re-run applicable documentation validation. Do not rewrite shared history.

Rollback is required if this README is used to justify:

- canonical-family promotion without an ADR;
- source activation without descriptor, rights, sensitivity, and steward review;
- direct publication from connector output;
- precise sensitive infrastructure exposure;
- bypass of evidence, policy, validation, release, correction, or rollback controls.

---

## Maintainer note

Keep this lane narrow, evidence-bound, and fail-closed. HIFLD can be valuable across multiple KFM domains, but breadth of coverage increases rather than reduces the need for explicit source identity, product scope, rights, sensitivity, temporal context, validation, review, and reversible release controls.
