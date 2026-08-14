<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0032-attested-compute-boundary
title: "ADR-0032 — Keep Attested Compute Decision-Gated and Simulation-Only by Default"
type: adr
adr_id: ADR-0032
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — security and confidential-computing steward"
  - "NEEDS VERIFICATION — privacy, consent, and disclosure-control steward"
  - "NEEDS VERIFICATION — data, evidence, policy, and release stewards"
owner_status: "CODEOWNERS supplies a repository review route; accepted stewardship, threat-model authority, independent review, real-workload approval, and release authority remain unverified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Security and confidential-computing steward
  - Privacy, consent, and disclosure-control steward
  - Data, evidence, and source steward
  - Policy steward
  - Contracts and schemas stewards
  - Validation and CI steward
  - Release, correction, and rollback steward
created: 2026-08-09
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Record the proposed necessity gate that keeps attested-compute work synthetic-only and non-authoritative until a separately reviewed real-workload decision closes threat, authority, verifier, disclosure, release, correction, and rollback obligations."
current_path: docs/adr/ADR-0032-attested-compute-boundary.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b7352aba93f7298bdd5a6ee6fd8de475b05c9e42
  target_prior_blob: dd4bbdff5f5c7c5ae62d46221267b58218f29d27
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_readme_blob: 793015c38f4066c2c23753d4e3dd26bcc890279d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  source_map_blob: 30f3b6aec046cadc0df87e41e028adfe5ceb5855
  assessment_contract_blob: ed4d5046f2eab11b8aec03c6428536fdfc91607a
  assessment_schema_blob: 418de89ae02fed1a5f1a2b0b410054a794c225dc
  assessment_fixture_blob: 3283af5189a38bcc7cdbdb6f846f21f9fd7a6967
  assessment_validator_blob: 6f0299c13971ad7b20e093291647ded66b82abcb
  assessment_tests_blob: 7b4717a6e87add0f7d44148417eceea0b81c45f7
  assessment_workflow_blob: c4a528a7f3146d9b2ff4ebc5e0c3610de06c8a55
  assessment_receipt_blob: 034e6ed79a728f7c04a67ee51c4d6af13d2d7da2
  implementation_pr: 2519
  implementation_merge: 1bb91ae8de2313dbebfe84fc5d986df64f0d7169
  last_observed_green_run: 31455932316
  latest_observed_profile_run: 31654971857
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/intake/exploratory/new-ideas-5-19-26-attested-compute-boundary-source-map.md
  - contracts/governance/attested_compute_boundary_assessment.md
  - schemas/contracts/v1/governance/attested_compute_boundary_assessment.schema.json
  - fixtures/contracts/v1/governance/attested_compute_boundary_assessment/cases.json
  - tools/validators/governance/validate_attested_compute_boundary_assessment.py
  - tests/validators/governance/test_validate_attested_compute_boundary_assessment.py
  - .github/workflows/attested-compute-boundary-assessment.yml
  - data/receipts/generated/genrec-new-ideas-5-19-26-attested-compute-boundary-20260810.json
tags: [kfm, adr, attestation, confidential-computing, tre, tee, simulation-only, no-network, privacy, security, governance, fail-closed]
notes:
  - "v1.1 is a same-path repository-evidence reconciliation. It preserves source and effective status proposed and grants no compute or release authority."
  - "ADR-0029 separately accepted Directory Rules v2, confirming docs/adr/ placement without accepting ADR-0032."
  - "A proposed-inactive assessment packet now implements the bounded routing vocabulary with a closed schema, 18 exact fixtures, deterministic validator, 10 focused tests, read-only CI, and an authoring receipt."
  - "The latest observed profile run passed functional validation and failed only historical receipt byte closure after PR #2657 changed the workflow installation command."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0032 — Keep Attested Compute Decision-Gated and Simulation-Only by Default

> **Proposed decision.** Default attested-compute proposals to `NO_TRE` until a named residual control gap is demonstrated. Permit only a separately reviewed, no-data, no-network `SIMULATED_ASSESSMENT`. Keep real trusted-execution-environment work at `DEFER_REAL_TEE`; unresolved external attestation is `DENY_UNVERIFIED_ATTESTATION`.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Bounded profile: implemented](https://img.shields.io/badge/bounded%20profile-implemented-0969da?style=flat-square)](#bounded-profile)
[![Real TEE: deferred](https://img.shields.io/badge/real%20TEE-DEFERRED-b42318?style=flat-square)](#real-tee-gates)
[![Receipt closure: hold](https://img.shields.io/badge/receipt%20closure-HOLD-b42318?style=flat-square)](#workflow-evidence)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-boundary)

> [!IMPORTANT]
> **Decision status, bounded implementation, and operational authority are separate.** ADR-0032 remains `proposed`. A validator `PASS`, workflow result, receipt, merge, or this documentation update cannot accept the ADR or authorize compute.

> [!CAUTION]
> **`SIMULATED_ASSESSMENT` is declaration review—not simulated confidential computing.** The profile performs no compute, verifies no external attestation, resolves no references, authenticates no workload, and processes no real or sensitive input.

> [!WARNING]
> **Attestation cannot supply missing authority.** Runtime measurement cannot establish source admissibility, lawful purpose, consent, evidence sufficiency, disclosure safety, reviewer approval, release fitness, or publication authority.

**Quick navigation:** [Status](#status) · [Evidence](#evidence) · [Decision](#decision) · [Profile](#bounded-profile) · [Authority](#authority-boundary) · [Gates](#current-gates) · [Real TEE](#real-tee-gates) · [Risks](#risks) · [Rollback](#migration-and-rollback) · [Verification](#verification) · [References](#references)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0032` — unique in [`INDEX.md`](./INDEX.md) |
| **Source / effective status** | `proposed` / `proposed` |
| **Record edition** | `v1.1` — evidence reconciliation; decision unchanged |
| **Decision class** | Cross-component necessity, trust, privacy, and release boundary |
| **Current implementation posture** | Proposed-inactive, fixture-only decision profile implemented; no real TEE runtime |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

ADR acceptance would approve the boundary. Real TEE admission would remain a later, separately reviewed decision with its own implementation and release evidence.

<a id="evidence"></a>

## Evidence Boundary

**CONFIRMED at the pinned snapshot:** accepted ADR-0029 governs placement; the ADR index keeps ADR-0032 proposed; PR #2519 added the bounded assessment contract, schema, fixtures, validator, tests, workflow, source map, and receipt. The schema fixes all data, credential, provider/TEE, key, external-verification, compute, release, deployment, and publication effects false.

**UNKNOWN:** whether KFM has a real workload whose residual problem cannot be solved by quarantine, access control, transformation, policy, evidence, review, and release controls.

**NEEDS VERIFICATION before real design:** workload and data owners, lawful purpose, rights and consent, threat model, alternatives and proportionality, verifier/trust-root model, freshness and replay, revocation and compromise, key lifecycle, input/egress controls, side channels, disclosure review, incident response, dependent-output invalidation, and release/rollback ownership.

### Evidence maturity

| Level | Current posture |
|---|---|
| Proposed decision identity and placement | **CONFIRMED** |
| Synthetic declaration contract and closed machine shape | **CONFIRMED present; proposed-inactive** |
| Deterministic fixture validation | **CONFIRMED bounded implementation** |
| External attestation verification | **ABSENT / denied by v1 profile** |
| Real workload, data, provider, key, verifier, or TEE runtime | **UNKNOWN / not authorized** |
| Release or public operation | **NONE** |

---

<a id="decision"></a>

## Decision

| Posture | Derived condition | Local validator result | Authority effect |
|---|---|---|---|
| `NO_TRE` | Existing controls were reviewed and no residual problem remains | `PASS` | Close or narrow proposal only |
| `SIMULATED_ASSESSMENT` | Named residual gap, reviewed controls, complete synthetic declarations, and pinned no-data/no-network plan | `PASS` | Continue human review only |
| `DEFER_REAL_TEE` | Problem, controls, declarations, or real-TEE request remain unresolved | `ABSTAIN` | Record verification work only |
| `DENY_UNVERIFIED_ATTESTATION` | An unresolved external attestation claim is asserted | `DENY` | Fail closed |
| Assessment or schema failure | Input is invalid or assessment state is erroneous | `ERROR` | Remediate; no fallback allow |

These are governance-profile outcomes, not `PolicyDecision`, `RuntimeResponseEnvelope`, `PromotionDecision`, `ReviewRecord`, or release outcomes.

### Conformance

- **MUST** default to `NO_TRE` until a residual control gap is evidenced.
- **MUST NOT** treat attestation as source, rights, purpose, consent, truth, privacy, review, release, or publication authority.
- **MUST NOT** select or contact a provider, verifier, trust root, key service, or real TEE under this decision.
- **MUST NOT** process real or sensitive data under the bounded profile.
- **MAY** review synthetic declarations only after all entry conditions are satisfied.

---

<a id="bounded-profile"></a>

## Bounded Profile

`AttestedComputeBoundaryAssessmentCandidate` separates ten responsibility seams: workload identity; input authority; attestation evidence; execution receipt; policy obligations; disclosure review; output transformation; evidence/reviewer decision; release approval; and rollback. Local `RESOLVED` means declaration completeness only—not authentication or approval.

The packet includes a semantic contract, closed Draft 2020-12 schema, 18 exact fixtures, deterministic validator, 10 focused tests, read-only workflow, source map, and generated authoring receipt. It performs no external verification or runtime execution.

> [!NOTE]
> The schema requires ten seams. One companion contract sentence and the workflow summary still say “eight.” This ADR records that wording drift; it does not silently rewrite companion artifacts or their historical receipt.

<a id="workflow-evidence"></a>

### Workflow Evidence

- Run `31455932316` was fully green after PR #2519 merged.
- Run `31654971857` again passed compilation, all 10 focused tests, and all 18 exact fixtures.
- That later run failed only generated-receipt byte replay because PR #2657 changed the workflow dependency-install command without rebinding the historical receipt.

**Classification:** profile logic is not shown failing; current byte-binding closure is `HOLD` until the receipt is legitimately rebound and hosted validation is green.

---

<a id="authority-boundary"></a>

## Authority Boundary

A profile `PASS` proves only local declaration coherence for the checked revision. It does not prove necessity, authenticity, confidentiality, side-channel resistance, privacy, lawful use, evidence closure, disclosure safety, reviewer approval, release fitness, or public safety.

The owning root remains `docs/adr/` because this file records a human architecture decision. Contracts own meaning, schemas own shape, fixtures/tests/validators own bounded conformance, workflows own read-only orchestration, and receipts own authoring accountability. No TEE, key, verifier, runtime, data, policy, release, or publication root is created.

---

<a id="current-gates"></a>

## Current Gates

| Gate | State |
|---|---|
| ADR identity and Directory Rules placement | `PASS` |
| ADR acceptance and accountable named owners | `HOLD` |
| Bounded profile shape, fixtures, validator, and tests | `PASS` at observed heads |
| Generated-receipt exact byte closure | `HOLD` |
| Real workload necessity and threat model | `UNKNOWN` |
| Provider, verifier, trust root, key, and external attestation | `DENY` under v1 profile |
| Real/sensitive input and compute | `DENY` |
| Release, deployment, publication, and public use | `DENY` |

Before proposed becomes accepted, reviewers must approve the `NO_TRE` default, finite routing, ten-seam separation, unsupported-authority list, invalidation/rollback rule, and explicit non-effects without claiming operational TEE maturity.

<a id="real-tee-gates"></a>

## Real TEE Admission Gates

A later real design requires a new decision packet—not incremental drift from the fixture profile. At minimum it must close:

1. named workload, data owner, lawful purpose, rights/consent, and residual problem;
2. threat model, alternatives, proportionality, accepted risks, and domain sensitivity review;
3. provider-neutral workload, measurement, endorsement, verifier, trust-root, freshness, replay, revocation, portability, and compromise model;
4. credentials, key lifecycle, input, network, egress, output, disclosure, logging, and side-channel controls;
5. execution receipts separated from policy, evidence/review, release, correction, withdrawal, and rollback;
6. synthetic negative fixtures, no-secret CI, verifier-failure tests, rollback drills, and incident response; and
7. governed release and dependent-output invalidation evidence.

Until then, use `DEFER_REAL_TEE` or `DENY_UNVERIFIED_ATTESTATION`.

---

<a id="risks"></a>

## Risks and Alternatives

| Risk / alternative | Disposition |
|---|---|
| Attestation overclaim | Deny; enumerate unsupported authorities |
| Provider lock-in | Defer selection until a portable trust model exists |
| Synthetic profile mistaken for security proof | Preserve fixed-false non-effects and explicit wording |
| Sensitive fixtures or logs | Synthetic-only; no identifiers, payloads, coordinates, or secrets |
| Revocation/freshness failure | Fail closed and invalidate dependents |
| Select a provider now | Rejected: no accepted workload or trust model |
| Extend a generic run receipt | Rejected: receipts cannot acquire privacy or release authority |
| Permanently forbid evaluation | Rejected: a real evidenced gap may justify a later decision |

---

<a id="migration-and-rollback"></a>

## Migration and Rollback

This update modifies one ADR in place. It changes no status, index row, contract, schema, fixture, validator, workflow, receipt, runtime, data, or release surface.

Before merge, close the draft pull request and abandon its branch. After a docs-only merge, revert the documentation commit. The PR #2519 packet is separate and requires its own reviewed revert or supersession. No operational TEE, credential, sensitive-data copy, release, deployment, or public artifact exists to unwind.

---

<a id="verification"></a>

## Verification

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
python -m unittest tests.validators.governance.test_validate_attested_compute_boundary_assessment --verbose
python tools/validators/governance/validate_attested_compute_boundary_assessment.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-new-ideas-5-19-26-attested-compute-boundary-20260810.json \
  --repo-root .
```

Expected bounded evidence: one proposed ADR identity; all four postures covered; 10 focused tests; 18 exact cases; deterministic identity; no network; fixed-false authority effects. Receipt replay remains expected to fail until exact workflow bytes are legitimately rebound.

---

<a id="references"></a>

## References

- [`docs/adr/README.md`](./README.md) and [`docs/adr/INDEX.md`](./INDEX.md)
- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../doctrine/directory-rules.md)
- [`ADR-0010`](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md), [`ADR-0018`](./ADR-0018-promotion-gate-sequence.md), and [`ADR-0024`](./ADR-0024-steward-separation-of-duties-for-release.md)
- [Attested-compute source map](../intake/exploratory/new-ideas-5-19-26-attested-compute-boundary-source-map.md)
- [Contract](../../contracts/governance/attested_compute_boundary_assessment.md), [schema](../../schemas/contracts/v1/governance/attested_compute_boundary_assessment.schema.json), [fixtures](../../fixtures/contracts/v1/governance/attested_compute_boundary_assessment/cases.json), [validator](../../tools/validators/governance/validate_attested_compute_boundary_assessment.py), [tests](../../tests/validators/governance/test_validate_attested_compute_boundary_assessment.py), [workflow](../../.github/workflows/attested-compute-boundary-assessment.yml), and [receipt](../../data/receipts/generated/genrec-new-ideas-5-19-26-attested-compute-boundary-20260810.json)

No external TEE, cryptographic, privacy, legal, provider, benchmark, or standards claim is adopted here. Those remain `NEEDS VERIFICATION` against primary authority if a real design is proposed.

## Change History

| Date | Edition / status | Change | PR |
|---|---|---|---|
| 2026-08-09 | `v1` / proposed | Initial decision-only boundary | #2408 |
| 2026-08-14 | `v1.1` / proposed | Reconciles bounded implementation, hosted evidence, receipt and wording drift, gates, risks, verification, and rollback without granting authority | pending |

[Back to top](#top)
