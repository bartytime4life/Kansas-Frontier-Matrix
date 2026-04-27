<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat Promotion and Rollback
type: standard
version: v1
status: draft
owners: TODO(confirm habitat release owner)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md, data/manifests/habitat/, data/receipts/habitat/]
tags: [kfm, habitat, release, rollback, correction]
notes: [Promotion flow described for lane consistency; concrete scripts and command names require verification.]
[/KFM_META_BLOCK_V2] -->

# Habitat Promotion and Rollback

## Promotion prerequisites
A habitat release candidate should not be promoted until:
- source descriptors are valid and approved;
- validation and policy gates pass;
- catalog closure (STAC/DCAT/PROV) is complete;
- EvidenceBundle and ReleaseManifest references resolve;
- reviewer approval is recorded.

## Promotion flow
1. Validate release candidate fixtures and generated artifacts.
2. Generate/verify RunReceipt and EvidenceBundle.
3. Build ReleaseManifest with immutable artifact digests.
4. Record review decision and policy posture.
5. Update current alias only after all checks pass.

## Rollback flow
Rollback is required when an active release is found invalid, superseded, or policy-incompatible.

1. Create CorrectionNotice or RollbackReceipt referencing impacted release.
2. Re-point current alias to last known good release.
3. Preserve superseded release for lineage traceability.
4. Publish runtime message indicating correction/rollback state.

## Non-negotiables
- No destructive overwrite of historical releases.
- No alias change without auditable receipt.
- No silent correction without evidence and policy references.
