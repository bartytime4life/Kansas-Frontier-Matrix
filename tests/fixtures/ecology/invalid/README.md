<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-ecology-invalid
title: Ecology Invalid Fixtures
type: standard
version: v1
status: active
owners: kfm-data-governance
created: 2026-04-28
updated: 2026-04-28
policy_label: restricted
related: [../README.md, ../valid/README.md, ../policy/README.md, ../../README.md, ../../../README.md]
tags: [kfm, tests, fixtures, ecology, invalid, policy, geoprivacy]
notes: [Negative fixtures for ecology validators; each file is intentionally invalid and should fail a specific gate.]
[/KFM_META_BLOCK_V2] -->

# Ecology Invalid Fixtures

Synthetic negative ecology fixtures used to verify fail-closed schema, policy, rights, identity, and geoprivacy behavior.

> [!IMPORTANT]
> **Status:** active  
> **Owners:** `kfm-data-governance`  
> **Policy label:** `restricted`  
> **Fixture posture:** intentionally invalid; never public-ready
>
> ![status: active](https://img.shields.io/badge/status-active-2ea44f)
> ![policy: restricted](https://img.shields.io/badge/policy-restricted-8b5cf6)
> ![fixtures: invalid](https://img.shields.io/badge/fixtures-invalid-b91c1c)
> ![outcome: fail--closed](https://img.shields.io/badge/outcome-fail--closed-1f6feb)
>
> **Quick jumps:** [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Fixture inventory](#fixture-inventory) · [Rules](#rules-for-this-folder) · [Quick checks](#quick-checks)

## Repo fit

| Field | Value |
| --- | --- |
| Path | `tests/fixtures/ecology/invalid/` |
| Purpose | Negative test payloads for ecology validators and publication/policy gates. |
| Upstream context | [`../README.md`](../README.md), [`../../README.md`](../../README.md), [`../../../README.md`](../../../README.md) |
| Adjacent fixture sets | [`../valid/README.md`](../valid/README.md), [`../policy/README.md`](../policy/README.md) |
| Downstream consumers | Ecology schema and policy tests that assert invalid payloads produce `DENY`, `HOLD`, `ABSTAIN`, or validator `ERROR`. |
| Downstream test paths | **NEEDS VERIFICATION:** exact test-module paths must be confirmed from the mounted repo. |

This folder is part of the KFM evidence-safety test surface. It exists to prove that invalid or unsafe ecology payloads do **not** silently cross into public-ready release posture.

## Accepted inputs

Place files here only when they are:

- Synthetic `.json` payloads.
- Intentionally invalid.
- Focused on one dominant expected failure.
- Useful for ecology schema, policy, rights, identity, or geoprivacy validator coverage.
- Safe to commit without exposing real sensitive coordinates, protected site detail, steward-controlled records, or live occurrence data.

## Exclusions

Do **not** place the following in this folder:

| Excluded material | Where it belongs instead |
| --- | --- |
| Valid ecology fixtures | [`../valid/`](../valid/) |
| Policy-only examples that are not invalid ecology payloads | [`../policy/`](../policy/) |
| Real occurrence records, sensitive coordinates, protected habitat detail, or steward-controlled data | Do not commit; use governed source intake and restricted storage. |
| Fixture documentation that changes suite-level behavior | Parent fixture README or domain test documentation. |
| Validator implementation code | Repo-native validator/tooling path. **NEEDS VERIFICATION:** confirm exact path in mounted repo. |

## Fixture inventory

| File | Primary expected failure | Gate family |
| --- | --- | --- |
| `derived_vegetation_layer.missing_catalog_refs.invalid.json` | Missing `catalog_refs` closure for derived layer payloads. | Catalog closure |
| `habitat_assignment.missing_class.invalid.json` | Missing `habitat_class` on derived habitat assignment. | Derived habitat schema |
| `missing_policy_id.invalid.json` | Missing required `policy_id` for publication decisioning. | Publication policy |
| `observation_plot.unknown_rights.invalid.json` | `rights_status` is `unknown` for a publishable observation payload. | Rights / publication |
| `sensitive_occurrence_record.public_exact_geometry.invalid.json` | Restricted occurrence includes public exact geometry posture. | Geoprivacy / sensitivity |
| `taxon_record.missing_spec_hash.invalid.json` | Missing deterministic `spec_hash`. | Identity / hashing |

## Failure contract

These fixtures are not “bad examples” for manual inspection only. They are regression guards.

```mermaid
flowchart LR
  A[Invalid synthetic fixture] --> B[JSON parse sanity]
  B --> C[Schema / policy validator]
  C -->|expected| D[DENY / HOLD / ABSTAIN / ERROR]
  C -->|regression| E[Accepted as public-ready]
  E --> F[Test failure]
