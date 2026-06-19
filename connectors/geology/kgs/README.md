<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-geology-kgs-readme
title: connectors/geology/kgs/ — KGS Geology Connector Compatibility Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Geology steward · Hydrology steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated
proposed_path: connectors/geology/kgs/README.md
truth_posture: CONFIRMED path exists / PROPOSED compatibility contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../../docs/sources/catalog/kansas/ksgs.md
  - ../../../docs/sources/catalog/kansas/README.md
  - ../../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/environment/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/geology/
  - ../../../data/raw/hydrology/
  - ../../../data/quarantine/geology/
  - ../../../data/quarantine/hydrology/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, geology, kansas, kgs, ksgs, source-admission, raw, quarantine, compatibility, governance]
notes:
  - "This README fills a previously blank requested path for KGS-related geology source admission."
  - "Visible KGS source-catalog docs identify the canonical connector lane as connectors/kansas/kgs/; this connectors/geology/kgs/ path should be treated as compatibility or PROPOSED until ratified."
  - "KGS source material may serve Geology, Hydrology, and Environment domains, but this folder must not become geology truth, hydrology truth, policy authority, release authority, or publication authority."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Implementation files, source activation, SourceDescriptor, fixtures, tests, CI wiring, rights, and current product scope remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KGS Geology Connector Compatibility Lane

> Source-admission README for the requested `connectors/geology/kgs/` path, with canonical placement marked for review.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: needs verification" src="https://img.shields.io/badge/canonicality-needs__verification-orange">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Rights: gated" src="https://img.shields.io/badge/rights-gated-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/geology/kgs/`

## Quick jumps

[Scope](#scope) · [Placement warning](#placement-warning) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Source-role posture](#source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/geology/kgs/` is a requested connector path for Kansas Geological Survey source-admission work related to KFM geology and adjacent hydrology/environment lanes.

It may document compatibility routing, source-admission boundaries, parser expectations, fixture expectations, and links to the canonical KGS source catalog entry.

It must not become geologic truth, hydrologic truth, well truth, mineral truth, hazard truth, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Placement warning

The visible KGS source catalog page states that the connector path in the source catalog is:

```text
connectors/kansas/kgs/
```

This requested path exists:

```text
connectors/geology/kgs/
```

Until Directory Rules, an ADR, a migration note, or current repo convention ratifies this folder, treat it as a compatibility or draft lane. New implementation code should not be placed here as canonical without review.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/geology/ or data/quarantine/geology/
  data/raw/hydrology/ or data/quarantine/hydrology/

NOT HERE:
  canonical geology truth
  hydrology truth
  hazard truth
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, stage, or inspect KGS source material. It does not decide whether a record is canonical, analytically complete, sensitivity-safe, rights-cleared, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved records;
- no conversion of source records into confirmed geology, hydrology, or hazard claims;
- no loss of source product, publisher, retrieval, rights, vintage, geometry, uncertainty, role, or review metadata;
- unclear rights, source role, product scope, location sensitivity, or schema drift routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Product scope unclear | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Rights or attribution unclear | `NEEDS_VERIFICATION`; no promotion. |
| Sensitive location handling unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Source-role posture

KGS material can include maps, well-related records, geologic units, water-well program material, digital logs, and other source products. Source role must be assigned per SourceDescriptor and product, not by this folder.

Minimum posture:

1. Preserve source product, publisher, retrieval, rights, citation, vintage, geometry, uncertainty, and review metadata.
2. Preserve product-specific identifiers where available.
3. Treat downstream joins with KCC, KDHE, KDA-DWR, USGS, FEMA, county, or local records as governed processing steps, not connector behavior.
4. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- product, publisher, rights, citation, retrieval, geometry, uncertainty, source-role, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- KGS records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, redaction/generalization, EvidenceBundle closure, and rollback remain outside this connector.

---

## Definition of done

This compatibility lane is ready for first review when:

- [ ] Directory Rules or ADR review confirms whether this path is canonical, compatibility-only, or a migration target.
- [ ] The canonical KGS connector home is linked and not duplicated.
- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] KGS product scope is documented before activation.
- [ ] Product, publisher, rights, citation, source role, geometry, uncertainty, and vintage metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, rights-unclear, product-scope-unclear, schema-drift, and sensitive-location cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonicality of `connectors/geology/kgs/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm relationship to `connectors/kansas/kgs/`. | **NEEDS VERIFICATION** | Repo tree and migration note. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm product-specific access and parsing scope. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm sensitive-location handling. | **NEEDS VERIFICATION** | Sensitivity policy and domain-steward review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this path narrow until canonical placement is resolved. KGS is a Kansas-source family in the visible catalog, so this geology path should not become a parallel authority unless a documented migration or ADR says so.
