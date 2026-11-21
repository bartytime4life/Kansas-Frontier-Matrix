<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-readme
title: Tests — Flora Domain
class: test-readme
version: v0.3.0
status: repository-grounded draft; one bounded executable slice established
truth_posture: CONFIRMED focused synthetic fixture suite / PROPOSED broader Flora coverage / UNKNOWN operational completeness
owner: NEEDS VERIFICATION — Flora steward, test steward, sensitivity/geoprivacy reviewer
created: 2026-07-05
updated: 2026-11-21
policy_label: public; no-network; fixture-only; fail-closed
owning_root: tests/
responsibility: Index the Flora domain tests, the no-network corpus check, and the held placeholders that wait on Flora policies, schemas and code.
related:
  - ../../../fixtures/domains/flora/README.md
  - ../../../tools/validators/domains/flora/README.md
  - ../../../.github/workflows/domain-flora.yml
  - ../../../docs/domains/flora/README.md
notes:
  - "The focused smoke module validates synthetic public-safe fixture conformance only."
  - "Proof and release readiness remain separate explicit holds."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/flora/` — Flora Tests

[![Status: bounded executable](https://img.shields.io/badge/status-bounded%20executable-1a7f37?style=flat-square)](#implemented-slice)
[![Network: blocked](https://img.shields.io/badge/network-blocked-b42318?style=flat-square)](#no-network-contract)
[![Data: synthetic only](https://img.shields.io/badge/data-synthetic%20only-0969da?style=flat-square)](#fixture-contract)
[![Authority: conformance only](https://img.shields.io/badge/authority-conformance%20only-6e7781?style=flat-square)](#limits)

> **Purpose.** Provide deterministic executable checks for Flora behavior without accessing live sources or treating tests as botanical, policy, proof, release, or publication authority.

## Implemented slice

`test_flora_smoke.py` exercises the bounded validator at:

```text
tools/validators/domains/flora/validate_public_safe_fixture.py
```

The suite proves:

- one explicit positive fixture inventory;
- six explicit negative fixtures and exact error sidecars;
- closed object shapes and stable sorted findings;
- strict source-role, taxon-state, rights, sensitivity, review, release, and promotion posture;
- case-insensitive rejection of exact-location aliases and transform-secret fields;
- rejection of URLs, coordinate-like strings, WKT-like strings, and numeric values;
- bounded UTF-8 JSON parsing with duplicate-key, size, depth, node, integer, and non-finite-number rejection;
- regular-file-only input handling;
- machine-readable CLI output and exit codes `0`, `1`, and `2`;
- no candidate-value echoing;
- no socket, DNS, HTTP, or other live-network use by the validator path.

## Fixture contract

The focused suite consumes only:

```text
fixtures/domains/flora/valid/public_safe_occurrence.json
fixtures/domains/flora/invalid/*.json
fixtures/domains/flora/invalid/*.expected_error.txt
```

All examples are synthetic. They contain no real taxa, occurrence coordinates, private-land records, access directions, collection clues, credentials, restricted source payloads, URLs, or geoprivacy transform parameters.

## No-network contract

The unit suite patches common socket and `urllib.request.urlopen` entry points. The validator itself uses only standard-library file, JSON, path, and CLI functionality. CI also sets `KFM_NO_NETWORK=1` and `PYTHONDONTWRITEBYTECODE=1`.

Run from repository root:

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

`test_no_live_network.py` checks the whole directory: it runs every other test module here in a child interpreter whose `sitecustomize` guard refuses and logs DNS lookups and non-local connections, including from that child's own subprocesses. The suite must pass and the log must stay empty.

## Limits

Passing this slice does **not** prove:

- botanical identity or occurrence truth;
- accepted Flora contracts or schemas;
- source admission, rights clearance, or source freshness;
- policy, sensitivity, stewardship, or sovereignty approval;
- execution of a public-safe geoprivacy transform;
- EvidenceBundle or proof construction;
- release readiness, deployment, publication, or public serving.

The `domain-flora` proof and release jobs remain explicit holds.

## Broader coverage

Existing Flora test modules and sublane READMEs remain useful planning and compatibility surfaces. Their presence must not be interpreted as complete domain enforcement. Future slices should be admitted independently with exact fixtures, finite outcomes, no-network tests, documentation, provenance, and rollback.

### Schema coverage

`test_schema_validation.py` checks that every schema under `schemas/contracts/v1/domains/flora/` is valid Draft 2020-12, and that each schema defining fields beyond `id` / `spec_hash` / `version` is listed with the test that accepts and rejects fixtures for it. A scaffold that gains fields without such a test fails with `SCHEMA_VALIDATION_NOT_IMPLEMENTED`.

### Held top-level tests (2026-11-21)

These modules stand in for planned tests whose subjects are still scaffolds. Each fails with its reason code as soon as a subject gains content, so the real tests must land in the same change.

| Module | Held on | Reason code |
|---|---|---|
| `test_taxonomy_reconciliation.py` | `flora_taxonomy_resolution.rego`; `flora_taxon_crosswalk` and `plant_taxon` schemas; `packages/domains/flora/{taxonomy,taxonomy_resolver}` | `TAXONOMY_RECONCILIATION_NOT_IMPLEMENTED` |
| `test_rights_validators.py` | `flora_rights`, `flora_source_role`, `rights` and `source_role` policies; `packages/domains/flora/source_role_resolver` | `RIGHTS_VALIDATORS_NOT_IMPLEMENTED` |
| `test_sensitivity_denial.py` | `geoprivacy` and `sensitivity` policies; `occurrence_public`, `occurrence_restricted` and `rare_plant_record` schemas; `packages/domains/flora/{geoprivacy,geoprivacy_transformer}` | `SENSITIVITY_DENIAL_NOT_IMPLEMENTED` |
| `test_redaction_receipts.py` | `redaction` policy; both `redaction_receipt` schemas; `pipelines/domains/flora/redact`; `data/receipts/flora` | `REDACTION_RECEIPT_NOT_IMPLEMENTED` |
| `test_api_envelopes.py` | `flora_decision_envelope`, `decision_envelope` and `evidence_drawer_payload` schemas | `API_ENVELOPES_NOT_IMPLEMENTED` |
| `test_temporal_logic.py` | `flora_occurrence`, `phenology_observation` and `correction_notice` schemas | `TEMPORAL_LOGIC_NOT_IMPLEMENTED` |
| `test_geometry_validity.py` | both `range_polygon` schemas and `distribution_surface.flora`; `packages/domains/flora/geoprivacy_transformer` | `GEOMETRY_VALIDITY_NOT_IMPLEMENTED` |
| `test_release_manifest.py` | `release_gate` policy; `release_manifest` and `rollback_card` schemas; `release/candidates/flora`; `data/proofs/flora` | `RELEASE_MANIFEST_NOT_IMPLEMENTED` |
| `test_catalog_closure.py` | Flora catalog lanes under `data/catalog/` | `CATALOG_CLOSURE_NOT_IMPLEMENTED` |

[Back to top](#top)
