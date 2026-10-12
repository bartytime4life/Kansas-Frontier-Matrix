# Flow observation: discharge pilot profile v1

Status: bounded implemented candidate contract; source admission and release held.
Owning root: contracts, with machine shape in
`schemas/contracts/v1/domains/hydrology/flow_observation.schema.json`, following
Directory Rules / ADR-0029. Broader hydrology object-family semantics remain in
this directory and the domain doctrine.

The previous permissive empty-object scaffold had no enforced field contract.
This migration closes that shape for `kfm.flow-observation/v1`.
Existing identifiers and old offline request fixtures are retained. It does not
claim compatibility for arbitrary objects that only passed the empty scaffold.
Consumers are the USGS pilot normalizer, candidate validator, catalog preview,
release packager and governed water read projections. Historical receipts are
unchanged. Rollback restores the previous code/schema together; never use a
permissive old schema to approve a newer package.

An observation preserves station and provider series/feature identifiers,
parameter 00060, statistic, method category, observation time, provider revision,
retrieval time, finite nullable value, ft^3/s unit, qualifiers, provider approval
state, provisional flag, observed source role, page digest, evidence reference
and deterministic record identity. Missing values stay null. Revision history
is retained separately; duplicate identities with conflicting same-revision
content quarantine the capture. Provider revision may not precede observation
or follow retrieval. Timestamp precision is preserved to microseconds.

Geometry belongs to verified station metadata, not an inferred river reach.
A station name is not a state/geographic classification. An observed discharge
is not a forecast, flood warning, water-quality claim, regulatory determination
or life-safety recommendation. Provisional values remain subject to revision.

Technical validity and EvidenceBundle resolution are separate from source,
rights, sensitivity, policy, review, release and correction eligibility. The
real pilot is WORK/quarantine-bound and unreleased. See
[water snapshot](../../release/water_snapshot.md) and
[water runbook](../../../docs/runbooks/water-pilot.md) for validation commands,
coverage/freshness behavior, negative outcomes and rollback.
