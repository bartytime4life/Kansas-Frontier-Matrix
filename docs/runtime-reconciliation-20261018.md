# Runtime reconciliation — 2026-10-18

Status: candidate, review required. Public publication remains on hold. No merge,
source admission, data activation, access change or production-store migration is authorized by this record.

This change carries the previously isolated application-input identity and About guide
from public alignment f37d4c847fef3ff3d96f321341a6de25b3953a1c into the current runtime.
The digest covers application inputs only. It excludes live stores, credentials,
model files and generated assets; it is not a data receipt or proof of hosted equivalence.
Clean Git builds disclose their exact source commit; dirty and archive builds do not
claim a parent commit as their own. The local and hosted profiles are intentionally distinct.

Shared navigation preserves map gestures, keyboard controls, layers, measurements,
reports and exports. Appearance includes Underground; choosing a surface view closes
the cutaway. Legacy Explore panel links resolve to Appearance. The current payload's
county search, outside-click menu dismissal, and Focus Mode provenance regressions
are retained or ported without changing observation values or source permissions.

The local Qwen model, native v268 API capsule and loopback adapters remain local.
Hosted queue/cancellation/completion and source-summary capabilities remain hosted.
The active GPT Public Staging v8 is separately governed and retains its held data;
the original Explorer project was intentionally removed. Historical receipts remain intact.

Rollback: use the pre-change source and prepared-build snapshot together, retain
immutable client assets for open tabs, and restore only the affected Explorer service.
Do not copy stores, model contracts or credentials between runtimes. Review tests,
CI and browser evidence independently; these source changes do not clear publication.

## Development and About follow-up

The normal hot-reload command generates the ignored application identity before
Vite starts, including on a clean checkout. About omits its canonical URL for the
local profile. With the documented `KFM_PUBLIC_ORIGIN=https://kansasfrontiermatrix.com`
it emits `https://kansasfrontiermatrix.com/about`; arbitrary origins are not accepted.
The local loopback link in the page body remains an explicitly local entry point.

The application hosting guide follows this build's source commit (or this local
branch when commit identity is unavailable). Governance and contributor links
explicitly target current `main`. All three originally reported missing targets
exist at `main@907cc58c72844bf56923b63c970b83a202fa5e75`; their absence from this
standalone branch did not establish broken links to `main`.
