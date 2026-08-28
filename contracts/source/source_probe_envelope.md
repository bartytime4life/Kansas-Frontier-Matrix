<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-probe-envelope
title: SourceProbeEnvelope Contract
type: contract
version: v1.0.0
status: implemented; fixture-first; no-network; non-publisher
owners: OWNER_TBD — source steward; affected domain steward; rights/sensitivity reviewer; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; source-admission; profile-aware; fail-closed
owning_root: contracts/
responsibility: Define a shared non-authoritative probe result while preserving source-family semantics and admission holds.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/source/source_probe_envelope.schema.json
  - ../../tools/validators/source_probe/validate_source_probe_envelope.py
  - ../../fixtures/contracts/v1/source/source_probe_envelope/
  - ../../tests/source/test_source_probe_envelope.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "One envelope provides stable identity and finite probe disposition without flattening domain-specific meaning."
  - "Profiles are fixture-only and inactive; live source terms, endpoints, credentials, rights, and activation remain outside this contract."
[/KFM_META_BLOCK_V2] -->

# SourceProbeEnvelope

> **Purpose.** Record what a bounded source probe observed, whether the observation is materially changed, held, denied, or errored, and what source-family rules applied—without activating a source, writing lifecycle data, upgrading evidence, or publishing.

## Profiles

| Profile | Preserved meaning | Fail-closed rules |
|---|---|---|
| `NASS_AGGREGATE` | County/state/national aggregate statistics and canonical row content. | Field/parcel truth, non-aggregate source role, or missing canonical-row digest is denied. |
| `EDNA_MONITORING` | Field sample, custody, laboratory controls, assay result, and bounded interpretation. | A detection signal is not an established population; a negative sample is not species absence; failed controls deny and incomplete custody holds. |
| `KGS_GEOLOGY` | Modeled bedrock or surficial geology context with unit vocabulary and source vintage. | Geologic polygons cannot imply permits, production, reserves, or regulatory status. |
| `LOC_CHRONICLING_AMERICA` | Candidate archival family awaiting source-family governance, rights, CARE, and sensitivity closure. | The profile is forced to `HOLD`; activation and public use remain false. |

## Finite materiality states

`NO_CHANGE | CHANGED | HOLD | DENY | ERROR` describe the probe's bounded disposition. A validator `PASS` means only that the envelope represents its declared state consistently. It does not mean the source is admitted, truthful, rights-cleared, review-approved, or public.

## Directory Rules basis

Meaning belongs under `contracts/source/`; machine shape under `schemas/contracts/v1/source/`; executable validation under `tools/validators/source_probe/`; reusable synthetic examples under `fixtures/contracts/v1/source/`; tests under `tests/source/`; CI under `.github/workflows/`; authoring provenance under `data/receipts/generated/`.

No connector placement is selected, no source descriptor is activated, and no parallel registry, policy, proof, release, or publication authority is created.

## Non-effects

A passing fixture does not establish current NASS, USFWS, KGS, or LOC endpoint behavior, terms, rights, cadence, schema, source authority, CARE review, sensitivity clearance, EvidenceBundle support, promotion, release, deployment, publication, API behavior, or map behavior.

## Rollback

Close the draft PR before merge or revert its bounded commit. No live source, credential, lifecycle instance, cache, release, or public artifact is affected.
