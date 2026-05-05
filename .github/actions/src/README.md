<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-github-actions-src-readme
title: GitHub Actions Source README
type: directory-readme
version: v1
status: draft
owners: <TODO: owner not verified>
created: <TODO: YYYY-MM-DD>
updated: <TODO: YYYY-MM-DD>
policy_label: <TODO: public|restricted|...>
related: [<TODO: verify .github/actions/>, <TODO: verify .github/workflows/>, <TODO: verify tools/ci/>, <TODO: verify scripts/>]
tags: [kfm, github-actions, ci, validation]
notes: [Directory placement and adjacent repo conventions require verification in a mounted KFM checkout.]
[/KFM_META_BLOCK_V2] -->

# GitHub Actions Source

`status: draft` `authority: operational-ci-source` `policy: no-secrets` `release-authority: none`

This directory contains source code used by local GitHub Actions. It supports repository validation and automation; it does not define KFM truth, policy, schema, release, source, or evidence authority.

## Quick jumps

- [Repo fit](#repo-fit)
- [Authority level](#authority-level)
- [Accepted contents](#accepted-contents)
- [Exclusions](#exclusions)
- [Inputs and outputs](#inputs-and-outputs)
- [Security and policy](#security-and-policy)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Rollback](#rollback)
- [Related folders](#related-folders)

## Repo fit

Path: `.github/actions/src/README.md`

`.github/` is a repository-wide automation root. Files under `.github/actions/src/` should implement local action behavior used by workflow definitions, composite actions, or action entrypoints under `.github/actions/`.

This folder is operational support. It may inspect, validate, summarize, and report on repository state, but it must not become a competing home for KFM contracts, schemas, policies, source descriptors, lifecycle data, proof objects, release manifests, or domain documentation.

## Authority level

| Area | Status | Rule |
| --- | --- | --- |
| Directory authority | PROPOSED | Valid only after this path and adjacent action files are verified in the mounted repository. |
| KFM truth authority | none | Action source cannot create canonical facts or publish claims as truth. |
| Policy authority | none | Policy meaning and policy-as-code belong in the repo policy roots, not in action helper source. |
| Schema authority | none | Machine-checkable object shape belongs in schema roots, not in GitHub Action source. |
| Release authority | none | Actions may support release checks, but promotion remains a governed state transition. |
| Runtime authority | limited | Code here may run in CI or local action contexts only through declared action/workflow entrypoints. |

## Accepted contents

Use this directory for action-local implementation source such as:

- modules invoked by local GitHub Actions;
- validation helpers that read repo files and emit CI status;
- annotation/reporting utilities for GitHub Actions output;
- deterministic path, manifest, or contract checks delegated by workflow entrypoints;
- action-local tests or test harness helpers, when the repo convention places them here;
- build configuration needed only for action source, when verified by nearby package or action files.

Keep implementation small and reversible. Prefer shared validation logic in repo-wide `tools/`, `scripts/`, or `packages/` roots when the logic is useful outside GitHub Actions.

## Exclusions

Do not place these here:

- workflow YAML files; use `.github/workflows/`;
- action metadata files such as `action.yml`, unless the repo convention explicitly places them adjacent to source rather than inside `src/`;
- contracts or semantic object definitions;
- JSON Schema or other machine schema authority files;
- policy-as-code bundles or policy rationale docs;
- source descriptors, source registries, or source credentials;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release data;
- domain-lane documentation such as hydrology, fauna, roads, archaeology, or agriculture docs;
- generated release artifacts, unless a workflow-specific ADR documents the generated-output requirement;
- secrets, tokens, private keys, credentials, `.env` files, or sample secrets.

## Inputs and outputs

### Allowed inputs

Action source may read:

- repository files made available by checkout;
- workflow-provided inputs and environment variables;
- canonical contracts, schemas, policies, fixtures, manifests, or docs for validation;
- GitHub Actions context values required for annotations and status reporting.

### Required input discipline

Action source must treat user-provided paths, workflow inputs, and environment variables as untrusted until validated. It must not read private source credentials, canonical internal stores, or lifecycle data outside the workflow's explicit permission scope.

### Allowed outputs

Action source may emit:

- GitHub annotations;
- `$GITHUB_OUTPUT` values;
- logs suitable for CI review;
- temporary validation reports in the runner workspace;
- workflow artifacts, when the workflow explicitly declares artifact retention and policy.

### Output limits

CI logs and action artifacts are operational evidence. They are not KFM proof objects, ReleaseManifests, PromotionDecisions, RollbackCards, CorrectionNotices, or published claims unless a governed workflow explicitly validates, stores, reviews, and promotes them through the proper lifecycle.

## Security and policy

Action code runs in a high-leverage automation context. Keep the default posture fail-closed.

- Never print secrets, tokens, private URLs, credential-bearing headers, or source-system credentials.
- Avoid network access unless the action has a documented need, explicit workflow permission, and source-rights review.
- Prefer read-only repository access for validation tasks.
- Validate paths before opening files. Do not allow path traversal outside the checked-out workspace.
- Treat pull-request input as untrusted, especially for forked pull requests.
- Avoid direct model-runtime or AI-provider calls from action code unless a governed AI ADR and policy gate explicitly approve the use.
- Do not publish, release, or promote data directly from this directory's code.

## Impact

Changing files in this directory can affect CI reliability, validation outcomes, release gates, and reviewer trust. A behavior change should identify:

- which workflow or action entrypoint invokes the code;
- which inputs are accepted;
- which outputs are emitted;
- which repository roots are read;
- which failure modes produce `DENY`, `ABSTAIN`, or `ERROR`-like outcomes;
- how a maintainer can reproduce the result locally;
- how to roll back the change.

## Validation

After the real repository is mounted, validate this README and its surrounding action source with repo-native commands. At minimum, check:

```bash
git status --short
git branch --show-current || true
git rev-parse --show-toplevel || true

find .github/actions -maxdepth 4 -type f | sort
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort

rg -n "github-actions|action.yml|KFM_META_BLOCK_V2|EvidenceBundle|DecisionEnvelope|ReleaseManifest|PromotionDecision|Rollback|CorrectionNotice|RAW|QUARANTINE|PROCESSED|PUBLISHED" \
  .github tools scripts packages docs contracts schemas policy tests fixtures 2>/dev/null || true
```

Then run the action-specific checks proven by adjacent files, such as linting, type checks, unit tests, shell checks, or a local dry-run. Do not invent a test command without package or workflow evidence.

## Review burden

A pull request touching this directory should receive extra review when it:

- changes workflow-visible outputs;
- changes failure semantics;
- introduces network calls;
- touches release, publication, proof, or policy gates;
- reads sensitive files or lifecycle data;
- expands permissions in a workflow;
- changes dependency installation or generated bundles;
- introduces model or AI-provider calls.

## Rollback

Rollback should be simple: revert the action source change and rerun the affected workflow. If a workflow artifact, receipt, release candidate, or generated report was emitted during the faulty run, attach the workflow run URL and mark downstream artifacts as invalid or superseded through the repo's governed correction and rollback process.

## Related folders

| Folder | Relationship | Status |
| --- | --- | --- |
| `.github/actions/` | Local action definitions and entrypoints. | NEEDS VERIFICATION |
| `.github/workflows/` | Workflow orchestration and permissions. | NEEDS VERIFICATION |
| `tools/` | Repo-wide validation or operational tooling. | NEEDS VERIFICATION |
| `scripts/` | Repo scripts invoked by maintainers or CI. | NEEDS VERIFICATION |
| `packages/` | Shared implementation packages. | NEEDS VERIFICATION |
| `contracts/` | Semantic contract authority. | NEEDS VERIFICATION |
| `schemas/` | Machine validation authority. | NEEDS VERIFICATION |
| `policy/` | Policy-as-code and policy documentation. | NEEDS VERIFICATION |
| `tests/` and `fixtures/` | Repo-wide tests and fixtures. | NEEDS VERIFICATION |
| `data/` and `release/` | Lifecycle data, emitted memory, proof, and release operations. | NEEDS VERIFICATION |

## Maintainer notes

This README should be revised after Phase 0 repo inspection confirms the actual action stack, action entrypoints, package manager, workflow names, test runner, generated-output requirements, and adjacent README conventions.

