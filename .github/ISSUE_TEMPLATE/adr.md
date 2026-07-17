---
name: ADR — Architecture Decision Record
about: Propose one consequential KFM architecture or governance decision for review.
title: "ADR-XXXX — <short decision title>"
labels: ["adr", "adr-proposed"]
assignees: ["bartytime4life"]
---

<!--
KFM ADR issue-intake template.

This issue is a proposal and routing record. It is not an accepted ADR, a
StewardshipAssignment, a ReviewRecord, a PolicyDecision, release approval,
publication authority, or proof that implementation exists.

Before submitting:
1. Read docs/adr/README.md and docs/adr/ADR-template.md.
2. Check docs/adr/ and open ADR work for number/decision collisions.
3. Use docs/doctrine/directory-rules.md for ADR triggers and placement.
4. Do not include secrets, exploit details, restricted source payloads, exact
   sensitive locations, living-person records, or DNA/genomic material.
5. Use the private-first path in SECURITY.md for security-sensitive reports.

When the decision is ready to become a repository record, open a PR that adds
or updates docs/adr/ADR-NNNN-<kebab-case-slug>.md from the canonical ADR
template. Closing this issue does not accept the decision.
-->

> [!IMPORTANT]
> This issue proposes a decision. The decision becomes authoritative only through the governed ADR review and merge path, with the accepted artifact in `docs/adr/` and its required companion changes.

> [!CAUTION]
> Do not paste secrets, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person data, DNA/genomic material, private-land details, or source-restricted content. Route security-sensitive material through `SECURITY.md`.

## Proposal summary

<!-- State the decision requested and why a decision is needed now. -->

-

## Proposed ADR identity

| Field | Value |
|---|---|
| Proposed ADR ID | `ADR-XXXX` |
| Proposed filename | `docs/adr/ADR-XXXX-<kebab-case-slug>.md` |
| Decision owner / steward role | |
| Target status | `proposed` |
| Related issue(s) / PR(s) | |
| Number-collision check | <!-- Highest existing number and open ADR work inspected --> |

> [!NOTE]
> The numeric ID is provisional until repository and open-work collision checks pass. Do not overwrite or reuse an existing ADR number.

## ADR trigger

<!-- Check every trigger that applies. At least one should normally apply. -->

- [ ] Add, remove, rename, or reclassify a canonical responsibility root.
- [ ] Promote or retire a compatibility root.
- [ ] Change schema-home authority or contract/schema placement.
- [ ] Split, merge, bypass, or redefine a lifecycle phase.
- [ ] Create a parallel schema, contract, policy, source, registry, release, proof, receipt, or canonical-truth home.
- [ ] Bend a KFM invariant or trust-membrane boundary.
- [ ] Approve or change a direct public-access path.
- [ ] Change promotion, release, correction, withdrawal, or rollback gates.
- [ ] Change sensitive-location, rights, sovereignty, consent, or geoprivacy posture.
- [ ] Change source-ledger, source-role, or evidence authority.
- [ ] Change deterministic identity, canonicalization, or object-family meaning.
- [ ] Adopt or materially change a model/runtime/public-response envelope.
- [ ] Introduce, retire, or materially change a steward/reviewer role or separation-of-duties rule.
- [ ] Change `CONTRACT_VERSION` pinning or a generated-receipt obligation.
- [ ] Structural migration or semantic rename requiring compatibility/supersession planning.
- [ ] Other consequential cross-cutting decision:
- [ ] No formal trigger; ADR is strongly recommended because the choice is cross-cutting, non-obvious, or likely to be re-litigated.

**Trigger basis:** <!-- Cite Directory Rules sections, accepted ADRs, doctrine, or drift entries. -->

## Status and truth labels

<!-- Apply labels per claim, not merely once for the whole proposal. -->

- [ ] `CONFIRMED` — verified from current repository evidence, tests, logs, accepted ADRs, or generated artifacts.
- [ ] `PROPOSED` — design or decision under review; not yet implemented or accepted.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and not safe to assume.

**Current proposal posture:** `PROPOSED`

## Context

<!--
Describe the current state, the problem, the forcing function, and the harm of
leaving the decision unresolved. Separate current evidence from desired state.
-->

-

## Decision

<!--
State one directive in plain language: "KFM will..." or "KFM will not...".
Avoid combining unrelated decisions; split them when independent review or
rollback would be clearer.
-->

KFM will ...

## Scope and non-goals

### In scope

-

### Non-goals

-

### Explicitly unchanged

-

## Evidence basis

<!--
Use precise repository paths plus immutable refs/SHAs, test or run IDs, logs,
manifests, schemas, receipts, or authoritative sources. Memory is not evidence.
-->

| Truth label | Evidence location | Observation supported | Verification / limitation |
|---|---|---|---|
| `CONFIRMED` | | | |
| `PROPOSED` | | | |
| `NEEDS VERIFICATION` | | | |
| `UNKNOWN` | | | |

**EvidenceRef / EvidenceBundle implications:** <!-- N/A or explain resolution requirements. -->

## Directory Rules and authority basis

| Proposed or affected path | Owning responsibility root | Authority / lifecycle role | Directory Rules or ADR basis | Status |
|---|---|---|---|---|
| | | | | |

- [ ] No new parallel authority home is created.
- [ ] Canonical and compatibility roots remain distinct.
- [ ] Human doctrine, semantic contracts, machine schemas, executable policy, data lifecycle, proof/receipt, and release authority remain in their owning roots.
- [ ] Any conflict between current implementation and doctrine is surfaced as drift rather than silently normalized.
- [ ] A migration note/manifest is included when paths or authority move.
- [ ] Not applicable; explanation:

## Affected surfaces

### Responsibility roots

- [ ] `.github/`
- [ ] `docs/`
- [ ] `control_plane/`
- [ ] `contracts/`
- [ ] `schemas/`
- [ ] `policy/`
- [ ] `data/`
- [ ] `release/`
- [ ] `apps/`
- [ ] `packages/`
- [ ] `connectors/`
- [ ] `pipelines/` / `pipeline_specs/`
- [ ] `tools/` / `scripts/`
- [ ] `tests/` / `fixtures/`
- [ ] `runtime/` / `infra/` / `configs/`
- [ ] Other:

**Cross-cutting explanation:** <!-- Required when several roots are affected. -->

### Object families and contracts

- [ ] Source / source-admission objects
- [ ] Evidence / citation objects
- [ ] Policy / sensitivity / rights decisions
- [ ] Validation / review records
- [ ] Identity / canonicalization objects
- [ ] AI/runtime response envelopes or receipts
- [ ] Promotion / release / correction / rollback objects
- [ ] Layer / map / tile / export manifests
- [ ] No object-family meaning changes
- [ ] Other:

### Lifecycle stages

- [ ] RAW
- [ ] WORK / QUARANTINE
- [ ] PROCESSED
- [ ] CATALOG / TRIPLET
- [ ] PUBLISHED
- [ ] No lifecycle-stage impact

### Public and governed interfaces

- [ ] Governed API
- [ ] Explorer/UI/map
- [ ] Focus Mode / AI surface
- [ ] Search / graph / catalog / export
- [ ] Release/publication
- [ ] No public-interface impact

**Trust-membrane notes:** <!-- Explain how public clients remain downstream of governed interfaces. -->

## Consequences and trade-offs

### Positive

-

### Negative / costs

-

### Neutral / accepted trade-offs

-

### Risks introduced

| Risk | Likelihood / impact | Mitigation | Residual risk |
|---|---|---|---|
| | | | |

## Alternatives considered

<!-- Include genuine alternatives. "Status quo" is a valid alternative. -->

1. **Preferred decision —**
2. **Alternative A —**
3. **Alternative B —**
4. **Status quo —**

## Implementation and migration plan

<!--
An ADR records the choice; companion artifacts implement it. List the smallest
reversible sequence and the responsible roots.
-->

| Step | Artifact or path | Owner role | Dependency | Reversible? |
|---|---|---|---|---|
| 1 | | | | |

- Migration manifest / note:
- Compatibility or deprecation window:
- Backfill or data transformation:
- Documentation updates:
- Release/correction implications:

## Companion artifacts affected

- [ ] Doctrine / architecture documentation
- [ ] Contract(s)
- [ ] Schema(s)
- [ ] Policy bundle(s)
- [ ] Positive and negative fixtures
- [ ] Validator(s) / test(s)
- [ ] Source registry / descriptor(s)
- [ ] Pipeline / connector / package / app
- [ ] Workflow / GitHub configuration
- [ ] Migration or deprecation record
- [ ] ReviewRecord / StewardshipAssignment
- [ ] Generated receipt / proof / validation report
- [ ] PromotionDecision / ReleaseManifest
- [ ] CorrectionNotice / RollbackCard
- [ ] None
- [ ] Other:

**Required companion changes:**

-

## Validation and acceptance

<!--
Distinguish tests already run from validation required before acceptance.
Use fixture-only and no-network checks first where feasible.
-->

### Performed

| Check or command | Scope | Outcome | Evidence |
|---|---|---|---|
| | | `PASS` / `FAIL` / `PARTIAL` / `NOT RUN` | |

### Required before acceptance

| Acceptance criterion | Expected outcome | Evidence required | Owner |
|---|---|---|---|
| | | | |

### Failure signals

-

### Post-acceptance verification

-

## Rollback, supersession, and correction

- Rollback target:
- Rollback procedure:
- Rollback cost / irreversible effects:
- Supersedes:
- Superseded by:
- Drift-register update required:
- Correction or withdrawal path:
- Existing released artifacts affected:

> [!IMPORTANT]
> Accepted ADRs are retained. Replace a decision through a successor ADR and explicit supersession links; do not delete history.

## Security, rights, sensitivity, and sovereignty

- [ ] None identified.
- [ ] Security-sensitive implementation or vulnerability details.
- [ ] Archaeology, cultural, Indigenous, burial, or sacred-site material.
- [ ] Rare species, rare plants, habitat, or geoprivacy.
- [ ] Critical infrastructure or emergency operations.
- [ ] Living-person, genealogy, consent, DNA, or genomic material.
- [ ] Private-land or stewardship information.
- [ ] Restricted source terms, licensing, or rights uncertainty.
- [ ] Exact-harm or reconstructable location exposure.
- [ ] Other:

**Required additional reviewer(s):**

**Public-safe transform / access restriction:**

**Private handling required:** `yes` / `no` / `NEEDS VERIFICATION`

## Review and separation of duties

| Role | Proposed reviewer / owner | Required because | Independent from author? |
|---|---|---|---|
| Architecture / repository steward | | | |
| Affected subsystem or domain steward | | | |
| Docs steward | | | |
| Policy / security / sensitivity / rights reviewer | | | |
| Release or correction authority | | | |

- [ ] The decision author is identified.
- [ ] Required approving roles are identified.
- [ ] Material author/approver separation is preserved where required.
- [ ] Missing reviewer identity or authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.

## `CONTRACT_VERSION` implications

Current pin: `3.0.0`

- [ ] No contract-version change.
- [ ] PATCH — clarification or compatible correction.
- [ ] MINOR — additive obligation, companion, field, or gate.
- [ ] MAJOR — operating-law or incompatible contract change.

**Required version action and rationale:**

## Open questions and verification backlog

-

## References

- `docs/adr/README.md`
- `docs/adr/ADR-template.md`
- `docs/doctrine/directory-rules.md`
- `docs/doctrine/ai-build-operating-contract.md`
- `docs/registers/DRIFT_REGISTER.md`
- `docs/registers/VERIFICATION_BACKLOG.md`
- Prior ADR(s):
- Related issue(s) / PR(s):
- Evidence / source links:

## Submitter acknowledgements

- [ ] I understand this issue is a proposal, not an accepted ADR.
- [ ] I checked for ADR number and decision collisions.
- [ ] I separated verified evidence from proposed or unknown claims.
- [ ] I identified Directory Rules placement and migration implications.
- [ ] I listed companion implementation, validation, rollback, and supersession work.
- [ ] I did not include secrets, restricted payloads, or sensitive exact-location details.
- [ ] I identified required independent reviewers and unresolved authority gaps.
- [ ] I understand that issue closure, labels, assignment, or bot actions do not grant decision, release, or publication authority.
