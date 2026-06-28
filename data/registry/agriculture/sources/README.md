<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/agriculture/sources/readme
name: Agriculture Source Registry README
path: data/registry/agriculture/sources/README.md
type: data-registry-domain-sources-readme
version: v0.2.0
status: draft
owners:
  - <source-registry-steward>
  - <agriculture-domain-steward>
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
registry_scope: agriculture-source-descriptors
path_posture: existing-requested-path-replaced; naming-conflict-needs-verification; source-descriptor-instance-lane-not-source-payload-lane
sensitivity_posture: registry-internal; aggregate-or-permissioned-public-posture; field-level-and-private-operator-data-fail-closed; rights-and-source-terms-required-before-activation
related:
  - ../../README.md
  - ../../../raw/agriculture/README.md
  - ../../../work/agriculture/README.md
  - ../../../quarantine/agriculture/README.md
  - ../../../processed/agriculture/README.md
  - ../../../receipts/README.md
  - ../../../receipts/validation/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/SOURCES.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/agriculture/
tags:
  - kfm
  - data
  - registry
  - agriculture
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - activation
  - quarantine
  - cite-or-abstain
notes:
  - "This README replaces the short placeholder at `data/registry/agriculture/sources/README.md`."
  - "Agriculture documentation names source registry paths using multiple patterns: `data/registry/sources/agriculture/`, `data/registry/source_descriptors/agriculture/`, and this existing requested path. The lane-order conflict remains NEEDS VERIFICATION until an ADR or registry migration resolves it."
  - "This directory is for source registry/source descriptor records only. It is not raw source data, not a source catalog profile, not a receipt lane, not proof, not release, and not public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Source Registry

Source descriptor instance lane for Agriculture-domain source admission and activation records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry" src="https://img.shields.io/badge/root-data%2Fregistry-blue">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Boundary: not raw data" src="https://img.shields.io/badge/boundary-not%20raw%20data-critical">
  <img alt="Path posture: needs verification" src="https://img.shields.io/badge/path-NEEDS%20VERIFICATION-orange">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Source descriptor boundary](#source-descriptor-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Source families](#source-families) · [Suggested descriptor fields](#suggested-descriptor-fields) · [Activation states](#activation-states) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/agriculture/sources/` is a registry lane for Agriculture source descriptor records and activation posture. It is not raw source storage, not a bibliography, not a source catalog profile, not a receipt lane, not a proof pack, not a release manifest, and not public Agriculture truth.

---

## Scope

This directory is for Agriculture-domain source registry records: compact, reviewable source descriptors that decide whether a source is admitted, restricted, quarantined, denied, retired, or pending review before any connector, watcher, pipeline, validator, or release candidate may rely on it.

A source registry record should answer:

- What source family or publisher is being admitted?
- What stable source identity is being used?
- What `source_role` applies at admission?
- What rights, license, attribution, redistribution, access, and terms posture applies?
- What sensitivity and public-release posture applies?
- What cadence, freshness, stale-state, and watcher expectations apply?
- Which steward owns review and revalidation?
- Which raw/work/quarantine/processed lanes may receive payloads from this source?
- Which policies, schemas, validators, receipts, proofs, catalog records, and release gates must reference this descriptor?

This lane stores **registry control records**, not the acquired source payloads themselves.

---

## Path posture

The requested and currently existing path is:

```text
data/registry/agriculture/sources/
```

Agriculture documentation also points to these alternative patterns:

```text
data/registry/sources/agriculture/
data/registry/source_descriptors/agriculture/
```

That is a real naming/order conflict. This README documents the existing requested path without resolving the conflict. Until accepted registry-layout governance or an ADR settles the convention, treat this path as **NEEDS VERIFICATION** for canonical placement while still using it safely as a local README-controlled registry lane.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/registry/agriculture/sources/` |
| Responsibility root | `data/` |
| Artifact family | registry |
| Domain lane | agriculture |
| Record type | SourceDescriptor / source activation record |
| Human-facing source registry docs | `docs/domains/agriculture/SOURCE_REGISTRY.md` and `docs/domains/agriculture/SOURCES.md` |
| Cross-domain authority register | `docs/registers/SOURCE_AUTHORITY.md` and `control_plane/source_authority_register.yaml`, where accepted |
| Schema authority | `schemas/contracts/v1/source/`, subject to accepted schema-home ADRs |
| Policy authority | `policy/domains/agriculture/`, `policy/sensitivity/agriculture/`, and cross-domain policy roots |
| Payload lanes | `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, `data/processed/agriculture/`, and `data/published/` after release |
| Receipt authority | `data/receipts/`, not this registry lane |
| Proof authority | `data/proofs/`, not this registry lane |
| Catalog authority | `data/catalog/`, not this registry lane |
| Release authority | `release/`, not this registry lane |
| Public access posture | No direct public path. Public clients use governed APIs and released artifacts. |

---

## Source descriptor boundary

| Rule | Handling |
|---|---|
| Registry is admission control | A descriptor controls whether a source may shape Agriculture claims. |
| Descriptor is not source data | Source payloads go to lifecycle data lanes, not this directory. |
| Source role is preserved | A modeled product does not become observed truth because validation or promotion succeeds. |
| Rights fail closed | Current terms, license, attribution, redistribution, API rules, and access constraints must be resolved before activation. |
| Sensitivity fail closed | Field-level, private operator, proprietary yield, pesticide, private-land, restricted, or sensitive joins are denied, quarantined, generalized, or permissioned unless policy says otherwise. |
| Registry is not catalog | Discovery records such as STAC/DCAT/PROV belong under `data/catalog/`. |
| Registry is not proof | EvidenceBundle, ProofPack, citation validation, and integrity proof belong under `data/proofs/`. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, and signatures belong under `release/`. |

---

## Accepted material

Accepted content is limited to source-registry records and source-descriptor-local sidecars:

- one descriptor file per Agriculture source family, publisher feed, API, dataset family, or controlled source endpoint;
- descriptor indexes that point to source descriptor records without becoming catalog or proof records;
- source identity, publisher, maintainer, access method, URL/API endpoint references, stable identifiers, version/cadence expectations, watcher strategy, and stale-state rules;
- `source_role` and anti-collapse notes;
- rights, license, attribution, redistribution, terms, access, rate-limit, and steward-review posture;
- sensitivity, public-release class, field-level/private-operator restrictions, aggregation requirements, redaction requirements, and quarantine triggers;
- references to policies, schemas, validators, receipts, proof requirements, catalog expectations, and release gates;
- local README files that help stewards inspect registry posture without becoming source data, proof, catalog, release, or public truth.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Agriculture source payloads, downloaded files, API responses, raster/vector data, station records, private field records, proprietary yield data, pesticide records, or source-native packages | `data/raw/agriculture/` or governed restricted storage; unresolved/sensitive records go to `data/quarantine/agriculture/` |
| Work-in-progress transforms, scratch outputs, unresolved candidates, or derived experiments | `data/work/agriculture/` |
| Processed Agriculture objects or public-safe derivatives | `data/processed/agriculture/` after gates; `data/published/` only after release |
| Source catalog profiles and human source documentation | `docs/sources/catalog/` and `docs/domains/agriculture/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or public catalog exports | `data/catalog/` |
| RunReceipt, validation receipt, redaction receipt, aggregation receipt, AI receipt, telemetry receipt, or watcher receipt | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, release signature, or release changelog | `release/` |
| Policy source, Rego files, source-role policies, sensitivity policies, or access-control rules | `policy/` |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Connector code, watcher code, packages, fixtures, tests, or CI workflows | `connectors/`, `tools/`, `packages/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Source families

The human-facing Agriculture source documents state that Agriculture admits a bounded set of source families and that rights, endpoints, terms, and cadence remain **NEEDS VERIFICATION** before ingestion. This registry lane should hold the machine-adjacent descriptors for those admitted families, not duplicate the full narrative register.

Starter descriptor filenames should use stable, lowercase slugs. Examples:

```text
data/registry/agriculture/sources/
├── README.md
├── usda-nrcs-ssurgo.source.json
├── usda-nrcs-gssurgo.source.json
├── kansas-mesonet.source.json
├── usda-nrcs-scan.source.json
├── noaa-uscrn.source.json
├── nasa-smap.source.json
├── nasa-hls.source.json
└── usda-nass-cdl.source.json
```

> [!NOTE]
> The filename examples are proposed registry hygiene. Do not treat them as proof that descriptor payloads already exist or that terms have been cleared.

---

## Suggested descriptor fields

The exact schema remains **NEEDS VERIFICATION** until accepted source descriptor schema evidence is checked. Agriculture source descriptors should be structured enough for policy, validation, receipts, proof assembly, catalog closure, and release review.

| Field | Purpose |
|---|---|
| `id` | Stable source descriptor identity. |
| `source_family` | Human-readable source family name. |
| `publisher` | Source publisher or responsible institution. |
| `source_role` | Primary source role at admission; must not be silently upgraded downstream. |
| `secondary_roles` | Permitted secondary roles, if any. |
| `domain` | `agriculture`. |
| `access_method` | API, bulk download, manual upload, mirror, or connector strategy. |
| `endpoint_refs` | URLs or endpoint identifiers, without secrets. |
| `rights_posture` | License, terms, redistribution, attribution, rate-limit, and access notes. |
| `sensitivity_posture` | Field-level, private operator, proprietary, restricted, aggregate-only, or public-safe posture. |
| `freshness` | Cadence, retrieval expectations, stale-state rules, and watcher strategy. |
| `geography` | Spatial scope, CRS expectations, geometry precision, and Kansas relevance. |
| `time_support` | Observed/source/retrieval/valid/release time expectations. |
| `policy_refs` | Relevant source, rights, sensitivity, geoprivacy, or release policies. |
| `schema_refs` | Source descriptor and domain schemas that apply. |
| `validator_refs` | Validators or fixture packs expected before activation. |
| `receipt_expectations` | Receipts expected from watchers, validators, redactors, transforms, or release dry runs. |
| `proof_requirements` | Evidence/proof closure required before claims or public layers depend on the source. |
| `activation_status` | Current finite state such as `candidate`, `active`, `restricted`, `quarantined`, `denied`, `retired`, or `superseded`. |
| `review_refs` | Steward, rights, sensitivity, policy, and release review references. |
| `correction_refs` | Correction, withdrawal, supersession, or rollback references when applicable. |

---

## Activation states

| State | Meaning | Allowed downstream use |
|---|---|---|
| `candidate` | Descriptor is being drafted or reviewed. | No ingestion beyond fixtures or controlled review. |
| `active` | Rights, role, sensitivity, cadence, and policy posture are sufficiently resolved for governed intake. | Connector/watcher may emit to approved lifecycle lanes. |
| `restricted` | Source may be used only under named restrictions, agreement, or reviewer-only access. | Restricted processing only; no public release without additional gates. |
| `quarantined` | Source has unresolved rights, sensitivity, integrity, identity, or terms risk. | No promotion; quarantine-only handling. |
| `denied` | Source must not shape KFM claims. | No intake or downstream use. |
| `retired` | Source is no longer active but historical references may remain. | Historical audit only; no new intake. |
| `superseded` | Source descriptor has been replaced by a newer descriptor. | Use successor for new work; preserve old descriptor for audit. |

---

## Required checks before use

- [ ] Confirm the descriptor belongs in the Agriculture source registry lane and not in raw/work/quarantine/processed/published data.
- [ ] Resolve the lane-order conflict before treating this path as canonical across the repository.
- [ ] Confirm descriptor identity, publisher, source family, access method, and source role.
- [ ] Confirm rights, license, attribution, redistribution, terms, access limits, rate limits, and review obligations from current publisher documentation.
- [ ] Confirm sensitivity posture, including field-level/private-operator restrictions, proprietary data, pesticide records, private-land joins, and aggregate-only release constraints.
- [ ] Confirm watcher cadence, freshness, stale-state rules, and correction/supersession handling.
- [ ] Confirm source role is preserved and not silently upgraded by validation, aggregation, modeling, or promotion.
- [ ] Confirm policies, schemas, validators, receipts, proof requirements, catalog expectations, and release gates are referenced.
- [ ] Confirm no credentials, tokens, private operator details, restricted identifiers, exact sensitive geometry, or source payloads are stored in the descriptor README or local indexes.
- [ ] Confirm public clients do not read this registry lane directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the short placeholder at `data/registry/agriculture/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists but is still a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Agriculture source-registry documentation exists at `docs/domains/agriculture/SOURCE_REGISTRY.md`. | CONFIRMED by GitHub contents API during this edit |
| Agriculture source-family documentation exists at `docs/domains/agriculture/SOURCES.md`. | CONFIRMED by GitHub contents API during this edit |
| Agriculture docs identify a registry path conflict between `sources/` and `source_descriptors/` patterns. | CONFIRMED from repo documentation |
| Emitted source descriptor payloads exist in this folder. | UNKNOWN |
| The canonical machine schema for Agriculture source descriptors is fully enforced. | NEEDS VERIFICATION |
| This README grants public access or activates any source. | DENY |

---

## Maintainer note

A source descriptor is the admission control record for a source. It can let a connector run, block a source, quarantine material, or support later receipts and proofs. It is not the source payload and it is not public truth.

Keep the chain explicit:

```text
source descriptor -> governed intake -> receipt -> proof/catalog/release checks -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Agriculture truth
```
