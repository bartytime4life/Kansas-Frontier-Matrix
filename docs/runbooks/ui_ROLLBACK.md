# Explorer Web change rollback and recovery

**Status:** Repository-grounded draft for source-control recovery in
`apps/explorer-web/`. Deployment and operational release rollback are `UNKNOWN`
and outside this procedure.

Use this runbook when an Explorer Web source, test, documentation, or build
configuration change must be backed out or corrected. It covers recovery through
a new reviewed pull request. It does not authorize a direct change to `main`, a
deployment rollback, a release transition, or a change to evidence, policy,
source, lifecycle, or published state.

> [!IMPORTANT]
> The repository currently proves a locked Explorer Web build-and-test lane, but
> it does not establish hosting, a deployment workflow, public operation, or an
> operational release rollback. A Git revert can recover repository content; it
> cannot withdraw or correct a released public-safe artifact.

## Choose the recovery path

| Observed state | Supported action | Boundary |
|---|---|---|
| Change is only on an unmerged branch or draft pull request | Close or supersede the draft after preserving the failure evidence. | No `main` revision or runtime state is changed. |
| A single-parent commit is on `main` | Revert that exact commit on a new branch and open a draft pull request. | The revert remains proposed until reviewed and merged. |
| A merge commit is on `main` | Confirm the intended mainline parent before preparing a merge revert. | Do not guess the parent or revert unrelated commits. |
| Reverting would remove required later work | Prepare the smallest forward fix instead. | Explain why a revert is unsafe and keep the fix scoped to the regression. |
| Local build output or dependency state is suspect | Stop the local server, remove ignored local output, and reinstall from the lockfile if needed. | Local cleanup does not change repository, deployment, or release state. |
| A live deployment, public artifact, source, evidence object, policy decision, or release record is affected | Stop and use the owning incident, correction, or release procedure. | This runbook has no verified authority or mechanism for that transition. |

## Stop conditions

Do not continue with a source-control-only rollback when any of these conditions
apply:

- the affected revision is not identified precisely;
- the proposed revert includes unrelated changes or later dependencies;
- the issue may expose restricted data, harmful precision, credentials, private
  endpoints, or sensitive operational detail;
- a public carrier, release alias, correction notice, rollback card, cache,
  catalog, triplet, evidence object, or source state must change;
- the recovery requires a deployment target, feature flag, environment,
  credential, or operator authority that current repository evidence does not
  establish;
- validation shows the recovery creates a new trust-boundary or accessibility
  regression.

For a trust-path or sensitive-material incident, preserve the observable evidence
and follow the [incident-response](./INCIDENT_RESPONSE.md) or
[sensitivity-escalation](./SENSITIVITY_ESCALATION.md) guidance. For a governed
release reversal, use the [cross-cutting rollback runbook](./ROLLBACK_RUNBOOK.md)
and the owning `release/` records. Do not describe a code revert as a completed
release rollback.

## Capture the rollback target

Record the following before modifying a branch:

- the affected commit or pull request and the last known-good commit;
- whether the affected commit has one parent or is a merge;
- the exact files and user-visible behavior in scope;
- the failing command, exit code, and relevant output, or a bounded manual
  reproduction;
- any later commits that depend on the affected change;
- whether any public, release, evidence, policy, rights, sensitivity, or
  correction state may be involved.

Inspect the candidate from a current checkout:

```bash
git fetch origin main
git show --stat --oneline <affected-commit>
git show --no-patch --format='%H %P' <affected-commit>
```

The second command exposes the commit's parent list. One parent indicates a
normal commit. More than one parent indicates a merge and requires an explicit
mainline choice.

## Prepare repository recovery

Create a dedicated branch from current `main`:

```bash
git switch --create ui-rollback/<short-description> origin/main
```

For a single-parent commit, stage its inverse without committing immediately:

```bash
git revert --no-commit <affected-commit>
```

For a merge, first verify which parent represents the intended mainline. Only
then prepare the inverse with that parent number; for the common case where the
first parent is `main`:

```bash
git revert --no-commit -m 1 <merge-commit>
```

If the revert enters a conflict state and a safe resolution is unclear, abort it
and stop:

```bash
git revert --abort
```

Review the staged recovery before committing:

```bash
git status --short
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Do not resolve conflicts by discarding later work wholesale. Abort and use a
forward fix when the inverse cannot be isolated safely.

## Validate the recovered revision

Run the checks that cover the changed surface from the repository root. The app
manifest currently implements these commands:

| Check | Command | Use when |
|---|---|---|
| TypeScript and production bundle | `pnpm --filter explorer-web build` | Any Explorer source, manifest, TypeScript, or build change is involved. |
| Unit tests | `pnpm --filter explorer-web test:unit` | Fixture, projection, state, or app logic is involved. |
| Browser tests | `pnpm --filter explorer-web test:browser` | Rendered interaction, focus, navigation, or accessibility behavior is involved. |
| Full app suite | `pnpm --filter explorer-web test` | Broad or uncertain Explorer impact warrants both test lanes. |
| Renderer/store boundary | `python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py` | Adapter, renderer-import, path, or trust-membrane behavior is involved. |

Also rerun the original failing check or reproduction. Record skipped checks and
why they were not applicable. A local or hosted pass is evidence for the tested
revision only; it is not review, merge approval, release, deployment, promotion,
or publication.

## Commit and hand off

After the diff and focused checks are satisfactory:

```bash
git commit -m "revert(ui): <concise reason>"
git push -u origin HEAD
```

Open a draft pull request to `main`. Include:

- affected and last-known-good commits;
- why revert or forward fix was selected;
- exact changed paths and any conflict resolution;
- reproduction and validation commands with results;
- known limitations and any release, deployment, or trust-state escalation;
- rollback of the proposed recovery by closing the draft or reverting its commit
  through another reviewed pull request.

Do not force-push, merge, enable auto-merge, deploy, publish, or mutate a release
record as part of this procedure.

## Local-only recovery

Explorer's Vite output is `apps/explorer-web/dist/`, and `dist/` is ignored by
the repository. To rebuild local output, stop the development server, remove only
that ignored directory, and run the locked install and build again:

```bash
rm -rf apps/explorer-web/dist
pnpm install --frozen-lockfile
pnpm --filter explorer-web build
```

Confirm the path before running the removal command. Do not use local cleanup as
evidence that a committed regression, remote deployment, or public artifact was
recovered.

## Related repository evidence

- [Explorer Web app boundary and maturity](../../apps/explorer-web/README.md)
- [Explorer Web local development](./ui_LOCAL_DEV.md)
- [Locked Explorer build-and-test workflow](../../.github/workflows/ui-build.yml)
- [Explorer renderer and internal-store boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [Cross-cutting release rollback procedure](./ROLLBACK_RUNBOOK.md)
- [Synthetic release rollback rehearsal](./rollback-rehearsal.md)
- [`release/` authority and operational holds](../../release/README.md)
- [Accepted Directory Rules adoption](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

This file replaces a small scaffold traced to
`docs/domains/agriculture/MAP_UI_CONTRACTS.md`. That draft source remains lineage,
not current operational authority; the procedure above is bounded by current
repository evidence.
