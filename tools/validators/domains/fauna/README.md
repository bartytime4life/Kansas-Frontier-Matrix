<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-fauna-readme
title: tools/validators/domains/fauna README
type: README
version: v0.3.0
status: draft; two bounded executable slices confirmed; production authority held
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-sensitive-species-reviewer-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-08-08
policy_label: repository-facing; per-domain-validator-index; fauna; sensitive-species; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: Index bounded Fauna validator implementations and proposed child lanes while preserving source, evidence, policy, sensitivity, proof, release, correction, rollback, and public-surface authority in their owning roots.
truth_posture: CONFIRMED current bounded executables; PROPOSED draft profiles; NEEDS VERIFICATION production source, policy, proof, release, and public use
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../biodiversity/README.md
  - ../../fauna/README.md
  - ../../fauna/source_role/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ./occurrence/README.md
  - ./occurrence/validate_occurrence_evidence.py
  - ./validate_public_safe_fixture.py
  - ../../../../docs/domains/fauna/README.md
  - ../../../../docs/domains/fauna/IDENTITY_MODEL.md
  - ../../../../docs/domains/fauna/FILE_SYSTEM_PLAN.md
  - ../../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../../docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/sensitivity/fauna/
  - ../../../../data/registry/sources/fauna/
  - ../../../../data/proofs/fauna/
  - ../../../../data/receipts/
  - ../../../../release/
  - ../../../../fixtures/domains/fauna/
  - ../../../../tests/domains/fauna/test_fauna_smoke.py
  - ../../../../tests/domains/fauna/test_occurrence_evidence.py
  - ../../../../.github/workflows/domain-fauna.yml
  - ../../../../.github/workflows/fauna-occurrence-evidence.yml
notes:
  - "The lane contains two separate bounded executables: synthetic public-safe fixture hygiene and the draft OccurrenceEvidence schema/semantic profile. Neither is production occurrence-public validation."
  - "OccurrenceEvidence validation was merged by PR #2209 with a closed draft schema, deterministic identity, exact fixtures, focused tests, and a dedicated workflow."
  - "Fauna sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, steward-controlled records, and reverse-engineerable derivatives remain deny-by-default until governing policy, review, evidence, transformation, release, correction, and rollback support exists."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-fauna--validators-informational)
![implementation](https://img.shields.io/badge/implementation-two--bounded--slices-orange)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![authority](https://img.shields.io/badge/authority-checkers--only-lightgrey)

> **One-line purpose.** `tools/validators/domains/fauna/` indexes bounded fail-closed Fauna validators without creating Fauna truth, taxonomic or stewardship authority, geoprivacy policy, proof closure, release approval, or public occurrence authority.

## Purpose

The durable question for this lane is:

> Does a declared Fauna candidate satisfy the exact configured schema, semantic, fixture-safety, source-role, rights, sensitivity, and public-surface constraints—or must the bounded checker fail closed while stronger authority remains held?

The lane owns executable checks and their local documentation only. Fauna meaning, machine shape, source admission, evidence, policy, review, proof, release, correction, rollback, and public delivery remain separate responsibilities.

[Back to top](#top)

## Current implementation

| Surface | Status | Exact scope |
|---|---|---|
| `validate_public_safe_fixture.py` | **CONFIRMED bounded executable** | Standard-library hygiene validator for closed synthetic, location-withheld, no-network, unreleased fixtures. It is not real occurrence validation. |
| `tools/validators/fauna/README.md` and `tools/validators/fauna/source_role/README.md` | **CONFIRMED routing documentation** | Broad Fauna and source-role routing surfaces; they do not replace this per-domain executable home. |
| [`occurrence/validate_occurrence_evidence.py`](occurrence/validate_occurrence_evidence.py) | **CONFIRMED bounded executable** | Draft closed `OccurrenceEvidence` schema and semantic validation, deterministic identity, role/basis anti-collapse, rights/provenance, sensitivity/geometry consistency, and exact fixture replay. |
| [`occurrence/README.md`](occurrence/README.md) | **CONFIRMED child-lane documentation** | Exact CLI, input/output, findings, tests, CI, receipt, trust boundary, maintenance, and rollback for the occurrence profile. |
| `tests/domains/fauna/test_fauna_smoke.py` | **CONFIRMED fixture-hygiene suite** | Seven deterministic tests for the older synthetic public-safe fixture profile. |
| `tests/domains/fauna/test_occurrence_evidence.py` | **CONFIRMED occurrence suite** | Eight deterministic no-network tests for the draft occurrence profile. |
| `.github/workflows/domain-fauna.yml` | **CONFIRMED bounded workflow** | Runs the older synthetic fixture-safety suite and keeps proof/release jobs held. |
| `.github/workflows/fauna-occurrence-evidence.yml` | **CONFIRMED dedicated workflow** | Runs occurrence tests, exact fixture replay, and current generated-receipt integrity. |
| Live sources, production policy, `EvidenceBundle` proof, public/restricted conversion, release, and public consumers | **NEEDS VERIFICATION / held** | Neither bounded executable creates this authority. |

Do not collapse the two executables. Fixture hygiene answers whether a synthetic test object is safe to keep in the repository. Occurrence validation answers whether a source-bound draft occurrence record is internally consistent with its declared profile. Neither answers whether a real occurrence may be released.

[Back to top](#top)

## Accepted bounded executable: synthetic fixture hygiene

`validate_public_safe_fixture.py` accepts only candidates that are explicitly synthetic, fixture-only, source-role `synthetic`, rights-scoped to fixture use, location-withheld, no-network, unreleased, and promotion-ineligible.

It fails closed on:

- undeclared top-level, spatial, or governance fields;
- exact or aliased location-bearing keys and finite numeric values beneath location-like keys;
- malformed or nested `public_caveats`, more than 16 caveats, or caveat strings longer than 512 characters;
- URL-like strings after whitespace and Unicode-format-marker normalization, including embedded HTTP(S), scheme-relative, and `www.` forms;
- control characters and coordinate-pair-shaped free text;
- cyclic, deeper-than-64-level, or more-than-4,096-node in-memory structures;
- fixture files larger than 1,000,000 bytes, integer tokens over 512 digits, or JSON values that cannot be parsed safely; and
- unsupported synthetic identifier shapes.

Structural cycle, depth, or node-limit findings stop further field inspection so malformed in-memory candidates cannot force unbounded secondary findings. Findings identify bounded paths and codes without printing protected values.

This checker reduces accidental leakage in fixtures. It does not determine whether a real taxon, occurrence, site, or derivative is public-safe.

[Back to top](#top)

## Accepted bounded executable: draft OccurrenceEvidence

[`occurrence/`](occurrence/README.md) owns the current draft occurrence profile. Its executable:

- validates the closed Draft 2020-12 schema;
- recomputes RFC 8785 JCS + SHA-256 identity and the `kfm://occurrence/<digest>` URI;
- keeps source family, canonical source role, and source-native basis of record separate;
- requires source-bound raw-artifact support where configured;
- fails closed on unresolved rights, taxon normalization, unsafe exact/public geometry, withholding/generalization conflicts, and pending sensitive review;
- reconciles seven declared readiness booleans, canonical reason codes, and finite candidate states; and
- replays three valid and five exact-negative synthetic fixtures.

Its CLI reports only stable code/path findings and returns wrapper `PASS` or `ERROR`. A consistently represented `quarantine` record may produce wrapper `PASS`; that is representation validity, not release readiness.

[Back to top](#top)

## Child-lane register

| Child | State | Boundary |
|---|---|---|
| [`occurrence/`](occurrence/README.md) | **CONFIRMED bounded executable lane** | Draft source-bound `OccurrenceEvidence`; no source admission, transformation, proof, release, or public occurrence authority. |
| `geoprivacy/` | **PROPOSED** | Redaction/generalization/buffering/gridding/aggregation checks after accepted policy and receipt contracts exist. |
| `sensitive-site/` | **PROPOSED** | Nests, dens, roosts, hibernacula, spawning, breeding, and aggregation-site posture. |
| `taxon-status/` | **PROPOSED** | Taxon identity, crosswalk, conservation, and legal-status posture. |
| `range-migration/` | **PROPOSED** | Range polygons, seasonal ranges, and migration claims. |
| `disease-mortality/` | **PROPOSED** | Mortality and disease observation boundaries. |

A future child requires externally owned meaning, machine shape, policy posture, synthetic fixtures, deterministic findings, tests, CI scope, receipt handling where required, and explicit non-authority language.

[Back to top](#top)

## What belongs here

Good fits include:

- this validator-lane index and child-lane documentation;
- deterministic validators that enforce declared, externally owned semantics;
- optional runners that delegate without redefining domain rules;
- stable value-safe finding codes and JSON Pointer paths;
- fixture references, exact command guidance, and test-surface documentation; and
- bounded implementation-status records that distinguish confirmed executables from proposed lanes.

## What does not belong here

| Do not put here | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Fauna domain doctrine and semantic contracts | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Machine schemas and enums | `schemas/contracts/v1/domains/fauna/` |
| Policy, sensitivity, and geoprivacy rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/` |
| Source descriptors and source mappings | `data/registry/sources/fauna/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | governed `data/` lifecycle roots |
| `EvidenceBundle`s, proofs, or process receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, corrections, withdrawals, rollback | `release/` |
| Reusable tests and fixtures | `tests/`, `fixtures/` |
| Public API, UI, map, tile, search, graph, export, Focus Mode, or AI runtime | governed released application/runtime roots |

[Back to top](#top)

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Fauna validator implementation and index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain ecology/biodiversity checks | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Fauna meaning and contracts | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` |
| Fauna policy and sensitivity rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/` |
| Source descriptors | `data/registry/sources/fauna/` |
| Evidence and proof support | `data/proofs/fauna/`, `data/proofs/` |
| Process receipts | `data/receipts/` |
| Release decisions, manifests, corrections, withdrawal, rollback | `release/` |
| Tests and fixtures | `tests/domains/fauna/`, `fixtures/domains/fauna/` |
| Public API, map, search, graph, export, Focus Mode, and AI | Governed released application/runtime surfaces |

A validator pass is never source admission, evidence closure, policy or review approval, release approval, or publication authority.

[Back to top](#top)

## Fauna fail-closed posture

Fauna validators must fail, hold, deny, abstain, quarantine, or route to authorized review when a candidate:

- lacks required source identity, source role, taxon, provenance, rights, evidence, sensitivity, or review support;
- collapses observed, modeled, aggregate, regulatory, administrative, candidate, or synthetic source roles;
- collapses source-bound evidence, restricted records, public derivatives, sensitive sites, ranges, migration routes, mortality, disease, or invasive-species records;
- exposes exact or reverse-engineerable sensitive location detail;
- lacks a required geoprivacy transform, receipt, policy decision, review record, release manifest, correction path, or rollback target;
- permits map, tile, search, graph, export, Focus Mode, or AI exposure beyond an approved public-safe derivative; or
- treats validator output as promotion, release, publication, legal guidance, hunting guidance, emergency instruction, or wildlife-management authority.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

## Stable bounded findings

The synthetic fixture-safety executable may emit stable findings including:

| Finding family | Meaning |
|---|---|
| `*_MISSING`, `*_INVALID`, `*_UNRESOLVED` | Required synthetic fixture state is absent or invalid. |
| `UNDECLARED_*_FIELD` | The closed fixture profile contains an undeclared field. |
| `PRECISE_LOCATION_FIELD_FORBIDDEN` | A location-bearing key or declared alias appears. |
| `LOCATION_NUMERIC_VALUE_FORBIDDEN` | A finite numeric value appears beneath a location-bearing key. |
| `LIVE_URL_FORBIDDEN` | A URL-like string appears in the fixture. |
| `COORDINATE_PATTERN_FORBIDDEN` | Free text resembles a coordinate pair. |
| `CONTROL_CHARACTER_FORBIDDEN` | A string contains a disallowed control character. |
| `PUBLIC_CAVEATS_INVALID`, `PUBLIC_CAVEAT_INVALID`, `PUBLIC_CAVEATS_TOO_MANY`, `PUBLIC_CAVEAT_TOO_LONG` | Caveat shape or bounds failed. |
| `DOCUMENT_CYCLE_FORBIDDEN`, `DOCUMENT_DEPTH_EXCEEDED`, `DOCUMENT_NODE_LIMIT_EXCEEDED` | An in-memory candidate exceeds bounded structure limits. |
| `FIXTURE_TOO_LARGE`, `FIXTURE_JSON_INVALID` | A fixture exceeds the byte cap or cannot be parsed safely. |
| `RELEASE_STATE_NOT_HELD`, `PROMOTION_STATE_NOT_HELD` | The fixture is not explicitly unreleased and promotion-ineligible. |

The occurrence child uses lowercase `schema.*`, `identity.*`, `prov.*`, `rights.*`, `geom.*`, `sens.*`, `taxon.*`, and `obs.*` families documented in [`occurrence/README.md`](occurrence/README.md). Both executables report paths/codes without protected values.

[Back to top](#top)

## Validation commands

Synthetic fixture-hygiene suite:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Draft occurrence suite and exact fixture replay:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_occurrence_evidence.py' \
  --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py \
  --fixtures
```

These commands are not source-admission checks, policy-engine evaluations, geoprivacy transforms, evidence/proof closure, release gates, promotion paths, or publication paths.

[Back to top](#top)

## Review checklist

- [ ] Keep the two bounded executable scopes distinct.
- [ ] Back every executable claim with current code, fixtures, tests, workflow, or emitted artifact evidence.
- [ ] Preserve source-role anti-collapse and exact/public-safe geometry separation.
- [ ] Keep sensitive taxa and exact or reverse-engineerable location detail fail-closed.
- [ ] Report codes and paths without protected values.
- [ ] Keep evidence, policy, review, release, correction, withdrawal, and rollback states explicit.
- [ ] Give map, tile, search, graph, export, Focus Mode, and AI surfaces no new authority.
- [ ] Write reports and receipts only to accepted responsibility roots.
- [ ] Use public-safe synthetic fixtures and no-network tests.
- [ ] Update this index when a child lane is added, retired, or changes maturity.

[Back to top](#top)

## Remaining verification backlog

- Live source descriptors, terms, rights, cadence, and source-family mappings.
- Accepted taxonomy authority, crosswalks, duplicate/misidentification handling, and correction lineage.
- Binding sensitivity and geoprivacy policy plus named steward/reviewer authority.
- Canonical restricted/public occurrence contracts, transformations, and receipts.
- `EvidenceRef` to `EvidenceBundle` resolution and Fauna proof closure.
- Release candidate, independent review, correction, withdrawal, rollback, and cache invalidation.
- Aggregate validator registration, required-check significance, report destinations, and retention.
- Governed API, MapLibre/Evidence Drawer, search, graph, export, Focus Mode, and AI consumers.

These remain `NEEDS VERIFICATION` or `UNKNOWN`; this index does not guess them.

[Back to top](#top)

## Correction and rollback

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert this documentation/index synchronization and the dedicated workflow receipt pointer, or make a transparent forward-fix PR. Do not rewrite historical generated receipts or shared history.

No live source, lifecycle record, proof, policy decision, API route, UI component, release, deployment, cache, or public artifact is changed by this documentation slice.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-08 |
| Evidence snapshot | `main@3f4e3ff133c6ea78ba1ca9f784b26b97a56b344f` |
| Review state | Current repository bytes reconciled; human review remains pending on the draft documentation pull request. |
| Current bounded scope | Synthetic fixture hygiene plus draft `OccurrenceEvidence` conformance; production source, policy, proof, release, and public use remain held. |

## Changelog

- **v0.3.0 — 2026-08-08:** indexes the merged draft `OccurrenceEvidence` validator alongside the older synthetic fixture-safety executable; preserves exact fixture-hygiene guardrails and finding families; adds current commands, workflows, child-lane maturity, authority boundaries, maintenance, and rollback.
- **v0.2.1 — 2026-07-25:** hardened the synthetic public-safe fixture validator and documented its bounded scope.
- **v0.2.0 — 2026-07-24:** recorded the accepted fixture-safety executable and held production authority.
- **v0.1.0 — 2026-07-07:** initial Fauna validator index.
