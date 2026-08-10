<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/habitat/land-cover/cover-class-crosswalk-profile
title: Habitat Cover-Class Crosswalk Profile
type: semantic-contract-profile
version: 0.1.0
status: proposed
owner: OWNER_TBD — Habitat steward · Land-cover steward · Crosswalk steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; proposed; fixture-only; no-silent-recode; non-authoritative
owning_root: contracts/
responsibility: fixture-only semantic meaning for version-bound Habitat CoverClassCrosswalk candidates
truth_posture: cite-or-abstain
related:
  - contracts/domains/habitat/land_cover/crosswalk.md
  - contracts/domains/habitat/land_cover/class_scheme.md
  - docs/domains/habitat/sublanes/land_cover.md
  - schemas/contracts/v1/domains/habitat/land_cover/cover_class_crosswalk_profile.schema.json
  - fixtures/domains/habitat/land_cover/crosswalk/profile_cases.json
  - tools/validators/domains/habitat/validate_cover_class_crosswalk_profile.py
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Additive fixture-only profile; it does not replace the broader crosswalk contract or its permissive scaffold schema."
  - "PASS proves bounded synthetic consistency only. It does not create a reviewed crosswalk, recode source data, resolve evidence, decide policy, approve release, render a layer, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# Habitat Cover-Class Crosswalk Profile

> **PROPOSED:** This additive profile makes a bounded Pass 20 semantic-drift
> requirement executable for the established Habitat `CoverClassCrosswalk`
> family: source and target schemes must be version-pinned, every source class
> must be accounted for, and lossy or reverse mappings must never be silent.

## Compatibility and authority boundary

The broader semantic contract remains
`contracts/domains/habitat/land_cover/crosswalk.md`. Its paired
`crosswalk.schema.json` remains a permissive proposed scaffold. This profile
does not silently tighten that schema or claim compatibility for existing
objects. It applies only to synthetic candidates declaring:

```json
{"profile_version":"kfm.cover-class-crosswalk-candidate.v1"}
```

Objects without that discriminator are outside this validator. A passing
candidate is still `REVIEW_REQUIRED`; it is not a reviewed mapping, class
scheme, observation, renderer transform, change summary, source activation,
policy decision, release manifest, or published Habitat product.

| Responsibility | Owning surface |
|---|---|
| Broad crosswalk meaning | `contracts/domains/habitat/land_cover/crosswalk.md` |
| Bounded candidate profile | `contracts/domains/habitat/land_cover/cover_class_crosswalk_profile.md` |
| Machine shape | `schemas/contracts/v1/domains/habitat/land_cover/cover_class_crosswalk_profile.schema.json` |
| Synthetic polarity evidence | `fixtures/domains/habitat/land_cover/crosswalk/profile_cases.json` |
| Local deterministic checks | `tools/validators/domains/habitat/validate_cover_class_crosswalk_profile.py` |
| Real scheme/crosswalk records | separately reviewed lifecycle, registry, evidence, and release surfaces |

## Required scheme anchors

Both source and target schemes carry:

- a distinct `scheme_id`;
- an explicit semantic `scheme_version`;
- an `ontology_ref` whose version suffix exactly matches that version;
- a sorted, unique class-code inventory; and
- an explicit source role that the crosswalk cannot upgrade or collapse.

The fixture grammar uses synthetic URNs only. The profile neither activates a
source nor asserts that the toy classes correspond to any real NLCD, GAP,
LANDFIRE, NWI, CDL, or other source legend.

## Required mapping behavior

Each source class must occur in exactly one mapping row. Target codes must
exist in the declared target scheme. Mapping rows are sorted and explicit:

| Mapping state | Required posture |
|---|---|
| `EXACT` | one source to one target; not lossy; no caveat required |
| `AGGREGATED` | two or more source codes to one target; lossy and caveated |
| `SPLIT` | one source to two or more targets; lossy and caveated |
| `AMBIGUOUS` | one or more targets; lossy and caveated |
| `NODATA` | no target code; caveated; never treated as land cover |
| `UNMAPPED` or `DENIED` | no target code; explicit but denied until remapped or separately resolved |

The profile is forward-only. A reverse or bidirectional request fails closed
because a fixture candidate cannot supply the separate review required for
reverse use. Allowed use is limited to fixture validation. Observation truth,
renderer transformation, public release, and automated reverse mapping are
fixed denied uses.

## Identity and summary

`spec_hash` is the repository canonical hash of every field except
`candidate_id` and `spec_hash`. `candidate_id` is the first 24 lowercase hex
characters of that hash with prefix `kfm:cover-class-crosswalk:`.

The summary is derived from scheme and mapping content. It records scheme
version binding, source-class coverage, unmapped count, row count, visible
lossiness/caveats, and fixed non-authority flags. The validator denies a false
summary rather than trusting it.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed schema and bounded semantics pass; state remains `REVIEW_REQUIRED`. |
| `DENY` | A readable candidate violates shape, version binding, coverage, mapping, identity, or authority rules. |
| `ERROR` | Input cannot be evaluated safely. |

There is no `APPROVED`, `READY`, `RELEASED`, or `PUBLISHED` result.

## Required fail-closed behavior

The validator denies ontology/version drift, duplicate or missing source-class
coverage, unknown target codes, unmarked aggregation or split lossiness,
missing caveats, unmapped classes, unreviewed reverse use, source-role
collapse, non-canonical identity, summary tampering, unknown fields, and any
authority escalation. Duplicate JSON keys, non-finite numbers, symbolic links,
oversized input, and malformed JSON are errors.

## Acceptance evidence

This profile is reviewable when its closed Draft 2020-12 schema meta-validates;
exact positive and negative fixtures replay deterministically; the no-network
test denies socket creation; existing Habitat land-cover materiality tests
remain green; documentation metadata validates; workflow YAML parses; and the
generated authoring receipt binds every introduced byte. Hosted exact-head CI
and human review remain pending on the draft pull request.

## Rollback

Revert the additive profile commit. Rollback removes only this profile,
schema, fixture manifest, validator, tests, workflow, source map, and authoring
receipt. It does not change the broad crosswalk contract, permissive scaffold,
source data, scheme records, mappings, renderers, releases, or public layers.
