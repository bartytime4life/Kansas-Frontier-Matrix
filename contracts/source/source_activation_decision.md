<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-activation-decision
title: SourceActivationDecision Contract
type: semantic-contract; source-admission-decision; pre-raw
version: v0.1.0
status: proposed; fixture-first; no-network; non-operational
owners: OWNER_TBD — Source steward · Rights steward · Sensitivity steward · Policy steward · Contract steward · Schema steward · Validation steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public; source; admission; pre-raw; fail-closed; no-public-authority
related:
  - ./README.md
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../policy/intake/README.md
  - ../../schemas/contracts/v1/source/source_activation_decision.schema.json
  - ../../fixtures/contracts/v1/source/source_activation_decision/
  - ../../tools/validators/validate_source_activation_decision.py
  - ../../tests/validators/test_validate_source_activation_decision.py
tags: [kfm, source-activation-decision, source-admission, pre-raw, rights, sensitivity, quarantine, fixture-first]
notes:
  - "This profile implements bounded shape and consistency checks only. ADR-0017 remains proposed."
  - "It activates no source, evaluates no live policy bundle, writes no lifecycle state, and grants no public-use or release authority."
  - "Existing non-schema placeholder files named source-activation-decision.json remain non-authoritative compatibility artifacts pending a separate placement decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceActivationDecision

> `SourceActivationDecision` is the proposed pre-RAW gate record that composes an explicit `SourceDescriptor` posture, bounded policy references, review posture, finite intake route, obligations, timing, and lineage into one operation-specific decision. It records how a source may be treated for one activation or re-admission operation. It does not make the source true, accepted doctrine, released, published, or safe for public use.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED` / fixture-first / no-network |
| Owning semantic lane | `contracts/source/` |
| Machine shape | `schemas/contracts/v1/source/source_activation_decision.schema.json` |
| Decision scope | One source activation, re-admission, scope-change, deactivation, or retirement operation |
| Public-use posture | Fixed to `false` |
| Release posture | `release_ref` fixed to `null` |
| Runtime/source activation | Not implemented or authorized by this profile |
| Governing ADR | ADR-0017 remains `proposed`; this profile does not accept it |

This slice converts a documented gap into reviewable repository state without claiming an operational source-admission engine. A schema-valid decision is still only a proposed record. It does not authenticate referenced policy decisions or reviews, mutate a source registry, enable a connector, persist RAW or QUARANTINE data, or approve release.

## Bounded context

The contract belongs to the source-admission bounded context:

```text
SourceDescriptor
  + rights / sensitivity / access posture
  + policy and review references
  + requested operation
  -> SourceActivationDecision
  -> proposed route:
       ADMIT_TO_RAW | QUARANTINE | DENY_INTAKE | HOLD | ERROR
```

The following remain separate object families:

| Object | Separate responsibility |
|---|---|
| `SourceDescriptor` | Stable source identity, source role, rights, sensitivity, cadence, access, review, registry and release posture |
| `PolicyDecision` | Independent policy-family outcome and obligations |
| `IngestReceipt` | Digest-pinned record of an actual source capture |
| `RunReceipt` | Broader pipeline/runtime stage execution memory |
| `EventRunReceipt` | Future pre-RAW event-family decision record |
| `EvidenceBundle` | Resolved evidence supporting downstream claims |
| `ReleaseManifest` | Release decision and published artifact set |

## Field groups

### Identity and descriptor binding

| Field | Meaning |
|---|---|
| `activation_decision_id` | Stable identity of this exact activation decision record |
| `source_id` | Source identity expected to resolve to a governed SourceDescriptor |
| `source_descriptor_ref` | Version-bound descriptor reference |
| `descriptor_version` | Semantic version of the descriptor record used |
| `source_descriptor_digest` | SHA-256 binding for the descriptor bytes or canonical representation |
| `source_role_ref` | Exact pointer to the declared descriptor's `/source_role` field |
| `operation` | `initial_activation`, `re_admission`, `scope_change`, `deactivation`, or `retirement` |

The dedicated validator requires:

```text
source_descriptor_ref =
  "source-descriptor:" + source_id + ":" + descriptor_version

source_role_ref =
  source_descriptor_ref + "#/source_role"
```

This lexical binding does not resolve or authenticate the descriptor. It prevents the decision from silently referring to one descriptor while claiming the role of another.

### Decision context

`context` copies only policy-significant posture needed to review the decision:

- rights status;
- sensitivity class;
- access posture;
- descriptor review state; and
- source-registry state.

The decision must not infer a more permissive posture than the referenced descriptor. Live runtime reconciliation against actual descriptor bytes remains future work.

### Finite route and activation state

| Route | Meaning | Permitted lifecycle effect |
|---|---|---|
| `ADMIT_TO_RAW` | The bounded operation may proceed under declared obligations | Candidate write to governed RAW only; not promotion or release |
| `QUARANTINE` | Material may be retained only in a governed hold | Governed QUARANTINE route with case and review obligations |
| `DENY_INTAKE` | The evaluated operation is denied | No admitted lifecycle write |
| `HOLD` | A time-bounded steward or external decision is required | No admitted lifecycle write while pending |
| `ERROR` | A trustworthy route could not be computed | No partial admitted state |

`activation_state` uses the existing SourceDescriptor vocabulary:

```text
disabled | fixture_only | live_candidate | live_active | quarantined | retired
```

`activation_scope` is deliberately smaller:

```text
none | fixture_only | metadata_only | raw_capture | quarantine_only
```

A route is operation-specific and time-bounded. It is not permanent source authority.

### Reasons, obligations, policy, and review

- `reason_codes` are stable identifiers that do not embed source values or protected details.
- `obligations` are enforceable requirements on the caller.
- `policy_decision_refs` point to independent decisions; the activation object does not create policy.
- `review_state` and `review_refs` disclose review posture.
- `decision_authority_ref` identifies the declared decision route without proving the actor's authority.

The schema freezes the reason-code and obligation vocabularies used by this proposed profile. Adding or reinterpreting a value is compatibility-significant.

### Timing and lineage

- `created_at` records when the decision record was created.
- `effective_at` records when its operation-specific route takes effect.
- `expires_at` limits any decision with a finite lifetime.
- `hold_expires_at` is mandatory for `HOLD`.
- `supersedes` and `superseded_by` retain append-only decision lineage.

A correction or re-evaluation creates a new decision record. Existing decisions are not edited in place.

## Semantic invariants

The no-network validator enforces:

1. descriptor and source-role references bind exactly to `source_id` and `descriptor_version`;
2. SHA-256 values are not all-zero placeholders;
3. all non-null timestamps carry explicit timezone offsets;
4. `effective_at` does not precede `created_at`;
5. `expires_at` is later than `effective_at`;
6. `hold_expires_at` is later than `created_at`;
7. an activation decision cannot supersede itself;
8. the same decision cannot be both predecessor and successor;
9. `ADMIT_TO_RAW` requires reviewed descriptor posture, policy references, and permitted rights;
10. `raw_capture` requires `live_active`, approved review, review evidence, and `require_ingest_receipt`;
11. fixture-only and metadata-only scopes remain bound to compatible activation states;
12. `QUARANTINE` requires `quarantined`, `quarantine_only`, `route_to_quarantine`, and `open_quarantine_case`;
13. `HOLD` requires pending review, review references, hold expiry, and `set_hold_expiry`;
14. `DENY_INTAKE` and `ERROR` cannot grant a usable activation scope;
15. public use and release remain impossible in this profile.

## Public and lifecycle boundary

A passing decision proves only bounded shape and local cross-field consistency. It does **not**:

- accept ADR-0017;
- authenticate a source steward or policy evaluator;
- resolve SourceDescriptor, PolicyDecision, or ReviewRecord references;
- admit source bytes;
- create an `IngestReceipt`;
- write `data/pre_raw/`, `data/raw/`, or `data/quarantine/`;
- activate a connector or watcher;
- create evidence, proof, catalog, release, or publication state;
- expose the source to a public API, MapLibre, Evidence Drawer, or AI context.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_activation_decision.py' \
  --verbose

python tools/validators/validate_source_activation_decision.py --fixtures

python -m pytest -q tests/schemas/test_common_contracts.py \
  -k source_activation_decision
```

The validator performs no network access. Diagnostics contain codes and JSON pointers, not candidate values.

## Compatibility and rollback

The repository currently contains non-schema placeholder files named `source-activation-decision.json` in source- and receipt-related schema lanes. This profile does not delete, move, or elevate those files. They remain non-authoritative compatibility artifacts pending a separate evidence-backed placement or migration decision.

Before merge, rollback is closing the draft pull request and abandoning its feature branch. After merge, rollback is a reviewed revert or corrective pull request. Preserve any stable decision identifiers and supersession lineage if downstream fixtures or consumers begin using the proposed profile.

[Back to top](#top)
