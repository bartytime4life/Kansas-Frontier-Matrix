# Tiny consent card

Status: **fixture-first Explorer component; not production-wired**.

This feature implements the bounded UI portion of `KFM-P7-FEAT-0002` for a
consent-governed layer. It consumes a strict, public-safe projection and shows:

- the governed basis for asking the viewer;
- the permitted viewing scope;
- the projected expiration;
- subject-inclusion consent as a separate upstream state;
- a local opt-in action, a local withdrawal action, and an obligation-detail
  callback.

## Critical distinction

The card records only whether **this viewer** wants the layer shown in the
current browser session. It does not issue, grant, alter, or revoke a subject's
consent to inclusion.

Required copy is kept literal:

> Your choice controls whether this layer is shown in this browser session. It
> does not grant or revoke a subject's consent to inclusion.

No `view anyway` action exists for `ABSTAIN`, `DENY`, `ERROR`, malformed, or
expired projections.

## Trust boundary

```text
resolved EvidenceBundle / PolicyDecision / PolicyObligationSet upstream
  -> governed public-safe consent-card projection
  -> strict app-local adapter
  -> tiny non-modal card
  -> viewer preference + caller callbacks
```

The implementation:

- performs no fetch or source access;
- reads no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED
  store directly;
- performs no policy evaluation or EvidenceBundle resolution;
- issues no consent credential and changes no subject-consent record;
- never reports a release, publication, or revocation as complete;
- hides the layer by default until a valid `ANSWER` projection is locally
  accepted;
- keeps a withdrawal local even when an optional upstream notice callback
  fails.

`onViewerDecision` receives an event with `affectsSubjectConsent: false`. A
withdrawal event also carries `upstreamNoticeRequired: true`; the component does
not claim that any remote feed was notified.

## Placement basis

- `apps/explorer-web/src/features/consent_card/` owns browser feature behavior.
- `apps/explorer-web/src/adapters/ConsentCardProjection.ts` owns the app-local
  parsing boundary.
- `fixtures/ui/consent_card_projection/` owns synthetic payloads.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are existing responsibility roots under adopted Directory Rules v2. No
new root or parallel contract, schema, policy, evidence, consent, release, or
proof authority is created.

## Production hold

Production wiring remains **HOLD** until a governed API producer is reviewed and
shown to project only released, policy-safe fields from resolved evidence and
obligation state. The component must not parse canonical PolicyObligationSet or
raw consent records in the browser.

## Validation

The repository-owned Explorer workflow runs:

```text
pnpm --filter explorer-web build
pnpm --filter explorer-web test
```

Tests cover valid display, local session persistence, withdrawal behavior,
subject/viewer distinction, expiration, invalid payloads, finite negative states,
no-leak copy, and absence of network/lifecycle-store access.

## Rollback

Revert the feature, adapter, fixtures, tests, and authoring receipt. No database,
source, consent credential, release artifact, cache contract, or external state
requires migration or rollback.
