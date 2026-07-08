<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-link-check-readme
title: tools/validators/docs/link-check README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator; link-check; markdown-qa; non-authoritative
owning_root: tools/
responsibility: proposed documentation link-check validator lane for Markdown link, anchor, path, citation, redirect, generated-report, and docs-QA checks without deciding doctrine, evidence sufficiency, source admissibility, or release approval
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/README.md
  - ../../../../docs/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/architecture/trust-membrane.md
  - ../../../../docs/adr/
  - ../../../../data/receipts/validation/
  - ../../../../artifacts/qa/
  - ../../../../tests/
notes:
  - "This README documents a proposed docs link-check validator lane. It does not confirm executable files."
  - "A link checker can report missing files, broken anchors, malformed URLs, stale redirects, and unresolved citations. It cannot decide that a claim is true, a source is admissible, a policy exception is valid, or a release is approved."
  - "The parent docs-tooling README confirms documentation tooling may check links and anchors while keeping doctrine and release authority outside tools code."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs/link-check

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--link--check-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/link-check/` is the proposed documentation link-check validator lane for Markdown files: intra-repo links, relative paths, anchors, image references, generated citation references, external-link posture, redirect notes, allowlists, ignore rules, and docs-QA reports.

---

## Purpose

`tools/validators/docs/link-check/` exists for link and anchor validation of repository documentation.

The durable KFM question for this lane is:

> Do documentation links resolve to the intended local files, anchors, references, or approved external targets without implying that link existence proves truth, policy approval, evidence closure, or release state?

The answer should be a deterministic validation result and, where configured, a docs QA report. It should not edit doctrine, approve ADRs, validate evidence sufficiency, decide source admissibility, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/link-check/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Link-check validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Parent docs-tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling may check links and anchors but cannot decide truth, admissibility, or release approval. |
| `tools/validators/docs/README.md` | **NOT FOUND in this task** | A parent validator README may be useful later, but this file does not create that parent authority. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, or artifact uploads are wired. |
| External-link status | **NEEDS VERIFICATION** | External link availability is time-sensitive and should be checked only by a configured validator run. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs link-check validator entrypoints | `tools/validators/docs/link-check/` |
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
- **PROPOSED:** link-check validator code may live here when it checks links, paths, anchors, and reference hygiene.
- **NEEDS VERIFICATION:** exact executable names, configuration files, ignore rules, fixture paths, CI wiring, and report destinations.
- **DENY:** using this folder as docs content authority, doctrine authority, ADR authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/link-check/` include checks that:

- validate relative Markdown links against the current repository tree;
- validate fragment anchors for headings and explicit HTML anchors;
- detect links to files that moved, were renamed, or never existed;
- detect image references that point to missing local assets;
- distinguish internal repository links from external URLs;
- record external-link checks as time-sensitive results rather than permanent truth;
- support allowlists, denylists, retry rules, and ignore rules with explicit reasons;
- detect generated citation/reference fragments that no longer resolve;
- emit deterministic docs QA summaries and validation receipts where configured;
- preserve a correction path for renamed docs, stale anchors, and broken references.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/link-check/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
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

## Link-check posture

Link checking is QA, not governance approval.

A passing link check means only that the configured validator could resolve the checked references at the time of the run. It does not mean:

- the linked document is authoritative;
- the linked claim is true;
- the source is admissible;
- the policy posture is correct;
- the release state is approved;
- the document is safe for public publication.

A failing link check should route to one of these actions:

- fix the path or anchor;
- update the renamed target;
- add a documented ignore rule with owner and expiry;
- quarantine or remove a stale public-facing reference;
- open a docs verification backlog item where the target authority is unclear.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `DOC_LINK_CHECK_PASS` | Configured link checks passed. |
| `DOC_LINK_CHECK_FAIL` | One or more configured link checks failed. |
| `LOCAL_TARGET_MISSING` | Local file or asset target does not exist. |
| `ANCHOR_MISSING` | Target file exists but requested fragment/anchor does not resolve. |
| `EXTERNAL_TARGET_UNVERIFIED` | External URL was not checked or could not be treated as stable. |
| `EXTERNAL_TARGET_FAILED` | External URL check failed during a configured run. |
| `CITATION_REF_UNRESOLVED` | Generated or structured citation/reference marker does not resolve. |
| `IGNORED_WITH_REASON` | Failure was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `DOC_AUTHORITY_CONFUSION` | Link text or target implies authority the linked artifact does not hold. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/docs/link-check/
├── README.md
├── test_docs_link_check.py
└── fixtures/
    ├── valid_local_links/
    ├── missing_local_target/
    ├── missing_anchor/
    ├── missing_image_asset/
    ├── unresolved_citation_ref/
    ├── ignored_with_reason/
    ├── expired_ignore_rule/
    └── authority_confusing_link_text/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs/link-check
```

```bash
python tools/validators/docs/link-check/check_links.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `check_links.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator checks local paths and anchors deterministically.
- [ ] External link checks are marked time-sensitive and not treated as permanent truth.
- [ ] Ignore rules include reason, owner, scope, and review/expiry posture.
- [ ] Link text does not imply doctrine, evidence, policy, or release authority where none exists.
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
| Next smallest safe change | Verify actual link-check scripts, configuration, ignore files, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
