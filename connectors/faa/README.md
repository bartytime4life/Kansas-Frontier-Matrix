<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-faa
title: FAA capture adapter
type: readme
version: v0.1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-21
updated: 2026-10-22
owning_root: connectors/
responsibility: Exact FAA product capture into private RAW with held receipts.
truth_posture: CONFIRMED implementation; no source activation or release.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# FAA capture adapter

`capture.py` captures only the inspected October 1, 2026 NASR APT ZIP. It
does not discover a newest download, select preview editions, extract archives,
normalize data, activate a source, or publish. Edition updates require schema
and source review. Its manual callable interface takes an existing private RAW
root; it never accesses or changes the AI PC.

Inputs are the exact product map and an operator-selected private directory.
The existing `tools/local_data/candidate_capture.py` operator boundary validates
the destination before acquisition or replay. Persistent output must be outside
the repository under `KFM_DATA_ROOT/data/raw/`; disposable system-temporary
directories remain available for synthetic tests. Other configured-store lanes,
repository paths, traversal and symlink ancestors are denied. Source capture
does not grant admission or publication authority.
Outputs are an immutable complete capture directory and held retrieval receipt.
Limits are 16 MiB compressed, 20-second socket timeout, 60-second checked
download deadline, and 128 MiB disk reserve. Redirects are rejected. Receipt
and archive fsync precede directory rename; interrupted work is removed and
retried from the beginning. Concurrent captures never replace a complete one.
Replay checks archive digest; a corrupt existing capture fails closed.
The connector buffers at most 16 MiB of archive bytes, then delegates exclusive,
private file writes and complete-directory commit to that shared operator
boundary. Concurrent complete captures do not replace each other. Partial
staging is removed after a failed download or receipt write. The static connector
scanner and its Directory Rules allowlist are unchanged; runtime destination
tests provide separate evidence for the delegated writer.

Use `tools/local_data/faa_airport_rehearsal.py` for private transformation/SQL
rehearsal. `pipelines/domains/roads-rail-trade/faa_airports.py` owns normalization.
`tests/connectors/test_faa_airports.py` proves deterministic failures and replay.
`docs/runbooks/aviation-intake-20261021.md` records exact source discovery,
placement, operational limits, remaining gates and recovery.

OpenSky and adsb.lol adapters return explicit disabled states without network
access. A provider directory entry, public radio transmission, aggregation,
rendering, embedding or AI summary does not grant redistribution permission.

Directory basis: accepted ADR-0029 and Directory Rules `DIR-EXEC-001/002`,
`DIR-SOURCE-003`, `DIR-PLACE-003`. Existing NTAD is a separate BTS-curated
source lane containing only its README at this checkpoint; it is not reused
as FAA authority. Review route is CODEOWNERS; independent admission/release
review is still required. Last reviewed October 22, 2026.
