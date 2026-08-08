<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-fauna-occurrence
title: Fauna OccurrenceEvidence Validator
type: validator-lane-readme
version: v0.2.0
status: draft; fixture-first executable confirmed; no-network; non-authoritative
owners: OWNER_TBD — Fauna steward · Schema steward · Validation steward · Sensitivity reviewer
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; fauna; occurrence-evidence; geoprivacy; fail-closed; no-publication-authority
owning_root: tools/
current_path: tools/validators/domains/fauna/occurrence/README.md
responsibility: Document the bounded deterministic OccurrenceEvidence validator, its exact CLI and finding contract, its direct repository dependencies, and the authority it does not possess.
truth_posture: CONFIRMED current repository implementation; PROPOSED draft profile; NEEDS VERIFICATION live-source, policy, steward, proof, release, and public-use adoption
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ./validate_occurrence_evidence.py
  - ../../../../../contracts/domains/fauna/occurrence_evidence.md
  - ../../../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../../../../fixtures/domains/fauna/occurrence_evidence/
  - ../../../../../tests/domains/fauna/test_occurrence_evidence.py
  - ../../../../../packages/hashing/
  - ../../../../../.github/workflows/fauna-occurrence-evidence.yml
  - ../../../../../data/receipts/generated/genrec-fauna-occurrence-evidence-readme-20260808.json
  - ../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fauna, occurrence-evidence, validator, source-role, rights, sensitivity, geoprivacy, spec-hash, no-network]
notes:
  - "v0.2.0 reconciles this README with the executable, closed schema, semantic contract, exact fixture manifest, focused tests, and dedicated workflow merged by PR #2209."
  - "The validator reports bounded conformance only. It does not admit a source, resolve evidence, decide policy or stewardship, transform protected geometry, release, promote, deploy, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna OccurrenceEvidence validator

`tools/validators/domains/fauna/occurrence/`

![status](https://img.shields.io/badge/status-draft-yellow)
![implementation](https://img.shields.io/badge/implementation-fixture--first-orange)
![schema](https://img.shields.io/badge/schema-Draft%202020--12-blue)
![network](https://img.shields.io/badge/network-denied-red)
![authority](https://img.shields.io/badge/authority-validator--only-lightgrey)

> **One-line purpose.** Deterministically validate one or more local draft `OccurrenceEvidence` JSON records against the closed machine shape and bounded Fauna semantics without fetching a source, exposing protected values, or creating publication authority.

> [!IMPORTANT]
> A CLI `PASS` means only that the supplied record is internally consistent with this draft schema and validator profile. It is not source admission, `EvidenceBundle` closure, policy or steward approval, geoprivacy transformation, release readiness, promotion, deployment, or publication.

## Quick navigation

[Purpose](#purpose) · [Current implementation](#current-implementation) · [Responsibility split](#responsibility-split) · [Input profile](#input-profile) · [Validation pipeline](#validation-pipeline) · [Outcomes and exit codes](#outcomes-and-exit-codes) · [Finding contract](#finding-contract) · [Commands](#commands) · [Fixtures and tests](#fixtures-and-tests) · [CI and receipt](#ci-and-generated-receipt) · [Trust boundary](#trust-boundary) · [Maintenance](#maintenance-checklist) · [Rollback](#correction-and-rollback)

## Purpose

This lane documents and runs the repository's bounded, fixture-first validator for the draft `OccurrenceEvidence` profile. The validator checks a source-bound Fauna occurrence candidate before any policy-controlled split into public or restricted derivatives.

It is intentionally local and deterministic:

- input is one or more repository-local JSON files, or the declared synthetic fixture manifest;
- the closed Draft 2020-12 schema is evaluated before semantic checks;
- identity is recomputed with the repository RFC 8785 JCS + SHA-256 helper;
- findings contain stable codes and JSON Pointer paths, never record values; and
- no network, lifecycle store, proof store, release store, public API, map, search, graph, export, or model runtime is read or written.

[Back to top](#top)

## Current implementation

| Surface | Status | Bounded meaning |
|---|---|---|
| [`validate_occurrence_evidence.py`](validate_occurrence_evidence.py) | **CONFIRMED executable** | Validates local JSON or replays the exact fixture manifest; emits deterministic JSON-line results. |
| [`OccurrenceEvidence` semantic contract](../../../../../contracts/domains/fauna/occurrence_evidence.md) | **PROPOSED draft contract** | Defines source-bound occurrence meaning and the pre-public/restricted boundary. |
| [Draft machine schema](../../../../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json) | **CONFIRMED closed schema / `DRAFT_SCHEMA`** | Draft 2020-12 shape with closed top-level and nested objects. |
| [Synthetic fixtures](../../../../../fixtures/domains/fauna/occurrence_evidence/) | **CONFIRMED fixture family** | Three valid cases and five exact-negative cases; no live biological or geographic evidence. |
| [Focused tests](../../../../../tests/domains/fauna/test_occurrence_evidence.py) | **CONFIRMED no-network tests** | Eight tests cover schema closure, identity, role anti-collapse, rights, exact fixture polarity, and value-safe output. |
| [Dedicated workflow](../../../../../.github/workflows/fauna-occurrence-evidence.yml) | **CONFIRMED CI orchestration** | Installs declared test dependencies, runs the focused suite and fixture replay, and validates the current generated receipt. |
| Live source adapters, binding policy, named stewards, proof closure, public/restricted conversion, release, and public consumers | **NEEDS VERIFICATION / held** | Not created or authorized by this lane. |

The implementation scope is `fauna-occurrence-evidence-draft-v1`. A future profile change should use an explicit successor scope rather than silently changing the meaning of recorded results.

[Back to top](#top)

## Responsibility split

| Responsibility | Owning surface |
|---|---|
| Source-bound occurrence meaning | `contracts/domains/fauna/occurrence_evidence.md` |
| Machine shape | `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json` |
| Executable validation and this lane README | `tools/validators/domains/fauna/occurrence/` |
| Canonical hashing implementation | `packages/hashing/` |
| Synthetic examples and exact expected findings | `fixtures/domains/fauna/occurrence_evidence/` |
| Enforceability | `tests/domains/fauna/test_occurrence_evidence.py` and `.github/workflows/fauna-occurrence-evidence.yml` |
| Source identity, source role, rights, and cadence | `data/registry/sources/fauna/` and accepted source contracts |
| Sensitivity, geoprivacy, admissibility, and obligations | `policy/domains/fauna/` and `policy/sensitivity/fauna/` |
| Evidence and proof | `EvidenceRef`/`EvidenceBundle` contracts and `data/proofs/` |
| Release, correction, withdrawal, and rollback | `release/` and their governing contracts |

Accepted ADR-0029 and Directory Rules v2 place executable validator code under `tools/`, semantic meaning under `contracts/`, machine shape under `schemas/`, examples under `fixtures/`, enforcement under `tests/`, and receipts under `data/receipts/`. This slice creates no parallel Fauna, schema, policy, source, proof, release, or publication authority.

[Back to top](#top)

## Input profile

The normal CLI accepts one or more paths to JSON files. Each candidate must be a JSON object conforming to the closed schema and declaring:

| Family | Required responsibility |
|---|---|
| Object and version | `object_type: occurrence_evidence` and `schema_version: v1`. |
| Deterministic identity | `spec_hash` and `occurrence_evidence_id`. |
| Source identity | `source_record_id`, `source_family`, and canonical `source_role`. |
| Taxon and observation | Taxon names/rank plus event date, basis of record, and method. |
| Geometry | Internal precision/geoprivacy and an explicit public-safe representation when required. |
| Rights and sensitivity | License/use posture plus exact-location, generalization, withholding, and review flags. |
| Provenance | Source URI, retrieval time, publisher, ingestion run, raw artifact, `SourceDescriptor`, and `EvidenceRef` links. |
| Validation declaration | Finite candidate result, canonical reason codes, seven readiness booleans, evidence strength, validator version, and validation time. |

`--fixtures` does not accept record paths. It replays every JSON case listed in `fixtures/domains/fauna/occurrence_evidence/expected_findings_manifest.json` and verifies exact code/path polarity and exact fixture inventory.

[Back to top](#top)

## Validation pipeline

Validation is fail-closed and ordered.

1. **Load bounded local JSON.** A non-object root or unreadable/invalid JSON produces a `schema.*` finding.
2. **Validate the closed schema.** Draft 2020-12 and format checks run first. Semantic checks do not run when machine shape fails. Schema output is capped at 100 findings, with an explicit truncation finding when exceeded.
3. **Recompute deterministic identity.** The identity subject contains the source record ID, event date, accepted scientific name, and normalized geometry. The validator compares both `spec_hash` and `occurrence_evidence_id` with the computed SHA-256 digest.
4. **Preserve source-role semantics.** The seven canonical roles remain distinct from source-native `basis_of_record`; modeled, aggregate, regulatory, administrative, candidate, and synthetic records cannot masquerade as direct observations.
5. **Check provenance, rights, and taxonomy.** Required raw-artifact support, resolved rights fields, and a normalized accepted scientific name are enforced.
6. **Check geometry and sensitivity consistency.** Non-open, generalized, or withheld records require a public-safe representation; withheld geometry contains no coordinates; exact public precision cannot conflict with generalization, withholding, or private geoprivacy; sensitive records require review posture.
7. **Reconcile declared readiness and finite state.** The seven declared booleans, reason-code array, review/evidence state, and `validator_result` must agree with computed checks. A declared `pass` fails when any bounded gate or reason remains.

### Source role and basis mapping

| `source_role` | Accepted basis posture |
|---|---|
| `observed` | Human or machine observation, specimen/sample, living/fossil specimen, or literature record. |
| `regulatory` | `regulatory_record`. |
| `modeled` | `model_output`. |
| `aggregate` | `aggregate_summary`. |
| `administrative` | `administrative_record`. |
| `candidate` | `candidate_report`. |
| `synthetic` | `synthetic_reconstruction`. |

A source family such as GBIF remains separate from source role. Aggregation or delivery through a source family does not silently upgrade the underlying evidence class.

[Back to top](#top)

## Outcomes and exit codes

Two finite-state layers must not be collapsed:

| Layer | Values | Meaning |
|---|---|---|
| CLI wrapper `outcome` | `PASS`, `ERROR` | Whether this validator found any schema or semantic inconsistency for the supplied file or fixture manifest. |
| Candidate `validation.validator_result` | `pass`, `quarantine`, `deny`, `error` | The internally declared state of the draft record. It must agree with reason codes, review posture, and computed readiness. |

A sensitive record may be schema-valid and internally consistent with `validator_result: quarantine`; the CLI then returns `PASS`. This proves only that a held record is represented consistently, not that it is public or release-ready.

| Exit code | Meaning |
|---:|---|
| `0` | Every supplied file, or the fixture manifest, produced no findings. |
| `1` | At least one supplied file or fixture expectation produced findings. |
| `2` | Command-line usage failed, such as providing neither paths nor `--fixtures`. |

When multiple file paths are supplied, the CLI prints one JSON object per input and returns `1` if any input fails.

[Back to top](#top)

## Finding contract

Each finding contains only:

```json
{
  "code": "<stable-family.code>",
  "path": "<JSON Pointer>"
}
```

Stable families are:

| Family | Scope |
|---|---|
| `schema.*` | JSON/machine shape, declared-check consistency, canonical arrays, finite-state discipline, and fixture replay. |
| `identity.*` | Hash computation, `spec_hash`, and `occurrence_evidence_id` binding. |
| `prov.*` | Raw-artifact and source-bound provenance support. |
| `rights.*` | License and use-rights resolution. |
| `geom.*` | Internal/public-safe geometry, precision, generalization, and withholding consistency. |
| `sens.*` | Sensitive-species, exact-location, review, and hold posture. |
| `taxon.*` | Accepted-name normalization. |
| `obs.*` | Source-role and basis-of-record semantics. |

The JSON-line envelope is deterministic and value-safe:

```json
{"findings": [], "input": "path/to/record.json", "outcome": "PASS", "scope": "fauna-occurrence-evidence-draft-v1"}
```

An error result reports codes and paths without echoing taxon names, identifiers, coordinates, URIs, publishers, methods, or other record values.

[Back to top](#top)

## Commands

Install the repository's declared test dependencies in an isolated environment when they are not already available:

```bash
python -m pip install -e ".[test]"
```

Run exact fixture replay:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py \
  --fixtures
```

Run the focused no-network suite:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_occurrence_evidence.py' \
  --verbose
```

Validate one or more local candidates:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py \
  path/to/first.json \
  path/to/second.json
```

The CLI has no live-source, URL, stdin, write, release, or publication mode.

[Back to top](#top)

## Fixtures and tests

The fixture manifest is the canonical test-polarity inventory for this profile.

| Lane | Cases | What is proven |
|---|---:|---|
| `valid/` | 3 | Open observed, modeled-context, and sensitive-withheld quarantine records can be represented consistently. |
| `semantic_invalid/` | 5 | Model-as-observation collapse, missing raw support, unresolved-rights pass, unsafe exact sensitive geometry, and identity drift fail deterministically. |
| `expected_findings_manifest.json` | 8 entries | Every fixture path is declared once and exact findings match code plus JSON Pointer path. |

Focused tests additionally prove that the schema and nested objects remain closed, identity is key-order independent, undeclared fields are rejected, unresolved rights cannot claim success, network calls are denied in the test boundary, and CLI diagnostics do not print protected values.

These fixtures are synthetic. They are not occurrence evidence, source rights, taxonomic authority, sensitivity decisions, public-safe transforms, or release artifacts.

[Back to top](#top)

## Security and privacy posture

- The validator has no network client or live-source mode; focused tests patch socket connection entry points to fail on attempted network access.
- Findings expose stable codes and JSON Pointer paths only. A focused test checks that protected taxon and coordinate-bearing values are absent from CLI output.
- Withheld public geometry must have `coordinates: null`; generalization-required public geometry cannot remain exact.
- Source geoprivacy and KFM public-safe precision remain separate fields.
- The validator never rewrites input, rounds coordinates, infers geometry, normalizes taxonomy, performs redaction, or approves exposure.
- Machine-shape findings are bounded; unexpected evaluation or hashing failures become explicit `schema.*` or `identity.*` errors rather than permissive fallback.

[Back to top](#top)

## CI and generated receipt

`.github/workflows/fauna-occurrence-evidence.yml` is the dedicated path-scoped workflow. It:

1. checks out the tested revision without persisted credentials;
2. installs `.[test]` under Python 3.11;
3. runs the focused unit suite and exact fixture replay with no-network environment flags;
4. validates `data/receipts/generated/genrec-fauna-occurrence-evidence-readme-20260808.json` against final repository bytes; and
5. records the authority boundary in the job summary.

The earlier `genrec-fauna-occurrence-evidence-20260808.json` remains immutable historical process memory for the implementation merged by PR #2209. The current receipt records this documentation/index synchronization and workflow pointer change; it does not rewrite the earlier record.

A green workflow proves only the declared schema/semantic profile, synthetic fixture polarity, and current receipt integrity at the tested commit. It does not authenticate source rights or reviewers, create proof, evaluate binding policy, approve release, deploy, or publish.

[Back to top](#top)

## Trust boundary

The validator reads only the supplied JSON object, the draft schema, the repository hashing helper, and synthetic fixtures. It does not:

- fetch or activate eBird, iNaturalist, GBIF, BISON, EDDMapS, or another live source;
- decide source admission, source terms, taxonomic authority, or steward ownership;
- resolve an `EvidenceRef` to an `EvidenceBundle` or close proof;
- decide which taxon, site, or join is sensitive;
- perform or approve redaction, buffering, gridding, aggregation, withholding, or another geoprivacy transform;
- create `OccurrencePublic`, `OccurrenceRestricted`, `RedactionReceipt`, `PolicyDecision`, `ReviewRecord`, `PromotionReceipt`, or `ReleaseManifest` objects;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, proof, receipt, or release records during validation;
- expose exact location values in findings; or
- provide hunting, wildlife-management, legal, emergency, or operational guidance.

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validators, fixtures, tests, commits, workflows, receipts, and pull requests are not promotion.

[Back to top](#top)

## Maintenance checklist

When the draft profile changes:

- [ ] Reconcile semantic contract, schema, validator, fixtures, tests, and this README in one dependency-closed slice.
- [ ] Preserve the source-role/basis distinction and exact/public-safe geometry split.
- [ ] Version any breaking field, identity-subject, scope, finding-code, or outcome change; do not silently reinterpret old results.
- [ ] Recompute fixture `spec_hash` and `occurrence_evidence_id` values with the repository hashing helper.
- [ ] Keep `expected_findings_manifest.json` sorted, unique, exact, and complete; no orphan fixture files.
- [ ] Add both positive and fail-closed negative coverage for new behavior.
- [ ] Preserve no-network execution and value-safe findings.
- [ ] Keep source admission, policy, steward review, proof, public/restricted conversion, and release in their owning lanes.
- [ ] Emit a new generated receipt for changed authoring bytes; do not rewrite historical process memory.
- [ ] Synchronize the parent Fauna validator index when child-lane maturity or commands change.

[Back to top](#top)

## Remaining verification backlog

- Current live-source descriptors, endpoints, terms, rights, cadence, and field mappings.
- Accepted taxonomy authority, taxon crosswalks, duplicate/misidentification handling, and correction lineage.
- Binding policy and named stewardship/review authority for sensitive taxa and sites.
- Canonical `OccurrenceEvidence` to `OccurrenceRestricted` / `OccurrencePublic` conversion and transform receipts.
- `EvidenceRef` to `EvidenceBundle` resolution, proof closure, and promotion/release integration.
- Production report destination, retention, aggregate validator registration, and required-check significance.
- Governed API, MapLibre/Evidence Drawer, search, graph, export, Focus Mode, and AI consumers.
- Correction, withdrawal, cache invalidation, and rollback propagation after public reliance.

These remain `NEEDS VERIFICATION` or `UNKNOWN`; the validator must not guess them.

[Back to top](#top)

## Correction and rollback

If the contract, schema, identity subject, source-role vocabulary, rights posture, sensitivity rules, fixture manifest, or release status changes, invalidate affected validation claims and rerun the exact profile. Public correction and withdrawal remain responsibilities of their governing lanes.

Before merge, rollback means closing the draft pull request and abandoning the feature branch. After an authorized merge, revert the documentation/index/workflow-pointer commit or make a transparent forward-fix PR. Preserve both generated receipts as historical process memory; do not rewrite shared history.

No live source, lifecycle record, proof, policy decision, API route, UI component, release, deployment, cache, or public artifact is changed by this documentation slice.

## Changelog

- **v0.2.0 — 2026-08-08:** reconciles the lane documentation with the merged closed schema, deterministic executable, exact fixture manifest, focused tests, CI behavior, output/exit-code contract, security posture, maintenance checklist, and immutable-receipt lineage.
- **v0.1.0 — 2026-08-08:** initial concise validator-lane README merged with the fixture-first `OccurrenceEvidence` implementation.
