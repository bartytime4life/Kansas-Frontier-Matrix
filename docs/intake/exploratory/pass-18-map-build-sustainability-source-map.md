<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-map-build-sustainability-source-map
title: Pass 18 Map Build Sustainability Telemetry Source Map
type: source-map
version: v1.0.0
status: review-ready; source-grounded; non-authoritative
owners: OWNER_TBD — Intake steward · Map artifact steward · Observability steward · Docs steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-map; telemetry; sustainability
responsibility: Reconcile supplied and Google Drive sustainability-telemetry ideas with current repository evidence and define the bounded implementation split.
truth_posture: CONFIRMED source bytes Drive retrieval and repository inspection / PROPOSED inactive fixture implementation / UNKNOWN runtime methodology thresholds and adoption
related:
  - ../../../contracts/telemetry/map_build_sustainability.md
  - ../../../docs/dashboards/observability/energy-carbon-footprint.md
  - ../../../docs/standards/TELEMETRY_MINIMUMS.md
  - ../../../docs/adr/ADR-0016-telemetry-redaction-posture.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Map Build Sustainability Telemetry Source Map

## Source ledger

| Source | Evidence inspected | Supports | Does not prove |
|---|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` | SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`; PDF pages 445–446 / printed pages 442–443; card `KFM-P18-INV-424` | Map artifact builds may record energy and CO2 telemetry as non-truth operational evidence; uncertainty and threshold questions remain open. | Mounted-repo implementation, provider accuracy, accounting methodology, threshold, policy, release, or runtime state. |
| Supplied `Master MapLibre Components-Functions-Features.pdf` | SHA-256 `309cf67311059c549e144ae9961b2f49eddf1caab8739a51b47ae88c2f5c1c90`; cited by the Pass 18 card as `SRC-P18-039` | Specialized MapLibre/map-artifact synthesis behind the card. | Current packages, endpoints, runtime telemetry, or release integration. |
| Google Drive `New Ideas 6` | Drive file `1icv4N9lh7m9AkkWjiyXA5n2svrmuxGM9`; retrieved 2026-08-11 | Visualization documentation repeatedly anticipates energy/carbon telemetry and contains illustrative per-render records. | That illustrative values, paths, certifications, or workflows exist in this repository or are suitable production defaults. |
| Google Drive `KFM_Full_Atlas_seed_cards` | Drive doc `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`; retrieved 2026-08-11 | Atlas posture: source-derived ideas must remain explicit about unknown repository maturity and be split into reversible, dependency-closed implementation slices. | Allocation of a production method, threshold, owner, or release authority. |

Drive links: [New Ideas 6](https://docs.google.com/document/d/1icv4N9lh7m9AkkWjiyXA5n2svrmuxGM9/edit) · [KFM Full Atlas seed cards](https://docs.google.com/document/d/1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho/edit)

## Current repository evidence

| Surface | Confirmed state at implementation start | Consequence |
|---|---|---|
| `docs/dashboards/observability/energy-carbon-footprint.md` | Draft specification describes joules/gCO2e signals, internal detail, possible public monthly+ rollups, and unresolved methodology/budget questions. | Reuse the signal vocabulary and internal-default boundary; do not claim the dashboard or policy exists. |
| `docs/standards/TELEMETRY_MINIMUMS.md` | Energy/carbon as a release field is explicitly `PROPOSED` and requires an ADR decision. | Do not add a release field or gate. |
| `docs/adr/ADR-0016-telemetry-redaction-posture.md` | Proposed ADR treats telemetry as governed emission and operational evidence, not sovereign truth or automatic publication. | Use a closed allowlist, internal detail, no public exposure, and no authority. |
| `contracts/telemetry/`, `schemas/contracts/v1/telemetry/`, `tools/validators/telemetry/`, `tests/validators/telemetry/` | Existing semantic/schema/validator/test homes are active responsibility lanes for bounded fixture-first telemetry profiles. | Place the slice in existing homes; do not create top-level telemetry or policy aliases. |
| GitHub PR and branch search | No PR containing `KFM-P18-INV-424` or “sustainability telemetry”; no matching branch found on 2026-08-11. | The slice is not a duplicate at authoring start. |

## Adopted slice

The implementation creates one inactive candidate profile with:

- a synthetic map-artifact build binding;
- decimal-string joules and gCO2e values;
- explicit energy method and carbon factor references/versions;
- relative uncertainty and carbon rounding tolerance;
- deterministic energy-to-carbon arithmetic checking;
- `ABSTAIN` for unavailable measurement or factor evidence;
- internal-only detail and no authorized public rollup; and
- all truth, policy, review, release, publication, and public-use authority fixed to false.

## Deferred dependencies

The following remain separate future decisions or slices:

- telemetry collection, meter/provider selection, and external calls;
- sustainability accounting methodology and factor provenance policy;
- retention, access, redaction receipt, and sink configuration;
- thresholds, budgets, alerts, review routing, or automatic denial;
- `RunReceipt` or `ReleaseManifest` integration;
- dashboard implementation and public rollup review;
- production build/artifact inputs; and
- release, correction, rollback, deployment, or publication integration.

This split preserves the card's useful invariant—telemetry may inform review but is not mapped truth—without resolving its explicit open questions by assumption.
