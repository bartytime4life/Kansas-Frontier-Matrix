<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/deployment-consolidation
title: Deployment consolidation and Vercel retirement
type: runbook
version: v1.2
prior_version: v1.1
status: draft; record cleanup, provider absence and environment retirement verified
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-22
policy_label: public
current_path: docs/runbooks/deployment-consolidation.md
owning_root: docs/
responsibility: Retire obsolete deployment records and plan source convergence without merging incompatible runtime histories.
truth_posture: CONFIRMED observations and PROPOSED implementation phases are separated below.
[/KFM_META_BLOCK_V2] -->

# Deployment consolidation and Vercel retirement

The owner requested removal of Vercel on 2026-10-19. Vercel is retired as a KFM
hosting target. This procedure removes its operational resources and records;
historical Git history and governed evidence retain their original meaning.
Application delivery, source admission, evidence release and publication remain
separate decisions.

## Confirmed checkpoint and remaining work

The following table is the pre-retirement baseline recorded by PR #5310. Its
resource counts and pending actions are historical; the operational checkpoint
below records the later verified outcome and the remaining environment blocker.

| Surface | Observation on 2026-10-19 | Disposition |
| --- | --- | --- |
| Scanned main checkpoint | `b1524d031c2ef21081226fc0ebc0f72a78bb6981` | Pinned source-scan baseline; re-read main before implementation |
| Hosted Explorer | `a0-hosted-ai-web-20261017@5b09c94de207409e4df08914f202097b2bcfae45` | Standalone Node baseline; not a monorepo-root deployment |
| Source scan | No case-insensitive `vercel` matches in 10,539 checked main-branch file paths across root files and implementation/configuration/test/governance roots, or in all 1,172 hosted-branch files | No active source integration found to remove; `docs/`, `data/` and `artifacts/` on main were outside this lexical content scan |
| GitHub Apps | Repository lists Codex, Claude, Claude Design Import and GoDaddy Node.js Hosting; no Vercel app | Already disconnected; keep the other applications |
| Repository webhooks | None listed | No Vercel webhook to remove |
| GitHub Actions credentials | Repository has no secrets or variables; the eight legacy environments below each have no secrets or variables | No Vercel credential was identified; provider-side credentials were not read |
| GitHub deployment history | UI lists 634 total deployment records; recent visible September entries are attributed to Vercel | Total is not an independently enumerated Vercel count; the operator below classifies exact records |
| Vercel projects | Repository-filtered project list returns `kfm` (`prj_WwIu1qs8CQLStFncZ1icOAwnkXvT`) and `usgs` (`prj_DwAiIlYcKiU4zwR9GYwnDYAKVoWx`) in team `team_XVYbnle9XkeYTypWx5l6LOQN` | Permanent deletion requires owner confirmation in the Vercel dashboard |
| Vercel domains | `kfm-sigma.vercel.app` and `usgs-beta.vercel.app`; no custom domain in either project's domain list | Retire these obsolete project endpoints; no GoDaddy DNS change |
| Pause attempts | Both pause calls returned `400 invalid_deployment`: no active production deployment exists | No pause or deletion occurred; this is not a claim that all preview deployments are absent |
| Concurrent app work | Open [PR #5308](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5308) changes login/private application paths on the hosted branch and prepares a replacement GoDaddy preview | Re-read its state and current hosting identity before source integration; this cleanup does not modify or publish that application |

The source scan uses current GitHub tree/blob identities. Existing local object
caches supplied matching bytes; unavailable blobs were read at the pinned GitHub
commit. Duplicate blobs were counted by tracked path. It covers `.github/`,
`apps/`, `infra/`, `configs/`, `scripts/`, `runtime/`, `tools/`, `packages/`,
`tests/`, `connectors/`, `pipelines/`, `pipeline_specs/`, `policy/`,
`control_plane/`, `schemas/`, `contracts/`, `fixtures/`, `examples/`,
`migrations/`, `release/` and root files. A lexical scan is not a dependency
security audit or evidence of current production health.

## Operational checkpoint after approved cleanup

**PARTIAL — record retirement and provider absence are verified; environment
retirement remains pending.** This checkpoint records external operations; merging
this documentation does not perform or authorize another deletion.

- **CONFIRMED:** [PR #5310](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5310)
  merged the existing operator. Its read-only
  [inventory run 39303802095](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39303802095)
  used `main@eb992b76d3762a20e6a1cca7c0228a2b9f8c7336`, passed the 18
  operator tests, and selected 607 Vercel records while excluding 27 records.
- **CONFIRMED:** the owner approved the exact inventory digest
  `8646e0197065de80abd7dd2708db2ed75922c1f2456fbe4e88412cd5a2775f53`
  and the eight environment IDs below. A fresh preflight matched that digest.
- **CONFIRMED:** the unchanged helper, blob
  `acd2f78e067d2c10c14ab604482f5933a33c5570`, completed at
  `2026-10-19T19:05:03Z` with exit 0. Its journal records exactly 607 unique
  completed deletions and 104 scoped inactive transitions. Every journal ID
  belongs to the approved inventory; its final re-enumeration reported
  `ELIGIBLE_VERCEL_GITHUB_RECORDS_ABSENT`.
- **CONFIRMED:** a separate full readback returned only the 27 owner-created
  `stage` records. Their saved minimal metadata, including IDs, source SHAs,
  refs, environments and timestamps, was unchanged.
- **CONFIRMED at 19:06 UTC:** both exact Vercel project IDs in the baseline table
  returned 404 under `team_XVYbnle9XkeYTypWx5l6LOQN`, and the full team
  project list was empty. The repository-filtered list alone was insufficient:
  it had previously omitted the still-existing `usgs` project.
- **UNKNOWN:** the actor and exact time of provider-side deletion. This session
  verified absence; it did not submit either project deletion.
- **CONFIRMED:** repository-installed Apps remain ChatGPT Codex Connector,
  Claude, Claude Design Import and GoDaddy Node.js Hosting, with no Vercel App.
  Repository webhooks, Actions secret names and Actions variable names are empty.
- **CONFIRMED at 19:11 UTC:** all eight legacy environments still exist, alongside
  `copilot` and `stage`. Action-time checks found zero secrets, zero variables,
  no protection rules and no branch policy on each legacy environment. Current
  main workflow environment declarations reference only
  `kfm-hosted-capture` and `godaddy-production`; the hosted application branch
  `a0-hosted-ai-web-20261017@53efe37cdc0ad916b3fc15acc19411d919a2fab4`
  has no workflow environment declarations.

The exact inventory, all 608 pre-cleanup status entries, the preserved 27 record
identities, owner approval, apply journal, exit result and readbacks are retained
in the owner-held `KFM-Vercel-Retirement-Audit-20261019.zip`. Its checkpoint
SHA-256 is
`dc751a280f96f8b1e0c6860f1882c13019a3eaa40a9d7f0f9620f4534fb407f6`.
This digest identifies the retained operational audit; it is not a public release
receipt or an independently authenticated approval. The original GitHub inventory
artifact is `12213155217` and expires on 2026-11-18. Do not rely on that expiring
artifact as the sole retained copy.

### Environment closure on 2026-10-22

**CONFIRMED — the repository now has one environment, `Production`, and zero
deployment records.** The owner requested that the Deployments page be reduced
to a single environment and approved this exact set in the authoring session.

- **CONFIRMED:** the 27 owner-created `stage` records (2025-11-27 to
  2025-12-22, ref `main`, every latest status `failure`) were set inactive and
  then deleted. Their source, the scheduled `kfm-auto-update.yml` workflow, is
  no longer on main.
- **CONFIRMED:** environments `stage`, `copilot`, `Preview`, `Preview – kfm`,
  `Production – kfm`, `Preview – kansas-frontier-matrix-explorer-web`,
  `Production – kansas-frontier-matrix-explorer-web` and `Production – usgs`
  were deleted. Each had zero secrets, variables and protection rules at action
  time. `Preview – usgs` was already absent.
- **CONFIRMED:** `Production` (`20759133715`) is retained by owner choice and is
  empty. The GoDaddy application is published from its own dashboard and
  creates no GitHub deployment records.
- **Recreation sources:** the Copilot coding agent recreates `copilot` when it
  runs. [godaddy-hosted-capture.yml](../../.github/workflows/godaddy-hosted-capture.yml)
  sets `deployment: false`, so enabling capture adds the `kfm-hosted-capture`
  environment but no deployment records.

This supersedes the preservation of `copilot`, `stage` and `Production` in the
2026-10-19 sections below, which remain as the historical procedure.

### Remaining environment cleanup (2026-10-19, superseded)

GitHub's existing environment settings required owner reauthentication before
deletion. The Mobile request timed out; no environment deletion was submitted.
The owner can use a passkey or retry authentication in
[repository environments](https://github.com/bartytime4life/Kansas-Frontier-Matrix/settings/environments).
The exact deletion-set approval is already recorded; authentication does not
broaden that scope.

After authentication, recheck identities, secrets, variables, protection rules
and active consumers immediately before removing only the eight listed legacy
environments. Stop on drift or an active consumer. Preserve `copilot`
(`11904832799`) and `stage` (`10250497541`), and verify the same 27
deployment records remain unchanged afterward. Do not rerun deployment-record
deletion merely because this runbook changes; the 607 approved records are
already absent.

The cleanup made no source, application-branch, GoDaddy, Sites or DNS changes.
It did not qualify current application health. Keep the temporary operator and
workflow until environment closure and durable audit retention are verified;
retire them through a separately reviewed follow-up. **Full Vercel retirement
remains incomplete.**

The [generated-work receipt](../../data/receipts/generated/genrec-vercel-retirement-outcome-20261019.json)
binds this documentation's bytes with human review pending. It is authoring
provenance, not proof of the external operations.

## Remove GitHub's historical Vercel records

Use [the manual cleanup workflow](../../.github/workflows/retire-vercel-deployments.yml)
and its [one-time operator](../../scripts/retire_vercel_deployments.py). It is
owner-only, restricted to protected `main`, serialized, and grants only contents
read plus deployments read. KFM-WF-009 forbids write-capable Actions jobs, so the
workflow cannot apply deletion. The owner-run helper uses existing GitHub CLI
authentication, or an explicitly supplied scoped GH_TOKEN, outside Actions.
Neither creates credentials. The workflow has no Vercel credentials and cannot change
GoDaddy, Sites, DNS, GitHub environments, repository secrets or source branches.

1. Use the reviewed operator merged by PR #5310. Review and merge any future
   operator changes through normal repository checks; a PR itself performs no cleanup.
2. Run **Inventory historical Vercel deployment records**.
   Download and preserve `inventory.json` and `sha256.txt` before deletion. The
   workflow artifact lasts 30 days; it is an operational snapshot, not a release
   receipt or permanent evidence store.
3. Review the exact IDs, source SHAs, refs, environments and creator identities.
   Only creator `vercel` or `vercel[bot]` in the eight named legacy environments
   is eligible. Other providers and `copilot`/`stage` are retained. Unknown creator
   formats require investigation; do not broaden attribution based only on an
   environment name. Deployment payloads and credentials are excluded.
4. After approval of that exact irreversible deletion set, the owner runs the
   helper from the reviewed checkout with existing authenticated `gh` access:

   ```bash
   python3 scripts/retire_vercel_deployments.py --use-gh --apply \
     --expected-digest REVIEWED_64_CHARACTER_LOWERCASE_DIGEST \
     --output /private/operator-records/kfm-vercel-retirement-new-run
   ```

   Replace the digest and absent output directory with reviewed values. The local
   CLI needs deployments-write access to this repository. Missing authentication,
   permissions or network stops the helper; it does not log in or request access.
   A changed inventory fails before mutations.
   GitHub's records have immutable IDs/source identities; the fresh inventory
   fixes the target set. The operator tries deletion first, then permits one
   explicit inactive-status transition only after a 422 and an eligible current
   status. Status changes set `auto_inactive=false` to avoid touching other records.
5. Retain the success or partial JSONL journal. HTTP errors stop the run; rate
   limits are not retried indefinitely. A partial run needs a new inventory and
   new digest. A successful apply re-enumerates and requires zero eligible records.

Deletion of GitHub deployment records cannot restore their original IDs/status
history. The saved minimal inventory supports an audit, not an identical rollback.
Deleting a GitHub record also does not delete the deployed application at Vercel.
Do not manufacture a success status or claim provider deletion from this result.

## Remove obsolete environments and Vercel projects

After record cleanup, remove only these legacy GitHub environments:

| Environment | GitHub environment ID |
| --- | --- |
| Preview | 20759370888 |
| Production | 20759133715 |
| Preview – kfm | 20790666281 |
| Production – kfm | 20790566089 |
| Preview – usgs | 21120929505 |
| Production – usgs | 21120614233 |
| Preview – kansas-frontier-matrix-explorer-web | 20790652137 |
| Production – kansas-frontier-matrix-explorer-web | 20790599922 |

Re-read secrets, variables, consumers and protection rules immediately before
deletion. Stop if the empty-state observation changed or an active consumer is
found. Preserve `copilot` and `stage`; their retirement is outside this request.
Environment deletion is permanent and requires action-time confirmation.

The supported Vercel project-deletion operation requires the owner to review and
confirm in the provider dashboard. At the operational checkpoint above, both
identified projects are absent, so no further provider deletion is needed for
those IDs. If a future check finds either project again, verify its exact ID,
team, domain list and retained-configuration needs before owner confirmation:

- [Review deletion of kfm](https://vercel.com/blackbart555-6322/kfm/settings/general#delete-project)
- [Review deletion of usgs](https://vercel.com/blackbart555-6322/usgs/settings/general#delete-project)

Project deletion removes deployments, environment variables, settings and
project-domain associations. Keep GoDaddy/Sites credentials and DNS outside this
operation. Do not infer project absence from a repository-filtered result alone.

Closure requires fresh readback: both exact Vercel project IDs absent, a full
team project listing inspected rather than relying only on a repository filter,
eligible GitHub records absent, the eight retired environments absent, and no
Vercel app/webhook/credential or active source integration. Do not reintroduce
Vercel to test the deletion. Retire the temporary operator/workflow through a
reviewed follow-up once the inventory and outcome have durable retention.

## Dependency-ordered source consolidation plan

1. **Retirement:** finish the resource cleanup above; retain the exact inventory
   and outcomes. This does not resolve the separate GoDaddy availability incident.
2. **Compatibility reconciliation:** pin the then-current hosted, local and
   Staging heads, identify unique changes and current consumers, and bring selected
   compatible changes through small, fresh integration PRs. At the inspected
   checkpoints, local `50f33a43509025ba35fc0b62258f5c60d709062c` had 49 unique commits
   versus 148 on hosted `5b09c94`; Staging merge `024337410ff297b45b1f2cf8f5e6870756e021df`
   had seven unique commits versus 87 on hosted. Commit counts are ancestry
   evidence, not a feature-parity checklist.
3. **Placement and migration decision:** main and the standalone hosted history
   have no common ancestor. Record the canonical application-source placement,
   Node/Sites adapter boundaries, preserved mirror lineage, packaging and rollback
   in a reviewed ADR/migration note. An exact destination is PROPOSED until that
   decision is made. Do not overwrite `apps/site/source/`, replace monorepo root
   scripts, force-push main or force unrelated histories together as a shortcut.
4. **Delivery convergence:** after that decision, produce target-specific Node and
   Sites artifacts from the approved feature baseline. Keep source commit, build
   digest, provider deployment/version and audience distinct. Do not copy private
   stores, model state or credentials into Git. Reuse existing Site identities.
5. **Branch retirement:** retire old application branches only after their unique
   work is classified, consumers are switched, target behavior is verified and
   rollback checkpoints remain available. Squash short-lived logical PRs; keep
   an explicit mapping to source commits and original review evidence.

Each implementation increment needs changed-area tests, exact-base/head overlap
checks and review. Application integration needs build/type checks, real Node
HTTP checks, browser acceptance for changed desktop/mobile flows and separate
Sites adapter validation. Source parity does not establish hosted parity. Owner
approval remains separate for merge, publication, data release and audience changes.

## Placement, validation and rollback

[Directory Rules](../doctrine/directory-rules.md), accepted
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), and the existing
[runbook boundary](README.md) place this human procedure under `docs/runbooks/`,
the small one-time operator under existing `scripts/`, its tests under `tests/qa/`,
and manual orchestration under `.github/workflows/`. No new root, policy/schema
authority, lifecycle lane or evidence home is introduced.

Offline validation:

```bash
python3 -m unittest discover -s tests/qa -p test_retire_vercel_deployments.py -v
```

Reverting the authoring commit removes the temporary helper, workflow, tests and
this procedure. It does not undo completed remote deletions. Vercel project and
GitHub environment deletion have no verified identical restoration procedure.
GoDaddy/Sites rollback follows their existing, separately reviewed procedures.
This document does not authorize restoring the retired Vercel hosting path.
