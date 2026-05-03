<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-generate-uuid
title: KFM Hydrology Architecture
type: standard
version: v1
status: draft
owners: TODO: hydrology domain steward; platform architecture steward
created: 2026-04-27
updated: 2026-04-27
policy_label: internal-draft
related: [docs/domains/hydrology/README.md, docs/domains/hydrology/IDENTITY_MODEL.md, docs/domains/hydrology/DATA_LIFECYCLE.md]
tags: [kfm, hydrology, architecture]
[/KFM_META_BLOCK_V2] -->

# Hydrology Architecture

## Purpose
Define the hydrology lane architecture that enforces an evidence-first RAW → PUBLISHED trust path.

## Core components
- **Source intake**: descriptors, fixture ingest, and rights checks.
- **Normalization**: canonical hydrology objects (HUC12, crosswalks, sites, observations).
- **Validation**: schema checks, policy checks, and role separation checks.
- **Proof assembly**: RunReceipt, EvidenceBundle, DecisionEnvelope, ReleaseManifest.
- **Governed delivery**: API payloads, map layer manifests, Evidence Drawer payloads.

## Boundaries
- Hydrology documentation does not replace machine contracts.
- Regulatory flood context (NFHL) is not observed inundation evidence.
- Ambiguous identity must produce `ABSTAIN` behavior.

## Interfaces
- **Upstream**: source registries, fixture stores, and policy bundles.
- **Downstream**: governed API contracts, map/UI contracts, release index.

## Non-goals
- Live-network dependence in P0 proof.
- Emergency alerting workflows.
- Simulation products without explicit model-card governance.
