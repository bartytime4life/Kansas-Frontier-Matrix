<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-readme
title: tools/validators/docs README
type: README
version: v0.4
status: draft; two-bounded-child-executables; remaining-children-proposed
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-08-06
policy_label: repository-facing; docs-validator-parent; markdown-qa; non-authoritative
owning_root: tools/
responsibility: parent/index lane for documentation validators that check Markdown metadata, links, anchors, graph connectivity, backlinks, reachability, freshness, terminology, truth-label posture, implementation-overclaim signals, and docs-QA reports without deciding doctrine, evidence sufficiency, source admissibility, policy exceptions, directory-rule exceptions, release approval, or publication
truth_posture: CONFIRMED bounded local-only link-check and document-graph executables with synthetic tests / PROPOSED remaining child executables and broader docs-QA orchestration / NEEDS VERIFICATION hosted exact-head results, historical graph classification, and required-check coupling
related:
  - ../README.md
  - ../_common/README.md
  - ../../docs/README.md
  - ./link-check/README.md
  - ./document-graph/README.md
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
  - "This parent lane contains two bounded local-only executables: link-check and document-graph; the remaining child lanes are README-only proposals."
  - "Documentation validators can report metadata, link, graph, freshness, terminology, and truth-label QA issues. They cannot decide that a claim is true, a source is admissible, a policy exception is valid, a Directory Rules exception is valid, or a release is approved."
  - "The document graph delegates exact target, fragment, case, and path QA to link-check and consumes only bounded identity/relationship metadata."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--validators-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/` is the parent/index lane for documentation validators: metadata blocks, local links and anchors, documentation-graph connectivity, backlinks, generated Maps of Content, freshness, terminology parity, truth-label linting, implementation-overclaim checks, and docs-QA reports.

---

## Purpose

`tools/validators/docs/` groups validator lanes that inspect documentation hygiene and evidence-posture signals across repository Markdown.

The durable KFM question for this parent lane is:

> Do repository documents carry enough metadata, link integrity, graph connectivity, freshness posture, terminology consistency, and truth-label discipline for maintainers to review them without confusing QA signals for doctrine, evidence closure, policy approval, release approval, or publication?

The answer should be deterministic validation results and, where configured, docs QA reports. This parent lane must not edit doctrine, decide whether a claim is true, validate evidence sufficiency, decide source admissibility, approve policy exceptions, override Directory Rules, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/README.md` | **CONFIRMED** | Parent index and authority boundary. |
| Parent docs validator executable | **PROPOSED / NEEDS VERIFICATION** | No parent runner is claimed here. |
| Bounded child executables | **CONFIRMED mixed scope** | `link-check/` validates bounded local targets; `document-graph/` builds a bounded connectivity/backlink/reachability projection. |
| README-only child lanes | **CONFIRMED proposals** | `meta-block/`, `stale-scan/`, `terminology-parity/`, and `truth-label-lint/` do not yet claim executables. |
| Parent docs tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling may check metadata, links, warnings, drift, overclaims, and house style, but cannot decide truth, admissibility, release approval, or Directory Rules exceptions. |
| Validator scope profile | **PROPOSED / NEEDS VERIFICATION** | Required fields, freshness thresholds, allowed truth labels, terminology profiles, ignore rules, graph baselines, and report destinations require steward acceptance before stricter CI enforcement. |
| CI wiring | **CONFIRMED definitions / NEEDS VERIFICATION execution** | `link-check.yml` and `docs-document-graph.yml` carry read-only changed-area checks; hosted exact-head results and required-check coupling remain separate evidence. |

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `link-check/` | Do local inline and defined reference-style Markdown file, directory, image, and fragment targets resolve without network access? | Bounded executable and synthetic suite confirmed; external URLs remain unverified. |
| `document-graph/` | How are scoped Markdown documents connected through local navigation and bounded metadata relationships, and which current changes introduce duplicate identity, broken declared relations, unreachable documents, or registry drift? | Bounded executable, synthetic suite, generated MOC/backlink workbench, and changed-file ratchet confirmed; whole-repository historical classification remains pending. |
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
| Tests and fixtures | `tests/` and fixture conventions |
| Release records | `release/` |
| Published public-safe docs/artifacts | accepted publication roots, not validator lanes |

Safe interpretation:

- **CONFIRMED:** this README and the named bounded child executables exist in the proposed change state.
- **PROPOSED:** a parent docs-validator runner may live here only when it delegates to child validators and preserves their boundaries.
- **NEEDS VERIFICATION:** accepted profiles, historical graph baseline, ignore files, report destinations, validation receipts, hosted exact-head results, and required-check wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, ADR authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/` include:

- parent README and navigation for docs validator lanes;
- bounded child validators with distinct QA contracts;
- optional orchestration wrappers that invoke child validators without redefining their logic;
- shared docs-validator configuration only when it is not better placed in `_common/` or an accepted config root;
- profile declarations that are explicitly accepted by docs stewards or marked **PROPOSED**;
- synthetic fixture references and test-surface guidance;
- docs-QA summary conventions that route reports to accepted non-authority roots; and
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
- the document is safe for public publication; or
- the path satisfies Directory Rules without further review.

A failing docs-validator run should route to one of these actions:

- fix metadata, links, anchors, graph relationships, terminology, or truth-label posture;
- weaken overconfident implementation or release claims;
- add a verification-backlog item;
- open a steward review task;
- propose an ADR for unresolved terminology, directory, policy, or authority conflict; or
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
| `DOCS_PROFILE_CONFLICT` | Profiles disagree about metadata, terminology, truth labels, freshness, graph baseline, or report handling. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `AUTHORITY_CONFUSION` | Docs text or validator output implies authority the artifact does not hold. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Run the bounded child suites independently:

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose
```

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/document-graph \
  --pattern 'test_*.py' \
  --verbose
```

A future parent runner may orchestrate the child lanes after profile precedence,
ignore rules, report destinations, and outcome composition are accepted. No
parent runner is claimed by this README.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Parent lane uses accepted profiles rather than hidden tool-only doctrine.
- [ ] Graph reports remain non-authoritative and do not become documentation or registry truth.
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
| Last reviewed | 2026-08-06 |
| Review state | Draft parent index with bounded link-check and document-graph child executables. |
| Next smallest safe change | Classify the first whole-repository graph report, then implement the separate meta-block validator without making either output authority. |
