<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-readme
title: tools/validators/docs README
type: README
version: v0.6
status: draft; four-bounded-child-executables; remaining-children-proposed
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-08-07
policy_label: repository-facing; docs-validator-parent; markdown-qa; non-authoritative
owning_root: tools/
responsibility: parent and navigation lane for bounded documentation validators covering local links, graph connectivity, metadata blocks, freshness, terminology, truth-label posture, and documentation QA without deciding doctrine, evidence sufficiency, source admissibility, policy exceptions, release approval, or publication
truth_posture: CONFIRMED bounded local-only link-check, document-graph, meta-block, and stale-scan executables with synthetic tests / PROPOSED remaining child executables and parent orchestration / NEEDS VERIFICATION hosted exact-head results, historical baselines, and required-check coupling
related:
  - ../README.md
  - ../_common/README.md
  - ./link-check/README.md
  - ./document-graph/README.md
  - ./meta-block/README.md
  - ./stale-scan/README.md
  - ./terminology-parity/README.md
  - ./truth-label-lint/README.md
  - ../../../docs/README.md
  - ../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../control_plane/document_registry.yaml
  - ../../../tests/validators/docs/
notes:
  - "This parent lane contains four bounded local-only executables: link-check, document-graph, meta-block, and stale-scan."
  - "Documentation validators emit QA projections and cannot create truth, source admission, policy, review, release, or publication authority."
  - "Link resolution, graph connectivity, metadata conformance, and freshness review signals remain distinct validator responsibilities."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/docs/`

> **Purpose.** Group deterministic documentation QA lanes while keeping each
> validator's scope, outcome grammar, evidence boundary, and non-effects
> explicit.

## Status

| Surface | State | Notes |
|---|---|---|
| Parent README | **CONFIRMED** | Navigation and authority boundary only; no parent executable is claimed. |
| `link-check/` | **CONFIRMED bounded executable** | Local inline/reference links, files, directories, images, and fragments; external URLs remain unverified. |
| `document-graph/` | **CONFIRMED bounded executable** | Nodes, typed edges, backlinks, reachability, generated MOCs, and registry parity. |
| `meta-block/` | **CONFIRMED bounded executable** | `KFM_META_BLOCK_V2` structure plus review-only registry-delta candidates. |
| `stale-scan/` | **CONFIRMED bounded executable** | Explicit-as-of freshness, review-age, placeholder-owner, temporal-marker, and review-due signals. |
| `terminology-parity/` | **README-only proposal** | Vocabulary, casing, and source-role consistency. |
| `truth-label-lint/` | **README-only proposal** | Evidence-posture and implementation-overclaim signals. |
| Hosted enforcement | **NEEDS VERIFICATION** | Workflow definitions exist; exact-head runs and required-check coupling remain separate evidence. |

## Responsibility split

| Question | Owning child lane |
|---|---|
| Does a local Markdown target or fragment resolve? | `link-check/` |
| How are documents connected, and which are unreachable or identity-conflicted? | `document-graph/` |
| Is the bounded metadata envelope structurally valid, and what registry review delta follows? | `meta-block/` |
| Is review/freshness posture stale under an explicit as-of date and threshold? | `stale-scan/` |
| Does terminology align with accepted KFM vocabulary? | `terminology-parity/` — proposed |
| Does prose expose truth labels without overclaiming? | `truth-label-lint/` — proposed |

Child validators must delegate rather than silently reimplement another lane's
authority. In particular:

- metadata validation does not become a second link checker;
- document graph construction does not become metadata doctrine;
- stale scanning does not infer truth or current runtime behavior from a date;
- freshness parsing delegates malformed metadata to `meta-block/`; and
- exact local target resolution remains with `link-check/`.

## Authority boundary

Documentation validators are repository QA tools. They may inspect explicit
Markdown, emit deterministic findings, produce non-authoritative summaries, and
route gaps to review. They must not:

- edit documentation or registries without a separate authorized change;
- decide whether a claim is true or an EvidenceBundle is sufficient;
- approve source admission, rights, sensitivity, or policy exceptions;
- create review, release, promotion, publication, correction, or rollback state;
- turn a passing workflow, badge, graph, metadata block, or recent date into authority; or
- write generated QA reports into canonical trust-object homes.

Responsibility-root placement remains:

| Responsibility | Home |
|---|---|
| Validator implementation | `tools/validators/docs/<lane>/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Executable tests and synthetic fixtures | `tests/validators/docs/<lane>/` |
| Read-only CI orchestration | `.github/workflows/` |
| Generated validation receipts | `data/receipts/validation/` when separately emitted |
| Non-authoritative QA reports | `artifacts/qa/` or ephemeral CI output |
| Documentation content | `docs/` and each owning responsibility root |
| Machine document register | `control_plane/document_registry.yaml` |

## Child outcomes

| Lane | Pass | Warn | Fail | Operational error |
|---|---|---|---|---|
| Link check | `DOC_LINK_CHECK_PASS` | informational external/unverified state | target/anchor/path failures | `ERROR` |
| Document graph | `DOC_GRAPH_PASS` | `DOC_GRAPH_WARN` | `DOC_GRAPH_FAIL` | `ERROR` |
| Metadata block | `DOC_META_BLOCK_PASS` | `DOC_META_BLOCK_WARN` | `DOC_META_BLOCK_FAIL` | `ERROR` |
| Freshness scan | `DOC_STALE_SCAN_PASS` | `DOC_STALE_SCAN_WARN` | `DOC_STALE_SCAN_FAIL` | `ERROR` |

A parent outcome grammar remains **PROPOSED** until precedence, waiver rules,
report destinations, and composition semantics are reviewed. No parent runner is
claimed by this README.

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

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/meta-block \
  --pattern 'test_*.py' \
  --verbose
```

```bash
python -m unittest discover \
  --start-directory tests/validators/docs/stale-scan \
  --pattern 'test_*.py' \
  --verbose
```

## Review checklist

- [ ] The child validator has one distinct QA responsibility.
- [ ] The implementation uses explicit bounded inputs and no network by default.
- [ ] Time-dependent scans record an explicit as-of date and thresholds.
- [ ] Current regressions fail closed while inherited debt is classified honestly.
- [ ] Generated outputs remain non-authoritative and review-only.
- [ ] Documentation and registry mutation require a separate authorized action.
- [ ] Passing checks are not described as truth, policy, review, release, or publication approval.
- [ ] Synthetic fixtures cover positive, negative, replay, and failure behavior.
- [ ] Rollback is ordinary Git reversion with no external-state claim.

## Next smallest safe change

Classify the first combined graph, metadata, and freshness reports. Then choose
one of two bounded follow-ups: a steward-reviewed freshness profile for a
specific documentation lane, or the separate terminology-parity validator.
Do not promote advisory freshness defaults into repository-wide required policy
without a reviewed baseline and owner disposition.

[Back to top](#top)
