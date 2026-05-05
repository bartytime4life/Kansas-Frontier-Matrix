<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat Open Questions and Verification Backlog
type: standard
version: v1
status: draft
owners: TODO(confirm habitat lane steward)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md]
tags: [kfm, habitat, backlog, verification, open-questions]
notes: [Tracks unresolved repository and governance questions blocking full habitat-lane promotion.]
[/KFM_META_BLOCK_V2] -->

# Habitat Open Questions

## Priority verification backlog
| Priority | Question | Why it matters |
|---:|---|---|
| P0 | Which schema home is canonical (`schemas/contracts/v1/habitat/` vs `contracts/habitat/`)? | Prevent split machine authority. |
| P0 | Who are the authoritative lane/documentation/policy owners? | Establish review and merge accountability. |
| P0 | Which source descriptors currently exist and are active? | Clarify admission status and rights risk. |
| P1 | What are the canonical paths for governed API and web UI habitat surfaces? | Avoid duplicate or drifting contracts. |
| P1 | Which validator toolchain is active in CI? | Ensure gate expectations map to executable checks. |
| P1 | Are rollback/correction receipts already standardized in-repo? | Align with existing release lineage conventions. |
| P2 | Which cross-domain habitat relationships are currently implemented? | Scope next documentation and contract updates. |

## Evidence requests for closure
- Confirm CODEOWNERS or stewardship references for Habitat files.
- Confirm existing policy rule locations and naming conventions.
- Confirm fixture inventory for regulatory, modeled, and occurrence cases.
- Confirm if current README companion links are valid relative paths.
