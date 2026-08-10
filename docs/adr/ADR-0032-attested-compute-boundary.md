<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0032
title: Keep attested compute decision-gated and simulation-only by default
type: adr
version: v1
status: proposed
owners: ["Architecture steward", "Security steward", "Privacy steward", "Data steward"]
created: 2026-08-09
updated: 2026-08-09
policy_label: public
owning_root: docs/
responsibility: proposed cross-component architecture boundary for attested-compute necessity, simulation, and real-TEE deferral without runtime or release authority
truth_posture: CONFIRMED repository and governed-intake evidence / PROPOSED decision and finite routing outcomes / UNKNOWN need for real TEE / NEEDS VERIFICATION external standards, providers, threats, trust roots, and workloads
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md"
  - "docs/adr/ADR-0018-promotion-gate-sequence.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "docs/intake/exploratory/new-ideas-5-19-26-source-map.md"
  - "docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md"
tags: [adr, kfm, attestation, confidential-computing, privacy, security, governance]
supersedes: []
superseded_by: []
notes:
  - "PROPOSED: this record authorizes no real data, compute, credentials, cloud selection, trust-root enrollment, external verification, release, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

# ADR-0032: Keep attested compute decision-gated and simulation-only by default

KFM should remain in `NO_TRE` posture unless a named problem is shown not to be solvable by existing quarantine, policy, evidence, review, transformation, and release controls. If a later review establishes that gap, the only next step authorized by this proposed decision is a separately reviewed, no-data, no-network `SIMULATED_ASSESSMENT`; real trusted-execution-environment selection and execution remain deferred.

| Field | Value |
|---|---|
| **ID** | ADR-0032 |
| **Status** | proposed |
| **Date** | 2026-08-09 |
| **Deciders** | Architecture steward · Security steward · Privacy steward · Data steward |
| **Consulted** | Evidence · policy · source · legal/privacy · release · correction/rollback stewards |
| **Informed** | Connector · pipeline · infrastructure · governed-API · domain maintainers |
| **Supersedes** | — |
| **Superseded by** | — |
| **Directory Rules trigger** | `n/a — non-structural cross-component decision`; invariant-preserving boundary under §§3, 4, and 6 |
| **Primary responsibility root** | `docs/` |
| **Migration required** | no |
| **Rollback required** | yes, documentation-only |
| **Truth posture** | CONFIRMED repository boundary gap / PROPOSED decision / UNKNOWN real TEE need |

---

## 1. Context

The governed source map for *New Ideas 5-19-26* identifies attested compute-to-data as a decision candidate, not an implementation-ready capability. It finds adjacent quarantine, policy, sensitivity, receipt, review, promotion, release, correction, and rollback surfaces, but no repository-wide trusted-execution-environment runtime or real attestation authority. Its highest-confidence next action is a decision-only boundary packet before any implementation.

The motivating document combines consumer DNA, consent, provider access, confidential-computing concepts, attestation, and output review. These are distinct responsibilities. A successful runtime attestation can support a bounded execution claim; it cannot establish source admissibility, lawful purpose, consent validity, EvidenceBundle closure, disclosure safety, review approval, or public-release fitness.

### 1.1 Decision drivers

- **Prove necessity before adding machinery.** Existing deny-by-default and lifecycle controls may already solve the actual problem.
- **Keep attestation evidence bounded.** Runtime identity and measurement evidence must not be promoted into truth, rights, privacy, or release authority.
- **Avoid provider lock-in before a trust model exists.** Selecting a cloud, enclave, verifier, trust root, key service, or SDK would prematurely create operational and security commitments.
- **Preserve separation of duties.** Workload execution, policy evaluation, disclosure review, release approval, and publication cannot collapse into one attested step.
- **Keep experimentation harmless and reproducible.** A synthetic assessment can test object boundaries without processing data or contacting a verifier.

### 1.2 Evidence boundary

- **CONFIRMED:** the repository contains deny-by-default doctrine, quarantine and promotion gates, policy/evidence/review/release families, and a source map that classifies TRE as a decision candidate.
- **CONFIRMED:** no repository-wide real TEE runtime or attestation authority was found by the source-map review at its pinned main revision; this ADR does not extend that claim beyond that review.
- **PROPOSED:** use the finite outcomes in this record to route any future attested-compute proposal.
- **UNKNOWN:** whether a real KFM workload exists whose requirements cannot be met by current controls.
- **NEEDS VERIFICATION:** threat model, data owner, lawful purpose, trust roots, verifier portability, revocation, key rotation, egress controls, disclosure mechanism, and residual risk before any real design.

### 1.3 Out of scope

This ADR does not select a provider, TEE, cloud, cryptographic library, attestation format, trust root, key-management system, workload, dataset, privacy mechanism, or deployment path. It does not authorize source access, credentials, network calls, real compute, sensitive inputs, output release, or publication.

---

## 2. Decision

> **Decision:** Default every attested-compute proposal to `NO_TRE`. Permit a transition to a no-data, no-network `SIMULATED_ASSESSMENT` only after reviewers document a concrete control gap. Keep real TEE design at `DEFER_REAL_TEE`, and return `DENY_UNVERIFIED_ATTESTATION` whenever a claim relies on unresolved measurement, trust-root, verifier, revocation, or workload identity.

### 2.1 Finite decision outcomes

| Outcome | Meaning | Permitted effect |
|---|---|---|
| `NO_TRE` | Existing KFM controls address the named problem, or no unmet problem has been established. | Close or narrow the proposal; make no implementation change. |
| `SIMULATED_ASSESSMENT` | A specific gap is documented and a bounded object/transition exercise could reduce uncertainty. | Draft a separate contract, schema, synthetic fixtures, validator, tests, and authoring receipt; all authority effects remain false. |
| `DEFER_REAL_TEE` | Simulation may be useful, but evidence is insufficient to select or run a real TEE. | Record verification work; no provider, credential, key, trust root, network, or runtime activation. |
| `DENY_UNVERIFIED_ATTESTATION` | A proposal treats unverified or incomplete attestation as authority for data use, disclosure, release, or publication. | Fail closed with explicit reasons; do not process or release data. |

These outcomes are proposal-routing vocabulary. They do not replace the canonical policy or public-answer envelopes owned elsewhere.

### 2.2 Entry evidence for a simulated assessment

Before reviewers may select `SIMULATED_ASSESSMENT`, the proposal **MUST** identify:

1. one named KFM problem and affected responsibility owners;
2. the existing controls considered and the precise residual gap;
3. the claim a runtime attestation could and could not support;
4. fixed-false authority effects for data access, execution, approval, release, deployment, and publication;
5. a no-data, no-network synthetic fixture plan; and
6. correction and rollback behavior if an attestation claim or verifier profile is later invalidated.

### 2.3 Required separation

Any later assessment **MUST** keep these objects or decisions distinct:

- workload identity and version;
- input identity, authority, rights, consent, and sensitivity;
- attestation evidence and verifier profile;
- execution/process receipt;
- policy obligations and decision;
- output transformation and disclosure review;
- evidence support and reviewer decision;
- release approval, correction, withdrawal, and rollback.

No attestation result may fill missing authority in another lane.

### 2.4 Placement basis

| Question | Answer |
|---|---|
| **Primary responsibility** | Cross-component architecture decision and authority boundary |
| **Owning root** | `docs/adr/` |
| **Domain segment** | `n/a — cross-domain`, with heightened People/DNA sensitivity relevance |
| **Lifecycle phase** | `n/a`; no data object is created by this record |
| **Directory Rules basis** | §§3, 4, and 6: preserve lifecycle, responsibility roots, governed interfaces, and policy-aware defaults |
| **Parallel authority risk** | Mitigated by forbidding this ADR and any simulation from replacing contracts, schemas, policy, evidence, receipts, or release objects |

### 2.5 Conformance language

- **MUST** default to `NO_TRE` until a concrete residual gap is evidenced.
- **MUST NOT** use attestation as proof of source rights, consent, truth, evidence sufficiency, disclosure safety, review, or release.
- **MUST NOT** select or contact a real provider or verifier under this decision.
- **SHOULD** prefer existing quarantine, transformation, policy, review, and release controls where they meet the need.
- **MAY** propose a separately reviewed synthetic assessment only with all entry evidence above.

---

## 3. Consequences

### 3.1 Positive

- Avoids premature infrastructure, credential, trust-root, and provider commitments.
- Makes the burden of proof for confidential-computing complexity explicit.
- Keeps runtime evidence subordinate to source, evidence, policy, privacy, review, and release governance.
- Provides a safe next step if an actual gap is established.

### 3.2 Negative

- KFM gains no immediate confidential-computing capability.
- A potentially useful real workload remains blocked until multiple owners supply evidence and accept the design.
- The finite outcomes add vocabulary that must stay confined to this proposal-routing boundary.

### 3.3 Accepted tradeoffs

The project accepts slower adoption of attested compute in exchange for clearer authority, reduced sensitive-data risk, portability, and reversible change. Simulation can test the boundary, but it cannot stand in for a real security or privacy evaluation.

### 3.4 Affected surfaces

| Surface | Impact |
|---|---|
| ADRs | Adds this proposed, non-binding decision record and index row. |
| Contracts, schemas, policy | Not changed; any simulated profile requires a separate reviewed PR. |
| Fixtures, tests, tools | Not changed; no simulation is authorized by file presence alone. |
| Data and registries | Not changed; no source, dataset, trust root, or provider is admitted. |
| Infrastructure and runtime | Not changed; no service, credential, network, verifier, or execution path is created. |
| Release and public clients | Not changed; all release, deployment, and publication effects remain false. |

---

## 4. Alternatives considered

### 4.1 Select a real TEE provider now

- **Summary:** Choose a cloud or enclave technology and build a proof of concept.
- **Why rejected:** No accepted workload, threat model, data authority, trust-root model, verifier profile, or disclosure plan establishes the need or makes provider selection responsible.

### 4.2 Treat attestation as an extension of the generic run receipt

- **Summary:** Add measurements to an existing execution receipt and infer a broader trusted result.
- **Why rejected:** A process receipt and attestation evidence cannot acquire policy, privacy, evidence, review, or release authority. This would hide the unresolved trust and revocation model.

### 4.3 Implement differential privacy inside a TEE

- **Summary:** Combine attested execution with a fixed privacy mechanism or budget.
- **Why rejected:** Attestation and statistical disclosure control answer different questions. Dataset adjacency, composition, budget ownership, utility, and residual disclosure risk remain undefined.

### 4.4 Status quo without an explicit decision boundary

- **Summary:** Leave the idea only in exploratory intake.
- **Why rejected:** The source contains implementation-shaped guidance. An explicit proposed boundary prevents that material from being mistaken for authority while preserving a reversible evaluation path.

---

## 5. Evidence and references

- `docs/intake/exploratory/new-ideas-5-19-26-source-map.md` — complete-source triage, repository overlap, TRE decision candidate, and recommended bounded action.
- `docs/doctrine/directory-rules.md` — responsibility roots, lifecycle law, governed interfaces, policy-aware defaults, evidence, and reversible change.
- `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` — accepted directory-governance authority.
- `docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md` — proposed sensitive-domain boundary; file presence is not acceptance.
- `docs/adr/ADR-0018-promotion-gate-sequence.md` — proposed gate ordering and unresolved attestation trust-root work; file presence is not acceptance.
- `docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md` — human/DNA sensitivity and scope boundary.

No external TEE, attestation, cryptographic, privacy, legal, provider, or benchmark claim is adopted by this ADR. Those facts remain `NEEDS VERIFICATION` against primary authority if a real design is later proposed.

---

## 6. Migration plan

Not applicable — this is a non-structural proposed decision. It moves no files, creates no compatibility surface, changes no schema home, and activates no runtime. If accepted, subsequent implementation remains a separate decision and change set.

---

## 7. Rollback plan

Before merge, close the draft pull request and delete only its branch if desired. After merge, reject or supersede the ADR through normal ADR governance and update `docs/adr/INDEX.md` in the same reviewed change. No data, runtime state, credential, or release artifact requires rollback because this record creates none.

---

## 8. Open questions

- Which named KFM problem, if any, cannot be addressed with current quarantine, transformation, access-control, policy, review, and release surfaces?
- Who owns the threat model and the decision that confidential computing is proportionate to that problem?
- What portable evidence model could represent measurement, endorsement, verifier, trust-root, freshness, and revocation without binding KFM to one provider?
- What disclosure review remains necessary after a workload executes as attested?
- What correction and rollback obligations apply when a measurement, trust root, verifier, or workload is later compromised or revoked?

---

## 9. Change history

| Date | Status | Change | PR |
|---|---|---|---|
| 2026-08-09 | proposed | Initial decision-only boundary mined from the governed *New Ideas 5-19-26* source map. | pending |
