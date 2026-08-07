# Source adaptation — source-role anti-collapse validator

## Goal

Close a current repository gap without creating a new source-role authority: replace the placeholder plural validator with one canonical, deterministic source-role anti-collapse implementation and a compatibility shim.

## Current repository evidence

At `main@a6bbaa2a7986858bd72629cf3a77181b9e72a761`:

- `tools/validators/source_role/README.md` defines role-fixed-at-admission, claim-role compatibility, anti-collapse, fail-closed conditions, finite outcomes, and a future validator layout, while marking executable behavior as unverified;
- `tools/validators/sources/validate_source_role.py` is a docstring-only placeholder;
- `tools/validators/sources/README.md` classifies `sources/` as a plural compatibility lane and directs real source-role behavior to `source_role/`;
- `schemas/contracts/v1/source/source_descriptor.schema.json` defines the active SourceDescriptor shape and source-role, authority-rank, claim-role, rights, sensitivity, review, release, and lifecycle vocabularies;
- `fixtures/contracts/v1/source/source_descriptor/valid/valid_wbd_huc12.json` provides a current synthetic/public-safe descriptor example.

## Source-derived ideas incorporated

### KFM doctrine

- Source roles are assigned at governed admission and cannot be upgraded downstream.
- Maps, tiles, graphs, exports, embeddings, Focus Mode, and AI are carriers rather than source-role authorities.
- Rights, sensitivity, evidence, review, release, correction, and rollback remain independent controls.
- Unknown or contradictory role posture fails closed.

### Soil and geology domain pressure

The soil planning corpus requires static soil survey, gridded derivatives, station readings, and satellite products to remain separate support types. The geology corpus likewise requires observed, interpreted, modeled, regulatory, production, and public-safe products to remain semantically distinct. This validator supplies a shared anti-collapse mechanism without embedding either domain's vocabulary into a generic source contract.

### Domain-driven design adaptation

The validator is an anti-corruption layer between the SourceDescriptor bounded context and downstream consumer contexts. It preserves a published language—source role, authority rank, and claim roles—without letting downstream code redefine that language.

## Directory Rules basis

| Responsibility | Path |
|---|---|
| Meaning | `contracts/source/source_role_use_request.md` |
| Machine shape | `schemas/contracts/v1/source/source_role_use_request.schema.json` |
| Executable validation | `tools/validators/source_role/` |
| Compatibility only | `tools/validators/sources/validate_source_role.py` |
| Synthetic cases | `fixtures/contracts/v1/source/source_role_use_request/` |
| Tests | `tests/validators/test_validate_source_role.py` |
| CI | `.github/workflows/source-role-anti-collapse.yml` |
| Source adaptation | this file |
| Authoring provenance | `data/receipts/generated/genrec-source-role-anti-collapse-20260807.json` |

No new root or parallel source registry, schema, contract, policy, evidence, proof, receipt, release, or public-runtime home is created.

## Deliberately excluded

- source-role assignment or vocabulary amendment;
- source registry or SourceDescriptor mutation;
- live endpoint fetches or connector activation;
- policy evaluation or rights/sensitivity decisions;
- EvidenceBundle creation or citation authentication;
- promotion, release, publication, or public-surface wiring;
- domain-specific role vocabularies that would collapse soil, geology, atmosphere, biodiversity, or other lane semantics.

## Validation and rollback

The implementation is exercised through exact synthetic PASS, HOLD, RESTRICT, ABSTAIN, DENY, and ERROR cases with a network kill switch. Rollback is a single feature-commit revert; no lifecycle or public artifact is affected.
