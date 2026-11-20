<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/hazards/nws-context-ingest-candidate
title: NWS Context Ingest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · Source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-context; not-for-life-safety; no-alert-authority
owning_root: contracts/
responsibility: define a held source-edge projection of existing NWS alert context
truth_posture: CONFIRMED bounded fixture replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# NWS context ingest candidate

`NwsContextIngestCandidate` is a proposed private, held projection of the existing
NOAA connector's `AlertCollectionCandidate`. It carries NWS-authored messages as
source context, evaluated at an explicit instant. It is not a KFM warning,
notification, current-alert determination, hazard observation, operational
instruction, emergency response, public layer or release.

This profile uses the established Hazards ingest candidate homes under ADR-0029.
It references the existing proposed [Atmosphere NWS descriptor](../../../data/registry/atmosphere/sources/noaa_nws.yaml)
without duplicating or admitting it. Cross-domain source use remains unreviewed.
The source role `regulatory` follows the existing NOAA product-role mapping for
NWS-issued context; it does not turn warnings into observed hazard truth. The
connector family descriptor's resolved settings do not resolve this source record.

## Capture, identity and freshness

The first profile accepts only supplied HTTP-200 JSON collections for the fixed
Kansas active-alert URL. It allows 256 KiB and 64 features, rejects duplicate JSON
keys and nonfinite values at any depth, and retains the parser's 32-container
nesting bound. Non-200 responses, including an unbound 304, are refused without
minting an empty capture. No pagination URL is followed. In-memory output is
limited to 4 MiB; no files, alerts or lifecycle artifacts are written.

The exact original body has its own digest and length. Candidate identity hashes
canonical JSON of the source URL and artifact; evaluation time does not change
that capture identity. `spec_hash` binds the entire candidate except itself.
Times normalize to UTC. Evaluation must not precede capture; a message sent after
capture is rejected. Individual sent/effective/onset/expiry/end times stay distinct.

The existing parser computes freshness at `evaluated_at`, retaining supersession
and cancellation lineage. Later reuse must rerun preparation with a new explicit
instant. `WITHIN_SOURCE_WINDOW_AT_AS_OF` is a source-window statement, never the
word “current”, an issue command or a safety determination. Unknown end times
remain unknown; expiry and supersession remain explicit. Missing lineage,
non-Actual status, outside-area messages and inverted expiry remain quarantined.

A further page makes capture `INCOMPLETE_CAPTURE`. An empty collection never
proves no hazards, complete coverage or current safety. Coverage is always
`NOT_ESTABLISHED`. The active surface is not an archive.

## Privacy and denial envelope

Original feature snapshots, including any instructions and unknown source fields,
remain source-faithful private context inside `raw_feature_json`. Instruction text
is not promoted to a field or CLI output. These in-memory snapshots do not prove
persistent capture availability or EvidenceBundle closure. Caller-controlled
captures require private handling; committed fixtures are wholly synthetic.

The final route is always `HOLD`, with source-admission, descriptor, rights and
sensitivity holds. All ten authority flags are false, including alert delivery
and life-safety authority. CLI output contains only finite aggregate state,
counts, reason codes and result hashes. It contains no message IDs, events,
source instructions, source URLs, geometry or UGC codes. KFM sends no alerts.

## Validation and rollback

The [closed schema](../../../schemas/contracts/v1/domains/hazards/nws_context_ingest_candidate.schema.json)
rejects missing/extra fields and authority claims. Runtime validation additionally
checks canonical times, both candidate hashes, body-digest agreement, feature
snapshot hashes and complete parser replay of source snapshots. Rehashing altered
freshness or lineage alone cannot make it valid. This is internal conformance,
not proof of source truth or official-source admission.

The [runbook](../../../docs/runbooks/nws-context-fixture-ingest.md) binds goldens,
negative checks and no-network CI. Revert the complete review unit to restore the
unbound inactive declaration. Preserve earlier receipts and the existing source
record; no provider activation, persistent dataset or release is involved.
