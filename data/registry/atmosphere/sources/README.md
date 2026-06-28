<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/atmosphere/sources/readme
name: Atmosphere Source Registry README
path: data/registry/atmosphere/sources/README.md
type: data-registry-domain-sources-readme
version: v0.2.0
status: draft
owners:
  - <atmosphere-source-steward>
  - <atmosphere-domain-steward>
  - <rights-reviewer>
  - <policy-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-source-descriptors
path_posture: existing-requested-path-replaced; registry-path-order-conflict-needs-verification; source-descriptor-instance-lane-not-source-payload-lane
safety_posture: advisory-and-operational-use-denied; source-role-and-freshness-required; public-output-blocked-until-evidence-policy-review-release
related:
  - ../../README.md
  - ../README.md
  - ../../../raw/atmosphere/README.md
  - ../../../work/atmosphere/README.md
  - ../../../quarantine/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../receipts/README.md
  - ../../../receipts/validation/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../data/registry/sources/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/SOURCES.md
  - ../../../../docs/domains/atmosphere/SOURCE_INDEX.md
  - ../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/atmosphere/
tags:
  - kfm
  - data
  - registry
  - atmosphere
  - sources
  - source-descriptor
  - source-role
  - knowledge-character
  - air
  - weather
  - smoke
  - climate
  - rights
  - sensitivity
  - stale-state
  - cite-or-abstain
notes:
  - "This README replaces the short placeholder at `data/registry/atmosphere/sources/README.md`."
  - "Atmosphere documentation points to `data/registry/sources/atmosphere/` as the machine-readable companion while this requested path exists as `data/registry/atmosphere/sources/`. The lane-order conflict remains NEEDS VERIFICATION until an ADR or registry migration resolves it."
  - "This directory is for source registry/source descriptor records only. It is not raw source data, not a receipt lane, not proof, not release, and not public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Registry

Source descriptor instance lane for Atmosphere/Air-domain source admission and activation records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry" src="https://img.shields.io/badge/root-data%2Fregistry-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-0aa">
  <img alt="Boundary: not public guidance" src="https://img.shields.io/badge/boundary-not%20public%20guidance-critical">
  <img alt="Path posture: needs verification" src="https://img.shields.io/badge/path-NEEDS%20VERIFICATION-orange">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Source descriptor boundary](#source-descriptor-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Source families](#source-families) · [Suggested descriptor fields](#suggested-descriptor-fields) · [Activation states](#activation-states) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/atmosphere/sources/` is a registry lane for Atmosphere source descriptor records and source activation posture. It is not raw source storage, not a bibliography, not a receipt lane, not proof, not release, not policy source, and not public Atmosphere truth.

---

## Scope

This directory is for Atmosphere-domain source registry records: compact, reviewable source descriptors that decide whether a source is admitted, restricted, quarantined, denied, retired, or pending review before any connector, watcher, pipeline, validator, AI surface, map layer, or release candidate may rely on it.

A source registry record should answer:

- What source family, publisher, agency, network, model provider, archive, or aggregator is being admitted?
- What stable source identity, knowledge character, and source role applies?
- What rights, attribution, redistribution, access, rate-limit, and terms posture applies?
- What sensitivity, public-release, caveat, confidence, stale-state, and advisory-use posture applies?
- What cadence, freshness, HTTP-validator, manifest-checksum, model-run, or watcher expectation applies?
- Which raw/work/quarantine/processed lanes may receive payloads from this source?
- Which policies, schemas, validators, receipts, proofs, catalog records, release gates, correction notices, and rollback targets must reference this descriptor?

This lane stores **registry control records**, not air-quality payloads, weather observations, climate grids, smoke rasters, model outputs, satellite scenes, or source-native files.

---

## Path posture

The requested and currently existing path is:

```text
data/registry/atmosphere/sources/
```

Atmosphere documentation and an existing scaffold also point to this alternate machine-registry pattern:

```text
data/registry/sources/atmosphere/
```

That is a real lane-order conflict. This README documents the existing requested path without resolving the conflict. Until accepted registry-layout governance, ADR review, or a migration note settles the convention, treat this path as **NEEDS VERIFICATION** for canonical placement while still using it safely as a README-controlled registry lane.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/registry/atmosphere/sources/` |
| Responsibility root | `data/` |
| Artifact family | registry |
| Domain lane | atmosphere |
| Record type | SourceDescriptor / SourceActivationDecision support |
| Human-facing source registry docs | `docs/domains/atmosphere/SOURCE_REGISTRY.md` and `docs/domains/atmosphere/SOURCES.md` |
| Alternate registry scaffold | `data/registry/sources/atmosphere/` |
| Schema authority | `schemas/contracts/v1/source/`, subject to accepted schema-home ADRs |
| Policy authority | `policy/domains/atmosphere/`, `policy/sensitivity/atmosphere/`, and cross-domain policy roots |
| Payload lanes | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/quarantine/atmosphere/`, `data/processed/atmosphere/`, and `data/published/` after release |
| Receipt authority | `data/receipts/`, not this registry lane |
| Proof authority | `data/proofs/`, not this registry lane |
| Catalog authority | `data/catalog/`, not this registry lane |
| Release authority | `release/`, not this registry lane |
| Public access posture | No direct public path. Public clients use governed APIs and released, policy-safe artifacts only. |

---

## Source descriptor boundary

| Rule | Handling |
|---|---|
| Registry is admission control | A descriptor controls whether a source may shape Atmosphere claims or candidate objects. |
| Descriptor is not source data | Source payloads go to lifecycle data lanes, not this directory. |
| Source role is fixed at admission | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be silently upgraded downstream. |
| Knowledge character is preserved | AQI, concentration, AOD, smoke mask, model field, forecast context, advisory context, and regulatory archive are not interchangeable. |
| Rights fail closed | Current terms, attribution, redistribution, API limits, key handling, and review obligations must resolve before activation. |
| Stale-state fails safe | Freshness and valid-time limits must be recorded so stale or lagged products are not presented as current truth. |
| Registry is not catalog | Discovery records such as STAC/DCAT/PROV belong under `data/catalog/`. |
| Registry is not proof | EvidenceBundle, ProofPack, citation validation, integrity proof, and model-run proof support belong under `data/proofs/` or the accepted proof lane. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, and signatures belong under `release/`. |

---

## Accepted material

Accepted content is limited to source-registry records and source-descriptor-local sidecars:

- one descriptor file per Atmosphere source family, agency feed, sensor network, regulatory archive, model product family, satellite product, controlled API, or aggregator;
- descriptor indexes that point to source descriptor records without becoming catalog or proof records;
- source identity, publisher, steward, access method, stable identifiers, endpoint references, model/product identifiers, version/cadence expectations, watcher strategy, stale-state rules, and activation posture;
- `source_role`, knowledge-character label, anti-collapse notes, and authority/candidate status;
- rights, attribution, redistribution, API terms, key-handling rules, rate-limit, and steward-review posture;
- sensitivity, public-release class, caveat/confidence requirements, quarantine triggers, and denial reasons;
- references to policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction notices, rollback targets, and review records;
- local README files that help stewards inspect registry posture without becoming source data, proof, catalog, release, policy, public output, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw atmosphere payloads, weather observations, climate grids, smoke rasters, model outputs, satellite scenes, downloaded packages, or source-native files | `data/raw/atmosphere/` or governed restricted storage; unresolved material goes to `data/quarantine/atmosphere/` |
| Work-in-progress transforms, scratch outputs, unresolved candidates, or derived experiments | `data/work/atmosphere/` |
| Processed Atmosphere objects or public-safe derivatives | `data/processed/atmosphere/` after gates; `data/published/` only after release |
| Source catalog profiles and human source documentation | `docs/sources/catalog/` and `docs/domains/atmosphere/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, model-run proof support, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or public catalog exports | `data/catalog/` |
| RunReceipt, validation receipt, redaction receipt, aggregation receipt, AI receipt, telemetry receipt, watcher receipt, or EventRunReceipt | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, release signature, or release changelog | `release/` |
| Policy source, Rego files, source-role policies, sensitivity policies, or access-control rules | `policy/` |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Connector code, watcher code, packages, fixtures, tests, or CI workflows | `connectors/`, `tools/`, `packages/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Source families

The human-facing Atmosphere source documents identify several source families and emphasize that rights/current terms remain **NEEDS VERIFICATION** and sensitive joins fail closed. This registry lane should hold machine-adjacent descriptors for admitted instances, not duplicate the full narrative register.

Starter descriptor filenames should use stable, lowercase slugs. Examples:

```text
data/registry/atmosphere/sources/
├── README.md
├── openaq-aggregators.source.json
├── epa-aqs.source.json
├── airnow-agency-reporting.source.json
├── cams-ecmwf-model-fields.source.json
├── hrrr-smoke-noaa.source.json
├── hms-smoke.source.json
├── goes-abi-aod.source.json
└── viirs-fire-hotspot.source.json
```

> [!NOTE]
> The filename examples are proposed registry hygiene. Do not treat them as proof that descriptor payloads already exist, that terms have been cleared, or that any Atmosphere source may be ingested.

---

## Suggested descriptor fields

The exact schema remains **NEEDS VERIFICATION** until accepted source descriptor schema evidence is checked. Atmosphere source descriptors should be structured enough for policy, validation, receipts, proof assembly, catalog closure, stale-state handling, correction, rollback, and release review.

| Field | Purpose |
|---|---|
| `id` | Stable source descriptor identity. |
| `source_family` | Source family name. |
| `publisher_or_authority` | Source publisher, agency, network, model provider, archive, or aggregator. |
| `source_role` | Primary source role at admission; must not be silently upgraded downstream. |
| `knowledge_character` | Observed sensor, public report, regulatory archive, model field, remote-sensing product, forecast context, advisory context, network/site context, or fusion product. |
| `domain` | `atmosphere`. |
| `access_method` | API, bulk download, feed, mirror, manual upload, public file, restricted endpoint, or connector strategy. |
| `endpoint_refs` | URLs, endpoint identifiers, product IDs, model run IDs, or archive refs, without secrets or access tokens. |
| `rights_posture` | Terms, attribution, redistribution, API limits, key handling, and access posture. |
| `freshness` | Cadence, retrieval expectations, stale-state rules, valid-time rules, HTTP validators, manifest checksum expectations, and source-vintage rules. |
| `geography` | Spatial scope, station/network scope, raster/grid scope, CRS expectations, and precision posture. |
| `time_support` | Observed/source/retrieval/valid/forecast/release/correction time expectations. |
| `policy_refs` | Relevant source, rights, sensitivity, stale-state, access, or release policies. |
| `schema_refs` | Source descriptor and domain schemas that apply. |
| `validator_refs` | Validators or fixture packs expected before activation. |
| `receipt_expectations` | Receipts expected from watchers, validators, transforms, model runs, review, or release dry runs. |
| `proof_requirements` | Evidence/proof/model-run closure required before claims or public layers depend on the source. |
| `activation_status` | Current finite state such as `candidate`, `active`, `restricted`, `quarantined`, `denied`, `retired`, or `superseded`. |
| `review_refs` | Steward, rights, sensitivity, policy, and release review references. |
| `correction_refs` | Correction, withdrawal, supersession, rollback, or revocation references when applicable. |

---

## Activation states

| State | Meaning | Allowed downstream use |
|---|---|---|
| `candidate` | Descriptor is being drafted or reviewed. | No ingestion beyond fixtures or controlled review. |
| `active` | Rights, source role, knowledge character, freshness, cadence, and policy posture are sufficiently resolved for governed intake. | Connector/watcher may emit to approved lifecycle lanes, subject to restrictions. |
| `restricted` | Source may be used only under named restrictions, terms, agreement, steward approval, or reviewer-only access. | Restricted processing only; no public release without additional gates. |
| `quarantined` | Source has unresolved rights, sensitivity, integrity, identity, terms, stale-state, or access risk. | No promotion; quarantine-only handling. |
| `denied` | Source must not shape KFM claims. | No intake or downstream use. |
| `retired` | Source is no longer active but historical references may remain. | Historical audit only; no new intake. |
| `superseded` | Source descriptor has been replaced by a newer descriptor. | Use successor for new work; preserve old descriptor for audit. |

---

## Required checks before use

- [ ] Confirm the descriptor belongs in the Atmosphere source registry lane and not in raw/work/quarantine/processed/published data.
- [ ] Resolve the lane-order conflict before treating this path as canonical across the repository.
- [ ] Confirm descriptor identity, publisher/authority, source family, access method, source role, and knowledge character.
- [ ] Confirm rights, attribution, redistribution, terms, API limits, key handling, access limits, and review obligations from current source documentation.
- [ ] Confirm freshness, stale-state, caveat/confidence, and official-source routing requirements where the source could be mistaken for current operational truth.
- [ ] Confirm watcher cadence, HTTP validators, valid-time rules, source-vintage rules, and correction/supersession handling.
- [ ] Confirm source role and knowledge character are preserved and not silently upgraded by validation, aggregation, modeling, AI interpretation, or promotion.
- [ ] Confirm policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction references, and rollback targets are referenced.
- [ ] Confirm no credentials, secrets, restricted identifiers, source payloads, or access tokens are stored in the descriptor README or local indexes.
- [ ] Confirm public clients and generated answer surfaces do not read this registry lane directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the short placeholder at `data/registry/atmosphere/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/atmosphere/README.md` exists but is still a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/atmosphere/README.md` exists as an alternate registry scaffold. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/atmosphere/aqs.source.json` exists as a PROPOSED placeholder. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere source-registry documentation exists at `docs/domains/atmosphere/SOURCE_REGISTRY.md`. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere source-family documentation exists at `docs/domains/atmosphere/SOURCES.md`. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere docs identify `data/registry/sources/atmosphere/` as the machine-readable companion while the requested path is `data/registry/atmosphere/sources/`. | CONFIRMED from repo documentation |
| Emitted source descriptor payloads exist in this requested folder. | UNKNOWN |
| The canonical machine schema for Atmosphere source descriptors is fully enforced. | NEEDS VERIFICATION |
| This README grants public access or activates any source. | DENY |

---

## Maintainer note

A source descriptor is the admission control record for a source. In Atmosphere, admission is inseparable from source role, knowledge character, rights, freshness, stale-state, caveat/confidence, and policy posture. Keep the chain explicit:

```text
source descriptor -> governed intake or quarantine -> receipt -> proof/review/catalog/release checks -> governed public-safe surface
```

Never collapse it into:

```text
source descriptor -> public Atmosphere truth
```
