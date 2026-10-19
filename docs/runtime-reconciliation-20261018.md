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

## Development and navigation follow-up

The hot-reload `npm run dev:local` command generates the ignored application
identity before Vite starts, including on a clean checkout. Production `dev`,
build, start, deployment and storage configuration retain their existing behavior.

Legacy shared URLs with `mapui=open&maptab=navigate`, missing or unknown tool keys,
and restored non-comparison snapshots resolve to Appearance (`scene`). Current
tool keys and comparison precedence remain intact. The primary control contract
is Appearance and Measure, with eight advanced tools; the removed Explore tab is
not advertised by navigation tests.
