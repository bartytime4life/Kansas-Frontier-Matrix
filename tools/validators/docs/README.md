<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-readme
title: tools/validators/docs README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator-parent; markdown-qa; non-authoritative
owning_root: tools/
responsibility: proposed parent/index lane for documentation validators that check Markdown metadata, links, anchors, freshness, terminology, truth-label posture, implementation-overclaim signals, and docs-QA reports without deciding doctrine, evidence sufficiency, source admissibility, policy exceptions, directory-rule exceptions, release approval, or publication
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../docs/README.md
  - ./link-check/README.md
  - ./meta-block/README.md
  - ./stale-scan/README.md
  - ./terminology-parity/README.md
  - ./truth-label-lint/README.md
  - ../../../docs/README.md
  - ../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../docs/adr/
  - ../../../policy/
  - ../../../contracts/
  - ../../../schemas/
  - ../../../data/receipts/validation/
  - ../../../artifacts/qa/
  - ../../../tests/
notes:
  - "This README documents a proposed parent lane for docs validators. It does not confirm executable files."
  - "Documentation validators can report metadata, link, freshness, terminology, and truth-label QA issues. They cannot decide that a claim is true, a source is admissible, a policy exception is valid, a Directory Rules exception is valid, or a release is approved."
  - "Child README lanes exist for link-check, meta-block, stale-scan, terminology-parity, and truth-label-lint; executable behavior remains NEEDS VERIFICATION unless verified separately."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--validators-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/` is the proposed parent/index lane for documentation validators: metadata blocks, links, anchors, freshness, terminology parity, truth-label linting, implementation-overclaim checks, and docs-QA reports.

---

## Purpose

`tools/validators/docs/` exists to group validator lanes that inspect documentation hygiene and evidence-posture signals across repository Markdown.

The durable KFM question for this parent lane is:

> Do repository documents carry enough metadata, link integrity, freshness posture, terminology consistency, and truth-label discipline for maintainers to review them without confusing QA signals for doctrine, evidence closure, policy approval, release approval, or publication?

The answer should be deterministic validation results and, where configured, docs QA reports. This parent lane should not edit doctrine, decide whether a claim is true, validate evidence sufficiency, decide source admissibility, approve policy exceptions, override Directory Rules, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent docs validator executables | **PROPOSED / NEEDS VERIFICATION** | No parent runner or script name is claimed here. |
| Child README lanes | **CONFIRMED README siblings / executable proposed** | `link-check/`, `meta-block/`, `stale-scan/`, `terminology-parity/`, and `truth-label-lint/` README files exist. |
| Parent docs tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling may check metadata, links, warnings, drift, overclaims, and house style, but cannot decide truth, admissibility, release approval, or Directory Rules exceptions. |
| Validator scope profile | **PROPOSED / NEEDS VERIFICATION** | Exact required fields, freshness thresholds, allowed truth labels, terminology profile, ignore rules, and report destinations must be accepted outside this README before CI enforcement. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, artifacts, or receipts are wired. |

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `link-check/` | Do documentation links, anchors, image refs, citation refs, and external-link postures resolve as configured? | README confirmed; executable proposed. |
| `meta-block/` | Does a document carry a parseable, internally consistent `KFM_META_BLOCK_V2` or accepted metadata block profile? | README confirmed; executable proposed. |
| `stale-scan/` | Does a document show stale metadata, overdue review posture, expired caveats, unresolved TODOs, or implementation-overclaim drift? | README confirmed; executable proposed. |
| `terminology-parity/` | Does a document use KFM terminology, casing, source-role vocabulary, truth-label terms, and authority pointers consistently? | README confirmed; executable proposed. |
| `truth-label-lint/` | Does a document use truth labels in a way that signals evidence posture and verification boundary without overclaiming? | README confirmed; executable proposed. |

Future child lanes should be added only when they cover a distinct docs-QA invariant. Avoid creating a new child lane for every document type unless it has a separate validator contract, fixtures, and report semantics.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs validator parent/index | `tools/validators/docs/` |
| Shared validator plumbing | `tools/validators/_common/` |
| General docs tooling | `tools/docs/` |
| Documentation content | `docs/` and each owning responsibility root |
| Documentation registries and backlogs | `docs/registers/` or accepted docs registry homes |
| Doctrine, ADRs, runbooks, standards | owning docs lanes under `docs/` |
| Policy rules | `policy/` |
| Contracts and schemas | `contracts/`, `schemas/` |
| Evidence and proof support | `data/proofs/` and accepted evidence/proof roots |
| Receipts from validation runs | `data/receipts/validation/` or accepted receipt home |
| QA artifacts and summaries | `artifacts/qa/` when non-authoritative and non-trust-bearing |
| Tests and fixtures | `tests/` and accepted fixture conventions |
| Release records | `release/` |
| Published public-safe docs/artifacts | accepted publication roots, not validator lanes |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** parent docs-validator runner code may live here only when it orchestrates child docs validators and preserves their boundaries.
- **NEEDS VERIFICATION:** exact executable names, accepted profiles, child runner behavior, fixture paths, report destinations, ignore rules, receipts, and CI wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, ADR authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/` include:

- parent README and navigation for docs validator lanes;
- optional orchestration wrappers that invoke child validators without redefining their logic;
- shared docs-validator configuration only when it is not better placed in `_common/` or an accepted config root;
- profile declarations that are explicitly accepted by docs stewards or marked **PROPOSED**;
- synthetic fixture references and test-surface guidance;
- docs-QA summary conventions that route reports to accepted non-authority roots;
- handoff guidance for steward review, verification backlog entries, ADR proposals, and correction follow-up.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
| Directory Rules exceptions | accepted ADR or governance lane |
| Policy rules | `policy/` |
| Contracts or schemas | `contracts/`, `schemas/` |
| EvidenceBundle validation | evidence/proof validator lanes and proof roots |
| Source-admissibility decisions | source registry, policy, review, and governance lanes |
| Receipts | `data/receipts/` |
| Proofs | `data/proofs/` |
| Release decisions or release manifests | `release/` |
| Published docs or public site output | accepted public/docs publishing root |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Docs validator posture

Docs validators are QA aids, not governance approval.

A passing docs-validator run means only that the configured checks did not detect configured documentation hygiene issues at scan time. It does not mean:

- the document is authoritative;
- the claims in the document are true;
- the evidence chain actually resolves;
- the source is admissible;
- the policy posture is correct;
- the implementation maturity is proven;
- the release state is approved;
- the document is safe for public publication;
- the path satisfies Directory Rules without further review.

A failing docs-validator run should route to one of these actions:

- fix metadata, links, anchors, terminology, or truth-label posture;
- weaken overconfident implementation or release claims;
- add a verification-backlog item;
- open a steward review task;
- propose an ADR for unresolved terminology, directory, policy, or authority conflict;
- add a documented ignore rule with owner, reason, scope, and review posture.

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `DOCS_VALIDATION_PASS` | Configured docs validator checks passed. |
| `DOCS_VALIDATION_FAIL` | One or more configured docs validator checks failed. |
| `CHILD_VALIDATOR_MISSING` | Expected child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `DOCS_PROFILE_MISSING` | Required docs validation profile is absent. |
| `DOCS_PROFILE_CONFLICT` | Profiles disagree about metadata, terminology, truth labels, freshness, or report handling. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `AUTHORITY_CONFUSION` | Docs text or validator output implies authority the artifact does not hold. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/docs/
├── README.md
├── test_docs_validator_parent.py
└── fixtures/
    ├── valid_docs_validator_bundle/
    ├── missing_child_validator/
    ├── conflicting_profiles/
    ├── invalid_report_destination/
    ├── authority_confusing_output/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs
```

```bash
python tools/validators/docs/run_docs_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_docs_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Parent lane uses accepted profiles rather than hidden tool-only doctrine.
- [ ] Reports and receipts are written only to accepted non-authority roots.
- [ ] Docs validators do not edit docs without a separate explicit change process.
- [ ] QA findings are routed to steward review, verification backlog, or ADR when needed.
- [ ] Ignore rules include reason, owner, scope, and review posture.
- [ ] Passing checks are not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use synthetic fixtures and do not require network access by default.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file and parent index for docs validator child lanes. |
| Next smallest safe change | Verify actual parent runner, child validator scripts, accepted docs-validation profiles, ignore rules, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
