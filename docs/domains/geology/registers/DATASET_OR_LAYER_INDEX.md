# Geology & Natural Resources Dataset/Layer Index

This file tracks documentation-level expectations for dataset and layer descriptors used by map/API surfaces.

## Descriptor checklist

| Field | Why it is required |
| --- | --- |
| `dataset_id` | Stable identity for data lineage and release traceability. |
| `layer_id` | Stable identity for renderer and API references. |
| `release_id` | Connects surfaced data to a governed release artifact. |
| `source_ids` + `source_roles` | Preserves authority boundaries and source-role meaning. |
| `knowledge_character` | Prevents observed/interpreted/modeled/admin collapse. |
| `geometry_role` | Distinguishes exact, generalized, redacted, and display-only geometry. |
| `evidence_lookup_ref` | Enables Evidence Drawer / API evidence resolution. |
| `policy_state` + `rights_state` + `sensitivity_state` | Carries public-safety and legal posture to point of use. |
| `review_state` + `freshness_state` | Communicates currentness and stewardship readiness. |
| `transform_receipt_ref` | Links generalization/redaction/resampling transforms to audit receipts. |

## Publication gate reminder

A dataset or layer descriptor is not publishable unless evidence resolution, policy checks, and release linkage are complete.

## Initial index status

No concrete descriptor files are registered here yet; this is a contract-facing stub for future lane implementation.
