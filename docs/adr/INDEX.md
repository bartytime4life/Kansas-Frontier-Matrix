<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-index
title: Architecture Decision Record Index
type: register-index
version: v1.0
status: draft; repository-grounded
owners:
  - Architecture steward
  - Docs steward
created: 2026-07-22
updated: 2026-07-22
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
canonical_for: human ADR file inventory and decision-status crosswalk
numbered_records: 28
unassigned_scaffolds: 12
related:
  - docs/adr/README.md
  - docs/adr/ADR-template.md
  - docs/registers/ADR_INDEX.md
  - docs/doctrine/directory-rules.md
  - tools/validators/validate_adr_index.py
tags: [kfm, adr, index, governance, decisions]
notes:
  - "Inventory verified at main@43f1d97954debda98691b2685c1bb75c4b63c872."
  - "Effective status never outranks source-record status or human review."
[/KFM_META_BLOCK_V2] -->

# Architecture Decision Record Index

[![numbered records](https://img.shields.io/badge/numbered_records-28-0969da)](#numbered-records)
[![effective status](https://img.shields.io/badge/effective_status-proposed-d4a72c)](#status-interpretation)
[![scaffolds](https://img.shields.io/badge/unassigned_scaffolds-12-6e7781)](#unassigned-scaffolds)
[![coherence](https://img.shields.io/badge/coherence-machine_checked-1a7f37)](../../tools/validators/validate_adr_index.py)

This file is the canonical human inventory for direct ADR records and unassigned ADR scaffolds under `docs/adr/`. It records what exists and how each record is classified; it does not accept a proposed decision.

> [!IMPORTANT]
> Every numbered decision below has effective status `proposed`. No tracked numbered ADR provides verified `accepted`, `superseded`, or `rejected` status at the recorded snapshot.

## Status interpretation

| Column | Meaning |
| --- | --- |
| **Effective status** | Governance status normalized to `proposed`, `accepted`, `superseded`, or `rejected` |
| **Source metadata** | What the record currently declares: `proposed`, `draft`, or `legacy-proposed` |
| **Supersedes / Superseded by** | ADR-to-ADR relationship only; non-ADR planning artifacts are described inside the record |

`draft` and `legacy-proposed` normalize conservatively to effective status `proposed`. An index edit cannot promote a record. A move to `accepted`, `superseded`, or `rejected` requires matching reviewed status in the ADR itself.

## Numbered records

The numbered sequence is complete and unique from `ADR-0001` through `ADR-0028` at `main@43f1d97954debda98691b2685c1bb75c4b63c872`.

<!-- ADR_INDEX_TABLE_START -->
| ID | Record | Effective status | Source metadata | Supersedes | Superseded by |
| --- | --- | --- | --- | --- | --- |
| `ADR-0001` | [Schema Home: `schemas/contracts/v1/` is Canonical](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | `proposed` | — | — |
| `ADR-0002` | [Contracts vs Schemas Split](./ADR-0002-contracts-vs-schemas-split.md) | `proposed` | `draft` | — | — |
| `ADR-0003` | [`policy/` is canonical; `policies/` is compatibility](<./ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | `proposed` | `proposed` | — | — |
| `ADR-0004` | [`apps/governed-api/` is the Trust Membrane](./ADR-0004-apps-governed-api-is-the-trust-membrane.md) | `proposed` | `draft` | — | — |
| `ADR-0005` | [`apps/explorer-web` is the canonical map-first shell](./ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | `proposed` | `proposed` | — | — |
| `ADR-0006` | [Only `MapLibreAdapter` Imports MapLibre](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | `proposed` | `draft` | — | — |
| `ADR-0007` | [MapLibre GL JS Is the Sole Browser-Side Renderer](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | `proposed` | `legacy-proposed` | — | — |
| `ADR-0008` | [Ollama and Local AI Runtimes Are Subordinate to the Governed API](./ADR-0008-ollama-subordinate-to-governed-api.md) | `proposed` | `draft` | — | — |
| `ADR-0009` | [Hydrology Is the First Proof-Bearing Lane](./ADR-0009-hydrology-is-the-first-proof-bearing-lane.md) | `proposed` | `draft` | — | — |
| `ADR-0010` | [Deny-by-Default for DNA, Rare Species, Archaeology, and Critical Infrastructure](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | `proposed` | `draft` | — | — |
| `ADR-0011` | [Receipts vs Proofs vs Manifests vs Catalog Separation](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `proposed` | `proposed` | — | — |
| `ADR-0012` | [Connector outputs land in `data/raw/` or `data/quarantine/` only](./ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | `proposed` | `draft` | — | — |
| `ADR-0013` | [`spec_hash` and `run_id` Identity Grammar](./ADR-0013-spec_hash-and-run_id-identity-grammar.md) | `proposed` | `proposed` | — | — |
| `ADR-0014` | [Temporal Vocabulary: Six Time Kinds Tracked](./ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | `proposed` | `proposed` | — | — |
| `ADR-0015` | [`data/published/<domain>/current` is governed by RollbackCard](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | `proposed` | `draft` | — | — |
| `ADR-0016` | [Telemetry Redaction Posture](./ADR-0016-telemetry-redaction-posture.md) | `proposed` | `proposed` | — | — |
| `ADR-0017` | [Source Descriptor Admission Process](./ADR-0017-source-descriptor-admission-process.md) | `proposed` | `proposed` | — | — |
| `ADR-0018` | [Promotion Gate Sequence](./ADR-0018-promotion-gate-sequence.md) | `proposed` | `proposed` | — | — |
| `ADR-0019` | [AI Adapter Contract and Finite Envelopes](./ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | `proposed` | `draft` | — | — |
| `ADR-0020` | [Abstain Is a First-Class Decision](./ADR-0020-abstain-is-a-first-class-decision.md) | `proposed` | `proposed` | — | — |
| `ADR-0021` | [Quarantine has structured exit paths](./ADR-0021-quarantine-has-structured-exit-paths.md) | `proposed` | `proposed` | — | — |
| `ADR-0022` | [Catalog Matrix: STAC + DCAT + PROV Must Agree](./ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | `proposed` | `proposed` | — | — |
| `ADR-0023` | [Geo Manifest Signs Every PMTiles and COG Release](./ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md) | `proposed` | `proposed` | — | — |
| `ADR-0024` | [Steward Separation of Duties for Release](./ADR-0024-steward-separation-of-duties-for-release.md) | `proposed` | `draft` | — | — |
| `ADR-0025` | [Public Client Never Reads Canonical or Internal Stores](./ADR-0025-public-client-never-reads-canonical-internal-stores.md) | `proposed` | `draft` | — | — |
| `ADR-0026` | [Hydrology source spine starts with WBD HUC12](./ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md) | `proposed` | `draft` | — | — |
| `ADR-0027` | [County Focus Mode Control Plane](./ADR-0027-county-focus-mode-control-plane.md) | `proposed` | `proposed` | — | — |
| `ADR-0028` | [State-scale Focus Mode scope and 13-domain coverage rule](<./ADR-0028 — State-scale Focus Mode scope.md>) | `proposed` | `proposed` | — | — |
<!-- ADR_INDEX_TABLE_END -->

## Unassigned scaffolds

These files are tracked but do not carry assigned repository-wide ADR numbers. They are not included in the numbered decision sequence and do not reserve a number.

<!-- ADR_SCAFFOLD_TABLE_START -->
| File | Classification | Decision status |
| --- | --- | --- |
| [`ADR-NNNN-connectors-domain-segment.md`](./ADR-NNNN-connectors-domain-segment.md) | explicit placeholder | `not-assigned` |
| [`ADR-XXXX-atmosphere-advisory-non-life-safety.md`](./ADR-XXXX-atmosphere-advisory-non-life-safety.md) | explicit placeholder | `not-assigned` |
| [`ADR-XXXX-atmosphere-knowledge-character-vocabulary.md`](./ADR-XXXX-atmosphere-knowledge-character-vocabulary.md) | explicit placeholder | `not-assigned` |
| [`ADR-XXXX-atmosphere-schema-home.md`](./ADR-XXXX-atmosphere-schema-home.md) | explicit placeholder | `not-assigned` |
| [`ADR-archaeology-exact-location-policy.md`](./ADR-archaeology-exact-location-policy.md) | slug-only scaffold | `not-assigned` |
| [`ADR-archaeology-source-roles.md`](./ADR-archaeology-source-roles.md) | slug-only scaffold | `not-assigned` |
| [`ADR-focus-model-adapter-boundary.md`](./ADR-focus-model-adapter-boundary.md) | slug-only scaffold | `not-assigned` |
| [`ADR-habitat-fauna-thin-slice.md`](./ADR-habitat-fauna-thin-slice.md) | slug-only scaffold | `not-assigned` |
| [`ADR-habitat-modeled-vs-critical.md`](./ADR-habitat-modeled-vs-critical.md) | slug-only scaffold | `not-assigned` |
| [`ADR-habitat-schema-home.md`](./ADR-habitat-schema-home.md) | slug-only scaffold | `not-assigned` |
| [`ADR-habitat-source-roles.md`](./ADR-habitat-source-roles.md) | slug-only scaffold | `not-assigned` |
| [`ADR-habitat-stewardship-zone-policy.md`](./ADR-habitat-stewardship-zone-policy.md) | slug-only scaffold | `not-assigned` |
<!-- ADR_SCAFFOLD_TABLE_END -->

Assigning one of these scaffolds requires the normal authoring workflow: inspect concurrent work, select a unique number, adopt the template, preserve any useful source attribution, update this index, and complete review. Do not merely rename a scaffold and infer acceptance.

## Support documents

| File | Role | Decision authority |
| --- | --- | --- |
| [`README.md`](./README.md) | ADR operating contract | Does not accept individual decisions |
| [`ADR-template.md`](./ADR-template.md) | Authoring template | No decision |
| [`NEXT_MOVE_ASSESSMENT_2026-05-13.md`](./NEXT_MOVE_ASSESSMENT_2026-05-13.md) | Historical assessment | Planning lineage only |
| [`NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md`](./NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md) | Consumer-readiness checklist | Validation guidance only |
| [`_next_move_log.md`](./_next_move_log.md) | Historical working log | Planning lineage only |

## Validation and change rules

Run:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

Update this index in the same pull request that:

- adds or assigns an ADR number;
- changes a source record's reviewed decision status;
- adds or removes an unassigned scaffold through an explicitly reviewed cleanup;
- establishes or changes an ADR-to-ADR supersession relationship;
- renames a record after inbound-link and migration review.

The validator rejects collisions, missing or extra rows, mismatched filename/H1 IDs, invalid effective statuses, source-status promotion, incomplete scaffold inventory, competing register tables, and broken supersession reciprocity.

## Known limits

- This index does not prove that the architecture described by an ADR is implemented.
- It does not verify GitHub rulesets, independent review, or status-transition authorization outside the repository.
- It does not resolve domain-local versus repository-wide ADR placement.
- It does not accept [`ADR-0011`](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) or authorize migration of `artifacts/release/` or `artifacts/perf/`.
- It treats current `draft` and legacy `PROPOSED` metadata conservatively as `proposed`; metadata cleanup remains separate work.

## Related

- [ADR operating contract](./README.md)
- [ADR template](./ADR-template.md)
- [Human ADR cross-register](../registers/ADR_INDEX.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [ADR index validator](../../tools/validators/validate_adr_index.py)
- [ADR validator tests](../../tests/validators/test_validate_adr_index.py)
