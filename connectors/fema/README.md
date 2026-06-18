<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fema-readme
title: connectors/fema/ — FEMA Connector Family Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Hazards steward · Hydrology steward · Settlements/Infrastructure steward · Data steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-context-only; not-for-life-safety
proposed_path: connectors/fema/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-family contract / IMPLEMENTATION DEPTH UNKNOWN
related:
  - ../README.md
  - ../fema-nfhl/README.md
  - ../fema-openfema/README.md
  - ../../docs/sources/catalog/fema/README.md
  - ../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../docs/sources/catalog/fema/map-service-center.md
  - ../../docs/sources/catalog/fema/openfema-disaster-declarations.md
  - ../../docs/sources/catalog/fema/openfema-auxiliary-tables.md
  - ../../docs/sources/catalog/fema/nfip-claim-policy-aggregates.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, fema, nfhl, openfema, map-service-center, hazards, hydrology, regulatory-context, administrative-context, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub with a governed FEMA connector-family contract."
  - "Visible FEMA source-catalog docs reference connectors/fema/ as the FEMA family connector location. Specialized folders such as connectors/fema-nfhl/ and connectors/fema-openfema/ should be treated as companion or candidate split lanes until an ADR or migration note resolves canonical structure."
  - "FEMA connector outputs may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, policy, review, release, and rollback remain outside this folder."
  - "FEMA products are regulatory or administrative context, not observed hazard events, forecasts, warnings, legal determinations, insurance determinations, or life-safety guidance."
  - "Specific endpoints, bulk-download behavior, API pagination, descriptors, tests, fixtures, CI wiring, terms, source roles, and activation state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FEMA Connector Family

> Source-family intake and admission lane for FEMA material used by KFM Hazards, Hydrology, Settlements/Infrastructure, and exposure-context workflows.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Life safety: not guidance" src="https://img.shields.io/badge/life__safety-not__guidance-critical">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fema/`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Canonicality and split-lane warning](#canonicality-and-split-lane-warning) · [Authority boundary](#authority-boundary) · [FEMA product lanes](#fema-product-lanes) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Admission posture](#admission-posture) · [Regulatory administrative and life-safety boundary](#regulatory-administrative-and-life-safety-boundary) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fema/` is the source-family connector lane for FEMA intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, pagination or bulk-download helpers, and tests for FEMA source products.

It must not become hazard truth, flood truth, observed-event truth, emergency-alert authority, regulatory interpretation authority, insurance determination authority, benefit-eligibility authority, source descriptor authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/fema/`  
> **Truth posture:** README path is CONFIRMED. Connector implementation, source activation, product coverage, endpoints, bulk strategy, OpenFEMA table coverage, tests, fixtures, policy enforcement, and CI wiring remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── fema/
    └── README.md
```

Visible FEMA source-catalog metadata points to this family connector location. Specialized connector folders also exist or have been documented nearby:

```text
connectors/fema/             # FEMA family connector lane
connectors/fema-nfhl/        # NFHL-specific connector lane; canonicality NEEDS VERIFICATION
connectors/fema-openfema/    # OpenFEMA-specific connector lane; canonicality NEEDS VERIFICATION
```

Related responsibility roots:

```text
connectors/                                      # source-specific fetch and admission code
docs/sources/catalog/fema/                       # FEMA source-family and product briefings
docs/domains/hazards/                            # hazards domain doctrine
docs/domains/hydrology/                          # hydrology domain doctrine
docs/domains/settlements-infrastructure/         # exposure and infrastructure domain doctrine
data/registry/sources/                           # source descriptors and activation state
data/raw/                                        # raw staged source outputs, domain-routed
data/quarantine/                                 # held material requiring review, domain-routed
data/receipts/                                   # process and validation receipts
data/proofs/                                     # EvidenceBundles and proof packs
policy/sensitivity/                              # sensitivity and release rules
release/                                         # release decisions and rollback/correction state
```

---

## Canonicality and split-lane warning

`connectors/fema/` appears to be the source-family connector home referenced by visible FEMA catalog docs. The more specific `connectors/fema-nfhl/` and `connectors/fema-openfema/` paths should not become parallel authority roots by accident.

Until a repo tree review, ADR, or migration note resolves the split, treat the relationship as follows:

| Path | Status | Working interpretation |
|---|---:|---|
| `connectors/fema/` | **CONFIRMED path / PROPOSED family contract** | FEMA source-family connector lane. |
| `connectors/fema-nfhl/` | **CONFIRMED path / CANONICALITY NEEDS VERIFICATION** | Candidate NFHL product-specific lane or compatibility split. |
| `connectors/fema-openfema/` | **CONFIRMED path / CANONICALITY NEEDS VERIFICATION** | Candidate OpenFEMA product-specific lane or compatibility split. |

Do not move, duplicate, or create additional FEMA connector homes without checking Directory Rules, source catalog references, source descriptors, and ADR/migration notes.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/<domain>/
  data/quarantine/<domain>/

NOT HERE:
  observed hazard event truth
  flood forecast or warning
  legal/regulatory interpretation
  insurance determination
  eligibility or benefit determination
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector family may help retrieve, parse, or stage FEMA source material. It does not decide whether an event happened on the ground, whether a location is safe, whether a property is insured or eligible, whether a regulation applies, or whether a record is publishable.

---

## FEMA product lanes

| Product lane | Source role posture | Connector posture |
|---|---|---|
| NFHL | Regulatory context | Preserve regulatory attributes, version, effective date, datum, units, and lineage; never treat as observed inundation. |
| Map Service Center | Distribution / document access context | Treat as a companion access surface; do not replace source-descriptor or release authority. |
| OpenFEMA Disaster Declarations | Administrative context | Record of federal action; not an observed hazard event. |
| OpenFEMA auxiliary tables | Mixed administrative and aggregate context | Per-table SourceDescriptor and admission decision required; no umbrella admission. |
| NFIP claim or policy aggregates | Aggregate context, subject to review | Preserve aggregation unit and sensitivity posture; do not infer household-level truth. |

Each product or table that participates in KFM must have its own source descriptor, role, cadence, rights snapshot, sensitivity tier, and admission decision.

---

## Inputs

Potential input classes include:

- source descriptor references;
- FEMA family or product identifiers;
- NFHL service or bulk package metadata;
- OpenFEMA dataset identifiers;
- pagination, freshness, and retrieval metadata;
- regulatory attributes, administrative action fields, aggregate fields, geography fields, and temporal fields;
- datum, units, version, effective date, and source lineage metadata;
- test fixtures that preserve source shape without becoming public guidance.

All live access, bulk download, API pagination, and per-product/table behavior is **NEEDS VERIFICATION** until source terms, source role, sensitivity tier, freshness cadence, and record identity rules are reviewed.

---

## Exclusions

Do not place these in `connectors/fema/`:

| Excluded material | Correct handling |
|---|---|
| SourceDescriptor authority records | `data/registry/sources/` or accepted source registry home. |
| Machine-checkable schemas | `schemas/contracts/v1/...` under accepted schema-home convention. |
| Policy decisions or release rules | `policy/` and release review surfaces. |
| Processed hazard, hydrology, settlement, infrastructure, or exposure records | Downstream lifecycle roots only. |
| Published maps, tiles, catalogs, dashboards, or public claims | Release and publication roots only. |
| Emergency, eligibility, benefit, legal, insurance, or life-safety determination text | Out of scope; redirect to official channels and reviewed public guidance. |
| Large source payloads or bulk extracts | Store only through approved RAW/QUARANTINE lifecycle paths with receipts. |
| Generated summaries used as evidence | Not allowed; EvidenceBundle-backed claims only. |

---

## Admission posture

FEMA connector output must be conservative.

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved source records;
- no conversion of regulatory context into observed event truth;
- no conversion of administrative records into observed events;
- no conversion of aggregate records into person-level or site-specific truth;
- no warning, forecast, legal, insurance, eligibility, or life-safety determination language;
- no loss of role, version, freshness, source lineage, rights, sensitivity, or attribution metadata;
- unclear source role, aggregation unit, version, datum, rights, sensitivity, or source shape routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Product/table has no admission decision | `NEEDS_VERIFICATION`; no live activation. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Bulk package or pagination incomplete | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Schema or source-shape drift detected | `NEEDS_VERIFICATION`; drift note candidate. |
| Datum, version, effective date, role, or aggregation unit unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |
| Source terms unclear | `NEEDS_VERIFICATION`; no live activation. |

---

## Regulatory administrative and life-safety boundary

FEMA products used by KFM are regulatory or administrative context unless a source descriptor and domain contract say otherwise. They are not live warnings, forecasts, emergency guidance, insurance rulings, benefit eligibility decisions, or legal advice.

Connector code and docs should preserve these defaults:

1. Preserve product/table identity and source role explicitly.
2. Preserve version, effective date, datum, units, declaration, program, aggregation unit, geography, and temporal metadata where available.
3. Keep visualization surfaces separate from analytic vector or table source material when the source docs require that separation.
4. Prevent export language that looks like emergency guidance, legal advice, eligibility determination, insurance determination, or site-specific determination.
5. Treat administrative records as administrative evidence only, not observation evidence.
6. Treat aggregate tables as aggregate evidence only, not household-level or person-level evidence.
7. Public surfaces must redirect emergency or life-safety decisions to official channels.
8. Derived maps, tiles, summaries, vector indexes, and AI-generated text are not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- product/table identity, source role, aggregation unit, version, effective date, datum, units, temporal fields, geography fields, and lineage fields are explicit where available;
- regulatory records are not emitted as observed events;
- administrative records are not emitted as observed events;
- aggregate records are not emitted as person-level or site-specific truth;
- malformed or incomplete responses fail closed;
- no test or connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this connector.

---

## Definition of done

This connector family lane is ready for first review when:

- [ ] FEMA source catalog entries are linked and current enough for review.
- [ ] The canonical relationship between `connectors/fema/`, `connectors/fema-nfhl/`, and `connectors/fema-openfema/` is resolved.
- [ ] Each admitted FEMA product or OpenFEMA table has its own SourceDescriptor.
- [ ] Each product/table has a source role, sensitivity tier, rights snapshot, cadence, and admission decision.
- [ ] Live access is disabled by default.
- [ ] Bulk, service, pagination, freshness, and table identity behavior are documented before activation.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims, warnings, eligibility decisions, legal determinations, insurance determinations, or life-safety guidance are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, schema-drift, source-not-admitted, role-unclear, aggregation-unit-unclear, and regulatory/administrative-vs-observed cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm whether `connectors/fema/` is the canonical family connector home. | **NEEDS VERIFICATION** | Directory Rules, repo tree, source-catalog metadata, and ADR/migration note. |
| Confirm relationship to `connectors/fema-nfhl/` and `connectors/fema-openfema/`. | **NEEDS VERIFICATION** | Repo tree, source-catalog metadata, and ADR/migration decision. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub listing. |
| Confirm source descriptor home and source IDs for each admitted FEMA product/table. | **NEEDS VERIFICATION** | Source registry entries and accepted schema. |
| Confirm API, bulk, service, and pagination behavior for first activation. | **NEEDS VERIFICATION** | Source steward review and connector tests. |
| Confirm source terms and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm sensitivity tier, source role, and aggregation unit for each product/table. | **NEEDS VERIFICATION** | Sensitivity steward and domain steward review. |
| Confirm fixture strategy for FEMA regulatory, administrative, and aggregate material. | **NEEDS VERIFICATION** | Test fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector family as source admission, not public truth. FEMA records can be strong regulatory or administrative context, but they must not be turned into observed events, forecasts, warnings, legal conclusions, insurance determinations, benefit decisions, or public KFM truth without downstream evidence, policy, review, release, and rollback support.
