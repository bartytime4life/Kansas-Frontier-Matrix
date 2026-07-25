<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-catalog-domain-agriculture-readme
title: data/catalog/domain/agriculture/README.md — Agriculture Domain Catalog README
version: v0.2.0
type: readme; data-lifecycle-sublane; domain-catalog-guide; authority-boundary
status: repository-grounded draft; README-only; canonical CATALOG sublane; release-gated; implementation-unverified
owners: NEEDS VERIFICATION — default GitHub review route is @bartytime4life; Agriculture, data, catalog, evidence, policy, release, schema, correction, rollback, and docs stewardship assignments remain unverified
created: NEEDS VERIFICATION — historical blank placeholder predates v0.1
updated: 2026-07-24
policy_label: public-doc; catalog-carrier; no-direct-public-path; release-gated; aggregation-aware; cite-or-abstain
tags: [kfm, data, catalog, agriculture, domain-catalog, CATALOG, TRIPLET, EvidenceBundle, AggregationReceipt, ReleaseManifest, CatalogMatrix]
related:
  - ../../README.md
  - ../../../../catalog/README.md
  - ../../../../catalog/domain/agriculture/README.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../processed/agriculture/README.md
  - ../../../proofs/agriculture/README.md
  - ../../../rollback/agriculture/README.md
  - ../../../published/layers/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/catalog/README.md
  - ../../../../tests/domains/agriculture/catalog_closure/README.md
  - ../../../../release/README.md
  - ../../../../.github/CODEOWNERS
notes:
  - "v0.2.0 modernizes the substantive v0.1 lane guide; it does not replace a blank file."
  - "The exact target path is confirmed and matches the canonical data-catalog/domain pattern in the supplied Directory Rules."
  - "The bounded lane inventory found this README only; concrete catalog records and operational enforcement are not established."
  - "The top-level catalog/domain/agriculture compatibility README contains unresolved merge-conflict markers and remains non-authoritative."
  - "This Markdown-only revision does not create catalog records, accept ADR-0022, validate closure, approve release, publish data, or change runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/catalog/domain/agriculture/` — Agriculture domain catalog

> Governed Agriculture discovery and interoperability projections at the `CATALOG / TRIPLET` lifecycle stage—never Agriculture source truth, release authority, or a direct public data service.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status-and-authority)
[![Maturity: README only](https://img.shields.io/badge/maturity-README--only-d4a72c?style=flat-square)](#current-maturity)
[![Lifecycle: CATALOG](https://img.shields.io/badge/lifecycle-CATALOG-8250df?style=flat-square)](#lifecycle-boundary)
[![Exposure: release gated](https://img.shields.io/badge/exposure-release--gated-b42318?style=flat-square)](#lifecycle-boundary)
[![Aggregation: load bearing](https://img.shields.io/badge/aggregation-load--bearing-0969da?style=flat-square)](#aggregation-and-sensitivity-guardrails)

> [!IMPORTANT]
> Catalog presence is not publication. A record in this lane remains internal or candidate state unless evidence, rights, sensitivity, validation, policy, accountable review, an immutable release decision, correction support, and a rollback target close for its intended use.

**Path:** `data/catalog/domain/agriculture/README.md`  
**Owning root:** `data/catalog/`  
**Responsibility:** Agriculture-domain catalog carrier  
**Lifecycle phase:** `CATALOG / TRIPLET`  
**Current maturity:** `README_ONLY`  
**Public posture:** no direct public path; released, policy-allowed carriers only through governed interfaces  
**Truth posture:** **CONFIRMED** exact path, canonical responsibility root, README-only bounded inventory, parent catalog boundary, and linked documentation surfaces; **PROPOSED** record profile and closure workflow; **UNKNOWN / NEEDS VERIFICATION** concrete records, accepted schemas, executable validators, fixtures, closure tests, release linkage, runtime consumers, and public-route enforcement.

**Quick navigation:** [Purpose](#purpose) · [Status and authority](#status-and-authority) · [Lifecycle](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Contents](#accepted-contents) · [Exclusions](#exclusions) · [Maturity](#current-maturity) · [Workflow](#authoring-and-promotion-workflow) · [Requirements](#agriculture-catalog-requirements) · [Guardrails](#aggregation-and-sensitivity-guardrails) · [Evidence](#evidence-ledger) · [Validation](#validation-checklist) · [Review](#review-and-maintenance) · [Rollback](#rollback)

---

## Purpose

`data/catalog/domain/agriculture/` is the canonical Agriculture-domain sublane under the governed `data/catalog/` responsibility root. It is intended to carry discovery records, indexes, release-linked subsets, and cross-vocabulary references derived from processed Agriculture records.

This lane may describe objects such as crop observations, field candidates, rotations, yield observations, irrigation links, conservation practices, soil-crop suitability, agricultural-economy observations, supply-chain nodes, stress indicators, and aggregate products—but only when an accepted contract and admissible evidence support that description.

A catalog record helps people and systems find, compare, review, and close a candidate. It cannot make a claim true, upgrade a source role, satisfy evidence by description, clear rights, authorize precision, approve a release, or publish an artifact.

## Status and authority

| Question | Current answer |
|---|---|
| Is this the canonical Agriculture domain-catalog path? | **CONFIRMED.** The exact path exists, the parent `data/catalog/` README identifies catalog as the canonical CATALOG responsibility, and the supplied Directory Rules places domain catalog material at `data/catalog/domain/<domain>/`. |
| Does this README define object meaning, machine shape, policy, or release state? | **No.** Those authorities remain in their governed contract, schema, policy, evidence, and release roots. |
| Does `catalog/domain/agriculture/` have equal authority? | **No.** Its parent documents the top-level `catalog/` root as non-authoritative compatibility drift. Its child README currently contains unresolved merge-conflict markers; that defect is recorded here but is outside this one-file change. |
| Are Agriculture catalog payloads established here? | **UNKNOWN / NOT ESTABLISHED.** The bounded repository search found this README, not a concrete record inventory. |
| Is ADR-0022 accepted? | **No claim.** The inspected ADR is `proposed`; its STAC/DCAT/PROV agreement model is design input, not accepted migration or release authority. |
| Does CODEOWNERS prove stewardship or approval? | **No.** `@bartytime4life` is the confirmed default GitHub review route; stewardship, accountable review, and separation of duties remain **NEEDS VERIFICATION**. |

## Lifecycle boundary

~~~mermaid
flowchart LR
  RAW["RAW<br/>source capture"] --> WORK["WORK"]
  WORK -->|admissible| PROCESSED["PROCESSED"]
  WORK -->|failed or sensitive| QUARANTINE["QUARANTINE"]
  PROCESSED --> CATALOG["CATALOG<br/>domain and standards projections"]
  PROCESSED --> TRIPLET["TRIPLET<br/>relationship projections"]
  CATALOG --> REVIEW{"Evidence, policy,<br/>review, release decision"}
  TRIPLET --> REVIEW
  PROOFS["Evidence / proofs / receipts"] -. support .-> REVIEW
  REVIEW -->|approved| PUBLISHED["PUBLISHED<br/>public-safe carrier"]
  REVIEW -->|hold, abstain, or deny| CATALOG
~~~

Promotion is a governed state transition, not a file move. `CATALOG` and `TRIPLET` are sibling projections after `PROCESSED`; neither is `PUBLISHED`. Public clients use governed interfaces or approved released-artifact paths and must not read this internal lane directly.

## Repo fit

| Responsibility | Governed home | Current posture |
|---|---|---|
| Agriculture domain catalog | `data/catalog/domain/agriculture/` | **CONFIRMED** canonical path; README-only bounded inventory. |
| Parent catalog contract | [`data/catalog/`](../../README.md) | **CONFIRMED** canonical CATALOG boundary. |
| Agriculture processed inputs | [`data/processed/agriculture/`](../../../processed/agriculture/README.md) | **CONFIRMED** documentation surface; payload maturity not inferred here. |
| Agriculture evidence/proof support | [`data/proofs/agriculture/`](../../../proofs/agriculture/README.md) | **CONFIRMED** documentation surface; evidence must remain distinct from catalog records. |
| Agriculture rollback support | [`data/rollback/agriculture/`](../../../rollback/agriculture/README.md) | **CONFIRMED** documentation surface; release-plane decisions remain under `release/`. |
| Released Agriculture map carriers | [`data/published/layers/agriculture/`](../../../published/layers/agriculture/README.md) | **CONFIRMED** downstream documentation surface; catalog placement is not release. |
| Release governance | [`release/`](../../../../release/README.md) | **CONFIRMED** responsibility root; current operational capability is bounded by documented holds. |
| Compatibility redirect | [`catalog/domain/agriculture/`](../../../../catalog/domain/agriculture/README.md) | **CONFLICTED / non-authoritative.** Unresolved merge markers were found in the current README. |
| Agriculture STAC projection | `data/catalog/stac/agriculture/` | **PROPOSED / NOT FOUND** at the checked README path. |
| Agriculture DCAT projection | `data/catalog/dcat/agriculture/` | **PROPOSED / NOT FOUND** at the checked README path. |
| Agriculture PROV projection | `data/catalog/prov/agriculture/` | **PROPOSED / NOT FOUND** at the checked README path. |
| CatalogMatrix agreement | Domain catalog plus applicable STAC/DCAT/PROV projections | **PROPOSED.** ADR-0022 is proposed, and the test lane records contract/schema/path conflicts. |

## Accepted contents

Only governed catalog carriers belong here:

| Content | Admission boundary |
|---|---|
| Agriculture domain catalog records | Stable identity, version/digest posture, object scope, lifecycle state, and accepted profile. |
| Catalog indexes | Index entries resolve to governed records; an index is not a new truth source. |
| Release-linked catalog subsets | Immutable release reference, policy posture, correction path, and rollback target. |
| Evidence and source pointers | Resolvable `EvidenceRef` / `EvidenceBundle` and `SourceDescriptor` references where claims depend on them. |
| Aggregation pointers | Resolvable `AggregationReceipt` for aggregate public-use candidates. |
| Policy and sensitivity pointers | Applicable decision, obligations, redaction/generalization, rights, and audience state. |
| Quality summaries | References to validation reports and receipts; summaries do not replace them. |
| Cross-vocabulary links | Identity, digest, scope, and release-reference agreement where an accepted profile requires it. |

README, inventory, digest, migration, and disposition sidecars may explain the lane without becoming catalog, evidence, policy, or release authority.

## Exclusions

| Do not put here | Governed home or disposition |
|---|---|
| RAW source captures | `data/raw/agriculture/` |
| WORK intermediates or sensitive joins | `data/work/agriculture/` or `data/quarantine/agriculture/` |
| Processed datasets | [`data/processed/agriculture/`](../../../processed/agriculture/README.md) |
| Triplet or graph payloads | The accepted `data/triplets/.../agriculture/` lane |
| EvidenceBundle or proof payloads | [`data/proofs/agriculture/`](../../../proofs/agriculture/README.md) |
| Process receipts | The accepted `data/receipts/` lane |
| Release decisions or manifests | [`release/`](../../../../release/README.md) |
| Published artifacts | [`data/published/layers/agriculture/`](../../../published/layers/agriculture/README.md) after release |
| Semantic contracts, JSON Schemas, or policy rules | Their governed `contracts/`, `schemas/`, or `policy/` roots |
| Validators, fixtures, tests, pipelines, or runtime code | Their owning implementation or test roots |
| Secrets, private endpoints, unsafe logs, or restricted payloads | Approved restricted systems; never an ordinary public-repository path |
| AI-generated descriptions presented as evidence | Resolve governed evidence or abstain |

## Current maturity

| Capability | State | Evidence boundary |
|---|---|---|
| Canonical path and lane guide | `CONFIRMED` | Exact README and parent catalog contract inspected. |
| Concrete Agriculture catalog records | `UNKNOWN / NOT ESTABLISHED` | Bounded search found no record inventory under this lane. |
| Agriculture catalog fixture family | `README_ONLY / STRUCTURALLY_EMPTY` | The fixture-lane README says the directory is fixture-only and implementation-blocked. |
| Executable catalog-closure tests | `NOT ESTABLISHED` | The test-lane README reports no executable child test in its bounded search. |
| CatalogMatrix contract/schema | `PROPOSED / PLACEHOLDER` | The test lane records a draft semantic contract, permissive id-only schema, and path conflicts. |
| CatalogMatrix validator/resolver | `UNKNOWN / NOT FOUND` | No declared executable was verified by the inspected test-lane evidence. |
| STAC/DCAT/PROV Agriculture projections | `NOT FOUND` | The three checked README paths returned 404 at the pinned base state. |
| Evidence, policy, release, correction, and rollback closure | `UNKNOWN` | Documentation exists; emitted linked instances and operational enforcement were not established. |
| Public API/UI/map/AI enforcement | `UNKNOWN` | No runtime, route, deployment, or production evidence is claimed by this README. |

Until these holds close, `README_ONLY` is the honest maturity label. A green documentation check cannot upgrade it.

## Authoring and promotion workflow

1. Start from an admitted `PROCESSED` Agriculture object or product; never write directly from a connector, watcher, RAW capture, or unreviewed WORK item.
2. Resolve stable identity, version, digest, source role, spatial and temporal scope, rights, sensitivity, and evidence references.
3. If aggregation, redaction, or generalization applies, require the corresponding receipt and preserve the transform reason and precision change.
4. Build the domain catalog candidate and only the applicable standards or triplet projections.
5. Validate local shape and cross-record identity, digest, scope, source, evidence, policy, and release-reference agreement with accepted validators.
6. Emit inspectable validation and build receipts; do not treat a receipt as proof or approval.
7. Hold on missing, stale, restricted, conflicting, or unresolved dependencies. Use finite outcomes such as `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` rather than implied success.
8. Submit the candidate to accountable policy, sensitivity, domain, and release review appropriate to significance.
9. Publish only after an immutable release decision identifies the approved carrier, correction path, and rollback target.
10. On correction, withdrawal, supersession, or rollback, re-evaluate affected catalog entries and downstream consumers without silently overwriting history.

## Agriculture catalog requirements

The profile below is **PROPOSED** until accepted contracts, schemas, fixtures, validators, and negative tests establish it.

| Gate | Required posture | Failure outcome |
|---|---|---|
| Identity | Stable catalog, object/product, version, and digest identity. | `HOLD` or `DENY`. |
| Lifecycle | No skip across `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`. | `DENY`. |
| Source | Resolvable source descriptor and preserved source role. | `ABSTAIN` or `DENY`. |
| Evidence | `EvidenceRef` resolves to admissible `EvidenceBundle` where claims depend on evidence. | `ABSTAIN`, `HOLD`, or `DENY`. |
| Aggregation | Public aggregate candidates resolve an `AggregationReceipt` with input, method, output, scale, and precision lineage. | `HOLD` or `DENY`. |
| Rights and sensitivity | Audience, rights, sovereignty, living-person, proprietary, location, and precision obligations are closed. | `RESTRICT`, `HOLD`, or `DENY`. |
| Catalog agreement | Applicable domain, STAC, DCAT, PROV, triplet, and matrix identities/digests/release refs agree under an accepted profile. | `DENY`. |
| Validation | Accepted validator versions and reports are resolvable; skipped or TODO checks remain visible. | `HOLD`. |
| Review and policy | Accountable review and policy decisions are distinct from authoring and catalog construction where materiality requires it. | `HOLD` or `DENY`. |
| Release | Public-use record resolves an immutable release decision and released carrier. | `HOLD`. |
| Correction and rollback | Correction path, downstream dependency scope, and rollback target are explicit. | `HOLD`. |

## Aggregation and sensitivity guardrails

- Agriculture catalog carriers are not Agriculture source truth.
- Aggregation is load-bearing for public Agriculture products. A label such as “county level” is not a substitute for a resolvable `AggregationReceipt`.
- Farm, operator, parcel, field-level, proprietary-yield, pesticide-record, private-contract, and private-sensitive joins fail closed until rights, sensitivity, evidence, policy, review, and release obligations support a bounded representation.
- Generalization and redaction must preserve input/output identity, method, precision change, reason, and receipt lineage.
- Source roles must not collapse: modeled crop-cover products are not observed field truth; aggregate statistics are not field evidence; stress indicators are not emergency alerts.
- Catalog metadata must not reveal more precision than the released carrier or policy permits.
- Unreleased or withdrawn records are not public because they are discoverable internally.
- When a claim cannot be supported safely, narrow scope, generalize, restrict, or abstain.

See [Agriculture sensitivity guidance](../../../../docs/domains/agriculture/SENSITIVITY.md) for the domain documentation posture.

## Evidence ledger

| Evidence | Pinned state | What it supports | Limit |
|---|---|---|---|
| This README baseline | blob `54c5793bdd194d2ccc71100f45f234a0b1f33458` | Substantive v0.1 boundary and preserved section contract. | Does not prove payloads or enforcement. |
| [Parent catalog README](../../README.md) | blob `b878b6156fdeea4f02143b39e6cb617a2b69ebc6` | Canonical CATALOG responsibility, no direct public path, closure remains unverified. | Parent evidence is lane-wide, not Agriculture payload proof. |
| Supplied `Directory Rules.pdf` | inspected 2026-07-24 | `data/catalog/domain/<domain>/` placement and explicit lifecycle classification. | Governing path doctrine, not runtime evidence. |
| [Agriculture canonical paths](../../../../docs/domains/agriculture/CANONICAL_PATHS.md) | blob `94e9fb5d76ff4aa032a8c499d86fc90ed25da86f`; status `draft` | Names this exact lifecycle path and release separation. | Agriculture-specific implementation is described as proposed. |
| [Agriculture lifecycle](../../../../docs/domains/agriculture/DATA_LIFECYCLE.md) | blob `d90fb138141c4b6b56ac5940f15a7219d5637797`; status `draft` | Lifecycle, aggregation, sensitivity, promotion, and correction posture. | Does not establish executable gates. |
| [ADR-0022](../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | status `proposed` | Proposed STAC/DCAT/PROV agreement model. | Not accepted authority; path conflicts remain. |
| [Fixture boundary](../../../../fixtures/domains/agriculture/catalog/README.md) | blob `07123479a65a0d9d9a227b675dd22ad319ae53a8` | README-only, structurally empty, fixture-only posture. | No synthetic fixture payloads established. |
| [Closure-test boundary](../../../../tests/domains/agriculture/catalog_closure/README.md) | blob `2086c10aa248c5e80de89d755a1a989aaed11257` | No executable child test found; placeholder schema and missing validator recorded. | Documentation is not execution proof. |
| [Compatibility root](../../../../catalog/README.md) | blob `638686cd5473219227a17b80e976c7caf54da710` | Top-level `catalog/` is severe, non-authoritative parallel drift. | Does not repair child conflicts. |
| [Compatibility child](../../../../catalog/domain/agriculture/README.md) | blob `bf1a333573c6d068fbb0b695356346003842aceb` | Redirect intent and unresolved merge-conflict markers. | Conflicted content is not authority. |
| [Release root](../../../../release/README.md) | blob `0752610b1df6d11143158f6f162f65ecd650e6a6` | Candidate is not release; operational release controls have explicit holds. | No Agriculture release is established. |
| [CODEOWNERS](../../../../.github/CODEOWNERS) | blob `dd2a84aa514d8ecd9208bc347f90f9a2b69ebc6` | Default review route `@bartytime4life`. | Routing is not stewardship, approval, or separation of duties. |

## Validation checklist

### Documentation packet

- [x] One H1; existing v0.1 section contract preserved.
- [x] Canonical path checked against the supplied Directory Rules and current parent catalog evidence.
- [x] Relative links target repository surfaces verified at the pinned base state.
- [x] Lifecycle diagram keeps release review and decision between CATALOG/TRIPLET and PUBLISHED.
- [x] Catalog, evidence, receipt, proof, policy, release, published, correction, and rollback authorities remain separate.
- [x] Current maturity and absent implementation evidence are stated without upgrading them.
- [x] Compatibility drift and unresolved conflict markers are visible without editing the compatibility root.

### Readiness holds

- [ ] Inventory concrete Agriculture catalog records and writers/consumers.
- [ ] Resolve the CatalogMatrix semantic, schema, validator, resolver, and instance-path conflicts through accepted governance.
- [ ] Define and accept an Agriculture catalog profile.
- [ ] Add synthetic valid, invalid, restricted, held, corrected, withdrawn, superseded, and rollback fixtures.
- [ ] Implement deterministic no-network validators and executable positive/negative closure tests.
- [ ] Establish STAC/DCAT/PROV projection homes and accepted agreement rules where applicable.
- [ ] Prove `EvidenceRef -> EvidenceBundle`, source-role, aggregation, policy, release, correction, and rollback resolution.
- [ ] Prove public clients cannot read candidate or internal catalog stores directly.
- [ ] Verify accountable stewardship, required review, and separation of release duties.

## Review and maintenance

Documentation-only changes require Agriculture plus data/catalog review appropriate to scope. Any change to payload admission, object meaning, machine shape, source activation, rights, sensitivity, aggregation, precision, policy, validators, lifecycle promotion, release, correction, rollback, or public consumption also requires the corresponding accountable reviewers and evidence.

Re-review this README when any of these occur:

- a concrete record, profile, schema, fixture, validator, resolver, workflow, or consumer appears;
- ADR-0022 or a competing catalog-placement decision changes status;
- STAC, DCAT, PROV, triplet, matrix, or release-reference conventions change;
- Agriculture sensitivity, aggregation, source-role, or precision policy changes;
- the compatibility copy is repaired, migrated, deprecated, or retired;
- release, correction, withdrawal, supersession, rollback, or public-interface behavior changes; or
- six months pass without evidence refresh.

Do not silently convert `UNKNOWN` or `NEEDS VERIFICATION` into fact. Record the evidence, pinned state, reviewer, correction effect, and rollback consequence.

## Rollback

For this documentation-only change:

- before merge, close the pull request or abandon the branch;
- after merge, revert the documentation commit;
- if a factual error survives release, issue the repository’s correction process and update inbound references;
- do not restore the historical blank placeholder as the normal rollback target, because that would discard the v0.1 lane contract rather than reverse only this modernization.

For catalog or published state, rollback is a separate governed action. Preserve the prior immutable release, affected identifiers and consumers, correction or withdrawal notice, rollback decision, execution receipt, and post-rollback verification. Never represent a documentation revert as a data rollback.

### Change history

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-06-24 | Replaced a historical blank placeholder with the first Agriculture catalog-lane guide. |
| `v0.2.0` | 2026-07-24 | Grounded the canonical path, corrected lifecycle and release semantics, added maturity and workflow boundaries, recorded compatibility conflict drift, expanded evidence and validation, and clarified rollback. |

<p align="right"><a href="#top">Back to top</a></p>
