<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-truth-label-lint-readme
title: tools/validators/docs/truth-label-lint README
type: README
version: v0.2.0
status: bounded-executable; opt-in; no-network; non-authoritative; review-pending
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-evidence-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-08-23
policy_label: repository-facing; docs-validator; truth-label-lint; evidence-posture-qa; non-authoritative
owning_root: tools/
responsibility: Deterministically verify that explicitly opted-in Markdown assessments record authority or epistemic posture separately from capability maturity, without deciding either axis, interpreting its values, editing documents, or creating evidence, policy, review, release, or publication authority.
truth_posture: CONFIRMED bounded standard-library executable, synthetic cases, focused tests, and read-only workflow proposal / PROPOSED adoption by individual assessment documents / NEEDS VERIFICATION hosted exact-head results, steward acceptance, and any future expansion beyond the opt-in structural rule
related:
  - ../README.md
  - ../../_common/README.md
  - ../meta-block/README.md
  - ../stale-scan/README.md
  - ../terminology-parity/README.md
  - ../../../../docs/intake/exploratory/circled-whole-system-sources-distinctive-delta-source-map.md
  - ../../../../docs/doctrine/truth-posture.md
  - ../../../../docs/registers/README.md
  - ../../../../CONTRIBUTING.md
  - ../../../../tests/validators/docs/truth-label-lint/README.md
  - ../../../../.github/workflows/truth-label-assessment-axes.yml
notes:
  - "Source provenance: KFM Circled Sources — Distinctive Delta Synthesis, section 3.1, preserves the residual rule that dated assessments keep authority or epistemic posture separate from capability maturity."
  - "The validator recognizes structure only. It deliberately does not define, validate, normalize, or rank the values recorded on either axis."
  - "Unmarked Markdown is NOT_APPLICABLE by default; repository-wide enforcement remains outside this slice."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/truth-label-lint/`

> **Purpose.** Enforce one narrow reporting invariant for documents that opt in:
> authority or epistemic posture and capability maturity must appear as separate,
> nonempty rows in the same Markdown assessment table.

## Status and source provenance

The source-corpus reconciliation retained one distinctive reporting rule from
*KFM Circled Sources — Distinctive Delta Synthesis*, §3.1, **“Two-axis
assessment: authority is not maturity.”** The current repository source map
preserves the rule as contributor guidance and explicitly rejects turning it into
another state machine or machine enum.

This lane implements only the structural portion of that rule. It does not adopt
the source document as repository authority and does not expand the accepted
truth-label vocabulary.

| Surface | Bounded current state |
|---|---|
| Validator | **PROPOSED / implemented on this branch** — standard-library, deterministic, no network, read-only |
| Opt-in contract | **PROPOSED** — exact marker and table shape below |
| Value vocabulary | **UNCHANGED** — values are preserved as written and not interpreted |
| Repository-wide use | **NOT ENABLED** — unmarked documents are skipped |
| Workflow | **PROPOSED** — focused tests only; no document mutation or QA artifact upload |
| Authority | **NONE** — a pass is documentation-structure evidence only |

## Opt-in document contract

A document opts in with the exact semantic marker, matched case-insensitively:

```markdown
<!-- kfm-assessment-axes: required -->
```

It must then contain one Markdown table whose headers include:

- `Axis`; and
- one of `Result`, `Assessment`, `Value`, or `Current result`.

The table must contain separate nonempty rows recognizable as:

```markdown
| Axis | Current result |
|---|---|
| Authority / epistemic posture | CONFIRMED for the stated evidence scope |
| Capability maturity | PARTIAL — bounded executable and synthetic tests |
```

The checker accepts reasonable label variants containing `authority` or
`epistemic` for the first row and `capability maturity` or `implementation
maturity` for the second. It does not validate the result strings against an
enum. That semantic decision remains with doctrine, contracts, policy, and human
review where applicable.

## Commands

Scan one opted-in document:

```bash
python tools/validators/docs/truth-label-lint/lint_truth_labels.py \
  path/to/assessment.md
```

Require every explicitly supplied Markdown file to carry the marker:

```bash
python tools/validators/docs/truth-label-lint/lint_truth_labels.py \
  --require-marker \
  path/to/assessment.md
```

Emit deterministic JSON:

```bash
python tools/validators/docs/truth-label-lint/lint_truth_labels.py \
  --format json \
  path/to/assessment.md
```

Run the focused tests:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/truth-label-lint \
  --pattern 'test_*.py' \
  --verbose
```

## Finite outcomes

| Outcome | Meaning | Exit code |
|---|---|---:|
| `DOC_TRUTH_LABEL_LINT_PASS` | Every opted-in document has one nonempty row for each separate axis in the same table. | `0` |
| `DOC_TRUTH_LABEL_LINT_NOT_APPLICABLE` | The document did not opt in and `--require-marker` was not used. | `0` |
| `DOC_TRUTH_LABEL_LINT_FAIL` | An opted-in document violates the structural contract. | `1` |
| `ERROR` | Input discovery, UTF-8 reading, or another operational precondition failed. | `2` |

Finding codes are deterministic:

- `ASSESSMENT_AXES_MARKER_MISSING`;
- `ASSESSMENT_TABLE_MISSING`;
- `AUTHORITY_AXIS_MISSING`;
- `CAPABILITY_MATURITY_AXIS_MISSING`;
- `ASSESSMENT_AXIS_VALUE_MISSING`;
- `ASSESSMENT_AXES_COLLAPSED`;
- `ASSESSMENT_AXIS_DUPLICATE`; and
- `ASSESSMENT_AXES_SPLIT_TABLE`.

## Authority and safety boundary

A green result proves only that configured Markdown structure was observed in
the scanned bytes. It does **not** prove that:

- either recorded value is true, current, accepted, or complete;
- repository behavior, tests, workflows, deployment, or operations match the document;
- an EvidenceRef resolves or an EvidenceBundle is sufficient;
- source rights, sensitivity, policy, review, correction, or rollback are closed;
- a change is ready for review, merge, release, deployment, promotion, publication, or public use.

The validator:

- reads Markdown only;
- ignores fenced examples so sample tables cannot satisfy a real assessment;
- does not follow symlink inputs;
- performs no network, model, subprocess, package, or repository write;
- emits findings to standard output only; and
- leaves metadata, freshness, terminology, evidence, and policy checks to their owning lanes.

## Directory Rules basis

Accepted ADR-0029 and Directory Rules place reusable repository validators under
`tools/`, executable proof under `tests/`, read-only GitHub orchestration under
`.github/workflows/`, and source-lineage explanations under `docs/`. This slice
uses those existing roots and creates no parallel doctrine, contract, schema,
policy, receipt, proof, registry, release, or publication home.

## Validation and rollback

Synthetic cases cover pass, not-applicable, missing-axis, collapsed-axis,
split-table, duplicate-axis, empty-value, fenced-example, deterministic-output,
UTF-8 failure, symlink, no-network, and finite-exit behavior.

Rollback is ordinary Git reversion of the validator, tests, documentation, and
focused workflow. No source, governed data, release, deployment, or public state
is created or mutated.

## Open verification

- **NEEDS VERIFICATION:** accountable tooling, docs, evidence, and CI stewards.
- **NEEDS VERIFICATION:** hosted exact-head workflow conclusions and effective required-check coupling.
- **PROPOSED:** opt-in adoption by selected dated assessment documents after human review.
- **UNKNOWN:** whether a future accepted profile should validate any axis values; this slice intentionally abstains.

[Back to top](#top)
