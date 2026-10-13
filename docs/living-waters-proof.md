<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/site/living-waters-synthetic-proof
title: Living Waters synthetic map proof
type: implementation-note
version: v0.1
status: proposed; repository-candidate; review-required
owners: bartytime4life — issue #3372 owner; independent acceptance pending
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-only; no-admission; no-release; no-deployment-authority
owning_root: apps/
responsibility: Document the bounded synthetic Site map carrier, deterministic validation and local correction/rollback behavior.
truth_posture: CONFIRMED repository implementation and local deterministic checks; PROPOSED review candidate; NOT_RUN browser/WebGL and independent acceptance.
related:
  - ../app/living-waters-control.tsx
  - ../app/living-waters-fixture.ts
  - ../app/living-waters-proof.json
  - ../tests/living-waters-fixture.test.mjs
  - ../../../../pipelines/domains/hydrology/proof_slice.py
[/KFM_META_BLOCK_V2] -->

# Living Waters synthetic map proof

Repository base: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`.
Issue #3372 and its October 8 checkpoint identify the retired Explorer carrier
as an implementation gap. The current Site's provider-backed Living Waters
starting view remains intact; its catalog card now includes **Inspect synthetic
proof**. The fixture is hidden by default and uses no provider route or store.

| Scenario | Packet state | Backend outcome | Presentation |
| --- | --- | --- | --- |
| current | AVAILABLE | ANSWER | Four schematic features; exact synthetic sample |
| stale | STALE | ANSWER | Same fixture with visible STALE label and obligation |
| no-results | NO_RESULTS | ABSTAIN | No features or values; empty reason retained |
| unavailable | UNAVAILABLE | ERROR | No features or values; unavailable reason retained |
| ambiguous-reach | ABSTAIN / AMBIGUOUS | ABSTAIN | No selected reach, features or values |

The checked application projection copies the canonical fixture packet,
EvidenceBundle identity/spec hash, packet digest, five backend envelopes and
proof-record hash. Client selection cannot evaluate policy, admit a source,
resolve a provider or substitute live data. Its schematic positions are authored
display geometry, **not** source geometry or the packet's HUC12 boundary. The
snapshot's all-ones declared digest remains a fixture placeholder, visibly
distinct from the actual packet digest and EvidenceBundle spec hash.

Snapshot reference, gauge metadata and series observation roles stay distinct.
The selected sample is synthetic instantaneous discharge in ft3/s with the
provisional qualifier; it is never a value for a reach, watershed or observed
flood. Numerical uncertainty is unspecified. Packet gauge support is generalized
county; the proof request's HUC12 safety gate does not supply a boundary.
Fixture sample times are exact; changing the Site's general timeline cannot
silently re-date them. AVAILABLE means the finite fixture scenario, never
freshness at the current wall clock. No interpolation is performed.

The control uses only the Site's existing renderer seam and owns one inline
GeoJSON source plus three layers. Visibility, opacity, exact sample selection,
flat-map restrictions, keyboard feature selection and map click inspection are
local. A persistent map label names SYNTHETIC and STALE as applicable, even when
the catalog is closed. Source errors, renderer partial installs, style changes,
scenario changes and closure remove only fixture resources and callbacks.
Synthetic clicks cannot select provider context underneath the schematic.

**Rehearse correction hold** removes values and geometry without changing the
backend envelope or evidence identity. **Restore pinned fixture** restores the
same bytes. This is a local rehearsal, not an invented source correction or
withdrawal. Closing the proof removes its map presentation; no saved workspace,
URL, database or lifecycle state is written. The backend's candidate/rollback
pointer rehearsal remains dry-run only.

## Replay and validation

From the repository root:

```bash
KFM_NO_NETWORK=1 python pipelines/domains/hydrology/proof_slice.py --check-site-carrier
KFM_NO_NETWORK=1 python -m pytest -q tests/domains/hydrology/test_proof_slice.py tests/e2e/test_hydrology_proof_slice.py
make proof-slice
```

When canonical pinned inputs change, generate `--site-carrier` to a temporary
file, then replace `app/living-waters-proof.json` only after the generator exits
successfully. Review the projection and upstream pin changes together.
Hydrology CI runs the currentness test and triggers on this carrier's paths.

From `apps/site/source`:

```bash
node node_modules/typescript/bin/tsc --noEmit --incremental false
npm run build
node --test tests/living-waters-fixture.test.mjs
```

Focused tests cover all five finite outcomes; byte/currentness/evidence identity;
no network, subprocess or writer use during projection; exact sample handling;
roles and non-attribution; correction/restore; inline source installation;
unrelated-ID rejection; late-callback cancellation; partial/async renderer
failure; projection/style cleanup; and default-hidden production catalog output.
These deterministic harness and Worker-render checks do not establish actual
browser/WebGL, touch/device or full accessibility acceptance.

### Local checkpoint — 2026-10-08

- Production build and TypeScript pass.
- Site Node suite: 657 pass, 0 fail, 2 skipped. The skipped installer cases
  intentionally refuse root execution; they are not synthetic map acceptance.
- Focused Site/map-performance/governed-water suite: 18 pass (11 proof-control
  cases). Hydrology proof/E2E/packet suite: 87 pass. The readiness lane retains
  all 14 passing cases, and the committed carrier passes byte-currentness.
- Changed TypeScript lint: 0 errors, 26 warnings with identical rule/message/file
  fingerprints at the exact base; the new control and projector have no warnings.
- Repository topology: 0 invariant failures / 0 new drift, with 113 existing
  baselined warnings. New note metadata passes the required profile.
- Mirror check returns `MIRROR_REVIEW_REQUIRED` on both the exact base and this
  candidate. Renderer acquisition assessment retains `HOLD` for runtime
  admission; these holds are not waived by the application checks.
- Hosted CI, browser/WebGL and independent review are not established here.

## Review and rollback boundary

Revert this bounded candidate together: generator projection, Site control,
catalog binding, focused tests and CI trigger additions. Preserve the original
canonical fixtures, proof profile, EvidenceBundle, historical receipts and
provider-backed Living Waters view. No external data state needs restoration.
An owner-approved deployment would require its own same-Site comparison,
rendered acceptance and version rollback evidence. Historical
`MIRROR_REVIEW_REQUIRED` remains held. This candidate does not close M08,
independent review, live USGS admission, deployment, publication or owner approval.
