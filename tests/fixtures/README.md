<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-readme
title: tests/fixtures/ — Test-local Fixture Index
type: README
version: v0.2
status: draft; repository-grounded; bounded-local-support; placement-conflicted; mixed-payload-maturity; non-authoritative
owners: OWNER_TBD — Test steward · Fixture steward · QA steward · Policy steward · Release steward
created: 2026-07-07
updated: 2026-08-31
policy_label: public-doc; tests; fixtures; local-support; synthetic-only; placement-review; non-authoritative; non-publisher
owning_root: tests/
responsibility: navigation, bounded consumer guidance, and placement disclosure for existing test-local support inputs without creating reusable fixture authority
truth_posture: CONFIRMED 11 direct child directories, 82 tracked files, 33 README files, 23 JSON payloads, 26 placeholder .gitkeep files, and two payload-bearing lanes at the pinned snapshot / CONFLICTED placement because the tests root prohibits test_fixture artifacts while current tests guidance treats this tree as bounded local support pending review / UNKNOWN complete consumer coverage, required-check status, migration disposition, and accountable stewardship
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_prior_blob: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
direct_child_directory_count: 11
tracked_file_count: 82
readme_count: 33
json_payload_count: 23
placeholder_gitkeep_count: 26
payload_bearing_lane_count: 2
related:
  - ../README.md
  - ../../fixtures/README.md
  - ../../docs/doctrine/directory-rules.md
  - governance/repository_control/README.md
  - maplibre/README.md
notes:
  - "Counts describe tracked files at the pinned Git tree, not collected cases, semantic coverage, hosted execution, or required-check state."
  - "Only governance/repository_control and maplibre/source-metadata contain JSON payloads at the pinned snapshot; other lanes are README and placeholder scaffolding."
  - "This index does not resolve the placement conflict or authorize a migration, deletion, new fixture root, release, deployment, promotion, or publication."
[/KFM_META_BLOCK_V2] -->

# Test-local fixture index

This authored index helps maintainers inspect the existing support material under
`tests/fixtures/`, find the two payload-bearing lanes, and run their verified
consumer tests. It is not generated test output and is not a fixture contract.

The authoritative reusable-fixture root is [`fixtures/`](../../fixtures/README.md).
The current [`tests/` guidance](../README.md) treats this tree as a bounded
local-support exception while its long-term placement remains unresolved.

## Placement and authority

The repository evidence is intentionally explicit about a conflict:

- [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml)
  reserves reusable synthetic valid, invalid, and golden inputs for `fixtures/`
  and prohibits the `test_fixture` artifact type under `tests/`.
- [`tests/README.md`](../README.md) records `tests/fixtures/` as an existing
  bounded local-support lane whose conformance and migration disposition still
  need verification.
- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md)
  governs responsibility-root placement; this README does not amend it.

Until that conflict is resolved, do not treat this tree as a second reusable
fixture authority. A file here may support a test, but it does not establish
source truth, schema or contract meaning, evidence sufficiency, policy approval,
review completion, release eligibility, deployment, promotion, or publication.

## Current tracked inventory

The pinned tree contains 82 tracked files: this parent README plus the 81 files
summarized below. Counts include nested descendants of each direct child.

| Direct child | Tracked files | READMEs | JSON | `.gitkeep` | Current posture |
|---|---:|---:|---:|---:|---|
| [`domains/`](domains/README.md) | 28 | 15 | 0 | 13 | Documentation and placeholder scaffolding only. |
| [`flora/`](flora/README.md) | 5 | 3 | 0 | 2 | Documentation and placeholder scaffolding only. |
| [`focus/`](focus/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`governance/`](governance/repository_control/README.md) | 12 | 1 | 11 | 0 | Payload-bearing repository-control lane. |
| [`hydrology/`](hydrology/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`layers/`](layers/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`maplibre/`](maplibre/README.md) | 22 | 6 | 12 | 4 | Payload-bearing source-metadata lane plus scaffolding. |
| [`people-dna-land/`](people-dna-land/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`settlements/`](settlements/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| [`ui/`](ui/README.md) | 2 | 1 | 0 | 1 | Documentation and placeholder scaffolding only. |
| **Child total** | **81** | **32** | **23** | **26** | Parent README excluded. |

The absence of payloads in a lane is not proof that its proposed behavior is
implemented or tested elsewhere. Consult its child README and consumer code
before making a coverage claim.

## Payload-bearing lanes

### Repository-control contexts

[`governance/repository_control/`](governance/repository_control/README.md)
contains 11 synthetic JSON contexts. The primary consumer is
[`tests/validators/test_repository_control.py`](../validators/test_repository_control.py),
which resolves this directory and evaluates its `context_*.json` files. Five
incident modules bind named terminal-divergence contexts:

- [`test_repository_control_incident_1789.py`](../validators/test_repository_control_incident_1789.py)
- [`test_repository_control_incident_1790.py`](../validators/test_repository_control_incident_1790.py)
- [`test_repository_control_incident_1791.py`](../validators/test_repository_control_incident_1791.py)
- [`test_repository_control_incident_1792.py`](../validators/test_repository_control_incident_1792.py)
- [`test_repository_control_incident_1829.py`](../validators/test_repository_control_incident_1829.py)

These fixtures exercise a repository-control evaluator; they do not grant
repository authority, change settings, authorize merge, or prove current
repository state. A direct hosted workflow command for this six-module group was
not established at the pinned snapshot.

### MapLibre source metadata

[`maplibre/source-metadata/`](maplibre/source-metadata/README.md) contains 12
synthetic JSON payloads across valid, invalid, and edge cases. The focused
[`test_source_metadata.py`](../maplibre/test_source_metadata.py) module has nine
tests for fixture polarity, finite outcomes, malformed and duplicate-key JSON,
determinism, redaction, CLI behavior, and attempted network access.

The [`maplibre-source-metadata` workflow](../../.github/workflows/maplibre-source-metadata.yml)
runs that module, executes the validator's fixture mode, and parses all JSON
payloads. The
[`MapLibre Perf Governance` workflow](../../.github/workflows/maplibre-perf-governance.yml)
separately verifies that the source-metadata fixture, test, validator, and
workflow boundary remains classified; it does not run the focused module.

Both workflows filter on descendants of `tests/fixtures/maplibre/`, so changing
this parent README alone does not trigger either focused workflow.

## Running the verified consumers

There are no executable test modules under `tests/fixtures/` itself. Do not use
`pytest tests/fixtures` as a fixture-lane validation claim; run the consumer
modules instead.

Repository-control consumers:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  PYTHONUNBUFFERED=1 TZ=UTC \
  python -m pytest -q \
  tests/validators/test_repository_control.py \
  tests/validators/test_repository_control_incident_1789.py \
  tests/validators/test_repository_control_incident_1790.py \
  tests/validators/test_repository_control_incident_1791.py \
  tests/validators/test_repository_control_incident_1792.py \
  tests/validators/test_repository_control_incident_1829.py
```

MapLibre source-metadata consumers, matching the focused workflow:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  PYTHONUNBUFFERED=1 TZ=UTC \
  python -m unittest discover \
  --start-directory tests/maplibre \
  --pattern 'test_source_metadata.py' \
  --verbose

python tools/validators/maplibre/validate_source_metadata.py --fixtures
```

For a syntax-only JSON check across this tree:

```bash
python - <<'PY'
import json
from pathlib import Path

paths = sorted(Path("tests/fixtures").rglob("*.json"))
for path in paths:
    json.loads(path.read_text(encoding="utf-8"))
print(f"parsed {len(paths)} JSON fixture payloads")
PY
```

That last command checks JSON parsing only. It does not validate schemas,
consumer semantics, fixture polarity, rights, sensitivity, policy, or release
fitness.

## Failure interpretation

| Failure | Interpret first as | Do not infer |
|---|---|---|
| JSON parsing fails | A tracked payload is not valid JSON. | Which contract or schema should govern it. |
| Repository-control test fails | Fixture assumptions, evaluator behavior, or the tracked control-state projection diverged. | Permission to alter settings, merge, or bypass review. |
| Source-metadata test fails | Projection outcome, reason code, redaction, determinism, CLI, or no-network behavior diverged. | Source authority, rights clearance, or remote-byte validation. |
| Consumer cannot find a path | Fixture layout and consumer binding disagree. | That moving the fixture is authorized. |
| Documentation-only lane remains empty | No payload has been admitted to that local lane. | Missing coverage, implementation maturity, or approval to invent fixtures. |

When a failure exposes a placement or semantic dispute, hold the narrow change
and resolve it with the owning contract, schema, policy, or responsibility root.
Do not change runtime behavior merely to make this index pass.

## Safety and maintenance

- Keep payloads synthetic, compact, deterministic, reviewable, and no-network.
- Do not store source exports, lifecycle data, production logs, secrets, real
  sensitive detail, released artifacts, or public outputs in this tree.
- Preserve deny, abstain, correction, rollback, redaction, and harmful-precision
  cases when a consumer depends on them.
- Update counts and consumer links in the same reviewable change when tracked
  fixture paths change.
- Add a payload only with an identified consumer and expected outcome. A child
  README or `.gitkeep` is not executable coverage.
- Do not duplicate material from [`fixtures/`](../../fixtures/README.md). Resolve
  reuse or migration through the accepted directory rules.
- Treat a passing test as bounded evidence about the checked behavior, not as
  review, release, deployment, promotion, or publication.

## Known gaps

- The long-term disposition of `tests/fixtures/` is unresolved against the
  registered fixture root and the `tests/` artifact prohibition.
- Accountable stewardship and review ownership remain `OWNER_TBD`.
- Complete consumer coverage outside the two verified payload-bearing lanes is
  unknown.
- Direct hosted collection for the repository-control fixture consumers was not
  established.
- Required-check status, production parity, correction propagation, and
  operational rollback remain unverified.

Removing or reverting this README changes navigation only. It does not move or
delete fixtures, modify a consumer, change policy, roll back runtime state, or
withdraw a released artifact.
