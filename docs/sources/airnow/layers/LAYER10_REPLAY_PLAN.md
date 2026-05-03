# AirNow Layer 10 Replay Plan

Internal replay planning only.

Layer 10 reads local Layer 9 verification outputs and local replay target manifests for Layers 6–9, then creates deterministic replay planning artifacts (DAG, step plan, command catalog, blockers, preflight, status board, runbook, receipt). It does not execute replay commands by default, apply patches, close tasks, or create GitHub issues/PRs.

AirNow caveats: AirNow data are preliminary and subject to change; AirNow is not EPA AQS/AirData regulatory data. Official regulatory air-quality data must come from EPA AQS/AirData.

Denied capabilities: publication, dashboard, tiles, public API, emergency alerts, regulatory claims, exact-sensitive overlays, auto-execute, auto-apply, task closure, GitHub issue/PR creation, and git push.

Next layer proposal: Layer 11 should intake manually executed replay results and compare local replay receipts against Layer 10 expected outputs, while remaining offline and non-executing.
