<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/4d4b83f1-3b5c-4d50-8c68-6b4ef0ad3fbf
title: tools/hash — Spec hashing + digest tooling
type: standard
version: v1
status: draft
owners: kfm-platform (TODO)
created: 2026-02-26
updated: 2026-02-26
policy_label: public
related:
  - (not confirmed in repo) docs/governance/promotion-contract.md
  - (not confirmed in repo) packages/catalog
  - (not confirmed in repo) packages/ingest
  - (not confirmed in repo) packages/evidence
tags: [kfm, hash, spec_hash, sha256, rfc8785, canonical-json, determinism, promotion-gates]
notes:
  - Contract-first doc for deterministic IDs + artifact digests. Update paths once repo wiring is verified.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/hash — spec_hash + digest tooling
Deterministic hashing primitives used by KFM to compute **stable identities** (`spec_hash`) and **content digests** (artifacts/manifests/bundles).

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-public-brightgreen)
![hash](https://img.shields.io/badge/hash-sha256-blue)
![canonical-json](https://img.shields.io/badge/canonical-json-RFC8785-blueviolet)
![posture](https://img.shields.io/badge/posture-fail--closed-red)

---

## Quick nav
- [Purpose](#purpose)
- [Contracts](#contracts)
- [Hash surfaces](#hash-surfaces)
- [spec_hash algorithm](#spec_hash-algorithm)
- [Digest conventions](#digest-conventions)
- [Hash drift prevention](#hash-drift-prevention)
- [CI gate](#ci-gate)
- [Directory layout](#directory-layout)
- [What belongs here](#what-belongs-here)
- [What must NOT go here](#what-must-not-go-here)
- [Definition of Done](#definition-of-done)
- [Repo reality checks](#repo-reality-checks)

---

## Purpose
KFM’s trust membrane depends on **stable, reproducible identifiers**. Without them you can’t reliably:
- cite evidence across time,
- reproduce pipelines,
- cache/index safely,
- detect tampering or drift.

This folder defines the **hashing contract** and supporting tools for:
- `spec_hash`: deterministic identity for a DatasetVersion derived from a canonical dataset spec.
- `sha256` digests: deterministic content hashing for artifacts, manifests, and bundles.

> [!IMPORTANT]
> This is governed infrastructure. If hashing behavior changes, it must be reviewed like an API change.

---

## Contracts
### Non-negotiable
1) **Determinism**
- Same input spec → same `spec_hash` on any machine.
- Same bytes → same content digest.

2) **Canonicalization**
- `spec_hash` MUST be derived from canonical JSON (RFC 8785 / JCS).
- Never hash pretty-printed JSON or language-specific object dumps.

3) **Fail-closed posture**
- If the canonicalization step fails, hashing fails.
- If drift is detected, CI fails.
- If an algorithm label is missing, CI fails.

4) **Algorithm transparency**
- Always include algorithm name in the identifier string (e.g., `sha256:<hex>`).

---

## Hash surfaces
| Surface | Input | Output | Purpose | Notes |
|---|---|---:|---|---|
| `spec_hash` | Canonical dataset spec (JSON) | `sha256:<hex>` | DatasetVersion identity | Canonicalize with RFC 8785 first |
| artifact digest | Artifact bytes | `sha256:<hex>` | Integrity + content addressing | Compute over raw bytes, not decoded text |
| manifest digest fields | Manifest JSON + referenced digests | `sha256:<hex>` | Tamper-evident receipts | Manifest itself should be canonicalized before hashing (if hashed) |

---

## spec_hash algorithm
### Canonical inputs
A dataset spec SHOULD include (at minimum):
- upstream source configuration (endpoints, params)
- normalization rules
- validation rules + thresholds
- output artifact plan
- policy label intent
- cadence/refresh intent

### Algorithm (normative)
```text
spec_hash = sha256( RFC8785_canonical_json(spec) )
```

### Required rules
- Canonicalize first. Always.
- Treat number formatting deterministically (handled by RFC 8785).
- Reject NaN/Infinity and non-JSON types.
- Reject non-UTF8 input.

> [!WARNING]
> If you skip canonicalization, you will get hash drift across runtimes and break citations.

---

## Digest conventions
### Required format
All digests MUST be formatted as:

```text
sha256:<64-hex>
```

### Why prefix the algorithm?
It makes IDs self-describing and supports future migrations without ambiguity.

> [!NOTE]
> If KFM ever adds another algorithm, the ID scheme stays unbroken because the algorithm is already part of the string.

---

## Hash drift prevention
Drift is a governance failure (it breaks reproducibility and evidence traceability).

**Checklist**
- Store the exact spec used to compute `spec_hash` next to the computed value.
- Maintain golden test vectors for canonicalization + hashing.
- Unit-test that recomputing from stored spec yields the same `spec_hash`.
- Treat `spec_hash` changes as **breaking**: require a human-readable diff of the spec and a rationale.
- Never compute `spec_hash` from nondeterministic inputs:
  - timestamps / clocks
  - random seeds
  - unstable key ordering (without RFC 8785)
  - environment-dependent defaults

---

## CI gate
A CI step SHOULD run a “hash drift check” that:
- recomputes `spec_hash` from canonical specs,
- compares to stored/declared `spec_hash`,
- fails if any mismatch is found.

### Expected command (verify in-repo)
```bash
node tools/hash/check_spec_hash.js
```

> [!TIP]
> Keep this check cheap and deterministic so it can be required on every PR.

---

## Directory layout
> Minimal expected layout. Update once repo wiring is confirmed.

```text
tools/hash/
├─ README.md
├─ check_spec_hash.js            # (expected) recompute & compare; fail on drift
└─ fixtures/                     # (recommended) golden vectors
   ├─ spec_minimal.json
   ├─ spec_ordering_variants.json
   └─ expected_hashes.json
```

---

## What belongs here
**Acceptable inputs**
- RFC 8785 canonicalization helpers
- sha256 digest helpers
- spec_hash drift checker(s) used by CI
- golden fixtures + test vectors
- minimal docs explaining invariants and failure modes

---

## What must NOT go here
**Exclusions**
- Password hashing, auth token derivation, credential storage, key derivation
- Encryption utilities / key management
- Ad-hoc “fast hashes” for convenience that aren’t part of governed identity/digest contracts
- Hashes over nondeterministic or user-environment-dependent inputs

---

## Definition of Done
- [ ] `spec_hash` computation is canonicalized (RFC 8785) and uses sha256
- [ ] All digests are `sha256:<hex>`
- [ ] Golden fixtures exist and pass on all supported runtimes
- [ ] CI drift check is wired and required
- [ ] Drift failure messages are actionable (point to spec file + expected vs actual)
- [ ] README updated to match actual repo paths/flags once tooling lands

---

## Repo reality checks
Because this is contract-first documentation, verify and update:
- Does `check_spec_hash.js` exist and match the command above?
- Where do canonical dataset specs live (path + naming)?
- Where is `spec_hash` stored (spec file, registry, manifest)?
- Are fixtures required by CI?

If any mismatch is found: **update this README to match repo truth** (fail-closed posture).

---

[Back to top](#top)
