# Fauna–Habitat cross-domain tests

## Current status

**PARTIAL, executable, fixture-only.** This lane now contains a pair-specific public-safe assignment candidate test profile. It closes the prior README-only gap without claiming that the full Habitat × Fauna seam, permissive scaffold join schema, policy evaluator, proof pipeline, release candidate, governed API, MapLibre layer, Evidence Drawer response, or publication path is complete.

## What is proved

The focused tests prove that the current generic `CrossLaneJoinAssessment` can be constrained for one synthetic Fauna–Habitat pair profile so that:

- Fauna and Habitat endpoint ownership stays separate;
- source roles and EvidenceRefs stay visible;
- public-safe generalized fixtures may emit only a `CANDIDATE_RELATION`;
- missing evidence and role/sensitivity ambiguity abstain;
- exact restricted/prohibited geometry denies;
- public-safe exact geometry fails the pair profile;
- all lifecycle, evidence, policy, review, release, publication, and public-use effects remain false;
- fixture provenance is synthetic and no coordinate/geometry bytes or network access are used.

## What is not proved

A passing test does not prove a real occurrence, habitat assignment, canonical relationship, live-source rights, geoprivacy transform, EvidenceBundle resolution, policy decision, reviewer approval, proof pack, PromotionDecision, ReleaseManifest, public API, map layer, release, deployment, or publication.

## Owning roots

- Meaning: `contracts/cross_domain/fauna_habitat/`
- Shared validator: `tools/validators/cross_domain/fauna_habitat/`
- Synthetic assessment fixtures: `fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/`
- Tests: this directory
- Generic machine shape and deterministic assessment: existing `schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json` and `tools/joins/join_candidates.py`

This follows accepted ADR-0029 and Directory Governance Standard v2 §12.5. No lead domain owns the seam.

## Run

```bash
python tools/joins/join_candidates.py --fixtures
python tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py --fixtures
python -m pytest \
  tests/joins/test_join_candidates.py \
  tests/cross_domain/fauna_habitat/test_public_safe_assignment.py \
  -q --strict-config --strict-markers
```

## Acceptance boundary

The lane remains `PARTIAL` until separate authority and implementation work resolves the canonical pair contract/schema/policy relationship, creates representative evidence-bound public-safe fixtures, executes geoprivacy transforms where needed, and closes proof/release/correction/rollback behavior. This PR deliberately does not cross those gates.

## Rollback

Revert the bounded implementation commit. The earlier documentation-only state is recoverable from Git history; no source, data, lifecycle, proof, release, or publication object requires reversal.
