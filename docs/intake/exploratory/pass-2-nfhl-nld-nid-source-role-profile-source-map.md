<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-2-nfhl-nld-nid-source-role-profile-source-map
title: Pass 2 NFHL/NLD/NID Source-Role Profile Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: implemented-as-draft; exploratory; non-authoritative; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Record the bounded repository adaptation of Pass 2 NFHL/NLD/NID candidates without promoting atlas prose into source, policy, evidence, or release authority.
related:
  - ./pass-2-idea-atlas-import-crosswalk.md
  - ../../../contracts/domains/hazards/nfhl_nld_nid_source_role_profile.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-2, nfhl, nld, nid, hazards, infrastructure, source-role]
notes:
  - "Source cards: KFM-P2-IDEA-0026 and KFM-P2-PROG-0008."
  - "Repository comparison snapshot: main@753cda68c468e8d01457c38e563c107a437aa608."
  - "The source atlas is a downstream carrier; this source map creates no source activation, evidence, policy, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Pass 2 NFHL/NLD/NID source-role profile source map

## Goal

Adapt the next bounded Pass 2 hazards/infrastructure candidate into a deterministic, no-network profile that preserves three source roles and proves fail-closed negative behavior before any connector or public layer work.

## Source cards

| Stable ID | Source proposal | Bounded repository adaptation |
|---|---|---|
| `KFM-P2-IDEA-0026` | FEMA NFHL and USACE NLD/NID as flood and infrastructure authorities | Keep three explicit source roles; do not name the combined packet as one authority. |
| `KFM-P2-PROG-0008` | Ingest NFHL/NLD/NID and deliver compact derivatives with infrastructure safeguards | Implement shape, source-role, time, identity, evidence-support, and public-geometry validation only. No ingestion or derivative production. |

## Repository evidence used

Current `main` already contains FEMA NFHL source documentation and Hazards architecture/trust-boundary material. It did not expose an exact `nfhl_nld_nid_source_role_profile` contract, schema, fixture, validator, focused test, or workflow in repository search at the authoring snapshot.

The new packet therefore extends existing responsibility roots without creating a connector, source descriptor, policy bundle, registry entry, lifecycle record, tile artifact, or public surface.

## Preserved distinctions

- NFHL is regulatory flood-hazard context, not observed or forecast flooding.
- NLD is a levee inventory reference, not current condition or protection assurance.
- NID is a dam inventory reference, not current condition, safety, or failure probability.
- Inventory relations are contextual and cannot become causal or engineering claims.
- NLD/NID public geometry must be generalized before any later public release.
- `EMPTY` is not `NO_DATA`.
- A fixture `PASS` is not source admission, evidence resolution, policy approval, release, or publication.

## Implemented draft packet

| Responsibility | Path |
|---|---|
| Semantic contract | `contracts/domains/hazards/nfhl_nld_nid_source_role_profile.md` |
| Machine schema | `schemas/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile.schema.json` |
| Synthetic fixture matrix | `fixtures/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile/cases.json` |
| Deterministic validator | `tools/validators/domains/hazards/validate_nfhl_nld_nid_source_role_profile.py` |
| Enforceability proof | `tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py` |
| Hosted check | `.github/workflows/nfhl-nld-nid-source-role-profile.yml` |
| Authoring accountability | `data/receipts/generated/genrec-pass2-nfhl-nld-nid-source-role-profile-20260808.json` |

All paths follow accepted responsibility-root placement under ADR-0029. The packet is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`.

## Validation boundary

The frozen matrix contains 14 cases: two `PASS`, two `ABSTAIN`, and ten `DENY`. It covers source-role collapse, observed/forecast/condition claim denial, exact or restricted infrastructure detail, generalization requirements, temporal order, deterministic identity, relation evidence, duplicate identity, canonical ordering, schema failure, no-network behavior, bounded loading, and finite exit codes.

Passing tests establish only local synthetic behavior. Current endpoints, source terms, field schemas, attribution, cadence, identifiers, sensitivity thresholds, source admission, and public fitness remain `NEEDS VERIFICATION`.

## Campaign cursor

After this independent draft slice, the next Pass 2 implementation candidate is the fixture-only ECHO/TRI environmental-facility EvidenceBundle profile. BLM CadNSDI/GLO and WIMAS/WWC5 remain later source-admission work because endpoint, rights, identity, positional-quality, and sensitivity decisions are less closed.

## Rollback

Revert the bounded feature commit or close the unmerged draft pull request. No live source, lifecycle record, public artifact, release, deployment, or publication state is affected.
