<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures/domains/fauna/evidence-bindings
title: Synthetic Fauna EvidenceBundle Binding Inputs
type: fixture-guide
version: v0.1
status: draft
owners: ["@bartytime4life - repository review route; evidence stewardship unverified"]
created: 2026-10-29
updated: 2026-10-29
policy_label: public
owning_root: fixtures/
responsibility: Explain invented metadata inputs for local reference-binding tests
truth_posture: CONFIRMED synthetic fixture; no biological claim or release authority
related:
  - docs/domains/fauna/normalization.md
  - schemas/contracts/v1/evidence/evidence_bundle.schema.json
tags: [fauna, fixtures, evidence, offline]
[/KFM_META_BLOCK_V2] -->

# Synthetic Fauna evidence binding inputs

[`bundles.json`](bundles.json) is a local array of two invented candidate
EvidenceBundles. One declares the source record and raw-artifact checksum
for the existing synthetic observed-open occurrence. The other declares the
snapshot and taxon-evidence refs added by normalization. No source is admitted.

The repeated-digit checksum and `spec_hash` values are **declared test markers**,
not computed payload digests. The binding helper deliberately reports
`integrity_verified: false`, including on the positive path. These inputs
contain no real species observations, private locations, authority assertions,
rights approvals, policy decisions or released artifacts.

Directory Rules sections 7.2 and 12 place reusable synthetic inputs in the
existing `fixtures/domains/fauna/` lane. The
[implementation guide](../../../../docs/domains/fauna/normalization.md) explains
the command, validation boundary and rollback. Tests derive missing, ambiguous,
malformed and mismatched variants in memory; they do not edit this fixture.
