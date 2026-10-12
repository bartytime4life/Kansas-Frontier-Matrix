<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-sensitivity-readme
title: Tests — Flora Sensitivity
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <flora-domain-steward> + <sensitivity-reviewer> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/architecture/sensitivity.md
  - docs/architecture/sensitivity-tiers.md
  - docs/domains/flora/SENSITIVITY.md
  - docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - docs/domains/flora/FILE_SYSTEM_PLAN.md
  - policy/domains/flora/sensitivity.rego
  - policy/sensitivity/flora/
  - fixtures/domains/flora/
  - schemas/contracts/v1/receipts/
tags:
  - kfm
  - tests
  - flora
  - sensitivity
  - geoprivacy
  - rare-plants
  - redaction
  - fail-closed
notes:
  - "This README governs the sensitivity test lane under tests/domains/flora/sensitivity/."
  - "It documents intended enforcement coverage; it does not claim that all tests already exist."
  - "Policy-home drift remains visible: Directory Rules and FILE_SYSTEM_PLAN prefer policy/domains/flora/ for flora-scoped rules, while current scaffolds also exist under policy/sensitivity/flora/. Do not treat this README as resolving that ADR-class conflict."
[/KFM_META_BLOCK_V2] -->

# Tests — Flora Sensitivity

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fflora%2Fsensitivity-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-deny--by--default-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the test home for Flora sensitivity enforcement: rare-plant geoprivacy, exact-geometry denial, tier transitions, join-induced sensitivity, culturally sensitive plant handling, and required redaction/review receipts.

---

## 1. Placement and authority

`tests/domains/flora/sensitivity/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove that Flora sensitivity rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `sensitivity/` |
| Primary doctrine | `docs/doctrine/directory-rules.md` |
| Domain doctrine | `docs/domains/flora/SENSITIVITY.md` and related Flora sensitivity docs |
| Enforcement target | Policy, receipt, fixture, and release-gate behavior for public-safe Flora exposure |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific tests under `tests/domains/<domain>/`. The Flora file-system plan names `tests/domains/flora/sensitivity/` as the rare-plant and join-induced sensitivity test lane.

---

## 2. What this lane must prove

These tests should prove that sensitive Flora material fails closed unless a governed, reviewable, and reversible path exists.

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Rare / protected plant records | Exact public geometry is denied by default. | `DENY` or equivalent fail-closed outcome. |
| Exact geometry denial | Public payloads containing sensitive exact coordinates cannot promote. | `DENY_BY_POLICY`, `SENSITIVITY_UNRESOLVED`, or local equivalent. |
| Public-safe geometry | Sensitive records may expose only generalized, aggregated, suppressed, or withheld geometry after review. | `MISSING_PUBLIC_SAFE_GEOMETRY` or equivalent. |
| Redaction receipt | Any sensitivity transform must reference a resolvable `RedactionReceipt`. | `MISSING_RECEIPT`. |
| Review record | More-public transitions, especially `T4 -> T1`, require steward review. | `MISSING_REVIEW`. |
| Join-induced sensitivity | Joined products inherit the most restrictive input sensitivity tier. | `JOIN_ESCALATES_SENSITIVITY` or equivalent. |
| CARE / sovereignty context | Culturally sensitive or steward-governed plant knowledge cannot publish without the required labels, consent, waiver, or review evidence. | `CARE_REVIEW_REQUIRED`, `SOVEREIGNTY_REVIEW_REQUIRED`, or equivalent. |
| Negative states | Public clients should see visible denial/generalization states, not silent empty results. | Test should fail on silent omission. |

---

## 3. Expected test families

This folder should eventually contain narrowly scoped tests, not one large mixed harness.

```text
tests/domains/flora/sensitivity/
├── README.md
├── test_exact_geometry_deny.py              # PROPOSED
├── test_rare_plant_geoprivacy.py            # PROPOSED
├── test_redaction_receipt_required.py       # PROPOSED
├── test_tier_transition_review.py           # PROPOSED
├── test_join_induced_sensitivity.py         # PROPOSED
├── test_cultural_sensitivity_review.py      # PROPOSED
├── test_negative_states.py                  # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If the repository uses another test runner or filename convention, preserve that convention and keep this README as the lane contract.

---

## 4. Fixture expectations

Tests in this lane should be no-network by default. They should use synthetic or golden fixtures from `fixtures/domains/flora/`, not live GBIF, iNaturalist, PLANTS, herbarium, or steward-provided sources.

Recommended fixture groups:

```text
fixtures/domains/flora/
├── valid/
│   ├── generalized_rare_plant_with_redaction_receipt.json
│   └── public_common_species_occurrence.json
├── invalid/
│   ├── rare_plant_exact_public_geometry.json
│   ├── rare_plant_missing_redaction_receipt.json
│   ├── t4_to_t1_missing_review_record.json
│   └── joined_product_drops_restrictive_tier.json
└── synthetic/
    ├── cultural_sensitivity_requires_review.json
    └── join_induced_sensitivity_case.json
```

Fixture data must not contain real precise rare-plant coordinates, unpublished steward knowledge, or culturally sensitive location detail. Use synthetic coordinates, generalized envelopes, or placeholders.

---

## 5. Policy and contract targets

This README does not decide the canonical policy home. It records the test lane’s expected targets while keeping the current placement conflict visible.

| Target | Role | Status |
|---|---|---|
| `policy/domains/flora/sensitivity.rego` | Flora-scoped sensitivity policy target under the domain segment. | Existing scaffold; enforcement depth still needs implementation. |
| `policy/sensitivity/flora/rare_plant_geoprivacy.rego` | Existing rare-plant geoprivacy scaffold. | Existing scaffold; placement is subject to drift/ADR review. |
| `policy/sensitivity/flora/exact_geometry_deny.rego` | Existing exact-geometry denial scaffold. | Existing scaffold; placement is subject to drift/ADR review. |
| `policy/sensitivity/flora/join_induced_sensitivity.rego` | Existing join-induced sensitivity scaffold. | Existing scaffold; placement is subject to drift/ADR review. |
| `schemas/contracts/v1/receipts/*redaction*` | Machine shape for redaction receipt evidence. | NEEDS VERIFICATION before hard-coded imports. |
| `docs/domains/flora/SENSITIVITY.md` | Human sensitivity contract and test backlog. | Draft; overlaps with `RIGHTS_AND_SENSITIVITY.md`. |

**Rule for future tests:** import policy modules through the repository’s chosen policy-test harness. Do not bake a second policy authority into tests. If the policy home changes by ADR, update imports and this table together.

---

## 6. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `FLORA-SENS-001` | Exact rare-plant public geometry is denied. | A rare/protected plant occurrence with exact public coordinates. | Policy denies public release. |
| `FLORA-SENS-002` | Generalized geometry can pass only with receipt and review. | A rare plant occurrence transformed to county/grid/generalized geometry. | Policy allows only if `RedactionReceipt` and `ReviewRecord` resolve. |
| `FLORA-SENS-003` | Missing receipt blocks release. | A public-safe-looking sensitive derivative without a redaction receipt. | Release/policy gate fails closed. |
| `FLORA-SENS-004` | Join inherits most restrictive tier. | A T0 public checklist joined to a T4 rare locality record. | Joined output is T4 or denied until generalized and reviewed. |
| `FLORA-SENS-005` | Culturally sensitive plant material requires review. | A plant record flagged culturally/steward sensitive. | Public release is denied without required authority evidence. |
| `FLORA-SENS-006` | User-facing negative state is visible. | A denied or generalized response. | Payload exposes a bounded negative state such as `DENIED_BY_POLICY` or `GENERALIZED_GEOMETRY`. |

---

## 7. Non-goals

This folder must not:

- call live external source APIs;
- include real exact coordinates for rare, protected, or culturally sensitive plants;
- publish source-derived sensitive locations as fixtures;
- create a new policy home or schema home;
- treat model output, map tiles, vector indexes, or summaries as root truth;
- relax public exposure because a record is well sourced; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, or `ERROR` into an empty success.

---

## 8. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The expected result is fail-closed where evidence, policy, receipt, or review is missing.
- [ ] The test preserves the RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED trust membrane.
- [ ] The test does not bypass governed API/release behavior to assert public exposure from internal stores.
- [ ] The test cites the policy or contract it is proving.
- [ ] Any path conflict is recorded as drift or verification backlog, not silently normalized.

---

## 9. Current implementation note

This lane is documentation-first. The neighboring Flora test root is still a minimal greenfield stub, and the currently visible Flora sensitivity policy files are proposed scaffolds with deny-by-default defaults. That is acceptable for a README, but it means test coverage should be treated as `PROPOSED` until actual test files, fixtures, and CI runs prove enforcement.

---

## 10. Definition of done

This README becomes implementation-backed when:

- at least the `FLORA-SENS-001` through `FLORA-SENS-006` scenarios exist as executable tests;
- test fixtures live under `fixtures/domains/flora/` and contain no sensitive real coordinates;
- policy imports follow the ADR-approved Flora policy home;
- redaction/review receipt shapes are validated against schemas;
- CI runs the tests without network access; and
- failures emit finite, inspectable outcomes rather than silent skips.
