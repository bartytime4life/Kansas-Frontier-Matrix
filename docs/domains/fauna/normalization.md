<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/fauna/normalization
title: Fauna Offline Normalization
type: implementation-guide
version: v0.1
status: draft
owners: ["@bartytime4life - repository review route; domain authority unverified"]
created: 2026-10-29
updated: 2026-10-29
policy_label: public
owning_root: docs/
responsibility: Explain the implemented local Fauna normalization and its verification boundary
truth_posture: CONFIRMED local source and focused tests; UNKNOWN live source admission and production operation
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/domains/fauna/occurrence_evidence.md
  - contracts/domains/fauna/taxon_crosswalk.md
  - packages/domains/fauna/README.md
  - pipelines/domains/fauna/README.md
tags: [fauna, normalization, taxonomy, quarantine, no-network]
[/KFM_META_BLOCK_V2] -->

# Fauna offline normalization

This implementation turns local, source-shaped OccurrenceEvidence candidates
into deterministic, schema-checked **internal quarantine candidates**. It also
provides explicit-snapshot taxonomy matching and a small allowlisted metadata
projection for internal review. It introduces no public route, source fetcher,
lifecycle writer, geoprivacy approval, or release decision.

The implementation base is `main@fe50cdbf7eb91f3fcc236fcbe3a8a882bd9972b4`.
The source-shaped input uses the existing
[OccurrenceEvidence contract](../../../contracts/domains/fauna/occurrence_evidence.md).
All source-native values remain in the original local input and its raw-artifact
reference; the source scientific name also survives in the normalized taxon.

## Components and placement

[Accepted Directory Rules](../../doctrine/directory-rules.md) sections 7.2 and 12,
under [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place
each artifact inside an existing responsibility root:

| Owner | Implementation | Responsibility |
|---|---|---|
| `packages/` | [Fauna library](../../../packages/domains/fauna/src/fauna/) | Reusable identity, validation, taxonomy, normalization, and review projection |
| `pipelines/` | [Local rehearsal](../../../pipelines/domains/fauna/normalize.py) | Bounded batch orchestration with aggregate-only stdout |
| `schemas/` | [Candidate taxonomy snapshot](../../../schemas/contracts/v1/domains/fauna/taxonomy_snapshot.schema.json) | Closed draft shape for one supplied matching inventory |
| `fixtures/` | [Normalization fixture](../../../fixtures/domains/fauna/normalization/README.md) | Entirely invented names, identifiers, and references |
| `tests/` | [Fauna tests](../../../tests/domains/fauna/) | Offline conformance, ambiguity, denial, malformed-input, and leakage tests |
| `tools/` | [Occurrence validator](../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py) | Existing repository CLI, backed by the shared validation engine |
| `.github/` | [Focused workflow](../../../.github/workflows/fauna-occurrence-evidence.yml) | Changed-area validation; does not produce release approval |

There are no root moves, compatibility-root writes, new registries, or new
policy/release/proof homes. `packages/taxonomy/` remains a broader planned
cross-domain surface; this bounded resolver stays in the existing Fauna package
and does not claim cross-domain authority.

## Behavior

`TaxonomyCatalog.from_candidate(snapshot, schema=...)` accepts a closed,
candidate-only snapshot. Matching normalizes case, Unicode NFC, and whitespace;
authorship and rank qualifiers are retained. Only accepted names and explicitly
listed synonyms match. Multiple matching concepts yield `ambiguous`; unknown
names yield `unresolved`. Neither case fabricates a taxon or normalized record.
The snapshot is an input inventory, not an admitted authority, full `Taxon`, or
cross-authority `TaxonCrosswalk` decision.

`normalize_occurrence(...)` preserves source family/role, observation time,
internal coordinates, source links, and raw-artifact linkage. It carries the
taxonomy snapshot and concept evidence references forward, without letting
taxonomy evidence replace missing occurrence evidence. It always withholds
public geometry, resets review strength to `unreviewed`, and emits `quarantine`.
Existing denial/error dispositions and earlier hold reasons survive. Invalid
shape, rights metadata, provenance, or source-role/basis combinations return
bounded findings with no usable normalized payload.

`prepare_public_candidate(...)` validates before selecting an explicit field
allowlist. Held or sensitive records return no payload. The positive result is
only internal, unreleased taxon/role metadata: no location, dates, observer,
source identifiers, links, free text, or evidence URLs. It is not an
`OccurrencePublic` instance or evidence-closed UI response.

Identity retains the existing draft RFC 8785 JCS + SHA-256 subject and digest
grammar. That subject omits source family and role, so the digest is **not a
global cross-source deduplication key**. Batch processing preserves every input
and its order. A future identity expansion needs a versioned migration.

## Run and validate

Use Python 3.11 or later with the root project dependencies. To install the
reusable package, install the local hashing package first:

```bash
python -m pip install -e packages/hashing -e packages/domains/fauna
python pipelines/domains/fauna/normalize.py \
  --input fixtures/domains/fauna/occurrence_evidence/valid/valid_observed_open.json \
  --taxonomy fixtures/domains/fauna/normalization/taxonomy_snapshot.json \
  --validated-at 2026-10-29T00:00:00Z
python -m unittest -v \
  tests.domains.fauna.test_taxonomy_resolution \
  tests.domains.fauna.test_occurrence_split \
  tests.domains.fauna.test_normalization_pipeline \
  tests.domains.fauna.test_occurrence_evidence
```

The CLI accepts one local object or an array of at most 1,000 records. The shared
JSON loader rejects duplicate keys, nonfinite numbers, oversized/deep inputs,
and non-regular or final-component symlink inputs. Schemas use an empty
reference registry: unresolved external references fail without network access.
Stdout contains aggregate counts and `public_ready: false`; normalized payloads
remain in memory for separately governed callers. Exit 0 means the rehearsal
completed with held/empty results; 1 means record errors/denial; 2 means invalid
input. None means release readiness. Empty inventory reports `EMPTY`.

## Optional local EvidenceBundle binding check

`EvidenceCatalog.from_candidates(bundles, schema=..., resources=...)` validates
an explicit local bundle inventory against the existing
[shared EvidenceBundle schema](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json).
The [Fauna projection](../../../schemas/contracts/v1/domains/fauna/evidence_bundle.schema.json)
already references that shared shape. This increment creates no parallel
EvidenceBundle schema, evidence store, registry, policy or release authority.
The helper belongs in `packages/`; the opt-in rehearsal stays in `pipelines/`;
synthetic inputs and executable evidence remain in `fixtures/` and `tests/`,
under the same Directory Rules sections 7.2 and 12 basis as the initial slice.

```bash
python pipelines/domains/fauna/normalize.py \
  --input fixtures/domains/fauna/occurrence_evidence/valid/valid_observed_open.json \
  --taxonomy fixtures/domains/fauna/normalization/taxonomy_snapshot.json \
  --validated-at 2026-10-29T00:00:00Z \
  --evidence-bundles fixtures/domains/fauna/evidence_bindings/bundles.json
python -m unittest -v tests.domains.fauna.test_evidence_closure
```

The CLI accepts an array of at most 128 candidate bundles, each with at most
256 constituent refs. The library accepts at most 16 explicitly supplied
schema resources; the CLI supplies the three existing shared leaf schemas.
Its reference registry cannot fetch missing schemas. Duplicate bundle IDs,
duplicate constituents, blank scope/source/citation metadata, invalid schema
fields and dangling `bundle_ref` declarations reject the inventory. When
present, a constituent `bundle_ref` must equal its containing `bundle_id`;
URI aliases require separate governed resolution and are not inferred here.

`catalog.assess(occurrence, schema=...)` checks the occurrence first and matches
every occurrence and taxonomy reference exactly. Missing or multiply matched
refs abstain. At least one linked bundle must declare the source record;
when a raw artifact is present, a bundle supporting that source record must
also declare its checksum. This checks literal metadata membership, not whether
claim scope, source attribution or a declared checksum is factually correct.
The immutable index retains reference/support sets rather than bundle payloads.
Input order cannot choose a winner between colliding bundles.

The result is `linked`, `abstain`, `error`, or a preserved upstream `deny`.
Even `linked` reports `public_ready: false` and `integrity_verified: false`.
It does not interpret claims, authenticate rights, verify source admission,
recompute bundle/spec/artifact hashes, retrieve raw files, or close evidence.
The normalized record keeps `quarantine`, `unreviewed`, withheld geometry and
`prov.evidence_closure_unverified`; the assessment never mutates it.

With the flag, aggregate stdout adds `evidence_bindings` counts for checked,
linked, abstained, failed and skipped records. A failed normalization is
skipped, never counted as evidence checked. An empty inventory abstains on
each normalized record; an empty input batch remains `EMPTY`. Metadata
abstention remains `HELD` with exit 0; malformed inventory exits 2. Without
the flag, the existing summary and behavior are unchanged. Both input modes
avoid outputting refs, source IDs, paths, bundle text or occurrence payloads.

## Source basis and limits

The local Repository Build-Out & Markdown Modernization Implementation Agent
v7 and Fauna seed-card programming surface informed this reversible branch
slice. Synced `sources/` material was read without modification. A Drive
[Habitat/Fauna coordination note](https://drive.google.com/file/d/1F-yD2slZM-FPQvbYWUx5whfFVPgxgzjx/view)
was checked as historical documentation, not decision acceptance.

Research informs the conservative boundaries. GBIF documents that sensitive
fields and contextual information can require withholding or generalization;
this implementation chooses withholding and introduces no invented distance
threshold. [GBIF guidance](https://docs.gbif.org/sensitive-species-best-practices/master/en/index.en.html)
Scientific distribution maps also carry uncertainty from data and mapping;
this helper makes no range, absence, occupancy, or abundance inference.
[Rocchini et al., 2011](https://doi.org/10.1177/0309133311399491)
External JSON Schema retrieval is explicitly disabled following the library's
[reference handling guidance](https://python-jsonschema.readthedocs.io/en/latest/referencing/).
SciSpace, Life Sciences database/literature lookups, and these documents were
research context only. No live biological records were imported or admitted.

Production source admission, rights verification, EvidenceBundle closure,
policy evaluation, stewardship, generalized map layers, governed API/UI wiring,
release/correction/rollback records, deployment, and publication remain open.
Creative assets and a new visual design are outside this processing slice.

## Rollback

Revert the scoped implementation commit(s) to restore the prior validator and
package/pipeline placeholders. There is no data migration or live-state write
to reverse. Do not delete or rewrite original source inputs.
