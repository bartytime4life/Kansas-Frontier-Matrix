# Golden fixtures

`fixtures/golden/`

Status: draft / top-level expected-output fixture index / synthetic golden examples.

This directory is the top-level lane for small synthetic golden fixtures when an expected output is broader than one domain-specific fixture lane, supports a cross-cutting runtime/rendering check, or has not yet been routed to a more specific owner. Golden fixtures describe the expected result for known synthetic inputs used by bounded checks, renderer smoke tests, governed API dry-runs, Evidence Drawer examples, Focus Mode examples, policy dry-runs, replay checks, documentation examples, and regression comparisons.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Golden fixture posture

Use this lane for stable expected outputs paired with synthetic inputs. A golden fixture should make the expected finite posture explicit, such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, policy pass, policy failure, renderer-safe output, drawer-safe output, Focus Mode output, replay pass, replay failure, blocked render, blocked projection, release-ready, release-blocked, correction-visible, rollback-ready, or another documented expected outcome.

This top-level lane is not the preferred home when a domain-specific golden lane clearly owns the fixture. Use the most specific owner when practical, such as `fixtures/domains/<domain>/golden/`. Keep this root for cross-domain, runtime-level, renderer-level, or not-yet-sorted expected outputs.

A golden fixture can describe expected behavior before validators, renderer checks, governed API routes, policy bundles, schema checks, replay checks, release integration, or CI coverage exist. Fixture success is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic expected-output examples for runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to domain golden lanes

| Lane | Relationship |
|---|---|
| `../domains/habitat/golden/` | Domain-specific expected outputs for Habitat fixture inputs. |
| `../domains/flora/golden/` | Domain-specific expected outputs for Flora fixture inputs. |
| `../domains/fauna/golden/` | Domain-specific expected outputs for Fauna fixture inputs, if present. |
| `../domains/hydrology/golden/` | Domain-specific expected outputs for Hydrology fixture inputs. |
| `../domains/hazards/golden/` | Domain-specific expected outputs for Hazards fixture inputs. |
| `../domains/geology/golden/` | Domain-specific expected outputs for Geology fixture inputs. |
| `../domains/people-dna-land/golden/` | Domain-specific expected outputs for People/DNA/Land fixture inputs. |
| `../generated_receipt/valid/` and `../generated_receipt/invalid/` | Receipt-like fixtures may produce expected outputs, but they remain synthetic and non-authoritative. |
| `../ecology/` | Cross-domain ecology fixtures may use this lane for stable expected outputs until a domain owner is clear. |

## When to use this lane vs a specific golden lane

| Use case | Preferred lane | Reason |
|---|---|---|
| Domain-owned expected output | `fixtures/domains/<domain>/golden/` | Domain-specific lanes preserve ownership and policy context. |
| Cross-domain expected output without one clear owner | `fixtures/golden/` | This lane can stage the expected output until ownership is clear. |
| Runtime renderer or map smoke expected output | `fixtures/golden/` or runtime-specific child lane | The expected output may be runtime-wide rather than domain-owned. |
| Stable generated-receipt expected output | `fixtures/generated_receipt/` plus documented expected pair | Receipt fixtures stay separate from actual receipt storage. |
| Test-only expected output not used by runtime examples | `tests/fixtures/` | Root fixture README separates runtime fixture inputs from deterministic test-only fixtures. |
| Generated CI output | `artifacts/` | CI artifacts are not fixture authority. |
| Real lifecycle data, proof, release, source registry, or publication material | Not fixtures | Route through the governed responsibility root and lifecycle. |

## Accepted material

This lane may contain:

- small synthetic `*.expected.json`, `*.expected.geojson`, `*.expected.jsonl`, `*.expected.yaml`, `*.expected.yml`, `*.expected.svg`, `*.golden.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- expected positive-path outputs for synthetic public-safe fixture inputs;
- expected fail-closed outputs for invalid, denied, abstained, blocked, stale, unresolved, unsupported, or review-required fixture inputs;
- expected renderer, map, Evidence Drawer, Focus Mode, governed API, replay, policy, citation, source-role, correction, rollback, or documentation-example outputs;
- paired expected outputs for inputs stored in sibling fixture lanes;
- README files documenting fixture intent, boundaries, consumer checks, and verification state.

## Exclusions

Do not use this lane for real source records, live upstream payloads, lifecycle data, EvidenceBundles, SourceDescriptors, actual receipts, proof packs, policy decisions, review records, release manifests, rollback cards, correction notices, implementation code, public API material, public map material, public tiles, generated CI outputs, direct model runtime output, unpublished candidate content, source authority, evidence authority, policy authority, proof authority, schema authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep expected outputs synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the most specific domain or object-family golden lane when ownership is clear.
- Pair golden outputs with a clearly named input fixture whenever practical.
- Use naming that makes the relationship obvious, such as `<scenario>.input.json` in an input lane and `<scenario>.expected.json` in this lane, or an equivalent documented pair.
- Keep expected outcomes explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, validation pass, validation failure, policy pass, policy failure, replay pass, replay failure, renderer-safe output, drawer-safe output, Focus Mode output, blocked render, blocked projection, release-ready, release-blocked, correction-visible, rollback-ready, or another documented finite posture.
- Keep source role, evidence state, rights state, sensitivity state, policy state, freshness state, review state, release state, correction state, rollback state, replay state, and expected-output state explicit where material.
- Treat `schema-valid`, `semantic-valid`, `source-role-valid`, `evidence-resolved`, `citation-safe`, `policy-admissible`, `release-safe`, `renderer-safe`, `drawer-safe`, `focus-safe`, and `replay-stable` as separate checks.
- Do not treat golden fixtures as evidence, approval, release state, proof authority, source authority, schema authority, implementation proof, public-map authority, tile authority, or published output.

## Expected top-level golden fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned Habitat, Flora, Fauna, Hydrology, Hazards, Geology, or People/DNA/Land output | Domain-specific `golden/` lane | Deterministic expected output with domain context preserved. |
| Cross-domain ecology expected output | `fixtures/golden/` until ownership is clear | Context-only, evidence-resolved, review-required, or bounded answer. |
| Runtime renderer smoke expected output | `fixtures/golden/` or runtime fixture child lane | Renderer-safe output or validation failure. |
| Evidence Drawer expected output | `fixtures/golden/` or domain-specific lane | Drawer-safe output with evidence refs visible. |
| Focus Mode expected output | `fixtures/golden/` or domain-specific lane | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` with finite posture. |
| Generated-receipt expected output | `fixtures/generated_receipt/` with documented pair | Receipt summary or validation result, not actual receipt authority. |
| Stable expected output becomes release-like | Move concern to release lane | Golden fixtures must not become release artifacts. |

## Maintenance notes

- Update this README when child lanes, payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each golden fixture to the input fixture and the test, renderer check, governed-API contract, Evidence Drawer test, Focus Mode test, replay check, source-role check, evidence resolver, policy check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- Move stable domain-owned expected outputs into the owning domain golden lane once ownership is clear.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, or sensitive exact geometry, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced one-line stub content.
- Fixture payload inventory: no payload files verified under this top-level golden lane during this update.
- Exact child-lane inventory under `fixtures/golden/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Habitat golden alignment: PARTIALLY VERIFIED against `fixtures/domains/habitat/golden/README.md`.
- Flora golden alignment: PARTIALLY VERIFIED against `fixtures/domains/flora/golden/README.md`.
- Domain golden inventory: PARTIALLY VERIFIED by repository search for populated domain golden README paths.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, replay checks, source-role checks, evidence-resolver checks, citation-validation checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
