<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/missing-value-filter-receipt
title: MissingValueFilterReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; common; analysis-qa; missingness; population-change; auditability
responsibility: Define a fixture-only receipt candidate for disclosing missing-value filters, before/after count summaries, supporting references, and population-change review posture without analysis-truth, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/missing_value_filter_receipt.schema.json
  - ../../fixtures/contracts/v1/common/missing_value_filter_receipt/cases.json
  - ../../tools/validators/validate_missing_value_filter_receipt.py
  - ../../tests/validators/test_validate_missing_value_filter_receipt.py
  - ../../docs/intake/exploratory/pass-18-missing-value-filter-receipt-source-map.md
[/KFM_META_BLOCK_V2] -->

# MissingValueFilterReceiptCandidate

`MissingValueFilterReceiptCandidate` is an additive, fixture-only profile for making missing-value row filters and their population consequences inspectable before a derived analysis can be considered by a later governed workflow.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-443`: record missing-value filters, before/after summary-statistic steps, supporting analysis/DQ/layer references, and the possibility that filtering changes or biases the analyzed population.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. Its `downstream_disposition` is fixed to `HOLD_FOR_REVIEW`. A validator `PASS` means only that:

- the candidate is closed under this schema;
- its deterministic profile hash replays;
- the input and output dataset candidates are pinned by reference and digest;
- supporting analysis-receipt, DQ-report, summary-statistics, and layer-manifest references are explicit;
- ordered filter steps state the field, missing-value rule, rationale, and row counts;
- each step and the complete step chain reconcile without silent row loss;
- each filter has paired `COUNT` summary steps for the population before and after filtering;
- the paired summary row counts match the referenced filter step;
- a population-change assessment posture and limitations are present; and
- evidence references are canonically ordered.

It does **not** open a dataset, infer which values are missing, execute a filter, recompute a statistic, determine whether exclusion is scientifically justified, authenticate any digest, resolve evidence, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `receipt_ref` | Stable identity of this proposed missing-value filter receipt. |
| `analysis_scope` | Pinned scope candidate and explicit local resolution state. |
| `input_dataset` / `output_dataset` | Pinned dataset candidates and row counts; neither is opened or authenticated. |
| `supporting_artifacts` | Pinned analysis receipt, DQ report, summary-statistics report, and layer manifest with explicit local resolution states. |
| `filter_steps` | Ordered field-level exclusion disclosures. Each rule states whether nulls, empty strings, and/or declared sentinel tokens count as missing. |
| `summary_statistic_steps` | Pinned result candidates for before/after counts tied to each filter step and field. Values other than row counts remain opaque. |
| `population_change_assessment` | Explicit `REVIEW_REQUIRED`, claimed material/no-material shift, or unresolved posture with rationale and compared dimensions. It is not a review approval. |
| `downstream_disposition` | Fixed `HOLD_FOR_REVIEW`; the profile cannot authorize publication. |
| `evidence_refs` | Canonically ordered references retained for a later resolver. |
| `authority_claims` | Fixed-false declaration preventing analysis-truth, evidence, policy, review, promotion, release, publication, or public-use authority. |

No source rows, field values, derived statistics, or sensitive payloads are carried by this profile.

## Filter-chain reconciliation

Every step must satisfy:

`input rows = excluded rows + output rows`.

The first step's input count must equal the input dataset count. Each later step's input count must equal the previous step's output count. The final step's output count must equal the output dataset count.

These equations prevent undisclosed row disappearance within the candidate. They do not prove that the counts were computed from a real dataset.

## Missing-value rule disclosure

Each step must declare at least one missing representation: JSON/database-style null, empty string, or one or more bounded sentinel tokens. Sentinel tokens must be unique and canonically ordered. Recording a token does not endorse its use or prove that it is safe for a real field.

## Population-change posture

Filtering can change the population represented by an analysis. The profile requires an explicit assessment candidate:

- `REVIEW_REQUIRED` records that downstream review is necessary;
- `MATERIAL_SHIFT_CLAIMED` or `NO_MATERIAL_SHIFT_CLAIMED` records an unauthenticated candidate claim for later review; and
- `UNKNOWN` or an unresolved assessment causes validator `ABSTAIN`.

No status authorizes publication. All outcomes remain held for review.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, bindings, filter chain, paired count summaries, population-change disclosure, and canonical references are coherent. |
| `ABSTAIN` | The analysis scope, input dataset, a supporting artifact, or population-change assessment is explicitly unresolved. |
| `DENY` | A deterministic identity, UTC, filter-rule, count, chain, summary, output, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These are validator outcomes only. They are not QA approval, evidence findings, policy decisions, release states, or runtime answers.

## Directory Rules basis

Missing-value filtering changes the meaning of an analysis population across domains, so the bounded semantic profile lives under the established shared `contracts/common/` lane. Machine shape, synthetic cases, executable validation, tests, CI, source reconciliation, and authoring accountability remain in their accepted responsibility roots.

No new root, data-quality authority, evidence authority, policy authority, runtime analysis, or publication path is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_missing_value_filter_receipt -v
python tools/validators/validate_missing_value_filter_receipt.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no dataset, analysis, statistic, layer, evidence record, policy decision, lifecycle record, release, cache, route, deployment, or public artifact.
