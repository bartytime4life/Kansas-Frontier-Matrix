# Current Site identity and source-alignment hold

Status: **IDENTITY_TARGET_RECONCILED / SOURCE_EQUIVALENCE_HOLD / ACCEPTANCE_HOLD**

Observation date: **2026-09-17 UTC**. This record reconciles repository target
metadata with a current connected readback of the active owner-private OpenAI
Site. [Issue #4418](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418)
remains the coordination tracker. This record does not claim that the Site
source, a GitHub mirror, or this monorepo application are equivalent.

## Current target and bounded evidence

| Surface | Recorded value |
|---|---|
| Active Site project | `appgprj_6aa0b1c41bc08191bfd86003920f1631` |
| Slug | `kansas-frontier-matrix-explorer` |
| Public URL | `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site` |
| Access observation | Owner-private; access revision 1 |
| Saved and deployed Site version | `45`; version ID `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_62df758dd2e0819197329087b6c2fe57` |
| Sites source commit | `2a0bd440a1aa5ff375efea5af87f283cd62c464b` |
| Saved archive | SHA-256 `b1415f7325668ac766240be8a94dd9b80b1ac5453ef5fa33049841a5d39034f3` |
| Deployment record | `appgdep_6aab4ac3bb64819182773975685b99e8`; platform status `succeeded` |
| Immediate recovery candidate | Version 44; version ID `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_4660be183b408191b21df3cc99bd9cd7`; source `b893683c33ef1a85d75f88db58e27e361c7e01a0`; archive SHA-256 `0653b89744b7ff44fa08570dcf75055b80d6c5449322cff655a550eb6043c637`; deployment `appgdep_6aab382f7ad081918c667ad763c32fe3` |
| Repository comparison base | `main@65e7070fcf77525ee8a61c2764d0f3dedb5f520d` |

The deployment record proves only that the platform reported a successful v45
transition. It does not prove current production behavior, rollback readiness,
release acceptance, or equality with a GitHub source tree.

Version 44 is an identified recovery candidate, not a rehearsed restoration.
Its presence in version history does not clear the recovery hold.

## Why equivalence remains held

**No full-tree comparison between the v45 Site source and a v45 GitHub mirror is
recorded.** No GitHub commit is designated as the v45 mirror by this patch. The
Site source and any older mirror must not be treated as equivalent because a
slug, URL, project, or partial path set matches. Earlier v42 evidence is a
superseded historical checkpoint, not proof of currentness.

The standalone Site source also has a different root layout from monorepo
`main`. Its renderer, operational-context adapters, and hosted bindings are not
admitted into this application merely because `.openai/hosting.json` selects the
active project. Do not merge a standalone Site mirror into monorepo `main`.

`SOURCE_EQUIVALENCE_HOLD` therefore remains in force. Production browser smoke,
WebGL behavior, selection and Drawer flows, accessibility, restricted-state
checks, and a recovery exercise are not recorded for v45, so `ACCEPTANCE_HOLD`
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
2. Advance the existing standalone mirror without rewriting history, then prove
   its complete Git tree equals the exact v45 Site source tree. A shared-path or
   file-count comparison is insufficient.
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
