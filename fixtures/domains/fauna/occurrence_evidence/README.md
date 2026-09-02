<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-domains-fauna-occurrence-evidence
title: Fauna OccurrenceEvidence Fixtures
type: fixture-lane-readme
version: v0.1.0
status: synthetic; no-network; public-safe; non-release
owners: OWNER_TBD — Fauna steward · Fixture steward · Sensitivity reviewer · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public-safe-synthetic; fauna; occurrence-evidence; no-live-source; no-publication-authority
related:
  - ../../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
  - ../../../../tests/domains/fauna/test_occurrence_evidence.py
tags: [kfm, fauna, occurrence-evidence, fixtures, negative-tests, geoprivacy, source-role]
[/KFM_META_BLOCK_V2] -->

# Fauna OccurrenceEvidence fixtures

These fixtures are synthetic, no-network, and unsuitable as biological or geographic evidence. The open example uses the non-Kansas coordinate pair `[0, 0]`; the held example carries no coordinate. Names, identifiers, URIs, publishers, methods, and evidence references are fixture-only values.

## Inventory

| Path | Expected posture |
|---|---|
| `valid/valid_observed_open.json` | Structurally and semantically valid direct observation; fixture-only `pass`. |
| `valid/valid_modeled_context.json` | Valid `modeled` record that remains distinct from an observation. |
| `valid/valid_sensitive_withheld_quarantine.json` | Valid sensitive record with withheld public geometry and `quarantine`, proving valid does not mean publishable. |
| `semantic_invalid/modeled_as_observed.json` | Rejects model-as-observation role collapse. |
| `semantic_invalid/observed_without_raw_artifact.json` | Rejects missing source-bound raw-artifact support for an observed record. |
| `semantic_invalid/rights_unresolved_pass.json` | Rejects a claimed pass with unresolved rights. |
| `semantic_invalid/sensitive_exact_without_generalization.json` | Rejects exact public precision when generalization and review are required. |
| `semantic_invalid/spec_hash_mismatch.json` | Rejects mismatched deterministic hash and occurrence identity. |
| `expected_findings_manifest.json` | Canonical exact outcome/code/path manifest for all JSON fixtures above. |

The fixtures do not activate an eBird, iNaturalist, GBIF, BISON, EDDMapS, or other connector and do not establish rights, taxonomic authority, stewardship review, evidence closure, release, or publication.
