<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-habitat-readme
title: connectors/habitat/ — Habitat Connector Coordination Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Habitat steward · Flora steward · Fauna steward · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-18
updated: 2026-06-18
policy_label: public-doctrine; sensitivity-gated; rights-gated; no-publication
proposed_path: connectors/habitat/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector-family contract / UNKNOWN implementation depth
related:
  - ../README.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../docs/domains/habitat/SOURCE_REGISTRY/README.md
  - ../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../docs/domains/habitat/ARCHITECTURE.md
  - ../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../data/registry/sources/habitat/
  - ../../data/raw/habitat/
  - ../../data/quarantine/habitat/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/domains/habitat/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, habitat, ecology, source-admission, sensitivity, rare-species, rights, raw, quarantine, governance]
notes:
  - "This README fills a previously blank habitat connector-family README."
  - "Habitat source registry docs define source admission as an authority-control surface, not a bibliography, truth store, or publication path."
  - "Habitat connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, catalog/triplet projection, redaction/generalization, release, publication, correction, and rollback remain outside this folder."
  - "Rare-species, habitat, conservation, restoration, and sensitive-location material must fail closed until sensitivity, rights, source role, review, release class, and rollback path are verified."
  - "Implementation files, source activation, SourceDescriptor records, fixtures, tests, CI wiring, source inventory, and public-release classes remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Connector Coordination Lane

> Coordination README for habitat-related source-admission connectors.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Scope: source admission" src="https://img.shields.io/badge/scope-source__admission-blue">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
  <img alt="Rights: gated" src="https://img.shields.io/badge/rights-gated-orange">
  <img alt="Lifecycle: raw or quarantine only" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20only-orange">
</p>

`connectors/habitat/`

## Quick jumps

[Scope](#scope) · [Evidence basis](#evidence-basis) · [Authority boundary](#authority-boundary) · [Admission posture](#admission-posture) · [Sensitivity posture](#sensitivity-posture) · [Validation](#validation) · [Definition of done](#definition-of-done) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/habitat/` is the connector coordination lane for habitat source-intake and source-admission helpers.

It may contain connector-family documentation, compatibility routing, source-admission expectations, safe fixture rules, and links to source-specific connector homes for habitat material.

It must not become habitat truth, species-presence truth, restoration truth, conservation-status authority, source descriptor authority, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, pipeline authority, or publication authority.

---

## Evidence basis

Repo evidence checked for this update:

- `connectors/habitat/README.md` existed but was blank.
- `docs/domains/habitat/SOURCE_REGISTRY.md` defines the Habitat source registry as a human-facing admission and authority-control surface, not a bibliography, truth store, or publication path.
- The same registry describes source admission before connector activation and RAW capture before WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED lifecycle stages.
- Search results show habitat source ledger, source registry, source lifecycle, architecture, rare-species deny-by-default ADR, and related flora/fauna registries as relevant governance surfaces.

This README does not invent active sources, endpoints, credentials, rate limits, schemas, source IDs, source activation state, or public-release classes.

---

## Authority boundary

```text
OUTPUT LIMIT:
  data/raw/habitat/
  data/quarantine/habitat/

NOT HERE:
  habitat truth
  species-presence truth
  restoration success claims
  conservation-status authority
  precise sensitive-location publication
  source descriptor authority
  policy authority
  schema authority
  processed records
  catalog or triplet records
  published records
  release decisions
```

Connectors under this lane may help retrieve, parse, stage, or inspect habitat source material. They do not decide whether a habitat claim is evidence-complete, sensitivity-safe, rights-cleared, review-complete, public-safe, or publishable.

---

## Admission posture

Expected behavior for habitat connector work:

- no live network access unless explicitly enabled and reviewed;
- no source fetch without a SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no conversion of source rows into confirmed habitat, species, or restoration claims;
- no publication of precise sensitive locations from connector code;
- no loss of source product, publisher, retrieval, rights, vintage, geometry, uncertainty, source role, sensitivity, review, or release-class metadata;
- unclear rights, source role, habitat meaning, species association, location sensitivity, or schema drift routes to quarantine or abstention.

Recommended finite outcomes:

| Situation | Outcome |
|---|---|
| SourceDescriptor missing | `ABSTAIN` or connector error. |
| Live access not enabled | `ABSTAIN`; fixture-based tests still pass. |
| Product scope unclear | `NEEDS_VERIFICATION` or quarantine-safe output. |
| Rights or attribution unclear | `NEEDS_VERIFICATION`; no promotion. |
| Sensitive-location handling unclear | Quarantine or review-required result. |
| Species or habitat meaning unclear | Quarantine or review-required result. |
| Source response malformed | `ERROR` with safe metadata. |

---

## Sensitivity posture

Habitat connector work must default to restraint.

Minimum posture:

1. Preserve sensitivity metadata and uncertainty instead of normalizing it away.
2. Treat rare-species, critical-habitat, restoration, private-land, cultural, and infrastructure-adjacent joins as policy-significant until reviewed.
3. Prefer quarantine, redaction, generalization, staged access, delayed publication, or denial when sensitivity or rights are unclear.
4. Record any redaction or generalization as a downstream transform with a reason and receipt; do not hide transformation in connector code.
5. Treat maps, tiles, graphs, summaries, vector indexes, and AI-generated text as downstream carriers, not sovereign truth.

---

## Validation

Connector-local validation should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- product, publisher, rights, citation, retrieval, geometry, uncertainty, source-role, sensitivity, review, and vintage fields are explicit where available;
- malformed or incomplete responses fail closed;
- habitat records remain source-admission candidates until downstream validation;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores;
- fixture data is synthetic, minimized, redacted, or approved for committed use.

Root-level validation, policy-as-code, sensitivity review, redaction/generalization, release gates, EvidenceBundle closure, and rollback remain outside this connector family.

---

## Definition of done

This connector-family README is ready for first review when:

- [ ] Habitat source registry and source ledger are linked and current enough for review.
- [ ] Source-specific connector homes are inventoried without creating duplicate authority.
- [ ] SourceDescriptor homes and source IDs are verified for active habitat sources.
- [ ] Live access is disabled by default for connector code.
- [ ] Product, publisher, rights, citation, source role, geometry, uncertainty, sensitivity, review, and vintage metadata are preserved in parser output.
- [ ] Connector output is limited to RAW or QUARANTINE handoff.
- [ ] Sensitive-location publication is impossible from connector code.
- [ ] No public claims are created by connector code.
- [ ] Tests cover no-network, malformed, incomplete, rights-unclear, product-scope-unclear, schema-drift, sensitive-location, and rare-species-adjacent cases.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual habitat connector inventory below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm canonicality of `connectors/habitat/`. | **NEEDS VERIFICATION** | Directory Rules, ADR, migration note, or repo convention. |
| Confirm source descriptor homes and source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm source-specific access and parsing scope. | **NEEDS VERIFICATION** | Source steward review and connector implementation. |
| Confirm rights and redistribution posture. | **NEEDS VERIFICATION** | Rights review and terms snapshots. |
| Confirm sensitive-location and rare-species handling. | **NEEDS VERIFICATION** | Sensitivity policy and habitat/flora/fauna steward review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector family narrow. It should organize habitat source-admission work without becoming a source registry, habitat interpretation engine, species-location exposure path, restoration-claim authority, release path, or public truth surface.
