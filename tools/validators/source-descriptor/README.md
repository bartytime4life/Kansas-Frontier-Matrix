<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-source-descriptor-readme
title: tools/validators/source-descriptor README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-source-steward-plus-validator-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; source-descriptor-validator-index; source-admission; source-role-anti-collapse; rights-aware; sensitivity-aware; cadence-aware; citation-aware; registry-aware; fail-closed; release-gated; non-authoritative; naming-drift-aware
owning_root: tools/
responsibility: parent SourceDescriptor validator routing README under tools/validators; documents validation expectations for source identity, descriptor versioning, source type, source role, authority rank, publisher/steward, rights, sensitivity default, cadence, access posture, citation guidance, source-head/content identity, admissibility limits, public release posture, review state, release state, lifecycle posture, registry linkage, schema/contract pairing, policy/evidence/release references, correction/supersession posture, naming drift, fixture/test routing, and finite outcomes while deferring SourceDescriptor meaning, canonical schemas, policy decisions, source registry records, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
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
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/SOURCE_DESCRIPTOR.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/source/source-descriptor.schema.json
  - ../../../data/registry/sources/
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
  - "This README replaces an empty placeholder at tools/validators/source-descriptor/README.md. It does not confirm executable SourceDescriptor validators, registry wiring, schema bindings, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "docs/sources/SOURCE_DESCRIPTOR_STANDARD.md names tools/validators/source_descriptor/ with an underscore as a proposed validator path. That underscore README was not found during this edit. This hyphenated path is therefore documented as the confirmed requested routing lane with naming drift still NEEDS VERIFICATION."
  - "SourceDescriptor fixes source identity, role, rights, sensitivity, cadence, access posture, and citation guidance at admission. It does not make source claims true, approve release, replace EvidenceBundles, or authorize AI/public surfaces."
  - "Source role, rights, and sensitivity must not be upgraded downstream by promotion, generation, publication, map rendering, or AI summary. Corrections and supersession should produce traceable descriptor/version transitions."
  - "Unknown rights, unresolved sensitivity, missing source role, stale cadence, unresolved access limits, missing citation guidance, missing review state, missing release state, or registry gaps should fail closed or route to quarantine/review, not default to public use."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/source-descriptor

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-source--descriptor--validator-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![authority](https://img.shields.io/badge/authority-validator--not--registry-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/source-descriptor/` is the SourceDescriptor validator routing lane for checking source-admission records, source role, rights, sensitivity, cadence, access, citation, source-head identity, admissibility limits, review/release state, registry linkage, and anti-collapse posture without becoming the source registry, schema home, policy authority, evidence authority, or release authority.

---

## Purpose

`tools/validators/source-descriptor/` exists to make SourceDescriptor validation visible under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a SourceDescriptor candidate carry the required source identity, descriptor version, source type, source role, authority rank, publisher/steward, rights, sensitivity default, cadence, access posture, citation guidance, source-head/content identity, admissibility limits, public-release posture, review state, release state, lifecycle posture, registry linkage, policy references, evidence/release readiness, correction/supersession posture, and finite outcomes required before source material can shape downstream claims?

The answer should be a deterministic validation result or routing decision. This folder should not define SourceDescriptor meaning, store source registry records, write source descriptors as authority, define machine schemas, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, expose public API/map/AI payloads, or turn source metadata into truth.

[Back to top](#top)

---

## Naming and placement note

The repository currently has this requested hyphenated path:

```text
tools/validators/source-descriptor/README.md
```

The Source Descriptor Standard also names a proposed underscore path:

```text
tools/validators/source_descriptor/
```

During this edit, the underscore README was **not found**, while the hyphenated requested path was present as an empty placeholder. Until an accepted ADR or migration note settles the spelling, this README treats `tools/validators/source-descriptor/` as a **confirmed routing README** and records `source_descriptor` versus `source-descriptor` as **NEEDS VERIFICATION / naming drift**.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/source-descriptor/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/source_descriptor/README.md` | **NOT FOUND in this edit** | The Source Descriptor Standard names the underscore validator path as proposed; spelling remains a drift item. |
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines SourceDescriptor scope, fields, role/rights/sensitivity vocabulary, intake posture, citation guidance, and anti-collapse rule. |
| `contracts/source/source_descriptor.md` | **CONFIRMED contract / schema-paired draft** | Defines SourceDescriptor as governed source-admission and authority-control descriptor; not source truth, release approval, or policy bypass. |
| `schemas/contracts/v1/source/README.md` | **CONFIRMED schema-family README / mixed maturity** | Source schemas define object shape only; registry records, emitted records, lifecycle data, validators, and release records live outside schemas. |
| `tools/validators/rights/README.md` | **CONFIRMED sibling README / executable behavior NEEDS VERIFICATION** | Rights validation checks SourceDescriptor rights posture and related policy/release readiness without becoming rights authority. |
| Executable SourceDescriptor validator scripts, registry wiring, schema bindings, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## SourceDescriptor validation packet

A SourceDescriptor candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Object identity | `object_type`, `schema_version`, `source_id`, `descriptor_version`, title, descriptor status, and stable identity. | Source claim truth. |
| Source classification | Source type, source role, authority rank, domain applicability, allowed/prohibited claim roles, and anti-collapse posture. | Authority upgrade by validator. |
| Publisher/steward | Publisher and owner/steward identity, contacts, stewardship posture, and source accountability. | Legal or policy approval by presence. |
| Rights posture | Rights, license/terms, attribution, redistribution, commercial use, AI use, verification, expiration, and obligations. | Release approval. |
| Sensitivity posture | Sensitivity default, review requirements, redaction/generalization requirements, and most-restrictive downstream posture. | Sensitivity downgrade. |
| Cadence and freshness | Update cadence, source-head observation, retrieved/observed/valid time, staleness policy, and refresh expectations. | Current-truth guarantee. |
| Access posture | Access method, access limits, authentication/credential posture, endpoint/format targets, and no-public-source bypass posture. | Permission to fetch or publish. |
| Citation guidance | Required citation template, attribution text, disclaimer/link-back requirements, and downstream citation obligations. | Evidence closure. |
| Review and lifecycle | Review state, release state, lifecycle state, quarantine/deny/retire/supersede posture, and correction lineage. | Promotion or release by itself. |
| Registry linkage | Accepted registry home, source authority register ref where used, source activation posture, and descriptor version continuity. | Registry record creation by validator. |
| Evidence/policy/release linkage | EvidenceRef, policy decision, reason codes, obligations, ValidationReport, ReleaseManifest, correction path, rollback target where required. | Public-surface authorization. |

[Back to top](#top)

---

## Invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Role is fixed at admission | Source role is explicitly recorded and cannot be upgraded by promotion, AI, UI, or downstream derivative. | Modeled becomes observed, aggregate becomes per-place truth, candidate becomes verified, or context becomes primary evidence without governed transition. |
| Rights and sensitivity are admission gates | Rights, terms, sensitivity, access limits, and review obligations are visible before source material shapes public claims. | Unknown rights or sensitivity defaults to public use. |
| Descriptor is governance handle | Descriptor records how KFM may treat a source. | Descriptor is treated as evidence that source claims are true. |
| Registry remains separate | Source registry records and activation decisions live in accepted registry/control-plane homes. | Validator folder stores source registry authority. |
| Schemas stay in schemas | Machine shape lives under accepted schema homes. | Validator-local schema becomes canonical without ADR. |
| Policy stays in policy | Allow/deny/restrict/hold/abstain decisions live in accepted policy homes and decision records. | Validator success becomes policy approval. |
| Corrections are traceable | Rights changes, sensitivity changes, source-head drift, cadence expiration, supersession, retirement, and correction produce traceable transitions. | Descriptor silently changes without version/correction/supersession posture. |
| Downstream carriers stay subordinate | Catalog, triplets, tiles, maps, exports, graphs, AI answers, and releases cite source posture without upgrading it. | Downstream carrier becomes source authority or evidence closure. |

[Back to top](#top)

---

## Fail-closed conditions

A SourceDescriptor candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- `source_id`, `descriptor_version`, source type, source role, authority rank, publisher/steward, rights, sensitivity default, cadence, access, citation, review state, release state, or lifecycle posture is missing or malformed;
- source role is unknown, contradictory, unsupported, inferred by AI, or upgraded by downstream flow;
- rights, terms, attribution, redistribution, commercial use, AI use, access limits, or source-owner/steward posture is unknown, contested, expired, incompatible, or not verified;
- sensitivity default, redaction/generalization requirement, consent/stewardship posture, cultural/tribal authority, living-person, DNA/genomic, rare species, archaeology, infrastructure, private parcel/person, or precise-location risk is unresolved;
- cadence, source-head/content identity, retrieval time, validity time, stale-state, source retirement, or supersession posture is missing where required;
- citation guidance is absent, impossible to satisfy, or dropped by a downstream surface;
- source registry linkage, activation decision, source authority register reference, or descriptor version lineage is missing where required;
- policy decision, EvidenceRef, ValidationReport, ReleaseManifest, correction path, rollback target, or receipt reference is required but absent;
- source metadata is treated as claim truth, public release permission, evidence closure, or AI/public-surface authority.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| SourceDescriptor validator routing | `tools/validators/source-descriptor/` |
| Possible underscore validator path | `tools/validators/source_descriptor/` — **NEEDS VERIFICATION / naming drift** |
| Shared validator plumbing | `tools/validators/_common/` |
| SourceDescriptor doctrine | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` |
| SourceDescriptor semantic contract | `contracts/source/source_descriptor.md` and accepted source contract homes |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/` or accepted schema homes |
| Source registry records | `data/registry/sources/` and accepted source registry homes |
| Source admission / authority register | accepted control-plane or registry homes when verified |
| Rights, sensitivity, access, and release policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes |
| Rights validation | `tools/validators/rights/` |
| Sensitivity validation | `tools/validators/sensitivity/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists at the requested hyphenated path.
- **PROPOSED:** validator code may live here when it checks declared SourceDescriptor invariants and delegates meaning, schemas, registry records, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** executable files, registry entries, canonical hyphen/underscore path choice, SourceDescriptor schema drift, source activation register maturity, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as source registry, source data store, source admission authority, legal authority, policy rule authority, canonical schema home, semantic contract home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/source-descriptor/` include:

- this README;
- small validation adapters that check SourceDescriptor packets;
- checks for required SourceDescriptor fields, versioning, source role, rights, sensitivity, cadence, access, citation, source-head, admissibility, review state, release state, lifecycle posture, registry linkage, and anti-collapse rules;
- checks that descriptor naming drift and schema-path drift are reported, not silently normalized;
- checks that unknown rights, sensitivity, role, cadence, citation, registry, or release posture fails closed;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, registry, and release authority unless explicitly routed to accepted homes.

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
| `SOURCE_DESCRIPTOR_VALIDATOR_PASS` | Candidate passed configured SourceDescriptor checks. |
| `SOURCE_DESCRIPTOR_VALIDATOR_FAIL` | Candidate failed one or more configured SourceDescriptor checks. |
| `SOURCE_DESCRIPTOR_VALIDATOR_DENY` | Candidate must not proceed because source role, rights, sensitivity, access, registry, evidence, policy, release, correction, rollback, or public-surface support cannot be resolved. |
| `SOURCE_DESCRIPTOR_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SOURCE_DESCRIPTOR_VALIDATOR_HOLD` | Candidate must remain held pending source, rights, sensitivity, citation, review, registry, or policy closure. |
| `SOURCE_DESCRIPTOR_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a source-admission assertion. |
| `SOURCE_DESCRIPTOR_SCHEMA_INVALID` | Candidate fails accepted SourceDescriptor schema checks. |
| `SOURCE_DESCRIPTOR_SCHEMA_HOME_DRIFT` | Candidate uses an unaccepted or drifted hyphen/underscore/plural/singular schema path. |
| `SOURCE_DESCRIPTOR_VALIDATOR_PATH_DRIFT` | Validator path naming is unresolved between hyphenated and underscored routes. |
| `SOURCE_ID_MISSING` | Required source id is absent or malformed. |
| `DESCRIPTOR_VERSION_MISSING` | Descriptor version or supersession lineage is absent. |
| `SOURCE_ROLE_MISSING` | Source role is absent or unsupported. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Source role is upgraded or collapsed downstream. |
| `RIGHTS_POSTURE_UNRESOLVED` | Rights, license, terms, attribution, redistribution, AI use, or access posture is unresolved. |
| `SENSITIVITY_POSTURE_UNRESOLVED` | Sensitivity default, review, redaction, consent, or geoprivacy posture is unresolved. |
| `CADENCE_OR_SOURCE_HEAD_STALE` | Cadence, source-head, retrieved time, valid time, or stale-state posture is missing or stale. |
| `CITATION_GUIDANCE_MISSING` | Required citation or attribution guidance is absent. |
| `REGISTRY_LINKAGE_MISSING` | Required source registry, source activation, or authority-register reference is absent. |
| `PUBLIC_RELEASE_POSTURE_MISSING` | Public release allowance, review, redaction, or conditions are absent. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights review, sensitivity review, or reason-code support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `SOURCE_METADATA_OVERCLAIM` | Descriptor metadata is treated as claim truth, evidence closure, policy approval, release approval, or public permission. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose source-limited or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/source-descriptor/
├── README.md
├── validate_source_descriptor.py        # PROPOSED; not confirmed
├── validate_source_role.py              # PROPOSED; not confirmed
├── validate_source_descriptor_links.py  # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If the project later settles on `tools/validators/source_descriptor/`, use an ADR or migration note and avoid creating two competing validator authorities.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/source-descriptor/README.md`.
- [x] It records the hyphen/underscore validator path issue as **NEEDS VERIFICATION / naming drift**.
- [x] It marks this path as SourceDescriptor validator routing, not source registry, source admission authority, schema authority, policy authority, evidence authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves source-role anti-collapse, rights/sensitivity/cadence/citation admission posture, registry linkage, correction/supersession posture, and fail-closed handling.
- [x] It routes source meaning to `contracts/`, machine shape to `schemas/`, registry records to `data/registry/sources/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, schema drift, source activation register maturity, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to SourceDescriptor validators are searched and classified.
- [ ] Hyphenated and underscored validator path spelling is settled by ADR, migration note, or accepted convention.
- [ ] SourceDescriptor schema path drift between singular `source/`, plural `sources/`, hyphenated, and underscored filenames is resolved or documented.
- [ ] Source registry and source activation register homes are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, schema-invalid, role-collapse, rights-unresolved, sensitivity-unresolved, stale-cadence, missing-citation, registry-missing, release-missing, and public-surface-blocked cases.
- [ ] CI invokes SourceDescriptor validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with SourceDescriptor validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
