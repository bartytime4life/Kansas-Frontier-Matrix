<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-meta-block-readme
title: tools/validators/docs/meta-block README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator; meta-block; markdown-qa; non-authoritative
owning_root: tools/
responsibility: proposed documentation metadata-block validator lane for KFM_META_BLOCK_V2 presence, parseability, required fields, path/doc_id consistency, truth-posture labels, owner/status posture, related-link hygiene, and docs-QA reports without deciding doctrine, evidence sufficiency, source admissibility, or release approval
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../../docs/README.md
  - ../../../../docs/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/adr/
  - ../../../../docs/architecture/trust-membrane.md
  - ../../../../data/receipts/validation/
  - ../../../../artifacts/qa/
  - ../../../../tests/
notes:
  - "This README documents a proposed docs meta-block validator lane. It does not confirm executable files."
  - "A meta-block checker can report missing, malformed, inconsistent, or stale metadata. It cannot decide that a claim is true, a source is admissible, a policy exception is valid, or a release is approved."
  - "KFM_META_BLOCK_V2 is widely used in repository Markdown, but this README does not assert that every file is compliant or that a validator already exists."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs/meta-block

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--meta--block-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/meta-block/` is the proposed documentation metadata-block validator lane for Markdown files: `KFM_META_BLOCK_V2` presence, delimiters, parseability, required keys, path consistency, `doc_id` posture, owner/status fields, policy labels, related-link hygiene, truth-posture labels, and docs-QA reports.

---

## Purpose

`tools/validators/docs/meta-block/` exists for metadata-block validation of repository documentation and README-style Markdown.

The durable KFM question for this lane is:

> Does a document carry a parseable, bounded, internally consistent KFM metadata block without implying that metadata presence proves truth, policy approval, evidence closure, implementation maturity, or release state?

The answer should be a deterministic validation result and, where configured, a docs QA report. It should not edit doctrine, approve ADRs, validate evidence sufficiency, decide source admissibility, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/meta-block/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Meta-block validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| `KFM_META_BLOCK_V2` usage | **CONFIRMED in repo evidence / broad pattern** | Search results show many repository Markdown files use this marker. Completeness and compliance remain unverified. |
| Parent docs-tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says metadata checks are docs tooling and cannot decide truth, admissibility, or release approval. |
| `tools/validators/docs/README.md` | **NOT FOUND in related task evidence** | A parent validator README may be useful later, but this file does not create that parent authority. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, or artifact uploads are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs meta-block validator entrypoints | `tools/validators/docs/meta-block/` |
| Shared validator plumbing | `tools/validators/_common/` |
| General docs tooling | `tools/docs/` |
| Documentation content | `docs/` and each owning responsibility root |
| Documentation registry | `docs/registers/` or accepted docs registry home |
| Doctrine, ADRs, runbooks, standards | owning docs lanes under `docs/` |
| Policy rules | `policy/` |
| Contracts and schemas | `contracts/`, `schemas/` |
| Receipts from validation runs | `data/receipts/validation/` or accepted receipt home |
| QA artifacts and summaries | `artifacts/qa/` when non-authoritative and non-trust-bearing |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** meta-block validator code may live here when it checks metadata-block syntax, parseability, and consistency.
- **NEEDS VERIFICATION:** exact executable names, required-field contract, fixture paths, report destinations, ignore rules, and CI wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, ADR authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/meta-block/` include checks that:

- detect missing `KFM_META_BLOCK_V2` blocks where the configured profile requires one;
- detect malformed opening and closing delimiters;
- parse metadata blocks safely without executing content;
- validate required keys such as `doc_id`, `title`, `type`, `version`, `status`, `owner` or `owners`, `updated`, `policy_label`, `owning_root`, `responsibility`, and `truth_posture` when required by profile;
- check whether `doc_id`, title, owning root, and file path are internally consistent;
- check that `status` and truth-posture labels do not overclaim implementation maturity;
- check `related` entries for basic path hygiene, optionally delegating link resolution to `tools/validators/docs/link-check/`;
- detect duplicate `doc_id` values where a registry or scan is available;
- emit deterministic docs QA summaries and validation receipts where configured;
- support explicit ignore rules with owner, reason, scope, and review posture.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/meta-block/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
| Metadata policy as doctrine | accepted docs standard or ADR, not tool-only convention |
| Policy rules | `policy/` |
| Contracts or schemas | `contracts/`, `schemas/` |
| EvidenceBundle validation | evidence/proof validator lanes |
| Receipts | `data/receipts/` |
| Proofs | `data/proofs/` |
| Release decisions or release manifests | `release/` |
| Published docs or public site output | accepted public/docs publishing root |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Meta-block validation posture

Meta-block checking is documentation QA, not governance approval.

A passing meta-block check means only that the configured validator could parse and check the metadata fields it was asked to inspect. It does not mean:

- the document is authoritative;
- the claims in the document are true;
- the source is admissible;
- the policy posture is correct;
- the implementation maturity is proven;
- the release state is approved;
- the document is safe for public publication.

A failing meta-block check should route to one of these actions:

- add or repair the metadata block;
- correct stale or overconfident status fields;
- fix path, `doc_id`, title, owner, policy label, or related-link drift;
- add a documented ignore rule with owner and review posture;
- open a docs verification backlog item where the correct authority or status is unclear.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `DOC_META_BLOCK_PASS` | Configured metadata-block checks passed. |
| `DOC_META_BLOCK_FAIL` | One or more configured metadata-block checks failed. |
| `META_BLOCK_MISSING` | Required metadata block is absent. |
| `META_BLOCK_MALFORMED` | Metadata block delimiters or parse structure are invalid. |
| `REQUIRED_FIELD_MISSING` | Required metadata key is absent. |
| `FIELD_VALUE_INVALID` | Metadata key is present but outside the accepted profile. |
| `DOC_ID_PATH_MISMATCH` | `doc_id`, title, or owning root does not align with the file path/profile. |
| `DUPLICATE_DOC_ID` | A duplicate `doc_id` was detected in the configured scan scope. |
| `STATUS_OVERCLAIM` | Status/truth posture appears stronger than current evidence supports. |
| `RELATED_ENTRY_INVALID` | A `related` entry is malformed or outside expected path posture. |
| `IGNORED_WITH_REASON` | Failure was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/docs/meta-block/
├── README.md
├── test_docs_meta_block.py
└── fixtures/
    ├── valid_meta_block_v2/
    ├── missing_meta_block/
    ├── malformed_delimiters/
    ├── missing_required_field/
    ├── doc_id_path_mismatch/
    ├── duplicate_doc_id/
    ├── status_overclaim/
    ├── related_entry_invalid/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs/meta-block
```

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `check_meta_blocks.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator checks metadata blocks deterministically without executing content.
- [ ] Required-field profile is documented outside the validator implementation or clearly marked proposed.
- [ ] Validator detects status/truth-posture overclaims without deciding truth itself.
- [ ] Link resolution is delegated to link-check tooling where appropriate.
- [ ] Ignore rules include reason, owner, scope, and review posture.
- [ ] Reports and receipts are written only to accepted non-authority roots.
- [ ] Validator does not edit docs without a separate explicit change process.
- [ ] Tests use synthetic fixtures and do not require network access by default.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual meta-block scripts, required-field profile, ignore files, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
