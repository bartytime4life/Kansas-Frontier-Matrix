<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-source-descriptor-readme
title: Tests — Flora Source Descriptor
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <flora-domain-steward> + <source-authority-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_INTAKE.md
  - contracts/source/source_descriptor.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - tools/validators/validate_source_descriptor.py
  - tools/validators/domains/flora/validate_source_descriptor.py
  - fixtures/contracts/v1/source/source_descriptor/
  - fixtures/domains/flora/
tags:
  - kfm
  - tests
  - flora
  - source-descriptor
  - source-registry
  - admission
  - rights
  - sensitivity
  - source-role
  - fail-closed
notes:
  - "This README governs the source-descriptor test lane under tests/domains/flora/source_descriptor/."
  - "It documents intended Flora-specific descriptor test coverage; it does not claim that all tests already exist."
  - "Generic source_descriptor validation currently has a repo-wide validator; the Flora-specific validator path is currently a greenfield placeholder and should not be treated as enforcement proof."
[/KFM_META_BLOCK_V2] -->

# Tests — Flora Source Descriptor

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fflora%2Fsource__descriptor-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-success?style=flat-square)
![admission](https://img.shields.io/badge/admission-fail--closed-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Flora-domain test lane for `SourceDescriptor` admission checks: source identity, source role, rights, sensitivity, cadence, access posture, citation guidance, descriptor versioning, and Flora-specific domain extensions.

---

## 1. Placement and authority

`tests/domains/flora/source_descriptor/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove source-admission rules are enforceable for the Flora lane.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `source_descriptor/` |
| Cross-domain standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` |
| Domain registry doctrine | `docs/domains/flora/SOURCE_REGISTRY.md` |
| Generic validator target | `tools/validators/validate_source_descriptor.py` |
| Flora validator target | `tools/validators/domains/flora/validate_source_descriptor.py` |
| Fixture homes | `fixtures/contracts/v1/source/source_descriptor/` and `fixtures/domains/flora/` |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific tests under `tests/domains/<domain>/`. The Flora file-system plan names `tests/domains/flora/source_descriptor/` as the admission-gate test lane for Flora source descriptors.

---

## 2. What this lane must prove

These tests should prove that Flora sources cannot enter active use unless their descriptor fixes the minimum governance facts needed for later evidence, policy, citation, and release checks.

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Core identity | `source_id`, `source_role`, `display_name`, `domain_lane`, and `owner_steward` are present and stable. | Validation failure; no activation. |
| Domain lane | Flora descriptors resolve to `domain_lane = flora` or the repository's canonical flora lane value. | Domain mismatch failure. |
| Source role | `source_role` uses the canonical vocabulary and is not inferred from convenience. | Role validation failure or `needs-review`. |
| Role-conditional fields | Modeled, aggregate, synthetic, regulatory, and candidate descriptors carry the extra fields required by role. | Fail closed for missing conditional fields. |
| Rights | License, attribution, redistribution class, and terms review state are explicit. Unknown or stale terms route to restriction, denial, or review. | `RIGHTS_UNRESOLVED`, `TERMS_STALE`, or equivalent. |
| Sensitivity | Tier, sensitivity classes, steward-review requirement, and transform profile are resolved where needed. | `SENSITIVITY_UNSET` or equivalent. |
| Cadence and freshness | Expected update interval, staleness threshold, last-seen timestamp, and retrieval method are present. | Stale/invalid descriptor outcome. |
| Access posture | Endpoint class, auth model where required, and deny-by-default access posture are present. | Access validation failure. |
| Citation guidance | Public-facing sources provide citation template and role qualifier where needed. | `MISSING_CITATION_GUIDANCE` or equivalent. |
| Provenance and versioning | Ingest hash, prior descriptor reference, and correction lineage are present when applicable. | `MISSING_PROVENANCE` or equivalent. |

---

## 3. Expected test families

This folder should eventually contain narrowly scoped tests, not a single mixed harness.

```text
tests/domains/flora/source_descriptor/
├── README.md
├── test_core_identity.py                    # PROPOSED
├── test_domain_lane.py                      # PROPOSED
├── test_source_role_vocabulary.py           # PROPOSED
├── test_role_conditional_fields.py          # PROPOSED
├── test_rights_and_terms.py                 # PROPOSED
├── test_sensitivity_fields.py               # PROPOSED
├── test_cadence_and_freshness.py            # PROPOSED
├── test_access_posture.py                   # PROPOSED
├── test_citation_guidance.py                # PROPOSED
├── test_provenance_and_versioning.py        # PROPOSED
├── test_flora_domain_extensions.py          # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If the repository uses another test runner or filename convention, preserve that convention and keep this README as the lane contract.

---

## 4. Fixture expectations

Tests in this lane should be no-network by default. They should use small synthetic or golden descriptors, not live source calls.

Recommended fixture groups:

```text
fixtures/domains/flora/source_descriptor/
├── valid/
│   ├── usda_plants_observed_or_reference_descriptor.json
│   ├── gbif_occurrence_restricted_descriptor.json
│   ├── herbarium_specimen_descriptor.json
│   └── modeled_distribution_surface_descriptor.json
├── invalid/
│   ├── missing_source_role.json
│   ├── role_candidate_missing_disposition.json
│   ├── aggregate_missing_aggregation_unit.json
│   ├── modeled_missing_model_run_ref.json
│   ├── rights_unknown_public_derivative.json
│   ├── sensitivity_tier_missing.json
│   ├── stale_terms_review_state.json
│   └── citation_template_missing.json
└── golden/
    ├── flora_source_descriptor_minimal_open.json
    └── flora_source_descriptor_restricted_sensitive.json
```

Fixture descriptors must not include live credentials, API keys, unpublished steward contacts, or real precise sensitive coordinates. Use placeholder endpoints and synthetic hashes unless the descriptor fixture is intentionally public and rights-reviewed.

---

## 5. Generic vs. Flora-specific validation

Source-descriptor checks have two layers.

| Layer | Responsibility | Example target | Status note |
|---|---|---|---|
| Generic source descriptor | Cross-domain schema and baseline required fields. | `tools/validators/validate_source_descriptor.py` | Existing repo-wide validator target. |
| Flora-specific descriptor | Flora lane requirements: domain lane, source family constraints, rights/sensitivity defaults, botanical role mapping, and rare-plant restrictions. | `tools/validators/domains/flora/validate_source_descriptor.py` | Existing placeholder; enforcement still needs implementation. |

**Rule for future tests:** use the generic validator for cross-domain shape and shared required fields; add Flora-specific tests only for domain behavior that cannot be enforced safely by the generic schema alone.

---

## 6. Flora-specific checks

The Flora source-descriptor lane should add domain assertions only where the Flora registry requires them.

| ID | Flora-specific assertion | Why it matters |
|---|---|---|
| `FLORA-SD-001` | `domain_lane` resolves to Flora and does not silently fall through to a generic ecology lane. | Prevents domain ownership drift. |
| `FLORA-SD-002` | Occurrence/specimen sources that can expose rare plants default to restricted or review-required posture until sensitivity is resolved. | Preserves rare-plant geoprivacy. |
| `FLORA-SD-003` | Aggregate/range/distribution sources declare aggregation or model provenance rather than presenting as direct observations. | Prevents source-role collapse. |
| `FLORA-SD-004` | Candidate or watcher-discovered sources cannot activate a connector without a `SourceActivationDecision`. | Keeps watchers non-publishers. |
| `FLORA-SD-005` | Rights-unknown descriptors cannot back public derivatives. | Preserves deny-by-default source admission. |
| `FLORA-SD-006` | Citation guidance includes a role qualifier for modeled, aggregate, administrative, synthetic, regulatory, or candidate sources. | Prevents misleading public claims. |
| `FLORA-SD-007` | Descriptor freshness fields exist for periodically refreshed botanical sources. | Supports stale-state badges and recheck gates. |
| `FLORA-SD-008` | Sensitive source classes require steward review and transform-profile linkage before public release. | Connects source admission to release safety. |

---

## 7. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `FLORA-SD-001` | Valid open source descriptor passes. | A Flora descriptor with required identity, role, rights, cadence, access, sensitivity, and citation fields. | Generic validation passes and Flora-specific checks pass. |
| `FLORA-SD-002` | Missing `source_role` fails. | A descriptor without source-role vocabulary. | Validation fails closed. |
| `FLORA-SD-003` | Candidate descriptor cannot publish. | A candidate Flora source with pending disposition. | Public activation/published edge is denied. |
| `FLORA-SD-004` | Rights-unknown public derivative is denied. | A descriptor with `rights.redistribution_class = unknown` and public derivative intent. | Policy or validator returns deny/review. |
| `FLORA-SD-005` | Rare-plant-sensitive source requires review. | An occurrence/specimen source with rare-species sensitivity class. | Descriptor requires steward review and transform profile before public exposure. |
| `FLORA-SD-006` | Modeled distribution descriptor carries model provenance. | A modeled Flora distribution surface source. | `role_model_run_ref` is required and validated. |
| `FLORA-SD-007` | Aggregate source carries aggregation unit. | A range/checklist/summary source scoped to county, grid, ecoregion, or year. | `role_aggregation_unit` is required and validated. |
| `FLORA-SD-008` | Citation guidance is role-aware. | A modeled, aggregate, candidate, or synthetic Flora descriptor. | Citation role qualifier is required. |

---

## 8. Non-goals

This folder must not:

- call live external source APIs;
- store source payloads or downloaded data;
- store credentials, tokens, or private steward contacts;
- decide source rights by prose alone;
- treat a descriptor as a publishable claim;
- infer `source_role` using AI or convenience naming;
- weaken rare-plant or culturally sensitive source posture because a source is authoritative; or
- create a second source-descriptor schema, policy, or registry home.

---

## 9. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The test proves a source-admission rule, not a downstream botanical fact.
- [ ] Required failures are fail-closed and produce inspectable reason codes.
- [ ] Role, rights, sensitivity, cadence, access, and citation behavior are preserved separately.
- [ ] The test uses the repository's chosen schema and validator homes.
- [ ] The test does not bypass `SourceActivationDecision` or equivalent admission gates.
- [ ] Any path conflict is recorded as drift or verification backlog, not silently normalized.

---

## 10. Current implementation note

This lane is documentation-first. The repo has a generic `validate_source_descriptor.py` entry point wired to the shared source-descriptor schema and fixture family, while the Flora-specific validator path is currently a greenfield placeholder. That means this README describes the intended Flora test matrix; it is not proof that every Flora source-admission rule is already enforced in CI.

---

## 11. Definition of done

This README becomes implementation-backed when:

- at least the `FLORA-SD-001` through `FLORA-SD-008` scenarios exist as executable tests;
- fixtures exist under the repository's approved source-descriptor fixture homes;
- generic and Flora-specific validators are both wired into CI or the repo-wide validation orchestrator;
- rights, sensitivity, and source-role failures emit finite reason codes;
- candidate, synthetic, modeled, aggregate, and restricted descriptors each have negative tests; and
- descriptor changes have a correction/supersession path rather than silent mutation.
