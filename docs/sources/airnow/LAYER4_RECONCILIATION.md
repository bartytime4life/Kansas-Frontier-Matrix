# AirNow Layer 4 Reconciliation

Offline-only reconciliation/index layer. Inputs are Layer 3 parsed JSONL and parse receipts. No live API/download/network access.

Outputs: site index, site-parameter index, reporting-area index, ZIP/reporting-area index, relationship edges, conflicts, quarantine, reconciliation receipt.

Governance: denies publication, web-service ZIP loops, network paths, secrets, emergency/regulatory claims. AirNow data are preliminary.

`reportingarea.dat` exact layout remains **NEEDS_VERIFICATION** unless separately proven.
