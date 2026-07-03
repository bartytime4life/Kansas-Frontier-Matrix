# Invalid fixtures

`fixtures/invalid/`

Status: draft / top-level fail-closed fixture index / synthetic invalid examples.

This directory is the top-level lane for small synthetic invalid fixtures when a fail-closed example is broader than one domain-specific fixture lane, supports a cross-cutting runtime/rendering check, or has not yet been routed to a more specific owner. Invalid fixtures describe inputs or fixture states that should not produce a normal public answer, public map state, public export, drawer projection, Focus Mode answer, layer resolver output, release-ready artifact, or canonical claim.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

## Invalid fixture posture

Use this lane for synthetic inputs that should fail closed. Expected outcomes may include `ABSTAIN`, `DENY`, `ERROR`, validation failure, policy failure, replay failure, review-required, blocked render, blocked projection, release-readiness failure, evidence-resolution failure, citation-validation failure, source-role failure, rights/sensitivity failure, correction-required, rollback-required, or trust-membrane failure.

This top-level lane is not the preferred home when a domain-specific invalid lane clearly owns the fixture. Use the most specific owner when practical, such as `fixtures/domains/<domain>/invalid/`, a domain `negative/` lane, or an object-family-specific `invalid/` child. Keep this root for cross-domain, runtime-level, renderer-level, or not-yet-sorted invalid examples.

A fixture can describe a desired invalid case before validators, renderer checks, governed API routes, policy bundles, schema checks, replay checks, release integration, or CI coverage exist. Fixture failure is not implementation proof by itself.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic fail-closed examples for runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also separates `fixtures/` from `tests/fixtures/`, `artifacts/`, and `data/`, and says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here.

## Relationship to domain invalid lanes

| Lane | Relationship |
|---|---|
| `../domains/hydrology/invalid/` | Domain-specific Hydrology invalid parent lane for fail-closed Hydrology examples. |
| `../domains/hazards/invalid/` | Domain-specific Hazards invalid lane if present. |
| `../domains/agriculture/invalid/` | Domain-specific Agriculture invalid lane if present. |
| `../domains/people-dna-land/invalid/` | Domain-specific People/DNA/Land invalid parent lane for privacy, consent, identity, land-link, evidence, and release failures. |
| `../domains/geology/invalid/` | Domain-specific Geology invalid lane if present. |
| `../domains/habitat/invalid/` | Domain-specific Habitat invalid lane if present. |
| `../generated_receipt/invalid/` | Generated-receipt invalid lane for receipt-shape, outcome, replay, policy, and projection failures. |
| `../golden/` | Stable fail-closed expected outputs may be paired there when they are cross-domain or runtime-wide. |

## When to use this lane vs a specific invalid lane

| Use case | Preferred lane | Reason |
|---|---|---|
| Domain-owned invalid fixture | `fixtures/domains/<domain>/invalid/` or a specific child lane | Domain-specific lanes preserve ownership, policy, evidence, and sensitivity context. |
| Domain-owned exploratory negative fixture | Domain `negative/` lane if present | Keeps draft negative scenarios close to the owning domain. |
| Cross-domain invalid example without one clear owner | `fixtures/invalid/` | This lane can stage the fail-closed family until ownership is clear. |
| Runtime renderer or map invalid smoke case | `fixtures/invalid/` or runtime-specific child lane | The failure may be runtime-wide rather than domain-owned. |
| Stable expected fail-closed output | `fixtures/golden/` or domain `golden/` lane | Golden fixtures anchor deterministic expected outputs. |
| Generated-receipt invalid example | `fixtures/generated_receipt/invalid/` | Receipt fixtures stay separate from actual receipt storage. |
| Test-only invalid fixture not used by runtime examples | `tests/fixtures/` | Root fixture README separates runtime fixtures from deterministic test-only fixtures. |
| Real lifecycle data, proof, release, source registry, or publication material | Not fixtures | Route through the governed responsibility root and lifecycle. |

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- synthetic invalid inputs for runtime envelopes, renderer outputs, map layers, drawer projections, Focus Mode outputs, governed API envelopes, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ABSTAIN`, `DENY`, `ERROR`, validation-failure, policy-failure, replay-failure, review-required, blocked-render, blocked-projection, evidence-missing, citation-failed, rights-missing, sensitivity-missing, source-role-conflicted, release-blocked, correction-required, rollback-required, or expected-output examples;
- contrast examples showing the difference between a valid public-safe fixture and an invalid variant;
- paired expected outputs in `../golden/` or a domain-specific golden lane when behavior becomes stable.

## Exclusions

Do not use this lane for real source records, live upstream payloads, lifecycle data, EvidenceBundles, SourceDescriptors, actual receipts, proof packs, policy decisions, review records, release manifests, rollback cards, correction notices, implementation code, public API material, public map material, public tiles, generated CI outputs, direct model runtime output, unpublished candidate content, source authority, evidence authority, policy authority, proof authority, schema authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the most specific domain or object-family invalid lane when ownership is clear.
- Make the invalid condition explicit in the file name, payload, expected output, and consumer notes.
- Make expected outcome explicit when known: `ABSTAIN`, `DENY`, `ERROR`, validation failure, policy failure, replay failure, review-required, blocked render, blocked projection, release-readiness failure, correction-required, rollback-required, or expected output.
- Pair each stable invalid input with an expected failure output when practical.
- Keep schema validity, semantic validity, source-role validity, evidence resolution, citation validation, rights posture, sensitivity posture, policy filtering, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, replay posture, and expected-output state separate.
- Do not treat fixture failure as evidence closure, policy approval, validator implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or published output.

## Expected top-level invalid fixture families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned Hydrology, Hazards, Agriculture, Geology, Habitat, Flora, Fauna, Infrastructure, or People/DNA/Land invalid example | Domain-specific `invalid/` or `negative/` lane | Fail-closed output with domain context preserved. |
| Cross-domain invalid example | `fixtures/invalid/` until ownership is clear | `ABSTAIN`, `DENY`, validation failure, or review-required. |
| Runtime renderer invalid case | `fixtures/invalid/` or runtime fixture child lane | Blocked render or validation failure. |
| Evidence Drawer invalid case | `fixtures/invalid/` or domain-specific lane | Blocked projection or drawer-safe failure. |
| Focus Mode invalid case | `fixtures/invalid/` or domain-specific lane | `ABSTAIN`, `DENY`, or `ERROR` with finite posture. |
| Generated-receipt invalid case | `fixtures/generated_receipt/invalid/` | Validation failure, policy failure, replay failure, `DENY`, or `ERROR`. |
| Stable fail-closed output is ready to compare | `fixtures/golden/` or domain-specific `golden/` lane | Deterministic expected output, not release. |

## Maintenance notes

- Update this README when child lanes, payload files, input fixture lanes, validators, tests, helper scripts, expected-output names, or consumer contracts are added.
- Link each invalid fixture to the input fixture and the test, renderer check, governed-API contract, Evidence Drawer test, Focus Mode test, replay check, source-role check, evidence resolver, citation validator, policy check, release-readiness check, correction check, rollback check, or documentation example that consumes it.
- Move stable domain-owned invalid examples into the owning domain invalid or negative lane once ownership is clear.
- If expected invalid behavior stabilizes, update the paired input, expected output, consumer notes, and this root index together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, or private/restricted material, move it out of this lane, quarantine it through the governed lifecycle or responsibility root, and record the correction path.

## Verification status

- Target README: replaced one-line stub content.
- Fixture payload inventory: no payload files verified under this top-level invalid lane during this update.
- Exact child-lane inventory under `fixtures/invalid/`: NOT VERIFIED during this update.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Hydrology invalid alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/invalid/README.md`.
- People/DNA/Land invalid alignment: PARTIALLY VERIFIED against `fixtures/domains/people-dna-land/invalid/README.md`.
- Domain invalid inventory: PARTIALLY VERIFIED by repository search for populated domain invalid README paths.
- Consumer alignment: NEEDS VERIFICATION against validators, renderer checks, governed-API tests, Evidence Drawer tests, Focus Mode tests, replay checks, source-role checks, evidence-resolver checks, citation-validation checks, rights checks, sensitivity checks, policy checks, release-readiness checks, correction checks, rollback checks, schema checks, and CI implementation.
- Tests and validators: NOT RUN.
