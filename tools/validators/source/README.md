<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-source-readme
title: tools/validators/source README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-source-steward-plus-validator-steward-plus-registry-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; source-validator-index; source-admission; source-registry-aware; source-descriptor-aware; source-role-anti-collapse; rights-aware; sensitivity-aware; cadence-aware; citation-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: parent source validator routing README under tools/validators; indexes source-admission and source-registry validation concerns including SourceDescriptor shape and contract pairing, source role preservation, source type and authority rank, rights and sensitivity admission posture, cadence and stale-state checks, access and citation guidance, source-head/content identity, registry linkage, fixture routing, source-registry package reachability, evidence/proof/receipt linkage, policy/review/release posture, correction and supersession propagation, lifecycle boundary checks, public-surface denial, and finite outcomes while deferring SourceDescriptor meaning, canonical schemas, policy decisions, source registry records, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../source-descriptor/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../policy/README.md
  - ../evidence/README.md
  - ../lifecycle/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/sources/CITATION_GUIDANCE.md
  - ../../../docs/sources/RIGHTS_GUIDANCE.md
  - ../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../contracts/source/README.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../packages/source-registry/README.md
  - ../../../packages/source-registry/src/source_registry/README.md
  - ../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../policy/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../policy/release/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/source/README.md. It does not confirm executable source validators, registry wiring, schema bindings, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "This is the broad source validator parent route. The narrower SourceDescriptor validator route is tools/validators/source-descriptor/."
  - "Source registry helpers may load and normalize source-descriptor and source-authority references, but must not become source truth, policy authority, schema authority, catalog authority, evidence authority, or release authority."
  - "data/registry/sources/ is the source-admission and authority-control surface for admitted sources; validators check it but do not own or write source registry records as authority."
  - "Source role, rights, sensitivity, cadence, access posture, and citation guidance are fixed by governed admission records and must not be upgraded downstream by promotion, generation, map rendering, publication, or AI summary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/source

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-source--validator--index-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![authority](https://img.shields.io/badge/authority-validator--not--registry-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/source/` is the parent source validator routing index for checking source admission, SourceDescriptor posture, source registry linkage, source-role anti-collapse, rights/sensitivity/cadence/citation readiness, evidence/policy/release support, correction/supersession propagation, and public-surface denial without becoming source registry, schema, policy, evidence, or release authority.

---

## Purpose

`tools/validators/source/` exists to organize source-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a source candidate, SourceDescriptor, source registry reference, source authority reference, fixture, connector preflight output, catalog-bound source reference, evidence-bound source reference, release candidate, public artifact, map surface, graph edge, export, screenshot, embedding, Focus Mode surface, or AI answer carry resolved source identity, source role, rights, sensitivity, cadence, access, citation, registry linkage, policy/review posture, evidence/proof/receipt support, release state, correction path, rollback target, and public-surface limits for its intended use?

The answer should be a deterministic validation result or routing decision. This folder should not define source meaning, store source registry records, write source descriptors as authority, define schemas, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, expose public API/map/AI payloads, or turn source metadata into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/source/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/source-descriptor/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Narrow SourceDescriptor validator routing lane; documents hyphen/underscore naming drift. |
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines SourceDescriptor fields, source role, rights, sensitivity, intake posture, citation guidance, and anti-collapse rule. |
| `contracts/source/source_descriptor.md` | **CONFIRMED contract / schema-paired draft** | Defines SourceDescriptor as governed source-admission and authority-control descriptor; not source truth, release approval, or policy bypass. |
| `schemas/contracts/v1/source/README.md` | **CONFIRMED schema-family README / mixed maturity** | Source schemas define object shape only and do not store registry records, lifecycle data, validators, or release records. |
| `data/registry/sources/README.md` | **CONFIRMED registry README / implementation maturity mixed** | Source registry is admission and authority-control surface, not bibliography; exact files remain mixed/proposed. |
| `packages/source-registry/README.md` | **CONFIRMED package README / implementation NEEDS VERIFICATION** | Shared helper package may load/normalize source descriptors and authority references without becoming authority. |
| `fixtures/contracts/v1/source/source_descriptor/README.md` | **CONFIRMED fixture README / behavior NEEDS VERIFICATION** | Fixture family covers one valid and one invalid SourceDescriptor example; fixtures are not source registry records or authority. |
| Executable source validator scripts, registry wiring, schema bindings, policy bundles, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Broad source validator routing | `tools/validators/source/` | Parent source validation index. |
| SourceDescriptor-specific validation | `tools/validators/source-descriptor/` | Checks SourceDescriptor packets and naming drift. |
| Source registry helper package | `packages/source-registry/` | Shared loading/normalization helpers; not authority. |
| Source registry records | `data/registry/sources/` | Admission and authority-control records; validators check refs, not own records. |
| Source doctrine | `docs/sources/` | Human-facing standards and admission guidance. |
| Source semantic contracts | `contracts/source/` | Meaning of source objects. |
| Source machine shape | `schemas/contracts/v1/source/` and accepted schema homes | Machine shape only. |
| Source rights and sensitivity checks | `tools/validators/rights/`, `tools/validators/sensitivity/` | Specialized cross-cutting validators. |
| Policy and release checks | `tools/validators/policy/`, `tools/validators/release/`, `tools/validators/promotion_gate/` | Validators report gaps; they do not decide policy/release. |
| Source fixtures and tests | `fixtures/contracts/v1/source/`, `fixtures/`, `tests/` | Fixtures prove examples only when tests verify them. |

[Back to top](#top)

---

## Source validation packet

A source candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Source identity | Stable source id, descriptor ref, descriptor version, source title, source type, source family, publisher, owner/steward, and source authority reference where used. | Truth of source claims. |
| Source role | Source role, authority rank, allowed/prohibited claim roles, and anti-collapse posture. | Upgrade from candidate/modeled/contextual to observed/primary truth. |
| Rights posture | License, access terms, attribution, redistribution, commercial use, AI use, rights verification, expiration, and obligations. | Release approval. |
| Sensitivity posture | Sensitivity default, required review, redaction/generalization requirements, geoprivacy posture, and downstream most-restrictive propagation. | Sensitivity downgrade. |
| Cadence/freshness | Update cadence, source-head identity, retrieval time, observed/valid time, staleness policy, source retirement, supersession, and refresh posture. | Current-truth guarantee. |
| Access posture | Access method, endpoint/format posture, auth requirements, rate limits, source restrictions, and no-secret/no-public-bypass posture. | Permission to fetch or publish. |
| Citation posture | Citation template, attribution requirements, link-back/disclaimer obligations, and downstream citation propagation. | Evidence closure. |
| Registry linkage | Registry home, source descriptor location, source activation/authority reference when used, descriptor lineage, supersession, and correction posture. | Validator-owned registry authority. |
| Evidence/policy/release support | EvidenceRef, validation report, policy decision, reason codes, obligations, release reference, correction path, rollback target, and receipts where required. | Public-surface authorization. |
| Consumer envelope | Connector, watcher, pipeline, catalog, proof, release, map, API, graph, export, embedding, Focus Mode, and AI surfaces are constrained to the admitted source posture. | Unbounded reuse. |

[Back to top](#top)

---

## Source invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Admission precedes use | Source posture is admitted or explicitly held/quarantined/denied before source material shapes downstream claims. | Source material enters RAW, catalog, proof, release, or public surface without resolvable source posture. |
| Source role is fixed at admission | Source role cannot be upgraded by promotion, derivation, UI display, map rendering, or AI generation. | Candidate becomes verified, modeled becomes observed, aggregate becomes per-place truth, context becomes primary evidence. |
| Rights and sensitivity fail closed | Unknown rights, unresolved sensitivity, access limits, or obligations block public use. | Public release proceeds from incomplete rights/sensitivity support. |
| Source metadata is not truth | SourceDescriptor and registry records describe how KFM may treat source material. | Descriptor or registry record is treated as evidence that source claims are true. |
| Registry stays separate | Registry records live in accepted source registry homes. | Validator folder stores or mutates registry records as authority. |
| Packages do not become authority | Source-registry helper packages load and normalize references only. | Package output overrides policy, evidence, schema, registry, or release authority. |
| Corrections are traceable | Rights changes, sensitivity changes, source-head drift, cadence expiration, supersession, retirement, and correction produce traceable transitions. | Source posture changes in place without version/correction/supersession support. |
| Downstream carriers stay subordinate | Catalog, triplets, tiles, maps, exports, graphs, screenshots, embeddings, Focus Mode, and AI answers cite source posture without upgrading it. | Downstream carrier becomes source authority. |

[Back to top](#top)

---

## Fail-closed conditions

A source candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- source id, descriptor ref, descriptor version, source type, source role, authority rank, publisher/steward, rights, sensitivity, cadence, access, citation, registry linkage, review state, release state, or lifecycle posture is missing or malformed;
- source role is unknown, contradicted, unsupported, inferred by AI, upgraded downstream, or collapsed across source families;
- rights, terms, attribution, redistribution, AI use, access limits, owner/steward posture, consent, or sovereignty/cultural/community authority is unknown, contested, expired, incompatible, or unverified;
- sensitivity default, redaction/generalization requirement, exact-location posture, living-person/DNA/genomic/private parcel/cultural/archaeology/rare-species/infrastructure risk, or review obligation is unresolved;
- cadence, source-head/content identity, retrieval/valid time, stale-state, retirement, supersession, or correction posture is missing where required;
- citation guidance is absent, impossible to satisfy, or dropped by a downstream surface;
- source registry linkage, source activation decision, source authority reference, or descriptor lineage is missing where required;
- policy decision, EvidenceRef, ValidationReport, receipt, ReleaseManifest, correction path, or rollback target is required but absent;
- source metadata is treated as claim truth, public release permission, evidence closure, policy approval, or AI/public-surface authority.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad source validator routing | `tools/validators/source/` |
| SourceDescriptor validator routing | `tools/validators/source-descriptor/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Source-registry helper package | `packages/source-registry/` |
| Source doctrine and admission guidance | `docs/sources/` |
| Source semantic contracts | `contracts/source/` |
| Source schemas | `schemas/contracts/v1/source/` and accepted source schema homes |
| Source registry records | `data/registry/sources/` and accepted source registry homes |
| Source rights/sensitivity/release policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists at `tools/validators/source/README.md`.
- **PROPOSED:** validator code may live here when it checks declared source-admission and source-registry invariants and delegates meaning, schemas, registry records, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** executable files, registry entries, source validator versus `source-descriptor` path roles, source activation register maturity, source schema drift, fixture paths, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as source registry, source data store, source admission authority, legal authority, policy rule authority, canonical schema home, semantic contract home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/source/` include:

- this README;
- parent routing notes for source-facing validators;
- small validation adapters that check source admission packets, registry linkage, descriptor linkage, source role, source authority, source freshness, and source anti-collapse posture;
- checks that source registry helper package outputs do not become authority;
- checks that unknown rights, sensitivity, role, cadence, access, citation, registry, review, release, evidence, or policy support fails closed;
- checks that downstream consumers preserve source role, rights, sensitivity, citation, and release limits;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of registry, policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Source registry records, activation decisions, source authority registers, source payloads | `data/registry/sources/`, accepted control-plane/source registry homes, governed lifecycle roots |
| SourceDescriptor semantic contracts | `contracts/source/` |
| SourceDescriptor JSON Schemas, enums, DTOs, or machine shape | `schemas/contracts/v1/source/` or accepted schema homes |
| Policy rules, rights decisions, sensitivity decisions, release decisions, steward approvals | `policy/`, `release/`, accepted governance homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOURCE_VALIDATOR_PASS` | Candidate passed configured source checks. |
| `SOURCE_VALIDATOR_FAIL` | Candidate failed one or more configured source checks. |
| `SOURCE_VALIDATOR_DENY` | Candidate must not proceed because source role, rights, sensitivity, access, registry, evidence, policy, release, correction, rollback, or public-surface support cannot be resolved. |
| `SOURCE_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SOURCE_VALIDATOR_HOLD` | Candidate must remain held pending source, rights, sensitivity, citation, review, registry, or policy closure. |
| `SOURCE_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a source assertion. |
| `SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor reference is absent or unresolved. |
| `SOURCE_REGISTRY_LINK_MISSING` | Required source registry or source authority reference is absent. |
| `SOURCE_ID_MISSING` | Required source id is absent or malformed. |
| `SOURCE_ROLE_MISSING` | Required source role is absent or unsupported. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Source role is upgraded or collapsed downstream. |
| `SOURCE_RIGHTS_UNRESOLVED` | Rights, license, terms, attribution, redistribution, AI use, or access posture is unresolved. |
| `SOURCE_SENSITIVITY_UNRESOLVED` | Sensitivity default, review, redaction, consent, geoprivacy, or restricted-use posture is unresolved. |
| `SOURCE_CADENCE_STALE` | Cadence, source-head, retrieval time, valid time, or stale-state posture is missing or stale. |
| `SOURCE_CITATION_MISSING` | Required citation or attribution guidance is absent. |
| `SOURCE_REGISTRY_HELPER_OVERCLAIM` | Source-registry helper output is treated as policy, evidence, registry, release, or truth authority. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights review, sensitivity review, or reason-code support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `SOURCE_METADATA_OVERCLAIM` | Source metadata is treated as claim truth, evidence closure, policy approval, release approval, or public permission. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose source-limited or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/source/
├── README.md
├── validate_source_packet.py            # PROPOSED; not confirmed
├── validate_source_registry_link.py     # PROPOSED; not confirmed
├── validate_source_role.py              # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Keep `tools/validators/source/` as the parent source validator route. Keep `tools/validators/source-descriptor/` as the SourceDescriptor-specific route unless an ADR or migration note chooses a different spelling and merges the responsibilities.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/source/README.md`.
- [x] It distinguishes this broad source parent route from the narrower `tools/validators/source-descriptor/` route.
- [x] It marks this path as source validator routing, not source registry, source admission authority, schema authority, policy authority, evidence authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves source-role anti-collapse, rights/sensitivity/cadence/citation admission posture, registry linkage, source-registry helper boundaries, correction/supersession posture, and fail-closed handling.
- [x] It routes source meaning to `contracts/`, machine shape to `schemas/`, registry records to `data/registry/sources/`, helper code to `packages/source-registry/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, source activation register maturity, schema drift, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to source validators are searched and classified.
- [ ] Boundary between broad `source/` validators and `source-descriptor/` validators is confirmed by ADR, migration note, or accepted convention.
- [ ] Source registry and source activation register homes are verified.
- [ ] SourceDescriptor schema path drift and fixture-root drift are resolved or documented.
- [ ] Fixture files are added or verified only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, descriptor-missing, registry-missing, role-collapse, rights-unresolved, sensitivity-unresolved, stale-cadence, missing-citation, release-missing, helper-overclaim, and public-surface-blocked cases.
- [ ] CI invokes source validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with broad source validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
