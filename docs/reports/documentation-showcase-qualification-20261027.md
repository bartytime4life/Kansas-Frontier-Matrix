<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/documentation-showcase-qualification-20261027
title: Recorded Explorer showcase — qualification and limits
type: qualification-report
version: v1.0
status: source-grounded candidate; independent review pending
owners: ["@bartytime4life"]
created: 2026-10-27
updated: 2026-10-27
policy_label: public
owning_root: docs/
responsibility: human-readable account of the documentation edition's source identities, tests, visual lineage, limits and recovery
truth_posture: CONFIRMED bounded execution and source inspection; NEEDS VERIFICATION independent review and later acceptance
related:
  - ../../README.md
  - ../wiki/Project-Status.md
  - ../brand/readme/showcase-media.json
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Recorded Explorer showcase: qualification and limits

**October 27, 2026. Documentation and derived display media only.**

## Goal and exact scope

Replace an illustration-led, historically private-Sites front door with a current,
source-aware introduction: one finite recorded hero, five tour choices, a source
selection table, readable onboarding and explicit verification boundaries.
Application, policy, contracts, data admission, access and deployment are unchanged.

| Identity | Inspected value |
|---|---|
| Monorepo base | `17f106d558674ec92a11809bcf3a06c82453777e` |
| Public Node app tested | `bbcec824fe57e6be0409ba1e35d737fa99581560` |
| App build identity | `sha256:d74c852dbb0c18c00bd62e224216620d6e9e472ffc7d5ba2780dd8c797256a33`; CLEAN_CHECKOUT |
| Visual-asset checkpoint | `974d3b340e619effc91d8da98cf9e67d95119df9` |
| Native wiki read-only base | `8e42e354a2c74bb31a5397d6c06caf81ba545953` |
| Review separation | Author self-review performed; independent/human review pending |

Exact documentation head and CI state belong to the associated draft PR. They are
not inferred from this report's filename. The standalone branch advanced during this
session to `533fd88679868619ac7b00db45dec8385d00ea79`; its later welcome changes are
not included in the application test result below. Main remained at the stated base
at that recheck. No other working tree's unpublished edits were copied or reset.

## Application execution performed

An isolated clean checkout of the named public application was used. Dependencies
were installed with its own exact lockfile, using `npm ci --no-audit --no-fund`.
This is an install/build/test result; disabling the npm audit output is not a
vulnerability assessment. No host credentials or inference configuration were copied.

```bash
npm ci --no-audit --no-fund
npm test
node_modules/.bin/tsc --noEmit
```

`npm test` expands to the production build and
`node --test --test-concurrency=4 tests/*.test.mjs`. Observed result:

```text
tests 1953
pass 1934
fail 0
cancelled 0
skipped 19
todo 0
```

The npm process exited **0**. TypeScript exited **0** independently. The test
runner reported about 32.94 seconds for the tests, excluding the preceding build.
This is not application response latency, production FPS or owner-workstation speed.
The build emitted its existing experimental-glob and bundle-size warnings. A green
build does not mean those warnings disappeared or the bundles became smaller.

### Skipped coverage stays skipped

| Skip family | Count | Missing/explicitly unselected boundary |
|---|---:|---|
| Cloudflare Worker integration and storage/runtime checks | 14 | The standalone Node composition does not ship the corresponding Wrangler/Miniflare/Worker build |
| Python weather-policy/source parity | 2 | Separate monorepo Python source selection was not configured |
| Disposable real MySQL integration | 2 | Explicit `KFM_MYSQL_TEST` / `KFM_PIPELINE_MYSQL_TEST` opt-ins not selected |
| Built HTTP pipeline smoke | 1 | `KFM_NODE_TEST_ORIGIN` was not supplied |

These were not changed or rerun as passes. There is no claim of a qualified production
MySQL migration, Worker integration, Python parity or fresh local HTTP startup here.
The test input/fixture scopes remain those in the
[pinned test tree](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/bbcec824fe57e6be0409ba1e35d737fa99581560/tests).

## Visual lineage and inspection

Five existing source WebM files were matched against their recorded SHA-256 values
in the application's existing derivative provenance. Their source manifests declare
complete captures with 120 source-ready renderer frames. The capture method renders
a camera path frame by frame; it is explicitly not a real-time frame-rate recording.
No new measurements, imagery, geographic outlines or intermediate source values
were synthesized for this edition.

The operator builder at [tools/docs/build_showcase_media.py](../../tools/docs/build_showcase_media.py)
checks the exact checkout, every input hash and complete-capture state before writing.
It samples/scales the existing tour pixels to 960×540 at 8 fps and retains the burned-in
source/date/limitation/attribution captions. Each output was reopened and decoded to
verify one-play metadata, seven-second total duration, dimensions and multiple
distinct frames. First/middle/end display content was inspected; a contact sheet of
midpoints was also reviewed. All imagery remains dated; forecast wind is October 20,
KGS classes are 2022–2024, and historic routes sit on explicitly modern imagery.

[showcase-media.json](../brand/readme/showcase-media.json) records input/output hashes,
capture time, original source clocks, attribution, limitations, tool versions and
actual encoded-frame counts. It is documentation derivative metadata, not a new
canonical evidence/proof/registry home. KFM code licensing does not relicense provider
imagery. These excerpts retain the existing project tour attribution; broader reuse
rights and provider-term requalification were not independently certified.

The five animated derivatives total **11,556,956 bytes**. Root and wiki landing pages
embed only the 1,843,200-byte terrain motion hero; other tours are reached through
still-image links. Each page offers a reduced-motion poster source and independent
still links. GitHub controls sanitization, caching and image rendering. These design
choices are not a measured page-load, battery, memory or Core Web Vitals improvement.

## Browser observations

The public Explorer was opened in a separate Chrome tab on October 27. The real-map
welcome, nineteen category choices in four groups, and the Water & watersheds dialog
were visible. Selecting the Tuttle Creek starting point changed the tour title,
source line and limitations. At the captured instant its animation area had not
established visible playback, so native full-tour playback is **not** counted as
accepted by this observation. The checked local media files provide the pixels for
the documentation, independently of that hosted loading state.

This was a bounded read/interaction check. No AI request, source activation, data
change, capture job, host setting or public deployment was performed.

## Documentation validation

The final validation record is completed alongside the associated source PR. Existing
validators, not a substitute broad test framework, check local links, metadata and
wiki projection. External URLs are classified by the local checker; only pinned
source paths separately inspected in the available local trees count as verified.

- Wiki synchronization contract: **9 passed**, including executable PowerShell
  navigation projection and historical filename compatibility.
- Media builder: five inputs and outputs checked; decoded motion and duration passed.
- Local-link validator: **24 documents, 772 local targets, zero failures**; 372
  external references classified as unverified by that local-only checker.
- Metadata profile `present`: **five valid metadata blocks, zero failures/warnings**;
  19 legacy wiki comments remain outside the v2 block profile, not falsely enrolled.
- Document graph: **24 reachable documents, zero unreachable/orphan documents,
  zero failures/warnings** in the selected front-door/wiki scope.
- Separately inspected **31 unique commit-pinned source/media targets** in their
  exact Git trees; zero missing targets. Other historical external URLs were not
  collectively certified.
- Removed root-heading anchors were checked against repository inbound links;
  no existing inbound root anchor was broken. One wiki recovery anchor was restored
  after the link validator identified its existing builder-profile consumer.
- Final projection, rendered-page and diff results are recorded by the source PR;
  native publication remains a separate, unperformed transition.

## Placement and governing material

The supplied Directory Rules.pdf was resolved but did not expose readable text;
Library byte materialization was unavailable. Its existing Google Drive Directory
Rules text was read as historical lineage. Placement is governed by the exact adopted
v2 bytes at [docs/doctrine/directory-rules.md](../doctrine/directory-rules.md) and
accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md). The
pinned doctrine intentionally retains its original draft header; accepted ADR-0029
records adoption of those bytes. This edition does not edit either authority.

| Affected paths | Owning responsibility and basis |
|---|---|
| `README.md` | Existing repository identity/orientation entry point; stable anchors retained |
| `docs/README.md`, `docs/wiki/` | Existing human explanation and source-managed wiki projection |
| `docs/brand/readme/` | Existing human-facing visual assets; source/derivative separation documented |
| `docs/reports/` | Existing human-readable qualification/report lane; no proof or release authority |
| `tools/docs/build_showcase_media.py` | Existing documentation operator lane; a media builder with defensive input checks, not a new standalone validator authority |
| `data/receipts/generated/` | Existing generated-work provenance lane; review remains pending |

The Contributor Reliability System and modernization reference were consulted for
bounded claims, source identity, review separation and readable navigation. The
current contributor/PR contracts govern the actual delivery. No new root, parallel
schema, contract, policy, registry, release or proof home is introduced.

## Review, risks and limits

Self-review covers claim wording, source paths, public-safe display content, source
hashes, native-route stability, finite motion and rollback. Codex Security Cloud was
opened as requested; it returned no scan result. No new scan was launched and no
security clearance is implied. This documentation scope does not justify a claim of
whole-repository vulnerability coverage.

No full browser/accessibility matrix, sustained rendering benchmark, live AI quality
check, production provider audit, scientific measurement validation, source admission
or governed release review was performed. Historical wiki references retain their
original checkpoints. The production app and monorepo remain separate histories.

## Delivery and rollback

This is a draft source update. [Wiki source rules](../wiki/README.md#editing-contract)
require source review/merge before a separate native-wiki sync. A dry-run projection
can be inspected without publishing. Native documentation and program/data releases
remain distinct decisions. No native wiki push, main merge or app deployment is
claimed here.

Revert the source commits to restore prior prose and assets. The update needs no data
migration, local-store reset, configuration change or application rollback. If a later
reviewed wiki synchronization needs correction, revert that wiki commit normally and
correct its source; never force-push. Exact base/head, changed paths and CI readback
remain on the associated PR.
