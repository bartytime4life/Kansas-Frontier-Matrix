# Ecology fixtures

`fixtures/ecology/`

Status: draft / fixture root index / cross-domain synthetic ecology examples.

This directory is for small synthetic ecology fixture examples that cut across Habitat, Flora, Fauna, Hydrology, Soil, Hazards, and related map/UI surfaces. Use it for toy ecological context examples, public-safe derivative examples, expected-output pairs, governed API dry-runs, Evidence Drawer examples, Focus Mode examples, renderer checks, source-role checks, policy dry-runs, correction checks, rollback checks, and documentation examples when the fixture is broader than one domain-specific fixture lane.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, EvidenceBundles, RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, species occurrence truth, habitat truth, flora truth, fauna truth, hydrology truth, soil truth, source authority, evidence authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture root posture

Use this lane as a cross-domain ecology fixture boundary, not as a new canonical domain. Domain-specific examples should normally live under `fixtures/domains/<domain>/`. This root is for synthetic ecology examples that intentionally exercise joins, context projections, combined map behavior, or public-safe derivative behavior across domain boundaries.

Ecology fixtures may demonstrate context, evidence refs, source-role labels, rights posture, review posture, release posture, correction posture, rollback posture, finite outcomes, and renderer/API behavior. They do not create source authority, evidence closure, policy approval, release approval, public-map authority, tile authority, implementation proof, or published output.

Habitat doctrine treats Habitat as a context lane that owns land cover, ecological systems, habitat patches, suitability surfaces, connectivity, restoration opportunity, stewardship zones, and public-safe derivatives. It explicitly does not own species occurrence truth, plant or animal taxonomy, watershed truth, soil identity, or land-management instruction. Ecology fixtures must preserve those ownership boundaries and must not collapse context into truth.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, domain root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to domain fixture lanes

| Lane | Relationship |
|---|---|
| `../domains/habitat/` | Primary adjacent fixture lane for habitat, land-cover, ecoregions, uncertainty, watcher, and habitat-fauna thin-slice examples. |
| `../domains/flora/` | Primary adjacent fixture lane for plant taxa, occurrences, public-safe occurrence derivatives, vegetation communities, phenology, source descriptors, and Flora decision envelopes. |
| `../domains/fauna/` | Expected adjacent fixture lane for animal occurrence, species, sensitivity, and habitat-fauna examples if present. |
| `../domains/hydrology/` | Adjacent fixture lane for watershed, evidence-bundle, decision-envelope, RunReceipt, source, valid, invalid, negative, and golden Hydrology examples. |
| `../domains/soil/` | Expected adjacent fixture lane for soil context and soil-map-unit examples if present. |
| `../domains/hazards/` | Adjacent fixture lane for environmental hazard context, trust-membrane, drawer, Focus Mode, layer-manifest, and invalid examples. |
| `../domains/` | Domain-specific fixture homes should be preferred when the object family has a clear owner. |

## When to use this root vs domain-specific fixture lanes

| Use case | Preferred lane | Reason |
|---|---|---|
| Habitat object, land-cover observation, ecoregion, uncertainty, watcher, or habitat-fauna thin slice | `../domains/habitat/` | Habitat already has a populated fixture root and child lanes. |
| Flora object, plant taxon, plant occurrence, vegetation community, phenology, or Flora source example | `../domains/flora/` | Flora already has a populated fixture root and child lanes. |
| Hydrology evidence, watershed, source, RunReceipt, or decision-envelope example | `../domains/hydrology/` | Hydrology has a populated fixture root and object-specific lanes. |
| Cross-domain ecology example with no single owner yet | `./` | This root can stage bounded synthetic examples until ownership is clear. |
| Stable expected output for a cross-domain ecology fixture | `./golden/` if added, or a documented expected-output pair | Expected outputs must remain synthetic and non-release. |
| Real source material, lifecycle data, actual EvidenceBundle, actual RunReceipt, release manifest, public tile, or published map output | Not fixtures | Route through the governed responsibility root and lifecycle. |

## Related references

- `../README.md`
- `../domains/habitat/README.md`
- `../domains/flora/README.md`
- `../domains/hydrology/README.md`
- `../domains/hazards/README.md`
- `../../docs/domains/habitat/README.md`
- `../../docs/domains/habitat/ARCHITECTURE.md`
- `../../docs/domains/habitat/sublanes/ecoregions.md`
- `../../docs/domains/habitat/sublanes/land_cover.md`
- `../../docs/domains/flora/API_CONTRACTS.md`
- `../../docs/domains/flora/SENSITIVITY.md`
- `../../docs/domains/fauna/ARCHITECTURE.md`
- `../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../docs/domains/hazards/API_CONTRACTS.md`
- `../../contracts/domains/habitat/`
- `../../contracts/domains/flora/`
- `../../contracts/domains/fauna/`
- `../../contracts/domains/hydrology/`
- `../../schemas/contracts/v1/domains/habitat/`
- `../../schemas/contracts/v1/domains/flora/`
- `../../schemas/contracts/v1/domains/fauna/`
- `../../schemas/contracts/v1/domains/hydrology/`
- `../../policy/domains/habitat/`
- `../../policy/domains/flora/`
- `../../policy/domains/fauna/`
- `../../policy/sensitivity/habitat/`
- `../../policy/sensitivity/flora/`
- `../../policy/sensitivity/fauna/`
- `../../data/registry/sources/habitat/`
- `../../data/registry/sources/flora/`
- `../../data/registry/sources/fauna/`
- `../../release/manifests/habitat/`
- `../../release/manifests/flora/`
- `../../release/manifests/fauna/`
- `../../docs/doctrine/directory-rules.md`

## Accepted material

This root may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy ecological context refs, habitat refs, taxon refs, occurrence refs, watershed refs, soil refs, hazard refs, source refs, evidence refs, policy refs, review refs, release refs, correction refs, rollback refs, finite outcomes, and renderer/API examples;
- toy cross-domain examples for habitat-flora, habitat-fauna, habitat-hydrology, habitat-soil, ecology-hazards, or map/UI ecology overlays;
- toy public-safe derivatives where protected or restricted ecology details are withheld, generalized, delayed, denied, or routed to review;
- expected-output examples when a synthetic input becomes stable enough to anchor a regression check;
- README files documenting fixture intent, boundaries, consumer checks, and verification state.

## Exclusions

Do not use this root for real records, source exports, lifecycle data, actual EvidenceBundles, actual RunReceipts, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, evidence authority, policy authority, release authority, protected exact locations, restricted ecological joins, canonical ecology truth, Habitat truth, Flora truth, Fauna truth, Hydrology truth, Soil truth, Hazards truth, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the most specific domain fixture lane when ownership is clear.
- Use toy IDs, toy refs, toy taxa, toy sources, toy timestamps, toy hashes, toy evidence references, toy geometries, and toy expected outputs.
- Make fixture posture explicit: valid, invalid, negative, expected output, context-only, proof-support, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, rights-visible, rights-missing, review-required, deny, hold, abstain, release-ready, release-blocked, correction-visible, rollback-ready, or blocked render.
- Keep source role, evidence state, rights state, review state, release state, correction state, rollback state, and expected outcome explicit where material.
- Pair each stable input with an expected output when practical.
- Keep schema validity, semantic validity, source-role validity, evidence support, citation safety, policy admissibility, release posture, renderer safety, trust-membrane safety, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success as implementation proof, source authority, evidence closure, policy approval, release state, public-map authority, tile authority, or published output.

## Expected fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Habitat ecoregion or land-cover context | `../domains/habitat/` | Validation pass, review-ready, or expected output. |
| Flora occurrence or public-safe plant derivative | `../domains/flora/` | Validation pass, review-ready, generalized, denied, or review-required. |
| Fauna occurrence or species-related public-safe derivative | `../domains/fauna/` if present; otherwise this root until sorted | Validation pass, generalized, denied, or review-required. |
| Habitat-Flora cross-domain example | `./` until ownership is clear, then domain-specific lane | Context-only, evidence-resolved, or review-required. |
| Habitat-Fauna thin slice | `../domains/habitat/habitat_fauna_thin_slice/` | Proof-support or review-ready where present. |
| Habitat-Hydrology wetland/watershed context | `./` or `../domains/hydrology/` depending on owner | Context-only, evidence-resolved, or bounded answer. |
| Restricted exact location appears | Domain-specific invalid lane or this root until sorted | `DENY`, blocked render, or validation failure. |
| Stable expected cross-domain output | Future `golden/` or documented expected-output pair | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- Move stable domain-specific examples to the owning domain fixture lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, protected exact locations, restricted ecology data, actual proof material, or release material, move it out of this root, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this root during this update.
- Exact child-lane inventory under `fixtures/ecology/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Habitat fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/README.md`.
- Flora fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/flora/README.md`.
- Habitat architecture alignment: PARTIALLY VERIFIED against `docs/domains/habitat/ARCHITECTURE.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, ecology fixture checks, habitat checks, flora checks, fauna checks, hydrology joins, soil joins, hazards joins, source-role checks, evidence-bundle checks, citation-validation checks, rights checks, decision-envelope checks, drawer checks, Focus Mode checks, release-readiness checks, correction checks, rollback checks, schema checks, policy checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
