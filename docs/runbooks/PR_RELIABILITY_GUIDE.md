# KFM Pull Request Reliability Guide

> **Status:** PROPOSED contributor runbook. This document improves PR preparation and failure attribution; it does not change repository policy, required checks, release authority, or publication authority.

## Purpose

Use this guide before opening or updating a KFM pull request. Its goal is to reduce avoidable review churn, stale PR claims, duplicated work, and failed checks while preserving KFM's evidence, governance, and rollback boundaries.

This guide is subordinate to accepted ADRs, adopted Directory Rules, the exact-current `.github/PULL_REQUEST_TEMPLATE.md`, path-scoped instructions, contracts, schemas, policy, tests, and workflows.

## 1. Start from exact current evidence

Before editing:

1. Resolve the current `main` SHA and record it.
2. Read the target file or implementation at that exact ref.
3. Search open PRs and recent merges for path or behavior overlap.
4. Read the accepted ADRs, Directory Rules, adjacent README/runbook guidance, and CODEOWNERS that apply to the target.
5. Define one observable outcome, explicit non-goals, acceptance criteria, and rollback.

Do not use a remembered SHA, an older PR body, Drive/Notion prose, or a previous check result as current implementation evidence.

## 2. Keep the PR dependency-closed but small

A good KFM PR contains every artifact materially required for the declared behavior, but no unrelated cleanup.

Before branching, classify the work:

| Change class | Minimum review focus |
|---|---|
| Documentation / metadata | Target role, factual claims, links/navigation, Markdown checks |
| Test / fixture / validator | Positive and negative cases, non-vacuity, fail-closed behavior |
| Application / package | Focused tests, build/typecheck where applicable, ownership/import boundaries |
| Workflow / CI | YAML/config validity, exact commands, permissions, network/secret exposure, workflow-security checks |
| Contract / schema / policy | Valid and invalid fixtures, consumer compatibility, finite outcomes, fail-closed behavior |
| Dependency / supply chain | Exact pins/locks, audit/security evidence, build compatibility, rollback |
| Data/public surface | Synthetic/no-network proof where possible, evidence/policy/release separation, correction/rollback |

If the change crosses three or more top-level responsibility roots, explain why one PR is safer than splitting it.

## 3. Placement: a path is an authority claim

For existing tracked files, prefer the established responsibility root unless current governance says otherwise. For new, moved, renamed, deleted, or authority-bearing files, record:

- owning responsibility root;
- Directory Rules / accepted ADR / adjacent accepted precedent;
- affected navigation, registry, manifest, generator, alias, or compatibility surfaces;
- rollback or migration implications;
- why the change does not create a parallel schema, contract, policy, source, registry, receipt, proof, catalog, release, or canonical-truth home.

If ownership remains unresolved, use `HOLD`; do not create a new authority home by convenience.

## 4. Validate in proportion to the changed surface

Run the narrowest meaningful checks first. A docs-only PR should not be forced through unrelated local build work merely to appear thorough; a runtime or dependency PR should not hide behind Markdown-only checks.

For every reported check, record:

- exact SHA tested;
- command or workflow name;
- scope;
- outcome;
- whether it is head validation, merge-result validation, base-only evidence, or not comparable.

A new commit invalidates earlier head-specific validation.

## 5. Failure attribution: do not turn every red check into a code claim

Classify failures before changing the PR:

| Classification | Meaning | Action |
|---|---|---|
| `INTRODUCED` | Comparable base passes and exact PR head fails | Fix before the affected transition |
| `INHERITED` | Same material failure exists on comparable base and head | Keep visible; do not misattribute to the PR |
| `RESOLVED` | Base fails and head passes | Record as repair evidence |
| `BASE_DRIFT / INTEGRATION` | Original branch passed but changed main/merge result now fails | Reconcile against current main |
| `ENVIRONMENTAL / FLAKY` | Evidence supports runner/service/capacity failure or nondeterminism | Record separately; retry only when useful |
| `PENDING` | Hosted execution has not settled | Do not claim success or failure yet |
| `NOT_RUN` | Check was not run | State why |
| `NOT_APPLICABLE` | Check has no meaningful relationship to the change | State why |
| `UNKNOWN` | Evidence is insufficient | Do not guess |

### Current recurring repository signals

At the 2026-08-30 repository checkpoint used to draft this guide, recent PRs repeatedly showed two non-change-specific failure classes:

1. `accessibility` and `ui-build` can stop during locked pnpm workspace installation with `ERR_PNPM_IGNORED_BUILDS` before the downstream Explorer build/tests or keyboard smoke run.
2. Vercel preview can fail because the account exceeds its daily deployment limit.

These are **not permanent classifications**. Re-check the exact base and exact PR head. Do not label a future occurrence `INHERITED` merely because the job name or error looks familiar.

## 6. Dependency and pnpm guardrail

If a PR changes no dependency manifest, lockfile, package-manager policy, or build-script approval surface, do not broaden the PR merely to repair a repository-wide pnpm install policy failure.

If the PR does change that surface, dependency installation becomes part of the acceptance proof. Verify the exact manifest/lock relationship, package-manager version, relevant audit/security checks, build/test compatibility, and rollback as one coherent dependency change.

Never bypass a dependency or security gate with `--force`, an audit waiver, lockfile drift, or an unrelated workflow relaxation just to make a PR green.

## 7. PR body: make review state machine-readable to humans

Use the exact-current `.github/PULL_REQUEST_TEMPLATE.md`. At minimum, a draft should state:

- goal and why now;
- delivery state (`DRAFT_WIP`, `DRAFT_REVIEWABLE`, or `HOLD`);
- exact base SHA and exact head SHA;
- changed paths and Directory Rules basis;
- overlap search and ownership decision;
- material truth labels (`CONFIRMED`, `PROPOSED`, `NEEDS VERIFICATION`, `UNKNOWN`);
- what changed and what explicitly did not change;
- performed validation and exact-head hosted state;
- inherited, pending, skipped, unavailable, and not-run checks separately;
- open verification items and the first transition each blocks;
- security/rights/sensitivity impact;
- rollback or forward-fix path;
- explicit non-effects for merge, source admission, release, deployment, promotion, and publication when they are not requested.

Green checks, mergeability, CODEOWNERS, automated review, and generated receipts are not human approval.

## 8. Before the final push or PR update

Re-run a bounded overlap and drift check immediately before the final remote mutation:

- Has `main` moved?
- Did an overlapping PR merge, close, or change head?
- Did an accepted ADR, Directory Rule, contract, schema, policy, workflow, or dependency change?
- Does the PR body still describe the exact head?
- Are all cited checks attached to the exact current head or clearly labeled otherwise?
- Is the PR still in the intended draft/readiness state?

If drift is material, reconcile and revalidate. If drift is path-disjoint and does not change acceptance criteria, record it without needless branch churn.

## 9. Fast preflight checklist

- [ ] Current `main` SHA recorded.
- [ ] Open-PR/recent-merge overlap checked.
- [ ] Target responsibility root and Directory Rules basis verified.
- [ ] One observable outcome and explicit non-goals defined.
- [ ] Direct dependencies and consumers identified.
- [ ] Acceptance criteria include relevant negative/fail-closed behavior.
- [ ] Focused validation chosen for the actual change class.
- [ ] Secrets, private data, exact sensitive locations, restricted payloads, and hidden reasoning excluded from Git/CI/PR text.
- [ ] Exact-head results separated from base, stale-head, merge-result, and external-service results.
- [ ] Introduced failures distinguished from inherited/environmental failures using comparable evidence.
- [ ] PR body matches the exact-current template and exact head.
- [ ] Rollback is specific and reversible.
- [ ] Merge, release, deployment, promotion, publication, and source activation remain separate transitions.

## 10. Evidence basis for this revision

This guide was drafted from current repository evidence and coordination material, including:

- `docs/doctrine/directory-rules.md` and its responsibility-root / placement-outcome model;
- `.github/PULL_REQUEST_TEMPLATE.md` v1.6;
- `docs/runbooks/FIRST_GOVERNED_PR_RUNBOOK.md`;
- recent PRs showing exact-head validation practice and recurring failure attribution patterns;
- the KFM Repository Workbench coordination page;
- the KFM Verified Improvement Campaign v1.1 design lineage.

Repository evidence controls current behavior. Notion and Google Drive remain coordination/design lineage unless separately adopted by repository authority.

## Rollback

Before merge, close the draft PR or delete the feature branch. After an authorized merge, revert the single documentation commit or apply a reviewed forward correction. This document has no source-admission, policy, lifecycle, release, deployment, promotion, or publication effect.
