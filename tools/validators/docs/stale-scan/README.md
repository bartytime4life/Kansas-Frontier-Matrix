<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-stale-scan-readme
title: tools/validators/docs/stale-scan README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator; stale-scan; freshness-qa; non-authoritative
owning_root: tools/
responsibility: proposed documentation staleness/freshness validator lane for updated-date posture, review-age signals, status drift, implementation-overclaim, stale related links, TODO/owner posture, release/reference freshness, and docs-QA reports without deciding doctrine, evidence sufficiency, source admissibility, or release approval
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../link-check/README.md
  - ../meta-block/README.md
  - ../../../docs/README.md
  - ../../../../docs/README.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../docs/adr/
  - ../../../../docs/architecture/trust-membrane.md
  - ../../../../data/receipts/validation/
  - ../../../../artifacts/qa/
  - ../../../../tests/
notes:
  - "This README documents a proposed docs stale-scan validator lane. It does not confirm executable files."
  - "A stale-scan checker can report stale dates, overdue review posture, unresolved TODOs, broken freshness promises, status overclaims, and potentially drifted references. It cannot decide that a claim is false, a source is inadmissible, a policy exception is valid, or a release is approved."
  - "Freshness findings are time-sensitive QA signals and should route to steward review, not automatic doctrinal edits."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs/stale-scan

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--stale--scan-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/stale-scan/` is the proposed documentation freshness/staleness validator lane for Markdown files: `updated` dates, last-reviewed fields, stale TODOs, owner/status drift, implementation-maturity overclaims, stale references, release/freshness caveats, review cadence, and docs-QA reports.

---

## Purpose

`tools/validators/docs/stale-scan/` exists for freshness and drift checks over repository documentation and README-style Markdown.

The durable KFM question for this lane is:

> Does a document show signs of stale metadata, stale review posture, outdated implementation claims, expired caveats, unresolved owner/TODO fields, or references that need steward review, without treating the scan as a truth or release decision?

The answer should be a deterministic validation result and, where configured, a docs QA report. It should not edit doctrine, approve ADRs, validate evidence sufficiency, decide source admissibility, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/stale-scan/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Stale-scan validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Parent docs-tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling may detect missing metadata, required warnings, report drift, and implementation-maturity overclaims, but cannot decide truth, admissibility, or release approval. |
| Related docs validator lanes | **CONFIRMED README siblings / executable proposed** | `link-check/` and `meta-block/` README lanes exist; executable behavior remains unverified. |
| Staleness thresholds | **PROPOSED / NEEDS VERIFICATION** | Review age, warning expiry, and stale-reference thresholds must be accepted by docs stewards before CI enforcement. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, or artifact uploads are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs stale-scan validator entrypoints | `tools/validators/docs/stale-scan/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Link-check validator lane | `tools/validators/docs/link-check/` |
| Meta-block validator lane | `tools/validators/docs/meta-block/` |
| General docs tooling | `tools/docs/` |
| Documentation content | `docs/` and each owning responsibility root |
| Documentation registry and backlog | `docs/registers/` or accepted docs registry home |
| Doctrine, ADRs, runbooks, standards | owning docs lanes under `docs/` |
| Policy rules | `policy/` |
| Contracts and schemas | `contracts/`, `schemas/` |
| Receipts from validation runs | `data/receipts/validation/` or accepted receipt home |
| QA artifacts and summaries | `artifacts/qa/` when non-authoritative and non-trust-bearing |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** stale-scan validator code may live here when it checks freshness signals, review cadence, and drift posture.
- **NEEDS VERIFICATION:** exact executable names, freshness thresholds, required-field profiles, fixture paths, report destinations, ignore rules, and CI wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, ADR authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/stale-scan/` include checks that:

- detect old or missing `updated`, `last_reviewed`, or equivalent review fields where the configured profile requires them;
- flag stale TODO owner fields and unresolved placeholder owners;
- detect documents whose `status` or truth-posture labels appear stronger than nearby evidence supports;
- detect stale warnings, caveats, ADR references, verification-backlog pointers, or review-expiry markers;
- detect docs that claim current implementation behavior without a recent verification basis;
- identify links or related entries that should be delegated to `link-check/` for resolution;
- identify metadata-block drift that should be delegated to `meta-block/` for parse/field checks;
- compare generated docs QA reports against prior reports without treating either as doctrine;
- emit deterministic docs QA summaries and validation receipts where configured;
- support explicit ignore rules with owner, reason, scope, and review posture.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/stale-scan/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
| Freshness policy as doctrine | accepted docs standard or ADR, not tool-only convention |
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

## Stale-scan posture

Stale scanning is documentation QA, not governance approval.

A passing stale-scan check means only that the configured validator did not detect configured freshness or drift issues at scan time. It does not mean:

- the document is authoritative;
- the claims in the document are true;
- the document is up to date in every material way;
- the source is admissible;
- the policy posture is correct;
- the implementation maturity is proven;
- the release state is approved;
- the document is safe for public publication.

A failing stale-scan check should route to one of these actions:

- update review metadata after a real steward review;
- weaken overconfident status or truth-posture claims;
- add a verification-backlog item;
- refresh stale related references;
- add a documented ignore rule with owner and review posture;
- route the document to an owning steward rather than auto-editing doctrine.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `DOC_STALE_SCAN_PASS` | Configured stale-scan checks passed. |
| `DOC_STALE_SCAN_FAIL` | One or more configured stale-scan checks failed. |
| `UPDATED_FIELD_MISSING` | Required update/review metadata is absent. |
| `REVIEW_WINDOW_EXPIRED` | Document exceeds the configured review-age threshold. |
| `OWNER_PLACEHOLDER_STALE` | Owner/TODO placeholder remains beyond accepted posture. |
| `STATUS_OVERCLAIM` | Status/truth posture appears stronger than evidence supports. |
| `IMPLEMENTATION_CLAIM_STALE` | Current-behavior claim lacks recent verification support. |
| `WARNING_OR_CAVEAT_EXPIRED` | Warning, caveat, or temporary exception needs review. |
| `RELATED_REFERENCE_STALE` | Related path, ADR, registry, or backlog pointer may need review. |
| `DELEGATE_TO_LINK_CHECK` | Link resolution should be checked by the link-check lane. |
| `DELEGATE_TO_META_BLOCK` | Metadata parse/field issue should be checked by the meta-block lane. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/docs/stale-scan/
├── README.md
├── test_docs_stale_scan.py
└── fixtures/
    ├── valid_recent_review/
    ├── missing_updated_field/
    ├── expired_review_window/
    ├── stale_owner_placeholder/
    ├── status_overclaim/
    ├── stale_implementation_claim/
    ├── expired_caveat/
    ├── delegate_to_link_check/
    ├── delegate_to_meta_block/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs/stale-scan
```

```bash
python tools/validators/docs/stale-scan/scan_stale_docs.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `scan_stale_docs.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator uses accepted freshness thresholds rather than hidden tool-only policy.
- [ ] Validator reports staleness without deciding doctrine, evidence sufficiency, or release approval.
- [ ] Validator detects implementation-maturity overclaims without asserting the correct implementation state unless verified.
- [ ] Link resolution is delegated to link-check tooling where appropriate.
- [ ] Metadata parse/field checks are delegated to meta-block tooling where appropriate.
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
| Next smallest safe change | Verify actual stale-scan scripts, freshness thresholds, ignore files, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
