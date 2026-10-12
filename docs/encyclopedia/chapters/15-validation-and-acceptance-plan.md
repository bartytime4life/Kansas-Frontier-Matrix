<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/15-validation-and-acceptance-plan
title: "Validation and acceptance plan"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain validation and acceptance plan and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Validation and acceptance plan

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

Validation should match the claim being made. Documentation checks, code tests, provider access, hosted deployment and human acceptance answer different questions.

## Evidence matrix

| Claim | Appropriate evidence | Does not establish |
|---|---|---|
| A document is structurally usable | Metadata, local links and document graph checks | Truth of every claim or external link availability |
| A behavior is implemented | Source plus focused tests of the real path | Provider availability or deployed version |
| A candidate conforms | Exact schema/profile and meaningful invalid cases | Source admission or release approval |
| A Site version is deployed | Saved source/artifact identity and deployment result | Keyboard, touch, WebGL or visual acceptance |
| A workflow is usable | Browser/host exercise with recorded environment and cases | All possible environments or source products |
| A governed result is accepted | Required reviewer/decision records for the exact candidate | Future candidates or unrelated releases |

## Documentation commands

From the repository root with Python 3.11 or newer and declared validation dependencies:

```sh
python3 tools/validators/docs/link-check/check_links.py --repo-root . docs/encyclopedia
python3 tools/validators/docs/meta-block/check_meta_blocks.py --repo-root . docs/encyclopedia
python3 tools/qa/gap_scan.py --check
```

Use the [document-graph checker](../../../tools/validators/docs/document-graph/README.md) with the exact base/head for broader navigation and identity review. The Python executable must meet the requirement; some hosts map `python3` to an older interpreter.

## Acceptance cases

Check a normal reading path, missing data, partial coverage, stale dates and unsupported capability claims. For changed UI behavior, include selection/time changes while requests are pending, empty and failed responses, keyboard access and a narrow display. For acquisition, test limits, verification failure and immutable identity conflicts without downloading unbounded data.

Record command, version, input scope, result and any inherited failure separately. Do not loosen a baseline or rewrite an old receipt to make a new change pass. Correct introduced issues; attribute unresolved inherited issues with a base comparison. No acceptance is recorded by this plan alone.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
