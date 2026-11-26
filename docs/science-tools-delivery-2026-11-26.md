# Accessible observation tools: hosted source integration

The standalone application adds Heat & Rain, County Drought and Soil Profile,
with a question-led doorway at `/science`. The existing Labs atlas, Research
Discovery and topic resources remain in place. The new guided entries navigate
directly to their own routes; they do not enter the story-bundle loader or add
new records to the public dataset allowlist.

The copied lab source originates from monorepo commit
`02f2a7c312c449c03e21b8ccaa18f80a99a61d71`, proposed separately in
[PR #6121](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6121).
This hosted integration starts from fresh hosted-branch commit
`c8ec3e02a6378b2e3d544dd63f8ba313f602c60b`. It preserves the existing NEON
terrain, River Flow, Water Chemistry and 2012 Drought Replay tools. The new
county tool covers all 105 counties in 2020–2025; it does not replace the
Finney County 2012 replay.

## Reproduction and source limits

The six display assets and three manifests reproduce byte-for-byte from the
previously saved provider captures. No new provider request is needed to build
or use these tools. Models and captured display bytes retain their monorepo
identity. Preparation scripts use standalone-root paths, with private original
captures required outside this repository. Run the commands in
[Heat & Rain](heat-and-rain-lab.md) and
[County Drought and Soil Profile](drought-and-soil-labs.md) from the application
root. Offline parsing and integrity checks are in
`tests/test_daily_climate_display.py` and
`tests/test_drought_and_soil_display.py`.

All three tools present bounded provider context. Scientific review and KFM
source admission remain PENDING; release remains UNRELEASED. These additions
do not activate a capture worker, alter a map-source registry, change the
existing USCRN pipeline or migrate data stores. Source coverage, raw flags,
missing values, attribution and export settings remain visible.

## Local validation

The shared drought/soil reader also includes the compression correction from
monorepo commit `7ccf135966acf3deb63220347f3bb87eb033f1d2`: Content-Length is
compared with the snapshot size only for identity encoding. Decoded body limits,
exact length and SHA-256 verification still apply to every response. Real gzip
and Brotli HTTP tests accept both tools and reject changed or incomplete bodies.

Production build, TypeScript, the 21 offline parser checks and all 3,761 active
Node tests passed (25 optional tests skipped). The full suite used Node
22.23.3, matching the existing CI workflow. The machine's default 22.13.1 build
lacks SQLite R-tree and FTS5 modules and cannot run 15 existing local-data tests;
the complete rerun on the CI version passed without application changes.

## Publication boundary

A public `/api/build` read on 2026-11-26 identified app `urdng3v1vk` with
1,491 application inputs and digest
`sha256:fc0037f55ea96a2c900a02a42f265cb612e3cda71ffcea75205b05c1d89e6f08`.
It did not provide a source commit (`WORKTREE_MODIFIED`, with one untracked
entry outside application inputs). The clean freshly fetched hosted base had
1,487 inputs and digest
`sha256:49e85947e1d24ae69088b70ce21c20a3deb2db195e623b105e2762e87ea83ce5`.
Those fingerprints differ; this source integration does not identify or
replace the additional live inputs.

Chrome could not attach to the existing GoDaddy dashboard: the browser
integration reported that attachment requires a network policy and an updated
Codex desktop app. The GoDaddy connector does not expose Node app deployment.
No preview update or public publication was attempted. Before publication,
restore dashboard access, re-read its connected branch and Published/Preview
commits, reconcile the live inputs and preserve any unfinished preview work.
Follow `AGENTS.md` and `docs/godaddy-node-preview.md`; local checks and GitHub CI
remain separate from hosted preview, owner release authority and live browser
acceptance.
