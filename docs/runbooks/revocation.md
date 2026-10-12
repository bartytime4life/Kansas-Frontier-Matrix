<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/revocation
title: Revocation routing and evidence handoff
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Consent, rights and release stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Revocation routing and evidence handoff; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/runbooks/people-dna-land/revocation.md
  - docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md
  - contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Revocation

Use this entry point when consent, source rights, access permission or a released
artifact's authority is withdrawn or cannot be confirmed. Its role is routing
and a minimized evidence handoff. Detailed consent-propagation review belongs to
[People/DNA/Land revocation](people-dna-land/revocation.md), which remains the
owning runbook for that bounded profile.

## First classify the request

| Trigger | Primary review route | Key distinction |
|---|---|---|
| Consent withdrawn, expired or out of scope | [Consent runbook](people-dna-land/CONSENT_RUNBOOK.md) and domain revocation procedure | Consent status, cleanup execution and operational closure are different facts |
| Source rights changed | Source/rights steward and affected domain | A public URL is not continuing redistribution permission |
| Evidence or published claim withdrawn | [Evidence correction](EVIDENCE_CORRECTION.md) and release owner | Correction, withdrawal and rollback have separate records |
| Retention/erasure question | [Retention doctrine](../doctrine/retention.md) and privacy/data-custody review | Access denial is not proof of deletion or permission to erase |
| Runtime access no longer valid | Owning runtime/security authority | This documentation cannot disable a service or verify its state |

Use reference IDs, scope and timestamps in public handoffs. Keep real consent
credentials, private locators, names, DNA, protected relationships and precise
sensitive locations in their authorized custody surface.

## Minimal intake record

Capture request/notice identity and origin, observed time, affected authority,
subject/artifact references, claimed effective time, impacted products, current
status, required reviewer roles and unresolved authenticity/scope questions.
Do not assume a sender is authorized to revoke on behalf of a subject, community,
source owner or joint rights holder.

## Propagation review

1. Establish the current status through the owning authority. Unknown status
   must not be treated as continuing permission.
2. Inventory consequential reads, answers, exports, tiles, graphs, indexes and
   caches; include released and copied derivatives where applicable.
3. Identify the required denial, invalidation, withdrawal or separately authorized
   erasure action for each affected surface.
4. Record declared action references and actual execution/readback separately.
5. Verify that evidence, rights, sensitivity, policy and release gates remain
   independent even if the consent dimension is satisfied.
6. Route unresolved execution or receipt-resolution gaps to the owner. A
   declaration saying “purged” is not verification that a derivative is absent.

## Current executable boundary

The [consent-propagation contract](../../contracts/domains/people-dna-land/consent_revocation_propagation_assessment.md)
is inactive and synthetic-fixture-only. It checks an ordered inventory of seven
surfaces: `READ`, `ANSWER`, `EXPORT`, `TILE`, `GRAPH`, `INDEX`, `CACHE`.

- Active, in-scope declared consent can yield `SATISFIED` for that dimension.
- Revoked, expired or out-of-scope consent yields `DENY`.
- Unknown current status yields `ABSTAIN`; failed evaluation yields `ERROR`.
- Receipt references are declarations; the evaluator does not resolve them or
  execute blocking, invalidation, purge, withdrawal or deletion.

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

A pass proves the synthetic profile and expected failure behavior, not real
revocation closure. Follow the detailed domain runbook for its complete review
matrix and graduation gaps.

## Completion, escalation and rollback

A handoff is complete when authority/scope questions, dependency inventory,
required actions, actual evidence and remaining owners are explicit. Operational
closure additionally requires authorized action execution, resolved receipts and
consumer readback; do not claim it from this checklist.

If any dependent can still expose withdrawn material, keep closure pending and
route that concrete surface to its accountable owner. Correct or revert erroneous
documentation through review. Reverting documentation never restores consent,
undoes deletion or reauthorizes a withdrawn release; those decisions must return
to the owning authority.
