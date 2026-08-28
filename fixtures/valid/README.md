# Valid fixtures

`fixtures/valid/`

Status: draft / top-level positive-path fixture index / synthetic valid examples.

This directory is the top-level lane for small synthetic valid fixtures when a positive-path example is broader than one domain-specific fixture lane, supports a cross-cutting runtime/rendering check, or has not yet been routed to a more specific owner. Valid fixtures describe inputs or fixture states that should produce a bounded positive posture such as validation pass, renderer-safe output, drawer-safe output, Focus Mode output, governed API dry-run success, evidence-resolved posture, source-role-preserved posture, rights-visible posture, sensitivity-reviewed posture, release-ready posture, correction-visible posture, rollback-ready posture, or deterministic expected output.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Valid fixture posture

Use this lane for synthetic inputs that should demonstrate a bounded positive path. Positive-path does not mean authoritative, released, evidence-closed, policy-approved, or implementation-proven. A valid fixture may demonstrate that an example shape is intended to pass a check, but it does not make the represented claim true.

This top-level lane is not the preferred home when a domain-specific valid or positive lane clearly owns the fixture. Use the most specific owner when practical, such as `fixtures/domains/<domain>/valid/`, a domain `positive/` lane, or an object-family-specific valid child. Keep this root for cross-domain, runtime-level, renderer-level, or not-yet-sorted positive examples.

A fixture can describe a desired valid case before validators, renderer checks, governed API routes, policy bundles, schema checks, replay checks, release integration, or CI coverage exist. Fixture success is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic positive-path examples for runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to sibling fixture lanes

| Lane | Relationship |
|---|---|
| `../invalid/` | Top-level fail-closed contrast lane for broad invalid examples. |
| `../golden/` | Top-level expected-output lane for stable synthetic outputs paired with valid or invalid inputs. |
| `../slim/` | Small runtime fixture lane; use it when the fixture is a runtime smoke input rather than a broad positive-path example. |
| `../heavy/` | Heavy runtime stress lane; use only when a positive-path fixture is intentionally stress-sized and storage is approved. |
| `../public_safe/` | Parent lane for public-safe documentation/runtime examples. |
| `../synthetic/` | Parent lane for synthetic compatibility examples before ownership is clear. |
| `../release/` | Synthetic release-governance fixture lane. |
| `../domains/` | Preferred root for domain-owned fixtures once the object family and consumer are clear. |
| `../../tests/fixtures/` | Test-only fixture home; use it for deterministic test fixtures that are not runtime/benchmark corpora. |
| `../../artifacts/` | Generated CI output home; do not treat generated artifacts as fixture authority. |
| `../../data/` | Governed lifecycle data root; real data belongs there, not here. |

## When to use this lane vs a specific valid lane

| Use case | Preferred lane | Reason |
|---|---|---|
| Domain-owned valid fixture | `fixtures/domains/<domain>/valid/` or a specific positive child lane | Domain-specific lanes preserve ownership, policy, evidence, and sensitivity context. |
| Cross-domain valid example without one clear owner | `fixtures/valid/` | This lane can stage the positive family until ownership is clear. |
| Runtime renderer or map valid smoke case | `fixtures/slim/`, `fixtures/valid/`, or runtime-specific child lane | The positive case may be runtime-wide rather than domain-owned. |
| Stable expected positive output | `fixtures/golden/` or domain `golden/` lane | Golden fixtures anchor deterministic expected outputs. |
| Test-only valid fixture not used by runtime examples | `tests/fixtures/` | Root fixture README separates runtime fixtures from deterministic test-only fixtures. |
| Real lifecycle data, proof, release, source registry, or publication material | Not fixtures | Route through the governed responsibility root and lifecycle. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.positive.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- synthetic valid inputs for runtime envelopes, renderer outputs, map layers, drawer projections, Focus Mode outputs, governed API envelopes, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ANSWER`, validation-pass, policy-pass, review-ready, renderer-safe, drawer-safe, Focus-safe, evidence-resolved, citation-ready, rights-visible, sensitivity-reviewed, source-role-preserved, release-ready, correction-visible, rollback-ready, or expected-output examples;
- contrast examples showing the difference between a valid public-safe fixture and an invalid variant;
- paired expected outputs in `../golden/` or a domain-specific golden lane when behavior becomes stable.

## Exclusions

Do not use this lane for real source records, live upstream payloads, lifecycle data, EvidenceBundles, SourceDescriptors, actual receipts, proof packs, policy decisions, review records, release manifests, rollback cards, correction notices, implementation code, public API material, public map material, public tiles, generated CI outputs, direct model runtime output, unpublished candidate content, source authority, evidence authority, policy authority, proof authority, schema authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the most specific domain or object-family valid lane when ownership is clear.
- Make the valid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ANSWER`, validation pass, policy pass, review-ready, renderer-safe, drawer-safe, Focus-safe, evidence-resolved, citation-ready, rights-visible, sensitivity-reviewed, source-role-preserved, release-ready, correction-visible, rollback-ready, or expected output.
- Pair each stable valid input with an expected output when practical.
- Keep schema validity, semantic validity, source-role validity, evidence resolution, citation validation, rights posture, sensitivity posture, policy filtering, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, replay posture, and expected-output state separate.
- Do not treat fixture success as evidence closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or published output.

## Expected top-level valid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned Hydrology, Hazards, Agriculture, Geology, Habitat, Flora, Fauna, Infrastructure, or People/DNA/Land valid example | Domain-specific `valid/` or `positive/` lane | Positive output with domain context preserved. |
| Cross-domain valid example | `fixtures/valid/` until ownership is clear | Validation pass, review-ready, or bounded answer. |
| Runtime renderer valid case | `fixtures/slim/`, `fixtures/valid/`, or runtime fixture child lane | Renderer-safe output or validation pass. |
| Evidence Drawer valid case | `fixtures/valid/` or domain-specific lane | Drawer-safe output with evidence refs visible. |
| Focus Mode valid case | `fixtures/valid/` or domain-specific lane | `ANSWER` with finite posture, or review-ready. |
| Stable positive output is ready to compare | `fixtures/golden/` or domain-specific `golden/` lane | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when child lanes, payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each valid fixture to the input fixture and the test, renderer check, governed-API contract, Evidence Drawer test, Focus Mode test, replay check, source-role check, evidence resolver, citation validator, policy check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- Move stable domain-owned valid examples into the owning domain valid or positive lane once ownership is clear.
- If expected valid behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, or private/restricted material, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced one-line stub content.
- Fixture payload inventory: no payload files verified under this top-level valid lane during this update.
- Exact child-lane inventory under `fixtures/valid/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Invalid sibling alignment: PARTIALLY VERIFIED against `fixtures/invalid/README.md`.
- Golden sibling alignment: PARTIALLY VERIFIED against `fixtures/golden/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, replay checks, source-role checks, evidence-resolver checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
