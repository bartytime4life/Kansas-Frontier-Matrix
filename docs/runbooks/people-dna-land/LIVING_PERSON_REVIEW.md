<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-living-person-review
title: People, DNA, and Land Living-Person Review Runbook
type: runbook
version: 0.2.0
status: DRAFT_REPOSITORY_GROUNDED; SYNTHETIC_VALIDATION_ONLY; POLICY_RUNTIME_UNBOUND; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable privacy, consent, Indigenous/Tribal, legal, and domain stewardship NEEDS VERIFICATION"
created: NEEDS_VERIFICATION
updated: 2026-08-25
owning_root: docs/
responsibility: human review procedure for the existing people-dna-land lane
related:
  - docs/domains/people-dna-land/EXPANSION_BACKLOG.md
  - docs/policy/living_persons_geoprivacy.md
  - policy/domains/people-dna-land/README.md
  - policy/consent/people-dna-land/README.md
  - .github/workflows/domain-people-dna-land.yml
  - tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
[/KFM_META_BLOCK_V2] -->

# People, DNA, and Land Living-Person Review Runbook

## Purpose and authority boundary

Use this procedure to keep a repository change involving living people, DNA-derived material, family or kin relationships, or land-linked identity on hold until its evidence, consent, purpose, audience, sensitivity, and accountable-review requirements are established.

This runbook is a human procedure. It does not activate policy, grant consent, make a legal determination, recognize authority on behalf of an Indigenous Nation or Tribe, approve a lifecycle transition, or publish data. Accepted ADR-0029 and the adopted Directory Rules place human procedures under `docs/`; this file remains at its existing path and creates no new responsibility root or parallel authority home.

When repository documentation and executable evidence differ, preserve both facts: accepted governance defines the boundary, while executable evidence establishes only the behavior actually demonstrated. Do not infer operational maturity from an asserted policy posture.

## Current evidence boundary

| Surface | Current-session repository evidence | Review consequence |
|---|---|---|
| Consent-overlay fixture profile | `.github/workflows/domain-people-dna-land.yml`, `validate_consent_overlay.py`, and `test_consent_overlay_safety.py` execute deterministic checks over repository-owned synthetic fixtures. | A passing check confirms only the bounded fixture profile. |
| Revocation-propagation assessment | The workflow, validator, and tests exercise synthetic `ACTIVE`, `REVOKED`, `EXPIRED`, `UNKNOWN`, and `ERROR` states. The schema remains `PROPOSED_INACTIVE`, and the satisfied result is consent-dimension-only. | Do not describe this as an active policy runtime or complete release decision. |
| Policy sources | The domain and consent policy READMEs describe a fail-closed posture but also record inactive or evaluator-unbound implementation. | Policy activation and production binding remain **NEEDS VERIFICATION**. |
| Real-person or culturally controlled material | The executable lane deliberately uses synthetic fixtures and does not establish legal authority, consent sufficiency, sovereignty review, or safe handling of real records. | Real or source-derived material remains **HOLD** pending accountable review outside Git and CI. |
| Proof, promotion, release, and publication | The workflow reports that accepted proof production and release dry-run capability are not established. | No runbook result authorizes promotion, release, deployment, or publication. |

## Mandatory stop conditions

Stop and record **HOLD** without placing sensitive detail in Git, a PR, an issue, CI output, or an artifact when any of these conditions applies:

- whether a person is living cannot be established safely;
- purpose, audience, allowed use, retention, or data minimization is missing or ambiguous;
- consent is missing, expired, revoked, disputed, unverifiable, or narrower than the proposed use;
- the material includes or may reveal genomic data, kinship, living-person location, precise land relationships, protected cultural knowledge, burial or archaeology locations, rare-species associations, critical infrastructure, or another restricted attribute;
- Indigenous or Tribal sovereignty, consent, cultural protocol, data-governance authority, or appropriate representative cannot be resolved;
- rights, license, provenance, EvidenceRef, or chain of custody is insufficient;
- a requested public or lower-trust audience exceeds the established consent and sensitivity boundary;
- a workflow would expose payloads, identifiers, locations, credentials, or source excerpts in repository-visible output;
- a required accountable reviewer or policy binding cannot be identified from current repository authority; or
- the change would require source activation, access widening, lifecycle mutation, publication, deployment, or a repository-setting change.

Absence of a denial is not approval. Unresolved evidence remains **UNKNOWN**; a checkable but unproved control remains **NEEDS VERIFICATION**.

## Review procedure

### 1. Bound the proposed action

Record only a minimized, non-sensitive description of:

- the repository surface and owning responsibility root;
- whether the change is documentation, code, contract, schema, policy, validator, test, fixture, registry, or manifest work;
- the intended purpose and audience;
- the lifecycle state the change reads or proposes to affect; and
- whether real data, an external source, or a publication surface would be touched.

If the action cannot be described without disclosing protected details, keep those details out of repository systems and stop for an approved handling channel.

### 2. Classify the evidence and sensitivity boundary

Confirm, without copying source payloads, whether the proposal concerns:

- a demonstrably non-living historical person or a person who may be living;
- DNA, genomic, biometric, health, family, kinship, or inferential identity material;
- land tenure, allotment, parcel, address, mobility, or precise-location information;
- Indigenous or Tribal people, knowledge, places, governance, or cultural controls; and
- an EvidenceBundle/EvidenceRef or only generated, summarized, or asserted language.

Treat generated text, indexes, embeddings, maps, tiles, and summaries as derived material, not canonical truth. Evidence-dependent claims must resolve through EvidenceRef and follow cite-or-abstain.

### 3. Verify consent dimensions

For a synthetic validation profile, verify that the recorded consent is active, unexpired, not revoked, within purpose and audience, and limited to the requested operation. For any real case, the repository validators are insufficient: require the accountable privacy, consent, legal, domain, and—when implicated—Indigenous or Tribal governance review appropriate to the material.

Do not convert `UNKNOWN`, missing, or errored consent into approval. Revocation and expiry must block the next use within the bounded synthetic assessment; broader deletion, propagation, notification, and proof obligations remain unestablished unless separately demonstrated.

### 4. Run only the bounded synthetic checks

From a clean checkout at the exact SHA under review, with network access disabled by the workflow profile, run:

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json
python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

Also confirm that the workflow's invalid consent-overlay fixtures are rejected. Prefer the repository workflow for the complete negative-fixture loop; do not invent a broader parent validator or publication command.

A pass is **HEAD VALIDATION** only when the tested commit is the exact branch head. A pull-request merge ref is **MERGE-RESULT VALIDATION** and must be labeled with its synthetic merge SHA. Any other result is **NEEDS VERIFICATION**.

### 5. Interpret the result without overclaiming

| Observation | Required interpretation |
|---|---|
| Valid synthetic fixture accepted and invalid synthetic fixtures rejected | The bounded fixture profile passed; policy activation, real-data suitability, and release readiness remain unproved. |
| `REVOKED` or `EXPIRED` does not deny and block next use | **HOLD**; the bounded fail-closed acceptance criterion failed. |
| `UNKNOWN` does not abstain, or `ERROR` does not remain an error | **HOLD**; uncertainty or failure was converted into an unsafe result. |
| Consent scope, audience, evidence, sensitivity, rights, or accountable ownership is unresolved | **HOLD** with **UNKNOWN** or **NEEDS VERIFICATION**, as applicable. |
| The requested action reaches promotion, release, deployment, publication, or access control | Stop. This runbook has no authority to perform that action. |

### 6. Prepare a minimized review handoff

Record the exact repository SHA, affected paths, synthetic checks and tested SHAs, evidence-reference presence, consent-state category, sensitivity categories, unresolved authorities, and the reason for **HOLD**, **UNKNOWN**, or **NEEDS VERIFICATION**. Use opaque internal references where an approved review system supports them; do not place personal identifiers, sequences, precise locations, protected cultural information, or proprietary excerpts in repository-visible surfaces.

The handoff is evidence for accountable review, not the review decision itself.

## Acceptance criteria

This documentation slice is complete only when:

1. the runbook distinguishes the current synthetic executable profile from inactive or unverified policy runtime;
2. missing, revoked, expired, unknown, and errored consent cannot be described as approval;
3. living-person, genomic, land-linked, Indigenous/Tribal, precise-location, rights, and publication risks have explicit stop conditions;
4. exact existing commands are provided without inventing a parent validator, source activation, proof producer, release, or publication path;
5. HEAD and MERGE-RESULT validation are distinguished;
6. no real, private, proprietary, culturally controlled, or rights-unclear material appears in the file; and
7. rollback is limited to this documentation change and cannot be mistaken for data deletion or consent revocation.

## Proposal-source reconciliation

`KFM_Full_Atlas_seed_cards.md`, v2 expansion section, “People / DNA / Land Safety Lane” (lines 2794–2901 in the inspected Markdown copy; SHA-256 `9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2`, retrieved 2026-08-25) proposes bounded consent, sensitivity, evidence, and denial controls. It also says repository implementation maturity is unknown. That source is proposal material, not repository authority.

The later `KFM Circled Sources — Distinctive Delta Synthesis` (modified 2026-08-23), section 3.1, reinforces the need to separate authority posture from executable capability. It does not adopt this runbook or activate policy. The procedure above keeps only ideas corroborated by accepted ADR-0029 and exact-baseline repository evidence.

## Rollback and non-effects

Before merge, close the draft PR and discard only its campaign branch. After merge, revert the single documentation commit or submit a reviewed forward correction. Either action changes documentation only; it does not revoke consent, delete data, alter policy, undo a lifecycle event, retract a release, or change public state.

This runbook and its validation commands do not contact a live source, process real person data, admit a source, activate a policy, establish legal or sovereign authority, create proof, apply a promotion transition, issue a receipt, release, deploy, publish, widen access, or change repository settings.
