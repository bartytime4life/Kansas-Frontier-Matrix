<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/support-type-profile
title: Soil Support-Type Anti-Collapse Profile
type: semantic-contract; domain-profile; validation-profile
version: v0.1.2
status: proposed; inactive; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Soil steward · Contract steward · Source steward · Validation steward
created: 2026-08-05
updated: 2026-09-11
policy_label: public; soil; support-type; anti-collapse; non-publisher
related:
  - ./README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../packages/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/support_type_profile.schema.json
  - ../../../schemas/contracts/v1/domains/soil/support_type_candidate.schema.json
  - ../../../pipeline_specs/soil/support_type_profile.v1.json
  - ../../../tools/validators/domains/soil/support_type/validate_support_type_profile.py
tags: [kfm, soil, support-type, source-role, anti-collapse, fixture-first]
[/KFM_META_BLOCK_V2] -->

# Soil support-type anti-collapse profile

> This inactive, fixture-first profile proves that Soil support classes remain
> distinct across source family, source role, spatial support, and claim kind.
> It does not admit a source, resolve evidence, evaluate policy, authorize
> promotion, release a layer, or publish Soil truth.

## Goal

The Soil lane is a governed family rather than one all-purpose truth layer. The
profile records eight bounded support classes:

| Support type | Intended support | Primary anti-collapse rule |
|---|---|---|
| `authoritative_static_soil` | SSURGO/SDA map-unit survey support | Not a live station, satellite-grid, or management claim. |
| `gridded_derivative_soil` | gSSURGO/gNATSGO-style derived grids | Not source-of-record polygon or station truth. |
| `station_soil_moisture` | Kansas Mesonet-style point observations | Not countywide, satellite-grid, static-survey, or advisory truth. |
| `reference_station_soil_climate` | SCAN/USCRN reference observations | Not local Mesonet identity or countywide advice. |
| `satellite_soil_moisture_grid` | SMAP-style gridded context | Not a station reading, field verification, or survey map unit. |
| `profile_soil_evidence` | Pedon/profile/horizon evidence | Not map-unit or countywide truth without separate support. |
| `soil_interpretation` | Source or KFM-derived interpretations | Not legal, hazard, management, or engineering authority. |
| `governed_change_evidence` | Materiality/diff process memory | Not release authorization or publication state. |

The names are bound to this proposed profile version. They do not amend a
global vocabulary or activate live sources.

## Candidate boundary

`SoilSupportTypeCandidate` is a synthetic test object. It binds:

- profile identity, version, and digest;
- candidate content digest;
- one declared support type;
- source family and source role;
- spatial-support class and claim kind;
- source and evidence references;
- explicit `not_evaluated` policy and `not_released` release state;
- governance fields that are all false.

A schema-valid candidate can still fail the profile mapping. That distinction is
intentional: schema checks shape, while the validator checks profile coherence.

## Deterministic identity

`support_type_profile.v1.json` uses `kfm-canonical-json-v1`: remove the
top-level `spec_hash`, serialize sorted-key UTF-8 JSON without insignificant
whitespace, preserve array order, compute SHA-256, and prefix `sha256:`.

The validator also requires profile rule arrays and candidate reference arrays
to be sorted and unique so replay does not depend on incidental ordering.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, digest, profile binding, and support mapping are coherent. |
| `DENY` | The candidate collapses support types, requests public use, or violates the inactive governance boundary. |
| `ERROR` | The input, profile, or schema cannot be read or evaluated safely. |

`PASS` is a bounded test result. It is not `ANSWER`, policy approval, evidence
closure, release readiness, or publication permission.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2. Placement follows one owning
responsibility per artifact:

- semantic meaning → `contracts/domains/soil/`;
- machine shape → `schemas/contracts/v1/domains/soil/`;
- inactive executable profile → `pipeline_specs/soil/`;
- validation logic → `tools/validators/domains/soil/support_type/`;
- synthetic cases → `fixtures/domains/soil/support_type/`;
- enforceability proof → `tests/validators/domains/soil/support_type/`;
- CI orchestration → `.github/workflows/`;
- AI authoring accountability → `data/receipts/generated/`.

No new root or parallel source, policy, evidence, proof, release, or published
home is created.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/soil/support_type \
  --pattern 'test_support_type_profile.py' \
  --verbose

python tools/validators/domains/soil/support_type/validate_support_type_profile.py \
  --fixtures
```

Both commands are deterministic and perform no network access.

### Fixture execution contract

Select exactly one CLI mode: `--candidate PATH` or `--fixtures`. Supplying both
or neither is a usage error (exit `2`) before validation runs. `--profile PATH`
applies to either mode; fixture mode must not silently fall back to the default
profile. The Python fixture entrypoint retains its existing positional root and
adds the optional keyword-only `profile_path`.

A fixture run reads and validates the selected profile before evaluating any
candidate. A missing, malformed, schema-invalid, or hash-incoherent profile
produces `PROFILE_INVALID` plus its available diagnostic findings, with an
`ERROR` outcome. All fixtures use that one parsed profile. This is not an atomic
snapshot of every fixture and schema file.

Both `valid/` and `invalid/` must contain JSON fixtures. A positive fixture must
produce `PASS`; a negative fixture must be read and evaluated successfully enough
to produce `DENY`. Malformed JSON, duplicate keys, invalid UTF-8, non-finite
numbers, oversized/non-object inputs, disappearing files, or schema evaluation
errors produce `FIXTURE_EVALUATION_ERROR`, never a passing negative control.
Negative parser tests therefore belong in the focused test suite, not as broken
JSON silently accepted by the persisted `invalid/` fixture runner.

Wrong polarity retains `VALID_FIXTURE_REJECTED` or `INVALID_FIXTURE_ACCEPTED`.
Findings remain sorted, unique code/field pairs. Evaluated runs retain JSON output
and exit `0` for `PASS`, `1` for `DENY` or `ERROR`; no runtime or release authority
is added. The default profile's version, digest, eight support classes, and all
persisted positive and negative candidates remain unchanged.

The existing [profile workflow](../../../.github/workflows/soil-support-type-profile.yml)
already invokes the [focused test file](../../../tests/validators/domains/soil/support_type/test_support_type_profile.py)
and default fixture runner; no new workflow or live-source step is needed.
Workflow configuration is not evidence of hosted execution. Its historical
receipt check remains separate from this change's authoring receipt.

### Bounded JSON and schema evaluation

The file entrypoints capture at most `MAX_JSON_BYTES + 1` bytes from one open
stream and reject payloads larger than 1 MiB before UTF-8 decoding or JSON
parsing. `FILE_TOO_LARGE` is an `ERROR`, not an evaluated candidate `DENY`.
Interpreter recursion or integer-conversion limits become
`JSON_COMPLEXITY_LIMIT`; exception messages and input values are not echoed.
This bounds a read, not filesystem snapshot consistency, CPU time, or every
possible resource-exhaustion condition. Files must remain ordinary local inputs;
concurrent replacement, special-file handling, and full parser isolation are
not proved by this profile.

Schemas use the same bounded, duplicate-free, finite-number JSON reader as
profiles and candidates. A malformed/schema-invalid schema, recursion failure,
or unresolved reference produces `SCHEMA_UNAVAILABLE`. Validation uses an
explicit non-retrieving `referencing.Registry`, following the already declared
`jsonschema` dependency's referencing API. In-document `$defs`/fragment references
continue to resolve. No HTTP, file-URI, or other external reference is fetched;
cross-document schema composition would require a separately reviewed local
resource map rather than enabling implicit retrieval. No schema bytes or
package versions are changed by this repair.

The implementation choices are supported by the official
[Python JSON input cautions](https://docs.python.org/3.13/library/json.html) and
[jsonschema referencing API](https://python-jsonschema.readthedocs.io/en/stable/referencing/),
checked 2026-09-11. These are library references, not source-admission or KFM
release authority. The added regression controls exercise bounded reads,
strict schema parsing, finite exceptions, and denied reference retrieval while
retaining the existing fixture-execution and support-separation tests.

### Source and implementation boundary

This repair follows the distinction between validator failure and invariant
rejection in the *KFM Soil Architecture Extended Pro* report, page 16, and its
fixture-first tests on page 19
([Drive source](https://drive.google.com/file/d/1c19HxzdgZRPBaimFIg06KckEHBrhj33R/view)).
That report is planning lineage, not authority for its proposed paths or proof
that live Soil data is admitted. The current contract and implementation own
this bounded `PASS` / `DENY` / `ERROR` profile; this change does not import the
report's broader pipeline, quarantine, map, source, or release proposals.

## Rollback

For this fixture-execution repair, retain the branch and its exact validation
record while review or the PR-delivery path is held. Before integration, the
branch may be abandoned without changing main. After an authorized integration,
revert the paired validator, tests, and contract change together, retaining the
authoring receipt as historical lineage. Reverting restores the older false-pass
behavior, so prefer a bounded forward correction when possible. This repair
does not change schemas, the profile, persisted fixtures, workflows, sources,
release state, or public artifacts.
