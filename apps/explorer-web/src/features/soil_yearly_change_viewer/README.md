# SSURGO yearly change viewer

This inactive Explorer feature adapts Pass 32 card `KFM-P32-FEAT-0018` into a strict, text-first comparison of two consecutive synthetic SSURGO snapshots.

The viewer reports bounded added, removed, and modified record counts; canonical changed-property names; and explicit snapshot, STAC, PROV, receipt, and diff anchors. It labels the result fixture-only and never interprets the counts as real soil change or materiality.

The adapter requires an exact pre-governed projection. Missing or malformed input renders nothing; finite abstain, deny, and error results expose no source, snapshot, digest, receipt, STAC, or provenance detail.

This module is not mounted on a route. It performs no transport, source activation, comparison, digest verification, evidence resolution, lifecycle write, promotion, release, deployment, or publication action.

Validation lives in `apps/explorer-web/tests/soil-yearly-change-viewer.test.ts` and the isolated browser fixture. Rollback is a focused revert of this additive feature packet.
