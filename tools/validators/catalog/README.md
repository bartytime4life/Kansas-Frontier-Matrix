<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-readme
title: tools/validators/catalog/ — Catalog Record Validator Boundary
type: readme; validator-lane; catalog-record-validation; stac; dcat; prov; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only; catalog-matrix-stub-confirmed; shared-runtime-confirmed; aggregate-registration-absent; catalog-closure-sibling-confirmed; data-catalog-canonical; root-catalog-compatibility-only; placeholder-schemas; catalog-matrix-placement-conflicted; dedicated-tests-unestablished; dedicated-ci-unestablished; release-gated; fail-closed
owners: OWNER_TBD — Catalog · STAC · DCAT · PROV/PAV · Validator · Schema · Contract · Source · Evidence · Rights/Sensitivity · Policy · Release · Security · CI · Docs stewards
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1
policy_label: repository-facing; catalog; discovery; interchange; evidence-aware; rights-aware; sensitivity-aware; release-gated; fail-closed; discovery-not-truth
owning_root: tools/
current_path: tools/validators/catalog/README.md
responsibility: Validate individual catalog discovery/interchange records and bounded indexes; delegate cross-record closure, evidence, policy, release, storage, construction, and public serving to their owning lanes.
truth_posture: >
  CONFIRMED target v0.1 and prior blob; direct lane README-only in bounded search; catalog_closure sibling documented;
  top-level validate_catalog_matrix.py raises NotImplementedError; shared five-entry aggregate excludes placeholder validators;
  data/catalog is canonical CATALOG-stage home with RELEASED ONLY exposure; root catalog is compatibility-only; STAC, DCAT,
  PROV and domain catalog sublanes exist; catalog package and pipeline are scaffolds/documentation-led; CatalogMatrix and
  ValidationReport schemas are permissive placeholders / PROPOSED packet, report, reason codes, fixtures, CI and rollback /
  CONFLICTED ADR-0011 versus ADR-0022 CatalogMatrix placement and validator/schema paths / NEEDS VERIFICATION owners,
  profiles, namespace, canonical matrix path, policies, tests, CI and public-route enforcement / UNKNOWN runtime consumers,
  emitted reports, hosting/search behavior, metrics, deployment and pass results
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: "05e403a1d607c8e69f028baf92010f4b2501203a"
  prior_blob: e4736954d8cecdc55b3ce48b52523f0c9ba61343
  data_catalog_blob: 9cf67c4ce5308b9088466b023a244107e3863a48
  catalog_closure_blob: fef3e0df1d566d2839b6c3da17d75723f16628fc
  catalog_matrix_contract_blob: c67923beb505aa39e7c0c768c16e75a00826ff31
  catalog_matrix_schema_blob: 75a927376066226d8a0f89a630d7bb3693143c41
  catalog_matrix_stub_blob: 91ecf78675cf19672a0e94a3899df3074c36ddc4
  catalog_package_blob: 14d0462d9dfa0d594df33e9a8da6cc7bc1f8ebf0
  catalog_pipeline_blob: 6404f3228f307faa7e1e5347a185011e8589f840
  adr_0011_blob: 158ad6d31946d7d32537d5278ec6d2828ec880b3
  adr_0022_blob: b09c1d7aaa39f3030afdcec419c58236fd324f17
  run_all_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  validator_suite_blob: 7651f0571ba8f879819b197155d160c08f9fe7ac
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog_closure/README.md
  - ../validate_catalog_matrix.py
  - ../../../data/catalog/README.md
  - ../../../data/catalog/stac/README.md
  - ../../../data/catalog/dcat/README.md
  - ../../../data/catalog/prov/README.md
  - ../../../data/catalog/domain/README.md
  - ../../../catalog/README.md
  - ../../../pipelines/catalog/README.md
  - ../../../packages/catalog/src/catalog/README.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../contracts/data/validation_report.md
  - ../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../policy/data/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/validator-suite.yml
tags: [kfm, tools, validators, catalog, stac, dcat, prov, evidence, lifecycle, rights, sensitivity, release, rollback]
notes:
  - Documentation-only update paired with a generated provenance receipt.
  - No executable, catalog record, schema, policy, test, workflow, pipeline, package code, lifecycle object, release record or public artifact changes.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Record Validator Boundary

`tools/validators/catalog/`

> Validate individual catalog discovery/interchange records without turning catalog metadata into truth, proof, policy, release approval or publication.

<p>
  <img alt="Status draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Discovery not truth" src="https://img.shields.io/badge/catalog-discovery__not__truth-blueviolet">
  <img alt="Release gated" src="https://img.shields.io/badge/exposure-release__gated-critical">
  <img alt="Fail closed" src="https://img.shields.io/badge/posture-fail__closed-red">
</p>

> [!IMPORTANT]
> No working executable was established in this directory. The observed top-level CatalogMatrix validator is a `NotImplementedError` stub excluded from the shared five-entry aggregate.

**Quick links:** [Purpose](#purpose) · [Status and evidence](#status) · [Directory Rules and authority](#placement) · [Validator topology](#topology) · [Record families](#families) · [Validation packet](#packet) · [Identity, digest, namespace and time](#identity) · [STAC rules](#stac) · [DCAT rules](#dcat) · [PROV/PAV rules](#prov) · [Domain catalog and index rules](#domain-index) · [Reference and family separation](#references) · [Lifecycle and public boundary](#lifecycle) · [Rights, sensitivity and metadata exposure](#sensitivity) · [CatalogMatrix conflict register](#matrix-conflict) · [Validation report contract](#report) · [Outcomes and reason codes](#outcomes) · [Security and resource posture](#security) · [Tests and fixtures](#tests) · [CI admission](#ci) · [Implementation sequence](#sequence) · [Definition of done](#done) · [Migration and deprecation](#migration) · [Correction, supersession and rollback](#rollback) · [Open verification register](#open) · [Evidence ledger](#ledger) · [Changelog](#changelog)

---
<a id="purpose"></a>

## Purpose

Validate one catalog record or bounded index against an explicit profile and governed references. The lane does not build records, close a release, create evidence, decide policy, publish, host, search, or serve public clients.

[Back to top](#top)

---
<a id="status"></a>

## Status and evidence

**Snapshot:** `main@05e403a1d607c8e69f028baf92010f4b2501203a` · **prior blob:** `e4736954d8cecdc55b3ce48b52523f0c9ba61343`.

| Surface | Status |
|---|---|
| Direct lane | README-only in bounded search |
| `validate_catalog_matrix.py` | Confirmed `NotImplementedError` stub |
| Shared aggregate | Five non-placeholder validators; catalog absent |
| CatalogMatrix/ValidationReport schemas | Confirmed permissive placeholders |
| Dedicated catalog tests/CI | Not established |
| Runtime consumers and pass results | UNKNOWN |

A future pass proves only configured checks for the identified record/profile/input digest.

[Back to top](#top)

---
<a id="placement"></a>

## Directory Rules and authority

`tools/validators/catalog/` owns record-local checks. `catalog_closure/` owns cross-record readiness; `pipelines/catalog/` builds; `packages/catalog/` provides reusable helpers; `data/catalog/` stores CATALOG-stage records; `release/` decides publication; governed APIs serve released outputs. Root `catalog/` remains a compatibility fence.

[Back to top](#top)

---
<a id="topology"></a>

## Validator topology

Route STAC/DCAT/PROV/domain-record shape here; route STAC↔DCAT↔PROV agreement and CatalogMatrix completeness to `catalog_closure/`; route source, evidence, rights, sensitivity, lifecycle and release checks to their owning validators. Do not create a second closure engine or validator-local policy/profile authority.

[Back to top](#top)

---
<a id="families"></a>

## Record families

Supported families require an explicit profile: STAC Catalog/Collection/Item/Asset/Link; DCAT Catalog/Dataset/Distribution/DataService; PROV Entity/Activity/Agent plus PAV fields; domain catalog entries; bounded indexes; quality summaries; CatalogMatrix references. Unknown families return `ABSTAIN` or `UNSUPPORTED_PROFILE`.

[Back to top](#top)

---
<a id="packet"></a>

## Validation packet

Use immutable inputs:
```yaml
packet_version: kfm.catalog.validation-packet.v1
operation: validate_catalog_record
candidate: {record_ref: ..., record_family: ..., profile_ref: ..., candidate_digest: ...}
context: {lifecycle_state: CATALOG, source_descriptor_refs: [], evidence_refs: [], policy_decision_refs: [], release_ref: null}
limits: {network: deny, max_bytes: configured, max_reference_depth: configured}
```
Missing required context produces a finding, never an inferred default.

[Back to top](#top)

---
<a id="identity"></a>

## Identity, digest, namespace and time

Check canonical record/artifact identity, profile digest, asset/distribution/entity checksums, accepted KFM namespace, URI normalization, and distinct observation/source/valid/retrieval/catalog/release/correction times. Stale or superseded records cannot appear current.

[Back to top](#top)

---
<a id="stac"></a>

## STAC rules

Bind the accepted STAC version/profile; check object type, links, collection relation, geometry/bbox/time, assets, media type, roles, checksums, extension declarations and governed references. STAC validity does not prove asset existence, truth, permission or release.

[Back to top](#top)

---
<a id="dcat"></a>

## DCAT rules

Bind the accepted DCAT profile; check class, identifier, publisher, themes, coverage, distributions/services, URLs, formats, checksums, rights, provenance and release references. Metadata URLs do not guarantee availability or public access.

[Back to top](#top)

---
<a id="prov"></a>

## PROV/PAV rules

Check Entity/Activity/Agent identities, generation/usage/derivation/association, times, plans and PAV versioning. Keep semantic provenance separate from receipts, EvidenceBundles and supply-chain attestations.

[Back to top](#top)

---
<a id="domain-index"></a>

## Domain catalog and index rules

Require owning domain/object family, stable artifact version, source/evidence/policy/release references, spatial/temporal scope, rights/sensitivity, lifecycle and correction state. Index membership is not completeness, truth or release.

[Back to top](#top)

---
<a id="references"></a>

## Reference and family separation

Resolve syntax, target family, existence, digest and authority separately. Enforce `receipt ≠ proof ≠ catalog ≠ publication`; reject a receipt as proof, CatalogMatrix as ReleaseManifest, ValidationReport as PolicyDecision, compatibility README as data, or UI/generated text as evidence.

[Back to top](#top)

---
<a id="lifecycle"></a>

## Lifecycle and public boundary

Preserve `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. Public-bound records cannot expose internal stages; `data/catalog/` placement alone is not release; withdrawn/superseded/rolled-back entries cannot remain active; public clients use governed interfaces.

[Back to top](#top)

---
<a id="sensitivity"></a>

## Rights, sensitivity and metadata exposure

Fail closed on rights gaps or metadata that can reveal rare species/plants, archaeology/cultural places, living-person/DNA/land/private-well data, critical infrastructure, restricted endpoints, precise geometry, sensitive cadence or reconstructable link graphs. Most-restrictive policy propagates.

[Back to top](#top)

---
<a id="matrix-conflict"></a>

## CatalogMatrix conflict register

| Evidence | Posture |
|---|---|
| `contracts/data/catalog_matrix.md` | Draft semantic contract |
| `schemas/contracts/v1/data/catalog_matrix.schema.json` | Placeholder, only `id` required |
| Schema-declared validator | `tools/validators/data/validate_catalog_matrix.py` |
| Observed validator | top-level stub raising `NotImplementedError` |
| ADR-0011 | Proposed proof-side placement |
| ADR-0022 | Proposed catalog/release matrix and different homes |
| `catalog_closure/` | Documented closure lane |

This README chooses no canonical matrix path and creates no duplicate implementation.

[Back to top](#top)

---
<a id="report"></a>

## Validation report contract

A future report should identify target/profile/validator/input digests, finite outcome, safe findings, dependency results, policy implications and lifecycle effect:
```yaml
overall_outcome: PASS | WARN | FAIL | ABSTAIN | ERROR | REVIEW_REQUIRED
findings: [{code: CAT_<FAMILY>_<REASON>, severity: blocking, safe_message: ...}]
```
Reports are not receipts, proof closure, policy decisions or release approval.

[Back to top](#top)

---
<a id="outcomes"></a>

## Outcomes and reason codes

Top outcomes are `PASS`, `WARN`, `FAIL`, `ABSTAIN`, `ERROR`, `REVIEW_REQUIRED`. Proposed stable families: `CAT_PROFILE_*`, `CAT_SHAPE_*`, `CAT_IDENTITY_*`, `CAT_DIGEST_*`, `CAT_TIME_*`, `CAT_LINK_*`, `CAT_SOURCE_*`, `CAT_EVIDENCE_*`, `CAT_RIGHTS_*`, `CAT_SENSITIVITY_*`, `CAT_LIFECYCLE_*`, `CAT_RELEASE_*`, `CAT_CORRECTION_*`, `CAT_PUBLIC_*`, `CAT_RESOURCE_*`, `CAT_INTERNAL_*`.

[Back to top](#top)

---
<a id="security"></a>

## Security and resource posture

Default no-network; local profiles only; bounded bytes/nesting/reference depth/diagnostics; safe URI schemes; no remote schema fetch, redirects, shell/template/query injection, credential discovery or secret-bearing diagnostics; deterministic ordering; fail closed on parser/resolver/resource errors.

[Back to top](#top)

---
<a id="tests"></a>

## Tests and fixtures

No dedicated executable suite surfaced. Future synthetic fixtures must cover valid record families, unknown profile, malformed shape, identity/digest/time mismatch, missing dependencies, unreleased public exposure, sensitive metadata leakage, stale state, family collapse, hostile URIs, oversized/deep inputs, network denial and deterministic reruns.

[Back to top](#top)

---
<a id="ci"></a>

## CI admission

Current `validator-suite` runs `make schemas`; the shared aggregate excludes placeholders and does not establish catalog coverage. A future job must require nonempty positive/negative fixtures, record/closure separation, reason-code uniqueness, no-network/resource canaries, safe diagnostics, retained machine reports and approved release significance.

[Back to top](#top)

---
<a id="sequence"></a>

## Implementation sequence

1. Decide registry/path/CatalogMatrix authority. 2. Accept profiles and strengthen schemas. 3. Implement pure record-local validator. 4. Add public-safe fixtures/tests. 5. Bind policy/release/correction adapters. 6. Register CI/consumers. Keep each step reversible and independently reviewed.

[Back to top](#top)

---
<a id="done"></a>

## Definition of done

Owners, one executable/registry id, accepted STAC/DCAT/PROV/domain profiles, namespace/identity/digest/time rules, meaningful schemas, source/evidence/rights/sensitivity/lifecycle/release adapters, nonempty fixtures, deterministic no-network tests, stable reports/codes, CI, governed RELEASED ONLY serving and tested correction/rollback are required.

[Back to top](#top)

---
<a id="migration"></a>

## Migration and deprecation

Track root `catalog/` versus `data/catalog/`, proof-side versus catalog-side CatalogMatrix proposals, `schemas/.../data` versus proposed `.../catalog`, top-level stub versus schema-declared validator path, record versus closure lanes and namespace drift. Migration needs an accepted target, inventory, one active implementation, compatibility plan, deprecation and rollback.

[Back to top](#top)

---
<a id="rollback"></a>

## Correction, supersession and rollback

On source/rights/sensitivity/evidence/digest/profile/release changes: issue governed correction/withdrawal; mark records stale/superseded/withdrawn; invalidate indexes/closure; rebuild or withdraw released records; update governed caches; preserve lineage and rollback target. Documentation rollback reverts this README and receipt.

[Back to top](#top)

---
<a id="open"></a>

## Open verification register

1. Owners/CODEOWNERS. 2. Executable and registry id. 3. STAC profile/namespace. 4. DCAT profile/serialization. 5. PROV/PAV profile. 6. Domain/index contracts. 7. ADR-0011/0022 resolution. 8. CatalogMatrix homes. 9. ValidationReport schema/destination. 10. Record/closure dependency. 11. Source/evidence adapters. 12. Rights/sensitivity policy. 13. Lifecycle/release fields. 14. Identity/digest/time rules. 15. URI/media/link registries. 16. Local profile registry. 17. Network/resource budgets. 18. Diagnostic redaction. 19. Fixtures/tests. 20. Package/pipeline behavior. 21. CatalogBuildReceipt. 22. CI/required check. 23. Public consumers. 24. Compatibility producer exclusion. 25. Correction/cache invalidation. 26. Sensitive-domain review. 27. Stub disposition. 28. Duplicate authority detection. 29. Separation of duties. 30. Metrics/pass results/deployment.

---
<a id="ledger"></a>

## Evidence ledger

| Evidence | Status | Supports |
|---|---|---|
| target `e4736954d8cecdc55b3ce48b52523f0c9ba61343` | CONFIRMED | prior v0.1 |
| `data/catalog/` and STAC/DCAT/PROV READMEs | CONFIRMED draft | canonical lifecycle/carrier boundaries |
| root `catalog/` | CONFIRMED compatibility | drift fence |
| `catalog_closure/` | CONFIRMED README-only | record versus closure split |
| CatalogMatrix/ValidationReport contracts and schemas | CONFIRMED draft/placeholders | intended meaning and maturity gap |
| top-level CatalogMatrix stub | CONFIRMED | placeholder, not enforcement |
| package/pipeline READMEs | CONFIRMED scaffold/docs | implementation boundary |
| ADR-0011/ADR-0022 | CONFIRMED documents; PROPOSED decisions | unresolved placement/closure conflict |
| `policy/data/` | CONFIRMED draft | fail-closed intent |
| `run_all.py` and validator-suite | CONFIRMED executable/workflow | five-entry aggregate, no catalog |
| Directory Rules | CONFIRMED doctrine | responsibility-root placement |

This supports documentation only, not production validation or release adoption.

---
<a id="changelog"></a>

## Changelog

**v0.2 — 2026-07-16:** repository-grounded status; record/closure split; CatalogMatrix stub and path conflicts; canonical/compatibility catalog roots; record-family, identity, lifecycle, rights/sensitivity, packet/report, reason-code, security, fixture, CI, implementation, migration and rollback guidance. No executable or trust-bearing behavior changed.

**v0.1 — 2026-07-07:** initial proposed lane.

---
