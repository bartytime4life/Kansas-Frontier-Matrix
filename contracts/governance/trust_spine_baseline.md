<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/trust-spine-baseline/v1
title: Trust Spine Authority Baseline Contract
version: v1.0.0
type: semantic-contract
status: proposed; repository-grounded; implementation-partial; non-authoritative
owners: Control-plane steward; Architecture steward; Validation/CI steward
created: 2026-08-22
updated: 2026-08-22
responsibility_root: contracts/
owning_root: contracts/
responsibility: define the bounded semantics of a pinned repository authority and implementation evidence projection without creating authority accepting decisions waiving drift activating sources or changing lifecycle release deployment promotion publication or public-runtime state
policy_label: internal-governance; cite-or-abstain; no-self-authority; no-network-validation
truth_posture: CONFIRMED pinned main adopted Directory Rules accepted ADR inventory declared root registry observed control-plane files focused validation results current object-family coverage milestone issues and inherited topology findings / PROPOSED this contract schema validator fixtures workflow and baseline projection / UNKNOWN deployed consumers branch-protection enforcement production behavior and independent review / NEEDS VERIFICATION steward adoption and hosted exact-head results
related:
  - ../../control_plane/trust_spine_baseline.yaml
  - ../../schemas/contracts/v1/governance/trust_spine_baseline.schema.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../tools/validators/control_plane/validate_trust_spine_baseline.py
  - ../../fixtures/contracts/v1/governance/trust_spine_baseline/README.md
  - ../../tests/validators/test_validate_trust_spine_baseline.py
  - ../../.github/workflows/trust-spine-baseline.yml
notes:
  - This contract implements the MRTS-01 baseline slice for milestone KFM-MS-MRTS-001.
  - It does not complete MRTS-02 through MRTS-06.
  - It does not create authority, accept an ADR, waive drift, activate a source, or change release state.
[/KFM_META_BLOCK_V2] -->

# Trust Spine Authority Baseline Contract

## Purpose

The trust-spine baseline is a pinned, machine-readable observation of the repository state used to start milestone `KFM-MS-MRTS-001`. It makes the implementation starting point reviewable without turning an inventory into authority.

The canonical instance is [`control_plane/trust_spine_baseline.yaml`](../../control_plane/trust_spine_baseline.yaml). The `.yaml` file deliberately uses the JSON-compatible subset of YAML so parsing is deterministic, duplicate-key rejection is possible, and no YAML loader is required.

## Authority boundary

The baseline may cite an authority; it cannot create one.

| Question | Owning authority | Baseline role |
| --- | --- | --- |
| Where a repository artifact belongs | Adopted Directory Rules and accepted placement ADRs | Pin path, digest, and observed status |
| What an object means | `contracts/` | Report whether a contract surface was observed |
| What shape an object has | `schemas/` | Report whether a schema surface was observed |
| What is allowed or denied | `policy/` plus a valid policy decision | Report references and unresolved state only |
| What evidence proves | Evidence and proof objects | Record bounded validation observations, never truth promotion |
| What is released, corrected, withdrawn, or rolled back | `release/` | Report coverage only; no lifecycle mutation |
| What is deployed or public | Governed runtime and released artifacts | Not established by this projection |

An accepted ADR is still not proof that its described implementation exists. The `implementation_status` field records the bounded repository observation separately from ADR decision status.

## Required identity and base

Every instance must declare:

- schema version `1.0.0`;
- a stable `snapshot_id`;
- repository `bartytime4life/Kansas-Frontier-Matrix`;
- `projection_status: PROPOSED` and `implementation_status: PARTIAL`;
- `authority_mode: evidence_projection_only`;
- an RFC 3339 observation timestamp;
- the exact 40-character base commit, branch, milestone identity, and observed open pull-request numbers.

The pinned base must resolve to a local Git commit during current-instance validation. It need not equal the pull request head: the baseline intentionally describes the pre-change starting point. Referenced paths and digests are replayed from that pinned Git tree, not from mutable working-tree bytes, so a later same-path forward correction cannot rewrite the historical observation.

## Evidence sections

### Authority snapshot

`authority_snapshot` separates three kinds of record:

1. the adopted Directory Rules document, its content digest, and accepting ADR;
2. every accepted numbered ADR observed in the canonical ADR index, including whether it is relevant to this milestone;
3. proposed ADRs whose subjects overlap the milestone but remain unresolved authority candidates.

Candidates must remain `PROPOSED`. Listing them does not accept them.

### Repository roots

`repository_roots` pins the existing root registry, its digest, class counts, present-root count, and unresolved root conditions. Class counts must sum to the declared root count. A conditional absent root is not silently treated as implemented.

### Control-plane projections

`control_plane_projections` inventories observed register and projection files. Each entry contains a stable ID, canonical repository-relative path, SHA-256 digest, implementation status, and the exact validation state observed for that bounded surface.

`PASS` means only that the named validation profile passed. It does not imply complete population or cross-register semantic closure.

### Trust-object catalog

`trust_object_catalog` records the sixteen object families required by the milestone and separates:

- required families already registered;
- required families not yet registered;
- other families already present in the object-family register.

Counts must reconcile with their arrays. The three arrays must be sorted, unique, and disjoint. This section remains `PARTIAL` while any required family is unregistered.

### Validation observations

Each observation declares the exact command, execution state, outcome, implementation status, and bounded scope. A result may be recorded as `PASS` or `FAIL` only when the command was executed.

An inherited failure remains a failure. In particular, a nonzero `fail_invariant` or `fail_new_drift` count cannot be represented as `PASS`. This slice does not expand the topology baseline to manufacture a green result.

### Overlap and unresolved work

`overlap` records the milestone issues, related issues, and open pull requests observed at the pinned base. `unresolved_items` records material gaps that prevent a complete milestone claim.

These lists are review aids. They do not reserve paths, assign ownership, close issues, or establish merge authority.

## Status vocabulary

The implementation vocabulary is closed:

- `IMPLEMENTED`
- `PARTIAL`
- `ABSENT`
- `SUPERSEDED`
- `CONFLICTED`
- `DEPRECATED`
- `NOT_INSPECTED`

Validation outcomes are also closed: `PASS`, `FAIL`, `NOT_RUN`, `SKIPPED`, `HOLD`, and `UNKNOWN`.

Do not translate uncertainty into success. `NOT_INSPECTED`, `NOT_RUN`, and `UNKNOWN` are first-class states.

## Deterministic validation

Run the repository-native profile:

```bash
make trust-spine-baseline
```

The profile performs:

1. Draft 2020-12 schema validation;
2. duplicate-key and non-finite-number rejection;
3. canonical ordering, uniqueness, count, and cross-field checks;
4. repository-relative path containment and existence checks;
5. SHA-256 replay against referenced bytes in the declared base commit for the canonical instance;
6. pinned Git commit and blob existence checking for the canonical instance;
7. exact valid/invalid fixture polarity;
8. focused no-network unit tests;
9. generated authoring-receipt integrity validation.

After declared Python dependencies are installed, the validator and tests make no network calls. A green workflow proves only this bounded contract.

## Failure and correction rules

The validator fails closed when:

- JSON-compatible parsing fails or duplicate keys/non-finite values appear;
- schema constraints fail;
- IDs, paths, family names, or issue numbers are not sorted and unique;
- declared counts do not reconcile;
- referenced paths escape the repository, do not exist in the validation target (the pinned Git tree for the canonical instance), or differ from their pinned digests;
- an unexecuted command claims `PASS` or `FAIL`;
- topology failure counts are presented as a pass;
- a required non-effect is removed;
- the pinned base commit cannot be resolved locally.

Corrections use a same-path forward fix or a Git revert to the pinned base. Receipts are append-only process memory; they do not overwrite prior evidence or grant review authority.

## Non-effects

Creation or validation of this packet:

- does not create governance, contract, schema, policy, evidence, review, or release authority;
- does not accept or supersede an ADR;
- does not activate a source or admit data;
- does not move an artifact through lifecycle phases;
- does not expand or waive the topology drift baseline;
- does not approve human review;
- does not release, deploy, promote, or publish anything;
- does not prove public or production runtime behavior.

## Milestone relationship

This contract closes only the implementation portion of `MRTS-01` once reviewed and merged. It intentionally exposes dependency work for `MRTS-02` through `MRTS-06`: registry normalization, trust-object catalog reconciliation, validators and drift ratchets, a deterministic trust-spine proof slice, and CI conformance/rollback handoff.
