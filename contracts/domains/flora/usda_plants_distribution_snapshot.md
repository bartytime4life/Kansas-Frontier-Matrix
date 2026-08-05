# USDA PLANTS Distribution Snapshot Candidate Contract

**Status:** PROPOSED, fixture-first, no-network.  
**Object:** `USDAPlantsDistributionSnapshotCandidate`  
**Scope:** a source-versioned Kansas county-by-taxon distribution matrix derived from an explicitly bounded synthetic CSV profile.  
**Authority boundary:** structural conformance is not source admission, botanical occurrence proof, rights clearance, sensitivity clearance, promotion, release, or publication.

## Purpose

The New Ideas 4-30 source map identifies a remaining repository gap after reconciling the packet with current Flora and USDA PLANTS documentation: define source-versioned distribution states and missing-row behavior with synthetic counties and taxa without activating the live source.

This contract closes that narrow gap. It represents the complete cross-product of a declared taxon universe and Kansas county universe. Every taxon-county pair has one explicit state, so a missing source row cannot silently become an absence claim.

## Source-role and claim boundary

USDA PLANTS distribution rows are treated here as **administrative distribution claims**.

They are not:

- specimen or observation evidence;
- proof that a taxon currently occurs at a precise place;
- proof that a taxon is absent when no row is present;
- rare-plant sensitivity approval;
- release or publication authority.

`source_role` is fixed to `administrative` for this candidate profile. Promotion cannot upgrade that role.

## Distribution state vocabulary

| State | Source row required | Interpretation |
|---|---:|---|
| `reported_present` | yes, normalized as `present` | `administrative_presence_claim` |
| `reported_absent` | yes, normalized as `absent` | `administrative_absence_claim` |
| `not_reported` | no | `no_claim` |
| `not_evaluated` | no | `no_claim`; reserved for a future profile that declares incomplete source coverage |

The profile fixes `missing_row_policy` to:

```text
NO_SOURCE_ROW_IS_NO_CLAIM_NOT_ABSENCE
```

An absence is valid only when an explicit normalized source row says `absent`.

## Deterministic identity

The candidate identity is:

```text
kfm://candidate/flora/usda-plants/distribution/ks/<snapshot_date>
```

`spec_hash` is SHA-256 over canonical JSON after removing only the top-level `spec_hash` member. Canonical JSON uses sorted keys, UTF-8, ASCII escaping, no insignificant whitespace, and no non-finite numbers.

Taxa, counties, normalized source rows, and distribution-state cells are sorted before hashing. The input file digests are included in provenance.

## Required review hold

Every v1 fixture candidate is explicitly non-releasable:

- `review.rights = NEEDS_VERIFICATION`
- `review.sensitivity = NEEDS_VERIFICATION`
- `review.release = HOLD`
- holds include source-rights/currentness verification and rare-plant sensitivity assessment.

A successor profile may change this posture only after source terms, descriptor activation, steward review, policy, evidence, and release controls are accepted.

## Input profile

The normalizer accepts three local UTF-8 CSV files with exact headers:

```text
taxa.csv:         plants_symbol,scientific_name,family
counties.csv:     fips,name
distribution.csv: plants_symbol,county_fips,presence
```

The CSV profile is synthetic and deliberately narrower than live USDA downloads. Exact live filenames, headers, codes, cadence, terms, and attribution remain NEEDS VERIFICATION.

## Invariants

- Kansas county FIPS are five digits and begin with `20`.
- USDA PLANTS symbols are unique in the declared taxon universe.
- Scientific names include a bounded authorship heuristic; this is validation support, not taxonomic authority.
- Source rows reference only declared taxa and counties.
- Source-row pairs and distribution-state pairs are unique and sorted.
- The distribution-state set exactly covers `taxa × counties`.
- Reported presence/absence states reconcile to explicit normalized source rows.
- `first_observed` remains `null`; the profile does not invent an observation date.
- Exact coordinates or geometry fields are denied.
- References into RAW, WORK, or QUARANTINE are denied from the candidate object.
- Evidence references are digest-bound.
- Summary counts must recompute exactly.

## Directory Rules basis

The accepted responsibility-root model is preserved:

- semantic meaning: `contracts/domains/flora/`
- machine shape: `schemas/contracts/v1/domains/flora/`
- synthetic inputs and expected records: `fixtures/domains/flora/`
- normalization tool: `tools/ingest/usda_plants/`
- semantic validator: `tools/validators/domains/flora/`
- regression proof: `tests/domains/flora/`
- hosted orchestration: `.github/workflows/`

No connector alias is selected or activated. No new root or parallel source, schema, policy, receipt, proof, release, or publication home is created.

## Validation

```bash
python -m pytest -q tests/domains/flora/test_usda_plants_distribution_snapshot.py
python tools/validators/domains/flora/validate_usda_plants_distribution_snapshot.py --fixtures
```

The workflow also rebuilds the valid fixture from the synthetic CSV inputs and byte-compares the result.

## Non-effects

This contract and its tools perform no network request, live USDA download, source activation, raw-store write, taxonomy acceptance, occurrence validation, geoprivacy decision, EvidenceBundle resolution, policy evaluation, promotion, release, deployment, or publication.

## Rollback

Revert the contract, schema, fixture family, normalizer, validator, tests, and workflow together. The slice is additive and creates no migration or persistent runtime state.
