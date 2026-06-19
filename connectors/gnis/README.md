<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gnis-readme
title: connectors/gnis/ — GNIS Connector Compatibility Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Spatial-foundation steward · Settlements steward · Cultural-sensitivity reviewer · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; cultural-sensitivity-aware; rights-and-sensitivity-gated
proposed_path: connectors/gnis/README.md
truth_posture: CONFIRMED path exists / PROPOSED compatibility contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/sources/catalog/usgs/gnis-names.md
  - ../../docs/sources/catalog/usgs/README.md
  - ../../docs/sources/catalog/usgs/IDENTITY.md
  - ../../docs/sources/catalog/usgs/RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../docs/domains/settlements/README.md
  - ../../docs/domains/settlements-infrastructure/README.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../data/registry/sources/usgs/
  - ../../data/raw/spatial-foundation/
  - ../../data/quarantine/spatial-foundation/
  - ../../data/raw/settlements/
  - ../../data/quarantine/settlements/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../schemas/contracts/v1/spatial/
  - ../../schemas/contracts/v1/settlements/
  - ../../policy/sources/usgs/
  - ../../policy/sensitivity/cultural/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, gnis, usgs, place-names, toponymy, settlements, spatial-foundation, source-admission, administrative, raw, quarantine, governance]
notes:
  - "This README fills a previously blank requested path for GNIS-related source admission."
  - "Visible GNIS source-catalog docs identify GNIS as a USGS product and point to connectors/usgs/; this connectors/gnis/ path should be treated as compatibility or PROPOSED until ratified."
  - "GNIS is an administrative place-name carrier, not sole place-name truth, boundary truth, cultural-name authority, Tribal-authority substitute, or publication authority."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Implementation files, source activation, SourceDescriptor, fixtures, tests, CI wiring, cultural-sensitivity handling, and current access method remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GNIS Connector Compatibility Lane

> Source-admission README for the requested `connectors/gnis/` path, with canonical placement marked for review.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Canonicality: needs verification" src="https://img.shields.io/badge/canonicality-needs__verification-orange">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Role: administrative" src="https://img.shields.io/badge/role-administrative-yellowgreen">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/gnis/`

## Quick jumps

[Scope](#scope) · [Placement warning](#placement-warning) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Name-authority posture](#name-authority-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/gnis/` is a requested connector path for USGS Geographic Names Information System source-admission work.

It may document compatibility routing, source-admission boundaries, parser expectations, fixture expectations, and links to the canonical GNIS source catalog entry.

It must not become place truth, boundary truth, cultural-name authority, Tribal-name authority, settlement truth, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Placement warning

The visible GNIS source catalog page treats GNIS as a USGS product and points to:

```text
connectors/usgs/
```

This requested path exists:

```text
connectors/gnis/
```

Until Directory Rules, an ADR, a migration note, or current repo convention ratifies this folder, treat it as a compatibility or draft lane. New implementation code should not be placed here as canonical without review.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/spatial-foundation/ or data/quarantine/spatial-foundation/
  data/raw/settlements/ or data/quarantine/settlements/

NOT HERE:
  canonical place truth
  boundary truth
  cultural-name authority
  Tribal-authority substitution
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, stage, or inspect GNIS source material. It does not decide whether a name is culturally complete, locally preferred, boundary-valid, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved records;
- no silent substitution of GNIS names for Tribal-authoritative, locally authoritative, or historically attested names;
- no conversion of point coordinates into boundary proof;
- no loss of feature ID, feature class, name variants, decision history, retrieval, rights, source role, geometry, uncertainty, or review metadata;
- unclear cultural sensitivity, source role, name-history status, coordinate uncertainty, or schema drift routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Name-history handling unclear | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Cultural-sensitivity handling unclear | Quarantine or review-required result. |
| Feature identity unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Name-authority posture

GNIS is an administrative U.S. federal place-name carrier. KFM must preserve that role without turning it into sole name truth.

Minimum posture:

1. Preserve feature ID, feature class, current name, variants, decision/history fields, coordinates, source vintage, and retrieval metadata where available.
2. Preserve administrative source role instead of flattening GNIS into observed reality.
3. Preserve name history rather than overwriting it.
4. Treat downstream joins with Tribal, state, local, archival, FamilySearch, Census, HIFLD, USGS, USDOT, or other place authorities as governed processing steps, not connector behavior.
5. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- feature ID, feature class, name, variants, decision/history, coordinate, uncertainty, source-role, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- GNIS records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, cultural-sensitivity review, EvidenceBundle closure, and rollback remain outside this connector.

---

## Definition of done

This compatibility lane is ready for first review when:

- [ ] Directory Rules or ADR review confirms whether this path is canonical, compatibility-only, or a migration target.
- [ ] The canonical USGS/GNIS connector home is linked and not duplicated.
- [ ] GNIS source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Name-history and cultural-sensitivity handling are documented before activation.
- [ ] Feature ID, feature class, name, variants, decision/history, coordinate, uncertainty, and vintage metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, name-history-unclear, cultural-sensitivity-unclear, coordinate-unclear, schema-drift, and authority-conflict cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonicality of `connectors/gnis/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm relationship to `connectors/usgs/`. | **NEEDS VERIFICATION** | Repo tree and migration note. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm GNIS access and refresh approach. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm cultural-sensitivity handling. | **NEEDS VERIFICATION** | Policy review and steward review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this path narrow until canonical placement is resolved. GNIS is a USGS place-name source, so this standalone connector path should not become a parallel authority unless a documented migration or ADR says so.
