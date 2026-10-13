# Site v259 and main CI reconciliation

Review evidence, 2026-10-13 (America/Chicago). This records a workflow repair,
an owner-private local installation and a public repository mirror candidate.
It does not approve source data, the receipt, release activation or publication.

## Identity and repair

The observed failed main job was governance parity at
`c52ceb2dcc028dd35da266f2c7702ca6fa108e44`, job `115331909385`.
Its push environment supplied literal `HEAD^`; the validator requires a full
immutable commit SHA. The workflow now retains the trusted PR base when supplied
and resolves the parent commit for push/manual runs before validation. Invalid
or unavailable bases fail before invoking the parity target. The validator,
baseline, severity, permissions and inherited-hold boundary are unchanged.

Four regression tests execute the actual workflow shell against disposable Git
history: push parent, PR base, malformed/symbolic base and absent parent. The
real push fallback also completed the full Make target, including receipt replay.
Missing historical objects in the isolated shallow checkout were fetched and
history completed; no Git evidence requirement was bypassed.

Authoritative Site v259 is source
`441c3e29581ffb0293d8e643e5c37eed50319032`, saved version
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_c3fa245c97f08191a8c1110aa4ba521c`,
successfully deployed as `appgdep_6acd77e0e4988191b68fbb4463aa2529`, environment
revision 6. Native archive digest is
`f030a3072fbb2d275422412d48c91fdf64964489c9bad7dfae5181a47ea68073`,
56,401,920 bytes / 428 files. Audience remains one owner, no editors/groups or
external visitors. No source edit, new saved version or Site deployment occurred.

## Preservation and concurrent work

The primary PC repository changed branches during work on another task. A
fast-forward refused safely; this repair neither reset nor overwrote that work.
Subsequent owner merges advanced main, and their changes were reconciled into
this isolated branch. #5110's public subsurface containment and later Qwen/TLS
repairs remain intact. The completed candidate can be copied separately to the
PC without switching the primary checkout beneath another task.

The current local Site alias now uses the exact v259 source in
`KFM-Explorer-Site-aligned-v259-20261013`. All **993 tracked source paths and
428 prepared build files** were byte-verified. The v257 source and build bytes
remain unchanged in their retained folder. Twenty older immutable client assets
remain available for existing tabs. The same v109 persistent-store link, hosting
bindings and dependency lock remain; no migration, reseed or archive write ran.
Only the existing loopback Explorer service was restarted.

An ignored three-file tooling cache was preserved outside the isolated Git root
to satisfy the existing root registry. Read-only dependency-cache writes were
avoided by making a separate unchanged-lock dependency copy. Standalone weather
parity tests used their existing absolute repository-root setting; the Python
reference checks remained mandatory. These environment repairs are not source
or test waivers.

## Mirror and public-data boundary

The [v259 receipt](../../data/receipts/generated/site-v259-alignment-20261013.json)
supersedes the selected v252 comparison for this candidate without rewriting its
predecessor. It records 693 identical paths, 40 inherited repository overlays,
68 repository-only paths, two canonical tool mappings and one canonical document
mapping. The Site's uppercase prepared-review document remains byte-identical at
the repository's existing lowercase path. Mapping checks reject path/digest drift.

**258 exact-geometry source files remain withheld from the public repository**
under merged #5110. They remain recoverable in the private copies. The new receipt
explicitly records this protective exclusion, and checks reject reintroduction,
false counts, invalid digests or unsafe withheld paths. The public repository
worker/build safeguards and held manifest remain; parity does not restore raw
geometry simply to make two file inventories match.

Thus owner-private v259 operation and the public mirror are deliberately distinct
serving boundaries. No exact subsurface publication or human clearance is implied.
Receipt status is REVIEW_ONLY, checker authority CONTENT_PARITY_ONLY, review and
human acceptance pending, and comprehensive hosted equivalence false.

Placement follows adopted Directory Rules v2 / ADR-0029: CI wiring stays in
`.github/workflows`, workflow tests remain in the existing directory-governance
test responsibility, comparison checks stay under `tools/qa`, application
changes stay under `apps/site/source`, review narrative under `docs/reports`, and
process evidence under `data/receipts/generated`. No new authority root is added.

## Executed verification

- Standalone build, TypeScript and 1,154 tests: PASS.
- Composed build and TypeScript after containment: PASS; 1,209 tests after the latest Qwen merge passed;
  the earlier pre-containment 1,213-test run is separate dated evidence.
- Full composed lint: zero errors, 66 existing warnings.
- Parity tests: 17 passed, including four new workflow-shell tests.
- Mirror tests: 38 passed, including canonical-document and withheld-file checks.
- Actual workflow push fallback / complete Make target: PASS, retaining
  HOLD_INHERITED, 93 baselined warnings, zero new topology drift/invariants.
- Installed local and owner-private hosted browser: same High Plains view at
  50 records / 28 columns / one aquifer range, partial coverage and one withheld
  unbounded class. Both completed 2048 × 1718 and 4096 × 3437 surfaces.
- Local keyboard Top/Reset and record-time filtering: 2000 showed 17 records /
  11 columns; All loaded records restored 50/28. Aquifer time remained 2022–2024.
- Closure restored map focus and reduced five canvases to three in both views.
  Final captured warning/error logs were empty. One external-feed issue remained
  disclosed; this is not an all-source-readiness claim.

The source data and Underground/model files in the private v259 copy are unchanged
from retained v257. Browser counts are observations, not independent certification
of provider accuracy. This smoke does not replace physical-device, reduced-motion,
multi-hour, heap/GPU, fully cold-network or hosted rollback acceptance. Final
exact-head CI and later main execution are reported separately on the PR.

## Recovery

Local recovery switches the current alias back to retained v257 and restarts the
same existing service using its same persistent store. No data rollback is needed.
Repository recovery reverts this follow-up while retaining merged #5110 protection;
it must not restore the old public exact-geometry assets. The prior receipt remains
available as historical review evidence. No recovery drill was newly executed here.

## Post-merge concurrent overlay reconciliation

The authorized #5117 merge is `0ccc3b5bc4fe8ebe19f84ea54f1faf32a7ef7030`;
its exact head completed 109 successful and two skipped checks. Concurrent #5118
then merged to `3d5d623df75a7ef366f8f3993ea18b0f2d4cfef8`, changing three
repository Qwen paths. Its changes preserve personal-location privacy,
but its historical v252 receipt did not update the selected v259 comparison.
The existing mirror checker correctly withheld parity for the newer bytes.

The append-only [post-merge receipt](../../data/receipts/generated/site-v259-post-merge-overlay-20261013.json)
records those exact already-merged bytes and retains the previous v259 receipt.
No source, dependency, build, workflow, geometry, Site deployment or approval gate
changes in this follow-up. REVIEW_ONLY / CONTENT_PARITY_ONLY remains explicit;
692 identical paths, 41 inherited overlays, 68 repository-only paths and 258
withheld precise-geometry paths remain. The selected checker and its 38 regression
tests pass. New main CI is evaluated separately; superseded/cancelled jobs are
not failures or passing evidence. The primary PC checkout has a concurrent
workflow edit and its branch/work are preserved; the separate PC repository copy
is the safe synchronization destination.
