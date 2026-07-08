<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-readme
title: tools/validators README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-validator-steward-plus-domain-stewards-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: NEEDS VERIFICATION — file existed before this expansion as a two-line stub
updated: 2026-07-08
policy_label: repository-facing; validator-root-index; fail-closed; evidence-aware; policy-aware; sensitivity-aware; source-aware; domain-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: parent validator routing README under tools/validators; indexes KFM validation lanes, validator authority boundaries, fail-closed posture, responsibility-root separation, source/evidence/policy/lifecycle/release gates, domain and cross-domain validator families, public-surface denial, fixture/test routing, executable-claim verification, correction and rollback expectations, and finite outcomes while deferring domain meaning, canonical schemas, policy decisions, source registry records, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - _common/README.md
  - domains/README.md
  - source/README.md
  - source-descriptor/README.md
  - source_descriptor/README.md
  - source_role/README.md
  - sources/README.md
  - policy/README.md
  - rights/README.md
  - sensitivity/README.md
  - sensitive_geometry/README.md
  - sensitive_location_allow/README.md
  - geoprivacy/README.md
  - evidence/README.md
  - lifecycle/README.md
  - release/README.md
  - promotion_gate/README.md
  - smoke/README.md
  - joins/README.md
  - cross-domain-joins/README.md
  - cross-lane/README.md
  - taxonomy_resolver/README.md
  - suitability/README.md
  - soil-suitability/README.md
  - transport-facility-topology/README.md
  - vegetation_community/README.md
  - maplibre/README.md
  - pmtiles/README.md
  - ../../docs/domains/
  - ../../docs/sources/
  - ../../contracts/
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../data/registry/sources/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../release/
  - ../../fixtures/
  - ../../tests/
notes:
  - "This README replaces the prior two-line tools/validators parent stub. It does not confirm executable validator scripts, registry wiring, package entrypoints, generated reports, receipt emission, runtime behavior, or CI behavior."
  - "Validators are fail-closed checkers. They do not define domain meaning, create canonical schemas, admit sources, create EvidenceBundles, decide policy, approve release, publish artifacts, or authorize public API/UI/map/AI surfaces."
  - "Each validator lane should have a deterministic finite outcome, cite evidence or abstain, preserve lifecycle boundaries, preserve source roles, preserve sensitivity/rights constraints, and route unresolved cases to hold/deny/restrict/abstain/review rather than silently pass."
  - "A passing validator is not sovereign truth. It means only that the configured validation checks passed for the declared scope; evidence, policy, review, release, correction, and rollback obligations still control public use."
  - "Executable behavior, fixture coverage, registry ids, schemas, policy bundles, receipts, report destinations, runtime wiring, and CI integration remain NEEDS VERIFICATION unless separately verified in current repo evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-validator--root--index-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![authority](https://img.shields.io/badge/authority-checkers--not--truth-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/` is the parent routing surface for KFM fail-closed validators: checker lanes that test source, schema, contract, evidence, policy, lifecycle, sensitivity, rights, release, domain, cross-domain, map/tile, and public-surface readiness without becoming the authority for any of those things.

---

## Purpose

`tools/validators/` exists to organize deterministic KFM validation helpers and validator documentation.

The durable KFM question for this root is:

> Can a candidate object, source, packet, layer, join, artifact, claim, graph edge, map surface, export, Focus Mode item, AI answer, or release candidate prove enough governed support for its requested use — or must it fail closed, abstain, hold, restrict, deny, quarantine, or route to steward review?

Validators should help enforce KFM's trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A validator may check that evidence exists, policy was evaluated, release references are present, sensitivity is handled, or a public derivative is safe. It must not turn itself into evidence, policy, release authority, source authority, schema authority, public runtime, or generated truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/README.md` | **CONFIRMED README** | This file replaces the previous two-line parent stub. |
| `tools/validators/domains/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent index for per-domain validator lanes. |
| `tools/validators/policy/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Policy validator routing; not the policy authority root. |
| `tools/validators/release/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Release validator routing; not release governance or publication authority. |
| `tools/validators/source/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Source-admission and source-registry validation routing; not the source registry. |
| `tools/validators/sensitivity/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Sensitivity posture checks; not tier, policy, redaction, or release authority. |
| Executable validators, registry wiring, CLI/package entrypoints, CI jobs, report outputs, receipt emission, runtime behavior, and end-to-end enforcement | **NEEDS VERIFICATION** | This parent README is documentation and routing only. |

[Back to top](#top)

---

## Root rules

| Rule | Validator posture | Forbidden shortcut |
|---|---|---|
| Cite or abstain | Claims that depend on evidence must resolve to EvidenceRef/EvidenceBundle support or abstain. | Passing from generated text, memory, labels, UI state, or path names. |
| Fail closed | Missing, stale, contradictory, rights-limited, sensitive, unreviewed, unreleased, or unsupported inputs route to fail/hold/restrict/deny/abstain. | Silent pass, best-effort allow, or hidden warning. |
| Preserve responsibility roots | `tools/validators/` checks. It does not own schemas, contracts, policy, data, receipts, proofs, release, or public runtime. | Validator-local authority roots. |
| Preserve lifecycle boundaries | Validators must not let RAW, WORK, QUARANTINE, unpublished candidates, or internal stores leak to public clients. | Direct public reads from internal/canonical/lifecycle stores. |
| Preserve source roles | Observed, modeled, aggregate, candidate, administrative, synthetic, regulatory, and contextual roles remain distinct. | Role upgrade by publication, map rendering, AI summary, or derived artifact. |
| Preserve sensitivity and rights | Most-restrictive posture wins across joins, derivatives, tiles, maps, graphs, exports, embeddings, Focus Mode, and AI answers. | T0/default-public assumptions, style-as-policy, client-side hiding, or undocumented redaction. |
| Release is governed | Release validation checks readiness; release records and promotion decisions live under release/governance homes. | Treating validator success as publication approval. |
| Public surfaces are downstream | MapLibre, PMTiles, API, UI, graph, search, export, screenshots, Focus Mode, and AI surfaces consume released public-safe derivatives. | Public runtime reads internal truth stores or model output directly. |
| Corrections and rollback stay visible | Validators check correction paths, supersession, withdrawal, rollback targets, and cascade effects. | In-place mutation without audit trail or rollback target. |

[Back to top](#top)

---

## Validator family map

The folders below are routing lanes, indexes, or validator-local documentation. A README being present is not proof of executable behavior.

### Trust, governance, and release gates

| Lane | Use | Authority boundary |
|---|---|---|
| [`policy/`](policy/README.md) | Policy input, policy decision, finite outcome, obligation, reason-code, and public-surface readiness checks. | Policy rules and decisions remain in `policy/` and accepted decision homes. |
| [`rights/`](rights/README.md) | Source rights, license, access terms, consent, attribution, stewardship, and reuse posture checks. | Rights authority and policy decisions remain outside validators. |
| [`sensitivity/`](sensitivity/README.md) | Sensitivity tier posture, most-restrictive propagation, public-safe transform, review, release, and public-surface checks. | Sensitivity policy, redaction parameters, and tier authority remain in policy/governance homes. |
| [`sensitive_geometry/`](sensitive_geometry/README.md) | Exact-location denial, public-safe geometry, reconstruction risk, redaction/aggregation receipt checks. | Does not store sensitive geometry or define hidden thresholds. |
| [`sensitive_location_allow/`](sensitive_location_allow/README.md) | Allow-exception packet checks after deny-by-default sensitive-location posture. | Does not make policy decisions or publish sensitive locations. |
| [`evidence/`](evidence/README.md) | EvidenceRef/EvidenceBundle/proof closure and citation checks. | Evidence/proof authority remains in `data/proofs/` and accepted evidence homes. |
| [`lifecycle/`](lifecycle/README.md) | Lifecycle boundary, transition, quarantine, promotion, correction, and rollback checks. | Does not move files or decide promotion. |
| [`promotion_gate/`](promotion_gate/README.md) | Promotion gate checks at governed publication transitions. | Promotion decisions remain governed records, not validator output alone. |
| [`release/`](release/README.md) | ReleaseManifest, PromotionDecision, rollback/correction/withdrawal, artifact-integrity, and public-surface readiness checks. | Release records and publication authority remain in `release/`. |
| [`smoke/`](smoke/README.md) | Fast import/CLI/registry/fixture/side-effect health checks. | Smoke pass is not correctness, policy, evidence, or release proof. |

### Source, taxonomy, and identity helpers

| Lane | Use | Authority boundary |
|---|---|---|
| [`source/`](source/README.md) | Broad source admission, SourceDescriptor posture, source registry linkage, source-role/rights/sensitivity/cadence/citation checks. | Source registry authority remains in `data/registry/sources/`. |
| [`source-descriptor/`](source-descriptor/README.md) | Hyphenated SourceDescriptor validator lane and naming-drift tracking. | Must not diverge from underscore SourceDescriptor route without ADR/migration. |
| [`source_descriptor/`](source_descriptor/README.md) | Underscore SourceDescriptor canonical-candidate / compatibility lane. | One implementation entrypoint and one registry id should be preferred. |
| [`source_role/`](source_role/README.md) | Source-role presence, authority rank, admissibility, anti-collapse, and claim-role compatibility checks. | Source-role vocabulary and enum authority remain in schemas/docs/ADRs. |
| [`sources/`](sources/README.md) | Plural compatibility/index lane for older or proposed source-validator paths. | Must not create duplicate source validator authority. |
| [`taxonomy_resolver/`](taxonomy_resolver/README.md) | Controlled vocabulary, class id, alias, hierarchy, crosswalk, deprecation, and provenance checks. | Canonical taxonomy records and vocabularies remain in accepted registry/taxonomy homes. |

### Domain and cross-domain routing

| Lane | Use | Authority boundary |
|---|---|---|
| [`domains/`](domains/README.md) | Parent index for per-domain validator lanes. | Domain meaning remains in `docs/domains/` and `contracts/domains/`. |
| [`joins/`](joins/README.md) | Shared join-validator routing. | Join validators do not absorb domain authority. |
| [`cross-domain-joins/`](cross-domain-joins/README.md) | Cross-domain join posture, evidence, policy, and anti-collapse checks. | Cross-domain artifacts remain downstream from domain truth. |
| [`cross-lane/`](cross-lane/README.md) | Cross-lane routing and trust-boundary checks. | Does not create a parallel domain or governance root. |
| [`suitability/`](suitability/README.md) | Broad modeled/derived suitability validation. | Suitability is not domain truth, model authority, or field advice. |
| [`soil-suitability/`](soil-suitability/README.md) | SoilCropSuitability and Agriculture×Soil suitability derivative checks. | Soil truth and Agriculture derivative authority remain separate. |
| [`transport-facility-topology/`](transport-facility-topology/README.md) | Transport facility topology, NetworkNode/NetworkEdge link, graph-projection, and public-surface checks. | Not facility truth, graph truth, live routing, legal access, or infrastructure authority. |
| [`vegetation_community/`](vegetation_community/README.md) | Flora VegetationCommunity classification, taxonomy/crosswalk, Habitat anti-collapse, sensitivity, and release checks. | Not Flora truth, Habitat truth, occurrence proof, or taxonomy authority. |

### Geometry, map, tile, and artifact surfaces

| Lane | Use | Authority boundary |
|---|---|---|
| [`geometry/`](geometry/README.md) | Shared geometry carrier validation, geometry role, topology, and public-safe posture. | Geometry does not authorize sensitive exposure. |
| [`geoprivacy/`](geoprivacy/README.md) | Geoprivacy posture, redaction/generalization, most-restrictive handling, and public-surface limits. | Does not define hidden policy values or publish coordinates. |
| [`geoprivacy_transform/`](geoprivacy_transform/README.md) | Transform-check routing for geoprivacy operations and receipts. | Transform output still needs policy/review/release closure. |
| [`maplibre/`](maplibre/README.md) | Map renderer boundary, released artifact eligibility, descriptor/readiness checks. | MapLibre is a downstream renderer, not truth or release authority. |
| [`pmtiles/`](pmtiles/README.md) | PMTiles integrity, attestation, index/signature/receipt readiness checks. | Tile presence is not evidence, policy, or release approval. |
| [`citation/`](citation/README.md) | Citation/attribution posture and cite-or-abstain support. | Citation formatting is not evidence closure by itself. |
| [`catalog/`](catalog/README.md) and [`catalog_closure/`](catalog_closure/README.md) | Catalog readiness and closure checks. | Catalog records remain governed data objects, not validator-owned truth. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Validator routing and checker code | `tools/validators/` |
| Shared validator helpers | `tools/validators/_common/` and accepted helper packages |
| Domain doctrine | `docs/domains/` |
| Source doctrine | `docs/sources/` |
| Semantic meaning | `contracts/` |
| Machine shape | `schemas/contracts/v1/` and accepted schema homes |
| Policy rules and decisions | `policy/` and accepted policy/decision homes |
| Source registry records | `data/registry/sources/` |
| Evidence/proofs | `data/proofs/` and accepted evidence homes |
| Receipts | `data/receipts/` and accepted receipt homes |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records, promotion decisions, rollback, correction, withdrawal | `release/` and accepted release/correction homes |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists as the parent validator index.
- **PROPOSED:** new validator lanes may live under `tools/validators/` when they are checkers that preserve responsibility-root boundaries and have clear references to contracts, schemas, policy, evidence, fixtures, tests, release, correction, and rollback.
- **NEEDS VERIFICATION:** exact executable files, registry ids, entrypoints, schema bindings, fixture files, test coverage, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this tree as a source registry, policy root, schema root, contract root, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/` include:

- README indexes and validator-lane documentation;
- small deterministic validator scripts that check declared contracts/schemas/policy/evidence/release readiness;
- registry notes for validator ids, entrypoints, finite outcomes, and dependency boundaries;
- side-effect-safe smoke checks;
- adapters that produce validation reports to accepted report/artifact homes;
- routing shims that preserve migration compatibility without creating duplicate authority;
- documentation that points maintainers to the owning roots for schemas, policy, evidence, receipts, release, fixtures, and tests.

[Back to top](#top)

---

## What does not belong here

| Do not put in this tree | Correct home |
|---|---|
| Canonical schemas, enums, DTOs, OpenAPI contracts | `schemas/` and accepted API/schema homes |
| Semantic object contracts | `contracts/` |
| Policy rules, allowlists, denylists, tier tables, release decisions | `policy/`, `release/`, accepted governance homes |
| Source descriptors and source registry records | `data/registry/sources/` and accepted source registry homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | governed `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, signed attestations | `data/proofs/`, `data/receipts/`, accepted trust-artifact homes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` and accepted release/correction homes |
| Fixtures and test suites | `fixtures/` and `tests/` unless an accepted local convention says otherwise |
| Public API/UI/map/tile/graph/search/export/Focus Mode/AI runtime code | governed application/runtime roots |
| Secrets, credentials, private source data, exact sensitive locations, restricted infrastructure fields, hidden thresholds, signing keys, reconstruction hints | denied here |

[Back to top](#top)

---

## Standard validator outcomes

Validator lanes may define narrower outcome vocabularies, but parent-level outcomes should remain finite and inspectable.

| Outcome | Meaning |
|---|---|
| `VALIDATOR_PASS` | Candidate passed configured checks for the declared scope. |
| `VALIDATOR_FAIL` | Candidate failed one or more configured checks. |
| `VALIDATOR_DENY` | Candidate must not proceed for the requested use. |
| `VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `VALIDATOR_HOLD` | Candidate must remain held pending evidence, source, rights, sensitivity, policy, review, release, correction, or rollback closure. |
| `VALIDATOR_ABSTAIN` | Candidate lacks enough support for a claim or decision. |
| `VALIDATOR_ROUTE` | Candidate should be routed to a narrower validator lane. |
| `VALIDATOR_NEEDS_REVIEW` | Steward review is required before use. |
| `VALIDATOR_PUBLIC_SURFACE_DENIED` | Candidate is not eligible for public API/UI/map/tile/export/search/graph/Focus Mode/AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, timeout, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain modular and reversible:

```text
tools/validators/
├── README.md
├── _common/                         # shared validator utilities, if verified
├── domains/                         # per-domain validator lanes
├── policy/                          # policy-facing validation routing
├── source/                          # source-admission validation routing
├── sensitivity/                     # sensitivity posture validation routing
├── evidence/                         # evidence/proof reference validation routing
├── lifecycle/                        # lifecycle transition validation routing
├── release/                          # release-readiness validation routing
├── smoke/                            # shallow health checks
└── <specialized-lane>/               # narrow validator routes with clear authority boundaries
```

Do not add executable validators, local schemas, local policy bundles, local source registries, local evidence stores, local release records, or local fixture/test trees unless the placement decision is documented and tests prove fail-closed behavior without granting validator-authority over the governed roots.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the previous two-line parent stub.
- [x] It describes `tools/validators/` as fail-closed checker routing, not truth or publication authority.
- [x] It preserves the responsibility split between validators, docs, contracts, schemas, policy, data, proofs, receipts, release, fixtures, tests, and public runtime.
- [x] It indexes trust/governance gates, source/taxonomy lanes, domain/cross-domain lanes, and map/tile/artifact/public-surface validators.
- [x] It marks executable behavior, registry wiring, schemas, fixtures, tests, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.
- [x] It includes finite parent-level outcomes and denies validator overclaim.

Future implementation is not complete until:

- [ ] Validator registry or CLI references are searched and classified.
- [ ] Validator ids, entrypoints, dependencies, and report destinations are documented.
- [ ] Schema bindings, policy bundle references, evidence/proof refs, receipt families, and release refs are verified per lane.
- [ ] Fixture files are synthetic/minimized/public-safe unless explicitly governed otherwise.
- [ ] Tests cover pass, fail, deny, restrict, hold, abstain, route, review-required, public-surface-denied, and system-error cases.
- [ ] CI invokes validators in deterministic order and records artifacts in accepted locations.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, artifact, or CI homes.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Expanded parent validators README from two-line stub into governed validator-root index. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
