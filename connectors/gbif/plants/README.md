<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gbif-plants-readme
title: connectors/gbif/plants/ — GBIF Plants Connector Sublane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Flora steward · Biodiversity steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated
proposed_path: connectors/gbif/plants/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-sublane contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../../docs/sources/catalog/gbif/README.md
  - ../../../docs/sources/catalog/gbif/async-download.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../data/registry/sources/
  - ../../../data/raw/flora/
  - ../../../data/quarantine/flora/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, gbif, plants, flora, biodiversity, darwin-core, occurrence, taxonomy, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank GBIF plants connector-sublane README."
  - "The parent GBIF connector README and GBIF source catalog page remain the main source-admission references."
  - "This sublane is flora-focused and does not create taxonomy authority, occurrence truth, policy authority, release authority, or publication authority."
  - "Connector output may enter RAW or QUARANTINE flora handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Canonical placement of a nested `connectors/gbif/plants/` sublane remains NEEDS VERIFICATION until confirmed by Directory Rules, ADR, migration note, or current repo convention."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF Plants Connector Sublane

> Flora-focused sublane under the GBIF connector for plant occurrence and plant-taxonomy source-admission candidates.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Canonicality: needs verification" src="https://img.shields.io/badge/canonicality-needs__verification-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/gbif/plants/`

## Quick jumps

[Scope](#scope) · [Placement warning](#placement-warning) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Flora source-role posture](#flora-source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/gbif/plants/` is a proposed flora-focused sublane below the GBIF connector.

It may document and support plant-specific source-admission handling for GBIF-shaped material, including plant occurrence records, plant taxon references, Darwin Core fields, taxonomic backbone metadata, dataset provenance, license/citation metadata, and source-vintage metadata.

It must not become plant occurrence truth, taxonomic authority, conservation status authority, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Placement warning

The path exists, but the canonical placement of nested connector sublanes under `connectors/gbif/` is **NEEDS VERIFICATION**.

Before adding additional GBIF organism-group sublanes, check:

- Directory Rules;
- source catalog references;
- parent `connectors/gbif/README.md`;
- current repo tree;
- source descriptor layout;
- any ADR or migration note.

If source-specific connector homes are preferred, this sublane may need to remain a compatibility index rather than an implementation home.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/flora/
  data/quarantine/flora/

NOT HERE:
  plant occurrence truth
  taxonomy authority
  conservation-status authority
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

This sublane may help prepare GBIF plant source material for governed admission. It does not decide whether a record is taxonomically settled, rights-cleared, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved records;
- no automatic conversion from source records into confirmed flora occurrence truth;
- no assumption that GBIF Backbone is the final taxonomy for every KFM flora use;
- no loss of dataset key, publisher, license, citation, retrieval metadata, source role, taxon identifier, backbone version, uncertainty, or review metadata;
- unclear rights, source role, taxonomic certainty, restricted-record status, or schema drift routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| License or citation metadata missing | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Dataset or publisher provenance unclear | Quarantine or review-required result. |
| Taxonomic backbone version unclear | `NEEDS_VERIFICATION`; no promotion. |
| Source response malformed | `ERROR` with safe metadata. |
| Restricted-record handling unclear | Quarantine or review-required result. |

---

## Flora source-role posture

GBIF plant material can be useful as occurrence evidence, taxonomy crosswalk support, dataset provenance, and context. The source role must be preserved at admission and must not be upgraded by this sublane.

Minimum posture:

1. Preserve dataset, publisher, license, citation, retrieval, and version metadata.
2. Preserve Darwin Core terms where available.
3. Preserve taxonomic backbone/version metadata where available.
4. Treat downstream joins with USDA PLANTS, ITIS, iNaturalist, iDigBio, NatureServe, KU Herbarium, EDDMapS, or local flora datasets as governed processing steps, not connector behavior.
5. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Sublane-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- dataset, publisher, license, citation, retrieval, taxon, uncertainty, source-role, and version fields are explicit where available;
- malformed or incomplete responses fail closed;
- GBIF plant records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, redaction/generalization, EvidenceBundle closure, and rollback remain outside this sublane.

---

## Definition of done

This connector sublane is ready for first review when:

- [ ] Parent GBIF connector README exists and is linked.
- [ ] GBIF source catalog entry is linked and current enough for review.
- [ ] Directory Rules or ADR review confirms whether `connectors/gbif/plants/` is canonical, compatibility-only, or a migration target.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Plant-specific filter/download strategy is documented before activation.
- [ ] Dataset, publisher, license, citation, source role, taxon, uncertainty, and version metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE flora handoff.
- [ ] No public claims are created by sublane code.
- [ ] Tests cover no-network, malformed, incomplete, license-missing, provenance-unclear, version-unclear, schema-drift, and restricted-record cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm canonicality of `connectors/gbif/plants/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm plant-specific GBIF query/download strategy. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm Darwin Core and backbone-version handling. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm restricted-record handling. | **NEEDS VERIFICATION** | Sensitivity policy and flora steward review. |
| Confirm fixture strategy for plant occurrence and taxonomy material. | **NEEDS VERIFICATION** | Fixture registry and validation review. |
| Confirm CI wiring for sublane-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Keep this sublane narrow. It should make GBIF plant intake more inspectable without becoming a flora truth store, taxonomy authority, policy engine, release path, or public truth surface.
