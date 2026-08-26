<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-not-for-life-safety-audit
title: Hazards Not-for-Life-Safety Audit Runbook
type: runbook
version: 0.3.0
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_VALIDATION_ONLY; RUNTIME_ENFORCEMENT_UNVERIFIED; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable hazards, safety, emergency-management, policy, legal, and accessibility stewardship NEEDS VERIFICATION"
created: 2026-08-25
updated: 2026-08-26
owning_root: docs/
responsibility: human audit procedure for the existing hazards lane
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 7115f5c046d0660c65befef65f20964de79c5f2b
related:
  - docs/domains/hazards/README.md
  - docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - contracts/domains/hazards/README.md
  - schemas/contracts/v1/domains/hazards/README.md
  - policy/domains/hazards/README.md
  - .github/workflows/domain-hazards.yml
  - tools/validators/domains/hazards/validate_usdm_materiality.py
  - tests/domains/hazards/test_hazards_smoke.py
  - tests/domains/hazards/test_validate_usdm_materiality.py
[/KFM_META_BLOCK_V2] -->

# Hazards Not-for-Life-Safety Audit Runbook

> [!CAUTION]
> KFM is not an emergency alert system, incident-command system, protective-action authority, medical service, regulatory authority, or substitute for official instructions. A reviewed surface that could reasonably be mistaken for current life-safety direction must stop at `HOLD`; this runbook cannot authorize an exception.

## Purpose and authority boundary

Use this procedure to audit whether a proposed Hazards repository surface stays within KFM's not-for-life-safety boundary. KFM may provide evidence-linked historical, regulatory, observed, modeled, exposure, resilience, and time-bounded operational context. It must not tell a person what protective action to take, guarantee current conditions, or present KFM as the issuer, interpreter, or relay authority for an emergency product.

This runbook is a documentary audit and accountable-review handoff. It does not prove that every runtime path enforces the boundary, activate a source or policy bundle, resolve an EvidenceRef, approve a lifecycle transition, create a proof, assemble a release candidate, deploy, or publish. Accepted ADR-0029 and the adopted Directory Rules place human procedures under `docs/`; this same-path update creates no new responsibility root or parallel policy, evidence, alert, proof, release, or publication home.

## Current evidence boundary

The statements below are bounded to the metadata snapshot. Re-read current bytes when the base, target, workflow, Makefile, policy lane, or validator lane moves.

| Surface | Repository-grounded evidence | Audit consequence |
|---|---|---|
| Hazards doctrine | `docs/domains/hazards/README.md`, `LIFE_SAFETY_BOUNDARY.md`, and `PUBLICATION_AND_BOUNDARY.md` document the not-for-life-safety posture, referral posture, source-role separation, temporal controls, and deny/abstain conditions. | Human-readable doctrine constrains the audit; it is not proof that every runtime path enforces it. |
| Bounded executable validation | `.github/workflows/domain-hazards.yml`, `python -m unittest -v tests.domains.hazards.test_hazards_smoke`, `make hazards-validate`, the USDM materiality validator, and committed synthetic fixtures form the current executable lane. | Passing proves only the named deterministic, no-network fixture profiles at the tested SHA. |
| Policy binding | `policy/domains/hazards/README.md` reports draft, default-only policy source with no accepted active bundle, evaluator, or governed-consumer enforcement path. | An operational policy-enforcement claim remains `NEEDS VERIFICATION`; do not manufacture an `ALLOW`, `ABSTAIN`, `DENY`, or `ERROR` result without an actual evaluator record. |
| Proof and release | The domain workflow contains explicit readiness holds for Hazards proof production and Hazards release dry-run assembly. | Proof, promotion, release, deployment, and publication remain `HOLD`. A green held job does not graduate the lane. |
| Public clients | Governing documents require governed interfaces and released public-safe carriers, but this documentation slice does not enumerate or execute every API, UI, export, map, or AI path. | Public-client conformance remains `NEEDS VERIFICATION` until exact paths and negative tests are demonstrated. |
| Live sources and current conditions | The workflow is fixture-only and declares `KFM_NO_NETWORK=1`; it does not retrieve or validate current hazard conditions. | Freshness, warning validity, current official instructions, and live-source fitness remain outside this audit. |

## Change-impact triage

Classify the proposed change before selecting evidence and checks. Use the highest applicable class; the class does not itself authorize work or reduce any mandatory gate.

| Class | Typical change | Minimum audit depth |
|---|---|---|
| `H1_DOCUMENTARY` | Same-path wording, navigation, or non-behavioral explanation. | Pin the diff; preserve boundary meaning, links, truth labels, and non-effects; run the current Hazards workflow-triggered checks. |
| `H2_SEMANTIC_CONTROL` | Contract, schema, policy-source, validator, fixture, test, or source-role meaning. | Reconcile every direct companion; test positive and fail-closed cases; verify compatibility, finite outcomes, and ownership. |
| `H3_PUBLIC_CARRIER` | Governed API response, Explorer view, map layer, Evidence Drawer, Focus Mode, export, report, or dashboard. | Inspect the exact rendered or machine-consumed output, public path, evidence join, temporal state, referral behavior, accessibility, and negative tests. |
| `H4_SOURCE_OR_TIME` | Source descriptor, operational context, issue/expiry semantics, freshness, correction, or source activation. | Verify issuing authority, source role, terms, retrieval path, time fields, stale/expired behavior, correction lineage, and live-network classification. |
| `H5_RELEASE_OR_CORRECTION` | Candidate, proof, release manifest, withdrawal, correction, rollback, or already public carrier. | Require independently governed proof/release/correction evidence and an exact rollback target. Under the current snapshot, Hazards proof and release remain held. |

Record the selected class and why lower classes are insufficient. Do not label a runtime or release-affecting change `H1_DOCUMENTARY` merely because its diff includes Markdown.

## Mandatory stop conditions

Stop and record `HOLD` when any reviewed surface:

- claims or implies that KFM issues an emergency alert, warning, evacuation order, shelter direction, medical instruction, incident-command instruction, regulatory decision, all-clear, safe-return message, or guaranteed-current condition;
- obscures that official sources and accountable authorities control life-safety action;
- converts missing, stale, expired, conflicting, unsupported, corrected, withdrawn, or policy-denied evidence into reassuring or actionable language;
- lets generated language outrank an EvidenceBundle, omits required EvidenceRef resolution, or answers an evidence-dependent question without cite-or-abstain behavior;
- treats a map, tile, index, embedding, summary, model output, dashboard, badge, screenshot, or generated narrative as canonical truth;
- lacks an auditable source role, object family, issue/observation time, validity or expiry context, freshness state, limitation, or correction/withdrawal path required by its governing contract;
- presents operational context as current when the issuing authority, source record, issue time, validity interval, expiry, cancellation, supersession, or retrieval time cannot be established;
- points users to an unverified, private, signed, stale, or non-authoritative referral destination where an official-source route is required;
- exposes precise restricted locations, critical infrastructure, culturally controlled information, archaeology locations, rare-species locations, living-person information, credentials, proprietary content, or another protected payload;
- contacts or activates a live source, widens access, mutates lifecycle state, releases, deploys, publishes, or changes repository settings outside separately authorized scope;
- requires a workflow that exposes secrets, grants unnecessary write authority, runs untrusted code with privileged context, or causes release, deployment, publication, or administrative side effects;
- affects an already released carrier but lacks an exact correction, withdrawal, cache-invalidation, supersession, and rollback path appropriate to actual reliance; or
- cannot identify its governing contract, policy, validator, owner/review route, and public compatibility boundary from current repository authority.

Do not downgrade `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD` to a pass. Absence of a detected unsafe phrase is not proof of semantic safety or runtime enforcement.

## Audit procedure

### 1. Pin the surface and exact repository state

Record the exact 40-character commit SHA, target blob or artifact digest when available, changed paths, owning roots, exposed audience, and whether the surface is documentation, API, UI, AI-generated language, export, map layer, tile, index, contract, schema, policy, validator, test, registry, proof, candidate, or manifest.

Distinguish validation identities:

- **HEAD VALIDATION** tested the exact branch-head SHA.
- **MERGE-RESULT VALIDATION** tested a named synthetic merge SHA.
- **RELEASE-CANDIDATE VALIDATION** tested an immutable candidate identity and its referenced artifacts.
- **UNKNOWN** applies when checkout or artifact identity cannot be established.

If behavior depends on an unpinned live service, private payload, mutable source, deployed client, or unavailable authority record, classify the affected claim `UNKNOWN` and stop that portion.

### 2. Classify the outward claim and source role

For every consequential item, record both what it is and how the public surface uses it.

| Audit class | Meaning | Required outward behavior |
|---|---|---|
| `analysis_context` | KFM-authored historical, analytical, planning, exposure, resilience, or model interpretation. | Keep evidence, source role, spatial/temporal scope, limitations, release state, and correction lineage visible; never convert it into protective-action advice. |
| `source_observed_official_context` | A warning, advisory, watch, bulletin, declaration, or incident message carried from an identified official source. | Attribute the issuing authority, preserve exact time/currentness fields, distinguish source text from KFM paraphrase, show the not-for-life-safety boundary, and provide the governed official referral. |
| `prohibited_operational_guidance` | KFM-authored, transformed, or presented language that directs protective action or appears to carry official authority. | `HOLD`; where an accepted evaluator exists, the use must be denied. Do not release or publish. |
| `unresolved` | Source role, object family, time, evidence, rights, sensitivity, authorship, or correction state cannot be established. | `UNKNOWN` or `NEEDS VERIFICATION`; use `HOLD` when the unresolved fact is required for safe review. |

Do not infer source authority from warning colors, icons, badges, map symbols, visual prominence, provider branding, model confidence, or interface freshness.

### 3. Trace authority and evidence joins

For each evidence-dependent claim or output, verify the chain that is actually present:

1. governed interface and applicable contract;
2. stable object and artifact identity;
3. EvidenceRef resolution to an EvidenceBundle, or an explicit finite abstention where the contract requires evidence;
4. source role, object family, provenance, and transform lineage;
5. observation, issue, effective, validity, expiry, cancellation, supersession, correction, retrieval, and transaction time required by the contract;
6. rights, sensitivity, precision, and access posture;
7. an actual policy decision and all obligations, only when an accepted evaluator path exists;
8. review and release state; and
9. correction, revocation, withdrawal, cache invalidation, and rollback references where applicable.

Do not fill a missing join with prose. Record `HOLD`, `UNKNOWN`, or `NEEDS VERIFICATION` and identify only the missing control, without copying a sensitive payload into the audit record.

### 4. Verify the minimum envelope for official operational context

A `source_observed_official_context` item is incomplete until the reviewed surface or its governed backing record provides the applicable fields below.

| Field family | Required evidence |
|---|---|
| Source identity | Issuing authority, governed source identifier, source record identifier, and authoritative retrieval/referral basis. |
| Content identity | Immutable content digest or version when available; clear distinction between verbatim source material, quoted excerpt, machine transform, and KFM-authored paraphrase. |
| Source role and object family | Explicit warning/advisory/watch/declaration/context role without collapsing the item into an observed event, forecast, model, regulatory polygon, or KFM instruction. |
| Time | Issue and retrieval time plus every applicable effective, validity, expiry, cancellation, supersession, correction, and transaction time. |
| Currentness | Explicit current, stale, expired, cancelled, superseded, corrected, historical, or unknown state derived from evidence rather than UI recency. |
| Evidence | Resolvable evidence reference or a recorded reason the outward surface must abstain. |
| Transform and representation | Transform/representation receipt or equivalent lineage when text, geometry, precision, symbology, aggregation, or format changed materially. |
| Correction and rollback | Stable correction/supersession reference and rollback or withdrawal target where the carrier has been released or cached. |

Missing fields fail closed in proportion to consequence. A timestamp alone does not prove currentness, and a live-looking interface does not prove that an official product remains valid.

### 5. Review representation, interaction, and referral

Inspect the exact user-visible or machine-consumed output for:

- clear KFM role and limitations at the point a user could act;
- no KFM-authored protective-action instruction, assurance, or interpretation of official guidance;
- no stale, expired, cancelled, superseded, corrected, or unknown observation represented as current;
- no generated recommendation that exceeds its evidence or policy boundary;
- citation or abstention for evidence-dependent claims;
- accessible, non-color-only presentation of critical limitations when a UI is in scope;
- evidence, time, correction, and release state retained in exports and API responses; and
- no direct pointer from a public carrier to RAW, WORK, QUARANTINE, canonical/internal stores, private links, signed URLs, or direct model output.

Where an official referral is consequential, verify that it:

1. points to the responsible issuing authority appropriate to the product context;
2. is derived from a governed source/registry or another accepted authority record rather than invented ad hoc;
3. does not contain credentials, signed query material, private hostnames, or user-specific state;
4. preserves KFM's non-authority posture and does not paraphrase official protective-action guidance as KFM advice;
5. has a recorded observation result when link reachability is checked; and
6. is not called safe or current merely because an HTTP request succeeded.

A `403`, `429`, authentication requirement, robots denial, network restriction, timeout, or indeterminate redirect is `INACCESSIBLE` or `UNKNOWN`, not automatic evidence that the destination is broken or safe. This step requires the actual governed output path; a mockup, proposal, isolated string search, or screenshot is insufficient to prove runtime behavior.

### 6. Perform workflow-safety preflight

Before push or release-adjacent review, inspect every workflow triggered by the changed paths. Record event, permissions, runner, checkout credential behavior, dependency installation, executed commands, network posture, artifacts, and external side effects.

**CONFIRMED snapshot:** at `main@7115f5c046d0660c65befef65f20964de79c5f2b`, `.github/workflows/domain-hazards.yml` uses GitHub-hosted `ubuntu-latest`, `permissions: contents: read`, pinned checkout/setup actions, `persist-credentials: false`, a five-minute timeout, and `KFM_NO_NETWORK=1`. Its executable validation job runs the Hazards smoke test and `make hazards-validate`; its proof and release-dry-run jobs are explicit readiness holds. It contains no deployment, publication, release, or administrative mutation. Re-read current bytes if the workflow or base moves.

Use `HOLD` when required validation depends on an unsafe or unreviewed execution path. Ordinary read-only pull-request validation is expected and is not by itself a blocker.

### 7. Run the current bounded repository checks

From a clean checkout at the exact SHA under review:

```bash
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

At the metadata snapshot, `make hazards-validate` runs:

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 TZ=UTC \
python -m unittest discover \
  --start-directory tests/domains/hazards \
  --pattern 'test_validate_usdm_materiality.py' \
  --verbose

KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 TZ=UTC \
python tools/validators/domains/hazards/validate_usdm_materiality.py --fixtures
```

Confirm that valid fixtures pass and negative fixtures fail as specified. Re-read the current `Makefile`; command text in this runbook is a pinned snapshot, not permanent command authority.

Do not interpret a pass as a life-safety enforcement test, live-feed validation, current-conditions check, active policy evaluation, EvidenceBundle, proof packet, release dry run, public readback, deployment, or publication approval.

### 8. Check for control drift

Use read-only search to locate the boundary, public carriers, and bounded validator wiring:

```bash
rg -n "not[-_ ]for[-_ ]life[-_ ]safety|emergency alert|alert authority|official_source" \
  docs/domains/hazards policy/domains/hazards apps packages tests tools \
  contracts schemas data/registry release .github/workflows/domain-hazards.yml

rg -n "hazards-validate|validate_usdm_materiality|test_hazards_smoke" \
  Makefile .github/workflows/domain-hazards.yml tests tools
```

Review each match in context. A search result is discovery evidence, not control enforcement. New runtime paths with no governed denial/abstention behavior, exact-source/time envelope, or negative test remain `NEEDS VERIFICATION`.

### 9. Record a finite audit disposition

Keep audit, policy, validator, CI, review, and release states separate.

| Observation | Audit disposition |
|---|---|
| KFM issues or implies life-safety direction or authority | `HOLD`; do not advance to release review. |
| Missing, stale, expired, unsupported, corrected, or denied evidence becomes actionable or reassuring output | `HOLD`; fail-closed behavior is not demonstrated. |
| Bounded synthetic materiality checks pass but runtime enforcement is not exercised | `NEEDS VERIFICATION`; record the exact limited pass separately. |
| Exact runtime path, evidence joins, source/time envelope, referral behavior, negative tests, and policy binding are demonstrated at the tested SHA | Record a scoped audit `PASS`; accountable review and release authority remain separate. |
| Evidence, ownership, rights, sensitivity, currentness, or validation is unavailable or non-comparable | `UNKNOWN` or `NEEDS VERIFICATION`; use `HOLD` when required for safe progression. |

A policy result may be reported only from an accepted evaluator record. Validator and hosted-check results use their own finite states: `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, or `UNKNOWN`. Every `NOT_APPLICABLE` entry must include a rationale tied to the reviewed scope.

> [!IMPORTANT]
> A scoped audit `PASS`, policy `ALLOW`, green validator, commit, pull request, merge, badge, or screenshot does not establish source truth, current conditions, emergency fitness, proof closure, release, deployment, or publication.

### 10. Assemble the audit packet

The audit packet must include at least:

```yaml
audit_id: "kfm://audit/hazards/<stable-id>"
repository: "bartytime4life/Kansas-Frontier-Matrix"
validation_identity: "HEAD | MERGE_RESULT | RELEASE_CANDIDATE | UNKNOWN"
base_sha: "<40-character-sha>"
tested_sha: "<40-character-sha>"
branch_or_candidate: "<stable-id>"
change_impact_class: "H1_DOCUMENTARY | H2_SEMANTIC_CONTROL | H3_PUBLIC_CARRIER | H4_SOURCE_OR_TIME | H5_RELEASE_OR_CORRECTION"
changed_paths: []
artifact_digests: {}
public_or_review_audience: "<audience>"
audit_disposition: "PASS | HOLD | NEEDS_VERIFICATION | UNKNOWN"
commands: []
validator_results: []
hosted_check_results: []
not_applicable_rationales: []
authority_and_evidence_joins: []
source_observation_envelopes: []
official_referral_checks: []
rights_sensitivity_precision_findings: []
correction_withdrawal_rollback_refs: []
unresolved_items: []
accountable_handoff_route: "<verified-route-or-NEEDS-VERIFICATION>"
notes: []
```

Keep real hazard payloads, restricted locations, credentials, private links, signed URLs, personal data, culturally controlled information, and proprietary excerpts out of Git and CI. The audit packet is not an EvidenceBundle, policy decision, proof pack, promotion decision, release manifest, correction notice, deployment record, or publication event.

## Acceptance criteria

This runbook update is complete only when:

1. the not-for-life-safety boundary is explicit and cannot be mistaken for KFM alert authority;
2. the current USDM materiality checks are correctly scoped as bounded synthetic validation;
3. missing runtime binding, accepted policy evaluation, proof, release, and public-readback capability remain held or unverified;
4. change-impact triage prevents runtime, source/time, or release work from being disguised as a documentation-only review;
5. operational context requires source identity, role, time/currentness, evidence, transform, correction, and rollback fields appropriate to consequence;
6. official referral review distinguishes a pointer to authority from relaying or interpreting protective-action guidance;
7. evidence, freshness, policy, rights, sensitivity, precision, official-authority, public-client, and workflow-safety review fail closed;
8. head, merge-result, and release-candidate validation identities remain distinct;
9. every `NOT_APPLICABLE` result includes a reason;
10. no live, sensitive, proprietary, culturally controlled, rights-unclear, or precise-location material appears; and
11. rollback changes documentation only unless a separately governed public correction is required.

## Proposal-source reconciliation

`KFM_Full_Atlas_seed_cards.md`, v2 expansion section, **“Hazards Without Emergency Alerting,”** proposes hazard history, regulatory context, operational context, observations, detections, models, resilience review, visible freshness/expiry, official-source routing, and finite deny/abstain behavior without turning KFM into an emergency alert system. The source explicitly labels these statements `PROPOSED` and leaves repository implementation maturity `UNKNOWN`.

This update retains those ideas only where current repository authority corroborates them. The seed card remains proposal lineage; it does not establish source admission, accepted policy, runtime enforcement, steward assignment, proof, release, deployment, publication, or emergency fitness.

## Rollback and non-effects

Before merge, close or abandon the draft pull request and its feature branch; deleting remote objects requires separate authority. After merge, use a transparent revert or reviewed forward-fix pull request against the actual merged commit. Do not rewrite shared history.

If an already public carrier is affected, a Git revert may be insufficient. Preserve and execute the governed correction, withdrawal, supersession, cache invalidation, public notice, and rollback process required by actual reliance.

This runbook and its validation commands do not contact a live source, issue or relay a warning, provide life-safety guidance, admit or activate a source, create evidence or proof, activate policy, approve review, promote, release, deploy, publish, widen access, or change repository settings.
