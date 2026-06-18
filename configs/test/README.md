<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-test-readme
title: configs/test/ — Test Configuration Defaults and Templates
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · QA steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../dev/README.md
  - ../examples/README.md
  - ../../tests/README.md
  - ../../fixtures/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../apps/
  - ../../pipelines/
  - ../../runtime/
tags: [kfm, configs, test, testing, defaults, templates, validation, governance]
notes:
  - "configs/test/ is for commit-safe test configuration defaults and templates only."
  - "Test configs can support tests, but tests/ remains the canonical enforceability root."
  - "Fixtures, lifecycle records, receipts, proofs, release records, generated reports, and implementation code belong in their own roots."
  - "Current inventory, consumers, validation coverage, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Test Configs

`configs/test/`

`configs/test/` is a sublane under the canonical `configs/` root for commit-safe test configuration defaults and templates.

It may describe test runner options, local validation toggles, small template settings, and expected test configuration shape. It must not become the test suite, fixture home, schema authority, policy authority, lifecycle store, release record home, or generated-output home.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `configs/`  
> **Responsibility:** test configuration defaults and templates only  
> **Truth posture:** README path CONFIRMED; parent `configs/` root CONFIRMED as config home; `tests/` root CONFIRMED as the enforceability root; current test config inventory, consumers, validation coverage, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> A test config does not prove a test passes. Do not cite a file in `configs/test/` as evidence of enforcement, coverage, runtime behavior, release readiness, or policy compliance. Verify the test suite, fixtures, tools, and CI evidence before making those claims.

## Purpose

Use this folder for small, reviewable test configuration templates that help maintainers run validation consistently without placing tests, fixtures, reports, or generated output under `configs/`.

This folder should not store test implementation, fixture payloads, lifecycle data, release decisions, schemas, policy rules, source code, runtime adapters, or generated reports.

## Canonical fit

```text
configs/
└── test/
    └── README.md
```

Related roots:

```text
tests/            # canonical enforceability proof
fixtures/         # golden, valid, invalid, and controlled inputs
tools/            # validators and repo-wide checks
schemas/          # machine-checkable shape
policy/           # admissibility rules
apps/             # deployable app code
pipelines/        # executable pipeline logic
runtime/          # runtime adapters
data/             # lifecycle records, receipts, proofs, registry, published artifacts
release/          # release decisions and rollback/correction state
artifacts/        # generated reports and build/QA outputs
```

## Authority boundary

```text
configs/test/
├── test config defaults
├── test config templates
├── local validation toggles
└── notes about expected consumers

NOT HERE:
  test implementation
  fixture data
  generated reports
  schemas
  policy rules
  lifecycle records
  receipts/proofs
  release decisions
  source code
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Test config template | `pytest.example.toml`, `test.template.yaml` | Commit-safe and placeholder-based |
| Local validation config | small test-only defaults | Must identify intended consumer |
| Test runner notes | `validation.md` | Must not claim pass state unless verified |
| Compatibility note | migration note for renamed test config | Temporary and review-linked |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Test source code | `tests/` |
| Fixture payloads and controlled inputs | `fixtures/` or test-confirmed fixture home |
| Validators and repo-wide checks | `tools/` |
| App source | `apps/` |
| Pipeline logic | `pipelines/` |
| Runtime adapter code | `runtime/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Lifecycle records, receipts, proofs, registry rows, or published artifacts | `data/` |
| Release decisions or rollback/correction records | `release/` |
| Generated reports and build/QA outputs | `artifacts/` |
| Worked examples and walkthroughs | `examples/` |

## Suggested directory shape

Current inventory remains `NEEDS VERIFICATION`.

```text
configs/test/
├── README.md
├── pytest.example.toml       # PROPOSED test runner config example
├── validation.example.yaml   # PROPOSED validation config template
├── ci.example.yaml           # PROPOSED CI-facing example only
└── domains/                  # PROPOSED domain-specific test config templates
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual files before making inventory or migration claims.

## Validation expectations

Before relying on a test config here, verify:

- the file is safe to commit;
- placeholders are used where local customization is expected;
- the intended test consumer is named;
- the relevant test suite, fixture set, tool, schema, contract, and policy path are aligned;
- the file is not a test, fixture, report, lifecycle record, release record, or generated output.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve necessary owner notes and rollback instructions.
5. Add a drift note if the misplaced test config was already consumed.

## Safe change pattern

For changes under `configs/test/`:

1. Confirm the file is a test configuration template or config-facing documentation.
2. Confirm the config does not duplicate schema, policy, contract, release, lifecycle, fixture, or test authority.
3. Confirm test implementation belongs under `tests/` and controlled inputs belong under the accepted fixture home.
4. Confirm consumers and validators are updated or explicitly marked `NEEDS VERIFICATION`.
5. Update tests or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `configs/test/` contents are inventoried.
- [ ] Test config templates identify consumers and validation paths.
- [ ] Misplaced files are migrated to the correct owning root.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`configs/test/` is for commit-safe test configuration defaults and templates only. It is not a source of test authority, fixture authority, runtime truth, release truth, schema truth, policy truth, lifecycle truth, implementation truth, or generated-output authority.

<p align="right"><a href="#top">Back to top</a></p>
