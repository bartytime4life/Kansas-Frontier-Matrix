<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/retention-agriculture
title: Agriculture retention review runbook
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Agriculture and retention stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Agriculture retention review runbook; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/agriculture/PRESERVATION_MATRIX.md
  - docs/doctrine/retention.md
  - contracts/governance/temporal_retention_disposition_assessment.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Retention Agriculture

Use this runbook to prepare a retention, archival, compaction or erasure review
for Agriculture artifacts. It authorizes no deletion and adopts no calendar
retention duration. The [preservation matrix](../domains/agriculture/PRESERVATION_MATRIX.md)
still labels its per-state defaults and WORK-TTL as proposed/open questions.

## Trigger and required inputs

Start a review for storage pressure, source withdrawal, supersession, changed
rights, correction, expired candidate handling or an independently established
privacy obligation. Obtain exact artifact identities, lifecycle states, source
terms, dependency inventory, intended disposition, decision authority and a
proposed rollback/restore target. Minimize any private farm, operator, parcel or
person-linked material in the review record.

## Preservation worksheet

| Material | Retain or account for before disposition |
|---|---|
| RAW source | Edition, capture digest, permitted custody, history needed for reproduction |
| WORK / QUARANTINE | Candidate reason, review state, retry/re-entry trigger and any bound expiry |
| PROCESSED | Transformation, source identity, units/time/scale and reproducibility |
| Aggregated/generalized output | Named threshold/profile, input lineage and relevant receipt |
| CATALOG / graph references | Resolvable identities and affected dependency edges |
| Published carrier | Manifest, evidence, policy/review, correction and withdrawal route |
| Receipts and proofs | Subject binding and retained audit/reconstruction support |
| Caches and indexes | Dependents that could continue exposing withdrawn material |

A stale source is not automatically a retention failure. Keep freshness status
separate from custody and access decisions. Do not infer that every cached
artifact can be deleted under the same rule as a WORK candidate.

## Review procedure

1. Pin current policy/contract/source decisions and the exact affected version.
2. Inventory direct and derived dependents before choosing a disposition.
3. Explain what historical queries, comparison or reconstruction would be lost.
   Unresolved loss is a review blocker, not a storage optimization detail.
4. Select one proposed action: retain, archive, compact or request separate
   erasure handling. Do not substitute an unreviewed “cleanup” label.
5. For archival, establish complete history, accessible archive reference,
   reversibility, receipt and rollback. For compaction, additionally prove what
   is preserved and what record count/representation changes.
6. Evaluate the bounded fixture profile below when changing its declared
   assessment semantics. It is not a scan of production artifacts.
7. Route the packet to Agriculture, data-custody, evidence, privacy/rights and
   release reviewers as applicable; named assignments remain unverified here.
8. Execute only through a separately authorized, reviewed process. Afterward,
   verify references, dependents, retained evidence and rollback at that scope.

## Available bounded assessment

The [temporal-retention contract](../../contracts/governance/temporal_retention_disposition_assessment.md)
checks declared controls for synthetic `RETAIN`, `ARCHIVE`, `COMPACT` and `ERASE`
proposals. All destructive and governance authority flags remain false.

```bash
python -m unittest -v tests.validators.governance.test_temporal_retention_disposition_assessment
python tools/validators/governance/validate_temporal_retention_disposition_assessment.py --fixtures
```

`PASS` means local coherence for retain/archive/compact, with human review still
required. `ABSTAIN` covers unresolved authority or dependencies; even a declared
verified erasure obligation remains a separate handoff. `DENY` rejects silent
history loss, contradictory policy or forbidden destructive authority. `ERROR`
means no assessment result can be trusted.

## Failure handling and rollback

If a receipt would detach, a released dependent remains active or a restore target
cannot be verified, keep the proposed disposition held. Do not run deletion,
vacuum or object-store expiry commands as a substitute. A rollback plan must
include reference and consumer recovery; merely retaining a filename is not
reconstructability. If erasure is separately required, do not promise restoration
that conflicts with that decision.

## Review completion

Record the proposed action, authority, exact identities, dependency and
lost-query analysis, test results, unresolved questions and authorized next step.
This documentation fills the runbook gap but does not resolve
`OQ-AG-PRES-04`, `OQ-AG-PRES-05` or prove enforcement of retention schedules.
