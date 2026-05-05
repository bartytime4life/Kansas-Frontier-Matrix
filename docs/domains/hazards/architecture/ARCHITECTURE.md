# Hazards Lane Architecture

Status: **proposed architecture baseline** for the hazards lane.

## Purpose

Define the end-to-end trust path for hazards so that public claims are always evidence-backed, policy-checked, and reviewable.

## System boundaries

- **In scope:** source descriptors, ingestion, normalization, policy checks, promotion, governed API payloads, MapLibre layers, Evidence Drawer payloads, and Focus Mode outcomes.
- **Out of scope:** emergency dispatch, life-safety instructions, direct client access to raw feeds.

## Reference flow

```text
SourceDescriptor -> RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PROMOTION -> PUBLISHED
                                                                                      -> Governed API
                                                                                      -> MapLibre + Drawer + Focus
```

## Core architectural rules

1. **Source-role first:** each hazard object has exactly one primary `source_role`.
2. **Evidence mandatory:** public hazard claims resolve through `EvidenceRef` -> `EvidenceBundle`.
3. **Fail-closed policy:** unresolved rights, role, sensitivity, or evidence blocks promotion.
4. **No emergency masquerade:** operational warning/advisory/watch content is contextual only.
5. **Derivative humility:** model outputs, detections, and resilience analysis cannot masquerade as observations.
6. **Lineage required:** corrections, supersessions, and rollbacks append lineage; they do not delete history.

## Runtime surfaces

- **Governed API:** released artifacts only.
- **MapLibre:** released layer descriptors only; no live raw source URLs.
- **Evidence Drawer:** must explain what a claim is and is not.
- **Focus Mode:** finite outcomes (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`) only.

## Verification targets

- Implemented schema locations and CI validation commands.
- Actual route and package names used by the active repo.
- Signature and attestation infrastructure state.
