<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/agriculture/readme
name: Agriculture Registry README
path: data/registry/agriculture/README.md
type: data-registry-domain-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
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
registry_scope: agriculture-domain-registry-parent
path_posture: existing-parent-stub-replaced; child-sources-lane-confirmed; registry-path-order-conflict-needs-verification
sensitivity_posture: registry-internal; aggregate-or-permissioned-public-posture; field-level-and-private-operator-data-fail-closed; rights-and-source-terms-required-before-activation
related:
  - ../README.md
  - sources/README.md
  - ../../raw/agriculture/README.md
  - ../../work/agriculture/README.md
  - ../../quarantine/agriculture/README.md
  - ../../processed/agriculture/README.md
  - ../../receipts/README.md
  - ../../receipts/validation/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/agriculture/LIFECYCLE.md
  - ../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/architecture/source-roles.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/agriculture/
tags:
  - kfm
  - data
  - registry
  - agriculture
  - source-descriptor
  - source-role
  - admission-control
  - rights
  - sensitivity
  - activation
  - quarantine
  - cite-or-abstain
notes:
  - "This README replaces the greenfield stub at `data/registry/agriculture/README.md`."
  - "The confirmed child lane during this edit is `sources/`."
  - "Agriculture source-registry docs show a path-order conflict among `data/registry/agriculture/sources/`, `data/registry/sources/agriculture/`, and `data/registry/source_descriptors/agriculture/`. This README documents the existing parent lane without resolving that conflict."
  - "This directory is for Agriculture registry records and local routing documentation only. It is not raw source data, receipts, proofs, catalog output, release state, policy source, or public Agriculture truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Registry

Domain parent lane for Agriculture registry records and source-admission routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry" src="https://img.shields.io/badge/root-data%2Fregistry-blue">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Boundary: not raw data" src="https://img.shields.io/badge/boundary-not%20raw%20data-critical">
  <img alt="Path posture: needs verification" src="https://img.shields.io/badge/path-NEEDS%20VERIFICATION-orange">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Registry boundary](#registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/agriculture/` is a registry parent lane. It may route Agriculture source descriptors and future Agriculture registry records, but it is not raw source storage, not a source catalog profile, not a receipt lane, not proof, not release, not policy source, and not public Agriculture truth.

---

## Scope

This directory is the Agriculture-domain parent lane under `data/registry/`. It exists to organize registry records that control whether Agriculture sources, descriptors, authorities, activation states, and related domain registry objects may shape downstream KFM work.

At this maturity level, the confirmed child lane is:

```text
data/registry/agriculture/sources/
```

That child lane is for Agriculture source descriptor and activation records. This parent README routes maintainers to the correct responsibility homes and prevents registry material from being confused with raw payloads, proofs, catalogs, receipts, release decisions, or public artifacts.

A registry record in this branch should help answer:

- Which Agriculture source or registry object is being admitted or controlled?
- What stable identity and source role applies?
- What rights, access, license, attribution, redistribution, cadence, and stale-state posture applies?
- What sensitivity and public-release posture applies?
- Which policies, schemas, validators, receipts, proofs, catalogs, release gates, corrections, and rollback hooks must reference the registry record?
- What is the current finite activation state: candidate, active, restricted, quarantined, denied, retired, or superseded?

---

## Path posture

The requested and currently existing parent path is:

```text
data/registry/agriculture/
```

The confirmed child path is:

```text
data/registry/agriculture/sources/
```

Agriculture documentation also points to competing registry path patterns:

```text
data/registry/sources/agriculture/
data/registry/source_descriptors/agriculture/
```

This is an unresolved path-order conflict. This README documents the existing requested parent lane and its confirmed child lane without declaring final canonical placement. Treat this branch as **NEEDS VERIFICATION** for canonical registry layout until an ADR, migration note, or accepted Directory Rules update resolves the registry ordering convention.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/registry/agriculture/` |
| Responsibility root | `data/` |
| Artifact family | registry |
| Domain lane | agriculture |
| Confirmed child lane | `sources/` |
| Current child purpose | SourceDescriptor / source activation records |
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

## Confirmed child lanes

The child lane below was confirmed by a current GitHub read while replacing this parent stub. This confirms README/path evidence only. It does **not** prove emitted descriptor payloads, canonical schema enforcement, validators, fixtures, CI enforcement, policy enforcement, connector activation, release integration, correction hooks, rollback hooks, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Agriculture source descriptor and activation records for source admission, source-role preservation, rights posture, sensitivity posture, cadence, stale-state, and downstream gate references. | Not raw source data, not receipts, not proofs, not catalog records, not release manifests, not policy source, and not public Agriculture truth. |

---

## Registry boundary

| Rule | Handling |
|---|---|
| Registry is admission control | It controls whether sources and registry objects may shape downstream Agriculture work. |
| Registry is not source data | Acquired payloads go to lifecycle data lanes, not this directory. |
| Registry is not documentation-only | Human-facing docs explain; registry records should be machine-adjacent and gateable. |
| Source role is preserved | A modeled product does not become observed truth because validation, aggregation, or promotion succeeds. |
| Rights fail closed | Current terms, license, attribution, redistribution, access constraints, and review obligations must resolve before activation. |
| Sensitivity fails closed | Field-level, private operator, proprietary yield, pesticide, private-land, restricted, or sensitive joins are denied, quarantined, generalized, or permissioned unless policy says otherwise. |
| Registry is not receipt | Run, validation, redaction, telemetry, AI, aggregation, correction, rollback, and release-support receipts live under `data/receipts/`. |
| Registry is not proof | EvidenceBundle, ProofPack, citation validation, and integrity proof live under `data/proofs/`. |
| Registry is not catalog | Discovery records such as STAC/DCAT/PROV live under `data/catalog/`. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, and signatures live under `release/`. |

---

## Accepted material

Accepted content is limited to Agriculture registry records and registry-local sidecars:

- README files that route Agriculture registry material without becoming source truth;
- source descriptor records under the confirmed `sources/` child lane;
- local registry indexes that point to source descriptors without becoming catalog or proof records;
- source identity, publisher, maintainer, access method, stable identifiers, endpoint references, version/cadence expectations, watcher strategy, stale-state rules, and activation posture;
- `source_role` and anti-collapse notes;
- rights, license, attribution, redistribution, terms, access, rate-limit, and steward-review posture;
- sensitivity, public-release class, field-level/private-operator restrictions, aggregation requirements, redaction requirements, and quarantine triggers;
- references to policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction notices, and rollback targets.

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

## Suggested directory shape

The following map is documentation guidance, not proof that payloads exist beyond the README paths verified in this edit.

```text
data/registry/agriculture/
├── README.md
├── sources/
│   ├── README.md
│   ├── usda-nrcs-ssurgo.source.json
│   ├── usda-nrcs-gssurgo.source.json
│   ├── kansas-mesonet.source.json
│   ├── usda-nrcs-scan.source.json
│   ├── noaa-uscrn.source.json
│   ├── nasa-smap.source.json
│   ├── nasa-hls.source.json
│   └── usda-nass-cdl.source.json
└── index.local.json
```

`index.local.json` is optional and registry-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, source truth, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the registry record belongs in the Agriculture registry lane and not in raw/work/quarantine/processed/published data.
- [ ] Resolve the registry path-order conflict before treating this path as canonical across the repository.
- [ ] Confirm descriptor identity, publisher, source family, access method, and source role.
- [ ] Confirm rights, license, attribution, redistribution, terms, access limits, rate limits, and review obligations from current publisher documentation.
- [ ] Confirm sensitivity posture, including field-level/private-operator restrictions, proprietary data, pesticide records, private-land joins, and aggregate-only release constraints.
- [ ] Confirm watcher cadence, freshness, stale-state rules, and correction/supersession handling.
- [ ] Confirm source role is preserved and not silently upgraded by validation, aggregation, modeling, or promotion.
- [ ] Confirm policies, schemas, validators, receipts, proof requirements, catalog expectations, and release gates are referenced.
- [ ] Confirm no credentials, tokens, private operator details, restricted identifiers, exact sensitive geometry, or source payloads are stored in README or local indexes.
- [ ] Confirm public clients do not read this registry lane directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/agriculture/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/agriculture/sources/README.md` exists and defines the Agriculture source descriptor child lane. | CONFIRMED by GitHub contents API during this edit |
| Agriculture source-registry documentation exists at `docs/domains/agriculture/SOURCE_REGISTRY.md`. | CONFIRMED by GitHub contents API during this edit |
| Agriculture source-family documentation exists at `docs/domains/agriculture/SOURCES.md`. | CONFIRMED by GitHub contents API during this edit |
| Agriculture docs identify a registry path conflict between `sources/` and `source_descriptors/` patterns. | CONFIRMED from repo documentation |
| Emitted source descriptor payloads exist under this parent lane. | UNKNOWN |
| The canonical machine schema for Agriculture source descriptors is fully enforced. | NEEDS VERIFICATION |
| This README grants public access or activates any source. | DENY |

---

## Maintainer note

This parent lane keeps Agriculture registry material organized without turning registry records into data, receipts, proofs, catalog records, release decisions, or public truth. Keep the chain explicit:

```text
registry record -> governed intake -> receipt -> proof/catalog/release checks -> governed public surface
```

Never collapse it into:

```text
registry record -> public Agriculture truth
```
