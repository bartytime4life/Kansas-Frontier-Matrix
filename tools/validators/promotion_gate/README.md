<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-promotion-gate-readme
title: tools/validators/promotion_gate README
type: README
version: v1.1.0
status: implemented; bounded-readiness-validator; no-network; non-publisher
owners: OWNER_TBD - Tooling/QA owner; promotion steward; release steward; policy steward; evidence steward; review steward; rollback steward
created: 2026-07-08
updated: 2026-08-03
policy_label: repository-facing; promotion-gate; fail-closed; public-safe-fixtures; non-authoritative
owning_root: tools/
responsibility: Own the bounded executable that checks declared promotion-packet closure and emits deterministic readiness findings while deferring contracts, schemas, policy, evidence, receipts, proofs, review authority, release records, rollback execution, lifecycle state, and publication to their owning roots.
truth_posture: cite-or-abstain; implementation claims require current repository evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../release/README.md
  - ../../../contracts/release/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../policy/promotion/README.md
  - ../../../fixtures/release/promotion_gate/README.md
  - ../validate_review_record.py
  - ../../../tests/release/test_review_record.py
  - ../../../tests/release/test_promotion_gate.py
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/publication/promotion-gates.md
  - ../../../.github/workflows/promotion-gate.yml
notes:
  - "PASS means APPROVE_READY for accountable release review only; it is not a PromotionDecision, release, publication, or public-surface permission."
  - "Gate G now composes a fixture-only ReviewRecord projection with synthetic actor identity and authority declarations; it does not authenticate live identities, assignments, or review records."
  - "The implementation uses only the Python standard library and the repository bounded-JSON helper; it performs no network access and writes no artifact."
[/KFM_META_BLOCK_V2] -->

# Promotion-gate readiness validator

> **One-line purpose.** Evaluate a declared `CATALOG`/`TRIPLET` to `PUBLISHED`
> promotion packet through seven fail-closed readiness gates without promoting,
> releasing, publishing, signing, or mutating anything.

## Status

| Surface | Current status | Boundary |
|---|---|---|
| `validate_promotion_gate.py` | **CONFIRMED executable** | Emits finite JSON findings and exit codes; no writes or network. |
| `../validate_promotion_gate.py` | **CONFIRMED compatibility entry point** | Preserves the pre-existing flat command path. |
| `../validate_review_record.py` | **CONFIRMED fixture-only validator** | Checks ReviewRecord shape, actor identity/authority binding, freshness, supersession, scope, subject, and hash binding without resolving live records. |
| `fixtures/release/promotion_gate/` | **CONFIRMED synthetic matrix** | One `PASS`, eleven `DENY`, two `ABSTAIN`, and two `ERROR` files. |
| `tests/release/test_review_record.py` and `test_promotion_gate.py` | **CONFIRMED focused tests** | Exact ReviewRecord and A-G outcomes, precedence, parser, CLI, deterministic-output, non-emission, and no-network behavior. |
| `make publish-check` | **CONFIRMED executable target** | Runs the fixture matrix and focused standard-library suite. |
| `.github/workflows/promotion-gate.yml` | **CONFIRMED orchestration** | Runs the bounded fixture-only review and A-G gates while retaining the governed-record and hydrology-promoter holds. |
| Policy Rego stubs | **NEEDS VERIFICATION / not executed here** | Declared `policy_context.evaluation` is checked; actual policy evaluation remains policy-owned. |
| Evidence, attestation, catalog, review, rollback, and correction resolution | **NEEDS VERIFICATION** | References are syntactically present and cross-field declarations agree; authenticity and authority are not established. |

## Directory Rules basis

The executable belongs under `tools/validators/` because its authority owner is
repository validation. The existing flat file remains a compatibility wrapper;
the implementation lives in the established `promotion_gate/` specialization.
Synthetic reusable inputs remain in `fixtures/`, enforceability in `tests/`, and
workflow orchestration in `.github/workflows/`.

This lane does not own:

- release object meaning (`contracts/release/`);
- machine schemas (`schemas/contracts/v1/release/`);
- allow/deny policy (`policy/promotion/`, `policy/release/`);
- evidence, proofs, or receipts (`data/` trust-artifact lanes);
- review or release records (`release/`);
- rollback execution or lifecycle mutation; or
- public API, UI, map, export, or AI behavior.

No new responsibility root, release state, or object-family authority is created.

## Input profile

The command accepts bounded, duplicate-free UTF-8 JSON. The profile is a
validator input, not a new release record type.

| Field | Gate | Declared meaning |
|---|:---:|---|
| `profile_version`, `candidate_id`, `candidate_author`, `spec_hash` | A | Stable candidate identity for this evaluation. |
| `gate_evaluated_at` | D/G | Fixed UTC instant for deterministic review-freshness evaluation; never wall-clock time. |
| `lifecycle` | A | Exact declared boundary: `CATALOG` or `TRIPLET` to `PUBLISHED`. |
| `release_manifest` | A/B | Minimal manifest identity, spec hash, and declared artifact digests. |
| `run_receipt` | B/F | Minimal process-memory identity, spec hash, and output digests. |
| `geometry` | C | Declared validity, deterministic processing, CRS, and bounded bbox. |
| `temporal` | D | Real UTC-second start/end interval. |
| `policy_context` | E | Profile, labels, policy result, and bundle reference supplied by the policy lane. |
| `evidence_refs`, `attestation_refs`, `catalog_refs` | F | Declared proof and STAC/DCAT/PROV closure references. |
| `review` | G | Fixture-only ReviewRecord shape plus author/reviewer IdentityToken projections, StewardshipAssignment projection, freshness/supersession, scope/subject, and spec/artifact bindings. |
| `rollback`, `correction` | G | Prior target and correction linkage. |
| `ai_mediation` | F | Conditional AI receipt when model mediation affected the candidate. |

Unknown fields fail closed. Diagnostics contain only a stable code, gate, JSON
parent path, and status; candidate values and untrusted field names are never
echoed. An undeclared nested field is attributed to its owning A-G gate.

## Gates

| Gate | Name | Checks | Failure posture |
|:---:|---|---|---|
| A | Identity and closure | Profile, candidate, author, hash, lifecycle boundary, manifest identity. | `DENY` on missing or contradictory identity. |
| B | Asset integrity | Candidate/manifest/receipt hash agreement; non-empty unique digest-set equality. | `DENY` on mismatch or invalid digest. |
| C | Geometry and CRS | Declared validity, deterministic processing, `EPSG:4326`, ordered finite world bbox. | `DENY` on invalid or nondeterministic geometry. |
| D | Temporal semantics | Strict real UTC seconds, `start <= end`, and a declared gate-evaluation instant. | `DENY` on malformed or inverted time. |
| E | Rights/sensitivity policy context | Known profile/labels, public-safe label discipline, finite policy evaluation. | `DENY` on policy rejection; `ERROR` on evaluator failure. |
| F | Proof and catalog support | Evidence, attestation, STAC/DCAT/PROV, run receipt, conditional AI receipt. | `ABSTAIN` for unresolved evidence; `DENY` for mandatory integrity/catalog gaps. |
| G | Review and rollback | Fixture-only ReviewRecord shape; actor identity and authority; separation, freshness, supersession, scope, subject, hash binding; rollback and correction linkage. | `DENY` on unsafe or contradictory declarations; `ABSTAIN` on missing authority or correction lineage. |

The validator checks what the packet declares. It does not dereference a URI,
authenticate an actor or authority assignment, verify DSSE/cosign, evaluate Rego, prove rights or
sensitivity clearance, resolve an EvidenceBundle, or inspect a public surface.

## Finite results and exit codes

| Status | Meaning | Exit |
|---|---|---:|
| `PASS` | Every bounded gate passed; output readiness is `APPROVE_READY`. | `0` |
| `ABSTAIN` | Support is insufficient without a contradictory unsafe claim. | `1` |
| `DENY` | A mandatory, unsafe, or contradictory condition blocks readiness. | `1` |
| `ERROR` | Input or policy evaluation could not be completed safely. | `2` |

Precedence is `ERROR > DENY > ABSTAIN > PASS`. Every non-`PASS` result has
`readiness: BLOCKED`. `PASS` never emits or implies `APPROVE`, `PROMOTED`,
`PUBLISHED`, or `RELEASED`.

## Commands

Run the complete local proof:

```bash
make publish-check
```

Run only the repository matrix:

```bash
python tools/validators/validate_promotion_gate.py --fixtures
python tools/validators/validate_review_record.py --fixtures
```

Evaluate explicit packets:

```bash
python tools/validators/validate_promotion_gate.py candidate.json
```

Each explicit input produces one compact deterministic JSON line. Multiple
files are sorted by path. No report, receipt, proof, decision, or release record
is written.

## Fixture and test coverage

The checked-in matrix covers:

- complete declared closure;
- missing candidate identity;
- manifest/receipt artifact disagreement;
- invalid geometry;
- unknown policy label;
- missing approval;
- missing actor authority;
- self-review;
- stale or superseded review;
- review scope mismatch;
- unbound specification or artifact hashes;
- missing evidence support;
- policy-evaluator error; and
- malformed JSON.

Focused unit tests additionally cover conditional AI receipts, correction
lineage, finite-outcome precedence, equal temporal boundaries, impossible calendar
timestamps, duplicate keys, non-echoing diagnostics, deterministic CLI output,
gate-local unknown-field handling, exit-code polarity, and network denial.

## What a pass proves

A pass proves only that the bounded validator executed over the declared packet
and found no condition in its current profile. It does not prove:

- source authority, rights, sensitivity clearance, or evidence truth;
- that a referenced object exists, is authentic, or is current;
- that policy or review authority is valid;
- cryptographic signature or transparency-log verification;
- release manifest completeness outside the minimal profile;
- actual rollback readiness or correction propagation;
- promotion, release, deployment, publication, or public-serving behavior; or
- that a workflow is required by repository settings.

## Compatibility and rollback

The pre-existing flat entry point is preserved. Workflow name `promotion-gate`
and its job identities remain stable. The feature adds no dependency, database,
migration, external service, credential, or data-source access.

Before merge, close the draft PR and remove only its scoped branch. After merge,
revert the feature commit through a reviewed PR. That restores the prior
placeholder and TODO target without rewriting history or changing release or
publication state.

## Changelog

| Date | Change | Result |
|---|---|---|
| 2026-07-08 | Replaced an empty placeholder with validator-routing documentation. | README-only; implementation unverified. |
| 2026-08-02 | Added bounded A-G readiness implementation, fixture matrix, focused tests, Make target, and CI wiring. | Executable no-network proof; non-publisher. |
| 2026-08-03 | Added fixture-only ReviewRecord, actor-authority, freshness, supersession, scope, and hash-binding checks to Gate G. | Review declarations fail closed without creating review or release authority. |
