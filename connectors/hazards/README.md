<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-hazards-readme
title: connectors/hazards/ — Hazards Connector Coordination Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Hazards steward · Release safety reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; not-life-safety; rights-and-sensitivity-gated; no-publication
proposed_path: connectors/hazards/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-family contract / CANONICALITY NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../docs/domains/hazards/SOURCES.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../docs/runbooks/hazards/SOURCE_REFRESH_RUNBOOK.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/hazards/
  - ../../data/raw/hazards/
  - ../../data/quarantine/hazards/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/domains/hazards/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, hazards, source-admission, noaa, fema, usgs, kansas, boundary, raw, quarantine, governance]
notes:
  - "This README fills a previously blank hazards connector-family README."
  - "Hazards source-registry docs define the hazards registry as an admission/control surface, not a public safety service, truth store, bibliography, or publication authority."
  - "Visible hazards docs describe connectors as authority-clustered under source families such as noaa/, fema/, usgs/, nasa/, and kansas/; connectors/hazards/ should coordinate boundaries, not replace source-family homes."
  - "Hazards connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
  - "Implementation files, source activation, SourceDescriptor records, fixtures, tests, CI wiring, source inventory, boundary controls, and public-release classes remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Connector Coordination Lane

> Coordination README for hazards-related source-admission connectors. Not a public safety service.

`connectors/hazards/`

## Scope

`connectors/hazards/` is a proposed coordination lane for hazards-related source-admission connectors.

It may document connector-family boundaries, compatibility routing, source-admission expectations, safe fixture rules, and links to source-specific connector homes.

It must not become a current-conditions service, public safety service, forecast authority, hazard truth store, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Evidence basis

Repo evidence checked for this update:

- `connectors/hazards/README.md` existed but was blank.
- `docs/domains/hazards/SOURCE_REGISTRY.md` defines the Hazards source registry as a human-facing admission and authority-control surface, not a public safety service, bibliography, truth store, or publication authority.
- The registry shows connectors as authority-clustered under source-family folders such as `noaa/`, `fema/`, `usgs/`, `nasa/`, and `kansas/`.

This README does not invent active sources, endpoints, credentials, rate limits, schemas, source IDs, source activation state, or public-release classes.

---

## Placement warning

The hazards registry describes connector organization as source-family or authority-clustered. Therefore, `connectors/hazards/` should be treated as a coordination or compatibility lane unless Directory Rules, an ADR, a migration note, or repo convention confirms it as an implementation home.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/hazards/
  data/quarantine/hazards/

NOT HERE:
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

Connectors under this lane may help retrieve, parse, stage, or inspect hazard source material. They do not decide whether a hazard claim is current, official, actionable, sensitivity-safe, rights-cleared, review-complete, public-safe, or publishable.

---

## Admission posture

Expected behavior for hazards connector work:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no conversion of source rows into confirmed hazard truth;
- no loss of source product, publisher, retrieval, rights, vintage, geometry, uncertainty, source role, validity window, review, or release-class metadata;
- unclear rights, source role, time validity, hazard meaning, location sensitivity, or schema drift routes to quarantine or abstention.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- product, publisher, issuing authority, rights, citation, retrieval, geometry, uncertainty, source-role, validity window, review, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- hazard records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, release review, EvidenceBundle closure, public caveats, official-source routing, and rollback remain outside this connector family.

---

## Definition of done

This connector-family README is ready for first review when:

- [ ] Hazards source registry and source role matrix are linked and current enough for review.
- [ ] Source-specific connector homes are inventoried without creating duplicate authority.
- [ ] SourceDescriptor homes and source IDs are verified for active hazards sources.
- [ ] Live access is disabled by default for connector code.
- [ ] Product, publisher, issuing authority, rights, citation, source role, geometry, uncertainty, validity window, review, and vintage metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, rights-unclear, product-scope-unclear, time-validity-unclear, schema-drift, and boundary cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual hazards connector inventory below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonicality of `connectors/hazards/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm relationship to authority-clustered connector homes. | **NEEDS VERIFICATION** | Repo tree and migration note. |
| Confirm source descriptor homes and source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm source-specific access and parsing scope. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm rights, sensitivity, and release-review posture. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and release review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector family narrow. It should coordinate hazards source-admission work without becoming a current-conditions service, forecast authority, hazard truth store, release path, or public safety surface.
