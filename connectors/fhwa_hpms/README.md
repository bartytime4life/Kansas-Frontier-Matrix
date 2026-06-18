<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-fhwa-hpms-readme
title: connectors/fhwa_hpms/ — FHWA HPMS Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Roads/Rail/Trade steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public
proposed_path: connectors/fhwa_hpms/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/sources/catalog/usdot/README.md
  - ../../docs/sources/catalog/usdot/fhwa-hpms.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/SOURCE_FAMILIES.md
  - ../../data/registry/sources/
  - ../../data/raw/roads-rail-trade/
  - ../../data/quarantine/roads-rail-trade/
  - ../../data/receipts/roads-rail-trade/
  - ../../data/proofs/roads-rail-trade/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, fhwa, hpms, usdot, roads-rail-trade, highway, road-network, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-lane contract for FHWA HPMS source admission."
  - "Visible source-catalog docs identify `fhwa_hpms` as a proposed source_id hint and `connectors/fhwa_hpms/` as the connector lane."
  - "Current endpoint URL, exact cadence, schema version, access form, rights text, tests, fixtures, CI wiring, and activation state remain NEEDS VERIFICATION."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FHWA HPMS Connector

> Source-specific intake and admission lane for FHWA Highway Performance Monitoring System material used by the KFM Roads/Rail/Trade domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Domain: roads rail trade" src="https://img.shields.io/badge/domain-roads__rail__trade-purple">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/fhwa_hpms/`

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Authority boundary](#authority-boundary) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Admission posture](#admission-posture) · [Road-network and source-role posture](#road-network-and-source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/fhwa_hpms/` is the connector lane for FHWA HPMS source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, normalization helpers, and tests for HPMS-shaped source material.

It must not become road-network truth, transportation-policy authority, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/fhwa_hpms/`  
> **Truth posture:** README path is CONFIRMED. Connector implementation, source activation, endpoint/access surface, schema version, current cadence, tests, fixtures, and CI wiring remain `NEEDS VERIFICATION`.

---

## Repo fit

```text
connectors/
└── fhwa_hpms/
    └── README.md
```

Known related paths:

```text
docs/sources/catalog/usdot/README.md        # USDOT source-family catalog entry
docs/sources/catalog/usdot/fhwa-hpms.md     # FHWA HPMS source product page
docs/domains/roads-rail-trade/              # roads/rail/trade domain lane
data/registry/sources/                      # source descriptors and activation state
connectors/fhwa_hpms/                       # this connector lane
```

Related responsibility roots:

```text
connectors/                                  # source-specific fetch and admission code
docs/sources/catalog/usdot/                  # USDOT source-family briefings
docs/domains/roads-rail-trade/               # domain doctrine, source-family register, object meaning
data/registry/sources/                       # source descriptors and activation state
data/raw/roads-rail-trade/                   # raw staged source outputs, if admitted
data/quarantine/roads-rail-trade/            # held material requiring review
fixtures/                                    # shared fixtures, when promoted out of connector-local scope
schemas/contracts/v1/source/                 # source/admission schemas, subject to accepted schema-home convention
policy/sensitivity/                          # sensitivity and release rules
policy/rights/                               # rights and license policy, if present
release/                                     # release decisions, rollback, and correction state
```

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/roads-rail-trade/
  data/quarantine/roads-rail-trade/

NOT HERE:
  canonical road-network truth
  transportation-policy conclusions
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, or stage HPMS source material. It does not decide whether a road feature is canonical, currently open, legally classified, safe, or publishable.

---

## Inputs

Potential input classes include:

- source descriptor references;
- steward-approved HPMS access surface identifiers;
- reporting year or source-vintage parameters;
- state, county, route, segment, functional-class, condition, performance, use, or operating-characteristic fields where present in the source shape;
- geometry, linear-reference, projection, and spatial-resolution metadata where available;
- table, schema, data dictionary, or release metadata;
- rights and source-term metadata;
- test fixtures that preserve HPMS source shape without becoming canonical road-network truth.

All live access and bulk/source retrieval behavior is **NEEDS VERIFICATION** until endpoint/access form, cadence, schema version, rights, and source descriptor state are reviewed.

---

## Exclusions

Do not place these in `connectors/fhwa_hpms/`:

| Excluded material | Correct handling |
|---|---|
| SourceDescriptor authority records | `data/registry/sources/` or accepted source registry home. |
| Machine-checkable schemas | `schemas/contracts/v1/...` under accepted schema-home convention. |
| Domain object contracts | `contracts/` or accepted domain-contract root. |
| Policy decisions or release rules | `policy/` and release review surfaces. |
| Processed road-network records | Downstream lifecycle roots only. |
| Published maps, tiles, catalog records, graph records, or public claims | Release and publication roots only. |
| Large source payloads or bulk extracts | Store only through approved RAW/QUARANTINE lifecycle paths with receipts. |
| Generated summaries used as evidence | Not allowed; EvidenceBundle-backed claims only. |

---

## Admission posture

FHWA HPMS connector output must be conservative and source-vintage aware.

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved records;
- no conversion of HPMS source rows into canonical KFM road-network truth;
- no assumption that annual source-vintage data is current operational status;
- no loss of source year, table identity, field definitions, spatial reference, or lineage metadata;
- no joining to sensitive private-facility, person, parcel, or critical-infrastructure context without downstream policy review;
- unclear endpoint, cadence, schema version, rights, projection, field semantics, or join sensitivity routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| Source descriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Source vintage missing | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Schema or field definition drift detected | `NEEDS_VERIFICATION`; drift note candidate. |
| Geometry/projection metadata unclear | Quarantine or review-required result. |
| Rights or terms unclear | `NEEDS_VERIFICATION`; no live activation. |
| Source response malformed | `ERROR` with safe metadata. |
| Sensitive join risk detected | Quarantine or policy-review-required result. |

---

## Road-network and source-role posture

HPMS material may be useful as authority, observation, context, or model-supporting evidence depending on the field and downstream use. The connector must preserve source-role posture rather than flattening every HPMS field into one truth class.

Minimum posture:

1. Preserve source vintage and retrieval metadata.
2. Preserve source table, field definitions, and source role where available.
3. Preserve geometry, projection, linear reference, and spatial-resolution metadata where available.
4. Treat downstream conflation with other road-network sources as a governed processing step, not connector behavior.
5. Treat sensitive joins as fail-closed until policy and review approve the join.
6. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- source year/vintage, table identity, schema version, field definitions, geometry/projection metadata, and lineage fields are explicit where available;
- malformed or incomplete responses fail closed;
- HPMS records remain source-admission candidates until downstream validation;
- sensitive join risks route to quarantine or review-required behavior;
- no test or connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and proposed source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Endpoint/access form and bulk/source retrieval method are documented before activation.
- [ ] Source year/vintage, schema version, table identity, and field semantics are preserved in parser output.
- [ ] Geometry, projection, and spatial-resolution metadata are preserved where available.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No canonical road-network truth or public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, source-vintage-missing, projection-unclear, schema-drift, rights-unclear, and sensitive-join-risk cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Mounted repo tree or GitHub listing. |
| Confirm source descriptor home and source ID `fhwa_hpms`. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm current HPMS endpoint/access form. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm current cadence, source vintage, and schema version handling. | **NEEDS VERIFICATION** | Source descriptor and test fixtures. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm geometry, projection, and linear-reference handling. | **NEEDS VERIFICATION** | Fixture review and downstream schema/contract checks. |
| Confirm sensitive-join rules for HPMS-derived material. | **NEEDS VERIFICATION** | Sensitivity policy and Roads/Rail/Trade steward review. |
| Confirm fixture strategy for HPMS material. | **NEEDS VERIFICATION** | Test fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector as source-vintage-aware road-network intake, not canonical road-network truth. It can make FHWA HPMS material easier to inspect, stage, validate, and cite, but it must not promote source rows into public KFM claims without downstream evidence, policy, review, release, and rollback support.
