# FluencyLoop change-context adaptation source map

Status: `PROPOSED` implementation adaptation record.

## Source boundary

This slice was mined from `baokhang83/fluencyloop` at commit
`fe3ccf6dada2c36057a3d65b84ca150bd9b9c96e`, especially:

- `plugins/fluencyloop/scripts/bash/slice-context.sh`;
- `plugins/fluencyloop/scripts/powershell/slice-context.ps1`;
- `plugins/fluencyloop/skills/backfill/SKILL.md`;
- `MANIFESTO.md`.

The upstream repository is Apache-2.0 licensed. This implementation does not copy or vendor its scripts, skills, hooks, plugin manifests, templates, or private-calibration behavior. It reimplements a narrower KFM profile around current repository contracts and governance boundaries.

## Problem selected

The first FluencyLoop adaptation added `ImplementationDecisionRecord`, which stores the irreducible explanation for a few load-bearing choices. Its renderer deliberately does not inspect Git diffs. That leaves a mechanical companion gap: a reviewer or AI tool still has to establish which paths changed, the immutable commit range, line-count totals, top-level roots, binary changes, and attention signals.

The selected change closes that gap without widening decision or review authority.

## Incorporated ideas

| Upstream idea | KFM implementation |
|---|---|
| Read the changed slice instead of whole files | Build one context from an immutable base/head Git range. |
| Scripts perform mechanical work | Python collects name-status and numstat metadata locally and deterministically. |
| Use cheap decision signals to conserve model attention | Closed signal vocabulary, fixed weights, recomputed score, and `decision_capture_recommended`. |
| Quantify unjournaled or skipped work | A merged range can be represented as `DRAFT` for later evidence-backed backfill. |
| Feature/review context should be durable | Content-derived context ID and closed schema. |

## Adapted or narrowed

- Raw diff hunks are not stored. Only path, status, count, binary, and immutable commit metadata are admitted.
- Branch names are not identity. Full base and head SHAs define the range.
- A heuristic recommendation is not a gate, approval, risk decision, or proof that a design choice exists.
- Backfill does not infer rationale. It produces a draft mechanical context; separately authored decision records remain unverified until reviewed.
- GitHub state is not authenticated. The tool reads a local repository only and creates no remote mutation authority.

## Rejected ideas

- Committed free-form session transcripts.
- Private developer calibration, familiarity levels, competence labels, or engagement ledgers.
- Raw patch storage in a governance object.
- Automatic rationale or rejected-alternative generation from a diff.
- Plugin-managed branch creation, marketplace refresh, session hooks, or automatic updates.
- A second constitution or replacement for KFM doctrine, ADRs, `ReviewRecord`, the Decision Log, or the pull-request template.
- Making missing context or decision journals a merge gate.

## KFM fit

The profile keeps the FluencyLoop separation between mechanical scripts and irreducible human/model reasoning while applying KFM boundaries:

```text
local committed Git range
  -> ImplementationChangeContext
       paths + statuses + counts + mechanical signals only
  -> optional ImplementationDecisionRecord(s)
       mechanism + rationale + alternatives + evidence + validation + rollback
  -> existing KFM pull-request and human-review surfaces
```

Neither object creates evidence, policy, review approval, repository authorization, promotion, release, deployment, publication, or public-use authority.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. The adaptation uses existing responsibility roots:

- semantic contract: `contracts/governance/`;
- machine shape: `schemas/contracts/v1/governance/`;
- synthetic cases: `fixtures/contracts/v1/governance/`;
- model, local-Git adapter, and CLI validator: `tools/validators/governance/`;
- tests: `tests/validators/governance/`;
- workflow: `.github/workflows/`;
- source adaptation record: `docs/intake/exploratory/`;
- generated authoring receipt: `data/receipts/generated/`.

No new root or parallel contract, schema, decision, review, receipt, proof, release, policy, catalog, or source-registry authority is introduced.

## Deferred candidates

1. A deterministic PR-comment renderer that consumes only a validated context plus validated decision records, with no write action in the core tool.
2. A repository-native integration that emits the context as a CI artifact after workflow-security review.
3. A human-confirmed backfill workflow for selected merged changes, preserving `NEEDS_VERIFICATION` until confirmation.
4. Cross-platform parity tests on native Windows for local Git metadata parsing.

## Evidence and limitations

- **CONFIRMED:** the upstream files expose the changed-slice, mechanical-context, heuristic-signal, and unverified-backfill patterns at the pinned commit.
- **CONFIRMED:** current KFM `main@4e5a45f19d5b3bd24e108c816b0e88d4606ff1be` contains `ImplementationDecisionRecord` and no search result for an equivalent `ImplementationChangeContext` object or likely-decision metadata profile.
- **CONFIRMED:** open PR #2084 is RecompileManifest-scoped and path-disjoint from this slice; the intervening merged PRs #2080–#2083 are also path-disjoint from the selected change.
- **PROPOSED:** the new contract, schema, validator, tests, workflow, and documentation until reviewed and merged.
- **NEEDS VERIFICATION:** exact-head hosted workflow results, effective repository settings, branch-protection coupling, and human reviewer disposition.
