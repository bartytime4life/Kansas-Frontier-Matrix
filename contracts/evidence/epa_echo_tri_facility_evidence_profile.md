<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/epa-echo-tri-facility-evidence-profile
title: EPA ECHO/TRI Facility Evidence Profile
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; evidence; fixture-only; no-authority
owning_root: contracts/
responsibility: Keep EPA ECHO compliance context and TRI annual releases separate inside a fixture-only EvidenceBundle profile.
truth_posture: "CONFIRMED repository dependencies; PROPOSED profile; NEEDS VERIFICATION source rights and human review"
related:
  - ./evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/epa_echo_tri_facility_evidence_profile.schema.json
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, echo, tri, facility, source-role, pass-2]
[/KFM_META_BLOCK_V2] -->

# EPA ECHO/TRI Facility Evidence Profile

This closed, fixture-only profile adapts `KFM-P2-IDEA-0025` and `KFM-P2-PROG-0007`. It embeds the existing `EvidenceBundle` shape, keeps `ECHO_COMPLIANCE`, `TRI_ANNUAL_RELEASE`, and optional `DERIVED_PUBLIC_SAFE_SUMMARY` roles non-interchangeable, and denies exact geometry or authority-bearing claims.

## Boundary

- `status=PROPOSED_INACTIVE`; `execution_mode=FIXTURE_ONLY`.
- ECHO may support compliance, inspection, or enforcement context. It cannot establish annual chemical-release quantities or facility truth.
- TRI may support annual source-reported releases. It cannot establish compliance, current emissions, or a facility score.
- A derived summary remains generalized and must cite upstream support.
- Missing policy, review, or evidence support returns `ABSTAIN`.
- Unsafe role collapse or precise/private/operational detail returns `DENY`.
- Identity, time, arithmetic, and hash contradictions return `ERROR`.
- `PASS` proves local synthetic consistency only.

## Directory Rules basis

Semantic meaning stays in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; fixtures, validator, tests, workflow, exploratory source map, and generated receipt stay in their existing responsibility roots. No source registry, connector, lifecycle record, proof, release, API, UI, map layer, or publication authority is created.

## Validation

```bash
python -m unittest discover --start-directory tests/validators --pattern 'test_validate_epa_echo_tri_facility_evidence_profile.py' --verbose
KFM_NO_NETWORK=1 python tools/validators/validate_epa_echo_tri_facility_evidence_profile.py --fixtures
```

## Non-effects and rollback

No live EPA request, source activation, evidence resolution, policy decision, lifecycle write, release, deployment, or publication occurs. Before merge, close the draft PR. After an authorized merge, revert its bounded commit or merge commit.
