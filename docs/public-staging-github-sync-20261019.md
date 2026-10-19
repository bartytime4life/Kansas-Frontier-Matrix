<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/public-staging-github-sync-20261019
title: Public Staging GitHub frontend sync
type: verification-record
version: v1
status: bounded source update; human review pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Record the portable GitHub frontend delta, retained public boundaries, verification and recovery
truth_posture: CONFIRMED source and bounded checks; rendered WebGL acceptance NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# Public Staging GitHub frontend sync

The owner requested an update from the GitHub files. This adapts the current
hosted Explorer frontend to the existing restricted Sites Worker. CONTRACT_VERSION
is `3.0.0`. It does not replace the separate private mirror or Node deployment.

## Source identities observed

| Source | Exact revision | Role |
|---|---|---|
| Existing Public Staging v8 | `084b730ca6e4e3f67af1da0426a275e7889c4603` | Actual native Site source; tree `89315ea9754326d5aeade7443f99bcbb6ba3650b` |
| GitHub Staging review base | `review-base/public-staging-v7-20261018@25fe5f2e531065a7aafad99e8710fa024beb01a7` | Owner-merged #5252; tree exactly matches v8 |
| GitHub main | `14ad5d8c6b34badbcf6e4c026afc9d39aeb217bd` | Governed monorepo; `apps/site/source` remains the separate private mirror |
| Hosted Explorer | `a0-hosted-ai-web-20261017@7b02dc22369f97b68577f821dc9dc7021e91cde5` | Current portable frontend reference, including merged #5257, #5265, #5279–#5281; a branch head is not publication evidence |
| Local Node counterpart | `a0-godaddy-navigation-pacing@50f33a43509025ba35fc0b62258f5c60d709062c` | Separate local runtime; not a Sites deployment source |

The Site is `appgprj_6acd1aafe0d88191a4306ea2ab44ed91`. Native v8 deployment
`appgdep_6ad4e5bd8d388191b3f0b8ba5ddab25c` succeeded. Its deployment URL is
`https://kfm-public-staging-20261012.blackbart-55.chatgpt.site`.
The custom access policy contains only the owner, with no added visitors/editors.
The canonical GoDaddy app `q9r9beo47t` and domain are separate. Its published
revision was not refreshed in this follow-up; the prior dated observation remains
in `docs/public-staging-alignment-20261018.md`. No claim of GoDaddy publication
or complete runtime parity follows from these GitHub revisions.

## Portable delta and deliberate boundaries

| GitHub change | Staging implementation |
|---|---|
| Prairie Field Desk welcome and theme | Upstream `atlas-studio.css`; adapted guide opens actual Layers/Time/search and links Topics. Public release notices and the external Chat boundary remain explicit. |
| Appearance navigation / legacy URLs | Remove obsolete Explore tab; old `navigate` state resolves to Appearance. Public private-only utility URLs remain filtered. |
| Search loading and empty-state repair | Discard stale debounced results; show updating state and truthful county-source unavailability. No county feed is activated. |
| Water upload / terrain sampling repair | Copy the bounded sampling algorithm; avoid unchanged Float32 uploads and continue pending batches. Retain Staging's 13-float geometry, minimum-zoom field and shader behavior. |
| Science discovery helpers and labels | Carry current pure helpers/styles and internal workspace source. The public `/observatory` route still renders its release-held page; no archive or new data product is enabled. |
| Focus Mode provenance regression check | Bring the current main mirror test into this isolated source lane. No Focus Mode or evidence authority expansion. |
| Node Find/Ask/Evidence composer, hosted inference, filesystem/model/account/history services | Excluded. Existing fixed external chat link transfers no Staging selection or draft. Node response/asset staging is not substituted for Worker packaging. |

`docs/repository-sync-20261019.json` records exact versus adapted file hashes.
This standalone source remains in its existing responsibilities under accepted
ADR-0029 / Directory Rules v2; the existing generated receipt family records the
work. No parallel policy, schema, source registry, release store or proof authority
is introduced. Prior dated receipts are retained unchanged. CI remains read-only
and contains no deployment step or secrets.

Public profile, route policy, release readers, catalog, data files, bindings,
dependencies, lockfile and hosting manifest are unchanged. All observational and
subsurface data remain held. Access controls, private stores and GoDaddy are not
modified. The generated receipt records human review as pending; the PR is draft.

## Verification

- Production Worker build and both public-asset scans pass. TypeScript, focused
  lint and `git diff --check` pass.
- 118 tests in the expanded existing Staging CI unit command pass, plus one
  separately executed compiled Worker integration test (119 total). These cover
  the public boundary/release gates, navigation, layout, identity, guide callbacks,
  stale search results, science helpers, Focus provenance and water uploads.
  This is not a full-suite acceptance claim.
- Compiled Worker serves the guide/identity/routes and exact emitted JS/CSS bytes;
  private routes, wrong origin and identity POST remain refused. Empty catalog
  records do not grant release authority.
- Browser desktop welcome and Evidence Drawer are readable. Find focuses the
  existing header search. Search reports the held county source accurately.
- At 390 × 844 CSS pixels, root clientWidth and scrollWidth are both 390; the
  374-pixel guide stays within the viewport and scrolls internally. Investigate
  change opens Time and focuses its controls. The phone Map menu displays
  Appearance, Map controls and Measure. The temporary harness was removed.
- Browser reports WebGL2 unavailable. Fallback and navigation are verified;
  rendered map/terrain/globe/Underground, real touch hardware, populated evidence,
  exports, broad accessibility/performance and independent review remain
  NEEDS VERIFICATION. No AI service acceptance is claimed.

The native publication response and PR body separately record the final saved
version, pushed source and deployment. This authoring record is not a deployment
attestation. The final Site and GitHub source commits may have different parents
and metadata; equal Git tree IDs establish exact file parity only.

## Recovery

Retain v8 saved version
`appgprj_6acd1aafe0d88191a4306ea2ab44ed91~appgver_8c01dfc92da481918c51bb5530428e39`
for same-Site rollback. Preserve newer source edits and retained versions before
recovery. Keep DB/R2, owner access, release pointers and GoDaddy intact. Closing
or reverting the isolated GitHub proposal does not deploy either application.
