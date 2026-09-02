<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/evidence-drawer-drift-integrity-profile
title: Evidence Drawer source-drift and artifact-integrity profile
type: semantic-contract-extension; public-safe-ui-projection; fixture-first
version: v0.1.0
status: proposed; subordinate-profile; fixture-first; no-network
owners: OWNER_TBD — UI steward · Evidence steward · Source steward · Integrity steward · Policy steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public-safe; ui; evidence-drawer; source-drift; artifact-integrity; no-leak
related:
  - ./evidence_drawer_payload.md
  - ../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../contracts/source/source_intake_record.md
  - ../../fixtures/ui/evidence_drawer_payload/
  - ../../apps/explorer-web/src/adapters/GovernedClient.ts
  - ../../apps/explorer-web/src/features/evidence_drawer/
tags: [kfm, ui, evidence-drawer, source-drift, sidecar, hash, provenance, quarantine, public-safe]
notes:
  - "Source idea: KFM-P4-FEAT-0001."
  - "This extension reuses the existing public-safe payload vocabulary and creates no second schema authority."
[/KFM_META_BLOCK_V2] -->

# Evidence Drawer source-drift and artifact-integrity profile

This subordinate profile realizes **KFM-P4-FEAT-0001** with the existing `kfm.explorer.evidence-drawer.public-safe.v1` payload and Explorer resolver. It adds representative source-drift and artifact-integrity fixtures without inventing a parallel Evidence Drawer schema or treating operational diagnostics as public evidence.

## Public mapping

| Operational condition | Public outcome | Existing reason code | Public-safe effect |
|---|---|---|---|
| Source drift awaiting review | `ABSTAIN` | `HELD_EVIDENCE` | Explain that evidence is held; show only a public-safe historical reference. |
| Source quarantined because rights are unresolved | `DENY` | `RIGHTS_UNRESOLVED` | Render fixed no-leak denial copy; expose no evidence, citation, history, path, or raw reason. |
| Required artifact sidecar missing | `ABSTAIN` | `MISSING_EVIDENCE` | Explain that required support is unavailable. |
| Provenance reference cannot resolve | `ABSTAIN` | `CITATION_UNRESOLVED` | Explain that required citation/provenance support cannot be resolved. |
| Artifact hash verification failed | `ERROR` | `UPSTREAM_ERROR` | Render fixed error copy; expose no computed/expected digest, path, or internal diagnostic. |

The mapping intentionally reuses existing finite outcomes and reason codes. New source-specific diagnostic codes belong in steward-only operational records unless a separately reviewed public-contract change proves they are safe and necessary.

## Public/steward separation

The public payload may contain only the closed fields accepted by `EvidenceDrawerPayload`. It must not contain:

- raw, WORK, or QUARANTINE paths;
- expected or observed private digests;
- source credentials, endpoint diagnostics, stack traces, or internal hostnames;
- exact sensitive geometry or the reason a protected location was selected;
- unreviewed SourceIntakeRecord detail;
- reviewer identities or private issue/incident references; or
- arbitrary `internal_diagnostics`, `steward_context`, or equivalent fields.

Steward diagnostics remain in governed operational records and access-controlled review surfaces. A public projection may state that a condition is held, missing, unresolved, denied, or unavailable, but it must not reveal the private diagnostic that produced that state.

## Runtime behavior

The Explorer adapter validates a closed payload and the Evidence Drawer renders fixed copy for `ABSTAIN`, `DENY`, and `ERROR`. Payload-supplied negative summaries are not reflected. The fixtures in this slice include canary strings to prove denied/error/internal-diagnostic text does not cross the public projection boundary.

## Non-effects

This profile does not resolve EvidenceBundle support, execute source comparison, verify an artifact, approve rights or policy, authenticate review, release a layer, publish a claim, expose steward diagnostics, or grant a watcher authority.

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. The slice contains synthetic fixtures and tests only; no public artifact, source, cache, release, or lifecycle migration requires cleanup.
