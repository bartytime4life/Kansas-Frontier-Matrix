<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/roads-rail-trade/tiger-roads-ingest
title: Synthetic TIGER Roads Ingest Packets
type: fixture-guide
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Source steward · Roads/Rail/Trade steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public; source-capture; candidate-only; no-road-authority
owning_root: fixtures/
responsibility: describe sealed synthetic TIGER package inputs and expected held candidates
truth_posture: CONFIRMED synthetic fixture content; no provider geometry or source admission claim
[/KFM_META_BLOCK_V2] -->

# Synthetic TIGER roads ingest packets

`clean.json` and `duplicate-identity.json` embed small deterministic ZIP archives
with invented two-point polyline records, SHX indices, DBF attributes and NAD83
projection text. ZIP timestamps are fixed at 2020-01-01 and the DBF header date
at 2025-01-01; the filename vintage is 2025 and capture time is separately fixed
at 2026-11-19T00:00:00Z. These are not provider data or verified road geometry.

Each packet seals exact bytes and a complete expected held candidate. The clean
fixture has two distinct synthetic LINEARIDs. The duplicate fixture reuses an
ID, producing an explicit quarantine proposal. Both mismatch the unchanged
provider reference and remain held. No state/county DBF columns are present;
filename scope is not fabricated into an observed Kansas feature count.

Use the [runbook](../../../../docs/runbooks/tiger-roads-fixture-ingest.md).
Changing expected values requires deliberate review alongside the implementation
and tests; a fixture match alone grants no public or operational authority.
