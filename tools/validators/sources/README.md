<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-sources-readme
title: tools/validators/sources README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-source-steward-plus-validator-steward-plus-registry-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; sources-validator-index; plural-path; compatibility-lane; source-admission; source-registry-aware; source-descriptor-aware; source-role-anti-collapse; rights-aware; sensitivity-aware; cadence-aware; citation-aware; fail-closed; release-gated; non-authoritative; naming-drift-aware
owning_root: tools/
responsibility: plural sources validator routing README under tools/validators; documents compatibility and migration posture for older/proposed references to tools/validators/sources/ while indexing the singular tools/validators/source/ parent, SourceDescriptor-specific lanes, source-role validation, source registry admission checks, source descriptor fixtures, source-registry helper package, source role/rights/sensitivity/cadence/citation posture, source-head and registry linkage, policy/evidence/release references, correction and supersession propagation, public-surface denial, fixture/test routing, and finite outcomes while deferring SourceDescriptor meaning, source-role vocabulary authority, canonical schemas, policy decisions, source registry records, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../source/README.md
  - ../source-descriptor/README.md
  - ../source_descriptor/README.md
  - ../source_role/README.md
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
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/README.md
  - ../../../packages/source-registry/README.md
  - ../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../tests/sources/
  - ../../../tests/fixtures/sources/source_descriptor/
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
  - "This README replaces an empty placeholder at tools/validators/sources/README.md. It does not confirm executable sources validators, registry wiring, schema bindings, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "data/registry/sources/README.md names a proposed validator at tools/validators/sources/validate_source_descriptor.py. That proposed executable was not verified during this edit."
  - "tools/validators/source/ is the confirmed broad source validator parent README; tools/validators/source_descriptor/ and tools/validators/source-descriptor/ are SourceDescriptor-specific lanes. This plural path must not become a competing validator authority."
  - "Use one implementation entrypoint and one registry id for any SourceDescriptor/source-admission validator. If plural sources/ remains, treat it as compatibility routing or an index unless an ADR/migration note chooses it as canonical."
  - "Source role, rights, sensitivity, cadence, access posture, and citation guidance are fixed by governed source admission and must not be upgraded downstream by promotion, generation, map rendering, publication, or AI summary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/sources

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-sources--validator--index-informational)
![path](https://img.shields.io/badge/path-plural--compatibility-blueviolet)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/sources/` is the plural source-validator compatibility/index lane for older or proposed references to `sources/`; it should route to the accepted source-admission validators without creating a second source registry, SourceDescriptor, schema, policy, evidence, or release authority.

---

## Purpose

`tools/validators/sources/` exists to make plural-path source validation explicit and safe.

The durable KFM question for this lane is:

> When a workflow or older document references `tools/validators/sources/`, does it resolve to the accepted source-admission validator path, preserve SourceDescriptor posture, source role, source registry linkage, rights, sensitivity, cadence, access, citation, source-head identity, evidence/policy/release support, correction/supersession posture, and public-surface denial without creating competing validator behavior?

The answer should be a deterministic validation result or routing decision. This folder should not define source meaning, store source registry records, write source descriptors as authority, define schemas, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, expose public API/map/AI payloads, or turn source metadata into truth.

[Back to top](#top)

---

## Naming and compatibility posture

KFM currently has several source-validator path shapes in play:

```text
tools/validators/source/             # confirmed broad source validator parent README
tools/validators/source_descriptor/  # SourceDescriptor underscore path named by the Source Descriptor Standard
tools/validators/source-descriptor/  # hyphenated SourceDescriptor routing lane
tools/validators/source_role/        # source-role anti-collapse validator lane
tools/validators/sources/            # plural compatibility/index lane documented here
```

Use this posture until an accepted ADR or migration note resolves executable paths:

- Treat `tools/validators/source/` as the broad source validator parent index.
- Treat `tools/validators/source_descriptor/` and `tools/validators/source-descriptor/` as SourceDescriptor-specific lanes that must not diverge into competing implementations.
- Treat `tools/validators/source_role/` as the source-role anti-collapse lane.
- Treat `tools/validators/sources/` as a plural compatibility/index path because older/proposed registry docs named a validator under this plural folder.
- Prefer one implementation entrypoint and one registry id for any real SourceDescriptor/source-admission validator.
- Record any migration as a reversible change with tests and references updated in `docs/`, `schemas/`, `fixtures/`, `tests/`, and validator registry metadata.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/sources/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/source/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Broad source validator parent route. |
| `tools/validators/source_descriptor/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | SourceDescriptor underscore canonical-candidate / compatibility path. |
| `tools/validators/source-descriptor/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | SourceDescriptor hyphenated routing lane. |
| `tools/validators/source_role/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Source-role anti-collapse route. |
| `data/registry/sources/README.md` | **CONFIRMED registry README / implementation maturity mixed** | Documents source registry as admission and authority-control surface and names `tools/validators/sources/validate_source_descriptor.py` as a proposed validator filename. |
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines SourceDescriptor field surface, source role, rights, sensitivity, intake posture, citation guidance, and anti-collapse rule. |
| Executable plural `sources/` validator scripts, registry wiring, schema bindings, policy bundles, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Plural-path validation packet

A plural-path source validation candidate should expose enough explicit context for deterministic routing and validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Path resolution | Requested validator path, implementation path, registry id, CLI entrypoint, and compatibility alias are explicit. | Silent creation of a second validator authority. |
| Source identity | Stable source id, descriptor ref, descriptor version, source title, source type, source family, publisher, owner/steward, and source authority reference where used. | Truth of source claims. |
| Source role | Source role, authority rank, allowed/prohibited claim roles, and anti-collapse posture. | Upgrade from candidate/modeled/contextual to observed/primary truth. |
| Rights posture | License, access terms, attribution, redistribution, commercial use, AI use, rights verification, expiration, and obligations. | Release approval. |
| Sensitivity posture | Sensitivity default, required review, redaction/generalization requirements, geoprivacy posture, and downstream most-restrictive propagation. | Sensitivity downgrade. |
| Cadence/freshness | Update cadence, source-head identity, retrieval time, observed/valid time, staleness policy, source retirement, supersession, and refresh posture. | Current-truth guarantee. |
| Access/citation posture | Access method, endpoint/format posture, auth requirements, citation template, attribution requirements, disclaimer/link-back obligations, and downstream propagation. | Permission to fetch, cite, or publish by itself. |
| Registry linkage | Registry home, source descriptor location, source activation/authority reference where used, descriptor lineage, supersession, and correction posture. | Validator-owned registry authority. |
| Evidence/policy/release support | EvidenceRef, validation report, policy decision, reason codes, obligations, release reference, correction path, rollback target, and receipts where required. | Public-surface authorization. |
| Consumer envelope | Connector, watcher, pipeline, catalog, proof, release, map, API, graph, export, embedding, Focus Mode, and AI surfaces preserve admitted source posture. | Unbounded reuse. |

[Back to top](#top)

---

## Invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| One source validator authority | Plural, singular, underscore, and hyphen paths do not diverge into conflicting executable behavior. | Two paths define separate behavior, registry ids, or outcome vocabularies without ADR. |
| Admission precedes use | Source posture is admitted or explicitly held/quarantined/denied before source material shapes downstream claims. | Source material enters RAW, catalog, proof, release, or public surface without resolvable source posture. |
| Source role is fixed at admission | Source role cannot be upgraded by promotion, derivation, UI display, map rendering, or AI generation. | Candidate becomes verified, modeled becomes observed, aggregate becomes per-place truth, context becomes primary evidence. |
| Rights and sensitivity fail closed | Unknown rights, unresolved sensitivity, access limits, or obligations block public use. | Public release proceeds from incomplete rights/sensitivity support. |
| Source metadata is not truth | SourceDescriptor and registry records describe how KFM may treat source material. | Descriptor or registry record is treated as evidence that source claims are true. |
| Registry stays separate | Registry records live in accepted source registry homes. | Validator folder stores or mutates registry records as authority. |
| Corrections are traceable | Rights changes, sensitivity changes, source-head drift, cadence expiration, supersession, retirement, and correction produce traceable transitions. | Source posture changes in place without version/correction/supersession support. |
| Downstream carriers stay subordinate | Catalog, triplets, tiles, maps, exports, graphs, screenshots, embeddings, Focus Mode, and AI answers cite source posture without upgrading it. | Downstream carrier becomes source authority. |

[Back to top](#top)

---

## Fail-closed conditions

A plural-path source validator candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- plural `sources/` path and singular/SourceDescriptor path disagree about implementation entrypoint, registry id, schema path, fixture path, outcome vocabulary, or report destination;
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
| Plural compatibility/index routing | `tools/validators/sources/` |
| Broad source validator routing | `tools/validators/source/` |
| SourceDescriptor validator routing | `tools/validators/source_descriptor/`, `tools/validators/source-descriptor/` |
| Source-role validation | `tools/validators/source_role/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Source-registry helper package | `packages/source-registry/` |
| Source doctrine and admission guidance | `docs/sources/` |
| Source semantic contracts | `contracts/source/` |
| Source schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/sources/` if accepted, and accepted schema homes |
| Source registry records | `data/registry/sources/` and accepted source registry homes |
| Source rights/sensitivity/release policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/`, `tests/fixtures/`, and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists at `tools/validators/sources/README.md`.
- **PROPOSED:** compatibility/shim validator code may live here only if it routes to the accepted source validation implementation and does not define divergent behavior.
- **NEEDS VERIFICATION:** executable files, registry entries, plural/singular path choice, SourceDescriptor schema drift, source activation register maturity, fixture paths, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as source registry, source data store, source admission authority, legal authority, policy rule authority, canonical schema home, semantic contract home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/sources/` include:

- this README;
- compatibility notes for plural `sources/` references;
- a shim that routes to the accepted source validation entrypoint, if accepted and tested;
- checks that older references to `tools/validators/sources/validate_source_descriptor.py` do not silently drift from the accepted source validator;
- routing notes for source, SourceDescriptor, and source-role validators;
- finite outcome vocabulary and reason-code mapping shared with the chosen source validator path;
- report destination notes that keep generated outputs out of registry, policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Duplicate source validator implementation that diverges from `source/` or SourceDescriptor lanes | choose one path via ADR/migration and use the other as shim or docs |
| Source registry records, activation decisions, source authority registers, source payloads | `data/registry/sources/`, accepted control-plane/source registry homes, governed lifecycle roots |
| SourceDescriptor semantic contracts | `contracts/source/` |
| SourceDescriptor JSON Schemas, enums, DTOs, or machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/sources/` if accepted, or accepted schema homes |
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
| `SOURCES_VALIDATOR_PASS` | Candidate passed configured plural-path compatibility checks. |
| `SOURCES_VALIDATOR_FAIL` | Candidate failed one or more configured plural-path compatibility checks. |
| `SOURCES_VALIDATOR_DENY` | Candidate must not proceed because source path, role, rights, sensitivity, access, registry, evidence, policy, release, correction, rollback, or public-surface support cannot be resolved. |
| `SOURCES_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SOURCES_VALIDATOR_HOLD` | Candidate must remain held pending path, source, rights, sensitivity, citation, review, registry, or policy closure. |
| `SOURCES_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a source assertion or route selection. |
| `SOURCES_PATH_DRIFT` | Plural `sources/` route conflicts with singular or SourceDescriptor validator route. |
| `SOURCES_IMPLEMENTATION_DUPLICATE_DENIED` | Plural route defines divergent executable behavior without ADR/migration note. |
| `SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor reference is absent or unresolved. |
| `SOURCE_REGISTRY_LINK_MISSING` | Required source registry or source authority reference is absent. |
| `SOURCE_ROLE_MISSING` | Required source role is absent or unsupported. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Source role is upgraded or collapsed downstream. |
| `SOURCE_RIGHTS_UNRESOLVED` | Rights, license, terms, attribution, redistribution, AI use, or access posture is unresolved. |
| `SOURCE_SENSITIVITY_UNRESOLVED` | Sensitivity default, review, redaction, consent, geoprivacy, or restricted-use posture is unresolved. |
| `SOURCE_CADENCE_STALE` | Cadence, source-head, retrieval time, valid time, or stale-state posture is missing or stale. |
| `SOURCE_CITATION_MISSING` | Required citation or attribution guidance is absent. |
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
tools/validators/sources/
├── README.md
├── validate_source_descriptor.py        # PROPOSED legacy/compatibility shim; not confirmed
├── validate_sources_route.py            # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If the project chooses singular `tools/validators/source/` or `tools/validators/source_descriptor/` as the executable home, keep this plural folder as a compatibility README or shim until references are migrated. Do not maintain two divergent validators.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/sources/README.md`.
- [x] It records `sources/` as a plural compatibility/index lane tied to older or proposed references.
- [x] It distinguishes this path from `tools/validators/source/`, `tools/validators/source_descriptor/`, `tools/validators/source-descriptor/`, and `tools/validators/source_role/`.
- [x] It marks this path as validator routing, not source registry, source admission authority, schema authority, policy authority, evidence authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves source-role anti-collapse, rights/sensitivity/cadence/citation admission posture, registry linkage, correction/supersession posture, path-drift handling, and fail-closed behavior.
- [x] It routes source meaning to `contracts/`, machine shape to `schemas/`, registry records to `data/registry/sources/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, source activation register maturity, schema drift, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to plural source validators are searched and classified.
- [ ] Boundary between `sources/`, `source/`, `source_descriptor/`, and `source-descriptor/` validators is confirmed by ADR, migration note, or accepted convention.
- [ ] Source registry and source activation register homes are verified.
- [ ] SourceDescriptor schema path drift and fixture-root drift are resolved or documented.
- [ ] Fixture files are added or verified only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, path-drift, duplicate-implementation, descriptor-missing, registry-missing, role-collapse, rights-unresolved, sensitivity-unresolved, stale-cadence, missing-citation, release-missing, and public-surface-blocked cases.
- [ ] CI invokes accepted source validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with plural sources validator compatibility README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
