<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-flora-readme
title: tools/validators/domains/flora README
type: README
version: v0.2.0
status: repository-grounded draft; one bounded executable profile established
owner: NEEDS VERIFICATION — tooling/QA owner, Flora steward, sensitivity/geoprivacy reviewer, policy steward, evidence steward
created: 2026-07-07
updated: 2026-08-03
policy_label: repository-facing; flora; synthetic-fixtures; fail-closed; non-authoritative
owning_root: tools/
responsibility: bounded Flora validator implementations that check declared synthetic fixture profiles without creating botanical, policy, proof, release, or publication authority
truth_posture: cite-or-abstain; executable claims are limited to the named profile and tests below
related:
  - ../../_common/public_safe_fixture.py
  - ../../../../../tests/domains/flora/README.md
  - ../../../../../fixtures/domains/flora/README.md
  - ../../../../../docs/domains/flora/README.md
  - ../../../../../policy/domains/flora/README.md
  - ../../../../../policy/sensitivity/flora/README.md
  - ../../../../../data/proofs/flora/README.md
  - ../../../../../release/candidates/flora/README.md
notes:
  - "The executable profile validates synthetic public-safe candidates only."
  - "A PASS is fixture conformance, not botanical truth, source admission, rights clearance, stewardship approval, proof, release, or publication."
  - "Exact or reverse-engineerable sensitive Flora locations and geoprivacy transform parameters fail closed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/domains/flora/` — Flora Validators

[![Status: bounded executable](https://img.shields.io/badge/status-bounded%20executable-1a7f37?style=flat-square)](#current-implementation)
[![Network: forbidden](https://img.shields.io/badge/network-forbidden-b42318?style=flat-square)](#execution)
[![Sensitivity: fail closed](https://img.shields.io/badge/sensitivity-fail%20closed-b42318?style=flat-square)](#profile-boundary)
[![Authority: validation only](https://img.shields.io/badge/authority-validation%20only-6e7781?style=flat-square)](#authority-boundary)

> **Purpose.** Hold deterministic Flora validators under the `tools/` responsibility root. The current implementation is intentionally narrow: it validates one closed, synthetic, public-safe fixture profile and emits stable machine findings without echoing candidate values.

> [!IMPORTANT]
> A successful run proves only conformance to the frozen synthetic fixture profile. It does not establish a real occurrence, accepted taxonomy, source authority, rights, sensitivity approval, stewardship review, EvidenceBundle closure, release readiness, or public safety.

## Current implementation

| Surface | State |
|---|---|
| `validate_public_safe_fixture.py` | **Implemented** — standard-library, deterministic, no-network validator |
| Shared mechanics | `tools/validators/_common/public_safe_fixture.py` |
| Positive fixture | `fixtures/domains/flora/valid/public_safe_occurrence.json` |
| Exact negative fixtures | `fixtures/domains/flora/invalid/*.json` with `*.expected_error.txt` sidecars |
| Tests | `tests/domains/flora/test_flora_smoke.py` |
| CI | `domain-flora / validate-flora` executes the focused test module |
| Flora proof producer | **Not established; held** |
| Flora release dry run | **Not established; held** |

## Profile boundary

The validator accepts only a synthetic candidate that declares:

- fixture-only identity and network-forbidden posture;
- synthetic taxon and source references;
- the frozen `synthetic_occurrence` source role;
- fixture-only rights and evidence references;
- generalized fixture-area support rather than coordinates or geometry;
- no exact, reverse-engineerable, private-land, or culturally sensitive location state;
- a fixture redaction-receipt reference and fixture review-record reference;
- `not_released` and `promotion_eligible: false` governance;
- explicit caveats stating the record is synthetic, is not a botanical occurrence claim, and is not released.

The profile rejects:

- undeclared fields at every owned object level;
- exact-location aliases, coordinates, WKT-like values, parcel/access/collection clues;
- URLs and external references;
- redaction offsets, generalization thresholds, jitter seeds, precision values, or other transform secrets;
- missing or malformed taxon, source, evidence, review, or redaction references;
- occurrence/model/range role collapse;
- unresolved taxonomy or rights state;
- release or promotion claims;
- malformed, duplicate-key, non-finite, oversized, overly deep, overly large, or non-regular JSON inputs.

## Execution

From repository root:

```bash
python tools/validators/domains/flora/validate_public_safe_fixture.py \
  fixtures/domains/flora/valid/public_safe_occurrence.json
```

Expected exit codes:

| Code | Meaning |
|---:|---|
| `0` | Every supplied fixture conforms to the bounded profile |
| `1` | At least one supplied fixture has findings |
| `2` | CLI usage error, such as no fixture path |

Each input produces one compact JSON line:

```json
{"file":"<path>","findings":[],"scope":"flora-public-safe-fixture","status":"PASS"}
```

Findings contain only stable `code` and `path` values. Candidate values are never echoed.

## Authority boundary

This lane owns validator implementation only. It does not own:

- Flora object meaning or taxonomy;
- source admission or source-role authority;
- rights, sensitivity, stewardship, or sovereignty decisions;
- geoprivacy transform implementation;
- canonical EvidenceBundle or proof records;
- receipts, policy decisions, release manifests, corrections, withdrawals, or rollback cards;
- public API, map, tile, search, Focus Mode, or AI output.

Those responsibilities remain in their governing roots. The validator may check references to them only within the declared synthetic profile.

## Stable findings

| Finding family | Examples |
|---|---|
| Shape | `CANDIDATE_NOT_OBJECT`, `UNDECLARED_*`, `FIXTURE_JSON_INVALID` |
| Identity/support | `RECORD_ID_INVALID`, `TAXON_REF_INVALID`, `SOURCE_DESCRIPTOR_REF_INVALID`, `EVIDENCE_REFS_INVALID` |
| Role/rights | `SOURCE_ROLE_INVALID`, `TAXON_CONCEPT_STATE_INVALID`, `RIGHTS_STATE_INVALID` |
| Spatial/sensitivity | `SPATIAL_SUPPORT_INVALID`, `SENSITIVE_LOCATION_FIELD_FORBIDDEN`, `COORDINATE_LIKE_VALUE_FORBIDDEN`, `SENSITIVITY_STATE_INVALID` |
| Public controls | `PUBLIC_REPRESENTATION_INVALID`, `PUBLIC_CAVEATS_INVALID`, `GOVERNANCE_STATE_INVALID` |
| Exfiltration/secret resistance | `EXTERNAL_REFERENCE_FORBIDDEN`, `TRANSFORM_SECRET_FIELD_FORBIDDEN`, `NUMERIC_VALUE_FORBIDDEN` |
| Loader bounds | `FIXTURE_TOO_LARGE`, `FIXTURE_JSON_INVALID` |

## Validation command

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

The suite blocks common socket and `urllib` entry points, exercises exact fixture inventories and sidecars, tests parser bounds and CLI contracts, and verifies that sensitive candidate values are not emitted.

## Deferred work

Broader Flora validation remains **PROPOSED** or **NEEDS VERIFICATION**, including real contract/schema validation, accepted source and taxon vocabularies, rights and sensitivity policy execution, deterministic geoprivacy transforms, EvidenceBundle resolution, release candidates, corrections, and rollback drills.

[Back to top](#top)
