<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-truth-label-lint-readme
title: tools/validators/docs/truth-label-lint README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-evidence-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator; truth-label-lint; evidence-posture-qa; non-authoritative
owning_root: tools/
responsibility: proposed documentation truth-label lint validator lane for CONFIRMED, PROPOSED, NEEDS VERIFICATION, UNKNOWN, CONFLICTED, DENY, ABSTAIN, and related evidence-posture label hygiene without deciding doctrine, evidence sufficiency, source admissibility, policy exceptions, or release approval
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../link-check/README.md
  - ../meta-block/README.md
  - ../stale-scan/README.md
  - ../terminology-parity/README.md
  - ../../../docs/README.md
  - ../../../../docs/README.md
  - ../../../../docs/doctrine/evidence-first.md
  - ../../../../docs/doctrine/truth-posture.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../docs/adr/
  - ../../../../data/receipts/validation/
  - ../../../../artifacts/qa/
  - ../../../../tests/
notes:
  - "This README documents a proposed docs truth-label lint validator lane. It does not confirm executable files."
  - "A truth-label linter can report missing labels, overconfident labels, malformed labels, stale labels, inconsistent nearby wording, and labels that need evidence-review. It cannot decide that the underlying claim is true, false, admissible, policy-approved, or release-approved."
  - "Evidence First doctrine says consequential claims either resolve to EvidenceBundle support or abstain; this validator only checks documentation label hygiene around that posture."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs/truth-label-lint

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--truth--label--lint-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/truth-label-lint/` is the proposed documentation truth-label lint validator lane for Markdown files: truth-label presence, casing, allowed vocabulary, overclaim detection, evidence-posture alignment, stale labels, contradiction signals, and docs-QA reports.

---

## Purpose

`tools/validators/docs/truth-label-lint/` exists for truth-label hygiene checks over repository documentation and README-style Markdown.

The durable KFM question for this lane is:

> Does a document use truth labels in a way that accurately signals evidence posture, implementation maturity, and verification boundary without letting the lint result decide truth by itself?

The answer should be a deterministic validation result and, where configured, a docs QA report. It should not edit doctrine, decide whether a claim is true, validate evidence sufficiency, decide source admissibility, approve policy exceptions, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/truth-label-lint/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Truth-label lint executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Evidence-first doctrine | **CONFIRMED in repo evidence / draft** | `docs/doctrine/evidence-first.md` states consequential claims require resolvable evidence or abstain. |
| Truth-posture doctrine | **CONFIRMED in repo evidence / draft** | `docs/doctrine/truth-posture.md` exists, but exact truth-label vocabulary should be verified against accepted doctrine and operating contract before CI enforcement. |
| Parent docs-tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling can detect documentation drift and overclaims but cannot decide truth, admissibility, or release approval. |
| Related docs validator lanes | **CONFIRMED README siblings / executable proposed** | `link-check/`, `meta-block/`, `stale-scan/`, and `terminology-parity/` README lanes exist; executable behavior remains unverified. |
| Accepted truth-label profile | **PROPOSED / NEEDS VERIFICATION** | Allowed labels, aliases, casing, and context rules must be accepted outside this README before CI enforcement. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, or artifact uploads are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs truth-label lint validator entrypoints | `tools/validators/docs/truth-label-lint/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Link-check validator lane | `tools/validators/docs/link-check/` |
| Meta-block validator lane | `tools/validators/docs/meta-block/` |
| Stale-scan validator lane | `tools/validators/docs/stale-scan/` |
| Terminology-parity validator lane | `tools/validators/docs/terminology-parity/` |
| General docs tooling | `tools/docs/` |
| Documentation content | `docs/` and each owning responsibility root |
| Truth posture and evidence doctrine | accepted doctrine / operating-contract lanes under `docs/` |
| Evidence/proof support | `data/proofs/` and accepted evidence/proof roots |
| Receipts from validation runs | `data/receipts/validation/` or accepted receipt home |
| QA artifacts and summaries | `artifacts/qa/` when non-authoritative and non-trust-bearing |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** truth-label lint code may live here when it checks label spelling, casing, placement, and consistency with a declared profile.
- **NEEDS VERIFICATION:** exact executable names, accepted label profile, fixture paths, report destinations, ignore rules, and CI wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, truth authority, evidence validator, source-admissibility authority, policy authority, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/truth-label-lint/` include checks that:

- detect missing truth labels where the configured profile requires one;
- validate canonical spelling and casing for labels such as `CONFIRMED`, `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`, `CONFLICTED`, `DENY`, and `ABSTAIN` where accepted by the active profile;
- flag overconfident labels, such as `CONFIRMED` near text that also says implementation, schema, fixture, runtime, or CI behavior has not been verified;
- flag unsupported implementation-maturity claims in README status tables;
- flag stale labels where a review date, ADR reference, or verification backlog item says the posture may have changed;
- detect conflicting truth labels in the same paragraph, table row, or metadata block;
- check that generated docs summaries do not upgrade `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` statements into `CONFIRMED` prose;
- delegate metadata-field issues to `meta-block/`;
- delegate stale review posture to `stale-scan/`;
- delegate canonical term issues to `terminology-parity/`;
- emit deterministic docs QA summaries and validation receipts where configured.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/truth-label-lint/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
| Truth-label policy as doctrine | accepted doctrine, operating contract, or ADR, not tool-only convention |
| EvidenceBundle validation | evidence/proof validator lanes and proof roots |
| Policy rules | `policy/` |
| Contracts or schemas | `contracts/`, `schemas/` |
| Receipts | `data/receipts/` |
| Proofs | `data/proofs/` |
| Release decisions or release manifests | `release/` |
| Published docs or public site output | accepted public/docs publishing root |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Truth-label lint posture

Truth-label linting is documentation QA, not governance approval.

A passing truth-label lint check means only that the configured validator did not detect configured label hygiene issues at scan time. It does not mean:

- the document is authoritative;
- the claims in the document are true;
- the evidence chain actually resolves;
- the source is admissible;
- the policy posture is correct;
- the implementation maturity is proven;
- the release state is approved;
- the document is safe for public publication.

A failing truth-label lint check should route to one of these actions:

- downgrade or qualify an overconfident label;
- add a missing truth label;
- link to evidence, proof, review, or verification backlog where required;
- open a docs verification backlog item;
- propose an ADR for unresolved label vocabulary conflict;
- add a documented ignore rule with owner, reason, scope, and review posture.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `DOC_TRUTH_LABEL_LINT_PASS` | Configured truth-label checks passed. |
| `DOC_TRUTH_LABEL_LINT_FAIL` | One or more configured truth-label checks failed. |
| `TRUTH_LABEL_MISSING` | Required truth label is absent. |
| `TRUTH_LABEL_UNKNOWN` | Label is outside the accepted profile. |
| `TRUTH_LABEL_CASING_MISMATCH` | Label spelling or casing is outside the accepted profile. |
| `TRUTH_LABEL_OVERCLAIM` | Label appears stronger than nearby evidence posture supports. |
| `TRUTH_LABEL_CONFLICT` | Nearby labels conflict without explanation. |
| `IMPLEMENTATION_MATURITY_OVERCLAIM` | Current-behavior, schema, fixture, runtime, or CI claim lacks verified support. |
| `EVIDENCE_POSTURE_MISSING` | Evidence basis or verification boundary is absent where required. |
| `DELEGATE_TO_META_BLOCK` | Metadata label issue should be checked by the meta-block lane. |
| `DELEGATE_TO_STALE_SCAN` | Staleness or review-age issue should be checked by the stale-scan lane. |
| `DELEGATE_TO_TERMINOLOGY_PARITY` | Term/casing issue should be checked by the terminology-parity lane. |
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
tests/validators/docs/truth-label-lint/
├── README.md
├── test_docs_truth_label_lint.py
└── fixtures/
    ├── valid_truth_labels/
    ├── missing_truth_label/
    ├── unknown_truth_label/
    ├── casing_mismatch/
    ├── truth_label_overclaim/
    ├── truth_label_conflict/
    ├── implementation_maturity_overclaim/
    ├── evidence_posture_missing/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs/truth-label-lint
```

```bash
python tools/validators/docs/truth-label-lint/lint_truth_labels.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `lint_truth_labels.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator uses an accepted truth-label profile rather than hidden tool-only doctrine.
- [ ] Validator reports label drift without deciding truth by itself.
- [ ] `CONFIRMED` is not allowed to mask unverified implementation, schema, fixture, runtime, CI, release, or public-surface claims.
- [ ] Missing evidence posture is routed to verification backlog or steward review.
- [ ] Metadata label issues are delegated to meta-block tooling where appropriate.
- [ ] Stale review and label-age checks are delegated to stale-scan tooling where appropriate.
- [ ] Terminology/casing checks are delegated to terminology-parity tooling where appropriate.
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
| Next smallest safe change | Verify actual truth-label lint scripts, accepted label profile, ignore files, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
