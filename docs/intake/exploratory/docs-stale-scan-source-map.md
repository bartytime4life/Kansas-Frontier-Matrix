<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/docs-stale-scan-source-map
title: Documentation Freshness Validator Source Adaptation
type: source-map
version: v0.1
status: exploratory; implementation-source-map
owner: TODO-docs-steward-plus-tooling-qa-owner
created: 2026-08-07
updated: 2026-08-07
policy_label: public; repository-facing; non-authoritative
owning_root: docs/
responsibility: record the evidence-led transition from a proposal-only stale-scan lane to bounded, non-mutating freshness QA without adopting repository-wide thresholds or inferring truth from dates
truth_posture: CONFIRMED repository gap and accepted placement basis / PROPOSED freshness defaults / NEEDS VERIFICATION hosted execution and corpus classification
related:
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../tools/validators/docs/README.md
  - ../../../tools/validators/docs/stale-scan/README.md
  - ../../../tests/validators/docs/stale-scan/README.md
notes:
  - "The prior lane README explicitly said no executable existed and that thresholds required steward acceptance."
  - "This slice therefore uses an advisory changed-file ratchet and keeps warning promotion opt-in."
[/KFM_META_BLOCK_V2] -->

# Documentation freshness validator source adaptation

## Evidence-led selection

At base `main@55f2f981bc252b14c19c9d5069bf3aff0625bb6b`:

- `link-check/`, `document-graph/`, and `meta-block/` were bounded executable
  documentation-QA lanes;
- `stale-scan/` remained README-only and explicitly disclaimed executable code;
- its README named review dates, owner placeholders, temporary caveats,
  implementation claims, deterministic reports, no-network fixtures, and
  changed-file handling as the intended responsibility; and
- the parent docs-validator README named stale-scan as the next candidate after
  metadata and graph work.

The smallest dependency-closed upgrade is therefore a freshness **review
signal**, not automatic documentation repair and not a repository-wide policy
that every old document fails.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the effective placement authority.
The implementation uses existing responsibility roots:

| Responsibility | Placement |
|---|---|
| reusable docs QA | `tools/validators/docs/stale-scan/` |
| executable synthetic evidence | `tests/validators/docs/stale-scan/` |
| read-only CI orchestration | `.github/workflows/docs-stale-scan.yml` |
| source adaptation and limitations | this file under `docs/intake/exploratory/` |
| AI authoring accountability | `data/receipts/generated/` |

No new root or parallel contract, schema, policy, source, registry, receipt,
proof, release, catalog, or publication authority is created.

## Guarded design choices

1. **Explicit as-of date.** Time is an input and participates in the digest.
2. **Advisory default.** Expired windows and placeholders warn rather than fail.
3. **Bounded-required profile.** Strict missing-date behavior exists only for a
   separately adopted documentation lane.
4. **Delegation.** Meta-block owns structural metadata, link-check owns target
   resolution, and document-graph owns connectivity.
5. **No truth inference.** An old date requests review; it does not prove
   falsehood. Current implementation language requests reverification; the tool
   does not decide runtime state.
6. **No mutation.** Reports are ephemeral CI output or explicit local files.

## Deferred work

- whole-repository freshness classification and steward dispositions;
- accepted per-document-type review windows;
- reviewable waiver files with owner, reason, scope, and expiry;
- integration of freshness, graph, and metadata reports into a combined steward
  dashboard; and
- separate truth-label and implementation-overclaim analysis backed by current
  implementation evidence.

## Rollback

Revert the bounded implementation commit or its eventual merge commit. The
slice creates no source activation, lifecycle transition, release, deployment,
publication, or external state.
