<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hazards/nfhl-nld-nid-source-role-profile
title: NFHL/NLD/NID Source-Role Profile
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; hazards; infrastructure; fixture-only; no-authority
owning_root: contracts/
responsibility: Define a bounded source-role, temporal, evidence-support, and public-geometry profile for FEMA NFHL and USACE NLD/NID without creating source, evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED profile; UNKNOWN operational state; NEEDS VERIFICATION human and source-steward review"
related:
  - ../../../schemas/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile.schema.json
  - ../../../fixtures/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile/cases.json
  - ../../../tools/validators/domains/hazards/validate_nfhl_nld_nid_source_role_profile.py
  - ../../../tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py
  - ../../../docs/intake/exploratory/pass-2-nfhl-nld-nid-source-role-profile-source-map.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, hazards, nfhl, nld, nid, source-role, infrastructure, fixture-first, public-safe]
notes:
  - "Adapts Pass 2 cards KFM-P2-IDEA-0026 and KFM-P2-PROG-0008."
  - "NFHL is represented as regulatory flood-hazard baseline, NLD as levee inventory reference, and NID as dam inventory reference."
  - "A passing result establishes synthetic local consistency only; it does not establish current conditions, engineering safety, source admission, evidence resolution, release, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NFHL/NLD/NID Source-Role Profile

> A closed, fixture-only profile that prevents regulatory flood-hazard geometry, levee inventory records, and dam inventory records from collapsing into observed flooding, forecasts, operational condition, engineering safety, or publication authority.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Owning semantic lane | `contracts/domains/hazards/` |
| Machine shape | `schemas/contracts/v1/domains/hazards/nfhl_nld_nid_source_role_profile.schema.json` |
| Live source access | Not performed |
| Source admission, evidence resolution, policy, review, promotion, release, publication | Not performed or authorized |

A validator `PASS` means only that one synthetic candidate obeys the reviewed local grammar, source-role distinctions, deterministic identity, temporal order, evidence-reference closure, and public-geometry safeguards. It is not a regulatory interpretation, flood observation, inundation forecast, levee or dam condition assessment, engineering determination, life-safety statement, or public release decision.

## Source adaptation

Pass 2 proposes a combined FEMA NFHL and USACE NLD/NID implementation lane. This contract preserves the useful shared packet while refusing semantic collapse:

| Source | Profile role | May support | Must not be represented as |
|---|---|---|---|
| FEMA NFHL | `REGULATORY_FLOOD_HAZARD_BASELINE` | Effective flood-hazard mapping context and source-versioned regulatory attributes | Observed flood extent, current inundation, forecast, evacuation or emergency guidance |
| USACE NLD | `LEVEE_INVENTORY_REFERENCE` | Public-safe inventory identity and generalized spatial context | Current operational condition, structural fitness, inspection conclusion, failure probability |
| USACE NID | `DAM_INVENTORY_REFERENCE` | Public-safe inventory identity and generalized spatial context | Current operational condition, structural fitness, inspection conclusion, failure probability |

The sources can participate in explicit `SPATIAL_CONTEXT_ONLY` or `ADMINISTRATIVE_CONTEXT_ONLY` relations. A relation is not proof of causation, protection level, structural state, emergency consequence, or engineering safety.

## Directory Rules basis

ADR-0029 accepts Directory Rules v2. This packet uses existing responsibility roots only:

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/domains/hazards/` |
| Machine shape | `schemas/contracts/v1/domains/hazards/` |
| Synthetic examples | `fixtures/contracts/v1/domains/hazards/` |
| Reusable validation | `tools/validators/domains/hazards/` |
| Enforceability proof | `tests/validators/domains/hazards/` |
| Hosted orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, source registry, connector, policy home, evidence store, lifecycle store, catalog, proof lane, release lane, API, map layer, or public path is created.

## Profile shape

```text
NfhlNldNidSourceRoleProfile
├── profile / status / execution_mode
├── assessment_id
├── sources
│   ├── nfhl
│   │   ├── source identity and regulatory-baseline role
│   │   ├── effective / updated / retrieved time
│   │   ├── evidence_refs
│   │   └── public regulatory geometry boundary
│   ├── nld
│   │   ├── levee-inventory role
│   │   ├── time and evidence_refs
│   │   └── generalized line + transform reference
│   └── nid
│       ├── dam-inventory role
│       ├── time and evidence_refs
│       └── generalized point + transform reference
├── relations
├── claims                         all non-authority assertions
└── spec_hash
```

## Deterministic identity

The profile uses the repository hashing package when available and a bounded canonical-JSON SHA-256 fallback for isolated authoring validation.

`spec_hash` covers `profile`, `status`, `execution_mode`, `sources`, `relations`, and `claims`. `assessment_id` is:

```text
kfm:hazards:nfhl-nld-nid:<spec_hash>
```

The profile additionally requires:

- distinct source-native identity hashes;
- lexically sorted and unique evidence references;
- lexically sorted unique relation identities;
- relation evidence that is a subset of source evidence; and
- ordered times: `source_effective_at <= source_updated_at <= retrieved_at`.

## Missing-data and finite-outcome semantics

| Condition | Outcome |
|---|---|
| Closed schema, identity, time, source roles, support, relations, and public geometry pass | `PASS` |
| A source is `NO_DATA`, populated/empty support lacks evidence, or relation support is unresolved | `ABSTAIN` |
| Source-role collapse, unsafe precision, restricted attribute, time contradiction, identity drift, authority overreach, or unsupported condition/safety claim | `DENY` |
| Input, schema, or fixture manifest cannot be read safely | `ERROR` |

`EMPTY` and `NO_DATA` are distinct. `EMPTY` means an evaluated synthetic scope contains no matching records and still has evidence explaining the result. `NO_DATA` means support is unavailable; it cannot be displayed as zero hazard, zero infrastructure, or safe conditions.

## Public-geometry safeguards

NFHL may retain source-defined public regulatory geometry in this profile because the geometry is part of the regulatory baseline. This does not authorize any public layer.

NLD and NID populated records require generalized public representations and explicit synthetic transform references. Exact gate controls, pump details, restricted attributes, security-sensitive operational detail, or reconstructive precision are denied. A style filter is not a transform and cannot satisfy the requirement.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/hazards \
  --pattern 'test_validate_nfhl_nld_nid_source_role_profile.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/domains/hazards/validate_nfhl_nld_nid_source_role_profile.py \
  --fixtures
```

The frozen fixture matrix contains two `PASS`, two `ABSTAIN`, and ten `DENY` cases. Tests also cover schema closure, source-role anti-collapse, sensitive-detail denial, generalization requirements, temporal order, deterministic identity, relation canonicalization, patched network access, duplicate keys, oversized inputs, symbolic links, deterministic diagnostics, and finite CLI exits.

## Explicit non-goals

This profile does not:

- call FEMA, USACE, FMSC, ArcGIS, REST, WFS, WMS, or any other network service;
- activate, authenticate, cache, poll, or admit a source;
- ingest real NFHL, NLD, or NID identifiers, geometries, attributes, or coordinates;
- infer observed flood extent, current inundation, protection level, structural condition, hazard probability, or engineering safety;
- create an `EvidenceBundle`, `PolicyDecision`, review, proof, promotion record, release manifest, correction notice, or rollback card;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state; or
- add an API, tile, PMTiles archive, MapLibre layer, Evidence Drawer view, Focus Mode answer, deployment, or public product.

## Follow-up boundaries

Independently reviewed work is still required for:

1. current official endpoint, product, identifier, cadence, rights, and attribution verification;
2. source descriptors and admission decisions;
3. source-native version and correction lineage;
4. field-level public-safety policy, including infrastructure-specific restrictions;
5. transform algorithms and `RedactionReceipt` or equivalent authority;
6. EvidenceBundle resolution and catalog closure;
7. public-safe API/layer projections; and
8. correction, withdrawal, cache invalidation, rollback, and release.

Those capabilities must not be activated by editing this fixture profile in place.

## Rollback

Before merge, close the draft pull request and leave its feature branch unmerged. After an authorized merge, revert the bounded implementation commit or merge commit. The rollback removes only the contract, schema, fixture manifest, validator, tests, workflow, source map, and generated authoring receipt. No live source, lifecycle state, policy decision, release, deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
