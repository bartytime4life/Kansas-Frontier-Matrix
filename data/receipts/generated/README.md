<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/generated/readme
name: Generated Work Receipts README
path: data/receipts/generated/README.md
type: data-generated-receipts-lane-readme
version: v0.4.0
status: draft; repository-grounded; implementation-inspected; execution-not-reverified
owners:
  - <receipt-steward>
  - <docs-steward>
  - <validation-steward>
created: 2026-07-17
updated: 2026-09-05
evidence_snapshot: d1b430ca51887777766050e5582659ab34322286
prior_blob: 5a67f8d743306799a014590ccb45fa9f1177f16a
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: generated-receipts
receipt_scope: AI-authored artifact provenance and process memory
path_posture: existing-lane; worktree-and-ancestor-replay-inspected; emitter-automation-needs-verification
sensitivity_posture: receipt-internal; no-public-path; no-secrets; no-hidden-reasoning; process-memory-not-proof; receipt-not-release
related:
  - ../README.md
  - ../../proofs/README.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../CONTRIBUTING.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../../tools/validators/validate_generated_receipt.py
  - ../../../tests/validators/test_validate_generated_receipt.py
tags:
  - kfm
  - data
  - receipts
  - generated-receipt
  - ai-provenance
  - audit
  - cite-or-abstain
  - no-public-path
notes:
  - "This README documents an existing populated lane; it does not certify every pre-existing receipt or prove an emitter is automated."
  - "A generated receipt records provenance for AI-authored work. It is not human approval, factual proof, policy permission, catalog closure, release authority, or publication authority."
  - "v0.2 records the bounded no-network schema, cross-field, local-path, SHA-256-prefix, citation-presence, and optional declared-review-claim validator; BLAKE3 verification remains unsupported without an admitted dependency."
  - "v0.3 documents the one-time, hash-exact Scorecard dependency-lock migration ledger; it does not create a general receipt bypass."
  - "v0.4 documents explicit historical artifact replay and accepted ADR-0029 placement; no historical receipt bytes, review claims, schemas, or validator behavior change."
[/KFM_META_BLOCK_V2] -->

# Generated work receipts

`data/receipts/generated/` stores repository-committed provenance records for AI-authored artifacts. It is a process-memory lane inside `data/receipts/`, not a truth, proof, policy, catalog, release, or public-delivery surface.

## Purpose

Generated receipts make an AI-authored change inspectable by recording the artifacts produced, their content hashes, the model identity, the prompt or contract hash, repository evidence, truth labels, validation gates, citations, and human-review state.

The lane supports review and rollback. It does not make the authored artifacts correct or mergeable by itself.

## Authority level

**Provenance-bearing process memory; non-authoritative for domain truth and release.**

A receipt may show what was authored and which checks were reported. It cannot:

- approve its own artifacts;
- substitute for repository evidence, tests, or reviewer judgment;
- create a policy decision, proof pack, catalog record, release manifest, or publication decision;
- authorize access to sensitive or unreleased material;
- convert generated language into sovereign truth.

Human review remains separate. A receipt whose `human_review.state` is `pending` is not merge authorization.

## Status

Implementation inspection is pinned to
[`main@d1b430ca51887777766050e5582659ab34322286`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/d1b430ca51887777766050e5582659ab34322286).
The sources below establish available code and document contracts, not a fresh
execution of those tools or a complete inventory of receipt payloads.

| Surface | Bounded repository evidence | Status |
|---|---|---|
| Machine shape | The [generated-receipt schema](../../../schemas/contracts/v1/receipts/generated_receipt.schema.json) defines the payload. The [validator](../../../tools/validators/validate_generated_receipt.py) and PR template pin `contract_version` to `3.0.0`. | CONFIRMED source inspection |
| Default validation | The validator checks duplicate-free finite JSON, schema and artifact-map parity, canonical paths, supported SHA-256 bindings, required reference presence, and an optional review claim. | CONFIRMED implementation; execution not reverified here |
| Historical artifact replay | `--artifact-git-ref` selects regular blobs from one exact locally available ancestor commit; the supplied receipt remains the current input file. | CONFIRMED implementation; replay is opt-in |
| Focused tests | [Synthetic validator tests](../../../tests/validators/test_validate_generated_receipt.py) exist. | CONFIRMED test source; NOT RUN for this README review |
| Authoring and PR guidance | [Contributor guidance](../../../CONTRIBUTING.md) and the [PR template](../../../.github/PULL_REQUEST_TEMPLATE.md) govern receipt applicability, final artifact coverage, validation reporting, and separate human review. | CONFIRMED document contracts; not proof of hosted enforcement |
| Generator, emitter automation, complete payload inventory and lane-wide validity | Not established by this focused review. | UNKNOWN / NEEDS VERIFICATION |

**Retained historical observations, not current counts:** earlier README editions
recorded 256 direct-child JSON receipts at
`main@029ed6b66240358aaacc97e0b18ad3f0378b9de1`, a later inspection at
`main@2e31e0cf51c08d792cc1f301ceb21b235424cb40`, and predominant
`genrec-<scope>-<digest>.json` naming. Those observations are preserved as lineage;
they were not re-counted or revalidated in this review and do not establish a
filename requirement.

This update does not retroactively validate, approve, or normalize existing receipts.

## What belongs here

- one bounded JSON provenance record for a related set of AI-authored repository artifacts;
- exact repository-relative artifact paths and content hashes;
- model identity and version information that is available to the emitter;
- a hash of the governing prompt or contract rather than prompt contents or hidden reasoning;
- pinned repository evidence references and per-artifact truth labels;
- validation gates with explicit `PASS`, `FAIL`, or `SKIPPED` outcomes and reasons;
- validated citations, policy-decision references when actually consulted, and human-review state;
- concise notes that preserve limitations, rollback posture, and no-public-authority boundaries.

Receipts should use reproducible artifact identities, remain small and reviewable,
and be safe to commit. Emission timestamps and run identity need not be identical
across runs. Existing filename practice may guide a new name, but the schema and
governing contract control the payload.

`internal-governance` and `no-public-path` describe handling and service boundaries,
not repository access controls. This public repository must not receive confidential
receipt payloads merely because a metadata label calls them internal.

## What does NOT belong here

- prompts, chain-of-thought, hidden reasoning, private review notes, or full tool transcripts;
- credentials, tokens, private keys, connection strings, source-system secrets, or sensitive operational details;
- raw/work/quarantine payloads, exact sensitive locations, living-person private data, or restricted source material;
- model output presented as fact, an EvidenceBundle, a proof pack, a catalog record, or a policy decision;
- release manifests, promotion decisions, correction notices, rollback cards, or published artifacts;
- a receipt that claims a check ran when it was not run, or reports `SKIPPED` work as success;
- duplicate schema, contract, policy, registry, proof, catalog, or release authority.

## Inputs

A generated receipt may derive from:

- the final AI-authored artifact set and its content hashes; prefer full SHA-256 digests for the currently supported integrity check;
- a pinned base commit and repository files inspected as evidence;
- the governing AI build contract and user prompt hash;
- validation commands and their observed outcomes;
- citations that were resolved to exact repository evidence;
- human-review state supplied by an authorized reviewer or review system.

Evidence references should be precise and stable. Unknown parameters should remain
`null` or be omitted when the schema allows; they must not be invented. Required
model-identity strings must explicitly identify unavailable version information
rather than fabricate a model build. The schema permits BLAKE3-shaped digests,
but the current validator rejects BLAKE3 artifact bindings as unsupported.

## Outputs

The output is a JSON object conforming to `generated_receipt.schema.json`. Required fields include:

- `receipt_id`, `contract_version`, `artifact_paths`, and `artifact_hashes`;
- `model_identity`, `prompt_or_contract`, `parameters`, and `inputs`;
- `truth_labels`, `validation_gates`, `policy_decisions`, and `citations`;
- `human_review`, `created_at`, and `emitter`.

Optional links and notes may connect the receipt to a draft pull request, ADR, or drift record. Those links remain references; they do not confer authority.

## Validation

For a newly emitted receipt, reviewers should:

1. parse the JSON;
2. validate it against `schemas/contracts/v1/receipts/generated_receipt.schema.json` using JSON Schema Draft 2020-12 and format checking;
3. compare the complete intended change with `artifact_paths`, `artifact_hashes`, and `truth_labels`; their keys must agree, and a receipt must not bind its own bytes;
4. recompute each content hash from the final file bytes;
5. verify that evidence references resolve at the pinned commit or branch;
6. compare every reported validation gate with the actual command result;
7. scan the receipt and artifacts for secrets and sensitive content;
8. run repository-native validation such as `make validate` when it applies;
9. keep human review `pending` until an authorized reviewer acts.

### Current-checkout validation

Run these examples from a complete repository checkout with its validation
dependencies installed. Replace the illustrative receipt filename first. Commands
are usage guidance, not a claim that this README review executed them.

```bash
RECEIPT='data/receipts/generated/replace-with-receipt.json'
python tools/validators/validate_generated_receipt.py "$RECEIPT"
python -m json.tool "$RECEIPT" >/dev/null

# Separate fixture invocation; do not combine it with receipt options.
python tools/validators/validate_generated_receipt.py --fixtures
python -m unittest discover -s tests/validators -p 'test_validate_generated_receipt.py'
git diff --check
```

Default success reports `GENERATED_RECEIPT_VALID`, `integrity=bound`, and the
receipt's declared review state. A well-formed `pending` receipt can pass. This
means bounded schema, cross-field, path and supported digest checks passed; it
is not proof of approval or of complete PR coverage.

The integrity check accepts non-zero SHA-256 prefixes of 32–64 lowercase hex
characters; new receipts should use all 64. It denies self-binding and symbolic-link
artifact paths. Parser, schema and artifact budgets bound the check. BLAKE3
bindings fail with `ARTIFACT_DIGEST_UNSUPPORTED`; schema acceptance alone does
not establish supported integrity verification.

### Historical artifact replay

Later legitimate edits can make an immutable historical receipt fail against
current working-tree bytes. Do not overwrite its hashes or review fields to hide
that mismatch. Identify the commit containing the authored artifacts and opt into
historical replay instead:

```bash
# Set RECEIPT to the supplied receipt and ARTIFACT_COMMIT to its artifact snapshot.
: "${RECEIPT:?Set the repository-relative receipt path}"
: "${ARTIFACT_COMMIT:?Set the exact lowercase 40-character artifact commit}"
python tools/validators/validate_generated_receipt.py \
  --artifact-git-ref "$ARTIFACT_COMMIT" "$RECEIPT"
```

The commit must exist locally and be an ancestor of checkout `HEAD` (including
`HEAD` itself). Branch names, tags, abbreviations and unavailable or non-ancestor
commits are not accepted. The validator does not fetch history or switch the
checkout. It reads regular `100644`/`100755` Git blobs at canonical
repository-relative paths and compares them directly with the receipt's digests.

**Only artifact bytes come from the selected commit.** The receipt remains the
supplied current file; its evidence references do not automatically select the
commit. A successful historical replay does not validate current-checkout or
current-PR artifact bytes. Record the chosen commit and actual result separately,
and emit a new receipt for later authored changes without rewriting old receipts.

### Review claims and validation limits

When a separate review process requires a declaration check:

```bash
python tools/validators/validate_generated_receipt.py \
  --require-review-claim "$RECEIPT"
```

`--require-review-claim` requires a schema-valid approved-review or override
claim. A pending receipt with no override fails with `REVIEW_CLAIM_MISSING`;
that is not an instruction to mark it approved. The flag does not authenticate
the reviewer, approver, scope, expiry or external authorization and grants no
mutation, ready-for-review, merge, release or publication authority.

`--fixtures` cannot be combined with a receipt, `--artifact-git-ref`,
`--require-review-claim` or a non-default `--repo-root`. For receipt validation,
exit `0` means valid and `1` means invalid; argument errors and a missing fixture
inventory use exit `2`. Do not report invalid, skipped or unrun checks as passes.

The validator checks required citation and policy-reference presence; it does not
resolve those references, substantiate truth labels, evaluate Rego or authenticate
review. JSON parsing and an aggregate `make validate` result are not substitutes
for individual receipt integrity checks. Run applicable repository-wide checks
under contributor guidance and attribute each result to its exact scope and ref.

### One-time workflow dependency-lock transition

Historical receipts remain immutable when the Scorecard dependency-lock
migration replaces a workflow's prior `pip install` command. The validator may
recognize only the finite transition ledger at
`tools/ci/python-dependency-lock-migration.json`, whose complete bytes are
pinned in the validator. Each ledger entry binds one canonical workflow path,
the exact base SHA-256, the exact migrated SHA-256, any explicitly superseded
historical receipt hash, and the finite install profiles used by that workflow.

This is not a general waiver. A missing entry, altered ledger, unknown profile,
unexpected prior receipt hash, or any later workflow-byte change falls back to
`ARTIFACT_DIGEST_MISMATCH`. The migration's own generated receipt binds the
ledger, shared installer, lockfiles, tests, documentation, container inputs,
and every migrated workflow as one dependency-closed review packet.

The workflow-migration exception applies to the default working-tree integrity
path. Historical Git replay compares pinned blobs directly and does not apply
that exception. Neither mode authorizes extending the ledger to waive unrelated
artifact changes.

## Review burden

Reviewers must check the artifact list, hashes, evidence citations, truth labels, validation outcomes, sensitive-data posture, Directory Rules placement, and rollback statement. They must also distinguish schema conformance from factual correctness and merge approval.

Changes that affect a sensitive domain, authority root, lifecycle boundary, public path, or release gate require the additional reviewers and ADR handling established by repository governance. The receipt cannot waive those requirements.

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent receipt boundary: process memory is not proof, catalog closure, release, or truth. |
| [`../../proofs/README.md`](../../proofs/README.md) | Separate proof authority; generated receipts do not replace proof closure. |
| [`../../../schemas/contracts/v1/receipts/generated_receipt.schema.json`](../../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Machine shape for generated receipts. |
| [`../../../docs/doctrine/ai-build-operating-contract.md`](../../../docs/doctrine/ai-build-operating-contract.md) | AI build discipline and receipt contract version. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Sole writable human Directory Rules authority, adopted by ADR-0029. |
| [`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted exact-byte adoption and compatibility-migration boundary. |
| [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) | Current contributor, validation, delivery and review boundaries. |
| [`../../../.github/PULL_REQUEST_TEMPLATE.md`](../../../.github/PULL_REQUEST_TEMPLATE.md) | Receipt applicability, final artifact coverage, actual validation and human-review reporting. |
| [`../../../tools/validators/validate_generated_receipt.py`](../../../tools/validators/validate_generated_receipt.py) | Bounded current-checkout and opt-in ancestor-commit integrity checker. |
| [`../../../tests/validators/test_validate_generated_receipt.py`](../../../tests/validators/test_validate_generated_receipt.py) | Focused synthetic regression tests; existence is not a passing execution result. |

## ADRs

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
is **accepted** and adopts the exact Directory Rules v2 bytes at
`docs/doctrine/directory-rules.md`, despite the draft label retained inside those
pinned bytes. The architecture-path copy is read-only compatibility, not a second
writable authority. [Directory Rules](../../../docs/doctrine/directory-rules.md)
§§11.1 and 11.3 assign receipts to the `data/` accountability plane, separate from
proofs and the `release/` decision plane. The existing README and newly emitted
receipts stay in this established lane; this update creates no parallel home.

[ADR-0011](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
continues to document a **proposed** receipt/proof/manifest/catalog separation
decision. ADR-0029's acceptance does not accept ADR-0011 or promote receipts to
proof, policy, catalog, release or public authority. This README changes neither
ADR status nor the adopted Directory Rules bytes.

## Last reviewed

- Date: 2026-09-05; documentation and implementation inspection, not human approval.
- Evidence snapshot: `main@d1b430ca51887777766050e5582659ab34322286`.
- Prior README blob: `5a67f8d743306799a014590ccb45fa9f1177f16a`.
- Validator blob: `52cbca1fe46c583894196855ba52ddc331f78e4f`; schema blob: `fba21ed27ebccf1362fe397fe0c3ebd85e072685`.
- Historical 2026-08-02 count/pin: retained in [Status](#status), not a new inventory.
- Native validator, historical replay, fixtures, full suite and lane-wide validation: NOT RUN for this README review.
- Emitter automation, accountable stewards, independent review and hosted enforcement: NEEDS VERIFICATION.

Re-review when schema, contract version, validator modes, emitter, naming,
validation wiring or review controls change. For corrections, append a focused
README fix and a new receipt; preserve older receipts and their authorship-time
limits. Reverting this documentation does not revert artifact history, change
review state or authorize a delivery transition.
