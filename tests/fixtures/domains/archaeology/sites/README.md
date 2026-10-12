# `tests/fixtures/domains/archaeology/sites/` — Archaeology Sites Test-Local Fixture and Site-Identity Boundary

> Repository-grounded routing and safety contract for test-local Archaeology site-shaped examples. This lane may describe small synthetic manifests and expectations owned by specific tests, but it does not create site records, confirm candidates, define object authority, prove evidence, approve review or policy, release geometry, publish map/API/AI artifacts, or expose protected archaeological detail.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-sites-readme
title: tests/fixtures/domains/archaeology/sites/README.md — Archaeology Sites Test-Local Fixture and Site-Identity Boundary
type: readme; directory-readme; test-local-fixture-lane; archaeology-sites-routing-boundary; site-identity-test-boundary
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; tests-fixtures-parent-confirmed; archaeology-parent-confirmed; domains-parent-index-absent; singular-reusable-site-lane-readme-only; reusable-site-and-candidate-placeholders-confirmed; primary-site-schemas-permissive; site-name-conflict-visible; public-safe-fixture-home-conflict-visible; executable-enforcement-unestablished; non-authoritative
owners: OWNER_TBD — Archaeology domain steward · Test steward · Fixture steward · Site-identity steward · GIS steward · Sensitivity reviewer · Cultural-review liaison · Rights-holder representative · Evidence steward · Contract/schema steward · Policy steward · Review steward · Release steward · Correction/rollback steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doc; tests; fixtures; archaeology; sites-fixtures; test-local-only; synthetic-only; no-network-default; deny-by-default; candidate-not-confirmed; component-not-site; exact-location-denied; cultural-authority-deferred; evidence-required; review-gated; policy-gated; release-subordinate; correction-aware; revocation-aware; rollback-aware; no-publication
current_path: tests/fixtures/domains/archaeology/sites/README.md
truth_posture:
  CONFIRMED:
    - target README v0.1 and prior blob
    - tests/fixtures parent README and test-local fixture-home rule
    - tests/fixtures/domains/archaeology parent README and sites child index
    - singular fixtures/domains/archaeology/site README is the observed reusable site-shaped lane
    - direct sites lane and singular reusable site lane are README-only in bounded evidence
    - checked synthetic ArchaeologicalSite and CandidateFeature JSON files are four-field PROPOSED placeholders
    - ArchaeologicalSite, CandidateFeature, SiteComponent, and Site compatibility semantic contracts
    - ArchaeologicalSite, CandidateFeature, and SiteComponent paired permissive PROPOSED schemas
    - OBJECT_MAP expects ArchaeologicalSite, CandidateFeature, and SiteComponent and marks all NEEDS VERIFICATION
    - Site short-name contract is compatibility/lineage only and is not current object-map authority
    - two public-safe Archaeology fixture lanes coexist with unresolved compatibility
    - Archaeology validator lane is README-only in bounded evidence and sampled enforcement remains scaffolded
    - checked absence of tests/fixtures/domains/README.md
    - checked absence of direct-lane conftest.py, manifest_expectations.json, and representative test module
    - checked absence of tests/domains/archaeology/fixtures/sites/README.md
  CONFLICTED:
    - v0.1 claim that tests/fixtures/domains/archaeology/README.md was absent
    - v0.1 proposed executable test modules inside a fixture directory versus parent guidance
    - plural test-local sites path versus singular reusable site path
    - Site compatibility name versus object-map ArchaeologicalSite family
    - corpus term Feature may map to SiteComponent or CandidateFeature
    - root-level and domain-facing public-safe Archaeology fixture lanes coexist without a final canonical decision
    - fixture filenames imply valid, deny, or generalized behavior while payloads are only placeholders
    - rich object semantics versus permissive empty-property schemas
  UNKNOWN:
    - exhaustive fixture inventory outside checked paths
    - generated, ignored, branch-local, dynamic, or externally stored fixtures
    - real evidence, review, cultural-authority, rights, consent, policy, release, and production workflows
    - branch-protection significance, current pass rates, and production use
  NEEDS_VERIFICATION:
    - lane-retention decision and accepted test-local fixture threshold
    - canonical Site versus ArchaeologicalSite migration decision
    - Feature-to-SiteComponent/CandidateFeature reconciliation
    - accepted site, candidate, component, source-role, geometry, reason-code, and obligation vocabularies
    - substantive payloads, schemas, validators, consumer tests, and backlinks
    - accepted public-safe fixture-home relationship
    - policy, cultural review, candidate promotion, CI, correction, revocation, cache invalidation, and rollback enforcement
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0d0f8109486763c7b4099a7a7b8b4c9fbed7219d
  target_prior_blob: 3db34077e8736f9d42bb9a471dfda3ae98ee0437
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    schema_home_adr: ab0010a278d766356845c23055f882f328abb418
    drift_register: 97a775522dcd058299f752ac7862d0fc56c13280
    tests_fixtures_parent_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    archaeology_test_fixtures_parent: 34b8aa536aa19c234f30f939ed1c06fa428b57dc
    singular_site_fixture_readme: 01562c74ff68b7cb9e3cdf15f89771236eb45339
    synthetic_site_readme: 7411bf141b1c9aca24f0dd2c804871dd1222e967
    synthetic_site_generalized_placeholder: 99a71c7326062db7c8f7fcd0c48ca42ddef6edf8
    synthetic_candidate_readme: c713b9803bc2b092fc9e25c3e07576878babea41
    synthetic_candidate_valid_placeholder: 33433a22afd41bd0e685f3d30d81b2a528d941ba
    synthetic_candidate_deny_placeholder: 6e4f6b65bef0272b41ece51e23e0a57340825b94
    archaeological_site_contract: 2bd6729c7e4c118958f4de7f6f81a0425bea1216
    archaeological_site_schema: 5a1371a2fb4dc6d1a5c7b13f7c5198823ae89b40
    candidate_feature_contract: 8167e1e3be69c177a069249b597947f1ef529695
    candidate_feature_schema: 103fa2d86448490f83a0b9918fcd1c2d445fe269
    site_component_contract: e10ba89b19a88df64c21ab7a40c1914926a1754c
    site_component_schema: 096a572bc2ebdfed8f5d9ff5a7ce5114e07e4b67
    site_compatibility_contract: 841ef554709218ae4c1029e493ad152cc7a219d4
    archaeology_object_map: 69da4c6eb259ba5e41149ff0cde4c825f5290e10
    root_public_safe_fixture_readme: 1611242b09ec089b4c9312846f49a7fdfb2b2b5f
    domain_public_safe_fixture_readme: 621b85912ceba3e1e6169318788ad130da7baac5
    archaeology_validator_readme: bae2eabb5d29bf7099ed74a66a17c0071ae98557
    archaeology_policy_readme: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
    archaeology_sensitivity_doc: ca7888f2d43f022faeef5e1a6e16ab00526cf7aa
    archaeology_publication_policy_doc: 835bd3afb1b6a41de8f598d16b794873df0b6f75
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    domain_archaeology_workflow: b6a2869314efe2e34890baa5bbbe41d656629dd3
  direct_lane_files_confirmed:
    - tests/fixtures/domains/archaeology/sites/README.md
  checked_absent_paths:
    - tests/fixtures/domains/README.md
    - tests/fixtures/domains/archaeology/sites/conftest.py
    - tests/fixtures/domains/archaeology/sites/manifest_expectations.json
    - tests/fixtures/domains/archaeology/sites/test_site_fixture_manifest_shape.py
    - tests/domains/archaeology/fixtures/sites/README.md
notes:
  - "v0.2 corrects the stale missing-parent claim and keeps this direct lane documentation-only."
  - "Executable tests belong in an owning tests lane and consume declarative fixtures by reference."
  - "The singular reusable site lane is also README-only in bounded search."
  - "Primary site-family contracts are semantically rich, but their checked schemas are permissive scaffolds."
  - "The checked synthetic site and candidate JSON files are planned-file placeholders; filenames do not prove behavior."
  - "This README preserves naming and fixture-home conflicts instead of selecting a silent winner."
  - "This revision changes documentation only and creates no site record, candidate record, fixture payload, test, schema, contract, policy, validator, workflow, receipt, proof, release record, map artifact, AI output, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Scope: test local" src="https://img.shields.io/badge/scope-test__local-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Candidate: not confirmed" src="https://img.shields.io/badge/candidate-not__confirmed-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-scope) · [Authority](#authority-and-directory-rules-basis) · [Object model](#site-object-model-and-anti-collapse-rules) · [Fixture homes](#fixture-home-and-compatibility-rules) · [Admission](#test-local-fixture-admission-contract) · [Manifest](#minimum-sites-fixture-manifest) · [Cases](#required-fixture-families-and-case-matrix) · [Safety](#sensitivity-location-and-public-surface-safety) · [Execution](#determinism-no-network-and-side-effects) · [Coverage](#inventory-consumers-and-vacuous-pass-risk) · [Commands](#validation-commands) · [CI](#ci-and-promotion-boundary) · [Maintenance](#maintenance-migration-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@0d0f8109486763c7b4099a7a7b8b4c9fbed7219d`  
> **Prior target blob:** `3db34077e8736f9d42bb9a471dfda3ae98ee0437`  
> **Direct lane:** README-only in bounded evidence  
> **Parent state:** `tests/fixtures/README.md` and `tests/fixtures/domains/archaeology/README.md` exist; `tests/fixtures/domains/README.md` was not found  
> **Reusable site lane:** `fixtures/domains/archaeology/site/README.md` exists; no direct payload surfaced in bounded search  
> **Executable consumer child:** not established at `tests/domains/archaeology/fixtures/sites/`

This directory is a routing README. It is not a fixture corpus, executable suite, site registry, candidate queue, schema family, validator, policy bundle, evidence store, review registry, release queue, map source, API source, AI source, or publication surface.

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from repository files or bounded connector search at the pinned snapshot. |
| `PROPOSED` | A recommended contract, path, fixture, test, command, or gate not established as current implementation. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Repository sources preserve incompatible or unresolved alternatives; no silent winner is selected. |
| `DENY` | A prohibited confirmation, authority, exposure, or publication interpretation. |

[Back to top](#top)

---

## Purpose and scope

`tests/fixtures/domains/archaeology/sites/` documents test-local expectations for site-shaped Archaeology fixtures.

Its durable question is:

> Can a bounded synthetic fixture exercise site, candidate, component, evidence, review, policy, sensitivity, release, correction, and rollback behavior without becoming a real site record, confirming a candidate, leaking protected detail, or creating public authority?

A mature lane should prove that:

- `CandidateFeature` remains a candidate until governed promotion closes evidence, review, policy, and sensitivity requirements;
- `SiteComponent` remains a part or sub-unit and does not become a whole site by naming or aggregation;
- `ArchaeologicalSite` fixture shape does not prove that a site exists;
- the short `Site` compatibility name cannot create a second canonical object family;
- exact and reverse-engineerable location detail is denied before public carriers are produced;
- fixture success cannot substitute for EvidenceBundle support, ReviewRecord, PolicyDecision, PromotionDecision, ReleaseManifest, or RollbackCard;
- correction, withdrawal, revocation, supersession, cache invalidation, and rollback remain inspectable.

### In scope

- small synthetic test-local manifests and expectation maps;
- valid, invalid, denied, abstained, quarantined, superseded, withdrawn, correction, and rollback cases;
- candidate-not-confirmed, component-not-site, exact-detail-denied, generalized, and withheld-state examples;
- local no-network and public-no-leak inputs owned by named consumer tests.

### Out of scope

- real site or candidate records;
- exact coordinates, raw geometry, private-owner detail, cultural knowledge, collection-security detail, or looting-risk information;
- source exports, lifecycle data, production payloads, logs, secrets, or telemetry;
- schema, contract, policy, evidence, review, receipt, release, map, API, pipeline, or AI authority.

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules treat root folders as responsibility boundaries. This path is already under `tests/`, so the smallest sound change is to keep it in place and clarify its test-local routing role.

| Responsibility | Owning home | Relationship to this lane |
|---|---|---|
| Test-local fixture wrappers | `tests/fixtures/domains/archaeology/sites/` | This README; direct payload admission requires a named consumer. |
| Executable assertions | `tests/domains/archaeology/fixtures/sites/` or another verified test lane | PROPOSED consumer child; not established here. |
| Reusable site-shaped fixtures | `fixtures/domains/archaeology/site/` | Observed singular reusable lane; referenced, not copied. |
| Synthetic site/candidate examples | `fixtures/domains/archaeology/synthetic_archaeological_site/`, `synthetic_candidate_feature/` | Reusable examples; checked files are placeholders. |
| Object meaning | `contracts/domains/archaeology/` | Contracts define semantics. |
| Machine shape | `schemas/contracts/v1/domains/archaeology/` | Schemas define shape; checked site-family schemas are permissive scaffolds. |
| Admissibility | `policy/` | Policy decides allow, restrict, hold, deny, or abstain. |
| Evidence and review | governed evidence/review roots | Fixtures may carry toy refs only. |
| Release and rollback | `release/` | Fixtures never approve publication. |
| Public map/API/AI carriers | governed released surfaces | Must consume released public-safe derivatives only. |

> [!CAUTION]
> Do not create a second site registry, schema home, policy home, review store, evidence store, release queue, or public map source under this path.

[Back to top](#top)

---

## Site object model and anti-collapse rules

| Object or term | Verified semantic posture | Fixture rule |
|---|---|---|
| `ArchaeologicalSite` | Reviewed site identity; current object-map expected site family. | Shape is not truth; requires evidence/review/policy lineage. |
| `CandidateFeature` | Possible archaeology-relevant feature requiring review and governed promotion. | Must remain visibly candidate; no label, filename, map symbol, or prose may confirm it. |
| `SiteComponent` | Reviewed part or sub-unit associated with a site. | A component is not a whole site and does not prove its association. |
| `Site` | Compatibility/lineage short name; not current object-map authority. | Must not become a parallel canonical contract or fixture vocabulary. |
| `Feature` | May map to `SiteComponent` or `CandidateFeature`; conflict unresolved. | Fixture must name the intended object family explicitly. |

Core invariants:

1. Candidate-to-site promotion is a governed state transition, not a rename.
2. Component-to-site aggregation does not prove a site identity.
3. Schema acceptance does not prove truth, source authority, review completion, policy allowance, geometry safety, or release.
4. Maps, tiles, screenshots, exports, indexes, graph edges, embeddings, and generated text are carriers, not evidence.
5. Source role, object family, lifecycle state, sensitivity, and uncertainty must not be silently upgraded.
6. Unknown or conflicting object-family vocabulary fails closed for consequential use.

[Back to top](#top)

---

## Fixture home and compatibility rules

### Singular reusable lane versus plural test-local lane

- `fixtures/domains/archaeology/site/` is the observed reusable site-shaped fixture lane.
- `tests/fixtures/domains/archaeology/sites/` is a plural test-local routing path.
- The plural path must not become a duplicate reusable fixture registry.
- A test-local wrapper must point to a named consumer and explain why the reusable lane is insufficient.

### Public-safe fixture lanes

Two public-safe Archaeology fixture READMEs exist:

- `fixtures/archaeology-public-safe/`
- `fixtures/domains/archaeology-public-safe/`

Their canonical relationship is unresolved. This README does not select a winner. Do not duplicate payloads across them without:

- a migration note;
- source and destination checksums;
- a declared canonical owner;
- consumer updates;
- a deprecation period;
- a rollback path.

### Fixture-home decision law

| Need | Preferred route |
|---|---|
| Reusable site fixture shared by multiple consumers | `fixtures/domains/archaeology/site/` after fixture-owner review. |
| Test-only wrapper or expectation manifest | This lane, only with a named consumer backlink. |
| Executable test module | Owning `tests/` lane, not this fixture directory. |
| Renderer/runtime public-safe corpus | Existing public-safe lane chosen through a documented compatibility decision. |
| Real site, candidate, component, or lifecycle record | Governed data lifecycle—not any fixture lane. |

[Back to top](#top)

---

## Test-local fixture admission contract

A file may enter this direct lane only when all requirements below are met.

| Requirement | Required evidence |
|---|---|
| Test-local need | A named consuming test, validator test, renderer test, or policy test. |
| No reusable duplication | Explanation of why a reusable fixture reference is insufficient. |
| Synthetic marker | Explicit fixture/non-authoritative marker and fake identity. |
| Object family | One explicit family: `ArchaeologicalSite`, `CandidateFeature`, `SiteComponent`, or compatibility test. |
| Source role | Explicit primary/corroborating/context/restricted/toy posture as applicable; no silent upcast. |
| Geometry safety | No exact protected geometry or reverse-geocodable hint. |
| Expected result | Finite outcome and safe reason code. |
| Prohibited claims | Canary list for site confirmation, exact location, review, policy, release, map truth, and AI truth. |
| Consumer backlink | Consumer points to fixture; fixture manifest points back to consumer. |
| Lifecycle | Correction, withdrawal, revocation, supersession, or rollback behavior when material. |

A filename such as `valid.json`, `deny.json`, or `public_generalized_tile.json` does not satisfy this contract by itself.

[Back to top](#top)

---

## Minimum sites fixture manifest

The following is illustrative and `PROPOSED`; it is not an accepted schema.

```json
{
  "fixture_manifest_id": "kfm://fixture-test/archaeology/sites/example",
  "fixture_version": "v1",
  "domain": "archaeology",
  "fixture_scope": "test_local",
  "fixture_authority": "non_authoritative",
  "synthetic": true,
  "consumer_refs": [
    "tests/domains/archaeology/fixtures/sites/test_candidate_not_site.py"
  ],
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_candidate_feature/example.json",
  "object_family": "CandidateFeature",
  "object_posture": "candidate_not_confirmed",
  "source_role": "toy_context",
  "geometry_posture": "withheld_or_generalized",
  "contains_exact_geometry": false,
  "contains_reconstruction_hint": false,
  "evidence_ref": "evidence-ref:fixture:example",
  "review_ref": null,
  "policy_decision_ref": null,
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card:fixture:example",
  "expected_test_outcome": "ABSTAIN",
  "expected_domain_outcome": "candidate_retained",
  "reason_code": "SITE_FIXTURE_DOES_NOT_CONFIRM_CANDIDATE",
  "must_not_claim": [
    "SITE_EXISTS",
    "CANDIDATE_CONFIRMED",
    "EXACT_LOCATION_PUBLIC",
    "REVIEW_COMPLETE",
    "POLICY_ALLOWED",
    "RELEASED",
    "MAP_TRUTH",
    "AI_TRUTH"
  ]
}
```

Required future schema decisions include identity, versioning, object-family enums, source-role enums, geometry posture, expected outcomes, safe reason codes, evidence/review/policy/release refs, and lifecycle invalidation fields.

[Back to top](#top)

---

## Required fixture families and case matrix

| Family | Minimum positive case | Minimum negative or fail-closed case |
|---|---|---|
| ArchaeologicalSite shape | Synthetic reviewed-site envelope with explicit non-authority and safe geometry posture. | Missing evidence/review/policy refs; exact-detail request; unsupported site claim. |
| CandidateFeature | Candidate remains candidate in API/map/AI wording. | Candidate renamed, styled, summarized, or promoted as confirmed site. |
| SiteComponent | Component remains linked part with bounded uncertainty. | Component treated as whole site or component association treated as proof. |
| Naming compatibility | `Site` routes to compatibility warning and `ArchaeologicalSite` contract. | Parallel canonical `Site` authority or schema selected silently. |
| Feature terminology | Explicit mapping to candidate or component. | Ambiguous `Feature` accepted for consequential use. |
| Geometry | Withheld/generalized synthetic carrier. | Exact, reverse-geocodable, side-channel, or reconstruction-bearing detail. |
| Evidence | Resolvable toy EvidenceRef with bounded support. | Missing, unresolved, contradictory, or scope-mismatched evidence. |
| Review and rights | Explicit synthetic review/right posture where required. | Review, consultation, consent, or cultural authority inferred from filename or role label. |
| Policy | Explicit allow/restrict/hold/deny/abstain expectation. | Missing bundle/version/obligation or unknown decision value. |
| Public carrier | Released public-safe synthetic derivative only. | Direct lifecycle read, unreleased fixture, style-only hiding, or public exact detail. |
| Correction/rollback | Prior safe state and invalidation refs. | Stale carrier remains active after withdrawal, revocation, or correction. |
| Hermeticity | Local deterministic fixture loading. | Network, geocoder, live map service, secret, production log, or governed-root write. |

### Finite vocabulary separation

Do not collapse these into one enum:

- test result: `PASS | FAIL | SKIP | ERROR`;
- policy result: `ALLOW | RESTRICT | HOLD | DENY | ABSTAIN | ERROR`;
- candidate state: intake/review/retained/rejected/promoted/quarantined/superseded;
- review disposition;
- promotion decision;
- release state;
- lifecycle state.

Adapters between vocabularies must be explicit and tested.

[Back to top](#top)

---

## Sensitivity, location, and public-surface safety

Archaeology is deny-by-default for exact site geometry, burials, sacred places, human remains, collection-security information, private-owner detail, looting-risk exposure, and unresolved cultural or sovereignty-bearing information.

Fixtures must not include:

- real coordinates or recognizable geometry;
- precise footprints, parcel clues, road-distance clues, imagery references, or location joins;
- real site identifiers, registry keys, restricted source identifiers, or collection-security references;
- sensitive cultural content, participant identity, consultation detail, or consent tokens;
- transform parameters or side-channel clues that enable reconstruction.

Public-surface tests must prove that:

1. exact/internal geometry never reaches normal clients;
2. style, zoom, opacity, filtering, or hidden fields are not treated as geoprivacy;
3. candidate status stays visible in labels, popups, legends, search, exports, and generated prose;
4. evidence, review, policy, transform/receipt, release, correction, and rollback refs are checked before exposure;
5. withheld and denied states expose safe reason codes without sensitive detail;
6. cache keys, filenames, logs, bounds, counts, labels, screenshots, graph relations, and error messages do not leak location or confirmation.

[Back to top](#top)

---

## Determinism, no-network, and side effects

Default fixture execution must be hermetic.

- no live source APIs;
- no geocoding or reverse geocoding;
- no map/tile service calls;
- no public API or AI runtime calls;
- no direct reads from RAW, WORK, QUARANTINE, PROCESSED, catalog, proof, receipt, release, or published stores;
- no writes outside test-owned temporary directories;
- no real secrets, private endpoints, production logs, or telemetry;
- stable clock, seed, ordering, identifiers, versions, and hashes;
- deterministic replay from the same fixture and configuration.

Unknown network or write behavior is `ERROR` and fails closed.

[Back to top](#top)

---

## Inventory, consumers, and vacuous-pass risk

A mature lane must maintain two-way traceability:

```text
fixture manifest -> consumer test
consumer test -> fixture manifest
```

Required inventory checks:

- every direct fixture has at least one active consumer;
- every consumer reference resolves;
- reusable fixtures are not copied into the test-local lane without justification;
- every object family has nonempty positive and fail-closed coverage;
- placeholder-only payloads do not count as semantic coverage;
- zero discovered cases is a failure, not a green result;
- skipped cases include a reason, owner, and expiry;
- no fixture path is interpreted as current release or lifecycle state.

The checked placeholder files do not satisfy nonempty semantic coverage because they contain only `status`, `source_doc`, `path`, and planning notes.

[Back to top](#top)

---

## Validation commands

No dedicated sites-fixture runner was established in the checked snapshot. The following commands are `PROPOSED` until the consumer lane exists and repository tooling is verified:

```bash
python -m pytest tests/domains/archaeology/fixtures/sites -q
python -m pytest tests/domains/archaeology/fixtures/sites -q --disable-warnings
```

A future runner must fail when:

- no cases are collected;
- only placeholder payloads are present;
- consumer backlinks are missing;
- unknown object-family or outcome values occur;
- exact/protected/reconstructable detail is detected;
- candidate/site/component boundaries collapse;
- required evidence, review, policy, receipt, release, correction, or rollback refs are absent;
- network or governed-root writes occur.

[Back to top](#top)

---

## CI and promotion boundary

Current checked maturity:

| Surface | Status |
|---|---|
| Direct sites fixture lane | README-only in bounded evidence. |
| Singular reusable site lane | README-only in bounded search. |
| Site-family schemas | Present, `PROPOSED`, empty-property, permissive. |
| Broad Archaeology validator lane | README-only in bounded evidence. |
| Dedicated sites consumer tests | Not established at checked path. |
| `make fixtures` | TODO/scaffold behavior in checked Makefile. |
| `domain-archaeology` workflow | Trigger exists; checked jobs are TODO-only scaffolding. |
| Required branch-protection significance | UNKNOWN. |

A CI success must never be treated as site confirmation, review approval, policy approval, release approval, or publication. Promotion remains a separate governed transition.

[Back to top](#top)

---

## Maintenance, migration, and rollback

When adding or changing a fixture:

1. identify the consuming test;
2. verify the correct fixture home;
3. keep the case synthetic and public-safe;
4. preserve object-family and source-role labels;
5. add both positive and fail-closed behavior where material;
6. update manifest, consumer backlink, expected outcome, and safe reason code;
7. run no-network, no-write, no-leak, candidate-not-site, evidence, review, policy, and release-boundary checks;
8. document corrections, supersession, withdrawal, revocation, and rollback impacts;
9. update this README when the lane’s actual maturity changes.

### Migration discipline

Any consolidation of plural/singular site paths, `Site`/`ArchaeologicalSite`, `Feature` mappings, or public-safe fixture homes requires:

- inventory and inbound-reference audit;
- declared source and destination authority;
- compatibility period or explicit breaking-change note;
- checksums and consumer updates;
- deprecation notice;
- rollback target;
- ADR or migration note when authority or compatibility changes materially.

[Back to top](#top)

---

## Definition of done

This lane is not mature until all applicable rows are satisfied.

- [ ] owners and CODEOWNERS are confirmed;
- [ ] lane-retention and fixture-home decisions are accepted;
- [ ] a machine-checkable manifest contract exists;
- [ ] substantive site, candidate, and component schemas exist;
- [ ] validators enforce semantics beyond permissive shape acceptance;
- [ ] reusable fixtures are non-placeholder and reviewable;
- [ ] consumer tests and two-way backlinks exist;
- [ ] positive and fail-closed families are nonempty;
- [ ] candidate-to-site and component-to-site anti-collapse tests pass;
- [ ] exact-location, side-channel, and reconstruction tests pass;
- [ ] evidence, review, policy, receipt, release, correction, and rollback closure is tested;
- [ ] no-network and no-governed-root-write controls are enforced;
- [ ] CI fails on zero cases and produces finite outcomes;
- [ ] branch-protection significance is verified;
- [ ] documentation, migration, correction, and rollback instructions are current.

Until then, this README is a routing and safety contract, not proof of implemented fixture coverage.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| ARCH-SITES-FIX-001 | Should this direct plural lane be retained? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-002 | Who owns it and which CODEOWNERS rule applies? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-003 | Should `tests/fixtures/domains/README.md` be created? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-004 | What threshold admits a test-local fixture here? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-005 | What is the canonical manifest schema? | UNKNOWN |
| ARCH-SITES-FIX-006 | What are stable fixture identity/version/hash rules? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-007 | Is `ArchaeologicalSite` the final canonical site name? | CONFLICTED / NEEDS VERIFICATION |
| ARCH-SITES-FIX-008 | What is the retirement or alias plan for `Site`? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-009 | How is `Feature` mapped to candidate versus component? | CONFLICTED |
| ARCH-SITES-FIX-010 | When will the primary site-family schemas become substantive? | UNKNOWN |
| ARCH-SITES-FIX-011 | Which validators enforce site-family semantics? | UNKNOWN |
| ARCH-SITES-FIX-012 | Are placeholder payloads retained, replaced, or removed? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-013 | Which executable tests consume these fixtures? | UNKNOWN |
| ARCH-SITES-FIX-014 | Where should the executable child lane live? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-015 | How are consumer backlinks and orphan checks enforced? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-016 | Which public-safe fixture lane is canonical for each use? | CONFLICTED |
| ARCH-SITES-FIX-017 | What is the canonical source-role vocabulary? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-018 | How is candidate-to-site promotion represented and tested? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-019 | How are cultural authority, rights, consent, and consultation represented safely? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-020 | Which exact policy bundle/version governs site exposure? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-021 | How is separation of duties enforced? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-022 | What no-leak and reconstruction suite is required? | UNKNOWN |
| ARCH-SITES-FIX-023 | How are corrections and contradictions propagated? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-024 | How are withdrawal, revocation, cache invalidation, and rollback propagated? | NEEDS VERIFICATION |
| ARCH-SITES-FIX-025 | Are coordinate-like and protected-canary scans enforced? | UNKNOWN |
| ARCH-SITES-FIX-026 | Are no-network and no-governed-root-write rules enforced? | UNKNOWN |
| ARCH-SITES-FIX-027 | Which workflows trigger for this path? | UNKNOWN |
| ARCH-SITES-FIX-028 | Is any sites suite required by branch protection? | UNKNOWN |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Directory Rules | CONFIRMED repository doctrine | Responsibility-root placement and no parallel authority. | Current implementation maturity. |
| Target v0.1 README | CONFIRMED prior content | Safety intent and stale claims to correct. | Executable coverage. |
| `tests/fixtures/README.md` | CONFIRMED | Test-local versus reusable fixture split. | Lane retention or payload validity. |
| Archaeology test-fixture parent | CONFIRMED | Parent exists and indexes `sites/`. | Child maturity. |
| Singular site fixture README | CONFIRMED | Reusable site-shaped fixture boundary. | Payload inventory or tests. |
| Synthetic site/candidate READMEs | CONFIRMED | Non-authoritative fixture posture. | Semantic payload validity. |
| Checked site/candidate JSON files | CONFIRMED placeholders | Planned path lineage. | Validity, denial, generalization, confirmation, or release. |
| ArchaeologicalSite contract/schema | CONFIRMED draft + permissive schema | Site semantics and candidate boundary. | Machine enforcement or truth. |
| CandidateFeature contract/schema | CONFIRMED draft + permissive schema | Candidate-not-site semantics. | Promotion enforcement. |
| SiteComponent contract/schema | CONFIRMED draft + permissive schema | Component semantics and Feature conflict. | Component confirmation or site truth. |
| Site compatibility contract | CONFIRMED draft | Naming/alias conflict. | Canonical migration decision. |
| Archaeology object map | CONFIRMED draft | Expected object families and unresolved mappings. | Complete implementation. |
| Two public-safe fixture READMEs | CONFIRMED | Existing compatibility lanes. | Canonical winner or payload parity. |
| Archaeology validator README | CONFIRMED | README-only maturity and intended checks. | Executable validator behavior. |
| Archaeology policy and sensitivity docs | CONFIRMED drafts | Deny-by-default and release-boundary intent. | Runtime policy enforcement. |
| Makefile and domain workflow | CONFIRMED scaffolding | Current target/workflow posture. | Substantive CI or required checks. |
| Checked 404 paths | CONFIRMED bounded checks | Named direct/consumer files absent at pinned ref. | Permanent or exhaustive absence. |

[Back to top](#top)

---

## Documentation rollback

This is a documentation-only revision.

Before merge, rollback means leaving the draft pull request unmerged or adding a transparent revert commit to the feature branch. Do not reset or force-push shared history.

After merge, rollback means a transparent revert commit or revert pull request, followed by documentation validation.

Rollback is required if this README:

- is mistaken for site, candidate, component, evidence, review, policy, release, or publication authority;
- directs executable tests into a fixture directory;
- encourages storage of real coordinates or protected archaeology detail;
- treats placeholders, filenames, schema acceptance, map styling, or generated prose as semantic proof;
- collapses candidate, component, site, short-name compatibility, or Feature vocabularies;
- silently selects a fixture home or canonical contract without migration governance;
- weakens evidence, rights, cultural, consent, sensitivity, correction, withdrawal, revocation, or rollback safeguards;
- hides permissive schemas, missing consumers, README-only validators, or TODO-only CI behavior.

**No-loss assessment:** v0.2 preserves the v0.1 synthetic-only, no-network, candidate-aware, exact-location-denied, evidence, review, policy, release, correction, withdrawal, rollback, map, API, and AI boundaries. It corrects the stale parent claim, removes misleading executable-test placement, grounds object and fixture maturity in current evidence, exposes placeholder and compatibility risks, and makes future implementation requirements inspectable.

[Back to top](#top)
