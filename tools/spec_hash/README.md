<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-spec-hash-readme
title: tools/spec_hash README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-architecture-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; deterministic-hashing; provenance-support
owning_root: tools/
responsibility: deterministic spec_hash helper boundary for canonicalization, digest computation, recomputation, and mismatch reporting
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/standards/CANONICALIZATION.md
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../docs/standards/RELEASE_MANIFEST.md
  - ../release/README.md
  - ../proof_pack/README.md
  - ../validators/README.md
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
notes:
  - "This README documents the spec_hash helper lane. It does not confirm executable files."
  - "KFM doctrine defines spec_hash as RFC 8785 JCS canonicalization plus SHA-256, represented as jcs:sha256:<hex>."
  - "tools/spec_hash may compute, recompute, compare, and report hashes. It does not create receipts, EvidenceBundles, policy decisions, release decisions, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/spec_hash

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-spec--hash--helper-informational)
![hash](https://img.shields.io/badge/hash-jcs%3Asha256-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/spec_hash/` is the proposed helper lane for deterministic `spec_hash` computation and verification. It may canonicalize, hash, recompute, compare, and report, but it is not a receipt store, proof store, policy root, release root, or truth authority.

---

## Purpose

`tools/spec_hash/` exists to make KFM identity reproducible.

KFM architecture defines `spec_hash` as a digest over canonical bytes: RFC 8785 JSON Canonicalization Scheme followed by SHA-256, represented as:

```text
jcs:sha256:<hex>
```

A helper in this lane may compute a hash for a JSON record, recompute a stored hash, compare expected vs actual values, and emit a deterministic report. The durable KFM question is:

> Do the checked bytes match the stored `spec_hash` under the accepted canonicalization rule?

The answer is a verification result. It is not, by itself, a receipt, EvidenceBundle, policy decision, release decision, or publication.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/spec_hash/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| `spec_hash` helper executable | **PROPOSED / NEEDS VERIFICATION** | No script or module name is claimed here. |
| Architecture doctrine | **CONFIRMED in repo evidence / draft** | `docs/architecture/identity-and-spec-hash.md` defines the hashing rule and points to this helper home. |
| Canonicalization algorithm | **CONFIRMED in repo evidence / doctrine** | JCS plus SHA-256, formatted as `jcs:sha256:<hex>`. |
| Promotion gate use | **CONFIRMED in repo evidence / doctrine; implementation UNKNOWN** | Promotion recomputes and compares stored hash to checked bytes; implementation maturity still requires verification. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Hash computation and comparison helpers | `tools/spec_hash/` |
| Canonicalization standard | `docs/standards/CANONICALIZATION.md` and accepted ADR/docs |
| Receipt instances | `data/receipts/` |
| EvidenceBundles and proof support | `data/proofs/` |
| Release manifests and decisions | `release/` |
| Contracts, schemas, and policy | `contracts/`, `schemas/`, `policy/` |
| Validators of record | `tools/validators/` or accepted validator home |
| Tests | `tests/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** hash helper code may live here when deterministic, fixture-tested, and explicit about canonicalization.
- **NEEDS VERIFICATION:** exact executable names, fixtures, CI wiring, schema references, and accepted canonicalization edge cases.
- **DENY:** using this folder as storage for receipts, proofs, manifests, release records, contracts, schemas, or policy rules.

[Back to top](#top)

---

## What belongs here

- JCS canonicalization helpers.
- SHA-256 digest helpers.
- `jcs:sha256:<hex>` formatter and parser helpers.
- Stored-vs-recomputed hash comparison helpers.
- Canonicalization fixture runners.
- Mismatch report emitters.
- Dry-run CLI wrappers for CI or local review.
- Small compatibility wrappers that call the accepted implementation.

A helper belongs here only when it is deterministic, no-network by default, explicit about input bytes, and conservative when input is not valid for the accepted canonicalization rule.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/spec_hash/` | Correct home |
|---|---|
| Receipt instances | `data/receipts/` |
| EvidenceBundles or ProofPacks | `data/proofs/` |
| Release manifests or release decisions | `release/` |
| Policy rules | `policy/` |
| Contracts | `contracts/` |
| Schemas | `schemas/` |
| Validators of record | `tools/validators/` |
| Source fetchers | `connectors/` |
| Pipeline orchestration | `pipelines/` |
| Tests | `tests/spec_hash/` or accepted test convention |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SPEC_HASH_MATCH` | Recomputed hash matches stored value. |
| `SPEC_HASH_MISMATCH` | Recomputed hash differs from stored value. |
| `SPEC_HASH_CREATED` | Hash was computed for caller review. |
| `CANONICALIZATION_ERROR` | Input could not be canonicalized under the accepted rule. |
| `UNSUPPORTED_INPUT` | Input type or encoding is unsupported. |
| `MISSING_SPEC_HASH` | Expected stored hash was absent. |
| `ABSTAIN` | Helper cannot decide with available context. |
| `ERROR` | Helper could not safely complete. |

[Back to top](#top)

---

## Standard report envelope

```json
{
  "tool": "spec-hash-placeholder",
  "status": "SPEC_HASH_MATCH",
  "algorithm": "jcs:sha256",
  "input_ref": "path/or/object-id-placeholder",
  "stored_spec_hash": "jcs:sha256:<hex>",
  "recomputed_spec_hash": "jcs:sha256:<hex>",
  "decision": {
    "outcome": "SPEC_HASH_MATCH",
    "authority_created": false
  }
}
```

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/spec_hash/
├── README.md
├── test_spec_hash.py
└── fixtures/
    ├── valid_json/
    ├── mismatch/
    ├── missing_spec_hash/
    └── canonicalization_error/
```

Suggested future command pattern:

```bash
pytest -q tests/spec_hash
```

```bash
python tools/spec_hash/spec_hash.py --input tests/spec_hash/fixtures/valid_json/input.json --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `spec_hash.py` or `tests/spec_hash/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Helper uses the accepted canonicalization algorithm.
- [ ] Helper is deterministic.
- [ ] Helper is no-network by default.
- [ ] Input encoding and JSON validity are handled explicitly.
- [ ] Hash output uses `jcs:sha256:<hex>` format.
- [ ] Mismatches fail closed or produce explicit review outcomes.
- [ ] Output is machine-readable where practical.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Add `tests/spec_hash/README.md`, then add canonicalization fixtures and a dry-run hash checker. |
