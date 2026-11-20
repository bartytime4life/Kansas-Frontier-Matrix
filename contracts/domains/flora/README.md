<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-readme
title: Flora Contracts
type: readme
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Flora steward · iNaturalist source steward · Rights and sensitivity reviewers · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-source-candidates; no-public-coordinates
owning_root: contracts/
responsibility: index Flora semantic contracts and their authority boundaries
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION cross-domain source admission, human review and downstream use
[/KFM_META_BLOCK_V2] -->

# Flora Contracts

This lane owns human-readable Flora object meaning. Machine shape belongs in
`schemas/`, admissibility in `policy/`, executable behavior in `pipelines/` and
`packages/`, source acquisition in `connectors/`, lifecycle artifacts in `data/`
and release decisions in `release/`. This index grants no source or release authority.

## Current bounded source-edge contract

The proposed [iNaturalist ingest candidate](inaturalist_ingest_candidate.md) pairs
with a [closed schema](../../../schemas/contracts/v1/domains/flora/inaturalist_ingest_candidate.schema.json),
synthetic fixtures, replay validation and a no-network workflow. It preserves
source geoprivacy/rights and unknown plant lineage, minimizes nested user objects
and remains private and held. The referenced Fauna source template is unresolved;
Flora use requires separate review. This candidate is not a normalized FloraOccurrence
or a taxonomy/sensitivity/redaction decision.

Other domain contract files, including [flora_occurrence.md](flora_occurrence.md)
and [redaction_receipt.md](redaction_receipt.md), retain their own proposed semantics
and verification limits. This index does not claim those object families are
implemented or source-approved.

## Review and correction

Contract, schema, fixture, validator, test and workflow changes require maintainer
and relevant domain/source/rights/sensitivity review. See the
[runbook](../../../docs/runbooks/inaturalist-fixture-ingest.md) for bounded validation.
A pass establishes conformance only. Correct through reviewed versioned changes,
preserve historical receipts, and keep unresolved candidates held.
