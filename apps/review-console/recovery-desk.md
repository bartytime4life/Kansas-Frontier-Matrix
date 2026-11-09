# Feed recovery evidence desk

This browser-local client organizes post-rebuild IEM wind (`iem-wind`), USGS daily observations (`usgs-daily`) and Wikidata Kansas (`wikidata-kansas`) recovery work. It records observations obtained elsewhere. It does not execute feeds, install releases, access an operational database, alter tables or source identities, or authorize any operational step.

The [private hosted workspace](https://kfm-feed-recovery-workspace.blackbart-55.chatgpt.site) was published separately. This repository change does not update or deploy that Site, the public Explorer, a local installed release or any feed service.

## Local use

Use Node 22.13 or newer, from `apps/review-console/recovery`:

```bash
npm ci
npm run typecheck
npm test
npm run build
npm run dev
```

Open `http://127.0.0.1:5179`. The development server has a fixed loopback address and fails if its port is occupied. For the production bundle, use `npm run preview` and open `http://127.0.0.1:4179`.

This app has no server-side record store or authenticated review interface. Use it on the owner's local machine. Its names, excerpts and reviewer decisions are browser-local working attestations, not authenticated KFM ReviewRecords. A static build alone establishes no identity or network-exposure controls; deployment is a separate action.

The original hosted Site, development server and production preview use different browser origins. Records are not automatically synchronized across them. Export a JSON backup and import it into the chosen origin; imported decisions remain historical notes and require fresh local review.

## Evidence states and changing inputs

- Merged source, targeted tests, installed-machine observations, actual feed execution and recovery assessments remain distinct states.
- The source baseline pins PR #5751's exact base, head and merge. Historical failures and KFM test totals are explicitly author-reported; the full reported suite has one failure. The Site/client tests do not rerun that KFM suite.
- Record run identifiers and UTC observation times, actual installed release/commit, catalog identity, database-preservation references, read-only status and journals, provider responses and raw Retry-After, attempts, individual waits and total, cursors, row counts, receipts, reviewer decisions, retests and remaining gaps.
- Empty count fields mean unknown. Contradictory waiting totals need correction. Observations exceeding the 2,700-second source wait budget remain recordable but cannot support a bounded recovery assessment. Provider waits are never shortened or executed here.
- The source-preservation descriptions concern merged implementation, not an inspected database. The IEM PR/runbook station count discrepancy (67 / 68) remains visible.
- Editing appends a run revision and invalidates its active review. The latest observed after-change run determines each feed's recovery summary; later adverse observations reopen gaps while preserving history. A completed run does not mean the whole backlog is finished.
- Acceptance applies only to a named scope and exact revision. A recovery assessment additionally needs the linked evidence, completed run and retest fields. It is reviewer-supported, not independently authenticated or operationally approved.

## Local storage, import and offline operation

Working records live only in browser localStorage. The UI reports actual save attempts. Browser storage is editable and may be cleared; it is not a tamperproof archive. Export includes evidence, all revisions, decisions, import history and seed provenance. The backup size limit is 5 MB; invalid data, missing references and ID collisions are rejected without overwriting existing records. Imported acceptance never becomes active acceptance.

Evidence notes are immutable through the UI; corrections use another note. Pasted data render as text. HTTP/HTTPS references open only on explicit click; local paths remain text. A recorded checksum is not independently verified. No provider link or local reference is fetched automatically.

Use **Backup & offline → Prepare this page for offline review** while the production app is available. The opt-in service worker caches the current shell, explicit script/style assets, the display baseline and already-loaded same-origin resources, excluding API routes. Test a reload and the needed workflows with that origin unavailable before relying on it. External source links and uncached downloads still need a connection. Browser eviction and storage policies may remove caches; keep an exported backup.

Offline review was verified against the original production bundle during Site authoring. Repository integration has its own validation record below; that earlier check does not prove all hosted/private-browser offline behavior.

## Source integration and rollback

The owner requested this repository integration after creating the standalone Site. The starting source is Site source commit `7065895d564dafa025e827ad77421f965159a351` (the first private publication), integrated on repository base `5316e030c86d33d194eebd686d622af55f8bc4ba`.

| Upstream Site path | Path below `recovery/` | Adaptation |
| --- | --- | --- |
| `app/page.tsx` | `src/feed-recovery.tsx` | Local model import and explicit offline-asset discovery; same review UI and evidence behavior |
| `lib/recovery-model.ts` | `src/recovery-model.ts` | Copied without behavior changes |
| `app/globals.css` | `src/styles.css` | Same styling and referenced CSS vendor file |
| `tests/recovery-model.test.mjs` | `tests/recovery-model.test.mjs` | Model import path only |
| `public/{favicon.svg,baseline-evidence.json,recovery-sw.js}` | Same app-local public paths | Copied source/display assets; cache version updated for repository assets |

The repository app uses a small Vite entrypoint instead of the hosted Vinext/Worker scaffold. Vite 8.3.3 follows the existing monorepo override rather than the original Site scaffold version. It imports no hosting project ID, credentials, DB/R2 bindings, unused connector/auth handlers, generated build, real browser notes or QA downloads. Runtime and build dependencies are pinned in the app lockfile. This is an explicit source integration snapshot, not an automatic mirror or a second source/registry/receipt authority.

Offline adaptation explicitly discovers module/style URLs, waits for a replacement service worker to activate, and matches cached fixed `/assets/` files independently of Vite's `Vary: Origin` header. HTML navigation keeps its separate matching rules; API and external provider requests remain excluded. Regression tests cover these cache boundaries and worker replacement.

Directory Rules section 10.1 under accepted ADR-0029 places deployable composition in existing `apps/`; section 10.4 keeps app-local configuration beside its consumer. The `recovery/` subapp is independent of the placeholder parent workspace manifest, like the existing standalone Site source package. Its `.npmrc` disables ancestor npm workspace expansion. `recovery/src/` and `recovery/tests/` are app-local, not new repository roots. The inherited feature-scaffold documents retain their original governance role. Canonical source descriptors, contracts, schemas, policy, lifecycle data, proofs and releases retain their existing owners and homes. No accepted ADR is amended.

The [CI workflow](../../.github/workflows/feed-recovery-workspace.yml) installs the lockfile, checks types, runs the pure model tests and builds this client. It does not deploy, contact providers or validate an installed KFM machine. Current local validation and its limitations are recorded in the pull request. Hosted CI status is separate from local checks.

Rollback is a revert of this bounded app/CI/documentation integration. It does not require an operational database migration, feed-state rewrite, installed-release rollback or hosted Site version change. Preserve/export any browser working records before changing local origins or clearing browser state.
