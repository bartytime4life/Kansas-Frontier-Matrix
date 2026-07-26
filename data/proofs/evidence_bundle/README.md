<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-evidence-bundle-readme
title: data/proofs/evidence_bundle/ — EvidenceBundle Proof Support
type: directory-readme
subtype: evidence-bundle-proof-family
version: v0.2.0
status: repository-grounded draft; schema and bounded fixture validation confirmed; cross-record resolver, policy, release, access, and runtime closure remain bounded
owners:
  - "NEEDS VERIFICATION — Evidence and EvidenceBundle steward"
  - "NEEDS VERIFICATION — proof, validation, citation, policy, review, and release stewards"
  - "NEEDS VERIFICATION — domain, correction, rollback, Evidence Drawer, governed-AI, and docs stewards"
created: NEEDS VERIFICATION — a greenfield stub predated the v0.1 expansion
updated: 2026-07-26
policy_label: public-doc; proof-support; evidence-bundle; cite-or-abstain; no-direct-public-path; release-gated
path: data/proofs/evidence_bundle/README.md
prepared_under_prompt: KFM Markdown Modernization & GitHub Documentation Implementation Agent v4.0.0
truth_posture: >
  CONFIRMED exact target path and prior blob, Directory Rules proof placement, canonical proofs-root
  contract, Atmosphere and Flora child-lane documents, fielded EvidenceBundle semantic contract and
  Draft 2020-12 schema, dedicated validator wrapper, minimal valid/invalid fixtures, schema test harness,
  and read-only pull-request workflow boundaries / PROPOSED authoritative instance-versus-index profile,
  cross-domain bundle packet, invalidation propagation, and downstream handoff requirements / UNKNOWN
  recursive proof payload inventory, active writers and consumers, generated indexes, access controls,
  public routes, caches, hosting, release instances, and public effects / NEEDS VERIFICATION accountable
  owners, accepted materialization profile, cross-record EvidenceRef resolution, policy and review
  enforcement, release/correction/rollback integration, complete fixture coverage, current remote check
  conclusions, and operational rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 01d927659c183d252fc655eeffb1f44f0e0830ad
  prior_blob: bf304383b725db95e0f8902f0c7c59d0a3cd0ee3
  blank_stub_lineage_blob: e01c7dd1b5b6f8fe81f5c96e7820f6151b0d2120
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  proofs_root_blob: 0d8b6e92d3b4b9ff3961d29c53ead497922a31cf
  atmosphere_child_blob: 9106953a468386cbc3065469ba3a5b18849fb7ee
  flora_child_blob: 2259e9b91a9d6d461e7c620e1a403e9bca74a19e
  evidence_bundle_contract_blob: 731c348832add23cddd14e796aa56ce2b9268259
  evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  evidence_bundle_validator_blob: c1760c5e92eae6390f5adcde4593e8e9bab26535
  evidence_bundle_fixtures_readme_blob: 89ace659414a757c14a4d3e516fd31d44c6a9969
  validator_suite_workflow_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
  schema_validation_workflow_blob: e6b26337aa1eea142b96560e041419f855c44d59
  evidence_resolver_workflow_blob: cfa1555433d74a135462aba84ee1e052ae7f3ac9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ../README.md
  - ../../README.md
  - atmosphere/README.md
  - flora/README.md
  - ../citation_validation/README.md
  - ../citation_validation/atmosphere/README.md
  - ../citation_validation/flora/README.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md
  - ../../../tools/validators/validate_evidence_bundle.py
  - ../../../tests/schemas/test_common_contracts.py
  - ../../../policy/evidence/README.md
  - ../../../release/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/validator-suite.yml
  - ../../../.github/workflows/schema-validation.yml
  - ../../../.github/workflows/evidence-resolver.yml
notes:
  - "Same-path Markdown modernization only; no proof payload, contract, schema, policy, validator, fixture, workflow, release, route, hosting, or publication state changed."
  - "EvidenceBundle is a claim-scope closure artifact. It is not an EvidenceRef, PolicyDecision, ReviewRecord, ReleaseManifest, receipt, source registry, public response body, map layer, or AI-answer authority."
  - "The dedicated schema wrapper passed its minimal valid/invalid fixture polarity check in this task using exact connector-fetched bytes from the pinned base. This proves bounded machine-shape behavior only."
  - "The evidence-resolver workflow explicitly remains a readiness hold; cross-record EvidenceRef-to-EvidenceBundle resolution is not claimed."
  - "The v0.1 documentation rollback target is prior blob bf304383b725db95e0f8902f0c7c59d0a3cd0ee3; the earlier blank-stub lineage blob is retained for history."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/proofs/evidence_bundle/` — EvidenceBundle Proof Support

> **One-line purpose.** Hold or index governed, claim-scoped EvidenceBundle proof artifacts that preserve evidence references, source records, citations, rights, sensitivity, transforms, integrity, correction lineage, and release dependencies without becoming public truth or release authority.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: proof support](https://img.shields.io/badge/authority-proof%20support-0969da?style=flat-square)](#authority-level)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-1a7f37?style=flat-square)](#evidencebundle-requirements)
[![EvidenceBundle validator suite](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/validator-suite.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/validator-suite.yml)
[![Exposure: no direct public path](https://img.shields.io/badge/exposure-no%20direct%20public%20path-b42318?style=flat-square)](#outputs)

> [!IMPORTANT]
> **Evidence closure is necessary but not sufficient for publication.** A structurally valid EvidenceBundle can support policy, review, and release evaluation, but it does not make a claim true, current, rights-cleared, sensitivity-safe, reviewed, released, public, or KFM-published.

> [!CAUTION]
> Missing, stale, conflicting, role-collapsed, rights-unclear, sensitivity-unsafe, unreleased, withdrawn, invalidated, or unresolvable support must produce a contract-defined finite negative result such as `ABSTAIN`, `HOLD`, `RESTRICT`, `DENY`, or `ERROR`—not plausible completion.

> [!WARNING]
> Do not place secrets, restricted source material, exact or reverse-engineerable protected locations, living-person or genomic data, private-land joins, critical-infrastructure detail, redaction offsets, transform secrets, access instructions, or other control-defeating material in this ordinary repository lane.

- **Path:** `data/proofs/evidence_bundle/README.md`
- **Owning responsibility:** `data/proofs/`
- **Proof family:** `evidence_bundle/`
- **Direct public access:** denied
- **Documentation rollback target:** prior blob `bf304383b725db95e0f8902f0c7c59d0a3cd0ee3`

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Lifecycle](#lifecycle-relationship) · [Repo fit](#repo-fit) · [Evidence](#evidence-ledger) · [Lanes](#lane-index) · [Artifact classes](#accepted-contents) · [Schema](#evidencebundle-requirements) · [Guardrails](#evidencebundle-guardrails) · [Checklist](#validation-checklist) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger) · [Rollback](#rollback)

---

## Purpose

`data/proofs/evidence_bundle/` is the cross-domain parent lane for materialized EvidenceBundle proof support. It exists to make the evidence side of a bounded claim inspectable before downstream policy, review, release, governed API, Evidence Drawer, export, map, or AI surfaces use that support.

A governed EvidenceBundle should answer, at minimum:

1. What exact `claim_scope` is supported?
2. Which governed `EvidenceRef` values and reconstructable source records are members?
3. Which citations, rights, sensitivity labels, transforms, checksums, and governing spec identity close the bundle?
4. Which domain object families, source roles, spatial and temporal scopes, uncertainty, freshness, corrections, and limitations qualify the support?
5. Which policy, review, release, correction, withdrawal, invalidation, and rollback decisions remain outside the bundle?
6. Which downstream result is justified when support is complete—or incomplete?

This lane supports evidence resolution. It does not admit sources, determine domain truth, decide policy, approve review or release, publish claims, serve public files directly, or authorize AI answers.

## Authority level

**Implementation-bearing proof-support lane under the canonical `data/proofs/` responsibility.**

The responsibility split is deliberate:

- [`contracts/evidence/evidence_bundle.md`](../../../contracts/evidence/evidence_bundle.md) defines EvidenceBundle meaning.
- [`schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) defines machine shape.
- [`fixtures/contracts/v1/evidence/evidence_bundle/`](../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md) provides bounded schema examples.
- [`tools/validators/validate_evidence_bundle.py`](../../../tools/validators/validate_evidence_bundle.py) performs schema-oriented validation.
- [`policy/evidence/`](../../../policy/evidence/README.md), review records, and [`release/`](../../../release/README.md) retain admissibility, review, release, correction, withdrawal, and rollback authority.
- This lane may hold or index materialized EvidenceBundle proof support only under an accepted profile.

When one artifact could fit more than one proof axis, an accepted contract and profile must select one authoritative home. Other lanes may hold immutable references, indexes, or validation summaries; they must not duplicate mutable authority, restricted source material, canonical proof records, or public-state decisions.

This README creates no new proof family, parallel evidence store, public route, or release state.

## Status

| Surface | Bounded result |
|---|---|
| Exact path and prior bytes | **CONFIRMED** at `main@01d927659c183d252fc655eeffb1f44f0e0830ad`; prior blob `bf304383b725db95e0f8902f0c7c59d0a3cd0ee3` |
| Documentation version | `v0.2.0` |
| Canonical proofs responsibility | **CONFIRMED repository-grounded draft** at [`data/proofs/README.md`](../README.md) |
| EvidenceBundle semantic contract | **CONFIRMED fielded draft**; defines claim-scope closure and separates evidence, policy, release, receipts, public APIs, maps, and AI authority |
| EvidenceBundle schema | **CONFIRMED fielded / status `PROPOSED`**; Draft 2020-12, ten required fields, root `additionalProperties: false` |
| Dedicated validator wrapper | **CONFIRMED executable**; points to the canonical schema and fixture root |
| Minimal shared fixtures | **CONFIRMED one valid and one invalid case**; the invalid case omits required `bundle_id` |
| Current task fixture execution | **PASS, bounded**; exact connector-fetched pinned bytes produced the expected valid acceptance and invalid required-property rejection |
| Aggregate schema and contract harness | **CONFIRMED repository implementation**; execution in this task remains **NOT RUN** |
| Validator and schema workflows | **CONFIRMED read-only pull-request workflows**; current remote conclusions remain **UNKNOWN** until this PR runs |
| Cross-record evidence resolver | **HOLD / NEEDS VERIFICATION**; the workflow explicitly says no accepted EvidenceRef-to-EvidenceBundle resolver command is established |
| Concrete recursive bundle inventory | **UNKNOWN**; no recursive payload census or sensitive-content review was performed |
| Public serving, access controls, release instances, hosting, caches, and runtime behavior | **UNKNOWN / denied by default**; path presence creates none of these states |

The workflow badge above reports GitHub's current `validator-suite` status for `main`. It proves only that workflow's configured checks when green; it does not establish evidence closure, source authority, rights, sensitivity, policy approval, release readiness, runtime correctness, or publication.

## What belongs here

Good fits include governed EvidenceBundle-family artifacts whose claim scope, members, rights, sensitivity, transforms, integrity, limitations, and release dependencies remain inspectable:

- field-valid EvidenceBundle instances under an accepted materialization profile;
- immutable indexes or bundle pointers when another accepted store owns the instances;
- EvidenceRef-to-bundle resolution maps that preserve unresolved, denied, stale, and invalidated states;
- claim-to-bundle maps for catalog records, triplets, release candidates, governed API fixtures, Evidence Drawer projections, correction review, and rollback review;
- digest-closure manifests linking admitted source records, processed artifacts, catalog or triplet projections, receipts, proof packets, and release dependencies;
- bundle-member indexes that preserve object family, source role, space, time, rights, sensitivity, uncertainty, freshness, caveats, corrections, and limitations;
- finite negative-state support explaining why claim-grade closure is absent;
- local README, inventory, migration, compatibility, or disposition notes that explain the proof boundary without becoming authority records.

Every artifact must remain subordinate to its semantic contract, schema, policy, review, release, correction, and rollback dependencies.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED source/domain data | The corresponding `data/<phase>/<domain>/` lane |
| SourceDescriptor or source-activation authority | `data/registry/sources/` and accepted source-governance surfaces |
| RunReceipt, TransformReceipt, ValidationReport, RedactionReceipt, AIReceipt, or review receipts as primary records | `data/receipts/` |
| PolicyDecision, access rules, sensitivity rules, or stewardship decisions | `policy/` and governed review records |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, RollbackCard, or release signatures | `release/` |
| Contracts, schemas, validators, fixtures, tests, pipelines, packages, apps, API code, UI code, or styles | Their owning responsibility roots |
| Public maps, tiles, APIs, downloads, Evidence Drawer payloads, Focus Mode text, model prose, or public products | Governed delivery surfaces backed by released public-safe artifacts |
| Generated text, vector retrieval, graph projections, model fields, suitability surfaces, or aggregate data presented as sovereign evidence | Resolve admissible source evidence or abstain |
| Secrets, restricted payloads, harmful precision, control-defeating transform details, or private access instructions | Approved restricted systems, quarantine, redaction, generalization, staged access, or denial |
| A second mutable EvidenceBundle authority | Select one home through an accepted contract/ADR and use immutable references elsewhere |

## Inputs

An EvidenceBundle packet may reference only governed records and must preserve unresolved states instead of fabricating closure.

As applicable, inputs include:

- stable bundle identity and bounded `claim_scope`;
- one or more governed `EvidenceRef` values;
- reconstructable source records and immutable source roles;
- publication-ready citations;
- rights/license and sensitivity posture;
- ordered transforms and content checksums;
- deterministic `spec_hash`;
- object family, geography or generalized geography, valid/source/retrieval/release time, method, uncertainty, confidence, freshness, caveats, and correction state;
- pointers to receipts, validation results, policy decisions, review records, release records, correction notices, withdrawal notices, and rollback targets when those external authorities are required.

References do not transfer authority into this lane. A pointer to a release record does not make the bundle a release record.

## Outputs

Permitted outputs are proof-support artifacts or indexes that make claim-scoped evidence inspectable for downstream validation, policy, review, release, correction, rollback, governed API, Evidence Drawer, export, map, and AI evaluation.

Outputs must not:

- become direct browser, tile, download, search, graph, or model endpoints;
- expose canonical or restricted stores;
- convert a schema pass into evidence truth;
- convert evidence closure into policy or release approval;
- erase stale, denied, withheld, withdrawn, superseded, or corrected state;
- omit the correction and rollback dependencies required by the consuming surface.

Public clients must use governed interfaces and released public-safe projections. They must not read this directory as public truth.

## Validation

Validation is layered. Each check proves only its declared scope.

| Check | Repository command or surface | What a pass proves | What it does not prove |
|---|---|---|---|
| Dedicated EvidenceBundle fixture polarity | `python tools/validators/validate_evidence_bundle.py --fixtures` | The configured valid fixture passes and the configured invalid fixture fails schema validation | Cross-record resolution, semantic sufficiency, policy, review, release, public safety, or runtime behavior |
| Aggregate configured validators | `make schemas` | Configured validator/fixture families preserve expected valid/invalid polarity | Complete schema-tree or domain-profile coverage |
| Schema and contract tests | `python -m pytest -q tests/schemas tests/contracts` | Repository-owned schema/contract tests pass | Source truth, evidence closure, rights, sensitivity, policy, or release approval |
| Pull-request validator workflow | [`validator-suite`](../../../.github/workflows/validator-suite.yml) | Aggregate validators run and the reviewed invalid EvidenceBundle canary fails for the expected missing-`bundle_id` reason | Resolver integrity or publication readiness |
| Pull-request schema workflow | [`schema-validation`](../../../.github/workflows/schema-validation.yml) | Schema JSON, Draft 2020-12 shape, canonical IDs, configured fixtures, and schema/contract tests pass | Semantic truth or lifecycle closure |
| Resolver readiness workflow | [`evidence-resolver`](../../../.github/workflows/evidence-resolver.yml) | Required boundary files remain visible and readiness drift is detected | Actual EvidenceRef-to-EvidenceBundle resolution; the current workflow intentionally reports a hold |

**Authoring validation performed for v0.2.0:** the dedicated wrapper was run against exact connector-fetched bytes for the pinned schema, referenced schemas, runner, and minimal fixture pair. The command returned success after accepting `valid_1.json` and rejecting `invalid_1.json` because `bundle_id` is required. A full repository clone, aggregate suite, pytest suite, GitHub host render, and current remote workflow conclusion were not available in that local check.

## Review burden

Accountable stewardship remains **NEEDS VERIFICATION**. Changes should route through the repository's verified CODEOWNERS pattern while keeping GitHub routing separate from substantive approval.

Review burden scales with the change:

- README-only boundary clarification: proof/evidence and docs review;
- materialized bundle or index change: proof, evidence, domain, source-role, rights, sensitivity, and validation review;
- public-bound use: policy, release, correction, rollback, governed API, UI, and independent review;
- sensitive domains: the applicable cultural, sovereignty, stewardship, living-person, genomic, ecological, infrastructure, or private-land reviewer;
- contract, schema, policy, workflow, or authority changes: their owning-root reviewers and any required ADR.

The generator or author must not be treated as the sole approver for policy-significant or release-significant work.

## Related folders

- Parent responsibility: [`data/proofs/`](../README.md)
- Data root: [`data/`](../../README.md)
- Current child lanes: [`atmosphere/`](atmosphere/README.md) · [`flora/`](flora/README.md)
- Citation validation: [`data/proofs/citation_validation/`](../citation_validation/README.md) · [`atmosphere/`](../citation_validation/atmosphere/README.md) · [`flora/`](../citation_validation/flora/README.md)
- Lifecycle support: [`data/processed/`](../../processed/README.md) · [`data/catalog/`](../../catalog/README.md) · [`data/triplets/`](../../triplets/README.md) · [`data/receipts/`](../../receipts/README.md) · [`data/registry/`](../../registry/README.md) · [`data/published/`](../../published/README.md)
- Evidence meaning: [`EvidenceBundle`](../../../contracts/evidence/evidence_bundle.md) · [`EvidenceRef`](../../../contracts/evidence/evidence_ref.md) · [`CitationValidationReport`](../../../contracts/evidence/citation_validation_report.md)
- Machine shape and examples: [`evidence_bundle.schema.json`](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) · [`evidence_bundle` fixtures](../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md)
- Validation and policy: [`validate_evidence_bundle.py`](../../../tools/validators/validate_evidence_bundle.py) · [`test_common_contracts.py`](../../../tests/schemas/test_common_contracts.py) · [`policy/evidence/`](../../../policy/evidence/README.md)
- Governance and release: [Directory Rules](../../../docs/doctrine/directory-rules.md) · [`release/`](../../../release/README.md)

## ADRs

Relevant proposed decisions include ADR-0001 (schema home), ADR-0011 (receipt/proof/manifest/catalog separation), ADR-0012 (connector output boundary), ADR-0015 (published aliases and rollback split), and ADR-0025 (public clients do not read internal stores).

This README accepts none of them. An accepted ADR plus a migration and rollback plan is required before:

- changing the canonical proof responsibility;
- creating a second mutable EvidenceBundle home;
- promoting a compatibility or generated lane to authority;
- changing lifecycle boundaries;
- approving direct public access;
- collapsing evidence, receipts, catalogs, policy, release, correction, or rollback into one object or folder.

No ADR is required for this same-path Markdown clarification because it does not change placement, authority, lifecycle, object shape, policy, release, or public behavior.

## Last reviewed

- **Date:** 2026-07-26
- **Evidence boundary:** `main@01d927659c183d252fc655eeffb1f44f0e0830ad`
- **Review type:** complete target read; Directory Rules and parent/child README reconciliation; contract, schema, validator, fixture, test, workflow, and CODEOWNERS inspection; bounded exact-byte validator execution
- **Not inspected:** recursive proof payloads, deployed routes, hosting, caches, access controls, release instances, policy decisions, review records, correction propagation, or operational rollback drills
- **Owners and independent approval:** needs verification

Re-review on contract/schema/profile, proof topology, writer/consumer, policy, release, public-interface, correction, withdrawal, or rollback changes—or within six months.

## Lifecycle relationship

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                           \-> data/proofs/evidence_bundle supports claim-scope closure
```

```mermaid
flowchart LR
  SRC["SourceDescriptor<br/>source role · rights · sensitivity"] --> RAW["RAW"]
  RAW --> WQ["WORK / QUARANTINE"]
  WQ --> PROC["PROCESSED"]
  PROC --> CAT["CATALOG / TRIPLET"]
  CAT --> REL["Policy · review · release"]
  REL --> PUB["PUBLISHED"]

  PROC -. "EvidenceRef members" .-> EB["data/proofs/evidence_bundle/{domain}"]
  CAT -. "claim and catalog support" .-> EB
  EB -. "citations and closure" .-> CIT["data/proofs/citation_validation/{domain}"]
  EB -. "references only" .-> RECEIPTS["data/receipts/"]
  EB -. "release dependency" .-> REL
  PUB -. "governed projection" .-> CLIENT["Governed API · Evidence Drawer · map · export · AI"]

  EB -. "does not publish" .-> CLIENT
```

The final dashed edge is a boundary warning, not a data path: EvidenceBundle proof files must not be served directly to public clients.

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Raw source payloads | `data/raw/<domain>/` | Not this lane |
| Work transforms, QA, notebooks, redaction trials | `data/work/<domain>/` | Not this lane |
| Rights-, role-, sensitivity-, quality-, or release-unclear material | `data/quarantine/<domain>/` | Not this lane |
| Normalized domain artifacts | `data/processed/<domain>/` | Not this lane |
| Catalog and provenance records | `data/catalog/` and accepted STAC/DCAT/PROV lanes | Catalog is not EvidenceBundle authority |
| Triplets and graph projections | `data/triplets/` | Projection is not sovereign evidence |
| General domain proof support | `data/proofs/<domain>/` | Domain proof axis |
| EvidenceBundle-family proof support | `data/proofs/evidence_bundle/<domain>/` | This family and its verified children |
| Citation-validation proof support | `data/proofs/citation_validation/<domain>/` | Citation check axis |
| Receipts and review support | `data/receipts/` | Referenced, not owned here |
| Source identity and activation | `data/registry/sources/<domain>/` | Source authority |
| Public-safe released artifacts | `data/published/` | Downstream only |
| Release, correction, withdrawal, rollback | `release/` | Publication authority |
| Semantic meaning | `contracts/evidence/` | Contract authority |
| Machine shape | `schemas/contracts/v1/evidence/` | Schema authority |
| Admissibility | `policy/evidence/` and applicable domain/sensitivity policy | Policy authority |
| Validators, tests, fixtures, pipelines, apps, packages | Their named responsibility roots | Implementation and proof of behavior remain separate |

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Previous target blob `bf304383…` | **CONFIRMED** | Complete v0.1 parent guide and stable headings | Contained stale verification statements and a broad proposed lane table |
| [`data/proofs/README.md`](../README.md) | **CONFIRMED repository-grounded draft** | Canonical proofs responsibility, no-direct-public-path posture, review and rollback boundaries | Recursive payloads and enforcement remain unverified |
| [`contracts/evidence/evidence_bundle.md`](../../../contracts/evidence/evidence_bundle.md) | **CONFIRMED fielded draft** | EvidenceBundle meaning, authority split, fields, closure rules, lifecycle | Contract status is draft; implementation behavior remains separate |
| [`evidence_bundle.schema.json`](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | **CONFIRMED fielded / `PROPOSED` status** | Draft 2020-12 shape, ten required fields, closed top level, metadata links | Shape does not prove cross-record or policy/release closure |
| [`evidence_bundle` fixtures](../../../fixtures/contracts/v1/evidence/evidence_bundle/README.md) | **CONFIRMED minimal family** | One positive and one missing-`bundle_id` negative case | Not domain-specific; not comprehensive |
| [`validate_evidence_bundle.py`](../../../tools/validators/validate_evidence_bundle.py) | **CONFIRMED executable / bounded PASS in this task** | Schema and fixture-root wiring; expected polarity for current minimal fixtures | Not a semantic resolver or publication gate |
| [`test_common_contracts.py`](../../../tests/schemas/test_common_contracts.py) | **CONFIRMED repository implementation / NOT RUN in this task** | Valid/invalid fixture discovery and expected-error behavior | Current aggregate result not locally observed |
| [`validator-suite`](../../../.github/workflows/validator-suite.yml) | **CONFIRMED read-only PR workflow** | Aggregate validator run plus specific missing-`bundle_id` fail-closed canary | Current PR conclusion pending; no cross-record resolution |
| [`schema-validation`](../../../.github/workflows/schema-validation.yml) | **CONFIRMED read-only PR workflow** | Schema meta-validation, fixture inventory, aggregate validators, schema/contract tests | Does not establish semantic truth or release readiness |
| [`evidence-resolver`](../../../.github/workflows/evidence-resolver.yml) | **CONFIRMED explicit readiness hold** | Boundary-file presence and drift detection | No accepted resolver command or denied-resolution suite |
| [`atmosphere/README.md`](atmosphere/README.md) | **CONFIRMED repository-grounded draft** | Atmosphere child boundary, source-role and claim-scope posture | Recursive bundle instances and runtime closure unknown |
| [`flora/README.md`](flora/README.md) | **CONFIRMED repository-grounded draft** | Flora child boundary, sensitivity/geoprivacy and claim-scope posture | Recursive bundle instances and operational enforcement unknown |
| `data/proofs/atmosphere/pm25_2026/evidence_bundle.json` | **CONFIRMED placeholder / not schema-valid evidence** | Shows a proposed placeholder path in a separate domain proof lane | Must not be cited as a concrete valid EvidenceBundle instance |

## Lane index

### Confirmed current child documents

| Child lane | Bounded role | Hard boundary |
|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | Atmosphere claim-scope evidence closure and proof indexing | Not AQI/advisory, regulatory, medical, emergency, public-output, receipt, or release authority |
| [`flora/`](flora/README.md) | Flora claim-scope evidence closure with taxonomy, source-role, sensitivity, and safe-representation posture | Not rare-plant discovery, exact-location disclosure, collection/access guidance, stewardship, policy, public-output, or release authority |

### Unverified candidate domain segments

The v0.1 README named the following candidate child segments. Their placement is consistent with the existing proof-family/domain pattern, but their current path presence, accepted profile, payload inventory, validation, policy, access, release, and review state were not verified in this task:

| Candidate segment | Intended claim-support boundary |
|---|---|
| `agriculture/` | Aggregate, crop, yield, field, and county-year support must not become operator or parcel truth |
| `archaeology/` | Exact sites, cultural authority, stewardship, and sovereignty fail closed |
| `fauna/` | Sensitive nest, den, roost, spawning, and occurrence precision fail closed |
| `habitat/` | Suitability or modeled habitat must not become occurrence truth |
| `hazards/` | Not emergency warning, response, or life-safety authority |
| `hydrology/` | Observation, model, regulatory, and warning source roles remain distinct |
| `people-dna-land/` | Living-person, genomic, title, parcel, and private joins fail closed |
| `roads-rail-trade/` | Not routing, operations, security, or legal road-status authority |
| `settlements-infrastructure/` | Critical assets and dependency graphs are restricted by default |
| `soil/` | Survey, gridded derivative, station, satellite, profile, and suitability support types must not collapse |

These rows are continuity-preserving proposals, not claims that the directories exist.

## Accepted contents

An accepted profile may allow one or more of these artifact classes:

| Artifact class | Purpose | Admission condition |
|---|---|---|
| Materialized EvidenceBundle instance | Close evidence for a bounded claim scope | Schema-valid, profile-valid, source-role/rights/sensitivity complete, policy/review/release dependencies explicit |
| Immutable instance index | Locate accepted instances without duplicating them | Authoritative store and digests resolve; stale/withdrawn state preserved |
| EvidenceRef resolution map | Map refs to bundle members or finite negative states | Resolver contract and deterministic checks accepted |
| Claim-to-bundle map | Bind catalog, triplet, release, API/UI fixture, correction, or rollback scope to support | Claim scope and consumer contract explicit |
| Digest-closure manifest | Preserve integrity across source, processed, catalog/triplet, receipt, proof, and release references | Hash algorithm, canonicalization, membership, and invalidation rules accepted |
| Negative-state support record | Explain missing, stale, denied, restricted, unreleased, withdrawn, or invalidated closure | Outcome vocabulary defined by the consuming contract |
| Documentation/index sidecar | Explain boundary, inventory, migration, or disposition | Must not create mutable authority or public truth |

The accepted materialization profile remains **NEEDS VERIFICATION**. Until it is accepted, new payloads should be held for review rather than inferred from this README.

## Exclusions

Do not use this lane to:

- bypass SourceDescriptor or source-activation review;
- store source-native payloads or canonical processed data;
- replace catalog, triplet, receipt, policy, review, release, correction, withdrawal, or rollback families;
- publish a claim because a file exists or a schema validates;
- treat EvidenceRef as equivalent to EvidenceBundle closure;
- treat EvidenceBundle as equivalent to PolicyDecision or ReleaseManifest;
- expose canonical/internal proof files to public clients;
- convert generated language, retrieval results, maps, tiles, graphs, scenes, screenshots, dashboards, or models into root truth;
- hide uncertainty, caveats, rights, sensitivity, stale state, invalidation, correction, or withdrawal;
- create a parallel mutable evidence or proof authority without an accepted ADR and migration plan.

## EvidenceBundle requirements

The fielded schema currently requires these ten top-level fields:

| Field | Required | Current machine-shape rule | Evidence meaning |
|---|---:|---|---|
| `bundle_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Stable bundle identity |
| `claim_scope` | Yes | String | Exact bounded claim family the bundle may support |
| `evidence_refs` | Yes | Non-empty array of `EvidenceRef` objects | Governed pointers included in closure |
| `source_records` | Yes | Non-empty array of strings | Reconstructable source-record handles |
| `citations` | Yes | Non-empty array of strings | Citation strings for the claim scope |
| `rights` | Yes | Object requiring `license`; no extra fields | Effective rights summary |
| `sensitivity` | Yes | `sensitivity_label` schema reference | Exposure constraints and reason |
| `transforms` | Yes | Array of strings | Ordered derivation steps |
| `checksums` | Yes | Non-empty object; values match `sha256:<64 lowercase hex>` | Integrity over critical inputs and outputs |
| `spec_hash` | Yes | `spec_hash` schema reference | Governing spec identity |

The schema forbids undeclared top-level fields. That is a machine-shape constraint, not proof that the values are true, complete, mutually consistent, current, policy-admissible, reviewed, or released.

Cross-record closure remains a separate obligation:

- every `EvidenceRef` must resolve through an accepted resolver or produce a finite negative state;
- source records, citations, rights, sensitivity, transforms, checksums, and spec identity must agree with their governing records;
- corrections, withdrawals, supersessions, invalidations, and stale state must propagate;
- public-bound consumers must separately verify policy, review, release, correction, and rollback state.

## EvidenceBundle guardrails

- EvidenceBundle is claim-scope evidence closure, not source truth, policy clearance, review approval, release approval, or publication.
- EvidenceBundle outranks generated summaries, but it remains subordinate to admissible source evidence and separate policy/release authorities.
- EvidenceRef is a pointer; EvidenceBundle is a closure artifact. Neither substitutes for the other.
- A structurally valid bundle with unresolved members, conflicting roles, unclear rights, unsafe sensitivity, stale evidence, or missing external decisions must not yield claim-grade completion.
- Cross-domain bundles must preserve each owning lane's object authority, source role, spatial/temporal scope, sensitivity, rights, caveats, and correction lineage.
- Public-bound representations must use released, policy-safe, reviewed, generalized, redacted, staged, withheld, or denied projections as required.
- AI may interpret only governed, released, evidence-supported surfaces through a validated response envelope. AI text is never evidence.
- Public clients and Focus Mode must use governed APIs and released public-safe carriers, not this directory or canonical/internal stores directly.
- A workflow badge, passing schema check, pull request, merge, GitHub release, or file placement does not make a bundle KFM-published.

## Validation checklist

Before adding or changing a payload, index, manifest, or lane guide:

- [ ] The artifact's authoritative class—instance, index, map, manifest, negative-state record, or documentation—is explicit.
- [ ] One accepted home owns mutable authority; other lanes use immutable references.
- [ ] `bundle_id` and `claim_scope` are stable and bounded.
- [ ] All ten required schema fields are present and schema-valid.
- [ ] Every `EvidenceRef` resolves through an accepted mechanism or carries a finite negative state.
- [ ] Source records and source roles are reconstructable and non-collapsed.
- [ ] Citations support the exact claim scope.
- [ ] Rights, sensitivity, spatial precision, temporal scope, uncertainty, freshness, caveats, and limitations are explicit.
- [ ] Transforms, checksums, canonicalization, and `spec_hash` are reconstructable.
- [ ] Validation results and receipts are referenced from their owning roots.
- [ ] Policy, review, release, correction, withdrawal, invalidation, and rollback dependencies are explicit when applicable.
- [ ] Sensitive or control-defeating content is absent, restricted, generalized, redacted, staged, quarantined, or denied.
- [ ] Public clients cannot read the lane directly.
- [ ] Positive and negative fixtures cover the changed behavior.
- [ ] Repository commands and relevant read-only workflows pass for their declared scope.
- [ ] Passing validation is not described as truth, policy approval, release approval, or publication.

## Open verification register

| Item | Status | Evidence required before relying on it |
|---|---:|---|
| Accountable owners and independent reviewer assignments | `NEEDS VERIFICATION` | Approved stewardship records and repository access |
| Authoritative materialization profile | `NEEDS VERIFICATION` | Accepted contract/ADR defining instance, index, generation, identity, retention, and one-writer rules |
| Recursive payload inventory | `UNKNOWN` | Pinned tree, file hashes, LFS/external stores, generated status, rights/sensitivity review |
| Active writers and consumers | `UNKNOWN` | Connector, pipeline, validator, resolver, API/UI, workflow, and deployed-consumer inventory |
| Cross-record EvidenceRef resolution | `HOLD` | Accepted resolver contract, implementation, deterministic valid/denied fixtures, tests, and workflow |
| Domain-profile validation depth | `NEEDS VERIFICATION` | Domain schemas, validators, positive/negative cases, source-role and sensitivity checks |
| Policy and review enforcement | `UNKNOWN` | Executable policy inputs/decisions, review records, negative tests, and CI evidence |
| Release, correction, withdrawal, invalidation, rollback closure | `UNKNOWN` | Emitted instances, identity agreement, release manifests, correction propagation, cache invalidation, drills |
| Public serving and access controls | `UNKNOWN / denied by default` | Governed routes, authorization, hosting, cache, telemetry, and no-direct-store tests |
| Current remote workflow conclusions | `UNKNOWN until PR execution` | PR workflow runs and check conclusions tied to the final head SHA |
| Third-party action immutability | `NEEDS VERIFICATION` | Reviewed immutable action pins or an accepted supply-chain exception |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| v0.1 element | v0.2 disposition |
|---|---|
| Stable path, `doc_id`, H1 role, and top anchor | Preserved |
| Parent EvidenceBundle proof-family purpose | Preserved and made repository-grounded |
| Lifecycle invariant and Mermaid relationship | Preserved and clarified |
| Repo-fit responsibility split | Preserved and aligned with the modernized proofs-root contract |
| Atmosphere and Flora child lanes | Preserved and updated to current repository-grounded child documents |
| Ten proposed domain child segments | Preserved as explicitly unverified candidate segments rather than path facts |
| Accepted content and exclusion lists | Preserved, deduplicated, and sharpened |
| EvidenceBundle requirements and guardrails | Preserved and grounded in the current semantic contract and fielded schema |
| Sensitivity, rights, source-role, finite-negative-state, public-client, correction, and rollback controls | Preserved and strengthened |
| Prior evidence ledger and validation checklist | Preserved with current schema, validator, fixture, test, and workflow evidence |
| Original stub lineage and rollback reference | Preserved as historical lineage |
| Payload, move, rename, deletion, workflow, schema, policy, release, or public-state change | None |

## Rollback

Before merge, rollback means closing the draft pull request or abandoning its review branch; neither action changes proof payloads or public state.

After merge, restore this documentation with a transparent revert of the implementation commit or by restoring prior blob:

```text
bf304383b725db95e0f8902f0c7c59d0a3cd0ee3
```

The earlier blank-stub lineage remains:

```text
e01c7dd1b5b6f8fe81f5c96e7820f6151b0d2120
```

Documentation rollback does not roll back proof payloads, contracts, schemas, policies, release records, routes, caches, or public artifacts. Any operational rollback must use the owning lifecycle, correction, withdrawal, cache-invalidation, and release controls.

## Change history

### v0.2.0 — 2026-07-26

- reconciled the parent lane with current Directory Rules and the modernized proofs-root contract;
- replaced stale schema, validator, fixture, and CI unknowns with bounded repository evidence;
- preserved the v0.1 child-lane and domain-candidate continuity without presenting proposals as existing paths;
- added exact schema fields, layered validation commands, workflow boundaries, resolver hold, review burden, open verification, no-loss, and rollback controls;
- modernized GitHub presentation with evidence-backed badges, alerts, navigation, tables, links, and an updated lifecycle diagram;
- changed Markdown only.

### v0.1 — 2026-06-25

- expanded a greenfield stub into the first EvidenceBundle proof-family guide;
- established lifecycle, repo-fit, child-lane, accepted-content, exclusion, guardrail, evidence-ledger, validation, and rollback sections.

[Back to top](#top)
