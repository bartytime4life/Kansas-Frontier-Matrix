<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/gate-override-record
title: Gate Override Record Candidate Contract
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; governance; override-candidate; fixture-only; no-authority
owning_root: contracts/
responsibility: Define the bounded semantic shape of a proposed gate-override record without granting bypass, policy, review, promotion, release, deployment, or publication authority.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED contract; NEEDS VERIFICATION human review and production signing design"
related:
  - ../../schemas/contracts/v1/governance/gate_override_record.schema.json
  - ../../fixtures/contracts/v1/governance/gate_override_record/cases.json
  - ../../tools/validators/governance/validate_gate_override_record.py
  - ../../tests/validators/governance/test_validate_gate_override_record.py
  - ../../docs/intake/exploratory/pass-3-gate-override-record-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, gate, override, emergency, remediation, fixture-first]
notes:
  - "Adapts Pass 3 card KFM-P3-IDEA-0003 as an inactive candidate profile."
  - "The fixture attestation is deterministic test pressure only; it is not DSSE, Cosign, Sigstore, authenticated review, or a production signature."
  - "PASS proves local candidate consistency only and cannot bypass a gate."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Gate Override Record Candidate Contract

> A closed, fixture-only contract for describing the minimum evidence, actor separation, scope, validity, remediation, rollback, and attestation information a future gate override would need. The candidate cannot authorize or perform an override.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Owning semantic lane | `contracts/governance/` |
| Machine shape | `schemas/contracts/v1/governance/gate_override_record.schema.json` |
| Production signature profile | `NEEDS VERIFICATION`; deliberately not selected here |
| Override, review, policy, release, deployment, publication authority | Not created or authorized |

A validator `PASS` means only that one synthetic candidate has a closed shape, deterministic identity, coherent actor and gate references, bounded scope, ordered time fields, explicit remediation and rollback, complete local support references, and a matching fixture-only attestation. It does **not** authenticate an actor, approve a reviewer, execute policy, bypass a gate, change GitHub settings, merge, promote, release, deploy, or publish.

## Source requirement

Pass 3 card `KFM-P3-IDEA-0003` states that emergency hotfix and time-sensitive correction overrides must not be silent. A record should name the actor, gate, rationale, and expected remediation and remain visible in the audit trail. This contract preserves that intent while keeping the signing actor, production cryptography, dual-actor policy, allowed duration, and operational integration as separately governed decisions.

## Directory Rules basis

ADR-0029 accepts Directory Rules v2. The packet uses existing responsibility roots only:

| Responsibility | Home |
|---|---|
| Human-readable meaning | `contracts/governance/` |
| Machine-checkable shape | `schemas/contracts/v1/governance/` |
| Synthetic examples | `fixtures/contracts/v1/governance/` |
| Deterministic validation | `tools/validators/governance/` |
| Enforceability proof | `tests/validators/governance/` |
| Hosted orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

This follows `DIR-AUTHROOT-001` through `DIR-AUTHROOT-003`: contracts define meaning, schemas define shape, and policy remains the separate authority for whether an override may ever be allowed. No override ledger, policy rule, source registry, release object, runtime adapter, GitHub setting, or public surface is created.

## Object meaning

```text
GateOverrideRecordCandidate
├── created_at and finite validity window
├── override_class
├── target_gate
│   ├── gate identity and prior blocking result
│   ├── candidate and revision refs
│   └── requested effect = TEMPORARY_GATE_BYPASS
├── actors
│   ├── requester and approver refs/roles
│   ├── policy profile ref
│   └── separation_required
├── rationale
│   ├── reason code and bounded summary
│   └── justification digest
├── scope
│   ├── environment, operations, and repository-relative paths
│   └── effect limit = NO_RELEASE_NO_PUBLICATION
├── remediation
│   ├── work item, owner, due time, expected actions
│   ├── rollback reference
│   └── required verification
├── evidence, policy-decision, and review references
├── fixture-only attestation
├── explicit no-authority claims
├── spec_hash
└── override_id derived from spec_hash
```

## Deterministic identity and fixture attestation

The repository hashing package supplies RFC 8785 JCS plus SHA-256.

1. Exclude `override_id`, `spec_hash`, and `attestation` from the record identity subject.
2. Compute `spec_hash` over the remaining candidate.
3. Set `override_id` to `kfm:gate-override:` plus the full `spec_hash`.
4. Set `attestation.subject_digest` to the record `spec_hash`.
5. Compute `attestation.signature_value` over the remaining attestation members.

The attestation profile is the literal `kfm.fixture.sha256-attestation.v1`. It proves deterministic fixture binding only. A future operational design must select an authenticated signer, signature profile, key/identity policy, transparency requirements, and revocation/correction behavior through a separate contract, policy, and review process.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed shape, identity, time, actor, scope, remediation, support, and fixture-attestation checks pass locally. |
| `HOLD` | Shape is coherent but evidence, policy-decision, or review support is incomplete. |
| `DENY` | Shape, identity, canonical ordering, actor separation, signer binding, fixture attestation, or no-authority rules fail. |
| `ERROR` | The candidate contradicts itself, such as an inverted validity or remediation interval, or cannot be read safely. |

Stable diagnostics contain finding codes and JSON Pointer paths and never echo submitted values.

## Required invariants

- The target gate must report a prior blocking state: `FAILED`, `HOLD`, or `BLOCKED`.
- `requested_effect` is always `TEMPORARY_GATE_BYPASS`; the candidate still claims no actual bypass.
- `separation_required` is supplied by a referenced policy profile; this contract supplies no universal dual-actor default.
- When separation is required, requester and approver must be distinct.
- The fixture signer must equal the declared approver; this is shape coherence, not authentication.
- `valid_from` cannot precede `created_at`; `expires_at` must follow `valid_from`.
- The remediation due time cannot precede record creation.
- Scope paths and reference arrays are canonical, sorted, unique, and repository-relative where applicable.
- Evidence, policy-decision, and review references are all required for `PASS`; absence yields `HOLD`.
- Remediation must name a work item, owner, expected actions, verification requirement, and rollback reference.
- Every authority-bearing claim remains false.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_validate_gate_override_record.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/governance/validate_gate_override_record.py \
  --fixtures
```

The exact fixture matrix covers one complete candidate, three support holds, actor self-approval, noncanonical scope arrays, signer mismatch, fixture-signature drift, record hash/ID drift, and three temporal contradictions.

## Explicit non-goals

This contract does not:

- decide which gates are bypassable;
- define an allowed override duration or universal dual-actor rule;
- authenticate requester, approver, reviewer, or signer identities;
- implement DSSE, Cosign, Sigstore, Rekor, key management, or revocation;
- evaluate a live policy engine;
- change repository settings, rulesets, checks, or merge permissions;
- bypass or rerun a gate;
- authorize a commit, merge, promotion, release, deployment, or publication;
- write lifecycle, audit-ledger, release, or public state;
- create a public badge or UI claim that an override occurred.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the bounded contract/schema/fixture/validator/test/workflow/source-map/receipt packet. No gate, branch rule, source, lifecycle record, release, deployment, cache, or public artifact requires restoration because the profile has no operational adapter or authority.

<p align="right"><a href="#top">Back to top</a></p>
