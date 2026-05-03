<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat Domain Architecture
type: standard
version: v1
status: draft
owners: TODO(confirm habitat lane steward and documentation-control owner)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md, docs/architecture/habitat/HABITAT_CONTROL_PLANE_INDEX.md]
tags: [kfm, habitat, architecture, evidence-first]
notes: [Draft companion file created to complete docs/domains/habitat set; confirm links and owner metadata before promotion.]
[/KFM_META_BLOCK_V2] -->

# Habitat Architecture

## Purpose
This document defines the Habitat lane boundaries, object families, and trust boundaries that support the `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED` lifecycle described in the Habitat README.

## Bounded context
Habitat owns environmental and habitat-support context products. It can depend on and link to fauna, flora, and other lane evidence, but does not absorb those domains into habitat truth.

### In-bounds
- regulatory critical habitat
- state review/list context for habitat relevance
- modeled habitat and range-support layers
- occurrence-derived habitat assignments (derived artifacts only)
- landscape/community/context layers
- connectivity and corridor context
- correction and supersession lineage for habitat releases

### Out-of-bounds
- raw source connectors and credentials
- direct legal conclusions outside source-role scope
- exact sensitive occurrence disclosure in public outputs
- browser-side policy inference

## Primary object families
| Object family | Role | Notes |
|---|---|---|
| `SourceDescriptor` | Source admission and rights posture | Must exist before live fetch or publication. |
| `HabitatFeature` | Normalized habitat geometry/object payload | Carries source-role and support scale metadata. |
| `ValidationReport` | Fixture and schema gate result | Fail-closed on critical violations. |
| `EvidenceBundle` | Claim-to-evidence resolution container | Runtime and UI claims must resolve through this surface. |
| `ReleaseManifest` | Immutable release contract | Supports reproducibility, rollback, and alias updates. |
| `DecisionEnvelope` | Runtime finite outcome wrapper | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. |

## Trust boundaries
1. Public surfaces read from released artifacts only.
2. No public consumer reads RAW/WORK/QUARANTINE or internal canonical stores directly.
3. Source role must be preserved through derivation and publication.
4. Sensitive locations default to deny, generalize, or abstain depending on policy.

## Cross-lane dependencies
Habitat can reference:
- Fauna and Flora evidence for habitat-support context.
- Hydrology and Soil layers for environmental covariates.
- Hazards and Infrastructure for disturbance and barrier context.

Cross-lane joins must preserve provenance edges and source-role meaning.
