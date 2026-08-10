# HUC crosswalk explorer

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0008` into a read-only reviewer
surface for one county/HUC12 crosswalk projection. It can show a finite status,
source hash, digest-bound crosswalk reference, digest-bound validation-receipt
reference, and sorted digest-bound station references.

## Projection boundary

The app-local profile `kfm.explorer.huc-crosswalk.public-safe.v1` accepts only:

- a five-digit county FIPS and 12-digit HUC identifier;
- one finite outcome/status/reason binding;
- a SHA-256 source hash;
- a crosswalk reference whose suffix matches its declared digest;
- a digest-bound validation-receipt reference;
- zero to eight unique, sorted, digest-bound station references; and
- a canonical whole-second UTC evaluation time.

`VERIFIED_EXACT` is the only status that may carry station references and it
must carry at least one. `AMBIGUOUS`, `STALE`, and `UNRESOLVED` bind to
`ABSTAIN`; `RELEASE_DENIED` binds to `DENY`; every non-`AVAILABLE` projection
must omit station references. Unknown fields, mutable references, status drift,
digest mismatch, unsorted or duplicate station references, and invalid time
fail closed to fixed `ERROR` copy with no projection detail.

## Authority boundary

The explorer is a projection consumer. It does not fetch WBD, NHDPlus, NWIS,
or another source; parse a source row; compute or validate a crosswalk; inspect
flow statistics; render geometry; produce a hash or receipt; verify a digital
signature; change ambiguity; evaluate evidence or policy; or approve, release,
deploy, or publish an artifact.

The validation-receipt reference is integrity context, not a claim that the
receipt is cryptographically signed. The surface provides no button, link, or
callback for fetching, editing, overriding, or releasing the crosswalk.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/huc_crosswalk_explorer/` owns fixed display
  behavior.
- `fixtures/ui/huc_crosswalk_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are established responsibility roots under accepted ADR-0029 and
Directory Rules v2. No parallel hydrology, station, crosswalk, receipt,
signature, evidence, policy, or release authority is created.

## Existing hydrology relationship

Current KFM hydrology contracts and validators already own HUC12/COMID and
NHDPlus identity/crosswalk semantics. This component does not replace or import
their canonical objects. A future governed producer must validate those inputs,
apply any separate NWIS station association contract, and emit this exact
public-safe projection. Direct browser reads from canonical manifests or
lifecycle stores are prohibited.

## Production hold

Production wiring remains **HOLD** until hydrology, evidence, privacy, policy,
and release stewards accept a producer for this projection and its station
association semantics. This fixture-first slice does not prove a live source,
real station association, signed receipt, reviewed release, deployment, or
public availability.

## Validation

The existing `ui-build` workflow runs the Explorer build, unit suite, and
headless-browser suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/huc-crosswalk-explorer.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/huc-crosswalk-explorer.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This read-only slice creates no hydrology, evidence, policy, review,
release, deployment, publication, or public-use state to restore.
