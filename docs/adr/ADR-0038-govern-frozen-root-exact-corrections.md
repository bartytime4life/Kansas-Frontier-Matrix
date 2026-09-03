<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0038
title: Govern Frozen-Root Exact Corrections Through Trusted-Base Records
type: adr
version: v1.0
status: accepted
owners: ["@bartytime4life"]
created: 2026-09-02
updated: 2026-09-02
policy_label: public
owning_root: "docs/"
responsibility: "Accept one bounded, fail-closed mechanism for an exact correction of a damaged containment document beneath a frozen compatibility root without weakening the repository-topology ratchet."
truth_posture: "CONFIRMED repository evidence / ACCEPTED bounded decision / STAGE_1_INERT implementation / STAGE_2_NOT_IMPLEMENTED"
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "docs/adr/INDEX.md"
  - "control_plane/root_registry.yaml"
  - "control_plane/repository_topology_correction_register.yaml"
  - "contracts/governance/repository_topology_correction_register.md"
  - "schemas/contracts/v1/governance/repository_topology_correction_register.schema.json"
  - "tools/validators/directory_governance/validate_repository_topology.py"
  - "tools/validators/directory_governance/repository_topology_baseline.json"
  - "tools/validators/directory_governance/validate_repository_topology_correction_register.py"
  - "tests/validators/directory_governance/test_validate_repository_topology_correction_register.py"
tags: [adr, kfm, directory-governance, topology, correction, trusted-base, fail-closed, compatibility]
supersedes: []
superseded_by: []
notes:
  - "Accepted by explicit project-owner continuation recorded in issue #4228 comment 5518331532; this is a transparent single-owner bootstrap decision and not independent review."
  - "This decision does not supersede ADR-0029 or reclassify catalog/."
  - "Stage 1 is deliberately inert: it adds no topology-validator consumer and performs no baseline replacement."
  - "Stage 2 requires a trusted base that already contains this accepted decision and a byte-identical correction register."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0038: Govern Frozen-Root Exact Corrections Through Trusted-Base Records

> **Decision.** Accept a two-stage, trusted-base exact-transition mechanism for one reviewed correction beneath the frozen `catalog/` compatibility root. Stage 1 records the decision and an inert machine projection. Stage 2 may later consume only trusted-base bytes and permit only the exact registered baseline transition. The live topology finding remains visible and fail-closed until Stage 2 is separately implemented and validated.

| Field | Value |
|---|---|
| **ID** | `ADR-0038` |
| **Status** | `accepted` |
| **Date** | 2026-09-02 |
| **Decision authority** | `@bartytime4life`, explicit project-owner continuation in issue `#4228`, comment `5518331532` |
| **Independent review** | `NEEDS VERIFICATION`; no independent reviewer is claimed |
| **Evidence checkpoint** | `main@df45bbaea90c210ec485dd85562a314ed0c9ccf4` |
| **Governing decision retained** | `ADR-0029` |
| **Affected topology identity** | `KFM-TOPO-004` / `catalog/` |
| **Stage 1** | Accepted decision, inert projection, contract, schema, fixtures, validator, and tests |
| **Stage 2** | `NOT IMPLEMENTED`; trusted-base consumption and exact baseline replacement only |
| **Release/publication effect** | none |
| **Rollback posture** | revoke recognition and fail closed; never restore the damaged blob automatically |

> [!IMPORTANT]
> Acceptance becomes effective only when this ADR and the canonical ADR index merge together with `status: accepted`. This branch packet is reviewable implementation evidence, not default-branch authority. Stage 1 must not modify the topology baseline, the topology validator's transition logic, or any file beneath `catalog/`.

**Quick navigation:** [Context](#1-context) · [Decision](#2-decision) · [Exact transition](#3-exact-transition) · [Stage separation](#4-stage-separation) · [Stage 2 algorithm](#5-stage-2-acceptance-algorithm) · [Alternatives](#6-alternatives-considered) · [Consequences](#7-consequences) · [Validation](#8-validation-and-negative-proof) · [Rollback](#9-rollback-and-retirement) · [Open verification](#10-open-verification) · [History](#11-change-history)

## 1. Context

Accepted ADR-0029 classifies `catalog/` as a deprecated, immutable, `frozen_no_writes`, `redirect_only` compatibility root whose canonical target is `data/catalog/`. The repository-topology ratchet binds every tracked path and Git object ID beneath that root, so an unreviewed same-path edit changes the `KFM-TOPO-004` fingerprint.

PR `#4209` repaired literal merge-conflict boundaries in `catalog/domain/agriculture/README.md`. The clean redirect-only correction is now on `main`, but the topology baseline still binds the damaged blob. The evidence set retains 43 paths; exactly one member changed. The current transition validator accepts only waiver removal or identity-preserving strict evidence shrinkage, so it correctly rejects this equal-cardinality replacement.

Reverting the Agriculture README would restore known-bad conflict markers. Deleting the redirect is not authorized because producer, consumer, link, and retirement closure remain unresolved. Silently refreshing the baseline or weakening `KFM-TOPO-004` would turn a specific correction into broad write authority.

The problem is therefore not whether the corrected content should remain. It is how a frozen-root correction can be represented without allowing the current change to authorize itself.

### 1.1 Governing constraints

This decision preserves all of the following:

- `catalog/` remains deprecated, immutable, `frozen_no_writes`, and `redirect_only`;
- `data/catalog/` remains the canonical target;
- `KFM-TOPO-004` continues to observe `path@object_id` evidence;
- the topology baseline remains an implementation-waiver artifact;
- new paths, deleted paths, additional changed members, payload growth, and unregistered same-path edits fail closed;
- a current branch cannot introduce or modify the record that authorizes itself;
- no correction record grants catalog, evidence, policy, review, release, deployment, or publication authority;
- rollback returns enforcement to fail closed and does not recreate the damaged content.

### 1.2 Out of scope

This ADR does not:

- amend the adopted Directory Rules bytes;
- supersede ADR-0029;
- authorize general maintenance under frozen roots;
- permit a current-only correction entry to authorize its own branch;
- modify `catalog/`;
- replace the topology baseline;
- wire the correction register into `validate_repository_topology.py`;
- approve a pull request, merge, release, deploy, promote, publish, or change repository settings;
- resolve issue `#4024` or prove a safe draft-delivery path.

## 2. Decision

Adopt a two-stage mechanism with one narrow machine projection at:

`control_plane/repository_topology_correction_register.yaml`

The register is a projection of accepted decision evidence. It is not a policy engine, topology baseline, migration manifest, release record, or independent authority.

### 2.1 Stage 1 decision packet

Stage 1 may contain only:

1. this accepted ADR and the synchronized canonical ADR index;
2. the inert root-level correction register;
3. a semantic contract;
4. a machine-checkable schema;
5. a register-shape and decision-binding validator;
6. deterministic valid and invalid fixtures;
7. focused tests and directly necessary explanatory documentation.

Stage 1 must declare:

- `implementation_status: INERT_STAGE1`;
- `consumer_status: NONE`;
- the correction entry as `ACCEPTED` and `UNCONSUMED`;
- an exact constant-shape version for the single reviewed transition;
- explicit non-effects and rollback semantics.

Stage 1 must not:

- import the correction register into `validate_repository_topology.py`;
- modify `repository_topology_baseline.json`;
- modify any file beneath `catalog/`;
- suppress a live finding;
- authorize reuse;
- open or mark a pull request ready, merge, release, deploy, promote, or publish.

### 2.2 Stage 2 delivery

Stage 2 is a separate implementation change. It may begin only after Stage 1 is part of the trusted base used by the change.

Stage 2 may only:

- load the register and ADR from the trusted base;
- require the current register to be byte-identical to the trusted-base register;
- consume exactly one accepted and unconsumed entry;
- permit only the exact baseline-entry replacement defined in section 3;
- preserve every unregistered transition as a failure;
- preserve the existing strict-shrink path for genuine monotonic closure;
- add the positive and negative proof in section 8.

Stage 2 must not:

- treat a current-branch record as authority;
- change the `Finding` fingerprint model;
- add a generic equal-cardinality replacement rule;
- skip any remaining baseline addition, removal, expiry, or protected-metadata check;
- modify `catalog/`;
- authorize a second correction without a new accepted decision.

## 3. Exact transition boundary

The only transition accepted by this decision is:

| Field | Exact value |
|---|---|
| `correction_id` | `KFM-TOPO-004-CORR-4228-01` |
| `rule_id` | `KFM-TOPO-004` |
| `subject` | `catalog/` |
| `path` | `catalog/domain/agriculture/README.md` |
| Prior fingerprint | `sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006` |
| Current fingerprint | `sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f` |
| Prior blob | `bf1a333573c6d068fbb0b695356346003842aceb` |
| Current blob | `4be1711bfa011636ac1c5cd13e7c98e5002ff9c0` |
| Prior/current member count | `43 / 43` |
| Exact removal | `catalog/domain/agriculture/README.md@bf1a333573c6d068fbb0b695356346003842aceb` |
| Exact addition | `catalog/domain/agriculture/README.md@4be1711bfa011636ac1c5cd13e7c98e5002ff9c0` |
| Reason | `committed_merge_conflict_boundary_repair` |
| Reuse | `FORBIDDEN` |
| Consumption | once, from a trusted base only |
| Rollback | revoke recognition and return to fail closed; do not restore the prior blob |

The named path, blobs, fingerprints, counts, and delta are constants in the v1 schema. Introducing a second correction requires a new accepted decision and a versioned schema/register change.

## 4. Stage separation

### 4.1 Why the register is inert in Stage 1

A change cannot import a decision record that it introduces and then use that record to permit the same change. That collapses decision and execution.

The Stage 1 register is therefore intentionally unused by `validate_repository_topology.py`. Its validator verifies that the consumer path is absent. This creates a reviewable trusted-base boundary for Stage 2.

### 4.2 Trusted-base rules

Stage 2 must:

1. resolve the trusted base using the existing pull-request or push trusted-ref input;
2. load the ADR and correction register from that exact commit;
3. reject a missing or unresolved trusted base;
4. reject any current-register byte difference;
5. reject an ADR or register that exists only on the current branch;
6. reject a decision-blob mismatch;
7. keep trusted-ref values out of public diagnostic output.

### 4.3 Baseline authority remains unchanged

The baseline continues to record only implementation waivers. It does not authorize corrections. Stage 2 may transform one baseline entry only because an accepted trusted-base decision separately authorizes that exact transition.

## 5. Stage 2 acceptance algorithm

For the one otherwise unresolved same-identity removal-plus-addition:

1. Find the stale baseline entry for `KFM-TOPO-004` / `catalog/`.
2. Find the current live finding with the same identity.
3. Confirm the stale and live fingerprints exactly match this ADR.
4. Load the trusted-base register and accepted ADR.
5. Require current and trusted register bytes to match exactly.
6. Require one and only one matching `ACCEPTED` and `UNCONSUMED` entry.
7. Require `consume_once: true`.
8. Require the same path set and `43 -> 43` evidence count.
9. Require the exact one-member removal and one-member addition in section 3.
10. Require no second changed member and no path addition or deletion.
11. Replace only the stale baseline entry with the serialized current finding.
12. Apply the existing transition checks to every remaining baseline addition, removal, mutation, expiry, and protected metadata field.
13. Fail closed on any mismatch or ambiguity.

The algorithm must be deterministic, no-network, bounded, and independent of wall-clock acceptance.

## 6. Alternatives considered

| Option | Benefit | Rejection reason |
|---|---|---|
| Hard-code the path/blob pair in validator code | Exact | Makes executable code the practical decision authority and has poor retirement semantics |
| Let the baseline directly authorize replacements | One artifact | Broadens a waiver artifact into correction authority and enables silent refresh |
| Use prose or `PathDecisionRecord` only | Strong rationale | Cannot deterministically bind the transition consumed by the validator |
| Supersede ADR-0029 | Strong human authority | Reopens root classification unnecessarily |
| Revert the Agriculture README | Restores old fingerprint | Reintroduces literal merge-conflict markers |
| Delete the redirect | Removes mutable member | Consumer and retirement closure are not established |
| Trusted-base accepted decision plus inert projection | Exact, auditable, one-use, fail-closed | **Selected** |

## 7. Consequences

### 7.1 Positive

- The damaged content remains repaired.
- The ratchet does not gain generic same-path replacement authority.
- Decision and implementation occur on separate trusted bases.
- The exact old/new evidence is inspectable and testable.
- Future reuse is forbidden.
- A revoked or missing decision returns the system to fail closed.
- Stage 2 can close the current repository-integrity blocker without weakening unrelated topology rules.

### 7.2 Costs

- Two reviewed stages are required.
- The correction record and tests add maintenance surface.
- The current topology check remains red until Stage 2 is completed.
- A future correction requires a new accepted decision; this v1 record is deliberately not reusable.

### 7.3 Risks and controls

| Risk | Control |
|---|---|
| Current change authorizes itself | Trusted-base-only load plus byte-identical current register |
| Register becomes a generic waiver list | Schema v1 permits exactly one correction identity |
| Baseline authority expands | Contract and tests preserve implementation-waiver-only semantics |
| Damaged blob restored during rollback | Automatic restore is explicitly prohibited |
| Entry reused | `consume_once`, source-fingerprint absence, and `reuse: FORBIDDEN` |
| Second member changes | Exact symmetric-difference and member-count checks |
| Network-dependent acceptance | No remote lookup; trusted Git bytes only |
| Release/publication inference | Explicit non-effects in ADR, register, schema, and diagnostics |

## 8. Validation and negative proof

### 8.1 Stage 1 checks

Stage 1 must prove:

- the register is deterministic canonical JSON-compatible YAML;
- the schema is valid Draft 2020-12;
- the accepted entry exactly matches section 3;
- the ADR Git blob matches the register binding;
- duplicate keys and non-finite values fail;
- non-effects are exact and canonically ordered;
- only one correction ID exists;
- `validate_repository_topology.py` does not consume the register;
- the topology baseline is not changed by the Stage 1 branch;
- all focused valid and invalid fixtures produce stable results.

### 8.2 Required negative fixtures

The proof packet must reject:

- wrong old blob;
- wrong new fingerprint;
- a second changed evidence member;
- path-set or cardinality change;
- proposed or revoked entry status;
- enabled consumer during Stage 1;
- reusable entry;
- rollback that restores the damaged blob;
- wrong decision blob;
- extra fields or duplicate keys;
- noncanonical arrays or serialization.

### 8.3 Stage 2 checks

Stage 2 must add negative proof for:

- no trusted-base entry;
- entry present only in the current change;
- current register differing from trusted base;
- duplicate or ambiguous match;
- wrong rule, subject, path, fingerprint, blob, or counts;
- attempted reuse after the source fingerprint is absent;
- any residual baseline transition not accepted by the existing rules.

## 9. Rollback and retirement

Rollback means:

1. remove or revoke Stage 2 recognition of the correction;
2. restore the topology transition to fail closed;
3. retain the clean Agriculture README unless a separately governed correction changes it;
4. preserve this ADR and register lineage;
5. record why recognition was revoked.

Rollback does **not** mean restoring blob `bf1a333573c6d068fbb0b695356346003842aceb`.

The entry is naturally one-use because it cannot match after the source fingerprint is absent. It may be marked consumed or retired only in a later reviewed change after the baseline contains the live fingerprint and no pending consumer depends on the unconsumed state.

## 10. Open verification

- Independent review and separation of duties remain unavailable and must not be inferred.
- Stage 2 consumer code and baseline replacement are not implemented.
- Exact-current-main topology remains expected to fail until Stage 2.
- Issue `#4024` still governs the unsafe intended-draft delivery path.
- The `control_plane/` root README direct-child inventory requires a focused refresh before pull-request delivery.
- A separately proven one-shot draft creator is required before pull-request delivery.
- Required-check and ruleset hardening remains a separate P0 governance operation.

## 11. Change history

| Date | Version | Change |
|---|---|---|
| 2026-09-02 | v1.0 | Accepted the narrow two-stage trusted-base correction mechanism and its inert Stage 1 packet under issue `#4228`; no Stage 2 consumer or baseline change. |
