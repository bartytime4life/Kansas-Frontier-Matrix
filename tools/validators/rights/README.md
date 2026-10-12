<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-rights-readme
title: tools/validators/rights README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-rights-steward-plus-source-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward-plus-privacy-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; rights-validator-index; source-rights-aware; license-aware; attribution-aware; consent-aware; sovereignty-aware; cultural-sensitivity-aware; privacy-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: parent rights validator routing README under tools/validators; documents rights validation expectations for source license, access terms, reuse authority, redistribution permission, attribution obligations, consent, stewardship authority, sovereignty and cultural sensitivity constraints, public-surface limits, SourceDescriptor rights posture, RightsDecision or policy decision references, lifecycle quarantine routing, evidence/proof/receipt linkage, release readiness, correction/rollback propagation, schema/fixture/test routing, and finite outcomes while deferring source registry authority, policy decisions, legal determinations, canonical schemas, semantic contracts, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../policy/README.md
  - ../lifecycle/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../maplibre/README.md
  - ../../../docs/sources/RIGHTS_GUIDANCE.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/policy/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../policy/release/
  - ../../../data/registry/sources/
  - ../../../data/quarantine/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/rights/README.md. It does not confirm executable rights validators, registry wiring, policy bundles, rights decision storage, or CI behavior."
  - "Rights are a first-class admission and release condition. Unknown, ambiguous, contested, expired, or incompatible rights fail closed."
  - "A rights validator may check SourceDescriptor rights posture, license/terms fields, consent/stewardship references, obligations, policy decisions, quarantine routing, and release readiness. It does not decide legal rights, issue legal advice, approve release, write policy decisions, or publish outputs."
  - "Source role, rights, and sensitivity are fixed at admission and must travel with downstream derivatives. Promotion must not upgrade or erase rights limits."
  - "Rights-unresolved material must route to quarantine or hold/restrict/deny/abstain posture until source terms, rights posture, sensitivity, evidence, review, receipts, correction path, and rollback target are resolved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/rights

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-rights--validator--index-informational)
![authority](https://img.shields.io/badge/authority-validator--not--legal--or--policy--root-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/rights/` is the rights validator routing index for checking source rights, licenses, access terms, reuse authority, attribution obligations, consent/stewardship constraints, sovereignty/cultural sensitivity posture, quarantine routing, release readiness, and public-surface denial without becoming legal authority, policy authority, source registry authority, or release authority.

---

## Purpose

`tools/validators/rights/` exists to organize rights-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a candidate source, derivative, catalog record, triplet, layer, release candidate, public artifact, export, map surface, search index, graph edge, story, Focus Mode surface, screenshot, embedding, or AI answer carry sufficient rights, terms, license, consent, stewardship, attribution, redistribution, sensitivity, policy, review, evidence, correction, rollback, and release support for its intended KFM use?

The answer should be a deterministic validation result or routing decision. This folder should not make legal determinations, author policy rules, own SourceDescriptor records, store rights decisions, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, authorize public API/UI/map/AI access, or convert generated language into rights authority.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/rights/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `docs/sources/RIGHTS_GUIDANCE.md` | **CONFIRMED draft guidance / implementation NEEDS VERIFICATION** | Rights are described as a first-class admission condition, with unknown rights failing closed and rights records traveling through the lifecycle. |
| `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | SourceDescriptor governs source identity, role, rights, sensitivity, cadence, and citation guidance at admission; allow/deny/restrict/abstain decisions belong in policy. |
| `tools/validators/policy/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Policy validator routing covers rights posture, sensitivity posture, obligations, evidence context, release references, and public-surface denial without becoming policy authority. |
| `data/quarantine/flora/rights_unresolved/README.md` | **CONFIRMED quarantine example / payload behavior NEEDS VERIFICATION** | Demonstrates rights-unresolved material as no-public-path quarantine with hold/deny/restrict/abstain posture until review and release support are resolved. |
| Executable rights validator scripts, registry wiring, rights-decision homes, policy bundles, schema bindings, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/rights/` is a **validator routing index**, not the rights, source registry, policy, or legal authority root.

| Responsibility | Preferred home | Validator relationship |
|---|---|---|
| Rights validation adapters | `tools/validators/rights/` | Check rights readiness and emit deterministic findings. |
| SourceDescriptor records and source registry entries | `data/registry/sources/` and accepted source registry homes | Validators check references; they do not own registry authority. |
| Source descriptor semantic meaning | `contracts/source/` | Contracts explain object meaning; validators check conformance. |
| Source descriptor and policy machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/policy/` | Schemas define shape; validators check schema bindings. |
| Rights, sensitivity, access, publication, and release policy | `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes | Validators reference accepted policy bundle ids/digests; they do not decide policy. |
| Rights guidance and doctrine | `docs/sources/RIGHTS_GUIDANCE.md`, `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | Human-facing standards; validators check conformance. |
| Quarantine for unresolved rights | `data/quarantine/` and domain-specific quarantine lanes | Validators route held material; they do not store lifecycle payloads. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check refs and may emit receipt-ready metadata only to accepted homes. |
| Release decisions and rollback | `release/` | Validator success is not release approval. |
| Fixtures and tests | `fixtures/`, `tests/`, accepted fixture/test homes | Synthetic examples and tests prove behavior; they are not rights authority. |

Validators may fail closed when required rights support is absent, stale, contradictory, unsupported, contested, expired, non-transferable, incompatible with intended use, or unresolved. They must not silently substitute source popularity, public web visibility, generated text, map visibility, file path presence, schema validity, or citation availability for rights permission.

[Back to top](#top)

---

## Rights validation packet

A rights candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Source identity | SourceDescriptor ref, source id, source role, source owner/steward where applicable, source version, source access path, and acquisition context. | Rights permission by source existence. |
| Rights posture | License, terms of use, rights holder, reuse/redistribution permission, public-display permission, derivative-work permission, AI-use posture, and expiration/renewal posture. | Legal conclusion by validator. |
| Attribution obligations | Citation text, required attribution, copyright notice, license notice, link-back requirement, disclaimer, and downstream propagation rules. | Evidence support or release approval. |
| Consent/stewardship posture | Consent scope, revocation posture, stewardship authority, partner terms, tribal/cultural authority, CARE obligations, living-person/privacy constraints, and review owner. | Permanent permission or transferable consent. |
| Sensitivity overlap | Rights posture combined with T0–T4 sensitivity, precise location, protected species, archaeology, infrastructure, DNA/genomic, private parcel/person, or cultural sensitivity. | Sensitivity downgrade by license alone. |
| Evidence/policy support | EvidenceRef, RightsDecision or PolicyDecision refs, policy bundle id/version/digest, reason codes, obligations, review flags, and decision timestamp where applicable. | Policy approval inside validator. |
| Lifecycle posture | Current phase, requested transition, quarantine status, rights reevaluation state, and derivative inheritance. | File path as permission proof. |
| Release posture | ReleaseManifest or release reference, correction path, withdrawal posture, rollback target, reevaluation/expiration rule, and public-surface allowlist. | Publication approval by itself. |

[Back to top](#top)

---

## Rights invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Rights are fixed at admission | Source role, rights, sensitivity, cadence, and citation guidance are recorded before source bytes shape claims. | Source is used before rights posture is established. |
| Unknown rights fail closed | Missing, ambiguous, contested, expired, incompatible, or unverifiable rights route to hold/quarantine/deny/restrict/abstain. | Candidate proceeds by assumption or generated interpretation. |
| Rights travel downstream | Derivatives, joins, layers, tiles, reports, stories, embeddings, exports, screenshots, and AI answers inherit upstream obligations and restrictions. | Derivative drops source terms or attribution obligations. |
| Public visibility is not permission | Public web access, public-record status, or file availability does not automatically grant KFM public reuse. | Validator treats discoverability as license. |
| License is not sensitivity clearance | A permissive license does not override geoprivacy, cultural sensitivity, living-person, DNA/genomic, archaeology, infrastructure, or private-land limits. | Candidate downgrades sensitivity because rights appear open. |
| Consent is scoped and revocable | Consent and partner terms are explicit, current, use-scoped, audience-scoped, and revocation-aware. | Consent is implied, stale, inherited, unscoped, revoked, or not traceable. |
| FAIR pairs with CARE | Technical openness is checked alongside responsibility, authority to control, ethics, and community/steward obligations where applicable. | FAIR reuse is treated as sufficient when CARE restrictions apply. |
| Release requires rights closure | Public-bound candidates need rights/policy/review/release support and rollback/correction posture. | Release proceeds with unresolved rights or obligations. |
| Corrections propagate | Rights changes, source-term changes, revocation, takedown request, correction, withdrawal, supersession, or rollback invalidates downstream carriers. | Downstream artifact remains active after rights support changes. |

[Back to top](#top)

---

## Fail-closed conditions

A rights candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- SourceDescriptor rights fields, license fields, access terms, citation guidance, source role, sensitivity, cadence, or steward information are missing or unresolved;
- license terms conflict with intended storage, transformation, redistribution, public display, map rendering, export, story publication, search indexing, embedding, AI summarization, screenshot generation, or downstream reuse;
- rights holder, stewardship authority, consent scope, partner terms, cultural authority, or tribal/community authority is missing, ambiguous, contradicted, revoked, or expired;
- attribution obligations, disclaimers, link-backs, copyright notices, no-derivatives clauses, no-commercial clauses, no-AI clauses, no-redistribution clauses, access-window limits, or audience limits cannot be satisfied;
- rights uncertainty overlaps with precise location, rare species, archaeology, cultural sensitivity, infrastructure exposure, DNA/genomic data, living-person data, private parcel/person links, or protected community data;
- policy, review, evidence, release, correction, withdrawal, rollback, or reevaluation references are required but absent;
- a candidate tries to leave quarantine without closing the rights reason code;
- a derivative, join, tile, layer, report, graph, search index, embedding, screenshot, Focus Mode card, story, or AI answer drops inherited rights obligations;
- public surfaces would expose rights-limited, restricted, unresolved, withdrawn, revoked, stale, or unsupported content.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Rights validator routing | `tools/validators/rights/` |
| Policy validation | `tools/validators/policy/` |
| Lifecycle/quarantine validation | `tools/validators/lifecycle/` |
| Release/promotion validation | `tools/validators/release/`, `tools/validators/promotion_gate/` |
| Evidence/citation validation | `tools/validators/evidence/`, `tools/validators/citation/` |
| Source descriptor doctrine | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` |
| Rights doctrine | `docs/sources/RIGHTS_GUIDANCE.md` |
| Source descriptor semantic contracts | `contracts/source/` |
| Source and policy schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/policy/` |
| Source registry records | `data/registry/sources/` and accepted registry homes |
| Rights/sensitivity/release policy | `policy/rights/`, `policy/sensitivity/`, `policy/release/`, accepted policy homes |
| Quarantine/lifecycle data | `data/quarantine/` and other `data/` lifecycle roots |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records and process outputs | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared rights-readiness invariants and delegates policy, legal/steward decisions, source registry authority, schemas, contracts, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, RightsDecision schema/contract homes, policy bundle homes, policy bundle digests, source registry topology, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as legal authority, policy rule authority, rights decision store, source registry, source payload store, lifecycle data store, proof store, receipt store, release record store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/rights/` include:

- this README;
- small validation adapters that check rights readiness, rights inheritance, source descriptor rights fields, obligations, consent/stewardship references, policy bundle references, and release readiness;
- checks for unknown/ambiguous/contested/expired rights and quarantine routing;
- checks that attribution, disclaimers, citation obligations, no-derivatives/no-redistribution/no-AI/no-commercial restrictions, and audience limits propagate downstream;
- checks that rights limitations are preserved across derivatives, joins, tiles, layers, reports, graphs, search indexes, embeddings, exports, screenshots, Focus Mode cards, stories, and AI answers;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of source registry, policy, proof, receipt, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Legal opinions, final rights determinations, steward approvals, policy rules, allowlists, denylists, thresholds | `policy/`, steward review records, or accepted governance homes |
| SourceDescriptor records or source registry payloads | `data/registry/sources/` and accepted registry homes |
| Source data, downloaded payloads, licensed media, restricted datasets, private terms, source credentials | dedicated governed data/security homes; not validator docs |
| Canonical schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/policy/`, accepted schema homes |
| Semantic contracts | `contracts/source/`, `contracts/policy/`, accepted contract homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `RIGHTS_VALIDATOR_PASS` | Candidate passed configured rights checks. |
| `RIGHTS_VALIDATOR_FAIL` | Candidate failed one or more configured rights checks. |
| `RIGHTS_VALIDATOR_DENY` | Candidate must not proceed because rights, terms, consent, stewardship, sensitivity, policy, release, correction, rollback, or public-surface support cannot be resolved. |
| `RIGHTS_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `RIGHTS_VALIDATOR_HOLD` | Candidate must remain held pending rights, consent, stewardship, evidence, or policy review. |
| `RIGHTS_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a rights assertion. |
| `SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source registry reference is absent. |
| `SOURCE_RIGHTS_MISSING` | Source rights, license, or terms fields are absent. |
| `RIGHTS_UNKNOWN` | Rights posture is unresolved and must fail closed. |
| `RIGHTS_CONFLICT_WITH_USE` | Source terms conflict with intended KFM use or public surface. |
| `ATTRIBUTION_OBLIGATION_MISSING` | Required attribution, notice, citation, disclaimer, or link-back obligation is absent. |
| `CONSENT_STATE_MISSING` | Required consent or stewardship authority is absent or unresolved. |
| `CONSENT_REVOKED` | Consent was revoked and downstream cleanup, correction, or rollback is required. |
| `REDISTRIBUTION_NOT_ALLOWED` | Source terms do not permit redistribution or public release. |
| `DERIVATIVE_USE_NOT_ALLOWED` | Source terms do not permit derivative work, transformation, tiling, embedding, AI summarization, or other intended downstream use. |
| `AI_USE_NOT_ALLOWED` | Source terms, consent, or policy do not permit AI summarization, embedding, retrieval, or generated-answer use. |
| `SENSITIVITY_RIGHTS_CONFLICT` | Rights posture interacts with sensitivity restrictions and cannot be safely resolved. |
| `QUARANTINE_REQUIRED` | Candidate must enter or remain in quarantine because rights support is unresolved. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, rights review, steward review, or reason-code support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `RIGHTS_CORRECTION_CASCADE_MISSING` | Rights change, revocation, takedown, withdrawal, or correction did not propagate downstream. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose rights-limited or unreleased content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/rights/
├── README.md
├── validate_rights_packet.py            # PROPOSED; not confirmed
├── validate_source_rights.py            # PROPOSED; not confirmed
├── validate_rights_inheritance.py       # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, local schema files, rights-decision records, source registry records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting rights or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/rights/README.md`.
- [x] It marks this path as rights validator routing, not legal authority, policy authority, source registry authority, evidence authority, proof/receipt storage, lifecycle data, release records, public runtime, or AI authority.
- [x] It preserves fail-closed posture for unknown, ambiguous, contested, expired, incompatible, revoked, or unsupported rights.
- [x] It routes source registry records to `data/registry/`, policy to `policy/`, source contracts to `contracts/`, schemas to `schemas/`, evidence/proofs/receipts to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It distinguishes public visibility, citation availability, license openness, schema validity, and validator success from rights permission, evidence closure, policy approval, release approval, and public safety.
- [x] It marks executable scripts, registry wiring, RightsDecision homes, policy bundles, schema files, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to rights validators are searched and classified.
- [ ] RightsDecision contract/schema homes and source rights policy bundle homes are verified.
- [ ] SourceDescriptor rights fields, source registry topology, accepted license vocabulary, obligation vocabulary, consent vocabulary, and reason-code vocabulary are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, consent-revoked, attribution-missing, derivative-use-denied, AI-use-denied, quarantine-required, and public-surface-blocked cases.
- [ ] CI invokes rights validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with rights validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
