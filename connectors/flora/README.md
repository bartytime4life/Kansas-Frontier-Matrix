<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-flora-readme
title: connectors/flora/ — Flora Connector Group
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Flora steward · Data steward · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine
proposed_path: connectors/flora/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-group contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../docs/sources/catalog/usda/usda-plants.md
  - ../../docs/sources/catalog/kansas/ku-herbarium.md
  - ../../docs/sources/catalog/eddmaps/README.md
  - ../../data/registry/sources/flora/
  - ../../data/raw/flora/
  - ../../data/quarantine/flora/
  - ../../data/receipts/flora/
  - ../../data/proofs/flora/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, flora, plants, herbarium, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank file with a governed connector-group contract for flora-related connector lanes."
  - "Visible flora doctrine says intake code lives in connectors/ and pipelines/, while concrete connector path strings remain PROPOSED until verified against repo evidence."
  - "Connector output may enter RAW or QUARANTINE only; downstream validation, EvidenceBundle closure, catalog/triplet projection, publication, release, and rollback remain outside this folder."
  - "Specific child connectors, source descriptors, tests, fixtures, CI wiring, source terms, rights snapshots, and activation state remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Connector Group

> Connector-group landing page for flora-related source-admission lanes under `connectors/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/flora/`

## Scope

`connectors/flora/` is a connector-group landing page for flora-related source-admission lanes.

It may explain how connector code retrieves, parses, stages, or quarantines source-shaped material such as plant taxon references, herbarium records, occurrence observations, survey datasets, vegetation-community inputs, invasive-plant reports, and restoration-planting records.

It must not become plant truth, taxonomic authority, source descriptor authority, policy authority, schema authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Canonicality warning

This folder is a confirmed repo path, but its canonical role is still **NEEDS VERIFICATION**. Treat it as a connector-group index until Directory Rules, repo tree review, ADRs, or migration notes confirm whether flora connectors should live here or in source-first connector homes.

Do not add child connector lanes here merely because they are flora-related. First check source catalog references, source descriptors, existing connector paths, and placement guidance.

---

## Repo fit

```text
connectors/
└── flora/
    └── README.md
```

Related surfaces:

```text
docs/domains/flora/SOURCE_INTAKE.md
docs/domains/flora/SOURCE_FAMILIES.md
docs/domains/flora/SOURCE_REGISTRY.md
docs/sources/catalog/usda/usda-plants.md
docs/sources/catalog/kansas/ku-herbarium.md
docs/sources/catalog/eddmaps/README.md
data/registry/sources/flora/
data/raw/flora/
data/quarantine/flora/
```

---

## Authority boundary

```text
THIS GROUP MAY EXPLAIN:
  flora connector admission posture
  source-admission limits
  child connector responsibilities
  validation and rollback expectations
  open placement questions

THIS GROUP MUST NOT CONTAIN OR DECIDE:
  canonical flora records
  taxonomy authority
  source descriptor authority
  policy authority
  schemas
  processed records
  catalog or triplet records
  published records
  release decisions
```

Connectors may help retrieve or stage source material. They do not decide whether a record is true, taxonomy-settled, rights-cleared, review-complete, or ready for public release.

---

## Admission posture

Expected connector behavior:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a source descriptor or source activation decision;
- no implicit publication from retrieved records;
- no automatic conversion from source records to confirmed occurrence truth;
- no loss of source rights, license, attribution, uncertainty, or review metadata;
- unclear rights, source role, or taxonomic certainty routes to quarantine or abstention.

Connector output targets only:

```text
data/raw/flora/
data/quarantine/flora/
```

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- source descriptor references are required for live activation;
- identifiers, timestamps, retrieval metadata, taxon identifiers, uncertainty fields, source-role fields, and license fields are explicit where available;
- malformed or incomplete responses fail closed;
- records remain candidate evidence until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, or approved for committed use.

Root-level validation, policy-as-code, release gates, and EvidenceBundle closure remain outside this folder.

---

## Definition of done

This connector group is ready for first review when:

- [ ] Directory Rules and ADR review determine whether `connectors/flora/` is canonical, compatibility-only, or a migration target.
- [ ] Existing flora source connector homes under `connectors/` are inventoried.
- [ ] Child connector READMEs link to source catalog entries and source descriptors.
- [ ] Live access is disabled by default across child connectors.
- [ ] Credentials are excluded from source control.
- [ ] Per-record rights/license handling is documented before activation.
- [ ] Connector outputs are limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, empty, rights-unclear, review-required, and taxon-uncertain cases.
- [ ] Reviewers have a rollback path for connector activation and cached material.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve whether `connectors/flora/` is canonical or compatibility-only. | **NEEDS VERIFICATION** | Directory Rules, ADR, repo tree, and migration note. |
| Inventory existing flora source connector homes under `connectors/`. | **NEEDS VERIFICATION** | Repo tree and search results. |
| Confirm child connector test locations. | **NEEDS VERIFICATION** | Test tree and CI workflows. |
| Confirm source descriptor homes and source IDs for flora connectors. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm rights, attribution, and fixture handling. | **NEEDS VERIFICATION** | Source profiles, rights policy, and fixture review. |
| Confirm CI wiring for connector-local tests. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

Use this folder cautiously. If `connectors/flora/` remains in the repo, it should make flora connector boundaries more inspectable without becoming a parallel source hierarchy, policy engine, release path, or public truth surface.
