<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat Source Registry Guide
type: standard
version: v1
status: draft
owners: TODO(confirm habitat lane steward and source-governance owner)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md, data/registry/habitat/MASTER_REGISTRY_INDEX.md]
tags: [kfm, habitat, source-registry, rights, sensitivity]
notes: [Human-readable guide; machine source descriptors remain under data/registry/habitat/.]
[/KFM_META_BLOCK_V2] -->

# Habitat Source Registry

## Registry intent
Habitat source descriptors define what may be ingested, why it is admissible, and under what rights/sensitivity posture it can be published.

## Minimum descriptor fields
Each source descriptor should provide:
- source identifier and steward
- source role (regulatory, modeled, occurrence, context, etc.)
- rights/license and redistribution constraints
- sensitivity handling requirements
- update cadence and refresh policy
- schema/version and validation expectations
- default activation state (`inactive` until reviewed)

## Source-role families
| Role | Typical examples | Publication posture |
|---|---|---|
| `regulatory_critical_habitat` | USFWS official designations | Can support regulatory questions when release-approved. |
| `state_review_context` | KDWP listed/review context | Supports state review context; not a permit decision by default. |
| `modeled_habitat` | GAP/NatureServe model outputs | Contextual support only; cannot answer legal-designation questions. |
| `occurrence_signal` | GBIF/iDigBio or local reviewed signals | Rights + precision + sensitivity checks required before publication. |
| `landscape_context` | NLCD/LANDFIRE/NWI/PAD-US/HLS | Context layers; scope and uncertainty must be explicit. |

## Admission checklist
- Descriptor schema validates.
- Rights and terms are documented and compatible.
- Sensitivity policy is mapped.
- Source role is unambiguous.
- At least one valid and one invalid fixture exist.
- Live fetch remains disabled until steward review is complete.
