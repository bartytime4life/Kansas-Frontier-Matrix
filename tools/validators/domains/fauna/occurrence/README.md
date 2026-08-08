<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-fauna-occurrence
title: Fauna OccurrenceEvidence Validator
type: validator-lane-readme
version: v0.1.0
status: draft; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Fauna steward · Schema steward · Validation steward · Sensitivity reviewer
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; fauna; occurrence-evidence; geoprivacy; fail-closed; no-publication-authority
related:
  - ../../../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../../../fixtures/domains/fauna/occurrence_evidence/
  - ../../../../../tests/domains/fauna/test_occurrence_evidence.py
  - ../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, fauna, occurrence-evidence, validator, source-role, rights, sensitivity, geoprivacy, spec-hash]
[/KFM_META_BLOCK_V2] -->

# Fauna OccurrenceEvidence validator

> Fixture-first deterministic validation for the draft `OccurrenceEvidence` schema and bounded semantic profile. A PASS is not source admission, evidence closure, policy approval, steward review, release, or publication authority.

## Responsibility split

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/domains/fauna/occurrence_evidence.md` |
| Machine shape | `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json` |
| Executable validation | `tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py` |
| Synthetic examples | `fixtures/domains/fauna/occurrence_evidence/` |
| Enforceability | `tests/domains/fauna/test_occurrence_evidence.py` and `.github/workflows/fauna-occurrence-evidence.yml` |

The placement follows accepted ADR-0029: meaning under `contracts/`, shape under `schemas/`, executable checks under `tools/validators/`, and proof of enforcement under `fixtures/` and `tests/`. No new root or parallel Fauna authority is created.

## What the validator checks

The validator:

- applies the closed Draft 2020-12 schema;
- recomputes `spec_hash` from `source_record_id`, `event_date`, normalized geometry, and `accepted_scientific_name` using the repository RFC 8785 JCS + SHA-256 helper;
- binds `occurrence_evidence_id` to the computed digest;
- enforces the canonical seven-class repository `source_role` vocabulary while preserving the Pass 3 `source_family` values;
- rejects role/basis collapse such as a modeled product claiming `human_observation`;
- checks the four normalized rights fields and fails a `pass` result when rights remain unresolved;
- requires a raw-artifact reference for direct, regulatory, administrative, and candidate records;
- checks public-safe geometry, generalization, withholding, and review-state consistency without printing protected values;
- verifies the seven Pass 3 promotion-readiness check booleans; and
- replays an exact positive/negative fixture manifest.

Stable finding families follow the Pass 3 grammar: `prov.*`, `rights.*`, `geom.*`, `sens.*`, `taxon.*`, and `obs.*`, plus `schema.*` and `identity.*` for machine-shape and deterministic-identity failures.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py --fixtures

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_occurrence_evidence.py' \
  --verbose
```

## Trust boundary

The validator reads only the supplied JSON object, the schema, and synthetic fixtures. It does not:

- fetch a live biodiversity source;
- decide taxonomic authority or source admission;
- resolve an EvidenceRef to an EvidenceBundle;
- decide which taxa or sites are sensitive;
- perform or approve a geoprivacy transform;
- create `OccurrencePublic` or `OccurrenceRestricted` records;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data;
- emit a ReleaseManifest, PromotionDecision, or public layer; or
- expose exact location values in findings.

## Rollback

Before merge, close the draft PR and delete its branch. After an authorized merge, revert the additive validator/fixture/test/workflow packet and restore the prior contract/schema blobs. No live source, lifecycle data, release, cache, route, or public artifact requires rollback.
