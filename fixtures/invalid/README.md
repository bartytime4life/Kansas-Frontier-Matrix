# Invalid fixtures

`fixtures/invalid/`

Status: draft / top-level fail-closed fixture index / synthetic invalid examples.

This directory is the top-level lane for small synthetic invalid fixtures when a fail-closed example is broader than one domain-specific fixture lane, supports a cross-cutting runtime or rendering check, or has not yet been routed to a more specific owner. Invalid fixtures describe inputs or fixture states that should not produce a normal public answer, public map state, public export, drawer projection, Focus Mode answer, layer-resolver output, release-ready artifact, or canonical claim.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, SourceDescriptors, RunReceipts, proof packs, policy decisions, review approvals, release manifests, public API material, public map material, public tiles, canonical truth, source authority, evidence authority, policy authority, proof authority, release authority, AI authority, or published artifacts.

> [!IMPORTANT]
> A rejected fixture proves only the behavior exercised by the check that consumed it. It does not prove evidence closure, policy approval, release readiness, publication safety, or complete fail-closed coverage.

## Quick navigation

- [Scope and audience](#scope-and-audience)
- [Repository fit and placement](#repository-fit-and-placement)
- [Related fixture lanes](#related-fixture-lanes)
- [Choosing a fixture lane](#choosing-a-fixture-lane)
- [Accepted material](#accepted-material)
- [Adding an invalid fixture](#adding-an-invalid-fixture)
- [Maintenance checklist](#maintenance-checklist)
- [Verification status](#verification-status)

## Scope and audience

This README is for maintainers, fixture authors, validator and test owners, renderer and governed-API implementers, policy reviewers, and documentation reviewers who need to place or review a cross-cutting negative example.

Use this lane for synthetic inputs that should fail closed. Expected results may include `ABSTAIN`, `DENY`, `ERROR`, validation failure, policy failure, replay failure, review-required, blocked render, blocked projection, release-readiness failure, evidence-resolution failure, citation-validation failure, source-role failure, rights or sensitivity failure, correction-required, rollback-required, or trust-membrane failure.

This README governs fixture placement, boundaries, and review expectations. It does not define object meaning, machine shape, policy decisions, validator behavior, runtime behavior, or release authority. Those responsibilities remain with the applicable contracts, schemas, policies, implementation, tests, and governed release records.

## Invalid fixture posture

The top-level lane is not the preferred home when a domain-specific or object-family-specific invalid lane clearly owns the fixture. Use the most specific owner when practical, such as `fixtures/domains/<domain>/invalid/`, a domain `negative/` lane, or an object-family-specific `invalid/` child. Keep this root for cross-domain, runtime-wide, renderer-wide, or not-yet-sorted invalid examples.

A fixture may describe a desired invalid case before validators, renderer checks, governed API routes, policy bundles, schema checks, replay checks, release integration, or CI coverage exist. Mark that implementation boundary explicitly; fixture content is not implementation proof by itself.

## Repository fit and placement

[Directory Rules](../../docs/architecture/directory-rules.md) places golden, valid, and invalid sample data under the canonical `fixtures/` responsibility root and domain-owned examples under `fixtures/domains/<domain>/`. The [fixture root README](../README.md) defines root fixtures as cross-cutting reusable runtime and synthetic examples, while [`tests/fixtures/`](../../tests/fixtures/README.md) is for fixtures local to particular tests.

This lane is therefore a cross-cutting fixture index. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, artifact root, or publication root.

Do not place RAW, WORK, QUARANTINE, or other real lifecycle data here. Do not place secrets, private information, rights-restricted material, sensitive exact geometry, or real person, DNA, archaeological, ecological, infrastructure, or title data here. Route such material through the applicable governed lifecycle, sensitivity, rights, and quarantine controls.

### Verified direct entry

The bounded repository inspection for this revision verified this README as a direct entry:

```text
fixtures/invalid/
└── README.md
```

This is not an exhaustive tree claim. Direct child lanes and payload files remain **NEEDS VERIFICATION** until an authoritative tree walk confirms them.

## Related fixture lanes

Use these verified lanes when they provide the more specific owner:

| Lane | Relationship |
|---|---|
| [Agriculture invalid fixtures](../domains/agriculture/invalid/) | Domain-specific Agriculture validation, policy, sensitivity, and aggregation failures. |
| [Fauna invalid fixtures](../domains/fauna/invalid/) | Domain-specific Fauna negative cases, including public-safe and sensitivity boundaries. |
| [Flora invalid fixtures](../domains/flora/invalid/) | Domain-specific Flora negative cases, including geoprivacy and publication boundaries. |
| [Geology invalid fixtures](../domains/geology/invalid/) | Domain-specific Geology semantic, topology, source, renderer, and release failures. |
| [Habitat invalid fixtures](../domains/habitat/invalid/) | Domain-specific Habitat hierarchy, topology, model, context-join, policy, and release failures. |
| [Hazards invalid fixtures](../domains/hazards/invalid/) | Domain-specific Hazards evidence, freshness, policy, source-role, and public-safe UI failures. |
| [Hydrology invalid fixtures](../domains/hydrology/invalid/) | Domain-specific Hydrology evidence, decision-envelope, citation, source-role, and release failures. |
| [People/DNA/Land invalid fixtures](../domains/people-dna-land/invalid/) | Deny-first privacy, consent, identity, genealogy, DNA, land-link, rights, and sensitivity failures. |
| [`GENERATED_RECEIPT` invalid fixtures](../generated_receipt/invalid/) | Invalid generated-work receipt candidates; not actual receipt storage. |
| [Golden fixtures](../golden/) | Stable deterministic expected outputs paired with reviewed inputs. |
| [Test-local fixtures](../../tests/fixtures/) | Fixtures owned by particular tests rather than cross-cutting reusable examples. |

The table is a navigation aid. Lane existence and README coverage do not prove payload inventory, consumer wiring, test coverage, runtime enforcement, release readiness, or publication state.

## Choosing a fixture lane

| Use case | Preferred lane | Reason |
|---|---|---|
| Domain-owned invalid fixture | `fixtures/domains/<domain>/invalid/` or a verified specific child lane | Preserves domain ownership, policy, evidence, rights, and sensitivity context. |
| Domain-owned exploratory negative fixture | Domain `negative/` lane when that convention is established | Keeps draft negative scenarios close to the owning domain. |
| Object-family invalid fixture | Object-family-specific `invalid/` lane | Keeps the fixture aligned with its contract, schema, policy, validator, and consumer. |
| Cross-domain invalid example without one clear owner | `fixtures/invalid/` | Provides a bounded staging lane until ownership is resolved. |
| Runtime-wide renderer or map invalid smoke case | `fixtures/invalid/` or a verified runtime-specific child lane | The failure crosses domain ownership. |
| Stable expected fail-closed output | `fixtures/golden/` or a domain-specific `golden/` lane | Golden fixtures anchor deterministic expected outputs. |
| Invalid generated-work receipt candidate | `fixtures/generated_receipt/invalid/` | Keeps generated-work receipt fixtures separate from emitted receipts and runtime AIReceipt fixtures. |
| Test-only invalid fixture | `tests/fixtures/` or the test's established local fixture lane | Keeps test-local data with its consumer and avoids a competing shared fixture authority. |
| Real lifecycle data, proof, release, source-registry, or publication material | Not fixtures | Route it through the governed responsibility root and lifecycle. |

When ownership is unresolved, document the uncertainty rather than duplicating the fixture across lanes. Move the fixture to the specific owner once that ownership is verified, updating consumers and links in the same change.

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.invalid.json`, `*.negative.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- cross-cutting invalid inputs for runtime envelopes, renderer outputs, map layers, drawer projections, Focus Mode outputs, governed API envelopes, source-role checks, evidence-resolution checks, citation-validation checks, rights checks, sensitivity checks, release-readiness checks, correction checks, rollback checks, and trust-membrane checks;
- toy `ABSTAIN`, `DENY`, `ERROR`, validation-failure, policy-failure, replay-failure, review-required, blocked-render, blocked-projection, evidence-missing, citation-failed, rights-missing, sensitivity-missing, source-role-conflicted, release-blocked, correction-required, rollback-required, or expected-output examples;
- contrast cases that show why a public-safe valid fixture passes while an invalid variant fails;
- links to paired expected outputs in `../golden/` or a domain-specific golden lane after the behavior and consumer convention stabilize.

Use the extension, file naming, and expected-result convention already established by the fixture's verified consumer. Do not create a new object contract or schema through fixture naming alone.

## Exclusions

Do not use this lane for real source records, live upstream payloads, lifecycle data, EvidenceBundles, SourceDescriptors, actual receipts, proof packs, policy decisions, review records, release manifests, rollback cards, correction notices, implementation code, public API material, public map material, public tiles, generated CI outputs, direct model runtime output, unpublished candidate content, source authority, evidence authority, policy authority, proof authority, schema authority, release authority, AI authority, or published artifacts.

## Adding an invalid fixture

1. **Choose the narrowest verified owner.** Prefer a domain or object-family invalid lane. Use this top-level lane only for a genuinely cross-cutting or unresolved case.
2. **Keep the example synthetic and public-safe.** Remove real identifiers, source payloads, secrets, restricted content, and sensitive exact geometry. Synthetic substitution must not preserve a real sensitive linkage.
3. **State one primary defect.** Make the invalid condition recognizable in the filename or payload and explain it in the owning README when the file alone is insufficient.
4. **Declare the expected result.** Use the consumer's established convention for an expected error, `ABSTAIN`, `DENY`, `ERROR`, blocked render, validation failure, or other finite outcome. Do not imply a runtime outcome that has not been tested.
5. **Bind only verified authorities.** Link the applicable contract, schema, policy, validator, test, or consumer when confirmed. Otherwise mark the relationship **NEEDS VERIFICATION**.
6. **Pair stable outputs.** Add a golden or expected-result sidecar only when the consumer's naming and comparison behavior are established and reviewed.
7. **Validate proportionately.** Run the smallest repository-native checks that exercise the fixture. Record what passed, failed, remained pending, or was not run.
8. **Update navigation.** Add the fixture or child lane to the nearest owning README and remove stale routing notes when ownership changes.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Prefer the most specific domain or object-family invalid lane when ownership is clear.
- Make the invalid condition and expected result explicit without conflating the input with proof of the result.
- Pair each stable invalid input with an expected failure output when practical and supported by a verified consumer convention.
- Keep schema validity, semantic validity, source-role validity, evidence resolution, citation validation, rights posture, sensitivity posture, policy filtering, temporal validity, release posture, trust-membrane safety, drawer display, Focus Mode wording, layer-manifest state, UI behavior, correction posture, rollback posture, replay posture, and expected-output state separate.
- Do not treat fixture rejection as evidence closure, policy approval, validator completeness, API implementation proof, UI implementation proof, release state, public-map authority, tile authority, or publication.
- Keep watchers, generators, renderers, and AI systems non-publishing; a fixture cannot promote its own output.

## Expected top-level scenario families

| Scenario family | Preferred lane | Expected posture |
|---|---|---|
| Domain-owned invalid example | Domain-specific `invalid/` or `negative/` lane | Fail-closed output with domain context preserved. |
| Cross-domain invalid example | `fixtures/invalid/` until ownership is resolved | `ABSTAIN`, `DENY`, `ERROR`, validation failure, or review-required. |
| Runtime-wide renderer invalid case | `fixtures/invalid/` or a verified runtime fixture lane | Blocked render or validation failure. |
| Evidence Drawer invalid case | Specific object or domain lane; otherwise `fixtures/invalid/` | Blocked projection or drawer-safe failure. |
| Focus Mode invalid case | Specific domain or focus lane; otherwise `fixtures/invalid/` | `ABSTAIN`, `DENY`, or `ERROR` with a finite posture. |
| Generated-work receipt invalid case | `fixtures/generated_receipt/invalid/` | Schema, policy, integrity, or merge-readiness failure. |
| Stable fail-closed output ready for comparison | `fixtures/golden/` or a domain-specific `golden/` lane | Deterministic expected output, not release or proof. |

## Maintenance checklist

- [ ] The fixture is in the narrowest verified owner lane.
- [ ] The example is synthetic, compact, deterministic, public-safe, and free of secrets or real sensitive linkages.
- [ ] The primary defect and expected result are explicit.
- [ ] Referenced contracts, schemas, policies, validators, tests, and consumers were verified rather than inferred.
- [ ] Missing consumer wiring or implementation remains marked **NEEDS VERIFICATION**.
- [ ] Stable expected output is paired using the consumer's established convention.
- [ ] The nearest README and any affected navigation are current.
- [ ] Relevant checks were run and their bounded results recorded.
- [ ] No fixture is described as evidence, approval, release state, canonical truth, or publication.
- [ ] Correction and rollback paths remain visible when the scenario models consequential or public state.

If a fixture accidentally includes real source material, lifecycle data, proof material, release material, generated CI output, sensitive exact geometry, or private or restricted information, stop using it, route it through the applicable quarantine or responsibility-root process, and record the correction path. Do not rely on deletion alone to resolve a material exposure.

## Verification status

Evidence snapshot for this revision: `main@91a2df5aa12c0a060167bc8b79716caf0f04ee35`.

| Item | Status | Boundary |
|---|---|---|
| Target README baseline | **CONFIRMED** | `fixtures/invalid/README.md` was read at the pinned commit; baseline blob `4cf897379d49eceb2b14a69d3ce1a1c13ed19aa9`. |
| Placement under `fixtures/` | **CONFIRMED** | Aligned with `docs/architecture/directory-rules.md`, `fixtures/README.md`, and `tests/fixtures/README.md` at the pinned commit. |
| Related lanes in the navigation table | **CONFIRMED / NARROWED** | Each linked README was read at the pinned commit; the table is intentionally not an exhaustive domain inventory. |
| Direct child and payload inventory | **NEEDS VERIFICATION** | This README was verified directly; the available connector did not provide an authoritative recursive directory listing. No claim of payload absence is made. |
| Contract, schema, policy, validator, test, runtime, renderer, governed-API, UI, replay, correction, rollback, release, and CI wiring | **NEEDS VERIFICATION** | No complete consumer-to-fixture trace was established by this documentation-only revision. |
| Repository-native tests and validators | **NOT RUN** | Pull-request checks are reported separately from this README and do not establish publication authority. |

