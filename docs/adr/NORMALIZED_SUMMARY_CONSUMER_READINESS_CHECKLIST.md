<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/normalized-summary-consumer-readiness-checklist
title: "Normalized Summary Consumer Readiness Checklist"
type: checklist
version: v1.1
status: draft; repository-grounded; validation-guidance-only
owners:
  - "NEEDS VERIFICATION — doctrine-preflight steward"
  - "NEEDS VERIFICATION — normalized-summary consumer owners"
  - "NEEDS VERIFICATION — docs steward"
created: 2026-05-13
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: "Provide human, evidence-first readiness criteria for migrating doctrine-artifact preflight-summary consumers from compatibility fields to normalized artifact path and digest maps without granting cutover, release, or publication authority."
current_path: docs/adr/NORMALIZED_SUMMARY_CONSUMER_READINESS_CHECKLIST.md
canonical_for: human normalized-summary consumer migration guidance
machine_authority: control_plane/normalized_summary_consumer_readiness.yaml
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f755b84c73d70e3c64b43bebd07b7f7617a35f2a
  target_creation_commit: 621a34eff9edf9c22c38ff4ec42ee0017ff09ba8
  target_prior_blob: 7b64e354460621875910648743a08a43ed7e4865
related:
  - docs/adr/INDEX.md
  - docs/adr/README.md
  - docs/adr/_next_move_log.md
  - docs/doctrine/directory-rules.md
  - docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md
  - control_plane/normalized_summary_consumer_readiness.yaml
  - scripts/maintenance/check_normalized_summary_consumer_readiness.py
  - scripts/maintenance/run_doctrine_artifact_preflight.py
  - scripts/maintenance/run_doctrine_artifact_test_suite.sh
  - schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - tools/validators/source/validate_doctrine_preflight_summary_consistency.py
  - tests/policy/test_normalized_summary_consumer_readiness.py
  - tests/policy/test_preflight_summary_consistency.py
tags: [kfm, doctrine-preflight, normalized-summary, consumer-readiness, migration, compatibility, validation, rollback]
notes:
  - "This file is an ADR support document, not an ADR, acceptance record, release decision, or cutover authorization."
  - "v1.1 preserves the original checklist intent while reconciling it with the current emitter, schema, validators, registry, tests, and known evidence gaps."
  - "The machine registry currently records two internal consumers as validated; exhaustive in-repository and external-consumer coverage remains unverified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Normalized Summary Consumer Readiness Checklist

Use this checklist before representing any parser, workflow, operator tool, dashboard, integration, or other downstream reader as ready for **normalized-only doctrine-artifact preflight summaries**.

> [!IMPORTANT]
> **This is validation guidance, not cutover authority.** The canonical ADR index classifies this file as a support document. The machine-readable readiness state lives in [`control_plane/normalized_summary_consumer_readiness.yaml`](../../control_plane/normalized_summary_consumer_readiness.yaml). Neither surface accepts an ADR, changes the emitter default, removes compatibility fields, authorizes release, or proves that every external consumer has been discovered.

> [!CAUTION]
> **A normalized-only validator pass is necessary but not sufficient.** The current `--require-normalized-only` consistency mode rejects legacy standalone fields, but it does not independently require `artifact_paths` or `artifact_digests` to be present. Each consumer-readiness proof must directly assert the normalized maps, required keys, value types, null behavior, and digest verification.

> [!WARNING]
> **Do not infer global readiness from the current two-entry registry.** Both recorded entries are internal repository consumers and are marked `validated`, but the registry is `PROPOSED`, was last reviewed on 2026-05-16, and does not prove exhaustive discovery of external integrations, copied scripts, dashboards, release automation, or operator workflows.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Contract](#normalized-contract) · [Inventory](#consumer-inventory) · [Checklist](#readiness-checklist) · [Validation](#validation) · [Evidence packet](#evidence-packet) · [Cutover](#cutover-gates) · [Failure](#failure-handling) · [Rollback](#rollback) · [Open questions](#open-questions) · [References](#references) · [History](#change-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **Document role** | ADR support document and human migration checklist |
| **Decision authority** | None; [`INDEX.md`](./INDEX.md) classifies this file as “Validation guidance only” |
| **Record edition** | `v1.1` — same-path repository-evidence reconciliation |
| **Current emitter default** | Compatibility output; normalized-only emission requires `--emit-normalized-only` |
| **Normalized-only implementation** | Present as an optional emitter mode, consistency-validator mode, fixture/test path, and shadow check |
| **Machine readiness registry** | Two recorded internal consumers; both carry `status: validated` in the tracked registry |
| **Exhaustive consumer inventory** | `UNKNOWN` |
| **Default normalized-only cutover** | `HOLD` pending complete inventory, current evidence, hosted validation, and reviewed switch/rollback authority |
| **Release or publication effect** | None |
| **Path placement** | Same tracked support-document path under `docs/adr/`; no move, rename, root, or compatibility migration |

The original file was created by commit `621a34eff9edf9c22c38ff4ec42ee0017ff09ba8` on 2026-05-13. This edition preserves its purpose—consumer-level evidence before default cutover—while replacing the seven-item checklist with a repository-grounded migration and verification contract.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence Boundary

The observations below are pinned to `main@f755b84c73d70e3c64b43bebd07b7f7617a35f2a`. They describe tracked repository bytes, not a production deployment or a fresh execution result.

| Surface | CONFIRMED repository observation | Limit |
|---|---|---|
| [`INDEX.md`](./INDEX.md) | Lists this file under support documents as a consumer-readiness checklist with validation guidance only. | Indexing does not authorize cutover. |
| [`run_doctrine_artifact_preflight.py`](../../scripts/maintenance/run_doctrine_artifact_preflight.py) | Always builds `artifact_paths` and `artifact_digests`; `--emit-normalized-only` removes six legacy standalone fields. | The flag is optional, so normalized-only is not the default. |
| [Preflight summary schema](../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json) | Defines normalized maps, exact keys, nullable `presence_output`, and 64-character lowercase hexadecimal digest shapes. | The normalized maps are properties but are not in the schema’s top-level `required` list. |
| [Consistency validator](../../tools/validators/source/validate_doctrine_preflight_summary_consistency.py) | Checks map↔standalone parity in compatibility mode and rejects legacy fields in normalized-only mode. | Normalized-only mode does not independently fail when both normalized maps are absent. |
| [Readiness checker](../../scripts/maintenance/check_normalized_summary_consumer_readiness.py) | Accepts `validated`, `pending`, or `blocked`; requires six non-empty fields; can require all entries to be `validated`. | It does not authenticate owners, resolve evidence, validate date format, or enforce evidence freshness. |
| [Machine registry](../../control_plane/normalized_summary_consumer_readiness.yaml) | Records two internal consumers as `validated`, with dates, commands, and notes. | Registry completeness and current execution remain unverified. |
| [Readiness tests](../../tests/policy/test_normalized_summary_consumer_readiness.py) | Cover tracked-registry pass, malformed/invalid entry failure, and strict failure for a `pending` consumer. | Tests prove bounded behavior, not exhaustive consumer discovery. |
| [Consistency tests](../../tests/policy/test_preflight_summary_consistency.py) | Cover compatibility parity, mismatch failure, legacy-field rejection, map-only pass, and end-to-end normalized-only emission. | The map-only fixture includes both maps; it does not test their total absence. |
| [Doctrine test suite](../../scripts/maintenance/run_doctrine_artifact_test_suite.sh) | Generates a normalized-only shadow summary, runs strict normalized-only consistency, requires all registered consumers validated, and runs focused tests. | Source inspection does not prove the suite is currently green on this branch or required by repository protection. |
| [`scripts/maintenance/README.md`](../../scripts/maintenance/README.md) | Classifies the lane as mixed maturity, warns that current pass/production use is unknown, and records an unresolved receipt-output-path conflict. | This checklist cannot resolve tool graduation or output-home authority. |

### Truth labels used here

- **CONFIRMED** — directly supported by the pinned repository surface.
- **PROPOSED** — a migration or cutover step not yet approved or observed.
- **UNKNOWN** — evidence is insufficient to establish completeness or operation.
- **NEEDS VERIFICATION** — a concrete current check remains.
- **HOLD** — default cutover must not proceed until named gates close.

[Back to top](#top)

---

<a id="normalized-contract"></a>

## Normalized Contract

A normalized-only consumer reads artifact locations and digests from two closed maps.

```json
{
  "artifact_paths": {
    "check_receipt": "string",
    "provenance_sync_receipt": "string",
    "presence_output": null
  },
  "artifact_digests": {
    "check_receipt": "64-character lowercase SHA-256 hex",
    "provenance_sync_receipt": "64-character lowercase SHA-256 hex",
    "presence_output": null
  }
}
```

### Required keys and semantics

| Map | Key | Current shape | Consumer obligation |
|---|---|---|---|
| `artifact_paths` | `check_receipt` | Non-empty string | Treat as the required-artifact-check receipt pointer. |
| `artifact_paths` | `provenance_sync_receipt` | Non-empty string | Treat as the provenance-sync receipt pointer. |
| `artifact_paths` | `presence_output` | Non-empty string or `null` | Handle absence without inventing a path or treating it as failure unless the consumer’s own contract requires persisted presence output. |
| `artifact_digests` | `check_receipt` | Lowercase 64-character hex or `null` under schema | Require a non-null digest before dereferencing or trusting the corresponding emitted artifact. |
| `artifact_digests` | `provenance_sync_receipt` | Lowercase 64-character hex or `null` under schema | Require a non-null digest before dereferencing or trusting the corresponding emitted artifact. |
| `artifact_digests` | `presence_output` | Lowercase 64-character hex or `null` | Require `null` when the path is `null`; when a path exists, require and verify the digest. |

> [!NOTE]
> The current schema permits `null` for all three digest entries. A consumer that needs artifact integrity must apply the stronger operation-specific rule above: a usable non-null path requires a usable digest and successful byte verification.

### Legacy standalone compatibility fields

Normalized-only consumers must not require any of these fields:

| Legacy path field | Replacement |
|---|---|
| `check_receipt` | `artifact_paths.check_receipt` |
| `provenance_sync_receipt` | `artifact_paths.provenance_sync_receipt` |
| `presence_output` | `artifact_paths.presence_output` |

| Legacy digest field | Replacement |
|---|---|
| `check_receipt_sha256` | `artifact_digests.check_receipt` |
| `provenance_sync_receipt_sha256` | `artifact_digests.provenance_sync_receipt` |
| `presence_output_sha256` | `artifact_digests.presence_output` |

Other preflight-summary fields—return codes, stderr, inline payloads, readiness data, alignment data, and presence input—retain their own schema meaning. This migration does not authorize consumers to ignore those fields when their operation depends on them.

### Fail-closed parsing rules

A consumer claiming normalized-only readiness must:

1. reject a missing or non-object `artifact_paths`;
2. reject a missing or non-object `artifact_digests`;
3. require the exact three registered keys in both maps;
4. reject an unexpected value type;
5. preserve `null` for optional `presence_output`;
6. bind each non-null path to its matching digest;
7. verify referenced bytes before treating an artifact as intact;
8. avoid fallback to a legacy field when a normalized entry is absent or malformed; and
9. avoid exposing internal paths, receipts, or diagnostic payloads to public clients without a separate governed release decision.

[Back to top](#top)

---

<a id="consumer-inventory"></a>

## Consumer Inventory

The machine registry is the queryable readiness surface:

```text
control_plane/normalized_summary_consumer_readiness.yaml
```

The checker recognizes exactly three readiness states:

| Status | Meaning for cutover |
|---|---|
| `validated` | Current evidence shows the named consumer passed its declared normalized-only proof at the recorded checkpoint. |
| `pending` | Migration or evidence is incomplete; default cutover remains blocked for that consumer. |
| `blocked` | A known incompatibility or unresolved dependency prevents readiness; default cutover remains blocked. |

### Current tracked entries

| Consumer | Recorded owner | Recorded status | Recorded validation | Bounded interpretation |
|---|---|---|---|---|
| `scripts/maintenance/run_doctrine_artifact_test_suite.sh` | `platform-governance` | `validated` | 2026-05-16; doctrine artifact suite command | Internal regression-bundle evidence only. |
| `tests/policy/test_preflight_summary_consistency.py` | `platform-governance` | `validated` | 2026-05-16; focused pytest command | Test-consumer evidence only. |

These entries do **not** establish that there are only two consumers.

### Inventory discovery checklist

- [ ] Search current repository code, workflows, tests, docs, fixtures, dashboards, and generated templates for all six legacy fields.
- [ ] Search for `artifact_paths`, `artifact_digests`, and serialized doctrine-preflight summary filenames.
- [ ] Inspect shell pipelines, `jq` expressions, Python/TypeScript parsers, CI outputs, workflow artifacts, and operator runbooks.
- [ ] Identify copied scripts or integrations outside the repository through the owning team’s inventory.
- [ ] Record one registry entry per independently deployed or maintained parser—not merely per repository directory.
- [ ] Record the exact owner role, repository/ref or deployment identity, invocation path, and evidence location.
- [ ] Mark undiscovered or unreachable integrations `pending`; do not omit them to make strict mode pass.
- [ ] Re-run inventory whenever the summary schema, emitter, workflow, consumer list, or compatibility window changes.

### Required machine-registry fields

Every consumer entry must contain non-empty values for:

```yaml
- consumer: path-or-stable-consumer-id
  owner: accountable-owner-role
  status: pending
  validated_utc: 2026-08-14
  evidence: exact-command-or-resolvable-evidence-reference
  notes: scope limitations, follow-ups, and recheck triggers
```

The current checker verifies presence and status vocabulary only. Human review must verify that each owner, date, evidence reference, and note is truthful and current.

[Back to top](#top)

---

<a id="readiness-checklist"></a>

## Readiness Checklist

A consumer may be recorded as `validated` only after every applicable item below has evidence.

### 1. Identity, scope, and ownership

- [ ] Consumer has a stable identifier that distinguishes code path, deployment, or integration instance.
- [ ] Accountable owner role is named and reachable.
- [ ] Input source and invocation path are identified.
- [ ] Repository commit, package version, image digest, or deployment revision used for validation is recorded.
- [ ] Consumer purpose and failure consequence are documented.
- [ ] Public, internal, CI-only, release-adjacent, or operator-only exposure is classified.
- [ ] External or copied instances are either inventoried or explicitly marked `UNKNOWN`.

### 2. Normalized map parsing

- [ ] Consumer reads `artifact_paths.check_receipt`.
- [ ] Consumer reads `artifact_paths.provenance_sync_receipt`.
- [ ] Consumer handles nullable `artifact_paths.presence_output`.
- [ ] Consumer reads all digest lookups from `artifact_digests`.
- [ ] Consumer directly asserts that both normalized maps exist.
- [ ] Consumer directly asserts the exact three required keys in each map.
- [ ] Consumer rejects wrong map/key value types.
- [ ] Consumer does not require any standalone path or digest field.
- [ ] Consumer does not silently fall back to legacy fields.
- [ ] Consumer tolerates unrelated, schema-valid summary fields without treating them as artifact-map entries.

### 3. Path, digest, and null integrity

- [ ] Non-null path is paired with the matching non-null digest.
- [ ] Digest is treated as lowercase SHA-256 hex, not as a prefixed `sha256:` identifier.
- [ ] Consumer recomputes and compares the digest before trusting referenced bytes.
- [ ] `presence_output: null` pairs with `artifact_digests.presence_output: null`.
- [ ] A non-null `presence_output` requires a non-null verified digest.
- [ ] Path dereferencing is confined to the consumer’s allowed root or artifact boundary.
- [ ] Missing, mismatched, unreadable, or out-of-bound artifacts fail closed.
- [ ] Logs do not disclose sensitive artifact content, secrets, or unsafe internal paths.

### 4. Positive and negative tests

- [ ] Representative normalized-only summary passes.
- [ ] Compatibility summary with matching maps and legacy fields still behaves as expected during rollback window.
- [ ] Legacy-free payload proves the consumer has no hidden standalone-field dependency.
- [ ] Missing `artifact_paths` fails.
- [ ] Missing `artifact_digests` fails.
- [ ] Missing required key fails.
- [ ] Wrong type fails.
- [ ] Nullable presence-output case passes.
- [ ] Path/digest mismatch fails.
- [ ] Digest tamper fails.
- [ ] Unreadable or missing referenced file fails.
- [ ] Unknown extra key behavior is explicitly tested against the current closed-map schema.
- [ ] Error behavior produces a finite, inspectable result rather than unsafe continuation.

### 5. Repository-native validation

- [ ] Normalized-only summary is emitted with `--emit-normalized-only`.
- [ ] Summary passes the Draft 2020-12 schema validator.
- [ ] Summary passes `validate_doctrine_preflight_summary_consistency.py --require-normalized-only`.
- [ ] Consumer tests independently verify map presence because the current consistency validator does not.
- [ ] Readiness registry passes its structural checker.
- [ ] Readiness registry passes `--require-all-validated` only after all known consumers are complete.
- [ ] Focused consumer tests pass at the exact reviewed revision.
- [ ] Hosted CI result or equivalent immutable test artifact is attached.
- [ ] Introduced failures are distinguished from inherited repository failures.

### 6. Operations and correction

- [ ] Shadow-mode observation window is defined.
- [ ] Parser errors, digest failures, and legacy-field reads are observable without exposing sensitive content.
- [ ] Compatibility-mode rollback is documented and rehearsed.
- [ ] Rollback owner and trigger are named.
- [ ] Cutover does not delete historical receipts or evidence.
- [ ] Correction procedure updates machine readiness state and invalidates stale evidence.
- [ ] Revalidation triggers include schema changes, emitter changes, parser changes, dependency changes, deployment changes, and failed observations.
- [ ] Evidence expiration or review cadence is defined even though the current checker does not enforce it.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

Use temporary output paths for focused validation so investigation does not accidentally create or overwrite repository-local receipt candidates.

```bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
summary="$tmp_dir/normalized-summary.json"

python scripts/maintenance/run_doctrine_artifact_preflight.py \
  --stable-filenames \
  --emit-normalized-only \
  --output-dir "$tmp_dir/receipts" \
  > "$summary"

python tools/validators/source/validate_doctrine_artifact_preflight_summary.py \
  --fixtures

python tools/validators/source/validate_doctrine_preflight_summary_consistency.py \
  "$summary" \
  --require-normalized-only

python scripts/maintenance/check_normalized_summary_consumer_readiness.py \
  --require-all-validated

python -m pytest \
  tests/policy/test_preflight_summary_consistency.py \
  tests/policy/test_normalized_summary_consumer_readiness.py \
  tests/policy/test_run_doctrine_artifact_preflight.py \
  tests/policy/test_preflight_summary_schema_contract.py \
  tests/source/test_doctrine_artifact_preflight_summary_schema.py \
  -q --strict-config --strict-markers
```

### Direct assertions not supplied by the current normalized-only consistency mode

Add consumer-specific checks equivalent to:

```python
paths = summary.get("artifact_paths")
digests = summary.get("artifact_digests")

assert isinstance(paths, dict)
assert isinstance(digests, dict)
assert set(paths) == {
    "check_receipt",
    "provenance_sync_receipt",
    "presence_output",
}
assert set(digests) == set(paths)
```

Then test path/digest pairing and actual digest replay. Do not interpret the example as a repository patch or a substitute for the consumer’s own language/runtime tests.

### Full regression bundle

The repository also provides:

```bash
bash scripts/maintenance/run_doctrine_artifact_test_suite.sh
```

Run it in a clean or disposable checkout, inspect written outputs and `git diff`, and record the exact revision and result. A green bundle proves bounded checked behavior; it does not prove exhaustive external consumer readiness, ADR acceptance, release approval, or publication.

[Back to top](#top)

---

<a id="evidence-packet"></a>

## Evidence Packet

Attach one reviewable packet per consumer.

| Evidence field | Required content |
|---|---|
| Consumer identity | Stable name, path, deployment, or integration ID |
| Owner | Accountable role and review route |
| Revision | Commit SHA, package version, image digest, or deployment revision |
| Input profile | Compatibility and normalized-only fixture identities |
| Positive tests | Exact commands and immutable results |
| Negative tests | Missing maps/keys, null handling, type errors, digest tamper, unreadable artifact |
| Legacy independence | Search or test proving no required standalone-field read |
| Digest replay | Evidence that referenced bytes were recomputed and matched |
| Hosted evidence | CI run, test artifact, or equivalent immutable locator |
| Shadow window | Start/end, sample count, observed failures, and limitations |
| Rollback | Exact compatibility-mode or version rollback and rehearsal result |
| Residual risk | Known unsupported environments, external copies, or unresolved consumers |
| Recheck triggers | Schema/emitter/parser/dependency/deployment changes and evidence expiry |
| Final status | `validated`, `pending`, or `blocked` with reviewer note |

### Registry update rule

- Use `pending` while evidence is being assembled.
- Use `blocked` when a known defect or dependency prevents migration.
- Use `validated` only after the packet is complete at a pinned revision.
- Never retain `validated` after a material recheck trigger without fresh evidence.
- Do not encode approval, release, or publication in the readiness status.

[Back to top](#top)

---

<a id="cutover-gates"></a>

## Cutover Gates

Default normalized-only emission remains on `HOLD` until all gates are closed.

| Gate | Required evidence | Current state at the pinned snapshot |
|---|---|---|
| **C0 — Authority and scope** | Named migration owner, exact producer/consumer scope, and reviewed non-effects | `NEEDS VERIFICATION` |
| **C1 — Consumer inventory** | Bounded repository search plus known external integration inventory | `UNKNOWN` completeness |
| **C2 — Contract closure** | Mode-specific required maps/keys, null rules, digest rules, compatibility window | `PARTIAL`; schema/validator gaps remain |
| **C3 — Consumer migration** | Every known registry entry has current `validated` evidence | Two internal entries recorded; global closure `UNKNOWN` |
| **C4 — Negative proof** | Missing maps/keys, type errors, null, mismatch, tamper, unreadable artifact all fail safely | `PARTIAL` |
| **C5 — Shadow operation** | Normalized-only summaries observed in representative CI/operator paths without hidden legacy reads | `NEEDS VERIFICATION` |
| **C6 — Hosted exact-head validation** | Schema, consistency, readiness, consumer, and regression checks green on reviewed head | `PENDING` for this docs revision |
| **C7 — Rollback rehearsal** | Compatibility output restored and consumers recover within the declared objective | `NEEDS VERIFICATION` |
| **C8 — Reviewed default switch** | Separate, explicit producer-default change with docs/tests/evidence and no compatibility-field deletion unless authorized | Not performed |
| **C9 — Post-cutover observation** | Error monitoring, correction path, and rollback window remain active | Future work |

### Cutover non-effects

Completing this checklist does not itself:

- change `run_doctrine_artifact_preflight.py` defaults;
- remove or deprecate legacy schema properties;
- prove external consumer completeness;
- make the readiness registry authoritative for release;
- resolve the maintenance-output-path conflict;
- approve a promotion or release;
- publish a doctrine artifact or summary; or
- change repository settings or required checks.

[Back to top](#top)

---

<a id="failure-handling"></a>

## Failure Handling

| Condition | Required readiness status | Required action |
|---|---|---|
| Consumer not yet inventoried completely | `pending` | Continue discovery; hold default cutover. |
| Consumer requires a legacy standalone field | `blocked` or `pending` | Migrate parser and add normalized-only proof. |
| Missing normalized maps or keys is accepted | `blocked` | Add fail-closed parsing and negative tests. |
| Nullable `presence_output` crashes or invents a path | `blocked` | Correct null semantics and rerun fixtures. |
| Path exists without a verified matching digest | `blocked` | Deny artifact use; correct pairing and replay. |
| Digest mismatch or tamper | `blocked` | Stop downstream use, preserve evidence, investigate, correct, and rerun. |
| Evidence link, date, or owner cannot be verified | `pending` | Replace with resolvable current evidence. |
| Schema, emitter, validator, or parser materially changes | `pending` | Invalidate prior readiness and revalidate. |
| Hosted checks fail for an introduced reason | `blocked` | Fix or revert the change; do not bypass. |
| Failure is inherited and unrelated | Keep truthful status with limitation | Record exact evidence and do not misattribute causality. |
| External consumer is unreachable or ownership is unknown | `pending` | Hold cutover or explicitly remove the unsupported integration through a separate reviewed change. |

A parser error must not cause fallback to unverified legacy data, fabricated paths, skipped digest checks, or public exposure of internal diagnostics.

[Back to top](#top)

---

<a id="rollback"></a>

## Rollback

### Before default cutover

Keep compatibility emission available by omitting `--emit-normalized-only`. Continue emitting normalized maps so migrated consumers remain forward-compatible.

### After a default-switch change

1. Stop or pause the affected producer/consumer path.
2. Preserve the failing summary, referenced artifact identities, logs, and exact revision subject to sensitivity rules.
3. Restore compatibility-mode emission through the reviewed configuration or code rollback.
4. Restore the last known compatible consumer version where necessary.
5. Mark affected readiness entries `pending` or `blocked`.
6. Identify whether the failure is in inventory, schema, emitter, parser, digest verification, deployment, or evidence.
7. Correct the root cause with focused fixtures and tests.
8. Re-run normalized-only shadow validation and rollback rehearsal.
9. Record correction, supersession, and residual risk.
10. Reattempt cutover only through a new reviewed decision.

Do not reset shared history, delete audit material, remove normalized maps, or rewrite prior evidence to conceal the failure.

### Documentation rollback

Before merge, close the draft pull request or restore blob `7b64e354460621875910648743a08a43ed7e4865` in a transparent commit. After merge, revert the documentation commit. Documentation rollback does not alter emitter or consumer behavior.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open Questions and Verification Backlog

1. **Consumer completeness — UNKNOWN.** Which repository, external, copied, dashboard, operator, or deployment consumers are not represented in the two-entry registry?
2. **Mode-specific schema — NEEDS VERIFICATION.** Should the summary schema use explicit compatibility and normalized-only profiles so normalized maps become required in normalized-only mode?
3. **Validator closure — NEEDS VERIFICATION.** Should `--require-normalized-only` reject absent normalized maps and missing registered keys, not only legacy-field presence?
4. **Path/digest coupling — NEEDS VERIFICATION.** Which validator should enforce null pairing and non-null path→digest requirements?
5. **Evidence freshness — NEEDS VERIFICATION.** What review interval or change trigger invalidates a `validated` entry?
6. **Evidence resolution — NEEDS VERIFICATION.** Should registry evidence become a structured, resolvable reference instead of a free-form string?
7. **Owner authenticity — NEEDS VERIFICATION.** Which control confirms an owner role and review route?
8. **Promotion coupling — UNKNOWN.** Is strict readiness actually required by a current release/promotion path or only exercised in the doctrine regression bundle?
9. **Compatibility window — NEEDS VERIFICATION.** How long must standalone fields remain available after default cutover?
10. **Output authority — CONFLICTED.** The maintenance orchestrator default output and the documented governed receipt lane differ; this checklist does not choose between them.
11. **Hosted proof — NEEDS VERIFICATION.** Which checks are required by branch protection and what exact-head run proves this migration on the target branch?
12. **External publication posture — DENY by default.** Are preflight summaries or their internal artifact paths ever intended for public exposure? No current evidence authorizes that use.

[Back to top](#top)

---

<a id="references"></a>

## References

- [ADR support-document inventory](./INDEX.md)
- [ADR operating contract](./README.md)
- [Historical next-move lineage](./_next_move_log.md)
- [Accepted Directory Rules decision](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)
- [Doctrine-artifact preflight runbook](../runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md)
- [Machine readiness registry](../../control_plane/normalized_summary_consumer_readiness.yaml)
- [Readiness checker](../../scripts/maintenance/check_normalized_summary_consumer_readiness.py)
- [Preflight emitter](../../scripts/maintenance/run_doctrine_artifact_preflight.py)
- [Maintenance lane operating guide](../../scripts/maintenance/README.md)
- [Doctrine regression bundle](../../scripts/maintenance/run_doctrine_artifact_test_suite.sh)
- [Preflight summary schema](../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json)
- [Consistency validator](../../tools/validators/source/validate_doctrine_preflight_summary_consistency.py)
- [Readiness tests](../../tests/policy/test_normalized_summary_consumer_readiness.py)
- [Consistency tests](../../tests/policy/test_preflight_summary_consistency.py)

[Back to top](#top)

---

<a id="change-history"></a>

## Change History

| Date | Edition | Change | Authority effect |
|---|---|---|---|
| 2026-05-13 | Initial | Added a concise seven-check consumer-readiness list before normalized-only default cutover. | Validation guidance only |
| 2026-08-14 | `v1.1` | Reconciled current emitter, schema, validators, registry, tests, shadow validation, machine statuses, known gaps, cutover gates, evidence packet, failure handling, and rollback. | None; default cutover remains on `HOLD` |

### No-loss reconciliation

The original requirements remain explicit:

- normalized path maps replace standalone path reads;
- normalized digest maps replace standalone digest reads;
- `presence_output` remains nullable;
- consumers must not require standalone digest fields;
- normalized-only consistency validation remains required;
- rollback re-enables compatibility output; and
- each consumer attaches owner, tests, UTC date, CI/test evidence, and follow-ups.

This edition adds the missing evidence boundary, direct map-presence assertions, digest replay, inventory discipline, status vocabulary, negative tests, cutover gates, correction behavior, and known validator/schema limitations without changing runtime behavior.

[Back to top](#top)
