<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-docs-readme
title: tools/docs README
type: README
version: v0.2
status: draft
owner: TODO-docs-steward-plus-tooling-qa-owner
created: 2026-07-07
updated: 2026-08-24
policy_label: public
owning_root: tools/
responsibility: repo-wide documentation operators, render and normalization helpers, and routing to canonical documentation validators
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../validators/docs/README.md
  - ./wiki/README.md
  - ../../docs/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../tools/qa/README.md
  - ../../tools/ci/README.md
notes:
  - "This README defines the governed boundary for documentation tooling under tools/docs/."
  - "Documentation validator implementation is routed to tools/validators/docs/ under accepted Directory Rule DIR-EXEC-006."
  - "Documentation content belongs under docs/ or the relevant responsibility root; tools/docs/ owns bounded non-validator operators and helpers, not documentation authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/docs

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--tooling-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![authority](https://img.shields.io/badge/content--authority-docs%2F-lightgrey)

> **One-line purpose.** `tools/docs/` owns bounded documentation-specific operators and non-validator helpers such as explicit rendering, normalization, transport, or reviewer-handoff support. Documentation validators live under [`tools/validators/docs/`](../validators/docs/README.md). This lane does **not** own KFM doctrine, documentation authority, policy meaning, schema shape, contracts, or publication decisions.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Documentation tooling contract](#documentation-tooling-contract)
- [Inputs and outputs](#inputs-and-outputs)
- [Current routing](#current-routing)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/docs/` is a tooling lane for documentation operations that need bounded executable support across the repository but are not validator implementations.

It exists because KFM documentation is part of the governed system. Good documentation helps maintainers understand evidence boundaries, responsibility roots, policy posture, source roles, validation gates, release state, correction paths, rollback targets, and implementation uncertainty.

This lane may help produce or check documentation, but it must not blur the authority boundary:

- `docs/` owns human-facing doctrine, architecture, runbooks, ADRs, source documentation, and public-facing documentation content.
- `tools/docs/` owns bounded operators and helpers used to render, normalize, transport, summarize, or inspect those documents.
- [`tools/validators/docs/`](../validators/docs/README.md) owns documentation validator implementations, including metadata, local-link, document-graph, freshness, and opt-in assessment-axis checks.
- `policy/`, `contracts/`, and `schemas/` remain the sources of policy meaning, object-family meaning, and field-level shape.
- `release/`, `data/receipts/`, and `data/proofs/` remain the homes for release decisions and trust artifacts.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/docs/README.md` | **CONFIRMED** | This README defines the lane boundary. |
| [`wiki/`](wiki/README.md) | **CONFIRMED tracked operator surface / PROPOSED use** | The dry-run-first synchronization helper exists; its child README keeps remote execution review-gated and unverified. |
| Documentation validators | **CONFIRMED separate canonical lane** | Implemented documentation checks are indexed under [`tools/validators/docs/`](../validators/docs/README.md), not duplicated here. |
| Additional render, normalization, or index helpers | **NOT CLAIMED** | No additional helper name or implementation status is established by this README. |
| Doctrine authority | **DENY here** | Doctrine lives in `docs/doctrine/` and accepted ADRs, not tool code. |

> [!IMPORTANT]
> Do not treat a documentation tool output as doctrine. A tool can detect missing metadata, unresolved links, bad anchors, broken tables, or mismatched front matter. It cannot decide that a claim is true, a source is admissible, a release is approved, or a directory-rule exception is valid.

[Back to top](#top)

---

## Governance boundary

KFM's documentation tooling must preserve the same trust membrane as the rest of the system:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Documentation helpers can support review and release readiness, but they do not move data or documents across lifecycle states. Publication remains a governed state transition.

### Allowed questions

`tools/docs/` may help answer:

- Does a README contain the expected KFM metadata block?
- Do intra-repo links resolve?
- Are Markdown anchors stable?
- Does a document include required truth-posture warnings?
- Does a generated documentation report differ from the prior report?
- Does a documentation page accidentally claim implementation maturity without evidence labels?
- Does a docs table or badge set follow the expected house pattern?

### Disallowed questions

`tools/docs/` must not decide:

- Is this doctrine accepted?
- Does this claim have sufficient evidence?
- Is this source legally or ethically admissible?
- Is this artifact safe for public release?
- Should this path override Directory Rules?
- Should this release be promoted?

Those decisions require the owning docs steward, ADRs, source stewards, policy checks, review state, release state, evidence closure, and rollback controls.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/docs/` include:

- Explicit documentation render or preview helpers that do not publish.
- Markdown normalization helpers that preserve meaning.
- Generated docs index builders.
- Docs report generators for CI handoff.
- Review-gated documentation transport or synchronization operators.
- Non-authoritative summarization or inventory helpers whose output remains derived.

Repository-wide documentation validators belong under [`tools/validators/docs/`](../validators/docs/README.md). A validator must not be placed here merely because its input is Markdown.

Every helper should be:

- deterministic;
- safe to run locally and in CI;
- network-free by default;
- explicit about inputs and outputs;
- conservative about rewriting content;
- tested with public-safe fixtures;
- clear about whether it checks format, links, metadata, evidence labels, or prose hygiene.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/docs/` | Correct home | Reason |
|---|---|---|
| Documentation validator implementations | `tools/validators/docs/<lane>/` | Accepted `DIR-EXEC-006` places validator implementation under `tools/validators/`; subject matter does not create a second validator home. |
| Doctrine documents | `docs/doctrine/` | Tooling checks doctrine; it does not own doctrine. |
| ADRs | `docs/adr/` | ADRs are governance records, not executable helpers. |
| Architecture prose | `docs/architecture/` | Human-facing architecture belongs in docs. |
| Source catalog pages | `docs/sources/` or `data/registry/sources/` depending on responsibility | Source documentation and source registry records are not docs tooling. |
| Generated release manifests | `release/` | Release authority does not live in tooling. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts belong in lifecycle roots. |
| Policy files | `policy/` | Policy meaning must not be embedded in docs helpers. |
| JSON Schemas | `schemas/contracts/v1/...` | Field shape belongs in schema home. |
| Contract definitions | `contracts/` | Object-family meaning belongs in contract home. |
| Validator tests | `tests/validators/docs/<lane>/` | Tests prove validators; validators and tests remain responsibility-aligned. |
| Other helper tests and fixtures | The current responsibility-aligned `tests/` or `fixtures/` lane | Test data is not executable tooling, and this README does not invent a parallel test topology. |
| One-off manual cleanup snippets | `scripts/maintenance/` or `scripts/one_off/` | Promote only durable, repo-wide tooling into `tools/docs/`. |

[Back to top](#top)

---

## Documentation tooling contract

A helper under `tools/docs/` should document its contract before being used in CI or review gates.

Minimum contract:

| Field | Requirement |
|---|---|
| Inputs | Explicit files, directories, or manifests. Avoid implicit whole-repo mutation. |
| Output | Stable JSON, Markdown report, or console summary. |
| Side effects | None by default. Any write mode must require an explicit flag. |
| Network | Off by default. Network checks require explicit opt-in and source rationale. |
| Determinism | Stable ordering and repeatable output. |
| Failure mode | Fail closed on malformed files, missing required metadata, or unsafe write target. |
| Evidence posture | Flag unsupported claims; do not invent evidence. |
| Rewrite posture | Preserve meaning; never silently rewrite doctrine, ADRs, rights statements, sensitivity notes, or release decisions. |

Recommended finite statuses:

| Status | Meaning |
|---|---|
| `pass` | The checked documentation surface satisfies the documented rule. |
| `warn` | A reviewable issue exists, but the helper cannot determine whether it is blocking. |
| `fail` | The checked surface violates a documented rule. |
| `error` | The helper could not safely complete. |
| `abstain` | The helper cannot decide because evidence, path authority, or configured scope is insufficient. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Markdown files under `docs/`.
- README files under responsibility roots.
- ADR templates and ADR index files.
- Documentation inventories.
- Source catalog documentation pages.
- Generated docs reports from previous CI runs.
- Public-safe test fixtures.

### Unsuitable inputs

- private credentials;
- raw source dumps;
- living-person records;
- DNA/genomic data;
- exact sensitive archaeology or rare-species locations;
- unpublished release payloads outside their review workflow;
- unredacted policy-sensitive material.

### Suitable outputs

- CI-friendly JSON reports;
- Markdown review summaries;
- local normalized copies when explicitly requested;
- anchor/link inventories;
- metadata coverage reports;
- verification backlog suggestions.

Generated outputs should go to a caller-selected output path. The helper should not silently write into `docs/`, `release/`, `data/receipts/`, `data/proofs/`, or `artifacts/` without an explicit workflow decision.

[Back to top](#top)

---

## Current routing

The verified direct-child implementation surface is intentionally small:

```text
tools/docs/
├── README.md                 # this non-authoritative routing boundary
└── wiki/                     # dry-run-first native-wiki synchronization operator
```

Current documentation validator responsibilities are routed as follows:

| Responsibility | Canonical implementation lane | Current evidence boundary |
|---|---|---|
| Local Markdown targets and fragments | [`tools/validators/docs/link-check/`](../validators/docs/link-check/README.md) | **CONFIRMED bounded executable**; external URLs remain unverified. |
| Document connectivity and registry parity | [`tools/validators/docs/document-graph/`](../validators/docs/document-graph/README.md) | **CONFIRMED bounded executable**. |
| KFM metadata blocks | [`tools/validators/docs/meta-block/`](../validators/docs/meta-block/README.md) | **CONFIRMED bounded executable**. |
| Explicit freshness and review-age signals | [`tools/validators/docs/stale-scan/`](../validators/docs/stale-scan/README.md) | **CONFIRMED bounded executable**; freshness is not truth. |
| Opt-in authority/maturity axis separation | [`tools/validators/docs/truth-label-lint/`](../validators/docs/truth-label-lint/README.md) | **CONFIRMED bounded executable**; the opt-in profile remains non-authoritative. |
| Terminology parity | [`tools/validators/docs/terminology-parity/`](../validators/docs/terminology-parity/README.md) | **README-only proposal**. |

This map records current routing; it does not propose another helper, validator, workflow, or authority surface.

[Back to top](#top)

---

## Validation

Validate the current routing documents with the existing canonical validators:

```bash
python tools/validators/docs/link-check/check_links.py \
  tools/docs/README.md \
  tools/validators/docs/README.md \
  tools/validators/docs/truth-label-lint/README.md
```

```bash
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  tools/docs/README.md \
  tools/validators/docs/README.md \
  tools/validators/docs/truth-label-lint/README.md
```

Each implemented child validator owns its executable and synthetic test command. The [`tools/validators/docs/` parent README](../validators/docs/README.md#validation) indexes those commands. The wiki operator's child README documents its separate dry-run, remote-write, and verification boundary; this README does not claim that a live synchronization was run.

[Back to top](#top)

---

## Review checklist

Before adding or changing a `tools/docs/` helper or operator, reviewers should confirm:

- [ ] The helper has a narrow documented purpose.
- [ ] Validator implementation is routed to `tools/validators/docs/` instead of duplicated here.
- [ ] The helper does not redefine doctrine, policy, schema, contract, release, receipt, or proof authority.
- [ ] The helper is deterministic.
- [ ] Network access is off by default.
- [ ] Write mode is opt-in and safe.
- [ ] Public-safe fixtures cover pass, warn, fail, error, and abstain where relevant.
- [ ] The helper preserves KFM truth labels and uncertainty boundaries.
- [ ] The helper does not silently rewrite ADRs, doctrine, rights statements, or sensitivity notes.
- [ ] CI use is documented before a helper becomes blocking.
- [ ] Any generated report has a clear owner and retention location.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Maintain this lane boundary | **CONFIRMED** | Keeps non-validator documentation operations separate from documentation authority. |
| Route validator implementation to `tools/validators/docs/` | **CONFIRMED current topology** | Avoids parallel metadata, link, freshness, graph, or assessment-axis validator homes. |
| Maintain the wiki synchronization operator | **PROPOSED use / child-owned** | Any remote write remains explicit, review-gated, and verified by the child contract. |
| Add another documentation helper | **NOT PROPOSED here** | Requires a distinct non-validator responsibility, current-tree review, tests, and an owned output lane. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-24 |
| Review state | Current routing reconciled against `main@a565914ea37b2ffc2f8dfeaa5a4b35eed137ae34`, accepted ADR-0029, and tracked documentation-validator implementations. |
| Next smallest safe change | None proposed by this README; re-review when the direct-child topology or a documentation-operator responsibility changes. |
