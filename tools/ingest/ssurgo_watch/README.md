<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-ssurgo-watch-readme
title: SSURGO package drift fixture comparator
type: README
version: v0.1
status: bounded executable fixture profile
owners:
  - OWNER_TBD - tooling QA (responsible owner; identity NEEDS VERIFICATION)
required_review_roles:
  - Soil steward
  - NRCS source steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; fixture-only; no-network; review-signal-only; no-publication
owning_root: tools/
responsibility: Deterministically compare two frozen synthetic SSURGO package sidecars and emit a review-only drift report.
related:
  - ../README.md
  - ../../../tests/ingest/ssurgo_watch/README.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/doctrine/directory-rules.md
  - ../cdl_watch/README.md
notes:
  - "This helper neither fetches SSURGO nor acts as a connector, source registry, pipeline of record, receipt producer, or release gate."
  - "The 5,000 ppm fixture threshold is frozen test data derived from a supplied design document; it is not accepted live policy."
  - "The synthetic survey-area symbol ZZ999 is deliberately non-real and avoids treating SSURGO survey areas as counties."
  - "Soil and NRCS source stewards are required review roles, not parallel authority owners for this repository tool."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SSURGO package drift fixture comparator

> **One-line purpose.** Compare two bounded synthetic SSURGO package sidecars,
> detect package, schema, geometry, chronology, and mapunit-area drift, and emit
> a deterministic report for steward review without fetching, promoting, or
> publishing anything.

## Status and authority boundary

| Surface | Status |
|---|---|
| Fixture parser and comparator | **CONFIRMED bounded executable** |
| Synthetic positive, negative, and threshold fixtures | **CONFIRMED** |
| Live NRCS endpoint, package cadence, rights posture, and SourceDescriptor | **NOT SELECTED / NEEDS VERIFICATION** |
| Live materiality threshold | **NOT ADOPTED** |
| Connector, lifecycle pipeline, receipt, proof, promotion, release, or publication | **OUT OF SCOPE / DENIED** |

This is a watcher-shaped **review-signal helper**, not a watcher service and not
source authority. It may read two explicit local fixture paths and report one
finite outcome. It cannot access the network, select a live source, persist a
checkpoint, create a `SourceIntakeRecord`, write RAW or WORK data, resolve an
`EvidenceBundle`, create a governed receipt, approve policy, promote, release,
or publish.

## Path decision

```yaml
path_decision:
  artifact: ssurgo-package-drift-fixture-comparator
  proposed_path: tools/ingest/ssurgo_watch/ssurgo_watch.py
  artifact_kind: executable_code
  authority_owner: repository_tooling
  lifecycle_stage: not_applicable
  execution_role: repository_tool
  scope_kind: source
  scope_id: fixture-profile-nrcs-ssurgo
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - tools/ingest/README.md
    - docs/domains/soil/CANONICAL_PATHS.md
    - docs/sources/catalog/nrcs/ssurgo.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-004
    - DIR-PLACE-004
    - DIR-PLACE-005
    - DIR-EXEC-007
    - DIR-SOURCE-003
  outcome: PLACE
```

`tools/` owns long-lived repository support tooling. The parent
[`tools/ingest/`](../README.md) contract explicitly admits deterministic,
dry-run, report-only prior/current sidecar comparators. Tests remain under
[`tests/ingest/`](../../../tests/ingest/README.md). No domain or source topic is
introduced as a repository root.

## Frozen fixture profile

Every input must use `kfm.ssurgo-watch.synthetic.v1` and must declare:

- `fixture_only: true`;
- the non-live source reference `fixture://source/nrcs-ssurgo`;
- the non-real survey-area symbol `ZZ999`;
- canonical UTC observation time and an ISO publication date;
- nonzero package and analysis-geometry SHA-256 values;
- versioned extraction- and geometry-profile hashes;
- one exact synthetic analysis area;
- a complete mapunit-area partition of that analysis area;
- per-mapunit geometry fingerprints;
- a canonical bounded table/column schema inventory including primary-key and
  foreign-key declarations;
- one content digest for every profiled table;
- a frozen `mapunit_area_change_ppm` value; and
- a stable `spec_hash` over fixture configuration plus a recomputable
  `content_hash` over the full sidecar.

When mapunit geometry fingerprints differ, the caller must also provide a
separate `kfm.ssurgo-watch.synthetic-spatial-diff.v1` artifact. That artifact
declares the frozen method, `EPSG:5070`, square-metre units, the geometry-profile
hash, both sidecar content hashes, both computed geometry-set hashes, exact
mapunit-label disagreement area, and its own recomputable content hash. Keeping
this evidence separate avoids a predecessor-dependent snapshot hash.

The parser rejects duplicate JSON keys, unknown fields, oversized inputs,
noncanonical dates and timestamps, invalid hashes, coverage mismatch, mismatched
mapunit or table hash inventories, duplicate or unordered columns, unsupported
column or relationship types, live-source fields, and tampered spec/content
hashes.

## Comparison semantics

The helper compares a fixed **survey-area analysis extent**, not a county. That
avoids assuming a one-to-one county relationship that SSURGO does not guarantee.

For two complete mapunit partitions over the same analysis extent, exact
mapunit-label disagreement area is defined as one half of the sum, over mapunit
identifiers, of the symmetric-difference area between the prior and current
mapunit regions. This equals the area whose mapunit label changed. It is not the
symmetric difference of the survey-area union, which would normally be zero.

Half the L1 distance between aggregate per-mapunit areas is only a lower bound
on that spatial quantity. The comparator uses that lower bound as a consistency
check; threshold math uses the separately supplied, content-addressed exact
fixture value. The helper does not calculate geometry.

The fixture rule is intentionally exact:

- a schema inventory, key relationship, or profiled table-content change is
  material;
- an analysis-geometry hash or analysis-area change returns `GEOMETRY_DRIFT`
  before materiality is evaluated;
- a mapunit-geometry fingerprint change without a valid separately hashed and
  fully bound partition-disagreement artifact returns `GEOMETRY_DRIFT`;
- a publication or observation regression returns `STALE_INPUT`;
- an extraction-, geometry-, or materiality-profile change returns `ABSTAIN`;
- changed derived output with an unchanged package digest and unchanged
  extraction, geometry, and materiality profiles returns `ERROR`;
- mapunit-label disagreement area must be **strictly greater than** 5,000 ppm
  (0.5%) of the frozen analysis area to return `PROPOSED_WORK_RECORD`; and
- equality at the 5,000 ppm boundary remains `NO_MATERIAL_CHANGE`.

The 5,000 ppm value is fixture design evidence, not a policy decision. A live
threshold requires its own steward-reviewed policy authority and cannot be
created by this helper or README.

## Finite outcomes

| Outcome | Meaning | Exit |
|---|---|---:|
| `NO_MATERIAL_CHANGE` | Inputs are valid; schema, constraints, and profiled content are stable; label disagreement did not cross the frozen rule. | `0` |
| `PROPOSED_WORK_RECORD` | Schema, key-constraint, profiled table-content, or above-threshold label drift requires governed review. | `1` |
| `GEOMETRY_DRIFT` | The comparison extent changed, or mapunit fingerprints changed without bound spatial evidence; rebase or supply the fixture diff. | `1` |
| `STALE_INPUT` | Observation or publication chronology regressed. | `1` |
| `ABSTAIN` | Extraction, geometry, or materiality comparison semantics changed. | `1` |
| `ERROR` | An input failed validation or package/derived-state consistency failed. | `1` |

Every report sets `publication: false` and `promotion_allowed: false`.
`steward_review_required` is false only for `NO_MATERIAL_CHANGE`.
`PROPOSED_WORK_RECORD` is only a review signal; the helper does not write that
record into a lifecycle store.

## Direct children

```text
tools/ingest/ssurgo_watch/
├── README.md
└── ssurgo_watch.py
```

The Python module is durable repository tooling. It reads caller-selected local
fixtures, returns a deterministic JSON report, and may create one explicit file
outside the repository. It retains no state. Repository, lifecycle, receipt,
proof, release, and published destinations are denied.

## Run the fixture proof

From the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

Example dry run:

```bash
python tools/ingest/ssurgo_watch/ssurgo_watch.py \
  --prior tests/ingest/ssurgo_watch/fixtures/material_area_change/prior.sidecar.json \
  --current tests/ingest/ssurgo_watch/fixtures/material_area_change/current.sidecar.json \
  --spatial-diff tests/ingest/ssurgo_watch/fixtures/material_area_change/spatial_diff.json \
  --dry-run
```

`--output` is optional, create-only, and restricted to an existing directory
outside the repository. This prevents the helper from writing into RAW, WORK,
receipt, proof, release, or published authority lanes.

## Evidence lineage

The implementation independently adapts the SSURGO low-churn material-change
idea in the supplied `New Ideas 5-15-26.pdf` (design discussion on pages 18-22
and 137-145). It reconciles that idea with current repository evidence:

- [`docs/sources/catalog/nrcs/ssurgo.md`](../../../docs/sources/catalog/nrcs/ssurgo.md)
  keeps live endpoint, rights, cadence, and source activation provisional;
- [`docs/domains/soil/CANONICAL_PATHS.md`](../../../docs/domains/soil/CANONICAL_PATHS.md)
  requires support-type and responsibility-root separation;
- [`tools/ingest/README.md`](../README.md) limits this lane to deterministic
  ingest-adjacent reports; and
- [`cdl_watch/`](../cdl_watch/README.md) supplies the current repo-native
  fixture-comparator pattern without making this tool a CDL copy or shared
  authority contract.

No third-party code, source bytes, endpoint, package identifier, county record,
or rights assertion is copied into this slice.

## Known limits and deferred work

- The spatial-diff fixtures assert exact mapunit-label disagreement values; the
  helper verifies their hashes, bindings, profile, CRS, unit, and aggregate
  lower bound, but does not recompute geometry. A live pipeline must calculate
  and retain this metric from admitted source geometry.
- The synthetic schema and complete-table digest inventory proves drift
  mechanics for the tiny fixture profile, not real SSURGO table completeness or
  semantic compatibility.
- The fixture profile does not validate MUKEY/COKEY/CHKEY lineage.
- Package digests and geometry hashes are synthetic; they prove comparison
  behavior only.
- Live fetching belongs under an admitted connector; lifecycle transforms
  belong under a governed pipeline; receipts, policy, proofs, release, and
  publication retain their own responsibility roots.

## Rollback

Revert the feature commit. The helper creates no live source state, lifecycle
data, receipt, proof, release candidate, or published artifact, so no external
or data-state rollback is required.

[Back to top](#top)
