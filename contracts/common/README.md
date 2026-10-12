<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-common-readme
title: contracts/common/ — Shared Semantic Contract Family Index
type: readme; semantic-contract-index
version: v0.3
status: draft; repository-grounded; mixed-maturity; configured-schema-paired; no-policy-authority; no-release-authority
owners: OWNER_TBD — Contract steward · Schema steward · Validation steward · Policy steward · Affected-family stewards · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; common; shared-kernel; no-parallel-authority; no-release; no-publication
current_path: contracts/common/README.md
owning_root: contracts/
responsibility: index shared semantic meaning, invariants, exclusions, compatibility, and evidence boundaries without owning machine shape, admissibility, evidence, fixtures, tests, runtime, lifecycle, release, or publication
truth_posture: cite-or-abstain; file presence and bounded validation never establish semantic adoption, source authority, policy permission, review approval, release, or publication
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@0db0a76b3a825b6f47ee5a429a80752affda73d2
prior_blob: 1bf959b1f940996e70f1822a33e5839af384ff4e
authority_evidence: ADR-0029 adopts docs/doctrine/directory-rules.md as the writable human Directory Rules authority
notes:
  - "Same-path modernization of the existing README; no contract, schema, policy, fixture, validator, test, runtime, release, or data object is created by this edit."
  - "Current main contains 38 direct Markdown contract files plus this README. Every direct basename has a paired v1 common schema and fixture family in the inspected tree; pairing is presence evidence, not acceptance or production readiness."
  - "The common lane is mixed-maturity: 34 child statuses contain PROPOSED and 4 are draft-only. Child documents remain authoritative for their own status and semantics."
  - "No policy/common directory exists at the inspected main; policy/contract/ is the current Contract-policy documentation boundary and does not define common semantic meaning."
  - "Notion and Google Drive were consulted as coordination and proposal lineage only. GitHub repository evidence controls implementation classification."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/common/` — Shared Semantic Contract Family Index

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: semantic meaning](https://img.shields.io/badge/authority-semantic%20meaning-1f6feb?style=flat-square)](#authority-boundary)
[![Inventory: 38 contracts](https://img.shields.io/badge/inventory-38%20contracts-8250df?style=flat-square)](#direct-contract-inventory)
[![Policy: no common lane](https://img.shields.io/badge/policy-no%20common%20lane-6e7781?style=flat-square)](#policy-and-admissibility)

> **Purpose.** This directory is the shared-kernel lane for KFM semantic meanings that are genuinely cross-cutting. It documents what a reusable concept means, which invariants and exclusions bind it, and where its companion shape, fixtures, validators, policy, evidence, and release decisions live. It does not make any instance true, valid, admissible, reviewed, released, or public-safe.

`contracts/common/` is an index and responsibility boundary, not a data store or executable registry.

## Quick navigation

[Status](#status) · [Authority boundary](#authority-boundary) · [Path and repo fit](#path-and-repo-fit) · [Direct inventory](#direct-contract-inventory) · [Paired implementation surfaces](#paired-implementation-surfaces) · [Admission rules](#shared-kernel-admission-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Policy and admissibility](#policy-and-admissibility) · [Lifecycle and trust boundary](#lifecycle-and-trust-boundary) · [Validation](#validation) · [Evidence](#evidence-ledger) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

This README is grounded to [`main@0db0a76`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/0db0a76b3a825b6f47ee5a429a80752affda73d2), inspected on 2026-09-07.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `contracts/common/` direct inventory | **CONFIRMED** — 39 entries: this README plus 38 Markdown contracts | The directory is populated and navigable; presence does not establish adoption or maturity. |
| Child maturity | **CONFIRMED mixed** — 34 child statuses contain `PROPOSED`; 4 are `draft`-only | Most families remain proposed, inactive, fixture-first, assessment-only, or otherwise non-authoritative. Read each child contract for exact posture. |
| Paired machine shape | **CONFIRMED configured tree** — 38 same-basename JSON files under [`schemas/contracts/v1/common/`](../../schemas/contracts/v1/common/) plus its README and an `uncertainty/` child index | Shape files exist in the configured v1 surface; schema acceptance, registry authority, and production consumers remain separate questions. |
| Synthetic fixtures | **CONFIRMED tree** — 38 same-basename fixture directories under [`fixtures/contracts/v1/common/`](../../fixtures/contracts/v1/common/) plus its README | Fixtures exercise bounded cases; they are not source, evidence, policy, release, or publication authority. |
| Generic schema/fixture harness | **CONFIRMED** at [`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) | The harness is executable evidence for its discovered cases, not proof that every semantic invariant or current CI run passes. |
| Validator support | **CONFIRMED mixed** — 36 matching root-level validator entrypoints, one nested station-assignment validator, and no matching direct validator for `stale_state_supersession_assessment` | Validator presence is bounded implementation evidence; missing or indirect coverage must remain visible. |
| Policy pairing | **CONFIRMED boundary** — no `policy/common/` path was found; [`policy/contract/`](../../policy/contract/README.md) is README-only direct policy boundary | Do not copy policy references into this directory or infer an active common-policy evaluator. |
| Review, release, publication, and production parity | **UNKNOWN / not inferred** | A file, fixture, validator, workflow, or merged change does not prove stewardship, required review, source authority, release, deployment, or public exposure. |

### Truth labels

| Label | Use |
|---|---|
| `CONFIRMED` | Directly verified in the pinned repository tree or a cited bounded source. |
| `PROPOSED` | A candidate meaning, profile, or future adoption path; not current authority. |
| `UNKNOWN` | The inspected evidence cannot resolve the claim. |
| `NEEDS VERIFICATION` | Checkable but unresolved; do not use as a completed dependency. |
| `DENY` | The proposed use would collapse responsibility or bypass a trust boundary. |

---

## Authority boundary

`contracts/common/` may own:

- human-readable meaning, field intent, invariants, exclusions, compatibility semantics, and migration notes for a truly shared concept;
- links to the paired schema, fixture family, validator/test profile, policy boundary, and downstream consumers;
- explicit uncertainty, abstention, correction, supersession, and rollback semantics.

It must not own:

- JSON Schema, DTO shape, executable validators, fixtures, test code, policy rules, source registries, EvidenceBundles, lifecycle data, runtime behavior, release decisions, or published artifacts;
- domain vocabulary whose owner is clear;
- a second schema, policy, evidence, proof, receipt, release, or registry root;
- claims that a passed fixture or validator proves a real-world observation, source authority, rights posture, review approval, or public-safe exposure.

The parent [`contracts/` root](../README.md) owns semantic meaning. The responsibility split is documented in [`contract-schema-policy-split.md`](../../docs/architecture/contract-schema-policy-split.md) and constrained by the adopted [`Directory Rules`](../../docs/doctrine/directory-rules.md) and [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

| Question | Owning surface | Role of this directory |
|---|---|---|
| What does the object mean? | `contracts/common/` or the owning domain/family | **Owns** only when the concept is genuinely shared. |
| What machine shape is accepted? | `schemas/contracts/v1/` | Link and reconcile; never author shape here. |
| May an action or exposure proceed? | Singular `policy/` | Record the boundary; never decide from Markdown presence. |
| Which synthetic cases are exercised? | `fixtures/` | Link examples; never treat them as evidence. |
| Can a rule be enforced? | `tests/` and `tools/validators/` | Link bounded executable coverage; never overstate a pass. |
| What source or evidence is authoritative? | Source/evidence/proof roots | Defer to their accepted registers and admissibility. |
| What is released, corrected, or withdrawn? | `release/`, `data/receipts/`, `data/proofs/` | Do not create lifecycle or release records here. |

---

## Path and repo fit

```text
contracts/
├── README.md
└── common/
    ├── README.md                         # this index and boundary
    └── <shared-semantic-contract>.md    # 38 direct child contracts

schemas/contracts/v1/common/
├── README.md
├── <shared-semantic-contract>.schema.json
└── uncertainty/                          # child index lane; current files are not adoption proof

fixtures/contracts/v1/common/
├── README.md
└── <shared-semantic-contract>/            # synthetic, deterministic cases
```

The path is a semantic contract home. A requested shared concept that has a clear domain owner belongs under that domain's contract lane; a source/evidence/runtime/release concept belongs under its specialized family. Placement disputes require an accepted governance decision or reversible migration, not a convenience copy.

---

## Direct contract inventory

The following 38 child files are present at the pinned main. Links are relative to this README; the child file remains authoritative for its own status, version, owner, and semantics.

| Shared family | Direct semantic contracts |
|---|---|
| **Identity and integrity** | [`hash_binding_assessment`](hash_binding_assessment.md) · [`hash_profile_readiness_matrix`](hash_profile_readiness_matrix.md) · [`identifier_precision_lineage_assessment`](identifier_precision_lineage_assessment.md) · [`identity_token`](identity_token.md) · [`recursive_traversal_safety_assessment`](recursive_traversal_safety_assessment.md) · [`reversible_entity_reconciliation`](reversible_entity_reconciliation.md) · [`spec_hash`](spec_hash.md) · [`stale_state_supersession_assessment`](stale_state_supersession_assessment.md) |
| **Temporal semantics** | [`elapsed_time_unit_disclosure`](elapsed_time_unit_disclosure.md) · [`open_ended_temporal_semantics_disclosure`](open_ended_temporal_semantics_disclosure.md) · [`period_boundary_predicate_disclosure`](period_boundary_predicate_disclosure.md) · [`rolling_metric_window_disclosure`](rolling_metric_window_disclosure.md) · [`temporal_authority_envelope`](temporal_authority_envelope.md) · [`temporal_reference_integrity_assessment`](temporal_reference_integrity_assessment.md) · [`temporal_support_acceptance_assessment`](temporal_support_acceptance_assessment.md) · [`temporal_uniqueness_assessment`](temporal_uniqueness_assessment.md) · [`temporal_view_state`](temporal_view_state.md) · [`temporal_window`](temporal_window.md) |
| **Spatial and geography carriers** | [`admin_boundary_change`](admin_boundary_change.md) · [`geography_version`](geography_version.md) · [`spatial_geometry`](spatial_geometry.md) · [`spatial_model_family_assessment`](spatial_model_family_assessment.md) · [`station_spatial_assignment_assessment`](station_spatial_assignment_assessment.md) |
| **Aggregation, measurement, and quality** | [`aggregate_grouping_disclosure`](aggregate_grouping_disclosure.md) · [`aggregate_null_semantics_disclosure`](aggregate_null_semantics_disclosure.md) · [`aggregate_statistic`](aggregate_statistic.md) · [`analytical_query_cost_profile`](analytical_query_cost_profile.md) · [`conditions_source_role_readiness_matrix`](conditions_source_role_readiness_matrix.md) · [`distinct_null_deduplication_assessment`](distinct_null_deduplication_assessment.md) · [`measurement_support_reconciliation`](measurement_support_reconciliation.md) · [`missing_value_filter_receipt`](missing_value_filter_receipt.md) · [`source_native_quality_translation`](source_native_quality_translation.md) |
| **Condition and derived-product semantics** | [`advisory_event_envelope`](advisory_event_envelope.md) · [`classification_release`](classification_release.md) · [`condition_relation`](condition_relation.md) · [`forecast_product`](forecast_product.md) · [`modeled_surface`](modeled_surface.md) · [`outcome_projection_parity`](outcome_projection_parity.md) |

This index intentionally does not promote the inventory into a generated registry. New shared files require an owner rationale, paired-path review, fixture/test posture, and a reversible migration path if a more specific owner is later established.

---

## Paired implementation surfaces

| Surface | Current path/evidence | Boundary |
|---|---|---|
| Semantic contracts | `contracts/common/*.md` | Meaning, invariants, exclusions, compatibility, and navigation only. |
| Machine shape | [`schemas/contracts/v1/common/`](../../schemas/contracts/v1/common/) | 38 same-basename JSON schemas plus README and `uncertainty/` index; configured repository surface, not automatically accepted authority. |
| Synthetic examples | [`fixtures/contracts/v1/common/`](../../fixtures/contracts/v1/common/) | 38 same-basename fixture lanes; deterministic and public-safe only. |
| Generic schema tests | [`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) | Discovers bounded valid/invalid fixture cases across configured families. |
| Contract wiring tests | [`tests/contracts/`](../../tests/contracts/README.md) | Includes identity-token and runtime/evidence wiring checks; not complete semantic equivalence. |
| Focused validator tests | [`tests/validators/`](../../tests/validators/README.md) | Current tree contains focused tests for common validators, including spatial, temporal, and nested station-assignment profiles. |
| Validator implementation | [`tools/validators/`](../../tools/validators/README.md) | 36 matching root-level common entrypoints; station assignment is nested under `tools/validators/common/`; stale-state has no matching direct entrypoint verified here. |
| Admissibility | [`policy/contract/`](../../policy/contract/README.md) | README-only Contract-policy boundary; no `policy/common/` directory or active common-policy evaluator was verified. |

The paired tree is a compatibility surface, not a claim that every contract is accepted, complete, consumed, or release-ready. `schemas/contracts/v1/common/README.md` and `fixtures/contracts/v1/common/README.md` retain narrower local gaps and should be updated in their own changes rather than silently corrected by this index.

---

## Shared-kernel admission rules

A concept belongs here only when all of the following are true:

1. It is used by two or more contract families or governed subsystems.
2. No single domain or specialized family owns its meaning.
3. The shared definition is small, stable, and composable rather than a domain model in disguise.
4. Identity-bearing fields, invariants, source/evidence requirements, sensitivity implications, and compatibility behavior are explicit.
5. A paired schema, fixture/test posture, validator scope, and rollback target are linked or marked `NEEDS VERIFICATION`.

Prefer a specific owner over `common/` when ownership is clear. A shared field group is not automatically a shared contract: copying a field into several domains is a drift signal, not proof of common ownership.

Each child contract should answer:

- What does the concept mean, and what does it explicitly not mean?
- Why is it not owned by `source/`, `evidence/`, `runtime/`, `release/`, or a domain lane?
- Which fields carry identity, time, space, provenance, sensitivity, or compatibility state?
- Which source roles, EvidenceRefs, review states, rights, or policy gates are required?
- What schema, fixture, validator, test, consumer, migration, correction, and rollback paths apply?

---

## Anti-collapse rules

| Common concept | Must not be collapsed into |
|---|---|
| `identity_token` | An authentication credential, secret, consent token, or proof of identity by itself. |
| `spatial_geometry` | Survey accuracy, CRS transformation, geocoding, map-rendering instructions, or permission to expose sensitive coordinates. |
| `temporal_window` and temporal assessments | Currentness, forecast truth, observation truth, or release state without their owning evidence/source/policy support. |
| `modeled_surface` and `forecast_product` | An observation, field truth, classification, advisory action, or public guidance. |
| `classification_release` and `outcome_projection_parity` | A release decision, promotion receipt, or publication approval. |
| `geography_version` and `admin_boundary_change` | Legal boundary truth, geometry, identity equivalence, or an executed crosswalk that transfers observations. |
| Aggregation/quality assessments and receipts | Evidence of the underlying phenomenon, source authority, policy approval, or production health. |
| Fixture or validator `PASS` | Review approval, source admission, rights/consent, release, deployment, or public use. |

When a consumer needs a stronger claim, it must resolve the accepted source, evidence, policy, review, release, and correction surfaces rather than upgrading a common carrier.

---

## Policy and admissibility

There is no verified `policy/common/` directory at the pinned main. The current contract-change policy boundary is [`policy/contract/README.md`](../../policy/contract/README.md), under the singular `policy/` root. That document explicitly leaves semantic meaning to `contracts/`, machine shape to `schemas/contracts/v1/`, and bounded enforceability to fixtures/tests/validators.

Therefore:

- do not add policy rules, OPA/Rego, policy decisions, receipts, or evaluator output under `contracts/common/`;
- do not treat a child contract's historical `policy/common/` pointer as proof that that path exists or is active;
- route rights, sensitivity, source admission, access, and publication questions to accepted policy/evidence/release roots;
- keep policy changes separate from semantic meaning changes and record compatibility, review, and rollback impact.

---

## Lifecycle and trust boundary

| Stage | Owning surface | What this README can say |
|---|---|---|
| Meaning | `contracts/common/` | Define shared vocabulary and invariants. |
| Shape | `schemas/contracts/v1/common/` | Link the configured machine shape; do not imply acceptance. |
| Examples and enforcement | `fixtures/`, `tests/`, `tools/validators/` | Identify bounded cases and coverage gaps. |
| Source and evidence | `contracts/source/`, `contracts/evidence/`, accepted registries | Require references; never manufacture support. |
| Admissibility and sensitivity | `policy/`, evidence, review | Require a decision; never infer permission from presence. |
| Lifecycle, release, correction | `data/`, `release/`, proofs/receipts | Link records; never store or emit them here. |
| Runtime and publication | governed packages, APIs, UI, and published roots | Treat as downstream consumers, not contract authority. |

For a material change, preserve predecessor/successor identity, migration and deprecation semantics, consumer impact, correction behavior, and an immediate rollback target. A documentation update never moves data, activates a source, changes a policy default, promotes an artifact, releases a product, deploys code, or publishes a map/API/UI surface.

---

## Validation

Before adding or materially changing a child contract, verify:

- the concept is truly cross-cutting and has no better domain or specialized-family owner;
- the direct Markdown path, same-basename schema, fixture lane, validator, and focused tests are linked or each gap is labeled `NEEDS VERIFICATION`;
- the schema/fixture/test profile is deterministic and no-network where claimed;
- semantic-invalid, denied, abstain, unsupported, and correction cases are represented where applicable;
- source, evidence, policy, rights, sensitivity, review, release, and publication claims remain outside this directory;
- downstream consumers reference one shared contract instead of copying fields or redefining meaning;
- changes preserve compatibility, deprecation, migration, correction, and rollback semantics;
- current CI and hosted checks are actually read back before claiming validation success.

Useful bounded checks already present in the repository include [`test_common_contracts.py`](../../tests/schemas/test_common_contracts.py), [`test_identity_token_wiring.py`](../../tests/contracts/test_identity_token_wiring.py), [`test_validate_spatial_geometry.py`](../../tests/validators/test_validate_spatial_geometry.py), [`test_validate_temporal_window.py`](../../tests/validators/test_validate_temporal_window.py), and [`test_validate_station_spatial_assignment_assessment.py`](../../tests/validators/common/test_validate_station_spatial_assignment_assessment.py). These are evidence of test surfaces, not a blanket pass claim for current main.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| [`contracts/README.md`](../README.md) at pinned main | **CONFIRMED** | `contracts/` owns semantic meaning and must not become schema, policy, evidence, lifecycle, release, runtime, or publication authority. | Parent guidance does not certify every child family. |
| [`contract-schema-policy-split.md`](../../docs/architecture/contract-schema-policy-split.md) | **CONFIRMED** | Meaning/shape/admissibility/enforceability are separate responsibility concerns. | It does not make a proposed ADR or a child schema accepted. |
| [`Directory Rules v2`](../../docs/doctrine/directory-rules.md) and [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **CONFIRMED** | Adopted placement and no-parallel-authority discipline. | Acceptance does not prove owners, required reviews, or production parity. |
| [`contracts/common/` tree](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/0db0a76b3a825b6f47ee5a429a80752affda73d2/contracts/common) | **CONFIRMED** | 38 direct child contract files plus this README and their current child blobs. | Presence is not adoption or correctness. |
| [`schemas/contracts/v1/common/`](../../schemas/contracts/v1/common/) | **CONFIRMED configured surface** | 38 same-basename JSON schema files, README, and `uncertainty/` child index. | Schema registry status, steward acceptance, and consumer coverage remain unresolved. |
| [`fixtures/contracts/v1/common/`](../../fixtures/contracts/v1/common/) | **CONFIRMED synthetic surface** | 38 same-basename fixture lanes. | Fixture outcomes do not establish real-world truth, policy, release, or publication. |
| [`tests/schemas/test_common_contracts.py`](../../tests/schemas/test_common_contracts.py) and focused validator tests | **CONFIRMED bounded code paths** | Generic fixture discovery plus focused common-family checks. | No current hosted run or full semantic-equivalence claim is made here. |
| [`policy/contract/README.md`](../../policy/contract/README.md) | **CONFIRMED policy boundary** | Current Contract-policy documentation lane and its non-authority limits. | No `policy/common/` lane or active common-policy evaluator was verified. |
| [Notion: KFM Full Atlas Seed Cards](https://app.notion.com/p/7c05096b570043e696a832c7d97eafb4?pvs=204) and [KFM Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447?pvs=204) | **Coordination lineage** | Notion tracks proposal lineage, implementation handoffs, and the rule that GitHub is implementation authority. | Notion is not semantic or runtime authority for this path. |
| [Google Drive: KFM_Full_Atlas_seed_cards](https://docs.google.com/document/d/1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho/edit?usp=drivesdk) | **Read-only proposal lineage** | Source ideas and shared governance vocabulary consulted during reconciliation. | Drive content was not imported as repository authority, source admission, review, release, or publication state. |

---

## Rollback

This is a same-path documentation change. If the index is rejected or its inventory becomes stale, restore the immediate prior blob [`1bf959b1f940996e70f1822a33e5839af384ff4e`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/1bf959b1f940996e70f1822a33e5839af384ff4e/contracts/common/README.md) at `contracts/common/README.md`.

Rollback must not delete or rewrite the 38 child contracts, paired schemas, fixture lanes, validators, tests, policy boundaries, or their history. Any semantic relocation requires a separate reviewed migration with predecessor/successor IDs, compatibility notes, consumer impact, correction behavior, and a new rollback target.

---

## Definition of done

- [ ] Affected stewards confirm that each child concept is genuinely cross-cutting.
- [ ] Each child keeps its own status, version, owner, and truth posture current.
- [ ] Every paired schema, fixture lane, validator, and focused test is linked or explicitly marked `NEEDS VERIFICATION`.
- [ ] No `policy/common/`, parallel schema home, source registry, evidence store, release record, or runtime authority is implied by this path.
- [ ] Domain-specific or specialized concepts are routed to their owning contract family.
- [ ] Material changes include compatibility, migration, deprecation, correction, and rollback notes.
- [ ] Current validation is read back from the exact head before a pass is claimed.
- [ ] No documentation change is represented as source admission, review approval, release, deployment, or publication.

---

## Status summary

`contracts/common/` is the repository-grounded shared semantic-contract lane: 38 child Markdown contracts, 38 same-basename configured v1 schemas, and 38 synthetic fixture families are present at the inspected main. The surface remains mixed-maturity and largely proposed; it is not a schema registry, policy evaluator, evidence store, lifecycle root, release authority, runtime, API/UI surface, or public-publication gate.

<p align="right"><a href="#top">Back to top</a></p>
