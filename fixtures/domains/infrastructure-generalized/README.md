# Infrastructure-generalized fixtures

`fixtures/domains/infrastructure-generalized/`

Status: draft / fixture parent index / generalized infrastructure synthetic examples.

This directory is for small synthetic generalized-infrastructure fixture examples. Use it to stage public-safe, generalized, redacted, aggregated, or toy examples that exercise infrastructure rendering, sensitivity handling, cross-lane references, release-readiness checks, EvidenceBundle references, RunReceipt references, decision envelopes, layer manifests, map/UI behavior, correction posture, rollback posture, and expected outputs.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, proof packs, policy decisions, review approvals, release state, public API material, public map material, public tiles, infrastructure truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Fixture root posture

This lane exists for **generalized** infrastructure examples. It is not the canonical home for infrastructure truth or infrastructure contracts. The Settlements/Infrastructure domain owns infrastructure-side object families such as physical assets, network nodes, network segments, facilities, service areas, operators, observations, and dependency relations. Roads/Rail/Trade may reference infrastructure through crossings, facilities, corridors, and transport relations, but those joins must preserve ownership and sensitivity boundaries.

The default posture is public-safe synthetic data only. Do not include real exact infrastructure locations, restricted attributes, sensitive operational details, restricted-source terms, or any geometry that could reasonably be mistaken for real sensitive infrastructure.

A fixture may describe intended behavior before the corresponding validator, route, policy bundle, UI surface, release gate, or CI check exists. When implementation is not verified, the README must say so.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to infrastructure governance

| Lane or document | Relationship |
|---|---|
| `../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md` | Infrastructure-side object-family dossier; governs asset, network, facility, service-area, operator, observation, and dependency meaning. |
| `../../docs/domains/roads-rail-trade/SENSITIVITY.md` | Roads/Rail/Trade sensitivity and publication posture for transport-adjacent infrastructure and corridor examples. |
| `../../contracts/domains/settlements-infrastructure/` | Contract home for Settlements/Infrastructure meaning; fixtures do not define contracts. |
| `../../contracts/domains/roads-rail-trade/` | Contract home for transport network objects; fixtures do not define transport truth. |
| `../../policy/sensitivity/infrastructure/` | Expected sensitivity-policy home for infrastructure; fixtures do not decide policy. |
| `../../policy/sensitivity/transport/` | Expected sensitivity-policy home for transport; fixtures do not decide policy. |
| `../../data/processed/settlements-infrastructure/` | Processed lifecycle lane if implementation exists; fixtures do not replace lifecycle data. |
| `../../data/processed/roads-rail-trade/` | Processed transport lifecycle lane if implementation exists; fixtures do not replace lifecycle data. |
| `../../release/candidates/` and `../../release/manifests/` | Release homes if present; fixtures do not publish. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.golden.json`, `*.geojson`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy generalized point, line, polygon, tile, layer, drawer, Focus Mode, export, or expected-output examples;
- toy infrastructure asset, facility, service-area, network-node, network-segment, operator, dependency, bridge, crossing, corridor, route-adjacent, or utility-context examples when generalized enough for public-safe fixture use;
- toy sensitivity-tier examples showing open, generalized, reviewer, restricted, and denied outcomes;
- toy transform examples for redaction, generalization, aggregation, coarse depiction, attribute stripping, sensitivity downgrade, correction, rollback, or blocked render;
- toy cross-lane examples where Settlements/Infrastructure owns infrastructure identity while Roads/Rail, Hydrology, Hazards, Archaeology, or People/Land references remain citation-only;
- paired expected outputs in a future `golden/` child or sibling expected-output lane when behavior stabilizes.

## Exclusions

Do not use this lane for real records, real source exports, lifecycle data, SourceDescriptors, actual EvidenceBundles, actual RunReceipts, source activation decisions, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, real exact infrastructure geometry, sensitive operational details, restricted-source-derived fields, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer generalized, coarse, or toy geometry; never include sensitive exact geometry.
- Use toy IDs, refs, timestamps, digests, checksums, hashes, source descriptor refs, evidence refs, validation refs, policy refs, release refs, reviewer refs, and transform refs.
- Make fixture posture explicit: generalized, redacted, aggregated, public-safe, reviewer-only, restricted, denied, valid, invalid, negative, expected output, source-role-preserved, source-role-conflicted, evidence-resolved, evidence-missing, citation-ready, citation-failed, rights-visible, rights-missing, sensitivity-visible, sensitivity-missing, provenance-resolved, replay-reviewable, release-blocked, correction-visible, rollback-visible, or blocked render.
- Pair each stable input with an expected output when practical.
- Keep source admission, source role, evidence support, receipt provenance, citation validation, rights posture, sensitivity posture, policy filtering, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, and expected-output state separate.
- Do not treat fixture success or failure as source admission, SourceDescriptor authority, EvidenceBundle closure, RunReceipt storage proof, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Generalized infrastructure asset marker | Public-safe or validation pass | Must be toy/generalized, not real exact geometry. |
| Generalized facility service area | Public-safe or review-ready | Service area may be aggregate/coarse. |
| Transport crossing or route-adjacent context | Public-safe only after sensitivity review | Ownership and source role remain explicit. |
| Dependency sketch | Reviewer-only, restricted, denied, or synthetic-only | Real dependency information remains outside fixtures unless governed. |
| Redacted layer-manifest example | Validation pass or blocked render | Layer metadata may be public-safe while sensitive geometry is withheld. |
| Drawer or Focus Mode context | `ANSWER`, `ABSTAIN`, or `DENY` as governed | Generated text remains interpretive and evidence-bound. |
| Missing evidence, rights, sensitivity, or release state | `ABSTAIN`, `DENY`, validation failure, or review-required | Cite-or-abstain and deny-by-default remain visible. |
| Sensitive exact geometry included | `DENY` or validation failure | Sensitive exact geometry does not belong in fixtures. |

## Maintenance notes

- Update this README when child lanes, payload files, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each stable fixture to the exact check and consumer that uses it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real infrastructure material, sensitive exact geometry, restricted operational detail, source exports, or release material, move it out of this root, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified under this root during this update.
- Exact prior fixture precedent for `fixtures/domains/infrastructure-generalized/`: NOT FOUND in repository search during this update.
- Settlements/Infrastructure alignment: PARTIALLY VERIFIED against `docs/domains/settlements-infrastructure/sublanes/infrastructure.md`.
- Roads/Rail/Trade sensitivity alignment: PARTIALLY VERIFIED against `docs/domains/roads-rail-trade/SENSITIVITY.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, generalized-infrastructure checks, sensitivity checks, source-descriptor checks, source-role checks, evidence-bundle checks, run-receipt checks, decision-envelope checks, layer-manifest checks, drawer checks, Focus Mode checks, map/UI checks, release-readiness checks, schema checks, policy checks, renderer checks, correction checks, rollback checks, and CI implementation.
- Tests and validators: NOT RUN.
