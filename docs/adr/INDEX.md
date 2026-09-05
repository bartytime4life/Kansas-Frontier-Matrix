<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-index
title: Architecture Decision Record Index
type: register-index
version: v1.14
status: draft; repository-grounded
owners:
  - Architecture steward
  - Docs steward
created: 2026-07-22
updated: 2026-09-05
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: canonical human ADR file inventory and decision-status crosswalk without independent acceptance or implementation authority
canonical_for: human ADR file inventory and decision-status crosswalk
numbered_records: 39
unassigned_scaffolds: 12
related:
  - docs/adr/README.md
  - docs/adr/ADR-template.md
  - docs/registers/ADR_INDEX.md
  - docs/doctrine/directory-rules.md
  - tools/validators/validate_adr_index.py
tags: [kfm, adr, index, governance, decisions]
notes:
  - "ADR-0039 registers an unadopted byte-bound Directory Rules amendment; no effective doctrine, projection, enforcement, application migration or release changes. ADR-0029 and ADR-0038 remain unchanged."
  - "ADR-0006 and ADR-0007 transition to accepted together with their source records under the binding maintainer disposition in issue #2957; this records architecture only and does not admit MapLibre, implement a runtime, or change release, deployment, or publication state."
  - "ADR-0029 remains accepted as the Directory Governance Standard v2 decision."
  - "ADR-0038 transitions to accepted under the project-owner decision in issue #4228 comment 5518331532; this accepts the Stage 1 mechanism only, leaves the machine register inert pending exact trusted-main binding, and authorizes no Stage 2 topology transition."
  - "ADR-0037 is registered as proposed and selects a candidate UI-family authority and compatibility plan for EvidenceDrawerPayload; registration is not acceptance and authorizes no dependent migration."
  - "ADR-0036 is registered as proposed; index registration does not accept the planning-encyclopedia carrier, single-writer, generated-mirror, or migration decision."
  - "ADR-0035 remains proposed; registration assigns inventory identity only and does not accept repository-wide numbering or domain-indexing guidance."
  - "Effective status never outranks source-record status or human review."
[/KFM_META_BLOCK_V2] -->

# Architecture Decision Record Index

[![numbered records](https://img.shields.io/badge/numbered_records-39-0969da)](#numbered-records)
[![effective status](https://img.shields.io/badge/effective_status-4_accepted_%7C_35_proposed-1a7f37)](#status-interpretation)
[![scaffolds](https://img.shields.io/badge/unassigned_scaffolds-12-6e7781)](#unassigned-scaffolds)
[![coherence](https://img.shields.io/badge/coherence-machine_checked-1a7f37)](../../tools/validators/validate_adr_index.py)

This file is the canonical human inventory for direct ADR records and unassigned ADR scaffolds under `docs/adr/`. It records what exists and how each record is classified; it cannot accept or promote a decision independently.

> [!IMPORTANT]
> ADR-0006, ADR-0007, ADR-0029, and ADR-0038 have effective status `accepted`. The other 35 numbered records remain `proposed`; no numbered record is `superseded` or `rejected`. ADR-0006 and ADR-0007 accept architecture only—their status does not admit `maplibre-gl`, prove implementation or browser readiness, or authorize release, deployment, or publication. ADR-0038 accepts only the trusted-base correction mechanism; its machine register remains inert until a later exact-binding transition, and Stage 2 remains separate.

## Status interpretation

| Column | Meaning |
| --- | --- |
| **Effective status** | Governance status normalized to `proposed`, `accepted`, `superseded`, or `rejected` |
| **Source metadata** | What the record currently declares: `proposed`, `draft`, `legacy-proposed`, `accepted`, `superseded`, or `rejected` |
| **Supersedes / Superseded by** | ADR-to-ADR relationship only; non-ADR planning artifacts are described inside the record |

`draft` and `legacy-proposed` normalize conservatively to effective `proposed`. An index edit cannot promote a record. A move to `accepted`, `superseded`, or `rejected` requires matching reviewed status in the ADR itself.

## Numbered records

The numbered sequence is complete and unique from `ADR-0001` through `ADR-0039`. ADR-0006, ADR-0007, ADR-0029, and ADR-0038 are `accepted`; all other numbered records remain effectively `proposed`.

<!-- ADR_INDEX_TABLE_START -->
| ID | Record | Effective status | Source metadata | Supersedes | Superseded by |
| --- | --- | --- | --- | --- | --- |
| `ADR-0001` | [Schema Home: `schemas/contracts/v1/` is Canonical](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | `proposed` | — | — |
| `ADR-0002` | [Contracts vs Schemas Split](./ADR-0002-contracts-vs-schemas-split.md) | `proposed` | `draft` | — | — |
| `ADR-0003` | [`policy/` is canonical; `policies/` is compatibility](<./ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | `proposed` | `proposed` | — | — |
| `ADR-0004` | [`apps/governed-api/` is the Trust Membrane](./ADR-0004-apps-governed-api-is-the-trust-membrane.md) | `proposed` | `draft` | — | — |
| `ADR-0005` | [`apps/explorer-web` is the canonical map-first shell](./ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) | `proposed` | `proposed` | — | — |
| `ADR-0006` | [Only `MapLibreAdapter` Imports MapLibre](./ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | `accepted` | `accepted` | — | — |
| `ADR-0007` | [MapLibre GL JS Is the Sole Browser-Side Renderer](<./ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | `accepted` | `accepted` | — | — |
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
| `ADR-0029` | [Adopt Directory Governance Standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md) | `accepted` | `accepted` | — | — |
| `ADR-0030` | [Define the minimum Geology resource-character vocabulary](./ADR-0030-geology-resource-character-vocabulary.md) | `proposed` | `proposed` | — | — |
| `ADR-0031` | [Shared watcher ownership and placement](./ADR-0031-shared-watcher-ownership-and-placement.md) | `proposed` | `proposed` | — | — |
| `ADR-0032` | [Keep attested compute decision-gated and simulation-only by default](./ADR-0032-attested-compute-boundary.md) | `proposed` | `proposed` | — | — |
| `ADR-0033` | [Keep GeoParquet 1.1 as the default and gate 2.0 evaluation](./ADR-0033-geoparquet-version-readiness.md) | `proposed` | `proposed` | — | — |
| `ADR-0034` | [Keep COMPASS qualitative and subordinate to KFM authority gates](./ADR-0034-compass-qualitative-checklist-boundary.md) | `proposed` | `proposed` | — | — |
| `ADR-0035` | [Repository-Wide ADR Identity, Numbering, and Domain Indexing](./ADR-0035-repository-wide-adr-identity-numbering-and-domain-indexing.md) | `proposed` | `proposed` | — | — |
| `ADR-0036` | [Planning Encyclopedia Carrier, Single-Writer, and Scaffold Disposition](./ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md) | `proposed` | `proposed` | — | — |
| `ADR-0037` | [Keep `EvidenceDrawerPayload` authority in the UI family](./ADR-0037-evidence-drawer-payload-ui-authority-and-compatibility.md) | `proposed` | `proposed` | — | — |
| `ADR-0038` | [Trusted-Base Exact Transitions for Frozen-Topology Corrections](./ADR-0038-trusted-base-topology-correction-transitions.md) | `accepted` | `accepted` | — | — |
| `ADR-0039` | [Directory Build and Verification Profiles Amendment](./ADR-0039-directory-build-and-verification-profiles.md) | `proposed` | `proposed` | — | — |
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
| [`NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md`](./NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md) | Consumer-readiness checklist | Validation guidance only |

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
- Proposed ADR-0035 does not resolve domain-local versus repository-wide ADR placement until explicit acceptance.
- Proposed ADR-0036 does not admit or populate `docs/encyclopedia/` until explicit acceptance and a separate implementation change.
- Proposed ADR-0037 does not select `EvidenceDrawerPayload` authority or authorize contract/schema compatibility migration until explicit acceptance and a separate implementation change.
- Accepted ADR-0038 authorizes only the trusted-base exact-transition mechanism. It does not authorize topology-validator consumption or a baseline transition until a later exact register binding is present in the trusted base and Stage 2 is separately implemented.
- It does not accept [`ADR-0011`](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) or authorize migration of `artifacts/release/` or `artifacts/perf/`.
- It treats current `draft` and `legacy-proposed` metadata conservatively as `proposed`; metadata cleanup remains separate work.

## Related

- [ADR operating contract](./README.md)
- [ADR template](./ADR-template.md)
- [Human ADR cross-register](../registers/ADR_INDEX.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [ADR index validator](../../tools/validators/validate_adr_index.py)
- [ADR validator tests](../../tests/validators/test_validate_adr_index.py)
