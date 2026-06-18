<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-openfema-readme
title: connectors/fema-openfema/ — OpenFEMA Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Hazards steward · Settlements/Infrastructure steward · Sensitivity reviewer · Data steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-administrative; per-table-review-required; not-for-life-safety
proposed_path: connectors/fema-openfema/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/sources/catalog/fema/README.md
  - ../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../docs/sources/catalog/fema/openfema-auxiliary-tables.md
  - ../../docs/sources/catalog/fema/nfip-claim-policy-aggregates.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../data/registry/sources/
  - ../../data/raw/hazards/
  - ../../data/quarantine/hazards/
  - ../../data/raw/settlements-infrastructure/
  - ../../data/quarantine/settlements-infrastructure/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, fema, openfema, disaster-declarations, administrative, aggregate, hazards, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-lane contract for OpenFEMA source admission."
  - "Visible FEMA source-catalog docs reference connectors/fema/ as the family connector location; connectors/fema-openfema/ canonicality is NEEDS VERIFICATION until resolved by repo tree review or ADR."
  - "OpenFEMA datasets are mixed administrative and aggregate tables; each table requires its own SourceDescriptor and admission decision."
  - "OpenFEMA administrative records are not observed events, forecasts, warnings, or life-safety guidance."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, policy, review, release, and rollback remain outside this folder."
  - "Specific tables, endpoints, pagination behavior, descriptors, tests, fixtures, CI wiring, terms, sensitivity tiers, and activation state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# OpenFEMA Connector

> Source-specific intake and admission lane for OpenFEMA administrative and aggregate datasets used by KFM Hazards, Settlements/Infrastructure, Hydrology-adjacent, and exposure-context workflows.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Admission: per table" src="https://img.shields.io/badge/admission-per__table-orange">
  <img alt="Life safety: not guidance" src="https://img.shields.io/badge/life__safety-not__guidance-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fema-openfema/`

## Quick jumps

[Scope](#scope) · [Canonicality warning](#canonicality-warning) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Per-table admission posture](#per-table-admission-posture) · [Administrative and life-safety boundary](#administrative-and-life-safety-boundary) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fema-openfema/` is the connector lane for OpenFEMA source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, pagination helpers, and tests for OpenFEMA datasets.

It must not become hazard truth, observed-event truth, emergency-alert authority, damage-assessment authority, benefit-eligibility authority, source-family authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/fema-openfema/`  
> **Truth posture:** README path is CONFIRMED. Connector implementation, canonical path, table coverage, source activation, endpoint coverage, pagination behavior, tests, fixtures, policy enforcement, and CI wiring remain `NEEDS VERIFICATION`.

---

## Canonicality warning

Visible FEMA source-catalog docs point to `connectors/fema/` as the FEMA family connector location. This README lives at `connectors/fema-openfema/`.

Treat this path as **NEEDS VERIFICATION** until one of these is confirmed:

1. `connectors/fema-openfema/` is the accepted source-specific OpenFEMA connector home;
2. `connectors/fema/` is the canonical FEMA family connector home and this folder is a compatibility path;
3. the repo needs a migration note or ADR to resolve the split;
4. this folder should be folded into a different FEMA source-family structure.

Do not create additional FEMA connector paths without checking Directory Rules, existing source catalog references, source descriptors, and any ADR or migration note.

---

## Repo fit

```text
connectors/
└── fema-openfema/
    └── README.md
```

Known related paths:

```text
docs/sources/catalog/fema/README.md                         # FEMA source-family catalog entry
docs/sources/catalog/fema/openfema-disaster-declarations.md  # disaster declaration product page
docs/sources/catalog/fema/openfema-auxiliary-tables.md       # multi-table OpenFEMA product page
docs/sources/catalog/fema/nfip-claim-policy-aggregates.md    # NFIP aggregate product page, if present
connectors/fema/                                             # referenced by visible FEMA source-catalog metadata; NEEDS VERIFICATION
connectors/fema-openfema/                                    # this connector lane
```

Related responsibility roots:

```text
connectors/                                      # source-specific fetch and admission code
docs/domains/hazards/                            # hazards domain doctrine
docs/domains/settlements-infrastructure/         # exposure and infrastructure domain doctrine
data/registry/sources/                           # source descriptors and activation state
data/raw/hazards/                                # raw staged hazards source outputs, if admitted
data/quarantine/hazards/                         # held hazards material requiring review
data/raw/settlements-infrastructure/             # raw staged exposure/infrastructure outputs, if admitted
data/quarantine/settlements-infrastructure/      # held exposure/infrastructure material requiring review
data/receipts/                                   # process and validation receipts
data/proofs/                                     # EvidenceBundles and proof packs
policy/sensitivity/                              # sensitivity and release rules
release/                                         # release decisions and rollback/correction state
```

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/<domain>/
  data/quarantine/<domain>/

NOT HERE:
  observed hazard event truth
  emergency warning or alerting
  eligibility or benefit determination
  damage assessment truth
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, or stage OpenFEMA source material. It does not decide whether an event happened on the ground, whether a person or property is eligible for aid, whether a location is safe, or whether a record is publishable.

---

## Inputs

Potential input classes include:

- source descriptor references;
- steward-approved OpenFEMA dataset identifiers;
- API query parameters approved for each table;
- pagination and freshness metadata;
- disaster declaration numbers and incident metadata;
- administrative program, grant, project, registration, or aggregate fields;
- geography and temporal fields carried by the source;
- per-table sensitivity and rights metadata;
- test fixtures that preserve source shape without exposing restricted details.

All live access and table admission behavior is **NEEDS VERIFICATION** until source terms, per-table source role, sensitivity tier, freshness cadence, and record identity rules are reviewed.

---

## Exclusions

Do not place these in `connectors/fema-openfema/`:

| Excluded material | Correct handling |
|---|---|
| SourceDescriptor authority records | `data/registry/sources/` or accepted source registry home. |
| Machine-checkable schemas | `schemas/contracts/v1/...` under accepted schema-home convention. |
| Policy decisions or release rules | `policy/` and release review surfaces. |
| Processed hazard, settlement, infrastructure, hydrology, or exposure records | Downstream lifecycle roots only. |
| Published maps, tiles, catalogs, dashboards, or public claims | Release and publication roots only. |
| Emergency, eligibility, benefit, legal, or life-safety determination text | Out of scope; redirect to official channels and reviewed public guidance. |
| Large source payloads or bulk extracts | Store only through approved RAW/QUARANTINE lifecycle paths with receipts. |
| Generated summaries used as evidence | Not allowed; EvidenceBundle-backed claims only. |

---

## Per-table admission posture

OpenFEMA is not a single uniform source product. It is a family of tables with mixed source roles and sensitivity posture.

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no umbrella admission for every OpenFEMA table;
- no implicit publication from retrieved administrative records;
- no conversion of administrative records into observed hazard events;
- no assumption that aggregate records can support household-level or site-specific conclusions;
- no assumption that every table is T0/open without sensitivity review;
- unclear source role, aggregation unit, sensitivity tier, rights, or table shape routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Table has no admission decision | `NEEDS_VERIFICATION`; no live activation. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Pagination incomplete | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Table schema drift detected | `NEEDS_VERIFICATION`; drift note candidate. |
| Aggregation unit unclear | Quarantine or review-required result. |
| Sensitivity tier unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |
| Source terms unclear | `NEEDS_VERIFICATION`; no live activation. |

---

## Administrative and life-safety boundary

OpenFEMA administrative records are records of federal actions, program activity, declarations, awards, projects, or aggregates. They are not observed hazard events, live warnings, forecasts, or direct safety instructions.

Connector code and docs should preserve these defaults:

1. Preserve source table identity and source role explicitly.
2. Preserve declaration, program, project, aggregate, geography, and temporal metadata where available.
3. Preserve table version, freshness, pagination, and retrieval metadata.
4. Prevent export language that looks like emergency guidance, eligibility determination, legal advice, or site-specific determination.
5. Treat administrative records as administrative evidence only, not observation evidence.
6. Treat aggregate tables as aggregate evidence only, not household-level or person-level evidence.
7. Public surfaces must redirect emergency or life-safety decisions to official channels.
8. Derived maps, tiles, summaries, vector indexes, and AI-generated text are not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- table identity, source role, aggregation unit, temporal fields, and geography fields are explicit where available;
- administrative records are not emitted as observed events;
- aggregate records are not emitted as person-level or site-specific truth;
- malformed or incomplete responses fail closed;
- no test or connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entries are linked and current enough for review.
- [ ] The canonical relationship between `connectors/fema/` and `connectors/fema-openfema/` is resolved.
- [ ] Each admitted OpenFEMA table has its own SourceDescriptor.
- [ ] Each table has a source role, aggregation unit, sensitivity tier, rights snapshot, cadence, and admission decision.
- [ ] Live access is disabled by default.
- [ ] Pagination, freshness, and table identity behavior are documented before activation.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims, warnings, eligibility decisions, legal determinations, or life-safety guidance are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, schema-drift, table-not-admitted, aggregation-unit-unclear, and administrative-vs-observed cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm whether canonical connector home is `connectors/fema-openfema/` or `connectors/fema/`. | **NEEDS VERIFICATION** | Directory Rules, repo tree, source-catalog metadata, and ADR/migration note. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub listing. |
| Confirm source descriptor home and source IDs for each admitted table. | **NEEDS VERIFICATION** | Source registry entries and accepted schema. |
| Confirm OpenFEMA datasets included in first activation. | **NEEDS VERIFICATION** | Source steward review and source catalog updates. |
| Confirm API access method, pagination behavior, and freshness cadence. | **NEEDS VERIFICATION** | Source steward review and connector tests. |
| Confirm source terms and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm sensitivity tier and aggregation unit for each table. | **NEEDS VERIFICATION** | Sensitivity steward and domain steward review. |
| Confirm fixture strategy for OpenFEMA administrative and aggregate material. | **NEEDS VERIFICATION** | Test fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector as administrative and aggregate source intake, not hazard-event truth. It can make OpenFEMA material easier to inspect, stage, validate, and cite, but it must not turn administrative tables into observed events, eligibility decisions, emergency guidance, or public KFM truth without downstream evidence, policy, review, release, and rollback support.
