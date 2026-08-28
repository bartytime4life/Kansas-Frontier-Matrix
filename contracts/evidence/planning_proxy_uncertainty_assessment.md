<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/planning-proxy-uncertainty-assessment
title: PlanningProxyUncertaintyAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Planning-analysis steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; planning; proxy; uncertainty; disclosure
responsibility: Define fixture-only declaration-coherence semantics for proxy-supported planning analysis without creating evidence, policy, review, release, publication, or decision authority.
truth_posture: "CONFIRMED source-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./evidence_bundle.md
  - ./representation_fitness_assessment.md
  - ../../schemas/contracts/v1/evidence/planning_proxy_uncertainty_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/planning_proxy_uncertainty_assessment/cases.json
  - ../../tools/validators/evidence/validate_planning_proxy_uncertainty_assessment.py
  - ../../tests/validators/evidence/test_validate_planning_proxy_uncertainty_assessment.py
  - ../../docs/intake/exploratory/pass-18-planning-proxy-uncertainty-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# PlanningProxyUncertaintyAssessmentCandidate

`PlanningProxyUncertaintyAssessmentCandidate` is an additive, fixture-only profile for declaring when a planning analysis is data-poor, which proxies or assumptions it uses, how uncertainty is characterized, and where limitations are disclosed.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-320`: planning support in data-poor contexts should record proxy data, assumptions, uncertainty, and scenario-analysis limits.

## Boundary

The profile is `PROPOSED_INACTIVE`, deterministic, no-network, and non-authoritative. A validator `PASS` means only that the declaration is closed under this schema, its profile hash replays, arrays are canonically ordered, proxy use is locally coherent with the declared evidence condition, and uncertainty/limitations are not hidden.

It does **not** resolve an `EvidenceBundle`, determine whether a proxy is scientifically fit, choose a planning scenario, quantify uncertainty, evaluate policy, approve review, authorize a decision, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the candidate except this field. |
| `planning_product_ref` / `planning_product_digest` | Pinned candidate-product identity; no reference resolution occurs. |
| `evidence_scope` | Evidence-scope reference and resolution state. |
| `assessment` | Declared evidence condition, proxy use, scenario use, completeness, and known undisclosed-limit count. |
| `proxy_sources` | Canonically ordered proxy or assumption declarations with target, fitness, assumptions, and limitations. |
| `uncertainty` | Declared class, quantification posture, method reference, and public disclosure surface. |
| `scenario_limitations` | Canonically ordered limitations that bound interpretation. |
| `authority_claims` | Fixed-false declaration preventing evidence, policy, review, decision, promotion, release, publication, or public-use authority. |

The profile stores references and bounded declarations only. It does not store raw source payloads, hidden model reasoning, precise sensitive locations, or planning decisions.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, ordering, proxy declaration, uncertainty disclosure, and local completeness invariants are coherent. |
| `ABSTAIN` | Evidence scope, data condition, completeness, proxy fitness, uncertainty, or decision-support suitability remains unresolved. |
| `DENY` | Identity, proxy requirement, limitation, disclosure, quantification, completeness, or overconfidence invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These outcomes are validator results only, not planning recommendations or release decisions.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, executable validation under `tools/`, conformance checks under `tests/`, CI orchestration under `.github/`, source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object belongs to the evidence family because it declares the support limits of an evidence-dependent planning product. It does not create a planning, policy, source, release, or publication authority home.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_planning_proxy_uncertainty_assessment -v
python tools/validators/evidence/validate_planning_proxy_uncertainty_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no source, evidence, planning product, policy, review, lifecycle, catalog, release, deployment, cache, or public artifact.
