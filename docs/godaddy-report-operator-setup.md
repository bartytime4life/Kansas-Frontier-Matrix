# Report service setup and activation boundary

The public Explorer is already hosted on GoDaddy. The pricing/purchase core
in `server/reports` is a review candidate. Production `/api/reports/quote`
still returns `REPORT_SERVICE_NOT_CONFIGURED`; no live reports are sold.

## Owner configuration

Supply the currency and configured amounts for brief/standard/technical
report value, source-context/corroborated/measured evidence bands, the
replacement-effort hourly rate, minimum/maximum totals and quote lifetime.
Every monetary value is an integer in the currency's minor units. Estimates
must retain their basis; the measured band requires an actual measurement,
method, unit and citation. The implementation has no default sale prices.

Use a versioned server setting, not browser input. `validatePricingPolicy`
rejects incomplete settings. Changing a policy must not rewrite old quotes
or purchased artifacts. The illustrative monetary values in tests are fixtures.

## Merchant connection

An existing Kansas Frontier Matrix Commerce store was observed in the
owner's account. Merchant activation, supported currency, tax treatment and
application API access still need verification. Keep API secrets in GoDaddy's
server environment; never place them in this source tree, chat, public bundles
or report documents. Account ownership verification and financial/legal setup
must be completed directly by the owner when required.

The official `@godaddy/react` 1.0.58 SDK was inspected from the npm registry,
with its SHA-512 integrity verified. Its server export supports a PAT and sends
`CreateCheckoutSession` to
`/v2/commerce/stores/{storeId}/checkout-subgraph`. Checkout supports dynamic
line items via `lineItemData.priceData.unitAmount` and `currencyCode`, hosted
return/success URLs and expiry. The package was not installed or executed.
The generic Commerce reference does not document this full checkout surface;
verify the actual merchant's required scopes, money-unit semantics, checkout
host and payment/order linkage in sandbox before binding an adapter.

The provider adapter must save the checkout session and any verification
secrets privately. A return URL is navigation only. Verify captured payment
on the server using authoritative provider data, matching the actual merchant,
quote reference, integer amount/currency and bound input/source digests.
Do not treat an order's COMPLETED status as payment proof. A pending checkout
may have no transaction ID; captured/refunded transactions require one.
Do not use the Shopping API: it purchases GoDaddy's own products.

## Private storage, identity and generation

Implement `ReportRepository.transaction` with a real private database. Quote
creation and quote ownership are immutable. Order transitions need row locking;
one checkout per quote and one payment consumption per provider transaction
need database uniqueness constraints. Generation leases and artifacts must
survive restarts. The reference store in tests is not a deployment adapter.
Do not reset GoDaddy's shared preview/published database or apply Sites SQLite
migrations to MySQL. Prepare and test an additive schema first.

Resolve `ownerId` from a verified server session. For anonymous purchasers,
use a secure guest session and a tested purchase recovery mechanism. Public
map access must continue without a session. Staff sign-in must verify identity
with a configured provider; server-owned assignments grant only active steward
or admin exemptions. No assignments or sign-in provider currently exist.

Bind `assess` to server-held, rights-eligible source snapshots, not purchaser
claims or browser-only prepared collections. Bind `render` to those same
immutable snapshots; preserve source URLs, roles, units, dates, transformations
and uncertainty. Store completed artifact bytes privately. Only `download`
returns content after current entitlement checks. Other methods return status
and hosted-checkout metadata without report bytes or verification secrets.

## Acceptance required before activation

1. Real database transaction, rollback, concurrent checkout/payment and lease tests.
2. Merchant sandbox checkout, capture, delayed/failed payment and refund verification.
3. Guest-session isolation and recovery; real staff sign-in and assignment revocation.
4. End-to-end wiring of both report workspaces, receipts, status and repeated downloads.
5. Production anonymous map and paid/staff report journeys, including bypass attempts.
6. Multi-layer frame pacing and unchanged source/display data after those integrations.

## Primary references

- https://www.npmjs.com/package/@godaddy/react
- https://github.com/godaddy/javascript
- https://developer.godaddy.com/en/docs/api-users/commerce
- https://developer.godaddy.com/en/docs/references/rest/transactions/get-transaction-by-id
