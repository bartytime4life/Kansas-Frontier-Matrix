# Explorer reliability review — 2026-10-06

This maintenance pass starts from the current standalone source for Site
`appgprj_6aa0b1c41bc08191bfd86003920f1631`, commit
`6b5477617a0f30bd70b266e3e45d4d0616dcccf8`. The native readback reported
latest saved version 163 and owner-only access. No monorepo or older Site
source was substituted. Existing DB/R2 bindings and protected Earth Engine
features are retained.

## Verified repairs

| Surface | Failure | Repair and proof |
|---|---|---|
| Site-wide dropdowns | Escape also reached the surrounding panel's close handler; pointer focus could leave a modal for the body-mounted menu | Consume Escape at the open dropdown; keep pointer focus on its select and remove option buttons from the Tab sequence. Handler tests exercise dismissal, focus retention, and selection events. |
| Changing dropdown options | Disabled hover could become the active choice, and an option disabled after opening could still be selected | Ignore disabled hover and recheck the live select, option identity, option disabled state, and optgroup state before changing the form value. |
| Report/story preview maps | Later scenes retained the earlier basemap and terrain always used the default provider at 1× | Switch styles when the saved basemap changes; apply the latest scene after style readiness; restore saved provider and scale. Legacy snapshots retain the existing Mapzen/1× fallback. |
| Location-redacted scenes | A redacted scene skipped camera restoration and retained the previous precise view | Reset to the Kansas overview for redacted scenes. Programmatic restoration does not feed camera changes back into comparison synchronization. |
| Preview terrain errors | Terrain setup could return ERROR without presenting a failure | Keep a finite failure message and readable scene details; successful updates recover the preview status. |
| Knowledge record | An unavailable read offered no in-page retry | Retry the same identifier, expose loading state, cancel the previous request, and preserve the reviewed-release result contract. |

Seven focused executable regressions cover these component handlers and mocked
map transitions. They do not run a browser or a real WebGL renderer.

## Page traversal

The locally built production Worker was invoked with HTML requests at
`http://localhost`. No production writes, source activation, model operation,
or provider mutation was performed by this traversal.

| Route | Result | Interpretation |
|---|---|---|
| `/` | 200 | Map shell renders. |
| `/about` | 200 | Help and context boundaries render. |
| `/earth-engine` | 200 | Dataset and recipe workspace renders. |
| `/observatory` | 200 | Event Observatory shell renders. |
| `/observatory/sources` | 200 | Source and coverage directory renders. |
| `/acquisition` | 200 | Acquisition receipt workspace renders. |
| `/knowledge` | 200 | Reviewed knowledge search renders. |
| `/knowledge/record?id=missing` | 200 | Record status shell renders; client read is separate. |
| `/data` | 307 | Unauthenticated request redirects to sign-in with its return path. |
| `/stewards` | 307 | Unauthenticated request redirects to sign-in with its return path. |
| `/earth-engine-context/install` | 404 | Installer is withheld from an unauthenticated request. |

The initial HTTPS-origin in-process traversal did not complete and was
cancelled. The bounded localhost traversal above completed; it does not prove
hosted HTTPS routing or sign-in acceptance.

Validation: production build and TypeScript check passed. The complete test
inventory reports **552 tests: 550 passed, zero failed, two skipped**. The two
skips are local installer mutation/fault tests that intentionally refuse root
execution. Whitespace validation also passed.

## Remaining checks and incomplete capabilities

1. Rendered browser traversal, responsive geometry, actual focus behavior,
   accessibility tooling, and WebGL acceptance remain **NOT RUN**. This managed
   session lacks the required control-browser capability; no alternate browser
   or preview server was installed or started.
2. Provider feed visibility and availability, including smoke, radar, lightning,
   aquifer images and groundwater snapshots, still need a hosted rendered check.
   Adapter and transition tests do not establish that every overlay is visible.
3. Snapshot maps replay registry state, camera, basemap, representation and
   selected terrain. They do not replay the main map's external provider
   overlays. The preview caption now states that limitation. Dated fire,
   research and underground context remains separate from admitted evidence.
4. The knowledge store's live release state, owner acquisition save/readback,
   data contribution, steward review, Earth Engine installer, and local Qwen
   availability require independently authorized runtime verification. The
   unauthenticated page checks cannot establish those flows.
5. Source admission, governed-water activation, evidence release, public access,
   independent review and owner acceptance do not follow from this maintenance
   build or private application deployment.

Recovery: use the retained preceding same-Site saved version 163 if a deployment
rollback is needed. A rollback must preserve newer work and the existing
audience and storage bindings; the v68 preservation record remains historical
recovery evidence.
