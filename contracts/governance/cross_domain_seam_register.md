<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/cross-domain-seam-register/v1
title: Cross-Domain Seam Register Contract
type: semantic-contract
version: v1
status: draft; PROPOSED; projection-only; no-join-authority
owners: OWNER_TBD — Architecture steward · Domain stewards · Policy steward · Evidence steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; governance; cross-domain; context-map; published-language; fail-closed
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/DOMAIN_LANE.md
  - ../../control_plane/domain_lane_register.yaml
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../schemas/contracts/v1/governance/cross_domain_seam_register.schema.json
  - ../../tools/validators/directory_governance/validate_cross_domain_seam_register.py
notes:
  - "A validated seam entry records a proposed context boundary and hold; it does not authorize a join, mutate another domain, admit a source, release data, or publish a composed claim."
[/KFM_META_BLOCK_V2] -->

# Cross-Domain Seam Register Contract

## Purpose

The `CrossDomainSeamRegister` is KFM's machine-readable **Context Map projection** for high-risk relationships between registered domain lanes. It records which bounded contexts participate, which concepts each context owns, which inferences remain prohibited, and which evidence, source-role, policy, sensitivity, and release rules must remain visible before any composed claim is considered.

The register follows two operating rules:

1. A domain may publish an interface that another domain cites, but the consumer does not modify the owner's records or redefine their meaning.
2. A cross-domain composition applies the most restrictive relevant evidence, policy, sensitivity, precision, review, and release posture.

This is a proposed governance projection, not a join engine, public API, policy evaluator, or release decision.

## Initial scope

Version 1 covers five high-risk seams already emphasized in KFM doctrine:

| Seam | Boundary preserved |
|---|---|
| Agriculture × Soil | Soil suitability context cannot become private farm/operator/parcel/yield disclosure or observed yield. |
| Archaeology × Roads/Rail/Trade | Historic corridors do not disclose archaeological provenience or precise cultural locations. |
| Atmosphere × Hazards | Observation, forecast, model, regulatory context, event, and advisory roles remain distinct. |
| Fauna × Hydrology | Public HUC/reach identity cannot reveal precise sensitive occurrence or imply an established population. |
| Hazards × Settlements/Infrastructure | Exposure summaries cannot reveal precise critical-asset locations or redefine asset identity. |

Coverage is deliberately `partial`. The register does not claim every valid seam, every cross-cutting scope, or every published-language term is represented.

## Entry semantics

Each entry records:

- a deterministic `seam_id` beginning with two lexically ordered registered domain IDs;
- exactly two participating bounded contexts;
- one authority allocation per participant;
- concepts owned by each participant;
- `may_modify_other_context: false` for both participants;
- a bounded relation summary;
- explicit prohibited inferences;
- `HOLD_UNRESOLVED` while no reviewed seam contract and accepted cross-lane decision exist;
- `public_join_allowed: false` and a null `seam_contract_path` in this first projection.

The shared defaults require an `EvidenceBundle` from each participant, preserve source roles, apply the most restrictive policy and sensitivity posture, require each participant's released support, and grant no mutation or publication authority.

## Finite validator outcomes

- `PASS` — the register consistently represents its proposed holds and authority boundaries.
- `FAIL_NEW_DRIFT` — an unknown lane, new unregistered seam, duplicate identity, or root-level seam path appears.
- `FAIL_INVARIANT` — ownership, evidence, source-role, sensitivity, policy, release, or public-use constraints are weakened.
- `HOLD_UNRESOLVED` — required doctrine, decision, lane-register, or future seam-contract evidence is absent.
- `ERROR_VALIDATOR` — input, parsing, schema, repository-root, or bounded-evaluation failure.

`PASS` does not mean a cross-domain join is approved.

## Published-language boundary

This register is a precursor to a project-wide Published Language. It exposes only stable seam identity and governance constraints. Domain-internal schemas, RAW/WORK/QUARANTINE identifiers, restricted reasons, precise sensitive values, and implementation-specific storage details are not public vocabulary.

A future active seam requires a separate semantic contract under the Directory Rules cross-domain seam home, an accepted decision, compatible schemas, policy tests, fixtures, evidence closure, release rules, correction behavior, and rollback support.

## Directory Rules basis

The register's meaning belongs in `contracts/governance/`; its machine projection belongs in `control_plane/`; its shape belongs in `schemas/contracts/v1/governance/`; deterministic enforcement belongs in `tools/validators/directory_governance/`; synthetic replay material belongs in `fixtures/contracts/v1/governance/`; and focused conformance belongs in `tests/validators/directory_governance/`.

No domain or seam becomes a repository root. A future seam-specific semantic contract follows `contracts/cross_domain/<seam_id>/` only after placement, ownership, and decision evidence are reviewed.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_cross_domain_seam_register.py' \
  --verbose

python tools/validators/directory_governance/validate_cross_domain_seam_register.py
```

## Rollback

Close the draft pull request or revert the bounded implementation commit. The register does not execute joins, mutate domain records, activate sources, write lifecycle state, release, deploy, promote, or publish, so rollback requires no data or public correction migration.
