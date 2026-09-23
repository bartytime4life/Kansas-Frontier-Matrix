# Current Site identity and source-alignment hold

Status: **IDENTITY_TARGET_RECONCILED / SOURCE_EQUIVALENCE_HOLD / ACCEPTANCE_HOLD**

Latest observation: **2026-09-23 UTC** (2026-09-22 America/Chicago). This
record distinguishes connected platform metadata from source equivalence and
application acceptance. The 2026-09-17 readback is retained below as history. [Issue #4418](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418)
remains the coordination tracker. This record does not claim that the Site
source, a GitHub mirror, or this monorepo application are equivalent.

## Verified platform checkpoint — 2026-09-23 UTC

| Surface | Connected readback |
|---|---|
| Active project / slug | `appgprj_6aa0b1c41bc08191bfd86003920f1631` / `kansas-frontier-matrix-explorer` |
| Site URL | [Kansas Frontier Matrix Explorer](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site) |
| Audience | Owner-private custom access; revision 1; no external visitors. A reachable URL is not public-access authorization. |
| Latest saved version | `53`; `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_20f1bb51899c81919c92077dbcd04672` |
| Exact Site source | `22ac19960c2f72f11f5e4e9b87c7e12f62074d6e` |
| Saved archive digest | `sha256:9ed44c87d4099eb5ddf26c93bc9357203bae44d1a5e42b093848b3ef3a8572fa` |
| Deployment | `appgdep_6aaf81da36008191a8654bd97f4addac`; `publish`; `succeeded`; updated `2026-09-20T06:50:01.739476+00:00`; bound to the exact v53 ID above |
| Previous saved version | `52`; `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_9f13692829788191888f2bba42b44a3f` |
| v52 source / archive | `8e6a60982ee121f0a81ba76d434696d136866929` / `sha256:caa9a9a9f76d56e79bfda6215b10a07e1a724ced051fa65211272dcd5b01e8fe` |
| Repository source checkpoint | [`main@9dcdaec2cacbbf9880bd613b546a7314a2673ac5`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/9dcdaec2cacbbf9880bd613b546a7314a2673ac5) |

Evidence method: connected Sites `get_site`, `list_site_versions`,
`get_site_version` for v53/v52, and `get_deployment_status` for v53. These
read-only observations confirm the returned identities and platform status.
The archive digest is a platform-reported value; this review did not download
or independently hash the archive. No credentials or personal allowlist values
are included in this record.

No complete-tree comparison, authenticated browser acceptance, WebGL/selection/
Drawer check, or recovery exercise was performed in this reconciliation.
`SOURCE_EQUIVALENCE_HOLD` and `ACCEPTANCE_HOLD` therefore remain unresolved in
this record. Version 52 is the prior saved **recovery candidate**, not a tested
rollback. The platform description mentions comparison views and device-local
report/story drafts; metadata alone does not establish their working behavior.
The monorepo app and this Site source are still separate implementations.

<a id="current-target-and-bounded-evidence"></a>

## Historical target and bounded evidence — 2026-09-17 UTC

The following v45/v44 identities preserve the earlier observation. They are
not the current deployed/recovery pair and their checks must not be transferred
to v53/v52.

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

<a id="why-equivalence-remains-held"></a>

## Historical v45 equivalence limitation

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
   its complete Git tree equals the exact candidate Site source tree (v53 at
   this observation; re-read before any later operation). A shared-path or
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

## Reconciliation scope and rollback

This edit updates human-readable records inside the existing application
boundary. It changes no Site source, saved version, audience, binding, receipt,
release, or deployment. Revert the documentation edit if its readback is
superseded or incorrect; use a new dated observation for later platform state.
Historical receipts and adopted governance bytes stay unchanged.
