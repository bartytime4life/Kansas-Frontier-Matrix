# ADR-001: Public map and server-owned report purchases

**Status:** Proposed; pricing and purchase lifecycle implemented, activation incomplete
**Date:** 2026-10-13
**Deciders:** Project owner for merchant, pricing and staff assignments

## Context

The owner requires a public GoDaddy Explorer and paid reports for everyone
except verified stewards/admins. The map is deployed at commit 49ccc422.
The existing report workspaces produce browser-local drafts; those drafts
cannot serve as authoritative evidence assessments or payment entitlements.
No staff sign-in service, role list or monetary policy was supplied.

An existing Kansas Frontier Matrix Commerce store is visible in the owner's
GoDaddy dashboard. That proves a store exists, not merchant activation or
application API access. GoDaddy's public Commerce documentation exposes
transaction reads and order management; an order marked COMPLETED or a
success redirect does not itself establish captured payment. Hosted report
checkout, verification field semantics and sandbox credentials must be
verified against the actual merchant integration before activation.

## Decision

Keep the public map anonymous. Build a separate server report workflow with
server-resolved source snapshots, versioned owner pricing, purchaser-bound
fixed quotes, private persisted artifacts and verified entitlements. Staff
roles must come from active server assignments after trusted sign-in.
Purchaser submissions must never provide an accuracy grade, price or role.

The pricing foundation captures source times, units, limitations and content
digests. It combines configured product/value and evidence-band amounts with
documented estimated manual effort, using integer minor currency units.
Measured validation is required for the measured tier; no numerical accuracy,
labor rate, currency or sale price is guessed. Insufficient/restricted evidence
is rejected before payment. Already paid purchases retain the quoted terms.

## Options considered

| Option | Complexity | Cost | Durability | Assessment |
|---|---|---|---|---|
| Browser flags and local downloads | Low | Low | Device only | Cannot enforce payment or private delivery |
| GoDaddy Node service with private database and provider checkout | Moderate | Existing hosting plus merchant fees | Requires tested database/storage adapters | Fits the selected host and provider |
| New external report/payment platform | Higher integration work | Unverified | Depends on new service | Adds an account and changes the selected provider |

## Trade-offs and consequences

Server fulfillment can enforce ordinary purchases, verified staff exemptions,
idempotent payment consumption and repeat downloads. It requires persistent
private storage, trusted staff identity, merchant setup and operational recovery.
Public map navigation and its rendering budget stay independent of fulfillment.
Public data and notes already delivered to a browser remain copyable.

## Action items

1. [x] Deploy the public Node map and verify multi-layer performance.
2. [x] Implement and test the configuration-required pricing foundation.
3. [x] Restore and verify the two original email-signing records on both nameservers.
4. [ ] Verify merchant activation, supported hosted checkout and authoritative payment reads.
5. [ ] Configure owner monetary settings and trusted staff identity/assignments.
6. [x] Implement and locally test purchaser isolation, payment consumption, staff expiry, generation leases, retry and repeat downloads against a transactional reference store.
7. [ ] Bind that workflow to a verified GoDaddy payment adapter, real private database/storage, source snapshot resolver and report renderer. The reference store/payment fixtures are test-only.
8. [ ] Connect both report workspaces and verify complete production journeys.

## Primary references

- https://developer.godaddy.com/en/docs/api-users/commerce
- https://developer.godaddy.com/en/docs/references/rest/commerce-scopes
- https://developer.godaddy.com/en/docs/references/rest/transactions/get-transaction-by-id
- https://developer.godaddy.com/en/docs/api-users/commerce/manage-orders-and-customers
