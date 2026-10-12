<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/trust-spine-fixture-slice/v1
title: MRTS-05 Deterministic Trust-Spine Fixture Slice
type: semantic-contract
version: v1.0.0
status: proposed; fixture-only; no-network; non-authoritative
owner: OWNER_TBD — Governance steward · Evidence steward · Release steward · Validation steward
created: 2026-08-22
updated: 2026-08-22
policy_label: internal-governance; synthetic-fixture; public-safe; no-publication
owning_root: contracts/
responsibility: bounded cross-family fixture manifest, deterministic reference closure, negative-case polarity, and offline release-candidate dry-run semantics without selecting conflicted candidates or creating source, policy, review, lifecycle, release, or publication authority
truth_posture: CONFIRMED repository-local candidate schemas, validators, fixtures, hashes, and deterministic local execution / PROPOSED cross-family fixture profile / NEEDS VERIFICATION human review, hosted exact-head execution, and any future production applicability
related:
  - ../../control_plane/object_family_register.yaml
  - ../../docs/doctrine/directory-rules.md
  - ../../fixtures/contracts/v1/governance/trust_spine_fixture_slice/README.md
  - ../../schemas/contracts/v1/governance/trust_spine_fixture_slice.schema.json
  - ../../tools/validators/governance/validate_trust_spine_fixture_slice.py
notes:
  - "A candidate schema pinned for one fixture is not selected as the canonical family authority."
  - "The canonical PolicyDecision vocabulary uses ANSWER for the allow-side outcome; this contract does not invent an ALLOW value."
  - "READY_FOR_REVIEW and APPROVE_READY are dry-run classifications only and never authorize a transition."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MRTS-05 deterministic trust-spine fixture slice

This contract defines one wholly synthetic, public-safe, deterministic, no-network fixture chain from a `SourceDescriptor` candidate through a release-candidate `ProofPack` and explicit `RollbackCard`. It stops before publication and writes no source, lifecycle, review, release, or public state.

## Candidate-binding posture

The object-family register records unresolved candidate conflicts for several families. This slice therefore pins one existing schema per fixture object and labels that choice `CONFLICTED_CANDIDATE_PIN` or `SINGLE_SURFACE_FIXTURE_PIN`. Passing the slice cannot settle a conflict, rename a family, or move an authority surface.

| Family | Fixture role | Candidate posture |
|---|---|---|
| SourceDescriptor | Synthetic source identity and public-safe rights context | Conflict preserved |
| SourceActivationDecision | Fixture-only admission route; `source_activated=false` | Conflict preserved |
| EvidenceRef / EvidenceBundle | Exact reference and digest closure | Partial / conflict preserved |
| PolicyDecision | Canonical `ANSWER` allow-side plus canonical `DENY` negative case | Conflict preserved |
| ValidationReport / RunReceipt | Validation and execution references | Conflict preserved |
| PromotionReceipt | Seven PASS gates with `transition.applied=false` | Single-surface fixture pin |
| ReleaseManifest | Inactive candidate with all governance flags false | Conflict preserved |
| ProofPack | Eleven component kinds with local SHA-256 replay | Single-surface fixture pin |
| RollbackCard | Explicit affected release and distinct prior target | Single-surface fixture pin |

## Required closure

The validator enforces nineteen cross-family links. These include descriptor identity and byte digest, activation policy, EvidenceRef-to-bundle resolution, bundle/run source links, validation-report linkage, promotion evidence and policy support, release references to source/evidence/policy/run/promotion/proof/rollback, ProofPack release and component-digest binding, and a distinct rollback target.

The successful dry-run path composes two existing repository lanes:

1. Offline promotion-verification execution must report `PASS` and `APPROVE_READY` while every authority flag remains false.
2. The publication-deny dry run must pass all five denial mutations with `publication_created=false` and `network_used=false`.

The combined result is `READY_FOR_REVIEW` and `publication_outcome=NOT_ATTEMPTED`, not approval or release.

## Negative matrix

Thirteen deterministic mutations must fail with exact bounded codes:

| Case | Required result |
|---|---|
| Missing source identity | `SOURCE_IDENTITY_MISSING` |
| Unknown rights or non-public sensitivity | `RIGHTS_OR_SENSITIVITY_UNKNOWN` |
| Unresolved EvidenceRef | `EVIDENCE_REF_UNRESOLVED` |
| Schema mismatch | `SCHEMA_MISMATCH` |
| Duplicate object ID | `DUPLICATE_OBJECT_ID` |
| Invalid lifecycle placement | `LIFECYCLE_PLACEMENT_INVALID` |
| Missing receipt | `MISSING_RECEIPT` |
| Incomplete promotion gates | `PROMOTION_GATES_INCOMPLETE` |
| Missing release manifest | `MISSING_RELEASE_MANIFEST` |
| Missing rollback target | `ROLLBACK_TARGET_MISSING` |
| Direct public-path attempt | `DIRECT_PUBLIC_PATH_ATTEMPT` |
| Unauthorized parallel writer | `UNAUTHORIZED_PARALLEL_WRITER` |
| Canonical policy deny | `POLICY_DENIED` |

## Determinism and safety

- Every fixture object, governing reference, and dry-run entrypoint is SHA-256 bound.
- JSON parsing rejects duplicate keys and non-finite numbers.
- Paths must be canonical repository-relative regular files with no symlink component.
- Subprocess commands are constant, bounded, output-captured, and run with `KFM_NO_NETWORK=1`.
- Repeated CLI executions must produce identical bytes.
- Logs contain only stable codes and lane names, not attacker-controlled values.

## Run

```bash
make trust-spine-fixture-slice
```

## Non-effects

A passing result does not activate or admit a live source, authenticate evidence, approve a policy or review, mutate lifecycle state, assemble a production release, verify external signatures, authorize promotion, deploy, publish, or create a public route. It also does not replace any canonical object-family contract or schema.

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert the fixture packet, validator, tests, workflow, registry entry, Make target, and generated receipt together. Never reinterpret fixture receipts as production evidence.

[Back to top](#top)
