<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/habitat-source-roles
title: Habitat Source Roles
adr_id: unassigned
scaffold_identity: ADR-habitat-source-roles
type: architecture-decision-record
version: v1.1
status: proposed
effective_decision_status: proposed
classification: "PROPOSED scaffold; slug-only, unassigned ADR record"
owners:
  - <habitat-domain-steward>
  - <source-governance-steward>
reviewers:
  - <policy-steward>
  - <evidence-steward>
created: 2026-07-24
updated: 2026-09-14
policy_label: public
owning_root: docs/
responsibility: "Preserve the unresolved Habitat source-role assignment question as an unassigned scaffold without admitting a source or accepting a decision."
truth_posture: cite-or-abstain
related:
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/habitat/SOURCE_FAMILIES.md
  - docs/domains/habitat/SOURCE_REGISTRY.md
  - docs/architecture/source-roles.md
  - docs/architecture/source-role-anti-collapse.md
  - docs/architecture/cross-domain/source-role-anti-collapse.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - tests/domains/habitat/test_critical_habitat_source_role.py
  - policy/domains/habitat/source_role.rego
  - policy/domains/habitat/source_role_authority.rego
  - tools/validators/domains/habitat/validate_critical_habitat_source_role.py
  - docs/doctrine/directory-rules.md
tags: [kfm, adr, habitat, source-role, evidence, policy, anti-collapse]
notes:
  - "Currentness refresh v1.1 is evidence-grounded against repository state at commit fff1a37e4e4eba52b795a0fd99572bfb063efc79."
  - "This record remains slug-only and unassigned in docs/adr/INDEX.md; its effective decision status is PROPOSED."
  - "Habitat policy files remain PROPOSED deny-by-default scaffolds; the critical-habitat validator and focused tests are fixture-only and do not prove admission, release, publication, or runtime enforcement."
  - "Concrete source-family role assignments remain PROPOSED until admitted SourceDescriptor records are verified."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: fff1a37e4e4eba52b795a0fd99572bfb063efc79
  target_prior_blob: ed836f8440051eb7bdca675e4cb4eca1e645171e
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  adr_readme_blob: 27c8f00622afe6cd0c65a1b116cd768dac31bea6
  accepted_adr_0029_blob: 4c1ef5f7f812d58fbdde9898acc96bb4c9280b2c
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  cross_register_blob: c5a056011d6496cb2574cedd7f9e5dadadbbbe1e
  habitat_architecture_blob: 82263ea8f5862401e5aef57ec43f49711d12c998
  habitat_source_families_blob: d7e88d9b8d9a532da78c7d2788c843090650e5b3
  habitat_source_registry_blob: d6a54cd7f5333455de6e6b23f4f9beacda4761c4
  source_role_architecture_blob: 702515cf920f811305f04598453322b28ba20d48
  cross_domain_source_role_architecture_blob: 89da72168d6165c744ebb4970ba45c80940ce746
  source_descriptor_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  habitat_source_role_policy_blob: b91935af6b998d497c6048525ee18ab6047e5a0e
  habitat_source_role_authority_policy_blob: f98e75b16295f3eca3fc8bc2d5696a09e09a2d3c
  critical_habitat_source_role_validator_blob: 0e1c859b493f9c485885a1e4ae66ff60bf376a6d
  critical_habitat_source_role_tests_blob: 3fb512a9812affb8caec9750fc29cd749f82cddf
  habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
inspection_boundary:
  - "Repository source reads only; no validators, tests, policy, CI, runtime, release, or publication workflows were executed."
  - "No source, descriptor, authority, rights record, EvidenceBundle, model receipt, release candidate, or public artifact was admitted, promoted, or published by this refresh."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR — Habitat Source Roles

> Habitat products must preserve the role of every admitted source through normalization, modeling, cataloging, release, and public presentation. A source role is not inferred from topic, provider, filename, map style, or downstream use.

![status](https://img.shields.io/badge/status-PROPOSED-yellow?style=flat-square)
![domain](https://img.shields.io/badge/domain-habitat-2ea44f?style=flat-square)
![decision](https://img.shields.io/badge/decision-source--role%20preservation-blue?style=flat-square)
![policy](https://img.shields.io/badge/policy-scaffold-lightgrey?style=flat-square)
![validator](https://img.shields.io/badge/validator-fixture--only-lightgrey?style=flat-square)
![truth](https://img.shields.io/badge/truth-evidence--bounded-orange?style=flat-square)

> [!IMPORTANT]
> **Decision maturity is PROPOSED and the ADR identity remains unassigned.** Repository evidence confirms Habitat architecture and source-family guidance, proposed deny-by-default policy scaffolds, and a substantive fixture-only critical-habitat validator with focused tests. The fixture checks prove only synthetic separation of regulatory-designation and modeled-suitability lanes; they do not verify source admission, authority, rights, sensitivity, evidence, policy wiring, release, publication, or public-use readiness. This ADR therefore states intended obligations and acceptance conditions, not complete repository enforcement.

## Contents

1. [Status](#1-status)
2. [Context](#2-context)
3. [Decision](#3-decision)
4. [Habitat role assignments](#4-habitat-role-assignments)
5. [Authority and anti-collapse rules](#5-authority-and-anti-collapse-rules)
6. [Lifecycle and publication behavior](#6-lifecycle-and-publication-behavior)
7. [Repository responsibility boundaries](#7-repository-responsibility-boundaries)
8. [Consequences](#8-consequences)
9. [Implementation and enforcement status](#9-implementation-and-enforcement-status)
10. [Acceptance criteria](#10-acceptance-criteria)
11. [Validation plan](#11-validation-plan)
12. [Rollback and correction](#12-rollback-and-correction)
13. [Open questions](#13-open-questions)
14. [Evidence basis](#14-evidence-basis)

---

## 1. Status

| Field | Value |
|---|---|
| ADR identity | **Unassigned** — this is a slug-only scaffold in `docs/adr/INDEX.md`; `ADR-habitat-source-roles` is retained only as the stable path/scaffold identity |
| Decision status | **PROPOSED** |
| Scope | Habitat-domain source-role assignment, preservation, and release framing |
| Owning responsibility root | `docs/adr/` — architecture decision record |
| Primary domain reference | `docs/domains/habitat/ARCHITECTURE.md` |
| Enforcement maturity | **PROPOSED / incomplete** — fixture-only validation exists; runtime, CI, and release wiring are not asserted |
| Source-admission state | **No admitted Habitat source descriptor is verified by this ADR refresh** |
| Publication effect | Fail closed when role, authority, rights, sensitivity, provenance, or required receipts are unresolved |
| Supersedes | The prior v1.0 scaffold at this same path |

This ADR becomes accepted only after the acceptance criteria in §10 are satisfied and the required owners approve it.

[Back to top](#top)

---

## 2. Context

Habitat combines source families that can describe similar places while carrying materially different relationships to truth. Examples include:

- federal or state designations with legal or administrative force;
- remotely sensed inventories and survey observations;
- modeled vegetation, ecological-system, suitability, and connectivity products;
- aggregate summaries;
- candidate records awaiting review; and
- synthetic representations.

Without an explicit role decision, a system can accidentally present modeled suitability as observed habitat, administrative context as regulatory authority, or a regulatory designation as a general ecological observation. This is a source-role collapse defect.

The seven historical guidance labels remain useful for human review:

`observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`

They are **not** the repository's sole current machine vocabulary. The proposed `SourceDescriptor` schema exposes 16 role tokens, while cross-domain transition guidance separately uses a seven-value uppercase profile. No accepted global crosswalk reconciles those vocabularies. This ADR neither selects a canonical vocabulary nor maps between them; an admitted descriptor and its governing contract must control any concrete source decision.

The role belongs to the admitted source or product, not merely to the provider or subject matter. One provider may publish multiple products that require separate descriptors and separate roles.

The Habitat architecture also establishes a key ownership boundary: Habitat does not own taxonomic identity, species-occurrence truth, conservation status, or rare-species sensitivity defaults. Those remain in the Fauna and Flora lanes and may enter Habitat only through governed, public-safe joins.

[Back to top](#top)

---

## 3. Decision

If this ADR is accepted, KFM will apply the following decision for the Habitat domain. Until then, this is proposed guidance only; no role assignment, descriptor, policy result, release decision, or public representation is created by this document refresh.

1. **Every admitted Habitat source or independently versioned product MUST have one explicit source role under its verified governing contract.**
2. **The role MUST be recorded on the admitted `SourceDescriptor` or its verified successor contract.**
3. **The role MUST remain traceable through every derived artifact, EvidenceBundle, model receipt, catalog record, release candidate, and published derivative that depends on that source.**
4. **A role MUST NOT be silently changed in place.** A correction creates a new descriptor or corrected version, records the reason, preserves lineage, and identifies affected downstream artifacts.
5. **Provider identity MUST NOT substitute for product-level role classification.** A provider that publishes designations and observations requires separate descriptors where those products have different roles.
6. **Derived Habitat products MUST disclose the roles of their contributing sources.** A derived product does not erase or upgrade the authority of its inputs.
7. **Release MUST fail closed** when the role is missing, incompatible with the release framing, unsupported by required authority or model receipts, or unresolved after policy evaluation.
8. **Public clients MUST receive role-aware released representations through governed interfaces.** They must not infer role from canonical/internal stores or bypass release policy.

The decision preserves the broader KFM invariant that EvidenceBundle outranks generated language. Generated summaries may explain a source role, but they cannot assign, promote, or override it.

[Back to top](#top)

---

## 4. Habitat role assignments

The assignments below are proposed decision guidance grounded in current Habitat source-family documents. They are **not admitted source assignments** and remain **PROPOSED at the concrete product level** until verified against admitted descriptors, rights records, review state, and the governing role vocabulary. The role terms retain their historical guidance meaning here; they must not be treated as a silent crosswalk to the current 16-token schema.

| Source family or product | Expected role | Decision rule |
|---|---|---|
| USFWS ECOS critical-habitat designation | `regulatory` | It is a federal designation. It must not be represented as modeled suitability or an observed occurrence. The descriptor must identify the authority and designation product. |
| KDWP state designation or legally operative list | `regulatory` | Apply only to the specific designation product carrying authority. |
| KDWP survey or field-observation product | `observed` | Use a separate descriptor from regulatory products. Sensitive locations remain subject to policy and geoprivacy controls. |
| NLCD land-cover product | `observed` **PROPOSED** | Treat as a remotely sensed classification product while preserving product vintage, method, and classification uncertainty. Final disposition requires steward review because classification products may combine observations and modeling. |
| NWI wetlands inventory | `observed` **PROPOSED** | Preserve inventory vintage and Cowardin classification. Do not convert inventory status into regulatory jurisdiction or legal determination. |
| GAP / LANDFIRE vegetation or ecological-system surface | `modeled` | Require model/product identity, version, input provenance, and uncertainty support appropriate to release significance. |
| Habitat suitability surface | `modeled` | Require a model-run receipt, input EvidenceRefs, uncertainty, time support, and explicit model framing. |
| Connectivity or corridor candidate generated by analysis | `modeled` or `candidate` | `modeled` when it is an approved model output; `candidate` while awaiting validation or steward review. It is never regulatory merely because it informs conservation planning. |
| PAD-US stewardship or ownership-context compilation | `administrative` **PROPOSED** | It provides stewardship/administrative context and does not itself establish observed habitat condition. |
| County, watershed, or statewide habitat summary | `aggregate` | Preserve the aggregation unit, method, time range, and receipt. Never expose it as a parcel- or site-level observation. |
| Unreviewed connector output or unresolved crosswalk | `candidate` | Must remain in WORK or QUARANTINE until validation, evidence resolution, rights review, and promotion. |
| AI-generated habitat narrative or reconstructed scene | `synthetic` | Must retain representation labeling and evidence links; it must never be represented as observed habitat. |

> [!CAUTION]
> **Regulatory critical habitat is not ecological suitability.** A designation may overlap a suitability surface, but neither may inherit the other's role or authority. Any combined view must preserve both source identities, both roles, and the distinction between legal designation and modeled ecological inference.

[Back to top](#top)

---

## 5. Authority and anti-collapse rules

The following rules are normative for this ADR:

### 5.1 Role is product-specific

A single institution may act as regulator, observer, administrator, or model publisher across different products. Role assignment is made at the admitted product/version boundary.

### 5.2 Regulatory authority requires an authority reference

A Habitat source labeled `regulatory` must identify the issuing authority and the exact designation, rule, list, or administrative act that gives the product force. A familiar agency name alone is insufficient.

### 5.3 Modeled products require model disclosure

A source or derivative labeled `modeled` must identify the model or product version and provide required provenance and uncertainty support. Missing uncertainty or model identity is a release blocker where the product's significance requires them.

### 5.4 Aggregate products cannot regain lost precision

A county, watershed, or statewide summary cannot be treated as a site-level observation. Downstream joins must retain the aggregation unit and avoid false precision.

### 5.5 Candidate and synthetic products cannot self-promote

A candidate becomes releasable only through governed validation and promotion. Synthetic content remains synthetic even when reviewed or published; review may approve its use but does not convert it into observation.

### 5.6 Joins preserve all contributing roles

A Habitat product combining land cover, modeled suitability, regulatory designations, and public-safe occurrence context must preserve the role and provenance of each contribution. The combined artifact may have its own derived-product classification, but it must not collapse input roles into a single unsupported authority claim.

[Back to top](#top)

---

## 6. Lifecycle and publication behavior

Source-role handling follows the governed lifecycle:

`RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`

| Stage | Required behavior |
|---|---|
| RAW | Preserve the source payload or resolvable reference, capture identity and acquisition metadata, and avoid interpretive relabeling. |
| WORK | Assign or verify the product-level role, rights, sensitivity, cadence, authority/model fields, and source identity. |
| QUARANTINE | Hold records with missing or conflicting role, rights, authority, provenance, or sensitivity information. Record reason codes and structured exit conditions. |
| PROCESSED | Preserve the admitted role and provenance in normalized objects and transformations. |
| CATALOG / TRIPLET | Resolve role-bearing EvidenceRefs to EvidenceBundles and record contribution relationships without authority inflation. |
| RELEASE CANDIDATE | Run schema, semantic, policy, source-role, sensitivity, rights, provenance, and publication-framing checks. |
| PUBLISHED | Expose only approved, role-aware, public-safe derivatives through governed interfaces with correction and rollback targets. |

Promotion is a governed state transition, not a file move. A file appearing under a later lifecycle root is not sufficient proof of promotion or publication.

[Back to top](#top)

---

## 7. Repository responsibility boundaries

Directory Rules place this ADR under `docs/adr/` because it records an architecture decision. The decision does not move executable or authoritative material into documentation.

| Responsibility | Expected root | Role in this decision |
|---|---|---|
| Architecture decision | `docs/adr/` | This document; rationale, consequences, acceptance, and rollback. |
| Habitat domain explanation | `docs/domains/habitat/` | Domain guidance, source-family dossiers, registry explanation, and cross-links. |
| Semantic contract | `contracts/` | Meaning and invariants of source descriptors and related objects. |
| Machine shape | `schemas/` | JSON Schema or equivalent validation shapes. |
| Admissibility and release policy | `policy/` | Deny/allow/abstain logic and reason codes. |
| Executable validation | `tools/`, `packages/`, or another verified implementation root | Validators and shared enforcement code. |
| Test evidence | `tests/` and `fixtures/` | Positive, negative, boundary, and regression proof. |
| Canonical source registry | Verified `data/registry/` path | Admitted role-bearing source descriptors; exact canonical path remains subject to repository contract verification. |
| Release decision | `release/` | Promotion decision, release manifest, approvals, rollback target, and receipts. |

No parallel schema, contract, policy, registry, proof, or release home should be created to implement this ADR without an accepted migration decision.

[Back to top](#top)

---

## 8. Consequences

### Positive

- Habitat products remain honest about whether they are observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic.
- Regulatory designations cannot be silently inflated into ecological observations, and model outputs cannot be presented as legal authority.
- Evidence drawers, APIs, maps, and AI responses can explain why a product has a particular role and what that role permits.
- Corrections can identify affected derivatives and releases because source identity and role remain traceable.
- Cross-domain joins with Fauna, Flora, Hydrology, Soil, Hazards, and land-management context remain inspectable.

### Costs and tradeoffs

- Providers that publish multiple product types require multiple descriptors and more detailed admission work.
- Some existing Habitat documentation may contain assignments that require steward review or correction.
- Model, authority, aggregation, and representation receipts add implementation and validation work.
- Fail-closed behavior may delay publication when metadata or rights are incomplete.

These costs are intentional. They prevent a polished map or narrative from outranking source authority, evidence, and release state.

[Back to top](#top)

---

## 9. Implementation and enforcement status

The following status is verified against repository evidence from this session:

| Artifact | Status | Evidence-bounded interpretation |
|---|---|---|
| `docs/domains/habitat/ARCHITECTURE.md` | **CONFIRMED present** | Defines Habitat scope, non-ownership boundaries, source families, lifecycle, and proposed repository shape. Its implementation claims are explicitly bounded. |
| `docs/domains/habitat/SOURCE_FAMILIES.md` | **CONFIRMED present** | Provides detailed proposed source-family role guidance and states that admitted descriptors outrank the documentation. |
| `docs/architecture/source-role-anti-collapse.md` | **CONFIRMED present** | Documents the current boundary: the former seven-role guidance is not the sole machine vocabulary; `SourceDescriptor` currently has 16 role tokens and the transition profile is a separate seven-value vocabulary. |
| `docs/architecture/cross-domain/source-role-anti-collapse.md` | **CONFIRMED present** | States that no accepted global crosswalk reconciles the descriptor tokens and transition profile. |
| `schemas/contracts/v1/source/source_descriptor.schema.json` | **CONFIRMED present; PROPOSED** | Declares a 16-token `source_role` enum and related authority, rights, sensitivity, and provenance shape. Its path/projection assertions are not resolved by this ADR. |
| `policy/domains/habitat/source_role.rego` | **CONFIRMED present; PROPOSED scaffold** | Contains a generated package and `default allow := false`; no verified role-evaluation rules were found in the file. |
| `policy/domains/habitat/source_role_authority.rego` | **CONFIRMED present; PROPOSED scaffold** | Contains a generated package and `default allow := false`; no verified authority-evaluation rules were found in the file. |
| `tools/validators/domains/habitat/validate_critical_habitat_source_role.py` | **CONFIRMED present; fixture-only executable** | Validates synthetic `PROPOSED_INACTIVE` candidates that keep regulatory critical-habitat and modeled-suitability source/claim lanes separate; a pass expressly denies admission, release, publication, and public-use conclusions. |
| `tests/domains/habitat/test_critical_habitat_source_role.py` | **CONFIRMED present; not executed in this refresh** | Contains focused positive and negative fixtures for the synthetic lane-separation validator. Presence is not CI or runtime proof. |
| Runtime wiring, CI enforcement, admitted descriptors, release resolver | **UNKNOWN / NEEDS VERIFICATION** | Not established by source reads in this refresh; no workflow or test execution was performed. |

Therefore, current behavior must not be described as "the repository enforces this ADR." The defensible statement is that proposed documentation and policy scaffolds exist alongside a narrow, fixture-only validator/test profile, while complete enforceability remains to be implemented and verified.

[Back to top](#top)

---

## 10. Acceptance criteria

This ADR may move from **PROPOSED** to **ACCEPTED** only when all applicable items are satisfied:

- [ ] Habitat and source-governance owners are assigned and approve the decision.
- [ ] The canonical `SourceDescriptor` semantic contract and schema are accepted, including either one governing role vocabulary or an explicit, approved crosswalk between descriptor tokens and transition-profile guidance.
- [ ] Product-level role assignment rules are documented for core Habitat source families.
- [ ] Regulatory products require an authority reference and fail closed without one.
- [ ] Modeled products require model identity, provenance, and uncertainty support appropriate to significance.
- [ ] Aggregate products retain aggregation unit and method.
- [ ] Candidate and synthetic products cannot be published under observed, regulatory, or administrative framing.
- [ ] Habitat source-role policy contains executable rules rather than scaffolds.
- [ ] The existing fixture-only critical-habitat lane-separation validator is retained or superseded by an approved executable validation scope; its pass conditions remain non-admission and non-release proof.
- [ ] Positive, negative, boundary, and regression fixtures exist for the approved scope.
- [ ] CI or an equivalent governed validation path executes the relevant tests and records the applicable scope.
- [ ] Release candidates include role-aware receipts and fail closed on unresolved role conflicts.
- [ ] Public API and map surfaces preserve role labels and do not bypass the governed release path.
- [ ] Correction and rollback procedures identify downstream artifacts affected by a role correction.

[Back to top](#top)

---

## 11. Validation plan

Minimum validation should include:

1. **Schema tests**
   - accept each valid role;
   - reject missing or unknown roles;
   - enforce conditional authority, model, aggregation, and representation fields.

2. **Policy tests**
   - deny modeled suitability framed as regulatory critical habitat;
   - deny regulatory designation framed as observation;
   - deny aggregate data projected as site-level observation;
   - deny candidate or synthetic content framed as observed reality;
   - deny a regulatory role without verified authority support;
   - abstain or quarantine when required evidence cannot be resolved.

3. **Transformation tests**
   - prove the role survives normalization, joins, catalog projection, and release packaging;
   - prove derived products retain references to all contributing source roles.

4. **Public-surface tests**
   - verify the governed API exposes role and evidence information appropriate to the caller;
   - verify the UI distinguishes regulatory, observed, modeled, aggregate, candidate, and synthetic content without relying only on color;
   - verify restricted source details do not leak through evidence presentation.

5. **Correction tests**
   - correct a misclassified source through a new descriptor/version;
   - identify impacted catalog objects and releases;
   - issue correction and rollback artifacts without rewriting historical receipts.

[Back to top](#top)

---

## 12. Rollback and correction

### ADR rollback

Because this v1.1 change is documentation-only, rollback is a reversion of this file to prior blob `ed836f8440051eb7bdca675e4cb4eca1e645171e` or an equivalent reviewed correction. Reverting the ADR does not automatically remove schemas, policy, validators, descriptors, receipts, or releases created under it; those require their own governed rollback decisions. This refresh creates none of those artifacts.

### Source-role correction

When a role assignment is wrong:

1. preserve the original descriptor and receipt history;
2. create a corrected descriptor or version with a stable relationship to the superseded record;
3. record the correction reason, reviewer, effective time, and affected artifacts;
4. re-run policy and release validation;
5. issue a correction notice and rollback or supersede affected published derivatives where required; and
6. keep public clients on governed interfaces throughout the correction.

A role correction must never be implemented by silently editing provenance history or relabeling a published layer without a receipt.

[Back to top](#top)

---

## 13. Open questions

| ID | Question | Status |
|---|---|---|
| HAB-SR-01 | Which accepted contract and canonical path govern the role-bearing `SourceDescriptor` used by executable code, given the present schema projection/path conflict? | **NEEDS VERIFICATION** |
| HAB-SR-02 | What approved crosswalk, if any, reconciles the proposed 16-token descriptor vocabulary with seven-role historical/transition guidance? | **NEEDS ARCHITECTURE DECISION** |
| HAB-SR-03 | Should remotely sensed classification products such as NLCD and NWI be represented under the approved product-specific interpretation once the governing vocabulary is accepted? | **NEEDS DOMAIN REVIEW** |
| HAB-SR-04 | Which exact Habitat source descriptors have been admitted, reviewed for rights, and assigned roles? | **UNKNOWN** |
| HAB-SR-05 | Which reason-code registry is canonical for Habitat source-role denial and abstention outcomes? | **NEEDS VERIFICATION** |
| HAB-SR-06 | Is the Habitat source-role policy wired into promotion and release CI? | **UNKNOWN** |
| HAB-SR-07 | Which public API and UI fields expose source role and evidence without leaking sensitive source details? | **NEEDS VERIFICATION** |
| HAB-SR-08 | Who owns final disposition of cross-domain role disagreements involving Habitat, Fauna, Flora, and external regulatory authorities? | **PROPOSED: joint steward review** |

[Back to top](#top)

---

## 14. Evidence basis

### CONFIRMED in this session

- This ADR path existed as a short proposed scaffold.
- `docs/domains/habitat/ARCHITECTURE.md` exists and defines Habitat as a context lane with explicit non-ownership of species truth and regulatory authority.
- `docs/domains/habitat/SOURCE_FAMILIES.md` exists and documents proposed role assignments for core Habitat source families.
- `docs/architecture/source-role-anti-collapse.md` and its cross-domain counterpart exist and document the unresolved boundary between the proposed 16-token `SourceDescriptor` vocabulary and separate seven-role guidance/profile.
- `schemas/contracts/v1/source/source_descriptor.schema.json` exists as a proposed 16-token source-role schema; this ADR does not resolve its canonical-path/projection assertions.
- `policy/domains/habitat/source_role.rego` and `policy/domains/habitat/source_role_authority.rego` exist as deny-by-default proposed scaffolds.
- `tools/validators/domains/habitat/validate_critical_habitat_source_role.py` and its focused test module exist as fixture-only, synthetic lane-separation evidence; neither was executed by this refresh and neither proves admission, release, publication, or public use.
- `docs/doctrine/directory-rules.md` places ADRs and domain documentation under responsibility-based roots and separates docs, contracts, schemas, policy, tests, data, and release authority.

### PROPOSED by this ADR

- The complete Habitat decision, normative rules, acceptance criteria, validation plan, and correction workflow.
- Concrete role assignments until verified against admitted product-level descriptors and steward review.
- The exact integration points for policy, CI, release resolution, public API, and UI.

### UNKNOWN or needs verification

- Runtime policy wiring.
- CI execution and passing tests.
- Canonical admitted Habitat descriptors and their review state.
- An accepted role-vocabulary crosswalk, if one is required.
- Rights status for individual source families.
- Release manifests and public products currently governed by these rules.

---

## 15. Revision history

| Version | Date | Change | Governance effect |
|---|---|---|---|
| v1.0 | 2026-07-24 | Initial proposed scaffold. | No source admission, release, or publication effect. |
| v1.1 | 2026-09-14 | Currentness-only reconciliation: marks the ADR identity unassigned, distinguishes seven-role guidance from the 16-token proposed descriptor vocabulary, and corrects policy/validator evidence. | No source admission, role assignment, policy activation, CI execution, release, deployment, or publication effect. |

[Back to top](#top)

---

**Decision posture:** preserve role, cite evidence, fail closed on ambiguity, and never let a derived Habitat product inherit authority its sources do not possess.
