<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-source-role-readme
title: Tests — Geology Source Role
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <source-steward> + <evidence-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - docs/domains/geology/SOURCE_REGISTRY.md
  - docs/domains/geology/SOURCES.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - data/registry/sources/geology/README.md
  - data/proofs/geology/README.md
  - data/catalog/domain/geology/README.md
  - tests/domains/geology/claim-class/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/governed-ai/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - source-role
  - source-descriptor
  - anti-collapse
  - observed
  - regulatory
  - modeled
  - aggregate
  - administrative
  - candidate
  - synthetic
  - fail-closed
notes:
  - "This README governs the source-role test lane under tests/domains/geology/source_role/."
  - "It documents intended Geology source-role test coverage; it does not claim that all tests already exist."
  - "Source role is fixed at admission by SourceDescriptor and must not be upgraded, downcast, relabeled, hidden, or inferred from generated text."
  - "This lane is distinct from claim-class tests: source_role describes source support; claim-class describes the geology claim being made."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Source Role

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Fsource__role-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-role--preserving-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Geology-domain test lane for source-role discipline. It proves that Geology sources keep their admitted role through normalization, validation, catalog closure, release, rollback, public map surfaces, Evidence Drawer payloads, and governed AI answers.

---

## 1. Placement and authority

`tests/domains/geology/source_role/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove source-role rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/geology/` |
| Test lane | `source_role/` |
| Primary matrix | `docs/domains/geology/SOURCE_ROLE_MATRIX.md` |
| Primary runbook | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` |
| Source registry lane | `data/registry/sources/geology/` |
| Fixture counterpart | `fixtures/domains/geology/` |
| Adjacent claim-class lane | `tests/domains/geology/claim-class/` |
| Adjacent catalog lane | `tests/domains/geology/catalog-closure/` |
| Adjacent AI lane | `tests/domains/geology/governed-ai/` |
| Current implementation status | README path exists; executable tests, fixtures, validators, registry records, and CI wiring remain `UNKNOWN` until verified. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. This lane tests source-role preservation; it must not become a source registry, descriptor store, schema home, policy home, proof store, catalog store, release authority, fixture home, or implementation package.

---

## 2. Source role vs. claim class

This lane intentionally tests **source role**, not claim class.

| Concept | Meaning | Example |
|---|---|---|
| Source role | What kind of support a source record provides. | `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic`. |
| Claim class | What kind of geology assertion is being made. | Unit, observation, estimate, permit/context, production/context, or release claim. |

A regulatory record can support a regulatory/context claim without becoming an observed geology measurement. A modeled record can support an interpreted product without becoming direct observation. An aggregate record can support summary context without becoming per-place truth.

---

## 3. Role vocabulary under test

The seven source roles below are the vocabulary this lane should enforce.

| Role | Safe meaning | Must not become |
|---|---|---|
| `observed` | Direct reading or first-hand record tied to place/time. | Modeled certainty, legal authority, aggregate summary. |
| `regulatory` | Governing-body determination or filing context. | Observed event or physical measurement. |
| `modeled` | Derived from inputs, assumptions, and method; uncertainty preserved. | Observed truth or source-native measurement. |
| `aggregate` | Summary over a unit where per-record fidelity is lost. | Per-place or per-feature observation. |
| `administrative` | Agency compilation, accounting, registry, or index context. | Direct observed truth or legal/resource conclusion. |
| `candidate` | Intake or review-pending material. | Public, regulatory, observed, or released truth. |
| `synthetic` | Simulated, reconstructed, generated, or AI-derived representation. | Observed reality or evidence source. |

---

## 4. What this lane must prove

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Admission fixation | Source role is set in SourceDescriptor at admission and remains attached downstream. | `SOURCE_ROLE_MISSING` or hold. |
| No role upcast | Processing cannot upgrade modeled to observed, aggregate to per-place, candidate to regulatory, or synthetic to observed. | `ROLE_UPCAST_FORBIDDEN` or fail. |
| No role hiding | Records cannot hide role by dropping the field or relabeling as generic context. | `ROLE_MISSING_AFTER_TRANSFORM` or fail. |
| Role-conditional receipts | Modeled, aggregate, synthetic, or transformed records carry required receipt/reference when the matrix requires it. | `MISSING_ROLE_RECEIPT` or hold. |
| Matrix-cell semantics | Source family, source role, claim family, and geometry scope remain compatible. | `MATRIX_CELL_VIOLATION` or deny. |
| Join behavior | Joins preserve the most restrictive/source-role-aware semantics and do not create stronger claims. | `JOIN_ROLE_COLLAPSE` or hold. |
| Catalog closure | Catalog and triplet records preserve source_role and EvidenceBundle linkage. | Hold at PROCESSED/CATALOG. |
| Public surfaces | API/map/drawer/AI outputs retain role qualifiers and do not strengthen claims. | `SUMMARY_OVERCLAIM`, deny, or abstain. |
| Candidate boundary | Candidate material cannot reach public surfaces. | `CANDIDATE_PUBLIC_DENIED` or hold. |
| AI guard | AI-generated text cannot become evidence and cannot relabel source roles. | `AI_TEXT_AS_EVIDENCE` or abstain. |

---

## 5. Expected test families

This folder should eventually contain narrow role-preservation tests.

```text
tests/domains/geology/source_role/
├── README.md
├── test_source_role_required.py             # PROPOSED
├── test_role_fixed_at_admission.py          # PROPOSED
├── test_role_upcast_forbidden.py            # PROPOSED
├── test_role_not_dropped.py                 # PROPOSED
├── test_role_conditional_receipts.py        # PROPOSED
├── test_matrix_cell_semantics.py            # PROPOSED
├── test_join_role_preservation.py           # PROPOSED
├── test_catalog_triplet_role_support.py     # PROPOSED
├── test_public_surface_role_qualifiers.py   # PROPOSED
├── test_candidate_not_public.py             # PROPOSED
├── test_ai_text_not_evidence.py             # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

This requested directory already uses underscore form (`source_role/`), which is suitable for Python-oriented test discovery.

---

## 6. Fixture expectations

Tests in this lane should be no-network by default. They should use synthetic SourceDescriptor, EvidenceBundle, catalog, triplet, public-surface, and AI-answer fixtures.

Recommended fixture groups:

```text
fixtures/domains/geology/source_role/
├── valid/
│   ├── observed_source_descriptor.json
│   ├── modeled_claim_with_receipt.json
│   ├── aggregate_summary_with_receipt.json
│   ├── regulatory_context_record.json
│   ├── administrative_index_context.json
│   └── candidate_held_in_work.json
├── invalid/
│   ├── source_role_missing.json
│   ├── modeled_labeled_observed.json
│   ├── aggregate_labeled_per_place.json
│   ├── candidate_labeled_regulatory.json
│   ├── synthetic_labeled_observed.json
│   ├── role_dropped_after_transform.json
│   ├── join_creates_stronger_role.json
│   ├── catalog_record_missing_role.json
│   ├── public_summary_drops_role_qualifier.json
│   └── ai_text_used_as_evidence.json
└── golden/
    ├── geology_source_role_minimal.json
    └── geology_source_role_negative_outcomes.json
```

Fixture rules:

- Use synthetic examples unless a public-safe, rights-reviewed fixture is intentionally included.
- Do not include restricted real-world coordinates, private operational details, credentials, source payloads, or live service responses.
- Invalid fixtures should fail for one primary source-role reason where practical.
- Golden fixtures should make SourceDescriptor role, permitted claims, forbidden claims, evidence linkage, policy state, and output qualifiers easy to inspect.

---

## 7. Collapse pairs this lane must deny

The following source-role collapses should be represented in tests.

| Collapse | Why it fails |
|---|---|
| `aggregate -> observed` | Aggregate summaries lose per-record fidelity and cannot be read as per-place truth. |
| `modeled -> observed` | Model outputs carry assumptions and uncertainty; they cannot be relabeled as observation. |
| `regulatory -> observed` | Regulatory/filing/permit context does not prove a physical observed event. |
| `administrative -> observed` | Administrative compilations and indexes are not first-hand observations by default. |
| `candidate -> public` | Candidate material is review-pending and has no public edge. |
| `synthetic -> observed` | Generated or simulated material is not observed reality. |
| `AI text -> evidence` | Generated language is downstream interpretation, not a source or EvidenceBundle. |

---

## 8. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `GEOL-ROLE-001` | Valid observed source passes. | SourceDescriptor with `source_role = observed` supporting an allowed observed claim. | Validation passes. |
| `GEOL-ROLE-002` | Missing source role fails. | SourceDescriptor or catalog candidate lacks `source_role`. | Hold or fail. |
| `GEOL-ROLE-003` | Modeled cannot become observed. | Modeled source or model-derived artifact is labeled observed. | Fail closed. |
| `GEOL-ROLE-004` | Aggregate cannot become per-place. | Aggregate summary is joined to a single feature as observed truth. | Fail closed. |
| `GEOL-ROLE-005` | Candidate cannot publish. | Candidate fixture reaches public map/API/drawer/AI payload. | Deny or hold. |
| `GEOL-ROLE-006` | Synthetic cannot become evidence. | Synthetic/AI-derived text is used as evidence support. | Abstain or fail. |
| `GEOL-ROLE-007` | Role receipt required. | Modeled or aggregate role lacks required receipt/reference. | Hold or fail. |
| `GEOL-ROLE-008` | Role persists through catalog. | Catalog/triplet fixture drops or changes source role. | Hold or fail. |
| `GEOL-ROLE-009` | Public summary keeps qualifier. | Public label or AI answer omits role qualifier and strengthens the claim. | Fail or abstain. |
| `GEOL-ROLE-010` | Join preserves restrictive role. | Joined evidence carries multiple roles; output chooses stronger unsupported role. | Fail closed. |

---

## 9. Surfaces under test

| Surface | What the test should verify |
|---|---|
| SourceDescriptor | Role exists, is allowed for source family, and carries role-conditional fields where needed. |
| Validation report | Role failures emit finite reason codes. |
| Catalog record | Role is preserved with EvidenceBundle and CatalogMatrix linkage. |
| Triplet/graph edge | Role travels with derivative graph facts and does not become root truth. |
| Public API/map payload | Role qualifier is visible or recoverable; public output is not stronger than evidence. |
| Evidence Drawer | Role is displayed with citation and policy context. |
| Governed AI | AI answer cites evidence and role, or abstains. |
| Rollback/correction | Corrected releases cannot keep stale role-collapsed derivatives current. |

---

## 10. Non-goals

This folder must not:

- store SourceDescriptor records, source payloads, fixtures, proofs, receipts, catalog records, releases, schemas, policies, or package code;
- call live source APIs, map services, model services, or LLMs by default;
- decide claim class, resource truth, reserve status, legal/property meaning, hazard risk, or engineering conclusions;
- infer source role from generated language, layer name, map symbol, or folder path alone;
- expose restricted details or sensitive locations;
- silently promote candidate, modeled, aggregate, administrative, regulatory, or synthetic material into stronger roles; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, missing role, missing receipt, or role collapse into a passing response.

---

## 11. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] SourceDescriptor role is explicit.
- [ ] Role and claim class are tested separately.
- [ ] Role-conditional receipts/references are represented where needed.
- [ ] Joins preserve restrictive role semantics.
- [ ] Catalog/triplet/public-surface fixtures keep role qualifiers.
- [ ] AI output cannot become evidence or relabel roles.
- [ ] Failure emits finite reason codes rather than silent success.

---

## 12. Current implementation note

This lane is documentation-first. The target README existed as an empty placeholder before this update. The Geology promotion runbook states source role is fixed at admission and identifies a proposed source-role validator. The Source Role Matrix documents the seven roles, matrix-cell semantics, and fail-closed collapse pairs. This README does not prove that executable source-role tests, fixtures, validators, registry records, or CI wiring already exist.

---

## 13. Definition of done

This README becomes implementation-backed when:

- at least the `GEOL-ROLE-001` through `GEOL-ROLE-010` scenarios exist as executable tests;
- fixtures exist under the repository's approved Geology fixture home and contain no restricted real-world details;
- tests validate SourceDescriptor role, permitted/forbidden claims, role-conditional receipts, and matrix-cell semantics;
- catalog, triplet, public API/map, Evidence Drawer, governed AI, correction, and rollback fixtures prove role preservation;
- source-role failures emit bounded reason codes; and
- CI runs this lane without network access or live model calls by default.
