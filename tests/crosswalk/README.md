<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION__tests_crosswalk_readme
title: tests/crosswalk
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION__likely_@bartytime4life_from_tests_parent
created: NEEDS_VERIFICATION__file_history
updated: 2026-04-26
policy_label: NEEDS_VERIFICATION
related: [
  ../README.md,
  ../../README.md,
  ./test_crosswalk_fixture.py,
  ../../pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/README.md,
  ../../data/receipts/,
  ../../schemas/,
  ../../contracts/,
  ../../policy/,
  ../../tools/,
  ../../.github/workflows/
]
tags: [kfm, tests, crosswalk, hydrology, huc12, admin-boundary, postgis, pytest, run_receipt, spec_hash]
notes: [
  Target path was supplied directly as tests/crosswalk/README.md.
  Public-main inspection showed this leaf contains README.md and test_crosswalk_fixture.py at drafting time.
  The sibling test file is a PostGIS/pytest fixture for the HUC12 admin crosswalk watcher and requires a local DSN.
  Owner, created date, policy label, CI enforcement, branch protection, and active-checkout parity remain NEEDS VERIFICATION.
  Local workspace inspection in this ChatGPT session did not expose a mounted KFM Git checkout.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/crosswalk`

PostGIS-backed integration fixture for proving the HUC12 ↔ administrative-boundary crosswalk watcher emits bounded, no-publish, receipt-aware results.

> [!IMPORTANT]
> **Status:** `experimental`  
> **Owners:** `NEEDS VERIFICATION` — parent `tests/` material surfaces `@bartytime4life`, but active-branch `CODEOWNERS` must be checked.  
> **Path:** `tests/crosswalk/README.md`  
> **Repo fit:** child verification leaf under [`../README.md`](../README.md), coupled to the hydrology watcher at [`../../pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/`](../../pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/) and downstream receipt surfaces under [`../../data/receipts/`](../../data/receipts/).  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![doc](https://img.shields.io/badge/doc-draft-lightgrey) ![owners](https://img.shields.io/badge/owners-NEEDS%20VERIFICATION-yellow) ![path](https://img.shields.io/badge/path-tests%2Fcrosswalk-0a7ea4) ![suite](https://img.shields.io/badge/suite-PostGIS%20fixture-blue) ![network](https://img.shields.io/badge/network-no--network%20fixtures-2ea043) ![publish](https://img.shields.io/badge/publish-no--publish-b60205) ![truth](https://img.shields.io/badge/truth-bounded-6f42c1)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current evidence snapshot](#current-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Operating tables](#operating-tables) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!CAUTION]
> The crosswalk fixture truncates and repopulates `kfm_crosswalk.*` tables in the configured database. Run it only against a disposable local PostGIS test database.

---

## Scope

`tests/crosswalk/` is the narrow verification leaf for the HUC12 ↔ administrative-boundary crosswalk watcher. Its job is to prove that a small, synthetic, no-network fixture can move through the watcher path without turning a crosswalk into public truth, release proof, or canonical hydrology.

The leaf should verify four things first:

1. the fixture can create deterministic crosswalk pairs from controlled HUC12 and administrative geometries;
2. the watcher emits a `run_receipt` as process memory;
3. `--no-publish` remains honored;
4. computed measures, CRS, hashes, assignment methods, and weights remain bounded and inspectable.

This is not a generic geography test suite. It is a governed integration fixture for a specific crosswalk burden.

[Back to top](#top)

---

## Repo fit

| Surface | Relationship to `tests/crosswalk/` | Status |
|---|---|---:|
| [`../README.md`](../README.md) | Parent governed verification surface for KFM tests. | **CONFIRMED upstream path in public repo** |
| [`./test_crosswalk_fixture.py`](./test_crosswalk_fixture.py) | Executable sibling fixture for this leaf. | **CONFIRMED sibling in public repo** |
| [`../../pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/`](../../pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/) | Watcher lane under test; expected to normalize inputs, run area overlap, and emit receipt output. | **PARTLY CONFIRMED / NEEDS VERIFICATION for runner and schema files** |
| [`../../data/receipts/`](../../data/receipts/) | Expected home for emitted `run_receipt` process memory. | **NEEDS VERIFICATION for exact subpath policy** |
| [`../../schemas/`](../../schemas/) and [`../../contracts/`](../../contracts/) | Machine-contract authority surfaces for objects such as receipts, source descriptors, and crosswalk records. | **NEEDS VERIFICATION for schema-home authority** |
| [`../../policy/`](../../policy/) | Publication, rights, sensitivity, and release decision rules. | **NEEDS VERIFICATION for active gate coverage** |
| [`../../tools/`](../../tools/) | Validators, diff helpers, and support tooling that should remain outside this test leaf. | **NEEDS VERIFICATION for exact entrypoints** |
| [`../../.github/workflows/`](../../.github/workflows/) | CI orchestration and review handoff. | **UNKNOWN enforcement until workflow and branch settings are verified** |

### Upstream

This leaf consumes watcher code, schema SQL, a disposable PostGIS DSN, tiny synthetic geometry fixtures, and KFM’s broader truth-path expectations.

### Downstream

This leaf supports review of crosswalk watcher behavior, receipt emission, deterministic hash discipline, and promotion-readiness checks. It does **not** publish, release, sign, tile, or approve anything.

[Back to top](#top)

---

## Accepted inputs

Material belongs in `tests/crosswalk/` when it is tiny, deterministic, fixture-scoped, and directly tied to the HUC12/admin crosswalk proof burden.

| Accepted input | Required handling |
|---|---|
| Disposable PostGIS DSN | Use `KFM_CROSSWALK_TEST_DSN` or `DATABASE_URL`; never point to production, shared staging, or a canonical data store. |
| Synthetic HUC12 geometry | Small fixture geometry only; preserve CRS and area-basis expectations. |
| Synthetic administrative geometry | Small fixture geometry only; do not imply legal, regulatory, land-title, or hydrologic truth. |
| Watcher schema SQL | Apply only to the disposable test database. |
| Watcher runner path | Verify existence in the active checkout before claiming the test is executable. |
| Expected receipt JSON | Assert object type, run ID, publication state, CRS, record count, and anomaly count. |
| Hash and metric assertions | Check `geometry_hash`, `spec_hash`, overlap ranges, assignment method, and normalized weight behavior. |
| Negative or edge fixtures | Add only when they stay no-network, public-safe, and reviewable. |

[Back to top](#top)

---

## Exclusions

These do **not** belong in this leaf.

| Excluded material | Send it instead to | Reason |
|---|---|---|
| RAW, WORK, QUARANTINE, or unpublished candidate data | `../../data/` lifecycle lanes | Tests must not create a public or review shortcut around lifecycle state. |
| Production database DSNs or shared staging databases | Local secret manager / disposable test setup | The fixture truncates crosswalk tables. |
| Credentials, tokens, cookies, API keys, or private endpoints | Local environment or repository secrets | Test files must be safe to inspect. |
| Live WBD, Census, TIGER, or other source pulls | Source watcher / ingest lanes with source descriptors | This leaf should remain no-network by default. |
| Full provider mirrors or large geospatial datasets | RAW/WORK source lifecycle | Fixtures prove behavior; they are not shadow data stores. |
| Release proofs, proof packs, or publication manifests | `../../data/proofs/`, `../../data/catalog/`, or `../../release/` | This leaf can assert closure but does not own proof custody. |
| Policy definitions | `../../policy/` | Tests verify policy-facing behavior; they do not define policy. |
| Canonical schemas | `../../schemas/` or `../../contracts/` after schema-home ADR | Tests contain examples and assertions only. |
| Direct model prompts or AI-generated summaries | Governed AI/runtime lanes | Crosswalk claims require evidence resolution, not generated fluency. |
| Map layers or public tiles | Published/released delivery surfaces | Crosswalk fixture output is not public release authority. |

[Back to top](#top)

---

## Current evidence snapshot

> [!WARNING]
> This snapshot is useful for orientation, not a substitute for active checkout inspection. Re-run the inventory before merging or using this README as implementation proof.

| Claim | Label | Basis |
|---|---:|---|
| `tests/crosswalk/` exists on public `main` and contains `README.md` plus `test_crosswalk_fixture.py`. | **CONFIRMED** | Public repository tree inspection. |
| The current public `tests/crosswalk/README.md` had no substantive body before this revision. | **CONFIRMED** | Raw README fetch returned zero lines. |
| `test_crosswalk_fixture.py` is an integration-style pytest fixture requiring `KFM_CROSSWALK_TEST_DSN` or `DATABASE_URL`. | **CONFIRMED** | Sibling test file content. |
| The test references `pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py` and `sql/001_schema.sql`. | **CONFIRMED as test references / NEEDS VERIFICATION for active file presence** | Sibling test file content plus active branch check needed. |
| The fixture inserts one HUC12 polygon and two county polygons in EPSG:5070. | **CONFIRMED** | Sibling test fixture setup. |
| The first test expects a receipt, `published: false`, `crs: EPSG:5070`, `record_count: 2`, and `anomaly_count: 0`. | **CONFIRMED** | Sibling test assertions. |
| The second test checks metric ranges, `geometry_hash`, `spec_hash`, one primary assignment, and total weight `1.0`. | **CONFIRMED** | Sibling test assertions. |
| CI runs this fixture by default. | **UNKNOWN** | Requires workflow and branch-protection inspection. |
| This fixture proves live source correctness. | **DENY** | It proves bounded fixture behavior only. |

[Back to top](#top)

---

## Directory tree

Current public tree for this leaf is intentionally small.

```text
tests/crosswalk/
├── README.md                    # this guide
└── test_crosswalk_fixture.py    # PostGIS-backed integration fixture
```

Referenced surfaces to verify in the active checkout:

```text
pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/
├── runner.py                    # referenced by test; NEEDS VERIFICATION
└── sql/
    └── 001_schema.sql           # referenced by test; NEEDS VERIFICATION

data/receipts/crosswalk/         # receipt output target; NEEDS VERIFICATION
```

> [!TIP]
> Keep this leaf small. If crosswalk testing grows beyond the current watcher fixture, create explicit child fixtures or sibling lanes rather than mixing source-intake, schema authority, policy definition, release proof, and integration behavior in one file.

[Back to top](#top)

---

## Quickstart

Start with non-destructive discovery.

```bash
# Confirm repository and branch state.
git status --short
git branch --show-current

# Inventory this leaf and the watcher path it references.
find tests/crosswalk -maxdepth 2 -type f | sort
find pipelines/watchers/hydrology_huc12_admin_crosswalk_watch -maxdepth 3 -type f | sort

# Confirm the test imports and collects.
python3 -m pytest --collect-only -q tests/crosswalk/test_crosswalk_fixture.py
```

Run the fixture only against a disposable PostGIS database.

```bash
# Example only. Use a throwaway local test database.
export KFM_CROSSWALK_TEST_DSN="postgresql://postgres:postgres@localhost:5432/kfm_crosswalk_fixture"

# Optional in a disposable database only.
psql "$KFM_CROSSWALK_TEST_DSN" \
  -v ON_ERROR_STOP=1 \
  -c 'CREATE EXTENSION IF NOT EXISTS postgis;'

# Run the crosswalk fixture.
python3 -m pytest -q tests/crosswalk/test_crosswalk_fixture.py
```

> [!CAUTION]
> Do not run this against a database containing real source records, reviewer artifacts, staged release candidates, or canonical state. The fixture setup truncates `kfm_crosswalk.crosswalk_pairs`, `kfm_crosswalk.huc12_processed`, `kfm_crosswalk.admin_processed`, and `kfm_crosswalk.source_snapshot`.

[Back to top](#top)

---

## Usage

Use this test leaf to prove watcher behavior at the smallest meaningful boundary.

### What the fixture is expected to do

```text
schema SQL -> synthetic source snapshots -> synthetic HUC12/admin geometries
          -> watcher runner --no-publish
          -> run_receipt JSON
          -> crosswalk_pairs rows
          -> bounded metric/hash assertions
```

### What a strong crosswalk test proves

| Proof burden | Example assertion |
|---|---|
| Receipt emission | `receipt["object_type"] == "run_receipt"` |
| Run identity | `receipt["run_id"] == run_id` |
| No public publish | `receipt["publication"]["published"] is False` |
| CRS discipline | `receipt["crs"] == "EPSG:5070"` and row CRS is `EPSG:5070` |
| Deterministic record count | `record_count == 2` for the synthetic split fixture |
| Anomaly discipline | `anomaly_count == 0` for the happy-path fixture |
| Bounded metrics | overlap and weight values remain between expected bounds |
| Hash shape | `geometry_hash` and `spec_hash` match `sha256:<64 lowercase hex>` |
| Assignment method | expected primary overlap assignment is present exactly once |
| Normalized weighting | sum of weights for the fixture run equals `1.0` |

### Pseudocode for future negative cases

```python
# pseudocode: adapt to repo-native fixtures before implementation
def test_unknown_rights_crosswalk_fixture_does_not_publish():
    result = run_crosswalk_fixture("unknown_rights.invalid.json", no_publish=True)

    assert result.outcome in {"ABSTAIN", "DENY"}
    assert result.publication.published is False
    assert "rights" in result.reason_codes
    assert result.evidence_bundle_ref is None or result.evidence_bundle_ref.startswith("kfm://")
```

[Back to top](#top)

---

## Diagram

```mermaid
flowchart LR
    A[pytest fixture] --> B[Apply watcher schema SQL]
    B --> C[TRUNCATE disposable kfm_crosswalk tables]
    C --> D[Insert synthetic source snapshots]
    D --> E[Insert one HUC12 polygon]
    D --> F[Insert two admin polygons]
    E --> G[Run watcher --no-publish]
    F --> G
    G --> H[Emit data/receipts/crosswalk/<run_id>.json]
    G --> I[Write crosswalk_pairs rows]
    H --> J[Assert run_receipt fields]
    I --> K[Assert CRS, metrics, hashes, assignment, weights]
    J --> L{Fixture outcome}
    K --> L
    L -->|PASS| M[Review confidence for watcher behavior]
    L -->|FAIL / SKIP| N[Fix runner, schema, fixture, DB setup, or docs]

    M -. not release authority .-> O[Promotion gate / proof / catalog / release]
    G -. must not publish .-> P[PUBLISHED artifacts]
    G -. must not read .-> Q[RAW / WORK / QUARANTINE public path]
```

The key boundary is simple: the test may prove fixture behavior and receipt emission, but it must not become a release path.

[Back to top](#top)

---

## Operating tables

### Environment and command contract

| Item | Expected value | Notes |
|---|---|---|
| `KFM_CROSSWALK_TEST_DSN` | PostgreSQL/PostGIS DSN | Preferred explicit test DSN. |
| `DATABASE_URL` | PostgreSQL/PostGIS DSN | Fallback used by the test if the explicit DSN is absent. |
| `psql` | available on `PATH` | Test skips if missing. |
| `python3` | available on `PATH` | Test skips if missing. |
| `runner.py` | watcher runner referenced by test | Test skips if missing. |
| `001_schema.sql` | watcher schema SQL referenced by test | Must be verified in active checkout. |
| `--no-publish` | required runner argument | Protects publication boundary. |

### Test family map

| Test | Primary burden | Positive signal | Failure meaning |
|---|---|---|---|
| `test_crosswalk_fixture_builds_pairs_and_receipt` | receipt and row creation | receipt exists, no publish, two rows | runner/schema/DB/receipt behavior regressed |
| `test_crosswalk_fixture_metrics_and_hashes_are_valid` | metric and identity discipline | valid ranges, hashes, assignment method, total weight | geometry, hash, CRS, or assignment rules drifted |

### Boundary matrix

| Boundary | Test should prove | Must not imply |
|---|---|---|
| Source identity | fixture snapshots are explicit and traceable | source registry is complete |
| Geometry | synthetic areas and CRS behave as expected | real WBD/admin geometries are correct |
| Receipt | process memory is emitted and parseable | receipt is a proof pack |
| Publication | `--no-publish` is honored | candidate is release-approved |
| Policy | future negative cases can fail closed | tests replace policy decisions |
| Evidence | downstream claims need `EvidenceBundle` closure | crosswalk rows are public truth |

[Back to top](#top)

---

## Task list / definition of done

A change touching `tests/crosswalk/` is not done until the relevant boxes are true.

- [ ] The active checkout inventory confirms the files this README names.
- [ ] The test uses a disposable PostGIS database and never a canonical, staging, or production database.
- [ ] The test remains no-network by default.
- [ ] The fixture geometries are synthetic, tiny, public-safe, and reviewable.
- [ ] The runner is invoked with `--no-publish`.
- [ ] Receipt output is asserted as process memory, not release proof.
- [ ] `record_count`, `anomaly_count`, CRS, metric bounds, assignment method, `geometry_hash`, `spec_hash`, and weight behavior are asserted.
- [ ] Missing DSN, missing `psql`, missing `python3`, or missing runner produces a clear skip rather than a misleading pass.
- [ ] Any new fixture includes a negative or edge case when it protects a consequential boundary.
- [ ] No test fixture stores secrets, source mirrors, sensitive exact locations, or unchecked provider data.
- [ ] CI usage is documented only after workflow and branch-protection behavior are verified.
- [ ] Documentation changes with behavior when the crosswalk proof burden changes.
- [ ] Rollback is simple: remove the test or fixture without migrating canonical data.

[Back to top](#top)

---

## FAQ

### Why does this leaf require PostGIS?

The crosswalk burden is spatial: it depends on geometry, CRS, intersections, areas, and hashable outputs. A pure unit test can verify helper functions, but this leaf verifies the database-backed fixture path.

### Does this test publish anything?

No. The runner is invoked with `--no-publish`, and the receipt assertion requires `publication.published` to be `False`.

### Can this run in default CI?

Only after CI has a safe disposable PostGIS service and the workflow is verified. Until then, treat it as integration-only and manually invoked.

### Is a HUC12/admin crosswalk authoritative?

No. It is a derived overlap relationship between hydrologic-unit geometry and administrative-boundary geometry. It must not be treated as legal jurisdiction, hydrologic observation, regulatory flood evidence, land-title truth, or a public release by itself.

### What should happen if the watcher runner is missing?

The current fixture should skip clearly. A missing runner is not a pass; it is an implementation gap that belongs in the verification backlog.

### Can live WBD or Census inputs be added here?

Not by default. Live source activation belongs in source-aware watcher or ingest lanes with source descriptors, rights checks, update cadence, and review. This leaf should keep no-network fixtures as the default proof shape.

[Back to top](#top)

---

## Appendix

<details>
<summary>Truth labels used in this README</summary>

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from surfaced public repository evidence, direct current-session command output, or sibling file content. |
| **INFERRED** | Strongly supported by adjacent KFM evidence but not directly proven for this exact path. |
| **PROPOSED** | Recommended behavior, fixture, or next step not yet verified as active implementation. |
| **UNKNOWN** | Not verified strongly enough to claim. |
| **NEEDS VERIFICATION** | Requires active checkout, CI, branch protection, owner, source rights, runtime, or emitted artifact verification before stronger claims. |
| **DENY** | Explicitly not allowed under KFM trust posture. |

</details>

<details>
<summary>Reviewer checklist for future expansion</summary>

Before adding more crosswalk tests, reviewers should ask:

- Does the new test preserve the distinction between hydrologic units, administrative boundaries, source snapshots, derived relationships, receipts, proofs, and publication?
- Does the fixture remain tiny, deterministic, and no-network?
- Does it avoid RAW/WORK/QUARANTINE data and exact sensitive geometry?
- Does it assert a meaningful failure mode rather than only a happy path?
- Does it keep watcher behavior separate from promotion approval?
- Does it update this README when the proof burden changes?
- Does it avoid claiming live-source correctness from fixture-only evidence?

</details>

<details>
<summary>Suggested next fixture backlog</summary>

| Priority | Candidate fixture | Why |
|---:|---|---|
| P0 | invalid or missing DSN skip behavior | keeps local setup failures honest |
| P0 | unknown rights / no-publish negative case | proves publication remains blocked |
| P1 | ambiguous overlap fixture | protects assignment-method logic |
| P1 | zero-overlap or sliver-overlap fixture | protects area and anomaly logic |
| P1 | unstable hash regression fixture | protects deterministic identity |
| P2 | promotion handoff dry-run fixture | proves receipt/diff handoff without release |
| P2 | correction/rollback reference fixture | preserves reversibility after downstream use |

</details>

[Back to top](#top)
