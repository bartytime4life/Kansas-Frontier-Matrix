<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-gbif-readme
title: connectors/gbif/ — GBIF Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Biodiversity steward · Flora steward · Fauna steward · Habitat steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; rights-and-sensitivity-gated
proposed_path: connectors/gbif/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-lane contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/sources/catalog/gbif/README.md
  - ../../docs/sources/catalog/gbif/async-download.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/habitat/README.md
  - ../../data/registry/sources/
  - ../../data/raw/fauna/
  - ../../data/raw/flora/
  - ../../data/raw/habitat/
  - ../../data/quarantine/fauna/
  - ../../data/quarantine/flora/
  - ../../data/quarantine/habitat/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, gbif, biodiversity, darwin-core, occurrence, taxonomy, flora, fauna, habitat, source-admission, raw, quarantine, governance]
notes:
  - "This README replaces a greenfield stub with a governed connector-lane contract for GBIF source admission."
  - "Visible source-catalog docs treat GBIF as both biodiversity occurrence aggregator and taxonomic backbone; final source role is assigned at admission by SourceDescriptor."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Rights, license, dataset provenance, source role, backbone versioning, restricted-record handling, tests, fixtures, CI wiring, and activation state remain NEEDS VERIFICATION until backed by current repo evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GBIF Connector

> Source-specific intake and admission lane for Global Biodiversity Information Facility material used by KFM biodiversity domains.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Rights: gated" src="https://img.shields.io/badge/rights-gated-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/gbif/`

## Quick jumps

[Scope](#scope) · [Evidence basis](#evidence-basis) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Source-role posture](#source-role-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/gbif/` is the connector lane for GBIF source intake and admission helpers.

It may contain connector-local documentation, configuration examples, source-admission code, bounded client helpers, parser helpers, Darwin Core normalization helpers, taxonomic-backbone metadata helpers, and tests for GBIF-shaped source material.

It must not become biodiversity truth, taxonomic authority, conservation-status authority, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Evidence basis

Repo evidence checked for this update:

- `connectors/gbif/README.md` existed as a greenfield stub.
- `docs/sources/catalog/gbif/README.md` describes GBIF as a KFM source catalog entry.
- The GBIF source catalog entry separates GBIF as an occurrence aggregator from GBIF as a taxonomic backbone.
- The catalog entry states that rights, sensitivity, backbone versioning, and source roles are governed at admission and by downstream policy.

This connector README does not invent current endpoints, rate limits, API credentials, download strategy, schema version, or activation state.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/fauna/ or data/quarantine/fauna/
  data/raw/flora/ or data/quarantine/flora/
  data/raw/habitat/ or data/quarantine/habitat/

NOT HERE:
  canonical occurrence truth
  taxonomic truth
  conservation-status truth
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

The connector may help retrieve, parse, or stage GBIF source material. It does not decide whether a record is taxonomically settled, rights-cleared, sensitivity-safe, review-complete, or publishable.

---

## Admission posture

Expected behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved records;
- no automatic conversion from source records into confirmed occurrence truth;
- no assumption that one taxonomic backbone is final for all KFM uses;
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

## Source-role posture

GBIF material can play more than one source role depending on the artifact and downstream use. The connector must preserve source-role metadata rather than flattening all records into one authority class.

Minimum posture:

1. Preserve dataset, publisher, license, citation, retrieval, and version metadata.
2. Preserve Darwin Core terms where available.
3. Preserve taxonomic backbone/version metadata where available.
4. Treat downstream joins with Flora, Fauna, Habitat, NatureServe, USFWS, ITIS, iNaturalist, iDigBio, or local source material as governed processing steps, not connector behavior.
5. Treat derived maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- dataset, publisher, license, citation, retrieval, taxon, uncertainty, source-role, and version fields are explicit where available;
- malformed or incomplete responses fail closed;
- GBIF records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release gates, redaction/generalization, EvidenceBundle closure, and rollback remain outside this connector.

---

## Definition of done

This connector lane is ready for first review when:

- [ ] Source catalog entry is linked and current enough for review.
- [ ] SourceDescriptor location and source ID are verified.
- [ ] Live access is disabled by default.
- [ ] Access form, download strategy, and retrieval method are documented before activation.
- [ ] Dataset, publisher, license, citation, source role, taxon, uncertainty, and version metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, license-missing, provenance-unclear, version-unclear, schema-drift, and restricted-record cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual implementation files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm source descriptor home and source ID. | **NEEDS VERIFICATION** | Source registry entry and accepted schema. |
| Confirm current GBIF access method and download strategy. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm Darwin Core and backbone-version handling. | **NEEDS VERIFICATION** | Parser tests and source descriptor. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshot. |
| Confirm restricted-record handling. | **NEEDS VERIFICATION** | Sensitivity policy and domain-steward review. |
| Confirm fixture strategy for occurrence and taxonomy material. | **NEEDS VERIFICATION** | Fixture registry and validation review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Treat this connector as biodiversity source intake, not release-ready truth. It can make GBIF material easier to inspect, stage, validate, and cite, but it must not promote source rows into public KFM claims without downstream evidence, policy, review, release, and rollback support.
