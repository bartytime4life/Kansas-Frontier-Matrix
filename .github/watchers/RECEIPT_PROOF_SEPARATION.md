# Receipt vs Proof Separation (Watchers)

This file captures the canonical language for watcher artifacts.

## Definitions
- **Receipt:** Process memory from a watcher run (inputs, outputs, checks, timestamps, links).
- **Proof:** A higher-order trust object (attestation/proof pack/release-significant evidence).
- **Summary:** Reviewer-facing convenience rendering; not sovereign truth.
- **Work state:** Temporary bounded intermediate state.

## Rules
1. Every watcher run may emit a receipt.
2. A receipt is **not automatically** a proof.
3. Proof objects are assembled only after validation and policy gates pass.
4. Watchers must not gain hidden publish authority.
5. Receipts and proofs must be stored in their governed locations, not in `.github/watchers/`.

## Storage
- Work: `data/work/**`
- Receipts: `data/receipts/**`
- Optional proofs: `data/proofs/**`

## Review language
Prefer: "receipt emitted", "validation passed/failed", "policy gate passed/failed", "proof pack assembled".
Avoid: "autonomous publish", "self-healing bot", "automatic truth updater".
