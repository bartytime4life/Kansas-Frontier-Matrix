<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-source-role-readme
title: tools/validators/source_role README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-source-steward-plus-validator-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; source-role-validator-index; source-admission; source-role-anti-collapse; authority-rank-aware; admissibility-limits-aware; evidence-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: source-role validator routing README under tools/validators; documents validation expectations for source_role presence, authority_rank presence, role vocabulary conformance, role immutability after admission, role-to-claim compatibility, admissibility limits, source-role anti-collapse, modeled/aggregate/candidate/context/primary role boundaries, evidence support posture, downstream role propagation, policy/review/release posture, correction and supersession handling, fixture/test routing, and finite outcomes while deferring SourceDescriptor meaning, source-role vocabulary authority, canonical schemas, policy decisions, source registry records, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../source/README.md
  - ../source-descriptor/README.md
  - ../source_descriptor/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../policy/README.md
  - ../evidence/README.md
  - ../lifecycle/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/sources/source-roles.md
  - ../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/README.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../data/registry/sources/
  - ../../../policy/source/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../policy/release/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/contracts/v1/source/source_descriptor/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/source_role/README.md. It does not confirm executable source-role validators, registry wiring, schema bindings, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "Source role is fixed at source admission. Promotion, publication, map rendering, AI generation, downstream derivation, or catalog appearance must not upgrade a role."
  - "This lane validates source-role posture and anti-collapse behavior. It does not define the source-role vocabulary, mutate source descriptors, decide policy, approve release, or make source claims true."
  - "Exact enum values and source-role vocabulary authority remain NEEDS VERIFICATION unless verified from the active schema, accepted ADR, or source-role standard."
  - "Unknown, missing, contradictory, unsupported, AI-inferred, or downstream-upgraded source roles should fail closed or route to steward review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/source_role

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-source__role--validator-informational)
![posture](https://img.shields.io/badge/posture-anti--collapse-critical)
![authority](https://img.shields.io/badge/authority-validator--not--vocabulary-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/source_role/` is the source-role validator routing lane for checking `source_role`, `authority_rank`, admissibility limits, role-to-claim compatibility, source-role anti-collapse, downstream role propagation, and review/release posture without becoming the source-role vocabulary authority, source registry, schema home, policy authority, evidence authority, or release authority.

---

## Purpose

`tools/validators/source_role/` exists to make source-role validation visible under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a source candidate, SourceDescriptor, registry entry, connector preflight output, catalog record, EvidenceRef, release candidate, map layer, graph edge, export, screenshot, embedding, Focus Mode card, or AI answer preserve the admitted source role, authority rank, admissibility limits, claim-role boundaries, correction lineage, policy/review posture, and public-surface limits without upgrading or collapsing source authority?

The answer should be a deterministic validation result or routing decision. This folder should not define source-role vocabulary, assign roles as authority, mutate SourceDescriptor records, store source registry records, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, expose public API/map/AI payloads, or turn source metadata into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/source_role/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Includes source-role vocabulary and anti-collapse sections. |
| `contracts/source/source_descriptor.md` | **CONFIRMED contract / schema-paired draft** | SourceDescriptor requires `source_role`, `authority_rank`, and `admissibility_limits`; exact accepted enum values still need active schema verification here. |
| `tools/validators/source/README.md` | **CONFIRMED parent README / executable behavior NEEDS VERIFICATION** | Broad source validator parent route already treats source role and anti-collapse as parent source concerns. |
| `tools/validators/source-descriptor/README.md` and `tools/validators/source_descriptor/README.md` | **CONFIRMED sibling READMEs / executable behavior NEEDS VERIFICATION** | SourceDescriptor-specific lanes cover broader descriptor validation and naming drift. |
| Executable source-role validator scripts, registry wiring, source-role vocabulary authority, schema bindings, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/source_role/` is a **validator routing lane**, not the source-role vocabulary authority.

| Responsibility | Preferred home | Validator relationship |
|---|---|---|
| Source-role validation adapters | `tools/validators/source_role/` | Check declared source-role posture and anti-collapse behavior. |
| Broad source validation | `tools/validators/source/` | Parent source validation route. |
| SourceDescriptor validation | `tools/validators/source-descriptor/`, `tools/validators/source_descriptor/` | Full descriptor packet validation. |
| Source-role doctrine and vocabulary | `docs/sources/`, accepted ADRs, accepted source-role standard | Validators check conformance; they do not define vocabulary. |
| SourceDescriptor meaning | `contracts/source/source_descriptor.md` and accepted source contracts | Contracts define semantic meaning. |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/` or accepted schema homes | Schemas define required fields and enum shape. |
| Source registry records | `data/registry/sources/` and accepted source registry homes | Validators check refs; they do not own records. |
| Source policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/release/` | Validators reference policy outputs; they do not decide policy. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check refs; they do not create authority records. |
| Release/correction/rollback | `release/` | Validator success is not release approval. |
| Fixtures and tests | `fixtures/`, `tests/` | Synthetic examples and tests prove behavior; they are not role authority. |

[Back to top](#top)

---

## Source-role validation packet

A source-role candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Source identity | Stable source id, descriptor ref, descriptor version, source family, source registry ref, and source authority ref where used. | Truth of source claims. |
| Source role | `source_role` is present, accepted by the active vocabulary, and consistent with the descriptor version. | Role assignment by validator. |
| Authority rank | `authority_rank` is present and compatible with the source role, source type, and intended claim use. | Claim truth or release approval. |
| Admissibility limits | Allowed/prohibited claim roles, confidence posture, and role-specific limits are present where required. | Permission to use source for all claim types. |
| Claim-role compatibility | Candidate claim, layer, triplet, map, graph, export, or AI answer uses the source only within its admitted role. | Upgrade by downstream consumer. |
| Review lineage | Role assignment, role correction, role supersession, or role downgrade has steward/ticket/correction lineage where required. | Silent in-place authority change. |
| Rights/sensitivity posture | Role usage is checked alongside rights, sensitivity, consent, access, and public-release constraints. | Role as a substitute for policy. |
| Evidence/policy/release support | EvidenceRef, validation report, policy decision, reason codes, obligations, release reference, correction path, rollback target, and receipts exist where required. | Public-surface authorization. |
| Consumer envelope | Connector, watcher, pipeline, catalog, proof, release, map, API, graph, export, embedding, Focus Mode, and AI surfaces preserve the role. | Unbounded reuse. |

[Back to top](#top)

---

## Anti-collapse invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Role is fixed at admission | Source role is set by governed admission and visible in SourceDescriptor posture. | Role is missing, inferred by AI, or inferred from source popularity. |
| Promotion does not upgrade role | Release or publication never converts a weak role into a stronger one. | Modeled becomes observed, aggregate becomes per-place truth, candidate becomes verified, or contextual becomes authoritative. |
| Corrections are explicit | Role changes require descriptor versioning, correction/supersession lineage, review, and policy impact checks. | Role changes silently in place. |
| Claim use respects role | Claims, layers, triplets, joins, maps, graphs, exports, and AI answers use the source only for allowed claim roles. | Source is used outside admitted role. |
| Role differs from rights and sensitivity | A strong source role does not override rights, sensitivity, consent, or release limits. | Role is used to bypass rights, geoprivacy, or review. |
| Role differs from evidence closure | A source role says how a source may contribute; it does not prove the claim. | Source role is treated as EvidenceBundle closure. |
| Derivatives preserve role lineage | Transform, redaction, aggregation, tiling, embedding, and AI downstream outputs preserve role lineage and limitations. | Derivative drops or upgrades role metadata. |
| Carriers are not role authority | Maps, tiles, screenshots, popups, exports, graph edges, Focus Mode cards, and AI prose are downstream carriers. | Carrier assigns or upgrades role. |

[Back to top](#top)

---

## Fail-closed conditions

A source-role candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- `source_role`, `authority_rank`, `admissibility_limits`, source id, descriptor version, or registry linkage is missing or malformed;
- source-role value is not accepted by the active vocabulary or cannot be verified against the active schema/standard;
- role is inferred by AI, copied from prose, guessed from publisher reputation, guessed from file path, or inferred from public web visibility;
- downstream flow upgrades modeled to observed, aggregate to per-place truth, candidate to verified, contextual to authoritative, corroborating to primary, or any weaker role to a stronger one without governed correction and review;
- a claim, layer, triplet, graph edge, tile, export, screenshot, Focus Mode card, or AI answer uses the source outside its admitted role;
- role assignment conflicts with rights, sensitivity, access, cadence, citation, evidence, policy, review, release, correction, or rollback posture;
- role correction, downgrade, supersession, or retirement lacks traceable lineage;
- public surfaces would expose a candidate, restricted, unresolved, or role-limited source as stronger evidence than admitted.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Source-role validator routing | `tools/validators/source_role/` |
| Broad source validation | `tools/validators/source/` |
| SourceDescriptor validation | `tools/validators/source-descriptor/`, `tools/validators/source_descriptor/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Source-role doctrine/vocabulary | `docs/sources/`, accepted ADRs, accepted vocabulary docs |
| SourceDescriptor semantic contract | `contracts/source/source_descriptor.md` and accepted source contract homes |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/` or accepted schema homes |
| Source registry records | `data/registry/sources/` and accepted source registry homes |
| Source policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists at `tools/validators/source_role/README.md`.
- **PROPOSED:** validator code may live here when it checks declared source-role and anti-collapse invariants and delegates vocabulary authority, meaning, schemas, registry records, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, source-role vocabulary authority, accepted enum values, schema bindings, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as source-role vocabulary authority, source registry, source data store, source admission authority, legal authority, policy rule authority, canonical schema home, semantic contract home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/source_role/` include:

- this README;
- small validation adapters that check source-role presence and anti-collapse behavior;
- checks that `source_role`, `authority_rank`, and `admissibility_limits` are present and compatible with active schema/contract/vocabulary;
- checks that downstream consumers do not upgrade or erase source role;
- checks that role changes require descriptor versioning, correction, review, and policy impact handling;
- checks that source role does not override rights, sensitivity, evidence, policy, release, correction, or rollback requirements;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of registry, policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Source-role vocabulary authority, enum definitions, ADRs, steward decisions | `docs/sources/`, `schemas/`, `policy/`, accepted ADR/governance homes |
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
| `SOURCE_ROLE_VALIDATOR_PASS` | Candidate passed configured source-role checks. |
| `SOURCE_ROLE_VALIDATOR_FAIL` | Candidate failed one or more configured source-role checks. |
| `SOURCE_ROLE_VALIDATOR_DENY` | Candidate must not proceed because source role, authority rank, admissibility, policy, evidence, review, release, correction, rollback, or public-surface support cannot be resolved. |
| `SOURCE_ROLE_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SOURCE_ROLE_VALIDATOR_HOLD` | Candidate must remain held pending source-role, review, registry, or policy closure. |
| `SOURCE_ROLE_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a source-role assertion. |
| `SOURCE_ROLE_MISSING` | Required `source_role` is absent. |
| `AUTHORITY_RANK_MISSING` | Required `authority_rank` is absent. |
| `ADMISSIBILITY_LIMITS_MISSING` | Required allowed/prohibited claim-role posture is absent. |
| `SOURCE_ROLE_UNSUPPORTED` | Role value is not accepted by the active vocabulary or schema. |
| `SOURCE_ROLE_AI_INFERRED_DENIED` | Role was inferred by AI or generated text rather than governed admission. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Role is upgraded, downgraded, erased, or collapsed downstream without governed correction/review. |
| `CLAIM_ROLE_INCOMPATIBLE` | Candidate uses the source outside its admitted claim role or authority rank. |
| `ROLE_LINEAGE_MISSING` | Role correction, supersession, or retirement lacks traceable descriptor lineage. |
| `ROLE_POLICY_OR_REVIEW_GAP` | Required policy decision, steward review, rights review, sensitivity review, or reason-code support is absent. |
| `ROLE_EVIDENCE_GAP` | Required EvidenceRef, EvidenceBundle, or validation support is absent. |
| `ROLE_RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `SOURCE_ROLE_OVERCLAIM` | Role metadata is treated as claim truth, evidence closure, policy approval, release approval, or public permission. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose source-limited or role-limited content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/source_role/
├── README.md
├── validate_source_role.py              # PROPOSED; not confirmed
├── validate_role_anti_collapse.py       # PROPOSED; not confirmed
├── validate_claim_role_compatibility.py # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, local vocabulary files, local schema files, registry records, policy bundles, source data, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting source-role, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/source_role/README.md`.
- [x] It marks this path as source-role validator routing, not source-role vocabulary authority, source registry, source admission authority, schema authority, policy authority, evidence authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves role-fixed-at-admission posture, anti-collapse checks, role-to-claim compatibility, correction/supersession lineage, and fail-closed handling.
- [x] It routes source-role doctrine/vocabulary to `docs/` and accepted ADR/schema homes, source meaning to `contracts/`, machine shape to `schemas/`, registry records to `data/registry/sources/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks exact enum values, executable scripts, registry wiring, schema bindings, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to source-role validators are searched and classified.
- [ ] Accepted source-role vocabulary and enum values are verified from schema, ADR, or source-role standard.
- [ ] Source role, authority rank, admissibility limits, claim-role compatibility, and anti-collapse schema bindings are verified.
- [ ] Fixture files are added or verified only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, role-missing, unsupported-role, AI-inferred-role, role-collapse, claim-role-incompatible, lineage-missing, release-missing, and public-surface-blocked cases.
- [ ] CI invokes source-role validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with source-role validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
