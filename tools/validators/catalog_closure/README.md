<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-closure-readme
title: tools/validators/catalog_closure/ — Catalog Closure Readiness Validator Boundary
type: readme; validator-lane; catalog-closure; catalog-matrix; proof-readiness; release-readiness; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only; catalog-record-sibling-confirmed; domain-child-readmes-confirmed; catalog-matrix-stub-confirmed; schema-validator-path-missing; fixture-root-missing; proof-side-instance-readme-missing; shared-runtime-confirmed; aggregate-registration-absent; placeholder-schema; adr-placement-conflicted; release-resolver-unestablished; dedicated-tests-unestablished; dedicated-ci-unestablished; release-gated; no-network-by-default; fail-closed
owners: OWNER_TBD — Catalog closure steward · Catalog steward · STAC steward · DCAT steward · PROV/PAV steward · Evidence/proof steward · Source-registry steward · Validation steward · Policy steward · Rights/sensitivity reviewer · Release steward · Correction/rollback steward · Security reviewer · CI steward · Domain stewards · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 proposed catalog-closure validator guide
policy_label: "repository-facing; tools; validators; catalog-closure; catalog-matrix; stac; dcat; prov; source-descriptor; evidence-bundle; proof-pack; validation-report; policy-decision; review-record; release-manifest; lifecycle; correction; supersession; withdrawal; rollback; metadata-leakage; release-gated; fail-closed; no-network; no-truth-authority; no-proof-authority; no-policy-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/catalog_closure/README.md
responsibility: >
  Repository-grounded parent and routing boundary for deterministic catalog-closure readiness checks over an explicit,
  immutable set of catalog records, source descriptors, evidence/proof references, validation reports, policy/review records,
  release references, correction lineage, and lifecycle state. The lane checks completeness, agreement, resolvability,
  consistency, public-surface safety, and correction impact; delegates individual record validation to
  tools/validators/catalog/, domain-specific closure to domain child lanes, and release decisions to release authority. It
  never creates catalog records, CatalogMatrix instances, EvidenceBundles, proofs, receipts, PolicyDecisions,
  ReleaseManifests, published artifacts, public routes, search indexes, or publication approval.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; tools/validators/catalog/ v0.2 is the record-local sibling; bounded search
  surfaced only this README for validate_catalog_closure and CATALOG_CLOSURE_PASS; the observed top-level
  tools/validators/validate_catalog_matrix.py raises NotImplementedError; the schema-declared
  tools/validators/data/validate_catalog_matrix.py path is absent; fixtures/data/catalog_matrix/README.md and
  data/proofs/catalog_matrix/README.md are absent at exact checked paths; CatalogMatrix contract exists and says the matrix
  is an inspectability aid, not evidence, proof closure, policy, or release approval; its schema is a permissive PROPOSED
  placeholder requiring only id; ADR-0011 and ADR-0022 are both proposed and conflict over CatalogMatrix placement/emphasis;
  ADR-0022 proposes STAC/DCAT/PROV agreement on identity, digest, and release reference plus a live resolver, but no resolver
  surfaced in bounded search; domain-specific closure README lanes exist, including Soil, while executable behavior remains
  unverified; tests/validators is README-only while shared validator runtime and a five-entry aggregate exist elsewhere and
  exclude CatalogMatrix/catalog closure; dedicated fixtures, tests, CI, emitted reports, release integration, and public
  route enforcement are not established / PROPOSED immutable closure packet, dependency result envelope, deterministic
  ValidationReport profile, finite outcomes and CCL_ reason codes, no-network fixtures, CI admission, correction cascade,
  migration, deprecation, and rollback / CONFLICTED ADR-0011 proof-side CatalogMatrix versus ADR-0022 release/catalog matrix,
  schema and validator path drift, parent versus domain-child routing, and catalog matrix versus closure resolver authority /
  NEEDS VERIFICATION owners, CODEOWNERS, accepted CatalogMatrix and report homes, accepted profile/namespace versions,
  canonical executable/registry entry, complete child inventory, policies, meaningful fixtures/tests, report destination, CI
  significance, release-gate adoption, correction cascade, and compatibility retirement / UNKNOWN runtime consumers,
  production invocation, emitted reports/matrices, hosting/search behavior, metrics, deployment, current pass results,
  branch-protection significance, and operational rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "87c90c7034a0d6310a286d7ffd34b5c89cffabec"
  prior_blob: fef3e0df1d566d2839b6c3da17d75723f16628fc
  catalog_record_sibling_blob: 2b05c5e0054862d2990e59adfead83f14f409d5f
  catalog_matrix_contract_blob: c67923beb505aa39e7c0c768c16e75a00826ff31
  catalog_matrix_schema_blob: 75a927376066226d8a0f89a630d7bb3693143c41
  catalog_matrix_stub_blob: 91ecf78675cf19672a0e94a3899df3074c36ddc4
  soil_domain_child_blob: 298c4a3ecff2c9fdf548a0a2da46b701f1df6cb2
  validator_tests_parent_blob: c703a64eef3f69044a54696f121f4e5ae05a3631
  adr_0011_blob: 158ad6d31946d7d32537d5278ec6d2828ec880b3
  adr_0022_blob: b09c1d7aaa39f3030afdcec419c58236fd324f17
  run_all_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  validator_suite_blob: 7651f0571ba8f879819b197155d160c08f9fe7ac
  bounded_path_checks:
    - tools/validators/catalog_closure/ surfaced only README.md for the direct lane
    - validate_catalog_closure and CATALOG_CLOSURE_PASS searches returned no executable implementation
    - tools/validators/validate_catalog_matrix.py is a NotImplementedError stub
    - tools/validators/data/validate_catalog_matrix.py returned 404
    - fixtures/data/catalog_matrix/README.md returned 404
    - data/proofs/catalog_matrix/README.md returned 404
    - resolve_release_manifest search returned only ADR documentation
    - tests/validators/catalog_closure search returned only this README reference
related:
  - ../README.md
  - ../_common/README.md
  - ../_common/run_all.py
  - ../catalog/README.md
  - ../validate_catalog_matrix.py
  - ../domains/soil/catalog_closure/README.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../contracts/data/validation_report.md
  - ../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../policy/data/README.md
  - ../../../data/catalog/README.md
  - ../../../data/catalog/stac/README.md
  - ../../../data/catalog/dcat/README.md
  - ../../../data/catalog/prov/README.md
  - ../../../data/catalog/domain/README.md
  - ../../../data/triplets/README.md
  - ../../../data/registry/README.md
  - ../../../data/proofs/README.md
  - ../../../data/receipts/README.md
  - ../../../data/published/README.md
  - ../../../release/README.md
  - ../../../tests/validators/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/validator-suite.yml
tags: [kfm, tools, validators, catalog-closure, catalog-matrix, stac, dcat, prov, evidence, proof, lifecycle, release, correction, rollback, fail-closed]
notes:
  - "Documentation-only update paired with a generated provenance receipt."
  - "No executable, schema, contract, policy, fixture, test, workflow, catalog data, proof, receipt, release record, runtime, or public surface is changed."
  - "Proposed ADR language is recorded as proposed; this README does not accept ADR-0011 or ADR-0022."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Closure Readiness Validator Boundary

`tools/validators/catalog_closure/`

> Determine whether an explicit catalog-facing package is complete, mutually consistent, resolvable, policy-aware, reviewable, correction-aware, and safe enough to proceed to the next governed review gate—without turning validator success into proof closure, policy permission, release approval, or publication.

<p>
  <img alt="Status draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Boundary readiness not approval" src="https://img.shields.io/badge/boundary-readiness__not__approval-blueviolet">
  <img alt="Catalog matrix placement conflicted" src="https://img.shields.io/badge/CatalogMatrix-placement__conflicted-red">
  <img alt="Release gated" src="https://img.shields.io/badge/exposure-release__gated-critical">
  <img alt="Fail closed" src="https://img.shields.io/badge/posture-fail__closed-red">
</p>

> [!IMPORTANT]
> No working catalog-closure executable was established in this directory. The observed top-level CatalogMatrix validator raises `NotImplementedError`, its schema-declared alternate path is absent, the schema is a permissive placeholder, and no dedicated closure fixture/test lane or release resolver was established.

**Quick links:** [Purpose](#purpose) · [Status and evidence](#status) · [Directory Rules and authority](#placement) · [Validator topology](#topology) · [Closure scope](#scope) · [What closure does not prove](#non-claims) · [Proposed validation packet](#packet) · [Dependency result envelope](#dependency-envelope) · [Closure invariants](#invariants) · [STAC/DCAT/PROV agreement](#agreement) · [Source, evidence and validation closure](#support) · [Policy, review and release readiness](#governance) · [Lifecycle and public boundary](#lifecycle) · [CatalogMatrix conflict register](#matrix-conflict) · [Validation report contract](#report) · [Outcomes and reason codes](#outcomes) · [Security and resource posture](#security) · [Tests and fixtures](#tests) · [CI admission](#ci) · [Implementation sequence](#sequence) · [Definition of done](#done) · [Migration and deprecation](#migration) · [Correction and rollback](#rollback) · [Open verification register](#open) · [Evidence ledger](#ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

This lane checks a **declared closure package**. It asks whether the package's catalog records, source references, evidence support, validation findings, policy/review posture, release references, and correction/rollback links are complete and mutually consistent for a named operation and audience.

It does not build the package, create its trust records, or decide publication.

A durable question for the lane is:

> Given this exact set of immutable inputs and requested transition, are all configured closure dependencies present, resolvable, mutually consistent, and safe to hand to the next governed gate—or must the request fail, hold, deny, abstain, require review, or error?

[Back to top](#top)

---

<a id="status"></a>

## Status and evidence

**Snapshot:** `main@87c90c7034a0d6310a286d7ffd34b5c89cffabec` · **prior target blob:** `fef3e0df1d566d2839b6c3da17d75723f16628fc`.

| Surface | Status | Consequence |
|---|---|---|
| Direct `catalog_closure/` lane | **CONFIRMED README-only in bounded search** | No executable behavior is claimed. |
| Catalog-record sibling | **CONFIRMED README v0.2** | Individual record/profile checks belong in [`catalog/`](../catalog/README.md). |
| Domain-specific closure children | **CONFIRMED README examples / executable NEEDS VERIFICATION** | Domain rules may extend shared closure without redefining it. |
| Top-level CatalogMatrix validator | **CONFIRMED stub** | [`../validate_catalog_matrix.py`](../validate_catalog_matrix.py) raises `NotImplementedError`. |
| Schema-declared validator path | **CONFIRMED absent at exact path** | `tools/validators/data/validate_catalog_matrix.py` is not an established entrypoint. |
| CatalogMatrix schema | **CONFIRMED permissive placeholder** | It requires only `id` and permits arbitrary additional properties. |
| CatalogMatrix contract | **CONFIRMED draft** | It defines an inspectability aid, not proof or release authority. |
| CatalogMatrix fixture README | **CONFIRMED absent at exact path** | No meaningful fixture family is established by the checked path. |
| Proof-side CatalogMatrix README | **CONFIRMED absent at exact path** | ADR-0011's proposed instance home is not established by a lane README. |
| Release closure resolver | **NOT ESTABLISHED in bounded search** | ADR-0022's proposed live enforcement is not a current implementation claim. |
| Shared validator runtime | **CONFIRMED executable elsewhere** | Shared mechanics exist but do not establish this lane. |
| Shared aggregate | **CONFIRMED five entries; closure absent** | Catalog closure is not registered in the observed aggregate. |
| Dedicated tests and CI | **NOT ESTABLISHED** | No direct closure suite, fixtures, artifact, pass result, or required gate is claimed. |
| Production consumers, metrics and deployment | **UNKNOWN** | No operational maturity claim is made. |

### Bounded absence language

The checks above are commit-scoped and path-scoped. They do not prove that historical, ignored, generated, branch-local, dynamically loaded, package-local, external, or uninspected implementations never existed.

[Back to top](#top)

---

<a id="placement"></a>

## Directory Rules and authority

Directory Rules place this README under `tools/` because validators are implementation/checker concerns. Topic does not move authority into this folder.

| Responsibility | Owning root or lane | This lane's relationship |
|---|---|---|
| Individual catalog record validation | [`tools/validators/catalog/`](../catalog/README.md) | Required dependency; not duplicated here. |
| Shared catalog-closure readiness | `tools/validators/catalog_closure/` | This lane. |
| Domain-specific closure | `tools/validators/domains/<domain>/catalog_closure/` when verified | Child specialization; shared rules remain here. |
| Shared validator mechanics | [`tools/validators/_common/`](../_common/README.md) | Reusable runtime only. |
| Catalog construction | [`pipelines/catalog/`](../../../pipelines/catalog/README.md), catalog package lanes | Builders; not validation authority. |
| Catalog records | [`data/catalog/`](../../../data/catalog/README.md) | CATALOG-stage records and indexes. |
| STAC, DCAT, PROV records | `data/catalog/stac/`, `data/catalog/dcat/`, `data/catalog/prov/` | Catalog carriers. |
| Domain catalog records | `data/catalog/domain/` | Domain-scoped discovery/index records. |
| Triplet/graph projection | `data/triplets/` | Paired derived projection; not catalog truth. |
| Source descriptors and governance registries | `data/registry/` | Source, rights, sensitivity, and registry authority. |
| Evidence and proof support | `data/proofs/` | EvidenceBundle, ProofPack, and accepted proof records. |
| Receipts and process memory | `data/receipts/` | Run and validation process memory. |
| Contracts and schemas | `contracts/`, `schemas/` | Meaning and shape. |
| Policy decisions and rules | `policy/` and accepted decision homes | Admissibility authority. |
| Review and release governance | `release/` and accepted review homes | Promotion, release, correction, withdrawal, rollback. |
| Published public-safe artifacts | `data/published/` | Downstream delivery artifacts after release. |
| Tests and fixtures | `tests/`, `fixtures/` | Enforceability proof. |
| Public clients | Governed APIs and released artifacts | Must not read this lane or internal stores directly. |

### Allowed contents

Good fits include:

- this README;
- future validator source that checks a declared closure packet against accepted contracts, schemas, policy adapters, and dependency results;
- validator-local registry or dispatch metadata after a canonical entrypoint decision;
- safe diagnostic templates;
- references to synthetic fixtures and tests;
- compatibility adapters that do not create a second authority;
- documentation of finite outcomes, dependencies, migration, and rollback.

### Forbidden contents

Do not store:

- STAC, DCAT, PROV, domain catalog, or index records;
- CatalogMatrix, EvidenceBundle, ProofPack, ValidationReport, receipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, or RollbackCard instances;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads;
- schemas, contracts, policy modules, source registry records, release records, public catalogs, search indexes, hosted artifacts, or route handlers;
- secrets, credentials, private endpoints, signed URLs, sensitive coordinates, restricted-source payloads, or hidden policy parameters.

[Back to top](#top)

---

<a id="topology"></a>

## Validator topology

The parent should stay thin and explicit.

```text
catalog record validators
  tools/validators/catalog/
            |
            v
catalog closure parent
  tools/validators/catalog_closure/
            |
            +--> source / rights / sensitivity validators
            +--> evidence / citation / proof validators
            +--> lifecycle / freshness / policy validators
            +--> release / correction / rollback validators
            +--> domain child catalog-closure validators
            |
            v
structured readiness report
  not proof, not policy, not release
```

| Concern | Delegate or authority | Parent check |
|---|---|---|
| STAC/DCAT/PROV record shape and local semantics | `catalog/` | Require identified profile and successful child result. |
| Domain object-family coverage | Domain closure child | Require configured child result; do not invent domain rules. |
| Source identity, role, rights and cadence | Source/rights validators and registry | Require resolvable refs and acceptable child results. |
| EvidenceRef/EvidenceBundle and citations | Evidence/proof/citation validators | Require resolution and configured closure state. |
| Lifecycle and freshness | Lifecycle/freshness validators | Require valid stage/time posture. |
| Policy and sensitivity | Policy/sensitivity validators | Require decision/ref; never decide policy locally. |
| Release/correction/rollback | Release validators and release authority | Check refs/readiness; never approve. |
| STAC/DCAT/PROV cross-record agreement | Accepted closure profile | Compare only declared fields under a versioned profile. |
| CatalogMatrix | Accepted contract/schema/home after decision | Validate only after authority and shape are resolved. |

### Parent/child rule

A child result may narrow or block the parent result. The parent must not convert `DENY`, `HOLD`, `ABSTAIN`, `REVIEW_REQUIRED`, `ERROR`, stale, or unresolved child states into `PASS`.

[Back to top](#top)

---

<a id="scope"></a>

## Closure scope

Every invocation must name one bounded scope.

| Scope | Meaning | Typical next gate | Required caution |
|---|---|---|---|
| `CATALOG_CANDIDATE` | A candidate set of catalog records before release review. | Catalog review or hold. | Not public and not proof closure. |
| `DOMAIN_CATALOG_SLICE` | One domain's catalog set plus configured domain-child results. | Domain steward review. | Domain child owns domain-specific invariants. |
| `RELEASE_CANDIDATE` | Catalog/evidence/policy package associated with a release candidate. | Promotion/release review. | Passing is not a PromotionDecision. |
| `PUBLISHED_AUDIT` | Audit of already released catalog and dependency references. | Continue, correct, supersede, withdraw, or rollback review. | Never silently mutate released state. |
| `CORRECTION_IMPACT` | Dependency closure after a source, evidence, policy, catalog, or release correction. | Correction cascade review. | Affected public carriers may need withdrawal. |

A generic unbounded "validate the catalog" request should produce `ABSTAIN`, `HOLD`, or `ERROR`, not a broad pass.

[Back to top](#top)

---

<a id="non-claims"></a>

## What closure does not prove

A successful configured closure check does **not** prove:

- that the underlying claims are true;
- that an EvidenceBundle is valid beyond its delegated result;
- that rights or sensitivity policy allows release;
- that a reviewer approved the package;
- that the package is legally distributable;
- that the release is complete outside the declared scope;
- that a CatalogMatrix is proof closure by itself;
- that a ReleaseManifest exists or is approved unless explicitly resolved;
- that public routes, hosting, search, tiles, exports, Focus Mode, or AI surfaces are safe;
- that production and CI invoke this validator;
- that no uninspected dependency exists;
- that a prior release remains valid after correction.

The safe statement is:

> The configured closure checks completed for the declared packet, profile versions, input digests, dependencies, operation, and audience, with the reported outcome and findings.

[Back to top](#top)

---

<a id="packet"></a>

## Proposed validation packet

No accepted packet schema is confirmed. A future implementation should accept an immutable, bounded envelope similar to:

```yaml
packet_version: kfm.catalog_closure.packet.v1
request_id: req_example
closure_scope: RELEASE_CANDIDATE
requested_operation: review_release_candidate
requested_audience: internal_release_review
network_allowed: false

target:
  release_candidate_ref: kfm://release-candidate/example
  target_digest: sha256:<hex>
  lifecycle_state: CATALOG

profiles:
  catalog_closure_profile_ref: kfm://profile/catalog-closure/v1
  catalog_closure_profile_digest: sha256:<hex>
  stac_profile_ref: kfm://profile/stac/v1
  dcat_profile_ref: kfm://profile/dcat/v3
  prov_profile_ref: kfm://profile/prov-o/v1

catalog_refs:
  stac_refs: []
  dcat_refs: []
  prov_refs: []
  domain_catalog_refs: []
  index_refs: []
  triplet_refs: []

support_refs:
  source_descriptor_refs: []
  evidence_refs: []
  proof_refs: []
  validation_report_refs: []
  policy_decision_refs: []
  review_record_refs: []
  receipt_refs: []

release_context:
  release_manifest_ref: null
  published_artifact_refs: []
  correction_refs: []
  supersession_refs: []
  withdrawal_refs: []
  rollback_ref: null

child_results: []
resource_limits:
  max_records: 1000
  max_reference_depth: 8
  max_findings: 500
```

All fields, enums, paths, limits, and identifiers above are **PROPOSED**.

### Packet rules

- Refs must be immutable or version-pinned where consequences depend on them.
- Digests must bind the checked bytes, not display labels.
- The requested operation and audience must be explicit.
- Profiles and policy bundles must be identified by version and digest.
- `network_allowed` defaults to `false`.
- Missing optional families must be distinguishable from empty, not-applicable, denied, or unresolved families.
- Public or release-bound operations require correction and rollback context.
- The packet must not embed sensitive payloads merely to validate their references.

[Back to top](#top)

---

<a id="dependency-envelope"></a>

## Dependency result envelope

The parent should consume structured dependency results, not parse log prose.

```yaml
dependency_id: catalog-record-stac
validator_ref: kfm://validator/catalog/stac/v1
validator_digest: sha256:<hex>
target_digest: sha256:<hex>
outcome: PASS
findings: []
resolved_refs: []
obligations: []
checked_at: 2026-07-16T00:00:00Z
```

A dependency result must identify:

- validator and rule/profile versions;
- target digest;
- finite outcome;
- structured findings with reason codes;
- resolved and unresolved references;
- obligations and blockers;
- safe timestamps and execution identity;
- whether network access occurred;
- any truncation or resource-limit condition.

Unversioned, target-mismatched, stale, malformed, or payload-leaking dependency results must not be accepted as closure support.

[Back to top](#top)

---

<a id="invariants"></a>

## Closure invariants

A future implementation should enforce only accepted rules, but the following are the proposed minimum invariant families.

### Scope and determinism

1. Closure scope, operation, audience, lifecycle stage, target ref, and target digest are explicit.
2. The same packet, rules, dependency results, and local repository state produce the same ordered findings.
3. Validators do not use network access by default.
4. Unknown profile, schema, policy, or dependency versions fail closed.
5. Truncation and resource limits are visible and cannot yield an unqualified pass.

### Catalog and identity

6. Each catalog ref resolves to the exact record and digest named by the packet.
7. Record-local validators have passed or returned an explicitly accepted bounded state.
8. One canonical artifact identity is used consistently across configured closure records.
9. Aliases, external identifiers, display names, and canonical identifiers remain distinct.
10. Checksums/digests compare normalized declared values without silent coercion.
11. A geometry, title, URL, filename, collection membership, or proximity match is not identity proof.

### Support and governance

12. SourceDescriptor refs resolve for source-derived records.
13. Source roles remain fixed and do not upgrade through cataloging or release preparation.
14. Consequential claim-bearing entries resolve to EvidenceRef/EvidenceBundle or accepted proof support.
15. ValidationReport refs identify the exact target/rule/input digests they report on.
16. Rights, sensitivity, and policy posture is explicit where material.
17. Required review state is present and scoped to the target/version.
18. Release references are checked for consistency but never created or approved locally.

### Lifecycle and public boundary

19. RAW, WORK, QUARANTINE, unresolved PROCESSED candidates, and denied/restricted records do not become public catalog dependencies.
20. Catalog and triplet states remain paired projections, not interchangeable truth.
21. Catalog closure is not publication and does not authorize public hosting, search, map, API, export, Focus Mode, or AI use.
22. Public-facing diagnostics contain no restricted metadata, sensitive geometry, private endpoint, or internal storage path.
23. The most restrictive applicable rights/sensitivity/policy posture propagates through the closure package.

### Correction and reversibility

24. Superseded, withdrawn, corrected, stale, or revoked dependencies cannot remain silently active.
25. Corrections identify affected catalog records, matrices, proofs, releases, and public carriers.
26. Public-impacting packages carry a rollback target or a blocking finding.
27. Validators append findings and audit references; they do not mutate trust records in place.
28. A corrected package receives a new identity/digest and preserves the prior audit trail.

### Authority separation

29. Receipt is not proof.
30. Proof is not catalog.
31. Catalog is not publication.
32. ValidationReport is not PolicyDecision.
33. CatalogMatrix is not EvidenceBundle, ProofPack, ReleaseManifest, or PromotionDecision.
34. Validator success is not release approval.
35. Domain children extend shared closure but do not redefine shared families or neighboring-domain truth.

[Back to top](#top)

---

<a id="agreement"></a>

## STAC/DCAT/PROV agreement

ADR-0022 is **proposed**, not accepted authority. Its proposed release-level invariant is still valuable as an explicit review target:

| Agreement dimension | Proposed check | Failure posture |
|---|---|---|
| Canonical artifact identity | STAC, DCAT, PROV, matrix, and release context refer to one content-addressed artifact identity. | `DENY`, `HOLD`, or `ABSTAIN`. |
| Bytewise digest | Declared checksums and release artifact digests agree after profile-defined normalization. | `DENY`. |
| Release reference | Release-bound records cite the same immutable release reference. | `DENY` or `HOLD`. |
| Producing activity | PROV activity and catalog links identify the declared producing run/activity. | `FAIL` or `ABSTAIN`. |
| Upstream sources | Source refs and PROV derivation links resolve to admitted sources. | `FAIL`, `HOLD`, or `ABSTAIN`. |
| Evidence support | Catalog records and matrix cells cite the accepted EvidenceBundle/proof support. | `ABSTAIN` or `HOLD`. |
| Profile version | Each record identifies an accepted profile/namespace version. | `FAIL` or `REVIEW_REQUIRED`. |

This README does not activate ADR-0022, select its field names, or claim the proposed resolver exists.

[Back to top](#top)

---

<a id="support"></a>

## Source, evidence and validation closure

### Source closure

For each source-derived catalog entry:

- the SourceDescriptor ref resolves;
- source identity, role, rights, sensitivity, cadence, authority limits, and supersession posture are available to delegated validators;
- cataloging does not upgrade source role;
- source withdrawal or correction propagates to dependent closure packages;
- aggregator or derived records preserve underlying source distinctions where required.

### Evidence and proof closure

For each consequential claim or release-bound artifact:

- EvidenceRef resolves to the intended EvidenceBundle or accepted proof object;
- the evidence target, artifact, source, and time scope match the catalog claim;
- proof references are not receipts or catalog records mislabeled as proof;
- unresolved citations, digests, signatures, or attestations remain blocking according to accepted policy;
- evidence changes after release trigger correction-impact review.

### Validation closure

Required ValidationReports must:

- target the exact record/artifact digest;
- identify validator/rule/profile digests;
- use finite outcomes;
- expose blocking findings and obligations;
- distinguish skipped, not-applicable, unresolved, stale, truncated, and error states;
- link process receipts separately;
- not be treated as proof closure or policy/release approval.

[Back to top](#top)

---

<a id="governance"></a>

## Policy, review and release readiness

The parent checks the presence and consistency of governance results. It does not produce them.

| Governance family | Parent question | Forbidden conclusion |
|---|---|---|
| Rights | Are use, redistribution, attribution, and audience constraints resolved for this operation? | "A catalog entry means reuse is allowed." |
| Sensitivity | Did the most restrictive applicable posture propagate to catalog metadata and public carriers? | "Metadata cannot leak sensitive facts." |
| Policy | Is a versioned PolicyDecision or accepted child result present for the target and audience? | "Validation pass equals ALLOW." |
| Review | Are required steward/security/rights/domain reviews present and current? | "A reviewer name in metadata is approval." |
| Release | Is the release reference consistent, immutable, and appropriate to the scope? | "Release reference means release is approved." |
| Correction | Are supersession, withdrawal, correction, and rollback obligations closed or blocking? | "The latest file silently replaces prior release." |

A release authority may consume a closure report as one input. The closure report cannot promote or publish.

[Back to top](#top)

---

<a id="lifecycle"></a>

## Lifecycle and public boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| State or transition | Closure posture |
|---|---|
| RAW / WORK / QUARANTINE | Never a public catalog dependency. |
| PROCESSED candidate | May be evaluated for catalog readiness; remains non-public. |
| CATALOG / TRIPLET | Closure may be evaluated; directory placement alone does not imply release. |
| Release candidate | Requires evidence, policy, review, release, correction, and rollback readiness. |
| PUBLISHED | Audit closure against immutable release state and public-safe carriers. |
| Corrected / superseded / withdrawn | Recompute dependency closure and invalidate affected outputs as governed. |

Public clients must consume governed APIs or released artifacts. They must not read the closure packet, internal CatalogMatrix candidate, proof store, source registry, canonical store, or validator output directly as public truth.

[Back to top](#top)

---

<a id="matrix-conflict"></a>

## CatalogMatrix conflict register

Current evidence is internally inconsistent and must remain visible.

| Question | Evidence A | Evidence B | Current posture |
|---|---|---|---|
| Instance family/home | Proposed ADR-0011 places `CatalogMatrix` in `data/proofs/catalog_matrix/<domain>/` or ProofPack. | Proposed ADR-0022 describes a release/catalog matrix and examples under catalog-oriented paths. | **CONFLICTED — ADR/steward decision required.** |
| Meaning | Contract calls CatalogMatrix an inspectability aid and not proof closure. | ADR-0022 uses it as the explicit release-level closure object alongside a resolver. | **Compatible only if matrix and resolver roles are separated explicitly.** |
| Schema home | Confirmed placeholder at `schemas/contracts/v1/data/catalog_matrix.schema.json`. | ADR-0022 proposes catalog-family schema paths. | **CONFLICTED / NEEDS VERIFICATION.** |
| Validator path | Schema metadata names `tools/validators/data/validate_catalog_matrix.py`, which is absent. | Observed top-level `tools/validators/validate_catalog_matrix.py` is a stub; this lane is README-only. | **CONFLICTED / no canonical executable.** |
| Fixture home | Schema metadata names `fixtures/data/catalog_matrix/`. | Exact README was absent; no meaningful coverage was established. | **NEEDS VERIFICATION.** |
| Domain schemas | Domain-specific CatalogMatrix schema files appear in search. | Their semantics, completeness, registry status, fixtures, and relationship to the global placeholder are not established here. | **NEEDS VERIFICATION.** |

Until resolved:

1. Do not create a second CatalogMatrix schema, instance home, or executable.
2. Do not treat the placeholder schema as semantic closure.
3. Do not use the stub as a working gate.
4. Do not make `catalog_closure/` the CatalogMatrix instance store.
5. Require an ADR or reviewed migration note before canonicalization.
6. Keep compatibility and rollback mechanical.

[Back to top](#top)

---

<a id="report"></a>

## Proposed ValidationReport profile

No accepted closure-report schema was established. A future report should be bounded and deterministic.

```yaml
report_version: kfm.catalog_closure.report.v1
report_id: ccl_report_<digest>
validator_ref: kfm://validator/catalog-closure/v1
validator_digest: sha256:<hex>
input_digest: sha256:<hex>
closure_scope: RELEASE_CANDIDATE
outcome: HOLD
readiness_level: NOT_READY
findings:
  - code: CCL_RELEASE_REF_MISSING
    severity: BLOCKING
    target_ref: kfm://release-candidate/example
    message: Required immutable release reference was not resolved.
child_results: []
resolved_refs: []
unresolved_refs: []
obligations: []
affected_public_refs: []
correction_impact: REVIEW_REQUIRED
truncated: false
network_used: false
```

### Report rules

- Findings use stable reason codes and deterministic ordering.
- Messages are safe and do not include sensitive payload values.
- A report identifies the exact packet and rule/profile digests.
- `PASS` means only the configured closure checks passed.
- `DENY`, `HOLD`, `ABSTAIN`, `REVIEW_REQUIRED`, and `ERROR` remain first-class.
- A report cannot be used as a receipt, EvidenceBundle, PolicyDecision, ReviewRecord, PromotionDecision, or ReleaseManifest.
- Report storage and retention remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

<a id="outcomes"></a>

## Outcomes and reason codes

### Proposed top-level outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | All configured closure checks passed for the declared scope; continue only to the next governed gate. |
| `FAIL` | One or more configured structural or semantic closure checks failed. |
| `DENY` | A policy-significant, sensitive, rights, public-boundary, or release-critical condition blocks the operation. |
| `HOLD` | Required dependency, review, correction, or governance support is incomplete. |
| `REVIEW_REQUIRED` | Human/steward review is required before a safe decision. |
| `ABSTAIN` | The validator cannot support a decision from the available bounded evidence. |
| `ERROR` | The validator or dependency failed; no target-validity inference is permitted. |

### Proposed `CCL_` reason-code families

| Family | Representative codes |
|---|---|
| Packet/scope | `CCL_PACKET_INVALID`, `CCL_SCOPE_MISSING`, `CCL_OPERATION_MISSING`, `CCL_AUDIENCE_MISSING`, `CCL_TARGET_DIGEST_MISSING` |
| Profiles/rules | `CCL_PROFILE_UNRESOLVED`, `CCL_PROFILE_DIGEST_MISMATCH`, `CCL_SCHEMA_PLACEHOLDER`, `CCL_RULESET_CONFLICT` |
| Entry points/coverage | `CCL_ENTRYPOINT_MISSING`, `CCL_CHILD_RESULT_MISSING`, `CCL_CHILD_RESULT_FAILED`, `CCL_FIXTURE_COVERAGE_MISSING` |
| Catalog records | `CCL_STAC_REF_MISSING`, `CCL_DCAT_REF_MISSING`, `CCL_PROV_REF_MISSING`, `CCL_DOMAIN_CATALOG_REF_MISSING`, `CCL_RECORD_VALIDATION_FAILED` |
| Agreement | `CCL_IDENTITY_MISMATCH`, `CCL_DIGEST_MISMATCH`, `CCL_RELEASE_REF_MISMATCH`, `CCL_PRODUCING_ACTIVITY_MISMATCH`, `CCL_CROSS_LINK_DRIFT` |
| Sources/evidence | `CCL_SOURCE_DESCRIPTOR_MISSING`, `CCL_SOURCE_ROLE_COLLAPSE`, `CCL_EVIDENCE_REF_MISSING`, `CCL_EVIDENCE_UNRESOLVED`, `CCL_PROOF_FAMILY_COLLAPSE` |
| Validation | `CCL_VALIDATION_REPORT_MISSING`, `CCL_VALIDATION_REPORT_TARGET_MISMATCH`, `CCL_VALIDATION_REPORT_FAILED`, `CCL_VALIDATION_REPORT_STALE` |
| Governance | `CCL_RIGHTS_UNRESOLVED`, `CCL_SENSITIVITY_UNRESOLVED`, `CCL_POLICY_DECISION_MISSING`, `CCL_POLICY_DENY`, `CCL_REVIEW_STATE_MISSING` |
| Lifecycle/public | `CCL_LIFECYCLE_INVALID`, `CCL_UNRELEASED_PUBLIC_REFERENCE`, `CCL_CATALOG_TRIPLET_DRIFT`, `CCL_PUBLIC_METADATA_LEAKAGE`, `CCL_PUBLIC_BYPASS` |
| Matrix/path conflicts | `CCL_MATRIX_HOME_CONFLICT`, `CCL_MATRIX_SCHEMA_CONFLICT`, `CCL_MATRIX_VALIDATOR_CONFLICT`, `CCL_MATRIX_NOT_PROOF`, `CCL_MATRIX_NOT_RELEASE` |
| Correction/release | `CCL_RELEASE_REFERENCE_MISSING`, `CCL_CORRECTION_CHAIN_INCOMPLETE`, `CCL_SUPERSEDED_ACTIVE`, `CCL_WITHDRAWN_ACTIVE`, `CCL_ROLLBACK_TARGET_MISSING` |
| Runtime/security | `CCL_NETWORK_ACCESS_DENIED`, `CCL_NONDETERMINISTIC_RESULT`, `CCL_RESOURCE_LIMIT`, `CCL_DIAGNOSTIC_LEAKAGE`, `CCL_INTERNAL_ERROR` |

The accepted vocabulary must eventually live in a contract/schema/registry or other verified authority, not only this README.

[Back to top](#top)

---

<a id="security"></a>

## Security and resource posture

Catalog metadata can leak more than the underlying public artifact.

A future validator must:

- default to local, no-network resolution;
- reject remote fetches unless an explicit, policy-approved mode exists;
- constrain path traversal, symlinks, URI schemes, archive expansion, reference depth, record count, finding count, and input size;
- avoid dereferencing private endpoints, signed URLs, credentials, internal hostnames, or restricted object stores;
- never print sensitive coordinates, hidden fields, authorization headers, secrets, full private URLs, or restricted metadata in diagnostics;
- inspect output metadata for reverse-engineerable sensitive locations, infrastructure vulnerability, living-person/DNA, archaeology, rare-species, private-land, or restricted-source context;
- preserve the most restrictive rights and sensitivity posture;
- distinguish resolution failure from not-found, denied, malformed, stale, or policy-blocked;
- make truncation, skipped checks, and resource limits explicit;
- emit safe identifiers/digests rather than payload excerpts.

[Back to top](#top)

---

<a id="tests"></a>

## Tests and fixtures

No dedicated closure test implementation is established. The following is a proposed minimum suite.

### Fixture principles

- synthetic, public-safe, deterministic, no-network;
- fake but structurally realistic refs and digests;
- no production source payloads, private endpoints, signed URLs, secrets, restricted identifiers, sensitive coordinates, or live release records;
- explicit valid, invalid, denied, held, abstain, review, stale, superseded, withdrawn, corrected, and error polarity;
- nonempty fixture assertions;
- immutable expected outcomes and reason codes.

### Proposed fixture matrix

| Fixture | Expected result |
|---|---|
| Complete candidate closure with matching local refs | `PASS` |
| STAC/DCAT/PROV identity mismatch | `DENY` or blocking `FAIL` |
| Digest mismatch against release context | `DENY` |
| Release ref mismatch | `DENY` |
| Missing SourceDescriptor | `HOLD` or `ABSTAIN` |
| Source role silently upgraded | `FAIL` or `DENY` |
| Missing EvidenceBundle for claim-bearing entry | `ABSTAIN` or `HOLD` |
| ValidationReport target digest mismatch | `FAIL` |
| Policy decision missing | `HOLD` |
| Policy outcome `DENY` | `DENY` |
| Review required but absent | `REVIEW_REQUIRED` |
| RAW/WORK/QUARANTINE public reference | `DENY` |
| Sensitive metadata leakage | `DENY` |
| CatalogMatrix treated as proof or release | `FAIL` |
| Superseded dependency still active | `HOLD` or `DENY` |
| Withdrawn dependency still public | `DENY` |
| Missing rollback target for public-impacting package | `HOLD` |
| Unknown profile/version | `ABSTAIN` or `REVIEW_REQUIRED` |
| Network fetch attempt in default mode | `ERROR` or `DENY` |
| Excessive reference depth or record count | `ERROR` with resource-limit code |
| Determinism replay | Byte-stable normalized report |
| Child domain closure failure | Parent cannot pass |
| Empty valid or invalid fixture family | Test failure |

### Proposed tests

- packet and dependency-envelope schema tests;
- profile dispatch and version pinning;
- identity/digest/release-ref agreement;
- reference resolution and cycle handling;
- source/evidence/validation/policy/review/release closure;
- lifecycle and public-boundary denial;
- rights/sensitivity metadata leakage;
- correction/supersession/withdrawal/rollback cascade;
- finite outcomes, exit codes, structured diagnostics, and deterministic ordering;
- no-network, path safety, symlink, URI-scheme, archive, depth, size, and timeout controls;
- parent/child result propagation;
- placeholder-schema and unresolved-ADR blockers;
- zero-fixture and anti-tautology controls.

[Back to top](#top)

---

<a id="ci"></a>

## CI admission

Current shared CI runs `make schemas` and a fail-closed EvidenceBundle canary. That does not establish catalog-closure coverage.

A future dedicated check should require:

1. canonical entrypoint and registry metadata;
2. accepted packet/report contracts and schemas;
3. accepted CatalogMatrix authority/home decision;
4. meaningful nonempty fixtures;
5. deterministic no-network execution;
6. positive, negative, denied, held, abstain, stale, correction, and rollback tests;
7. structured report artifact retention;
8. reason-code stability checks;
9. dependency/child coverage manifest;
10. resource and path-safety tests;
11. documented correction and rollback path;
12. explicit promotion dependency only after governance acceptance.

The workflow must not claim catalog closure because a placeholder schema accepted arbitrary properties or because the stub was skipped.

[Back to top](#top)

---

<a id="sequence"></a>

## Smallest sound implementation sequence

Each step should be a separate, reversible review unit.

### PR 1 — Resolve authority and path conflicts

- decide CatalogMatrix semantic role and instance/schema homes;
- decide canonical validator and registry entrypoint;
- document ADR-0011/ADR-0022 disposition or migration;
- identify accepted catalog, proof, report, policy, and release dependencies;
- define compatibility and rollback targets.

### PR 2 — Contracts, schemas and vocabularies

- define packet, dependency result, closure report, finding, outcome, and reason-code contracts;
- strengthen CatalogMatrix schema only if its role is accepted;
- pin profile and namespace versions;
- add schema registry records and examples.

### PR 3 — Local resolver adapters

- implement bounded local ref resolution;
- reuse shared validator mechanics;
- delegate record-local, source, evidence, policy, lifecycle, release, and domain checks;
- prohibit network and side effects by default.

### PR 4 — Fixtures and tests

- add public-safe fixture families;
- assert nonempty valid/invalid sets;
- cover conflicts, stale state, correction, withdrawal, rollback, leakage, resources, and determinism;
- add parent/child propagation tests.

### PR 5 — Canonical entrypoint and reports

- select one executable and registry ID;
- deprecate aliases/stubs with warnings and compatibility tests;
- emit the accepted structured report to the accepted destination;
- document exit codes and retention.

### PR 6 — CI and governed release integration

- add dedicated CI;
- retain reports and coverage metadata;
- connect to promotion only after policy/release review;
- run rollback and correction drills;
- update docs and operational ownership.

[Back to top](#top)

---

<a id="done"></a>

## Definition of done

This lane is not implemented merely because a README, schema, matrix, or script exists.

- [ ] Owners and CODEOWNERS are accepted.
- [ ] CatalogMatrix authority, meaning, instance home, and schema home are resolved.
- [ ] ADR-0011 and ADR-0022 disposition is recorded.
- [ ] One canonical validator entrypoint and registry ID is accepted.
- [ ] Placeholder and alias/stub migration is documented.
- [ ] Packet, dependency result, report, finding, outcome, and reason-code contracts are accepted.
- [ ] STAC/DCAT/PROV profiles and KFM namespace are version-pinned.
- [ ] Source, evidence, validation, policy, review, release, correction, and rollback dependencies are identified.
- [ ] Domain-child routing and coverage manifest are complete.
- [ ] Meaningful valid/invalid/deny/hold/abstain/review/error/stale/correction fixtures exist.
- [ ] Fixture families are asserted nonempty.
- [ ] Tests cover determinism, no-network, path safety, resource limits, and diagnostic leakage.
- [ ] Record-local and child validator results are consumed as structured envelopes.
- [ ] Reports are stored in an accepted non-authority destination with retention rules.
- [ ] CI runs the exact accepted entrypoint and retains evidence of results.
- [ ] Release integration is reviewed and cannot treat pass as approval.
- [ ] Correction, supersession, withdrawal, and rollback cascade is tested.
- [ ] Public routes consume only governed released artifacts.
- [ ] Documentation, migration notes, and rollback targets are current.
- [ ] Human review approves the implementation and generated receipt.

[Back to top](#top)

---

<a id="migration"></a>

## Migration and deprecation

Current drift includes:

- README-only `catalog_closure/`;
- top-level `validate_catalog_matrix.py` stub;
- absent schema-declared `tools/validators/data/validate_catalog_matrix.py`;
- permissive global schema plus searched domain-specific schemas;
- proposed proof-side and catalog/release-side matrix homes;
- domain child closure lanes without established executable registration.

A safe migration should:

1. inventory all entrypoints, schema metadata, imports, fixtures, workflows, docs, and consumers;
2. resolve authority through ADR/steward review;
3. select one canonical executable and registry ID;
4. add compatibility shims only when needed;
5. emit deprecation warnings with replacement and end date;
6. update schema metadata, docs, tests, workflows, and consumers together;
7. prevent dual writes or divergent result vocabularies;
8. verify rollback before removing a compatibility route;
9. preserve historical reports and receipts;
10. retire stubs only after replacement behavior is proven.

Do not silently repurpose the existing stub or create another parallel validator path.

[Back to top](#top)

---

<a id="rollback"></a>

## Correction and rollback

### Documentation rollback

Before merge, close the draft PR and abandon the branch. After merge, revert the documentation commit and restore prior blob `fef3e0df1d566d2839b6c3da17d75723f16628fc` through a reviewed branch; revert or supersede the generated receipt.

### Future implementation rollback

A mature implementation must support:

- disabling the validator registry entry without deleting reports;
- restoring the prior rules/profile version;
- replaying fixtures against the rollback target;
- invalidating reports generated by a defective validator version;
- identifying releases and public carriers that depended on affected reports;
- routing affected releases to correction, supersession, withdrawal, or rollback review;
- preserving source, evidence, policy, review, release, and receipt history;
- preventing a rollback from reactivating denied, stale, or vulnerable behavior.

Validator rollback does not roll back source truth, evidence, policy, or release authority automatically; it creates a governed impact-review obligation.

[Back to top](#top)

---

<a id="open"></a>

## Open verification register

| ID | Verification item | Status |
|---|---|---|
| CCL-OV-01 | Confirm owners and CODEOWNERS. | NEEDS VERIFICATION |
| CCL-OV-02 | Confirm complete direct-lane file inventory. | NEEDS VERIFICATION |
| CCL-OV-03 | Confirm all catalog-closure executables, imports and dynamic registry entries. | NEEDS VERIFICATION |
| CCL-OV-04 | Decide canonical CatalogMatrix semantic role. | NEEDS VERIFICATION |
| CCL-OV-05 | Decide canonical CatalogMatrix instance home. | NEEDS VERIFICATION |
| CCL-OV-06 | Decide canonical CatalogMatrix schema home. | NEEDS VERIFICATION |
| CCL-OV-07 | Record ADR-0011 disposition. | NEEDS VERIFICATION |
| CCL-OV-08 | Record ADR-0022 disposition. | NEEDS VERIFICATION |
| CCL-OV-09 | Reconcile ADR-0011 and ADR-0022. | NEEDS VERIFICATION |
| CCL-OV-10 | Decide canonical validator entrypoint and registry ID. | NEEDS VERIFICATION |
| CCL-OV-11 | Resolve schema-declared missing validator path. | NEEDS VERIFICATION |
| CCL-OV-12 | Decide disposition of top-level NotImplementedError stub. | NEEDS VERIFICATION |
| CCL-OV-13 | Inventory domain-specific CatalogMatrix schemas and semantics. | NEEDS VERIFICATION |
| CCL-OV-14 | Confirm meaningful CatalogMatrix fixture home and coverage. | NEEDS VERIFICATION |
| CCL-OV-15 | Confirm closure packet contract and schema. | NEEDS VERIFICATION |
| CCL-OV-16 | Confirm dependency result contract and schema. | NEEDS VERIFICATION |
| CCL-OV-17 | Confirm closure report contract/schema and storage destination. | NEEDS VERIFICATION |
| CCL-OV-18 | Confirm accepted finite outcomes and reason-code registry. | NEEDS VERIFICATION |
| CCL-OV-19 | Confirm STAC profile version. | NEEDS VERIFICATION |
| CCL-OV-20 | Confirm DCAT profile version. | NEEDS VERIFICATION |
| CCL-OV-21 | Confirm PROV/PAV profile version. | NEEDS VERIFICATION |
| CCL-OV-22 | Resolve KFM catalog namespace and extension fields. | NEEDS VERIFICATION |
| CCL-OV-23 | Confirm identity canonicalization and digest normalization. | NEEDS VERIFICATION |
| CCL-OV-24 | Confirm SourceDescriptor/source-role dependency behavior. | NEEDS VERIFICATION |
| CCL-OV-25 | Confirm EvidenceRef/EvidenceBundle resolver behavior. | NEEDS VERIFICATION |
| CCL-OV-26 | Confirm proof-family and CatalogMatrix relationship. | NEEDS VERIFICATION |
| CCL-OV-27 | Confirm ValidationReport semantics and target binding. | NEEDS VERIFICATION |
| CCL-OV-28 | Confirm policy/data runtime entrypoints and bundle parity. | NEEDS VERIFICATION |
| CCL-OV-29 | Confirm rights and sensitivity metadata-leakage profiles. | NEEDS VERIFICATION |
| CCL-OV-30 | Confirm review-record requirements and freshness. | NEEDS VERIFICATION |
| CCL-OV-31 | Confirm release-ref and ReleaseManifest resolver behavior. | NEEDS VERIFICATION |
| CCL-OV-32 | Confirm correction, supersession, withdrawal and rollback cascade. | NEEDS VERIFICATION |
| CCL-OV-33 | Confirm complete domain-child catalog-closure inventory. | NEEDS VERIFICATION |
| CCL-OV-34 | Confirm parent/child result propagation and most-restrictive outcome. | NEEDS VERIFICATION |
| CCL-OV-35 | Confirm catalog/triplet consistency rules. | NEEDS VERIFICATION |
| CCL-OV-36 | Confirm public-route, hosting, search, map, export, Focus Mode and AI enforcement. | NEEDS VERIFICATION |
| CCL-OV-37 | Confirm no-network default and approved exception mechanism. | NEEDS VERIFICATION |
| CCL-OV-38 | Confirm path, URI, symlink, archive, depth, size and timeout limits. | NEEDS VERIFICATION |
| CCL-OV-39 | Confirm safe diagnostic redaction and retention. | NEEDS VERIFICATION |
| CCL-OV-40 | Confirm dedicated tests and nonempty fixture assertions. | NEEDS VERIFICATION |
| CCL-OV-41 | Confirm deterministic replay and ordering. | NEEDS VERIFICATION |
| CCL-OV-42 | Confirm dedicated CI artifact and required-check status. | NEEDS VERIFICATION |
| CCL-OV-43 | Confirm promotion-gate adoption and separation of duties. | NEEDS VERIFICATION |
| CCL-OV-44 | Confirm production invocation, consumers and metrics. | UNKNOWN |
| CCL-OV-45 | Confirm current pass/fail results and branch protection significance. | UNKNOWN |
| CCL-OV-46 | Confirm deprecation window and compatibility retirement. | NEEDS VERIFICATION |
| CCL-OV-47 | Confirm operational rollback and correction drill results. | UNKNOWN |
| CCL-OV-48 | Confirm documentation and evidence ledger update ownership. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="ledger"></a>

## Evidence ledger

| Evidence | Blob / result | Supports | Does not prove |
|---|---|---|---|
| Target README | `fef3e0df1d566d2839b6c3da17d75723f16628fc` | Existing lane and v0.1 boundary. | Executable behavior. |
| Catalog-record sibling | `2b05c5e0054862d2990e59adfead83f14f409d5f` | Record-local versus closure split. | Closure implementation. |
| CatalogMatrix contract | `c67923beb505aa39e7c0c768c16e75a00826ff31` | Matrix meaning and non-authority boundaries. | Complete shape, proof closure, release approval. |
| CatalogMatrix schema | `75a927376066226d8a0f89a630d7bb3693143c41` | Placeholder schema and metadata paths. | Semantic completeness. |
| Top-level validator stub | `91ecf78675cf19672a0e94a3899df3074c36ddc4` | A placeholder exists and raises `NotImplementedError`. | Working validation. |
| Missing schema-declared validator path | exact 404 | Path drift. | Historical or branch-local absence. |
| Missing fixture README | exact 404 | Checked fixture root is not established by README. | No fixture bytes anywhere. |
| Missing proof-side matrix README | exact 404 | ADR-0011 instance lane is not established by README. | No matrix instances anywhere. |
| ADR-0011 | `158ad6d31946d7d32537d5278ec6d2828ec880b3` | Proposed four-family separation and proof-side matrix home. | Accepted decision or compliance. |
| ADR-0022 | `b09c1d7aaa39f3030afdcec419c58236fd324f17` | Proposed must-agree and closure-resolver design. | Accepted decision or implementation. |
| Soil domain child | `298c4a3ecff2c9fdf548a0a2da46b701f1df6cb2` | Parent/child delegation pattern. | Executable child coverage. |
| Validator tests parent | `c703a64eef3f69044a54696f121f4e5ae05a3631` | Shared runtime and partial aggregate/test boundary. | Closure tests or pass results. |
| Shared aggregate | `3375cce172631dc3675cf2e46bb7788d273ff425` | Five hard-coded non-placeholder entrypoints. | Catalog closure registration. |
| Validator workflow | `7651f0571ba8f879819b197155d160c08f9fe7ac` | `make schemas` and EvidenceBundle canary. | Dedicated closure CI. |
| Bounded searches | commit-scoped search | No direct closure executable/resolver/test surfaced. | Global or historical nonexistence. |

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- Replaced the broad v0.1 proposal with a repository-grounded README-only boundary.
- Aligned with the grounded catalog-record sibling.
- Recorded the CatalogMatrix stub, missing declared path, placeholder schema, missing checked fixture/proof lanes, and aggregate exclusion.
- Preserved ADR-0011/ADR-0022 conflict without selecting a path.
- Added closure scope, proposed packet, dependency envelope, invariants, agreement, governance, lifecycle, report, outcomes, reason codes, security, tests, CI, implementation sequence, definition of done, migration, rollback, verification register, and evidence ledger.
- Changed documentation only.

[Back to top](#top)
