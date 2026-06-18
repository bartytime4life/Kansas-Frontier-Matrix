<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fra-gcis-readme
title: connectors/fra_gcis/ — FRA GCIS Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Roads/Rail/Trade steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; review-required-source-intake
proposed_path: connectors/fra_gcis/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/sources/catalog/usdot/README.md
  - ../../docs/sources/catalog/usdot/fra-gcis.md
  - ../../docs/sources/catalog/usdot/fra-form57.md
  - ../../docs/sources/catalog/usdot/stb-class1.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../data/registry/sources/
  - ../../data/raw/roads-rail-trade/
  - ../../data/quarantine/roads-rail-trade/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, fra, gcis, usdot, rail, crossing-inventory, roads-rail-trade, source-admission, administrative, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-lane contract for FRA GCIS source admission."
  - "Visible source-catalog docs identify `fra_gcis` as a proposed source_id hint and `connectors/fra_gcis/` as the connector lane."
  - "GCIS is treated as administrative compilation source material; do not collapse the inventory itself into observed-change evidence."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Implementation files, source activation, source descriptor, access method, fixtures, tests, CI wiring, rights, and current schema scope remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FRA GCIS Connector

> Source-specific intake and admission lane for FRA Grade Crossing Inventory System material used by KFM Roads/Rail/Trade review workflows.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Role: administrative source" src="https://img.shields.io/badge/role-administrative__source-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fra_gcis/`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Source-role posture](#source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fra_gcis/` is the connector lane for FRA GCIS source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, normalization helpers, and tests for GCIS-shaped source material.

It must not become crossing truth, observed-change truth, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Repo fit

```text
connectors/
└── fra_gcis/
    └── README.md
```

Known related paths:

```text
docs/sources/catalog/usdot/README.md
docs/sources/catalog/usdot/fra-gcis.md
docs/sources/catalog/usdot/fra-form57.md
docs/sources/catalog/usdot/stb-class1.md
docs/domains/roads-rail-trade/
docs/domains/settlements-infrastructure/
data/registry/sources/
data/raw/roads-rail-trade/
data/quarantine/roads-rail-trade/
connectors/fra_gcis/
```

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/roads-rail-trade/
  data/quarantine/roads-rail-trade/

NOT HERE:
  final inventory truth
  public products
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, or stage GCIS source material. It does not decide whether a record is canonical, release-ready, analytically complete, or suitable for public display.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved records;
- no conversion of an administrative inventory snapshot into observed-change evidence;
- no assumption that one source snapshot is complete without downstream validation;
- no loss of inventory identity, source vintage, source role, field definitions, or lineage metadata;
- unclear access method, schema scope, rights, field semantics, or review readiness routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Source vintage missing | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Schema or field definition drift detected | `NEEDS_VERIFICATION`; drift note candidate. |
| Rights or terms unclear | `NEEDS_VERIFICATION`; no live activation. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Source-role posture

GCIS material is treated as administrative compilation source material. Individual fields may carry their own dates or review context, but the connector must not upgrade the entire inventory into observed-change evidence.

Minimum posture:

1. Preserve source vintage and retrieval metadata.
2. Preserve inventory identity, field definitions, and source role where available.
3. Treat downstream joins with related rail, transportation, or place sources as governed processing steps, not connector behavior.
4. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- source vintage, inventory identity, schema version, field definitions, and lineage fields are explicit where available;
- malformed or incomplete responses fail closed;
- GCIS records remain source-admission candidates until downstream validation;
- no test or connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and proposed source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Access form and retrieval method are documented before activation.
- [ ] Source vintage, inventory identity, schema version, and field semantics are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, source-vintage-missing, schema-drift, role-collapse, and rights-unclear cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub listing. |
| Confirm source descriptor home and source ID `fra_gcis`. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm current GCIS access method. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm current schema scope and source-vintage handling. | **NEEDS VERIFICATION** | Source descriptor and test fixtures. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm fixture strategy for GCIS material. | **NEEDS VERIFICATION** | Test fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector as administrative source intake, not release-ready truth. It can make FRA GCIS material easier to inspect, stage, validate, and cite, but it must not promote source rows into public KFM claims without downstream evidence, policy, review, release, and rollback support.
