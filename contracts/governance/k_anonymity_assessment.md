<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/k-anonymity-assessment
title: K-Anonymity Assessment Contract
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; governance; privacy-assessment; fixture-only; no-authority
owning_root: contracts/
responsibility: Define the semantic boundary for measuring equivalence-class sizes against one separately governed policy-selected k without creating privacy, policy, release, or publication authority.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED contract; NEEDS VERIFICATION human review"
related:
  - ../../schemas/contracts/v1/governance/k_anonymity_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/k_anonymity_assessment/cases.json
  - ../../tools/validators/governance/validate_k_anonymity_assessment.py
  - ../../tests/validators/governance/test_validate_k_anonymity_assessment.py
  - ../../docs/intake/exploratory/pass-2-k-anonymity-assessment-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, privacy, k-anonymity, aggregation, suppression, generalization, fixture-first]
notes:
  - "Adapts Pass 2 card KFM-P2-IDEA-0015 as a bounded assessment, not a policy threshold."
  - "The atlas examples of k=5 or k=10 are not adopted; selected_k must come from policy_profile_ref."
  - "PASS proves local synthetic consistency only and is not a privacy proof or publication decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# K-Anonymity Assessment Contract

> A closed, fixture-only contract for checking whether synthetic equivalence classes meet one **separately governed** `selected_k`. It records quasi-identifiers, generalization, suppression, evidence support, and deterministic identity without deciding policy or authorizing release.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Owning semantic lane | `contracts/governance/` |
| Policy threshold authority | External `policy_profile_ref`; this contract supplies no default |
| Machine shape | `schemas/contracts/v1/governance/k_anonymity_assessment.schema.json` |
| Privacy proof, policy approval, release, publication | Not created or authorized |

A `PASS` means that the submitted synthetic assessment has closed shape, deterministic identity, internally consistent row and class counts, explained transforms, complete local support references, and no equivalence class smaller than the policy-selected value. It does **not** establish that the quasi-identifier set is complete, that linkage risk is acceptable, that k-anonymity is sufficient for the use case, or that the dataset may be released.

## Directory Rules basis

ADR-0029 accepts Directory Rules v2. The change uses existing responsibility roots:

| Responsibility | Home |
|---|---|
| Human-readable meaning | `contracts/governance/` |
| Machine-checkable shape | `schemas/contracts/v1/governance/` |
| Synthetic examples | `fixtures/contracts/v1/governance/` |
| Deterministic validation | `tools/validators/governance/` |
| Enforceability proof | `tests/validators/governance/` |
| Hosted orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No privacy-policy root, source registry, lifecycle store, evidence store, proof lane, release lane, API, UI route, or public artifact is created.

## Object meaning

```text
KAnonymityAssessment
├── subject
│   ├── row_count
│   ├── geography_granularity
│   ├── time_granularity
│   └── policy_label
├── policy_selection
│   ├── policy_profile_ref
│   ├── policy_version
│   ├── selected_k
│   ├── selected_k_source = policy_profile
│   └── policy_decision_refs
├── quasi_identifiers
├── generalization
│   └── explained transform steps and receipt refs
├── suppression
│   └── count, reasons, and transform receipt refs
├── equivalence_classes
│   └── digest-only class key plus record_count
├── evidence_refs
├── assessment
│   └── class_count and min_class_size
├── explicit no-authority claims
├── spec_hash
└── assessment_id derived from spec_hash
```

Raw quasi-identifier values are not part of this profile. Each class is represented by a SHA-256 digest and count. That reduces fixture exposure but does not make a real dataset safe.

## Deterministic identity

The repository hashing package supplies RFC 8785 JCS plus SHA-256.

1. Remove `assessment_id` and `spec_hash`.
2. Compute `spec_hash` over the remaining document.
3. Set `assessment_id` to `kfm:k-anonymity-assessment:` plus the full `spec_hash`.
4. Sort `equivalence_classes` lexically by `key_digest`.

A changed policy selection, quasi-identifier set, transform explanation, class count, evidence reference, or authority claim therefore changes identity.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, arithmetic, transform explanations, support references, and every class threshold pass locally. |
| `ABSTAIN` | The class arithmetic passes, but evidence or policy-decision support is incomplete. |
| `DENY` | Shape, identity, quasi-identifier, ordering, transform-field, no-authority, or class-threshold rules fail. |
| `ERROR` | The input cannot be read safely or the assessment contradicts itself, such as unexplained suppression or broken row-count closure. |

Stable diagnostics contain codes and JSON Pointer paths; they do not echo candidate values.

## Required invariants

- `selected_k` has no schema default and `selected_k_source` is always `policy_profile`.
- At least one quasi-identifier is required for a meaningful assessment.
- Every equivalence-class count must be at least `selected_k` for `PASS`.
- Class counts plus suppressed rows must equal `subject.row_count`.
- Generalization and suppression require reasons and transform receipt references when used.
- A generalization field must be a declared quasi-identifier.
- Evidence and policy-decision references are required for `PASS`; absence yields `ABSTAIN`.
- `claims.privacy_proof`, `policy_approved`, `release_authorized`, `lifecycle_write_performed`, and `published` remain false.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_validate_k_anonymity_assessment.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/governance/validate_k_anonymity_assessment.py \
  --fixtures
```

The fixture matrix covers `PASS`, `ABSTAIN`, `DENY`, and `ERROR`, including missing support, a class below k, empty quasi-identifiers, hash and ID drift, noncanonical class order, unexplained transforms, arithmetic contradiction, and forbidden authority claims.

## Explicit non-goals

This contract does not:

- choose `k`;
- decide which quasi-identifiers are complete;
- measure composition, differencing, linkage, singling-out, or attribute-disclosure risk;
- prove privacy or legal compliance;
- admit or access a source;
- transform or persist real records;
- evaluate a live policy engine;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- create evidence, proof, review, release, correction, or rollback authority;
- expose an API, map layer, export, or UI.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the bounded feature commit or merge commit. The rollback removes only this proposed contract, schema, fixture matrix, validator, tests, workflow, source map, and generated receipt. No live data, policy decision, lifecycle state, release, deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
