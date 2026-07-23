<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/adr-index
title: ADR Index Cross-Register
type: register-pointer
version: v1.0
status: draft; repository-grounded
owners:
  - Docs steward
  - Architecture steward
created: 2026-07-22
updated: 2026-07-22
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
canonical_adr_index: ../adr/INDEX.md
related:
  - docs/adr/INDEX.md
  - docs/adr/README.md
  - docs/registers/README.md
  - docs/doctrine/directory-rules.md
  - tools/validators/validate_adr_index.py
tags: [kfm, registers, adr, pointer, governance]
notes:
  - "This file is a non-duplicating human cross-register pointer."
  - "The canonical per-record inventory lives only in docs/adr/INDEX.md."
[/KFM_META_BLOCK_V2] -->

# ADR Index Cross-Register

[![register](https://img.shields.io/badge/register-human_pointer-0969da)](./README.md)
[![canonical inventory](https://img.shields.io/badge/canonical_inventory-docs%2Fadr%2FINDEX.md-1a7f37)](../adr/INDEX.md)
[![decisions](https://img.shields.io/badge/decision_authority-source_ADR_only-d4a72c)](../adr/README.md)

This register connects the human register lane to the canonical Architecture Decision Record inventory without copying its rows.

> [!IMPORTANT]
> The canonical ADR inventory is [`docs/adr/INDEX.md`](../adr/INDEX.md). This file must remain a pointer and consumer map. A second ADR table here would create avoidable control-plane drift.

## Register contract

| Field | Value |
| --- | --- |
| Owning root | `docs/` — human-facing control plane |
| Register lane | `docs/registers/` |
| Canonical ADR inventory | [`docs/adr/INDEX.md`](../adr/INDEX.md) |
| ADR operating rules | [`docs/adr/README.md`](../adr/README.md) |
| Current numbered inventory | 28 tracked records, `ADR-0001` through `ADR-0028` |
| Current effective decision status | All `proposed`; no verified accepted record |
| Review route | `@bartytime4life` via `.github/CODEOWNERS` |
| Validation | [`tools/validators/validate_adr_index.py`](../../tools/validators/validate_adr_index.py) |
| Authority limit | Inventory and routing only; never decision acceptance, policy, release, promotion, or publication authority |

## Why this is a pointer

`docs/adr/INDEX.md` owns the exact file-to-ID and status crosswalk because it lives beside the records it inventories. `docs/registers/ADR_INDEX.md` provides the cross-register view needed by doctrine, drift, verification, and control-plane consumers.

Keeping one row source ensures that:

- an ADR addition or status transition has one human inventory to update;
- register readers can discover the canonical decision lane;
- validators can reject missing, extra, or conflicting rows deterministically;
- presence, status, acceptance, implementation, and release authority remain separate facts.

## Inputs and consumers

| Direction | Surface | Relationship |
| --- | --- | --- |
| Upstream | [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Defines placement, status vocabulary, and ADR triggers |
| Canonical record set | [`docs/adr/`](../adr/) | Holds numbered records, scaffolds, template, and canonical index |
| Drift input | [`DRIFT_REGISTER.md`](./DRIFT_REGISTER.md) | Placement or authority conflicts may require an ADR |
| Verification input | [`VERIFICATION_BACKLOG.md`](./VERIFICATION_BACKLOG.md) | Checkable unresolved questions may mature into ADRs |
| Machine control plane | [`control_plane/`](../../control_plane/) | May reference decisions; does not replace human ADR records |
| Enforcement | [`tools/validators/validate_adr_index.py`](../../tools/validators/validate_adr_index.py) | Checks file/index/status/supersession coherence |
| CI | [`.github/workflows/docs-control-plane.yml`](../../.github/workflows/docs-control-plane.yml) | Runs the read-only coherence gate |

## Update protocol

1. Update the source ADR and [`docs/adr/INDEX.md`](../adr/INDEX.md) together.
2. Run the ADR index validator and its negative-path tests.
3. Change this pointer only when its contract, canonical target, summary, consumers, or validation path changes.
4. Keep proposed decisions proposed until their source records carry explicit reviewed status.
5. Preserve superseded and rejected records; never delete decision history.

## Validation boundary

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

A green result confirms the checked revision has one coherent human ADR inventory, valid ID/status/link relationships, complete scaffold separation, and this canonical pointer. It does not establish that any decision was correctly accepted, implemented, enforced across all runtime paths, or approved for release or publication.

## Open governance work

- Human status review for the 28 numbered ADRs.
- Metadata normalization for records whose source metadata says `draft` or uses legacy structure.
- Domain-local versus repository-wide ADR placement reconciliation.
- Review of proposed ADR-0011 before any `artifacts/release/` migration.
- Resolution of `OPEN-DR-09-b` and the `artifacts/perf/` placement conflict.

## Related

- [Canonical ADR index](../adr/INDEX.md)
- [ADR operating contract](../adr/README.md)
- [Registers README](./README.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Drift Register](./DRIFT_REGISTER.md)
- [Verification Backlog](./VERIFICATION_BACKLOG.md)
