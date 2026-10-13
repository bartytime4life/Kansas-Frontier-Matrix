# Site source reconciliation — 2026-10-06

This update reconciles the existing owner-private Explorer's v164 source
`5a2c8f05c76ceadcf141fe95a140564ed89f7484` with the Site changes already merged
into KFM repository main `07e6b26c3ba0cd1c689de29fa2c07d0a30c26ae5`.

The v164 dropdown, saved-map privacy/terrain, and knowledge retry repairs are
retained. Five repository files carry forward the Sharp 0.35.5 override and the
shared MapLibre/worker construction boundary. Two component test fixtures now
record instances without violating the existing lint rule; their assertions and
behavior are unchanged. Source differences were compared before copying; no
older Site, data collection, or configuration replaced the current application.

Validation of the combined source: production build and TypeScript passed;
552 Node tests passed with none skipped. Lint has zero errors and 46 existing
warnings. This is not full security clearance or browser/WebGL acceptance.
The repository's historical mirror-review receipt remains independently held;
this source reconciliation does not rewrite it or imply reviewed equivalence.

Local installation preserves the `http://127.0.0.1:4173` origin and the physical
v109 D1/R2 state. A new stopped-writer backup, isolated rehearsal, and guarded
alias change are required before declaring the local installation complete.
The prior v163 application is retained for source rollback; never restore an
older database over subsequent writes. Hosted rollback selects the prior saved
v164 version, independently of the local source alias.

Data-refresh candidates are retained outside application and repository source.
Provider observations, local captures, and derived review snapshots retain their
own timestamps and validation state. A failed review remains held; no refresh
admits, activates, or releases it. Existing audience and DB/R2 bindings remain.

Placement reuses this application's `app/`, `tests/`, and `docs/` responsibilities,
mirrored under `apps/site/source`, under accepted ADR-0029 and Directory Rules
v2. External RAW and QUARANTINE lanes retain data identity and authority.
