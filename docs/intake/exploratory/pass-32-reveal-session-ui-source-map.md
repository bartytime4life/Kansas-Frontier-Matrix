<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-reveal-session-ui-source-map
title: Pass 32 Reveal Session UI Source Map
type: exploratory-source-map; implementation-record
version: v0.1.0
status: proposed adaptation; fixture-first; production wiring held
owners: OWNER_TBD — UI steward · Consent steward · Privacy steward · Security steward
created: 2026-08-10
updated: 2026-08-10
policy_label: restricted; exploratory; source-adaptation; no-authority
related:
  - ../../../apps/explorer-web/src/features/reveal_session/README.md
  - ../../../apps/explorer-web/src/adapters/RevealSessionProjection.ts
  - ../../../fixtures/ui/reveal_session_projection/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, pass-32, reveal, ttl, consent, overlay, ui, teardown]
notes:
  - "Records a bounded repository adaptation of KFM-P32-FEAT-0010, KFM-P32-IDEA-0015, and KFM-P32-PROG-0019."
  - "Source candidates do not create policy, credential, key, audit, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Pass 32 Reveal Session UI Source Map

## Source candidates

| Field | Value |
|---|---|
| Atlas | `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` |
| Source document | `New Ideas 5-17-26` (`SRC-P32-002`) |
| Cards | `KFM-P32-FEAT-0010`, `KFM-P32-IDEA-0015`, `KFM-P32-PROG-0019` |
| Atlas status | `NEW` / active / `PROPOSED` |
| Feature statement | Show active reveal state, remaining time, consent scope, and revoke action. |
| Programming statement | On TTL expiry, discard keys, remove overlays, restore obfuscation, and finalize audit. |
| Retrieved evidence | Google Drive source document and supplied consolidated atlas, inspected 2026-08-10. |

## Repository reconciliation

**CONFIRMED at `main@9e76413313b8529091d01be6132d6e987e3f9fae`:**

- Explorer Web already owns strict app-local governed projections, finite
  no-leak view states, Vitest coverage, and Playwright browser fixtures;
- the consent card keeps viewer preference distinct from subject consent, but
  no reveal timer or expiry teardown handler exists;
- the sensitive-overlay gatehouse preflight evaluates only synthetic summary
  declarations and remains `HOLD`, so it is not a browser credential or reveal
  producer;
- repository and pull-request searches found no implementation or open PR for
  the three selected cards; and
- accepted ADR-0029 routes browser behavior, app-local adapters, synthetic UI
  fixtures, tests, exploratory adaptation records, and generated receipts to
  existing responsibility roots.

The MapLibre headless-render candidate was not selected because current main
explicitly holds renderer runtime admission, local render fixtures, and
screenshot/proof claims. This slice does not weaken that hold.

## Bounded adaptation

The implementation adds one strict projection adapter, a timer/teardown
controller, an accessible HUD, four synthetic fixtures, focused unit and
headless-browser tests, this source map, and an authoring receipt.

The projection uses only fixed scope codes and opaque references. The
controller clears its local key reference first, then attempts all four caller
effects in order. Failure or missing wiring results in `INCOMPLETE`; it never
extends the timer, keeps the HUD active, or exposes a re-open action.

## Source-pressure treatment

| Source pressure | Treatment | Boundary |
|---|---|---|
| Visible active state and time remaining | **IMPLEMENTED** | Whole-second HUD driven by an injected/testable clock. |
| Consent scope | **IMPLEMENTED AS FIXED CODES** | No free-form consent or sensitive detail is rendered. |
| Revoke action | **IMPLEMENTED** | Uses the same teardown path as TTL expiry. |
| Discard key | **BOUNDED CLIENT HANDOFF** | Local opaque reference is cleared first, then the caller-owned key store receives a destruction request. |
| Remove overlay and restore obfuscation | **BOUNDED CLIENT HANDOFF** | Both callbacks are attempted; no renderer is activated here. |
| Finalize audit | **BOUNDED CLIENT HANDOFF** | A fixed event is emitted; no audit-store write or receipt claim is made. |
| Production sensitive reveal | **HELD** | Requires reviewed governed API, key store, overlay controller, obfuscation transition, and append-only audit sink. |

## Non-effects and rollback

The slice performs no network request, token verification, policy evaluation,
key generation, source access, sensitive-data read, overlay activation, audit
write, receipt issuance, promotion, release, deployment, or publication.

Before merge, close the draft and abandon its branch. After an authorized
merge, revert the bounded files together and rerun `ui-build`. No external or
public state requires restoration.
