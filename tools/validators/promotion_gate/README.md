<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: tools/validators/promotion_gate
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-16
policy_label: public
related: [../README.md, ../../tests/contracts/README.md, ../../tests/reproducibility/README.md, ../../schemas/contracts/README.md, ../../schemas/contracts/v1/README.md, ../../schemas/contracts/v1/runtime/README.md, ../../schemas/contracts/v1/release/README.md, ../../schemas/contracts/v1/policy/README.md, ../../contracts/README.md, ../../policy/README.md, ../../data/receipts/README.md, ../../data/proofs/README.md, ../../docs/standards/README.md, ../../.github/workflows/README.md, ./validate.py, ./cli.py]
tags: [kfm, validators, promotion-gate, spec-hash, receipts, proofs, release, runtime]
notes: [
  "Updated to reflect the now-documented promotion-gate thin slice with validate.py and cli.py.",
  "Preserves fail-closed posture and keeps schema, policy, receipt, proof, and runtime roles distinct.",
  "Exact branch inventory, workflow enforcement depth, and neighboring lane parity still need direct checkout verification before merge."
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/validators/promotion_gate/`

Fail-closed promotion validator for trust-bearing objects,