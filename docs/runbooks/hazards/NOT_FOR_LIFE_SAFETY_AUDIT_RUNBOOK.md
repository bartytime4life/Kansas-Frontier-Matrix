<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-not-for-life-safety-audit
title: Hazards Not-for-Life-Safety Audit Runbook
type: runbook
version: 0.2.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_VALIDATION_ONLY; RUNTIME_ENFORCEMENT_UNVERIFIED; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable hazards, safety, emergency-management, policy, legal, and accessibility stewardship NEEDS VERIFICATION"
created: 2026-08-25
updated: 2026-08-25
owning_root: docs/
responsibility: human audit procedure for the existing hazards lane
related:
  - docs/domains/hazards/README.md
  - docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - policy/domains/hazards/README.md
  - .github/workflows/domain-hazards.yml
  - tools/validators/domains/hazards/validate_usdm_materiality.py
  - tests/domains/hazards/test_validate_usdm_materiality.py
[/KFM_META_BLOCK_V2] -->

# Hazards Not-for-Life-Safety Audit Runbook

## Purpose and authority boundary

Use this procedure to audit whether a proposed Hazards repository surface stays within KFM's not-for-life-safety boundary. KFM may provide evidence-linked context; it must not present itself as an emergency alert system, incident command, evacuation authority, weather service, medical service, regulatory authority, or substitute for official instructions.

This runbook is a documentary audit and accountable-review handoff. It does not establish that every runtime path enforces the boundary, approve a lifecycle transition, activate a source, or authorize release or publication. Accepted ADR-0029 and the adopted Directory Rules place human procedures under `docs/`; this file remains at its existing path and creates no new responsibility root or parallel policy, evidence, alert, proof, or publication home.

## Current evidence boundary

| Surface | Current-session repository evidence | Audit consequence |
|---|---|---|
| Hazards doctrine | `docs/domains/hazards/README.md` and `LIFE_SAFETY_BOUNDARY.md` state a not-for-life-safety posture and describe deny/abstain conditions. | This is repository documentation, not proof that every public runtime enforces it. |
| Bounded executable validation | `.github/workflows/domain-hazards.yml`, `make hazards-validate`, and the USDM materiality validator/tests exercise repository-owned synthetic fixture behavior without a live feed. | Passing proves only the bounded USDM materiality profile at the tested SHA. |
| Policy binding | `policy/domains/hazards/README.md` records a non-release, non-publication posture; broader runtime binding and accountable stewardship remain unverified. | Operational policy enforcement is **NEEDS VERIFICATION**. |
| Proof and release | The workflow reports no accepted Hazards proof producer and no release dry-run command or candidate manifest. | Proof, promotion, release, deployment, and publication remain **HOLD**. |
| Public clients | The audit found governing intent that clients use governed interfaces, but this documentation slice does not execute or enumerate every client path. | A public-client conformance claim remains **NEEDS VERIFICATION** until exact paths and negative tests are demonstrated. |

## Mandatory stop conditions

Stop and record **HOLD** when any reviewed surface:

- claims or implies that KFM issues an emergency alert, warning, evacuation order, shelter direction, medical instruction, incident-command instruction, regulatory decision, or guaranteed-current condition;
- obscures that official sources and accountable authorities control life-safety action;
- converts missing, stale, expired, conflicting, unsupported, or policy-denied evidence into reassuring or actionable language;
- lets generated language outrank an EvidenceBundle, omits required EvidenceRef resolution, or answers an evidence-dependent question without cite-or-abstain behavior;
- treats a map, tile, index, embedding, summary, model output, or generated narrative as canonical truth;
- lacks an auditable source role, observation time, validity/freshness context, limitation, or correction/withdrawal path required by its governing contract;
- exposes precise restricted locations, critical infrastructure, culturally controlled information, archaeology locations, rare-species locations, living-person information, credentials, proprietary content, or another protected payload;
- contacts or activates a live source, widens access, mutates lifecycle state, releases, deploys, publishes, or changes repository settings; or
- cannot identify its governing contract, policy, validator, owner, and public compatibility boundary from current repository authority.

Do not downgrade **UNKNOWN** or **NEEDS VERIFICATION** to a pass. Absence of a detected unsafe phrase is not proof of runtime enforcement.

## Audit procedure

### 1. Pin the surface and exact repository state

Record the exact 40-character commit SHA, paths, owning roots, exposed audience, and whether the surface is documentation, API, UI, AI-generated language, export, map layer, tile, index, contract, schema, policy, validator, test, registry, or manifest. Distinguish a branch-head check from a synthetic merge-result check.

A check is **HEAD VALIDATION** only when it tested the exact branch-head SHA. A pull-request merge ref is **MERGE-RESULT VALIDATION** and must name its synthetic merge SHA; when checkout identity cannot be established, report **NEEDS VERIFICATION**.

If the inspected behavior depends on an unpinned live service, private payload, mutable source, deployed client, or unavailable authority record, classify the result **UNKNOWN** and stop.

### 2. Trace authority and evidence joins

For each evidence-dependent claim or output, verify the chain that is actually present:

1. governed interface and applicable contract;
2. EvidenceRef resolution to an EvidenceBundle or an explicit abstention;
3. source role and provenance;
4. observation, issue, validity, expiry, or retrieval time required by the contract;
5. policy decision and limitation handling; and
6. correction, revocation, withdrawal, and rollback references where applicable.

Do not fill a missing join with prose. Record **HOLD** or **NEEDS VERIFICATION** and identify only the missing control, without copying a sensitive payload into the audit record.

### 3. Review representation and interaction

Inspect the exact user-visible or machine-consumed output for:

- clear KFM role and limitations;
- no KFM-authored life-safety instruction or assurance;
- no stale observation represented as current;
- no generated recommendation that exceeds its evidence or policy boundary;
- citation or abstention for evidence-dependent claims;
- a clear route to the responsible official authority appropriate to the product context, without KFM impersonating or intermediating that authority; and
- accessible, non-color-only presentation of critical limitations when a UI is in scope.

This step requires the actual governed output path. A mockup, proposal document, or isolated string search is insufficient to prove runtime behavior.

### 4. Run the current bounded repository checks

From a clean checkout at the exact SHA under review, use the existing commands:

```bash
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

`make hazards-validate` runs the synthetic USDM materiality validator and its fixture tests under the repository's deterministic no-network profile. Confirm that valid fixtures are accepted and negative fixtures are rejected. Do not interpret a pass as a life-safety enforcement test, live-feed validation, proof packet, release dry run, or public-readback check.

### 5. Check for control drift

Use read-only search to locate the boundary and bounded validator wiring:

```bash
rg -n "not[-_ ]for[-_ ]life[-_ ]safety|emergency alert|alert authority" \
  docs/domains/hazards policy/domains/hazards apps packages tests tools \
  .github/workflows/domain-hazards.yml
rg -n "hazards-validate|validate_usdm_materiality" \
  Makefile .github/workflows/domain-hazards.yml tests tools
```

Review each match in context. A search result is discovery evidence, not control enforcement. New runtime paths with no governed denial or abstention test remain **NEEDS VERIFICATION**.

### 6. Record a finite audit disposition

| Observation | Required disposition |
|---|---|
| KFM issues or implies life-safety direction or authority | **HOLD**; do not release or publish. |
| Missing, stale, expired, unsupported, or denied evidence becomes actionable or reassuring output | **HOLD**; fail-closed behavior is not demonstrated. |
| Bounded synthetic materiality checks pass but runtime enforcement is not exercised | **NEEDS VERIFICATION**; record the limited pass separately. |
| Exact runtime path, evidence joins, negative tests, and policy binding are all demonstrated at the tested SHA | Record the scoped evidence; accountable approval is still separate and this runbook performs no transition. |
| Evidence, ownership, rights, sensitivity, or validation is unavailable or non-comparable | **UNKNOWN** or **NEEDS VERIFICATION**; do not infer approval. |

The audit packet must include the exact tested SHA, commands, head-versus-merge-result classification, paths, observed control joins, failure or hold reason, and accountable handoff route. Keep real hazard payloads, restricted locations, credentials, private links, and proprietary excerpts out of Git and CI.

## Acceptance criteria

This documentation slice is complete only when:

1. the not-for-life-safety boundary is explicit and cannot be mistaken for KFM alert authority;
2. the current USDM materiality checks are correctly scoped as bounded synthetic validation;
3. missing runtime binding, proof, release, and public-readback capability remain held or unverified;
4. evidence, freshness, policy, sensitivity, official-authority, and public-client review steps fail closed;
5. head validation and merge-result validation are distinguished;
6. no live, sensitive, proprietary, culturally controlled, rights-unclear, or precise-location material appears; and
7. rollback changes documentation only.

## Proposal-source reconciliation

`KFM_Full_Atlas_seed_cards.md`, v2 expansion section, “Hazards Without Emergency Alerting” (lines 2359–2466 in the inspected Markdown copy; SHA-256 `9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2`, retrieved 2026-08-25) proposes official-source routing, freshness/expiry context, and finite deny/abstain behavior while explicitly describing a design synthesis rather than current implementation. It is proposal material, not repository authority.

The procedure above retains only controls corroborated by accepted ADR-0029, the exact-baseline Hazards documentation, and current executable workflow/validator/test evidence. It does not adopt a proposal-era architecture or assert that runtime enforcement already exists.

## Rollback and non-effects

Before merge, close the draft PR and discard only its campaign branch. After merge, revert the single documentation commit or submit a reviewed forward correction. Either action changes documentation only; it does not correct or withdraw public data, alter a policy decision, undo a lifecycle transition, or establish emergency authority.

This runbook and its validation commands do not contact a live source, issue a warning, provide life-safety guidance, admit or activate a source, create proof, activate policy, approve review, promote, release, deploy, publish, widen access, or change repository settings.
