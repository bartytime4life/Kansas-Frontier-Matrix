<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-redaction-src-redaction-readme
title: Redaction Import Namespace README
type: readme
version: v1
status: draft
owners: OWNER_TBD
created: NEEDS VERIFICATION — target file existed before this repair but contained only placeholder text
updated: 2026-07-19
policy_label: public
related: [packages/redaction/README.md, packages/redaction/src/README.md, packages/redaction/pyproject.toml, packages/redaction/src/redaction/__init__.py, packages/redaction/src/redaction/core.py, docs/doctrine/directory-rules.md, docs/standards/REDACTION_DETERMINISM.md, contracts/shared/redaction_receipt.md, schemas/contracts/v1/receipts/redaction_receipt.schema.json, policy/redaction/profiles.yaml, docs/registers/DRIFT_REGISTER.md]
tags: [kfm, packages, redaction, import-namespace, privacy, sensitivity, geoprivacy, deterministic-transform, fail-closed]
notes: ["Repository-grounded namespace guide for the current greenfield redaction package scaffold.", "The package distribution is declared as kfm-redaction version 0.0.0; the redaction namespace exists, __init__.py is empty, and core.py remains a one-line greenfield placeholder at the recorded evidence snapshot.", "This namespace is not policy, schema, contract, receipt, proof, release, publication, API, UI, source, or evidence authority."]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `redaction` import namespace

`packages/redaction/src/redaction/` is the Python namespace reserved for reusable, deterministic redaction and public-safe transformation helpers.

> [!IMPORTANT]
> **Document lifecycle:** draft
> **Component maturity:** experimental greenfield scaffold
> **Evidence snapshot:** `main@aebbca0f18fe8cd907b36b267cc5372a636830d8`
> **Distribution metadata:** `kfm-redaction` version `0.0.0`
> **Namespace:** `redaction`
> **Confirmed exports:** none
> **Confirmed runtime behavior:** none; `core.py` is a placeholder
> **Authority boundary:** helper implementation only; no policy, schema, contract, receipt, proof, release, publication, or public-interface authority

## Purpose

This README defines the bounded context and admission rules for code that may eventually implement KFM redaction, masking, suppression, withholding, aggregation, and spatial generalization.

The namespace is intentionally subordinate to:

- policy decisions and sensitivity obligations;
- semantic contracts and machine schemas;
- evidence, rights, consent, and review state;
- receipt, proof, correction, rollback, and release workflows;
- governed API envelopes and released public-safe artifacts.

A function in this namespace may execute an already-authorized transform. It must not decide whether a person, place, record, geometry, claim, or dataset is eligible for release.

## Current repository state

The package is present as a scaffold, not as a working redaction library.

| Surface | Confirmed repository state | What it does not prove |
| --- | --- | --- |
| `packages/redaction/pyproject.toml` | Declares project name `kfm-redaction` and version `0.0.0`; the file identifies itself as a greenfield placeholder. | Installability, dependencies, build backend, supported Python version, entry points, or release readiness. |
| `packages/redaction/src/redaction/__init__.py` | Exists and is empty. | A supported public API or intentional export set. |
| `packages/redaction/src/redaction/core.py` | Contains only `# redaction core — greenfield placeholder`. | Redaction, validation, replay, policy integration, or deterministic behavior. |
| This README | Documents the intended boundary and current evidence. | Executable enforcement, runtime safety, or publication approval. |

The directly inspected namespace files are:

```text
packages/redaction/src/redaction/
├── README.md
├── __init__.py        # empty at the evidence snapshot
└── core.py            # one-line greenfield placeholder
```

This is a bounded direct-read inventory, not proof that an unindexed or later file cannot exist. Re-inspect the target ref before relying on it.

## Repository fit

Directory Rules place reusable implementation libraries under `packages/`. A package must be reusable; one-off workflow logic belongs under `tools/` or `pipelines/`.

```text
packages/
└── redaction/
    ├── README.md
    ├── pyproject.toml
    └── src/
        ├── README.md
        └── redaction/
            ├── README.md
            ├── __init__.py
            └── core.py
```

| Responsibility | Canonical owner | Namespace boundary |
| --- | --- | --- |
| Redaction helper implementation | `packages/redaction/src/redaction/` | Pure or tightly bounded reusable transforms only. |
| Policy and sensitivity decisions | `policy/` and policy-runtime surfaces | Select obligations, deny, abstain, restrict, or require review. |
| Semantic meaning | `contracts/` | Defines object and receipt semantics. |
| Machine-checkable shape | `schemas/contracts/v1/` | Defines accepted fields, constraints, and versions. |
| Tests and fixtures | `tests/` and `fixtures/` | Prove positive and negative behavior with synthetic data. |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Persist separately auditable trust artifacts. |
| Release, correction, and rollback decisions | `release/` and governed release workflows | Authorize or reverse publication state. |
| Public API and UI behavior | Governed application surfaces | Consume released public-safe outputs; never treat this package as a public authority. |

> [!WARNING]
> Client-side hiding is not redaction. Restricted fields or geometry must be transformed, generalized, withheld, or denied before a public or semi-public representation is emitted.

## Authority boundaries

### This namespace may eventually

Subject to accepted contracts, schemas, policy bindings, fixtures, and tests, this namespace may implement:

- deterministic field removal, masking, bucketing, or replacement;
- deterministic geometry generalization, aggregation, clipping, or simplification;
- suppression, withholding, and public-safe derivative construction;
- replay-safe transform metadata and digest calculation;
- validation of caller-supplied obligations and transform results;
- adapters that return explicit, typed outcomes to governed callers.

These are **PROPOSED capability families**, not confirmed modules, functions, exports, or runtime behavior.

### This namespace must not

- evaluate policy or classify sensitivity as authority;
- select a release audience or approve public access;
- fetch source records or access source credentials;
- read directly from RAW, WORK, QUARANTINE, or unpublished candidate stores;
- persist canonical data, receipts, proofs, evidence bundles, catalogs, or release manifests;
- create or redefine contracts, schemas, policy profiles, source registries, or lifecycle states;
- expose public routes, render UI, hide disclosure only through styling, or publish map layers;
- invoke a model to infer sensitive truth or use generated language as evidence;
- include real living-person data, DNA or genomic content, protected coordinates, private land details, or restricted source payloads in fixtures;
- report a transform result as proof of truth, evidence closure, admissibility, safety, release, or publication.

## Input contract for future implementations

Future functions should accept explicit values from a governed caller. They must not discover missing authority from ambient state.

| Input family | Expected caller-supplied material | Required posture |
| --- | --- | --- |
| Policy context | Decision reference, obligations, audience class, reason codes, review requirements | Consume; do not reinterpret or replace policy. |
| Transform context | Named method/profile, version, parameters, deterministic seed inputs where permitted | Reject unknown or incomplete definitions. |
| Target context | Explicit field, record, geometry, layer property, or derivative candidate | Operate only on the declared target. |
| Evidence and identity context | Object identifiers, EvidenceRefs, hashes, source/release references | Preserve references; do not fabricate evidence or identity. |
| Sensitivity and rights context | Classification, consent, rights, source-role, or disclosure constraints | Fail closed when required context is absent or conflicted. |
| Correction context | Prior receipt, supersession, withdrawal, rollback, or correction references | Preserve lineage; never silently overwrite history. |

No stable Python data model for these inputs is confirmed in the current package.

## Output contract for future implementations

A mature helper should return a typed transform result to its caller, containing only the information needed for downstream validation and audit.

Candidate output families may include:

- a public-safe derivative or an explicit no-output state;
- the applied transform class and version;
- stable reason codes;
- input and output digests that do not reveal protected content;
- references to the caller-supplied policy decision, evidence, review, and release context;
- replay and correction metadata;
- explicit validation or failure details.

The package must not write a `RedactionReceipt` directly merely because it can prepare receipt-safe metadata. Receipt persistence remains a separate responsibility.

## Finite outcomes and fail-closed behavior

The current package defines no runtime outcome type. Future implementation must align with accepted KFM contracts rather than inventing a private success vocabulary.

The draft redaction-determinism standard uses these verifier outcomes:

| Outcome | Required posture |
| --- | --- |
| `ANSWER` | The bounded verification operation completed and its checks passed. This is not release approval. |
| `ABSTAIN` | Required input or evidence is unavailable; do not guess or emit authoritative output. |
| `DENY` | A policy, profile, digest, parameter, or replay check failed; block the affected candidate. |
| `ERROR` | The verifier or execution environment failed; quarantine or stop safely. |

A review workflow may separately use a governed hold state where policy defines one. This namespace must not silently translate missing context, unsupported methods, validation failure, or execution errors into allow.

## Determinism requirements

Before any transform becomes a supported export, its contract must pin enough information to reproduce and compare the result.

At minimum:

1. The transform has a stable name and version.
2. Canonical input normalization is documented.
3. Seed construction and pseudo-random behavior, when used, are versioned and reproducible.
4. Coordinate reference system, precision, rounding, and geometry serialization are explicit.
5. Identical governed inputs produce identical output bytes or a documented deterministic equivalent.
6. Input and output digests are computed using repository-approved canonicalization.
7. No wall clock, locale, process-global random state, network response, hidden environment value, or model output changes the result.
8. Replay detects profile, parameter, input, output, or implementation drift and fails closed.
9. Test vectors cover cross-run and, where required, cross-language parity.

The current `core.py` placeholder satisfies none of these implementation requirements yet.

## Contract, schema, and policy readiness

The surrounding redaction authority surfaces are also incomplete at the evidence snapshot:

| Surface | Current posture |
| --- | --- |
| Shared `RedactionReceipt` contract | Draft and PROPOSED; defines cross-domain semantics but not package API. |
| Redaction receipt schema | PROPOSED permissive scaffold with no declared properties and no linked contract document. |
| Redaction profile registry | PROPOSED placeholder with no confirmed profiles. |
| Redaction determinism standard | Draft and PROPOSED; concrete byte-level rules require governance acceptance and executable verification. |

Therefore, implementation must not hard-code speculative field names, profile identifiers, receipt shapes, or policy behavior as stable public API.

## Admission gates for a supported export

A new export is ready for review only when all applicable gates are satisfied.

- [ ] A semantic contract defines the transform and its invariants.
- [ ] A machine schema or typed interface defines accepted inputs and outputs.
- [ ] Policy selects or supplies the obligation outside this namespace.
- [ ] The implementation is deterministic and no-network by default.
- [ ] Valid, invalid, denied, abstained, and error fixtures are synthetic and public-safe.
- [ ] Unit tests cover every branch and negative path.
- [ ] Replay tests detect input, parameter, profile, output, and implementation drift.
- [ ] Sensitive details and reversal-enabling secrets are absent from outputs, logs, errors, and fixtures.
- [ ] Receipt-safe metadata is separated from receipt persistence.
- [ ] Package metadata declares the build backend, Python compatibility, dependencies, and included packages.
- [ ] `__init__.py` exports are explicit, minimal, documented, and covered by compatibility tests.
- [ ] Repository-native validation and applicable CI checks pass.
- [ ] Human review is complete for policy- or sensitivity-significant behavior.

Until then, keep the export private or leave the implementation in scaffold state.

## Development rules

1. Keep functions pure where practical and make every external dependency explicit.
2. Keep the namespace no-network by default.
3. Reject missing, unknown, malformed, conflicted, or unsupported obligations.
4. Preserve caller-supplied policy, evidence, identity, review, correction, rollback, and release references.
5. Never log or return protected input merely to improve debugging.
6. Never use a UI filter, map style, or client-side omission as the only disclosure control.
7. Keep domain-specific sensitivity rules in their policy and domain authority homes.
8. Keep fixtures synthetic, minimized, sanitized, and safe for a public repository.
9. Use explicit types and stable reason codes instead of booleans or warning-only failure.
10. Treat every redacted derivative as a representation candidate, not canonical exact truth.
11. Do not add dependencies, cryptographic choices, profile names, or transform algorithms without repository evidence and review.
12. Update this README when supported exports, package metadata, tests, schemas, profiles, or runtime behavior change.

## Validation

### Current evidence checks

At the recorded snapshot:

- project metadata declares `kfm-redaction` version `0.0.0`;
- the import namespace directory and empty `__init__.py` exist;
- `core.py` remains a one-line placeholder;
- no supported export or caller was established by the bounded repository search;
- the shared receipt contract, receipt schema, profile registry, and determinism standard remain draft or PROPOSED.

These observations do not substitute for repository-native execution.

### Checks required after implementation begins

Use repository-native commands when they are established. Bounded checks may include:

```bash
python -m compileall -q packages/redaction/src/redaction

PYTHONPATH=packages/redaction/src \
python -c "import redaction; print(redaction.__file__)"

git grep -n \
  -e "from redaction" \
  -e "import redaction" \
  -- packages apps pipelines tools tests

git diff --check
```

Do not add a `pip install` or package-build instruction until `pyproject.toml` defines a complete, verified build configuration.

## Evidence boundary

| Evidence | Truth status | Supports | Does not prove |
| --- | --- | --- | --- |
| `packages/redaction/pyproject.toml` at the recorded snapshot | CONFIRMED | Distribution name, version, and placeholder status. | Installability or runtime maturity. |
| `packages/redaction/src/redaction/__init__.py` | CONFIRMED | Namespace initializer exists and is empty. | Supported exports. |
| `packages/redaction/src/redaction/core.py` | CONFIRMED | Only a greenfield placeholder is present. | Any transform behavior. |
| Directory Rules §7.2 | CONFIRMED doctrine | `packages/` owns reusable shared libraries. | That this package is implemented correctly. |
| Shared `RedactionReceipt` contract | CONFIRMED file; PROPOSED semantics | Intended cross-domain receipt boundary. | Accepted machine shape, policy approval, or persistence behavior. |
| Redaction receipt schema | CONFIRMED scaffold; PROPOSED | A schema path exists. | Field validation; the scaffold is permissive and empty. |
| Redaction profile registry | CONFIRMED placeholder; PROPOSED | A registry path exists. | Any accepted profile or executable policy behavior. |
| Redaction determinism standard | CONFIRMED document; PROPOSED concrete rules | Intended determinism and replay burden. | Accepted algorithm or passing test vectors. |
| Bounded repository search | CONFIRMED search performed | No caller or additional implementation surface was established by the inspected index. | Global absence, later changes, unindexed content, runtime use, or branch protection. |

## Related documentation

- [Redaction package boundary](../../README.md)
- [Redaction source envelope](../README.md)
- [`packages/` shared-library rules](../../../README.md)
- [Directory Rules](../../../../docs/doctrine/directory-rules.md)
- [Redaction determinism standard](../../../../docs/standards/REDACTION_DETERMINISM.md)
- [Shared `RedactionReceipt` contract](../../../../contracts/shared/redaction_receipt.md)
- [Redaction receipt schema scaffold](../../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json)
- [Redaction profile registry placeholder](../../../../policy/redaction/profiles.yaml)
- [Repository drift register](../../../../docs/registers/DRIFT_REGISTER.md)

## Rollback

This documentation change is reversible by reverting its implementation commit or closing the unmerged review pull request.

Rollback of this README does not roll back data, policy, receipts, proofs, releases, or publication because this change performs none of those actions. If future code causes authority drift, sensitive disclosure, nondeterminism, or an unsafe allow path, revert the code change, preserve the audit trail, quarantine affected candidates, and record the conflict in the appropriate drift, correction, or rollback surface.
