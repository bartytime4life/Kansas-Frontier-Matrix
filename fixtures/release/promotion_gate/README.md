<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures/release/promotion-gate
title: Promotion-gate readiness fixtures
type: README
version: v1.0.0
status: implemented; synthetic; no-network; non-authoritative
owners: OWNER_TBD - Release steward; promotion steward; validation steward
created: 2026-08-02
updated: 2026-08-02
policy_label: repository-facing; public-safe; synthetic; release-readiness; non-publisher
owning_root: fixtures/
responsibility: Own bounded synthetic inputs for the repository promotion-gate readiness validator without storing release records, evidence, proofs, receipts, review authority, policy authority, or published artifacts.
related:
  - ../README.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../tools/validators/promotion_gate/validate_promotion_gate.py
  - ../../../tests/release/test_promotion_gate.py
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "Fixture filename prefixes bind each example to PASS, DENY, ABSTAIN, or ERROR."
  - "PASS means APPROVE_READY for review only; it never means promoted, released, or published."
[/KFM_META_BLOCK_V2] -->

# Promotion-gate readiness fixtures

This lane contains the deterministic, synthetic packet matrix consumed by
`tools/validators/validate_promotion_gate.py --fixtures` and
`tests/release/test_promotion_gate.py`.

## Authority and placement

`fixtures/` owns reusable synthetic inputs. Promotion semantics remain in
`contracts/release/`; policy remains in `policy/`; executable checks remain in
`tools/validators/`; tests remain in `tests/`; release records remain in
`release/`; receipts and proofs remain in their governed `data/` lanes. No file
here is a real candidate, review, policy decision, attestation, release, or
publication record.

## Matrix

| Fixture | Expected result | Behavior proved |
|---|---|---|
| `valid/pass__complete_candidate.json` | `PASS` / `APPROVE_READY` | A-G declared closure is internally consistent. |
| `invalid/deny__missing_candidate_id.json` | `DENY` | Anonymous candidates cannot proceed. |
| `invalid/deny__artifact_set_mismatch.json` | `DENY` | Manifest and receipt digest sets must agree. |
| `invalid/deny__invalid_geometry.json` | `DENY` | Invalid geometry fails closed. |
| `invalid/deny__unknown_policy_label.json` | `DENY` | Unknown labels cannot be treated as public-safe. |
| `invalid/deny__review_missing.json` | `DENY` | Pending review is not approval. |
| `invalid/abstain__missing_evidence_ref.json` | `ABSTAIN` | Missing support without a contrary claim preserves uncertainty. |
| `invalid/error__policy_evaluation.json` | `ERROR` | Policy-engine failure blocks readiness. |
| `invalid/error__malformed_json.json` | `ERROR` | Malformed input is visible and fail-closed. |

Additional unit cases cover AI-mediated candidates without an AI receipt,
supersession without a correction link, author/reviewer separation, equal
temporal boundaries, impossible timestamps, duplicate JSON keys, deterministic
CLI output, exit-code polarity, and network denial.

All identities and references are visibly synthetic. The non-zero digest
strings are deterministic hashes of synthetic labels; the validator checks
declared cross-field consistency, not the existence or authenticity of an
external artifact.

## Run

```bash
make publish-check
```

The command uses no network and writes no output file. Exit `0` proves only the
repository fixture matrix and unit behavior. It does not create or approve a
`PromotionDecision`, publish an artifact, execute rollback, or establish source,
evidence, rights, sensitivity, policy, review, release, or public-surface
authority.

## Rollback

Revert the validator feature commit and restore the prior TODO-only
`publish-check` only through a reviewed Git change. No external state or data
migration is involved.
