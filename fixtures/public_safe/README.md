# Public-safe fixtures

`fixtures/public_safe/`

Status: draft / fixture parent index / public-safe synthetic examples.

This directory is the parent lane for small synthetic public-safe fixture examples. Use it for runtime/documentation examples that are intentionally generalized, non-sensitive, reproducible, and safe to show in public-facing README examples, renderer smoke contexts, governed API dry-runs, Evidence Drawer examples, Focus Mode examples, source-role examples, correction examples, rollback examples, and expected-output examples.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Fixture parent posture

Public-safe fixtures are synthetic examples that should be safe for open review and documentation. They may demonstrate governed shapes, generalized map behavior, drawer copy, Focus Mode copy, source-role labels, evidence refs, rights posture, sensitivity posture, review posture, release posture, correction posture, rollback posture, finite outcomes, and expected outputs.

Public-safe does not mean authoritative, released, complete, or risk-free. A public-safe fixture does not become canonical truth, release evidence, public API authority, public map authority, tile authority, source authority, policy authority, proof authority, or implementation proof.

A fixture may describe intended behavior before validators, renderer checks, governed API routes, policy bundles, schema checks, release integration, or CI coverage exist. Fixture success is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic runtime/checking inputs and public-safe generalized examples. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, public API root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Child lane inventory

The following child lanes have populated README coverage. This table is a navigation index, not proof that payload files, validators, tests, governed API routes, UI checks, policy bundles, release manifests, source-registry records, proof stores, or CI coverage exist.

| Child lane | Purpose | Expected posture |
|---|---|---|
| `settlement/` | Synthetic public-safe settlement-side examples for settlement, municipality, census-place, townsite, ghost-town, fort, mission, reservation-community, map-rendering, drawer, Focus Mode, governed API, source-role, evidence-reference, correction, rollback, and expected-output examples. | Public-safe, generalized, valid, invalid, negative, expected output, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, release-blocked, correction-visible, rollback-visible, blocked render, `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |

## Relationship to sibling fixture lanes

| Lane | Relationship |
|---|---|
| `../slim/` | Preferred home for small renderer/runtime fixtures that are not explicitly public-safe examples. |
| `../heavy/` | Heavy runtime stress lane; use it only when a public-safe fixture is intentionally stress-sized and repo storage is approved. |
| `../golden/` | Top-level expected-output lane for stable cross-domain or runtime-wide outputs. |
| `../invalid/` | Top-level fail-closed lane for broad invalid examples. |
| `../ecology/` | Cross-domain ecology fixture root; public-safe ecology examples may eventually be routed there. |
| `../hydrology/` | Top-level Hydrology runtime fixture lane; water-context examples belong there when Hydrology ownership is material. |
| `../infrastructure-generalized/` | Top-level generalized-infrastructure runtime fixture lane; infrastructure examples belong there when infrastructure ownership is material. |
| `../domains/` | Domain-specific fixture homes should be preferred when the object family has a clear owner. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## Accepted material

This parent lane and its child lanes may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy public-safe settlement, ecology, hydrology context, generalized infrastructure context, map-rendering, layer, drawer, Focus Mode, governed API, source-role, evidence-ref, citation-ref, correction, rollback, or expected-output examples when a more specific owner is not yet clear;
- public-safe generalized geometries and toy attributes for renderer smoke tests, map UI checks, documentation examples, and dry-runs;
- examples that demonstrate finite outcomes without claiming source truth, domain truth, release state, public API authority, public map authority, tile authority, or publication state;
- paired expected outputs in `../golden/` or a future domain-specific golden lane when behavior becomes stable.

## Exclusions

Do not use this lane for RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data; real source exports; live upstream payloads; real legal records; real census data extracts; real historic-site records; real tribal/community records; real exact sensitive geometry; private person-land joins; ownership/title data; critical infrastructure detail; emergency alerts; lifecycle data; SourceDescriptors; actual EvidenceBundles; actual RunReceipts; proof packs; release manifests; generated CI artifacts; implementation code; public API material; public map material; public tiles; source authority; evidence authority; policy authority; proof authority; release authority; AI authority; or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, generalized, and public-safe.
- Prefer a domain-specific fixture lane when ownership is clear.
- Use toy IDs, toy refs, toy dates, toy places, toy geometries, toy source refs, toy evidence refs, toy policy refs, toy release refs, toy reviewer refs, and toy hashes.
- Prefer generalized, coarse, aggregated, or toy geometry; never include sensitive exact geometry.
- Make fixture posture explicit: public-safe, generalized, valid, invalid, negative, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, release-blocked, correction-visible, rollback-visible, or blocked render.
- Keep source role, evidence support, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as domain truth, source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or published output.

## Expected public-safe fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Settlement-side public-safe example | `settlement/` | Public-safe, generalized, review-ready, or finite governed outcome. |
| Cross-domain public-safe example without one clear owner | `./` until ownership is clear | Context-only, evidence-resolved, review-required, or bounded answer. |
| Public-safe renderer smoke example | `./`, `../slim/`, or a domain lane depending on owner | Renderer-safe output or validation failure. |
| Public-safe Evidence Drawer example | `./` or a domain-specific lane | Drawer-safe output with evidence refs visible. |
| Public-safe Focus Mode example | `./` or a domain-specific lane | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` with finite posture. |
| Stable public-safe expected output | `../golden/` or domain-specific `golden/` lane | Deterministic expected output, not release. |
| Public-safe fixture becomes domain-owned | Move to domain lane | Preserve ownership, policy, evidence, and sensitivity context. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, renderer checks, expected-output names, storage decisions, or consumer contracts are added.
- Link each stable fixture to the renderer check, governed-API dry-run, Evidence Drawer check, Focus Mode check, source-role check, evidence-resolution check, citation-validation check, release-readiness check, correction check, rollback check, sensitivity check, or documentation example that consumes it.
- Move stable domain-owned examples into the owning domain fixture lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, child README, and this parent index together.
- Keep payloads small enough for normal code review unless an explicit large-corpus storage decision exists.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, private joins, restricted cultural/community detail, infrastructure-sensitive detail, or emergency-authority content, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Child README inventory: PARTIALLY VERIFIED against populated `settlement/README.md` fetched during this update.
- Fixture payload inventory: no payload files verified under this public-safe parent lane during this update.
- Exact child-lane inventory under `fixtures/public_safe/`: PARTIALLY VERIFIED by fetching `settlement/README.md`; no exhaustive tree listing was performed.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Settlement public-safe alignment: PARTIALLY VERIFIED against `fixtures/public_safe/settlement/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, public-safe fixture checks, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, source-role checks, evidence-resolver checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
