<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/renderer-capability-profile-source-map
title: Renderer Capability Profile Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · UI steward · Map runtime steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of the pluggable renderer proposal into a bounded capability-declaration candidate without selecting or admitting a renderer
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/ui/renderer_capability_profile.md
  - ../../architecture/map-master.md
  - ../../architecture/maplibre-master.md
  - ../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, atlas, ui, maplibre, renderer, capability, source-map]
[/KFM_META_BLOCK_V2] -->

# Renderer Capability Profile Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The "Renderer as Pluggable Component Framework" pattern proposes an abstract interface with implementations compared or substituted behind it; MapLibre remains downstream of governed contracts. | Proposal register, not proof of an implemented interface, package admission, or runtime parity. |
| Attached `Domain-Driven Design Reference.pdf`, SHA-256 `4406daa99ff0e3d58757d62d40358c9fd745f95137e99f14602659d0c3f54e55`, page 59 | The Pluggable Component Framework pattern separates abstract core interfaces from substitutable concrete implementations. | Generic architecture reference; it does not decide KFM renderer policy. |
| Attached `Master MapLibre Components-Functions-Features.pdf`, SHA-256 `309cf67311059c549e144ae9961b2f49eddf1caab8739a51b47ae88c2f5c1c90`, page 14 | MapLibre GL JS, Native, and RS are distinct implementation families with different maturity and runtime postures. | Candidate inventory, not parity, package, policy, or release evidence. |
| `docs/architecture/map-master.md` and `docs/architecture/maplibre-master.md` | Existing renderer-boundary doctrine keeps adapters downstream of governed manifests and records GL JS, Native, and RS with explicit dispositions. | Architecture documentation does not install, probe, admit, or release an implementation. |
| `docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md` | The accepted browser boundary permits MapLibre GL JS only, behind the KFM-owned adapter seam; Native scope and peer-renderer exceptions require separate decisions. | This decision constrains the proposal and is not weakened by capability compatibility. |

## Repository reconciliation

GitHub was inspected on 2026-08-09 with no open pull requests. Live `main` did
not contain `RendererCapabilityProfileCandidate`, its schema, validator,
fixtures, tests, workflow, or receipt. The checked repository already had:

- an accepted sole-browser-renderer decision and adapter-seam boundary;
- renderer doctrine that labels Native parity `NEEDS VERIFICATION` and RS
  experimental or sandbox-only;
- governed view, Evidence Drawer, and tile-artifact contracts; and
- multiple implementation and release gates that must remain separate.

The implementation therefore adds a synthetic compatibility declaration only.
It does not add a renderer registry, plugin loader, adapter implementation,
package dependency, runtime probe, allowlist, or selection mechanism.

## Bounded adaptation

| Source pressure | Retained behavior | Repository constraint |
|---|---|---|
| Compare implementations behind an interface | One fixed abstract-interface version and canonical capability vocabulary. | Compatibility is a declaration result, never admission. |
| Make substitution visible | `FULL`, `PARTIAL`, and `INCOMPATIBLE` derive deterministic dispositions. | Even `SUBSTITUTE_CANDIDATE` remains `REVIEW_REQUIRED` and production selection is false. |
| Keep renderer downstream | References are repository-local semantic contracts only. | Store access, embedded queries, evidence, policy, and release authority are fixed false. |
| Represent GL JS, Native, RS, and headless candidates | Renderer kind and runtime surface remain separate. | Browser candidates other than GL JS fail closed; RS is test-only and Native is not browser-admitted. |

## Path decision

~~~yaml
path_decision:
  artifact: RendererCapabilityProfileCandidate
  proposed_path: contracts/ui/renderer_capability_profile.md
  artifact_kind: semantic contract
  authority_owner: fixture-only renderer capability declaration meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: ui
  scope_id: renderer-capability-profile
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/architecture/map-master.md
    - docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The `contracts/ui/` lane owns renderer-facing candidate meaning; schema,
fixtures, validator, tests, workflow, source map, and receipt remain in their
separate responsibility roots. Any implementation, register, policy, package,
probe, or release artifact requires a separately reviewed change.

## Non-effects

This packet does not select, install, import, load, contact, benchmark, admit,
or release a renderer; declare Native parity; admit RS; weaken the sole-browser
rule; read a store; issue a query; resolve evidence; evaluate policy; change a
manifest or allowlist; approve review; deploy; publish; or authorize public use.

