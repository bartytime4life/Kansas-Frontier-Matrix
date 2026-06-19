<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-geology-readme
title: connectors/geology/ — Geology Connector Coordination Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Geology steward · Hydrology steward · Environment steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated
proposed_path: connectors/geology/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-family contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - kgs/README.md
  - ../../docs/domains/geology/README.md
  - ../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../docs/domains/geology/SOURCES.md
  - ../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../docs/domains/geology/DATA_LIFECYCLE.md
  - ../../docs/sources/catalog/kansas/ksgs.md
  - ../../docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - ../../docs/sources/catalog/usgs/usgs-ngmdb.md
  - ../../docs/sources/catalog/usgs/usgs-mrds.md
  - ../../data/registry/sources/
  - ../../data/raw/geology/
  - ../../data/quarantine/geology/
  - ../../data/raw/hydrology/
  - ../../data/quarantine/hydrology/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, geology, natural-resources, kgs, usgs, source-admission, raw, quarantine, compatibility, governance]
notes:
  - "This README fills a previously blank geology connector-family README."
  - "Geology domain docs are confirmed under docs/domains/geology/; this connector-family path remains PROPOSED until confirmed by Directory Rules, ADR, migration note, or repo convention."
  - "Visible KGS source-catalog docs identify KGS connector placement under connectors/kansas/kgs/; connectors/geology/ must not become a parallel publisher authority without review."
  - "This folder coordinates geology source-admission boundaries only; it does not create geology truth, resource truth, hazard truth, policy authority, release authority, or publication authority."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Connector Coordination Lane

> Coordination README for geology-related source-admission connectors and compatibility paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: needs verification" src="https://img.shields.io/badge/canonicality-needs__verification-orange">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Rights: gated" src="https://img.shields.io/badge/rights-gated-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/geology/`

## Quick jumps

[Scope](#scope) · [Placement warning](#placement-warning) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Source-role posture](#source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/geology/` is a proposed coordination lane for geology-related source-admission connectors.

It may document connector-family boundaries, compatibility routing, source-admission expectations, shared fixture rules, and links to source-specific connector homes.

It must not become geology truth, hydrology truth, environment truth, resource truth, hazard truth, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Placement warning

The path exists, but canonicality is **NEEDS VERIFICATION**.

Current evidence shows:

```text
docs/domains/geology/README.md        # confirmed geology domain documentation home
connectors/geology/README.md          # this proposed connector-family README
connectors/geology/kgs/README.md      # compatibility lane created for requested KGS path
connectors/kansas/kgs/                # KGS connector lane named by the KGS source catalog page
```

Because KGS is a Kansas publisher source, publisher-specific KGS implementation should not be moved under `connectors/geology/` without a documented migration or ADR. This folder should coordinate geology connector expectations rather than create a parallel authority root.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/geology/ or data/quarantine/geology/
  data/raw/hydrology/ or data/quarantine/hydrology/

NOT HERE:
  canonical geology truth
  resource or hazard truth
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

Connectors under this lane may help retrieve, parse, stage, or inspect source material. They do not decide whether a record is canonical, analytically complete, sensitivity-safe, rights-cleared, review-complete, or publishable.

---

## Admission posture

Expected behavior for geology connector work:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved records;
- no conversion of source records into confirmed geology, hydrology, environment, resource, or hazard claims;
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

Geology source material may include maps, stratigraphic references, lithology, structures, subsurface observations, wells, logs, resource context, and related records. Source role must be assigned per SourceDescriptor and product, not by this folder.

Minimum posture:

1. Preserve source product, publisher, retrieval, rights, citation, vintage, geometry, uncertainty, and review metadata.
2. Preserve product-specific identifiers where available.
3. Keep occurrence, deposit, estimate, permit, production, reserve, and interpretation claims separate.
4. Treat downstream joins with KGS, USGS, KCC, KDHE, KDA-DWR, FEMA, county, or local records as governed processing steps, not connector behavior.
5. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- product, publisher, rights, citation, retrieval, geometry, uncertainty, source-role, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- geology records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, redaction/generalization, EvidenceBundle closure, and rollback remain outside this connector family.

---

## Definition of done

This connector-family README is ready for first review when:

- [ ] Directory Rules or ADR review confirms whether `connectors/geology/` is canonical, compatibility-only, or a migration target.
- [ ] Existing source-specific homes are linked without creating duplicate authority.
- [ ] KGS, USGS, and other geology source catalog entries are linked where they exist.
- [ ] SourceDescriptor homes and source IDs are verified for active sources.
- [ ] Live access is disabled by default for connector code.
- [ ] Product, publisher, rights, citation, source role, geometry, uncertainty, and vintage metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, rights-unclear, product-scope-unclear, schema-drift, and sensitive-location cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonicality of `connectors/geology/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm relationship to `connectors/kansas/kgs/`. | **NEEDS VERIFICATION** | Repo tree and migration note. |
| Confirm geology connector inventory below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor homes and source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm source-specific access and parsing scope. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshots. |
| Confirm sensitive-location handling. | **NEEDS VERIFICATION** | Sensitivity policy and domain-steward review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this folder narrow until canonical placement is resolved. It should coordinate geology connector boundaries without becoming a source registry, interpretation engine, resource-claim authority, release path, or public truth surface.
