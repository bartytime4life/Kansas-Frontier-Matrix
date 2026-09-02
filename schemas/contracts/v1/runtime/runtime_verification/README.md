<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas/runtime/runtime-verification/v1
title: Runtime Verification Schema Family
type: schema-family-readme
version: 1.0.0
status: PROPOSED
owners:
  - OWNER_TBD — Runtime steward
  - OWNER_TBD — Schema steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; schema; runtime-verification; no-publication-effect
related:
  - ../../../../../../contracts/runtime/runtime_verification.md
  - ../../../../../../fixtures/contracts/v1/runtime/runtime_verification/README.md
  - ../../../../../../tools/validators/runtime_verification/README.md
notes:
  - "Nested under the accepted schemas/contracts/v1 runtime family; no parallel schema home."
[/KFM_META_BLOCK_V2] -->

# Runtime verification schema family

Machine shapes for the narrow runtime-verification receipt/proof family.

| Schema | Role |
|---|---|
| `outcome.schema.json` | Finite final outcomes. |
| `digest.schema.json` | SHA-256 digest plus explicit encoding. |
| `receipt.schema.json` | Progress/checkpoint process-memory object. |
| `proof.schema.json` | Final proof-ready outcome object. |

Schema validity proves shape only. Semantic equality, inequality, receipt/proof separation, declaration binding, and interrupted-state rules are enforced by `tools/validators/runtime_verification/validate_runtime_verification.py`.

The family is subordinate to the semantic contract, policy, evidence, release, and publication authorities. It creates no permission to promote or expose an artifact.
