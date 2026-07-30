<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-water-planning-readme
title: tools/validators/domains/water_planning README
type: README
version: v0.1
status: confirmed-implementation; registry-records-not-released
owner: @bartytime4life (CODEOWNERS review routing only); local steward NEEDS VERIFICATION
created: 2026-07-30
updated: 2026-07-30
policy_label: repository-facing; water-planning; deterministic; no-network; fail-closed; non-authoritative
owning_root: tools/
responsibility: documents the bounded water-planning validator lane, its three current entrypoints, inputs, outputs, deterministic outcomes, tests, fixtures, workflow integration, authority limits, recovery, and maintenance expectations
truth_posture: cite-or-abstain; implementation claims are grounded in current repository code and tests; validator success is not source admission, proof, policy approval, release, deployment, publication, or public truth
related:
  - validate_status_collapse.py
  - validate_geometry_authority.py
  - validate_rac_registry.py
  - ../../README.md
  - ../README.md
  - ../../../../contracts/domains/water_planning/README.md
  - ../../../../schemas/contracts/v1/domains/water_planning/README.md
  - ../../../../fixtures/domains/water_planning/
  - ../../../../tests/domains/water_planning/
  - ../../../../.github/workflows/briefing-integration.yml
  - ../../../../docs/doctrine/directory-rules.md
notes:
  - "This v0.1 replaces the one-newline placeholder introduced by merged pull request #1845."
  - "The three Python validators are current implementation surfaces; the semantic contracts remain proposed/draft and the checked-in RAC registry records remain not-released."
  - "The RAC registry validator verifies pinned repository bytes and metadata. It does not refresh sources, recompute spatial intersections, clear rights, or authorize release."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Water-planning validators

[![briefing-integration](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml/badge.svg?branch=main)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/briefing-integration.yml)
[![Status: confirmed implementation](https://img.shields.io/badge/status-confirmed_implementation-1f883d)](#validator-index)
[![Posture: deterministic and no-network](https://img.shields.io/badge/posture-deterministic_%7C_no--network-0969da)](#determinism-and-outcomes)
[![Release: not authorized](https://img.shields.io/badge/release-not_authorized-b42318)](#authority-boundary)

> **Purpose.** `tools/validators/domains/water_planning/` contains three deterministic, fail-closed command-line validators for synthetic water-planning semantic fixtures, synthetic geometry-authority fixtures, and the checked-in Kansas Water Office Regional Advisory Committee registry slice.

> [!IMPORTANT]
> A green result means only that the configured checks passed for the declared input and scope. It is not source admission, evidence or proof closure, a rights decision, governance approval, release, deployment, publication, or public truth.

## Quick navigation

- [Scope and placement](#scope-and-placement)
- [Authority boundary](#authority-boundary)
- [Directory map](#directory-map)
- [Validator index](#validator-index)
- [Quick start](#quick-start)
- [Inputs and outputs](#inputs-and-outputs)
- [Rules enforced](#rules-enforced)
- [Determinism and outcomes](#determinism-and-outcomes)
- [Fixtures and tests](#fixtures-and-tests)
- [CI integration](#ci-integration)
- [Limitations and recovery](#limitations-and-recovery)
- [Maintenance](#maintenance)
- [Related authority](#related-authority)

## Scope and placement

| Field | Current posture |
|---|---|
| Purpose | Validate bounded water-planning candidates without defining water-planning meaning or publishing data. |
| Nearest parent index | [`tools/validators/domains/`](../README.md) |
| Validator-root index | [`tools/validators/`](../../README.md) |
| Owning responsibility root | `tools/` |
| Scope identifier | `water_planning` |
| Exposure | Public repository tooling and documentation; fixtures are synthetic or public-safe. |
| Inputs | UTF-8 JSON fixture files, or the explicitly listed checked-in RAC registry/data records. |
| Outputs | Finite stdout findings or a success line plus a process exit code; the validators do not write repository artifacts. |
| Mutation and retention | Validators read inputs only. Code, fixtures, records, and tests are versioned in Git. |
| Review routing | [`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) routes `tools/validators/` review to `@bartytime4life`; that route is not proof of independent review or approval. |
| Local steward | **NEEDS VERIFICATION.** No separate water-planning validator steward is established by this directory. |
| Implementation evidence | **CONFIRMED** against the three scripts, their tests, their fixtures/data, and the read-only workflow linked below. |
| Review snapshot | Code and tests inspected on 2026-07-30 at [`main@96d7085`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/96d7085af6a0b2682ef04361311c5b6f29810f22). |

This path is a `PLACE` outcome under the accepted [Directory Rules](../../../../docs/doctrine/directory-rules.md): executable repository validators belong under `tools/`, a domain is a scope lane within that responsibility root, and this README uses the compact boundary profile. The relevant rules include `DIR-EXEC-006`, `DIR-SCOPELANE-001`, `DIR-SCOPELANE-003`, and `DIR-README-001` through `DIR-README-004`.

[Back to top](#top)

## Authority boundary

| This lane may | This lane must not |
|---|---|
| Check declared semantic anti-collapse rules. | Define canonical water-planning semantics; those belong in `contracts/` and domain doctrine. |
| Check bounded authority references, identity inventory, lineage, digests, and correction posture. | Admit a source, create a source registry record, or claim current source freshness. |
| Check pinned repository geometry and crosswalk bytes against expected metadata. | Fetch a source, construct geometry, recompute spatial intersections, or silently replace a pinned baseline. |
| Return finite findings and fail closed on malformed, missing, oversized, or unsupported input. | Treat a validator pass as evidence, proof, a policy decision, governance review, or rights clearance. |
| Protect synthetic fixtures from authority collapse and value echoing. | Store secrets, restricted records, exact sensitive locations, or real applicant/recipient/project data here. |
| Participate in read-only pull-request validation. | Release, deploy, publish, or authorize any public API, map, export, search, Focus Mode, or AI surface. |

Current truth labels:

- **CONFIRMED:** three Python validator entrypoints, matching regression tests, synthetic fixture families, checked-in RAC registry/data inputs, and read-only CI integration exist.
- **PROPOSED / draft:** the linked semantic contracts and schemas describe evolving domain surfaces; their presence does not grant release authority.
- **NEEDS VERIFICATION:** independent stewardship, source freshness, rights clearance, governance membership, broader evidence closure, and public-release eligibility.
- **DENY:** interpreting any validator result as proof of funding, payment, construction, completion, operational benefit, source admission, or publication authorization.

[Back to top](#top)

## Directory map

The current direct children are:

```text
water_planning/
├── README.md
├── validate_geometry_authority.py
├── validate_rac_registry.py
└── validate_status_collapse.py
```

Fixtures, tests, contracts, schemas, registry records, and processed data remain in their own responsibility roots.

[Back to top](#top)

## Validator index

| Validator | Declared scope | Primary input | Success outcome | Failure outcome |
|---|---|---|---|---|
| [`validate_status_collapse.py`](./validate_status_collapse.py) | Synthetic water-planning semantic anti-collapse fixtures only | One or more JSON paths, each at most 1,000,000 bytes | One compact JSON object per file with `"outcome":"PASS"` | One compact JSON object per file with sorted findings and `"outcome":"FAIL"` |
| [`validate_geometry_authority.py`](./validate_geometry_authority.py) | Synthetic region identity, geometry-authority, county-crosswalk-authority, and project-reference envelopes | One or more JSON paths, each at most 1,000,000 bytes | `{"files":N,"outcome":"VALIDATOR_PASS"}` | One JSON object with sorted `code`, `file_index`, and `path` findings and `"outcome":"VALIDATOR_FAIL"` |
| [`validate_rac_registry.py`](./validate_rac_registry.py) | The pinned, checked-in RAC geometry/county-crosswalk registry slice and its source descriptors | Five default repository paths or explicit CLI overrides | `RAC_REGISTRY_OK regions=14 counties=105 mappings=209` | Sorted tab-separated `CODE<TAB>PATH` findings |

All three tools are read-only and use the Python standard library. Normal validation returns exit `0` on success and exit `1` when findings exist. Invalid command syntax is handled by `argparse` and may return exit `2`; it is not a validation pass or fail.

[Back to top](#top)

## Quick start

Run commands from the repository root.

### Validate the synthetic status-collapse envelope

```bash
python tools/validators/domains/water_planning/validate_status_collapse.py \
  fixtures/domains/water_planning/status_collapse/valid/valid_1.json
```

Expected stdout:

```json
{"file":"fixtures/domains/water_planning/status_collapse/valid/valid_1.json","findings":[],"outcome":"PASS","scope":"synthetic-water-planning-status-collapse-only"}
```

### Validate the synthetic geometry-authority envelope

```bash
python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json
```

Expected stdout:

```json
{"files":1,"outcome":"VALIDATOR_PASS"}
```

### Validate the checked-in RAC registry slice

```bash
python tools/validators/domains/water_planning/validate_rac_registry.py
```

Expected stdout:

```text
RAC_REGISTRY_OK regions=14 counties=105 mappings=209
```

### Run the complete domain regression suite

```bash
python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_*.py' \
  --verbose
```

[Back to top](#top)

## Inputs and outputs

### Status-collapse validator

The positional `files` argument accepts one or more JSON paths. Paths are processed in sorted order. Each output object contains:

| Field | Meaning |
|---|---|
| `file` | The supplied path, normalized with POSIX separators. |
| `findings` | A deterministically sorted list of `{code, path}` objects; values from the input are not echoed. |
| `outcome` | `PASS` when no finding exists; otherwise `FAIL`. |
| `scope` | Always `synthetic-water-planning-status-collapse-only`. |

An unreadable, malformed, or missing input becomes `FIXTURE_JSON_INVALID`; an oversized input becomes `FIXTURE_TOO_LARGE`.

### Geometry-authority validator

The positional `paths` argument accepts one or more JSON paths. Paths and findings are sorted before serialization. The success document reports the number of files. A failure document reports only finite codes, the sorted input's `file_index`, and JSON paths.

Input handling remains finite:

| Condition | Finding |
|---|---|
| Path does not exist | `INPUT_NOT_FOUND` |
| File cannot be read as UTF-8 | `INPUT_READ_ERROR` |
| JSON is malformed | `INVALID_JSON` |
| File exceeds 1,000,000 bytes | `INPUT_TOO_LARGE` |

### RAC registry validator

With no options, the validator resolves these repository-relative inputs:

| Option | Default path |
|---|---|
| `--dataset-record` | [`data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json`](../../../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json) |
| `--crosswalk-record` | [`data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json`](../../../../data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json) |
| `--geometry` | [`data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson`](../../../../data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson) |
| `--kwo-source` | [`data/registry/sources/water_planning/kwo_rac_feature_service.source.json`](../../../../data/registry/sources/water_planning/kwo_rac_feature_service.source.json) |
| `--census-source` | [`data/registry/sources/water_planning/census_tigerweb_counties_2025.source.json`](../../../../data/registry/sources/water_planning/census_tigerweb_counties_2025.source.json) |

Use `--repo-root` to resolve relative overrides against a different checkout root. Absolute paths are also accepted. Overrides change the files inspected; they do not change the pinned expectations encoded by this validator.

[Back to top](#top)

## Rules enforced

### Semantic status anti-collapse

[`validate_status_collapse.py`](./validate_status_collapse.py) checks that:

- a meeting is not an approval;
- an application is not a recommendation or award;
- a recommendation is not an award;
- an award is not payment;
- payment is not construction;
- construction is not completion;
- a scoring matrix or program version is not a project outcome;
- applicant identity, recipient identity, project geometry, and regional geometry are not guessed;
- requested, recommended, awarded, agreed, paid, and expended amounts remain distinct facts;
- required lineage references and blocked-behavior flags have the declared shapes;
- the candidate is fixture-only, declares no network access, and contains no undeclared top-level fields.

### Synthetic geometry and authority references

[`validate_geometry_authority.py`](./validate_geometry_authority.py) checks that:

- the inventory contains exactly `kwo-rac-01` through `kwo-rac-14`, in order, with the pinned public KWO RAC names;
- the KFM-assigned numeric suffix is not represented as a KWO-native identifier;
- authority version, digest, correction, and lineage metadata are coherent;
- geometry and county-crosswalk authorities are reference-only in synthetic fixtures;
- RAC identity remains separate from groundwater-management-district identity;
- project regional membership remains separate from project location geometry;
- unresolved, approximate, and confirmed states agree with nullable authority references;
- inline coordinates, geometry, addresses, and real project/recipient behavior are denied;
- blocked behaviors cannot claim source admission, geometry construction, registry creation, release, or publication.

### Checked-in RAC registry

[`validate_rac_registry.py`](./validate_rac_registry.py) checks that:

- the processed geometry bytes match the pinned digest and byte count;
- the geometry has exactly 14 expected RAC features and stable identities;
- all 105 Kansas county GEOIDs are represented across the ordered 209 positive-area intersection mappings;
- mapping order, digest, uniqueness, and overlap-class counts remain pinned;
- county overlap classes do not overstate boundary slivers as material membership;
- dataset, crosswalk, geometry, and source-descriptor references agree;
- source descriptors remain disabled, review-gated, and not publicly released;
- registry release posture remains `not-released`;
- version, source, lineage, correction, and baseline metadata remain coherent.

[Back to top](#top)

## Determinism and outcomes

| Property | Enforcement |
|---|---|
| Stable ordering | Input paths and findings are sorted before output where multiple results are possible. |
| Finite findings | Findings expose declared codes and JSON paths, not arbitrary exception text. |
| No value echo | Tests assert that protected input values do not appear in findings or CLI output. |
| No network | Regression tests deny socket, DNS/connection, and URL access. The CI workflow also sets `KFM_NO_NETWORK=1`. |
| Read-only behavior | Validators read supplied or checked-in files and write only to stdout. |
| Fail closed | Missing, unreadable, malformed, oversized, mismatched, authority-collapsed, or release-overclaiming inputs produce findings and a nonzero result. |
| Bounded pass | Exit `0` describes only the declared validator scope; it creates no proof, receipt, decision, release record, or publication state. |

Do not parse human prose from stderr as an authority signal. Automation should use the documented exit code and the finite stdout format for the selected validator.

[Back to top](#top)

## Fixtures and tests

| Surface | Evidence |
|---|---|
| Status-collapse fixtures | [`fixtures/domains/water_planning/status_collapse/`](../../../../fixtures/domains/water_planning/status_collapse/) |
| Status-collapse tests | [`tests/domains/water_planning/test_status_collapse.py`](../../../../tests/domains/water_planning/test_status_collapse.py) |
| Geometry-authority fixtures | [`fixtures/domains/water_planning/geometry_authority/`](../../../../fixtures/domains/water_planning/geometry_authority/) |
| Geometry fixture notes | [`fixtures/domains/water_planning/geometry_authority/README.md`](../../../../fixtures/domains/water_planning/geometry_authority/README.md) |
| Geometry-authority tests | [`tests/domains/water_planning/test_geometry_authority.py`](../../../../tests/domains/water_planning/test_geometry_authority.py) |
| RAC registry regression tests | [`tests/domains/water_planning/test_rac_registry.py`](../../../../tests/domains/water_planning/test_rac_registry.py) |
| Schema contract tests | [`tests/schemas/test_water_planning_contracts.py`](../../../../tests/schemas/test_water_planning_contracts.py) |

The tests cover non-vacuous valid inputs, stable invalid findings, malformed/missing input, authority and identity drift, digest and mapping drift, release overclaim, no-network behavior, and non-echoing output. Fixtures must remain synthetic, minimized, and public-safe unless a separately governed path and review authorize otherwise.

[Back to top](#top)

## CI integration

The read-only [`briefing-integration`](../../../../.github/workflows/briefing-integration.yml) workflow is triggered by changes under this directory. Its `preserve-water-planning-anti-collapse` job:

1. checks out the tested revision without persisted credentials;
2. runs every `tests/domains/water_planning/test_*.py` module;
3. runs `validate_rac_registry.py` against the checked-in defaults; and
4. records a bounded job summary stating that green CI is not source freshness, rights clearance, evidence closure, release, deployment, or publication.

The workflow declares only `contents: read`. It does not write repository content or grant KFM release authority.

[Back to top](#top)

## Limitations and recovery

### Known limitations

- The status-collapse and geometry-authority validators accept synthetic fixture envelopes only. They do not validate live applications, recipients, projects, meetings, awards, payments, construction, or completion records.
- The geometry-authority validator checks references and bounded authority metadata. It does not contain or construct production geometry.
- The RAC registry validator checks pinned checked-in bytes and metadata. It does not refetch KWO or Census sources, prove freshness, independently recompute polygon intersections, or resolve rights.
- Passing validators do not prove that a source is correct, complete, current, admissible, licensed for a use, independently reviewed, or releasable.
- The linked contracts and schemas remain proposed/draft surfaces; validator coverage does not promote their governance status.
- Public API, UI, MapLibre, PMTiles, export, graph, search, Focus Mode, and AI behavior is outside this lane.

### Recovery

1. Read the finite finding code and JSON path; do not bypass or reinterpret a nonzero result as a warning.
2. Correct the fixture or the owning contract/schema/registry/data record in its responsibility root.
3. When changing pinned registry bytes, update the version, digest, byte count, lineage, correction metadata, and regression expectations together.
4. Add or update the smallest matching valid and invalid regression case.
5. Rerun the focused validator, then the complete domain regression suite.
6. If the intended change would admit a source, alter authority, clear rights, release, or publish, stop and route it through the owning governance surface.

Rollback is a normal Git revert of the offending code/data/documentation commit. These validators create no generated repository state that requires cleanup.

[Back to top](#top)

## Maintenance

- Keep CLI examples, options, stdout formats, exit behavior, limits, and default paths synchronized with code in the same pull request.
- Preserve deterministic sorting, finite finding codes, non-echoing diagnostics, no-network behavior, and read-only execution.
- Add matching tests and synthetic/public-safe fixtures for every new rule or finding code.
- Keep contracts, schemas, policies, source records, processed data, proofs, receipts, and releases in their owning roots.
- Do not add an empty validator or directory for symmetry. A new child must have an evidenced responsibility, bounded interface, tests, and placement justification.
- Treat changes to the pinned RAC inventory, geometry digest, county set, mapping count/order, overlap classes, or source posture as governed baseline changes, not maintenance trivia.
- Reverify links and CI routing whenever files move.
- Update the metadata date and review snapshot when implementation behavior is re-inspected.

[Back to top](#top)

## Related authority

| Surface | Role |
|---|---|
| [`contracts/domains/water_planning/`](../../../../contracts/domains/water_planning/README.md) | Semantic meaning and anti-collapse boundaries |
| [`schemas/contracts/v1/domains/water_planning/`](../../../../schemas/contracts/v1/domains/water_planning/README.md) | Machine-readable shapes |
| [`docs/sources/catalog/kansas/kwo.md`](../../../../docs/sources/catalog/kansas/kwo.md) | Kansas Water Office source catalog entry |
| [`data/registry/`](../../../../data/registry/) | Registry records and source descriptors |
| [`data/processed/water_planning/rac_regions/`](../../../../data/processed/water_planning/rac_regions/) | Pinned processed RAC geometry bytes |
| [`fixtures/domains/water_planning/`](../../../../fixtures/domains/water_planning/) | Synthetic/public-safe validator inputs |
| [`tests/domains/water_planning/`](../../../../tests/domains/water_planning/) | Domain validator regression suite |
| [Directory Rules](../../../../docs/doctrine/directory-rules.md) | Repository placement authority |
| [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for the canonical Directory Rules |
| [`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) | GitHub review routing only |
| [`briefing-integration.yml`](../../../../.github/workflows/briefing-integration.yml) | Read-only pull-request and `main` validation |

[Back to top](#top)
