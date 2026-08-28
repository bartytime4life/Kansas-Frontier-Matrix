<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-denial-reason-explorer-source-map
title: Pass 32 Denial Reason Explorer Source Map
type: exploratory-source-map; implementation-record
version: v0.1.0
status: proposed adaptation; fixture-first; production wiring held
owners: OWNER_TBD — UI steward · Policy steward · Release steward · Privacy steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; source-adaptation; no-authority
related:
  - ../../../apps/explorer-web/src/features/denial_reason_explorer/README.md
  - ../../../apps/explorer-web/src/adapters/DenialReasonProjection.ts
  - ../../../fixtures/ui/denial_reason_projection/README.md
  - ../../../contracts/policy/policy_decision.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, pass-32, deny, reason-code, release-review, ui, no-leak]
notes:
  - "Records a bounded repository adaptation of KFM-P32-FEAT-0017."
  - "The source candidate does not create policy, override, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Pass 32 Denial Reason Explorer Source Map

## Source candidate

| Field | Value |
|---|---|
| Atlas | `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` |
| Source document | `New Ideas 5-17-26` (`SRC-P32-002`) |
| Card | `KFM-P32-FEAT-0017` — Denial reason explorer |
| Atlas status | `NEW` / active / `PROPOSED` |
| Atlas `spec_hash` | `sha256:7d8fabfc1fb17ae1c64fe9afd5b8bac3ea8bbf09e52f1d77cae7330847196190` |
| Normalized statement | A release review surface should expose reason codes such as missing receipt, zoom-too-fine, low-count-cell, or invalid attestation. |
| Retrieved evidence | Google Drive source document and supplied consolidated atlas, inspected 2026-08-10. |

## Repository reconciliation

**CONFIRMED at `main@9e76413313b8529091d01be6132d6e987e3f9fae`:**

- `PolicyDecision` already defines finite outcomes, reasons, obligations, and a
  public-safe explanation boundary, while executable policy remains under
  `policy/`;
- Explorer adapters already reject unknown fields and use fixed no-leak copy
  for negative states;
- no Explorer denial-reason feature, selected-card implementation, or open PR
  for the selected card was found;
- the governance dashboard README lists this feature as proposed rather than
  implemented; and
- accepted ADR-0029 routes the app-local projection, browser feature, synthetic
  fixtures, tests, exploratory record, and generated receipt to existing roots.

## Bounded adaptation

The implementation adds a closed projection adapter and a read-only accessible
list. Only the four source-named codes are accepted. Their titles,
explanations, categories, and next steps are authored as fixed browser copy;
upstream prose is never accepted or reflected.

Digest-bound release-candidate and PolicyDecision references keep the input
from silently pointing to mutable `latest` state. The component does not render
an override action or callback.

## Source-pressure treatment

| Source pressure | Treatment | Boundary |
|---|---|---|
| Missing receipt | **IMPLEMENTED AS FIXED CODE** | Does not validate, create, or attach a receipt. |
| Zoom too fine | **IMPLEMENTED AS FIXED CODE** | Does not expose exact sensitive zoom or change a map configuration. |
| Low-count cell | **IMPLEMENTED AS FIXED CODE** | Does not expose observed count, threshold, or sensitive cell detail. |
| Invalid attestation | **IMPLEMENTED AS FIXED CODE** | Does not expose verifier diagnostics or re-run attestation. |
| Release-review override | **EXCLUDED** | The component is read-only and cannot alter `DENY`. |
| Production governed API wiring | **HELD** | Requires a reviewed public-safe projection producer. |

## Non-effects and rollback

The slice performs no source read, network request, policy evaluation,
threshold calculation, attestation validation, receipt creation, decision
mutation, override, promotion, release, deployment, or publication.

Before merge, close the draft and abandon its branch. After an authorized
merge, revert the bounded files together and rerun `ui-build`. No external or
public state requires restoration.
