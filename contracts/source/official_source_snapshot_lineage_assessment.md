# OfficialSourceSnapshotLineageAssessment Contract

Status: **PROPOSED_INACTIVE** fixture-only profile.

`OfficialSourceSnapshotLineageAssessment` is a deterministic, no-network comparison record for a bounded set of `OfficialSourceSnapshotCandidate` objects from one declared source. It makes volatile-source states explicit without turning source captures into evidence or publication authority.

The profile implements the briefing-integration backlog item to add conflict, correction, supersession, and withdrawal fixture behavior for volatile facts. It remains weaker than `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, review records, correction notices, and release manifests.

## Finite lineage states

- `CURRENT` — one snapshot is the current candidate for later verification.
- `SUPERSEDED` — a preferred newer snapshot supersedes one or more older snapshots.
- `CORRECTED` — a preferred snapshot is explicitly linked to one or more corrected snapshots.
- `CONFLICTED` — two or more snapshots cannot be safely reduced to one preferred candidate.
- `WITHDRAWN` — the compared snapshot set is withdrawn from current-use candidacy.

These are source-lineage assessment states only. They are not KFM lifecycle, evidence, policy, review, release, or public-product states.

## Deterministic identity

`assessment_id` is `kfm:source-snapshot-lineage:` plus the lowercase SHA-256 of canonical sorted-key JSON over every field except `assessment_id`.

## Fail-closed rules

- `snapshot_refs` are unique and lexicographically sorted.
- Every lineage reference must also occur in `snapshot_refs`.
- `CURRENT` requires exactly one snapshot, the same preferred snapshot, and no lineage edges.
- `SUPERSEDED` requires a preferred snapshot and at least one superseded snapshot.
- `CORRECTED` requires a preferred snapshot and at least one corrected snapshot.
- `CONFLICTED` requires at least two snapshots and no preferred snapshot.
- `WITHDRAWN` requires no preferred snapshot and at least one withdrawn snapshot.
- Reason codes are finite and must match the declared lineage state.
- Source activation, EvidenceBundle emission, lifecycle mutation, release, publication, and public-use flags are always `false`.

A passing assessment means only that declared source-snapshot lineage is internally coherent for synthetic or already-captured inputs. It does not verify the source, establish factual truth, choose a legal authority, resolve rights or sensitivity, emit evidence, or authorize correction/release/publication.