<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps/kansas-frontier-matrix-explorer/openai-sites-in-place-replacement
title: OpenAI Sites In-Place Replacement Handoff
type: app-local operational handoff
version: v0.1.0
status: READY_FOR_SITES_EXECUTION / HOLD_NO_SITES_MUTATION_SURFACE
owners:
  - "@bartytime4life — verified repository and Site-owner review route"
created: 2026-09-04
updated: 2026-09-04
policy_label: public; fixture-only; no protected precision
current_path: apps/kansas-frontier-matrix-explorer/docs/openai-sites-in-place-replacement.md
owning_root: apps/
responsibility: "Describe the bounded, reversible operator procedure for replacing the existing OpenAI Sites version of this application in place without creating repository, Vercel, source-admission, release, or KFM-publication effects."
truth_posture: cite-or-abstain
repository_checkpoint: 7c5d4125c277536258be6345e366efae59dbe5d6
related:
  - ../README.md
  - ../.openai/hosting.json
  - ../vercel.json
  - ../tests/hosting-boundary.test.mjs
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4232
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4235
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4246
notes:
  - "The Drive ZIP and execution document are immutable execution inputs and lineage records, not repository implementation authority."
  - "A Site deployment is an external Sites version transition, not a KFM source admission, release, or knowledge-publication transition."
[/KFM_META_BLOCK_V2] -->

# OpenAI Sites In-Place Replacement Handoff

> **Status:** `READY_FOR_SITES_EXECUTION / HOLD_NO_SITES_MUTATION_SURFACE`
>
> Use this procedure only from the **Edit** session of the existing OpenAI Site.
> The repository change that carries this handoff does not deploy, restore, or
> otherwise mutate that Site.

## Goal

Replace the current OpenAI Sites version of `kansas-frontier-matrix-explorer`
in place with the staged KFM Evidence Atlas package while preserving:

- the same Site project;
- the slug `kansas-frontier-matrix-explorer`;
- the public URL
  `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site`;
- the existing audience and access settings; and
- the immediately preceding Site version as the rollback target.

Do not create a second Site.

## Pinned identities

| Field | Required value |
|---|---|
| OpenAI Sites project ID | `appgprj_6a870a079c1c8191abb7401ef092a181` |
| Existing slug | `kansas-frontier-matrix-explorer` |
| Expected public URL | `https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site` |
| Replacement file | `kfm-evidence-atlas-replacement-2026-09-03.zip` |
| Replacement Drive ID | `1ze-jvGbn_doNZf7YgTKs2R9xb8mx-0C6` |
| Replacement SHA-256 | `6444f960bee9d2269fbf6854733bc63a59d2dd14c486670a0bfb040fd6136655` |
| Execution-packet Drive ID | `1StBDmSu_uW49fvQo8dha_oSd10CqNiZpzyEOpF2ceXs` |
| Controlling Notion page ID | `3d1a9202-1bf6-81fe-892c-e0f082c47cca` |
| Packet repository checkpoint | `7c5d4125c277536258be6345e366efae59dbe5d6` |

The package's embedded older repository snapshot is generation lineage only.
It does not supersede current GitHub state and must not be treated as authority
to rewrite this application.

## Authority and placement boundary

This is an app-local operational handoff under the existing
`apps/kansas-frontier-matrix-explorer/` deployable-application boundary. It
explains how an authorized Sites owner should perform one external version
transition. It does not define Site platform behavior, grant deployment authority,
create a release object, or replace repository-wide runbook doctrine.

The portable package intentionally loads MapLibre from a CDN as a standalone
Sites portability compromise. **Do not copy that acquisition pattern into the
repository.** Any repository-side renderer integration continues through the
accepted `packages/maplibre/` seam and its separate dependency, browser, CSP,
worker, evidence, and review gates.

## Stop conditions

Return `HOLD` without deployment when any of the following is true:

- the observed Site project, slug, or URL does not exactly match the pinned target;
- the session did not begin from the existing Site's **Edit** action;
- owner-level version restoration is unavailable or cannot be verified;
- the immediately preceding deployed Site version ID cannot be recorded;
- ZIP filename, digest, or `ARTIFACT_MANIFEST.json` verification fails;
- any required command fails, is skipped, is unavailable, or runs against different bytes;
- the candidate cannot be saved and previewed before production deployment;
- an existing Site URL or access setting would change;
- restricted archaeology fixture data appears in rendered, persisted, exported,
  telemetry, analytics, or shared state;
- the operation would require GitHub, Vercel, source, policy, release, or
  publication mutation; or
- rollback cannot restore the immediately preceding version.

## Procedure

### 1. Freeze the existing Site identity and rollback target

Before unpacking or replacing anything:

1. Open **Sites**, select the existing `kansas-frontier-matrix-explorer`, and
   choose **Edit**.
2. Record the observed project identity, slug, public URL, access settings, and
   current deployed Site version ID.
3. Verify that the current actor can restore the immediately preceding Site
   version through version history.
4. Record that preceding version ID as `rollback_target_version_id`.
5. Confirm that no second Site will be created and no URL or custom-domain
   operation is required.

### 2. Verify the exact package

1. Retrieve the ZIP by its stable Drive ID.
2. Compute SHA-256 and require the pinned digest above.
3. Unpack the archive without editing it.
4. Verify every path, byte count, and digest declared in
   `ARTIFACT_MANIFEST.json`.
5. Stop on any missing, extra-sensitive, mismatched, or unreadable artifact.

### 3. Run package-bound pre-publication validation

Run from the unpacked package root:

```bash
node --check core.mjs
node --check app.mjs
node --test tests/core.test.mjs
python3 tests/validate_static.py
```

A failed, skipped, unavailable, stale, or package-unbound result is not a pass.
Capture exact command output for the deployment receipt.

### 4. Replace only the existing Site working version

Use the package as the source for the existing Site's candidate working version.
Preserve the complete demonstrator path:

`Map -> Area of Interest -> Layers -> Time -> Measure -> Inspect -> Evidence -> Report -> Share`

Preserve:

- interactive MapLibre when the Sites runtime supports it;
- the public-safe SVG degradation path;
- nine synthetic or generalized KFM domains;
- domain, time, confidence, and visibility controls;
- AOI drawing and clearing;
- geodesic distance measurement;
- map and search inspection;
- EvidenceBundle presentation and finite negative states;
- deterministic science lenses labeled `PROPOSED` and `DERIVED`;
- reports labeled `NOT_PUBLISHED`;
- device-local workspace state and public-safe URL restoration; and
- keyboard, responsive, mobile, and reduced-motion behavior.

The restricted archaeology fixture is a negative-test input only. It must never
enter the map, visible DOM, search, inspector, Evidence Drawer, report, download,
local workspace, telemetry, analytics payload, or shared URL.

### 5. Save and inspect before deployment

1. Save a new Site version without deploying it.
2. Record `candidate_saved_version_id`.
3. Preview desktop and mobile widths.
4. Exercise keyboard navigation and reduced motion.
5. Exercise AOI draw/clear, distance measurement, all filters, map/search
   selection, EvidenceBundle display, science lenses, report download, URL
   restoration, local-workspace restoration, and SVG fallback.
6. Search rendered, persisted, exported, telemetry, analytics, and shared state
   for the restricted fixture identifiers and precision fields.
7. Confirm the prior deployed version remains available and the public URL,
   slug, and access settings are unchanged.

### 6. Deploy the saved candidate to the same Site

Deploy only the verified saved candidate to the existing Site. Record the new
Site version ID and UTC timestamp. Do not create an alternate host.

Repeat the complete smoke-test matrix against the production URL. A preview pass
does not substitute for production verification.

### 7. Return and preserve the receipt

Return the receipt in chat. When Notion access is present, append the same receipt
to the controlling Notion page and the KFM System Chronicle. Do not silently
commit a production receipt to GitHub; repository placement and release meaning
require their own reviewed decision.

## Required receipt shape

```json
{
  "terminal_state": "PUBLISHED_SITE_VERSION|HOLD|ROLLED_BACK|ERROR",
  "timestamp_utc": "<ISO-8601>",
  "target": {
    "project_id_expected": "appgprj_6a870a079c1c8191abb7401ef092a181",
    "project_id_observed": "<value>",
    "slug_expected": "kansas-frontier-matrix-explorer",
    "slug_observed": "<value>",
    "public_url_before": "<value>",
    "public_url_after": "<value>",
    "same_site_confirmed": false,
    "second_site_created": false,
    "access_settings_unchanged": false,
    "owner_restore_capability_confirmed": false
  },
  "versions": {
    "previous_site_version_id": "<value>",
    "candidate_saved_version_id": "<value|null>",
    "new_site_version_id": "<value|null>",
    "final_deployed_version_id": "<value>",
    "rollback_target_version_id": "<value>",
    "previous_version_retained": false
  },
  "source": {
    "zip_file": "kfm-evidence-atlas-replacement-2026-09-03.zip",
    "expected_sha256": "6444f960bee9d2269fbf6854733bc63a59d2dd14c486670a0bfb040fd6136655",
    "observed_sha256": "<value>",
    "artifact_manifest_verified": false
  },
  "validation": {
    "node_check_core": "PASS|FAIL|NOT_RUN",
    "node_check_app": "PASS|FAIL|NOT_RUN",
    "node_core_tests": "PASS|FAIL|NOT_RUN",
    "static_validation": "PASS|FAIL|NOT_RUN"
  },
  "preview_verification": {
    "outcome": "PASS|FAIL|NOT_RUN",
    "evidence": "<check-by-check bounded evidence>"
  },
  "production_verification": {
    "outcome": "PASS|FAIL|NOT_RUN",
    "evidence": "<check-by-check bounded evidence>"
  },
  "restricted_state_negative_test": {
    "outcome": "PASS|FAIL|NOT_RUN",
    "evidence": "<bounded evidence>"
  },
  "rollback": {
    "required": false,
    "exercised": false,
    "procedure": "Restore rollback_target_version_id through Sites version history",
    "result": "NOT_NEEDED|PASS|FAIL"
  },
  "non_effects": {
    "github_mutated_by_site_execution": false,
    "repository_settings_mutated": false,
    "vercel_mutated": false,
    "source_admission_changed": false,
    "kfm_release_or_publication_authority_created": false
  },
  "open_verification": []
}
```

Do not invent values or convert `NOT_RUN` into `PASS`.

## Terminal outcomes

| Outcome | Meaning |
|---|---|
| `PUBLISHED_SITE_VERSION` | Same project, slug, URL, and access settings; all checks passed; candidate deployed; prior version retained. |
| `HOLD` | No production deployment because identity, ownership, rollback, integrity, validation, preview, or negative-test proof is insufficient. |
| `ROLLED_BACK` | A deployed candidate failed a critical production check and the immediately preceding version was restored and reverified. |
| `ERROR` | Wrong Site, second Site, URL change, bypassed mismatch, restricted exposure, hidden authority expansion, or failed rollback. |

## Rollback

Restore `rollback_target_version_id` through OpenAI Sites version history, then
verify the original public URL, access behavior, desktop/mobile composition, and
critical interaction path. Preserve both the failed candidate receipt and rollback
evidence.

A Site rollback does not rewrite Git history, change repository source, alter
Vercel configuration, reverse source admission, change KFM lifecycle state, or
withdraw a KFM knowledge release.

## Hard non-effects

This procedure must not:

- create a GitHub branch, commit, pull request, merge, release, tag, or settings change;
- change a Vercel project, preset, deployment, domain, environment, or Git integration;
- add a repository MapLibre dependency or copy the package's CDN acquisition path;
- bind D1 or R2;
- admit a source or read RAW, WORK, QUARANTINE, PROCESSED, candidate,
  canonical, private, restricted, or unreleased stores;
- add a model-provider path, secret, private endpoint, or external persistence;
- approve evidence, policy, review, release, promotion, or publication; or
- imply that deploying a Site version makes its reports or derived scores sovereign truth.

## Open verification

- A Sites-enabled session must confirm the current and previous Site version IDs.
- Owner-level restore capability must be demonstrated before mutation.
- Runtime compatibility and all preview/production checks remain unproved until
  executed against the exact candidate version.
- GitHub repository homepage metadata still points at a non-authoritative host;
  [issue #4246](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4246)
  holds that settings-only transition pending explicit authorization and readback.
