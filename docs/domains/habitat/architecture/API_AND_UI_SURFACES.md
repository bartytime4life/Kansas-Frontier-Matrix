<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat API and UI Surfaces
type: standard
version: v1
status: draft
owners: TODO(confirm habitat API owner and web/UI owner)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md, docs/architecture/habitat/RUNTIME_EVIDENCE_MODEL.md]
tags: [kfm, habitat, api, ui, evidence-drawer, maplibre]
notes: [Path conventions for API and web apps remain NEEDS VERIFICATION in this repository.]
[/KFM_META_BLOCK_V2] -->

# Habitat API and UI Surfaces

## API contract expectations
Public habitat endpoints should:
- return governed `DecisionEnvelope` responses;
- include evidence references resolvable to an `EvidenceBundle`;
- include freshness/review/limitation metadata;
- expose denial/abstention reasons when policy blocks an answer.

Public habitat endpoints must not:
- expose RAW/WORK/QUARANTINE paths;
- return restricted internal canonical-store objects;
- infer legal authority from modeled/context-only sources.

## UI surface expectations
MapLibre, Evidence Drawer, and Focus Mode should render only governed API payloads.

### Map behavior
- Layers must identify source role and review state.
- Popups should link to evidence metadata, not raw internal records.
- Sensitive geometry should be generalized/withheld as required by policy.

### Evidence Drawer behavior
- Show claim summary, source-role labels, and policy posture.
- Show limitation and confidence context.
- Support correction/supersession visibility.

### Focus Mode behavior
- Summarize only released evidence-backed claims.
- Use `ABSTAIN` for unsupported or incomplete evidence situations.
- Never fabricate policy permissions or legal conclusions.
