# Current Site identity and source-alignment hold

Status: **IDENTITY_TARGET_RECONCILED / SOURCE_EQUIVALENCE_HOLD / ACCEPTANCE_HOLD**

Observation date: **2026-09-21 UTC**. This record reconciles repository target
metadata with a read-only connected readback of the active OpenAI
Site. [Issue #4418](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418)
remains the coordination tracker. This record does not claim that the Site
source, a GitHub mirror, or this monorepo application are equivalent.

## Current target and bounded evidence

| Surface | Recorded value |
|---|---|
| Active Site project | `appgprj_6aa0b1c41bc08191bfd86003920f1631` |
| Slug | `kansas-frontier-matrix-explorer` |
| Public URL | `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site` |
| Access observation | `custom`; revision 1; one allowed user, no allowed groups or external visitors; current caller has owner role |
| Saved and deployed Site version | `53`; version ID `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_20f1bb51899c81919c92077dbcd04672` |
| Sites source commit | `22ac19960c2f72f11f5e4e9b87c7e12f62074d6e` |
| Saved archive | SHA-256 `9ed44c87d4099eb5ddf26c93bc9357203bae44d1a5e42b093848b3ef3a8572fa`; 58 files |
| Deployment record | `appgdep_6aaf81da36008191a8654bd97f4addac`; platform status `succeeded` at 2026-09-20 06:50 UTC |
| Immediate recovery candidate | Version 52; version ID `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_9f13692829788191888f2bba42b44a3f`; source `8e6a60982ee121f0a81ba76d434696d136866929`; archive SHA-256 `caa9a9a9f76d56e79bfda6215b10a07e1a724ced051fa65211272dcd5b01e8fe`; prior deployment `appgdep_6aaf6f2b629c8191845cb6f7809bc571` reported `succeeded` |
| v53 Site source tree | Git tree `f4a107e04e1e2dc780c700b05ce0526e11f8b359`; 132 tracked files in a clean, read-only source checkout at the exact Sites-reported commit |
| Monorepo app comparison | `claude/sweet-fermi-is9m0e@e2e1ea7215d53139bf83c3b97bcfd06ef9956e10`, `apps/kansas-frontier-matrix-explorer/` tree `4f3df2d43569f85c80bcf115f219b3b0a22740a8`; 87 tracked files; **DIFFERENT** from v53 source |

The deployment record proves only that the platform reported a successful v53
transition. It does not prove current production behavior, rollback readiness,
release acceptance, or equality with a GitHub source tree.

Version 52 is an identified recovery candidate, not a rehearsed restoration.
Its presence in version history does not clear the recovery hold.

The 2026-09-17 readback of v45 remains historical: version ID
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_62df758dd2e0819197329087b6c2fe57`,
source `2a0bd440a1aa5ff375efea5af87f283cd62c464b`, archive SHA-256
`b1415f7325668ac766240be8a94dd9b80b1ac5453ef5fa33049841a5d39034f3`,
and deployment `appgdep_6aab4ac3bb64819182773975685b99e8` were recorded
against `main@65e7070fcf77525ee8a61c2764d0f3dedb5f520d`. Its then-current
recovery candidate was v44, version ID
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_4660be183b408191b21df3cc99bd9cd7`,
source `b893683c33ef1a85d75f88db58e27e361c7e01a0`, archive SHA-256
`0653b89744b7ff44fa08570dcf75055b80d6c5449322cff655a550eb6043c637`,
and deployment `appgdep_6aab382f7ad081918c667ad763c32fe3`. Neither historical
version nor its recovery candidate is the current v53 target or a rehearsed
restoration.

## Why equivalence remains held

On 2026-09-21, the existing Site source repository was opened read-only at
the exact v53 commit returned by Sites. The offline
[`compare-site-source-tree.mjs`](../scripts/compare-site-source-tree.mjs)
compared complete committed Git trees, not a sampled path set. Of 42 shared
paths, 12 had identical mode/type/blob IDs and 30 differed; 90 paths existed
only in the Site source and 45 only in the monorepo app. The source tree has
132 tracked files versus 87 in the app subtree. The 58-file saved archive is
a separate build artifact and was not treated as a source tree. The comparator
prints only aggregate counts, hashes, and a finite `MATCH` or `DIFFERENT`
outcome; a match by itself would confer no Site version, review, release, or
deployment authority.

To repeat this bounded comparison, first open the existing Site source into an
isolated checkout through the Sites source workflow, then run from this app
directory (using absolute checkout paths):

```sh
node scripts/compare-site-source-tree.mjs \
  --site-checkout "$KFM_SITE_CHECKOUT" \
  --site-commit 22ac19960c2f72f11f5e4e9b87c7e12f62074d6e \
  --project-id appgprj_6aa0b1c41bc08191bfd86003920f1631 \
  --candidate-repo "$KFM_MONOREPO_CHECKOUT" \
  --candidate-commit e2e1ea7215d53139bf83c3b97bcfd06ef9956e10 \
  --candidate-subtree apps/kansas-frontier-matrix-explorer
```

The comparator exits `0` for identical trees, `1` for different trees, and
`2` for an invalid or untrustworthy comparison. This observed monorepo
comparison returned `1` and `DIFFERENT`. It is pinned to the monorepo commit
immediately before this documentation and comparison-tool batch; the batch
does not synchronize the application source. The comparator never contacts
Sites or GitHub.

**The monorepo app is not an exact v53 Site source mirror.** No GitHub commit is
designated as the v53 standalone mirror by this patch, so full-tree equality
to such a mirror remains unproved. The Site source and any older mirror must
not be treated as equivalent because a slug, URL, project, or partial path set
matches. Earlier v42 evidence is a superseded historical checkpoint, not
proof of currentness.

No full-tree comparison with a designated v53 standalone mirror is recorded.

The standalone Site source also has a different root layout from monorepo
`main`. Its renderer, operational-context adapters, and hosted bindings are not
admitted into this application merely because `.openai/hosting.json` selects the
active project. Do not merge a standalone Site mirror into monorepo `main`.

`SOURCE_EQUIVALENCE_HOLD` therefore remains in force. Production browser smoke,
WebGL behavior, selection and Drawer flows, accessibility, restricted-state
checks, and a recovery exercise are not recorded for v53, so `ACCEPTANCE_HOLD`
also remains in force.

## Repository target boundary

The repository hosting manifest now selects the active Site project. Its `d1`
and `r2` values remain `null` because this monorepo application does not own or
describe the hosted Site's live bindings. No alternate-host deployment
configuration is retained in the application or connector source.

Changing repository metadata does not mutate a Site, deploy a version, alter an
audience, or prove a source mirror. This reconciliation does not authorize deployment,
release, publication, source admission, or rollback.

The version-1 deployment receipt schema, fixture, validator, and 2026-09-03
replacement handoff remain historical lineage for project
`appgprj_6a870a079c1c8191abb7401ef092a181`. The historical and active project IDs
are not aliases. Those v1 artifacts must not be replayed as current-project
evidence.

## Evidence required to clear the holds

1. Read back the active Site project, saved/deployed version, access policy,
   exact source commit, archive digest, and immediately preceding recovery target.
2. Identify and advance the existing standalone mirror without rewriting history,
   then prove its complete Git tree equals the exact v53 Site source tree. The
   offline comparator requires the exact Site commit, project ID, candidate
   commit, and candidate subtree; it rejects a dirty Site checkout and returns
   nonzero for a different tree. A shared-path or file-count comparison is
   insufficient.
3. Record a reviewed current-project receipt that binds the candidate, archive,
   source commit, complete tree, and rollback target. Historical v1 inputs are
   ineligible.
4. Run the repository-native build and tests plus authenticated desktop/mobile,
   WebGL, selection/Drawer, accessibility, and restricted-state checks against
   the same candidate.
5. Exercise and record same-Site recovery before clearing the recovery hold.

Until all five items close, the safe outcome is `HOLD`. A future correction must
preserve the historical records and source-separation controls; it must not
create a second Site or force-push the standalone mirror.
