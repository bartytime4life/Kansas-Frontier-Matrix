# Hydrology source fixtures

`fixtures/domains/hydrology/sources/`

Status: draft / fixture lane / synthetic Hydrology source examples.

This directory is for small synthetic Hydrology source-reference, source-descriptor, source-role, admission, rights, sensitivity, cadence, freshness, source-head, activation, and source-family examples. These fixtures help exercise source-registry checks without placing real source records, source payloads, registry authority, or public-use material in the fixture tree.

These files are examples only. They are not source records, lifecycle data, SourceDescriptors, source activation decisions, EvidenceBundles, proof packs, policy decisions, release state, public API material, public map material, public tiles, Hydrology truth, source authority, policy authority, release authority, AI authority, or published artifacts.

## Source fixture posture

Hydrology source fixtures are toy inputs for checks that need source-like shape or source-role behavior. The actual Hydrology source registry is an admission and authority-control lane, not a bibliography. It records identity, role, rights posture, access method, cadence, steward, sensitivity, freshness expectations, attribution requirements, and public-release class before source material can shape public claims.

The canonical source role is set on `SourceDescriptor` at admission and must not be inferred from convenience or upgraded by promotion. Hydrology source-role doctrine specifically warns that regulatory, observed, modeled, aggregate, administrative, candidate, and synthetic roles must not collapse into each other. A fixture may imitate those roles for tests, but it does not create or update any real registry record.

This lane can support future validation and governed-API checks, but examples here do not prove source admission, connector activation, source rights, schema enforcement, policy enforcement, registry storage, EvidenceBundle closure, release integration, UI rendering, or CI coverage by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for runtime fixture inputs and separates it from `tests/fixtures/`, `artifacts/`, and `data/`. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hydrology fixture README is still a greenfield stub during this update.

## Relationship to real source governance

| Lane or document | Relationship |
|---|---|
| `../../../../data/registry/hydrology/sources/` | Existing domain-first Hydrology source registry lane; registry authority is there, not here. |
| `../../../../data/registry/sources/hydrology/` | Source-registry doctrine names this subtype-first pattern as the registry data home; topology remains needs verification where both patterns exist. |
| `../../../../docs/domains/hydrology/SOURCE_REGISTRY.md` | Human-facing Hydrology source-registry doctrine and source-family reference. |
| `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Source-role proof/cannot-prove matrix; fixtures may test it but do not replace it. |
| `../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` | Cross-domain source descriptor meaning and intake posture. |
| `../run_receipt/` | Run receipts may reference toy source descriptor refs for governed-run provenance examples. |
| `../evidence_bundle/` | EvidenceBundle examples may reference toy source refs, but claim support belongs to evidence bundles. |
| `../decision_envelope/` | Decision envelopes may consume source-role outcomes and fail closed when roles or rights are unresolved. |
| `../invalid/` and `../negative/` | Stable or draft source-role, rights, cadence, or admission failures may be cross-linked there. |
| `../golden/` | Stable expected outputs for source fixture inputs may be paired there. |

## Related references

- `../README.md`
- `../run_receipt/README.md`
- `../run_receipt/valid/README.md`
- `../run_receipt/invalid/README.md`
- `../evidence_bundle/README.md`
- `../decision_envelope/README.md`
- `../invalid/README.md`
- `../negative/README.md`
- `../golden/README.md`
- `../../../README.md`
- `../../../../data/registry/hydrology/sources/README.md`
- `../../../../data/registry/sources/hydrology/`
- `../../../../docs/domains/hydrology/SOURCE_REGISTRY.md`
- `../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`
- `../../../../docs/domains/hydrology/SOURCE_FAMILIES.md`
- `../../../../docs/domains/hydrology/DATA_LIFECYCLE.md`
- `../../../../docs/domains/hydrology/API_CONTRACTS.md`
- `../../../../docs/domains/hydrology/BOUNDARY.md`
- `../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`
- `../../../../schemas/contracts/v1/source/`
- `../../../../schemas/contracts/v1/domains/hydrology/`
- `../../../../policy/domains/hydrology/`
- `../../../../policy/sensitivity/hydrology/`
- `../../../../data/proofs/hydrology/`
- `../../../../release/candidates/hydrology/`
- `../../../../release/manifests/hydrology/`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy source descriptor refs, source-family refs, source-role cases, source-head refs, activation-state examples, cadence examples, freshness examples, rights examples, sensitivity examples, attribution examples, and admission-review examples;
- toy source-role examples for observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic role boundaries;
- toy Hydrology source-family examples for USGS water data, WBD/HUC, NHDPlus/3DHP, FEMA NFHL, 3DEP terrain, state water offices, water-quality programs, groundwater networks, historical flood evidence, drought links, and irrigation links;
- toy invalid examples for missing role, unknown rights, unresolved sensitivity, stale source head, source-role collapse, candidate-to-public misuse, descriptor-as-evidence misuse, and registry-as-public-truth misuse;
- paired expected outputs in `../golden/` when behavior becomes stable.

## Exclusions

Do not use this lane for real source records, real source exports, real SourceDescriptors, connector credentials, access tokens, license files, lifecycle data, actual EvidenceBundles, source activation decisions, source ledgers, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, source authority, policy authority, release authority, AI authority, or published artifacts.

## Shared fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy source IDs, toy source-family IDs, toy source descriptor refs, toy access refs, toy rights refs, toy sensitivity labels, toy source-head refs, toy cadence values, toy timestamps, toy digests, and toy reviewer refs.
- Make the source posture explicit: valid, invalid, observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, rights-known, rights-unknown, sensitivity-known, sensitivity-unknown, active, restricted, denied, quarantined, stale, superseded, source-role-preserved, source-role-conflicted, or expected output.
- Pair each stable source fixture with an expected output when practical.
- Keep source admission, source role, source rights, source sensitivity, source cadence, source freshness, source-head identity, connector activation, evidence support, citation validation, policy filtering, release posture, trust-membrane safety, decision-envelope outcome, correction posture, and rollback posture separate.
- Do not treat source fixtures as SourceDescriptors, source-registry entries, EvidenceBundles, source truth, rights approval, policy approval, validator implementation proof, connector implementation proof, API implementation proof, UI implementation proof, release state, public-map authority, or published output.

## Expected fixture families

| Scenario family | Expected posture | Notes |
|---|---|---|
| Toy source descriptor ref with role, rights, sensitivity, cadence, and source-head metadata | Validation pass or review-ready | Real descriptor authority remains in the registry lane. |
| Toy observed streamgage source role | Valid source-role case | Observed role must remain observed and time-scoped. |
| Toy NFHL regulatory source role | Valid regulatory-context case | Regulatory context must not become observed flooding. |
| Toy modeled hydrograph source role | Valid modeled-context case | Modeled role must not become observation. |
| Unknown rights or missing sensitivity label | Review-required, `DENY`, or validation failure | Public use fails closed until resolved. |
| Candidate source routed to public output | `DENY` or validation failure | Candidate material must not become public truth without governed transition. |
| Descriptor treated as evidence support | `ABSTAIN` or validation failure | EvidenceBundle owns claim support. |
| Registry record treated as release approval | `DENY` or release-readiness failure | Release still requires policy and release gates. |

## Maintenance notes

- Update this README when source fixture payloads, child lanes, validators, tests, helper scripts, expected-output names, or source-fixture consumer contracts are added.
- Link each stable fixture to the source-role check, source-descriptor shape check, source-registry check, rights check, sensitivity check, cadence check, freshness check, source-head check, evidence-bundle check, decision-envelope check, run-receipt check, policy check, release-readiness check, or governed-API dry-run that consumes it.
- If expected behavior stabilizes, update the paired input, expected output, consumer notes, `../golden/README.md`, and any specific invalid/negative lane together.
- Keep payloads small enough for normal code review.
- If a fixture accidentally includes real source material or a real source descriptor, move it out of this lane, quarantine it through the governed lifecycle or registry process, and record the correction path.

## Verification status

- Target README: replaced blank placeholder content.
- Fixture payload inventory: no payload files verified in this directory during this update.
- Parent Hydrology fixture README: present but still a greenfield stub during this update.
- Hydrology source-registry alignment: PARTIALLY VERIFIED against `data/registry/hydrology/sources/README.md` and `docs/domains/hydrology/SOURCE_REGISTRY.md`.
- Hydrology source-role alignment: PARTIALLY VERIFIED against `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`.
- SourceDescriptor standard alignment: PARTIALLY VERIFIED against `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`.
- Hydrology run-receipt fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/run_receipt/README.md`.
- Hydrology evidence-bundle fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/evidence_bundle/README.md`.
- Hydrology decision-envelope fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hydrology/decision_envelope/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- Consumer alignment: NEEDS VERIFICATION against validators, source-descriptor checks, source-role checks, source-registry checks, rights checks, sensitivity checks, cadence checks, freshness checks, source-head checks, evidence-bundle checks, decision-envelope checks, run-receipt checks, policy checks, release-readiness checks, schema checks, renderer checks, and UI implementation.
- Tests and validators: NOT RUN.
