<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/hazards/nws-context-ingest
title: Synthetic NWS Context Packets
type: fixture-guide
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · Source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-context; not-for-life-safety; no-alert-authority
owning_root: fixtures/
responsibility: describe deterministic private-context capture fixtures
truth_posture: CONFIRMED bounded fixture replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# Synthetic NWS context packets

Three packets seal exact JSON body text, body SHA-256, fixed retrieval/evaluation
times and complete expected held candidates. No packet is a real NWS message,
warning, forecast or operational instruction. All messages have invented IDs,
sender, content and geography codes. Their instruction marker is test text.

- `lineage.json`: two messages, the second an update referencing the first; the
  first stays superseded at the fixed evaluation time.
- `expired-partial.json`: one expired Test message and a next-page marker. It is
  quarantined and incomplete; no URL is followed.
- `empty.json`: zero messages; coverage stays unestablished and output stays held.

Use the [runbook](../../../../docs/runbooks/nws-context-fixture-ingest.md).
Goldens require deliberate review; fixed synthetic capture/evaluation times do
not establish current conditions, source admission or public-use authority.
