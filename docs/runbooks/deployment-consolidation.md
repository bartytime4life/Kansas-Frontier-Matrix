<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/deployment-consolidation
title: Deployment consolidation and Vercel retirement
type: runbook
version: v1.0
status: draft; source inventory complete; external retirement pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
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

## Remove GitHub's historical Vercel records

Use [the manual cleanup workflow](../../.github/workflows/retire-vercel-deployments.yml)
and its [one-time operator](../../scripts/retire_vercel_deployments.py). It is
owner-only, restricted to protected `main`, serialized, and grants only contents
read plus deployments read. KFM-WF-009 forbids write-capable Actions jobs, so the
workflow cannot apply deletion. The owner-run helper uses existing GitHub CLI
authentication, or an explicitly supplied scoped GH_TOKEN, outside Actions.
Neither creates credentials. The workflow has no Vercel credentials and cannot change
GoDaddy, Sites, DNS, GitHub environments, repository secrets or source branches.

1. Review and merge this bounded operator change through the normal repository
   checks. The draft PR itself performs no cleanup.
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

The Vercel connector returns `requires_user_action` for project deletion. The
owner must sign in and review/confirm deletion of the two exact projects above:

- [Review deletion of kfm](https://vercel.com/blackbart555-6322/kfm/settings/general#delete-project)
- [Review deletion of usgs](https://vercel.com/blackbart555-6322/usgs/settings/general#delete-project)

Vercel project deletion also removes that project's deployments, environment
variables, settings and project-domain associations. Recheck the domain list and
any required retained configuration before confirmation; do not move or delete
GoDaddy/Sites credentials as part of this operation. The current browser is at
Vercel sign-in; no project deletion was submitted.

Closure requires fresh readback: repository-filtered Vercel projects absent,
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
